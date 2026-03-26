"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Internal Gains
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllHeatTranAngFacNamesRef,
    AllHeatTranSurfNamesRef,
    BivariateFunctionsRef,
    FloorSurfaceNamesRef,
    RoomAirNodesRef,
    ScheduleNamesRef,
    SpaceAndSpaceListNamesRef,
    SpaceNamesRef,
    SurfaceNamesRef,
    SurfAndSubSurfNamesRef,
    UnivariateFunctionsRef,
    ZoneAndZoneListNamesRef,
    ZoneNamesRef,
)


class ComfortViewFactorAnglesAnglesItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor: float | None = Field(default=None, ge=0.0, le=1.0)


class ComfortViewFactorAngles(IDFBaseModel):
    """Used to specify radiant view factors for thermal comfort calculations. Note
    that the following angle factor fractions must sum up to 1.0 All surfaces
    must be in the same enclosure."""

    _idf_object_type: ClassVar[str] = 'ComfortViewFactorAngles'
    name: str | None = Field(default=None)
    angles: list[ComfortViewFactorAnglesAnglesItem] | None = Field(default=None)


class ElectricEquipment(IDFBaseModel):
    """Sets internal gains for electric equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ElectricEquipment'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to design level of electric equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal['', 'EquipmentLevel', 'Watts/Area', 'Watts/Person'] | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of electric equipment for this set of attributes Choices: EquipmentLevel => Equipment Level -- simply enter watts of equipment Wa...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    watts_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class ElectricEquipmentITEAirCooled(IDFBaseModel):
    """This object describes air-cooled electric information technology equipment
    (ITE) which has variable power consumption as a function of loading and
    temperature. If a Zone comprised of more than one Space is specified then
    this definition applies to all applicable spaces, and each instance will be
    named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ElectricEquipment:ITE:AirCooled'
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceNames', 'ZoneNames'],
            'note': 'ZoneList and SpaceList names are not allowed.',
        },
    )
    air_flow_calculation_method: (
        Literal['', 'FlowControlWithApproachTemperatures', 'FlowFromSystem'] | None
    ) = Field(
        default='FlowFromSystem',
        json_schema_extra={
            'note': 'The specified method is used to calculate the IT inlet temperature and zone return air temperature. If FlowFromSystem is chosen, the zone is assumed to be well-mixed. If FlowControlWithApproachTemp...'
        },
    )
    design_power_input_calculation_method: (
        Literal['', 'Watts/Area', 'Watts/Unit'] | None
    ) = Field(
        default='Watts/Unit',
        json_schema_extra={
            'note': 'The entered calculation method is used to specify the design power input Watts/Unit => Watts per Unit -- Design Power = Watts per Unit * Number of Units Watts/Area => Watts per Floor Area -- Design...'
        },
    )
    watts_per_unit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    number_of_units: float | None = Field(default=1.0, ge=0.0)
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    design_power_input_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Operating schedule for this equipment, fraction applied to the design power input, generally (0.0 - 1.0) If this field is blank, the schedule is assumed to always be 1.0.',
        },
    )
    cpu_loading_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'CPU loading schedule for this equipment as a fraction from 0.0 (idle) to 1.0 (full load). If this field is blank, the schedule is assumed to always be 1.0.',
        },
    )
    cpu_power_input_function_of_loading_and_air_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the CPU power input as a function of CPU loading (x) and air inlet node temperature (y). This curve (table) should equal 1.0 a...',
        },
    )
    design_fan_power_input_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'The fraction of the total power input at design conditions which is for the cooling fan(s)'
        },
    )
    design_fan_air_flow_rate_per_power_input: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'The cooling fan air flow rate per total electric power input at design conditions',
        },
    )
    air_flow_function_of_loading_and_air_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the cooling air flow rate as a function of CPU loading (x) and air inlet node temperature (y). This curve (table) should equal...',
        },
    )
    fan_power_input_function_of_flow_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'The name of a single-variable curve or table lookup object which modifies the cooling fan power as a function of flow fraction (x). This curve (table) should equal 1.0 at a flow fraction of 1.0.',
        },
    )
    design_entering_air_temperature: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The entering air temperature at design conditions.',
        },
    )
    environmental_class: (
        Literal['', 'A1', 'A2', 'A3', 'A4', 'B', 'C', 'H1', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Specifies the allowable operating conditions for the air inlet conditions. Used for reporting time outside allowable conditions.'
        },
    )
    air_inlet_connection_type: (
        Literal['', 'AdjustedSupply', 'RoomAirModel', 'ZoneAirNode'] | None
    ) = Field(
        default='AdjustedSupply',
        json_schema_extra={
            'note': 'Specifies the type of connection between the zone and the ITE air inlet node. AdjustedSupply = ITE inlet temperature will be the current Supply Air Node temperature adjusted by the current recircul...'
        },
    )
    air_inlet_room_air_model_node_name: RoomAirNodesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RoomAirNodes'],
            'note': 'Name of a RoomAir:Node object which is connected to the ITE air inlet.',
        },
    )
    air_outlet_room_air_model_node_name: RoomAirNodesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RoomAirNodes'],
            'note': 'Name of a RoomAir:Node object which is connected to the ITE air outlet.',
        },
    )
    supply_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the supply air inlet node serving this ITE. Required if the Air Node Connection Type = AdjustedSupply. Also required if Calculation Method = FlowControlWithApproachTemperatures. Also requir...'
        },
    )
    design_recirculation_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=0.5,
        json_schema_extra={
            'note': 'The recirculation fraction for this equipment at design conditions. This field is used only if the Air Node Connection Type = AdjustedSupply. The default is 0.0 (no recirculation). This field is on...'
        },
    )
    recirculation_function_of_loading_and_supply_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the recirculation fraction as a function of CPU loading (x) and supply air node temperature (y). This curve (table) should equ...',
        },
    )
    design_electric_power_supply_efficiency: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'The efficiency of the power supply system serving this ITE'
        },
    )
    electric_power_supply_efficiency_function_of_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'The name of a single-variable curve or table lookup object which modifies the electric power supply efficiency as a function of part-load ratio (x). This curve (table) should equal 1.0 at full load...',
        },
    )
    fraction_of_electric_power_supply_losses_to_zone: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Fraction of the electric power supply losses which are a heat gain to the zone If this field is <1.0, the remainder of the losses are assumed to be lost to the outdoors.'
        },
    )
    cpu_end_use_subcategory: str | None = Field(
        default='ITE-CPU',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    fan_end_use_subcategory: str | None = Field(
        default='ITE-Fans',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    electric_power_supply_end_use_subcategory: str | None = Field(
        default='ITE-UPS',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    supply_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The difference of the IT inlet temperature from the AHU supply air temperature. Either Supply Temperature Difference or Supply Temperature Difference Schedule is required if Air Flow Calculation Me...',
        },
    )
    supply_temperature_difference_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The difference schedule of the IT inlet temperature from the AHU supply air temperature. Either Supply Temperature Difference or Supply Temperature Difference Schedule is required if Air Flow Calcu...',
        },
    )
    return_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The difference of the the actual AHU return air temperature to the IT equipment outlet temperature. Either Return Temperature Difference or Return Temperature Difference Schedule is required if Air...',
        },
    )
    return_temperature_difference_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The difference schedule of the actual AHU return air temperature to the IT equipment outlet temperature. Either Return Temperature Difference or Return Temperature Difference Schedule is required i...',
        },
    )


class GasEquipment(IDFBaseModel):
    """Sets internal gains and contaminant rates for gas equipment in the zone. If
    a ZoneList, SpaceList, or a Zone comprised of more than one Space is
    specified then this definition applies to all applicable spaces, and each
    instance will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'GasEquipment'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of gas equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of gas equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipment Watt...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    carbon_dioxide_generation_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=4e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of power input The default value assumes the equipment is fully vented. For unvented equipment, a suggested value is 3.45E-8 m3/s-W. This value is converted from a natu...',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class HotWaterEquipment(IDFBaseModel):
    """Sets internal gains for hot water equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'HotWaterEquipment'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of hot water equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of hot water equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipmen...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class IndoorLivingWall(IDFBaseModel):
    """Indoor greenery systems such as indoor living walls are panels of plants,
    which grow hydroponically or from substrates. The living wall structures can
    be either free-standing or attached to walls. The IndoorLivingWall module
    directly connects with inside surface heat balance, zone air heat balance,
    and zone air moisture balance."""

    _idf_object_type: ClassVar[str] = 'IndoorLivingWall'
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SurfaceNames'],
            'note': 'Name of the wall partition where indoor green is located.',
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)',
        },
    )
    evapotranspiration_calculation_method: (
        Literal['', 'Penman-Monteith', 'Stanghellini'] | None
    ) = Field(
        default='Penman-Monteith',
        json_schema_extra={
            'note': 'Model selection for calculating evapotranspiration of indoor greenery system. This rate can also be actuated with user-defined calculations, see EMS application guide for actuator details.'
        },
    )
    lighting_method: Literal['Daylight', 'LED', 'LED-Daylight'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Three different methods are provided here (LED; Daylight; LED-Daylight)'
        },
    )
    led_intensity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    daylighting_control_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If daylighting is used in the selected lighting methods (Daylight or LED-Daylight), users should define an object of Daylighting:Control to obtain the daylighting illuminance level and an object fo...'
        },
    )
    led_daylight_targeted_lighting_intensity_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'This field defines targeted LED intensity level for indoor living wall systems. The schedule values can be any positive number representing targeted photosynthetic photon flux density (PPFD). Based...',
            },
        )
    )
    total_leaf_area: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm2',
            'note': 'The value is the one-sided leaf area of an indoor living wall. Based on the users’ input, LAI is calculated as the ratio of the total leaf area and the partition wall area. Typical LAIs are 1.0 for...',
        },
    )
    led_nominal_intensity: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'umol/m2-s',
            'note': 'The value represents photosynthetic photon flux density (PPFD) of LED grow light. PPFD is measured in micro-mole per m2 per second (umol/m2-s) which establishes exactly how many photosynthetically ...',
        },
    )
    led_nominal_power: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field defines nominal total LED power for an indoor living wall system.',
        },
    )
    radiant_fraction_of_led_lights: float | None = Field(
        default=0.6,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This field defines the fraction of radiation from LED lights'
        },
    )


class Lights(IDFBaseModel):
    """Sets internal gains for lights in the zone. If a ZoneList, SpaceList, or a
    Zone comprised of more than one Space is specified then this definition
    applies to all applicable spaces, and each instance will be named with the
    Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'Lights'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to design level of lights, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal['', 'LightingLevel', 'Watts/Area', 'Watts/Person'] | None
    ) = Field(
        default='LightingLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of lights for this set of attributes Choices: LightingLevel => Lighting Level -- simply enter watts of lights Watts/Area => Watts...'
        },
    )
    lighting_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    watts_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    return_air_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Used only for sizing calculation if return-air-fraction coefficients are specified.'
        },
    )
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_visible: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_replaceable: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'For Daylighting:Controls must be 0 or 1:  0 = no dimming control, 1 = full dimming control'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    return_air_fraction_calculated_from_plenum_temperature: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    return_air_fraction_function_of_plenum_temperature_coefficient_1: float | None = (
        Field(
            default=0.0,
            ge=0.0,
            json_schema_extra={
                'note': 'Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)'
            },
        )
    )
    return_air_fraction_function_of_plenum_temperature_coefficient_2: float | None = (
        Field(
            default=0.0,
            ge=0.0,
            json_schema_extra={
                'units': '1/K',
                'note': 'Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)',
            },
        )
    )
    return_air_heat_gain_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the return air node for this heat gain. If left blank, defaults to the first return air node for the zone. Leave this field blank when using a ZoneList name.'
        },
    )
    exhaust_air_heat_gain_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the exhaust air node for this heat gain. If the node name is entered, return heat gain will be shared by both return and exhaust air nodes. The air properties of both nodes are weighted by ...'
        },
    )


class OtherEquipment(IDFBaseModel):
    """Sets internal gains or losses for \"other\" equipment in the zone. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'OtherEquipment'
    name: str = Field(...)
    fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'None',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='None')
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of other equipment. to set a loss, use a negative value in the following fields. for this set of attributes Choices: EquipmentLev...'
        },
    )
    design_level: float | None = Field(default=None, json_schema_extra={'units': 'W'})
    power_per_floor_area: float | None = Field(
        default=None, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    carbon_dioxide_generation_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=4e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of power input The default value assumes the equipment is fully vented.',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class People(IDFBaseModel):
    """Sets internal gains and contaminant rates for occupants in the zone. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'People'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    number_of_people_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to number of people (0.0 - 1.0)',
        },
    )
    number_of_people_calculation_method: (
        Literal['', 'Area/Person', 'People', 'People/Area'] | None
    ) = Field(
        default='People',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum number of people for this set of attributes (i.e. sensible fraction, schedule, etc) Choices: People -- simply enter number of occupants....'
        },
    )
    number_of_people: float | None = Field(default=None, ge=0.0)
    people_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'person/m2'}
    )
    floor_area_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm2/person'}
    )
    fraction_radiant: float | None = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This is radiant fraction of the sensible heat released by people in a zone. This value will be multiplied by the total sensible heat released by people yields the amount of long wavelength radiatio...'
        },
    )
    sensible_heat_fraction: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'if input, overrides program calculated sensible/latent split'
        },
    )
    activity_level_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Note that W has to be converted to mets in TC routine units in schedule are W/person',
        },
    )
    carbon_dioxide_generation_rate: float | None = Field(
        default=3.82e-08,
        ge=0.0,
        le=3.82e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of activity level. The default value is obtained from ASHRAE Std 62.1 at 0.0084 cfm/met/person over the general adult population.',
        },
    )
    enable_ashrae_55_comfort_warnings: Literal['', 'No', 'Yes'] | None = Field(
        default='No'
    )
    mean_radiant_temperature_calculation_type: (
        Literal['', 'AngleFactor', 'EnclosureAveraged', 'SurfaceWeighted'] | None
    ) = Field(
        default='EnclosureAveraged',
        json_schema_extra={'note': 'optional (only required for thermal comfort runs)'},
    )
    surface_name_angle_factor_list_name: AllHeatTranAngFacNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AllHeatTranAngFacNames'],
            'note': 'optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    work_efficiency_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule are 0.0 to 1.0 optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    clothing_insulation_calculation_method: (
        Literal[
            '',
            'CalculationMethodSchedule',
            'ClothingInsulationSchedule',
            'DynamicClothingModelASHRAE55',
        ]
        | None
    ) = Field(default='ClothingInsulationSchedule')
    clothing_insulation_calculation_method_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'a schedule value of 1 for the Scheduled method, and 2 for the DynamicClothingModelASHRAE55 method',
            },
        )
    )
    clothing_insulation_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'use "Clo" from ASHRAE or Thermal Comfort guides optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    air_velocity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in the schedule are m/s optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    thermal_comfort_model_1_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (only needed for people thermal comfort results reporting)'
        },
    )
    thermal_comfort_model_2_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (second type of thermal comfort model and results reporting)'
        },
    )
    thermal_comfort_model_3_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (third thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_4_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (fourth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_5_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (fifth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_6_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (sixth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_7_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (seventh thermal comfort model and report type)'
        },
    )
    ankle_level_air_velocity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in the schedule are m/s this is the schedule of the air speed at the 0.1 m above the floor optional (only required for runs of thermal comfort models AnkleDraftASH55)',
        },
    )
    cold_stress_temperature_threshold: float | None = Field(
        default=15.56,
        json_schema_extra={
            'units': 'C',
            'note': 'this is the indoor safe temperature threshold for cold stress',
        },
    )
    heat_stress_temperature_threshold: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'C',
            'note': 'this is the indoor safe temperature threshold for heat stress',
        },
    )


class SteamEquipment(IDFBaseModel):
    """Sets internal gains for steam equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'SteamEquipment'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of steam equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of steam equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipment Wa...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion'
    )
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    mass_transfer_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )
    henry_adsorption_constant_or_partition_coefficient: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )


class SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink'
    )
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    deposition_velocity: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )


class SurfaceContaminantSourceAndSinkGenericPressureDriven(IDFBaseModel):
    """Simulate generic contaminant source driven by the pressure difference across
    a surface."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:PressureDriven'
    )
    name: str = Field(...)
    surface_name: SurfAndSubSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfAndSubSurfNames']}
    )
    design_generation_rate_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    generation_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate Coefficient',
        },
    )
    generation_exponent: float | None = Field(
        default=None, le=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )


class SwimmingPoolIndoor(IDFBaseModel):
    """Specifies an indoor swimming pools linked to a floor surface. The pool is
    assumed to cover the entire floor to which it is linked."""

    _idf_object_type: ClassVar[str] = 'SwimmingPool:Indoor'
    name: str = Field(...)
    surface_name: FloorSurfaceNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FloorSurfaceNames'],
            'note': 'Name of the floor surface where the pool is located.',
        },
    )
    average_depth: float = Field(..., json_schema_extra={'units': 'm'})
    activity_factor_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    make_up_water_supply_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cover_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cover_evaporation_factor: float | None = Field(default=0.0, ge=0.0, le=1.0)
    cover_convection_factor: float | None = Field(default=0.0, ge=0.0, le=1.0)
    cover_short_wavelength_radiation_factor: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    cover_long_wavelength_radiation_factor: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    pool_water_inlet_node: str = Field(...)
    pool_water_outlet_node: str = Field(...)
    pool_heating_system_maximum_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    pool_miscellaneous_equipment_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Power input per pool water flow rate',
        },
    )
    setpoint_temperature_schedule: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    maximum_number_of_people: float = Field(..., ge=0.0)
    people_schedule: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    people_heat_gain_schedule: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class ZoneBaseboardOutdoorTemperatureControlled(IDFBaseModel):
    """Specifies outside temperature-controlled electric baseboard heating. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ZoneBaseboard:OutdoorTemperatureControlled'
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to capacity of the baseboard heat equipment, generally (0.0 - 1.0)',
        },
    )
    capacity_at_low_temperature: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W'}
    )
    low_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    capacity_at_high_temperature: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    high_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class ZoneContaminantSourceAndSinkCarbonDioxide(IDFBaseModel):
    """Represents internal CO2 gains and sinks in the zone."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:CarbonDioxide'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Positive values represent sources and negative values represent sinks.',
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate',
        },
    )


class ZoneContaminantSourceAndSinkGenericConstant(IDFBaseModel):
    """Sets internal generic contaminant gains and sinks in a zone with constant
    values."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:Constant'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'The values represent source.'},
    )
    generation_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate',
        },
    )
    design_removal_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'The value represent sink.'},
    )
    removal_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design removal Coefficient',
        },
    )


class ZoneContaminantSourceAndSinkGenericCutoffModel(IDFBaseModel):
    """Simulate generic contaminant source driven by the cutoff concentration
    model."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:CutoffModel'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate Coefficient',
        },
    )
    cutoff_generic_contaminant_at_which_emission_ceases: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'ppm',
            'note': 'When the zone concentration level is greater than the cutoff level, emission stops, and the source level is zero.',
        },
    )


class ZoneContaminantSourceAndSinkGenericDecaySource(IDFBaseModel):
    """Simulate generic contaminant source driven by the cutoff concentration
    model."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:DecaySource'
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    initial_emission_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )
    delay_time_constant: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 's'}
    )


class ZoneContaminantSourceAndSinkGenericDepositionRateSink(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'ZoneContaminantSourceAndSink:Generic:DepositionRateSink'
    )
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    deposition_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )
