"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Energy Management System (EMS)
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    ConstructionNamesRef,
    ErlProgramNamesRef,
    MultivariateFunctionsRef,
    QuadvariateFunctionsRef,
    QuintvariateFunctionsRef,
    TrivariateFunctionsRef,
    UnivariateFunctionsRef,
)


class EnergyManagementSystemGlobalVariableVariablesItem(IDFBaseModel):
    """Nested object type for array items."""
    erl_variable_name: str = Field(..., json_schema_extra={'note': 'no spaces allowed in name'})


class EnergyManagementSystemProgramLinesItem(IDFBaseModel):
    """Nested object type for array items."""
    program_line: str | None = Field(default=None)


class EnergyManagementSystemProgramCallingManagerProgramsItem(IDFBaseModel):
    """Nested object type for array items."""
    program_name: ErlProgramNamesRef = Field(..., json_schema_extra={'object_list': ['ErlProgramNames'], 'note': 'no spaces allowed in name'})



class EnergyManagementSystemActuator(IDFBaseModel):
    """Hardware portion of EMS used to set up actuators in the model"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:Actuator"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces or other special characters (-,+,/,\\) allowed in name'})
    actuated_component_unique_name: str = Field(...)
    actuated_component_type: str = Field(...)
    actuated_component_control_type: str = Field(...)


class EnergyManagementSystemConstructionIndexVariable(IDFBaseModel):
    """Declares EMS variable that identifies a construction"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:ConstructionIndexVariable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    construction_object_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})


class EnergyManagementSystemCurveOrTableIndexVariable(IDFBaseModel):
    """Declares EMS variable that identifies a curve or table"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:CurveOrTableIndexVariable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    curve_or_table_object_name: BivariateFunctionsRef | MultivariateFunctionsRef | QuadvariateFunctionsRef | QuintvariateFunctionsRef | TrivariateFunctionsRef | UnivariateFunctionsRef = Field(..., json_schema_extra={'object_list': ['BivariateFunctions', 'MultivariateFunctions', 'QuadvariateFunctions', 'QuintvariateFunctions', 'TrivariateFunctions', 'UnivariateFunctions']})


class EnergyManagementSystemGlobalVariable(IDFBaseModel):
    """Declares Erl variable as having global scope No spaces allowed in names used
for Erl variables"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:GlobalVariable"
    variables: list[EnergyManagementSystemGlobalVariableVariablesItem] | None = Field(default=None)


class EnergyManagementSystemInternalVariable(IDFBaseModel):
    """Declares EMS variable as an internal data variable"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:InternalVariable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    internal_data_index_key_name: str | None = Field(default=None)
    internal_data_type: str = Field(...)


class EnergyManagementSystemMeteredOutputVariable(IDFBaseModel):
    """This object sets up an EnergyPlus output variable from an Erl variable"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:MeteredOutputVariable"
    name: str = Field(...)
    ems_variable_name: str = Field(..., json_schema_extra={'note': 'must be an acceptable EMS variable, no spaces'})
    update_frequency: Literal['SystemTimestep', 'ZoneTimestep'] = Field(...)
    ems_program_or_subroutine_name: str | None = Field(default=None, json_schema_extra={'note': 'optional for global scope variables, required for local scope variables'})
    resource_type: Literal['Coal', 'CondensateWaterCollected', 'Diesel', 'DistrictCooling', 'DistrictHeatingSteam', 'DistrictHeatingWater', 'Electricity', 'ElectricityProducedOnSite', 'EnergyTransfer', 'FuelOilNo1', 'FuelOilNo2', 'Gasoline', 'MainsWaterSupply', 'NaturalGas', 'OnSiteWaterProduced', 'OtherFuel1', 'OtherFuel2', 'Propane', 'RainWaterCollected', 'SolarAirHeating', 'SolarWaterHeating', 'WaterUse', 'WellWaterDrawn'] = Field(..., json_schema_extra={'note': 'choose the type of fuel, water, electricity, pollution or heat rate that should be metered.'})
    group_type: Literal['Building', 'HVAC', 'Plant', 'System'] = Field(..., json_schema_extra={'note': 'choose a general classification, building (internal services), HVAC (air systems), or plant (hydronic systems), or system'})
    end_use_category: Literal['Baseboard', 'Boilers', 'Chillers', 'Cooling', 'CoolingCoils', 'ExteriorEquipment', 'ExteriorLights', 'Fans', 'HeatRecovery', 'HeatRecoveryForCooling', 'HeatRecoveryForHeating', 'HeatRejection', 'Heating', 'HeatingCoils', 'Humidifier', 'InteriorEquipment', 'InteriorLights', 'OnSiteGeneration', 'Pumps', 'Refrigeration', 'WaterSystems'] = Field(..., json_schema_extra={'note': 'choose how the metered output should be classified for end-use category'})
    end_use_subcategory: str | None = Field(default=None, json_schema_extra={'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table. enter a user-defined subcategory for this metered output'})
    units: str | None = Field(default=None, json_schema_extra={'note': 'optional but will result in dimensionless units for blank EnergyPlus units are standard SI units'})


class EnergyManagementSystemOutputVariable(IDFBaseModel):
    """This object sets up an EnergyPlus output variable from an Erl variable"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:OutputVariable"
    name: str = Field(...)
    ems_variable_name: str = Field(..., json_schema_extra={'note': 'must be an acceptable EMS variable'})
    type_of_data_in_variable: Literal['Averaged', 'Summed'] = Field(...)
    update_frequency: Literal['SystemTimestep', 'ZoneTimestep'] = Field(...)
    ems_program_or_subroutine_name: str | None = Field(default=None, json_schema_extra={'note': 'optional for global scope variables, required for local scope variables'})
    units: str | None = Field(default=None, json_schema_extra={'note': 'optional but will result in dimensionless units for blank EnergyPlus units are standard SI units'})


class EnergyManagementSystemProgram(IDFBaseModel):
    """This input defines an Erl program Each field after the name is a line of EMS
Runtime Language"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:Program"
    name: str = Field(..., json_schema_extra={'note': 'no spaces allowed in name'})
    lines: list[EnergyManagementSystemProgramLinesItem] = Field(...)


class EnergyManagementSystemProgramCallingManager(IDFBaseModel):
    """Input EMS program. a program needs a name a description of when it should be
called and then lines of program code for EMS Runtime language"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:ProgramCallingManager"
    name: str = Field(..., json_schema_extra={'note': 'no spaces allowed in name'})
    energyplus_model_calling_point: Literal['AfterComponentInputReadIn', 'AfterNewEnvironmentWarmUpIsComplete', 'AfterPredictorAfterHVACManagers', 'AfterPredictorBeforeHVACManagers', 'BeginNewEnvironment', 'BeginTimestepBeforePredictor', 'BeginZoneTimestepAfterInitHeatBalance', 'BeginZoneTimestepBeforeInitHeatBalance', 'BeginZoneTimestepBeforeSetCurrentWeather', 'EndOfSystemSizing', 'EndOfSystemTimestepAfterHVACReporting', 'EndOfSystemTimestepBeforeHVACReporting', 'EndOfZoneSizing', 'EndOfZoneTimestepAfterZoneReporting', 'EndOfZoneTimestepBeforeZoneReporting', 'InsideHVACSystemIterationLoop', 'UnitarySystemSizing', 'UserDefinedComponentModel'] | None = Field(default=None)
    programs: list[EnergyManagementSystemProgramCallingManagerProgramsItem] | None = Field(default=None)


class EnergyManagementSystemSensor(IDFBaseModel):
    """Declares EMS variable as a sensor a list of output variables and meters that
can be reported are available after a run on the report (.rdd) or meter
dictionary file (.mdd) if the Output:VariableDictionary has been requested."""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:Sensor"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    output_variable_or_output_meter_index_key_name: str | None = Field(default=None)
    output_variable_or_output_meter_name: str = Field(...)


class EnergyManagementSystemSubroutine(IDFBaseModel):
    """This input defines an Erl program subroutine Each field after the name is a
line of EMS Runtime Language"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:Subroutine"
    name: str = Field(..., json_schema_extra={'note': 'no spaces allowed in name'})
    lines: list[EnergyManagementSystemProgramLinesItem] | None = Field(default=None)


class EnergyManagementSystemTrendVariable(IDFBaseModel):
    """This object sets up an EMS trend variable from an Erl variable A trend
variable logs values across timesteps"""

    _idf_object_type: ClassVar[str] = "EnergyManagementSystem:TrendVariable"
    name: str = Field(..., json_schema_extra={'note': 'no spaces allowed in name'})
    ems_variable_name: str = Field(..., json_schema_extra={'note': 'must be a global scope EMS variable'})
    number_of_timesteps_to_be_logged: int = Field(..., ge=1)

