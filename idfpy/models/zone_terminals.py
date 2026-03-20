"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Zone HVAC Air Loop Terminal Units
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AirTerminalUnitNamesRef,
    CoolingCoilNameRef,
    DOAToZonalUnitRef,
    DSOASpaceListNamesRef,
    DesignSpecificationAirTerminalSizingNameRef,
    DesignSpecificationOutdoorAirNamesRef,
    FansCVRef,
    FansSystemModelRef,
    FansVAVRef,
    HeatingCoilNameRef,
    ScheduleNamesRef,
    UnivariateFunctionsRef,
    ZoneMixersRef,
    ZoneNamesRef,
)



class AirTerminalDualDuctConstantVolume(IDFBaseModel):
    """Central air system terminal unit, dual duct, constant volume."""

    _idf_object_type: ClassVar[str] = "AirTerminal:DualDuct:ConstantVolume"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit. This is also the zone inlet node.'})
    hot_air_inlet_node_name: str = Field(...)
    cold_air_inlet_node_name: str = Field(...)
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})


class AirTerminalDualDuctVAV(IDFBaseModel):
    """Central air system terminal unit, dual duct, variable volume."""

    _idf_object_type: ClassVar[str] = "AirTerminal:DualDuct:VAV"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit. This is also the zone inlet node.'})
    hot_air_inlet_node_name: str = Field(...)
    cold_air_inlet_node_name: str = Field(...)
    maximum_damper_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_fraction: float | None = Field(default=0.2, ge=0.0, le=1.0, json_schema_extra={'note': 'fraction of maximum air flow'})
    design_specification_outdoor_air_object_name: (DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...'})
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the design minimum flow rate by multiplying it using this schedule of fraction values. This field is used with "Zone Minimum Air Flow Fraction". Schedule values are fractions 0.0...'})


class AirTerminalDualDuctVAVOutdoorAir(IDFBaseModel):
    """Central air system terminal unit, dual duct, variable volume with special
controls. One VAV duct is controlled to supply ventilation air and the other
VAV duct is controlled to meet the zone cooling load."""

    _idf_object_type: ClassVar[str] = "AirTerminal:DualDuct:VAV:OutdoorAir"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit. This is also the zone inlet node.'})
    outdoor_air_inlet_node_name: str = Field(...)
    recirculated_air_inlet_node_name: str | None = Field(default=None)
    maximum_terminal_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'If autosized this is the sum of flow needed for cooling and maximum required outdoor air'})
    design_specification_outdoor_air_object_name: DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef = Field(..., json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...'})
    per_person_ventilation_rate_mode: Literal['CurrentOccupancy', 'DesignOccupancy'] | None = Field(default=None, json_schema_extra={'note': 'CurrentOccupancy models demand controlled ventilation using the current number of people DesignOccupancy uses the total Number of People in the zone and is constant'})


class AirTerminalSingleDuctConstantVolumeCooledBeam(IDFBaseModel):
    """Central air system terminal unit, single duct, constant volume, with cooled
beam (active or passive)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ConstantVolume:CooledBeam"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    cooled_beam_type: Literal['Active', 'Passive'] = Field(...)
    supply_air_inlet_node_name: str = Field(...)
    supply_air_outlet_node_name: str = Field(...)
    chilled_water_inlet_node_name: str = Field(...)
    chilled_water_outlet_node_name: str = Field(...)
    supply_air_volumetric_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    maximum_total_chilled_water_volumetric_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    number_of_beams: int | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'note': 'Number of individual beam units in the zone'})
    beam_length: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm', 'note': 'Length of an individual beam unit'})
    design_inlet_water_temperature: float | None = Field(default=15.0, ge=0.0, json_schema_extra={'units': 'C'})
    design_outlet_water_temperature: float | None = Field(default=17.0, ge=0.0, json_schema_extra={'units': 'C'})
    coil_surface_area_per_coil_length: float | None = Field(default=5.422, ge=0.0, json_schema_extra={'units': 'm2/m'})
    model_parameter_a: float | None = Field(default=15.3, ge=0.0)
    model_parameter_n1: float | None = Field(default=0.0, ge=0.0)
    model_parameter_n2: float | None = Field(default=0.84, ge=0.0)
    model_parameter_n3: float | None = Field(default=0.12, ge=0.0)
    model_parameter_a0: float | None = Field(default=0.171, ge=0.0, json_schema_extra={'units': 'm2/m', 'note': 'Free area of the coil in plan view per unit beam length'})
    model_parameter_k1: float | None = Field(default=0.0057, ge=0.0)
    model_parameter_n: float | None = Field(default=0.4, ge=0.0)
    coefficient_of_induction_kin: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate')
    leaving_pipe_inside_diameter: float | None = Field(default=0.0145, gt=0.0, json_schema_extra={'units': 'm'})


class AirTerminalSingleDuctConstantVolumeFourPipeBeam(IDFBaseModel):
    """Central air system terminal unit, single duct, constant volume, with heating
and/or cooling. Operates as two-pipe unit if heating or cooling water is
omitted. Heating and/or cooling can be scheduled off for dedicated
ventilation."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam"
    name: str = Field(...)
    primary_air_availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Primary air is supplied by central air handling unit and must be on for heating or cooling. Schedule value > 0 means the primary air supply is available. If this field is blank, the primary air sup...'})
    cooling_availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Cooling operation can be controlled separately using this availability schedule. Schedule value > 0 means beam cooling is available. If this field is blank, the beam cooling is always available (as...'})
    heating_availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Heating operation can be controlled separately using this availability schedule. Schedule value > 0 means beam heating is available. If this field is blank, the beam heating is always available (as...'})
    primary_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of the air system node for primary supply air entering the air distribution unit.'})
    primary_air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of the air system node for primary supply air leaving the air distribution unit and entering the zone.'})
    chilled_water_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Name of the plant system node for chilled water entering the beam. The two chilled water nodes can (only) be omitted to model a two-pipe heating only beam.'})
    chilled_water_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Name of the plant system node for chilled water leaving the beam.'})
    hot_water_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Name of the plant system node for hot water entering the beam. The two hot water nodes can (only) be omitted to model a two-pipe cooling-only beam.'})
    hot_water_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Name of the plant system node for hot water leaving the beam.'})
    design_primary_air_volume_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    design_chilled_water_volume_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    design_hot_water_volume_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    zone_total_beam_length: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm', 'note': 'Sum of the length of all the beam units in the zone represented by this terminal unit.'})
    rated_primary_air_flow_rate_per_beam_length: float | None = Field(default=0.035, gt=0.0, json_schema_extra={'units': 'm3/s-m', 'note': 'Primary air supply flow rate normalized by beam length.'})
    beam_rated_cooling_capacity_per_beam_length: float | None = Field(default=600.0, gt=0.0, json_schema_extra={'units': 'W/m', 'note': 'Sensible cooling capacity per meter of beam length at the rating point.'})
    beam_rated_cooling_room_air_chilled_water_temperature_difference: float | None = Field(default=10.0, gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'Difference in temperature between the zone air and the entering chilled water at the rating point.'})
    beam_rated_chilled_water_volume_flow_rate_per_beam_length: float | None = Field(default=5e-05, gt=0.0, json_schema_extra={'units': 'm3/s-m', 'note': 'The volume flow rate of chilled water per meter of beam length at the rating point.'})
    beam_cooling_capacity_temperature_difference_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam cooling capacity when the temperature difference between entering water and zone air is different than at the rating point. Single independent variable is the ratio of the current temp...'})
    beam_cooling_capacity_air_flow_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam cooling capacity when the primary air supply flow rate is different than at the rating point. The single independent variable is the current normalized air flow rate divided by the nor...'})
    beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam cooling capacity when the normalized chilled water flow rate is different than at the rating point. The single independent variable is the current normalized chilled water flow rate di...'})
    beam_rated_heating_capacity_per_beam_length: float | None = Field(default=1500.0, gt=0.0, json_schema_extra={'units': 'W/m', 'note': 'Sensible heating capacity per meter of beam length at the rating point.'})
    beam_rated_heating_room_air_hot_water_temperature_difference: float | None = Field(default=27.8, gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'Difference in temperature between the zone air and the entering hot water at the rating point.'})
    beam_rated_hot_water_volume_flow_rate_per_beam_length: float | None = Field(default=5e-05, gt=0.0, json_schema_extra={'units': 'm3/s-m', 'note': 'The volume flow rate of hot water per meter of beam length at the rating point.'})
    beam_heating_capacity_temperature_difference_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam heating capacity when the temperature difference between entering water and zone air is different than at the rating point. Single independent variable is the ratio of the current temp...'})
    beam_heating_capacity_air_flow_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam heating capacity when the primary air supply flow rate is different than at the rating point. The single independent variable is the current normalized air flow rate divided by the nor...'})
    beam_heating_capacity_hot_water_flow_modification_factor_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Adjusts beam heating capacity when the normalized hot water flow rate is different than at the rating point. The single independent variable is the current normalized hot water flow rate divided by...'})


class AirTerminalSingleDuctConstantVolumeFourPipeInduction(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, induction
unit with hot water reheat coil and chilled water recool coil."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    maximum_total_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    induction_ratio: float | None = Field(default=2.5, ge=0.0, json_schema_extra={'note': 'ratio of induced air flow rate to primary air flow rate'})
    supply_air_inlet_node_name: str = Field(...)
    induced_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'should be a zone exhaust node, also the heating coil inlet node'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'should be a zone inlet node'})
    heating_coil_object_type: Literal['Coil:Heating:Water'] = Field(...)
    heating_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when heating coil type is gas or electric'})
    minimum_hot_water_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when heating coil type is gas or electric'})
    heating_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    cooling_coil_object_type: Literal['Coil:Cooling:Water', 'Coil:Cooling:Water:DetailedGeometry'] | None = Field(default=None)
    cooling_coil_name: CoolingCoilNameRef | None = Field(default=None, json_schema_extra={'object_list': ['CoolingCoilName']})
    maximum_cold_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    minimum_cold_water_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s'})
    cooling_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    zone_mixer_name: ZoneMixersRef = Field(..., json_schema_extra={'object_list': ['ZoneMixers']})


class AirTerminalSingleDuctConstantVolumeNoReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, constant volume, without
reheat coil"""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ConstantVolume:NoReheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'The air-inlet node name that connects the air splitter to the individual zone air distribution unit. This node should also be one of the outlet air node of an AirLoopHVAC:ZoneSplitter or AirLoopHVA...'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'This is an air outlet node from the air distribution unit. This node name should be one of the supply air inlet node names of a zone served by this component.'})
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_specification_outdoor_air_object_name: (DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'This field is used to modulate the terminal unit flow rate based on the specified outdoor air requirement. When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit wil...'})
    per_person_ventilation_rate_mode: Literal['', 'CurrentOccupancy', 'DesignOccupancy'] | None = Field(default='CurrentOccupancy', json_schema_extra={'note': 'CurrentOccupancy uses current number of people in the zone which may vary DesignOccupancy uses the total number of people in the zone and is constant'})


class AirTerminalSingleDuctConstantVolumeReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, constant volume, with reheat
coil (hot water, electric, gas, or steam)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ConstantVolume:Reheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    reheat_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    reheat_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    maximum_reheat_air_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.'})


class AirTerminalSingleDuctMixer(IDFBaseModel):
    """The mixer air terminal unit provides a means of supplying central system air
to the air inlet or outlet side of a zoneHVAC equipment such as a four pipe
fan coil unit. Normally the central air would be ventilation air from a
dedicated outdoor air system (DOAS)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:Mixer"
    name: str = Field(...)
    zonehvac_unit_object_type: Literal['AirLoopHVAC:UnitarySystem', 'ZoneHVAC:FourPipeFanCoil', 'ZoneHVAC:PackagedTerminalAirConditioner', 'ZoneHVAC:PackagedTerminalHeatPump', 'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow', 'ZoneHVAC:UnitVentilator', 'ZoneHVAC:WaterToAirHeatPump'] = Field(..., json_schema_extra={'note': 'The type of ZoneHVAC equipment to which this terminal mixer will be connected.'})
    zonehvac_unit_object_name: DOAToZonalUnitRef = Field(..., json_schema_extra={'object_list': ['DOAToZonalUnit'], 'note': 'The name of ZoneHVAC equipment to which this terminal mixer will be connected.'})
    mixer_outlet_node_name: str = Field(..., json_schema_extra={'note': 'This is the outlet air node name of the mixer. This will be the inlet air node name of the ZoneHVAC equipment if the connection type in the input field Mixer Connection Type below is InletSide, els...'})
    mixer_primary_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'The primary air (treated outdoor air) inlet node name of the mixer. This will be an outlet air node name of an AirLoopHVAC:ZoneSplitter or AirLoopHVAC:SupplyPlenum providing the connection to the D...'})
    mixer_secondary_air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'The secondary air (recirculating air) inlet node name of the mixer. This will be the outlet air node name of the ZoneHVAC equipment if the connection type in the input field mixer Connection Type b...'})
    mixer_connection_type: Literal['InletSide', 'SupplySide'] = Field(..., json_schema_extra={'note': 'This input field allows user to specify the mixer connection type. Valid choices are InletSide or SupplySide. This is a required input field. If the mixer connection type selected is InletSide, the...'})
    design_specification_outdoor_air_object_name: (DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will adjust flow to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero, then the ou...'})
    per_person_ventilation_rate_mode: Literal['', 'CurrentOccupancy', 'DesignOccupancy'] | None = Field(default='CurrentOccupancy', json_schema_extra={'note': 'CurrentOccupancy models demand controlled ventilation using the current number of people DesignOccupancy uses the total Number of People in the zone and is constant'})


class AirTerminalSingleDuctParallelPIUReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, parallel
powered induction unit (PIU), with reheat coil (hot water, electric, gas, or
steam)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:ParallelPIU:Reheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    maximum_primary_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    maximum_secondary_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    minimum_primary_air_flow_fraction: float | Literal['Autosize'] = Field(..., json_schema_extra={'note': "When set to autosize, the calculated air flow is determined based on the System Outdoor Air Method used in the air loop's Sizing:System object."})
    fan_on_flow_fraction: float | Literal['Autosize'] = Field(..., json_schema_extra={'note': 'the fraction of the primary air flow at which fan turns on'})
    supply_air_inlet_node_name: str | None = Field(default=None)
    secondary_air_inlet_node_name: str | None = Field(default=None)
    outlet_node_name: str | None = Field(default=None)
    reheat_coil_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'mixer outlet node'})
    zone_mixer_name: ZoneMixersRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneMixers']})
    fan_name: (FansCVRef | FansSystemModelRef) | None = Field(default=None, json_schema_extra={'object_list': ['FansCV', 'FansSystemModel'], 'note': 'Fan type must be Fan:SystemModel or Fan:ConstantVolume'})
    reheat_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    reheat_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    fan_control_type: Literal['', 'ConstantSpeed', 'VariableSpeed'] | None = Field(default='ConstantSpeed', json_schema_extra={'note': 'If VariableSpeed, then the fan object type must be Fan:SystemModel'})
    minimum_fan_turn_down_ratio: float | None = Field(default=0.3, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'flow through terminal at minimum fan speed is this ratio multiplied by Maximum Air Flow Rate'})
    heating_control_type: Literal['Modulated', 'Staged'] | None = Field(default=None)
    design_heating_discharge_air_temperature: float | None = Field(default=32.1, json_schema_extra={'units': 'C', 'note': 'Only used if Heating Control Type is Modulated Used to control second stage heating, typically zone heat setpoint plus 20F'})
    high_limit_heating_discharge_air_temperature: float | None = Field(default=37.7, json_schema_extra={'units': 'C', 'note': 'Only used if Heating Control Type is Modulated Used to determine end of third stage heating'})


class AirTerminalSingleDuctSeriesPIUReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, series
powered induction unit (PIU), with reheat coil (hot water, electric, gas, or
steam)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:SeriesPIU:Reheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    maximum_primary_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    minimum_primary_air_flow_fraction: float | Literal['Autosize'] = Field(..., json_schema_extra={'note': "When set to autosize, the calculated air flow is determined based on the System Outdoor Air Method used in the air loop's Sizing:System object."})
    supply_air_inlet_node_name: str | None = Field(default=None)
    secondary_air_inlet_node_name: str | None = Field(default=None)
    outlet_node_name: str | None = Field(default=None)
    reheat_coil_air_inlet_node_name: str | None = Field(default=None)
    zone_mixer_name: ZoneMixersRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneMixers']})
    fan_name: (FansCVRef | FansSystemModelRef) | None = Field(default=None, json_schema_extra={'object_list': ['FansCV', 'FansSystemModel'], 'note': 'Fan type must be Fan:SystemModel or Fan:ConstantVolume'})
    reheat_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    reheat_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    fan_control_type: Literal['', 'ConstantSpeed', 'VariableSpeed'] | None = Field(default='ConstantSpeed', json_schema_extra={'note': 'If VariableSpeed, then the fan object type must be Fan:SystemModel'})
    minimum_fan_turn_down_ratio: float | None = Field(default=0.3, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'flow through terminal at minimum fan speed is this ratio multiplied by Maximum Air Flow Rate'})
    heating_control_type: Literal['Modulated', 'Staged'] | None = Field(default=None)
    design_heating_discharge_air_temperature: float | None = Field(default=32.1, json_schema_extra={'units': 'C', 'note': 'Only used if Heating Control Type is Modulated Used to control second stage heating, typically zone heat setpoint plus 20F'})
    high_limit_heating_discharge_air_temperature: float | None = Field(default=37.7, json_schema_extra={'units': 'C', 'note': 'Only used if Heating Control Type is Modulated Used to determine end of third stage heating'})


class AirTerminalSingleDuctVAVHeatAndCoolNoReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume for both
cooling and heating, with no reheat coil."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit. This is also the zone inlet node.'})
    air_inlet_node_name: str = Field(...)
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_fraction: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'note': 'fraction of maximum air flow'})
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the design minimum flow rate by multiplying it using this schedule of fraction values. This field is used with "Zone Minimum Air Flow Fraction". Schedule values are fractions 0.0...'})


class AirTerminalSingleDuctVAVHeatAndCoolReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume for both
cooling and heating, with reheat coil (hot water, electric, gas, or steam)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    damper_air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'the outlet node of the damper and the inlet node of the reheat coil this is an internal node to the terminal unit and connects the damper and reheat coil'})
    air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'the inlet node to the terminal unit and the damper'})
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_fraction: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'note': 'fraction of maximum air flow'})
    reheat_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    reheat_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit and the reheat coil. This is also the zone inlet node.'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    maximum_reheat_air_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.'})
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the design minimum flow rate by multiplying it using this schedule of fraction values. This field is used with "Zone Minimum Air Flow Fraction". Schedule values are fractions 0.0...'})


class AirTerminalSingleDuctVAVNoReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, with no
reheat coil."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:VAV:NoReheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    air_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_input_method: Literal['', 'Constant', 'FixedFlowRate', 'Scheduled'] | None = Field(default='Constant', json_schema_extra={'note': 'Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate) FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate) Scheduled = Scheduled Minimum ...'})
    constant_minimum_air_flow_fraction: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Constant If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional; if a value is entered, then...'})
    fixed_minimum_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s', 'note': 'This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate. If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional; if a value is entered...'})
    minimum_air_flow_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Scheduled Schedule values are fractions, 0.0 to 1.0. If the field Constant Minimum Air Flow Fraction is blank, then the average...'})
    design_specification_outdoor_air_object_name: (DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...'})
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the design minimum flow rate by multiplying it using this schedule of fraction values. This field can be used with any of the three "Zone Minimum Air Flow Input Method". Schedule...'})


class AirTerminalSingleDuctVAVReheat(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, with reheat
coil (hot water, electric, gas, or steam)."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:VAV:Reheat"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    damper_air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'the outlet node of the damper and the inlet node of the reheat coil this is an internal node to the terminal unit and connects the damper and reheat coil'})
    air_inlet_node_name: str = Field(..., json_schema_extra={'note': 'the inlet node to the terminal unit and the damper'})
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_input_method: Literal['', 'Constant', 'FixedFlowRate', 'Scheduled'] | None = Field(default='Constant', json_schema_extra={'note': 'Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate) FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate) Scheduled = Scheduled Minimum ...'})
    constant_minimum_air_flow_fraction: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Constant If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional; if a value is entered, then...'})
    fixed_minimum_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s', 'note': 'This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate. If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional; if a value is entered...'})
    minimum_air_flow_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Scheduled Schedule values are fractions, 0.0 to 1.0. If the field Constant Minimum Air Flow Fraction is blank, then the average...'})
    reheat_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    reheat_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when reheat coil type is gas or electric'})
    air_outlet_node_name: str = Field(..., json_schema_extra={'note': 'The outlet node of the terminal unit and the reheat coil. This is also the zone inlet node.'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    damper_heating_action: Literal['', 'Normal', 'Reverse', 'ReverseWithLimits'] | None = Field(default='ReverseWithLimits', json_schema_extra={'note': 'Normal means the damper is fixed at the minimum position in heating mode Reverse means the damper can open fully during reheat ReverseWithLimits means the damper will open partially during reheat a...'})
    maximum_flow_per_zone_floor_area_during_reheat: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s-m2', 'note': 'Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = ReverseWithLimits When autocalculating, the maximum flow per zone is set to 0.002032 m3/s-m2 (0.4 cfm/sqft) T...'})
    maximum_flow_fraction_during_reheat: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'note': 'Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = ReverseWithLimits When autocalculating, the maximum flow fraction is set to the ratio of 0.002032 m3/s-m2 (0....'})
    maximum_reheat_air_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.'})
    design_specification_outdoor_air_object_name: (DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'], 'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...'})
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the design minimum flow rate by multiplying it using this schedule of fraction values. This field can be used with any of the three "Zone Minimum Air Flow Input Method". Schedule...'})


class AirTerminalSingleDuctVAVReheatVariableSpeedFan(IDFBaseModel):
    """Central air system terminal unit, single duct, variable volume, with reheat
coil (hot water, electric, gas, or steam) and variable-speed fan. These
units are usually employed in underfloor air distribution (UFAD) systems
where the air is supplied at low static pressure through an underfloor
plenum. The fan is used to control the flow of conditioned air that enters
the space."""

    _idf_object_type: ClassVar[str] = "AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    maximum_cooling_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    maximum_heating_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    zone_minimum_air_flow_fraction: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'note': 'fraction of cooling air flow rate'})
    air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': "The name of the HVAC system node that is the air inlet node for the terminal unit. This is also the air inlet node for the unit's fan."})
    air_outlet_node_name: str | None = Field(default=None, json_schema_extra={'note': "The name of the HVAC system node that is the air outlet node for the terminal unit. This is also the air outlet node for the unit's heating coil's air outlet node. This node is also a zone inlet node."})
    fan_object_type: Literal['Fan:SystemModel', 'Fan:VariableVolume'] = Field(...)
    fan_name: FansSystemModelRef | FansVAVRef = Field(..., json_schema_extra={'object_list': ['FansSystemModel', 'FansVAV']})
    heating_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] = Field(...)
    heating_coil_name: HeatingCoilNameRef = Field(..., json_schema_extra={'object_list': ['HeatingCoilName']})
    maximum_hot_water_or_steam_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Not used when heating coil type is gas or electric'})
    minimum_hot_water_or_steam_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Not used when heating coil type is gas or electric'})
    heating_convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    minimum_air_flow_turndown_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field adjusts the fan-off minimum flow rate by multiplying it using this scheduled fraction values. This field is used with "Zone Minimum Air Flow Fraction". Schedule values are fractions 0.0 ...'})


class ZoneHVACAirDistributionUnit(IDFBaseModel):
    """Central air system air distribution unit, serves as a wrapper for a specific
type of air terminal unit. This object is referenced in a
ZoneHVAC:EquipmentList."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:AirDistributionUnit"
    name: str = Field(...)
    air_distribution_unit_outlet_node_name: str = Field(...)
    air_terminal_object_type: Literal['AirTerminal:DualDuct:ConstantVolume', 'AirTerminal:DualDuct:VAV', 'AirTerminal:DualDuct:VAV:OutdoorAir', 'AirTerminal:SingleDuct:ConstantVolume:CooledBeam', 'AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam', 'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction', 'AirTerminal:SingleDuct:ConstantVolume:NoReheat', 'AirTerminal:SingleDuct:ConstantVolume:Reheat', 'AirTerminal:SingleDuct:Mixer', 'AirTerminal:SingleDuct:ParallelPIU:Reheat', 'AirTerminal:SingleDuct:SeriesPIU:Reheat', 'AirTerminal:SingleDuct:UserDefined', 'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat', 'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat', 'AirTerminal:SingleDuct:VAV:NoReheat', 'AirTerminal:SingleDuct:VAV:Reheat', 'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan'] = Field(...)
    air_terminal_name: AirTerminalUnitNamesRef = Field(..., json_schema_extra={'object_list': ['AirTerminalUnitNames']})
    nominal_upstream_leakage_fraction: float | None = Field(default=0.0, ge=0.0, le=0.3, json_schema_extra={'note': 'fraction at system design Flow; leakage Flow constant, leakage fraction varies with variable system Flow Rate.'})
    constant_downstream_leakage_fraction: float | None = Field(default=0.0, ge=0.0, le=0.3)
    design_specification_air_terminal_sizing_object_name: DesignSpecificationAirTerminalSizingNameRef | None = Field(default=None, json_schema_extra={'object_list': ['DesignSpecificationAirTerminalSizingName'], 'note': 'This optional field is the name of a DesignSpecification:AirTerminal:Sizing object which specifies sizing adjustments to be made for this terminal unit.'})


class ZoneHVACExhaustControl(IDFBaseModel):
    """Defines a controlled exhaust flow from a zone which finally feeds into one
of AirLoopHVAC:ZoneMixer's inlets, which are part of an
AirLoopHVAC:ExhaustSystem."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:ExhaustControl"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this exhaust system. Schedule value > 0 means it is available. If this field is blank, the exhaust system is always available. If the attached AirLoopHVAC:ExhaustSyst...'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the exhaust inlet node is part of'})
    inlet_node_name: str = Field(..., json_schema_extra={'note': 'Inlet node name for the exhaust. Must be a zone exhaust node.'})
    outlet_node_name: str = Field(..., json_schema_extra={'note': 'Outlet node name for the exhaust'})
    design_exhaust_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    flow_control_type: Literal['', 'FollowSupply', 'Scheduled'] | None = Field(default='Scheduled', json_schema_extra={'note': 'Control type of the zone exhaust flow'})
    exhaust_flow_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule name of the exhaust flow fraction. Used only with Scheduled control type. If this field is blank, the flow fraction is always 1.0.'})
    supply_node_or_nodelist_name: str | None = Field(default=None, json_schema_extra={'note': 'Used only with FollowSupply control type.'})
    minimum_zone_temperature_limit_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule name of the Minimum Zone Temperature Limit in degree Celsius If this field is blank, there is no limit.'})
    minimum_exhaust_flow_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule name of the minimum exhaust flow fraction. Applied when the zone temperature falls below the Minimum Zone Temperature Limit.'})
    balanced_exhaust_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule name of the Balanced Exhaust Fraction.'})

