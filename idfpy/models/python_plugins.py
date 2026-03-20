"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Python Plugin System
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel


class PythonPluginSearchPathsPySearchPathsItem(IDFBaseModel):
    """Nested object type for array items."""
    search_path: str | None = Field(default=None)


class PythonPluginVariablesGlobalPyVarsItem(IDFBaseModel):
    """Nested object type for array items."""
    variable_name: str | None = Field(default=None, json_schema_extra={'note': 'This variable is used to identify and create a shared variable in EnergyPlus. This variable can then be used by all running Python Plugin instances.'})



class PythonPluginInstance(IDFBaseModel):
    """A single plugin to be executed during the simulation, which can contain
multiple calling points for the same class instance by overriding multiple
calling point methods."""

    _idf_object_type: ClassVar[str] = "PythonPlugin:Instance"
    name: str = Field(..., json_schema_extra={'note': 'This is the name used to represent this plugin in traditional EMS fields'})
    run_during_warmup_days: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If this field is enabled, the plugin will be executed during warmup days, otherwise it will only be executed once warmup is completed and the actual run period begins'})
    python_module_name: str = Field(..., json_schema_extra={'note': 'This is the name of the Python file, without a file extension. For "plugin_b.py", use just "plugin_b". The Python plugin file must be on the plugin system search path to be found during a simulatio...'})
    plugin_class_name: str = Field(..., json_schema_extra={'note': 'This is the name of the class to be executed as a plugin during a simulation The class must inherit the EnergyPlusPlugin base class'})


class PythonPluginOutputVariable(IDFBaseModel):
    """This object sets up an EnergyPlus output variable from a Python Plugin
variable"""

    _idf_object_type: ClassVar[str] = "PythonPlugin:OutputVariable"
    name: str = Field(...)
    python_plugin_variable_name: str = Field(..., json_schema_extra={'note': 'Must be listed in the PythonPlugin:Variables object'})
    type_of_data_in_variable: Literal['Averaged', 'Metered', 'Summed'] = Field(..., json_schema_extra={'note': 'If Metered is selected, the variable is automatically set to a "Summed" type, and the Resource Type, Group Type, and End-Use Subcategory fields on this object are required'})
    update_frequency: Literal['SystemTimestep', 'ZoneTimestep'] = Field(...)
    units: str | None = Field(default=None, json_schema_extra={'note': 'optional but will result in dimensionless units for blank EnergyPlus units are standard SI units'})
    resource_type: Literal['Coal', 'CondensateWaterCollected', 'Diesel', 'DistrictCooling', 'DistrictHeatingSteam', 'DistrictHeatingWater', 'Electricity', 'ElectricityProducedOnSite', 'EnergyTransfer', 'FuelOilNo1', 'FuelOilNo2', 'Gasoline', 'MainsWaterSupply', 'NaturalGas', 'OnSiteWaterProduced', 'OtherFuel1', 'OtherFuel2', 'Propane', 'RainWaterCollected', 'SolarAirHeating', 'SolarWaterHeating', 'WaterUse', 'WellWaterDrawn'] | None = Field(default=None, json_schema_extra={'note': 'This field is optional for regular output variables with "Type of Data in Variable" set to either Averaged or Summed. For Metered variables, this field is required. Choose the type of fuel, water, ...'})
    group_type: Literal['Building', 'HVAC', 'Plant', 'System'] | None = Field(default=None, json_schema_extra={'note': 'This field is optional for regular output variables with "Type of Data in Variable" set to either Averaged or Summed. For Metered variables, this field is required. Choose a general classification,...'})
    end_use_category: Literal['Baseboard', 'Boilers', 'Chillers', 'Cooling', 'CoolingCoils', 'ExteriorEquipment', 'ExteriorLights', 'Fans', 'HeatRecovery', 'HeatRecoveryForCooling', 'HeatRecoveryForHeating', 'HeatRejection', 'Heating', 'HeatingCoils', 'Humidifier', 'InteriorEquipment', 'InteriorLights', 'OnSiteGeneration', 'Pumps', 'Refrigeration', 'WaterSystems'] | None = Field(default=None, json_schema_extra={'note': 'This field is optional for regular output variables with "Type of Data in Variable" set to either Averaged or Summed. For Metered variables, this field is required. Choose how the metered output sh...'})
    end_use_subcategory: str | None = Field(default=None, json_schema_extra={'note': 'This field is always optional. For regular output variables with "Type of Data in Variable" set to either Averaged or Summed, this field is completely ignored. For Metered variables, this field is ...'})


class PythonPluginSearchPaths(IDFBaseModel):
    """Add directories to the search path for Python plugin modules The directory
containing the EnergyPlus executable file is automatically added so that the
Python interpreter can find the packaged up pyenergyplus Python package. By
default, the current working directory and input file directory are also
added to the search path. However, this object allows modifying this
behavior. With this object, searching these directories can be disabled, and
users can add supplemental search paths that point to libraries of plugin
scripts."""

    _idf_object_type: ClassVar[str] = "PythonPlugin:SearchPaths"
    name: str = Field(...)
    add_current_working_directory_to_search_path: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'Adding the current working directory allows Python to find plugin scripts in the current directory.'})
    add_input_file_directory_to_search_path: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'Enabling this will allow Python to find plugin scripts in the same directory as the running input file, even if that is not the current working directory.'})
    add_epin_environment_variable_to_search_path: Literal['', 'No', 'Yes'] | None = Field(default='Yes', json_schema_extra={'note': 'The "epin" environment variable is set by some EnergyPlus interfaces in order to let EnergyPlus find external files in special locations. If this is enabled, and that variable is set, the value of ...'})
    py_search_paths: list[PythonPluginSearchPathsPySearchPathsItem] | None = Field(default=None)


class PythonPluginTrendVariable(IDFBaseModel):
    """This object sets up a Python plugin trend variable from an Python plugin
variable A trend variable logs values across timesteps"""

    _idf_object_type: ClassVar[str] = "PythonPlugin:TrendVariable"
    name: str = Field(...)
    name_of_a_python_plugin_variable: str = Field(...)
    number_of_timesteps_to_be_logged: int = Field(..., ge=1)


class PythonPluginVariables(IDFBaseModel):
    """This object defines name identifiers for custom Python Plugin variable data
that should be shared among all running Python Plugins."""

    _idf_object_type: ClassVar[str] = "PythonPlugin:Variables"
    name: str = Field(..., json_schema_extra={'note': 'This object name is purely for reporting and diagnostics'})
    global_py_vars: list[PythonPluginVariablesGlobalPyVarsItem] | None = Field(default=None)

