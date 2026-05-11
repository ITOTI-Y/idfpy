"""EnergyPlus Pydantic model code generator.

This module generates type-safe Pydantic models from EnergyPlus schema
object specifications. Models are organized by EnergyPlus group categories.
"""

from __future__ import annotations

import importlib
import re
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar

from loguru import logger

if TYPE_CHECKING:
    from jinja2 import Environment

from .field_parser import FieldSpec
from .schema_parser import ObjectSpec
from .template_filters import (
    TEMPLATE_FILTERS,
    collect_nav_imports,
    collect_used_ref_types,
    extract_nested_classes,
    set_nav_type_mapping,
    set_object_list_ref_types,
    set_object_type_to_class,
    set_reference_class_name_groups,
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

    GROUP_FILE_MAPPING: ClassVar[dict[str, str]] = {
        'Simulation Parameters': 'simulation',
        'Location and Climate': 'location',
        'Schedules': 'schedules',
        'Surface Construction Elements': 'constructions',
        'Thermal Zones and Surfaces': 'thermal_zones',
        'Advanced Construction': 'advanced_construction',
        'Advanced Construction, Surface, Zone Concepts': 'advanced_construction',
        'Room Air Models': 'room_air',
        'Internal Gains': 'internal_gains',
        'Daylighting': 'daylighting',
        'Zone Airflow': 'zone_airflow',
        'Natural Ventilation and Duct Leakage': 'ventilation',
        'Exterior Equipment': 'exterior',
        'HVAC Templates': 'hvac_templates',
        'HVAC Design Objects': 'hvac_design',
        'Zone HVAC Controls and Thermostats': 'zone_controls',
        'Zone HVAC Air Loop Terminal Units': 'zone_terminals',
        'Zone HVAC Equipment Connections': 'zone_equipment',
        'Zone HVAC Forced Air Units': 'zone_forced_air',
        'Zone HVAC Radiative/Convective Units': 'zone_radiative',
        'Fans': 'fans',
        'Coils': 'coils',
        'Evaporative Coolers': 'evap_coolers',
        'Humidifiers and Dehumidifiers': 'humidifiers',
        'Heat Recovery': 'heat_recovery',
        'Unitary Equipment': 'unitary',
        'Variable Refrigerant Flow Equipment': 'vrf',
        'Air Distribution': 'air_distribution',
        'Pumps': 'pumps',
        'Plant Heating and Cooling Equipment': 'plant_equipment',
        'Condenser Equipment and Heat Exchangers': 'condensers',
        'Water Heaters and Thermal Storage': 'water_heaters',
        'Plant-Condenser Loops': 'plant_loops',
        'Plant-Condenser Control': 'plant_control',
        'Non-Zone Equipment': 'non_zone',
        'Solar Collectors': 'solar',
        'Refrigeration': 'refrigeration',
        'Demand Limiting Controls': 'demand_limiting',
        'Electric Load Center-Generator Specifications': 'electric_load',
        'Water Systems': 'water_systems',
        'Operational Faults': 'faults',
        'Performance Curves': 'curves',
        'Performance Curves and Tables': 'curves',
        'Fluid Properties': 'fluids',
        'Economics': 'economics',
        'Parametrics': 'parametrics',
        'Output Reporting': 'outputs',
        'Hybrid Model': 'hybrid',
        'Python Plugin System': 'python_plugins',
        'Compliance Objects': 'compliance',
        'User Defined HVAC and Plant Component Models': 'user_defined',
        'Energy Management System (EMS)': 'ems',
        'External Interface': 'external_interface',
        'Setpoint Managers': 'setpoint_managers',
        'System Availability Managers': 'availability_managers',
        'Controllers': 'controllers',
        'Air Path': 'air_path',
        'Node-Branch Management': 'node_branch',
        'Plant-Condenser Flow Control': 'plant_flow_control',
    }

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

        object_lists = self._collect_object_lists(specs)
        self._generate_refs_file(object_lists, schema_version)

        self._object_list_to_ref_type = {
            ol: self._object_list_to_type_name(ol) for ol in object_lists
        }
        set_object_list_ref_types(self._object_list_to_ref_type)

        self._rcn_groups = self._collect_reference_class_name_groups(specs)
        set_reference_class_name_groups(set(self._rcn_groups.keys()))

        set_object_type_to_class({s.name: s.class_name for s in specs.values()})

        self._ext_mixins = self._discover_ext_mixins()
        if self._ext_mixins:
            affected = ', '.join(sorted(self._ext_mixins))
            logger.info('Discovered ext mixins for: {}', affected)

        file_groups = self._group_objects_by_file(specs)

        group_to_classes: dict[str, set[str]] = {}
        class_to_module: dict[str, str] = {}
        for file_name, objs in file_groups.items():
            for obj in objs:
                class_to_module[obj.class_name] = file_name
                for field in obj.fields:
                    if field.reference:
                        for group in field.reference:
                            group_to_classes.setdefault(group, set()).add(
                                obj.class_name
                            )
        self._class_to_module = class_to_module
        set_nav_type_mapping(group_to_classes)

        all_classes: dict[str, list[str]] = {}
        all_nested_classes: dict[str, list[dict]] = {}
        object_type_registry: dict[str, str] = {}
        field_order_registry: dict[str, list[str]] = {}
        singleton_types: set[str] = set()

        for file_name, unsorted_objects in file_groups.items():
            logger.info(
                'Generating {}.py with {} objects...', file_name, len(unsorted_objects)
            )

            sorted_objects = sorted(unsorted_objects, key=lambda o: o.class_name)
            group_name = sorted_objects[0].group if sorted_objects else 'Unknown'

            class_names, nested_classes = self._generate_model_file(
                file_name=file_name,
                objects=sorted_objects,
                group_name=group_name,
                schema_version=schema_version,
            )

            all_classes[file_name] = class_names
            all_nested_classes[file_name] = nested_classes

            for obj in sorted_objects:
                object_type_registry[obj.name] = obj.class_name
                field_order_registry[obj.name] = [f.python_name for f in obj.fields]
                if obj.is_singleton:
                    singleton_types.add(obj.name)

        self._generate_ref_meta_file(specs, all_nested_classes, schema_version)

        self._generate_init_file(
            all_classes=all_classes,
            object_type_registry=object_type_registry,
            field_order_registry=field_order_registry,
            singleton_types=sorted(singleton_types),
            schema_version=schema_version,
        )

        total_objects = sum(len(objs) for objs in file_groups.values())
        logger.info(
            'Generated {} model files with {} object types',
            len(file_groups),
            total_objects,
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

        if unmapped_objects:
            unmapped_groups = sorted({s.group for s in unmapped_objects})
            logger.warning(
                'Found {} objects in {} unmapped groups: {}',
                len(unmapped_objects),
                len(unmapped_groups),
                unmapped_groups,
            )
            file_groups['misc'].extend(unmapped_objects)

        final_groups: dict[str, list[ObjectSpec]] = {}
        small_objects: list[ObjectSpec] = []

        for file_name, objects in file_groups.items():
            if len(objects) < self.MERGE_THRESHOLD and file_name != 'misc':
                logger.debug(
                    'Merging {} ({} objects) into misc', file_name, len(objects)
                )
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

        Uses exact match first, then case-insensitive partial match.
        """
        if group in self.GROUP_FILE_MAPPING:
            return self.GROUP_FILE_MAPPING[group]

        group_lower = group.lower()
        for pattern, file_name in self.GROUP_FILE_MAPPING.items():
            if pattern.lower() in group_lower:
                return file_name

        return None

    def _generate_model_file(
        self,
        file_name: str,
        objects: list[ObjectSpec],
        group_name: str,
        schema_version: str,
    ) -> tuple[list[str], list[dict]]:
        """Generate a single model file.

        Args:
            file_name: Output file name (without .py extension).
            objects: List of ObjectSpec to include.
            group_name: EnergyPlus group name for documentation.
            schema_version: Schema version for documentation.

        Returns:
            Tuple of (class_names, nested_classes).
        """
        env = self._get_jinja_env()
        template = env.get_template('idf_model_py.jinja2')

        nested_classes = extract_nested_classes(objects, deduplicate=True)

        for nc in nested_classes:
            self._class_to_module[nc['name']] = file_name

        used_ref_types = collect_used_ref_types(objects)
        has_refs = len(used_ref_types) > 0

        nav_imports = collect_nav_imports(
            objects, nested_classes, file_name, self._class_to_module
        )

        file_mixin_map: dict[str, list[str]] = {}
        file_mixin_imports: dict[str, set[str]] = {}
        for obj in objects:
            if obj.class_name in self._ext_mixins:
                mixins = self._ext_mixins[obj.class_name]
                file_mixin_map[obj.class_name] = [m[0] for m in mixins]
                for mixin_name, import_path in mixins:
                    file_mixin_imports.setdefault(import_path, set()).add(mixin_name)

        content = template.render(
            schema_version=schema_version,
            group_name=group_name,
            file_name=file_name,
            objects=objects,
            nested_classes=nested_classes,
            has_refs=has_refs,
            used_ref_types=used_ref_types,
            nav_imports=nav_imports,
            mixin_map=file_mixin_map,
            mixin_imports={k: sorted(v) for k, v in sorted(file_mixin_imports.items())},
        )

        output_path = self.output_dir / f'{file_name}.py'
        output_path.write_text(content, encoding='utf-8')
        logger.debug('Written {}', output_path)

        class_names = [obj.class_name for obj in objects]
        class_names.extend(nc['name'] for nc in nested_classes)

        return class_names, nested_classes

    def _generate_ref_meta_file(
        self,
        specs: dict[str, ObjectSpec],
        all_nested_classes: dict[str, list[dict]],
        schema_version: str,
    ) -> None:
        """Generate _ref_meta.py with REF_PROVIDERS, REF_GROUP_PROVIDERS, REF_CONSUMERS.

        Args:
            specs: All object specifications.
            all_nested_classes: file_name -> list of nested class dicts,
                each with 'name' and 'fields' keys.
            schema_version: Schema version for docs.
        """
        providers: dict[str, list[tuple[str, list[str]]]] = {}
        group_providers: dict[str, set[str]] = {}
        consumers: dict[str, dict[str, list[str]]] = {}

        for obj_name, obj_spec in specs.items():
            obj_providers: list[tuple[str, list[str]]] = []
            for field in obj_spec.fields:
                if field.reference:
                    obj_providers.append((field.python_name, field.reference))
                    for group in field.reference:
                        group_providers.setdefault(group, set()).add(obj_name)
            if obj_providers:
                providers[obj_name] = obj_providers

            cls_fields: dict[str, list[str]] = {}
            for field in obj_spec.fields:
                if field.object_list:
                    cls_fields[field.python_name] = field.object_list
            if cls_fields:
                consumers[obj_spec.class_name] = cls_fields

        for _file_name, nested_list in all_nested_classes.items():
            for nc in nested_list:
                item_fields: dict[str, list[str]] = {}
                for field in nc['fields']:
                    if field.object_list:
                        item_fields[field.python_name] = field.object_list
                if item_fields:
                    consumers[nc['name']] = item_fields

        env = self._get_jinja_env()
        template = env.get_template('ref_meta_py.jinja2')

        providers_data = []
        for obj_type in sorted(providers):
            entries = providers[obj_type]
            formatted = ', '.join(f'("{fn}", {gl!r})' for fn, gl in entries)
            providers_data.append((obj_type, formatted))

        group_providers_data = [
            (group, sorted(group_providers[group])) for group in sorted(group_providers)
        ]

        consumers_data = [
            (
                cls_name,
                [(fn, repr(groups)) for fn, groups in consumers[cls_name].items()],
            )
            for cls_name in sorted(consumers)
        ]

        rcn_types_data = [
            (group, sorted(types)) for group, types in sorted(self._rcn_groups.items())
        ]

        content = template.render(
            schema_version=schema_version,
            providers=providers_data,
            group_providers=group_providers_data,
            consumers=consumers_data,
            rcn_types=rcn_types_data,
        )

        output_path = self.output_dir / '_ref_meta.py'
        output_path.write_text(content, encoding='utf-8')
        logger.info(
            'Generated _ref_meta.py: {} providers, {} groups, '
            '{} consumers, {} reference-class-name groups',
            len(providers),
            len(group_providers),
            len(consumers),
            len(rcn_types_data),
        )

    def _generate_init_file(
        self,
        all_classes: dict[str, list[str]],
        object_type_registry: dict[str, str],
        field_order_registry: dict[str, list[str]],
        singleton_types: list[str],
        schema_version: str,
    ) -> None:
        """Generate __init__.py with lazy imports and registries, plus __init__.pyi type stub.

        Uses PEP 562 module-level __getattr__ for lazy importing of model
        classes. Only IDFBaseModel is eagerly imported. A companion .pyi stub
        is generated with explicit imports for IDE autocompletion.

        Args:
            all_classes: Mapping of file names to class names.
            object_type_registry: Mapping of object type names to class names.
            field_order_registry: Mapping of object type names to field orders.
            singleton_types: Sorted list of object type names with maxProperties=1.
            schema_version: Schema version for documentation.
        """
        env = self._get_jinja_env()
        template = env.get_template('init_py.jinja2')

        class_to_module: dict[str, str] = {}
        for file_name, class_names in all_classes.items():
            for cls_name in class_names:
                class_to_module[cls_name] = file_name

        all_exports = [
            'IDFBaseModel',
            'OBJECT_TYPE_REGISTRY',
            'CLASS_NAME_REGISTRY',
            'FIELD_ORDER_REGISTRY',
            'SINGLETON_TYPES',
        ]
        all_exports.extend(['get_model_class', 'get_field_order'])
        for class_names in all_classes.values():
            all_exports.extend(class_names)
        all_exports = sorted(set(all_exports))

        content = template.render(
            schema_version=schema_version,
            class_to_module=sorted(class_to_module.items()),
            object_type_registry=sorted(object_type_registry.items()),
            field_order_registry=sorted(field_order_registry.items()),
            singleton_types=singleton_types,
            all_exports=all_exports,
        )

        output_path = self.output_dir / '__init__.py'
        output_path.write_text(content, encoding='utf-8')
        logger.debug('Written {}', output_path)

        pyi_template = env.get_template('init_pyi.jinja2')
        module_to_classes = sorted(
            (mod, sorted(classes, key=str.lower))
            for mod, classes in all_classes.items()
        )
        pyi_content = pyi_template.render(
            schema_version=schema_version,
            module_to_classes=module_to_classes,
        )
        pyi_path = self.output_dir / '__init__.pyi'
        pyi_path.write_text(pyi_content, encoding='utf-8')
        logger.debug('Written {}', pyi_path)

    def _get_jinja_env(self) -> Environment:
        """Get or create the Jinja2 environment with filters.

        Returns:
            Configured Jinja2 Environment.
        """
        if self._env is not None:
            return self._env

        from jinja2 import Environment as Env
        from jinja2 import FileSystemLoader

        template_dir = Path(__file__).parent / 'templates'
        self._env = Env(
            loader=FileSystemLoader(str(template_dir)),
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )

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

    def _collect_reference_class_name_groups(
        self, specs: dict[str, ObjectSpec]
    ) -> dict[str, list[str]]:
        """Collect reference-class-name groups and their member type names.

        Returns:
            Mapping of group name to list of object type names that belong
            to that group (via reference-class-name on their name field).
        """
        groups: dict[str, list[str]] = {}
        for obj_name, spec in specs.items():
            for field in spec.fields:
                if field.reference_class_name and field.is_name:
                    for group in field.reference_class_name:
                        groups.setdefault(group, []).append(obj_name)
        return groups

    def _object_list_to_type_name(self, object_list: str) -> str:
        """Convert object_list name to type alias name.

        Args:
            object_list: Object list name (e.g., "ZoneNames").

        Returns:
            Type alias name (e.g., "ZoneNamesRef").
        """
        name = re.sub(r'[^a-zA-Z0-9]', '', object_list)
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
        env = self._get_jinja_env()
        template = env.get_template('refs_py.jinja2')

        ref_types = [
            {'type_name': self._object_list_to_type_name(ol), 'object_list': ol}
            for ol in sorted(object_lists)
        ]

        content = template.render(
            schema_version=schema_version,
            ref_types=ref_types,
        )

        output_path = self.output_dir / '_refs.py'
        output_path.write_text(content, encoding='utf-8')
        logger.info('Generated _refs.py with {} reference types', len(object_lists))

    def _discover_ext_mixins(self) -> dict[str, list[tuple[str, str]]]:
        """Discover ext plugin mixin mappings.

        Scans ``idfpy/ext/`` sub-packages for a ``MIXIN_MAP`` attribute and
        collects ``(mixin_class_name, import_path)`` entries per target class.

        Returns:
            Mapping of model class name to list of
            ``(mixin_class_name, mixin_module_path)`` tuples.
        """
        result: dict[str, list[tuple[str, str]]] = {}
        ext_dir = self.output_dir.parent / 'ext'
        if not ext_dir.is_dir():
            return result

        for subdir in sorted(ext_dir.iterdir()):
            if not subdir.is_dir() or subdir.name.startswith('_'):
                continue
            init_file = subdir / '__init__.py'
            if not init_file.exists():
                continue
            try:
                plugin = importlib.import_module(f'idfpy.ext.{subdir.name}')
            except Exception:
                logger.warning('Failed to import ext plugin: {}', subdir.name)
                continue
            mixin_map = getattr(plugin, 'MIXIN_MAP', None)
            if not mixin_map or not isinstance(mixin_map, dict):
                continue
            for class_name, mixin_cls in mixin_map.items():
                entry = (mixin_cls.__name__, mixin_cls.__module__)
                result.setdefault(class_name, []).append(entry)

        return result
