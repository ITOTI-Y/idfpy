"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Unitary Equipment
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    CoilCoolingDXRef,
    CoolingCoilsDXMultiModeOrSingleSpeedRef,
    CoolingCoilsDXMultiSpeedRef,
    CoolingCoilsDXRef,
    CoolingCoilsDXSingleSpeedRef,
    CoolingCoilsDXVariableSpeedRef,
    CoolingCoilsWaterRef,
    CoolingCoilsWaterToAirHPRef,
    CoolingCoilsWaterToAirVSHPRef,
    FansCVandOnOffRef,
    FansOnOffRef,
    FansRef,
    FansSystemModelRef,
    HeatingCoilNameRef,
    HeatingCoilsDesuperheaterRef,
    HeatingCoilsDXMultiSpeedRef,
    HeatingCoilsDXRef,
    HeatingCoilsDXSingleSpeedRef,
    HeatingCoilsDXVariableSpeedRef,
    HeatingCoilsElectricMultiStageRef,
    HeatingCoilsGasMultiStageRef,
    HeatingCoilsWaterToAirHPRef,
    HeatingCoilsWaterToAirVSHPRef,
    IntegratedHeatPumpsRef,
    OutdoorAirMixersRef,
    ScheduleNamesRef,
    UnitarySystemPerformanceNamesRef,
    UserDefinedCoilRef,
    ZoneNamesRef,
)


class UnitarySystemPerformanceMultispeedFlowRatiosItem(IDFBaseModel):
    """Nested object type for array items."""

    heating_speed_supply_air_flow_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Used only for Multi speed coils Enter the lowest operating supply air flow ratio during heating operation or specify autosize. This value is the ratio of air flow at this speed to the maximum air f...'
        },
    )
    cooling_speed_supply_air_flow_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Used only for Multi speed coils Enter the lowest operating supply air flow ratio during cooling operation or specify autosize. This value is the ratio of air flow at this speed to the maximum air f...'
        },
    )


class AirLoopHVACUnitaryFurnaceHeatCool(IDFBaseModel):
    """Unitary system, heating and cooling with constant volume supply fan
    (continuous or cycling), direct expansion (DX) cooling coil, heating coil
    (gas, electric, hot water, or steam), and optional reheat coil for
    dehumidification control. Identical to AirLoopHVAC:UnitaryHeatCool."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:Unitary:Furnace:HeatCool'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. A schedule value greater than zero (usually 1 i...',
        },
    )
    furnace_air_inlet_node_name: str = Field(...)
    furnace_air_outlet_node_name: str = Field(...)
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the cooling or heating coil). Any other schedule value indicates continuous fan ...',
        },
    )
    maximum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=80.0, json_schema_extra={'units': 'C'}
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate.",
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow fate.",
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate. Only used when fan operating mode is continuous (disregarded for cycling fan mode). This air flow rate is used when no heating or cooling ...",
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply air fan operating mode schedule values not equal to 0).'
        },
    )
    supply_fan_name: FansCVandOnOffRef = Field(
        ..., json_schema_extra={'object_list': ['FansCVandOnOff']}
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    heating_coil_object_type: Literal[
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
    heating_coil_name: HeatingCoilNameRef = Field(
        ..., json_schema_extra={'object_list': ['HeatingCoilName']}
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(..., json_schema_extra={'note': 'Only works with DX cooling coil types'})
    cooling_coil_name: CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'CoolingCoilsDXSingleSpeed',
                    'CoolingCoilsDXVariableSpeed',
                ]
            },
        )
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only Multimode = activate enhanced dehumidification mode as needed and meet sensible load. Valid only with cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted. T...'
        },
    )
    reheat_coil_object_type: (
        Literal[
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Only required if dehumidification control type is "CoolReheat" works with gas, electric, hot water and steam heating coils'
        },
    )
    reheat_coil_name: HeatingCoilNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Only required if dehumidification control type is "CoolReheat"',
        },
    )


class AirLoopHVACUnitaryFurnaceHeatOnly(IDFBaseModel):
    """Unitary system, heating-only with constant volume supply fan (continuous or
    cycling) and heating coil (gas, electric, hot water, or steam). Identical to
    AirLoopHVAC:UnitaryHeatOnly."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:Unitary:Furnace:HeatOnly'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    furnace_air_inlet_node_name: str = Field(...)
    furnace_air_outlet_node_name: str = Field(...)
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the heating coil). Any other schedule value indicates continuous fan mode (suppl...',
        },
    )
    maximum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=80.0, json_schema_extra={'units': 'C'}
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This value should be > 0 and <= than the fan air flow rate.',
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan operating mode schedule values are greater than 0).'
        },
    )
    supply_fan_name: FansCVandOnOffRef = Field(
        ..., json_schema_extra={'object_list': ['FansCVandOnOff']}
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    heating_coil_object_type: Literal[
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
    heating_coil_name: HeatingCoilNameRef = Field(
        ..., json_schema_extra={'object_list': ['HeatingCoilName']}
    )


class AirLoopHVACUnitaryHeatCool(IDFBaseModel):
    """Unitary system, heating and cooling with constant volume supply fan
    (continuous or cycling), direct expansion (DX) cooling coil, heating coil
    (gas, electric, hot water, or steam), and optional reheat coil for
    dehumidification control. Identical to AirLoopHVAC:Unitary:Furnace:HeatCool."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatCool'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    unitary_system_air_inlet_node_name: str = Field(...)
    unitary_system_air_outlet_node_name: str = Field(...)
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the cooling or heating coil). Any other schedule value indicates continuous fan ...',
        },
    )
    maximum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=80.0, json_schema_extra={'units': 'C'}
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate.",
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate.",
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate. Only used when fan operating mode is continuous (disregarded for cycling fan mode). This air flow rate is used when no heating or cooling ...",
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply air fan operating mode schedule values not equal to 0).'
        },
    )
    supply_fan_name: FansCVandOnOffRef = Field(
        ..., json_schema_extra={'object_list': ['FansCVandOnOff']}
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    heating_coil_object_type: Literal[
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
    heating_coil_name: HeatingCoilNameRef = Field(
        ..., json_schema_extra={'object_list': ['HeatingCoilName']}
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Only works with DX cooling coil types or Coil:Cooling:DX:VariableSpeed.'
        },
    )
    cooling_coil_name: CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'CoolingCoilsDXSingleSpeed',
                    'CoolingCoilsDXVariableSpeed',
                ]
            },
        )
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only Multimode = activate enhanced dehumidification mode as needed and meet sensible load. Valid only with cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted. T...'
        },
    )
    reheat_coil_object_type: (
        Literal[
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Only required if dehumidification control type is "CoolReheat" works with gas, electric, desuperheating, hot water and steam heating coils'
        },
    )
    reheat_coil_name: HeatingCoilNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Only required if dehumidification control type is "CoolReheat"',
        },
    )


class AirLoopHVACUnitaryHeatCoolVAVChangeoverBypass(IDFBaseModel):
    """Unitary system, heating and cooling with constant volume supply fan
    (continuous or cycling), direct expansion (DX) cooling coil, heating coil
    (gas, electric, hot water, steam, or DX air-to-air heat pump) and bypass
    damper for variable volume flow to terminal units. Used with
    AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat or
    AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass'
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this unitary system.'}
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Enter the availability schedule name. Schedule ...',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the system air flow rate during cooling operation or specify autosize.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the system air flow rate during heating operation or specify autosize.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when the supply air fan operating mode is continuous (see field Supply air fan operating mode schedule name). This system air flow rate is used when no heating or cooling is required and ...',
        },
    )
    cooling_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the outdoor air flow rate during cooling operation or specify autosize.',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the outdoor air flow rate during heating operation or specify autosize.',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when the supply air fan operating mode is continuous (see field Supply air fan operating mode schedule name). This outdoor air flow rate is used when no heating or cooling is required and...',
        },
    )
    outdoor_air_flow_rate_multiplier_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that contains multipliers for the outdoor air flow rates. Schedule values must be from 0 to 1. If field is left blank, model assumes multiplier is 1 for the entire simu...',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': "Enter the name of the unitary system's air inlet node."
        },
    )
    bypass_duct_mixer_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the name of the bypass duct mixer node. This name should be the name of the return air node for the outdoor air mixer associated with this system. This node name must be different from the ai...'
        },
    )
    bypass_duct_splitter_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the name of the bypass duct splitter node. This splitter air node is the outlet node of the last component in this unitary system. For blow through fan placement, the splitter air node is the...'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': "Enter the name of the unitary system's air outlet node."
        },
    )
    outdoor_air_mixer_object_type: Literal['OutdoorAir:Mixer'] = Field(
        ...,
        json_schema_extra={
            'note': 'currently only one type OutdoorAir:Mixer object is available.'
        },
    )
    outdoor_air_mixer_name: OutdoorAirMixersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['OutdoorAirMixers'],
            'note': 'Enter the name of the outdoor air mixer used with this unitary system.',
        },
    )
    supply_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Specify the type of supply air fan used in this unitary system.'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff', 'FansSystemModel'],
            'note': 'Enter the name of the supply air fan used in this unitary system.',
        },
    )
    supply_air_fan_placement: Literal['BlowThrough', 'DrawThrough'] = Field(
        ...,
        json_schema_extra={
            'note': 'Specify supply air fan placement as either blow through or draw through. BlowThrough means the supply air fan is located before the cooling coil. DrawThrough means the supply air fan is located aft...'
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule to control the supply air fan. Schedule Name values of zero mean that the supply air fan will cycle off if there is no cooling or heating load in any of the zones being...',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Specify the type of cooling coil used in this unitary system.'
        },
    )
    cooling_coil_name: (
        CoolingCoilsDXMultiModeOrSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ],
            'note': 'Enter the name of the cooling coil used in this unitary system.',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:DX:SingleSpeed',
        'Coil:Heating:DX:VariableSpeed',
        'Coil:Heating:Electric',
        'Coil:Heating:Fuel',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'works with DX, gas, electric, hot water and steam heating coils Specify the type of heating coil used in this unitary system.'
        },
    )
    heating_coil_name: HeatingCoilNameRef | HeatingCoilsDXVariableSpeedRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatingCoilName', 'HeatingCoilsDXVariableSpeed'],
            'note': 'Enter the name of the heating coil used in this unitary system.',
        },
    )
    priority_control_mode: (
        Literal[
            '', 'CoolingPriority', 'HeatingPriority', 'LoadPriority', 'ZonePriority'
        ]
        | None
    ) = Field(
        default='ZonePriority',
        json_schema_extra={
            'note': 'CoolingPriority = system provides cooling if any zone requires cooling. HeatingPriority = system provides heating if any zone requires heating. ZonePriority = system controlled based on the total n...'
        },
    )
    minimum_outlet_air_temperature_during_cooling_operation: float | None = Field(
        default=8.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Specify the minimum outlet air temperature allowed for this unitary system during cooling operation. This value should be less than the maximum outlet air temperature during heating operation.',
        },
    )
    maximum_outlet_air_temperature_during_heating_operation: float | None = Field(
        default=50.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Specify the maximum outlet air temperature allowed for this unitary system during heating operation. This value should be greater than the minimum outlet air temperature during cooling operation.',
        },
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only. Multimode = activate enhanced dehumidification mode as needed and meet sensible load. Valid only with Coil:Cooling:DX:TwoStageWithHumidityControlMode. CoolReheat = c...'
        },
    )
    plenum_or_mixer_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of the bypass duct node connected to a plenum or mixer. This field is required when this HVAC System is connected to a plenum or mixer. This is a different node name than that entere...'
        },
    )
    minimum_runtime_before_operating_mode_change: float | None = Field(
        default=0.25,
        ge=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'This is the minimum amount of time the unit operates in cooling or heating mode before changing modes.',
        },
    )


class AirLoopHVACUnitaryHeatOnly(IDFBaseModel):
    """Unitary system, heating-only with constant volume supply fan (continuous or
    cycling) and heating coil (gas, electric, hot water, or steam). Identical to
    AirLoopHVAC:Unitary:Furnace:HeatOnly."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatOnly'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    unitary_system_air_inlet_node_name: str = Field(...)
    unitary_system_air_outlet_node_name: str = Field(...)
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the heating coil). Any other schedule value indicates continuous fan mode (suppl...',
        },
    )
    maximum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=80.0, json_schema_extra={'units': 'C'}
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This value should be > 0 and <= than the fan air flow rate.',
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan operating mode schedule values are greater than 0).'
        },
    )
    supply_fan_name: FansCVandOnOffRef = Field(
        ..., json_schema_extra={'object_list': ['FansCVandOnOff']}
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    heating_coil_object_type: Literal[
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
    heating_coil_name: HeatingCoilNameRef = Field(
        ..., json_schema_extra={'object_list': ['HeatingCoilName']}
    )


class AirLoopHVACUnitaryHeatPumpAirToAir(IDFBaseModel):
    """Unitary heat pump system, heating and cooling, single-speed with supply fan,
    direct expansion (DX) cooling coil, DX heating coil (air-to-air heat pump),
    and supplemental heating coil (gas, electric, hot water, or steam)."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatPump:AirToAir'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. A schedule value greater than zero (usually 1 i...',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    cooling_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate.",
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate.",
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Must be less than or equal to the fan's maximum flow rate. Only used when fan operating mode is continuous (disregarded for cycling fan mode). This air flow rate is used when no heating or cooling ...",
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_air_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Fan:ConstantVolume only works with continuous fan operating mode (i.e. fan operating mode schedule values are greater than 0 or the fan operating mode schedule name field is left blank).'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff'],
            'note': 'Needs to match in the fan object',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:DX:SingleSpeed',
        'Coil:Heating:DX:VariableSpeed',
        'CoilSystem:IntegratedHeatPump:AirSource',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Only works with Coil:Heating:DX:SingleSpeed or Coil:Heating:DX:VariableSpeed or CoilSystem:IntegratedHeatPump:AirSource'
        },
    )
    heating_coil_name: (
        HeatingCoilsDXSingleSpeedRef
        | HeatingCoilsDXVariableSpeedRef
        | IntegratedHeatPumpsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'HeatingCoilsDXSingleSpeed',
                'HeatingCoilsDXVariableSpeed',
                'IntegratedHeatPumps',
            ],
            'note': 'Needs to match in the DX heating coil object',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
        'CoilSystem:IntegratedHeatPump:AirSource',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Only works with Coil:Cooling:DX:SingleSpeed or CoilSystem:Cooling:DX:HeatExchangerAssisted or Coil:Cooling:DX:VariableSpeed or CoilSystem:IntegratedHeatPump:AirSource'
        },
    )
    cooling_coil_name: (
        CoolingCoilsDXSingleSpeedRef
        | CoolingCoilsDXVariableSpeedRef
        | IntegratedHeatPumpsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoolingCoilsDXSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
                'IntegratedHeatPumps',
            ],
            'note': 'Needs to match in the DX cooling coil object',
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
        float | Literal['Autosize']
    ) = Field(..., json_schema_extra={'units': 'C'})
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(default=21.0, le=21.0, json_schema_extra={'units': 'C'})
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the cooling or heating coil). Any other schedule value indicates continuous fan ...',
        },
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only Multimode = activate enhanced dehumidification mode as needed and meet sensible load. Valid only with cooling coil type CoilSystem:Cooling:DX:HeatExchangerAssisted. T...'
        },
    )


class AirLoopHVACUnitaryHeatPumpAirToAirMultiSpeed(IDFBaseModel):
    """Unitary system, heating and cooling, multi-speed with constant volume supply
    fan (continuous or cycling), direct expansion (DX) cooling coil, heating
    coil (DX air-to-air heat pump, gas, electric, hot water, or steam), and
    supplemental heating coil (gas, electric, hot water, or steam)."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed'
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
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_air_fan_object_type: Literal['Fan:ConstantVolume', 'Fan:OnOff'] = Field(
        ...,
        json_schema_extra={
            'note': 'Select the type of supply air fan used in this unitary system.'
        },
    )
    supply_air_fan_name: FansCVandOnOffRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOff'],
            'note': 'Enter the name of the supply air fan used in this unitary system.',
        },
    )
    supply_air_fan_placement: Literal['BlowThrough', 'DrawThrough'] = Field(
        ...,
        json_schema_extra={
            'note': 'Select supply air fan placement as either BlowThrough or DrawThrough. BlowThrough means the supply air fan is located before the cooling coil. DrawThrough means the supply air fan is located after ...'
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule to control the supply air fan. Schedule values of zero mean that the supply air fan will cycle off if there is no cooling or heating load in the control zone. Non-zero ...',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:DX:MultiSpeed',
        'Coil:Heating:Electric:MultiStage',
        'Coil:Heating:Gas:MultiStage',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Multi Speed DX, Electric, Gas, and Single speed Water and Steam coils'
        },
    )
    heating_coil_name: (
        HeatingCoilsDXMultiSpeedRef
        | HeatingCoilsElectricMultiStageRef
        | HeatingCoilsGasMultiStageRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'HeatingCoilsDXMultiSpeed',
                'HeatingCoilsElectricMultiStage',
                'HeatingCoilsGasMultiStage',
            ]
        },
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-8.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Needs to match the corresponding minimum outdoor temperature defined in the DX heating coil object.',
        },
    )
    cooling_coil_object_type: Literal['Coil:Cooling:DX:MultiSpeed'] = Field(
        ..., json_schema_extra={'note': 'Only works with Coil:Cooling:DX:MultiSpeed'}
    )
    cooling_coil_name: CoolingCoilsDXMultiSpeedRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingCoilsDXMultiSpeed'],
            'note': 'Needs to match in the DX Cooling Coil object',
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
            'note': 'works with gas, electric, hot water and steam heating coils'
        },
    )
    supplemental_heating_coil_name: HeatingCoilNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Needs to match in the supplemental heating coil object',
        },
    )
    maximum_supply_air_temperature_from_supplemental_heater: (
        float | Literal['Autosize'] | None
    ) = Field(default=None, json_schema_extra={'units': 'C'})
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(default=21.0, le=21.0, json_schema_extra={'units': 'C'})
    auxiliary_on_cycle_electric_power: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    auxiliary_off_cycle_electric_power: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    design_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If non-zero, then the heat recovery inlet and outlet node names must be entered. Used for heat recovery to an EnergyPlus plant loop.',
        },
    )
    maximum_temperature_for_heat_recovery: float | None = Field(
        default=80.0, ge=0.0, le=100.0, json_schema_extra={'units': 'C'}
    )
    heat_recovery_water_inlet_node_name: str | None = Field(default=None)
    heat_recovery_water_outlet_node_name: str | None = Field(default=None)
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when the supply air fan operating mode is continuous (see field Supply Air Fan Operating Mode Schedule Name). This air flow rate is used when no heating or cooling is required and the coi...',
        },
    )
    number_of_speeds_for_heating: int = Field(
        ...,
        ge=1,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for air flow rates. If Heating Coil Object Type is Coil:Heating:Water or Coil:Heating:Steam, this field should be 1.'
        },
    )
    number_of_speeds_for_cooling: int = Field(
        ...,
        ge=2,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for air flow rates.'
        },
    )
    heating_speed_1_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during heating operation or specify autosize.',
        },
    )
    heating_speed_2_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during heating operation or specify autosize.',
        },
    )
    heating_speed_3_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during heating operation or specify autosize.',
        },
    )
    heating_speed_4_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during heating operation or specify autosize.',
        },
    )
    cooling_speed_1_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during cooling operation or specify autosize.',
        },
    )
    cooling_speed_2_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during cooling operation or specify autosize.',
        },
    )
    cooling_speed_3_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during cooling operation or specify autosize.',
        },
    )
    cooling_speed_4_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the operating supply air flow rate during cooling operation or specify autosize.',
        },
    )


class AirLoopHVACUnitaryHeatPumpWaterToAir(IDFBaseModel):
    """Unitary heat pump system, heating and cooling, single-speed with constant
    volume supply fan (continuous or cycling), direct expansion (DX) cooling
    coil, DX heating coil (water-to-air heat pump), and supplemental heating
    coil (gas, electric, hot water, or steam)."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitaryHeatPump:WaterToAir'
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
    supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This value should be > 0 and <= than the fan air flow rate.',
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_air_fan_object_type: Literal['Fan:OnOff'] = Field(
        ..., json_schema_extra={'note': 'Only works with On/Off Fan'}
    )
    supply_air_fan_name: FansOnOffRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff'],
            'note': 'Needs to match Fan:OnOff object',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:WaterToAirHeatPump:EquationFit',
        'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
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
    heating_convergence: float | None = Field(default=0.001, gt=0.0)
    cooling_coil_object_type: Literal[
        'Coil:Cooling:WaterToAirHeatPump:EquationFit',
        'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
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
    cooling_convergence: float | None = Field(default=0.001, gt=0.0)
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
        float | Literal['Autosize']
    ) = Field(..., json_schema_extra={'units': 'C'})
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
    dehumidification_control_type: Literal['', 'CoolReheat', 'None'] | None = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint. as required to meet the humidity setpoint. Valid only with Coil:Cooling:WaterToAirHeatPump:EquationFit or Coil:Cooling...'
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


class AirLoopHVACUnitarySystem(IDFBaseModel):
    """AirloopHVAC:UnitarySystem is a generic HVAC system type that allows any
    configuration of coils and/or fan. This object is a replacement of other
    AirloopHVAC objects. This object can be used in outdoor air systems, outdoor
    air units, air loops, and as zone equipment if desired."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:UnitarySystem'
    name: str = Field(
        ..., json_schema_extra={'note': 'Unique name for the Unitary System.'}
    )
    control_type: Literal['', 'Load', 'SetPoint', 'SingleZoneVAV'] | None = Field(
        default='Load',
        json_schema_extra={
            'note': 'Load control requires a Controlling Zone name. SetPoint control requires set points at coil outlet node. SingleZoneVAV also requires a Controlling Zone name and allows load control at low speed fan...'
        },
    )
    controlling_zone_or_thermostat_location: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Used only for Load based control Zone name where thermostat is located. Required when Control Type = Load.',
        },
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only. Required when Control Type = SingleZoneVAV. Multimode = activate enhanced dehumidification mode as needed and meet sensible load. Valid only with cooling coil type C...'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. A schedule value greater than zero (usually 1 i...',
        },
    )
    air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the node name used as the inlet air node for the unitary system.'
        },
    )
    air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the node name used as the outlet air node for the unitary system.'
        },
    )
    supply_fan_object_type: (
        Literal[
            'Fan:ComponentModel',
            'Fan:ConstantVolume',
            'Fan:OnOff',
            'Fan:SystemModel',
            'Fan:VariableVolume',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of supply air fan if included in the unitary system. Fan:ConstantVolume only works with continuous fan operating mode (i.e. supply air fan operating mode schedule values greater than...'
        },
    )
    supply_fan_name: FansRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['Fans'],
            'note': 'Enter the name of the supply air fan if included in the unitary system.',
        },
    )
    fan_placement: Literal['BlowThrough', 'DrawThrough'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of supply air fan if included in the unitary system.'
        },
    )
    supply_air_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A fan operating mode schedule value of 0 indicates cycling fan mode (supply air fan cycles on and off in tandem with the cooling or heating coil). Any other schedule value indicates continuous fan ...',
        },
    )
    heating_coil_object_type: (
        Literal[
            'Coil:Heating:DX:MultiSpeed',
            'Coil:Heating:DX:SingleSpeed',
            'Coil:Heating:DX:VariableSpeed',
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Electric:MultiStage',
            'Coil:Heating:Fuel',
            'Coil:Heating:Gas:MultiStage',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'Coil:Heating:WaterToAirHeatPump:EquationFit',
            'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
            'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
            'Coil:UserDefined',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of heating coil if included in the unitary system.'
        },
    )
    heating_coil_name: (
        HeatingCoilNameRef
        | HeatingCoilsDXRef
        | HeatingCoilsDXMultiSpeedRef
        | HeatingCoilsDXVariableSpeedRef
        | HeatingCoilsDesuperheaterRef
        | HeatingCoilsElectricMultiStageRef
        | HeatingCoilsGasMultiStageRef
        | HeatingCoilsWaterToAirHPRef
        | HeatingCoilsWaterToAirVSHPRef
        | UserDefinedCoilRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'HeatingCoilName',
                'HeatingCoilsDX',
                'HeatingCoilsDXMultiSpeed',
                'HeatingCoilsDXVariableSpeed',
                'HeatingCoilsDesuperheater',
                'HeatingCoilsElectricMultiStage',
                'HeatingCoilsGasMultiStage',
                'HeatingCoilsWaterToAirHP',
                'HeatingCoilsWaterToAirVSHP',
                'UserDefinedCoil',
            ],
            'note': 'Enter the name of the heating coil if included in the unitary system.',
        },
    )
    dx_heating_coil_sizing_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Used to adjust heat pump heating capacity with respect to DX cooling capacity used only for heat pump configurations (i.e., a DX cooling and DX heating coil is used).'
        },
    )
    cooling_coil_object_type: (
        Literal[
            'Coil:Cooling:DX',
            'Coil:Cooling:DX:MultiSpeed',
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'Coil:Cooling:DX:TwoSpeed',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'Coil:Cooling:DX:VariableSpeed',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Cooling:WaterToAirHeatPump:EquationFit',
            'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
            'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
            'Coil:UserDefined',
            'CoilSystem:Cooling:DX:HeatExchangerAssisted',
            'CoilSystem:Cooling:Water:HeatExchangerAssisted',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of cooling coil if included in the unitary system.'
        },
    )
    cooling_coil_name: (
        CoilCoolingDXRef
        | CoolingCoilsDXRef
        | CoolingCoilsDXMultiSpeedRef
        | CoolingCoilsDXVariableSpeedRef
        | CoolingCoilsWaterRef
        | CoolingCoilsWaterToAirHPRef
        | CoolingCoilsWaterToAirVSHPRef
        | UserDefinedCoilRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'CoolingCoilsDX',
                'CoolingCoilsDXMultiSpeed',
                'CoolingCoilsDXVariableSpeed',
                'CoolingCoilsWater',
                'CoolingCoilsWaterToAirHP',
                'CoolingCoilsWaterToAirVSHP',
                'UserDefinedCoil',
            ],
            'note': 'Enter the name of the cooling coil if included in the unitary system.',
        },
    )
    use_doas_dx_cooling_coil: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'If Yes, the DX cooling coil runs as 100% DOAS DX coil. If No, the DX cooling coil runs as a regular DX coil. If left blank the default is regular dx coil.'
        },
    )
    minimum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'When Use DOAS DX Cooling Coil is specified as Yes, Minimum Supply Air Temperature defines the minimum DOAS DX cooling coil leaving air temperature that should be maintained to avoid frost formation...',
        },
    )
    latent_load_control: (
        Literal[
            '',
            'LatentOnlyLoadControl',
            'LatentOrSensibleLoadControl',
            'LatentWithSensibleLoadControl',
            'SensibleOnlyLoadControl',
        ]
        | None
    ) = Field(
        default='SensibleOnlyLoadControl',
        json_schema_extra={
            'note': 'SensibleOnlyLoadControl is selected when thermostat or SingleZoneVAV control is used. LatentOnlyLoadControl is selected when humidistat control is used. LatentWithSensibleLoadControl is selected wh...'
        },
    )
    supplemental_heating_coil_object_type: (
        Literal[
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Electric:Multistage',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'Coil:UserDefined',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of supplemental heating or reheat coil if included in the unitary system. Only required if dehumidification control type is "CoolReheat". This coil supplements heating mode operation...'
        },
    )
    supplemental_heating_coil_name: (
        HeatingCoilNameRef
        | HeatingCoilsDesuperheaterRef
        | HeatingCoilsElectricMultiStageRef
        | UserDefinedCoilRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'HeatingCoilName',
                'HeatingCoilsDesuperheater',
                'HeatingCoilsElectricMultiStage',
                'UserDefinedCoil',
            ],
            'note': 'Enter the name of the supplemental heating coil if included in the unitary system. Only required if dehumidification control type is "CoolReheat".',
        },
    )
    cooling_supply_air_flow_rate_method: (
        Literal[
            'FlowPerCoolingCapacity',
            'FlowPerFloorArea',
            'FractionOfAutosizedCoolingValue',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the method used to determine the cooling supply air volume flow rate. None is used when a cooling coil is not included in the unitary system or this field may be blank. SupplyAirFlowRate is s...'
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of the supply air volume flow rate during cooling operation. Required field when Cooling Supply Air Flow Rate Method is SupplyAirFlowRate. This field may be blank if a cooling c...',
        },
    )
    cooling_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the supply air volume flow rate per total floor area fraction. Required field when Cooling Supply Air Flow Rate Method is FlowPerFloorArea. This field may be blank if a cooling coil is not in...',
        },
    )
    cooling_fraction_of_autosized_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when Cooling Supply Air Flow Rate Method is FractionOfAutosizedCoolingValue. This field may b...'
        },
    )
    cooling_supply_air_flow_rate_per_unit_of_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling capacity. Required field when Cooling Supply Air Flow Rate Method is FlowPerCoolingCapacity. This field may be blank if a cooling ...',
        },
    )
    heating_supply_air_flow_rate_method: (
        Literal[
            'FlowPerFloorArea',
            'FlowPerHeatingCapacity',
            'FractionOfAutosizedHeatingValue',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the method used to determine the heating supply air volume flow rate. None is used when a heating coil is not included in the unitary system or this field may be blank. SupplyAirFlowRate is s...'
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of the supply air volume flow rate during heating operation. Required field when Heating Supply Air Flow Rate Method is SupplyAirFlowRate. This field may be blank if a heating c...',
        },
    )
    heating_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the supply air volume flow rate per total floor area fraction. Required field when Heating Supply Air Flow Rate Method is FlowPerFloorArea. This field may be blank if a heating coil is not in...',
        },
    )
    heating_fraction_of_autosized_heating_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the heating supply air flow rate. Required field when Heating Supply Air Flow Rate Method is FractionOfAutosizedHeatingValue. This field may b...'
        },
    )
    heating_supply_air_flow_rate_per_unit_of_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate as a fraction of the heating capacity. Required field when Heating Supply Air Flow Rate Method is FlowPerHeatingCapacity. This field may be blank if a heating ...',
        },
    )
    no_load_supply_air_flow_rate_method: (
        Literal[
            'FlowPerCoolingCapacity',
            'FlowPerFloorArea',
            'FlowPerHeatingCapacity',
            'FractionOfAutosizedCoolingValue',
            'FractionOfAutosizedHeatingValue',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the method used to determine the supply air volume flow rate when no cooling or heating is required. None is used when a cooling and heating coil is not included in the unitary system or this...'
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of the supply air volume flow rate during when no cooling or heating is required. Required field when No Load Supply Air Flow Rate Method is SupplyAirFlowRate.',
        },
    )
    no_load_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the supply air volume flow rate per total floor area fraction. Required field when No Load Supply Air Flow Rate Method is FlowPerFloorArea.',
        },
    )
    no_load_fraction_of_autosized_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when No Load Supply Air Flow Rate Method is FractionOfAutosizedCoolingValue.'
        },
    )
    no_load_fraction_of_autosized_heating_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the heating supply air flow rate. Required field when No Load Supply Air Flow Rate Method is FractionOfAutosizedHeatingValue.'
        },
    )
    no_load_supply_air_flow_rate_per_unit_of_capacity_during_cooling_operation: (
        float | None
    ) = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling capacity. Required field when No Load Supply Air Flow Rate Method is FlowPerCoolingCapacity.',
        },
    )
    no_load_supply_air_flow_rate_per_unit_of_capacity_during_heating_operation: (
        float | None
    ) = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate as a fraction of the heating capacity. Required field when No Load Supply Air Flow Rate Method is FlowPerHeatingCapacity.',
        },
    )
    no_load_supply_air_flow_rate_control_set_to_low_speed: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'This field is not used when Design Specification Multispeed Object Type input is present When Yes is selected the minimum air flow rate is used. When No is selected the maximum air flow rate is used.'
        },
    )
    maximum_supply_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default=80.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum supply air temperature leaving the heating coil. When Control Type = SingleZoneVAV, enter the maximum air temperature limit for reduced fan speed.',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_supplemental_heater_operation: (
        float | None
    ) = Field(
        default=21.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dry-bulb temperature for supplemental heater operation.',
        },
    )
    outdoor_dry_bulb_temperature_sensor_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If this field is blank, outdoor temperature from the weather file is used. If this field is not blank, the node name specified determines the outdoor temperature used for controlling supplemental h...'
        },
    )
    ancillary_on_cycle_electric_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the value of ancillary electric power for controls or other devices consumed during the on cycle.',
        },
    )
    ancillary_off_cycle_electric_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the value of ancillary electric power for controls or other devices consumed during the off cycle.',
        },
    )
    design_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If non-zero, then the heat recovery inlet and outlet node names must be entered. Used for heat recovery to an EnergyPlus plant loop.',
        },
    )
    maximum_temperature_for_heat_recovery: float | None = Field(
        default=80.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum heat recovery inlet temperature allowed for heat recovery.',
        },
    )
    heat_recovery_water_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of the heat recovery water inlet node if plant water loop connections are present.'
        },
    )
    heat_recovery_water_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of the heat recovery water outlet node if plant water loop connections are present.'
        },
    )
    design_specification_multispeed_object_type: (
        Literal['UnitarySystemPerformance:Multispeed'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the type of performance specification object used to describe the multispeed coil.'
        },
    )
    design_specification_multispeed_object_name: (
        UnitarySystemPerformanceNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnitarySystemPerformanceNames'],
            'note': 'The name of the performance specification object used to describe the multispeed coil.',
        },
    )


class UnitarySystemPerformanceMultispeed(IDFBaseModel):
    """The UnitarySystemPerformance object is used to specify the air flow ratio at
    each operating speed. This object is primarily used for multispeed DX and
    water coils to allow operation at alternate flow rates different from those
    specified in the coil object."""

    _idf_object_type: ClassVar[str] = 'UnitarySystemPerformance:Multispeed'
    name: str = Field(...)
    number_of_speeds_for_heating: int = Field(
        ...,
        ge=0,
        le=10,
        json_schema_extra={
            'note': 'Used only for Multi speed coils Enter the number of the following sets of data for air flow rates.'
        },
    )
    number_of_speeds_for_cooling: int = Field(
        ...,
        ge=0,
        le=10,
        json_schema_extra={
            'note': 'Used only for Multi speed coils Enter the number of the following sets of data for air flow rates.'
        },
    )
    single_mode_operation: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Controls coil operation during each HVAC timestep. This choice does not apply to speed 1 operation. Yes = operate at the highest speed possible without exceeding the current load. No = allow operat...'
        },
    )
    no_load_supply_air_flow_rate_ratio: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Used to define the no load operating air flow rate when the system fan is specified to operate continuously.'
        },
    )
    flow_ratios: list[UnitarySystemPerformanceMultispeedFlowRatiosItem] | None = Field(
        default=None
    )
