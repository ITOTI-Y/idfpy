"""Tests for IDF.merge_dict(), from_dict() strict param, and add() singleton check."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from idfpy import IDF
from idfpy.models import SINGLETON_TYPES
from idfpy.models._errors import UnknownObjectTypeError
from idfpy.models.constructions import Construction
from idfpy.models.simulation import Building, SimulationControl, Version
from idfpy.models.thermal_zones import BuildingSurfaceDetailed, Zone


def _zone_dict(name: str = 'Z1', north: float = 0.0) -> dict:
    return {name: {'direction_of_relative_north': north}}


def _building_dict(name: str = 'B1', north_axis: float = 0.0) -> dict:
    return {name: {'north_axis': north_axis}}


def test_merge_into_empty_idf():
    idf = IDF()
    idf.merge_dict({'Zone': _zone_dict('Z1')})
    assert len(idf) == 1
    assert idf.has('Zone', 'Z1')


def test_merge_non_conflicting():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    idf.merge_dict({'Zone': _zone_dict('Z2', north=45.0)})
    assert len(idf) == 2
    assert idf.has('Zone', 'Z1')
    assert idf.has('Zone', 'Z2')
    z2 = idf.get('Zone', 'Z2')
    assert z2.direction_of_relative_north == 45.0  # type: ignore


def test_named_conflict_raise():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    original_len = len(idf)
    with pytest.raises(ValueError, match='already exists'):
        idf.merge_dict({'Zone': _zone_dict('Z1', north=99.0)})
    assert len(idf) == original_len
    z1 = idf.get('Zone', 'Z1')
    assert z1.direction_of_relative_north == 0.0  # type: ignore


def test_named_conflict_skip():
    idf = IDF()
    idf.add(Zone(name='Z1', direction_of_relative_north=10.0))
    idf.merge_dict(
        {'Zone': _zone_dict('Z1', north=99.0)},
        on_conflict='skip',
    )
    z1 = idf.get('Zone', 'Z1')
    assert z1.direction_of_relative_north == 10.0  # type: ignore


def test_named_conflict_replace():
    idf = IDF()
    idf.add(Zone(name='Z1', direction_of_relative_north=10.0))
    idf.merge_dict(
        {'Zone': _zone_dict('Z1', north=99.0)},
        on_conflict='replace',
    )
    z1 = idf.get('Zone', 'Z1')
    assert z1.direction_of_relative_north == 99.0  # type: ignore


def test_replace_preserves_reference_integrity():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    idf.add(
        Construction(name='Const1', outside_layer='SomeMaterial'),
    )
    idf.add(
        BuildingSurfaceDetailed(
            name='Wall1',
            surface_type='Wall',
            construction_name='Const1',
            zone_name='Z1',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
        ),
    )

    idf.merge_dict(
        {'Zone': {'Z1': {'direction_of_relative_north': 45.0}}},
        on_conflict='replace',
    )

    wall = idf.get('BuildingSurface:Detailed', 'Wall1')
    assert wall is not None
    zone_ref = wall.zone_name  # type: ignore
    assert zone_ref == 'Z1'

    errors = idf.validate()
    ref_errors = [e for e in errors if e.field_name == 'zone_name']
    assert len(ref_errors) == 0


def test_nameless_non_singleton_merge():
    idf = IDF()
    data = {
        'Output:Variable': {
            'Output:Variable 1': {
                'key_value': '*',
                'variable_name': 'Zone Mean Air Temperature',
                'reporting_frequency': 'Timestep',
            },
        },
    }
    idf.merge_dict(data)
    assert len(idf.all_of_type('Output:Variable')) == 1


def test_unknown_type_strict_true():
    idf = IDF()
    with pytest.raises(UnknownObjectTypeError):
        idf.merge_dict({'FakeObject:NonExistent': {'X': {}}})


def test_unknown_type_strict_false():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    idf.merge_dict(
        {
            'FakeObject:NonExistent': {'X': {}},
            'Zone': _zone_dict('Z2'),
        },
        strict=False,
    )
    assert idf.has('Zone', 'Z2')
    assert len(idf) == 2


def test_validation_error_strict_true():
    idf = IDF()
    with pytest.raises(ValidationError):
        idf.merge_dict(
            {
                'BuildingSurface:Detailed': {
                    'Bad': {'surface_type': 'INVALID_ENUM_VALUE'},
                },
            }
        )


def test_validation_error_strict_false():
    idf = IDF()
    idf.merge_dict(
        {
            'BuildingSurface:Detailed': {
                'Bad': {'surface_type': 'INVALID_ENUM_VALUE'},
            },
            'Zone': _zone_dict('Z1'),
        },
        strict=False,
    )
    assert idf.has('Zone', 'Z1')


def test_invalid_top_level_type():
    idf = IDF()
    with pytest.raises(ValueError, match='top-level dict'):
        idf.merge_dict('not a dict')  # type: ignore


def test_singleton_merge_raise():
    idf = IDF()
    idf.add(SimulationControl())
    with pytest.raises(ValueError, match='singleton'):
        idf.merge_dict(
            {
                'SimulationControl': {
                    'SimulationControl 1': {
                        'do_zone_sizing_calculation': 'Yes',
                    },
                },
            }
        )


def test_singleton_merge_replace():
    idf = IDF()
    idf.add(SimulationControl(do_zone_sizing_calculation='No'))
    idf.merge_dict(
        {
            'SimulationControl': {
                'SimulationControl 1': {
                    'do_zone_sizing_calculation': 'Yes',
                },
            },
        },
        on_conflict='replace',
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'Yes'  # type: ignore


def test_singleton_merge_skip():
    idf = IDF()
    idf.add(SimulationControl(do_zone_sizing_calculation='No'))
    idf.merge_dict(
        {
            'SimulationControl': {
                'SimulationControl 1': {
                    'do_zone_sizing_calculation': 'Yes',
                },
            },
        },
        on_conflict='skip',
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'No'  # type: ignore


def test_add_duplicate_singleton():
    idf = IDF()
    idf.add(Version())
    with pytest.raises(ValueError, match='Singleton constraint'):
        idf.add(Version())


def test_add_named_singleton_different_name():
    idf = IDF()
    idf.add(Building(name='A'))
    with pytest.raises(ValueError, match='Singleton constraint'):
        idf.add(Building(name='B'))


def test_named_singleton_merge_replace_different_name():
    idf = IDF()
    idf.add(Building(name='A', north_axis=0.0))
    idf.merge_dict(
        {'Building': _building_dict('B', north_axis=45.0)},
        on_conflict='replace',
    )
    assert not idf.has('Building', 'A', strict=False)
    assert idf.has('Building', 'B', strict=False)
    b = idf.get('Building', 'B', strict=False)
    assert b.north_axis == 45.0  # type: ignore
    assert len(idf.all_of_type('Building')) == 1
    errors = idf.validate()
    building_errors = [e for e in errors if e.object_type == 'Building']
    assert building_errors == []


def test_from_dict_unknown_type_strict_true():
    with pytest.raises(UnknownObjectTypeError):
        IDF.from_dict({'FakeType': {'X': {}}})


def test_from_dict_unknown_type_strict_false():
    idf = IDF.from_dict(
        {
            'FakeType': {'X': {}},
            'Zone': _zone_dict('Z1'),
        },
        strict=False,
    )
    assert idf.has('Zone', 'Z1')


def test_merge_atomic_on_validation_error():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    original_len = len(idf)
    with pytest.raises(ValidationError):
        idf.merge_dict(
            {
                'Zone': _zone_dict('Z2'),
                'BuildingSurface:Detailed': {
                    'Bad': {'surface_type': 'INVALID_ENUM_VALUE'},
                },
            }
        )
    assert len(idf) == original_len
    assert not idf.has('Zone', 'Z2')
    assert idf.has('Zone', 'Z1')


def test_merge_atomic_on_conflict_raise():
    idf = IDF()
    idf.add(Zone(name='Z1'))
    original_len = len(idf)
    with pytest.raises(ValueError, match='already exists'):
        idf.merge_dict(
            {
                'Zone': {
                    'Z2': {'direction_of_relative_north': 10.0},
                    'Z1': {'direction_of_relative_north': 99.0},
                },
            }
        )
    assert len(idf) == original_len
    assert not idf.has('Zone', 'Z2')
    z1 = idf.get('Zone', 'Z1')
    assert z1.direction_of_relative_north == 0.0  # type: ignore


def test_singleton_multiple_entries_replace():
    idf = IDF()
    idf.add(SimulationControl(do_zone_sizing_calculation='No'))
    idf.merge_dict(
        {
            'SimulationControl': {
                'SC1': {'do_zone_sizing_calculation': 'Yes'},
                'SC2': {'do_zone_sizing_calculation': 'No'},
            },
        },
        on_conflict='replace',
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'No'  # type: ignore


def test_invalid_on_conflict_value():
    idf = IDF()
    with pytest.raises(ValueError, match='on_conflict must be one of'):
        idf.merge_dict({'Zone': _zone_dict('Z1')}, on_conflict='invalid')  # type: ignore


def test_intra_data_singleton_raise():
    idf = IDF()
    with pytest.raises(ValueError, match='multiple entries'):
        idf.merge_dict(
            {
                'SimulationControl': {
                    'SC1': {'do_zone_sizing_calculation': 'Yes'},
                    'SC2': {'do_zone_sizing_calculation': 'No'},
                },
            },
        )
    assert len(idf.all_of_type('SimulationControl')) == 0


def test_intra_data_singleton_skip():
    idf = IDF()
    idf.merge_dict(
        {
            'SimulationControl': {
                'SC1': {'do_zone_sizing_calculation': 'Yes'},
                'SC2': {'do_zone_sizing_calculation': 'No'},
            },
        },
        on_conflict='skip',
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'Yes'  # type: ignore


def test_intra_data_singleton_replace():
    idf = IDF()
    idf.merge_dict(
        {
            'SimulationControl': {
                'SC1': {'do_zone_sizing_calculation': 'Yes'},
                'SC2': {'do_zone_sizing_calculation': 'No'},
            },
        },
        on_conflict='replace',
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'No'  # type: ignore


def test_singleton_replace_keeps_first_when_second_invalid():
    idf = IDF()
    idf.merge_dict(
        {
            'SimulationControl': {
                'SC1': {'do_zone_sizing_calculation': 'Yes'},
                'SC2': {'do_zone_sizing_calculation': 'INVALID'},
            },
        },
        on_conflict='replace',
        strict=False,
    )
    sims = idf.all_of_type('SimulationControl')
    assert len(sims) == 1
    obj = next(iter(sims.values()))
    assert obj.do_zone_sizing_calculation == 'Yes'  # type: ignore


def test_singleton_types_contents():
    assert 'Building' in SINGLETON_TYPES
    assert 'Version' in SINGLETON_TYPES
    assert 'SimulationControl' in SINGLETON_TYPES
    assert 'Zone' not in SINGLETON_TYPES
    assert len(SINGLETON_TYPES) >= 50
