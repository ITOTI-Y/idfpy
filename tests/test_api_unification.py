"""Tests for the unified query API: type/str symmetry, strict mode, errors."""

from __future__ import annotations

import pytest

from idfpy import IDF, IDFBaseModel, UnknownObjectTypeError
from idfpy.models.thermal_zones import (
    BuildingSurfaceDetailed,
    Zone,
)


def _make_zone(name: str = 'Zone1') -> Zone:
    return Zone(name=name)


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


class _NotAnIDFModel:
    """Placeholder class that is not an IDFBaseModel subclass."""


class TestResolveType:
    def test_accepts_idf_model_class(self):
        assert IDF._resolve_type(Zone) == 'Zone'

    def test_accepts_ep_native_name(self):
        assert IDF._resolve_type('Zone') == 'Zone'
        assert (
            IDF._resolve_type('BuildingSurface:Detailed') == 'BuildingSurface:Detailed'
        )

    def test_accepts_python_class_name(self):
        assert (
            IDF._resolve_type('BuildingSurfaceDetailed') == 'BuildingSurface:Detailed'
        )

    def test_unknown_string_raises_by_default(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF._resolve_type('NoSuchType')

    def test_unknown_string_silent_when_not_strict(self):
        assert IDF._resolve_type('NoSuchType', strict=False) is None

    def test_non_idf_class_raises_by_default(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF._resolve_type(_NotAnIDFModel)  # type: ignore

    def test_non_idf_class_silent_when_not_strict(self):
        assert (
            IDF._resolve_type(_NotAnIDFModel, strict=False)  # type: ignore
            is None
        )


class TestApiSymmetry:
    def test_get_class_equals_ep_name(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        assert idf.get(Zone, 'Zone1') is idf.get('Zone', 'Zone1') is zone

    def test_has_class_equals_ep_name(self):
        idf = IDF()
        idf.add(_make_zone())
        assert idf.has(Zone, 'Zone1') is idf.has('Zone', 'Zone1') is True

    def test_all_of_type_class_equals_ep_name(self):
        idf = IDF()
        idf.add(_make_zone('A'))
        idf.add(_make_zone('B'))
        by_class = idf.all_of_type(Zone)
        by_str = idf.all_of_type('Zone')
        assert set(by_class) == set(by_str) == {'A', 'B'}

    def test_remove_class_equals_ep_name(self):
        idf = IDF()
        idf.add(_make_zone())
        removed = idf.remove(Zone, 'Zone1')
        assert removed is not None and removed.name == 'Zone1'
        assert not idf.has(Zone, 'Zone1')

    def test_get_via_python_class_name(self):
        idf = IDF()
        surface = _make_surface()
        idf.add(surface)
        via_str = idf.get('BuildingSurfaceDetailed', 'Wall1')
        via_class = idf.get(BuildingSurfaceDetailed, 'Wall1')
        assert via_str is via_class is surface

    def test_has_via_python_class_name(self):
        idf = IDF()
        idf.add(_make_surface())
        assert idf.has('BuildingSurfaceDetailed', 'Wall1') is True
        assert idf.has(BuildingSurfaceDetailed, 'Wall1') is True

    def test_all_of_type_via_python_class_name(self):
        idf = IDF()
        idf.add(_make_surface('W1'))
        idf.add(_make_surface('W2'))
        assert set(idf.all_of_type('BuildingSurfaceDetailed')) == {'W1', 'W2'}
        assert set(idf.all_of_type(BuildingSurfaceDetailed)) == {'W1', 'W2'}

    def test_remove_via_python_class_name(self):
        idf = IDF()
        idf.add(_make_surface())
        removed = idf.remove(BuildingSurfaceDetailed, 'Wall1')
        assert removed is not None and removed.name == 'Wall1'


class TestStrictMode:
    def test_get_unknown_type_raises(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF().get('NoSuchType', 'x')

    def test_has_unknown_type_raises(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF().has('NoSuchType', 'x')

    def test_all_of_type_unknown_type_raises(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF().all_of_type('NoSuchType')

    def test_remove_unknown_type_raises(self):
        with pytest.raises(UnknownObjectTypeError):
            IDF().remove('NoSuchType', 'x')

    def test_existing_type_with_missing_name_is_silent(self):
        idf = IDF()
        idf.add(_make_zone())
        assert idf.get(Zone, 'NoSuchName') is None
        assert idf.has(Zone, 'NoSuchName') is False

    def test_strict_false_opts_out(self):
        idf = IDF()
        assert idf.get('NoSuchType', 'x', strict=False) is None
        assert idf.has('NoSuchType', 'x', strict=False) is False
        assert idf.all_of_type('NoSuchType', strict=False) == {}
        assert idf.remove('NoSuchType', 'x', strict=False) is None

    def test_strict_default_is_true(self):
        """Regression guard: default must stay True (fail-fast principle)."""
        with pytest.raises(UnknownObjectTypeError):
            IDF().has('Typo', 'x')

    def test_error_message_contains_key_and_hint(self):
        try:
            IDF().has('MyTypo', 'x')
        except UnknownObjectTypeError as e:
            msg = str(e)
            assert 'MyTypo' in msg
            assert 'EnergyPlus' in msg
            assert e.key == 'MyTypo'
        else:
            pytest.fail('Expected UnknownObjectTypeError')

    def test_error_key_preserves_class_object(self):
        try:
            IDF()._resolve_type(_NotAnIDFModel)  # type: ignore
        except UnknownObjectTypeError as e:
            assert e.key is _NotAnIDFModel
            assert '_NotAnIDFModel' in str(e)
        else:
            pytest.fail('Expected UnknownObjectTypeError')

    def test_unknown_object_type_error_is_value_error(self):
        with pytest.raises(ValueError):
            IDF().has('NoSuchType', 'x')


class TestReferencingAlignment:
    def test_referencing_accepts_class(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)
        refs = zone.referencing(BuildingSurfaceDetailed)
        assert len(refs) == 1 and refs[0] is surface

    def test_referencing_accepts_python_class_name(self):
        idf = IDF()
        zone = _make_zone()
        surface = _make_surface()
        idf.add(zone)
        idf.add(surface)
        refs = zone.referencing('BuildingSurfaceDetailed')
        assert len(refs) == 1 and refs[0] is surface

    def test_referencing_unknown_type_raises(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        with pytest.raises(UnknownObjectTypeError):
            zone.referencing('NoSuchType')

    def test_referencing_unknown_type_silent_when_not_strict(self):
        idf = IDF()
        zone = _make_zone()
        idf.add(zone)
        assert zone.referencing('NoSuchType', strict=False) == []

    def test_referencing_unbound_raises_runtime_error(self):
        zone = _make_zone()
        with pytest.raises(RuntimeError):
            zone.referencing()


def test_unknown_object_type_error_exported_from_top_level():
    """Regression guard: top-level re-export of the exception."""
    from idfpy import UnknownObjectTypeError as Exported

    assert Exported is UnknownObjectTypeError


def test_public_api_types_preserved():
    """The four query methods must accept both type and str uniformly."""
    idf = IDF()
    idf.add(_make_zone())
    # If any signature regresses, one of these calls fails type-check or runtime.
    for fn_call in (
        lambda: idf.has(Zone, 'Zone1'),
        lambda: idf.get(Zone, 'Zone1'),
        lambda: idf.all_of_type(Zone),
    ):
        fn_call()
    # remove (separate since it mutates)
    assert idf.remove(Zone, 'Zone1') is not None


def test_idf_base_model_import():
    """IDFBaseModel is re-exported at top level (sanity)."""
    assert issubclass(Zone, IDFBaseModel)
