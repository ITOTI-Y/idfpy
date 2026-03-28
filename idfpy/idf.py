"""Unified IDF class for EnergyPlus file handling.

This module provides the IDF class that integrates object container
and IDF file read/write functionality.
"""

from __future__ import annotations

import json
import subprocess
import sys
import types
from collections.abc import Iterator
from pathlib import Path
from typing import Annotated, Any, Literal, Union, get_args, get_origin

from loguru import logger

from idfpy.models import FIELD_ORDER_REGISTRY, OBJECT_TYPE_REGISTRY, get_model_class
from idfpy.models._base import IDFBaseModel
from idfpy.models.simulation import Version


def _find_list_item_class(annotation: Any) -> type[IDFBaseModel] | None:
    """Extract the IDFBaseModel item class from a list type annotation.

    Handles list[X], list[X] | None, Annotated[list[X], ...], etc.

    Returns:
        The item class if the annotation is a list of IDFBaseModel subclass,
        None otherwise.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is list and args:
        item_type = args[0]
        if isinstance(item_type, type) and issubclass(item_type, IDFBaseModel):
            return item_type
        return None

    if origin is Union or isinstance(annotation, types.UnionType):
        for arg in args:
            result = _find_list_item_class(arg)
            if result is not None:
                return result

    if origin is Annotated and args:
        return _find_list_item_class(args[0])

    return None


def _coerce_numerics(fields: dict[str, Any]) -> dict[str, Any]:
    """Coerce numeric strings to numbers in extensible (list) fields for epJSON."""
    result = {}
    for k, v in fields.items():
        if isinstance(v, list):
            result[k] = [_coerce_list_item(item) for item in v]
        else:
            result[k] = v
    return result


def _coerce_list_item(obj: Any) -> Any:
    """Recursively coerce numeric strings in extensible field items."""
    if isinstance(obj, dict):
        return {k: _coerce_list_item(v) for k, v in obj.items()}
    if isinstance(obj, str):
        try:
            f = float(obj)
            return int(f) if f == int(f) else f
        except ValueError:
            return obj
    return obj


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
        name = getattr(obj, 'name', None) or getattr(
            obj, 'zone_name', None) or ''

        if object_type not in self._objects:
            self._objects[object_type] = {}

        objects = self._objects[object_type]

        if name and name in objects:
            raise ValueError(
                f"Duplicate object: {object_type} '{name}' already exists")

        if not name or name in objects:
            idx = len(objects)
            while f'_{idx}' in objects:
                idx += 1
            name = f'_{idx}'

        objects[name] = obj
        logger.debug(f'Added {object_type}: {name}')

    def get(self, object_type: str, name: str) -> IDFBaseModel | None:
        """Get an object by type and name.

        Args:
            object_type: EnergyPlus object type (e.g., 'Zone').
            name: Object name.

        Returns:
            IDF object or None if not found.
        """
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

    def to_dict(self) -> dict[str, dict[str, dict[str, Any]]]:
        """Convert IDF container to epJSON-style nested dictionary.

        Returns:
            Nested dict: object_type → object_name → fields (without name).
        """
        result: dict[str, dict[str, dict[str, Any]]] = {}
        for object_type, objects in self._objects.items():
            type_dict: dict[str, dict[str, Any]] = {}
            unnamed_counter = 1
            for obj in objects.values():
                fields = obj.model_dump(
                    exclude_none=True, exclude_unset=True, by_alias=True
                )
                fields.pop('name', None)
                # Rename fields using validation_alias where alias is not set
                for field_name, field_info in type(obj).model_fields.items():
                    va = field_info.validation_alias
                    if (
                        isinstance(va, str)
                        and va != field_name
                        and not field_info.alias
                        and field_name in fields
                    ):
                        fields[va] = fields.pop(field_name)
                has_name_field = 'name' in type(obj).model_fields
                name_value = getattr(obj, 'name', None)
                if has_name_field and name_value is not None:
                    obj_name = name_value
                else:
                    while f'{object_type} {unnamed_counter}' in type_dict:
                        unnamed_counter += 1
                    obj_name = f'{object_type} {unnamed_counter}'
                    unnamed_counter += 1
                type_dict[obj_name] = _coerce_numerics(fields)
            result[object_type] = type_dict
        return result

    @classmethod
    def from_dict(cls, data: dict[str, dict[str, dict[str, Any]]]) -> IDF:
        """Construct IDF from epJSON-style nested dictionary.

        Args:
            data: Nested dict: object_type → object_name → fields.

        Returns:
            IDF instance with parsed objects.
        """
        idf = cls()
        for object_type, objects in data.items():
            model_class = get_model_class(object_type)
            if model_class is None:
                logger.warning(f'Unknown object type: {object_type}')
                continue
            for obj_name, fields in objects.items():
                field_dict = dict(fields)
                if 'name' in model_class.model_fields:
                    field_dict['name'] = obj_name
                try:
                    obj = model_class(**field_dict)
                    idf.add(obj)
                except Exception as e:
                    logger.warning(
                        f'Failed to parse {object_type} "{obj_name}": {e}')
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

        content = path.read_text(encoding='utf-8')
        return cls._parse_idf_content(content)

    @classmethod
    def _load_epjson(cls, path: Path) -> IDF:
        """Load epJSON file and parse into object container."""
        content = path.read_text(encoding='utf-8')
        data = json.loads(content)
        return cls.from_dict(data)

    @classmethod
    def _parse_idf_content(cls, content: str) -> IDF:
        """Parse IDF content string into objects.

        Args:
            content: IDF file content.

        Returns:
            IDF instance with parsed objects.
        """
        idf = cls()

        lines = []
        for line in content.splitlines():
            if '!' in line:
                line = line.split('!')[0]
            lines.append(line)

        full_content = '\n'.join(lines)
        object_blocks = full_content.split(';')

        for block in object_blocks:
            block = block.strip()
            if not block:
                continue

            fields = [f.strip() for f in block.split(',')]
            if not fields:
                continue

            object_type = fields[0]
            field_values = fields[1:]

            if object_type not in OBJECT_TYPE_REGISTRY:
                logger.warning(f'Unknown object type: {object_type}')
                continue

            model_class = get_model_class(object_type)
            if model_class is None:
                logger.warning(f'No model class for: {object_type}')
                continue

            field_order = FIELD_ORDER_REGISTRY.get(object_type, [])
            field_dict = cls._build_field_dict(
                model_class, field_order, field_values)

            try:
                obj = model_class(**field_dict)
                idf.add(obj)
            except Exception as e:
                logger.warning(f'Failed to parse {object_type}: {e}')

        return idf

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
            field_info = model_class.model_fields.get(field_name)
            if field_info is not None:
                item_class = _find_list_item_class(field_info.annotation)
                if item_class is not None:
                    # Mark as extensible and start collecting
                    extensible_field_name = field_name
                    extensible_values.append(value)
                    continue

            if value:
                field_dict[field_name] = value

        # Assemble extensible values into list of item dicts
        if extensible_field_name and extensible_values:
            field_info = model_class.model_fields[extensible_field_name]
            item_class = _find_list_item_class(field_info.annotation)
            if item_class is not None:
                item_field_names = list(item_class.model_fields.keys())
                item_field_count = len(item_field_names)

                items: list[dict[str, str]] = []
                for j in range(0, len(extensible_values), item_field_count):
                    chunk = extensible_values[j: j + item_field_count]
                    item_dict = {}
                    for k, v in enumerate(chunk):
                        if k < len(item_field_names) and v:
                            item_dict[item_field_names[k]] = v
                    if item_dict:
                        items.append(item_dict)

                field_dict[extensible_field_name] = items

        return field_dict

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
                f"Invalid output_type '{output_type}'. "
                "Allowed values: 'idf', 'epjson'"
            )

    def _save_idf(self, path: Path) -> None:
        """Save IDF container in IDF text format."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        lines: list[str] = []

        lines.append(
            f'!- Generated by idfpy, EnergyPlus Version {self.version}')
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
        logger.info(f'Saved IDF with {len(self)} objects to {path}')

    def _save_epjson(self, path: Path) -> None:
        """Save IDF container in epJSON format."""
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data = self.to_dict()
        path.write_text(json.dumps(
            data, indent=4, sort_keys=True), encoding='utf-8')
        logger.info(f'Saved epJSON with {len(self)} objects to {path}')

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
        obj_dict = obj.model_dump(by_alias=True)

        # Separate regular fields and extensible fields (like vertices)
        regular_fields: list[tuple[str, str]] = []
        extensible_items: list[dict] = []

        for field_name in field_order:
            value = obj_dict.get(field_name)
            # Check if this is an extensible field (list of vertex items)
            if isinstance(value, list) and value and isinstance(value[0], dict):
                extensible_items = value
            else:
                formatted = self._format_value(value)
                regular_fields.append((field_name, formatted))

        last_non_empty_idx = -1
        for i, (_, value) in enumerate(regular_fields):
            if value:
                last_non_empty_idx = i

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
                vertex_line = self._format_list_item(
                    item, idx + 1, is_last_item)
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
        logger.info(f'Running EnergyPlus: {" ".join(cmd)}')

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
            logger.error(
                f'EnergyPlus simulation failed with return code {return_code}')

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
