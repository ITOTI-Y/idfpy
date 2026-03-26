"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Air Distribution
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AirLoopHVACMixerNamesRef,
    AirLoopHVACSplitterNamesRef,
    AirLoopOAEquipmentListsRef,
    AirPrimaryLoopsRef,
    BranchListsRef,
    ConnectorListsRef,
    ControllerListsRef,
    FansComponentModelRef,
    FansSystemModelRef,
    ReturnPathComponentNamesRef,
    ScheduleNamesRef,
    SupplyPathComponentNamesRef,
    SystemAvailabilityManagerListsRef,
    ValidBranchEquipmentNamesRef,
    ValidOASysEquipmentNamesRef,
    ValidOASysEquipmentTypesRef,
    ZoneMixersRef,
    ZoneNamesRef,
)


class AirLoopHVACDedicatedOutdoorAirSystemAirloophvacsItem(IDFBaseModel):
    """Nested object type for array items."""

    airloophvac_name: AirPrimaryLoopsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'The rest of fields are extensible. It requires AirLoopHVAC names served by an AirLoopHVAC:DedicatedOutdoorAirSystem.',
        },
    )


class AirLoopHVACMixerNodesItem(IDFBaseModel):
    """Nested object type for array items."""

    inlet_node_name: str = Field(...)


class AirLoopHVACReturnPathComponentsItem(IDFBaseModel):
    """Nested object type for array items."""

    component_object_type: Literal[
        'AirLoopHVAC:ReturnPlenum', 'AirLoopHVAC:ZoneMixer'
    ] = Field(...)
    component_name: ReturnPathComponentNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ReturnPathComponentNames']}
    )


class AirLoopHVACSplitterNodesItem(IDFBaseModel):
    """Nested object type for array items."""

    outlet_node_name: str = Field(...)


class AirLoopHVACSupplyPathComponentsItem(IDFBaseModel):
    """Nested object type for array items."""

    component_object_type: Literal[
        'AirLoopHVAC:SupplyPlenum', 'AirLoopHVAC:ZoneSplitter'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Supply path components must be listed in flow order.'
        },
    )
    component_name: SupplyPathComponentNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SupplyPathComponentNames']}
    )


class AirLoopHVAC(IDFBaseModel):
    """Defines a central forced air system."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC'
    name: str = Field(...)
    controller_list_name: ControllerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControllerLists'],
            'note': 'Enter the name of an AirLoopHVAC:ControllerList object.',
        },
    )
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SystemAvailabilityManagerLists'],
            'note': 'Enter the name of an AvailabilityManagerAssignmentList object.',
        },
    )
    design_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default=0.0, json_schema_extra={'units': 'm3/s'}
    )
    branch_list_name: BranchListsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BranchLists'],
            'note': 'Name of a BranchList containing all the branches in this air loop',
        },
    )
    connector_list_name: ConnectorListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ConnectorLists'],
            'note': 'Name of a ConnectorList containing all the splitters and mixers in the loop',
        },
    )
    supply_side_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Name of inlet node where air enters the supply side of the air loop. If this air loop has a return path, then this node is where return air enters the supply side. If this air loop has no return pa...'
        },
    )
    demand_side_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of outlet node where return air leaves the demand side and enters the supply side. Required if this air loop has a return path. Leave this field blank if there is no return.'
        },
    )
    demand_side_inlet_node_names: str = Field(
        ...,
        json_schema_extra={
            'note': 'Name of a Node or NodeList containing the inlet node(s) supplying air to zone equipment.'
        },
    )
    supply_side_outlet_node_names: str = Field(
        ...,
        json_schema_extra={
            'note': 'Name of a Node or NodeList containing the outlet node(s) supplying air to the demand side.'
        },
    )
    design_return_air_flow_fraction_of_supply_air_flow: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'note': 'The design return air flow rate as a fraction of supply air flow rate with no exhaust. This can be used to model a pressurized system or set to zero to model a DOAS with no return flow. Use ZoneAir...'
        },
    )


class AirLoopHVACDedicatedOutdoorAirSystem(IDFBaseModel):
    """Defines a central forced air system to provide dedicated outdoor air to
    multiple AirLoopHVACs."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:DedicatedOutdoorAirSystem'
    name: str = Field(...)
    airloophvac_outdoorairsystem_name: ValidBranchEquipmentNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['validBranchEquipmentNames'],
            'note': 'Enter the name of an AirLoopHVAC:OutdoorAirSystem object.',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    airloophvac_mixer_name: AirLoopHVACMixerNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirLoopHVACMixerNames'],
            'note': 'Name of AirLoopHVAC:Mixer.',
        },
    )
    airloophvac_splitter_name: AirLoopHVACSplitterNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirLoopHVACSplitterNames'],
            'note': 'Name of AirLoopHVAC:Splitter.',
        },
    )
    preheat_design_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    preheat_design_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    precool_design_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    precool_design_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    number_of_airloophvac: int = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the number of the AirLoopHAVC served by AirLoopHVAC:DedicatedOutdoorAirSystem'
        },
    )
    airloophvacs: list[AirLoopHVACDedicatedOutdoorAirSystemAirloophvacsItem] | None = (
        Field(default=None)
    )


class AirLoopHVACExhaustSystem(IDFBaseModel):
    """Defines a general exhaust system with a central exhaust fan drawing from one
    or more ZoneHVAC:ExhaustControl outlet nodes via an AirLoopHVAC:ZoneMixer."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ExhaustSystem'
    name: str = Field(..., json_schema_extra={'note': 'Name of the exhaust system'})
    zone_mixer_name: ZoneMixersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneMixers'],
            'note': 'The name of the exhaust system AirLoopHVAC:ZoneMixer',
        },
    )
    fan_object_type: Literal['Fan:ComponentModel', 'Fan:SystemModel'] = Field(...)
    fan_name: FansComponentModelRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={'object_list': ['FansComponentModel', 'FansSystemModel']},
    )


class AirLoopHVACMixer(IDFBaseModel):
    """Mix N inlet air streams from Relief Air Stream Node in OutdoorAir:Mixer
    objects served by AirLoopHVAC objects listed in
    AirLoopHVAC:DedicatedOutdoorAirSystem into one (currently 10 as default, but
    extensible). Node names cannot be duplicated within a single mixer list."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:Mixer'
    name: str = Field(...)
    outlet_node_name: str = Field(...)
    nodes: list[AirLoopHVACMixerNodesItem] | None = Field(default=None)


class AirLoopHVACOutdoorAirSystem(IDFBaseModel):
    """Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box
    and optional outdoor air conditioning equipment such as heat recovery,
    preheat, and precool coils. From the perspective of the primary air loop the
    outdoor air system is treated as a single component."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:OutdoorAirSystem'
    name: str = Field(...)
    controller_list_name: ControllerListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ControllerLists'],
            'note': 'Enter the name of an AirLoopHVAC:ControllerList object or blank if this object is used in AirLoopHVAC:DedicatedOutdoorAirSystem.',
        },
    )
    outdoor_air_equipment_list_name: AirLoopOAEquipmentListsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirLoopOAEquipmentLists'],
            'note': 'Enter the name of an AirLoopHVAC:OutdoorAirSystem:EquipmentList object.',
        },
    )


class AirLoopHVACOutdoorAirSystemEquipmentList(IDFBaseModel):
    """List equipment in simulation order"""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:OutdoorAirSystem:EquipmentList'
    name: str = Field(...)
    component_1_object_type: ValidOASysEquipmentTypesRef = Field(
        ..., json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_1_name: ValidOASysEquipmentNamesRef = Field(
        ..., json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_2_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_2_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_3_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_3_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_4_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_4_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_5_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_5_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_6_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_6_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_7_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_7_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_8_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_8_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )
    component_9_object_type: ValidOASysEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentTypes']}
    )
    component_9_name: ValidOASysEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validOASysEquipmentNames']}
    )


class AirLoopHVACReturnPath(IDFBaseModel):
    """A return air path can only contain one AirLoopHVAC:ZoneMixer and one or more
    AirLoopHVAC:ReturnPlenum objects."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ReturnPath'
    name: str = Field(...)
    return_air_path_outlet_node_name: str = Field(...)
    components: list[AirLoopHVACReturnPathComponentsItem] | None = Field(default=None)


class AirLoopHVACReturnPlenum(IDFBaseModel):
    """Connects N zone inlet air streams, through zone return plenum, to outlet
    (currently 500 per air loop) Node names cannot be duplicated within a single
    plenum list."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ReturnPlenum'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    zone_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    induced_air_outlet_node_or_nodelist_name: str | None = Field(default=None)
    nodes: list[AirLoopHVACMixerNodesItem] | None = Field(default=None)


class AirLoopHVACSplitter(IDFBaseModel):
    """Split one air stream from AirLoopHVAC:DedicatedOutdoorAirSystem outlet node
    into N outlet streams (currently 10 as default, but extensible). Node names
    should be Outdoor Air Stream Node Name in OutdoorAir:Mixer objects served by
    AirLoopHVAC objects listed in AirLoopHVAC:DedicatedOutdoorAirSystem."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:Splitter'
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    nodes: list[AirLoopHVACSplitterNodesItem] | None = Field(default=None)


class AirLoopHVACSupplyPath(IDFBaseModel):
    """A supply path can only contain AirLoopHVAC:ZoneSplitter and
    AirLoopHVAC:SupplyPlenum objects which may be in series or parallel."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:SupplyPath'
    name: str = Field(...)
    supply_air_path_inlet_node_name: str = Field(...)
    components: list[AirLoopHVACSupplyPathComponentsItem] | None = Field(default=None)


class AirLoopHVACSupplyPlenum(IDFBaseModel):
    """Connects 1 zone inlet air stream, through zone supply plenum, to one or more
    outlets. Node names cannot be duplicated within a single supply plenum list."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:SupplyPlenum'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    zone_node_name: str = Field(...)
    inlet_node_name: str = Field(...)
    nodes: list[AirLoopHVACSplitterNodesItem] | None = Field(default=None)


class AirLoopHVACZoneMixer(IDFBaseModel):
    """Mix N inlet air streams into one (currently 500 per air loop, but
    extensible). Node names cannot be duplicated within a single zone mixer
    (AirLoopHVAC:ZoneMixer) list."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ZoneMixer'
    name: str = Field(...)
    outlet_node_name: str = Field(...)
    nodes: list[AirLoopHVACMixerNodesItem] | None = Field(default=None)


class AirLoopHVACZoneSplitter(IDFBaseModel):
    """Split one air stream into N outlet streams (currently 500 per air loop, but
    extensible). Node names cannot be duplicated within a single zone splitter
    (AirLoopHVAC:ZoneSplitter) list."""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ZoneSplitter'
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    nodes: list[AirLoopHVACSplitterNodesItem] | None = Field(default=None)


class OutdoorAirMixer(IDFBaseModel):
    """Outdoor air mixer. Node names cannot be duplicated within a single
    OutdoorAir:Mixer object or across all outdoor air mixers."""

    _idf_object_type: ClassVar[str] = 'OutdoorAir:Mixer'
    name: str = Field(...)
    mixed_air_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Mixed Air Node'}
    )
    outdoor_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Outdoor Air Stream Node'}
    )
    relief_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Relief Air Stream Node'}
    )
    return_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Return Air Stream Node'}
    )
