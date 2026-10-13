"""Auto-generated reference metadata for EnergyPlus validation.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
"""

from __future__ import annotations

REF_PROVIDERS: dict[str, list[tuple[str, list[str]]]] = {
    'AirConditioner:VariableRefrigerantFlow': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC': [('name', ['AirPrimaryLoops'])],
    'AirLoopHVAC:ControllerList': [('name', ['ControllerLists'])],
    'AirLoopHVAC:DedicatedOutdoorAirSystem': [('name', ['DOASAirLoops'])],
    'AirLoopHVAC:Mixer': [('name', ['AirLoopHVACMixerNames'])],
    'AirLoopHVAC:OutdoorAirSystem': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:OutdoorAirSystem:EquipmentList': [
        ('name', ['AirLoopOAEquipmentLists'])
    ],
    'AirLoopHVAC:ReturnPlenum': [('name', ['ReturnPathComponentNames'])],
    'AirLoopHVAC:Splitter': [('name', ['AirLoopHVACSplitterNames'])],
    'AirLoopHVAC:SupplyPlenum': [('name', ['SupplyPathComponentNames'])],
    'AirLoopHVAC:Unitary:Furnace:HeatCool': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:Unitary:Furnace:HeatOnly': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:UnitaryHeatCool': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass': [
        ('name', ['validBranchEquipmentNames'])
    ],
    'AirLoopHVAC:UnitaryHeatOnly': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:UnitaryHeatPump:AirToAir': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed': [
        ('name', ['validBranchEquipmentNames'])
    ],
    'AirLoopHVAC:UnitaryHeatPump:WaterToAir': [('name', ['validBranchEquipmentNames'])],
    'AirLoopHVAC:UnitarySystem': [
        (
            'name',
            [
                'DOAToZonalUnit',
                'ZoneEquipmentNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'AirLoopHVAC:ZoneMixer': [('name', ['ReturnPathComponentNames', 'ZoneMixers'])],
    'AirLoopHVAC:ZoneSplitter': [('name', ['SupplyPathComponentNames'])],
    'AirTerminal:DualDuct:ConstantVolume': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:DualDuct:VAV': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:DualDuct:VAV:OutdoorAir': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:SingleDuct:ConstantVolume:CooledBeam': [
        ('name', ['AirTerminalUnitNames', 'validBranchEquipmentNames'])
    ],
    'AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam': [
        ('name', ['AirTerminalUnitNames', 'validBranchEquipmentNames'])
    ],
    'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction': [
        ('name', ['AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:ConstantVolume:NoReheat': [
        ('name', ['AFNTerminalUnitNames', 'AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:ConstantVolume:Reheat': [
        ('name', ['AFNTerminalUnitNames', 'AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:Mixer': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:SingleDuct:ParallelPIU:Reheat': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:SingleDuct:SeriesPIU:Reheat': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:SingleDuct:UserDefined': [
        ('name', ['AirTerminalUnitNames', 'validBranchEquipmentNames'])
    ],
    'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat': [
        ('name', ['AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat': [
        ('name', ['AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:VAV:NoReheat': [('name', ['AirTerminalUnitNames'])],
    'AirTerminal:SingleDuct:VAV:Reheat': [
        ('name', ['AFNTerminalUnitNames', 'AirTerminalUnitNames'])
    ],
    'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan': [
        ('name', ['AirTerminalUnitNames'])
    ],
    'AirflowNetwork:Distribution:Component:Coil': [
        ('coil_name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:ConstantPressureDrop': [
        ('name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:Duct': [
        ('name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:Fan': [
        ('fan_name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:HeatExchanger': [
        ('heatexchanger_name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:Leak': [
        ('name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:LeakageRatio': [
        ('name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:OutdoorAirFlow': [
        ('name', ['AFNOutdoorAirFlowNames', 'AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:ReliefAirFlow': [
        ('name', ['AFNReliefAirFlowNames', 'AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Component:TerminalUnit': [
        ('terminal_unit_name', ['AirflowNetworkComponentNames'])
    ],
    'AirflowNetwork:Distribution:Node': [('name', ['AirflowNetworkNodeAndZoneNames'])],
    'AirflowNetwork:IntraZone:Linkage': [('name', ['AirflowNetwork LinkageNames'])],
    'AirflowNetwork:IntraZone:Node': [('name', ['AirflowNetworkNodeNames'])],
    'AirflowNetwork:MultiZone:Component:DetailedOpening': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:Component:HorizontalOpening': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:Component:SimpleOpening': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:Component:ZoneExhaustFan': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:ExternalNode': [('name', ['ExternalNodeNames'])],
    'AirflowNetwork:MultiZone:ReferenceCrackConditions': [
        ('name', ['ReferenceCrackConditions'])
    ],
    'AirflowNetwork:MultiZone:SpecifiedFlowRate': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:Surface:Crack': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea': [
        ('name', ['SurfaceAirflowLeakageNames'])
    ],
    'AirflowNetwork:MultiZone:WindPressureCoefficientArray': [
        ('name', ['WPCSetNames'])
    ],
    'AirflowNetwork:MultiZone:WindPressureCoefficientValues': [
        ('name', ['WPCValueNames'])
    ],
    'AirflowNetwork:MultiZone:Zone': [('zone_name', ['AirFlowNetworkMultizoneZones'])],
    'AirflowNetwork:OccupantVentilationControl': [
        ('name', ['AirflowNetworkOccupantVentilationControlNames'])
    ],
    'AirflowNetwork:ZoneControl:PressureController': [
        ('name', ['AirflowNetworkZoneControlPressureControllerNames'])
    ],
    'AvailabilityManager:DifferentialThermostat': [
        ('name', ['SystemAvailabilityManagers'])
    ],
    'AvailabilityManager:HighTemperatureTurnOff': [
        ('name', ['SystemAvailabilityManagers'])
    ],
    'AvailabilityManager:HighTemperatureTurnOn': [
        ('name', ['SystemAvailabilityManagers'])
    ],
    'AvailabilityManager:HybridVentilation': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:LowTemperatureTurnOff': [
        ('name', ['SystemAvailabilityManagers'])
    ],
    'AvailabilityManager:LowTemperatureTurnOn': [
        ('name', ['SystemAvailabilityManagers'])
    ],
    'AvailabilityManager:NightCycle': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:NightVentilation': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:OptimumStart': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:Scheduled': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:ScheduledOff': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManager:ScheduledOn': [('name', ['SystemAvailabilityManagers'])],
    'AvailabilityManagerAssignmentList': [('name', ['SystemAvailabilityManagerLists'])],
    'Boiler:HotWater': [
        ('name', ['Boilers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Boiler:Steam': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Branch': [('name', ['Branches'])],
    'BranchList': [('name', ['BranchLists'])],
    'BuildingSurface:Detailed': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'FloorSurfaceNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Ceiling:Adiabatic': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Ceiling:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'CentralHeatPumpSystem': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Absorption': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Absorption:Indirect': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:CombustionTurbine': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:ConstantCOP': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Electric': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Electric:ASHRAE205': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Electric:EIR': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:Electric:ReformulatedEIR': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Chiller:EngineDriven': [
        ('name', ['Chillers', 'validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'ChillerHeater:Absorption:DirectFired': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'ChillerHeater:Absorption:DoubleEffect': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'ChillerHeaterPerformance:Electric:EIR': [('name', ['ChillerHeaterEIRNames'])],
    'Coil:Cooling:DX': [
        ('name', ['AFNCoilNames', 'CoilCoolingDX', 'DesuperHeatingCoilSources'])
    ],
    'Coil:Cooling:DX:CurveFit:OperatingMode': [
        ('name', ['DXCoolingOperatingModeNames'])
    ],
    'Coil:Cooling:DX:CurveFit:Performance': [('name', ['DXCoolingPerformanceNames'])],
    'Coil:Cooling:DX:CurveFit:Speed': [('name', ['DXCoolingSpeedNames'])],
    'Coil:Cooling:DX:MultiSpeed': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilsDXMultiSpeed',
                'DesuperHeatingWaterOnlySources',
            ],
        )
    ],
    'Coil:Cooling:DX:SingleSpeed': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilsDX',
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'CoolingCoilsDXSingleSpeed',
                'DesuperHeatingCoilSources',
            ],
        )
    ],
    'Coil:Cooling:DX:SingleSpeed:ThermalStorage': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilsDX',
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'CoolingCoilsDXSingleSpeed',
                'validBranchEquipmentNames',
            ],
        )
    ],
    'Coil:Cooling:DX:TwoSpeed': [
        ('name', ['AFNCoilNames', 'CoolingCoilsDX', 'DesuperHeatingCoilSources'])
    ],
    'Coil:Cooling:DX:TwoStageWithHumidityControlMode': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilsDX',
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'DesuperHeatingCoilSources',
            ],
        )
    ],
    'Coil:Cooling:DX:VariableRefrigerantFlow': [
        ('name', ['CoolingCoilsDXVarRefrigFlow'])
    ],
    'Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl': [
        ('name', ['CoolingCoilsDXVarRefrigFlowFluidTemperatureControl'])
    ],
    'Coil:Cooling:DX:VariableSpeed': [
        ('name', ['CoolingCoilsDXVariableSpeed', 'DesuperHeatingCoilSources'])
    ],
    'Coil:Cooling:Water': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilName',
                'CoolingCoilsWater',
                'CoolingCoilsWaterNoHX',
                'SimpleCoils',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Cooling:Water:DetailedGeometry': [
        (
            'name',
            [
                'AFNCoilNames',
                'CoolingCoilName',
                'CoolingCoilsWater',
                'CoolingCoilsWaterNoHX',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Cooling:WaterToAirHeatPump:EquationFit': [
        (
            'name',
            [
                'CoolingCoilsWaterToAirHP',
                'DesuperHeatingWaterOnlySources',
                'validBranchEquipmentNames',
            ],
        )
    ],
    'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation': [
        ('name', ['CoolingCoilsWaterToAirHP', 'validBranchEquipmentNames'])
    ],
    'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit': [
        (
            'name',
            [
                'CoolingCoilsWaterToAirVSHP',
                'DesuperHeatingWaterOnlySources',
                'validBranchEquipmentNames',
            ],
        )
    ],
    'Coil:Heating:DX:MultiSpeed': [
        ('name', ['AFNCoilNames', 'HeatingCoilsDXMultiSpeed'])
    ],
    'Coil:Heating:DX:SingleSpeed': [
        ('name', ['AFNCoilNames', 'HeatingCoilsDX', 'HeatingCoilsDXSingleSpeed'])
    ],
    'Coil:Heating:DX:VariableRefrigerantFlow': [
        (
            'name',
            [
                'HeatingCoilsDX',
                'HeatingCoilsDXSingleSpeed',
                'HeatingCoilsDXVarRefrigFlow',
            ],
        )
    ],
    'Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl': [
        ('name', ['HeatingCoilsDXVarRefrigFlowFluidTemperatureControl'])
    ],
    'Coil:Heating:DX:VariableSpeed': [('name', ['HeatingCoilsDXVariableSpeed'])],
    'Coil:Heating:Desuperheater': [
        (
            'name',
            ['AFNCoilNames', 'HeatingCoilsDesuperheater', 'validBranchEquipmentNames'],
        )
    ],
    'Coil:Heating:Electric': [
        (
            'name',
            [
                'AFNCoilNames',
                'HeatingCoilName',
                'HeatingCoilsElectric',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Heating:Electric:MultiStage': [('name', ['HeatingCoilsElectricMultiStage'])],
    'Coil:Heating:Fuel': [
        (
            'name',
            [
                'AFNCoilNames',
                'HeatingCoilName',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Heating:Gas:MultiStage': [('name', ['HeatingCoilsGasMultiStage'])],
    'Coil:Heating:Steam': [
        (
            'name',
            [
                'HeatingCoilName',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Heating:Water': [
        (
            'name',
            [
                'AFNCoilNames',
                'HeatingCoilName',
                'HeatingCoilsWater',
                'SimpleCoils',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:Heating:WaterToAirHeatPump:EquationFit': [
        ('name', ['HeatingCoilsWaterToAirHP', 'validBranchEquipmentNames'])
    ],
    'Coil:Heating:WaterToAirHeatPump:ParameterEstimation': [
        ('name', ['HeatingCoilsWaterToAirHP', 'validBranchEquipmentNames'])
    ],
    'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit': [
        ('name', ['HeatingCoilsWaterToAirVSHP', 'validBranchEquipmentNames'])
    ],
    'Coil:UserDefined': [
        (
            'name',
            [
                'UserDefinedCoil',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Coil:WaterHeating:AirToWaterHeatPump:Pumped': [
        ('name', ['HeatPumpWaterHeaterDXCoilsPumped'])
    ],
    'Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed': [
        ('name', ['HeatPumpWaterHeaterDXCoilsVariableSpeed'])
    ],
    'Coil:WaterHeating:AirToWaterHeatPump:Wrapped': [
        ('name', ['HeatPumpWaterHeaterDXCoilsWrapped'])
    ],
    'CoilPerformance:DX:Cooling': [('name', ['CoilPerformanceDX'])],
    'CoilSystem:Cooling:DX': [
        (
            'name',
            [
                'CoolingCoilSystemName',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'CoilSystem:Cooling:DX:HeatExchangerAssisted': [
        (
            'name',
            [
                'CoolingCoilsDX',
                'CoolingCoilsDXMultiModeOrSingleSpeed',
                'CoolingCoilsDXSingleSpeed',
            ],
        )
    ],
    'CoilSystem:Cooling:Water': [
        ('name', ['validBranchEquipmentNames', 'validOASysEquipmentNames'])
    ],
    'CoilSystem:Cooling:Water:HeatExchangerAssisted': [
        (
            'name',
            [
                'CoolingCoilsWater',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'CoilSystem:Heating:DX': [
        (
            'name',
            [
                'HeatingCoilSystemName',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'CoilSystem:IntegratedHeatPump:AirSource': [('name', ['IntegratedHeatPumps'])],
    'ComfortViewFactorAngles': [('name', ['AllHeatTranAngFacNames'])],
    'CondenserEquipmentList': [
        ('name', ['CondenserEquipmentLists', 'PlantAndCondenserEquipmentLists'])
    ],
    'CondenserEquipmentOperationSchemes': [('name', ['CondenserOperationSchemes'])],
    'CondenserLoop': [('name', ['PlantLoops'])],
    'Connector:Mixer': [('name', ['PlantConnectors'])],
    'Connector:Splitter': [('name', ['PlantConnectors'])],
    'ConnectorList': [('name', ['ConnectorLists'])],
    'Construction': [('name', ['ConstructionNames'])],
    'Construction:AirBoundary': [('name', ['ConstructionNames'])],
    'Construction:CfactorUndergroundWall': [('name', ['ConstructionNames'])],
    'Construction:ComplexFenestrationState': [('name', ['ComplexFenestrationStates'])],
    'Construction:FfactorGroundFloor': [('name', ['ConstructionNames'])],
    'Construction:WindowDataFile': [('name', ['ConstructionNames'])],
    'Construction:WindowEquivalentLayer': [('name', ['ConstructionNames'])],
    'ConstructionProperty:InternalHeatSource': [('name', ['InternalHeatSourceNames'])],
    'Controller:MechanicalVentilation': [('name', ['ControllerMechanicalVentNames'])],
    'Controller:OutdoorAir': [('name', ['AirLoopControllers', 'OAControllerNames'])],
    'Controller:WaterCoil': [('name', ['AirLoopControllers', 'WaterCoilControllers'])],
    'CoolingTower:SingleSpeed': [
        (
            'name',
            [
                'CoolingTowers',
                'CoolingTowersWithUA',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'CoolingTower:TwoSpeed': [
        (
            'name',
            [
                'CoolingTowers',
                'CoolingTowersWithUA',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'CoolingTower:VariableSpeed': [
        (
            'name',
            [
                'CoolingTowers',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'CoolingTower:VariableSpeed:Merkel': [
        (
            'name',
            [
                'CoolingTowers',
                'CoolingTowersWithUA',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'CoolingTowerPerformance:CoolTools': [('name', ['VariableSpeedTowerCoefficient'])],
    'CoolingTowerPerformance:YorkCalc': [('name', ['VariableSpeedTowerCoefficient'])],
    'Curve:Bicubic': [('name', ['BivariateFunctions'])],
    'Curve:Biquadratic': [('name', ['BivariateFunctions'])],
    'Curve:ChillerPartLoadWithLift': [('name', ['TrivariateFunctions'])],
    'Curve:Cubic': [('name', ['UnivariateFunctions'])],
    'Curve:CubicLinear': [('name', ['BivariateFunctions'])],
    'Curve:DoubleExponentialDecay': [('name', ['UnivariateFunctions'])],
    'Curve:Exponent': [('name', ['UnivariateFunctions'])],
    'Curve:ExponentialDecay': [('name', ['UnivariateFunctions'])],
    'Curve:ExponentialSkewNormal': [('name', ['UnivariateFunctions'])],
    'Curve:FanPressureRise': [('name', ['BivariateFunctions'])],
    'Curve:Functional:PressureDrop': [('name', ['UnivariateFunctions'])],
    'Curve:Linear': [('name', ['UnivariateFunctions'])],
    'Curve:QuadLinear': [('name', ['QuadvariateFunctions'])],
    'Curve:Quadratic': [('name', ['UnivariateFunctions'])],
    'Curve:QuadraticLinear': [('name', ['BivariateFunctions'])],
    'Curve:Quartic': [('name', ['UnivariateFunctions'])],
    'Curve:QuintLinear': [('name', ['QuintvariateFunctions'])],
    'Curve:RectangularHyperbola1': [('name', ['UnivariateFunctions'])],
    'Curve:RectangularHyperbola2': [('name', ['UnivariateFunctions'])],
    'Curve:Sigmoid': [('name', ['UnivariateFunctions'])],
    'Curve:Triquadratic': [('name', ['TrivariateFunctions'])],
    'Daylighting:Controls': [('name', ['DaylightingControlNames'])],
    'Daylighting:ReferencePoint': [('name', ['DaylightReferencePointNames'])],
    'Dehumidifier:Desiccant:NoFans': [
        ('name', ['validBranchEquipmentNames', 'validOASysEquipmentNames'])
    ],
    'Dehumidifier:Desiccant:System': [
        ('name', ['validBranchEquipmentNames', 'validOASysEquipmentNames'])
    ],
    'DemandManager:ElectricEquipment': [('name', ['DemandManagerNames'])],
    'DemandManager:ExteriorLights': [('name', ['DemandManagerNames'])],
    'DemandManager:Lights': [('name', ['DemandManagerNames'])],
    'DemandManager:Thermostats': [('name', ['DemandManagerNames'])],
    'DemandManager:Ventilation': [('name', ['DemandManagerNames'])],
    'DesignSpecification:AirTerminal:Sizing': [
        ('name', ['DesignSpecificationAirTerminalSizingName'])
    ],
    'DesignSpecification:OutdoorAir': [
        ('name', ['DesignSpecificationOutdoorAirNames'])
    ],
    'DesignSpecification:OutdoorAir:SpaceList': [('name', ['DSOASpaceListNames'])],
    'DesignSpecification:ZoneAirDistribution': [
        ('name', ['DesignSpecificationZoneAirDistributionNames'])
    ],
    'DesignSpecification:ZoneHVAC:Sizing': [
        ('name', ['DesignSpecificationZoneHVACSizingName'])
    ],
    'DistrictCooling': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'DistrictHeating:Steam': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'DistrictHeating:Water': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'Door': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'Door:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'Duct': [('name', ['validBranchEquipmentNames'])],
    'ElectricEquipment': [('name', ['ElectricEquipmentNames'])],
    'ElectricLoadCenter:Generators': [('name', ['GeneratorLists'])],
    'ElectricLoadCenter:Inverter:FunctionOfPower': [('name', ['InverterList'])],
    'ElectricLoadCenter:Inverter:LookUpTable': [('name', ['InverterList'])],
    'ElectricLoadCenter:Inverter:PVWatts': [('name', ['InverterList'])],
    'ElectricLoadCenter:Inverter:Simple': [('name', ['InverterList'])],
    'ElectricLoadCenter:Storage:Battery': [('name', ['ElecStorageList'])],
    'ElectricLoadCenter:Storage:Converter': [('name', ['ConverterList'])],
    'ElectricLoadCenter:Storage:LiIonNMCBattery': [('name', ['ElecStorageList'])],
    'ElectricLoadCenter:Storage:Simple': [('name', ['ElecStorageList'])],
    'ElectricLoadCenter:Transformer': [('name', ['TransformerNames'])],
    'EnergyManagementSystem:Program': [('name', ['ErlProgramNames'])],
    'EnergyManagementSystem:ProgramCallingManager': [('name', ['ProgramNames'])],
    'EnergyManagementSystem:Subroutine': [('name', ['ErlProgramNames'])],
    'EvaporativeCooler:Direct:CelDekPad': [
        (
            'name',
            [
                'EvapCoolerNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'EvaporativeCooler:Direct:ResearchSpecial': [
        (
            'name',
            [
                'EvapCoolerNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'EvaporativeCooler:Indirect:CelDekPad': [
        (
            'name',
            [
                'EvapCoolerNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'EvaporativeCooler:Indirect:ResearchSpecial': [
        (
            'name',
            [
                'EvapCoolerNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'EvaporativeCooler:Indirect:WetCoil': [
        (
            'name',
            [
                'EvapCoolerNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'EvaporativeFluidCooler:SingleSpeed': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'EvaporativeFluidCooler:TwoSpeed': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'Exterior:Lights': [('name', ['ExteriorLightsNames'])],
    'ExternalInterface:FunctionalMockupUnitExport:To:Schedule': [
        ('schedule_name', ['ScheduleNames'])
    ],
    'ExternalInterface:FunctionalMockupUnitImport': [
        ('fmu_file_name', ['FMUFileName'])
    ],
    'ExternalInterface:FunctionalMockupUnitImport:To:Schedule': [
        ('name', ['ScheduleNames'])
    ],
    'ExternalInterface:Schedule': [('name', ['ScheduleNames'])],
    'Fan:ComponentModel': [
        (
            'name',
            [
                'Fans',
                'FansComponentModel',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Fan:ConstantVolume': [
        (
            'name',
            [
                'Fans',
                'FansCV',
                'FansCVandOnOff',
                'FansCVandOnOffandVAV',
                'FansCVandVAV',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Fan:OnOff': [
        (
            'name',
            [
                'Fans',
                'FansCVandOnOff',
                'FansCVandOnOffandVAV',
                'FansOnOff',
                'FansOnOffandVAV',
            ],
        )
    ],
    'Fan:SystemModel': [
        (
            'name',
            [
                'Fans',
                'FansSystemModel',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Fan:VariableVolume': [
        (
            'name',
            [
                'Fans',
                'FansCVandOnOffandVAV',
                'FansCVandVAV',
                'FansOnOffandVAV',
                'FansVAV',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'Fan:ZoneExhaust': [('name', ['FansZoneExhaust', 'ZoneEquipmentNames'])],
    'FaultModel:ThermostatOffset': [('name', ['ThermostatOffsetFaults'])],
    'FenestrationSurface:Detailed': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'GlazedExtSubSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'Floor:Adiabatic': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'FloorSurfaceNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Floor:Detailed': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'FloorSurfaceNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Floor:GroundContact': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'FloorSurfaceNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Floor:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'FloorSurfaceNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'FluidCooler:SingleSpeed': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'FluidCooler:TwoSpeed': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'FluidProperties:GlycolConcentration': [('name', ['FluidAndGlycolNames'])],
    'FluidProperties:Name': [('fluid_name', ['FluidAndGlycolNames', 'FluidNames'])],
    'FluidProperties:Temperatures': [('name', ['FluidPropertyTemperatures'])],
    'Foundation:Kiva': [('name', ['OutFaceEnvNames'])],
    'Generator:CombustionTurbine': [
        ('name', ['GeneratorNames', 'validBranchEquipmentNames'])
    ],
    'Generator:FuelCell': [('name', ['GeneratorNames'])],
    'Generator:FuelCell:AirSupply': [('name', ['FCAirSupNames'])],
    'Generator:FuelCell:AuxiliaryHeater': [('name', ['FCAuxHeatNames'])],
    'Generator:FuelCell:ElectricalStorage': [('name', ['FCStorageNames'])],
    'Generator:FuelCell:ExhaustGasToWaterHeatExchanger': [
        (
            'name',
            [
                'FCExhaustHXNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'Generator:FuelCell:Inverter': [('name', ['FCInverterNames'])],
    'Generator:FuelCell:PowerModule': [('name', ['FCPMNames'])],
    'Generator:FuelCell:StackCooler': [
        ('name', ['FCStackCoolerNames', 'validBranchEquipmentNames'])
    ],
    'Generator:FuelCell:WaterSupply': [('name', ['FCWaterSupNames'])],
    'Generator:FuelSupply': [('name', ['GenFuelSupNames'])],
    'Generator:InternalCombustionEngine': [
        ('name', ['GeneratorNames', 'validBranchEquipmentNames'])
    ],
    'Generator:MicroCHP': [
        (
            'name',
            ['GeneratorNames', 'validBranchEquipmentNames', 'validPlantEquipmentNames'],
        )
    ],
    'Generator:MicroCHP:NonNormalizedParameters': [
        ('name', ['MicroCHPParametersNames'])
    ],
    'Generator:MicroTurbine': [
        (
            'name',
            [
                'GeneratorNames',
                'MicroTurbineGeneratorNames',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'Generator:PVWatts': [('name', ['GeneratorNames'])],
    'Generator:Photovoltaic': [('name', ['GeneratorNames', 'PVGeneratorNames'])],
    'Generator:WindTurbine': [('name', ['GeneratorNames'])],
    'GlazedDoor': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'GlazedExtSubSurfNames',
                'OutFaceEnvNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'GlazedDoor:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'GroundHeatExchanger:HorizontalTrench': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'GroundHeatExchanger:Pond': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'GroundHeatExchanger:ResponseFactors': [
        ('name', ['GroundHeatExchangerVerticalResponseFactorNames'])
    ],
    'GroundHeatExchanger:Slinky': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'GroundHeatExchanger:Surface': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'GroundHeatExchanger:System': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'GroundHeatExchanger:Vertical:Array': [
        ('name', ['GroundHeatExchangerVerticalArrayNames'])
    ],
    'GroundHeatExchanger:Vertical:Properties': [
        ('name', ['GroundHeatExchangerVerticalPropertiesNames'])
    ],
    'GroundHeatExchanger:Vertical:Single': [
        ('name', ['GroundHeatExchangerVerticalSingleNames'])
    ],
    'HVACTemplate:System:ConstantVolume': [
        ('name', ['CompactHVACSystemConstantVolume', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:DedicatedOutdoorAir': [
        ('name', ['HVACTemplateDOASSystems', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:DualDuct': [
        ('name', ['CompactHVACSystemDualDuct', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:PackagedVAV': [
        ('name', ['CompactHVACSystemVAV', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:Unitary': [
        ('name', ['CompactHVACSystemUnitary', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:UnitaryHeatPump:AirToAir': [
        ('name', ['CompactHVACSystemUnitary', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:UnitarySystem': [
        ('name', ['CompactHVACSystemUnitary', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:VAV': [
        ('name', ['CompactHVACSystemVAV', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:System:VRF': [
        ('name', ['CompactHVACSystemVRF', 'HVACTemplateSystems'])
    ],
    'HVACTemplate:Thermostat': [('name', ['CompactHVACThermostats'])],
    'HVACTemplate:Zone:ConstantVolume': [
        ('zone_name', ['HVACTemplateConstantVolumeZones'])
    ],
    'HeaderedPumps:ConstantSpeed': [('name', ['validBranchEquipmentNames'])],
    'HeaderedPumps:VariableSpeed': [('name', ['validBranchEquipmentNames'])],
    'HeatExchanger:AirToAir:FlatPlate': [
        (
            'name',
            [
                'AFNHeatExchangerNames',
                'HXAirToAirNames',
                'ZoneEquipmentNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'HeatExchanger:AirToAir:SensibleAndLatent': [
        (
            'name',
            [
                'AFNHeatExchangerNames',
                'HXAirToAirNames',
                'HXAirToAirSensibleAndLatentNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'HeatExchanger:Desiccant:BalancedFlow': [
        (
            'name',
            [
                'AFNHeatExchangerNames',
                'HXAirToAirNames',
                'HXDesiccantBalanced',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1': [
        ('name', ['DesiccantHXPerfData'])
    ],
    'HeatExchanger:FluidToFluid': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'HeatPump:AirToWater:FuelFired:Cooling': [
        ('name', ['HeatPumpAirToWaterFuelFiredCoolingNames'])
    ],
    'HeatPump:AirToWater:FuelFired:Heating': [
        ('name', ['HeatPumpAirToWaterFuelFiredHeatingNames'])
    ],
    'HeatPump:PlantLoop:EIR:Cooling': [
        (
            'name',
            [
                'PLHPCoolingNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'HeatPump:PlantLoop:EIR:Heating': [
        (
            'name',
            [
                'PLHPHeatingNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'HeatPump:WaterToWater:EquationFit:Cooling': [
        (
            'name',
            [
                'WWHPCoolingNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'HeatPump:WaterToWater:EquationFit:Heating': [
        (
            'name',
            [
                'WWHPHeatingNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'HeatPump:WaterToWater:ParameterEstimation:Cooling': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'HeatPump:WaterToWater:ParameterEstimation:Heating': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'Humidifier:Steam:Electric': [
        ('name', ['validBranchEquipmentNames', 'validOASysEquipmentNames'])
    ],
    'Humidifier:Steam:Gas': [
        ('name', ['validBranchEquipmentNames', 'validOASysEquipmentNames'])
    ],
    'InternalMass': [
        (
            'name',
            ['AllHeatTranAngFacNames', 'AllHeatTranSurfNames', 'RadiantSurfaceNames'],
        )
    ],
    'Lights': [('name', ['LightsNames'])],
    'LoadProfile:Plant': [('name', ['validBranchEquipmentNames'])],
    'Material': [('name', ['MaterialName'])],
    'Material:AirGap': [('name', ['MaterialName'])],
    'Material:InfraredTransparent': [('name', ['MaterialName'])],
    'Material:NoMass': [('name', ['MaterialName'])],
    'Material:RoofVegetation': [('name', ['MaterialName'])],
    'MaterialProperty:GlazingSpectralData': [('name', ['SpectralDataSets'])],
    'Matrix:TwoDimension': [('name', ['DataMatrices'])],
    'OutdoorAir:Mixer': [('name', ['OutdoorAirMixers', 'validOASysEquipmentNames'])],
    'OutdoorAir:Node': [('name', ['OutdoorAirNodeNames'])],
    'OutputControl:SurfaceColorScheme': [('name', ['ColorSchemes'])],
    'People': [('name', ['PeopleNames'])],
    'PhotovoltaicPerformance:EquivalentOne-Diode': [('name', ['PVModules'])],
    'PhotovoltaicPerformance:Sandia': [('name', ['PVModules'])],
    'PhotovoltaicPerformance:Simple': [('name', ['PVModules'])],
    'Pipe:Adiabatic': [('name', ['validBranchEquipmentNames'])],
    'Pipe:Adiabatic:Steam': [('name', ['validBranchEquipmentNames'])],
    'Pipe:Indoor': [('name', ['validBranchEquipmentNames'])],
    'Pipe:Outdoor': [('name', ['validBranchEquipmentNames'])],
    'Pipe:Underground': [('name', ['validBranchEquipmentNames'])],
    'PipingSystem:Underground:PipeCircuit': [
        (
            'name',
            [
                'PipingSystemUndergroundCircuitNames',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'PipingSystem:Underground:PipeSegment': [
        ('name', ['PipingSystemUndergroundSegmentNames'])
    ],
    'PlantComponent:TemperatureSource': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'PlantComponent:UserDefined': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'PlantEquipmentList': [('name', ['PlantAndCondenserEquipmentLists'])],
    'PlantEquipmentOperation:ChillerHeaterChangeover': [
        ('name', ['ControlSchemeList'])
    ],
    'PlantEquipmentOperation:ComponentSetpoint': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:CoolingLoad': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:HeatingLoad': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:OutdoorDewpoint': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:OutdoorDewpointDifference': [
        ('name', ['ControlSchemeList'])
    ],
    'PlantEquipmentOperation:OutdoorDryBulb': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:OutdoorDryBulbDifference': [
        ('name', ['ControlSchemeList'])
    ],
    'PlantEquipmentOperation:OutdoorRelativeHumidity': [
        ('name', ['ControlSchemeList'])
    ],
    'PlantEquipmentOperation:OutdoorWetBulb': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:OutdoorWetBulbDifference': [
        ('name', ['ControlSchemeList'])
    ],
    'PlantEquipmentOperation:ThermalEnergyStorage': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperation:Uncontrolled': [('name', ['ControlSchemeList'])],
    'PlantEquipmentOperationSchemes': [('name', ['PlantOperationSchemes'])],
    'PlantLoop': [('name', ['PlantLoops'])],
    'Pump:ConstantSpeed': [('name', ['validBranchEquipmentNames'])],
    'Pump:VariableSpeed': [('name', ['validBranchEquipmentNames'])],
    'Pump:VariableSpeed:Condensate': [('name', ['validBranchEquipmentNames'])],
    'PythonPlugin:Instance': [('name', ['ProgramNames'])],
    'Refrigeration:AirChiller': [
        (
            'name',
            [
                'RefrigerationAirChillerNames',
                'RefrigerationCaseAndWalkInAndListNames',
                'RefrigerationCaseAndWalkInNames',
            ],
        )
    ],
    'Refrigeration:Case': [
        (
            'name',
            [
                'RefrigerationCaseAndWalkInAndListNames',
                'RefrigerationCaseAndWalkInNames',
            ],
        )
    ],
    'Refrigeration:CaseAndWalkInList': [
        ('name', ['RefrigerationCaseAndWalkInAndListNames'])
    ],
    'Refrigeration:Compressor': [
        (
            'name',
            ['RefrigerationCompressorAndListNames', 'RefrigerationCompressorNames'],
        )
    ],
    'Refrigeration:CompressorList': [('name', ['RefrigerationCompressorAndListNames'])],
    'Refrigeration:CompressorRack': [
        ('name', ['DesuperHeatingCoilSources', 'validBranchEquipmentNames'])
    ],
    'Refrigeration:Condenser:AirCooled': [
        ('name', ['DesuperHeatingCoilSources', 'RefrigerationAllTypesCondenserNames'])
    ],
    'Refrigeration:Condenser:Cascade': [
        (
            'name',
            [
                'RefrigerationAllTypesCondenserNames',
                'RefrigerationCascadeCondenserAndSecondarySystemNames',
                'RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames',
            ],
        )
    ],
    'Refrigeration:Condenser:EvaporativeCooled': [
        ('name', ['DesuperHeatingCoilSources', 'RefrigerationAllTypesCondenserNames'])
    ],
    'Refrigeration:Condenser:WaterCooled': [
        (
            'name',
            [
                'DesuperHeatingCoilSources',
                'RefrigerationAllTypesCondenserNames',
                'validBranchEquipmentNames',
            ],
        )
    ],
    'Refrigeration:GasCooler:AirCooled': [
        ('name', ['RefrigerationAllTypesGasCoolerNames'])
    ],
    'Refrigeration:SecondarySystem': [
        (
            'name',
            [
                'RefrigerationCascadeCondenserAndSecondarySystemNames',
                'RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames',
            ],
        )
    ],
    'Refrigeration:Subcooler': [('name', ['RefrigerationSubcoolerNames'])],
    'Refrigeration:System': [('name', ['RefrigerationSystemNames'])],
    'Refrigeration:TranscriticalSystem': [('name', ['RefrigerationSystemNames'])],
    'Refrigeration:TransferLoadList': [
        (
            'name',
            ['RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames'],
        )
    ],
    'Refrigeration:WalkIn': [
        (
            'name',
            [
                'RefrigerationCaseAndWalkInAndListNames',
                'RefrigerationCaseAndWalkInNames',
            ],
        )
    ],
    'Roof': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'RoofCeiling:Detailed': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'RoomAir:Node': [('name', ['RoomAirNodes'])],
    'RoomAir:Node:AirflowNetwork': [('name', ['RoomAirflowNetworkNodes'])],
    'RoomAir:Node:AirflowNetwork:AdjacentSurfaceList': [
        ('name', ['RoomAirNodeSurfaceLists'])
    ],
    'RoomAir:Node:AirflowNetwork:HVACEquipment': [
        ('name', ['RoomAirNodeHVACEquipment'])
    ],
    'RoomAir:Node:AirflowNetwork:InternalGains': [('name', ['RoomAirNodeGains'])],
    'RunPeriod': [('name', ['RunPeriodsAndDesignDays'])],
    'Schedule:Compact': [('name', ['ScheduleNames'])],
    'Schedule:Constant': [('name', ['ScheduleNames'])],
    'Schedule:Day:Hourly': [('name', ['DayScheduleNames'])],
    'Schedule:Day:Interval': [('name', ['DayScheduleNames'])],
    'Schedule:Day:List': [('name', ['DayScheduleNames'])],
    'Schedule:File': [('name', ['ScheduleNames'])],
    'Schedule:Week:Compact': [('name', ['WeekScheduleNames'])],
    'Schedule:Week:Daily': [('name', ['WeekScheduleNames'])],
    'Schedule:Year': [('name', ['ScheduleNames'])],
    'ScheduleTypeLimits': [('name', ['ScheduleTypeLimitsNames'])],
    'Shading:Building': [('name', ['AllShadingAndHTSurfNames', 'AllShadingSurfNames'])],
    'Shading:Building:Detailed': [
        ('name', ['AllShadingAndHTSurfNames', 'AllShadingSurfNames'])
    ],
    'Shading:Fin': [
        (
            'name',
            [
                'AllShadingAndHTSurfNames',
                'AllShadingSurfNames',
                'AttachedShadingSurfNames',
            ],
        )
    ],
    'Shading:Fin:Projection': [
        (
            'name',
            [
                'AllShadingAndHTSurfNames',
                'AllShadingSurfNames',
                'AttachedShadingSurfNames',
            ],
        )
    ],
    'Shading:Overhang': [
        (
            'name',
            [
                'AllShadingAndHTSurfNames',
                'AllShadingSurfNames',
                'AttachedShadingSurfNames',
            ],
        )
    ],
    'Shading:Overhang:Projection': [
        (
            'name',
            [
                'AllShadingAndHTSurfNames',
                'AllShadingSurfNames',
                'AttachedShadingSurfNames',
            ],
        )
    ],
    'Shading:Site': [('name', ['AllShadingAndHTSurfNames', 'AllShadingSurfNames'])],
    'Shading:Site:Detailed': [
        ('name', ['AllShadingAndHTSurfNames', 'AllShadingSurfNames'])
    ],
    'Shading:Zone:Detailed': [
        (
            'name',
            [
                'AllShadingAndHTSurfNames',
                'AllShadingSurfNames',
                'AttachedShadingSurfNames',
            ],
        )
    ],
    'Site:GroundTemperature:Undisturbed:FiniteDifference': [
        ('name', ['UndisturbedGroundTempModels'])
    ],
    'Site:GroundTemperature:Undisturbed:KusudaAchenbach': [
        ('name', ['UndisturbedGroundTempModels'])
    ],
    'Site:GroundTemperature:Undisturbed:Xing': [
        ('name', ['UndisturbedGroundTempModels'])
    ],
    'Site:SpectrumData': [('name', ['SpectrumDataNames'])],
    'SizingPeriod:DesignDay': [('name', ['RunPeriodsAndDesignDays'])],
    'SizingPeriod:WeatherFileConditionType': [('name', ['RunPeriodsAndDesignDays'])],
    'SizingPeriod:WeatherFileDays': [('name', ['RunPeriodsAndDesignDays'])],
    'SolarCollector:FlatPlate:PhotovoltaicThermal': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'SolarCollector:FlatPlate:Water': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'SolarCollector:IntegralCollectorStorage': [
        ('name', ['validBranchEquipmentNames', 'validPlantEquipmentNames'])
    ],
    'SolarCollector:UnglazedTranspired': [
        ('name', ['UTSCNames', 'validOASysEquipmentNames'])
    ],
    'SolarCollectorPerformance:FlatPlate': [
        ('name', ['FlatPlateSolarCollectorParameters'])
    ],
    'SolarCollectorPerformance:IntegralCollectorStorage': [
        ('name', ['CollectorStoragePerformance'])
    ],
    'SolarCollectorPerformance:PhotovoltaicThermal:BIPVT': [
        ('name', ['FlatPlatePVTParameters'])
    ],
    'SolarCollectorPerformance:PhotovoltaicThermal:Simple': [
        ('name', ['FlatPlatePVTParameters'])
    ],
    'Space': [
        (
            'name',
            [
                'OutFaceEnvNames',
                'SpaceAndSpaceListNames',
                'SpaceNames',
                'ZoneAndZoneListAndSpaceAndSpaceListNames',
            ],
        )
    ],
    'SpaceHVAC:ZoneEquipmentMixer': [('name', ['SpaceMixerNames'])],
    'SpaceHVAC:ZoneEquipmentSplitter': [('name', ['SpaceSplitterNames'])],
    'SpaceHVAC:ZoneReturnMixer': [('name', ['SpaceMixerNames'])],
    'SpaceList': [
        (
            'name',
            [
                'SpaceAndSpaceListNames',
                'SpaceListNames',
                'ZoneAndZoneListAndSpaceAndSpaceListNames',
            ],
        )
    ],
    'SurfaceConvectionAlgorithm:Inside:UserCurve': [
        ('name', ['UserConvectionInsideModels', 'UserConvectionModels'])
    ],
    'SurfaceConvectionAlgorithm:Outside:UserCurve': [
        ('name', ['UserConvectionModels', 'UserConvectionOutsideModels'])
    ],
    'SurfaceProperty:GroundSurfaces': [('name', ['GroundSurfacesNames'])],
    'SurfaceProperty:LocalEnvironment': [('name', ['SurfaceLocalEnvironmentNames'])],
    'SurfaceProperty:OtherSideCoefficients': [('name', ['OutFaceEnvNames'])],
    'SurfaceProperty:OtherSideConditionsModel': [
        ('name', ['OSCMNames', 'OutFaceEnvNames'])
    ],
    'SurfaceProperty:SurroundingSurfaces': [('name', ['SurroundingSurfacesNames'])],
    'SurfaceProperty:Underwater': [('name', ['SurfacePropUnderWaterNames'])],
    'SwimmingPool:Indoor': [('name', ['validBranchEquipmentNames'])],
    'Table:IndependentVariable': [('name', ['IndependentVariableName'])],
    'Table:IndependentVariableList': [('name', ['IndependentVariableListName'])],
    'Table:Lookup': [
        (
            'name',
            [
                'BivariateFunctions',
                'MultivariateFunctions',
                'QuadvariateFunctions',
                'QuintvariateFunctions',
                'TrivariateFunctions',
                'UnivariateFunctions',
            ],
        )
    ],
    'TemperingValve': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'ThermalStorage:ChilledWater:Mixed': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'ThermalStorage:ChilledWater:Stratified': [
        (
            'name',
            [
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'ThermalStorage:Ice:Detailed': [
        (
            'name',
            [
                'IceThermalStorageEquipment',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'ThermalStorage:Ice:Simple': [
        ('name', ['IceThermalStorageEquipment', 'validBranchEquipmentNames'])
    ],
    'ThermostatSetpoint:DualSetpoint': [('name', ['ControlTypeNames'])],
    'ThermostatSetpoint:SingleCooling': [('name', ['ControlTypeNames'])],
    'ThermostatSetpoint:SingleHeating': [('name', ['ControlTypeNames'])],
    'ThermostatSetpoint:SingleHeatingOrCooling': [('name', ['ControlTypeNames'])],
    'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint': [
        ('name', ['ThermalComfortControlTypeNames'])
    ],
    'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling': [
        ('name', ['ThermalComfortControlTypeNames'])
    ],
    'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating': [
        ('name', ['ThermalComfortControlTypeNames'])
    ],
    'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling': [
        ('name', ['ThermalComfortControlTypeNames'])
    ],
    'UnitarySystemPerformance:Multispeed': [
        ('name', ['UnitarySystemPerformanceNames'])
    ],
    'UtilityCost:Tariff': [('name', ['UtilityCostTariffs'])],
    'Wall:Adiabatic': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Wall:Detailed': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Wall:Exterior': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Wall:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'Wall:Underground': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'RadiantSurfaceNames',
                'SurfAndSubSurfNames',
                'SurfaceNames',
            ],
        )
    ],
    'WaterHeater:HeatPump:PumpedCondenser': [
        (
            'name',
            [
                'ZoneEquipmentNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'WaterHeater:HeatPump:WrappedCondenser': [
        (
            'name',
            [
                'ZoneEquipmentNames',
                'validBranchEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'WaterHeater:Mixed': [
        (
            'name',
            [
                'WaterHeaterMixedNames',
                'WaterHeaterNames',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'WaterHeater:Stratified': [
        (
            'name',
            [
                'WaterHeaterNames',
                'WaterHeaterStratifiedNames',
                'validBranchEquipmentNames',
                'validCondenserEquipmentNames',
                'validPlantEquipmentNames',
            ],
        )
    ],
    'WaterUse:Connections': [('name', ['validBranchEquipmentNames'])],
    'WaterUse:Equipment': [('name', ['WaterUseEquipmentNames'])],
    'WaterUse:Storage': [('name', ['WaterStorageTankNames'])],
    'Window': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'GlazedExtSubSurfNames',
                'OutFaceEnvNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'Window:Interzone': [
        (
            'name',
            [
                'AllHeatTranAngFacNames',
                'AllHeatTranSurfNames',
                'AllShadingAndHTSurfNames',
                'OutFaceEnvNames',
                'SubSurfNames',
                'SurfAndSubSurfNames',
            ],
        )
    ],
    'WindowGap:DeflectionState': [('name', ['WindowGapDeflectionStates'])],
    'WindowGap:SupportPillar': [('name', ['WindowGapSupportPillars'])],
    'WindowMaterial:Blind': [
        ('name', ['MaterialName', 'WindowShadesScreensAndBlinds'])
    ],
    'WindowMaterial:Blind:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:ComplexShade': [('name', ['WindowComplexShades'])],
    'WindowMaterial:Drape:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:Gap': [('name', ['CFSGap'])],
    'WindowMaterial:Gap:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:Gas': [('name', ['MaterialName', 'WindowGasAndGasMixtures'])],
    'WindowMaterial:GasMixture': [
        ('name', ['MaterialName', 'WindowGasAndGasMixtures'])
    ],
    'WindowMaterial:Glazing': [
        ('name', ['CFSGlazingName', 'GlazingMaterialName', 'MaterialName'])
    ],
    'WindowMaterial:Glazing:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:Glazing:RefractionExtinctionMethod': [
        ('name', ['GlazingMaterialName', 'MaterialName'])
    ],
    'WindowMaterial:GlazingGroup:Thermochromic': [
        ('name', ['GlazingMaterialName', 'MaterialName'])
    ],
    'WindowMaterial:Screen': [
        ('name', ['MaterialName', 'WindowShadesScreensAndBlinds'])
    ],
    'WindowMaterial:Screen:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:Shade': [
        ('name', ['MaterialName', 'WindowShadesScreensAndBlinds'])
    ],
    'WindowMaterial:Shade:EquivalentLayer': [
        ('name', ['WindowEquivalentLayerMaterialNames'])
    ],
    'WindowMaterial:SimpleGlazingSystem': [
        ('name', ['GlazingMaterialName', 'MaterialName'])
    ],
    'WindowProperty:FrameAndDivider': [('name', ['WindowFrameAndDividerNames'])],
    'WindowShadingControl': [('name', ['WindowShadeControlNames'])],
    'WindowThermalModel:Params': [('name', ['WindowThermalModelParameters'])],
    'Zone': [
        (
            'name',
            [
                'AirflowNetworkNodeAndZoneNames',
                'OutFaceEnvNames',
                'ZoneAndZoneListAndSpaceAndSpaceListNames',
                'ZoneAndZoneListNames',
                'ZoneNames',
            ],
        )
    ],
    'ZoneControl:Humidistat': [('name', ['ZoneControlHumidistatNames'])],
    'ZoneControl:Thermostat': [('name', ['ZoneControlThermostaticNames'])],
    'ZoneControl:Thermostat:StagedDualSetpoint': [
        ('name', ['ZoneControlThermostaticNames'])
    ],
    'ZoneEarthtube:Parameters': [
        ('earth_tube_model_parameters_name', ['EarthTubeParameterNames'])
    ],
    'ZoneHVAC:AirDistributionUnit': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:Baseboard:Convective:Electric': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:Baseboard:Convective:Water': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:Baseboard:RadiantConvective:Electric': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:Baseboard:RadiantConvective:Steam': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:Baseboard:RadiantConvective:Steam:Design': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:Baseboard:RadiantConvective:Water': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:Baseboard:RadiantConvective:Water:Design': [
        ('name', ['BaseboardDesignObject'])
    ],
    'ZoneHVAC:CoolingPanel:RadiantConvective:Water': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:Dehumidifier:DX': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:EnergyRecoveryVentilator': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:EnergyRecoveryVentilator:Controller': [
        ('name', ['ControllerStandAloneEnergyRecoveryVentilator'])
    ],
    'ZoneHVAC:EquipmentList': [('name', ['ZoneEquipmentLists'])],
    'ZoneHVAC:EvaporativeCoolerUnit': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:ForcedAir:UserDefined': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:FourPipeFanCoil': [('name', ['DOAToZonalUnit', 'ZoneEquipmentNames'])],
    'ZoneHVAC:HighTemperatureRadiant': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:HybridUnitaryHVAC': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:IdealLoadsAirSystem': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:LowTemperatureRadiant:ConstantFlow': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:LowTemperatureRadiant:ConstantFlow:Design': [
        ('name', ['RadiantDesignObject'])
    ],
    'ZoneHVAC:LowTemperatureRadiant:Electric': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:LowTemperatureRadiant:SurfaceGroup': [('name', ['RadiantGroupNames'])],
    'ZoneHVAC:LowTemperatureRadiant:VariableFlow': [
        ('name', ['ZoneEquipmentNames', 'validBranchEquipmentNames'])
    ],
    'ZoneHVAC:LowTemperatureRadiant:VariableFlow:Design': [
        ('name', ['RadiantDesignObject'])
    ],
    'ZoneHVAC:OutdoorAirUnit': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:OutdoorAirUnit:EquipmentList': [
        ('name', ['OutdoorAirUnitEquipmentLists'])
    ],
    'ZoneHVAC:PackagedTerminalAirConditioner': [
        ('name', ['DOAToZonalUnit', 'ZoneEquipmentNames'])
    ],
    'ZoneHVAC:PackagedTerminalHeatPump': [
        ('name', ['DOAToZonalUnit', 'ZoneEquipmentNames'])
    ],
    'ZoneHVAC:RefrigerationChillerSet': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow': [
        (
            'name',
            [
                'DOAToZonalUnit',
                'ZoneEquipmentNames',
                'ZoneTerminalUnitNames',
                'validBranchEquipmentNames',
                'validOASysEquipmentNames',
            ],
        )
    ],
    'ZoneHVAC:UnitHeater': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:UnitVentilator': [('name', ['DOAToZonalUnit', 'ZoneEquipmentNames'])],
    'ZoneHVAC:VentilatedSlab': [('name', ['ZoneEquipmentNames'])],
    'ZoneHVAC:VentilatedSlab:SlabGroup': [('name', ['VentSlabGroupNames'])],
    'ZoneHVAC:WaterToAirHeatPump': [('name', ['DOAToZonalUnit', 'ZoneEquipmentNames'])],
    'ZoneHVAC:WindowAirConditioner': [('name', ['ZoneEquipmentNames'])],
    'ZoneList': [
        (
            'name',
            [
                'ZoneAndZoneListAndSpaceAndSpaceListNames',
                'ZoneAndZoneListNames',
                'ZoneListNames',
            ],
        )
    ],
    'ZoneProperty:LocalEnvironment': [('name', ['ZoneLocalEnvironmentNames'])],
    'ZoneTerminalUnitList': [
        ('zone_terminal_unit_list_name', ['ZoneTerminalUnitListNames'])
    ],
    'ZoneVentilation:DesignFlowRate': [('name', ['VentilationNames'])],
    'ZoneVentilation:WindandStackOpenArea': [('name', ['VentilationNames'])],
}


REF_GROUP_PROVIDERS: dict[str, frozenset[str]] = {
    'AFNCoilNames': frozenset(
        {
            'Coil:Cooling:DX',
            'Coil:Cooling:DX:MultiSpeed',
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'Coil:Cooling:DX:TwoSpeed',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:DX:MultiSpeed',
            'Coil:Heating:DX:SingleSpeed',
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Water',
        }
    ),
    'AFNHeatExchangerNames': frozenset(
        {
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
            'HeatExchanger:Desiccant:BalancedFlow',
        }
    ),
    'AFNOutdoorAirFlowNames': frozenset(
        {
            'AirflowNetwork:Distribution:Component:OutdoorAirFlow',
        }
    ),
    'AFNReliefAirFlowNames': frozenset(
        {
            'AirflowNetwork:Distribution:Component:ReliefAirFlow',
        }
    ),
    'AFNTerminalUnitNames': frozenset(
        {
            'AirTerminal:SingleDuct:ConstantVolume:NoReheat',
            'AirTerminal:SingleDuct:ConstantVolume:Reheat',
            'AirTerminal:SingleDuct:VAV:Reheat',
        }
    ),
    'AirFlowNetworkMultizoneZones': frozenset(
        {
            'AirflowNetwork:MultiZone:Zone',
        }
    ),
    'AirLoopControllers': frozenset(
        {
            'Controller:OutdoorAir',
            'Controller:WaterCoil',
        }
    ),
    'AirLoopHVACMixerNames': frozenset(
        {
            'AirLoopHVAC:Mixer',
        }
    ),
    'AirLoopHVACSplitterNames': frozenset(
        {
            'AirLoopHVAC:Splitter',
        }
    ),
    'AirLoopOAEquipmentLists': frozenset(
        {
            'AirLoopHVAC:OutdoorAirSystem:EquipmentList',
        }
    ),
    'AirPrimaryLoops': frozenset(
        {
            'AirLoopHVAC',
        }
    ),
    'AirTerminalUnitNames': frozenset(
        {
            'AirTerminal:DualDuct:ConstantVolume',
            'AirTerminal:DualDuct:VAV',
            'AirTerminal:DualDuct:VAV:OutdoorAir',
            'AirTerminal:SingleDuct:ConstantVolume:CooledBeam',
            'AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam',
            'AirTerminal:SingleDuct:ConstantVolume:FourPipeInduction',
            'AirTerminal:SingleDuct:ConstantVolume:NoReheat',
            'AirTerminal:SingleDuct:ConstantVolume:Reheat',
            'AirTerminal:SingleDuct:Mixer',
            'AirTerminal:SingleDuct:ParallelPIU:Reheat',
            'AirTerminal:SingleDuct:SeriesPIU:Reheat',
            'AirTerminal:SingleDuct:UserDefined',
            'AirTerminal:SingleDuct:VAV:HeatAndCool:NoReheat',
            'AirTerminal:SingleDuct:VAV:HeatAndCool:Reheat',
            'AirTerminal:SingleDuct:VAV:NoReheat',
            'AirTerminal:SingleDuct:VAV:Reheat',
            'AirTerminal:SingleDuct:VAV:Reheat:VariableSpeedFan',
        }
    ),
    'AirflowNetwork LinkageNames': frozenset(
        {
            'AirflowNetwork:IntraZone:Linkage',
        }
    ),
    'AirflowNetworkComponentNames': frozenset(
        {
            'AirflowNetwork:Distribution:Component:Coil',
            'AirflowNetwork:Distribution:Component:ConstantPressureDrop',
            'AirflowNetwork:Distribution:Component:Duct',
            'AirflowNetwork:Distribution:Component:Fan',
            'AirflowNetwork:Distribution:Component:HeatExchanger',
            'AirflowNetwork:Distribution:Component:Leak',
            'AirflowNetwork:Distribution:Component:LeakageRatio',
            'AirflowNetwork:Distribution:Component:OutdoorAirFlow',
            'AirflowNetwork:Distribution:Component:ReliefAirFlow',
            'AirflowNetwork:Distribution:Component:TerminalUnit',
        }
    ),
    'AirflowNetworkNodeAndZoneNames': frozenset(
        {
            'AirflowNetwork:Distribution:Node',
            'Zone',
        }
    ),
    'AirflowNetworkNodeNames': frozenset(
        {
            'AirflowNetwork:IntraZone:Node',
        }
    ),
    'AirflowNetworkOccupantVentilationControlNames': frozenset(
        {
            'AirflowNetwork:OccupantVentilationControl',
        }
    ),
    'AirflowNetworkZoneControlPressureControllerNames': frozenset(
        {
            'AirflowNetwork:ZoneControl:PressureController',
        }
    ),
    'AllHeatTranAngFacNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'ComfortViewFactorAngles',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'InternalMass',
            'Roof',
            'RoofCeiling:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
            'Window',
            'Window:Interzone',
        }
    ),
    'AllHeatTranSurfNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'InternalMass',
            'Roof',
            'RoofCeiling:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
            'Window',
            'Window:Interzone',
        }
    ),
    'AllShadingAndHTSurfNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'Roof',
            'RoofCeiling:Detailed',
            'Shading:Building',
            'Shading:Building:Detailed',
            'Shading:Fin',
            'Shading:Fin:Projection',
            'Shading:Overhang',
            'Shading:Overhang:Projection',
            'Shading:Site',
            'Shading:Site:Detailed',
            'Shading:Zone:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
            'Window',
            'Window:Interzone',
        }
    ),
    'AllShadingSurfNames': frozenset(
        {
            'Shading:Building',
            'Shading:Building:Detailed',
            'Shading:Fin',
            'Shading:Fin:Projection',
            'Shading:Overhang',
            'Shading:Overhang:Projection',
            'Shading:Site',
            'Shading:Site:Detailed',
            'Shading:Zone:Detailed',
        }
    ),
    'AttachedShadingSurfNames': frozenset(
        {
            'Shading:Fin',
            'Shading:Fin:Projection',
            'Shading:Overhang',
            'Shading:Overhang:Projection',
            'Shading:Zone:Detailed',
        }
    ),
    'BaseboardDesignObject': frozenset(
        {
            'ZoneHVAC:Baseboard:RadiantConvective:Water:Design',
        }
    ),
    'BivariateFunctions': frozenset(
        {
            'Curve:Bicubic',
            'Curve:Biquadratic',
            'Curve:CubicLinear',
            'Curve:FanPressureRise',
            'Curve:QuadraticLinear',
            'Table:Lookup',
        }
    ),
    'Boilers': frozenset(
        {
            'Boiler:HotWater',
        }
    ),
    'BranchLists': frozenset(
        {
            'BranchList',
        }
    ),
    'Branches': frozenset(
        {
            'Branch',
        }
    ),
    'CFSGap': frozenset(
        {
            'WindowMaterial:Gap',
        }
    ),
    'CFSGlazingName': frozenset(
        {
            'WindowMaterial:Glazing',
        }
    ),
    'ChillerHeaterEIRNames': frozenset(
        {
            'ChillerHeaterPerformance:Electric:EIR',
        }
    ),
    'Chillers': frozenset(
        {
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
        }
    ),
    'CoilCoolingDX': frozenset(
        {
            'Coil:Cooling:DX',
        }
    ),
    'CoilPerformanceDX': frozenset(
        {
            'CoilPerformance:DX:Cooling',
        }
    ),
    'CollectorStoragePerformance': frozenset(
        {
            'SolarCollectorPerformance:IntegralCollectorStorage',
        }
    ),
    'ColorSchemes': frozenset(
        {
            'OutputControl:SurfaceColorScheme',
        }
    ),
    'CompactHVACSystemConstantVolume': frozenset(
        {
            'HVACTemplate:System:ConstantVolume',
        }
    ),
    'CompactHVACSystemDualDuct': frozenset(
        {
            'HVACTemplate:System:DualDuct',
        }
    ),
    'CompactHVACSystemUnitary': frozenset(
        {
            'HVACTemplate:System:Unitary',
            'HVACTemplate:System:UnitaryHeatPump:AirToAir',
            'HVACTemplate:System:UnitarySystem',
        }
    ),
    'CompactHVACSystemVAV': frozenset(
        {
            'HVACTemplate:System:PackagedVAV',
            'HVACTemplate:System:VAV',
        }
    ),
    'CompactHVACSystemVRF': frozenset(
        {
            'HVACTemplate:System:VRF',
        }
    ),
    'CompactHVACThermostats': frozenset(
        {
            'HVACTemplate:Thermostat',
        }
    ),
    'ComplexFenestrationStates': frozenset(
        {
            'Construction:ComplexFenestrationState',
        }
    ),
    'CondenserEquipmentLists': frozenset(
        {
            'CondenserEquipmentList',
        }
    ),
    'CondenserOperationSchemes': frozenset(
        {
            'CondenserEquipmentOperationSchemes',
        }
    ),
    'ConnectorLists': frozenset(
        {
            'ConnectorList',
        }
    ),
    'ConstructionNames': frozenset(
        {
            'Construction',
            'Construction:AirBoundary',
            'Construction:CfactorUndergroundWall',
            'Construction:FfactorGroundFloor',
            'Construction:WindowDataFile',
            'Construction:WindowEquivalentLayer',
        }
    ),
    'ControlSchemeList': frozenset(
        {
            'PlantEquipmentOperation:ChillerHeaterChangeover',
            'PlantEquipmentOperation:ComponentSetpoint',
            'PlantEquipmentOperation:CoolingLoad',
            'PlantEquipmentOperation:HeatingLoad',
            'PlantEquipmentOperation:OutdoorDewpoint',
            'PlantEquipmentOperation:OutdoorDewpointDifference',
            'PlantEquipmentOperation:OutdoorDryBulb',
            'PlantEquipmentOperation:OutdoorDryBulbDifference',
            'PlantEquipmentOperation:OutdoorRelativeHumidity',
            'PlantEquipmentOperation:OutdoorWetBulb',
            'PlantEquipmentOperation:OutdoorWetBulbDifference',
            'PlantEquipmentOperation:ThermalEnergyStorage',
            'PlantEquipmentOperation:Uncontrolled',
        }
    ),
    'ControlTypeNames': frozenset(
        {
            'ThermostatSetpoint:DualSetpoint',
            'ThermostatSetpoint:SingleCooling',
            'ThermostatSetpoint:SingleHeating',
            'ThermostatSetpoint:SingleHeatingOrCooling',
        }
    ),
    'ControllerLists': frozenset(
        {
            'AirLoopHVAC:ControllerList',
        }
    ),
    'ControllerMechanicalVentNames': frozenset(
        {
            'Controller:MechanicalVentilation',
        }
    ),
    'ControllerStandAloneEnergyRecoveryVentilator': frozenset(
        {
            'ZoneHVAC:EnergyRecoveryVentilator:Controller',
        }
    ),
    'ConverterList': frozenset(
        {
            'ElectricLoadCenter:Storage:Converter',
        }
    ),
    'CoolingCoilName': frozenset(
        {
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
        }
    ),
    'CoolingCoilSystemName': frozenset(
        {
            'CoilSystem:Cooling:DX',
        }
    ),
    'CoolingCoilsDX': frozenset(
        {
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'Coil:Cooling:DX:TwoSpeed',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'CoilSystem:Cooling:DX:HeatExchangerAssisted',
        }
    ),
    'CoolingCoilsDXMultiModeOrSingleSpeed': frozenset(
        {
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'CoilSystem:Cooling:DX:HeatExchangerAssisted',
        }
    ),
    'CoolingCoilsDXMultiSpeed': frozenset(
        {
            'Coil:Cooling:DX:MultiSpeed',
        }
    ),
    'CoolingCoilsDXSingleSpeed': frozenset(
        {
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'CoilSystem:Cooling:DX:HeatExchangerAssisted',
        }
    ),
    'CoolingCoilsDXVarRefrigFlow': frozenset(
        {
            'Coil:Cooling:DX:VariableRefrigerantFlow',
        }
    ),
    'CoolingCoilsDXVarRefrigFlowFluidTemperatureControl': frozenset(
        {
            'Coil:Cooling:DX:VariableRefrigerantFlow:FluidTemperatureControl',
        }
    ),
    'CoolingCoilsDXVariableSpeed': frozenset(
        {
            'Coil:Cooling:DX:VariableSpeed',
        }
    ),
    'CoolingCoilsWater': frozenset(
        {
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'CoilSystem:Cooling:Water:HeatExchangerAssisted',
        }
    ),
    'CoolingCoilsWaterNoHX': frozenset(
        {
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
        }
    ),
    'CoolingCoilsWaterToAirHP': frozenset(
        {
            'Coil:Cooling:WaterToAirHeatPump:EquationFit',
            'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
        }
    ),
    'CoolingCoilsWaterToAirVSHP': frozenset(
        {
            'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
        }
    ),
    'CoolingTowers': frozenset(
        {
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed',
            'CoolingTower:VariableSpeed:Merkel',
        }
    ),
    'CoolingTowersWithUA': frozenset(
        {
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed:Merkel',
        }
    ),
    'DOASAirLoops': frozenset(
        {
            'AirLoopHVAC:DedicatedOutdoorAirSystem',
        }
    ),
    'DOAToZonalUnit': frozenset(
        {
            'AirLoopHVAC:UnitarySystem',
            'ZoneHVAC:FourPipeFanCoil',
            'ZoneHVAC:PackagedTerminalAirConditioner',
            'ZoneHVAC:PackagedTerminalHeatPump',
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
            'ZoneHVAC:UnitVentilator',
            'ZoneHVAC:WaterToAirHeatPump',
        }
    ),
    'DSOASpaceListNames': frozenset(
        {
            'DesignSpecification:OutdoorAir:SpaceList',
        }
    ),
    'DXCoolingOperatingModeNames': frozenset(
        {
            'Coil:Cooling:DX:CurveFit:OperatingMode',
        }
    ),
    'DXCoolingPerformanceNames': frozenset(
        {
            'Coil:Cooling:DX:CurveFit:Performance',
        }
    ),
    'DXCoolingSpeedNames': frozenset(
        {
            'Coil:Cooling:DX:CurveFit:Speed',
        }
    ),
    'DataMatrices': frozenset(
        {
            'Matrix:TwoDimension',
        }
    ),
    'DayScheduleNames': frozenset(
        {
            'Schedule:Day:Hourly',
            'Schedule:Day:Interval',
            'Schedule:Day:List',
        }
    ),
    'DaylightReferencePointNames': frozenset(
        {
            'Daylighting:ReferencePoint',
        }
    ),
    'DaylightingControlNames': frozenset(
        {
            'Daylighting:Controls',
        }
    ),
    'DemandManagerNames': frozenset(
        {
            'DemandManager:ElectricEquipment',
            'DemandManager:ExteriorLights',
            'DemandManager:Lights',
            'DemandManager:Thermostats',
            'DemandManager:Ventilation',
        }
    ),
    'DesiccantHXPerfData': frozenset(
        {
            'HeatExchanger:Desiccant:BalancedFlow:PerformanceDataType1',
        }
    ),
    'DesignSpecificationAirTerminalSizingName': frozenset(
        {
            'DesignSpecification:AirTerminal:Sizing',
        }
    ),
    'DesignSpecificationOutdoorAirNames': frozenset(
        {
            'DesignSpecification:OutdoorAir',
        }
    ),
    'DesignSpecificationZoneAirDistributionNames': frozenset(
        {
            'DesignSpecification:ZoneAirDistribution',
        }
    ),
    'DesignSpecificationZoneHVACSizingName': frozenset(
        {
            'DesignSpecification:ZoneHVAC:Sizing',
        }
    ),
    'DesuperHeatingCoilSources': frozenset(
        {
            'Coil:Cooling:DX',
            'Coil:Cooling:DX:SingleSpeed',
            'Coil:Cooling:DX:TwoSpeed',
            'Coil:Cooling:DX:TwoStageWithHumidityControlMode',
            'Coil:Cooling:DX:VariableSpeed',
            'Refrigeration:CompressorRack',
            'Refrigeration:Condenser:AirCooled',
            'Refrigeration:Condenser:EvaporativeCooled',
            'Refrigeration:Condenser:WaterCooled',
        }
    ),
    'DesuperHeatingWaterOnlySources': frozenset(
        {
            'Coil:Cooling:DX:MultiSpeed',
            'Coil:Cooling:WaterToAirHeatPump:EquationFit',
            'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
        }
    ),
    'EarthTubeParameterNames': frozenset(
        {
            'ZoneEarthtube:Parameters',
        }
    ),
    'ElecStorageList': frozenset(
        {
            'ElectricLoadCenter:Storage:Battery',
            'ElectricLoadCenter:Storage:LiIonNMCBattery',
            'ElectricLoadCenter:Storage:Simple',
        }
    ),
    'ElectricEquipmentNames': frozenset(
        {
            'ElectricEquipment',
        }
    ),
    'ErlProgramNames': frozenset(
        {
            'EnergyManagementSystem:Program',
            'EnergyManagementSystem:Subroutine',
        }
    ),
    'EvapCoolerNames': frozenset(
        {
            'EvaporativeCooler:Direct:CelDekPad',
            'EvaporativeCooler:Direct:ResearchSpecial',
            'EvaporativeCooler:Indirect:CelDekPad',
            'EvaporativeCooler:Indirect:ResearchSpecial',
            'EvaporativeCooler:Indirect:WetCoil',
        }
    ),
    'ExteriorLightsNames': frozenset(
        {
            'Exterior:Lights',
        }
    ),
    'ExternalNodeNames': frozenset(
        {
            'AirflowNetwork:MultiZone:ExternalNode',
        }
    ),
    'FCAirSupNames': frozenset(
        {
            'Generator:FuelCell:AirSupply',
        }
    ),
    'FCAuxHeatNames': frozenset(
        {
            'Generator:FuelCell:AuxiliaryHeater',
        }
    ),
    'FCExhaustHXNames': frozenset(
        {
            'Generator:FuelCell:ExhaustGasToWaterHeatExchanger',
        }
    ),
    'FCInverterNames': frozenset(
        {
            'Generator:FuelCell:Inverter',
        }
    ),
    'FCPMNames': frozenset(
        {
            'Generator:FuelCell:PowerModule',
        }
    ),
    'FCStackCoolerNames': frozenset(
        {
            'Generator:FuelCell:StackCooler',
        }
    ),
    'FCStorageNames': frozenset(
        {
            'Generator:FuelCell:ElectricalStorage',
        }
    ),
    'FCWaterSupNames': frozenset(
        {
            'Generator:FuelCell:WaterSupply',
        }
    ),
    'FMUFileName': frozenset(
        {
            'ExternalInterface:FunctionalMockupUnitImport',
        }
    ),
    'Fans': frozenset(
        {
            'Fan:ComponentModel',
            'Fan:ConstantVolume',
            'Fan:OnOff',
            'Fan:SystemModel',
            'Fan:VariableVolume',
        }
    ),
    'FansCV': frozenset(
        {
            'Fan:ConstantVolume',
        }
    ),
    'FansCVandOnOff': frozenset(
        {
            'Fan:ConstantVolume',
            'Fan:OnOff',
        }
    ),
    'FansCVandOnOffandVAV': frozenset(
        {
            'Fan:ConstantVolume',
            'Fan:OnOff',
            'Fan:VariableVolume',
        }
    ),
    'FansCVandVAV': frozenset(
        {
            'Fan:ConstantVolume',
            'Fan:VariableVolume',
        }
    ),
    'FansComponentModel': frozenset(
        {
            'Fan:ComponentModel',
        }
    ),
    'FansOnOff': frozenset(
        {
            'Fan:OnOff',
        }
    ),
    'FansOnOffandVAV': frozenset(
        {
            'Fan:OnOff',
            'Fan:VariableVolume',
        }
    ),
    'FansSystemModel': frozenset(
        {
            'Fan:SystemModel',
        }
    ),
    'FansVAV': frozenset(
        {
            'Fan:VariableVolume',
        }
    ),
    'FansZoneExhaust': frozenset(
        {
            'Fan:ZoneExhaust',
        }
    ),
    'FlatPlatePVTParameters': frozenset(
        {
            'SolarCollectorPerformance:PhotovoltaicThermal:BIPVT',
            'SolarCollectorPerformance:PhotovoltaicThermal:Simple',
        }
    ),
    'FlatPlateSolarCollectorParameters': frozenset(
        {
            'SolarCollectorPerformance:FlatPlate',
        }
    ),
    'FloorSurfaceNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
        }
    ),
    'FluidAndGlycolNames': frozenset(
        {
            'FluidProperties:GlycolConcentration',
            'FluidProperties:Name',
        }
    ),
    'FluidNames': frozenset(
        {
            'FluidProperties:Name',
        }
    ),
    'FluidPropertyTemperatures': frozenset(
        {
            'FluidProperties:Temperatures',
        }
    ),
    'GenFuelSupNames': frozenset(
        {
            'Generator:FuelSupply',
        }
    ),
    'GeneratorLists': frozenset(
        {
            'ElectricLoadCenter:Generators',
        }
    ),
    'GeneratorNames': frozenset(
        {
            'Generator:CombustionTurbine',
            'Generator:FuelCell',
            'Generator:InternalCombustionEngine',
            'Generator:MicroCHP',
            'Generator:MicroTurbine',
            'Generator:PVWatts',
            'Generator:Photovoltaic',
            'Generator:WindTurbine',
        }
    ),
    'GlazedExtSubSurfNames': frozenset(
        {
            'FenestrationSurface:Detailed',
            'GlazedDoor',
            'Window',
        }
    ),
    'GlazingMaterialName': frozenset(
        {
            'WindowMaterial:Glazing',
            'WindowMaterial:Glazing:RefractionExtinctionMethod',
            'WindowMaterial:GlazingGroup:Thermochromic',
            'WindowMaterial:SimpleGlazingSystem',
        }
    ),
    'GroundHeatExchangerVerticalArrayNames': frozenset(
        {
            'GroundHeatExchanger:Vertical:Array',
        }
    ),
    'GroundHeatExchangerVerticalPropertiesNames': frozenset(
        {
            'GroundHeatExchanger:Vertical:Properties',
        }
    ),
    'GroundHeatExchangerVerticalResponseFactorNames': frozenset(
        {
            'GroundHeatExchanger:ResponseFactors',
        }
    ),
    'GroundHeatExchangerVerticalSingleNames': frozenset(
        {
            'GroundHeatExchanger:Vertical:Single',
        }
    ),
    'GroundSurfacesNames': frozenset(
        {
            'SurfaceProperty:GroundSurfaces',
        }
    ),
    'HVACTemplateConstantVolumeZones': frozenset(
        {
            'HVACTemplate:Zone:ConstantVolume',
        }
    ),
    'HVACTemplateDOASSystems': frozenset(
        {
            'HVACTemplate:System:DedicatedOutdoorAir',
        }
    ),
    'HVACTemplateSystems': frozenset(
        {
            'HVACTemplate:System:ConstantVolume',
            'HVACTemplate:System:DedicatedOutdoorAir',
            'HVACTemplate:System:DualDuct',
            'HVACTemplate:System:PackagedVAV',
            'HVACTemplate:System:Unitary',
            'HVACTemplate:System:UnitaryHeatPump:AirToAir',
            'HVACTemplate:System:UnitarySystem',
            'HVACTemplate:System:VAV',
            'HVACTemplate:System:VRF',
        }
    ),
    'HXAirToAirNames': frozenset(
        {
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
            'HeatExchanger:Desiccant:BalancedFlow',
        }
    ),
    'HXAirToAirSensibleAndLatentNames': frozenset(
        {
            'HeatExchanger:AirToAir:SensibleAndLatent',
        }
    ),
    'HXDesiccantBalanced': frozenset(
        {
            'HeatExchanger:Desiccant:BalancedFlow',
        }
    ),
    'HeatPumpAirToWaterFuelFiredCoolingNames': frozenset(
        {
            'HeatPump:AirToWater:FuelFired:Cooling',
        }
    ),
    'HeatPumpAirToWaterFuelFiredHeatingNames': frozenset(
        {
            'HeatPump:AirToWater:FuelFired:Heating',
        }
    ),
    'HeatPumpWaterHeaterDXCoilsPumped': frozenset(
        {
            'Coil:WaterHeating:AirToWaterHeatPump:Pumped',
        }
    ),
    'HeatPumpWaterHeaterDXCoilsVariableSpeed': frozenset(
        {
            'Coil:WaterHeating:AirToWaterHeatPump:VariableSpeed',
        }
    ),
    'HeatPumpWaterHeaterDXCoilsWrapped': frozenset(
        {
            'Coil:WaterHeating:AirToWaterHeatPump:Wrapped',
        }
    ),
    'HeatingCoilName': frozenset(
        {
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
        }
    ),
    'HeatingCoilSystemName': frozenset(
        {
            'CoilSystem:Heating:DX',
        }
    ),
    'HeatingCoilsDX': frozenset(
        {
            'Coil:Heating:DX:SingleSpeed',
            'Coil:Heating:DX:VariableRefrigerantFlow',
        }
    ),
    'HeatingCoilsDXMultiSpeed': frozenset(
        {
            'Coil:Heating:DX:MultiSpeed',
        }
    ),
    'HeatingCoilsDXSingleSpeed': frozenset(
        {
            'Coil:Heating:DX:SingleSpeed',
            'Coil:Heating:DX:VariableRefrigerantFlow',
        }
    ),
    'HeatingCoilsDXVarRefrigFlow': frozenset(
        {
            'Coil:Heating:DX:VariableRefrigerantFlow',
        }
    ),
    'HeatingCoilsDXVarRefrigFlowFluidTemperatureControl': frozenset(
        {
            'Coil:Heating:DX:VariableRefrigerantFlow:FluidTemperatureControl',
        }
    ),
    'HeatingCoilsDXVariableSpeed': frozenset(
        {
            'Coil:Heating:DX:VariableSpeed',
        }
    ),
    'HeatingCoilsDesuperheater': frozenset(
        {
            'Coil:Heating:Desuperheater',
        }
    ),
    'HeatingCoilsElectric': frozenset(
        {
            'Coil:Heating:Electric',
        }
    ),
    'HeatingCoilsElectricMultiStage': frozenset(
        {
            'Coil:Heating:Electric:MultiStage',
        }
    ),
    'HeatingCoilsGasMultiStage': frozenset(
        {
            'Coil:Heating:Gas:MultiStage',
        }
    ),
    'HeatingCoilsWater': frozenset(
        {
            'Coil:Heating:Water',
        }
    ),
    'HeatingCoilsWaterToAirHP': frozenset(
        {
            'Coil:Heating:WaterToAirHeatPump:EquationFit',
            'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
        }
    ),
    'HeatingCoilsWaterToAirVSHP': frozenset(
        {
            'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
        }
    ),
    'IceThermalStorageEquipment': frozenset(
        {
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
        }
    ),
    'IndependentVariableListName': frozenset(
        {
            'Table:IndependentVariableList',
        }
    ),
    'IndependentVariableName': frozenset(
        {
            'Table:IndependentVariable',
        }
    ),
    'IntegratedHeatPumps': frozenset(
        {
            'CoilSystem:IntegratedHeatPump:AirSource',
        }
    ),
    'InternalHeatSourceNames': frozenset(
        {
            'ConstructionProperty:InternalHeatSource',
        }
    ),
    'InverterList': frozenset(
        {
            'ElectricLoadCenter:Inverter:FunctionOfPower',
            'ElectricLoadCenter:Inverter:LookUpTable',
            'ElectricLoadCenter:Inverter:PVWatts',
            'ElectricLoadCenter:Inverter:Simple',
        }
    ),
    'LightsNames': frozenset(
        {
            'Lights',
        }
    ),
    'MaterialName': frozenset(
        {
            'Material',
            'Material:AirGap',
            'Material:InfraredTransparent',
            'Material:NoMass',
            'Material:RoofVegetation',
            'WindowMaterial:Blind',
            'WindowMaterial:Gas',
            'WindowMaterial:GasMixture',
            'WindowMaterial:Glazing',
            'WindowMaterial:Glazing:RefractionExtinctionMethod',
            'WindowMaterial:GlazingGroup:Thermochromic',
            'WindowMaterial:Screen',
            'WindowMaterial:Shade',
            'WindowMaterial:SimpleGlazingSystem',
        }
    ),
    'MicroCHPParametersNames': frozenset(
        {
            'Generator:MicroCHP:NonNormalizedParameters',
        }
    ),
    'MicroTurbineGeneratorNames': frozenset(
        {
            'Generator:MicroTurbine',
        }
    ),
    'MultivariateFunctions': frozenset(
        {
            'Table:Lookup',
        }
    ),
    'OAControllerNames': frozenset(
        {
            'Controller:OutdoorAir',
        }
    ),
    'OSCMNames': frozenset(
        {
            'SurfaceProperty:OtherSideConditionsModel',
        }
    ),
    'OutFaceEnvNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Interzone',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Detailed',
            'Floor:Interzone',
            'Foundation:Kiva',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'RoofCeiling:Detailed',
            'Space',
            'SurfaceProperty:OtherSideCoefficients',
            'SurfaceProperty:OtherSideConditionsModel',
            'Wall:Detailed',
            'Wall:Interzone',
            'Window',
            'Window:Interzone',
            'Zone',
        }
    ),
    'OutdoorAirMixers': frozenset(
        {
            'OutdoorAir:Mixer',
        }
    ),
    'OutdoorAirNodeNames': frozenset(
        {
            'OutdoorAir:Node',
        }
    ),
    'OutdoorAirUnitEquipmentLists': frozenset(
        {
            'ZoneHVAC:OutdoorAirUnit:EquipmentList',
        }
    ),
    'PLHPCoolingNames': frozenset(
        {
            'HeatPump:PlantLoop:EIR:Cooling',
        }
    ),
    'PLHPHeatingNames': frozenset(
        {
            'HeatPump:PlantLoop:EIR:Heating',
        }
    ),
    'PVGeneratorNames': frozenset(
        {
            'Generator:Photovoltaic',
        }
    ),
    'PVModules': frozenset(
        {
            'PhotovoltaicPerformance:EquivalentOne-Diode',
            'PhotovoltaicPerformance:Sandia',
            'PhotovoltaicPerformance:Simple',
        }
    ),
    'PeopleNames': frozenset(
        {
            'People',
        }
    ),
    'PipingSystemUndergroundCircuitNames': frozenset(
        {
            'PipingSystem:Underground:PipeCircuit',
        }
    ),
    'PipingSystemUndergroundSegmentNames': frozenset(
        {
            'PipingSystem:Underground:PipeSegment',
        }
    ),
    'PlantAndCondenserEquipmentLists': frozenset(
        {
            'CondenserEquipmentList',
            'PlantEquipmentList',
        }
    ),
    'PlantConnectors': frozenset(
        {
            'Connector:Mixer',
            'Connector:Splitter',
        }
    ),
    'PlantLoops': frozenset(
        {
            'CondenserLoop',
            'PlantLoop',
        }
    ),
    'PlantOperationSchemes': frozenset(
        {
            'PlantEquipmentOperationSchemes',
        }
    ),
    'ProgramNames': frozenset(
        {
            'EnergyManagementSystem:ProgramCallingManager',
            'PythonPlugin:Instance',
        }
    ),
    'QuadvariateFunctions': frozenset(
        {
            'Curve:QuadLinear',
            'Table:Lookup',
        }
    ),
    'QuintvariateFunctions': frozenset(
        {
            'Curve:QuintLinear',
            'Table:Lookup',
        }
    ),
    'RadiantDesignObject': frozenset(
        {
            'ZoneHVAC:LowTemperatureRadiant:ConstantFlow:Design',
            'ZoneHVAC:LowTemperatureRadiant:VariableFlow:Design',
        }
    ),
    'RadiantGroupNames': frozenset(
        {
            'ZoneHVAC:LowTemperatureRadiant:SurfaceGroup',
        }
    ),
    'RadiantSurfaceNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'InternalMass',
            'Roof',
            'RoofCeiling:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
        }
    ),
    'ReferenceCrackConditions': frozenset(
        {
            'AirflowNetwork:MultiZone:ReferenceCrackConditions',
        }
    ),
    'RefrigerationAirChillerNames': frozenset(
        {
            'Refrigeration:AirChiller',
        }
    ),
    'RefrigerationAllTypesCondenserNames': frozenset(
        {
            'Refrigeration:Condenser:AirCooled',
            'Refrigeration:Condenser:Cascade',
            'Refrigeration:Condenser:EvaporativeCooled',
            'Refrigeration:Condenser:WaterCooled',
        }
    ),
    'RefrigerationAllTypesGasCoolerNames': frozenset(
        {
            'Refrigeration:GasCooler:AirCooled',
        }
    ),
    'RefrigerationCascadeCondenserAndSecondarySystemNames': frozenset(
        {
            'Refrigeration:Condenser:Cascade',
            'Refrigeration:SecondarySystem',
        }
    ),
    'RefrigerationCaseAndWalkInAndListNames': frozenset(
        {
            'Refrigeration:AirChiller',
            'Refrigeration:Case',
            'Refrigeration:CaseAndWalkInList',
            'Refrigeration:WalkIn',
        }
    ),
    'RefrigerationCaseAndWalkInNames': frozenset(
        {
            'Refrigeration:AirChiller',
            'Refrigeration:Case',
            'Refrigeration:WalkIn',
        }
    ),
    'RefrigerationCompressorAndListNames': frozenset(
        {
            'Refrigeration:Compressor',
            'Refrigeration:CompressorList',
        }
    ),
    'RefrigerationCompressorNames': frozenset(
        {
            'Refrigeration:Compressor',
        }
    ),
    'RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames': frozenset(
        {
            'Refrigeration:Condenser:Cascade',
            'Refrigeration:SecondarySystem',
            'Refrigeration:TransferLoadList',
        }
    ),
    'RefrigerationSubcoolerNames': frozenset(
        {
            'Refrigeration:Subcooler',
        }
    ),
    'RefrigerationSystemNames': frozenset(
        {
            'Refrigeration:System',
            'Refrigeration:TranscriticalSystem',
        }
    ),
    'ReturnPathComponentNames': frozenset(
        {
            'AirLoopHVAC:ReturnPlenum',
            'AirLoopHVAC:ZoneMixer',
        }
    ),
    'RoomAirNodeGains': frozenset(
        {
            'RoomAir:Node:AirflowNetwork:InternalGains',
        }
    ),
    'RoomAirNodeHVACEquipment': frozenset(
        {
            'RoomAir:Node:AirflowNetwork:HVACEquipment',
        }
    ),
    'RoomAirNodeSurfaceLists': frozenset(
        {
            'RoomAir:Node:AirflowNetwork:AdjacentSurfaceList',
        }
    ),
    'RoomAirNodes': frozenset(
        {
            'RoomAir:Node',
        }
    ),
    'RoomAirflowNetworkNodes': frozenset(
        {
            'RoomAir:Node:AirflowNetwork',
        }
    ),
    'RunPeriodsAndDesignDays': frozenset(
        {
            'RunPeriod',
            'SizingPeriod:DesignDay',
            'SizingPeriod:WeatherFileConditionType',
            'SizingPeriod:WeatherFileDays',
        }
    ),
    'ScheduleNames': frozenset(
        {
            'ExternalInterface:FunctionalMockupUnitExport:To:Schedule',
            'ExternalInterface:FunctionalMockupUnitImport:To:Schedule',
            'ExternalInterface:Schedule',
            'Schedule:Compact',
            'Schedule:Constant',
            'Schedule:File',
            'Schedule:Year',
        }
    ),
    'ScheduleTypeLimitsNames': frozenset(
        {
            'ScheduleTypeLimits',
        }
    ),
    'SimpleCoils': frozenset(
        {
            'Coil:Cooling:Water',
            'Coil:Heating:Water',
        }
    ),
    'SpaceAndSpaceListNames': frozenset(
        {
            'Space',
            'SpaceList',
        }
    ),
    'SpaceListNames': frozenset(
        {
            'SpaceList',
        }
    ),
    'SpaceMixerNames': frozenset(
        {
            'SpaceHVAC:ZoneEquipmentMixer',
            'SpaceHVAC:ZoneReturnMixer',
        }
    ),
    'SpaceNames': frozenset(
        {
            'Space',
        }
    ),
    'SpaceSplitterNames': frozenset(
        {
            'SpaceHVAC:ZoneEquipmentSplitter',
        }
    ),
    'SpectralDataSets': frozenset(
        {
            'MaterialProperty:GlazingSpectralData',
        }
    ),
    'SpectrumDataNames': frozenset(
        {
            'Site:SpectrumData',
        }
    ),
    'SubSurfNames': frozenset(
        {
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'Window',
            'Window:Interzone',
        }
    ),
    'SupplyPathComponentNames': frozenset(
        {
            'AirLoopHVAC:SupplyPlenum',
            'AirLoopHVAC:ZoneSplitter',
        }
    ),
    'SurfAndSubSurfNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'Door',
            'Door:Interzone',
            'FenestrationSurface:Detailed',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'GlazedDoor',
            'GlazedDoor:Interzone',
            'Roof',
            'RoofCeiling:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
            'Window',
            'Window:Interzone',
        }
    ),
    'SurfaceAirflowLeakageNames': frozenset(
        {
            'AirflowNetwork:MultiZone:Component:DetailedOpening',
            'AirflowNetwork:MultiZone:Component:HorizontalOpening',
            'AirflowNetwork:MultiZone:Component:SimpleOpening',
            'AirflowNetwork:MultiZone:Component:ZoneExhaustFan',
            'AirflowNetwork:MultiZone:SpecifiedFlowRate',
            'AirflowNetwork:MultiZone:Surface:Crack',
            'AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea',
        }
    ),
    'SurfaceLocalEnvironmentNames': frozenset(
        {
            'SurfaceProperty:LocalEnvironment',
        }
    ),
    'SurfaceNames': frozenset(
        {
            'BuildingSurface:Detailed',
            'Ceiling:Adiabatic',
            'Ceiling:Interzone',
            'Floor:Adiabatic',
            'Floor:Detailed',
            'Floor:GroundContact',
            'Floor:Interzone',
            'Roof',
            'RoofCeiling:Detailed',
            'Wall:Adiabatic',
            'Wall:Detailed',
            'Wall:Exterior',
            'Wall:Interzone',
            'Wall:Underground',
        }
    ),
    'SurfacePropUnderWaterNames': frozenset(
        {
            'SurfaceProperty:Underwater',
        }
    ),
    'SurroundingSurfacesNames': frozenset(
        {
            'SurfaceProperty:SurroundingSurfaces',
        }
    ),
    'SystemAvailabilityManagerLists': frozenset(
        {
            'AvailabilityManagerAssignmentList',
        }
    ),
    'SystemAvailabilityManagers': frozenset(
        {
            'AvailabilityManager:DifferentialThermostat',
            'AvailabilityManager:HighTemperatureTurnOff',
            'AvailabilityManager:HighTemperatureTurnOn',
            'AvailabilityManager:HybridVentilation',
            'AvailabilityManager:LowTemperatureTurnOff',
            'AvailabilityManager:LowTemperatureTurnOn',
            'AvailabilityManager:NightCycle',
            'AvailabilityManager:NightVentilation',
            'AvailabilityManager:OptimumStart',
            'AvailabilityManager:Scheduled',
            'AvailabilityManager:ScheduledOff',
            'AvailabilityManager:ScheduledOn',
        }
    ),
    'ThermalComfortControlTypeNames': frozenset(
        {
            'ThermostatSetpoint:ThermalComfort:Fanger:DualSetpoint',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleCooling',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeating',
            'ThermostatSetpoint:ThermalComfort:Fanger:SingleHeatingOrCooling',
        }
    ),
    'ThermostatOffsetFaults': frozenset(
        {
            'FaultModel:ThermostatOffset',
        }
    ),
    'TransformerNames': frozenset(
        {
            'ElectricLoadCenter:Transformer',
        }
    ),
    'TrivariateFunctions': frozenset(
        {
            'Curve:ChillerPartLoadWithLift',
            'Curve:Triquadratic',
            'Table:Lookup',
        }
    ),
    'UTSCNames': frozenset(
        {
            'SolarCollector:UnglazedTranspired',
        }
    ),
    'UndisturbedGroundTempModels': frozenset(
        {
            'Site:GroundTemperature:Undisturbed:FiniteDifference',
            'Site:GroundTemperature:Undisturbed:KusudaAchenbach',
            'Site:GroundTemperature:Undisturbed:Xing',
        }
    ),
    'UnitarySystemPerformanceNames': frozenset(
        {
            'UnitarySystemPerformance:Multispeed',
        }
    ),
    'UnivariateFunctions': frozenset(
        {
            'Curve:Cubic',
            'Curve:DoubleExponentialDecay',
            'Curve:Exponent',
            'Curve:ExponentialDecay',
            'Curve:ExponentialSkewNormal',
            'Curve:Functional:PressureDrop',
            'Curve:Linear',
            'Curve:Quadratic',
            'Curve:Quartic',
            'Curve:RectangularHyperbola1',
            'Curve:RectangularHyperbola2',
            'Curve:Sigmoid',
            'Table:Lookup',
        }
    ),
    'UserConvectionInsideModels': frozenset(
        {
            'SurfaceConvectionAlgorithm:Inside:UserCurve',
        }
    ),
    'UserConvectionModels': frozenset(
        {
            'SurfaceConvectionAlgorithm:Inside:UserCurve',
            'SurfaceConvectionAlgorithm:Outside:UserCurve',
        }
    ),
    'UserConvectionOutsideModels': frozenset(
        {
            'SurfaceConvectionAlgorithm:Outside:UserCurve',
        }
    ),
    'UserDefinedCoil': frozenset(
        {
            'Coil:UserDefined',
        }
    ),
    'UtilityCostTariffs': frozenset(
        {
            'UtilityCost:Tariff',
        }
    ),
    'VariableSpeedTowerCoefficient': frozenset(
        {
            'CoolingTowerPerformance:CoolTools',
            'CoolingTowerPerformance:YorkCalc',
        }
    ),
    'VentSlabGroupNames': frozenset(
        {
            'ZoneHVAC:VentilatedSlab:SlabGroup',
        }
    ),
    'VentilationNames': frozenset(
        {
            'ZoneVentilation:DesignFlowRate',
            'ZoneVentilation:WindandStackOpenArea',
        }
    ),
    'WPCSetNames': frozenset(
        {
            'AirflowNetwork:MultiZone:WindPressureCoefficientArray',
        }
    ),
    'WPCValueNames': frozenset(
        {
            'AirflowNetwork:MultiZone:WindPressureCoefficientValues',
        }
    ),
    'WWHPCoolingNames': frozenset(
        {
            'HeatPump:WaterToWater:EquationFit:Cooling',
        }
    ),
    'WWHPHeatingNames': frozenset(
        {
            'HeatPump:WaterToWater:EquationFit:Heating',
        }
    ),
    'WaterCoilControllers': frozenset(
        {
            'Controller:WaterCoil',
        }
    ),
    'WaterHeaterMixedNames': frozenset(
        {
            'WaterHeater:Mixed',
        }
    ),
    'WaterHeaterNames': frozenset(
        {
            'WaterHeater:Mixed',
            'WaterHeater:Stratified',
        }
    ),
    'WaterHeaterStratifiedNames': frozenset(
        {
            'WaterHeater:Stratified',
        }
    ),
    'WaterStorageTankNames': frozenset(
        {
            'WaterUse:Storage',
        }
    ),
    'WaterUseEquipmentNames': frozenset(
        {
            'WaterUse:Equipment',
        }
    ),
    'WeekScheduleNames': frozenset(
        {
            'Schedule:Week:Compact',
            'Schedule:Week:Daily',
        }
    ),
    'WindowComplexShades': frozenset(
        {
            'WindowMaterial:ComplexShade',
        }
    ),
    'WindowEquivalentLayerMaterialNames': frozenset(
        {
            'WindowMaterial:Blind:EquivalentLayer',
            'WindowMaterial:Drape:EquivalentLayer',
            'WindowMaterial:Gap:EquivalentLayer',
            'WindowMaterial:Glazing:EquivalentLayer',
            'WindowMaterial:Screen:EquivalentLayer',
            'WindowMaterial:Shade:EquivalentLayer',
        }
    ),
    'WindowFrameAndDividerNames': frozenset(
        {
            'WindowProperty:FrameAndDivider',
        }
    ),
    'WindowGapDeflectionStates': frozenset(
        {
            'WindowGap:DeflectionState',
        }
    ),
    'WindowGapSupportPillars': frozenset(
        {
            'WindowGap:SupportPillar',
        }
    ),
    'WindowGasAndGasMixtures': frozenset(
        {
            'WindowMaterial:Gas',
            'WindowMaterial:GasMixture',
        }
    ),
    'WindowShadeControlNames': frozenset(
        {
            'WindowShadingControl',
        }
    ),
    'WindowShadesScreensAndBlinds': frozenset(
        {
            'WindowMaterial:Blind',
            'WindowMaterial:Screen',
            'WindowMaterial:Shade',
        }
    ),
    'WindowThermalModelParameters': frozenset(
        {
            'WindowThermalModel:Params',
        }
    ),
    'ZoneAndZoneListAndSpaceAndSpaceListNames': frozenset(
        {
            'Space',
            'SpaceList',
            'Zone',
            'ZoneList',
        }
    ),
    'ZoneAndZoneListNames': frozenset(
        {
            'Zone',
            'ZoneList',
        }
    ),
    'ZoneControlHumidistatNames': frozenset(
        {
            'ZoneControl:Humidistat',
        }
    ),
    'ZoneControlThermostaticNames': frozenset(
        {
            'ZoneControl:Thermostat',
            'ZoneControl:Thermostat:StagedDualSetpoint',
        }
    ),
    'ZoneEquipmentLists': frozenset(
        {
            'ZoneHVAC:EquipmentList',
        }
    ),
    'ZoneEquipmentNames': frozenset(
        {
            'AirLoopHVAC:UnitarySystem',
            'Fan:ZoneExhaust',
            'HeatExchanger:AirToAir:FlatPlate',
            'WaterHeater:HeatPump:PumpedCondenser',
            'WaterHeater:HeatPump:WrappedCondenser',
            'ZoneHVAC:AirDistributionUnit',
            'ZoneHVAC:Baseboard:Convective:Electric',
            'ZoneHVAC:Baseboard:Convective:Water',
            'ZoneHVAC:Baseboard:RadiantConvective:Electric',
            'ZoneHVAC:Baseboard:RadiantConvective:Steam',
            'ZoneHVAC:Baseboard:RadiantConvective:Steam:Design',
            'ZoneHVAC:Baseboard:RadiantConvective:Water',
            'ZoneHVAC:CoolingPanel:RadiantConvective:Water',
            'ZoneHVAC:Dehumidifier:DX',
            'ZoneHVAC:EnergyRecoveryVentilator',
            'ZoneHVAC:EvaporativeCoolerUnit',
            'ZoneHVAC:ForcedAir:UserDefined',
            'ZoneHVAC:FourPipeFanCoil',
            'ZoneHVAC:HighTemperatureRadiant',
            'ZoneHVAC:HybridUnitaryHVAC',
            'ZoneHVAC:IdealLoadsAirSystem',
            'ZoneHVAC:LowTemperatureRadiant:ConstantFlow',
            'ZoneHVAC:LowTemperatureRadiant:Electric',
            'ZoneHVAC:LowTemperatureRadiant:VariableFlow',
            'ZoneHVAC:OutdoorAirUnit',
            'ZoneHVAC:PackagedTerminalAirConditioner',
            'ZoneHVAC:PackagedTerminalHeatPump',
            'ZoneHVAC:RefrigerationChillerSet',
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
            'ZoneHVAC:UnitHeater',
            'ZoneHVAC:UnitVentilator',
            'ZoneHVAC:VentilatedSlab',
            'ZoneHVAC:WaterToAirHeatPump',
            'ZoneHVAC:WindowAirConditioner',
        }
    ),
    'ZoneListNames': frozenset(
        {
            'ZoneList',
        }
    ),
    'ZoneLocalEnvironmentNames': frozenset(
        {
            'ZoneProperty:LocalEnvironment',
        }
    ),
    'ZoneMixers': frozenset(
        {
            'AirLoopHVAC:ZoneMixer',
        }
    ),
    'ZoneNames': frozenset(
        {
            'Zone',
        }
    ),
    'ZoneTerminalUnitListNames': frozenset(
        {
            'ZoneTerminalUnitList',
        }
    ),
    'ZoneTerminalUnitNames': frozenset(
        {
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
        }
    ),
    'validBranchEquipmentNames': frozenset(
        {
            'AirConditioner:VariableRefrigerantFlow',
            'AirLoopHVAC:OutdoorAirSystem',
            'AirLoopHVAC:Unitary:Furnace:HeatCool',
            'AirLoopHVAC:Unitary:Furnace:HeatOnly',
            'AirLoopHVAC:UnitaryHeatCool',
            'AirLoopHVAC:UnitaryHeatCool:VAVChangeoverBypass',
            'AirLoopHVAC:UnitaryHeatOnly',
            'AirLoopHVAC:UnitaryHeatPump:AirToAir',
            'AirLoopHVAC:UnitaryHeatPump:AirToAir:MultiSpeed',
            'AirLoopHVAC:UnitaryHeatPump:WaterToAir',
            'AirLoopHVAC:UnitarySystem',
            'AirTerminal:SingleDuct:ConstantVolume:CooledBeam',
            'AirTerminal:SingleDuct:ConstantVolume:FourPipeBeam',
            'AirTerminal:SingleDuct:UserDefined',
            'Boiler:HotWater',
            'Boiler:Steam',
            'CentralHeatPumpSystem',
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ChillerHeater:Absorption:DirectFired',
            'ChillerHeater:Absorption:DoubleEffect',
            'Coil:Cooling:DX:SingleSpeed:ThermalStorage',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Cooling:WaterToAirHeatPump:EquationFit',
            'Coil:Cooling:WaterToAirHeatPump:ParameterEstimation',
            'Coil:Cooling:WaterToAirHeatPump:VariableSpeedEquationFit',
            'Coil:Heating:Desuperheater',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'Coil:Heating:WaterToAirHeatPump:EquationFit',
            'Coil:Heating:WaterToAirHeatPump:ParameterEstimation',
            'Coil:Heating:WaterToAirHeatPump:VariableSpeedEquationFit',
            'Coil:UserDefined',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water',
            'CoilSystem:Cooling:Water:HeatExchangerAssisted',
            'CoilSystem:Heating:DX',
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed',
            'CoolingTower:VariableSpeed:Merkel',
            'Dehumidifier:Desiccant:NoFans',
            'Dehumidifier:Desiccant:System',
            'DistrictCooling',
            'DistrictHeating:Steam',
            'DistrictHeating:Water',
            'Duct',
            'EvaporativeCooler:Direct:CelDekPad',
            'EvaporativeCooler:Direct:ResearchSpecial',
            'EvaporativeCooler:Indirect:CelDekPad',
            'EvaporativeCooler:Indirect:ResearchSpecial',
            'EvaporativeCooler:Indirect:WetCoil',
            'EvaporativeFluidCooler:SingleSpeed',
            'EvaporativeFluidCooler:TwoSpeed',
            'Fan:ComponentModel',
            'Fan:ConstantVolume',
            'Fan:SystemModel',
            'Fan:VariableVolume',
            'FluidCooler:SingleSpeed',
            'FluidCooler:TwoSpeed',
            'Generator:CombustionTurbine',
            'Generator:FuelCell:ExhaustGasToWaterHeatExchanger',
            'Generator:FuelCell:StackCooler',
            'Generator:InternalCombustionEngine',
            'Generator:MicroCHP',
            'Generator:MicroTurbine',
            'GroundHeatExchanger:HorizontalTrench',
            'GroundHeatExchanger:Pond',
            'GroundHeatExchanger:Slinky',
            'GroundHeatExchanger:Surface',
            'GroundHeatExchanger:System',
            'HeaderedPumps:ConstantSpeed',
            'HeaderedPumps:VariableSpeed',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
            'HeatExchanger:Desiccant:BalancedFlow',
            'HeatExchanger:FluidToFluid',
            'HeatPump:PlantLoop:EIR:Cooling',
            'HeatPump:PlantLoop:EIR:Heating',
            'HeatPump:WaterToWater:EquationFit:Cooling',
            'HeatPump:WaterToWater:EquationFit:Heating',
            'HeatPump:WaterToWater:ParameterEstimation:Cooling',
            'HeatPump:WaterToWater:ParameterEstimation:Heating',
            'Humidifier:Steam:Electric',
            'Humidifier:Steam:Gas',
            'LoadProfile:Plant',
            'Pipe:Adiabatic',
            'Pipe:Adiabatic:Steam',
            'Pipe:Indoor',
            'Pipe:Outdoor',
            'Pipe:Underground',
            'PipingSystem:Underground:PipeCircuit',
            'PlantComponent:TemperatureSource',
            'PlantComponent:UserDefined',
            'Pump:ConstantSpeed',
            'Pump:VariableSpeed',
            'Pump:VariableSpeed:Condensate',
            'Refrigeration:CompressorRack',
            'Refrigeration:Condenser:WaterCooled',
            'SolarCollector:FlatPlate:PhotovoltaicThermal',
            'SolarCollector:FlatPlate:Water',
            'SolarCollector:IntegralCollectorStorage',
            'SwimmingPool:Indoor',
            'TemperingValve',
            'ThermalStorage:ChilledWater:Mixed',
            'ThermalStorage:ChilledWater:Stratified',
            'ThermalStorage:Ice:Detailed',
            'ThermalStorage:Ice:Simple',
            'WaterHeater:HeatPump:PumpedCondenser',
            'WaterHeater:HeatPump:WrappedCondenser',
            'WaterHeater:Mixed',
            'WaterHeater:Stratified',
            'WaterUse:Connections',
            'ZoneHVAC:Baseboard:Convective:Water',
            'ZoneHVAC:Baseboard:RadiantConvective:Steam',
            'ZoneHVAC:Baseboard:RadiantConvective:Steam:Design',
            'ZoneHVAC:Baseboard:RadiantConvective:Water',
            'ZoneHVAC:CoolingPanel:RadiantConvective:Water',
            'ZoneHVAC:ForcedAir:UserDefined',
            'ZoneHVAC:LowTemperatureRadiant:ConstantFlow',
            'ZoneHVAC:LowTemperatureRadiant:VariableFlow',
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
        }
    ),
    'validCondenserEquipmentNames': frozenset(
        {
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed',
            'CoolingTower:VariableSpeed:Merkel',
            'DistrictCooling',
            'DistrictHeating:Steam',
            'DistrictHeating:Water',
            'EvaporativeFluidCooler:SingleSpeed',
            'EvaporativeFluidCooler:TwoSpeed',
            'FluidCooler:SingleSpeed',
            'FluidCooler:TwoSpeed',
            'Generator:MicroTurbine',
            'GroundHeatExchanger:HorizontalTrench',
            'GroundHeatExchanger:Pond',
            'GroundHeatExchanger:Slinky',
            'GroundHeatExchanger:Surface',
            'GroundHeatExchanger:System',
            'HeatExchanger:FluidToFluid',
            'PipingSystem:Underground:PipeCircuit',
            'PlantComponent:TemperatureSource',
            'PlantComponent:UserDefined',
            'TemperingValve',
            'ThermalStorage:ChilledWater:Mixed',
            'ThermalStorage:ChilledWater:Stratified',
            'WaterHeater:Mixed',
            'WaterHeater:Stratified',
        }
    ),
    'validOASysEquipmentNames': frozenset(
        {
            'AirLoopHVAC:UnitarySystem',
            'Coil:Cooling:Water',
            'Coil:Cooling:Water:DetailedGeometry',
            'Coil:Heating:Electric',
            'Coil:Heating:Fuel',
            'Coil:Heating:Steam',
            'Coil:Heating:Water',
            'Coil:UserDefined',
            'CoilSystem:Cooling:DX',
            'CoilSystem:Cooling:Water',
            'CoilSystem:Cooling:Water:HeatExchangerAssisted',
            'CoilSystem:Heating:DX',
            'Dehumidifier:Desiccant:NoFans',
            'Dehumidifier:Desiccant:System',
            'EvaporativeCooler:Direct:CelDekPad',
            'EvaporativeCooler:Direct:ResearchSpecial',
            'EvaporativeCooler:Indirect:CelDekPad',
            'EvaporativeCooler:Indirect:ResearchSpecial',
            'EvaporativeCooler:Indirect:WetCoil',
            'Fan:ComponentModel',
            'Fan:ConstantVolume',
            'Fan:SystemModel',
            'Fan:VariableVolume',
            'HeatExchanger:AirToAir:FlatPlate',
            'HeatExchanger:AirToAir:SensibleAndLatent',
            'HeatExchanger:Desiccant:BalancedFlow',
            'Humidifier:Steam:Electric',
            'Humidifier:Steam:Gas',
            'OutdoorAir:Mixer',
            'SolarCollector:FlatPlate:PhotovoltaicThermal',
            'SolarCollector:UnglazedTranspired',
            'ZoneHVAC:TerminalUnit:VariableRefrigerantFlow',
        }
    ),
    'validPlantEquipmentNames': frozenset(
        {
            'Boiler:HotWater',
            'Boiler:Steam',
            'CentralHeatPumpSystem',
            'Chiller:Absorption',
            'Chiller:Absorption:Indirect',
            'Chiller:CombustionTurbine',
            'Chiller:ConstantCOP',
            'Chiller:Electric',
            'Chiller:Electric:ASHRAE205',
            'Chiller:Electric:EIR',
            'Chiller:Electric:ReformulatedEIR',
            'Chiller:EngineDriven',
            'ChillerHeater:Absorption:DirectFired',
            'ChillerHeater:Absorption:DoubleEffect',
            'CoolingTower:SingleSpeed',
            'CoolingTower:TwoSpeed',
            'CoolingTower:VariableSpeed',
            'CoolingTower:VariableSpeed:Merkel',
            'DistrictCooling',
            'DistrictHeating:Steam',
            'DistrictHeating:Water',
            'EvaporativeFluidCooler:SingleSpeed',
            'EvaporativeFluidCooler:TwoSpeed',
            'FluidCooler:SingleSpeed',
            'FluidCooler:TwoSpeed',
            'Generator:FuelCell:ExhaustGasToWaterHeatExchanger',
            'Generator:MicroCHP',
            'Generator:MicroTurbine',
            'GroundHeatExchanger:HorizontalTrench',
            'GroundHeatExchanger:Pond',
            'GroundHeatExchanger:Slinky',
            'GroundHeatExchanger:Surface',
            'GroundHeatExchanger:System',
            'HeatExchanger:FluidToFluid',
            'HeatPump:PlantLoop:EIR:Cooling',
            'HeatPump:PlantLoop:EIR:Heating',
            'HeatPump:WaterToWater:EquationFit:Cooling',
            'HeatPump:WaterToWater:EquationFit:Heating',
            'HeatPump:WaterToWater:ParameterEstimation:Cooling',
            'HeatPump:WaterToWater:ParameterEstimation:Heating',
            'PipingSystem:Underground:PipeCircuit',
            'PlantComponent:TemperatureSource',
            'PlantComponent:UserDefined',
            'SolarCollector:FlatPlate:PhotovoltaicThermal',
            'SolarCollector:FlatPlate:Water',
            'SolarCollector:IntegralCollectorStorage',
            'TemperingValve',
            'ThermalStorage:ChilledWater:Mixed',
            'ThermalStorage:ChilledWater:Stratified',
            'ThermalStorage:Ice:Detailed',
            'WaterHeater:HeatPump:PumpedCondenser',
            'WaterHeater:HeatPump:WrappedCondenser',
            'WaterHeater:Mixed',
            'WaterHeater:Stratified',
        }
    ),
}


REF_CONSUMERS: dict[str, dict[str, list[str]]] = {
    'AirConditionerVariableRefrigerantFlow': {
        'availability_schedule_name': ['ScheduleNames'],
        'cooling_capacity_ratio_modifier_function_of_low_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_capacity_ratio_boundary_curve_name': ['UnivariateFunctions'],
        'cooling_capacity_ratio_modifier_function_of_high_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_energy_input_ratio_modifier_function_of_low_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_energy_input_ratio_boundary_curve_name': ['UnivariateFunctions'],
        'cooling_energy_input_ratio_modifier_function_of_high_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_combination_ratio_correction_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'heating_capacity_ratio_modifier_function_of_low_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_capacity_ratio_boundary_curve_name': ['UnivariateFunctions'],
        'heating_capacity_ratio_modifier_function_of_high_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_energy_input_ratio_modifier_function_of_low_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_energy_input_ratio_boundary_curve_name': ['UnivariateFunctions'],
        'heating_energy_input_ratio_modifier_function_of_high_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_energy_input_ratio_modifier_function_of_low_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_energy_input_ratio_modifier_function_of_high_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_combination_ratio_correction_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'zone_name_for_master_thermostat_location': ['ZoneNames'],
        'thermostat_priority_schedule_name': ['ScheduleNames'],
        'zone_terminal_unit_list_name': ['ZoneTerminalUnitListNames'],
        'piping_correction_factor_for_length_in_cooling_mode_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'piping_correction_factor_for_length_in_heating_mode_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'defrost_energy_input_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'heat_recovery_cooling_capacity_modifier_curve_name': ['BivariateFunctions'],
        'heat_recovery_cooling_energy_modifier_curve_name': ['BivariateFunctions'],
        'heat_recovery_heating_capacity_modifier_curve_name': ['BivariateFunctions'],
        'heat_recovery_heating_energy_modifier_curve_name': ['BivariateFunctions'],
    },
    'AirConditionerVariableRefrigerantFlowFluidTemperatureControl': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_terminal_unit_list_name': ['ZoneTerminalUnitListNames'],
        'refrigerant_type': ['FluidNames'],
        'outdoor_unit_evaporating_temperature_function_of_superheating_curve_name': [
            'UnivariateFunctions'
        ],
        'outdoor_unit_condensing_temperature_function_of_subcooling_curve_name': [
            'UnivariateFunctions'
        ],
        'defrost_energy_input_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
    },
    'AirConditionerVariableRefrigerantFlowFluidTemperatureControlHR': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_terminal_unit_list_name': ['ZoneTerminalUnitListNames'],
        'refrigerant_type': ['FluidNames'],
        'outdoor_unit_evaporating_temperature_function_of_superheating_curve_name': [
            'UnivariateFunctions'
        ],
        'outdoor_unit_condensing_temperature_function_of_subcooling_curve_name': [
            'UnivariateFunctions'
        ],
        'defrost_energy_input_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
    },
    'AirConditionerVariableRefrigerantFlowFluidTemperatureControlLoadingIndicesItem': {
        'loading_index_evaporative_capacity_multiplier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'loading_index_compressor_power_multiplier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
    },
    'AirLoopHVAC': {
        'controller_list_name': ['ControllerLists'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'branch_list_name': ['BranchLists'],
        'connector_list_name': ['ConnectorLists'],
    },
    'AirLoopHVACControllerList': {
        'controller_1_name': ['AirLoopControllers'],
        'controller_2_name': ['AirLoopControllers'],
        'controller_3_name': ['AirLoopControllers'],
        'controller_4_name': ['AirLoopControllers'],
        'controller_5_name': ['AirLoopControllers'],
        'controller_6_name': ['AirLoopControllers'],
        'controller_7_name': ['AirLoopControllers'],
        'controller_8_name': ['AirLoopControllers'],
    },
    'AirLoopHVACDedicatedOutdoorAirSystem': {
        'airloophvac_outdoorairsystem_name': ['validBranchEquipmentNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'airloophvac_mixer_name': ['AirLoopHVACMixerNames'],
        'airloophvac_splitter_name': ['AirLoopHVACSplitterNames'],
    },
    'AirLoopHVACDedicatedOutdoorAirSystemAirloophvacsItem': {
        'airloophvac_name': ['AirPrimaryLoops'],
    },
    'AirLoopHVACExhaustSystem': {
        'zone_mixer_name': ['ZoneMixers'],
        'fan_name': ['FansComponentModel', 'FansSystemModel'],
    },
    'AirLoopHVACOutdoorAirSystem': {
        'controller_list_name': ['ControllerLists'],
        'outdoor_air_equipment_list_name': ['AirLoopOAEquipmentLists'],
    },
    'AirLoopHVACOutdoorAirSystemEquipmentList': {
        'component_1_object_type': ['validOASysEquipmentTypes'],
        'component_1_name': ['validOASysEquipmentNames'],
        'component_2_object_type': ['validOASysEquipmentTypes'],
        'component_2_name': ['validOASysEquipmentNames'],
        'component_3_object_type': ['validOASysEquipmentTypes'],
        'component_3_name': ['validOASysEquipmentNames'],
        'component_4_object_type': ['validOASysEquipmentTypes'],
        'component_4_name': ['validOASysEquipmentNames'],
        'component_5_object_type': ['validOASysEquipmentTypes'],
        'component_5_name': ['validOASysEquipmentNames'],
        'component_6_object_type': ['validOASysEquipmentTypes'],
        'component_6_name': ['validOASysEquipmentNames'],
        'component_7_object_type': ['validOASysEquipmentTypes'],
        'component_7_name': ['validOASysEquipmentNames'],
        'component_8_object_type': ['validOASysEquipmentTypes'],
        'component_8_name': ['validOASysEquipmentNames'],
        'component_9_object_type': ['validOASysEquipmentTypes'],
        'component_9_name': ['validOASysEquipmentNames'],
    },
    'AirLoopHVACReturnPathComponentsItem': {
        'component_name': ['ReturnPathComponentNames'],
    },
    'AirLoopHVACReturnPlenum': {
        'zone_name': ['ZoneNames'],
    },
    'AirLoopHVACSupplyPathComponentsItem': {
        'component_name': ['SupplyPathComponentNames'],
    },
    'AirLoopHVACSupplyPlenum': {
        'zone_name': ['ZoneNames'],
    },
    'AirLoopHVACUnitaryFurnaceHeatCool': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_fan_name': ['FansCVandOnOff'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': [
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'reheat_coil_name': ['HeatingCoilName'],
    },
    'AirLoopHVACUnitaryFurnaceHeatOnly': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_fan_name': ['FansCVandOnOff'],
        'heating_coil_name': ['HeatingCoilName'],
    },
    'AirLoopHVACUnitaryHeatCool': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_fan_name': ['FansCVandOnOff'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': [
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'reheat_coil_name': ['HeatingCoilName'],
    },
    'AirLoopHVACUnitaryHeatCoolVAVChangeoverBypass': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_flow_rate_multiplier_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansCVandOnOff', 'FansSystemModel'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_name': [
            'CoolingCoilsDXMultiModeOrSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'heating_coil_name': ['HeatingCoilName', 'HeatingCoilsDXVariableSpeed'],
    },
    'AirLoopHVACUnitaryHeatOnly': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_fan_name': ['FansCVandOnOff'],
        'heating_coil_name': ['HeatingCoilName'],
    },
    'AirLoopHVACUnitaryHeatPumpAirToAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_air_fan_name': ['FansCVandOnOff'],
        'heating_coil_name': [
            'HeatingCoilsDXSingleSpeed',
            'HeatingCoilsDXVariableSpeed',
            'IntegratedHeatPumps',
        ],
        'cooling_coil_name': [
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
            'IntegratedHeatPumps',
        ],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
    },
    'AirLoopHVACUnitaryHeatPumpAirToAirMultiSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_air_fan_name': ['FansCVandOnOff'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'heating_coil_name': [
            'HeatingCoilsDXMultiSpeed',
            'HeatingCoilsElectricMultiStage',
            'HeatingCoilsGasMultiStage',
        ],
        'cooling_coil_name': ['CoolingCoilsDXMultiSpeed'],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
    },
    'AirLoopHVACUnitaryHeatPumpWaterToAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'supply_air_fan_name': ['FansOnOff'],
        'heating_coil_name': ['HeatingCoilsWaterToAirHP', 'HeatingCoilsWaterToAirVSHP'],
        'cooling_coil_name': ['CoolingCoilsWaterToAirHP', 'CoolingCoilsWaterToAirVSHP'],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
    },
    'AirLoopHVACUnitarySystem': {
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'supply_fan_name': ['Fans'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'heating_coil_name': [
            'HeatingCoilName',
            'HeatingCoilsDX',
            'HeatingCoilsDXMultiSpeed',
            'HeatingCoilsDXVariableSpeed',
            'HeatingCoilsDesuperheater',
            'HeatingCoilsElectricMultiStage',
            'HeatingCoilsGasMultiStage',
            'HeatingCoilsWaterToAirHP',
            'HeatingCoilsWaterToAirVSHP',
            'UserDefinedCoil',
        ],
        'cooling_coil_name': [
            'CoilCoolingDX',
            'CoolingCoilsDX',
            'CoolingCoilsDXMultiSpeed',
            'CoolingCoilsDXVariableSpeed',
            'CoolingCoilsWater',
            'CoolingCoilsWaterToAirHP',
            'CoolingCoilsWaterToAirVSHP',
            'UserDefinedCoil',
        ],
        'supplemental_heating_coil_name': [
            'HeatingCoilName',
            'HeatingCoilsDesuperheater',
            'HeatingCoilsElectricMultiStage',
            'UserDefinedCoil',
        ],
        'design_specification_multispeed_object_name': [
            'UnitarySystemPerformanceNames'
        ],
    },
    'AirTerminalDualDuctConstantVolume': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalDualDuctVAV': {
        'availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalDualDuctVAVOutdoorAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
    },
    'AirTerminalSingleDuctConstantVolumeCooledBeam': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalSingleDuctConstantVolumeFourPipeBeam': {
        'primary_air_availability_schedule_name': ['ScheduleNames'],
        'cooling_availability_schedule_name': ['ScheduleNames'],
        'heating_availability_schedule_name': ['ScheduleNames'],
        'beam_cooling_capacity_temperature_difference_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'beam_cooling_capacity_air_flow_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'beam_cooling_capacity_chilled_water_flow_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'beam_heating_capacity_temperature_difference_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'beam_heating_capacity_air_flow_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
        'beam_heating_capacity_hot_water_flow_modification_factor_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'AirTerminalSingleDuctConstantVolumeFourPipeInduction': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': ['CoolingCoilName'],
        'zone_mixer_name': ['ZoneMixers'],
    },
    'AirTerminalSingleDuctConstantVolumeNoReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
    },
    'AirTerminalSingleDuctConstantVolumeReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'reheat_coil_name': ['HeatingCoilName'],
    },
    'AirTerminalSingleDuctMixer': {
        'zonehvac_unit_object_name': ['DOAToZonalUnit'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
    },
    'AirTerminalSingleDuctParallelPIUReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_mixer_name': ['ZoneMixers'],
        'fan_name': ['FansCV', 'FansSystemModel'],
        'reheat_coil_name': ['HeatingCoilName'],
    },
    'AirTerminalSingleDuctSeriesPIUReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_mixer_name': ['ZoneMixers'],
        'fan_name': ['FansCV', 'FansSystemModel'],
        'reheat_coil_name': ['HeatingCoilName'],
    },
    'AirTerminalSingleDuctUserDefined': {
        'overall_model_simulation_program_calling_manager_name': ['ProgramNames'],
        'model_setup_and_sizing_program_calling_manager_name': ['ProgramNames'],
        'supply_inlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'collection_outlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'ambient_zone_name': ['ZoneNames'],
    },
    'AirTerminalSingleDuctVAVHeatAndCoolNoReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalSingleDuctVAVHeatAndCoolReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'reheat_coil_name': ['HeatingCoilName'],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalSingleDuctVAVNoReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'minimum_air_flow_fraction_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalSingleDuctVAVReheat': {
        'availability_schedule_name': ['ScheduleNames'],
        'minimum_air_flow_fraction_schedule_name': ['ScheduleNames'],
        'reheat_coil_name': ['HeatingCoilName'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirTerminalSingleDuctVAVReheatVariableSpeedFan': {
        'availability_schedule_name': ['ScheduleNames'],
        'fan_name': ['FansSystemModel', 'FansVAV'],
        'heating_coil_name': ['HeatingCoilName'],
        'minimum_air_flow_turndown_schedule_name': ['ScheduleNames'],
    },
    'AirflowNetworkDistributionComponentCoil': {
        'coil_name': ['AFNCoilNames'],
    },
    'AirflowNetworkDistributionComponentFan': {
        'fan_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
    },
    'AirflowNetworkDistributionComponentHeatExchanger': {
        'heatexchanger_name': ['AFNHeatExchangerNames'],
    },
    'AirflowNetworkDistributionComponentOutdoorAirFlow': {
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'reference_crack_conditions': ['ReferenceCrackConditions'],
    },
    'AirflowNetworkDistributionComponentReliefAirFlow': {
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'reference_crack_conditions': ['ReferenceCrackConditions'],
    },
    'AirflowNetworkDistributionComponentTerminalUnit': {
        'terminal_unit_name': ['AFNTerminalUnitNames'],
    },
    'AirflowNetworkDistributionDuctViewFactors': {
        'linkage_name': ['AirflowNetworkComponentNames'],
    },
    'AirflowNetworkDistributionDuctViewFactorsSurfacesItem': {
        'surface_name': ['AllHeatTranSurfNames'],
    },
    'AirflowNetworkDistributionLinkage': {
        'node_1_name': ['AirflowNetworkNodeAndZoneNames'],
        'node_2_name': ['AirflowNetworkNodeAndZoneNames'],
        'component_name': [
            'AFNCoilNames',
            'AFNHeatExchangerNames',
            'AFNTerminalUnitNames',
            'AirflowNetworkComponentNames',
            'FansCVandOnOffandVAV',
        ],
        'thermal_zone_name': ['ZoneNames'],
    },
    'AirflowNetworkIntraZoneLinkage': {
        'node_1_name': ['AirflowNetworkNodeNames', 'ZoneNames'],
        'node_2_name': ['AirflowNetworkNodeNames', 'ZoneNames'],
        'component_name': ['AirflowNetworkComponentNames'],
        'airflownetwork_multizone_surface_name': ['SurfAndSubSurfNames'],
    },
    'AirflowNetworkIntraZoneNode': {
        'roomair_node_airflownetwork_name': ['RoomAirflowNetworkNodes'],
        'zone_name': ['AirFlowNetworkMultizoneZones'],
    },
    'AirflowNetworkMultiZoneComponentZoneExhaustFan': {
        'name': ['FansZoneExhaust'],
        'reference_crack_conditions': ['ReferenceCrackConditions'],
    },
    'AirflowNetworkMultiZoneExternalNode': {
        'wind_pressure_coefficient_curve_name': [
            'UnivariateFunctions',
            'WPCValueNames',
        ],
    },
    'AirflowNetworkMultiZoneSurface': {
        'surface_name': ['SurfAndSubSurfNames'],
        'leakage_component_name': ['SurfaceAirflowLeakageNames'],
        'external_node_name': ['ExternalNodeNames', 'OutdoorAirNodeNames'],
        'ventilation_control_zone_temperature_setpoint_schedule_name': [
            'ScheduleNames'
        ],
        'venting_availability_schedule_name': ['ScheduleNames'],
        'occupant_ventilation_control_name': [
            'AirflowNetworkOccupantVentilationControlNames'
        ],
    },
    'AirflowNetworkMultiZoneSurfaceCrack': {
        'reference_crack_conditions': ['ReferenceCrackConditions'],
    },
    'AirflowNetworkMultiZoneWindPressureCoefficientValues': {
        'airflownetwork_multizone_windpressurecoefficientarray_name': ['WPCSetNames'],
    },
    'AirflowNetworkMultiZoneZone': {
        'zone_name': ['ZoneNames'],
        'ventilation_control_zone_temperature_setpoint_schedule_name': [
            'ScheduleNames'
        ],
        'venting_availability_schedule_name': ['ScheduleNames'],
        'occupant_ventilation_control_name': [
            'AirflowNetworkOccupantVentilationControlNames'
        ],
    },
    'AirflowNetworkOccupantVentilationControl': {
        'thermal_comfort_low_temperature_curve_name': ['UnivariateFunctions'],
        'thermal_comfort_high_temperature_curve_name': ['UnivariateFunctions'],
        'opening_probability_schedule_name': ['ScheduleNames'],
        'closing_probability_schedule_name': ['ScheduleNames'],
    },
    'AirflowNetworkZoneControlPressureController': {
        'control_zone_name': ['ZoneNames'],
        'control_object_name': ['AFNReliefAirFlowNames', 'FansZoneExhaust'],
        'pressure_control_availability_schedule_name': ['ScheduleNames'],
        'pressure_setpoint_schedule_name': ['ScheduleNames'],
    },
    'AvailabilityManagerAssignmentListManagersItem': {
        'availability_manager_name': ['SystemAvailabilityManagers'],
    },
    'AvailabilityManagerHybridVentilation': {
        'hvac_air_loop_name': ['AirPrimaryLoops', 'HVACTemplateSystems'],
        'control_zone_name': ['ZoneNames'],
        'ventilation_control_mode_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_ventilation_air_schedule_name': ['ScheduleNames'],
        'opening_factor_function_of_wind_speed_curve_name': ['UnivariateFunctions'],
        'airflownetwork_control_type_schedule_name': ['ScheduleNames'],
        'simple_airflow_control_type_schedule_name': ['ScheduleNames'],
        'zoneventilation_object_name': ['VentilationNames'],
    },
    'AvailabilityManagerLowTemperatureTurnOff': {
        'applicability_schedule_name': ['ScheduleNames'],
    },
    'AvailabilityManagerNightCycle': {
        'applicability_schedule_name': ['ScheduleNames'],
        'fan_schedule_name': ['ScheduleNames'],
        'control_zone_or_zone_list_name': ['ZoneAndZoneListNames'],
        'cooling_control_zone_or_zone_list_name': ['ZoneAndZoneListNames'],
        'heating_control_zone_or_zone_list_name': ['ZoneAndZoneListNames'],
        'heating_zone_fans_only_zone_or_zone_list_name': ['ZoneAndZoneListNames'],
    },
    'AvailabilityManagerNightVentilation': {
        'applicability_schedule_name': ['ScheduleNames'],
        'fan_schedule_name': ['ScheduleNames'],
        'ventilation_temperature_schedule_name': ['ScheduleNames'],
        'control_zone_name': ['ZoneNames'],
    },
    'AvailabilityManagerOptimumStart': {
        'applicability_schedule_name': ['ScheduleNames'],
        'fan_schedule_name': ['ScheduleNames'],
        'control_zone_name': ['ZoneNames'],
        'zone_list_name': ['ZoneListNames'],
    },
    'AvailabilityManagerScheduled': {
        'schedule_name': ['ScheduleNames'],
    },
    'AvailabilityManagerScheduledOff': {
        'schedule_name': ['ScheduleNames'],
    },
    'AvailabilityManagerScheduledOn': {
        'schedule_name': ['ScheduleNames'],
    },
    'BoilerHotWater': {
        'normalized_boiler_efficiency_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
    },
    'Branch': {
        'pressure_drop_curve_name': ['UnivariateFunctions'],
    },
    'BranchComponentsItem': {
        'component_object_type': ['validBranchEquipmentTypes'],
        'component_name': ['validBranchEquipmentNames'],
    },
    'BranchListBranchesItem': {
        'branch_name': ['Branches'],
    },
    'BuildingSurfaceDetailed': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'CeilingAdiabatic': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'CeilingInterzone': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'CentralHeatPumpSystem': {
        'ancillary_operation_schedule_name': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_1': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_1': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_2': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_2': ['ScheduleNames'],
        'chiller_heater_performance_component_name_3': ['ChillerHeaterEIRNames'],
        'chiller_heater_modules_control_schedule_name_3': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_4': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_4': ['ScheduleNames'],
        'chiller_heater_models_performance_component_name_5': ['ChillerHeaterEIRNames'],
        'chiller_heater_modules_control_schedule_name_5': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_6': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_6': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_7': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_7': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_8': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_8': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_9': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_9': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_10': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_10': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_11': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_module_control_schedule_name_11': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_12': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_12': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_13': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_13': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_14': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_14': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_15': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_15': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_16': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_16': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_17': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_17': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_18': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_control_schedule_name_18': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_19': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_19': ['ScheduleNames'],
        'chiller_heater_modules_performance_component_name_20': [
            'ChillerHeaterEIRNames'
        ],
        'chiller_heater_modules_control_schedule_name_20': ['ScheduleNames'],
    },
    'ChillerAbsorptionIndirect': {
        'generator_heat_input_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'pump_electric_input_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'capacity_correction_function_of_condenser_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'capacity_correction_function_of_chilled_water_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'capacity_correction_function_of_generator_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'generator_heat_input_correction_function_of_condenser_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'generator_heat_input_correction_function_of_chilled_water_temperature_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'ChillerCombustionTurbine': {
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
    },
    'ChillerConstantCOP': {
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'thermosiphon_capacity_fraction_curve_name': ['UniVariateFunctions'],
    },
    'ChillerElectric': {
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'heat_recovery_inlet_high_temperature_limit_schedule_name': ['ScheduleNames'],
        'thermosiphon_capacity_fraction_curve_name': ['UniVariateFunctions'],
    },
    'ChillerElectricASHRAE205': {
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
    },
    'ChillerElectricEIR': {
        'cooling_capacity_function_of_temperature_curve_name': ['BivariateFunctions'],
        'electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'heat_recovery_inlet_high_temperature_limit_schedule_name': ['ScheduleNames'],
        'condenser_loop_flow_rate_fraction_function_of_loop_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'temperature_difference_across_condenser_schedule_name': ['ScheduleNames'],
        'thermosiphon_capacity_fraction_curve_name': ['UniVariateFunctions'],
    },
    'ChillerElectricReformulatedEIR': {
        'cooling_capacity_function_of_temperature_curve_name': ['BivariateFunctions'],
        'electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'BivariateFunctions',
            'TrivariateFunctions',
        ],
        'heat_recovery_inlet_high_temperature_limit_schedule_name': ['ScheduleNames'],
        'condenser_loop_flow_rate_fraction_function_of_loop_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'temperature_difference_across_condenser_schedule_name': ['ScheduleNames'],
        'thermosiphon_capacity_fraction_curve_name': ['UniVariateFunctions'],
    },
    'ChillerEngineDriven': {
        'fuel_use_curve_name': ['UnivariateFunctions'],
        'jacket_heat_recovery_curve_name': ['UnivariateFunctions'],
        'lube_heat_recovery_curve_name': ['UnivariateFunctions'],
        'total_exhaust_energy_curve_name': ['UnivariateFunctions'],
        'exhaust_temperature_curve_name': ['UnivariateFunctions'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
    },
    'ChillerHeaterAbsorptionDirectFired': {
        'cooling_capacity_function_of_temperature_curve_name': ['BivariateFunctions'],
        'fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_capacity_function_of_cooling_capacity_curve_name': [
            'UnivariateFunctions'
        ],
        'fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'ChillerHeaterAbsorptionDoubleEffect': {
        'cooling_capacity_function_of_temperature_curve_name': ['BivariateFunctions'],
        'fuel_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_capacity_function_of_cooling_capacity_curve_name': [
            'UnivariateFunctions'
        ],
        'fuel_input_to_heat_output_ratio_during_heating_only_operation_curve_name': [
            'UnivariateFunctions'
        ],
        'exhaust_source_object_name': ['MicroTurbineGeneratorNames'],
    },
    'ChillerHeaterPerformanceElectricEIR': {
        'cooling_mode_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_mode_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_mode_electric_input_to_cooling_output_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heating_mode_electric_input_to_cooling_output_ratio_function_of_part_load_ratio_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
    },
    'CoilCoolingDX': {
        'availability_schedule_name': ['ScheduleNames'],
        'condenser_zone_name': ['ZoneNames'],
        'performance_object_name': ['DXCoolingPerformanceNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'evaporative_condenser_supply_water_storage_tank_name': [
            'WaterStorageTankNames'
        ],
    },
    'CoilCoolingDXCurveFitOperatingMode': {
        'speed_1_name': ['DXCoolingSpeedNames'],
        'speed_2_name': ['DXCoolingSpeedNames'],
        'speed_3_name': ['DXCoolingSpeedNames'],
        'speed_4_name': ['DXCoolingSpeedNames'],
        'speed_5_name': ['DXCoolingSpeedNames'],
        'speed_6_name': ['DXCoolingSpeedNames'],
        'speed_7_name': ['DXCoolingSpeedNames'],
        'speed_8_name': ['DXCoolingSpeedNames'],
        'speed_9_name': ['DXCoolingSpeedNames'],
        'speed_10_name': ['DXCoolingSpeedNames'],
    },
    'CoilCoolingDXCurveFitPerformance': {
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'evaporative_condenser_basin_heater_operating_schedule_name': ['ScheduleNames'],
        'base_operating_mode': ['DXCoolingOperatingModeNames'],
        'alternative_operating_mode_1': ['DXCoolingOperatingModeNames'],
        'alternative_operating_mode_2': ['DXCoolingOperatingModeNames'],
    },
    'CoilCoolingDXCurveFitSpeed': {
        'total_cooling_capacity_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'total_cooling_capacity_modifier_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'energy_input_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'energy_input_ratio_modifier_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'waste_heat_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilCoolingDXMultiSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'speed_1_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_1_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_2_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_2_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_3_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_3_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_4_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_4_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'zone_name_for_condenser_placement': ['ZoneNames'],
    },
    'CoilCoolingDXSingleSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'energy_input_ratio_function_of_temperature_curve_name': ['BivariateFunctions'],
        'energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'zone_name_for_condenser_placement': ['ZoneNames'],
    },
    'CoilCoolingDXSingleSpeedThermalStorage': {
        'availability_schedule_name': ['ScheduleNames'],
        'operation_mode_control_schedule_name': ['ScheduleNames'],
        'user_defined_fluid_type': ['FluidAndGlycolNames'],
        'cooling_only_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_only_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_only_mode_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_only_mode_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_only_mode_sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'cooling_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_charge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_charge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_evaporator_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_storage_charge_capacity_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_charge_mode_storage_charge_capacity_function_of_total_evaporator_plr_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_storage_energy_input_ratio_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_charge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_storage_energy_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_charge_mode_sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'TrivariateFunctions',
        ],
        'cooling_and_charge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_discharge_mode_total_evaporator_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_discharge_mode_evaporator_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_evaporator_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_discharge_capacity_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_discharge_capacity_function_of_total_evaporator_plr_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_energy_input_ratio_function_of_temperature_curve_name': [
            'TrivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_storage_energy_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'cooling_and_discharge_mode_sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'TrivariateFunctions',
        ],
        'cooling_and_discharge_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'charge_only_mode_storage_charge_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'charge_only_mode_storage_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'discharge_only_mode_storage_discharge_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'discharge_only_mode_storage_discharge_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'discharge_only_mode_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'discharge_only_mode_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'discharge_only_mode_part_load_fraction_correlation_curve_name': [
            'UnivariateFunctions'
        ],
        'discharge_only_mode_sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'TrivariateFunctions',
        ],
        'discharge_only_mode_sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'basin_heater_availability_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoilCoolingDXTwoSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'energy_input_ratio_function_of_temperature_curve_name': ['BivariateFunctions'],
        'energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'low_speed_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'low_speed_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'low_speed_sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'low_speed_sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'zone_name_for_condenser_placement': ['ZoneNames'],
    },
    'CoilCoolingDXTwoStageWithHumidityControlMode': {
        'availability_schedule_name': ['ScheduleNames'],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'normal_mode_stage_1_coil_performance_name': ['CoilPerformanceDX'],
        'normal_mode_stage_1_2_coil_performance_name': ['CoilPerformanceDX'],
        'dehumidification_mode_1_stage_1_coil_performance_name': ['CoilPerformanceDX'],
        'dehumidification_mode_1_stage_1_2_coil_performance_name': [
            'CoilPerformanceDX'
        ],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
    },
    'CoilCoolingDXVariableRefrigerantFlow': {
        'availability_schedule_name': ['ScheduleNames'],
        'cooling_capacity_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'cooling_capacity_modifier_curve_function_of_flow_fraction_name': [
            'UnivariateFunctions'
        ],
        'name_of_water_storage_tank_for_condensate_collection': [
            'WaterStorageTankNames'
        ],
    },
    'CoilCoolingDXVariableRefrigerantFlowFluidTemperatureControl': {
        'availability_schedule_name': ['ScheduleNames'],
        'indoor_unit_evaporating_temperature_function_of_superheating_curve_name': [
            'UnivariateFunctions'
        ],
        'name_of_water_storage_tank_for_condensate_collection': [
            'WaterStorageTankNames'
        ],
    },
    'CoilCoolingDXVariableSpeed': {
        'energy_part_load_fraction_curve_name': ['UnivariateFunctions'],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'speed_1_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilCoolingWater': {
        'availability_schedule_name': ['ScheduleNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoilCoolingWaterDetailedGeometry': {
        'availability_schedule_name': ['ScheduleNames'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoilCoolingWaterToAirHeatPumpEquationFit': {
        'total_cooling_capacity_curve_name': ['QuadvariateFunctions'],
        'sensible_cooling_capacity_curve_name': ['QuintvariateFunctions'],
        'cooling_power_consumption_curve_name': ['QuadvariateFunctions'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilCoolingWaterToAirHeatPumpParameterEstimation': {
        'refrigerant_type': ['FluidNames'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilCoolingWaterToAirHeatPumpVariableSpeedEquationFit': {
        'energy_part_load_fraction_curve_name': ['UnivariateFunctions'],
        'speed_1_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_2_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_3_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_4_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_5_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_6_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_7_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_8_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_9_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_10_total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_total_cooling_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_total_cooling_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_waste_heat_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
    },
    'CoilHeatingDXMultiSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'defrost_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_1_heating_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_1_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_1_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_2_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_2_heating_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_2_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_2_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_3_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_3_heating_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_3_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_3_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_4_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_4_heating_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_4_energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_4_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_1_sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilHeatingDXSingleSpeed': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'defrost_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'sensible_heat_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilHeatingDXVariableRefrigerantFlow': {
        'availability_schedule': ['ScheduleNames'],
        'heating_capacity_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_capacity_modifier_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilHeatingDXVariableRefrigerantFlowFluidTemperatureControl': {
        'availability_schedule': ['ScheduleNames'],
        'indoor_unit_condensing_temperature_function_of_subcooling_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilHeatingDXVariableSpeed': {
        'energy_part_load_fraction_curve_name': ['UnivariateFunctions'],
        'defrost_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilHeatingDesuperheater': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_source_name': ['DesuperHeatingCoilSources'],
    },
    'CoilHeatingElectric': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'CoilHeatingElectricMultiStage': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'CoilHeatingFuel': {
        'availability_schedule_name': ['ScheduleNames'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilHeatingGasMultiStage': {
        'availability_schedule_name': ['ScheduleNames'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilHeatingSteam': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'CoilHeatingWater': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'CoilHeatingWaterToAirHeatPumpEquationFit': {
        'heating_capacity_curve_name': ['QuadvariateFunctions'],
        'heating_power_consumption_curve_name': ['QuadvariateFunctions'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilHeatingWaterToAirHeatPumpParameterEstimation': {
        'refrigerant_type': ['FluidNames'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilHeatingWaterToAirHeatPumpVariableSpeedEquationFit': {
        'energy_part_load_fraction_curve_name': ['UnivariateFunctions'],
        'speed_1_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_2_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_3_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_4_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_5_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_6_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_7_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_8_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_9_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_waste_heat_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_10_heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_total_heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_energy_input_ratio_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_waste_heat_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
    },
    'CoilPerformanceDXCooling': {
        'total_cooling_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'total_cooling_capacity_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'energy_input_ratio_function_of_temperature_curve_name': ['BivariateFunctions'],
        'energy_input_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'sensible_heat_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'sensible_heat_ratio_function_of_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilSystemCoolingDX': {
        'availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_name': [
            'CoilCoolingDX',
            'CoolingCoilsDX',
            'CoolingCoilsDXVariableSpeed',
        ],
    },
    'CoilSystemCoolingDXHeatExchangerAssisted': {
        'heat_exchanger_name': ['HXAirToAirNames'],
        'cooling_coil_name': [
            'CoilCoolingDX',
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
    },
    'CoilSystemCoolingWater': {
        'availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_name': ['CoolingCoilsWater'],
        'companion_coil_used_for_heat_recovery': ['CoolingCoilsWater'],
    },
    'CoilSystemCoolingWaterHeatExchangerAssisted': {
        'cooling_coil_name': ['CoolingCoilsWaterNoHX'],
    },
    'CoilSystemHeatingDX': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_coil_name': [
            'HeatingCoilsDXSingleSpeed',
            'HeatingCoilsDXVariableSpeed',
        ],
    },
    'CoilSystemIntegratedHeatPumpAirSource': {
        'space_cooling_coil_name': ['CoolingCoilsDXVariableSpeed'],
        'space_heating_coil_name': ['HeatingCoilsDXVariableSpeed'],
        'dedicated_water_heating_coil_name': [
            'HeatPumpWaterHeaterDXCoilsVariableSpeed'
        ],
        'scwh_coil_name': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
        'scdwh_cooling_coil_name': ['CoolingCoilsDXVariableSpeed'],
        'scdwh_water_heating_coil_name': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
        'shdwh_heating_coil_name': ['HeatingCoilsDXVariableSpeed'],
        'shdwh_water_heating_coil_name': ['HeatPumpWaterHeaterDXCoilsVariableSpeed'],
    },
    'CoilUserDefined': {
        'overall_model_simulation_program_calling_manager_name': ['ProgramNames'],
        'model_setup_and_sizing_program_calling_manager_name': ['ProgramNames'],
        'supply_inlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'collection_outlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'ambient_zone_name': ['ZoneNames'],
    },
    'CoilWaterHeatingAirToWaterHeatPumpPumped': {
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_cop_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'heating_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilWaterHeatingAirToWaterHeatPumpVariableSpeed': {
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'speed_1_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_1_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_1_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_1_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_1_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_2_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_2_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_2_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_2_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_3_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_3_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_3_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_3_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_4_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_4_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_4_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_4_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_5_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_5_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_5_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_5_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_6_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_6_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_6_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_6_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_7_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_7_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_7_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_7_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_8_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_8_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_8_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_8_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_9_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_9_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_9_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'speed_9_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_total_wh_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'speed_10_total_wh_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_total_wh_capacity_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_cop_function_of_temperature_curve_name': ['BivariateFunctions'],
        'speed_10_cop_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'speed_10_cop_function_of_water_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'CoilWaterHeatingAirToWaterHeatPumpWrapped': {
        'crankcase_heater_capacity_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_capacity_function_of_air_flow_fraction_curve_name': [
            'UnivariateFunctions'
        ],
        'heating_cop_function_of_temperature_curve_name': [
            'BivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_cop_function_of_air_flow_fraction_curve_name': ['UnivariateFunctions'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
    },
    'CoilWaterHeatingDesuperheater': {
        'availability_schedule_name': ['ScheduleNames'],
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
        'heat_reclaim_efficiency_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'tank_name': ['WaterHeaterMixedNames', 'WaterHeaterStratifiedNames'],
        'heating_source_name': [
            'CoilCoolingDX',
            'DesuperHeatingCoilSources',
            'DesuperHeatingWaterOnlySources',
        ],
    },
    'ComfortViewFactorAngles': {
        'surface_1_name': ['AllHeatTranSurfNames'],
        'surface_2_name': ['AllHeatTranSurfNames'],
        'surface_3_name': ['AllHeatTranSurfNames'],
        'surface_4_name': ['AllHeatTranSurfNames'],
        'surface_5_name': ['AllHeatTranSurfNames'],
        'surface_6_name': ['AllHeatTranSurfNames'],
        'surface_7_name': ['AllHeatTranSurfNames'],
        'surface_8_name': ['AllHeatTranSurfNames'],
        'surface_9_name': ['AllHeatTranSurfNames'],
        'surface_10_name': ['AllHeatTranSurfNames'],
        'surface_11_name': ['AllHeatTranSurfNames'],
        'surface_12_name': ['AllHeatTranSurfNames'],
        'surface_13_name': ['AllHeatTranSurfNames'],
        'surface_14_name': ['AllHeatTranSurfNames'],
        'surface_15_name': ['AllHeatTranSurfNames'],
        'surface_16_name': ['AllHeatTranSurfNames'],
        'surface_17_name': ['AllHeatTranSurfNames'],
        'surface_18_name': ['AllHeatTranSurfNames'],
        'surface_19_name': ['AllHeatTranSurfNames'],
        'surface_20_name': ['AllHeatTranSurfNames'],
        'surface_21_name': ['AllHeatTranSurfNames'],
        'surface_22_name': ['AllHeatTranSurfNames'],
        'surface_23_name': ['AllHeatTranSurfNames'],
        'surface_24_name': ['AllHeatTranSurfNames'],
        'surface_25_name': ['AllHeatTranSurfNames'],
        'surface_26_name': ['AllHeatTranSurfNames'],
        'surface_27_name': ['AllHeatTranSurfNames'],
        'surface_28_name': ['AllHeatTranSurfNames'],
        'surface_29_name': ['AllHeatTranSurfNames'],
        'surface_30_name': ['AllHeatTranSurfNames'],
        'surface_31_name': ['AllHeatTranSurfNames'],
        'surface_32_name': ['AllHeatTranSurfNames'],
        'surface_33_name': ['AllHeatTranSurfNames'],
        'surface_34_name': ['AllHeatTranSurfNames'],
        'surface_35_name': ['AllHeatTranSurfNames'],
        'surface_36_name': ['AllHeatTranSurfNames'],
        'surface_37_name': ['AllHeatTranSurfNames'],
        'surface_38_name': ['AllHeatTranSurfNames'],
        'surface_39_name': ['AllHeatTranSurfNames'],
        'surface_40_name': ['AllHeatTranSurfNames'],
        'surface_41_name': ['AllHeatTranSurfNames'],
        'surface_42_name': ['AllHeatTranSurfNames'],
        'surface_43_name': ['AllHeatTranSurfNames'],
        'surface_44_name': ['AllHeatTranSurfNames'],
        'surface_45_name': ['AllHeatTranSurfNames'],
        'surface_46_name': ['AllHeatTranSurfNames'],
        'surface_47_name': ['AllHeatTranSurfNames'],
        'surface_48_name': ['AllHeatTranSurfNames'],
        'surface_49_name': ['AllHeatTranSurfNames'],
        'surface_50_name': ['AllHeatTranSurfNames'],
        'surface_51_name': ['AllHeatTranSurfNames'],
        'surface_52_name': ['AllHeatTranSurfNames'],
        'surface_53_name': ['AllHeatTranSurfNames'],
        'surface_54_name': ['AllHeatTranSurfNames'],
        'surface_55_name': ['AllHeatTranSurfNames'],
        'surface_56_name': ['AllHeatTranSurfNames'],
        'surface_57_name': ['AllHeatTranSurfNames'],
        'surface_58_name': ['AllHeatTranSurfNames'],
        'surface_59_name': ['AllHeatTranSurfNames'],
        'surface_60_name': ['AllHeatTranSurfNames'],
        'surface_61_name': ['AllHeatTranSurfNames'],
        'surface_62_name': ['AllHeatTranSurfNames'],
        'surface_63_name': ['AllHeatTranSurfNames'],
        'surface_64_name': ['AllHeatTranSurfNames'],
        'surface_65_name': ['AllHeatTranSurfNames'],
        'surface_66_name': ['AllHeatTranSurfNames'],
        'surface_67_name': ['AllHeatTranSurfNames'],
        'surface_68_name': ['AllHeatTranSurfNames'],
        'surface_69_name': ['AllHeatTranSurfNames'],
        'surface_70_name': ['AllHeatTranSurfNames'],
        'surface_71_name': ['AllHeatTranSurfNames'],
        'surface_72_name': ['AllHeatTranSurfNames'],
        'surface_73_name': ['AllHeatTranSurfNames'],
        'surface_74_name': ['AllHeatTranSurfNames'],
        'surface_75_name': ['AllHeatTranSurfNames'],
        'surface_76_name': ['AllHeatTranSurfNames'],
        'surface_77_name': ['AllHeatTranSurfNames'],
        'surface_78_name': ['AllHeatTranSurfNames'],
        'surface_79_name': ['AllHeatTranSurfNames'],
        'surface_80_name': ['AllHeatTranSurfNames'],
        'surface_81_name': ['AllHeatTranSurfNames'],
        'surface_82_name': ['AllHeatTranSurfNames'],
        'surface_83_name': ['AllHeatTranSurfNames'],
        'surface_84_name': ['AllHeatTranSurfNames'],
        'surface_85_name': ['AllHeatTranSurfNames'],
        'surface_86_name': ['AllHeatTranSurfNames'],
        'surface_87_name': ['AllHeatTranSurfNames'],
        'surface_88_name': ['AllHeatTranSurfNames'],
        'surface_89_name': ['AllHeatTranSurfNames'],
        'surface_90_name': ['AllHeatTranSurfNames'],
        'surface_91_name': ['AllHeatTranSurfNames'],
        'surface_92_name': ['AllHeatTranSurfNames'],
        'surface_93_name': ['AllHeatTranSurfNames'],
        'surface_94_name': ['AllHeatTranSurfNames'],
        'surface_95_name': ['AllHeatTranSurfNames'],
        'surface_96_name': ['AllHeatTranSurfNames'],
        'surface_97_name': ['AllHeatTranSurfNames'],
        'surface_98_name': ['AllHeatTranSurfNames'],
        'surface_99_name': ['AllHeatTranSurfNames'],
        'surface_100_name': ['AllHeatTranSurfNames'],
    },
    'ComplexFenestrationPropertySolarAbsorbedLayers': {
        'fenestration_surface': ['SubSurfNames'],
        'construction_name': ['ComplexFenestrationStates'],
        'layer_1_solar_radiation_absorbed_schedule_name': ['ScheduleNames'],
        'layer_2_solar_radiation_absorbed_schedule_name': ['ScheduleNames'],
        'layer_3_solar_radiation_absorbed_schedule_name': ['ScheduleNames'],
        'layer_4_solar_radiation_absorbed_schedule_name': ['ScheduleNames'],
        'layer_5_solar_radiation_absorbed_schedule_name': ['ScheduleNames'],
    },
    'CondenserEquipmentListEquipmentItem': {
        'equipment_object_type': ['validCondenserEquipmentTypes'],
        'equipment_name': ['validCondenserEquipmentNames'],
    },
    'CondenserEquipmentOperationSchemes': {
        'control_scheme_1_name': ['ControlSchemeList'],
        'control_scheme_1_schedule_name': ['ScheduleNames'],
        'control_scheme_2_name': ['ControlSchemeList'],
        'control_scheme_2_schedule_name': ['ScheduleNames'],
        'control_scheme_3_name': ['ControlSchemeList'],
        'control_scheme_3_schedule_name': ['ScheduleNames'],
        'control_scheme_4_name': ['ControlSchemeList'],
        'control_scheme_4_schedule_name': ['ScheduleNames'],
        'control_scheme_5_name': ['ControlSchemeList'],
        'control_scheme_5_schedule_name': ['ScheduleNames'],
        'control_scheme_6_name': ['ControlSchemeList'],
        'control_scheme_6_schedule_name': ['ScheduleNames'],
        'control_scheme_7_name': ['ControlSchemeList'],
        'control_scheme_7_schedule_name': ['ScheduleNames'],
        'control_scheme_8_name': ['ControlSchemeList'],
        'control_scheme_8_schedule_name': ['ScheduleNames'],
    },
    'CondenserLoop': {
        'user_defined_fluid_type': ['FluidAndGlycolNames'],
        'condenser_equipment_operation_scheme_name': ['CondenserOperationSchemes'],
        'condenser_side_branch_list_name': ['BranchLists'],
        'condenser_side_connector_list_name': ['ConnectorLists'],
        'condenser_demand_side_branch_list_name': ['BranchLists'],
        'condenser_demand_side_connector_list_name': ['ConnectorLists'],
    },
    'ConnectorList': {
        'connector_1_name': ['PlantConnectors'],
        'connector_2_name': ['PlantConnectors'],
    },
    'ConnectorMixer': {
        'outlet_branch_name': ['Branches'],
    },
    'ConnectorMixerBranchesItem': {
        'inlet_branch_name': ['Branches'],
    },
    'ConnectorSplitter': {
        'inlet_branch_name': ['Branches'],
    },
    'ConnectorSplitterBranchesItem': {
        'outlet_branch_name': ['Branches'],
    },
    'Construction': {
        'outside_layer': ['MaterialName'],
        'layer_2': ['MaterialName'],
        'layer_3': ['MaterialName'],
        'layer_4': ['MaterialName'],
        'layer_5': ['MaterialName'],
        'layer_6': ['MaterialName'],
        'layer_7': ['MaterialName'],
        'layer_8': ['MaterialName'],
        'layer_9': ['MaterialName'],
        'layer_10': ['MaterialName'],
    },
    'ConstructionAirBoundary': {
        'simple_mixing_schedule_name': ['ScheduleNames'],
    },
    'ConstructionComplexFenestrationState': {
        'window_thermal_model': ['WindowThermalModelParameters'],
        'basis_matrix_name': ['DataMatrices'],
        'solar_optical_complex_front_transmittance_matrix_name': ['DataMatrices'],
        'solar_optical_complex_back_reflectance_matrix_name': ['DataMatrices'],
        'visible_optical_complex_front_transmittance_matrix_name': ['DataMatrices'],
        'visible_optical_complex_back_transmittance_matrix_name': ['DataMatrices'],
        'outside_layer_name': ['CFSGlazingName', 'WindowComplexShades'],
        'outside_layer_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'outside_layer_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'gap_1_name': ['CFSGap'],
        'cfs_gap_1_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'cfs_gap_1_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'layer_2_name': ['CFSGlazingName', 'WindowComplexShades'],
        'layer_2_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'layer_2_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'gap_2_name': ['CFSGap'],
        'gap_2_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'gap_2_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'layer_3_name': ['CFSGlazingName', 'WindowComplexShades'],
        'layer_3_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'layer_3_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'gap_3_name': ['CFSGap'],
        'gap_3_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'gap_3_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'layer_4_name': ['CFSGlazingName', 'WindowComplexShades'],
        'layer_4_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'layer_4_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'gap_4_name': ['CFSGap'],
        'gap_4_directional_front_absorptance_matrix_name': ['DataMatrices'],
        'gap_4_directional_back_absorptance_matrix_name': ['DataMatrices'],
        'layer_5_name': ['CFSGlazingName', 'WindowComplexShades'],
        'layer_5_directional_front_absorptance_matrix_name': ['DataMatrices'],
    },
    'ConstructionPropertyInternalHeatSource': {
        'construction_name': ['ConstructionNames'],
    },
    'ConstructionWindowEquivalentLayer': {
        'outside_layer': ['WindowEquivalentLayerMaterialNames'],
        'layer_2': ['WindowEquivalentLayerMaterialNames'],
        'layer_3': ['WindowEquivalentLayerMaterialNames'],
        'layer_4': ['WindowEquivalentLayerMaterialNames'],
        'layer_5': ['WindowEquivalentLayerMaterialNames'],
        'layer_6': ['WindowEquivalentLayerMaterialNames'],
        'layer_7': ['WindowEquivalentLayerMaterialNames'],
        'layer_8': ['WindowEquivalentLayerMaterialNames'],
        'layer_9': ['WindowEquivalentLayerMaterialNames'],
        'layer_10': ['WindowEquivalentLayerMaterialNames'],
        'layer_11': ['WindowEquivalentLayerMaterialNames'],
    },
    'ControllerMechanicalVentilation': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ControllerMechanicalVentilationZoneSpecificationsItem': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'ControllerOutdoorAir': {
        'electronic_enthalpy_limit_curve_name': ['UnivariateFunctions'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'minimum_fraction_of_outdoor_air_schedule_name': ['ScheduleNames'],
        'maximum_fraction_of_outdoor_air_schedule_name': ['ScheduleNames'],
        'mechanical_ventilation_controller_name': ['ControllerMechanicalVentNames'],
        'time_of_day_economizer_control_schedule_name': ['ScheduleNames'],
        'humidistat_control_zone_name': ['ZoneNames'],
    },
    'CoolingTowerSingleSpeed': {
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoolingTowerTwoSpeed': {
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoolingTowerVariableSpeed': {
        'model_coefficient_name': ['VariableSpeedTowerCoefficient'],
        'fan_power_ratio_function_of_air_flow_rate_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'CoolingTowerVariableSpeedMerkel': {
        'fan_power_modifier_function_of_air_flow_rate_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'u_factor_times_area_modifier_function_of_air_flow_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'u_factor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name': [
            'UnivariateFunctions'
        ],
        'u_factor_times_area_modifier_function_of_water_flow_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'DaylightingControls': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'glare_calculation_daylighting_reference_point_name': [
            'DaylightReferencePointNames'
        ],
    },
    'DaylightingControlsControlDataItem': {
        'daylighting_reference_point_name': ['DaylightReferencePointNames'],
    },
    'DaylightingDELightComplexFenestration': {
        'building_surface_name': ['SurfaceNames'],
        'window_name': ['SubSurfNames'],
    },
    'DaylightingDeviceLightWell': {
        'exterior_window_name': ['SubSurfNames'],
    },
    'DaylightingDeviceShelf': {
        'window_name': ['SubSurfNames'],
        'inside_shelf_name': ['SurfaceNames'],
        'outside_shelf_name': ['AttachedShadingSurfNames'],
        'outside_shelf_construction_name': ['ConstructionNames'],
    },
    'DaylightingDeviceTubular': {
        'dome_name': ['SubSurfNames'],
        'diffuser_name': ['SubSurfNames'],
        'construction_name': ['ConstructionNames'],
    },
    'DaylightingDeviceTubularTransitionLengthsItem': {
        'transition_zone_name': ['ZoneNames'],
    },
    'DaylightingReferencePoint': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
    },
    'DehumidifierDesiccantNoFans': {
        'availability_schedule_name': ['ScheduleNames'],
        'regeneration_coil_name': ['HeatingCoilName'],
        'regeneration_fan_name': ['FansCVandVAV', 'FansSystemModel'],
        'leaving_dry_bulb_function_of_entering_dry_bulb_and_humidity_ratio_curve_name': [
            'BivariateFunctions'
        ],
        'leaving_dry_bulb_function_of_air_velocity_curve_name': ['UnivariateFunctions'],
        'leaving_humidity_ratio_function_of_entering_dry_bulb_and_humidity_ratio_curve_name': [
            'BivariateFunctions'
        ],
        'leaving_humidity_ratio_function_of_air_velocity_curve_name': [
            'UnivariateFunctions'
        ],
        'regeneration_energy_function_of_entering_dry_bulb_and_humidity_ratio_curve_name': [
            'BivariateFunctions'
        ],
        'regeneration_energy_function_of_air_velocity_curve_name': [
            'UnivariateFunctions'
        ],
        'regeneration_velocity_function_of_entering_dry_bulb_and_humidity_ratio_curve_name': [
            'BivariateFunctions'
        ],
        'regeneration_velocity_function_of_air_velocity_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'DehumidifierDesiccantSystem': {
        'availability_schedule_name': ['ScheduleNames'],
        'desiccant_heat_exchanger_name': ['HXDesiccantBalanced'],
        'regeneration_air_fan_name': ['FansOnOffandVAV', 'FansSystemModel'],
        'regeneration_air_heater_name': ['HeatingCoilName'],
        'companion_cooling_coil_name': [
            'CoolingCoilsDXMultiModeOrSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'exhaust_fan_power_curve_name': ['UnivariateFunctions'],
    },
    'DemandManagerAssignmentList': {
        'demand_limit_schedule_name': ['ScheduleNames'],
        'billing_period_schedule_name': ['ScheduleNames'],
        'peak_period_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerAssignmentListManagerDataItem': {
        'demandmanager_name': ['DemandManagerNames'],
    },
    'DemandManagerElectricEquipment': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerElectricEquipmentEquipmentItem': {
        'electric_equipment_name': ['ElectricEquipmentNames'],
    },
    'DemandManagerExteriorLights': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerExteriorLightsLightsItem': {
        'exterior_lights_name': ['ExteriorLightsNames'],
    },
    'DemandManagerLights': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerLightsLightsItem': {
        'lights_name': ['LightsNames'],
    },
    'DemandManagerThermostats': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerThermostatsThermostatsItem': {
        'thermostat_name': ['ZoneControlThermostaticNames'],
    },
    'DemandManagerVentilation': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'DemandManagerVentilationControllersItem': {
        'controller_outdoor_air_name': ['OAControllerNames'],
    },
    'DesignSpecificationOutdoorAir': {
        'outdoor_air_schedule_name': ['ScheduleNames'],
        'proportional_control_minimum_outdoor_air_flow_rate_schedule_name': [
            'ScheduleNames'
        ],
    },
    'DesignSpecificationOutdoorAirSpaceListSpaceSpecsItem': {
        'space_name': ['SpaceNames'],
        'space_design_specification_outdoor_air_object_name': [
            'DesignSpecificationOutdoorAirNames'
        ],
    },
    'DesignSpecificationZoneAirDistribution': {
        'zone_air_distribution_effectiveness_schedule_name': ['ScheduleNames'],
    },
    'DistrictCooling': {
        'capacity_fraction_schedule_name': ['ScheduleNames'],
    },
    'DistrictHeatingSteam': {
        'capacity_fraction_schedule_name': ['ScheduleNames'],
    },
    'DistrictHeatingWater': {
        'capacity_fraction_schedule_name': ['ScheduleNames'],
    },
    'Door': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
    },
    'DoorInterzone': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'ElectricEquipment': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'ElectricEquipmentITEAirCooled': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'design_power_input_schedule_name': ['ScheduleNames'],
        'cpu_loading_schedule_name': ['ScheduleNames'],
        'cpu_power_input_function_of_loading_and_air_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'air_flow_function_of_loading_and_air_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fan_power_input_function_of_flow_curve_name': ['UnivariateFunctions'],
        'air_inlet_room_air_model_node_name': ['RoomAirNodes'],
        'air_outlet_room_air_model_node_name': ['RoomAirNodes'],
        'recirculation_function_of_loading_and_supply_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_power_supply_efficiency_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'supply_temperature_difference_schedule': ['ScheduleNames'],
        'return_temperature_difference_schedule': ['ScheduleNames'],
    },
    'ElectricLoadCenterDistribution': {
        'generator_list_name': ['GeneratorLists'],
        'generator_track_schedule_name_scheme_schedule_name': ['ScheduleNames'],
        'inverter_name': ['InverterList'],
        'electrical_storage_object_name': ['ElecStorageList'],
        'transformer_object_name': ['TransformerNames'],
        'storage_converter_object_name': ['ConverterList'],
        'storage_charge_power_fraction_schedule_name': ['ScheduleNames'],
        'storage_discharge_power_fraction_schedule_name': ['ScheduleNames'],
        'storage_control_utility_demand_target_fraction_schedule_name': [
            'ScheduleNames'
        ],
    },
    'ElectricLoadCenterGeneratorsGeneratorOutputsItem': {
        'generator_name': ['GeneratorNames'],
        'generator_availability_schedule_name': ['ScheduleNames'],
    },
    'ElectricLoadCenterInverterFunctionOfPower': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'efficiency_function_of_power_curve_name': ['UnivariateFunctions'],
    },
    'ElectricLoadCenterInverterLookUpTable': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'ElectricLoadCenterInverterSimple': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'ElectricLoadCenterStorageBattery': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'voltage_change_curve_name_for_charging': ['UnivariateFunctions'],
        'voltage_change_curve_name_for_discharging': ['UnivariateFunctions'],
        'battery_life_curve_name': ['UnivariateFunctions'],
    },
    'ElectricLoadCenterStorageConverter': {
        'availability_schedule_name': ['ScheduleNames'],
        'efficiency_function_of_power_curve_name': ['UnivariateFunctions'],
        'zone_name': ['ZoneNames'],
    },
    'ElectricLoadCenterStorageLiIonNMCBattery': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'ElectricLoadCenterStorageSimple': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'ElectricLoadCenterTransformer': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'EnergyManagementSystemConstructionIndexVariable': {
        'construction_object_name': ['ConstructionNames'],
    },
    'EnergyManagementSystemCurveOrTableIndexVariable': {
        'curve_or_table_object_name': [
            'BivariateFunctions',
            'MultivariateFunctions',
            'QuadvariateFunctions',
            'QuintvariateFunctions',
            'TrivariateFunctions',
            'UnivariateFunctions',
        ],
    },
    'EnergyManagementSystemProgramCallingManagerProgramsItem': {
        'program_name': ['ErlProgramNames'],
    },
    'EvaporativeCoolerDirectCelDekPad': {
        'availability_schedule_name': ['ScheduleNames'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeCoolerDirectResearchSpecial': {
        'availability_schedule_name': ['ScheduleNames'],
        'effectiveness_flow_ratio_modifier_curve_name': ['UnivariateFunctions'],
        'water_pump_power_modifier_curve_name': ['UnivariateFunctions'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeCoolerIndirectCelDekPad': {
        'availability_schedule_name': ['ScheduleNames'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeCoolerIndirectResearchSpecial': {
        'availability_schedule_name': ['ScheduleNames'],
        'wetbulb_effectiveness_flow_ratio_modifier_curve_name': ['UnivariateFunctions'],
        'drybulb_effectiveness_flow_ratio_modifier_curve_name': ['UnivariateFunctions'],
        'water_pump_power_modifier_curve_name': ['UnivariateFunctions'],
        'secondary_air_fan_power_modifier_curve_name': ['UnivariateFunctions'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeCoolerIndirectWetCoil': {
        'availability_schedule_name': ['ScheduleNames'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeFluidCoolerSingleSpeed': {
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'EvaporativeFluidCoolerTwoSpeed': {
        'blowdown_makeup_water_usage_schedule_name': ['ScheduleNames'],
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'ExteriorFuelEquipment': {
        'schedule_name': ['ScheduleNames'],
    },
    'ExteriorLights': {
        'schedule_name': ['ScheduleNames'],
    },
    'ExteriorWaterEquipment': {
        'schedule_name': ['ScheduleNames'],
    },
    'ExternalInterfaceFunctionalMockupUnitExportToSchedule': {
        'schedule_type_limits_names': ['ScheduleTypeLimitsNames'],
    },
    'ExternalInterfaceFunctionalMockupUnitImportFromVariable': {
        'fmu_file_name': ['FMUFileName'],
    },
    'ExternalInterfaceFunctionalMockupUnitImportToActuator': {
        'fmu_file_name': ['FMUFileName'],
    },
    'ExternalInterfaceFunctionalMockupUnitImportToSchedule': {
        'schedule_type_limits_names': ['ScheduleTypeLimitsNames'],
        'fmu_file_name': ['FMUFileName'],
    },
    'ExternalInterfaceFunctionalMockupUnitImportToVariable': {
        'fmu_file_name': ['FMUFileName'],
    },
    'ExternalInterfaceSchedule': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'FanComponentModel': {
        'availability_schedule_name': ['ScheduleNames'],
        'fan_pressure_rise_curve_name': ['BivariateFunctions'],
        'duct_static_pressure_reset_curve_name': ['UnivariateFunctions'],
        'normalized_fan_static_efficiency_curve_name_non_stall_region': [
            'UnivariateFunctions'
        ],
        'normalized_fan_static_efficiency_curve_name_stall_region': [
            'UnivariateFunctions'
        ],
        'normalized_dimensionless_airflow_curve_name_non_stall_region': [
            'UnivariateFunctions'
        ],
        'normalized_dimensionless_airflow_curve_name_stall_region': [
            'UnivariateFunctions'
        ],
        'maximum_belt_efficiency_curve_name': ['UnivariateFunctions'],
        'normalized_belt_efficiency_curve_name_region_1': ['UnivariateFunctions'],
        'normalized_belt_efficiency_curve_name_region_2': ['UnivariateFunctions'],
        'normalized_belt_efficiency_curve_name_region_3': ['UnivariateFunctions'],
        'maximum_motor_efficiency_curve_name': ['UnivariateFunctions'],
        'normalized_motor_efficiency_curve_name': ['UnivariateFunctions'],
        'vfd_efficiency_curve_name': ['UnivariateFunctions'],
    },
    'FanConstantVolume': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'FanOnOff': {
        'availability_schedule_name': ['ScheduleNames'],
        'fan_power_ratio_function_of_speed_ratio_curve_name': ['UnivariateFunctions'],
        'fan_efficiency_ratio_function_of_speed_ratio_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'FanPerformanceNightVentilation': {
        'fan_name': ['FansCVandVAV', 'FansComponentModel'],
    },
    'FanSystemModel': {
        'availability_schedule_name': ['ScheduleNames'],
        'electric_power_function_of_flow_fraction_curve_name': ['UnivariateFunctions'],
        'motor_loss_zone_name': ['ZoneNames'],
    },
    'FanVariableVolume': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'FanZoneExhaust': {
        'availability_schedule_name': ['ScheduleNames'],
        'flow_fraction_schedule_name': ['ScheduleNames'],
        'minimum_zone_temperature_limit_schedule_name': ['ScheduleNames'],
        'balanced_exhaust_fraction_schedule_name': ['ScheduleNames'],
    },
    'FaultModelEnthalpySensorOffsetOutdoorAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'controller_object_name': ['OAControllerNames'],
    },
    'FaultModelEnthalpySensorOffsetReturnAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'controller_object_name': ['OAControllerNames'],
    },
    'FaultModelFoulingAirFilter': {
        'fan_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
        'availability_schedule_name': ['ScheduleNames'],
        'pressure_fraction_schedule_name': ['ScheduleNames'],
        'fan_curve_name': ['UnivariateFunctions'],
    },
    'FaultModelFoulingBoiler': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'boiler_object_name': ['Boilers'],
    },
    'FaultModelFoulingChiller': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'chiller_object_name': ['Chillers'],
    },
    'FaultModelFoulingCoil': {
        'coil_name': ['SimpleCoils'],
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
    },
    'FaultModelFoulingCoolingTower': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'cooling_tower_object_name': ['CoolingTowersWithUA'],
    },
    'FaultModelFoulingEvaporativeCooler': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'evaporative_cooler_object_name': ['Chillers'],
    },
    'FaultModelHumidistatOffset': {
        'humidistat_name': ['ZoneControlHumidistatNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'related_thermostat_offset_fault_name': ['ThermostatOffsetFaults'],
    },
    'FaultModelHumiditySensorOffsetOutdoorAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'controller_object_name': ['OAControllerNames'],
    },
    'FaultModelTemperatureSensorOffsetChillerSupplyWater': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'chiller_object_name': ['Chillers'],
    },
    'FaultModelTemperatureSensorOffsetCoilSupplyAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'coil_object_name': [
            'CoolingCoilName',
            'CoolingCoilSystemName',
            'DOAToZonalUnit',
            'HeatingCoilName',
            'HeatingCoilSystemName',
            'HeatingCoilsDesuperheater',
            'HeatingCoilsElectricMultiStage',
            'HeatingCoilsGasMultiStage',
        ],
        'water_coil_controller_name': ['WaterCoilControllers'],
    },
    'FaultModelTemperatureSensorOffsetCondenserSupplyWater': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'cooling_tower_object_name': ['CoolingTowers'],
    },
    'FaultModelTemperatureSensorOffsetOutdoorAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'controller_object_name': ['OAControllerNames'],
    },
    'FaultModelTemperatureSensorOffsetReturnAir': {
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
        'controller_object_name': ['OAControllerNames'],
    },
    'FaultModelThermostatOffset': {
        'thermostat_name': ['ZoneControlThermostaticNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'severity_schedule_name': ['ScheduleNames'],
    },
    'FenestrationSurfaceDetailed': {
        'construction_name': ['ComplexFenestrationStates', 'ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
        'frame_and_divider_name': ['WindowFrameAndDividerNames'],
    },
    'FloorAdiabatic': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'FloorDetailed': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'FloorGroundContact': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'FloorInterzone': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'FluidPropertiesConcentration': {
        'fluid_name': ['FluidNames'],
        'temperature_values_name': ['FluidPropertyTemperatures'],
    },
    'FluidPropertiesGlycolConcentration': {
        'user_defined_glycol_name': ['FluidAndGlycolNames'],
    },
    'FluidPropertiesSaturated': {
        'fluid_name': ['FluidNames'],
        'temperature_values_name': ['FluidPropertyTemperatures'],
    },
    'FluidPropertiesSuperheated': {
        'fluid_name': ['FluidNames'],
        'temperature_values_name': ['FluidPropertyTemperatures'],
    },
    'FoundationKiva': {
        'interior_horizontal_insulation_material_name': ['MaterialName'],
        'interior_vertical_insulation_material_name': ['MaterialName'],
        'exterior_horizontal_insulation_material_name': ['MaterialName'],
        'exterior_vertical_insulation_material_name': ['MaterialName'],
        'footing_wall_construction_name': ['ConstructionNames'],
        'footing_material_name': ['MaterialName'],
    },
    'FoundationKivaBlocksItem': {
        'custom_block_material_name': ['MaterialName'],
    },
    'FuelFactors': {
        'source_energy_schedule_name': ['ScheduleNames'],
        'co2_emission_factor_schedule_name': ['ScheduleNames'],
        'co_emission_factor_schedule_name': ['ScheduleNames'],
        'ch4_emission_factor_schedule_name': ['ScheduleNames'],
        'nox_emission_factor_schedule_name': ['ScheduleNames'],
        'n2o_emission_factor_schedule_name': ['ScheduleNames'],
        'so2_emission_factor_schedule_name': ['ScheduleNames'],
        'pm_emission_factor_schedule_name': ['ScheduleNames'],
        'pm10_emission_factor_schedule_name': ['ScheduleNames'],
        'pm2_5_emission_factor_schedule_name': ['ScheduleNames'],
        'nh3_emission_factor_schedule_name': ['ScheduleNames'],
        'nmvoc_emission_factor_schedule_name': ['ScheduleNames'],
        'hg_emission_factor_schedule_name': ['ScheduleNames'],
        'pb_emission_factor_schedule_name': ['ScheduleNames'],
        'water_emission_factor_schedule_name': ['ScheduleNames'],
        'nuclear_high_level_emission_factor_schedule_name': ['ScheduleNames'],
        'nuclear_low_level_emission_factor_schedule_name': ['ScheduleNames'],
    },
    'GasEquipment': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'GeneratorCombustionTurbine': {
        'part_load_based_fuel_input_curve_name': ['UnivariateFunctions'],
        'temperature_based_fuel_input_curve_name': ['UnivariateFunctions'],
        'exhaust_flow_curve_name': ['UnivariateFunctions'],
        'part_load_based_exhaust_temperature_curve_name': ['UnivariateFunctions'],
        'temperature_based_exhaust_temperature_curve_name': ['UnivariateFunctions'],
        'heat_recovery_lube_energy_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorFuelCell': {
        'power_module_name': ['FCPMNames'],
        'air_supply_name': ['FCAirSupNames'],
        'fuel_supply_name': ['GenFuelSupNames'],
        'water_supply_name': ['FCWaterSupNames'],
        'auxiliary_heater_name': ['FCAuxHeatNames'],
        'heat_exchanger_name': ['FCExhaustHXNames'],
        'electrical_storage_name': ['FCStorageNames'],
        'inverter_name': ['FCInverterNames'],
        'stack_cooler_name': ['FCStackCoolerNames'],
    },
    'GeneratorFuelCellAirSupply': {
        'blower_power_curve_name': ['UnivariateFunctions'],
        'air_rate_function_of_electric_power_curve_name': ['UnivariateFunctions'],
        'air_rate_function_of_fuel_rate_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorFuelCellAuxiliaryHeater': {
        'zone_name_to_receive_skin_losses': ['ZoneNames'],
    },
    'GeneratorFuelCellInverter': {
        'efficiency_function_of_dc_power_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorFuelCellPowerModule': {
        'efficiency_curve_name': ['UnivariateFunctions'],
        'zone_name': ['ZoneNames'],
        'skin_loss_quadratic_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorFuelCellWaterSupply': {
        'reformer_water_flow_rate_function_of_fuel_rate_curve_name': [
            'UnivariateFunctions'
        ],
        'reformer_water_pump_power_function_of_fuel_rate_curve_name': [
            'UnivariateFunctions'
        ],
        'water_temperature_schedule_name': ['ScheduleNames'],
    },
    'GeneratorFuelSupply': {
        'fuel_temperature_schedule_name': ['ScheduleNames'],
        'compressor_power_multiplier_function_of_fuel_rate_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'GeneratorInternalCombustionEngine': {
        'shaft_power_curve_name': ['UnivariateFunctions'],
        'jacket_heat_recovery_curve_name': ['UnivariateFunctions'],
        'lube_heat_recovery_curve_name': ['UnivariateFunctions'],
        'total_exhaust_energy_curve_name': ['UnivariateFunctions'],
        'exhaust_temperature_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorMicroCHP': {
        'performance_parameters_name': ['MicroCHPParametersNames'],
        'zone_name': ['ZoneNames'],
        'generator_fuel_supply_name': ['GenFuelSupNames'],
        'availability_schedule_name': ['ScheduleNames'],
    },
    'GeneratorMicroCHPNonNormalizedParameters': {
        'electrical_efficiency_curve_name': ['TrivariateFunctions'],
        'thermal_efficiency_curve_name': ['TrivariateFunctions'],
        'cooling_water_flow_rate_curve_name': ['BivariateFunctions'],
        'air_flow_rate_curve_name': ['UnivariateFunctions'],
    },
    'GeneratorMicroTurbine': {
        'electrical_power_function_of_temperature_and_elevation_curve_name': [
            'BivariateFunctions'
        ],
        'electrical_efficiency_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'electrical_efficiency_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'ancillary_power_function_of_fuel_input_curve_name': ['UnivariateFunctions'],
        'heat_recovery_water_flow_rate_function_of_temperature_and_power_curve_name': [
            'BivariateFunctions'
        ],
        'thermal_efficiency_function_of_temperature_and_elevation_curve_name': [
            'BivariateFunctions'
        ],
        'heat_recovery_rate_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'heat_recovery_rate_function_of_inlet_water_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'heat_recovery_rate_function_of_water_flow_rate_curve_name': [
            'UnivariateFunctions'
        ],
        'exhaust_air_flow_rate_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'exhaust_air_flow_rate_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'exhaust_air_temperature_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'exhaust_air_temperature_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'GeneratorPVWatts': {
        'surface_name': ['AllShadingAndHTSurfNames'],
    },
    'GeneratorPhotovoltaic': {
        'surface_name': ['AllShadingAndHTSurfNames'],
        'module_performance_name': ['PVModules'],
    },
    'GeneratorWindTurbine': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'GlazedDoor': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'frame_and_divider_name': ['WindowFrameAndDividerNames'],
    },
    'GlazedDoorInterzone': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'GroundHeatExchangerHorizontalTrench': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
    },
    'GroundHeatExchangerResponseFactors': {
        'ghe_vertical_properties_object_name': [
            'GroundHeatExchangerVerticalPropertiesNames'
        ],
    },
    'GroundHeatExchangerSlinky': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
    },
    'GroundHeatExchangerSurface': {
        'construction_name': ['ConstructionNames'],
    },
    'GroundHeatExchangerSystem': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
        'ghe_vertical_responsefactors_object_name': [
            'GroundHeatExchangerVerticalResponseFactorNames'
        ],
        'ghe_vertical_array_object_name': ['GroundHeatExchangerVerticalArrayNames'],
    },
    'GroundHeatExchangerSystemVerticalWellLocationsItem': {
        'ghe_vertical_single_object_name': ['GroundHeatExchangerVerticalSingleNames'],
    },
    'GroundHeatExchangerVerticalArray': {
        'ghe_vertical_properties_object_name': [
            'GroundHeatExchangerVerticalPropertiesNames'
        ],
    },
    'GroundHeatExchangerVerticalSingle': {
        'ghe_vertical_properties_object_name': [
            'GroundHeatExchangerVerticalPropertiesNames'
        ],
    },
    'HVACTemplatePlantBoilerObjectReference': {
        'boiler_name': ['Boilers'],
    },
    'HVACTemplatePlantChilledWaterLoop': {
        'pump_schedule_name': ['ScheduleNames'],
        'chiller_plant_equipment_operation_schemes_name': ['PlantOperationSchemes'],
        'chilled_water_setpoint_schedule_name': ['ScheduleNames'],
        'condenser_equipment_operation_schemes_name': ['CondenserOperationSchemes'],
        'condenser_water_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplatePlantChillerObjectReference': {
        'chiller_name': ['Chillers'],
    },
    'HVACTemplatePlantHotWaterLoop': {
        'pump_schedule_name': ['ScheduleNames'],
        'hot_water_plant_equipment_operation_schemes_name': ['PlantOperationSchemes'],
        'hot_water_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplatePlantMixedWaterLoop': {
        'pump_schedule_name': ['ScheduleNames'],
        'equipment_operation_schemes_name': ['PlantOperationSchemes'],
        'high_temperature_setpoint_schedule_name': ['ScheduleNames'],
        'low_temperature_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplatePlantTowerObjectReference': {
        'cooling_tower_name': ['CoolingTowers'],
    },
    'HVACTemplateSystemConstantVolume': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_control_zone_name': ['HVACTemplateConstantVolumeZones'],
        'cooling_coil_setpoint_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_control_zone_name': ['HVACTemplateConstantVolumeZones'],
        'heating_coil_setpoint_schedule_name': ['ScheduleNames'],
        'preheat_coil_availability_schedule_name': ['ScheduleNames'],
        'preheat_coil_setpoint_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'dehumidification_control_zone_name': ['ZoneNames'],
        'dehumidification_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
        'humidifier_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateSystemDedicatedOutdoorAir': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_setpoint_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_setpoint_schedule_name': ['ScheduleNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'dehumidification_setpoint_schedule_name': ['ScheduleNames'],
        'humidifier_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateSystemDualDuct': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_setpoint_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_setpoint_schedule_name': ['ScheduleNames'],
        'preheat_coil_availability_schedule_name': ['ScheduleNames'],
        'preheat_coil_setpoint_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'cold_supply_plenum_name': ['ZoneNames'],
        'hot_supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'dehumidification_control_zone_name': ['ZoneNames'],
        'dehumidification_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
        'humidifier_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateSystemPackagedVAV': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_setpoint_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_setpoint_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'dehumidification_control_zone_name': ['ZoneNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
    },
    'HVACTemplateSystemUnitary': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'control_zone_or_thermostat_location_name': ['ZoneNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
    },
    'HVACTemplateSystemUnitaryHeatPumpAirToAir': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'control_zone_or_thermostat_location_name': ['ZoneNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heat_pump_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'supplemental_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
    },
    'HVACTemplateSystemUnitarySystem': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'control_zone_or_thermostat_location_name': ['ZoneNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'supplemental_heating_or_reheat_coil_availability_schedule_name': [
            'ScheduleNames'
        ],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'dehumidification_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
        'humidifier_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateSystemVAV': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_setpoint_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_setpoint_schedule_name': ['ScheduleNames'],
        'preheat_coil_availability_schedule_name': ['ScheduleNames'],
        'preheat_coil_setpoint_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'night_cycle_control_zone_name': ['ZoneNames'],
        'dehumidification_control_zone_name': ['ZoneNames'],
        'humidifier_availability_schedule_name': ['ScheduleNames'],
        'humidifier_control_zone_name': ['ZoneNames'],
    },
    'HVACTemplateSystemVRF': {
        'system_availability_schedule_name': ['ScheduleNames'],
        'zone_name_for_master_thermostat_location': ['ZoneNames'],
        'thermostat_priority_schedule_name': ['ScheduleNames'],
        'basin_heater_operating_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateThermostat': {
        'heating_setpoint_schedule_name': ['ScheduleNames'],
        'cooling_setpoint_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneBaseboardHeat': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'HVACTemplateZoneConstantVolume': {
        'zone_name': ['ZoneNames'],
        'template_constant_volume_system_name': ['CompactHVACSystemConstantVolume'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'reheat_coil_availability_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneDualDuct': {
        'zone_name': ['ZoneNames'],
        'template_dual_duct_system_name': ['CompactHVACSystemDualDuct'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'design_specification_outdoor_air_object_name_for_sizing': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'design_specification_outdoor_air_object_name_for_control': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'cold_supply_plenum_name': ['ZoneNames'],
        'hot_supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneFanCoil': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'system_availability_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'outdoor_air_schedule_name': ['ScheduleNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneIdealLoadsAirSystem': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'system_availability_schedule_name': ['ScheduleNames'],
        'heating_availability_schedule_name': ['ScheduleNames'],
        'cooling_availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
    },
    'HVACTemplateZonePTAC': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'system_availability_schedule_name': ['ScheduleNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heating_coil_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZonePTHP': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'system_availability_schedule_name': ['ScheduleNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heat_pump_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'supplemental_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneUnitary': {
        'zone_name': ['ZoneNames'],
        'template_unitary_system_name': ['CompactHVACSystemUnitary'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'HVACTemplateZoneVAV': {
        'zone_name': ['ZoneNames'],
        'template_vav_system_name': ['CompactHVACSystemVAV'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'minimum_air_flow_fraction_schedule_name': ['ScheduleNames'],
        'reheat_coil_availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name_for_control': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name_for_sizing': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'HVACTemplateZoneVAVFanPowered': {
        'zone_name': ['ZoneNames'],
        'template_vav_system_name': ['CompactHVACSystemVAV'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'reheat_coil_availability_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
        'zone_piu_fan_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'HVACTemplateZoneVAVHeatAndCool': {
        'zone_name': ['ZoneNames'],
        'template_vav_system_name': ['CompactHVACSystemVAV'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'design_specification_outdoor_air_object_name_for_sizing': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'reheat_coil_availability_schedule_name': ['ScheduleNames'],
        'supply_plenum_name': ['ZoneNames'],
        'return_plenum_name': ['ZoneNames'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneVRF': {
        'zone_name': ['ZoneNames'],
        'template_vrf_system_name': ['CompactHVACSystemVRF'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'system_availability_schedule_name': ['ScheduleNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'cooling_coil_availability_schedule_name': ['ScheduleNames'],
        'heat_pump_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HVACTemplateZoneWaterToAirHeatPump': {
        'zone_name': ['ZoneNames'],
        'template_thermostat_name': ['CompactHVACThermostats'],
        'system_availability_schedule_name': ['ScheduleNames'],
        'supply_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'supplemental_heating_coil_availability_schedule_name': ['ScheduleNames'],
        'dedicated_outdoor_air_system_name': ['HVACTemplateDOASSystems'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
        'baseboard_heating_availability_schedule_name': ['ScheduleNames'],
    },
    'HeaderedPumpsConstantSpeed': {
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'HeaderedPumpsVariableSpeed': {
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'HeatExchangerAirToAirFlatPlate': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'HeatExchangerAirToAirSensibleAndLatent': {
        'availability_schedule_name': ['ScheduleNames'],
        'sensible_effectiveness_of_heating_air_flow_curve_name': [
            'UnivariateFunctions'
        ],
        'latent_effectiveness_of_heating_air_flow_curve_name': ['UnivariateFunctions'],
        'sensible_effectiveness_of_cooling_air_flow_curve_name': [
            'UnivariateFunctions'
        ],
        'latent_effectiveness_of_cooling_air_flow_curve_name': ['UnivariateFunctions'],
    },
    'HeatExchangerDesiccantBalancedFlow': {
        'availability_schedule_name': ['ScheduleNames'],
        'heat_exchanger_performance_name': ['DesiccantHXPerfData'],
    },
    'HeatExchangerFluidToFluid': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'HeatPumpAirToWaterFuelFiredCooling': {
        'air_source_node_name': ['OutdoorAirNodeNames'],
        'companion_heating_heat_pump_name': ['HeatPumpAirToWaterFuelFiredHeatingNames'],
        'normalized_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_energy_input_ratio_function_of_plr_curve_name': ['UnivariateFunctions'],
        'cycling_ratio_factor_curve_name': ['UnivariateFunctions'],
        'auxiliary_electric_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'auxiliary_electric_energy_input_ratio_function_of_plr_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'HeatPumpAirToWaterFuelFiredHeating': {
        'air_source_node_name': ['OutdoorAirNodeNames'],
        'companion_cooling_heat_pump_name': ['HeatPumpAirToWaterFuelFiredCoolingNames'],
        'normalized_capacity_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'fuel_energy_input_ratio_function_of_plr_curve_name': ['UnivariateFunctions'],
        'fuel_energy_input_ratio_defrost_adjustment_curve_name': [
            'UnivariateFunctions'
        ],
        'cycling_ratio_factor_curve_name': ['UnivariateFunctions'],
        'auxiliary_electric_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'auxiliary_electric_energy_input_ratio_function_of_plr_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'HeatPumpPlantLoopEIRCooling': {
        'companion_heat_pump_name': ['PLHPHeatingNames'],
        'capacity_modifier_function_of_temperature_curve_name': ['BivariateFunctions'],
        'electric_input_to_output_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'electric_input_to_output_ratio_modifier_function_of_part_load_ratio_curve_name': [
            'UniVariateFunctions'
        ],
        'minimum_supply_water_temperature_curve_name': ['UniVariateFunctions'],
        'maximum_supply_water_temperature_curve_name': ['UniVariateFunctions'],
        'heat_recovery_capacity_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heat_recovery_electric_input_to_output_ratio_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'thermosiphon_capacity_fraction_curve_name': ['UniVariateFunctions'],
    },
    'HeatPumpPlantLoopEIRHeating': {
        'companion_heat_pump_name': ['PLHPCoolingNames'],
        'capacity_modifier_function_of_temperature_curve_name': ['BivariateFunctions'],
        'electric_input_to_output_ratio_modifier_function_of_temperature_curve_name': [
            'BiVariateFunctions'
        ],
        'electric_input_to_output_ratio_modifier_function_of_part_load_ratio_curve_name': [
            'UnivariateFunctions'
        ],
        'minimum_supply_water_temperature_curve_name': ['UniVariateFunctions'],
        'maximum_supply_water_temperature_curve_name': ['UniVariateFunctions'],
        'dry_outdoor_correction_factor_curve_name': ['UniVariateFunctions'],
        'defrost_energy_input_ratio_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'timed_empirical_defrost_frequency_curve_name': ['UniVariateFunctions'],
        'timed_empirical_defrost_heat_load_penalty_curve_name': [
            'BivariateFunctions',
            'UniVariateFunctions',
        ],
        'timed_empirical_defrost_heat_input_energy_fraction_curve_name': [
            'BivariateFunctions',
            'UniVariateFunctions',
        ],
        'heat_recovery_capacity_modifier_function_of_temperature_curve_name': [
            'BivariateFunctions'
        ],
        'heat_recovery_electric_input_to_output_ratio_modifier_function_of_temperature_curve_name': [
            'BiVariateFunctions'
        ],
    },
    'HeatPumpWaterToWaterEquationFitCooling': {
        'cooling_capacity_curve_name': ['QuadvariateFunctions'],
        'cooling_compressor_power_curve_name': ['QuadvariateFunctions'],
        'companion_heating_heat_pump_name': ['WWHPHeatingNames'],
    },
    'HeatPumpWaterToWaterEquationFitHeating': {
        'heating_capacity_curve_name': ['QuadvariateFunctions'],
        'heating_compressor_power_curve_name': ['QuadvariateFunctions'],
        'companion_cooling_heat_pump_name': ['WWHPCoolingNames'],
    },
    'HotWaterEquipment': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'HumidifierSteamElectric': {
        'availability_schedule_name': ['ScheduleNames'],
        'water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'HumidifierSteamGas': {
        'availability_schedule_name': ['ScheduleNames'],
        'thermal_efficiency_modifier_curve_name': ['UnivariateFunctions'],
        'water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'HybridModelZone': {
        'zone_name': ['ZoneNames'],
        'zone_measured_air_temperature_schedule_name': ['ScheduleNames'],
        'zone_measured_air_humidity_ratio_schedule_name': ['ScheduleNames'],
        'zone_measured_air_co2_concentration_schedule_name': ['ScheduleNames'],
        'zone_input_people_activity_schedule_name': ['ScheduleNames'],
        'zone_input_people_sensible_heat_fraction_schedule_name': ['ScheduleNames'],
        'zone_input_people_radiant_heat_fraction_schedule_name': ['ScheduleNames'],
        'zone_input_people_co2_generation_rate_schedule_name': ['ScheduleNames'],
        'zone_input_supply_air_temperature_schedule_name': ['ScheduleNames'],
        'zone_input_supply_air_mass_flow_rate_schedule_name': ['ScheduleNames'],
        'zone_input_supply_air_humidity_ratio_schedule_name': ['ScheduleNames'],
        'zone_input_supply_air_co2_concentration_schedule_name': ['ScheduleNames'],
    },
    'IndoorLivingWall': {
        'surface_name': ['SurfaceNames'],
        'schedule_name': ['ScheduleNames'],
        'led_intensity_schedule_name': ['ScheduleNames'],
        'led_daylight_targeted_lighting_intensity_schedule_name': ['ScheduleNames'],
    },
    'InternalMass': {
        'construction_name': ['ConstructionNames'],
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'space_or_spacelist_name': ['SpaceAndSpaceListNames'],
    },
    'Lights': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'LoadProfilePlant': {
        'load_schedule_name': ['ScheduleNames'],
        'flow_rate_fraction_schedule_name': ['ScheduleNames'],
    },
    'MaterialPropertyHeatAndMoistureTransferDiffusion': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyHeatAndMoistureTransferRedistribution': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyHeatAndMoistureTransferSettings': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyHeatAndMoistureTransferSorptionIsotherm': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyHeatAndMoistureTransferSuction': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyHeatAndMoistureTransferThermalConductivity': {
        'material_name': ['MaterialName'],
    },
    'MaterialPropertyMoisturePenetrationDepthSettings': {
        'name': ['MaterialName'],
    },
    'MaterialPropertyPhaseChange': {
        'name': ['MaterialName'],
    },
    'MaterialPropertyPhaseChangeHysteresis': {
        'name': ['MaterialName'],
    },
    'MaterialPropertyVariableAbsorptance': {
        'reference_material_name': ['MaterialName'],
    },
    'MaterialPropertyVariableThermalConductivity': {
        'name': ['MaterialName'],
    },
    'OtherEquipment': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'OutdoorAirNode': {
        'drybulb_temperature_schedule_name': ['ScheduleNames'],
        'wetbulb_temperature_schedule_name': ['ScheduleNames'],
        'wind_speed_schedule_name': ['ScheduleNames'],
        'wind_direction_schedule_name': ['ScheduleNames'],
        'wind_pressure_coefficient_curve_name': [
            'UnivariateFunctions',
            'WPCValueNames',
        ],
    },
    'OutputIlluminanceMap': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
    },
    'OutputSurfacesDrawing': {
        'report_specifications_2': ['ColorSchemes'],
    },
    'OutputTableAnnual': {
        'schedule_name': ['ScheduleNames'],
    },
    'OutputTableTimeBins': {
        'schedule_name': ['ScheduleNames'],
    },
    'OutputVariable': {
        'schedule_name': ['ScheduleNames'],
    },
    'People': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'number_of_people_schedule_name': ['ScheduleNames'],
        'activity_level_schedule_name': ['ScheduleNames'],
        'surface_name_angle_factor_list_name': ['AllHeatTranAngFacNames'],
        'work_efficiency_schedule_name': ['ScheduleNames'],
        'clothing_insulation_calculation_method_schedule_name': ['ScheduleNames'],
        'clothing_insulation_schedule_name': ['ScheduleNames'],
        'air_velocity_schedule_name': ['ScheduleNames'],
        'ankle_level_air_velocity_schedule_name': ['ScheduleNames'],
    },
    'PhotovoltaicPerformanceSimple': {
        'efficiency_schedule_name': ['ScheduleNames'],
    },
    'PipeIndoor': {
        'construction_name': ['ConstructionNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_air_velocity_schedule_name': ['ScheduleNames'],
    },
    'PipeOutdoor': {
        'construction_name': ['ConstructionNames'],
    },
    'PipeUnderground': {
        'construction_name': ['ConstructionNames'],
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
    },
    'PipingSystemUndergroundDomain': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
        'name_of_basement_wall_boundary_condition_model': ['OSCMNames'],
        'name_of_basement_floor_boundary_condition_model': ['OSCMNames'],
    },
    'PipingSystemUndergroundDomainPipeCircuitsItem': {
        'pipe_circuit': ['PipingSystemUndergroundCircuitNames'],
    },
    'PipingSystemUndergroundPipeCircuitPipeSegmentsItem': {
        'pipe_segment': ['PipingSystemUndergroundSegmentNames'],
    },
    'PlantComponentTemperatureSource': {
        'source_temperature_schedule_name': ['ScheduleNames'],
    },
    'PlantComponentUserDefined': {
        'main_model_program_calling_manager_name': ['ProgramNames'],
        'plant_connection_1_initialization_program_calling_manager_name': [
            'ProgramNames'
        ],
        'plant_connection_1_simulation_program_calling_manager_name': ['ProgramNames'],
        'plant_connection_2_initialization_program_calling_manager_name': [
            'ProgramNames'
        ],
        'plant_connection_2_simulation_program_calling_manager_name': ['ProgramNames'],
        'plant_connection_3_initialization_program_calling_manager_name': [
            'ProgramNames'
        ],
        'plant_connection_3_simulation_program_calling_manager_name': ['ProgramNames'],
        'plant_connection_4_initialization_program_calling_manager_name': [
            'ProgramNames'
        ],
        'plant_connection_4_simulation_program_calling_manager_name': ['ProgramNames'],
        'supply_inlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'collection_outlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'ambient_zone_name': ['ZoneNames'],
    },
    'PlantEquipmentListEquipmentItem': {
        'equipment_object_type': ['validPlantEquipmentTypes'],
        'equipment_name': ['validPlantEquipmentNames'],
    },
    'PlantEquipmentOperationChillerHeaterChangeover': {
        'zone_load_polling_zonelist_name': ['ZoneListNames'],
        'cooling_only_load_plant_equipment_operation_cooling_load_name': [
            'ControlSchemeList'
        ],
        'heating_only_load_plant_equipment_operation_heating_load_name': [
            'ControlSchemeList'
        ],
        'simultaneous_cooling_and_heating_plant_equipment_operation_cooling_load_name': [
            'ControlSchemeList'
        ],
        'simultaneous_cooling_and_heating_plant_equipment_operation_heating_load_name': [
            'ControlSchemeList'
        ],
        'dedicated_chilled_water_return_recovery_heat_pump_name': ['PLHPCoolingNames'],
        'dedicated_hot_water_return_recovery_heat_pump_name': ['PLHPHeatingNames'],
    },
    'PlantEquipmentOperationCoolingLoad': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationHeatingLoad': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorDewpoint': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorDewpointDifference': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorDryBulb': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorDryBulbDifference': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorRelativeHumidity': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorWetBulb': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationOutdoorWetBulbDifference': {
        'range_1_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_2_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_3_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_4_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_5_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_6_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_7_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_8_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_9_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
        'range_10_equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationSchemes': {
        'control_scheme_1_name': ['ControlSchemeList'],
        'control_scheme_1_schedule_name': ['ScheduleNames'],
        'control_scheme_2_name': ['ControlSchemeList'],
        'control_scheme_2_schedule_name': ['ScheduleNames'],
        'control_scheme_3_name': ['ControlSchemeList'],
        'control_scheme_3_schedule_name': ['ScheduleNames'],
        'control_scheme_4_name': ['ControlSchemeList'],
        'control_scheme_4_schedule_name': ['ScheduleNames'],
        'control_scheme_5_name': ['ControlSchemeList'],
        'control_scheme_5_schedule_name': ['ScheduleNames'],
        'control_scheme_6_name': ['ControlSchemeList'],
        'control_scheme_6_schedule_name': ['ScheduleNames'],
        'control_scheme_7_name': ['ControlSchemeList'],
        'control_scheme_7_schedule_name': ['ScheduleNames'],
        'control_scheme_8_name': ['ControlSchemeList'],
        'control_scheme_8_schedule_name': ['ScheduleNames'],
    },
    'PlantEquipmentOperationThermalEnergyStorage': {
        'on_peak_schedule': ['ScheduleNames'],
        'charging_availability_schedule': ['ScheduleNames'],
        'component_1_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_2_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_3_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_4_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_5_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_6_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_7_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_8_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_9_name': ['Chillers', 'IceThermalStorageEquipment'],
        'component_10_name': ['Chillers', 'IceThermalStorageEquipment'],
    },
    'PlantEquipmentOperationUncontrolled': {
        'equipment_list_name': ['PlantAndCondenserEquipmentLists'],
    },
    'PlantEquipmentOperationUserDefined': {
        'main_model_program_calling_manager_name': ['ProgramNames'],
        'initialization_program_calling_manager_name': ['ProgramNames'],
    },
    'PlantLoop': {
        'user_defined_fluid_type': ['FluidAndGlycolNames'],
        'plant_equipment_operation_scheme_name': ['PlantOperationSchemes'],
        'plant_side_branch_list_name': ['BranchLists'],
        'plant_side_connector_list_name': ['ConnectorLists'],
        'demand_side_branch_list_name': ['BranchLists'],
        'demand_side_connector_list_name': ['ConnectorLists'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
    },
    'PumpConstantSpeed': {
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'pump_curve_name': ['UnivariateFunctions'],
        'zone_name': ['ZoneNames'],
    },
    'PumpVariableSpeed': {
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'pump_curve_name': ['UnivariateFunctions'],
        'pump_rpm_schedule_name': ['ScheduleNames'],
        'minimum_pressure_schedule': ['ScheduleNames'],
        'maximum_pressure_schedule': ['ScheduleNames'],
        'minimum_rpm_schedule': ['ScheduleNames'],
        'maximum_rpm_schedule': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'PumpVariableSpeedCondensate': {
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'RefrigerationAirChiller': {
        'availability_schedule_name': ['ScheduleNames'],
        'capacity_correction_curve_name': [
            'TrivariateFunctions',
            'UnivariateFunctions',
        ],
        'heating_power_schedule_name': ['ScheduleNames'],
        'defrost_schedule_name': ['ScheduleNames'],
        'defrost_drip_down_schedule_name': ['ScheduleNames'],
    },
    'RefrigerationCase': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'latent_case_credit_curve_name': ['UnivariateFunctions'],
        'case_lighting_schedule_name': ['ScheduleNames'],
        'case_defrost_schedule_name': ['ScheduleNames'],
        'case_defrost_drip_down_schedule_name': ['ScheduleNames'],
        'defrost_energy_correction_curve_name': ['UnivariateFunctions'],
        'refrigerated_case_restocking_schedule_name': ['ScheduleNames'],
        'case_credit_fraction_schedule_name': ['ScheduleNames'],
    },
    'RefrigerationCaseAndWalkInListCasesAndWalkinsItem': {
        'case_or_walkin_name': ['RefrigerationCaseAndWalkInNames'],
    },
    'RefrigerationCompressor': {
        'refrigeration_compressor_power_curve_name': ['BivariateFunctions'],
        'refrigeration_compressor_capacity_curve_name': ['BivariateFunctions'],
        'transcritical_compressor_power_curve_name': ['BivariateFunctions'],
        'transcritical_compressor_capacity_curve_name': ['BivariateFunctions'],
    },
    'RefrigerationCompressorListCompressorsItem': {
        'refrigeration_compressor_name': ['RefrigerationCompressorNames'],
    },
    'RefrigerationCompressorRack': {
        'compressor_rack_cop_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'condenser_fan_power_function_of_temperature_curve_name': [
            'UnivariateFunctions'
        ],
        'water_cooled_condenser_outlet_temperature_schedule_name': ['ScheduleNames'],
        'evaporative_condenser_availability_schedule_name': ['ScheduleNames'],
        'evaporative_water_supply_tank_name': ['WaterStorageTankNames'],
        'refrigeration_case_name_or_walkin_name_or_caseandwalkinlist_name': [
            'RefrigerationCaseAndWalkInAndListNames'
        ],
        'heat_rejection_zone_name': ['ZoneNames'],
    },
    'RefrigerationCondenserAirCooled': {
        'rated_effective_total_heat_rejection_rate_curve_name': ['UnivariateFunctions'],
    },
    'RefrigerationCondenserEvaporativeCooled': {
        'evaporative_water_supply_tank_name': ['WaterStorageTankNames'],
        'evaporative_condenser_availability_schedule_name': ['ScheduleNames'],
    },
    'RefrigerationCondenserWaterCooled': {
        'water_outlet_temperature_schedule_name': ['ScheduleNames'],
    },
    'RefrigerationGasCoolerAirCooled': {
        'rated_total_heat_rejection_rate_curve_name': ['UnivariateFunctions'],
    },
    'RefrigerationSecondarySystem': {
        'refrigerated_case_or_walkin_or_caseandwalkinlist_name': [
            'RefrigerationCaseAndWalkInAndListNames'
        ],
        'circulating_fluid_name': ['FluidAndGlycolNames'],
        'variable_speed_pump_cubic_curve_name': ['UnivariateFunctions'],
        'distribution_piping_zone_name': ['ZoneNames'],
        'receiver_separator_zone_name': ['ZoneNames'],
    },
    'RefrigerationSubcooler': {
        'capacity_providing_system': ['RefrigerationSystemNames'],
    },
    'RefrigerationSystem': {
        'refrigerated_case_or_walkin_or_caseandwalkinlist_name': [
            'RefrigerationCaseAndWalkInAndListNames'
        ],
        'refrigeration_transfer_load_or_transferload_list_name': [
            'RefrigerationSecondarySystemAndCascadeCondenserAndTransferLoadListNames'
        ],
        'refrigeration_condenser_name': ['RefrigerationAllTypesCondenserNames'],
        'compressor_or_compressorlist_name': ['RefrigerationCompressorAndListNames'],
        'refrigeration_system_working_fluid_type': ['FluidNames'],
        'mechanical_subcooler_name': ['RefrigerationSubcoolerNames'],
        'liquid_suction_heat_exchanger_subcooler_name': ['RefrigerationSubcoolerNames'],
        'suction_piping_zone_name': ['ZoneNames'],
        'high_stage_compressor_or_compressorlist_name': [
            'RefrigerationCompressorAndListNames'
        ],
    },
    'RefrigerationTranscriticalSystem': {
        'medium_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name': [
            'RefrigerationCaseAndWalkInAndListNames'
        ],
        'low_temperature_refrigerated_case_or_walkin_or_caseandwalkinlist_name': [
            'RefrigerationCaseAndWalkInAndListNames'
        ],
        'refrigeration_gas_cooler_name': ['RefrigerationAllTypesGasCoolerNames'],
        'high_pressure_compressor_or_compressorlist_name': [
            'RefrigerationCompressorAndListNames'
        ],
        'low_pressure_compressor_or_compressorlist_name': [
            'RefrigerationCompressorAndListNames'
        ],
        'refrigeration_system_working_fluid_type': ['FluidNames'],
        'medium_temperature_suction_piping_zone_name': ['ZoneNames'],
        'low_temperature_suction_piping_zone_name': ['ZoneNames'],
    },
    'RefrigerationTransferLoadListTransferLoadsItem': {
        'cascade_condenser_name_or_secondary_system_name': [
            'RefrigerationCascadeCondenserAndSecondarySystemNames'
        ],
    },
    'RefrigerationWalkIn': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_power_schedule_name': ['ScheduleNames'],
        'lighting_schedule_name': ['ScheduleNames'],
        'defrost_schedule_name': ['ScheduleNames'],
        'defrost_drip_down_schedule_name': ['ScheduleNames'],
        'restocking_schedule_name': ['ScheduleNames'],
    },
    'RefrigerationWalkInZoneDataItem': {
        'zone_name': ['ZoneNames'],
        'glass_reach_in_door_opening_schedule_name_facing_zone': ['ScheduleNames'],
        'stocking_door_opening_schedule_name_facing_zone': ['ScheduleNames'],
    },
    'Roof': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'RoofCeilingDetailed': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'RoofIrrigation': {
        'irrigation_rate_schedule_name': ['ScheduleNames'],
    },
    'RoomAirModelType': {
        'zone_name': ['ZoneNames'],
    },
    'RoomAirNode': {
        'zone_name': ['ZoneNames'],
        'surface_1_name': ['AllHeatTranSurfNames'],
        'surface_2_name': ['AllHeatTranSurfNames'],
        'surface_3_name': ['AllHeatTranSurfNames'],
        'surface_4_name': ['AllHeatTranSurfNames'],
        'surface_5_name': ['AllHeatTranSurfNames'],
        'surface_6_name': ['AllHeatTranSurfNames'],
        'surface_7_name': ['AllHeatTranSurfNames'],
        'surface_8_name': ['AllHeatTranSurfNames'],
        'surface_9_name': ['AllHeatTranSurfNames'],
        'surface_10_name': ['AllHeatTranSurfNames'],
        'surface_11_name': ['AllHeatTranSurfNames'],
        'surface_12_name': ['AllHeatTranSurfNames'],
        'surface_13_name': ['AllHeatTranSurfNames'],
        'surface_14_name': ['AllHeatTranSurfNames'],
        'surface_15_name': ['AllHeatTranSurfNames'],
        'surface_16_name': ['AllHeatTranSurfNames'],
        'surface_17_name': ['AllHeatTranSurfNames'],
        'surface_18_name': ['AllHeatTranSurfNames'],
        'surface_19_name': ['AllHeatTranSurfNames'],
        'surface_20_name': ['AllHeatTranSurfNames'],
        'surface_21_name': ['AllHeatTranSurfNames'],
    },
    'RoomAirNodeAirflowNetwork': {
        'zone_name': ['ZoneNames'],
        'roomair_node_airflownetwork_adjacentsurfacelist_name': [
            'RoomAirNodeSurfaceLists'
        ],
        'roomair_node_airflownetwork_internalgains_name': ['RoomAirNodeGains'],
        'roomair_node_airflownetwork_hvacequipment_name': ['RoomAirNodeHVACEquipment'],
    },
    'RoomAirNodeAirflowNetworkAdjacentSurfaceListSurfacesItem': {
        'surface_name': ['AllHeatTranSurfNames'],
    },
    'RoomAirSettingsAirflowNetwork': {
        'zone_name': ['ZoneNames'],
        'control_point_roomairflownetwork_node_name': ['RoomAirflowNetworkNodes'],
    },
    'RoomAirSettingsAirflowNetworkNodesItem': {
        'roomairflownetwork_node_name': ['RoomAirflowNetworkNodes'],
    },
    'RoomAirSettingsCrossVentilation': {
        'zone_name': ['ZoneNames'],
        'gain_distribution_schedule_name': ['ScheduleNames'],
    },
    'RoomAirSettingsOneNodeDisplacementVentilation': {
        'zone_name': ['ZoneNames'],
    },
    'RoomAirSettingsThreeNodeDisplacementVentilation': {
        'zone_name': ['ZoneNames'],
        'gain_distribution_schedule_name': ['ScheduleNames'],
    },
    'RoomAirSettingsUnderFloorAirDistributionExterior': {
        'zone_name': ['ZoneNames'],
    },
    'RoomAirSettingsUnderFloorAirDistributionInterior': {
        'zone_name': ['ZoneNames'],
    },
    'RoomAirTemperaturePatternSurfaceMappingSurfaceDeltasItem': {
        'surface_name_pair': ['AllHeatTranSurfNames'],
    },
    'RoomAirTemperaturePatternUserDefined': {
        'zone_name': ['ZoneNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'pattern_control_schedule_name': ['ScheduleNames'],
    },
    'ScheduleCompact': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleConstant': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleDayHourly': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleDayInterval': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleDayList': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleFile': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleWeekCompactDataItem': {
        'schedule_day_name': ['DayScheduleNames'],
    },
    'ScheduleWeekDaily': {
        'sunday_schedule_day_name': ['DayScheduleNames'],
        'monday_schedule_day_name': ['DayScheduleNames'],
        'tuesday_schedule_day_name': ['DayScheduleNames'],
        'wednesday_schedule_day_name': ['DayScheduleNames'],
        'thursday_schedule_day_name': ['DayScheduleNames'],
        'friday_schedule_day_name': ['DayScheduleNames'],
        'saturday_schedule_day_name': ['DayScheduleNames'],
        'holiday_schedule_day_name': ['DayScheduleNames'],
        'summerdesignday_schedule_day_name': ['DayScheduleNames'],
        'winterdesignday_schedule_day_name': ['DayScheduleNames'],
        'customday1_schedule_day_name': ['DayScheduleNames'],
        'customday2_schedule_day_name': ['DayScheduleNames'],
    },
    'ScheduleYear': {
        'schedule_type_limits_name': ['ScheduleTypeLimitsNames'],
    },
    'ScheduleYearScheduleWeeksItem': {
        'schedule_week_name': ['WeekScheduleNames'],
    },
    'SetpointManagerColdest': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerCondenserEnteringReset': {
        'default_condenser_entering_water_temperature_schedule_name': ['ScheduleNames'],
        'minimum_design_wetbulb_temperature_curve_name': ['QuadvariateFunctions'],
        'minimum_outside_air_wetbulb_temperature_curve_name': ['QuadvariateFunctions'],
        'optimized_cond_entering_water_temperature_curve_name': [
            'QuadvariateFunctions'
        ],
    },
    'SetpointManagerMultiZoneCoolingAverage': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerMultiZoneHeatingAverage': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerMultiZoneHumidityMaximum': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerMultiZoneHumidityMinimum': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerMultiZoneMaximumHumidityAverage': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerMultiZoneMinimumHumidityAverage': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerOutdoorAirReset': {
        'schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerReturnAirBypassFlow': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
        'temperature_setpoint_schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerReturnTemperatureChilledWater': {
        'return_temperature_setpoint_schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerReturnTemperatureHotWater': {
        'return_temperature_setpoint_schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerScheduled': {
        'schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerScheduledDualSetpoint': {
        'high_setpoint_schedule_name': ['ScheduleNames'],
        'low_setpoint_schedule_name': ['ScheduleNames'],
    },
    'SetpointManagerSingleZoneCooling': {
        'control_zone_name': ['ZoneNames'],
    },
    'SetpointManagerSingleZoneHeating': {
        'control_zone_name': ['ZoneNames'],
    },
    'SetpointManagerSingleZoneOneStageCooling': {
        'control_zone_name': ['ZoneNames'],
    },
    'SetpointManagerSingleZoneOneStageHeating': {
        'control_zone_name': ['ZoneNames'],
    },
    'SetpointManagerSingleZoneReheat': {
        'control_zone_name': ['ZoneNames'],
    },
    'SetpointManagerWarmest': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'SetpointManagerWarmestTemperatureFlow': {
        'hvac_air_loop_name': ['AirPrimaryLoops'],
    },
    'ShadingBuildingDetailed': {
        'transmittance_schedule_name': ['ScheduleNames'],
    },
    'ShadingFin': {
        'window_or_door_name': ['SubSurfNames'],
    },
    'ShadingFinProjection': {
        'window_or_door_name': ['SubSurfNames'],
    },
    'ShadingOverhang': {
        'window_or_door_name': ['SubSurfNames'],
    },
    'ShadingOverhangProjection': {
        'window_or_door_name': ['SubSurfNames'],
    },
    'ShadingPropertyReflectance': {
        'shading_surface_name': ['AllShadingSurfNames'],
    },
    'ShadingSiteDetailed': {
        'transmittance_schedule_name': ['ScheduleNames'],
    },
    'ShadingZoneDetailed': {
        'base_surface_name': ['SurfaceNames'],
        'transmittance_schedule_name': ['ScheduleNames'],
    },
    'ShadowCalculationShadingZoneGroupsItem': {
        'shading_zone_group_zonelist_name': ['ZoneListNames'],
    },
    'SiteGroundDomainBasement': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
        'basement_floor_boundary_condition_model_name': ['OSCMNames'],
        'horizontal_insulation_material_name': ['MaterialName'],
        'basement_wall_boundary_condition_model_name': ['OSCMNames'],
        'basement_wall_vertical_insulation_material_name': ['MaterialName'],
    },
    'SiteGroundDomainSlab': {
        'undisturbed_ground_temperature_model_name': ['UndisturbedGroundTempModels'],
        'slab_boundary_condition_model_name': ['OSCMNames'],
        'slab_material_name': ['MaterialName'],
        'horizontal_insulation_material_name': ['MaterialName'],
        'vertical_insulation_material_name': ['MaterialName'],
    },
    'SitePrecipitation': {
        'precipitation_rates_schedule_name': ['ScheduleNames'],
    },
    'SiteSolarAndVisibleSpectrum': {
        'solar_spectrum_data_object_name': ['SpectrumDataNames'],
        'visible_spectrum_data_object_name': ['SpectrumDataNames'],
    },
    'SiteVariableLocation': {
        'building_location_latitude_schedule': ['ScheduleNames'],
        'building_location_longitude_schedule': ['ScheduleNames'],
        'building_location_orientation_schedule': ['ScheduleNames'],
    },
    'SiteWaterMainsTemperature': {
        'temperature_schedule_name': ['ScheduleNames'],
    },
    'SizingPeriodDesignDay': {
        'dry_bulb_temperature_range_modifier_day_schedule_name': ['DayScheduleNames'],
        'humidity_condition_day_schedule_name': ['DayScheduleNames'],
        'beam_solar_day_schedule_name': ['DayScheduleNames'],
        'diffuse_solar_day_schedule_name': ['DayScheduleNames'],
    },
    'SizingPlant': {
        'plant_or_condenser_loop_name': ['PlantLoops'],
    },
    'SizingSystem': {
        'airloop_name': ['AirPrimaryLoops'],
    },
    'SizingZone': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zone_air_distribution_object_name': [
            'DesignSpecificationZoneAirDistributionNames'
        ],
    },
    'SolarCollectorFlatPlatePhotovoltaicThermal': {
        'surface_name': ['AllShadingAndHTSurfNames'],
        'photovoltaic_thermal_model_performance_name': ['FlatPlatePVTParameters'],
        'photovoltaic_name': ['PVGeneratorNames'],
    },
    'SolarCollectorFlatPlateWater': {
        'solarcollectorperformance_name': ['FlatPlateSolarCollectorParameters'],
        'surface_name': ['AllShadingAndHTSurfNames'],
    },
    'SolarCollectorIntegralCollectorStorage': {
        'integralcollectorstorageparameters_name': ['CollectorStoragePerformance'],
        'surface_name': ['AllShadingAndHTSurfNames'],
    },
    'SolarCollectorPerformancePhotovoltaicThermalBIPVT': {
        'boundary_conditions_model_name': ['OSCMNames'],
        'availability_schedule_name': ['ScheduleNames'],
    },
    'SolarCollectorPerformancePhotovoltaicThermalSimple': {
        'thermal_conversion_efficiency_schedule_name': ['ScheduleNames'],
    },
    'SolarCollectorUnglazedTranspired': {
        'boundary_conditions_model_name': ['OSCMNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'free_heating_setpoint_schedule_name': ['ScheduleNames'],
    },
    'SolarCollectorUnglazedTranspiredMultisystem': {
        'solar_collector_name': ['UTSCNames'],
    },
    'SolarCollectorUnglazedTranspiredSurfacesItem': {
        'surface_name': ['AllShadingAndHTSurfNames'],
    },
    'Space': {
        'zone_name': ['ZoneNames'],
    },
    'SpaceHVACEquipmentConnections': {
        'space_name': ['SpaceNames'],
        'space_return_air_node_1_flow_rate_fraction_schedule_name': ['ScheduleNames'],
    },
    'SpaceHVACZoneEquipmentMixer': {
        'zone_name': ['ZoneNames'],
    },
    'SpaceHVACZoneEquipmentMixerSpacesItem': {
        'space_name': ['SpaceNames'],
    },
    'SpaceHVACZoneEquipmentSplitter': {
        'zone_name': ['ZoneNames'],
        'zone_equipment_name': ['ZoneEquipmentNames'],
        'control_space_name': ['SpaceNames'],
    },
    'SpaceHVACZoneEquipmentSplitterSpacesItem': {
        'space_name': ['SpaceNames'],
    },
    'SpaceHVACZoneReturnMixer': {
        'zone_name': ['ZoneNames'],
    },
    'SpaceHVACZoneReturnMixerSpacesItem': {
        'space_name': ['SpaceNames'],
    },
    'SpaceListSpacesItem': {
        'space_name': ['SpaceNames'],
    },
    'SteamEquipment': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion': {
        'surface_name': ['SurfaceNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink': {
        'surface_name': ['SurfaceNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'SurfaceContaminantSourceAndSinkGenericPressureDriven': {
        'surface_name': ['SurfAndSubSurfNames'],
        'generation_schedule_name': ['ScheduleNames'],
    },
    'SurfaceControlMovableInsulation': {
        'surface_name': ['SurfaceNames'],
        'material_name': ['MaterialName'],
        'schedule_name': ['ScheduleNames'],
    },
    'SurfaceConvectionAlgorithmInsideAdaptiveModelSelections': {
        'simple_buoyancy_vertical_wall_user_curve_name': ['UserConvectionInsideModels'],
        'simple_buoyancy_stable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'simple_buoyancy_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'simple_buoyancy_stable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'simple_buoyancy_unstable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'simple_buoyancy_windows_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_heated_floor_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'floor_heat_ceiling_cool_window_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_vertical_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_heated_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_stable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_stable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_unstable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'wall_panel_heating_window_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_vertical_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_stable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_stable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_unstable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'convective_zone_heater_windows_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'central_air_diffuser_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'central_air_diffuser_ceiling_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'central_air_diffuser_floor_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'central_air_diffuser_window_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mechanical_zone_fan_circulation_window_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_stable_floor_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_unstable_floor_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_stable_ceiling_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_unstable_ceiling_equation_user_curve_name': [
            'UserConvectionInsideModels'
        ],
        'mixed_regime_window_equation_user_curve_name': ['UserConvectionInsideModels'],
    },
    'SurfaceConvectionAlgorithmInsideUserCurve': {
        'hc_function_of_temperature_difference_curve_name': ['UnivariateFunctions'],
        'hc_function_of_temperature_difference_divided_by_height_curve_name': [
            'UnivariateFunctions'
        ],
        'hc_function_of_air_change_rate_curve_name': ['UnivariateFunctions'],
        'hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'SurfaceConvectionAlgorithmOutsideAdaptiveModelSelections': {
        'wind_convection_windward_equation_vertical_wall_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
        'wind_convection_leeward_vertical_wall_equation_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
        'wind_convection_horizontal_roof_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
        'natural_convection_vertical_wall_equation_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
        'natural_convection_stable_horizontal_equation_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
        'natural_convection_unstable_horizontal_equation_user_curve_name': [
            'UserConvectionOutsideModels'
        ],
    },
    'SurfaceConvectionAlgorithmOutsideUserCurve': {
        'hf_function_of_wind_speed_curve_name': ['UnivariateFunctions'],
        'hn_function_of_temperature_difference_curve_name': ['UnivariateFunctions'],
        'hn_function_of_temperature_difference_divided_by_height_curve_name': [
            'UnivariateFunctions'
        ],
    },
    'SurfacePropertiesVaporCoefficients': {
        'surface_name': ['SurfaceNames'],
    },
    'SurfacePropertyConvectionCoefficients': {
        'surface_name': ['AllHeatTranSurfNames'],
        'convection_coefficient_1_schedule_name': ['ScheduleNames'],
        'convection_coefficient_1_user_curve_name': ['UserConvectionModels'],
        'convection_coefficient_2_schedule_name': ['ScheduleNames'],
        'convection_coefficient_2_user_curve_name': ['UserConvectionModels'],
    },
    'SurfacePropertyConvectionCoefficientsMultipleSurface': {
        'convection_coefficient_1_schedule_name': ['ScheduleNames'],
        'convection_coefficient_1_user_curve_name': ['UserConvectionModels'],
        'convection_coefficient_2_schedule_name': ['ScheduleNames'],
        'convection_coefficient_2_user_curve_name': ['UserConvectionModels'],
    },
    'SurfacePropertyExposedFoundationPerimeter': {
        'surface_name': ['FloorSurfaceNames'],
    },
    'SurfacePropertyExteriorNaturalVentedCAVity': {
        'boundary_conditions_model_name': ['OSCMNames'],
    },
    'SurfacePropertyExteriorNaturalVentedCAVitySurfaceItem': {
        'surface_name': ['AllShadingAndHTSurfNames'],
    },
    'SurfacePropertyGroundSurfacesGroundSurfacesItem': {
        'ground_surface_temperature_schedule_name': ['ScheduleNames'],
        'ground_surface_reflectance_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertyHeatBalanceSourceTerm': {
        'surface_name': ['SurfaceNames'],
        'inside_face_heat_source_term_schedule_name': ['ScheduleNames'],
        'outside_face_heat_source_term_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertyHeatTransferAlgorithm': {
        'surface_name': ['SurfaceNames'],
    },
    'SurfacePropertyHeatTransferAlgorithmConstruction': {
        'construction_name': ['ConstructionNames'],
    },
    'SurfacePropertyHeatTransferAlgorithmSurfaceListSurfaceItem': {
        'surface_name': ['SurfaceNames'],
    },
    'SurfacePropertyIncidentSolarMultiplier': {
        'surface_name': ['SurfaceNames'],
        'incident_solar_multiplier_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertyLocalEnvironment': {
        'exterior_surface_name': ['SurfaceNames'],
        'sunlit_fraction_schedule_name': ['ScheduleNames'],
        'surrounding_surfaces_object_name': ['SurroundingSurfacesNames'],
        'outdoor_air_node_name': ['OutdoorAirNodeNames'],
        'ground_surfaces_object_name': ['GroundSurfacesNames'],
    },
    'SurfacePropertyOtherSideCoefficients': {
        'constant_temperature_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertySolarIncidentInside': {
        'surface_name': ['SurfaceNames'],
        'construction_name': ['ConstructionNames'],
        'inside_surface_incident_sun_solar_radiation_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertySurroundingSurfaces': {
        'sky_temperature_schedule_name': ['ScheduleNames'],
        'ground_temperature_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertySurroundingSurfacesSurfacesItem': {
        'surrounding_surface_temperature_schedule_name': ['ScheduleNames'],
    },
    'SurfacePropertyUnderwater': {
        'free_stream_water_temperature_schedule': ['ScheduleNames'],
        'free_stream_water_velocity_schedule': ['ScheduleNames'],
    },
    'SwimmingPoolIndoor': {
        'surface_name': ['FloorSurfaceNames'],
        'activity_factor_schedule_name': ['ScheduleNames'],
        'make_up_water_supply_schedule_name': ['ScheduleNames'],
        'cover_schedule_name': ['ScheduleNames'],
        'setpoint_temperature_schedule': ['ScheduleNames'],
        'people_schedule': ['ScheduleNames'],
        'people_heat_gain_schedule': ['ScheduleNames'],
    },
    'TableIndependentVariableListIndependentVariablesItem': {
        'independent_variable_name': ['IndependentVariableName'],
    },
    'TableLookup': {
        'independent_variable_list_name': ['IndependentVariableListName'],
    },
    'ThermalStorageChilledWaterMixed': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
        'use_side_availability_schedule_name': ['ScheduleNames'],
        'source_side_availability_schedule_name': ['ScheduleNames'],
    },
    'ThermalStorageChilledWaterStratified': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
        'use_side_availability_schedule_name': ['ScheduleNames'],
        'source_side_availability_schedule_name': ['ScheduleNames'],
    },
    'ThermalStorageIceDetailed': {
        'availability_schedule_name': ['ScheduleNames'],
        'discharging_curve_name': ['BivariateFunctions'],
        'charging_curve_name': ['BivariateFunctions'],
    },
    'ThermostatSetpointDualSetpoint': {
        'heating_setpoint_temperature_schedule_name': ['ScheduleNames'],
        'cooling_setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointSingleCooling': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointSingleHeating': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointSingleHeatingOrCooling': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointThermalComfortFangerDualSetpoint': {
        'fanger_thermal_comfort_heating_schedule_name': ['ScheduleNames'],
        'fanger_thermal_comfort_cooling_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointThermalComfortFangerSingleCooling': {
        'fanger_thermal_comfort_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointThermalComfortFangerSingleHeating': {
        'fanger_thermal_comfort_schedule_name': ['ScheduleNames'],
    },
    'ThermostatSetpointThermalComfortFangerSingleHeatingOrCooling': {
        'fanger_thermal_comfort_schedule_name': ['ScheduleNames'],
    },
    'UtilityCostChargeBlock': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'UtilityCostChargeSimple': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'UtilityCostComputation': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'UtilityCostQualify': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'UtilityCostRatchet': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'UtilityCostTariff': {
        'time_of_use_period_schedule_name': ['ScheduleNames'],
        'season_schedule_name': ['ScheduleNames'],
        'month_schedule_name': ['ScheduleNames'],
        'real_time_pricing_charge_schedule_name': ['ScheduleNames'],
        'customer_baseline_load_schedule_name': ['ScheduleNames'],
    },
    'UtilityCostVariable': {
        'tariff_name': ['UtilityCostTariffs'],
    },
    'WallAdiabatic': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'WallDetailed': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'WallExterior': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'WallInterzone': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'WallUnderground': {
        'construction_name': ['ConstructionNames'],
        'zone_name': ['ZoneNames'],
        'space_name': ['SpaceNames'],
    },
    'WaterHeaterHeatPumpPumpedCondenser': {
        'availability_schedule_name': ['ScheduleNames'],
        'compressor_setpoint_temperature_schedule_name': ['ScheduleNames'],
        'inlet_air_temperature_schedule_name': ['ScheduleNames'],
        'inlet_air_humidity_schedule_name': ['ScheduleNames'],
        'inlet_air_zone_name': ['ZoneNames'],
        'tank_name': ['WaterHeaterNames'],
        'dx_coil_name': [
            'HeatPumpWaterHeaterDXCoilsPumped',
            'HeatPumpWaterHeaterDXCoilsVariableSpeed',
            'IntegratedHeatPumps',
        ],
        'compressor_ambient_temperature_schedule_name': ['ScheduleNames'],
        'fan_name': ['FansOnOff', 'FansSystemModel'],
        'inlet_air_mixer_schedule_name': ['ScheduleNames'],
    },
    'WaterHeaterHeatPumpWrappedCondenser': {
        'availability_schedule_name': ['ScheduleNames'],
        'compressor_setpoint_temperature_schedule_name': ['ScheduleNames'],
        'inlet_air_temperature_schedule_name': ['ScheduleNames'],
        'inlet_air_humidity_schedule_name': ['ScheduleNames'],
        'inlet_air_zone_name': ['ZoneNames'],
        'tank_name': ['WaterHeaterStratifiedNames'],
        'dx_coil_name': ['HeatPumpWaterHeaterDXCoilsWrapped'],
        'compressor_ambient_temperature_schedule_name': ['ScheduleNames'],
        'fan_name': ['FansOnOff', 'FansSystemModel'],
        'inlet_air_mixer_schedule_name': ['ScheduleNames'],
    },
    'WaterHeaterMixed': {
        'setpoint_temperature_schedule_name': ['ScheduleNames'],
        'part_load_factor_curve_name': ['UnivariateFunctions'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
        'use_flow_rate_fraction_schedule_name': ['ScheduleNames'],
        'cold_water_supply_temperature_schedule_name': ['ScheduleNames'],
        'indirect_alternate_setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'WaterHeaterSizing': {
        'waterheater_name': ['WaterHeaterNames'],
    },
    'WaterHeaterStratified': {
        'heater_1_setpoint_temperature_schedule_name': ['ScheduleNames'],
        'heater_2_setpoint_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_zone_name': ['ZoneNames'],
        'use_flow_rate_fraction_schedule_name': ['ScheduleNames'],
        'cold_water_supply_temperature_schedule_name': ['ScheduleNames'],
        'indirect_alternate_setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'WaterUseConnections': {
        'supply_water_storage_tank_name': ['WaterStorageTankNames'],
        'reclamation_water_storage_tank_name': ['WaterStorageTankNames'],
        'hot_water_supply_temperature_schedule_name': ['ScheduleNames'],
        'cold_water_supply_temperature_schedule_name': ['ScheduleNames'],
    },
    'WaterUseConnectionsConnectionsItem': {
        'water_use_equipment_name': ['WaterUseEquipmentNames'],
    },
    'WaterUseEquipment': {
        'flow_rate_fraction_schedule_name': ['ScheduleNames'],
        'target_temperature_schedule_name': ['ScheduleNames'],
        'hot_water_supply_temperature_schedule_name': ['ScheduleNames'],
        'cold_water_supply_temperature_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'sensible_fraction_schedule_name': ['ScheduleNames'],
        'latent_fraction_schedule_name': ['ScheduleNames'],
    },
    'WaterUseRainCollector': {
        'storage_tank_name': ['WaterStorageTankNames'],
        'collection_loss_factor_schedule_name': ['ScheduleNames'],
    },
    'WaterUseRainCollectorSurfacesItem': {
        'collection_surface_name': ['AllShadingAndHTSurfNames'],
    },
    'WaterUseStorage': {
        'overflow_destination': ['WaterStorageTankNames'],
        'other_tank_name': ['WaterStorageTankNames'],
        'water_temperature_schedule_name': ['ScheduleNames'],
        'ambient_temperature_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'tank_outside_surface_material_name': ['MaterialName'],
    },
    'WaterUseWell': {
        'storage_tank_name': ['WaterStorageTankNames'],
        'water_table_depth_schedule_name': ['ScheduleNames'],
    },
    'WeatherPropertySkyTemperature': {
        'name': ['RunPeriodsAndDesignDays'],
        'schedule_name': ['DayScheduleNames', 'ScheduleNames'],
    },
    'Window': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'frame_and_divider_name': ['WindowFrameAndDividerNames'],
    },
    'WindowInterzone': {
        'construction_name': ['ConstructionNames'],
        'building_surface_name': ['SurfaceNames'],
        'outside_boundary_condition_object': ['OutFaceEnvNames'],
    },
    'WindowMaterialGap': {
        'gas_or_gas_mixture': ['WindowGasAndGasMixtures'],
        'deflection_state': ['WindowGapDeflectionStates'],
        'support_pillar': ['WindowGapSupportPillars'],
    },
    'WindowMaterialGlazing': {
        'window_glass_spectral_data_set_name': ['SpectralDataSets'],
        'window_glass_spectral_and_incident_angle_transmittance_data_set_table_name': [
            'BivariateFunctions'
        ],
        'window_glass_spectral_and_incident_angle_front_reflectance_data_set_table_name': [
            'BivariateFunctions'
        ],
        'window_glass_spectral_and_incident_angle_back_reflectance_data_set_table_name': [
            'BivariateFunctions'
        ],
    },
    'WindowMaterialGlazingEquivalentLayer': {
        'window_glass_spectral_data_set_name': ['SpectralDataSets'],
    },
    'WindowMaterialGlazingGroupThermochromicTemperatureDataItem': {
        'window_material_glazing_name': ['GlazingMaterialName'],
    },
    'WindowPropertyAirflowControl': {
        'name': ['SubSurfNames'],
        'airflow_multiplier_schedule_name': ['ScheduleNames'],
    },
    'WindowPropertyStormWindow': {
        'window_name': ['SubSurfNames'],
        'storm_glass_layer_name': ['GlazingMaterialName'],
    },
    'WindowShadingControl': {
        'zone_name': ['ZoneNames'],
        'construction_with_shading_name': ['ConstructionNames'],
        'schedule_name': ['ScheduleNames'],
        'shading_device_material_name': ['WindowShadesScreensAndBlinds'],
        'slat_angle_schedule_name': ['ScheduleNames'],
        'daylighting_control_object_name': ['DaylightingControlNames'],
    },
    'WindowShadingControlFenestrationSurfacesItem': {
        'fenestration_surface_name': ['GlazedExtSubSurfNames'],
    },
    'ZoneAirBalanceOutdoorAir': {
        'zone_name': ['ZoneNames'],
        'induced_outdoor_air_schedule_name': ['ScheduleNames'],
    },
    'ZoneAirContaminantBalance': {
        'outdoor_carbon_dioxide_schedule_name': ['ScheduleNames'],
        'outdoor_generic_contaminant_schedule_name': ['ScheduleNames'],
    },
    'ZoneBaseboardOutdoorTemperatureControlled': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneCapacitanceMultiplierResearchSpecial': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
    },
    'ZoneContaminantSourceAndSinkCarbonDioxide': {
        'zone_name': ['ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneContaminantSourceAndSinkGenericConstant': {
        'zone_name': ['ZoneNames'],
        'generation_schedule_name': ['ScheduleNames'],
        'removal_schedule_name': ['ScheduleNames'],
    },
    'ZoneContaminantSourceAndSinkGenericCutoffModel': {
        'zone_name': ['ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneContaminantSourceAndSinkGenericDecaySource': {
        'zone_name': ['ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneContaminantSourceAndSinkGenericDepositionRateSink': {
        'zone_name': ['ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneControlContaminantController': {
        'zone_name': ['ZoneNames'],
        'carbon_dioxide_control_availability_schedule_name': ['ScheduleNames'],
        'carbon_dioxide_setpoint_schedule_name': ['ScheduleNames'],
        'minimum_carbon_dioxide_concentration_schedule_name': ['ScheduleNames'],
        'maximum_carbon_dioxide_concentration_schedule_name': ['ScheduleNames'],
        'generic_contaminant_control_availability_schedule_name': ['ScheduleNames'],
        'generic_contaminant_setpoint_schedule_name': ['ScheduleNames'],
    },
    'ZoneControlHumidistat': {
        'zone_name': ['ZoneNames'],
        'humidifying_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
        'dehumidifying_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
    },
    'ZoneControlThermostat': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'control_type_schedule_name': ['ScheduleNames'],
        'control_1_name': ['ControlTypeNames'],
        'control_2_name': ['ControlTypeNames'],
        'control_3_name': ['ControlTypeNames'],
        'control_4_name': ['ControlTypeNames'],
    },
    'ZoneControlThermostatOperativeTemperature': {
        'thermostat_name': ['ZoneControlThermostaticNames'],
        'radiative_fraction_schedule_name': ['ScheduleNames'],
    },
    'ZoneControlThermostatStagedDualSetpoint': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'heating_temperature_setpoint_schedule_name': ['ScheduleNames'],
        'cooling_temperature_setpoint_base_schedule_name': ['ScheduleNames'],
    },
    'ZoneControlThermostatTemperatureAndHumidity': {
        'thermostat_name': ['ZoneControlThermostaticNames'],
        'dehumidifying_relative_humidity_setpoint_schedule_name': ['ScheduleNames'],
        'overcool_range_schedule_name': ['ScheduleNames'],
    },
    'ZoneControlThermostatThermalComfort': {
        'zone_or_zonelist_name': ['ZoneAndZoneListNames'],
        'specific_people_name': ['PeopleNames'],
        'thermal_comfort_control_type_schedule_name': ['ScheduleNames'],
        'thermal_comfort_control_1_name': ['ThermalComfortControlTypeNames'],
        'thermal_comfort_control_2_name': ['ThermalComfortControlTypeNames'],
        'thermal_comfort_control_3_name': ['ThermalComfortControlTypeNames'],
        'thermal_comfort_control_4_name': ['ThermalComfortControlTypeNames'],
    },
    'ZoneCoolTowerShower': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'water_supply_storage_tank_name': ['WaterStorageTankNames'],
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
    },
    'ZoneCrossMixing': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'schedule_name': ['ScheduleNames'],
        'source_zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'delta_temperature_schedule_name': ['ScheduleNames'],
        'minimum_receiving_temperature_schedule_name': ['ScheduleNames'],
        'maximum_receiving_temperature_schedule_name': ['ScheduleNames'],
        'minimum_source_temperature_schedule_name': ['ScheduleNames'],
        'maximum_source_temperature_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneEarthtube': {
        'zone_name': ['ZoneNames'],
        'schedule_name': ['ScheduleNames'],
        'earth_tube_model_parameters': ['EarthTubeParameterNames'],
    },
    'ZoneGroup': {
        'zone_list_name': ['ZoneListNames'],
    },
    'ZoneHVACAirDistributionUnit': {
        'air_terminal_name': ['AirTerminalUnitNames'],
        'design_specification_air_terminal_sizing_object_name': [
            'DesignSpecificationAirTerminalSizingName'
        ],
    },
    'ZoneHVACBaseboardConvectiveElectric': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACBaseboardConvectiveWater': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACBaseboardRadiantConvectiveElectric': {
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem': {
        'surface_name': ['AllHeatTranSurfNames'],
    },
    'ZoneHVACBaseboardRadiantConvectiveSteam': {
        'design_object': ['RadiantDesignObject'],
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACBaseboardRadiantConvectiveWater': {
        'design_object': ['BaseboardDesignObject'],
        'availability_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACCoolingPanelRadiantConvectiveWater': {
        'availability_schedule_name': ['ScheduleNames'],
        'cooling_control_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACDehumidifierDX': {
        'availability_schedule_name': ['ScheduleNames'],
        'water_removal_curve_name': ['BivariateFunctions'],
        'energy_factor_curve_name': ['BivariateFunctions'],
        'part_load_fraction_correlation_curve_name': ['UnivariateFunctions'],
        'condensate_collection_water_storage_tank_name': ['WaterStorageTankNames'],
    },
    'ZoneHVACEnergyRecoveryVentilator': {
        'availability_schedule_name': ['ScheduleNames'],
        'heat_exchanger_name': ['HXAirToAirSensibleAndLatentNames'],
        'supply_air_fan_name': ['FansOnOff', 'FansSystemModel'],
        'exhaust_air_fan_name': ['FansOnOff', 'FansSystemModel'],
        'controller_name': ['ControllerStandAloneEnergyRecoveryVentilator'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
    },
    'ZoneHVACEnergyRecoveryVentilatorController': {
        'electronic_enthalpy_limit_curve_name': ['UnivariateFunctions'],
        'time_of_day_economizer_flow_control_schedule_name': ['ScheduleNames'],
        'humidistat_control_zone_name': ['ZoneNames'],
    },
    'ZoneHVACEquipmentConnections': {
        'zone_name': ['ZoneNames'],
        'zone_conditioning_equipment_list_name': ['ZoneEquipmentLists'],
        'zone_return_air_node_1_flow_rate_fraction_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACEquipmentListEquipmentItem': {
        'zone_equipment_name': ['ZoneEquipmentNames'],
        'zone_equipment_sequential_cooling_fraction_schedule_name': ['ScheduleNames'],
        'zone_equipment_sequential_heating_fraction_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACEvaporativeCoolerUnit': {
        'availability_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'supply_air_fan_name': ['Fans'],
        'first_evaporative_cooler_object_name': ['EvapCoolerNames'],
        'second_evaporative_cooler_name': ['EvapCoolerNames'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACExhaustControl': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'exhaust_flow_fraction_schedule_name': ['ScheduleNames'],
        'minimum_zone_temperature_limit_schedule_name': ['ScheduleNames'],
        'minimum_exhaust_flow_fraction_schedule_name': ['ScheduleNames'],
        'balanced_exhaust_fraction_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACForcedAirUserDefined': {
        'overall_model_simulation_program_calling_manager_name': ['ProgramNames'],
        'model_setup_and_sizing_program_calling_manager_name': ['ProgramNames'],
        'supply_inlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'collection_outlet_water_storage_tank_name': ['WaterStorageTankNames'],
        'ambient_zone_name': ['ZoneNames'],
    },
    'ZoneHVACFourPipeFanCoil': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
        'cooling_coil_name': ['CoolingCoilsWater'],
        'heating_coil_name': ['HeatingCoilsElectric', 'HeatingCoilsWater'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACHighTemperatureRadiant': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'heating_setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACHybridUnitaryHVAC': {
        'availability_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'minimum_supply_air_temperature_schedule_name': ['ScheduleNames'],
        'maximum_supply_air_temperature_schedule_name': ['ScheduleNames'],
        'minimum_supply_air_humidity_ratio_schedule_name': ['ScheduleNames'],
        'maximum_supply_air_humidity_ratio_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'mode_0_supply_air_temperature_lookup_table_name': ['MultivariateFunctions'],
        'mode_0_supply_air_humidity_ratio_lookup_table_name': ['MultivariateFunctions'],
        'mode_0_system_electric_power_lookup_table_name': ['MultivariateFunctions'],
        'mode_0_supply_fan_electric_power_lookup_table_name': ['MultivariateFunctions'],
        'mode_0_external_static_pressure_lookup_table_name': ['MultivariateFunctions'],
        'mode_0_system_second_fuel_consumption_lookup_table_name': [
            'MultivariateFunctions'
        ],
        'mode_0_system_third_fuel_consumption_lookup_table_name': [
            'MultivariateFunctions'
        ],
        'mode_0_system_water_use_lookup_table_name': ['MultivariateFunctions'],
    },
    'ZoneHVACHybridUnitaryHVACModesItem': {
        'mode_supply_air_temperature_lookup_table_name': ['MultivariateFunctions'],
        'mode_supply_air_humidity_ratio_lookup_table_name': ['MultivariateFunctions'],
        'mode_system_electric_power_lookup_table_name': ['MultivariateFunctions'],
        'mode_supply_fan_electric_power_lookup_table_name': ['MultivariateFunctions'],
        'mode_external_static_pressure_lookup_table_name': ['MultivariateFunctions'],
        'mode_system_second_fuel_consumption_lookup_table_name': [
            'MultivariateFunctions'
        ],
        'mode_system_third_fuel_consumption_lookup_table_name': [
            'MultivariateFunctions'
        ],
        'mode_system_water_use_lookup_table_name': ['MultivariateFunctions'],
    },
    'ZoneHVACIdealLoadsAirSystem': {
        'availability_schedule_name': ['ScheduleNames'],
        'heating_availability_schedule_name': ['ScheduleNames'],
        'cooling_availability_schedule_name': ['ScheduleNames'],
        'design_specification_outdoor_air_object_name': [
            'DSOASpaceListNames',
            'DesignSpecificationOutdoorAirNames',
        ],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACLowTemperatureRadiantConstantFlow': {
        'design_object': ['RadiantDesignObject'],
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'surface_name_or_radiant_surface_group_name': [
            'RadiantGroupNames',
            'RadiantSurfaceNames',
        ],
        'pump_flow_rate_schedule_name': ['ScheduleNames'],
        'heating_high_water_temperature_schedule_name': ['ScheduleNames'],
        'heating_low_water_temperature_schedule_name': ['ScheduleNames'],
        'heating_high_control_temperature_schedule_name': ['ScheduleNames'],
        'heating_low_control_temperature_schedule_name': ['ScheduleNames'],
        'cooling_high_water_temperature_schedule_name': ['ScheduleNames'],
        'cooling_low_water_temperature_schedule_name': ['ScheduleNames'],
        'cooling_high_control_temperature_schedule_name': ['ScheduleNames'],
        'cooling_low_control_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACLowTemperatureRadiantConstantFlowDesign': {
        'changeover_delay_time_period_schedule': ['ScheduleNames'],
    },
    'ZoneHVACLowTemperatureRadiantElectric': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'surface_name_or_radiant_surface_group_name': [
            'RadiantGroupNames',
            'RadiantSurfaceNames',
        ],
        'heating_setpoint_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneHVACLowTemperatureRadiantSurfaceGroupSurfaceFractionsItem': {
        'surface_name': ['RadiantSurfaceNames'],
    },
    'ZoneHVACLowTemperatureRadiantVariableFlow': {
        'design_object': ['RadiantDesignObject'],
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'surface_name_or_radiant_surface_group_name': [
            'RadiantGroupNames',
            'RadiantSurfaceNames',
        ],
    },
    'ZoneHVACLowTemperatureRadiantVariableFlowDesign': {
        'heating_control_temperature_schedule_name': ['ScheduleNames'],
        'cooling_control_temperature_schedule_name': ['ScheduleNames'],
        'changeover_delay_time_period_schedule': ['ScheduleNames'],
    },
    'ZoneHVACOutdoorAirUnit': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'outdoor_air_schedule_name': ['ScheduleNames'],
        'supply_fan_name': ['FansCVandVAV', 'FansSystemModel'],
        'exhaust_fan_name': ['FansCVandVAV', 'FansSystemModel'],
        'exhaust_air_schedule_name': ['ScheduleNames'],
        'high_air_control_temperature_schedule_name': ['ScheduleNames'],
        'low_air_control_temperature_schedule_name': ['ScheduleNames'],
        'outdoor_air_unit_list_name': ['OutdoorAirUnitEquipmentLists'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
    },
    'ZoneHVACPackagedTerminalAirConditioner': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansCVandOnOff', 'FansSystemModel'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': [
            'CoilCoolingDX',
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACPackagedTerminalHeatPump': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansCVandOnOff', 'FansSystemModel'],
        'heating_coil_name': [
            'HeatingCoilsDXSingleSpeed',
            'HeatingCoilsDXVariableSpeed',
        ],
        'cooling_coil_name': [
            'CoilCoolingDX',
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACRefrigerationChillerSet': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
    },
    'ZoneHVACRefrigerationChillerSetChillersItem': {
        'air_chiller_name': ['RefrigerationAirChillerNames'],
    },
    'ZoneHVACTerminalUnitVariableRefrigerantFlow': {
        'terminal_unit_availability_schedule': ['ScheduleNames'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'supply_air_fan_object_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
        'outside_air_mixer_object_name': ['OutdoorAirMixers'],
        'cooling_coil_object_name': [
            'CoolingCoilsDXVarRefrigFlow',
            'CoolingCoilsDXVarRefrigFlowFluidTemperatureControl',
        ],
        'heating_coil_object_name': [
            'HeatingCoilsDXVarRefrigFlow',
            'HeatingCoilsDXVarRefrigFlowFluidTemperatureControl',
        ],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
        'controlling_zone_or_thermostat_location': ['ZoneNames'],
        'design_specification_multispeed_object_name': [
            'UnitarySystemPerformanceNames'
        ],
    },
    'ZoneHVACUnitHeater': {
        'availability_schedule_name': ['ScheduleNames'],
        'supply_air_fan_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
        'heating_coil_name': ['HeatingCoilName'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACUnitVentilator': {
        'availability_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_air_fraction_or_temperature_schedule_name': ['ScheduleNames'],
        'supply_air_fan_name': ['FansCVandOnOffandVAV', 'FansSystemModel'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': ['CoolingCoilsWater'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACVentilatedSlab': {
        'availability_schedule_name': ['ScheduleNames'],
        'zone_name': ['ZoneNames'],
        'surface_name_or_radiant_surface_group_name': [
            'RadiantSurfaceNames',
            'VentSlabGroupNames',
        ],
        'minimum_outdoor_air_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_air_fraction_or_temperature_schedule_name': ['ScheduleNames'],
        'heating_high_air_temperature_schedule_name': ['ScheduleNames'],
        'heating_low_air_temperature_schedule_name': ['ScheduleNames'],
        'heating_high_control_temperature_schedule_name': ['ScheduleNames'],
        'heating_low_control_temperature_schedule_name': ['ScheduleNames'],
        'cooling_high_air_temperature_schedule_name': ['ScheduleNames'],
        'cooling_low_air_temperature_schedule_name': ['ScheduleNames'],
        'cooling_high_control_temperature_schedule_name': ['ScheduleNames'],
        'cooling_low_control_temperature_schedule_name': ['ScheduleNames'],
        'fan_name': ['FansCV', 'FansSystemModel'],
        'heating_coil_name': ['HeatingCoilName'],
        'cooling_coil_name': ['CoolingCoilsWater'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneHVACVentilatedSlabSlabGroupDataItem': {
        'zone_name': ['ZoneNames'],
        'surface_name': ['RadiantSurfaceNames'],
    },
    'ZoneHVACWaterToAirHeatPump': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansOnOff', 'FansSystemModel'],
        'heating_coil_name': ['HeatingCoilsWaterToAirHP', 'HeatingCoilsWaterToAirVSHP'],
        'cooling_coil_name': ['CoolingCoilsWaterToAirHP', 'CoolingCoilsWaterToAirVSHP'],
        'supplemental_heating_coil_name': ['HeatingCoilName'],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
        'design_specification_multispeed_object_name': [
            'UnitarySystemPerformanceNames'
        ],
    },
    'ZoneHVACWindowAirConditioner': {
        'availability_schedule_name': ['ScheduleNames'],
        'outdoor_air_mixer_name': ['OutdoorAirMixers'],
        'supply_air_fan_name': ['FansCVandOnOff', 'FansSystemModel'],
        'dx_cooling_coil_name': [
            'CoolingCoilsDXSingleSpeed',
            'CoolingCoilsDXVariableSpeed',
        ],
        'supply_air_fan_operating_mode_schedule_name': ['ScheduleNames'],
        'availability_manager_list_name': ['SystemAvailabilityManagerLists'],
        'design_specification_zonehvac_sizing_object_name': [
            'DesignSpecificationZoneHVACSizingName'
        ],
    },
    'ZoneInfiltrationDesignFlowRate': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneInfiltrationEffectiveLeakageArea': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneInfiltrationFlowCoefficient': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneListZonesItem': {
        'zone_name': ['ZoneNames'],
    },
    'ZoneMixing': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'schedule_name': ['ScheduleNames'],
        'source_zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'delta_temperature_schedule_name': ['ScheduleNames'],
        'minimum_receiving_temperature_schedule_name': ['ScheduleNames'],
        'maximum_receiving_temperature_schedule_name': ['ScheduleNames'],
        'minimum_source_temperature_schedule_name': ['ScheduleNames'],
        'maximum_source_temperature_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZonePropertyLocalEnvironment': {
        'zone_name': ['ZoneNames'],
        'outdoor_air_node_name': ['OutdoorAirNodeNames'],
    },
    'ZonePropertyUserViewFactorsBySurfaceName': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceListNames',
            'SpaceNames',
            'ZoneListNames',
            'ZoneNames',
        ],
    },
    'ZonePropertyUserViewFactorsBySurfaceNameViewFactorsItem': {
        'from_surface': ['AllHeatTranSurfNames'],
        'to_surface': ['AllHeatTranSurfNames'],
    },
    'ZoneRefrigerationDoorMixing': {
        'zone_or_space_name_1': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_2': ['SpaceNames', 'ZoneNames'],
        'schedule_name': ['ScheduleNames'],
    },
    'ZoneTerminalUnitListTerminalUnitsItem': {
        'zone_terminal_unit_name': ['ZoneTerminalUnitNames'],
    },
    'ZoneThermalChimney': {
        'zone_name': ['ZoneNames'],
        'availability_schedule_name': ['ScheduleNames'],
        'zone_or_space_name_1': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_2': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_3': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_4': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_5': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_6': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_7': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_8': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_9': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_10': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_11': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_12': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_13': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_14': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_15': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_16': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_17': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_18': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_19': ['SpaceNames', 'ZoneNames'],
        'zone_or_space_name_20': ['SpaceNames', 'ZoneNames'],
    },
    'ZoneVentilationDesignFlowRate': {
        'zone_or_zonelist_or_space_or_spacelist_name': [
            'SpaceAndSpaceListNames',
            'ZoneAndZoneListNames',
        ],
        'schedule_name': ['ScheduleNames'],
        'minimum_indoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_indoor_temperature_schedule_name': ['ScheduleNames'],
        'delta_temperature_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_temperature_schedule_name': ['ScheduleNames'],
    },
    'ZoneVentilationWindandStackOpenArea': {
        'zone_or_space_name': ['SpaceNames', 'ZoneNames'],
        'opening_area_fraction_schedule_name': ['ScheduleNames'],
        'minimum_indoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_indoor_temperature_schedule_name': ['ScheduleNames'],
        'delta_temperature_schedule_name': ['ScheduleNames'],
        'minimum_outdoor_temperature_schedule_name': ['ScheduleNames'],
        'maximum_outdoor_temperature_schedule_name': ['ScheduleNames'],
    },
}


REF_CLASS_NAME_TYPES: dict[str, frozenset[str]] = {
    'validBranchEquipmentTypes': frozenset(
        {
            'AIRCONDITIONER:VARIABLEREFRIGERANTFLOW',
            'AIRLOOPHVAC:OUTDOORAIRSYSTEM',
            'AIRLOOPHVAC:UNITARY:FURNACE:HEATCOOL',
            'AIRLOOPHVAC:UNITARY:FURNACE:HEATONLY',
            'AIRLOOPHVAC:UNITARYHEATCOOL',
            'AIRLOOPHVAC:UNITARYHEATCOOL:VAVCHANGEOVERBYPASS',
            'AIRLOOPHVAC:UNITARYHEATONLY',
            'AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR',
            'AIRLOOPHVAC:UNITARYHEATPUMP:AIRTOAIR:MULTISPEED',
            'AIRLOOPHVAC:UNITARYHEATPUMP:WATERTOAIR',
            'AIRLOOPHVAC:UNITARYSYSTEM',
            'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:COOLEDBEAM',
            'AIRTERMINAL:SINGLEDUCT:CONSTANTVOLUME:FOURPIPEBEAM',
            'AIRTERMINAL:SINGLEDUCT:USERDEFINED',
            'BOILER:HOTWATER',
            'BOILER:STEAM',
            'CENTRALHEATPUMPSYSTEM',
            'CHILLER:ABSORPTION',
            'CHILLER:ABSORPTION:INDIRECT',
            'CHILLER:COMBUSTIONTURBINE',
            'CHILLER:CONSTANTCOP',
            'CHILLER:ELECTRIC',
            'CHILLER:ELECTRIC:ASHRAE205',
            'CHILLER:ELECTRIC:EIR',
            'CHILLER:ELECTRIC:REFORMULATEDEIR',
            'CHILLER:ENGINEDRIVEN',
            'CHILLERHEATER:ABSORPTION:DIRECTFIRED',
            'CHILLERHEATER:ABSORPTION:DOUBLEEFFECT',
            'COIL:COOLING:DX:SINGLESPEED:THERMALSTORAGE',
            'COIL:COOLING:WATER',
            'COIL:COOLING:WATER:DETAILEDGEOMETRY',
            'COIL:COOLING:WATERTOAIRHEATPUMP:EQUATIONFIT',
            'COIL:COOLING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION',
            'COIL:COOLING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT',
            'COIL:HEATING:DESUPERHEATER',
            'COIL:HEATING:ELECTRIC',
            'COIL:HEATING:FUEL',
            'COIL:HEATING:STEAM',
            'COIL:HEATING:WATER',
            'COIL:HEATING:WATERTOAIRHEATPUMP:EQUATIONFIT',
            'COIL:HEATING:WATERTOAIRHEATPUMP:PARAMETERESTIMATION',
            'COIL:HEATING:WATERTOAIRHEATPUMP:VARIABLESPEEDEQUATIONFIT',
            'COIL:USERDEFINED',
            'COILSYSTEM:COOLING:DX',
            'COILSYSTEM:COOLING:WATER',
            'COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED',
            'COILSYSTEM:HEATING:DX',
            'COOLINGTOWER:SINGLESPEED',
            'COOLINGTOWER:TWOSPEED',
            'COOLINGTOWER:VARIABLESPEED',
            'COOLINGTOWER:VARIABLESPEED:MERKEL',
            'DEHUMIDIFIER:DESICCANT:NOFANS',
            'DEHUMIDIFIER:DESICCANT:SYSTEM',
            'DISTRICTCOOLING',
            'DISTRICTHEATING:STEAM',
            'DISTRICTHEATING:WATER',
            'DUCT',
            'EVAPORATIVECOOLER:DIRECT:CELDEKPAD',
            'EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL',
            'EVAPORATIVECOOLER:INDIRECT:CELDEKPAD',
            'EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL',
            'EVAPORATIVECOOLER:INDIRECT:WETCOIL',
            'EVAPORATIVEFLUIDCOOLER:SINGLESPEED',
            'EVAPORATIVEFLUIDCOOLER:TWOSPEED',
            'FAN:COMPONENTMODEL',
            'FAN:CONSTANTVOLUME',
            'FAN:SYSTEMMODEL',
            'FAN:VARIABLEVOLUME',
            'FLUIDCOOLER:SINGLESPEED',
            'FLUIDCOOLER:TWOSPEED',
            'GENERATOR:COMBUSTIONTURBINE',
            'GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER',
            'GENERATOR:FUELCELL:STACKCOOLER',
            'GENERATOR:INTERNALCOMBUSTIONENGINE',
            'GENERATOR:MICROCHP',
            'GENERATOR:MICROTURBINE',
            'GROUNDHEATEXCHANGER:HORIZONTALTRENCH',
            'GROUNDHEATEXCHANGER:POND',
            'GROUNDHEATEXCHANGER:SLINKY',
            'GROUNDHEATEXCHANGER:SURFACE',
            'GROUNDHEATEXCHANGER:SYSTEM',
            'HEADEREDPUMPS:CONSTANTSPEED',
            'HEADEREDPUMPS:VARIABLESPEED',
            'HEATEXCHANGER:AIRTOAIR:FLATPLATE',
            'HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT',
            'HEATEXCHANGER:DESICCANT:BALANCEDFLOW',
            'HEATEXCHANGER:FLUIDTOFLUID',
            'HEATPUMP:PLANTLOOP:EIR:COOLING',
            'HEATPUMP:PLANTLOOP:EIR:HEATING',
            'HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING',
            'HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING',
            'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING',
            'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING',
            'HUMIDIFIER:STEAM:ELECTRIC',
            'HUMIDIFIER:STEAM:GAS',
            'LOADPROFILE:PLANT',
            'PIPE:ADIABATIC',
            'PIPE:ADIABATIC:STEAM',
            'PIPE:INDOOR',
            'PIPE:OUTDOOR',
            'PIPE:UNDERGROUND',
            'PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT',
            'PLANTCOMPONENT:TEMPERATURESOURCE',
            'PLANTCOMPONENT:USERDEFINED',
            'PUMP:CONSTANTSPEED',
            'PUMP:VARIABLESPEED',
            'PUMP:VARIABLESPEED:CONDENSATE',
            'REFRIGERATION:COMPRESSORRACK',
            'REFRIGERATION:CONDENSER:WATERCOOLED',
            'SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL',
            'SOLARCOLLECTOR:FLATPLATE:WATER',
            'SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE',
            'SWIMMINGPOOL:INDOOR',
            'TEMPERINGVALVE',
            'THERMALSTORAGE:CHILLEDWATER:MIXED',
            'THERMALSTORAGE:CHILLEDWATER:STRATIFIED',
            'THERMALSTORAGE:ICE:DETAILED',
            'THERMALSTORAGE:ICE:SIMPLE',
            'WATERHEATER:HEATPUMP:PUMPEDCONDENSER',
            'WATERHEATER:HEATPUMP:WRAPPEDCONDENSER',
            'WATERHEATER:MIXED',
            'WATERHEATER:STRATIFIED',
            'WATERUSE:CONNECTIONS',
            'ZONEHVAC:BASEBOARD:CONVECTIVE:WATER',
            'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM',
            'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:STEAM:DESIGN',
            'ZONEHVAC:BASEBOARD:RADIANTCONVECTIVE:WATER',
            'ZONEHVAC:COOLINGPANEL:RADIANTCONVECTIVE:WATER',
            'ZONEHVAC:FORCEDAIR:USERDEFINED',
            'ZONEHVAC:LOWTEMPERATURERADIANT:CONSTANTFLOW',
            'ZONEHVAC:LOWTEMPERATURERADIANT:VARIABLEFLOW',
            'ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW',
        }
    ),
    'validCondenserEquipmentTypes': frozenset(
        {
            'COOLINGTOWER:SINGLESPEED',
            'COOLINGTOWER:TWOSPEED',
            'COOLINGTOWER:VARIABLESPEED',
            'COOLINGTOWER:VARIABLESPEED:MERKEL',
            'DISTRICTCOOLING',
            'DISTRICTHEATING:STEAM',
            'DISTRICTHEATING:WATER',
            'EVAPORATIVEFLUIDCOOLER:SINGLESPEED',
            'EVAPORATIVEFLUIDCOOLER:TWOSPEED',
            'FLUIDCOOLER:SINGLESPEED',
            'FLUIDCOOLER:TWOSPEED',
            'GENERATOR:MICROTURBINE',
            'GROUNDHEATEXCHANGER:HORIZONTALTRENCH',
            'GROUNDHEATEXCHANGER:POND',
            'GROUNDHEATEXCHANGER:SLINKY',
            'GROUNDHEATEXCHANGER:SURFACE',
            'GROUNDHEATEXCHANGER:SYSTEM',
            'HEATEXCHANGER:FLUIDTOFLUID',
            'PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT',
            'PLANTCOMPONENT:TEMPERATURESOURCE',
            'PLANTCOMPONENT:USERDEFINED',
            'TEMPERINGVALVE',
            'THERMALSTORAGE:CHILLEDWATER:MIXED',
            'THERMALSTORAGE:CHILLEDWATER:STRATIFIED',
            'WATERHEATER:MIXED',
            'WATERHEATER:STRATIFIED',
        }
    ),
    'validOASysEquipmentTypes': frozenset(
        {
            'AIRLOOPHVAC:UNITARYSYSTEM',
            'COIL:COOLING:WATER',
            'COIL:COOLING:WATER:DETAILEDGEOMETRY',
            'COIL:HEATING:ELECTRIC',
            'COIL:HEATING:FUEL',
            'COIL:HEATING:STEAM',
            'COIL:HEATING:WATER',
            'COIL:USERDEFINED',
            'COILSYSTEM:COOLING:DX',
            'COILSYSTEM:COOLING:WATER',
            'COILSYSTEM:COOLING:WATER:HEATEXCHANGERASSISTED',
            'COILSYSTEM:HEATING:DX',
            'DEHUMIDIFIER:DESICCANT:NOFANS',
            'DEHUMIDIFIER:DESICCANT:SYSTEM',
            'EVAPORATIVECOOLER:DIRECT:CELDEKPAD',
            'EVAPORATIVECOOLER:DIRECT:RESEARCHSPECIAL',
            'EVAPORATIVECOOLER:INDIRECT:CELDEKPAD',
            'EVAPORATIVECOOLER:INDIRECT:RESEARCHSPECIAL',
            'EVAPORATIVECOOLER:INDIRECT:WETCOIL',
            'FAN:COMPONENTMODEL',
            'FAN:CONSTANTVOLUME',
            'FAN:SYSTEMMODEL',
            'FAN:VARIABLEVOLUME',
            'HEATEXCHANGER:AIRTOAIR:FLATPLATE',
            'HEATEXCHANGER:AIRTOAIR:SENSIBLEANDLATENT',
            'HEATEXCHANGER:DESICCANT:BALANCEDFLOW',
            'HUMIDIFIER:STEAM:ELECTRIC',
            'HUMIDIFIER:STEAM:GAS',
            'OUTDOORAIR:MIXER',
            'SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL',
            'SOLARCOLLECTOR:UNGLAZEDTRANSPIRED',
            'ZONEHVAC:TERMINALUNIT:VARIABLEREFRIGERANTFLOW',
        }
    ),
    'validPlantEquipmentTypes': frozenset(
        {
            'BOILER:HOTWATER',
            'BOILER:STEAM',
            'CENTRALHEATPUMPSYSTEM',
            'CHILLER:ABSORPTION',
            'CHILLER:ABSORPTION:INDIRECT',
            'CHILLER:COMBUSTIONTURBINE',
            'CHILLER:CONSTANTCOP',
            'CHILLER:ELECTRIC',
            'CHILLER:ELECTRIC:ASHRAE205',
            'CHILLER:ELECTRIC:EIR',
            'CHILLER:ELECTRIC:REFORMULATEDEIR',
            'CHILLER:ENGINEDRIVEN',
            'CHILLERHEATER:ABSORPTION:DIRECTFIRED',
            'CHILLERHEATER:ABSORPTION:DOUBLEEFFECT',
            'COOLINGTOWER:SINGLESPEED',
            'COOLINGTOWER:TWOSPEED',
            'COOLINGTOWER:VARIABLESPEED',
            'COOLINGTOWER:VARIABLESPEED:MERKEL',
            'DISTRICTCOOLING',
            'DISTRICTHEATING:STEAM',
            'DISTRICTHEATING:WATER',
            'EVAPORATIVEFLUIDCOOLER:SINGLESPEED',
            'EVAPORATIVEFLUIDCOOLER:TWOSPEED',
            'FLUIDCOOLER:SINGLESPEED',
            'FLUIDCOOLER:TWOSPEED',
            'GENERATOR:FUELCELL:EXHAUSTGASTOWATERHEATEXCHANGER',
            'GENERATOR:MICROCHP',
            'GENERATOR:MICROTURBINE',
            'GROUNDHEATEXCHANGER:HORIZONTALTRENCH',
            'GROUNDHEATEXCHANGER:POND',
            'GROUNDHEATEXCHANGER:SLINKY',
            'GROUNDHEATEXCHANGER:SURFACE',
            'GROUNDHEATEXCHANGER:SYSTEM',
            'HEATEXCHANGER:FLUIDTOFLUID',
            'HEATPUMP:PLANTLOOP:EIR:COOLING',
            'HEATPUMP:PLANTLOOP:EIR:HEATING',
            'HEATPUMP:WATERTOWATER:EQUATIONFIT:COOLING',
            'HEATPUMP:WATERTOWATER:EQUATIONFIT:HEATING',
            'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:COOLING',
            'HEATPUMP:WATERTOWATER:PARAMETERESTIMATION:HEATING',
            'PIPINGSYSTEM:UNDERGROUND:PIPECIRCUIT',
            'PLANTCOMPONENT:TEMPERATURESOURCE',
            'PLANTCOMPONENT:USERDEFINED',
            'SOLARCOLLECTOR:FLATPLATE:PHOTOVOLTAICTHERMAL',
            'SOLARCOLLECTOR:FLATPLATE:WATER',
            'SOLARCOLLECTOR:INTEGRALCOLLECTORSTORAGE',
            'TEMPERINGVALVE',
            'THERMALSTORAGE:CHILLEDWATER:MIXED',
            'THERMALSTORAGE:CHILLEDWATER:STRATIFIED',
            'THERMALSTORAGE:ICE:DETAILED',
            'WATERHEATER:HEATPUMP:PUMPEDCONDENSER',
            'WATERHEATER:HEATPUMP:WRAPPEDCONDENSER',
            'WATERHEATER:MIXED',
            'WATERHEATER:STRATIFIED',
        }
    ),
}
