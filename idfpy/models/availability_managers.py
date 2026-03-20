"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: System Availability Managers
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AirPrimaryLoopsRef,
    HVACTemplateSystemsRef,
    ScheduleNamesRef,
    SystemAvailabilityManagersRef,
    UnivariateFunctionsRef,
    VentilationNamesRef,
    ZoneAndZoneListNamesRef,
    ZoneListNamesRef,
    ZoneNamesRef,
)


class AvailabilityManagerAssignmentListManagersItem(IDFBaseModel):
    """Nested object type for array items."""
    availability_manager_object_type: Literal['AvailabilityManager:DifferentialThermostat', 'AvailabilityManager:HighTemperatureTurnOff', 'AvailabilityManager:HighTemperatureTurnOn', 'AvailabilityManager:LowTemperatureTurnOff', 'AvailabilityManager:LowTemperatureTurnOn', 'AvailabilityManager:NightCycle', 'AvailabilityManager:NightVentilation', 'AvailabilityManager:OptimumStart', 'AvailabilityManager:Scheduled', 'AvailabilityManager:ScheduledOff', 'AvailabilityManager:ScheduledOn'] = Field(...)
    availability_manager_name: SystemAvailabilityManagersRef = Field(..., json_schema_extra={'object_list': ['SystemAvailabilityManagers']})



class AvailabilityManagerAssignmentList(IDFBaseModel):
    """Defines the applicable managers used for an AirLoopHVAC or PlantLoop. The
priority of availability managers is based on a set of rules and are
specific to the type of loop. The output from each availability manager is
an availability status flag: NoAction, ForceOff, CycleOn, or
CycleOnZoneFansOnly (used only for air loops)."""

    _idf_object_type: ClassVar[str] = "AvailabilityManagerAssignmentList"
    name: str = Field(...)
    managers: list[AvailabilityManagerAssignmentListManagersItem] | None = Field(default=None)


class AvailabilityManagerDifferentialThermostat(IDFBaseModel):
    """Overrides fan/pump schedules depending on temperature difference between two
nodes."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:DifferentialThermostat"
    name: str = Field(...)
    hot_node_name: str = Field(...)
    cold_node_name: str = Field(...)
    temperature_difference_on_limit: float = Field(..., json_schema_extra={'units': 'deltaC'})
    temperature_difference_off_limit: float | None = Field(default=None, json_schema_extra={'units': 'deltaC', 'note': 'Defaults to Temperature Difference On Limit.'})


class AvailabilityManagerHighTemperatureTurnOff(IDFBaseModel):
    """Overrides fan/pump schedules depending on temperature at sensor node."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:HighTemperatureTurnOff"
    name: str = Field(...)
    sensor_node_name: str = Field(...)
    temperature: float = Field(..., json_schema_extra={'units': 'C'})


class AvailabilityManagerHighTemperatureTurnOn(IDFBaseModel):
    """Overrides fan/pump schedules depending on temperature at sensor node."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:HighTemperatureTurnOn"
    name: str = Field(...)
    sensor_node_name: str = Field(...)
    temperature: float = Field(..., json_schema_extra={'units': 'C'})


class AvailabilityManagerHybridVentilation(IDFBaseModel):
    """Depending on zone and outdoor conditions overrides window/door opening
controls to maximize natural ventilation and turn off an HVAC system when
ventilation control conditions are met. This object (zone ventilation object
name) has not been instrumented to work with global Zone or Zone List names
option for Ventilation:DesignFlowRate. In order to use, you must enter the
single <Ventilation:DesignFlowRate> name in that field. If it is a part of a
global ventilation assignment the name will be <Zone Name> <global
Ventilation:DesignFlowRate> name. Currently, hybrid ventilation manager is
restricted to one per zone. It can either be applied through the air loop or
directly to the zone. If hybrid ventilation manager is applied to an air
loop and one of the zones served by that air loop also has hybrid
ventilation manager, then zone hybrid ventilation manager is disabled."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:HybridVentilation"
    name: str = Field(...)
    hvac_air_loop_name: (AirPrimaryLoopsRef | HVACTemplateSystemsRef) | None = Field(default=None, json_schema_extra={'object_list': ['AirPrimaryLoops', 'HVACTemplateSystems'], 'note': 'Enter the name of an AirLoopHVAC or HVACTemplate:System:* object. If this field is left blank, hybrid ventilation managers will be simulated for zone equipment control'})
    control_zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'the zone name should be a zone where a thermostat or humidistat is located served by an air primary loop.'})
    ventilation_control_mode_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'The Ventilation control mode contains appropriate integer control types. 0 - uncontrolled (Natural ventilation and HVAC system are controlled by themselves) 1 = Temperature control 2 = Enthalpy con...'})
    use_weather_file_rain_indicators: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'If Yes, ventilation is shutoff when there is rain If No, there is no rain control'})
    maximum_wind_speed: float | None = Field(default=40.0, ge=0.0, le=40.0, json_schema_extra={'units': 'm/s', 'note': 'this is the wind speed above which ventilation is shutoff'})
    minimum_outdoor_temperature: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor temperature below which ventilation is shutoff'})
    maximum_outdoor_temperature: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor temperature above which ventilation is shutoff'})
    minimum_outdoor_enthalpy: float | None = Field(default=None, gt=0.0, lt=300000.0, json_schema_extra={'units': 'J/kg', 'note': 'this is the outdoor Enthalpy below which ventilation is shutoff'})
    maximum_outdoor_enthalpy: float | None = Field(default=None, gt=0.0, lt=300000.0, json_schema_extra={'units': 'J/kg', 'note': 'this is the outdoor Enthalpy above which ventilation is shutoff'})
    minimum_outdoor_dewpoint: float | None = Field(default=-100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor temperature below which ventilation is shutoff Applicable only if Ventilation Control Mode = 3'})
    maximum_outdoor_dewpoint: float | None = Field(default=100.0, ge=-100.0, le=100.0, json_schema_extra={'units': 'C', 'note': 'this is the outdoor dewpoint above which ventilation is shutoff Applicable only if Ventilation Control Mode = 3'})
    minimum_outdoor_ventilation_air_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Used only if Ventilation Control Mode = 4'})
    opening_factor_function_of_wind_speed_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'linear curve = a + b*WS quadratic curve = a + b*WS + c*WS**2 WS = wind speed (m/s)'})
    airflownetwork_control_type_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'The schedule is used to incorporate operation of AirflowNetwork large opening objects and HVAC system operation.'})
    simple_airflow_control_type_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'The schedule is used to incorporate operation of simple airflow objects and HVAC system operation. The simple airflow objects are Ventilation and Mixing only'})
    zoneventilation_object_name: VentilationNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['VentilationNames'], 'note': 'This field has not been instrumented to work with global Zone or Zone List names option for Ventilation:DesignFlowRate. In order to use, you must enter the single <Ventilation:DesignFlowRate> name ...'})
    minimum_hvac_operation_time: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'minutes', 'note': 'Minimum operation time when HVAC system is forced on.'})
    minimum_ventilation_time: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'minutes', 'note': 'Minimum ventilation time when natural ventilation is forced on.'})


class AvailabilityManagerLowTemperatureTurnOff(IDFBaseModel):
    """Overrides fan/pump schedules depending on temperature at sensor node."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:LowTemperatureTurnOff"
    name: str = Field(...)
    sensor_node_name: str = Field(...)
    temperature: float = Field(..., json_schema_extra={'units': 'C'})
    applicability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If blank, defaults to always active'})


class AvailabilityManagerLowTemperatureTurnOn(IDFBaseModel):
    """Overrides fan/pump schedules depending on temperature at sensor node."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:LowTemperatureTurnOn"
    name: str = Field(...)
    sensor_node_name: str = Field(...)
    temperature: float = Field(..., json_schema_extra={'units': 'C'})


class AvailabilityManagerNightCycle(IDFBaseModel):
    """Determines the availability of a loop or system: whether it is on or off.
Depending on zone temperatures, overrides Schedules and forces system Fans
on."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:NightCycle"
    name: str = Field(...)
    applicability_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    fan_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    control_type: Literal['', 'CycleOnAny', 'CycleOnAnyCoolingOrHeatingZone', 'CycleOnAnyCoolingZone', 'CycleOnAnyHeatingZone', 'CycleOnAnyHeatingZoneFansOnly', 'CycleOnAnyZoneFansOnly', 'CycleOnControlZone', 'StayOff'] | None = Field(default='StayOff', json_schema_extra={'note': 'When AvailabilityManager:NightCycle is used in the zone component availability manager assignment list, the key choices for Control Type would only be StayOff and CycleOnControlZone'})
    thermostat_tolerance: float | None = Field(default=1.0, json_schema_extra={'units': 'deltaC'})
    cycling_run_time_control_type: Literal['', 'FixedRunTime', 'Thermostat', 'ThermostatWithMinimumRunTime'] | None = Field(default='FixedRunTime')
    cycling_run_time: float | None = Field(default=3600.0, json_schema_extra={'units': 's'})
    control_zone_or_zone_list_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames'], 'note': 'When AvailabilityManager:NightCycle is used in the zone component availability manager assignment list, the Control Zone Name should be the name of the zone in which the zone component is.'})
    cooling_control_zone_or_zone_list_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames']})
    heating_control_zone_or_zone_list_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames']})
    heating_zone_fans_only_zone_or_zone_list_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames']})


class AvailabilityManagerNightVentilation(IDFBaseModel):
    """depending on zone and outdoor conditions overrides fan schedule to do
precooling with outdoor air"""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:NightVentilation"
    name: str = Field(...)
    applicability_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    fan_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    ventilation_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'One zone temperature must be above this scheduled temperature for night ventilation to be enabled'})
    ventilation_temperature_difference: float | None = Field(default=2.0, json_schema_extra={'units': 'deltaC', 'note': 'The outdoor air temperature minus the control zone temperature must be greater than the ventilation delta T'})
    ventilation_temperature_low_limit: float | None = Field(default=15.0, json_schema_extra={'units': 'C', 'note': 'Night ventilation is disabled if any conditioned zone served by the system falls below this temperature'})
    night_venting_flow_fraction: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'the fraction (could be > 1) of the design system Flow Rate at which night ventilation will be done'})
    control_zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'When AvailabilityManager:NightVentilation is used in the zone component availability manager assignment list, the Control Zone Name should be the name of the zone in which the zone component is.'})


class AvailabilityManagerOptimumStart(IDFBaseModel):
    """Determines the optimal start of HVAC systems before occupancy."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:OptimumStart"
    name: str = Field(...)
    applicability_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    fan_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    control_type: Literal['', 'ControlZone', 'MaximumofZoneList', 'StayOff'] | None = Field(default='ControlZone')
    control_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames']})
    zone_list_name: ZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneListNames']})
    maximum_value_for_optimum_start_time: float | None = Field(default=6.0, json_schema_extra={'units': 'hr', 'note': 'this is the maximum number of hours that a system can start before occupancy'})
    control_algorithm: Literal['', 'AdaptiveASHRAE', 'AdaptiveTemperatureGradient', 'ConstantStartTime', 'ConstantTemperatureGradient'] | None = Field(default='AdaptiveASHRAE')
    constant_temperature_gradient_during_cooling: float | None = Field(default=None, json_schema_extra={'units': 'deltaC/hr'})
    constant_temperature_gradient_during_heating: float | None = Field(default=None, json_schema_extra={'units': 'deltaC/hr'})
    initial_temperature_gradient_during_cooling: float | None = Field(default=None, json_schema_extra={'units': 'deltaC/hr'})
    initial_temperature_gradient_during_heating: float | None = Field(default=None, json_schema_extra={'units': 'deltaC/hr'})
    constant_start_time: float | None = Field(default=None, json_schema_extra={'units': 'hr', 'note': 'this is the number of hours before occupancy for a system'})
    number_of_previous_days: int | None = Field(default=2, ge=2, le=5, json_schema_extra={'units': 'days', 'note': 'this is the number of days that their actual temperature gradients will be used in the AdaptiveTemperatureGradient method'})


class AvailabilityManagerScheduled(IDFBaseModel):
    """Determines the availability of a loop or system: whether it is on or off.
Schedule overrides fan/pump schedule."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:Scheduled"
    name: str = Field(...)
    schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})


class AvailabilityManagerScheduledOff(IDFBaseModel):
    """Determines the availability of a loop or system: only controls the turn off
action. Schedule overrides fan/pump schedule."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:ScheduledOff"
    name: str = Field(...)
    schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})


class AvailabilityManagerScheduledOn(IDFBaseModel):
    """Determines the availability of a loop or system: only controls the turn on
action. Schedule overrides fan/pump schedule."""

    _idf_object_type: ClassVar[str] = "AvailabilityManager:ScheduledOn"
    name: str = Field(...)
    schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})

