"""Geometry mixin classes for EnergyPlus surface models."""

from __future__ import annotations

from .functions import (
    polygon_area_3d,
    polygon_azimuth,
    polygon_bounding_box,
    polygon_centroid,
    polygon_is_convex,
    polygon_normal,
    polygon_perimeter,
    polygon_tilt,
)


class _BaseGeometryMixin:
    """Base mixin providing geometry properties from ``vertices_as_tuples``."""

    @property
    def vertices_as_tuples(self) -> list[tuple[float, float, float]]:
        raise NotImplementedError

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

    @property
    def tilt(self) -> float:
        """Tilt angle in degrees — 0 = up, 90 = vertical wall, 180 = down."""
        return polygon_tilt(self.vertices_as_tuples)

    @property
    def azimuth(self) -> float:
        """Azimuth in degrees, clockwise from north (N=0, E=90, S=180, W=270)."""
        return polygon_azimuth(self.vertices_as_tuples)

    @property
    def perimeter(self) -> float:
        """Polygon perimeter in m."""
        return polygon_perimeter(self.vertices_as_tuples)

    @property
    def bounding_box(
        self,
    ) -> tuple[tuple[float, float, float], tuple[float, float, float]]:
        """Axis-aligned bounding box ``((xmin, ymin, zmin), (xmax, ymax, zmax))``."""
        return polygon_bounding_box(self.vertices_as_tuples)

    @property
    def is_convex(self) -> bool:
        """Whether the planar polygon is convex."""
        return polygon_is_convex(self.vertices_as_tuples)


class ExtensibleVertexGeometryMixin(_BaseGeometryMixin):
    """Geometry mixin for surfaces with an extensible ``vertices`` list."""

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


class FixedVertexGeometryMixin(_BaseGeometryMixin):
    """Geometry mixin for surfaces with fixed ``vertex_N_x/y/z`` fields."""

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
