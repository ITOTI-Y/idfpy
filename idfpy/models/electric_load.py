"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Electric Load Center-Generator Specifications
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllShadingAndHTSurfNamesRef,
    BivariateFunctionsRef,
    ConverterListRef,
    ElecStorageListRef,
    FCAirSupNamesRef,
    FCAuxHeatNamesRef,
    FCExhaustHXNamesRef,
    FCInverterNamesRef,
    FCPMNamesRef,
    FCStackCoolerNamesRef,
    FCStorageNamesRef,
    FCWaterSupNamesRef,
    GeneratorListsRef,
    GeneratorNamesRef,
    GenFuelSupNamesRef,
    InverterListRef,
    MicroCHPParametersNamesRef,
    PVModulesRef,
    ScheduleNamesRef,
    TransformerNamesRef,
    TrivariateFunctionsRef,
    UnivariateFunctionsRef,
    ZoneNamesRef,
)


class ElectricLoadCenterGeneratorsGeneratorOutputsItem(IDFBaseModel):
    """Nested object type for array items."""

    generator_name: GeneratorNamesRef = Field(
        ..., json_schema_extra={'object_list': ['GeneratorNames']}
    )
    generator_object_type: Literal[
        'Generator:CombustionTurbine',
        'Generator:FuelCell',
        'Generator:InternalCombustionEngine',
        'Generator:MicroCHP',
        'Generator:MicroTurbine',
        'Generator:PVWatts',
        'Generator:Photovoltaic',
        'Generator:WindTurbine',
    ] = Field(...)
    generator_rated_electric_power_output: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    generator_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this generator. Schedule value > 0 means the generator is available. If this field is blank, the generator is always available.',
        },
    )
    generator_rated_thermal_to_electrical_power_ratio: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required field when generator is used by an ElectricLoadCenter:Distribution object with Generator Operation Scheme set to FollowThermal or FollowThermalLimitElectrical'
        },
    )


class ElectricLoadCenterTransformerMetersItem(IDFBaseModel):
    """Nested object type for array items."""

    meter_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Must be an electric meter (with electricity as the resource type) Only required when transformer is used for power in from the utility grid'
        },
    )


class GeneratorFuelCellAirSupplyConstituentFractionsItem(IDFBaseModel):
    """Nested object type for array items."""

    constituent_name: (
        Literal['Argon', 'CarbonDioxide', 'Nitrogen', 'Oxygen', 'Water'] | None
    ) = Field(default=None)
    molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)


class ElectricLoadCenterDistribution(IDFBaseModel):
    """ElectricLoadCenter:Distribution objects are used to include on-site
    electricity generators and or storage in a simulation."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Distribution'
    name: str = Field(...)
    generator_list_name: GeneratorListsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['GeneratorLists'],
            'note': 'Name of an ElectricLoadCenter:Generators object',
        },
    )
    generator_operation_scheme_type: (
        Literal[
            'Baseload',
            'DemandLimit',
            'FollowThermal',
            'FollowThermalLimitElectrical',
            'TrackElectrical',
            'TrackMeter',
            'TrackSchedule',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Determines how generators are to be controlled Required if Generator List is entered.'
        },
    )
    generator_demand_limit_scheme_purchased_electric_demand_limit: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    generator_track_schedule_name_scheme_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'required when Generator Operation Scheme Type=TrackSchedule schedule values in Watts',
        },
    )
    generator_track_meter_scheme_meter_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required when Generator Operation Scheme Type=TrackMeter'
        },
    )
    electrical_buss_type: (
        Literal[
            '',
            'AlternatingCurrent',
            'AlternatingCurrentWithStorage',
            'DirectCurrentWithInverter',
            'DirectCurrentWithInverterACStorage',
            'DirectCurrentWithInverterDCStorage',
        ]
        | None
    ) = Field(default='AlternatingCurrent')
    inverter_name: InverterListRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['InverterList'],
            'note': 'required when Electrical Buss Type=DirectCurrentWithInverter, DirectCurrentWithInverterDCStorage, or DirectCurrentWithInverterACStorage',
        },
    )
    electrical_storage_object_name: ElecStorageListRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ElecStorageList'],
            'note': 'required when Electrical Buss Type=AlternatingCurrentWithStorage, DirectCurrentWithInverterDCStorage, or DirectCurrentWithInverterACStorage',
        },
    )
    transformer_object_name: TransformerNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TransformerNames'],
            'note': 'required when power needs to be output from on-site generation or storage to the grid via transformer',
        },
    )
    storage_operation_scheme: (
        Literal[
            '',
            'FacilityDemandLeveling',
            'TrackChargeDischargeSchedules',
            'TrackFacilityElectricDemandStoreExcessOnSite',
            'TrackMeterDemandStoreExcessOnSite',
        ]
        | None
    ) = Field(
        default='TrackFacilityElectricDemandStoreExcessOnSite',
        json_schema_extra={
            'note': 'Select method to govern how storage charge and discharge is controlled TrackFacilityElectricDemandStoreExcessOnSite indicates that storage control will follow the facility power demand while accoun...'
        },
    )
    storage_control_track_meter_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'required when Storage Operation Scheme is set to TrackMeterDemandStoreExcessOnSite.'
        },
    )
    storage_converter_object_name: ConverterListRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ConverterList'],
            'note': 'Name of an ElectricLoadCenter:Storage:Converter used to convert AC to DC when charging DC storage from grid supply. A converter is expected when using Storage Operation Schemes FacilityDemandLeveli...',
        },
    )
    maximum_storage_state_of_charge_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'Fraction of storage capacity used as upper limit for controlling charging, for all storage operation schemes.'
        },
    )
    minimum_storage_state_of_charge_fraction: float | None = Field(
        default=0.0,
        json_schema_extra={
            'note': 'Fraction of storage capacity used as lower limit for controlling discharging, for all storage operation schemes.'
        },
    )
    design_storage_control_charge_power: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Maximum rate that electric power can be charged into storage. Storage charging adjusted downward for conversion losses. Rate is modified by fractional values in the schedule named in the next field...',
        },
    )
    storage_charge_power_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Controls timing and magnitude of charging storage. Required field if Storage Operation Scheme is set to TrackChargeDischargeSchedules. Schedule values should be fractions from 0.0 to 1.0, inclusive.',
        },
    )
    design_storage_control_discharge_power: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Maximum rate that electric power can be discharged from storage. Rate is modified by fractional values in the schedule named in the next field. Required field when using Storage Operation Schemes F...',
        },
    )
    storage_discharge_power_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Controls timing and magnitude of discharging storage Required field if Storage Operation Scheme is set to TrackChargeDischargeSchedules. Schedule values should be fractions from 0.0 to 1.0, inclusive.',
        },
    )
    storage_control_utility_demand_target: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Target utility service demand power for discharge control. Storage draws are adjusted upwards for conversion losses. Required field for FacilityDemandLeveling storage operation scheme',
        },
    )
    storage_control_utility_demand_target_fraction_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Modifies the target utility service demand power over time. Schedule values should be fractions from -1.0 to 1.0, inclusive. if omitted a schedule value of 1.0 is used. Negative values indicate exp...',
        },
    )


class ElectricLoadCenterGenerators(IDFBaseModel):
    """List of electric power generators to include in the simulation including the
    name and type of each generators along with availability schedule, rated
    power output, and thermal-to-electrical power ratio."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Generators'
    name: str = Field(...)
    generator_outputs: list[ElectricLoadCenterGeneratorsGeneratorOutputsItem] | None = (
        Field(default=None)
    )


class ElectricLoadCenterInverterFunctionOfPower(IDFBaseModel):
    """Electric power inverter to convert from direct current (DC) to alternating
    current (AC) in an electric load center that contains photovoltaic modules.
    This input object is for an inverter model where efficiency is a function of
    normalized power."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Inverter:FunctionOfPower'
    name: str | None = Field(default=None)
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
            'note': 'Enter name of zone to receive inverter losses as heat if blank then inverter is assumed to be outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=None)
    efficiency_function_of_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve describes efficiency as a function of power curve is normalized relative to rated power in next field',
        },
    )
    rated_maximum_continuous_input_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    minimum_efficiency: float | None = Field(default=None, ge=0.0, le=1.0)
    maximum_efficiency: float | None = Field(default=None, ge=0.0, le=1.0)
    minimum_power_output: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    maximum_power_output: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    ancillary_power_consumed_in_standby: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )


class ElectricLoadCenterInverterLookUpTable(IDFBaseModel):
    """California Energy Commission tests and publishes data on inverters This
    inverter model interpolates using CEC test data Input data are at
    http://www.gosolarcalifornia.org/equipment/inverter_tests/summaries"""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Inverter:LookUpTable'
    name: str | None = Field(default=None)
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
            'note': 'Enter name of zone to receive inverter losses as heat if blank then inverter is assumed to be outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    rated_maximum_continuous_output_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    night_tare_loss_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    nominal_voltage_input: float | None = Field(
        default=None, json_schema_extra={'units': 'V'}
    )
    efficiency_at_10_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    efficiency_at_20_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    efficiency_at_30_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    efficiency_at_50_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    efficiency_at_75_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    efficiency_at_100_power_and_nominal_voltage: float | None = Field(
        default=None, ge=0.0, le=1.0
    )


class ElectricLoadCenterInverterPVWatts(IDFBaseModel):
    """Electric power inverter to convert from direct current (DC) to alternating
    current (AC) in an electric load center that contains Generator:PVWatts
    objects. It implements the PVWatts inverter performance curves."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Inverter:PVWatts'
    name: str | None = Field(default=None)
    dc_to_ac_size_ratio: float | None = Field(default=1.1, gt=0.0)
    inverter_efficiency: float | None = Field(default=0.96, le=1.0, gt=0.0)


class ElectricLoadCenterInverterSimple(IDFBaseModel):
    """Electric power inverter to convert from direct current (DC) to alternating
    current (AC) in an electric load center that contains photovoltaic modules.
    This input object is for the simplest inverter model and uses a fixed
    efficiency."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Inverter:Simple'
    name: str | None = Field(default=None)
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
            'note': 'enter name of zone to receive inverter losses as heat if blank then inverter is assumed to be outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    inverter_efficiency: float | None = Field(default=None, ge=0.0, le=1.0)


class ElectricLoadCenterStorageBattery(IDFBaseModel):
    """Uses the kinetic battery model (KiBaM) to simulate rechargeable battery
    banks in an electrical load center. The battery bank is a collection of one
    or more individual battery modules. Given the surplus or deficit power from
    the electrical system and the state of charge from the previous time step,
    this object can model the voltage, current, and energy losses with charging
    and discharging during each time step. The cumulative battery damage can be
    also modeled and reported at the end of each simulation run."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Storage:Battery'
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
            'note': 'Enter name of zone to receive electrical storage losses as heat if blank then electrical storage losses are dissipated to outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0)
    number_of_battery_modules_in_parallel: int | None = Field(
        default=1,
        ge=1,
        json_schema_extra={
            'note': 'A module usually consists of several cells. The total number of modules in the battery bank is equal to number of modules in parallel times number of modules in series.'
        },
    )
    number_of_battery_modules_in_series: int | None = Field(
        default=1,
        ge=1,
        json_schema_extra={
            'note': 'A module usually consists of several cells. The total number of modules in the battery bank is equal to number of modules in parallel times number of modules in series.'
        },
    )
    maximum_module_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'Ah',
            'note': "The capacity is for each module. A model parameter from manufacturer's data or test data.",
        },
    )
    initial_fractional_state_of_charge: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'The state of charge is evaluated based on the maximum capacity defined in the next field.'
        },
    )
    fraction_of_available_charge_capacity: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'A model parameter usually derived from test data by curve fitting.'
        },
    )
    change_rate_from_bound_charge_to_available_charge: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': '1/hr',
            'note': 'A model parameter usually derived from test data by curve fitting.',
        },
    )
    fully_charged_module_open_circuit_voltage: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'The voltage is for each battery module.',
        },
    )
    fully_discharged_module_open_circuit_voltage: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'The voltage is for each battery module.',
        },
    )
    voltage_change_curve_name_for_charging: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Determines how the open circuit voltage change with state of charge relative to the fully discharged state.',
        },
    )
    voltage_change_curve_name_for_discharging: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Determines how the open circuit voltage change with state of charge relative to the fully charged state.',
        },
    )
    module_internal_electrical_resistance: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'ohms',
            'note': 'A model parameter from manufacture or derived from test data. Internal resistance is assumed to be constant. The internal resistance is for each battery module.',
        },
    )
    maximum_module_discharging_current: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'A',
            'note': 'The constraint on discharging current is for each battery module.',
        },
    )
    module_cut_off_voltage: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'The voltage constraint is for each battery module.',
        },
    )
    module_charge_rate_limit: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'note': 'units 1/hr Charge rate limit is the division between charging current the remaining capacity. The constraint on charging current is for each module.'
        },
    )
    battery_life_calculation: Literal['', 'No', 'Yes'] | None = Field(default='No')
    number_of_cycle_bins: int | None = Field(
        default=10,
        ge=5,
        json_schema_extra={
            'note': 'Only required when battery life calculation is activated'
        },
    )
    battery_life_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Determines the number of cycles to failure in relation to cycle range. Only required when battery life calculation is activated.',
        },
    )


class ElectricLoadCenterStorageConverter(IDFBaseModel):
    """This model is for converting AC to DC for grid-supplied charging of DC
    storage"""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Storage:Converter'
    name: str | None = Field(default=None)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the converter is always available.',
        },
    )
    power_conversion_efficiency_method: (
        Literal['', 'FunctionOfPower', 'SimpleFixed'] | None
    ) = Field(
        default='SimpleFixed',
        json_schema_extra={
            'note': 'SimpleFixed indicates power conversion losses are based on Simple Fixed Efficiency FunctionOfPower indicates power conversion losses are a function of normalized power using a curve or table.'
        },
    )
    simple_fixed_efficiency: float | None = Field(
        default=0.95,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Constant efficiency for conversion of AC to DC at all power levels. Field is only used when Power Conversion Efficiency Method is set to SimpleFixed.'
        },
    )
    design_maximum_continuous_input_power: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Required field when Power Conversion Efficiency Method is set to FunctionOfPower.',
        },
    )
    efficiency_function_of_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve or table with a single independent variable that describes efficiency as a function of normalized power. The "x" input for curve or table is the ratio of current input power divided by design...',
        },
    )
    ancillary_power_consumed_in_standby: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Optional standby power consumed when converter is available but no power is being conditioned.',
        },
    )
    zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'enter name of zone to receive converter losses as heat if blank then converter is assumed to be outdoors',
        },
    )
    radiative_fraction: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'fraction of zone heat gains treated as thermal radiation'
        },
    )


class ElectricLoadCenterStorageLiIonNMCBattery(IDFBaseModel):
    """Uses Lithium Ion NMC model to simulate rechargeable battery banks in an
    electrical load center. The battery bank is a collection of one or more
    individual battery modules. Given the surplus or deficit power from the
    electrical system and the state of charge from the previous time step, this
    object can model the voltage, current, and energy losses with charging and
    discharging during each time step. The cumulative battery damage can be also
    modeled and reported at the end of each simulation run."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Storage:LiIonNMCBattery'
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
            'note': 'Enter name of zone to receive electrical storage losses as heat if blank then electrical storage losses are dissipated to outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0)
    lifetime_model: Literal['', 'KandlerSmith', 'None'] | None = Field(
        default='KandlerSmith'
    )
    number_of_cells_in_series: int = Field(
        ...,
        ge=1,
        json_schema_extra={
            'note': 'Battery voltage is calculated by multiplying this field by the nominal cell voltage (Numeric Field 13, default 3.342V)'
        },
    )
    number_of_strings_in_parallel: int = Field(
        ...,
        ge=1,
        json_schema_extra={
            'note': 'Capacity (Ah) is determined by multiplying this field by the cell capacity (Numeric Field 14, default 3.2 Ah)'
        },
    )
    initial_fractional_state_of_charge: float | None = Field(
        default=0.5,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'The state of charge is evaluated based on the maximum capacity defined in the next field.'
        },
    )
    dc_to_dc_charging_efficiency: float | None = Field(default=0.95, le=1.0, gt=0.0)
    battery_mass: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg'})
    battery_surface_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2'})
    battery_specific_heat_capacity: float | None = Field(
        default=1500.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    heat_transfer_coefficient_between_battery_and_ambient: float | None = Field(
        default=7.5, gt=0.0, json_schema_extra={'units': 'W/m2-K'}
    )
    fully_charged_cell_voltage: float | None = Field(
        default=4.2,
        gt=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'Most users should not need to change this value.',
        },
    )
    cell_voltage_at_end_of_exponential_zone: float | None = Field(
        default=3.53,
        gt=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'Most users should not need to change this value.',
        },
    )
    cell_voltage_at_end_of_nominal_zone: float | None = Field(
        default=3.342,
        gt=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'Most users should not need to change this value.',
        },
    )
    default_nominal_cell_voltage: float | None = Field(
        default=3.342,
        gt=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'Most users should not need to change this value.',
        },
    )
    fully_charged_cell_capacity: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'Ah',
            'note': 'Most users should not need to change this value.',
        },
    )
    fraction_of_cell_capacity_removed_at_the_end_of_exponential_zone: float | None = (
        Field(
            default=0.8075,
            gt=0.0,
            lt=1.0,
            json_schema_extra={
                'note': 'Most users should not need to change this value.'
            },
        )
    )
    fraction_of_cell_capacity_removed_at_the_end_of_nominal_zone: float | None = Field(
        default=0.976875,
        gt=0.0,
        lt=1.0,
        json_schema_extra={'note': 'Most users should not need to change this value.'},
    )
    charge_rate_at_which_voltage_vs_capacity_curve_was_generated: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={'note': 'Most users should not need to change this value.'},
    )
    battery_cell_internal_electrical_resistance: float | None = Field(
        default=0.09,
        ge=0.0,
        json_schema_extra={
            'units': 'ohms',
            'note': 'for a single cell Most users should not need to change this value.',
        },
    )


class ElectricLoadCenterStorageSimple(IDFBaseModel):
    """Used to model storage of electricity in an electric load center. This is a
    simple model that does not attempt to represent any of the characteristics
    of a real storage device such as a battery. The type of power, AC or DC,
    depends on the configuration chosen as the Electrical Buss Type in the
    ElectricLoadCenter:Distribution object."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Storage:Simple'
    name: str | None = Field(default=None)
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
            'note': 'Enter name of zone to receive storage losses as heat if blank then storage is assumed to be outdoors',
        },
    )
    radiative_fraction_for_zone_heat_gains: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    nominal_energetic_efficiency_for_charging: float | None = Field(
        default=None, ge=0.001, le=1.0
    )
    nominal_discharging_energetic_efficiency: float | None = Field(
        default=None, ge=0.001, le=1.0
    )
    maximum_storage_capacity: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )
    maximum_power_for_discharging: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    maximum_power_for_charging: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    initial_state_of_charge: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )


class ElectricLoadCenterTransformer(IDFBaseModel):
    """This object is used to model the energy losses of transformers when they are
    used to transfer electricity from the grid to a building (as distribution
    transformers) or transfer electricity from onsite generators to the grid."""

    _idf_object_type: ClassVar[str] = 'ElectricLoadCenter:Transformer'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    transformer_usage: (
        Literal['', 'LoadCenterPowerConditioning', 'PowerInFromGrid', 'PowerOutToGrid']
        | None
    ) = Field(
        default='PowerInFromGrid',
        json_schema_extra={
            'note': 'A transformer can be used to transfer electric energy from utility grid to building (PowerInFromGrid)or from building on-site generation to the grid (PowerOutToGrid) or within a load center to matc...'
        },
    )
    zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter name of zone to receive transformer losses as heat if blank then transformer losses are dissipated to outdoors',
        },
    )
    radiative_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0)
    rated_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'VA',
            'note': 'the unit is VA, instead of kVA as usually shown on transformer nameplates.',
        },
    )
    phase: Literal[1, 3] | Literal[''] | None = Field(
        default=3,
        json_schema_extra={
            'note': 'Must be single or three phase transformer. NOT used in the current model.'
        },
    )
    conductor_material: Literal['', 'Aluminum', 'Copper'] | None = Field(
        default='Aluminum',
        json_schema_extra={'note': 'Winding material used by the transformer.'},
    )
    full_load_temperature_rise: float | None = Field(
        default=150.0, ge=50.0, le=180.0, json_schema_extra={'units': 'C'}
    )
    fraction_of_eddy_current_losses: float | None = Field(default=0.1, ge=0.0, le=1.0)
    performance_input_method: Literal['', 'NominalEfficiency', 'RatedLosses'] | None = (
        Field(
            default='RatedLosses',
            json_schema_extra={
                'note': 'User can define transformer performance by specifying load and no load losses at rated conditions or nameplate efficiency and maximum efficiency'
            },
        )
    )
    rated_no_load_loss: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Only required when RatedLosses is the performance input method',
        },
    )
    rated_load_loss: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Only required when RatedLosses is the performance input method',
        },
    )
    nameplate_efficiency: float | None = Field(
        default=0.98,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Only required when NominalEfficiency is the performance input method'
        },
    )
    per_unit_load_for_nameplate_efficiency: float | None = Field(
        default=0.35,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Percentage of the rated capacity at which the nameplate efficiency is defined Only required when NominalEfficiency is the performance input method'
        },
    )
    reference_temperature_for_nameplate_efficiency: float | None = Field(
        default=75.0,
        ge=20.0,
        le=150.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Conductor operating temperature at which the nameplate efficiency is defined Only required when NominalEfficiency is the performance input method',
        },
    )
    per_unit_load_for_maximum_efficiency: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Percentage of the rate capacity at which the maximum efficiency is obtained Only required when NominalEfficiency is the performance input method'
        },
    )
    consider_transformer_loss_for_utility_cost: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Only required when the transformer is used for power in from the utility grid'
        },
    )
    meters: list[ElectricLoadCenterTransformerMetersItem] | None = Field(default=None)


class GeneratorCombustionTurbine(IDFBaseModel):
    """This generator model is the empirical model from the Building Loads and
    System Thermodynamics (BLAST) program. Generator performance curves are
    generated by fitting catalog data to second order polynomial equations.
    Three sets of coefficients are required."""

    _idf_object_type: ClassVar[str] = 'Generator:CombustionTurbine'
    name: str = Field(...)
    rated_power_output: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    electric_circuit_node_name: str | None = Field(default=None)
    minimum_part_load_ratio: float | None = Field(default=None, ge=0.0, le=1.0)
    maximum_part_load_ratio: float | None = Field(default=None, le=1.0, gt=0.0)
    optimum_part_load_ratio: float | None = Field(default=None)
    part_load_based_fuel_input_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output this curve is multiplied to the Temperature Based Fuel Input Curve to determine Fuel Energy In',
        },
    )
    temperature_based_fuel_input_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*AT + c*AT**2 AT = Ambient Delta T this curve is multiplied to the Part Load Based Fuel Input Curve to determine Fuel Energy In',
        },
    )
    exhaust_flow_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*AT + c*AT**2 AT = Ambient Delta T',
        },
    )
    part_load_based_exhaust_temperature_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output this curve is multiplied to the Temperature Based Exhaust Temperature Curve to determine Exhaust Temperature',
            },
        )
    )
    temperature_based_exhaust_temperature_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'curve = a + b*AT + c*AT**2 AT = Ambient Delta T this curve is multiplied to the Part Load Based Exhaust Temperature Curve to determine Exhaust Temperature',
            },
        )
    )
    heat_recovery_lube_energy_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    coefficient_1_of_u_factor_times_area_curve: float | None = Field(
        default=None, json_schema_extra={'note': 'curve = C1 * Rated Power Output**C2'}
    )
    coefficient_2_of_u_factor_times_area_curve: float | None = Field(
        default=None,
        le=2.0,
        json_schema_extra={
            'note': 'curve = C1 * Rated Power Output**C2 typical value .9'
        },
    )
    maximum_exhaust_flow_per_unit_of_power_output: float | None = Field(
        default=None, json_schema_extra={'units': '(kg/s)/W'}
    )
    design_minimum_exhaust_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    design_air_inlet_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    fuel_higher_heating_value: float | None = Field(
        default=None, json_schema_extra={'units': 'kJ/kg'}
    )
    design_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'if non-zero, then inlet, outlet nodes must be entered.',
        },
    )
    heat_recovery_inlet_node_name: str | None = Field(default=None)
    heat_recovery_outlet_node_name: str | None = Field(default=None)
    fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='NaturalGas')
    heat_recovery_maximum_temperature: float | None = Field(
        default=80.0, ge=0.0, le=100.0, json_schema_extra={'units': 'C'}
    )
    outdoor_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={'note': 'Enter the name of an outdoor air node'},
    )


class GeneratorFuelCell(IDFBaseModel):
    """This generator model is the FC model from IEA Annex 42"""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell'
    name: str = Field(...)
    power_module_name: FCPMNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCPMNames'],
            'note': 'Enter the name of a Generator:FuelCell:PowerModule object.',
        },
    )
    air_supply_name: FCAirSupNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCAirSupNames'],
            'note': 'Enter the name of a Generator:FuelCell:AirSupply object.',
        },
    )
    fuel_supply_name: GenFuelSupNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['GenFuelSupNames'],
            'note': 'Enter the name of a Generator:FuelSupply object.',
        },
    )
    water_supply_name: FCWaterSupNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCWaterSupNames'],
            'note': 'Enter the name of a Generator:FuelCell:WaterSupply object.',
        },
    )
    auxiliary_heater_name: FCAuxHeatNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCAuxHeatNames'],
            'note': 'Enter the name of a Generator:FuelCell:AuxiliaryHeater object.',
        },
    )
    heat_exchanger_name: FCExhaustHXNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCExhaustHXNames'],
            'note': 'Enter the name of a Generator:FuelCell:ExhaustGasToWaterHeatExchanger object.',
        },
    )
    electrical_storage_name: FCStorageNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCStorageNames'],
            'note': 'Enter the name of a Generator:FuelCell:ElectricalStorage object.',
        },
    )
    inverter_name: FCInverterNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FCInverterNames'],
            'note': 'Enter the name of a Generator:FuelCell:Inverter object.',
        },
    )
    stack_cooler_name: FCStackCoolerNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FCStackCoolerNames'],
            'note': 'Enter the name of a Generator:FuelCell:StackCooler object. optional, used for PEMFC',
        },
    )


class GeneratorFuelCellAirSupply(IDFBaseModel):
    """Used to define details of the air supply subsystem for a fuel cell power
    generator."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:AirSupply'
    name: str = Field(...)
    air_inlet_node_name: str | None = Field(default=None)
    blower_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    blower_heat_loss_factor: float | None = Field(default=None, ge=0.0, le=1.0)
    air_supply_rate_calculation_mode: Literal[
        'AirRatiobyStoics',
        'QuadraticFunctionofElectricPower',
        'QuadraticFunctionofFuelRate',
    ] = Field(...)
    stoichiometric_ratio: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This is the excess air "stoics" the value entered is incremented by 1 in the model.'
        },
    )
    air_rate_function_of_electric_power_curve_name: UnivariateFunctionsRef | None = (
        Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    )
    air_rate_air_temperature_coefficient: float | None = Field(default=None)
    air_rate_function_of_fuel_rate_curve_name: UnivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    air_intake_heat_recovery_mode: Literal[
        'NoRecovery',
        'RecoverAuxiliaryBurner',
        'RecoverBurnerInverterStorage',
        'RecoverElectricalStorage',
        'RecoverInverter',
        'RecoverInverterandStorage',
    ] = Field(...)
    air_supply_constituent_mode: Literal['AmbientAir', 'UserDefinedConstituents'] = (
        Field(...)
    )
    number_of_userdefined_constituents: float | None = Field(default=None, le=5.0)
    constituent_fractions: (
        list[GeneratorFuelCellAirSupplyConstituentFractionsItem] | None
    ) = Field(default=None)


class GeneratorFuelCellAuxiliaryHeater(IDFBaseModel):
    """Intended for modeling an auxiliary heater for a fuel cell power generator,
    however this portion of the model is not yet available. The program still
    requires one of these objects be included even though the data are not yet
    used (so that internal data structures can be allocated)."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:AuxiliaryHeater'
    name: str = Field(...)
    excess_air_ratio: float | None = Field(default=None)
    ancillary_power_constant_term: float | None = Field(default=None)
    ancillary_power_linear_term: float | None = Field(default=None)
    skin_loss_u_factor_times_area_value: float | None = Field(
        default=None, json_schema_extra={'units': 'W/K'}
    )
    skin_loss_destination: Literal['AirInletForFuelCell', 'SurroundingZone'] | None = (
        Field(default=None)
    )
    zone_name_to_receive_skin_losses: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    heating_capacity_units: Literal['Watts', 'kmol/s'] | None = Field(default=None)
    maximum_heating_capacity_in_watts: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    minimum_heating_capacity_in_watts: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    maximum_heating_capacity_in_kmol_per_second: float | None = Field(
        default=None, json_schema_extra={'units': 'kmol/s'}
    )
    minimum_heating_capacity_in_kmol_per_second: float | None = Field(
        default=None, json_schema_extra={'units': 'kmol/s'}
    )


class GeneratorFuelCellElectricalStorage(IDFBaseModel):
    """Used to describe the electrical storage subsystem for a fuel cell power
    generator. The electrical storage model is a very simple \"constrained
    bucket\" model. Note that this electrical storage is embedded within the FC
    device."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:ElectricalStorage'
    name: str = Field(...)
    choice_of_model: Literal['SimpleEfficiencyWithConstraints'] | None = Field(
        default=None
    )
    nominal_charging_energetic_efficiency: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    nominal_discharging_energetic_efficiency: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    simple_maximum_capacity: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )
    simple_maximum_power_draw: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    simple_maximum_power_store: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    initial_charge_state: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )


class GeneratorFuelCellExhaustGasToWaterHeatExchanger(IDFBaseModel):
    """Describes the exhaust gas heat exchanger subsystem of a fuel cell power
    generator used to recovery thermal energy"""

    _idf_object_type: ClassVar[str] = (
        'Generator:FuelCell:ExhaustGasToWaterHeatExchanger'
    )
    name: str = Field(...)
    heat_recovery_water_inlet_node_name: str | None = Field(default=None)
    heat_recovery_water_outlet_node_name: str | None = Field(default=None)
    heat_recovery_water_maximum_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    exhaust_outlet_air_node_name: str | None = Field(default=None)
    heat_exchanger_calculation_method: (
        Literal[
            'Condensing', 'EmpiricalUAeff', 'FixedEffectiveness', 'FundementalUAeff'
        ]
        | None
    ) = Field(default=None)
    method_1_heat_exchanger_effectiveness: float | None = Field(default=None)
    method_2_parameter_hxs0: float | None = Field(default=None)
    method_2_parameter_hxs1: float | None = Field(default=None)
    method_2_parameter_hxs2: float | None = Field(default=None)
    method_2_parameter_hxs3: float | None = Field(default=None)
    method_2_parameter_hxs4: float | None = Field(default=None)
    method_3_h0gas_coefficient: float | None = Field(default=None)
    method_3_ndotgasref_coefficient: float | None = Field(default=None)
    method_3_n_coefficient: float | None = Field(default=None)
    method_3_gas_area: float | None = Field(
        default=None, json_schema_extra={'units': 'm2'}
    )
    method_3_h0_water_coefficient: float | None = Field(default=None)
    method_3_n_dot_water_ref_coefficient: float | None = Field(default=None)
    method_3_m_coefficient: float | None = Field(default=None)
    method_3_water_area: float | None = Field(
        default=None, json_schema_extra={'units': 'm2'}
    )
    method_3_f_adjustment_factor: float | None = Field(default=None)
    method_4_hxl1_coefficient: float | None = Field(default=None)
    method_4_hxl2_coefficient: float | None = Field(default=None)
    method_4_condensation_threshold: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )


class GeneratorFuelCellInverter(IDFBaseModel):
    """Used to describe the power condition unit subsystem of a fuel cell power
    generator. This object models an inverter system contained within a fuel
    cell system that converts from direct current (DC) to alternating current
    (AC)."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:Inverter'
    name: str = Field(...)
    inverter_efficiency_calculation_mode: Literal['Constant', 'Quadratic'] | None = (
        Field(default=None)
    )
    inverter_efficiency: float | None = Field(default=None, ge=0.0, le=1.0)
    efficiency_function_of_dc_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['UnivariateFunctions']}
    )


class GeneratorFuelCellPowerModule(IDFBaseModel):
    """Describe the core power module subsystem of a fuel cell power generator.
    This includes the fuel cell stack, fuel reformer, and whatever ancillary
    devices are included inside. If the model has multiple FC generators that
    are of the exact same type, then only one of these objects is needed and all
    the Generator:FuelCell objects can reference it."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:PowerModule'
    name: str = Field(...)
    efficiency_curve_mode: Literal['Annex42', 'Normalized'] | None = Field(default=None)
    efficiency_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    nominal_efficiency: float | None = Field(
        default=None, json_schema_extra={'note': 'This field is not used.'}
    )
    nominal_electrical_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W', 'note': 'This field is not used'}
    )
    number_of_stops_at_start_of_simulation: float | None = Field(
        default=None,
        json_schema_extra={'note': 'this is Nstops in SOFC model specification'},
    )
    cycling_performance_degradation_coefficient: float | None = Field(
        default=None,
        json_schema_extra={'note': 'this is D in SOFC model specification'},
    )
    number_of_run_hours_at_beginning_of_simulation: float | None = Field(
        default=None, json_schema_extra={'units': 'hr'}
    )
    accumulated_run_time_degradation_coefficient: float | None = Field(
        default=None,
        json_schema_extra={'note': 'this is L in SOFC model specification'},
    )
    run_time_degradation_initiation_time_threshold: float | None = Field(
        default=None, json_schema_extra={'units': 'hr'}
    )
    power_up_transient_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/s',
            'note': 'Maximum rate of change in electrical output [power increasing]',
        },
    )
    power_down_transient_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/s',
            'note': 'Maximum rate of change in electrical output [power decreasing] Enter positive value for rate of change',
        },
    )
    start_up_time: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 's',
            'note': 'Time from start up to normal operation',
        },
    )
    start_up_fuel: float | None = Field(
        default=None, json_schema_extra={'units': 'kmol'}
    )
    start_up_electricity_consumption: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )
    start_up_electricity_produced: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )
    shut_down_time: float | None = Field(default=None, json_schema_extra={'units': 's'})
    shut_down_fuel: float | None = Field(
        default=None, json_schema_extra={'units': 'kmol'}
    )
    shut_down_electricity_consumption: float | None = Field(
        default=None, json_schema_extra={'units': 'J'}
    )
    ancillary_electricity_constant_term: float | None = Field(default=None)
    ancillary_electricity_linear_term: float | None = Field(default=None)
    skin_loss_calculation_mode: (
        Literal[
            'ConstantRate', 'QuadraticFunctionOfFuelRate', 'UAForProcessGasTemperature'
        ]
        | None
    ) = Field(default=None)
    zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constant_skin_loss_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    skin_loss_u_factor_times_area_term: float | None = Field(
        default=None, json_schema_extra={'units': 'W/K'}
    )
    skin_loss_quadratic_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve is function of fuel use rate',
        },
    )
    dilution_air_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'kmol/s'}
    )
    stack_heat_loss_to_dilution_air: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    dilution_inlet_air_node_name: str | None = Field(default=None)
    dilution_outlet_air_node_name: str | None = Field(default=None)
    minimum_operating_point: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    maximum_operating_point: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )


class GeneratorFuelCellStackCooler(IDFBaseModel):
    """This object is optional and is used to define details needed to model the
    stack cooler on PEMFC."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:StackCooler'
    name: str = Field(...)
    heat_recovery_water_inlet_node_name: str | None = Field(default=None)
    heat_recovery_water_outlet_node_name: str | None = Field(default=None)
    nominal_stack_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    actual_stack_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    coefficient_r0: float | None = Field(default=None)
    coefficient_r1: float | None = Field(default=None)
    coefficient_r2: float | None = Field(default=None)
    coefficient_r3: float | None = Field(default=None)
    stack_coolant_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'kg/s'}
    )
    stack_cooler_u_factor_times_area_value: float | None = Field(
        default=None, json_schema_extra={'units': 'W/K'}
    )
    fs_cogen_adjustment_factor: float | None = Field(default=None)
    stack_cogeneration_exchanger_area: float | None = Field(
        default=None, json_schema_extra={'units': 'm2'}
    )
    stack_cogeneration_exchanger_nominal_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'kg/s'}
    )
    stack_cogeneration_exchanger_nominal_heat_transfer_coefficient: float | None = (
        Field(default=None, json_schema_extra={'units': 'W/m2-K'})
    )
    stack_cogeneration_exchanger_nominal_heat_transfer_coefficient_exponent: (
        float | None
    ) = Field(default=None)
    stack_cooler_pump_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stack_cooler_pump_heat_loss_fraction: float | None = Field(
        default=None, ge=0.0, le=1.0
    )
    stack_air_cooler_fan_coefficient_f0: float | None = Field(default=None)
    stack_air_cooler_fan_coefficient_f1: float | None = Field(default=None)
    stack_air_cooler_fan_coefficient_f2: float | None = Field(default=None)


class GeneratorFuelCellWaterSupply(IDFBaseModel):
    """Used to provide details of the water supply subsystem for a fuel cell power
    generator. This water is used for steam reforming of the fuel and is not the
    same as the water used for thermal heat recovery."""

    _idf_object_type: ClassVar[str] = 'Generator:FuelCell:WaterSupply'
    name: str = Field(...)
    reformer_water_flow_rate_function_of_fuel_rate_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    reformer_water_pump_power_function_of_fuel_rate_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    pump_heat_loss_factor: float | None = Field(default=None)
    water_temperature_modeling_mode: (
        Literal[
            'MainsWaterTemperature',
            'TemperatureFromAirNode',
            'TemperatureFromSchedule',
            'TemperatureFromWaterNode',
        ]
        | None
    ) = Field(default=None)
    water_temperature_reference_node_name: str | None = Field(default=None)
    water_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )


class GeneratorFuelSupply(IDFBaseModel):
    """Used only with Generator:FuelCell and Generator:MicroCHP"""

    _idf_object_type: ClassVar[str] = 'Generator:FuelSupply'
    name: str = Field(...)
    fuel_temperature_modeling_mode: (
        Literal['Scheduled', 'TemperatureFromAirNode'] | None
    ) = Field(default=None)
    fuel_temperature_reference_node_name: str | None = Field(default=None)
    fuel_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    compressor_power_multiplier_function_of_fuel_rate_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    compressor_heat_loss_factor: float | None = Field(default=None, ge=0.0, le=1.0)
    fuel_type: Literal['GaseousConstituents', 'LiquidGeneric'] | None = Field(
        default=None
    )
    liquid_generic_fuel_lower_heating_value: float | None = Field(
        default=None, json_schema_extra={'units': 'kJ/kg'}
    )
    liquid_generic_fuel_higher_heating_value: float | None = Field(
        default=None, json_schema_extra={'units': 'kJ/kg'}
    )
    liquid_generic_fuel_molecular_weight: float | None = Field(
        default=None, json_schema_extra={'units': 'g/mol'}
    )
    liquid_generic_fuel_co2_emission_factor: float | None = Field(default=None)
    number_of_constituents_in_gaseous_constituent_fuel_supply: float | None = Field(
        default=None, ge=0.0, le=12.0
    )
    constituent_1_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_1_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_2_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_2_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_3_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_3_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_4_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_4_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_5_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_5_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_6_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_6_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_7_name: (
        Literal[
            'Butane',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Pentane',
            'Propane',
        ]
        | None
    ) = Field(default=None)
    constituent_7_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_8_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_8_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_9_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_9_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_10_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_10_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_11_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_11_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    constituent_12_name: (
        Literal[
            'Argon',
            'Butane',
            'CarbonDioxide',
            'Ethane',
            'Ethanol',
            'Hexane',
            'Hydrogen',
            'Methane',
            'Methanol',
            'Nitrogen',
            'Oxygen',
            'Pentane',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    constituent_12_molar_fraction: float | None = Field(default=None, ge=0.0, le=1.0)


class GeneratorInternalCombustionEngine(IDFBaseModel):
    """This generator model is the empirical model from the Building Loads and
    System Thermodynamics (BLAST) program. Engine performance curves are
    generated by fitting catalog data to second order polynomial equations.
    Three sets of coefficients are required."""

    _idf_object_type: ClassVar[str] = 'Generator:InternalCombustionEngine'
    name: str = Field(...)
    rated_power_output: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    electric_circuit_node_name: str | None = Field(default=None)
    minimum_part_load_ratio: float | None = Field(default=None, ge=0.0, le=1.0)
    maximum_part_load_ratio: float | None = Field(default=None, le=1.0, gt=0.0)
    optimum_part_load_ratio: float | None = Field(default=None)
    shaft_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    jacket_heat_recovery_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    lube_heat_recovery_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    total_exhaust_energy_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    exhaust_temperature_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'curve = a + b*PLR + c*PLR**2 PLR = Ratio of Generator Load to Rated Power Output',
        },
    )
    coefficient_1_of_u_factor_times_area_curve: float | None = Field(
        default=None,
        json_schema_extra={'note': 'curve = C1 * Generator Rated Power Output**C2'},
    )
    coefficient_2_of_u_factor_times_area_curve: float | None = Field(
        default=None,
        le=2.0,
        json_schema_extra={
            'note': 'curve = C1 * Generator Rated Power Output**C2 typical value .9'
        },
    )
    maximum_exhaust_flow_per_unit_of_power_output: float | None = Field(
        default=None, json_schema_extra={'units': '(kg/s)/W'}
    )
    design_minimum_exhaust_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    fuel_higher_heating_value: float | None = Field(
        default=None, json_schema_extra={'units': 'kJ/kg'}
    )
    design_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'if non-zero, then inlet, outlet nodes must be entered.',
        },
    )
    heat_recovery_inlet_node_name: str | None = Field(default=None)
    heat_recovery_outlet_node_name: str | None = Field(default=None)
    fuel_type: (
        Literal[
            '',
            'Diesel',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='Diesel')
    heat_recovery_maximum_temperature: float | None = Field(
        default=80.0, ge=0.0, le=100.0, json_schema_extra={'units': 'C'}
    )


class GeneratorMicroCHP(IDFBaseModel):
    """Small-scale combined heat and power (micro CHP) electric generator using the
    model developed by IEA/ECBCS Annex 42 see www.cogen-sim.net. The model was
    developed for both internal combustion and Stirling cycle engines, but might
    be used for other types of residential CHP devices."""

    _idf_object_type: ClassVar[str] = 'Generator:MicroCHP'
    name: str | None = Field(default=None)
    performance_parameters_name: MicroCHPParametersNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['MicroCHPParametersNames'],
            'note': 'Enter the name of a Generator:MicroCHP:NonNormalizedParameters object.',
        },
    )
    zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    cooling_water_inlet_node_name: str | None = Field(default=None)
    cooling_water_outlet_node_name: str | None = Field(default=None)
    air_inlet_node_name: str | None = Field(default=None)
    air_outlet_node_name: str | None = Field(default=None)
    generator_fuel_supply_name: GenFuelSupNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['GenFuelSupNames'],
            'note': 'Enter the name of a Generator:FuelSupply object.',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )


class GeneratorMicroCHPNonNormalizedParameters(IDFBaseModel):
    """This object is referenced by a Generator:MicroCHP object and provides the
    non-normalized parameters for the MicroCHP generator model."""

    _idf_object_type: ClassVar[str] = 'Generator:MicroCHP:NonNormalizedParameters'
    name: str | None = Field(default=None)
    maximum_electric_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    minimum_electric_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    minimum_cooling_water_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'kg/s'}
    )
    maximum_cooling_water_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    electrical_efficiency_curve_name: TrivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'TriQuadratic',
        },
    )
    thermal_efficiency_curve_name: TrivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'TriQuadratic',
        },
    )
    cooling_water_flow_rate_mode: Literal['InternalControl', 'PlantControl'] | None = (
        Field(default=None)
    )
    cooling_water_flow_rate_curve_name: BivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['BivariateFunctions']}
    )
    air_flow_rate_curve_name: UnivariateFunctionsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    maximum_net_electrical_power_rate_of_change: float | None = Field(
        default=None, json_schema_extra={'units': 'W/s'}
    )
    maximum_fuel_flow_rate_of_change: float | None = Field(
        default=None, json_schema_extra={'units': 'kg/s2'}
    )
    heat_exchanger_u_factor_times_area_value: float | None = Field(
        default=None, json_schema_extra={'units': 'W/K'}
    )
    skin_loss_u_factor_times_area_value: float | None = Field(
        default=None, json_schema_extra={'units': 'W/K'}
    )
    skin_loss_radiative_fraction: float | None = Field(default=None)
    aggregated_thermal_mass_of_energy_conversion_portion_of_generator: float | None = (
        Field(default=None, gt=0.0, json_schema_extra={'units': 'W/K'})
    )
    aggregated_thermal_mass_of_heat_recovery_portion_of_generator: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/K'}
    )
    standby_power: float | None = Field(default=None, json_schema_extra={'units': 'W'})
    warm_up_mode: Literal['NominalEngineTemperature', 'TimeDelay'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Stirling engines use Nominal Engine Temperature Internal combustion engines use Time Delay'
        },
    )
    warm_up_fuel_flow_rate_coefficient: float | None = Field(default=None)
    nominal_engine_operating_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    warm_up_power_coefficient: float | None = Field(default=None)
    warm_up_fuel_flow_rate_limit_ratio: float | None = Field(default=None)
    warm_up_delay_time: float | None = Field(
        default=None, json_schema_extra={'units': 's'}
    )
    cool_down_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    cool_down_delay_time: float | None = Field(
        default=None, json_schema_extra={'units': 's'}
    )
    restart_mode: Literal['MandatoryCoolDown', 'OptionalCoolDown'] | None = Field(
        default=None
    )


class GeneratorMicroTurbine(IDFBaseModel):
    """MicroTurbine generators are small combustion turbines (e.g., 25kW to 500kW).
    The model calculates electrical power output, fuel use, standby and
    ancillary power. Energy recovery from exhaust air can be used to heat water."""

    _idf_object_type: ClassVar[str] = 'Generator:MicroTurbine'
    name: str = Field(...)
    reference_electrical_power_output: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W'}
    )
    minimum_full_load_electrical_power_output: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_full_load_electrical_power_output: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'If left blank, Maximum Full Load Electrical Power Output will be set equal to the Reference Electrical Power Output.',
        },
    )
    reference_electrical_efficiency_using_lower_heating_value: float = Field(
        ...,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Electric power output divided by fuel energy input (LHV basis) at reference conditions.'
        },
    )
    reference_combustion_air_inlet_temperature: float | None = Field(
        default=15.0, json_schema_extra={'units': 'C'}
    )
    reference_combustion_air_inlet_humidity_ratio: float | None = Field(
        default=0.00638, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    reference_elevation: float | None = Field(
        default=0.0, ge=-300.0, json_schema_extra={'units': 'm'}
    )
    electrical_power_function_of_temperature_and_elevation_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*T + c*T**2 + d*Elev + e*Elev**2 + f*T*Elev T = combustion air inlet temperature (C) Elev = elevation (m)',
        },
    )
    electrical_efficiency_function_of_temperature_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*T + c*T**2 Cubic curve = a + b*T + c*T**2 + d*T**3 T = combustion air inlet temperature (C)',
        },
    )
    electrical_efficiency_function_of_part_load_ratio_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*PLR + c*PLR**2 Cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = ratio of Generator Load to steady state Electrical Power Output at current operating conditions',
        },
    )
    fuel_type: (
        Literal[
            '',
            'Coal',
            'Diesel',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='NaturalGas')
    fuel_higher_heating_value: float | None = Field(
        default=50000.0, gt=0.0, json_schema_extra={'units': 'kJ/kg'}
    )
    fuel_lower_heating_value: float | None = Field(
        default=45450.0, gt=0.0, json_schema_extra={'units': 'kJ/kg'}
    )
    standby_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power consumed when the generator is available but not being called by the Electric Load Center.',
        },
    )
    ancillary_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Electric power consumed by ancillary equipment (e.g., external fuel pressurization pump). Set to zero if Reference Electrical Power Output is the 'net' value (ancillary power already deducted). Inp...",
        },
    )
    ancillary_power_function_of_fuel_input_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'Quadratic curve = a + b*mdot + c*mdot**2 mdot = fuel mass flow rate (kg/s) If left blank, model assumes ancillary power defined in previous field is constant whenever the generator is operating.',
            },
        )
    )
    heat_recovery_water_inlet_node_name: str | None = Field(default=None)
    heat_recovery_water_outlet_node_name: str | None = Field(default=None)
    reference_thermal_efficiency_using_lower_heat_value: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Reference thermal efficiency (heat recovery to water) based on the Lower Heating Value (LHV) of the fuel.'
        },
    )
    reference_inlet_water_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    heat_recovery_water_flow_operating_mode: (
        Literal['', 'InternalControl', 'PlantControl'] | None
    ) = Field(
        default='PlantControl',
        json_schema_extra={
            'note': 'PlantControl means the heat recovery water flow rate is determined by the plant, but the user needs to supply a heat recovery water flow rate. InternalControl means the heat recovery water flow rat...'
        },
    )
    reference_heat_recovery_water_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm3/s'}
    )
    heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*T + c*T**2 + d*Pnet + e*Pnet + f*T*Pnet T = heat recovery inlet water temperature Pnet = net power output = electric power output - ancillary power If left blank, model assumes the he...',
        },
    )
    thermal_efficiency_function_of_temperature_and_elevation_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Bicubic curve = a + b*T + c*T**2 + d*Elev + e*Elev**2 + f*T*Elev + g*T**3 + h*Elev**3 + i*T**2*Elev + j*T*Elev**2 Biquadratic curve = a + b*T + c*T**2 + d*Elev + e*Elev**2 + f*T*Elev T = combustion...',
        },
    )
    heat_recovery_rate_function_of_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*PLR + c*PLR**2 Cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = ratio of Generator Load to steady state Electrical Power Output at current operating conditions If field i...',
        },
    )
    heat_recovery_rate_function_of_inlet_water_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*T + c*T**2 T = inlet water temperature (C) If field is left blank, model assumes this modifier equals 1 for entire simulation.',
        },
    )
    heat_recovery_rate_function_of_water_flow_rate_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*Flow + c*Flow**2 Flow = flow rate of water through the heat exchanger (m3/s) If field is left blank, model assumes this modifier equals 1 for entire simulation.',
        },
    )
    minimum_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    maximum_heat_recovery_water_flow_rate: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    maximum_heat_recovery_water_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    combustion_air_inlet_node_name: str | None = Field(
        default=None, json_schema_extra={'note': 'Must be an outdoor air node.'}
    )
    combustion_air_outlet_node_name: str | None = Field(default=None)
    reference_exhaust_air_mass_flow_rate: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'kg/s'}
    )
    exhaust_air_flow_rate_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*T + c*T**2 Cubic curve = a + b*T + c*T**2 + d*T**3 T = combustion air inlet temperature (C) If field is left blank, model assumes this modifier equals 1 for entire simulation.',
        },
    )
    exhaust_air_flow_rate_function_of_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*PLR + c*PLR**2 Cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = ratio of Generator Load to steady state Electrical Power Output at current operating conditions. If field ...',
        },
    )
    nominal_exhaust_air_outlet_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Exhaust air outlet temperature at reference conditions.'
        },
    )
    exhaust_air_temperature_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*T + c*T**2 Cubic curve = a + b*T + c*T**2 + d*T**3 T = combustion air inlet temperature (C) If field is left blank, model assumes this modifier equals 1 for entire simulation.',
        },
    )
    exhaust_air_temperature_function_of_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Quadratic curve = a + b*PLR + c*PLR**2 Cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = ratio of Generator Load to steady state Electrical Power Output at current operating conditions. If field ...',
        },
    )


class GeneratorPVWatts(IDFBaseModel):
    """Describes a simple set of inputs for an array of photovoltaic (PV) modules
    as described in the PVWatts software. A series of different PVWatts arrays
    can be connected to a single electric load center (preferably through an
    ElectricLoadCenter:Inverter:PVWatts). Array tilt and azimuth can be either
    specified on this object or taken from a referenced building surface or
    shading surface. If a surface is specified, the array participates normally
    in all shading calculations."""

    _idf_object_type: ClassVar[str] = 'Generator:PVWatts'
    name: str = Field(...)
    pvwatts_version: Literal['5'] | None = Field(default=None)
    dc_system_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Nameplate rated DC system capacity in watts',
        },
    )
    module_type: Literal['Premium', 'Standard', 'ThinFilm'] = Field(...)
    array_type: Literal[
        'FixedOpenRack', 'FixedRoofMounted', 'OneAxis', 'OneAxisBacktracking', 'TwoAxis'
    ] = Field(...)
    system_losses: float | None = Field(default=0.14, ge=0.0, le=1.0)
    array_geometry_type: Literal['', 'Surface', 'TiltAzimuth'] | None = Field(
        default='TiltAzimuth',
        json_schema_extra={
            'note': 'TiltAzimuth - The tilt and azimuth angles are specified in the next two fields. An unshaded array is assumed. Surface - The array geometry (tilt and azimuth) as well as shading is determined from s...'
        },
    )
    tilt_angle: float | None = Field(
        default=20.0,
        ge=0.0,
        le=90.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'The tilt angle is the angle from horizontal of the photovoltaic modules in the array.',
        },
    )
    azimuth_angle: float | None = Field(
        default=180.0,
        ge=0.0,
        lt=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'For a fixed array, the azimuth angle is the angle clockwise from true north describing the direction that the array faces. For an array with one-axis tracking, the azimuth angle is the angle clockw...',
        },
    )
    surface_name: AllShadingAndHTSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )
    ground_coverage_ratio: float | None = Field(
        default=0.4,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applies only to arrays with one-axis tracking and is the ratio of module surface area to area of the ground or roof occupied by the array.'
        },
    )


class GeneratorPhotovoltaic(IDFBaseModel):
    """Describes an array of photovoltaic (PV) modules. A series of different PV
    arrays can be connected to a single electric load center (and inverter) by
    listing them all in an ElectricLoadCenter:Generator object. PV performance
    is taken from the referenced PhotovoltaicPerformance:* object. Array tilt,
    azimuth, and gross area are taken from the referenced building surface or
    shading surface. The array surface participates normally in all shading
    calculations."""

    _idf_object_type: ClassVar[str] = 'Generator:Photovoltaic'
    name: str = Field(...)
    surface_name: AllShadingAndHTSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AllShadingAndHTSurfNames']}
    )
    photovoltaic_performance_object_type: (
        Literal[
            'PhotovoltaicPerformance:EquivalentOne-Diode',
            'PhotovoltaicPerformance:Sandia',
            'PhotovoltaicPerformance:Simple',
        ]
        | None
    ) = Field(default=None)
    module_performance_name: PVModulesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PVModules'],
            'note': 'PV array modeling details',
        },
    )
    heat_transfer_integration_mode: (
        Literal[
            '',
            'Decoupled',
            'DecoupledUllebergDynamic',
            'IntegratedExteriorVentedCavity',
            'IntegratedSurfaceOutsideFace',
            'IntegratedTranspiredCollector',
            'PhotovoltaicThermalSolarCollector',
        ]
        | None
    ) = Field(default='Decoupled')
    number_of_series_strings_in_parallel: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'number of series-wired strings of PV modules that are in parallel',
        },
    )
    number_of_modules_in_series: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Number of PV modules wired in series for each string.',
        },
    )


class GeneratorWindTurbine(IDFBaseModel):
    """Wind turbine generator."""

    _idf_object_type: ClassVar[str] = 'Generator:WindTurbine'
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rotor_type: (
        Literal['', 'HorizontalAxisWindTurbine', 'VerticalAxisWindTurbine'] | None
    ) = Field(
        default='HorizontalAxisWindTurbine',
        json_schema_extra={
            'note': 'allowed values are: Horizontal Axis Wind Turbine or Vertical Axis Wind Turbine'
        },
    )
    power_control: (
        Literal[
            '',
            'FixedSpeedFixedPitch',
            'FixedSpeedVariablePitch',
            'VariableSpeedFixedPitch',
            'VariableSpeedVariablePitch',
        ]
        | None
    ) = Field(
        default='VariableSpeedVariablePitch',
        json_schema_extra={
            'note': 'Constant power output is obtained in the last three control types when the wind speed exceeds the rated wind speed. allowed values are: Fixed Speed Fixed Pitch, Fixed Speed Variable Pitch, Variable...'
        },
    )
    rated_rotor_speed: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'rev/min'}
    )
    rotor_diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field is the diameter of the perpendicular circle of the Vertical Axis Wind Turbine system from the upright pole on the ground.',
        },
    )
    overall_height: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field is the height of the hub for the Horizontal Axis Wind Turbines and of the pole for the Vertical Axis Wind Turbines.',
        },
    )
    number_of_blades: float | None = Field(default=3.0, ge=2.0)
    rated_power: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'This field is the nominal power at the rated wind speed. Users should input maximum power in case of Fixed Speed Fixed Pitch control type.',
        },
    )
    rated_wind_speed: float = Field(..., gt=0.0, json_schema_extra={'units': 'm/s'})
    cut_in_wind_speed: float = Field(..., gt=0.0, json_schema_extra={'units': 'm/s'})
    cut_out_wind_speed: float = Field(..., gt=0.0, json_schema_extra={'units': 'm/s'})
    fraction_system_efficiency: float | None = Field(default=0.835, le=1.0, gt=0.0)
    maximum_tip_speed_ratio: float | None = Field(default=5.0, le=12.0, gt=0.0)
    maximum_power_coefficient: float | None = Field(
        default=0.25,
        le=0.59,
        gt=0.0,
        json_schema_extra={
            'note': 'This field should be input if the rotor type is Horizontal Axis Wind Turbine'
        },
    )
    annual_local_average_wind_speed: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm/s'}
    )
    height_for_local_average_wind_speed: float | None = Field(
        default=50.0, gt=0.0, json_schema_extra={'units': 'm'}
    )
    blade_chord_area: float | None = Field(
        default=None, json_schema_extra={'units': 'm2'}
    )
    blade_drag_coefficient: float | None = Field(
        default=0.9,
        json_schema_extra={
            'note': 'This field is only for Vertical Axis Wind Turbine.. The user must input this field if the rotor type is Vertical Axis Wind Turbine.'
        },
    )
    blade_lift_coefficient: float | None = Field(
        default=0.05,
        json_schema_extra={
            'note': 'This field is only for Vertical Axis Wind Turbine.. The user must input this field if the rotor type is Vertical Axis Wind Turbine.'
        },
    )
    power_coefficient_c1: float | None = Field(
        default=0.5176,
        gt=0.0,
        json_schema_extra={
            'note': 'This field is only available for Horizontal Axis Wind Turbine. The user should input all six parameters so that the analytic approximation is assumed. The simple approximation will be assumed, if a...'
        },
    )
    power_coefficient_c2: float | None = Field(default=116.0, gt=0.0)
    power_coefficient_c3: float | None = Field(default=0.4, gt=0.0)
    power_coefficient_c4: float | None = Field(default=0.0, ge=0.0)
    power_coefficient_c5: float | None = Field(default=5.0, gt=0.0)
    power_coefficient_c6: float | None = Field(default=21.0, gt=0.0)


class PhotovoltaicPerformanceEquivalentOneDiode(IDFBaseModel):
    """Describes the performance characteristics of Photovoltaic (PV) modules to be
    modeled using an equivalent one-diode circuit. This model is also known as
    the 4- or 5-parameter TRNSYS model for photovoltaics."""

    _idf_object_type: ClassVar[str] = 'PhotovoltaicPerformance:EquivalentOne-Diode'
    name: str | None = Field(default=None)
    cell_type: Literal['AmorphousSilicon', 'CrystallineSilicon'] | None = Field(
        default=None
    )
    number_of_cells_in_series: int | None = Field(
        default=36, ge=0, json_schema_extra={'units': 'dimensionless'}
    )
    active_area: float | None = Field(
        default=0.89,
        ge=0.1,
        json_schema_extra={
            'units': 'm2',
            'note': 'The total power output of the array is determined by the number of modules (see above). The Active Area is only used to calculate the PV Array Efficiency output variable.',
        },
    )
    transmittance_absorptance_product: float | None = Field(
        default=0.95, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    semiconductor_bandgap: float | None = Field(
        default=1.12, ge=0.0, json_schema_extra={'units': 'eV'}
    )
    shunt_resistance: float | None = Field(
        default=1000000.0, ge=0.0, json_schema_extra={'units': 'ohms'}
    )
    short_circuit_current: float | None = Field(
        default=6.5, ge=0.0, json_schema_extra={'units': 'A'}
    )
    open_circuit_voltage: float | None = Field(
        default=21.6, ge=0.0, json_schema_extra={'units': 'V'}
    )
    reference_temperature: float | None = Field(
        default=25.0, ge=0.0, json_schema_extra={'units': 'C'}
    )
    reference_insolation: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    module_current_at_maximum_power: float | None = Field(
        default=5.9,
        ge=0.0,
        json_schema_extra={
            'units': 'A',
            'note': 'Single module current at the maximum power point and reference conditions. Module Current, Module Voltage, Number of Modules in Parallel and Number of Modules in Series determine the maximum power ...',
        },
    )
    module_voltage_at_maximum_power: float | None = Field(
        default=17.0,
        ge=0.0,
        json_schema_extra={
            'units': 'V',
            'note': 'Single module voltage at the maximum power point and reference conditions. Module Current, Module Voltage, Number of Modules in Parallel and Number of Modules in Series determine the maximum power ...',
        },
    )
    temperature_coefficient_of_short_circuit_current: float | None = Field(
        default=0.02, json_schema_extra={'units': 'A/K'}
    )
    temperature_coefficient_of_open_circuit_voltage: float | None = Field(
        default=-0.079, json_schema_extra={'units': 'V/K'}
    )
    nominal_operating_cell_temperature_test_ambient_temperature: float | None = Field(
        default=20.0, ge=0.0, json_schema_extra={'units': 'C'}
    )
    nominal_operating_cell_temperature_test_cell_temperature: float | None = Field(
        default=40.0, ge=0.0, json_schema_extra={'units': 'C'}
    )
    nominal_operating_cell_temperature_test_insolation: float | None = Field(
        default=800.0, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    module_heat_loss_coefficient: float | None = Field(
        default=30.0, ge=0.0, json_schema_extra={'units': 'W/m2-K'}
    )
    total_heat_capacity: float | None = Field(
        default=50000.0, ge=0.0, json_schema_extra={'units': 'J/m2-K'}
    )


class PhotovoltaicPerformanceSandia(IDFBaseModel):
    """Describes performance input data needed for specific makes and models of
    production PV panels using the empirical coefficients assembled by Sandia
    National Laboratory."""

    _idf_object_type: ClassVar[str] = 'PhotovoltaicPerformance:Sandia'
    name: str | None = Field(default=None)
    active_area: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={'units': 'm2', 'note': '(m2, single module)'},
    )
    number_of_cells_in_series: int | None = Field(
        default=1, ge=1, json_schema_extra={'units': 'dimensionless'}
    )
    number_of_cells_in_parallel: int | None = Field(
        default=1, ge=1, json_schema_extra={'units': 'dimensionless'}
    )
    short_circuit_current: float | None = Field(
        default=None, json_schema_extra={'units': 'A', 'note': '(Amps)'}
    )
    open_circuit_voltage: float | None = Field(
        default=None, json_schema_extra={'units': 'V', 'note': '(Volts)'}
    )
    current_at_maximum_power_point: float | None = Field(
        default=None, json_schema_extra={'units': 'A', 'note': '(Amps)'}
    )
    voltage_at_maximum_power_point: float | None = Field(
        default=None, json_schema_extra={'units': 'V', 'note': '(Volts)'}
    )
    sandia_database_parameter_aisc: float | None = Field(
        default=None, json_schema_extra={'units': '1/K', 'note': '(1/degC)'}
    )
    sandia_database_parameter_aimp: float | None = Field(
        default=None, json_schema_extra={'units': '1/K', 'note': '(1/degC)'}
    )
    sandia_database_parameter_c0: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c1: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_bvoc0: float | None = Field(
        default=None, json_schema_extra={'units': 'V/K', 'note': '(Volts/degC)'}
    )
    sandia_database_parameter_mbvoc: float | None = Field(
        default=None, json_schema_extra={'units': 'V/K', 'note': '(Volts/degC)'}
    )
    sandia_database_parameter_bvmp0: float | None = Field(
        default=None, json_schema_extra={'units': 'V/K', 'note': '(Volts/degC)'}
    )
    sandia_database_parameter_mbvmp: float | None = Field(
        default=None, json_schema_extra={'units': 'V/K', 'note': '(Volts/degC)'}
    )
    diode_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c2: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c3: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a0: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a1: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a2: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a3: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a4: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b0: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b1: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b2: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b3: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b4: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b5: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_delta_tc: float | None = Field(
        default=None,
        validation_alias='sandia_database_parameter_delta_tc_',
        json_schema_extra={'units': 'deltaC', 'note': '(deg C)'},
    )
    sandia_database_parameter_fd: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_a: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_b: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c4: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c5: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_ix0: float | None = Field(
        default=None, json_schema_extra={'note': '(Amps)'}
    )
    sandia_database_parameter_ixx0: float | None = Field(
        default=None, json_schema_extra={'note': '(Amps)'}
    )
    sandia_database_parameter_c6: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    sandia_database_parameter_c7: float | None = Field(
        default=None,
        json_schema_extra={'units': 'dimensionless', 'note': '(non-dimensional)'},
    )


class PhotovoltaicPerformanceSimple(IDFBaseModel):
    """Describes a simple model of photovoltaics that may be useful for early phase
    design analysis. In this model the user has direct access to the efficiency
    with which surfaces convert incident solar radiation to electricity and need
    not specify arrays of specific modules."""

    _idf_object_type: ClassVar[str] = 'PhotovoltaicPerformance:Simple'
    name: str | None = Field(default=None)
    fraction_of_surface_area_with_active_solar_cells: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    conversion_efficiency_input_mode: Literal['Fixed', 'Scheduled'] | None = Field(
        default=None
    )
    value_for_cell_efficiency_if_fixed: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Efficiency = (power generated [W])/(incident solar[W])'
        },
    )
    efficiency_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
