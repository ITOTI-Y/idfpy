"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Operational Faults
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BoilersRef,
    ChillersRef,
    CoolingCoilNameRef,
    CoolingCoilSystemNameRef,
    CoolingTowersRef,
    CoolingTowersWithUARef,
    DOAToZonalUnitRef,
    FansCVandOnOffandVAVRef,
    FansSystemModelRef,
    HeatingCoilNameRef,
    HeatingCoilsDesuperheaterRef,
    HeatingCoilsElectricMultiStageRef,
    HeatingCoilsGasMultiStageRef,
    HeatingCoilSystemNameRef,
    OAControllerNamesRef,
    ScheduleNamesRef,
    SimpleCoilsRef,
    ThermostatOffsetFaultsRef,
    UnivariateFunctionsRef,
    WaterCoilControllersRef,
    ZoneControlHumidistatNamesRef,
    ZoneControlThermostaticNamesRef,
)


class FaultModelEnthalpySensorOffsetOutdoorAir(IDFBaseModel):
    """This object describes outdoor air enthalpy sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:EnthalpySensorOffset:OutdoorAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    controller_object_type: Literal['Controller:OutdoorAir'] = Field(...)
    controller_object_name: OAControllerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OAControllerNames']}
    )
    enthalpy_sensor_offset: float | None = Field(
        default=0.0, gt=-20000.0, lt=20000.0, json_schema_extra={'units': 'J/kg'}
    )


class FaultModelEnthalpySensorOffsetReturnAir(IDFBaseModel):
    """This object describes return air enthalpy sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:EnthalpySensorOffset:ReturnAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    controller_object_type: Literal['Controller:OutdoorAir'] = Field(...)
    controller_object_name: OAControllerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OAControllerNames']}
    )
    enthalpy_sensor_offset: float | None = Field(
        default=0.0, gt=-20000.0, lt=20000.0, json_schema_extra={'units': 'J/kg'}
    )


class FaultModelFoulingAirFilter(IDFBaseModel):
    """This object describes fault of dirty air filters"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:AirFilter'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:VariableVolume'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Choose the type of the fan Support for Fan:SystemModel is pending'
        },
    )
    fan_name: FansCVandOnOffandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel'],
            'note': 'Enter the name of a fan object',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    pressure_fraction_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule describing the variations of the fan pressure rise in terms of multipliers to the fan design pressure rise',
        },
    )
    fan_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'The curve describes the relationship between the fan pressure rise and air flow rate',
        },
    )


class FaultModelFoulingBoiler(IDFBaseModel):
    """This object describes the fouling fault of boilers with water-based heat
    exchangers"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:Boiler'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    boiler_object_type: Literal['Boiler:HotWater'] = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the type of a boiler object The fault applies to the hot-water boilers'
        },
    )
    boiler_object_name: BoilersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Boilers'],
            'note': 'Enter the name of a Boiler object',
        },
    )
    fouling_factor: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The factor indicates the decrease of the nominal capacity of the boiler It is the ratio between the nominal capacity at fouling case and that at fault free case',
        },
    )


class FaultModelFoulingChiller(IDFBaseModel):
    """This object describes the fouling fault of chillers with water-cooled
    condensers"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:Chiller'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    chiller_object_type: Literal[
        'Chiller:CombustionTurbine',
        'Chiller:ConstantCOP',
        'Chiller:Electric',
        'Chiller:Electric:EIR',
        'Chiller:Electric:ReformulatedEIR',
        'Chiller:EngineDriven',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the type of a chiller object The fault applies to the chillers with water-cooled condensers'
        },
    )
    chiller_object_name: ChillersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Chillers'],
            'note': 'Enter the name of a chiller object',
        },
    )
    fouling_factor: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The factor indicates the decrease of the nominal capacity of the chiller It is the ratio between the nominal capacity at fouling case and that at fault free case',
        },
    )


class FaultModelFoulingCoil(IDFBaseModel):
    """This object describes fouling water heating or cooling coils"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:Coil'
    name: str = Field(...)
    coil_name: SimpleCoilsRef = Field(
        ..., json_schema_extra={'object_list': ['SimpleCoils']}
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    fouling_input_method: Literal['', 'FouledUARated', 'FoulingFactor'] | None = Field(
        default='FouledUARated'
    )
    uafouled: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'Fouling coil UA value under rating conditions For Fouling Input Method: FouledUARated',
        },
    )
    water_side_fouling_factor: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm2-K/W',
            'note': 'For Fouling Input Method: FoulingFactor',
        },
    )
    air_side_fouling_factor: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm2-K/W',
            'note': 'For Fouling Input Method: FoulingFactor',
        },
    )
    outside_coil_surface_area: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm2',
            'note': 'For Fouling Input Method: FoulingFactor',
        },
    )
    inside_to_outside_coil_surface_area_ratio: float | None = Field(
        default=0.07,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'For Fouling Input Method: FoulingFactor',
        },
    )


class FaultModelFoulingCoolingTower(IDFBaseModel):
    """This object describes the fault of fouling cooling towers"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:CoolingTower'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cooling_tower_object_type: Literal[
        'CoolingTower:SingleSpeed',
        'CoolingTower:TwoSpeed',
        'CoolingTower:VariableSpeed:MERKEL',
    ] = Field(
        ..., json_schema_extra={'note': 'Enter the type of the cooling tower affected'}
    )
    cooling_tower_object_name: CoolingTowersWithUARef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingTowersWithUA'],
            'note': 'Enter the name of the cooling tower affected',
        },
    )
    reference_ua_reduction_factor: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Factor describing the tower UA reduction due to fouling It is the ratio between the UA value at fouling case and that at fault free case It is applicable to both the Design UA and Free Convection U...',
        },
    )


class FaultModelFoulingEvaporativeCooler(IDFBaseModel):
    """This object describes the fouling fault of the wetted coil evaporative
    cooler"""

    _idf_object_type: ClassVar[str] = 'FaultModel:Fouling:EvaporativeCooler'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    evaporative_cooler_object_type: Literal['EvaporativeCooler:Indirect:WetCoil'] = (
        Field(
            ...,
            json_schema_extra={
                'note': 'Enter the type of a Evaporative Cooler object The fault applies to the wetted coil evaporative cooler The fault does not apply to direct evaporative coolers or the dry coil indirect evaporative coo...'
            },
        )
    )
    evaporative_cooler_object_name: ChillersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Chillers'],
            'note': 'Enter the name of aN Evaporative Cooler object',
        },
    )
    fouling_factor: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The factor indicates the decrease of the indirect stage efficiency It is the ratio between the indirect stage efficiency at fouling case and that at fault free case',
        },
    )


class FaultModelHumidistatOffset(IDFBaseModel):
    """This object describes fault of humidistat offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:HumidistatOffset'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    humidistat_name: ZoneControlHumidistatNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneControlHumidistatNames'],
            'note': 'Enter the name of a ZoneControl:Humidistat object.',
        },
    )
    humidistat_offset_type: (
        Literal['', 'ThermostatOffsetDependent', 'ThermostatOffsetIndependent'] | None
    ) = Field(
        default='ThermostatOffsetIndependent',
        json_schema_extra={
            'note': 'Two types are available: Type ThermostatOffsetIndependent Type ThermostatOffsetDependent'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is applicable for Type ThermostatOffsetIndependent',
        },
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is applicable for Type ThermostatOffsetIndependent',
        },
    )
    reference_humidistat_offset: float | None = Field(
        default=5.0,
        gt=-20.0,
        lt=20.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Required field for Type ThermostatOffsetIndependent',
        },
    )
    related_thermostat_offset_fault_name: ThermostatOffsetFaultsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ThermostatOffsetFaults'],
            'note': 'Enter the name of a FaultModel:ThermostatOffset object Required field for Type ThermostatOffsetDependent',
        },
    )


class FaultModelHumiditySensorOffsetOutdoorAir(IDFBaseModel):
    """This object describes outdoor air humidity sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:HumiditySensorOffset:OutdoorAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    controller_object_type: Literal['Controller:OutdoorAir'] = Field(...)
    controller_object_name: OAControllerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OAControllerNames']}
    )
    humidity_sensor_offset: float | None = Field(
        default=0.0, gt=-0.02, lt=0.02, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )


class FaultModelTemperatureSensorOffsetChillerSupplyWater(IDFBaseModel):
    """This object describes fault of chiller supply water temperature sensor
    offset"""

    _idf_object_type: ClassVar[str] = (
        'FaultModel:TemperatureSensorOffset:ChillerSupplyWater'
    )
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    chiller_object_type: Literal[
        'Chiller:Absorption',
        'Chiller:Absorption:Indirect',
        'Chiller:CombustionTurbine',
        'Chiller:ConstantCOP',
        'Chiller:Electric',
        'Chiller:Electric:EIR',
        'Chiller:Electric:ReformulatedEIR',
        'Chiller:EngineDriven',
    ] = Field(..., json_schema_extra={'note': 'Enter the type of a chiller object'})
    chiller_object_name: ChillersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Chillers'],
            'note': 'Enter the name of a chiller object',
        },
    )
    reference_sensor_offset: float | None = Field(
        default=0.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )


class FaultModelTemperatureSensorOffsetCoilSupplyAir(IDFBaseModel):
    """This object describes fault of coil supply air temperature sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:TemperatureSensorOffset:CoilSupplyAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    coil_object_type: Literal[
        'AirLoopHVAC:UnitarySystem',
        'Coil:Cooling:Water',
        'Coil:Cooling:Water:Detailedgeometry',
        'Coil:Heating:Desuperheater',
        'Coil:Heating:Electric',
        'Coil:Heating:Gas',
        'Coil:Heating:Steam',
        'Coil:Heating:Water',
        'CoilSystem:Cooling:DX',
        'CoilSystem:Heating:DX',
    ] = Field(..., json_schema_extra={'note': 'Enter the type of the coil affected'})
    coil_object_name: (
        CoolingCoilNameRef
        | CoolingCoilSystemNameRef
        | DOAToZonalUnitRef
        | HeatingCoilNameRef
        | HeatingCoilSystemNameRef
        | HeatingCoilsDesuperheaterRef
        | HeatingCoilsElectricMultiStageRef
        | HeatingCoilsGasMultiStageRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'CoolingCoilName',
                'CoolingCoilSystemName',
                'DOAToZonalUnit',
                'HeatingCoilName',
                'HeatingCoilSystemName',
                'HeatingCoilsDesuperheater',
                'HeatingCoilsElectricMultiStage',
                'HeatingCoilsGasMultiStage',
            ],
            'note': 'Enter the name of the coil affected',
        },
    )
    water_coil_controller_name: WaterCoilControllersRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['WaterCoilControllers'],
            'note': 'Enter the name of controller for the water coil affected Required for water coils',
        },
    )
    reference_sensor_offset: float | None = Field(
        default=0.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )


class FaultModelTemperatureSensorOffsetCondenserSupplyWater(IDFBaseModel):
    """This object describes fault of condenser supply water temperature sensor
    offset"""

    _idf_object_type: ClassVar[str] = (
        'FaultModel:TemperatureSensorOffset:CondenserSupplyWater'
    )
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cooling_tower_object_type: Literal[
        'CoolingTower:SingleSpeed',
        'CoolingTower:TwoSpeed',
        'CoolingTower:VariableSpeed',
        'CoolingTower:VariableSpeed:MERKEL',
    ] = Field(
        ..., json_schema_extra={'note': 'Enter the type of the cooling tower affected'}
    )
    cooling_tower_object_name: CoolingTowersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingTowers'],
            'note': 'Enter the name of the cooling tower affected',
        },
    )
    reference_sensor_offset: float | None = Field(
        default=0.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )


class FaultModelTemperatureSensorOffsetOutdoorAir(IDFBaseModel):
    """This object describes outdoor air temperature sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:TemperatureSensorOffset:OutdoorAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    controller_object_type: Literal['Controller:OutdoorAir'] = Field(...)
    controller_object_name: OAControllerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OAControllerNames']}
    )
    temperature_sensor_offset: float | None = Field(
        default=0.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )


class FaultModelTemperatureSensorOffsetReturnAir(IDFBaseModel):
    """This object describes return air temperature sensor offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:TemperatureSensorOffset:ReturnAir'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    controller_object_type: Literal['Controller:OutdoorAir'] = Field(...)
    controller_object_name: OAControllerNamesRef = Field(
        ..., json_schema_extra={'object_list': ['OAControllerNames']}
    )
    temperature_sensor_offset: float | None = Field(
        default=0.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )


class FaultModelThermostatOffset(IDFBaseModel):
    """This object describes fault of thermostat offset"""

    _idf_object_type: ClassVar[str] = 'FaultModel:ThermostatOffset'
    name: str = Field(..., json_schema_extra={'note': 'Enter the name of the fault'})
    thermostat_name: ZoneControlThermostaticNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneControlThermostaticNames'],
            'note': 'Enter the name of a ZoneControl:Thermostat object.',
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    severity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    reference_thermostat_offset: float | None = Field(
        default=2.0, gt=-10.0, lt=10.0, json_schema_extra={'units': 'deltaC'}
    )
