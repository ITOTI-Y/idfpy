"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: User Defined HVAC and Plant Component Models
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ProgramNamesRef,
    WaterStorageTankNamesRef,
    ZoneNamesRef,
)



class AirTerminalSingleDuctUserDefined(IDFBaseModel):
    """Defines a generic single duct air terminal unit for custom modeling using
Energy Management System or External Interface"""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:UserDefined"
    name: str = Field(..., json_schema_extra={'note': 'This is the name of the air terminal'})
    overall_model_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    model_setup_and_sizing_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    primary_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Air inlet node for the unit must be a zone splitter outlet.'})
    primary_air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Air outlet node for the unit must be a zone air inlet node.'})
    secondary_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Inlet air used for heat rejection or air source'})
    secondary_air_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Outlet air used for heat rejection or air source'})
    number_of_plant_loop_connections: int = Field(..., ge=0, le=2)
    plant_connection_1_inlet_node_name: str = Field(...)
    plant_connection_1_outlet_node_name: str = Field(...)
    plant_connection_2_inlet_node_name: str | None = Field(default=None)
    plant_connection_2_outlet_node_name: str | None = Field(default=None)
    supply_inlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for alternate source of water consumed by device'})
    collection_outlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for collection of condensate by device'})
    ambient_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Used for modeling device losses to surrounding zone'})


class CoilUserDefined(IDFBaseModel):
    """Defines a generic air system component for custom modeling using Energy
Management System or External Interface"""

    _idf_object_type: ClassVar[str] = "Coil:UserDefined"
    name: str = Field(..., json_schema_extra={'note': 'This is the name of the coil'})
    overall_model_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'This is the name of a program to run that defines the user-defined functionality for this component. This can match the name of an EnergyManagementSystem:Program or PythonPlugin:Instance object as ...'})
    model_setup_and_sizing_program_calling_manager_name: ProgramNamesRef = Field(..., json_schema_extra={'object_list': ['ProgramNames']})
    number_of_air_connections: int = Field(..., ge=1, le=2)
    air_connection_1_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Inlet air for primary air stream'})
    air_connection_1_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Outlet air for primary air stream'})
    air_connection_2_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Inlet air for secondary air stream'})
    air_connection_2_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Outlet air for secondary air stream'})
    plant_connection_is_used: Literal['No', 'Yes'] | None = Field(default=None)
    plant_connection_inlet_node_name: str | None = Field(default=None)
    plant_connection_outlet_node_name: str | None = Field(default=None)
    supply_inlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for alternate source of water consumed by device'})
    collection_outlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for collection of condensate by device'})
    ambient_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Used for modeling device losses to surrounding zone'})


class PlantComponentUserDefined(IDFBaseModel):
    """Defines a generic plant component for custom modeling using Energy
Management System or External Interface"""

    _idf_object_type: ClassVar[str] = "PlantComponent:UserDefined"
    name: str = Field(..., json_schema_extra={'note': 'This is the name of the plant component'})
    main_model_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    number_of_plant_loop_connections: int = Field(..., ge=1, le=4)
    plant_connection_1_inlet_node_name: str = Field(...)
    plant_connection_1_outlet_node_name: str = Field(...)
    plant_connection_1_loading_mode: Literal['DemandsLoad', 'MeetsLoadWithNominalCapacity', 'MeetsLoadWithNominalCapacityHiOutLimit', 'MeetsLoadWithNominalCapacityLowOutLimit', 'MeetsLoadWithPassiveCapacity'] = Field(...)
    plant_connection_1_loop_flow_request_mode: Literal['NeedsFlowAndTurnsLoopOn', 'NeedsFlowIfLoopOn', 'ReceivesWhateverFlowAvailable'] = Field(...)
    plant_connection_1_initialization_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    plant_connection_1_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    plant_connection_2_inlet_node_name: str | None = Field(default=None)
    plant_connection_2_outlet_node_name: str | None = Field(default=None)
    plant_connection_2_loading_mode: Literal['DemandsLoad', 'MeetLoadWithNominalCapacity', 'MeetLoadWithNominalCapacityHiOutLimit', 'MeetLoadWithNominalCapacityLowOutLimit', 'MeetLoadWithPassiveCapacity'] | None = Field(default=None)
    plant_connection_2_loop_flow_request_mode: Literal['NeedsFlowAndTurnsLoopOn', 'NeedsFlowIfLoopOn', 'ReceivesWhateverFlowAvailable'] | None = Field(default=None)
    plant_connection_2_initialization_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    plant_connection_2_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    plant_connection_3_inlet_node_name: str | None = Field(default=None)
    plant_connection_3_outlet_node_name: str | None = Field(default=None)
    plant_connection_3_loading_mode: Literal['DemandsLoad', 'MeetLoadWithNominalCapacity', 'MeetLoadWithNominalCapacityHiOutLimit', 'MeetLoadWithNominalCapacityLowOutLimit', 'MeetLoadWithPassiveCapacity'] | None = Field(default=None)
    plant_connection_3_loop_flow_request_mode: Literal['NeedsFlowAndTurnsLoopOn', 'NeedsFlowIfLoopOn', 'ReceivesWhateverFlowAvailable'] | None = Field(default=None)
    plant_connection_3_initialization_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    plant_connection_3_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    plant_connection_4_inlet_node_name: str | None = Field(default=None)
    plant_connection_4_outlet_node_name: str | None = Field(default=None)
    plant_connection_4_loading_mode: Literal['DemandsLoad', 'MeetLoadWithNominalCapacity', 'MeetLoadWithNominalCapacityHiOutLimit', 'MeetLoadWithNominalCapacityLowOutLimit', 'MeetLoadWithPassiveCapacity'] | None = Field(default=None)
    plant_connection_4_loop_flow_request_mode: Literal['NeedsFlowAndTurnsLoopOn', 'NeedsFlowIfLoopOn', 'ReceivesWhateverFlowAvailable'] | None = Field(default=None)
    plant_connection_4_initialization_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    plant_connection_4_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    air_connection_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Inlet air used for heat rejection or air source'})
    air_connection_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Outlet air used for heat rejection or air source'})
    supply_inlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for alternate source of water consumed by device'})
    collection_outlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for collection of condensate by device'})
    ambient_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Used for modeling device losses to surrounding zone'})


class PlantEquipmentOperationUserDefined(IDFBaseModel):
    """Defines a generic plant operation scheme for custom supervisory control
using Energy Management System or External Interface to dispatch loads"""

    _idf_object_type: ClassVar[str] = "PlantEquipmentOperation:UserDefined"
    name: str = Field(..., json_schema_extra={'note': 'This is the name of the plant operation scheme'})
    main_model_program_calling_manager_name: ProgramNamesRef = Field(..., json_schema_extra={'object_list': ['ProgramNames']})
    initialization_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames']})
    equipment_1_object_type: str | None = Field(default=None)
    equipment_1_name: str | None = Field(default=None)
    equipment_2_object_type: str | None = Field(default=None)
    equipment_2_name: str | None = Field(default=None)
    equipment_3_object_type: str | None = Field(default=None)
    equipment_3_name: str | None = Field(default=None)
    equipment_4_object_type: str | None = Field(default=None)
    equipment_4_name: str | None = Field(default=None)
    equipment_5_object_type: str | None = Field(default=None)
    equipment_5_name: str | None = Field(default=None)
    equipment_6_object_type: str | None = Field(default=None)
    equipment_6_name: str | None = Field(default=None)
    equipment_7_object_type: str | None = Field(default=None)
    equipment_7_name: str | None = Field(default=None)
    equipment_8_object_type: str | None = Field(default=None)
    equipment_8_name: str | None = Field(default=None)
    equipment_9_object_type: str | None = Field(default=None)
    equipment_9_name: str | None = Field(default=None)
    equipment_10_object_type: str | None = Field(default=None)
    equipment_10_name: str | None = Field(default=None)


class ZoneHVACForcedAirUserDefined(IDFBaseModel):
    """Defines a generic zone air unit for custom modeling using Energy Management
System or External Interface"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:ForcedAir:UserDefined"
    name: str = Field(..., json_schema_extra={'note': 'This is the name of the zone unit'})
    overall_model_simulation_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    model_setup_and_sizing_program_calling_manager_name: ProgramNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ProgramNames'], 'note': 'For use with the API (Library, Callback) workflow, this field should be the same string that the user provides when registering a callback function using the API.  In this workflow, the callback na...'})
    primary_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Air inlet node for the unit must be a zone air exhaust Node.'})
    primary_air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Air outlet node for the unit must be a zone air inlet node.'})
    secondary_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Inlet air used for heat rejection or air source'})
    secondary_air_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Outlet air used for heat rejection or air source'})
    number_of_plant_loop_connections: int = Field(..., ge=0, le=3)
    plant_connection_1_inlet_node_name: str | None = Field(default=None)
    plant_connection_1_outlet_node_name: str | None = Field(default=None)
    plant_connection_2_inlet_node_name: str | None = Field(default=None)
    plant_connection_2_outlet_node_name: str | None = Field(default=None)
    plant_connection_3_inlet_node_name: str | None = Field(default=None)
    plant_connection_3_outlet_node_name: str | None = Field(default=None)
    supply_inlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for alternate source of water consumed by device'})
    collection_outlet_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames'], 'note': 'Water use storage tank for collection of condensate by device'})
    ambient_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Used for modeling device losses to surrounding zone'})

