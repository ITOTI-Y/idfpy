"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Zone HVAC Equipment Connections
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ScheduleNamesRef,
    SpaceNamesRef,
    ZoneEquipmentListsRef,
    ZoneEquipmentNamesRef,
    ZoneNamesRef,
)


class SpaceHVACZoneEquipmentMixerSpacesItem(IDFBaseModel):
    """Nested object type for array items."""
    space_name: SpaceNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames']})
    space_fraction: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'dimensionless', 'note': 'Fraction of the Zone Equipment Inlet Node airflow drawn from this space.'})
    space_node_name: str = Field(..., json_schema_extra={'note': 'Matches a SpaceHVAC:EquipmentConnections Exhaust Node Name'})


class SpaceHVACZoneEquipmentSplitterSpacesItem(IDFBaseModel):
    """Nested object type for array items."""
    space_name: SpaceNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames']})
    space_fraction: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'dimensionless', 'note': 'Fraction of this zone equipment output or airflow distributed to this space.'})
    space_supply_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Only used for airflow equipment Matches a SpaceHVAC:EquipmentConnections Inlet Node Name'})


class SpaceHVACZoneReturnMixerSpacesItem(IDFBaseModel):
    """Nested object type for array items."""
    space_name: SpaceNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames']})
    space_return_air_node_name: str = Field(..., json_schema_extra={'note': 'Matches a SpaceHVAC:EquipmentConnections Return Air Node Name'})


class ZoneHVACEquipmentListEquipmentItem(IDFBaseModel):
    """Nested object type for array items."""
    zone_equipment_object_type: Literal['AirLoopHVAC:UnitarySystem', 'Fan:ZoneExhaust', 'HeatExchanger:AirToAir:FlatPlate', 'WaterHeater:HeatPump:PumpedCondenser', 'WaterHeater:HeatPump:WrappedCondenser', 'ZoneHVAC:AirDistributionUnit', 'ZoneHVAC:Baseboard:Convective:Electric', 'ZoneHVAC:Baseboard:Convective:Water', 'ZoneHVAC:Baseboard:RadiantConvective:Electric', 'ZoneHVAC:Baseboard:RadiantConvective:Steam', 'ZoneHVAC:Baseboard:RadiantConvective:Water', 'ZoneHVAC:CoolingPanel:RadiantConvective:Water', 'ZoneHVAC:Dehumidifier:DX', 'ZoneHVAC:EnergyRecoveryVentilator', 'ZoneHVAC:EvaporativeCoolerUnit', 'ZoneHVAC:ForcedAir:UserDefined', 'ZoneHVAC:FourPipeFanCoil', 'ZoneHVAC:HighTemperatureRadiant', 'ZoneHVAC:HybridUnitaryHVAC', 'ZoneHVAC:IdealLoadsAirSystem', 'ZoneHVAC:LowTemperatureRadiant:ConstantFlow', 'ZoneHVAC:LowTemperatureRadiant:Electric', 'ZoneHVAC:LowTemperatureRadiant:VariableFlow', 'ZoneHVAC:OutdoorAirUnit', 'ZoneHVAC:PackagedTerminalAirConditioner', 'ZoneHVAC:PackagedTerminalHeatPump', 'ZoneHVAC:RefrigerationChillerSet', 'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow', 'ZoneHVAC:UnitHeater', 'ZoneHVAC:UnitVentilator', 'ZoneHVAC:VentilatedSlab', 'ZoneHVAC:WaterToAirHeatPump', 'ZoneHVAC:WindowAirConditioner'] = Field(...)
    zone_equipment_name: ZoneEquipmentNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneEquipmentNames']})
    zone_equipment_cooling_sequence: int = Field(..., ge=0, json_schema_extra={'note': 'Specifies the zone equipment simulation order when the zone thermostat requests cooling'})
    zone_equipment_heating_or_no_load_sequence: int = Field(..., ge=0, json_schema_extra={'note': 'Specifies the zone equipment simulation order when the zone thermostat requests heating or no load'})
    zone_equipment_sequential_cooling_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'The fraction of the remaining cooling load this equipment will attempt to serve if the load distribution scheme is SequentialLoad, otherwise ignored.'})
    zone_equipment_sequential_heating_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'The fraction of the remaining heating load this equipment will attempt to serve if the load distribution scheme is SequentialLoad, otherwise ignored.'})



class SpaceHVACEquipmentConnections(IDFBaseModel):
    """Specifies the HVAC equipment connections for a space. Node names are
specified for the space air node, air inlet nodes, air exhaust nodes, and
the air return node. If any space in a zone has a
SpaceHVAC:EquipmentConnections object, then all spaces in the zone must have
one. Used only when ZoneAirHeatBalanceAlgorithm \"Do Space Heat Balance for
Sizing\"is Yes."""

    _idf_object_type: ClassVar[str] = "SpaceHVAC:EquipmentConnections"
    space_name: SpaceNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames']})
    space_air_inlet_node_or_nodelist_name: str | None = Field(default=None)
    space_air_exhaust_node_or_nodelist_name: str | None = Field(default=None)
    space_air_node_name: str = Field(...)
    space_return_air_node_or_nodelist_name: str | None = Field(default=None)
    space_return_air_node_1_flow_rate_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule is multiplied times the base return air flow rate. If this field is left blank, the schedule defaults to 1.0 at all times.'})
    space_return_air_node_1_flow_rate_basis_node_or_nodelist_name: str | None = Field(default=None, json_schema_extra={'note': 'The optional basis node(s) used to calculate the base return air flow rate for the first return air node in this space. The return air flow rate is the sum of the flow rates at the basis node(s) mu...'})


class SpaceHVACZoneEquipmentMixer(IDFBaseModel):
    """Mixes the airflow from one or more Spaces into a piece of zone equipment.
All spaces in the zone must also have a SpaceHVAC:EquipmentConnections
object. Used only when ZoneAirHeatBalanceAlgorithm \"Do Space Heat Balance
for Sizing\" = Yes."""

    _idf_object_type: ClassVar[str] = "SpaceHVAC:ZoneEquipmentMixer"
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Must be a controlled zone which has a ZoneHVAC:EquipmentConfiguration object.'})
    zone_equipment_inlet_node_name: str = Field(..., json_schema_extra={'note': 'The inlet node from the zone equipment that will be mixed from the spaces. Must match a Zone Exhaust Node for this zone.'})
    space_fraction_method: Literal['', 'DesignCoolingLoad', 'DesignHeatingLoad', 'FloorArea', 'PerimeterLength', 'Volume'] | None = Field(default='DesignCoolingLoad', json_schema_extra={'note': 'The basis used to autosize the space output fractions.'})
    spaces: list[SpaceHVACZoneEquipmentMixerSpacesItem] | None = Field(default=None)


class SpaceHVACZoneEquipmentSplitter(IDFBaseModel):
    """Distributes the output from a piece of zone equipment to one or more Spaces
in the Zone. If any equipment in a zone has a
SpaceHVAC:ZoneEquipmentSplitter, then all equipment in the zone must have
one. except Fan:ZoneExhaust. All spaces in the zone must also have a
SpaceHVAC:EquipmentConnections object. Used only when
ZoneAirHeatBalanceAlgorithm \"Do Space Heat Balance for Sizing\" = Yes."""

    _idf_object_type: ClassVar[str] = "SpaceHVAC:ZoneEquipmentSplitter"
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Must be a controlled zone which has a ZoneHVAC:EquipmentConfiguration object.'})
    zone_equipment_object_type: Literal['AirLoopHVAC:UnitarySystem', 'HeatExchanger:AirToAir:FlatPlate', 'WaterHeater:HeatPump:PumpedCondenser', 'WaterHeater:HeatPump:WrappedCondenser', 'ZoneHVAC:AirDistributionUnit', 'ZoneHVAC:Baseboard:Convective:Electric', 'ZoneHVAC:Baseboard:Convective:Water', 'ZoneHVAC:Baseboard:RadiantConvective:Electric', 'ZoneHVAC:Baseboard:RadiantConvective:Steam', 'ZoneHVAC:Baseboard:RadiantConvective:Water', 'ZoneHVAC:CoolingPanel:RadiantConvective:Water', 'ZoneHVAC:Dehumidifier:DX', 'ZoneHVAC:EnergyRecoveryVentilator', 'ZoneHVAC:EvaporativeCoolerUnit', 'ZoneHVAC:ForcedAir:UserDefined', 'ZoneHVAC:FourPipeFanCoil', 'ZoneHVAC:HighTemperatureRadiant', 'ZoneHVAC:HybridUnitaryHVAC', 'ZoneHVAC:IdealLoadsAirSystem', 'ZoneHVAC:LowTemperatureRadiant:ConstantFlow', 'ZoneHVAC:LowTemperatureRadiant:Electric', 'ZoneHVAC:LowTemperatureRadiant:VariableFlow', 'ZoneHVAC:OutdoorAirUnit', 'ZoneHVAC:PackagedTerminalAirConditioner', 'ZoneHVAC:PackagedTerminalHeatPump', 'ZoneHVAC:RefrigerationChillerSet', 'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow', 'ZoneHVAC:UnitHeater', 'ZoneHVAC:UnitVentilator', 'ZoneHVAC:VentilatedSlab', 'ZoneHVAC:WaterToAirHeatPump', 'ZoneHVAC:WindowAirConditioner'] = Field(...)
    zone_equipment_name: ZoneEquipmentNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneEquipmentNames']})
    zone_equipment_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Only used for airflow equipment. The outlet node from the zone equipment that will be split to the spaces.'})
    thermostat_control_method: Literal['', 'Ideal', 'Maximum', 'SingleSpace'] | None = Field(default='SingleSpace', json_schema_extra={'note': 'SingleSpace satisfies the thermostat in the Control Space Name Maximum satisfies the thermostat in the connected spaces with the highest deviation from setpoint Ideal ignores the Space Output Fract...'})
    control_space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'This field is only used when Thermostat Control Method = SingleSpace.'})
    space_fraction_method: Literal['', 'DesignCoolingLoad', 'DesignHeatingLoad', 'FloorArea', 'PerimeterLength', 'Volume'] | None = Field(default='DesignCoolingLoad', json_schema_extra={'note': 'The basis used to autosize the space output fractions.'})
    spaces: list[SpaceHVACZoneEquipmentSplitterSpacesItem] | None = Field(default=None)


class SpaceHVACZoneReturnMixer(IDFBaseModel):
    """Mixes the return airflow from one or more Spaces into a zone return node.
All spaces in the zone must also have a SpaceHVAC:EquipmentConnections
object. Used only when ZoneAirHeatBalanceAlgorithm \"Do Space Heat Balance
for Sizing\" = Yes."""

    _idf_object_type: ClassVar[str] = "SpaceHVAC:ZoneReturnMixer"
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Must be a controlled zone which has a ZoneHVAC:EquipmentConfiguration object.'})
    zone_return_air_node_name: str = Field(..., json_schema_extra={'note': 'The zone return air node will be mixed from the spaces. Must match a Zone Return Air Node for this zone.'})
    spaces: list[SpaceHVACZoneReturnMixerSpacesItem] | None = Field(default=None)


class ZoneHVACEquipmentConnections(IDFBaseModel):
    """Specifies the HVAC equipment connections for a zone. Node names are
specified for the zone air node, air inlet nodes, air exhaust nodes, and the
air return node. A zone equipment list is referenced which lists all HVAC
equipment connected to the zone."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:EquipmentConnections"
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    zone_conditioning_equipment_list_name: ZoneEquipmentListsRef = Field(..., json_schema_extra={'object_list': ['ZoneEquipmentLists'], 'note': 'Enter the name of a ZoneHVAC:EquipmentList object.'})
    zone_air_inlet_node_or_nodelist_name: str | None = Field(default=None)
    zone_air_exhaust_node_or_nodelist_name: str | None = Field(default=None)
    zone_air_node_name: str = Field(...)
    zone_return_air_node_or_nodelist_name: str | None = Field(default=None)
    zone_return_air_node_1_flow_rate_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This schedule is multiplied times the base return air flow rate. If this field is left blank, the schedule defaults to 1.0 at all times.'})
    zone_return_air_node_1_flow_rate_basis_node_or_nodelist_name: str | None = Field(default=None, json_schema_extra={'note': 'The optional basis node(s) used to calculate the base return air flow rate for the first return air node in this zone. The return air flow rate is the sum of the flow rates at the basis node(s) mul...'})


class ZoneHVACEquipmentList(IDFBaseModel):
    """List equipment in simulation order. Note that an
ZoneHVAC:AirDistributionUnit object must be listed in this statement if
there is a forced air system serving the zone from the air loop. Equipment
is simulated in the order specified by Zone Equipment Cooling Sequence and
Zone Equipment Heating or No-Load Sequence, depending on the thermostat
request. For equipment of similar type, assign sequence 1 to the first
system intended to serve that type of load. For situations where one or more
equipment types has limited capacity or limited control, order the sequence
so that the most controllable piece of equipment runs last. For example,
with a dedicated outdoor air system (DOAS), the air terminal for the DOAS
should be assigned Heating Sequence = 1 and Cooling Sequence = 1. Any other
equipment should be assigned sequence 2 or higher so that it will see the
net load after the DOAS air is added to the zone."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:EquipmentList"
    name: str = Field(...)
    load_distribution_scheme: Literal['', 'SequentialLoad', 'SequentialUniformPLR', 'UniformLoad', 'UniformPLR'] | None = Field(default='SequentialLoad')
    equipment: list[ZoneHVACEquipmentListEquipmentItem] | None = Field(default=None)

