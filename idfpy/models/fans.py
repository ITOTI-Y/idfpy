"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Fans
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    FansCVandVAVRef,
    FansComponentModelRef,
    ScheduleNamesRef,
    UnivariateFunctionsRef,
    ZoneNamesRef,
)


class FanSystemModelSpeedFractionsItem(IDFBaseModel):
    """Nested object type for array items."""
    speed_flow_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    speed_electric_power_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'if left blank then use Electric Power Function of Flow Fraction Curve'})



class FanComponentModel(IDFBaseModel):
    """A detailed fan type for constant-air-volume (CAV) and variable-air-volume
(VAV) systems. It includes inputs that describe the air-distribution system
as well as the fan, drive belt (if used), motor, and variable-frequency-
drive (if used)."""

    _idf_object_type: ClassVar[str] = "Fan:ComponentModel"
    name: str = Field(...)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    minimum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    fan_sizing_factor: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Applied to specified or autosized max fan airflow'})
    fan_wheel_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'Diameter of wheel outer circumference'})
    fan_outlet_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2', 'note': 'Area at fan outlet plane for determining discharge velocity pressure'})
    maximum_fan_static_efficiency: float = Field(..., le=1.0, gt=0.0, json_schema_extra={'note': 'Maximum ratio between power delivered to air and fan shaft input power Determined from fan performance data'})
    euler_number_at_maximum_fan_static_efficiency: float = Field(..., gt=0.0, json_schema_extra={'note': 'Euler number (Eu) determined from fan performance data'})
    maximum_dimensionless_fan_airflow: float = Field(..., gt=0.0, json_schema_extra={'note': 'Corresponds to maximum ratio between fan airflow and fan shaft rotational speed for specified fan wheel diameter Determined from fan performance data'})
    motor_fan_pulley_ratio: float | Literal['', 'Autosize'] | None = Field(default=1.0, json_schema_extra={'note': 'Ratio of motor pulley diameter to fan pulley diameter'})
    belt_maximum_torque: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'N-m', 'note': 'Maximum torque transmitted by belt'})
    belt_sizing_factor: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Applied to specified or autosized max torque transmitted by belt'})
    belt_fractional_torque_transition: float | None = Field(default=0.167, ge=0.0, le=1.0, json_schema_extra={'note': 'Region 1 to 2 curve transition for belt normalized efficiency'})
    motor_maximum_speed: float = Field(..., gt=0.0, json_schema_extra={'units': 'rev/min', 'note': 'Maximum rotational speed of fan motor shaft'})
    maximum_motor_output_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'Maximum power input to drive belt by motor'})
    motor_sizing_factor: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Applied to specified or autosized motor output power'})
    motor_in_airstream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means motor outside air stream 1.0 means motor inside air stream'})
    vfd_efficiency_type: Literal['Power', 'Speed'] | None = Field(default=None, json_schema_extra={'note': 'Efficiency depends on fraction of full-load motor speed Efficiency depends on  fraction of full-load motor input power If field blank, then assumes constant VFD efficiency (0.97)'})
    maximum_vfd_output_power: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W', 'note': 'Maximum power input to motor by VFD'})
    vfd_sizing_factor: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Applied to specified or autosized VFD output power'})
    fan_pressure_rise_curve_name: BivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['BivariateFunctions'], 'note': 'Pressure rise depends on volumetric flow, system resistances, system leakage, and duct static pressure set point'})
    duct_static_pressure_reset_curve_name: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Function of fan volumetric flow Minimum and maximum fan airflows correspond respectively to minimum and maximum duct static pressure set points'})
    normalized_fan_static_efficiency_curve_name_non_stall_region: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'xfan <= 0 Curve should have maximum of 1.0'})
    normalized_fan_static_efficiency_curve_name_stall_region: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'xfan > 0 Curve should have maximum of 1.0'})
    normalized_dimensionless_airflow_curve_name_non_stall_region: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'xspd <= 0 Curve should have maximum of 1.0'})
    normalized_dimensionless_airflow_curve_name_stall_region: UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'xspd > 0 Curve should have maximum of 1.0'})
    maximum_belt_efficiency_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Determines maximum fan drive belt efficiency in log space as function of xbelt,max Curve should have minimum of -4.6 and maximum of 0.0 If field blank, assumes output of curve is always 1.0'})
    normalized_belt_efficiency_curve_name_region_1: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Region 1 (0 <= xbelt < xbelt,trans) Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes output of curve is always 1.0 in Region 1'})
    normalized_belt_efficiency_curve_name_region_2: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Region 2 (xbelt,trans <= xbelt <= 1) Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes output of curve is always 1.0 in Region 2'})
    normalized_belt_efficiency_curve_name_region_3: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Determines normalized drive belt efficiency Region 3 (xbelt > 1) Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes output of curve is always 1.0 in Region 3'})
    maximum_motor_efficiency_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes output of curve is always 1.0'})
    normalized_motor_efficiency_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes output of curve is always 1.0'})
    vfd_efficiency_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Determines VFD efficiency as function of motor load or speed fraction Curve should have minimum > 0.0 and maximum of 1.0 If field blank, assumes constant VFD efficiency (0.97)'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class FanConstantVolume(IDFBaseModel):
    """Constant volume fan that is intended to operate continuously based on a time
schedule. This fan will not cycle on and off based on cooling/heating load
or other control signals."""

    _idf_object_type: ClassVar[str] = "Fan:ConstantVolume"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    pressure_rise: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    motor_in_airstream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream'})
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class FanOnOff(IDFBaseModel):
    """Constant volume fan that is intended to cycle on and off based on
cooling/heating load or other control signals. This fan can also operate
continuously like Fan:ConstantVolume."""

    _idf_object_type: ClassVar[str] = "Fan:OnOff"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    fan_total_efficiency: float | None = Field(default=0.6, le=1.0, gt=0.0)
    pressure_rise: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    motor_efficiency: float | None = Field(default=0.8, le=1.0, gt=0.0)
    motor_in_airstream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream'})
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    fan_power_ratio_function_of_speed_ratio_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    fan_efficiency_ratio_function_of_speed_ratio_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions']})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class FanPerformanceNightVentilation(IDFBaseModel):
    """Specifies an alternate set of performance parameters for a fan. These
alternate parameters are used when a system manager (such as
AvailabilityManager:NightVentilation) sets a specified flow rate. May be
used with Fan:ConstantVolume, Fan:VariableVolume and Fan:ComponentModel. If
the fan model senses that a fixed flow rate has been set, it will use these
alternate performance parameters. It is assumed that the fan will run at a
fixed speed in the alternate mode."""

    _idf_object_type: ClassVar[str] = "FanPerformance:NightVentilation"
    fan_name: FansCVandVAVRef | FansComponentModelRef = Field(..., json_schema_extra={'object_list': ['FansCVandVAV', 'FansComponentModel']})
    fan_total_efficiency: float = Field(..., le=1.0, gt=0.0)
    pressure_rise: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    motor_efficiency: float = Field(..., le=1.0, gt=0.0)
    motor_in_airstream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means fan motor outside of airstream 1.0 means fan motor inside of airstream'})


class FanSystemModel(IDFBaseModel):
    """Versatile simple fan that can be used in variable air volume, constant
volume, on-off cycling, two-speed or multi-speed applications. Performance
at different flow rates, or speed levels, is determined using separate
performance curve or table or prescribed power fractions at discrete speed
levels for two-speed or multi-speed fans."""

    _idf_object_type: ClassVar[str] = "Fan:SystemModel"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this fan. Schedule value > 0 means the fan is available. If this field is blank, the fan is always available.'})
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    design_maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    speed_control_method: Literal['', 'Continuous', 'Discrete'] | None = Field(default='Discrete')
    electric_power_minimum_flow_rate_fraction: float | None = Field(default=0.2, ge=0.0, le=1.0)
    design_pressure_rise: float = Field(..., gt=0.0, json_schema_extra={'units': 'Pa'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    motor_in_air_stream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream'})
    design_electric_power_consumption: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Fan power consumption at maximum air flow rate. If autosized the method used to scale power is chosen in the following field'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure', 'TotalEfficiencyAndPressure'] | None = Field(default='PowerPerFlowPerPressure')
    electric_power_per_unit_flow_rate: float | None = Field(default=None, json_schema_extra={'units': 'W/(m3/s)'})
    electric_power_per_unit_flow_rate_per_unit_pressure: float | None = Field(default=1.66667, json_schema_extra={'units': 'W/((m3/s)-Pa)'})
    fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    electric_power_function_of_flow_fraction_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'independent variable is normalized flow rate, current flow divided by Design Maximum Air Flow Rate. dependent variable is modification factor multiplied by Design Power Consumption. This field is r...'})
    night_ventilation_mode_pressure_rise: float | None = Field(default=None, json_schema_extra={'units': 'Pa', 'note': 'Total system fan pressure rise at the fan when in night mode using AvailabilityManager:NightVentilation'})
    night_ventilation_mode_flow_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Fraction of Design Maximum Air Flow Rate to use when in night mode using AvailabilityManager:NightVentilation'})
    motor_loss_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used fan motor heat losses that not added to air stream are transferred to zone as internal gains'})
    motor_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': "optional. If zone identified in previous field then this determines the split between convection and radiation for the fan motor's skin losses"})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})
    number_of_speeds: int | None = Field(default=1, json_schema_extra={'note': 'number of different speed levels available when Speed Control Method is set to Discrete Speed need to be arranged in increasing order in remaining field sets. If set to 1, or omitted, and Speed Con...'})
    speed_fractions: list[FanSystemModelSpeedFractionsItem] | None = Field(default=None)


class FanVariableVolume(IDFBaseModel):
    """Variable air volume fan where the electric power input varies according to a
performance curve as a function of flow fraction."""

    _idf_object_type: ClassVar[str] = "Fan:VariableVolume"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    pressure_rise: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    fan_power_minimum_flow_rate_input_method: Literal['', 'FixedFlowRate', 'Fraction'] | None = Field(default='Fraction')
    fan_power_minimum_flow_fraction: float | None = Field(default=0.25, ge=0.0, le=1.0)
    fan_power_minimum_air_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    motor_in_airstream_fraction: float | None = Field(default=1.0, ge=0.0, le=1.0, json_schema_extra={'note': '0.0 means fan motor outside of air stream, 1.0 means motor inside of air stream'})
    fan_power_coefficient_1: float | None = Field(default=None, json_schema_extra={'note': 'all Fan Power Coefficients should not be 0.0 or no fan power will be consumed. Fan Power Coefficients are specified as function of full flow rate/power Equation:'})
    fan_power_coefficient_2: float | None = Field(default=None)
    fan_power_coefficient_3: float | None = Field(default=None)
    fan_power_coefficient_4: float | None = Field(default=None)
    fan_power_coefficient_5: float | None = Field(default=None)
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class FanZoneExhaust(IDFBaseModel):
    """Models a fan that exhausts air from a zone."""

    _idf_object_type: ClassVar[str] = "Fan:ZoneExhaust"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    fan_total_efficiency: float | None = Field(default=0.6, le=1.0, gt=0.0)
    pressure_rise: float = Field(..., json_schema_extra={'units': 'Pa'})
    maximum_flow_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s'})
    air_inlet_node_name: str = Field(...)
    air_outlet_node_name: str = Field(...)
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})
    flow_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If field is used, then when fan runs the exhausted air flow rate is controlled to be the scheduled fraction times the Maximum Flow Rate'})
    system_availability_manager_coupling_mode: Literal['', 'Coupled', 'Decoupled'] | None = Field(default='Coupled', json_schema_extra={'note': 'Control if fan is to be interlocked with HVAC system Availability Managers or not.'})
    minimum_zone_temperature_limit_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If field is used, the exhaust fan will not run if the zone temperature is lower than this limit'})
    balanced_exhaust_fraction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': "Used to control fan's impact on flow at the return air node. Enter the portion of the exhaust that is balanced by simple airflows."})

