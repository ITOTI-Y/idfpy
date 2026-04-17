"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 26.1.
Group: Variable Refrigerant Flow Equipment
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AFNCoilNamesRef,
    AFNHeatExchangerNamesRef,
    AFNReliefAirFlowNamesRef,
    AFNTerminalUnitNamesRef,
    AirflowNetworkComponentNamesRef,
    AirflowNetworkDistributionLinkageNamesRef,
    AirFlowNetworkMultizoneZonesRef,
    AirflowNetworkNodeAndZoneNamesRef,
    AirflowNetworkNodeNamesRef,
    AirflowNetworkOccupantVentilationControlNamesRef,
    AirLoopControllersRef,
    AirPrimaryLoopsRef,
    AllHeatTranSurfNamesRef,
    BivariateFunctionsRef,
    BranchListsRef,
    CondenserOperationSchemesRef,
    ConnectorListsRef,
    ControllerMechanicalVentNamesRef,
    CoolingCoilsDXMultiModeOrSingleSpeedRef,
    CoolingCoilsDXVariableSpeedRef,
    DesiccantHXPerfDataRef,
    DesignSpecificationOutdoorAirNamesRef,
    DesignSpecificationZoneAirDistributionNamesRef,
    DSOASpaceListNamesRef,
    ExternalNodeNamesRef,
    FansCVandOnOffandVAVRef,
    FansCVandVAVRef,
    FansOnOffandVAVRef,
    FansSystemModelRef,
    FansZoneExhaustRef,
    FluidAndGlycolNamesRef,
    FluidNamesRef,
    HeatingCoilNameRef,
    HXDesiccantBalancedRef,
    IndependentVariableListNameRef,
    IndependentVariableNameRef,
    OutdoorAirMixersRef,
    OutdoorAirNodeNamesRef,
    PlantOperationSchemesRef,
    ReferenceCrackConditionsRef,
    RoomAirflowNetworkNodesRef,
    ScheduleNamesRef,
    SurfaceAirflowLeakageNamesRef,
    SurfAndSubSurfNamesRef,
    SystemAvailabilityManagerListsRef,
    UnivariateFunctionsRef,
    WaterStorageTankNamesRef,
    WPCSetNamesRef,
    WPCValueNamesRef,
    ZoneAndZoneListNamesRef,
    ZoneNamesRef,
    ZoneTerminalUnitListNamesRef,
    ZoneTerminalUnitNamesRef,
)

if TYPE_CHECKING:
    from .air_distribution import AirLoopHVAC, OutdoorAirMixer
    from .availability_managers import AvailabilityManagerAssignmentList
    from .coils import (
        CoilCoolingDXSingleSpeed,
        CoilCoolingDXTwoStageWithHumidityControlMode,
        CoilCoolingDXVariableSpeed,
        CoilHeatingElectric,
        CoilHeatingFuel,
        CoilHeatingSteam,
        CoilHeatingWater,
    )
    from .fans import (
        FanConstantVolume,
        FanOnOff,
        FanSystemModel,
        FanVariableVolume,
        FanZoneExhaust,
    )
    from .fluids import FluidPropertiesGlycolConcentration, FluidPropertiesName
    from .hvac_design import (
        DesignSpecificationOutdoorAir,
        DesignSpecificationOutdoorAirSpaceList,
        DesignSpecificationZoneAirDistribution,
    )
    from .node_branch import BranchList, ConnectorList, OutdoorAirNode
    from .plant_control import (
        CondenserEquipmentOperationSchemes,
        PlantEquipmentOperationSchemes,
    )
    from .room_air import RoomAirNodeAirflowNetwork
    from .thermal_zones import Zone, ZoneList
    from .water_systems import WaterUseStorage
    from .zone_forced_air import ZoneHVACTerminalUnitVariableRefrigerantFlow
    from .zone_terminals import (
        AirTerminalSingleDuctConstantVolumeReheat,
        AirTerminalSingleDuctVAVReheat,
    )


class AirConditionerVariableRefrigerantFlowFluidTemperatureControlLoadingIndicesItem(
    IDFBaseModel
):
    """Nested object type for array items."""

    compressor_speed_at_loading_index: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'rev/min', 'note': 'Minimum compressor speed'},
    )
    loading_index_evaporative_capacity_multiplier_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['BivariateFunctions']}
    )
    loading_index_compressor_power_multiplier_function_of_temperature_curve_name: BivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['BivariateFunctions']}
    )

    @property
    def loading_index_evaporative_capacity_multiplier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.loading_index_evaporative_capacity_multiplier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def loading_index_compressor_power_multiplier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.loading_index_compressor_power_multiplier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class AirflowNetworkDistributionDuctViewFactorsSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""

    surface_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    surface_view_factor: float | None = Field(default=None, ge=0.0, le=1.0)

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])


class ControllerMechanicalVentilationZoneSpecificationsItem(IDFBaseModel):
    """Nested object type for array items."""

    zone_or_zonelist_name: ZoneAndZoneListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneAndZoneListNames'],
            'note': 'A zone name or a zone list name may be used here',
        },
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
    design_specification_zone_air_distribution_object_name: (
        DesignSpecificationZoneAirDistributionNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['DesignSpecificationZoneAirDistributionNames'],
            'note': 'If left blank, the name will be taken from the Sizing:Zone object for this zone. If no specification is found for this zone, then effectiveness will be 1.0 and and secondary recirculation will be z...',
        },
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


class MatrixTwoDimensionValuesItem(IDFBaseModel):
    """Nested object type for array items."""

    value: float | None = Field(default=None)


class ParametricFileNameSuffixSuffixesItem(IDFBaseModel):
    """Nested object type for array items."""

    suffix_for_file_name_in_run: str | None = Field(default=None)


class ParametricLogicLinesItem(IDFBaseModel):
    """Nested object type for array items."""

    parametric_logic_line: str | None = Field(default=None)


class ParametricRunControlRunsItem(IDFBaseModel):
    """Nested object type for array items."""

    perform_run: Literal['', 'No', 'Yes'] | None = Field(default='Yes')


class ParametricSetValueForRunValuesItem(IDFBaseModel):
    """Nested object type for array items."""

    value_for_run: str | None = Field(default=None)


class TableIndependentVariableListIndependentVariablesItem(IDFBaseModel):
    """Nested object type for array items."""

    independent_variable_name: IndependentVariableNameRef = Field(
        ..., json_schema_extra={'object_list': ['IndependentVariableName']}
    )

    @property
    def independent_variable(self) -> TableIndependentVariable | None:
        v = self.independent_variable_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['IndependentVariableName'])


class TableLookupValuesItem(IDFBaseModel):
    """Nested object type for array items."""

    output_value: float | None = Field(default=None)


class ZoneTerminalUnitListTerminalUnitsItem(IDFBaseModel):
    """Nested object type for array items."""

    zone_terminal_unit_name: ZoneTerminalUnitNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneTerminalUnitNames']}
    )

    @property
    def zone_terminal_unit(self) -> ZoneHVACTerminalUnitVariableRefrigerantFlow | None:
        v = self.zone_terminal_unit_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneTerminalUnitNames'])


class AirConditionerVariableRefrigerantFlow(IDFBaseModel):
    """Variable refrigerant flow (VRF) air-to-air heat pump condensing unit
    (includes one or more electric compressors and outdoor fan). Serves one or
    more VRF zone terminal units. See
    ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and ZoneTerminalUnitList."""

    _idf_object_type: ClassVar[str] = 'AirConditioner:VariableRefrigerantFlow'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter a unique name for this variable refrigerant flow heat pump.'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available. Enter the name of a schedule that defines the a...',
        },
    )
    gross_rated_total_cooling_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
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
    minimum_condenser_inlet_node_temperature_in_cooling_mode: float | None = Field(
        default=-6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'For cooling mode operation, enter the minimum inlet outdoor air dry-bulb temperature for air-cooled units or minimum inlet water temperature for water-cooled units. Cooling is disabled below this t...',
        },
    )
    maximum_condenser_inlet_node_temperature_in_cooling_mode: float | None = Field(
        default=43.0,
        json_schema_extra={
            'units': 'C',
            'note': 'For cooling mode operation, enter the maximum inlet outdoor air dry-bulb temperature for air-cooled units or maximum inlet water temperature for water-cooled units. Cooling is disabled above this t...',
        },
    )
    cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Enter a curve name that represents full load cooling capacity ratio as a function of outdoor dry-bulb temperature and indoor wet-bulb temperature. Up to two curves are allowed if the performance ca...',
        },
    )
    cooling_capacity_ratio_boundary_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve object is used to allow separate low and high cooling capacity ratio performance curves. This curve represents a line passing through the points where performance changes. The curve calc...',
        },
    )
    cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'This curve object is used to describe the high outdoor temperature performance curve used to describe cooling capacity ratio. This curve is used when a single performance curve does not accurately ...',
        },
    )
    cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Enter a curve name that represents cooling energy ratio as a function of outdoor dry-bulb temperature and indoor wet-bulb temperature',
        },
    )
    cooling_energy_input_ratio_boundary_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'This curve object is used to allow separate low and high cooling energy input ratio performance curves. This curve represents a line passing through the points where performance changes. The curve ...',
            },
        )
    )
    cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'This curve object is used to describe the high outdoor temperature performance curve used to describe cooling energy ratio. This curve is used when a single performance curve does not accurately de...',
        },
    )
    cooling_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter a curve name that represents cooling energy ratio as a function of part-load ratio for part-load ratios less than or equal to 1. If this field is left blank, the model assumes energy is propo...',
        },
    )
    cooling_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter a curve name that represents cooling energy ratio as a function of part-load ratio for part-load ratios greater than 1. Part-load ratios can exceed 1 in variable speed compression systems. If...',
        },
    )
    cooling_combination_ratio_correction_factor_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve defines how rated capacity changes when the total indoor terminal unit cooling capacity is greater than the Gross Rated Total Cooling Capacity defined in this object. If this field is le...',
        },
    )
    cooling_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'This curve defines the cycling losses when the heat pump compressor cycles on and off below the Minimum Heat Pump Part-Load Ratio specified in the field below.',
            },
        )
    )
    gross_rated_heating_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
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
    minimum_condenser_inlet_node_temperature_in_heating_mode: float | None = Field(
        default=-20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'For heating mode operation, enter the minimum inlet outdoor air dry-bulb temperature for air-cooled units or minimum inlet water temperature for water-cooled units. Heating is disabled below this t...',
        },
    )
    maximum_condenser_inlet_node_temperature_in_heating_mode: float | None = Field(
        default=16.0,
        json_schema_extra={
            'units': 'C',
            'note': 'For heating mode operation, enter the maximum inlet outdoor air dry-bulb temperature for air-cooled units or maximum inlet water temperature for water-cooled units. Heating is disabled below this t...',
        },
    )
    heating_capacity_ratio_modifier_function_of_low_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Enter a curve name that represents full load heating capacity ratio as a function of outdoor wet-bulb temperature and indoor dry-bulb temperature. Outdoor dry-bulb temperature may be used if wet-bu...',
        },
    )
    heating_capacity_ratio_boundary_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve object is used to allow separate low and high heating capacity ratio performance curves. This curve represents a line passing through the points where performance changes. The curve calc...',
        },
    )
    heating_capacity_ratio_modifier_function_of_high_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'This curve object is used to describe the high outdoor temperature performance curve used to describe heating capacity ratio. This curve is used when a single performance curve does not accurately ...',
        },
    )
    heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Enter a curve name that represents heating energy ratio as a function of outdoor wet-bulb temperature and indoor dry-bulb temperature Outdoor dry-bulb temperature may be used if wet-bulb temperatur...',
        },
    )
    heating_energy_input_ratio_boundary_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'This curve object is used to allow separate low and high heating energy input ratio performance curves. This curve represents a line passing through the points where performance changes. The curve ...',
            },
        )
    )
    heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'This curve object is used to allow separate performance curves for heating energy. If a single performance curve is used, leave this field blank.',
        },
    )
    heating_performance_curve_outdoor_temperature_type: (
        Literal['', 'DryBulbTemperature', 'WetBulbTemperature'] | None
    ) = Field(
        default='WetBulbTemperature',
        json_schema_extra={
            'note': 'Determines temperature type for heating capacity curves and heating energy curves. This input determines whether the outdoor air dry-bulb or wet-bulb temperature is used to evaluate these curves.'
        },
    )
    heating_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve represents the heating energy input ratio for part-load ratios less than 1.',
        },
    )
    heating_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve represents the heating energy input ratio for part-load ratios greater than 1.',
        },
    )
    heating_combination_ratio_correction_factor_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'This curve defines how rated capacity changes when the total indoor terminal unit heating capacity is greater than the Gross Rated Heating Capacity defined in this object. If this field is left bla...',
        },
    )
    heating_part_load_fraction_correlation_curve_name: UnivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['UnivariateFunctions'],
                'note': 'This curve defines the cycling losses when the heat pump compressor cycles on and off below the Minimum Heat Pump Part-Load Ratio specified in the following field.',
            },
        )
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
            'note': 'Choose a thermostat control logic scheme. If these control types fail to control zone temperature within a reasonable limit, consider using multiple VRF systems. This field is not used when all ter...'
        },
    )
    thermostat_priority_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'this field is required if Master Thermostat Priority Control Type is Scheduled. Schedule values of 0 denote cooling, 1 for heating, and all other values disable the system.',
        },
    )
    zone_terminal_unit_list_name: ZoneTerminalUnitListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneTerminalUnitListNames'],
            'note': 'Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this heat pump.',
        },
    )
    heat_pump_waste_heat_recovery: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'This field enables heat recovery operation within this VRF outdoor unit.'
        },
    )
    equivalent_piping_length_used_for_piping_correction_factor_in_cooling_mode: (
        float | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the equivalent length of the farthest terminal unit from the condenser',
        },
    )
    vertical_height_used_for_piping_correction_factor: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the height difference between the highest and lowest terminal unit',
        },
    )
    piping_correction_factor_for_length_in_cooling_mode_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) where L = length and CR = combination ratio specifies coefficients for a0, a1, a2, and a3 in the PCF...',
        },
    )
    piping_correction_factor_for_height_in_cooling_mode_coefficient: float | None = (
        Field(
            default=0.0,
            json_schema_extra={
                'units': '1/m',
                'note': 'PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H where L = length, H = height, and CR = combination ratio specifies coefficient a4 (or a6 for ...',
            },
        )
    )
    equivalent_piping_length_used_for_piping_correction_factor_in_heating_mode: (
        float | None
    ) = Field(
        default=None,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the equivalent length of the farthest terminal unit from the condenser',
        },
    )
    piping_correction_factor_for_length_in_heating_mode_curve_name: (
        BivariateFunctionsRef | UnivariateFunctionsRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions', 'UnivariateFunctions'],
            'note': 'PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H where L = length and CR = combination ratio specifies coefficients for a0, a1, a2, and a3 (or...',
        },
    )
    piping_correction_factor_for_height_in_heating_mode_coefficient: float | None = (
        Field(
            default=0.0,
            json_schema_extra={
                'units': '1/m',
                'note': 'PCF = a0 + a1*L + a2*L^2 + a3*L^3 + a4*H PCF = a0 + a1*L + a2*L^2 + a3*CR + a4*CR^2 + a5*(L)(CR) + a6*H where L = length, H = height, and CR = combination ratio specifies coefficient a4 (or a6 for ...',
            },
        )
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
    defrost_energy_input_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'A valid performance curve must be used if reversecycle defrost strategy is selected.',
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
        default=0.0,
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
            'note': 'Select either an air-cooled, evaporatively-cooled or water-cooled condenser.'
        },
    )
    condenser_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Choose an outside air node name or leave this field blank to use weather data. If this field is blank, the Condenser Type is assumed to be AirCooled. This input must be specified if Condenser Type ...'
        },
    )
    condenser_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Enter a water outlet node name if Condenser Type = WaterCooled. Leave this field blank if Condenser Type = Air or EvaporativelyCooled.'
        },
    )
    water_condenser_volume_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
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
    evaporative_condenser_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
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
    supply_water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['WaterStorageTankNames'],
            'note': 'A separate storage tank may be used to supply an evaporatively cooled condenser.',
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
    minimum_condenser_inlet_node_temperature_in_heat_recovery_mode: float | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'C',
                'note': 'For heat recovery mode operation, enter the minimum inlet outdoor air dry-bulb temperature for air-cooled units or minimum inlet water temperature for water-cooled units. Heat recovery is disabled ...',
            },
        )
    )
    maximum_condenser_inlet_node_temperature_in_heat_recovery_mode: float | None = (
        Field(
            default=None,
            json_schema_extra={
                'units': 'C',
                'note': 'For heat recovery mode operation, enter the maximum inlet outdoor air dry-bulb temperature for air-cooled units or maximum inlet water temperature for water-cooled units. Heat recovery is disabled ...',
            },
        )
    )
    heat_recovery_cooling_capacity_modifier_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Enter the name of a performance curve which represents the change in cooling capacity when heat recovery is active A default constant of 0.9 is used if this input is blank',
            },
        )
    )
    initial_heat_recovery_cooling_capacity_fraction: float | None = Field(
        default=0.5,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the fractional capacity available at the start of heat recovery mode. The capacity exponentially approaches the steady-state value according to the inputs for Heat Recovery Cooling Capacity M...',
        },
    )
    heat_recovery_cooling_capacity_time_constant: float | None = Field(
        default=0.15,
        json_schema_extra={
            'units': 'hr',
            'note': 'Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    heat_recovery_cooling_energy_modifier_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Enter the name of a performance curve which represents the change in cooling energy when heat recovery is active A default constant of 1.1 is used if this input is blank',
            },
        )
    )
    initial_heat_recovery_cooling_energy_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the fractional electric consumption rate at the start of heat recovery mode. The electric consumption rate exponentially approaches the steady-state value according to the inputs for Heat Rec...',
        },
    )
    heat_recovery_cooling_energy_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    heat_recovery_heating_capacity_modifier_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Enter the name of a performance curve which represents the change in heating capacity when heat recovery is active A default constant of 1.1 is used if this input is blank',
            },
        )
    )
    initial_heat_recovery_heating_capacity_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the fractional capacity available at the start of heat recovery mode. The capacity exponentially approaches the steady-state value according to the inputs for Heat Recovery Heating Capacity M...',
        },
    )
    heat_recovery_heating_capacity_time_constant: float | None = Field(
        default=0.15,
        json_schema_extra={
            'units': 'hr',
            'note': 'Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    heat_recovery_heating_energy_modifier_curve_name: BivariateFunctionsRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['BivariateFunctions'],
                'note': 'Enter the name of a performance curve which represents the change in heating electric consumption rate when heat recovery is active A default constant of 1.1 is used if this input is blank',
            },
        )
    )
    initial_heat_recovery_heating_energy_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'Enter the fractional electric consumption rate at the start of heat recovery mode. The electric consumption rate exponentially approaches the steady-state value according to the inputs for Heat Rec...',
        },
    )
    heat_recovery_heating_energy_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_capacity_ratio_modifier_function_of_low_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_capacity_ratio_boundary_curve(self) -> IDFBaseModel | None:
        v = self.cooling_capacity_ratio_boundary_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_capacity_ratio_modifier_function_of_high_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_energy_input_ratio_boundary_curve(self) -> IDFBaseModel | None:
        v = self.cooling_energy_input_ratio_boundary_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def cooling_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cooling_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_combination_ratio_correction_factor_curve(self) -> IDFBaseModel | None:
        v = self.cooling_combination_ratio_correction_factor_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def cooling_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.cooling_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_capacity_ratio_modifier_function_of_low_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_ratio_modifier_function_of_low_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heating_capacity_ratio_boundary_curve(self) -> IDFBaseModel | None:
        v = self.heating_capacity_ratio_boundary_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_capacity_ratio_modifier_function_of_high_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_capacity_ratio_modifier_function_of_high_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heating_energy_input_ratio_modifier_function_of_low_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heating_energy_input_ratio_boundary_curve(self) -> IDFBaseModel | None:
        v = self.heating_energy_input_ratio_boundary_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_energy_input_ratio_modifier_function_of_high_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heating_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.heating_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_combination_ratio_correction_factor_curve(self) -> IDFBaseModel | None:
        v = self.heating_combination_ratio_correction_factor_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def heating_part_load_fraction_correlation_curve(self) -> IDFBaseModel | None:
        v = self.heating_part_load_fraction_correlation_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def zone_for_master_thermostat_location_ref(self) -> Zone | None:
        v = self.zone_name_for_master_thermostat_location
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def thermostat_priority_schedule(self) -> IDFBaseModel | None:
        v = self.thermostat_priority_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_terminal_unit_list(self) -> ZoneTerminalUnitList | None:
        v = self.zone_terminal_unit_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneTerminalUnitListNames'])

    @property
    def piping_correction_factor_for_length_in_cooling_mode_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.piping_correction_factor_for_length_in_cooling_mode_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def piping_correction_factor_for_length_in_heating_mode_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.piping_correction_factor_for_length_in_heating_mode_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions', 'UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def supply_water_storage_tank(self) -> WaterUseStorage | None:
        v = self.supply_water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])

    @property
    def basin_heater_operating_schedule(self) -> IDFBaseModel | None:
        v = self.basin_heater_operating_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heat_recovery_cooling_capacity_modifier_curve(self) -> IDFBaseModel | None:
        v = self.heat_recovery_cooling_capacity_modifier_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heat_recovery_cooling_energy_modifier_curve(self) -> IDFBaseModel | None:
        v = self.heat_recovery_cooling_energy_modifier_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heat_recovery_heating_capacity_modifier_curve(self) -> IDFBaseModel | None:
        v = self.heat_recovery_heating_capacity_modifier_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def heat_recovery_heating_energy_modifier_curve(self) -> IDFBaseModel | None:
        v = self.heat_recovery_heating_energy_modifier_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class AirConditionerVariableRefrigerantFlowFluidTemperatureControl(IDFBaseModel):
    """This is a key object in the new physics based VRF model applicable for Fluid
    Temperature Control It describes the Variable Refrigerant Flow system
    excluding the performance of indoor units Indoor units are modeled
    separately, see ZoneHVAC:TerminalUnit:VariableRefrigerantFlow"""

    _idf_object_type: ClassVar[str] = (
        'AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl'
    )
    heat_pump_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter a unique name for this variable refrigerant flow heat pump'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that defines the availability of the unit Schedule values of 0 denote the unit is off. All other values denote the unit is available If this field is left blank, the un...',
        },
    )
    zone_terminal_unit_list_name: ZoneTerminalUnitListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneTerminalUnitListNames'],
            'note': 'Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this heat pump',
        },
    )
    refrigerant_type: FluidNamesRef | None = Field(
        default='R410A', json_schema_extra={'object_list': ['FluidNames']}
    )
    rated_evaporative_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=40000.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the total evaporative capacity in watts at rated conditions This is the capacity corresponding to the max compressor speed at rated conditions The actual evaporative capacity is obtained by m...',
        },
    )
    rated_compressor_power_per_unit_of_rated_evaporative_capacity: float | None = Field(
        default=0.35,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the rated compressor power per Watt of rated evaporative capacity [W/W] Rated compressor power corresponds to the max compressor speed at rated conditions The actual compressor power is obtai...',
        },
    )
    minimum_outdoor_air_temperature_in_cooling_mode: float | None = Field(
        default=-6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for cooling operation Cooling is disabled below this temperature',
        },
    )
    maximum_outdoor_air_temperature_in_cooling_mode: float | None = Field(
        default=43.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for cooling operation Cooling is disabled above this temperature',
        },
    )
    minimum_outdoor_air_temperature_in_heating_mode: float | None = Field(
        default=-20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for heating operation Heating is disabled below this temperature',
        },
    )
    maximum_outdoor_air_temperature_in_heating_mode: float | None = Field(
        default=16.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for heating operation Heating is disabled below this temperature',
        },
    )
    reference_outdoor_unit_superheating: float | None = Field(
        default=3.0, json_schema_extra={'units': 'deltaC'}
    )
    reference_outdoor_unit_subcooling: float | None = Field(
        default=5.0, json_schema_extra={'units': 'deltaC'}
    )
    refrigerant_temperature_control_algorithm_for_indoor_unit: (
        Literal['', 'ConstantTemp', 'VariableTemp'] | None
    ) = Field(default='VariableTemp')
    reference_evaporating_temperature_for_indoor_unit: float | None = Field(
        default=6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is ConstantTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    reference_condensing_temperature_for_indoor_unit: float | None = Field(
        default=44.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is ConstantTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_evaporating_temperature_minimum_for_indoor_unit: float | None = Field(
        default=4.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_evaporating_temperature_maximum_for_indoor_unit: float | None = Field(
        default=13.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_condensing_temperature_minimum_for_indoor_unit: float | None = Field(
        default=42.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_condensing_temperature_maximum_for_indoor_unit: float | None = Field(
        default=46.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity: float | None = Field(
        default=0.00425,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the outdoor unit fan power per Watt of rated evaporative capacity [W/W]',
        },
    )
    outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity: float | None = (
        Field(
            default=7.5e-05,
            gt=0.0,
            json_schema_extra={
                'units': 'm3/s-W',
                'note': 'This field is only used if the previous is set to autocalculate and performance input method is NominalCapacity',
            },
        )
    )
    outdoor_unit_evaporating_temperature_function_of_superheating_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    outdoor_unit_condensing_temperature_function_of_subcooling_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    diameter_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint: (
        float | None
    ) = Field(
        default=0.0762,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'used to calculate the piping loss'},
    )
    length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint: (
        float | None
    ) = Field(
        default=30.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'used to calculate the heat loss of the main pipe',
        },
    )
    equivalent_length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint: (
        float | None
    ) = Field(
        default=36.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'used to calculate the refrigerant pressure drop of the main pipe',
        },
    )
    height_difference_between_outdoor_unit_and_indoor_units: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Difference between outdoor unit height and indoor unit height Positive means outdoor unit is higher than indoor unit Negative means outdoor unit is lower than indoor unit',
        },
    )
    main_pipe_insulation_thickness: float | None = Field(
        default=0.02, ge=0.0, json_schema_extra={'units': 'm'}
    )
    main_pipe_insulation_thermal_conductivity: float | None = Field(
        default=0.032, ge=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    crankcase_heater_power_per_compressor: float | None = Field(
        default=33.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the value of the resistive heater located in the compressor(s). This heater is used to warm the refrigerant and oil when the compressor is off',
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
            'note': 'Enter the ratio of the first stage compressor to total compressor capacity All other compressors are assumed to be equally sized. This inputs is used only for crankcase heater calculations',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which the crankcase heaters are disabled',
        },
    )
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='Resistive',
        json_schema_extra={
            'note': 'Select a defrost strategy. Reverse cycle reverses the operating mode from heating to cooling to melt frost formation on the condenser coil The resistive strategy uses a resistive heater to melt the...'
        },
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed',
        json_schema_extra={
            'note': 'Choose a defrost control type Either use a fixed Timed defrost period or select OnDemand to defrost only when necessary'
        },
    )
    defrost_energy_input_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'A valid performance curve must be used if ReverseCycle defrost strategy is selected',
        },
    )
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode Only applicable if timed defrost control is specified'
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the size of the resistive defrost heating element Only applicable if resistive defrost strategy is specified',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which the defrost operation is disabled',
        },
    )
    compressor_maximum_delta_pressure: float | None = Field(
        default=4500000.0, ge=0.0, le=50000000.0, json_schema_extra={'units': 'Pa'}
    )
    number_of_compressor_loading_index_entries: int | None = Field(
        default=2,
        ge=2,
        le=9,
        json_schema_extra={
            'note': 'First index represents minimal capacity operation Last index represents full capacity operation'
        },
    )
    loading_indices: (
        list[
            AirConditionerVariableRefrigerantFlowFluidTemperatureControlLoadingIndicesItem
        ]
        | None
    ) = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_terminal_unit_list(self) -> ZoneTerminalUnitList | None:
        v = self.zone_terminal_unit_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneTerminalUnitListNames'])

    @property
    def refrigerant_type_ref(self) -> FluidPropertiesName | None:
        v = self.refrigerant_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidNames'])

    @property
    def outdoor_unit_evaporating_temperature_function_of_superheating_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.outdoor_unit_evaporating_temperature_function_of_superheating_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def outdoor_unit_condensing_temperature_function_of_subcooling_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.outdoor_unit_condensing_temperature_function_of_subcooling_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class AirConditionerVariableRefrigerantFlowFluidTemperatureControlHR(IDFBaseModel):
    """This is a key object in the new physics based VRF Heat Recovery (HR) model
    applicable for Fluid Temperature Control. It describes the VRF HR system
    excluding the performance of indoor units. Indoor units are modeled
    separately in the ZoneHVAC:TerminalUnit:VariableRefrigerantFlow object"""

    _idf_object_type: ClassVar[str] = (
        'AirConditioner:VariableRefrigerantFlow:FluidTemperatureControl:HR'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter a unique name for this variable refrigerant flow heat pump'
        },
    )
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Enter the name of a schedule that defines the availability of the unit Schedule values of 0 denote the unit is off. All other values denote the unit is available If this field is left blank, the un...',
        },
    )
    zone_terminal_unit_list_name: ZoneTerminalUnitListNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneTerminalUnitListNames'],
            'note': 'Enter the name of a ZoneTerminalUnitList. This list connects zone terminal units to this heat pump',
        },
    )
    refrigerant_type: FluidNamesRef | None = Field(
        default='R410A', json_schema_extra={'object_list': ['FluidNames']}
    )
    rated_evaporative_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=40000.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the total evaporative capacity in watts at rated conditions This is the capacity corresponding to the max compressor speed at rated conditions The actual evaporative capacity is obtained by m...',
        },
    )
    rated_compressor_power_per_unit_of_rated_evaporative_capacity: float | None = Field(
        default=0.35,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the rated compressor power per Watt of rated evaporative capacity [W/W] Rated compressor power corresponds to the max compressor speed at rated conditions The actual compressor power is obtai...',
        },
    )
    minimum_outdoor_air_temperature_in_cooling_only_mode: float | None = Field(
        default=-6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for cooling operation Cooling is disabled below this temperature',
        },
    )
    maximum_outdoor_air_temperature_in_cooling_only_mode: float | None = Field(
        default=43.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for cooling operation Cooling is disabled above this temperature',
        },
    )
    minimum_outdoor_air_temperature_in_heating_only_mode: float | None = Field(
        default=-20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor temperature allowed for heating operation Heating is disabled below this temperature',
        },
    )
    maximum_outdoor_air_temperature_in_heating_only_mode: float | None = Field(
        default=16.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature allowed for heating operation Heating is disabled below this temperature',
        },
    )
    minimum_outdoor_temperature_in_heat_recovery_mode: float | None = Field(
        default=-20.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The minimum outdoor temperature below which heat recovery mode will not operate.',
        },
    )
    maximum_outdoor_temperature_in_heat_recovery_mode: float | None = Field(
        default=43.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The maximum outdoor temperature above which heat recovery mode will not operate.',
        },
    )
    refrigerant_temperature_control_algorithm_for_indoor_unit: (
        Literal['', 'ConstantTemp', 'VariableTemp'] | None
    ) = Field(default='VariableTemp')
    reference_evaporating_temperature_for_indoor_unit: float | None = Field(
        default=6.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is ConstantTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    reference_condensing_temperature_for_indoor_unit: float | None = Field(
        default=44.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is ConstantTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_evaporating_temperature_minimum_for_indoor_unit: float | None = Field(
        default=4.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_evaporating_temperature_maximum_for_indoor_unit: float | None = Field(
        default=13.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Evaporating temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_condensing_temperature_minimum_for_indoor_unit: float | None = Field(
        default=42.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    variable_condensing_temperature_maximum_for_indoor_unit: float | None = Field(
        default=46.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used if Refrigerant Temperature Control Algorithm is VariableTemp Condensing temperature is the refrigerant temperature, not air temperature',
        },
    )
    outdoor_unit_evaporator_reference_superheating: float | None = Field(
        default=3.0, json_schema_extra={'units': 'deltaC'}
    )
    outdoor_unit_condenser_reference_subcooling: float | None = Field(
        default=5.0, json_schema_extra={'units': 'deltaC'}
    )
    outdoor_unit_evaporator_rated_bypass_factor: float | None = Field(
        default=0.4, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    outdoor_unit_condenser_rated_bypass_factor: float | None = Field(
        default=0.2, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    difference_between_outdoor_unit_evaporating_temperature_and_outdoor_air_temperature_in_heat_recovery_mode: (
        float | None
    ) = Field(default=5.0, json_schema_extra={'units': 'deltaC'})
    outdoor_unit_heat_exchanger_capacity_ratio: float | None = Field(
        default=0.3,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the rated capacity ratio between the main and supplementary outdoor unit heat exchangers [W/W]',
        },
    )
    outdoor_unit_fan_power_per_unit_of_rated_evaporative_capacity: float | None = Field(
        default=0.00425,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the outdoor unit fan power per Watt of rated evaporative capacity [W/W]',
        },
    )
    outdoor_unit_fan_flow_rate_per_unit_of_rated_evaporative_capacity: float | None = (
        Field(
            default=7.5e-05,
            gt=0.0,
            json_schema_extra={
                'units': 'm3/s-W',
                'note': 'Enter the outdoor unit fan flow rate per Watt of rated evaporative capacity [W/W]',
            },
        )
    )
    outdoor_unit_evaporating_temperature_function_of_superheating_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    outdoor_unit_condensing_temperature_function_of_subcooling_curve_name: UnivariateFunctionsRef = Field(
        ..., json_schema_extra={'object_list': ['UnivariateFunctions']}
    )
    diameter_of_main_pipe_for_suction_gas: float | None = Field(
        default=0.0762,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'used to calculate the piping loss'},
    )
    diameter_of_main_pipe_for_discharge_gas: float | None = Field(
        default=0.0762,
        ge=0.0,
        json_schema_extra={'units': 'm', 'note': 'used to calculate the piping loss'},
    )
    length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint: (
        float | None
    ) = Field(
        default=30.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'used to calculate the heat loss of the main pipe',
        },
    )
    equivalent_length_of_main_pipe_connecting_outdoor_unit_to_the_first_branch_joint: (
        float | None
    ) = Field(
        default=36.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'used to calculate the refrigerant pressure drop of the main pipe',
        },
    )
    height_difference_between_outdoor_unit_and_indoor_units: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Difference between outdoor unit height and indoor unit height Positive means outdoor unit is higher than indoor unit Negative means outdoor unit is lower than indoor unit',
        },
    )
    main_pipe_insulation_thickness: float | None = Field(
        default=0.02, ge=0.0, json_schema_extra={'units': 'm'}
    )
    main_pipe_insulation_thermal_conductivity: float | None = Field(
        default=0.032, ge=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    crankcase_heater_power_per_compressor: float | None = Field(
        default=33.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the value of the resistive heater located in the compressor(s). This heater is used to warm the refrigerant and oil when the compressor is off',
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
            'note': 'Enter the ratio of the first stage compressor to total compressor capacity All other compressors are assumed to be equally sized. This inputs is used only for crankcase heater calculations',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_crankcase_heater: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which the crankcase heaters are disabled',
        },
    )
    defrost_strategy: Literal['', 'Resistive', 'ReverseCycle'] | None = Field(
        default='Resistive',
        json_schema_extra={
            'note': 'Select a defrost strategy. Reverse cycle reverses the operating mode from heating to cooling to melt frost formation on the condenser coil The resistive strategy uses a resistive heater to melt the...'
        },
    )
    defrost_control: Literal['', 'OnDemand', 'Timed'] | None = Field(
        default='Timed',
        json_schema_extra={
            'note': 'Choose a defrost control type Either use a fixed Timed defrost period or select OnDemand to defrost only when necessary'
        },
    )
    defrost_energy_input_ratio_modifier_function_of_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'A valid performance curve must be used if ReverseCycle defrost strategy is selected',
        },
    )
    defrost_time_period_fraction: float | None = Field(
        default=0.058333,
        ge=0.0,
        json_schema_extra={
            'note': 'Fraction of time in defrost mode Only applicable if timed defrost control is specified'
        },
    )
    resistive_defrost_heater_capacity: float | Literal['', 'Autosize'] | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Enter the size of the resistive defrost heating element Only applicable if resistive defrost strategy is specified',
        },
    )
    maximum_outdoor_dry_bulb_temperature_for_defrost_operation: float | None = Field(
        default=5.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the maximum outdoor temperature above which the defrost operation is disabled',
        },
    )
    initial_heat_recovery_cooling_capacity_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'This is used to describe the transition from Cooling Only mode to Heat Recovery mode Enter the fractional capacity available at the start of heat recovery mode. The capacity exponentially approache...',
        },
    )
    heat_recovery_cooling_capacity_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'This is used to describe the transition from Cooling Only mode to Heat Recovery mode Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    initial_heat_recovery_cooling_energy_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'This is used to describe the transition from Cooling Only mode to Heat Recovery mode Enter the fractional electric consumption rate at the start of heat recovery mode. The electric consumption rate...',
        },
    )
    heat_recovery_cooling_energy_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'This is used to describe the transition from Cooling Only mode to Heat Recovery mode Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    initial_heat_recovery_heating_capacity_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'This is used to describe the transition from Heating Only mode to Heat Recovery mode Enter the fractional capacity available at the start of heat recovery mode. The capacity exponentially approache...',
        },
    )
    heat_recovery_heating_capacity_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'This is used to describe the transition from Heating Only mode to Heat Recovery mode Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    initial_heat_recovery_heating_energy_fraction: float | None = Field(
        default=1.0,
        json_schema_extra={
            'units': 'W/W',
            'note': 'This is used to describe the transition from Heating Only mode to Heat Recovery mode Enter the fractional electric consumption rate at the start of heat recovery mode. The electric consumption rate...',
        },
    )
    heat_recovery_heating_energy_time_constant: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'hr',
            'note': 'This is used to describe the transition from Heating Only mode to Heat Recovery mode Enter the time constant used to model the transition from cooling only mode to heat recovery mode',
        },
    )
    compressor_maximum_delta_pressure: float | None = Field(
        default=4500000.0, ge=0.0, le=50000000.0, json_schema_extra={'units': 'Pa'}
    )
    compressor_inverter_efficiency: float | None = Field(
        default=0.95,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Efficiency of the compressor inverter',
        },
    )
    compressor_evaporative_capacity_correction_factor: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Describe the evaporative capacity difference because of system configuration difference between test bed and real system.',
        },
    )
    number_of_compressor_loading_index_entries: int | None = Field(
        default=2,
        ge=2,
        json_schema_extra={
            'note': 'Load index describe the compressor operational state, either a single compressor or multiple compressors, at different load levels. First index represents minimal capacity operation Last index repr...'
        },
    )
    loading_indices: (
        list[
            AirConditionerVariableRefrigerantFlowFluidTemperatureControlLoadingIndicesItem
        ]
        | None
    ) = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_terminal_unit_list(self) -> ZoneTerminalUnitList | None:
        v = self.zone_terminal_unit_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneTerminalUnitListNames'])

    @property
    def refrigerant_type_ref(self) -> FluidPropertiesName | None:
        v = self.refrigerant_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidNames'])

    @property
    def outdoor_unit_evaporating_temperature_function_of_superheating_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.outdoor_unit_evaporating_temperature_function_of_superheating_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def outdoor_unit_condensing_temperature_function_of_subcooling_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.outdoor_unit_condensing_temperature_function_of_subcooling_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def defrost_energy_input_ratio_modifier_function_of_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.defrost_energy_input_ratio_modifier_function_of_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])


class AirLoopHVACControllerList(IDFBaseModel):
    """List controllers in order of control sequence"""

    _idf_object_type: ClassVar[str] = 'AirLoopHVAC:ControllerList'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    controller_1_object_type: Literal[
        'Controller:OutdoorAir', 'Controller:WaterCoil'
    ] = Field(...)
    controller_1_name: AirLoopControllersRef = Field(
        ..., json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_2_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_2_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_3_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_3_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_4_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_4_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_5_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_5_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_6_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_6_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_7_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_7_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )
    controller_8_object_type: (
        Literal['Controller:OutdoorAir', 'Controller:WaterCoil'] | None
    ) = Field(default=None)
    controller_8_name: AirLoopControllersRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AirLoopControllers']}
    )

    @property
    def controller_1(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_2(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_3(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_3_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_4(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_4_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_5(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_5_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_6(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_6_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_7(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_7_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])

    @property
    def controller_8(self) -> ControllerOutdoorAir | ControllerWaterCoil | None:
        v = self.controller_8_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirLoopControllers'])


class AirflowNetworkDistributionComponentCoil(IDFBaseModel):
    """This object defines the name of a coil used in an air loop."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Component:Coil'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'coil_name'})
    coil_name: AFNCoilNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AFNCoilNames'],
            'note': 'Enter the name of a cooling or heating coil in the primary Air loop.',
        },
    )
    coil_object_type: Literal[
        'Coil:Cooling:DX',
        'Coil:Cooling:DX:MultiSpeed',
        'Coil:Cooling:DX:SingleSpeed',
        'Coil:Cooling:DX:TwoSpeed',
        'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
        'Coil:Cooling:DX:VariableSpeed',
        'Coil:Cooling:Water',
        'Coil:Cooling:Water:DetailedGeometry',
        'Coil:Cooling:WaterToAirHeatPump:EquationFit',
        'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
        'Coil:Heating:DX:MultiSpeed',
        'Coil:Heating:DX:SingleSpeed',
        'Coil:Heating:DX:VariableSpeed',
        'Coil:Heating:Desuperheater',
        'Coil:Heating:Electric',
        'Coil:Heating:Electric:MultiStage',
        'Coil:Heating:Fuel',
        'Coil:Heating:Gas:MultiStage',
        'Coil:Heating:Water',
        'Coil:Heating:WaterToAirHeatPump:EquationFit',
        'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Select the type of coil corresponding to the name entered in the field above.'
        },
    )
    air_path_length: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the air path length (depth) for the coil.',
        },
    )
    air_path_hydraulic_diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the hydraulic diameter of this coil. The hydraulic diameter is defined as 4 multiplied by the cross section area divided by perimeter.',
        },
    )

    @property
    def coil(self) -> IDFBaseModel | None:
        v = self.coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AFNCoilNames'])


class AirflowNetworkDistributionComponentConstantPressureDrop(IDFBaseModel):
    """This object defines the characteristics of a constant pressure drop
    component (e.g. filter). Each node connected to this object can not be a
    node of mixer, splitter, a node of air primary loop, or zone equipment loop.
    It is recommended to connect to a duct component at both ends."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:ConstantPressureDrop'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    pressure_difference_across_the_component: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter the pressure drop across this component.',
        },
    )


class AirflowNetworkDistributionComponentDuct(IDFBaseModel):
    """This object defines the relationship between pressure and air flow through
    the duct."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Component:Duct'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    duct_length: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm', 'note': 'Enter the length of the duct.'},
    )
    hydraulic_diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the hydraulic diameter of the duct. Hydraulic diameter is defined as 4 multiplied by cross section area divided by perimeter',
        },
    )
    cross_section_area: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm2',
            'note': 'Enter the cross section area of the duct.',
        },
    )
    surface_roughness: float | None = Field(
        default=0.0009,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the inside surface roughness of the duct.',
        },
    )
    coefficient_for_local_dynamic_loss_due_to_fitting: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the coefficient used to calculate dynamic losses of fittings (e.g. elbows).',
        },
    )
    heat_transmittance_coefficient_u_factor_for_duct_wall_construction: float | None = (
        Field(
            default=0.943,
            gt=0.0,
            json_schema_extra={
                'units': 'W/m2-K',
                'note': 'conduction only Default value of 0.943 is equivalent to 1.06 m2-K/W (R6) duct insulation.',
            },
        )
    )
    overall_moisture_transmittance_coefficient_from_air_to_air: float | None = Field(
        default=0.001,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/m2',
            'note': 'Enter the overall moisture transmittance coefficient including moisture film coefficients at both surfaces.',
        },
    )
    outside_convection_coefficient: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'optional. convection coefficient calculated automatically, unless specified',
        },
    )
    inside_convection_coefficient: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'optional. convection coefficient calculated automatically, unless specified',
        },
    )


class AirflowNetworkDistributionComponentFan(IDFBaseModel):
    """This object defines the name of the supply Air Fan used in an Air loop."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Component:Fan'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'fan_name'})
    fan_name: FansCVandOnOffandVAVRef | FansSystemModelRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansCVandOnOffandVAV', 'FansSystemModel'],
            'note': 'Enter the name of the fan in the primary air loop.',
        },
    )
    supply_fan_object_type: (
        Literal[
            '',
            'Fan:ConstantVolume',
            'Fan:OnOff',
            'Fan:SystemModel',
            'Fan:VariableVolume',
        ]
        | None
    ) = Field(default='Fan:ConstantVolume')

    @property
    def fan(
        self,
    ) -> FanConstantVolume | FanOnOff | FanSystemModel | FanVariableVolume | None:
        v = self.fan_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FansCVandOnOffandVAV', 'FansSystemModel'])


class AirflowNetworkDistributionComponentHeatExchanger(IDFBaseModel):
    """This object defines the name of an air-to-air heat exchanger used in an air
    loop."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:HeatExchanger'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'heatexchanger_name'})
    heatexchanger_name: AFNHeatExchangerNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AFNHeatExchangerNames'],
            'note': 'Enter the name of an air-to-air heat exchanger in the primary Air loop.',
        },
    )
    heatexchanger_object_type: Literal[
        'HeatExchanger:AirToAir:FlatPlate',
        'HeatExchanger:AirToAir:SensibleAndLatent',
        'HeatExchanger:Desiccant:BalancedFlow',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Select the type of heat exchanger corresponding to the name entered in the field above.'
        },
    )
    air_path_length: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the air path length (depth) for the heat exchanger.',
        },
    )
    air_path_hydraulic_diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the hydraulic diameter of this heat exchanger. The hydraulic diameter is defined as 4 multiplied by the cross section area divided by perimeter.',
        },
    )

    @property
    def heatexchanger(
        self,
    ) -> (
        HeatExchangerAirToAirFlatPlate
        | HeatExchangerAirToAirSensibleAndLatent
        | HeatExchangerDesiccantBalancedFlow
        | None
    ):
        v = self.heatexchanger_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AFNHeatExchangerNames'])


class AirflowNetworkDistributionComponentLeak(IDFBaseModel):
    """This object defines the characteristics of a supply or return air leak."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Component:Leak'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_mass_flow_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'Defined at 1 Pa pressure difference across this component. Enter the coefficient used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent',
        },
    )
    air_mass_flow_exponent: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent',
        },
    )


class AirflowNetworkDistributionComponentLeakageRatio(IDFBaseModel):
    """This object is used to define supply and return air leaks with respect to
    the fan's maximum air flow rate."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:LeakageRatio'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    effective_leakage_ratio: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Defined as a ratio of leak flow rate to the maximum flow rate.',
        },
    )
    maximum_flow_rate: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Enter the maximum air flow rate in this air loop.',
        },
    )
    reference_pressure_difference: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter the pressure corresponding to the Effective leakage ratio entered above.',
        },
    )
    air_mass_flow_exponent: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the air mass flow equation.',
        },
    )


class AirflowNetworkDistributionComponentOutdoorAirFlow(IDFBaseModel):
    """This object includes the outdoor air flow rate set by the
    Controller:OutdoorAir object in the airflow network."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:OutdoorAirFlow'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    outdoor_air_mixer_name: OutdoorAirMixersRef = Field(
        ..., json_schema_extra={'object_list': ['OutdoorAirMixers']}
    )
    air_mass_flow_coefficient_when_no_outdoor_air_flow_at_reference_conditions: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'Enter the air mass flow coefficient at the conditions defined in the Reference Crack Conditions object. Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation: Ma...',
        },
    )
    air_mass_flow_exponent_when_no_outdoor_air_flow: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when no outdoor air flow rate.',
        },
    )
    reference_crack_conditions: ReferenceCrackConditionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ReferenceCrackConditions'],
            'note': 'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with the air mass flow coefficient entered above.',
        },
    )

    @property
    def outdoor_air_mixer(self) -> OutdoorAirMixer | None:
        v = self.outdoor_air_mixer_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['OutdoorAirMixers'])

    @property
    def reference_crack_conditions_ref(
        self,
    ) -> AirflowNetworkMultiZoneReferenceCrackConditions | None:
        v = self.reference_crack_conditions
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ReferenceCrackConditions'])


class AirflowNetworkDistributionComponentReliefAirFlow(IDFBaseModel):
    """This object allows variation of air flow rate to perform pressure."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:ReliefAirFlow'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    outdoor_air_mixer_name: OutdoorAirMixersRef = Field(
        ..., json_schema_extra={'object_list': ['OutdoorAirMixers']}
    )
    air_mass_flow_coefficient_when_no_outdoor_air_flow_at_reference_conditions: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'Enter the air mass flow coefficient at the conditions defined in the Reference Crack Conditions object. Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation: Ma...',
        },
    )
    air_mass_flow_exponent_when_no_outdoor_air_flow: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when no outdoor air flow rate.',
        },
    )
    reference_crack_conditions: ReferenceCrackConditionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ReferenceCrackConditions'],
            'note': 'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with the air mass flow coefficient entered above.',
        },
    )

    @property
    def outdoor_air_mixer(self) -> OutdoorAirMixer | None:
        v = self.outdoor_air_mixer_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['OutdoorAirMixers'])

    @property
    def reference_crack_conditions_ref(
        self,
    ) -> AirflowNetworkMultiZoneReferenceCrackConditions | None:
        v = self.reference_crack_conditions
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ReferenceCrackConditions'])


class AirflowNetworkDistributionComponentTerminalUnit(IDFBaseModel):
    """This object defines the name of a terminal unit in an air loop."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:Distribution:Component:TerminalUnit'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'terminal_unit_name'})
    terminal_unit_name: AFNTerminalUnitNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AFNTerminalUnitNames'],
            'note': 'Enter the name of a terminal unit in the AirLoopHVAC.',
        },
    )
    terminal_unit_object_type: Literal[
        'AirTerminal:SingleDuct:ConstantVolume:Reheat',
        'AirTerminal:SingleDuct:VAV:Reheat',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'Select the type of terminal unit corresponding to the name entered in the field above.'
        },
    )
    air_path_length: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the air path length (depth) for the terminal unit.',
        },
    )
    air_path_hydraulic_diameter: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the hydraulic diameter of this terminal unit. The hydraulic diameter is defined as 4 multiplied by the cross section area divided by perimeter.',
        },
    )

    @property
    def terminal_unit(
        self,
    ) -> (
        AirTerminalSingleDuctConstantVolumeReheat
        | AirTerminalSingleDuctVAVReheat
        | None
    ):
        v = self.terminal_unit_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AFNTerminalUnitNames'])


class AirflowNetworkDistributionDuctSizing(IDFBaseModel):
    """This object defines required parameters for duct sizing in an Airflow
    Network simulation. To activate duct sizing, see
    AirflowNetwork:SimulationControl Do Distribution Duct Sizing Calculation."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:DuctSizing'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    duct_sizing_method: (
        Literal[
            '', 'MaximumVelocity', 'PressureLoss', 'PressureLossWithMaximumVelocity'
        ]
        | None
    ) = Field(default='MaximumVelocity')
    duct_sizing_factor: float | None = Field(default=1.0, gt=0.0)
    maximum_airflow_velocity: float | None = Field(
        default=5.0,
        le=25.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm/s',
            'note': 'Used only if Duct Sizing Type = MaximumVelocity or PressureLossWithMaximumVelocity. When MaximumVelocity is entered, duct diameter is calculated at D = flow rate / cross section area. When Pressure...',
        },
    )
    total_pressure_loss_across_supply_trunk: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': "Used only if Duct Sizing Type = PressureLoss or PressureLossWithMaximumVelocity. When PressureLoss is entered, duct diameter is calculated using Colebrook's equation When PressureLossWithMaximumVel...",
        },
    )
    total_pressure_loss_across_supply_branch: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': "Duct diameter is calculated using Colebrook's equation. When there is no solution, velocity = 5 m/s is used to calculate duct diameter.",
        },
    )
    total_pressure_loss_across_return_trunk: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': "Duct diameter is calculated using Colebrook's equation. When there is no solution, velocity = 5 m/s is used to calculate duct diameter.",
        },
    )
    total_pressure_loss_across_return_branch: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': "Duct diameter is calculated using Colebrook's equation. When there is no solution, velocity = 5 m/s is used to calculate duct diameter.",
        },
    )


class AirflowNetworkDistributionDuctViewFactors(IDFBaseModel):
    """This object is used to allow user-defined view factors to be used for duct-
    surface radiation calculations. All surfaces must be in the same enclosure."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:DuctViewFactors'
    linkage_name: AirflowNetworkComponentNamesRef = Field(
        ..., json_schema_extra={'object_list': ['AirflowNetworkComponentNames']}
    )
    duct_surface_exposure_fraction: float | None = Field(default=0.0, ge=0.0, le=1.0)
    duct_surface_emittance: float | None = Field(default=0.9, ge=0.0, le=1.0)
    surfaces: list[AirflowNetworkDistributionDuctViewFactorsSurfacesItem] | None = (
        Field(default=None)
    )

    @property
    def linkage(self) -> IDFBaseModel | None:
        v = self.linkage_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkComponentNames'])


class AirflowNetworkDistributionLinkage(IDFBaseModel):
    """This object defines the connection between two nodes and a component."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Linkage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    node_1_name: AirflowNetworkNodeAndZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirflowNetworkNodeAndZoneNames'],
            'note': 'Enter the name of zone or AirflowNetwork Node.',
        },
    )
    node_2_name: AirflowNetworkNodeAndZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirflowNetworkNodeAndZoneNames'],
            'note': 'Enter the name of zone or AirflowNetwork Node.',
        },
    )
    component_name: (
        AFNCoilNamesRef
        | AFNHeatExchangerNamesRef
        | AFNTerminalUnitNamesRef
        | AirflowNetworkComponentNamesRef
        | FansCVandOnOffandVAVRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': [
                'AFNCoilNames',
                'AFNHeatExchangerNames',
                'AFNTerminalUnitNames',
                'AirflowNetworkComponentNames',
                'FansCVandOnOffandVAV',
            ],
            'note': 'Enter the name of an AirflowNetwork component. A component is one of the following AirflowNetwork:Distribution:Component objects: Leak, LeakageRatio, Duct, ConstantVolumeFan, Coil, TerminalUnit, Co...',
        },
    )
    thermal_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Only used if component = AirflowNetwork:Distribution:Component:Duct The zone name is where AirflowNetwork:Distribution:Component:Duct is exposed. Leave this field blank if the duct conduction loss ...',
        },
    )

    @property
    def node_1(self) -> AirflowNetworkDistributionNode | Zone | None:
        v = self.node_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkNodeAndZoneNames'])

    @property
    def node_2(self) -> AirflowNetworkDistributionNode | Zone | None:
        v = self.node_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkNodeAndZoneNames'])

    @property
    def component(self) -> IDFBaseModel | None:
        v = self.component_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v,
            [
                'AFNCoilNames',
                'AFNHeatExchangerNames',
                'AFNTerminalUnitNames',
                'AirflowNetworkComponentNames',
                'FansCVandOnOffandVAV',
            ],
        )

    @property
    def thermal_zone(self) -> Zone | None:
        v = self.thermal_zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])


class AirflowNetworkDistributionNode(IDFBaseModel):
    """This object represents an air distribution node in the AirflowNetwork model."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:Distribution:Node'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    component_name_or_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Designates node names defined in another object. The node name may occur in air branches. Enter a node name to represent a node already defined in an air loop. Leave this field blank if the Node or...'
        },
    )
    component_object_type_or_node_type: (
        Literal[
            '',
            'AirLoopHVAC:OutdoorAirSystem',
            'AirLoopHVAC:ZoneMixer',
            'AirLoopHVAC:ZoneSplitter',
            'OAMixerOutdoorAirStreamNode',
            'Other',
            'OutdoorAir:Node',
            'OutdoorAir:NodeList',
            'Zone',
        ]
        | None
    ) = Field(
        default='Other',
        json_schema_extra={
            'note': 'Designates Node type for the Node or Component Name defined in the field above. AirLoopHVAC:ZoneMixer -- Represents a AirLoopHVAC:ZoneMixer object. AirLoopHVAC:ZoneSplitter -- Represents a AirLoopH...'
        },
    )
    node_height: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the reference height used to calculate the relative pressure.',
        },
    )


class AirflowNetworkIntraZoneLinkage(IDFBaseModel):
    """This object defines the connection between two nodes and a component used in
    the combination of RoomAir and AirflowNetwork model."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:IntraZone:Linkage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    node_1_name: AirflowNetworkNodeNamesRef | ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirflowNetworkNodeNames', 'ZoneNames'],
            'note': 'Enter the name of zone or AirflowNetwork Node.',
        },
    )
    node_2_name: AirflowNetworkNodeNamesRef | ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirflowNetworkNodeNames', 'ZoneNames'],
            'note': 'Enter the name of zone or AirflowNetwork Node.',
        },
    )
    component_name: AirflowNetworkComponentNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AirflowNetworkComponentNames'],
            'note': 'Enter the name of an AirflowNetwork component. A component is one of the following AirflowNetwork:Multizone:Component objects: AirflowNetwork:MultiZone:Surface:Crack, AirflowNetwork:MultiZone:Surfa...',
        },
    )
    airflownetwork_multizone_surface_name: SurfAndSubSurfNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['SurfAndSubSurfNames'],
            'note': 'Only used when one of two nodes defined above are not located in the same zone, and the input of the Component Name field in this object is ignored',
        },
    )

    @property
    def node_1(self) -> AirflowNetworkIntraZoneNode | Zone | None:
        v = self.node_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkNodeNames', 'ZoneNames'])

    @property
    def node_2(self) -> AirflowNetworkIntraZoneNode | Zone | None:
        v = self.node_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkNodeNames', 'ZoneNames'])

    @property
    def component(self) -> IDFBaseModel | None:
        v = self.component_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkComponentNames'])

    @property
    def airflownetwork_multizone_surface(self) -> IDFBaseModel | None:
        v = self.airflownetwork_multizone_surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SurfAndSubSurfNames'])


class AirflowNetworkIntraZoneNode(IDFBaseModel):
    """This object represents a node in a zone in the combination of RoomAir and
    AirflowNetwork model."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:IntraZone:Node'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    roomair_node_airflownetwork_name: RoomAirflowNetworkNodesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['RoomAirflowNetworkNodes'],
            'note': 'Enter the name of a RoomAir:Node object defined in a RoomAirSettings:AirflowNetwork object.',
        },
    )
    zone_name: AirFlowNetworkMultizoneZonesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AirFlowNetworkMultizoneZones'],
            'note': 'Enter the name of a zone object defined in a AirflowNetwork:MultiZone:Zone object.',
        },
    )
    node_height: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Enter the reference height used to calculate the relative pressure',
        },
    )

    @property
    def roomair_node_airflownetwork(self) -> RoomAirNodeAirflowNetwork | None:
        v = self.roomair_node_airflownetwork_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['RoomAirflowNetworkNodes'])

    @property
    def zone(self) -> AirflowNetworkMultiZoneZone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirFlowNetworkMultizoneZones'])


class AirflowNetworkMultiZoneComponentDetailedOpening(IDFBaseModel):
    """This object specifies the properties of airflow through windows and doors
    (window, door and glass door heat transfer subsurfaces) when they are closed
    or open."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:Component:DetailedOpening'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_mass_flow_coefficient_when_opening_is_closed: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s-m',
            'note': 'Defined at 1 Pa per meter of crack length. Enter the coefficient used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening (wi...',
        },
    )
    air_mass_flow_exponent_when_opening_is_closed: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening (window or door) is closed.',
        },
    )
    type_of_rectangular_large_vertical_opening_lvo: (
        Literal['', 'HorizontallyPivoted', 'NonPivoted'] | None
    ) = Field(
        default='NonPivoted',
        validation_alias='type_of_rectangular_large_vertical_opening_lvo_',
        json_schema_extra={
            'note': 'Select the type of vertical opening: Non-pivoted opening or Horizontally pivoted opening.'
        },
    )
    extra_crack_length_or_height_of_pivoting_axis: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Extra crack length is used for LVO Non-pivoted type with multiple openable parts. Height of pivoting axis is used for LVO Horizontally pivoted type. Specifies window or door characteristics that de...',
        },
    )
    number_of_sets_of_opening_factor_data: int = Field(
        ...,
        ge=2,
        le=4,
        json_schema_extra={
            'note': 'Enter the number of the following sets of data for opening factor, discharge coefficient, width factor, height factor, and start height factor.'
        },
    )
    opening_factor_1: float | None = Field(
        default=0.0,
        ge=0.0,
        le=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This value must be specified as 0.',
        },
    )
    discharge_coefficient_for_opening_factor_1: float | None = Field(
        default=0.001,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through a window or door at that Opening Factor.',
        },
    )
    width_factor_for_opening_factor_1: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Width Factor is the opening width divided by the window or door width.',
        },
    )
    height_factor_for_opening_factor_1: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Height Factor is the opening height divided by the window or door height.',
        },
    )
    start_height_factor_for_opening_factor_1: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Start Height Factor is the Start Height divided by the window or door height. Start Height is the distance between the bottom of the window or door and the bottom of the window or door opening....',
        },
    )
    opening_factor_2: float = Field(
        ...,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'If Number of Sets of Opening Factor Data = 2, this value must be 1.0. If Number of Sets of Opening Factor Data = 3, this value must be less than 1.0. If Number of Sets of Opening Factor Data = 4, t...',
        },
    )
    discharge_coefficient_for_opening_factor_2: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through a window or door at that Opening Factor.',
        },
    )
    width_factor_for_opening_factor_2: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Width Factor is the opening width divided by the window or door width.',
        },
    )
    height_factor_for_opening_factor_2: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Height Factor is the opening height divided by the window or door height.',
        },
    )
    start_height_factor_for_opening_factor_2: float | None = Field(
        default=0.0,
        ge=0.0,
        lt=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Start Height Factor is the Start Height divided by the window or door height. Start Height is the distance between the bottom of the window or door and the bottom of the window or door opening....',
        },
    )
    opening_factor_3: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'If Number of Sets of Opening Factor Data = 3, this value must be 1.0. If Number of Sets of Opening Factor Data = 4, this value must be less than 1.0, and greater than value entered for Opening fact...',
        },
    )
    discharge_coefficient_for_opening_factor_3: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through a window or door at that Opening Factor.',
        },
    )
    width_factor_for_opening_factor_3: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Width Factor is the opening width divided by the window or door width.',
        },
    )
    height_factor_for_opening_factor_3: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Height Factor is the opening height divided by the window or door height.',
        },
    )
    start_height_factor_for_opening_factor_3: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Start Height Factor is the Start Height divided by the window or door height. Start Height is the distance between the bottom of the window or door and the bottom of the window or door opening....',
        },
    )
    opening_factor_4: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'If Number of Sets of Opening Factor Data = 4, this value must be 1.0',
        },
    )
    discharge_coefficient_for_opening_factor_4: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through a window or door at that Opening Factor.',
        },
    )
    width_factor_for_opening_factor_4: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Width Factor is the opening width divided by the window or door width.',
        },
    )
    height_factor_for_opening_factor_4: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Height Factor is the opening height divided by the window or door height.',
        },
    )
    start_height_factor_for_opening_factor_4: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Start Height Factor is the Start Height divided by the window or door height. Start Height is the distance between the bottom of the window or door and the bottom of the window or door opening....',
        },
    )


class AirflowNetworkMultiZoneComponentHorizontalOpening(IDFBaseModel):
    """This object specifies the properties of air flow through a horizontal
    opening"""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:Component:HorizontalOpening'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_mass_flow_coefficient_when_opening_is_closed: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s-m',
            'note': 'Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation: Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening is closed.',
        },
    )
    air_mass_flow_exponent_when_opening_is_closed: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass flow rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening is closed.',
        },
    )
    sloping_plane_angle: float | None = Field(
        default=90.0,
        le=90.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Sloping plane angle = 90 is equivalent to fully open.',
        },
    )
    discharge_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through the opening at that Opening Factor.',
        },
    )


class AirflowNetworkMultiZoneComponentSimpleOpening(IDFBaseModel):
    """This object specifies the properties of air flow through windows and doors
    (window, door and glass door heat transfer subsurfaces) when they are closed
    or open."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:Component:SimpleOpening'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_mass_flow_coefficient_when_opening_is_closed: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s-m',
            'note': 'Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening (window o...',
        },
    )
    air_mass_flow_exponent_when_opening_is_closed: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when opening (window or door) is closed.',
        },
    )
    minimum_density_difference_for_two_way_flow: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/m3',
            'note': 'Enter the minimum density difference above which two-way flow may occur due to stack effect.',
        },
    )
    discharge_coefficient: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'The Discharge Coefficient indicates the fractional effectiveness for air flow through a window or door at that Opening Factor.',
        },
    )


class AirflowNetworkMultiZoneComponentZoneExhaustFan(IDFBaseModel):
    """This object specifies the additional properties for a zone exhaust fan to
    perform multizone airflow calculations."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:Component:ZoneExhaustFan'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: FansZoneExhaustRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FansZoneExhaust'],
            'note': 'Enter the name of a Fan:ZoneExhaust object.',
        },
    )
    air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'Enter the air mass flow coefficient at the conditions defined in the Reference Crack Conditions object. Defined at 1 Pa pressure difference. Enter the coefficient used in the following equation: Ma...',
        },
    )
    air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the following equation: Mass Flow Rate = Air Mass Flow Coefficient * (dP)^Air Mass Flow Exponent. Used only when the fan is off.',
        },
    )
    reference_crack_conditions: ReferenceCrackConditionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ReferenceCrackConditions'],
            'note': 'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with the air mass flow coefficient entered above.',
        },
    )

    @property
    def name_ref(self) -> FanZoneExhaust | None:
        v = self.name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FansZoneExhaust'])

    @property
    def reference_crack_conditions_ref(
        self,
    ) -> AirflowNetworkMultiZoneReferenceCrackConditions | None:
        v = self.reference_crack_conditions
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ReferenceCrackConditions'])


class AirflowNetworkMultiZoneExternalNode(IDFBaseModel):
    """This object defines outdoor environmental conditions outside of the
    building."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:ExternalNode'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter a unique name for this object. This node name will be referenced by a particular building facade.'
        },
    )
    external_node_height: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Designates the reference height used to calculate relative pressure.',
        },
    )
    wind_pressure_coefficient_curve_name: UnivariateFunctionsRef | WPCValueNamesRef = (
        Field(
            ...,
            json_schema_extra={
                'object_list': ['UnivariateFunctions', 'WPCValueNames'],
                'note': 'The name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues, curve, or table object specifying the wind pressure coefficient.',
            },
        )
    )
    symmetric_wind_pressure_coefficient_curve: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Specify whether the pressure curve is symmetric or not. Specify Yes for curves that should be evaluated from 0 to 180 degrees Specify No for curves that should be evaluated from 0 to 360 degrees'
        },
    )
    wind_angle_type: Literal['', 'Absolute', 'Relative'] | None = Field(
        default='Absolute',
        json_schema_extra={
            'note': 'Specify whether the angle used to compute the wind pressure coefficient is absolute or relative Specify Relative to compute the angle between the wind direction and the surface azimuth Specify Abso...'
        },
    )

    @property
    def wind_pressure_coefficient_curve(self) -> IDFBaseModel | None:
        v = self.wind_pressure_coefficient_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions', 'WPCValueNames'])


class AirflowNetworkMultiZoneReferenceCrackConditions(IDFBaseModel):
    """This object specifies the conditions under which the air mass flow
    coefficient was measured."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:ReferenceCrackConditions'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    reference_temperature: float = Field(
        ...,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the reference temperature under which the surface crack data were obtained. Suggested value 20C.',
        },
    )
    reference_barometric_pressure: float | None = Field(
        default=101325.0,
        ge=31000.0,
        le=120000.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter the reference barometric pressure under which the surface crack data were obtained.',
        },
    )
    reference_humidity_ratio: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Enter the reference humidity ratio under which the surface crack data were obtained.',
        },
    )


class AirflowNetworkMultiZoneSpecifiedFlowRate(IDFBaseModel):
    """This object is used to define specified flow through a linkage."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:SpecifiedFlowRate'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_flow_value: float = Field(
        ..., json_schema_extra={'note': 'Enter the specified flow rate.'}
    )
    air_flow_units: Literal['', 'MassFlow', 'VolumetricFlow'] | None = Field(
        default='MassFlow',
        json_schema_extra={
            'note': 'Enter the units of the air flow value. VolumetricFlow (m3/s) MassFlow (kg/s)'
        },
    )


class AirflowNetworkMultiZoneSurface(IDFBaseModel):
    """This object specifies the properties of a surface linkage through which air
    flows. Airflow Report: Node 1 as an inside face zone; Node 2 as an outside
    face zone or external node."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:Surface'
    surface_name: SurfAndSubSurfNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SurfAndSubSurfNames'],
            'note': 'Enter the name of a heat transfer surface.',
        },
    )
    leakage_component_name: SurfaceAirflowLeakageNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SurfaceAirflowLeakageNames'],
            'note': 'Enter the name of an Airflow Network leakage component. A leakage component is one of the following AirflowNetwork:Multizone objects: AirflowNetwork:MultiZone:Component:DetailedOpening, AirflowNetw...',
        },
    )
    external_node_name: (ExternalNodeNamesRef | OutdoorAirNodeNamesRef) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ExternalNodeNames', 'OutdoorAirNodeNames'],
            'note': 'Used if Wind Pressure Coefficient Type = Input in the AirflowNetwork:SimulationControl object, otherwise this field may be left blank.',
        },
    )
    window_door_opening_factor_or_crack_factor: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This field specifies a multiplier for a crack, window, or door.',
        },
    )
    ventilation_control_mode: (
        Literal[
            '',
            'ASHRAE55Adaptive',
            'AdjacentEnthalpy',
            'AdjacentTemperature',
            'CEN15251Adaptive',
            'Constant',
            'Enthalpy',
            'NoVent',
            'Temperature',
            'ZoneLevel',
        ]
        | None
    ) = Field(
        default='ZoneLevel',
        json_schema_extra={
            'note': "When Ventilation Control Mode = Temperature or Enthalpy, the following fields are used to modulate the Ventilation Open Factor for a window or door opening according to the parent zone's indoor-out..."
        },
    )
    ventilation_control_zone_temperature_setpoint_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Ventilation Control Mode = Temperature or Enthalpy.',
        },
    )
    minimum_venting_open_factor: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Used only if Ventilation Control Mode = Temperature or Enthalpy.',
        },
    )
    indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        lt=100.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Applicable only if Ventilation Control Mode = Temperature',
        },
    )
    indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor: (
        float | None
    ) = Field(
        default=100.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Applicable only if Ventilation Control Mode = Temperature. This value must be greater than the corresponding lower value (previous field).',
        },
    )
    indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        lt=300000.0,
        json_schema_extra={
            'units': 'deltaJ/kg',
            'note': 'Applicable only if Ventilation Control Mode = Enthalpy. This value must be less than the corresponding upper value (next field).',
        },
    )
    indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor: (
        float | None
    ) = Field(
        default=300000.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaJ/kg',
            'note': 'Applicable only if Ventilation Control Mode = Enthalpy. This value must be greater than the corresponding lower value (previous field).',
        },
    )
    venting_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Non-zero schedule value means venting is allowed if other venting control conditions are satisfied. A zero (or negative) schedule value means venting is not allowed under any circumstances. The sch...',
        },
    )
    occupant_ventilation_control_name: (
        AirflowNetworkOccupantVentilationControlNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AirflowNetworkOccupantVentilationControlNames'],
            'note': 'Enter the name where Occupancy Ventilation Control is required.',
        },
    )
    equivalent_rectangle_method: (
        Literal['', 'BaseSurfaceAspectRatio', 'PolygonHeight', 'UserDefinedAspectRatio']
        | None
    ) = Field(
        default='PolygonHeight',
        json_schema_extra={
            'note': 'This field is applied to a non-rectangular window or door. The equivalent shape has the same area as a polygonal window or door.'
        },
    )
    equivalent_rectangle_aspect_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This field is used when UserDefinedAspectRatio is entered in the Equivalent Rectangle Method field.',
        },
    )

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SurfAndSubSurfNames'])

    @property
    def leakage_component(self) -> IDFBaseModel | None:
        v = self.leakage_component_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SurfaceAirflowLeakageNames'])

    @property
    def external_node(
        self,
    ) -> AirflowNetworkMultiZoneExternalNode | OutdoorAirNode | None:
        v = self.external_node_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ExternalNodeNames', 'OutdoorAirNodeNames'])

    @property
    def ventilation_control_zone_temperature_setpoint_schedule(
        self,
    ) -> IDFBaseModel | None:
        v = self.ventilation_control_zone_temperature_setpoint_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def venting_availability_schedule(self) -> IDFBaseModel | None:
        v = self.venting_availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def occupant_ventilation_control(
        self,
    ) -> AirflowNetworkOccupantVentilationControl | None:
        v = self.occupant_ventilation_control_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['AirflowNetworkOccupantVentilationControlNames']
        )


class AirflowNetworkMultiZoneSurfaceCrack(IDFBaseModel):
    """This object specifies the properties of airflow through a crack."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:Surface:Crack'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    air_mass_flow_coefficient_at_reference_conditions: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'Enter the air mass flow coefficient at the conditions defined in the Reference Crack Conditions object. Defined at 1 Pa pressure difference across this crack.',
        },
    )
    air_mass_flow_exponent: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the air mass flow exponent for the surface crack.',
        },
    )
    reference_crack_conditions: ReferenceCrackConditionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ReferenceCrackConditions'],
            'note': 'Select a AirflowNetwork:MultiZone:ReferenceCrackConditions name associated with the air mass flow coefficient entered above.',
        },
    )

    @property
    def reference_crack_conditions_ref(
        self,
    ) -> AirflowNetworkMultiZoneReferenceCrackConditions | None:
        v = self.reference_crack_conditions
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ReferenceCrackConditions'])


class AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea(IDFBaseModel):
    """This object is used to define surface air leakage."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    effective_leakage_area: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={'units': 'm2', 'note': 'Enter the effective leakage area.'},
    )
    discharge_coefficient: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the coefficient used in the air mass flow equation.',
        },
    )
    reference_pressure_difference: float | None = Field(
        default=4.0,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'Enter the pressure difference used to define the air mass flow coefficient and exponent.',
        },
    )
    air_mass_flow_exponent: float | None = Field(
        default=0.65,
        ge=0.5,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the exponent used in the air mass flow equation.',
        },
    )


class AirflowNetworkMultiZoneWindPressureCoefficientArray(IDFBaseModel):
    """Used only if Wind Pressure Coefficient (WPC) Type = Input in the
    AirflowNetwork:SimulationControl object. Number of WPC Values in the
    corresponding AirflowNetwork:MultiZone:WindPressureCoefficientValues object
    must be the same as the number of wind directions specified for this
    AirflowNetwork:MultiZone:WindPressureCoefficientArray object."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:WindPressureCoefficientArray'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for the object.'}
    )
    wind_direction_1: float = Field(
        ...,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 1st WPC Array value.',
        },
    )
    wind_direction_2: float = Field(
        ...,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 2nd WPC Array value.',
        },
    )
    wind_direction_3: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 3rd WPC Array value.',
        },
    )
    wind_direction_4: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 4th WPC Array value.',
        },
    )
    wind_direction_5: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 5th WPC Array value.',
        },
    )
    wind_direction_6: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 6th WPC Array value.',
        },
    )
    wind_direction_7: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 7th WPC Array value.',
        },
    )
    wind_direction_8: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 8th WPC Array value.',
        },
    )
    wind_direction_9: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 9th WPC Array value.',
        },
    )
    wind_direction_10: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 10th WPC Array value.',
        },
    )
    wind_direction_11: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 11th WPC Array value.',
        },
    )
    wind_direction_12: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 12th WPC Array value.',
        },
    )
    wind_direction_13: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 13th WPC Array value.',
        },
    )
    wind_direction_14: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 14th WPC Array value.',
        },
    )
    wind_direction_15: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 15th WPC Array value.',
        },
    )
    wind_direction_16: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 16th WPC Array value.',
        },
    )
    wind_direction_17: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 17th WPC Array value.',
        },
    )
    wind_direction_18: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 18th WPC Array value.',
        },
    )
    wind_direction_19: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 19th WPC Array value.',
        },
    )
    wind_direction_20: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 20th WPC Array value.',
        },
    )
    wind_direction_21: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 21st WPC Array value.',
        },
    )
    wind_direction_22: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 22nd WPC Array value.',
        },
    )
    wind_direction_23: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 23rd WPC Array value.',
        },
    )
    wind_direction_24: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 24th WPC Array value.',
        },
    )
    wind_direction_25: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 25th WPC Array value.',
        },
    )
    wind_direction_26: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 26th WPC Array value.',
        },
    )
    wind_direction_27: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 27th WPC Array value.',
        },
    )
    wind_direction_28: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 28th WPC Array value.',
        },
    )
    wind_direction_29: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 29th WPC Array value.',
        },
    )
    wind_direction_30: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 30th WPC Array value.',
        },
    )
    wind_direction_31: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 31st WPC Array value.',
        },
    )
    wind_direction_32: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 32nd WPC Array value.',
        },
    )
    wind_direction_33: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 33rd WPC Array value.',
        },
    )
    wind_direction_34: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 34th WPC Array value.',
        },
    )
    wind_direction_35: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 35th WPC Array value.',
        },
    )
    wind_direction_36: float | None = Field(
        default=None,
        ge=0.0,
        le=360.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Enter the wind direction corresponding to the 36th WPC Array value.',
        },
    )


class AirflowNetworkMultiZoneWindPressureCoefficientValues(IDFBaseModel):
    """Used only if Wind Pressure Coefficient (WPC) Type = INPUT in the
    AirflowNetwork:SimulationControl object. The number of WPC numeric inputs
    must correspond to the number of wind direction inputs in the
    AirflowNetwork:Multizone:WindPressureCoefficientArray object."""

    _idf_object_type: ClassVar[str] = (
        'AirflowNetwork:MultiZone:WindPressureCoefficientValues'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    airflownetwork_multizone_windpressurecoefficientarray_name: WPCSetNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['WPCSetNames'],
            'note': 'Enter the name of the AirflowNetwork:Multizone:WindPressureCoefficientArray object.',
        },
    )
    wind_pressure_coefficient_value_1: float = Field(
        ...,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 1st wind direction.',
        },
    )
    wind_pressure_coefficient_value_2: float = Field(
        ...,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 2nd wind direction.',
        },
    )
    wind_pressure_coefficient_value_3: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 3rd wind direction.',
        },
    )
    wind_pressure_coefficient_value_4: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 4th wind direction.',
        },
    )
    wind_pressure_coefficient_value_5: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 5th wind direction.',
        },
    )
    wind_pressure_coefficient_value_6: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 6th wind direction.',
        },
    )
    wind_pressure_coefficient_value_7: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 7th wind direction.',
        },
    )
    wind_pressure_coefficient_value_8: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 8th wind direction.',
        },
    )
    wind_pressure_coefficient_value_9: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 9th wind direction.',
        },
    )
    wind_pressure_coefficient_value_10: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 10th wind direction.',
        },
    )
    wind_pressure_coefficient_value_11: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 11th wind direction.',
        },
    )
    wind_pressure_coefficient_value_12: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 12th wind direction.',
        },
    )
    wind_pressure_coefficient_value_13: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 13th wind direction.',
        },
    )
    wind_pressure_coefficient_value_14: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 14th wind direction.',
        },
    )
    wind_pressure_coefficient_value_15: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 15th wind direction.',
        },
    )
    wind_pressure_coefficient_value_16: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 16th wind direction.',
        },
    )
    wind_pressure_coefficient_value_17: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 17th wind direction.',
        },
    )
    wind_pressure_coefficient_value_18: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 18th wind direction.',
        },
    )
    wind_pressure_coefficient_value_19: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 19th wind direction.',
        },
    )
    wind_pressure_coefficient_value_20: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 20th wind direction.',
        },
    )
    wind_pressure_coefficient_value_21: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 21st wind direction.',
        },
    )
    wind_pressure_coefficient_value_22: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 22nd wind direction.',
        },
    )
    wind_pressure_coefficient_value_23: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 23rd wind direction.',
        },
    )
    wind_pressure_coefficient_value_24: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 24th wind direction.',
        },
    )
    wind_pressure_coefficient_value_25: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 25th wind direction.',
        },
    )
    wind_pressure_coefficient_value_26: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 26th wind direction.',
        },
    )
    wind_pressure_coefficient_value_27: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 27th wind direction.',
        },
    )
    wind_pressure_coefficient_value_28: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 28th wind direction.',
        },
    )
    wind_pressure_coefficient_value_29: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 29th wind direction.',
        },
    )
    wind_pressure_coefficient_value_30: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 30th wind direction.',
        },
    )
    wind_pressure_coefficient_value_31: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 31st wind direction.',
        },
    )
    wind_pressure_coefficient_value_32: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 32nd wind direction.',
        },
    )
    wind_pressure_coefficient_value_33: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 33rd wind direction.',
        },
    )
    wind_pressure_coefficient_value_34: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 34th wind direction.',
        },
    )
    wind_pressure_coefficient_value_35: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 35th wind direction.',
        },
    )
    wind_pressure_coefficient_value_36: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Enter the WPC Value corresponding to the 36th wind direction.',
        },
    )

    @property
    def airflownetwork_multizone_windpressurecoefficientarray(
        self,
    ) -> AirflowNetworkMultiZoneWindPressureCoefficientArray | None:
        v = self.airflownetwork_multizone_windpressurecoefficientarray_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WPCSetNames'])


class AirflowNetworkMultiZoneZone(IDFBaseModel):
    """This object is used to simultaneously control a thermal zone's window and
    door openings, both exterior and interior."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:MultiZone:Zone'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'zone_name'})
    zone_name: ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter the zone name where ventilation control is required.',
        },
    )
    ventilation_control_mode: (
        Literal[
            '',
            'ASHRAE55Adaptive',
            'CEN15251Adaptive',
            'Constant',
            'Enthalpy',
            'NoVent',
            'Temperature',
        ]
        | None
    ) = Field(
        default='NoVent',
        json_schema_extra={
            'note': "When Ventilation Control Mode = Temperature or Enthalpy, the following fields are used to modulate the Ventilation Open Factor for all window and door openings in the zone according to the zone's i..."
        },
    )
    ventilation_control_zone_temperature_setpoint_schedule_name: (
        ScheduleNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Used only if Ventilation Control Mode = Temperature or Enthalpy.',
        },
    )
    minimum_venting_open_factor: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Used only if Ventilation Control Mode = Temperature or Enthalpy.',
        },
    )
    indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        lt=100.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Applicable only if Ventilation Control Mode = Temperature. This value must be less than the corresponding upper value (next field).',
        },
    )
    indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor: (
        float | None
    ) = Field(
        default=100.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'Applicable only if Ventilation Control Mode = Temperature. This value must be greater than the corresponding lower value (previous field).',
        },
    )
    indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor: (
        float | None
    ) = Field(
        default=0.0,
        ge=0.0,
        lt=300000.0,
        json_schema_extra={
            'units': 'deltaJ/kg',
            'note': 'Applicable only if Ventilation Control Mode = Enthalpy. This value must be less than the corresponding upper value (next field).',
        },
    )
    indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor: (
        float | None
    ) = Field(
        default=300000.0,
        gt=0.0,
        json_schema_extra={
            'units': 'deltaJ/kg',
            'note': 'Applicable only if Ventilation Control Mode = Enthalpy. This value must be greater than the corresponding lower value (previous field).',
        },
    )
    venting_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Non-zero Schedule value means venting is allowed if other venting control conditions are satisfied. A zero (or negative) Schedule value means venting is not allowed under any The Schedule values sh...',
        },
    )
    single_sided_wind_pressure_coefficient_algorithm: (
        Literal['', 'Advanced', 'Standard'] | None
    ) = Field(
        default='Standard',
        json_schema_extra={
            'note': 'Selecting Advanced results in EnergyPlus calculating modified Wind Pressure Coefficients to account for wind direction and turbulence effects on single sided ventilation rates. Model is only valid ...'
        },
    )
    facade_width: float | None = Field(
        default=10.0,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This is the whole building width along the direction of the facade of this zone.',
        },
    )
    occupant_ventilation_control_name: (
        AirflowNetworkOccupantVentilationControlNamesRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AirflowNetworkOccupantVentilationControlNames'],
            'note': 'Enter the name where Occupancy Ventilation Control is required.',
        },
    )

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def ventilation_control_zone_temperature_setpoint_schedule(
        self,
    ) -> IDFBaseModel | None:
        v = self.ventilation_control_zone_temperature_setpoint_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def venting_availability_schedule(self) -> IDFBaseModel | None:
        v = self.venting_availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def occupant_ventilation_control(
        self,
    ) -> AirflowNetworkOccupantVentilationControl | None:
        v = self.occupant_ventilation_control_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['AirflowNetworkOccupantVentilationControlNames']
        )


class AirflowNetworkOccupantVentilationControl(IDFBaseModel):
    """This object is used to provide advanced thermal comfort control of window
    opening and closing for both exterior and interior windows."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:OccupantVentilationControl'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Enter the name where the advanced thermal comfort control is required.'
        },
    )
    minimum_opening_time: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'minutes'}
    )
    minimum_closing_time: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'minutes'}
    )
    thermal_comfort_low_temperature_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter a curve name that represents thermal comfort temperature as a function of outdoor dry-bulb temperature. Up to two curves are allowed if the performance cannot be represented by a single curve...',
        },
    )
    thermal_comfort_temperature_boundary_point: float | None = Field(
        default=10.0,
        ge=0.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This point is used to allow separate low and high thermal comfort temperature curves. If a single performance curve is used, leave this field blank.',
        },
    )
    thermal_comfort_high_temperature_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter a curve name that represents thermal comfort temperature as a function of outdoor dry-bulb temperature. Up to two curves are allowed if the performance cannot be represented by a single curve...',
        },
    )
    maximum_threshold_for_persons_dissatisfied_ppd: float | None = Field(
        default=10.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    occupancy_check: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'If Yes, occupancy check will be performed as part of the opening probability check.'
        },
    )
    opening_probability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If this field is blank, the opening probability check is bypassed and opening is true.',
        },
    )
    closing_probability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If this field is blank, the closing probability check is bypassed and closing is true.',
        },
    )

    @property
    def thermal_comfort_low_temperature_curve(self) -> IDFBaseModel | None:
        v = self.thermal_comfort_low_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def thermal_comfort_high_temperature_curve(self) -> IDFBaseModel | None:
        v = self.thermal_comfort_high_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def opening_probability_schedule(self) -> IDFBaseModel | None:
        v = self.opening_probability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def closing_probability_schedule(self) -> IDFBaseModel | None:
        v = self.closing_probability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class AirflowNetworkSimulationControl(IDFBaseModel):
    """This object defines the global parameters used in an Airflow Network
    simulation."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:SimulationControl'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ..., json_schema_extra={'note': 'Enter a unique name for this object.'}
    )
    airflownetwork_control: (
        Literal[
            '',
            'MultizoneWithDistribution',
            'MultizoneWithDistributionOnlyDuringFanOperation',
            'MultizoneWithoutDistribution',
            'NoMultizoneOrDistribution',
        ]
        | None
    ) = Field(
        default='NoMultizoneOrDistribution',
        json_schema_extra={
            'note': 'NoMultizoneOrDistribution: Only perform Simple calculations (objects ZoneInfiltration:*, ZoneVentilation:*, ZoneMixing, ZoneCrossMixing, ZoneRefrigerationDoorMixing, ZoneAirBalance:OutdoorAir, Zone...'
        },
    )
    wind_pressure_coefficient_type: (
        Literal['', 'Input', 'SurfaceAverageCalculation'] | None
    ) = Field(
        default='SurfaceAverageCalculation',
        json_schema_extra={
            'note': 'Input: User must enter AirflowNetwork:MultiZone:WindPressureCoefficientArray, AirflowNetwork:MultiZone:ExternalNode, and AirflowNetwork:MultiZone:WindPressureCoefficientValues objects. SurfaceAvera...'
        },
    )
    height_selection_for_local_wind_pressure_calculation: (
        Literal['', 'ExternalNode', 'OpeningHeight'] | None
    ) = Field(
        default='OpeningHeight',
        json_schema_extra={
            'note': 'If ExternalNode is selected, the height given in the AirflowNetwork:MultiZone:ExternalNode object will be used. If OpeningHeight is selected, the surface opening height (centroid) will be used to c...'
        },
    )
    building_type: Literal['', 'HighRise', 'LowRise'] | None = Field(
        default='LowRise',
        json_schema_extra={
            'note': 'Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation, otherwise this field may be left blank.'
        },
    )
    maximum_number_of_iterations: int | None = Field(
        default=500,
        le=30000,
        gt=10,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Determines the maximum number of iterations used to converge on a solution. If this limit is exceeded, the program terminates.',
        },
    )
    initialization_type: (
        Literal['', 'LinearInitializationMethod', 'ZeroNodePressures'] | None
    ) = Field(default='ZeroNodePressures')
    relative_airflow_convergence_tolerance: float | None = Field(
        default=0.0001,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'This tolerance is defined as the absolute value of the sum of the mass Flow Rates divided by the sum of the absolute value of the mass Flow Rates. The mass Flow Rates described here refer to the ma...',
        },
    )
    absolute_airflow_convergence_tolerance: float | None = Field(
        default=1e-06,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/s',
            'note': 'This tolerance is defined as the absolute value of the sum of the mass flow rates. The mass flow rates described here refer to the mass flow rates at all nodes in the AirflowNetwork model. The solu...',
        },
    )
    convergence_acceleration_limit: float | None = Field(
        default=-0.5,
        ge=-1.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Used only for AirflowNetwork:SimulationControl',
        },
    )
    azimuth_angle_of_long_axis_of_building: float | None = Field(
        default=0.0,
        ge=0.0,
        le=180.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Degrees clockwise from true North. Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.',
        },
    )
    ratio_of_building_width_along_short_axis_to_width_along_long_axis: float | None = (
        Field(
            default=1.0,
            le=1.0,
            gt=0.0,
            json_schema_extra={
                'note': 'Used only if Wind Pressure Coefficient Type = SurfaceAverageCalculation.'
            },
        )
    )
    height_dependence_of_external_node_temperature: Literal['', 'No', 'Yes'] | None = (
        Field(
            default='No',
            json_schema_extra={
                'note': 'If Yes, external node temperature is height dependent. If No, external node temperature is based on zero height.'
            },
        )
    )
    solver: Literal['', 'ConjugateGradient', 'SkylineLU'] | None = Field(
        default='SkylineLU',
        json_schema_extra={
            'note': 'Select the solver to use for the pressure network solution'
        },
    )
    allow_unsupported_zone_equipment: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Set this input to Yes to have zone equipment that are currently unsupported in the AirflowNetwork model allowed in the simulation if present. Setting this field to Yes, allows the following equipme...'
        },
    )
    do_distribution_duct_sizing_calculation: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Controls duct sizing. See AirflowNetwork:Distribution:DuctSizing for sizing options.'
        },
    )


class AirflowNetworkZoneControlPressureController(IDFBaseModel):
    """This object is used to control a zone to a specified indoor pressure using
    the AirflowNetwork model. The specified pressure setpoint is used to control
    the zone exhaust fan flow rate in a controlled zone or the relief air flow
    rate in an air loop."""

    _idf_object_type: ClassVar[str] = 'AirflowNetwork:ZoneControl:PressureController'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    control_zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    control_object_type: Literal[
        'AirflowNetwork:Distribution:Component:ReliefAirFlow',
        'AirflowNetwork:MultiZone:Component:ZoneExhaustFan',
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'The current selection is AirflowNetwork:MultiZone:Component:ZoneExhaustFan or AirflowNetwork:Distribution:Component:ReliefAirFlow.'
        },
    )
    control_object_name: AFNReliefAirFlowNamesRef | FansZoneExhaustRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['AFNReliefAirFlowNames', 'FansZoneExhaust'],
            'note': 'Control names are names of individual control objects',
        },
    )
    pressure_control_availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for pressure controller. Schedule value > 0 means the pressure controller is enabled. If this field is blank, then pressure controller is always enabled.',
        },
    )
    pressure_setpoint_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )

    @property
    def control_zone(self) -> Zone | None:
        v = self.control_zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def control_object(
        self,
    ) -> AirflowNetworkDistributionComponentReliefAirFlow | FanZoneExhaust | None:
        v = self.control_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AFNReliefAirFlowNames', 'FansZoneExhaust'])

    @property
    def pressure_control_availability_schedule(self) -> IDFBaseModel | None:
        v = self.pressure_control_availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def pressure_setpoint_schedule(self) -> IDFBaseModel | None:
        v = self.pressure_setpoint_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ComplianceBuilding(IDFBaseModel):
    """Building level inputs related to compliance to building standards, building
    codes, and beyond energy code programs."""

    _idf_object_type: ClassVar[str] = 'Compliance:Building'
    building_rotation_for_appendix_g: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'deg',
            'note': 'Additional degrees of rotation to be used with the requirement in ASHRAE Standard 90.1 Appendix G that states that the baseline building should be rotated in four directions.',
        },
    )


class CondenserLoop(IDFBaseModel):
    """Defines a central plant condenser loop. CondenserLoop and PlantLoop are
    nearly identical except some components and operation schemes are applicable
    to only one loop type or the other."""

    _idf_object_type: ClassVar[str] = 'CondenserLoop'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    fluid_type: Literal['', 'UserDefinedFluidType', 'Water'] | None = Field(
        default='Water'
    )
    user_defined_fluid_type: FluidAndGlycolNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidAndGlycolNames'],
            'note': 'This field is only required when Fluid Type is UserDefinedFluidType',
        },
    )
    condenser_equipment_operation_scheme_name: CondenserOperationSchemesRef = Field(
        ..., json_schema_extra={'object_list': ['CondenserOperationSchemes']}
    )
    condenser_loop_temperature_setpoint_node_name: str = Field(...)
    maximum_loop_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    minimum_loop_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    maximum_loop_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    minimum_loop_flow_rate: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm3/s'}
    )
    condenser_loop_volume: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate', json_schema_extra={'units': 'm3'}
    )
    condenser_side_inlet_node_name: str = Field(...)
    condenser_side_outlet_node_name: str = Field(...)
    condenser_side_branch_list_name: BranchListsRef = Field(
        ..., json_schema_extra={'object_list': ['BranchLists']}
    )
    condenser_side_connector_list_name: ConnectorListsRef = Field(
        ..., json_schema_extra={'object_list': ['ConnectorLists']}
    )
    demand_side_inlet_node_name: str = Field(...)
    demand_side_outlet_node_name: str = Field(...)
    condenser_demand_side_branch_list_name: BranchListsRef = Field(
        ..., json_schema_extra={'object_list': ['BranchLists']}
    )
    condenser_demand_side_connector_list_name: ConnectorListsRef = Field(
        ..., json_schema_extra={'object_list': ['ConnectorLists']}
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
    pressure_simulation_type: (
        Literal['', 'LoopFlowCorrection', 'None', 'PumpPowerCorrection'] | None
    ) = Field(default='None')
    loop_circulation_time: float | None = Field(
        default=2.0,
        ge=0.0,
        json_schema_extra={
            'units': 'minutes',
            'note': 'This field is only used to autocalculate the Condenser Loop Volume. Loop Volume = Loop Circulation Time * Maximum Loop Flow Rate',
        },
    )

    @property
    def user_defined_fluid_type_ref(
        self,
    ) -> FluidPropertiesGlycolConcentration | FluidPropertiesName | None:
        v = self.user_defined_fluid_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidAndGlycolNames'])

    @property
    def condenser_equipment_operation_scheme(
        self,
    ) -> CondenserEquipmentOperationSchemes | None:
        v = self.condenser_equipment_operation_scheme_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['CondenserOperationSchemes'])

    @property
    def condenser_side_branch_list(self) -> BranchList | None:
        v = self.condenser_side_branch_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BranchLists'])

    @property
    def condenser_side_connector_list(self) -> ConnectorList | None:
        v = self.condenser_side_connector_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ConnectorLists'])

    @property
    def condenser_demand_side_branch_list(self) -> BranchList | None:
        v = self.condenser_demand_side_branch_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BranchLists'])

    @property
    def condenser_demand_side_connector_list(self) -> ConnectorList | None:
        v = self.condenser_demand_side_connector_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ConnectorLists'])


class ControllerMechanicalVentilation(IDFBaseModel):
    """This object is used in conjunction with Controller:OutdoorAir to specify
    outdoor ventilation air based on outdoor air specified in the
    DesignSpecification:OutdoorAir object The Controller:OutdoorAir object is
    associated with a specific air loop, so the outdoor air flow rates specified
    in Controller:MechanicalVentilation correspond to the zones attached to that
    specific air loop. Duplicate groups of Zone name, Design Specification
    Outdoor Air Object Name, and Design Specification Zone Air Distribution
    Object Name to increase allowable number of entries"""

    _idf_object_type: ClassVar[str] = 'Controller:MechanicalVentilation'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'If this field is blank, the controller uses the values from the associated Controller:OutdoorAir. Schedule values greater than 0 indicate mechanical ventilation is enabled',
        },
    )
    demand_controlled_ventilation: Literal['', 'No', 'Yes'] | None = Field(default='No')
    system_outdoor_air_method: (
        Literal[
            '',
            'IndoorAirQualityProcedure',
            'IndoorAirQualityProcedureCombined',
            'IndoorAirQualityProcedureGenericContaminant',
            'ProportionalControlBasedOnDesignOARate',
            'ProportionalControlBasedOnDesignOccupancy',
            'ProportionalControlBasedOnOccupancySchedule',
            'Standard62.1VentilationRateProcedure',
            'Standard62.1VentilationRateProcedureWithLimit',
            'ZoneSum',
        ]
        | None
    ) = Field(default='Standard62.1VentilationRateProcedure')
    zone_maximum_outdoor_air_fraction: float | None = Field(
        default=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )
    zone_specifications: (
        list[ControllerMechanicalVentilationZoneSpecificationsItem] | None
    ) = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ControllerOutdoorAir(IDFBaseModel):
    """Controller to set the outdoor air flow rate for an air loop. Control options
    include fixed, proportional, scheduled, economizer, and demand-controlled
    ventilation."""

    _idf_object_type: ClassVar[str] = 'Controller:OutdoorAir'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    relief_air_outlet_node_name: str = Field(...)
    return_air_node_name: str = Field(...)
    mixed_air_node_name: str = Field(...)
    actuator_node_name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Outdoor air inlet node entering the first pre-treat component if any'
        },
    )
    minimum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ...,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'If there is a Mechanical Ventilation Controller (Controller:MechanicalVentilation), note that this value times the Minimum Outdoor Air Schedule is a hard minimum that may override DCV or other adva...',
        },
    )
    maximum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    economizer_control_type: (
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
    economizer_control_action_type: (
        Literal['', 'MinimumFlowWithBypass', 'ModulateFlow'] | None
    ) = Field(default='ModulateFlow')
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
    electronic_enthalpy_limit_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Enter the name of a quadratic or cubic curve which defines the maximum outdoor humidity ratio (function of outdoor dry-bulb temperature) for ElectronicEnthalpy economizer control type. No input or ...',
        },
    )
    economizer_minimum_limit_dry_bulb_temperature: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'Enter the minimum outdoor dry-bulb temperature limit for economizer control. No input or blank input means this limit is not operative Limit is applied regardless of economizer control type.',
        },
    )
    lockout_type: (
        Literal['', 'LockoutWithCompressor', 'LockoutWithHeating', 'NoLockout'] | None
    ) = Field(default='NoLockout')
    minimum_limit_type: Literal['', 'FixedMinimum', 'ProportionalMinimum'] | None = (
        Field(default='ProportionalMinimum')
    )
    minimum_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values multiply the minimum outdoor air flow rate',
        },
    )
    minimum_fraction_of_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'schedule values multiply the design/mixed air flow rate',
        },
    )
    maximum_fraction_of_outdoor_air_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'schedule values multiply the design/mixed air flow rate',
        },
    )
    mechanical_ventilation_controller_name: ControllerMechanicalVentNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ControllerMechanicalVentNames'],
                'note': 'Enter the name of a Controller:MechanicalVentilation object. Optional field for defining outdoor ventilation air based on flow rate per unit floor area and flow rate per person. Simplified method o...',
            },
        )
    )
    time_of_day_economizer_control_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Optional schedule to simulate "push-button" type economizer control. Schedule values greater than 0 indicate time-of-day economizer control is enabled. Economizer control may be used with or withou...',
        },
    )
    high_humidity_control: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Optional field to enable modified outdoor air flow rates based on zone relative humidity. Select Yes to modify outdoor air flow rate based on a zone humidistat. Select No to disable this feature. I...'
        },
    )
    humidistat_control_zone_name: ZoneNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ZoneNames'],
            'note': 'Enter the name of the zone where the humidistat is located. This field is only used when the field High Humidity Control = Yes.',
        },
    )
    high_humidity_outdoor_air_flow_ratio: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'Enter the ratio of outdoor air to the maximum outdoor air flow rate when modified air flow rates are active based on high indoor humidity. The minimum value must be greater than 0. This field is on...'
        },
    )
    control_high_indoor_humidity_based_on_outdoor_humidity_ratio: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='Yes',
        json_schema_extra={
            'note': 'If No is selected, the outdoor air flow rate is modified any time indoor relative humidity is above the humidistat setpoint. If Yes is selected, the outdoor air flow rate is modified any time the i...'
        },
    )
    heat_recovery_bypass_control_type: (
        Literal[
            '', 'BypassWhenOAFlowGreaterThanMinimum', 'BypassWhenWithinEconomizerLimits'
        ]
        | None
    ) = Field(
        default='BypassWhenWithinEconomizerLimits',
        json_schema_extra={
            'note': 'BypassWhenWithinEconomizerLimits specifies that heat recovery is active only when the economizer is off because conditions are outside the economizer control limits BypassWhenOAFlowGreaterThanMinim...'
        },
    )
    economizer_operation_staging: (
        Literal['', 'EconomizerFirst', 'InterlockedWithMechanicalCooling'] | None
    ) = Field(
        default='InterlockedWithMechanicalCooling',
        json_schema_extra={
            'note': 'This input is only used when the Controller:OutdoorAir is used in conjunction with an AirLoopHVAC:UnitarySystem with multiple cooling speeds. When modeling an AirLoopHVAC:UnitarySystem with multipl...'
        },
    )

    @property
    def electronic_enthalpy_limit_curve(self) -> IDFBaseModel | None:
        v = self.electronic_enthalpy_limit_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def minimum_outdoor_air_schedule(self) -> IDFBaseModel | None:
        v = self.minimum_outdoor_air_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def minimum_fraction_of_outdoor_air_schedule(self) -> IDFBaseModel | None:
        v = self.minimum_fraction_of_outdoor_air_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def maximum_fraction_of_outdoor_air_schedule(self) -> IDFBaseModel | None:
        v = self.maximum_fraction_of_outdoor_air_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def mechanical_ventilation_controller(
        self,
    ) -> ControllerMechanicalVentilation | None:
        v = self.mechanical_ventilation_controller_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ControllerMechanicalVentNames'])

    @property
    def time_of_day_economizer_control_schedule(self) -> IDFBaseModel | None:
        v = self.time_of_day_economizer_control_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def humidistat_control_zone(self) -> Zone | None:
        v = self.humidistat_control_zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])


class ControllerWaterCoil(IDFBaseModel):
    """Controller for a water coil which is located directly in an air loop branch
    or outdoor air equipment list. Controls the coil water flow to meet the
    specified leaving air setpoint(s). Used with Coil:Heating:Water,
    Coil:Cooling:Water, Coil:Cooling:Water:DetailedGeometry, and
    CoilSystem:Cooling:Water:HeatexchangerAssisted."""

    _idf_object_type: ClassVar[str] = 'Controller:WaterCoil'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    control_variable: Literal[
        'HumidityRatio', 'Temperature', 'TemperatureAndHumidityRatio'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'keys HumidityRatio or TemperatureAndHumidityRatio requires a ZoneControl:Humidistat object along with SetpointManager:SingleZone:Humidity:Maximum, SetpointManager:MultiZone:MaximumHumidity:Average,...'
        },
    )
    action: Literal['Normal', 'Reverse'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Leave blank to have this automatically selected from coil type. Chilled water coils should be reverse action Hot water coils should be normal action'
        },
    )
    actuator_variable: Literal['Flow'] = Field(...)
    sensor_node_name: str = Field(...)
    actuator_node_name: str = Field(...)
    controller_convergence_tolerance: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'deltaC'}
    )
    maximum_actuated_flow: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    minimum_actuated_flow: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )


class DehumidifierDesiccantNoFans(IDFBaseModel):
    """This object models a solid desiccant dehumidifier. The process air stream is
    the air which is dehumidified. The regeneration air stream is the air which
    is heated to regenerate the desiccant. This object determines the process
    air outlet conditions, the load on the regeneration heating coil, the
    electric power consumption for the wheel rotor motor, and the regeneration
    air fan mass flow rate. All other heat exchangers are modeled as separate
    objects connected to the inlet and outlet nodes of the dehumidifier. The
    solid desiccant dehumidifier is typically used in an
    AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC."""

    _idf_object_type: ClassVar[str] = 'Dehumidifier:Desiccant:NoFans'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    process_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This is the node entering the process side of the desiccant wheel.'
        },
    )
    process_air_outlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This is the node leaving the process side of the desiccant wheel.'
        },
    )
    regeneration_air_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'This is the node entering the regeneration side of the desiccant wheel after the regeneration coil.'
        },
    )
    regeneration_fan_inlet_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Node for air entering the regeneration fan, mass flow is set by the desiccant dehumidifier module.'
        },
    )
    control_type: (
        Literal[
            'LeavingMaximumHumidityRatioSetpoint',
            'SystemNodeMaximumHumidityRatioSetpoint',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Type of setpoint control: LeavingMaximumHumidityRatioSetpoint means that the unit is controlled to deliver air at the Leaving Max Humidity Ratio Setpoint (see below), SystemNodeMaximumHumidityRatio...'
        },
    )
    leaving_maximum_humidity_ratio_setpoint: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'kgWater/kgDryAir',
            'note': 'Fixed setpoint for maximum process air leaving humidity ratio Applicable only when Control Type = LeavingMaximumHumidityRatioSetpoint.',
        },
    )
    nominal_process_air_flow_rate: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Process air flow rate at nominal conditions',
        },
    )
    nominal_process_air_velocity: float | None = Field(
        default=None,
        le=6.0,
        gt=0.0,
        json_schema_extra={
            'units': 'm/s',
            'note': 'Process air velocity at nominal flow When using Performance Model Type of Default, must be 2.032 to 4.064 m/s (400 to 800 fpm)',
        },
    )
    rotor_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'W', 'note': 'Power input to wheel rotor motor'},
    )
    regeneration_coil_object_type: (
        Literal[
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'heating coil type works with gas, electric, hot water and steam heating coils'
        },
    )
    regeneration_coil_name: HeatingCoilNameRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['HeatingCoilName'],
            'note': 'Name of heating coil object for regeneration air',
        },
    )
    regeneration_fan_object_type: (
        Literal['Fan:ConstantVolume', 'Fan:SystemModel', 'Fan:VariableVolume'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Type of fan object for regeneration air. When using the Default Performance Model Type (see below), only Fan:VariableVolume or Fan:SystemModel are valid.'
        },
    )
    regeneration_fan_name: (FansCVandVAVRef | FansSystemModelRef) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FansCVandVAV', 'FansSystemModel'],
            'note': 'Name of fan object for regeneration air',
        },
    )
    performance_model_type: Literal['Default', 'UserCurves'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Specifies whether the default performance model or user-specified curves should be used to model the performance. The default model is a generic solid desiccant wheel using performance curves of th...'
        },
    )
    leaving_dry_bulb_function_of_entering_dry_bulb_and_humidity_ratio_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Leaving dry-bulb of process air as a function of entering dry-bulb and entering humidity ratio, biquadratic curve curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew edb = process enteri...',
        },
    )
    leaving_dry_bulb_function_of_air_velocity_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Leaving dry-bulb of process air as a function of air velocity, quadratic curve. curve = C1 + C2*v + C3*v**2 v = process air velocity [m/s]',
        },
    )
    leaving_humidity_ratio_function_of_entering_dry_bulb_and_humidity_ratio_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Leaving humidity ratio of process air as a function of entering dry-bulb and entering humidity ratio, biquadratic curve curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew edb = process ...',
        },
    )
    leaving_humidity_ratio_function_of_air_velocity_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Leaving humidity ratio of process air as a function of process air velocity, quadratic curve. curve = C1 + C2*v + C3*v**2 v = process air velocity [m/s]',
        },
    )
    regeneration_energy_function_of_entering_dry_bulb_and_humidity_ratio_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Regeneration energy [J/kg of water removed] as a function of entering dry-bulb and entering humidity ratio, biquadratic curve curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew edb = pr...',
        },
    )
    regeneration_energy_function_of_air_velocity_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Regeneration energy [J/kg of water removed] as a function of process air velocity, quadratic curve. curve = C1 + C2*v + C3*v**2 v = process air velocity [m/s]',
        },
    )
    regeneration_velocity_function_of_entering_dry_bulb_and_humidity_ratio_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'Regeneration velocity [m/s] as a function of entering dry-bulb and entering humidity ratio, biquadratic curve curve = C1 + C2*edb + C3*edb**2 + C4*ew + C5*ew**2 + C6*edb*ew edb = process entering d...',
        },
    )
    regeneration_velocity_function_of_air_velocity_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Regeneration velocity [m/s] as a function of process air velocity, quadratic curve. curve = C1 + C2*v + C3*v**2 v = process air velocity [m/s]',
        },
    )
    nominal_regeneration_temperature: float | None = Field(
        default=None,
        ge=40.0,
        le=250.0,
        json_schema_extra={
            'units': 'C',
            'note': 'Nominal regen temperature upon which the regen energy modifier curve is based. Not used if Default if chosen for the field Performance Mode Type. 121 C is a commonly used value.',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def regeneration_coil(
        self,
    ) -> (
        CoilHeatingElectric
        | CoilHeatingFuel
        | CoilHeatingSteam
        | CoilHeatingWater
        | None
    ):
        v = self.regeneration_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatingCoilName'])

    @property
    def regeneration_fan(
        self,
    ) -> FanConstantVolume | FanSystemModel | FanVariableVolume | None:
        v = self.regeneration_fan_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FansCVandVAV', 'FansSystemModel'])

    @property
    def leaving_dry_bulb_function_of_entering_dry_bulb_and_humidity_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.leaving_dry_bulb_function_of_entering_dry_bulb_and_humidity_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def leaving_dry_bulb_function_of_air_velocity_curve(self) -> IDFBaseModel | None:
        v = self.leaving_dry_bulb_function_of_air_velocity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def leaving_humidity_ratio_function_of_entering_dry_bulb_and_humidity_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.leaving_humidity_ratio_function_of_entering_dry_bulb_and_humidity_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def leaving_humidity_ratio_function_of_air_velocity_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.leaving_humidity_ratio_function_of_air_velocity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def regeneration_energy_function_of_entering_dry_bulb_and_humidity_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.regeneration_energy_function_of_entering_dry_bulb_and_humidity_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def regeneration_energy_function_of_air_velocity_curve(self) -> IDFBaseModel | None:
        v = self.regeneration_energy_function_of_air_velocity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def regeneration_velocity_function_of_entering_dry_bulb_and_humidity_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.regeneration_velocity_function_of_entering_dry_bulb_and_humidity_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def regeneration_velocity_function_of_air_velocity_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.regeneration_velocity_function_of_air_velocity_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class DehumidifierDesiccantSystem(IDFBaseModel):
    """This compound object models a desiccant heat exchanger, an optional heater,
    and associated fans. The process air stream is the air which is
    dehumidified. The regeneration air stream is the air which is heated to
    regenerate the desiccant. The desiccant heat exchanger transfers both
    sensible and latent energy between the process and regeneration air streams.
    The desiccant dehumidifier is typically used in an
    AirLoopHVAC:OutdoorAirSystem, but can also be specified in any AirLoopHVAC."""

    _idf_object_type: ClassVar[str] = 'Dehumidifier:Desiccant:System'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    desiccant_heat_exchanger_object_type: Literal[
        'HeatExchanger:Desiccant:BalancedFlow'
    ] = Field(...)
    desiccant_heat_exchanger_name: HXDesiccantBalancedRef = Field(
        ..., json_schema_extra={'object_list': ['HXDesiccantBalanced']}
    )
    sensor_node_name: str = Field(...)
    regeneration_air_fan_object_type: Literal[
        'Fan:ConstantVolume', 'Fan:OnOff', 'Fan:SystemModel'
    ] = Field(...)
    regeneration_air_fan_name: FansOnOffandVAVRef | FansSystemModelRef = Field(
        ..., json_schema_extra={'object_list': ['FansOnOffandVAV', 'FansSystemModel']}
    )
    regeneration_air_fan_placement: Literal['', 'BlowThrough', 'DrawThrough'] | None = (
        Field(default='DrawThrough')
    )
    regeneration_air_heater_object_type: (
        Literal[
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'works with gas, electric, hot water and steam heating coils. For autosizing the regeneration air heating coil the Design Coil Inlet Air Condition used is the outdoor air condition if the desiccant ...'
        },
    )
    regeneration_air_heater_name: HeatingCoilNameRef | None = Field(
        default=None, json_schema_extra={'object_list': ['HeatingCoilName']}
    )
    regeneration_inlet_air_setpoint_temperature: float | None = Field(
        default=46.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This value is also used as regeneration air heater design coil air outlet temperature for autosizing calculation of the heater.',
        },
    )
    companion_cooling_coil_object_type: (
        Literal[
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'Coil:Cooling:DX:VariableSpeed',
        ]
        | None
    ) = Field(default=None)
    companion_cooling_coil_name: (
        CoolingCoilsDXMultiModeOrSingleSpeedRef | CoolingCoilsDXVariableSpeedRef
    ) | None = Field(
        default=None,
        json_schema_extra={
            'object_list': [
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'CoolingCoilsDXVariableSpeed',
            ]
        },
    )
    companion_cooling_coil_upstream_of_dehumidifier_process_inlet: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(
        default='No',
        json_schema_extra={
            'note': "Select Yes if the companion cooling coil is located directly upstream of the desiccant heat exchanger's process air inlet node."
        },
    )
    companion_coil_regeneration_air_heating: Literal['', 'No', 'Yes'] | None = Field(
        default='No'
    )
    exhaust_fan_maximum_flow_rate: float | None = Field(
        default=None, json_schema_extra={'units': 'm3/s'}
    )
    exhaust_fan_maximum_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    exhaust_fan_power_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Curve object type must be Curve:Quadratic or Curve:Cubic',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def desiccant_heat_exchanger(self) -> HeatExchangerDesiccantBalancedFlow | None:
        v = self.desiccant_heat_exchanger_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HXDesiccantBalanced'])

    @property
    def regeneration_air_fan(self) -> FanOnOff | FanSystemModel | None:
        v = self.regeneration_air_fan_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FansOnOffandVAV', 'FansSystemModel'])

    @property
    def regeneration_air_heater(
        self,
    ) -> (
        CoilHeatingElectric
        | CoilHeatingFuel
        | CoilHeatingSteam
        | CoilHeatingWater
        | None
    ):
        v = self.regeneration_air_heater_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['HeatingCoilName'])

    @property
    def companion_cooling_coil(
        self,
    ) -> (
        CoilCoolingDXSingleSpeed
        | CoilCoolingDXTwoStageWithHumidityControlMode
        | CoilCoolingDXVariableSpeed
        | None
    ):
        v = self.companion_cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['CoolingCoilsDXMultiModeOrSingleSpeed', 'CoolingCoilsDXVariableSpeed']
        )

    @property
    def exhaust_fan_power_curve(self) -> IDFBaseModel | None:
        v = self.exhaust_fan_power_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class DuctLossConduction(IDFBaseModel):
    """Duct:Loss:Conduction"""

    _idf_object_type: ClassVar[str] = 'Duct:Loss:Conduction'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    airloophvac_name: AirPrimaryLoopsRef = Field(
        ..., json_schema_extra={'object_list': ['AirPrimaryLoops']}
    )
    airflownetwork_distribution_linkage_name: AirflowNetworkDistributionLinkageNamesRef = Field(
        ...,
        json_schema_extra={'object_list': ['AirflowNetworkDistributionLinkageNames']},
    )
    environment_type: Literal['', 'Schedule', 'Zone'] | None = Field(default='Zone')
    ambient_zone_name: ZoneNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ZoneNames']}
    )
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    ambient_humidity_ratio_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )

    @property
    def airloophvac(self) -> AirLoopHVAC | None:
        v = self.airloophvac_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirPrimaryLoops'])

    @property
    def airflownetwork_distribution_linkage(
        self,
    ) -> AirflowNetworkDistributionLinkage | None:
        v = self.airflownetwork_distribution_linkage_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkDistributionLinkageNames'])

    @property
    def ambient_zone(self) -> Zone | None:
        v = self.ambient_zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def ambient_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.ambient_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def ambient_humidity_ratio_schedule(self) -> IDFBaseModel | None:
        v = self.ambient_humidity_ratio_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class DuctLossLeakage(IDFBaseModel):
    """Duct:Loss:Leakage"""

    _idf_object_type: ClassVar[str] = 'Duct:Loss:Leakage'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    airloophvac_name: AirPrimaryLoopsRef = Field(
        ..., json_schema_extra={'object_list': ['AirPrimaryLoops']}
    )
    airflownetwork_distribution_linkage_name: AirflowNetworkDistributionLinkageNamesRef = Field(
        ...,
        json_schema_extra={'object_list': ['AirflowNetworkDistributionLinkageNames']},
    )

    @property
    def airloophvac(self) -> AirLoopHVAC | None:
        v = self.airloophvac_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirPrimaryLoops'])

    @property
    def airflownetwork_distribution_linkage(
        self,
    ) -> AirflowNetworkDistributionLinkage | None:
        v = self.airflownetwork_distribution_linkage_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkDistributionLinkageNames'])


class DuctLossMakeupAir(IDFBaseModel):
    """Duct:Loss:MakeupAir"""

    _idf_object_type: ClassVar[str] = 'Duct:Loss:MakeupAir'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    airloophvac_name: AirPrimaryLoopsRef = Field(
        ..., json_schema_extra={'object_list': ['AirPrimaryLoops']}
    )
    airflownetwork_distribution_linkage_name: AirflowNetworkDistributionLinkageNamesRef = Field(
        ...,
        json_schema_extra={'object_list': ['AirflowNetworkDistributionLinkageNames']},
    )

    @property
    def airloophvac(self) -> AirLoopHVAC | None:
        v = self.airloophvac_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirPrimaryLoops'])

    @property
    def airflownetwork_distribution_linkage(
        self,
    ) -> AirflowNetworkDistributionLinkage | None:
        v = self.airflownetwork_distribution_linkage_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AirflowNetworkDistributionLinkageNames'])


class ExteriorFuelEquipment(IDFBaseModel):
    """only used for Meter type reporting, does not affect building loads"""

    _idf_object_type: ClassVar[str] = 'Exterior:FuelEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    fuel_use_type: Literal[
        'Coal',
        'Diesel',
        'DistrictCooling',
        'DistrictHeatingSteam',
        'DistrictHeatingWater',
        'Electricity',
        'FuelOilNo1',
        'FuelOilNo2',
        'Gasoline',
        'NaturalGas',
        'OtherFuel1',
        'OtherFuel2',
        'Propane',
        'Water',
    ] = Field(...)
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to capacity of the exterior fuel equipment, generally (0.0 - 1.0)',
        },
    )
    design_level: float = Field(..., ge=0.0, json_schema_extra={'units': 'W'})
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ExteriorLights(IDFBaseModel):
    """only used for Meter type reporting, does not affect building loads"""

    _idf_object_type: ClassVar[str] = 'Exterior:Lights'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to capacity of the exterior lights equipment, generally (0.0 - 1.0)',
        },
    )
    design_level: float = Field(..., ge=0.0, json_schema_extra={'units': 'W'})
    control_option: Literal['AstronomicalClock', 'ScheduleNameOnly'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Astronomical Clock option overrides schedule to turn lights off when sun is up'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ExteriorWaterEquipment(IDFBaseModel):
    """only used for Meter type reporting, does not affect building loads"""

    _idf_object_type: ClassVar[str] = 'Exterior:WaterEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    fuel_use_type: Literal['', 'Water'] | None = Field(default='Water')
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to capacity of the exterior water equipment, generally (0.0 - 1.0)',
        },
    )
    design_level: float = Field(..., ge=0.0, json_schema_extra={'units': 'm3/s'})
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class GroundHeatTransferBasementAutoGrid(IDFBaseModel):
    """AutoGrid only necessary when EquivSizing is false If the modeled building is
    not a rectangle or square, Equivalent sizing MUST be used to get accurate
    results"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:AutoGrid'
    clearance_distance_from_outside_of_wall_to_edge: float | None = Field(
        default=15.0,
        validation_alias='clearance_distance_from_outside_of_wall_to_edge_',
        ge=0.0,
        json_schema_extra={'units': 'm'},
    )
    slabx_x_dimension_of_the_building_slab: float = Field(
        ..., ge=0.0, le=60.0, json_schema_extra={'units': 'm'}
    )
    slaby_y_dimension_of_the_building_slab: float = Field(
        ..., ge=0.0, le=60.0, json_schema_extra={'units': 'm'}
    )
    concagheight_height_of_the_foundation_wall_above_grade: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'm'}
    )
    slabdepth_thickness_of_the_floor_slab: float | None = Field(
        default=0.1, json_schema_extra={'units': 'm'}
    )
    basedepth_depth_of_the_basement_wall_below_grade: float | None = Field(
        default=2.0, ge=0.0, json_schema_extra={'units': 'm'}
    )


class GroundHeatTransferBasementBldgData(IDFBaseModel):
    """Specifies the surface and gravel thicknesses used for the Basement
    preprocessor ground heat transfer simulation."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:BldgData'
    dwall_wall_thickness: float | None = Field(
        default=0.2, ge=0.2, json_schema_extra={'units': 'm'}
    )
    dslab_floor_slab_thickness: float | None = Field(
        default=0.1, le=0.25, gt=0.0, json_schema_extra={'units': 'm'}
    )
    dgravxy_width_of_gravel_pit_beside_basement_wall: float | None = Field(
        default=0.3, gt=0.0, json_schema_extra={'units': 'm'}
    )
    dgravzn_gravel_depth_extending_above_the_floor_slab: float | None = Field(
        default=0.2, gt=0.0, json_schema_extra={'units': 'm'}
    )
    dgravzp_gravel_depth_below_the_floor_slab: float | None = Field(
        default=0.1, gt=0.0, json_schema_extra={'units': 'm'}
    )


class GroundHeatTransferBasementComBldg(IDFBaseModel):
    """ComBldg contains the monthly average temperatures (C) and possibility of
    daily variation amplitude"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:ComBldg'
    january_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    february_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    march_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    april_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    may_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    june_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    july_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    august_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    september_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    october_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    november_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    december_average_temperature: float | None = Field(
        default=22.0, json_schema_extra={'units': 'C'}
    )
    daily_variation_sine_wave_amplitude: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': '(Normally zero, just for checking)',
        },
    )


class GroundHeatTransferBasementEquivAutoGrid(IDFBaseModel):
    """EquivAutoGrid necessary when EquivSizing=TRUE, TRUE is is the normal case."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:EquivAutoGrid'
    clearance_distance_from_outside_of_wall_to_edge_of_3_d_ground_domain: (
        float | None
    ) = Field(default=15.0, ge=0.0, json_schema_extra={'units': 'm'})
    slabdepth_thickness_of_the_floor_slab: float | None = Field(
        default=0.1, ge=0.0, json_schema_extra={'units': 'm'}
    )
    basedepth_depth_of_the_basement_wall_below_grade: float | None = Field(
        default=2.0, ge=0.0, json_schema_extra={'units': 'm'}
    )


class GroundHeatTransferBasementEquivSlab(IDFBaseModel):
    """Using an equivalent slab allows non-rectangular shapes to be modeled
    accurately. The simulation default should be EquivSizing=True"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:EquivSlab'
    apratio_the_area_to_perimeter_ratio_for_this_slab: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm'}
    )
    equivsizing_flag: Literal['FALSE', 'TRUE'] = Field(
        ...,
        json_schema_extra={
            'note': 'Will the dimensions of an equivalent slab be calculated (TRUE) or will the dimensions be input directly? (FALSE)] Only advanced special simulations should use FALSE.'
        },
    )


class GroundHeatTransferBasementInsulation(IDFBaseModel):
    """Describes the insulation used on an exterior basement wall for the Basement
    preprocessor ground heat transfer simulation."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:Insulation'
    rext_r_value_of_any_exterior_insulation: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'm2-K/W'}
    )
    insfull_flag_is_the_wall_fully_insulated: Literal['FALSE', 'TRUE'] = Field(
        ...,
        validation_alias='insfull_flag_is_the_wall_fully_insulated_',
        json_schema_extra={
            'note': 'True for full insulation False for insulation half way down side wall from grade line'
        },
    )


class GroundHeatTransferBasementInterior(IDFBaseModel):
    """Provides the information needed to simulate the inside boundary conditions
    for the Basement preprocessor ground heat transfer simulation."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:Interior'
    cond_flag_is_the_basement_conditioned: Literal['', 'FALSE', 'TRUE'] | None = Field(
        default='TRUE',
        validation_alias='cond_flag_is_the_basement_conditioned_',
        json_schema_extra={'note': 'for EnergyPlus this should be TRUE'},
    )
    hin_downward_convection_only_heat_transfer_coefficient: float | None = Field(
        default=0.92, gt=0.0, json_schema_extra={'units': 'W/m2-K'}
    )
    hin_upward_convection_only_heat_transfer_coefficient: float | None = Field(
        default=4.04, gt=0.0, json_schema_extra={'units': 'W/m2-K'}
    )
    hin_horizontal_convection_only_heat_transfer_coefficient: float | None = Field(
        default=3.08, gt=0.0, json_schema_extra={'units': 'W/m2-K'}
    )
    hin_downward_combined_convection_and_radiation_heat_transfer_coefficient: (
        float | None
    ) = Field(default=6.13, gt=0.0, json_schema_extra={'units': 'W/m2-K'})
    hin_upward_combined_convection_and_radiation_heat_transfer_coefficient: (
        float | None
    ) = Field(default=9.26, gt=0.0, json_schema_extra={'units': 'W/m2-K'})
    hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient: (
        float | None
    ) = Field(default=8.29, gt=0.0, json_schema_extra={'units': 'W/m2-K'})


class GroundHeatTransferBasementManualGrid(IDFBaseModel):
    """Manual Grid only necessary using manual gridding (not recommended)"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:ManualGrid'
    nx_number_of_cells_in_the_x_direction_20: float = Field(
        ..., validation_alias='nx_number_of_cells_in_the_x_direction_20_', ge=1.0
    )
    ny_number_of_cells_in_the_y_direction_20: float = Field(
        ..., validation_alias='ny_number_of_cells_in_the_y_direction_20_', ge=1.0
    )
    nzag_number_of_cells_in_the_z_direction_above_grade_4_always: float = Field(
        ...,
        validation_alias='nzag_number_of_cells_in_the_z_direction_above_grade_4_always_',
        ge=1.0,
    )
    nzbg_number_of_cells_in_z_direction_below_grade_10_35: float = Field(
        ...,
        validation_alias='nzbg_number_of_cells_in_z_direction_below_grade_10_35_',
        ge=1.0,
    )
    ibase_x_direction_cell_indicator_of_slab_edge_5_20: float = Field(
        ..., validation_alias='ibase_x_direction_cell_indicator_of_slab_edge_5_20_'
    )
    jbase_y_direction_cell_indicator_of_slab_edge_5_20: float = Field(
        ..., validation_alias='jbase_y_direction_cell_indicator_of_slab_edge_5_20_'
    )
    kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_5_20: float = Field(
        ...,
        validation_alias='kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_5_20_',
    )


class GroundHeatTransferBasementMatlProps(IDFBaseModel):
    """Specifies the material properties for the Basement preprocessor ground heat
    transfer simulation. Only the Foundation Wall, Floor Slab, Soil, and Gravel
    properties are currently used."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:MatlProps'
    nmat_number_of_materials_in_this_domain: float = Field(..., le=6.0)
    density_for_foundation_wall: float | None = Field(
        default=2243.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    density_for_floor_slab: float | None = Field(
        default=2243.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    density_for_ceiling: float | None = Field(
        default=311.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    density_for_soil: float | None = Field(
        default=1500.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    density_for_gravel: float | None = Field(
        default=2000.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    density_for_wood: float | None = Field(
        default=449.0, gt=0.0, json_schema_extra={'units': 'kg/m3'}
    )
    specific_heat_for_foundation_wall: float | None = Field(
        default=880.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    specific_heat_for_floor_slab: float | None = Field(
        default=880.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    specific_heat_for_ceiling: float | None = Field(
        default=1530.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    specific_heat_for_soil: float | None = Field(
        default=840.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    specific_heat_for_gravel: float | None = Field(
        default=720.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    specific_heat_for_wood: float | None = Field(
        default=1530.0, gt=0.0, json_schema_extra={'units': 'J/kg-K'}
    )
    thermal_conductivity_for_foundation_wall: float | None = Field(
        default=1.4, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    thermal_conductivity_for_floor_slab: float | None = Field(
        default=1.4, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    thermal_conductivity_for_ceiling: float | None = Field(
        default=0.09, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    thermal_conductivity_for_soil: float | None = Field(
        default=1.1, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    thermal_conductivity_for_gravel: float | None = Field(
        default=1.9, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )
    thermal_conductivity_for_wood: float | None = Field(
        default=0.12, gt=0.0, json_schema_extra={'units': 'W/m-K'}
    )


class GroundHeatTransferBasementSimParameters(IDFBaseModel):
    """Specifies certain parameters that control the Basement preprocessor ground
    heat transfer simulation."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:SimParameters'
    f_multiplier_for_the_adi_solution: float | None = Field(
        default=None,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': '0<F<1.0, typically 0.1 (0.3 for high k soil - saturated sand is about 2.6 w/m-K)'
        },
    )
    iyrs_maximum_number_of_yearly_iterations: float | None = Field(
        default=15.0,
        validation_alias='iyrs_maximum_number_of_yearly_iterations_',
        ge=0.0,
        json_schema_extra={'note': 'typically 15-30]'},
    )


class GroundHeatTransferBasementSurfaceProps(IDFBaseModel):
    """Specifies the soil surface properties for the Basement preprocessor ground
    heat transfer simulation."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:SurfaceProps'
    albedo_surface_albedo_for_no_snow_conditions: float | None = Field(
        default=0.16, ge=0.0, le=1.0
    )
    albedo_surface_albedo_for_snow_conditions: float | None = Field(
        default=0.4, ge=0.0, le=1.0
    )
    epsln_surface_emissivity_no_snow: float | None = Field(default=0.94, ge=0.0, le=1.0)
    epsln_surface_emissivity_with_snow: float | None = Field(
        default=0.86, ge=0.0, le=1.0
    )
    veght_surface_roughness_no_snow_conditions: float | None = Field(
        default=6.0, ge=0.0, json_schema_extra={'units': 'cm'}
    )
    veght_surface_roughness_snow_conditions: float | None = Field(
        default=0.25, ge=0.0, json_schema_extra={'units': 'cm'}
    )
    pet_flag_potential_evapotranspiration_on: Literal['', 'FALSE', 'TRUE'] | None = (
        Field(
            default='FALSE',
            validation_alias='pet_flag_potential_evapotranspiration_on_',
            json_schema_extra={'note': 'Typically, PET is False'},
        )
    )


class GroundHeatTransferBasementXFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) XFACE: X
    Direction cell face coordinates: m"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:XFACE'


class GroundHeatTransferBasementYFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) YFACE: Y
    Direction cell face coordinates: m"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:YFACE'


class GroundHeatTransferBasementZFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) ZFACE: Z
    Direction cell face coordinates: m"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Basement:ZFACE'


class GroundHeatTransferControl(IDFBaseModel):
    """Object determines if the Slab and Basement preprocessors are going to be
    executed."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Control'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str | None = Field(
        default=None,
        json_schema_extra={'note': 'This field is included for consistency.11'},
    )
    run_basement_preprocessor: Literal['', 'No', 'Yes'] | None = Field(default='No')
    run_slab_preprocessor: Literal['', 'No', 'Yes'] | None = Field(default='No')


class GroundHeatTransferSlabAutoGrid(IDFBaseModel):
    """AutoGrid only necessary when EquivalentSlab option not chosen. Not normally
    needed by EnergyPlus users. This object permits user selection of
    rectangular slab dimensions. NO SLAB DIMENSIONS LESS THAN 6 m."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:AutoGrid'
    slabx_x_dimension_of_the_building_slab: float = Field(
        ...,
        ge=6.0,
        json_schema_extra={'units': 'm', 'note': 'typical values= 6 to 60.0'},
    )
    slaby_y_dimension_of_the_building_slab: float = Field(
        ...,
        ge=6.0,
        json_schema_extra={'units': 'm', 'note': 'typical values= 6 to 60.0'},
    )
    slabdepth_thickness_of_slab_on_grade: float | None = Field(
        default=0.1, json_schema_extra={'units': 'm'}
    )
    clearance_distance_from_edge_of_slab_to_domain_edge: float | None = Field(
        default=15.0, json_schema_extra={'units': 'm'}
    )
    zclearance_distance_from_bottom_of_slab_to_domain_bottom: float | None = Field(
        default=15.0, json_schema_extra={'units': 'm'}
    )


class GroundHeatTransferSlabBldgProps(IDFBaseModel):
    """Object provides information about the building and its operating conditions
    Monthly Average Temperature SetPoint fields specify the average indoor
    building set point temperatures for each month of the year. These fields are
    useful for simulating a building that is not temperature controlled for some
    of the year. In such a case, the average indoor set point temperatures can
    be obtained by first running the model in EnergyPlus with an insulated floor
    boundary condition, and then using the resulting monthly average zone
    temperatures in these fields."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:BldgProps'
    iyrs_number_of_years_to_iterate: float | None = Field(
        default=10.0,
        ge=1.0,
        json_schema_extra={
            'note': 'This field specifies the number of years to iterate. Either the ground heat transfer calculations come to an an annual steady periodic condition by converging to a tolerance (see ConvTol field) or ...'
        },
    )
    shape_slab_shape: float | None = Field(
        default=None,
        ge=0.0,
        le=0.0,
        json_schema_extra={
            'note': 'Use only the value 0 here. Only a rectangular shape is implemented.'
        },
    )
    hbldg_building_height: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field supplies the building height. This is used to calculate the building shadowing on the ground. typical value= 0-20',
        },
    )
    tin1_january_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin2_february_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin3_march_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin4_april_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin5_may_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin6_june_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin7_july_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin8_august_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin9_september_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin10_october_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin11_november_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tin12_december_indoor_average_temperature_setpoint: float | None = Field(
        default=22.0,
        json_schema_extra={
            'units': 'C',
            'note': 'see memo on object for more information',
        },
    )
    tinamp_daily_indoor_sine_wave_variation_amplitude: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'This field permits imposing a daily sinusoidal variation in the indoor setpoint temperature to simulate the effect of a setback profile. The value specified is the amplitude of the sine wave.',
        },
    )
    convtol_convergence_tolerance: float | None = Field(
        default=0.1,
        json_schema_extra={
            'note': 'This field specifies the convergence tolerance used to control the iteration. When the temperature change of all nodes is less than the convergence value, iteration ceases.'
        },
    )


class GroundHeatTransferSlabBoundConds(IDFBaseModel):
    """Supplies some of the boundary conditions used in the ground heat transfer
    calculations."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:BoundConds'
    evtr_is_surface_evapotranspiration_modeled: Literal['FALSE', 'TRUE'] = Field(
        ...,
        json_schema_extra={
            'note': 'This field specifies whether or not to use the evapotranspiration model. The inclusion of evapotranspiration in the calculation has the greatest effect in warm dry climates, primarily on the ground...'
        },
    )
    fixbc_is_the_lower_boundary_at_a_fixed_temperature: Literal['FALSE', 'TRUE'] = (
        Field(
            ...,
            json_schema_extra={
                'note': 'This field permits using a fixed temperature at the lower surface of the model instead of a zero heat flux condition. This change normally has a very small effect on the results. FALSE selects the ...'
            },
        )
    )
    tdeepin: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'C',
            'note': 'User input lower boundary temperature if FIXBC is TRUE Blank for FIXBC FALSE or to use the calculated 1-D deep ground temperature.',
        },
    )
    usrhflag_is_the_ground_surface_h_specified_by_the_user: Literal['FALSE', 'TRUE'] = (
        Field(
            ...,
            validation_alias='usrhflag_is_the_ground_surface_h_specified_by_the_user_',
            json_schema_extra={
                'note': 'This field flags the use of a user specified heat transfer coefficient on the ground surface. This condition is used primarily for testing. For normal runs (USPHflag is FALSE) and the program calcu...'
            },
        )
    )
    userh_user_specified_ground_surface_heat_transfer_coefficient: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'Used only if USRHflag is TRUE and the heat transfer coefficient value is specified in this field.',
        },
    )


class GroundHeatTransferSlabEquivalentSlab(IDFBaseModel):
    """Using an equivalent slab allows non-rectangular shapes to be modeled
    accurately. Object uses the area - perimeter (area/perimeter) ratio to
    determine the size of an equivalent rectangular slab. EnergyPlus users
    normally use this option."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:EquivalentSlab'
    apratio_the_area_to_perimeter_ratio_for_this_slab: float = Field(
        ...,
        ge=1.5,
        le=22.0,
        json_schema_extra={
            'units': 'm',
            'note': 'Equivalent square slab is simulated,  side is 4*APRatio.',
        },
    )
    slabdepth_thickness_of_slab_on_grade: float | None = Field(
        default=0.1,
        json_schema_extra={
            'units': 'm',
            'note': 'This field specifies the thickness of the slab. The slab top surface is level with the ground surface, so this is the depth into the ground. The slab depth has a significant effect on the temperatu...',
        },
    )
    clearance_distance_from_edge_of_slab_to_domain_edge: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field specifies the distance from the slab to the edge of the area that will be modeled with the grid system. It is the basic size dimension that is used to set the horizontal extent of the do...',
        },
    )
    zclearance_distance_from_bottom_of_slab_to_domain_bottom: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field specifies the vertical distance from the slab to the bottom edge of the area that will be modeled with the grid system. 15 meters is a reasonable value.',
        },
    )


class GroundHeatTransferSlabInsulation(IDFBaseModel):
    """This object supplies the information about insulation used around the slab.
    There are two possible configurations: under the slab or vertical insulation
    around the slab."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:Insulation'
    rins_r_value_of_under_slab_insulation: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm2-K/W',
            'note': 'This field provides the thermal resistance value of the under slab insulation. It should be zero if the vertical insulation configuration is selected. typical value= 0-2.0',
        },
    )
    dins_width_of_strip_of_under_slab_insulation: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This specifies the width of the perimeter strip of insulation under the slab. It should be zero if for the vertical insulation configuration is selected. typical value= 0-2.0',
        },
    )
    rvins_r_value_of_vertical_insulation: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm2-K/W',
            'note': 'This field specifies the thermal resistance of the vertical insulation. It should be zero if the under slab insulation configuration is selected. typical value= 0-3.0',
        },
    )
    zvins_depth_of_vertical_insulation: float | None = Field(
        default=0.0,
        json_schema_extra={
            'units': 'm',
            'note': 'This field specifies the depth of the vertical insulation into the ground in meters. It starts at the slab upper surface and extends into the ground. It should be zero if the under slab insulation ...',
        },
    )
    ivins_flag_is_there_vertical_insulation: Literal[0, 1] | Literal[''] | None = Field(
        default=0,
        json_schema_extra={
            'note': 'Specifies if the vertical insulation configuration is being used. values: 1=yes vertical insulation 0=no under-slab insulation'
        },
    )


class GroundHeatTransferSlabManualGrid(IDFBaseModel):
    """Manual Grid only necessary when using manual gridding (not recommended) Used
    only in special cases when previous two objects are not used. User must
    input complete gridding information."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:ManualGrid'
    nx_number_of_cells_in_the_x_direction: float = Field(..., ge=1.0)
    ny_number_of_cells_in_the_y_direction: float = Field(..., ge=1.0)
    nz_number_of_cells_in_the_z_direction: float = Field(..., ge=1.0)
    ibox_x_direction_cell_indicator_of_slab_edge: float = Field(
        ..., json_schema_extra={'note': 'typical values= 1-10'}
    )
    jbox_y_direction_cell_indicator_of_slab_edge: float = Field(
        ..., json_schema_extra={'note': 'typical values= 1-10'}
    )


class GroundHeatTransferSlabMaterials(IDFBaseModel):
    """Object gives an overall description of the slab ground heat transfer model."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:Materials'
    nmat_number_of_materials: float = Field(
        ...,
        gt=0.0,
        json_schema_extra={
            'note': 'This field specifies the number of different materials that will be used in the model. Typically only a ground material and a slab material are used. (2 materials)'
        },
    )
    albedo_surface_albedo_no_snow: float | None = Field(
        default=0.16,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Two fields specify the albedo value of the surface: first for no snow coverage days; second for days with snow coverage. The albedo is the solar reflectivity of the surface, and can vary from 0.05 ...'
        },
    )
    albedo_surface_albedo_snow: float | None = Field(default=0.4, ge=0.0, le=1.0)
    epslw_surface_emissivity_no_snow: float | None = Field(
        default=0.94,
        gt=0.0,
        json_schema_extra={
            'note': 'EPSLW (No Snow and Snow) specifies the long wavelength (thermal) emissivity of the ground surface. primarily important for nighttime radiation to sky. typical value .95'
        },
    )
    epslw_surface_emissivity_snow: float | None = Field(default=0.86, gt=0.0)
    z0_surface_roughness_no_snow: float | None = Field(
        default=0.75,
        gt=0.0,
        json_schema_extra={
            'units': 'cm',
            'note': 'fields Z0 (No Snow and Snow) describe the height at which an experimentally velocity profile goes to zero. typical value= .75 cm',
        },
    )
    z0_surface_roughness_snow: float | None = Field(
        default=0.25,
        gt=0.0,
        json_schema_extra={'units': 'cm', 'note': 'typical value= .05 cm'},
    )
    hin_indoor_hconv_downward_flow: float | None = Field(
        default=6.13,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m2-K',
            'note': 'These fields specify the combined convective and radiative heat transfer coefficient between the slab top inside surface and the room air for the cases where heat is flowing downward, and upward. T...',
        },
    )
    hin_indoor_hconv_upward: float | None = Field(
        default=9.26,
        gt=0.0,
        json_schema_extra={'units': 'W/m2-K', 'note': 'typical value= 4-10'},
    )


class GroundHeatTransferSlabMatlProps(IDFBaseModel):
    """This object contains the material properties for the materials used in the
    model. The fields are mostly self explanatory."""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:MatlProps'
    rho_slab_material_density: float | None = Field(
        default=2300.0,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/m3',
            'note': 'Density of Slab Material typical value= 2300.0',
        },
    )
    rho_soil_density: float | None = Field(
        default=1200.0,
        gt=0.0,
        json_schema_extra={
            'units': 'kg/m3',
            'note': 'Density of Soil Material typical value= 1200.0',
        },
    )
    cp_slab_cp: float | None = Field(
        default=650.0,
        gt=0.0,
        json_schema_extra={
            'units': 'J/kg-K',
            'note': 'Specific Heat of Slab Material typical value=650.0',
        },
    )
    cp_soil_cp: float | None = Field(
        default=1200.0,
        gt=0.0,
        json_schema_extra={
            'units': 'J/kg-K',
            'note': 'Specific Heat of Soil Material typical value= 1200.0',
        },
    )
    tcon_slab_k: float | None = Field(
        default=0.9,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m-K',
            'note': 'Conductivity of Slab Material typical value= .9',
        },
    )
    tcon_soil_k: float | None = Field(
        default=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'W/m-K',
            'note': 'Conductivity of Soil Material typical value= 1.0',
        },
    )


class GroundHeatTransferSlabXFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) XFACE: X
    Direction cell face coordinates: m"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:XFACE'


class GroundHeatTransferSlabYFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) YFACE: Y
    Direction cell face coordinates: m,"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:YFACE'


class GroundHeatTransferSlabZFACE(IDFBaseModel):
    """This is only needed when using manual gridding (not recommended) ZFACE: Z
    Direction cell face coordinates: m"""

    _idf_object_type: ClassVar[str] = 'GroundHeatTransfer:Slab:ZFACE'


class HeatExchangerAirToAirFlatPlate(IDFBaseModel):
    """Flat plate air-to-air heat exchanger, typically used for exhaust or relief
    air heat recovery."""

    _idf_object_type: ClassVar[str] = 'HeatExchanger:AirToAir:FlatPlate'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    flow_arrangement_type: (
        Literal['CounterFlow', 'CrossFlowBothUnmixed', 'ParallelFlow'] | None
    ) = Field(default=None)
    economizer_lockout: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Yes means that the heat exchanger will be locked out (off) when the economizer is operating or high humidity control is active'
        },
    )
    ratio_of_supply_to_secondary_ha_values: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'note': 'Ratio of h*A for supply side to h*A for exhaust side'
        },
    )
    nominal_supply_air_flow_rate: float | Literal['', 'Autosize'] | None = Field(
        default='Autosize', json_schema_extra={'units': 'm3/s'}
    )
    nominal_supply_air_inlet_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    nominal_supply_air_outlet_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    nominal_secondary_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    nominal_secondary_air_inlet_temperature: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    nominal_electric_power: float | None = Field(
        default=None, json_schema_extra={'units': 'W'}
    )
    supply_air_inlet_node_name: str = Field(...)
    supply_air_outlet_node_name: str = Field(...)
    secondary_air_inlet_node_name: str = Field(...)
    secondary_air_outlet_node_name: str = Field(...)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class HeatExchangerAirToAirSensibleAndLatent(IDFBaseModel):
    """This object models an air-to-air heat exchanger using effectiveness
    relationships. The heat exchanger can transfer sensible energy, latent
    energy, or both between the supply (primary) and exhaust (secondary) air
    streams."""

    _idf_object_type: ClassVar[str] = 'HeatExchanger:AirToAir:SensibleAndLatent'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    nominal_supply_air_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    sensible_effectiveness_at_100_heating_air_flow: float | None = Field(
        default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    latent_effectiveness_at_100_heating_air_flow: float | None = Field(
        default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    sensible_effectiveness_at_100_cooling_air_flow: float | None = Field(
        default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    latent_effectiveness_at_100_cooling_air_flow: float | None = Field(
        default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless'}
    )
    supply_air_inlet_node_name: str = Field(...)
    supply_air_outlet_node_name: str = Field(...)
    exhaust_air_inlet_node_name: str = Field(...)
    exhaust_air_outlet_node_name: str = Field(...)
    nominal_electric_power: float | None = Field(
        default=0.0, ge=0.0, json_schema_extra={'units': 'W'}
    )
    supply_air_outlet_temperature_control: Literal['', 'No', 'Yes'] | None = Field(
        default='No'
    )
    heat_exchanger_type: Literal['', 'Plate', 'Rotary'] | None = Field(default='Plate')
    frost_control_type: (
        Literal[
            '',
            'ExhaustAirRecirculation',
            'ExhaustOnly',
            'MinimumExhaustTemperature',
            'None',
        ]
        | None
    ) = Field(default='None')
    threshold_temperature: float | None = Field(
        default=1.7,
        json_schema_extra={
            'units': 'C',
            'note': 'Supply (outdoor) air inlet temp threshold for exhaust air recirculation and exhaust only frost control types. Exhaust air outlet threshold Temperature for minimum exhaust temperature frost control ...',
        },
    )
    initial_defrost_time_fraction: float | None = Field(
        default=0.083,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Fraction of the time when frost control will be invoked at the threshold temperature. This field only used for exhaust air recirc and exhaust-only frost control types.',
        },
    )
    rate_of_defrost_time_fraction_increase: float | None = Field(
        default=0.012,
        ge=0.0,
        json_schema_extra={
            'units': '1/K',
            'note': 'Rate of increase in defrost time fraction as actual temp falls below threshold temperature. This field only used for exhaust air recirc and exhaust-only frost control types.',
        },
    )
    economizer_lockout: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Yes means that the heat exchanger will be locked out (off) when the economizer is operating or high humidity control is active'
        },
    )
    sensible_effectiveness_of_heating_air_flow_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional if this field has value, then the sensible effectiveness for heating will be the value in N2 multiplied by this curve value',
        },
    )
    latent_effectiveness_of_heating_air_flow_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional if this field has value, then the latent effectiveness for heating will be the value in N3 multiplied by this curve value',
        },
    )
    sensible_effectiveness_of_cooling_air_flow_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional if this field has value, then the sensible effectiveness for cooling will be the value in N4 multiplied by this curve value',
        },
    )
    latent_effectiveness_of_cooling_air_flow_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'optional if this field has value, then the latent effectiveness for cooling will be the value in N5 multiplied by this curve value',
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def sensible_effectiveness_of_heating_air_flow_curve(self) -> IDFBaseModel | None:
        v = self.sensible_effectiveness_of_heating_air_flow_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def latent_effectiveness_of_heating_air_flow_curve(self) -> IDFBaseModel | None:
        v = self.latent_effectiveness_of_heating_air_flow_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def sensible_effectiveness_of_cooling_air_flow_curve(self) -> IDFBaseModel | None:
        v = self.sensible_effectiveness_of_cooling_air_flow_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def latent_effectiveness_of_cooling_air_flow_curve(self) -> IDFBaseModel | None:
        v = self.latent_effectiveness_of_cooling_air_flow_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])


class HeatExchangerDesiccantBalancedFlow(IDFBaseModel):
    """This object models a balanced desiccant heat exchanger. The heat exchanger
    transfers both sensible and latent energy between the process and
    regeneration air streams. The air flow rate and face velocity are assumed to
    be the same on both the process and regeneration sides of the heat
    exchanger."""

    _idf_object_type: ClassVar[str] = 'HeatExchanger:Desiccant:BalancedFlow'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    regeneration_air_inlet_node_name: str = Field(...)
    regeneration_air_outlet_node_name: str = Field(...)
    process_air_inlet_node_name: str = Field(...)
    process_air_outlet_node_name: str = Field(...)
    heat_exchanger_performance_object_type: (
        Literal['', 'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1'] | None
    ) = Field(default='HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1')
    heat_exchanger_performance_name: DesiccantHXPerfDataRef = Field(
        ..., json_schema_extra={'object_list': ['DesiccantHXPerfData']}
    )
    economizer_lockout: Literal['', 'No', 'Yes'] | None = Field(
        default='Yes',
        json_schema_extra={
            'note': 'Yes means that the heat exchanger will be locked out (off) when the economizer is operating or high humidity control is active'
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heat_exchanger_performance(
        self,
    ) -> HeatExchangerDesiccantBalancedFlowPerformanceDataType1 | None:
        v = self.heat_exchanger_performance_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['DesiccantHXPerfData'])


class HeatExchangerDesiccantBalancedFlowPerformanceDataType1(IDFBaseModel):
    """RTO = B1 + B2*RWI + B3*RTI + B4*(RWI/RTI) + B5*PWI + B6*PTI + B7*(PWI/PTI) +
    B8*RFV RWO = C1 + C2*RWI + C3*RTI + C4*(RWI/RTI) + C5*PWI + C6*PTI +
    C7*(PWI/PTI) + C8*RFV where, RTO = Dry-bulb temperature of the regeneration
    outlet air (C) RWO = Humidity ratio of the regeneration outlet air
    (kgWater/kgDryAir) RWI = Humidity ratio of the regeneration inlet air
    (kgWater/kgDryAir) RTI = Dry-bulb temperature of the regeneration inlet air
    (C) PWI = Humidity ratio of the process inlet air (kgWater/kgDryAir) PTI =
    Dry-bulb temperature of the process inlet air (C) RFV = Regeneration Face
    Velocity (m/s)"""

    _idf_object_type: ClassVar[str] = (
        'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    nominal_air_flow_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Air flow rate at nominal conditions (assumed to be the same for both sides of the heat exchanger).',
        },
    )
    nominal_air_face_velocity: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm/s'}
    )
    nominal_electric_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'Parasitic electric power (e.g., desiccant wheel motor)',
        },
    )
    temperature_equation_coefficient_1: float = Field(...)
    temperature_equation_coefficient_2: float = Field(...)
    temperature_equation_coefficient_3: float = Field(...)
    temperature_equation_coefficient_4: float = Field(...)
    temperature_equation_coefficient_5: float = Field(...)
    temperature_equation_coefficient_6: float = Field(...)
    temperature_equation_coefficient_7: float = Field(...)
    temperature_equation_coefficient_8: float = Field(...)
    minimum_regeneration_inlet_air_humidity_ratio_for_temperature_equation: float = (
        Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'})
    )
    maximum_regeneration_inlet_air_humidity_ratio_for_temperature_equation: float = (
        Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'})
    )
    minimum_regeneration_inlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    maximum_regeneration_inlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    minimum_process_inlet_air_humidity_ratio_for_temperature_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_process_inlet_air_humidity_ratio_for_temperature_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    minimum_process_inlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    maximum_process_inlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    minimum_regeneration_air_velocity_for_temperature_equation: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm/s'}
    )
    maximum_regeneration_air_velocity_for_temperature_equation: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm/s'}
    )
    minimum_regeneration_outlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    maximum_regeneration_outlet_air_temperature_for_temperature_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    minimum_regeneration_inlet_air_relative_humidity_for_temperature_equation: float = (
        Field(..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    )
    maximum_regeneration_inlet_air_relative_humidity_for_temperature_equation: float = (
        Field(..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    )
    minimum_process_inlet_air_relative_humidity_for_temperature_equation: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    maximum_process_inlet_air_relative_humidity_for_temperature_equation: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    humidity_ratio_equation_coefficient_1: float = Field(...)
    humidity_ratio_equation_coefficient_2: float = Field(...)
    humidity_ratio_equation_coefficient_3: float = Field(...)
    humidity_ratio_equation_coefficient_4: float = Field(...)
    humidity_ratio_equation_coefficient_5: float = Field(...)
    humidity_ratio_equation_coefficient_6: float = Field(...)
    humidity_ratio_equation_coefficient_7: float = Field(...)
    humidity_ratio_equation_coefficient_8: float = Field(...)
    minimum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation: float = (
        Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'})
    )
    maximum_regeneration_inlet_air_humidity_ratio_for_humidity_ratio_equation: float = (
        Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'})
    )
    minimum_regeneration_inlet_air_temperature_for_humidity_ratio_equation: float = (
        Field(..., json_schema_extra={'units': 'C'})
    )
    maximum_regeneration_inlet_air_temperature_for_humidity_ratio_equation: float = (
        Field(..., json_schema_extra={'units': 'C'})
    )
    minimum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_process_inlet_air_humidity_ratio_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    minimum_process_inlet_air_temperature_for_humidity_ratio_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    maximum_process_inlet_air_temperature_for_humidity_ratio_equation: float = Field(
        ..., json_schema_extra={'units': 'C'}
    )
    minimum_regeneration_air_velocity_for_humidity_ratio_equation: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm/s'}
    )
    maximum_regeneration_air_velocity_for_humidity_ratio_equation: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'm/s'}
    )
    minimum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    maximum_regeneration_outlet_air_humidity_ratio_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=1.0, json_schema_extra={'units': 'kgWater/kgDryAir'}
    )
    minimum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    maximum_regeneration_inlet_air_relative_humidity_for_humidity_ratio_equation: float = Field(
        ..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'}
    )
    minimum_process_inlet_air_relative_humidity_for_humidity_ratio_equation: float = (
        Field(..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    )
    maximum_process_inlet_air_relative_humidity_for_humidity_ratio_equation: float = (
        Field(..., ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    )


class HumidifierSteamElectric(IDFBaseModel):
    """Electrically heated steam humidifier with fan."""

    _idf_object_type: ClassVar[str] = 'Humidifier:Steam:Electric'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rated_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Capacity is m3/s of water at 5.05 C',
        },
    )
    rated_power: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'if autosized the rated power is calculated from the rated capacity and enthalpy rise of water from 20.0C to 100.0C steam and assumes electric to thermal energy conversion efficiency of 100.0%',
        },
    )
    rated_fan_power: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    standby_power: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    air_inlet_node_name: str | None = Field(default=None)
    air_outlet_node_name: str | None = Field(default=None)
    water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def water_storage_tank(self) -> WaterUseStorage | None:
        v = self.water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class HumidifierSteamGas(IDFBaseModel):
    """Natural gas fired steam humidifier with optional blower fan."""

    _idf_object_type: ClassVar[str] = 'Humidifier:Steam:Gas'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.',
        },
    )
    rated_capacity: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Capacity is m3/s of water at 5.05 C The nominal full capacity water addition rate in m3/s of water at 5.05 C',
        },
    )
    rated_gas_use_rate: float | Literal['Autosize'] | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'if auto-sized, the rated gas use rate is calculated from the rated capacity and enthalpy rise of water from 20.0C to 100.0C steam and user input thermal efficiency value specified in the next input...',
        },
    )
    thermal_efficiency: float | None = Field(
        default=0.8,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Based on the higher heating value of fuel. If "Rated Gas Use Rate" in the field above is not auto-sized and the Inlet Water Temperature Option input field is specified as FixedInletWaterTemperature...',
        },
    )
    thermal_efficiency_modifier_curve_name: UnivariateFunctionsRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'Linear, Quadratic and Cubic efficiency curves are solely a function of PLR. Linear = C1 + C2*PLR Quadratic = C1 + C2*PLR + C3*PLR^2 Cubic = C1 + C2*PLR + C3*PLR^2 + C4*PLR^3 This is thermal efficie...',
        },
    )
    rated_fan_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The nominal full capacity electric power input to the blower fan in Watts. If no blower fan is required to inject the dry steam to the supply air stream, then this input field is set to zero.',
        },
    )
    auxiliary_electric_power: float | None = Field(
        default=0.0,
        ge=0.0,
        json_schema_extra={
            'units': 'W',
            'note': 'The auxiliary electric power input in watts. This amount of power will be consumed whenever the unit is available (as defined by the availability schedule). This electric power is used for control ...',
        },
    )
    air_inlet_node_name: str | None = Field(default=None)
    air_outlet_node_name: str | None = Field(default=None)
    water_storage_tank_name: WaterStorageTankNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['WaterStorageTankNames']}
    )
    inlet_water_temperature_option: (
        Literal['', 'FixedInletWaterTemperature', 'VariableInletWaterTemperature']
        | None
    ) = Field(
        default='FixedInletWaterTemperature',
        json_schema_extra={
            'note': 'The inlet water temperature can be fixed at 20C as it is done for electric steam humidifier or it can be allowed to vary with temperature of the water source. Currently allowed water sources are ma...'
        },
    )

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def thermal_efficiency_modifier_curve(self) -> IDFBaseModel | None:
        v = self.thermal_efficiency_modifier_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def water_storage_tank(self) -> WaterUseStorage | None:
        v = self.water_storage_tank_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['WaterStorageTankNames'])


class HybridModelZone(IDFBaseModel):
    """Zones with measured air temperature data and a range of dates. If the range
    of temperature measurement dates includes a leap day, the weather data
    should include a leap day."""

    _idf_object_type: ClassVar[str] = 'HybridModel:Zone'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    calculate_zone_internal_thermal_mass: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Use measured zone air temperature to calculate zone internal thermal mass. If set to Yes, the measured zone air temperature should be provided to calculate the thermal mass. If set to No, the inver...'
        },
    )
    calculate_zone_air_infiltration_rate: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Use measured temperature data (temperature, humidity ratio, or CO2 concentration) to calculate zone air infiltration air flow rate. Only one of field Calculate Zone Internal Thermal Mass, Calculate...'
        },
    )
    calculate_zone_people_count: Literal['', 'No', 'Yes'] | None = Field(
        default='No',
        json_schema_extra={
            'note': 'Use measured humidity ratio data (temperature, humidity ratio, or CO2 concentration) to calculate zone people count. Only one of field Calculate Zone Internal Thermal Mass, Calculate Zone Air Infil...'
        },
    )
    zone_measured_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_measured_air_humidity_ratio_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_measured_air_co2_concentration_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_input_people_activity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'When this field is provided and valid, the default people activity level (used to calculate people count) will be overwritten. from Schedule:File',
        },
    )
    zone_input_people_sensible_heat_fraction_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'When this field is provided and valid, the default sensible heat fraction from people (used to calculate people count) will be overwritten. from Schedule:File',
            },
        )
    )
    zone_input_people_radiant_heat_fraction_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'When this field is provided and valid, the default radiant heat portion of the sensible heat from people (used to calculate people count) will be overwritten. from Schedule:File',
            },
        )
    )
    zone_input_people_co2_generation_rate_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'When this field is provided and valid, the default people CO2 generation rate (used to calculate people count) will be overwritten. from Schedule:File',
            },
        )
    )
    zone_input_supply_air_temperature_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_input_supply_air_mass_flow_rate_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_input_supply_air_humidity_ratio_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'from Schedule:File',
        },
    )
    zone_input_supply_air_co2_concentration_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'from Schedule:File',
            },
        )
    )
    begin_month: int = Field(..., ge=1, le=12)
    begin_day_of_month: int = Field(..., ge=1, le=31)
    end_month: int = Field(..., ge=1, le=12)
    end_day_of_month: int = Field(..., ge=1, le=31)

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def zone_measured_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.zone_measured_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_measured_air_humidity_ratio_schedule(self) -> IDFBaseModel | None:
        v = self.zone_measured_air_humidity_ratio_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_measured_air_co2_concentration_schedule(self) -> IDFBaseModel | None:
        v = self.zone_measured_air_co2_concentration_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_people_activity_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_people_activity_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_people_sensible_heat_fraction_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_people_sensible_heat_fraction_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_people_radiant_heat_fraction_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_people_radiant_heat_fraction_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_people_co2_generation_rate_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_people_co2_generation_rate_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_supply_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_supply_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_supply_air_mass_flow_rate_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_supply_air_mass_flow_rate_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_supply_air_humidity_ratio_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_supply_air_humidity_ratio_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone_input_supply_air_co2_concentration_schedule(self) -> IDFBaseModel | None:
        v = self.zone_input_supply_air_co2_concentration_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class LoadProfilePlant(IDFBaseModel):
    """Used to simulate a scheduled plant loop demand profile. Load and flow rate
    are specified using schedules. Positive values are heating loads, and
    negative values are cooling loads. The actual load met is dependent on the
    performance of the supply loop components. Optional inputs for steam loop."""

    _idf_object_type: ClassVar[str] = 'LoadProfile:Plant'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    load_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Schedule values are load in [W]',
        },
    )
    peak_flow_rate: float = Field(..., json_schema_extra={'units': 'm3/s'})
    flow_rate_fraction_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    plant_loop_fluid_type: Literal['', 'Steam', 'Water'] | None = Field(default='Water')
    degree_of_subcooling: float | None = Field(
        default=5.0,
        ge=1.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used only when Plant Loop Fluid Type=Steam.',
        },
    )
    degree_of_loop_subcooling: float | None = Field(
        default=20.0,
        ge=10.0,
        json_schema_extra={
            'units': 'C',
            'note': 'This field is used only when Plant Loop Fluid Type=Steam.',
        },
    )

    @property
    def load_schedule(self) -> IDFBaseModel | None:
        v = self.load_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def flow_rate_fraction_schedule(self) -> IDFBaseModel | None:
        v = self.flow_rate_fraction_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class MatrixTwoDimension(IDFBaseModel):
    """matrix data in row-major order list each row keeping the columns in order
    number of values must equal N1 x N2"""

    _idf_object_type: ClassVar[str] = 'Matrix:TwoDimension'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    number_of_rows: int = Field(...)
    number_of_columns: int = Field(...)
    values: list[MatrixTwoDimensionValuesItem] | None = Field(default=None)


class ParametricFileNameSuffix(IDFBaseModel):
    """Defines the suffixes to be appended to the idf and output file names for
    each parametric run. If this object is omitted, the suffix will default to
    the run number."""

    _idf_object_type: ClassVar[str] = 'Parametric:FileNameSuffix'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str | None = Field(default=None)
    suffixes: list[ParametricFileNameSuffixSuffixesItem] | None = Field(default=None)


class ParametricLogic(IDFBaseModel):
    """This object allows some types of objects to be included for some parametric
    cases and not for others. For example, you might want an overhang on a
    window in some parametric runs and not others. A single Parametric:Logic
    object is allowed per file. Consult the Input Output Reference for available
    commands and syntax."""

    _idf_object_type: ClassVar[str] = 'Parametric:Logic'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    lines: list[ParametricLogicLinesItem] | None = Field(default=None)


class ParametricRunControl(IDFBaseModel):
    """Controls which parametric runs are simulated. This object is optional. If it
    is not included, then all parametric runs are performed."""

    _idf_object_type: ClassVar[str] = 'Parametric:RunControl'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str | None = Field(default=None)
    runs: list[ParametricRunControlRunsItem] | None = Field(default=None)


class ParametricSetValueForRun(IDFBaseModel):
    """Parametric objects allow a set of multiple simulations to be defined in a
    single idf file. The parametric preprocessor scans the idf for Parametric:*
    objects then creates and runs multiple idf files, one for each defined
    simulation. The core parametric object is Parametric:SetValueForRun which
    defines the name of a parameter and sets the parameter to different values
    depending on which run is being simulated."""

    _idf_object_type: ClassVar[str] = 'Parametric:SetValueForRun'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(
        ...,
        json_schema_extra={
            'note': 'Parameter Name Must begin with the dollar sign character. The second character must be a letter. Remaining characters may only be letters or numbers. No spaces allowed.'
        },
    )
    values: list[ParametricSetValueForRunValuesItem] | None = Field(default=None)


class PlantLoop(IDFBaseModel):
    """Defines a central plant loop."""

    _idf_object_type: ClassVar[str] = 'PlantLoop'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    fluid_type: Literal['', 'Steam', 'UserDefinedFluidType', 'Water'] | None = Field(
        default='Water'
    )
    user_defined_fluid_type: FluidAndGlycolNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidAndGlycolNames'],
            'note': 'This field is only required when Fluid Type is UserDefinedFluidType',
        },
    )
    plant_equipment_operation_scheme_name: PlantOperationSchemesRef = Field(
        ..., json_schema_extra={'object_list': ['PlantOperationSchemes']}
    )
    loop_temperature_setpoint_node_name: str = Field(...)
    maximum_loop_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    minimum_loop_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    maximum_loop_flow_rate: float | Literal['Autosize'] = Field(
        ..., json_schema_extra={'units': 'm3/s'}
    )
    minimum_loop_flow_rate: float | None = Field(
        default=0.0, json_schema_extra={'units': 'm3/s'}
    )
    plant_loop_volume: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate', json_schema_extra={'units': 'm3'}
    )
    plant_side_inlet_node_name: str = Field(...)
    plant_side_outlet_node_name: str = Field(...)
    plant_side_branch_list_name: BranchListsRef = Field(
        ..., json_schema_extra={'object_list': ['BranchLists']}
    )
    plant_side_connector_list_name: ConnectorListsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ConnectorLists']}
    )
    demand_side_inlet_node_name: str = Field(...)
    demand_side_outlet_node_name: str = Field(...)
    demand_side_branch_list_name: BranchListsRef = Field(
        ..., json_schema_extra={'object_list': ['BranchLists']}
    )
    demand_side_connector_list_name: ConnectorListsRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ConnectorLists']}
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
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(
        default=None,
        json_schema_extra={'object_list': ['SystemAvailabilityManagerLists']},
    )
    plant_loop_demand_calculation_scheme: (
        Literal['', 'DualSetpointDeadband', 'SingleSetpoint'] | None
    ) = Field(default='SingleSetpoint')
    common_pipe_simulation: (
        Literal['', 'CommonPipe', 'None', 'TwoWayCommonPipe'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Specifies a primary-secondary loop configuration. The plant side is the primary loop, and the demand side is the secondary loop. A secondary supply pump is required on the demand side. None = Prima...'
        },
    )
    pressure_simulation_type: (
        Literal['', 'LoopFlowCorrection', 'None', 'PumpPowerCorrection'] | None
    ) = Field(default='None')
    loop_circulation_time: float | None = Field(
        default=2.0,
        ge=0.0,
        json_schema_extra={
            'units': 'minutes',
            'note': 'This field is only used to autocalculate the Plant Loop Volume. Loop Volume = Loop Circulation Time * Maximum Loop Flow Rate',
        },
    )

    @property
    def user_defined_fluid_type_ref(
        self,
    ) -> FluidPropertiesGlycolConcentration | FluidPropertiesName | None:
        v = self.user_defined_fluid_type
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FluidAndGlycolNames'])

    @property
    def plant_equipment_operation_scheme(self) -> PlantEquipmentOperationSchemes | None:
        v = self.plant_equipment_operation_scheme_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['PlantOperationSchemes'])

    @property
    def plant_side_branch_list(self) -> BranchList | None:
        v = self.plant_side_branch_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BranchLists'])

    @property
    def plant_side_connector_list(self) -> ConnectorList | None:
        v = self.plant_side_connector_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ConnectorLists'])

    @property
    def demand_side_branch_list(self) -> BranchList | None:
        v = self.demand_side_branch_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BranchLists'])

    @property
    def demand_side_connector_list(self) -> ConnectorList | None:
        v = self.demand_side_connector_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ConnectorLists'])

    @property
    def availability_manager_list(self) -> AvailabilityManagerAssignmentList | None:
        v = self.availability_manager_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SystemAvailabilityManagerLists'])


class TableIndependentVariable(IDFBaseModel):
    """An independent variable representing a single dimension of a Table:Lookup
    object."""

    _idf_object_type: ClassVar[str] = 'Table:IndependentVariable'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    interpolation_method: Literal['', 'Cubic', 'Linear'] | None = Field(
        default='Linear'
    )
    extrapolation_method: Literal['', 'Constant', 'Linear'] | None = Field(
        default='Constant'
    )
    minimum_value: float | None = Field(default=None)
    maximum_value: float | None = Field(default=None)
    normalization_reference_value: float | None = Field(default=None)
    unit_type: (
        Literal[
            '',
            'Angle',
            'Dimensionless',
            'Distance',
            'MassFlow',
            'Power',
            'Temperature',
            'VolumetricFlow',
        ]
        | None
    ) = Field(default='Dimensionless')
    external_file_name: str | None = Field(default=None)
    external_file_column_number: int | None = Field(default=None, ge=1)
    external_file_starting_row_number: int | None = Field(default=None, ge=1)
    values: list[MatrixTwoDimensionValuesItem] | None = Field(default=None)


class TableIndependentVariableList(IDFBaseModel):
    """A sorted list of independent variables used by one or more Table:Lookup
    objects."""

    _idf_object_type: ClassVar[str] = 'Table:IndependentVariableList'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    independent_variables: (
        list[TableIndependentVariableListIndependentVariablesItem] | None
    ) = Field(default=None)


class TableLookup(IDFBaseModel):
    """Lookup tables are used in place of curves and can represent any number of
    independent variables (defined as Table:IndependentVariable objects in a
    Table:IndependentVariableList). Output values are interpolated within the
    bounds defined by each independent variable and extrapolated beyond the
    bounds according to the interpolation/extrapolation methods defined by each
    independent variable."""

    _idf_object_type: ClassVar[str] = 'Table:Lookup'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    independent_variable_list_name: IndependentVariableListNameRef = Field(
        ..., json_schema_extra={'object_list': ['IndependentVariableListName']}
    )
    normalization_method: (
        Literal['', 'AutomaticWithDivisor', 'DivisorOnly', 'None'] | None
    ) = Field(default='None')
    normalization_divisor: float | None = Field(default=1.0)
    minimum_output: float | None = Field(default=None)
    maximum_output: float | None = Field(default=None)
    output_unit_type: (
        Literal['', 'Capacity', 'Dimensionless', 'Power', 'Pressure', 'Temperature']
        | None
    ) = Field(default='Dimensionless')
    external_file_name: str | None = Field(default=None)
    external_file_column_number: int | None = Field(default=None, ge=1)
    external_file_starting_row_number: int | None = Field(default=None, ge=1)
    values: list[TableLookupValuesItem] | None = Field(default=None)

    @property
    def independent_variable_list(self) -> TableIndependentVariableList | None:
        v = self.independent_variable_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['IndependentVariableListName'])


class TemperingValve(IDFBaseModel):
    """Temperature-controlled diversion valve used to divert flow around one or
    more plant components such as a hot water heater. It can only be used on one
    of two branches between a Splitter and a Mixer."""

    _idf_object_type: ClassVar[str] = 'TemperingValve'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    inlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of a Node'})
    outlet_node_name: str = Field(..., json_schema_extra={'note': 'Name of a Node'})
    stream_2_source_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of a Node'}
    )
    temperature_setpoint_node_name: str = Field(
        ..., json_schema_extra={'note': 'Name of a Node'}
    )
    pump_outlet_node_name: str = Field(...)


class ZoneTerminalUnitList(IDFBaseModel):
    """List of variable refrigerant flow (VRF) terminal units served by a given VRF
    condensing unit. See ZoneHVAC:TerminalUnit:VariableRefrigerantFlow and
    AirConditioner:VariableRefrigerantFlow."""

    _idf_object_type: ClassVar[str] = 'ZoneTerminalUnitList'
    _provider_fields: ClassVar[frozenset[str]] = frozenset(
        {'zone_terminal_unit_list_name'}
    )
    zone_terminal_unit_list_name: str = Field(...)
    terminal_units: list[ZoneTerminalUnitListTerminalUnitsItem] | None = Field(
        default=None
    )
