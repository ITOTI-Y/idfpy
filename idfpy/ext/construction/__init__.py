"""Construction extension — ordered layers and window/opaque classification."""

from .mixins import ConstructionLayersMixin

MIXIN_MAP: dict[str, type] = {
    'Construction': ConstructionLayersMixin,
}
