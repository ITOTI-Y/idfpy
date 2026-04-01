"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Zone HVAC Radiative/Convective Units
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401
from typing import TYPE_CHECKING

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllHeatTranSurfNamesRef,
    CoolingCoilsWaterRef,
    DesignSpecificationZoneHVACSizingNameRef,
    FansCVRef,
    FansSystemModelRef,
    HeatingCoilNameRef,
    RadiantDesignObjectRef,
    RadiantGroupNamesRef,
    RadiantSurfaceNamesRef,
    ScheduleNamesRef,
    SystemAvailabilityManagerListsRef,
    VentSlabGroupNamesRef,
    ZoneNamesRef,
)

if TYPE_CHECKING:
    from .availability_managers import AvailabilityManagerAssignmentList
    from .coils import CoilCoolingWater, CoilCoolingWaterDetailedGeometry, CoilHeatingElectric, CoilHeatingFuel, CoilHeatingSteam, CoilHeatingWater, CoilSystemCoolingWaterHeatExchangerAssisted
    from .hvac_design import DesignSpecificationZoneHVACSizing
    from .fans import FanConstantVolume, FanSystemModel
    from .thermal_zones import Zone


class ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem(IDFBaseModel):
    """Nested object type for array items."""
    surface_name: AllHeatTranSurfNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames'], 'note': 'Radiant energy may be distributed to specific surfaces'})
    fraction_of_radiant_energy_to_surface: float | None = Field(default=None, ge=0.0, le=1.0)

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])


class ZoneHVACLowTemperatureRadiantSurfaceGroupSurfaceFractionsItem(IDFBaseModel):
    """Nested object type for array items."""
    surface_name: RadiantSurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['RadiantSurfaceNames']})
    flow_fraction_for_surface: float = Field(..., ge=0.0)

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantSurfaceNames'])


class ZoneHVACVentilatedSlabSlabGroupDataItem(IDFBaseModel):
    """Nested object type for array items."""
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames']})
    surface_name: RadiantSurfaceNamesRef = Field(..., json_schema_extra={'object_list': ['RadiantSurfaceNames']})
    core_diameter_for_surface: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    core_length_for_surface: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    core_numbers_for_surface: float = Field(..., ge=0.0)
    slab_inlet_node_name_for_surface: str = Field(...)
    slab_outlet_node_name_for_surface: str = Field(...)

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantSurfaceNames'])



class ZoneHVACBaseboardConvectiveElectric(IDFBaseModel):
    """Electric baseboard heater, convection-only. Natural convection electric
heating unit."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:Convective:Electric"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea = > selected...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    efficiency: float | None = Field(default=1.0, ge=0.0, le=1.0)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACBaseboardConvectiveWater(IDFBaseModel):
    """Hot water baseboard heater, convection-only. Natural convection hydronic
heating unit."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:Convective:Water"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea = > selected...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    u_factor_times_area_value: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'W/K'})
    maximum_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACBaseboardRadiantConvectiveElectric(IDFBaseModel):
    """The number of surfaces can be expanded beyond 100, if necessary, by adding
more groups to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:RadiantConvective:Electric"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea = > selected...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    efficiency: float | None = Field(default=1.0, le=1.0, gt=0.0)
    fraction_radiant: float = Field(..., ge=0.0, le=1.0)
    fraction_of_radiant_energy_incident_on_people: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_fractions: list[ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem] | None = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACBaseboardRadiantConvectiveSteam(IDFBaseModel):
    """The number of surfaces can be expanded beyond 100, if necessary, by adding
more groups to the end of the list."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:RadiantConvective:Steam"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    design_object: RadiantDesignObjectRef = Field(..., json_schema_extra={'object_list': ['RadiantDesignObject']})
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    degree_of_subcooling: float | None = Field(default=5.0, ge=1.0, json_schema_extra={'units': 'deltaC'})
    maximum_steam_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    surface_fractions: list[ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem] | None = Field(default=None)

    @property
    def design_object_ref(self) -> ZoneHVACBaseboardRadiantConvectiveWaterDesign | ZoneHVACLowTemperatureRadiantConstantFlowDesign | ZoneHVACLowTemperatureRadiantVariableFlowDesign | None:
        v = self.design_object
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantDesignObject'])

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACBaseboardRadiantConvectiveSteamDesign(IDFBaseModel):
    """ZoneHVAC:Baseboard:RadiantConvective:Steam:Design"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:RadiantConvective:Steam:Design"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity is selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea is selected w...'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    fraction_radiant: float = Field(..., ge=0.0, le=1.0)
    fraction_of_radiant_energy_incident_on_people: float | None = Field(default=None, ge=0.0, le=1.0)


class ZoneHVACBaseboardRadiantConvectiveWater(IDFBaseModel):
    """The number of surfaces can be expanded beyond 100, if necessary, by adding
more groups to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:RadiantConvective:Water"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    design_object: RadiantDesignObjectRef = Field(..., json_schema_extra={'object_list': ['RadiantDesignObject']})
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    inlet_node_name: str = Field(...)
    outlet_node_name: str = Field(...)
    rated_average_water_temperature: float | None = Field(default=87.78, ge=20.0, le=150.0, json_schema_extra={'units': 'C', 'note': 'Rated average water temperature is the average of the inlet and outlet water temperatures at rated conditions.'})
    rated_water_mass_flow_rate: float | None = Field(default=0.063, le=10.0, gt=0.0, json_schema_extra={'units': 'kg/s', 'note': 'Standard is I=B=R Rating document where all baseboards are rated at either 0.063 kg/s (1 gpm) or 0.252 kg/s (4 gpm). It is recommended that users find data for the baseboard heater that corresponds...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity. This input field is rated heating capacity. Users must multiply the actual finned le...'})
    maximum_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    surface_fractions: list[ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem] | None = Field(default=None)

    @property
    def design_object_ref(self) -> ZoneHVACBaseboardRadiantConvectiveWaterDesign | ZoneHVACLowTemperatureRadiantConstantFlowDesign | ZoneHVACLowTemperatureRadiantVariableFlowDesign | None:
        v = self.design_object
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantDesignObject'])

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACBaseboardRadiantConvectiveWaterDesign(IDFBaseModel):
    """ZoneHVAC:Baseboard:RadiantConvective:Water:Design"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:Baseboard:RadiantConvective:Water:Design"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea = > selected...'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    convergence_tolerance: float | None = Field(default=0.001, gt=0.0)
    fraction_radiant: float = Field(..., ge=0.0, le=1.0)
    fraction_of_radiant_energy_incident_on_people: float | None = Field(default=None, ge=0.0, le=1.0)


class ZoneHVACCoolingPanelRadiantConvectiveWater(IDFBaseModel):
    """The number of surfaces can be expanded beyond 100, if necessary, by adding
more groups to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:CoolingPanel:RadiantConvective:Water"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    water_inlet_node_name: str = Field(...)
    water_outlet_node_name: str = Field(...)
    rated_inlet_water_temperature: float | None = Field(default=5.0, json_schema_extra={'units': 'C'})
    rated_inlet_space_temperature: float | None = Field(default=24.0, json_schema_extra={'units': 'C'})
    rated_water_mass_flow_rate: float | None = Field(default=0.063, gt=0.0, json_schema_extra={'units': 'kg/s'})
    cooling_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'CoolingDesignCapacity', 'FractionOfAutosizedCoolingCapacity', 'None'] | None = Field(default='CoolingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the cooling design capacity for scalable sizing. CoolingDesignCapacity => selected when the design cooling capacity value is specified or auto-sized. CapacityPerF...'})
    cooling_design_capacity: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Enter the design cooling capacity. Required field when the cooling design capacity method CoolingDesignCapacity.'})
    cooling_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the cooling design capacity per total floor area of cooled zones served by the unit. Required field when the cooling design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_cooling_design_capacity: float | None = Field(default=None, ge=0.0, json_schema_extra={'note': 'Enter the fraction of auto-sized cooling design capacity. Required field when the cooling design capacity method field is FractionOfAutosizedCoolingCapacity.'})
    maximum_chilled_water_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    control_type: Literal['', 'MeanAirTemperature', 'MeanRadiantTemperature', 'OperativeTemperature', 'OutdoorDryBulbTemperature', 'OutdoorWetBulbTemperature', 'ZoneConvectiveLoad', 'ZoneTotalLoad'] | None = Field(default='MeanAirTemperature', json_schema_extra={'note': 'Temperature on which unit is controlled'})
    cooling_control_throttling_range: float | None = Field(default=0.5, ge=0.5, json_schema_extra={'units': 'deltaC'})
    cooling_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    condensation_control_type: Literal['', 'Off', 'SimpleOff', 'VariableOff'] | None = Field(default='SimpleOff')
    condensation_control_dewpoint_offset: float | None = Field(default=1.0, json_schema_extra={'units': 'C'})
    fraction_radiant: float = Field(..., ge=0.0, le=1.0)
    fraction_of_radiant_energy_incident_on_people: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_fractions: list[ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem] | None = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACHighTemperatureRadiant(IDFBaseModel):
    """The number of surfaces can be expanded beyond 100, if necessary, by adding
more groups to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:HighTemperatureRadiant"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Name of zone system is serving'})
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the maximum heating power input capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    fuel_type: Literal['Electricity', 'NaturalGas'] = Field(..., json_schema_extra={'note': 'Natural gas or electricity'})
    combustion_efficiency: float | None = Field(default=0.9, ge=0.0, le=1.0, json_schema_extra={'note': 'Not used for non-gas radiant heaters'})
    fraction_of_input_converted_to_radiant_energy: float | None = Field(default=0.7, ge=0.0, le=1.0, json_schema_extra={'note': 'Radiant+latent+lost fractions must sum to 1 or less, remainder is considered convective heat'})
    fraction_of_input_converted_to_latent_energy: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_of_input_that_is_lost: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'note': 'Fraction of input vented to outdoor environment'})
    temperature_control_type: Literal['', 'MeanAirTemperature', 'MeanAirTemperatureSetpoint', 'MeanRadiantTemperature', 'MeanRadiantTemperatureSetpoint', 'OperativeTemperature', 'OperativeTemperatureSetpoint'] | None = Field(default='OperativeTemperature', json_schema_extra={'note': 'Temperature type used to control unit'})
    heating_throttling_range: float | None = Field(default=2.0, ge=0.0, json_schema_extra={'units': 'deltaC'})
    heating_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'This setpoint is a "mean air temperature", a "mean radiant temperature" or an "operative temperature" setpoint depending on the control type'})
    fraction_of_radiant_energy_incident_on_people: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'This will affect thermal comfort but from an energy balance standpoint this value gets added to the convective gains from the radiant heater'})
    surface_fractions: list[ZoneHVACBaseboardRadiantConvectiveElectricSurfaceFractionsItem] | None = Field(default=None)

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def heating_setpoint_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_setpoint_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACLowTemperatureRadiantConstantFlow(IDFBaseModel):
    """Low temperature hydronic radiant heating and/or cooling system embedded in a
building surface (wall, ceiling, or floor). Controlled by varying the hot or
chilled water temperature circulating through the unit."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:ConstantFlow"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    design_object: RadiantDesignObjectRef = Field(..., json_schema_extra={'object_list': ['RadiantDesignObject']})
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Name of zone system is serving'})
    surface_name_or_radiant_surface_group_name: (RadiantGroupNamesRef | RadiantSurfaceNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['RadiantGroupNames', 'RadiantSurfaceNames'], 'note': 'Identifies surfaces that radiant system is embedded in. For a system with multiple surfaces, enter the name of a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.'})
    hydronic_tubing_length: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm', 'note': '(total length of pipe embedded in surface)'})
    rated_flow_rate: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    pump_flow_rate_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Modifies the Rated Flow Rate of the pump on a time basis the default is that the pump is ON and runs according to its other operational requirements specified above. The schedule is for special pum...'})
    rated_pump_head: float | None = Field(default=179352.0, json_schema_extra={'units': 'Pa', 'note': 'default head is 60 feet'})
    rated_power_consumption: float | None = Field(default=None, json_schema_extra={'units': 'W'})
    heating_water_inlet_node_name: str | None = Field(default=None)
    heating_water_outlet_node_name: str | None = Field(default=None)
    heating_high_water_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Water and control temperatures for heating work together to provide a linear function that determines the water temperature sent to the radiant system. The current control temperature (see Temperat...'})
    heating_low_water_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    heating_high_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    heating_low_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_water_inlet_node_name: str | None = Field(default=None)
    cooling_water_outlet_node_name: str | None = Field(default=None)
    cooling_high_water_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'See note for Heating High Water Temperature Schedule above for interpretation information (or see the Input/Output Reference).'})
    cooling_low_water_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_high_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_low_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    number_of_circuits: Literal['', 'CalculateFromCircuitLength', 'OnePerSurface'] | None = Field(default='OnePerSurface')
    circuit_length: float | None = Field(default=106.7, json_schema_extra={'units': 'm'})

    @property
    def design_object_ref(self) -> ZoneHVACBaseboardRadiantConvectiveWaterDesign | ZoneHVACLowTemperatureRadiantConstantFlowDesign | ZoneHVACLowTemperatureRadiantVariableFlowDesign | None:
        v = self.design_object
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantDesignObject'])

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def surface_or_radiant_surface_group(self) -> IDFBaseModel | None:
        v = self.surface_name_or_radiant_surface_group_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantGroupNames', 'RadiantSurfaceNames'])

    @property
    def pump_flow_rate_schedule(self) -> IDFBaseModel | None:
        v = self.pump_flow_rate_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_high_water_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_high_water_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_low_water_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_low_water_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_high_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_high_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_low_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_low_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_high_water_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_high_water_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_low_water_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_low_water_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_high_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_high_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_low_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_low_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACLowTemperatureRadiantConstantFlowDesign(IDFBaseModel):
    """ZoneHVAC:LowTemperatureRadiant:ConstantFlow:Design"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:ConstantFlow:Design"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    fluid_to_radiant_surface_heat_transfer_model: Literal['', 'ConvectionOnly', 'ISOStandard'] | None = Field(default='ConvectionOnly', json_schema_extra={'note': 'This parameter identifies how the heat transfer between fluid being circulated through the radiant system and the radiant system (slab) is modeled. ConvectionOnly means that only convection between...'})
    hydronic_tubing_inside_diameter: float | None = Field(default=0.013, gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_outside_diameter: float | None = Field(default=0.016, gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_conductivity: float | None = Field(default=0.35, gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'Conductivity of the tubing/piping material'})
    temperature_control_type: Literal['', 'MeanAirTemperature', 'MeanRadiantTemperature', 'OperativeTemperature', 'OutdoorDryBulbTemperature', 'OutdoorWetBulbTemperature', 'RunningMeanOutdoorDryBulbTemperature', 'SurfaceFaceTemperature', 'SurfaceInteriorTemperature'] | None = Field(default='MeanAirTemperature', json_schema_extra={'note': 'Temperature used to control system'})
    running_mean_outdoor_dry_bulb_temperature_weighting_factor: float | None = Field(default=0.8, ge=0.0, le=1.0, json_schema_extra={'note': 'this is the weighting factor in the equation that calculate the running mean outdoor dry-bulb temperature as a weighted average of the previous dayâ€™s running mean outdoor dry-bulb temperature and...'})
    motor_efficiency: float | None = Field(default=0.9, ge=0.0, le=1.0)
    fraction_of_motor_inefficiencies_to_fluid_stream: float | None = Field(default=0.0, ge=0.0, le=1.0)
    condensation_control_type: Literal['', 'Off', 'SimpleOff', 'VariableOff'] | None = Field(default='SimpleOff')
    condensation_control_dewpoint_offset: float | None = Field(default=1.0, json_schema_extra={'units': 'C'})
    changeover_delay_time_period_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Changeover delay schedule name for this system. Schedule value <= 0 allows changeover with no delay The schedule values are interpreted as hours. If this field is blank, the system allows changeove...'})

    @property
    def changeover_delay_time_period_schedule_ref(self) -> IDFBaseModel | None:
        v = self.changeover_delay_time_period_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACLowTemperatureRadiantElectric(IDFBaseModel):
    """Electric resistance low temperature radiant system"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:Electric"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Name of zone system is serving'})
    surface_name_or_radiant_surface_group_name: (RadiantGroupNamesRef | RadiantSurfaceNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['RadiantGroupNames', 'RadiantSurfaceNames'], 'note': 'Identifies surfaces that radiant system is embedded in. For a system with multiple surfaces, enter the name of a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.'})
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the maximum electrical heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFlo...'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    temperature_control_type: Literal['', 'MeanAirTemperature', 'MeanRadiantTemperature', 'OperativeTemperature', 'OutdoorDryBulbTemperature', 'OutdoorWetBulbTemperature', 'SurfaceFaceTemperature', 'SurfaceInteriorTemperature'] | None = Field(default='MeanAirTemperature', json_schema_extra={'note': 'Temperature used to control unit'})
    setpoint_control_type: Literal['', 'HalfFlowPower', 'ZeroFlowPower'] | None = Field(default='HalfFlowPower', json_schema_extra={'note': 'How setpoint temperature is defined'})
    heating_throttling_range: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'deltaC'})
    heating_setpoint_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def surface_or_radiant_surface_group(self) -> IDFBaseModel | None:
        v = self.surface_name_or_radiant_surface_group_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantGroupNames', 'RadiantSurfaceNames'])

    @property
    def heating_setpoint_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_setpoint_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACLowTemperatureRadiantSurfaceGroup(IDFBaseModel):
    """This is used to allow the coordinate control of several radiant system
surfaces. Note that the following flow fractions must sum up to 1.0 The
number of surfaces can be expanded beyond 100, if necessary, by adding more
groups to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:SurfaceGroup"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    surface_fractions: list[ZoneHVACLowTemperatureRadiantSurfaceGroupSurfaceFractionsItem] | None = Field(default=None)


class ZoneHVACLowTemperatureRadiantVariableFlow(IDFBaseModel):
    """Low temperature hydronic radiant heating and/or cooling system embedded in a
building surface (wall, ceiling, or floor). Controlled by varying the hot or
chilled water flow to the unit."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:VariableFlow"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    design_object: RadiantDesignObjectRef = Field(..., json_schema_extra={'object_list': ['RadiantDesignObject']})
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_name: ZoneNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ZoneNames'], 'note': 'Name of zone system is serving'})
    surface_name_or_radiant_surface_group_name: (RadiantGroupNamesRef | RadiantSurfaceNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['RadiantGroupNames', 'RadiantSurfaceNames'], 'note': 'Identifies surfaces that radiant system is embedded in. For a system with multiple surfaces, enter the name of a ZoneHVAC:LowTemperatureRadiant:SurfaceGroup object.'})
    hydronic_tubing_length: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'm', 'note': '(total length of pipe embedded in surface)'})
    heating_design_capacity: float | Literal['', 'Autosize'] | None = Field(default='Autosize', json_schema_extra={'units': 'W', 'note': 'Enter the design heating capacity. Required field when the heating design capacity method HeatingDesignCapacity.'})
    maximum_hot_water_flow: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    heating_water_inlet_node_name: str | None = Field(default=None)
    heating_water_outlet_node_name: str | None = Field(default=None)
    cooling_design_capacity: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'W', 'note': 'Enter the design cooling capacity. Required field when the cooling design capacity method CoolingDesignCapacity.'})
    maximum_cold_water_flow: float | Literal['Autosize'] | None = Field(default=None, json_schema_extra={'units': 'm3/s'})
    cooling_water_inlet_node_name: str | None = Field(default=None)
    cooling_water_outlet_node_name: str | None = Field(default=None)
    number_of_circuits: Literal['', 'CalculateFromCircuitLength', 'OnePerSurface'] | None = Field(default='OnePerSurface')
    circuit_length: float | None = Field(default=106.7, json_schema_extra={'units': 'm'})

    @property
    def design_object_ref(self) -> ZoneHVACBaseboardRadiantConvectiveWaterDesign | ZoneHVACLowTemperatureRadiantConstantFlowDesign | ZoneHVACLowTemperatureRadiantVariableFlowDesign | None:
        v = self.design_object
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantDesignObject'])

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def surface_or_radiant_surface_group(self) -> IDFBaseModel | None:
        v = self.surface_name_or_radiant_surface_group_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantGroupNames', 'RadiantSurfaceNames'])


class ZoneHVACLowTemperatureRadiantVariableFlowDesign(IDFBaseModel):
    """ZoneHVAC:LowTemperatureRadiant:VariableFlow:Design"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:LowTemperatureRadiant:VariableFlow:Design"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str | None = Field(default=None)
    fluid_to_radiant_surface_heat_transfer_model: Literal['', 'ConvectionOnly', 'ISOStandard'] | None = Field(default='ConvectionOnly', json_schema_extra={'note': 'This parameter identifies how the heat transfer between fluid being circulated through the radiant system and the radiant system (slab) is modeled. ConvectionOnly means that only convection between...'})
    hydronic_tubing_inside_diameter: float | None = Field(default=0.013, gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_outside_diameter: float | None = Field(default=0.016, gt=0.0, json_schema_extra={'units': 'm'})
    hydronic_tubing_conductivity: float | None = Field(default=0.35, gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'Conductivity of the tubing/piping material'})
    temperature_control_type: Literal['', 'MeanAirTemperature', 'MeanRadiantTemperature', 'OperativeTemperature', 'OutdoorDryBulbTemperature', 'OutdoorWetBulbTemperature', 'SurfaceFaceTemperature', 'SurfaceInteriorTemperature'] | None = Field(default='MeanAirTemperature', json_schema_extra={'note': '(Temperature on which unit is controlled)'})
    setpoint_control_type: Literal['', 'HalfFlowPower', 'ZeroFlowPower'] | None = Field(default='HalfFlowPower', json_schema_extra={'note': 'How setpoint temperature is defined'})
    heating_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'FractionOfAutosizedHeatingCapacity', 'HeatingDesignCapacity'] | None = Field(default='HeatingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the heating design capacity. HeatingDesignCapacity = > selected when the design heating capacity value or autosize is specified. CapacityPerFloorArea = > selected...'})
    heating_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the heating design capacity per zone floor area. Required field when the heating design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_heating_design_capacity: float | None = Field(default=1.0, ge=0.0, json_schema_extra={'note': 'Enter the fraction of autosized heating design capacity. Required field when capacity the heating design capacity method field is FractionOfAutosizedHeatingCapacity.'})
    heating_control_throttling_range: float | None = Field(default=0.5, ge=0.0, json_schema_extra={'units': 'deltaC'})
    heating_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_design_capacity_method: Literal['', 'CapacityPerFloorArea', 'CoolingDesignCapacity', 'FractionOfAutosizedCoolingCapacity', 'None'] | None = Field(default='CoolingDesignCapacity', json_schema_extra={'note': 'Enter the method used to determine the cooling design capacity for scalable sizing. CoolingDesignCapacity => selected when the design cooling capacity value is specified or auto-sized. CapacityPerF...'})
    cooling_design_capacity_per_floor_area: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'W/m2', 'note': 'Enter the cooling design capacity per total floor area of cooled zones served by the unit. Required field when the cooling design capacity method field is CapacityPerFloorArea.'})
    fraction_of_autosized_cooling_design_capacity: float | None = Field(default=None, ge=0.0, json_schema_extra={'note': 'Enter the fraction of auto-sized cooling design capacity. Required field when the cooling design capacity method field is FractionOfAutosizedCoolingCapacity.'})
    cooling_control_throttling_range: float | None = Field(default=0.5, ge=0.0, json_schema_extra={'units': 'deltaC'})
    cooling_control_temperature_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames']})
    condensation_control_type: Literal['', 'Off', 'SimpleOff', 'VariableOff'] | None = Field(default='SimpleOff')
    condensation_control_dewpoint_offset: float | None = Field(default=1.0, json_schema_extra={'units': 'C'})
    changeover_delay_time_period_schedule: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Changeover delay schedule name for this system. Schedule value <= 0 allows changeover with no delay The schedule values are interpreted as hours. If this field is blank, the system allows changeove...'})

    @property
    def heating_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def changeover_delay_time_period_schedule_ref(self) -> IDFBaseModel | None:
        v = self.changeover_delay_time_period_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneHVACVentilatedSlab(IDFBaseModel):
    """Ventilated slab system where outdoor air flows through hollow cores in a
building surface (wall, ceiling, or floor)."""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:VentilatedSlab"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    availability_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Availability schedule name for this system. Schedule value > 0 means the system is available. If this field is blank, the system is always available.'})
    zone_name: ZoneNamesRef = Field(..., json_schema_extra={'object_list': ['ZoneNames'], 'note': '(name of zone system is serving)'})
    surface_name_or_radiant_surface_group_name: (RadiantSurfaceNamesRef | VentSlabGroupNamesRef) | None = Field(default=None, json_schema_extra={'object_list': ['RadiantSurfaceNames', 'VentSlabGroupNames'], 'note': '(name of surface system is embedded in) or list of surfaces'})
    maximum_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    outdoor_air_control_type: Literal['FixedAmount', 'FixedTemperature', 'VariablePercent'] = Field(...)
    minimum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s'})
    minimum_outdoor_air_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    maximum_outdoor_air_flow_rate: float | Literal['Autosize'] = Field(..., json_schema_extra={'units': 'm3/s', 'note': 'schedule values multiply the minimum outdoor air flow rate'})
    maximum_outdoor_air_fraction_or_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Note that this depends on the control type as to whether schedule values are a fraction or temperature'})
    system_configuration_type: Literal['', 'SeriesSlabs', 'SlabAndZone', 'SlabOnly'] | None = Field(default='SlabOnly')
    hollow_core_inside_diameter: float | None = Field(default=0.05, ge=0.0, json_schema_extra={'units': 'm'})
    hollow_core_length: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm', 'note': '(length of core cavity embedded in surface)'})
    number_of_cores: float | None = Field(default=None, ge=0.0, json_schema_extra={'note': 'flow will be divided evenly among the cores'})
    temperature_control_type: Literal['', 'MeanAirTemperature', 'MeanRadiantTemperature', 'OperativeTemperature', 'OutdoorDryBulbTemperature', 'OutdoorWetBulbTemperature', 'SurfaceTemperature', 'ZoneAirDewPointTemperature'] | None = Field(default='OutdoorDryBulbTemperature', json_schema_extra={'note': '(temperature on which unit is controlled)'})
    heating_high_air_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'Air and control temperatures for heating work together to provide a linear function that determines the air temperature sent to the radiant system. The current control temperature (see A14) is comp...'})
    heating_low_air_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    heating_high_control_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    heating_low_control_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_high_air_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'See note for heating high air temperature schedule above for interpretation information (or see the Input/Output Reference).'})
    cooling_low_air_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_high_control_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    cooling_low_control_temperature_schedule_name: ScheduleNamesRef = Field(..., json_schema_extra={'object_list': ['ScheduleNames']})
    return_air_node_name: str = Field(..., json_schema_extra={'note': 'This is the zone return air inlet to the ventilated slab system outdoor air mixer. This node is typically a zone exhaust node (do not connect to "Zone Return Air Node").'})
    slab_in_node_name: str = Field(..., json_schema_extra={'note': 'This is the node entering the slab or series of slabs after the fan and coil(s).'})
    zone_supply_air_node_name: str | None = Field(default=None, json_schema_extra={'note': 'This is the node name exiting the slab. This node is typically a zone inlet node. Leave blank when the system configuration is SlabOnly or SeriesSlabs.'})
    outdoor_air_node_name: str = Field(..., json_schema_extra={'note': 'This node is the outdoor air inlet to the ventilated slab oa mixer. This node should also be specified in an OutdoorAir:Node or OutdoorAir:NodeList object.'})
    relief_air_node_name: str = Field(..., json_schema_extra={'note': 'This node is the relief air node from the ventilated slab outdoor air mixer.'})
    outdoor_air_mixer_outlet_node_name: str = Field(..., json_schema_extra={'note': 'This is the node name leaving the outdoor air mixer and entering the fan and coil(s).'})
    fan_outlet_node_name: str = Field(..., json_schema_extra={'note': 'This is the node name of the fan outlet.'})
    fan_name: FansCVRef | FansSystemModelRef = Field(..., json_schema_extra={'object_list': ['FansCV', 'FansSystemModel'], 'note': 'Allowable fan types are Fan:SystemModel and Fan:ConstantVolume'})
    coil_option_type: Literal['Cooling', 'Heating', 'HeatingAndCooling', 'None'] = Field(...)
    heating_coil_object_type: Literal['Coil:Heating:Electric', 'Coil:Heating:Fuel', 'Coil:Heating:Steam', 'Coil:Heating:Water'] | None = Field(default=None)
    heating_coil_name: HeatingCoilNameRef | None = Field(default=None, json_schema_extra={'object_list': ['HeatingCoilName']})
    hot_water_or_steam_inlet_node_name: str | None = Field(default=None)
    cooling_coil_object_type: Literal['Coil:Cooling:Water', 'Coil:Cooling:Water:DetailedGeometry', 'CoilSystem:Cooling:Water:HeatExchangerAssisted'] | None = Field(default=None)
    cooling_coil_name: CoolingCoilsWaterRef | None = Field(default=None, json_schema_extra={'object_list': ['CoolingCoilsWater']})
    cold_water_inlet_node_name: str | None = Field(default=None)
    availability_manager_list_name: SystemAvailabilityManagerListsRef | None = Field(default=None, json_schema_extra={'object_list': ['SystemAvailabilityManagerLists'], 'note': 'Enter the name of an AvailabilityManagerAssignmentList object.'})
    design_specification_zonehvac_sizing_object_name: DesignSpecificationZoneHVACSizingNameRef | None = Field(default=None, json_schema_extra={'object_list': ['DesignSpecificationZoneHVACSizingName'], 'note': 'Enter the name of a DesignSpecificationZoneHVACSizing object.'})

    @property
    def availability_schedule(self) -> IDFBaseModel | None:
        v = self.availability_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def zone(self) -> Zone | None:
        v = self.zone_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ZoneNames'])

    @property
    def surface_or_radiant_surface_group(self) -> IDFBaseModel | None:
        v = self.surface_name_or_radiant_surface_group_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['RadiantSurfaceNames', 'VentSlabGroupNames'])

    @property
    def minimum_outdoor_air_schedule(self) -> IDFBaseModel | None:
        v = self.minimum_outdoor_air_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def maximum_outdoor_air_fraction_or_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.maximum_outdoor_air_fraction_or_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_high_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_high_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_low_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_low_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_high_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_high_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def heating_low_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.heating_low_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_high_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_high_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_low_air_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_low_air_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_high_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_high_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cooling_low_control_temperature_schedule(self) -> IDFBaseModel | None:
        v = self.cooling_low_control_temperature_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def fan(self) -> FanConstantVolume | FanSystemModel | None:
        v = self.fan_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['FansCV', 'FansSystemModel'])

    @property
    def heating_coil(self) -> CoilHeatingElectric | CoilHeatingFuel | CoilHeatingSteam | CoilHeatingWater | None:
        v = self.heating_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['HeatingCoilName'])

    @property
    def cooling_coil(self) -> CoilCoolingWater | CoilCoolingWaterDetailedGeometry | CoilSystemCoolingWaterHeatExchangerAssisted | None:
        v = self.cooling_coil_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CoolingCoilsWater'])

    @property
    def availability_manager_list(self) -> AvailabilityManagerAssignmentList | None:
        v = self.availability_manager_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['SystemAvailabilityManagerLists'])

    @property
    def design_specification_zonehvac_sizing_object(self) -> DesignSpecificationZoneHVACSizing | None:
        v = self.design_specification_zonehvac_sizing_object_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DesignSpecificationZoneHVACSizingName'])


class ZoneHVACVentilatedSlabSlabGroup(IDFBaseModel):
    """This is used to allow the coordinate control of several ventilated slab
system surfaces. Note that the flow fractions must sum up to 1.0. The number
of surfaces can be expanded beyond 10, if necessary, by adding more groups
to the end of the list"""

    _idf_object_type: ClassVar[str] = "ZoneHVAC:VentilatedSlab:SlabGroup"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    data: list[ZoneHVACVentilatedSlabSlabGroupDataItem] | None = Field(default=None)

