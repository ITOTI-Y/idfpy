"""Material classification and layer resolution for layered constructions."""

from __future__ import annotations

from typing import TYPE_CHECKING, Final

from idfpy.models.constructions import (
    WindowMaterialBlind,
    WindowMaterialGas,
    WindowMaterialGasMixture,
    WindowMaterialGlazing,
    WindowMaterialGlazingGroupThermochromic,
    WindowMaterialGlazingRefractionExtinctionMethod,
    WindowMaterialScreen,
    WindowMaterialShade,
    WindowMaterialSimpleGlazingSystem,
)

if TYPE_CHECKING:
    from idfpy.models._base import IDFBaseModel
    from idfpy.models.constructions import Construction

# Window-material layer types accepted by ``Construction`` layer fields.
WINDOW_MATERIAL_TYPES: Final = (
    WindowMaterialBlind,
    WindowMaterialGas,
    WindowMaterialGasMixture,
    WindowMaterialGlazing,
    WindowMaterialGlazingGroupThermochromic,
    WindowMaterialGlazingRefractionExtinctionMethod,
    WindowMaterialScreen,
    WindowMaterialShade,
    WindowMaterialSimpleGlazingSystem,
)


def is_window_material(material: IDFBaseModel) -> bool:
    """Whether ``material`` is a window-material layer (glazing, gas or shading)."""
    return isinstance(material, WINDOW_MATERIAL_TYPES)


def construction_layers(construction: Construction) -> list[IDFBaseModel]:
    """Resolve the layers of a bound construction.

    Args:
        construction: Construction bound to an IDF container.

    Returns:
        Materials from outside to inside; repeated names yield repeated
        entries and empty layer fields are skipped.

    Raises:
        RuntimeError: If the construction is not bound to an IDF.
        LookupError: If a layer name does not resolve to any material.
    """
    c = construction
    slots = (
        (c.outside_layer, c.outside_layer_ref),
        (c.layer_2, c.layer_2_ref),
        (c.layer_3, c.layer_3_ref),
        (c.layer_4, c.layer_4_ref),
        (c.layer_5, c.layer_5_ref),
        (c.layer_6, c.layer_6_ref),
        (c.layer_7, c.layer_7_ref),
        (c.layer_8, c.layer_8_ref),
        (c.layer_9, c.layer_9_ref),
        (c.layer_10, c.layer_10_ref),
    )
    layers: list[IDFBaseModel] = []
    for name, material in slots:
        if not name:
            continue
        if material is None:
            raise LookupError(
                f'Construction {c.name!r} references unknown material {name!r}'
            )
        layers.append(material)
    return layers
