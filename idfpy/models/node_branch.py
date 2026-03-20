"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Node-Branch Management
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BranchesRef,
    ConstructionNamesRef,
    OSCMNamesRef,
    PipingSystemUndergroundCircuitNamesRef,
    PipingSystemUndergroundSegmentNamesRef,
    PlantConnectorsRef,
    ScheduleNamesRef,
    UndisturbedGroundTempModelsRef,
    UnivariateFunctionsRef,
    ValidBranchEquipmentNamesRef,
    ValidBranchEquipmentTypesRef,
    WPCValueNamesRef,
    ZoneNamesRef,
)


class BranchComponentsItem(IDFBaseModel):
    """Nested object type for array items."""
    component_object_type: ValidBranchEquipmentTypesRef = Field(..., json_schema_extra={'object_list': ['validBranchEquipmentTypes']})
    component_name: ValidBranchEquipmentNamesRef = Field(..., json_schema_extra={'object_list': ['validBranchEquipmentNames']})
    component_inlet_node_name: str = Field(...)
    component_outlet_node_name: str = Field(...)


class BranchListBranchesItem(IDFBaseModel):
    """Nested object type for array items."""
    branch_name: BranchesRef = Field(..., json_schema_extra={'object_list': ['Branches']})


class ConnectorMixerBranchesItem(IDFBaseModel):
    """Nested object type for array items."""
    inlet_branch_name: BranchesRef = Field(..., json_schema_extra={'object_list': ['Branches']})


class ConnectorSplitterBranchesItem(IDFBaseModel):
    """Nested object type for array items."""
    outlet_branch_name: BranchesRef = Field(..., json_schema_extra={'object_list': ['Branches']})


class NodeListNodesItem(IDFBaseModel):
    """Nested object type for array items."""
    node_name: str = Field(...)


class OutdoorAirNodeListNodesItem(IDFBaseModel):
    """Nested object type for array items."""
    node_or_nodelist_name: str = Field(...)


class PipingSystemUndergroundDomainPipeCircuitsItem(IDFBaseModel):
    """Nested object type for array items."""
    pipe_circuit: PipingSystemUndergroundCircuitNamesRef = Field(..., json_schema_extra={'object_list': ['PipingSystemUndergroundCircuitNames'], 'note': 'Name of a pipe circuit to be simulated in this domain'})


class PipingSystemUndergroundPipeCircuitPipeSegmentsItem(IDFBaseModel):
    """Nested object type for array items."""
    pipe_segment: PipingSystemUndergroundSegmentNamesRef = Field(..., json_schema_extra={'object_list': ['PipingSystemUndergroundSegmentNames'], 'note': 'Name of a pipe segment to be included in this pipe circuit'})



class Branch(IDFBaseModel):
    """List components on the branch in simulation and connection order Note: this
should NOT include splitters or mixers which define endpoints of branches"""

    _idf_object_type: ClassVar[str] = "Branch"
    name: str = Field(...)
    pressure_drop_curve_name: UnivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions'], 'note': 'Optional field to include this branch in plant pressure drop calculations This field is only relevant for branches in PlantLoops and CondenserLoops Air loops do not account for pressure drop using ...'})
    components: list[BranchComponentsItem] | None = Field(default=None)


class BranchList(IDFBaseModel):
    """Branches MUST be listed in Flow order: Inlet branch, then parallel branches,
then Outlet branch. Branches are simulated in the order listed. Branch names
cannot be duplicated within a single branch list."""

    _idf_object_type: ClassVar[str] = "BranchList"
    name: str = Field(...)
    branches: list[BranchListBranchesItem] | None = Field(default=None)


class ConnectorList(IDFBaseModel):
    """only two connectors allowed per loop if two entered, one must be
Connector:Splitter and one must be Connector:Mixer"""

    _idf_object_type: ClassVar[str] = "ConnectorList"
    name: str = Field(...)
    connector_1_object_type: Literal['Connector:Mixer', 'Connector:Splitter'] = Field(...)
    connector_1_name: PlantConnectorsRef = Field(..., json_schema_extra={'object_list': ['PlantConnectors']})
    connector_2_object_type: Literal['Connector:Mixer', 'Connector:Splitter'] | None = Field(default=None)
    connector_2_name: PlantConnectorsRef | None = Field(default=None, json_schema_extra={'object_list': ['PlantConnectors']})


class ConnectorMixer(IDFBaseModel):
    """Mix N inlet air/water streams into one. Branch names cannot be duplicated
within a single mixer list."""

    _idf_object_type: ClassVar[str] = "Connector:Mixer"
    name: str = Field(...)
    outlet_branch_name: BranchesRef = Field(..., json_schema_extra={'object_list': ['Branches']})
    branches: list[ConnectorMixerBranchesItem] | None = Field(default=None)


class ConnectorSplitter(IDFBaseModel):
    """Split one air/water stream into N outlet streams. Branch names cannot be
duplicated within a single Splitter list."""

    _idf_object_type: ClassVar[str] = "Connector:Splitter"
    name: str = Field(...)
    inlet_branch_name: BranchesRef = Field(..., json_schema_extra={'object_list': ['Branches']})
    branches: list[ConnectorSplitterBranchesItem] | None = Field(default=None)


class Duct(IDFBaseModel):
    """Passes inlet node state variables to outlet node state variables"""

    _idf_object_type: ClassVar[str] = "Duct"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)


class NodeList(IDFBaseModel):
    """This object is used in places where lists of nodes may be needed, e.g.
ZoneHVAC:EquipmentConnections field Zone Air Inlet Node or NodeList Name"""

    _idf_object_type: ClassVar[str] = "NodeList"
    name: str = Field(...)
    nodes: list[NodeListNodesItem] | None = Field(default=None)


class OutdoorAirNode(IDFBaseModel):
    """This object sets the temperature and humidity conditions for an outdoor air
node. It allows the height above ground to be specified. This object may be
used more than once. The same node name may not appear in both an
OutdoorAir:Node object and an OutdoorAir:NodeList object. This object
defines local outdoor air environmental conditions."""

    _idf_object_type: ClassVar[str] = "OutdoorAir:Node"
    name: str = Field(...)
    height_above_ground: float | None = Field(default=-1.0, json_schema_extra={'units': 'm', 'note': 'A value less than zero indicates that the height will be ignored and the weather file conditions will be used.'})
    drybulb_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values are real numbers, -100.0 to 100.0, units C'})
    wetbulb_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values are real numbers, -100.0 to 100.0, units C'})
    wind_speed_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values are real numbers, 0.0 to 40.0, units m/s'})
    wind_direction_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Schedule values are real numbers, 0.0 to 360.0, units degree'})
    wind_pressure_coefficient_curve_name: (UnivariateFunctionsRef | WPCValueNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['UnivariateFunctions', 'WPCValueNames'], 'note': 'The name of the AirflowNetwork:MultiZone:WindPressureCoefficientValues, curve, or table object specifying the wind pressure coefficient.'})
    symmetric_wind_pressure_coefficient_curve: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'Specify whether the pressure curve is symmetric or not. Specify Yes for curves that should be evaluated from 0 to 180 degrees Specify No for curves that should be evaluated from 0 to 360 degrees'})
    wind_angle_type: Literal['', 'Absolute', 'Relative'] | None = Field(default='Absolute', json_schema_extra={'note': 'Specify whether the angle used to compute the wind pressure coefficient is absolute or relative Specify Relative to compute the angle between the wind direction and the surface azimuth Specify Abso...'})


class OutdoorAirNodeList(IDFBaseModel):
    """This object sets the temperature and humidity conditions for an outdoor air
node using the weather data values. to vary outdoor air node conditions with
height above ground use OutdoorAir:Node instead of this object. This object
may be used more than once. The same node name may not appear in both an
OutdoorAir:Node object and an OutdoorAir:NodeList object."""

    _idf_object_type: ClassVar[str] = "OutdoorAir:NodeList"
    nodes: list[OutdoorAirNodeListNodesItem] | None = Field(default=None)


class PipeAdiabatic(IDFBaseModel):
    """Passes Inlet Node state variables to Outlet Node state variables"""

    _idf_object_type: ClassVar[str] = "Pipe:Adiabatic"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)


class PipeAdiabaticSteam(IDFBaseModel):
    """Passes Inlet Node state variables to Outlet Node state variables"""

    _idf_object_type: ClassVar[str] = "Pipe:Adiabatic:Steam"
    name: str = Field(...)
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)


class PipeIndoor(IDFBaseModel):
    """Pipe model with transport delay and heat transfer to the environment."""

    _idf_object_type: ClassVar[str] = "Pipe:Indoor"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})
    fluid_inlet_node_name: str = Field(...)
    fluid_outlet_node_name: str = Field(...)
    environment_type: Literal['', 'Schedule', 'Zone'] | None = Field(default='Zone')
    ambient_temperature_zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames']})
    ambient_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    ambient_air_velocity_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    pipe_inside_diameter: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_length: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})


class PipeOutdoor(IDFBaseModel):
    """Pipe model with transport delay and heat transfer to the environment."""

    _idf_object_type: ClassVar[str] = "Pipe:Outdoor"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})
    fluid_inlet_node_name: str = Field(...)
    fluid_outlet_node_name: str = Field(...)
    ambient_temperature_outdoor_air_node_name: str | None = Field(default=None)
    pipe_inside_diameter: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    pipe_length: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})


class PipeUnderground(IDFBaseModel):
    """Buried Pipe model: For pipes buried at a depth less than one meter, this is
an alternative object to: HeatExchanger:Surface"""

    _idf_object_type: ClassVar[str] = "Pipe:Underground"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames']})
    fluid_inlet_node_name: str = Field(...)
    fluid_outlet_node_name: str = Field(...)
    sun_exposure: Literal['NoSun', 'SunExposed'] = Field(...)
    pipe_inside_diameter: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm', 'note': 'pipe thickness is defined in the Construction object'})
    pipe_length: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'm'})
    soil_material_name: str = Field(...)
    undisturbed_ground_temperature_model_type: Literal['Site:GroundTemperature:Undisturbed:FiniteDifference', 'Site:GroundTemperature:Undisturbed:KusudaAchenbach', 'Site:GroundTemperature:Undisturbed:Xing'] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']})


class PipingSystemUndergroundDomain(IDFBaseModel):
    """The ground domain object for underground piping system simulation."""

    _idf_object_type: ClassVar[str] = "PipingSystem:Underground:Domain"
    name: str = Field(...)
    xmax: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': "Domain extent in the local 'X' direction"})
    ymax: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': "Domain extent in the local 'Y' direction"})
    zmax: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': "Domain extent in the local 'Y' direction"})
    x_direction_mesh_density_parameter: int | None = Field(default=4, gt=0, json_schema_extra={'note': 'If mesh type is symmetric geometric, this should be an even number.'})
    x_direction_mesh_type: Literal['SymmetricGeometric', 'Uniform'] = Field(...)
    x_direction_geometric_coefficient: float | None = Field(default=1.3, ge=1.0, le=2.0, json_schema_extra={'note': 'optional Only used if mesh type is symmetric geometric'})
    y_direction_mesh_density_parameter: int | None = Field(default=4, gt=0, json_schema_extra={'note': 'If mesh type is symmetric geometric, this should be an even number.'})
    y_direction_mesh_type: Literal['SymmetricGeometric', 'Uniform'] = Field(...)
    y_direction_geometric_coefficient: float | None = Field(default=1.3, ge=1.0, le=2.0, json_schema_extra={'note': 'optional Only used if mesh type is symmetric geometric'})
    z_direction_mesh_density_parameter: int | None = Field(default=4, gt=0, json_schema_extra={'note': 'If mesh type is symmetric geometric, this should be an even number.'})
    z_direction_mesh_type: Literal['SymmetricGeometric', 'Uniform'] = Field(...)
    z_direction_geometric_coefficient: float | None = Field(default=1.3, ge=1.0, le=2.0, json_schema_extra={'note': 'optional Only used if mesh type is symmetric geometric'})
    soil_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    soil_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    soil_specific_heat: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/kg-K', 'note': 'This is a dry soil property, which is adjusted for freezing effects by the simulation algorithm.'})
    soil_moisture_content_volume_fraction: float | None = Field(default=30.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    soil_moisture_content_volume_fraction_at_saturation: float | None = Field(default=50.0, ge=0.0, le=100.0, json_schema_extra={'units': 'percent'})
    undisturbed_ground_temperature_model_type: Literal['Site:GroundTemperature:Undisturbed:FiniteDifference', 'Site:GroundTemperature:Undisturbed:KusudaAchenbach', 'Site:GroundTemperature:Undisturbed:Xing'] = Field(...)
    undisturbed_ground_temperature_model_name: UndisturbedGroundTempModelsRef = Field(..., json_schema_extra={'object_list': ['UndisturbedGroundTempModels']})
    this_domain_includes_basement_surface_interaction: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'if Yes, then the following basement inputs are used if No, then the following basement inputs are *ignored*'})
    width_of_basement_floor_in_ground_domain: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Required only if Domain Has Basement Interaction'})
    depth_of_basement_wall_in_ground_domain: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Required only if Domain Has Basement Interaction'})
    shift_pipe_x_coordinates_by_basement_width: Literal['No', 'Yes'] | None = Field(default=None, json_schema_extra={'note': 'Required only if Domain Has Basement Interaction'})
    name_of_basement_wall_boundary_condition_model: OSCMNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OSCMNames'], 'note': 'Required only if Domain Has Basement Interaction'})
    name_of_basement_floor_boundary_condition_model: OSCMNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OSCMNames'], 'note': 'Required only if Domain Has Basement Interaction'})
    convergence_criterion_for_the_outer_cartesian_domain_iteration_loop: float | None = Field(default=0.001, ge=1e-06, le=0.5, json_schema_extra={'units': 'deltaC'})
    maximum_iterations_in_the_outer_cartesian_domain_iteration_loop: int | None = Field(default=500, ge=3, le=10000)
    evapotranspiration_ground_cover_parameter: float | None = Field(default=0.4, ge=0.0, le=1.5, json_schema_extra={'note': 'This specifies the ground cover effects during evapotranspiration calculations. The value roughly represents the following cases: = 0   : concrete or other solid, non-permeable ground surface mater...'})
    number_of_pipe_circuits_entered_for_this_domain: int = Field(..., ge=1)
    pipe_circuits: list[PipingSystemUndergroundDomainPipeCircuitsItem] | None = Field(default=None)


class PipingSystemUndergroundPipeCircuit(IDFBaseModel):
    """The pipe circuit object in an underground piping system. This object is
simulated within an underground piping domain object and connected on a
branch on a plant loop."""

    _idf_object_type: ClassVar[str] = "PipingSystem:Underground:PipeCircuit"
    name: str = Field(...)
    pipe_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    pipe_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    pipe_specific_heat: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/kg-K'})
    pipe_inner_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    pipe_outer_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    design_flow_rate: float = Field(..., gt=0.0, json_schema_extra={'units': 'm3/s'})
    circuit_inlet_node: str = Field(...)
    circuit_outlet_node: str = Field(...)
    convergence_criterion_for_the_inner_radial_iteration_loop: float | None = Field(default=0.001, ge=1e-06, le=0.5, json_schema_extra={'units': 'deltaC'})
    maximum_iterations_in_the_inner_radial_iteration_loop: int | None = Field(default=500, ge=3, le=10000)
    number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region: int | None = Field(default=3, ge=1, le=15)
    radial_thickness_of_inner_radial_near_pipe_mesh_region: float = Field(..., gt=0.0, json_schema_extra={'note': 'Required because it must be selected by user instead of being inferred from circuit/domain object inputs.'})
    number_of_pipe_segments_entered_for_this_pipe_circuit: int = Field(..., ge=1)
    pipe_segments: list[PipingSystemUndergroundPipeCircuitPipeSegmentsItem] | None = Field(default=None)


class PipingSystemUndergroundPipeSegment(IDFBaseModel):
    """The pipe segment to be used in an underground piping system This object
represents a single pipe leg positioned axially in the local z-direction, at
a given x, y location in the domain"""

    _idf_object_type: ClassVar[str] = "PipingSystem:Underground:PipeSegment"
    name: str = Field(...)
    x_position: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'This segment will be centered at this distance from the x=0 domain surface or the basement wall surface, based on whether a basement exists in this domain and the selection of the shift input field...'})
    y_position: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'This segment will be centered at this distance away from the ground surface; thus this value represents the burial depth of this pipe segment.'})
    flow_direction: Literal['DecreasingZ', 'IncreasingZ'] = Field(..., json_schema_extra={'note': 'This segment will be simulated such that the flow is in the selected direction. This can allow for detailed analysis of circuiting effects in a single domain.'})

