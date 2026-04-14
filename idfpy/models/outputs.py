"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 26.1.
Group: Output Reporting
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ColorSchemesRef,
    ScheduleNamesRef,
)


class MeterCustomVariableDetailsItem(IDFBaseModel):
    """Nested object type for array items."""

    key_name: str | None = Field(default=None)
    output_variable_or_meter_name: str | None = Field(default=None)


class OutputDiagnosticsDiagnosticsItem(IDFBaseModel):
    """Nested object type for array items."""

    key: (
        Literal[
            'DisplayAdvancedReportVariables',
            'DisplayAllWarnings',
            'DisplayExtraWarnings',
            'DisplayUnusedObjects',
            'DisplayUnusedSchedules',
            'DisplayWeatherMissingDataWarnings',
            'DisplayZoneAirHeatBalanceOffBalance',
            'DoNotMirrorAttachedShading',
            'DoNotMirrorDetachedShading',
            'ReportDetailedWarmupConvergence',
            'ReportDuringHVACSizingSimulation',
            'ReportDuringWarmup',
        ]
        | None
    ) = Field(default=None)


class OutputTableAnnualVariableDetailsItem(IDFBaseModel):
    """Nested object type for array items."""

    variable_or_meter_or_ems_variable_or_field_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'contain the name of a variable (see Output:Variable and eplusout.rdd), meter (see Output:Meter and eplusout.mdd), or EMS Internal Variable Name or IDF Object Field name. This value is shown using t...'
        },
    )
    aggregation_type_for_variable_or_meter: (
        Literal[
            'HourInTenBinsMinToMax',
            'HourInTenBinsMinToZero',
            'HourInTenBinsZeroToMax',
            'HoursNegative',
            'HoursNonNegative',
            'HoursNonPositive',
            'HoursNonZero',
            'HoursPositive',
            'HoursZero',
            'Maximum',
            'MaximumDuringHoursShown',
            'Minimum',
            'MinimumDuringHoursShown',
            'SumOrAverage',
            'SumOrAverageDuringHoursShown',
            'ValueWhenMaximumOrMinimum',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'The method of aggregation for the selected variable or meter. SumOrAverage adds up the values for every timestep in the month if the variable is a sum variable. If the variable is an average variab...'
        },
    )
    digits_after_decimal: int | None = Field(default=2, ge=0, le=10)


class OutputTableMonthlyVariableDetailsItem(IDFBaseModel):
    """Nested object type for array items."""

    variable_or_meter_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The name of an output variable or  meter that is available in the RDD file.'
        },
    )
    aggregation_type_for_variable_or_meter: (
        Literal[
            'HoursNegative',
            'HoursNonNegative',
            'HoursNonPositive',
            'HoursNonZero',
            'HoursPositive',
            'HoursZero',
            'Maximum',
            'MaximumDuringHoursShown',
            'Minimum',
            'MinimumDuringHoursShown',
            'SumOrAverage',
            'SumOrAverageDuringHoursShown',
            'ValueWhenMaximumOrMinimum',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'The method of aggregation for the selected variable or meter. SumOrAverage adds up the values for every timestep in the month if the variable is a sum variable. If the variable is an average variab...'
        },
    )


class OutputTableSummaryReportsReportsItem(IDFBaseModel):
    """Nested object type for array items."""

    report_name: (
        Literal[
            'AdaptiveComfortSummary',
            'AirLoopComponentLoadSummary',
            'AirLoopSystemComponentEnergyUseMonthly',
            'AirLoopSystemComponentLoadsMonthly',
            'AirLoopSystemEnergyAndWaterUseMonthly',
            'AllMonthly',
            'AllSummary',
            'AllSummaryAndMonthly',
            'AllSummaryAndSizingPeriod',
            'AllSummaryMonthlyAndSizingPeriod',
            'AnnualBuildingUtilityPerformanceSummary',
            'AverageOutdoorConditionsMonthly',
            'BoilerReportMonthly',
            'CO2ResilienceSummary',
            'ChillerReportMonthly',
            'ClimaticDataSummary',
            'CoilReportMonthly',
            'CoilSizingDetails',
            'ComfortReportSimple55Monthly',
            'ComponentCostEconomicsSummary',
            'ComponentSizingSummary',
            'CondLoopDemandReportMonthly',
            'DXReportMonthly',
            'DaylightingReportMonthly',
            'DemandEndUseComponentsSummary',
            'EconomicResultSummary',
            'ElectricComponentsOfPeakDemandMonthly',
            'EndUseEnergyConsumptionCoalMonthly',
            'EndUseEnergyConsumptionDieselMonthly',
            'EndUseEnergyConsumptionElectricityMonthly',
            'EndUseEnergyConsumptionFuelOilMonthly',
            'EndUseEnergyConsumptionGasolineMonthly',
            'EndUseEnergyConsumptionNaturalGasMonthly',
            'EndUseEnergyConsumptionOtherFuelsMonthly',
            'EndUseEnergyConsumptionPropaneMonthly',
            'EnergyConsumptionCoalGasolineMonthly',
            'EnergyConsumptionDieselFuelOilMonthly',
            'EnergyConsumptionDistrictHeatingCoolingMonthly',
            'EnergyConsumptionElectricityGeneratedPropaneMonthly',
            'EnergyConsumptionElectricityNaturalGasMonthly',
            'EnergyConsumptionOtherFuelsMonthly',
            'EnergyMeters',
            'EnvelopeSummary',
            'EquipmentSummary',
            'FacilityComponentLoadSummary',
            'FanReportMonthly',
            'GeneratorReportMonthly',
            'HVACSizingSummary',
            'HeatEmissionsReportMonthly',
            'HeatEmissionsSummary',
            'InitializationSummary',
            'InputVerificationandResultsSummary',
            'LEEDSummary',
            'LifeCycleCostReport',
            'LightingSummary',
            'MechanicalVentilationLoadsMonthly',
            'ObjectCountSummary',
            'OccupantComfortDataSummaryMonthly',
            'OutdoorAirDetails',
            'OutdoorAirSummary',
            'OutdoorConditionsMaximumDewPointMonthly',
            'OutdoorConditionsMaximumDryBulbMonthly',
            'OutdoorConditionsMaximumWetBulbMonthly',
            'OutdoorConditionsMinimumDryBulbMonthly',
            'OutdoorGroundConditionsMonthly',
            'PeakEnergyEndUseCoalMonthly',
            'PeakEnergyEndUseDieselMonthly',
            'PeakEnergyEndUseElectricityPart1Monthly',
            'PeakEnergyEndUseElectricityPart2Monthly',
            'PeakEnergyEndUseFuelOilMonthly',
            'PeakEnergyEndUseGasolineMonthly',
            'PeakEnergyEndUseNaturalGasMonthly',
            'PeakEnergyEndUseOtherFuelsMonthly',
            'PeakEnergyEndUsePropaneMonthly',
            'PeakSpaceGainsMonthly',
            'PlantLoopDemandReportMonthly',
            'PumpReportMonthly',
            'SensibleHeatGainSummary',
            'SetpointsNotMetWithTemperaturesMonthly',
            'ShadingSummary',
            'SourceEnergyEndUseComponentsSummary',
            'SpaceGainComponentsAtCoolingPeakMonthly',
            'SpaceGainsMonthly',
            'Standard62.1Summary',
            'SurfaceShadowingSummary',
            'SystemSummary',
            'TariffReport',
            'ThermalResilienceSummary',
            'TowerReportMonthly',
            'UnglazedTranspiredSolarCollectorSummaryMonthly',
            'VisualResilienceSummary',
            'WaterHeaterReportMonthly',
            'WindowACReportMonthly',
            'WindowEnergyReportMonthly',
            'WindowEnergyZoneSummaryMonthly',
            'WindowReportMonthly',
            'WindowZoneSummaryMonthly',
            'ZoneComponentLoadSummary',
            'ZoneCoolingSummaryMonthly',
            'ZoneElectricSummaryMonthly',
            'ZoneHeatingSummaryMonthly',
            'ZoneTemperatureOscillationReportMonthly',
        ]
        | None
    ) = Field(default=None)


class EnvironmentalImpactFactors(IDFBaseModel):
    """Used to help convert district and ideal energy use to a fuel type and
    provide total carbon equivalent with coefficients Also used in Source=>Site
    conversions."""

    _idf_object_type: ClassVar[str] = 'EnvironmentalImpactFactors'
    district_heating_water_efficiency: float | None = Field(
        default=0.3,
        gt=0.0,
        json_schema_extra={
            'note': 'District heating efficiency used when converted to natural gas'
        },
    )
    district_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'District cooling COP used when converted to electricity',
        },
    )
    district_heating_steam_conversion_efficiency: float | None = Field(
        default=0.25,
        gt=0.0,
        json_schema_extra={
            'note': 'Steam conversion efficiency used to convert steam usage to natural gas'
        },
    )
    total_carbon_equivalent_emission_factor_from_n2o: float | None = Field(
        default=80.7272, json_schema_extra={'units': 'kg/kg'}
    )
    total_carbon_equivalent_emission_factor_from_ch4: float | None = Field(
        default=6.2727, json_schema_extra={'units': 'kg/kg'}
    )
    total_carbon_equivalent_emission_factor_from_co2: float | None = Field(
        default=0.2727, json_schema_extra={'units': 'kg/kg'}
    )


class FuelFactors(IDFBaseModel):
    """Provides Fuel Factors for Emissions as well as Source=>Site conversions.
    OtherFuel1, OtherFuel2 provide options for users who want to create and use
    fuels that may not be mainstream (biomass, wood, pellets)."""

    _idf_object_type: ClassVar[str] = 'FuelFactors'
    existing_fuel_resource_name: (
        Literal[
            'Coal',
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
    ) = Field(default=None)
    source_energy_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'J/J'}
    )
    source_energy_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    co2_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    co2_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    co_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    co_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ch4_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    ch4_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    nox_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    nox_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    n2o_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    n2o_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    so2_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    so2_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    pm_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    pm_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    pm10_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    pm10_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    pm2_5_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    pm2_5_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    nh3_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    nh3_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    nmvoc_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    nmvoc_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    hg_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    hg_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    pb_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    pb_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    water_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'L/MJ'}
    )
    water_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    nuclear_high_level_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'g/MJ'}
    )
    nuclear_high_level_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    nuclear_low_level_emission_factor: float | None = Field(
        default=None, json_schema_extra={'units': 'm3/MJ'}
    )
    nuclear_low_level_emission_factor_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )

    @property
    def source_energy_schedule(self) -> IDFBaseModel | None:
        v = self.source_energy_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def co2_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.co2_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def co_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.co_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def ch4_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.ch4_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def nox_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.nox_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def n2o_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.n2o_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def so2_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.so2_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def pm_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.pm_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def pm10_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.pm10_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def pm2_5_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.pm2_5_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def nh3_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.nh3_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def nmvoc_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.nmvoc_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def hg_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.hg_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def pb_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.pb_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def water_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.water_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def nuclear_high_level_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.nuclear_high_level_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def nuclear_low_level_emission_factor_schedule(self) -> IDFBaseModel | None:
        v = self.nuclear_low_level_emission_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class MeterCustom(IDFBaseModel):
    """Used to allow users to combine specific variables and/or meters into
    \"custom\" meter configurations. To access these meters by name, one must
    first run a simulation to generate the RDD/MDD files and names. A
    Meter:Custom cannot reference another Meter:Custom."""

    _idf_object_type: ClassVar[str] = 'Meter:Custom'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    resource_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'Generic',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    variable_details: list[MeterCustomVariableDetailsItem] | None = Field(default=None)


class MeterCustomDecrement(IDFBaseModel):
    """Used to allow users to combine specific variables and/or meters into
    \"custom\" meter configurations. To access these meters by name, one must
    first run a simulation to generate the RDD/MDD files and names."""

    _idf_object_type: ClassVar[str] = 'Meter:CustomDecrement'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    resource_type: (
        Literal[
            'Coal',
            'Diesel',
            'DistrictCooling',
            'DistrictHeatingSteam',
            'DistrictHeatingWater',
            'Electricity',
            'FuelOilNo1',
            'FuelOilNo2',
            'Gasoline',
            'Generic',
            'NaturalGas',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
            'Water',
        ]
        | None
    ) = Field(default=None)
    source_meter_name: str = Field(...)
    variable_details: list[MeterCustomVariableDetailsItem] | None = Field(default=None)


class OutputConstructions(IDFBaseModel):
    """Adds a report to the eio output file which shows details for each
    construction, including overall properties, a list of material layers, and
    calculated results related to conduction transfer functions."""

    _idf_object_type: ClassVar[str] = 'Output:Constructions'
    details_type_1: Literal['Constructions', 'Materials'] | None = Field(default=None)
    details_type_2: Literal['Constructions', 'Materials'] | None = Field(default=None)


class OutputControlFiles(IDFBaseModel):
    """Conditionally turn on/off output from EnergyPlus."""

    _idf_object_type: ClassVar[str] = 'OutputControl:Files'
    output_csv: Literal['', 'No', 'Yes'] | None = Field(default='No')
    output_mtr: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_eso: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_eio: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_tabular: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_sqlite: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_json: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_audit: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_space_sizing: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_zone_sizing: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_system_sizing: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_dxf: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_bnd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_rdd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_mdd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_mtd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_end: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_shd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_dfs: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_glhe: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_delightin: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_delighteldmp: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_delightdfdmp: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_edd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_dbg: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_perflog: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_sln: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_sci: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_wrl: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_screen: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_extshd: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_tarcog: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes', json_schema_extra={'note': 'Not Implemented Yet'}
    )
    output_plant_component_sizing: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes', json_schema_extra={'note': 'epluspsz.csv'}
    )


class OutputControlReportingTolerances(IDFBaseModel):
    """Calculations of the time that setpoints are not met use a tolerance of 0.2C.
    This object allows changing the tolerance used to determine when setpoints
    are being met."""

    _idf_object_type: ClassVar[str] = 'OutputControl:ReportingTolerances'
    tolerance_for_time_heating_setpoint_not_met: float | None = Field(
        default=0.2,
        ge=0.0,
        le=10.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'If the zone temperature is below the heating setpoint by more than this value, the following output variables will increment as appropriate Zone Heating Setpoint Not Met Time Zone Heating Setpoint ...',
        },
    )
    tolerance_for_time_cooling_setpoint_not_met: float | None = Field(
        default=0.2,
        ge=0.0,
        le=10.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'If the zone temperature is above the cooling setpoint by more than this value, the following output variables will increment as appropriate Zone Cooling Setpoint Not Met Time Zone Cooling Setpoint ...',
        },
    )


class OutputControlResilienceSummaries(IDFBaseModel):
    """Specifies methods for resilience reporting variables"""

    _idf_object_type: ClassVar[str] = 'OutputControl:ResilienceSummaries'
    heat_index_algorithm: Literal['', 'Extended', 'Simplified'] | None = Field(
        default='Simplified',
        json_schema_extra={
            'note': 'Whether the simplified or the extended method should be used for heat index Simplified: based on regression analysis carried out by Lans P. Rothfusz Extended: Based on paper by Lu & Romps'
        },
    )


class OutputControlSurfaceColorScheme(IDFBaseModel):
    """This object is used to set colors for reporting on various building elements
    particularly for the DXF reports. We know the user can enter 0 to 255 and
    the color map is available in DXF output. Therefore, we are limiting the
    colors in that range. You can extend by editing the IDD but you do so on
    your own. Colors not changed in any scheme will remain as the default scheme
    uses."""

    _idf_object_type: ClassVar[str] = 'OutputControl:SurfaceColorScheme'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'choose a name or use one of the DataSets'}
    )
    drawing_element_1_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_1: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_2_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_2: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_3_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_3: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_4_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_4: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_5_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_5: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_6_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_6: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_7_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_7: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_8_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_8: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_9_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_9: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_10_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_10: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_11_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_11: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_12_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_12: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_13_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_13: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_14_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_14: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )
    drawing_element_15_type: (
        Literal[
            'AttachedBuildingShades',
            'DaylightReferencePoint1',
            'DaylightReferencePoint2',
            'DetachedBuildingShades',
            'DetachedFixedShades',
            'Doors',
            'Floors',
            'GlassDoors',
            'Photovoltaics',
            'Roofs',
            'Text',
            'TubularDaylightDiffusers',
            'TubularDaylightDomes',
            'Walls',
            'Windows',
        ]
        | None
    ) = Field(default=None)
    color_for_drawing_element_15: int | None = Field(
        default=None,
        ge=0,
        le=255,
        json_schema_extra={'note': 'use color number for output assignment (e.g. DXF)'},
    )


class OutputControlTableStyle(IDFBaseModel):
    """default style for the OutputControl:Table:Style is comma -- this works well
    for importing into spreadsheet programs such as Excel(tm) but not so well
    for word processing programs -- there tab may be a better choice. fixed puts
    spaces between the \"columns\". HTML produces tables in HTML. XML produces
    an XML file. note - if no OutputControl:Table:Style is included, the
    defaults are comma and None."""

    _idf_object_type: ClassVar[str] = 'OutputControl:Table:Style'
    column_separator: (
        Literal[
            '',
            'All',
            'Comma',
            'CommaAndHTML',
            'CommaAndXML',
            'Fixed',
            'HTML',
            'Tab',
            'TabAndHTML',
            'XML',
            'XMLandHTML',
        ]
        | None
    ) = Field(default='Comma')
    unit_conversion: (
        Literal[
            '',
            'InchPound',
            'InchPoundExceptElectricity',
            'JtoGJ',
            'JtoKWH',
            'JtoMJ',
            'None',
        ]
        | None
    ) = Field(default='None')
    format_numeric_values: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If No, all digits are shown after the decimal point without any rounding (23.238769213). If Yes, values are rounded for readability (23.24).'
        },
    )


class OutputControlTimestamp(IDFBaseModel):
    """Control timestamp format, currently applies only to JSON and native CSV (not
    CSV via ReadVars)"""

    _idf_object_type: ClassVar[str] = 'OutputControl:Timestamp'
    iso_8601_format: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Use the ISO 8601 format YYYY-MM-DDThh:mm:ss'},
    )
    timestamp_at_beginning_of_interval: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Determines where the timestamp is produced, either at the beginning (Yes) or end (No) of the interval'
        },
    )


class OutputDebuggingData(IDFBaseModel):
    """switch eplusout.dbg file on or off"""

    _idf_object_type: ClassVar[str] = 'Output:DebuggingData'
    report_debugging_data: Literal['', 'No', 'Yes'] | None = Field(default='No')
    report_during_warmup: Literal['', 'No', 'Yes'] | None = Field(default='No')


class OutputDiagnostics(IDFBaseModel):
    """Special keys to produce certain warning messages or effect certain
    simulation characteristics."""

    _idf_object_type: ClassVar[str] = 'Output:Diagnostics'
    diagnostics: list[OutputDiagnosticsDiagnosticsItem] | None = Field(default=None)


class OutputEnergyManagementSystem(IDFBaseModel):
    """This object is used to control the output produced by the Energy Management
    System"""

    _idf_object_type: ClassVar[str] = 'Output:EnergyManagementSystem'
    actuator_availability_dictionary_reporting: (
        Literal['', 'None', 'NotByUniqueKeyNames', 'Verbose'] | None
    ) = Field(default='None')
    internal_variable_availability_dictionary_reporting: (
        Literal['', 'None', 'NotByUniqueKeyNames', 'Verbose'] | None
    ) = Field(default='None')
    ems_runtime_language_debug_output_level: (
        Literal['', 'ErrorsOnly', 'None', 'Verbose'] | None
    ) = Field(default='None')


class OutputEnvironmentalImpactFactors(IDFBaseModel):
    """This is used to Automatically report the facility meters and turn on the
    Environmental Impact Report calculations for all of the Environmental
    Factors."""

    _idf_object_type: ClassVar[str] = 'Output:EnvironmentalImpactFactors'
    reporting_frequency: (
        Literal[
            'Annual',
            'Daily',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same. Detailed is not a valid choice.'
        },
    )


class OutputJSON(IDFBaseModel):
    """Output from EnergyPlus can be written to JSON format files."""

    _idf_object_type: ClassVar[str] = 'Output:JSON'
    option_type: Literal['TimeSeries', 'TimeSeriesAndTabular'] = Field(...)
    output_json: Literal['', 'No', 'Yes'] | None = Field(default='Yes')
    output_cbor: Literal['', 'No', 'Yes'] | None = Field(default='No')
    output_messagepack: Literal['', 'No', 'Yes'] | None = Field(default='No')
    unit_conversion_for_tabular_data: (
        Literal[
            '',
            'InchPound',
            'InchPoundExceptElectricity',
            'JtoGJ',
            'JtoKWH',
            'JtoMJ',
            'None',
            'UseOutputControlTableStyle',
        ]
        | None
    ) = Field(
        default='UseOutputControlTableStyle',
        json_schema_extra={
            'note': 'Unit conversion option used when writing JSON Tabular Data This option applies to TabularData and TabularDatawithString in the JSON file(s)'
        },
    )
    format_numeric_values_for_tabular_data: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If No, all digits are shown after the decimal point without any rounding (23.238769213). If Yes, values are rounded for readability (23.24).'
        },
    )


class OutputMeter(IDFBaseModel):
    """Each Output:Meter command picks meters to be put onto the standard output
    file (.eso) and meter file (.mtr). Not all meters are reported in every
    simulation. A list of meters that can be reported are available after a run
    on the meter dictionary file (.mdd) if the Output:VariableDictionary has
    been requested."""

    _idf_object_type: ClassVar[str] = 'Output:Meter'
    key_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters or EndUse:..., e.g. GeneralLights:* for all General Lights Output:Meter puts results on both the eplusout.mtr and eplusout.e...'
        },
    )
    reporting_frequency: (
        Literal[
            '',
            'Annual',
            'Daily',
            'Detailed',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same'
        },
    )


class OutputMeterCumulative(IDFBaseModel):
    """Each Output:Meter:Cumulative command picks meters to be reported
    cumulatively onto the standard output file (.eso) and meter file (.mtr). Not
    all meters are reported in every simulation. a list of meters that can be
    reported are available after a run on the meter dictionary file (.mdd) if
    the Output:VariableDictionary has been requested."""

    _idf_object_type: ClassVar[str] = 'Output:Meter:Cumulative'
    key_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters or EndUse:..., e.g. GeneralLights:* for all General Lights Output:Meter:Cumulative puts results on both the eplusout.mtr and...'
        },
    )
    reporting_frequency: (
        Literal[
            '',
            'Annual',
            'Daily',
            'Detailed',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same'
        },
    )


class OutputMeterCumulativeMeterFileOnly(IDFBaseModel):
    """Each Output:Meter:Cumulative:MeterFileOnly command picks meters to be
    reported cumulatively onto the standard output file (.eso) and meter file
    (.mtr). Not all meters are reported in every simulation. a list of meters
    that can be reported are available after a run on the meter dictionary file
    (.mdd) if the Output:VariableDictionary has been requested."""

    _idf_object_type: ClassVar[str] = 'Output:Meter:Cumulative:MeterFileOnly'
    key_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters or EndUse:..., e.g. GeneralLights:* for all General Lights Output:Meter:Cumulative:MeterFileOnly puts results on the eplusou...'
        },
    )
    reporting_frequency: (
        Literal[
            '',
            'Annual',
            'Daily',
            'Detailed',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same'
        },
    )


class OutputMeterMeterFileOnly(IDFBaseModel):
    """Each Output:Meter:MeterFileOnly command picks meters to be put only onto
    meter file (.mtr). Not all meters are reported in every simulation. A list
    of meters that can be reported a list of meters that can be reported are
    available after a run on the meter dictionary file (.mdd) if the
    Output:VariableDictionary has been requested."""

    _idf_object_type: ClassVar[str] = 'Output:Meter:MeterFileOnly'
    key_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Form is EnergyUseType:..., e.g. Electricity:* for all Electricity meters or EndUse:..., e.g. GeneralLights:* for all General Lights Output:Meter:MeterFileOnly puts results on the eplusout.mtr file ...'
        },
    )
    reporting_frequency: (
        Literal[
            '',
            'Annual',
            'Daily',
            'Detailed',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same'
        },
    )


class OutputPreprocessorMessage(IDFBaseModel):
    """This object does not come from a user input. This is generated by a pre-
    processor so that various conditions can be gracefully passed on by the
    InputProcessor."""

    _idf_object_type: ClassVar[str] = 'Output:PreprocessorMessage'
    preprocessor_name: str | None = Field(default=None)
    error_severity: Literal['Fatal', 'Information', 'Severe', 'Warning'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Depending on type, InputProcessor may terminate the program.'
        },
    )
    message_line_1: str | None = Field(default=None)
    message_line_2: str | None = Field(default=None)
    message_line_3: str | None = Field(default=None)
    message_line_4: str | None = Field(default=None)
    message_line_5: str | None = Field(default=None)
    message_line_6: str | None = Field(default=None)
    message_line_7: str | None = Field(default=None)
    message_line_8: str | None = Field(default=None)
    message_line_9: str | None = Field(default=None)
    message_line_10: str | None = Field(default=None)


class OutputSQLite(IDFBaseModel):
    """Output from EnergyPlus can be written to an SQLite format file."""

    _idf_object_type: ClassVar[str] = 'Output:SQLite'
    option_type: Literal['Simple', 'SimpleAndTabular'] | None = Field(default=None)
    unit_conversion_for_tabular_data: (
        Literal[
            '',
            'InchPound',
            'InchPoundExceptElectricity',
            'JtoGJ',
            'JtoKWH',
            'JtoMJ',
            'None',
            'UseOutputControlTableStyle',
        ]
        | None
    ) = Field(
        default='UseOutputControlTableStyle',
        json_schema_extra={
            'note': 'Unit conversion option used when writing SQLite Tabular Data This option applies to TabularData and TabularDatawithString in the SQLite file'
        },
    )
    format_numeric_values_for_tabular_data: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If No, all digits are shown after the decimal point without any rounding (23.238769213). If Yes, values are rounded for readability (23.24).'
        },
    )


class OutputSchedules(IDFBaseModel):
    """Produces a condensed reporting that illustrates the full range of schedule
    values in the eio output file. In the style of input: DaySchedule,
    WeekSchedule, and Annual Schedule."""

    _idf_object_type: ClassVar[str] = 'Output:Schedules'
    key_field: Literal['Hourly', 'Timestep'] = Field(...)


class OutputSurfacesDrawing(IDFBaseModel):
    """Produces reports/files that are capable of rendering graphically or being
    imported into other programs. Rendering does not alter the actual
    inputs/surfaces."""

    _idf_object_type: ClassVar[str] = 'Output:Surfaces:Drawing'
    report_type: Literal['DXF', 'DXF:WireFrame', 'VRML'] = Field(...)
    report_specifications_1: (
        Literal['', 'RegularPolyline', 'ThickPolyline', 'Triangulate3DFace'] | None
    ) = Field(
        default='Triangulate3DFace',
        json_schema_extra={
            'note': 'Triangulate3DFace (default), ThickPolyline, RegularPolyline apply to DXF This field is ignored for DXF:WireFrame and VRML'
        },
    )
    report_specifications_2: ColorSchemesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ColorSchemes'],
            'note': 'Use ColorScheme Name for DXF reports',
        },
    )

    @property
    def report_specifications_2_ref(self) -> OutputControlSurfaceColorScheme | None:
        v = self.report_specifications_2
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ColorSchemes'])


class OutputSurfacesList(IDFBaseModel):
    """Produces a report summarizing the details of surfaces in the eio output
    file."""

    _idf_object_type: ClassVar[str] = 'Output:Surfaces:List'
    report_type: Literal[
        'CostInfo',
        'DecayCurvesFromComponentLoadsSummary',
        'Details',
        'DetailsWithVertices',
        'Lines',
        'Vertices',
        'ViewFactorInfo',
    ] = Field(...)
    report_specifications: Literal['IDF'] | None = Field(
        default=None,
        json_schema_extra={
            'note': '(IDF, only for Output:Surfaces:List, Lines report -- will print transformed coordinates in IDF style)'
        },
    )


class OutputTableAnnual(IDFBaseModel):
    """Provides a generic method of setting up tables of annual results with one
    row per object. The report has multiple columns that are each defined using
    a repeated group of fields for any number of columns. A single
    Output:Table:Annual produces a single table in the output."""

    _idf_object_type: ClassVar[str] = 'Output:Table:Annual'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    filter: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'An optional text string that is compared to the names of the objects referenced by the variables and if they match are included in the table. A footnote will appear that indicates that the objects ...'
        },
    )
    schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Optional schedule name. If left blank, aggregation is performed for all hours simulated. If a schedule is specified, aggregation is performed for non-zero hours in the schedule.',
        },
    )
    variable_details: list[OutputTableAnnualVariableDetailsItem] | None = Field(
        default=None
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class OutputTableMonthly(IDFBaseModel):
    """Provides a generic method of setting up tables of monthly results. The
    report has multiple columns that are each defined using a repeated group of
    fields for any number of columns. A single Output:Table:Monthly object often
    produces multiple tables in the output. A table is produced for every
    instance of a particular output variable. For example, a table defined with
    zone variables will be produced once for every zone."""

    _idf_object_type: ClassVar[str] = 'Output:Table:Monthly'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    digits_after_decimal: int | None = Field(default=2, ge=0, le=10)
    variable_details: list[OutputTableMonthlyVariableDetailsItem] | None = Field(
        default=None
    )


class OutputTableReportPeriod(IDFBaseModel):
    """This object allows the user to generate the resilience tabular reports over
    a subset of a run period. When it is defined, a series of reporting-period-
    specific resilience summary tables will be generated at the end of all
    tabular reports. Multiple reporting periods may be input."""

    _idf_object_type: ClassVar[str] = 'Output:Table:ReportPeriod'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'descriptive name cannot be blank and must be unique'
        },
    )
    report_name: (
        Literal[
            'AllResilienceSummaries',
            'CO2ResilienceSummary',
            'ThermalResilienceSummary',
            'VisualResilienceSummary',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'currently only allow for these tables, could be extended in the future'
        },
    )
    begin_year: int | None = Field(
        default=None,
        json_schema_extra={'note': 'start year of reporting, if specified'},
    )
    begin_month: int = Field(..., ge=1, le=12)
    begin_day_of_month: int = Field(..., ge=1, le=31)
    begin_hour_of_day: int = Field(..., ge=1, le=24)
    end_year: int | None = Field(
        default=None,
        json_schema_extra={'note': 'start year of reporting, if specified'},
    )
    end_month: int = Field(..., ge=1, le=12)
    end_day_of_month: int = Field(..., ge=1, le=31)
    end_hour_of_day: int = Field(..., ge=1, le=24)


class OutputTableSummaryReports(IDFBaseModel):
    """This object allows the user to call report types that are predefined and
    will appear with the other tabular reports. These predefined reports are
    sensitive to the OutputControl:Table:Style object and appear in the same
    files as the tabular reports. The entries for this object is a list of the
    predefined reports that should appear in the tabular report output file."""

    _idf_object_type: ClassVar[str] = 'Output:Table:SummaryReports'
    reports: list[OutputTableSummaryReportsReportsItem] | None = Field(default=None)


class OutputTableTimeBins(IDFBaseModel):
    """Produces a bin report in the table output file which shows the amount of
    time in hours that occurs in different bins for a single specific output
    variable or meter. Two different types of binning are reported: by month and
    by hour of the day."""

    _idf_object_type: ClassVar[str] = 'Output:Table:TimeBins'
    key_value: str | None = Field(
        default='*',
        json_schema_extra={
            'note': "use '*' (without quotes) to apply this variable to all keys"
        },
    )
    variable_name: str = Field(...)
    interval_start: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The lowest value for the intervals being binned into.'
        },
    )
    interval_size: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the bins starting with Interval start.'
        },
    )
    interval_count: int | None = Field(
        default=None,
        ge=1,
        le=20,
        json_schema_extra={
            'note': 'The number of bins used. The number of hours below the start of the Lowest bin and above the value of the last bin are also shown.'
        },
    )
    schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Optional schedule name. Binning is performed for non-zero hours. Binning always performed if left blank.',
        },
    )
    variable_type: (
        Literal['Energy', 'Power', 'Temperature', 'VolumetricFlow'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Optional input on the type of units for the variable used by other fields in the object.'
        },
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class OutputVariable(IDFBaseModel):
    """each Output:Variable command picks variables to be put onto the standard
    output file (.eso) some variables may not be reported for every simulation.
    a list of variables that can be reported are available after a run on the
    report dictionary file (.rdd) if the Output:VariableDictionary has been
    requested."""

    _idf_object_type: ClassVar[str] = 'Output:Variable'
    key_value: str | None = Field(
        default='*',
        json_schema_extra={
            'note': "use '*' (without quotes) to apply this variable to all keys"
        },
    )
    variable_name: str = Field(...)
    reporting_frequency: (
        Literal[
            '',
            'Annual',
            'Daily',
            'Detailed',
            'Environment',
            'Hourly',
            'Monthly',
            'RunPeriod',
            'Timestep',
        ]
        | None
    ) = Field(
        default='Hourly',
        json_schema_extra={
            'note': 'Detailed lists every instance (i.e. HVAC variable timesteps) Timestep refers to the zone Timestep/Number of Timesteps in hour value RunPeriod and Environment are the same'
        },
    )
    schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class OutputVariableDictionary(IDFBaseModel):
    """Produces a list summarizing the output variables and meters that are
    available for reporting for the model being simulated (rdd output file). The
    list varies depending on the types of objects present in the idf file. For
    example, variables related to lights will only appear if a Lights object is
    present. The IDF option generates complete Output:Variable objects to
    simplify adding the desired output to the idf file."""

    _idf_object_type: ClassVar[str] = 'Output:VariableDictionary'
    key_field: Literal['', 'IDF', 'regular'] | None = Field(default='regular')
    sort_option: Literal['Name', 'Unsorted'] | None = Field(default=None)
