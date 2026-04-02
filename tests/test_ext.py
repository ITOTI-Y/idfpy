"""Tests for the ext plugin system and geometry calculations."""

from __future__ import annotations

import math

import pytest

from idfpy.ext.geometry.functions import (
    polygon_area_3d,
    polygon_centroid,
    polygon_normal,
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
