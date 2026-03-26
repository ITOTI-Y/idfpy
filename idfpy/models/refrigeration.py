"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Refrigeration
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    FluidAndGlycolNamesRef,
    FluidNamesRef,
    RefrigerationAirChillerNamesRef,
    RefrigerationAllTypesCondenserNamesRef,
    RefrigerationAllTypesGasCoolerNamesRef,
    RefrigerationCascadeCondenserAndSecondarySystemNamesRef,
    RefrigerationCaseAndWalkInAndListNamesRef,
    RefrigerationCaseAndWalkInNamesRef,
    RefrigerationCompressorAndListNamesRef,
    RefrigerationCompressorNamesRef,
    RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNamesRef,
    RefrigerationSubcoolerNamesRef,
    RefrigerationSystemNamesRef,
    ScheduleNamesRef,
    TrivariateFunctionsRef,
    UnivariateFunctionsRef,
    WaterStorageTankNamesRef,
    ZoneNamesRef,
)


class RefrigerationCaseAndWalkInListCasesAndWalkinsItem(IDFBaseModel):
    """Nested object type for array items."""

    case_or_walkin_name: RefrigerationCaseAndWalkInNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object.',
        },
    )


class RefrigerationCompressorListCompressorsItem(IDFBaseModel):
    """Nested object type for array items."""

    refrigeration_compressor_name: RefrigerationCompressorNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['RefrigerationCompressorNames'],
            'note': 'Enter the name of a Refrigeration:Compressor object.',
        },
    )


class RefrigerationTransferLoadListTransferLoadsItem(IDFBaseModel):
    """Nested object type for array items."""

    cascade_condenser_name_or_secondary_system_name: RefrigerationCascadeCondenserAndSecondarySystemNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['RefrigerationCascadeCondenserAndSecondarySystemNames'],
            'note': 'Enter the name of a Refrigeration:Condenser:Cascade object OR the name of a Refrigeration:SecondarySystem object.',
        },
    )


class RefrigerationWalkInZoneDataItem(IDFBaseModel):
    """Nested object type for array items."""

    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object. The walk-in cooler can face multiple zones. The heat exchange with each zone must be input separately',
        },
    )
    total_insulated_surface_area_facing_zone: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm2',
            'note': 'Area should include walls and ceilings, but not doors',
        },
    )
    insulated_surface_u_value_facing_zone: float | None = Field(
        default=0.3154,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'The default value corresponds to R18 [ft2-F-hr/Btu] To convert other IP R-values to U, divide 5.678 by the R-value Some examples: R15 is U 0.3785 W/m2-K R5 is U 1.136 W/m2-K',
        },
    )
    area_of_glass_reach_in_doors_facing_zone: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm2'}
    )
    height_of_glass_reach_in_doors_facing_zone: float | None = Field(
        default=1.5, json_schema_extra={'units': 'm'}
    )
    glass_reach_in_door_u_value_facing_zone: float | None = Field(
        default=1.136,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'The default value corresponds to R5 [ft2-F-hr/Btu] To convert other IP R-values to U, divide 5.678 by the R-value',
        },
    )
    glass_reach_in_door_opening_schedule_name_facing_zone: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Schedule values should all be between 0.0 and 1.0. For example, if the door is open 30% of the time during working hours, then the schedule would hold the value 0.3 during working hours and 0 durin...',
            },
        )
    )
    area_of_stocking_doors_facing_zone: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm2'}
    )
    height_of_stocking_doors_facing_zone: float | None = Field(
        default=3.0, json_schema_extra={'units': 'm'}
    )
    stocking_door_u_value_facing_zone: float | None = Field(
        default=0.3785,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'The default value corresponds to R15 [ft2-F-hr/Btu] To convert other IP R-values to U, divide 5.678 by the R-value Some examples: R5 is U 1.136 W/m2-K R18 is U 0.3154 W/m2-K',
        },
    )
    stocking_door_opening_schedule_name_facing_zone: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should all be between 0.0 and 1.0. For example, if the door is open 30% of the time during working hours, then the schedule would hold the value 0.3 during working hours and 0 durin...',
        },
    )
    stocking_door_opening_protection_type_facing_zone: (
        Literal['', 'AirCurtain', 'None', 'StripCurtain'] | None
    ) = Field(
        default='AirCurtain',
        json_schema_extra={
            'note': 'Use StripCurtain for hanging strips or airlock vestibules'
        },
    )


class ZoneHVACRefrigerationChillerSetChillersItem(IDFBaseModel):
    """Nested object type for array items."""

    air_chiller_name: RefrigerationAirChillerNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationAirChillerNames'],
            'note': 'This is the first chiller turned on to meet the zone load',
        },
    )


class RefrigerationAirChiller(IDFBaseModel):
    """Works in conjunction with a refrigeration chiller set, compressor rack, a
    refrigeration system, or a refrigeration secondary system to simulate the
    performance of an air chiller, similar to one found in a refrigerated
    warehouse. Energy use for fans and heaters is modeled based on inputs for
    nominal power, schedules, and control type. The air chiller model accounts
    for the sensible and latent heat exchange with the surrounding environment."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:AirChiller'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    capacity_rating_type: Literal[
        'CapacityTotalSpecificConditions',
        'EuropeanSC1NominalWet',
        'EuropeanSC1Standard',
        'EuropeanSC2NominalWet',
        'EuropeanSC2Standard',
        'EuropeanSC3NominalWet',
        'EuropeanSC3Standard',
        'EuropeanSC4NominalWet',
        'EuropeanSC4Standard',
        'EuropeanSC5NominalWet',
        'EuropeanSC5Standard',
        'FixedLinear',
        'UnitLoadFactorSensibleOnly',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'In each case, select the rating option that corresponds to the expected service conditions. For example, U.S. manufacturers quote a separate Unit Load Factor for wet or frosted coils. If the evapor...'
        },
    )
    rated_unit_load_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/K',
            'note': 'The sensible cooling capacity in watts (W/C) at rated conditions. The value entered for this field must be greater than zero, with no default value. This value is only used if the Capacity Rating T...',
        },
    )
    rated_capacity: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This value is only used if the Capacity Rating Type is NOT UnitLoadFactorSensibleOnly. For CapacityTotalSpecificConditions, this capacity includes both sensible and latent at the conditions given i...',
        },
    )
    rated_relative_humidity: float | None = Field(
        default=85.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'This field is ONLY used if the Capacity Rating Type is CapacityTotalSpecificConditions and represents the relative humidity at rated conditions. The default is 85.',
        },
    )
    rated_cooling_source_temperature: float = Field(
        ...,
        ge=-70.0,
        le=40.0,
        json_schema_extra={
            'units': 'C',
            'note': 'If DXEvaporator, use evaporating temperature (saturated suction temperature) If BrineCoil, use Brine entering temperature used to set minimum suction pressure for DX systems and minimum brine temp ...',
        },
    )
    rated_temperature_difference_dt1: float = Field(
        ...,
        ge=0.0,
        le=20.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The rated difference between the air entering the refrigeration chiller and the cooling source temperature in degC.',
        },
    )
    maximum_temperature_difference_between_inlet_air_and_evaporating_temperature: (
        float | None
    ) = Field(
        default=None,
        ge=0.0,
        le=25.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The maximum difference between the air entering the refrigeration chiller and the cooling source temperature in degC used to limit capacity during pull-down. defaults to 1.3 times the Rated Tempera...',
        },
    )
    coil_material_correction_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "This is the manufacturer's correction factor for coil material corresponding to rating",
        },
    )
    refrigerant_correction_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "This is the manufacturer's correction factor for refrigerant corresponding to rating",
        },
    )
    capacity_correction_curve_type: (
        Literal['European', 'LinearSHR60', 'QuadraticSHR', 'TabularRHxDT1xTRoom'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'In each case, select the correction curve type that corresponds to the rating type. default LinearSHR60 unless Capacity Rating Type = CapacityTotalSpecificConditions'
        },
    )
    capacity_correction_curve_name: (
        TrivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions', 'UnivariateFunctions'],
            'note': 'Should be blank for LinearSHR60 correction curve type',
        },
    )
    shr60_correction_factor: float | None = Field(
        default=1.48,
        le=1.67,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'only used when the capacity correction curve type is LinearSHR60',
        },
    )
    rated_total_heating_power: float = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Include total for all heater power Do not include defrost heater power',
        },
    )
    heating_power_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values will be used to multiply the total heating power Values in the schedule should be between 0.0 and 1.0 Defaults to always on if schedule name left blank.',
        },
    )
    fan_speed_control_type: (
        Literal['', 'Fixed', 'FixedLinear', 'TwoSpeed', 'VariableSpeed'] | None
    ) = Field(default='Fixed')
    rated_fan_power: float | None = Field(
        default=375.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    rated_air_flow: float = Field(..., json_schema_extra={'units': 'm3/s'})
    minimum_fan_air_flow_ratio: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Minimum air flow fraction through fan',
        },
    )
    defrost_type: Literal['', 'Electric', 'HotFluid', 'None', 'OffCycle'] | None = (
        Field(
            default='Electric',
            json_schema_extra={
                'note': 'HotFluid includes either hot gas defrost for a DX system or Hot Brine defrost if this walk in is cooled by brine from a secondary chiller'
            },
        )
    )
    defrost_control_type: (
        Literal['', 'TemperatureTermination', 'TimeSchedule'] | None
    ) = Field(default='TimeSchedule')
    defrost_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule values should be 0 (off) or 1 (on)',
        },
    )
    defrost_drip_down_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule values should be 0 (off) or 1 (on) The start time for each defrost period in this drip-down schedule should coincide with the start time for each defrost period in the defrost schedule...',
        },
    )
    defrost_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'needed for all defrost types except none and offcycle',
        },
    )
    temperature_termination_defrost_fraction_to_ice: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This is the portion of the defrost energy that is available to melt frost Needed only for defrost control type TemperatureTermination defaults to 0.7 for electric defrost and to 0.3 for hot fluid d...',
        },
    )
    vertical_location: Literal['', 'Ceiling', 'Floor', 'Middle'] | None = Field(
        default='Middle'
    )
    average_refrigerant_charge_inventory: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'kg',
            'note': 'This value is only used if the Cooling Source Type is DXEvaporator',
        },
    )


class RefrigerationCase(IDFBaseModel):
    """The Refrigeration Case object works in conjunction with a compressor rack, a
    refrigeration system, or a secondary loop to simulate the performance of a
    refrigerated case system. The object calculates the energy use for lights,
    fans and anti-sweat heaters and accounts for the sensible and latent heat
    exchange with the surrounding environment (termed \"case credits\") which
    impacts the temperature and humidity in the zone where the case is located."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Case'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.',
        },
    )
    rated_ambient_temperature: float | None = Field(
        default=23.9, gt=0.0, json_schema_extra={'units': 'C'}
    )
    rated_ambient_relative_humidity: float | None = Field(
        default=55.0, gt=0.0, lt=100.0, json_schema_extra={'units': 'percent'}
    )
    rated_total_cooling_capacity_per_unit_length: float | None = Field(
        default=1900.0, gt=0.0, json_schema_extra={'units': 'W/m'}
    )
    rated_latent_heat_ratio: float | None = Field(default=0.3, ge=0.0, le=1.0)
    rated_runtime_fraction: float | None = Field(default=0.85, le=1.0, gt=0.0)
    case_length: float | None = Field(
        default=3.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    case_operating_temperature: float | None = Field(
        default=1.1, lt=20.0, json_schema_extra={'units': 'C'}
    )
    latent_case_credit_curve_type: (
        Literal['', 'CaseTemperatureMethod', 'DewpointMethod', 'RelativeHumidityMethod']
        | None
    ) = Field(default='CaseTemperatureMethod')
    latent_case_credit_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    standard_case_fan_power_per_unit_length: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'W/m'}
    )
    operating_case_fan_power_per_unit_length: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'W/m'}
    )
    standard_case_lighting_power_per_unit_length: float | None = Field(
        default=90.0, json_schema_extra={'units': 'W/m'}
    )
    installed_case_lighting_power_per_unit_length: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/m',
            'note': 'default set equal to Standard Case Lighting Power per Unit Length',
        },
    )
    case_lighting_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    fraction_of_lighting_energy_to_case: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    case_anti_sweat_heater_power_per_unit_length: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W/m'}
    )
    minimum_anti_sweat_heater_power_per_unit_length: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m',
            'note': 'This field is only applicable to the Linear, Dewpoint Method, and Heat Balance Method anti-sweat heater control types',
        },
    )
    anti_sweat_heater_control_type: (
        Literal['', 'Constant', 'DewpointMethod', 'HeatBalanceMethod', 'Linear', 'None']
        | None
    ) = Field(default='None')
    humidity_at_zero_anti_sweat_heater_energy: float | None = Field(
        default=-10.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'This field is only applicable to Linear AS heater control type Zone relative humidity (%) where anti-sweat heater energy is zero',
        },
    )
    case_height: float | None = Field(
        default=1.5,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field only applicable to Heat Balance Method AS heater control type Height must be greater than zero if Heat Balance Method AS heater control is selected',
        },
    )
    fraction_of_anti_sweat_heater_energy_to_case: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    case_defrost_power_per_unit_length: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m',
            'note': 'Used to evaluate load on case as well as power or heat consumption',
        },
    )
    case_defrost_type: (
        Literal[
            '',
            'Electric',
            'ElectricWithTemperatureTermination',
            'HotFluid',
            'HotFluidWithTemperatureTermination',
            'HotGas',
            'HotGasWithTemperatureTermination',
            'None',
            'OffCycle',
        ]
        | None
    ) = Field(default='OffCycle')
    case_defrost_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'A case defrost schedule name is required unless case defrost type = None',
        },
    )
    case_defrost_drip_down_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If left blank, the defrost schedule will be used The start time for each defrost period in this drip-down schedule should coincide with the start time for each defrost period in the case defrost sc...',
        },
    )
    defrost_energy_correction_curve_type: (
        Literal[
            '',
            'CaseTemperatureMethod',
            'DewpointMethod',
            'None',
            'RelativeHumidityMethod',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Case Temperature, Relative Humidity, and Dewpoint Method are applicable to case defrost types with temperature termination only.'
        },
    )
    defrost_energy_correction_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Defrost Energy Correction Curve Name is applicable to case defrost types with temperature termination only.',
        },
    )
    under_case_hvac_return_air_fraction: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    refrigerated_case_restocking_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be in units of Watts per unit case length (W/m) Leave this field blank if no restocking is to be modeled',
        },
    )
    case_credit_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be from 0 to 1 Leave this field blank if no case credit fraction is to be applied',
        },
    )
    design_evaporator_temperature_or_brine_inlet_temperature: float | None = Field(
        default=None,
        ge=-70.0,
        le=40.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Required for detailed refrigeration system, not for compressor rack For a DX system, enter the saturated temperature for refrigerant pressure leaving case For a brine-cooled cooled (secondary syste...',
        },
    )
    average_refrigerant_charge_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg/m'}
    )
    under_case_hvac_return_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the return air node for this case. If left blank, defaults to the first return air node for this zone.'
        },
    )


class RefrigerationCaseAndWalkInList(IDFBaseModel):
    """Provides a list of all the refrigerated cases, walk in coolers, or air
    chillers cooled by a single refrigeration system. Note that the names of all
    cases, walk-ins ,air chillers, and CaseAndWalkInLists must be unique. That
    is, you cannot give a list the same name as one of list items. This list may
    contain a combination of case and walk-in names OR a list of air chiller
    names. Air chillers may not be included in any list that also includes cases
    or walk-ins."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:CaseAndWalkInList'
    name: str = Field(...)
    cases_and_walkins: (
        list[RefrigerationCaseAndWalkInListCasesAndWalkinsItem] | None
    ) = Field(default=None)


class RefrigerationCompressor(IDFBaseModel):
    """Refrigeration system compressor. Data is available for many compressors in
    the RefrigerationCompressor.idf dataset"""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Compressor'
    name: str = Field(...)
    refrigeration_compressor_power_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'the input order for the Curve:Bicubic does not match the ARI 540-2004 Eq. 1 coefficient order N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3, N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is...',
        },
    )
    refrigeration_compressor_capacity_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'the input order for the Curve:Bicubic does not match the ARI 540-2004 Eq. 1 coefficient order N1 is ARI_C1, N2 is ARI_C2, N3 is ARI_C4, N4 is ARI_C3, N5 is ARI_C6, N6 is ARI_C5, N7 is ARI_C7, N8 is...',
        },
    )
    rated_superheat: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Use this input field OR the next, not both This is used if the compressor rating is based upon degrees of superheat',
        },
    )
    rated_return_gas_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Use this input field OR the previous, not both This is used if the compressor rating is based upon rated return gas temperature (Rated Suction Temperature)',
        },
    )
    rated_liquid_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Use this input field OR the next, not both This is used if the compressor rating is based upon rated liquid temperature at the expansion valve',
        },
    )
    rated_subcooling: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Use this input field OR the previous, not both This is used if the compressor rating is based upon degrees of subcooling',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    mode_of_operation: Literal['', 'Subcritical', 'Transcritical'] | None = Field(
        default='Subcritical'
    )
    transcritical_compressor_power_curve_name: BivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['BivariateFunctions']}
    )
    transcritical_compressor_capacity_curve_name: BivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['BivariateFunctions']}
    )


class RefrigerationCompressorList(IDFBaseModel):
    """List of all the compressors included within a single refrigeration system
    (Refrigeration:System). Each list must contain at least one compressor. The
    order in which the individual compressors are listed here will be the order
    in which the compressors are dispatched to meet the system load. IMPORTANT:
    List compressor names in the order in which the compressors will be loaded
    Data is available for many compressors in the RefrigerationCompressor.idf
    dataset"""

    _idf_object_type: ClassVar[str] = 'Refrigeration:CompressorList'
    name: str = Field(...)
    compressors: list[RefrigerationCompressorListCompressorsItem] | None = Field(
        default=None
    )


class RefrigerationCompressorRack(IDFBaseModel):
    """Works in conjunction with the refrigeration case and walk-in objects to
    simulate the performance of a refrigerated case system. This object models
    the electric consumption of the rack compressors and the condenser fans.
    Heat can be rejected either outdoors or to a zone. Compressor rack waste
    heat can also be reclaimed for use by an optional air- or water-heating coil
    (Coil:Heating:Desuperheater and Coil:WaterHeating:Desuperheater)."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:CompressorRack'
    name: str = Field(...)
    heat_rejection_location: Literal['', 'Outdoors', 'Zone'] | None = Field(
        default='Outdoors'
    )
    design_compressor_rack_cop: float | None = Field(
        default=2.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'It is important that this COP correspond to the lowest saturated suction temperature needed to serve all refrigeration loads',
        },
    )
    compressor_rack_cop_function_of_temperature_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'It is important that this COP curve correspond to the lowest saturated suction temperature needed to serve all refrigeration loads',
        },
    )
    design_condenser_fan_power: float | None = Field(
        default=250.0,
        ge=0.0,
        json_schema_extra={'units': 'W', 'note': 'Design power for condenser fan(s).'},
    )
    condenser_fan_power_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    condenser_type: (
        Literal['', 'AirCooled', 'EvaporativelyCooled', 'WaterCooled'] | None
    ) = Field(
        default='AirCooled',
        json_schema_extra={
            'note': 'Applicable only when Heat Rejection Location is Outdoors.'
        },
    )
    water_cooled_condenser_inlet_node_name: str | None = Field(default=None)
    water_cooled_condenser_outlet_node_name: str | None = Field(default=None)
    water_cooled_loop_flow_type: Literal['', 'ConstantFlow', 'VariableFlow'] | None = (
        Field(
            default='VariableFlow',
            json_schema_extra={
                'note': 'Applicable only when Condenser Type is WaterCooled.'
            },
        )
    )
    water_cooled_condenser_outlet_temperature_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Applicable only when loop Flow type is VariableFlow.',
            },
        )
    )
    water_cooled_condenser_design_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Applicable only when loop flow type is ConstantFlow.',
        },
    )
    water_cooled_condenser_maximum_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3/s'}
    )
    water_cooled_condenser_maximum_water_outlet_temperature: float | None = Field(
        default=55.0, ge=10.0, le=60.0, json_schema_extra={'units': 'C'}
    )
    water_cooled_condenser_minimum_water_inlet_temperature: float | None = Field(
        default=10.0, ge=10.0, le=30.0, json_schema_extra={'units': 'C'}
    )
    evaporative_condenser_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 indicate that evaporative cooling of the condenser is available. This schedule allows the user to de...',
        },
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.9,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Applicable only for Condenser Type = EvaporativlyCooled.',
        },
    )
    evaporative_condenser_air_flow_rate: float | Literal['', 'Autocalculate'] | None = (
        Field(
            default='Autocalculate',
            json_schema_extra={
                'units': 'm3/s',
                'note': 'Applicable only for Condenser Type = EvaporativelyCooled. Used to calculate evaporative condenser water use.',
            },
        )
    )
    basin_heater_capacity: float | None = Field(
        default=200.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the evaporatively cooled condenser is available (field Evaporative Condenser Availability Schedule Name). For t...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the outdoor dry-bulb temperature at which the basin heater turns on.',
        },
    )
    design_evaporative_condenser_water_pump_power: (
        float | Literal['', 'Autocalculate'] | None
    ) = Field(
        default=1000.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Design recirc water pump power for Condenser Type = EvaporativelyCooled. Applicable only for Condenser Type = EvaporativelyCooled.',
        },
    )
    evaporative_water_supply_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['WaterStorageTankNames'],
            'note': 'If blank, water supply is from Mains. Applicable only for Condenser Type = EvaporativelyCooled.',
        },
    )
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Applicable only when Heat Rejection Location is Outdoors and Condenser Type is not WaterCooled; otherwise, leave field blank. If field is left blank with Heat Rejection Location = Outdoors, then th...'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name: (
        RefrigerationCaseAndWalkInAndListNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInAndListNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:Walkin or Refrigeration:CaseAndWalkinList object.',
        },
    )
    heat_rejection_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object. Required only if walk-in[s] are connected to this rack AND the heat rejection location is "Zone"',
        },
    )


class RefrigerationCondenserAirCooled(IDFBaseModel):
    """Air cooled condenser for a refrigeration system (Refrigeration:System)."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Condenser:AirCooled'
    name: str = Field(...)
    rated_effective_total_heat_rejection_rate_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Rating as per ARI 460 Be sure the rating corresponds to the correct refrigerant HeatRejection(W)=C1 +C2(Condensing Temp - Entering Air Temp, deg C) Will be adjusted for elevation automatically',
        },
    )
    rated_subcooling_temperature_difference: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'must correspond to rating given for total heat rejection effect',
        },
    )
    condenser_fan_speed_control_type: (
        Literal['', 'Fixed', 'FixedLinear', 'TwoSpeed', 'VariableSpeed'] | None
    ) = Field(default='Fixed')
    rated_fan_power: float | None = Field(
        default=250.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Power for condenser fan(s) corresponding to rated total heat rejection effect.',
        },
    )
    minimum_fan_air_flow_ratio: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Minimum air flow fraction through condenser fan',
        },
    )
    air_inlet_node_name_or_zone_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If field is left blank, then the model assumes that the inlet air conditions are the outdoor air conditions for the current timestep (e.g., no adjustment for height above ground). If the condenser ...'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    condenser_refrigerant_operating_charge_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_receiver_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_piping_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )


class RefrigerationCondenserCascade(IDFBaseModel):
    """Cascade condenser for a refrigeration system (Refrigeration:System). The
    cascade condenser is unlike the other condenser options because it rejects
    heat to another, higher-temperature, refrigeration system. That is, the
    cascade condenser acts as a heat rejection object for one system, but acts
    as a refrigeration load for another system."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Condenser:Cascade'
    name: str = Field(...)
    rated_condensing_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the condensing temperature for the lower temperature secondary loop',
        },
    )
    rated_approach_temperature_difference: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This is the difference between the condensing and evaporating temperatures',
        },
    )
    rated_effective_total_heat_rejection_rate: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'used for identification and rough system size error checking',
        },
    )
    condensing_temperature_control_type: Literal['', 'Fixed', 'Float'] | None = Field(
        default='Fixed',
        json_schema_extra={
            'note': 'Fixed keeps condensing temperature constant Float sets the condensing temperature according to the other loads on the higher temperature system'
        },
    )
    condenser_refrigerant_operating_charge_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_receiver_refrigerant_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_piping_refrigerant_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )


class RefrigerationCondenserEvaporativeCooled(IDFBaseModel):
    """Evaporative-cooled condenser for a refrigeration system
    (Refrigeration:System)."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Condenser:EvaporativeCooled'
    name: str = Field(...)
    rated_effective_total_heat_rejection_rate: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Rating as per ARI 490 Be sure the rating corresponds to the correct refrigerant',
        },
    )
    rated_subcooling_temperature_difference: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'must correspond to rating given for total heat rejection effect',
        },
    )
    fan_speed_control_type: (
        Literal['', 'Fixed', 'FixedLinear', 'TwoSpeed', 'VariableSpeed'] | None
    ) = Field(default='Fixed')
    rated_fan_power: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Power for condenser fan(s) corresponding to rated total heat rejection effect.',
        },
    )
    minimum_fan_air_flow_ratio: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Minimum air flow fraction through condenser fan',
        },
    )
    approach_temperature_constant_term: float | None = Field(
        default=6.63,
        ge=0.0,
        le=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'A1 in delta T = A1 + A2(hrcf) + A3/(hrcf) + A4(Twb)',
        },
    )
    approach_temperature_coefficient_2: float | None = Field(
        default=0.468,
        ge=0.0,
        le=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'A2 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)',
        },
    )
    approach_temperature_coefficient_3: float | None = Field(
        default=17.93,
        ge=0.0,
        le=30.0,
        json_schema_extra={
            'units': 'C',
            'note': 'A3 in delta T = A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)',
        },
    )
    approach_temperature_coefficient_4: float | None = Field(
        default=-0.322,
        ge=-20.0,
        le=20.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'A4 in deltaT=A1 + A2(hrcf) +A3/(hrcf) +A4(Twb)',
        },
    )
    minimum_capacity_factor: float | None = Field(
        default=0.5,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "taken from manufacturer's Heat Rejection Capacity Factor Table",
        },
    )
    maximum_capacity_factor: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "taken from manufacturer's Heat Rejection Capacity Factor Table",
        },
    )
    air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If field is left blank, then the model assumes that the inlet air conditions are the outdoor air conditions for the current timestep (e.g., no adjustment for height above ground).'
        },
    )
    rated_air_flow_rate: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use and fan energy use.',
        },
    )
    basin_heater_capacity: float | None = Field(
        default=200.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for periods when the evap condenser is available (field Evaporative Condenser Availability Schedule). For this situation, the heater heats the basin water when the outdoor a...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the outdoor dry-bulb temperature at which the basin heater turns on.',
        },
    )
    rated_water_pump_power: float | Literal['', 'Autocalculate'] | None = Field(
        default=1000.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Design recirculating water pump power.',
        },
    )
    evaporative_water_supply_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['WaterStorageTankNames'],
            'note': 'If blank, water supply is from Mains.',
        },
    )
    evaporative_condenser_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values greater than 0 indicate that evaporative cooling of the condenser is available. This schedule allows the user to define seasonal shutdown/draining of the water cooling system in col...',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    condenser_refrigerant_operating_charge_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_receiver_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_piping_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )


class RefrigerationCondenserWaterCooled(IDFBaseModel):
    """Water cooled condenser for a refrigeration system (Refrigeration:System)."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Condenser:WaterCooled'
    name: str = Field(...)
    rated_effective_total_heat_rejection_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Rating as per ARI 450 Be sure the rating corresponds to the correct refrigerant not used in calculations, only for identification and output',
        },
    )
    rated_condensing_temperature: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'must correspond to rating given for total heat rejection effect',
        },
    )
    rated_subcooling_temperature_difference: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'must correspond to rating given for total heat rejection effect',
        },
    )
    rated_water_inlet_temperature: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'must correspond to rating given for total heat rejection effect',
        },
    )
    water_inlet_node_name: str | None = Field(default=None)
    water_outlet_node_name: str | None = Field(default=None)
    water_cooled_loop_flow_type: Literal['', 'ConstantFlow', 'VariableFlow'] | None = (
        Field(default='VariableFlow')
    )
    water_outlet_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Applicable only when loop flow type is Variable Flow.',
        },
    )
    water_design_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'note required units must be converted from L/s as specified in ARI 450-2007 Applicable only when loop flow type is Constant Flow.',
        },
    )
    water_maximum_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3/s'}
    )
    water_maximum_water_outlet_temperature: float | None = Field(
        default=55.0, ge=10.0, le=60.0, json_schema_extra={'units': 'C'}
    )
    water_minimum_water_inlet_temperature: float | None = Field(
        default=10.0,
        ge=10.0,
        le=30.0,
        json_schema_extra={
            'units': 'C',
            'note': 'related to the minimum allowed refrigeration system condensing temperature',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    condenser_refrigerant_operating_charge_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_receiver_refrigerant_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    condensate_piping_refrigerant_inventory: float | None = Field(
        default=None, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )


class RefrigerationGasCoolerAirCooled(IDFBaseModel):
    """The transcritical refrigeration system requires a single gas cooler to
    reject the system heat."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:GasCooler:AirCooled'
    name: str = Field(...)
    rated_total_heat_rejection_rate_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Be sure the rating corresponds to the correct refrigerant (R744) HeatRejection(W)=C1 +C2(Gas Cooler Outlet Temp - Entering Air Temp, deg C) Will be adjusted for elevation automatically',
        },
    )
    gas_cooler_fan_speed_control_type: (
        Literal['', 'Fixed', 'FixedLinear', 'TwoSpeed', 'VariableSpeed'] | None
    ) = Field(default='Fixed')
    rated_fan_power: float | None = Field(
        default=5000.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Power for gas cooler fan(s) corresponding to rated total heat rejection effect.',
        },
    )
    minimum_fan_air_flow_ratio: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Minimum air flow fraction through gas cooler fan',
        },
    )
    transition_temperature: float | None = Field(
        default=27.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Temperature at which system transitions between subcritical and transcritical operation.',
        },
    )
    transcritical_approach_temperature: float | None = Field(
        default=3.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Temperature difference between the CO2 exiting the gas cooler and the air entering the gas cooler during transcritical operation.',
        },
    )
    subcritical_temperature_difference: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Temperature difference between the saturated condensing temperature and the air temperature during subcritical operation.',
        },
    )
    minimum_condensing_temperature: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Minimum saturated condensing temperature during subcritical operation.',
        },
    )
    air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If field is left blank, then the model assumes that the inlet air conditions are the outdoor air conditions for the current timestep (e.g., no adjustment for height above ground).'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    gas_cooler_refrigerant_operating_charge_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    gas_cooler_receiver_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )
    gas_cooler_outlet_piping_refrigerant_inventory: float | None = Field(
        default=0.0, json_schema_extra={'units': 'kg', 'note': 'optional input'}
    )


class RefrigerationSecondarySystem(IDFBaseModel):
    """Works in conjunction with refrigerated cases and walkins to simulate the
    performance of a secondary loop supermarket refrigeration system. Heat from
    the refrigeration loads served by the secondary loop is absorbed by a
    primary refrigeration system (Refrigeration:System). The SecondarySystem
    object simulates a heat exchanger that is an evaporator, or refrigeration
    load, on the primary refrigeration system."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:SecondarySystem'
    name: str = Field(...)
    refrigerated_case_or_walkin_or_caseandwalkinlist_name: RefrigerationCaseAndWalkInAndListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInAndListNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object. If there is more than one refrigerated case or walk-in served by this secondary system, enter the name of a Refrigeration:Case...',
        },
    )
    circulating_fluid_type: Literal['FluidAlwaysLiquid', 'FluidPhaseChange'] = Field(
        ...,
        json_schema_extra={
            'note': 'If "FluidAlwaysLiquid" is selected, the fluid properties must be input using the objects: FluidProperties:Name, FluidProperties:GlycolConcentration, and, if user defined fluid type, FluidProperties...'
        },
    )
    circulating_fluid_name: FluidAndGlycolNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FluidAndGlycolNames'],
            'note': 'This must correspond to a name in the FluidProperties:Name object.',
        },
    )
    evaporator_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR Evaporator Flow Rate for Secondary Fluid, is required. For "FluidPhaseChange", the default capacity is the sum of the rated ...',
        },
    )
    evaporator_flow_rate_for_secondary_fluid: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'For "FluidAlwaysLiquid", at least one of the two, Evaporator Capacity OR Evaporator Flow Rate for Secondary Fluid, is required. For "FluidPhaseChange" loops, this input is not used. (see PhaseChang...',
        },
    )
    evaporator_evaporating_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'This is the evaporating temperature in the heat exchanger used to chill or condense the secondary loop circulating fluid. It is NOT the temperature in any cases or walk-ins served by the secondary ...',
        },
    )
    evaporator_approach_temperature_difference: float = Field(
        ...,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'For "FluidAlwaysLiquid", this is the rated difference between the temperature of the circulating fluid leaving the heat exchanger and the heat exchanger\'s rated evaporating temperature. For "FluidP...',
        },
    )
    evaporator_range_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'For "FluidAlwaysLiquid", this is the rated difference between the temperature of the circulating fluid entering the heat exchanger and the temperature of the circulating fluid leaving the heat exch...',
        },
    )
    number_of_pumps_in_loop: int | None = Field(default=1)
    total_pump_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'For "FluidAlwaysLiquid",if not input, Evaporator Flow Rate for Secondary Fluid will be used. For "FluidPhaseChange", if not input, this will be calculated using the PhaseChange Circulating Rate.',
        },
    )
    total_pump_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Either the Total Pump Power or the Total Pump Head is required.',
        },
    )
    total_pump_head: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Either the Total Pump Power or the Total Pump Head is required.',
        },
    )
    phasechange_circulating_rate: float | None = Field(
        default=2.5,
        ge=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This is the total mass flow at the pump divided by the gaseous mass flow leaving the refrigeration load.',
        },
    )
    pump_drive_type: Literal['', 'Constant', 'Variable'] | None = Field(
        default='Constant'
    )
    variable_speed_pump_cubic_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Variable Speed Pump Curve Name is applicable to variable speed pumps only.',
        },
    )
    pump_motor_heat_to_fluid: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This is the portion of the pump motor heat added to secondary circulating fluid and is equal to the motor efficiency for non-hermetic motor. Enter 1.0 for a semi-hermetic motor.',
        },
    )
    sum_ua_distribution_piping: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use only if you want to include distribution piping heat gain in refrigeration load.',
        },
    )
    distribution_piping_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This will be used to determine the temperature used for distribution piping heat gain. The pipe heat gains are also counted as cooling credit for the zone. Required only if Sum UA Distribution Pipi...',
        },
    )
    sum_ua_receiver_separator_shell: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use only if you want to include Receiver/Separator Shell heat gain in refrigeration load.',
        },
    )
    receiver_separator_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This will be used to determine the temperature used for Receiver/Separator Shell heat gain. The shell heat gains are also counted as cooling credit for the zone. Required only if Sum UA Receiver/Se...',
        },
    )
    evaporator_refrigerant_inventory: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'kg',
            'note': 'This value refers to the refrigerant circulating within the primary system providing cooling to the chiller for the secondary loop, not to the fluid circulating within the secondary loop itself.',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class RefrigerationSubcooler(IDFBaseModel):
    """Two types of subcoolers are modeled by the detailed refrigeration system.
    The liquid suction heat exchanger uses cool suction gas to subcool the hot
    condensate after it leaves the condenser and before it reaches the thermal
    expansion valve. A mechanical subcooler is used to transfer cooling capacity
    from one refrigeration system to another."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:Subcooler'
    name: str = Field(...)
    subcooler_type: Literal['', 'LiquidSuction', 'Mechanical'] | None = Field(
        default='LiquidSuction',
        json_schema_extra={'note': 'plan to add ambient subcoolers at future time'},
    )
    liquid_suction_design_subcooling_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Applicable only and required for liquid suction heat exchangers design liquid suction subcooling',
        },
    )
    design_liquid_inlet_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'design inlet temperature on liquid side Applicable only and required for liquid suction heat exchangers (LSHX)',
        },
    )
    design_vapor_inlet_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'design inlet temperature on vapor side Applicable only and required for liquid suction heat exchangers (LSHX) Design vapor inlet temperature must be less than or equal to the Liquid inlet design temp',
        },
    )
    capacity_providing_system: RefrigerationSystemNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationSystemNames'],
            'note': 'Name of the Detailed Refrigeration System providing cooling capacity Applicable only and required for mechanical subcoolers',
        },
    )
    outlet_control_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Control Temperature Out for subcooled liquid Applicable only and required for mechanical subcoolers',
        },
    )


class RefrigerationSystem(IDFBaseModel):
    """Simulates the performance of a supermarket refrigeration system when used
    along with other objects to define the refrigeration load(s), the
    compressor(s), and the condenser."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:System'
    name: str = Field(...)
    refrigerated_case_or_walkin_or_caseandwalkinlist_name: (
        RefrigerationCaseAndWalkInAndListNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInAndListNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object. If there is more than one refrigerated case or walk-in served by this system, enter the name of a Refrigeration:CaseAndWalkInL...',
        },
    )
    refrigeration_transfer_load_or_transferload_list_name: (
        RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNamesRef
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames'
            ],
            'note': 'Enter the name of a Refrigeration:SecondarySystem object OR a Refrigeration:Condenser:Cascade object OR, a Refrigeration:TransferLoadList object. A transfer load is identified as one which moves th...',
        },
    )
    refrigeration_condenser_name: RefrigerationAllTypesCondenserNamesRef = Field(
        ..., json_schema_extra={'object_list': ['RefrigerationAllTypesCondenserNames']}
    )
    compressor_or_compressorlist_name: RefrigerationCompressorAndListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['RefrigerationCompressorAndListNames']}
    )
    minimum_condensing_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'related to the proper operation of the thermal expansion valves and compressors',
        },
    )
    refrigeration_system_working_fluid_type: FluidNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FluidNames'],
            'note': 'Fluid property data for the refrigerant must be entered. The fluid property data, including the objects: FluidProperties:Name, FluidProperties:Temperatures, FluidProperties:Saturated and FluidPrope...',
        },
    )
    suction_temperature_control_type: (
        Literal['', 'ConstantSuctionTemperature', 'FloatSuctionTemperature'] | None
    ) = Field(default='ConstantSuctionTemperature')
    mechanical_subcooler_name: RefrigerationSubcoolerNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationSubcoolerNames'],
            'note': 'Optional Field Recipient of refrigeration capacity, that is receives cool liquid from another refrigeration system to help meet aggregate case loads',
        },
    )
    liquid_suction_heat_exchanger_subcooler_name: (
        RefrigerationSubcoolerNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationSubcoolerNames'],
            'note': 'Optional Field Liquid Suction Heat Exchanger Name, or leave blank',
        },
    )
    sum_ua_suction_piping: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use only if you want to include suction piping heat gain in refrigeration load',
        },
    )
    suction_piping_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This will be used to determine the temperature used for distribution piping heat gain and the pipe heat gains  as cooling credit for the zone. Required only if Sum UA Distribution Piping >0.0',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    number_of_compressor_stages: Literal[1, 2] | Literal[''] | None = Field(default=1)
    intercooler_type: (
        Literal['', 'Flash Intercooler', 'None', 'Shell-and-Coil Intercooler'] | None
    ) = Field(default='None')
    shell_and_coil_intercooler_effectiveness: float | None = Field(default=0.8)
    high_stage_compressor_or_compressorlist_name: (
        RefrigerationCompressorAndListNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={'object_list': ['RefrigerationCompressorAndListNames']},
    )


class RefrigerationTranscriticalSystem(IDFBaseModel):
    """Detailed transcritical carbon dioxide (CO2) booster refrigeration systems
    used in supermarkets. The object allows for modeling either a single stage
    system with medium-temperature loads or a two stage system with both medium-
    and low-temperature loads."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:TranscriticalSystem'
    name: str = Field(...)
    system_type: Literal['SingleStage', 'TwoStage'] = Field(...)
    medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name: RefrigerationCaseAndWalkInAndListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInAndListNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object. If there is more than one refrigerated case or walk-in served by this system, enter the name of a Refrigeration:CaseAndWalkInL...',
        },
    )
    low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name: (
        RefrigerationCaseAndWalkInAndListNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RefrigerationCaseAndWalkInAndListNames'],
            'note': 'Enter the name of a Refrigeration:Case or Refrigeration:WalkIn object. If there is more than one refrigerated case or walk-in served by this system, enter the name of a Refrigeration:CaseAndWalkInL...',
        },
    )
    refrigeration_gas_cooler_name: RefrigerationAllTypesGasCoolerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['RefrigerationAllTypesGasCoolerNames']}
    )
    high_pressure_compressor_or_compressorlist_name: RefrigerationCompressorAndListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['RefrigerationCompressorAndListNames']}
    )
    low_pressure_compressor_or_compressorlist_name: (
        RefrigerationCompressorAndListNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={'object_list': ['RefrigerationCompressorAndListNames']},
    )
    receiver_pressure: float | None = Field(
        default=4000000.0, json_schema_extra={'units': 'Pa'}
    )
    subcooler_effectiveness: float | None = Field(default=0.4)
    refrigeration_system_working_fluid_type: FluidNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FluidNames'],
            'note': 'Fluid property data for the refrigerant must be entered. The fluid property data, including the objects: FluidProperties:Name, FluidProperties:Temperatures, FluidProperties:Saturated and FluidPrope...',
        },
    )
    sum_ua_suction_piping_for_medium_temperature_loads: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use only if you want to include suction piping heat gain in refrigeration load',
        },
    )
    medium_temperature_suction_piping_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This will be used to determine the temperature used for distribution piping heat gain and the pipe heat gains as cooling credit for the zone. Required only if Sum UA Distribution Piping for Medium ...',
        },
    )
    sum_ua_suction_piping_for_low_temperature_loads: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use only if you want to include suction piping heat gain in refrigeration load',
        },
    )
    low_temperature_suction_piping_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This will be used to determine the temperature used for distribution piping heat gain and the pipe heat gains as cooling credit for the zone. Required only if Sum UA Distribution Piping for Low Tem...',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )


class RefrigerationTransferLoadList(IDFBaseModel):
    """A refrigeration system may provide cooling to other, secondary, systems
    through either a secondary loop or a cascade condenser. If multiple transfer
    loads are served by a single primary system, use this list to group them
    together for reference by the primary system (see the field \"Refrigeration
    Transfer Load or TransferLoad List Name\" in the Refrigeration:System
    object)."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:TransferLoadList'
    name: str = Field(...)
    transfer_loads: list[RefrigerationTransferLoadListTransferLoadsItem] | None = Field(
        default=None
    )


class RefrigerationWalkIn(IDFBaseModel):
    """Works in conjunction with a compressor rack, a refrigeration system, or a
    refrigeration secondary system to simulate the performance of a walk-in
    cooler. The walk-in cooler model uses information at rated conditions along
    with input descriptions for heat transfer surfaces facing multiple zones to
    determine performance."""

    _idf_object_type: ClassVar[str] = 'Refrigeration:WalkIn'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rated_coil_cooling_capacity: float = Field(..., json_schema_extra={'units': 'W'})
    operating_temperature: float = Field(..., lt=20.0, json_schema_extra={'units': 'C'})
    rated_cooling_source_temperature: float = Field(
        ...,
        ge=-70.0,
        le=40.0,
        json_schema_extra={
            'units': 'C',
            'note': 'If DXEvaporator, use evaporating temperature (saturated suction temperature) If BrineCoil, use Brine entering temperature used to set minimum suction pressure for DX systems and minimum brine temp ...',
        },
    )
    rated_total_heating_power: float = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Include total for all anti-sweat, door, drip-pan, and floor heater power Do not include defrost heater power',
        },
    )
    heating_power_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Values will be used to multiply the total heating power Values in the schedule should be between 0.0 and 1.0 For example, this could be used if display door antisweat heaters are turned off at nigh...',
        },
    )
    rated_cooling_coil_fan_power: float | None = Field(
        default=375.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    rated_circulation_fan_power: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    rated_total_lighting_power: float = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the total (display + task) installed lighting power.',
        },
    )
    lighting_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule should contain values between 0 and 1 Defaults to always on if schedule name left blank.',
        },
    )
    defrost_type: Literal['', 'Electric', 'HotFluid', 'None', 'OffCycle'] | None = (
        Field(
            default='Electric',
            json_schema_extra={
                'note': 'HotFluid includes either hot gas defrost for a DX system or Hot Brine defrost if this walk in is cooled by brine from a secondary chiller'
            },
        )
    )
    defrost_control_type: (
        Literal['', 'TemperatureTermination', 'TimeSchedule'] | None
    ) = Field(default='TimeSchedule')
    defrost_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule values should be 0 (off) or 1 (on)',
        },
    )
    defrost_drip_down_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The schedule values should be 0 (off) or 1 (on) The start time for each defrost period in this drip-down schedule should coincide with the start time for each defrost period in the defrost schedule...',
        },
    )
    defrost_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'needed for all defrost types except none and offcycle',
        },
    )
    temperature_termination_defrost_fraction_to_ice: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This is the portion of the defrost energy that is available to melt frost Needed only for defrost control type TemperatureTermination defaults to 0.7 for electric defrost and to 0.3 for hot fluid d...',
        },
    )
    restocking_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values should be in units of Watts Leave this field blank if no restocking is to be modeled',
        },
    )
    average_refrigerant_charge_inventory: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'kg',
            'note': 'This value is only used if the Cooling Source Type is DXEvaporator',
        },
    )
    insulated_floor_surface_area: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm2', 'note': 'floor area of walk-in cooler'},
    )
    insulated_floor_u_value: float | None = Field(
        default=0.3154,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'The default value corresponds to R18 [ft2-F-hr/Btu] To convert other IP R-values to U, divide 5.678 by the R-value Some examples: R15 is U 0.3785 W/m2-K R5 is U 1.136 W/m2-K',
        },
    )
    zone_data: list[RefrigerationWalkInZoneDataItem] | None = Field(default=None)


class ZoneHVACRefrigerationChillerSet(IDFBaseModel):
    """Works in conjunction with one or multiple air chillers, compressor racks,
    refrigeration systems, or refrigeration secondary system objects to simulate
    the performance of a group of air chillers cooling a single zone. The
    chiller set model passes information about the zone conditions to determine
    the performance of individual chiller coils within the set, thus providing
    the sensible and latent heat exchange with the zone environment."""

    _idf_object_type: ClassVar[str] = 'ZoneHVAC:RefrigerationChillerSet'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This must be a controlled zone and appear in a ZoneHVAC:EquipmentConnections object.',
        },
    )
    air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Not used - reserved for future use Name of the zone exhaust node (see Node) from which the refrigeration chiller draws its indoor air. This should be one of the zone exhaust nodes for the zone cool...'
        },
    )
    air_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Not used - reserved for future use The name of the node where the chiller coil sends its outlet air, which must be one of the inlet air nodes for the zone which is being cooled.'
        },
    )
    chillers: list[ZoneHVACRefrigerationChillerSetChillersItem] | None = Field(
        default=None
    )
