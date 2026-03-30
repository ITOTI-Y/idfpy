"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Coils
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    CoilCoolingDXRef,
    CoilPerformanceDXRef,
    CoolingCoilsDXRef,
    CoolingCoilsDXSingleSpeedRef,
    CoolingCoilsDXVariableSpeedRef,
    CoolingCoilsWaterNoHXRef,
    CoolingCoilsWaterRef,
    DesuperHeatingCoilSourcesRef,
    DesuperHeatingWaterOnlySourcesRef,
    DXCoolingOperatingModeNamesRef,
    DXCoolingPerformanceNamesRef,
    DXCoolingSpeedNamesRef,
    FluidAndGlycolNamesRef,
    FluidNamesRef,
    HeatingCoilsDXSingleSpeedRef,
    HeatingCoilsDXVariableSpeedRef,
    HeatPumpWaterHeaterDXCoilsVariableSpeedRef,
    HXAirToAirNamesRef,
    QuadvariateFunctionsRef,
    QuintvariateFunctionsRef,
    ScheduleNamesRef,
    TrivariateFunctionsRef,
    UnivariateFunctionsRef,
    WaterHeaterMixedNamesRef,
    WaterHeaterStratifiedNamesRef,
    WaterStorageTankNamesRef,
    ZoneNamesRef,
)


class CoilCoolingDX(IDFBaseModel):
    """New general DX cooling coil supporting on or more speeds and one or or
    operating modes. Includes DX evaporator coil, compressor, and condenser.
    Object is currently only supported by the AIRLOOPHVAC:UNITARYSYSTEM object.
    Remaining Coil:Cooling:DX* objects will be deprecated at a future date,
    after which, this object will replace all other Coil:Cooling:DX* objects."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    evaporator_inlet_node_name: str = Field(...)
    evaporator_outlet_node_name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule value > 0 means the coil is available. If this field is blank, the coil is always available.',
        },
    )
    condenser_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (condenser) of a DX system or heat pump is to be placed. This is an optional input field specified only when...',
        },
    )
    condenser_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of an air node in the simulation. This may be an explicitly defined outdoor air node, or it may be a separate air node.'
        },
    )
    condenser_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This is the name of an air node in the simulation.'
        },
    )
    performance_object_name: DXCoolingPerformanceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['DXCoolingPerformanceNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    evaporative_condenser_supply_water_storage_tank_name: (
        WaterStorageTankNamesRef | None
    ) = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def condenser_zone(self) -> IDFBaseModel | None:
        v = self.condenser_zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def performance_object(self) -> IDFBaseModel | None:
        v = self.performance_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingPerformanceNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def evaporative_condenser_supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.evaporative_condenser_supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingDXCurveFitOperatingMode(IDFBaseModel):
    """DX cooling coil performance for a single operating mode which may have one
    or more speeds."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:CurveFit:OperatingMode'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    rated_gross_total_cooling_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Total (sensible+latent) cooling capacity not accounting for the effect of supply air fan heat. Rating point: air entering the evaporator coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering th...',
        },
    )
    rated_evaporator_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, Rated SHR and Rated COP. Should be between 0.00004027 m3/s and 0.00006041 m3/s per watt of rated total cooling capacity.',
        },
    )
    rated_condenser_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use.',
        },
    )
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    apply_latent_degradation_to_speeds_greater_than_1: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    nominal_evaporative_condenser_pump_power: float | Literal['', 'Autosize'] | None = (
        Field(
            default=0.0,
            json_schema_extra={
                'units': 'W',
                'note': "Rated power consumed by the evaporative condenser's water pump",
            },
        )
    )
    nominal_speed_number: int | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Must be lower than or equal to the highest speed number. If blank, defaults to the highest speed number used.'
        },
    )
    speed_1_name: DXCoolingSpeedNamesRef = Field(
        ..., json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_2_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_3_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_4_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_5_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_6_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_7_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_8_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_9_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )
    speed_10_name: DXCoolingSpeedNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['DXCoolingSpeedNames']}
    )

    @property
    def speed_1(self) -> IDFBaseModel | None:
        v = self.speed_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_2(self) -> IDFBaseModel | None:
        v = self.speed_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_3(self) -> IDFBaseModel | None:
        v = self.speed_3_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_4(self) -> IDFBaseModel | None:
        v = self.speed_4_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_5(self) -> IDFBaseModel | None:
        v = self.speed_5_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_6(self) -> IDFBaseModel | None:
        v = self.speed_6_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_7(self) -> IDFBaseModel | None:
        v = self.speed_7_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_8(self) -> IDFBaseModel | None:
        v = self.speed_8_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_9(self) -> IDFBaseModel | None:
        v = self.speed_9_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])

    @property
    def speed_10(self) -> IDFBaseModel | None:
        v = self.speed_10_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingSpeedNames'])


class CoilCoolingDXCurveFitPerformance(IDFBaseModel):
    """DX cooling coil performance specification referencing one or more operating
    modes. Mode 1 is always the base design operating mode. Additional modes are
    optional states such as subcool reheat for humidity control."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:CurveFit:Performance'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    unit_internal_static_air_pressure: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter pressure drop for the unit containing the coil. This value is only used to calculate Energy Efficiency Ratio (EER), Integrated Energy Efficiency Ratio (IEER), and the Standard Rating (Net) Co...',
        },
    )
    capacity_control_method: Literal['', 'Continuous', 'Discrete'] | None = Field(
        default='Discrete'
    )
    evaporative_condenser_basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    evaporative_condenser_basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    evaporative_condenser_basin_heater_operating_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    compressor_fuel_type: (
        Literal[
            '',
            'Diesel',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='Electricity')
    base_operating_mode: DXCoolingOperatingModeNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['DXCoolingOperatingModeNames'],
            'note': 'Operating Mode 1 is always used as the base design operating mode.',
        },
    )
    alternative_operating_mode_1: DXCoolingOperatingModeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DXCoolingOperatingModeNames'],
            'note': 'The alternative operating mode is used for enhanced dehumidification. If this is blank, the coil will always operate in the base operating mode. If an alternate mode is defined here, the coil will ...',
        },
    )
    alternative_operating_mode_2: DXCoolingOperatingModeNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DXCoolingOperatingModeNames'],
            'note': 'The alternative operating mode is used for enhanced dehumidification. If this is blank, the coil will always operate in the base operating mode or Alternative Mode 1. If both Alternative Operating ...',
        },
    )

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def evaporative_condenser_basin_heater_operating_schedule(
        self,
    ) -> IDFBaseModel | None:
        v = self.evaporative_condenser_basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def base_operating_mode_ref(self) -> IDFBaseModel | None:
        v = self.base_operating_mode
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingOperatingModeNames'])

    @property
    def alternative_operating_mode_1_ref(self) -> IDFBaseModel | None:
        v = self.alternative_operating_mode_1
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingOperatingModeNames'])

    @property
    def alternative_operating_mode_2_ref(self) -> IDFBaseModel | None:
        v = self.alternative_operating_mode_2
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DXCoolingOperatingModeNames'])


class CoilCoolingDXCurveFitSpeed(IDFBaseModel):
    """DX cooling coil performance for a single speed within a single operating
    mode."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:CurveFit:Speed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    gross_total_cooling_capacity_fraction: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'note': 'Ratio of capacity at this speed to the operating mode Rated Gross Total Cooling Capacity'
        },
    )
    evaporator_air_flow_rate_fraction: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'note': 'Ratio of capacity at this speed to the operating mode Rated Evaporator Air Flow Rate'
        },
    )
    condenser_air_flow_rate_fraction: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'note': 'Ratio of condenser air flow at this speed to the operating mode Rated Condenser Air Flow Rate'
        },
    )
    gross_sensible_heat_ratio: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    gross_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and condenser fan. Does not include supply fan heat or supply fan electrical energy input.',
        },
    )
    active_fraction_of_coil_face_area: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'The fraction of the cooling coil face which is actively cooled at this speed. For non-split-face coils, this should be 1.0.'
        },
    )
    n2017_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    evaporative_condenser_pump_power_fraction: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Ratio of evaporative condenser pump power at this speed to the operating mode Nominal Evaporative Condenser Pump Power'
        },
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    total_cooling_capacity_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'biquadratic curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb quadratic curve = a + b*edb + c*edb**2 wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    total_cooling_capacity_modifier_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load flow',
        },
    )
    energy_input_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    energy_input_ratio_modifier_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load flow',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Recoverable waste heat at full load and rated conditions',
        },
    )
    waste_heat_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*cdb + c*cdb**2 + d*edb + e*edb**2 + f*cdb*edb cdb = entering condenser dry-bulb temperature (C) edb = entering coil dry-bulb temperature (C)',
        },
    )
    sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the DX cooling coil (C) db = entering dry-bulb temperature seen by the DX cooling coil (C) entering ...',
        },
    )
    sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow If this curve is used and the Sensible Heat Ratio Modifier Function of Temperatur...',
        },
    )

    @property
    def total_cooling_capacity_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def total_cooling_capacity_modifier_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_modifier_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def energy_input_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.energy_input_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def energy_input_ratio_modifier_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.energy_input_ratio_modifier_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def waste_heat_modifier_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.waste_heat_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilCoolingDXMultiSpeed(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric or
    engine-driven compressor and condenser fan), multi-speed (or variable-
    speed). Optional moisture evaporation from wet coil when compressor cycles
    off with continuous fan operation. Requires two to four sets of performance
    data and will interpolate between speeds. Modeled as a single coil (multi-
    speed compressor or multiple compressors with row split or intertwined
    coil)."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:MultiSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    apply_part_load_fraction_to_speeds_greater_than_1: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    apply_latent_degradation_to_speeds_greater_than_1: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    fuel_type: Literal[
        'Diesel',
        'Electricity',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
    ] = Field(...)
    number_of_speeds: int = Field(
        ...,
        ge=2,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for coil capacity, SHR, COP, flow rate, and associated curves.'
        },
    )
    speed_1_gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Gross capacity excluding supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    speed_1_gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Gross Rated Sensible Heat Ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include supply fan heat'
        },
    )
    speed_1_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    speed_1_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, rated SHR and rated COP should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity',
        },
    )
    n2017_speed_1_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_1_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_1_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_1_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_1_total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_1_energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_1_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    speed_1_nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    speed_1_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation Rate from the Cooling Coil (when the compressor first turns off) and the Coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    speed_1_maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    speed_1_latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    speed_1_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Recoverable waste heat at full load and rated conditions',
        },
    )
    speed_1_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_1_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_1_evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'm3/s',
                'note': 'Used to calculate evaporative condenser water use',
            },
        )
    )
    speed_1_rated_evaporative_condenser_pump_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at high speed",
        },
    )
    speed_2_gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Gross capacity excluding supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    speed_2_gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Gross Rated Sensible Heat Ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include supply fan heat'
        },
    )
    speed_2_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    speed_2_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, rated SHR and rated COP should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity for Speed 2.',
        },
    )
    n2017_speed_2_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_2_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_2_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_2_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_2_total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_2_energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load Flow',
        },
    )
    speed_2_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (Cooling load/steady state capacity)',
        },
    )
    speed_2_nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    speed_2_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    speed_2_maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    speed_2_latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    speed_2_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Recoverable waste heat at full load and rated conditions',
        },
    )
    speed_2_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_2_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_2_evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'm3/s',
                'note': 'Used to calculate evaporative condenser water use',
            },
        )
    )
    speed_2_rated_evaporative_condenser_pump_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at low speed",
        },
    )
    speed_3_gross_rated_total_cooling_capacity: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Gross capacity excluding supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
            },
        )
    )
    speed_3_gross_rated_sensible_heat_ratio: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Gross Rated Sensible Heat Ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include supply fan heat'
        },
    )
    speed_3_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    speed_3_rated_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, rated SHR and rated COP should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity for Speed 3.',
        },
    )
    n2017_speed_3_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_3_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_3_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_3_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_3_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_3_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_3_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (Cooling load/steady state capacity)',
            },
        )
    )
    speed_3_nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    speed_3_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow and temperature conditions. ...",
        },
    )
    speed_3_maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    speed_3_latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    speed_3_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Recoverable waste heat at full load and rated conditions',
        },
    )
    speed_3_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_3_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_3_evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'm3/s',
                'note': 'Used to calculate evaporative condenser water use',
            },
        )
    )
    speed_3_rated_evaporative_condenser_pump_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at Low speed",
        },
    )
    speed_4_gross_rated_total_cooling_capacity: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Gross capacity excluding supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
            },
        )
    )
    speed_4_gross_rated_sensible_heat_ratio: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Gross Rated Sensible Heat Ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include supply fan heat'
        },
    )
    speed_4_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    speed_4_rated_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, rated SHR and rated COP should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity for Speed 4',
        },
    )
    n2017_speed_4_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_4_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_4_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_4_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_4_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    speed_4_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_4_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
            },
        )
    )
    speed_4_nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    speed_4_ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    speed_4_maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    speed_4_latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    speed_4_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Recoverable waste heat at full load and rated conditions',
        },
    )
    speed_4_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_4_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_4_evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'm3/s',
                'note': 'Used to calculate evaporative condenser water use',
            },
        )
    )
    speed_4_rated_evaporative_condenser_pump_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at Speed 4",
        },
    )
    zone_name_for_condenser_placement: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (condenser) of DX system or a heat pump is to be placed. This is an optional input field specified only when...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def speed_1_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def zone_for_condenser_placement_ref(self) -> IDFBaseModel | None:
        v = self.zone_name_for_condenser_placement
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])


class CoilCoolingDXSingleSpeed(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric
    compressor and condenser fan), single-speed. Optional inputs for moisture
    evaporation from wet coil when compressor cycles off with continuous fan
    operation."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:SingleSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, Rated SHR and Rated COP should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity',
        },
    )
    n2017_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    total_cooling_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load flow',
        },
    )
    energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = Fraction of the full load flow',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use',
        },
    )
    evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump",
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the DX cooling coil (C) db = entering dry-bulb temperature seen by the DX cooling coil (C) entering ...',
        },
    )
    sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    report_ashrae_standard_127_performance_ratings: Literal['', 'No', 'Yes'] | None = (
        Field(
            default='No',
            json_schema_extra={
                'note': 'when this input field is specified as Yes then the program calculates the net cooling capacity and total electric power input of DX cooling coils per ANSI/ASHRAE 127.'
            },
        )
    )
    zone_name_for_condenser_placement: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (condenser) of DX system or a heat pump is to be placed. This is an optional input field specified only when...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def energy_input_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def energy_input_ratio_function_of_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def sensible_heat_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def zone_for_condenser_placement_ref(self) -> IDFBaseModel | None:
        v = self.zone_name_for_condenser_placement
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])


class CoilCoolingDXSingleSpeedThermalStorage(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric
    compressor and condenser fan), single-speed with packaged integrated thermal
    storage for cooling."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:SingleSpeed:ThermalStorage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    operating_mode_control_method: Literal['EMSControlled', 'ScheduledModes'] = Field(
        ...
    )
    operation_mode_control_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is used if the control method is set to ScheduledModes Schedule values control operating mode: 0=off, 1=cooling only, 2= cooling and charge, 3= cooling and discharge, 4= charge only, and...',
        },
    )
    storage_type: Literal['Ice', 'UserDefinedFluidType', 'Water'] = Field(...)
    user_defined_fluid_type: FluidAndGlycolNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidAndGlycolNames'],
            'note': 'This field is required when Storage Type is UserDefinedFluidType',
        },
    )
    fluid_storage_volume: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3',
            'note': 'required field if Storage Type is Water or UserDefinedFluidType',
        },
    )
    ice_storage_capacity: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'GJ',
            'note': 'required field if Storage Type is Ice',
        },
    )
    storage_capacity_sizing_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'hr',
            'note': 'If one of the previous two fields is set to autocalculate, this determines the storage capacity as a function of Cooling Only Mode Rated Total Evaporator Cooling Capacity',
        },
    )
    storage_tank_ambient_temperature_node_name: str = Field(...)
    storage_tank_to_ambient_u_value_times_area_heat_transfer_coefficient: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/K'}
    )
    fluid_storage_tank_rating_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'required field if Storage Type is Water or UserDefinedFluidType',
        },
    )
    rated_evaporator_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, Rated SHR and Rated COP',
        },
    )
    evaporator_air_inlet_node_name: str = Field(...)
    evaporator_air_outlet_node_name: str = Field(...)
    cooling_only_mode_available: Literal['No', 'Yes'] = Field(...)
    cooling_only_mode_rated_total_evaporator_cooling_capacity: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Cooling Only Mode is available or if autocalculating sizes gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-b...',
        },
    )
    cooling_only_mode_rated_sensible_heat_ratio: float | None = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'required field if Cooling Only Mode is available Rated sensible heat ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    cooling_only_mode_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input required field if Cooling Only Mode is available',
        },
    )
    cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with two independent variables can be used biquadratic curve = a + b*ewb + c*ewb**2 + d*db + e*db**2 + f*ewb*db x = ewb = evapora...',
        },
    )
    cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x = ff ...',
        },
    )
    cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with two independent variables can be used curve = a + b*ewb + c*ewb**2 + d*db + e*db**2 + f*ewb*db x = ewb = evaporator entering...',
        },
    )
    cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x = ff ...',
        },
    )
    cooling_only_mode_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 x ...',
        },
    )
    cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with two independent variables can be used curve = a + b*ewb + c*ewb**2 + d*edb + e*edb**2 + f*ewb*edb x = ewb = evaporator enter...',
        },
    )
    cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x = ff ...',
        },
    )
    cooling_and_charge_mode_available: Literal['No', 'Yes'] = Field(...)
    cooling_and_charge_mode_rated_total_evaporator_cooling_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Cooling And Charge Mode is available gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering ...',
        },
    )
    cooling_and_charge_mode_capacity_sizing_factor: float | None = Field(
        default=0.5,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the evaporator capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    cooling_and_charge_mode_rated_storage_charging_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Cooling And Charge Mode is available net capacity including any internal devices rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering t...',
        },
    )
    cooling_and_charge_mode_storage_capacity_sizing_factor: float | None = Field(
        default=0.5,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the storage cooling capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    cooling_and_charge_mode_rated_sensible_heat_ratio: float | None = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'required field if Cooling And Charge Mode is available Rated sensible heat ratio (gross sensible evaporator capacity/gross total evaporator capacity) sensible and total capacities do not include su...'
        },
    )
    cooling_and_charge_mode_cooling_rated_cop: float | None = Field(
        default=3.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross evaporator cooling capacity divided by power input to the compressor (for cooling) and outdoor fan, does not include supply fan heat or supply fan electrical energy input required field if Co...',
        },
    )
    cooling_and_charge_mode_charging_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'net cooling capacity divided by power input to the compressor (for charging) and outdoor fan, includes any internal devices required field if Cooling And Charge Mode is available',
        },
    )
    cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporator e...',
        },
    )
    cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x...',
        },
    )
    cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporator e...',
        },
    )
    cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x...',
        },
    )
    cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR...',
        },
    )
    cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporator e...',
        },
    )
    cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR...',
        },
    )
    cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporator e...',
        },
    )
    cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x...',
        },
    )
    cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR...',
        },
    )
    cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | TrivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'TrivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Curves or tables with either two or three independent variables can be used. Curve:Biquadratic, Table:Lookup, Curve:Bicubic and Curve:Quadrati...',
        },
    )
    cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Charge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x...',
        },
    )
    cooling_and_discharge_mode_available: Literal['No', 'Yes'] = Field(...)
    cooling_and_discharge_mode_rated_total_evaporator_cooling_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Cooling And Discharge Mode is available gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air enteri...',
        },
    )
    cooling_and_discharge_mode_evaporator_capacity_sizing_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the charging capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    cooling_and_discharge_mode_rated_storage_discharging_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Cooling And Discharge Mode is available net capacity including any internal devices rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air enterin...',
        },
    )
    cooling_and_discharge_mode_storage_discharge_capacity_sizing_factor: (
        float | None
    ) = Field(
        default=1.0,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the charging capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    cooling_and_discharge_mode_rated_sensible_heat_ratio: float | None = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'required field if Cooling And Discharge Mode is available Rated sensible heat ratio (gross sensible evaporator capacity/gross total evaporator capacity) sensible and total capacities do not include...'
        },
    )
    cooling_and_discharge_mode_cooling_rated_cop: float | None = Field(
        default=3.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross evaporator cooling capacity divided by power input to the compressor (for cooling) and outdoor fan, does not include supply fan heat or supply fan electrical energy input required field if Co...',
        },
    )
    cooling_and_discharge_mode_discharging_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'gross cooling capacity divided by power input to the compressor (for discharging), includes any internal devices for discharging storage but not supply fan required field if Cooling And Discharge M...',
        },
    )
    cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling Only Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporator enterin...',
        },
    )
    cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**...',
        },
    )
    cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporato...',
        },
    )
    cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**...',
        },
    )
    cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*...',
        },
    )
    cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporato...',
        },
    )
    cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**...',
        },
    )
    cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*...',
        },
    )
    cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name: (
        TrivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['TrivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Allowed curve or table objects are Curve:Triquadratic and Table:Lookup curve or table = func(x = ewb, y = db, z = stes) x = ewb = evaporato...',
        },
    )
    cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**...',
        },
    )
    cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*...',
        },
    )
    cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | TrivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'TrivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Curves or tables with either two or three independent variables can be used. curve = a + b*ewb + c*ewb**2 + d*edb + e*edb**2 + f*ewb*edb x ...',
        },
    )
    cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Cooling And Discharge Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**...',
        },
    )
    charge_only_mode_available: Literal['No', 'Yes'] = Field(...)
    charge_only_mode_rated_storage_charging_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Charge Only  Mode is available net capacity including any internal devices air entering the outdoor condenser coil at 35 C dry-bulb/23.9 C wet-bulb thermal storage tank at 26.7 C ...',
        },
    )
    charge_only_mode_capacity_sizing_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the charging capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    charge_only_mode_charging_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'net cooling capacity divided by power input to the compressor (for charging) and outdoor fan, includes any internal devices required field if Charge Only Mode is available',
        },
    )
    charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Charge Only Mode is available Any curve or table with two independent variables can be used curve = a + b*db + c*db**2 + d*stes + e*stes**2 + f*db*stes x = db = dry-bulb temperatu...',
        },
    )
    charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Charge Only Mode is available Any curve or table with two independent variables can be used curve = a + b*db + c*db**2 + d*stes + e*stes**2 + f*db*stes x = db = dry-bulb temperatu...',
        },
    )
    discharge_only_mode_available: Literal['No', 'Yes'] = Field(...)
    discharge_only_mode_rated_storage_discharging_capacity: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'required field if Discharge Only Mode is available net capacity including any internal devices rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and thermal storage ta...',
        },
    )
    discharge_only_mode_capacity_sizing_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the discharging capacity as a multiplier on the Cooling Only Mode Rated Total Evaporator Cooling Capacity'
        },
    )
    discharge_only_mode_rated_sensible_heat_ratio: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'required field if Discharge Only Mode is available Rated sensible heat ratio (gross sensible evaporator capacity/gross total evaporator capacity) sensible and total capacities do not include supply...'
        },
    )
    discharge_only_mode_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'required field if Discharge Only Mode is available gross cooling capacity divided by power input to the compressor (for discharging), includes any internal devices for discharging storage but not s...',
        },
    )
    discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with two independent variables can be used curve = a + b*ewb + c*ewb**2 + d*stes + e*stes**2 + f*ewb*stes x = ewb = evaporator ...',
        },
    )
    discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x = f...',
        },
    )
    discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with two independent variables can be used curve = a + b*ewb + c*ewb**2 + d*stes + e*stes**2 + f*ewb*stes x = ewb = evaporator ...',
        },
    )
    discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 x = f...',
        },
    )
    discharge_only_mode_part_load_fraction_correlation_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3',
        },
    )
    discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | TrivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'TrivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Curves or tables with either two or three independent variables can be used. For two independent variables: x = ewb = entering wet-bulb temperatur...',
        },
    )
    discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'required field if Discharge Only Mode is available Any curve or table with one independent variable can be used quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = ...',
        },
    )
    ancillary_electric_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'controls and miscellaneous standby ancillary electric power draw, when available',
        },
    )
    cold_weather_operation_minimum_outdoor_air_temperature: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    cold_weather_operation_ancillary_power: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    condenser_air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_air_outlet_node_name: str = Field(...)
    condenser_design_air_flow_rate: float | Literal['Autocalculate'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate condenser leaving conditions and water use if evaporatively cooled.',
        },
    )
    condenser_air_flow_sizing_factor: float | None = Field(
        default=1.0,
        json_schema_extra={
            'note': 'If previous field is autocalculate, this determines the condenser air flow size as a multiplier on the Rated Evaporator Air Flow Rate.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.7,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'required field if condenser type is evaporatively cooled',
        },
    )
    evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump",
        },
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    storage_tank_plant_connection_inlet_node_name: str | None = Field(default=None)
    storage_tank_plant_connection_outlet_node_name: str | None = Field(default=None)
    storage_tank_plant_connection_design_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    storage_tank_plant_connection_heat_transfer_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    storage_tank_minimum_operating_limit_fluid_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'For fluid storage tanks only, minimum limit for storage tank If omitted,then the minimum temperature limit is that used for fluid property data.',
        },
    )
    storage_tank_maximum_operating_limit_fluid_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'For fluid storage tanks only, maximum limit for storage tank If omitted,then the maximum temperature limit is that used for fluid property data.',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def operation_mode_control_schedule(self) -> IDFBaseModel | None:
        v = self.operation_mode_control_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def user_defined_fluid_type_ref(self) -> IDFBaseModel | None:
        v = self.user_defined_fluid_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidAndGlycolNames'])

    @property
    def cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_only_mode_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_only_mode_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'TrivariateFunctions'])

    @property
    def cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['TrivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'TrivariateFunctions'])

    @property
    def cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def charge_only_mode_storage_charge_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def discharge_only_mode_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def discharge_only_mode_part_load_fraction_correlation_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'TrivariateFunctions'])

    @property
    def discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def basin_heater_availability_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingDXTwoSpeed(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric
    compressor and condenser fan), two-speed (or variable-speed). Requires two
    sets of performance data and will interpolate between speeds. Modeled as a
    single coil (multi-speed compressor or multiple compressors with row split
    or intertwined coil)."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:TwoSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    high_speed_gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    high_speed_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    high_speed_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    high_speed_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, Rated SHR and Rated COP. Should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity.',
        },
    )
    high_speed_2017_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=773.3,
            ge=0.0,
            le=1250.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    high_speed_2023_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=934.4,
            ge=0.0,
            le=1505.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    unit_internal_static_air_pressure: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter pressure drop for the unit containing the coil. This value is only used to calculate Energy Efficiency Ratio (EER), Integrated Energy Efficiency Ratio (IEER), and the Standard Rating (Net) Co...',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    total_cooling_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    low_speed_gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    low_speed_gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Gross Rated Sensible Heat Ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    low_speed_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    low_speed_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total cooling capacity, Rated SHR and Rated COP. Should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity.',
        },
    )
    low_speed_2017_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=773.3,
            ge=0.0,
            le=1250.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    low_speed_2023_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=934.4,
            ge=0.0,
            le=1505.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    low_speed_total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    low_speed_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    high_speed_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    high_speed_evaporative_condenser_air_flow_rate: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use',
        },
    )
    high_speed_evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at high speed",
        },
    )
    low_speed_evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    low_speed_evaporative_condenser_air_flow_rate: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use',
        },
    )
    low_speed_evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['Autosize'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump at low speed",
        },
    )
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the DX cooling coil (C) db = entering dry-bulb temperature seen by the DX cooling coil (C) entering ...',
        },
    )
    sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    low_speed_sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the DX cooling coil (C) db = entering dry-bulb temperature seen by the DX cooling coil (C) entering ...',
        },
    )
    low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    zone_name_for_condenser_placement: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (condenser) of DX system or a heat pump is to be placed. This is an optional input field specified only when...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def energy_input_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def energy_input_ratio_function_of_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def low_speed_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.low_speed_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def low_speed_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.low_speed_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def sensible_heat_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def low_speed_sensible_heat_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.low_speed_sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def low_speed_sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def zone_for_condenser_placement_ref(self) -> IDFBaseModel | None:
        v = self.zone_name_for_condenser_placement
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])


class CoilCoolingDXTwoStageWithHumidityControlMode(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric
    compressor and condenser fan), two-stage with humidity control mode (e.g.
    sub-cool or hot gas reheat). Optional inputs for moisture evaporation from
    wet coil when compressor cycles off with continuous fan operation. Requires
    two to four sets of performance data, see CoilPerformance:DX:Cooling. Stages
    are modeled as a face-split coil."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:TwoStageWithHumidityControlMode'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    number_of_capacity_stages: int | None = Field(default=1, ge=1, le=2)
    number_of_enhanced_dehumidification_modes: int | None = Field(default=0, ge=0, le=1)
    normal_mode_stage_1_coil_performance_object_type: Literal[
        'CoilPerformance:DX:Cooling'
    ] = Field(...)
    normal_mode_stage_1_coil_performance_name: CoilPerformanceDXRef = Field(
        ..., json_schema_extra={'object_list': ['CoilPerformanceDX']}
    )
    normal_mode_stage_1_2_coil_performance_object_type: (
        Literal['CoilPerformance:DX:Cooling'] | None
    ) = Field(default=None)
    normal_mode_stage_1_2_coil_performance_name: CoilPerformanceDXRef | None = Field(
        default=None, json_schema_extra={'object_list': ['CoilPerformanceDX']}
    )
    dehumidification_mode_1_stage_1_coil_performance_object_type: (
        Literal['CoilPerformance:DX:Cooling'] | None
    ) = Field(default=None)
    dehumidification_mode_1_stage_1_coil_performance_name: (
        CoilPerformanceDXRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['CoilPerformanceDX']})
    dehumidification_mode_1_stage_1_2_coil_performance_object_type: (
        Literal['CoilPerformance:DX:Cooling'] | None
    ) = Field(default=None)
    dehumidification_mode_1_stage_1_2_coil_performance_name: (
        CoilPerformanceDXRef | None
    ) = Field(default=None, json_schema_extra={'object_list': ['CoilPerformanceDX']})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def normal_mode_stage_1_coil_performance(self) -> IDFBaseModel | None:
        v = self.normal_mode_stage_1_coil_performance_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoilPerformanceDX'])

    @property
    def normal_mode_stage_1_2_coil_performance(self) -> IDFBaseModel | None:
        v = self.normal_mode_stage_1_2_coil_performance_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoilPerformanceDX'])

    @property
    def dehumidification_mode_1_stage_1_coil_performance(self) -> IDFBaseModel | None:
        v = self.dehumidification_mode_1_stage_1_coil_performance_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoilPerformanceDX'])

    @property
    def dehumidification_mode_1_stage_1_2_coil_performance(self) -> IDFBaseModel | None:
        v = self.dehumidification_mode_1_stage_1_2_coil_performance_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoilPerformanceDX'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class CoilCoolingDXVariableRefrigerantFlow(IDFBaseModel):
    """Variable refrigerant flow (VRF) direct expansion (DX) cooling coil. Used
    with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow. Condensing unit is
    modeled separately, see AirConditioner:VariableRefrigerantFlow."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:VariableRefrigerantFlow'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Cooling capacity excluding supply air fan heat',
        },
    )
    gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={'note': 'Sensible heat ratio excluding supply air fan heat'},
    )
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Volume flow rate corresponding to rated total cooling capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total cooling capacity',
        },
    )
    cooling_capacity_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions']
        },
    )
    cooling_capacity_modifier_curve_function_of_flow_fraction_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    coil_air_inlet_node: str = Field(...)
    coil_air_outlet_node: str = Field(...)
    name_of_water_storage_tank_for_condensate_collection: (
        WaterStorageTankNamesRef | None
    ) = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_capacity_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_capacity_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def cooling_capacity_modifier_curve_function_of_flow_fraction(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_capacity_modifier_curve_function_of_flow_fraction_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def name_of_water_storage_tank_for_condensate_collection_ref(
        self,
    ) -> IDFBaseModel | None:
        v = self.name_of_water_storage_tank_for_condensate_collection
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingDXVariableRefrigerantFlowFluidTemperatureControl(IDFBaseModel):
    """This is a key object in the new physics based VRF model applicable for Fluid
    Temperature Control. It describes the the indoor unit coil of the system at
    cooling mode. Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow.
    Outdoor unit is modeled separately, see
    AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl or
    AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR"""

    _idf_object_type: ClassVar[str] = (
        'Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that defines the availability of the coil Schedule values of 0 denote the unit is off. All other values denote the unit is available If this field is left blank, the un...',
        },
    )
    coil_air_inlet_node: str = Field(
        ..., json_schema_extra={'note': 'the inlet node to the coil'}
    )
    coil_air_outlet_node: str = Field(
        ..., json_schema_extra={'note': 'the outlet node to the coil'}
    )
    rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={'units': 'W', 'note': 'Supply air fan heat is not included'},
    )
    rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'note': 'Supply air fan heat is not included'}
    )
    indoor_unit_reference_superheating: float | None = Field(
        default=5.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    indoor_unit_evaporating_temperature_function_of_superheating_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    name_of_water_storage_tank_for_condensate_collection: (
        WaterStorageTankNamesRef | None
    ) = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def indoor_unit_evaporating_temperature_function_of_superheating_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.indoor_unit_evaporating_temperature_function_of_superheating_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def name_of_water_storage_tank_for_condensate_collection_ref(
        self,
    ) -> IDFBaseModel | None:
        v = self.name_of_water_storage_tank_for_condensate_collection
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingDXVariableSpeed(IDFBaseModel):
    """Direct expansion (DX) cooling coil and condensing unit (includes electric
    compressor and condenser fan), variable-speed. Optional inputs for moisture
    evaporation from wet coil when compressor cycles off with continuous fan
    operation. Requires two to ten sets of performance data and will interpolate
    between speeds. Modeled as a single coil with variable-speed compressor."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:DX:VariableSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    indoor_air_inlet_node_name: str = Field(...)
    indoor_air_outlet_node_name: str = Field(...)
    number_of_speeds: int | None = Field(
        default=2, ge=1, le=10, json_schema_extra={'units': 'dimensionless'}
    )
    nominal_speed_level: int | None = Field(
        default=2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'must be lower than or equal to the highest speed number',
        },
    )
    gross_rated_total_cooling_capacity_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    rated_air_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    nominal_time_for_condensate_to_begin_leaving_the_coil: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 's'}
    )
    initial_moisture_evaporation_rate_divided_by_steady_state_ac_latent_capacity: (
        float | None
    ) = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    maximum_cycling_rate: float | None = Field(
        default=2.5,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=60.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    fan_delay_time: float | None = Field(
        default=60.0,
        ge=0.0,
        json_schema_extra={
            'units': 's',
            'note': 'Programmed time delay for fan to shut off after compressor cycle off. Enter 0 when fan operating mode is continuous',
        },
    )
    energy_part_load_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump",
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-25.0, json_schema_extra={'units': 'C'}
    )
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    speed_1_reference_unit_gross_rated_total_cooling_capacity: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_1_reference_unit_gross_rated_sensible_heat_ratio: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_1_reference_unit_gross_rated_cooling_cop: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_1_reference_unit_rated_air_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_1_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_1_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_1_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_1_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_1_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled',
        },
    )
    speed_1_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None,
            ge=0.0,
            le=1.0,
            json_schema_extra={
                'units': 'dimensionless',
                'note': 'This field is only used for Condenser Type = EvaporativelyCooled',
            },
        )
    )
    speed_1_total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_2_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_2_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_2_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_2_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_2_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_2_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_2_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_2_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_2_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_3_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_3_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_3_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_3_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_3_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_3_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_3_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_3_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_3_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_4_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_4_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_4_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_4_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_4_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_4_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_4_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_4_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_4_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_5_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_5_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_5_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_5_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_5_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_5_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_5_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_5_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_5_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_6_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_6_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_6_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_6_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_6_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_6_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_6_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_6_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_6_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_7_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_7_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_7_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_7_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_7_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_7_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_7_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_7_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_7_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_8_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_8_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_8_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_8_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_8_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_8_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_8_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_8_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
        )
    )
    speed_8_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_9_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_9_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_9_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_9_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_9_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    n2023_speed_9_rated_evaporator_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_9_rated_evaporator_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
        },
    )
    speed_9_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'optional'}
    )
    speed_9_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None,
            ge=0.0,
            le=1.0,
            json_schema_extra={'units': 'dimensionless', 'note': 'optional'},
        )
    )
    speed_9_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_10_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_10_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_10_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_10_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=773.3,
            validation_alias='2017_speed_10_rated_evaporator_fan_power_per_volume_flow_rate',
            ge=0.0,
            le=1250.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    n2023_speed_10_rated_evaporator_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=934.4,
            validation_alias='2023_speed_10_rated_evaporator_fan_power_per_volume_flow_rate',
            ge=0.0,
            le=1505.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the evaporator fan power per air volume flow rate at the rated test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure ...',
            },
        )
    )
    speed_10_reference_unit_rated_condenser_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'optional'}
    )
    speed_10_reference_unit_rated_pad_effectiveness_of_evap_precooling: float | None = (
        Field(
            default=None,
            ge=0.0,
            le=1.0,
            json_schema_extra={'units': 'dimensionless', 'note': 'optional'},
        )
    )
    speed_10_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*odb + e*odb**2 + f*wb*odb wb = entering wet-bulb temperature (C) odb = air entering temperature seen by the condenser (C)',
        },
    )
    speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def energy_part_load_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_part_load_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def supply_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def speed_1_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilCoolingWater(IDFBaseModel):
    """Chilled water cooling coil, NTU-effectiveness model, with inputs for design
    entering and leaving conditions."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:Water'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    design_water_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    design_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    design_inlet_water_temperature: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'C'}
    )
    design_inlet_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'C'}
    )
    design_outlet_air_temperature: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'C'}
    )
    design_inlet_air_humidity_ratio: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    design_outlet_air_humidity_ratio: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    type_of_analysis: Literal['', 'DetailedAnalysis', 'SimpleAnalysis'] | None = Field(
        default='SimpleAnalysis'
    )
    heat_exchanger_configuration: Literal['', 'CounterFlow', 'CrossFlow'] | None = (
        Field(default='CounterFlow')
    )
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    design_water_temperature_difference: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This input field is optional. If specified, it is used for sizing the Design Water Flow Rate. If blank or omitted, the Loop Design Temperature Difference value specified in Sizing:Plant object is u...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingWaterDetailedGeometry(IDFBaseModel):
    """Chilled water cooling coil, detailed flat fin coil model for continuous
    plate fins, with inputs for detailed coil geometry specifications."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:Water:DetailedGeometry'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    maximum_water_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    tube_outside_surface_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'm2', 'note': 'Tube Primary Surface Area'},
    )
    total_tube_inside_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'm2', 'note': 'Total tube inside surface area'},
    )
    fin_surface_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm2'}
    )
    minimum_airflow_area: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm2'}
    )
    coil_depth: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm'}
    )
    fin_diameter: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'm', 'note': 'Fin diameter or the coil height'},
    )
    fin_thickness: float | None = Field(
        default=0.0015, gt=0.0, json_schema_extra={'units': 'm'}
    )
    tube_inside_diameter: float | None = Field(
        default=0.01445,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'Inner diameter of tubes'},
    )
    tube_outside_diameter: float | None = Field(
        default=0.0159,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'Outer diameter of tubes'},
    )
    tube_thermal_conductivity: float | None = Field(
        default=386.0, ge=1.0, json_schema_extra={'units': 'W/m-K'}
    )
    fin_thermal_conductivity: float | None = Field(
        default=204.0, ge=1.0, json_schema_extra={'units': 'W/m-K'}
    )
    fin_spacing: float | None = Field(
        default=0.0018,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'Fin spacing or distance'},
    )
    tube_depth_spacing: float | None = Field(
        default=0.026, gt=0.0, json_schema_extra={'units': 'm'}
    )
    number_of_tube_rows: float | None = Field(default=4.0, gt=0.0)
    number_of_tubes_per_row: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize'
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    condensate_collection_water_storage_tank_name: WaterStorageTankNamesRef | None = (
        Field(
            default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
        )
    )
    design_water_temperature_difference: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This input field is optional. If specified, it is used for sizing the Design Water Flow Rate. If blank or omitted, the Loop Design Temperature Difference value specified in Sizing:Plant object is u...',
        },
    )
    design_inlet_water_temperature: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'C',
            'note': 'This input field is optional. If specified, it is used for sizing the coil Design Geometry Parameters. If autosized, the Design Loop Exit Temperature value specified in Sizing:Plant object is used ...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def condensate_collection_water_storage_tank(self) -> IDFBaseModel | None:
        v = self.condensate_collection_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class CoilCoolingWaterToAirHeatPumpEquationFit(IDFBaseModel):
    """Direct expansion (DX) cooling coil for water-to-air heat pump (includes
    electric compressor), single-speed, equation-fit model. Optional inputs for
    moisture evaporation from wet coil when compressor cycles off with
    continuous fan operation. Equation-fit model uses normalized curves to
    describe the heat pump performance."""

    _idf_object_type: ClassVar[str] = 'Coil:Cooling:WaterToAirHeatPump:EquationFit'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    rated_water_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity at rated conditions not accounting for the effect of supply air fan heat',
        },
    )
    gross_rated_sensible_cooling_capacity: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    gross_rated_cooling_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling COP at rated conditions',
        },
    )
    rated_entering_water_temperature: float | None = Field(
        default=30.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Rated entering water temperature corresponding to the water-to -air application for which this coil is used. For example: for water loop applications, the rated temperature is 30 degree Celsius',
        },
    )
    rated_entering_air_dry_bulb_temperature: float | None = Field(
        default=27.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Rated entering air dry-bulb temperature corresponding to the water-to-air application for which this coil is used. For example: for water loop applications, the rated temperature is 27 degree Celsius',
        },
    )
    rated_entering_air_wet_bulb_temperature: float | None = Field(
        default=19.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Rated entering air wet-bulb temperature corresponding to the water-to-air application for which this coil is used. For example: for water loop applications, the rated temperature is 19 degree Celsius',
        },
    )
    total_cooling_capacity_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    sensible_cooling_capacity_curve_name: QuintvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuintvariateFunctions']}
    )
    cooling_power_consumption_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow and temperature conditions. Nominal time is equal to the ratio of the energy of the co...",
        },
    )
    ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    fan_delay_time: float | None = Field(
        default=60.0,
        ge=0.0,
        json_schema_extra={
            'units': 's',
            'note': 'Programmed time delay for heat pump fan to shut off after compressor cycle off. Only required when fan operating mode is cycling Enter 0 when fan operating mode is continuous',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def total_cooling_capacity_curve(self) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['QuadvariateFunctions'])

    @property
    def sensible_cooling_capacity_curve(self) -> IDFBaseModel | None:
        v = self.sensible_cooling_capacity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['QuintvariateFunctions'])

    @property
    def cooling_power_consumption_curve(self) -> IDFBaseModel | None:
        v = self.cooling_power_consumption_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['QuadvariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilCoolingWaterToAirHeatPumpParameterEstimation(IDFBaseModel):
    """Direct expansion (DX) cooling coil for water-to-air heat pump (includes
    electric compressor), single-speed, parameter estimation model. Optional
    inputs for moisture evaporation from wet coil when compressor cycles off
    with continuous fan operation. Parameter estimation model is a deterministic
    model that requires a consistent set of parameters to describe the operating
    conditions of the heat pump components."""

    _idf_object_type: ClassVar[str] = (
        'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    compressor_type: Literal['Reciprocating', 'Rotary', 'Scroll'] = Field(
        ...,
        json_schema_extra={
            'note': 'Parameters 1-5 are as named below. Parameters 6-10 depend on the type of compressor and fluid. Refer to the InputOutputReference on the parameters required'
        },
    )
    refrigerant_type: FluidNamesRef | None = Field(
        default='R22', json_schema_extra={'object_list': ['FluidNames']}
    )
    design_source_side_flow_rate: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm3/s'}
    )
    nominal_cooling_coil_capacity: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W'}
    )
    nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    high_pressure_cutoff: float = Field(..., gt=0.0, json_schema_extra={'units': 'Pa'})
    low_pressure_cutoff: float = Field(..., ge=0.0, json_schema_extra={'units': 'Pa'})
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    load_side_total_heat_transfer_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'W/K', 'note': 'Previously called Parameter 1'},
    )
    load_side_outside_surface_heat_transfer_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'W/K', 'note': 'Previously called Parameter 2'},
    )
    superheat_temperature_at_the_evaporator_outlet: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'C', 'note': 'Previously called Parameter 3'},
    )
    compressor_power_losses: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Accounts for the loss of work due to mechanical and electrical losses in the compressor. Previously called Parameter 4',
        },
    )
    compressor_efficiency: float = Field(
        ..., gt=0.0, json_schema_extra={'note': 'Previously called Parameter 5'}
    )
    compressor_piston_displacement: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Use when Compressor Type is Reciprocating or Rotary Leave this field blank for Compressor Type is Scroll. Previously part of Parameter 6',
        },
    )
    compressor_suction_discharge_pressure_drop: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Used when Compressor Type is Rotary or Reciprocating Leave this field blank for Compressor Type is Scroll. Previously part of Parameter 7',
        },
    )
    compressor_clearance_factor: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Used when Compressor Type is Reciprocating. Leave this field blank for Compressor Type is Rotary or Scroll. Previously part of Parameter 8',
        },
    )
    refrigerant_volume_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Use when Compressor Type is Scroll Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 6',
        },
    )
    volume_ratio: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Use when Compressor Type is Scroll. Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 7',
        },
    )
    leak_rate_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Use when Compressor Type is Scroll. Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 8'
        },
    )
    source_side_heat_transfer_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use when Source Side Fluid Name is Water Leave this field blank when Source Side Fluid Name is an antifreeze Previously part of Parameter 9',
        },
    )
    source_side_heat_transfer_resistance1: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Use when Source Side Fluid Name is an antifreeze Leave this field blank for Source Side Fluid is Water Previously part of Parameter 9',
        },
    )
    source_side_heat_transfer_resistance2: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use when Source Side Fluid Name is an antifreeze Leave this field blank for Source Side Fluid is Water Previously part of Parameter 10',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    fan_delay_time: float | None = Field(
        default=60.0,
        ge=0.0,
        json_schema_extra={
            'units': 's',
            'note': 'Programmed time delay for heat pump fan to shut off after compressor cycle off. Only required when fan operating mode is cycling Enter 0 when fan operating mode is continuous',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def refrigerant_type_ref(self) -> IDFBaseModel | None:
        v = self.refrigerant_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidNames'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit(IDFBaseModel):
    """Direct expansion (DX) cooling coil for water-to-air heat pump (includes
    electric compressor), variable-speed, equation-fit model. Optional inputs
    for moisture evaporation from wet coil when compressor cycles off with
    continuous fan operation. Equation-fit model uses normalized curves to
    describe the heat pump performance. Requires two to ten sets of performance
    data and will interpolate between speeds. Modeled as a single coil with
    variable-speed compressor."""

    _idf_object_type: ClassVar[str] = (
        'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    water_to_refrigerant_hx_water_inlet_node_name: str = Field(...)
    water_to_refrigerant_hx_water_outlet_node_name: str = Field(...)
    indoor_air_inlet_node_name: str = Field(...)
    indoor_air_outlet_node_name: str = Field(...)
    number_of_speeds: int | None = Field(
        default=2, ge=1, le=10, json_schema_extra={'units': 'dimensionless'}
    )
    nominal_speed_level: int | None = Field(
        default=2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'must be lower than or equal to the highest speed number',
        },
    )
    gross_rated_total_cooling_capacity_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    rated_air_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    rated_water_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    nominal_time_for_condensate_to_begin_leaving_the_coil: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 's'}
    )
    initial_moisture_evaporation_rate_divided_by_steady_state_ac_latent_capacity: (
        float | None
    ) = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling Rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    fan_delay_time: float | None = Field(
        default=60.0,
        ge=0.0,
        json_schema_extra={
            'units': 's',
            'note': 'Programmed time delay for heat pump fan to shut off after compressor cycle off. Enter 0 when fan operating mode is continuous',
        },
    )
    flag_for_using_hot_gas_reheat_0_or_1: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Flag for using hot gas reheat, 0 - not used, 1 - used',
        },
    )
    energy_part_load_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    speed_1_reference_unit_gross_rated_total_cooling_capacity: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_1_reference_unit_gross_rated_sensible_heat_ratio: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_1_reference_unit_gross_rated_cooling_cop: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_1_reference_unit_rated_air_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_reference_unit_rated_water_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_1_waste_heat_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_2_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_2_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_2_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_2_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_2_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_3_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_3_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_3_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_3_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_3_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_4_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_4_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_4_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_4_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_4_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_5_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_5_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_5_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_5_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_5_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_6_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_6_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_6_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_6_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_6_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_7_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_7_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_7_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_7_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_7_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_8_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_8_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_8_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_8_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_8_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_9_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_9_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_9_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_9_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_9_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_10_reference_unit_gross_rated_total_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_10_reference_unit_gross_rated_sensible_heat_ratio: float | None = Field(
        default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_10_reference_unit_gross_rated_cooling_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_10_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_total_cooling_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )
    speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_10_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature (C) ewt = water entering temperature seen by the condenser (C)',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def energy_part_load_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_part_load_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_5_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_6_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_7_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_8_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_9_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_10_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class CoilDXASHRAE205Performance(IDFBaseModel):
    """DX coil performance specification referencing an ASHRAE Standard 205
    compliant representation for air-to-air direct expansion refrigerant system
    (Representation Specification RS0004). As RS0004 files are intended to
    support both heating and cooling performance, this object may referenced by
    the Coil:Cooling:DX and the corresponding Coil:Heating:DX object (planned
    for future addition)."""

    _idf_object_type: ClassVar[str] = 'Coil:DX:ASHRAE205:Performance'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    representation_file_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of the ASHRAE 205 RS0004 (air-to-air direct expansion refrigerant system) representation file'
        },
    )
    performance_interpolation_method: Literal['', 'Cubic', 'Linear'] | None = Field(
        default='Linear'
    )
    rated_total_cooling_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Not yet implemented / reserved for future use. Full load cooling capacity at AHRI 210/240 "A" test conditions. Used to scale representation data.',
        },
    )
    rated_steady_state_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Not yet implemented / reserved for future use. Full load heating capacity at AHRI 210/240 "H1" test conditions. Used to scale representation data.',
        },
    )


class CoilHeatingDXMultiSpeed(IDFBaseModel):
    """Direct expansion (DX) heating coil (air-to-air heat pump) and compressor
    unit (includes electric or engine-driven compressor and outdoor fan), multi-
    speed (or variable-speed), with defrost controls. Requires two to four sets
    of performance data and will interpolate between speeds."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:DX:MultiSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-8.0, json_schema_extra={'units': 'C'}
    )
    outdoor_dry_bulb_temperature_to_turn_on_compressor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'The outdoor temperature when the compressor is automatically turned back on following an automatic shut off because of low outdoor dry-bulb temperature. This field is only used for the calculation ...',
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    defrost_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'biquadratic curve = a + b*wb + c*wb**2 + d*oat + e*oat**2 + f*wb*oat wb = wet-bulb temperature (C) of air entering the indoor coil oat = outdoor air dry-bulb temperature (C) only required if Revers...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(default='Timed')
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if timed defrost control is specified'
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'only applicable if resistive defrost strategy is specified',
        },
    )
    apply_part_load_fraction_to_speeds_greater_than_1: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    fuel_type: Literal[
        'Diesel',
        'Electricity',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
    ] = Field(...)
    region_number_for_calculating_hspf: int | None = Field(
        default=4,
        ge=1,
        le=6,
        json_schema_extra={
            'note': 'Standard Region number for which HSPF and other standard ratings are calculated'
        },
    )
    number_of_speeds: int = Field(
        ...,
        ge=2,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for coil capacity, COP, flow rate, and associated curves.'
        },
    )
    speed_1_gross_rated_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C rating point hea...',
        },
    )
    speed_1_gross_rated_heating_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Rated heating capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy',
        },
    )
    speed_1_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total heating capacity',
        },
    )
    n2017_speed_1_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_1_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_1_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_1_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_1_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_1_heating_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_1_energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_1_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (sensible heating load/steady state heating capacity)',
        },
    )
    speed_1_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'recoverable waste heat at full load and rated conditions',
        },
    )
    speed_1_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_2_gross_rated_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C rating point hea...',
        },
    )
    speed_2_gross_rated_heating_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Rated heating capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy',
        },
    )
    speed_2_rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total heating capacity',
        },
    )
    n2017_speed_2_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_2_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 2 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_2_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_2_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 2 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_2_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_2_heating_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_2_energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_2_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (sensible heating load/steady state heating capacity)',
        },
    )
    speed_2_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'recoverable waste heat at full load and rated conditions',
        },
    )
    speed_2_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_3_gross_rated_heating_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C rating point hea...',
        },
    )
    speed_3_gross_rated_heating_cop: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Rated heating capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy',
        },
    )
    speed_3_rated_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total heating capacity',
        },
    )
    n2017_speed_3_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_3_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 3 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_3_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_3_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 3 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_3_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_3_heating_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_3_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_3_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (sensible heating load/steady state heating capacity)',
            },
        )
    )
    speed_3_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'recoverable waste heat at full load and rated conditions',
        },
    )
    speed_3_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    speed_4_gross_rated_heating_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C rating point hea...',
        },
    )
    speed_4_gross_rated_heating_cop: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Rated heating capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy',
        },
    )
    speed_4_rated_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated total heating capacity',
        },
    )
    n2017_speed_4_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_4_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 4 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_4_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_4_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 4 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_4_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_4_heating_capacity_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    speed_4_energy_input_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    speed_4_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (sensible heating load/steady state heating capacity)',
            },
        )
    )
    speed_4_rated_waste_heat_fraction_of_power_input: float | None = Field(
        default=0.2,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'recoverable waste heat at full load and rated conditions',
        },
    )
    speed_4_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*odb + c*odb**2 + d*db + e*db**2 + f*odb*db odb = Outdoor air dry-bulb temperature (C) db = entering coil dry-bulb temperature (C)',
        },
    )
    zone_name_for_evaporator_placement: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (evaporator) of a heat pump is to be placed. This is an optional input field specified only when user desire...'
        },
    )
    speed_1_secondary_coil_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the secondary coil (evaporator) air flow rate when the heat pump is working in heating mode or the secondary DX coil (condenser) air flow rate when the heat pump is working in c...',
        },
    )
    speed_1_secondary_coil_fan_flow_scaling_factor: float | None = Field(
        default=1.25,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input field is scaling factor for autosizing the secondary DX coil fan flow rate. The secondary air flow rate is determined by multiplying the primary DX coil rated air flow rate by the fan fl...',
        },
    )
    speed_1_nominal_sensible_heat_ratio_of_secondary_coil: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the nominal sensible heat ratio used to split the heat extracted by a secondary DX coil (evaporator) of a heat pump into sensible and latent components. This is an optional inpu...',
        },
    )
    speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the secondary DX coil (C) db = entering dry-bulb temperature seen by the primary DX coil (C) This in...',
        },
    )
    speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = secondary air flow fraction of the full load flow This input field is name of sensible heat ratio modifier curve...',
        },
    )
    speed_2_secondary_coil_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the secondary coil (evaporator) air flow rate when the heat pump is working in heating mode or the secondary DX coil (condenser) air flow rate when the heat pump is working in c...',
        },
    )
    speed_2_secondary_coil_fan_flow_scaling_factor: float | None = Field(
        default=1.25,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input field is scaling factor for autosizing the secondary DX coil fan flow rate. The secondary air flow rate is determined by multiplying the primary DX coil rated air flow rate by the fan fl...',
        },
    )
    speed_2_nominal_sensible_heat_ratio_of_secondary_coil: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the nominal sensible heat ratio used to split the heat extracted by a secondary DX coil (evaporator) of a heat pump into sensible and latent components. This is an optional inpu...',
        },
    )
    speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the secondary DX coil (C) db = entering dry-bulb temperature seen by the primary DX coil (C) This in...',
        },
    )
    speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = secondary air flow fraction of the full load flow This input field is name of sensible heat ratio modifier curve...',
        },
    )
    speed_3_secondary_coil_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the secondary coil (evaporator) air flow rate when the heat pump is working in heating mode or the secondary DX coil (condenser) air flow rate when the heat pump is working in c...',
        },
    )
    speed_3_secondary_coil_fan_flow_scaling_factor: float | None = Field(
        default=1.25,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input field is scaling factor for autosizing the secondary DX coil fan flow rate. The secondary air flow rate is determined by multiplying the primary DX coil rated air flow rate by the fan fl...',
        },
    )
    speed_3_nominal_sensible_heat_ratio_of_secondary_coil: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the nominal sensible heat ratio used to split the heat extracted by a secondary DX coil (evaporator) of a heat pump into sensible and latent components. This is an optional inpu...',
        },
    )
    speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the secondary DX coil (C) db = entering dry-bulb temperature seen by the primary DX coil (C) This in...',
        },
    )
    speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = secondary air flow fraction of the full load flow This input field is name of sensible heat ratio modifier curve...',
        },
    )
    speed_4_secondary_coil_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the secondary coil (evaporator) air flow rate when the heat pump is working in heating mode or the secondary DX coil (condenser) air flow rate when the heat pump is working in c...',
        },
    )
    speed_4_secondary_coil_fan_flow_scaling_factor: float | None = Field(
        default=1.25,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input field is scaling factor for autosizing the secondary DX coil fan flow rate. The secondary air flow rate is determined by multiplying the primary DX coil rated air flow rate by the fan fl...',
        },
    )
    speed_4_nominal_sensible_heat_ratio_of_secondary_coil: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the nominal sensible heat ratio used to split the heat extracted by a secondary DX coil (evaporator) of a heat pump into sensible and latent components. This is an optional inpu...',
        },
    )
    speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the secondary DX coil (C) db = entering dry-bulb temperature seen by the primary DX coil (C) This in...',
        },
    )
    speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = secondary air flow fraction of the full load flow This input field is name of sensible heat ratio modifier curve...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_1_heating_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_heating_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_2_heating_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_heating_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_3_heating_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_heating_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_4_heating_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_heating_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingDXSingleSpeed(IDFBaseModel):
    """Direct expansion (DX) heating coil (air-to-air heat pump) and compressor
    unit (includes electric compressor and outdoor fan), single-speed, with
    defrost controls."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:DX:SingleSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    gross_rated_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C rating point hea...',
        },
    )
    gross_rated_heating_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Rated heating capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy does not include supply air fan heat or sup...',
        },
    )
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated heating capacity',
        },
    )
    n2017_rated_supply_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_rated_supply_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply fan power per air volume flow rate at the rated test conditions. as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure bas...',
        },
    )
    n2023_rated_supply_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_rated_supply_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply fan power per air volume flow rate at the rated test conditions. as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static pressure bas...',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    heating_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'quadratic curve = a + b*oat + c*oat**2 cubic curve = a + b*oat + c*oat**2 + d*oat**3 biquadratic curve = a + b*iat + c*iat**2 + d*oat + e*oat**2 + f*iat*oat oat = outdoor air dry-bulb temperature (...',
        },
    )
    energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (sensible heating load/steady state heating capacity)',
        },
    )
    defrost_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'biquadratic curve = a + b*wb + c*wb**2 + d*oat + e*oat**2 + f*wb*oat wb = wet-bulb temperature (C) of air entering the indoor coil oat = outdoor air dry-bulb temperature (C) only required if Revers...',
        },
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-8.0, json_schema_extra={'units': 'C'}
    )
    outdoor_dry_bulb_temperature_to_turn_on_compressor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'The outdoor temperature when the compressor is automatically turned back on following an automatic shut off because of low outdoor dry-bulb temperature. This field is only used for the calculation ...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(default='Timed')
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if timed defrost control is specified'
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'only applicable if resistive defrost strategy is specified',
        },
    )
    region_number_for_calculating_hspf: int | None = Field(
        default=4,
        ge=1,
        le=6,
        json_schema_extra={
            'note': 'Standard Region number for which HSPF and other standard ratings are calculated'
        },
    )
    evaporator_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    zone_name_for_evaporator_placement: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This input field is name of a conditioned or unconditioned zone where the secondary coil (evaporator) of a heat pump is to be placed. This is an optional input field specified only when user desire...'
        },
    )
    secondary_coil_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the secondary coil (evaporator) air flow rate when the heat pump is working in heating mode or the secondary DX coil (condenser) air flow rate when the heat pump is working in c...',
        },
    )
    secondary_coil_fan_flow_scaling_factor: float | None = Field(
        default=1.25,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input field is scaling factor for autosizing the secondary DX coil fan flow rate. The secondary air flow rate is determined by multiplying the primary DX coil rated air flow rate by the fan fl...',
        },
    )
    nominal_sensible_heat_ratio_of_secondary_coil: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input value is the nominal sensible heat ratio used to split the heat extracted by a secondary DX coil (evaporator) of a heat pump into sensible and latent components. This is an optional inpu...',
        },
    )
    sensible_heat_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the secondary DX coil (C) db = entering dry-bulb temperature seen by the primary DX coil (C) This in...',
        },
    )
    sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = secondary air flow fraction of the full load flow This input field is name of sensible heat ratio modifier curve...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_capacity_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_capacity_function_of_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def energy_input_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def energy_input_ratio_function_of_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def sensible_heat_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingDXVariableRefrigerantFlow(IDFBaseModel):
    """Variable refrigerant flow (VRF) direct expansion (DX) heating coil (air-to-
    air heat pump). Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow.
    Condensing unit is modeled separately, see
    AirConditioner:VariableRefrigerantFlow."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:DX:VariableRefrigerantFlow'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    gross_rated_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat capacity excluding supply air fan heat rating point outside dry-bulb temp 8.33 C, outside wet-bulb temp 6.11 C rating point hea...',
        },
    )
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'volume flow rate corresponding to rated total capacity should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated heating capacity',
        },
    )
    coil_air_inlet_node: str = Field(...)
    coil_air_outlet_node: str = Field(...)
    heating_capacity_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions']
        },
    )
    heating_capacity_modifier_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )

    @property
    def availability_schedule_ref(self) -> IDFBaseModel | None:
        v = self.availability_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_capacity_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_capacity_modifier_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_modifier_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingDXVariableRefrigerantFlowFluidTemperatureControl(IDFBaseModel):
    """This is a key object in the new physics based VRF model applicable for Fluid
    Temperature Control. It describes the the indoor unit coil of the system at
    heating mode. Used with ZoneHVAC:TerminalUnit:VariableRefrigerantFlow.
    Outdoor unit is modeled separately, see
    AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl or
    AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR"""

    _idf_object_type: ClassVar[str] = (
        'Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that defines the availability of the coil Schedule values of 0 denote the unit is off. All other values denote the unit is available If this field is left blank, the un...',
        },
    )
    coil_air_inlet_node: str = Field(
        ..., json_schema_extra={'note': 'the inlet node to the coil'}
    )
    coil_air_outlet_node: str = Field(
        ..., json_schema_extra={'note': 'the outlet node to the coil'}
    )
    rated_total_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={'units': 'W', 'note': 'Supply air fan heat is not included'},
    )
    indoor_unit_reference_subcooling: float | None = Field(
        default=5.0, ge=0.0, json_schema_extra={'units': 'deltaC'}
    )
    indoor_unit_condensing_temperature_function_of_subcooling_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )

    @property
    def availability_schedule_ref(self) -> IDFBaseModel | None:
        v = self.availability_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def indoor_unit_condensing_temperature_function_of_subcooling_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.indoor_unit_condensing_temperature_function_of_subcooling_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingDXVariableSpeed(IDFBaseModel):
    """Direct expansion (DX) heating coil (air-to-air heat pump) and compressor
    unit (includes electric compressor and outdoor fan), variable-speed, with
    defrost controls. Requires two to ten sets of performance data and will
    interpolate between speeds."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:DX:VariableSpeed'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    indoor_air_inlet_node_name: str = Field(...)
    indoor_air_outlet_node_name: str = Field(...)
    number_of_speeds: int | None = Field(
        default=2, ge=1, le=10, json_schema_extra={'units': 'dimensionless'}
    )
    nominal_speed_level: int | None = Field(
        default=2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'must be lower than or equal to the highest speed number',
        },
    )
    rated_heating_capacity_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'W'})
    rated_air_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    energy_part_load_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (heating load/steady state capacity)',
        },
    )
    defrost_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'biquadratic curve = a + b*wb + c*wb**2 + d*oat + e*oat**2 + f*wb*oat wb = wet-bulb temperature (C) of air entering the indoor coil oat = outdoor air dry-bulb temperature (C) only required if Revers...',
        },
    )
    minimum_outdoor_dry_bulb_temperature_for_compressor_operation: float | None = Field(
        default=-8.0, json_schema_extra={'units': 'C'}
    )
    outdoor_dry_bulb_temperature_to_turn_on_compressor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'The outdoor temperature when the compressor is automatically turned back on following an automatic shut off because of low outdoor dry-bulb temperature. This field is only used for the calculation ...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater_operation: (
        float | None
    ) = Field(default=10.0, ge=0.0, json_schema_extra={'units': 'C'})
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(default='Timed')
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if timed defrost control is specified'
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'only applicable if resistive defrost strategy is specified',
        },
    )
    speed_1_reference_unit_gross_rated_heating_capacity: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_1_reference_unit_gross_rated_heating_cop: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_1_reference_unit_rated_air_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_1_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_1_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_1_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_1_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_1_heating_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_2_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_2_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_2_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_2_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_2_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_2_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_2_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_3_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_3_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_3_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_3_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_3_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_3_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_3_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_4_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_4_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_4_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_4_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_4_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_4_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_4_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_5_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_5_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_5_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_5_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_5_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_5_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_5_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_6_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_6_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_6_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_6_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_6_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_6_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_6_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_7_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_7_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_7_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_7_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_7_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_7_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_7_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_8_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_8_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_8_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_8_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_8_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_8_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_8_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_9_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_9_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_9_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=773.3,
        validation_alias='2017_speed_9_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1250.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    n2023_speed_9_rated_supply_air_fan_power_per_volume_flow_rate: float | None = Field(
        default=934.4,
        validation_alias='2023_speed_9_rated_supply_air_fan_power_per_volume_flow_rate',
        ge=0.0,
        le=1505.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
        },
    )
    speed_9_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_10_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_10_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    n2017_speed_10_rated_supply_air_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=773.3,
            validation_alias='2017_speed_10_rated_supply_air_fan_power_per_volume_flow_rate',
            ge=0.0,
            le=1250.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2017 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
            },
        )
    )
    n2023_speed_10_rated_supply_air_fan_power_per_volume_flow_rate: float | None = (
        Field(
            default=934.4,
            validation_alias='2023_speed_10_rated_supply_air_fan_power_per_volume_flow_rate',
            ge=0.0,
            le=1505.0,
            json_schema_extra={
                'units': 'W/(m3/s)',
                'note': 'Enter the supply air fan power per air volume flow rate at the rated speed 1 test conditions as defined in the 2023 version of ANSI/AHRI Standard 210/240. The test conditions vary external static p...',
            },
        )
    )
    speed_10_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*oat + e*oat**2 + f*db*oat db = entering air dry-bulb temperature (C) oat = air entering temperature seen by the evaporator (C)',
        },
    )
    speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def energy_part_load_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_part_load_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def speed_3_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingDesuperheater(IDFBaseModel):
    """Desuperheater air heating coil. The heating energy provided by this coil is
    reclaimed from the superheated refrigerant gas leaving a compressor and does
    not impact the performance of the compressor. If the coil is located
    directly in an air loop branch or outdoor air equipment list, then it is
    controlled on leaving air temperature and the Temperature Setpoint Node Name
    must be specified. If the coil is contained within another component such as
    a unitary system, then the coil is controlled by the parent component and
    the setpoint node name is not entered."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Desuperheater'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    heat_reclaim_recovery_efficiency: float | None = Field(default=None, ge=0.0)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    heating_source_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:TwoSpeed',
        'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
        'Coil:Cooling:DX:VariableSpeed',
        'Refrigeration:CompressorRack',
        'Refrigeration:Condenser:AirCooled',
        'Refrigeration:Condenser:EvaporativeCooled',
        'Refrigeration:Condenser:WaterCooled',
    ] = Field(...)
    heating_source_name: DesuperHeatingCoilSourcesRef = Field(
        ..., json_schema_extra={'object_list': ['DesuperHeatingCoilSources']}
    )
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required if coil is temperature controlled. Temperature-based control requires the use of a SetpointManager object'
        },
    )
    on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'parasitic electric load associated with the desuperheater coil operation such as solenoid valves, etc.',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_source(self) -> IDFBaseModel | None:
        v = self.heating_source_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DesuperHeatingCoilSources'])


class CoilHeatingElectric(IDFBaseModel):
    """Electric heating coil. If the coil is located directly in an air loop branch
    or outdoor air equipment list, then it is controlled on leaving air
    temperature and the Temperature Setpoint Node Name must be specified. If the
    coil is contained within another component such as an air terminal unit,
    zone HVAC equipment, or unitary system, then the coil is controlled by the
    parent component and the setpoint node name is not entered."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Electric'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    efficiency: float | None = Field(default=1.0, le=1.0, gt=0.0)
    nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={'note': 'Required if coil is temperature controlled.'},
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class CoilHeatingElectricMultiStage(IDFBaseModel):
    """Electric heating coil, multi-stage. If the coil is located directly in an
    air loop branch or outdoor air equipment list, then it is controlled on
    leaving air temperature and the Temperature Setpoint Node Name must be
    specified. If the coil is contained within another component such as an air
    terminal unit, zone HVAC equipment, or unitary system, then the coil is
    controlled by the parent component and the setpoint node name is not
    entered."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Electric:MultiStage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required if coil is temperature controlled. controlled'
        },
    )
    number_of_stages: int = Field(
        ...,
        ge=1,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for coil capacity and Efficiency.'
        },
    )
    stage_1_efficiency: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/W'})
    stage_1_nominal_capacity: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    stage_2_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_2_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stage_3_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_3_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stage_4_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_4_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class CoilHeatingFuel(IDFBaseModel):
    """Gas or other fuel heating coil. If the coil is located directly in an air
    loop branch or outdoor air equipment list, then it is controlled on leaving
    air temperature and the Temperature Setpoint Node Name must be specified. If
    the coil is contained within another component such as an air terminal unit,
    zone HVAC equipment, or unitary system, then the coil is controlled by the
    parent component and the setpoint node name is not entered."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Fuel'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
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
    burner_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'optional, used if coil is temperature control and not load-base controlled'
        },
    )
    on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'parasitic electric load associated with the coil operation such as an inducer fan, etc... This will be modified by the part load ratio to reflect the time of operation in a timestep.',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve, PLF = a + b*PLR + c*PLR**2 cubic curve, PLF = a + b*PLR + c*PLR**2 + d*PLR**3 PLF = part load fraction PLR = part load ratio (sensible heating load/steady state heating capacity) C...',
        },
    )
    off_cycle_parasitic_fuel_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'parasitic fuel load when the coil is not operating (i.e., standing pilot)',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingGasMultiStage(IDFBaseModel):
    """Gas heating coil, multi-stage. If the coil is located directly in an air
    loop branch or outdoor air equipment list, then it is controlled on leaving
    air temperature and the Temperature Setpoint Node Name must be specified. If
    the coil is contained within another component such as an air terminal unit,
    zone HVAC equipment, or unitary system, then the coil is controlled by the
    parent component and the setpoint node name is not entered."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Gas:MultiStage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'optional, used if coil is temperature control and not load-base controlled.'
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve, PLF = a + b*PLR + c*PLR**2 cubic curve, PLF = a + b*PLR + c*PLR**2 + d*PLR**3 PLF = part load fraction PLR = part load ratio (sensible heating load/steady state heating capacity) C...',
        },
    )
    off_cycle_parasitic_gas_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'parasitic gas load when the gas coil is not operating (i.e., standing pilot)',
        },
    )
    number_of_stages: int = Field(
        ...,
        ge=1,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for coil capacity and Gas Burner Efficiency.'
        },
    )
    stage_1_gas_burner_efficiency: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_1_nominal_capacity: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'W'}
    )
    stage_1_on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Stage 1 parasitic electric load associated with the gas coil operation such as an inducer fan, etc. This will be modified by the part load ratio to reflect the time of operation in a timestep.',
        },
    )
    stage_2_gas_burner_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_2_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stage_2_on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Stage 2 parasitic electric load associated with the gas coil operation such as an inducer fan, etc. This will be modified by the part load ratio to reflect the time of operation in a timestep.',
        },
    )
    stage_3_gas_burner_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_3_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stage_3_on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Stage 3 parasitic electric load associated with the gas coil operation such as an inducer fan, etc. This will be modified by the part load ratio to reflect the time of operation in a timestep.',
        },
    )
    stage_4_gas_burner_efficiency: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    stage_4_nominal_capacity: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    stage_4_on_cycle_parasitic_electric_load: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Stage 4 parasitic electric load associated with the gas coil operation such as an inducer fan, etc. This will be modified by the part load ratio to reflect the time of operation in a timestep.',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingSteam(IDFBaseModel):
    """Steam heating coil. Condenses and sub-cools steam at loop pressure and
    discharges condensate through steam traps to low pressure condensate line."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Steam'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    maximum_steam_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    degree_of_subcooling: float | None = Field(
        default=None, ge=1.0, le=5.0, json_schema_extra={'units': 'C'}
    )
    degree_of_loop_subcooling: float | None = Field(
        default=20.0, ge=10.0, json_schema_extra={'units': 'C'}
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    coil_control_type: (
        Literal['TemperatureSetpointControl', 'ZoneLoadControl'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Use ZoneLoadControl if the coil is contained within another component such as an air terminal unit, zone HVAC equipment, or unitary system. Use TemperatureSetpointControl if the coil is located dir...'
        },
    )
    temperature_setpoint_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Required if Coil Control Type is TemperatureSetpointControl'
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class CoilHeatingWater(IDFBaseModel):
    """Hot water heating coil, NTU-effectiveness model, assumes a cross-flow heat
    exchanger. Two options for capacity inputs: UA and water flow rate or
    capacity and design temperatures."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:Water'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    u_factor_times_area_value: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'W/K', 'note': 'UA value under rating conditions'},
    )
    maximum_water_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    performance_input_method: (
        Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None
    ) = Field(default='UFactorTimesAreaAndDesignWaterFlowRate')
    rated_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    rated_inlet_water_temperature: float | None = Field(
        default=82.2, json_schema_extra={'units': 'C'}
    )
    rated_inlet_air_temperature: float | None = Field(
        default=16.6, json_schema_extra={'units': 'C'}
    )
    rated_outlet_water_temperature: float | None = Field(
        default=71.1, json_schema_extra={'units': 'C'}
    )
    rated_outlet_air_temperature: float | None = Field(
        default=32.2, json_schema_extra={'units': 'C'}
    )
    rated_ratio_for_air_and_water_convection: float | None = Field(default=0.5, gt=0.0)
    design_water_temperature_difference: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This input field is optional. If specified, it is used for sizing the Design Water Flow Rate. If blank or omitted, the Loop Design Temperature Difference value specified in Sizing:Plant object is u...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class CoilHeatingWaterToAirHeatPumpEquationFit(IDFBaseModel):
    """Direct expansion (DX) heating coil for water-to-air heat pump (includes
    electric compressor), single-speed, equation-fit model. Equation-fit model
    uses normalized curves to describe the heat pump performance."""

    _idf_object_type: ClassVar[str] = 'Coil:Heating:WaterToAirHeatPump:EquationFit'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    rated_water_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    gross_rated_heating_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at rated conditions not accounting for the effect of supply air fan heat',
        },
    )
    gross_rated_heating_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross heating COP at rated conditions',
        },
    )
    rated_entering_water_temperature: float | None = Field(
        default=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Rated entering water temperature corresponding to the water-to -air application for which this coil is used. For example: for water loop applications, the rated temperature is 20 degree Celsius.',
        },
    )
    rated_entering_air_dry_bulb_temperature: float | None = Field(
        default=20.0,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Rated entering air dry-bulb temperature corresponding to the water-to-air application for which this coil is used. For example: for water loop applications, the rated temperature is 20 degree Celsius.',
        },
    )
    ratio_of_rated_heating_capacity_to_rated_cooling_capacity: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Ratio of rated heating capacity to rated cooling capacity. This input is used to calculate the heating or cooling capacity when autosizing. This input is only used if a companion cooling coil of th...'
        },
    )
    heating_capacity_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    heating_power_consumption_curve_name: QuadvariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['QuadvariateFunctions']}
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (heat load/steady state capacity)',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_capacity_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['QuadvariateFunctions'])

    @property
    def heating_power_consumption_curve(self) -> IDFBaseModel | None:
        v = self.heating_power_consumption_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['QuadvariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingWaterToAirHeatPumpParameterEstimation(IDFBaseModel):
    """Direct expansion (DX) heating coil for water-to-air heat pump (includes
    electric compressor), single-speed, parameter estimation model. Parameter
    estimation model is a deterministic model that requires a consistent set of
    parameters to describe the operating conditions of the heat pump components."""

    _idf_object_type: ClassVar[str] = (
        'Coil:Heating:WaterToAirHeatPump:ParameterEstimation'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    compressor_type: Literal['Reciprocating', 'Rotary', 'Scroll'] = Field(
        ...,
        json_schema_extra={
            'note': 'Parameters 1-4 are as named below. Parameters 5-9 depend on the type of compressor. Refer to the InputOutputReference on the parameters required'
        },
    )
    refrigerant_type: FluidNamesRef | None = Field(
        default='R22', json_schema_extra={'object_list': ['FluidNames']}
    )
    design_source_side_flow_rate: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm3/s'}
    )
    gross_rated_heating_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    high_pressure_cutoff: float = Field(..., gt=0.0, json_schema_extra={'units': 'Pa'})
    low_pressure_cutoff: float = Field(..., ge=0.0, json_schema_extra={'units': 'Pa'})
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    load_side_total_heat_transfer_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'W/K', 'note': 'Previously called Parameter 1'},
    )
    superheat_temperature_at_the_evaporator_outlet: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'C', 'note': 'Previously called Parameter 2'},
    )
    compressor_power_losses: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Accounts for the loss of work due to mechanical and electrical losses in the compressor. Previously called Parameter 3',
        },
    )
    compressor_efficiency: float = Field(
        ..., gt=0.0, json_schema_extra={'note': 'Previously called Parameter 4'}
    )
    compressor_piston_displacement: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Use when Compressor Type is Reciprocating or Rotary Leave this field blank for Compressor Type is Scroll. Previously part of Parameter 5',
        },
    )
    compressor_suction_discharge_pressure_drop: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Used when Compressor Type is Rotary or Reciprocating Leave this field blank for Compressor Type is Scroll. Previously part of Parameter 6',
        },
    )
    compressor_clearance_factor: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Used when Compressor Type is Reciprocating. Leave this field blank for Compressor Type is Rotary or Scroll. Previously part of Parameter 7',
        },
    )
    refrigerant_volume_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Use when Compressor Type is Scroll Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 5',
        },
    )
    volume_ratio: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Use when Compressor Type is Scroll. Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 6',
        },
    )
    leak_rate_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Use when Compressor Type is Scroll. Leave this field blank for Compressor Type is Rotary or Reciprocating. Previously part of Parameter 7',
        },
    )
    source_side_heat_transfer_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use when Source Side Fluid Name is Water Leave this field blank when Source Side Fluid is an antifreeze Previously part of Parameter 8',
        },
    )
    source_side_heat_transfer_resistance1: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Use when Source Side Fluid Name is an antifreeze Leave this field blank for Source Side Fluid is Water Previously part of Parameter 8',
        },
    )
    source_side_heat_transfer_resistance2: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Use when Source Side Fluid Name is an antifreeze Leave this field blank for Source Side Fluid is Water Previously part of Parameter 9',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (heating load/steady state capacity)',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def refrigerant_type_ref(self) -> IDFBaseModel | None:
        v = self.refrigerant_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidNames'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit(IDFBaseModel):
    """Direct expansion (DX) heating coil for water-to-air heat pump (includes
    electric compressor), variable-speed, equation-fit model. Equation-fit model
    uses normalized curves to describe the heat pump performance. Requires two
    to ten sets of performance data and will interpolate between speeds."""

    _idf_object_type: ClassVar[str] = (
        'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    water_to_refrigerant_hx_water_inlet_node_name: str = Field(...)
    water_to_refrigerant_hx_water_outlet_node_name: str = Field(...)
    indoor_air_inlet_node_name: str = Field(...)
    indoor_air_outlet_node_name: str = Field(...)
    number_of_speeds: int | None = Field(
        default=2, ge=1, le=10, json_schema_extra={'units': 'dimensionless'}
    )
    nominal_speed_level: int | None = Field(
        default=2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'must be lower than or equal to the highest speed number',
        },
    )
    rated_heating_capacity_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'W'})
    rated_air_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    rated_water_flow_rate_at_selected_nominal_speed_level: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'm3/s'})
    energy_part_load_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (heating load/steady state capacity)',
        },
    )
    speed_1_reference_unit_gross_rated_heating_capacity: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_1_reference_unit_gross_rated_heating_cop: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_1_reference_unit_rated_air_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_reference_unit_rated_water_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_heating_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_heating_capacity_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_1_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    speed_1_waste_heat_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_2_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_2_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_2_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_2_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_3_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_3_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_3_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_3_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_4_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_4_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_4_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_4_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_5_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_5_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_5_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_5_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_6_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_6_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_6_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_6_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_7_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_7_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_7_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_7_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_8_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_8_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_8_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_8_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_9_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_9_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_9_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_9_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_10_reference_unit_gross_rated_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    speed_10_reference_unit_gross_rated_heating_cop: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'W/W'}
    )
    speed_10_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )
    speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_reference_unit_waste_heat_fraction_of_input_power_at_rated_conditions: (
        float | None
    ) = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    speed_10_waste_heat_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'optional curve = a + b*db + c*db**2 + d*ewt + e*ewt**2 + f*db*ewt db = entering air dry-bulb temperature (C) ewt = water entering temperature seen by the evaporator (C)',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def energy_part_load_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_part_load_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_5_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_6_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_7_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_8_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_9_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_heating_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_energy_input_ratio_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_waste_heat_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_10_waste_heat_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class CoilPerformanceDXCooling(IDFBaseModel):
    """Used to specify DX cooling coil performance for one mode of operation for a
    Coil:Cooling:DX:TwoStageWithHumidityControlMode object which may reference
    one to four CoilPerformance:DX:Cooling objects depending on the specified
    number of stages and dehumidification modes. In nearly all cases, the Rated
    Air Flow Rate will be the same for all performance objects associated with a
    given coil. If bypass is specified, the Rated Air Flow Rate includes both
    the bypassed flow and the flow through the active part of the coil."""

    _idf_object_type: ClassVar[str] = 'CoilPerformance:DX:Cooling'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    gross_rated_total_cooling_capacity: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat gross capacity excluding supply air fan heat rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bu...',
        },
    )
    gross_rated_sensible_heat_ratio: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) sensible and total capacities do not include supply fan heat'
        },
    )
    gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    rated_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Flow rate corresponding to Rated total Cooling capacity, Rated SHR and Rated COP',
        },
    )
    fraction_of_air_flow_bypassed_around_coil: float | None = Field(
        default=0.0,
        ge=0.0,
        lt=1.0,
        json_schema_extra={
            'note': 'Fraction of Rated Air Flow Rate which bypasses the cooling coil in this performance mode. The remaining portion of the flow should be between 0.00004027 m3/s and .00006041 m3/s per watt of rated to...'
        },
    )
    total_cooling_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    total_cooling_capacity_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    energy_input_ratio_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*edb + e*edb**2 + f*wb*edb wb = entering wet-bulb temperature (C) edb = dry-bulb temperature seen by the condenser (C)',
        },
    )
    energy_input_ratio_function_of_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*PLR + c*PLR**2 cubic curve = a + b*PLR + c*PLR**2 + d*PLR**3 PLR = part load ratio (cooling load/steady state capacity)',
        },
    )
    nominal_time_for_condensate_removal_to_begin: float | None = Field(
        default=0.0,
        ge=0.0,
        le=3000.0,
        json_schema_extra={
            'units': 's',
            'note': "The nominal time for condensate to begin leaving the coil's condensate drain line at the coil's rated air flow rate and temperature conditions. Nominal time is equal to the ratio of the energy of t...",
        },
    )
    ratio_of_initial_moisture_evaporation_rate_and_steady_state_latent_capacity: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': "Ratio of the initial moisture evaporation rate from the cooling coil (when the compressor first turns off) and the coil's steady state latent capacity at rated air flow rate and temperature conditi...",
        },
    )
    maximum_cycling_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor, which occurs at 50% run time fraction. Suggested value is 3; zero value means latent degradation model is disabled.',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=0.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's latent capacity to reach steady state after startup. Suggested value is 45; zero value means latent degradation model is disabled.",
        },
    )
    condenser_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the name of an outdoor air node. This node name is also specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'
        },
    )
    condenser_type: Literal['', 'AirCooled', 'EvaporativelyCooled'] | None = Field(
        default='AirCooled'
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.9, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use',
        },
    )
    evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump",
        },
    )
    sensible_heat_ratio_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'curve = a + b*wb + c*wb**2 + d*db + e*db**2 + f*wb*db wb = entering wet-bulb temperature seen by the DX cooling coil (C) db = entering dry-bulb temperature seen by the DX cooling coil (C) entering ...',
        },
    )
    sensible_heat_ratio_function_of_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'quadratic curve = a + b*ff + c*ff**2 cubic curve = a + b*ff + c*ff**2 + d*ff**3 ff = fraction of the full load flow',
        },
    )

    @property
    def total_cooling_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def total_cooling_capacity_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.total_cooling_capacity_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def energy_input_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def energy_input_ratio_function_of_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.energy_input_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def sensible_heat_ratio_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def sensible_heat_ratio_function_of_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.sensible_heat_ratio_function_of_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilSystemCoolingDX(IDFBaseModel):
    """Virtual container component that consists of a DX cooling coil and its
    associated controls. This control object supports several different types of
    DX cooling coils and may be placed directly in an air loop branch or outdoor
    air equipment list."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:Cooling:DX'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    dx_cooling_coil_system_inlet_node_name: str = Field(...)
    dx_cooling_coil_system_outlet_node_name: str = Field(...)
    dx_cooling_coil_system_sensor_node_name: str = Field(...)
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
        'Coil:Cooling:DX:TwoSpeed',
        'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
        'Coil:Cooling:DX:VariableSpeed',
        'CoilSystem:Cooling:DX:HeatExchangerAssisted',
    ] = Field(...)
    cooling_coil_name: (
        CoilCoolingDXRef | CoolingCoilsDXRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'CoolingCoilsDX',
                'CoolingCoilsDXVariableSpeed',
            ]
        },
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only Multimode = activate enhanced dehumidification mode as needed and meet sensible load. If no sensible load exists, and Run on Latent Load = Yes, and a latent load exis...'
        },
    )
    run_on_sensible_load: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If Yes, unit will run if there is a sensible load. If No, unit will not run if there is only a sensible load. Dehumidification controls will be active if specified.'
        },
    )
    run_on_latent_load: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'If Yes, unit will run if there is a latent load. even if there is no sensible load. If No, unit will not run only if there is a latent load. Dehumidification controls will be active if specified.'
        },
    )
    use_outdoor_air_dx_cooling_coil: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This input field is designed for use with DX cooling coils with low air flow to capacity ratio range (100 - 300 cfm/ton). Typical application is 100% dedicated outdoor air system (DOAS). Other air ...'
        },
    )
    outdoor_air_dx_cooling_coil_leaving_minimum_air_temperature: float | None = Field(
        default=2.0,
        ge=0.0,
        le=7.2,
        json_schema_extra={
            'units': 'C',
            'note': 'DX cooling coil leaving minimum air temperature defines the minimum DX cooling coil leaving air temperature that should be maintained to avoid frost formation. This input field is optional and only...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_coil(self) -> IDFBaseModel | None:
        v = self.cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['CoilCoolingDX', 'CoolingCoilsDX', 'CoolingCoilsDXVariableSpeed']
        )


class CoilSystemCoolingDXHeatExchangerAssisted(IDFBaseModel):
    """Virtual component consisting of a direct expansion (DX) cooling coil and an
    air-to-air heat exchanger. The air-to-air heat exchanger precools the air
    entering the cooling coil and reuses this energy to reheat the supply air
    leaving the cooling coil. This heat exchange process improves the latent
    removal performance of the cooling coil (lower sensible heat ratio)."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:Cooling:DX:HeatExchangerAssisted'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    heat_exchanger_object_type: Literal[
        'HeatExchanger:AirToAir:FlatPlate',
        'HeatExchanger:AirToAir:SensibleAndLatent',
        'HeatExchanger:Desiccant:BalancedFlow',
    ] = Field(...)
    heat_exchanger_name: HXAirToAirNamesRef = Field(
        ..., json_schema_extra={'object_list': ['HXAirToAirNames']}
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:VariableSpeed',
    ] = Field(...)
    cooling_coil_name: (
        CoilCoolingDXRef | CoolingCoilsDXSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'CoolingCoilsDXSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ]
        },
    )

    @property
    def heat_exchanger(self) -> IDFBaseModel | None:
        v = self.heat_exchanger_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HXAirToAirNames'])

    @property
    def cooling_coil(self) -> IDFBaseModel | None:
        v = self.cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v,
            [
                'CoilCoolingDX',
                'CoolingCoilsDXSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ],
        )


class CoilSystemCoolingWater(IDFBaseModel):
    """Virtual container component that consists of a water cooling coil and its
    associated controls. This control object supports the available water coil
    types and may be placed directly on an air loop branch or in an outdoor air
    equipment list."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:Cooling:Water'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    cooling_coil_object_type: Literal[
        'Coil:Cooling:Water',
        'Coil:Cooling:Water:DetailedGeometry',
        'CoilSystem:Cooling:Water:HeatExchangerAssisted',
    ] = Field(...)
    cooling_coil_name: CoolingCoilsWaterRef = Field(
        ..., json_schema_extra={'object_list': ['CoolingCoilsWater']}
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only. Valid with all cooling coil types. When a heat exchanger assisted cooling coil is used, the heat exchanger is locked on at all times. Multimode = activate water coil...'
        },
    )
    run_on_sensible_load: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If Yes, unit will run if there is a sensible load. If No, unit will not run if there is only a sensible load. Dehumidification controls will be active if specified.'
        },
    )
    run_on_latent_load: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'If Yes, unit will run if there is a latent load. even if there is no sensible load. If No, unit will not run if there is only a latent load. Dehumidification controls will be active if specified.'
        },
    )
    minimum_air_to_water_temperature_offset: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Coil will turn on as required when inlet air temperature is above water temperature by amount of offset. To model a waterside economizer connect to condenser loop and increase offset as desired.',
        },
    )
    economizer_lockout: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Yes means that the heat exchanger will be locked out (off)'
        },
    )
    minimum_water_loop_temperature_for_heat_recovery: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Only used for heat recovery loops. Loop will turn off below this temperature.',
        },
    )
    companion_coil_used_for_heat_recovery: CoolingCoilsWaterRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CoolingCoilsWater'],
            'note': 'Only used for heat recovery loops. Entering a coil name indicates a heat recovery loop is specified. Coil listed is connected in series with this objects coil on demand side branch of a plant loop....',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_coil(self) -> IDFBaseModel | None:
        v = self.cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoolingCoilsWater'])

    @property
    def companion_coil_used_for_heat_recovery_ref(self) -> IDFBaseModel | None:
        v = self.companion_coil_used_for_heat_recovery
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoolingCoilsWater'])


class CoilSystemCoolingWaterHeatExchangerAssisted(IDFBaseModel):
    """Virtual component consisting of a chilled-water cooling coil and an air-to-
    air heat exchanger. The air-to-air heat exchanger precools the air entering
    the cooling coil and reuses this energy to reheat the supply air leaving the
    cooling coil. This heat exchange process improves the latent removal
    performance of the cooling coil (lower sensible heat ratio)."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:Cooling:Water:HeatExchangerAssisted'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    heat_exchanger_object_type: Literal[
        'HeatExchanger:AirToAir:FlatPlate', 'HeatExchanger:AirToAir:SensibleAndLatent'
    ] = Field(...)
    heat_exchanger_name: str = Field(...)
    cooling_coil_object_type: Literal[
        'Coil:Cooling:Water', 'Coil:Cooling:Water:DetailedGeometry'
    ] = Field(...)
    cooling_coil_name: CoolingCoilsWaterNoHXRef = Field(
        ..., json_schema_extra={'object_list': ['CoolingCoilsWaterNoHX']}
    )

    @property
    def cooling_coil(self) -> IDFBaseModel | None:
        v = self.cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoolingCoilsWaterNoHX'])


class CoilSystemHeatingDX(IDFBaseModel):
    """Virtual container component that consists of a DX heating coil (heat pump)
    and its associated controls. This control object supports two different
    types of DX heating coils and may be placed directly in an air loop branch
    or outdoor air equipment list."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:Heating:DX'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    heating_coil_object_type: Literal[
        'Coil:Heating:DX:SingleSpeed', 'Coil:Heating:DX:VariableSpeed'
    ] = Field(...)
    heating_coil_name: HeatingCoilsDXSingleSpeedRef | HeatingCoilsDXVariableSpeedRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': [
                    'HeatingCoilsDXSingleSpeed',
                    'HeatingCoilsDXVariableSpeed',
                ]
            },
        )
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_coil(self) -> IDFBaseModel | None:
        v = self.heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['HeatingCoilsDXSingleSpeed', 'HeatingCoilsDXVariableSpeed']
        )


class CoilSystemIntegratedHeatPumpAirSource(IDFBaseModel):
    """This object is used for air-source integrated heat pump, a collection of its
    working modes."""

    _idf_object_type: ClassVar[str] = 'CoilSystem:IntegratedHeatPump:AirSource'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of an air-source integrated heat pump.'
        },
    )
    supply_hot_water_flow_sensor_node_name: str = Field(...)
    space_cooling_coil_name: CoolingCoilsDXVariableSpeedRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingCoilsDXVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:Cooling:DX:VariableSpeed object.',
        },
    )
    space_heating_coil_name: HeatingCoilsDXVariableSpeedRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilsDXVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:Heating:DX:VariableSpeed object.',
        },
    )
    dedicated_water_heating_coil_name: (
        HeatPumpWaterHeaterDXCoilsVariableSpeedRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed object.',
        },
    )
    scwh_coil_name: HeatPumpWaterHeaterDXCoilsVariableSpeedRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed object.',
        },
    )
    scdwh_cooling_coil_name: CoolingCoilsDXVariableSpeedRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CoolingCoilsDXVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:Cooling:DX:VariableSpeed object.',
        },
    )
    scdwh_water_heating_coil_name: HeatPumpWaterHeaterDXCoilsVariableSpeedRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
                'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed object.',
            },
        )
    )
    shdwh_heating_coil_name: HeatingCoilsDXVariableSpeedRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilsDXVariableSpeed'],
            'note': 'Must match the name used in the corresponding Coil:Heating:DX:VariableSpeed object.',
        },
    )
    shdwh_water_heating_coil_name: HeatPumpWaterHeaterDXCoilsVariableSpeedRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
                'note': 'Must match the name used in the corresponding Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed object.',
            },
        )
    )
    indoor_temperature_limit_for_scwh_mode: float | None = Field(
        default=20.0,
        gt=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Indoor Temperature above which Indoor Overcooling is Allowed during Cooling Operation',
        },
    )
    ambient_temperature_limit_for_scwh_mode: float | None = Field(
        default=27.0,
        gt=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Ambient Temperature above which Indoor Overcooling is Allowed during Cooling Operation',
        },
    )
    indoor_temperature_above_which_wh_has_higher_priority: float | None = Field(
        default=20.0,
        gt=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Indoor Temperature above which Water Heating has the higher priority and Space Heating Call Can be ignored.',
        },
    )
    ambient_temperature_above_which_wh_has_higher_priority: float | None = Field(
        default=20.0,
        gt=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Ambient Temperature above which Water Heating has the higher priority and Space Heating Call Can be ignored.',
        },
    )
    flag_to_indicate_load_control_in_scwh_mode: int | None = Field(
        default=0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': '0: match space cooling load in SCWH mode, 1: match water heating load in SCWH mode',
        },
    )
    minimum_speed_level_for_scwh_mode: int | None = Field(
        default=1, gt=0, lt=10, json_schema_extra={'units': 'dimensionless'}
    )
    maximum_water_flow_volume_before_switching_from_scdwh_to_scwh_mode: float | None = (
        Field(default=0.0, json_schema_extra={'units': 'm3'})
    )
    minimum_speed_level_for_scdwh_mode: int | None = Field(
        default=1, gt=0, lt=10, json_schema_extra={'units': 'dimensionless'}
    )
    maximum_running_time_before_allowing_electric_resistance_heat_use_during_shdwh_mode: (
        float | None
    ) = Field(default=360.0, gt=0.0, json_schema_extra={'units': 's'})
    minimum_speed_level_for_shdwh_mode: int | None = Field(
        default=1, gt=0, lt=10, json_schema_extra={'units': 'dimensionless'}
    )

    @property
    def space_cooling_coil(self) -> IDFBaseModel | None:
        v = self.space_cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoolingCoilsDXVariableSpeed'])

    @property
    def space_heating_coil(self) -> IDFBaseModel | None:
        v = self.space_heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatingCoilsDXVariableSpeed'])

    @property
    def dedicated_water_heating_coil(self) -> IDFBaseModel | None:
        v = self.dedicated_water_heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatPumpWaterHeaterDXCoilsVariableSpeed'])

    @property
    def scwh_coil(self) -> IDFBaseModel | None:
        v = self.scwh_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatPumpWaterHeaterDXCoilsVariableSpeed'])

    @property
    def scdwh_cooling_coil(self) -> IDFBaseModel | None:
        v = self.scdwh_cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CoolingCoilsDXVariableSpeed'])

    @property
    def scdwh_water_heating_coil(self) -> IDFBaseModel | None:
        v = self.scdwh_water_heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatPumpWaterHeaterDXCoilsVariableSpeed'])

    @property
    def shdwh_heating_coil(self) -> IDFBaseModel | None:
        v = self.shdwh_heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatingCoilsDXVariableSpeed'])

    @property
    def shdwh_water_heating_coil(self) -> IDFBaseModel | None:
        v = self.shdwh_water_heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatPumpWaterHeaterDXCoilsVariableSpeed'])


class CoilWaterHeatingAirToWaterHeatPumpPumped(IDFBaseModel):
    """Heat pump water heater (HPWH) heating coil, air-to-water direct-expansion
    (DX) system which includes a water heating coil, evaporator air coil,
    evaporator fan, electric compressor, and water pump. Part of a
    WaterHeater:HeatPump:PumpedCondenser system."""

    _idf_object_type: ClassVar[str] = 'Coil:WaterHeating:AirToWaterHeatPump:Pumped'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a heat pump water heater DX coil.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rated_heating_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    rated_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pum...',
        },
    )
    rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    rated_evaporator_inlet_air_dry_bulb_temperature: float | None = Field(
        default=19.7,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air dry-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_inlet_air_wet_bulb_temperature: float | None = Field(
        default=13.5,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air wet-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_condenser_inlet_water_temperature: float | None = Field(
        default=57.5,
        gt=25.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Condenser inlet water temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_air_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Evaporator air flow rate corresponding to rated coil performance (heating capacity, COP and SHR). Default is 5.035E-5 m3/s/W (31.25 cfm/MBH) of rated heating capacity when autocalculated.',
        },
    )
    rated_condenser_water_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Condenser water flow rate corresponding to rated coil performance (heating capacity, COP and SHR). Default is 4.487E-8 m3/s/W (0.208 gpm/MBH) of rated heating capacity when autocalculated. A warnin...',
        },
    )
    evaporator_fan_power_included_in_rated_cop: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Select Yes if the evaporator fan power is included in the rated COP. This choice field impacts the calculation of compressor electric power.'
        },
    )
    condenser_pump_power_included_in_rated_cop: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Select Yes if the condenser pump power is included in the rated COP. This choice field impacts the calculation of compressor electric power.'
        },
    )
    condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='No',
        json_schema_extra={
            'note': 'Select Yes if the condenser pump heat is included in the rated heating capacity and rated COP. This choice field impacts the calculation of water heating capacity.'
        },
    )
    condenser_water_pump_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'A warning message will be issued if the ratio of Condenser Water Pump Power to Rated Heating Capacity exceeds 0.1422 W/W (41.67 Watts/MBH), but the simulation will continue.',
        },
    )
    fraction_of_condenser_pump_heat_to_water: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Fraction of pump heat transferred to the condenser water. The pump is assumed to be located downstream of the condenser.'
        },
    )
    evaporator_air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the DX coil draws its inlet air.'
        },
    )
    evaporator_air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the DX coil sends its outlet air.'
        },
    )
    condenser_water_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the DX coil condenser draws its inlet water. This name should match the source side outlet node name in the associated water heater tank object.'
        },
    )
    condenser_water_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the DX coil condenser sends its outlet water. This name should match the source side inlet node name in the associated water heater tank object.'
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Ambient Temperature for Crankcase Heater Operation and the DX coil...',
        },
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_ambient_temperature_for_crankcase_heater_operation: float | None = Field(
        default=10.0,
        ge=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Outdoor Temperature for Crankcase Heater Operation and the unit is...',
        },
    )
    evaporator_air_temperature_type_for_curve_objects: (
        Literal['', 'DryBulbTemperature', 'WetBulbTemperature'] | None
    ) = Field(
        default='WetBulbTemperature',
        json_schema_extra={
            'note': 'Determines temperature type for heating capacity curves and heating COP curves. This input determines whether the inlet air dry-bulb or wet-bulb temperature is used to evaluate these curves.'
        },
    )
    heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'Heating capacity modifier curve (function of temperature) should be biquadratic or cubic. Biquadratic curve = a + b(ta) + c(ta)^2 + d(tw) + e(tw)^2 + f(ta)(tw). Cubic curve = a + b(ta) + c(ta)^2 + ...',
        },
    )
    heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating capacity modifier curve (function of air flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of th...',
        },
    )
    heating_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating capacity modifier curve (function of water flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of ...',
        },
    )
    heating_cop_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'Heating COP modifier curve (function of temperature) should be biquadratic or cubic. Biquadratic curve = a + b(ta) + c(ta)^2 + d(tw) + e(tw)^2 + f(ta)(tw). Cubic curve = a + b(ta) + c(ta)^2 + d(ta)...',
        },
    )
    heating_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating COP modifier curve (function of air flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of the rat...',
        },
    )
    heating_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating COP modifier curve (function of water flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of the r...',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Part Load Fraction Correlation (function of part load ratio) should be quadratic or cubic. Quadratic curve = a + b(PLR) + c(PLR)^2. Cubic curve = a + b(PLR) + c(PLR)^2 + d(PLR)^3. PLR = part load r...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_capacity_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.heating_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.heating_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.heating_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilWaterHeatingAirToWaterHeatPumpVariableSpeed(IDFBaseModel):
    """variable-speed Heat pump water heater (VSHPWH) heating coil, air-to-water
    direct-expansion (DX) system which includes a variable-speed water heating
    coil, evaporator air coil, evaporator fan, electric compressor, and water
    pump. Part of a WaterHeater:HeatPump system."""

    _idf_object_type: ClassVar[str] = (
        'Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a variable-speed heat pump water heater DX coil.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    number_of_speeds: int | None = Field(
        default=1, ge=1, le=10, json_schema_extra={'units': 'dimensionless'}
    )
    nominal_speed_level: int | None = Field(
        default=1,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'must be lower than or equal to the highest speed number',
        },
    )
    rated_water_heating_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Water Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    rated_evaporator_inlet_air_dry_bulb_temperature: float | None = Field(
        default=19.7,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air dry-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_inlet_air_wet_bulb_temperature: float | None = Field(
        default=13.5,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air wet-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_condenser_inlet_water_temperature: float | None = Field(
        default=57.5,
        gt=25.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Condenser inlet water temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_air_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Evaporator air flow rate corresponding to rated coil performance (heating capacity, COP and SHR). Default is 5.035E-5 m3/s/W (31.25 cfm/MBH) of rated heating capacity when autocalculated.',
        },
    )
    rated_condenser_water_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Condenser water flow rate corresponding to rated coil performance (heating capacity, COP and SHR). Default is 4.487E-8 m3/s/W (0.208 gpm/MBH) of rated heating capacity when autocalculated. A warnin...',
        },
    )
    evaporator_fan_power_included_in_rated_cop: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Select Yes if the evaporator fan power is included in the rated COP. This choice field impacts the calculation of compressor electric power.'
        },
    )
    condenser_pump_power_included_in_rated_cop: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Select Yes if the condenser pump power is included in the rated COP. This choice field impacts the calculation of compressor electric power.'
        },
    )
    condenser_pump_heat_included_in_rated_heating_capacity_and_rated_cop: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='No',
        json_schema_extra={
            'note': 'Select Yes if the condenser pump heat is included in the rated heating capacity and rated COP. This choice field impacts the calculation of water heating capacity.'
        },
    )
    fraction_of_condenser_pump_heat_to_water: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Fraction of pump heat transferred to the condenser water. The pump is assumed to be located downstream of the condenser.'
        },
    )
    evaporator_air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the DX coil draws its inlet air.'
        },
    )
    evaporator_air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the DX coil sends its outlet air.'
        },
    )
    condenser_water_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the DX coil condenser draws its inlet water. This name should match the source side outlet node name in the associated water heater tank object.'
        },
    )
    condenser_water_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the DX coil condenser sends its outlet water. This name should match the source side inlet node name in the associated water heater tank object.'
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Ambient Temperature for Crankcase Heater Operation and the DX coil...',
        },
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_ambient_temperature_for_crankcase_heater_operation: float | None = Field(
        default=10.0,
        ge=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Outdoor Temperature for Crankcase Heater Operation and the unit is...',
        },
    )
    evaporator_air_temperature_type_for_curve_objects: (
        Literal['', 'DryBulbTemperature', 'WetBulbTemperature'] | None
    ) = Field(
        default='WetBulbTemperature',
        json_schema_extra={
            'note': 'Determines temperature type for heating capacity curves and heating COP curves. This input determines whether the inlet air dry-bulb or wet-bulb temperature is used to evaluate these curves.'
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used Part Load Fraction Correlation (function of part load ratio) should be quadratic or cubic. Quadratic curve = a + b(PLR) + c(PLR)^2. Cubic curve = a + b(PLR) + c...',
        },
    )
    speed_1_rated_water_heating_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_1_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_1_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_1_reference_unit_rated_air_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_reference_unit_rated_water_flow_rate: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_1_reference_unit_water_pump_input_power_at_rated_conditions: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    speed_1_total_wh_capacity_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_1_cop_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_1_cop_function_of_air_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_1_cop_function_of_water_flow_fraction_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_2_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_2_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_2_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_2_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_2_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_2_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_2_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_2_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_3_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_3_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_3_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_3_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_3_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_3_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_3_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_3_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_4_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_4_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_4_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_4_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_4_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_4_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_4_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_4_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_5_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_5_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_5_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_5_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_5_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_5_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_5_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_5_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_6_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_6_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_6_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_6_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_6_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_6_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_6_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_6_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_7_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_7_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_7_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_7_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_7_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_7_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_7_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_7_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_8_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_8_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_8_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_8_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_8_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_8_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_8_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_8_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_9_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_9_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_9_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_9_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_9_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_9_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_9_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_9_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_rated_water_heating_capacity: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    speed_10_rated_water_heating_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air and water temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include con...',
        },
    )
    speed_10_rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    speed_10_reference_unit_rated_air_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_reference_unit_rated_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    speed_10_reference_unit_water_pump_input_power_at_rated_conditions: float | None = (
        Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    )
    speed_10_total_wh_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
        },
    )
    speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )
    speed_10_cop_function_of_temperature_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Table:Lookup object can also be used curve = a + b*wb + c*wb**2 + d*ewt + e*ewt**2 + f*wb*ewt wb = entering wet-bulb temperature or dry bulb temperature upon selection (C) ewt = water entering temp...',
            },
        )
    )
    speed_10_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffa + c*ffa**2 cubic curve = a + b*ffa + c*ffa**2 + d*ffa**3 ffa = Fraction of the full load Air Flow',
        },
    )
    speed_10_cop_function_of_water_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Table:Lookup object can also be used quadratic curve = a + b*ffw + c*ffw**2 cubic curve = a + b*ffw + c*ffw**2 + d*ffw**3 ffw = Fraction of the full load Water Flow',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_1_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_1_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_1_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_2_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_2_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_2_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_3_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_3_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_3_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_4_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_4_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_4_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_5_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_5_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_5_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_5_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_5_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_6_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_6_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_6_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_6_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_6_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_7_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_7_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_7_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_7_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_7_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_8_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_8_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_8_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_8_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_8_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_9_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_9_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_9_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_9_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_9_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_total_wh_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_wh_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_total_wh_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_total_wh_capacity_function_of_water_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.speed_10_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def speed_10_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_10_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def speed_10_cop_function_of_water_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.speed_10_cop_function_of_water_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilWaterHeatingAirToWaterHeatPumpWrapped(IDFBaseModel):
    """Heat pump water heater (HPWH) heating coil, air-to-water direct-expansion
    (DX) system which includes a water heating coil, evaporator air coil,
    evaporator fan, electric compressor, and water pump. Part of a
    WaterHeater:HeatPump:WrappedCondenser system."""

    _idf_object_type: ClassVar[str] = 'Coil:WaterHeating:AirToWaterHeatPump:Wrapped'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a heat pump water heater DX coil.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rated_heating_capacity: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Heating capacity at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pump heat.',
        },
    )
    rated_cop: float | None = Field(
        default=3.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating coefficient of performance at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Can optionally include condenser pum...',
        },
    )
    rated_sensible_heat_ratio: float | None = Field(
        default=0.85,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'note': 'Gross air-side sensible heat ratio at the rated inlet air temperatures, rated condenser inlet water temperature, rated air flow rate, and rated water flow rate. Sensible heat ratio equals gross sen...'
        },
    )
    rated_evaporator_inlet_air_dry_bulb_temperature: float | None = Field(
        default=19.7,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air dry-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_inlet_air_wet_bulb_temperature: float | None = Field(
        default=13.5,
        gt=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Evaporator inlet air wet-bulb temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_condenser_water_temperature: float | None = Field(
        default=57.5,
        gt=25.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Condenser inlet water temperature corresponding to rated coil performance (heating capacity, COP and SHR).',
        },
    )
    rated_evaporator_air_flow_rate: float | Literal['Autocalculate'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Evaporator air flow rate corresponding to rated coil performance (heating capacity, COP and SHR). Default is 5.035E-5 m3/s/W (31.25 cfm/MBH) of rated heating capacity when autocalculated.',
        },
    )
    evaporator_fan_power_included_in_rated_cop: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Select Yes if the evaporator fan power is included in the rated COP. This choice field impacts the calculation of compressor electric power.'
        },
    )
    evaporator_air_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the DX coil draws its inlet air.'
        },
    )
    evaporator_air_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the DX coil sends its outlet air.'
        },
    )
    crankcase_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Ambient Temperature for Crankcase Heater Operation and the DX coil...',
        },
    )
    crankcase_heater_capacity_function_of_temperature_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'A Curve:* or Table:Lookup object encoding the relationship between the crankcase heater capacity and the outdoor air temperature. When this field is missing or empty, constant crankcase heater capa...',
        },
    )
    maximum_ambient_temperature_for_crankcase_heater_operation: float | None = Field(
        default=10.0,
        ge=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The compressor crankcase heater only operates when the dry-bulb temperature of air surrounding the compressor is below the Maximum Outdoor Temperature for Crankcase Heater Operation and the unit is...',
        },
    )
    evaporator_air_temperature_type_for_curve_objects: (
        Literal['', 'DryBulbTemperature', 'WetBulbTemperature'] | None
    ) = Field(
        default='WetBulbTemperature',
        json_schema_extra={
            'note': 'Determines temperature type for heating capacity curves and heating COP curves. This input determines whether the inlet air dry-bulb or wet-bulb temperature is used to evaluate these curves.'
        },
    )
    heating_capacity_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'Heating capacity modifier curve (function of temperature) should be biquadratic or cubic. Biquadratic curve = a + b(ta) + c(ta)^2 + d(tw) + e(tw)^2 + f(ta)(tw). Cubic curve = a + b(ta) + c(ta)^2 + ...',
        },
    )
    heating_capacity_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating capacity modifier curve (function of air flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of th...',
        },
    )
    heating_cop_function_of_temperature_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'Heating COP modifier curve (function of temperature) should be biquadratic or cubic. Biquadratic curve = a + b(ta) + c(ta)^2 + d(tw) + e(tw)^2 + f(ta)(tw). Cubic curve = a + b(ta) + c(ta)^2 + d(ta)...',
        },
    )
    heating_cop_function_of_air_flow_fraction_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Heating COP modifier curve (function of air flow fraction) should be quadratic or cubic. Quadratic curve = a + b(ff) + c(ff)^2. Cubic curve = a + b(ff) + c(ff)^2 + d(ff)^3. ff = fraction of the rat...',
        },
    )
    part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Part Load Fraction Correlation (function of part load ratio) should be quadratic or cubic. Quadratic curve = a + b(PLR) + c(PLR)^2. Cubic curve = a + b(PLR) + c(PLR)^2 + d(PLR)^3. PLR = part load r...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def crankcase_heater_capacity_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.crankcase_heater_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_capacity_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_capacity_function_of_air_flow_fraction_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_cop_function_of_temperature_curve(self) -> IDFBaseModel | None:
        v = self.heating_cop_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def heating_cop_function_of_air_flow_fraction_curve(self) -> IDFBaseModel | None:
        v = self.heating_cop_function_of_air_flow_fraction_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class CoilWaterHeatingDesuperheater(IDFBaseModel):
    """Desuperheater air heating coil. The heating energy provided by this coil is
    reclaimed from the superheated refrigerant gas leaving a compressor and does
    not impact the performance of the compressor. This coil must be used with a
    water heater tank, see Water Heater:Mixed."""

    _idf_object_type: ClassVar[str] = 'Coil:WaterHeating:Desuperheater'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Unique name for this instance of a desuperheater water heating coil.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Schedule values of 0 denote the desuperheater h...',
        },
    )
    setpoint_temperature_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': "Defines the cut-out temperature where the desuperheater water heating coil turns off. The desuperheater heating coil setpoint temperature should always be greater than the water tank's heater (elem...",
        },
    )
    dead_band_temperature_difference: float | None = Field(
        default=5.0,
        le=20.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': "Setpoint temperature minus the dead band temperature difference defines the cut-in temperature where the desuperheater water heating coil turns on. The water tank's heater (element or burner) setpo...",
        },
    )
    rated_heat_reclaim_recovery_efficiency: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'note': 'Enter the fraction of waste heat reclaimed by the desuperheater water heating coil.'
        },
    )
    rated_inlet_water_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'The inlet water temperature corresponding to the rated heat reclaim recovery efficiency.',
        },
    )
    rated_outdoor_air_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'The outdoor air dry-bulb temperature corresponding to the rated heat reclaim recovery efficiency.',
        },
    )
    maximum_inlet_water_temperature_for_heat_reclaim: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'The desuperheater water heating coil is off when the inlet water temperature is above the maximum inlet water temperature for heat reclaim.',
        },
    )
    heat_reclaim_efficiency_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'A biquadratic curve defining the performance of the desuperheater heating coil. Performance can be specified as a function of inlet water temperature, outdoor air dry-bulb temperature, or both. Cur...',
        },
    )
    water_inlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node from which the desuperheater heating coil draws its inlet water. This name should match the source side outlet node name in the associated water heater tank object.'
        },
    )
    water_outlet_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The node to which the desuperheater heating coil sends its outlet water. This name should match the source side inlet node name in the associated water heater tank object.'
        },
    )
    tank_object_type: (
        Literal['', 'WaterHeater:Mixed', 'WaterHeater:Stratified'] | None
    ) = Field(
        default='WaterHeater:Mixed',
        json_schema_extra={
            'note': 'Specify the type of water heater tank used by this desuperheater water heating coil.'
        },
    )
    tank_name: WaterHeaterMixedNamesRef | WaterHeaterStratifiedNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['WaterHeaterMixedNames', 'WaterHeaterStratifiedNames'],
            'note': 'The name of the water heater tank used by this desuperheater water heating coil. Needs to match the name used in the corresponding water heater object.',
        },
    )
    heating_source_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:MultiSpeed',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:TwoSpeed',
        'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
        'Coil:Cooling:DX:VariableSpeed',
        'Coil:Cooling:WaterToAirHeatPump:EquationFit',
        'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
        'Refrigeration:CompressorRack',
        'Refrigeration:Condenser:AirCooled',
        'Refrigeration:Condenser:EvaporativeCooled',
        'Refrigeration:Condenser:WaterCooled',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'The type of DX system that is providing waste heat for reclaim.'
        },
    )
    heating_source_name: (
        CoilCoolingDXRef
        | DesuperHeatingCoilSourcesRef
        | DesuperHeatingWaterOnlySourcesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoilCoolingDX',
                'DesuperHeatingCoilSources',
                'DesuperHeatingWaterOnlySources',
            ],
            'note': 'The name of the DX system used for heat reclaim.',
        },
    )
    water_flow_rate: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'The operating water flow rate.'},
    )
    water_pump_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The water circulation pump electric power.',
        },
    )
    fraction_of_pump_heat_to_water: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'The fraction of pump heat transferred to the water. The pump is assumed to be downstream of the desuperheater water heating coil.'
        },
    )
    on_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power consumed when the desuperheater water heating coil operates. Parasitic electric load does not contribute to water heating or the zone air heat balance.',
        },
    )
    off_cycle_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric load consumed when the desuperheater water heating coil is off. Parasitic electric load does not contribute to water heating or the zone air heat balance. Off-cycle parasitic pow...',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def setpoint_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.setpoint_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heat_reclaim_efficiency_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heat_reclaim_efficiency_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def tank(self) -> IDFBaseModel | None:
        v = self.tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['WaterHeaterMixedNames', 'WaterHeaterStratifiedNames']
        )

    @property
    def heating_source(self) -> IDFBaseModel | None:
        v = self.heating_source_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v,
            [
                'CoilCoolingDX',
                'DesuperHeatingCoilSources',
                'DesuperHeatingWaterOnlySources',
            ],
        )
