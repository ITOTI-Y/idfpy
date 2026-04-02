"""Unified IDF class for EnergyPlus file handling.

This module provides the IDF class that integrates object container
and IDF file read/write functionality.
"""

from __future__ import annotations

import json
import subprocess
import sys
import weakref
from collections.abc import Iterable, Iterator, Mapping
from pathlib import Path
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
    overload,
)

from loguru import logger

from idfpy.models import (
    FIELD_ORDER_REGISTRY,
    OBJECT_TYPE_REGISTRY,
    get_model_class,
)
from idfpy.models._base import IDFBaseModel
from idfpy.models._metadata import get_model_metadata
from idfpy.models._ref_errors import RefError, RefValidationError
from idfpy.models._ref_meta import (
    REF_CLASS_NAME_TYPES,
    REF_GROUP_PROVIDERS,
    REF_PROVIDERS,
)
from idfpy.models.simulation import Version

_T = TypeVar('_T', bound=IDFBaseModel)


def _finalize_fields(
    fields: dict[str, Any],
    obj: IDFBaseModel,
    alias_remap: dict[str, str],
) -> dict[str, Any]:
    """Coerce numerics and apply validation_alias remapping in a single pass."""
    result: dict[str, Any] = {}
    for k, v in fields.items():
        if isinstance(v, list):
            obj_list = getattr(obj, k)
            if v and isinstance(v[0], dict) and obj_list:
                child_remap = get_model_metadata(
                    type(obj_list[0])
                ).validation_alias_remap
                coerced = [
                    _finalize_fields(
                        cast(dict[str, Any], item), obj_list[i], child_remap
                    )
                    if isinstance(item, dict)
                    else item
                    for i, item in enumerate(v)
                ]
            else:
                coerced = v
        else:
            coerced = getattr(obj, k)
        result[alias_remap.get(k, k)] = coerced
    return result


class IDF:
    """EnergyPlus IDF file unified interface.

    Integrates object container and IDF file read/write functionality.
    Reference validation is handled automatically by RefValidator in Pydantic models.

    Attributes:
        _objects: Internal storage mapping object_type -> {name -> object}
    """

    def __init__(self) -> None:
        """Initialize empty IDF container."""
        self._objects: dict[str, dict[str, IDFBaseModel]] = {}
        # ref_group -> {UPPER(name) -> [(object_type, original_name), ...]}
        self._ref_registry: dict[str, dict[str, list[tuple[str, str]]]] = {}
        # Reverse index: ref_group -> UPPER(value) -> [(consumer_obj_type, obj_name)]
        self._reverse_index: dict[str, dict[str, list[tuple[str, str]]]] = {}

    @property
    def version(self) -> str:
        """Get EnergyPlus schema version from Version model default.

        Returns:
            Schema version string (e.g., '25.1').
        """
        default_version = Version()
        return default_version.version_identifier or 'Unknown'

    def add(self, obj: IDFBaseModel) -> None:
        """Add an IDF object to the container.

        For named objects, raises ValueError on duplicate name.
        For nameless objects (no 'name' field or empty name), auto-generates
        a unique internal key with incrementing index.

        Args:
            obj: IDF object instance to add.

        Raises:
            ValueError: If a named object with same type and name already exists.
        """
        object_type = obj.idf_object_type()
        name = ''
        for pf in obj._provider_fields:
            name = getattr(obj, pf, None) or ''
            if name:
                break

        if object_type not in self._objects:
            self._objects[object_type] = {}

        objects = self._objects[object_type]

        if name and name in objects:
            raise ValueError(f"Duplicate object: {object_type} '{name}' already exists")

        if not name or name in objects:
            idx = len(objects)
            while f'_{idx}' in objects:
                idx += 1
            name = f'_{idx}'

        objects[name] = obj
        obj._idf_obj_key = name
        self._bind_recursive(obj)
        self._register_refs(obj)
        self._index_consumer_refs(obj, object_type, name)
        logger.debug('Added {}: {}', object_type, name)

    @overload
    def get(self, object_type: type[_T], name: str) -> _T | None: ...
    @overload
    def get(self, object_type: str, name: str) -> IDFBaseModel | None: ...
    def get(self, object_type: type[_T] | str, name: str) -> _T | IDFBaseModel | None:
        """Get an object by type and name.

        Args:
            object_type: EnergyPlus object type string (e.g., 'Zone')
                or model class (e.g., Zone).
            name: Object name.

        Returns:
            IDF object or None if not found.
        """
        if isinstance(object_type, type):
            object_type = object_type._idf_object_type
        return self._objects.get(object_type, {}).get(name)

    def has(self, object_type: str, name: str) -> bool:
        """Check if an object exists.

        Args:
            object_type: EnergyPlus object type.
            name: Object name.

        Returns:
            True if object exists, False otherwise.
        """
        return name in self._objects.get(object_type, {})

    def _objects_of_type(self, object_type: str) -> dict[str, IDFBaseModel]:
        """Get internal dict for a type (no copy, for internal use only)."""
        return self._objects.get(object_type, {})

    def all_of_type(self, object_type: str) -> dict[str, IDFBaseModel]:
        """Get all objects of a specific type.

        Args:
            object_type: EnergyPlus object type.

        Returns:
            Dictionary mapping name to object, empty dict if type not found.
        """
        return self._objects.get(object_type, {}).copy()

    def __iter__(self) -> Iterator[IDFBaseModel]:
        """Iterate over all objects in the container.

        Yields:
            IDF objects in insertion order by type.
        """
        for objects_by_name in self._objects.values():
            yield from objects_by_name.values()

    def __len__(self) -> int:
        """Return total number of objects.

        Returns:
            Total object count across all types.
        """
        return sum(len(objects) for objects in self._objects.values())

    def remove(self, object_type: str, name: str) -> IDFBaseModel | None:
        """Remove an object and unregister its references.

        Args:
            object_type: EnergyPlus object type.
            name: Object name.

        Returns:
            Removed object, or None if not found.
        """
        obj = self._objects.get(object_type, {}).pop(name, None)
        if obj is not None:
            self._unbind_recursive(obj)
            self._unregister_refs(obj)
            self._unindex_consumer_refs(obj, object_type, name)
            obj._idf_obj_key = ''
        return obj

    # ── Helpers ──────────────────────────────────────────────

    @staticmethod
    def _walk_obj_tree(obj: IDFBaseModel) -> Iterator[IDFBaseModel]:
        """Yield obj and all extensible children (iterative, stack-based)."""
        stack = [obj]
        while stack:
            current = stack.pop()
            yield current
            meta = get_model_metadata(type(current))
            for field_name in meta.list_field_names:
                items = getattr(current, field_name, None)
                if items:
                    stack.extend(
                        item
                        for item in reversed(items)
                        if isinstance(item, IDFBaseModel)
                    )

    @staticmethod
    def _prune_bucket(
        outer: dict[str, dict[str, list]], group: str, key: str, keep: Any
    ) -> None:
        """Filter a bucket list, removing the key if the list becomes empty."""
        bucket = outer.get(group)
        if bucket is None or key not in bucket:
            return
        bucket[key] = [e for e in bucket[key] if keep(e)]
        if not bucket[key]:
            del bucket[key]

    # ── Binding ──────────────────────────────────────────────

    def _bind_recursive(self, obj: IDFBaseModel) -> None:
        """Bind object and its extensible children to this IDF."""
        ref = weakref.ref(self)
        for current in self._walk_obj_tree(obj):
            current._idf_ref = ref

    def _unbind_recursive(self, obj: IDFBaseModel) -> None:
        """Unbind object and its extensible children."""
        for current in self._walk_obj_tree(obj):
            current._idf_ref = None

    # ── Reference registration ───────────────────────────────

    def _register_refs(self, obj: IDFBaseModel) -> None:
        """Register an object's provided references into the registry."""
        object_type = obj.idf_object_type()
        for field_name, ref_groups in REF_PROVIDERS.get(object_type, []):
            value = getattr(obj, field_name, None)
            if not value or not isinstance(value, str):
                continue
            key = value.upper()
            entry = (object_type, value)
            for group in ref_groups:
                self._ref_registry.setdefault(group, {}).setdefault(key, []).append(
                    entry
                )

    def _unregister_refs(self, obj: IDFBaseModel) -> None:
        """Remove an object's provided references from the registry."""
        object_type = obj.idf_object_type()
        for field_name, ref_groups in REF_PROVIDERS.get(object_type, []):
            value = getattr(obj, field_name, None)
            if not value or not isinstance(value, str):
                continue
            key = value.upper()
            entry = (object_type, value)
            for group in ref_groups:
                self._prune_bucket(
                    self._ref_registry, group, key, lambda e, _e=entry: e != _e
                )

    # ── Consumer reverse index ──────────────────────────────

    def _index_consumer_refs(
        self, obj: IDFBaseModel, obj_type: str, obj_name: str
    ) -> None:
        """Index an object's consumer references into the reverse index."""
        for current in self._walk_obj_tree(obj):
            meta = get_model_metadata(type(current))
            for field_name, ref_groups in meta.consumer_fields.items():
                value = getattr(current, field_name, None)
                if not value or not isinstance(value, str):
                    continue
                key = value.upper()
                for group in ref_groups:
                    bucket = self._reverse_index.setdefault(group, {})
                    bucket.setdefault(key, []).append((obj_type, obj_name))

    def _unindex_consumer_refs(
        self, obj: IDFBaseModel, obj_type: str, obj_name: str
    ) -> None:
        """Remove an object's consumer references from the reverse index."""
        entry = (obj_type, obj_name)
        for current in self._walk_obj_tree(obj):
            meta = get_model_metadata(type(current))
            for field_name, ref_groups in meta.consumer_fields.items():
                value = getattr(current, field_name, None)
                if not value or not isinstance(value, str):
                    continue
                key = value.upper()
                for group in ref_groups:
                    self._prune_bucket(
                        self._reverse_index, group, key, lambda e, _e=entry: e != _e
                    )

    # ── Cascade rename ──────────────────────────────────────

    def _before_provider_change(
        self,
        obj: IDFBaseModel,
        field_name: str,
        old_value: str | None,
        new_value: str,
    ) -> None:
        """Prepare index structures before a provider field changes."""
        object_type = obj.idf_object_type()
        old_obj_key = obj._idf_obj_key

        # 0. Conflict check: reject rename if it would overwrite another object
        #    Use case-insensitive comparison (matching _ref_registry/_reverse_index)
        if old_obj_key == old_value or not old_value:
            normalized_new = new_value.upper()
            existing = next(
                (
                    v
                    for k, v in self._objects.get(object_type, {}).items()
                    if k.upper() == normalized_new and v is not obj
                ),
                None,
            )
            if existing is not None:
                raise ValueError(
                    f"Cannot rename {object_type} '{old_value}' to '{new_value}': "
                    f'an object with that name already exists'
                )

        # 1. Tear down old index entries (obj still has old_value)
        self._unregister_refs(obj)
        self._unindex_consumer_refs(obj, object_type, old_obj_key)

        # 2-4. Cascade only when old_value is a real name
        if old_value:
            # 2. Determine affected ref groups
            affected_groups: set[str] = set()
            for fn, groups in REF_PROVIDERS.get(object_type, []):
                if fn == field_name:
                    affected_groups.update(groups)

            # 3. Cascade: update consumer reference fields
            old_key = old_value.upper()
            new_key = new_value.upper()
            for group in affected_groups:
                bucket = self._reverse_index.get(group, {})
                for consumer_type, consumer_name in list(bucket.get(old_key, [])):
                    consumer = self._objects.get(consumer_type, {}).get(consumer_name)
                    if consumer is not None:
                        self._cascade_consumer_fields(
                            consumer,
                            old_key,
                            new_value,
                            affected_groups,
                        )
                # 4. Move reverse_index bucket key
                entries = bucket.pop(old_key, [])
                if entries:
                    bucket.setdefault(new_key, []).extend(entries)

        # 5. Update _objects key when provider field is the key source
        if old_obj_key == old_value or not old_value:
            objs = self._objects.get(object_type, {})
            if old_obj_key in objs:
                objs[new_value] = objs.pop(old_obj_key)
                obj._idf_obj_key = new_value

    def _after_provider_change(
        self,
        obj: IDFBaseModel,
        field_name: str,
        new_value: str,
    ) -> None:
        """Rebuild index structures after a provider field has changed."""
        object_type = obj.idf_object_type()
        self._register_refs(obj)
        self._index_consumer_refs(obj, object_type, obj._idf_obj_key)

    def _cascade_consumer_fields(
        self,
        consumer: IDFBaseModel,
        old_key: str,
        new_value: str,
        affected_groups: set[str],
    ) -> None:
        """Update consumer reference fields that point to old_key."""
        for current in self._walk_obj_tree(consumer):
            meta = get_model_metadata(type(current))
            for field_name, field_groups in meta.consumer_fields.items():
                if not affected_groups.intersection(field_groups):
                    continue
                val = getattr(current, field_name, None)
                if isinstance(val, str) and val.upper() == old_key:
                    setattr(current, field_name, new_value)

    # ── Forward resolution ───────────────────────────────────

    def _resolve_forward(
        self,
        value: str,
        ref_groups: list[str],
        expected_type: str | None = None,
    ) -> IDFBaseModel | None:
        """Resolve a reference string to the target object.

        Uses _ref_registry for O(1) type + original_name determination,
        then direct dict lookup in _objects.

        Args:
            value: The reference name string.
            ref_groups: Candidate reference groups to search.
            expected_type: If provided, only match providers of this
                object type (e.g. ``"Zone"``).  When *None* the first
                candidate found is returned (backward-compatible).
        """
        key = value.upper()
        for group in ref_groups:
            candidates = self._ref_registry.get(group, {}).get(key)
            if candidates is None:
                continue
            for obj_type, original_name in candidates:
                if expected_type is not None and obj_type != expected_type:
                    continue
                obj = self._objects.get(obj_type, {}).get(original_name)
                if obj is not None:
                    return obj
        return None

    # ── Reverse navigation ───────────────────────────────────

    def _find_referencing(
        self,
        target: IDFBaseModel,
        consumer_type: str | None = None,
    ) -> list[IDFBaseModel]:
        """Find objects that reference target, optionally filtered by type.

        Uses _reverse_index for O(R) lookup where R = referencing objects.
        """
        provisions = self._target_provisions(target)
        if not provisions:
            return []

        seen: set[tuple[str, str]] = set()
        results: list[IDFBaseModel] = []
        for group, key in provisions:
            bucket = self._reverse_index.get(group, {})
            for entry_type, entry_name in bucket.get(key, ()):
                if consumer_type is not None and entry_type != consumer_type:
                    continue
                pair = (entry_type, entry_name)
                if pair not in seen:
                    seen.add(pair)
                    obj = self._objects.get(entry_type, {}).get(entry_name)
                    if obj is not None:
                        results.append(obj)
        return results

    @staticmethod
    def _target_provisions(target: IDFBaseModel) -> list[tuple[str, str]]:
        """Collect (group, UPPER(value)) pairs that target provides."""
        target_type = target.idf_object_type()
        provisions: list[tuple[str, str]] = []
        for field_name, groups in REF_PROVIDERS.get(target_type, []):
            val = getattr(target, field_name, None)
            if val and isinstance(val, str):
                key = val.upper()
                for group in groups:
                    provisions.append((group, key))
        return provisions

    # ── Validation ───────────────────────────────────────────

    def validate(self) -> list[RefError]:
        """Validate all cross-object references.

        Checks:
        1. Existence: referenced name exists in at least one ref group
        2. Type compatibility: provider type is valid for the matched group

        Multiple object_list groups per field have OR semantics.
        """
        errors: list[RefError] = []
        for objects_by_name in self._objects.values():
            for key, obj in objects_by_name.items():
                self._validate_obj_refs(key, obj, errors)
        return errors

    def validate_or_raise(self) -> None:
        """Validate references, raise RefValidationError if broken."""
        errors = self.validate()
        if errors:
            raise RefValidationError(errors)

    def _validate_obj_refs(
        self,
        key: str,
        obj: IDFBaseModel,
        errors: list[RefError],
    ) -> None:
        """Check one object's reference fields against the registry."""
        object_type = obj.idf_object_type()
        object_name = key or ''

        for current in self._walk_obj_tree(obj):
            meta = get_model_metadata(type(current))
            for field_name, ref_groups in meta.consumer_fields.items():
                value = getattr(current, field_name, None)
                if value is None or not isinstance(value, str):
                    continue
                self._check_ref(
                    object_type,
                    object_name,
                    field_name,
                    value,
                    ref_groups,
                    errors,
                )

    def _check_ref(
        self,
        object_type: str,
        object_name: str,
        field_name: str,
        value: str,
        ref_groups: list[str],
        errors: list[RefError],
    ) -> None:
        """Check a single reference value against its ref groups.

        Multiple ref_groups have OR semantics (186 fields affected).
        A value is valid if found in ANY of the groups.
        """
        key = value.upper()

        def _append_missing() -> None:
            all_groups = ', '.join(ref_groups)
            errors.append(
                RefError(
                    object_type=object_type,
                    object_name=object_name,
                    field_name=field_name,
                    ref_group=all_groups,
                    referenced_name=value,
                    error_type='missing',
                    detail=f'"{value}" not found in any of [{all_groups}]',
                )
            )

        # Phase 0: check reference-class-name groups (static type name validation)
        # These groups contain object TYPE names, not instance names.
        registry_groups: list[str] = []
        for group in ref_groups:
            valid_types = REF_CLASS_NAME_TYPES.get(group)
            if valid_types is not None:
                if key in valid_types:
                    return  # Found in static type set — valid
            else:
                registry_groups.append(group)

        # All groups were reference-class-name but none matched
        if not registry_groups:
            _append_missing()
            return

        # Phase 1: find the value in any registry-based group
        found_in_group: str | None = None
        found_provider_types: list[str] = []
        for group in registry_groups:
            candidates = self._ref_registry.get(group, {}).get(key)
            if candidates:
                found_in_group = group
                found_provider_types = [c[0] for c in candidates]
                break

        # Not found in ANY group -> missing
        if found_in_group is None:
            _append_missing()
            return

        # Phase 2: type compatibility – at least one provider must be allowed
        allowed_types = REF_GROUP_PROVIDERS.get(found_in_group)
        if allowed_types:
            valid = [t for t in found_provider_types if t in allowed_types]
            if not valid:
                errors.append(
                    RefError(
                        object_type=object_type,
                        object_name=object_name,
                        field_name=field_name,
                        ref_group=found_in_group,
                        referenced_name=value,
                        error_type='type_mismatch',
                        detail=(
                            f'"{value}" is provided by '
                            f'{sorted(set(found_provider_types))}, '
                            f'but {found_in_group} only accepts '
                            f'{sorted(allowed_types)}'
                        ),
                    )
                )

    def to_dict(self) -> dict[str, dict[str, dict[str, Any]]]:
        """Convert IDF container to epJSON-style nested dictionary.

        Returns:
            Nested dict: object_type → object_name → fields (without name).
        """
        result: dict[str, dict[str, dict[str, Any]]] = {}
        for object_type, objects in self._objects.items():
            type_dict: dict[str, dict[str, Any]] = {}
            unnamed_counter = 1
            meta = None
            for obj in objects.values():
                if meta is None:
                    meta = get_model_metadata(type(obj))
                fields = obj.model_dump(
                    exclude_none=True, exclude_unset=True, by_alias=True
                )
                fields.pop('name', None)
                fields = _finalize_fields(fields, obj, meta.validation_alias_remap)
                name_value = getattr(obj, 'name', None)
                if meta.has_name_field and name_value not in (None, ''):
                    obj_name = name_value
                else:
                    while f'{object_type} {unnamed_counter}' in type_dict:
                        unnamed_counter += 1
                    obj_name = f'{object_type} {unnamed_counter}'
                    unnamed_counter += 1
                type_dict[obj_name] = fields
            result[object_type] = type_dict
        return result

    @classmethod
    def from_dict(cls, data: dict[str, dict[str, dict[str, Any]]]) -> IDF:
        """Construct IDF from epJSON-style nested dictionary.

        Args:
            data: Nested dict: object_type → object_name → fields.

        Returns:
            IDF instance with parsed objects.

        Raises:
            ValueError: If *data* is not a dict, any object-type value is not
                a dict, or any fields entry is not a mapping.
        """
        if not isinstance(data, dict):
            raise ValueError(
                f'from_dict expects a top-level dict, got {type(data).__name__}'
            )

        idf = cls()
        for object_type, objects in data.items():
            if not isinstance(objects, dict):
                raise ValueError(
                    f'Expected a dict of objects for object type '
                    f'"{object_type}", got {type(objects).__name__}'
                )
            model_class = get_model_class(object_type)
            if model_class is None:
                logger.warning('Unknown object type: {}', object_type)
                continue
            for obj_name, fields in objects.items():
                if not isinstance(fields, Mapping):
                    raise ValueError(
                        f'Expected a mapping of fields for {object_type} '
                        f'"{obj_name}", got {type(fields).__name__}'
                    )
                field_dict = dict(fields)
                if 'name' in model_class.model_fields:
                    field_dict['name'] = obj_name
                try:
                    obj = model_class(**field_dict)
                    idf.add(obj)
                except Exception as e:
                    logger.warning(
                        'Failed to parse {} "{}": {}', object_type, obj_name, e
                    )
        return idf

    @classmethod
    def load(cls, path: Path) -> IDF:
        """Load IDF/epJSON file and parse into object container.

        File format is auto-detected by extension:
        - .epjson / .json → epJSON format
        - others → IDF text format

        Objects that fail validation are skipped with a warning log.

        Args:
            path: Path to IDF or epJSON file.

        Returns:
            IDF instance with successfully parsed objects.

        Raises:
            FileNotFoundError: If file does not exist.
        """
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f'IDF file not found: {path}')

        if path.suffix.lower() in ('.epjson', '.json'):
            return cls._load_epjson(path)

        with path.open(encoding='utf-8') as f:
            return cls._parse_idf_content(f)

    @classmethod
    def _load_epjson(cls, path: Path) -> IDF:
        """Load epJSON file and parse into object container."""
        content = path.read_text(encoding='utf-8')
        data = json.loads(content)
        return cls.from_dict(data)

    @classmethod
    def _parse_idf_content(cls, lines: str | Iterable[str]) -> IDF:
        """Parse IDF content from a string or line iterator.

        Single-pass parser: accumulates text chunks line by line,
        processes each complete object block when ';' is encountered.
        Accepts a string (split by lines) or any line iterable (file object,
        list of strings, etc.) for streaming support.
        """
        if isinstance(lines, str):
            lines = lines.splitlines()

        idf = cls()
        chunks: list[str] = []  # accumulated text between ';' terminators

        for raw_line in lines:
            # Strip comments
            bang = raw_line.find('!')
            line = raw_line[:bang] if bang >= 0 else raw_line
            line = line.strip()
            if not line:
                continue

            # Consume all ';'-terminated objects on this line
            semi = line.find(';')
            if semi < 0:
                chunks.append(line)
                continue

            while semi >= 0:
                before = line[:semi].strip()
                if before:
                    chunks.append(before)

                if chunks:
                    block = ' '.join(chunks)
                    fields = [f.strip() for f in block.split(',')]
                    if fields and fields[0]:
                        cls._process_block(idf, fields)
                    chunks = []

                line = line[semi + 1 :]
                semi = line.find(';')

            remainder = line.strip()
            if remainder:
                chunks.append(remainder)

        # Handle trailing block without terminator
        if chunks:
            block = ' '.join(chunks)
            fields = [f.strip() for f in block.split(',')]
            if fields and fields[0]:
                cls._process_block(idf, fields)

        return idf

    @classmethod
    def _process_block(cls, idf: IDF, fields: list[str]) -> None:
        """Parse a single object block from accumulated fields."""
        object_type = fields[0]
        field_values = fields[1:]

        if object_type not in OBJECT_TYPE_REGISTRY:
            logger.warning('Unknown object type: {}', object_type)
            return

        model_class = get_model_class(object_type)
        if model_class is None:
            logger.warning('No model class for: {}', object_type)
            return

        field_order = FIELD_ORDER_REGISTRY.get(object_type, [])
        field_dict = cls._build_field_dict(model_class, field_order, field_values)

        try:
            obj = model_class(**field_dict)
            idf.add(obj)
        except Exception as e:
            logger.warning('Failed to parse {}: {}', object_type, e)

    @classmethod
    def _build_field_dict(
        cls,
        model_class: type[IDFBaseModel],
        field_order: list[str],
        field_values: list[str],
    ) -> dict[str, Any]:
        """Build a field dictionary from positional IDF values.

        Handles both regular fields and extensible (list) fields.
        All values are kept as strings — Pydantic handles type coercion.

        Args:
            model_class: The Pydantic model class for this object type.
            field_order: Ordered list of field names from the registry.
            field_values: Raw string values from IDF parsing.

        Returns:
            Dictionary mapping field names to values, ready for model construction.
        """
        meta = get_model_metadata(model_class)
        field_dict: dict[str, Any] = {}
        extensible_field_name: str | None = None
        extensible_values: list[str] = []

        for i, value in enumerate(field_values):
            # Once we've hit an extensible field, collect all remaining values
            # (keep empty values to preserve positional mapping)
            if extensible_field_name is not None:
                extensible_values.append(value)
                continue

            if i >= len(field_order):
                break

            field_name = field_order[i]

            # Check if this field is an extensible (list) type
            if field_name in meta.list_item_classes:
                extensible_field_name = field_name
                extensible_values.append(value)
                continue

            if value:
                # Normalize autosize/autocalculate to match model's Literal
                lower = value.lower()
                if lower in ('autosize', 'autocalculate'):
                    value = cls._resolve_auto_keyword(
                        lower, meta.literal_case_maps.get(field_name, {})
                    )
                field_dict[field_name] = value

        # Assemble extensible values into list of item dicts
        if extensible_field_name and extensible_values:
            item_field_names = meta.list_item_field_names.get(extensible_field_name)
            if item_field_names is not None:
                item_field_count = len(item_field_names)

                items: list[dict[str, str]] = []
                for j in range(0, len(extensible_values), item_field_count):
                    chunk = extensible_values[j : j + item_field_count]
                    item_dict = {}
                    for k, v in enumerate(chunk):
                        if k < len(item_field_names) and v:
                            item_dict[item_field_names[k]] = v
                    if item_dict:
                        items.append(item_dict)

                field_dict[extensible_field_name] = items

        return field_dict

    @staticmethod
    def _resolve_auto_keyword(lower_value: str, case_map: dict[str, str | int]) -> str:
        """Resolve autosize/autocalculate to the keyword the model expects.

        EnergyPlus IDF files may use Autosize and Autocalculate
        interchangeably. This method checks the field's literal case map
        and returns whichever keyword is accepted.
        """
        # Exact match (e.g., 'autosize' → 'Autosize')
        matched = case_map.get(lower_value)
        if isinstance(matched, str):
            return matched
        # Cross-map: autosize ↔ autocalculate
        other = 'autocalculate' if lower_value == 'autosize' else 'autosize'
        matched = case_map.get(other)
        if isinstance(matched, str):
            return matched
        # Fallback: capitalize
        return lower_value.capitalize()

    def save(self, path: Path, output_type: Literal['idf', 'epjson'] = 'idf') -> None:
        """Save IDF container to file.

        Args:
            path: Output file path.
            output_type: Output format, 'idf' or 'epjson'.
        """
        if output_type == 'epjson':
            self._save_epjson(path)
        elif output_type == 'idf':
            self._save_idf(path)
        else:
            raise ValueError(
                f"Invalid output_type '{output_type}'. Allowed values: 'idf', 'epjson'"
            )

    def _save_idf(self, path: Path) -> None:
        """Save IDF container in IDF text format."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines: list[str] = []

        lines.append(f'!- Generated by idfpy, EnergyPlus Version {self.version}')
        lines.append('')

        for object_type in sorted(self._objects.keys()):
            objects = self._objects[object_type]
            if not objects:
                continue

            lines.append(f'!- =========== {object_type} ===========')
            lines.append('')

            field_order = FIELD_ORDER_REGISTRY.get(object_type, [])

            for obj in objects.values():
                obj_lines = self._format_object(obj, object_type, field_order)
                lines.extend(obj_lines)
                lines.append('')

        path.write_text('\n'.join(lines), encoding='utf-8')
        logger.info('Saved IDF with {} objects to {}', len(self), path)

    def _save_epjson(self, path: Path) -> None:
        """Save IDF container in epJSON format."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = self.to_dict()
        path.write_text(json.dumps(data, indent=4, sort_keys=True), encoding='utf-8')
        logger.info('Saved epJSON with {} objects to {}', len(self), path)

    def _format_object(
        self,
        obj: IDFBaseModel,
        object_type: str,
        field_order: list[str],
    ) -> list[str]:
        """Format a single object for IDF output.

        IDF format requires positional fields, so we must output all fields
        up to the last non-empty field (including empty intermediate fields).

        Handles extensible fields like 'vertices' by expanding each item's
        coordinates into separate lines.

        Args:
            obj: IDF object to format.
            object_type: Object type name.
            field_order: Ordered list of field names.

        Returns:
            List of formatted lines for the object.
        """
        lines: list[str] = []
        meta = get_model_metadata(type(obj))

        # Separate regular fields and extensible fields; track last non-empty
        regular_fields: list[tuple[str, str]] = []
        extensible_items: list[dict] = []
        last_non_empty_idx = -1

        for field_name in field_order:
            if field_name in meta.list_field_names:
                items = getattr(obj, field_name, None)
                if items:
                    extensible_items = [
                        item.model_dump(by_alias=True) for item in items
                    ]
            else:
                value = getattr(obj, field_name, None)
                formatted = self._format_value(value)
                regular_fields.append((field_name, formatted))
                if formatted:
                    last_non_empty_idx = len(regular_fields) - 1

        if last_non_empty_idx < 0 and not extensible_items:
            lines.append(f'{object_type};')
            return lines

        lines.append(f'{object_type},')

        if extensible_items:
            fields_to_output = regular_fields
        else:
            fields_to_output = regular_fields[: last_non_empty_idx + 1]

        for i, (field_name, value) in enumerate(fields_to_output):
            is_last = i == len(fields_to_output) - 1 and not extensible_items
            terminator = ';' if is_last else ','
            comment = f'!- {field_name}'
            lines.append(f'    {value}{terminator}  {comment}')

        if extensible_items:
            for idx, item in enumerate(extensible_items):
                is_last_item = idx == len(extensible_items) - 1
                vertex_line = self._format_list_item(item, idx + 1, is_last_item)
                lines.extend(vertex_line)

        return lines

    def _format_list_item(self, item: dict, item_num: int, is_last: bool) -> list[str]:
        """Format a single list item for IDF output.

        Args:
            item: Dictionary with item keys.
            item_num: 1-based item number for comment.
            is_last: Whether this is the last vertex.

        Returns:
            Formatted item lines.
        """
        result = []
        for i, (name, value) in enumerate(item.items()):
            terminator = ';' if is_last and i == len(item) - 1 else ','
            value_str = self._format_value(value)
            comment = f'!- {name}_{item_num}'
            result.append(f'    {value_str}{terminator}  {comment}')

        return result

    def run(
        self,
        idf_path: Path,
        weather_path: Path,
        output_dir: Path | None = None,
        energyplus_bin: str = 'energyplus',
    ) -> int:
        """Run EnergyPlus simulation with real-time terminal output.

        Args:
            idf_path: Path to IDF file.
            weather_path: Path to EPW weather file.
            output_dir: Output directory for simulation results. Defaults to idf_path parent.
            energyplus_bin: Path to EnergyPlus executable.

        Returns:
            EnergyPlus process return code.
        """
        idf_path = Path(idf_path)
        weather_path = Path(weather_path)
        if not weather_path.exists():
            raise FileNotFoundError(f'Weather file not found: {weather_path}')
        if not idf_path.exists():
            raise FileNotFoundError(f'IDF file not found: {idf_path}')
        if output_dir is None:
            output_dir = idf_path.parent

        output_dir.mkdir(parents=True, exist_ok=True)

        cmd = [
            energyplus_bin,
            '-x',
            '-w',
            str(weather_path),
            '-d',
            str(output_dir),
            str(idf_path),
        ]
        logger.info('Running EnergyPlus: {}', ' '.join(cmd))

        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )

        if process.stdout is None:
            raise RuntimeError('Failed to capture EnergyPlus output')
        for line in process.stdout:
            sys.stdout.write(line)
            sys.stdout.flush()

        return_code = process.wait()

        if return_code == 0:
            logger.info('EnergyPlus simulation completed successfully')
        else:
            logger.error('EnergyPlus simulation failed with return code {}', return_code)

        return return_code

    @staticmethod
    def _format_value(value: object) -> str:
        """Format a value for IDF output.

        Args:
            value: Value to format.

        Returns:
            Formatted string value.
        """
        if value is None:
            return ''
        if isinstance(value, bool):
            return 'Yes' if value else 'No'
        if isinstance(value, float):
            return f'{value:.12g}'
        return str(value)
