"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Zone Airflow
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    EarthTubeParameterNamesRef,
    ScheduleNamesRef,
    SpaceAndSpaceListNamesRef,
    SpaceNamesRef,
    WaterStorageTankNamesRef,
    ZoneAndZoneListNamesRef,
    ZoneNamesRef,
)



class ZoneAirBalanceOutdoorAir(IDFBaseModel):
    """Provide a combined zone outdoor air flow by including interactions between
mechanical ventilation, infiltration and duct leakage. This object will
combine outdoor flows from all ZoneInfiltration and ZoneVentilation objects
in the same zone. Balanced flows will be summed, while unbalanced flows will
be added in quadrature."""

    _idf_object_type: ClassVar[str] = "ZoneAirBalance:OutdoorAir"
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    air_balance_method: Literal['', 'None', 'Quadrature'] | None = Field(default='Quadrature', json_schema_extra={'note': 'None: Only perform simple calculations without using a combined zone outdoor air. Quadrature: A combined outdoor air is used in the quadrature sum.'})
    induced_outdoor_air_due_to_unbalanced_duct_leakage: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s'})
    induced_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the fraction values applied to the Induced Outdoor Air given in the previous input field (0.0 - 1.0).'})


class ZoneCoolTowerShower(IDFBaseModel):
    """A cooltower (sometimes referred to as a wind tower or a shower cooling
tower) models passive downdraught evaporative cooling (PDEC) that is
designed to capture the wind at the top of a tower and cool the outdoor air
using water evaporation before delivering it to a zone (or space)."""

    _idf_object_type: ClassVar[str] = "ZoneCoolTower:Shower"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'In case of stand alone tank or underground water, leave this input blank'})
    flow_control_type: Literal['', 'WaterFlowSchedule', 'WindDrivenFlow'] | None = Field(default='WindDrivenFlow', json_schema_extra={'note': 'Water flow schedule should be selected when the water flow rate is known. Wind-driven flow should be selected when the water flow rate is unknown.'})
    pump_flow_rate_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    maximum_water_flow_rate: float = Field(..., json_schema_extra={'units': 'm3/s'})
    effective_tower_height: float = Field(..., json_schema_extra={'units': 'm', 'note': 'This field is from either the spray or the wet pad to the top of the outlet.'})
    airflow_outlet_area: float = Field(..., json_schema_extra={'units': 'm2', 'note': 'User have to specify effective area when outlet area is relatively bigger than the cross sectional area of cooltower. If the number of outlet is more than one, assume the air passes through only one.'})
    maximum_air_flow_rate: float = Field(..., ge=0.0, json_schema_extra={'units': 'm3/s'})
    minimum_indoor_temperature: float = Field(..., ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'This field is to specify the indoor temperature below which cooltower is shutoff.'})
    fraction_of_water_loss: float | None = Field(default=None, ge=0.0, le=1.0)
    fraction_of_flow_schedule: float | None = Field(default=None, ge=0.0, le=1.0)
    rated_power_consumption: float = Field(..., json_schema_extra={'units': 'W'})


class ZoneCrossMixing(IDFBaseModel):
    """ZoneCrossMixing exchanges an equal amount of air between two zones or
spaces. Note that this statement affects the energy balance of both zones or
spaces."""

    _idf_object_type: ClassVar[str] = "ZoneCrossMixing"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'ZoneList and SpaceList names are not allowed.'})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    design_flow_rate_calculation_method: Literal['', 'AirChanges/Hour', 'Flow/Area', 'Flow/Person', 'Flow/Zone'] | None = Field(default='Flow/Zone', json_schema_extra={'note': 'The entered calculation method is used to create the maximum amount of ventilation for this set of attributes Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate Flow/Area => Fl...'})
    design_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    flow_rate_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-m2'})
    flow_rate_per_person: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-person'})
    air_changes_per_hour: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': '1/hr'})
    source_zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    delta_temperature: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC', 'note': 'This field contains the constant temperature differential between source and receiving zone or space below which mixing is shutoff. If a source zone is specified and it contains more than one space...'})
    delta_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the temperature differential between source and receiving zone or space below which mixing is shutoff. If a source zone is specified and it contains more than one space, the ...'})
    minimum_receiving_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the receiving zone or space temperature versus time below which cross mixing is shutoff.'})
    maximum_receiving_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the receiving zone or space  temperature versus time above which cross mixing is shutoff.'})
    minimum_source_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the source zone or space  temperature versus time below which cross mixing is shutoff.'})
    maximum_source_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the source zone or space  temperature versus time above which cross mixing is shutoff.'})
    minimum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time below which cross mixing is shutoff.'})
    maximum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time above which cross mixing is shutoff.'})


class ZoneEarthtube(IDFBaseModel):
    """Earth Tube is specified as a design level which is modified by a Schedule
fraction, temperature difference and wind speed: Earthtube=Edesign *
Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2)"""

    _idf_object_type: ClassVar[str] = "ZoneEarthtube"
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    design_flow_rate: float = Field(..., ge=0.0, json_schema_extra={'units': 'm3/s', 'note': '"Edesign" in Equation'})
    minimum_zone_temperature_when_cooling: float = Field(..., ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the indoor temperature below which the earth tube is shut off'})
    maximum_zone_temperature_when_heating: float = Field(..., ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the indoor temperature above which the earth tube is shut off'})
    delta_temperature: float = Field(..., ge=0.0, json_schema_extra={'units': 'deltaC', 'note': 'This is the temperature difference between indoor and outdoor below which the earth tube is shut off'})
    earthtube_type: Literal['', 'Exhaust', 'Intake', 'Natural'] | None = Field(default='Natural')
    fan_pressure_rise: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'Pa', 'note': 'pressure rise across the fan'})
    fan_total_efficiency: float | None = Field(default=1.0, gt=0.0)
    pipe_radius: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_thickness: float | None = Field(default=0.2, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_length: float | None = Field(default=15.0, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_thermal_conductivity: float | None = Field(default=200.0, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    pipe_depth_under_ground_surface: float | None = Field(default=3.0, gt=0.0, json_schema_extra={'units': 'm'})
    soil_condition: Literal['', 'HeavyAndDamp', 'HeavyAndDry', 'HeavyAndSaturated', 'LightAndDry'] | None = Field(default='HeavyAndDamp')
    average_soil_surface_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    amplitude_of_soil_surface_temperature: float = Field(..., ge=0.0, json_schema_extra={'units': 'deltaC'})
    phase_constant_of_soil_surface_temperature: float = Field(..., ge=0.0, json_schema_extra={'units': 'days'})
    constant_term_flow_coefficient: float | None = Field(default=1.0, json_schema_extra={'note': '"A" in Equation'})
    temperature_term_flow_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"B" in Equation'})
    velocity_term_flow_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"C" in Equation'})
    velocity_squared_term_flow_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"D" in Equation'})
    earth_tube_model_type: Literal['', 'Basic', 'Vertical'] | None = Field(default='Basic')
    earth_tube_model_parameters: EarthTubeParameterNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['EarthTubeParameterNames']})


class ZoneEarthtubeParameters(IDFBaseModel):
    """Parameters that apply to the vertical model for an earth tube"""

    _idf_object_type: ClassVar[str] = "ZoneEarthtube:Parameters"
    earth_tube_model_parameters_name: str = Field(...)
    nodes_above_earth_tube: int | None = Field(default=5, ge=3, le=10, json_schema_extra={'units': 'dimensionless'})
    nodes_below_earth_tube: int | None = Field(default=3, ge=3, le=10, json_schema_extra={'units': 'dimensionless'})
    earth_tube_dimensionless_boundary_above: float | None = Field(default=1.0, ge=0.25, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'When set to 1.0, the total thickness of the solution space above the earth tube node is equal to the maximum vertical dimension above the earth tube.'})
    earth_tube_dimensionless_boundary_below: float | None = Field(default=0.25, ge=0.25, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'When set to 1.0, the total thickness of the solution space below the earth tube node is equal to the maximum vertical dimension above the earth tube.'})
    earth_tube_solution_space_width: float | None = Field(default=4.0, ge=3.0, le=20.0, json_schema_extra={'units': 'dimensionless', 'note': 'Width of the nodes in the direction parallel to the ground, multiplied by earth tube radius'})


class ZoneInfiltrationDesignFlowRate(IDFBaseModel):
    """Infiltration is specified as a design level which is modified by a Schedule
fraction, temperature difference and wind speed: Infiltration=Idesign *
FSchedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2) If a
ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
then this definition applies to all applicable spaces, and each instance
will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = "ZoneInfiltration:DesignFlowRate"
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    design_flow_rate_calculation_method: Literal['', 'AirChanges/Hour', 'Flow/Area', 'Flow/ExteriorArea', 'Flow/ExteriorWallArea', 'Flow/Zone'] | None = Field(default='Flow/Zone', json_schema_extra={'note': 'The entered calculation method is used to create the maximum amount of infiltration for this set of attributes Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate Flow/Area => F...'})
    design_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    flow_rate_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-m2'})
    flow_rate_per_exterior_surface_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-m2', 'note': 'use key Flow/ExteriorArea for all exterior surface area use key Flow/ExteriorWallArea to include only exterior wall area'})
    air_changes_per_hour: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': '1/hr'})
    constant_term_coefficient: float | None = Field(default=1.0, json_schema_extra={'note': '"A" in Equation'})
    temperature_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"B" in Equation'})
    velocity_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"C" in Equation'})
    velocity_squared_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"D" in Equation'})
    density_basis: Literal['', 'Indoor', 'Outdoor', 'Standard'] | None = Field(default='Outdoor', json_schema_extra={'note': 'The air density to use when converting from volume flow to mass flow.'})


class ZoneInfiltrationEffectiveLeakageArea(IDFBaseModel):
    """Infiltration is specified as effective leakage area at 4 Pa, schedule
fraction, stack and wind coefficients, and is a function of temperature
difference and wind speed: Infiltration=FSchedule * (AL /1000)
SQRT(Cs*|(Tzone-Todb)| + Cw*WindSpd**2 ) If a Zone comprised of more than
one Space is specified then this definition applies to all applicable
spaces, and each instance will be named with the Space Name plus this Object
Name."""

    _idf_object_type: ClassVar[str] = "ZoneInfiltration:EffectiveLeakageArea"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'ZoneList and SpaceList names are not allowed.'})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    effective_air_leakage_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'cm2', 'note': '"AL" in Equation units are cm2 (square centimeters)'})
    stack_coefficient: float = Field(..., gt=0.0, json_schema_extra={'note': '"Cs" in Equation'})
    wind_coefficient: float = Field(..., gt=0.0, json_schema_extra={'note': '"Cw" in Equation'})


class ZoneInfiltrationFlowCoefficient(IDFBaseModel):
    """Infiltration is specified as flow coefficient, schedule fraction, stack and
wind coefficients, and is a function of temperature difference and wind
speed: Infiltration=FSchedule * SQRT( (c * Cs*|(Tzone-Todb)|**n)**2 + (c*
Cw*(s * WindSpd)**2n)**2 ) If a Zone comprised of more than one Space is
specified then this definition applies to all applicable spaces, and each
instance will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = "ZoneInfiltration:FlowCoefficient"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'ZoneList and SpaceList names are not allowed.'})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    flow_coefficient: float = Field(..., gt=0.0, json_schema_extra={'note': '"c" in Equation'})
    stack_coefficient: float = Field(..., gt=0.0, json_schema_extra={'note': '"Cs" in Equation'})
    pressure_exponent: float | None = Field(default=0.67, gt=0.0, json_schema_extra={'note': '"n" in Equation'})
    wind_coefficient: float = Field(..., gt=0.0, json_schema_extra={'note': '"Cw" in Equation'})
    shelter_factor: float = Field(..., gt=0.0, json_schema_extra={'note': '"s" in Equation'})


class ZoneMixing(IDFBaseModel):
    """ZoneMixing is a simple air exchange from one zone or space to another. Note
that this statement only affects the energy balance of the \"receiving\"
zone or space and will not produce any effect on the \"source\" zone. Mixing
statements can be complementary and include multiple zones, but the
balancing of flows between zones is left to the user's discretion."""

    _idf_object_type: ClassVar[str] = "ZoneMixing"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'ZoneList and SpaceList names are not allowed.'})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    design_flow_rate_calculation_method: Literal['', 'AirChanges/Hour', 'Flow/Area', 'Flow/Person', 'Flow/Zone'] | None = Field(default='Flow/Zone', json_schema_extra={'note': 'The entered calculation method is used to create the maximum amount of ventilation for this set of attributes Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate Flow/Area => Fl...'})
    design_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    flow_rate_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-m2'})
    flow_rate_per_person: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-person'})
    air_changes_per_hour: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': '1/hr'})
    source_zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    delta_temperature: float | None = Field(default=0.0, json_schema_extra={'units': 'deltaC', 'note': 'This field contains the constant temperature differential between source and receiving zone or space below which mixing is shutoff. If a source zone is specified and it contains more than one space...'})
    delta_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the temperature differential between source and receiving zone or space below which mixing is shutoff. If a source zone is specified and it contains more than one space, the ...'})
    minimum_receiving_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the receiving zone or space temperature versus time below which mixing is shutoff.'})
    maximum_receiving_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the receiving zone or space  temperature versus time above which mixing is shutoff.'})
    minimum_source_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the source zone or space temperature versus time below which mixing is shutoff.'})
    maximum_source_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the source zone or space temperature versus time above which mixing is shutoff.'})
    minimum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time below which mixing is shutoff.'})
    maximum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time above which mixing is shutoff.'})


class ZoneRefrigerationDoorMixing(IDFBaseModel):
    """Refrigeration Door Mixing is used for an opening between two zones (or
spaces) that are at the same elevation but have different air temperatures.
In this case, the mixing air flow between the two zones is determined by the
density difference between the two zones. This would typically be used
between two zones in a refrigerated warehouse that are controlled at
different temperatures. It could also be used to model a door to a walk-in
refrigerated space if that space were modeled as a zone instead of using the
object Refrigeration:WalkIn."""

    _idf_object_type: ClassVar[str] = "ZoneRefrigerationDoorMixing"
    name: str = Field(...)
    zone_or_space_name_1: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'If a space name is used, it must belong to a different zone than Zone or Space Name 2.'})
    zone_or_space_name_2: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'If a space name is used, it must belong to a different zone than Zone or Space Name 1.'})
    schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule defines the fraction of the time the refrigeration door is open For example, if the warehouse is closed at night and there are no door openings between two zones, the value for that t...'})
    door_height: float | None = Field(default=3.0, ge=0.0, le=50.0, json_schema_extra={'units': 'm'})
    door_area: float | None = Field(default=9.0, ge=0.0, le=400.0, json_schema_extra={'units': 'm2'})
    door_protection_type: Literal['', 'AirCurtain', 'None', 'StripCurtain'] | None = Field(default='None', json_schema_extra={'note': 'Door protection can reduce the air flow through a refrigeration door The default value is "None" Choices: "None", "AirCurtain", and "StripCurtain" A strip curtain reduces the air flow more than an ...'})


class ZoneThermalChimney(IDFBaseModel):
    """A thermal chimney is a vertical shaft utilizing solar radiation to enhance
natural ventilation. It consists of an absorber wall, air gap and glass
cover with high solar transmissivity."""

    _idf_object_type: ClassVar[str] = "ZoneThermalChimney"
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Name of zone that is the thermal chimney.'})
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    width_of_the_absorber_wall: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    cross_sectional_area_of_air_channel_outlet: float = Field(..., ge=0.0, json_schema_extra={'units': 'm2'})
    discharge_coefficient: float | None = Field(default=0.8, ge=0.0, le=1.0)
    zone_or_space_name_1: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_1: float | None = Field(default=1.0, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_2: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_2: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_3: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_3: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_4: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_4: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_5: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_5: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_6: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_6: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_7: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_7: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_8: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_8: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_9: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_9: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_10: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_10: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_11: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_11: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_12: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_12: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_13: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_13: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_14: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_14: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_15: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_15: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_16: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_16: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_17: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_17: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_18: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_18: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_19: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_19: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})
    zone_or_space_name_20: (SpaceNamesRef | ZoneNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames']})
    distance_from_top_of_thermal_chimney_to_inlet_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    relative_ratios_of_air_flow_rates_passing_through_inlet_20: float | None = Field(default=None, ge=0.0, le=1.0)
    cross_sectional_areas_of_air_channel_inlet_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2'})


class ZoneVentilationDesignFlowRate(IDFBaseModel):
    """Ventilation is specified as a design level which is modified by a schedule
fraction, temperature difference and wind speed: Ventilation=Vdesign *
Fschedule * (A + B*|(Tzone-Todb)| + C*WindSpd + D * WindSpd**2) If a
ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
then this definition applies to all applicable spaces, and each instance
will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = "ZoneVentilation:DesignFlowRate"
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always 1.0'})
    design_flow_rate_calculation_method: Literal['', 'AirChanges/Hour', 'Flow/Area', 'Flow/Person', 'Flow/Zone'] | None = Field(default='Flow/Zone', json_schema_extra={'note': 'The entered calculation method is used to create the maximum amount of ventilation for this set of attributes Choices: Flow/Zone => Design Flow Rate -- simply enter Design Flow Rate Flow/Area => Fl...'})
    design_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    flow_rate_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-m2'})
    flow_rate_per_person: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s-person'})
    air_changes_per_hour: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': '1/hr'})
    ventilation_type: Literal['', 'Balanced', 'Exhaust', 'Intake', 'Natural'] | None = Field(default='Natural')
    fan_pressure_rise: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'Pa', 'note': 'pressure rise across the fan'})
    fan_total_efficiency: float | None = Field(default=1.0, gt=0.0)
    constant_term_coefficient: float | None = Field(default=1.0, json_schema_extra={'note': '"A" in Equation'})
    temperature_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"B" in Equation'})
    velocity_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"C" in Equation'})
    velocity_squared_term_coefficient: float | None = Field(default=0.0, json_schema_extra={'note': '"D" in Equation'})
    minimum_indoor_temperature: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the indoor temperature below which ventilation is shutoff'})
    minimum_indoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the indoor temperature versus time below which ventilation is shutoff.'})
    maximum_indoor_temperature: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the indoor temperature above which ventilation is shutoff'})
    maximum_indoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the indoor temperature versus time above which ventilation is shutoff.'})
    delta_temperature: float | None = Field(default=-100.0, ge=-100.0, json_schema_extra={'units': 'deltaC', 'note': 'This is the temperature differential between indoor and outdoor below which ventilation is shutoff. If ((IndoorTemp - OutdoorTemp) < DeltaTemperature) then ventilation is not allowed. For example, ...'})
    delta_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the temperature differential between indoor and outdoor versus time below which ventilation is shutoff.'})
    minimum_outdoor_temperature: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor temperature below which ventilation is shutoff'})
    minimum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time below which ventilation is shutoff.'})
    maximum_outdoor_temperature: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor temperature above which ventilation is shutoff'})
    maximum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time above which ventilation is shutoff.'})
    maximum_wind_speed: float | None = Field(default=40.0, ge=0.0, le=40.0, json_schema_extra={'units': 'm/s', 'note': 'this is the outdoor wind speed above which ventilation is shutoff'})
    density_basis: Literal['', 'Indoor', 'Outdoor', 'Standard'] | None = Field(default='Outdoor', json_schema_extra={'note': 'The air density to use when converting from volume flow to mass flow.'})


class ZoneVentilationWindandStackOpenArea(IDFBaseModel):
    """This object is specified as natural ventilation driven by wind and stack
effect only: Ventilation Wind = Cw * Opening Area * Schedule * WindSpd
Ventilation Stack = Cd * Opening Area * Schedule * SQRT(2*g*DH*(|(Tzone-
Todb)|/Tzone)) Total Ventilation = SQRT((Ventilation Wind)^2 + (Ventilation
Stack)^2) If a Zone comprised of more than one Space is specified then this
definition applies to all applicable spaces, and each instance will be named
with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = "ZoneVentilation:WindandStackOpenArea"
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames', 'ZoneNames'], 'note': 'ZoneList and SpaceList names are not allowed.'})
    opening_area: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm2', 'note': 'This is the opening area used to calculate stack effect and wind driven ventilation.'})
    opening_area_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the fraction values applied to the opening area given in the previous input field (0.0 - 1.0). If blank, defaults to always 1.0'})
    opening_effectiveness: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'This field is used to calculate wind driven ventilation. "Cw" in the wind-driven equation and the maximum value is 1.0. When the input is Autocalculate, the program calculates Cw based on an angle ...'})
    effective_angle: float | None = Field(default=0.0, ge=0.0, lt=360.0, json_schema_extra={'units': 'deg', 'note': 'This field is defined as normal angle of the opening area and is used when input field Opening Effectiveness = Autocalculate.'})
    height_difference: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm', 'note': 'This is the height difference between the midpoint of an opening and the neutral pressure level. "DH" in the stack equation.'})
    discharge_coefficient_for_opening: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'This is the discharge coefficient used to calculate stack effect. "Cd" in the stack equation and the maximum value is 1.0. When the input is Autocalculate, the following equation is used to calcula...'})
    minimum_indoor_temperature: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'This is the indoor temperature below which ventilation is shutoff.'})
    minimum_indoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the indoor temperature versus time below which ventilation is shutoff.'})
    maximum_indoor_temperature: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'This is the indoor temperature above which ventilation is shutoff.'})
    maximum_indoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the indoor temperature versus time above which ventilation is shutoff.'})
    delta_temperature: float | None = Field(default=-100.0, ge=-100.0, json_schema_extra={'units': 'deltaC', 'note': 'This is the temperature differential between indoor and outdoor below which ventilation is shutoff.'})
    delta_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the temperature differential between indoor and outdoor versus time below which ventilation is shutoff.'})
    minimum_outdoor_temperature: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'This is the outdoor temperature below which ventilation is shutoff.'})
    minimum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time below which ventilation is shutoff.'})
    maximum_outdoor_temperature: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'This is the outdoor temperature above which ventilation is shutoff.'})
    maximum_outdoor_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule contains the outdoor temperature versus time above which ventilation is shutoff.'})
    maximum_wind_speed: float | None = Field(default=40.0, ge=0.0, le=40.0, json_schema_extra={'units': 'm/s', 'note': 'This is the outdoor wind speed above which ventilation is shutoff.'})

