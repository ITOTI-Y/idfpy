"""Tests for the ext plugin system and geometry calculations."""

from __future__ import annotations

import math

import pytest

from idfpy.ext.geometry.functions import (
    polygon_area_3d,
    polygon_azimuth,
    polygon_bounding_box,
    polygon_centroid,
    polygon_is_convex,
    polygon_normal,
    polygon_perimeter,
    polygon_tilt,
)
from idfpy.models.thermal_zones import (
    BuildingSurfaceDetailed,
    BuildingSurfaceDetailedVerticesItem,
    FenestrationSurfaceDetailed,
    FloorDetailed,
)


class TestPolygonArea3D:
    def test_triangle(self):
        verts = [(0.0, 0.0, 0.0), (1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]
        assert polygon_area_3d(verts) == pytest.approx(0.5)

    def test_rectangle(self):
        verts = [
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 0.0),
            (2.0, 0.0, 3.0),
            (0.0, 0.0, 3.0),
        ]
        assert polygon_area_3d(verts) == pytest.approx(6.0)

    def test_tilted_rectangle(self):
        s = math.sqrt(2) / 2
        verts = [(0, 0, 0), (1, 0, 0), (1, s, s), (0, s, s)]
        assert polygon_area_3d(verts) == pytest.approx(1.0)

    def test_degenerate_less_than_3(self):
        assert polygon_area_3d([]) == 0.0
        assert polygon_area_3d([(0, 0, 0)]) == 0.0
        assert polygon_area_3d([(0, 0, 0), (1, 0, 0)]) == 0.0

    def test_collinear_points(self):
        verts = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
        assert polygon_area_3d(verts) == pytest.approx(0.0)

    def test_non_convex_l_shape(self):
        # L-shape (2x2 square with top-right 1x1 removed), true area = 3
        verts = [
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 0.0),
            (2.0, 1.0, 0.0),
            (1.0, 1.0, 0.0),
            (1.0, 2.0, 0.0),
            (0.0, 2.0, 0.0),
        ]
        assert polygon_area_3d(verts) == pytest.approx(3.0)

    def test_non_convex_l_shape_tilted(self):
        # Same L-shape mapped onto the z = x plane, area scaled by sqrt(2)
        verts = [
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 2.0),
            (2.0, 1.0, 2.0),
            (1.0, 1.0, 1.0),
            (1.0, 2.0, 1.0),
            (0.0, 2.0, 0.0),
        ]
        assert polygon_area_3d(verts) == pytest.approx(3.0 * math.sqrt(2))


class TestPolygonNormal:
    def test_xy_plane(self):
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        nx, ny, nz = polygon_normal(verts)
        assert (nx, ny, nz) == pytest.approx((0.0, 0.0, 1.0))

    def test_xz_plane(self):
        verts = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)]
        nx, ny, nz = polygon_normal(verts)
        assert abs(ny) == pytest.approx(1.0)
        assert nx == pytest.approx(0.0)
        assert nz == pytest.approx(0.0)

    def test_unit_length(self):
        verts = [(0, 0, 0), (3, 0, 0), (3, 4, 0)]
        nx, ny, nz = polygon_normal(verts)
        length = math.sqrt(nx**2 + ny**2 + nz**2)
        assert length == pytest.approx(1.0)

    def test_degenerate(self):
        assert polygon_normal([]) == (0.0, 0.0, 0.0)
        assert polygon_normal([(0, 0, 0), (1, 0, 0)]) == (0.0, 0.0, 0.0)


class TestPolygonCentroid:
    def test_triangle(self):
        verts = [(0, 0, 0), (3, 0, 0), (0, 3, 0)]
        assert polygon_centroid(verts) == pytest.approx((1.0, 1.0, 0.0))

    def test_square(self):
        verts = [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)]
        assert polygon_centroid(verts) == pytest.approx((1.0, 1.0, 0.0))

    def test_empty(self):
        assert polygon_centroid([]) == (0.0, 0.0, 0.0)


class TestPolygonTilt:
    def test_horizontal_facing_up(self):
        # CCW polygon in XY plane viewed from +Z, normal = +Z, tilt = 0
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        assert polygon_tilt(verts) == pytest.approx(0.0)

    def test_horizontal_facing_down(self):
        # CW polygon in XY plane, normal = -Z, tilt = 180
        verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
        assert polygon_tilt(verts) == pytest.approx(180.0)

    def test_vertical_wall(self):
        # Wall in XZ plane, horizontal normal, tilt = 90
        verts = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)]
        assert polygon_tilt(verts) == pytest.approx(90.0)

    def test_45_deg_slope(self):
        # Wall tilted 45 degrees toward +Y
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 1), (0, 1, 1)]
        assert polygon_tilt(verts) == pytest.approx(45.0)

    def test_degenerate(self):
        assert polygon_tilt([]) == 0.0
        assert polygon_tilt([(0, 0, 0), (1, 0, 0)]) == 0.0


class TestPolygonAzimuth:
    def test_wall_facing_north(self):
        # Outward normal +Y, azimuth = 0
        verts = [(0, 0, 0), (0, 0, 1), (1, 0, 1), (1, 0, 0)]
        assert polygon_azimuth(verts) == pytest.approx(0.0)

    def test_wall_facing_south(self):
        # Outward normal -Y, azimuth = 180
        verts = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)]
        assert polygon_azimuth(verts) == pytest.approx(180.0)

    def test_wall_facing_east(self):
        # Outward normal +X, azimuth = 90
        verts = [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)]
        assert polygon_azimuth(verts) == pytest.approx(90.0)

    def test_wall_facing_west(self):
        # Outward normal -X, azimuth = 270
        verts = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (0, 1, 0)]
        assert polygon_azimuth(verts) == pytest.approx(270.0)

    def test_horizontal_surface(self):
        # Azimuth undefined for horizontal surfaces, returns 0
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        assert polygon_azimuth(verts) == pytest.approx(0.0)

    def test_southeast_wall(self):
        # Base line along (0,0)->(1,1), outward normal (1,-1,0)/sqrt(2), azimuth = 135
        verts = [(0, 0, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1)]
        assert polygon_azimuth(verts) == pytest.approx(135.0)

    def test_degenerate(self):
        assert polygon_azimuth([]) == 0.0


class TestPolygonPerimeter:
    def test_unit_square(self):
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        assert polygon_perimeter(verts) == pytest.approx(4.0)

    def test_3_4_5_triangle(self):
        verts = [(0, 0, 0), (3, 0, 0), (0, 4, 0)]
        assert polygon_perimeter(verts) == pytest.approx(12.0)

    def test_3d_tilted_rectangle(self):
        # 1x1 square tilted into 3D, all four edges have length 1
        s = math.sqrt(2) / 2
        verts = [(0, 0, 0), (1, 0, 0), (1, s, s), (0, s, s)]
        assert polygon_perimeter(verts) == pytest.approx(4.0)

    def test_3d_rectangle_with_diagonal_edges(self):
        # 2x1 rectangle with base in XY plane, perimeter = 2*(2 + 1) = 6
        verts = [(0, 0, 0), (2, 0, 0), (2, 0, 1), (0, 0, 1)]
        assert polygon_perimeter(verts) == pytest.approx(6.0)

    def test_degenerate_less_than_3(self):
        assert polygon_perimeter([]) == 0.0
        assert polygon_perimeter([(0, 0, 0)]) == 0.0
        assert polygon_perimeter([(0, 0, 0), (1, 0, 0)]) == 0.0


class TestPolygonBoundingBox:
    def test_unit_square_xy(self):
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        lo, hi = polygon_bounding_box(verts)
        assert lo == pytest.approx((0.0, 0.0, 0.0))
        assert hi == pytest.approx((1.0, 1.0, 0.0))

    def test_negative_coordinates(self):
        verts = [(-1, -2, -3), (4, 5, 6), (0, 0, 0)]
        lo, hi = polygon_bounding_box(verts)
        assert lo == pytest.approx((-1.0, -2.0, -3.0))
        assert hi == pytest.approx((4.0, 5.0, 6.0))

    def test_full_3d(self):
        verts = [(0, 0, 0), (2, 0, 0), (2, 3, 1), (0, 3, 1)]
        lo, hi = polygon_bounding_box(verts)
        assert lo == pytest.approx((0.0, 0.0, 0.0))
        assert hi == pytest.approx((2.0, 3.0, 1.0))

    def test_empty(self):
        assert polygon_bounding_box([]) == (
            (0.0, 0.0, 0.0),
            (0.0, 0.0, 0.0),
        )

    def test_single_point(self):
        lo, hi = polygon_bounding_box([(5.0, 6.0, 7.0)])
        assert lo == pytest.approx((5.0, 6.0, 7.0))
        assert hi == pytest.approx((5.0, 6.0, 7.0))


class TestPolygonIsConvex:
    def test_triangle(self):
        verts = [(0, 0, 0), (1, 0, 0), (0, 1, 0)]
        assert polygon_is_convex(verts) is True

    def test_square(self):
        verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        assert polygon_is_convex(verts) is True

    def test_tilted_rectangle_3d(self):
        s = math.sqrt(2) / 2
        verts = [(0, 0, 0), (1, 0, 0), (1, s, s), (0, s, s)]
        assert polygon_is_convex(verts) is True

    def test_l_shape_non_convex(self):
        verts = [
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 0.0),
            (2.0, 1.0, 0.0),
            (1.0, 1.0, 0.0),
            (1.0, 2.0, 0.0),
            (0.0, 2.0, 0.0),
        ]
        assert polygon_is_convex(verts) is False

    def test_l_shape_tilted_non_convex(self):
        verts = [
            (0.0, 0.0, 0.0),
            (2.0, 0.0, 2.0),
            (2.0, 1.0, 2.0),
            (1.0, 1.0, 1.0),
            (1.0, 2.0, 1.0),
            (0.0, 2.0, 0.0),
        ]
        assert polygon_is_convex(verts) is False

    def test_degenerate_less_than_3(self):
        assert polygon_is_convex([]) is False
        assert polygon_is_convex([(0, 0, 0), (1, 0, 0)]) is False

    def test_collinear_points(self):
        # Collinear vertices yield a zero normal, which returns False
        verts = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
        assert polygon_is_convex(verts) is False


def _make_vertex_item(x: float, y: float, z: float):
    return BuildingSurfaceDetailedVerticesItem(
        vertex_x_coordinate=x,
        vertex_y_coordinate=y,
        vertex_z_coordinate=z,
    )


class TestExtensibleVertexGeometryMixin:
    def test_area(self):
        surface = BuildingSurfaceDetailed(
            name='Wall1',
            surface_type='Wall',
            construction_name='ExtWall',
            zone_name='Zone1',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
            vertices=[
                _make_vertex_item(0, 0, 3),
                _make_vertex_item(0, 0, 0),
                _make_vertex_item(10, 0, 0),
                _make_vertex_item(10, 0, 3),
            ],
        )
        assert surface.area == pytest.approx(30.0)

    def test_normal(self):
        surface = BuildingSurfaceDetailed(
            name='Floor1',
            surface_type='Floor',
            construction_name='FloorConst',
            zone_name='Zone1',
            outside_boundary_condition='Ground',
            sun_exposure='NoSun',
            wind_exposure='NoWind',
            vertices=[
                _make_vertex_item(0, 0, 0),
                _make_vertex_item(1, 0, 0),
                _make_vertex_item(1, 1, 0),
                _make_vertex_item(0, 1, 0),
            ],
        )
        assert surface.normal == pytest.approx((0.0, 0.0, 1.0))

    def test_centroid(self):
        surface = BuildingSurfaceDetailed(
            name='W',
            surface_type='Wall',
            construction_name='C',
            zone_name='Z',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
            vertices=[
                _make_vertex_item(0, 0, 0),
                _make_vertex_item(4, 0, 0),
                _make_vertex_item(4, 0, 2),
                _make_vertex_item(0, 0, 2),
            ],
        )
        assert surface.centroid == pytest.approx((2.0, 0.0, 1.0))

    def test_vertices_as_tuples(self):
        surface = BuildingSurfaceDetailed(
            name='W',
            surface_type='Wall',
            construction_name='C',
            zone_name='Z',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
            vertices=[
                _make_vertex_item(1, 2, 3),
                _make_vertex_item(4, 5, 6),
                _make_vertex_item(7, 8, 9),
            ],
        )
        assert surface.vertices_as_tuples == [
            (1.0, 2.0, 3.0),
            (4.0, 5.0, 6.0),
            (7.0, 8.0, 9.0),
        ]

    def test_no_vertices(self):
        surface = BuildingSurfaceDetailed(
            name='W',
            surface_type='Wall',
            construction_name='C',
            zone_name='Z',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
        )
        assert surface.vertices_as_tuples == []
        assert surface.area == 0.0

    def test_floor_detailed(self):
        surface = FloorDetailed(
            name='Floor',
            construction_name='FloorConst',
            zone_name='Zone1',
            outside_boundary_condition='Ground',
            sun_exposure='NoSun',
            wind_exposure='NoWind',
            vertices=[
                BuildingSurfaceDetailedVerticesItem(
                    vertex_x_coordinate=0,
                    vertex_y_coordinate=0,
                    vertex_z_coordinate=0,
                ),
                BuildingSurfaceDetailedVerticesItem(
                    vertex_x_coordinate=5,
                    vertex_y_coordinate=0,
                    vertex_z_coordinate=0,
                ),
                BuildingSurfaceDetailedVerticesItem(
                    vertex_x_coordinate=5,
                    vertex_y_coordinate=5,
                    vertex_z_coordinate=0,
                ),
                BuildingSurfaceDetailedVerticesItem(
                    vertex_x_coordinate=0,
                    vertex_y_coordinate=5,
                    vertex_z_coordinate=0,
                ),
            ],
        )
        assert surface.area == pytest.approx(25.0)

    def test_all_new_properties(self):
        # 10m wide, 3m tall south-facing wall (outward normal -Y)
        surface = BuildingSurfaceDetailed(
            name='SouthWall',
            surface_type='Wall',
            construction_name='ExtWall',
            zone_name='Zone1',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
            vertices=[
                _make_vertex_item(0, 0, 0),
                _make_vertex_item(10, 0, 0),
                _make_vertex_item(10, 0, 3),
                _make_vertex_item(0, 0, 3),
            ],
        )
        assert surface.tilt == pytest.approx(90.0)
        assert surface.azimuth == pytest.approx(180.0)
        assert surface.perimeter == pytest.approx(26.0)
        lo, hi = surface.bounding_box
        assert lo == pytest.approx((0.0, 0.0, 0.0))
        assert hi == pytest.approx((10.0, 0.0, 3.0))
        assert surface.is_convex is True


class TestFixedVertexGeometryMixin:
    def test_area_quad(self):
        window = FenestrationSurfaceDetailed(
            name='Win1',
            surface_type='Window',
            construction_name='Glass',
            building_surface_name='Wall1',
            vertex_1_x_coordinate=0,
            vertex_1_y_coordinate=0,
            vertex_1_z_coordinate=2,
            vertex_2_x_coordinate=0,
            vertex_2_y_coordinate=0,
            vertex_2_z_coordinate=0,
            vertex_3_x_coordinate=3,
            vertex_3_y_coordinate=0,
            vertex_3_z_coordinate=0,
            vertex_4_x_coordinate=3,
            vertex_4_y_coordinate=0,
            vertex_4_z_coordinate=2,
        )
        assert window.area == pytest.approx(6.0)

    def test_area_triangle(self):
        window = FenestrationSurfaceDetailed(
            name='Tri1',
            surface_type='Window',
            construction_name='Glass',
            building_surface_name='Wall1',
            vertex_1_x_coordinate=0,
            vertex_1_y_coordinate=0,
            vertex_1_z_coordinate=0,
            vertex_2_x_coordinate=2,
            vertex_2_y_coordinate=0,
            vertex_2_z_coordinate=0,
            vertex_3_x_coordinate=0,
            vertex_3_y_coordinate=0,
            vertex_3_z_coordinate=2,
        )
        assert window.area == pytest.approx(2.0)

    def test_vertices_as_tuples(self):
        window = FenestrationSurfaceDetailed(
            name='W',
            surface_type='Window',
            construction_name='G',
            building_surface_name='S',
            vertex_1_x_coordinate=1,
            vertex_1_y_coordinate=2,
            vertex_1_z_coordinate=3,
            vertex_2_x_coordinate=4,
            vertex_2_y_coordinate=5,
            vertex_2_z_coordinate=6,
            vertex_3_x_coordinate=7,
            vertex_3_y_coordinate=8,
            vertex_3_z_coordinate=9,
        )
        assert window.vertices_as_tuples == [
            (1.0, 2.0, 3.0),
            (4.0, 5.0, 6.0),
            (7.0, 8.0, 9.0),
        ]

    def test_all_new_properties(self):
        # 3m wide, 2m tall south-facing window (outward normal -Y)
        window = FenestrationSurfaceDetailed(
            name='SouthWin',
            surface_type='Window',
            construction_name='Glass',
            building_surface_name='Wall1',
            vertex_1_x_coordinate=0,
            vertex_1_y_coordinate=0,
            vertex_1_z_coordinate=2,
            vertex_2_x_coordinate=0,
            vertex_2_y_coordinate=0,
            vertex_2_z_coordinate=0,
            vertex_3_x_coordinate=3,
            vertex_3_y_coordinate=0,
            vertex_3_z_coordinate=0,
            vertex_4_x_coordinate=3,
            vertex_4_y_coordinate=0,
            vertex_4_z_coordinate=2,
        )
        assert window.tilt == pytest.approx(90.0)
        assert window.azimuth == pytest.approx(180.0)
        assert window.perimeter == pytest.approx(10.0)
        lo, hi = window.bounding_box
        assert lo == pytest.approx((0.0, 0.0, 0.0))
        assert hi == pytest.approx((3.0, 0.0, 2.0))
        assert window.is_convex is True


class TestPluginIntegration:
    def test_mro_contains_mixin(self):
        from idfpy.ext.geometry.mixins import ExtensibleVertexGeometryMixin

        assert ExtensibleVertexGeometryMixin in BuildingSurfaceDetailed.__mro__

    def test_mro_contains_base(self):
        from idfpy.models._base import IDFBaseModel

        assert IDFBaseModel in BuildingSurfaceDetailed.__mro__

    def test_model_fields_preserved(self):
        assert 'name' in BuildingSurfaceDetailed.model_fields
        assert 'vertices' in BuildingSurfaceDetailed.model_fields

    def test_model_dump_works(self):
        surface = BuildingSurfaceDetailed(
            name='W',
            surface_type='Wall',
            construction_name='C',
            zone_name='Z',
            outside_boundary_condition='Outdoors',
            sun_exposure='SunExposed',
            wind_exposure='WindExposed',
        )
        data = surface.model_dump(exclude_none=True)
        assert data['name'] == 'W'
        assert 'area' not in data

    def test_new_properties_available_on_generated_models(self):
        # New mixin @property entries reach generated models without rerunning codegen
        for prop in ('tilt', 'azimuth', 'perimeter', 'bounding_box', 'is_convex'):
            assert hasattr(BuildingSurfaceDetailed, prop), (
                f'BuildingSurfaceDetailed missing {prop}'
            )
            assert hasattr(FenestrationSurfaceDetailed, prop), (
                f'FenestrationSurfaceDetailed missing {prop}'
            )
