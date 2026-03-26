"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Economics
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ScheduleNamesRef,
    UtilityCostTariffsRef,
)


class LifeCycleCostUseAdjustmentMultipliersItem(IDFBaseModel):
    """Nested object type for array items."""

    year_multiplier: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The multiplier to be applied to the end-use cost for the first year in the service period. The total utility costs for the selected end-use is multiplied by this value. For no change enter 1.0.'
        },
    )


class LifeCycleCostUsePriceEscalationEscalationsItem(IDFBaseModel):
    """Nested object type for array items."""

    year_escalation: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The escalation in price of the energy or water use for the first year expressed as a decimal.'
        },
    )


class ComponentCostAdjustments(IDFBaseModel):
    """Used to perform various modifications to the construction costs to arrive at
    an estimate for total project costs. This object allows extending the line
    item model so that the overall costs of the project will reflect various
    profit and fees."""

    _idf_object_type: ClassVar[str] = 'ComponentCost:Adjustments'
    miscellaneous_cost_per_conditioned_area: float | None = Field(
        default=None,
        json_schema_extra={
            'units': '$/m2',
            'note': 'based on conditioned floor area for cost not accounted for in current line item cost model',
        },
    )
    design_and_engineering_fees: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    contractor_fee: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    contingency: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    permits_bonding_and_insurance: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    commissioning_fee: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    regional_adjustment_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'for use with average data in line item and Misc cost models',
        },
    )


class ComponentCostLineItem(IDFBaseModel):
    """Each instance of this object creates a cost line item and will contribute to
    the total for a cost estimate."""

    _idf_object_type: ClassVar[str] = 'ComponentCost:LineItem'
    name: str | None = Field(default=None)
    type: str | None = Field(default=None)
    line_item_type: Literal[
        'Chiller:Electric',
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:DX',
        'Coil:Heating:Fuel',
        'Construction',
        'Daylighting:Controls',
        'General',
        'Generator:Photovoltaic',
        'Lights',
        'Shading:Zone:Detailed',
    ] = Field(
        ..., json_schema_extra={'note': 'extend choice-keys as Cases are added to code'}
    )
    item_name: str = Field(
        ...,
        json_schema_extra={'note': 'wildcard "*" is acceptable for some components'},
    )
    object_end_use_key: str | None = Field(
        default=None, json_schema_extra={'note': 'not yet used'}
    )
    cost_per_each: float | None = Field(default=None, json_schema_extra={'units': '$'})
    cost_per_area: float | None = Field(
        default=None, json_schema_extra={'units': '$/m2'}
    )
    cost_per_unit_of_output_capacity: float | None = Field(
        default=None, json_schema_extra={'units': '$/kW'}
    )
    cost_per_unit_of_output_capacity_per_cop: float | None = Field(
        default=None,
        json_schema_extra={'units': '$/kW', 'note': 'The value is per change in COP.'},
    )
    cost_per_volume: float | None = Field(
        default=None, json_schema_extra={'units': '$/m3'}
    )
    cost_per_volume_rate: float | None = Field(
        default=None, json_schema_extra={'units': '$/(m3/s)'}
    )
    cost_per_energy_per_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': '$/(W/K)',
            'note': 'as in for use with UA sizing of Coils',
        },
    )
    quantity: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'optional for use with Cost per Each and "General" object Type',
        },
    )


class ComponentCostReference(IDFBaseModel):
    """Used to allow comparing the current cost estimate to the results of a
    previous estimate for a reference building. This object parallels the
    ComponentCost:Adjustments object but adds a field for entering the cost line
    item model result for the reference building. The factors entered in this
    object are applied to the reference building while the factors listed in the
    ComponentCost:Adjustments object are applied to the current building model
    cost estimate."""

    _idf_object_type: ClassVar[str] = 'ComponentCost:Reference'
    reference_building_line_item_costs: float | None = Field(
        default=None,
        json_schema_extra={
            'units': '$',
            'note': 'should be comparable to the components in current line item cost model',
        },
    )
    reference_building_miscellaneous_cost_per_conditioned_area: float | None = Field(
        default=None,
        json_schema_extra={
            'units': '$/m2',
            'note': 'based on conditioned floor area for cost not accounted for in reference line item costs',
        },
    )
    reference_building_design_and_engineering_fees: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    reference_building_contractor_fee: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    reference_building_contingency: float | None = Field(default=None)
    reference_building_permits_bonding_and_insurance: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    reference_building_commissioning_fee: float | None = Field(
        default=None, json_schema_extra={'units': 'dimensionless'}
    )
    reference_building_regional_adjustment_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'for use with average data in line item and Misc cost models',
        },
    )


class CurrencyType(IDFBaseModel):
    """If CurrencyType is not specified, it will default to USD and produce $ in
    the reports."""

    _idf_object_type: ClassVar[str] = 'CurrencyType'
    monetary_unit: Literal[
        'AFN',
        'ALL',
        'ANG',
        'ARS',
        'AUD',
        'AWG',
        'AZN',
        'BAM',
        'BBD',
        'BGN',
        'BMD',
        'BND',
        'BOB',
        'BRL',
        'BSD',
        'BWP',
        'BYR',
        'BZD',
        'CAD',
        'CHF',
        'CLP',
        'CNY',
        'COP',
        'CRC',
        'CUP',
        'CZK',
        'DKK',
        'DOP',
        'EEK',
        'EGP',
        'EUR',
        'FJD',
        'GBP',
        'GHC',
        'GIP',
        'GTQ',
        'GYD',
        'HKD',
        'HNL',
        'HRK',
        'HUF',
        'IDR',
        'ILS',
        'IMP',
        'INR',
        'IRR',
        'ISK',
        'JEP',
        'JMD',
        'JPY',
        'KGS',
        'KHR',
        'KPW',
        'KRW',
        'KYD',
        'KZT',
        'LAK',
        'LBP',
        'LKR',
        'LRD',
        'LTL',
        'LVL',
        'MKD',
        'MNT',
        'MUR',
        'MXN',
        'MYR',
        'MZN',
        'NAD',
        'NGN',
        'NIO',
        'NOK',
        'NPR',
        'NZD',
        'OMR',
        'PAB',
        'PEN',
        'PHP',
        'PKR',
        'PLN',
        'PYG',
        'QAR',
        'RON',
        'RSD',
        'RUB',
        'SAR',
        'SBD',
        'SCR',
        'SEK',
        'SGD',
        'SHP',
        'SOS',
        'SRD',
        'SVC',
        'SYP',
        'THB',
        'TRL',
        'TRY',
        'TTD',
        'TVD',
        'TWD',
        'UAH',
        'USD',
        'UYU',
        'UZS',
        'VEF',
        'VND',
        'XCD',
        'YER',
        'ZAR',
        'ZWD',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'The commonly used three letter currency code for the units of money for the country or region. Based on ISO 4217 currency codes. Common currency codes are USD for $ and EUR for Euros.'
        },
    )


class LifeCycleCostNonrecurringCost(IDFBaseModel):
    """A non-recurring cost happens only once during the study period. For costs
    that occur more than once during the study period on a regular schedule, use
    the LifeCycleCost:RecurringCost object."""

    _idf_object_type: ClassVar[str] = 'LifeCycleCost:NonrecurringCost'
    name: str = Field(...)
    category: Literal['', 'Construction', 'OtherCapital', 'Salvage'] | None = Field(
        default='Construction'
    )
    cost: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the non-recurring cost value. For construction and other capital costs the value entered is typically a positive value. For salvage costs the value entered is typically a negative value which...'
        },
    )
    start_of_costs: Literal['', 'BasePeriod', 'ServicePeriod'] | None = Field(
        default='ServicePeriod',
        json_schema_extra={
            'note': 'Enter when the costs start. The First Year of Cost is based on the number of years past the Start of Costs. For most non-recurring costs the Start of Costs should be Base Period which begins at the...'
        },
    )
    years_from_start: int | None = Field(
        default=None,
        ge=0,
        le=100,
        json_schema_extra={
            'note': 'This field and the Months From Start field together represent the time from either the start of the Service Period on the service month and year or start of the Base Period on the base month and ye...'
        },
    )
    months_from_start: int | None = Field(
        default=None,
        ge=0,
        le=1200,
        json_schema_extra={
            'note': 'This field and the Years From Start field together represent the time from either the start of the Service Period on the service month and year or start of the Base Period on the base month and yea...'
        },
    )


class LifeCycleCostParameters(IDFBaseModel):
    """Provides inputs related to the overall life-cycle analysis. It establishes
    many of the assumptions used in computing the present value. It is important
    that when comparing the results of multiple simulations that the fields in
    the LifeCycleCost:Parameters objects are the same for all the simulations.
    When this object is present the tabular report file will contain the Life-
    Cycle Cost Report."""

    _idf_object_type: ClassVar[str] = 'LifeCycleCost:Parameters'
    name: str = Field(...)
    discounting_convention: (
        Literal['', 'BeginningOfYear', 'EndOfYear', 'MidYear'] | None
    ) = Field(
        default='EndOfYear',
        json_schema_extra={
            'note': 'The field specifies if the discounting of future costs should be computed as occurring at the end of each year or the middle of each year or the beginning of each year. The most common discounting ...'
        },
    )
    inflation_approach: Literal['', 'ConstantDollar', 'CurrentDollar'] | None = Field(
        default='ConstantDollar',
        json_schema_extra={
            'note': 'This field is used to determine if the analysis should use constant dollars or current dollars which is related to how inflation is treated. If ConstantDollar is selected then the Real Discount Rat...'
        },
    )
    real_discount_rate: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the real discount rate as a decimal. For a 3% rate enter the value 0.03. This input is used when the Inflation Approach is ConstantDollar. The real discount rate reflects the interest rates n...'
        },
    )
    nominal_discount_rate: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the nominal discount rate as a decimal. For a 5% rate enter the value 0.05. This input is used when the Inflation Approach is CurrentDollar. The real discount rate reflects the interest rates...'
        },
    )
    inflation: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the rate of inflation for general goods and services as a decimal. For a 2% rate enter the value 0.02.'
        },
    )
    base_date_month: (
        Literal[
            '',
            'April',
            'August',
            'December',
            'February',
            'January',
            'July',
            'June',
            'March',
            'May',
            'November',
            'October',
            'September',
        ]
        | None
    ) = Field(
        default='January',
        json_schema_extra={
            'note': 'Enter the month that is the beginning of study period also known as the beginning of the base period.'
        },
    )
    base_date_year: int | None = Field(
        default=None,
        ge=1900,
        le=2100,
        json_schema_extra={
            'note': 'Enter the four digit year that is the beginning of study period such as 2010. The study period is also known as the base period.'
        },
    )
    service_date_month: (
        Literal[
            '',
            'April',
            'August',
            'December',
            'February',
            'January',
            'July',
            'June',
            'March',
            'May',
            'November',
            'October',
            'September',
        ]
        | None
    ) = Field(
        default='January',
        json_schema_extra={
            'note': 'Enter the month that is the beginning of building occupancy. Energy costs computed by EnergyPlus are assumed to occur during the year following the service date. The service date must be the same o...'
        },
    )
    service_date_year: int | None = Field(
        default=None,
        ge=1900,
        le=2100,
        json_schema_extra={
            'note': 'Enter the four digit year that is the beginning of occupancy such as 2010.'
        },
    )
    length_of_study_period_in_years: int | None = Field(
        default=None,
        ge=1,
        le=100,
        json_schema_extra={
            'note': 'Enter the number of years of the study period. It is the number of years that the study continues based on the start at the base date. The default value is 25 years. Only integers may be used indic...'
        },
    )
    tax_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the overall marginal tax rate for the project costs. This does not include energy or water taxes. The tax rate entered should be based on the marginal tax rate for the entity and not the aver...'
        },
    )
    depreciation_method: (
        Literal[
            '',
            'ModifiedAcceleratedCostRecoverySystem-10year',
            'ModifiedAcceleratedCostRecoverySystem-15year',
            'ModifiedAcceleratedCostRecoverySystem-20year',
            'ModifiedAcceleratedCostRecoverySystem-3year',
            'ModifiedAcceleratedCostRecoverySystem-5year',
            'ModifiedAcceleratedCostRecoverySystem-7year',
            'None',
            'StraightLine-27year',
            'StraightLine-31year',
            'StraightLine-39year',
            'StraightLine-40year',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'For an analysis that includes income tax impacts this entry describes how capital costs are depreciated. Only one depreciation method may be used for an analysis and is applied to all capital expen...'
        },
    )


class LifeCycleCostRecurringCosts(IDFBaseModel):
    """Recurring costs are costs that repeat over time on a regular schedule during
    the study period. If costs associated with equipment do repeat but not on a
    regular schedule, use LifeCycleCost:NonrecurringCost objects instead."""

    _idf_object_type: ClassVar[str] = 'LifeCycleCost:RecurringCosts'
    name: str = Field(...)
    category: (
        Literal[
            '',
            'Maintenance',
            'MajorOverhaul',
            'MinorOverhaul',
            'Operation',
            'OtherOperational',
            'Repair',
            'Replacement',
        ]
        | None
    ) = Field(default='Maintenance')
    cost: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter the cost in dollars (or the appropriate monetary unit) for the recurring costs. Enter the cost for each time it occurs. For example if the annual maintenance cost is 500 dollars enter 500 here.'
        },
    )
    start_of_costs: Literal['', 'BasePeriod', 'ServicePeriod'] | None = Field(
        default='ServicePeriod',
        json_schema_extra={
            'note': 'Enter when the costs start. The First Year of Cost is based on the number of years past the Start of Costs. For most maintenance costs the Start of Costs should be Service Period.'
        },
    )
    years_from_start: int | None = Field(
        default=None,
        ge=0,
        le=100,
        json_schema_extra={
            'note': 'This field and the Months From Start field together represent the time from either the start of the Service Period on the service month and year or start of the Base Period on the base month and ye...'
        },
    )
    months_from_start: int | None = Field(
        default=None,
        ge=0,
        le=1200,
        json_schema_extra={
            'note': 'This field and the Years From Start field together represent the time from either the start of the Service Period on the service month and year or start of the Base Period on the base month and yea...'
        },
    )
    repeat_period_years: int | None = Field(
        default=1,
        ge=0,
        le=100,
        json_schema_extra={
            'note': 'This field and the Repeat Period Months field indicate how much time elapses between re-occurrences of the cost. For costs that occur every year such the Repeat Period Years should be 1 and Repeat ...'
        },
    )
    repeat_period_months: int | None = Field(
        default=0,
        ge=0,
        le=1200,
        json_schema_extra={
            'note': 'This field and the Repeat Period Years field indicate how much time elapses between re-occurrences of the cost. Only integers should be entered representing whole years. The Repeat Period Years (ti...'
        },
    )
    annual_escalation_rate: float | None = Field(
        default=None,
        ge=-0.3,
        le=0.3,
        json_schema_extra={
            'note': 'Enter the annual escalation rate as a decimal. For a 1% rate enter the value 0.01. This input is used when the Inflation Approach is CurrentDollar. When Inflation Approach is set to ConstantDollar ...'
        },
    )


class LifeCycleCostUseAdjustment(IDFBaseModel):
    """Used by advanced users to adjust the energy or water use costs for future
    years. This should not be used for compensating for inflation but should
    only be used to increase the costs of energy or water based on assumed
    changes to the actual usage, such as anticipated changes in the future
    function of the building. The adjustments begin at the start of the service
    period."""

    _idf_object_type: ClassVar[str] = 'LifeCycleCost:UseAdjustment'
    name: str = Field(...)
    resource: Literal[
        'Coal',
        'Diesel',
        'DistrictCooling',
        'DistrictHeatingSteam',
        'DistrictHeatingWater',
        'Electricity',
        'ElectricityNet',
        'ElectricityProduced',
        'ElectricityPurchased',
        'ElectricitySurplusSold',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
        'Water',
    ] = Field(...)
    multipliers: list[LifeCycleCostUseAdjustmentMultipliersItem] | None = Field(
        default=None
    )


class LifeCycleCostUsePriceEscalation(IDFBaseModel):
    """Life cycle cost escalation factors. The values for this object may be found
    in the annual supplement to NIST Handbook 135 in Tables Ca-1 to Ca-5 and are
    included in an EnergyPlus dataset file."""

    _idf_object_type: ClassVar[str] = 'LifeCycleCost:UsePriceEscalation'
    lcc_price_escalation_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The identifier used for the object. The name usually identifies the location (such as the state or region or country or census area) that the escalations apply to. In addition the name should ident...'
        },
    )
    resource: Literal[
        'Coal',
        'Diesel',
        'DistrictCooling',
        'DistrictHeatingSteam',
        'DistrictHeatingWater',
        'Electricity',
        'ElectricityNet',
        'ElectricityProduced',
        'ElectricityPurchased',
        'ElectricitySurplusSold',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
        'Water',
    ] = Field(...)
    escalation_start_year: int | None = Field(
        default=None,
        ge=1900,
        le=2100,
        json_schema_extra={
            'note': 'This field and the Escalation Start Month define the time that corresponds to Year 1 Escalation such as 2010 when the escalation rates are applied. This field and the Escalation Start Month define ...'
        },
    )
    escalation_start_month: (
        Literal[
            '',
            'April',
            'August',
            'December',
            'February',
            'January',
            'July',
            'June',
            'March',
            'May',
            'November',
            'October',
            'September',
        ]
        | None
    ) = Field(
        default='January',
        json_schema_extra={
            'note': 'This field and the Escalation Start Year define the time that corresponds to Year 1 Escalation such as 2010 when the escalation rates are applied. This field and the Escalation Start Year define th...'
        },
    )
    escalations: list[LifeCycleCostUsePriceEscalationEscalationsItem] | None = Field(
        default=None
    )


class UtilityCostChargeBlock(IDFBaseModel):
    """Used to compute energy and demand charges (or any other charges) that are
    structured in blocks of charges. Multiple UtilityCost:Charge:Block objects
    may be defined for a single tariff and they will be added together."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Charge:Block'
    utility_cost_charge_block_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Charge Variable Name This is the name associated with the UtilityCost:Charge:Block object and will appear in the report. In addition the results of the UtilityCost:Charge:Block are stored in a vari...'
        },
    )
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Block.',
        },
    )
    source_variable: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of the source used by the UtilityCost:Charge:Block. This is usually the name of the variable holding the energy or demand but may also be the name of any variable including the subtotal or...'
        },
    )
    season: Literal['', 'Annual', 'Fall', 'Spring', 'Summer', 'Winter'] | None = Field(
        default='Annual',
        json_schema_extra={
            'note': 'If this is set to annual the calculations are performed for the UtilityCost:Charge:Block for the entire year (all months) otherwise it is calculated only for those months in the season defined.'
        },
    )
    category_variable_name: Literal[
        'Adjustment',
        'Basis',
        'DemandCharges',
        'EnergyCharges',
        'NotIncluded',
        'ServiceCharges',
        'Subtotal',
        'Surcharge',
        'Taxes',
        'Total',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'This field shows where the charge should be added. The reason to enter this field appropriately is so that the charge gets reported in a reasonable category. The charge automatically gets added to ...'
        },
    )
    remaining_into_variable: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If the blocks do not use all of the energy or demand from the source some energy and demand remains then the remaining amount should be assigned to a variable. If no variable is assigned and some a...'
        },
    )
    block_size_multiplier_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The sizes of the blocks are usually used directly but if a value or a variable is entered here the block sizes entered in the rest of the charge are first multiplied by the entered value prior to b...'
        },
    )
    block_size_1_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_1_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_2_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_2_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_3_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_3_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_4_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_4_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_5_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_5_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_6_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_6_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_7_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_7_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_8_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_8_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_9_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_9_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_10_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_10_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_11_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_11_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_12_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_12_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_13_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_13_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_14_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_14_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )
    block_size_15_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The size of the block of the charges is entered here. For most rates that use multiple blocks this will be the value for the block size. Using remaining may be used when the remaining amount should...'
        },
    )
    block_15_cost_per_unit_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The cost of the block. This field is unusual for the EnergyPlus syntax because it can be either a number or a name of a variable.'
        },
    )


class UtilityCostChargeSimple(IDFBaseModel):
    """UtilityCost:Charge:Simple is one of the most often used objects for tariff
    calculation. It is used to compute energy and demand charges that are very
    simple. It may also be used for taxes, surcharges and any other charges that
    occur on a utility bill. Multiple UtilityCost:Charge:Simple objects may be
    defined for a single tariff and they will be added together."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Charge:Simple'
    utility_cost_charge_simple_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Charge Variable Name This is the name associated with the UtilityCost:Charge:Simple object and will appear in the report. In addition the results of the UtilityCost:Charge:Simple calculation are st...'
        },
    )
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Charge:Simple.',
        },
    )
    source_variable: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of the source used by the UtilityCost:Charge:Simple. This is usually the name of the variable holding the energy or demand but may also be the name of any variable including the subtotal o...'
        },
    )
    season: Literal['Annual', 'Fall', 'Spring', 'Summer', 'Winter'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If this is set to annual the calculations are performed for the UtilityCost:Charge:Simple for the entire year (all months) otherwise it is calculated only for those months in the season defined.'
        },
    )
    category_variable_name: Literal[
        'Adjustment',
        'Basis',
        'DemandCharges',
        'EnergyCharges',
        'NotIncluded',
        'ServiceCharges',
        'Subtotal',
        'Surcharge',
        'Taxes',
        'Total',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'This field shows where the charge should be added. The reason to enter this field appropriately is so that the charge gets reported in a reasonable category. The charge automatically gets added to ...'
        },
    )
    cost_per_unit_value_or_variable_name: float | str = Field(
        ...,
        json_schema_extra={
            'note': 'This field contains either a single number or the name of a variable. The number is multiplied with all of the energy or demand or other source that is specified in the source field. If a variable ...'
        },
    )


class UtilityCostComputation(IDFBaseModel):
    """The object lists a series of computations that are used to perform the
    utility bill calculation. The object is only used for complex tariffs that
    cannot be modeled any other way. For most utility tariffs,
    UtilityCost:Computation is unnecessary and should be avoided. If
    UtilityCost:Computation is used, it must contain references to all objects
    involved in the rate in the order that they should be computed."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Computation'
    name: str = Field(...)
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.',
        },
    )
    compute_step_1: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Contain a simple language that describes the steps used in the computation process similar to a programming language.'
        },
    )
    compute_step_2: str | None = Field(default=None)
    compute_step_3: str | None = Field(default=None)
    compute_step_4: str | None = Field(default=None)
    compute_step_5: str | None = Field(default=None)
    compute_step_6: str | None = Field(default=None)
    compute_step_7: str | None = Field(default=None)
    compute_step_8: str | None = Field(default=None)
    compute_step_9: str | None = Field(default=None)
    compute_step_10: str | None = Field(default=None)
    compute_step_11: str | None = Field(default=None)
    compute_step_12: str | None = Field(default=None)
    compute_step_13: str | None = Field(default=None)
    compute_step_14: str | None = Field(default=None)
    compute_step_15: str | None = Field(default=None)
    compute_step_16: str | None = Field(default=None)
    compute_step_17: str | None = Field(default=None)
    compute_step_18: str | None = Field(default=None)
    compute_step_19: str | None = Field(default=None)
    compute_step_20: str | None = Field(default=None)
    compute_step_21: str | None = Field(default=None)
    compute_step_22: str | None = Field(default=None)
    compute_step_23: str | None = Field(default=None)
    compute_step_24: str | None = Field(default=None)
    compute_step_25: str | None = Field(default=None)
    compute_step_26: str | None = Field(default=None)
    compute_step_27: str | None = Field(default=None)
    compute_step_28: str | None = Field(default=None)
    compute_step_29: str | None = Field(default=None)
    compute_step_30: str | None = Field(default=None)


class UtilityCostQualify(IDFBaseModel):
    """The qualify object allows only tariffs to be selected based on limits which
    may apply such as maximum or minimum demand requirements. If the results of
    the simulation fall outside of the range of qualifications, that tariff is
    still calculated but the \"Qualified\" entry will say \"No\" and the
    UtilityCost:Qualify that caused its exclusion is shown. Multiple
    UtilityCost:Qualify objects can appear for the same tariff and they can be
    based on any variable."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Qualify'
    utility_cost_qualify_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Displayed in the report if the tariff does not qualify'
        },
    )
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Qualify.',
        },
    )
    variable_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of the variable used. For energy and demand the automatically created variables totalEnergy and totalDemand should be used respectively.'
        },
    )
    qualify_type: Literal['', 'Maximum', 'Minimum'] | None = Field(default='Maximum')
    threshold_value_or_variable_name: float | str = Field(
        ...,
        json_schema_extra={
            'note': 'The minimum or maximum value for the qualify. If the variable has values that are less than this value when the qualify type is minimum then the tariff may be disqualified. If the variable has valu...'
        },
    )
    season: Literal['Annual', 'Fall', 'Spring', 'Summer', 'Winter'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If the UtilityCost:Qualify only applies to a season enter the season name. If this field is left blank it defaults to Annual.'
        },
    )
    threshold_test: Literal['', 'Consecutive', 'Count'] | None = Field(
        default='Consecutive',
        json_schema_extra={
            'note': 'Uses the number in Number of Months in one of two different ways depending on the Threshold  Test. If the Threshold Test is set to Count then the qualification is based on the count of the total nu...'
        },
    )
    number_of_months: float | None = Field(
        default=None,
        ge=1.0,
        le=12.0,
        json_schema_extra={
            'note': 'A number from 1 to 12. If no value entered 12 is assumed when the qualify type is minimum and 1 when the qualify type is maximum. This is the number of months that the threshold test applies to det...'
        },
    )


class UtilityCostRatchet(IDFBaseModel):
    """Allows the modeling of tariffs that include some type of seasonal
    ratcheting. Ratchets are most common when used with electric demand charges.
    A ratchet is when a utility requires that the demand charge for a month with
    a low demand may be increased to be more consistent with a month that set a
    higher demand charge."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Ratchet'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Ratchet Variable Name The name of the ratchet and the name of the result of this single ratchet.'
        },
    )
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Ratchet.',
        },
    )
    baseline_source_variable: str = Field(
        ...,
        json_schema_extra={
            'note': 'When the ratcheted value exceeds the baseline value for a month the ratcheted value is used but when the baseline value is greater then the ratcheted value the baseline value is used. Usually the e...'
        },
    )
    adjustment_source_variable: str = Field(
        ...,
        json_schema_extra={
            'note': 'The variable that the ratchet is calculated from. It is often but not always the same as the baseline source variable. The ratcheting calculations using offset and multiplier are using the values f...'
        },
    )
    season_from: (
        Literal['Annual', 'Fall', 'Monthly', 'Spring', 'Summer', 'Winter'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'The name of the season that is being examined. The maximum value for all of the months in the named season is what is used with the multiplier and offset. This is most commonly Summer or Annual. Wh...'
        },
    )
    season_to: Literal['Annual', 'Fall', 'Spring', 'Summer', 'Winter'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The name of the season when the ratchet would be calculated. This is most commonly Winter. The ratchet only is applied to the months in the named season. The resulting variable for months not in th...'
        },
    )
    multiplier_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Often the ratchet has a clause such as "the current month demand or 90% of the summer month demand". For this case a value of 0.9 would be entered here as the multiplier. This value may be left bla...'
        },
    )
    offset_value_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'A less common strategy is to say that the ratchet must be all demand greater than a value in this case an offset that is added to the demand may be entered here. If entered it is common for the off...'
        },
    )


class UtilityCostTariff(IDFBaseModel):
    """Defines the name of a utility cost tariff, the type of tariff, and other
    details about the overall tariff. Each other object that is part of the
    tariff model references the tariff name. See UtilityCost:Charge:Simple,
    UtilityCost:Charge:Block, UtilityCost:Ratchet, UtilityCost:Qualify,
    UtilityCost:Variable and UtilityCost:Computation objects."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Tariff'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of the tariff. Tariffs are sometimes called rates. The name is used in identifying the output results and in associating all of the charges and other objects that make up a tariff.'
        },
    )
    output_meter_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'The name of any standard meter or custom meter or but usually set to either Electricity:Facility or Gas:Facility'
        },
    )
    conversion_factor_choice: (
        Literal[
            'CCF',
            'MCF',
            'MJ',
            'MMBtu',
            'Therm',
            'UserDefined',
            'gal',
            'kBtu',
            'kWh',
            'kgal',
            'm3',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'A choice that allows several different predefined conversion factors to be used; otherwise user defined conversion factors are used as defined in the next two fields. If left blank m3 is used for w...'
        },
    )
    energy_conversion_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Is a multiplier used to convert energy into the units specified by the utility in their tariff. If left blank it defaults to 1 (no conversion). This field should will be used only if Conversion Fac...'
        },
    )
    demand_conversion_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Is a multiplier used to convert demand into the units specified by the utility in their tariff. If left blank it defaults to 1 (no conversion). This field should will be used only if Conversion Fac...'
        },
    )
    time_of_use_period_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of the schedule that defines the time-of-use periods that occur each day. The values for the different variables are: 1 for Peak. 2 for Shoulder. 3 for OffPeak. 4 for MidPeak. The followin...',
        },
    )
    season_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of a schedule that defines the seasons. The schedule values are: 1 for Winter. 2 for Spring. 3 for Summer. 4 for Autumn. Variables are automatically created if a season schedule is used. T...',
        },
    )
    month_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The name of the schedule that defines the billing periods of the year. Normally this entry is allowed to default and a schedule will be internally used that has the breaks between billing periods o...',
        },
    )
    demand_window_length: (
        Literal['Day', 'FullHour', 'HalfHour', 'QuarterHour', 'Week'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'The determination of demand can vary by utility. Some utilities use the peak instantaneous demand measured but most use a fifteen minute average demand or a one hour average demand. Some gas utilit...'
        },
    )
    monthly_charge_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The fixed monthly service charge that many utilities have. The entry may be numeric and gets added to the ServiceCharges variable or if a variable name is entered here its values for each month are...'
        },
    )
    minimum_monthly_charge_or_variable_name: float | str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The minimum total charge for the tariff or if a variable name is entered here its values for each month are used.'
        },
    )
    real_time_pricing_charge_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used with real time pricing rates. The name of a schedule that contains the cost of energy for that particular time period of the year. Real time rates can be modeled using a charge schedule with t...',
        },
    )
    customer_baseline_load_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used with real time pricing rates. The name of a schedule that contains the baseline energy use for the customer. Many real time rates apply the charges as a credit or debit only to the difference ...',
        },
    )
    group_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'The group name of the tariff such as distribution transmission supplier etc. If more than one tariff with the same group name is present and qualifies only the lowest cost tariff is used. Usually t...'
        },
    )
    buy_or_sell: (
        Literal['', 'BuyFromUtility', 'NetMetering', 'SellToUtility'] | None
    ) = Field(
        default='BuyFromUtility',
        json_schema_extra={
            'note': 'Sets whether the tariff is used for buying selling or both to the utility. This should be allowed to default to buyFromUtility unless a power generation system is included in the building that may ...'
        },
    )


class UtilityCostVariable(IDFBaseModel):
    """Allows for the direct entry of monthly values into a utility tariff
    variable."""

    _idf_object_type: ClassVar[str] = 'UtilityCost:Variable'
    name: str = Field(...)
    tariff_name: UtilityCostTariffsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UtilityCostTariffs'],
            'note': 'The name of the UtilityCost:Tariff that is associated with this UtilityCost:Variable.',
        },
    )
    variable_type: (
        Literal['', 'Currency', 'Demand', 'Dimensionless', 'Energy'] | None
    ) = Field(default='Dimensionless')
    january_value: float | None = Field(default=None)
    february_value: float | None = Field(default=None)
    march_value: float | None = Field(default=None)
    april_value: float | None = Field(default=None)
    may_value: float | None = Field(default=None)
    june_value: float | None = Field(default=None)
    july_value: float | None = Field(default=None)
    august_value: float | None = Field(default=None)
    september_value: float | None = Field(default=None)
    october_value: float | None = Field(default=None)
    november_value: float | None = Field(default=None)
    december_value: float | None = Field(default=None)
