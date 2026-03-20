"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Demand Limiting Controls
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    DemandManagerNamesRef,
    ElectricEquipmentNamesRef,
    ExteriorLightsNamesRef,
    LightsNamesRef,
    OAControllerNamesRef,
    ScheduleNamesRef,
    ZoneControlThermostaticNamesRef,
)


class DemandManagerAssignmentListManagerDataItem(IDFBaseModel):
    """Nested object type for array items."""
    demandmanager_object_type: Literal['DemandManager:ElectricEquipment', 'DemandManager:ExteriorLights', 'DemandManager:Lights', 'DemandManager:Thermostats', 'DemandManager:Ventilation'] | None = Field(default=None)
    demandmanager_name: DemandManagerNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['DemandManagerNames']})


class DemandManagerElectricEquipmentEquipmentItem(IDFBaseModel):
    """Nested object type for array items."""
    electric_equipment_name: ElectricEquipmentNamesRef = Field(..., json_schema_extra={'object_list': ['ElectricEquipmentNames'], 'note': 'Enter the name of an ElectricEquipment object. if ZoneList option is used on the ElectricEquipment object, a single equipment object from that assignment can be selected by entering <Zone Name><spa...'})


class DemandManagerExteriorLightsLightsItem(IDFBaseModel):
    """Nested object type for array items."""
    exterior_lights_name: ExteriorLightsNamesRef = Field(..., json_schema_extra={'object_list': ['ExteriorLightsNames'], 'note': 'Enter the name of an Exterior:Lights object.'})


class DemandManagerLightsLightsItem(IDFBaseModel):
    """Nested object type for array items."""
    lights_name: LightsNamesRef = Field(..., json_schema_extra={'object_list': ['LightsNames'], 'note': 'Enter the name of an Lights object. if ZoneList option is used on the Lights object, a single lights object from that assignment can be selected by entering <Zone Name><space><Global Lights Object ...'})


class DemandManagerThermostatsThermostatsItem(IDFBaseModel):
    """Nested object type for array items."""
    thermostat_name: ZoneControlThermostaticNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneControlThermostaticNames'], 'note': 'Enter the name of a ZoneControl:Thermostat object. if ZoneList option is used on the ZoneControl:Thermostat object, a single thermostat object from that assignment can be selected by entering <Zone...'})


class DemandManagerVentilationControllersItem(IDFBaseModel):
    """Nested object type for array items."""
    controller_outdoor_air_name: OAControllerNamesRef = Field(..., json_schema_extra={'object_list': ['OAControllerNames'], 'note': 'Enter the name of a Controller:OutdoorAir object.'})



class DemandManagerAssignmentList(IDFBaseModel):
    """A high level control that makes demand limiting decisions based on a list of
possible demand limiting strategies."""

    _idf_object_type: ClassVar[str] = "DemandManagerAssignmentList"
    name: str = Field(...)
    meter_name: str = Field(...)
    demand_limit_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    demand_limit_safety_fraction: float = Field(..., ge=0.0)
    billing_period_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field should reference the same schedule as the month schedule name field of the UtilityCost:Tariff object, if used. If blank, defaults to regular divisions between months.'})
    peak_period_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This field should reference the same schedule as the period schedule name field of the UtilityCost:Tariff object, if used. If blank, defaults to always on peak.'})
    demand_window_length: int = Field(..., gt=0, json_schema_extra={'units': 'minutes'})
    demand_manager_priority: Literal['All', 'Sequential'] = Field(...)
    manager_data: list[DemandManagerAssignmentListManagerDataItem] | None = Field(default=None)


class DemandManagerElectricEquipment(IDFBaseModel):
    """used for demand limiting ElectricEquipment objects."""

    _idf_object_type: ClassVar[str] = "DemandManager:ElectricEquipment"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    limit_control: Literal['Fixed', 'Off'] = Field(...)
    minimum_limit_duration: int | None = Field(default=None, gt=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    maximum_limit_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    limit_step_change: float | None = Field(default=None, json_schema_extra={'note': 'Not yet implemented'})
    selection_control: Literal['All', 'RotateMany', 'RotateOne'] = Field(...)
    rotation_duration: int | None = Field(default=None, ge=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    equipment: list[DemandManagerElectricEquipmentEquipmentItem] | None = Field(default=None)


class DemandManagerExteriorLights(IDFBaseModel):
    """used for demand limiting Exterior:Lights objects."""

    _idf_object_type: ClassVar[str] = "DemandManager:ExteriorLights"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    limit_control: Literal['Fixed', 'Off'] = Field(...)
    minimum_limit_duration: int | None = Field(default=None, gt=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    maximum_limit_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    limit_step_change: float | None = Field(default=None, json_schema_extra={'note': 'Not yet implemented'})
    selection_control: Literal['All', 'RotateMany', 'RotateOne'] = Field(...)
    rotation_duration: int | None = Field(default=None, ge=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    lights: list[DemandManagerExteriorLightsLightsItem] | None = Field(default=None)


class DemandManagerLights(IDFBaseModel):
    """used for demand limiting Lights objects."""

    _idf_object_type: ClassVar[str] = "DemandManager:Lights"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    limit_control: Literal['Fixed', 'Off'] = Field(...)
    minimum_limit_duration: int | None = Field(default=None, gt=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    maximum_limit_fraction: float | None = Field(default=None, ge=0.0, le=1.0)
    limit_step_change: float | None = Field(default=None, json_schema_extra={'note': 'Not yet implemented'})
    selection_control: Literal['All', 'RotateMany', 'RotateOne'] = Field(...)
    rotation_duration: int | None = Field(default=None, ge=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    lights: list[DemandManagerLightsLightsItem] | None = Field(default=None)


class DemandManagerThermostats(IDFBaseModel):
    """used for demand limiting ZoneControl:Thermostat objects."""

    _idf_object_type: ClassVar[str] = "DemandManager:Thermostats"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    reset_control: Literal['Fixed', 'Off'] = Field(...)
    minimum_reset_duration: int | None = Field(default=None, gt=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    maximum_heating_setpoint_reset: float = Field(..., json_schema_extra={'units': 'C'})
    maximum_cooling_setpoint_reset: float = Field(..., json_schema_extra={'units': 'C'})
    reset_step_change: float | None = Field(default=None, json_schema_extra={'note': 'Not yet implemented'})
    selection_control: Literal['All', 'RotateMany', 'RotateOne'] = Field(...)
    rotation_duration: int | None = Field(default=None, ge=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    thermostats: list[DemandManagerThermostatsThermostatsItem] | None = Field(default=None)


class DemandManagerVentilation(IDFBaseModel):
    """used for demand limiting Controller:OutdoorAir objects."""

    _idf_object_type: ClassVar[str] = "DemandManager:Ventilation"
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this demand manager. Schedule value > 0 means the demand manager is available. If this field is blank, the DR is always available.'})
    limit_control: Literal['FixedRate', 'Off', 'ReductionRatio'] = Field(...)
    minimum_limit_duration: int | None = Field(default=None, gt=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    fixed_rate: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm3/s', 'note': 'Used in case when Limit strategy is set to FixedRate'})
    reduction_ratio: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used in case when Limit Control is set to ReductionRatio'})
    limit_step_change: float | None = Field(default=None, json_schema_extra={'note': 'Not yet implemented'})
    selection_control: Literal['', 'All', 'RotateMany', 'RotateOne'] | None = Field(default='All')
    rotation_duration: int | None = Field(default=None, ge=0, json_schema_extra={'units': 'minutes', 'note': 'If blank, duration defaults to the timestep'})
    controllers: list[DemandManagerVentilationControllersItem] | None = Field(default=None)

