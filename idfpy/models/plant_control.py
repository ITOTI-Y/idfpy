"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Plant-Condenser Control
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ChillersRef,
    ControlSchemeListRef,
    IceThermalStorageEquipmentRef,
    PlantAndCondenserEquipmentListsRef,
    PLHPCoolingNamesRef,
    PLHPHeatingNamesRef,
    ScheduleNamesRef,
    ValidCondenserEquipmentNamesRef,
    ValidCondenserEquipmentTypesRef,
    ValidPlantEquipmentNamesRef,
    ValidPlantEquipmentTypesRef,
    ZoneListNamesRef,
)


class CondenserEquipmentListEquipmentItem(IDFBaseModel):
    """Nested object type for array items."""

    equipment_object_type: ValidCondenserEquipmentTypesRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['validCondenserEquipmentTypes']},
    )
    equipment_name: ValidCondenserEquipmentNamesRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['validCondenserEquipmentNames']},
    )


class PlantEquipmentListEquipmentItem(IDFBaseModel):
    """Nested object type for array items."""

    equipment_object_type: ValidPlantEquipmentTypesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validPlantEquipmentTypes']}
    )
    equipment_name: ValidPlantEquipmentNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['validPlantEquipmentNames']}
    )


class CondenserEquipmentList(IDFBaseModel):
    """List condenser equipment in order of operating priority, 1st in list will be
    used 1st, etc Use only condenser equipment in this list. If no equipment
    object types and equipment names are specified, then the corresponding
    PlantEquipmentOperation:* object will assume all available condenser
    equipment for the loop should be OFF (not operate) within the specified
    lower/upper limit."""

    _idf_object_type: ClassVar[str] = 'CondenserEquipmentList'
    name: str = Field(...)
    equipment: list[CondenserEquipmentListEquipmentItem] | None = Field(default=None)


class CondenserEquipmentOperationSchemes(IDFBaseModel):
    """Operation schemes are listed in \"priority\" order. Note that each scheme
    must address the entire load and/or condition ranges for the simulation. The
    actual one selected for use will be the first that is \"Scheduled\" on. That
    is, if control scheme 1 is not \"on\" and control scheme 2 is -- then
    control scheme 2 is selected. Only condenser equipment should be listed on a
    Control Scheme for this item."""

    _idf_object_type: ClassVar[str] = 'CondenserEquipmentOperationSchemes'
    name: str = Field(...)
    control_scheme_1_object_type: Literal[
        'PlantEquipmentOperation:CoolingLoad',
        'PlantEquipmentOperation:HeatingLoad',
        'PlantEquipmentOperation:OutdoorDewpoint',
        'PlantEquipmentOperation:OutdoorDewpointDifference',
        'PlantEquipmentOperation:OutdoorDryBulb',
        'PlantEquipmentOperation:OutdoorDryBulbDifference',
        'PlantEquipmentOperation:OutdoorRelativeHumidity',
        'PlantEquipmentOperation:OutdoorWetBulb',
        'PlantEquipmentOperation:OutdoorWetBulbDifference',
        'PlantEquipmentOperation:Uncontrolled',
        'PlantEquipmentOperation:UserDefined',
    ] = Field(...)
    control_scheme_1_name: ControlSchemeListRef = Field(
        ..., json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_1_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_2_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_2_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_2_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_3_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_3_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_3_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_4_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_4_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_4_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_5_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_5_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_5_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_6_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_6_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_6_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_7_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_7_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_7_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_8_object_type: (
        Literal[
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_8_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_8_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class PlantEquipmentList(IDFBaseModel):
    """List plant equipment in order of operating priority, 1st in list will be
    used 1st, etc Use only plant equipment in this list. If no equipment object
    types and equipment names are specified, then the corresponding
    PlantEquipmentOperation:* object will assume all available plant equipment
    for the loop should be OFF (not operate) within the specified lower/upper
    limit."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentList'
    name: str = Field(...)
    equipment: list[PlantEquipmentListEquipmentItem] | None = Field(default=None)


class PlantEquipmentOperationChillerHeaterChangeover(IDFBaseModel):
    """Plant equipment operation object to control switchover between chiller and
    heater operation of chiller heater heat pump serving 2 plant loops. Poll
    zone loads and determine if plant should be in heating, cooling or
    simultaneous heating and cooling and dispatch equipment accordingly."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:ChillerHeaterChangeover'
    name: str = Field(...)
    primary_cooling_plant_setpoint_temperature: float = Field(
        ..., ge=-10.0, le=20.0, json_schema_extra={'units': 'C'}
    )
    secondary_distribution_cooling_plant_setpoint_temperature: float | None = Field(
        default=None, ge=0.0, le=20.0, json_schema_extra={'units': 'C'}
    )
    primary_heating_plant_setpoint_at_outdoor_high_temperature: float = Field(
        ..., ge=20.0, le=80.0, json_schema_extra={'units': 'C'}
    )
    outdoor_high_temperature: float = Field(
        ..., ge=0.0, le=35.0, json_schema_extra={'units': 'C'}
    )
    primary_heating_plant_setpoint_at_outdoor_low_temperature: float = Field(
        ..., ge=20.0, le=80.0, json_schema_extra={'units': 'C'}
    )
    outdoor_low_temperature: float = Field(
        ..., ge=-35.0, le=35.0, json_schema_extra={'units': 'C'}
    )
    secondary_distribution_heating_plant_setpoint_temperature: float | None = Field(
        default=None, ge=20.0, le=80.0, json_schema_extra={'units': 'C'}
    )
    zone_load_polling_zonelist_name: ZoneListNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneListNames']}
    )
    cooling_only_load_plant_equipment_operation_cooling_load_name: (
        ControlSchemeListRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['ControlSchemeList']})
    heating_only_load_plant_equipment_operation_heating_load_name: (
        ControlSchemeListRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['ControlSchemeList']})
    simultaneous_cooling_and_heating_plant_equipment_operation_cooling_load_name: (
        ControlSchemeListRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['ControlSchemeList']})
    simultaneous_cooling_and_heating_plant_equipment_operation_heating_load_name: (
        ControlSchemeListRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['ControlSchemeList']})
    dedicated_chilled_water_return_recovery_heat_pump_name: (
        PLHPCoolingNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PLHPCoolingNames'],
            'note': 'enter name of HeatPump:PlantLoop:EIR:Cooling object to control chilled water return adding heat to hot water return',
        },
    )
    dedicated_hot_water_return_recovery_heat_pump_name: PLHPHeatingNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['PLHPHeatingNames'],
                'note': 'enter name of HeatPump:PlantLoop:EIR:Heating object to control hot water return cooling the chilled water return',
            },
        )
    )
    boiler_setpoint_temperature_offset: float | None = Field(
        default=0.5, json_schema_extra={'units': 'deltaC'}
    )
    primary_heating_plant_setpoint_at_backup_outdoor_low_temperature: float | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'C',
                'note': 'if empty or not used then set equal to Primary Heating Plant Setpoint at Outdoor Low Temperature',
            },
        )
    )
    backup_outdoor_low_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )


class PlantEquipmentOperationComponentSetpoint(IDFBaseModel):
    """Plant equipment operation scheme for component setpoint operation. Specifies
    one or pieces of equipment which are controlled to meet the temperature
    setpoint at the component outlet node."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:ComponentSetpoint'
    name: str = Field(...)
    equipment_1_object_type: str = Field(...)
    equipment_1_name: str = Field(...)
    demand_calculation_1_node_name: str = Field(...)
    setpoint_1_node_name: str = Field(...)
    component_1_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    operation_1_type: Literal['Cooling', 'Dual', 'Heating'] = Field(...)
    equipment_2_object_type: str | None = Field(default=None)
    equipment_2_name: str | None = Field(default=None)
    demand_calculation_2_node_name: str | None = Field(default=None)
    setpoint_2_node_name: str | None = Field(default=None)
    component_2_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_2_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_3_object_type: str | None = Field(default=None)
    equipment_3_name: str | None = Field(default=None)
    demand_calculation_3_node_name: str | None = Field(default=None)
    setpoint_3_node_name: str | None = Field(default=None)
    component_3_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_3_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_4_object_type: str | None = Field(default=None)
    equipment_4_name: str | None = Field(default=None)
    demand_calculation_4_node_name: str | None = Field(default=None)
    setpoint_4_node_name: str | None = Field(default=None)
    component_4_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_4_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_5_object_type: str | None = Field(default=None)
    equipment_5_name: str | None = Field(default=None)
    demand_calculation_5_node_name: str | None = Field(default=None)
    setpoint_5_node_name: str | None = Field(default=None)
    component_5_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_5_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_6_object_type: str | None = Field(default=None)
    equipment_6_name: str | None = Field(default=None)
    demand_calculation_6_node_name: str | None = Field(default=None)
    setpoint_6_node_name: str | None = Field(default=None)
    component_6_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_6_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_7_object_type: str | None = Field(default=None)
    equipment_7_name: str | None = Field(default=None)
    demand_calculation_7_node_name: str | None = Field(default=None)
    setpoint_7_node_name: str | None = Field(default=None)
    component_7_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_7_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_8_object_type: str | None = Field(default=None)
    equipment_8_name: str | None = Field(default=None)
    demand_calculation_8_node_name: str | None = Field(default=None)
    setpoint_8_node_name: str | None = Field(default=None)
    component_8_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_8_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_9_object_type: str | None = Field(default=None)
    equipment_9_name: str | None = Field(default=None)
    demand_calculation_9_node_name: str | None = Field(default=None)
    setpoint_9_node_name: str | None = Field(default=None)
    component_9_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_9_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(default=None)
    equipment_10_object_type: str | None = Field(default=None)
    equipment_10_name: str | None = Field(default=None)
    demand_calculation_10_node_name: str | None = Field(default=None)
    setpoint_10_node_name: str | None = Field(default=None)
    component_10_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    operation_10_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )


class PlantEquipmentOperationCoolingLoad(IDFBaseModel):
    """Plant equipment operation scheme for cooling load range operation. Specifies
    one or more groups of equipment which are available to operate for
    successive cooling load ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:CoolingLoad'
    name: str = Field(...)
    load_range_1_lower_limit: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_1_upper_limit: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_2_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_2_upper_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_3_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_3_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_4_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_4_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_5_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_5_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_6_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_6_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_7_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_7_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_8_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_8_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_9_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_9_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_10_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_10_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationHeatingLoad(IDFBaseModel):
    """Plant equipment operation scheme for heating load range operation. Specifies
    one or more groups of equipment which are available to operate for
    successive heating load ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:HeatingLoad'
    name: str = Field(...)
    load_range_1_lower_limit: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_1_upper_limit: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    load_range_2_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_2_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_3_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_3_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_4_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_4_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_5_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_5_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_6_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_6_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_7_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_7_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_8_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_8_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_9_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_9_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    load_range_10_lower_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    load_range_10_upper_limit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorDewpoint(IDFBaseModel):
    """Plant equipment operation scheme for outdoor dewpoint temperature range
    operation. Specifies one or more groups of equipment which are available to
    operate for successive outdoor dewpoint temperature ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorDewpoint'
    name: str = Field(...)
    dewpoint_temperature_range_1_lower_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_1_upper_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    dewpoint_temperature_range_2_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_2_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_3_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_3_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_4_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_4_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_5_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_5_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_6_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_6_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_7_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_7_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_8_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_8_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_9_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_9_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_range_10_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dewpoint_temperature_range_10_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorDewpointDifference(IDFBaseModel):
    """Plant equipment operation scheme for outdoor dewpoint temperature difference
    operation. Specifies one or more groups of equipment which are available to
    operate for successive ranges based the difference between a reference node
    temperature and the outdoor dewpoint temperature."""

    _idf_object_type: ClassVar[str] = (
        'PlantEquipmentOperation:OutdoorDewpointDifference'
    )
    name: str = Field(...)
    reference_temperature_node_name: str = Field(...)
    dewpoint_temperature_difference_range_1_lower_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_1_upper_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    dewpoint_temperature_difference_range_2_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_2_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_3_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_3_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_4_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_4_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_5_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_5_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_6_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_6_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_7_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_7_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_8_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_8_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_9_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_9_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dewpoint_temperature_difference_range_10_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dewpoint_temperature_difference_range_10_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorDryBulb(IDFBaseModel):
    """Plant equipment operation scheme for outdoor dry-bulb temperature range
    operation. Specifies one or more groups of equipment which are available to
    operate for successive outdoor dry-bulb temperature ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorDryBulb'
    name: str = Field(...)
    dry_bulb_temperature_range_1_lower_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_1_upper_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    dry_bulb_temperature_range_2_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_2_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_3_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_3_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_4_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_4_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_5_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_5_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_6_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_6_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_7_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_7_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_8_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_8_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_9_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_9_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_range_10_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    dry_bulb_temperature_range_10_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorDryBulbDifference(IDFBaseModel):
    """Plant equipment operation scheme for outdoor dry-bulb temperature difference
    operation. Specifies one or more groups of equipment which are available to
    operate for successive ranges based the difference between a reference node
    temperature and the outdoor dry-bulb temperature."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorDryBulbDifference'
    name: str = Field(...)
    reference_temperature_node_name: str = Field(...)
    dry_bulb_temperature_difference_range_1_lower_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_1_upper_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    dry_bulb_temperature_difference_range_2_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_2_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_3_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_3_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_4_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_4_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_5_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_5_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_6_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_6_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_7_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_7_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_8_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_8_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_9_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_9_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    dry_bulb_temperature_difference_range_10_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    dry_bulb_temperature_difference_range_10_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorRelativeHumidity(IDFBaseModel):
    """Plant equipment operation scheme for outdoor relative humidity range
    operation. Specifies one or more groups of equipment which are available to
    operate for successive outdoor relative humidity ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorRelativeHumidity'
    name: str = Field(...)
    relative_humidity_range_1_lower_limit: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_1_upper_limit: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    relative_humidity_range_2_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_2_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_3_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_3_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_4_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_4_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_5_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_5_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_6_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_6_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_7_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_7_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_8_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_8_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_9_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_9_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    relative_humidity_range_10_lower_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    relative_humidity_range_10_upper_limit: float | None = Field(
        default=None, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorWetBulb(IDFBaseModel):
    """Plant equipment operation scheme for outdoor wet-bulb temperature range
    operation. Specifies one or more groups of equipment which are available to
    operate for successive outdoor wet-bulb temperature ranges."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorWetBulb'
    name: str = Field(...)
    wet_bulb_temperature_range_1_lower_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_1_upper_limit: float = Field(
        ..., ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    wet_bulb_temperature_range_2_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_2_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_3_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_3_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_4_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_4_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_5_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_5_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_6_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_6_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_7_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_7_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_8_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_8_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_9_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_9_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_range_10_lower_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    wet_bulb_temperature_range_10_upper_limit: float | None = Field(
        default=None, ge=-70.0, le=70.0, json_schema_extra={'units': 'C'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationOutdoorWetBulbDifference(IDFBaseModel):
    """Plant equipment operation scheme for outdoor wet-bulb temperature difference
    operation. Specifies one or more groups of equipment which are available to
    operate for successive ranges based the difference between a reference node
    temperature and the outdoor wet-bulb temperature."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:OutdoorWetBulbDifference'
    name: str = Field(...)
    reference_temperature_node_name: str = Field(...)
    wet_bulb_temperature_difference_range_1_lower_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_1_upper_limit: float = Field(
        ..., ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_1_equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
    wet_bulb_temperature_difference_range_2_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_2_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_2_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_3_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_3_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_3_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_4_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_4_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_4_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_5_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_5_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_5_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_6_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_6_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_6_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_7_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_7_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_7_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_8_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_8_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_8_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_9_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_9_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_9_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )
    wet_bulb_temperature_difference_range_10_lower_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    wet_bulb_temperature_difference_range_10_upper_limit: float | None = Field(
        default=None, ge=-50.0, le=100.0, json_schema_extra={'units': 'deltaC'}
    )
    range_10_equipment_list_name: PlantAndCondenserEquipmentListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']},
    )


class PlantEquipmentOperationSchemes(IDFBaseModel):
    """Operation schemes are listed in \"priority\" order. Note that each scheme
    must address the entire load and/or condition ranges for the simulation. The
    actual one selected for use will be the first that is \"Scheduled\" on. That
    is, if control scheme 1 is not \"on\" and control scheme 2 is -- then
    control scheme 2 is selected. Only plant equipment should be listed on a
    Control Scheme for this item."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperationSchemes'
    name: str = Field(...)
    control_scheme_1_object_type: Literal[
        'PlantEquipmentOperation:ChillerHeaterChangeover',
        'PlantEquipmentOperation:ComponentSetpoint',
        'PlantEquipmentOperation:CoolingLoad',
        'PlantEquipmentOperation:HeatingLoad',
        'PlantEquipmentOperation:OutdoorDewpoint',
        'PlantEquipmentOperation:OutdoorDewpointDifference',
        'PlantEquipmentOperation:OutdoorDryBulb',
        'PlantEquipmentOperation:OutdoorDryBulbDifference',
        'PlantEquipmentOperation:OutdoorRelativeHumidity',
        'PlantEquipmentOperation:OutdoorWetBulb',
        'PlantEquipmentOperation:OutdoorWetBulbDifference',
        'PlantEquipmentOperation:ThermalEnergyStorage',
        'PlantEquipmentOperation:Uncontrolled',
        'PlantEquipmentOperation:UserDefined',
    ] = Field(...)
    control_scheme_1_name: ControlSchemeListRef = Field(
        ..., json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_1_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_2_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_2_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_2_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_3_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_3_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_3_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_4_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_4_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_4_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_5_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_5_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_5_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_6_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_6_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_6_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_7_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_7_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_7_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    control_scheme_8_object_type: (
        Literal[
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
            'PlantEquipmentOperation:UserDefined',
        ]
        | None
    ) = Field(default=None)
    control_scheme_8_name: ControlSchemeListRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ControlSchemeList']}
    )
    control_scheme_8_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class PlantEquipmentOperationThermalEnergyStorage(IDFBaseModel):
    """Plant equipment operation scheme for simpler input to control thermal (ice)
    energy storage systems. It replaces a host of setpoint managers with simple,
    single input values. For more complex controls, use the ComponentSetpoint
    scheme."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:ThermalEnergyStorage'
    name: str = Field(...)
    on_peak_schedule: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    charging_availability_schedule: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    non_charging_chilled_water_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'Single temperature for chiller outlet when not in cooling season or during on-peak cooling (discharge)',
        },
    )
    charging_chilled_water_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'Single temperature for chiller outlet when off-peak during cooling season (charging)',
        },
    )
    component_1_object_type: Literal[
        'Chiller:Absorption',
        'Chiller:Absorption:Indirect',
        'Chiller:CombustionTurbine',
        'Chiller:ConstantCOP',
        'Chiller:Electric',
        'Chiller:Electric:EIR',
        'Chiller:Electric:ReformulatedEIR',
        'Chiller:EngineDriven',
        'ThermalStorage:Ice:Detailed',
        'ThermalStorage:Ice:Simple',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'This field is the type of object and should either be a chiller or some ice storage equipment.'
        },
    )
    component_1_name: ChillersRef | IceThermalStorageEquipmentRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Chillers', 'IceThermalStorageEquipment'],
            'note': 'This field is the name of either the chiller or ice storage equipment on the loop.',
        },
    )
    component_1_demand_calculation_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This field is the name of the inlet node for the component defined in the two previous input fields.'
        },
    )
    component_1_setpoint_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This field is the name of the outlet node for the component listed above.'
        },
    )
    component_1_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is the flow rate for the component listed above.',
        },
    )
    component_1_operation_type: Literal['Cooling', 'Dual', 'Heating'] = Field(
        ...,
        json_schema_extra={
            'note': 'This field is the operation type for the component listed above. For this plant equipment operation scheme, "Cooling" should be selected for chiller equipment while ice storage equipment should be ...'
        },
    )
    component_2_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_2_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_2_demand_calculation_node_name: str | None = Field(default=None)
    component_2_setpoint_node_name: str | None = Field(default=None)
    component_2_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_2_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_3_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_3_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_3_demand_calculation_node_name: str | None = Field(default=None)
    component_3_setpoint_node_name: str | None = Field(default=None)
    component_3_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_3_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_4_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_4_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_4_demand_calculation_node_name: str | None = Field(default=None)
    component_4_setpoint_node_name: str | None = Field(default=None)
    component_4_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_4_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_5_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_5_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_5_demand_calculation_node_name: str | None = Field(default=None)
    component_5_setpoint_node_name: str | None = Field(default=None)
    component_5_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_5_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_6_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_6_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_6_demand_calculation_node_name: str | None = Field(default=None)
    component_6_setpoint_node_name: str | None = Field(default=None)
    component_6_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_6_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_7_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_7_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_7_demand_calculation_node_name: str | None = Field(default=None)
    component_7_setpoint_node_name: str | None = Field(default=None)
    component_7_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_7_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_8_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_8_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_8_demand_calculation_node_name: str | None = Field(default=None)
    component_8_setpoint_node_name: str | None = Field(default=None)
    component_8_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_8_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_9_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_9_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_9_demand_calculation_node_name: str | None = Field(default=None)
    component_9_setpoint_node_name: str | None = Field(default=None)
    component_9_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_9_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )
    component_10_object_type: (
        Literal[
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        ]
        | None
    ) = Field(default=None)
    component_10_name: (ChillersRef | IceThermalStorageEquipmentRef) | None = Field(
        default=None,
        json_schema_extra={'object_list': ['Chillers', 'IceThermalStorageEquipment']},
    )
    component_10_demand_calculation_node_name: str | None = Field(default=None)
    component_10_setpoint_node_name: str | None = Field(default=None)
    component_10_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    component_10_operation_type: Literal['Cooling', 'Dual', 'Heating'] | None = Field(
        default=None
    )


class PlantEquipmentOperationUncontrolled(IDFBaseModel):
    """Plant equipment operation scheme for uncontrolled operation. Specifies a
    group of equipment that runs if the loop is active, unless turned off by the
    loop flow resolver to maintain continuity in the fluid loop."""

    _idf_object_type: ClassVar[str] = 'PlantEquipmentOperation:Uncontrolled'
    name: str = Field(...)
    equipment_list_name: PlantAndCondenserEquipmentListsRef = Field(
        ..., json_schema_extra={'object_list': ['PlantAndCondenserEquipmentLists']}
    )
