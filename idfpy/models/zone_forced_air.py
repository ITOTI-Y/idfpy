"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Zone HVAC Forced Air Units
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    CoilCoolingDXRef,
    ControllerStandAloneEnergyRecoveryVentilatorRef,
    CoolingCoilsDXSingleSpeedRef,
    CoolingCoilsDXVariableSpeedRef,
    CoolingCoilsDXVarRefrigFlowFluidTemperatureControlRef,
    CoolingCoilsDXVarRefrigFlowRef,
    CoolingCoilsWaterRef,
    CoolingCoilsWaterToAirHPRef,
    CoolingCoilsWaterToAirVSHPRef,
    DesignSpecificationOutdoorAirNamesRef,
    DesignSpecificationZoneHVACSizingNameRef,
    DSOASpaceListNamesRef,
    EvapCoolerNamesRef,
    FansCVandOnOffandVAVRef,
    FansCVandOnOffRef,
    FansCVandVAVRef,
    FansOnOffRef,
    FansRef,
    FansSystemModelRef,
    HeatingCoilNameRef,
    HeatingCoilsDXSingleSpeedRef,
    HeatingCoilsDXVariableSpeedRef,
    HeatingCoilsDXVarRefrigFlowFluidTemperatureControlRef,
    HeatingCoilsDXVarRefrigFlowRef,
    HeatingCoilsElectricRef,
    HeatingCoilsWaterRef,
    HeatingCoilsWaterToAirHPRef,
    HeatingCoilsWaterToAirVSHPRef,
    HXAirToAirSensibleAndLatentNamesRef,
    MultivariateFunctionsRef,
    OutdoorAirMixersRef,
    OutdoorAirUnitEquipmentListsRef,
    ScheduleNamesRef,
    SystemAvailabilityManagerListsRef,
    UnitarySystemPerformanceNamesRef,
    UnivariateFunctionsRef,
    WaterStorageTankNamesRef,
    ZoneNamesRef,
)


class ZoneHVACHybridUnitaryHVACModesItem(IDFBaseModel):
    """Nested object type for array items."""

    mode_name: str | None = Field(
        default=None, json_schema_extra={'note': 'Enter a name for Mode 1.'}
    )
    mode_supply_air_temperature_lookup_table_name: MultivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['MultivariateFunctions'],
                'note': 'Enter the name of the Supply Air Temperature Lookup Table for Mode 1. Units for lookup table values should be in C. If this field is blank, Mode 1 will not be considered for any time step that requ...',
            },
        )
    )
    mode_supply_air_humidity_ratio_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the Supply Air Humidity Ratio Lookup Table for Mode 1. Units for lookup table values should be in kgWater/kgDryAir. If this field is blank, Mode 1 will not be considered for any t...',
        },
    )
    mode_system_electric_power_lookup_table_name: MultivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['MultivariateFunctions'],
                'note': 'Enter the name of the Electric Power Lookup Table for Mode 1. Units for lookup table values should be in W. If this field is blank, Mode 1 does not use electricity',
            },
        )
    )
    mode_supply_fan_electric_power_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the Supply Fan Electric Power Lookup Table for Mode 1. Units for lookup table values should be in W. If this field is blank, Mode 1 does not use electricity for supply fan.',
        },
    )
    mode_external_static_pressure_lookup_table_name: MultivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['MultivariateFunctions'],
                'note': 'Enter the name of the External Static Pressure Lookup Table for Mode 1. Units for lookup table values should be in Pa. If this field is blank, external static pressure will not be reported for Mode 1.',
            },
        )
    )
    mode_system_second_fuel_consumption_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Second Fuel Consumption Lookup Table for Mode 1. Units for lookup table values should be in W. If this field is blank, Mode 1 does not consume a second fuel.',
        },
    )
    mode_system_third_fuel_consumption_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Third Fuel Consumption Lookup Table for Mode 1. Units for lookup table values should be in W. If this field is blank, Mode 1 does not consume a third fuel.',
        },
    )
    mode_system_water_use_lookup_table_name: MultivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Water Use Lookup Table for Mode 1. Units for lookup table values should be in kg/s. If this field is blank, Mode 1 does not consume water.',
        },
    )
    mode_minimum_outdoor_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor air temperature allowed for Mode 1. Mode 1 will not be considered when outdoor air temperature is below the value in this field. If this field is blank, there will be no l...',
        },
    )
    mode_maximum_outdoor_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor air temperature allowed for Mode 1. Mode 1 will not be considered wen outdoor air temperature is above the value in this field. If this field is blank, there will be no up...',
        },
    )
    mode_minimum_outdoor_air_humidity_ratio: float | None = Field(
        default=0.0,
        ge=0.0,
        le=0.1,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Enter the minimum outdoor humidity ratio allowed for Mode 1. Mode 1 will not be considered when outdoor air absolute humidity is below the value in this field. If this field is blank, the lower con...',
        },
    )
    mode_maximum_outdoor_air_humidity_ratio: float | None = Field(
        default=0.1,
        ge=0.0,
        le=0.1,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Enter the maximum outdoor air humidity ratio allowed for Mode 1. Mode 1 will not be considered when outdoor air humidity ratio is above the value in this field. If this field is blank, the upper co...',
        },
    )
    mode_minimum_outdoor_air_relative_humidity: float | None = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Enter the minimum outdoor relative humidity allowed for Mode 1. Mode 1 will not be considered when the outdoor air relative humidity is below the value in this field. If this field is blank, the lo...',
        },
    )
    mode_maximum_outdoor_air_relative_humidity: float | None = Field(
        default=100.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Enter the maximum outdoor air relative humidity allowed for Mode 1. Relative humidity as percent from 0.00 to 100.00. Mode 1 will not be considered when the outdoor air relative humidity is above t...',
        },
    )
    mode_minimum_return_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum return air temperature allowed for Mode 1. Mode 1 will not be considered when the return air temperature is below the value in this field. If this field is blank, there will be no...',
        },
    )
    mode_maximum_return_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum return air temperature allowed for Mode 1. Mode 1 will not be considered when the return air temperature is above the value in this field. If this field is blank, there will be no...',
        },
    )
    mode_minimum_return_air_humidity_ratio: float | None = Field(
        default=0.0,
        ge=0.0,
        le=0.1,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Enter the minimum return air humidity ratio allowed for Mode 1. Mode 1 will not be considered when the return air humidity ratio is below the value in this field. If this field is blank, the lower ...',
        },
    )
    mode_maximum_return_air_humidity_ratio: float | None = Field(
        default=0.1,
        ge=0.0,
        le=0.1,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Enter the maximum return air humidity ratio allowed for Mode 1. Mode 1 will not be considered when the return air humidity ratio is above the value in this field. If this field is blank, the upper ...',
        },
    )
    mode_minimum_return_air_relative_humidity: float | None = Field(
        default=0.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Enter the minimum return air relative humidity allowed for Mode 1. Relative humidity as percent from 0.00 to 100.00. Mode 1 will not be considered when the return air relative humidity is below the...',
        },
    )
    mode_maximum_return_air_relative_humidity: float | None = Field(
        default=100.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Enter the maximum return air relative humidity allowed for Mode 1. Relative humidity as percent from 0.00 to 100.00. Mode 1 will not be considered when the return air relative humidity is above the...',
        },
    )
    mode_minimum_outdoor_air_fraction: float | None = Field(
        default=0.1,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the minimum outdoor air fraction allowed for Mode 1. Outdoor air fractions below this value will not be considered for operation in Mode 1. If this field is blank, the lower constraint on out...'
        },
    )
    mode_maximum_outdoor_air_fraction: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the maximum outdoor air fraction allowed for Mode 1. Outdoor air fractions above this value will not be considered for operation in Mode 1. If this field is blank, the upper constraint on out...'
        },
    )
    mode_minimum_supply_air_mass_flow_rate_ratio: float | None = Field(
        default=0.1,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the minimum supply air mass flow rate ratio allowed for Mode 1. Supply air mass flow rate ratios below this value will not be considered for operation in Mode 1. Supply air mass flow rate rat...'
        },
    )
    mode_maximum_supply_air_mass_flow_rate_ratio: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the maximum supply air mass flow rate ratio allowed for Mode 1. Supply air mass flow rate ratios above this value will not be considered for operation in Mode 1. Supply air mass flow rate rat...'
        },
    )


class ZoneHVACDehumidifierDX(IDFBaseModel):
    """This object calculates the performance of zone (room) air dehumidifiers.
    Meant to model conventional direct expansion (DX) cooling-based room air
    dehumidifiers (reject 100% of condenser heat to the zone air), but this
    object might be able to be used to model other room air dehumidifier types."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:Dehumidifier:DX'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this direct expansion (DX) zone dehumidifier object.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the unit is off. Sc...',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air inlet node for the dehumidifier must be a zone air exhaust node.'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air outlet node for the dehumidifier must be a zone air inlet node.'
        },
    )
    rated_water_removal: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'L/day',
            'note': 'Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.',
        },
    )
    rated_energy_factor: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'L/kWh',
            'note': 'Rating point: air entering dehumidifier at 26.7 C (80 F) dry-bulb and 60% relative humidity.',
        },
    )
    rated_air_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    water_removal_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Name of a curve that describes the water removal rate (normalized to rated conditions) as a function of the dry-bulb temperature and relative humidity of the air entering the dehumidifier. Curve ou...',
        },
    )
    energy_factor_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Name of a curve that describes the energy factor (normalized to rated conditions) as a function of the dry-bulb temperature and relative humidity of the air entering the dehumidifier. Curve output ...',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Name of a curve that describes the part load fraction (PLF) of the system as a function of the part load ratio. Used to calculate dehumidifier run time fraction and electric power. quadratic curve ...',
        },
    )
    minimum_dry_bulb_temperature_for_dehumidifier_operation: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Dehumidifier shut off if inlet air (zone) temperature is below this value. This value must be less than the Maximum Dry-Bulb Temperature for Dehumidifier Operation.',
        },
    )
    maximum_dry_bulb_temperature_for_dehumidifier_operation: float | None = Field(
        default=35.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Dehumidifier shut off if inlet air (zone) temperature is above this value. This value must be greater than the Minimum Dry-Bulb Temperature for Dehumidifier Operation.',
        },
    )
    off_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the dehumidifier is available to operate, but does not operate (i.e., no high humidity load to be met). Off cycle parasitic power is 0 when the availability s...',
        },
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['WaterStorageTankNames'],
                'note': 'Name of storage tank used to collect water removed by the dehumidifier.',
            },
        )
    )


class ZoneHVACEnergyRecoveryVentilator(IDFBaseModel):
    """This compound component models a stand-alone energy recovery ventilator
    (ERV) that conditions outdoor ventilation air and supplies that air directly
    to a zone. The ERV unit is modeled as a collection of components: air-to-air
    heat exchanger, supply air fan, exhaust air fan and an optional controller
    to avoid overheating of the supply air (economizer or free cooling
    operation)."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:EnergyRecoveryVentilator'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    heat_exchanger_name: HXAirToAirSensibleAndLatentNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HXAirToAirSensibleAndLatentNames'],
            'note': 'Heat exchanger type must be HeatExchanger:AirToAir:SensibleAndLatent',
        },
    )
    supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "This flow rate must match the supply fan's air flow rate.",
        },
    )
    exhaust_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This flow rate must match the supply fan air flow rate.',
        },
    )
    supply_air_fan_name: FansOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff', 'FansSystemModel'],
            'note': 'Fan type must be Fan:OnOff or Fan:SystemModel',
        },
    )
    exhaust_air_fan_name: FansOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff', 'FansSystemModel'],
            'note': 'Fan type must be Fan:OnOff or Fan:SystemModel',
        },
    )
    controller_name: ControllerStandAloneEnergyRecoveryVentilatorRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControllerStandAloneEnergyRecoveryVentilator'],
            'note': 'Enter the name of a ZoneHVAC:EnergyRecoveryVentilator:Controller object.',
        },
    )
    ventilation_rate_per_unit_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': '0.000508 m3/s-m2 corresponds to 0.1 ft3/min-ft2 Used only when supply and exhaust air flow rates are autosized.',
        },
    )
    ventilation_rate_per_occupant: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-person',
            'note': '0.00236 m3/s-person corresponds to 5 ft3/min-person Used only when supply and exhaust air flow rates are autosized.',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )


class ZoneHVACEnergyRecoveryVentilatorController(IDFBaseModel):
    """This controller is used exclusively by the ZoneHVAC:EnergyRecoveryVentilator
    object to allow economizer (free cooling) operation when possible."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:EnergyRecoveryVentilator:Controller'
    name: str = Field(...)
    temperature_high_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dry-bulb temperature limit for economizer operation. No input or blank input means this limit is not operative',
        },
    )
    temperature_low_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor dry-bulb temperature limit for economizer operation. No input or blank input means this limit is not operative',
        },
    )
    enthalpy_high_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Enter the maximum outdoor enthalpy limit for economizer operation. No input or blank input means this limit is not operative',
        },
    )
    dewpoint_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dew point temperature limit for economizer operation. No input or blank input means this limit is not operative',
        },
    )
    electronic_enthalpy_limit_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter the name of a quadratic or cubic curve which defines the maximum outdoor humidity ratio (function of outdoor dry-bulb temperature) for economizer operation. No input or blank input means this...',
        },
    )
    exhaust_air_temperature_limit: (
        Literal['', 'ExhaustAirTemperatureLimit', 'NoExhaustAirTemperatureLimit'] | None
    ) = Field(default='NoExhaustAirTemperatureLimit')
    exhaust_air_enthalpy_limit: (
        Literal['', 'ExhaustAirEnthalpyLimit', 'NoExhaustAirEnthalpyLimit'] | None
    ) = Field(default='NoExhaustAirEnthalpyLimit')
    time_of_day_economizer_flow_control_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values greater than 0 indicate economizer operation is active. This schedule may be used with or without the High Humidity Control option. When used together, high humidity control has pri...',
        },
    )
    high_humidity_control_flag: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Select Yes to modify air flow rates based on a zone humidistat. Select No to disable this feature.'
        },
    )
    humidistat_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter the name of the zone where the humidistat is located.',
        },
    )
    high_humidity_outdoor_air_flow_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Enter the ratio of supply (outdoor) air to the maximum supply air flow rate when modified air flow rates are active based on high indoor humidity.'
        },
    )
    control_high_indoor_humidity_based_on_outdoor_humidity_ratio: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If NO is selected, the air flow rate is modified any time indoor relative humidity is above humidistat setpoint. If YES is selected, outdoor air flow rate is modified any time indoor relative humid...'
        },
    )


class ZoneHVACEvaporativeCoolerUnit(IDFBaseModel):
    """Zone evaporative cooler. Forced-convection cooling-only unit with supply
    fan, 100% outdoor air supply. Optional relief exhaust node"""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:EvaporativeCoolerUnit'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    outdoor_air_inlet_node_name: str = Field(
        ..., json_schema_extra={'note': 'this is an outdoor air node'}
    )
    cooler_outlet_node_name: str = Field(
        ..., json_schema_extra={'note': 'this is a zone inlet node'}
    )
    zone_relief_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'this is a zone exhaust node, optional if flow is being balanced elsewhere'
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ComponentModel',
        'Fan:ConstantVolume',
        'Fan:OnOff',
        'Fan:SystemModel',
        'Fan:VariableVolume',
    ] = Field(...)
    supply_air_fan_name: FansRef = Field(
        ..., json_schema_extra={'object_list': ['Fans']}
    )
    design_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    fan_placement: Literal['BlowThrough', 'DrawThrough'] = Field(...)
    cooler_unit_control_method: Literal[
        'ZoneCoolingLoadOnOffCycling',
        'ZoneCoolingLoadVariableSpeedFan',
        'ZoneTemperatureDeadbandOnOffCycling',
    ] = Field(...)
    throttling_range_temperature_difference: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'used for ZoneTemperatureDeadbandOnOffCycling hysteresis range for thermostatic control',
        },
    )
    cooling_load_control_threshold_heat_transfer_rate: float | None = Field(
        default=100.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Sign convention is that positive values indicate a cooling load',
        },
    )
    first_evaporative_cooler_object_type: Literal[
        'EvaporativeCooler:Direct:CelDekPad',
        'EvaporativeCooler:Direct:ResearchSpecial',
        'EvaporativeCooler:Indirect:CelDekPad',
        'EvaporativeCooler:Indirect:ResearchSpecial',
        'EvaporativeCooler:Indirect:WetCoil',
    ] = Field(...)
    first_evaporative_cooler_object_name: EvapCoolerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['EvapCoolerNames']}
    )
    second_evaporative_cooler_object_type: (
        Literal[
            'EvaporativeCooler:Direct:CelDekPad',
            'EvaporativeCooler:Direct:ResearchSpecial',
            'EvaporativeCooler:Indirect:CelDekPad',
            'EvaporativeCooler:Indirect:ResearchSpecial',
            'EvaporativeCooler:Indirect:WetCoil',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional, used for direct/indirect configurations second cooler must be immediately downstream of first cooler, if present'
        },
    )
    second_evaporative_cooler_name: EvapCoolerNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['EvapCoolerNames'],
            'note': 'optional, used for direct/indirect configurations',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    shut_off_relative_humidity: float | None = Field(
        default=None,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity above which the evap cooler is shut off.',
        },
    )


class ZoneHVACFourPipeFanCoil(IDFBaseModel):
    """Four pipe fan coil system. Forced-convection hydronic heating-cooling unit
    with supply fan, hot water heating coil, chilled water cooling coil, and
    fixed-position outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:FourPipeFanCoil'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    capacity_control_method: Literal[
        'ASHRAE90VariableFan',
        'ConstantFanVariableFlow',
        'CyclingFan',
        'MultiSpeedFan',
        'VariableFanConstantFlow',
        'VariableFanVariableFlow',
    ] = Field(...)
    maximum_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    low_speed_supply_air_flow_ratio: float | None = Field(default=0.33, gt=0.0)
    medium_speed_supply_air_flow_ratio: float | None = Field(
        default=0.66,
        gt=0.0,
        json_schema_extra={
            'note': 'Medium Speed Supply Air Flow Ratio should be greater than Low Speed Supply Air Flow Ratio'
        },
    )
    maximum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value of schedule multiplies maximum outdoor air flow rate',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Currently only one type OutdoorAir:Mixer object is available. This field should be left blank if the FanCoil is connected to central dedicated outdoor air through an AirTerminal:SingleDuct:Mixer ob...'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'If this field is blank, the OutdoorAir:Mixer is not used. This optional field specifies the name of the OutdoorAir:Mixer object. When used, this name needs to match name of the OutdoorAir:Mixer obj...',
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel', 'Fan:VariableVolume'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan type must be according to capacity control method (see I/O) For ConstantFanVariableFlow a Fan:OnOff or Fan:ConstantVolume is valid. For CyclingFan a Fan:OnOff is valid. For VariableFanVariableF...'
        },
    )
    supply_air_fan_name: FansCVandOnOffandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel']},
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:Water',
        'Coil:Cooling:Water:DetailedGeometry',
        'CoilSystem:Cooling:Water:HeatExchangerAssisted',
    ] = Field(...)
    cooling_coil_name: CoolingCoilsWaterRef = Field(
        ..., json_schema_extra={'object_list': ['CoolingCoilsWater']}
    )
    maximum_cold_water_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    minimum_cold_water_flow_rate: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm3/s'}
    )
    cooling_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    heating_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Water'] = (
        Field(...)
    )
    heating_coil_name: HeatingCoilsElectricRef | HeatingCoilsWaterRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatingCoilsElectric', 'HeatingCoilsWater']
        },
    )
    maximum_hot_water_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    minimum_hot_water_flow_rate: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm3/s'}
    )
    heating_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote cycling fan operation (fan cycles with cooling coil). Schedule values greater than 0 denote constant fan o...',
        },
    )
    minimum_supply_air_temperature_in_cooling_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = ASHRAE90VariableFan, enter the minimum air temperature in cooling mode. Leave this field blank or enter 0 to control to the zone load per ASHRAE 90.1. In this case, a ...',
        },
    )
    maximum_supply_air_temperature_in_heating_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = ASHRAE90VariableFan, enter the maximum air temperature in heating mode. Leave this field blank or enter 0 to control to the zone load per ASHRAE 90.1. In this case, a ...',
        },
    )


class ZoneHVACHybridUnitaryHVAC(IDFBaseModel):
    """Hybrid Unitary HVAC. A black box model for multi-mode packaged forced air
    equipment. Independent variables include outdoor air conditions and indoor
    air conditions. Controlled inputs include operating mode, supply air flow
    rate, and outdoor air faction. Empirical lookup tables are required to map
    supply air temperature supply air humidity, electricity use, fuel uses,
    water use, fan electricity use, and external static pressure as a function
    of each independent variable and each controlled input. In each timestep the
    model will choose one or more combinations of settings for mode, supply air
    flow rate, outdoor air faction, and part runtime fraction so as to satisfy
    zone requests for sensible cooling, heating, ventilation, and/or
    dehumidification with the least resource consumption. Equipment in this
    class may consume electricity, water, and up to two additional fuel types."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:HybridUnitaryHVAC'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    minimum_supply_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in this schedule are used as a constraint in choosing the feasible settings for supply air flow rate and outside air fraction in each operating mode. If this field is blank, no minimum is im...',
        },
    )
    maximum_supply_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in this schedule are used as a constraint in choosing the feasible settings for supply air flow rate and outdoor air fraction in each operating mode. If this field is blank, no maximum is im...',
        },
    )
    minimum_supply_air_humidity_ratio_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in this schedule are used as a constraint in choosing the feasible settings for supply air flow rate and outdoor air fraction in each operating mode. If this field is blank, no minimum is im...',
        },
    )
    maximum_supply_air_humidity_ratio_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values in this schedule are used as a constraint in choosing the feasible settings for supply air flow rate and outdoor air fraction in each operating mode. If this field is blank, no maximum is im...',
        },
    )
    method_to_choose_controlled_inputs_and_part_runtime_fraction: (
        Literal['', 'Automatic', 'User Defined'] | None
    ) = Field(
        default='Automatic',
        json_schema_extra={
            'note': 'Select the method that will be used to choose operating mode(s), supply air flow rate(s), outdoor air fraction(s) and part runtime fraction(s) in each time step. "Automatic" = chooses controlled in...'
        },
    )
    return_air_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Return air node for the hybrid unit must be a zone exhaust node.'
        },
    )
    outdoor_air_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Outdoor air node for the hybrid unit must be an outdoor air node.'
        },
    )
    supply_air_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Supply air node for the hybrid unit must be a zone air inlet node.'
        },
    )
    relief_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Relief node for the hybrid unit must be a zone exhaust node, unless flow is being balanced elsewhere.'
        },
    )
    system_maximum_supply_air_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'The value in this field represents the maximum supply air volume flow rate among all operating modes. Values of extensive variables in lookup tables are normalized by the system maximum supply air ...',
        },
    )
    external_static_pressure_at_system_maximum_supply_air_flow_rate: float | None = (
        Field(
            default=None,
            gt=0.0,
            json_schema_extra={
                'units': 'Pa',
                'note': 'Input the external static pressure when the system operates at maximum supply air flow rate. Fan affinity laws are used to scale supply fan power from the values tabulated in lookup tables, to valu...',
            },
        )
    )
    fan_heat_included_in_lookup_tables: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field specifies if the fan heat is accounted for in the lookup tables.'
        },
    )
    fan_heat_gain_location: Literal['', 'MixedAirStream', 'SupplyAirStream'] | None = (
        Field(
            default='SupplyAirStream',
            json_schema_extra={
                'note': 'This field specifies where to add the fan heat in the air stream.'
            },
        )
    )
    fan_heat_in_air_stream_fraction: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': '0.0 means no fan heat is added to the air stream, 1.0 means all fan heat is added to the air stream.'
        },
    )
    scaling_factor: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'The value in this field scales all extensive performance variables including: supply air mass flow rate, fuel uses, and water use. If this field is blank, the default scaling factor is 1.'
        },
    )
    minimum_time_between_mode_change: float | None = Field(
        default=10.0,
        ge=1.0,
        json_schema_extra={
            'units': 'minutes',
            'note': 'Any mode selected will not operate for less time than the value input in this field. If the value in this field is larger than each timestep, the mode selected in one time step will persist in late...',
        },
    )
    first_fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'None',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(
        default='Electricity',
        json_schema_extra={
            'note': 'Select the fuel type associated with field: "System Electric Power Lookup Table" in each mode. If this field is blank, default first fuel type = Electricity.'
        },
    )
    second_fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'None',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Select the fuel type associated with field: "System Second Fuel Consumption Lookup Table" in each mode. If this field is blank, default second fuel type = None.'
        },
    )
    third_fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'None',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Select the fuel type associated with field: "System Third Fuel Consumption Lookup Table" in each mode. If this field is blank, default third fuel type = None.'
        },
    )
    objective_function_to_minimize: (
        Literal['', 'Electricity Use', 'Second Fuel Use', 'Third Fuel Use', 'Water Use']
        | None
    ) = Field(
        default='Electricity Use',
        json_schema_extra={
            'note': 'In each time step, controlled variables will be chosen to minimize the selection in this field, subject to constraints. If this field is blank, the objective function will minimize electricity use.'
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'Enter the name of a DesignSpecification:OutdoorAir object. Information in that object will be used to compute the minimum outdoor air flow rate in each time step. If this field is blank, the system...',
        },
    )
    mode_0_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter a name for Mode 0. Mode 0 describes equipment performance in standby. Mode 0 is usually characterized by electricity use for controls and crankcase heaters, or other standby resource consumpt...'
        },
    )
    mode_0_supply_air_temperature_lookup_table_name: MultivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['MultivariateFunctions'],
                'note': 'Enter the name of the Supply Air Temperature Lookup Table for Mode 0. Units for lookup table values should be in C. If this field is blank, Mode 0 will not be considered for any period that require...',
            },
        )
    )
    mode_0_supply_air_humidity_ratio_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the Supply Air Humidity Ratio Lookup Table for Mode 0. Units for lookup table values should be in kgWater/kgDryAir. If this field is blank, Mode 0 will not be considered for any p...',
        },
    )
    mode_0_system_electric_power_lookup_table_name: MultivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['MultivariateFunctions'],
                'note': 'Enter the name of the Electric Power Lookup Table for Mode 0. Units for lookup table values should be in W. If this field is blank, Mode 0 does not consume electricity.',
            },
        )
    )
    mode_0_supply_fan_electric_power_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the Supply Fan Electric Power Lookup Table for Mode 0. Units for lookup table values should be in W. If this field is blank, Mode 0 does not consume electricity for supply fan.',
        },
    )
    mode_0_external_static_pressure_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the External Static Pressure Lookup Table for Mode 0. Units for lookup table values should be in Pa. If this field is blank, external static pressure will not be reported.',
        },
    )
    mode_0_system_second_fuel_consumption_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Second Fuel Consumption Lookup Table for Mode 0. Units for lookup table values should be in W. If this field is blank, Mode 0 does not consume a second fuel.',
        },
    )
    mode_0_system_third_fuel_consumption_lookup_table_name: (
        MultivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Third Fuel Consumption Lookup Table for Mode 0. Units for lookup table values should be in W. If this field is blank, Mode 0 does not consume a third fuel.',
        },
    )
    mode_0_system_water_use_lookup_table_name: MultivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MultivariateFunctions'],
            'note': 'Enter the name of the System Water Use Lookup Table for Mode 0. Units for lookup table values should be in kg/s. If this field is blank, Mode 0 does not consume water.',
        },
    )
    mode_0_outdoor_air_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the outdoor air fraction for Mode 0. If this field is blank, the outdoor air fraction for Mode 0 will be 0.00.'
        },
    )
    mode_0_supply_air_mass_flow_rate_ratio: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Enter the supply air mass flow rate ratio for Mode 0. The value in this field will be used to determine the supply air mass flow rate in Mode 0. Supply air mass flow rate ratio describes supply air...'
        },
    )
    modes: list[ZoneHVACHybridUnitaryHVACModesItem] | None = Field(default=None)


class ZoneHVACIdealLoadsAirSystem(IDFBaseModel):
    """Ideal system used to calculate loads without modeling a full HVAC system.
    All that is required for the ideal system are zone controls, zone equipment
    configurations, and the ideal loads system component. This component can be
    thought of as an ideal unit that mixes zone air with the specified amount of
    outdoor air and then adds or removes heat and moisture at 100% efficiency in
    order to meet the specified controls. Energy use is reported as
    DistrictHeatingWater and DistrictCooling."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:IdealLoadsAirSystem'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    zone_supply_air_node_name: str = Field(
        ..., json_schema_extra={'note': 'Must match a zone air inlet node name.'}
    )
    zone_exhaust_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Should match a zone air exhaust node name. This field is optional, but is required if this this object is used with other forced air equipment.'
        },
    )
    system_inlet_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This field is only required when the Ideal Loads Air System is connected to an AirloopHVAC:ZoneReturnPlenum, otherwise leave this field blank. When connected to a plenum the return plenum Outlet No...'
        },
    )
    maximum_heating_supply_air_temperature: float | None = Field(
        default=50.0, gt=0.0, lt=100.0, json_schema_extra={'units': 'C'}
    )
    minimum_cooling_supply_air_temperature: float | None = Field(
        default=13.0, gt=-100.0, lt=50.0, json_schema_extra={'units': 'C'}
    )
    maximum_heating_supply_air_humidity_ratio: float | None = Field(
        default=0.0156, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    minimum_cooling_supply_air_humidity_ratio: float | None = Field(
        default=0.0077, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    heating_limit: (
        Literal[
            '', 'LimitCapacity', 'LimitFlowRate', 'LimitFlowRateAndCapacity', 'NoLimit'
        ]
        | None
    ) = Field(default='NoLimit')
    maximum_heating_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is ignored if Heating Limit = NoLimit If this field is blank, there is no limit.',
        },
    )
    maximum_sensible_heating_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field is ignored if Heating Limit = NoLimit If this field is blank, there is no limit.',
        },
    )
    cooling_limit: (
        Literal[
            '', 'LimitCapacity', 'LimitFlowRate', 'LimitFlowRateAndCapacity', 'NoLimit'
        ]
        | None
    ) = Field(default='NoLimit')
    maximum_cooling_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is ignored if Cooling Limit = NoLimit This field is required if Outdoor Air Economizer Type is anything other than NoEconomizer.',
        },
    )
    maximum_total_cooling_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field is ignored if Cooling Limit = NoLimit',
        },
    )
    heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, heating is always available.',
        },
    )
    cooling_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, cooling is always available.',
        },
    )
    dehumidification_control_type: (
        Literal[
            '',
            'ConstantSensibleHeatRatio',
            'ConstantSupplyHumidityRatio',
            'Humidistat',
            'None',
        ]
        | None
    ) = Field(
        default='ConstantSensibleHeatRatio',
        json_schema_extra={
            'note': 'ConstantSensibleHeatRatio means that the ideal loads system will be controlled to meet the sensible cooling load, and the latent cooling rate will be computed using a constant sensible heat ratio (...'
        },
    )
    cooling_sensible_heat_ratio: float | None = Field(
        default=0.7,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This field is applicable only when Dehumidification Control Type is ConstantSensibleHeatRatio',
        },
    )
    humidification_control_type: (
        Literal['', 'ConstantSupplyHumidityRatio', 'Humidistat', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None means that there is no humidification. Humidistat means that there is a ZoneControl:Humidistat for this zone and the ideal loads system will attempt to satisfy the humidistat. ConstantSupplyHu...'
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the minimum outdoor air flow rate will be computed using these specifications. The outdoor air flow rate will also be affected b...',
        },
    )
    outdoor_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This field is required if the system provides outdoor air Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    demand_controlled_ventilation_type: (
        Literal['', 'CO2Setpoint', 'None', 'OccupancySchedule'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'This field controls how the minimum outdoor air flow rate is calculated. None means that design occupancy will be used to compute the minimum outdoor air flow rate OccupancySchedule means that curr...'
        },
    )
    outdoor_air_economizer_type: (
        Literal['', 'DifferentialDryBulb', 'DifferentialEnthalpy', 'NoEconomizer']
        | None
    ) = Field(
        default='NoEconomizer',
        json_schema_extra={
            'note': 'DifferentialDryBulb and DifferentialEnthalpy will increase the outdoor air flow rate when there is a cooling load and the outdoor air temperature or enthalpy is below the zone exhaust air temperatu...'
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Applicable only if Heat Recovery Type is Enthalpy.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )


class ZoneHVACOutdoorAirUnit(IDFBaseModel):
    """The zone outdoor air unit models a single-zone dedicated outdoor air system
    (DOAS). Forced-convection 100% outdoor air unit with supply fan and optional
    equipment including exhaust fan, heating coil, cooling coil, and heat
    recovery."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:OutdoorAirUnit'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': '(name of zone system is serving)',
        },
    )
    outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    outdoor_air_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    supply_fan_name: FansCVandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandVAV', 'FansSystemModel'],
            'note': 'Allowable fan types are Fan:SystemModel and Fan:ConstantVolume and Fan:VariableVolume',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    exhaust_fan_name: (FansCVandVAVRef | FansSystemModelRef) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FansCVandVAV', 'FansSystemModel'],
            'note': 'Allowable fan types are Fan:SystemModel and Fan:ConstantVolume and Fan:VariableVolume Fan:VariableVolume',
        },
    )
    exhaust_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    exhaust_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    unit_control_type: Literal['', 'NeutralControl', 'TemperatureControl'] | None = (
        Field(default='NeutralControl')
    )
    high_air_control_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Air and control temperatures for cooling. If outdoor air temperature is above the high air control temperature, then the zone inlet air temperature is set to the high air control temperature. If th...',
        },
    )
    low_air_control_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Air and control temperatures for Heating. If outdoor air temperature is below the low air control temperature, then the zone inlet air temperature is set to the low air control temperature. If the ...',
        },
    )
    outdoor_air_node_name: str = Field(...)
    airoutlet_node_name: str = Field(...)
    airinlet_node_name: str | None = Field(
        default=None, json_schema_extra={'note': 'air leaves zone'}
    )
    supply_fanoutlet_node_name: str = Field(...)
    outdoor_air_unit_list_name: OutdoorAirUnitEquipmentListsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['OutdoorAirUnitEquipmentLists'],
            'note': 'Enter the name of an ZoneHVAC:OutdoorAirUnit:EquipmentList object.',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )


class ZoneHVACOutdoorAirUnitEquipmentList(IDFBaseModel):
    """Equipment list for components in a ZoneHVAC:OutdoorAirUnit. Components are
    simulated sequentially in the order given in the equipment list."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:OutdoorAirUnit:EquipmentList'
    name: str = Field(...)
    component_1_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_1_name: str | None = Field(default=None)
    component_2_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_2_name: str | None = Field(default=None)
    component_3_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_3_name: str | None = Field(default=None)
    component_4_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_4_name: str | None = Field(default=None)
    component_5_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_5_name: str | None = Field(default=None)
    component_6_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_6_name: str | None = Field(default=None)
    component_7_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_7_name: str | None = Field(default=None)
    component_8_object_type: (
        Literal[
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water:HeatexchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
        ]
        | None
    ) = Field(default=None)
    component_8_name: str | None = Field(default=None)


class ZoneHVACPackagedTerminalAirConditioner(IDFBaseModel):
    """Packaged terminal air conditioner (PTAC). Forced-convection heating-cooling
    unit with supply fan, direct expansion (DX) cooling coil, heating coil (gas,
    electric, hot water, or steam) and fixed-position outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:PackagedTerminalAirConditioner'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this packaged terminal air conditioner object.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the unit is off.',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air inlet node for the PTAC must be a zone air exhaust Node.'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air outlet node for the PTAC must be a zone air inlet node.'
        },
    )
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Currently only one OutdoorAir:Mixer object type is available. This field should be left blank if the PTAC is connected to central dedicated outdoor air through an AirTerminal:SingleDuct:Mixer object.'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'If this field is blank, the OutdoorAir:Mixer is not used. This optional field specifies the name of the OutdoorAir:Mixer object. When used, this name needs to match name of the OutdoorAir:Mixer obj...',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size. Only used when supply air fan operating mode schedule values specify continuous fan (schedule values greater than 0 specify continuous fan operation). This a...',
        },
    )
    no_load_supply_air_flow_rate_control_set_to_low_speed: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'When Yes is selected the minimum air flow rate is used. When No is selected the maximum air flow rate is used.'
        },
    )
    cooling_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during cooling operation. This field is set to zero flow when the PTAC is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during heating operation. This field is set to zero flow when the PTAC is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when supply air fan operating mode schedule values specify continuous fan (schedule values greater than 0 specify continuous fan operation). This air flow rate is used when no heating or ...',
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works when continuous fan operation is used the entire simulation (all supply air fan operating mode schedule values are greater than 0). If any fan operating mode schedule ...'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff', 'FansSystemModel'],
            'note': 'Needs to match in the fan object.',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:Electric',
        'Coil:Heating:Fuel',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(..., json_schema_extra={'note': 'Select the type of heating coil.'})
    heating_coil_name: HeatingCoilNameRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Needs to match in the heating coil object.',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Select the type of Cooling Coil. Only works with Coil:Cooling:DX or Coil:Cooling:DX:SingleSpeed or CoilSystem:Cooling:DX:HeatExchangerAssisted or Coil:Cooling:DX:VariableSpeed.'
        },
    )
    cooling_coil_name: (
        CoilCoolingDXRef | CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'CoolingCoilsDXSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ],
            'note': 'Needs to match a DX cooling coil object.',
        },
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough',
        json_schema_extra={
            'note': 'Select fan placement as either blow through or draw through.'
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater than 0 denot...',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    capacity_control_method: Literal['', 'None', 'SingleZoneVAV'] | None = Field(
        default='None'
    )
    minimum_supply_air_temperature_in_cooling_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = SingleZoneVAV, enter the minimum air temperature limit for reduced fan speed.',
        },
    )
    maximum_supply_air_temperature_in_heating_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = SingleZoneVAV, enter the maximum air temperature limit for reduced fan speed.',
        },
    )


class ZoneHVACPackagedTerminalHeatPump(IDFBaseModel):
    """Packaged terminal heat pump (PTHP). Forced-convection heating-cooling unit
    with supply fan, direct expansion (DX) cooling coil, DX heating coil (air-
    to-air heat pump), supplemental heating coil (gas, electric, hot water, or
    steam), and fixed-position outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:PackagedTerminalHeatPump'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this packaged terminal heat pump object.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the unit is off.',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air inlet node for the PTHP must be a zone air exhaust node.'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Air outlet node for the PTHP must be a zone air inlet node.'
        },
    )
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Currently only one OutdoorAir:Mixer object type is available. This field should be left blank if the PTHP is connected to central dedicated outdoor air through an AirTerminal:SingleDuct:Mixer object.'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'If this field is blank, the OutdoorAir:Mixer is not used. This optional field specifies the name of the OutdoorAir:Mixer object. When used, this name needs to match name of the OutdoorAir:Mixer obj...',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size. Only used when heat pump fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coil compressor is of...',
        },
    )
    no_load_supply_air_flow_rate_control_set_to_low_speed: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'When Yes is selected the minimum air flow rate is used. When No is selected the maximum air flow rate is used.'
        },
    )
    cooling_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during cooling operation. This field is set to zero flow when the PTHP is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during heating operation. This field is set to zero flow when the PTHP is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when heat pump Fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coil compressor is off. If this field is left blank or zero, ...',
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with fan operating mode is continuous.'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff', 'FansSystemModel'],
            'note': 'Needs to match a fan object.',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:DX:SingleSpeed', 'Coil:Heating:DX:VariableSpeed'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Only works with Coil:Heating:DX:SingleSpeed or Coil:Heating:DX:VariableSpeed.'
        },
    )
    heating_coil_name: HeatingCoilsDXSingleSpeedRef | HeatingCoilsDXVariableSpeedRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'HeatingCoilsDXSingleSpeed',
                    'HeatingCoilsDXVariableSpeed',
                ],
                'note': 'Needs to match in the DX Heating Coil object.',
            },
        )
    )
    heating_convergence_tolerance: float | None = Field(
        default=0.001,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Defines Heating convergence tolerance as a fraction of Heating load to be met.',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Only works with Coil:Cooling:DX or Coil:Cooling:DX:SingleSpeed or CoilSystem:Cooling:DX:HeatExchangerAssisted or Coil:Cooling:DX:VariableSpeed.'
        },
    )
    cooling_coil_name: (
        CoilCoolingDXRef | CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'CoolingCoilsDXSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ],
            'note': 'Needs to match in the DX Cooling Coil object.',
        },
    )
    cooling_convergence_tolerance: float | None = Field(
        default=0.001,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Defines Cooling convergence tolerance as a fraction of the Cooling load to be met.',
        },
    )
    supplemental_heating_coil_object_type: Literal[
        'Coil:Heating:Electric',
        'Coil:Heating:Fuel',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'works with gas, electric, hot water and steam heating coil.'
        },
    )
    supplemental_heating_coil_name: HeatingCoilNameRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Needs to match in the supplemental heating coil object.',
        },
    )
    maximum_supply_air_temperature_from_supplemental_heater: (
        float | Literal['Autosize']
    ) = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'Supply air temperature from the supplemental heater will not exceed this value.',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(
        default=21.0,
        le=21.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Supplemental heater will not operate when outdoor temperature exceeds this value.',
        },
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough',
        json_schema_extra={
            'note': 'Select fan placement as either blow through or draw through.'
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule values of 0 denote cycling fan operation (fan cycles with cooling or heating coil). Schedule Name values greater than 0 denote con...',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    capacity_control_method: Literal['', 'None', 'SingleZoneVAV'] | None = Field(
        default='None'
    )
    minimum_supply_air_temperature_in_cooling_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = SingleZoneVAV, enter the minimum air temperature limit for reduced fan speed.',
        },
    )
    maximum_supply_air_temperature_in_heating_mode: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'For Capacity Control Method = SingleZoneVAV, enter the maximum air temperature limit for reduced fan speed.',
        },
    )


class ZoneHVACTerminalUnitVariableRefrigerantFlow(IDFBaseModel):
    """A terminal unit with variable refrigerant flow (VRF) DX cooling and heating
    coils (air-to-air heat pump). The VRF terminal units are served by an
    AirConditioner:VariableRefrigerantFlow or
    AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:* system.
    Terminal units can be configured as zone, air loop or outside air system
    equipment."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow'
    name: str | None = Field(default=None)
    terminal_unit_availability_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The unit is available the entire simulation if this field is left blank Schedule values of 0 denote the unit is off.',
        },
    )
    terminal_unit_air_inlet_node_name: str = Field(
        ..., json_schema_extra={'note': 'the inlet node to the terminal unit'}
    )
    terminal_unit_air_outlet_node_name: str = Field(
        ..., json_schema_extra={'note': 'the outlet node of the terminal unit'}
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    no_cooling_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    no_heating_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    cooling_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is used only when an outdoor air mixer is included. This field is set to zero flow when the VRF terminal unit is connected to central dedicated outdoor air through air terminal single du...',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is used only when an outdoor air mixer is included. This field is set to zero flow when the VRF terminal unit is connected to central dedicated outdoor air through air terminal single du...',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is used only when an outdoor air mixer is included. This field is set to zero flow when the VRF terminal unit is connected to central dedicated outdoor air through air terminal single du...',
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Required for zone equipment. Leave blank if terminal unit is used in AirLoopHVAC:OutdoorAirSystem:EquipmentList. Also leave blank if terminal unit is used on main AirloopHVAC branch and terminal un...',
        },
    )
    supply_air_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough',
        json_schema_extra={
            'note': 'Select fan placement as either blow through or draw through. Required for zone equipment. This field is ignored if the VRF terminal unit is used in AirLoopHVAC:OutdoorAirSystem:EquipmentList. This ...'
        },
    )
    supply_air_fan_object_type: (
        Literal['', 'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'] | None
    ) = Field(
        default='Fan:ConstantVolume',
        json_schema_extra={
            'note': 'Supply Air Fan Object Type must be Fan:SystemModel, Fan:OnOff, or Fan:ConstantVolume if AirConditioner:VariableRefrigerantFlow is used to model VRF outdoor unit Supply Air Fan Object Type must be F...'
        },
    )
    supply_air_fan_object_name: (
        FansCVandOnOffandVAVRef | FansSystemModelRef
    ) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel']},
    )
    outside_air_mixer_object_type: Literal['OutdoorAir:Mixer'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Currently only one type OutdoorAir:Mixer object is available. If this field is blank, and outside air mixer is not used. This field should be left blank if the VRF terminal unit is connected to cen...'
        },
    )
    outside_air_mixer_object_name: OutdoorAirMixersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'If this field is blank, the OutdoorAir:Mixer is not used. This optional field specifies the name of the OutdoorAir:Mixer object. When used, this name needs to match name of the OutdoorAir:Mixer obj...',
        },
    )
    cooling_coil_object_type: (
        Literal[
            'Coil:Cooling:DX:VariableRefrigerantFlow',
            'Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow if AirConditioner:VariableRefrigerantFlow is used to model VRF outdoor unit Cooling Coil Type must be Coil:Cooling:DX:VariableRefri...'
        },
    )
    cooling_coil_object_name: (
        CoolingCoilsDXVarRefrigFlowRef
        | CoolingCoilsDXVarRefrigFlowFluidTemperatureControlRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'CoolingCoilsDXVarRefrigFlow',
                'CoolingCoilsDXVarRefrigFlowFluidTemperatureControl',
            ],
            'note': 'Cooling Coil Type must be Coil:Cooling:DX:VariableRefrigerantFlow This field may be left blank if heating-only mode is used',
        },
    )
    heating_coil_object_type: (
        Literal[
            'Coil:Heating:DX:VariableRefrigerantFlow',
            'Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow if AirConditioner:VariableRefrigerantFlow is used to model VRF outdoor unit Heating Coil Type must be Coil:Heating:DX:VariableRefri...'
        },
    )
    heating_coil_object_name: (
        HeatingCoilsDXVarRefrigFlowRef
        | HeatingCoilsDXVarRefrigFlowFluidTemperatureControlRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'HeatingCoilsDXVarRefrigFlow',
                'HeatingCoilsDXVarRefrigFlowFluidTemperatureControl',
            ],
            'note': 'Heating Coil Type must be Coil:Heating:DX:VariableRefrigerantFlow This field may be left blank if cooling-only mode is used',
        },
    )
    zone_terminal_unit_on_parasitic_electric_energy_use: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    zone_terminal_unit_off_parasitic_electric_energy_use: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    rated_heating_capacity_sizing_ratio: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': "If this terminal unit's heating coil is autosized, the heating capacity is sized to be equal to the cooling capacity multiplied by this sizing ratio. This input applies to the terminal unit heating...",
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    supplemental_heating_coil_object_type: (
        Literal[
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'works with gas, electric, hot water and steam heating coil.'
        },
    )
    supplemental_heating_coil_name: HeatingCoilNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Needs to match in the supplemental heating coil object.',
        },
    )
    maximum_supply_air_temperature_from_supplemental_heater: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'Supply air temperature from the supplemental heater will not exceed this value.',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(
        default=21.0,
        le=21.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Supplemental heater will not operate when outdoor temperature exceeds this value.',
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Used only for AirloopHVAC equipment on a main branch and defines zone name where thermostat is located. Not required for zone equipment. Leave blank if terminal unit is used in AirLoopHVAC:OutdoorA...',
        },
    )
    design_specification_multispeed_object_type: (
        Literal['UnitarySystemPerformance:Multispeed'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of performance specification object used to describe the multispeed coil or fan.'
        },
    )
    design_specification_multispeed_object_name: (
        UnitarySystemPerformanceNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnitarySystemPerformanceNames'],
            'note': 'The name of the performance specification object used to describe the multispeed coil or fan.',
        },
    )


class ZoneHVACUnitHeater(IDFBaseModel):
    """Unit heater. Forced-convection heating-only unit with supply fan, heating
    coil (gas, electric, hot water, or steam) and fixed-position outdoor air
    mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:UnitHeater'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str | None = Field(default=None)
    air_outlet_node_name: str | None = Field(default=None)
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel', 'Fan:VariableVolume'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Allowable fan types are Fan:ConstantVolume, Fan:OnOff, Fan:VariableVolume and Fan:SystemModel'
        },
    )
    supply_air_fan_name: FansCVandOnOffandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel']},
    )
    maximum_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:Electric',
        'Coil:Heating:Fuel',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(...)
    heating_coil_name: HeatingCoilNameRef = Field(
        ..., json_schema_extra={'object_list': ['HeatingCoilName']}
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule name values of 0 denote cycling fan operation (fan cycles with the heating coil). Schedule values greater than 0 denote constant f...',
        },
    )
    supply_air_fan_operation_during_no_heating: Literal['No', 'Yes'] = Field(
        ...,
        json_schema_extra={
            'note': 'This choice field allows the user to define how the unit heater will operate under "no heating load" or cooling conditions. If the "No" is selected, then the fan will not run unless there is a heat...'
        },
    )
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Not used when heating coil is gas or electric',
        },
    )
    minimum_hot_water_or_steam_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Not used when heating coil is gas or electric',
        },
    )
    heating_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )


class ZoneHVACUnitVentilator(IDFBaseModel):
    """Unit ventilator. Forced-convection ventilation unit with supply fan
    (constant-volume or variable-volume), optional chilled water cooling coil,
    optional heating coil (gas, electric, hot water, or steam) and controllable
    outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:UnitVentilator'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    maximum_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    outdoor_air_control_type: Literal[
        'FixedAmount', 'FixedTemperature', 'VariablePercent'
    ] = Field(...)
    minimum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'schedule values multiply the minimum outdoor air flow rate',
        },
    )
    maximum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    maximum_outdoor_air_fraction_or_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'that this depends on the control type as to whether it is a fraction or temperature',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Inlet node name must be zone exhaust node name if there is no DOA Mixer, or if the unit ventilator is connected DOA, then the air inlet node name must be the mixer outlet air node name for InletSid...'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Outlet node name must be zone inlet node name if there is no DOA Mixer, or if the unit ventilator is connected DOA, then the air outlet node name must be the mixer secondary air inlet node name for...'
        },
    )
    outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'this field is left blank only if the Unit Ventilator is connected to a central dedicated outdoor air (DOA) via AirTerminal:SingleDuct:Mixer object'
        },
    )
    exhaust_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'this field is left blank only if the Unit Ventilator is connected to a central dedicated outdoor air (DOA) via AirTerminal:SingleDuct:Mixer object'
        },
    )
    mixed_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'inlet to coils this field is left blank only if the Unit Ventilator is connected to a central dedicated outdoor air (DOA) via AirTerminal:SingleDuct:Mixer object'
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel', 'Fan:VariableVolume'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Allowable fan types are Fan:ConstantVolume, Fan:OnOff, Fan:VariableVolume, and Fan:SystemModel'
        },
    )
    supply_air_fan_name: FansCVandOnOffandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel']},
    )
    coil_option: Literal['Cooling', 'Heating', 'HeatingAndCooling', 'None'] = Field(...)
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule name values of 0 denote cycling fan operation (fan cycles with cooling/heating coil). Schedule values greater than 0 denote consta...',
        },
    )
    heating_coil_object_type: (
        Literal[
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(default=None)
    heating_coil_name: HeatingCoilNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['HeatingCoilName']}
    )
    heating_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    cooling_coil_object_type: (
        Literal[
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'CoilSystem:Cooling:Water:HeatExchangerAssisted',
        ]
        | None
    ) = Field(default=None)
    cooling_coil_name: CoolingCoilsWaterRef | None = Field(
        default=None, json_schema_extra={'object_list': ['CoolingCoilsWater']}
    )
    cooling_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )


class ZoneHVACWaterToAirHeatPump(IDFBaseModel):
    """Water-to-air heat pump. Forced-convection heating-cooling unit with supply
    fan, water-to-air cooling and heating coils, supplemental heating coil (gas,
    electric, hot water, or steam), and fixed-position outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:WaterToAirHeatPump'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Currently only one OutdoorAir:Mixer object type is available. This field should be left blank if the WSHP is connected to central dedicated outdoor air through an AirTerminal:SingleDuct:Mixer object.'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'If this field is blank, the OutdoorAir:Mixer is not used. This optional field specifies the name of the OutdoorAir:Mixer object. When used, this name needs to match name of the OutdoorAir:Mixer obj...',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to fan size. Only used when heat pump fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coil compressor is of...',
        },
    )
    no_load_supply_air_flow_rate_control_set_to_low_speed: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'When Yes is selected the minimum air flow rate is used. When No is selected the maximum air flow rate is used.'
        },
    )
    cooling_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during cooling operation. This field is set to zero flow when the WSHP is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Must be less than or equal to supply air flow rate during heating operation. This field is set to zero flow when the WSHP is connected to central dedicated outdoor air through air terminal single d...',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when heat pump Fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coil compressor is off. If this field is left blank or zero, ...',
        },
    )
    supply_air_fan_object_type: Literal['Fan:OnOff', 'Fan:SystemModel'] = Field(...)
    supply_air_fan_name: FansOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff', 'FansSystemModel'],
            'note': 'Needs to match Fan:SystemModel or Fan:OnOff object',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:WaterToAirHeatPump:EquationFit',
        'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
    ] = Field(...)
    heating_coil_name: HeatingCoilsWaterToAirHPRef | HeatingCoilsWaterToAirVSHPRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'HeatingCoilsWaterToAirHP',
                    'HeatingCoilsWaterToAirVSHP',
                ],
                'note': 'Needs to match in the water-to-air heat pump heating coil object',
            },
        )
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:WaterToAirHeatPump:EquationFit',
        'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
    ] = Field(...)
    cooling_coil_name: CoolingCoilsWaterToAirHPRef | CoolingCoilsWaterToAirVSHPRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'CoolingCoilsWaterToAirHP',
                    'CoolingCoilsWaterToAirVSHP',
                ],
                'note': 'Needs to match in the water-to-air heat pump cooling coil object',
            },
        )
    )
    supplemental_heating_coil_object_type: Literal[
        'Coil:Heating:Electric',
        'Coil:Heating:Fuel',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'works with gas, electric, hot water and steam heating coils'
        },
    )
    supplemental_heating_coil_name: HeatingCoilNameRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Needs to match in the supplemental heating coil object',
        },
    )
    maximum_supply_air_temperature_from_supplemental_heater: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'Supply air temperature from the supplemental heater will not exceed this value.',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(default=21.0, le=21.0, json_schema_extra={'units': 'C'})
    outdoor_dry_bulb_temperature_sensor_node_name: str | None = Field(default=None)
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule values of 0 denote cycling fan operation (fan cycles with cooling or heating coil). Schedule values greater than 0 denote constant...',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    heat_pump_coil_water_flow_mode: (
        Literal['', 'Constant', 'ConstantOnDemand', 'Cycling'] | None
    ) = Field(
        default='Cycling',
        json_schema_extra={
            'note': 'used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit Constant results in 100% water flow regardless of compressor PLR Cycling results in water flow that matches compres...'
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
    design_specification_multispeed_object_type: (
        Literal['UnitarySystemPerformance:Multispeed'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of performance specification object used to describe the multispeed coil or fan.'
        },
    )
    design_specification_multispeed_object_name: (
        UnitarySystemPerformanceNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnitarySystemPerformanceNames'],
            'note': 'The name of the performance specification object used to describe the multispeed coil or fan.',
        },
    )


class ZoneHVACWindowAirConditioner(IDFBaseModel):
    """Window air conditioner. Forced-convection cooling-only unit with supply fan,
    direct expansion (DX) cooling coil, and fixed-position outdoor air mixer."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:WindowAirConditioner'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    maximum_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] = Field(
        ...,
        json_schema_extra={
            'note': 'currently only one OutdoorAir:Mixer object type is available.'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef = Field(
        ..., json_schema_extra={'object_list': ['OutdoorAirMixers']}
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works when continuous fan operation is used the entire simulation (all supply air fan operating mode schedule values are greater than 0). If any fan operating mode schedule ...'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff', 'FansSystemModel'],
            'note': 'Fan type Fan:ConstantVolume is used with continuous fan and fan type Fan:OnOff is used with cycling Fan.',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(...)
    dx_cooling_coil_name: (
        CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingCoilsDXSingleSpeed', 'CoolingCoilsDXVariableSpeed']
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that controls fan operation. Schedule Name values of 0 denote cycling fan operation (fan cycles with cooling coil). Schedule values greater than 0 denote constant fan o...',
        },
    )
    fan_placement: Literal['BlowThrough', 'DrawThrough'] = Field(...)
    cooling_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_specification_zonehvac_sizing_object_name: (
        DesignSpecificationZoneHVACSizingNameRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneHVACSizingName'],
            'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.',
        },
    )
