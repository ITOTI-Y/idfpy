"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: HVAC Templates
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BoilersRef,
    ChillersRef,
    CompactHVACSystemConstantVolumeRef,
    CompactHVACSystemDualDuctRef,
    CompactHVACSystemUnitaryRef,
    CompactHVACSystemVAVRef,
    CompactHVACSystemVRFRef,
    CompactHVACThermostatsRef,
    CondenserOperationSchemesRef,
    CoolingTowersRef,
    DesignSpecificationOutdoorAirNamesRef,
    DesignSpecificationZoneAirDistributionNamesRef,
    DSOASpaceListNamesRef,
    HVACTemplateConstantVolumeZonesRef,
    HVACTemplateDOASSystemsRef,
    PlantOperationSchemesRef,
    ScheduleNamesRef,
    ZoneNamesRef,
)


class HVACTemplatePlantBoiler(IDFBaseModel):
    """This object adds a boiler to an HVACTemplate:Plant:HotWaterLoop or
    MixedWaterLoop."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Boiler'
    name: str = Field(...)
    boiler_type: Literal[
        'CondensingHotWaterBoiler', 'DistrictHotWater', 'HotWaterBoiler'
    ] = Field(...)
    capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    efficiency: float | None = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Not applicable  if Boiler Type is DistrictHotWater'
        },
    )
    fuel_type: (
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
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Not applicable  if Boiler Type is DistrictHotWater'
        },
    )
    priority: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If Hot Water Plant Operation Scheme Type=Default in HVACTemplate:Plant:HotWaterLoop, then equipment operates in priority order, 1, 2, 3, etc.'
        },
    )
    sizing_factor: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'},
    )
    minimum_part_load_ratio: float | None = Field(default=0.0, ge=0.0)
    maximum_part_load_ratio: float | None = Field(default=1.1, ge=0.0)
    optimum_part_load_ratio: float | None = Field(default=1.0, ge=0.0)
    water_outlet_upper_temperature_limit: float | None = Field(
        default=100.0, json_schema_extra={'units': 'C'}
    )
    template_plant_loop_type: Literal['HotWater', 'MixedWater'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specifies if this boiler serves a template hot water loop or mixed water loop If left blank, will serve a hot water loop if present, or a mixed water loop (if no hot water loop is present).'
        },
    )


class HVACTemplatePlantBoilerObjectReference(IDFBaseModel):
    """This object references a detailed boiler object and adds it to an
    HVACTemplate:Plant:HotWaterLoop or MixedWaterLoop. The user must create a
    complete detailed boiler object with all required curve or performance
    objects."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Boiler:ObjectReference'
    name: str = Field(..., json_schema_extra={'note': 'The name of this object.'})
    boiler_object_type: Literal['', 'Boiler:HotWater'] | None = Field(
        default='Boiler:HotWater'
    )
    boiler_name: BoilersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Boilers'],
            'note': 'The name of the detailed boiler object.',
        },
    )
    priority: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If Hot Water Plant Operation Scheme Type=Default in HVACTemplate:Plant:HotWaterLoop or MixedWaterLoop, then equipment operates in Priority order, 1, 2, 3, etc.'
        },
    )
    template_plant_loop_type: Literal['HotWater', 'MixedWater'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specifies if this boiler serves a template hot water loop or mixed water loop If left blank, will serve a hot water loop if present, or a mixed water loop (if no hot water loop is present).'
        },
    )


class HVACTemplatePlantChilledWaterLoop(IDFBaseModel):
    """Plant and condenser loops to serve all HVACTemplate chilled water coils,
    chillers, and towers."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:ChilledWaterLoop'
    name: str = Field(...)
    pump_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available Applies to both chilled water and condenser loop pumps',
        },
    )
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(
        default='Intermittent',
        json_schema_extra={
            'note': 'Applies to both chilled water and condenser loop pumps'
        },
    )
    chiller_plant_operation_scheme_type: (
        Literal['', 'Default', 'UserDefined'] | None
    ) = Field(
        default='Default',
        json_schema_extra={
            'note': 'Default operation type makes all equipment available at all times operating in order of Priority specified in HVACTemplate:Plant:Chiller objects.'
        },
    )
    chiller_plant_equipment_operation_schemes_name: PlantOperationSchemesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['PlantOperationSchemes'],
                'note': 'Name of a PlantEquipmentOperationSchemes object Ignored if Chiller Plant Operation Scheme Type = Default',
            },
        )
    )
    chilled_water_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    chilled_water_design_setpoint: float | None = Field(
        default=7.22,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Chilled Water Setpoint Schedule Name is specified.',
        },
    )
    chilled_water_pump_configuration: (
        Literal[
            '',
            'ConstantPrimaryNoSecondary',
            'ConstantPrimaryVariableSecondary',
            'VariablePrimaryNoSecondary',
        ]
        | None
    ) = Field(
        default='ConstantPrimaryNoSecondary',
        json_schema_extra={
            'note': 'VariablePrimaryNoSecondary - variable flow to chillers and coils ConstantPrimaryNoSecondary - constant flow to chillers and coils, excess bypassed ConstantPrimaryVariableSecondary - constant flow t...'
        },
    )
    primary_chilled_water_pump_rated_head: float | None = Field(
        default=179352.0,
        ge=0.0,
        json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet H2O'},
    )
    secondary_chilled_water_pump_rated_head: float | None = Field(
        default=179352.0,
        ge=0.0,
        json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet H2O'},
    )
    condenser_plant_operation_scheme_type: (
        Literal['', 'Default', 'UserDefined'] | None
    ) = Field(
        default='Default',
        json_schema_extra={
            'note': 'Default operation type makes all equipment available at all times operating in order of Priority specified in HVACTemplate:Plant:Tower objects. May be left blank if not serving any water cooled chi...'
        },
    )
    condenser_equipment_operation_schemes_name: CondenserOperationSchemesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['CondenserOperationSchemes'],
                'note': 'Name of a CondenserEquipmentOperationSchemes object Ignored if Condenser Plant Operation Scheme Type = Default May be left blank if not serving any water cooled chillers',
            },
        )
    )
    condenser_water_temperature_control_type: (
        Literal['OutdoorWetBulbTemperature', 'SpecifiedSetpoint'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'May be left blank if not serving any water cooled chillers'
        },
    )
    condenser_water_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint May be left blank if not serving any water cooled chillers',
        },
    )
    condenser_water_design_setpoint: float | None = Field(
        default=29.4,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Condenser Water Setpoint Schedule Name is specified. May be left blank if not serving any water cooled chillers',
        },
    )
    condenser_water_pump_rated_head: float | None = Field(
        default=179352.0,
        ge=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'May be left blank if not serving any water cooled chillers default head is 60 feet H2O',
        },
    )
    chilled_water_setpoint_reset_type: (
        Literal['', 'None', 'OutdoorAirTemperatureReset'] | None
    ) = Field(
        default='None',
        json_schema_extra={'note': 'Overrides Chilled Water Setpoint Schedule Name'},
    )
    chilled_water_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    chilled_water_reset_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    chilled_water_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=6.7,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    chilled_water_reset_outdoor_dry_bulb_high: float | None = Field(
        default=26.7,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    chilled_water_primary_pump_type: (
        Literal[
            '',
            'FiveHeaderedPumps',
            'FourHeaderedPumps',
            'PumpPerChiller',
            'SinglePump',
            'ThreeHeaderedPumps',
            'TwoHeaderedPumps',
        ]
        | None
    ) = Field(
        default='SinglePump',
        json_schema_extra={
            'note': 'Describes the type of pump configuration used for the primary portion of the chilled water loop.'
        },
    )
    chilled_water_secondary_pump_type: (
        Literal[
            '',
            'FiveHeaderedPumps',
            'FourHeaderedPumps',
            'SinglePump',
            'ThreeHeaderedPumps',
            'TwoHeaderedPumps',
        ]
        | None
    ) = Field(
        default='SinglePump',
        json_schema_extra={
            'note': 'Describes the type of pump configuration used for the secondary portion of the chilled water loop.'
        },
    )
    condenser_water_pump_type: (
        Literal[
            '',
            'FiveHeaderedPumps',
            'FourHeaderedPumps',
            'PumpPerTower',
            'SinglePump',
            'ThreeHeaderedPumps',
            'TwoHeaderedPumps',
        ]
        | None
    ) = Field(
        default='SinglePump',
        json_schema_extra={
            'note': 'Describes the type of pump configuration used for the condenser water loop.'
        },
    )
    chilled_water_supply_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a supply side bypass pipe is present in the chilled water loop.'
        },
    )
    chilled_water_demand_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a demand side bypass pipe is present in the chilled water loop.'
        },
    )
    condenser_water_supply_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a supply side bypass pipe is present in the condenser water loop.'
        },
    )
    condenser_water_demand_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a demand side bypass pipe is present in the condenser water loop.'
        },
    )
    fluid_type: (
        Literal[
            '',
            'EthyleneGlycol30',
            'EthyleneGlycol40',
            'EthyleneGlycol50',
            'EthyleneGlycol60',
            'PropyleneGlycol30',
            'PropyleneGlycol40',
            'PropyleneGlycol50',
            'PropyleneGlycol60',
            'Water',
        ]
        | None
    ) = Field(default='Water')
    loop_design_delta_temperature: float | None = Field(
        default=6.67,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The temperature difference used in sizing the loop flow rate.',
        },
    )
    minimum_outdoor_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'The minimum outdoor dry-bulb temperature that the chilled water loops operate. Leave blank for no limit.',
        },
    )
    chilled_water_load_distribution_scheme: (
        Literal[
            '',
            'Optimal',
            'SequentialLoad',
            'SequentialUniformPLR',
            'UniformLoad',
            'UniformPLR',
        ]
        | None
    ) = Field(default='SequentialLoad')
    condenser_water_load_distribution_scheme: (
        Literal[
            '',
            'Optimal',
            'SequentialLoad',
            'SequentialUniformPLR',
            'UniformLoad',
            'UniformPLR',
        ]
        | None
    ) = Field(default='SequentialLoad')


class HVACTemplatePlantChiller(IDFBaseModel):
    """This object adds a chiller to an HVACTemplate:Plant:ChilledWaterLoop."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Chiller'
    name: str = Field(...)
    chiller_type: Literal[
        'DistrictChilledWater',
        'ElectricCentrifugalChiller',
        'ElectricReciprocatingChiller',
        'ElectricScrewChiller',
    ] = Field(...)
    capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    nominal_cop: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Not applicable if Chiller Type is DistrictChilledWater Electric Reciprocating Chiller',
        },
    )
    condenser_type: (
        Literal['', 'AirCooled', 'EvaporativelyCooled', 'WaterCooled'] | None
    ) = Field(
        default='WaterCooled',
        json_schema_extra={
            'note': 'Not applicable if Chiller Type is DistrictChilledWater'
        },
    )
    priority: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If Chiller Plant Operation Scheme Type=Default in HVACTemplate:Plant:ChilledWaterLoop, then equipment operates in Priority order, 1, 2, 3, etc.'
        },
    )
    sizing_factor: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'},
    )
    minimum_part_load_ratio: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'note': 'Part load ratio below which the chiller starts cycling on/off to meet the load. Must be less than or equal to Maximum Part Load Ratio.'
        },
    )
    maximum_part_load_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Maximum allowable part load ratio. Must be greater than or equal to Minimum Part Load Ratio.'
        },
    )
    optimum_part_load_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Optimum part load ratio where the chiller is most efficient. Must be greater than or equal to the Minimum Part Load Ratio and less than or equal to the Maximum Part Load Ratio.'
        },
    )
    minimum_unloading_ratio: float | None = Field(
        default=0.25,
        ge=0.0,
        json_schema_extra={
            'note': 'Part load ratio where the chiller can no longer unload and false loading begins. Minimum unloading ratio must be greater than or equal to the Minimum Part Load Ratio and less than or equal to the M...'
        },
    )
    leaving_chilled_water_lower_temperature_limit: float | None = Field(
        default=5.0, json_schema_extra={'units': 'C'}
    )


class HVACTemplatePlantChillerObjectReference(IDFBaseModel):
    """This object references a detailed chiller object and adds it to an
    HVACTemplate:Plant:ChilledWaterLoop. The user must create a complete
    detailed chiller object with all required curve or performance objects."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Chiller:ObjectReference'
    name: str = Field(..., json_schema_extra={'note': 'The name of this object.'})
    chiller_object_type: (
        Literal['', 'Chiller:Electric:EIR', 'Chiller:Electric:ReformulatedEIR'] | None
    ) = Field(default='Chiller:Electric:EIR')
    chiller_name: ChillersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['Chillers'],
            'note': 'The name of the detailed chiller object.',
        },
    )
    priority: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If Chiller Plant Operation Scheme Type=Default in HVACTemplate:Plant:ChilledWaterLoop, then equipment operates in Priority order, 1, 2, 3, etc.'
        },
    )


class HVACTemplatePlantHotWaterLoop(IDFBaseModel):
    """Plant loop to serve all HVACTemplate hot water coils and boilers."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:HotWaterLoop'
    name: str = Field(...)
    pump_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(
        default='Intermittent'
    )
    hot_water_plant_operation_scheme_type: (
        Literal['', 'Default', 'UserDefined'] | None
    ) = Field(
        default='Default',
        json_schema_extra={
            'note': 'Default operation type makes all equipment available at all times operating in order of Priority specified in HVACTemplate:Plant:Boiler objects.'
        },
    )
    hot_water_plant_equipment_operation_schemes_name: (
        PlantOperationSchemesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PlantOperationSchemes'],
            'note': 'Name of a PlantEquipmentOperationSchemes object Ignored if Plant Operation Scheme Type = Default',
        },
    )
    hot_water_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    hot_water_design_setpoint: float | None = Field(
        default=82.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Setpoint Schedule Name is specified.',
        },
    )
    hot_water_pump_configuration: Literal['', 'ConstantFlow', 'VariableFlow'] | None = (
        Field(
            default='ConstantFlow',
            json_schema_extra={
                'note': 'VariableFlow - variable flow to boilers and coils, excess bypassed ConstantFlow - constant flow to boilers and coils, excess bypassed'
            },
        )
    )
    hot_water_pump_rated_head: float | None = Field(
        default=179352.0,
        ge=0.0,
        json_schema_extra={'units': 'Pa', 'note': 'Default head is 60 feet H2O'},
    )
    hot_water_setpoint_reset_type: (
        Literal['', 'None', 'OutdoorAirTemperatureReset'] | None
    ) = Field(
        default='None',
        json_schema_extra={'note': 'Overrides Hot Water Setpoint Schedule Name'},
    )
    hot_water_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=82.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    hot_water_reset_outdoor_dry_bulb_low: float | None = Field(
        default=-6.7,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    hot_water_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=65.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    hot_water_reset_outdoor_dry_bulb_high: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    hot_water_pump_type: (
        Literal[
            '',
            'FiveHeaderedPumps',
            'FourHeaderedPumps',
            'PumpPerBoiler',
            'SinglePump',
            'ThreeHeaderedPumps',
            'TwoHeaderedPumps',
        ]
        | None
    ) = Field(
        default='SinglePump',
        json_schema_extra={
            'note': 'Describes the type of pump configuration used for the hot water loop.'
        },
    )
    supply_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a supply side bypass pipe is present in the hot water loop.'
        },
    )
    demand_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a demand side bypass pipe is present in the hot water loop.'
        },
    )
    fluid_type: (
        Literal[
            '',
            'EthyleneGlycol30',
            'EthyleneGlycol40',
            'EthyleneGlycol50',
            'EthyleneGlycol60',
            'PropyleneGlycol30',
            'PropyleneGlycol40',
            'PropyleneGlycol50',
            'PropyleneGlycol60',
            'Water',
        ]
        | None
    ) = Field(default='Water')
    loop_design_delta_temperature: float | None = Field(
        default=11.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The temperature difference used in sizing the loop flow rate.',
        },
    )
    maximum_outdoor_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'The maximum outdoor dry-bulb temperature that the hot water loops operate. Leave blank for no limit.',
        },
    )
    load_distribution_scheme: (
        Literal[
            '',
            'Optimal',
            'SequentialLoad',
            'SequentialUniformPLR',
            'UniformLoad',
            'UniformPLR',
        ]
        | None
    ) = Field(default='SequentialLoad')


class HVACTemplatePlantMixedWaterLoop(IDFBaseModel):
    """Central plant loop portion of a water source heat pump system."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:MixedWaterLoop'
    name: str = Field(...)
    pump_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available Applies to both chilled water and condenser loop pumps',
        },
    )
    pump_control_type: Literal['', 'Continuous', 'Intermittent'] | None = Field(
        default='Intermittent',
        json_schema_extra={
            'note': 'Applies to both chilled water and condenser loop pumps'
        },
    )
    operation_scheme_type: Literal['', 'Default', 'UserDefined'] | None = Field(
        default='Default',
        json_schema_extra={
            'note': 'Default operation type makes all equipment available at all times operating in order of Priority specified in HVACTemplate:Plant:Boiler and HVACTemplate:Plant:Tower objects.'
        },
    )
    equipment_operation_schemes_name: PlantOperationSchemesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['PlantOperationSchemes'],
            'note': 'Name of a PlantEquipmentOperationSchemes object Ignored if Plant Operation Scheme Type = Default',
        },
    )
    high_temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    high_temperature_design_setpoint: float | None = Field(
        default=33.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Setpoint Schedule Name is specified.',
        },
    )
    low_temperature_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint May be left blank if not serving any water cooled chillers',
        },
    )
    low_temperature_design_setpoint: float | None = Field(
        default=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Condenser Water Setpoint Schedule Name is specified. May be left blank if not serving any water cooled chillers',
        },
    )
    water_pump_configuration: Literal['', 'ConstantFlow', 'VariableFlow'] | None = (
        Field(
            default='ConstantFlow',
            json_schema_extra={
                'note': 'VariableFlow - variable flow to boilers and coils, excess bypassed ConstantFlow - constant flow to boilers and coils, excess bypassed'
            },
        )
    )
    water_pump_rated_head: float | None = Field(
        default=179352.0,
        ge=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'May be left blank if not serving any water cooled chillers default head is 60 feet H2O',
        },
    )
    water_pump_type: (
        Literal[
            '',
            'FiveHeaderedPumps',
            'FourHeaderedPumps',
            'PumpPerTowerOrBoiler',
            'SinglePump',
            'ThreeHeaderedPumps',
            'TwoHeaderedPumps',
        ]
        | None
    ) = Field(
        default='SinglePump',
        json_schema_extra={
            'note': 'Describes the type of pump configuration used for the mixed water loop.'
        },
    )
    supply_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a supply side bypass pipe is present in the hot water loop.'
        },
    )
    demand_side_bypass_pipe: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Determines if a demand side bypass pipe is present in the hot water loop.'
        },
    )
    fluid_type: (
        Literal[
            '',
            'EthyleneGlycol30',
            'EthyleneGlycol40',
            'EthyleneGlycol50',
            'EthyleneGlycol60',
            'PropyleneGlycol30',
            'PropyleneGlycol40',
            'PropyleneGlycol50',
            'PropyleneGlycol60',
            'Water',
        ]
        | None
    ) = Field(default='Water')
    loop_design_delta_temperature: float | None = Field(
        default=5.6,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The temperature difference used in sizing the loop flow rate.',
        },
    )
    load_distribution_scheme: (
        Literal[
            '',
            'Optimal',
            'SequentialLoad',
            'SequentialUniformPLR',
            'UniformLoad',
            'UniformPLR',
        ]
        | None
    ) = Field(default='SequentialLoad')


class HVACTemplatePlantTower(IDFBaseModel):
    """This object adds a cooling tower to an HVACTemplate:Plant:ChilledWaterLoop
    or MixedWaterLoop."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Tower'
    name: str = Field(...)
    tower_type: Literal['SingleSpeed', 'TwoSpeed'] = Field(...)
    high_speed_nominal_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Applicable for tower type SingleSpeed and TwoSpeed Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C ...',
        },
    )
    high_speed_fan_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Applicable for tower type SingleSpeed and TwoSpeed',
        },
    )
    low_speed_nominal_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Applicable only for Tower Type TwoSpeed Nominal tower capacity with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb temperature and 35C (95F) dry-b...',
        },
    )
    low_speed_fan_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Applicable only for Tower Type TwoSpeed',
        },
    )
    free_convection_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Applicable for Tower Type SingleSpeed and TwoSpeed Tower capacity in free convection regime with entering water at 35C (95F), leaving water at 29.44C (85F), entering air at 25.56C (78F) wet-bulb te...',
        },
    )
    priority: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Applicable for all Tower Types If Condenser Plant Operation Scheme Type=Default in HVACTemplate:Plant:ChilledWaterLoop, then equipment operates in Priority order, 1, 2, 3, etc.'
        },
    )
    sizing_factor: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={'note': 'Multiplies the autosized capacity and flow rates'},
    )
    template_plant_loop_type: Literal['ChilledWater', 'MixedWater'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specifies if this tower serves a template chilled water loop or mixed water loop If left blank, will serve a chilled water loop if present, or a mixed water loop (if no chilled water loop is present).'
        },
    )


class HVACTemplatePlantTowerObjectReference(IDFBaseModel):
    """This object references a detailed cooling tower object and adds it to an
    HVACTemplate:Plant:ChilledWaterLoop or MixedWaterLoop. The user must create
    a complete detailed cooling tower object with all required curve or
    performance objects."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Plant:Tower:ObjectReference'
    name: str = Field(..., json_schema_extra={'note': 'The name of this object.'})
    cooling_tower_object_type: (
        Literal[
            '',
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed',
        ]
        | None
    ) = Field(default='CoolingTower:SingleSpeed')
    cooling_tower_name: CoolingTowersRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CoolingTowers'],
            'note': 'The name of the detailed cooling tower object.',
        },
    )
    priority: float | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If Condenser Plant Operation Scheme Type=Default in HVACTemplate:Plant:ChilledWaterLoop or MixedWaterLoop, then equipment operates in Priority order, 1, 2, 3, etc.'
        },
    )
    template_plant_loop_type: Literal['ChilledWater', 'MixedWater'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specifies if this tower serves a template chilled water loop or mixed water loop If left blank, will serve a chilled water loop if present, or a mixed water loop (if no chilled water loop is present).'
        },
    )


class HVACTemplateSystemConstantVolume(IDFBaseModel):
    """Constant Air Volume air loop with optional chilled water cooling coil,
    optional heating coil and optional preheat."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:ConstantVolume'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on;  Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
        },
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=600.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    cooling_coil_type: (
        Literal[
            '',
            'ChilledWater',
            'ChilledWaterDetailedFlatModel',
            'HeatExchangerAssistedChilledWater',
            'None',
        ]
        | None
    ) = Field(default='ChilledWater')
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_setpoint_control_type: (
        Literal[
            '',
            'ControlZone',
            'FixedSetpoint',
            'OutdoorAirTemperatureReset',
            'Scheduled',
            'Warmest',
        ]
        | None
    ) = Field(default='FixedSetpoint')
    cooling_coil_control_zone_name: HVACTemplateConstantVolumeZonesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateConstantVolumeZones'],
            'note': 'name of the HVACTemplate:ZoneConstantVolume object that contains the cooling thermostat when Cooling Coil Setpoint Control Type = ControlZone',
        },
    )
    cooling_coil_design_setpoint_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Cooling Coil Setpoint Schedule Name is specified.',
        },
    )
    cooling_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults are 15.6C (60F) at 15.6C (60F) to 12.8C (55F) at 23.3C (74F)',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=23.3,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='HotWater')
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_setpoint_control_type: (
        Literal[
            '',
            'ControlZone',
            'FixedSetpoint',
            'OutdoorAirTemperatureReset',
            'Scheduled',
        ]
        | None
    ) = Field(default='FixedSetpoint')
    heating_coil_control_zone_name: HVACTemplateConstantVolumeZonesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateConstantVolumeZones'],
            'note': 'name of the HVACTemplate:ZoneConstantVolume object that contains the heating thermostat',
        },
    )
    heating_coil_design_setpoint: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Heating Coil Setpoint Schedule Name is specified.',
        },
    )
    heating_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=7.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults are 15.6C (60F) at 15.6C (60F) to 12.8C (55F) at 23.3C (74F)',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    preheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='None')
    )
    preheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    preheat_coil_design_setpoint: float | None = Field(
        default=7.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Preheat Coil Setpoint Schedule Name specified.',
        },
    )
    preheat_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    gas_preheat_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_preheat_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the Minimum Outdoor Air Flow Rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_upper_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_lower_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature below which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_upper_enthalpy_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Outdoor enthalpy above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    night_cycle_control: (
        Literal[
            '', 'CycleOnAny', 'CycleOnAnyZoneFansOnly', 'CycleOnControlZone', 'StayOff'
        ]
        | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65, ge=0.0, le=1.0
    )
    heat_recovery_heat_exchanger_type: Literal['', 'Plate', 'Rotary'] | None = Field(
        default='Plate'
    )
    heat_recovery_frost_control_type: (
        Literal[
            '',
            'ExhaustAirRecirculation',
            'ExhaustOnly',
            'MinimumExhaustTemperature',
            'None',
        ]
        | None
    ) = Field(default='None')
    dehumidification_control_type: Literal['', 'CoolReheat', 'None'] | None = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint as required to meet the humidity setpoint.'
        },
    )
    dehumidification_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    dehumidification_relative_humidity_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100) Ignored if Dehumidification Relative Humidity Setpoint Schedule specified below',
        },
    )
    dehumidification_relative_humidity_setpoint_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank to use constant setpoint specified in Dehumidification Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_relative_humidity_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100). Ignored if Humidifier Relative Humidity Setpoint Schedule specified below',
        },
    )
    humidifier_relative_humidity_setpoint_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Leave blank to use constant setpoint specified in Humidifier Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
            },
        )
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=300.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )


class HVACTemplateSystemDedicatedOutdoorAir(IDFBaseModel):
    """This object creates a dedicated outdoor air system that must be used with
    HVACTemplate:Zone:* objects for BaseboardHeat FanCoil PTAC PTHP
    WaterToAirHeatPump and VRF. Does not support HVACTemplate:Zone:VAV or other
    central multizone systems"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:DedicatedOutdoorAir'
    name: str | None = Field(default=None)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on; DOAS System always on. Schedule is used in availability manager and fan scheduling.',
        },
    )
    air_outlet_type: Literal['', 'DirectIntoZone'] | None = Field(
        default='DirectIntoZone'
    )
    supply_fan_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    cooling_coil_type: (
        Literal[
            '',
            'ChilledWater',
            'ChilledWaterDetailedFlatModel',
            'HeatExchangerAssistedChilledWater',
            'HeatExchangerAssistedDX',
            'None',
            'TwoSpeedDX',
            'TwoStageDX',
            'TwoStageHumidityControlDX',
        ]
        | None
    ) = Field(default='ChilledWater')
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_setpoint_control_type: (
        Literal['', 'FixedSetpoint', 'OutdoorAirTemperatureReset', 'Scheduled'] | None
    ) = Field(default='FixedSetpoint')
    cooling_coil_design_setpoint: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Cooling Coil Setpoint Schedule Name is specified.',
        },
    )
    cooling_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults are 15.6C (60F) at 15.6C (60F) to 12.8C (55F) at 23.3C (74F)',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=23.3,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    dx_cooling_coil_gross_rated_total_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    dx_cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'note': 'Gross SHR'})
    dx_cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='HotWater')
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_setpoint_control_type: (
        Literal['', 'FixedSetpoint', 'OutdoorAirTemperatureReset', 'Scheduled'] | None
    ) = Field(
        default='FixedSetpoint',
        json_schema_extra={
            'note': 'When selecting OutdoorAirTemperatureReset, the Heating Coil Design Setpoint may need to be changed'
        },
    )
    heating_coil_design_setpoint: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Heating Coil Setpoint Schedule Name is specified.',
        },
    )
    heating_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults 15.0C (59F) at 7.8C (46F) to 12.2C (54F) at 12.2C (54F)',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=7.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    heat_recovery_sensible_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    heat_recovery_latent_effectiveness: float | None = Field(
        default=0.65, ge=0.0, le=1.0
    )
    heat_recovery_heat_exchanger_type: Literal['', 'Plate', 'Rotary'] | None = Field(
        default='Plate'
    )
    heat_recovery_frost_control_type: (
        Literal[
            '',
            'ExhaustAirRecirculation',
            'ExhaustOnly',
            'MinimumExhaustTemperature',
            'None',
        ]
        | None
    ) = Field(default='None')
    dehumidification_control_type: (
        Literal[
            '', 'CoolReheatDesuperheater', 'CoolReheatHeatingCoil', 'Multimode', 'None'
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheatHeatingCoil = cool beyond the dry-bulb setpoint, reheat with heating coil Valid for all cooling coil types. If no heating coil specified, cold supply temps ...'
        },
    )
    dehumidification_setpoint: float | None = Field(
        default=0.00924,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'The supply air humidity ratio for dehumidification control. Default of 0.00924 kgWater/kgDryAir is equivalent to 12.8C (55F) dewpoint. Ignored if Dehumidification Setpoint Schedule specified below',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_constant_setpoint: float | None = Field(
        default=0.003,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'The supply air humidity ratio for humidification control. Ignored if Humidifier Setpoint Schedule specified below',
        },
    )
    dehumidification_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank to use constant setpoint specified in Dehumidification Setpoint above. Schedule values must be in units of humidity ratio (kgWater/kgDryAir or lbWater/lbDryAir)',
        },
    )
    humidifier_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank to use constant setpoint specified in Humidifier Constant Setpoint above. Schedule values must be in units of humidity ratio (kgWater/kgDryAir or lbWater/lbDryAir)',
        },
    )


class HVACTemplateSystemDualDuct(IDFBaseModel):
    """Dual-duct constant volume or variable volume air loop"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:DualDuct'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on;  Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    system_configuration_type: (
        Literal[
            '',
            'DualFanConstantVolume',
            'DualFanVariableVolume',
            'SingleFanConstantVolume',
            'SingleFanVariableVolume',
        ]
        | None
    ) = Field(
        default='SingleFanConstantVolume',
        json_schema_extra={
            'note': 'SingleFan - a single supply fan before the split to dual ducts DualFan - two supply fans, one each for the cold and hot ducts ConstantVolume - constant volume VariableVolume - variable volume'
        },
    )
    main_supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
        },
    )
    main_supply_fan_minimum_flow_fraction: float | None = Field(
        default=0.2, ge=0.0, le=1.0
    )
    main_supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    main_supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    main_supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    main_supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    main_supply_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )
    cold_duct_supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'm3/s',
                'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
            },
        )
    )
    cold_duct_supply_fan_minimum_flow_fraction: float | None = Field(
        default=0.2, ge=0.0, le=1.0
    )
    cold_duct_supply_fan_total_efficiency: float | None = Field(
        default=0.7, le=1.0, gt=0.0
    )
    cold_duct_supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    cold_duct_supply_fan_motor_efficiency: float | None = Field(
        default=0.9, le=1.0, gt=0.0
    )
    cold_duct_supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cold_duct_supply_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )
    cold_duct_supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = (
        Field(default='DrawThrough')
    )
    hot_duct_supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'm3/s',
                'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
            },
        )
    )
    hot_duct_supply_fan_minimum_flow_fraction: float | None = Field(
        default=0.2, ge=0.0, le=1.0
    )
    hot_duct_supply_fan_total_efficiency: float | None = Field(
        default=0.7, le=1.0, gt=0.0
    )
    hot_duct_supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    hot_duct_supply_fan_motor_efficiency: float | None = Field(
        default=0.9, le=1.0, gt=0.0
    )
    hot_duct_supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    hot_duct_supply_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )
    hot_duct_supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = (
        Field(default='DrawThrough')
    )
    cooling_coil_type: (
        Literal['', 'ChilledWater', 'ChilledWaterDetailedFlatModel', 'None'] | None
    ) = Field(default='ChilledWater')
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_setpoint_control_type: (
        Literal[
            '', 'FixedSetpoint', 'OutdoorAirTemperatureReset', 'Scheduled', 'Warmest'
        ]
        | None
    ) = Field(default='FixedSetpoint')
    cooling_coil_design_setpoint_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Cooling Coil Setpoint Schedule Name is specified.',
        },
    )
    cooling_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=15.6,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults are 15.6C (60F) at 15.6C (60F) to 12.8C (55F) at 23.3C (74F)',
        },
    )
    cooling_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    cooling_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=23.3,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='HotWater')
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_setpoint_control_type: (
        Literal[
            '', 'Coldest', 'FixedSetpoint', 'OutdoorAirTemperatureReset', 'Scheduled'
        ]
        | None
    ) = Field(default='FixedSetpoint')
    heating_coil_design_setpoint: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Heating Coil Setpoint Schedule Name is specified.',
        },
    )
    heating_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_low: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_low: float | None = Field(
        default=7.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control. Defaults are 15.6C (60F) at 15.6C (60F) to 12.8C (55F) at 23.3C (74F)',
        },
    )
    heating_coil_setpoint_at_outdoor_dry_bulb_high: float | None = Field(
        default=20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_reset_outdoor_dry_bulb_high: float | None = Field(
        default=12.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Applicable only for OutdoorAirTemperatureReset control.',
        },
    )
    heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    preheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='None')
    )
    preheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    preheat_coil_design_setpoint: float | None = Field(
        default=7.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Preheat Coil Setpoint Schedule Name specified.',
        },
    )
    preheat_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    gas_preheat_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_preheat_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_control_type: (
        Literal['', 'FixedMinimum', 'ProportionalMinimum'] | None
    ) = Field(default='ProportionalMinimum')
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the Minimum Outdoor Air Flow Rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: Literal['', 'NoLockout'] | None = Field(default='NoLockout')
    economizer_upper_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_lower_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature below which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_upper_enthalpy_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Outdoor enthalpy above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    cold_supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves the cold inlets of all zones on this system. Blank if none.',
        },
    )
    hot_supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves the hot inlets of all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    night_cycle_control: (
        Literal['', 'CycleOnAny', 'CycleOnControlZone', 'StayOff'] | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65, ge=0.0, le=1.0
    )
    heat_recovery_heat_exchanger_type: Literal['', 'Plate', 'Rotary'] | None = Field(
        default='Plate'
    )
    heat_recovery_frost_control_type: (
        Literal[
            '',
            'ExhaustAirRecirculation',
            'ExhaustOnly',
            'MinimumExhaustTemperature',
            'None',
        ]
        | None
    ) = Field(default='None')
    dehumidification_control_type: Literal['', 'CoolReheat', 'None'] | None = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint as required to meet the humidity setpoint.'
        },
    )
    dehumidification_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    dehumidification_relative_humidity_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100) Ignored if Dehumidification Relative Humidity Setpoint Schedule specified below',
        },
    )
    dehumidification_relative_humidity_setpoint_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank to use constant setpoint specified in Dehumidification Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_relative_humidity_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100). Ignored if Humidifier Relative Humidity Setpoint Schedule specified below',
        },
    )
    humidifier_relative_humidity_setpoint_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Leave blank to use constant setpoint specified in Humidifier Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
            },
        )
    )
    sizing_option: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident',
        json_schema_extra={
            'note': 'Select whether autosized system supply flow rate is the sum of Coincident or NonCoincident zone air flow rates.'
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=500.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    return_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )


class HVACTemplateSystemPackagedVAV(IDFBaseModel):
    """Packaged Variable Air Volume (PVAV) air loop with optional heating coil and
    optional preheat."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:PackagedVAV'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on; PVAV System always on. Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
        },
    )
    supply_fan_minimum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is only used to set a minimum part load on the VAV fan power curve. Autosize or zero is recommended.',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: Literal['', 'TwoSpeedDX', 'TwoSpeedHumidControlDX'] | None = (
        Field(default='TwoSpeedDX')
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    cooling_coil_design_setpoint: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Cooling Coil Setpoint Schedule Name is specified.',
        },
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'note': 'Gross SHR'})
    cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electric power input',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='None')
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    heating_coil_design_setpoint: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Heating Coil Setpoint Schedule Name is specified.',
        },
    )
    heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_control_type: (
        Literal['', 'FixedMinimum', 'ProportionalMinimum'] | None
    ) = Field(default='ProportionalMinimum')
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the Minimum Outdoor Air Flow Rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: (
        Literal['', 'LockoutWithCompressor', 'LockoutWithHeating', 'NoLockout'] | None
    ) = Field(default='NoLockout')
    economizer_maximum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of economizer c...',
        },
    )
    economizer_maximum_limit_enthalpy: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    economizer_minimum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor dry-bulb temperature limit for economizer control. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    supply_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )
    night_cycle_control: (
        Literal[
            '', 'CycleOnAny', 'CycleOnAnyZoneFansOnly', 'CycleOnControlZone', 'StayOff'
        ]
        | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65, ge=0.0, le=1.0
    )
    cooling_coil_setpoint_reset_type: (
        Literal[
            '',
            'None',
            'OutdoorAirTemperatureReset',
            'Warmest',
            'WarmestTemperatureFirst',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Overrides Cooling Coil Setpoint Schedule Name None = no reset, control to Cooling Coil Design Setpoint Temperature or Schedule Warmest = reset as warm as possible yet meet all zone cooling loads at...'
        },
    )
    heating_coil_setpoint_reset_type: (
        Literal['', 'None', 'OutdoorAirTemperatureReset'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Overrides Heating Coil Setpoint Schedule Name None = no reset, control to Heating Coil Design Setpoint Temperature or Schedule OutdoorAirTemperatureReset = reset based on outdoor air temperature (H...'
        },
    )
    dehumidification_control_type: Literal['', 'CoolReheat', 'None'] | None = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint as required to meet the humidity setpoint.'
        },
    )
    dehumidification_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    dehumidification_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    sizing_option: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident',
        json_schema_extra={
            'note': 'Select whether autosized system supply flow rate is the sum of Coincident or NonCoincident zone air flow rates.'
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=500.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    return_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )


class HVACTemplateSystemUnitary(IDFBaseModel):
    """Unitary furnace with air conditioner"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:Unitary'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on; Unitary System always on. Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    control_zone_or_thermostat_location_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=600.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: Literal['', 'None', 'SingleSpeedDX'] | None = Field(
        default='SingleSpeedDX'
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_design_supply_air_temperature: float | None = Field(
        default=12.8, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'note': 'Gross SHR'})
    cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electric power',
        },
    )
    heating_coil_type: Literal['Electric', 'Gas', 'HotWater'] = Field(...)
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_design_supply_air_temperature: float | None = Field(
        default=50.0, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the minimum outdoor air flow rate If blank, always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: (
        Literal['', 'LockoutWithCompressor', 'LockoutWithHeating', 'NoLockout'] | None
    ) = Field(default='NoLockout')
    economizer_upper_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_lower_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature below which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_upper_enthalpy_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Outdoor enthalpy above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum serves all zones on this system. Blank if none.',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    night_cycle_control: (
        Literal['', 'CycleOnAny', 'CycleOnControlZone', 'StayOff'] | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applicable only if Heat Recovery Type is Enthalpy.'
        },
    )
    dehumidification_control_type: (
        Literal['', 'CoolReheatDesuperheater', 'CoolReheatHeatingCoil', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible cooling load only CoolReheatHeatingCoil = cool beyond the dry-bulb setpoint as required to meet the humidity setpoint, reheat with main heating coil. CoolReheatDesuperheater = ...'
        },
    )
    dehumidification_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=500.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )


class HVACTemplateSystemUnitaryHeatPumpAirToAir(IDFBaseModel):
    """Unitary furnace with electric air-to-air heat pump"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:UnitaryHeatPump:AirToAir'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on; Unitary System always on. Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    control_zone_or_thermostat_location_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during cooling operation This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone mult...',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during heating operation This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone mult...',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate when no cooling or heating is needed Only used when heat pump fan operating mode is Continuous. This air flow rate is used when no heating or cooling is required and the DX coi...',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=600.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: Literal['', 'SingleSpeedDX'] | None = Field(
        default='SingleSpeedDX'
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_design_supply_air_temperature: float | None = Field(
        default=12.8, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering the outdoor condenser co...',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electric power input',
        },
    )
    heat_pump_heating_coil_type: Literal['', 'SingleSpeedDXHeatPump'] | None = Field(
        default='SingleSpeedDXHeatPump'
    )
    heat_pump_heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_design_supply_air_temperature: float | None = Field(
        default=50.0, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    heat_pump_heating_coil_gross_rated_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Rated heating capacity excluding the effect of supply air fan heat Rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C Rating point heating coil entering air dry-bulb 21.11 C, c...',
        },
    )
    heat_pump_heating_coil_rated_cop: float | None = Field(
        default=2.75,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heat Pump Heating Coil Rated Capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy. Rating point outdoor dry-bu...',
        },
    )
    heat_pump_heating_minimum_outdoor_dry_bulb_temperature: float | None = Field(
        default=-8.0, ge=-20.0, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_maximum_outdoor_dry_bulb_temperature: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    heat_pump_defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed'
    )
    heat_pump_defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if Timed defrost control is specified'
        },
    )
    supplemental_heating_coil_type: (
        Literal['', 'Electric', 'Gas', 'HotWater'] | None
    ) = Field(default='Electric')
    supplemental_heating_coil_availability_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'If blank, always on',
            },
        )
    )
    supplemental_heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    supplemental_heating_coil_maximum_outdoor_dry_bulb_temperature: float | None = (
        Field(
            default=21.0,
            le=21.0,
            json_schema_extra={
                'units': 'C',
                'note': 'Supplemental heater will not operate when outdoor temperature exceeds this value.',
            },
        )
    )
    supplemental_gas_heating_coil_efficiency: float | None = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applies only if Supplemental Heating Coil Type is Gas'
        },
    )
    supplemental_gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Applies only if Supplemental Heating Coil Type is Gas',
        },
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the minimum outdoor air flow rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: (
        Literal['', 'LockoutWithCompressor', 'LockoutWithHeating', 'NoLockout'] | None
    ) = Field(default='NoLockout')
    economizer_maximum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of economizer c...',
        },
    )
    economizer_maximum_limit_enthalpy: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    economizer_minimum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor dry-bulb temperature limit for economizer control. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum serves all zones on this system. Blank if none.',
        },
    )
    night_cycle_control: (
        Literal['', 'CycleOnAny', 'CycleOnControlZone', 'StayOff'] | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applicable only if Heat Recovery Type is Enthalpy.'
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=500.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )


class HVACTemplateSystemUnitarySystem(IDFBaseModel):
    """Unitary HVAC system with optional cooling and heating. Supports DX and
    chilled water, cooling, gas, electric, and hot water heating, air-to-air and
    water-to-air heat pumps."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:UnitarySystem'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available. Also see Supply Fan Operating Mode Schedule Name field.',
        },
    )
    control_type: Literal['', 'Load', 'SetPoint'] | None = Field(
        default='Load',
        json_schema_extra={
            'note': 'Load control requires a Controlling Zone name. SetPoint control requires set points at coil outlet nodes. The user must add appropriate SetpointManager objects to the idf file.'
        },
    )
    control_zone_or_thermostat_location_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'This field is required if Control Type is Load.',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during cooling operation This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone mult...',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during heating operation This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone mult...',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate when no cooling or heating is needed Only used when heat pump fan operating mode is Continuous. This air flow rate is used when no heating or cooling is required and the DX coi...',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=600.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: (
        Literal[
            '',
            'ChilledWater',
            'ChilledWaterDetailedFlatModel',
            'HeatExchangerAssistedChilledWater',
            'HeatExchangerAssistedDX',
            'MultiSpeedDX',
            'None',
            'SingleSpeedDX',
            'SingleSpeedDXWaterCooled',
            'TwoSpeedDX',
            'TwoStageDX',
            'TwoStageHumidityControlDX',
        ]
        | None
    ) = Field(default='SingleSpeedDX')
    number_of_speeds_for_cooling: int | None = Field(
        default=1,
        ge=0,
        le=4,
        json_schema_extra={'note': 'Used only for Cooling Coil Type = MultiSpeedDX.'},
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_design_supply_air_temperature: float | None = Field(
        default=12.8, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    dx_cooling_coil_gross_rated_total_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering the outdoor condenser co...',
        },
    )
    dx_cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    dx_cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electric power input',
        },
    )
    heating_coil_type: (
        Literal[
            '',
            'Electric',
            'Gas',
            'HotWater',
            'MultiSpeedDXHeatPumpAirSource',
            'MultiStageElectric',
            'MultiStageGas',
            'None',
            'SingleSpeedDXHeatPumpAirSource',
            'SingleSpeedDXHeatPumpWaterSource',
        ]
        | None
    ) = Field(default='Gas')
    number_of_speeds_or_stages_for_heating: int | None = Field(
        default=1,
        ge=0,
        le=4,
        json_schema_extra={
            'note': 'Used only for Heating Coil Type = MultiSpeedDXHeatPumpAirSource), MultiStageElectric, or MultiStageGas.'
        },
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_design_supply_air_temperature: float | None = Field(
        default=50.0, json_schema_extra={'units': 'C', 'note': 'Used for sizing.'}
    )
    heating_coil_gross_rated_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Rated heating capacity excluding the effect of supply air fan heat Rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C Rating point heating coil entering air dry-bulb 21.11 C, c...',
        },
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    heat_pump_heating_coil_gross_rated_cop: float | None = Field(
        default=2.75,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heating Coil Rated Capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electrical energy. Rating point outdoor dry-bulb temp 8....',
        },
    )
    heat_pump_heating_minimum_outdoor_dry_bulb_temperature: float | None = Field(
        default=-8.0, ge=-20.0, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_maximum_outdoor_dry_bulb_temperature: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    heat_pump_defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed'
    )
    heat_pump_defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if Timed defrost control is specified'
        },
    )
    supplemental_heating_or_reheat_coil_type: (
        Literal['', 'DesuperHeater', 'Electric', 'Gas', 'HotWater', 'None'] | None
    ) = Field(default='None')
    supplemental_heating_or_reheat_coil_availability_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supplemental_heating_or_reheat_coil_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'W'})
    supplemental_heating_or_reheat_coil_maximum_outdoor_dry_bulb_temperature: (
        float | None
    ) = Field(
        default=21.0,
        le=21.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Supplemental heater will not operate when outdoor temperature exceeds this value.',
        },
    )
    supplemental_gas_heating_or_reheat_coil_efficiency: float | None = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applies only if Supplemental Heating Coil Type is Gas'
        },
    )
    supplemental_gas_heating_or_reheat_coil_parasitic_electric_load: float | None = (
        Field(
            default=0.0,
            ge=0.0,
            json_schema_extra={
                'units': 'W',
                'note': 'Applies only if Supplemental Heating Coil Type is Gas',
            },
        )
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the minimum outdoor air flow rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: (
        Literal['', 'LockoutWithCompressor', 'LockoutWithHeating', 'NoLockout'] | None
    ) = Field(default='NoLockout')
    economizer_maximum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dry-bulb temperature limit for FixedDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of economizer c...',
        },
    )
    economizer_maximum_limit_enthalpy: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Enter the maximum outdoor enthalpy limit for FixedEnthalpy economizer control type. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    economizer_minimum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor dry-bulb temperature limit for economizer control. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum serves all zones on this system. Blank if none.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applicable only if Heat Recovery Type is Enthalpy.'
        },
    )
    heat_recovery_heat_exchanger_type: Literal['', 'Plate', 'Rotary'] | None = Field(
        default='Plate'
    )
    heat_recovery_frost_control_type: (
        Literal[
            '',
            'ExhaustAirRecirculation',
            'ExhaustOnly',
            'MinimumExhaustTemperature',
            'None',
        ]
        | None
    ) = Field(default='None')
    dehumidification_control_type: (
        Literal['', 'CoolReheat', 'Multimode', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint, reheat with reheat coil If no reheat coil specified, cold supply temps may occur. Multimode = activate enhanced dehumi...'
        },
    )
    dehumidification_relative_humidity_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100) Ignored if Dehumidification Relative Humidity Setpoint Schedule specified below',
        },
    )
    dehumidification_relative_humidity_setpoint_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank to use constant setpoint specified in Dehumidification Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_relative_humidity_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100). Ignored if Humidifier Relative Humidity Setpoint Schedule specified below',
        },
    )
    humidifier_relative_humidity_setpoint_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Leave blank to use constant setpoint specified in Humidifier Relative Humidity Setpoint above. Schedule values must be in percent relative humidity (0 to 100).',
            },
        )
    )
    sizing_option: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident',
        json_schema_extra={
            'note': 'Select whether autosized system supply flow rate is the sum of Coincident or NonCoincident zone air flow rates.'
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=300.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )


class HVACTemplateSystemVAV(IDFBaseModel):
    """Variable Air Volume (VAV) air loop with optional heating coil and optional
    preheat."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:VAV'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on; VAV System always on. Schedule is used in availability manager and fan scheduling. Also see "Night Cycle Control" field.',
        },
    )
    supply_fan_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers a value entered here must be large eno...',
        },
    )
    supply_fan_minimum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is only used to set a minimum part load on the VAV fan power curve. Autosize or zero is recommended.',
        },
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: (
        Literal['', 'ChilledWater', 'ChilledWaterDetailedFlatModel'] | None
    ) = Field(default='ChilledWater')
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    cooling_coil_design_setpoint: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Cooling Coil Setpoint Schedule Name is specified.',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='None')
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    heating_coil_design_setpoint: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Heating Coil Setpoint Schedule Name is specified.',
        },
    )
    gas_heating_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    preheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = (
        Field(default='None')
    )
    preheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    preheat_coil_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint',
        },
    )
    preheat_coil_design_setpoint: float | None = Field(
        default=7.2,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing and as constant setpoint if no Preheat Coil Setpoint Schedule Name specified.',
        },
    )
    gas_preheat_coil_efficiency: float | None = Field(default=0.8, ge=0.0, le=1.0)
    gas_preheat_coil_parasitic_electric_load: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    maximum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_outdoor_air_control_type: (
        Literal['', 'FixedMinimum', 'ProportionalMinimum'] | None
    ) = Field(default='ProportionalMinimum')
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the Minimum Outdoor Air Flow Rate If blank, multiplier is always one',
        },
    )
    economizer_type: (
        Literal[
            '',
            'DifferentialDryBulb',
            'DifferentialDryBulbAndEnthalpy',
            'DifferentialEnthalpy',
            'ElectronicEnthalpy',
            'FixedDewPointAndDryBulb',
            'FixedDryBulb',
            'FixedEnthalpy',
            'NoEconomizer',
        ]
        | None
    ) = Field(default='NoEconomizer')
    economizer_lockout: Literal['', 'NoLockout'] | None = Field(default='NoLockout')
    economizer_upper_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_lower_temperature_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Outdoor temperature below which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_upper_enthalpy_limit: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'J/kg',
            'note': 'Outdoor enthalpy above which economizer is disabled and heat recovery is enabled (if available). Blank means no limit.',
        },
    )
    economizer_maximum_limit_dewpoint_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor dewpoint temperature limit for FixedDewPointAndDryBulb economizer control type. No input or blank input means this limit is not operative. Limit is applied regardless of e...',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum serves all zones on this system. Blank if none.',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    supply_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )
    night_cycle_control: (
        Literal[
            '', 'CycleOnAny', 'CycleOnAnyZoneFansOnly', 'CycleOnControlZone', 'StayOff'
        ]
        | None
    ) = Field(default='StayOff')
    night_cycle_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Applicable only if Night Cycle Control is Cycle On Control Zone.',
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65, ge=0.0, le=1.0
    )
    cooling_coil_setpoint_reset_type: (
        Literal[
            '',
            'None',
            'OutdoorAirTemperatureReset',
            'Warmest',
            'WarmestTemperatureFirst',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Overrides Cooling Coil Setpoint Schedule Name None = no reset, control to Cooling Coil Design Setpoint Temperature or Schedule Warmest = reset as warm as possible yet meet all zone cooling loads at...'
        },
    )
    heating_coil_setpoint_reset_type: (
        Literal['', 'None', 'OutdoorAirTemperatureReset'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Overrides Heating Coil Setpoint Schedule Name None = no reset, control to Heating Coil Design Setpoint Temperature or Schedule OutdoorAirTemperatureReset = reset based on outdoor air temperature (H...'
        },
    )
    dehumidification_control_type: Literal['', 'CoolReheat', 'None'] | None = Field(
        default='None',
        json_schema_extra={
            'note': 'None = meet sensible load only CoolReheat = cool beyond the dry-bulb setpoint as required to meet the humidity setpoint.'
        },
    )
    dehumidification_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    dehumidification_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    humidifier_type: Literal['', 'ElectricSteam', 'None'] | None = Field(default='None')
    humidifier_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always available',
        },
    )
    humidifier_rated_capacity: float | None = Field(
        default=1e-06,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Moisture output rate at full rated power input. The humidifier does not currently autosize, so the default is very large to allow for adequate capacity.',
        },
    )
    humidifier_rated_electric_power: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Electric power input at rated capacity moisture output. Power consumption is proportional to moisture output with no part-load penalty.',
        },
    )
    humidifier_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name where humidistat is located',
        },
    )
    humidifier_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    sizing_option: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident',
        json_schema_extra={
            'note': 'Select whether autosized system supply flow rate is the sum of Coincident or NonCoincident zone air flow rates.'
        },
    )
    return_fan: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={'note': 'Specifies if the system has a return fan.'},
    )
    return_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    return_fan_delta_pressure: float | None = Field(
        default=500.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    return_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    return_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    return_fan_part_load_power_coefficients: (
        Literal[
            '',
            'ASHRAE90.1-2004AppendixG',
            'InletVaneDampers',
            'OutletDampers',
            'VariableSpeedMotor',
            'VariableSpeedMotorPressureReset',
        ]
        | None
    ) = Field(
        default='InletVaneDampers',
        json_schema_extra={
            'note': 'This field selects a predefined set of fan power coefficients. The ASHRAE 90.1-2004 Appendix G coefficients are from TABLE G3.1.3.15, Method 2. The other sets of coefficients are from the EnergyPlu...'
        },
    )


class HVACTemplateSystemVRF(IDFBaseModel):
    """Variable refrigerant flow (VRF) heat pump condensing unit. Serves one or
    more VRF zone terminal units (HVACTemplate:Zone:VRF)."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:System:VRF'
    name: str = Field(...)
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    gross_rated_total_cooling_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the total cooling capacity in watts at rated conditions or set to autosize. Total cooling capacity not accounting for the effect of supply air fan heat',
        },
    )
    gross_rated_cooling_cop: float | None = Field(
        default=3.3,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the coefficient of performance at rated conditions or leave blank to use default. COP includes compressor and condenser fan electrical energy input COP does not include supply fan heat or sup...',
        },
    )
    minimum_outdoor_temperature_in_cooling_mode: float | None = Field(
        default=-6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for cooling operation. Cooling is disabled below this temperature.',
        },
    )
    maximum_outdoor_temperature_in_cooling_mode: float | None = Field(
        default=43.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for cooling operation. Cooling is disabled above this temperature.',
        },
    )
    gross_rated_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the heating capacity in watts at rated conditions or set to autosize. Heating capacity not accounting for the effect of supply air fan heat',
        },
    )
    rated_heating_capacity_sizing_ratio: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'If the Gross Rated Heating Capacity is autosized, the heating capacity is sized to be equal to the cooling capacity multiplied by this sizing ratio. The zone terminal unit heating coils are also si...',
        },
    )
    gross_rated_heating_cop: float | None = Field(
        default=3.4,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'COP includes compressor and condenser fan electrical energy input COP does not include supply fan heat or supply fan electrical energy input',
        },
    )
    minimum_outdoor_temperature_in_heating_mode: float | None = Field(
        default=-20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for heating operation.',
        },
    )
    maximum_outdoor_temperature_in_heating_mode: float | None = Field(
        default=16.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for heating operation.',
        },
    )
    minimum_heat_pump_part_load_ratio: float | None = Field(
        default=0.15,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the minimum heat pump part-load ratio (PLR). When the cooling or heating PLR is below this value, the heat pump compressor will cycle to meet the cooling or heating demand.',
        },
    )
    zone_name_for_master_thermostat_location: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter the name of the zone where the master thermostat is located.',
        },
    )
    master_thermostat_priority_control_type: (
        Literal[
            '',
            'LoadPriority',
            'MasterThermostatPriority',
            'Scheduled',
            'ThermostatOffsetPriority',
            'ZonePriority',
        ]
        | None
    ) = Field(
        default='MasterThermostatPriority',
        json_schema_extra={
            'note': 'Choose a thermostat control logic scheme. If these control types fail to control zone temperature within a reasonable limit, consider using multiple VRF systems'
        },
    )
    thermostat_priority_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'this field is required if Master Thermostat Priority Control Type is Scheduled. Schedule values of 0 denote cooling, 1 for heating, and all other values disable the system.',
        },
    )
    heat_pump_waste_heat_recovery: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field is reserved for future use. The only valid choice is No.'
        },
    )
    equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode: (
        float | None
    ) = Field(
        default=30.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the equivalent length of the farthest terminal unit from the condenser',
        },
    )
    vertical_height_used_for_piping_correction_factor: float | None = Field(
        default=10.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the height difference between the highest and lowest terminal unit',
        },
    )
    equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode: (
        float | None
    ) = Field(
        default=30.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the equivalent length of the farthest terminal unit from the condenser',
        },
    )
    crankcase_heater_power_per_compressor: float | None = Field(
        default=33.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the value of the resistive heater located in the compressor(s). This heater is used to warm the refrigerant and oil when the compressor is off.',
        },
    )
    number_of_compressors: int | None = Field(
        default=2,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the total number of compressor. This input is used only for crankcase heater calculations.',
        },
    )
    ratio_of_compressor_size_to_total_compressor_capacity: float | None = Field(
        default=0.5,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the ratio of the first stage compressor to total compressor capacity. All other compressors are assumed to be equally sized. This inputs is used only for crankcase heater calculations.',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which the crankcase heaters are disabled.',
        },
    )
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='Resistive',
        json_schema_extra={
            'note': 'Select a defrost strategy. Reverse cycle reverses the operating mode from heating to cooling to melt frost formation on the condenser coil. The resistive strategy uses a resistive heater to melt th...'
        },
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed',
        json_schema_extra={
            'note': 'Choose a defrost control type. Either use a fixed Timed defrost period or select OnDemand to defrost only when necessary.'
        },
    )
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Fraction of time in defrost mode. Only applicable if timed defrost control is specified.',
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the size of the resistive defrost heating element. Only applicable if resistive defrost strategy is specified',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which defrost operation is disabled.',
        },
    )
    condenser_type: (
        Literal['', 'AirCooled', 'EvaporativelyCooled', 'WaterCooled'] | None
    ) = Field(
        default='AirCooled',
        json_schema_extra={
            'note': 'Select either an air cooled or evaporatively cooled condenser.'
        },
    )
    water_condenser_volume_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Only used when Condenser Type = WaterCooled.',
        },
    )
    evaporative_condenser_effectiveness: float | None = Field(
        default=0.9,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the effectiveness of the evaporatively cooled condenser. This field is only used when the Condenser Type = EvaporativelyCooled.',
        },
    )
    evaporative_condenser_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Used to calculate evaporative condenser water use. This field is only used when the Condenser Type = EvaporativelyCooled.',
        },
    )
    evaporative_condenser_pump_rated_power_consumption: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': "Rated power consumed by the evaporative condenser's water pump. This field is only used when the Condenser Type = EvaporativelyCooled.",
        },
    )
    basin_heater_capacity: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W/K',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled and for periods when the basin heater is available (field Basin Heater Operating Schedule Name). For this situation, the heater main...',
        },
    )
    basin_heater_setpoint_temperature: float | None = Field(
        default=2.0,
        ge=2.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Enter the outdoor dry-bulb temperature when the basin heater turns on.',
        },
    )
    basin_heater_operating_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is only used for Condenser Type = EvaporativelyCooled. Schedule values greater than 0 allow the basin heater to operate whenever the outdoor air dry-bulb temperature is below the basin h...',
        },
    )
    fuel_type: (
        Literal[
            '',
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
    ) = Field(default='Electricity')
    minimum_outdoor_temperature_in_heat_recovery_mode: float | None = Field(
        default=-15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The minimum outdoor temperature below which heat recovery mode will not operate.',
        },
    )
    maximum_outdoor_temperature_in_heat_recovery_mode: float | None = Field(
        default=45.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The maximum outdoor temperature above which heat recovery mode will not operate.',
        },
    )


class HVACTemplateThermostat(IDFBaseModel):
    """Zone thermostat control. Referenced schedules must be defined elsewhere in
    the idf. Thermostat control type is dual setpoint with deadband. It is not
    necessary to create a thermostat object for every zone, only for each unique
    set of setpoint schedules. For example, an office building may have two
    thermostat objects, one for \"Office\" and one for \"Storage\"."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Thermostat'
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This name is referenced by HVACTemplate:Zone:* objects'
        },
    )
    heating_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint specified below, must enter schedule or constant setpoint',
        },
    )
    constant_heating_setpoint: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Ignored if schedule specified above, must enter schedule or constant setpoint',
        },
    )
    cooling_setpoint_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Leave blank if constant setpoint specified below, must enter schedule or constant setpoint',
        },
    )
    constant_cooling_setpoint: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Ignored if schedule specified above, must enter schedule or constant setpoint',
        },
    )


class HVACTemplateZoneBaseboardHeat(IDFBaseModel):
    """Zone baseboard heating system."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:BaseboardHeat'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater'] | None = Field(
        default='HotWater'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )


class HVACTemplateZoneConstantVolume(IDFBaseModel):
    """Zone terminal unit, constant volume, reheat optional. Referenced schedules
    must be defined elsewhere in the idf."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:ConstantVolume'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_constant_volume_system_name: CompactHVACSystemConstantVolumeRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemConstantVolume'],
            'note': 'Name of a HVACTemplate:System:ConstantVolume object serving this zone',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    reheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    reheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    maximum_reheat_air_temperature: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum runs through only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum runs through only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )


class HVACTemplateZoneDualDuct(IDFBaseModel):
    """Zone terminal unit, dual-duct, constant or variable volume."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:DualDuct'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_dual_duct_system_name: CompactHVACSystemDualDuctRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemDualDuct'],
            'note': 'Name of a HVACTemplate:System:DualDuct object serving this zone',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_minimum_air_flow_fraction: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This field is the Zone Minimum Air Flow Fraction specified as a fraction of the maximum air flow rate. This field is ignored if the system serving this zone is constant volume.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name_for_sizing: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification. Note that this field is used only for specifying the design outdoor air flow rate used for sizing. The field Design Specificat...',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_outdoor_air_object_name_for_control: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...',
        },
    )
    cold_supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Cold supply plenum that serves only this zone. Blank if none.',
        },
    )
    hot_supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Hot supply plenum that serves only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum that serves only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )


class HVACTemplateZoneFanCoil(IDFBaseModel):
    """4 pipe fan coil unit with optional outdoor air."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:FanCoil'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_fan_motor_in_air_stream_fraction: float | None = Field(
        default=1.0, ge=0.0, le=1.0
    )
    cooling_coil_type: (
        Literal[
            '',
            'ChilledWater',
            'ChilledWaterDetailedFlatModel',
            'HeatExchangerAssistedChilledWater',
        ]
        | None
    ) = Field(default='ChilledWater')
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_design_setpoint: float | None = Field(
        default=14.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'HotWater'] | None = Field(
        default='HotWater'
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_design_setpoint: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Used for sizing when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Cooling Coil Design Setpoint (above) TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference'
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Heating Coil Design Setpoint (above) TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    capacity_control_method: (
        Literal[
            'ASHRAE90VariableFan',
            'ConstantFanVariableFlow',
            'CyclingFan',
            'MultiSpeedFan',
            'VariableFanConstantFlow',
            'VariableFanVariableFlow',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'If this field is left blank, it will default to CyclingFan if a Dedicated Outdoor Air System is specified (see above), otherwise it will default to ConstantFanVariableFlow.'
        },
    )
    low_speed_supply_air_flow_ratio: float | None = Field(default=0.33, gt=0.0)
    medium_speed_supply_air_flow_ratio: float | None = Field(
        default=0.66,
        gt=0.0,
        json_schema_extra={
            'note': 'Medium Speed Supply Air Flow Ratio should be greater than Low Speed Supply Air Flow Ratio'
        },
    )
    outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value of schedule multiplies maximum outdoor air flow rate This schedule is ignored if this zone is served by an HVACTemplate dedicated outdoor air system.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )


class HVACTemplateZoneIdealLoadsAirSystem(IDFBaseModel):
    """Zone with ideal air system that meets heating or cooling loads"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:IdealLoadsAirSystem'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    maximum_heating_supply_air_temperature: float | None = Field(
        default=50.0, gt=0.0, lt=100.0, json_schema_extra={'units': 'C'}
    )
    minimum_cooling_supply_air_temperature: float | None = Field(
        default=13.0, gt=-100.0, lt=50.0, json_schema_extra={'units': 'C'}
    )
    maximum_heating_supply_air_humidity_ratio: float | None = Field(
        default=0.0156, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    minimum_cooling_supply_air_humidity_ratio: float | None = Field(
        default=0.0077, gt=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    heating_limit: (
        Literal[
            '', 'LimitCapacity', 'LimitFlowRate', 'LimitFlowRateAndCapacity', 'NoLimit'
        ]
        | None
    ) = Field(default='NoLimit')
    maximum_heating_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is ignored if Heating Limit = NoLimit If this field is blank, there is no limit.',
        },
    )
    maximum_sensible_heating_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field is ignored if Heating Limit = NoLimit If this field is blank, there is no limit.',
        },
    )
    cooling_limit: (
        Literal[
            '', 'LimitCapacity', 'LimitFlowRate', 'LimitFlowRateAndCapacity', 'NoLimit'
        ]
        | None
    ) = Field(default='NoLimit')
    maximum_cooling_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is ignored if Cooling Limit = NoLimit This field is required if Outdoor Air Economizer Type is anything other than NoEconomizer.',
        },
    )
    maximum_total_cooling_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field is ignored if Cooling Limit = NoLimit',
        },
    )
    heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, heating is always available.',
        },
    )
    cooling_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, cooling is always available.',
        },
    )
    dehumidification_control_type: (
        Literal[
            '',
            'ConstantSensibleHeatRatio',
            'ConstantSupplyHumidityRatio',
            'Humidistat',
            'None',
        ]
        | None
    ) = Field(
        default='ConstantSensibleHeatRatio',
        json_schema_extra={
            'note': 'ConstantSensibleHeatRatio means that the ideal loads system will be controlled to meet the sensible cooling load, and the latent cooling rate will be computed using a constant sensible heat ratio (...'
        },
    )
    cooling_sensible_heat_ratio: float | None = Field(
        default=0.7,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This field is applicable only when Dehumidification Control Type is ConstantSensibleHeatRatio',
        },
    )
    dehumidification_setpoint: float | None = Field(
        default=60.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    humidification_control_type: (
        Literal['', 'ConstantSupplyHumidityRatio', 'Humidistat', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None means that there is no humidification. Humidistat means that there is a ZoneControl:Humidistat for this zone and the ideal loads system will attempt to satisfy the humidistat. ConstantSupplyHu...'
        },
    )
    humidification_setpoint: float | None = Field(
        default=30.0,
        ge=0.0,
        le=100.0,
        json_schema_extra={
            'units': 'percent',
            'note': 'Zone relative humidity setpoint in percent (0 to 100)',
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'None',
            'Sum',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'None means there is no outdoor air and all related fields will be ignored Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Pers...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the minimum outdoor air flow rate will be computed using these specifications. The outdoor air flow rate will also be affected b...',
        },
    )
    demand_controlled_ventilation_type: (
        Literal['', 'CO2Setpoint', 'None', 'OccupancySchedule'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'This field controls how the minimum outdoor air flow rate is calculated. None means that design occupancy will be used to compute the minimum outdoor air flow rate OccupancySchedule means that curr...'
        },
    )
    outdoor_air_economizer_type: (
        Literal['', 'DifferentialDryBulb', 'DifferentialEnthalpy', 'NoEconomizer']
        | None
    ) = Field(
        default='NoEconomizer',
        json_schema_extra={
            'note': 'DifferentialDryBulb and DifferentialEnthalpy will increase the outdoor air flow rate when there is a cooling load and the outdoor air temperature or enthalpy is below the zone exhaust air temperatu...'
        },
    )
    heat_recovery_type: Literal['', 'Enthalpy', 'None', 'Sensible'] | None = Field(
        default='None'
    )
    sensible_heat_recovery_effectiveness: float | None = Field(
        default=0.7, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    latent_heat_recovery_effectiveness: float | None = Field(
        default=0.65,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Applicable only if Heat Recovery Type is Enthalpy.',
        },
    )


class HVACTemplateZonePTAC(IDFBaseModel):
    """Packaged Terminal Air Conditioner"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:PTAC'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during cooling operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during heating operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate when no cooling or heating is needed Only used when heat pump fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coi...',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule Name values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blan...',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    cooling_coil_type: Literal['', 'SingleSpeedDX'] | None = Field(
        default='SingleSpeedDX'
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering the outdoor condenser co...',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    cooling_coil_gross_rated_cooling_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    heating_coil_type: Literal['', 'Electric', 'Gas', 'HotWater'] | None = Field(
        default='Electric'
    )
    heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    gas_heating_coil_efficiency: float | None = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        json_schema_extra={'note': 'Applies only if Heating Coil Type is Gas'},
    )
    gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Applies only if Heating Coil Type is Gas',
        },
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=14.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    capacity_control_method: Literal['', 'None', 'SingleZoneVAV'] | None = Field(
        default='None'
    )


class HVACTemplateZonePTHP(IDFBaseModel):
    """Packaged Terminal Heat Pump"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:PTHP'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during cooling operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during heating operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate when no cooling or heating is needed Only used when heat pump fan operating mode is continuous. This air flow rate is used when no heating or cooling is required and the DX coi...',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    cooling_coil_type: Literal['', 'SingleSpeedDX'] | None = Field(
        default='SingleSpeedDX'
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering the outdoor condenser co...',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    cooling_coil_gross_rated_cop: float | None = Field(
        default=3.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electrical energy input',
        },
    )
    heat_pump_heating_coil_type: Literal['', 'SingleSpeedDXHeatPump'] | None = Field(
        default='SingleSpeedDXHeatPump'
    )
    heat_pump_heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heat_pump_heating_coil_gross_rated_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Capacity excluding supply air fan heat Rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C Rating point heating coil entering air dry-bulb 21.11 C, coil entering wet-bulb 15.55 C',
        },
    )
    heat_pump_heating_coil_gross_rated_cop: float | None = Field(
        default=2.75,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heat Pump Heating Coil Rated Capacity divided by power input to the compressor and outdoor fan, Does not include supply air fan heat or supply air fan electrical energy Rating point outdoor dry-bul...',
        },
    )
    heat_pump_heating_minimum_outdoor_dry_bulb_temperature: float | None = Field(
        default=-8.0, ge=-20.0, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_maximum_outdoor_dry_bulb_temperature: float | None = Field(
        default=5.0, ge=0.0, le=7.22, json_schema_extra={'units': 'C'}
    )
    heat_pump_defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='ReverseCycle'
    )
    heat_pump_defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed'
    )
    heat_pump_defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode only applicable if Timed defrost control is specified'
        },
    )
    supplemental_heating_coil_type: (
        Literal['', 'Electric', 'Gas', 'HotWater'] | None
    ) = Field(default='Electric')
    supplemental_heating_coil_availability_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'If blank, always on',
            },
        )
    )
    supplemental_heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    supplemental_heating_coil_maximum_outdoor_dry_bulb_temperature: float | None = (
        Field(
            default=21.0,
            le=21.0,
            json_schema_extra={
                'units': 'C',
                'note': 'Supplemental heater will not operate when outdoor temperature exceeds this value.',
            },
        )
    )
    supplemental_gas_heating_coil_efficiency: float | None = Field(
        default=0.8,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Applies only if Supplemental Heating Coil Type is Gas'
        },
    )
    supplemental_gas_heating_coil_parasitic_electric_load: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Applies only if Supplemental Heating Coil Type is Gas',
        },
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=14.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    capacity_control_method: Literal['', 'None', 'SingleZoneVAV'] | None = Field(
        default='None'
    )


class HVACTemplateZoneUnitary(IDFBaseModel):
    """Zone terminal unit, constant volume, no controls."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:Unitary'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_unitary_system_name: CompactHVACSystemUnitaryRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemUnitary'],
            'note': 'Enter the name of an HVACTemplate:System:Unitary, HVACTemplate:System:UnitaryHeatPump:AirToAir, or HVACTemplate:System:UnitarySystem object serving this zone.',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum runs through only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum runs through only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )


class HVACTemplateZoneVAV(IDFBaseModel):
    """Zone terminal unit, variable volume, reheat optional. For heating, this unit
    activates reheat coil first, then increases airflow (if reverse action
    specified)."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:VAV'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_vav_system_name: CompactHVACSystemVAVRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemVAV'],
            'note': 'Name of a HVACTemplate:System:VAV or HVACTemplate:System:PackagedVAV object serving this zone',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_minimum_air_flow_input_method: (
        Literal['', 'Constant', 'FixedFlowRate', 'Scheduled'] | None
    ) = Field(
        default='Constant',
        json_schema_extra={
            'note': 'Constant = Constant Minimum Air Flow Fraction (a fraction of Maximum Air Flow Rate) FixedFlowRate = Fixed Minimum Air Flow Rate (a fixed minimum air volume flow rate) Scheduled = Scheduled Minimum ...'
        },
    )
    constant_minimum_air_flow_fraction: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Constant If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional. If a value is entered, then...'
        },
    )
    fixed_minimum_air_flow_rate: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field is used if the field Zone Minimum Air Flow Input Method is FixedFlowRate. If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional. If a value is entered...',
        },
    )
    minimum_air_flow_fraction_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Scheduled Schedule values are fractions, 0.0 to 1.0. If the field Constant Minimum Air Flow Fraction is blank, then the average...',
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    reheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    reheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    damper_heating_action: Literal['', 'Normal', 'Reverse'] | None = Field(
        default='Reverse'
    )
    maximum_flow_per_zone_floor_area_during_reheat: (
        float | Literal['Autocalculate'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse When autocalculating, the maximum flow per zone is set to 0.002032 m3/s-m2 (0.4 cfm/sqft) This option...',
        },
    )
    maximum_flow_fraction_during_reheat: float | Literal['Autocalculate'] | None = (
        Field(
            default=None,
            json_schema_extra={
                'note': 'Used only when Reheat Coil Object Type = Coil:Heating:Water and Damper Heating Action = Reverse When autocalculating, the maximum flow fraction is set to the ratio of 0.002032 m3/s-m2 (0.4 cfm/sqft...'
            },
        )
    )
    maximum_reheat_air_temperature: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.',
        },
    )
    design_specification_outdoor_air_object_name_for_control: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'When the name of a DesignSpecification:OutdoorAir object is entered, the terminal unit will increase flow as needed to meet this outdoor air requirement. If Outdoor Air Flow per Person is non-zero,...',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum runs through only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum runs through only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    design_specification_outdoor_air_object_name_for_sizing: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification. Note that this field is used only for specifying the design outdoor air flow rate used for sizing. The field Design Specificat...',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )


class HVACTemplateZoneVAVFanPowered(IDFBaseModel):
    """Zone terminal unit, fan powered variable volume, reheat optional. Referenced
    schedules must be defined elsewhere in the idf."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:VAV:FanPowered'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone Name must match a building zone name',
        },
    )
    template_vav_system_name: CompactHVACSystemVAVRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemVAV'],
            'note': 'Enter the name of a HVACTemplate:System:VAV or HVACTemplate:System:PackagedVAV object serving this zone.',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    primary_supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'm3/s',
                'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
            },
        )
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    primary_supply_air_minimum_flow_fraction: float | Literal['', 'Autosize'] | None = (
        Field(default='Autosize')
    )
    secondary_supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'm3/s',
                'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
            },
        )
    )
    flow_type: (
        Literal['', 'Parallel', 'ParallelFromPlenum', 'Series', 'SeriesFromPlenum']
        | None
    ) = Field(default='Parallel')
    parallel_fan_on_flow_fraction: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'The fraction of the primary air flow at which fan turns on Applicable only to Parallel Flow Type'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    reheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater'] | None = Field(
        default='Electric'
    )
    reheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    fan_delta_pressure: float | None = Field(
        default=1000.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum runs through only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum runs through only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    zone_piu_fan_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This is the operating schedule for the zone PIU fan. For a parallel PIU, the fan operates only when the primary air flow is below the Parallel Fan On Flow Fraction and the Zone PIU Fan Schedule is ...',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames']
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames']
        },
    )


class HVACTemplateZoneVAVHeatAndCool(IDFBaseModel):
    """VAV system with VAV for both heating and cooling and optional reheat coil.
    For heating, this unit increases airflow first, then activates reheat coil."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:VAV:HeatAndCool'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_vav_system_name: CompactHVACSystemVAVRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemVAV'],
            'note': 'Name of a HVACTemplate:System:VAV or HVACTemplate:System:PackagedVAV object serving this zone',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    supply_air_maximum_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    constant_minimum_air_flow_fraction: float | None = Field(
        default=0.2,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This field is used if the field Zone Minimum Air Flow Input Method is Constant If the field Zone Minimum Air Flow Input Method is Scheduled, then this field is optional. If a value is entered, then...'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name_for_sizing: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification. Note that this field is used only for specifying the design outdoor air flow rate used for sizing. The field Design Specificat...',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    reheat_coil_type: Literal['', 'Electric', 'Gas', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    reheat_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    maximum_reheat_air_temperature: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Specifies the maximum allowable supply air temperature leaving the reheat coil. If left blank, there is no limit and no default. If unknown, 35C (95F) is recommended.',
        },
    )
    supply_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Supply plenum runs through only this zone. Blank if none.',
        },
    )
    return_plenum_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Plenum zone name. Return plenum runs through only this zone. Blank if none.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal[
            '',
            'SupplyAirTemperature',
            'SystemSupplyAirTemperature',
            'TemperatureDifference',
        ]
        | None
    ) = Field(
        default='SystemSupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference SystemSupplyAir...'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=12.8,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature SystemSupplyAirTemperature = use the value from HVACTemplate:System:VAV Heating Coil Design Setpoint Temperature...'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )


class HVACTemplateZoneVRF(IDFBaseModel):
    """Zone terminal unit with variable refrigerant flow (VRF) DX cooling and
    heating coils (air-to-air or water-to-air heat pump). The VRF terminal units
    are served by an HVACTemplate:System:VRF system."""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:VRF'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_vrf_system_name: CompactHVACSystemVRFRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['CompactHVACSystemVRF'],
            'note': 'Name of a HVACTemplate:System:VRF object serving this zone',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    rated_total_heating_capacity_sizing_ratio: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': "If this terminal unit's heating coil is autosized, the heating capacity is sized to be equal to the cooling capacity multiplied by this sizing ratio. This input applies to the terminal unit heating...",
        },
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    no_cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This flow rate is used when the terminal is not cooling and the previous mode was cooling. This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing...',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    no_heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This flow rate is used when the terminal is not heating and the previous mode was heating. This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing...',
        },
    )
    cooling_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If this field is set to autosize it will be sized based on the outdoor air inputs below, unless a dedicated outdoor air system is specified for this zone and then it will be set to zero.',
        },
    )
    heating_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If this field is set to autosize it will be sized based on the outdoor air inputs below, unless a dedicated outdoor air system is specified for this zone and then it will be set to zero.',
        },
    )
    no_load_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If this field is set to autosize it will be sized based on the outdoor air inputs below, unless a dedicated outdoor air system is specified for this zone and then it will be set to zero.',
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_air_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='BlowThrough',
        json_schema_extra={
            'note': 'Select fan placement as either blow through or draw through.'
        },
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    cooling_coil_type: Literal['', 'None', 'VariableRefrigerantFlowDX'] | None = Field(
        default='VariableRefrigerantFlowDX'
    )
    cooling_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat Rating point: air entering the cooling coil at 26.7 C dry-bulb/19.4 C wet-bulb, and air entering the outdoor condenser co...',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    heat_pump_heating_coil_type: (
        Literal['', 'None', 'VariableRefrigerantFlowDX'] | None
    ) = Field(default='VariableRefrigerantFlowDX')
    heat_pump_heating_coil_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    heat_pump_heating_coil_gross_rated_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Capacity excluding supply air fan heat Rating point outdoor dry-bulb temp 8.33 C, outdoor wet-bulb temp 6.11 C Rating point heating coil entering air dry-bulb 21.11 C, coil entering wet-bulb 15.55 C',
        },
    )
    zone_terminal_unit_on_parasitic_electric_energy_use: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    zone_terminal_unit_off_parasitic_electric_energy_use: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=14.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )


class HVACTemplateZoneWaterToAirHeatPump(IDFBaseModel):
    """Water to Air Heat Pump to be used with HVACTemplate:Plant:MixedWaterLoop"""

    _idf_object_type: ClassVar[str] = 'HVACTemplate:Zone:WaterToAirHeatPump'
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Zone name must match a building zone name',
        },
    )
    template_thermostat_name: CompactHVACThermostatsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['CompactHVACThermostats'],
            'note': 'Enter the name of a HVACTemplate:Thermostat object. If blank, then it is assumed that standard thermostat objects have been defined for this zone.',
        },
    )
    cooling_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during cooling operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    heating_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate during heating operation This field may be set to "autosize". If a value is entered, it will be multiplied by the Supply Air Sizing Factor and by zone multipliers.',
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Supply air flow rate when no cooling or heating is needed Only used when heat pump fan operating mode is continuous. This air flow rate is used when no heating or cooling is required. If this field...',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'If blank, value from Sizing:Parameters will be used.'
        },
    )
    outdoor_air_method: (
        Literal[
            '',
            'DetailedSpecification',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'Maximum',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person, Flow/Zone, Flow/Area, Sum, and Maximum use the values in the next three fields: Outdoor Air Flow Rate per Person, Outdoor Air Flow Rate per Zone Floor Area, and Outdoor Air Flow Rate p...'
        },
    )
    outdoor_air_flow_rate_per_person: float | None = Field(
        default=0.00944,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Default 0.00944 is 20 cfm per person This input is used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone_floor_area: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_rate_per_zone: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    system_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    supply_fan_operating_mode_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Refers to a schedule to specify unitary supply fan operating mode. Schedule values of 0 indicate cycling fan (auto) Schedule values of 1 indicate continuous fan (on) If this field is left blank, a ...',
        },
    )
    supply_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = Field(
        default='DrawThrough'
    )
    supply_fan_total_efficiency: float | None = Field(default=0.7, le=1.0, gt=0.0)
    supply_fan_delta_pressure: float | None = Field(
        default=75.0, ge=0.0, json_schema_extra={'units': 'Pa'}
    )
    supply_fan_motor_efficiency: float | None = Field(default=0.9, le=1.0, gt=0.0)
    cooling_coil_type: (
        Literal['', 'Coil:Cooling:WaterToAirHeatPump:EquationFit'] | None
    ) = Field(default='Coil:Cooling:WaterToAirHeatPump:EquationFit')
    cooling_coil_gross_rated_total_capacity: float | Literal['', 'Autosize'] | None = (
        Field(
            default='Autosize',
            json_schema_extra={
                'units': 'W',
                'note': 'Total cooling capacity not accounting for the effect of supply air fan heat',
            },
        )
    )
    cooling_coil_gross_rated_sensible_heat_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'note': 'Rated sensible heat ratio (gross sensible capacity/gross total capacity) Sensible and total capacities do not include effect of supply fan heat'
        },
    )
    cooling_coil_gross_rated_cop: float | None = Field(
        default=3.5,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Gross cooling capacity divided by power input to the compressor and outdoor fan, does not include supply fan heat or supply fan electric power input',
        },
    )
    heat_pump_heating_coil_type: (
        Literal['', 'Coil:Heating:WaterToAirHeatPump:EquationFit'] | None
    ) = Field(default='Coil:Heating:WaterToAirHeatPump:EquationFit')
    heat_pump_heating_coil_gross_rated_capacity: (
        float | Literal['', 'Autosize'] | None
    ) = Field(
        default='Autosize',
        json_schema_extra={
            'units': 'W',
            'note': 'Capacity excluding supply air fan heat',
        },
    )
    heat_pump_heating_coil_gross_rated_cop: float | None = Field(
        default=4.2,
        gt=0.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Heat Pump Heating Coil Rated Capacity divided by power input to the compressor and outdoor fan, does not include supply air fan heat or supply air fan electric power input',
        },
    )
    supplemental_heating_coil_availability_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'If blank, always on',
            },
        )
    )
    supplemental_heating_coil_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
    maximum_cycling_rate: float | None = Field(
        default=2.5,
        ge=0.0,
        le=5.0,
        json_schema_extra={
            'units': 'cycles/hr',
            'note': 'The maximum on-off cycling rate for the compressor Suggested value is 2.5 for a typical heat pump',
        },
    )
    latent_capacity_time_constant: float | None = Field(
        default=60.0,
        ge=0.0,
        le=500.0,
        json_schema_extra={
            'units': 's',
            'note': "Time constant for the cooling coil's capacity to reach steady state after startup Suggested value is 60 for a typical heat pump",
        },
    )
    heat_pump_fan_delay_time: float | None = Field(
        default=60.0,
        ge=0.0,
        json_schema_extra={
            'units': 's',
            'note': 'Programmed time delay for heat pump fan to shut off after compressor cycle off. Only required when fan operating mode is cycling Enter 0 when fan operating mode is continuous',
        },
    )
    dedicated_outdoor_air_system_name: HVACTemplateDOASSystemsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HVACTemplateDOASSystems'],
            'note': 'Enter the name of an HVACTemplate:System:DedicatedOutdoorAir object if this zone is served by a separate dedicated outdoor air system (DOAS). Leave field blank if no DOAS serves this zone.',
        },
    )
    supplemental_heating_coil_type: Literal['', 'Electric', 'HotWater'] | None = Field(
        default='Electric'
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Cooling Design Supply Air Temperature TemperatureDifference = use the value from Zone Cooling Design Supply Air Temperature Difference'
        },
    )
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=14.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=11.11,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(
        default='SupplyAirTemperature',
        json_schema_extra={
            'note': 'SupplyAirTemperature = use the value from Zone Heating Design Supply Air Temperature TemperatureDifference = use the value from Zone Heating Design Supply Air Temperature Difference'
        },
    )
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=50.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    heat_pump_coil_water_flow_mode: (
        Literal['', 'Constant', 'ConstantOnDemand', 'Cycling'] | None
    ) = Field(
        default='Cycling',
        json_schema_extra={
            'note': 'used only when the heat pump coils are of the type WaterToAirHeatPump:EquationFit Constant results in 100% water flow regardless of compressor PLR Cycling results in water flow that matches compres...'
        },
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'This field is used only when Outdoor Air Method=DetailedSpecification.',
        },
    )
    baseboard_heating_type: Literal['', 'Electric', 'HotWater', 'None'] | None = Field(
        default='None'
    )
    baseboard_heating_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If blank, always on',
        },
    )
    baseboard_heating_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'W'}
    )
