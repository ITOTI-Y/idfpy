"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Solar Collectors
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllShadingAndHTSurfNamesRef,
    CollectorStoragePerformanceRef,
    FlatPlatePVTParametersRef,
    FlatPlateSolarCollectorParametersRef,
    OSCMNamesRef,
    PVGeneratorNamesRef,
    ScheduleNamesRef,
    UTSCNamesRef,
)


class SolarCollectorUnglazedTranspiredSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )


class SolarCollectorUnglazedTranspiredMultisystemSystemsItem(IDFBaseModel):
    """Nested object type for array items."""

    outdoor_air_system_collector_inlet_node: str | None = Field(default=None)
    outdoor_air_system_collector_outlet_node: str | None = Field(default=None)
    outdoor_air_system_mixed_air_node: str | None = Field(default=None)
    outdoor_air_system_zone_node: str | None = Field(default=None)


class SolarCollectorFlatPlatePhotovoltaicThermal(IDFBaseModel):
    """Models hybrid photovoltaic-thermal (PVT) solar collectors that convert
    incident solar energy into both electricity and useful thermal energy by
    heating air or water."""

    _idf_object_type: ClassVar[str] = 'SolarCollector:FlatPlate:PhotovoltaicThermal'
    name: str | None = Field(default=None)
    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )
    photovoltaic_thermal_model_performance_name: FlatPlatePVTParametersRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['FlatPlatePVTParameters']}
        )
    )
    photovoltaic_name: PVGeneratorNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PVGeneratorNames'],
            'note': 'Enter the name of a Generator:Photovoltaic object.',
        },
    )
    thermal_working_fluid_type: Literal['Air', 'Water'] | None = Field(default=None)
    water_inlet_node_name: str | None = Field(default=None)
    water_outlet_node_name: str | None = Field(default=None)
    air_inlet_node_name: str | None = Field(default=None)
    air_outlet_node_name: str | None = Field(default=None)
    design_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )


class SolarCollectorFlatPlateWater(IDFBaseModel):
    """Flat plate water solar collector (single glazed, unglazed, or evacuated
    tube). Thermal and optical properties are taken from the referenced
    SolarCollectorPerformance:FlatPlate object. Collector tilt, azimuth, and
    gross area are taken from the referenced building surface or shading
    surface. The collector surface participates normally in all shading
    calculations."""

    _idf_object_type: ClassVar[str] = 'SolarCollector:FlatPlate:Water'
    name: str = Field(...)
    solarcollectorperformance_name: FlatPlateSolarCollectorParametersRef = Field(
        ..., json_schema_extra={'object_list': ['FlatPlateSolarCollectorParameters']}
    )
    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    maximum_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3/s'}
    )


class SolarCollectorIntegralCollectorStorage(IDFBaseModel):
    """Glazed solar collector with integral storage unit. Thermal and optical
    properties are taken from the referenced
    SolarCollectorPerformance:IntegralCollectorStorage object. Collector tilt,
    azimuth, and gross area are taken from the referenced building surface or
    shading surface. The collector surface participates normally in all shading
    calculations."""

    _idf_object_type: ClassVar[str] = 'SolarCollector:IntegralCollectorStorage'
    name: str = Field(...)
    integralcollectorstorageparameters_name: CollectorStoragePerformanceRef = Field(
        ..., json_schema_extra={'object_list': ['CollectorStoragePerformance']}
    )
    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )
    bottom_surface_boundary_conditions_type: (
        Literal['', 'AmbientAir', 'OtherSideConditionsModel'] | None
    ) = Field(default='AmbientAir')
    boundary_condition_model_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of a SurfaceProperty:OtherSideConditionsModel object. Specified only if the boundary condition type is OtherSideConditionsModel, otherwise leave it blank'
        },
    )
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    maximum_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3/s'}
    )


class SolarCollectorPerformanceFlatPlate(IDFBaseModel):
    """Thermal and optical performance parameters for a single flat plate solar
    collector module. These parameters are based on the testing methodologies
    described in ASHRAE Standards 93 and 96 which are used Solar Rating and
    Certification Corporation (SRCC) Directory of SRCC Certified Solar Collector
    Ratings. See EnergyPlus DataSets file SolarCollectors.idf."""

    _idf_object_type: ClassVar[str] = 'SolarCollectorPerformance:FlatPlate'
    name: str = Field(...)
    gross_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2'})
    test_fluid: Literal['', 'Water'] | None = Field(default='Water')
    test_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    test_correlation_type: Literal['Average', 'Inlet', 'Outlet'] = Field(...)
    coefficient_1_of_efficiency_equation: float = Field(
        ..., json_schema_extra={'units': 'dimensionless', 'note': 'Y-intercept term'}
    )
    coefficient_2_of_efficiency_equation: float = Field(
        ..., json_schema_extra={'units': 'W/m2-K', 'note': '1st Order term'}
    )
    coefficient_3_of_efficiency_equation: float | None = Field(
        default=None, json_schema_extra={'units': 'W/m2-K2', 'note': '2nd order term'}
    )
    coefficient_2_of_incident_angle_modifier: float | None = Field(
        default=None, json_schema_extra={'note': '1st order term'}
    )
    coefficient_3_of_incident_angle_modifier: float | None = Field(
        default=None, json_schema_extra={'note': '2nd order term'}
    )


class SolarCollectorPerformanceIntegralCollectorStorage(IDFBaseModel):
    """Thermal and optical performance parameters for a single glazed solar
    collector with integral storage unit."""

    _idf_object_type: ClassVar[str] = (
        'SolarCollectorPerformance:IntegralCollectorStorage'
    )
    name: str = Field(...)
    ics_collector_type: Literal['', 'RectangularTank'] | None = Field(
        default='RectangularTank',
        json_schema_extra={
            'note': 'Currently only RectangularTank ICS collector type is available.'
        },
    )
    gross_area: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm2'}
    )
    collector_water_volume: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3'}
    )
    bottom_heat_loss_conductance: float | None = Field(
        default=0.4,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'Heat loss conductance of the collector bottom insulation',
        },
    )
    side_heat_loss_conductance: float | None = Field(
        default=0.6,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'heat loss conductance of the collector side insulation',
        },
    )
    aspect_ratio: float | None = Field(
        default=0.8,
        gt=0.5,
        lt=1.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This value is ratio of the width (short side) to length (long side of) of the collector. Used to calculate the perimeter of the collector',
        },
    )
    collector_side_height: float | None = Field(
        default=0.2,
        gt=0.0,
        lt=0.3,
        json_schema_extra={
            'units': 'm',
            'note': 'This value is used to estimate collector side area for the heat loss calculation through the collector side',
        },
    )
    thermal_mass_of_absorber_plate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'J/m2-K',
            'note': 'Calculated from the specific heat, density and thickness of the absorber plate.',
        },
    )
    number_of_covers: int | None = Field(
        default=2,
        ge=1,
        le=2,
        json_schema_extra={
            'note': 'Number of transparent covers. Common practice is to use low-iron glass as the outer cover and very thin transparent sheet such as Teflon as the inner cover.'
        },
    )
    cover_spacing: float | None = Field(
        default=0.05,
        le=0.2,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'The gap between the transparent covers and between the inner cover and the absorber plate',
        },
    )
    refractive_index_of_outer_cover: float | None = Field(
        default=1.526,
        ge=1.0,
        le=2.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Refractive index of outer cover. Typically low-iron glass is used as the outer cover material, and used as the default outer cover with a value of 1.526.',
        },
    )
    extinction_coefficient_times_thickness_of_outer_cover: float | None = Field(
        default=0.045,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Clear glass has extinction coefficient of about 15 [1/m] and with thickness of 3.0mm, the product of the extinction coefficient and thickness becomes 0.045 (=15 * 0.003)',
        },
    )
    emissivity_of_outer_cover: float | None = Field(
        default=0.88,
        gt=0.0,
        lt=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Thermal emissivity of the outer cover, commonly glass is used as the out collector cover material.',
        },
    )
    refractive_index_of_inner_cover: float | None = Field(
        default=1.37,
        ge=1.0,
        le=2.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Typical material is very thin sheet of Teflon (PTFE). The default value is refractive index of Teflon.',
        },
    )
    extinction_coefficient_times_thickness_of_the_inner_cover: float | None = Field(
        default=0.008,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Default inner cover is very thin sheet of Teflon with extinction coefficient of approximately 40.0 and a thickness 0.2mm yields a default value of 0.008.',
        },
    )
    emissivity_of_inner_cover: float | None = Field(
        default=0.88,
        gt=0.0,
        lt=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Thermal emissivity of the inner cover material',
        },
    )
    absorptance_of_absorber_plate: float | None = Field(
        default=0.96,
        gt=0.0,
        lt=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The absorber plate solar absorptance. Copper is assumed as the default absorber plate.',
        },
    )
    emissivity_of_absorber_plate: float | None = Field(
        default=0.3,
        gt=0.0,
        lt=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Thermal emissivity of the absorber plate',
        },
    )


class SolarCollectorPerformancePhotovoltaicThermalBIPVT(IDFBaseModel):
    """Thermal performance parameters for Building-Integrated Photovoltaic-Thermal
    (BIPVT) solar collector."""

    _idf_object_type: ClassVar[str] = (
        'SolarCollectorPerformance:PhotovoltaicThermal:BIPVT'
    )
    name: str | None = Field(default=None)
    boundary_conditions_model_name: OSCMNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['OSCMNames'],
            'note': 'Enter the name of a SurfaceProperty:OtherSideConditionsModel object',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this collector. Schedule value > 0 means it is available. If this field is blank, the collector is always available.',
        },
    )
    effective_plenum_gap_thickness_behind_pv_modules: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm'}
    )
    pv_cell_normal_transmittance_absorptance_product: float | None = Field(
        default=0.957, gt=0.0, lt=1.0
    )
    backing_material_normal_transmittance_absorptance_product: float | None = Field(
        default=0.87, gt=0.0, lt=1.0
    )
    cladding_normal_transmittance_absorptance_product: float | None = Field(
        default=0.85, gt=0.0, lt=1.0
    )
    fraction_of_collector_gross_area_covered_by_pv_module: float | None = Field(
        default=0.85, gt=0.0, lt=1.0
    )
    fraction_of_pv_cell_area_to_pv_module_area: float | None = Field(
        default=0.9, gt=0.0, lt=1.0
    )
    pv_module_top_thermal_resistance: float | None = Field(
        default=0.0044, gt=0.0, json_schema_extra={'units': 'm2-K/W'}
    )
    pv_module_bottom_thermal_resistance: float | None = Field(
        default=0.0039, gt=0.0, json_schema_extra={'units': 'm2-K/W'}
    )
    pv_module_front_longwave_emissivity: float | None = Field(
        default=0.85, gt=0.0, lt=1.0
    )
    pv_module_back_longwave_emissivity: float | None = Field(
        default=0.9, gt=0.0, lt=1.0
    )
    glass_thickness: float | None = Field(
        default=0.002, gt=0.0, lt=0.01, json_schema_extra={'units': 'm'}
    )
    glass_refraction_index: float | None = Field(default=1.526, gt=1.0, lt=10.0)
    glass_extinction_coefficient: float | None = Field(
        default=4.0, gt=0.0, lt=100.0, json_schema_extra={'units': '1/m'}
    )


class SolarCollectorPerformancePhotovoltaicThermalSimple(IDFBaseModel):
    """Thermal performance parameters for a hybrid photovoltaic-thermal (PVT) solar
    collector."""

    _idf_object_type: ClassVar[str] = (
        'SolarCollectorPerformance:PhotovoltaicThermal:Simple'
    )
    name: str | None = Field(default=None)
    fraction_of_surface_area_with_active_thermal_collector: float = Field(
        ..., le=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    thermal_conversion_efficiency_input_mode_type: (
        Literal['Fixed', 'Scheduled'] | None
    ) = Field(default=None)
    value_for_thermal_conversion_efficiency_if_fixed: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Efficiency = (thermal power generated [W])/(incident solar[W])'
        },
    )
    thermal_conversion_efficiency_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    front_surface_emittance: float | None = Field(default=0.84, gt=0.0, lt=1.0)


class SolarCollectorUnglazedTranspired(IDFBaseModel):
    """Unglazed transpired solar collector (UTSC) used to condition outdoor air.
    This type of collector is generally used to heat air drawn through
    perforated absorbers and also recover heat conducted out through the
    underlying surface. This object represents a single collector attached to
    one or more building or shading surfaces and to one or more outdoor air
    systems."""

    _idf_object_type: ClassVar[str] = 'SolarCollector:UnglazedTranspired'
    name: str = Field(...)
    boundary_conditions_model_name: OSCMNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['OSCMNames'],
            'note': 'Enter the name of a SurfaceProperty:OtherSideConditionsModel object',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this collector. Schedule value > 0 means it is available. If this field is blank, the collector is always available.',
        },
    )
    inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required field if no SolarCollector:UnglazedTranspired:Multisystem'
        },
    )
    outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required field if no SolarCollector:UnglazedTranspired:Multisystem'
        },
    )
    setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This node is where the mixed air setpoint is determined. required field if no SolarCollector:UnglazedTranspired:Multisystem'
        },
    )
    zone_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This node is used to identify the affected zone required field if no SolarCollector:UnglazedTranspired:Multisystem'
        },
    )
    free_heating_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    diameter_of_perforations_in_collector: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm'}
    )
    distance_between_perforations_in_collector: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm'}
    )
    thermal_emissivity_of_collector_surface: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    solar_absorbtivity_of_collector_surface: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    effective_overall_height_of_collector: float = Field(..., gt=0.0)
    effective_gap_thickness_of_plenum_behind_collector: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'if corrugated, use average depth'},
    )
    effective_cross_section_area_of_plenum_behind_collector: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm2', 'note': 'if corrugated, use average depth'},
    )
    hole_layout_pattern_for_pitch: Literal['', 'Square', 'Triangle'] | None = Field(
        default='Square'
    )
    heat_exchange_effectiveness_correlation: (
        Literal['', 'Kutscher1994', 'VanDeckerHollandsBrunger2001'] | None
    ) = Field(default='Kutscher1994')
    ratio_of_actual_collector_surface_area_to_projected_surface_area: float | None = (
        Field(
            default=1.0,
            ge=1.0,
            le=2.0,
            json_schema_extra={
                'units': 'dimensionless',
                'note': 'This parameter is used to help account for corrugations in the collector',
            },
        )
    )
    roughness_of_collector: Literal[
        'MediumRough', 'MediumSmooth', 'Rough', 'Smooth', 'VeryRough', 'VerySmooth'
    ] = Field(...)
    collector_thickness: float | None = Field(
        default=None,
        ge=0.0005,
        le=0.007,
        json_schema_extra={
            'units': 'm',
            'note': 'Collector thickness is not required for Kutscher correlation Collector thickness is required for Van Decker et al. correlation',
        },
    )
    effectiveness_for_perforations_with_respect_to_wind: float | None = Field(
        default=0.25,
        le=1.5,
        gt=0.0,
        json_schema_extra={'units': 'dimensionless', 'note': 'Cv'},
    )
    discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow: (
        float | None
    ) = Field(
        default=0.65,
        le=1.5,
        gt=0.0,
        json_schema_extra={'units': 'dimensionless', 'note': 'Cd'},
    )
    surfaces: list[SolarCollectorUnglazedTranspiredSurfacesItem] | None = Field(
        default=None
    )


class SolarCollectorUnglazedTranspiredMultisystem(IDFBaseModel):
    """quad-tuples of inlet, outlet, control, and zone nodes for multiple different
    outdoor air systems attached to same collector"""

    _idf_object_type: ClassVar[str] = 'SolarCollector:UnglazedTranspired:Multisystem'
    solar_collector_name: UTSCNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UTSCNames'],
            'note': 'Enter the name of a SolarCollector:UnglazedTranspired object.',
        },
    )
    systems: list[SolarCollectorUnglazedTranspiredMultisystemSystemsItem] | None = (
        Field(default=None)
    )
