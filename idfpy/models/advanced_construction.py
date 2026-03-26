"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Advanced Construction, Surface, Zone Concepts
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllHeatTranSurfNamesRef,
    AllShadingAndHTSurfNamesRef,
    ComplexFenestrationStatesRef,
    ConstructionNamesRef,
    FloorSurfaceNamesRef,
    GroundSurfacesNamesRef,
    MaterialNameRef,
    OSCMNamesRef,
    OutdoorAirNodeNamesRef,
    ScheduleNamesRef,
    SpaceListNamesRef,
    SpaceNamesRef,
    SubSurfNamesRef,
    SurfaceNamesRef,
    SurroundingSurfacesNamesRef,
    UnivariateFunctionsRef,
    UserConvectionInsideModelsRef,
    UserConvectionModelsRef,
    UserConvectionOutsideModelsRef,
    ZoneListNamesRef,
    ZoneNamesRef,
)


class FoundationKivaBlocksItem(IDFBaseModel):
    """Nested object type for array items."""

    custom_block_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    custom_block_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Top-to-bottom dimension of the block downward.',
        },
    )
    custom_block_x_position: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm',
            'note': 'Position outward (+) or inward (-) relative to the foundation wall interior',
        },
    )
    custom_block_z_position: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm',
            'note': 'Position downward (+) relative to the foundation wall top',
        },
    )


class SurfacePropertyExposedFoundationPerimeterSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_segment_exposed: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Surface Segment N is the perimeter between the Nth and (N+1)th vertices'
        },
    )


class SurfacePropertyExteriorNaturalVentedCAVitySurfaceItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )


class SurfacePropertyGroundSurfacesGroundSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    ground_surface_name: str = Field(...)
    ground_surface_view_factor: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    ground_surface_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are real numbers, -100.0 to 100.0, units C',
        },
    )
    ground_surface_reflectance_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are fraction, 0.0 to 1.0, units dimensionless',
        },
    )


class SurfacePropertyHeatTransferAlgorithmSurfaceListSurfaceItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )


class SurfacePropertySurroundingSurfacesSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    surrounding_surface_name: str = Field(...)
    surrounding_surface_view_factor: float | None = Field(default=0.0, ge=0.0, le=1.0)
    surrounding_surface_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are real numbers, -100.0 to 100.0, units C',
        },
    )


class ZonePropertyUserViewFactorsBySurfaceNameViewFactorsItem(IDFBaseModel):
    """Nested object type for array items."""

    from_surface: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    to_surface: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    view_factor: float | None = Field(
        default=None,
        le=1.0,
        json_schema_extra={
            'note': 'This value is the view factor value From Surface => To Surface'
        },
    )


class ComplexFenestrationPropertySolarAbsorbedLayers(IDFBaseModel):
    """Used to provide solar radiation absorbed in fenestration layers. References
    surface-construction pair and if that pair is used in a simulation, then
    program will use value provided in schedules instead of calculating it."""

    _idf_object_type: ClassVar[str] = 'ComplexFenestrationProperty:SolarAbsorbedLayers'
    name: str = Field(...)
    fenestration_surface: SubSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SubSurfNames']}
    )
    construction_name: ComplexFenestrationStatesRef = Field(
        ..., json_schema_extra={'object_list': ['ComplexFenestrationStates']}
    )
    layer_1_solar_radiation_absorbed_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )
    layer_2_solar_radiation_absorbed_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )
    layer_3_solar_radiation_absorbed_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )
    layer_4_solar_radiation_absorbed_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )
    layer_5_solar_radiation_absorbed_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )


class FoundationKiva(IDFBaseModel):
    """Refined definition of the foundation surface construction used to inform
    two-dimensional heat transfer calculated using the Kiva ground heat transfer
    methodology."""

    _idf_object_type: ClassVar[str] = 'Foundation:Kiva'
    name: str = Field(...)
    initial_indoor_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Indoor air temperature used for Kiva initialization (prior to warmup period) If left blank, indoor air temperature will be determined based on zone setpoints',
        },
    )
    interior_horizontal_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    interior_horizontal_insulation_depth: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the slab bottom to the top of interior horizontal insulation',
        },
    )
    interior_horizontal_insulation_width: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Extent of insulation as measured from the wall interior',
        },
    )
    interior_vertical_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    interior_vertical_insulation_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Extent of insulation as measured from the wall top to the bottom edge of the interior vertical insulation',
        },
    )
    exterior_horizontal_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    exterior_horizontal_insulation_depth: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the exterior grade to the top of exterior horizontal insulation',
        },
    )
    exterior_horizontal_insulation_width: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Extent of insulation as measured from the wall exterior',
        },
    )
    exterior_vertical_insulation_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    exterior_vertical_insulation_depth: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Extent of insulation as measured from the wall top to the bottom edge of the exterior vertical insulation',
        },
    )
    wall_height_above_grade: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the exterior grade to the wall top',
        },
    )
    wall_depth_below_slab: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the slab bottom to the bottom of the foundation wall',
        },
    )
    footing_wall_construction_name: ConstructionNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ConstructionNames'],
            'note': 'Defines the below-grade surface construction for slabs. Required if foundation wall is not exposed to the zone.',
        },
    )
    footing_material_name: MaterialNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['MaterialName']}
    )
    footing_depth: float | None = Field(
        default=0.3,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': "Top-to-bottom dimension of the footing (not to be confused with its depth in the ground). The width of the footing is defined by the material's thickness.",
        },
    )
    blocks: list[FoundationKivaBlocksItem] | None = Field(default=None)


class FoundationKivaSettings(IDFBaseModel):
    """Settings applied across all Kiva foundation calculations. Object is not
    required. If not defined, defaults will be applied."""

    _idf_object_type: ClassVar[str] = 'Foundation:Kiva:Settings'
    soil_conductivity: float | None = Field(
        default=1.73, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    soil_density: float | None = Field(
        default=1842.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    soil_specific_heat: float | None = Field(
        default=419.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    ground_solar_absorptivity: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    ground_thermal_absorptivity: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    ground_surface_roughness: float | None = Field(
        default=0.03, gt=0.0, json_schema_extra={'units': 'm'}
    )
    far_field_width: float | None = Field(
        default=40.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    deep_ground_boundary_condition: (
        Literal['', 'Autoselect', 'GroundWater', 'ZeroFlux'] | None
    ) = Field(default='Autoselect')
    deep_ground_depth: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate', json_schema_extra={'units': 'm'}
    )
    minimum_cell_dimension: float | None = Field(
        default=0.02, gt=0.0, json_schema_extra={'units': 'm'}
    )
    maximum_cell_growth_coefficient: float | None = Field(
        default=1.5, ge=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    simulation_timestep: Literal['', 'Hourly', 'Timestep'] | None = Field(
        default='Hourly'
    )


class SurfaceControlMovableInsulation(IDFBaseModel):
    """Exterior or Interior Insulation on opaque surfaces"""

    _idf_object_type: ClassVar[str] = 'SurfaceControl:MovableInsulation'
    insulation_type: Literal['Inside', 'Outside'] = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    material_name: MaterialNameRef = Field(
        ..., json_schema_extra={'object_list': ['MaterialName']}
    )
    schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )


class SurfaceConvectionAlgorithmInsideAdaptiveModelSelections(IDFBaseModel):
    """Options to change the individual convection model equations for dynamic
    selection when using AdaptiveConvectiongAlgorithm This object is only needed
    to make changes to the default model selections for any or all of the
    surface categories. This object is for the inside face, the side of the
    surface facing a thermal zone."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections'
    )
    name: str | None = Field(default=None)
    simple_buoyancy_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq3WallAwayFromHeat',
            'KhalifaEq6NonHeatedWalls',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='FohannoPolidoriVerticalWall',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for vertical walls'
        },
    )
    simple_buoyancy_vertical_wall_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    simple_buoyancy_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondStableHorizontal',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for horizontal surfaces with heat flow directed for stable thermal stratification'
        },
    )
    simple_buoyancy_stable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    simple_buoyancy_unstable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondUnstableHorizontal',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for passive horizontal surfaces with heat flow for unstable thermal stratification'
        },
    )
    simple_buoyancy_unstable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    simple_buoyancy_stable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for tilted surfaces with heat flow for stable thermal stratification'
        },
    )
    simple_buoyancy_stable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    simple_buoyancy_unstable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonUnstableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for tilted surfaces with heat flow for unstable thermal stratification'
        },
    )
    simple_buoyancy_unstable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    simple_buoyancy_windows_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KaradagChilledCeiling',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ISO15099Windows',
        json_schema_extra={
            'note': 'Applies to zone with no HVAC or when HVAC is off This is for all window surfaces'
        },
    )
    simple_buoyancy_windows_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq3WallAwayFromHeat',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='KhalifaEq3WallAwayFromHeat',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for vertical walls'
        },
    )
    floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondStableHorizontal',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for passive horizontal surfaces with heat flow for stable thermal stratification'
        },
    )
    floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_unstable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'KhalifaEq4CeilingAwayFromHeat',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='KhalifaEq4CeilingAwayFromHeat',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for passive horizontal surfaces with heat flow for unstable thermal stratification'
        },
    )
    floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_heated_floor_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'AwbiHattonHeatedFloor',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AwbiHattonHeatedFloor',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for a floor with active heating elements'
        },
    )
    floor_heat_ceiling_cool_heated_floor_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_chilled_ceiling_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'KaradagChilledCeiling',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='KaradagChilledCeiling',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for a ceiling with active cooling elements'
        },
    )
    floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_stable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'ISO15099Windows',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for tilted surfaces with heat flow for stable thermal stratification'
        },
    )
    floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_unstable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'ISO15099Windows',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonUnstableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for tilted surfaces with heat flow for unstable thermal stratification'
        },
    )
    floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    floor_heat_ceiling_cool_window_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ISO15099Windows',
        json_schema_extra={
            'note': 'Applies to zone with in-floor heating and/or in-ceiling cooling This is for all window surfaces'
        },
    )
    floor_heat_ceiling_cool_window_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq6NonHeatedWalls',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='KhalifaEq6NonHeatedWalls',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for vertical walls that are not actively heated'
        },
    )
    wall_panel_heating_vertical_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_heated_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'AwbiHattonHeatedWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq5WallNearHeat',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='AwbiHattonHeatedWall',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for vertical walls that are being actively heated'
        },
    )
    wall_panel_heating_heated_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondStableHorizontal',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for horizontal surfaces with heat flow directed for stable thermal stratification'
        },
    )
    wall_panel_heating_stable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_unstable_horizontal_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondUnstableHorizontal',
            'KaradagChilledCeiling',
            'KhalifaEq7Ceiling',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='KhalifaEq7Ceiling',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for horizontal surfaces with heat flow directed for unstable thermal stratification'
        },
    )
    wall_panel_heating_unstable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_stable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'ISO15099Windows',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for tilted surfaces with heat flow for stable thermal stratification'
        },
    )
    wall_panel_heating_stable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_unstable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'ISO15099Windows',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonUnstableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for tilted surfaces with heat flow for unstable thermal stratification'
        },
    )
    wall_panel_heating_unstable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wall_panel_heating_window_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ISO15099Windows',
        json_schema_extra={
            'note': 'Applies to zone with in-wall panel heating This is for all window surfaces'
        },
    )
    wall_panel_heating_window_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq3WallAwayFromHeat',
            'KhalifaEq6NonHeatedWalls',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='FohannoPolidoriVerticalWall',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for vertical walls not directly affected by heater'
        },
    )
    convective_zone_heater_vertical_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_vertical_walls_near_heater_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'AwbiHattonHeatedWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq5WallNearHeat',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='KhalifaEq5WallNearHeat',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for vertical walls that are directly affected by heater Walls are considered "near" when listed in field set for Fraction of Radiant Energy to Surface'
        },
    )
    convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondStableHorizontal',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for horizontal surfaces with heat flow directed for stable thermal stratification'
        },
    )
    convective_zone_heater_stable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_unstable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'KhalifaEq4CeilingAwayFromHeat',
            'KhalifaEq7Ceiling',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='KhalifaEq7Ceiling',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for horizontal surfaces with heat flow directed for unstable thermal stratification'
        },
    )
    convective_zone_heater_unstable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_stable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for tilted surfaces with heat flow for stable thermal stratification'
        },
    )
    convective_zone_heater_stable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_unstable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonUnstableHorizontalOrTilt',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for tilted surfaces with heat flow for unstable thermal stratification'
        },
    )
    convective_zone_heater_unstable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    convective_zone_heater_windows_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'KhalifaEq3WallAwayFromHeat',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ISO15099Windows',
        json_schema_extra={
            'note': 'Applies to zone with convective heater This is for all window surfaces'
        },
    )
    convective_zone_heater_windows_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    central_air_diffuser_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='GoldsteinNovoselacCeilingDiffuserWalls',
        json_schema_extra={
            'note': 'Applies to zone with mechanical forced central air with diffusers This is for all wall surfaces'
        },
    )
    central_air_diffuser_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    central_air_diffuser_ceiling_equation_source: (
        Literal[
            '',
            'BeausoleilMorrisonMixedStableCeiling',
            'BeausoleilMorrisonMixedUnstableCeiling',
            'FisherPedersenCeilingDiffuserCeiling',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='FisherPedersenCeilingDiffuserCeiling',
        json_schema_extra={
            'note': 'Applies to zone with mechanical forced central air with diffusers This is for all ceiling surfaces'
        },
    )
    central_air_diffuser_ceiling_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    central_air_diffuser_floor_equation_source: (
        Literal[
            '',
            'BeausoleilMorrisonMixedStableFloor',
            'BeausoleilMorrisonMixedUnstableFloor',
            'FisherPedersenCeilingDiffuserFloor',
            'GoldsteinNovoselacCeilingDiffuserFloor',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='GoldsteinNovoselacCeilingDiffuserFloor',
        json_schema_extra={
            'note': 'Applies to zone with mechanical forced central air with diffusers This is for all floor surfaces'
        },
    )
    central_air_diffuser_floor_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    central_air_diffuser_window_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWindow',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='GoldsteinNovoselacCeilingDiffuserWindow',
        json_schema_extra={
            'note': 'Applies to zone with mechanical forced central air with diffusers This is for all window surfaces'
        },
    )
    central_air_diffuser_window_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'ISO15099Windows',
            'KhalifaEq3WallAwayFromHeat',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='KhalifaEq3WallAwayFromHeat',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='AlamdariHammondStableHorizontal',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_unstable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'KhalifaEq4CeilingAwayFromHeat',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='KhalifaEq4CeilingAwayFromHeat',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_stable_tilted_equation_source: (
        Literal['', 'UserCurve', 'WaltonStableHorizontalOrTilt'] | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_unstable_tilted_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonUnstableHorizontalOrTilt',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mechanical_zone_fan_circulation_window_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWindow',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ISO15099Windows', json_schema_extra={'note': 'reference choice fields'}
    )
    mechanical_zone_fan_circulation_window_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_buoyancy_assisting_flow_on_walls_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedAssistedWall',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_buoyancy_opposing_flow_on_walls_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedOpposingWall',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_stable_floor_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'BeausoleilMorrisonMixedStableFloor',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedStableFloor',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_stable_floor_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_unstable_floor_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'BeausoleilMorrisonMixedUnstableFloor',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedUnstableFloor',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_unstable_floor_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_stable_ceiling_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'BeausoleilMorrisonMixedStableCeiling',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedStableCeiling',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_stable_ceiling_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_unstable_ceiling_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'BeausoleilMorrisonMixedUnstableCeiling',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='BeausoleilMorrisonMixedUnstableCeiling',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_unstable_ceiling_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    mixed_regime_window_equation_source: (
        Literal[
            '',
            'GoldsteinNovoselacCeilingDiffuserWindow',
            'ISO15099Windows',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='GoldsteinNovoselacCeilingDiffuserWindow',
        json_schema_extra={'note': 'reference choice fields'},
    )
    mixed_regime_window_equation_user_curve_name: (
        UserConvectionInsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionInsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Inside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )


class SurfaceConvectionAlgorithmInsideUserCurve(IDFBaseModel):
    """Used to describe a custom model equation for surface convection heat
    transfer coefficient If more than one curve is referenced they are all used
    and added together."""

    _idf_object_type: ClassVar[str] = 'SurfaceConvectionAlgorithm:Inside:UserCurve'
    name: str | None = Field(default=None)
    reference_temperature_for_convection_heat_transfer: (
        Literal['AdjacentAirTemperature', 'MeanAirTemperature', 'SupplyAirTemperature']
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Controls which temperature is differenced from surface temperature when using the Hc value'
        },
    )
    hc_function_of_temperature_difference_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'Curve\'s "x" is absolute value of delta-T (Surface temperature minus reference temperature, (C))',
            },
        )
    )
    hc_function_of_temperature_difference_divided_by_height_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve\'s "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m) when used for an inside face the vertical length scale is the zone\'s interior height',
        },
    )
    hc_function_of_air_change_rate_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve\'s "x" is mechanical ACH (Air Changes per hour from mechanical air system), (1/hr)',
        },
    )
    hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve\'s "x" is mechanical system air flow rate (m3/s) divided by zone\'s length along exterior walls (m).',
        },
    )


class SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections(IDFBaseModel):
    """Options to change the individual convection model equations for dynamic
    selection when using AdaptiveConvectiongAlgorithm This object is only needed
    to make changes to the default model selections for any or all of the
    surface categories. This object is for the outside face, the side of the
    surface facing away from the thermal zone."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections'
    )
    name: str | None = Field(default=None)
    wind_convection_windward_vertical_wall_equation_source: (
        Literal[
            '',
            'BlockenWindward',
            'DOE2Windward',
            'EmmelVertical',
            'McAdams',
            'Mitchell',
            'MoWiTTWindward',
            'NusseltJurges',
            'SimpleCombined',
            'TARPWindward',
            'UserCurve',
        ]
        | None
    ) = Field(default='TARPWindward')
    wind_convection_windward_equation_vertical_wall_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wind_convection_leeward_vertical_wall_equation_source: (
        Literal[
            '',
            'DOE2Leeward',
            'EmmelVertical',
            'McAdams',
            'Mitchell',
            'MoWiTTLeeward',
            'NusseltJurges',
            'SimpleCombined',
            'TARPLeeward',
            'UserCurve',
        ]
        | None
    ) = Field(default='TARPLeeward')
    wind_convection_leeward_vertical_wall_equation_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    wind_convection_horizontal_roof_equation_source: (
        Literal[
            '',
            'BlockenWindward',
            'ClearRoof',
            'DOE2Windward',
            'EmmelRoof',
            'McAdams',
            'Mitchell',
            'MoWiTTWindward',
            'NusseltJurges',
            'SimpleCombined',
            'TARPWindward',
            'UserCurve',
        ]
        | None
    ) = Field(default='ClearRoof')
    wind_convection_horizontal_roof_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    natural_convection_vertical_wall_equation_source: (
        Literal[
            '',
            'ASHRAEVerticalWall',
            'AlamdariHammondVerticalWall',
            'FohannoPolidoriVerticalWall',
            'ISO15099Windows',
            'None',
            'UserCurve',
        ]
        | None
    ) = Field(
        default='ASHRAEVerticalWall',
        json_schema_extra={'note': 'This is for vertical walls'},
    )
    natural_convection_vertical_wall_equation_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    natural_convection_stable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondStableHorizontal',
            'None',
            'UserCurve',
            'WaltonStableHorizontalOrTilt',
        ]
        | None
    ) = Field(
        default='WaltonStableHorizontalOrTilt',
        json_schema_extra={
            'note': 'This is for horizontal surfaces with heat flow directed for stable thermal stratification'
        },
    )
    natural_convection_stable_horizontal_equation_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )
    natural_convection_unstable_horizontal_equation_source: (
        Literal[
            '',
            'AlamdariHammondUnstableHorizontal',
            'None',
            'UserCurve',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(default='WaltonUnstableHorizontalOrTilt')
    natural_convection_unstable_horizontal_equation_user_curve_name: (
        UserConvectionOutsideModelsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionOutsideModels'],
            'note': 'The SurfaceConvectionAlgorithm:Outside:UserCurve named in this field is used when the previous field is set to UserCurve',
        },
    )


class SurfaceConvectionAlgorithmOutsideUserCurve(IDFBaseModel):
    """Used to describe a custom model equation for surface convection heat
    transfer coefficient If more than one curve is referenced they are all used
    and added together."""

    _idf_object_type: ClassVar[str] = 'SurfaceConvectionAlgorithm:Outside:UserCurve'
    name: str | None = Field(default=None)
    wind_speed_type_for_curve: (
        Literal[
            '',
            'HeightAdjust',
            'ParallelComponent',
            'ParallelComponentHeightAdjust',
            'WeatherFile',
        ]
        | None
    ) = Field(default='HeightAdjust')
    hf_function_of_wind_speed_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve\'s "x" is wind speed of the type determined in the previous field (m/s)',
        },
    )
    hn_function_of_temperature_difference_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'Curve\'s "x" is absolute value of delta-T (Surface temperature minus air temperature, (C))',
            },
        )
    )
    hn_function_of_temperature_difference_divided_by_height_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve\'s "x" is absolute value of delta-T/Height (Surface temp minus Air temp)/(vertical length scale), (C/m) when used for an outside face the vertical length scale is the exterior facade\'s overall...',
        },
    )


class SurfacePropertiesVaporCoefficients(IDFBaseModel):
    """The interior and external vapor transfer coefficients. Normally these value
    are calculated using the heat convection coefficient values. Use this object
    to used fixed constant values. Units are kg/Pa.s.m2 This will only work with
    the CombinedHeatAndMoistureFiniteElement algorithm for surfaces. Other
    algorithms will ignore these coefficients"""

    _idf_object_type: ClassVar[str] = 'SurfaceProperties:VaporCoefficients'
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    constant_external_vapor_transfer_coefficient: Literal['', 'No', 'Yes'] | None = (
        Field(default='No')
    )
    external_vapor_coefficient_value: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'kg/Pa-s-m2'}
    )
    constant_internal_vapor_transfer_coefficient: Literal['', 'No', 'Yes'] | None = (
        Field(default='No')
    )
    internal_vapor_coefficient_value: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'kg/Pa-s-m2'}
    )


class SurfacePropertyConvectionCoefficients(IDFBaseModel):
    """Allow user settable interior and/or exterior convection coefficients. Note
    that some other factors may limit the lower bounds for these values, such as
    for windows, the interior convection coefficient must be >.28, for trombe
    wall algorithm selection (zone), the interior convection coefficient must be
    >.1 for TARP interior convection, the lower limit is also .1 Minimum and
    maximum limits are set in HeatBalanceAlgorithm object. Defaults in
    HeatBalanceAlgorithm object are [.1,1000]."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:ConvectionCoefficients'
    surface_name: AllHeatTranSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    convection_coefficient_1_location: Literal['Inside', 'Outside'] = Field(...)
    convection_coefficient_1_type: Literal[
        'ASHRAEVerticalWall',
        'ASTMC1340',
        'AdaptiveConvectionAlgorithm',
        'AlamdariHammondStableHorizontal',
        'AlamdariHammondUnstableHorizontal',
        'AlamdariHammondVerticalWall',
        'AwbiHattonHeatedFloor',
        'AwbiHattonHeatedWall',
        'BeausoleilMorrisonMixedAssistedWall',
        'BeausoleilMorrisonMixedOpposingWall',
        'BeausoleilMorrisonMixedStableCeiling',
        'BeausoleilMorrisonMixedStableFloor',
        'BeausoleilMorrisonMixedUnstableCeiling',
        'BeausoleilMorrisonMixedUnstableFloor',
        'BlockenWindard',
        'ClearRoof',
        'DOE-2',
        'EmmelRoof',
        'EmmelVertical',
        'FisherPedersenCeilingDiffuserCeiling',
        'FisherPedersenCeilingDiffuserFloor',
        'FisherPedersenCeilingDiffuserWalls',
        'FohannoPolidoriVerticalWall',
        'GoldsteinNovoselacCeilingDiffuserFloor',
        'GoldsteinNovoselacCeilingDiffuserWalls',
        'GoldsteinNovoselacCeilingDiffuserWindow',
        'ISO15099Windows',
        'KaradagChilledCeiling',
        'KhalifaEq3WallAwayFromHeat',
        'KhalifaEq4CeilingAwayFromHeat',
        'KhalifaEq5WallNearHeat',
        'KhalifaEq6NonHeatedWalls',
        'KhalifaEq7Ceiling',
        'McAdams',
        'Mitchell',
        'MoWitt',
        'NusseltJurges',
        'Schedule',
        'Simple',
        'SimpleCombined',
        'TARP',
        'UserCurve',
        'Value',
        'WaltonStableHorizontalOrTilt',
        'WaltonUnstableHorizontalOrTilt',
    ] = Field(...)
    convection_coefficient_1: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_1_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_1_user_curve_name: UserConvectionModelsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionModels'],
            'note': 'used if Convection Type = UserCurve',
        },
    )
    convection_coefficient_2_location: Literal['Inside', 'Outside'] | None = Field(
        default=None
    )
    convection_coefficient_2_type: (
        Literal[
            'ASHRAEVerticalWall',
            'ASTMC1340',
            'AdaptiveConvectionAlgorithm',
            'AlamdariHammondStableHorizontal',
            'AlamdariHammondUnstableHorizontal',
            'AlamdariHammondVerticalWall',
            'AwbiHattonHeatedFloor',
            'AwbiHattonHeatedWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'BeausoleilMorrisonMixedStableCeiling',
            'BeausoleilMorrisonMixedStableFloor',
            'BeausoleilMorrisonMixedUnstableCeiling',
            'BeausoleilMorrisonMixedUnstableFloor',
            'BlockenWindard',
            'ClearRoof',
            'DOE-2',
            'EmmelRoof',
            'EmmelVertical',
            'FisherPedersenCeilingDiffuserCeiling',
            'FisherPedersenCeilingDiffuserFloor',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserFloor',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'GoldsteinNovoselacCeilingDiffuserWindow',
            'ISO15099Windows',
            'KaradagChilledCeiling',
            'KhalifaEq3WallAwayFromHeat',
            'KhalifaEq4CeilingAwayFromHeat',
            'KhalifaEq5WallNearHeat',
            'KhalifaEq6NonHeatedWalls',
            'KhalifaEq7Ceiling',
            'McAdams',
            'Mitchell',
            'MoWitt',
            'NusseltJurges',
            'Schedule',
            'Simple',
            'SimpleCombined',
            'TARP',
            'UserCurve',
            'Value',
            'WaltonStableHorizontalOrTilt',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(default=None)
    convection_coefficient_2: float | None = Field(
        default=0.1,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_2_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_2_user_curve_name: UserConvectionModelsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionModels'],
            'note': 'used if Convection Type = UserCurve',
        },
    )


class SurfacePropertyConvectionCoefficientsMultipleSurface(IDFBaseModel):
    """Allow user settable interior and/or exterior convection coefficients. Note
    that some other factors may limit the lower bounds for these values, such as
    for windows, the interior convection coefficient must be >.28, for trombe
    wall algorithm selection (zone), the interior convection coefficient must be
    >.1 for TARP interior convection, the lower limit is also .1 Minimum and
    maximum limits are set in HeatBalanceAlgorithm object. Defaults in
    HeatBalanceAlgorithm object are [.1,1000]."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceProperty:ConvectionCoefficients:MultipleSurface'
    )
    surface_type: Literal[
        'AllExteriorFloors',
        'AllExteriorRoofs',
        'AllExteriorSurfaces',
        'AllExteriorWalls',
        'AllExteriorWindows',
        'AllInteriorCeilings',
        'AllInteriorFloors',
        'AllInteriorSurfaces',
        'AllInteriorWalls',
        'AllInteriorWindows',
    ] = Field(...)
    convection_coefficient_1_location: Literal['Inside', 'Outside'] = Field(...)
    convection_coefficient_1_type: Literal[
        'ASHRAEVerticalWall',
        'ASTMC1340',
        'AdaptiveConvectionAlgorithm',
        'AlamdariHammondStableHorizontal',
        'AlamdariHammondUnstableHorizontal',
        'AlamdariHammondVerticalWall',
        'AwbiHattonHeatedFloor',
        'AwbiHattonHeatedWall',
        'BeausoleilMorrisonMixedAssistedWall',
        'BeausoleilMorrisonMixedOpposingWall',
        'BeausoleilMorrisonMixedStableCeiling',
        'BeausoleilMorrisonMixedStableFloor',
        'BeausoleilMorrisonMixedUnstableCeiling',
        'BeausoleilMorrisonMixedUnstableFloor',
        'BlockenWindard',
        'ClearRoof',
        'DOE-2',
        'EmmelRoof',
        'EmmelVertical',
        'FisherPedersenCeilingDiffuserCeiling',
        'FisherPedersenCeilingDiffuserFloor',
        'FisherPedersenCeilingDiffuserWalls',
        'FohannoPolidoriVerticalWall',
        'GoldsteinNovoselacCeilingDiffuserFloor',
        'GoldsteinNovoselacCeilingDiffuserWalls',
        'GoldsteinNovoselacCeilingDiffuserWindow',
        'ISO15099Windows',
        'KaradagChilledCeiling',
        'KhalifaEq3WallAwayFromHeat',
        'KhalifaEq4CeilingAwayFromHeat',
        'KhalifaEq5WallNearHeat',
        'KhalifaEq6NonHeatedWalls',
        'KhalifaEq7Ceiling',
        'McAdams',
        'Mitchell',
        'MoWitt',
        'NusseltJurges',
        'Schedule',
        'Simple',
        'SimpleCombined',
        'TARP',
        'UserCurve',
        'Value',
        'WaltonStableHorizontalOrTilt',
        'WaltonUnstableHorizontalOrTilt',
    ] = Field(...)
    convection_coefficient_1: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_1_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_1_user_curve_name: UserConvectionModelsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionModels'],
            'note': 'used if Convection Type = UserCurve',
        },
    )
    convection_coefficient_2_location: Literal['Inside', 'Outside'] | None = Field(
        default=None
    )
    convection_coefficient_2_type: (
        Literal[
            'ASHRAEVerticalWall',
            'ASTMC1340',
            'AdaptiveConvectionAlgorithm',
            'AlamdariHammondStableHorizontal',
            'AlamdariHammondUnstableHorizontal',
            'AlamdariHammondVerticalWall',
            'AwbiHattonHeatedFloor',
            'AwbiHattonHeatedWall',
            'BeausoleilMorrisonMixedAssistedWall',
            'BeausoleilMorrisonMixedOpposingWall',
            'BeausoleilMorrisonMixedStableCeiling',
            'BeausoleilMorrisonMixedStableFloor',
            'BeausoleilMorrisonMixedUnstableCeiling',
            'BeausoleilMorrisonMixedUnstableFloor',
            'BlockenWindard',
            'ClearRoof',
            'DOE-2',
            'EmmelRoof',
            'EmmelVertical',
            'FisherPedersenCeilingDiffuserCeiling',
            'FisherPedersenCeilingDiffuserFloor',
            'FisherPedersenCeilingDiffuserWalls',
            'FohannoPolidoriVerticalWall',
            'GoldsteinNovoselacCeilingDiffuserFloor',
            'GoldsteinNovoselacCeilingDiffuserWalls',
            'GoldsteinNovoselacCeilingDiffuserWindow',
            'ISO15099Windows',
            'KaradagChilledCeiling',
            'KhalifaEq3WallAwayFromHeat',
            'KhalifaEq4CeilingAwayFromHeat',
            'KhalifaEq5WallNearHeat',
            'KhalifaEq6NonHeatedWalls',
            'KhalifaEq7Ceiling',
            'McAdams',
            'Mitchell',
            'MoWitt',
            'NusseltJurges',
            'Schedule',
            'Simple',
            'SimpleCombined',
            'TARP',
            'UserCurve',
            'Value',
            'WaltonStableHorizontalOrTilt',
            'WaltonUnstableHorizontalOrTilt',
        ]
        | None
    ) = Field(default=None)
    convection_coefficient_2: float | None = Field(
        default=0.1,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'used if Convection Type=Value, min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_2_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'used if Convection Type=Schedule,  min and max limits are set in HeatBalanceAlgorithm object. Default limits are Minimum >= 0.1 and Maximum <= 1000',
        },
    )
    convection_coefficient_2_user_curve_name: UserConvectionModelsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UserConvectionModels'],
            'note': 'used if Convection Type = UserCurve',
        },
    )


class SurfacePropertyExposedFoundationPerimeter(IDFBaseModel):
    """Defines the perimeter of a foundation floor that is exposed to the exterior
    environment through the floor. User may either define the total exposed
    perimeter, fraction of perimeter exposed or individually define which
    segments of the floor surface perimeter are exposed."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:ExposedFoundationPerimeter'
    surface_name: FloorSurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['FloorSurfaceNames']}
    )
    exposed_perimeter_calculation_method: Literal[
        'BySegment', 'ExposedPerimeterFraction', 'TotalExposedPerimeter'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Choices: TotalExposedPerimeter => total exposed perimeter in meters ExposedPerimeterFraction => fraction of total perimeter that is exposed. Value * Fraction = Total exposed perimeter BySegment => ...'
        },
    )
    total_exposed_perimeter: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm'}
    )
    exposed_perimeter_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    surfaces: list[SurfacePropertyExposedFoundationPerimeterSurfacesItem] | None = (
        Field(default=None)
    )


class SurfacePropertyExteriorNaturalVentedCAVity(IDFBaseModel):
    """Used to describe the decoupled layer, or baffle, and the characteristics of
    the cavity and openings for naturally ventilated exterior surfaces. This
    object is also used in conjunction with the OtherSideConditionsModel."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:ExteriorNaturalVentedCavity'
    name: str = Field(...)
    boundary_conditions_model_name: OSCMNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['OSCMNames'],
            'note': 'Enter the name of a SurfaceProperty:OtherSideConditionsModel object',
        },
    )
    area_fraction_of_openings: float | None = Field(
        default=None, le=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    thermal_emissivity_of_exterior_baffle_material: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    solar_absorbtivity_of_exterior_baffle: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    height_scale_for_buoyancy_driven_ventilation: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm'}
    )
    effective_thickness_of_cavity_behind_exterior_baffle: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'if corrugated, use average depth'},
    )
    ratio_of_actual_surface_area_to_projected_surface_area: float | None = Field(
        default=1.0,
        ge=0.8,
        le=2.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'this parameter is used to help account for corrugations in the collector',
        },
    )
    roughness_of_exterior_surface: Literal[
        'MediumRough', 'MediumSmooth', 'Rough', 'Smooth', 'VeryRough', 'VerySmooth'
    ] = Field(...)
    effectiveness_for_perforations_with_respect_to_wind: float | None = Field(
        default=0.25, le=1.5, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow: (
        float | None
    ) = Field(
        default=0.65, le=1.5, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    surface: list[SurfacePropertyExteriorNaturalVentedCAVitySurfaceItem] | None = Field(
        default=None
    )


class SurfacePropertyGroundSurfaces(IDFBaseModel):
    """This object defines a list of ground surfaces for use with an exterior
    surface."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:GroundSurfaces'
    name: str = Field(...)
    ground_surfaces: list[SurfacePropertyGroundSurfacesGroundSurfacesItem] | None = (
        Field(default=None)
    )


class SurfacePropertyHeatBalanceSourceTerm(IDFBaseModel):
    """Allows an additional heat source term to be added to the inside or outside
    surface boundary. A heat source can be added to either or both the inside
    and outside of the same surface."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:HeatBalanceSourceTerm'
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    inside_face_heat_source_term_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The value of this schedule is the source term value for the inside face of this surface If this field is left blank, no inside surface source term will be applied. The schedule values are heat rate...',
        },
    )
    outside_face_heat_source_term_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The value of this schedule is the source term value for the outside face of this surface If this field is left blank, no outside surface source term will be applied. The schedule values are heat ra...',
        },
    )


class SurfacePropertyHeatTransferAlgorithm(IDFBaseModel):
    """Determines which Heat Balance Algorithm will be used for a specific surface
    Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF
    (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth
    with Conduction Transfer Functions). Advanced/Research Usage: CondFD
    (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat
    And Moisture Finite Element)"""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:HeatTransferAlgorithm'
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    algorithm: (
        Literal[
            '',
            'CombinedHeatAndMoistureFiniteElement',
            'ConductionFiniteDifference',
            'ConductionTransferFunction',
            'MoisturePenetrationDepthConductionTransferFunction',
        ]
        | None
    ) = Field(default='ConductionTransferFunction')


class SurfacePropertyHeatTransferAlgorithmConstruction(IDFBaseModel):
    """Determines which Heat Balance Algorithm will be used for surfaces that have
    a specific type of construction Allows selectively overriding the global
    setting in HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD
    (Effective Moisture Penetration Depth with Conduction Transfer Functions).
    Advanced/Research Usage: CondFD (Conduction Finite Difference)
    Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)"""

    _idf_object_type: ClassVar[str] = (
        'SurfaceProperty:HeatTransferAlgorithm:Construction'
    )
    name: str | None = Field(default=None)
    algorithm: (
        Literal[
            '',
            'CombinedHeatAndMoistureFiniteElement',
            'ConductionFiniteDifference',
            'ConductionTransferFunction',
            'MoisturePenetrationDepthConductionTransferFunction',
        ]
        | None
    ) = Field(default='ConductionTransferFunction')
    construction_name: ConstructionNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ConstructionNames']}
    )


class SurfacePropertyHeatTransferAlgorithmMultipleSurface(IDFBaseModel):
    """Determines which Heat Balance Algorithm will be used for a group of surface
    types Allows selectively overriding the global setting in
    HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD (Effective
    Moisture Penetration Depth with Conduction Transfer Functions).
    Advanced/Research Usage: CondFD (Conduction Finite Difference)
    Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)"""

    _idf_object_type: ClassVar[str] = (
        'SurfaceProperty:HeatTransferAlgorithm:MultipleSurface'
    )
    name: str = Field(...)
    surface_type: Literal[
        'AllExteriorFloors',
        'AllExteriorRoofs',
        'AllExteriorSurfaces',
        'AllExteriorWalls',
        'AllGroundContactSurfaces',
        'AllInteriorCeilings',
        'AllInteriorFloors',
        'AllInteriorSurfaces',
        'AllInteriorWalls',
    ] = Field(...)
    algorithm: (
        Literal[
            '',
            'CombinedHeatAndMoistureFiniteElement',
            'ConductionFiniteDifference',
            'ConductionTransferFunction',
            'MoisturePenetrationDepthConductionTransferFunction',
        ]
        | None
    ) = Field(default='ConductionTransferFunction')


class SurfacePropertyHeatTransferAlgorithmSurfaceList(IDFBaseModel):
    """Determines which Heat Balance Algorithm will be used for a list of surfaces
    Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF
    (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth
    with Conduction Transfer Functions). Advanced/Research Usage: CondFD
    (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat
    And Moisture Finite Element)"""

    _idf_object_type: ClassVar[str] = (
        'SurfaceProperty:HeatTransferAlgorithm:SurfaceList'
    )
    name: str = Field(...)
    algorithm: (
        Literal[
            '',
            'CombinedHeatAndMoistureFiniteElement',
            'ConductionFiniteDifference',
            'ConductionTransferFunction',
            'MoisturePenetrationDepthConductionTransferFunction',
        ]
        | None
    ) = Field(default='ConductionTransferFunction')
    surface: list[SurfacePropertyHeatTransferAlgorithmSurfaceListSurfaceItem] | None = (
        Field(default=None)
    )


class SurfacePropertyIncidentSolarMultiplier(IDFBaseModel):
    """SurfaceProperty:IncidentSolarMultiplier"""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:IncidentSolarMultiplier'
    surface_name: SurfaceNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SurfaceNames'],
            'note': 'Enter the name of an exterior window outside surface object',
        },
    )
    incident_solar_multiplier: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'a constant multiplier for window solar transmittance and visible transmittance. If the Shading Multiplier Schedule Name is defined, the product of these two will be the final shading multiplier.',
        },
    )
    incident_solar_multiplier_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule values should be greater than or equal to 0 and less than or equal to 1.',
        },
    )


class SurfacePropertyLocalEnvironment(IDFBaseModel):
    """This object defines the local environment properties of an exterior surface.
    One or more environment properties have to be defined and linked to the
    exterior surface."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:LocalEnvironment'
    name: str = Field(...)
    exterior_surface_name: SurfaceNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SurfaceNames'],
            'note': 'Enter the name of an exterior surface object',
        },
    )
    sunlit_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a Schedule object',
        },
    )
    surrounding_surfaces_object_name: SurroundingSurfacesNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SurroundingSurfacesNames'],
            'note': 'Enter the name of a SurfaceProperty:SurroundingSurfaces object',
        },
    )
    outdoor_air_node_name: OutdoorAirNodeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirNodeNames'],
            'note': 'Enter the name of an OutdoorAir:Node object',
        },
    )
    ground_surfaces_object_name: GroundSurfacesNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['GroundSurfacesNames'],
            'note': 'Enter the name of a SurfaceProperty:GroundSurfaces object',
        },
    )


class SurfacePropertyOtherSideCoefficients(IDFBaseModel):
    """This object sets the other side conditions for a surface in a variety of
    ways."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:OtherSideCoefficients'
    name: str = Field(...)
    combined_convective_radiative_film_coefficient: float = Field(
        ...,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'if>0, this field becomes the exterior convective/radiative film coefficient and the other fields are used to calculate the outdoor air temperature then exterior surface temperature based on outdoor...',
        },
    )
    constant_temperature: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This parameter will be overwritten by the values from the Constant Temperature Schedule Name (below) if one is present',
        },
    )
    constant_temperature_coefficient: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'This coefficient is used even with a Schedule. It should normally be 1.0 in that case. This field is ignored if Sinusoidal Variation of Constant Temperature Coefficient = Yes.'
        },
    )
    external_dry_bulb_temperature_coefficient: float | None = Field(default=0.0)
    ground_temperature_coefficient: float | None = Field(default=0.0)
    wind_speed_coefficient: float | None = Field(default=0.0)
    zone_air_temperature_coefficient: float | None = Field(default=0.0)
    constant_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Name of schedule for values of constant temperature. Schedule values replace any value specified in the field Constant Temperature.',
        },
    )
    sinusoidal_variation_of_constant_temperature_coefficient: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='No',
        json_schema_extra={
            'note': 'Optionally used to vary Constant Temperature Coefficient with unitary sine wave'
        },
    )
    period_of_sinusoidal_variation: float | None = Field(
        default=24.0,
        gt=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Use with sinusoidal variation to define the time period',
        },
    )
    previous_other_side_temperature_coefficient: float | None = Field(
        default=0.0,
        json_schema_extra={
            'note': 'This coefficient multiplies the other side temperature result from the previous zone timestep'
        },
    )
    minimum_other_side_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'This field specifies a lower limit for the other side temperature result. Blank indicates no limit',
        },
    )
    maximum_other_side_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'This field specifies an upper limit for the other side temperature result. Blank indicates no limit',
        },
    )


class SurfacePropertyOtherSideConditionsModel(IDFBaseModel):
    """This object sets up modifying the other side conditions for a surface from
    other model results."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:OtherSideConditionsModel'
    name: str = Field(...)
    type_of_modeling: (
        Literal[
            '',
            'ConvectiveUnderwater',
            'GapConvectionRadiation',
            'GroundCoupledSurface',
            'UndergroundPipingSystemSurface',
        ]
        | None
    ) = Field(
        default='GapConvectionRadiation',
        json_schema_extra={
            'note': 'GapConvectionRadiation provides boundary conditions for convection and linearized thermal radiation across a gap or cavity on the other side of the surface that are modeled separately. UndergroundP...'
        },
    )


class SurfacePropertySolarIncidentInside(IDFBaseModel):
    """Used to provide incident solar radiation on the inside of the surface.
    Reference surface-construction pair and if that pair is used in a
    simulation, then program will use value provided in schedule instead of
    calculating it."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:SolarIncidentInside'
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    construction_name: ConstructionNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ConstructionNames']}
    )
    inside_surface_incident_sun_solar_radiation_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in schedule are expected to be in W/m2',
        },
    )


class SurfacePropertySurroundingSurfaces(IDFBaseModel):
    """This object defines a list of surrounding surfaces for an exterior surface."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:SurroundingSurfaces'
    name: str = Field(...)
    sky_view_factor: float | None = Field(
        default=0.5, ge=0.0, le=1.0, json_schema_extra={'note': 'optional'}
    )
    sky_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are real numbers, -100.0 to 100.0, units C optional',
        },
    )
    ground_view_factor: float | None = Field(
        default=0.5, ge=0.0, le=1.0, json_schema_extra={'note': 'optional'}
    )
    ground_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are real numbers, -100.0 to 100.0, units C optional',
        },
    )
    surfaces: list[SurfacePropertySurroundingSurfacesSurfacesItem] | None = Field(
        default=None
    )


class SurfacePropertyUnderwater(IDFBaseModel):
    """This object sets up a convective water boundary condition for a surface The
    free stream temperature and velocity are scheduled. If the free stream
    velocity is zero, the surface will naturally convect with the surrounding
    water."""

    _idf_object_type: ClassVar[str] = 'SurfaceProperty:Underwater'
    name: str = Field(...)
    distance_from_surface_centroid_to_leading_edge_of_boundary_layer: float = Field(
        ...,
        json_schema_extra={
            'units': 'm',
            'note': 'This is the distance from the leading edge of the boundary layer development to the centroid of the surface of interest. The value of this field is used as the distance in the Reynolds number for e...',
        },
    )
    free_stream_water_temperature_schedule: ScheduleNamesRef = Field(
        ..., json_schema_extra={'units': 'C', 'object_list': ['ScheduleNames']}
    )
    free_stream_water_velocity_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={'units': 'm/s', 'object_list': ['ScheduleNames']},
    )


class ZonePropertyLocalEnvironment(IDFBaseModel):
    """This object defines the local environment properties of a zone object. A
    corresponding outdoor air node should be defined and linked to the zone
    object."""

    _idf_object_type: ClassVar[str] = 'ZoneProperty:LocalEnvironment'
    name: str = Field(...)
    zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter the name of a zone object',
        },
    )
    outdoor_air_node_name: OutdoorAirNodeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirNodeNames'],
            'note': 'Enter the name of an OutdoorAir:Node object',
        },
    )


class ZonePropertyUserViewFactorsBySurfaceName(IDFBaseModel):
    """View factors for Surface to Surface in a zone. (Number of Surfaces)**2 are
    expected. Any omitted surface pairs will be assumed to have a view factor of
    zero."""

    _idf_object_type: ClassVar[str] = 'ZoneProperty:UserViewFactors:BySurfaceName'
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceListNamesRef | SpaceNamesRef | ZoneListNamesRef | ZoneNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'SpaceListNames',
                'SpaceNames',
                'ZoneListNames',
                'ZoneNames',
            ],
            'note': 'View factors may be entered for a space, zone, group of spaces, or group of zones in the same enclosure by way of Construction:AirBoundary or open spaces within a zone. This name must align with an...',
        },
    )
    view_factors: (
        list[ZonePropertyUserViewFactorsBySurfaceNameViewFactorsItem] | None
    ) = Field(default=None)
