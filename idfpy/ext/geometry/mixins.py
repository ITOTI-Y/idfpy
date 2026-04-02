"""Geometry mixin classes for EnergyPlus surface models."""

from __future__ import annotations

from .functions import polygon_area_3d, polygon_centroid, polygon_normal


class ExtensibleVertexGeometryMixin:
    """Geometry mixin for surfaces with an extensible ``vertices`` list.

    Target classes: BuildingSurfaceDetailed, FloorDetailed,
    RoofCeilingDetailed, WallDetailed, ShadingBuildingDetailed,
    ShadingSiteDetailed, ShadingZoneDetailed.
    """

    @property
    def vertices_as_tuples(self) -> list[tuple[float, float, float]]:
        """Return vertex coordinates as a list of ``(x, y, z)`` tuples."""
        items = getattr(self, 'vertices', None)
        if not items:
            return []
        return [
            (
                item.vertex_x_coordinate,
                item.vertex_y_coordinate,
                item.vertex_z_coordinate,
            )
            for item in items
        ]

    @property
    def area(self) -> float:
        """Surface area in m²."""
        return polygon_area_3d(self.vertices_as_tuples)

    @property
    def normal(self) -> tuple[float, float, float]:
        """Outward unit normal vector."""
        return polygon_normal(self.vertices_as_tuples)

    @property
    def centroid(self) -> tuple[float, float, float]:
        """Centroid (arithmetic mean of vertices)."""
        return polygon_centroid(self.vertices_as_tuples)


class FixedVertexGeometryMixin:
    """Geometry mixin for surfaces with fixed ``vertex_N_x/y/z`` fields.

    Target classes: FenestrationSurfaceDetailed.
    """

    @property
    def vertices_as_tuples(self) -> list[tuple[float, float, float]]:
        """Return vertex coordinates as a list of ``(x, y, z)`` tuples."""
        result: list[tuple[float, float, float]] = []
        for i in range(1, 5):
            x = getattr(self, f'vertex_{i}_x_coordinate', None)
            y = getattr(self, f'vertex_{i}_y_coordinate', None)
            z = getattr(self, f'vertex_{i}_z_coordinate', None)
            if x is None or y is None or z is None:
                break
            result.append((x, y, z))
        return result

    @property
    def area(self) -> float:
        """Surface area in m²."""
        return polygon_area_3d(self.vertices_as_tuples)

    @property
    def normal(self) -> tuple[float, float, float]:
        """Outward unit normal vector."""
        return polygon_normal(self.vertices_as_tuples)

    @property
    def centroid(self) -> tuple[float, float, float]:
        """Centroid (arithmetic mean of vertices)."""
        return polygon_centroid(self.vertices_as_tuples)
