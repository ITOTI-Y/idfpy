"""Tests for the construction ext plugin: layer resolution and classification."""

from __future__ import annotations

import pytest

import idfpy.models as models
from idfpy import IDF
from idfpy.ext.construction.functions import is_window_material
from idfpy.models._ref_meta import REF_PROVIDERS
from idfpy.models.constructions import (
    Construction,
    Material,
    WindowMaterialGas,
    WindowMaterialGlazing,
    WindowMaterialSimpleGlazingSystem,
)

OPAQUE_LAYER_TYPES = {
    'Material',
    'Material:AirGap',
    'Material:InfraredTransparent',
    'Material:NoMass',
    'Material:RoofVegetation',
}
WINDOW_LAYER_TYPES = {
    'WindowMaterial:Blind',
    'WindowMaterial:Gas',
    'WindowMaterial:GasMixture',
    'WindowMaterial:Glazing',
    'WindowMaterial:Glazing:RefractionExtinctionMethod',
    'WindowMaterial:GlazingGroup:Thermochromic',
    'WindowMaterial:Screen',
    'WindowMaterial:Shade',
    'WindowMaterial:SimpleGlazingSystem',
}


def _layer_material_classes() -> dict[str, type[models.IDFBaseModel]]:
    layer_types = {
        object_type
        for object_type, fields in REF_PROVIDERS.items()
        if any('MaterialName' in groups for _, groups in fields)
    }
    classes = (getattr(models, name) for name in models.__all__)
    return {
        cls.idf_object_type(): cls
        for cls in classes
        if isinstance(cls, type)
        and issubclass(cls, models.IDFBaseModel)
        and getattr(cls, '_idf_object_type', None) in layer_types
    }


@pytest.fixture
def idf() -> IDF:
    idf = IDF()
    idf.add(
        Material(
            name='Brick',
            roughness='Rough',
            thickness=0.1,
            conductivity=0.9,
            density=1900.0,
            specific_heat=800.0,
        )
    )
    idf.add(
        WindowMaterialGlazing(
            name='Clear3mm', optical_data_type='SpectralAverage', thickness=0.003
        )
    )
    idf.add(WindowMaterialGas(name='Air13mm', gas_type='Air', thickness=0.013))
    idf.add(
        WindowMaterialSimpleGlazingSystem(
            name='SGS', u_factor=2.5, solar_heat_gain_coefficient=0.4
        )
    )
    return idf


def _add(idf: IDF, name: str, *layers: str) -> Construction:
    fields = ['outside_layer', *(f'layer_{i}' for i in range(2, 11))]
    construction = Construction(name=name, **dict(zip(fields, layers, strict=False)))
    idf.add(construction)
    return construction


class TestIsWindowMaterial:
    def test_partition_of_layer_material_types(self):
        classes = _layer_material_classes()
        assert set(classes) == OPAQUE_LAYER_TYPES | WINDOW_LAYER_TYPES

        window = {
            t for t, cls in classes.items() if is_window_material(cls.model_construct())
        }
        assert window == WINDOW_LAYER_TYPES


class TestLayers:
    def test_order_and_repeats(self, idf: IDF):
        construction = _add(idf, 'Dbl', 'Clear3mm', 'Air13mm', 'Clear3mm')
        glass = idf.get(WindowMaterialGlazing, 'Clear3mm')
        gas = idf.get(WindowMaterialGas, 'Air13mm')
        assert construction.layers == [glass, gas, glass]

    def test_unknown_material_raises(self, idf: IDF):
        construction = _add(idf, 'Broken', 'Brick', 'Missing')
        with pytest.raises(
            LookupError, match="'Broken' references unknown material 'Missing'"
        ):
            _ = construction.layers

    def test_unbound_raises(self):
        construction = Construction(name='Loose', outside_layer='Brick')
        with pytest.raises(RuntimeError):
            _ = construction.layers


class TestClassification:
    @pytest.mark.parametrize(
        ('layers', 'is_window', 'is_opaque'),
        [
            (('Brick',), False, True),
            (('SGS',), True, False),
            (('Clear3mm', 'Air13mm', 'Clear3mm'), True, False),
            (('Brick', 'Clear3mm'), False, False),
            (('Clear3mm', 'Brick'), False, False),
        ],
    )
    def test_window_and_opaque(
        self, idf: IDF, layers: tuple[str, ...], is_window: bool, is_opaque: bool
    ):
        construction = _add(idf, 'C', *layers)
        assert construction.is_window_construction is is_window
        assert construction.is_opaque_construction is is_opaque
