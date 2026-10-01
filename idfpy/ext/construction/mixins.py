"""Layer access and classification mixin for ``Construction``."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from idfpy.models._base import IDFBaseModel
    from idfpy.models.constructions import Construction

# ``functions`` imports the window-material classes from
# ``idfpy.models.constructions``, which itself imports this mixin; the
# imports below are deferred to break that cycle.


class ConstructionLayersMixin:
    """Ordered layer access and window/opaque classification."""

    @property
    def layers(self: Construction) -> list[IDFBaseModel]:
        """Materials from outside to inside (see ``construction_layers``)."""
        from .functions import construction_layers

        return construction_layers(self)

    @property
    def is_window_construction(self: Construction) -> bool:
        """Whether every layer is a window material (glazing, gas or shading)."""
        from .functions import construction_layers, is_window_material

        return all(is_window_material(m) for m in construction_layers(self))

    @property
    def is_opaque_construction(self: Construction) -> bool:
        """Whether no layer is a window material."""
        from .functions import construction_layers, is_window_material

        return not any(is_window_material(m) for m in construction_layers(self))
