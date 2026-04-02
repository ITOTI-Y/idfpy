"""Geometry extension — surface area, normal, centroid calculations."""

from .mixins import ExtensibleVertexGeometryMixin, FixedVertexGeometryMixin

# Mapping from generated model class name to mixin class.
# The code generator reads this at generation time and injects the mixin
# into the generated class hierarchy.
MIXIN_MAP: dict[str, type] = {
    'BuildingSurfaceDetailed': ExtensibleVertexGeometryMixin,
    'FloorDetailed': ExtensibleVertexGeometryMixin,
    'RoofCeilingDetailed': ExtensibleVertexGeometryMixin,
    'WallDetailed': ExtensibleVertexGeometryMixin,
    'ShadingBuildingDetailed': ExtensibleVertexGeometryMixin,
    'ShadingSiteDetailed': ExtensibleVertexGeometryMixin,
    'ShadingZoneDetailed': ExtensibleVertexGeometryMixin,
    'FenestrationSurfaceDetailed': FixedVertexGeometryMixin,
}
