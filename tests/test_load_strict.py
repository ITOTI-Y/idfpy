"""Tests for IDF.load() strict mode on IDF text and epJSON input."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from idfpy import IDF, UnknownObjectTypeError
from idfpy.models.simulation import Timestep


def _write_idf(tmp_path: Path, body: str) -> Path:
    path = tmp_path / 'model.idf'
    path.write_text(body, encoding='utf-8')
    return path


VALID_HEAD = 'Version, 26.1;\n\n! comment\nZone,\n  Z1;\n'


@pytest.mark.parametrize(
    ('body', 'error'),
    [
        ('Zonee,\n  Z2;\n', UnknownObjectTypeError),
        ('Zone,\n  Z2,\n  abc;\n', ValidationError),
        ('Zone,\n  Z1;\n', ValueError),
        ('Timestep, 4, 5;\n', ValueError),
    ],
    ids=['unknown-type', 'invalid-value', 'duplicate-name', 'surplus-values'],
)
def test_strict_load_raises_with_source_line(tmp_path, body, error):
    path = _write_idf(tmp_path, VALID_HEAD + body)
    with pytest.raises(error) as exc_info:
        IDF.load(path)
    assert f'{path}:6' in exc_info.value.__notes__[0]


def test_location_points_at_second_object_on_shared_line(tmp_path):
    path = _write_idf(tmp_path, 'Version, 26.1; Zonee, Z2;\n')
    with pytest.raises(UnknownObjectTypeError) as exc_info:
        IDF.load(path)
    assert f'{path}:1' in exc_info.value.__notes__[0]


def test_trailing_empty_values_are_accepted(tmp_path):
    path = _write_idf(tmp_path, 'Timestep, 4, , ;\n')
    assert IDF.load(path).has('Timestep', '_0')


def test_lenient_load_skips_invalid_and_truncates_surplus(tmp_path):
    body = VALID_HEAD + 'Zonee, Z2;\nZone, Z3, abc;\nTimestep, 4, 5;\n'
    idf = IDF.load(_write_idf(tmp_path, body), strict=False)
    assert sorted(idf.types()) == ['Timestep', 'Version', 'Zone']
    assert list(idf.all_of_type('Zone')) == ['Z1']
    assert idf.all_of_type(Timestep)['_0'].number_of_timesteps_per_hour == 4


def test_epjson_strict_load_names_failing_object(tmp_path):
    path = tmp_path / 'model.epJSON'
    data = {'Zone': {'Z1': {'direction_of_relative_north': 'abc'}}}
    path.write_text(json.dumps(data), encoding='utf-8')

    with pytest.raises(ValidationError) as exc_info:
        IDF.load(path)
    assert 'Zone "Z1"' in exc_info.value.__notes__[0]
    assert len(IDF.load(path, strict=False)) == 0
