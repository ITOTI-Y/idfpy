"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Room Air Models
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllHeatTranSurfNamesRef,
    RoomAirflowNetworkNodesRef,
    RoomAirNodeGainsRef,
    RoomAirNodeHVACEquipmentRef,
    RoomAirNodeSurfaceListsRef,
    ScheduleNamesRef,
    ZoneNamesRef,
)


class RoomAirNodeAirflowNetworkAdjacentSurfaceListSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )


class RoomAirNodeAirflowNetworkHVACEquipmentEquipmentFractionsItem(IDFBaseModel):
    """Nested object type for array items."""

    zonehvac_or_air_terminal_equipment_object_type: (
        Literal[
            'AirLoopHVACReturnAir',
            'AirTerminal:DualDuct:ConstantVolume',
            'AirTerminal:DualDuct:VAV',
            'AirTerminal:DualDuct:VAV:OutdoorAir',
            'AirTerminal:SingleDuct:ConstantVolume:CooledBeam',
            'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction',
            'AirTerminal:SingleDuct:ConstantVolume:NoReheat',
            'AirTerminal:SingleDuct:ConstantVolume:Reheat',
            'AirTerminal:SingleDuct:ParallelPIU:Reheat',
            'AirTerminal:SingleDuct:SeriesPIU:Reheat',
            'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat',
            'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat',
            'AirTerminal:SingleDuct:VAV:NoReheat',
            'AirTerminal:SingleDuct:VAV:Reheat',
            'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan',
            'Fan:ZoneExhaust',
            'WaterHeater:HeatPump:PumpedCondenser',
            'WaterHeater:HeatPump:WrappedCondenser',
            'ZoneHVAC:Baseboard:Convective:Electric',
            'ZoneHVAC:Baseboard:Convective:Water',
            'ZoneHVAC:Baseboard:RadiantConvective:Electric',
            'ZoneHVAC:Baseboard:RadiantConvective:Steam',
            'ZoneHVAC:Baseboard:RadiantConvective:Water',
            'ZoneHVAC:Dehumidifier:DX',
            'ZoneHVAC:EnergyRecoveryVentilator',
            'ZoneHVAC:FourPipeFanCoil',
            'ZoneHVAC:HighTemperatureRadiant',
            'ZoneHVAC:IdealLoadsAirSystem',
            'ZoneHVAC:OutdoorAirUnit',
            'ZoneHVAC:PackagedTerminalAirConditioner',
            'ZoneHVAC:PackagedTerminalHeatPump',
            'ZoneHVAC:RefrigerationChillerSet',
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
            'ZoneHVAC:UnitHeater',
            'ZoneHVAC:UnitVentilator',
            'ZoneHVAC:VentilatedSlab',
            'ZoneHVAC:WaterToAirHeatPump',
            'ZoneHVAC:WindowAirConditioner',
        ]
        | None
    ) = Field(default=None)
    zonehvac_or_air_terminal_equipment_object_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'for object type AirLoopHVACReturnAir, then enter zone return air node name'
        },
    )
    fraction_of_output_or_supply_air_from_hvac_equipment: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    fraction_of_input_or_return_air_to_hvac_equipment: float | None = Field(
        default=None, ge=0.0, le=1.0
    )


class RoomAirNodeAirflowNetworkInternalGainsGainsItem(IDFBaseModel):
    """Nested object type for array items."""

    internal_gain_object_type: (
        Literal[
            'AirTerminal:SingleDuct:UserDefined',
            'Coil:UserDefined',
            'DaylightingDevice:Tubular',
            'ElectricEquipment',
            'ElectricLoadCenter:Inverter:FunctionOfPower',
            'ElectricLoadCenter:Inverter:LookUpTable',
            'ElectricLoadCenter:Inverter:Simple',
            'ElectricLoadCenter:Storage:Battery',
            'ElectricLoadCenter:Storage:Converter',
            'ElectricLoadCenter:Storage:LiIonNMCBattery',
            'ElectricLoadCenter:Storage:Simple',
            'ElectricLoadCenter:Transformer',
            'GasEquipment',
            'Generator:FuelCell',
            'Generator:MicroCHP',
            'HeaderedPumps:ConstantSpeed',
            'HeaderedPumps:VariableSpeed',
            'HotWaterEquipment',
            'Lights',
            'OtherEquipment',
            'People',
            'Pipe:Indoor',
            'PlantComponent:UserDefined',
            'Pump:ConstantSpeed',
            'Pump:VariableSpeed',
            'Pump:VariableSpeed:Condensate',
            'Refrigeration:Case',
            'Refrigeration:CompressorRack',
            'Refrigeration:SecondarySystem:Pipe',
            'Refrigeration:SecondarySystem:Receiver',
            'Refrigeration:System:Condenser:AirCooled',
            'Refrigeration:System:SuctionPipe',
            'Refrigeration:TranscriticalSystem:GasCooler:AirCooled',
            'Refrigeration:TranscriticalSystem:SuctionPipeLT',
            'Refrigeration:TranscriticalSystem:SuctionPipeMT',
            'Refrigeration:WalkIn',
            'SteamEquipment',
            'ThermalStorage:ChilledWater:Mixed',
            'ThermalStorage:ChilledWater:Stratified',
            'WaterHeater:Mixed',
            'WaterHeater:Stratified',
            'WaterUse:Equipment',
            'ZoneBaseboard:OutdoorTemperatureControlled',
            'ZoneContaminantSourceAndSink:CarbonDioxide',
            'ZoneContaminantSourceAndSink:GenericContaminant',
            'ZoneHVAC:ForcedAir:UserDefined',
        ]
        | None
    ) = Field(default=None)
    internal_gain_object_name: str | None = Field(default=None)
    fraction_of_gains_to_node: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'fraction applies to sensible, latent, carbon dioxide, and generic contaminant gains or losses'
        },
    )


class RoomAirSettingsAirflowNetworkNodesItem(IDFBaseModel):
    """Nested object type for array items."""

    roomairflownetwork_node_name: RoomAirflowNetworkNodesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['RoomAirflowNetworkNodes']}
    )


class RoomAirTemperaturePatternNondimensionalHeightPairsItem(IDFBaseModel):
    """Nested object type for array items."""

    pair_zeta_nondimensional_height: float = Field(...)
    pair_delta_adjacent_air_temperature: float = Field(
        ..., ge=-10.0, le=20.0, json_schema_extra={'units': 'deltaC'}
    )


class RoomAirTemperaturePatternSurfaceMappingSurfaceDeltasItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name_pair: AllHeatTranSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    delta_adjacent_air_temperature_pair: float = Field(
        ..., json_schema_extra={'units': 'deltaC'}
    )


class RoomAirModelType(IDFBaseModel):
    """Selects the type of room air model to be used in a given zone. If no
    RoomAirModelType object is specified then the default Mixing model (all zone
    air at the same temperature) will be used."""

    _idf_object_type: ClassVar[str] = 'RoomAirModelType'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    room_air_modeling_type: (
        Literal[
            '',
            'AirflowNetwork',
            'CrossVentilation',
            'Mixing',
            'OneNodeDisplacementVentilation',
            'ThreeNodeDisplacementVentilation',
            'UnderFloorAirDistributionExterior',
            'UnderFloorAirDistributionInterior',
            'UserDefined',
        ]
        | None
    ) = Field(
        default='Mixing',
        json_schema_extra={
            'note': 'Mixing = Complete mixing air model UserDefined = UserDefined Room Air Temperature Patterns needs RoomAir:TemperaturePattern:UserDefined object referencing this Zone OneNodeDisplacementVentilation =...'
        },
    )
    air_temperature_coupling_strategy: Literal['', 'Direct', 'Indirect'] | None = Field(
        default='Direct'
    )


class RoomAirNode(IDFBaseModel):
    """Define an air node for some types of nodal room air models"""

    _idf_object_type: ClassVar[str] = 'RoomAir:Node'
    name: str | None = Field(default=None)
    node_type: Literal[
        'Ceiling', 'Control', 'Floor', 'Inlet', 'MundtRoom', 'Return'
    ] = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    height_of_nodal_control_volume_center: float = Field(
        ..., json_schema_extra={'units': 'm'}
    )
    surface_1_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_2_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_3_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_4_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_5_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_6_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_7_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_8_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_9_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_10_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_11_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_12_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_13_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_14_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_15_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_16_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_17_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_18_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_19_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_20_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_21_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )


class RoomAirNodeAirflowNetwork(IDFBaseModel):
    """define an air node for some types of nodal air models"""

    _idf_object_type: ClassVar[str] = 'RoomAir:Node:AirflowNetwork'
    name: str | None = Field(default=None)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    fraction_of_zone_air_volume: float | None = Field(default=None, ge=0.0, le=1.0)
    roomair_node_airflownetwork_adjacentsurfacelist_name: (
        RoomAirNodeSurfaceListsRef | None
    ) = Field(
        default=None, json_schema_extra={'object_list': ['RoomAirNodeSurfaceLists']}
    )
    roomair_node_airflownetwork_internalgains_name: RoomAirNodeGainsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['RoomAirNodeGains']}
    )
    roomair_node_airflownetwork_hvacequipment_name: (
        RoomAirNodeHVACEquipmentRef | None
    ) = Field(
        default=None, json_schema_extra={'object_list': ['RoomAirNodeHVACEquipment']}
    )


class RoomAirNodeAirflowNetworkAdjacentSurfaceList(IDFBaseModel):
    """RoomAir:Node:AirflowNetwork:AdjacentSurfaceList"""

    _idf_object_type: ClassVar[str] = 'RoomAir:Node:AirflowNetwork:AdjacentSurfaceList'
    name: str | None = Field(default=None)
    surfaces: list[RoomAirNodeAirflowNetworkAdjacentSurfaceListSurfacesItem] | None = (
        Field(default=None)
    )


class RoomAirNodeAirflowNetworkHVACEquipment(IDFBaseModel):
    """define the zone equipment associated with one particular RoomAir:Node"""

    _idf_object_type: ClassVar[str] = 'RoomAir:Node:AirflowNetwork:HVACEquipment'
    name: str | None = Field(default=None)
    equipment_fractions: (
        list[RoomAirNodeAirflowNetworkHVACEquipmentEquipmentFractionsItem] | None
    ) = Field(default=None)


class RoomAirNodeAirflowNetworkInternalGains(IDFBaseModel):
    """define the internal gains that are associated with one particular
    RoomAir:Node"""

    _idf_object_type: ClassVar[str] = 'RoomAir:Node:AirflowNetwork:InternalGains'
    name: str | None = Field(default=None)
    gains: list[RoomAirNodeAirflowNetworkInternalGainsGainsItem] | None = Field(
        default=None
    )


class RoomAirSettingsAirflowNetwork(IDFBaseModel):
    """RoomAir modeling using Airflow pressure network solver"""

    _idf_object_type: ClassVar[str] = 'RoomAirSettings:AirflowNetwork'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Name of Zone being described. Any existing zone name',
        },
    )
    control_point_roomairflownetwork_node_name: RoomAirflowNetworkNodesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['RoomAirflowNetworkNodes']}
        )
    )
    nodes: list[RoomAirSettingsAirflowNetworkNodesItem] | None = Field(default=None)


class RoomAirSettingsCrossVentilation(IDFBaseModel):
    """This UCSD Cross Ventilation Room Air Model provides a simple model for heat
    transfer and vertical temperature profile prediction in cross ventilated
    rooms. The model distinguishes two regions in the room, the main jet region
    and the recirculations, and predicts characteristic airflow velocities and
    average air temperatures. Used with RoomAirModelType = CrossVentilation."""

    _idf_object_type: ClassVar[str] = 'RoomAirSettings:CrossVentilation'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Name of Zone being described. Any existing zone name',
        },
    )
    gain_distribution_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Distribution of the convective heat gains between the jet and recirculation zones. 0<= Accepted Value <= 1. In the CV model 1 means all convective gains in the jet region.',
        },
    )
    airflow_region_used_for_thermal_comfort_evaluation: (
        Literal['Jet', 'Recirculation'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Required field whenever thermal comfort is predicted defines Air temperature and Airflow velocity that will be used in the Fanger model conditions must refer to one of the two regions: jet or recir...'
        },
    )


class RoomAirSettingsOneNodeDisplacementVentilation(IDFBaseModel):
    """The Mundt model for displacement ventilation"""

    _idf_object_type: ClassVar[str] = 'RoomAirSettings:OneNodeDisplacementVentilation'
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    fraction_of_convective_internal_loads_added_to_floor_air: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    fraction_of_infiltration_internal_loads_added_to_floor_air: float | None = Field(
        default=None, ge=0.0, le=1.0
    )


class RoomAirSettingsThreeNodeDisplacementVentilation(IDFBaseModel):
    """The UCSD model for Displacement Ventilation"""

    _idf_object_type: ClassVar[str] = 'RoomAirSettings:ThreeNodeDisplacementVentilation'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Name of Zone being described. Any existing zone name',
        },
    )
    gain_distribution_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Distribution of the convective heat gains between the occupied and mixed zones. 0<= Accepted Value <= 1. In the DV model 1 means all convective gains in the lower layer.',
        },
    )
    number_of_plumes_per_occupant: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Used only in the UCSD displacement ventilation model. Effective number of separate plumes per occupant in the occupied zone. Plumes that merge together in the occupied zone count as one.'
        },
    )
    thermostat_height: float | None = Field(
        default=1.1,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height of thermostat/temperature control sensor above floor',
        },
    )
    comfort_height: float | None = Field(
        default=1.1,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height at which air temperature is calculated for comfort purposes',
        },
    )
    temperature_difference_threshold_for_reporting: float | None = Field(
        default=0.4,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Minimum temperature difference between predicted upper and lower layer temperatures above which DV auxiliary outputs are calculated. These outputs are 'DV Transition Height', 'DV Fraction Min Recom...",
        },
    )


class RoomAirSettingsUnderFloorAirDistributionExterior(IDFBaseModel):
    """Applicable to exterior spaces that are served by an underfloor air
    distribution system. The dominant sources of heat gain should be from
    people, equipment, and other localized sources located in the occupied part
    of the room, as well as convective gain coming from a warm window. Used with
    RoomAirModelType = CrossVentilation."""

    _idf_object_type: ClassVar[str] = (
        'RoomAirSettings:UnderFloorAirDistributionExterior'
    )
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Name of Zone being described. Any existing zone name',
        },
    )
    number_of_diffusers_per_zone: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate'
    )
    power_per_plume: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate', json_schema_extra={'units': 'W'}
    )
    design_effective_area_of_diffuser: float | Literal['', 'Autocalculate'] | None = (
        Field(default='Autocalculate', json_schema_extra={'units': 'm2'})
    )
    diffuser_slot_angle_from_vertical: float | Literal['', 'Autocalculate'] | None = (
        Field(default='Autocalculate', json_schema_extra={'units': 'deg'})
    )
    thermostat_height: float | None = Field(
        default=1.2,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height of thermostat/temperature control sensor above floor',
        },
    )
    comfort_height: float | None = Field(
        default=1.1,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height at which Air temperature is calculated for comfort purposes',
        },
    )
    temperature_difference_threshold_for_reporting: float | None = Field(
        default=0.4,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Minimum temperature difference between upper and lower layer temperatures above which UFAD auxiliary outputs are calculated. These outputs are 'UF Transition Height' and 'UF Average Temp Gradient'....",
        },
    )
    floor_diffuser_type: (
        Literal[
            '', 'Custom', 'HorizontalSwirl', 'LinearBarGrille', 'Swirl', 'VariableArea'
        ]
        | None
    ) = Field(default='Swirl')
    transition_height: float | Literal['', 'Autocalculate'] | None = Field(
        default=1.7,
        json_schema_extra={
            'units': 'm',
            'note': 'User-specified height above floor of boundary between occupied and upper subzones',
        },
    )
    coefficient_a_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_b_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_c_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_d_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_e_in_formula_kc_a_gamma_b_c_d_gamma_e_gamma_2: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )


class RoomAirSettingsUnderFloorAirDistributionInterior(IDFBaseModel):
    """This Room Air Model is applicable to interior spaces that are served by an
    underfloor air distribution system. The dominant sources of heat gain should
    be from people, equipment, and other localized sources located in the
    occupied part of the room. The model should be used with caution in zones
    which have large heat gains or losses through exterior walls or windows or
    which have considerable direct solar gain. Used with RoomAirModelType =
    UnderFloorAirDistributionInterior."""

    _idf_object_type: ClassVar[str] = (
        'RoomAirSettings:UnderFloorAirDistributionInterior'
    )
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Name of Zone with underfloor air distribution',
        },
    )
    number_of_diffusers: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={'note': 'Total number of diffusers in this zone'},
    )
    power_per_plume: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate', json_schema_extra={'units': 'W'}
    )
    design_effective_area_of_diffuser: float | Literal['', 'Autocalculate'] | None = (
        Field(default='Autocalculate', json_schema_extra={'units': 'm2'})
    )
    diffuser_slot_angle_from_vertical: float | Literal['', 'Autocalculate'] | None = (
        Field(default='Autocalculate', json_schema_extra={'units': 'deg'})
    )
    thermostat_height: float | None = Field(
        default=1.2,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height of thermostat/temperature control sensor above floor',
        },
    )
    comfort_height: float | None = Field(
        default=1.1,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Height at which air temperature is calculated for comfort purposes',
        },
    )
    temperature_difference_threshold_for_reporting: float | None = Field(
        default=0.4,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Minimum temperature difference between predicted upper and lower layer temperatures above which UFAD auxiliary outputs are calculated. These outputs are 'UF Transition Height' and 'UF Average Temp ...",
        },
    )
    floor_diffuser_type: (
        Literal[
            '', 'Custom', 'HorizontalSwirl', 'LinearBarGrille', 'Swirl', 'VariableArea'
        ]
        | None
    ) = Field(default='Swirl')
    transition_height: float | Literal['', 'Autocalculate'] | None = Field(
        default=1.7,
        json_schema_extra={
            'units': 'm',
            'note': 'user-specified height above floor of boundary between occupied and upper subzones',
        },
    )
    coefficient_a: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Coefficient A in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2 Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_b: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Coefficient B in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2 Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_c: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Coefficient C in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2 Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_d: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Coefficient D in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2 Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )
    coefficient_e: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'Coefficient E in Formula Kc = A*Gamma**B + C + D*Gamma + E*Gamma**2 Kc is the fraction of the total zone load attributable to the lower subzone'
        },
    )


class RoomAirTemperaturePatternConstantGradient(IDFBaseModel):
    """Used to model room air with a fixed temperature gradient in the vertical
    direction. Used in combination with RoomAir:TemperaturePattern:UserDefined."""

    _idf_object_type: ClassVar[str] = 'RoomAir:TemperaturePattern:ConstantGradient'
    room_air_temperature_pattern_constant_gradient_name: str = Field(...)
    control_integer_for_pattern_control_schedule_name: int = Field(
        ..., json_schema_extra={'note': 'reference this entry in Schedule Name'}
    )
    thermostat_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Temp at thermostat- Mean Air Temp)',
        },
    )
    return_air_offset: float | None = Field(
        default=None,
        json_schema_extra={'units': 'deltaC', 'note': '= (Tleaving - Mean Air Temp )'},
    )
    exhaust_air_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Texhaust - Mean Air Temp) deg C',
        },
    )
    temperature_gradient: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'K/m',
            'note': 'Slope of temperature change in vertical direction',
        },
    )


class RoomAirTemperaturePatternNondimensionalHeight(IDFBaseModel):
    """Defines a distribution pattern for air temperatures relative to the current
    mean air temperature as a function of height. The height, referred to as
    Zeta, is nondimensional by normalizing with the zone ceiling height. Used in
    combination with RoomAir:TemperaturePattern:UserDefined."""

    _idf_object_type: ClassVar[str] = 'RoomAir:TemperaturePattern:NondimensionalHeight'
    name: str = Field(...)
    control_integer_for_pattern_control_schedule_name: int = Field(
        ...,
        json_schema_extra={'note': 'this value should appear in as a schedule value'},
    )
    thermostat_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Temp at thermostat- Mean Air Temp)',
        },
    )
    return_air_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Temp leaving - Mean Air Temp ) deg C',
        },
    )
    exhaust_air_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Temp exhaust - Mean Air Temp) deg C the remaining fields have pairs that describe the relative temperature pattern in the vertical direction of a zone Zeta is the nondimensional height (in z-dir...',
        },
    )
    pairs: list[RoomAirTemperaturePatternNondimensionalHeightPairsItem] | None = Field(
        default=None
    )


class RoomAirTemperaturePatternSurfaceMapping(IDFBaseModel):
    """Defines a distribution pattern for the air temperatures adjacent to
    individual surfaces. This allows controlling the adjacent air temperature on
    a surface-by-surface basis rather than by height. This allows modeling
    different adjacent air temperatures on the opposite sides of the zone. Used
    in combination with RoomAir:TemperaturePattern:UserDefined."""

    _idf_object_type: ClassVar[str] = 'RoomAir:TemperaturePattern:SurfaceMapping'
    name: str = Field(...)
    control_integer_for_pattern_control_schedule_name: int = Field(
        ..., json_schema_extra={'note': 'reference this entry in schedule'}
    )
    thermostat_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Temp at thermostat- Mean Air Temp)',
        },
    )
    return_air_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Tleaving - Mean Air Temp ) deg C',
        },
    )
    exhaust_air_offset: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': '= (Texhaust - Mean Air Temp) deg C',
        },
    )
    surface_deltas: (
        list[RoomAirTemperaturePatternSurfaceMappingSurfaceDeltasItem] | None
    ) = Field(default=None)


class RoomAirTemperaturePatternTwoGradient(IDFBaseModel):
    """Used to model room air with two temperature gradients in the vertical
    direction. Used in combination with RoomAir:TemperaturePattern:UserDefined."""

    _idf_object_type: ClassVar[str] = 'RoomAir:TemperaturePattern:TwoGradient'
    room_air_temperature_pattern_two_gradient_name: str = Field(...)
    control_integer_for_pattern_control_schedule_name: int = Field(
        ..., json_schema_extra={'note': 'reference this entry in Schedule Name'}
    )
    thermostat_height: float | None = Field(
        default=None,
        json_schema_extra={'units': 'm', 'note': '= Distance from floor of zone'},
    )
    return_air_height: float | None = Field(
        default=None,
        json_schema_extra={'units': 'm', 'note': '= Distance from floor of zone'},
    )
    exhaust_air_height: float | None = Field(
        default=None,
        json_schema_extra={'units': 'm', 'note': '= Distance from floor of zone'},
    )
    temperature_gradient_lower_bound: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'K/m',
            'note': 'Slope of temperature change in vertical direction',
        },
    )
    temperature_gradient_upper_bound: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'K/m',
            'note': 'Slope of temperature change in vertical direction',
        },
    )
    gradient_interpolation_mode: (
        Literal[
            'OutdoorDryBulbTemperature',
            'SensibleCoolingLoad',
            'SensibleHeatingLoad',
            'ZoneAndOutdoorTemperatureDifference',
            'ZoneDryBulbTemperature',
        ]
        | None
    ) = Field(default=None)
    upper_temperature_bound: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    lower_temperature_bound: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    upper_heat_rate_bound: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    lower_heat_rate_bound: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )


class RoomAirTemperaturePatternUserDefined(IDFBaseModel):
    """Used to explicitly define temperature patterns that are to be applied to the
    mean air temperature within a thermal zone. Used with RoomAirModelType =
    UserDefined."""

    _idf_object_type: ClassVar[str] = 'RoomAir:TemperaturePattern:UserDefined'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this model. Schedule value > 0 means the model is active. Schedule value = 0 means the model is inactive and the zone will be modeled as fully mixed (Mixing). If this...',
        },
    )
    pattern_control_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule should contain integer values that correspond to unique Control Integer fields in one of the RoomAir:TemperaturePattern:* objects.',
        },
    )
