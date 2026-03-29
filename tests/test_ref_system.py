"""Tests for the reference system: binding, forward/reverse nav, validation."""

from __future__ import annotations

import pytest

from idfpy import IDF, RefValidationError
from idfpy.models.constructions import Construction
from idfpy.models.internal_gains import Lights
from idfpy.models.schedules import ScheduleCompact
from idfpy.models.thermal_zones import (
    BuildingSurfaceDetailed,
    BuildingSurfaceDetailedVerticesItem,
    Zone,
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
