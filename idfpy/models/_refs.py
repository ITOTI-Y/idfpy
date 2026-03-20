"""Auto-generated reference types for EnergyPlus object validation.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.

This module provides type aliases with runtime validation for object
references. Use with validation context for reference checking.
"""
from __future__ import annotations

from typing import Annotated, Any

from pydantic import BeforeValidator
from pydantic_core import core_schema


class RefValidator:
    """Reference validator for EnergyPlus object lists.

    When used with validation context containing an IDF instance,
    validates that referenced object names exist in the registry.
    """

    def __init__(self, object_list: str):
        self.object_list = object_list

    def __call__(self, v: Any) -> str | None:
        """Validate reference value.

        Note: Context-based validation happens in IDF.add().
        This basic validator just ensures string conversion.
        """
        if v is None:
            return None
        return str(v)

    def __get_pydantic_core_schema__(self, source_type, handler):
        """Generate Pydantic core schema for this validator."""
        return core_schema.no_info_before_validator_function(
            self,
            core_schema.str_schema(),
        )

    def __repr__(self) -> str:
        return f"RefValidator({self.object_list!r})"


# ============================================================
# Reference type aliases
# ============================================================

AFNCoilNamesRef = Annotated[str, BeforeValidator(RefValidator("AFNCoilNames"))]
AFNHeatExchangerNamesRef = Annotated[str, BeforeValidator(RefValidator("AFNHeatExchangerNames"))]
AFNReliefAirFlowNamesRef = Annotated[str, BeforeValidator(RefValidator("AFNReliefAirFlowNames"))]
AFNTerminalUnitNamesRef = Annotated[str, BeforeValidator(RefValidator("AFNTerminalUnitNames"))]
AirFlowNetworkMultizoneZonesRef = Annotated[str, BeforeValidator(RefValidator("AirFlowNetworkMultizoneZones"))]
AirLoopControllersRef = Annotated[str, BeforeValidator(RefValidator("AirLoopControllers"))]
AirLoopHVACMixerNamesRef = Annotated[str, BeforeValidator(RefValidator("AirLoopHVACMixerNames"))]
AirLoopHVACSplitterNamesRef = Annotated[str, BeforeValidator(RefValidator("AirLoopHVACSplitterNames"))]
AirLoopOAEquipmentListsRef = Annotated[str, BeforeValidator(RefValidator("AirLoopOAEquipmentLists"))]
AirPrimaryLoopsRef = Annotated[str, BeforeValidator(RefValidator("AirPrimaryLoops"))]
AirTerminalUnitNamesRef = Annotated[str, BeforeValidator(RefValidator("AirTerminalUnitNames"))]
AirflowNetworkComponentNamesRef = Annotated[str, BeforeValidator(RefValidator("AirflowNetworkComponentNames"))]
AirflowNetworkNodeAndZoneNamesRef = Annotated[str, BeforeValidator(RefValidator("AirflowNetworkNodeAndZoneNames"))]
AirflowNetworkNodeNamesRef = Annotated[str, BeforeValidator(RefValidator("AirflowNetworkNodeNames"))]
AirflowNetworkOccupantVentilationControlNamesRef = Annotated[str, BeforeValidator(RefValidator("AirflowNetworkOccupantVentilationControlNames"))]
AllHeatTranAngFacNamesRef = Annotated[str, BeforeValidator(RefValidator("AllHeatTranAngFacNames"))]
AllHeatTranSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("AllHeatTranSurfNames"))]
AllShadingAndHTSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("AllShadingAndHTSurfNames"))]
AllShadingSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("AllShadingSurfNames"))]
AttachedShadingSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("AttachedShadingSurfNames"))]
BaseboardDesignObjectRef = Annotated[str, BeforeValidator(RefValidator("BaseboardDesignObject"))]
BiVariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("BiVariateFunctions"))]
BivariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("BivariateFunctions"))]
BoilersRef = Annotated[str, BeforeValidator(RefValidator("Boilers"))]
BranchListsRef = Annotated[str, BeforeValidator(RefValidator("BranchLists"))]
BranchesRef = Annotated[str, BeforeValidator(RefValidator("Branches"))]
CFSGapRef = Annotated[str, BeforeValidator(RefValidator("CFSGap"))]
CFSGlazingNameRef = Annotated[str, BeforeValidator(RefValidator("CFSGlazingName"))]
ChillerHeaterEIRNamesRef = Annotated[str, BeforeValidator(RefValidator("ChillerHeaterEIRNames"))]
ChillersRef = Annotated[str, BeforeValidator(RefValidator("Chillers"))]
CoilCoolingDXRef = Annotated[str, BeforeValidator(RefValidator("CoilCoolingDX"))]
CoilPerformanceDXRef = Annotated[str, BeforeValidator(RefValidator("CoilPerformanceDX"))]
CollectorStoragePerformanceRef = Annotated[str, BeforeValidator(RefValidator("CollectorStoragePerformance"))]
ColorSchemesRef = Annotated[str, BeforeValidator(RefValidator("ColorSchemes"))]
CompactHVACSystemConstantVolumeRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACSystemConstantVolume"))]
CompactHVACSystemDualDuctRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACSystemDualDuct"))]
CompactHVACSystemUnitaryRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACSystemUnitary"))]
CompactHVACSystemVAVRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACSystemVAV"))]
CompactHVACSystemVRFRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACSystemVRF"))]
CompactHVACThermostatsRef = Annotated[str, BeforeValidator(RefValidator("CompactHVACThermostats"))]
ComplexFenestrationStatesRef = Annotated[str, BeforeValidator(RefValidator("ComplexFenestrationStates"))]
CondenserOperationSchemesRef = Annotated[str, BeforeValidator(RefValidator("CondenserOperationSchemes"))]
ConnectorListsRef = Annotated[str, BeforeValidator(RefValidator("ConnectorLists"))]
ConstructionNamesRef = Annotated[str, BeforeValidator(RefValidator("ConstructionNames"))]
ControlSchemeListRef = Annotated[str, BeforeValidator(RefValidator("ControlSchemeList"))]
ControlTypeNamesRef = Annotated[str, BeforeValidator(RefValidator("ControlTypeNames"))]
ControllerListsRef = Annotated[str, BeforeValidator(RefValidator("ControllerLists"))]
ControllerMechanicalVentNamesRef = Annotated[str, BeforeValidator(RefValidator("ControllerMechanicalVentNames"))]
ControllerStandAloneEnergyRecoveryVentilatorRef = Annotated[str, BeforeValidator(RefValidator("ControllerStandAloneEnergyRecoveryVentilator"))]
ConverterListRef = Annotated[str, BeforeValidator(RefValidator("ConverterList"))]
CoolingCoilNameRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilName"))]
CoolingCoilSystemNameRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilSystemName"))]
CoolingCoilsDXRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDX"))]
CoolingCoilsDXMultiModeOrSingleSpeedRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXMultiModeOrSingleSpeed"))]
CoolingCoilsDXMultiSpeedRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXMultiSpeed"))]
CoolingCoilsDXSingleSpeedRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXSingleSpeed"))]
CoolingCoilsDXVarRefrigFlowRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXVarRefrigFlow"))]
CoolingCoilsDXVarRefrigFlowFluidTemperatureControlRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXVarRefrigFlowFluidTemperatureControl"))]
CoolingCoilsDXVariableSpeedRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsDXVariableSpeed"))]
CoolingCoilsWaterRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsWater"))]
CoolingCoilsWaterNoHXRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsWaterNoHX"))]
CoolingCoilsWaterToAirHPRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsWaterToAirHP"))]
CoolingCoilsWaterToAirVSHPRef = Annotated[str, BeforeValidator(RefValidator("CoolingCoilsWaterToAirVSHP"))]
CoolingTowersRef = Annotated[str, BeforeValidator(RefValidator("CoolingTowers"))]
CoolingTowersWithUARef = Annotated[str, BeforeValidator(RefValidator("CoolingTowersWithUA"))]
DOAToZonalUnitRef = Annotated[str, BeforeValidator(RefValidator("DOAToZonalUnit"))]
DSOASpaceListNamesRef = Annotated[str, BeforeValidator(RefValidator("DSOASpaceListNames"))]
DXCoolingOperatingModeNamesRef = Annotated[str, BeforeValidator(RefValidator("DXCoolingOperatingModeNames"))]
DXCoolingPerformanceNamesRef = Annotated[str, BeforeValidator(RefValidator("DXCoolingPerformanceNames"))]
DXCoolingSpeedNamesRef = Annotated[str, BeforeValidator(RefValidator("DXCoolingSpeedNames"))]
DataMatricesRef = Annotated[str, BeforeValidator(RefValidator("DataMatrices"))]
DayScheduleNamesRef = Annotated[str, BeforeValidator(RefValidator("DayScheduleNames"))]
DaylightReferencePointNamesRef = Annotated[str, BeforeValidator(RefValidator("DaylightReferencePointNames"))]
DaylightingControlNamesRef = Annotated[str, BeforeValidator(RefValidator("DaylightingControlNames"))]
DemandManagerNamesRef = Annotated[str, BeforeValidator(RefValidator("DemandManagerNames"))]
DesiccantHXPerfDataRef = Annotated[str, BeforeValidator(RefValidator("DesiccantHXPerfData"))]
DesignSpecificationAirTerminalSizingNameRef = Annotated[str, BeforeValidator(RefValidator("DesignSpecificationAirTerminalSizingName"))]
DesignSpecificationOutdoorAirNamesRef = Annotated[str, BeforeValidator(RefValidator("DesignSpecificationOutdoorAirNames"))]
DesignSpecificationZoneAirDistributionNamesRef = Annotated[str, BeforeValidator(RefValidator("DesignSpecificationZoneAirDistributionNames"))]
DesignSpecificationZoneHVACSizingNameRef = Annotated[str, BeforeValidator(RefValidator("DesignSpecificationZoneHVACSizingName"))]
DesuperHeatingCoilSourcesRef = Annotated[str, BeforeValidator(RefValidator("DesuperHeatingCoilSources"))]
DesuperHeatingWaterOnlySourcesRef = Annotated[str, BeforeValidator(RefValidator("DesuperHeatingWaterOnlySources"))]
EarthTubeParameterNamesRef = Annotated[str, BeforeValidator(RefValidator("EarthTubeParameterNames"))]
ElecStorageListRef = Annotated[str, BeforeValidator(RefValidator("ElecStorageList"))]
ElectricEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("ElectricEquipmentNames"))]
ErlProgramNamesRef = Annotated[str, BeforeValidator(RefValidator("ErlProgramNames"))]
EvapCoolerNamesRef = Annotated[str, BeforeValidator(RefValidator("EvapCoolerNames"))]
ExteriorLightsNamesRef = Annotated[str, BeforeValidator(RefValidator("ExteriorLightsNames"))]
ExternalNodeNamesRef = Annotated[str, BeforeValidator(RefValidator("ExternalNodeNames"))]
FCAirSupNamesRef = Annotated[str, BeforeValidator(RefValidator("FCAirSupNames"))]
FCAuxHeatNamesRef = Annotated[str, BeforeValidator(RefValidator("FCAuxHeatNames"))]
FCExhaustHXNamesRef = Annotated[str, BeforeValidator(RefValidator("FCExhaustHXNames"))]
FCInverterNamesRef = Annotated[str, BeforeValidator(RefValidator("FCInverterNames"))]
FCPMNamesRef = Annotated[str, BeforeValidator(RefValidator("FCPMNames"))]
FCStackCoolerNamesRef = Annotated[str, BeforeValidator(RefValidator("FCStackCoolerNames"))]
FCStorageNamesRef = Annotated[str, BeforeValidator(RefValidator("FCStorageNames"))]
FCWaterSupNamesRef = Annotated[str, BeforeValidator(RefValidator("FCWaterSupNames"))]
FMUFileNameRef = Annotated[str, BeforeValidator(RefValidator("FMUFileName"))]
FansRef = Annotated[str, BeforeValidator(RefValidator("Fans"))]
FansCVRef = Annotated[str, BeforeValidator(RefValidator("FansCV"))]
FansCVandOnOffRef = Annotated[str, BeforeValidator(RefValidator("FansCVandOnOff"))]
FansCVandOnOffandVAVRef = Annotated[str, BeforeValidator(RefValidator("FansCVandOnOffandVAV"))]
FansCVandVAVRef = Annotated[str, BeforeValidator(RefValidator("FansCVandVAV"))]
FansComponentModelRef = Annotated[str, BeforeValidator(RefValidator("FansComponentModel"))]
FansOnOffRef = Annotated[str, BeforeValidator(RefValidator("FansOnOff"))]
FansOnOffandVAVRef = Annotated[str, BeforeValidator(RefValidator("FansOnOffandVAV"))]
FansSystemModelRef = Annotated[str, BeforeValidator(RefValidator("FansSystemModel"))]
FansVAVRef = Annotated[str, BeforeValidator(RefValidator("FansVAV"))]
FansZoneExhaustRef = Annotated[str, BeforeValidator(RefValidator("FansZoneExhaust"))]
FlatPlatePVTParametersRef = Annotated[str, BeforeValidator(RefValidator("FlatPlatePVTParameters"))]
FlatPlateSolarCollectorParametersRef = Annotated[str, BeforeValidator(RefValidator("FlatPlateSolarCollectorParameters"))]
FloorSurfaceNamesRef = Annotated[str, BeforeValidator(RefValidator("FloorSurfaceNames"))]
FluidAndGlycolNamesRef = Annotated[str, BeforeValidator(RefValidator("FluidAndGlycolNames"))]
FluidNamesRef = Annotated[str, BeforeValidator(RefValidator("FluidNames"))]
FluidPropertyTemperaturesRef = Annotated[str, BeforeValidator(RefValidator("FluidPropertyTemperatures"))]
GenFuelSupNamesRef = Annotated[str, BeforeValidator(RefValidator("GenFuelSupNames"))]
GeneratorListsRef = Annotated[str, BeforeValidator(RefValidator("GeneratorLists"))]
GeneratorNamesRef = Annotated[str, BeforeValidator(RefValidator("GeneratorNames"))]
GlazedExtSubSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("GlazedExtSubSurfNames"))]
GlazingMaterialNameRef = Annotated[str, BeforeValidator(RefValidator("GlazingMaterialName"))]
GroundHeatExchangerVerticalArrayNamesRef = Annotated[str, BeforeValidator(RefValidator("GroundHeatExchangerVerticalArrayNames"))]
GroundHeatExchangerVerticalPropertiesNamesRef = Annotated[str, BeforeValidator(RefValidator("GroundHeatExchangerVerticalPropertiesNames"))]
GroundHeatExchangerVerticalResponseFactorNamesRef = Annotated[str, BeforeValidator(RefValidator("GroundHeatExchangerVerticalResponseFactorNames"))]
GroundHeatExchangerVerticalSingleNamesRef = Annotated[str, BeforeValidator(RefValidator("GroundHeatExchangerVerticalSingleNames"))]
GroundSurfacesNamesRef = Annotated[str, BeforeValidator(RefValidator("GroundSurfacesNames"))]
HVACTemplateConstantVolumeZonesRef = Annotated[str, BeforeValidator(RefValidator("HVACTemplateConstantVolumeZones"))]
HVACTemplateDOASSystemsRef = Annotated[str, BeforeValidator(RefValidator("HVACTemplateDOASSystems"))]
HVACTemplateSystemsRef = Annotated[str, BeforeValidator(RefValidator("HVACTemplateSystems"))]
HXAirToAirNamesRef = Annotated[str, BeforeValidator(RefValidator("HXAirToAirNames"))]
HXAirToAirSensibleAndLatentNamesRef = Annotated[str, BeforeValidator(RefValidator("HXAirToAirSensibleAndLatentNames"))]
HXDesiccantBalancedRef = Annotated[str, BeforeValidator(RefValidator("HXDesiccantBalanced"))]
HeatPumpAirToWaterFuelFiredCoolingNamesRef = Annotated[str, BeforeValidator(RefValidator("HeatPumpAirToWaterFuelFiredCoolingNames"))]
HeatPumpAirToWaterFuelFiredHeatingNamesRef = Annotated[str, BeforeValidator(RefValidator("HeatPumpAirToWaterFuelFiredHeatingNames"))]
HeatPumpWaterHeaterDXCoilsPumpedRef = Annotated[str, BeforeValidator(RefValidator("HeatPumpWaterHeaterDXCoilsPumped"))]
HeatPumpWaterHeaterDXCoilsVariableSpeedRef = Annotated[str, BeforeValidator(RefValidator("HeatPumpWaterHeaterDXCoilsVariableSpeed"))]
HeatPumpWaterHeaterDXCoilsWrappedRef = Annotated[str, BeforeValidator(RefValidator("HeatPumpWaterHeaterDXCoilsWrapped"))]
HeatingCoilNameRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilName"))]
HeatingCoilSystemNameRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilSystemName"))]
HeatingCoilsDXRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDX"))]
HeatingCoilsDXMultiSpeedRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDXMultiSpeed"))]
HeatingCoilsDXSingleSpeedRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDXSingleSpeed"))]
HeatingCoilsDXVarRefrigFlowRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDXVarRefrigFlow"))]
HeatingCoilsDXVarRefrigFlowFluidTemperatureControlRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDXVarRefrigFlowFluidTemperatureControl"))]
HeatingCoilsDXVariableSpeedRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDXVariableSpeed"))]
HeatingCoilsDesuperheaterRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsDesuperheater"))]
HeatingCoilsElectricRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsElectric"))]
HeatingCoilsElectricMultiStageRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsElectricMultiStage"))]
HeatingCoilsGasMultiStageRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsGasMultiStage"))]
HeatingCoilsWaterRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsWater"))]
HeatingCoilsWaterToAirHPRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsWaterToAirHP"))]
HeatingCoilsWaterToAirVSHPRef = Annotated[str, BeforeValidator(RefValidator("HeatingCoilsWaterToAirVSHP"))]
IceThermalStorageEquipmentRef = Annotated[str, BeforeValidator(RefValidator("IceThermalStorageEquipment"))]
IndependentVariableListNameRef = Annotated[str, BeforeValidator(RefValidator("IndependentVariableListName"))]
IndependentVariableNameRef = Annotated[str, BeforeValidator(RefValidator("IndependentVariableName"))]
IntegratedHeatPumpsRef = Annotated[str, BeforeValidator(RefValidator("IntegratedHeatPumps"))]
InverterListRef = Annotated[str, BeforeValidator(RefValidator("InverterList"))]
LightsNamesRef = Annotated[str, BeforeValidator(RefValidator("LightsNames"))]
MaterialNameRef = Annotated[str, BeforeValidator(RefValidator("MaterialName"))]
MicroCHPParametersNamesRef = Annotated[str, BeforeValidator(RefValidator("MicroCHPParametersNames"))]
MicroTurbineGeneratorNamesRef = Annotated[str, BeforeValidator(RefValidator("MicroTurbineGeneratorNames"))]
MultivariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("MultivariateFunctions"))]
OAControllerNamesRef = Annotated[str, BeforeValidator(RefValidator("OAControllerNames"))]
OSCMNamesRef = Annotated[str, BeforeValidator(RefValidator("OSCMNames"))]
OutFaceEnvNamesRef = Annotated[str, BeforeValidator(RefValidator("OutFaceEnvNames"))]
OutdoorAirMixersRef = Annotated[str, BeforeValidator(RefValidator("OutdoorAirMixers"))]
OutdoorAirNodeNamesRef = Annotated[str, BeforeValidator(RefValidator("OutdoorAirNodeNames"))]
OutdoorAirUnitEquipmentListsRef = Annotated[str, BeforeValidator(RefValidator("OutdoorAirUnitEquipmentLists"))]
PLHPCoolingNamesRef = Annotated[str, BeforeValidator(RefValidator("PLHPCoolingNames"))]
PLHPHeatingNamesRef = Annotated[str, BeforeValidator(RefValidator("PLHPHeatingNames"))]
PVGeneratorNamesRef = Annotated[str, BeforeValidator(RefValidator("PVGeneratorNames"))]
PVModulesRef = Annotated[str, BeforeValidator(RefValidator("PVModules"))]
PeopleNamesRef = Annotated[str, BeforeValidator(RefValidator("PeopleNames"))]
PipingSystemUndergroundCircuitNamesRef = Annotated[str, BeforeValidator(RefValidator("PipingSystemUndergroundCircuitNames"))]
PipingSystemUndergroundSegmentNamesRef = Annotated[str, BeforeValidator(RefValidator("PipingSystemUndergroundSegmentNames"))]
PlantAndCondenserEquipmentListsRef = Annotated[str, BeforeValidator(RefValidator("PlantAndCondenserEquipmentLists"))]
PlantConnectorsRef = Annotated[str, BeforeValidator(RefValidator("PlantConnectors"))]
PlantLoopsRef = Annotated[str, BeforeValidator(RefValidator("PlantLoops"))]
PlantOperationSchemesRef = Annotated[str, BeforeValidator(RefValidator("PlantOperationSchemes"))]
ProgramNamesRef = Annotated[str, BeforeValidator(RefValidator("ProgramNames"))]
QuadvariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("QuadvariateFunctions"))]
QuintvariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("QuintvariateFunctions"))]
RadiantDesignObjectRef = Annotated[str, BeforeValidator(RefValidator("RadiantDesignObject"))]
RadiantGroupNamesRef = Annotated[str, BeforeValidator(RefValidator("RadiantGroupNames"))]
RadiantSurfaceNamesRef = Annotated[str, BeforeValidator(RefValidator("RadiantSurfaceNames"))]
ReferenceCrackConditionsRef = Annotated[str, BeforeValidator(RefValidator("ReferenceCrackConditions"))]
RefrigerationAirChillerNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationAirChillerNames"))]
RefrigerationAllTypesCondenserNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationAllTypesCondenserNames"))]
RefrigerationAllTypesGasCoolerNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationAllTypesGasCoolerNames"))]
RefrigerationCascadeCondenserAndSecondarySystemNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationCascadeCondenserAndSecondarySystemNames"))]
RefrigerationCaseAndWalkInAndListNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationCaseAndWalkInAndListNames"))]
RefrigerationCaseAndWalkInNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationCaseAndWalkInNames"))]
RefrigerationCompressorAndListNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationCompressorAndListNames"))]
RefrigerationCompressorNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationCompressorNames"))]
RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames"))]
RefrigerationSubcoolerNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationSubcoolerNames"))]
RefrigerationSystemNamesRef = Annotated[str, BeforeValidator(RefValidator("RefrigerationSystemNames"))]
ReturnPathComponentNamesRef = Annotated[str, BeforeValidator(RefValidator("ReturnPathComponentNames"))]
RoomAirNodeGainsRef = Annotated[str, BeforeValidator(RefValidator("RoomAirNodeGains"))]
RoomAirNodeHVACEquipmentRef = Annotated[str, BeforeValidator(RefValidator("RoomAirNodeHVACEquipment"))]
RoomAirNodeSurfaceListsRef = Annotated[str, BeforeValidator(RefValidator("RoomAirNodeSurfaceLists"))]
RoomAirNodesRef = Annotated[str, BeforeValidator(RefValidator("RoomAirNodes"))]
RoomAirflowNetworkNodesRef = Annotated[str, BeforeValidator(RefValidator("RoomAirflowNetworkNodes"))]
RunPeriodsAndDesignDaysRef = Annotated[str, BeforeValidator(RefValidator("RunPeriodsAndDesignDays"))]
ScheduleNamesRef = Annotated[str, BeforeValidator(RefValidator("ScheduleNames"))]
ScheduleTypeLimitsNamesRef = Annotated[str, BeforeValidator(RefValidator("ScheduleTypeLimitsNames"))]
SimpleCoilsRef = Annotated[str, BeforeValidator(RefValidator("SimpleCoils"))]
SpaceAndSpaceListNamesRef = Annotated[str, BeforeValidator(RefValidator("SpaceAndSpaceListNames"))]
SpaceListNamesRef = Annotated[str, BeforeValidator(RefValidator("SpaceListNames"))]
SpaceNamesRef = Annotated[str, BeforeValidator(RefValidator("SpaceNames"))]
SpectralDataSetsRef = Annotated[str, BeforeValidator(RefValidator("SpectralDataSets"))]
SpectrumDataNamesRef = Annotated[str, BeforeValidator(RefValidator("SpectrumDataNames"))]
SubSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("SubSurfNames"))]
SupplyPathComponentNamesRef = Annotated[str, BeforeValidator(RefValidator("SupplyPathComponentNames"))]
SurfAndSubSurfNamesRef = Annotated[str, BeforeValidator(RefValidator("SurfAndSubSurfNames"))]
SurfaceAirflowLeakageNamesRef = Annotated[str, BeforeValidator(RefValidator("SurfaceAirflowLeakageNames"))]
SurfaceNamesRef = Annotated[str, BeforeValidator(RefValidator("SurfaceNames"))]
SurroundingSurfacesNamesRef = Annotated[str, BeforeValidator(RefValidator("SurroundingSurfacesNames"))]
SystemAvailabilityManagerListsRef = Annotated[str, BeforeValidator(RefValidator("SystemAvailabilityManagerLists"))]
SystemAvailabilityManagersRef = Annotated[str, BeforeValidator(RefValidator("SystemAvailabilityManagers"))]
ThermalComfortControlTypeNamesRef = Annotated[str, BeforeValidator(RefValidator("ThermalComfortControlTypeNames"))]
ThermostatOffsetFaultsRef = Annotated[str, BeforeValidator(RefValidator("ThermostatOffsetFaults"))]
TransformerNamesRef = Annotated[str, BeforeValidator(RefValidator("TransformerNames"))]
TrivariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("TrivariateFunctions"))]
UTSCNamesRef = Annotated[str, BeforeValidator(RefValidator("UTSCNames"))]
UndisturbedGroundTempModelsRef = Annotated[str, BeforeValidator(RefValidator("UndisturbedGroundTempModels"))]
UniVariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("UniVariateFunctions"))]
UnitarySystemPerformanceNamesRef = Annotated[str, BeforeValidator(RefValidator("UnitarySystemPerformanceNames"))]
UnivariateFunctionsRef = Annotated[str, BeforeValidator(RefValidator("UnivariateFunctions"))]
UserConvectionInsideModelsRef = Annotated[str, BeforeValidator(RefValidator("UserConvectionInsideModels"))]
UserConvectionModelsRef = Annotated[str, BeforeValidator(RefValidator("UserConvectionModels"))]
UserConvectionOutsideModelsRef = Annotated[str, BeforeValidator(RefValidator("UserConvectionOutsideModels"))]
UserDefinedCoilRef = Annotated[str, BeforeValidator(RefValidator("UserDefinedCoil"))]
UtilityCostTariffsRef = Annotated[str, BeforeValidator(RefValidator("UtilityCostTariffs"))]
VariableSpeedTowerCoefficientRef = Annotated[str, BeforeValidator(RefValidator("VariableSpeedTowerCoefficient"))]
VentSlabGroupNamesRef = Annotated[str, BeforeValidator(RefValidator("VentSlabGroupNames"))]
VentilationNamesRef = Annotated[str, BeforeValidator(RefValidator("VentilationNames"))]
WPCSetNamesRef = Annotated[str, BeforeValidator(RefValidator("WPCSetNames"))]
WPCValueNamesRef = Annotated[str, BeforeValidator(RefValidator("WPCValueNames"))]
WWHPCoolingNamesRef = Annotated[str, BeforeValidator(RefValidator("WWHPCoolingNames"))]
WWHPHeatingNamesRef = Annotated[str, BeforeValidator(RefValidator("WWHPHeatingNames"))]
WaterCoilControllersRef = Annotated[str, BeforeValidator(RefValidator("WaterCoilControllers"))]
WaterHeaterMixedNamesRef = Annotated[str, BeforeValidator(RefValidator("WaterHeaterMixedNames"))]
WaterHeaterNamesRef = Annotated[str, BeforeValidator(RefValidator("WaterHeaterNames"))]
WaterHeaterStratifiedNamesRef = Annotated[str, BeforeValidator(RefValidator("WaterHeaterStratifiedNames"))]
WaterStorageTankNamesRef = Annotated[str, BeforeValidator(RefValidator("WaterStorageTankNames"))]
WaterUseEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("WaterUseEquipmentNames"))]
WeekScheduleNamesRef = Annotated[str, BeforeValidator(RefValidator("WeekScheduleNames"))]
WindowComplexShadesRef = Annotated[str, BeforeValidator(RefValidator("WindowComplexShades"))]
WindowEquivalentLayerMaterialNamesRef = Annotated[str, BeforeValidator(RefValidator("WindowEquivalentLayerMaterialNames"))]
WindowFrameAndDividerNamesRef = Annotated[str, BeforeValidator(RefValidator("WindowFrameAndDividerNames"))]
WindowGapDeflectionStatesRef = Annotated[str, BeforeValidator(RefValidator("WindowGapDeflectionStates"))]
WindowGapSupportPillarsRef = Annotated[str, BeforeValidator(RefValidator("WindowGapSupportPillars"))]
WindowGasAndGasMixturesRef = Annotated[str, BeforeValidator(RefValidator("WindowGasAndGasMixtures"))]
WindowShadesScreensAndBlindsRef = Annotated[str, BeforeValidator(RefValidator("WindowShadesScreensAndBlinds"))]
WindowThermalModelParametersRef = Annotated[str, BeforeValidator(RefValidator("WindowThermalModelParameters"))]
ZoneAndZoneListNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneAndZoneListNames"))]
ZoneControlHumidistatNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneControlHumidistatNames"))]
ZoneControlThermostaticNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneControlThermostaticNames"))]
ZoneEquipmentListsRef = Annotated[str, BeforeValidator(RefValidator("ZoneEquipmentLists"))]
ZoneEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneEquipmentNames"))]
ZoneListNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneListNames"))]
ZoneMixersRef = Annotated[str, BeforeValidator(RefValidator("ZoneMixers"))]
ZoneNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneNames"))]
ZoneTerminalUnitListNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneTerminalUnitListNames"))]
ZoneTerminalUnitNamesRef = Annotated[str, BeforeValidator(RefValidator("ZoneTerminalUnitNames"))]
ValidBranchEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("validBranchEquipmentNames"))]
ValidBranchEquipmentTypesRef = Annotated[str, BeforeValidator(RefValidator("validBranchEquipmentTypes"))]
ValidCondenserEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("validCondenserEquipmentNames"))]
ValidCondenserEquipmentTypesRef = Annotated[str, BeforeValidator(RefValidator("validCondenserEquipmentTypes"))]
ValidOASysEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("validOASysEquipmentNames"))]
ValidOASysEquipmentTypesRef = Annotated[str, BeforeValidator(RefValidator("validOASysEquipmentTypes"))]
ValidPlantEquipmentNamesRef = Annotated[str, BeforeValidator(RefValidator("validPlantEquipmentNames"))]
ValidPlantEquipmentTypesRef = Annotated[str, BeforeValidator(RefValidator("validPlantEquipmentTypes"))]

__all__ = [
    "RefValidator",
    "AFNCoilNamesRef",
    "AFNHeatExchangerNamesRef",
    "AFNReliefAirFlowNamesRef",
    "AFNTerminalUnitNamesRef",
    "AirFlowNetworkMultizoneZonesRef",
    "AirLoopControllersRef",
    "AirLoopHVACMixerNamesRef",
    "AirLoopHVACSplitterNamesRef",
    "AirLoopOAEquipmentListsRef",
    "AirPrimaryLoopsRef",
    "AirTerminalUnitNamesRef",
    "AirflowNetworkComponentNamesRef",
    "AirflowNetworkNodeAndZoneNamesRef",
    "AirflowNetworkNodeNamesRef",
    "AirflowNetworkOccupantVentilationControlNamesRef",
    "AllHeatTranAngFacNamesRef",
    "AllHeatTranSurfNamesRef",
    "AllShadingAndHTSurfNamesRef",
    "AllShadingSurfNamesRef",
    "AttachedShadingSurfNamesRef",
    "BaseboardDesignObjectRef",
    "BiVariateFunctionsRef",
    "BivariateFunctionsRef",
    "BoilersRef",
    "BranchListsRef",
    "BranchesRef",
    "CFSGapRef",
    "CFSGlazingNameRef",
    "ChillerHeaterEIRNamesRef",
    "ChillersRef",
    "CoilCoolingDXRef",
    "CoilPerformanceDXRef",
    "CollectorStoragePerformanceRef",
    "ColorSchemesRef",
    "CompactHVACSystemConstantVolumeRef",
    "CompactHVACSystemDualDuctRef",
    "CompactHVACSystemUnitaryRef",
    "CompactHVACSystemVAVRef",
    "CompactHVACSystemVRFRef",
    "CompactHVACThermostatsRef",
    "ComplexFenestrationStatesRef",
    "CondenserOperationSchemesRef",
    "ConnectorListsRef",
    "ConstructionNamesRef",
    "ControlSchemeListRef",
    "ControlTypeNamesRef",
    "ControllerListsRef",
    "ControllerMechanicalVentNamesRef",
    "ControllerStandAloneEnergyRecoveryVentilatorRef",
    "ConverterListRef",
    "CoolingCoilNameRef",
    "CoolingCoilSystemNameRef",
    "CoolingCoilsDXRef",
    "CoolingCoilsDXMultiModeOrSingleSpeedRef",
    "CoolingCoilsDXMultiSpeedRef",
    "CoolingCoilsDXSingleSpeedRef",
    "CoolingCoilsDXVarRefrigFlowRef",
    "CoolingCoilsDXVarRefrigFlowFluidTemperatureControlRef",
    "CoolingCoilsDXVariableSpeedRef",
    "CoolingCoilsWaterRef",
    "CoolingCoilsWaterNoHXRef",
    "CoolingCoilsWaterToAirHPRef",
    "CoolingCoilsWaterToAirVSHPRef",
    "CoolingTowersRef",
    "CoolingTowersWithUARef",
    "DOAToZonalUnitRef",
    "DSOASpaceListNamesRef",
    "DXCoolingOperatingModeNamesRef",
    "DXCoolingPerformanceNamesRef",
    "DXCoolingSpeedNamesRef",
    "DataMatricesRef",
    "DayScheduleNamesRef",
    "DaylightReferencePointNamesRef",
    "DaylightingControlNamesRef",
    "DemandManagerNamesRef",
    "DesiccantHXPerfDataRef",
    "DesignSpecificationAirTerminalSizingNameRef",
    "DesignSpecificationOutdoorAirNamesRef",
    "DesignSpecificationZoneAirDistributionNamesRef",
    "DesignSpecificationZoneHVACSizingNameRef",
    "DesuperHeatingCoilSourcesRef",
    "DesuperHeatingWaterOnlySourcesRef",
    "EarthTubeParameterNamesRef",
    "ElecStorageListRef",
    "ElectricEquipmentNamesRef",
    "ErlProgramNamesRef",
    "EvapCoolerNamesRef",
    "ExteriorLightsNamesRef",
    "ExternalNodeNamesRef",
    "FCAirSupNamesRef",
    "FCAuxHeatNamesRef",
    "FCExhaustHXNamesRef",
    "FCInverterNamesRef",
    "FCPMNamesRef",
    "FCStackCoolerNamesRef",
    "FCStorageNamesRef",
    "FCWaterSupNamesRef",
    "FMUFileNameRef",
    "FansRef",
    "FansCVRef",
    "FansCVandOnOffRef",
    "FansCVandOnOffandVAVRef",
    "FansCVandVAVRef",
    "FansComponentModelRef",
    "FansOnOffRef",
    "FansOnOffandVAVRef",
    "FansSystemModelRef",
    "FansVAVRef",
    "FansZoneExhaustRef",
    "FlatPlatePVTParametersRef",
    "FlatPlateSolarCollectorParametersRef",
    "FloorSurfaceNamesRef",
    "FluidAndGlycolNamesRef",
    "FluidNamesRef",
    "FluidPropertyTemperaturesRef",
    "GenFuelSupNamesRef",
    "GeneratorListsRef",
    "GeneratorNamesRef",
    "GlazedExtSubSurfNamesRef",
    "GlazingMaterialNameRef",
    "GroundHeatExchangerVerticalArrayNamesRef",
    "GroundHeatExchangerVerticalPropertiesNamesRef",
    "GroundHeatExchangerVerticalResponseFactorNamesRef",
    "GroundHeatExchangerVerticalSingleNamesRef",
    "GroundSurfacesNamesRef",
    "HVACTemplateConstantVolumeZonesRef",
    "HVACTemplateDOASSystemsRef",
    "HVACTemplateSystemsRef",
    "HXAirToAirNamesRef",
    "HXAirToAirSensibleAndLatentNamesRef",
    "HXDesiccantBalancedRef",
    "HeatPumpAirToWaterFuelFiredCoolingNamesRef",
    "HeatPumpAirToWaterFuelFiredHeatingNamesRef",
    "HeatPumpWaterHeaterDXCoilsPumpedRef",
    "HeatPumpWaterHeaterDXCoilsVariableSpeedRef",
    "HeatPumpWaterHeaterDXCoilsWrappedRef",
    "HeatingCoilNameRef",
    "HeatingCoilSystemNameRef",
    "HeatingCoilsDXRef",
    "HeatingCoilsDXMultiSpeedRef",
    "HeatingCoilsDXSingleSpeedRef",
    "HeatingCoilsDXVarRefrigFlowRef",
    "HeatingCoilsDXVarRefrigFlowFluidTemperatureControlRef",
    "HeatingCoilsDXVariableSpeedRef",
    "HeatingCoilsDesuperheaterRef",
    "HeatingCoilsElectricRef",
    "HeatingCoilsElectricMultiStageRef",
    "HeatingCoilsGasMultiStageRef",
    "HeatingCoilsWaterRef",
    "HeatingCoilsWaterToAirHPRef",
    "HeatingCoilsWaterToAirVSHPRef",
    "IceThermalStorageEquipmentRef",
    "IndependentVariableListNameRef",
    "IndependentVariableNameRef",
    "IntegratedHeatPumpsRef",
    "InverterListRef",
    "LightsNamesRef",
    "MaterialNameRef",
    "MicroCHPParametersNamesRef",
    "MicroTurbineGeneratorNamesRef",
    "MultivariateFunctionsRef",
    "OAControllerNamesRef",
    "OSCMNamesRef",
    "OutFaceEnvNamesRef",
    "OutdoorAirMixersRef",
    "OutdoorAirNodeNamesRef",
    "OutdoorAirUnitEquipmentListsRef",
    "PLHPCoolingNamesRef",
    "PLHPHeatingNamesRef",
    "PVGeneratorNamesRef",
    "PVModulesRef",
    "PeopleNamesRef",
    "PipingSystemUndergroundCircuitNamesRef",
    "PipingSystemUndergroundSegmentNamesRef",
    "PlantAndCondenserEquipmentListsRef",
    "PlantConnectorsRef",
    "PlantLoopsRef",
    "PlantOperationSchemesRef",
    "ProgramNamesRef",
    "QuadvariateFunctionsRef",
    "QuintvariateFunctionsRef",
    "RadiantDesignObjectRef",
    "RadiantGroupNamesRef",
    "RadiantSurfaceNamesRef",
    "ReferenceCrackConditionsRef",
    "RefrigerationAirChillerNamesRef",
    "RefrigerationAllTypesCondenserNamesRef",
    "RefrigerationAllTypesGasCoolerNamesRef",
    "RefrigerationCascadeCondenserAndSecondarySystemNamesRef",
    "RefrigerationCaseAndWalkInAndListNamesRef",
    "RefrigerationCaseAndWalkInNamesRef",
    "RefrigerationCompressorAndListNamesRef",
    "RefrigerationCompressorNamesRef",
    "RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNamesRef",
    "RefrigerationSubcoolerNamesRef",
    "RefrigerationSystemNamesRef",
    "ReturnPathComponentNamesRef",
    "RoomAirNodeGainsRef",
    "RoomAirNodeHVACEquipmentRef",
    "RoomAirNodeSurfaceListsRef",
    "RoomAirNodesRef",
    "RoomAirflowNetworkNodesRef",
    "RunPeriodsAndDesignDaysRef",
    "ScheduleNamesRef",
    "ScheduleTypeLimitsNamesRef",
    "SimpleCoilsRef",
    "SpaceAndSpaceListNamesRef",
    "SpaceListNamesRef",
    "SpaceNamesRef",
    "SpectralDataSetsRef",
    "SpectrumDataNamesRef",
    "SubSurfNamesRef",
    "SupplyPathComponentNamesRef",
    "SurfAndSubSurfNamesRef",
    "SurfaceAirflowLeakageNamesRef",
    "SurfaceNamesRef",
    "SurroundingSurfacesNamesRef",
    "SystemAvailabilityManagerListsRef",
    "SystemAvailabilityManagersRef",
    "ThermalComfortControlTypeNamesRef",
    "ThermostatOffsetFaultsRef",
    "TransformerNamesRef",
    "TrivariateFunctionsRef",
    "UTSCNamesRef",
    "UndisturbedGroundTempModelsRef",
    "UniVariateFunctionsRef",
    "UnitarySystemPerformanceNamesRef",
    "UnivariateFunctionsRef",
    "UserConvectionInsideModelsRef",
    "UserConvectionModelsRef",
    "UserConvectionOutsideModelsRef",
    "UserDefinedCoilRef",
    "UtilityCostTariffsRef",
    "VariableSpeedTowerCoefficientRef",
    "VentSlabGroupNamesRef",
    "VentilationNamesRef",
    "WPCSetNamesRef",
    "WPCValueNamesRef",
    "WWHPCoolingNamesRef",
    "WWHPHeatingNamesRef",
    "WaterCoilControllersRef",
    "WaterHeaterMixedNamesRef",
    "WaterHeaterNamesRef",
    "WaterHeaterStratifiedNamesRef",
    "WaterStorageTankNamesRef",
    "WaterUseEquipmentNamesRef",
    "WeekScheduleNamesRef",
    "WindowComplexShadesRef",
    "WindowEquivalentLayerMaterialNamesRef",
    "WindowFrameAndDividerNamesRef",
    "WindowGapDeflectionStatesRef",
    "WindowGapSupportPillarsRef",
    "WindowGasAndGasMixturesRef",
    "WindowShadesScreensAndBlindsRef",
    "WindowThermalModelParametersRef",
    "ZoneAndZoneListNamesRef",
    "ZoneControlHumidistatNamesRef",
    "ZoneControlThermostaticNamesRef",
    "ZoneEquipmentListsRef",
    "ZoneEquipmentNamesRef",
    "ZoneListNamesRef",
    "ZoneMixersRef",
    "ZoneNamesRef",
    "ZoneTerminalUnitListNamesRef",
    "ZoneTerminalUnitNamesRef",
    "ValidBranchEquipmentNamesRef",
    "ValidBranchEquipmentTypesRef",
    "ValidCondenserEquipmentNamesRef",
    "ValidCondenserEquipmentTypesRef",
    "ValidOASysEquipmentNamesRef",
    "ValidOASysEquipmentTypesRef",
    "ValidPlantEquipmentNamesRef",
    "ValidPlantEquipmentTypesRef",
]
