"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Zone HVAC Controls and Thermostats
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ControlTypeNamesRef,
    PeopleNamesRef,
    ScheduleNamesRef,
    ThermalComfortControlTypeNamesRef,
    ZoneAndZoneListNamesRef,
    ZoneControlThermostaticNamesRef,
    ZoneNamesRef,
)


class ThermostatSetpointDualSetpoint(IDFBaseModel):
    """Used for a heating and cooling thermostat with dual setpoints. The setpoints
    can be scheduled and varied throughout the simulation for both heating and
    cooling."""

    _idf_object_type: ClassVar[str] = 'ThermostatSetpoint:DualSetpoint'
    name: str = Field(...)
    heating_setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cooling_setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class ThermostatSetpointSingleCooling(IDFBaseModel):
    """Used for a cooling only thermostat. The setpoint can be scheduled and varied
    throughout the simulation but only cooling is allowed."""

    _idf_object_type: ClassVar[str] = 'ThermostatSetpoint:SingleCooling'
    name: str = Field(...)
    setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class ThermostatSetpointSingleHeating(IDFBaseModel):
    """Used for a heating only thermostat. The setpoint can be scheduled and varied
    throughout the simulation but only heating is allowed with this control
    type."""

    _idf_object_type: ClassVar[str] = 'ThermostatSetpoint:SingleHeating'
    name: str = Field(...)
    setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class ThermostatSetpointSingleHeatingOrCooling(IDFBaseModel):
    """Used for a heating and cooling thermostat with a single setpoint. The
    setpoint can be scheduled and varied throughout the simulation for both
    heating and cooling."""

    _idf_object_type: ClassVar[str] = 'ThermostatSetpoint:SingleHeatingOrCooling'
    name: str = Field(...)
    setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class ThermostatSetpointThermalComfortFangerDualSetpoint(IDFBaseModel):
    """Used for heating and cooling thermal comfort control with dual setpoints.
    The PMV setpoints can be scheduled and varied throughout the simulation for
    both heating and cooling."""

    _idf_object_type: ClassVar[str] = (
        'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint'
    )
    name: str = Field(...)
    fanger_thermal_comfort_heating_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be Predicted Mean Vote (PMV)',
        },
    )
    fanger_thermal_comfort_cooling_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be Predicted Mean Vote (PMV)',
        },
    )


class ThermostatSetpointThermalComfortFangerSingleCooling(IDFBaseModel):
    """Used for cooling only thermal comfort control. The PMV setpoint can be
    scheduled and varied throughout the simulation but only cooling is allowed
    with this control type."""

    _idf_object_type: ClassVar[str] = (
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling'
    )
    name: str = Field(...)
    fanger_thermal_comfort_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be Predicted Mean Vote (PMV)',
        },
    )


class ThermostatSetpointThermalComfortFangerSingleHeating(IDFBaseModel):
    """Used for heating only thermal comfort control. The PMV setpoint can be
    scheduled and varied throughout the simulation but only heating is allowed
    with this control type."""

    _idf_object_type: ClassVar[str] = (
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating'
    )
    name: str = Field(...)
    fanger_thermal_comfort_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be Predicted Mean Vote (PMV)',
        },
    )


class ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling(IDFBaseModel):
    """Used for heating and cooling thermal comfort control with a single setpoint.
    The PMV setpoint can be scheduled and varied throughout the simulation for
    both heating and cooling."""

    _idf_object_type: ClassVar[str] = (
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling'
    )
    name: str = Field(...)
    fanger_thermal_comfort_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be Predicted Mean Vote (PMV)',
        },
    )


class ZoneControlContaminantController(IDFBaseModel):
    """Used to control a zone to a specified indoor level of CO2 or generic
    contaminants, or to specify minimum CO2 concentration schedule name for a
    zone."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:ContaminantController'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    carbon_dioxide_control_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for CO2 controller. Schedule value > 0 means the CO2 controller is enabled. If this field is blank, then CO2 controller is always enabled.',
        },
    )
    carbon_dioxide_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be carbon dioxide concentration in parts per million (ppm)',
        },
    )
    minimum_carbon_dioxide_concentration_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be carbon dioxide concentration in parts per million (ppm) This field is used when the field System Outdoor Air Method = ProportionalControlBasedOnOccupancySchedule or Propor...',
        },
    )
    maximum_carbon_dioxide_concentration_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be carbon dioxide concentration in parts per million (ppm) This field is used when the field System Outdoor Air Method = ProportionalControlBasedOnOccupancySchedule or Propor...',
        },
    )
    generic_contaminant_control_availability_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Availability schedule name for generic contaminant controller. Schedule value > 0 means the generic contaminant controller is enabled. If this field is blank, then generic contaminant controller is...',
            },
        )
    )
    generic_contaminant_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be generic contaminant concentration in parts per million (ppm) This field is used when the field System Outdoor Air Method = IndoorAirQualityProcedureGenericContaminant in C...',
        },
    )


class ZoneControlHumidistat(IDFBaseModel):
    """Specifies zone relative humidity setpoint schedules for humidifying and
    dehumidifying."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Humidistat'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    humidifying_relative_humidity_setpoint_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'hourly schedule values should be in Relative Humidity (percent)',
        },
    )
    dehumidifying_relative_humidity_setpoint_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'hourly schedule values should be in Relative Humidity (percent)',
            },
        )
    )


class ZoneControlThermostat(IDFBaseModel):
    """Define the Thermostat settings for a zone or list of zones. If you use a
    ZoneList in the Zone or ZoneList name field then this definition applies to
    all the zones in the ZoneList."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Thermostat'
    name: str = Field(...)
    zone_or_zonelist_name: ZoneAndZoneListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneAndZoneListNames']}
    )
    control_type_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This schedule contains appropriate control types for thermostat. Control types are integers: 0 - Uncontrolled (floating, no thermostat), 1 = ThermostatSetpoint:SingleHeating, 2 = ThermostatSetpoint...',
        },
    )
    control_1_object_type: Literal[
        'ThermostatSetpoint:DualSetpoint',
        'ThermostatSetpoint:SingleCooling',
        'ThermostatSetpoint:SingleHeating',
        'ThermostatSetpoint:SingleHeatingOrCooling',
    ] = Field(...)
    control_1_name: ControlTypeNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ControlTypeNames'],
            'note': 'Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating) Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    control_2_object_type: (
        Literal[
            'ThermostatSetpoint:DualSetpoint',
            'ThermostatSetpoint:SingleCooling',
            'ThermostatSetpoint:SingleHeating',
            'ThermostatSetpoint:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    control_2_name: ControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControlTypeNames'],
            'note': 'Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating) Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    control_3_object_type: (
        Literal[
            'ThermostatSetpoint:DualSetpoint',
            'ThermostatSetpoint:SingleCooling',
            'ThermostatSetpoint:SingleHeating',
            'ThermostatSetpoint:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    control_3_name: ControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControlTypeNames'],
            'note': 'Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating) Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    control_4_object_type: (
        Literal[
            'ThermostatSetpoint:DualSetpoint',
            'ThermostatSetpoint:SingleCooling',
            'ThermostatSetpoint:SingleHeating',
            'ThermostatSetpoint:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    control_4_name: ControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControlTypeNames'],
            'note': 'Control names are names of individual control objects (e.g. ThermostatSetpoint:SingleHeating) Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    temperature_difference_between_cutout_and_setpoint: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This optional choice field provides a temperature difference between cut-out temperature and setpoint. The difference is used to adjust to heating or cooling setpoint based on control types.',
        },
    )


class ZoneControlThermostatOperativeTemperature(IDFBaseModel):
    """This object can be used with the ZoneList option on a thermostat or with one
    of the zones on that list (but you won't be able to use the object list to
    pick only one of those zones. Thermostat names are <Zone Name> <global
    Thermostat name> internally."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Thermostat:OperativeTemperature'
    thermostat_name: ZoneControlThermostaticNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneControlThermostaticNames'],
            'note': 'Enter the name of a ZoneControl:Thermostat object. This object modifies a ZoneControl:Thermostat object to add a radiative fraction.',
        },
    )
    radiative_fraction_input_mode: Literal['Constant', 'Scheduled'] = Field(...)
    fixed_radiative_fraction: float | None = Field(default=None, ge=0.0, lt=0.9)
    radiative_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values of 0.0 indicate no operative temperature control',
        },
    )
    adaptive_comfort_model_type: (
        Literal[
            '',
            'AdaptiveASH5580PercentUpperLine',
            'AdaptiveASH5590PercentUpperLine',
            'AdaptiveASH55CentralLine',
            'AdaptiveCEN15251CategoryIIIUpperLine',
            'AdaptiveCEN15251CategoryIIUpperLine',
            'AdaptiveCEN15251CategoryIUpperLine',
            'AdaptiveCEN15251CentralLine',
            'None',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'the cooling setpoint temperature schedule of the referenced thermostat will be adjusted based on the selected adaptive comfort model type'
        },
    )


class ZoneControlThermostatStagedDualSetpoint(IDFBaseModel):
    """Define the Thermostat StagedDualSetpoint settings for a zone or list of
    zones. If you use a ZoneList in the Zone or ZoneList name field then this
    definition applies to all the zones in the ZoneList."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Thermostat:StagedDualSetpoint'
    name: str = Field(...)
    zone_or_zonelist_name: ZoneAndZoneListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneAndZoneListNames']}
    )
    number_of_heating_stages: int = Field(
        ...,
        ge=1,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for heating temperature offset'
        },
    )
    heating_temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    heating_throttling_temperature_range: float | None = Field(
        default=1.1, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    stage_1_heating_temperature_offset: float = Field(
        ...,
        le=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The heating temperature offset is used to determine heating stage number for multi stage equipment. When the temperature difference of the heating setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_2_heating_temperature_offset: float | None = Field(
        default=None,
        le=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The heating temperature offset is used to determine heating stage number for multi stage equipment. When the temperature difference of the heating setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_3_heating_temperature_offset: float | None = Field(
        default=None,
        le=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The heating temperature offset is used to determine heating stage number for multi stage equipment. When the temperature difference of the heating setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_4_heating_temperature_offset: float | None = Field(
        default=None,
        le=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The heating temperature offset is used to determine heating stage number for multi stage equipment. When the temperature difference of the heating setpoint and the controlled zone temperature at pr...',
        },
    )
    number_of_cooling_stages: int = Field(
        ...,
        ge=1,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for cooling temperature offset'
        },
    )
    cooling_temperature_setpoint_base_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cooling_throttling_temperature_range: float | None = Field(
        default=1.1, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    stage_1_cooling_temperature_offset: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The cooling temperature offset is used to determine cooling stage number for multi stage equipment. When the temperature difference of the cooling setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_2_cooling_temperature_offset: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The cooling temperature offset is used to determine cooling stage number for multi stage equipment. When the temperature difference of the cooling setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_3_cooling_temperature_offset: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The cooling temperature offset is used to determine cooling stage number for multi stage equipment. When the temperature difference of the cooling setpoint and the controlled zone temperature at pr...',
        },
    )
    stage_4_cooling_temperature_offset: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The cooling temperature offset is used to determine cooling stage number for multi stage equipment. When the temperature difference of the cooling setpoint and the controlled zone temperature at pr...',
        },
    )


class ZoneControlThermostatTemperatureAndHumidity(IDFBaseModel):
    """This object modifies a ZoneControl:Thermostat object to effect temperature
    control based on zone air humidity conditions."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Thermostat:TemperatureAndHumidity'
    thermostat_name: ZoneControlThermostaticNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneControlThermostaticNames'],
            'note': 'Enter the name of a ZoneControl:Thermostat object whose operation is to be modified to effect temperature control based on zone air humidity conditions. If the ZoneControl: Thermostat object refere...',
        },
    )
    dehumidifying_relative_humidity_setpoint_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be in Relative Humidity (percent)',
        },
    )
    dehumidification_control_type: Literal['', 'None', 'Overcool'] | None = Field(
        default='Overcool'
    )
    overcool_range_input_method: Literal['', 'Constant', 'Scheduled'] | None = Field(
        default='Constant'
    )
    overcool_constant_range: float | None = Field(
        default=1.7,
        ge=0.0,
        le=3.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Maximum Overcool temperature range for cooling setpoint reduction. Used with Dehumidification Control Type = Overcool. A value of 0.0 indicates no zone temperature overcooling will be provided to g...',
        },
    )
    overcool_range_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values of 0.0 indicates no zone temperature overcooling will be provided to gain additional dehumidification. Schedule values should be >= 0 and <= 3 (deltaC).',
        },
    )
    overcool_control_ratio: float | None = Field(
        default=3.6,
        ge=0.0,
        json_schema_extra={
            'units': 'percent/K',
            'note': 'The value of this input field is used to adjust the cooling setpoint temperature (established by the associated ZoneControl:Thermostat object) downward based on the difference between the zone air ...',
        },
    )


class ZoneControlThermostatThermalComfort(IDFBaseModel):
    """If you use a ZoneList in the Zone or ZoneList name field then this
    definition applies to all the zones in the ZoneList."""

    _idf_object_type: ClassVar[str] = 'ZoneControl:Thermostat:ThermalComfort'
    name: str = Field(...)
    zone_or_zonelist_name: ZoneAndZoneListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneAndZoneListNames']}
    )
    averaging_method: (
        Literal['', 'ObjectAverage', 'PeopleAverage', 'SpecificObject'] | None
    ) = Field(
        default='PeopleAverage',
        json_schema_extra={
            'note': 'The method used to calculate thermal comfort dry-bulb temperature setpoint for multiple people objects in a zone'
        },
    )
    specific_people_name: PeopleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PeopleNames'],
            'note': 'Used only when Averaging Method = SpecificObject in the previous field.',
        },
    )
    minimum_dry_bulb_temperature_setpoint: float | None = Field(
        default=0.0, ge=0.0, le=50.0, json_schema_extra={'units': 'C'}
    )
    maximum_dry_bulb_temperature_setpoint: float | None = Field(
        default=50.0, ge=0.0, le=50.0, json_schema_extra={'units': 'C'}
    )
    thermal_comfort_control_type_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The Thermal Comfort Control Type Schedule contains values that are appropriate control types. Thermal Comfort Control types are integers: 0 - Uncontrolled (floating), 1 = ThermostatSetpoint:Thermal...',
        },
    )
    thermal_comfort_control_1_object_type: Literal[
        'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
        'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
    ] = Field(...)
    thermal_comfort_control_1_name: ThermalComfortControlTypeNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ThermalComfortControlTypeNames'],
            'note': 'Control type names are names for individual control type objects. Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    thermal_comfort_control_2_object_type: (
        Literal[
            'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    thermal_comfort_control_2_name: ThermalComfortControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ThermalComfortControlTypeNames'],
            'note': 'Control Type names are names for individual control type objects. Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    thermal_comfort_control_3_object_type: (
        Literal[
            'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    thermal_comfort_control_3_name: ThermalComfortControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ThermalComfortControlTypeNames'],
            'note': 'Control type names are names for individual control type objects. Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
    thermal_comfort_control_4_object_type: (
        Literal[
            'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
        ]
        | None
    ) = Field(default=None)
    thermal_comfort_control_4_name: ThermalComfortControlTypeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ThermalComfortControlTypeNames'],
            'note': 'Control type names are names for individual control type objects. Schedule values in these objects list actual setpoint temperatures for the control types',
        },
    )
