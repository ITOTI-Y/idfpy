"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: External Interface
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    FMUFileNameRef,
    ScheduleTypeLimitsNamesRef,
)



class ExternalInterface(IDFBaseModel):
    """This object activates the external interface of EnergyPlus. If the object
ExternalInterface is present, then all ExtnernalInterface:* objects will
receive their values from the BCVTB interface or from FMUs at each zone time
step. If this object is not present, then the values of these objects will
be fixed at the value declared in the \"initial value\" field of the
corresponding object, and a warning will be written to the EnergyPlus error
file."""

    _idf_object_type: ClassVar[str] = "ExternalInterface"
    name_of_external_interface: Literal['FunctionalMockupUnitExport', 'FunctionalMockupUnitImport', 'PtolemyServer'] = Field(..., json_schema_extra={'note': 'Name of External Interface Currently, the only valid entries are PtolemyServer, FunctionalMockupUnitImport, and FunctionalMockupUnitExport.'})


class ExternalInterfaceActuator(IDFBaseModel):
    """Hardware portion of EMS used to set up actuators in the model"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:Actuator"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    actuated_component_unique_name: str = Field(...)
    actuated_component_type: str = Field(...)
    actuated_component_control_type: str = Field(...)
    optional_initial_value: float | None = Field(default=None, json_schema_extra={'note': 'If specified, it is used during warm-up and system sizing. If not specified, then the actuator only overwrites the actuated component after the warm-up and system sizing.'})


class ExternalInterfaceFunctionalMockupUnitExportFromVariable(IDFBaseModel):
    """This object declares an FMU input variable"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitExport:From:Variable"
    output_variable_index_key_name: str = Field(...)
    output_variable_name: str = Field(...)
    fmu_variable_name: str = Field(...)


class ExternalInterfaceFunctionalMockupUnitExportToActuator(IDFBaseModel):
    """Hardware portion of EMS used to set up actuators in the model that are
dynamically updated from the FMU."""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitExport:To:Actuator"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a read-only variable for use in Erl programs no spaces allowed in name'})
    actuated_component_unique_name: str = Field(...)
    actuated_component_type: str = Field(...)
    actuated_component_control_type: str = Field(...)
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceFunctionalMockupUnitExportToSchedule(IDFBaseModel):
    """This objects contains only one value, which is used during the first call of
EnergyPlus"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitExport:To:Schedule"
    schedule_name: str = Field(...)
    schedule_type_limits_names: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceFunctionalMockupUnitExportToVariable(IDFBaseModel):
    """Declares Erl variable as having global scope No spaces allowed in names used
for Erl variables"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitExport:To:Variable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceFunctionalMockupUnitImport(IDFBaseModel):
    """This object declares an FMU"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitImport"
    fmu_file_name: str = Field(...)
    fmu_timeout: float | None = Field(default=0.0, json_schema_extra={'units': 'ms', 'note': 'in milli-seconds'})
    fmu_loggingon: int | None = Field(default=0)


class ExternalInterfaceFunctionalMockupUnitImportFromVariable(IDFBaseModel):
    """This object declares an FMU input variable"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitImport:From:Variable"
    output_variable_index_key_name: str = Field(...)
    output_variable_name: str = Field(...)
    fmu_file_name: FMUFileNameRef = Field(..., json_schema_extra={'object_list': ['FMUFileName']})
    fmu_instance_name: str = Field(...)
    fmu_variable_name: str = Field(...)


class ExternalInterfaceFunctionalMockupUnitImportToActuator(IDFBaseModel):
    """Hardware portion of EMS used to set up actuators in the model that are
dynamically updated from the FMU."""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitImport:To:Actuator"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a read-only variable for use in Erl programs no spaces allowed in name'})
    actuated_component_unique_name: str = Field(...)
    actuated_component_type: str = Field(...)
    actuated_component_control_type: str = Field(...)
    fmu_file_name: FMUFileNameRef = Field(..., json_schema_extra={'object_list': ['FMUFileName']})
    fmu_instance_name: str = Field(...)
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceFunctionalMockupUnitImportToSchedule(IDFBaseModel):
    """This objects contains only one value, which is used during the first call of
EnergyPlus"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitImport:To:Schedule"
    name: str = Field(...)
    schedule_type_limits_names: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    fmu_file_name: FMUFileNameRef = Field(..., json_schema_extra={'object_list': ['FMUFileName']})
    fmu_instance_name: str = Field(...)
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceFunctionalMockupUnitImportToVariable(IDFBaseModel):
    """Declares Erl variable as having global scope No spaces allowed in names used
for Erl variables"""

    _idf_object_type: ClassVar[str] = "ExternalInterface:FunctionalMockupUnitImport:To:Variable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    fmu_file_name: FMUFileNameRef = Field(..., json_schema_extra={'object_list': ['FMUFileName']})
    fmu_instance_name: str = Field(...)
    fmu_variable_name: str = Field(...)
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during the first call of EnergyPlus.'})


class ExternalInterfaceSchedule(IDFBaseModel):
    """A ExternalInterface:Schedule contains only one value, which is used during
the warm-up period and the system sizing."""

    _idf_object_type: ClassVar[str] = "ExternalInterface:Schedule"
    name: str = Field(...)
    schedule_type_limits_name: ScheduleTypeLimitsNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleTypeLimitsNames']})
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during warm-up and system sizing.'})


class ExternalInterfaceVariable(IDFBaseModel):
    """This input object is similar to EnergyManagementSystem:GlobalVariable.
However, at the beginning of each zone time step, its value is set to the
value received from the external interface. During the warm-up period and
the system sizing, its value is set to the value specified by the field
\"initial value.\" This object can be used to move data into Erl
subroutines."""

    _idf_object_type: ClassVar[str] = "ExternalInterface:Variable"
    name: str = Field(..., json_schema_extra={'note': 'This name becomes a variable for use in Erl programs no spaces allowed in name'})
    initial_value: float = Field(..., json_schema_extra={'note': 'Used during warm-up and system sizing.'})

