"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Water Heaters and Thermal Storage
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    FansOnOffRef,
    FansSystemModelRef,
    HeatPumpWaterHeaterDXCoilsPumpedRef,
    HeatPumpWaterHeaterDXCoilsVariableSpeedRef,
    HeatPumpWaterHeaterDXCoilsWrappedRef,
    IntegratedHeatPumpsRef,
    ScheduleNamesRef,
    UnivariateFunctionsRef,
    WaterHeaterNamesRef,
    WaterHeaterStratifiedNamesRef,
    ZoneNamesRef,
)


class ThermalStorageChilledWaterMixed(IDFBaseModel):
    """Chilled water storage with a well-mixed, single-node tank. The chilled water
    is \"used\" by drawing from the \"Use Side\" of the water tank. The tank is
    indirectly charged by circulating cold water through the \"Source Side\" of
    the water tank."""

    _idf_object_type: ClassVar[str] = 'ThermalStorage:ChilledWater:Mixed'
    name: str = Field(...)
    tank_volume: float | None = Field(
        default=0.1, gt=0.0, json_schema_extra={'units': 'm3'}
    )
    setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    deadband_temperature_difference: float | None = Field(
        default=0.5, gt=0.0, json_schema_extra={'units': 'deltaC'}
    )
    minimum_temperature_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    nominal_cooling_capacity: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    ambient_temperature_indicator: Literal['Outdoors', 'Schedule', 'Zone'] = Field(...)
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ambient_temperature_zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    ambient_temperature_outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required when field Ambient Temperature Indicator=Outdoors'
        },
    )
    heat_gain_coefficient_from_ambient_temperature: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/K'}
    )
    use_side_inlet_node_name: str | None = Field(default=None)
    use_side_outlet_node_name: str | None = Field(default=None)
    use_side_heat_transfer_effectiveness: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    use_side_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for use side. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    use_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    source_side_inlet_node_name: str | None = Field(default=None)
    source_side_outlet_node_name: str | None = Field(default=None)
    source_side_heat_transfer_effectiveness: float | None = Field(
        default=1.0, le=1.0, gt=0.0
    )
    source_side_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for source side. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    source_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    tank_recovery_time: float | None = Field(
        default=4.0,
        gt=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Parameter for autosizing design flow rates for indirectly cooled water tanks time required to lower temperature of entire tank from 14.4C to 9.0C',
        },
    )


class ThermalStorageChilledWaterStratified(IDFBaseModel):
    """Chilled water storage with a stratified, multi-node tank. The chilled water
    is \"used\" by drawing from the \"Use Side\" of the water tank. The tank is
    indirectly charged by circulating cold water through the \"Source Side\" of
    the water tank."""

    _idf_object_type: ClassVar[str] = 'ThermalStorage:ChilledWater:Stratified'
    name: str = Field(...)
    tank_volume: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3'})
    tank_height: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height is measured in the axial direction for horizontal cylinders',
        },
    )
    tank_shape: (
        Literal['', 'HorizontalCylinder', 'Other', 'VerticalCylinder'] | None
    ) = Field(default='VerticalCylinder')
    tank_perimeter: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Only used if Tank Shape is Other'},
    )
    setpoint_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    deadband_temperature_difference: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    temperature_sensor_height: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm'}
    )
    minimum_temperature_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    nominal_cooling_capacity: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    ambient_temperature_indicator: Literal['Outdoors', 'Schedule', 'Zone'] = Field(...)
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ambient_temperature_zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    ambient_temperature_outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required for Ambient Temperature Indicator=Outdoors'
        },
    )
    uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2-K'})
    )
    use_side_inlet_node_name: str | None = Field(default=None)
    use_side_outlet_node_name: str | None = Field(default=None)
    use_side_heat_transfer_effectiveness: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': "The use side effectiveness in the stratified tank model is a simplified analogy of a heat exchanger's effectiveness. This effectiveness is equal to the fraction of use mass flow rate that directly ..."
        },
    )
    use_side_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for use side. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    use_side_inlet_height: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={'units': 'm', 'note': 'Defaults to top of tank'},
    )
    use_side_outlet_height: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Defaults to bottom of tank'},
    )
    use_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    source_side_inlet_node_name: str | None = Field(default=None)
    source_side_outlet_node_name: str | None = Field(default=None)
    source_side_heat_transfer_effectiveness: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': "The source side effectiveness in the stratified tank model is a simplified analogy of a heat exchanger's effectiveness. This effectiveness is equal to the fraction of source mass flow rate that dir..."
        },
    )
    source_side_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for use side. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    source_side_inlet_height: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Defaults to bottom of tank'},
    )
    source_side_outlet_height: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={'units': 'm', 'note': 'Defaults to top of tank'},
    )
    source_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    tank_recovery_time: float | None = Field(
        default=4.0,
        gt=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Parameter for autosizing design flow rates for indirectly cooled water tanks time required to lower temperature of entire tank from 14.4C to 9.0C',
        },
    )
    inlet_mode: Literal['', 'Fixed', 'Seeking'] | None = Field(default='Fixed')
    number_of_nodes: int | None = Field(default=1, ge=1, le=10)
    additional_destratification_conductivity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    node_1_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_2_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_3_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_4_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_5_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_6_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_7_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_8_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_9_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_10_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )


class ThermalStorageIceDetailed(IDFBaseModel):
    """This input syntax is intended to describe a thermal storage system that
    includes smaller containers filled with water that are placed in a larger
    tank or series of tanks. The model uses polynomial equations to describe the
    system performance."""

    _idf_object_type: ClassVar[str] = 'ThermalStorage:Ice:Detailed'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    capacity: float = Field(
        ...,
        json_schema_extra={
            'units': 'GJ',
            'note': 'This includes only the latent storage capacity',
        },
    )
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    discharging_curve_variable_specifications: Literal[
        'FractionChargedLMTD',
        'FractionDischargedLMTD',
        'LMTDFractionCharged',
        'LMTDMassFlow',
    ] = Field(...)
    discharging_curve_name: BivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['BivariateFunctions']}
    )
    charging_curve_variable_specifications: Literal[
        'FractionChargedLMTD',
        'FractionDischargedLMTD',
        'LMTDFractionCharged',
        'LMTDMassFlow',
    ] = Field(...)
    charging_curve_name: BivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['BivariateFunctions']}
    )
    timestep_of_the_curve_data: float | None = Field(
        default=None, json_schema_extra={'units': 'hr'}
    )
    parasitic_electric_load_during_discharging: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    parasitic_electric_load_during_charging: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    tank_loss_coefficient: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This is the fraction the total storage capacity that is lost or melts each hour',
        },
    )
    freezing_temperature_of_storage_medium: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This temperature is typically 0C for water. Simply changing this temperature without adjusting the performance parameters input above is inappropriate and not advised.',
        },
    )
    thaw_process_indicator: Literal['', 'InsideMelt', 'OutsideMelt'] | None = Field(
        default='OutsideMelt',
        json_schema_extra={
            'note': 'This field determines whether the system uses internal or external melt during discharging. This will then have an impact on charging performance.'
        },
    )


class ThermalStorageIceSimple(IDFBaseModel):
    """This ice storage model is a simplified model It requires a setpoint placed
    on the Chilled Water Side Outlet Node It should be placed in the chilled
    water supply side outlet branch followed by a pipe. Use the
    PlantEquipmentOperation:ComponentSetpoint plant operation scheme."""

    _idf_object_type: ClassVar[str] = 'ThermalStorage:Ice:Simple'
    name: str = Field(...)
    ice_storage_type: Literal['IceOnCoilExternal', 'IceOnCoilInternal'] = Field(
        ...,
        json_schema_extra={
            'note': 'IceOnCoilInternal = Ice-on-Coil, internal melt IceOnCoilExternal = Ice-on-Coil, external melt'
        },
    )
    capacity: float = Field(..., json_schema_extra={'units': 'GJ'})
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)


class WaterHeaterHeatPumpPumpedCondenser(IDFBaseModel):
    """This object models an air-source heat pump for water heating where the water
    is pumped out of the tank, through a heating coil and returned to the tank.
    For wrapped condenser HPWHs, see WaterHeater:HeatPump:WrappedCondenser.
    WaterHeater:HeatPump:PumpedCondenser is a compound object that references
    other component objects - Coil:WaterHeating:AirToWaterHeatPump:*, Fan:OnOff,
    WaterHeater:Mixed or WaterHeater:Stratified"""

    _idf_object_type: ClassVar[str] = 'WaterHeater:HeatPump:PumpedCondenser'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a heat pump water heater.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the heat pump compr...',
        },
    )
    compressor_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': "Defines the cut-out temperature where the heat pump compressor turns off. The heat pump compressor setpoint temperature should always be greater than the water tank's heater (element or burner) set...",
        },
    )
    dead_band_temperature_difference: float | None = Field(
        default=5.0,
        le=20.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Setpoint temperature minus the dead band temperature difference defines the cut-in temperature where the heat pump compressor turns on. The water tank's heater (element or burner) setpoint temperat...",
        },
    )
    condenser_water_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Should match the field Source Outlet Node Name in the water heater tank object. Should also match the Condenser Water Inlet Node Name in the associated DX coil object.'
        },
    )
    condenser_water_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Should match the field Source Inlet Node Name in water heater tank object. Should also match the Condenser Water Outlet Node Name in the associated DX Coil object.'
        },
    )
    condenser_water_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Actual water flow rate through the heat pump's water coil (condenser). If autocalculated, the water flow rate is set equal to 4.487E-8 m3/s/W times the rated heating capacity of the heat pump's DX ...",
        },
    )
    evaporator_air_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Actual air flow rate across the heat pump's air coil (evaporator). If autocalculated, the air flow rate is set equal to 5.035E-5 m3/s/W times the rated heating capacity of the heat pump's DX coil.",
        },
    )
    inlet_air_configuration: Literal[
        'OutdoorAirOnly', 'Schedule', 'ZoneAirOnly', 'ZoneAndOutdoorAir'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Defines the configuration of the airflow path through the air coil and fan section.'
        },
    )
    air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Zone air exhaust node name if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Simply a unique Node Name if Inlet Air Configuration is Schedule. Otherwise, leave field blank.'
        },
    )
    air_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Zone Air Inlet Node Name if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Simply a unique Node Name if Inlet Air Configuration is Schedule. Otherwise, leave field blank.'
        },
    )
    outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Outdoor air node name if inlet air configuration is ZoneAndOutdoorAir or OutdoorAirOnly, otherwise leave field blank.'
        },
    )
    exhaust_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Simply a unique Node Name if Inlet Air Configuration is ZoneAndOutdoorAir or OutdoorAirOnly, otherwise leave field blank.'
        },
    )
    inlet_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Inlet Air Configuration is Schedule, otherwise leave blank. Schedule values should be degrees C.',
        },
    )
    inlet_air_humidity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Inlet Air Configuration is Schedule, otherwise leave blank. Schedule values are entered as a fraction (e.g. 0.5 is equal to 50%RH)',
        },
    )
    inlet_air_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Used only if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Otherwise, leave field blank.',
        },
    )
    tank_object_type: (
        Literal['', 'WaterHeater:Mixed', 'WaterHeater:Stratified'] | None
    ) = Field(
        default='WaterHeater:Mixed',
        json_schema_extra={
            'note': 'Specify the type of water heater tank used by this heat pump water heater.'
        },
    )
    tank_name: WaterHeaterNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['WaterHeaterNames'],
            'note': 'Needs to match the name used in the corresponding Water Heater object.',
        },
    )
    tank_use_side_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Used only when the heat pump water heater is connected to a plant loop, otherwise leave blank. Needs to match the name used in the corresponding Water Heater object when connected to a plant loop.'
        },
    )
    tank_use_side_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Used only when the heat pump water heater is connected to a plant loop, otherwise leave blank. Needs to match the name used in the corresponding Water Heater object when connected to a plant loop.'
        },
    )
    dx_coil_object_type: (
        Literal[
            '',
            'Coil:WaterHeating:AirToWaterHeatPump:Pumped',
            'Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed',
            'CoilSystem:IntegratedHeatPump:AirSource',
        ]
        | None
    ) = Field(
        default='Coil:WaterHeating:AirToWaterHeatPump:Pumped',
        json_schema_extra={
            'note': 'Specify the type of DX coil used by this heat pump water heater. The only valid choice is Coil:WaterHeating:AirToWaterHeatPump:Pumped and Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed, and Coi...'
        },
    )
    dx_coil_name: (
        HeatPumpWaterHeaterDXCoilsPumpedRef
        | HeatPumpWaterHeaterDXCoilsVariableSpeedRef
        | IntegratedHeatPumpsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'HeatPumpWaterHeaterDXCoilsPumped',
                'HeatPumpWaterHeaterDXCoilsVariableSpeed',
                'IntegratedHeatPumps',
            ],
            'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:* object, or CoilSystem:IntegratedHeatPump:AirSource',
        },
    )
    minimum_inlet_air_temperature_for_compressor_operation: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Heat pump compressor will not operate when the inlet air dry-bulb temperature is below this value.',
        },
    )
    maximum_inlet_air_temperature_for_compressor_operation: float | None = Field(
        default=48.88888888889,
        ge=26.0,
        le=94.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Heat pump compressor will not operate when the inlet air dry-bulb temperature is above this value.',
        },
    )
    compressor_location: Literal['Outdoors', 'Schedule', 'Zone'] = Field(
        ...,
        json_schema_extra={
            'note': 'If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or ZoneAndOutdoorAir. If Schedule is selected, then you must provide a Compressor Ambient Temperature Schedule Name below.'
        },
    )
    compressor_ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Compressor Location is Schedule, otherwise leave field blank.',
        },
    )
    fan_object_type: Literal['', 'Fan:OnOff', 'Fan:SystemModel'] | None = Field(
        default='Fan:OnOff',
        json_schema_extra={
            'note': 'Specify the type of fan used by this heat pump water heater. The only valid choices are Fan:SystemModel or Fan:OnOff.'
        },
    )
    fan_name: FansOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff', 'FansSystemModel'],
            'note': 'Needs to match the name used in the corresponding Fan:SystemModel or Fan:OnOff object.',
        },
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough',
        json_schema_extra={
            'note': 'BlowThrough means the fan is located before the air coil (upstream). DrawThrough means the fan is located after the air coil (downstream).'
        },
    )
    on_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the heat pump compressor operates. Does not contribute to water heating but can impact the zone air heat balance.',
        },
    )
    off_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the heat pump compressor is off. Does not contribute to water heating but can impact the zone air heat balance. Off-cycle parasitic power is 0 when the availa...',
        },
    )
    parasitic_heat_rejection_location: Literal['', 'Outdoors', 'Zone'] | None = Field(
        default='Outdoors',
        json_schema_extra={
            'note': 'This field determines if the parasitic electric load impacts the zone air heat balance. If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or ZoneAndOutdoorAir.'
        },
    )
    inlet_air_mixer_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank.'
        },
    )
    outlet_air_splitter_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank.'
        },
    )
    inlet_air_mixer_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank. Schedule values define whether the heat pump draws its inlet air from the zone, outdoors or a combination...',
        },
    )
    tank_element_control_logic: (
        Literal['', 'MutuallyExclusive', 'Simultaneous'] | None
    ) = Field(
        default='Simultaneous',
        json_schema_extra={
            'note': 'MutuallyExclusive means that once the tank heating element is active the heat pump is shut down until setpoint is reached. Simultaneous (default) means that both the tank heating element and heat p...'
        },
    )
    control_sensor_1_height_in_stratified_tank: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Used to indicate height of control sensor for Tank Object Type = WaterHeater:Stratified If left blank, it will default to the height of Heater1',
        },
    )
    control_sensor_1_weight: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Weight to give Control Sensor 1 temperature The weight of Control Sensor 2 will be 1 - (wt. of control sensor 1)',
        },
    )
    control_sensor_2_height_in_stratified_tank: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Used to indicate height of control sensor for Tank Object Type = WaterHeater:Stratified If left blank, it will default to the height of Heater2',
        },
    )


class WaterHeaterHeatPumpWrappedCondenser(IDFBaseModel):
    """This object models an air-source heat pump for water heating where the
    heating coil is wrapped around the tank, which is typical of residential
    HPWHs. For pumped condenser HPWHs, see WaterHeater:HeatPump:PumpedCondenser.
    WaterHeater:HeatPump:WrappedCondenser is a compound object that references
    other component objects - Coil:WaterHeating:AirToWaterHeatPump:Pumped,
    Fan:OnOff, WaterHeater:Mixed"""

    _idf_object_type: ClassVar[str] = 'WaterHeater:HeatPump:WrappedCondenser'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a heat pump water heater.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the heat pump compr...',
        },
    )
    compressor_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': "Defines the cut-out temperature where the heat pump compressor turns off. The heat pump compressor setpoint temperature should always be greater than the water tank's heater (element or burner) set...",
        },
    )
    dead_band_temperature_difference: float | None = Field(
        default=5.0,
        le=20.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Setpoint temperature minus the dead band temperature difference defines the cut-in temperature where the heat pump compressor turns on. The water tank's heater (element or burner) setpoint temperat...",
        },
    )
    condenser_bottom_location: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the bottom of the tank to the bottom of the wrapped condenser.',
        },
    )
    condenser_top_location: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Distance from the bottom of the tank to the top of the wrapped condenser.',
        },
    )
    evaporator_air_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': "Actual air flow rate across the heat pump's air coil (evaporator). If autocalculated, the air flow rate is set equal to 5.035E-5 m3/s/W times the rated heating capacity of the heat pump's DX coil.",
        },
    )
    inlet_air_configuration: Literal[
        'OutdoorAirOnly', 'Schedule', 'ZoneAirOnly', 'ZoneAndOutdoorAir'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Defines the configuration of the airflow path through the air coil and fan section.'
        },
    )
    air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Zone air exhaust node name if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Simply a unique Node Name if Inlet Air Configuration is Schedule. Otherwise, leave field blank.'
        },
    )
    air_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Zone Air Inlet Node Name if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Simply a unique Node Name if Inlet Air Configuration is Schedule. Otherwise, leave field blank.'
        },
    )
    outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Outdoor air node name if inlet air configuration is ZoneAndOutdoorAir or OutdoorAirOnly, otherwise leave field blank.'
        },
    )
    exhaust_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Simply a unique Node Name if Inlet Air Configuration is ZoneAndOutdoorAir or OutdoorAirOnly, otherwise leave field blank.'
        },
    )
    inlet_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Inlet Air Configuration is Schedule, otherwise leave blank. Schedule values should be degrees C.',
        },
    )
    inlet_air_humidity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Inlet Air Configuration is Schedule, otherwise leave blank. Schedule values are entered as a fraction (e.g. 0.5 is equal to 50%RH)',
        },
    )
    inlet_air_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Used only if Inlet Air Configuration is ZoneAirOnly or ZoneAndOutdoorAir. Otherwise, leave field blank.',
        },
    )
    tank_object_type: Literal['', 'WaterHeater:Stratified'] | None = Field(
        default='WaterHeater:Stratified',
        json_schema_extra={
            'note': 'Specify the type of water heater tank used by this heat pump water heater.'
        },
    )
    tank_name: WaterHeaterStratifiedNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['WaterHeaterStratifiedNames'],
            'note': 'Needs to match the name used in the corresponding Water Heater object. Must be a WaterHeater:Stratified tank.',
        },
    )
    tank_use_side_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Used only when the heat pump water heater is connected to a plant loop, otherwise leave blank. Needs to match the name used in the corresponding Water Heater object when connected to a plant loop.'
        },
    )
    tank_use_side_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Used only when the heat pump water heater is connected to a plant loop, otherwise leave blank. Needs to match the name used in the corresponding Water Heater object when connected to a plant loop.'
        },
    )
    dx_coil_object_type: (
        Literal['', 'Coil:WaterHeating:AirToWaterHeatPump:Wrapped'] | None
    ) = Field(
        default='Coil:WaterHeating:AirToWaterHeatPump:Wrapped',
        json_schema_extra={
            'note': 'Specify the type of DX coil used by this heat pump water heater. The only valid choice is Coil:WaterHeating:AirToWaterHeatPump:Wrapped'
        },
    )
    dx_coil_name: HeatPumpWaterHeaterDXCoilsWrappedRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['HeatPumpWaterHeaterDXCoilsWrapped'],
            'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:Wrapped object.',
        },
    )
    minimum_inlet_air_temperature_for_compressor_operation: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Heat pump compressor will not operate when the inlet air dry-bulb temperature is below this value.',
        },
    )
    maximum_inlet_air_temperature_for_compressor_operation: float | None = Field(
        default=48.88888888889,
        ge=26.0,
        le=94.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Heat pump compressor will not operate when the inlet air dry-bulb temperature is above this value.',
        },
    )
    compressor_location: Literal['Outdoors', 'Schedule', 'Zone'] = Field(
        ...,
        json_schema_extra={
            'note': 'If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or ZoneAndOutdoorAir. If Schedule is selected, then you must provide a Compressor Ambient Temperature Schedule Name below.'
        },
    )
    compressor_ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Compressor Location is Schedule, otherwise leave field blank.',
        },
    )
    fan_object_type: Literal['', 'Fan:OnOff', 'Fan:SystemModel'] | None = Field(
        default='Fan:OnOff',
        json_schema_extra={
            'note': 'Specify the type of fan used by this heat pump water heater. The only valid choices are Fan:SystemModel or Fan:OnOff.'
        },
    )
    fan_name: FansOnOffRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansOnOff', 'FansSystemModel'],
            'note': 'Needs to match the name used in the corresponding Fan:SystemModel or Fan:OnOff object.',
        },
    )
    fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough',
        json_schema_extra={
            'note': 'BlowThrough means the fan is located before the air coil (upstream). DrawThrough means the fan is located after the air coil (downstream).'
        },
    )
    on_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the heat pump compressor operates. Does not contribute to water heating but can impact the zone air heat balance.',
        },
    )
    off_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the heat pump compressor is off. Does not contribute to water heating but can impact the zone air heat balance. Off-cycle parasitic power is 0 when the availa...',
        },
    )
    parasitic_heat_rejection_location: Literal['', 'Outdoors', 'Zone'] | None = Field(
        default='Outdoors',
        json_schema_extra={
            'note': 'This field determines if the parasitic electric load impacts the zone air heat balance. If Zone is selected, Inlet Air Configuration must be ZoneAirOnly or ZoneAndOutdoorAir.'
        },
    )
    inlet_air_mixer_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank.'
        },
    )
    outlet_air_splitter_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank.'
        },
    )
    inlet_air_mixer_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Required only if Inlet Air Configuration is ZoneAndOutdoorAir, otherwise leave field blank. Schedule values define whether the heat pump draws its inlet air from the zone, outdoors or a combination...',
        },
    )
    tank_element_control_logic: (
        Literal['', 'MutuallyExclusive', 'Simultaneous'] | None
    ) = Field(
        default='Simultaneous',
        json_schema_extra={
            'note': 'MutuallyExclusive means that once the tank heating element is active the heat pump is shut down until setpoint is reached. Simultaneous (default) means that both the tank heating element and heat p...'
        },
    )
    control_sensor_1_height_in_stratified_tank: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Used to indicate height of control sensor if Tank Object Type is WaterHeater:Stratified If left blank, it will default to the height of Heater1',
        },
    )
    control_sensor_1_weight: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Weight to give Control Sensor 1 temperature',
        },
    )
    control_sensor_2_height_in_stratified_tank: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Used to indicate height of control sensor if Tank Object Type is WaterHeater:Stratified If left blank, it will default to the height of Heater2 The weight of this control sensor will be 1 - (wt. of...',
        },
    )


class WaterHeaterMixed(IDFBaseModel):
    """Water heater with well-mixed, single-node water tank. May be used to model a
    tankless water heater (small tank volume), a hot water storage tank (zero
    heater capacity), or a heat pump water heater (see
    WaterHeater:HeatPump:PumpedCondenser.)"""

    _idf_object_type: ClassVar[str] = 'WaterHeater:Mixed'
    name: str = Field(...)
    tank_volume: float | Literal['', 'Autosize'] | None = Field(
        default=0.0, json_schema_extra={'units': 'm3'}
    )
    setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    deadband_temperature_difference: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    maximum_temperature_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    heater_control_type: Literal['', 'Cycle', 'Modulate'] | None = Field(
        default='Cycle'
    )
    heater_maximum_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    heater_minimum_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Only used when Heater Control Type is set to Modulate',
        },
    )
    heater_ignition_minimum_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'Not yet implemented'},
    )
    heater_ignition_delay: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 's', 'note': 'Not yet implemented'},
    )
    heater_fuel_type: Literal[
        'Coal',
        'Diesel',
        'DistrictHeatingSteam',
        'DistrictHeatingWater',
        'Electricity',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
    ] = Field(...)
    heater_thermal_efficiency: float = Field(..., gt=0.0)
    part_load_factor_curve_name: UnivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    off_cycle_parasitic_fuel_consumption_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    off_cycle_parasitic_fuel_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default=None)
    off_cycle_parasitic_heat_fraction_to_tank: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    on_cycle_parasitic_fuel_consumption_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    on_cycle_parasitic_fuel_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default=None)
    on_cycle_parasitic_heat_fraction_to_tank: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    ambient_temperature_indicator: Literal['Outdoors', 'Schedule', 'Zone'] = Field(...)
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ambient_temperature_zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    ambient_temperature_outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required for Ambient Temperature Indicator=Outdoors'
        },
    )
    off_cycle_loss_coefficient_to_ambient_temperature: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/K'}
    )
    off_cycle_loss_fraction_to_zone: float | None = Field(default=1.0, ge=0.0, le=1.0)
    on_cycle_loss_coefficient_to_ambient_temperature: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/K'}
    )
    on_cycle_loss_fraction_to_zone: float | None = Field(default=1.0, ge=0.0, le=1.0)
    peak_use_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used if Use Side Node connections are blank',
        },
    )
    use_flow_rate_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Only used if Use Side Node connections are blank',
        },
    )
    cold_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Only used if Use Side Node connections are blank Defaults to water temperatures calculated by Site:WaterMainsTemperature object',
        },
    )
    use_side_inlet_node_name: str | None = Field(default=None)
    use_side_outlet_node_name: str | None = Field(default=None)
    use_side_effectiveness: float | None = Field(default=1.0, ge=0.0, le=1.0)
    source_side_inlet_node_name: str | None = Field(default=None)
    source_side_outlet_node_name: str | None = Field(default=None)
    source_side_effectiveness: float | None = Field(default=1.0, le=1.0, gt=0.0)
    use_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    source_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    indirect_water_heating_recovery_time: float | None = Field(
        default=1.5,
        gt=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Parameter for autosizing design flow rates for indirectly heated water tanks Time required to raise temperature of entire tank from 14.4C to 57.2C',
        },
    )
    source_side_flow_control_mode: (
        Literal[
            '',
            'IndirectHeatAlternateSetpoint',
            'IndirectHeatPrimarySetpoint',
            'StorageTank',
        ]
        | None
    ) = Field(
        default='IndirectHeatPrimarySetpoint',
        json_schema_extra={
            'note': 'StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint calls for heat IndirectHeatAlternateSe...'
        },
    )
    indirect_alternate_setpoint_temperature_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'This field is only used if the previous is set to IndirectHeatAlternateSetpoint',
            },
        )
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class WaterHeaterSizing(IDFBaseModel):
    """This input object is used with WaterHeater:Mixed or with
    WaterHeater:Stratified to autosize tank volume and heater capacity This
    object is not needed if water heaters are not autosized."""

    _idf_object_type: ClassVar[str] = 'WaterHeater:Sizing'
    waterheater_name: WaterHeaterNamesRef = Field(
        ..., json_schema_extra={'object_list': ['WaterHeaterNames']}
    )
    design_mode: (
        Literal[
            'PeakDraw',
            'PerFloorArea',
            'PerPerson',
            'PerSolarCollectorArea',
            'PerUnit',
            'ResidentialHUD-FHAMinimum',
        ]
        | None
    ) = Field(default=None)
    time_storage_can_meet_peak_draw: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Only used for Design Mode = PeakDraw',
        },
    )
    time_for_tank_recovery: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Only used for Design Mode = PeakDraw',
        },
    )
    nominal_tank_volume_for_autosizing_plant_connections: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3',
            'note': 'Only used if Design Mode = PeakDraw and the water heater also has autosized flow rates for connections on the demand side of a plant loop',
        },
    )
    number_of_bedrooms: int | None = Field(
        default=None,
        ge=1,
        json_schema_extra={
            'note': 'Only used for Design Mode = ResidentialHUD-FHAMinimum'
        },
    )
    number_of_bathrooms: int | None = Field(
        default=None,
        ge=1,
        json_schema_extra={
            'note': 'Only used for Design Mode = ResidentialHUD-FHAMinimum'
        },
    )
    storage_capacity_per_person: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/person',
            'note': 'Only used for Design Mode = PerPerson',
        },
    )
    recovery_capacity_per_person: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/hr-person',
            'note': 'Only used for Design Mode = PerPerson',
        },
    )
    storage_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/m2',
            'note': 'Only used for Design Mode = PerFloorArea',
        },
    )
    recovery_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/hr-m2',
            'note': 'Only used for Design Mode = PerFloorArea',
        },
    )
    number_of_units: float | None = Field(
        default=None, json_schema_extra={'note': 'Only used for Design Mode = PerUnit'}
    )
    storage_capacity_per_unit: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3',
            'note': 'Only used for Design Mode = PerUnit',
        },
    )
    recovery_capacity_perunit: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/hr',
            'note': 'Only used for Design Mode = PerUnit',
        },
    )
    storage_capacity_per_collector_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/m2',
            'note': 'Only used for Design Mode = PerSolarCollectorArea',
        },
    )
    height_aspect_ratio: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'note': 'only used if for WaterHeater:Stratified'},
    )


class WaterHeaterStratified(IDFBaseModel):
    """Water heater with stratified, multi-node water tank. May be used to model a
    tankless water heater (small tank volume), a hot water storage tank (zero
    heater capacity), or a heat pump water heater (see WaterHeater:HeatPump:*.)"""

    _idf_object_type: ClassVar[str] = 'WaterHeater:Stratified'
    name: str = Field(...)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    tank_volume: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3'}
    )
    tank_height: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm',
            'note': 'Height is measured in the axial direction for horizontal cylinders',
        },
    )
    tank_shape: (
        Literal['', 'HorizontalCylinder', 'Other', 'VerticalCylinder'] | None
    ) = Field(default='VerticalCylinder')
    tank_perimeter: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Only used if Tank Shape is Other'},
    )
    maximum_temperature_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    heater_priority_control: Literal['', 'MasterSlave', 'Simultaneous'] | None = Field(
        default='MasterSlave'
    )
    heater_1_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    heater_1_deadband_temperature_difference: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    heater_1_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    heater_1_height: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm'}
    )
    heater_2_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    heater_2_deadband_temperature_difference: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    heater_2_capacity: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    heater_2_height: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm'}
    )
    heater_fuel_type: Literal[
        'Coal',
        'Diesel',
        'DistrictHeatingSteam',
        'DistrictHeatingWater',
        'Electricity',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
    ] = Field(...)
    heater_thermal_efficiency: float = Field(..., gt=0.0)
    off_cycle_parasitic_fuel_consumption_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    off_cycle_parasitic_fuel_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default=None)
    off_cycle_parasitic_heat_fraction_to_tank: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    off_cycle_parasitic_height: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm'}
    )
    on_cycle_parasitic_fuel_consumption_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    on_cycle_parasitic_fuel_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default=None)
    on_cycle_parasitic_heat_fraction_to_tank: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    on_cycle_parasitic_height: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm'}
    )
    ambient_temperature_indicator: Literal['Outdoors', 'Schedule', 'Zone'] = Field(...)
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ambient_temperature_zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    ambient_temperature_outdoor_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required for Ambient Temperature Indicator=Outdoors'
        },
    )
    uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2-K'})
    )
    skin_loss_fraction_to_zone: float | None = Field(default=1.0, ge=0.0, le=1.0)
    off_cycle_flue_loss_coefficient_to_ambient_temperature: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/K'}
    )
    off_cycle_flue_loss_fraction_to_zone: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    peak_use_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used if Use Side Node connections are blank',
        },
    )
    use_flow_rate_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, defaults to 1.0 at all times Only used if use side node connections are blank',
        },
    )
    cold_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Only used if use side node connections are blank Defaults to water temperatures calculated by Site:WaterMainsTemperature object',
        },
    )
    use_side_inlet_node_name: str | None = Field(default=None)
    use_side_outlet_node_name: str | None = Field(default=None)
    use_side_effectiveness: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': "The use side effectiveness in the stratified tank model is a simplified analogy of a heat exchanger's effectiveness. This effectiveness is equal to the fraction of use mass flow rate that directly ..."
        },
    )
    use_side_inlet_height: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Defaults to bottom of tank'},
    )
    use_side_outlet_height: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={'units': 'm', 'note': 'Defaults to top of tank'},
    )
    source_side_inlet_node_name: str | None = Field(default=None)
    source_side_outlet_node_name: str | None = Field(default=None)
    source_side_effectiveness: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': "The source side effectiveness in the stratified tank model is a simplified analogy of a heat exchanger's effectiveness. This effectiveness is equal to the fraction of source mass flow rate that dir..."
        },
    )
    source_side_inlet_height: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={'units': 'm', 'note': 'Defaults to top of tank'},
    )
    source_side_outlet_height: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'Defaults to bottom of tank'},
    )
    inlet_mode: Literal['', 'Fixed', 'Seeking'] | None = Field(default='Fixed')
    use_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    source_side_design_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    indirect_water_heating_recovery_time: float | None = Field(
        default=1.5,
        gt=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Parameter for autosizing design flow rates for indirectly heated water tanks time required to raise temperature of entire tank from 14.4C to 57.2C',
        },
    )
    number_of_nodes: int | None = Field(default=1, ge=1, le=12)
    additional_destratification_conductivity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    node_1_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_2_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_3_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_4_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_5_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_6_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_7_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_8_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_9_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_10_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_11_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    node_12_additional_loss_coefficient: float | None = Field(
        default=0.0, json_schema_extra={'units': 'W/K'}
    )
    source_side_flow_control_mode: (
        Literal[
            '',
            'IndirectHeatAlternateSetpoint',
            'IndirectHeatPrimarySetpoint',
            'StorageTank',
        ]
        | None
    ) = Field(
        default='IndirectHeatPrimarySetpoint',
        json_schema_extra={
            'note': 'StorageTank mode always requests flow unless tank is at its Maximum Temperature Limit IndirectHeatPrimarySetpoint mode requests flow whenever primary setpoint for heater 1 calls for heat IndirectHe...'
        },
    )
    indirect_alternate_setpoint_temperature_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'This field is only used if the previous is set to IndirectHeatAlternateSetpoint',
            },
        )
    )
