"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Setpoint Managers
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AirPrimaryLoopsRef,
    QuadvariateFunctionsRef,
    ScheduleNamesRef,
    ZoneNamesRef,
)


class SetpointManagerColdest(IDFBaseModel):
    """This SetpointManager is used in dual duct systems to reset the setpoint
    temperature of the air in the heating supply duct. Usually it is used in
    conjunction with a SetpointManager:Warmest resetting the temperature of the
    air in the cooling supply duct."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:Coldest'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object.',
        },
    )
    minimum_setpoint_temperature: float | None = Field(
        default=20.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=50.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    strategy: Literal['', 'MinimumTemperature'] | None = Field(
        default='MinimumTemperature'
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerCondenserEnteringReset(IDFBaseModel):
    """This setpoint manager uses one curve to determine the optimum condenser
    entering water temperature for a given timestep and two other curves to
    place boundary conditions on the setpoint value."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:CondenserEnteringReset'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    default_condenser_entering_water_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This scheduled setpoint value is only used in a given timestep if the "Optimized" Condenser Entering Temperature does not fall within the prescribed boundary conditions.',
        },
    )
    minimum_design_wetbulb_temperature_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    minimum_outside_air_wetbulb_temperature_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    optimized_cond_entering_water_temperature_curve_name: QuadvariateFunctionsRef = (
        Field(..., json_schema_extra={'object_list': ['QuadvariateFunctions']})
    )
    minimum_lift: float | None = Field(
        default=11.1, json_schema_extra={'units': 'deltaC'}
    )
    maximum_condenser_entering_water_temperature: float | None = Field(
        default=32.0, json_schema_extra={'units': 'C'}
    )
    cooling_tower_design_inlet_air_wet_bulb_temperature: float | None = Field(
        default=25.56, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerCondenserEnteringResetIdeal(IDFBaseModel):
    """This setpoint manager determine the ideal optimum condenser entering water
    temperature setpoint for a given timestep."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:CondenserEnteringReset:Ideal'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    minimum_lift: float | None = Field(
        default=11.1, json_schema_extra={'units': 'deltaC'}
    )
    maximum_condenser_entering_water_temperature: float | None = Field(
        default=32.0, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerFollowGroundTemperature(IDFBaseModel):
    """This setpoint manager is used to place a temperature setpoint on a system
    node that is derived from a current ground temperature. The ground
    temperatures are specified in different Site:GroundTemperature:* objects and
    used during the simulation. This setpoint manager is primarily intended for
    condenser or plant loops using some type of ground heat exchanger."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:FollowGroundTemperature'
    name: str = Field(...)
    control_variable: (
        Literal['', 'MaximumTemperature', 'MinimumTemperature', 'Temperature'] | None
    ) = Field(default='Temperature')
    reference_ground_temperature_object_type: (
        Literal[
            'Site:GroundTemperature:BuildingSurface',
            'Site:GroundTemperature:Deep',
            'Site:GroundTemperature:FCfactorMethod',
            'Site:GroundTemperature:Shallow',
        ]
        | None
    ) = Field(default=None)
    offset_temperature_difference: float | None = Field(
        default=None, json_schema_extra={'units': 'deltaC'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    minimum_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerFollowOutdoorAirTemperature(IDFBaseModel):
    """This setpoint manager is used to place a temperature setpoint on a system
    node that is derived from the current outdoor air environmental conditions.
    The outdoor air conditions are obtained from the weather information during
    the simulation."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:FollowOutdoorAirTemperature'
    name: str = Field(...)
    control_variable: (
        Literal['', 'MaximumTemperature', 'MinimumTemperature', 'Temperature'] | None
    ) = Field(default='Temperature')
    reference_temperature_type: (
        Literal['', 'OutdoorAirDryBulb', 'OutdoorAirWetBulb'] | None
    ) = Field(default='OutdoorAirWetBulb')
    offset_temperature_difference: float | None = Field(
        default=None, json_schema_extra={'units': 'deltaC'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    minimum_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerFollowSystemNodeTemperature(IDFBaseModel):
    """This setpoint manager is used to place a temperature setpoint on a system
    node that is derived from the current temperatures at a separate system
    node. The current value of the temperature at a reference node is obtained
    and used to generate setpoint on a second system node. If the reference node
    is also designated to be an outdoor air (intake) node, then this setpoint
    manager can be used to follow outdoor air conditions that are adjusted for
    altitude."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:FollowSystemNodeTemperature'
    name: str = Field(...)
    control_variable: (
        Literal['', 'MaximumTemperature', 'MinimumTemperature', 'Temperature'] | None
    ) = Field(default='Temperature')
    reference_node_name: str | None = Field(default=None)
    reference_temperature_type: Literal['', 'NodeDryBulb', 'NodeWetBulb'] | None = (
        Field(default='NodeDryBulb')
    )
    offset_temperature_difference: float | None = Field(
        default=None, json_schema_extra={'units': 'deltaC'}
    )
    maximum_limit_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    minimum_limit_setpoint_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerMixedAir(IDFBaseModel):
    """The Mixed Air Setpoint Manager is meant to be used in conjunction with a
    Controller:OutdoorAir object. This setpoint manager is used to establish a
    temperature setpoint at the mixed air node."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:MixedAir'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    reference_setpoint_node_name: str = Field(...)
    fan_inlet_node_name: str = Field(...)
    fan_outlet_node_name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )
    cooling_coil_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Optional field used to limit economizer operation to prevent freezing of DX cooling coil.'
        },
    )
    cooling_coil_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Optional field used to limit economizer operation to prevent freezing of DX cooling coil.'
        },
    )
    minimum_temperature_at_cooling_coil_outlet_node: float | None = Field(
        default=7.2,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Optional field used to limit economizer operation to prevent freezing of DX cooling coil.',
        },
    )


class SetpointManagerMultiZoneCoolingAverage(IDFBaseModel):
    """This setpoint manager sets the average supply air temperature based on the
    cooling load requirements of all controlled zones in an air loop served by a
    central air-conditioner."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:MultiZone:Cooling:Average'
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_temperature: float | None = Field(
        default=12.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=18.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerMultiZoneHeatingAverage(IDFBaseModel):
    """This setpoint manager sets the average supply air temperature based on the
    heating load requirements of all controlled zones in an air loop served by a
    central air-conditioner."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:MultiZone:Heating:Average'
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_temperature: float | None = Field(
        default=20.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=50.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerMultiZoneHumidityMaximum(IDFBaseModel):
    """This setpoint manager sets the maximum supply air humidity ratio based on
    dehumidification requirements of a controlled zone with critical humidity
    ratio setpoint (i.e., a zone with the lowest humidity ratio setpoint) in an
    air loop served by a central air-conditioner."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:MultiZone:Humidity:Maximum'
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_humidity_ratio: float | None = Field(
        default=0.008, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_setpoint_humidity_ratio: float | None = Field(
        default=0.015, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={'note': 'Node(s) at which the humidity ratio will be set'},
    )


class SetpointManagerMultiZoneHumidityMinimum(IDFBaseModel):
    """This setpoint manager sets the minimum supply air humidity ratio based on
    humidification requirements of a controlled zone with critical humidity
    ratio setpoint (i.e., a zone with the highest humidity ratio setpoint) in an
    air loop served by a central air-conditioner."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:MultiZone:Humidity:Minimum'
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_humidity_ratio: float | None = Field(
        default=0.005, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_setpoint_humidity_ratio: float | None = Field(
        default=0.012, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={'note': 'Node(s) at which the humidity ratio will be set'},
    )


class SetpointManagerMultiZoneMaximumHumidityAverage(IDFBaseModel):
    """This setpoint manager sets the average supply air maximum humidity ratio
    based on moisture load requirements of all controlled zones in an air loop
    served by a central air-conditioner."""

    _idf_object_type: ClassVar[str] = (
        'SetpointManager:MultiZone:MaximumHumidity:Average'
    )
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_humidity_ratio: float | None = Field(
        default=0.008, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_setpoint_humidity_ratio: float | None = Field(
        default=0.015, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={'note': 'Node(s) at which the humidity ratio will be set'},
    )


class SetpointManagerMultiZoneMinimumHumidityAverage(IDFBaseModel):
    """This setpoint manager sets the average supply air minimum humidity ratio
    based on moisture load requirements of all controlled zones in an air loop
    served by a central air-conditioner."""

    _idf_object_type: ClassVar[str] = (
        'SetpointManager:MultiZone:MinimumHumidity:Average'
    )
    name: str = Field(...)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_humidity_ratio: float | None = Field(
        default=0.005, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_setpoint_humidity_ratio: float | None = Field(
        default=0.012, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={'note': 'Node(s) at which the humidity ratio will be set'},
    )


class SetpointManagerOutdoorAirPretreat(IDFBaseModel):
    """This setpoint manager determines the required conditions at the outdoor air
    stream node which will produce the reference setpoint condition at the mixed
    air node when mixed with the return air stream"""

    _idf_object_type: ClassVar[str] = 'SetpointManager:OutdoorAirPretreat'
    name: str = Field(...)
    control_variable: (
        Literal[
            'HumidityRatio',
            'MaximumHumidityRatio',
            'MinimumHumidityRatio',
            'Temperature',
        ]
        | None
    ) = Field(default=None)
    minimum_setpoint_temperature: float | None = Field(
        default=-99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only if Control variable is Temperature',
        },
    )
    maximum_setpoint_temperature: float | None = Field(
        default=99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only if Control variable is Temperature',
        },
    )
    minimum_setpoint_humidity_ratio: float | None = Field(
        default=1e-05,
        le=1.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Applicable only if Control variable is MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001',
        },
    )
    maximum_setpoint_humidity_ratio: float | None = Field(
        default=1.0,
        le=1.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Applicable only if Control variable is MaximumHumidityRatio, MinimumHumidityRatio, or HumidityRatio - then minimum is 0.00001',
        },
    )
    reference_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The current setpoint at this node is the desired condition for the Mixed Air Node This node must have a valid setpoint which has been set by another setpoint manager'
        },
    )
    mixed_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Mixed Air Node'}
    )
    outdoor_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Outdoor Air Stream Node'}
    )
    return_air_stream_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of Return Air Stream Node'}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Node(s) at which the temperature or humidity ratio will be set'
        },
    )


class SetpointManagerOutdoorAirReset(IDFBaseModel):
    """This Setpoint Manager is used to place a setpoint temperature on system node
    according to the outdoor air temperature using a reset rule. The outdoor air
    temperature is obtained from the weather information during the simulation."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:OutdoorAirReset'
    name: str = Field(...)
    control_variable: (
        Literal['', 'MaximumTemperature', 'MinimumTemperature', 'Temperature'] | None
    ) = Field(default='Temperature')
    setpoint_at_outdoor_low_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    outdoor_low_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    setpoint_at_outdoor_high_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    outdoor_high_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which temperature will be set'}
    )
    schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Optional input. Schedule allows scheduling of the outdoor air reset rule - a schedule value of 1 means use the first rule; a value of 2 means use the second rule.',
        },
    )
    setpoint_at_outdoor_low_temperature_2: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': '2nd outdoor air temperature reset rule',
        },
    )
    outdoor_low_temperature_2: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': '2nd outdoor air temperature reset rule',
        },
    )
    setpoint_at_outdoor_high_temperature_2: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': '2nd outdoor air temperature reset rule',
        },
    )
    outdoor_high_temperature_2: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': '2nd outdoor air temperature reset rule',
        },
    )


class SetpointManagerReturnAirBypassFlow(IDFBaseModel):
    """This setpoint manager determines the required mass flow rate through a
    return air bypass duct to meet the specified temperature setpoint"""

    _idf_object_type: ClassVar[str] = 'SetpointManager:ReturnAirBypassFlow'
    name: str = Field(...)
    control_variable: Literal['', 'Flow'] | None = Field(default='Flow')
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object.',
        },
    )
    temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class SetpointManagerReturnTemperatureChilledWater(IDFBaseModel):
    """This setpoint manager is used to place a temperature setpoint on a plant
    supply outlet node based on a target return water setpoint. The setpoint
    manager attempts to achieve the desired return water temperature by
    adjusting the supply temperature setpoint based on the plant conditions at
    each system time step."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:ReturnTemperature:ChilledWater'
    name: str = Field(...)
    plant_loop_supply_outlet_node: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of the supply outlet node for the plant being controlled by this setpoint manager. Typically this is where the setpoint will be actuated for supply equipment to control to, but not...'
        },
    )
    plant_loop_supply_inlet_node: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of the supply inlet node for the plant being controlled with this setpoint manager. The temperature on this node is controlled by actuating the supply setpoint.'
        },
    )
    minimum_supply_temperature_setpoint: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the minimum chilled water supply temperature setpoint. This is also used as the default setpoint during no-load or negative-load conditions and during initialization.',
        },
    )
    maximum_supply_temperature_setpoint: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the maximum reset temperature for the chilled water supply.',
        },
    )
    return_temperature_setpoint_input_type: Literal[
        'Constant', 'ReturnTemperatureSetpoint', 'Scheduled'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'This defines whether the chilled water return temperature target is constant, scheduled, or specified on the supply inlet node by a separate setpoint manager.'
        },
    )
    return_temperature_setpoint_constant_value: float | None = Field(
        default=13.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the desired return temperature target, which is met by adjusting the supply temperature setpoint. This constant value is only used if the Design Chilled Water Return Temperature Input Type ...',
        },
    )
    return_temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This is the desired return temperature target, which is met by adjusting the supply temperature setpoint. This is a schedule name to allow the return temperature target value to be scheduled. This ...',
        },
    )


class SetpointManagerReturnTemperatureHotWater(IDFBaseModel):
    """This setpoint manager is used to place a temperature setpoint on a plant
    supply outlet node based on a target return water setpoint. The setpoint
    manager attempts to achieve the desired return water temperature by
    adjusting the supply temperature setpoint based on the plant conditions at
    each system time step."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:ReturnTemperature:HotWater'
    name: str = Field(...)
    plant_loop_supply_outlet_node: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of the supply outlet node for the plant being controlled by this setpoint manager. Typically this is where the setpoint will be actuated for supply equipment to control to, but not...'
        },
    )
    plant_loop_supply_inlet_node: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of the supply inlet node for the plant being controlled with this setpoint manager. The temperature on this node is controlled by actuating the supply setpoint.'
        },
    )
    minimum_supply_temperature_setpoint: float | None = Field(
        default=77.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the minimum reset temperature for the hot water supply.',
        },
    )
    maximum_supply_temperature_setpoint: float | None = Field(
        default=82.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the maximum hot water supply temperature setpoint. This is also used as the default setpoint during no-load or negative-load conditions and during initialization.',
        },
    )
    return_temperature_setpoint_input_type: Literal[
        'Constant', 'ReturnTemperatureSetpoint', 'Scheduled'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'This defines whether the hot water return temperature target is constant, scheduled, or specified on the supply inlet node by a separate setpoint manager.'
        },
    )
    return_temperature_setpoint_constant_value: float | None = Field(
        default=71.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the desired return temperature target, which is met by adjusting the supply temperature setpoint. This constant value is only used if the Design Hot Water Return Temperature Input Type is C...',
        },
    )
    return_temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This is the desired return temperature target, which is met by adjusting the supply temperature setpoint. This is a schedule name to allow the return temperature target value to be scheduled. This ...',
        },
    )


class SetpointManagerScheduled(IDFBaseModel):
    """The simplest Setpoint Manager simply uses a schedule to determine one or
    more setpoints. Values of the nodes are not used as input."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:Scheduled'
    name: str = Field(...)
    control_variable: Literal[
        'HumidityRatio',
        'MassFlowRate',
        'MaximumHumidityRatio',
        'MaximumMassFlowRate',
        'MaximumTemperature',
        'MinimumHumidityRatio',
        'MinimumMassFlowRate',
        'MinimumTemperature',
        'Temperature',
    ] = Field(...)
    schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which control variable will be set'}
    )


class SetpointManagerScheduledDualSetpoint(IDFBaseModel):
    """This setpoint manager places a high and low schedule value on one or more
    nodes."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:Scheduled:DualSetpoint'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    high_setpoint_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    low_setpoint_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which temperature will be set'}
    )


class SetpointManagerSingleZoneCooling(IDFBaseModel):
    """This setpoint manager detects the control zone load to meet the current
    cooling setpoint, zone inlet node flow rate, and zone node temperature, and
    calculates a setpoint temperature for the supply air that will satisfy the
    zone cooling load for the control zone."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:Cooling'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    minimum_supply_air_temperature: float | None = Field(
        default=-99.0, json_schema_extra={'units': 'C'}
    )
    maximum_supply_air_temperature: float | None = Field(
        default=99.0, json_schema_extra={'units': 'C'}
    )
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    zone_node_name: str = Field(...)
    zone_inlet_node_name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerSingleZoneHeating(IDFBaseModel):
    """This setpoint manager detects the control zone load to meet the current
    heating setpoint, zone inlet node flow rate, and zone node temperature, and
    calculates a setpoint temperature for the supply air that will satisfy the
    zone heating load for the control zone."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:Heating'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    minimum_supply_air_temperature: float | None = Field(
        default=-99.0, json_schema_extra={'units': 'C'}
    )
    maximum_supply_air_temperature: float | None = Field(
        default=99.0, json_schema_extra={'units': 'C'}
    )
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    zone_node_name: str = Field(...)
    zone_inlet_node_name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerSingleZoneHumidityMaximum(IDFBaseModel):
    """The Single Zone Maximum Humidity Setpoint Manager allows the control of a
    single zone maximum humidity level. This setpoint manager can be used in
    conjunction with object ZoneControl:Humidistat to detect humidity levels."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:Humidity:Maximum'
    name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Node(s) at which humidity ratio setpoint will be set'
        },
    )
    control_zone_air_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Name of the zone air node for the humidity control zone'
        },
    )


class SetpointManagerSingleZoneHumidityMinimum(IDFBaseModel):
    """The Single Zone Minimum Humidity Setpoint Manager allows the control of a
    single zone minimum humidity level. This setpoint manager can be used in
    conjunction with object ZoneControl:Humidistat to detect humidity levels."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:Humidity:Minimum'
    name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Node(s) at which humidity ratio setpoint will be set'
        },
    )
    control_zone_air_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Name of the zone air node for the humidity control zone'
        },
    )


class SetpointManagerSingleZoneOneStageCooling(IDFBaseModel):
    """This object can be used with CoilSystem:Cooling:DX to model on/off cycling
    control of single stage air systems. Setpoints are modulated to run coil
    full on or full off depending on zone conditions. Intended for use with
    ZoneControl:Thermostat:StagedDualSetpoint"""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:OneStageCooling'
    name: str = Field(...)
    cooling_stage_on_supply_air_setpoint_temperature: float | None = Field(
        default=-99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the setpoint value applied when cooling device is to cycle ON',
        },
    )
    cooling_stage_off_supply_air_setpoint_temperature: float | None = Field(
        default=99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the setpoint value applied when cooling device is to cycle OFF',
        },
    )
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerSingleZoneOneStageHeating(IDFBaseModel):
    """This object can be used with CoilSystem:Heating:DX, Coil:Heating:Fuel,
    Coil:Heating:Electric to model on/off cycling control of single stage air
    systems. Setpoints are modulated to run coil full on or full off depending
    on zone conditions. Intended for use with
    ZoneControl:Thermostat:StagedDualSetpoint."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:OneStageHeating'
    name: str = Field(...)
    heating_stage_on_supply_air_setpoint_temperature: float | None = Field(
        default=99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the setpoint value applied when heating device is to cycle ON',
        },
    )
    heating_stage_off_supply_air_setpoint_temperature: float | None = Field(
        default=-99.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the setpoint value applied when heating device is to cycle OFF',
        },
    )
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerSingleZoneReheat(IDFBaseModel):
    """This setpoint manager detects the control zone load, zone inlet node flow
    rate, and zone node temperature and calculates a setpoint temperature for
    the supply air that will satisfy the zone load (heating or cooling) for the
    control zone. This setpoint manager is not limited to reheat applications."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SingleZone:Reheat'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    minimum_supply_air_temperature: float | None = Field(
        default=-99.0, json_schema_extra={'units': 'C'}
    )
    maximum_supply_air_temperature: float | None = Field(
        default=99.0, json_schema_extra={'units': 'C'}
    )
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    zone_node_name: str = Field(...)
    zone_inlet_node_name: str = Field(...)
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerSystemNodeResetHumidity(IDFBaseModel):
    """This Setpoint Manager is used to place a humidity ratio setpoint on a system
    node according to the reference (e.g., return) humidity ratio using a reset
    rule. The humidity ratio setpoint is obtained by retrieving the humidity
    ratio of the user specified reference system node."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SystemNodeReset:Humidity'
    name: str = Field(...)
    control_variable: Literal[
        'HumidityRatio', 'MaximumHumidityRatio', 'MinimumHumidityRatio'
    ] = Field(...)
    setpoint_at_low_reference_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    setpoint_at_high_reference_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    low_reference_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    high_reference_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    reference_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of an HVAC system node that gets referenced.'
        },
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which humidity ratio will be set'}
    )


class SetpointManagerSystemNodeResetTemperature(IDFBaseModel):
    """This Setpoint Manager is used to place a temperature setpoint on a system
    node according to the reference (e.g., return) temperature using a reset
    rule. The temperature setpoint is obtained by retrieving the temperature of
    the user specified reference system node."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:SystemNodeReset:Temperature'
    name: str = Field(...)
    control_variable: Literal[
        'MaximumTemperature', 'MinimumTemperature', 'Temperature'
    ] = Field(...)
    setpoint_at_low_reference_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    setpoint_at_high_reference_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    low_reference_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    high_reference_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    reference_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of an HVAC system node that gets referenced.'
        },
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which temperature will be set'}
    )


class SetpointManagerWarmest(IDFBaseModel):
    """This SetpointManager resets the cooling supply air temperature of a central
    forced air HVAC system according to the cooling demand of the warmest zone."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:Warmest'
    name: str = Field(...)
    control_variable: Literal['', 'Temperature'] | None = Field(default='Temperature')
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object',
        },
    )
    minimum_setpoint_temperature: float | None = Field(
        default=12.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=18.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    strategy: Literal['', 'MaximumTemperature'] | None = Field(
        default='MaximumTemperature'
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )


class SetpointManagerWarmestTemperatureFlow(IDFBaseModel):
    """This setpoint manager sets both the supply air temperature and the supply
    air flow rate."""

    _idf_object_type: ClassVar[str] = 'SetpointManager:WarmestTemperatureFlow'
    name: str = Field(...)
    control_variable: Literal['Temperature'] | None = Field(default=None)
    hvac_air_loop_name: AirPrimaryLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirPrimaryLoops'],
            'note': 'Enter the name of an AirLoopHVAC object.',
        },
    )
    minimum_setpoint_temperature: float | None = Field(
        default=12.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    maximum_setpoint_temperature: float | None = Field(
        default=18.0, gt=0.0, json_schema_extra={'units': 'C'}
    )
    strategy: Literal['', 'FlowFirst', 'TemperatureFirst'] | None = Field(
        default='TemperatureFirst',
        json_schema_extra={
            'note': 'For TemperatureFirst the manager tries to find the highest setpoint temperature that will satisfy all the zone cooling loads at minimum supply air flow rate. If this setpoint temperature is less th...'
        },
    )
    setpoint_node_or_nodelist_name: str = Field(
        ..., json_schema_extra={'note': 'Node(s) at which the temperature will be set'}
    )
    minimum_turndown_ratio: float | None = Field(
        default=0.2,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Fraction of the maximum supply air flow rate. Used to define the minimum supply flow for the TemperatureFirst strategy.',
        },
    )
