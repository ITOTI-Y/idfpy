"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Evaporative Coolers
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ScheduleNamesRef,
    UnivariateFunctionsRef,
    WaterStorageTankNamesRef,
)


class EvaporativeCoolerDirectCelDekPad(IDFBaseModel):
    """Direct evaporative cooler with rigid media evaporative pad and recirculating
    water pump. This model has no controls other than its availability schedule."""

    _idf_object_type: ClassVar[str] = 'EvaporativeCooler:Direct:CelDekPad'
    name: str | None = Field(default=None)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    direct_pad_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm2'}
    )
    direct_pad_depth: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm'}
    )
    recirculating_water_pump_power_consumption: float = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    control_type: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This field is not currently used and can be left blank'
        },
    )
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )


class EvaporativeCoolerDirectResearchSpecial(IDFBaseModel):
    """Direct evaporative cooler with user-specified effectiveness (can represent
    rigid pad or similar media), and recirculating water pump, and secondary air
    fan. This model is controlled to meet the primary air outlet temperature
    setpoint."""

    _idf_object_type: ClassVar[str] = 'EvaporativeCooler:Direct:ResearchSpecial'
    name: str | None = Field(default=None)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    cooler_design_effectiveness: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={'note': 'effectiveness with respect to wet-bulb depression'},
    )
    effectiveness_flow_ratio_modifier_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the design effectiveness in the previous field by multiplying the value by the result of this curve. The effectiveness flow modifier curve is a function of flow fraction. Flow f...',
        },
    )
    primary_air_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    recirculating_water_pump_design_power: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'This is the design water pump or spray for evaporation at the primary air design air flow rates and cooler design effectiveness',
            },
        )
    )
    water_pump_power_sizing_factor: float | None = Field(
        default=90.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'This field is used when the previous field is set to autosize. The pump power is scaled with Primary Air Design Air Flow Rate. This value was backed out from inputs in energy plus example files. Av...',
        },
    )
    water_pump_power_modifier_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the pump power in the previous field by multiplying the design power by the result of this curve. x = ff = flow fraction on the primary air. The flow fraction is the primary air...',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    sensor_node_name: str = Field(...)
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    drift_loss_fraction: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Rate of drift loss as a fraction of evaporated water flow rate'
        },
    )
    blowdown_concentration_ratio: float | None = Field(
        default=None,
        ge=2.0,
        json_schema_extra={
            'note': 'Characterizes the rate of blowdown in the evaporative cooler. Blowdown is water intentionally drained from the cooler in order to offset the build up of solids in the water that would otherwise occ...'
        },
    )
    evaporative_operation_minimum_drybulb_temperature: float | None = Field(
        default=None,
        ge=-99.0,
        json_schema_extra={
            'note': 'This numeric field defines the evaporative cooler air inlet node drybulb temperature minimum limit in degrees Celsius. The evaporative cooler will be turned off when the evaporator cooler air inlet...'
        },
    )
    evaporative_operation_maximum_limit_wetbulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'when outdoor wetbulb temperature rises above this limit the cooler shuts down. This numeric field defines the evaporative cooler air inlet node wet-bulb temperature maximum limit in degrees Celsius...'
        },
    )
    evaporative_operation_maximum_limit_drybulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This numeric field defines the evaporative cooler air inlet node dry-bulb temperature maximum limit in degrees Celsius. The evaporative cooler will be turned off when its air inlet node drybulb tem...'
        },
    )


class EvaporativeCoolerIndirectCelDekPad(IDFBaseModel):
    """Indirect evaporative cooler with rigid media evaporative pad, recirculating
    water pump, and secondary air fan. This model has no controls other than its
    availability schedule."""

    _idf_object_type: ClassVar[str] = 'EvaporativeCooler:Indirect:CelDekPad'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    direct_pad_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm2'}
    )
    direct_pad_depth: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm'}
    )
    recirculating_water_pump_power_consumption: float = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    secondary_air_fan_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    secondary_air_fan_total_efficiency: float | None = Field(
        default=None, le=1.0, gt=0.0
    )
    secondary_air_fan_delta_pressure: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    indirect_heat_exchanger_effectiveness: float = Field(..., ge=0.0)
    primary_air_inlet_node_name: str = Field(...)
    primary_air_outlet_node_name: str = Field(...)
    control_type: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This field is not currently used and can be left blank'
        },
    )
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    secondary_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={'note': 'Enter the name of an outdoor air node'},
    )


class EvaporativeCoolerIndirectResearchSpecial(IDFBaseModel):
    """Indirect evaporative cooler with user-specified effectiveness (can represent
    rigid pad or wetted coil), recirculating water pump, and secondary air fan.
    This model is controlled to meet the primary air outlet temperature
    setpoint."""

    _idf_object_type: ClassVar[str] = 'EvaporativeCooler:Indirect:ResearchSpecial'
    name: str | None = Field(default=None)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    cooler_wetbulb_design_effectiveness: float = Field(
        ...,
        ge=0.0,
        le=2.0,
        json_schema_extra={
            'note': 'wet operation effectiveness with respect to wetbulb depression this is the nominal design wetbulb effectiveness at design air flow rates and water rate'
        },
    )
    wetbulb_effectiveness_flow_ratio_modifier_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the wetbulb effectiveness in the previous field (eff_wb_design) by multiplying the value by the result of this curve, eff_wb = eff_wb_design * func(HXFlowRatio) x = HXFlowRatio ...',
        },
    )
    cooler_drybulb_design_effectiveness: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'dry operation effectiveness with respect to drybulb temperature difference this is the nominal design drybulb effectiveness at design air flow rates, no evaporation water active'
        },
    )
    drybulb_effectiveness_flow_ratio_modifier_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the drybulb effectiveness in the previous field (eff_db_design) by multiplying the value by the result of this curve, eff_db = eff_db_design * f(HXFlowRatio) x = HXFlowRatio = s...',
        },
    )
    recirculating_water_pump_design_power: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'This is the nominal design pump power of water recirculation and spray for evaporation at design air flow rates and cooler design effectiveness',
            },
        )
    )
    water_pump_power_sizing_factor: float | None = Field(
        default=90.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'This field is used when the previous field is set to autosize. The pump power is scaled with Secondary Air Design Air Flow Rate. This value was backed out from inputs in energy plus example files. ...',
        },
    )
    water_pump_power_modifier_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the pump power in the previous field by multiplying the design power by the result of this curve. x = ff = flow fraction on the secondary side, secondary air flow rate during op...',
        },
    )
    secondary_air_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    secondary_air_flow_scaling_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This field is used when the previous field is set to autosize. The Primary Design Air Flow Rate is scaled using this factor to calculate the secondary design air flow rate.',
        },
    )
    secondary_air_fan_design_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'This is the fan design power at Secondary Design Air Flow Rate. This is the nominal design power at full speed.',
        },
    )
    secondary_air_fan_sizing_specific_power: float | None = Field(
        default=250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'This field is used when the previous field is set to autosize. The fan power is scaled with Secondary Air Design Flow Rate. The default value is estimated from 125 Pa fan total pressure and fan tot...',
        },
    )
    secondary_air_fan_power_modifier_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'this curve modifies the design fan power in the previous field by multiplying the value by the result of this curve. It should have a value of 1.0 at a x = 1.0. x = ff = flow fraction on the second...',
        },
    )
    primary_air_inlet_node_name: str = Field(...)
    primary_air_outlet_node_name: str = Field(...)
    primary_air_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    dewpoint_effectiveness_factor: float | None = Field(default=None, ge=0.0)
    secondary_air_inlet_node_name: str = Field(...)
    secondary_air_outlet_node_name: str = Field(...)
    sensor_node_name: str = Field(...)
    relief_air_inlet_node_name: str | None = Field(default=None)
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    drift_loss_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'note': 'Rate of drift loss as a fraction of evaporated water flow rate. If this input field is left blank, then zero drift loss is assumed.'
        },
    )
    blowdown_concentration_ratio: float | None = Field(
        default=None,
        ge=2.0,
        json_schema_extra={
            'note': 'Characterizes the rate of blowdown in the evaporative cooler. Blowdown is water intentionally drained from the cooler in order to offset the build up of solids in the water that would otherwise occ...'
        },
    )
    evaporative_operation_minimum_limit_secondary_air_drybulb_temperature: (
        float | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'This input field value defines the secondary air inlet node drybulb temperature limits in degreeCelsius. When the secondary side entering air dry bulb temperature drops below this limit, then the e...'
        },
    )
    evaporative_operation_maximum_limit_outdoor_wetbulb_temperature: float | None = (
        Field(
            default=None,
            json_schema_extra={
                'note': 'This input field value defines the secondary air inlet node wetbulb temperature limits in degree Celsius. When the secondary side entering air wet bulb temperature exceeds this limit, then the evap...'
            },
        )
    )
    dry_operation_maximum_limit_outdoor_drybulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This input field value defines the secondary air inlet node drybulb temperature limits in degree Celsius. When the secondary side entering air drybulb temperature exceeds this limit, then the evapo...'
        },
    )


class EvaporativeCoolerIndirectWetCoil(IDFBaseModel):
    """Indirect evaporative cooler with wetted coil, recirculating water pump, and
    secondary air fan. This model has no controls other than its availability
    schedule."""

    _idf_object_type: ClassVar[str] = 'EvaporativeCooler:Indirect:WetCoil'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    coil_maximum_efficiency: float = Field(..., ge=0.0, le=1.0)
    coil_flow_ratio: float | None = Field(default=None)
    recirculating_water_pump_power_consumption: float = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    secondary_air_fan_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    secondary_air_fan_total_efficiency: float = Field(..., le=1.0, gt=0.0)
    secondary_air_fan_delta_pressure: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    primary_air_inlet_node_name: str = Field(...)
    primary_air_outlet_node_name: str = Field(...)
    control_type: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This field is not currently used and can be left blank'
        },
    )
    water_supply_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    secondary_air_inlet_node_name: str = Field(
        ..., json_schema_extra={'note': 'Enter the name of an outdoor air node'}
    )
