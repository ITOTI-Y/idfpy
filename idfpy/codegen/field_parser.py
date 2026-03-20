"""EnergyPlus JSON Schema parser for code generation.

This module parses Energy+.schema.epJSON to extract field and object
specifications for generating type-safe Pydantic models.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

_UNSET = object()


@dataclass
class FieldSpec:
    """EnergyPlus field specification.

    Represents a single field definition extracted from the schema,
    including type information, constraints, and metadata.

    Attributes:
        name: Original field name from schema (e.g., "direction_of_relative_north").
        python_name: Python-compatible name in snake_case.
        field_type: JSON schema type ("number", "string", "integer", "array").
        default: Default value if specified.
        required: Whether the field is required.
        enum_values: List of allowed values for enum fields.
        units: Physical units (e.g., "m", "deg", "W").
        minimum: Minimum allowed value (inclusive).
        maximum: Maximum allowed value (inclusive).
        exclusive_minimum: Exclusive minimum value.
        exclusive_maximum: Exclusive maximum value.
        object_list: Reference to other object types (for object_list fields).
        items_spec: Nested FieldSpec for array item types.
        note: Field description/note from schema.
        data_type: Additional data type hint (e.g., "object_list").
        anyof_specs: List of alternative type specs for anyOf fields.
        nested_fields: List of nested field specs for object fields.
    """

    name: str
    python_name: str
    field_type: str
    default: Any = _UNSET
    required: bool = False
    enum_values: list[str] | None = None
    units: str | None = None
    minimum: float | None = None
    maximum: float | None = None
    exclusive_minimum: float | None = None
    exclusive_maximum: float | None = None
    object_list: list[str] | None = None
    items_spec: FieldSpec | None = None
    item_class_name: str | None = None
    note: str | None = None
    data_type: str | None = None
    anyof_specs: list[FieldSpec] | None = None
    nested_fields: list[FieldSpec] | None = None


class FieldParser:
    """Parser for EnergyPlus schema field definitions.

    Extracts FieldSpec instances from JSON schema field definitions,
    handling various field types including nested objects and arrays.
    """

    _CAMEL_TO_SNAKE_PATTERN = re.compile(r'(?<!^)(?=[A-Z])')

    def parse_field(self, name: str, field_schema: dict[str, Any]) -> FieldSpec:
        """Parse a single field definition from schema.

        Args:
            name: Original field name.
            field_schema: Field definition dictionary from schema.

        Returns:
            Parsed FieldSpec instance.
        """
        python_name = self._to_python_name(name)

        if 'anyOf' in field_schema:
            return self._parse_anyof_field(name, python_name, field_schema)

        field_type = field_schema.get('type', 'string')

        spec = FieldSpec(
            name=name,
            python_name=python_name,
            field_type=field_type,
            default=field_schema.get('default', _UNSET),
            enum_values=field_schema.get('enum'),
            units=field_schema.get('units'),
            minimum=field_schema.get('minimum'),
            maximum=field_schema.get('maximum'),
            exclusive_minimum=field_schema.get('exclusiveMinimum'),
            exclusive_maximum=field_schema.get('exclusiveMaximum'),
            object_list=field_schema.get('object_list'),
            note=field_schema.get('note'),
            data_type=field_schema.get('data_type'),
        )

        if field_type == 'array' and 'items' in field_schema:
            spec.items_spec = self._parse_array_items(field_schema['items'])

        return spec

    def _parse_anyof_field(
        self, name: str, python_name: str, field_schema: dict[str, Any]
    ) -> FieldSpec:
        """Parse a field with anyOf type alternatives.

        Args:
            name: Original field name.
            python_name: Python-compatible field name.
            field_schema: Field definition with anyOf.

        Returns:
            FieldSpec with anyof_specs populated.
        """
        anyof_specs = []
        primary_type = 'string'  # Default fallback

        for alt_schema in field_schema.get('anyOf', []):
            alt_type = alt_schema.get('type', 'string')

            if alt_type != 'null' and primary_type == 'string':
                primary_type = alt_type

            alt_spec = FieldSpec(
                name=name,
                python_name=python_name,
                field_type=alt_type,
                enum_values=alt_schema.get('enum'),
                minimum=alt_schema.get('minimum'),
                maximum=alt_schema.get('maximum'),
            )
            anyof_specs.append(alt_spec)

        return FieldSpec(
            name=name,
            python_name=python_name,
            field_type=primary_type,
            default=field_schema.get('default', _UNSET),
            units=field_schema.get('units'),
            note=field_schema.get('note'),
            anyof_specs=anyof_specs,
        )

    def _parse_array_items(self, items_schema: dict[str, Any]) -> FieldSpec:
        """Parse array items specification.

        Handles nested object definitions within array items,
        such as vertices with x/y/z coordinates.

        Args:
            items_schema: Array items definition from schema.

        Returns:
            FieldSpec representing the array item type.
        """
        item_type = items_schema.get('type', 'object')

        if item_type == 'object' and 'properties' in items_schema:
            nested_fields = []
            required_set = set(items_schema.get('required', []))
            for prop_name, prop_schema in items_schema['properties'].items():
                nested_spec = self.parse_field(prop_name, prop_schema)
                nested_spec.required = prop_name in required_set
                nested_fields.append(nested_spec)

            return FieldSpec(
                name='_item',
                python_name='_item',
                field_type='object',
                nested_fields=nested_fields,
            )

        return FieldSpec(
            name='_item',
            python_name='_item',
            field_type=item_type,
            enum_values=items_schema.get('enum'),
            minimum=items_schema.get('minimum'),
            maximum=items_schema.get('maximum'),
        )

    def _to_python_name(self, name: str) -> str:
        """Convert field name to Python snake_case.

        Args:
            name: Original field name (may contain spaces, hyphens, etc.).

        Returns:
            Python-compatible snake_case name.

        Examples:
            >>> parser = FieldParser()
            >>> parser._to_python_name('direction_of_relative_north')
            'direction_of_relative_north'
            >>> parser._to_python_name('X Origin')
            'x_origin'
            >>> parser._to_python_name('vertex-x-coordinate')
            'vertex_x_coordinate'
            >>> parser._to_python_name('100% Outdoor Air in Cooling')
            'n100_outdoor_air_in_cooling'
        """
        result = name.replace(' ', '_').replace('-', '_')

        result = self._CAMEL_TO_SNAKE_PATTERN.sub('_', result)

        result = result.lower()

        result = re.sub(r'_+', '_', result)

        result = result.strip('_')

        # Python identifiers cannot start with a digit - prefix with 'n'
        if result and result[0].isdigit():
            result = 'n' + result

        return result

    def parse_fields_from_properties(
        self,
        properties: dict[str, Any],
        required_fields: list[str] | None = None,
    ) -> list[FieldSpec]:
        """Parse all fields from a properties dictionary.

        Args:
            properties: Dictionary of field name to field schema.
            required_fields: List of required field names.

        Returns:
            List of parsed FieldSpec instances.
        """
        required_set = set(required_fields or [])
        fields = []

        for name, schema in properties.items():
            spec = self.parse_field(name, schema)
            spec.required = name in required_set
            fields.append(spec)

        return fields


def get_python_type(spec: FieldSpec) -> str:
    """Convert FieldSpec to Python type annotation string.

    Args:
        spec: Field specification to convert.

    Returns:
        Python type annotation as string.

    Examples:
        - number -> float
        - integer -> int
        - string with enum -> Literal["A", "B", "C"]
        - array of objects -> list[VertexType]
    """
    if spec.enum_values:
        escaped = [repr(v) for v in spec.enum_values]
        return f'Literal[{", ".join(escaped)}]'

    if spec.anyof_specs:
        has_null = any(s.field_type == 'null' for s in spec.anyof_specs)
        non_null_types = [s for s in spec.anyof_specs if s.field_type != 'null']

        if len(non_null_types) == 1:
            base_type = _get_base_type(non_null_types[0].field_type)
            return f'{base_type} | None' if has_null else base_type

        types = [_get_base_type(s.field_type) for s in non_null_types]
        type_str = ' | '.join(types)
        return f'{type_str} | None' if has_null else type_str

    if spec.field_type == 'array':
        if spec.items_spec:
            item_type = _get_base_type(spec.items_spec.field_type)
            return f'list[{item_type}]'
        return 'list[Any]'

    return _get_base_type(spec.field_type)


def _get_base_type(field_type: str) -> str:
    type_mapping = {
        'number': 'float',
        'integer': 'int',
        'string': 'str',
        'boolean': 'bool',
        'object': 'dict[str, Any]',
        'null': 'None',
        'array': 'list[Any]',
    }
    return type_mapping.get(field_type, 'Any')


def is_optional_field(spec: FieldSpec) -> bool:
    """Determine if a field should be optional in the Pydantic model.

    A field is optional if:
    - It has a default value
    - It is not in the required list
    - It has anyOf with null type

    Args:
        spec: Field specification to check.

    Returns:
        True if the field should be optional.
    """
    if spec.default is not _UNSET:
        return True

    if not spec.required:
        return True

    if spec.anyof_specs:
        return any(s.field_type == 'null' for s in spec.anyof_specs)

    return False


def get_field_constraints(spec: FieldSpec) -> dict[str, Any]:
    """Extract Pydantic Field constraints from FieldSpec.

    Args:
        spec: Field specification.

    Returns:
        Dictionary of constraint kwargs for pydantic.Field().
    """
    constraints: dict[str, Any] = {}

    if spec.minimum is not None:
        constraints['ge'] = spec.minimum
    if spec.maximum is not None:
        constraints['le'] = spec.maximum
    if spec.exclusive_minimum is not None:
        constraints['gt'] = spec.exclusive_minimum
    if spec.exclusive_maximum is not None:
        constraints['lt'] = spec.exclusive_maximum

    return constraints


def get_field_metadata(spec: FieldSpec) -> dict[str, Any]:
    """Extract metadata for json_schema_extra from FieldSpec.

    Args:
        spec: Field specification.

    Returns:
        Dictionary for json_schema_extra parameter.
    """
    metadata: dict[str, Any] = {}

    if spec.units:
        metadata['units'] = spec.units
    if spec.object_list:
        metadata['object_list'] = spec.object_list
    if spec.note:
        metadata['note'] = spec.note

    return metadata
