"""EnergyPlus Pydantic model code generator.

This module generates type-safe Pydantic models from EnergyPlus schema
object specifications. Models are organized by EnergyPlus group categories.
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import ClassVar

from jinja2 import Environment, FileSystemLoader
from loguru import logger

from .field_parser import FieldSpec
from .schema_parser import ObjectSpec
from .template_filters import (
    TEMPLATE_FILTERS,
    collect_used_ref_types,
    extract_nested_classes,
    set_object_list_ref_types,
)


class ModelGenerator:
    """Generate Pydantic models from EnergyPlus ObjectSpec definitions.

    Organizes models by EnergyPlus group categories, generating separate
    Python files for each category. Small categories are merged into misc.py.

    Example:
        >>> from src.codegen.schema_parser import SchemaParser
        >>> parser = SchemaParser(Path('Energy+.schema.epJSON'))
        >>> specs = parser.parse()
        >>> generator = ModelGenerator(Path('src/idf/models'))
        >>> generator.generate_all(specs, schema_version='24.2.0')
    """

    # Mapping from EnergyPlus group names to output file names
    GROUP_FILE_MAPPING: ClassVar[dict[str, str]] = {
        # Simulation Parameters
        'Simulation Parameters': 'simulation',
        # Location and Climate
        'Location and Climate': 'location',
        # Schedules
        'Schedules': 'schedules',
        # Surface Construction Elements
        'Surface Construction Elements': 'constructions',
        # Thermal Zones and Surfaces
        'Thermal Zones and Surfaces': 'thermal_zones',
        # Advanced Construction, Surface, Zone Concepts
        'Advanced Construction': 'advanced_construction',
        'Advanced Construction, Surface, Zone Concepts': 'advanced_construction',
        # Room Air Models
        'Room Air Models': 'room_air',
        # Internal Gains
        'Internal Gains': 'internal_gains',
        # Daylighting
        'Daylighting': 'daylighting',
        # Zone Airflow
        'Zone Airflow': 'zone_airflow',
        # Natural Ventilation and Duct Leakage
        'Natural Ventilation and Duct Leakage': 'ventilation',
        # Exterior Equipment
        'Exterior Equipment': 'exterior',
        # HVAC Templates
        'HVAC Templates': 'hvac_templates',
        # HVAC Design Objects
        'HVAC Design Objects': 'hvac_design',
        # Zone HVAC Controls and Thermostats
        'Zone HVAC Controls and Thermostats': 'zone_controls',
        # Zone HVAC Air Loop Terminal Units
        'Zone HVAC Air Loop Terminal Units': 'zone_terminals',
        # Zone HVAC Equipment Connections
        'Zone HVAC Equipment Connections': 'zone_equipment',
        # Zone HVAC Forced Air Units
        'Zone HVAC Forced Air Units': 'zone_forced_air',
        # Zone HVAC Radiative/Convective Units
        'Zone HVAC Radiative/Convective Units': 'zone_radiative',
        # Fans
        'Fans': 'fans',
        # Coils
        'Coils': 'coils',
        # Evaporative Coolers
        'Evaporative Coolers': 'evap_coolers',
        # Humidifiers and Dehumidifiers
        'Humidifiers and Dehumidifiers': 'humidifiers',
        # Heat Recovery
        'Heat Recovery': 'heat_recovery',
        # Unitary Equipment
        'Unitary Equipment': 'unitary',
        # Variable Refrigerant Flow Equipment
        'Variable Refrigerant Flow Equipment': 'vrf',
        # Air Distribution
        'Air Distribution': 'air_distribution',
        # Pumps
        'Pumps': 'pumps',
        # Plant Heating and Cooling Equipment
        'Plant Heating and Cooling Equipment': 'plant_equipment',
        # Condenser Equipment and Heat Exchangers
        'Condenser Equipment and Heat Exchangers': 'condensers',
        # Water Heaters and Thermal Storage
        'Water Heaters and Thermal Storage': 'water_heaters',
        # Plant-Condenser Loops
        'Plant-Condenser Loops': 'plant_loops',
        # Plant-Condenser Control
        'Plant-Condenser Control': 'plant_control',
        # Non-Zone Equipment
        'Non-Zone Equipment': 'non_zone',
        # Solar Collectors
        'Solar Collectors': 'solar',
        # Refrigeration
        'Refrigeration': 'refrigeration',
        # Demand Limiting Controls
        'Demand Limiting Controls': 'demand_limiting',
        # Electric Load Center-Generator Specifications
        'Electric Load Center-Generator Specifications': 'electric_load',
        # Water Systems
        'Water Systems': 'water_systems',
        # Operational Faults
        'Operational Faults': 'faults',
        # Performance Curves and Tables
        'Performance Curves': 'curves',
        'Performance Curves and Tables': 'curves',
        # Fluid Properties
        'Fluid Properties': 'fluids',
        # Economics
        'Economics': 'economics',
        # Parametrics
        'Parametrics': 'parametrics',
        # Output Reporting
        'Output Reporting': 'outputs',
        # Hybrid Model
        'Hybrid Model': 'hybrid',
        # Python Plugin System
        'Python Plugin System': 'python_plugins',
        # Compliance Objects
        'Compliance Objects': 'compliance',
        # User Defined HVAC and Plant Component Models
        'User Defined HVAC and Plant Component Models': 'user_defined',
        # Energy Management System (EMS)
        'Energy Management System (EMS)': 'ems',
        # External Interface
        'External Interface': 'external_interface',
        # Setpoint Managers
        'Setpoint Managers': 'setpoint_managers',
        # System Availability Managers
        'System Availability Managers': 'availability_managers',
        # Controllers
        'Controllers': 'controllers',
        # Air Path
        'Air Path': 'air_path',
        # Node-Branch Management
        'Node-Branch Management': 'node_branch',
        # Plant-Condenser Flow Control
        'Plant-Condenser Flow Control': 'plant_flow_control',
    }

    # Pre-computed lowercase mapping for partial match optimization
    # Avoids repeated .lower() calls during group lookups
    _GROUP_LOWERCASE_MAPPING: ClassVar[dict[str, str]] = {
        pattern.lower(): file_name for pattern, file_name in GROUP_FILE_MAPPING.items()
    }

    # Minimum number of objects to create a separate file
    MERGE_THRESHOLD = 5

    def __init__(self, output_dir: Path):
        """Initialize the model generator.

        Args:
            output_dir: Directory where generated model files will be written.
        """
        self.output_dir = Path(output_dir)
        self._env: Environment | None = None

    def generate_all(
        self,
        specs: dict[str, ObjectSpec],
        schema_version: str = 'unknown',
    ) -> None:
        """Generate all model files from object specifications.

        Args:
            specs: Dictionary mapping object type names to ObjectSpec instances.
            schema_version: EnergyPlus schema version for documentation.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Collect all object_lists and generate _refs.py
        object_lists = self._collect_object_lists(specs)
        self._generate_refs_file(object_lists, schema_version)

        # Build and set object_list -> ref type mapping for template filters
        self._object_list_to_ref_type = {
            ol: self._object_list_to_type_name(ol) for ol in object_lists
        }
        set_object_list_ref_types(self._object_list_to_ref_type)

        # Group objects by output file
        file_groups = self._group_objects_by_file(specs)

        # Track all generated classes for __init__.py
        all_classes: dict[str, list[str]] = {}  # file_name -> [class_names]
        object_type_registry: dict[str, str] = {}  # "Zone" -> "Zone"
        # "Zone" -> ["field1", ...]
        field_order_registry: dict[str, list[str]] = {}

        # Generate each model file
        for file_name, unsorted_objects in file_groups.items():
            logger.info(
                f'Generating {file_name}.py with {len(unsorted_objects)} objects...'
            )

            # Sort objects by name for consistent output
            sorted_objects = sorted(unsorted_objects, key=lambda o: o.class_name)

            # Extract group name from first object
            group_name = sorted_objects[0].group if sorted_objects else 'Unknown'

            # Generate the file
            class_names = self._generate_model_file(
                file_name=file_name,
                objects=sorted_objects,
                group_name=group_name,
                schema_version=schema_version,
            )

            all_classes[file_name] = class_names

            # Build registries
            for obj in sorted_objects:
                object_type_registry[obj.name] = obj.class_name
                field_order_registry[obj.name] = [f.python_name for f in obj.fields]

        # Generate __init__.py
        self._generate_init_file(
            all_classes=all_classes,
            object_type_registry=object_type_registry,
            field_order_registry=field_order_registry,
            schema_version=schema_version,
        )

        total_objects = sum(len(objs) for objs in file_groups.values())
        logger.info(
            f'Generated {len(file_groups)} model files '
            f'with {total_objects} object types'
        )

    def _group_objects_by_file(
        self, specs: dict[str, ObjectSpec]
    ) -> dict[str, list[ObjectSpec]]:
        """Group objects by output file name.

        Objects are grouped according to GROUP_FILE_MAPPING. Small groups
        (fewer than MERGE_THRESHOLD objects) are merged into misc.py.

        Args:
            specs: Dictionary of object specifications.

        Returns:
            Dictionary mapping file names to lists of ObjectSpec.
        """
        file_groups: dict[str, list[ObjectSpec]] = defaultdict(list)
        unmapped_objects: list[ObjectSpec] = []

        for spec in specs.values():
            group = spec.group
            file_name = self._get_file_for_group(group)

            if file_name:
                file_groups[file_name].append(spec)
            else:
                unmapped_objects.append(spec)

        # Add unmapped objects to misc
        if unmapped_objects:
            unmapped_groups = sorted({s.group for s in unmapped_objects})
            logger.warning(
                f'Found {len(unmapped_objects)} objects in {len(unmapped_groups)} '
                f'unmapped groups: {unmapped_groups}'
            )
            file_groups['misc'].extend(unmapped_objects)

        # Merge small groups into misc
        final_groups: dict[str, list[ObjectSpec]] = {}
        small_objects: list[ObjectSpec] = []

        for file_name, objects in file_groups.items():
            if len(objects) < self.MERGE_THRESHOLD and file_name != 'misc':
                logger.debug(f'Merging {file_name} ({len(objects)} objects) into misc')
                small_objects.extend(objects)
            else:
                final_groups[file_name] = objects

        if small_objects:
            if 'misc' in final_groups:
                final_groups['misc'].extend(small_objects)
            else:
                final_groups['misc'] = small_objects

        return final_groups

    def _get_file_for_group(self, group: str) -> str | None:
        """Find the output file name for an EnergyPlus group.

        Uses exact match first, then partial match with pre-computed
        lowercase keys to avoid repeated .lower() calls.

        Args:
            group: EnergyPlus group name.

        Returns:
            File name or None if no mapping found.
        """
        # Exact match
        if group in self.GROUP_FILE_MAPPING:
            return self.GROUP_FILE_MAPPING[group]

        # Partial match using pre-computed lowercase mapping
        group_lower = group.lower()
        for pattern_lower, file_name in self._GROUP_LOWERCASE_MAPPING.items():
            if pattern_lower in group_lower:
                return file_name

        return None

    def _generate_model_file(
        self,
        file_name: str,
        objects: list[ObjectSpec],
        group_name: str,
        schema_version: str,
    ) -> list[str]:
        """Generate a single model file.

        Args:
            file_name: Output file name (without .py extension).
            objects: List of ObjectSpec to include.
            group_name: EnergyPlus group name for documentation.
            schema_version: Schema version for documentation.

        Returns:
            List of generated class names.
        """
        env = self._get_jinja_env()
        template = env.get_template('idf_model_py.jinja2')

        # Extract nested classes from array fields
        nested_classes = extract_nested_classes(objects, deduplicate=True)

        # Collect reference types used by this file's objects
        used_ref_types = collect_used_ref_types(objects)
        has_refs = len(used_ref_types) > 0

        # Render template
        content = template.render(
            schema_version=schema_version,
            group_name=group_name,
            file_name=file_name,
            objects=objects,
            nested_classes=nested_classes,
            has_refs=has_refs,
            used_ref_types=used_ref_types,
        )

        # Write file
        output_path = self.output_dir / f'{file_name}.py'
        output_path.write_text(content, encoding='utf-8')
        logger.debug(f'Written {output_path}')

        # Collect class names (main objects + nested)
        class_names = [obj.class_name for obj in objects]
        class_names.extend(nc['name'] for nc in nested_classes)

        return class_names

    def _generate_init_file(
        self,
        all_classes: dict[str, list[str]],
        object_type_registry: dict[str, str],
        field_order_registry: dict[str, list[str]],
        schema_version: str,
    ) -> None:
        """Generate __init__.py with exports and registries.

        Args:
            all_classes: Mapping of file names to class names.
            object_type_registry: Mapping of object type names to class names.
            field_order_registry: Mapping of object type names to field orders.
            schema_version: Schema version for documentation.
        """
        lines = [
            '"""Auto-generated EnergyPlus IDF models.',
            '',
            'This module exports all EnergyPlus object types as Pydantic models.',
            f'Generated from Energy+.schema.epJSON version {schema_version}.',
            '"""',
            'from __future__ import annotations',
            '',
            'from ._base import IDFBaseModel',
            '',
        ]

        # Generate imports
        for file_name in sorted(all_classes.keys()):
            class_names = sorted(all_classes[file_name])
            if not class_names:
                continue

            # Format imports nicely
            if len(class_names) <= 3:
                imports = ', '.join(class_names)
                lines.append(f'from .{file_name} import {imports}')
            else:
                lines.append(f'from .{file_name} import (')
                for cls_name in class_names:
                    lines.append(f'    {cls_name},')
                lines.append(')')

        lines.append('')

        # Generate OBJECT_TYPE_REGISTRY
        lines.extend(self._format_object_type_registry(object_type_registry))

        lines.append('')

        # Generate FIELD_ORDER_REGISTRY
        lines.extend(self._format_field_order_registry(field_order_registry))

        lines.append('')

        # Helper functions
        lines.extend(
            [
                '',
                'def get_model_class(object_type: str) -> type[IDFBaseModel] | None:',
                '    """Get model class by EnergyPlus object type name.',
                '',
                '    Args:',
                "        object_type: EnergyPlus object type (e.g., 'Zone').",
                '',
                '    Returns:',
                '        Model class or None if not found.',
                '    """',
                '    class_name = OBJECT_TYPE_REGISTRY.get(object_type)',
                '    if class_name is None:',
                '        return None',
                '    return globals().get(class_name)',
                '',
                '',
                'def get_field_order(object_type: str) -> list[str]:',
                '    """Get field order for an object type.',
                '',
                '    Args:',
                '        object_type: EnergyPlus object type name.',
                '',
                '    Returns:',
                '        List of field names in schema order, empty if not found.',
                '    """',
                '    return FIELD_ORDER_REGISTRY.get(object_type, [])',
                '',
            ]
        )

        # Generate __all__
        all_exports = ['IDFBaseModel', 'OBJECT_TYPE_REGISTRY', 'FIELD_ORDER_REGISTRY']
        all_exports.extend(['get_model_class', 'get_field_order'])
        for class_names in all_classes.values():
            all_exports.extend(class_names)
        all_exports = sorted(set(all_exports))

        lines.append('')
        lines.append('__all__ = [')
        for name in all_exports:
            lines.append(f'    "{name}",')
        lines.append(']')

        output_path = self.output_dir / '__init__.py'
        output_path.write_text('\n'.join(lines), encoding='utf-8')
        logger.debug(f'Written {output_path}')

    def _format_object_type_registry(self, registry: dict[str, str]) -> list[str]:
        """Format OBJECT_TYPE_REGISTRY as Python code.

        Args:
            registry: Mapping of object type names to class names.

        Returns:
            List of code lines.
        """
        lines = [
            '# Object type name to model class name mapping',
            'OBJECT_TYPE_REGISTRY: dict[str, str] = {',
        ]
        for obj_type in sorted(registry.keys()):
            class_name = registry[obj_type]
            lines.append(f'    "{obj_type}": "{class_name}",')
        lines.append('}')
        return lines

    def _format_field_order_registry(self, registry: dict[str, list[str]]) -> list[str]:
        """Format FIELD_ORDER_REGISTRY as Python code.

        Args:
            registry: Mapping of object type names to field name lists.

        Returns:
            List of code lines.
        """
        lines = [
            '# Field order mapping for IDF output (preserves schema order)',
            'FIELD_ORDER_REGISTRY: dict[str, list[str]] = {',
        ]
        for obj_type in sorted(registry.keys()):
            fields = registry[obj_type]
            if not fields:
                lines.append(f'    "{obj_type}": [],')
            elif len(fields) <= 3:
                fields_str = ', '.join(f'"{f}"' for f in fields)
                lines.append(f'    "{obj_type}": [{fields_str}],')
            else:
                lines.append(f'    "{obj_type}": [')
                for field_name in fields:
                    lines.append(f'        "{field_name}",')
                lines.append('    ],')
        lines.append('}')
        return lines

    def _get_jinja_env(self) -> Environment:
        """Get or create the Jinja2 environment with filters.

        Returns:
            Configured Jinja2 Environment.
        """
        if self._env is not None:
            return self._env

        template_dir = Path(__file__).parent / 'templates'
        self._env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

        # Register custom filters
        for name, func in TEMPLATE_FILTERS.items():
            self._env.filters[name] = func

        return self._env

    def _collect_object_lists(self, specs: dict[str, ObjectSpec]) -> set[str]:
        """Collect all unique object_list names from specifications.

        Args:
            specs: Dictionary of object specifications.

        Returns:
            Set of unique object_list names.
        """
        object_lists: set[str] = set()

        def collect_from_field(field: FieldSpec) -> None:
            if field.object_list:
                object_lists.update(field.object_list)

            if field.anyof_specs:
                for anyof in field.anyof_specs:
                    if anyof.object_list:
                        object_lists.update(anyof.object_list)

            if field.items_spec:
                if field.items_spec.object_list:
                    object_lists.update(field.items_spec.object_list)
                if field.items_spec.nested_fields:
                    for nested in field.items_spec.nested_fields:
                        collect_from_field(nested)

            if field.nested_fields:
                for nested in field.nested_fields:
                    collect_from_field(nested)

        for spec in specs.values():
            for field in spec.fields:
                collect_from_field(field)

        return object_lists

    def _object_list_to_type_name(self, object_list: str) -> str:
        """Convert object_list name to type alias name.

        Args:
            object_list: Object list name (e.g., "ZoneNames").

        Returns:
            Type alias name (e.g., "ZoneNamesRef").
        """
        # Remove special characters, ensure valid Python identifier
        name = re.sub(r'[^a-zA-Z0-9]', '', object_list)
        # Ensure PascalCase (first letter uppercase)
        if name and name[0].islower():
            name = name[0].upper() + name[1:]
        return f'{name}Ref'

    def _generate_refs_file(
        self,
        object_lists: set[str],
        schema_version: str,
    ) -> None:
        """Generate _refs.py with reference type aliases.

        Args:
            object_lists: Set of object list names.
            schema_version: Schema version for documentation.
        """
        lines = [
            '"""Auto-generated reference types for EnergyPlus object validation.',
            '',
            'DO NOT EDIT MANUALLY.',
            f'Generated from Energy+.schema.epJSON version {schema_version}.',
            '',
            'This module provides type aliases with runtime validation for object',
            'references. Use with validation context for reference checking.',
            '"""',
            'from __future__ import annotations',
            '',
            'from typing import Annotated, Any',
            '',
            'from pydantic import BeforeValidator',
            'from pydantic_core import core_schema',
            '',
            '',
        ]

        # Add RefValidator class
        lines.extend(self._get_ref_validator_code())

        lines.append('')
        lines.append('')
        lines.append('# ' + '=' * 60)
        lines.append('# Reference type aliases')
        lines.append('# ' + '=' * 60)
        lines.append('')

        # Generate type aliases for each object_list
        for obj_list in sorted(object_lists):
            type_name = self._object_list_to_type_name(obj_list)
            lines.append(
                f'{type_name} = Annotated[str, BeforeValidator(RefValidator("{obj_list}"))]'
            )

        lines.append('')

        # Generate __all__
        all_exports = ['RefValidator']
        all_exports.extend(
            self._object_list_to_type_name(ol) for ol in sorted(object_lists)
        )

        lines.append('__all__ = [')
        for name in all_exports:
            lines.append(f'    "{name}",')
        lines.append(']')
        lines.append('')

        output_path = self.output_dir / '_refs.py'
        output_path.write_text('\n'.join(lines), encoding='utf-8')
        logger.info(f'Generated _refs.py with {len(object_lists)} reference types')

    def _get_ref_validator_code(self) -> list[str]:
        """Get RefValidator class code.

        Returns:
            List of code lines for RefValidator class.
        """
        return [
            'class RefValidator:',
            '    """Reference validator for EnergyPlus object lists.',
            '',
            '    When used with validation context containing an IDF instance,',
            '    validates that referenced object names exist in the registry.',
            '    """',
            '',
            '    def __init__(self, object_list: str):',
            '        self.object_list = object_list',
            '',
            '    def __call__(self, v: Any) -> str | None:',
            '        """Validate reference value.',
            '',
            '        Note: Context-based validation happens in IDF.add().',
            '        This basic validator just ensures string conversion.',
            '        """',
            '        if v is None:',
            '            return None',
            '        return str(v)',
            '',
            '    def __get_pydantic_core_schema__(self, source_type, handler):',
            '        """Generate Pydantic core schema for this validator."""',
            '        return core_schema.no_info_before_validator_function(',
            '            self,',
            '            core_schema.str_schema(),',
            '        )',
            '',
            '    def __repr__(self) -> str:',
            '        return f"RefValidator({self.object_list!r})"',
        ]
