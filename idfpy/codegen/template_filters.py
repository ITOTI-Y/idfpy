"""Jinja2 template filters for IDF model code generation.

This module provides filter functions used by idf_model_py.jinja2 template.
These filters are registered with the Jinja2 environment by ModelGenerator.
"""

from __future__ import annotations

import re
import textwrap
from typing import TYPE_CHECKING, Any

from .field_parser import _UNSET, FieldSpec

if TYPE_CHECKING:
    from .schema_parser import ObjectSpec


# ============================================================
# Reference type mapping (set by ModelGenerator before rendering)
# ============================================================

_OBJECT_LIST_REF_TYPES: dict[str, str] = {}
_REFERENCE_CLASS_NAME_GROUPS: set[str] = set()


def set_object_list_ref_types(mapping: dict[str, str]) -> None:
    """Set object_list to reference type mapping.

    Called by ModelGenerator before template rendering.

    Args:
        mapping: Dict mapping object_list names to ref type names.
    """
    global _OBJECT_LIST_REF_TYPES
    _OBJECT_LIST_REF_TYPES = mapping


def set_reference_class_name_groups(groups: set[str]) -> None:
    """Set reference-class-name groups collected from schema.

    Called by ModelGenerator before template rendering.
    """
    global _REFERENCE_CLASS_NAME_GROUPS
    _REFERENCE_CLASS_NAME_GROUPS = groups


def get_ref_type_for_object_list(object_lists: list[str] | None) -> str | None:
    """Get reference type name for object_list(s).

    For fields with multiple object_lists, generates a union type.

    Args:
        object_lists: List of object list names.

    Returns:
        Reference type string or None if no mapping.
        For multiple object_lists: "TypeA | TypeB | TypeC"
    """
    if not object_lists:
        return None

    ref_types = []
    for ol in object_lists:
        ref_type = _OBJECT_LIST_REF_TYPES.get(ol)
        if ref_type:
            ref_types.append(ref_type)

    if not ref_types:
        return None

    # Return union type for multiple object_lists
    return ' | '.join(ref_types)


def python_type_filter(spec: FieldSpec) -> str:
    """Convert FieldSpec to Python type annotation string.

    This filter generates the complete type annotation including `| None`
    suffix for optional fields. For fields with object_list, uses
    reference types instead of plain str.

    Args:
        spec: Field specification to convert.

    Returns:
        Python type annotation as string.

    Examples:
        - number (required) -> "float"
        - number (optional) -> "float | None"
        - string with enum -> 'Literal["A", "B"]'
        - array of numbers -> "list[float]"
        - array of objects -> "list[VertexItem]" (nested class name)
        - string with object_list -> "ZoneNamesRef" or "TypeA | TypeB"
    """
    # Check if field has object_list and should use ref type
    ref_type = get_ref_type_for_object_list(spec.object_list)

    if ref_type:
        is_opt = is_optional_filter(spec)
        if is_opt:
            # Wrap union types in parentheses for clarity
            if ' | ' in ref_type:
                return f'({ref_type}) | None'
            return f'{ref_type} | None'
        return ref_type

    # Original logic for non-reference fields
    base_type = _get_base_type_annotation(spec)
    is_opt = is_optional_filter(spec)

    if is_opt and '| None' not in base_type:
        return f'{base_type} | None'
    return base_type


def _get_base_type_annotation(spec: FieldSpec) -> str:
    """Get base type annotation without optional suffix.

    Args:
        spec: Field specification.

    Returns:
        Base type annotation string.
    """
    if spec.enum_values:
        escaped = [repr(v) for v in spec.enum_values]
        return f'Literal[{", ".join(escaped)}]'

    if spec.anyof_specs:
        has_null = any(s.field_type == 'null' for s in spec.anyof_specs)
        non_null_types = [s for s in spec.anyof_specs if s.field_type != 'null']

        if len(non_null_types) == 1:
            base = _json_type_to_python(non_null_types[0].field_type)
            if non_null_types[0].enum_values:
                escaped = [repr(v) for v in non_null_types[0].enum_values]
                base = f'Literal[{", ".join(escaped)}]'
            return f'{base} | None' if has_null else base

        types = []
        for s in non_null_types:
            if s.enum_values:
                escaped = [repr(v) for v in s.enum_values]
                types.append(f'Literal[{", ".join(escaped)}]')
            else:
                types.append(_json_type_to_python(s.field_type))

        type_str = ' | '.join(types)
        return f'{type_str} | None' if has_null else type_str

    if spec.field_type == 'array':
        if spec.items_spec:
            if spec.items_spec.nested_fields:
                # Check for pre-computed class name (set by extract_nested_classes)
                # Falls back to generating from field name
                item_class = getattr(
                    spec.items_spec,
                    'item_class_name',
                    _generate_nested_class_name(spec.name),
                )
                return f'list[{item_class}]'
            item_type = _json_type_to_python(spec.items_spec.field_type)
            return f'list[{item_type}]'
        return 'list[Any]'

    return _json_type_to_python(spec.field_type)


_JSON_TYPE_TO_PYTHON: dict[str, str] = {
    'number': 'float',
    'integer': 'int',
    'string': 'str',
    'boolean': 'bool',
    'object': 'dict[str, Any]',
    'null': 'None',
    'array': 'list[Any]',
}


def _json_type_to_python(field_type: str) -> str:
    """Map JSON schema type to Python type."""
    return _JSON_TYPE_TO_PYTHON.get(field_type, 'Any')


def _generate_nested_class_name(
    field_name: str, parent_class: str | None = None
) -> str:
    """Generate a class name for nested array item types.

    Args:
        field_name: Original field name (e.g., "vertices").
        parent_class: Optional parent class name for disambiguation.

    Returns:
        PascalCase class name (e.g., "VerticesItem" or "BuildingSurfaceDetailedVerticesItem").
    """
    # Convert field name to PascalCase
    parts = re.split(r'[_\s-]+', field_name)
    pascal = ''.join(p.capitalize() for p in parts if p)

    if parent_class:
        return f'{parent_class}{pascal}Item'
    return f'{pascal}Item'


def extract_nested_classes(
    objects: list[ObjectSpec],
    deduplicate: bool = True,
) -> list[dict[str, Any]]:
    """Extract nested class definitions from object specifications.

    This function scans all objects for array fields with nested object items
    and generates class definitions for them. It also sets the `item_class_name`
    attribute on the `items_spec` so that `python_type_filter` can use it.

    Args:
        objects: List of ObjectSpec instances.
        deduplicate: If True, merge structurally identical nested classes.

    Returns:
        List of nested class dicts with "name" and "fields" keys.
        Also modifies items_spec.item_class_name in-place for type generation.
    """
    nested_classes: list[dict[str, Any]] = []
    seen_structures: dict[str, str] = {}  # structure hash -> class name

    for obj in objects:
        for field in obj.fields:
            if (
                field.field_type == 'array'
                and field.items_spec
                and field.items_spec.nested_fields
            ):
                nested_fields = field.items_spec.nested_fields

                if deduplicate:
                    structure_sig = _get_structure_signature(nested_fields)
                    if structure_sig in seen_structures:
                        field.items_spec.item_class_name = seen_structures[
                            structure_sig
                        ]
                        continue

                class_name = _generate_nested_class_name(field.name, obj.class_name)

                nested_classes.append({'name': class_name, 'fields': nested_fields})

                field.items_spec.item_class_name = class_name

                if deduplicate:
                    seen_structures[structure_sig] = class_name

    return nested_classes


def _get_structure_signature(fields: list[FieldSpec]) -> str:
    """Generate a signature string representing field structure.

    Used for deduplication of structurally identical nested classes.

    Args:
        fields: List of field specifications.

    Returns:
        String signature for comparison.
    """
    if not fields:
        return '<empty>'

    def _get_field_signature(field: FieldSpec) -> str:
        """Build a signature for a single field including constraints/enums."""
        parts: list[str] = [
            f'name={field.name}',
            f'type={field.field_type}',
            f'required={field.required}',
        ]

        if field.enum_values:
            enum_strings = [str(v) for v in field.enum_values]
            parts.append('enum=' + '|'.join(sorted(enum_strings)))
        if field.object_list:
            parts.append('object_list=' + '|'.join(sorted(field.object_list)))
        if field.data_type:
            parts.append(f'data_type={field.data_type}')

        # Numeric constraints
        if field.minimum is not None:
            parts.append(f'min={field.minimum}')
        if field.maximum is not None:
            parts.append(f'max={field.maximum}')
        if field.exclusive_minimum is not None:
            parts.append(f'gt={field.exclusive_minimum}')
        if field.exclusive_maximum is not None:
            parts.append(f'lt={field.exclusive_maximum}')

        # anyOf alternatives
        if field.anyof_specs:
            anyof_sigs = []
            for alt in field.anyof_specs:
                alt_parts = [f'type={alt.field_type}']
                if alt.enum_values:
                    alt_enum_strings = [str(v) for v in alt.enum_values]
                    alt_parts.append('enum=' + '|'.join(sorted(alt_enum_strings)))
                anyof_sigs.append(';'.join(alt_parts))
            parts.append('anyof=' + '|'.join(sorted(anyof_sigs)))

        # Array / nested object descriptors
        if field.items_spec:
            parts.append('items=' + _get_field_signature(field.items_spec))
        if field.nested_fields:
            parts.append('nested=' + _get_structure_signature(field.nested_fields))

        return ';'.join(parts)

    field_signatures = [
        _get_field_signature(f) for f in sorted(fields, key=lambda x: x.name)
    ]
    return '|'.join(field_signatures)


def is_optional_filter(spec: FieldSpec) -> bool:
    """Determine if a field should be optional in the Pydantic model.

    A field is optional if:
    - It has an explicit default value (including None from schema)
    - It is not in the required list
    - It has anyOf with null type

    Args:
        spec: Field specification to check.

    Returns:
        True if the field should be optional.
    """
    # Has explicit default value (including None from schema "default": null)
    if spec.default is not _UNSET:
        return True

    # Not required
    if not spec.required:
        return True

    # anyOf includes null type
    if spec.anyof_specs:
        return any(s.field_type == 'null' for s in spec.anyof_specs)

    return False


def field_definition_filter(spec: FieldSpec) -> str:
    """Generate complete Field(...) definition string.

    Args:
        spec: Field specification.

    Returns:
        Field(...) call as string.

    Examples:
        - Required field: 'Field(...)'
        - With default: 'Field(default=0.0)'
        - With constraints: 'Field(default=1, ge=1)'
        - With metadata: 'Field(default=0.0, json_schema_extra={"units": "m"})'
    """
    args: list[str] = []

    # Default value
    if _has_default(spec):
        default_repr = _format_default_value(spec.default, spec)
        args.append(f'default={default_repr}')
    elif is_optional_filter(spec):
        args.append('default=None')
    else:
        args.append('...')

    # Validation alias for original EnergyPlus schema key names
    if spec.name != spec.python_name:
        args.append(f'validation_alias={spec.name!r}')

    # Numeric constraints
    if spec.minimum is not None:
        args.append(f'ge={spec.minimum}')
    if spec.maximum is not None:
        args.append(f'le={spec.maximum}')
    if spec.exclusive_minimum is not None:
        args.append(f'gt={spec.exclusive_minimum}')
    if spec.exclusive_maximum is not None:
        args.append(f'lt={spec.exclusive_maximum}')

    # Metadata as json_schema_extra
    metadata = _build_metadata(spec)
    if metadata:
        args.append(f'json_schema_extra={metadata!r}')

    return f'Field({", ".join(args)})'


def _has_default(spec: FieldSpec) -> bool:
    """Check if field has an explicit default value.

    Returns True if default was explicitly set in schema (even to null/None).
    _UNSET means no default was specified in schema.

    Args:
        spec: Field specification.

    Returns:
        True if field has an explicit default (including None).
    """
    return spec.default is not _UNSET


def _format_default_value(value: Any, spec: FieldSpec | None = None) -> str:
    """Format default value for Python code.

    Args:
        value: Default value to format.
        spec: Optional field specification for type-aware formatting.

    Returns:
        Python repr string suitable for code generation.
    """
    if isinstance(value, str):
        return repr(value)
    if isinstance(value, bool):
        return 'True' if value else 'False'
    if isinstance(value, (int, float)):
        # Handle schema inconsistency: field_type is string but default is number
        # (e.g., Version.version_identifier has type="string" but default=25.1)
        if spec and spec.field_type == 'string':
            return repr(str(value))

        # Handle case where enum has integer values but default is float
        if spec and isinstance(value, float) and value == int(value):
            # Check direct enum_values
            if spec.enum_values:
                if all(isinstance(v, int) for v in spec.enum_values):
                    return repr(int(value))
            # Check anyof_specs for enum values (for union types)
            elif spec.anyof_specs:
                for anyof_spec in spec.anyof_specs:
                    if anyof_spec.enum_values and all(
                        isinstance(v, int) for v in anyof_spec.enum_values
                    ):
                        return repr(int(value))
        return repr(value)
    if value is None:
        return 'None'
    # For complex types, use repr
    return repr(value)


def _build_metadata(spec: FieldSpec) -> dict[str, Any]:
    """Build metadata dictionary for json_schema_extra.

    Args:
        spec: Field specification.

    Returns:
        Metadata dictionary (empty if no metadata).
    """
    metadata: dict[str, Any] = {}

    if spec.units:
        metadata['units'] = spec.units
    if spec.object_list:
        metadata['object_list'] = spec.object_list
    if spec.note:
        # Truncate long notes
        note = spec.note
        if len(note) > 200:
            note = note[:197] + '...'
        metadata['note'] = note

    return metadata


def format_docstring_filter(text: str | None, width: int = 76) -> str:
    """Format text for use as a docstring.

    Wraps long text and escapes special characters.

    Args:
        text: Raw docstring text.
        width: Maximum line width.

    Returns:
        Formatted docstring text.
    """
    if not text:
        return ''

    # Remove excessive whitespace
    text = ' '.join(text.split())

    # Escape backslashes and quotes
    text = text.replace('\\', '\\\\').replace('"', '\\"')

    # Wrap long lines
    if len(text) <= width:
        return text

    wrapped = textwrap.fill(text, width=width)
    return wrapped


def collect_used_ref_types(objects: list[ObjectSpec]) -> list[str]:
    """Collect all reference types used by objects.

    Scans all fields in objects for object_list references,
    including nested fields in array items.

    Args:
        objects: List of ObjectSpec instances.

    Returns:
        Sorted list of unique reference type names used.
    """
    used_types: set[str] = set()

    def _collect_from_field(field: FieldSpec) -> None:
        """Helper to collect ref types from a single field."""
        if field.object_list:
            for ol in field.object_list:
                ref_type = _OBJECT_LIST_REF_TYPES.get(ol)
                if ref_type:
                    used_types.add(ref_type)

    for obj in objects:
        for field in obj.fields:
            _collect_from_field(field)
            # Also check nested fields in array items
            if (
                field.field_type == 'array'
                and field.items_spec
                and field.items_spec.nested_fields
            ):
                for nested_field in field.items_spec.nested_fields:
                    _collect_from_field(nested_field)

    return sorted(used_types)


def nav_name_filter(spec: FieldSpec) -> str:
    """Derive navigation property name from field name.

    Rules:
    - strip '_name_' segments from the middle of the name
    - field_name ends with '_name' -> strip it: zone_name -> zone
    - field_name ends with '_names' -> strip it
    - otherwise -> append '_ref': outside_layer -> outside_layer_ref

    Verified: 0 collisions with existing fields, Python keywords, or reserved names
    across all consumer fields in the schema.
    """
    name = spec.python_name
    name = name.replace('_name_', '_')
    if name.endswith('_name'):
        return name[:-5]
    if name.endswith('_names'):
        return name[:-6]
    return f'{name}_ref'


def is_class_name_ref_filter(spec: FieldSpec) -> bool:
    """Check if a field's object_list references only reference-class-name groups."""
    if not spec.object_list:
        return False
    return all(ol in _REFERENCE_CLASS_NAME_GROUPS for ol in spec.object_list)


# Registry of all template filters
TEMPLATE_FILTERS: dict[str, Any] = {
    'python_type': python_type_filter,
    'is_optional': is_optional_filter,
    'field_definition': field_definition_filter,
    'format_docstring': format_docstring_filter,
    'nav_name': nav_name_filter,
    'is_class_name_ref': is_class_name_ref_filter,
}
