"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Simulation Parameters
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ScheduleNamesRef,
    ZoneAndZoneListNamesRef,
    ZoneListNamesRef,
)


class ShadowCalculationShadingZoneGroupsItem(IDFBaseModel):
    """Nested object type for array items."""
    shading_zone_group_zonelist_name: ZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneListNames'], 'note': 'Specifies a group of zones which are controlled by the Disable Self-Shading fields.'})



class Building(IDFBaseModel):
    """Describes parameters that are used during the simulation of the building.
There are necessary correlations between the entries for this object and
some entries in the Site:WeatherStation and Site:HeightVariation objects,
specifically the Terrain field."""

    _idf_object_type: ClassVar[str] = "Building"
    name: str | None = Field(default='NONE')
    north_axis: float | None = Field(default=0.0, json_schema_extra={'units': 'deg', 'note': 'degrees from true North'})
    terrain: Literal['', 'City', 'Country', 'Ocean', 'Suburbs', 'Urban'] | None = Field(default='Suburbs', json_schema_extra={'note': 'Country=FlatOpenCountry | Suburbs=CountryTownsSuburbs | City=CityCenter | Ocean=body of water (5km) | Urban=Urban-Industrial-Forest'})
    loads_convergence_tolerance_value: float | None = Field(default=0.04, le=0.5, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Loads Convergence Tolerance Value is a change in load from one warmup day to the next'})
    temperature_convergence_tolerance_value: float | None = Field(default=0.4, le=0.5, gt=0.0, json_schema_extra={'units': 'deltaC'})
    solar_distribution: Literal['', 'FullExterior', 'FullExteriorWithReflections', 'FullInteriorAndExterior', 'FullInteriorAndExteriorWithReflections', 'MinimalShadowing'] | None = Field(default='FullExterior', json_schema_extra={'note': 'MinimalShadowing | FullExterior | FullInteriorAndExterior | FullExteriorWithReflections | FullInteriorAndExteriorWithReflections'})
    maximum_number_of_warmup_days: int | None = Field(default=25, gt=0, json_schema_extra={'note': "EnergyPlus will only use as many warmup days as needed to reach convergence tolerance. This field's value should NOT be set less than 25."})
    minimum_number_of_warmup_days: int | None = Field(default=1, gt=0, json_schema_extra={'note': 'The minimum number of warmup days that produce enough temperature and flux history to start EnergyPlus simulation for all reference buildings was suggested to be 6. However this can lead to excessi...'})


class ConvergenceLimits(IDFBaseModel):
    """Specifies limits on HVAC system simulation timesteps and iterations. This
item is an advanced feature that should be used only with caution."""

    _idf_object_type: ClassVar[str] = "ConvergenceLimits"
    minimum_system_timestep: int | None = Field(default=None, ge=0, le=60, json_schema_extra={'units': 'minutes', 'note': '0 sets the minimum to the zone timestep (ref: Timestep) 1 is normal (ratchet down to 1 minute) setting greater than zone timestep (in minutes) will effectively set to zone timestep'})
    maximum_hvac_iterations: int | None = Field(default=20, ge=1)
    minimum_plant_iterations: int | None = Field(default=2, ge=1, json_schema_extra={'note': 'Controls the minimum number of plant system solver iterations within a single HVAC iteration Larger values will increase runtime but might improve solution accuracy for complicated plant systems Co...'})
    maximum_plant_iterations: int | None = Field(default=8, ge=2, json_schema_extra={'note': 'Controls the maximum number of plant system solver iterations within a single HVAC iteration Smaller values might decrease runtime but could decrease solution accuracy for complicated plant systems'})


class HVACSystemRootFindingAlgorithm(IDFBaseModel):
    """Specifies a HVAC system solver algorithm to find a root"""

    _idf_object_type: ClassVar[str] = "HVACSystemRootFindingAlgorithm"
    algorithm: Literal['', 'Alternation', 'Bisection', 'BisectionThenRegulaFalsi', 'RegulaFalsi', 'RegulaFalsiThenBisection'] | None = Field(default='RegulaFalsi')
    number_of_iterations_before_algorithm_switch: int | None = Field(default=5, json_schema_extra={'note': 'This field is used when RegulaFalsiThenBisection or BisectionThenRegulaFalsi is entered. When iteration number is greater than the value, algorithm switches.'})


class HeatBalanceAlgorithm(IDFBaseModel):
    """Determines which Heat Balance Algorithm will be used ie. CTF (Conduction
Transfer Functions), EMPD (Effective Moisture Penetration Depth with
Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction
Finite Difference) Advanced/Research Usage:
ConductionFiniteDifferenceSimplified Advanced/Research Usage: HAMT (Combined
Heat And Moisture Finite Element)"""

    _idf_object_type: ClassVar[str] = "HeatBalanceAlgorithm"
    algorithm: Literal['', 'CombinedHeatAndMoistureFiniteElement', 'ConductionFiniteDifference', 'ConductionTransferFunction', 'MoisturePenetrationDepthConductionTransferFunction'] | None = Field(default='ConductionTransferFunction')
    surface_temperature_upper_limit: float | None = Field(default=200.0, ge=200.0, json_schema_extra={'units': 'C'})
    minimum_surface_convection_heat_transfer_coefficient_value: float | None = Field(default=0.1, gt=0.0, json_schema_extra={'units': 'W/m2-K'})
    maximum_surface_convection_heat_transfer_coefficient_value: float | None = Field(default=1000.0, ge=1.0, json_schema_extra={'units': 'W/m2-K'})


class HeatBalanceSettingsConductionFiniteDifference(IDFBaseModel):
    """Determines settings for the Conduction Finite Difference algorithm for
surface heat transfer modeling."""

    _idf_object_type: ClassVar[str] = "HeatBalanceSettings:ConductionFiniteDifference"
    difference_scheme: Literal['', 'CrankNicholsonSecondOrder', 'FullyImplicitFirstOrder'] | None = Field(default='FullyImplicitFirstOrder')
    space_discretization_constant: float | None = Field(default=3.0, json_schema_extra={'note': 'increase or decrease number of nodes'})
    relaxation_factor: float | None = Field(default=1.0, ge=0.01, le=1.0)
    inside_face_surface_temperature_convergence_criteria: float | None = Field(default=0.002, ge=1e-07, le=0.01)


class PerformancePrecisionTradeoffs(IDFBaseModel):
    """This object enables users to choose certain options that speed up EnergyPlus
simulation, but may lead to small decreases in accuracy of results."""

    _idf_object_type: ClassVar[str] = "PerformancePrecisionTradeoffs"
    use_coil_direct_solutions: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, an analytical or empirical solution will be used to replace iterations in the coil performance calculations.'})
    zone_radiant_exchange_algorithm: Literal['', 'CarrollMRT', 'ScriptF'] | None = Field(default='ScriptF', json_schema_extra={'note': 'Determines which algorithm will be used to solve long wave radiant exchange among surfaces within a zone.'})
    override_mode: Literal['', 'Advanced', 'Mode01', 'Mode02', 'Mode03', 'Mode04', 'Mode05', 'Mode06', 'Mode07', 'Mode08', 'Normal'] | None = Field(default='Normal', json_schema_extra={'note': 'The increasing mode number roughly correspond with increased speed. A description of each mode are shown in the documentation. When Advanced is selected the N1 field value is used.'})
    maxzonetempdiff: float | None = Field(default=0.3, ge=0.1, le=3.0, json_schema_extra={'note': 'Maximum zone temperature change before HVAC timestep is shortened. Only used when Override Mode is set to Advanced'})
    maxalloweddeltemp: float | None = Field(default=0.002, ge=0.002, le=0.1, json_schema_extra={'note': 'Maximum surface temperature change before HVAC timestep is shortened. Only used when Override Mode is set to Advanced'})
    use_representative_surfaces_for_calculations: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'Automatically group surfaces with similar characteristics and perform relevant calculations only once for each group.'})


class ShadowCalculation(IDFBaseModel):
    """This object is used to control details of the solar, shading, and
daylighting models"""

    _idf_object_type: ClassVar[str] = "ShadowCalculation"
    shading_calculation_method: Literal['', 'Imported', 'PixelCounting', 'PolygonClipping', 'Scheduled'] | None = Field(default='PolygonClipping', json_schema_extra={'note': 'Select between CPU-based polygon clipping method, the GPU-based pixel counting method, or importing from external shading data. If PixelCounting is selected and GPU hardware (or GPU emulation) is n...'})
    shading_calculation_update_frequency_method: Literal['', 'Periodic', 'Timestep'] | None = Field(default='Periodic', json_schema_extra={'note': 'choose calculation frequency method. note that Timestep is only needed for certain cases and can increase execution time significantly.'})
    shading_calculation_update_frequency: int | None = Field(default=20, ge=1, json_schema_extra={'note': 'enter number of days this field is only used if the previous field is set to Periodic warning issued if >31'})
    maximum_figures_in_shadow_overlap_calculations: int | None = Field(default=15000, ge=200, json_schema_extra={'note': 'Number of allowable figures in shadow overlap in PolygonClipping calculations'})
    polygon_clipping_algorithm: Literal['', 'ConvexWeilerAtherton', 'SlaterBarskyandSutherlandHodgman', 'SutherlandHodgman'] | None = Field(default='SutherlandHodgman', json_schema_extra={'note': 'Advanced Feature. Internal default is SutherlandHodgman Refer to InputOutput Reference and Engineering Reference for more information'})
    pixel_counting_resolution: int | None = Field(default=512, json_schema_extra={'note': 'Number of pixels in both dimensions of the surface rendering'})
    sky_diffuse_modeling_algorithm: Literal['', 'DetailedSkyDiffuseModeling', 'SimpleSkyDiffuseModeling'] | None = Field(default='SimpleSkyDiffuseModeling', json_schema_extra={'note': 'Advanced Feature. Internal default is SimpleSkyDiffuseModeling If you have shading elements that change transmittance over the year, you may wish to choose the detailed method. Refer to InputOutput...'})
    output_external_shading_calculation_results: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes is chosen, the calculated external shading fraction results will be saved to an external CSV file with surface names as the column headers.'})
    disable_self_shading_within_shading_zone_groups: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, self-shading will be disabled from all exterior surfaces in a given Shading Zone Group to surfaces within the same Shading Zone Group. If both Disable Self-Shading Within Shading Zone Group...'})
    disable_self_shading_from_shading_zone_groups_to_other_zones: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, self-shading will be disabled from all exterior surfaces in a given Shading Zone Group to all other zones in the model. If both Disable Self-Shading Within Shading Zone Groups and Disable S...'})
    shading_zone_groups: list[ShadowCalculationShadingZoneGroupsItem] | None = Field(default=None)


class SimulationControl(IDFBaseModel):
    """Note that the following 3 fields are related to the Sizing:Zone,
Sizing:System, and Sizing:Plant objects. Having these fields set to Yes but
no corresponding Sizing object will not cause the sizing to be done.
However, having any of these fields set to No, the corresponding Sizing
object is ignored. Note also, if you want to do system sizing, you must also
do zone sizing in the same run or an error will result."""

    _idf_object_type: ClassVar[str] = "SimulationControl"
    do_zone_sizing_calculation: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, Zone sizing is accomplished from corresponding Sizing:Zone objects and autosize fields.'})
    do_system_sizing_calculation: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, System sizing is accomplished from corresponding Sizing:System objects and autosize fields. If Yes, Zone sizing (previous field) must also be Yes.'})
    do_plant_sizing_calculation: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, Plant sizing is accomplished from corresponding Sizing:Plant objects and autosize fields.'})
    run_simulation_for_sizing_periods: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'If Yes, SizingPeriod:* objects are executed and results from those may be displayed..'})
    run_simulation_for_weather_file_run_periods: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'If Yes, RunPeriod:* objects are executed and results from those may be displayed..'})
    do_hvac_sizing_simulation_for_sizing_periods: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, SizingPeriod:* objects are executed additional times for advanced sizing. Currently limited to use with coincident plant sizing, see Sizing:Plant object'})
    maximum_number_of_hvac_sizing_simulation_passes: int | None = Field(default=1, ge=1, json_schema_extra={'note': 'the entire set of SizingPeriod:* objects may be repeated to fine tune size results this input sets a limit on the number of passes that the sizing algorithms can repeat the set'})


class SurfaceConvectionAlgorithmInside(IDFBaseModel):
    """Default indoor surface heat transfer convection algorithm to be used for all
zones"""

    _idf_object_type: ClassVar[str] = "SurfaceConvectionAlgorithm:Inside"
    algorithm: Literal['', 'ASTMC1340', 'AdaptiveConvectionAlgorithm', 'CeilingDiffuser', 'Simple', 'TARP'] | None = Field(default='TARP', json_schema_extra={'note': 'Simple = constant value natural convection (ASHRAE) TARP = variable natural convection based on temperature difference (ASHRAE, Walton) CeilingDiffuser = ACH-based forced and mixed convection corre...'})


class SurfaceConvectionAlgorithmOutside(IDFBaseModel):
    """Default outside surface heat transfer convection algorithm to be used for
all zones"""

    _idf_object_type: ClassVar[str] = "SurfaceConvectionAlgorithm:Outside"
    algorithm: Literal['', 'AdaptiveConvectionAlgorithm', 'DOE-2', 'MoWiTT', 'SimpleCombined', 'TARP'] | None = Field(default='DOE-2', json_schema_extra={'note': 'SimpleCombined = Combined radiation and convection coefficient using simple ASHRAE model TARP = correlation from models developed by ASHRAE, Walton, and Sparrow et. al. MoWiTT = correlation from me...'})


class Timestep(IDFBaseModel):
    """Specifies the \"basic\" timestep for the simulation. The value entered here
is also known as the Zone Timestep. This is used in the Zone Heat Balance
Model calculation as the driving timestep for heat transfer and load
calculations."""

    _idf_object_type: ClassVar[str] = "Timestep"
    number_of_timesteps_per_hour: int | None = Field(default=6, ge=1, le=60, json_schema_extra={'note': 'Number in hour: normal validity 4 to 60: 6 suggested Must be evenly divisible into 60 Allowable values include 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60 Normal 6 is minimum as lower values may c...'})


class Version(IDFBaseModel):
    """Specifies the EnergyPlus version of the IDF file."""

    _idf_object_type: ClassVar[str] = "Version"
    version_identifier: str | None = Field(default='25.1')


class ZoneAirContaminantBalance(IDFBaseModel):
    """Determines which contaminant concentration will be simulates."""

    _idf_object_type: ClassVar[str] = "ZoneAirContaminantBalance"
    carbon_dioxide_concentration: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, CO2 simulation will be performed.'})
    outdoor_carbon_dioxide_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values should be in parts per million (ppm)'})
    generic_contaminant_concentration: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, generic contaminant simulation will be performed.'})
    outdoor_generic_contaminant_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values should be generic contaminant concentration in parts per million (ppm)'})


class ZoneAirHeatBalanceAlgorithm(IDFBaseModel):
    """Controls the zone/space air heat balance."""

    _idf_object_type: ClassVar[str] = "ZoneAirHeatBalanceAlgorithm"
    algorithm: Literal['', 'AnalyticalSolution', 'EulerMethod', 'ThirdOrderBackwardDifference'] | None = Field(default='ThirdOrderBackwardDifference', json_schema_extra={'note': 'Determines which algorithm will be used to solve the air heat balance.'})
    do_space_heat_balance_for_sizing: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If yes, space heat balance will be calculated and reported during sizing.'})
    do_space_heat_balance_for_simulation: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If yes, space heat balance will be calculated and reported during simulation.'})


class ZoneAirMassFlowConservation(IDFBaseModel):
    """Enforces the zone air mass flow balance by either adjusting zone mixing
object flow only, adjusting zone total return flow only, zone mixing and the
zone total return flows, or adjusting the zone total return and zone mixing
object flows. Zone infiltration flow air flow is increased or decreased
depending user selection in the infiltration treatment method. If either of
zone mixing or zone return flow adjusting methods or infiltration is active,
then the zone air mass flow balance calculation will attempt to enforce
conservation of mass for each zone. If flow balancing method is \"None\" and
infiltration is \"None\", then the zone air mass flow calculation defaults
to assume self-balanced simple flow mixing and infiltration objects."""

    _idf_object_type: ClassVar[str] = "ZoneAirMassFlowConservation"
    adjust_zone_mixing_and_return_for_air_mass_flow_balance: Literal['', 'AdjustMixingOnly', 'AdjustMixingThenReturn', 'AdjustReturnOnly', 'AdjustReturnThenMixing', 'None'] | None = Field(default='None', json_schema_extra={'note': 'If "AdjustMixingOnly", zone mixing object flow rates are adjusted to balance the zone air mass flow and zone infiltration air flow may be increased or decreased if required in order to balance the ...'})
    infiltration_balancing_method: Literal['', 'AddInfiltrationFlow', 'AdjustInfiltrationFlow', 'None'] | None = Field(default='AddInfiltrationFlow', json_schema_extra={'note': 'This input field allows user to choose how zone infiltration flow is treated during the zone air mass flow balance calculation. AddInfiltrationFlow may add infiltration to the base flow specified i...'})
    infiltration_balancing_zones: Literal['', 'AllZones', 'MixingSourceZonesOnly'] | None = Field(default='MixingSourceZonesOnly', json_schema_extra={'note': 'This input field allows user to choose which zones are included in infiltration balancing. MixingSourceZonesOnly allows infiltration balancing only in zones which as source zones for mixing which a...'})


class ZoneCapacitanceMultiplierResearchSpecial(IDFBaseModel):
    """Multiplier altering the relative capacitance of the air compared to an empty
zone"""

    _idf_object_type: ClassVar[str] = "ZoneCapacitanceMultiplier:ResearchSpecial"
    name: str = Field(...)
    zone_or_zonelist_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames'], 'note': 'If this field is left blank, the multipliers are applied to all the zones not specified'})
    temperature_capacity_multiplier: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Used to alter the capacitance of zone air with respect to heat or temperature'})
    humidity_capacity_multiplier: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Used to alter the capacitance of zone air with respect to moisture or humidity ratio'})
    carbon_dioxide_capacity_multiplier: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Used to alter the capacitance of zone air with respect to zone air carbon dioxide concentration'})
    generic_contaminant_capacity_multiplier: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Used to alter the capacitance of zone air with respect to zone air generic contaminant concentration'})

