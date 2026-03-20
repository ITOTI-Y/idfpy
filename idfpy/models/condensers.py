"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Condenser Equipment and Heat Exchangers
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ConstructionNamesRef,
    GroundHeatExchangerVerticalArrayNamesRef,
    GroundHeatExchangerVerticalPropertiesNamesRef,
    GroundHeatExchangerVerticalResponseFactorNamesRef,
    GroundHeatExchangerVerticalSingleNamesRef,
    ScheduleNamesRef,
    UndisturbedGroundTempModelsRef,
    UnivariateFunctionsRef,
    VariableSpeedTowerCoefficientRef,
    WaterStorageTankNamesRef,
)


class GroundHeatExchangerResponseFactorsGFunctionsItem(IDFBaseModel):
    """Nested object type for array items."""
    g_function_ln_t_ts_value: float = Field(...)
    g_function_g_value: float = Field(...)


class GroundHeatExchangerSystemVerticalWellLocationsItem(IDFBaseModel):
    """Nested object type for array items."""
    ghe_vertical_single_object_name: GroundHeatExchangerVerticalSingleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['GroundHeatExchangerVerticalSingleNames']})



class CoolingTowerPerformanceCoolTools(IDFBaseModel):
    """This object is used to define coefficients for the approach temperature
correlation for a variable speed cooling tower when tower Model Type is
specified as CoolToolsUserDefined in the object CoolingTower:VariableSpeed."""

    _idf_object_type: ClassVar[str] = "CoolingTowerPerformance:CoolTools"
    name: str = Field(...)
    minimum_inlet_air_wet_bulb_temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'Minimum valid inlet air wet-bulb temperature for this approach temperature correlation.'})
    maximum_inlet_air_wet_bulb_temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'Maximum valid inlet air wet-bulb temperature for this approach temperature correlation.'})
    minimum_range_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Minimum valid range temperature for this approach temperature correlation.'})
    maximum_range_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Maximum valid range temperature for this approach temperature correlation.'})
    minimum_approach_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Minimum valid approach temperature for this correlation.'})
    maximum_approach_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Maximum valid approach temperature for this correlation.'})
    minimum_water_flow_rate_ratio: float = Field(..., json_schema_extra={'note': 'Minimum valid water flow rate ratio for this approach temperature correlation.'})
    maximum_water_flow_rate_ratio: float = Field(..., json_schema_extra={'note': 'Maximum valid water flow rate ratio for this approach temperature correlation.'})
    coefficient_1: float = Field(...)
    coefficient_2: float = Field(...)
    coefficient_3: float = Field(...)
    coefficient_4: float = Field(...)
    coefficient_5: float = Field(...)
    coefficient_6: float = Field(...)
    coefficient_7: float = Field(...)
    coefficient_8: float = Field(...)
    coefficient_9: float = Field(...)
    coefficient_10: float = Field(...)
    coefficient_11: float = Field(...)
    coefficient_12: float = Field(...)
    coefficient_13: float = Field(...)
    coefficient_14: float = Field(...)
    coefficient_15: float = Field(...)
    coefficient_16: float = Field(...)
    coefficient_17: float = Field(...)
    coefficient_18: float = Field(...)
    coefficient_19: float = Field(...)
    coefficient_20: float = Field(...)
    coefficient_21: float = Field(...)
    coefficient_22: float = Field(...)
    coefficient_23: float = Field(...)
    coefficient_24: float = Field(...)
    coefficient_25: float = Field(...)
    coefficient_26: float = Field(...)
    coefficient_27: float = Field(...)
    coefficient_28: float = Field(...)
    coefficient_29: float = Field(...)
    coefficient_30: float = Field(...)
    coefficient_31: float = Field(...)
    coefficient_32: float = Field(...)
    coefficient_33: float = Field(...)
    coefficient_34: float = Field(...)
    coefficient_35: float = Field(...)


class CoolingTowerPerformanceYorkCalc(IDFBaseModel):
    """This object is used to define coefficients for the approach temperature
correlation for a variable speed cooling tower when tower Model Type is
specified as YorkCalcUserDefined in the object CoolingTower:VariableSpeed."""

    _idf_object_type: ClassVar[str] = "CoolingTowerPerformance:YorkCalc"
    name: str = Field(...)
    minimum_inlet_air_wet_bulb_temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'Minimum valid inlet air wet-bulb temperature for this approach temperature correlation.'})
    maximum_inlet_air_wet_bulb_temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'Maximum valid inlet air wet-bulb temperature for this approach temperature correlation.'})
    minimum_range_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Minimum valid range temperature for this approach temperature correlation.'})
    maximum_range_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Maximum valid range temperature for this approach temperature correlation.'})
    minimum_approach_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Minimum valid approach temperature for this correlation.'})
    maximum_approach_temperature: float = Field(..., json_schema_extra={'units': 'deltaC', 'note': 'Maximum valid approach temperature for this correlation.'})
    minimum_water_flow_rate_ratio: float = Field(..., json_schema_extra={'note': 'Minimum valid water flow rate ratio for this approach temperature correlation.'})
    maximum_water_flow_rate_ratio: float = Field(..., json_schema_extra={'note': 'Maximum valid water flow rate ratio for this approach temperature correlation.'})
    maximum_liquid_to_gas_ratio: float = Field(..., json_schema_extra={'note': 'Maximum liquid (water) to gas (air) ratio for this approach temperature correlation.'})
    coefficient_1: float = Field(...)
    coefficient_2: float = Field(...)
    coefficient_3: float = Field(...)
    coefficient_4: float = Field(...)
    coefficient_5: float = Field(...)
    coefficient_6: float = Field(...)
    coefficient_7: float = Field(...)
    coefficient_8: float = Field(...)
    coefficient_9: float = Field(...)
    coefficient_10: float = Field(...)
    coefficient_11: float = Field(...)
    coefficient_12: float = Field(...)
    coefficient_13: float = Field(...)
    coefficient_14: float = Field(...)
    coefficient_15: float = Field(...)
    coefficient_16: float = Field(...)
    coefficient_17: float = Field(...)
    coefficient_18: float = Field(...)
    coefficient_19: float = Field(...)
    coefficient_20: float = Field(...)
    coefficient_21: float = Field(...)
    coefficient_22: float = Field(...)
    coefficient_23: float = Field(...)
    coefficient_24: float = Field(...)
    coefficient_25: float = Field(...)
    coefficient_26: float = Field(...)
    coefficient_27: float = Field(...)


class CoolingTowerSingleSpeed(IDFBaseModel):
    """This tower model is based on Merkel's theory, which is also the basis for
the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is
modeled as a counter flow heat exchanger with a single-speed fan drawing air
through the tower (induced-draft configuration). Added fluid bypass as an
additional capacity control. 8/2008. For a multi-cell tower, the capacity
and air/water flow rate inputs are for the entire tower."""

    _idf_object_type: ClassVar[str] = "CoolingTower:SingleSpeed"
    name: str = Field(..., json_schema_extra={'note': 'Tower Name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water outlet node'})
    design_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Leave field blank if tower performance input method is NominalCapacity'})
    design_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power'})
    design_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if tower performance input method is NominalCapacity'})
    free_convection_regime_air_flow_rate: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'm3/s'})
    free_convection_regime_air_flow_rate_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    free_convection_regime_u_factor_times_area_value: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'W/K'})
    free_convection_u_factor_times_area_value_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate'})
    performance_input_method: Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None = Field(default='UFactorTimesAreaAndDesignWaterFlowRate', json_schema_extra={'note': 'User can define tower thermal performance by specifying the tower UA, the Design Air Flow Rate and the Design Water Flow Rate, or by specifying the tower nominal capacity'})
    heat_rejection_capacity_and_nominal_capacity_sizing_ratio: float | None = Field(default=1.25)
    nominal_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Design water flow rate ...'})
    free_convection_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Tower capacity in free convection regime with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Desig...'})
    free_convection_nominal_capacity_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    design_inlet_air_dry_bulb_temperature: float | None = Field(default=35.0, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air dry-bulb temperature"})
    design_inlet_air_wet_bulb_temperature: float | None = Field(default=25.6, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air wet-bulb temperature"})
    design_approach_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the approach temperature corresponding to the design inlet air wet-bulb temperature and design range temperature. Design approach temp = outlet water temperature minus inlet air wet-bulb temp...'})
    design_range_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the range temperature corresponding to the design inlet air wet-bulb temperature and design approach temperature. Design range = inlet water temperature minus outlet water temperature at desi...'})
    basin_heater_capacity: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'W/K', 'note': 'This heater maintains the basin water temperature at the basin heater setpoint temperature when the outdoor air temperature falls below the setpoint temperature. The basin heater only operates when...'})
    basin_heater_setpoint_temperature: float | None = Field(default=2.0, ge=2.0, json_schema_extra={'units': 'C', 'note': 'Enter the outdoor dry-bulb temperature when the basin heater turns on'})
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin heater setpoint temperature. If a schedule name is not entered, the...'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=0.2, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporation from the cooling tower and lost to the outdoor air [%/K] Evaporation loss is calculated as percentage of the circulating condenser water rate Value entered here is percent...'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': 'Rate of drift loss as a percentage of circulating condenser water flow rate Typical values are between 0.002 and 0.2% The default value is 0.008%'})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the cooling tower. Blowdown is water intentionally drained from the tower in order to offset the build up of solids in the water that would otherwise occur bec...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining a small amount of water in the tower basin to purge scale or other contaminants to reduce their concentration in order to maint...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    capacity_control: Literal['', 'FanCycling', 'FluidBypass'] | None = Field(default='FanCycling')
    number_of_cells: int | None = Field(default=1, ge=1)
    cell_control: Literal['', 'MaximalCell', 'MinimalCell'] | None = Field(default='MaximalCell')
    cell_minimum_water_flow_rate_fraction: float | None = Field(default=0.33, le=1.0, gt=0.0, json_schema_extra={'note': 'The allowable minimal fraction of the nominal flow rate per cell'})
    cell_maximum_water_flow_rate_fraction: float | None = Field(default=2.5, ge=1.0, json_schema_extra={'note': 'The allowable maximal fraction of the nominal flow rate per cell'})
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class CoolingTowerTwoSpeed(IDFBaseModel):
    """This tower model is based on Merkel's theory, which is also the basis for
the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is
modeled as a counter flow heat exchanger with a two-speed fan drawing air
through the tower (induced-draft configuration). For a multi-cell tower, the
capacity and air/water flow rate inputs are for the entire tower."""

    _idf_object_type: ClassVar[str] = "CoolingTower:TwoSpeed"
    name: str = Field(..., json_schema_extra={'note': 'Tower Name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower Water Inlet Node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower Water Outlet Node'})
    design_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Leave field blank if Tower Performance Input Method is NominalCapacity'})
    high_fan_speed_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    high_fan_speed_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at high speed'})
    high_fan_speed_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if Tower Performance Input Method is NominalCapacity'})
    low_fan_speed_air_flow_rate: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Low speed air flow rate must be less than high speed air flow rate Low speed air flow rate must be greater than free convection air flow rate'})
    low_fan_speed_air_flow_rate_sizing_factor: float | None = Field(default=0.5, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    low_fan_speed_fan_power: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at low speed'})
    low_fan_speed_fan_power_sizing_factor: float | None = Field(default=0.16, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    low_fan_speed_u_factor_times_area_value: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if tower Performance Input Method is NominalCapacity Low speed tower UA must be less than high speed tower UA Low speed tower UA must be greater than free convection tower UA'})
    low_fan_speed_u_factor_times_area_sizing_factor: float | None = Field(default=0.6, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate'})
    free_convection_regime_air_flow_rate: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'm3/s'})
    free_convection_regime_air_flow_rate_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    free_convection_regime_u_factor_times_area_value: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if Tower Performance Input Method is NominalCapacity'})
    free_convection_u_factor_times_area_value_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate'})
    performance_input_method: Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None = Field(default='UFactorTimesAreaAndDesignWaterFlowRate', json_schema_extra={'note': 'User can define tower thermal performance by specifying the tower UA, the Design Air Flow Rate and the Design Water Flow Rate, or by specifying the tower nominal capacity'})
    heat_rejection_capacity_and_nominal_capacity_sizing_ratio: float | None = Field(default=1.25)
    high_speed_nominal_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature, with the tower fan oper...'})
    low_speed_nominal_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature, with the tower fan oper...'})
    low_speed_nominal_capacity_sizing_factor: float | None = Field(default=0.5, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    free_convection_nominal_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Tower capacity in free convection regime with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Desig...'})
    free_convection_nominal_capacity_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    design_inlet_air_dry_bulb_temperature: float | None = Field(default=35.0, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air dry-bulb temperature"})
    design_inlet_air_wet_bulb_temperature: float | None = Field(default=25.6, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air wet-bulb temperature"})
    design_approach_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the approach temperature corresponding to the design inlet air wet-bulb temperature and design range temperature. Design approach temp = outlet water temperature minus inlet air wet-bulb temp...'})
    design_range_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the range temperature corresponding to the design inlet air wet-bulb temperature and design approach temperature. Design range = inlet water temperature minus outlet water temperature at desi...'})
    basin_heater_capacity: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'W/K', 'note': 'This heater maintains the basin water temperature at the basin heater setpoint temperature when the outdoor air temperature falls below the setpoint temperature. The basin heater only operates when...'})
    basin_heater_setpoint_temperature: float | None = Field(default=2.0, ge=2.0, json_schema_extra={'units': 'C', 'note': 'Enter the outdoor dry-bulb temperature when the basin heater turns on'})
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin heater setpoint temperature. If a schedule name is not entered, the...'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=0.2, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K] Evaporation loss is calculated as percentage of the circulating condenser water rate Value entered here is percent-...'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': 'Rate of drift loss as a percentage of circulating condenser water flow rate Typical values are between 0.002 and 0.2% The default value is 0.008%'})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the cooling tower. Blowdown is water intentionally drained from the tower in order to offset the build up of solids in the water that would otherwise occur bec...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining some amount of water in the tower basin to purge scale or other contaminants to reduce their concentration in order to maintain...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    number_of_cells: int | None = Field(default=1, ge=1)
    cell_control: Literal['', 'MaximalCell', 'MinimalCell'] | None = Field(default='MaximalCell')
    cell_minimum_water_flow_rate_fraction: float | None = Field(default=0.33, le=1.0, gt=0.0, json_schema_extra={'note': 'The allowable minimal fraction of the nominal flow rate per cell'})
    cell_maximum_water_flow_rate_fraction: float | None = Field(default=2.5, ge=1.0, json_schema_extra={'note': 'The allowable maximal fraction of the nominal flow rate per cell'})
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class CoolingTowerVariableSpeed(IDFBaseModel):
    """This open wet tower model is based on purely empirical algorithms derived
from manufacturer's performance data or field measurements. The user can
select from two existing algorithms (CoolTools or YorkCalc), or they can
enter their own correlation for approach temperature by using a variable
speed tower model coefficient object. For a multi-cell tower, the capacity
and air/water flow rate inputs are for the entire tower."""

    _idf_object_type: ClassVar[str] = "CoolingTower:VariableSpeed"
    name: str = Field(..., json_schema_extra={'note': 'Tower Name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water outlet node'})
    model_type: Literal['', 'CoolToolsCrossFlow', 'CoolToolsUserDefined', 'YorkCalc', 'YorkCalcUserDefined'] | None = Field(default='YorkCalc', json_schema_extra={'note': 'Determines the coefficients and form of the equation for calculating approach temperature'})
    model_coefficient_name: VariableSpeedTowerCoefficientRef | None = Field(default=None, json_schema_extra={'object_list': ['VariableSpeedTowerCoefficient'], 'note': 'Name of the tower model coefficient object. Used only when tower Model Type is either CoolToolsUserDefined or YorkCalcUserDefined.'})
    design_inlet_air_wet_bulb_temperature: float | None = Field(default=25.6, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air wet-bulb temperature"})
    design_approach_temperature: float | None = Field(default=3.9, gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'Enter the approach temperature corresponding to the design inlet air wet-bulb temperature and design range temperature. Design approach temp = outlet water temperature minus inlet air wet-bulb temp...'})
    design_range_temperature: float | None = Field(default=5.6, gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'Enter the range temperature corresponding to the design inlet air wet-bulb temperature and design approach temperature. Design range = inlet water temperature minus outlet water temperature at desi...'})
    design_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Water flow rate through the tower at design conditions'})
    design_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Design (maximum) air flow rate through the tower'})
    design_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'Enter the fan motor electric input power at design (max) air flow through the tower Standard conversion for horsepower is 1 HP = 745.7 W'})
    fan_power_ratio_function_of_air_flow_rate_ratio_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'FPR = a + b*AFR + c*AFR**2 + d*AFR**3 FPR = fraction of the design fan power AFR = fraction of the design air flow rate If left blank, then fan power is assumed to be proportional to (air flow rate...'})
    minimum_air_flow_rate_ratio: float | None = Field(default=0.2, ge=0.2, le=0.5, json_schema_extra={'note': 'Enter the minimum air flow rate ratio. This is typically determined by the variable speed drive that controls the fan motor speed. Valid entries are from 0.2 to 0.5.'})
    fraction_of_tower_capacity_in_free_convection_regime: float | None = Field(default=0.125, ge=0.0, le=0.2, json_schema_extra={'note': 'Enter the fraction of tower capacity in the free convection regime. This is the fraction of the tower capacity, at the current inlet air wet-bulb temperature, that is available when the tower fan i...'})
    basin_heater_capacity: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'W/K', 'note': 'This heater maintains the basin water temperature at the basin heater setpoint temperature when the outdoor air temperature falls below the setpoint temperature. The basin heater only operates when...'})
    basin_heater_setpoint_temperature: float | None = Field(default=2.0, ge=2.0, json_schema_extra={'units': 'C', 'note': 'Enter the outdoor dry-bulb temperature when the basin heater turns on'})
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin heater setpoint temperature. If a schedule name is not entered, the...'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=0.2, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K] Evaporation loss is calculated as percentage of the circulating condenser water rate Value entered here is percent-...'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': 'Rate of drift loss as a percentage of circulating condenser water flow rate Typical values are between 0.002 and 0.2% The default value is 0.008%'})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the cooling tower. Blowdown is water intentionally drained from the tower in order to offset the build up of solids in the water that would otherwise occur bec...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining a small amount of water in the tower basin to purge scale or other contaminants to reduce their concentration in order to maint...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    number_of_cells: int | None = Field(default=1, ge=1)
    cell_control: Literal['', 'MaximalCell', 'MinimalCell'] | None = Field(default='MaximalCell')
    cell_minimum_water_flow_rate_fraction: float | None = Field(default=0.33, le=1.0, gt=0.0, json_schema_extra={'note': 'The allowable minimal fraction of the nominal flow rate per cell'})
    cell_maximum_water_flow_rate_fraction: float | None = Field(default=2.5, ge=1.0, json_schema_extra={'note': 'The allowable maximal fraction of the nominal flow rate per cell'})
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class CoolingTowerVariableSpeedMerkel(IDFBaseModel):
    """This tower model is based on Merkel's theory, which is also the basis for
the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is
modeled as a counter flow heat exchanger with a variable-speed fan drawing
air through the tower (induced-draft configuration). For a multi-cell tower,
the capacity and air/water flow rate inputs are for the entire tower."""

    _idf_object_type: ClassVar[str] = "CoolingTower:VariableSpeed:Merkel"
    name: str = Field(..., json_schema_extra={'note': 'Tower Name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of tower water outlet node'})
    performance_input_method: Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None = Field(default='NominalCapacity', json_schema_extra={'note': 'User can define tower thermal performance by specifying the tower UA, the Design Air Flow Rate and the Design Water Flow Rate, or by specifying the tower nominal capacity'})
    heat_rejection_capacity_and_nominal_capacity_sizing_ratio: float | None = Field(default=1.25)
    nominal_capacity: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature, with the tower fan oper...'})
    free_convection_nominal_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'required field when performance method is NominalCapacity Tower capacity in free convection regime with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-...'})
    free_convection_nominal_capacity_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    design_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_water_flow_rate_per_unit_of_nominal_capacity: float | None = Field(default=5.382e-08, json_schema_extra={'units': 'm3/s-W', 'note': 'This field is only used if the previous is set to autocalculate and performance input method is NominalCapacity'})
    design_air_flow_rate: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'This is the air flow rate at full fan speed'})
    design_air_flow_rate_per_unit_of_nominal_capacity: float | None = Field(default=2.76316e-05, json_schema_extra={'units': 'm3/s-W', 'note': 'This field is only used if the previous is set to autocalculate When field is left blank the default scaling factor is adjusted for elevation to increase volume flow at altitude When field has a va...'})
    minimum_air_flow_rate_ratio: float | None = Field(default=0.2, ge=0.1, le=0.5, json_schema_extra={'note': 'Enter the minimum air flow rate ratio. This is typically determined by the variable speed drive that controls the fan motor speed. Valid entries are from 0.1 to 0.5.'})
    design_fan_power: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at high speed'})
    design_fan_power_per_unit_of_nominal_capacity: float | None = Field(default=0.0105, json_schema_extra={'units': 'dimensionless', 'note': 'This field is only used if the previous is set to autocalculate [W/W] Watts of fan power per Watt of tower nominal capacity'})
    fan_power_modifier_function_of_air_flow_rate_ratio_curve_name: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Any curve or table with one independent variable can be used cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3 quartic curve = a + b*AFR + c*AFR**2 + d*AFR**3 + e*AFR**4 x = AFR = Ratio of current oper...'})
    free_convection_regime_air_flow_rate: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'm3/s'})
    free_convection_regime_air_flow_rate_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    design_air_flow_rate_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'required field when performance method is UFactorTimesAreaAndDesignWaterFlowRate when performance method is NominalCapacity the program will solve for this UA'})
    free_convection_regime_u_factor_times_area_value: float | Literal['', 'Autocalculate'] | None = Field(default=0.0, json_schema_extra={'units': 'W/K', 'note': 'required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate Leave field blank if performance input method is NominalCapacity'})
    free_convection_u_factor_times_area_value_sizing_factor: float | None = Field(default=0.1, gt=0.0, lt=1.0, json_schema_extra={'note': 'required field when performance input method is UFactorTimesAreaAndDesignWaterFlowRate This field is only used if the previous field is set to autocalculate and the performance input method is UFac...'})
    u_factor_times_area_modifier_function_of_air_flow_ratio_curve_name: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': "This curve describes how tower's design UA changes with variable air flow rate Any curve or table with one independent variable can be used cubic curve = a + b*AFR + c*AFR**2 + d*AFR**3 quartic cur..."})
    u_factor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'curve describes how tower UA changes with outdoor air wet-bulb temperature difference from design wet-bulb Any curve or table with one independent variable can be used cubic curve = a + b*DeltaWB +...'})
    u_factor_times_area_modifier_function_of_water_flow_ratio_curve_name: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'curve describes how tower UA changes with the flow rate of condenser water through the tower Any curve or table with one independent variable can be used cubic curve = a + b*WFR + c*WFR**2 + d*WFR*...'})
    design_inlet_air_dry_bulb_temperature: float | None = Field(default=35.0, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air dry-bulb temperature"})
    design_inlet_air_wet_bulb_temperature: float | None = Field(default=25.6, ge=20.0, json_schema_extra={'units': 'C', 'note': "Enter the tower's design inlet air wet-bulb temperature"})
    design_approach_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the approach temperature corresponding to the design inlet air wet-bulb temperature and design range temperature. Design approach temp = outlet water temperature minus inlet air wet-bulb temp...'})
    design_range_temperature: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'deltaC', 'note': 'Enter the range temperature corresponding to the design inlet air wet-bulb temperature and design approach temperature. Design range = inlet water temperature minus outlet water temperature at desi...'})
    basin_heater_capacity: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'W/K', 'note': 'This heater maintains the basin water temperature at the basin heater setpoint temperature when the outdoor air temperature falls below the setpoint temperature. The basin heater only operates when...'})
    basin_heater_setpoint_temperature: float | None = Field(default=2.0, ge=2.0, json_schema_extra={'units': 'C', 'note': 'Enter the outdoor dry-bulb temperature when the basin heater turns on'})
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin heater setpoint temperature. If a schedule name is not entered, the...'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=0.2, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporated from the cooling tower and lost to the outdoor air [%/K] Evaporation loss is calculated as percentage of the circulating condenser water rate Value entered here is percent-...'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': 'Rate of drift loss as a percentage of circulating condenser water flow rate Typical values are between 0.002 and 0.2% The default value is 0.008%'})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the cooling tower. Blowdown is water intentionally drained from the tower in order to offset the build up of solids in the water that would otherwise occur bec...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining some amount of water in the tower basin to purge scale or other contaminants to reduce their concentration in order to maintain...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    number_of_cells: int | None = Field(default=1, ge=1)
    cell_control: Literal['', 'MaximalCell', 'MinimalCell'] | None = Field(default='MaximalCell')
    cell_minimum_water_flow_rate_fraction: float | None = Field(default=0.33, le=1.0, gt=0.0, json_schema_extra={'note': 'The allowable minimal fraction of the nominal flow rate per cell'})
    cell_maximum_water_flow_rate_fraction: float | None = Field(default=2.5, ge=1.0, json_schema_extra={'note': 'The allowable maximal fraction of the nominal flow rate per cell'})
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class EvaporativeFluidCoolerSingleSpeed(IDFBaseModel):
    """This model is based on Merkel's theory, which is also the basis for the
cooling tower model in EnergyPlus. The Evaporative fluid cooler is modeled
as a counter flow heat exchanger."""

    _idf_object_type: ClassVar[str] = "EvaporativeFluidCooler:SingleSpeed"
    name: str = Field(..., json_schema_extra={'note': 'Fluid Cooler Name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of Fluid Cooler water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of Fluid Cooler water outlet node'})
    design_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_air_flow_rate_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power'})
    design_spray_water_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    performance_input_method: Literal['StandardDesignCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate', 'UserSpecifiedDesignCapacity'] = Field(..., json_schema_extra={'note': 'User can define fluid cooler thermal performance by specifying the fluid cooler UA and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design Capacity or by specifying Design...'})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    heat_rejection_capacity_and_nominal_capacity_sizing_ratio: float | None = Field(default=1.25)
    standard_design_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Standard design capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Design water flow rat...'})
    design_air_flow_rate_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate; for other Performance Input Methods, this field is ignored.'})
    design_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity.'})
    user_specified_design_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored.'})
    design_entering_water_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Water Temperature must be greater than Design Enter...'})
    design_entering_air_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Air Temperature must be greater than Design Enterin...'})
    design_entering_air_wet_bulb_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Air Wet-bulb Temperature must be less than Design E...'})
    capacity_control: Literal['', 'FanCycling', 'FluidBypass'] | None = Field(default='FanCycling')
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=None, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K] Empirical correlation is used to calculate default loss factor if it not explicitly provided.'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': "Rate of drift loss as a percentage of circulating spray water flow rate Default value for this field is under investigation. For now Cooling tower's drift loss percent default value is taken here."})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the Evaporative Fluid Cooler. Blowdown is water intentionally drained from the basin in order to offset the build up of solids in the water that would otherwis...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining a small amount of water in the Fluid Cooler basin to purge scale or other contaminants to reduce their concentration in order t...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})


class EvaporativeFluidCoolerTwoSpeed(IDFBaseModel):
    """This model is based on Merkel's theory, which is also the basis for the
cooling tower model in EnergyPlus. The Evaporative fluid cooler is modeled
as a counter flow heat exchanger."""

    _idf_object_type: ClassVar[str] = "EvaporativeFluidCooler:TwoSpeed"
    name: str = Field(..., json_schema_extra={'note': 'fluid cooler name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water outlet node'})
    high_fan_speed_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    high_fan_speed_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at high speed'})
    low_fan_speed_air_flow_rate: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Low speed air flow rate must be less than high speed air flow rate'})
    low_fan_speed_air_flow_rate_sizing_factor: float | None = Field(default=0.5, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    low_fan_speed_fan_power: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at low speed'})
    low_fan_speed_fan_power_sizing_factor: float | None = Field(default=0.16, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    design_spray_water_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    performance_input_method: Literal['StandardDesignCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate', 'UserSpecifiedDesignCapacity'] = Field(..., json_schema_extra={'note': 'User can define fluid cooler thermal performance by specifying the fluid cooler UA and the Design Water Flow Rate, or by specifying the fluid cooler Standard Design Capacity or by specifying Design...'})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})
    heat_rejection_capacity_and_nominal_capacity_sizing_ratio: float | None = Field(default=1.25)
    high_speed_standard_design_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Standard design capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Design water flow rat...'})
    low_speed_standard_design_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Standard design capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-bulb temperature. Design water flow rat...'})
    low_speed_standard_capacity_sizing_factor: float | None = Field(default=0.5, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    high_fan_speed_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate; for other Performance Input Methods, this field is ignored.'})
    low_fan_speed_u_factor_times_area_value: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Only used for Performance Input Method = UFactorTimesAreaAndDesignWaterFlowRate; for other input methods, this field is ignored. Low speed fluid cooler UA must be less than high speed fluid cooler UA'})
    low_fan_speed_u_factor_times_area_sizing_factor: float | None = Field(default=0.6, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate'})
    design_water_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'Input value is ignored if fluid cooler Performance Input Method= StandardDesignCapacity'})
    high_speed_user_specified_design_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored.'})
    low_speed_user_specified_design_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored.'})
    low_speed_user_specified_design_capacity_sizing_factor: float | None = Field(default=0.5, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate'})
    design_entering_water_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Water Temperature must be greater than Design Enter...'})
    design_entering_air_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Air Temperature must be greater than Design Enterin...'})
    design_entering_air_wet_bulb_temperature: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'C', 'note': 'Only used for Performance Input Method = UserSpecifiedDesignCapacity; for other Performance Input Methods, this field is ignored. Design Entering Air Wet-bulb Temperature must be less than Design E...'})
    high_speed_sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'})
    evaporation_loss_mode: Literal['', 'LossFactor', 'SaturatedExit'] | None = Field(default='SaturatedExit')
    evaporation_loss_factor: float | None = Field(default=None, json_schema_extra={'units': 'percent/K', 'note': 'Rate of water evaporation from the Fluid Cooler and lost to the outdoor air [%/K] Empirical correlation is used to calculate default loss factor if it not explicitly provided.'})
    drift_loss_percent: float | None = Field(default=0.008, json_schema_extra={'units': 'percent', 'note': "Default value is under investigation. For now cooling tower's default value is taken."})
    blowdown_calculation_mode: Literal['', 'ConcentrationRatio', 'ScheduledRate'] | None = Field(default='ConcentrationRatio')
    blowdown_concentration_ratio: float | None = Field(default=3.0, ge=2.0, json_schema_extra={'note': 'Characterizes the rate of blowdown in the Evaporative Fluid Cooler. Blowdown is water intentionally drained from the Evaporative Fluid Cooler in order to offset the build up of solids in the water ...'})
    blowdown_makeup_water_usage_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Makeup water usage due to blowdown results from occasionally draining some amount of water in the Evaporative Fluid Cooler basin to purge scale or other contaminants to reduce their concentration i...'})
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']})


class FluidCoolerSingleSpeed(IDFBaseModel):
    """The fluid cooler is modeled as a cross flow heat exchanger (both streams
unmixed) with single-speed fans (induced draft configuration)."""

    _idf_object_type: ClassVar[str] = "FluidCooler:SingleSpeed"
    name: str = Field(..., json_schema_extra={'note': 'fluid cooler name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water outlet node'})
    performance_input_method: Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None = Field(default='NominalCapacity', json_schema_extra={'note': 'User can define fluid cooler thermal performance by specifying the fluid cooler UA and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity'})
    design_air_flow_rate_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if fluid cooler Performance Input Method is NominalCapacity'})
    nominal_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Nominal fluid cooler capacity'})
    design_entering_water_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Water Temperature must be specified for both the performance input methods and its value must be greater than Design Entering Air Temperature.'})
    design_entering_air_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Air Temperature must be specified for both the performance input methods and its value must be greater than Design Entering Air Wet-bulb Temperature.'})
    design_entering_air_wetbulb_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and its value must be less than Design Entering Air Temperature.'})
    design_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    design_air_flow_rate_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power'})
    outdoor_air_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Enter the name of an outdoor air node'})


class FluidCoolerTwoSpeed(IDFBaseModel):
    """The fluid cooler is modeled as a cross flow heat exchanger (both streams
unmixed) with two-speed fans (induced draft configuration)."""

    _idf_object_type: ClassVar[str] = "FluidCooler:TwoSpeed"
    name: str = Field(..., json_schema_extra={'note': 'fluid cooler name'})
    water_inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water inlet node'})
    water_outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of fluid cooler water outlet node'})
    performance_input_method: Literal['', 'NominalCapacity', 'UFactorTimesAreaAndDesignWaterFlowRate'] | None = Field(default='NominalCapacity', json_schema_extra={'note': 'User can define fluid cooler thermal performance by specifying the fluid cooler UA and the Design Water Flow Rate, or by specifying the fluid cooler nominal capacity'})
    high_fan_speed_u_factor_times_area_value: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if fluid cooler Performance Input Method is NominalCapacity'})
    low_fan_speed_u_factor_times_area_value: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W/K', 'note': 'Leave field blank if fluid cooler Performance Input Method is NominalCapacity Low speed fluid cooler UA must be less than high speed fluid cooler UA Low speed fluid cooler UA must be greater than f...'})
    low_fan_speed_u_factor_times_area_sizing_factor: float | None = Field(default=0.6, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is UFactorTimesAreaAndDesignWaterFlowRate'})
    high_speed_nominal_capacity: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W', 'note': 'Nominal fluid cooler capacity at high fan speed'})
    low_speed_nominal_capacity: float | Literal['Autocalculate'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Nominal fluid cooler capacity at low fan speed'})
    low_speed_nominal_capacity_sizing_factor: float | None = Field(default=0.5, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate and the Performance Input Method is NominalCapacity'})
    design_entering_water_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Water Temperature must be specified for both the performance input methods and its value must be greater than Design Entering Air Temperature.'})
    design_entering_air_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Air Temperature must be specified for both the performance input methods and its value must be greater than Design Entering Air Wet-bulb Temperature.'})
    design_entering_air_wet_bulb_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'Design Entering Air Wet-bulb Temperature must be specified for both the performance input methods and its value must be less than Design Entering Air Temperature.'})
    design_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    high_fan_speed_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Air Flow Rate at High Fan Speed must be greater than Air Flow Rate at Low Fan Speed'})
    high_fan_speed_fan_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at high speed'})
    low_fan_speed_air_flow_rate: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'Air Flow Rate at Low Fan Speed must be less than Air Flow Rate at High Fan Speed'})
    low_fan_speed_air_flow_rate_sizing_factor: float | None = Field(default=0.5, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    low_fan_speed_fan_power: float | Literal['Autocalculate'] = Field(..., json_schema_extra={'units': 'W', 'note': 'This is the fan motor electric input power at low speed'})
    low_fan_speed_fan_power_sizing_factor: float | None = Field(default=0.16, json_schema_extra={'note': 'This field is only used if the previous field is set to autocalculate.'})
    outdoor_air_inlet_node_name: str | None = Field(default=None)


class GroundHeatExchangerHorizontalTrench(IDFBaseModel):
    """This models a horizontal heat exchanger placed in a series of trenches The
model uses the PipingSystem:Underground underlying algorithms, but provides
a more usable input interface."""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:HorizontalTrench"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    trench_length_in_pipe_axial_direction: float | None = Field(default=50.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the total pipe axial length of the heat exchanger If all pipe trenches are parallel, this is the length of a single trench. If a single, long run of pipe is used with one trench, this is th...'})
    number_of_trenches: int | None = Field(default=1, ge=1, json_schema_extra={'note': 'This is the number of horizontal legs that will be used in the entire heat exchanger, one pipe per trench'})
    horizontal_spacing_between_pipes: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This represents the average horizontal spacing between any two trenches for heat exchangers that have multiple trenches'})
    pipe_inner_diameter: float | None = Field(default=0.016, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_outer_diameter: float | None = Field(default=0.026, gt=0.0, json_schema_extra={'units': 'm'})
    burial_depth: float | None = Field(default=1.5, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the burial depth of the pipes, or the trenches containing the pipes'})
    soil_thermal_conductivity: float | None = Field(default=1.08, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    soil_density: float | None = Field(default=962.0, gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float | None = Field(default=2576.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'})
    pipe_thermal_conductivity: float | None = Field(default=0.3895, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    pipe_density: float | None = Field(default=641.0, gt=0.0, json_schema_extra={'units': 'kg/m3'})
    pipe_specific_heat: float | None = Field(default=2405.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'})
    soil_moisture_content_percent: float | None = Field(default=30.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    soil_moisture_content_percent_at_saturation: float | None = Field(default=50.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    undisturbed_ground_temperature_model_type: Literal['Site:GroundTemperature:Undisturbed:FiniteDifference', 'Site:GroundTemperature:Undisturbed:KusudaAchenbach', 'Site:GroundTemperature:Undisturbed:Xing'] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']})
    evapotranspiration_ground_cover_parameter: float | None = Field(default=0.4, ge=0.0, le=1.5, json_schema_extra={'note': 'This specifies the ground cover effects during evapotranspiration calculations. The value roughly represents the following cases: = 0   : concrete or other solid, non-permeable ground surface mater...'})


class GroundHeatExchangerPond(IDFBaseModel):
    """A model of a shallow pond with immersed pipe loops. Typically used in hybrid
geothermal systems and included in the condenser loop. This component may
also be used as a simple solar collector."""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Pond"
    name: str = Field(...)
    fluid_inlet_node_name: str = Field(...)
    fluid_outlet_node_name: str = Field(...)
    pond_depth: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    pond_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2'})
    hydronic_tubing_inside_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_outside_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    ground_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m2-K'})
    number_of_tubing_circuits: int = Field(..., ge=1)
    length_of_each_tubing_circuit: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})


class GroundHeatExchangerResponseFactors(IDFBaseModel):
    """Response factor definitions from third-party tool, commonly referred to a
\"g-functions\""""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:ResponseFactors"
    name: str = Field(...)
    ghe_vertical_properties_object_name: GroundHeatExchangerVerticalPropertiesNamesRef = Field(..., json_schema_extra={'object_list': ['GroundHeatExchangerVerticalPropertiesNames']})
    number_of_boreholes: int = Field(...)
    g_function_reference_ratio: float | None = Field(default=0.0005, gt=0.0, json_schema_extra={'units': 'dimensionless'})
    g_functions: list[GroundHeatExchangerResponseFactorsGFunctionsItem] | None = Field(default=None)


class GroundHeatExchangerSlinky(IDFBaseModel):
    """This models a slinky horizontal heat exchanger placed in a series of
trenches The model uses the model developed by: Xiong, Z., D.E. Fisher, and
J.D. Spitler. 2015. Development and Validation of a Slinky Ground Heat
Exchanger Model. Applied Energy 141: 57-69."""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Slinky"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_flow_rate: float | None = Field(default=0.002, gt=0.0, json_schema_extra={'units': 'm3/s'})
    soil_thermal_conductivity: float | None = Field(default=1.08, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    soil_density: float | None = Field(default=962.0, gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float | None = Field(default=2576.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'})
    pipe_thermal_conductivity: float | None = Field(default=0.4, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    pipe_density: float | None = Field(default=641.0, gt=0.0, json_schema_extra={'units': 'kg/m3'})
    pipe_specific_heat: float | None = Field(default=2405.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'})
    pipe_outer_diameter: float | None = Field(default=0.02667, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_thickness: float | None = Field(default=0.002413, gt=0.0, json_schema_extra={'units': 'm'})
    heat_exchanger_configuration: Literal['Horizontal', 'Vertical'] | None = Field(default=None, json_schema_extra={'note': 'This is the orientation of the heat exchanger'})
    coil_diameter: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the diameter of the heat exchanger coil'})
    coil_pitch: float | None = Field(default=0.2, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the center-to-center distance between coils'})
    trench_depth: float | None = Field(default=1.8, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the distance from the ground surface to the trench bottom'})
    trench_length: float | None = Field(default=10.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This is the total length of a single trench This assumes the heat exchanger runs the full length of the trench'})
    number_of_trenches: int | None = Field(default=1, ge=1, json_schema_extra={'note': 'This is the number of parallel trenches that has a heat exchanger, one per trench'})
    horizontal_spacing_between_pipes: float | None = Field(default=2.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'This represents the average horizontal spacing between any two trenches for heat exchangers that have multiple trenches'})
    undisturbed_ground_temperature_model_type: Literal['Site:GroundTemperature:Undisturbed:FiniteDifference', 'Site:GroundTemperature:Undisturbed:KusudaAchenbach', 'Site:GroundTemperature:Undisturbed:Xing'] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']})
    maximum_length_of_simulation: float | None = Field(default=None, json_schema_extra={'units': 'years'})


class GroundHeatExchangerSurface(IDFBaseModel):
    """A hydronic surface/panel consisting of a multi-layer construction with
embedded rows of tubes. Typically used in hybrid geothermal systems and
included in the condenser loop. This component may also be used as a simple
solar collector. The bottom surface may be defined as ground-coupled or
exposed to wind (eg. bridge deck)."""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Surface"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})
    fluid_inlet_node_name: str = Field(...)
    fluid_outlet_node_name: str = Field(...)
    hydronic_tubing_inside_diameter: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    number_of_tubing_circuits: int | None = Field(default=None, ge=1)
    hydronic_tube_spacing: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    surface_length: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    surface_width: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    lower_surface_environment: Literal['', 'Exposed', 'Ground'] | None = Field(default='Ground')


class GroundHeatExchangerSystem(IDFBaseModel):
    """Models vertical ground heat exchangers systems using the response factor
approach developed by Eskilson. Response factors are calculated using a
finite line source model assuming uniform heat flux at the borehole wall if
UHFcalc is specified, or uniform borehole wall temperature if UBHWTcalc is
specified."""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:System"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    undisturbed_ground_temperature_model_type: Literal['Site:GroundTemperature:Undisturbed:FiniteDifference', 'Site:GroundTemperature:Undisturbed:KusudaAchenbach', 'Site:GroundTemperature:Undisturbed:Xing'] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']})
    ground_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    ground_thermal_heat_capacity: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/m3-K'})
    ghe_vertical_responsefactors_object_name: GroundHeatExchangerVerticalResponseFactorNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['GroundHeatExchangerVerticalResponseFactorNames']})
    g_function_calculation_method: Literal['', 'UBHWTcalc', 'UHFcalc'] | None = Field(default='UHFcalc')
    ghe_vertical_array_object_name: GroundHeatExchangerVerticalArrayNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['GroundHeatExchangerVerticalArrayNames']})
    vertical_well_locations: list[GroundHeatExchangerSystemVerticalWellLocationsItem] | None = Field(default=None)


class GroundHeatExchangerVerticalArray(IDFBaseModel):
    """GroundHeatExchanger:Vertical:Array"""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Vertical:Array"
    name: str = Field(...)
    ghe_vertical_properties_object_name: GroundHeatExchangerVerticalPropertiesNamesRef = Field(..., json_schema_extra={'object_list': ['GroundHeatExchangerVerticalPropertiesNames']})
    number_of_boreholes_in_x_direction: int = Field(..., ge=1)
    number_of_boreholes_in_y_direction: int = Field(..., ge=1)
    borehole_spacing: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})


class GroundHeatExchangerVerticalProperties(IDFBaseModel):
    """Properties for vertical ground heat exchanger systems"""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Vertical:Properties"
    name: str = Field(...)
    depth_of_top_of_borehole: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    borehole_length: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    borehole_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    grout_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    grout_thermal_heat_capacity: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/m3-K'})
    pipe_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    pipe_thermal_heat_capacity: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/m3-K'})
    pipe_outer_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    pipe_thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    u_tube_distance: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})


class GroundHeatExchangerVerticalSingle(IDFBaseModel):
    """GroundHeatExchanger:Vertical:Single"""

    _idf_object_type: ClassVar[str] = "GroundHeatExchanger:Vertical:Single"
    name: str = Field(...)
    ghe_vertical_properties_object_name: GroundHeatExchangerVerticalPropertiesNamesRef = Field(..., json_schema_extra={'object_list': ['GroundHeatExchangerVerticalPropertiesNames']})
    x_location: float = Field(..., json_schema_extra={'units': 'm'})
    y_location: float = Field(..., json_schema_extra={'units': 'm'})


class HeatExchangerFluidToFluid(IDFBaseModel):
    """A fluid/fluid heat exchanger designed to couple the supply side of one loop
to the demand side of another loop Loops can be either plant or condenser
loops but no air side connections are allowed"""

    _idf_object_type: ClassVar[str] = "HeatExchanger:FluidToFluid"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. default is that heat exchanger is on'})
    loop_demand_side_inlet_node_name: str = Field(..., json_schema_extra={'note': 'This connection is to the demand side of a loop and is the inlet to the heat exchanger'})
    loop_demand_side_outlet_node_name: str = Field(..., json_schema_extra={'note': 'This connection is to the demand side of a loop'})
    loop_demand_side_design_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    loop_supply_side_inlet_node_name: str = Field(...)
    loop_supply_side_outlet_node_name: str = Field(...)
    loop_supply_side_design_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    heat_exchange_model_type: Literal['', 'CounterFlow', 'CrossFlowBothMixed', 'CrossFlowBothUnMixed', 'CrossFlowSupplyMixedDemandUnMixed', 'CrossFlowSupplyUnMixedDemandMixed', 'Ideal', 'ParallelFlow'] | None = Field(default='Ideal')
    heat_exchanger_u_factor_times_area_value: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W/K'})
    control_type: Literal['', 'CoolingDifferentialOnOff', 'CoolingSetpointModulated', 'CoolingSetpointOnOff', 'CoolingSetpointOnOffWithComponentOverride', 'DualDeadbandSetpointModulated', 'DualDeadbandSetpointOnOff', 'HeatingSetpointModulated', 'HeatingSetpointOnOff', 'OperationSchemeModulated', 'OperationSchemeOnOff', 'UncontrolledOn'] | None = Field(default='UncontrolledOn')
    heat_exchanger_setpoint_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Setpoint node is needed with any Control Type that is "*Setpoint*"'})
    minimum_temperature_difference_to_activate_heat_exchanger: float | None = Field(default=0.01, ge=0.0, le=50.0, json_schema_extra={'units': 'deltaC', 'note': 'Tolerance between control temperatures used to determine if heat exchanger should run.'})
    heat_transfer_metering_end_use_type: Literal['', 'FreeCooling', 'HeatRecovery', 'HeatRecoveryForCooling', 'HeatRecoveryForHeating', 'HeatRejection', 'LoopToLoop'] | None = Field(default='LoopToLoop', json_schema_extra={'note': 'This field controls end use reporting for heat transfer meters'})
    component_override_loop_supply_side_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride'})
    component_override_loop_demand_side_inlet_node_name: str | None = Field(default=None, json_schema_extra={'note': 'This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride'})
    component_override_cooling_control_temperature_mode: Literal['', 'DryBulbTemperature', 'Loop', 'WetBulbTemperature'] | None = Field(default='Loop', json_schema_extra={'note': 'This field is only used if Control Type is set to CoolingSetpointOnOffWithComponentOverride'})
    sizing_factor: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'note': 'Multiplies the autosized flow rates for this device'})
    operation_minimum_temperature_limit: float | None = Field(default=None, json_schema_extra={'units': 'C', 'note': 'Lower limit on inlet temperatures, heat exchanger will not operate if either inlet is below this limit'})
    operation_maximum_temperature_limit: float | None = Field(default=None, json_schema_extra={'units': 'C', 'note': 'Upper limit on inlet temperatures, heat exchanger will not operate if either inlet is above this limit'})

