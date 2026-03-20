"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Pumps
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    ScheduleNamesRef,
    UnivariateFunctionsRef,
    ZoneNamesRef,
)



class HeaderedPumpsConstantSpeed(IDFBaseModel):
    """This Headered pump object describes a pump bank with more than 1 pump in
parallel"""

    _idf_object_type: ClassVar[str] = "HeaderedPumps:ConstantSpeed"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    total_design_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'If the field is not autosized set to the flow rate to the total flow when all pumps are running at full load'})
    number_of_pumps_in_bank: int | None = Field(default=None)
    flow_sequencing_control_scheme: Literal['', 'Sequential'] | None = Field(default='Sequential')
    design_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    design_power_consumption: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'If the field is not autosized set to the power consumed by the pump bank when all the pumps are running at nominal flow When autosized the type of scaling factor is chosen in the input field Design...'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0, json_schema_extra={'note': 'This is the motor efficiency only. When the Design Power Consumption is autosized using PowerPerFlowPerPressure, the Design Shaft Power per Unit Flow Rate per Unit Head is used in addition to the m...'})
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(default='Continuous')
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rated flow rate of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump o...'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used pump losses transferred to zone as internal gains'})
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'optional. If zone identified in previous field then this determines the split between convection and radiation for the skin losses'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure'] | None = Field(default='PowerPerFlowPerPressure', json_schema_extra={'note': 'Used to indicate which sizing factor is used to calculate Design Power Consumption. PowerPerFlow indicates that Design Electric Power per Unit Flow Rate is used as scaling factor. Design Power Cons...'})
    design_electric_power_per_unit_flow_rate: float | None = Field(default=348701.1, gt=0.0, json_schema_extra={'units': 'W/(m3/s)', 'note': 'Used to size Design Power Consumption from design flow rate'})
    design_shaft_power_per_unit_flow_rate_per_unit_head: float | None = Field(default=1.282051282, gt=0.0, json_schema_extra={'units': 'W/((m3/s)-Pa)', 'note': 'Used to size Design Power Consumption from design flow rate for head and motor efficiency'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class HeaderedPumpsVariableSpeed(IDFBaseModel):
    """This Headered pump object describes a pump bank with more than 1 pump in
parallel"""

    _idf_object_type: ClassVar[str] = "HeaderedPumps:VariableSpeed"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    total_design_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'If the field is not autosized set to the flow rate to the total flow when all pumps are running at full load'})
    number_of_pumps_in_bank: int | None = Field(default=None)
    flow_sequencing_control_scheme: Literal['', 'Sequential'] | None = Field(default='Sequential')
    design_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    design_power_consumption: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'If the field is not autosized set to the power consumed by the pump bank when all the pumps are running at nominal flow When autosized the type of scaling factor is chosen in the input field Design...'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0, json_schema_extra={'note': 'This is the motor efficiency only. When the Design Power Consumption is autosized using PowerPerFlowPerPressure, the Design Shaft Power per Unit Flow Rate per Unit Head is used in addition to the m...'})
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    coefficient_1_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_2_of_the_part_load_performance_curve: float | None = Field(default=1.0)
    coefficient_3_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_4_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    minimum_flow_rate_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'note': 'This value can be zero and will be defaulted to that if not specified.'})
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(default='Continuous')
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rated flow rate of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump o...'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used pump losses transferred to zone as internal gains'})
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'optional. If zone identified in previous field then this determines the split between convection and radiation for the skin losses'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure'] | None = Field(default='PowerPerFlowPerPressure', json_schema_extra={'note': 'Used to indicate which sizing factor is used to calculate Design Power Consumption. PowerPerFlow indicates that Design Electric Power per Unit Flow Rate is used as scaling factor. Design Power Cons...'})
    design_electric_power_per_unit_flow_rate: float | None = Field(default=348701.1, gt=0.0, json_schema_extra={'units': 'W/(m3/s)', 'note': 'Used to size Design Power Consumption from design flow rate'})
    design_shaft_power_per_unit_flow_rate_per_unit_head: float | None = Field(default=1.282051282, gt=0.0, json_schema_extra={'units': 'W/((m3/s)-Pa)', 'note': 'Used to size Design Power Consumption from design flow rate for head and motor efficiency'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class PumpConstantSpeed(IDFBaseModel):
    """This pump model is described in the ASHRAE secondary HVAC toolkit."""

    _idf_object_type: ClassVar[str] = "Pump:ConstantSpeed"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    design_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    design_power_consumption: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'When autosized the type of scaling factor is chosen in the input field Design Power Sizing Method'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0, json_schema_extra={'note': 'This is the motor efficiency only. When the Design Power Consumption is autosized using PowerPerFlowPerPressure, the Design Shaft Power per Unit Flow Rate per Unit Head is used in addition to the m...'})
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(default='Continuous')
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rated flow rate of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump o...'})
    pump_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'This references any single independent variable polynomial curve in order to do pressure vs. flow calculations for this pump. The available types are then: Linear, Quadratic, Cubic, and Quartic The...'})
    impeller_diameter: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': '"D" in above expression in field A6'})
    rotational_speed: float | None = Field(default=None, json_schema_extra={'units': 'rev/min', 'note': '"N" in above expression in field A6'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used pump losses transferred to zone as internal gains'})
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'optional. If zone identified in previous field then this determines the split between convection and radiation for the skin losses'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure'] | None = Field(default='PowerPerFlowPerPressure', json_schema_extra={'note': 'Used to indicate which sizing factor is used to calculate Design Power Consumption. PowerPerFlow indicates that Design Electric Power per Unit Flow Rate is used as scaling factor. Design Power Cons...'})
    design_electric_power_per_unit_flow_rate: float | None = Field(default=348701.1, gt=0.0, json_schema_extra={'units': 'W/(m3/s)', 'note': 'Used to size Design Power Consumption from design flow rate'})
    design_shaft_power_per_unit_flow_rate_per_unit_head: float | None = Field(default=1.282051282, gt=0.0, json_schema_extra={'units': 'W/((m3/s)-Pa)', 'note': 'Used to size Design Power Consumption from design flow rate for head and motor efficiency'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class PumpVariableSpeed(IDFBaseModel):
    """This pump model is described in the ASHRAE secondary HVAC toolkit."""

    _idf_object_type: ClassVar[str] = "Pump:VariableSpeed"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_maximum_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    design_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    design_power_consumption: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'When autosized the type of scaling factor is chosen in the input field Design Power Sizing Method'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0, json_schema_extra={'note': 'This is the motor efficiency only. When the Design Power Consumption is autosized using PowerPerFlowPerPressure, the Design Shaft Power per Unit Flow Rate per Unit Head is used in addition to the m...'})
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    coefficient_1_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_2_of_the_part_load_performance_curve: float | None = Field(default=1.0)
    coefficient_3_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_4_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    design_minimum_flow_rate: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm3/s', 'note': 'When autosized the scaling factor is the input field Design Minimum Flow Rate Fraction'})
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(default='Continuous')
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rated flow rate of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump o...'})
    pump_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'This references any single independent variable polynomial curve in order to do pressure vs. flow calculations for this pump. The available types are then: Linear, Quadratic, Cubic, and Quartic The...'})
    impeller_diameter: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': '"D" in above expression in field A6'})
    vfd_control_type: Literal['ManualControl', 'PressureSetpointControl'] | None = Field(default=None)
    pump_rpm_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rpm of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump operations.'})
    minimum_pressure_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'units': 'Pa', 'object_list': ['ScheduleNames']})
    maximum_pressure_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'units': 'Pa', 'object_list': ['ScheduleNames']})
    minimum_rpm_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'units': 'rev/min', 'object_list': ['ScheduleNames']})
    maximum_rpm_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'units': 'rev/min', 'object_list': ['ScheduleNames']})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used pump losses transferred to zone as internal gains'})
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'optional. If zone identified in previous field then this determines the split between convection and radiation for the skin losses'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure'] | None = Field(default='PowerPerFlowPerPressure', json_schema_extra={'note': 'Used to indicate which sizing factor is used to calculate Design Power Consumption. PowerPerFlow indicates that Design Electric Power per Unit Flow Rate is used as scaling factor. Design Power Cons...'})
    design_electric_power_per_unit_flow_rate: float | None = Field(default=348701.1, gt=0.0, json_schema_extra={'units': 'W/(m3/s)', 'note': 'Used to size Design Power Consumption from design flow rate'})
    design_shaft_power_per_unit_flow_rate_per_unit_head: float | None = Field(default=1.282051282, gt=0.0, json_schema_extra={'units': 'W/((m3/s)-Pa)', 'note': 'Used to size Design Power Consumption from design flow rate for head and motor efficiency'})
    design_minimum_flow_rate_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'note': 'Used to size Design Minimum Flow Rate'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})


class PumpVariableSpeedCondensate(IDFBaseModel):
    """This pump model is described in the ASHRAE secondary HVAC toolkit. Variable
Speed Condensate pump for Steam Systems"""

    _idf_object_type: ClassVar[str] = "Pump:VariableSpeed:Condensate"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    design_steam_volume_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s', 'note': 'this is the volume of steam before condensation, the volume of condensate is much lower and calculated from steam density'})
    design_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    design_power_consumption: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'When autosized the type of scaling factor is chosen in the input field Design Power Sizing Method'})
    motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0, json_schema_extra={'note': 'This is the motor efficiency only. When the Design Power Consumption is autosized using PowerPerFlowPerPressure, the Design Shaft Power per Unit Flow Rate per Unit Head is used in addition to the m...'})
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    coefficient_1_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_2_of_the_part_load_performance_curve: float | None = Field(default=1.0)
    coefficient_3_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    coefficient_4_of_the_part_load_performance_curve: float | None = Field(default=0.0)
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the rated flow rate of the pump on a time basis. Default is that the pump is on and runs according to its other operational requirements specified above. The schedule is for special pump o...'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'optional, if used pump losses transferred to zone as internal gains'})
    skin_loss_radiative_fraction: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'optional. If zone identified in previous field then this determines the split between convection and radiation for the skin losses'})
    design_power_sizing_method: Literal['', 'PowerPerFlow', 'PowerPerFlowPerPressure'] | None = Field(default='PowerPerFlowPerPressure', json_schema_extra={'note': 'Used to indicate which sizing factor is used to calculate Design Power Consumption. PowerPerFlow indicates that Design Electric Power per Unit Flow Rate is used as scaling factor. Design Power Cons...'})
    design_electric_power_per_unit_flow_rate: float | None = Field(default=348701.1, gt=0.0, json_schema_extra={'units': 'W/(m3/s)', 'note': 'Used to size Design Power Consumption from design flow rate'})
    design_shaft_power_per_unit_flow_rate_per_unit_head: float | None = Field(default=1.282051282, gt=0.0, json_schema_extra={'units': 'W/((m3/s)-Pa)', 'note': 'Used to size Design Power Consumption from design flow rate for head and motor efficiency'})
    end_use_subcategory: str | None = Field(default='General', json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'})

