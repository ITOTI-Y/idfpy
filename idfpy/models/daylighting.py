"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Daylighting
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AttachedShadingSurfNamesRef,
    ConstructionNamesRef,
    DaylightReferencePointNamesRef,
    ScheduleNamesRef,
    SpaceNamesRef,
    SubSurfNamesRef,
    SurfaceNamesRef,
    ZoneNamesRef,
)


class DaylightingControlsControlDataItem(IDFBaseModel):
    """Nested object type for array items."""
    daylighting_reference_point_name: DaylightReferencePointNamesRef = Field(..., json_schema_extra={'object_list': ['DaylightReferencePointNames']})
    fraction_of_lights_controlled_by_reference_point: float | None = Field(default=1.0, ge=0.0, le=1.0)
    illuminance_setpoint_at_reference_point: float | None = Field(default=500.0, ge=0.0, json_schema_extra={'units': 'lux'})


class DaylightingDeviceTubularTransitionLengthsItem(IDFBaseModel):
    """Nested object type for array items."""
    transition_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames']})
    transition_zone_length: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})



class DaylightingControls(IDFBaseModel):
    """Dimming of overhead electric lighting is determined from each reference
point. Glare from daylighting is also calculated."""

    _idf_object_type: ClassVar[str] = "Daylighting:Controls"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    daylighting_method: Literal['', 'DElight', 'SplitFlux'] | None = Field(default='SplitFlux')
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    lighting_control_type: Literal['', 'Continuous', 'ContinuousOff', 'Stepped'] | None = Field(default='Continuous')
    minimum_input_power_fraction_for_continuous_or_continuousoff_dimming_control: float | None = Field(default=0.3, ge=0.0, le=0.6)
    minimum_light_output_fraction_for_continuous_or_continuousoff_dimming_control: float | None = Field(default=0.2, ge=0.0, le=0.6)
    number_of_stepped_control_steps: int | None = Field(default=1, ge=1, json_schema_extra={'note': 'The number of steps, excluding off, in a stepped lighting control system. If Lighting Control Type is Stepped, this field must be greater than zero. The steps are assumed to be equally spaced.'})
    probability_lighting_will_be_reset_when_needed_in_manual_stepped_control: float | None = Field(default=1.0, ge=0.0, le=1.0)
    glare_calculation_daylighting_reference_point_name: DaylightReferencePointNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['DaylightReferencePointNames']})
    glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_y_axis: float | None = Field(default=0.0, ge=0.0, le=360.0, json_schema_extra={'units': 'deg'})
    maximum_allowable_discomfort_glare_index: float | None = Field(default=22.0, ge=1.0, json_schema_extra={'note': 'The default is for general office work'})
    delight_gridding_resolution: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm2', 'note': 'Maximum surface area for nodes in gridding all surfaces in the DElight zone. All reflective and transmitting surfaces will be subdivided into approximately square nodes that do not exceed this maxi...'})
    control_data: list[DaylightingControlsControlDataItem] | None = Field(default=None)


class DaylightingDELightComplexFenestration(IDFBaseModel):
    """Used for DElight Complex Fenestration of all types"""

    _idf_object_type: ClassVar[str] = "Daylighting:DELight:ComplexFenestration"
    name: str = Field(..., json_schema_extra={'note': 'Only used for user reference'})
    complex_fenestration_type: str = Field(..., json_schema_extra={'note': 'Used to select the appropriate Complex Fenestration BTDF data'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'This is a reference to a valid surface object (such as BuildingSurface:Detailed) hosting this complex fenestration, analogous to the base surface Name field for subsurfaces such as Windows.'})
    window_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames'], 'note': 'This is a reference to a valid FenestrationSurface:Detailed window object used to account for the geometry, and the solar and thermal gains/losses, of the Complex Fenestration'})
    fenestration_rotation: float | None = Field(default=0.0, json_schema_extra={'units': 'deg', 'note': 'In-plane counter-clockwise rotation angle of the Complex Fenestration optical reference direction and the base edge of the Complex Fenestration. The Rotation will typically be zero when the host an...'})


class DaylightingDeviceLightWell(IDFBaseModel):
    """Applies only to exterior windows in daylighting-controlled zones or in zones
that share an interior window with a daylighting-controlled zone. Generally
used with skylights."""

    _idf_object_type: ClassVar[str] = "DaylightingDevice:LightWell"
    exterior_window_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    height_of_well: float = Field(..., ge=0.0, json_schema_extra={'units': 'm', 'note': 'Distance from Bottom of Window to Bottom of Well'})
    perimeter_of_bottom_of_well: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    area_of_bottom_of_well: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2'})
    visible_reflectance_of_well_walls: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'})


class DaylightingDeviceShelf(IDFBaseModel):
    """Defines a daylighting which can have an inside shelf, an outside shelf, or
both. The inside shelf is defined as a building surface and the outside
shelf is defined as a shading surface."""

    _idf_object_type: ClassVar[str] = "DaylightingDevice:Shelf"
    name: str = Field(...)
    window_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    inside_shelf_name: SurfaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'This must refer to a BuildingSurface:Detailed or equivalent object This surface must be its own Surface for other side boundary conditions.'})
    outside_shelf_name: AttachedShadingSurfNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['AttachedShadingSurfNames'], 'note': 'This must refer to a Shading:Zone:Detailed object'})
    outside_shelf_construction_name: ConstructionNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'Required if outside shelf is specified'})
    view_factor_to_outside_shelf: float | None = Field(default=None, ge=0.0, le=1.0)


class DaylightingDeviceTubular(IDFBaseModel):
    """Defines a tubular daylighting device (TDD) consisting of three components: a
dome, a pipe, and a diffuser. The dome and diffuser are defined separately
using the FenestrationSurface:Detailed object."""

    _idf_object_type: ClassVar[str] = "DaylightingDevice:Tubular"
    name: str = Field(...)
    dome_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames'], 'note': 'This must refer to a subsurface object of type TubularDaylightDome'})
    diffuser_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames'], 'note': 'This must refer to a subsurface object of type TubularDaylightDiffuser Delivery zone is specified in the diffuser object'})
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})
    diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    total_length: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'The exterior exposed length is the difference between total and sum of zone lengths'})
    effective_thermal_resistance: float | None = Field(default=0.28, gt=0.0, json_schema_extra={'units': 'm2-K/W', 'note': 'R value between TubularDaylightDome and TubularDaylightDiffuser'})
    transition_lengths: list[DaylightingDeviceTubularTransitionLengthsItem] | None = Field(default=None)


class DaylightingReferencePoint(IDFBaseModel):
    """Used by Daylighting:Controls to identify the reference point coordinates for
each sensor. Reference points are given in coordinates specified in the
GlobalGeometryRules object Daylighting Reference Point CoordinateSystem
field."""

    _idf_object_type: ClassVar[str] = "Daylighting:ReferencePoint"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    x_coordinate_of_reference_point: float = Field(..., json_schema_extra={'units': 'm'})
    y_coordinate_of_reference_point: float = Field(..., json_schema_extra={'units': 'm'})
    z_coordinate_of_reference_point: float | None = Field(default=0.8, json_schema_extra={'units': 'm'})


class OutputControlIlluminanceMapStyle(IDFBaseModel):
    """default style for the Daylighting Illuminance Map is comma -- this works
well for importing into spreadsheet programs such as Excel(tm) but not so
well for word processing programs -- there tab may be a better choice. fixed
puts spaces between the \"columns\""""

    _idf_object_type: ClassVar[str] = "OutputControl:IlluminanceMap:Style"
    column_separator: Literal['', 'Comma', 'Fixed', 'Tab'] | None = Field(default='Comma')


class OutputDaylightFactors(IDFBaseModel):
    """Reports hourly daylight factors for each exterior window for four sky types
(clear, turbid clear, intermediate, and overcast)."""

    _idf_object_type: ClassVar[str] = "Output:DaylightFactors"
    reporting_days: Literal['AllShadowCalculationDays', 'SizingDays'] = Field(...)


class OutputIlluminanceMap(IDFBaseModel):
    """reference points are given in coordinates specified in the
GlobalGeometryRules object Daylighting Reference Point CoordinateSystem
field"""

    _idf_object_type: ClassVar[str] = "Output:IlluminanceMap"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    z_height: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    x_minimum_coordinate: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    x_maximum_coordinate: float | None = Field(default=1.0, json_schema_extra={'units': 'm'})
    number_of_x_grid_points: int | None = Field(default=2, ge=1, json_schema_extra={'note': 'Maximum number of total grid points must be <= 2500 (X*Y)'})
    y_minimum_coordinate: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    y_maximum_coordinate: float | None = Field(default=1.0, json_schema_extra={'units': 'm'})
    number_of_y_grid_points: int | None = Field(default=2, ge=1, json_schema_extra={'note': 'Maximum number of total grid points must be <= 2500 (X*Y)'})

