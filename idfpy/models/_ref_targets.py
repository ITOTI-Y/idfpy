"""Auto-generated unions of the classes each reference group can name.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 26.1.

Navigation properties whose field can name many object types return these
aliases. They are lazy ``type`` aliases, so the model imports below are only
needed by type checkers.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .advanced_construction import (
        FoundationKiva,
        SurfaceConvectionAlgorithmInsideUserCurve,
        SurfaceConvectionAlgorithmOutsideUserCurve,
        SurfacePropertyGroundSurfaces,
        SurfacePropertyLocalEnvironment,
        SurfacePropertyOtherSideCoefficients,
        SurfacePropertyOtherSideConditionsModel,
        SurfacePropertySurroundingSurfaces,
        SurfacePropertyUnderwater,
        ZonePropertyLocalEnvironment,
    )
    from .air_distribution import (
        AirLoopHVAC,
        AirLoopHVACDedicatedOutdoorAirSystem,
        AirLoopHVACMixer,
        AirLoopHVACOutdoorAirSystem,
        AirLoopHVACOutdoorAirSystemEquipmentList,
        AirLoopHVACReturnPlenum,
        AirLoopHVACSplitter,
        AirLoopHVACSupplyPlenum,
        AirLoopHVACZoneMixer,
        AirLoopHVACZoneSplitter,
        OutdoorAirMixer,
    )
    from .availability_managers import (
        AvailabilityManagerAssignmentList,
        AvailabilityManagerDifferentialThermostat,
        AvailabilityManagerHighTemperatureTurnOff,
        AvailabilityManagerHighTemperatureTurnOn,
        AvailabilityManagerHybridVentilation,
        AvailabilityManagerLowTemperatureTurnOff,
        AvailabilityManagerLowTemperatureTurnOn,
        AvailabilityManagerNightCycle,
        AvailabilityManagerNightVentilation,
        AvailabilityManagerOptimumStart,
        AvailabilityManagerScheduled,
        AvailabilityManagerScheduledOff,
        AvailabilityManagerScheduledOn,
    )
    from .coils import (
        CoilCoolingDX,
        CoilCoolingDXCurveFitOperatingMode,
        CoilCoolingDXCurveFitPerformance,
        CoilCoolingDXCurveFitSpeed,
        CoilCoolingDXMultiSpeed,
        CoilCoolingDXSingleSpeed,
        CoilCoolingDXSingleSpeedThermalStorage,
        CoilCoolingDXTwoSpeed,
        CoilCoolingDXTwoStageWithHumidityControlMode,
        CoilCoolingDXVariableRefrigerantFlow,
        CoilCoolingDXVariableRefrigerantFlowFluidTemperatureControl,
        CoilCoolingDXVariableSpeed,
        CoilCoolingWater,
        CoilCoolingWaterDetailedGeometry,
        CoilCoolingWaterToAirHeatPumpEquationFit,
        CoilCoolingWaterToAirHeatPumpParameterEstimation,
        CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit,
        CoilDXASHRAE205Performance,
        CoilHeatingDesuperheater,
        CoilHeatingDXMultiSpeed,
        CoilHeatingDXSingleSpeed,
        CoilHeatingDXVariableRefrigerantFlow,
        CoilHeatingDXVariableRefrigerantFlowFluidTemperatureControl,
        CoilHeatingDXVariableSpeed,
        CoilHeatingElectric,
        CoilHeatingElectricMultiStage,
        CoilHeatingFuel,
        CoilHeatingGasMultiStage,
        CoilHeatingSteam,
        CoilHeatingWater,
        CoilHeatingWaterToAirHeatPumpEquationFit,
        CoilHeatingWaterToAirHeatPumpParameterEstimation,
        CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit,
        CoilPerformanceDXCooling,
        CoilSystemCoolingDX,
        CoilSystemCoolingDXHeatExchangerAssisted,
        CoilSystemCoolingWater,
        CoilSystemCoolingWaterHeatExchangerAssisted,
        CoilSystemHeatingDX,
        CoilSystemIntegratedHeatPumpAirSource,
        CoilWaterHeatingAirToWaterHeatPumpPumped,
        CoilWaterHeatingAirToWaterHeatPumpVariableSpeed,
        CoilWaterHeatingAirToWaterHeatPumpWrapped,
    )
    from .condensers import (
        CoolingTowerPerformanceCoolTools,
        CoolingTowerPerformanceYorkCalc,
        CoolingTowerSingleSpeed,
        CoolingTowerTwoSpeed,
        CoolingTowerVariableSpeed,
        CoolingTowerVariableSpeedMerkel,
        EvaporativeFluidCoolerSingleSpeed,
        EvaporativeFluidCoolerTwoSpeed,
        FluidCoolerSingleSpeed,
        FluidCoolerTwoSpeed,
        GroundHeatExchangerHorizontalTrench,
        GroundHeatExchangerPond,
        GroundHeatExchangerResponseFactors,
        GroundHeatExchangerSlinky,
        GroundHeatExchangerSurface,
        GroundHeatExchangerSystem,
        GroundHeatExchangerVerticalArray,
        GroundHeatExchangerVerticalProperties,
        GroundHeatExchangerVerticalSingle,
        GroundHeatExchangerVerticalSizingRectangle,
        HeatExchangerFluidToFluid,
    )
    from .constructions import (
        Construction,
        ConstructionAirBoundary,
        ConstructionCfactorUndergroundWall,
        ConstructionComplexFenestrationState,
        ConstructionFfactorGroundFloor,
        ConstructionPropertyInternalHeatSource,
        ConstructionWindowDataFile,
        ConstructionWindowEquivalentLayer,
        Material,
        MaterialAirGap,
        MaterialInfraredTransparent,
        MaterialNoMass,
        MaterialPropertyGlazingSpectralData,
        MaterialRoofVegetation,
        WindowGapDeflectionState,
        WindowGapSupportPillar,
        WindowMaterialBlind,
        WindowMaterialBlindEquivalentLayer,
        WindowMaterialComplexShade,
        WindowMaterialDrapeEquivalentLayer,
        WindowMaterialGap,
        WindowMaterialGapEquivalentLayer,
        WindowMaterialGas,
        WindowMaterialGasMixture,
        WindowMaterialGlazing,
        WindowMaterialGlazingEquivalentLayer,
        WindowMaterialGlazingGroupThermochromic,
        WindowMaterialGlazingRefractionExtinctionMethod,
        WindowMaterialScreen,
        WindowMaterialScreenEquivalentLayer,
        WindowMaterialShade,
        WindowMaterialShadeEquivalentLayer,
        WindowMaterialSimpleGlazingSystem,
        WindowThermalModelParams,
    )
    from .curves import (
        CurveBicubic,
        CurveBiquadratic,
        CurveChillerPartLoadWithLift,
        CurveCubic,
        CurveCubicLinear,
        CurveDoubleExponentialDecay,
        CurveExponent,
        CurveExponentialDecay,
        CurveExponentialSkewNormal,
        CurveFanPressureRise,
        CurveFunctionalPressureDrop,
        CurveLinear,
        CurveQuadLinear,
        CurveQuadratic,
        CurveQuadraticLinear,
        CurveQuartic,
        CurveQuintLinear,
        CurveRectangularHyperbola1,
        CurveRectangularHyperbola2,
        CurveSigmoid,
        CurveTriquadratic,
    )
    from .daylighting import (
        DaylightingControls,
        DaylightingReferencePoint,
    )
    from .demand_limiting import (
        DemandManagerElectricEquipment,
        DemandManagerExteriorLights,
        DemandManagerLights,
        DemandManagerThermostats,
        DemandManagerVentilation,
    )
    from .economics import (
        UtilityCostTariff,
    )
    from .electric_load import (
        ElectricLoadCenterGenerators,
        ElectricLoadCenterInverterFunctionOfPower,
        ElectricLoadCenterInverterLookUpTable,
        ElectricLoadCenterInverterPVWatts,
        ElectricLoadCenterInverterSimple,
        ElectricLoadCenterStorageBattery,
        ElectricLoadCenterStorageConverter,
        ElectricLoadCenterStorageLiIonNMCBattery,
        ElectricLoadCenterStorageSimple,
        ElectricLoadCenterTransformer,
        GeneratorCombustionTurbine,
        GeneratorFuelCell,
        GeneratorFuelCellAirSupply,
        GeneratorFuelCellAuxiliaryHeater,
        GeneratorFuelCellElectricalStorage,
        GeneratorFuelCellExhaustGasToWaterHeatExchanger,
        GeneratorFuelCellInverter,
        GeneratorFuelCellPowerModule,
        GeneratorFuelCellStackCooler,
        GeneratorFuelCellWaterSupply,
        GeneratorFuelSupply,
        GeneratorInternalCombustionEngine,
        GeneratorMicroCHP,
        GeneratorMicroCHPNonNormalizedParameters,
        GeneratorMicroTurbine,
        GeneratorPhotovoltaic,
        GeneratorPVWatts,
        GeneratorWindTurbine,
        PhotovoltaicPerformanceEquivalentOneDiode,
        PhotovoltaicPerformanceSandia,
        PhotovoltaicPerformanceSimple,
    )
    from .ems import (
        EnergyManagementSystemProgram,
        EnergyManagementSystemProgramCallingManager,
        EnergyManagementSystemSubroutine,
    )
    from .evap_coolers import (
        EvaporativeCoolerDirectCelDekPad,
        EvaporativeCoolerDirectResearchSpecial,
        EvaporativeCoolerIndirectCelDekPad,
        EvaporativeCoolerIndirectResearchSpecial,
        EvaporativeCoolerIndirectWetCoil,
    )
    from .external_interface import (
        ExternalInterfaceFunctionalMockupUnitExportToSchedule,
        ExternalInterfaceFunctionalMockupUnitImport,
        ExternalInterfaceFunctionalMockupUnitImportToSchedule,
        ExternalInterfaceSchedule,
    )
    from .fans import (
        FanComponentModel,
        FanConstantVolume,
        FanOnOff,
        FanSystemModel,
        FanVariableVolume,
        FanZoneExhaust,
    )
    from .faults import (
        FaultModelThermostatOffset,
    )
    from .fluids import (
        FluidPropertiesGlycolConcentration,
        FluidPropertiesName,
        FluidPropertiesTemperatures,
    )
    from .hvac_design import (
        DesignSpecificationAirTerminalSizing,
        DesignSpecificationOutdoorAir,
        DesignSpecificationOutdoorAirSpaceList,
        DesignSpecificationZoneAirDistribution,
        DesignSpecificationZoneHVACSizing,
    )
    from .hvac_templates import (
        HVACTemplateSystemConstantVolume,
        HVACTemplateSystemDedicatedOutdoorAir,
        HVACTemplateSystemDualDuct,
        HVACTemplateSystemPackagedVAV,
        HVACTemplateSystemUnitary,
        HVACTemplateSystemUnitaryHeatPumpAirToAir,
        HVACTemplateSystemUnitarySystem,
        HVACTemplateSystemVAV,
        HVACTemplateSystemVRF,
        HVACTemplateThermostat,
        HVACTemplateZoneConstantVolume,
    )
    from .internal_gains import (
        ComfortViewFactorAngles,
        ElectricEquipment,
        Lights,
        People,
        SwimmingPoolIndoor,
    )
    from .location import (
        RunPeriod,
        SiteGroundTemperatureUndisturbedFiniteDifference,
        SiteGroundTemperatureUndisturbedKusudaAchenbach,
        SiteGroundTemperatureUndisturbedXing,
        SiteSpectrumData,
        SizingPeriodDesignDay,
        SizingPeriodWeatherFileConditionType,
        SizingPeriodWeatherFileDays,
    )
    from .misc import (
        AirConditionerVariableRefrigerantFlow,
        AirflowNetworkDistributionComponentCoil,
        AirflowNetworkDistributionComponentConstantPressureDrop,
        AirflowNetworkDistributionComponentDuct,
        AirflowNetworkDistributionComponentFan,
        AirflowNetworkDistributionComponentHeatExchanger,
        AirflowNetworkDistributionComponentLeak,
        AirflowNetworkDistributionComponentLeakageRatio,
        AirflowNetworkDistributionComponentOutdoorAirFlow,
        AirflowNetworkDistributionComponentReliefAirFlow,
        AirflowNetworkDistributionComponentTerminalUnit,
        AirflowNetworkDistributionLinkage,
        AirflowNetworkDistributionNode,
        AirflowNetworkIntraZoneLinkage,
        AirflowNetworkIntraZoneNode,
        AirflowNetworkMultiZoneComponentDetailedOpening,
        AirflowNetworkMultiZoneComponentHorizontalOpening,
        AirflowNetworkMultiZoneComponentSimpleOpening,
        AirflowNetworkMultiZoneComponentZoneExhaustFan,
        AirflowNetworkMultiZoneExternalNode,
        AirflowNetworkMultiZoneReferenceCrackConditions,
        AirflowNetworkMultiZoneSpecifiedFlowRate,
        AirflowNetworkMultiZoneSurfaceCrack,
        AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea,
        AirflowNetworkMultiZoneWindPressureCoefficientArray,
        AirflowNetworkMultiZoneWindPressureCoefficientValues,
        AirflowNetworkMultiZoneZone,
        AirflowNetworkOccupantVentilationControl,
        AirflowNetworkZoneControlPressureController,
        AirLoopHVACControllerList,
        CondenserLoop,
        ControllerMechanicalVentilation,
        ControllerOutdoorAir,
        ControllerWaterCoil,
        DehumidifierDesiccantNoFans,
        DehumidifierDesiccantSystem,
        ExteriorLights,
        HeatExchangerAirToAirFlatPlate,
        HeatExchangerAirToAirSensibleAndLatent,
        HeatExchangerDesiccantBalancedFlow,
        HeatExchangerDesiccantBalancedFlowPerformanceDataType1,
        HumidifierSteamElectric,
        HumidifierSteamGas,
        LoadProfilePlant,
        MatrixTwoDimension,
        PlantLoop,
        TableIndependentVariable,
        TableIndependentVariableList,
        TableLookup,
        TemperingValve,
        ZoneTerminalUnitList,
    )
    from .node_branch import (
        Branch,
        BranchList,
        ConnectorList,
        ConnectorMixer,
        ConnectorSplitter,
        Duct,
        OutdoorAirNode,
        PipeAdiabatic,
        PipeAdiabaticSteam,
        PipeIndoor,
        PipeOutdoor,
        PipeUnderground,
        PipingSystemUndergroundPipeCircuit,
        PipingSystemUndergroundPipeSegment,
    )
    from .outputs import (
        OutputControlSurfaceColorScheme,
    )
    from .plant_control import (
        CondenserEquipmentList,
        CondenserEquipmentOperationSchemes,
        PlantEquipmentList,
        PlantEquipmentOperationChillerHeaterChangeover,
        PlantEquipmentOperationComponentSetpoint,
        PlantEquipmentOperationCoolingLoad,
        PlantEquipmentOperationHeatingLoad,
        PlantEquipmentOperationOutdoorDewpoint,
        PlantEquipmentOperationOutdoorDewpointDifference,
        PlantEquipmentOperationOutdoorDryBulb,
        PlantEquipmentOperationOutdoorDryBulbDifference,
        PlantEquipmentOperationOutdoorRelativeHumidity,
        PlantEquipmentOperationOutdoorWetBulb,
        PlantEquipmentOperationOutdoorWetBulbDifference,
        PlantEquipmentOperationSchemes,
        PlantEquipmentOperationThermalEnergyStorage,
        PlantEquipmentOperationUncontrolled,
    )
    from .plant_equipment import (
        BoilerHotWater,
        BoilerSteam,
        CentralHeatPumpSystem,
        ChillerAbsorption,
        ChillerAbsorptionIndirect,
        ChillerCombustionTurbine,
        ChillerConstantCOP,
        ChillerElectric,
        ChillerElectricASHRAE205,
        ChillerElectricEIR,
        ChillerElectricReformulatedEIR,
        ChillerEngineDriven,
        ChillerHeaterAbsorptionDirectFired,
        ChillerHeaterAbsorptionDoubleEffect,
        ChillerHeaterPerformanceElectricEIR,
        DistrictCooling,
        DistrictHeatingSteam,
        DistrictHeatingWater,
        HeatPumpAirToWater,
        HeatPumpAirToWaterFuelFiredCooling,
        HeatPumpAirToWaterFuelFiredHeating,
        HeatPumpPlantLoopEIRCooling,
        HeatPumpPlantLoopEIRHeating,
        HeatPumpWaterToWaterEquationFitCooling,
        HeatPumpWaterToWaterEquationFitHeating,
        HeatPumpWaterToWaterParameterEstimationCooling,
        HeatPumpWaterToWaterParameterEstimationHeating,
        PlantComponentTemperatureSource,
    )
    from .pumps import (
        HeaderedPumpsConstantSpeed,
        HeaderedPumpsVariableSpeed,
        PumpConstantSpeed,
        PumpVariableSpeed,
        PumpVariableSpeedCondensate,
    )
    from .python_plugins import (
        PythonPluginInstance,
    )
    from .refrigeration import (
        RefrigerationAirChiller,
        RefrigerationCase,
        RefrigerationCaseAndWalkInList,
        RefrigerationCompressor,
        RefrigerationCompressorList,
        RefrigerationCompressorRack,
        RefrigerationCondenserAirCooled,
        RefrigerationCondenserCascade,
        RefrigerationCondenserEvaporativeCooled,
        RefrigerationCondenserWaterCooled,
        RefrigerationGasCoolerAirCooled,
        RefrigerationSecondarySystem,
        RefrigerationSubcooler,
        RefrigerationSystem,
        RefrigerationTranscriticalSystem,
        RefrigerationTransferLoadList,
        RefrigerationWalkIn,
        ZoneHVACRefrigerationChillerSet,
    )
    from .room_air import (
        RoomAirNode,
        RoomAirNodeAirflowNetwork,
        RoomAirNodeAirflowNetworkAdjacentSurfaceList,
        RoomAirNodeAirflowNetworkHVACEquipment,
        RoomAirNodeAirflowNetworkInternalGains,
    )
    from .schedules import (
        ScheduleCompact,
        ScheduleConstant,
        ScheduleDayHourly,
        ScheduleDayInterval,
        ScheduleDayList,
        ScheduleFile,
        ScheduleTypeLimits,
        ScheduleWeekCompact,
        ScheduleWeekDaily,
        ScheduleYear,
    )
    from .solar import (
        SolarCollectorFlatPlatePhotovoltaicThermal,
        SolarCollectorFlatPlateWater,
        SolarCollectorIntegralCollectorStorage,
        SolarCollectorPerformanceFlatPlate,
        SolarCollectorPerformanceIntegralCollectorStorage,
        SolarCollectorPerformancePhotovoltaicThermalBIPVT,
        SolarCollectorPerformancePhotovoltaicThermalSimple,
        SolarCollectorUnglazedTranspired,
    )
    from .thermal_zones import (
        BuildingSurfaceDetailed,
        CeilingAdiabatic,
        CeilingInterzone,
        Door,
        DoorInterzone,
        FenestrationSurfaceDetailed,
        FloorAdiabatic,
        FloorDetailed,
        FloorGroundContact,
        FloorInterzone,
        GlazedDoor,
        GlazedDoorInterzone,
        InternalMass,
        Roof,
        RoofCeilingDetailed,
        ShadingBuilding,
        ShadingBuildingDetailed,
        ShadingFin,
        ShadingFinProjection,
        ShadingOverhang,
        ShadingOverhangProjection,
        ShadingSite,
        ShadingSiteDetailed,
        ShadingZoneDetailed,
        Space,
        SpaceList,
        WallAdiabatic,
        WallDetailed,
        WallExterior,
        WallInterzone,
        WallUnderground,
        Window,
        WindowInterzone,
        WindowPropertyFrameAndDivider,
        WindowShadingControl,
        Zone,
        ZoneList,
    )
    from .unitary import (
        AirLoopHVACUnitaryFurnaceHeatCool,
        AirLoopHVACUnitaryFurnaceHeatOnly,
        AirLoopHVACUnitaryHeatCool,
        AirLoopHVACUnitaryHeatCoolVAVChangeoverBypass,
        AirLoopHVACUnitaryHeatOnly,
        AirLoopHVACUnitaryHeatPumpAirToAir,
        AirLoopHVACUnitaryHeatPumpAirToAirMultiSpeed,
        AirLoopHVACUnitaryHeatPumpWaterToAir,
        AirLoopHVACUnitarySystem,
        UnitarySystemPerformanceMultispeed,
    )
    from .user_defined import (
        AirTerminalSingleDuctUserDefined,
        CoilUserDefined,
        PlantComponentUserDefined,
        ZoneHVACForcedAirUserDefined,
    )
    from .water_heaters import (
        ThermalStorageChilledWaterMixed,
        ThermalStorageChilledWaterStratified,
        ThermalStorageHotWaterStratified,
        ThermalStorageIceDetailed,
        ThermalStorageIceSimple,
        ThermalStoragePCM,
        ThermalStorageSizing,
        WaterHeaterHeatPumpPumpedCondenser,
        WaterHeaterHeatPumpWrappedCondenser,
        WaterHeaterMixed,
        WaterHeaterStratified,
    )
    from .water_systems import (
        WaterUseConnections,
        WaterUseEquipment,
        WaterUseStorage,
    )
    from .zone_airflow import (
        ZoneEarthtubeParameters,
        ZoneVentilationDesignFlowRate,
        ZoneVentilationWindandStackOpenArea,
    )
    from .zone_controls import (
        ThermostatSetpointDualSetpoint,
        ThermostatSetpointSingleCooling,
        ThermostatSetpointSingleHeating,
        ThermostatSetpointSingleHeatingOrCooling,
        ThermostatSetpointThermalComfortFangerDualSetpoint,
        ThermostatSetpointThermalComfortFangerSingleCooling,
        ThermostatSetpointThermalComfortFangerSingleHeating,
        ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling,
        ZoneControlHumidistat,
        ZoneControlThermostat,
        ZoneControlThermostatStagedDualSetpoint,
    )
    from .zone_equipment import (
        SpaceHVACZoneEquipmentMixer,
        SpaceHVACZoneEquipmentSplitter,
        SpaceHVACZoneReturnMixer,
        ZoneHVACEquipmentList,
    )
    from .zone_forced_air import (
        ZoneHVACDehumidifierDX,
        ZoneHVACEnergyRecoveryVentilator,
        ZoneHVACEnergyRecoveryVentilatorController,
        ZoneHVACEvaporativeCoolerUnit,
        ZoneHVACFourPipeFanCoil,
        ZoneHVACHybridUnitaryHVAC,
        ZoneHVACIdealLoadsAirSystem,
        ZoneHVACOutdoorAirUnit,
        ZoneHVACOutdoorAirUnitEquipmentList,
        ZoneHVACPackagedTerminalAirConditioner,
        ZoneHVACPackagedTerminalHeatPump,
        ZoneHVACTerminalUnitVariableRefrigerantFlow,
        ZoneHVACUnitHeater,
        ZoneHVACUnitVentilator,
        ZoneHVACWaterToAirHeatPump,
        ZoneHVACWindowAirConditioner,
    )
    from .zone_radiative import (
        ZoneHVACBaseboardConvectiveElectric,
        ZoneHVACBaseboardConvectiveWater,
        ZoneHVACBaseboardRadiantConvectiveElectric,
        ZoneHVACBaseboardRadiantConvectiveSteam,
        ZoneHVACBaseboardRadiantConvectiveSteamDesign,
        ZoneHVACBaseboardRadiantConvectiveWater,
        ZoneHVACBaseboardRadiantConvectiveWaterDesign,
        ZoneHVACCoolingPanelRadiantConvectiveWater,
        ZoneHVACHighTemperatureRadiant,
        ZoneHVACLowTemperatureRadiantConstantFlow,
        ZoneHVACLowTemperatureRadiantConstantFlowDesign,
        ZoneHVACLowTemperatureRadiantElectric,
        ZoneHVACLowTemperatureRadiantSurfaceGroup,
        ZoneHVACLowTemperatureRadiantVariableFlow,
        ZoneHVACLowTemperatureRadiantVariableFlowDesign,
        ZoneHVACVentilatedSlab,
        ZoneHVACVentilatedSlabSlabGroup,
    )
    from .zone_terminals import (
        AirTerminalDualDuctConstantVolume,
        AirTerminalDualDuctVAV,
        AirTerminalDualDuctVAVOutdoorAir,
        AirTerminalSingleDuctConstantVolumeCooledBeam,
        AirTerminalSingleDuctConstantVolumeFourPipeBeam,
        AirTerminalSingleDuctConstantVolumeFourPipeInduction,
        AirTerminalSingleDuctConstantVolumeNoReheat,
        AirTerminalSingleDuctConstantVolumeReheat,
        AirTerminalSingleDuctMixer,
        AirTerminalSingleDuctParallelPIUReheat,
        AirTerminalSingleDuctSeriesPIUReheat,
        AirTerminalSingleDuctVAVHeatAndCoolNoReheat,
        AirTerminalSingleDuctVAVHeatAndCoolReheat,
        AirTerminalSingleDuctVAVNoReheat,
        AirTerminalSingleDuctVAVReheat,
        AirTerminalSingleDuctVAVReheatVariableSpeedFan,
        ZoneHVACAirDistributionUnit,
    )


type AFNCoilNamesTarget = (
    CoilCoolingDX
    | CoilCoolingDXMultiSpeed
    | CoilCoolingDXSingleSpeed
    | CoilCoolingDXSingleSpeedThermalStorage
    | CoilCoolingDXTwoSpeed
    | CoilCoolingDXTwoStageWithHumidityControlMode
    | CoilCoolingDXVariableSpeed
    | CoilCoolingWater
    | CoilCoolingWaterDetailedGeometry
    | CoilCoolingWaterToAirHeatPumpEquationFit
    | CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
    | CoilHeatingDXMultiSpeed
    | CoilHeatingDXSingleSpeed
    | CoilHeatingDXVariableSpeed
    | CoilHeatingDesuperheater
    | CoilHeatingElectric
    | CoilHeatingFuel
    | CoilHeatingWater
    | CoilHeatingWaterToAirHeatPumpEquationFit
    | CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit
)

type AFNHeatExchangerNamesTarget = (
    HeatExchangerAirToAirFlatPlate
    | HeatExchangerAirToAirSensibleAndLatent
    | HeatExchangerDesiccantBalancedFlow
)

type AFNOutdoorAirFlowNamesTarget = AirflowNetworkDistributionComponentOutdoorAirFlow

type AFNReliefAirFlowNamesTarget = AirflowNetworkDistributionComponentReliefAirFlow

type AFNTerminalUnitNamesTarget = (
    AirTerminalSingleDuctConstantVolumeNoReheat
    | AirTerminalSingleDuctConstantVolumeReheat
    | AirTerminalSingleDuctVAVReheat
)

type AirFlowNetworkMultizoneZonesTarget = AirflowNetworkMultiZoneZone

type AirLoopControllersTarget = ControllerOutdoorAir | ControllerWaterCoil

type AirLoopHVACMixerNamesTarget = AirLoopHVACMixer

type AirLoopHVACSplitterNamesTarget = AirLoopHVACSplitter

type AirLoopOAEquipmentListsTarget = AirLoopHVACOutdoorAirSystemEquipmentList

type AirPrimaryLoopsTarget = AirLoopHVAC

type AirTerminalUnitNamesTarget = (
    AirTerminalDualDuctConstantVolume
    | AirTerminalDualDuctVAV
    | AirTerminalDualDuctVAVOutdoorAir
    | AirTerminalSingleDuctConstantVolumeCooledBeam
    | AirTerminalSingleDuctConstantVolumeFourPipeBeam
    | AirTerminalSingleDuctConstantVolumeFourPipeInduction
    | AirTerminalSingleDuctConstantVolumeNoReheat
    | AirTerminalSingleDuctConstantVolumeReheat
    | AirTerminalSingleDuctMixer
    | AirTerminalSingleDuctParallelPIUReheat
    | AirTerminalSingleDuctSeriesPIUReheat
    | AirTerminalSingleDuctUserDefined
    | AirTerminalSingleDuctVAVHeatAndCoolNoReheat
    | AirTerminalSingleDuctVAVHeatAndCoolReheat
    | AirTerminalSingleDuctVAVNoReheat
    | AirTerminalSingleDuctVAVReheat
    | AirTerminalSingleDuctVAVReheatVariableSpeedFan
)

type AirflowNetworkLinkageNamesTarget = AirflowNetworkIntraZoneLinkage

type AirflowNetworkComponentNamesTarget = (
    AirflowNetworkDistributionComponentCoil
    | AirflowNetworkDistributionComponentConstantPressureDrop
    | AirflowNetworkDistributionComponentDuct
    | AirflowNetworkDistributionComponentFan
    | AirflowNetworkDistributionComponentHeatExchanger
    | AirflowNetworkDistributionComponentLeak
    | AirflowNetworkDistributionComponentLeakageRatio
    | AirflowNetworkDistributionComponentOutdoorAirFlow
    | AirflowNetworkDistributionComponentReliefAirFlow
    | AirflowNetworkDistributionComponentTerminalUnit
)

type AirflowNetworkDistributionLinkageNamesTarget = AirflowNetworkDistributionLinkage

type AirflowNetworkNodeAndZoneNamesTarget = AirflowNetworkDistributionNode | Zone

type AirflowNetworkNodeNamesTarget = AirflowNetworkIntraZoneNode

type AirflowNetworkOccupantVentilationControlNamesTarget = (
    AirflowNetworkOccupantVentilationControl
)

type AirflowNetworkZoneControlPressureControllerNamesTarget = (
    AirflowNetworkZoneControlPressureController
)

type AllHeatTranAngFacNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | ComfortViewFactorAngles
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | GlazedDoor
    | GlazedDoorInterzone
    | InternalMass
    | Roof
    | RoofCeilingDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
    | Window
    | WindowInterzone
)

type AllHeatTranSurfNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | GlazedDoor
    | GlazedDoorInterzone
    | InternalMass
    | Roof
    | RoofCeilingDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
    | Window
    | WindowInterzone
)

type AllShadingAndHTSurfNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | GlazedDoor
    | GlazedDoorInterzone
    | Roof
    | RoofCeilingDetailed
    | ShadingBuilding
    | ShadingBuildingDetailed
    | ShadingFin
    | ShadingFinProjection
    | ShadingOverhang
    | ShadingOverhangProjection
    | ShadingSite
    | ShadingSiteDetailed
    | ShadingZoneDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
    | Window
    | WindowInterzone
)

type AllShadingSurfNamesTarget = (
    ShadingBuilding
    | ShadingBuildingDetailed
    | ShadingFin
    | ShadingFinProjection
    | ShadingOverhang
    | ShadingOverhangProjection
    | ShadingSite
    | ShadingSiteDetailed
    | ShadingZoneDetailed
)

type AttachedShadingSurfNamesTarget = (
    ShadingFin
    | ShadingFinProjection
    | ShadingOverhang
    | ShadingOverhangProjection
    | ShadingZoneDetailed
)

type BivariateFunctionsTarget = (
    CurveBicubic
    | CurveBiquadratic
    | CurveCubicLinear
    | CurveFanPressureRise
    | CurveQuadraticLinear
    | TableLookup
)

type BoilersTarget = BoilerHotWater

type BranchListsTarget = BranchList

type BranchesTarget = Branch

type CFSGapTarget = WindowMaterialGap

type CFSGlazingNameTarget = WindowMaterialGlazing

type ChillerHeaterEIRNamesTarget = ChillerHeaterPerformanceElectricEIR

type ChillersTarget = (
    ChillerAbsorption
    | ChillerAbsorptionIndirect
    | ChillerCombustionTurbine
    | ChillerConstantCOP
    | ChillerElectric
    | ChillerElectricASHRAE205
    | ChillerElectricEIR
    | ChillerElectricReformulatedEIR
    | ChillerEngineDriven
)

type CoilCoolingDXTarget = CoilCoolingDX

type CoilPerformanceDXTarget = CoilPerformanceDXCooling

type CollectorStoragePerformanceTarget = (
    SolarCollectorPerformanceIntegralCollectorStorage
)

type ColorSchemesTarget = OutputControlSurfaceColorScheme

type CompactHVACSystemConstantVolumeTarget = HVACTemplateSystemConstantVolume

type CompactHVACSystemDualDuctTarget = HVACTemplateSystemDualDuct

type CompactHVACSystemUnitaryTarget = (
    HVACTemplateSystemUnitary
    | HVACTemplateSystemUnitaryHeatPumpAirToAir
    | HVACTemplateSystemUnitarySystem
)

type CompactHVACSystemVAVTarget = HVACTemplateSystemPackagedVAV | HVACTemplateSystemVAV

type CompactHVACSystemVRFTarget = HVACTemplateSystemVRF

type CompactHVACThermostatsTarget = HVACTemplateThermostat

type ComplexFenestrationStatesTarget = ConstructionComplexFenestrationState

type CondenserEquipmentListsTarget = CondenserEquipmentList

type CondenserOperationSchemesTarget = CondenserEquipmentOperationSchemes

type ConnectorListsTarget = ConnectorList

type ConstructionNamesTarget = (
    Construction
    | ConstructionAirBoundary
    | ConstructionCfactorUndergroundWall
    | ConstructionFfactorGroundFloor
    | ConstructionWindowDataFile
    | ConstructionWindowEquivalentLayer
)

type ControlSchemeListTarget = (
    PlantEquipmentOperationChillerHeaterChangeover
    | PlantEquipmentOperationComponentSetpoint
    | PlantEquipmentOperationCoolingLoad
    | PlantEquipmentOperationHeatingLoad
    | PlantEquipmentOperationOutdoorDewpoint
    | PlantEquipmentOperationOutdoorDewpointDifference
    | PlantEquipmentOperationOutdoorDryBulb
    | PlantEquipmentOperationOutdoorDryBulbDifference
    | PlantEquipmentOperationOutdoorRelativeHumidity
    | PlantEquipmentOperationOutdoorWetBulb
    | PlantEquipmentOperationOutdoorWetBulbDifference
    | PlantEquipmentOperationThermalEnergyStorage
    | PlantEquipmentOperationUncontrolled
)

type ControlTypeNamesTarget = (
    ThermostatSetpointDualSetpoint
    | ThermostatSetpointSingleCooling
    | ThermostatSetpointSingleHeating
    | ThermostatSetpointSingleHeatingOrCooling
)

type ControllerListsTarget = AirLoopHVACControllerList

type ControllerMechanicalVentNamesTarget = ControllerMechanicalVentilation

type ControllerStandAloneEnergyRecoveryVentilatorTarget = (
    ZoneHVACEnergyRecoveryVentilatorController
)

type ConverterListTarget = ElectricLoadCenterStorageConverter

type CoolingCoilNameTarget = CoilCoolingWater | CoilCoolingWaterDetailedGeometry

type CoolingCoilSystemNameTarget = CoilSystemCoolingDX

type CoolingCoilsDXTarget = (
    CoilCoolingDXSingleSpeed
    | CoilCoolingDXSingleSpeedThermalStorage
    | CoilCoolingDXTwoSpeed
    | CoilCoolingDXTwoStageWithHumidityControlMode
    | CoilSystemCoolingDXHeatExchangerAssisted
)

type CoolingCoilsDXMultiModeOrSingleSpeedTarget = (
    CoilCoolingDXSingleSpeed
    | CoilCoolingDXSingleSpeedThermalStorage
    | CoilCoolingDXTwoStageWithHumidityControlMode
    | CoilSystemCoolingDXHeatExchangerAssisted
)

type CoolingCoilsDXMultiSpeedTarget = CoilCoolingDXMultiSpeed

type CoolingCoilsDXSingleSpeedTarget = (
    CoilCoolingDXSingleSpeed
    | CoilCoolingDXSingleSpeedThermalStorage
    | CoilSystemCoolingDXHeatExchangerAssisted
)

type CoolingCoilsDXVarRefrigFlowTarget = CoilCoolingDXVariableRefrigerantFlow

type CoolingCoilsDXVarRefrigFlowFluidTemperatureControlTarget = (
    CoilCoolingDXVariableRefrigerantFlowFluidTemperatureControl
)

type CoolingCoilsDXVariableSpeedTarget = CoilCoolingDXVariableSpeed

type CoolingCoilsWaterTarget = (
    CoilCoolingWater
    | CoilCoolingWaterDetailedGeometry
    | CoilSystemCoolingWaterHeatExchangerAssisted
)

type CoolingCoilsWaterNoHXTarget = CoilCoolingWater | CoilCoolingWaterDetailedGeometry

type CoolingCoilsWaterToAirHPTarget = (
    CoilCoolingWaterToAirHeatPumpEquationFit
    | CoilCoolingWaterToAirHeatPumpParameterEstimation
)

type CoolingCoilsWaterToAirVSHPTarget = (
    CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
)

type CoolingTowersTarget = (
    CoolingTowerSingleSpeed
    | CoolingTowerTwoSpeed
    | CoolingTowerVariableSpeed
    | CoolingTowerVariableSpeedMerkel
)

type CoolingTowersWithUATarget = (
    CoolingTowerSingleSpeed | CoolingTowerTwoSpeed | CoolingTowerVariableSpeedMerkel
)

type DOASAirLoopsTarget = AirLoopHVACDedicatedOutdoorAirSystem

type DOAToZonalUnitTarget = (
    AirLoopHVACUnitarySystem
    | ZoneHVACFourPipeFanCoil
    | ZoneHVACPackagedTerminalAirConditioner
    | ZoneHVACPackagedTerminalHeatPump
    | ZoneHVACTerminalUnitVariableRefrigerantFlow
    | ZoneHVACUnitVentilator
    | ZoneHVACWaterToAirHeatPump
)

type DSOASpaceListNamesTarget = DesignSpecificationOutdoorAirSpaceList

type DXCoolingOperatingModeNamesTarget = CoilCoolingDXCurveFitOperatingMode

type DXCoolingPerformanceNamesTarget = (
    CoilCoolingDXCurveFitPerformance | CoilDXASHRAE205Performance
)

type DXCoolingSpeedNamesTarget = CoilCoolingDXCurveFitSpeed

type DataMatricesTarget = MatrixTwoDimension

type DayScheduleNamesTarget = ScheduleDayHourly | ScheduleDayInterval | ScheduleDayList

type DaylightReferencePointNamesTarget = DaylightingReferencePoint

type DaylightingControlNamesTarget = DaylightingControls

type DemandManagerNamesTarget = (
    DemandManagerElectricEquipment
    | DemandManagerExteriorLights
    | DemandManagerLights
    | DemandManagerThermostats
    | DemandManagerVentilation
)

type DesiccantHXPerfDataTarget = HeatExchangerDesiccantBalancedFlowPerformanceDataType1

type DesignSpecificationAirTerminalSizingNameTarget = (
    DesignSpecificationAirTerminalSizing
)

type DesignSpecificationOutdoorAirNamesTarget = DesignSpecificationOutdoorAir

type DesignSpecificationZoneAirDistributionNamesTarget = (
    DesignSpecificationZoneAirDistribution
)

type DesignSpecificationZoneHVACSizingNameTarget = DesignSpecificationZoneHVACSizing

type DesuperHeatingCoilSourcesTarget = (
    CoilCoolingDX
    | CoilCoolingDXSingleSpeed
    | CoilCoolingDXTwoSpeed
    | CoilCoolingDXTwoStageWithHumidityControlMode
    | CoilCoolingDXVariableSpeed
    | RefrigerationCompressorRack
    | RefrigerationCondenserAirCooled
    | RefrigerationCondenserEvaporativeCooled
    | RefrigerationCondenserWaterCooled
)

type DesuperHeatingWaterOnlySourcesTarget = (
    CoilCoolingDXMultiSpeed
    | CoilCoolingWaterToAirHeatPumpEquationFit
    | CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
)

type EarthTubeParameterNamesTarget = ZoneEarthtubeParameters

type ElecStorageListTarget = (
    ElectricLoadCenterStorageBattery
    | ElectricLoadCenterStorageLiIonNMCBattery
    | ElectricLoadCenterStorageSimple
)

type ElectricEquipmentNamesTarget = ElectricEquipment

type ErlProgramNamesTarget = (
    EnergyManagementSystemProgram | EnergyManagementSystemSubroutine
)

type EvapCoolerNamesTarget = (
    EvaporativeCoolerDirectCelDekPad
    | EvaporativeCoolerDirectResearchSpecial
    | EvaporativeCoolerIndirectCelDekPad
    | EvaporativeCoolerIndirectResearchSpecial
    | EvaporativeCoolerIndirectWetCoil
)

type ExteriorLightsNamesTarget = ExteriorLights

type ExternalNodeNamesTarget = AirflowNetworkMultiZoneExternalNode

type FCAirSupNamesTarget = GeneratorFuelCellAirSupply

type FCAuxHeatNamesTarget = GeneratorFuelCellAuxiliaryHeater

type FCExhaustHXNamesTarget = GeneratorFuelCellExhaustGasToWaterHeatExchanger

type FCInverterNamesTarget = GeneratorFuelCellInverter

type FCPMNamesTarget = GeneratorFuelCellPowerModule

type FCStackCoolerNamesTarget = GeneratorFuelCellStackCooler

type FCStorageNamesTarget = GeneratorFuelCellElectricalStorage

type FCWaterSupNamesTarget = GeneratorFuelCellWaterSupply

type FMUFileNameTarget = ExternalInterfaceFunctionalMockupUnitImport

type FansTarget = (
    FanComponentModel
    | FanConstantVolume
    | FanOnOff
    | FanSystemModel
    | FanVariableVolume
)

type FansCVTarget = FanConstantVolume

type FansCVandOnOffTarget = FanConstantVolume | FanOnOff

type FansCVandOnOffandVAVTarget = FanConstantVolume | FanOnOff | FanVariableVolume

type FansCVandVAVTarget = FanConstantVolume | FanVariableVolume

type FansComponentModelTarget = FanComponentModel

type FansOnOffTarget = FanOnOff

type FansOnOffandVAVTarget = FanOnOff | FanVariableVolume

type FansSystemModelTarget = FanSystemModel

type FansVAVTarget = FanVariableVolume

type FansZoneExhaustTarget = FanZoneExhaust

type FlatPlatePVTParametersTarget = (
    SolarCollectorPerformancePhotovoltaicThermalBIPVT
    | SolarCollectorPerformancePhotovoltaicThermalSimple
)

type FlatPlateSolarCollectorParametersTarget = SolarCollectorPerformanceFlatPlate

type FloorSurfaceNamesTarget = (
    BuildingSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
)

type FluidAndGlycolNamesTarget = (
    FluidPropertiesGlycolConcentration | FluidPropertiesName
)

type FluidNamesTarget = FluidPropertiesName

type FluidPropertyTemperaturesTarget = FluidPropertiesTemperatures

type GenFuelSupNamesTarget = GeneratorFuelSupply

type GeneratorListsTarget = ElectricLoadCenterGenerators

type GeneratorNamesTarget = (
    GeneratorCombustionTurbine
    | GeneratorFuelCell
    | GeneratorInternalCombustionEngine
    | GeneratorMicroCHP
    | GeneratorMicroTurbine
    | GeneratorPVWatts
    | GeneratorPhotovoltaic
    | GeneratorWindTurbine
)

type GlazedExtSubSurfNamesTarget = FenestrationSurfaceDetailed | GlazedDoor | Window

type GlazingMaterialNameTarget = (
    WindowMaterialGlazing
    | WindowMaterialGlazingGroupThermochromic
    | WindowMaterialGlazingRefractionExtinctionMethod
    | WindowMaterialSimpleGlazingSystem
)

type GroundHeatExchangerVerticalArrayNamesTarget = GroundHeatExchangerVerticalArray

type GroundHeatExchangerVerticalPropertiesNamesTarget = (
    GroundHeatExchangerVerticalProperties
)

type GroundHeatExchangerVerticalResponseFactorNamesTarget = (
    GroundHeatExchangerResponseFactors
)

type GroundHeatExchangerVerticalSingleNamesTarget = GroundHeatExchangerVerticalSingle

type GroundHeatExchangerVerticalSizingNamesTarget = (
    GroundHeatExchangerVerticalSizingRectangle
)

type GroundSurfacesNamesTarget = SurfacePropertyGroundSurfaces

type HVACTemplateConstantVolumeZonesTarget = HVACTemplateZoneConstantVolume

type HVACTemplateDOASSystemsTarget = HVACTemplateSystemDedicatedOutdoorAir

type HVACTemplateSystemsTarget = (
    HVACTemplateSystemConstantVolume
    | HVACTemplateSystemDedicatedOutdoorAir
    | HVACTemplateSystemDualDuct
    | HVACTemplateSystemPackagedVAV
    | HVACTemplateSystemUnitary
    | HVACTemplateSystemUnitaryHeatPumpAirToAir
    | HVACTemplateSystemUnitarySystem
    | HVACTemplateSystemVAV
    | HVACTemplateSystemVRF
)

type HXAirToAirNamesTarget = (
    HeatExchangerAirToAirFlatPlate
    | HeatExchangerAirToAirSensibleAndLatent
    | HeatExchangerDesiccantBalancedFlow
)

type HXAirToAirSensibleAndLatentNamesTarget = HeatExchangerAirToAirSensibleAndLatent

type HXDesiccantBalancedTarget = HeatExchangerDesiccantBalancedFlow

type HeatPumpAirToWaterFuelFiredCoolingNamesTarget = HeatPumpAirToWaterFuelFiredCooling

type HeatPumpAirToWaterFuelFiredHeatingNamesTarget = HeatPumpAirToWaterFuelFiredHeating

type HeatPumpWaterHeaterDXCoilsPumpedTarget = CoilWaterHeatingAirToWaterHeatPumpPumped

type HeatPumpWaterHeaterDXCoilsVariableSpeedTarget = (
    CoilWaterHeatingAirToWaterHeatPumpVariableSpeed
)

type HeatPumpWaterHeaterDXCoilsWrappedTarget = CoilWaterHeatingAirToWaterHeatPumpWrapped

type HeatingCoilNameTarget = (
    CoilHeatingElectric | CoilHeatingFuel | CoilHeatingSteam | CoilHeatingWater
)

type HeatingCoilSystemNameTarget = CoilSystemHeatingDX

type HeatingCoilsDXTarget = (
    CoilHeatingDXSingleSpeed | CoilHeatingDXVariableRefrigerantFlow
)

type HeatingCoilsDXMultiSpeedTarget = CoilHeatingDXMultiSpeed

type HeatingCoilsDXSingleSpeedTarget = (
    CoilHeatingDXSingleSpeed | CoilHeatingDXVariableRefrigerantFlow
)

type HeatingCoilsDXVarRefrigFlowTarget = CoilHeatingDXVariableRefrigerantFlow

type HeatingCoilsDXVarRefrigFlowFluidTemperatureControlTarget = (
    CoilHeatingDXVariableRefrigerantFlowFluidTemperatureControl
)

type HeatingCoilsDXVariableSpeedTarget = CoilHeatingDXVariableSpeed

type HeatingCoilsDesuperheaterTarget = CoilHeatingDesuperheater

type HeatingCoilsElectricTarget = CoilHeatingElectric

type HeatingCoilsElectricMultiStageTarget = CoilHeatingElectricMultiStage

type HeatingCoilsGasMultiStageTarget = CoilHeatingGasMultiStage

type HeatingCoilsWaterTarget = CoilHeatingWater

type HeatingCoilsWaterToAirHPTarget = (
    CoilHeatingWaterToAirHeatPumpEquationFit
    | CoilHeatingWaterToAirHeatPumpParameterEstimation
)

type HeatingCoilsWaterToAirVSHPTarget = (
    CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit
)

type IceThermalStorageEquipmentTarget = (
    ThermalStorageIceDetailed | ThermalStorageIceSimple
)

type IndependentVariableListNameTarget = TableIndependentVariableList

type IndependentVariableNameTarget = TableIndependentVariable

type IntegratedHeatPumpsTarget = CoilSystemIntegratedHeatPumpAirSource

type InternalHeatSourceNamesTarget = ConstructionPropertyInternalHeatSource

type InverterListTarget = (
    ElectricLoadCenterInverterFunctionOfPower
    | ElectricLoadCenterInverterLookUpTable
    | ElectricLoadCenterInverterPVWatts
    | ElectricLoadCenterInverterSimple
)

type LightsNamesTarget = Lights

type MaterialNameTarget = (
    Material
    | MaterialAirGap
    | MaterialInfraredTransparent
    | MaterialNoMass
    | MaterialRoofVegetation
    | WindowMaterialBlind
    | WindowMaterialGas
    | WindowMaterialGasMixture
    | WindowMaterialGlazing
    | WindowMaterialGlazingGroupThermochromic
    | WindowMaterialGlazingRefractionExtinctionMethod
    | WindowMaterialScreen
    | WindowMaterialShade
    | WindowMaterialSimpleGlazingSystem
)

type MicroCHPParametersNamesTarget = GeneratorMicroCHPNonNormalizedParameters

type MicroTurbineGeneratorNamesTarget = GeneratorMicroTurbine

type MultivariateFunctionsTarget = TableLookup

type OAControllerNamesTarget = ControllerOutdoorAir

type OSCMNamesTarget = SurfacePropertyOtherSideConditionsModel

type OutFaceEnvNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingInterzone
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorDetailed
    | FloorInterzone
    | FoundationKiva
    | GlazedDoor
    | GlazedDoorInterzone
    | RoofCeilingDetailed
    | Space
    | SurfacePropertyOtherSideCoefficients
    | SurfacePropertyOtherSideConditionsModel
    | WallDetailed
    | WallInterzone
    | Window
    | WindowInterzone
    | Zone
)

type OutdoorAirMixersTarget = OutdoorAirMixer

type OutdoorAirNodeNamesTarget = OutdoorAirNode

type OutdoorAirUnitEquipmentListsTarget = ZoneHVACOutdoorAirUnitEquipmentList

type PLHPCoolingNamesTarget = HeatPumpPlantLoopEIRCooling

type PLHPHeatingNamesTarget = HeatPumpPlantLoopEIRHeating

type PVGeneratorNamesTarget = GeneratorPhotovoltaic

type PVModulesTarget = (
    PhotovoltaicPerformanceEquivalentOneDiode
    | PhotovoltaicPerformanceSandia
    | PhotovoltaicPerformanceSimple
)

type PeopleNamesTarget = People

type PipingSystemUndergroundCircuitNamesTarget = PipingSystemUndergroundPipeCircuit

type PipingSystemUndergroundSegmentNamesTarget = PipingSystemUndergroundPipeSegment

type PlantAndCondenserEquipmentListsTarget = CondenserEquipmentList | PlantEquipmentList

type PlantConnectorsTarget = ConnectorMixer | ConnectorSplitter

type PlantLoopsTarget = CondenserLoop | PlantLoop

type PlantOperationSchemesTarget = PlantEquipmentOperationSchemes

type ProgramNamesTarget = (
    EnergyManagementSystemProgramCallingManager | PythonPluginInstance
)

type QuadvariateFunctionsTarget = CurveQuadLinear | TableLookup

type QuintvariateFunctionsTarget = CurveQuintLinear | TableLookup

type RadiantDesignObjectTarget = (
    ZoneHVACBaseboardRadiantConvectiveWaterDesign
    | ZoneHVACLowTemperatureRadiantConstantFlowDesign
    | ZoneHVACLowTemperatureRadiantVariableFlowDesign
)

type RadiantGroupNamesTarget = ZoneHVACLowTemperatureRadiantSurfaceGroup

type RadiantSurfaceNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | InternalMass
    | Roof
    | RoofCeilingDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
)

type ReferenceCrackConditionsTarget = AirflowNetworkMultiZoneReferenceCrackConditions

type RefrigerationAirChillerNamesTarget = RefrigerationAirChiller

type RefrigerationAllTypesCondenserNamesTarget = (
    RefrigerationCondenserAirCooled
    | RefrigerationCondenserCascade
    | RefrigerationCondenserEvaporativeCooled
    | RefrigerationCondenserWaterCooled
)

type RefrigerationAllTypesGasCoolerNamesTarget = RefrigerationGasCoolerAirCooled

type RefrigerationCascadeCondenserAndSecondarySystemNamesTarget = (
    RefrigerationCondenserCascade | RefrigerationSecondarySystem
)

type RefrigerationCaseAndWalkInAndListNamesTarget = (
    RefrigerationAirChiller
    | RefrigerationCase
    | RefrigerationCaseAndWalkInList
    | RefrigerationWalkIn
)

type RefrigerationCaseAndWalkInNamesTarget = (
    RefrigerationAirChiller | RefrigerationCase | RefrigerationWalkIn
)

type RefrigerationCompressorAndListNamesTarget = (
    RefrigerationCompressor | RefrigerationCompressorList
)

type RefrigerationCompressorNamesTarget = RefrigerationCompressor

type RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNamesTarget = (
    RefrigerationCondenserCascade
    | RefrigerationSecondarySystem
    | RefrigerationTransferLoadList
)

type RefrigerationSubcoolerNamesTarget = RefrigerationSubcooler

type RefrigerationSystemNamesTarget = (
    RefrigerationSystem | RefrigerationTranscriticalSystem
)

type ReturnPathComponentNamesTarget = AirLoopHVACReturnPlenum | AirLoopHVACZoneMixer

type RoomAirNodeGainsTarget = RoomAirNodeAirflowNetworkInternalGains

type RoomAirNodeHVACEquipmentTarget = RoomAirNodeAirflowNetworkHVACEquipment

type RoomAirNodeSurfaceListsTarget = RoomAirNodeAirflowNetworkAdjacentSurfaceList

type RoomAirNodesTarget = RoomAirNode

type RoomAirflowNetworkNodesTarget = RoomAirNodeAirflowNetwork

type RunPeriodsAndDesignDaysTarget = (
    RunPeriod
    | SizingPeriodDesignDay
    | SizingPeriodWeatherFileConditionType
    | SizingPeriodWeatherFileDays
)

type ScheduleNamesTarget = (
    ExternalInterfaceFunctionalMockupUnitExportToSchedule
    | ExternalInterfaceFunctionalMockupUnitImportToSchedule
    | ExternalInterfaceSchedule
    | ScheduleCompact
    | ScheduleConstant
    | ScheduleFile
    | ScheduleYear
)

type ScheduleTypeLimitsNamesTarget = ScheduleTypeLimits

type SimpleCoilsTarget = CoilCoolingWater | CoilHeatingWater

type SizingPeriodWeatherFileDaysTarget = SizingPeriodWeatherFileDays

type SpaceAndSpaceListNamesTarget = Space | SpaceList

type SpaceListNamesTarget = SpaceList

type SpaceMixerNamesTarget = SpaceHVACZoneEquipmentMixer | SpaceHVACZoneReturnMixer

type SpaceNamesTarget = Space

type SpaceSplitterNamesTarget = SpaceHVACZoneEquipmentSplitter

type SpectralDataSetsTarget = MaterialPropertyGlazingSpectralData

type SpectrumDataNamesTarget = SiteSpectrumData

type SubSurfNamesTarget = (
    Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | GlazedDoor
    | GlazedDoorInterzone
    | Window
    | WindowInterzone
)

type SupplyPathComponentNamesTarget = AirLoopHVACSupplyPlenum | AirLoopHVACZoneSplitter

type SurfAndSubSurfNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | Door
    | DoorInterzone
    | FenestrationSurfaceDetailed
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | GlazedDoor
    | GlazedDoorInterzone
    | Roof
    | RoofCeilingDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
    | Window
    | WindowInterzone
)

type SurfaceAirflowLeakageNamesTarget = (
    AirflowNetworkMultiZoneComponentDetailedOpening
    | AirflowNetworkMultiZoneComponentHorizontalOpening
    | AirflowNetworkMultiZoneComponentSimpleOpening
    | AirflowNetworkMultiZoneComponentZoneExhaustFan
    | AirflowNetworkMultiZoneSpecifiedFlowRate
    | AirflowNetworkMultiZoneSurfaceCrack
    | AirflowNetworkMultiZoneSurfaceEffectiveLeakageArea
)

type SurfaceLocalEnvironmentNamesTarget = SurfacePropertyLocalEnvironment

type SurfaceNamesTarget = (
    BuildingSurfaceDetailed
    | CeilingAdiabatic
    | CeilingInterzone
    | FloorAdiabatic
    | FloorDetailed
    | FloorGroundContact
    | FloorInterzone
    | Roof
    | RoofCeilingDetailed
    | WallAdiabatic
    | WallDetailed
    | WallExterior
    | WallInterzone
    | WallUnderground
)

type SurfacePropUnderWaterNamesTarget = SurfacePropertyUnderwater

type SurroundingSurfacesNamesTarget = SurfacePropertySurroundingSurfaces

type SystemAvailabilityManagerListsTarget = AvailabilityManagerAssignmentList

type SystemAvailabilityManagersTarget = (
    AvailabilityManagerDifferentialThermostat
    | AvailabilityManagerHighTemperatureTurnOff
    | AvailabilityManagerHighTemperatureTurnOn
    | AvailabilityManagerHybridVentilation
    | AvailabilityManagerLowTemperatureTurnOff
    | AvailabilityManagerLowTemperatureTurnOn
    | AvailabilityManagerNightCycle
    | AvailabilityManagerNightVentilation
    | AvailabilityManagerOptimumStart
    | AvailabilityManagerScheduled
    | AvailabilityManagerScheduledOff
    | AvailabilityManagerScheduledOn
)

type ThermalComfortControlTypeNamesTarget = (
    ThermostatSetpointThermalComfortFangerDualSetpoint
    | ThermostatSetpointThermalComfortFangerSingleCooling
    | ThermostatSetpointThermalComfortFangerSingleHeating
    | ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling
)

type ThermalStorageSizingTarget = ThermalStorageSizing

type ThermalStorageWaterNamesTarget = (
    ThermalStorageChilledWaterMixed
    | ThermalStorageChilledWaterStratified
    | ThermalStorageHotWaterStratified
)

type ThermostatOffsetFaultsTarget = FaultModelThermostatOffset

type TransformerNamesTarget = ElectricLoadCenterTransformer

type TrivariateFunctionsTarget = (
    CurveChillerPartLoadWithLift | CurveTriquadratic | TableLookup
)

type UTSCNamesTarget = SolarCollectorUnglazedTranspired

type UndisturbedGroundTempModelsTarget = (
    SiteGroundTemperatureUndisturbedFiniteDifference
    | SiteGroundTemperatureUndisturbedKusudaAchenbach
    | SiteGroundTemperatureUndisturbedXing
)

type UnitarySystemPerformanceNamesTarget = UnitarySystemPerformanceMultispeed

type UnivariateFunctionsTarget = (
    CurveCubic
    | CurveDoubleExponentialDecay
    | CurveExponent
    | CurveExponentialDecay
    | CurveExponentialSkewNormal
    | CurveFunctionalPressureDrop
    | CurveLinear
    | CurveQuadratic
    | CurveQuartic
    | CurveRectangularHyperbola1
    | CurveRectangularHyperbola2
    | CurveSigmoid
    | TableLookup
)

type UserConvectionInsideModelsTarget = SurfaceConvectionAlgorithmInsideUserCurve

type UserConvectionModelsTarget = (
    SurfaceConvectionAlgorithmInsideUserCurve
    | SurfaceConvectionAlgorithmOutsideUserCurve
)

type UserConvectionOutsideModelsTarget = SurfaceConvectionAlgorithmOutsideUserCurve

type UserDefinedCoilTarget = CoilUserDefined

type UtilityCostTariffsTarget = UtilityCostTariff

type VariableSpeedTowerCoefficientTarget = (
    CoolingTowerPerformanceCoolTools | CoolingTowerPerformanceYorkCalc
)

type VentSlabGroupNamesTarget = ZoneHVACVentilatedSlabSlabGroup

type VentilationNamesTarget = (
    ZoneVentilationDesignFlowRate | ZoneVentilationWindandStackOpenArea
)

type WPCSetNamesTarget = AirflowNetworkMultiZoneWindPressureCoefficientArray

type WPCValueNamesTarget = AirflowNetworkMultiZoneWindPressureCoefficientValues

type WWHPCoolingNamesTarget = HeatPumpWaterToWaterEquationFitCooling

type WWHPHeatingNamesTarget = HeatPumpWaterToWaterEquationFitHeating

type WaterCoilControllersTarget = ControllerWaterCoil

type WaterHeaterMixedNamesTarget = WaterHeaterMixed

type WaterHeaterNamesTarget = WaterHeaterMixed | WaterHeaterStratified

type WaterHeaterStratifiedNamesTarget = WaterHeaterStratified

type WaterStorageTankNamesTarget = WaterUseStorage

type WaterUseEquipmentNamesTarget = WaterUseEquipment

type WeekScheduleNamesTarget = ScheduleWeekCompact | ScheduleWeekDaily

type WindowComplexShadesTarget = WindowMaterialComplexShade

type WindowEquivalentLayerMaterialNamesTarget = (
    WindowMaterialBlindEquivalentLayer
    | WindowMaterialDrapeEquivalentLayer
    | WindowMaterialGapEquivalentLayer
    | WindowMaterialGlazingEquivalentLayer
    | WindowMaterialScreenEquivalentLayer
    | WindowMaterialShadeEquivalentLayer
)

type WindowFrameAndDividerNamesTarget = WindowPropertyFrameAndDivider

type WindowGapDeflectionStatesTarget = WindowGapDeflectionState

type WindowGapSupportPillarsTarget = WindowGapSupportPillar

type WindowGasAndGasMixturesTarget = WindowMaterialGas | WindowMaterialGasMixture

type WindowShadeControlNamesTarget = WindowShadingControl

type WindowShadesScreensAndBlindsTarget = (
    WindowMaterialBlind | WindowMaterialScreen | WindowMaterialShade
)

type WindowThermalModelParametersTarget = WindowThermalModelParams

type ZoneAndZoneListAndSpaceAndSpaceListNamesTarget = (
    Space | SpaceList | Zone | ZoneList
)

type ZoneAndZoneListNamesTarget = Zone | ZoneList

type ZoneControlHumidistatNamesTarget = ZoneControlHumidistat

type ZoneControlThermostaticNamesTarget = (
    ZoneControlThermostat | ZoneControlThermostatStagedDualSetpoint
)

type ZoneEquipmentListsTarget = ZoneHVACEquipmentList

type ZoneEquipmentNamesTarget = (
    AirLoopHVACUnitarySystem
    | FanZoneExhaust
    | HeatExchangerAirToAirFlatPlate
    | WaterHeaterHeatPumpPumpedCondenser
    | WaterHeaterHeatPumpWrappedCondenser
    | ZoneHVACAirDistributionUnit
    | ZoneHVACBaseboardConvectiveElectric
    | ZoneHVACBaseboardConvectiveWater
    | ZoneHVACBaseboardRadiantConvectiveElectric
    | ZoneHVACBaseboardRadiantConvectiveSteam
    | ZoneHVACBaseboardRadiantConvectiveSteamDesign
    | ZoneHVACBaseboardRadiantConvectiveWater
    | ZoneHVACCoolingPanelRadiantConvectiveWater
    | ZoneHVACDehumidifierDX
    | ZoneHVACEnergyRecoveryVentilator
    | ZoneHVACEvaporativeCoolerUnit
    | ZoneHVACForcedAirUserDefined
    | ZoneHVACFourPipeFanCoil
    | ZoneHVACHighTemperatureRadiant
    | ZoneHVACHybridUnitaryHVAC
    | ZoneHVACIdealLoadsAirSystem
    | ZoneHVACLowTemperatureRadiantConstantFlow
    | ZoneHVACLowTemperatureRadiantElectric
    | ZoneHVACLowTemperatureRadiantVariableFlow
    | ZoneHVACOutdoorAirUnit
    | ZoneHVACPackagedTerminalAirConditioner
    | ZoneHVACPackagedTerminalHeatPump
    | ZoneHVACRefrigerationChillerSet
    | ZoneHVACTerminalUnitVariableRefrigerantFlow
    | ZoneHVACUnitHeater
    | ZoneHVACUnitVentilator
    | ZoneHVACVentilatedSlab
    | ZoneHVACWaterToAirHeatPump
    | ZoneHVACWindowAirConditioner
)

type ZoneListNamesTarget = ZoneList

type ZoneLocalEnvironmentNamesTarget = ZonePropertyLocalEnvironment

type ZoneMixersTarget = AirLoopHVACZoneMixer

type ZoneNamesTarget = Zone

type ZoneTerminalUnitListNamesTarget = ZoneTerminalUnitList

type ZoneTerminalUnitNamesTarget = ZoneHVACTerminalUnitVariableRefrigerantFlow

type ValidBranchEquipmentNamesTarget = (
    AirConditionerVariableRefrigerantFlow
    | AirLoopHVACOutdoorAirSystem
    | AirLoopHVACUnitaryFurnaceHeatCool
    | AirLoopHVACUnitaryFurnaceHeatOnly
    | AirLoopHVACUnitaryHeatCool
    | AirLoopHVACUnitaryHeatCoolVAVChangeoverBypass
    | AirLoopHVACUnitaryHeatOnly
    | AirLoopHVACUnitaryHeatPumpAirToAir
    | AirLoopHVACUnitaryHeatPumpAirToAirMultiSpeed
    | AirLoopHVACUnitaryHeatPumpWaterToAir
    | AirLoopHVACUnitarySystem
    | AirTerminalSingleDuctConstantVolumeCooledBeam
    | AirTerminalSingleDuctConstantVolumeFourPipeBeam
    | AirTerminalSingleDuctUserDefined
    | BoilerHotWater
    | BoilerSteam
    | CentralHeatPumpSystem
    | ChillerAbsorption
    | ChillerAbsorptionIndirect
    | ChillerCombustionTurbine
    | ChillerConstantCOP
    | ChillerElectric
    | ChillerElectricASHRAE205
    | ChillerElectricEIR
    | ChillerElectricReformulatedEIR
    | ChillerEngineDriven
    | ChillerHeaterAbsorptionDirectFired
    | ChillerHeaterAbsorptionDoubleEffect
    | CoilCoolingDXSingleSpeedThermalStorage
    | CoilCoolingWater
    | CoilCoolingWaterDetailedGeometry
    | CoilCoolingWaterToAirHeatPumpEquationFit
    | CoilCoolingWaterToAirHeatPumpParameterEstimation
    | CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit
    | CoilHeatingDesuperheater
    | CoilHeatingElectric
    | CoilHeatingFuel
    | CoilHeatingSteam
    | CoilHeatingWater
    | CoilHeatingWaterToAirHeatPumpEquationFit
    | CoilHeatingWaterToAirHeatPumpParameterEstimation
    | CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit
    | CoilSystemCoolingDX
    | CoilSystemCoolingWater
    | CoilSystemCoolingWaterHeatExchangerAssisted
    | CoilSystemHeatingDX
    | CoilUserDefined
    | CoolingTowerSingleSpeed
    | CoolingTowerTwoSpeed
    | CoolingTowerVariableSpeed
    | CoolingTowerVariableSpeedMerkel
    | DehumidifierDesiccantNoFans
    | DehumidifierDesiccantSystem
    | DistrictCooling
    | DistrictHeatingSteam
    | DistrictHeatingWater
    | Duct
    | EvaporativeCoolerDirectCelDekPad
    | EvaporativeCoolerDirectResearchSpecial
    | EvaporativeCoolerIndirectCelDekPad
    | EvaporativeCoolerIndirectResearchSpecial
    | EvaporativeCoolerIndirectWetCoil
    | EvaporativeFluidCoolerSingleSpeed
    | EvaporativeFluidCoolerTwoSpeed
    | FanComponentModel
    | FanConstantVolume
    | FanSystemModel
    | FanVariableVolume
    | FluidCoolerSingleSpeed
    | FluidCoolerTwoSpeed
    | GeneratorCombustionTurbine
    | GeneratorFuelCellExhaustGasToWaterHeatExchanger
    | GeneratorFuelCellStackCooler
    | GeneratorInternalCombustionEngine
    | GeneratorMicroCHP
    | GeneratorMicroTurbine
    | GroundHeatExchangerHorizontalTrench
    | GroundHeatExchangerPond
    | GroundHeatExchangerSlinky
    | GroundHeatExchangerSurface
    | GroundHeatExchangerSystem
    | HeaderedPumpsConstantSpeed
    | HeaderedPumpsVariableSpeed
    | HeatExchangerAirToAirFlatPlate
    | HeatExchangerAirToAirSensibleAndLatent
    | HeatExchangerDesiccantBalancedFlow
    | HeatExchangerFluidToFluid
    | HeatPumpAirToWater
    | HeatPumpAirToWaterFuelFiredCooling
    | HeatPumpAirToWaterFuelFiredHeating
    | HeatPumpPlantLoopEIRCooling
    | HeatPumpPlantLoopEIRHeating
    | HeatPumpWaterToWaterEquationFitCooling
    | HeatPumpWaterToWaterEquationFitHeating
    | HeatPumpWaterToWaterParameterEstimationCooling
    | HeatPumpWaterToWaterParameterEstimationHeating
    | HumidifierSteamElectric
    | HumidifierSteamGas
    | LoadProfilePlant
    | PipeAdiabatic
    | PipeAdiabaticSteam
    | PipeIndoor
    | PipeOutdoor
    | PipeUnderground
    | PipingSystemUndergroundPipeCircuit
    | PlantComponentTemperatureSource
    | PlantComponentUserDefined
    | PumpConstantSpeed
    | PumpVariableSpeed
    | PumpVariableSpeedCondensate
    | RefrigerationCompressorRack
    | RefrigerationCondenserWaterCooled
    | SolarCollectorFlatPlatePhotovoltaicThermal
    | SolarCollectorFlatPlateWater
    | SolarCollectorIntegralCollectorStorage
    | SwimmingPoolIndoor
    | TemperingValve
    | ThermalStorageChilledWaterMixed
    | ThermalStorageChilledWaterStratified
    | ThermalStorageHotWaterStratified
    | ThermalStorageIceDetailed
    | ThermalStorageIceSimple
    | ThermalStoragePCM
    | WaterHeaterHeatPumpPumpedCondenser
    | WaterHeaterHeatPumpWrappedCondenser
    | WaterHeaterMixed
    | WaterHeaterStratified
    | WaterUseConnections
    | ZoneHVACBaseboardConvectiveWater
    | ZoneHVACBaseboardRadiantConvectiveSteam
    | ZoneHVACBaseboardRadiantConvectiveSteamDesign
    | ZoneHVACBaseboardRadiantConvectiveWater
    | ZoneHVACCoolingPanelRadiantConvectiveWater
    | ZoneHVACForcedAirUserDefined
    | ZoneHVACLowTemperatureRadiantConstantFlow
    | ZoneHVACLowTemperatureRadiantVariableFlow
    | ZoneHVACTerminalUnitVariableRefrigerantFlow
)

type ValidCondenserEquipmentNamesTarget = (
    CoolingTowerSingleSpeed
    | CoolingTowerTwoSpeed
    | CoolingTowerVariableSpeed
    | CoolingTowerVariableSpeedMerkel
    | DistrictCooling
    | DistrictHeatingSteam
    | DistrictHeatingWater
    | EvaporativeFluidCoolerSingleSpeed
    | EvaporativeFluidCoolerTwoSpeed
    | FluidCoolerSingleSpeed
    | FluidCoolerTwoSpeed
    | GeneratorMicroTurbine
    | GroundHeatExchangerHorizontalTrench
    | GroundHeatExchangerPond
    | GroundHeatExchangerSlinky
    | GroundHeatExchangerSurface
    | GroundHeatExchangerSystem
    | HeatExchangerFluidToFluid
    | PipingSystemUndergroundPipeCircuit
    | PlantComponentTemperatureSource
    | PlantComponentUserDefined
    | TemperingValve
    | ThermalStorageChilledWaterMixed
    | ThermalStorageChilledWaterStratified
    | ThermalStorageHotWaterStratified
    | WaterHeaterMixed
    | WaterHeaterStratified
)

type ValidOASysEquipmentNamesTarget = (
    AirLoopHVACUnitarySystem
    | CoilCoolingWater
    | CoilCoolingWaterDetailedGeometry
    | CoilHeatingElectric
    | CoilHeatingFuel
    | CoilHeatingSteam
    | CoilHeatingWater
    | CoilSystemCoolingDX
    | CoilSystemCoolingWater
    | CoilSystemCoolingWaterHeatExchangerAssisted
    | CoilSystemHeatingDX
    | CoilUserDefined
    | DehumidifierDesiccantNoFans
    | DehumidifierDesiccantSystem
    | EvaporativeCoolerDirectCelDekPad
    | EvaporativeCoolerDirectResearchSpecial
    | EvaporativeCoolerIndirectCelDekPad
    | EvaporativeCoolerIndirectResearchSpecial
    | EvaporativeCoolerIndirectWetCoil
    | FanComponentModel
    | FanConstantVolume
    | FanSystemModel
    | FanVariableVolume
    | HeatExchangerAirToAirFlatPlate
    | HeatExchangerAirToAirSensibleAndLatent
    | HeatExchangerDesiccantBalancedFlow
    | HumidifierSteamElectric
    | HumidifierSteamGas
    | OutdoorAirMixer
    | SolarCollectorFlatPlatePhotovoltaicThermal
    | SolarCollectorUnglazedTranspired
    | ZoneHVACTerminalUnitVariableRefrigerantFlow
)

type ValidPlantEquipmentNamesTarget = (
    BoilerHotWater
    | BoilerSteam
    | CentralHeatPumpSystem
    | ChillerAbsorption
    | ChillerAbsorptionIndirect
    | ChillerCombustionTurbine
    | ChillerConstantCOP
    | ChillerElectric
    | ChillerElectricASHRAE205
    | ChillerElectricEIR
    | ChillerElectricReformulatedEIR
    | ChillerEngineDriven
    | ChillerHeaterAbsorptionDirectFired
    | ChillerHeaterAbsorptionDoubleEffect
    | CoolingTowerSingleSpeed
    | CoolingTowerTwoSpeed
    | CoolingTowerVariableSpeed
    | CoolingTowerVariableSpeedMerkel
    | DistrictCooling
    | DistrictHeatingSteam
    | DistrictHeatingWater
    | EvaporativeFluidCoolerSingleSpeed
    | EvaporativeFluidCoolerTwoSpeed
    | FluidCoolerSingleSpeed
    | FluidCoolerTwoSpeed
    | GeneratorFuelCellExhaustGasToWaterHeatExchanger
    | GeneratorMicroCHP
    | GeneratorMicroTurbine
    | GroundHeatExchangerHorizontalTrench
    | GroundHeatExchangerPond
    | GroundHeatExchangerSlinky
    | GroundHeatExchangerSurface
    | GroundHeatExchangerSystem
    | HeatExchangerFluidToFluid
    | HeatPumpAirToWater
    | HeatPumpPlantLoopEIRCooling
    | HeatPumpPlantLoopEIRHeating
    | HeatPumpWaterToWaterEquationFitCooling
    | HeatPumpWaterToWaterEquationFitHeating
    | HeatPumpWaterToWaterParameterEstimationCooling
    | HeatPumpWaterToWaterParameterEstimationHeating
    | PipingSystemUndergroundPipeCircuit
    | PlantComponentTemperatureSource
    | PlantComponentUserDefined
    | SolarCollectorFlatPlatePhotovoltaicThermal
    | SolarCollectorFlatPlateWater
    | SolarCollectorIntegralCollectorStorage
    | TemperingValve
    | ThermalStorageChilledWaterMixed
    | ThermalStorageChilledWaterStratified
    | ThermalStorageHotWaterStratified
    | ThermalStorageIceDetailed
    | ThermalStoragePCM
    | WaterHeaterHeatPumpPumpedCondenser
    | WaterHeaterHeatPumpWrappedCondenser
    | WaterHeaterMixed
    | WaterHeaterStratified
)
