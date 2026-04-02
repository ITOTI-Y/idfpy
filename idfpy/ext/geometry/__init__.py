"""Geometry extension — surface area, normal, centroid calculations."""

from .mixins import ExtensibleVertexGeometryMixin, FixedVertexGeometryMixin

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
