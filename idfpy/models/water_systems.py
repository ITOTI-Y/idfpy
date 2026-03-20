"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Water Systems
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllShadingAndHTSurfNamesRef,
    MaterialNameRef,
    ScheduleNamesRef,
    WaterStorageTankNamesRef,
    WaterUseEquipmentNamesRef,
    ZoneNamesRef,
)


class WaterUseConnectionsConnectionsItem(IDFBaseModel):
    """Nested object type for array items."""
    water_use_equipment_name: WaterUseEquipmentNamesRef = Field(..., json_schema_extra={'object_list': ['WaterUseEquipmentNames'], 'note': 'Enter the name of a WaterUse:Equipment object.'})


class WaterUseRainCollectorSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""
    collection_surface_name: AllShadingAndHTSurfNamesRef = Field(..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']})



class WaterUseConnections(IDFBaseModel):
    """A subsystem that groups together multiple WaterUse:Equipment components. As
its name suggests, the object provides connections that are shared by these
components, including: 1. Inlet node and outlet node connections to a plant
loop 2. Connections to WaterUse:Storage objects to store and draw reclaimed
water 3. Internal connections to simulate drainwater heat recovery."""

    _idf_object_type: ClassVar[str] = "WaterUse:Connections"
    name: str = Field(...)
    inlet_node_name: str | None = Field(default=None)
    outlet_node_name: str | None = Field(default=None)
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'If blank, or tank is empty, defaults to fresh water from the mains'})
    reclamation_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    hot_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to cold water supply temperature'})
    cold_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to water temperatures calculated by Site:WaterMainsTemperature object'})
    drain_water_heat_exchanger_type: Literal['', 'CounterFlow', 'CrossFlow', 'Ideal', 'None'] | None = Field(default='None')
    drain_water_heat_exchanger_destination: Literal['', 'Equipment', 'Plant', 'PlantAndEquipment'] | None = Field(default='Plant')
    drain_water_heat_exchanger_u_factor_times_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/K'})
    connections: list[WaterUseConnectionsConnectionsItem] | None = Field(default=None)


class WaterUseEquipment(IDFBaseModel):
    """A generalized object for simulating all water end uses. Hot and cold water
uses are included, as well as controlled mixing of hot and cold water at the
tap. The WaterUse:Equipment object can be used stand-alone, or coupled into
a plant loop using the WaterUse:Connections object (see below). The
WaterUse:Connections object allows water uses to be linked to
WaterUse:Storage objects to store and draw reclaimed water. The object can
also simulate drainwater heat recovery."""

    _idf_object_type: ClassVar[str] = "WaterUse:Equipment"
    name: str = Field(...)
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})
    peak_flow_rate: float = Field(..., ge=0.0, json_schema_extra={'units': 'm3/s'})
    flow_rate_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to 1.0 at all times'})
    target_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to hot water supply temperature'})
    hot_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to cold water supply temperature'})
    cold_water_supply_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to water temperatures calculated by Site:WaterMainsTemperature object'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames']})
    sensible_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to 0.0 at all times'})
    latent_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Defaults to 0.0 at all times'})


class WaterUseRainCollector(IDFBaseModel):
    """Used for harvesting rainwater falling on building surfaces. The rainwater is
sent to a WaterUse:Storage object. In versions up till Version 9.6, it is
necessary to also include a Site:Precipitation object to describe the rates
of rainfall, in order to use this object. In later versions, if the
Site:Precipitation is not present, precipitation depth in the weather input
.epw will be used instead. When this is the case, please make sure the
precipitation in the .epw is accurate."""

    _idf_object_type: ClassVar[str] = "WaterUse:RainCollector"
    name: str = Field(...)
    storage_tank_name: WaterStorageTankNamesRef = Field(..., json_schema_extra={'object_list': ['WaterStorageTankNames']})
    loss_factor_mode: Literal['Constant', 'Scheduled'] | None = Field(default=None)
    collection_loss_factor: float | None = Field(default=None, json_schema_extra={'note': 'this is the portion of rain that is lost in the process of collecting it the rain collected is one minus this factor'})
    collection_loss_factor_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    maximum_collection_rate: float | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Defaults to unlimited flow.'})
    surfaces: list[WaterUseRainCollectorSurfacesItem] | None = Field(default=None)


class WaterUseStorage(IDFBaseModel):
    """A water storage tank. If the building model is to include any on-site water
collection, wells, or storing and reuse of graywater, then a
WaterUse:Storage object is needed. Each WaterUse:Storage can serve as a
central node and make connections to numerous sources of supply or numerous
components with demand. If a maximum capacity is not specified, the tank is
assumed to have unlimited capacity."""

    _idf_object_type: ClassVar[str] = "WaterUse:Storage"
    name: str = Field(...)
    water_quality_subcategory: str | None = Field(default=None)
    maximum_capacity: float | None = Field(default=None, json_schema_extra={'units': 'm3', 'note': 'Defaults to unlimited capacity.'})
    initial_volume: float | None = Field(default=None, json_schema_extra={'units': 'm3'})
    design_in_flow_rate: float | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Defaults to unlimited flow.'})
    design_out_flow_rate: float | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Defaults to unlimited flow.'})
    overflow_destination: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'If blank, overflow is discarded'})
    type_of_supply_controlled_by_float_valve: Literal['GroundwaterWell', 'Mains', 'None', 'OtherTank'] | None = Field(default=None)
    float_valve_on_capacity: float | None = Field(default=None, json_schema_extra={'units': 'm3', 'note': 'Lower range of target storage level e.g. float valve kicks on'})
    float_valve_off_capacity: float | None = Field(default=None, json_schema_extra={'units': 'm3', 'note': 'Upper range of target storage level e.g. float valve kicks off'})
    backup_mains_capacity: float | None = Field(default=None, json_schema_extra={'units': 'm3', 'note': "Lower range of secondary target storage level used to keep tanks at a minimum level using mains water if well can't keep up"})
    other_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    water_thermal_mode: Literal['ScheduledTemperature', 'ThermalModel'] | None = Field(default=None)
    water_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    ambient_temperature_indicator: Literal['Outdoors', 'Schedule', 'Zone'] | None = Field(default=None)
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames']})
    tank_surface_area: float | None = Field(default=None, json_schema_extra={'units': 'm2'})
    tank_u_value: float | None = Field(default=None, json_schema_extra={'units': 'W/m2-K'})
    tank_outside_surface_material_name: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})


class WaterUseWell(IDFBaseModel):
    """Simulates on-site water supply from a well. Well water is pumped out of the
ground into a WaterUse:Storage. The operation of the ground water well is
controlled by the associated WaterUse:Storage which is assumed to be
operated as a vented cistern with no pressure tank."""

    _idf_object_type: ClassVar[str] = "WaterUse:Well"
    name: str = Field(...)
    storage_tank_name: WaterStorageTankNamesRef = Field(..., json_schema_extra={'object_list': ['WaterStorageTankNames']})
    pump_depth: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    pump_rated_flow_rate: float | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    pump_rated_head: float | None = Field(default=None, json_schema_extra={'units': 'Pa'})
    pump_rated_power_consumption: float | None = Field(default=None, json_schema_extra={'units': 'W'})
    pump_efficiency: float | None = Field(default=None)
    well_recovery_rate: float | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    nominal_well_storage_volume: float | None = Field(default=None, json_schema_extra={'units': 'm3'})
    water_table_depth_mode: Literal['Constant', 'Scheduled'] | None = Field(default=None)
    water_table_depth: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    water_table_depth_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})

