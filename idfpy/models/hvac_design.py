"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 26.1.
Group: HVAC Design Objects
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401
from typing import TYPE_CHECKING

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AirPrimaryLoopsRef,
    DSOASpaceListNamesRef,
    DesignSpecificationOutdoorAirNamesRef,
    DesignSpecificationZoneAirDistributionNamesRef,
    PlantLoopsRef,
    ScheduleNamesRef,
    SpaceNamesRef,
    ZoneAndZoneListNamesRef,
)

if TYPE_CHECKING:
    from .air_distribution import AirLoopHVAC
    from .misc import CondenserLoop, PlantLoop
    from .thermal_zones import Space, Zone, ZoneList


class DesignSpecificationOutdoorAirSpaceListSpaceSpecsItem(IDFBaseModel):
    """Nested object type for array items."""

    space_name: SpaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SpaceNames']}
    )
    space_design_specification_outdoor_air_object_name: DesignSpecificationOutdoorAirNamesRef = Field(
        ..., json_schema_extra={'object_list': ['DesignSpecificationOutdoorAirNames']}
    )

    @property
    def space(self) -> Space | None:
        v = self.space_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SpaceNames'])

    @property
    def space_design_specification_outdoor_air_object(
        self,
    ) -> DesignSpecificationOutdoorAir | None:
        v = self.space_design_specification_outdoor_air_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DesignSpecificationOutdoorAirNames'])


class DesignSpecificationAirTerminalSizing(IDFBaseModel):
    """This object is used to scale the sizing of air terminal units."""

    _idf_object_type: ClassVar[str] = 'DesignSpecification:AirTerminal:Sizing'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'This name may be referenced by a ZoneHVAC:AirDistributionUnit object.'
        },
    )
    fraction_of_design_cooling_load: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The fraction of the design sensible cooling load to be met by this terminal unit. This fraction is applied after the Zone Cooling Sizing Factor (see Sizing:Zone).',
        },
    )
    cooling_design_supply_air_temperature_difference_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This ratio adjusts the supply air temperature difference used to calculate the cooling design supply air flow rate for this terminal unit.',
        },
    )
    fraction_of_design_heating_load: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The fraction of the design sensible heating load to be met by this terminal unit. This fraction is applied after the Zone Heating Sizing Factor (see Sizing:Zone).',
        },
    )
    heating_design_supply_air_temperature_difference_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This ratio adjusts the supply air temperature difference used to calculate the heating design supply air flow rate for this terminal unit.',
        },
    )
    fraction_of_minimum_outdoor_air_flow: float | None = Field(
        default=1.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The fraction of the zone minimum outdoor air requirement to be met by this terminal unit.',
        },
    )


class DesignSpecificationOutdoorAir(IDFBaseModel):
    """This object is used to describe general outdoor air requirements which are
    referenced by other objects."""

    _idf_object_type: ClassVar[str] = 'DesignSpecification:OutdoorAir'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    outdoor_air_method: (
        Literal[
            '',
            'AirChanges/Hour',
            'Flow/Area',
            'Flow/Person',
            'Flow/Zone',
            'IndoorAirQualityProcedure',
            'Maximum',
            'ProportionalControlBasedOnDesignOccupancy',
            'ProportionalControlBasedOnOccupancySchedule',
            'Sum',
        ]
        | None
    ) = Field(
        default='Flow/Person',
        json_schema_extra={
            'note': 'Flow/Person => Outdoor Air Flow per Person * Occupancy = Design Flow Rate, Flow/Area => Outdoor Air Flow per Zone Floor Area * Zone Floor Area = Design Flow Rate, Flow/Zone => Outdoor Air Flow per ...'
        },
    )
    outdoor_air_flow_per_person: float | None = Field(
        default=0.00944,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-person',
            'note': '0.00944 m3/s is equivalent to 20 cfm per person This input is only used if the field Outdoor Air Method is Flow/Person, Sum, or Maximum For sizing, the design number of occupants is used. For outdo...',
        },
    )
    outdoor_air_flow_per_zone_floor_area: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'This input is only used if the field Outdoor Air Method is Flow/Area, Sum, or Maximum',
        },
    )
    outdoor_air_flow_per_zone: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is only used if the field Outdoor Air Method is Flow/Zone, Sum, or Maximum',
        },
    )
    outdoor_air_flow_air_changes_per_hour: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': '1/hr',
            'note': 'This input is only used if the field Outdoor Air Method is AirChanges/Hour, Sum, or Maximum',
        },
    )
    outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are multiplied by the Outdoor Air Flow rate calculated using the previous four inputs. Schedule values are limited to 0 to 1. If left blank, the schedule defaults to 1.0. This sched...',
        },
    )
    proportional_control_minimum_outdoor_air_flow_rate_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'This input is only used to calculate the minimum outdoor air flow rate when the field System Outdoor Air Method = ProportionalControlBasedOnDesignOARate in Controller:MechanicalVentilation.',
        },
    )

    @property
    def outdoor_air_schedule(self) -> IDFBaseModel | None:
        v = self.outdoor_air_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def proportional_control_minimum_outdoor_air_flow_rate_schedule(
        self,
    ) -> IDFBaseModel | None:
        v = self.proportional_control_minimum_outdoor_air_flow_rate_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class DesignSpecificationOutdoorAirSpaceList(IDFBaseModel):
    """Defines a list of DesignSpecification:OutdoorAir names which can be
    referenced as a group. The DesignSpecification:OutdoorAir:SpaceList name may
    be used in Sizing:Zone and Controller:MechanicalVentilation to specify
    space-by-space OA requirements and anywhere else that accepts a
    DesignSpecification:OutdoorAir object name."""

    _idf_object_type: ClassVar[str] = 'DesignSpecification:OutdoorAir:SpaceList'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(..., json_schema_extra={'note': 'Name of the List'})
    space_specs: list[DesignSpecificationOutdoorAirSpaceListSpaceSpecsItem] | None = (
        Field(default=None)
    )


class DesignSpecificationZoneAirDistribution(IDFBaseModel):
    """This object is used to describe zone air distribution in terms of air
    distribution effectiveness and secondary recirculation fraction. It is
    referenced by Sizing:Zone and Controller:MechanicalVentilation objects"""

    _idf_object_type: ClassVar[str] = 'DesignSpecification:ZoneAirDistribution'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_air_distribution_effectiveness_in_cooling_mode: float | None = Field(
        default=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    zone_air_distribution_effectiveness_in_heating_mode: float | None = Field(
        default=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    zone_air_distribution_effectiveness_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'optionally used to replace Zone Air Distribution Effectiveness in Cooling and Heating Mode',
        },
    )
    zone_secondary_recirculation_fraction: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    minimum_zone_ventilation_efficiency: float | None = Field(
        default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )

    @property
    def zone_air_distribution_effectiveness_schedule(self) -> IDFBaseModel | None:
        v = self.zone_air_distribution_effectiveness_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class DesignSpecificationZoneHVACSizing(IDFBaseModel):
    """This object is used to describe general scalable zone HVAC equipment sizing
    which are referenced by other objects."""

    _idf_object_type: ClassVar[str] = 'DesignSpecification:ZoneHVAC:Sizing'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    cooling_supply_air_flow_rate_method: (
        Literal[
            '',
            'FlowPerCoolingCapacity',
            'FlowPerFloorArea',
            'FractionOfAutosizedCoolingAirflow',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default='SupplyAirFlowRate',
        json_schema_extra={
            'note': 'Enter the method used to determine the cooling supply air volume flow rate. None is used when a cooling coil is not included in the Zone HVAC Equip or this field may be blank. SupplyAirFlowRate => ...'
        },
    )
    cooling_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of supply air volume flow rate during cooling operation. Required field when Cooling Supply Air Flow Rate Method is SupplyAirFlowRate. This field may be blank if a cooling coil ...',
        },
    )
    cooling_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the cooling supply air volume flow rate per total conditioned floor area. Required field when Cooling Supply Air Flow Rate Method is FlowPerFloorArea. This field may be blank if a cooling coi...',
        },
    )
    cooling_fraction_of_autosized_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when Cooling Supply Air Flow Rate Method is FractionOfAutosizedCoolingAirflow. This field may...'
        },
    )
    cooling_supply_air_flow_rate_per_unit_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the cooling supply air volume flow rate unit cooling capacity. Required field when Cooling Supply Air Flow Rate Method is FlowPerCoolingCapacity. This field may be blank if a cooling coil is ...',
        },
    )
    no_load_supply_air_flow_rate_method: (
        Literal[
            '',
            'FlowPerFloorArea',
            'FractionOfAutosizedCoolingAirflow',
            'FractionOfAutosizedHeatingAirflow',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default='SupplyAirFlowRate',
        json_schema_extra={
            'note': 'Enter the method used to determine the supply air volume flow rate When No Cooling or Heating is Required. None is used when a cooling or heating coil is not included in the Zone HVAC Equipment or ...'
        },
    )
    no_load_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of the supply air volume flow rate during when no cooling or heating is required. Required field when No Load Supply Air Flow Rate Method is SupplyAirFlowRate.',
        },
    )
    no_load_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the supply air volume flow rate per total floor area. Required field when No Load Supply Air Flow Rate Method is FlowPerFloorArea.',
        },
    )
    no_load_fraction_of_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when No Load Supply Air Flow Rate Method is FractionOfAutosizedCoolingAirflow.'
        },
    )
    no_load_fraction_of_heating_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the heating supply air flow rate. Required field when No Load Supply Air Flow Rate Method is FractionOfAutosizedHeatingAirflow.'
        },
    )
    heating_supply_air_flow_rate_method: (
        Literal[
            '',
            'FlowPerFloorArea',
            'FlowPerHeatingCapacity',
            'FractionOfAutosizedHeatingAirflow',
            'None',
            'SupplyAirFlowRate',
        ]
        | None
    ) = Field(
        default='SupplyAirFlowRate',
        json_schema_extra={
            'note': 'Enter the method used to determine the heating supply air volume flow rate. None is used when a heating coil is not included in the Zone HVAC Equipment or this field may be blank. SupplyAirFlowRate...'
        },
    )
    heating_supply_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the magnitude of the supply air volume flow rate during heating operation. Required field when Heating Supply Air Flow Rate Method is SupplyAirFlowRate. This field may be blank if a heating c...',
        },
    )
    heating_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the heating supply air volume flow rate per total conditioned floor area. Required field when Heating Supply Air Flow Rate Method is FlowPerFloorArea. This field may be blank if a heating coi...',
        },
    )
    heating_fraction_of_heating_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the heating supply air flow rate. Required field when Heating Supply Air Flow Rate Method is FractionOfAutosizedHeatingAirflow. This field may...'
        },
    )
    heating_supply_air_flow_rate_per_unit_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate per unit heating capacity. Required field when Heating Supply Air Flow Rate Method is FlowPerHeatingCapacity. This field may be blank if a heating coil is not ...',
        },
    )
    cooling_design_capacity_method: (
        Literal[
            '',
            'CapacityPerFloorArea',
            'CoolingDesignCapacity',
            'FractionOfAutosizedCoolingCapacity',
            'None',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Enter the method used to determine the cooling design capacity for scalable sizing. None is used when a cooling coils is not included in the Zone HVAC Equipment or this field may be blank. If this ...'
        },
    )
    cooling_design_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the design cooling capacity. Required field when the cooling design capacity method CoolingDesignCapacity.',
        },
    )
    cooling_design_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m2',
            'note': 'Enter the cooling design capacity per zone floor area. Required field when the cooling design capacity method field is CapacityPerFloorArea.',
        },
    )
    fraction_of_autosized_cooling_design_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the fraction of auto-sized cooling design capacity. Required field when the cooling design capacity method field is FractionOfAutosizedCoolingCapacity.'
        },
    )
    heating_design_capacity_method: (
        Literal[
            '',
            'CapacityPerFloorArea',
            'FractionOfAutosizedHeatingCapacity',
            'HeatingDesignCapacity',
            'None',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Enter the method used to determine the heating design capacity for scalable sizing. None is used when a heating coil is not included in the Zone HVAC Equipment or this field may be blank. If this i...'
        },
    )
    heating_design_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.',
        },
    )
    heating_design_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m2',
            'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.',
        },
    )
    fraction_of_autosized_heating_design_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the fraction of auto-sized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'
        },
    )


class OutputControlSizingStyle(IDFBaseModel):
    """Default style for the Sizing output files is comma -- this works well for
    importing into spreadsheet programs such as Excel(tm) but not so well for
    word processing programs -- there tab may be a better choice. Fixed puts
    spaces between the \"columns\""""

    _idf_object_type: ClassVar[str] = 'OutputControl:Sizing:Style'
    column_separator: Literal['Comma', 'Fixed', 'Tab'] = Field(...)


class SizingParameters(IDFBaseModel):
    """Specifies global heating and cooling sizing factors/ratios. These ratios are
    applied at the zone level to all of the zone heating and cooling loads and
    air flow rates. Then these new loads and air flow rates are used to
    calculate the system level flow rates and capacities and are used in all
    component sizing calculations. Specifies the width (in load timesteps) of a
    moving average window which is used to smooth the peak load across more than
    one timestep."""

    _idf_object_type: ClassVar[str] = 'Sizing:Parameters'
    heating_sizing_factor: float | None = Field(default=1.0, gt=0.0)
    cooling_sizing_factor: float | None = Field(default=1.0, gt=0.0)
    timesteps_in_averaging_window: int | None = Field(
        default=None,
        ge=1,
        json_schema_extra={
            'note': 'blank => set the timesteps in averaging window to Number of Timesteps per Hour resulting in a 1 hour averaging window default is number of timesteps for 1 hour averaging window If the PerformancePr...'
        },
    )


class SizingPlant(IDFBaseModel):
    """Specifies the input needed to autosize plant loop flow rates and equipment
    capacities. This information is initially used by components that use water
    for heating or cooling such as hot or chilled water coils to calculate their
    maximum water flow rates. These flow rates are then summed for use in
    calculating the Plant Loop flow rates."""

    _idf_object_type: ClassVar[str] = 'Sizing:Plant'
    plant_or_condenser_loop_name: PlantLoopsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['PlantLoops'],
            'note': 'Enter the name of a PlantLoop or a CondenserLoop object',
        },
    )
    loop_type: Literal['Condenser', 'Cooling', 'Heating', 'Steam'] = Field(...)
    design_loop_exit_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    loop_design_temperature_difference: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'deltaC'}
    )
    sizing_option: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident',
        json_schema_extra={
            'note': 'if Coincident is chosen, then sizing is based on HVAC Sizing Simulations and the input field called Do HVAC Sizing Simulation for Sizing Periods in SimulationControl must be set to Yes'
        },
    )
    zone_timesteps_in_averaging_window: int | None = Field(
        default=1,
        ge=1,
        json_schema_extra={
            'note': 'this is used in the coincident sizing algorithm to apply a running average to peak flow rates that occur during HVAC Sizing Simulations'
        },
    )
    coincident_sizing_factor_mode: (
        Literal[
            'GlobalCoolingSizingFactor',
            'GlobalHeatingSizingFactor',
            'LoopComponentSizingFactor',
            'None',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'this is used to adjust the result for coincident sizing by applying a sizing factor'
        },
    )

    @property
    def plant_or_condenser_loop(self) -> CondenserLoop | PlantLoop | None:
        v = self.plant_or_condenser_loop_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['PlantLoops'])


class SizingSystem(IDFBaseModel):
    """Specifies the input needed to perform sizing calculations for a central
    forced air system. System design air flow, heating capacity, and cooling
    capacity will be calculated using this input data."""

    _idf_object_type: ClassVar[str] = 'Sizing:System'
    airloop_name: AirPrimaryLoopsRef = Field(
        ..., json_schema_extra={'object_list': ['AirPrimaryLoops']}
    )
    type_of_load_to_size_on: (
        Literal['', 'Latent', 'Sensible', 'Total', 'VentilationRequirement'] | None
    ) = Field(
        default='Sensible',
        json_schema_extra={
            'note': 'Specifies the basis for sizing the system supply air flow rate Sensible and Total use the zone design air flow rates to size the system supply air flow rate The cooling coil will then be sized at e...'
        },
    )
    design_outdoor_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    central_heating_maximum_system_air_flow_ratio: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize')
    preheat_design_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    preheat_design_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    precool_design_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    precool_design_humidity_ratio: float = Field(
        ..., json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    central_cooling_design_supply_air_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    central_heating_design_supply_air_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    type_of_zone_sum_to_use: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='NonCoincident'
    )
    n100_outdoor_air_in_cooling: Literal['', 'No', 'Yes'] | None = Field(
        default='No', validation_alias='100_outdoor_air_in_cooling'
    )
    n100_outdoor_air_in_heating: Literal['', 'No', 'Yes'] | None = Field(
        default='No', validation_alias='100_outdoor_air_in_heating'
    )
    central_cooling_design_supply_air_humidity_ratio: float | None = Field(
        default=0.008, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    central_heating_design_supply_air_humidity_ratio: float | None = Field(
        default=0.008, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    cooling_supply_air_flow_rate_method: (
        Literal[
            '',
            'DesignDay',
            'Flow/System',
            'FlowPerCoolingCapacity',
            'FlowPerFloorArea',
            'FractionOfAutosizedCoolingAirflow',
        ]
        | None
    ) = Field(default='DesignDay')
    cooling_supply_air_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if Cooling Supply Air Flow Rate Method is Flow/System This value will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers, this value must ...',
        },
    )
    cooling_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the cooling supply air volume flow rate per total conditioned floor area. Required field when Cooling Supply Air Flow Rate Method is FlowPerFloorArea.',
        },
    )
    cooling_fraction_of_autosized_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when Cooling Supply Air Flow Rate Method is FractionOfAutosizedCoolingAirflow.'
        },
    )
    cooling_supply_air_flow_rate_per_unit_cooling_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the supply air volume flow rate per unit cooling capacity. Required field when Cooling Supply Air Flow Rate Method is FlowPerCoolingCapacity.',
        },
    )
    heating_supply_air_flow_rate_method: (
        Literal[
            '',
            'DesignDay',
            'Flow/System',
            'FlowPerFloorArea',
            'FlowPerHeatingCapacity',
            'FractionOfAutosizedCoolingAirflow',
            'FractionOfAutosizedHeatingAirflow',
        ]
        | None
    ) = Field(default='DesignDay')
    heating_supply_air_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Required field when Heating Supply Air Flow Rate Method is Flow/System This value will *not* be multiplied by any sizing factor or by zone multipliers. If using zone multipliers, this value must be...',
        },
    )
    heating_supply_air_flow_rate_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'Enter the heating supply air volume flow rate per total conditioned floor area. Required field when Heating Supply Air Flow Rate Method is FlowPerFloorArea.',
        },
    )
    heating_fraction_of_autosized_heating_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the heating supply air flow rate. Required field when Heating Supply Air Flow Rate Method is FractionOfAutosizedHeatingAirflow.'
        },
    )
    heating_fraction_of_autosized_cooling_supply_air_flow_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the supply air volume flow rate as a fraction of the cooling supply air flow rate. Required field when Heating Supply Air Flow Rate Method is FractionOfAutosizedCoolingAirflow.'
        },
    )
    heating_supply_air_flow_rate_per_unit_heating_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'Enter the heating supply air volume flow rate per unit heating capacity. Required field when Heating Supply Air Flow Rate Method is FlowPerHeatingCapacity.',
        },
    )
    system_outdoor_air_method: (
        Literal[
            '',
            'Standard62.1SimplifiedProcedure',
            'Standard62.1VentilationRateProcedure',
            'ZoneSum',
        ]
        | None
    ) = Field(default='ZoneSum')
    zone_maximum_outdoor_air_fraction: float | None = Field(
        default=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    cooling_design_capacity_method: (
        Literal[
            '',
            'CapacityPerFloorArea',
            'CoolingDesignCapacity',
            'FractionOfAutosizedCoolingCapacity',
            'None',
        ]
        | None
    ) = Field(
        default='CoolingDesignCapacity',
        json_schema_extra={
            'note': 'Enter the method used to determine the system cooling design capacity for scalable sizing. None is used when a cooling coils is not included in an airloop or this field may be blank. If this input ...'
        },
    )
    cooling_design_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'W', 'note': 'Enter the design cooling capacity.'},
    )
    cooling_design_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m2',
            'note': 'Enter the cooling design capacity per total floor area of cooled zones served by an airloop. Required field when the cooling design capacity method field is CapacityPerFloorArea.',
        },
    )
    fraction_of_autosized_cooling_design_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the fraction of auto-sized cooling design capacity. Required field when the cooling design capacity method field is FractionOfAutosizedCoolingCapacity.'
        },
    )
    heating_design_capacity_method: (
        Literal[
            '',
            'CapacityPerFloorArea',
            'FractionOfAutosizedHeatingCapacity',
            'HeatingDesignCapacity',
            'None',
        ]
        | None
    ) = Field(
        default='HeatingDesignCapacity',
        json_schema_extra={
            'note': 'Enter the method used to determine the heating design capacity for scalable sizing. None is used when a heating coil not included in an airloop or this field may be blank. If this input field is le...'
        },
    )
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity.'},
    )
    heating_design_capacity_per_floor_area: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/m2',
            'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.',
        },
    )
    fraction_of_autosized_heating_design_capacity: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Enter the fraction of auto-sized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'
        },
    )
    central_cooling_capacity_control_method: (
        Literal['', 'Bypass', 'OnOff', 'VAV', 'VT'] | None
    ) = Field(
        default='OnOff',
        json_schema_extra={'note': "Method used to control the coil's output"},
    )
    occupant_diversity: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize',
        json_schema_extra={
            'note': "The Occupant Diversity is used to determine a multi-zone system's outdoor air intake when the System Outdoor Air Method is Standard62.1VentilationRateProcedure or the Standard62.1SimplifiedProcedur..."
        },
    )
    heating_coil_sizing_method: (
        Literal[
            '',
            'CoolingCapacity',
            'GreaterOfHeatingOrCooling',
            'HeatingCapacity',
            'None',
        ]
        | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Size a heat pump heating coil using the Cooling, Heating or GreaterOfHeatingOrCooling capacities'
        },
    )
    maximum_heating_capacity_to_cooling_capacity_sizing_ratio: float | None = Field(
        default=1.0,
        ge=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'The limit of heating coil capacity to cooling coil capacity',
        },
    )

    @property
    def airloop(self) -> AirLoopHVAC | None:
        v = self.airloop_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirPrimaryLoops'])


class SizingZone(IDFBaseModel):
    """Specifies the data needed to perform a zone design air flow calculation. The
    calculation is done for every sizing period included in the input. The
    maximum cooling and heating load and cooling, heating, and ventilation air
    flows are then saved for system level and zone component design
    calculations."""

    _idf_object_type: ClassVar[str] = 'Sizing:Zone'
    zone_or_zonelist_name: ZoneAndZoneListNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneAndZoneListNames']}
    )
    zone_cooling_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(default='SupplyAirTemperature')
    zone_cooling_design_supply_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_cooling_design_supply_air_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Cooling Design Supply Air Temperature is only used when Zone Cooling Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be subtracted from...',
        },
    )
    zone_heating_design_supply_air_temperature_input_method: (
        Literal['', 'SupplyAirTemperature', 'TemperatureDifference'] | None
    ) = Field(default='SupplyAirTemperature')
    zone_heating_design_supply_air_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = SupplyAirTemperature',
        },
    )
    zone_heating_design_supply_air_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Zone Heating Design Supply Air Temperature is only used when Zone Heating Design Supply Air Temperature Input Method = TemperatureDifference The absolute value of this field will be added to the zo...',
        },
    )
    zone_cooling_design_supply_air_humidity_ratio: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    zone_heating_design_supply_air_humidity_ratio: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    design_specification_outdoor_air_object_name: (
        DSOASpaceListNamesRef | DesignSpecificationOutdoorAirNamesRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames'],
            'note': 'Specify the name of a DesignSpecification:OutdoorAir object to specify one set of requirements for the Zone. Use a DesignSpecification:OutdoorAir:SpaceList object name to specify different requirem...',
        },
    )
    zone_heating_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'if blank or zero, global heating sizing factor from Sizing:Parameters is used.'
        },
    )
    zone_cooling_sizing_factor: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'if blank or zero, global cooling sizing factor from Sizing:Parameters is used.'
        },
    )
    cooling_design_air_flow_method: (
        Literal['', 'DesignDay', 'DesignDayWithLimit', 'Flow/Zone'] | None
    ) = Field(default='DesignDay')
    cooling_design_air_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if Cooling Design Air Flow Method is Flow/Zone This value will be multiplied by the global or zone sizing factor and by zone multipliers.',
        },
    )
    cooling_minimum_air_flow_per_zone_floor_area: float | None = Field(
        default=0.000762,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'default is .15 cfm/ft2 This input is used if Cooling Design Air Flow Method is DesignDayWithLimit',
        },
    )
    cooling_minimum_air_flow: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if Cooling Design Air Flow Method is DesignDayWithLimit',
        },
    )
    cooling_minimum_air_flow_fraction: float | None = Field(
        default=0.2,
        ge=0.0,
        json_schema_extra={
            'note': 'fraction of the Cooling design Air Flow Rate This input is currently used in sizing the VAV air terminal unit and fan minimum flow rate It does not currently affect other component autosizing.'
        },
    )
    heating_design_air_flow_method: (
        Literal['', 'DesignDay', 'DesignDayWithLimit', 'Flow/Zone'] | None
    ) = Field(default='DesignDay')
    heating_design_air_flow_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'This input is used if Heating Design Air Flow Method is Flow/Zone. This value will be multiplied by the global or zone sizing factor and by zone multipliers.',
        },
    )
    heating_maximum_air_flow_per_zone_floor_area: float | None = Field(
        default=0.002032,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-m2',
            'note': 'default is .40 cfm/ft2 This field is used to size the heating design flow rate when Heating Design Air Flow Method = Flow/Zone. This input is used for autosizing components when Heating Design Air ...',
        },
    )
    heating_maximum_air_flow: float | None = Field(
        default=0.1415762,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'default is 300 cfm This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.',
        },
    )
    heating_maximum_air_flow_fraction: float | None = Field(
        default=0.3,
        ge=0.0,
        json_schema_extra={
            'note': 'fraction of the Heating Design Air Flow Rate This input is used for autosizing components when Heating Design Air Flow Method = DesignDayWithLimit.'
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
    account_for_dedicated_outdoor_air_system: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'account for effect of dedicated outdoor air system supplying air directly to the zone'
        },
    )
    dedicated_outdoor_air_system_control_strategy: (
        Literal['', 'ColdSupplyAir', 'NeutralDehumidifiedSupplyAir', 'NeutralSupplyAir']
        | None
    ) = Field(
        default='NeutralSupplyAir',
        json_schema_extra={
            'note': '1)supply neutral ventilation air; 2)supply neutral dehumidified and reheated ventilation air; 3)supply cold ventilation air'
        },
    )
    dedicated_outdoor_air_low_setpoint_temperature_for_design: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'C'})
    dedicated_outdoor_air_high_setpoint_temperature_for_design: (
        float | Literal['', 'Autosize'] | None
    ) = Field(default='Autosize', json_schema_extra={'units': 'C'})
    zone_load_sizing_method: (
        Literal[
            '',
            'Latent Load',
            'Sensible And Latent Load',
            'Sensible Load',
            'Sensible Load Only No Latent Load',
        ]
        | None
    ) = Field(
        default='Sensible Load Only No Latent Load',
        json_schema_extra={
            'note': 'Specifies the basis for sizing the zone supply air flow rate. Zone latent loads will not be used during sizing only when Zone Load Sizing Method = Sensible Load Only No Latent Load. For this case t...'
        },
    )
    zone_latent_cooling_design_supply_air_humidity_ratio_input_method: (
        Literal['', 'HumidityRatioDifference', 'SupplyAirHumidityRatio'] | None
    ) = Field(
        default='HumidityRatioDifference',
        json_schema_extra={
            'note': 'Use SupplyAirHumidityRatio to enter the humidity ratio when zone dehumidification is required. The supply air humidity ratio should be less than the zone humidity ratio at the zone thermostat and h...'
        },
    )
    zone_dehumidification_design_supply_air_humidity_ratio: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Zone Dehumidification Design Supply Air Humidity Ratio is only used when Zone Latent Cooling Design Supply Air Humidity Ratio Input Method = SupplyAirHumidityRatio. This input must be less than the...',
        },
    )
    zone_cooling_design_supply_air_humidity_ratio_difference: float | None = Field(
        default=0.005,
        gt=0.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Zone Dehumidification Design Supply Air Humidity Ratio Difference is only used when Zone Latent Cooling Design Supply Air Humidity Ratio Input Method = HumidityRatioDifference. This input is a posi...',
        },
    )
    zone_latent_heating_design_supply_air_humidity_ratio_input_method: (
        Literal['', 'HumidityRatioDifference', 'SupplyAirHumidityRatio'] | None
    ) = Field(
        default='HumidityRatioDifference',
        json_schema_extra={
            'note': 'Use SupplyAirHumidityRatio to enter the humidity ratio when zone humidification is required. The supply air humidity ratio should be greater than the zone humidity ratio at the zone thermostat and ...'
        },
    )
    zone_humidification_design_supply_air_humidity_ratio: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Zone Humidification Design Supply Air Humidity Ratio is only used when Zone Latent Heating Design Supply Air Humidity Ratio Input Method = SupplyAirHumidityRatio. This input must be greater than th...',
        },
    )
    zone_humidification_design_supply_air_humidity_ratio_difference: float | None = (
        Field(
            default=0.005,
            ge=0.0,
            json_schema_extra={
                'units': 'kgWater/kgDryAir',
                'note': 'Zone Humidification Design Supply Air Humidity Ratio is only used when Zone Latent Heating Design Supply Air Humidity Ratio Input Method = HumidityRatioDifference. This input is a positive value an...',
            },
        )
    )
    zone_humidistat_dehumidification_set_point_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the zone relative humidity schedule used for zone latent cooling calculations. A zone humidistat will take priority over this input. This field is not used if Zone Load Sizing Method = Sensib...',
        },
    )
    zone_humidistat_humidification_set_point_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'Enter the zone relative humidity schedule used for zone latent heating calculations. A zone humidistat will take priority over this input. This field is not used if Zone Load Sizing Method = Sensib...',
            },
        )
    )
    type_of_space_sum_to_use: Literal['', 'Coincident', 'NonCoincident'] | None = Field(
        default='Coincident',
        json_schema_extra={
            'note': 'NonCoincident is available only if Do Space Heat Balance for Sizing=Yes in ZoneAirHeatBalanceAlgorithm.'
        },
    )
    heating_coil_sizing_method: (
        Literal[
            '',
            'CoolingCapacity',
            'GreaterOfHeatingOrCooling',
            'HeatingCapacity',
            'None',
        ]
        | None
    ) = Field(default='None')
    maximum_heating_capacity_to_cooling_load_sizing_ratio: float | None = Field(
        default=1.0, ge=1.0, json_schema_extra={'units': 'W/W'}
    )

    @property
    def zone_or_zonelist(self) -> Zone | ZoneList | None:
        v = self.zone_or_zonelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneAndZoneListNames'])

    @property
    def design_specification_outdoor_air_object(
        self,
    ) -> DesignSpecificationOutdoorAir | DesignSpecificationOutdoorAirSpaceList | None:
        v = self.design_specification_outdoor_air_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['DSOASpaceListNames', 'DesignSpecificationOutdoorAirNames']
        )

    @property
    def design_specification_zone_air_distribution_object(
        self,
    ) -> DesignSpecificationZoneAirDistribution | None:
        v = self.design_specification_zone_air_distribution_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DesignSpecificationZoneAirDistributionNames'])

    @property
    def zone_humidistat_dehumidification_set_point_schedule(
        self,
    ) -> IDFBaseModel | None:
        v = self.zone_humidistat_dehumidification_set_point_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_humidistat_humidification_set_point_schedule(self) -> IDFBaseModel | None:
        v = self.zone_humidistat_humidification_set_point_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])
