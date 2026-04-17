"""Tests for the reference system: binding, forward/reverse nav, validation."""

from __future__ import annotations

import pytest

from idfpy import IDF, RefValidationError
from idfpy.models.constructions import Construction
from idfpy.models.fluids import FluidPropertiesName, FluidPropertiesSaturated
from idfpy.models.internal_gains import Lights
from idfpy.models.misc import (
    AirflowNetworkMultiZoneComponentZoneExhaustFan,
    AirflowNetworkMultiZoneSurface,
    AirflowNetworkMultiZoneZone,
)
from idfpy.models.schedules import ScheduleCompact
from idfpy.models.thermal_zones import (
    BuildingSurfaceDetailed,
    BuildingSurfaceDetailedVerticesItem,
    Zone,
    ZoneList,
    ZoneListZonesItem,
)

# ── Helpers ──────────────────────────────────────────────


def _make_zone(name: str = 'Zone1') -> Zone:
    return Zone(name=name)


def _make_construction(name: str = 'Const1') -> Construction:
    return Construction(name=name, outside_layer='SomeMaterial')


def _make_surface(
    name: str = 'Wall1',
    zone_name: str = 'Zone1',
    construction_name: str = 'Const1',
) -> BuildingSurfaceDetailed:
    return BuildingSurfaceDetailed(
        name=name,
        surface_type='Wall',
        construction_name=construction_name,
        zone_name=zone_name,
        outside_boundary_condition='Outdoors',
    )


def _make_schedule(name: str = 'Sched1') -> ScheduleCompact:
    return ScheduleCompact(name=name, schedule_type_limits_name='')


def _make_lights(
    name: str = 'Light1',
    zone_name: str = 'Zone1',
    schedule_name: str = 'Sched1',
) -> Lights:
    return Lights(
        name=name,
        zone_or_zonelist_or_space_or_spacelist_name=zone_name,
        schedule_name=schedule_name,
    )


# ── Binding ──────────────────────────────────────────────


class TestBinding:
    def test_add_binds_object(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        assert zone._idf is idf

    def test_add_binds_extensible_items(self):
        idf = IDF()
        verts = [
            BuildingSurfaceDetailedVerticesItem(
                vertex_x_coordinate=0, vertex_y_coordinate=0, vertex_z_coordinate=0
            ),
            BuildingSurfaceDetailedVerticesItem(
                vertex_x_coordinate=1, vertex_y_coordinate=0, vertex_z_coordinate=0
            ),
            BuildingSurfaceDetailedVerticesItem(
                vertex_x_coordinate=1, vertex_y_coordinate=1, vertex_z_coordinate=1
            ),
        ]
        surface = BuildingSurfaceDetailed(
            name='Wall1',
            surface_type='Wall',
            construction_name='C1',
            zone_name='Z1',
            outside_boundary_condition='Outdoors',
            vertices=verts,
        )
        idf.add(surface)
        assert surface._idf is idf
        assert surface.vertices is not None
        for vertex in surface.vertices:
            assert vertex._idf is idf

    def test_unbound_object_idf_is_none(self):
        zone = _make_zone()
        assert zone._idf is None

    def test_remove_unbinds_object(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        assert zone._idf is idf
        idf.remove('Zone', 'Zone1')
        assert zone._idf is None

    def test_serialization_excludes_idf_ref(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        d = zone.model_dump()
        assert '_idf_ref' not in d


# ── Forward Navigation ───────────────────────────────────


class TestForwardNav:
    def test_basic_forward_nav(self):
        idf = IDF()
        zone = _make_zone()
        construction = _make_construction()
        surface = _make_surface()
        idf.add(zone)
        idf.add(construction)
        idf.add(surface)

        assert surface.zone is zone
        assert surface.construction is construction

    def test_forward_nav_optional_none(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)

        # space_name is not set, so space should be None
        assert surface.space is None

    def test_forward_nav_missing_target(self):
        idf = IDF()
        # Zone not added, surface references it
        surface = _make_surface(zone_name='NonExistent')
        idf.add(surface)

        # Forward nav returns None for missing target
        assert surface.zone is None

    def test_forward_nav_case_insensitive(self):
        idf = IDF()
        zone = _make_zone('MyZone')
        # Surface references zone with different case
        surface = _make_surface(zone_name='myzone')
        idf.add(zone)
        idf.add(surface)

        assert surface.zone is zone

    def test_forward_nav_unbound_raises(self):
        surface = _make_surface()
        with pytest.raises(RuntimeError, match='Not bound to IDF'):
            _ = surface.zone


# ── Reverse Navigation ──────────────────────────────────


class TestReverseNav:
    def test_referencing_basic(self):
        idf = IDF()
        zone = _make_zone()
        surface1 = _make_surface('Wall1', 'Zone1')
        surface2 = _make_surface('Wall2', 'Zone1')
        idf.add(zone)
        idf.add(surface1)
        idf.add(surface2)

        refs = zone.referencing('BuildingSurface:Detailed')
        assert len(refs) == 2
        assert surface1 in refs
        assert surface2 in refs

    def test_referencing_empty(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)

        refs = zone.referencing('BuildingSurface:Detailed')
        assert refs == []

    def test_referencing_by_class(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)

        refs = zone.referencing(BuildingSurfaceDetailed)
        assert len(refs) == 1
        assert refs[0] is surface

    def test_referencing_unbound_raises(self):
        zone = _make_zone()
        with pytest.raises(RuntimeError, match='Not bound to IDF'):
            zone.referencing('BuildingSurface:Detailed')

    def test_referencing_polymorphic(self):
        """Zone is referenced by both surfaces and lights."""
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        schedule = _make_schedule()
        light = _make_lights()
        idf.add(zone)
        idf.add(surface)
        idf.add(schedule)
        idf.add(light)

        surfaces = zone.referencing('BuildingSurface:Detailed')
        assert len(surfaces) == 1
        lights = zone.referencing('Lights')
        assert len(lights) == 1
        assert lights[0] is light

    def test_referencing_all(self):
        """referencing() with no args returns all referencing objects."""
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        schedule = _make_schedule()
        light = _make_lights()
        idf.add(zone)
        idf.add(surface)
        idf.add(schedule)
        idf.add(light)

        all_refs = zone.referencing()
        assert surface in all_refs
        assert light in all_refs

    def test_referencing_all_empty(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)

        assert zone.referencing() == []

    def test_referencing_all_unbound_raises(self):
        zone = _make_zone()
        with pytest.raises(RuntimeError, match='Not bound to IDF'):
            zone.referencing()


# ── Validation ───────────────────────────────────────────


class TestValidation:
    def test_validate_clean(self):
        idf = IDF()
        zone = _make_zone()
        construction = _make_construction()
        surface = _make_surface()
        idf.add(zone)
        idf.add(construction)
        idf.add(surface)

        # Zone and Construction are valid references
        errors = idf.validate()
        # Filter out errors for fields we didn't provide (like materials)
        surface_errors = [
            e
            for e in errors
            if e.object_type == 'BuildingSurface:Detailed'
            and e.field_name in ('zone_name', 'construction_name')
        ]
        assert surface_errors == []

    def test_validate_missing_ref(self):
        idf = IDF()
        # Surface references non-existent zone
        surface = _make_surface(zone_name='GhostZone')
        idf.add(surface)

        errors = idf.validate()
        zone_errors = [
            e
            for e in errors
            if e.field_name == 'zone_name' and e.referenced_name == 'GhostZone'
        ]
        assert len(zone_errors) == 1
        assert zone_errors[0].error_type == 'missing'

    def test_validate_or_raise_clean(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        # Zone has no consumer fields itself, so no errors
        idf.validate_or_raise()

    def test_validate_or_raise_broken(self):
        idf = IDF()
        surface = _make_surface(zone_name='Missing')
        idf.add(surface)

        with pytest.raises(RefValidationError) as exc_info:
            idf.validate_or_raise()
        assert len(exc_info.value.errors) > 0


# ── Remove ───────────────────────────────────────────────


class TestRemove:
    def test_remove_returns_object(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        removed = idf.remove('Zone', 'Zone1')
        assert removed is zone

    def test_remove_nonexistent_returns_none(self):
        idf = IDF()
        assert idf.remove('Zone', 'Nope') is None

    def test_remove_unregisters_refs(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)

        # Forward nav works before removal
        assert surface.zone is zone

        # Remove zone
        idf.remove('Zone', 'Zone1')

        # Forward nav returns None after removal
        assert surface.zone is None

    def test_remove_unbinds_recursive(self):
        idf = IDF()
        vert = BuildingSurfaceDetailedVerticesItem(
            vertex_x_coordinate=0, vertex_y_coordinate=0, vertex_z_coordinate=0
        )
        surface = BuildingSurfaceDetailed(
            name='Wall1',
            surface_type='Wall',
            construction_name='C1',
            zone_name='Z1',
            outside_boundary_condition='Outdoors',
            vertices=[vert],
        )
        idf.add(surface)
        assert vert._idf is idf

        idf.remove('BuildingSurface:Detailed', 'Wall1')
        assert surface._idf is None
        assert vert._idf is None


# ── Integration ──────────────────────────────────────────


class TestIntegration:
    def test_from_dict_auto_binds(self):
        data = {
            'Zone': {
                'TestZone': {},
            },
            'BuildingSurface:Detailed': {
                'TestWall': {
                    'surface_type': 'Wall',
                    'construction_name': 'C1',
                    'zone_name': 'TestZone',
                    'outside_boundary_condition': 'Outdoors',
                },
            },
        }
        idf = IDF.from_dict(data)
        zone = idf.get('Zone', 'TestZone')
        assert zone is not None
        surface = idf.get('BuildingSurface:Detailed', 'TestWall')
        assert surface is not None
        assert isinstance(surface, BuildingSurfaceDetailed)

        assert zone._idf is idf
        assert surface._idf is idf
        assert surface.zone is zone

    def test_to_dict_roundtrip_preserves_data(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)

        d = idf.to_dict()
        idf2 = IDF.from_dict(d)

        zone2 = idf2.get('Zone', 'Zone1')
        assert zone2 is not None
        surface2 = idf2.get('BuildingSurface:Detailed', 'Wall1')
        assert surface2 is not None
        assert isinstance(surface2, BuildingSurfaceDetailed)
        # Forward nav works in reloaded IDF
        assert surface2.zone is zone2

    def test_load_idf_binds_objects(self):
        from pathlib import Path

        test_idf = Path(__file__).parent / 'test.idf'
        if not test_idf.exists():
            pytest.skip('test.idf not found')

        idf = IDF.load(test_idf)
        # All objects should be bound
        for obj in idf:
            assert obj._idf is idf


# ── Cascade Rename ──────────────────────────────────────


class TestCascadeRename:
    """T1-T11: cascade rename of provider fields."""

    def test_basic_zone_rename(self):
        """T1: Zone.name change cascades to Lights consumer."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        schedule = _make_schedule()
        light = _make_lights('Light1', 'Zone 1', 'Sched1')
        idf.add(zone)
        idf.add(schedule)
        idf.add(light)

        zone.name = 'Zone 2'

        assert light.zone_or_zonelist_or_space_or_spacelist_name == 'Zone 2'
        assert idf.get('Zone', 'Zone 2') is zone
        assert idf.get('Zone', 'Zone 1') is None

    def test_roundtrip_after_rename(self):
        """T2: save/load roundtrip after rename preserves references."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        schedule = _make_schedule()
        light = _make_lights('Light1', 'Zone 1', 'Sched1')
        idf.add(zone)
        idf.add(schedule)
        idf.add(light)

        zone.name = 'Zone 2'

        d = idf.to_dict()
        idf2 = IDF.from_dict(d)
        zone2 = idf2.get(Zone, 'Zone 2')
        light2 = idf2.get(Lights, 'Light1')
        assert zone2 is not None
        assert light2 is not None
        assert light2.zone_or_zonelist_or_space_or_spacelist_name == 'Zone 2'

    def test_two_level_cascade_afn_zone(self):
        """T3a: Zone → AFN:MultiZone:Zone (L1 consumer+provider)."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        idf.add(zone)
        afn_zone = AirflowNetworkMultiZoneZone(zone_name='Zone 1')
        idf.add(afn_zone)

        zone.name = 'Zone 2'

        assert afn_zone.zone_name == 'Zone 2'
        assert idf.get('AirflowNetwork:MultiZone:Zone', 'Zone 2') is afn_zone
        assert idf.get('AirflowNetwork:MultiZone:Zone', 'Zone 1') is None

    def test_two_level_cascade_fan_exhaust(self):
        """T3b: Fan:ZoneExhaust → AFN:Component:ZoneExhaustFan → AFN:Surface."""
        from idfpy.models.fans import FanZoneExhaust

        idf = IDF()
        fan = FanZoneExhaust(
            name='ExhFan1',
            pressure_rise=0.0,
            air_inlet_node_name='InNode',
            air_outlet_node_name='OutNode',
        )
        idf.add(fan)
        afn_exhaust = AirflowNetworkMultiZoneComponentZoneExhaustFan(
            name='ExhFan1',
            air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions=0.01,
        )
        idf.add(afn_exhaust)
        surface = AirflowNetworkMultiZoneSurface(
            surface_name='Wall1',
            leakage_component_name='ExhFan1',
        )
        idf.add(surface)

        fan.name = 'ExhFan2'

        assert afn_exhaust.name == 'ExhFan2'
        assert surface.leakage_component_name == 'ExhFan2'
        assert idf.get('Fan:ZoneExhaust', 'ExhFan2') is fan
        assert (
            idf.get('AirflowNetwork:MultiZone:Component:ZoneExhaustFan', 'ExhFan2')
            is afn_exhaust
        )

    def test_two_level_cascade_hvac_template(self):
        """T3c: Zone → HVACTemplate:Zone:ConstantVolume."""
        from idfpy.models.hvac_templates import HVACTemplateZoneConstantVolume

        idf = IDF()
        zone = _make_zone('Zone 1')
        idf.add(zone)
        hvac = HVACTemplateZoneConstantVolume(
            zone_name='Zone 1',
            template_constant_volume_system_name='Sys1',
        )
        idf.add(hvac)

        zone.name = 'Zone 2'

        assert hvac.zone_name == 'Zone 2'
        assert idf.get('HVACTemplate:Zone:ConstantVolume', 'Zone 2') is hvac

    def test_noop_same_value(self):
        """T4: old == new does not trigger cascade."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        schedule = _make_schedule()
        light = _make_lights('Light1', 'Zone 1', 'Sched1')
        idf.add(zone)
        idf.add(schedule)
        idf.add(light)

        zone.name = 'Zone 1'

        assert light.zone_or_zonelist_or_space_or_spacelist_name == 'Zone 1'
        assert idf.get('Zone', 'Zone 1') is zone

    def test_unbound_object_no_cascade(self):
        """T5: unbound object assignment is plain Pydantic."""
        zone = Zone(name='Z1')
        zone.name = 'Z2'
        assert zone.name == 'Z2'

    def test_non_name_provider_fluid(self):
        """T6: FluidProperties:Name.fluid_name cascade, _objects key stays _0."""
        idf = IDF()
        fluid = FluidPropertiesName(fluid_name='Water', fluid_type='Glycol')
        idf.add(fluid)
        consumer = FluidPropertiesSaturated(fluid_name='Water')
        idf.add(consumer)

        fluid.fluid_name = 'Glycol50'

        assert consumer.fluid_name == 'Glycol50'
        # _objects key is auto-generated, should NOT change
        assert idf.get('FluidProperties:Name', fluid._idf_obj_key) is fluid

    def test_non_name_provider_afn_zone(self):
        """T7: AFN:MultiZone:Zone uses zone_name as _objects key."""
        idf = IDF()
        afn_zone = AirflowNetworkMultiZoneZone(zone_name='Office')
        idf.add(afn_zone)

        assert afn_zone._idf_obj_key == 'Office'

        afn_zone.zone_name = 'MainOffice'

        assert idf.get('AirflowNetwork:MultiZone:Zone', 'MainOffice') is afn_zone
        assert idf.get('AirflowNetwork:MultiZone:Zone', 'Office') is None

    def test_validate_after_rename(self):
        """T8: validate() returns 0 errors after rename."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        construction = _make_construction()
        surface = _make_surface('Wall1', 'Zone 1', 'Const1')
        schedule = _make_schedule()
        light = _make_lights('Light1', 'Zone 1', 'Sched1')
        idf.add(zone)
        idf.add(construction)
        idf.add(surface)
        idf.add(schedule)
        idf.add(light)

        zone.name = 'NewZone'

        errors = idf.validate()
        zone_errors = [
            e
            for e in errors
            if e.referenced_name in ('Zone 1', 'NewZone') and e.error_type == 'missing'
        ]
        assert zone_errors == []

    def test_extensible_items_cascade(self):
        """T9: ZoneList extensible items update on Zone rename."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        idf.add(zone)
        zone_list = ZoneList(
            name='AllZones',
            zones=[ZoneListZonesItem(zone_name='Zone 1')],
        )
        idf.add(zone_list)

        zone.name = 'Zone 2'

        assert zone_list.zones is not None
        assert zone_list.zones[0].zone_name == 'Zone 2'

    def test_consecutive_renames(self):
        """T10: multiple renames in sequence."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        schedule = _make_schedule()
        light = _make_lights('Light1', 'Zone 1', 'Sched1')
        idf.add(zone)
        idf.add(schedule)
        idf.add(light)

        zone.name = 'Zone 2'
        zone.name = 'Zone 3'

        assert light.zone_or_zonelist_or_space_or_spacelist_name == 'Zone 3'
        assert idf.get('Zone', 'Zone 3') is zone
        assert idf.get('Zone', 'Zone 1') is None
        assert idf.get('Zone', 'Zone 2') is None

    def test_idf_obj_key_reset_on_remove(self):
        """T11: _idf_obj_key cleared after remove."""
        idf = IDF()
        zone = _make_zone('Zone 1')
        idf.add(zone)

        assert zone._idf_obj_key == 'Zone 1'

        idf.remove('Zone', 'Zone 1')

        assert zone._idf_obj_key == ''


# ── Class name string lookup ─────────────────────────────


class TestClassNameLookup:
    """Public API accepts both class name and EnergyPlus name strings."""

    def test_get_by_class_name(self):
        idf = IDF()
        surface = _make_surface()
        idf.add(surface)
        assert idf.get('BuildingSurfaceDetailed', 'Wall1') is surface

    def test_get_by_ep_name_still_works(self):
        idf = IDF()
        surface = _make_surface()
        idf.add(surface)
        assert idf.get('BuildingSurface:Detailed', 'Wall1') is surface

    def test_get_identical_names(self):
        """Types where class name == EP name (e.g. Zone) work."""
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        assert idf.get('Zone', 'Zone1') is zone

    def test_has_by_class_name(self):
        idf = IDF()
        idf.add(_make_surface())
        assert idf.has('BuildingSurfaceDetailed', 'Wall1')
        assert idf.has('BuildingSurface:Detailed', 'Wall1')

    def test_remove_by_class_name(self):
        idf = IDF()
        idf.add(_make_surface())
        obj = idf.remove('BuildingSurfaceDetailed', 'Wall1')
        assert obj is not None
        assert not idf.has('BuildingSurface:Detailed', 'Wall1')

    def test_all_of_type_by_class_name(self):
        idf = IDF()
        idf.add(_make_surface('W1'))
        idf.add(_make_surface('W2'))
        assert len(idf.all_of_type('BuildingSurfaceDetailed')) == 2

    def test_referencing_by_class_name_string(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)
        refs = zone.referencing('BuildingSurfaceDetailed')
        assert len(refs) == 1 and refs[0] is surface

    def test_unknown_type_returns_empty_with_strict_false(self):
        """Legacy silent behavior is preserved via strict=False."""
        idf = IDF()
        assert idf.get('NonExistent', 'x', strict=False) is None
        assert not idf.has('NonExistent', 'x', strict=False)
        assert idf.all_of_type('NonExistent', strict=False) == {}
