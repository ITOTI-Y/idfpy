"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Thermal Zones and Surfaces
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllShadingSurfNamesRef,
    ComplexFenestrationStatesRef,
    ConstructionNamesRef,
    DaylightingControlNamesRef,
    GlazedExtSubSurfNamesRef,
    GlazingMaterialNameRef,
    OutFaceEnvNamesRef,
    ScheduleNamesRef,
    SpaceAndSpaceListNamesRef,
    SpaceNamesRef,
    SubSurfNamesRef,
    SurfaceNamesRef,
    WindowFrameAndDividerNamesRef,
    WindowShadesScreensAndBlindsRef,
    ZoneAndZoneListNamesRef,
    ZoneListNamesRef,
    ZoneNamesRef,
)


class BuildingSurfaceDetailedVerticesItem(IDFBaseModel):
    """Nested object type for array items."""
    vertex_x_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_y_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_z_coordinate: float = Field(..., json_schema_extra={'units': 'm'})


class SpaceTagsItem(IDFBaseModel):
    """Nested object type for array items."""
    tag: str | None = Field(default=None, json_schema_extra={'note': 'Optional reporting tag'})


class SpaceListSpacesItem(IDFBaseModel):
    """Nested object type for array items."""
    space_name: SpaceNamesRef = Field(..., json_schema_extra={'object_list': ['SpaceNames']})


class WindowShadingControlFenestrationSurfacesItem(IDFBaseModel):
    """Nested object type for array items."""
    fenestration_surface_name: GlazedExtSubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['GlazedExtSubSurfNames'], 'note': 'When Multiple Surface Control Type is set to Sequential the shades will be deployed for the referenced surface objects in order. When that field is set to Group the entire list is controlled simult...'})


class ZoneListZonesItem(IDFBaseModel):
    """Nested object type for array items."""
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})



class BuildingSurfaceDetailed(IDFBaseModel):
    """Allows for detailed entry of building heat transfer surfaces. Does not
include subsurfaces such as windows or doors."""

    _idf_object_type: ClassVar[str] = "BuildingSurface:Detailed"
    name: str = Field(...)
    surface_type: Literal['Ceiling', 'Floor', 'Roof', 'Wall'] = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    outside_boundary_condition: Literal['Adiabatic', 'Foundation', 'Ground', 'GroundBasementPreprocessorAverageFloor', 'GroundBasementPreprocessorAverageWall', 'GroundBasementPreprocessorLowerWall', 'GroundBasementPreprocessorUpperWall', 'GroundFCfactorMethod', 'GroundSlabPreprocessorAverage', 'GroundSlabPreprocessorCore', 'GroundSlabPreprocessorPerimeter', 'OtherSideCoefficients', 'OtherSideConditionsModel', 'Outdoors', 'Space', 'Surface', 'Zone'] = Field(...)
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Non-blank only if the field Outside Boundary Condition is Surface, Zone, Space, OtherSideCoefficients or OtherSideConditionsModel If Surface, specify name of corresponding surface in adjacent zone ...'})
    sun_exposure: Literal['', 'NoSun', 'SunExposed'] | None = Field(default='SunExposed')
    wind_exposure: Literal['', 'NoWind', 'WindExposed'] | None = Field(default='WindExposed')
    view_factor_to_ground: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'From the exterior of the surface Unused if one uses the "reflections" options in Solar Distribution in Building input unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been s...'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 120 vertex coordinates -- extensible object "extensible" -- duplicate last set of x,y,z coordinates (last 3 fields), remembering to remove ; from "inner" fields. for clarity in any error...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class CeilingAdiabatic(IDFBaseModel):
    """Allows for simplified entry of interior ceilings."""

    _idf_object_type: ClassVar[str] = "Ceiling:Adiabatic"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of Ceiling'})
    tilt_angle: float | None = Field(default=0.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Ceilings are usually tilted 0 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'If not Flat, Starting coordinate is the Lower Left Corner of the Ceiling'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class CeilingInterzone(IDFBaseModel):
    """Allows for simplified entry of ceilings using adjacent zone (interzone) heat
transfer - adjacent surface should be a floor"""

    _idf_object_type: ClassVar[str] = "Ceiling:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    outside_boundary_condition_object: OutFaceEnvNamesRef = Field(..., json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior floors Specify a zone name of an adjacent zone to automatically generate the interior floor in the adjacent zone.'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of wall (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=0.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Ceilings are usually tilted 0 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'If not Flat, should be Lower Left Corner (from outside)'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class Door(IDFBaseModel):
    """Allows for simplified entry of opaque Doors."""

    _idf_object_type: ClassVar[str] = "Door"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Door is on (i.e., Base Surface) Door assumes the azimuth and tilt angles of the surface it is on.'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Door starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class DoorInterzone(IDFBaseModel):
    """Allows for simplified entry of interzone (opaque interior) doors (adjacent
to other zones)."""

    _idf_object_type: ClassVar[str] = "Door:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Door is on (i.e., Base Surface) Door assumes the azimuth and tilt angles of the surface it is on.'})
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior doors. Specify a zone name of an adjacent zone to automatically generate the interior door in the adjacent zone. a blank field will set...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Door starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class FenestrationSurfaceDetailed(IDFBaseModel):
    """Allows for detailed entry of subsurfaces (windows, doors, glass doors,
tubular daylighting devices)."""

    _idf_object_type: ClassVar[str] = "FenestrationSurface:Detailed"
    name: str = Field(...)
    surface_type: Literal['Door', 'GlassDoor', 'TubularDaylightDiffuser', 'TubularDaylightDome', 'Window'] = Field(...)
    construction_name: ComplexFenestrationStatesRef | ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ComplexFenestrationStates', 'ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames']})
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': "Non-blank only if base surface field Outside Boundary Condition is Surface or OtherSideCoefficients If Base Surface's Surface, specify name of corresponding subsurface in adjacent zone or specify c..."})
    view_factor_to_ground: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'From the exterior of the surface Unused if one uses the "reflections" options in Solar Distribution in Building input unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been s...'})
    frame_and_divider_name: WindowFrameAndDividerNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowFrameAndDividerNames'], 'note': 'Enter the name of a WindowProperty:FrameAndDivider object Used only for exterior windows (rectangular) and glass doors. Unused for triangular windows. If not specified (blank), window or glass door...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates are "relative" to the Zone Origin. If world, then building and zone origins are used for some internal ...'})
    vertex_1_x_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_1_y_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_1_z_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_2_x_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_2_y_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_2_z_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_3_x_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_3_y_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_3_z_coordinate: float = Field(..., json_schema_extra={'units': 'm'})
    vertex_4_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Not used for triangles'})
    vertex_4_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Not used for triangles'})
    vertex_4_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Not used for triangles'})


class FloorAdiabatic(IDFBaseModel):
    """Allows for simplified entry of exterior floors ignoring ground contact or
interior floors. View Factor to Ground is automatically calculated."""

    _idf_object_type: ClassVar[str] = "Floor:Adiabatic"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg'})
    tilt_angle: float | None = Field(default=180.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Floors are usually tilted 180 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'if not flat, should be lower left corner (from outside)'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class FloorDetailed(IDFBaseModel):
    """Allows for detailed entry of floor heat transfer surfaces."""

    _idf_object_type: ClassVar[str] = "Floor:Detailed"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    outside_boundary_condition: Literal['Adiabatic', 'Foundation', 'Ground', 'GroundBasementPreprocessorAverageFloor', 'GroundBasementPreprocessorAverageWall', 'GroundBasementPreprocessorLowerWall', 'GroundBasementPreprocessorUpperWall', 'GroundFCfactorMethod', 'GroundSlabPreprocessorAverage', 'GroundSlabPreprocessorCore', 'GroundSlabPreprocessorPerimeter', 'OtherSideCoefficients', 'OtherSideConditionsModel', 'Outdoors', 'Space', 'Surface', 'Zone'] = Field(...)
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Non-blank only if the field Outside Boundary Condition is Surface, Zone, Space, OtherSideCoefficients or OtherSideConditionsModel If Surface, specify name of corresponding surface in adjacent zone ...'})
    sun_exposure: Literal['', 'NoSun', 'SunExposed'] | None = Field(default='SunExposed')
    wind_exposure: Literal['', 'NoWind', 'WindExposed'] | None = Field(default='WindExposed')
    view_factor_to_ground: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'From the exterior of the surface Unused if one uses the "reflections" options in Solar Distribution in Building input unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been s...'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 10 vertex coordinates -- extensible object "extensible" -- duplicate last set of x,y,z coordinates, renumbering please (and changing z terminator to a comma "," for all but last one whic...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class FloorGroundContact(IDFBaseModel):
    """Allows for simplified entry of exterior floors with ground contact. View
Factors to Ground is automatically calculated."""

    _idf_object_type: ClassVar[str] = "Floor:GroundContact"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file If the construction is type "Construction:FfactorGroundFloor", then the GroundFCfactorMethod will be used.'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg'})
    tilt_angle: float | None = Field(default=180.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Floors are usually tilted 180 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'if not flat, should be lower left corner (from outside)'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class FloorInterzone(IDFBaseModel):
    """Allows for simplified entry of floors using adjacent zone (interzone) heat
transfer - adjacent surface should be a ceiling."""

    _idf_object_type: ClassVar[str] = "Floor:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone for the inside face of the surface.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space for the inside face of the surface (optional, see description of Space object for more details).'})
    outside_boundary_condition_object: OutFaceEnvNamesRef = Field(..., json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior ceilings. Specify a zone name of an adjacent zone to automatically generate the interior ceiling in the adjacent zone.'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg'})
    tilt_angle: float | None = Field(default=180.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Floors are usually tilted 180 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'If not Flat, should be Lower Left Corner (from outside)'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class GeometryTransform(IDFBaseModel):
    """Provides a simple method of altering the footprint geometry of a model. The
intent is to provide a single parameter that can be used to reshape the
building description contained in the rest of the input file."""

    _idf_object_type: ClassVar[str] = "GeometryTransform"
    plane_of_transform: Literal['', 'XY'] | None = Field(default='XY', json_schema_extra={'note': 'only current allowed value is "XY"'})
    current_aspect_ratio: float = Field(..., gt=0.0, json_schema_extra={'note': 'Aspect ratio of building as described in idf'})
    new_aspect_ratio: float = Field(..., gt=0.0, json_schema_extra={'note': 'Aspect ratio to transform to during run'})


class GlazedDoor(IDFBaseModel):
    """Allows for simplified entry of glass Doors."""

    _idf_object_type: ClassVar[str] = "GlazedDoor"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Door is on (i.e., Base Surface) Door assumes the azimuth and tilt angles of the surface it is on.'})
    frame_and_divider_name: WindowFrameAndDividerNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowFrameAndDividerNames'], 'note': 'Enter the name of a WindowProperty:FrameAndDivider object Used only for exterior windows (rectangular) and glass doors. Unused for triangular windows. If not specified (blank), window or glass door...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Door starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class GlazedDoorInterzone(IDFBaseModel):
    """Allows for simplified entry of interzone (glass interior) doors (adjacent to
other zones)."""

    _idf_object_type: ClassVar[str] = "GlazedDoor:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Door is on (i.e., Base Surface) Door assumes the azimuth and tilt angles of the surface it is on.'})
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior doors. Specify a zone name of an adjacent zone to automatically generate the interior door in the adjacent zone. a blank field will set...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Door starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Door starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class GlobalGeometryRules(IDFBaseModel):
    """Specifies the geometric rules used to describe the input of surface vertices
and daylighting reference points."""

    _idf_object_type: ClassVar[str] = "GlobalGeometryRules"
    starting_vertex_position: Literal['LowerLeftCorner', 'LowerRightCorner', 'UpperLeftCorner', 'UpperRightCorner'] = Field(..., json_schema_extra={'note': 'Specified as entry for a 4 sided surface/rectangle Surfaces are specified as viewed from outside the surface Shading surfaces as viewed from behind. (towards what they are shading)'})
    vertex_entry_direction: Literal['Clockwise', 'Counterclockwise'] = Field(...)
    coordinate_system: Literal['Relative', 'World'] = Field(..., json_schema_extra={'note': 'Relative -- coordinates are entered relative to zone origin World -- all coordinates entered are "absolute" for this facility'})
    daylighting_reference_point_coordinate_system: Literal['', 'Relative', 'World'] | None = Field(default='Relative', json_schema_extra={'note': 'Relative -- coordinates are entered relative to zone origin World -- all coordinates entered are "absolute" for this facility'})
    rectangular_surface_coordinate_system: Literal['', 'Relative', 'World'] | None = Field(default='Relative', json_schema_extra={'note': 'Relative -- Starting corner is entered relative to zone origin World -- Starting corner is entered in "absolute"'})


class InternalMass(IDFBaseModel):
    """Used to describe internal zone surface area that does not need to be part of
geometric representation. This should be the total surface area exposed to
the zone air. If you use a ZoneList in the Zone or ZoneList name field then
this definition applies to all the zones in the ZoneList. Likewise for
SpaceList."""

    _idf_object_type: ClassVar[str] = "InternalMass"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_or_zonelist_name: ZoneAndZoneListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneAndZoneListNames'], 'note': 'Zone(s) the surface is a part of.  This field is ignored when a Space or SpaceList Name is specified.'})
    space_or_spacelist_name: SpaceAndSpaceListNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceAndSpaceListNames'], 'note': 'Space(s) the surface is a part of. This field is ignored when a ZoneList Name is specified for Zone or ZoneList Name. An internal mass surface will be added to every Space in every Zone in the Zone...'})
    surface_area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2'})


class Roof(IDFBaseModel):
    """Allows for simplified entry of roofs (exterior). View Factor to Ground is
automatically calculated."""

    _idf_object_type: ClassVar[str] = "Roof"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of Roof'})
    tilt_angle: float | None = Field(default=0.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Flat Roofs are tilted 0 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'If not Flat, Starting coordinate is the Lower Left Corner of the Roof'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along X Axis'})
    width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Along Y Axis'})


class RoofCeilingDetailed(IDFBaseModel):
    """Allows for detailed entry of roof/ceiling heat transfer surfaces."""

    _idf_object_type: ClassVar[str] = "RoofCeiling:Detailed"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    outside_boundary_condition: Literal['Adiabatic', 'Ground', 'GroundBasementPreprocessorAverageFloor', 'GroundBasementPreprocessorAverageWall', 'GroundBasementPreprocessorLowerWall', 'GroundBasementPreprocessorUpperWall', 'GroundSlabPreprocessorAverage', 'GroundSlabPreprocessorCore', 'GroundSlabPreprocessorPerimeter', 'OtherSideCoefficients', 'OtherSideConditionsModel', 'Outdoors', 'Space', 'Surface', 'Zone'] = Field(...)
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Non-blank only if the field Outside Boundary Condition is Surface, Zone, Space, OtherSideCoefficients or OtherSideConditionsModel If Surface, specify name of corresponding surface in adjacent zone ...'})
    sun_exposure: Literal['', 'NoSun', 'SunExposed'] | None = Field(default='SunExposed')
    wind_exposure: Literal['', 'NoWind', 'WindExposed'] | None = Field(default='WindExposed')
    view_factor_to_ground: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'From the exterior of the surface Unused if one uses the "reflections" options in Solar Distribution in Building input unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been s...'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 10 vertex coordinates -- extensible object "extensible" -- duplicate last set of x,y,z coordinates, renumbering please (and changing z terminator to a comma "," for all but last one whic...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class ShadingBuilding(IDFBaseModel):
    """used for shading elements such as trees, other buildings, parts of this
building not being modeled these items are relative to the current building
and would move with relative geometry"""

    _idf_object_type: ClassVar[str] = "Shading:Building"
    name: str = Field(...)
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of shading device (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting coordinate is the Lower Left Corner of the Shade'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class ShadingBuildingDetailed(IDFBaseModel):
    """used for shading elements such as trees, other buildings, parts of this
building not being modeled these items are relative to the current building
and would move with relative geometry"""

    _idf_object_type: ClassVar[str] = "Shading:Building:Detailed"
    name: str = Field(...)
    transmittance_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Transmittance schedule for the shading device, defaults to zero (always opaque)'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 6 vertex coordinates -- extensible object Rules for vertices are given in GlobalGeometryRules coordinates -- For this object all surface coordinates are relative to the building origin (...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class ShadingFin(IDFBaseModel):
    """Fins are usually shading surfaces that are perpendicular to a window or
door."""

    _idf_object_type: ClassVar[str] = "Shading:Fin"
    name: str = Field(...)
    window_or_door_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    left_extension_from_window_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    left_distance_above_top_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    left_distance_below_bottom_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N2 + N3 + height of Window/Door is height of Fin'})
    left_tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    left_depth: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})
    right_extension_from_window_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_distance_above_top_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_distance_below_bottom_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N7 + N8 + height of Window/Door is height of Fin'})
    right_tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    right_depth: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})


class ShadingFinProjection(IDFBaseModel):
    """Fins are usually shading surfaces that are perpendicular to a window or
door."""

    _idf_object_type: ClassVar[str] = "Shading:Fin:Projection"
    name: str = Field(...)
    window_or_door_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    left_extension_from_window_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    left_distance_above_top_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    left_distance_below_bottom_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N2 + N3 + height of Window/Door is height of Fin'})
    left_tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    left_depth_as_fraction_of_window_door_width: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    right_extension_from_window_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_distance_above_top_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_distance_below_bottom_of_window: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N7 + N8 + height of Window/Door is height of Fin'})
    right_tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    right_depth_as_fraction_of_window_door_width: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})


class ShadingOverhang(IDFBaseModel):
    """Overhangs are usually flat shading surfaces that reference a window or door."""

    _idf_object_type: ClassVar[str] = "Shading:Overhang"
    name: str = Field(...)
    window_or_door_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    height_above_window_or_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    left_extension_from_window_door_width: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_extension_from_window_door_width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N3 + N4 + Window/Door Width is Overhang Length'})
    depth: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm'})


class ShadingOverhangProjection(IDFBaseModel):
    """Overhangs are typically flat shading surfaces that reference a window or
door."""

    _idf_object_type: ClassVar[str] = "Shading:Overhang:Projection"
    name: str = Field(...)
    window_or_door_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames']})
    height_above_window_or_door: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    tilt_angle_from_window_door: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    left_extension_from_window_door_width: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    right_extension_from_window_door_width: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'N3 + N4 + Window/Door Width is Overhang Length'})
    depth_as_fraction_of_window_door_height: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})


class ShadingPropertyReflectance(IDFBaseModel):
    """If this object is not defined for a shading surface the default values
listed in following fields will be used in the solar reflection calculation."""

    _idf_object_type: ClassVar[str] = "ShadingProperty:Reflectance"
    shading_surface_name: AllShadingSurfNamesRef = Field(..., json_schema_extra={'object_list': ['AllShadingSurfNames']})
    diffuse_solar_reflectance_of_unglazed_part_of_shading_surface: float | None = Field(default=0.2, ge=0.0, le=1.0)
    diffuse_visible_reflectance_of_unglazed_part_of_shading_surface: float | None = Field(default=0.2, ge=0.0, le=1.0)
    fraction_of_shading_surface_that_is_glazed: float | None = Field(default=0.0, ge=0.0, le=1.0)
    glazing_construction_name: str | None = Field(default=None, json_schema_extra={'note': 'Required if Fraction of Shading Surface That Is Glazed > 0.0'})


class ShadingSite(IDFBaseModel):
    """used for shading elements such as trees these items are fixed in space and
would not move with relative geometry"""

    _idf_object_type: ClassVar[str] = "Shading:Site"
    name: str = Field(...)
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of shading device (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting coordinate is the Lower Left Corner of the Shade'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class ShadingSiteDetailed(IDFBaseModel):
    """used for shading elements such as trees these items are fixed in space and
would not move with relative geometry"""

    _idf_object_type: ClassVar[str] = "Shading:Site:Detailed"
    name: str = Field(...)
    transmittance_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Transmittance schedule for the shading device, defaults to zero (always opaque)'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 6 vertex coordinates -- extensible object Rules for vertices are given in GlobalGeometryRules coordinates -- For this object all surface coordinates are in world coordinates.'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class ShadingZoneDetailed(IDFBaseModel):
    """used For fins, overhangs, elements that shade the building, are attached to
the building but are not part of the heat transfer calculations"""

    _idf_object_type: ClassVar[str] = "Shading:Zone:Detailed"
    name: str = Field(...)
    base_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames']})
    transmittance_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Transmittance schedule for the shading device, defaults to zero (always opaque)'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 6 vertex coordinates -- extensible object vertices are given in GlobalGeometryRules coordinates -- if relative, all surface coordinates are "relative" to the Zone Origin. if world, then ...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class Space(IDFBaseModel):
    """Defines a space (room) in the building. All Spaces are part of a Zone. Every
Zone contains one or more spaces. Space is an optional input. If a Zone has
no Space(s) specified in input then a default Space named <Zone Name> will
be created. If some surfaces in a Zone are assigned to a space and some are
not, then a default Space named <Zone Name>-Remainder will be created. Input
references to Space Names must have a matching Space object (default space
names may not be referenced except in output variable keys)."""

    _idf_object_type: ClassVar[str] = "Space"
    name: str = Field(..., json_schema_extra={'note': 'Name of the Space. This name must be unique across Zone, Space, ZoneList, and SpaceList names.'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    ceiling_height: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm', 'note': 'If this field is 0.0, negative or autocalculate, then the average height of the space is automatically calculated and used in subsequent calculations. If this field is positive, then the number ent...'})
    volume: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm3', 'note': 'If this field is 0.0, negative or autocalculate, then the volume of the space is automatically calculated and used in subsequent calculations. If this field is positive, then the number entered her...'})
    floor_area: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm2', 'note': 'If this field is 0.0, negative or autocalculate, then the floor area of the space is automatically calculated and used in subsequent calculations. If this field is positive, then the number entered...'})
    space_type: str | None = Field(default='General', json_schema_extra={'note': 'Space type is used to tag spaces by activity type, such as office, classroom, storage, etc.'})
    tags: list[SpaceTagsItem] | None = Field(default=None)


class SpaceList(IDFBaseModel):
    """Defines a list of Spaces which can be referenced as a group. The SpaceList
name may be used elsewhere in the input to apply a parameter to all Spaces
in the list. SpaceLists can be used effectively with the following objects:
InternalMass, People, Lights, ElectricEquipment, GasEquipment,
HotWaterEquipment, and others."""

    _idf_object_type: ClassVar[str] = "SpaceList"
    name: str = Field(..., json_schema_extra={'note': 'Name of the SpaceList. This name must be unique across Zone, Space, ZoneList, and SpaceList names.'})
    spaces: list[SpaceListSpacesItem] | None = Field(default=None)


class WallAdiabatic(IDFBaseModel):
    """Allows for simplified entry of interior walls."""

    _idf_object_type: ClassVar[str] = "Wall:Adiabatic"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of wall (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Walls are usually tilted 90 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting (x,y,z) coordinate is the Lower Left Corner of the Wall'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class WallDetailed(IDFBaseModel):
    """Allows for detailed entry of wall heat transfer surfaces."""

    _idf_object_type: ClassVar[str] = "Wall:Detailed"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    outside_boundary_condition: Literal['Adiabatic', 'Foundation', 'Ground', 'GroundBasementPreprocessorAverageFloor', 'GroundBasementPreprocessorAverageWall', 'GroundBasementPreprocessorLowerWall', 'GroundBasementPreprocessorUpperWall', 'GroundFCfactorMethod', 'GroundSlabPreprocessorAverage', 'GroundSlabPreprocessorCore', 'GroundSlabPreprocessorPerimeter', 'OtherSideCoefficients', 'OtherSideConditionsModel', 'Outdoors', 'Space', 'Surface', 'Zone'] = Field(...)
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Non-blank only if the field Outside Boundary Condition is Surface, Zone, Space, OtherSideCoefficients or OtherSideConditionsModel If Surface, specify name of corresponding surface in adjacent zone ...'})
    sun_exposure: Literal['', 'NoSun', 'SunExposed'] | None = Field(default='SunExposed')
    wind_exposure: Literal['', 'NoWind', 'WindExposed'] | None = Field(default='WindExposed')
    view_factor_to_ground: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'From the exterior of the surface Unused if one uses the "reflections" options in Solar Distribution in Building input unless a DaylightingDevice:Shelf or DaylightingDevice:Tubular object has been s...'})
    number_of_vertices: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'note': 'shown with 10 vertex coordinates -- extensible object "extensible" -- duplicate last set of x,y,z coordinates, renumbering please (and changing z terminator to a comma "," for all but last one whic...'})
    vertices: list[BuildingSurfaceDetailedVerticesItem] | None = Field(default=None)


class WallExterior(IDFBaseModel):
    """Allows for simplified entry of exterior walls. View Factor to Ground is
automatically calculated."""

    _idf_object_type: ClassVar[str] = "Wall:Exterior"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of wall (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Walls are usually tilted 90 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting (x,y,z) coordinate is the Lower Left Corner of the Wall'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class WallInterzone(IDFBaseModel):
    """Allows for simplified entry of interzone walls (walls between zones)."""

    _idf_object_type: ClassVar[str] = "Wall:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone for the inside face of the surface.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space for the inside face of the surface (optional, see description of Space object for more details).'})
    outside_boundary_condition_object: OutFaceEnvNamesRef = Field(..., json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior walls. Specify a zone name of an adjacent zone to automatically generate the interior wall in the adjacent zone.'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of wall (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Walls are usually tilted 90 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting (x,y,z) coordinate is the Lower Left Corner of the Wall'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class WallUnderground(IDFBaseModel):
    """Allows for simplified entry of underground walls."""

    _idf_object_type: ClassVar[str] = "Wall:Underground"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file. If the construction is type "Construction:CfactorUndergroundWall", then the GroundFCfactorMethod will be used.'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Zone the surface is a part of.'})
    space_name: SpaceNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['SpaceNames'], 'note': 'Space the surface is a part of (optional, see description of Space object for more details).'})
    azimuth_angle: float | None = Field(default=None, ge=0.0, le=360.0, json_schema_extra={'units': 'deg', 'note': 'Facing direction of outside of wall (S=180,N=0,E=90,W=270)'})
    tilt_angle: float | None = Field(default=90.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Walls are usually tilted 90 degrees'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Starting (x,y,z) coordinate is the Lower Left Corner of the Wall'})
    starting_y_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class Window(IDFBaseModel):
    """Allows for simplified entry of Windows."""

    _idf_object_type: ClassVar[str] = "Window"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Window is on (i.e., Base Surface) Window assumes the azimuth and tilt angles of the surface it is on.'})
    frame_and_divider_name: WindowFrameAndDividerNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowFrameAndDividerNames'], 'note': 'Enter the name of a WindowProperty:FrameAndDivider object Used only for exterior windows (rectangular) and glass doors. Unused for triangular windows. If not specified (blank), window or glass door...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Window starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class WindowInterzone(IDFBaseModel):
    """Allows for simplified entry of interzone windows (adjacent to other zones)."""

    _idf_object_type: ClassVar[str] = "Window:Interzone"
    name: str = Field(...)
    construction_name: ConstructionNamesRef = Field(..., json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'To be matched with a construction in this input file'})
    building_surface_name: SurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['SurfaceNames'], 'note': 'Name of Surface (Wall, usually) the Window is on (i.e., Base Surface) Window assumes the azimuth and tilt angles of the surface it is on.'})
    outside_boundary_condition_object: OutFaceEnvNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['OutFaceEnvNames'], 'note': 'Specify a surface name in an adjacent zone for known interior windows. Specify a zone name of an adjacent zone to automatically generate the interior window in the adjacent zone. a blank field will...'})
    multiplier: float | None = Field(default=1.0, ge=1.0, json_schema_extra={'note': 'Used only for Surface Type = WINDOW, GLASSDOOR or DOOR Non-integer values will be truncated to integer'})
    starting_x_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'Window starting coordinate is specified relative to the Base Surface origin.'})
    starting_z_coordinate: float | None = Field(default=None, json_schema_extra={'units': 'm', 'note': 'How far up the wall the Window starts. (in 2-d, this would be a Y Coordinate)'})
    length: float | None = Field(default=None, json_schema_extra={'units': 'm'})
    height: float | None = Field(default=None, json_schema_extra={'units': 'm'})


class WindowPropertyAirflowControl(IDFBaseModel):
    """Used to control forced airflow through a gap between glass layers"""

    _idf_object_type: ClassVar[str] = "WindowProperty:AirflowControl"
    name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames'], 'note': 'Name must be that of an exterior window with two or three glass layers.'})
    airflow_source: Literal['', 'IndoorAir', 'OutdoorAir'] | None = Field(default='IndoorAir')
    airflow_destination: Literal['', 'IndoorAir', 'OutdoorAir', 'ReturnAir'] | None = Field(default='OutdoorAir', json_schema_extra={'note': 'If ReturnAir is selected, the name of the Return Air Node may be specified below.'})
    maximum_flow_rate: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm3/s-m', 'note': 'Above is m3/s per m of glazing width'})
    airflow_control_type: Literal['', 'AlwaysOff', 'AlwaysOnAtMaximumFlow', 'ScheduledOnly'] | None = Field(default='AlwaysOnAtMaximumFlow', json_schema_extra={'note': 'ScheduledOnly requires that Airflow Has Multiplier Schedule Name = Yes and that Airflow Multiplier Schedule Name is specified.'})
    airflow_is_scheduled: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, then Airflow Multiplier Schedule Name must be specified'})
    airflow_multiplier_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Required if Airflow Is Scheduled = Yes. Schedule values are 0.0 or 1.0 and multiply Maximum Air Flow.'})
    airflow_return_air_node_name: str | None = Field(default=None, json_schema_extra={'note': 'Name of the return air node for this airflow window if the Airflow Destination is ReturnAir. If left blank, defaults to the first return air node for the zone of the window surface.'})


class WindowPropertyFrameAndDivider(IDFBaseModel):
    """Specifies the dimensions of a window frame, dividers, and inside reveal
surfaces. Referenced by the surface objects for exterior windows and glass
doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor)."""

    _idf_object_type: ClassVar[str] = "WindowProperty:FrameAndDivider"
    name: str = Field(..., json_schema_extra={'note': 'Referenced by surfaces that are exterior windows Not used by interzone windows'})
    frame_width: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'm', 'note': 'Width of frame in plane of window Frame width assumed the same on all sides of window'})
    frame_outside_projection: float | None = Field(default=0.0, ge=0.0, le=0.5, json_schema_extra={'units': 'm', 'note': 'Amount that frame projects outward from the outside face of the glazing'})
    frame_inside_projection: float | None = Field(default=0.0, ge=0.0, le=0.5, json_schema_extra={'units': 'm', 'note': 'Amount that frame projects inward from the inside face of the glazing'})
    frame_conductance: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2-K', 'note': 'Effective conductance of frame Excludes air films Obtained from WINDOW 5 or other 2-D calculation'})
    ratio_of_frame_edge_glass_conductance_to_center_of_glass_conductance: float | None = Field(default=1.0, le=4.0, gt=0.0, json_schema_extra={'note': 'Excludes air films; applies only to multipane windows Obtained from WINDOW 5 or other 2-D calculation'})
    frame_solar_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0, json_schema_extra={'note': 'Assumed same on outside and inside of frame'})
    frame_visible_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0, json_schema_extra={'note': 'Assumed same on outside and inside of frame'})
    frame_thermal_hemispherical_emissivity: float | None = Field(default=0.9, gt=0.0, json_schema_extra={'note': 'Assumed same on outside and inside of frame'})
    divider_type: Literal['', 'DividedLite', 'Suspended'] | None = Field(default='DividedLite')
    divider_width: float | None = Field(default=0.0, ge=0.0, le=0.5, json_schema_extra={'units': 'm', 'note': 'Width of dividers in plane of window Width assumed the same for all dividers'})
    number_of_horizontal_dividers: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'note': '"Horizontal" means parallel to local window X-axis'})
    number_of_vertical_dividers: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'note': '"Vertical" means parallel to local window Y-axis'})
    divider_outside_projection: float | None = Field(default=0.0, ge=0.0, le=0.5, json_schema_extra={'units': 'm', 'note': 'Amount that divider projects outward from the outside face of the glazing Outside projection assumed the same for all divider elements'})
    divider_inside_projection: float | None = Field(default=0.0, ge=0.0, le=0.5, json_schema_extra={'units': 'm', 'note': 'Amount that divider projects inward from the inside face of the glazing Inside projection assumed the same for all divider elements'})
    divider_conductance: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'W/m2-K', 'note': 'Effective conductance of divider Excludes air films Obtained from WINDOW 5 or other 2-D calculation'})
    ratio_of_divider_edge_glass_conductance_to_center_of_glass_conductance: float | None = Field(default=1.0, le=4.0, gt=0.0, json_schema_extra={'note': 'Excludes air films Obtained from WINDOW 5 or other 2-D calculation'})
    divider_solar_absorptance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'note': 'Assumed same on outside and inside of divider'})
    divider_visible_absorptance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'note': 'Assumed same on outside and inside of divider'})
    divider_thermal_hemispherical_emissivity: float | None = Field(default=0.9, gt=0.0, lt=1.0, json_schema_extra={'note': 'Assumed same on outside and inside of divider'})
    outside_reveal_solar_absorptance: float | None = Field(default=0.0, ge=0.0, le=1.0)
    inside_sill_depth: float | None = Field(default=0.0, ge=0.0, le=2.0, json_schema_extra={'units': 'm'})
    inside_sill_solar_absorptance: float | None = Field(default=0.0, ge=0.0, le=1.0)
    inside_reveal_depth: float | None = Field(default=0.0, ge=0.0, le=2.0, json_schema_extra={'units': 'm', 'note': 'Distance from plane of inside surface of glazing to plane of inside surface of wall. Outside reveal depth is determined from the geometry of the window and the wall it is on; it is non-zero if the ...'})
    inside_reveal_solar_absorptance: float | None = Field(default=0.0, ge=0.0, le=1.0)
    nfrc_product_type_for_assembly_calculations: Literal['', 'CasementDouble', 'CasementSingle', 'CurtainWall', 'DoorSidelite', 'DoorTransom', 'DualAction', 'Fixed', 'Garage', 'Greenhouse', 'HingedEscape', 'HorizontalSlider', 'Jal', 'Pivoted', 'ProjectingDual', 'ProjectingSingle', 'SideHingedDoor', 'Skylight', 'SlidingPatioDoor', 'SpandrelPanel', 'TropicalAwning', 'TubularDaylightingDevice', 'VerticalSlider'] | None = Field(default='CurtainWall', json_schema_extra={'note': 'Used when computing the assembly u-factor, SHGC and visible transmittance for reporting only'})


class WindowPropertyStormWindow(IDFBaseModel):
    """This is a movable exterior glass layer that is usually applied in the winter
and removed in the summer."""

    _idf_object_type: ClassVar[str] = "WindowProperty:StormWindow"
    window_name: SubSurfNamesRef = Field(..., json_schema_extra={'object_list': ['SubSurfNames'], 'note': 'Must be the name of a FenestrationSurface:Detailed object with Surface Type = WINDOW. The WindowProperty:StormWindow object can only be used with exterior windows.'})
    storm_glass_layer_name: GlazingMaterialNameRef = Field(..., json_schema_extra={'object_list': ['GlazingMaterialName'], 'note': 'Must be a WindowMaterial:Glazing or WindowMaterial:Glazing:RefractionExtinctionMethod Gap between storm glass layer and adjacent glass layer is assumed to be filled with Air'})
    distance_between_storm_glass_layer_and_adjacent_glass: float | None = Field(default=0.05, le=0.5, gt=0.0, json_schema_extra={'units': 'm'})
    month_that_storm_glass_layer_is_put_on: int = Field(..., ge=1, le=12)
    day_of_month_that_storm_glass_layer_is_put_on: int = Field(..., ge=1, le=31)
    month_that_storm_glass_layer_is_taken_off: int = Field(..., ge=1, le=12)
    day_of_month_that_storm_glass_layer_is_taken_off: int = Field(..., ge=1, le=31)


class WindowShadingControl(IDFBaseModel):
    """Specifies the type, location, and controls for window shades, window blinds,
and switchable glazing. Referencing the surface objects for exterior windows
and glass doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor)."""

    _idf_object_type: ClassVar[str] = "WindowShadingControl"
    name: str = Field(..., json_schema_extra={'note': 'Referenced by surfaces that are exterior windows Not used by interzone windows'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    shading_control_sequence_number: int | None = Field(default=1, ge=1, json_schema_extra={'note': 'If multiple WindowShadingControl objects are used than the order that they deploy the window shades can be set with this field. The first WindowShadingControl should be 1 and subsequent WindowShadi...'})
    shading_type: Literal['BetweenGlassBlind', 'BetweenGlassShade', 'ExteriorBlind', 'ExteriorScreen', 'ExteriorShade', 'InteriorBlind', 'InteriorShade', 'SwitchableGlazing'] = Field(...)
    construction_with_shading_name: ConstructionNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ConstructionNames'], 'note': 'Required if Shading Type = SwitchableGlazing Required if Shading Type = interior or exterior shade or blind, or exterior screen, and "Shading Device Material Name" is not specified. If both "Constr...'})
    shading_control_type: Literal['AlwaysOff', 'AlwaysOn', 'MeetDaylightIlluminanceSetpoint', 'OffNightAndOnDayIfCoolingAndHighSolarOnWindow', 'OnIfHighGlare', 'OnIfHighHorizontalSolar', 'OnIfHighOutdoorAirTempAndHighHorizontalSolar', 'OnIfHighOutdoorAirTempAndHighSolarOnWindow', 'OnIfHighOutdoorAirTemperature', 'OnIfHighSolarOnWindow', 'OnIfHighSolarOrHighLuminanceTillMidnight', 'OnIfHighSolarOrHighLuminanceTillNextMorning', 'OnIfHighSolarOrHighLuminanceTillSunset', 'OnIfHighZoneAirTempAndHighHorizontalSolar', 'OnIfHighZoneAirTempAndHighSolarOnWindow', 'OnIfHighZoneAirTemperature', 'OnIfHighZoneCooling', 'OnIfScheduleAllows', 'OnNightAndOnDayIfCoolingAndHighSolarOnWindow', 'OnNightIfHeatingAndOffDay', 'OnNightIfHeatingAndOnDayIfCooling', 'OnNightIfLowInsideTempAndOffDay', 'OnNightIfLowOutdoorTempAndOffDay', 'OnNightIfLowOutdoorTempAndOnDayIfCooling'] = Field(..., json_schema_extra={'note': 'OnIfScheduleAllows requires that Schedule Name be specified and Shading Control Is Scheduled = Yes. AlwaysOn, AlwaysOff and OnIfScheduleAllows are the only valid control types for ExteriorScreen. T...'})
    schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Required if Shading Control Is Scheduled = Yes. If schedule value = 1, shading control is active, i.e., shading can take place only if the control test passes. If schedule value = 0, shading is off...'})
    setpoint: float | None = Field(default=None, json_schema_extra={'units': 'W/m2, W or deg C', 'note': 'W/m2 for solar-based controls, W for cooling- or heating-based controls, deg C for temperature-based controls. Unused for Shading Control Type = AlwaysOn, AlwaysOff, OnIfScheduleAllows, OnIfHighGla...'})
    shading_control_is_scheduled: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': 'If Yes, Schedule Name is required; if No, Schedule Name is not used. Shading Control Is Scheduled = Yes is required if Shading Control Type = OnIfScheduleAllows.'})
    glare_control_is_active: Literal['', 'No', 'Yes'] | None = Field(default='No', json_schema_extra={'note': "If Yes and window is in a daylit zone, shading is on if zone's discomfort glare index exceeds the maximum discomfort glare index specified in the Daylighting object referenced by the zone. The glar..."})
    shading_device_material_name: WindowShadesScreensAndBlindsRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowShadesScreensAndBlinds'], 'note': 'Enter the name of a WindowMaterial:Shade, WindowMaterial:Screen or WindowMaterial:Blind object. Required if "Construction with Shading Name" is not specified. Not used if Shading Control Type = Swi...'})
    type_of_slat_angle_control_for_blinds: Literal['', 'BlockBeamSolar', 'FixedSlatAngle', 'ScheduledSlatAngle'] | None = Field(default='FixedSlatAngle', json_schema_extra={'note': 'Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind. If choice is ScheduledSlatAngle then Slat Angle Schedule Name is required.'})
    slat_angle_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Used only if Shading Type = InteriorBlind, ExteriorBlind or BetweenGlassBlind. Required if Type of Slat Angle Control for Blinds = ScheduledSlatAngle Schedule values should be degrees (0 minimum, 1...'})
    setpoint_2: float | None = Field(default=None, json_schema_extra={'units': 'W/m2, deg C or cd/m2', 'note': 'W/m2 for solar-based controls, deg C for temperature-based controls, cd/m2 for luminance based controls. Used only as the second setpoint for the following two-setpoint control types: OnIfHighOutdo...'})
    daylighting_control_object_name: DaylightingControlNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['DaylightingControlNames'], 'note': 'Reference to the Daylighting:Controls object that provides the glare and illuminance control to the zone.'})
    multiple_surface_control_type: Literal['', 'Group', 'Sequential'] | None = Field(default='Sequential', json_schema_extra={'note': 'When Sequential is used the list of fenestration surfaces are controlled individually in the order specified When Group is used the entire list is controlled simultaneously and if glare control is ...'})
    fenestration_surfaces: list[WindowShadingControlFenestrationSurfacesItem] | None = Field(default=None)


class Zone(IDFBaseModel):
    """Defines a thermal zone of the building. Every zone contains one or more
Spaces. Space is an optional input. If a Zone has no Space(s) specified in
input then a default Space named <Zone Name> will be created. If some
surfaces in a Zone are assigned to a space and some are not, then a default
Space named <Zone Name>-Remainder will be created. Input references to Space
Names must have a matching Space object (default space names may not be
referenced except in output variable keys)."""

    _idf_object_type: ClassVar[str] = "Zone"
    name: str = Field(..., json_schema_extra={'note': 'Name of the Zone. This name must be unique across Zone, Space, ZoneList, and SpaceList names.'})
    direction_of_relative_north: float | None = Field(default=0.0, json_schema_extra={'units': 'deg'})
    x_origin: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    y_origin: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    z_origin: float | None = Field(default=0.0, json_schema_extra={'units': 'm'})
    type: int | None = Field(default=1, ge=1, le=1)
    multiplier: int | None = Field(default=1, ge=1)
    ceiling_height: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm', 'note': 'If this field is 0.0, negative or autocalculate, then the average height of the zone is automatically calculated and used in subsequent calculations. If this field is positive, then the number ente...'})
    volume: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm3', 'note': 'If this field is 0.0, negative or autocalculate, then the volume of the zone is automatically calculated and used in subsequent calculations. If this field is positive, then the number entered here...'})
    floor_area: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm2', 'note': 'If this field is 0.0, negative or autocalculate, then the floor area of the zone is automatically calculated and used in subsequent calculations. If this field is positive, then the number entered ...'})
    zone_inside_convection_algorithm: Literal['', 'ASTMC1340', 'AdaptiveConvectionAlgorithm', 'CeilingDiffuser', 'Simple', 'TARP', 'TrombeWall'] | None = Field(default=None, json_schema_extra={'note': 'Will default to same value as SurfaceConvectionAlgorithm:Inside object setting this field overrides the default SurfaceConvectionAlgorithm:Inside for this zone Simple = constant natural convection ...'})
    zone_outside_convection_algorithm: Literal['', 'AdaptiveConvectionAlgorithm', 'DOE-2', 'MoWiTT', 'SimpleCombined', 'TARP'] | None = Field(default=None, json_schema_extra={'note': 'Will default to same value as SurfaceConvectionAlgorithm:Outside object setting this field overrides the default SurfaceConvectionAlgorithm:Outside for this zone SimpleCombined = Combined radiation...'})
    part_of_total_floor_area: Literal['', 'No', 'Yes'] | None = Field(default='Yes')


class ZoneGroup(IDFBaseModel):
    """Adds a multiplier to a ZoneList. This can be used to reduce the amount of
input necessary for simulating repetitive structures, such as the identical
floors of a multi-story building."""

    _idf_object_type: ClassVar[str] = "ZoneGroup"
    name: str = Field(..., json_schema_extra={'note': 'Name of the Zone Group'})
    zone_list_name: ZoneListNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneListNames']})
    zone_list_multiplier: int | None = Field(default=1, ge=1)


class ZoneList(IDFBaseModel):
    """Defines a list of thermal zones which can be referenced as a group. The
ZoneList name may be used elsewhere in the input to apply a parameter to all
zones in the list. ZoneLists can be used effectively with the following
objects: People, Lights, ElectricEquipment, GasEquipment, HotWaterEquipment,
ZoneInfiltration:DesignFlowRate, ZoneVentilation:DesignFlowRate,
Sizing:Zone, ZoneControl:Thermostat, and others."""

    _idf_object_type: ClassVar[str] = "ZoneList"
    name: str = Field(..., json_schema_extra={'note': 'Name of the ZoneList. This name must be unique across Zone, Space, ZoneList, and SpaceList names.'})
    zones: list[ZoneListZonesItem] | None = Field(default=None)

