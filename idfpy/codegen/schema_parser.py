"""EnergyPlus JSON Schema parser for code generation.

This module parses Energy+.schema.epJSON to extract field and object
specifications for generating type-safe Pydantic models.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from loguru import logger

from .field_parser import FieldParser, FieldSpec


@dataclass
class ObjectSpec:
    """EnergyPlus object specification.

    Represents a complete object type definition from the schema,
    including all fields and metadata.

    Attributes:
        name: Original object type name (e.g., "BuildingSurface:Detailed").
        class_name: Python class name in PascalCase (e.g., "BuildingSurfaceDetailed").
        group: EnergyPlus group category (e.g., "Thermal Zones and Surfaces").
        fields: List of field specifications for this object.
        memo: Object description/documentation from schema.
        min_fields: Minimum number of fields required.
        max_fields: Maximum number of fields allowed.
        extensible_size: Size of extensible field groups (if any).
        format: Output format hint (e.g., "vertices", "singleLine").
    """

    name: str
    class_name: str
    group: str
    fields: list[FieldSpec] = field(default_factory=list)
    memo: str | None = None
    min_fields: int | None = None
    max_fields: int | None = None
    extensible_size: int | None = None
    format: str | None = None


class SchemaParser:
    """Parser for Energy+.schema.epJSON files.

    Parses the complete EnergyPlus JSON schema to extract all object
    type definitions as ObjectSpec instances.

    Example:
        >>> parser = SchemaParser(Path('Energy+.schema.epJSON'))
        >>> specs = parser.parse()
        >>> zone_spec = specs.get('Zone')
        >>> print(zone_spec.class_name)  # "Zone"
        >>> print(len(zone_spec.fields))  # Number of fields
    """

    _NON_ALNUM_PATTERN = re.compile(r'[^a-zA-Z0-9]+')
    _ACRONYM_PATTERNS: dict[str, re.Pattern[str]] = {
        acronym: re.compile(acronym, re.IGNORECASE)
        for acronym in ['HVAC', 'VAV', 'CAV', 'VRF', 'DX', 'AHU', 'FCU', 'DOAS']
    }

    def __init__(self, schema_path: Path):
        """Initialize the schema parser.

        Args:
            schema_path: Path to Energy+.schema.epJSON file.

        Raises:
            FileNotFoundError: If schema file does not exist.
        """
        self.schema_path = Path(schema_path)
        if not self.schema_path.exists():
            raise FileNotFoundError(f'Schema file not found: {schema_path}')

        self._raw_schema: dict[str, Any] | None = None
        self._field_parser = FieldParser()
        self._cached_specs: dict[str, ObjectSpec] | None = None

    def parse(self) -> dict[str, ObjectSpec]:
        """Parse the schema and return all object specifications.

        Returns:
            Dictionary mapping object type names to ObjectSpec instances.
            Keys are original names like "BuildingSurface:Detailed".

        Raises:
            ValueError: If schema format is invalid.
        """
        if self._cached_specs is not None:
            return self._cached_specs

        self._load_schema()

        if self._raw_schema is None:
            raise ValueError('Schema not loaded')

        properties = self._raw_schema.get('properties', {})
        if not properties:
            raise ValueError("No 'properties' found in schema")

        specs: dict[str, ObjectSpec] = {}
        total = len(properties)

        logger.info(f'Parsing {total} object types from schema...')

        for i, (name, obj_schema) in enumerate(properties.items(), 1):
            try:
                spec = self._parse_object(name, obj_schema)
                specs[name] = spec

                if i % 100 == 0:
                    logger.debug(f'Parsed {i}/{total} object types...')

            except Exception as e:
                logger.warning(f"Failed to parse object '{name}': {e}")
                continue

        logger.info(f'Successfully parsed {len(specs)}/{total} object types')
        self._cached_specs = specs
        return specs

    def _load_schema(self) -> None:
        """Load and cache the raw schema JSON."""
        if self._raw_schema is not None:
            return

        logger.debug(f'Loading schema from {self.schema_path}')
        content = self.schema_path.read_text(encoding='utf-8')
        self._raw_schema = json.loads(content)

        version = self._raw_schema.get('epJSON_schema_version', 'unknown')
        logger.info(f'Loaded EnergyPlus schema version: {version}')

    def _parse_object(self, name: str, obj_schema: dict[str, Any]) -> ObjectSpec:
        """Parse a single object type definition.

        Args:
            name: Object type name (e.g., "Zone", "BuildingSurface:Detailed").
            obj_schema: Object definition dictionary from schema.

        Returns:
            Parsed ObjectSpec instance.
        """
        class_name = self._to_class_name(name)
        group = obj_schema.get('group', 'Uncategorized')

        # Extract object-level metadata
        memo = obj_schema.get('memo')
        min_fields = obj_schema.get('min_fields')
        max_fields = obj_schema.get('max_fields')
        extensible_size = obj_schema.get('extensible_size')
        format_hint = obj_schema.get('format')

        # Fields are nested under patternProperties.*.properties
        # or directly under legacy_idd.fields for some objects
        fields = self._extract_fields(obj_schema)

        return ObjectSpec(
            name=name,
            class_name=class_name,
            group=group,
            fields=fields,
            memo=memo,
            min_fields=min_fields,
            max_fields=max_fields,
            extensible_size=extensible_size,
            format=format_hint,
        )

    def _extract_fields(self, obj_schema: dict[str, Any]) -> list[FieldSpec]:
        """Extract field specifications from object schema.

        The schema has a nested structure where fields are under:
        patternProperties -> ".*" (or similar pattern) -> properties

        Additionally, the top-level "name" property (if present) describes the
        object instance name and should be included as the first field.

        Args:
            obj_schema: Object definition dictionary.

        Returns:
            List of FieldSpec instances for all fields.
        """
        fields: list[FieldSpec] = []

        # Extract top-level "name" property if present
        # This is the object instance name (e.g., "Zone1" for a Zone object)
        name_schema = obj_schema.get('name')
        if name_schema and isinstance(name_schema, dict):
            name_field = self._field_parser.parse_field('name', name_schema)
            # is_required in schema means the field is required
            name_field.required = name_schema.get('is_required', False)
            fields.append(name_field)

        # Primary location: patternProperties.*.properties
        pattern_props = obj_schema.get('patternProperties', {})

        for _pattern, pattern_schema in pattern_props.items():
            # The pattern is usually ".*" or "^.*\\S.*$"
            if 'properties' in pattern_schema:
                properties = pattern_schema['properties']
                required = pattern_schema.get('required', [])
                fields.extend(
                    self._field_parser.parse_fields_from_properties(
                        properties, required
                    )
                )
                return fields

        # Fallback: Some objects may have properties directly
        if 'properties' in obj_schema:
            properties = obj_schema['properties']
            required = obj_schema.get('required', [])
            fields.extend(
                self._field_parser.parse_fields_from_properties(properties, required)
            )
            return fields

        # Return fields (may only contain name field or be empty)
        if not fields:
            logger.debug('No fields found in object schema')
        return fields

    def _to_class_name(self, name: str) -> str:
        """Convert object type name to Python PascalCase class name.

        Args:
            name: Original object name (e.g., "BuildingSurface:Detailed").

        Returns:
            PascalCase class name (e.g., "BuildingSurfaceDetailed").

        Examples:
            >>> parser = SchemaParser(Path('schema.json'))
            >>> parser._to_class_name('Zone')
            'Zone'
            >>> parser._to_class_name('BuildingSurface:Detailed')
            'BuildingSurfaceDetailed'
            >>> parser._to_class_name('Site:Location')
            'SiteLocation'
            >>> parser._to_class_name('ZoneHVAC:FourPipeFanCoil')
            'ZoneHVACFourPipeFanCoil'
        """
        # Split by non-alphanumeric characters
        parts = self._NON_ALNUM_PATTERN.split(name)

        # Process each part: capitalize first letter, preserve rest
        processed_parts = []
        for part in parts:
            if not part:
                continue
            # Capitalize first letter only, keep rest as-is
            processed_parts.append(
                part[0].upper() + part[1:] if len(part) > 1 else part.upper()
            )

        class_name = ''.join(processed_parts)

        # Handle special case: preserve uppercase sequences like "HVAC"
        # by checking if the original had them
        class_name = self._preserve_acronyms(name, class_name)

        return class_name

    def _preserve_acronyms(self, original: str, class_name: str) -> str:
        """Preserve common acronyms in class names.

        Args:
            original: Original object name.
            class_name: Generated class name.

        Returns:
            Class name with preserved acronyms.
        """
        result = class_name
        original_lower = original.lower()
        for acronym, pattern in self._ACRONYM_PATTERNS.items():
            if acronym.lower() in original_lower:
                result = pattern.sub(acronym, result)
        return result

    def get_version(self) -> str:
        """Get the EnergyPlus schema version.

        Returns:
            Schema version string (e.g., "25.1.0").
        """
        self._load_schema()
        if self._raw_schema is None:
            return 'unknown'
        version = self._raw_schema.get('properties', {}).get('Version', {})
        return (
            version.get('patternProperties', {})
            .get('.*', {})
            .get('properties', {})
            .get('version_identifier', {})
            .get('default', 'unknown')
        )

    def get_groups(self) -> dict[str, list[str]]:
        """Get all object types organized by group.

        Returns:
            Dictionary mapping group names to lists of object type names.
        """
        specs = self.parse()

        groups: dict[str, list[str]] = {}
        for name, spec in specs.items():
            group = spec.group
            if group not in groups:
                groups[group] = []
            groups[group].append(name)

        return groups
