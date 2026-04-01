"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.2.
Group: Surface Construction Elements
"""
from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401
from typing import TYPE_CHECKING

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    BivariateFunctionsRef,
    CFSGapRef,
    CFSGlazingNameRef,
    ConstructionNamesRef,
    DataMatricesRef,
    GlazingMaterialNameRef,
    MaterialNameRef,
    ScheduleNamesRef,
    SpectralDataSetsRef,
    WindowComplexShadesRef,
    WindowEquivalentLayerMaterialNamesRef,
    WindowGapDeflectionStatesRef,
    WindowGapSupportPillarsRef,
    WindowGasAndGasMixturesRef,
    WindowThermalModelParametersRef,
)

if TYPE_CHECKING:
    from .misc import MatrixTwoDimension


class MaterialPropertyGlazingSpectralDataExtensionsItem(IDFBaseModel):
    """Nested object type for array items."""
    wavelength: float | None = Field(default=None, json_schema_extra={'units': 'micron'})
    transmittance: float | None = Field(default=None)
    front_reflectance: float | None = Field(default=None)
    back_reflectance: float | None = Field(default=None)


class MaterialPropertyPhaseChangeValuesItem(IDFBaseModel):
    """Nested object type for array items."""
    temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'for Temperature-enthalpy function'})
    enthalpy: float = Field(..., json_schema_extra={'units': 'J/kg', 'note': 'for Temperature-enthalpy function corresponding to temperature 1'})


class MaterialPropertyVariableThermalConductivityValuesItem(IDFBaseModel):
    """Nested object type for array items."""
    temperature: float = Field(..., json_schema_extra={'units': 'C', 'note': 'for Temperature-Thermal Conductivity function'})
    thermal_conductivity: float = Field(..., json_schema_extra={'units': 'W/m-K', 'note': 'for Temperature-Thermal Conductivity function corresponding to temperature 1'})


class WindowMaterialGlazingGroupThermochromicTemperatureDataItem(IDFBaseModel):
    """Nested object type for array items."""
    optical_data_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    window_material_glazing_name: GlazingMaterialNameRef = Field(..., json_schema_extra={'object_list': ['GlazingMaterialName']})

    @property
    def window_material_glazing(self) -> WindowMaterialGlazing | WindowMaterialGlazingGroupThermochromic | WindowMaterialGlazingRefractionExtinctionMethod | WindowMaterialSimpleGlazingSystem | None:
        v = self.window_material_glazing_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['GlazingMaterialName'])



class Construction(IDFBaseModel):
    """Start with outside layer and work your way to the inside layer Up to 10
layers total, 8 for windows Enter the material name for each layer"""

    _idf_object_type: ClassVar[str] = "Construction"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    outside_layer: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName']})
    layer_2: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_3: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_4: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_5: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_6: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_7: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_8: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_9: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})
    layer_10: MaterialNameRef | None = Field(default=None, json_schema_extra={'object_list': ['MaterialName']})

    @property
    def outside_layer_ref(self) -> IDFBaseModel | None:
        v = self.outside_layer
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_2_ref(self) -> IDFBaseModel | None:
        v = self.layer_2
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_3_ref(self) -> IDFBaseModel | None:
        v = self.layer_3
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_4_ref(self) -> IDFBaseModel | None:
        v = self.layer_4
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_5_ref(self) -> IDFBaseModel | None:
        v = self.layer_5
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_6_ref(self) -> IDFBaseModel | None:
        v = self.layer_6
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_7_ref(self) -> IDFBaseModel | None:
        v = self.layer_7
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_8_ref(self) -> IDFBaseModel | None:
        v = self.layer_8
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_9_ref(self) -> IDFBaseModel | None:
        v = self.layer_9
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])

    @property
    def layer_10_ref(self) -> IDFBaseModel | None:
        v = self.layer_10
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class ConstructionAirBoundary(IDFBaseModel):
    """Indicates an open boundary between two zones. It may be used for base
surfaces and fenestration surfaces. The two adjacent zones are grouped
together for solar, daylighting and radiant exchange. When this construction
type is used, the Outside Boundary Condition of the surface (or the base
surface of a fenestration surface) must be either Surface or Zone. A base
surface with Construction:AirBoundary cannot hold any fenestration surfaces."""

    _idf_object_type: ClassVar[str] = "Construction:AirBoundary"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    air_exchange_method: Literal['', 'None', 'SimpleMixing'] | None = Field(default='None', json_schema_extra={'note': 'This field controls how air exchange is modeled across this boundary.'})
    simple_mixing_air_changes_per_hour: float | None = Field(default=0.5, ge=0.0, json_schema_extra={'units': '1/hr', 'note': 'If the Air Exchange Method is SimpleMixing then this field specifies the air changes per hour using the volume of the smaller zone as the basis. If an AirflowNetwork simulation is active this field...'})
    simple_mixing_schedule_name: ScheduleNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ScheduleNames'], 'note': 'If the Air Exchange Method is SimpleMixing then this field specifies the air exchange schedule. If this field is blank, the schedule is always 1.0. If an AirflowNetwork simulation is active this fi...'})

    @property
    def simple_mixing_schedule(self) -> IDFBaseModel | None:
        v = self.simple_mixing_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ScheduleNames'])


class ConstructionCfactorUndergroundWall(IDFBaseModel):
    """Alternate method of describing underground wall constructions"""

    _idf_object_type: ClassVar[str] = "Construction:CfactorUndergroundWall"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    c_factor: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m2-K', 'note': 'Enter C-Factor without film coefficients or soil'})
    height: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'Enter height of the underground wall'})


class ConstructionComplexFenestrationState(IDFBaseModel):
    """Describes one state for a complex glazing system These input objects are
typically generated by using WINDOW software and export to IDF syntax"""

    _idf_object_type: ClassVar[str] = "Construction:ComplexFenestrationState"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    basis_type: Literal['', 'LBNLWINDOW', 'UserDefined'] | None = Field(default='LBNLWINDOW')
    basis_symmetry_type: Literal['', 'Axisymmetric', 'None'] | None = Field(default='None')
    window_thermal_model: WindowThermalModelParametersRef = Field(..., json_schema_extra={'object_list': ['WindowThermalModelParameters']})
    basis_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    solar_optical_complex_front_transmittance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    solar_optical_complex_back_reflectance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    visible_optical_complex_front_transmittance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    visible_optical_complex_back_transmittance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    outside_layer_name: CFSGlazingNameRef | WindowComplexShadesRef = Field(..., json_schema_extra={'object_list': ['CFSGlazingName', 'WindowComplexShades']})
    outside_layer_directional_front_absorptance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    outside_layer_directional_back_absorptance_matrix_name: DataMatricesRef = Field(..., json_schema_extra={'object_list': ['DataMatrices']})
    gap_1_name: CFSGapRef | None = Field(default=None, json_schema_extra={'object_list': ['CFSGap']})
    cfs_gap_1_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    cfs_gap_1_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    layer_2_name: (CFSGlazingNameRef | WindowComplexShadesRef) | None = Field(default=None, json_schema_extra={'object_list': ['CFSGlazingName', 'WindowComplexShades']})
    layer_2_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    layer_2_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    gap_2_name: CFSGapRef | None = Field(default=None, json_schema_extra={'object_list': ['CFSGap']})
    gap_2_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    gap_2_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    layer_3_name: (CFSGlazingNameRef | WindowComplexShadesRef) | None = Field(default=None, json_schema_extra={'object_list': ['CFSGlazingName', 'WindowComplexShades']})
    layer_3_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    layer_3_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    gap_3_name: CFSGapRef | None = Field(default=None, json_schema_extra={'object_list': ['CFSGap']})
    gap_3_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    gap_3_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    layer_4_name: (CFSGlazingNameRef | WindowComplexShadesRef) | None = Field(default=None, json_schema_extra={'object_list': ['CFSGlazingName', 'WindowComplexShades']})
    layer_4_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    layer_4_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    gap_4_name: CFSGapRef | None = Field(default=None, json_schema_extra={'object_list': ['CFSGap']})
    gap_4_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    gap_4_directional_back_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices'], 'note': 'Reserved for future use. Leave it blank for this version'})
    layer_5_name: (CFSGlazingNameRef | WindowComplexShadesRef) | None = Field(default=None, json_schema_extra={'object_list': ['CFSGlazingName', 'WindowComplexShades']})
    layer_5_directional_front_absorptance_matrix_name: DataMatricesRef | None = Field(default=None, json_schema_extra={'object_list': ['DataMatrices']})
    layer_5_directional_back_absorptance_matrix_name: str | None = Field(default=None)

    @property
    def window_thermal_model_ref(self) -> WindowThermalModelParams | None:
        v = self.window_thermal_model
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowThermalModelParameters'])

    @property
    def basis_matrix(self) -> MatrixTwoDimension | None:
        v = self.basis_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def solar_optical_complex_front_transmittance_matrix(self) -> MatrixTwoDimension | None:
        v = self.solar_optical_complex_front_transmittance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def solar_optical_complex_back_reflectance_matrix(self) -> MatrixTwoDimension | None:
        v = self.solar_optical_complex_back_reflectance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def visible_optical_complex_front_transmittance_matrix(self) -> MatrixTwoDimension | None:
        v = self.visible_optical_complex_front_transmittance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def visible_optical_complex_back_transmittance_matrix(self) -> MatrixTwoDimension | None:
        v = self.visible_optical_complex_back_transmittance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def outside_layer(self) -> WindowMaterialComplexShade | WindowMaterialGlazing | None:
        v = self.outside_layer_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGlazingName', 'WindowComplexShades'])

    @property
    def outside_layer_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.outside_layer_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def outside_layer_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.outside_layer_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_1(self) -> WindowMaterialGap | None:
        v = self.gap_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGap'])

    @property
    def cfs_gap_1_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.cfs_gap_1_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def cfs_gap_1_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.cfs_gap_1_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_2(self) -> WindowMaterialComplexShade | WindowMaterialGlazing | None:
        v = self.layer_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGlazingName', 'WindowComplexShades'])

    @property
    def layer_2_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_2_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_2_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_2_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_2(self) -> WindowMaterialGap | None:
        v = self.gap_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGap'])

    @property
    def gap_2_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_2_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_2_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_2_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_3(self) -> WindowMaterialComplexShade | WindowMaterialGlazing | None:
        v = self.layer_3_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGlazingName', 'WindowComplexShades'])

    @property
    def layer_3_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_3_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_3_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_3_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_3(self) -> WindowMaterialGap | None:
        v = self.gap_3_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGap'])

    @property
    def gap_3_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_3_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_3_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_3_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_4(self) -> WindowMaterialComplexShade | WindowMaterialGlazing | None:
        v = self.layer_4_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGlazingName', 'WindowComplexShades'])

    @property
    def layer_4_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_4_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_4_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_4_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_4(self) -> WindowMaterialGap | None:
        v = self.gap_4_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGap'])

    @property
    def gap_4_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_4_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def gap_4_directional_back_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.gap_4_directional_back_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])

    @property
    def layer_5(self) -> WindowMaterialComplexShade | WindowMaterialGlazing | None:
        v = self.layer_5_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['CFSGlazingName', 'WindowComplexShades'])

    @property
    def layer_5_directional_front_absorptance_matrix(self) -> MatrixTwoDimension | None:
        v = self.layer_5_directional_front_absorptance_matrix_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['DataMatrices'])


class ConstructionFfactorGroundFloor(IDFBaseModel):
    """Alternate method of describing slab-on-grade or underground floor
constructions"""

    _idf_object_type: ClassVar[str] = "Construction:FfactorGroundFloor"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    f_factor: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    area: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2', 'note': 'Enter area of the floor'})
    perimeterexposed: float = Field(..., ge=0.0, json_schema_extra={'units': 'm', 'note': 'Enter exposed perimeter of the floor'})


class ConstructionPropertyInternalHeatSource(IDFBaseModel):
    """Internal heat source to be attached to a construction layer"""

    _idf_object_type: ClassVar[str] = "ConstructionProperty:InternalHeatSource"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    construction_name: ConstructionNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['ConstructionNames']})
    thermal_source_present_after_layer_number: int = Field(..., ge=1, json_schema_extra={'note': 'refers to the list of materials which follows'})
    temperature_calculation_requested_after_layer_number: int = Field(..., json_schema_extra={'note': 'refers to the list of materials which follows'})
    dimensions_for_the_ctf_calculation: int = Field(..., ge=1, le=2, json_schema_extra={'note': '1 = 1-dimensional calculation, 2 = 2-dimensional calculation'})
    tube_spacing: float = Field(..., ge=0.01, le=1.0, json_schema_extra={'units': 'm', 'note': 'uniform spacing between tubes or resistance wires in direction perpendicular to main intended direction of heat transfer'})
    two_dimensional_temperature_calculation_position: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'used in conjunction with field Temperature Calculation Requested After Layer Number this field is the location perpendicular to the main direction of heat transfer 0.0 means in line with the tubing...'})

    @property
    def construction(self) -> IDFBaseModel | None:
        v = self.construction_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['ConstructionNames'])


class ConstructionWindowDataFile(IDFBaseModel):
    """Initiates search of the Window data file for a window called Name."""

    _idf_object_type: ClassVar[str] = "Construction:WindowDataFile"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    file_name: str | None = Field(default=None, json_schema_extra={'note': 'default file name is "Window5DataFile.dat" limit on this field is 100 characters.'})


class ConstructionWindowEquivalentLayer(IDFBaseModel):
    """Start with outside layer and work your way to the inside Layer Up to 11
layers total. Up to six solid layers and up to five gaps. Enter the material
name for each layer"""

    _idf_object_type: ClassVar[str] = "Construction:WindowEquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    outside_layer: WindowEquivalentLayerMaterialNamesRef = Field(..., json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_2: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_3: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_4: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_5: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_6: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_7: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_8: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_9: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_10: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})
    layer_11: WindowEquivalentLayerMaterialNamesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowEquivalentLayerMaterialNames']})

    @property
    def outside_layer_ref(self) -> IDFBaseModel | None:
        v = self.outside_layer
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_2_ref(self) -> IDFBaseModel | None:
        v = self.layer_2
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_3_ref(self) -> IDFBaseModel | None:
        v = self.layer_3
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_4_ref(self) -> IDFBaseModel | None:
        v = self.layer_4
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_5_ref(self) -> IDFBaseModel | None:
        v = self.layer_5
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_6_ref(self) -> IDFBaseModel | None:
        v = self.layer_6
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_7_ref(self) -> IDFBaseModel | None:
        v = self.layer_7
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_8_ref(self) -> IDFBaseModel | None:
        v = self.layer_8
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_9_ref(self) -> IDFBaseModel | None:
        v = self.layer_9
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_10_ref(self) -> IDFBaseModel | None:
        v = self.layer_10
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])

    @property
    def layer_11_ref(self) -> IDFBaseModel | None:
        v = self.layer_11
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowEquivalentLayerMaterialNames'])


class Material(IDFBaseModel):
    """Regular materials described with full set of thermal properties"""

    _idf_object_type: ClassVar[str] = "Material"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    roughness: Literal['MediumRough', 'MediumSmooth', 'Rough', 'Smooth', 'VeryRough', 'VerySmooth'] = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3'})
    specific_heat: float = Field(..., ge=100.0, json_schema_extra={'units': 'J/kg-K'})
    thermal_absorptance: float | None = Field(default=0.9, le=0.99999, gt=0.0)
    solar_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0)
    visible_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0)


class MaterialAirGap(IDFBaseModel):
    """Air Space in Opaque Construction"""

    _idf_object_type: ClassVar[str] = "Material:AirGap"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    thermal_resistance: float = Field(..., gt=0.0, json_schema_extra={'units': 'm2-K/W'})


class MaterialInfraredTransparent(IDFBaseModel):
    """Special infrared transparent material. Similar to a Material:Nomass with low
thermal resistance. High absorptance in both wavelengths. Area will be
doubled internally to make internal radiant exchange accurate. Should be
only material in single layer surface construction. All thermal properties
are set internally. User needs only to supply name. Cannot be used with
ConductionFiniteDifference solution algorithms"""

    _idf_object_type: ClassVar[str] = "Material:InfraredTransparent"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)


class MaterialNoMass(IDFBaseModel):
    """Regular materials properties described whose principal description is R
(Thermal Resistance)"""

    _idf_object_type: ClassVar[str] = "Material:NoMass"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    roughness: Literal['MediumRough', 'MediumSmooth', 'Rough', 'Smooth', 'VeryRough', 'VerySmooth'] = Field(...)
    thermal_resistance: float = Field(..., ge=0.001, json_schema_extra={'units': 'm2-K/W'})
    thermal_absorptance: float | None = Field(default=0.9, le=0.99999, gt=0.0)
    solar_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0)
    visible_absorptance: float | None = Field(default=0.7, ge=0.0, le=1.0)


class MaterialPropertyGlazingSpectralData(IDFBaseModel):
    """Name is followed by up to 800 sets of normal-incidence measured values of
[wavelength, transmittance, front reflectance, back reflectance] for
wavelengths covering the solar spectrum (from about 0.25 to 2.5 microns)"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:GlazingSpectralData"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    wavelength_1: float | None = Field(default=None, json_schema_extra={'units': 'micron'})
    transmittance_1: float | None = Field(default=None)
    front_reflectance_1: float | None = Field(default=None)
    back_reflectance_1: float | None = Field(default=None)
    wavelength_2: float | None = Field(default=None, json_schema_extra={'units': 'micron'})
    transmittance_2: float | None = Field(default=None)
    front_reflectance_2: float | None = Field(default=None)
    back_reflectance_2: float | None = Field(default=None)
    wavelength_3: float | None = Field(default=None, json_schema_extra={'units': 'micron'})
    transmittance_3: float | None = Field(default=None)
    front_reflectance_3: float | None = Field(default=None)
    back_reflectance_3: float | None = Field(default=None)
    wavelength_4: float | None = Field(default=None, json_schema_extra={'units': 'micron'})
    transmittance_4: float | None = Field(default=None)
    front_reflectance_4: float | None = Field(default=None)
    back_reflectance_4: float | None = Field(default=None)
    extensions: list[MaterialPropertyGlazingSpectralDataExtensionsItem] | None = Field(default=None)


class MaterialPropertyHeatAndMoistureTransferDiffusion(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Relationship between water vapor diffusion and relative
humidity fraction Has no effect with other HeatBalanceAlgorithm solution
algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:Diffusion"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Moisture Material Name that the moisture properties will be added to.'})
    number_of_data_pairs: int = Field(..., ge=1, le=25, json_schema_extra={'note': 'Water Vapor Diffusion Resistance Factor'})
    relative_humidity_fraction_1: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_2: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_3: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_4: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_5: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_6: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_7: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_8: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_9: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_10: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_11: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_12: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_13: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_14: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_15: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_16: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_17: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_18: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_19: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_20: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_21: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_22: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_23: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_24: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})
    relative_humidity_fraction_25: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    water_vapor_diffusion_resistance_factor_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'dimensionless'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyHeatAndMoistureTransferRedistribution(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Relationship between liquid transport coefficient and
moisture content Has no effect with other HeatBalanceAlgorithm solution
algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:Redistribution"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Moisture Material Name that the moisture properties will be added to.'})
    number_of_redistribution_points: int = Field(..., ge=1, le=25, json_schema_extra={'note': 'number of data points'})
    moisture_content_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyHeatAndMoistureTransferSettings(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Additional material properties for surfaces. Has no effect
with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:Settings"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Material Name that the moisture properties will be added to. This augments material properties needed for combined heat and moisture transfer for surfaces.'})
    porosity: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'm3/m3'})
    initial_water_content_ratio: float | None = Field(default=0.2, ge=0.0, json_schema_extra={'units': 'kg/kg', 'note': 'units are the water/material density ratio at the beginning of each run period.'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyHeatAndMoistureTransferSorptionIsotherm(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Relationship between moisture content and relative humidity
fraction. Has no effect with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'The Material Name that the moisture sorption isotherm will be added to.'})
    number_of_isotherm_coordinates: int = Field(..., ge=1, le=25, json_schema_extra={'note': 'Number of data Coordinates'})
    relative_humidity_fraction_1: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_2: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_3: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_4: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_5: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_6: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_7: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_8: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_9: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_10: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_11: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_12: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_13: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_14: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_15: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_16: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_17: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_18: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_19: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_20: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_21: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_22: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_23: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_24: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    relative_humidity_fraction_25: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The relative humidity is entered as a fraction.'})
    moisture_content_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyHeatAndMoistureTransferSuction(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Relationship between liquid suction transport coefficient
and moisture content Has no effect with other HeatBalanceAlgorithm solution
algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:Suction"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Material Name that the moisture properties will be added to.'})
    number_of_suction_points: int = Field(..., ge=1, le=25, json_schema_extra={'note': 'Number of Suction Liquid Transport Coefficient coordinates'})
    moisture_content_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})
    moisture_content_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    liquid_transport_coefficient_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'm2/s'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyHeatAndMoistureTransferThermalConductivity(IDFBaseModel):
    """HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution
algorithm only. Relationship between thermal conductivity and moisture
content Has no effect with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity"
    material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Moisture Material Name that the Thermal Conductivity will be added to.'})
    number_of_thermal_coordinates: int = Field(..., ge=1, le=25, json_schema_extra={'note': 'number of data coordinates'})
    moisture_content_1: float = Field(..., ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_1: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_2: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_2: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_3: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_3: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_4: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_4: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_5: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_5: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_6: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_6: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_7: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_7: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_8: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_8: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_9: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_9: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_10: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_10: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_11: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_11: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_12: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_12: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_13: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_13: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_14: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_14: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_15: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_15: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_16: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_16: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_17: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_17: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_18: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_18: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_19: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_19: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_20: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_20: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_21: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_21: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_22: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_22: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_23: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_23: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_24: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_24: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    moisture_content_25: float | None = Field(default=None, ge=0.0, json_schema_extra={'units': 'kg/m3'})
    thermal_conductivity_25: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'W/m-K'})

    @property
    def material(self) -> IDFBaseModel | None:
        v = self.material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyMoisturePenetrationDepthSettings(IDFBaseModel):
    """Additional properties for moisture using EMPD procedure HeatBalanceAlgorithm
choice=MoisturePenetrationDepthConductionTransferFunction only Has no effect
with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:MoisturePenetrationDepth:Settings"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Material Name that the moisture properties will be added to. Additional material properties required to perform the EMPD model. Effective Mean Penetration Depth (EMPD)'})
    water_vapor_diffusion_resistance_factor: float = Field(..., ge=0.0, json_schema_extra={'units': 'dimensionless', 'note': 'Ratio of water vapor permeability of stagnant air to water vapor permeability of material'})
    moisture_equation_coefficient_a: float = Field(..., json_schema_extra={'units': 'dimensionless'})
    moisture_equation_coefficient_b: float = Field(..., json_schema_extra={'units': 'dimensionless'})
    moisture_equation_coefficient_c: float = Field(..., json_schema_extra={'units': 'dimensionless'})
    moisture_equation_coefficient_d: float = Field(..., json_schema_extra={'units': 'dimensionless'})
    surface_layer_penetration_depth: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm'})
    deep_layer_penetration_depth: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'm'})
    coating_layer_thickness: float = Field(..., ge=0.0, json_schema_extra={'units': 'm'})
    coating_layer_water_vapor_diffusion_resistance_factor: float = Field(..., ge=0.0, json_schema_extra={'units': 'dimensionless', 'note': "The coating's resistance to water vapor diffusion relative to the resistance to water vapor diffusion in stagnant air (see Water Vapor Diffusion Resistance Factor above)."})

    @property
    def name_ref(self) -> IDFBaseModel | None:
        v = self.name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyPhaseChange(IDFBaseModel):
    """Additional properties for temperature dependent thermal conductivity and
enthalpy for Phase Change Materials (PCM) Name and temperature coefficient
are followed by up to 100 sets of temperature-enthalpy pairs.
HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm
only. Constructions with this should use the detailed CondFD process. Has no
effect with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:PhaseChange"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Regular Material Name to which the additional properties will be added. this the material name for the basic material properties.'})
    temperature_coefficient_for_thermal_conductivity: float | None = Field(default=0.0, json_schema_extra={'units': 'W/m-K2', 'note': 'The base temperature is 20C. This is the thermal conductivity change per degree excursion from 20C. This variable conductivity function is overridden by the VariableThermalConductivity object, if p...'})
    values: list[MaterialPropertyPhaseChangeValuesItem] | None = Field(default=None)

    @property
    def name_ref(self) -> IDFBaseModel | None:
        v = self.name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyPhaseChangeHysteresis(IDFBaseModel):
    """Additional properties for temperature dependent thermal conductivity and
enthalpy for Phase Change Materials (PCM) with separate melting and freezing
curves. HeatBalanceAlgorithm = CondFD (ConductionFiniteDifference) solution
algorithm only. Constructions with this should use the detailed CondFD
process. Has no effect with other HeatBalanceAlgorithm solution algorithms."""

    _idf_object_type: ClassVar[str] = "MaterialProperty:PhaseChangeHysteresis"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Regular Material Name to which the additional properties will be added. this the material name for the basic material properties.'})
    latent_heat_during_the_entire_phase_change_process: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/kg', 'note': 'The total latent heat absorbed or rejected during the transition from solid to liquid, or back'})
    liquid_state_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'The thermal conductivity used by this material when the material is fully liquid'})
    liquid_state_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3', 'note': 'The density used by this material when the material is fully liquid'})
    liquid_state_specific_heat: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/kg-K', 'note': 'The constant specific heat used for the fully melted (liquid) state'})
    high_temperature_difference_of_melting_curve: float = Field(..., gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'The total melting range of the material is the sum of low and high temperature difference of melting curve.'})
    peak_melting_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'The temperature at which the melting curve peaks'})
    low_temperature_difference_of_melting_curve: float = Field(..., gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'The total melting range of the material is the sum of low and high temperature difference of melting curve.'})
    solid_state_thermal_conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'The thermal conductivity used by this material when the material is fully solid'})
    solid_state_density: float = Field(..., gt=0.0, json_schema_extra={'units': 'kg/m3', 'note': 'The density used by this material when the material is fully solid'})
    solid_state_specific_heat: float = Field(..., gt=0.0, json_schema_extra={'units': 'J/kg-K', 'note': 'The constant specific heat used for the fully frozen (crystallized) state'})
    high_temperature_difference_of_freezing_curve: float = Field(..., gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'The total freezing range of the material is the sum of low and high temperature difference of freezing curve.'})
    peak_freezing_temperature: float = Field(..., gt=0.0, json_schema_extra={'units': 'C', 'note': 'The temperature at which the freezing curve peaks'})
    low_temperature_difference_of_freezing_curve: float = Field(..., gt=0.0, json_schema_extra={'units': 'deltaC', 'note': 'The total freezing range of the material is the sum of low and high temperature difference of freezing curve.'})

    @property
    def name_ref(self) -> IDFBaseModel | None:
        v = self.name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyVariableAbsorptance(IDFBaseModel):
    """MaterialProperty:VariableAbsorptance"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:VariableAbsorptance"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(..., json_schema_extra={'note': 'The name of the dynamic coating material with variable thermal or solar absorptance.'})
    reference_material_name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Regular Material Name to which the additional properties will be added. this the material name for the basic material properties.'})
    control_signal: Literal['', 'Scheduled', 'SpaceHeatingCoolingMode', 'SurfaceReceivedSolarRadiation', 'SurfaceTemperature'] | None = Field(default='SurfaceTemperature', json_schema_extra={'note': 'the variable that drives the change in thermal/solar absorptance'})
    thermal_absorptance_function_name: str | None = Field(default=None, json_schema_extra={'note': 'A Curve:* or Table:Lookup object encoding the relationship between the control signal value and the surface thermal absorptance.'})
    thermal_absorptance_schedule_name: str | None = Field(default=None, json_schema_extra={'note': 'only used when Control Signal = "Scheduled"'})
    solar_absorptance_function_name: str | None = Field(default=None, json_schema_extra={'note': 'A Curve:* or Table:Lookup object encoding the relationship between the control signal value and the surface solar absorptance.'})
    solar_absorptance_schedule_name: str | None = Field(default=None, json_schema_extra={'note': 'only used when Control Signal = "Scheduled"'})

    @property
    def reference_material(self) -> IDFBaseModel | None:
        v = self.reference_material_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialPropertyVariableThermalConductivity(IDFBaseModel):
    """Additional properties for temperature dependent thermal conductivity using
piecewise linear temperature-conductivity function. Name is followed by up
to 100 sets of temperature-conductivity pairs. HeatBalanceAlgorithm =
CondFD(ConductionFiniteDifference) solution algorithm only. Has no effect
with other HeatBalanceAlgorithm solution algorithms"""

    _idf_object_type: ClassVar[str] = "MaterialProperty:VariableThermalConductivity"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: MaterialNameRef = Field(..., json_schema_extra={'object_list': ['MaterialName'], 'note': 'Regular Material Name to which the additional properties will be added. this the material name for the basic material properties.'})
    values: list[MaterialPropertyVariableThermalConductivityValuesItem] | None = Field(default=None)

    @property
    def name_ref(self) -> IDFBaseModel | None:
        v = self.name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['MaterialName'])


class MaterialRoofVegetation(IDFBaseModel):
    """EcoRoof model, plant layer plus soil layer Implemented by Portland State
University (Sailor et al., January, 2007) only one material must be
referenced per simulation though the same EcoRoof material could be used in
multiple constructions. New moisture redistribution scheme (2010) requires
higher number of timesteps per hour (minimum 12 recommended)."""

    _idf_object_type: ClassVar[str] = "Material:RoofVegetation"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    height_of_plants: float | None = Field(default=0.2, le=1.0, gt=0.005, json_schema_extra={'units': 'm', 'note': 'The ecoroof module is designed for short plants and shrubs.'})
    leaf_area_index: float | None = Field(default=1.0, le=5.0, gt=0.001, json_schema_extra={'units': 'dimensionless', 'note': 'Entire surface is assumed covered, so decrease LAI accordingly.'})
    leaf_reflectivity: float | None = Field(default=0.22, ge=0.05, le=0.5, json_schema_extra={'units': 'dimensionless', 'note': 'Leaf reflectivity (albedo) is typically 0.18-0.25'})
    leaf_emissivity: float | None = Field(default=0.95, ge=0.8, le=1.0)
    minimum_stomatal_resistance: float | None = Field(default=180.0, ge=50.0, le=300.0, json_schema_extra={'units': 's/m', 'note': 'This depends upon plant type'})
    soil_layer_name: str | None = Field(default='Green Roof Soil')
    roughness: Literal['', 'MediumRough', 'MediumSmooth', 'Rough', 'Smooth', 'VeryRough', 'VerySmooth'] | None = Field(default='MediumRough')
    thickness: float | None = Field(default=0.1, le=0.7, gt=0.05, json_schema_extra={'units': 'm', 'note': 'thickness of the soil layer of the EcoRoof Soil depths of 0.15m (6in) and 0.30m (12in) are common.'})
    conductivity_of_dry_soil: float | None = Field(default=0.35, ge=0.2, le=1.5, json_schema_extra={'units': 'W/m-K', 'note': 'Thermal conductivity of dry soil. Typical ecoroof soils range from 0.3 to 0.5'})
    density_of_dry_soil: float | None = Field(default=1100.0, ge=300.0, le=2000.0, json_schema_extra={'units': 'kg/m3', 'note': 'Density of dry soil (the code modifies this as the soil becomes moist) Typical ecoroof soils range from 400 to 1000 (dry to wet)'})
    specific_heat_of_dry_soil: float | None = Field(default=1200.0, le=2000.0, gt=500.0, json_schema_extra={'units': 'J/kg-K', 'note': 'Specific heat of dry soil'})
    thermal_absorptance: float | None = Field(default=0.9, le=1.0, gt=0.8, json_schema_extra={'note': 'Soil emissivity is typically in range of 0.90 to 0.98'})
    solar_absorptance: float | None = Field(default=0.7, ge=0.4, le=0.9, json_schema_extra={'note': 'Solar absorptance of dry soil (1-albedo) is typically 0.60 to 0.85 corresponding to a dry albedo of 0.15 to 0.40'})
    visible_absorptance: float | None = Field(default=0.75, le=1.0, gt=0.5)
    saturation_volumetric_moisture_content_of_the_soil_layer: float | None = Field(default=0.3, le=0.5, gt=0.1, json_schema_extra={'note': 'Maximum moisture content is typically less than 0.5'})
    residual_volumetric_moisture_content_of_the_soil_layer: float | None = Field(default=0.01, ge=0.01, le=0.1)
    initial_volumetric_moisture_content_of_the_soil_layer: float | None = Field(default=0.1, le=0.5, gt=0.05)
    moisture_diffusion_calculation_method: Literal['', 'Advanced', 'Simple'] | None = Field(default='Advanced', json_schema_extra={'note': 'Advanced calculation requires increased number of timesteps (recommended >20).'})


class WindowGapDeflectionState(IDFBaseModel):
    """Used to enter data describing deflection state of the gap. It is referenced
from WindowMaterial:Gap object only and it is used only when deflection
model is set to MeasuredDeflection, otherwise it is ignored."""

    _idf_object_type: ClassVar[str] = "WindowGap:DeflectionState"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    deflected_thickness: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm', 'note': 'If left blank will be considered that gap has no deflection.'})
    initial_temperature: float | None = Field(default=25.0, ge=0.0, json_schema_extra={'units': 'C'})
    initial_pressure: float | None = Field(default=101325.0, ge=0.0, json_schema_extra={'units': 'Pa'})


class WindowGapSupportPillar(IDFBaseModel):
    """used to define pillar geometry for support pillars"""

    _idf_object_type: ClassVar[str] = "WindowGap:SupportPillar"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    spacing: float | None = Field(default=0.04, gt=0.0, json_schema_extra={'units': 'm'})
    radius: float | None = Field(default=0.0004, gt=0.0, json_schema_extra={'units': 'm'})


class WindowMaterialBlind(IDFBaseModel):
    """Window blind thermal properties"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Blind"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    slat_orientation: Literal['', 'Horizontal', 'Vertical'] | None = Field(default='Horizontal')
    slat_width: float = Field(..., le=1.0, gt=0.0, json_schema_extra={'units': 'm'})
    slat_separation: float = Field(..., le=1.0, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Distance between adjacent slat faces'})
    slat_thickness: float | None = Field(default=0.00025, le=0.1, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Distance between top and bottom surfaces of slat Slat is assumed to be rectangular in cross section and flat'})
    slat_angle: float | None = Field(default=45.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'If WindowShadingControl referencing the window that incorporates this blind has Type of Slat Angle Control for Blinds = FixedSlatAngle, then this is the fixed value of the slat angle; If WindowShad...'})
    slat_conductivity: float | None = Field(default=221.0, gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'default is for aluminum'})
    slat_beam_solar_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0)
    front_side_slat_beam_solar_reflectance: float = Field(..., ge=0.0, lt=1.0)
    back_side_slat_beam_solar_reflectance: float = Field(..., ge=0.0, lt=1.0)
    slat_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'note': 'Must equal "Slat beam solar transmittance"'})
    front_side_slat_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'note': 'Must equal "Front Side Slat Beam Solar Reflectance"'})
    back_side_slat_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'note': 'Must equal "Back Side Slat Beam Solar Reflectance"'})
    slat_beam_visible_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'note': 'Required for detailed daylighting calculation'})
    front_side_slat_beam_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'note': 'Required for detailed daylighting calculation'})
    back_side_slat_beam_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'note': 'Required for detailed daylighting calculation'})
    slat_diffuse_visible_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'note': 'Used only for detailed daylighting calculation Must equal "Slat Beam Visible Transmittance"'})
    front_side_slat_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'note': 'Required for detailed daylighting calculation Must equal "Front Side Slat Beam Visible Reflectance"'})
    back_side_slat_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'note': 'Required for detailed daylighting calculation Must equal "Back Side Slat Beam Visible Reflectance"'})
    slat_infrared_hemispherical_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0)
    front_side_slat_infrared_hemispherical_emissivity: float | None = Field(default=0.9, ge=0.0, lt=1.0)
    back_side_slat_infrared_hemispherical_emissivity: float | None = Field(default=0.9, ge=0.0, lt=1.0)
    blind_to_glass_distance: float | None = Field(default=0.05, ge=0.01, le=1.0, json_schema_extra={'units': 'm'})
    blind_top_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    blind_bottom_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0)
    blind_left_side_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    blind_right_side_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    minimum_slat_angle: float | None = Field(default=0.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Used only if WindowShadingControl referencing the window that incorporates this blind varies the slat angle (i.e., WindowShadingControl with Type of Slat Angle Control for Blinds = ScheduledSlatAng...'})
    maximum_slat_angle: float | None = Field(default=180.0, ge=0.0, le=180.0, json_schema_extra={'units': 'deg', 'note': 'Used only if WindowShadingControl referencing the window that incorporates this blind varies the slat angle (i.e., WindowShadingControl with Type of Slat Angle Control for Blinds = ScheduledSlatAng...'})


class WindowMaterialBlindEquivalentLayer(IDFBaseModel):
    """Window equivalent layer blind slat optical and thermal properties. The model
assumes that slats are thin and flat, applies correction empirical
correlation to account for curvature effect. Slats are assumed to transmit
and reflect diffusely."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Blind:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    slat_orientation: Literal['', 'Horizontal', 'Vertical'] | None = Field(default='Horizontal')
    slat_width: float = Field(..., le=0.025, gt=0.0, json_schema_extra={'units': 'm'})
    slat_separation: float = Field(..., le=0.025, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Distance between adjacent slat faces'})
    slat_crown: float | None = Field(default=0.0015, ge=0.0, le=0.00156, json_schema_extra={'units': 'm', 'note': 'Perpendicular length between the cord and the curve. Slat is assumed to be rectangular in cross section and flat. Crown=0.0625x"Slat width"'})
    slat_angle: float | None = Field(default=45.0, ge=-90.0, le=90.0, json_schema_extra={'units': 'deg', 'note': 'Slat angle is +ve if the tip of the slat front face is tilted upward, else the slat angle is -ve if the tip of the slat front face is tilted downward. The slat angle varies between -90 to +90. The ...'})
    front_side_slat_beam_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'note': 'The front side beam-diffuse solar transmittance of the slat at normal incidence averaged over the entire spectrum of solar radiation.'})
    back_side_slat_beam_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar transmittance of the slat at normal incidence averaged over the entire spectrum of solar radiation.'})
    front_side_slat_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar reflectance of the slat at normal incidence averaged over the entire spectrum of solar radiation.'})
    back_side_slat_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar reflectance of the slat at normal incidence averaged over the entire spectrum of solar radiation.'})
    front_side_slat_beam_diffuse_visible_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse visible transmittance of the slat at normal incidence averaged over the visible spectrum range of solar radiation.'})
    back_side_slat_beam_diffuse_visible_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse visible transmittance of the slat at normal incidence averaged over the visible spectrum range of solar radiation.'})
    front_side_slat_beam_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse visible reflectance of the slat at normal incidence averaged over the visible spectrum range of solar radiation.'})
    back_side_slat_beam_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse visible reflectance of the slat at normal incidence averaged over the visible spectrum range of solar radiation.'})
    slat_diffuse_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse solar transmittance of the slat averaged over the entire solar spectrum of solar radiation.'})
    front_side_slat_diffuse_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar reflectance of the slat averaged over the entire solar spectrum of solar radiation.'})
    back_side_slat_diffuse_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar reflectance of the slat averaged over the entire solar spectrum of solar radiation.'})
    slat_diffuse_diffuse_visible_transmittance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'note': 'The beam-diffuse visible transmittance of the slat averaged over the visible spectrum range of solar radiation.'})
    front_side_slat_diffuse_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse visible reflectance of the slat averaged over the visible spectrum range of solar radiation.'})
    back_side_slat_diffuse_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse visible reflectance of the slat averaged over the visible spectrum range of solar radiation.'})
    slat_infrared_transmittance: float | None = Field(default=0.0, ge=0.0, lt=1.0, json_schema_extra={'note': 'Long-wave hemispherical transmittance of the slat material. Assumed to be the same for both sides of the slat.'})
    front_side_slat_infrared_emissivity: float | None = Field(default=0.9, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Front side long-wave hemispherical emissivity of the slat material.'})
    back_side_slat_infrared_emissivity: float | None = Field(default=0.9, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Back side long-wave hemispherical emissivity of the slat material.'})
    slat_angle_control: Literal['', 'BlockBeamSolar', 'FixedSlatAngle', 'MaximizeSolar'] | None = Field(default='FixedSlatAngle', json_schema_extra={'note': 'Used only if slat angle control is desired to either maximize solar gain (MaximizeSolar), maximize visibility while eliminating beam solar radiation (BlockBeamSolar), or fixed slate angle (FixedSla...'})


class WindowMaterialComplexShade(IDFBaseModel):
    """Complex window shading layer thermal properties"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:ComplexShade"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    layer_type: Literal['', 'BSDF', 'OtherShadingType', 'Perforated', 'VenetianHorizontal', 'VenetianVertical', 'Woven'] | None = Field(default='OtherShadingType')
    thickness: float | None = Field(default=0.002, gt=0.0, json_schema_extra={'units': 'm'})
    conductivity: float | None = Field(default=1.0, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    ir_transmittance: float | None = Field(default=0.0, ge=0.0, le=1.0)
    front_emissivity: float | None = Field(default=0.84, le=1.0, gt=0.0)
    back_emissivity: float | None = Field(default=0.84, le=1.0, gt=0.0)
    top_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0)
    bottom_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0)
    left_side_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0)
    right_side_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0)
    front_opening_multiplier: float | None = Field(default=0.05, ge=0.0, le=1.0)
    slat_width: float | None = Field(default=0.016, gt=0.0, json_schema_extra={'units': 'm'})
    slat_spacing: float | None = Field(default=0.012, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Distance between adjacent slat faces'})
    slat_thickness: float | None = Field(default=0.0006, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Distance between top and bottom surfaces of slat Slat is assumed to be rectangular in cross section and flat'})
    slat_angle: float | None = Field(default=90.0, ge=-90.0, le=90.0, json_schema_extra={'units': 'deg'})
    slat_conductivity: float | None = Field(default=160.0, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    slat_curve: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm', 'note': 'this value represents curvature radius of the slat. if the slat is flat use zero. if this value is not zero, then it must be > SlatWidth/2.'})


class WindowMaterialDrapeEquivalentLayer(IDFBaseModel):
    """Specifies the properties of equivalent layer drape fabric materials. Shades
are considered to be perfect diffusers (all transmitted and reflected
radiation is hemispherically-diffuse) independent of angle of incidence.
unpleated drape fabric is treated as thin and flat layer."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Drape:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    drape_beam_beam_solar_transmittance_at_normal_incidence: float | None = Field(default=0.0, ge=0.0, le=0.2, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam solar transmittance at normal incidence. This value is the same as the openness area fraction of the drape fabric. Assumed to be same for front and back sides.'})
    front_side_drape_beam_diffuse_solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar transmittance at normal incidence averaged over the entire spectrum of solar radiation. Assumed to be the same for front and back sides.'})
    back_side_drape_beam_diffuse_solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar transmittance at normal incidence averaged over the entire spectrum of solar radiation. Assumed to be the same for front and back sides.'})
    front_side_drape_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar reflectance at normal incidence averaged over the entire spectrum of solar radiation.'})
    back_side_drape_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar reflectance at normal incidence averaged over the entire spectrum of solar radiation.'})
    drape_beam_beam_visible_transmittance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam visible transmittance at normal incidence averaged over the visible spectrum of solar radiation. Assumed same for front and back sides.'})
    drape_beam_diffuse_visible_transmittance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse visible transmittance at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for front and back sides.'})
    drape_beam_diffuse_visible_reflectance: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse visible reflectance at normal incidence average over the visible spectrum range of solar radiation. Assumed to be the same for front and back sides.'})
    drape_material_infrared_transmittance: float | None = Field(default=0.05, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Long-wave transmittance of the drape fabric at zero openness fraction. Assumed same for front and back sides.'})
    front_side_drape_material_infrared_emissivity: float | None = Field(default=0.87, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Front side long-wave emissivity of the drape fabric at zero shade openness. Openness fraction specified above is used to calculate the effective emissivity value.'})
    back_side_drape_material_infrared_emissivity: float | None = Field(default=0.87, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Back side long-wave emissivity of the drape fabric at zero shade openness. Openness fraction specified above is used to calculate the effective emissivity value.'})
    width_of_pleated_fabric: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm', 'note': 'Width of the pleated section of the draped fabric. If the drape fabric is unpleated or is flat, then the pleated section width is set to zero.'})
    length_of_pleated_fabric: float | None = Field(default=0.0, ge=0.0, json_schema_extra={'units': 'm', 'note': 'Length of the pleated section of the draped fabric. If the drape fabric is unpleated or is flat, then the pleated section length is set to zero.'})


class WindowMaterialGap(IDFBaseModel):
    """Used to define the gap between two layers in a complex fenestration system,
where the Construction:ComplexFenestrationState object is used. It is
referenced as a layer in the Construction:ComplexFenestrationState object.
It cannot be referenced as a layer from the Construction object."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Gap"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    gas_or_gas_mixture: WindowGasAndGasMixturesRef = Field(..., validation_alias='gas_or_gas_mixture_', json_schema_extra={'object_list': ['WindowGasAndGasMixtures'], 'note': 'This field should reference only WindowMaterial:Gas or WindowMaterial:GasMixture objects'})
    pressure: float | None = Field(default=101325.0, json_schema_extra={'units': 'Pa'})
    deflection_state: WindowGapDeflectionStatesRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowGapDeflectionStates'], 'note': 'If left blank, it will be considered that gap is not deflected'})
    support_pillar: WindowGapSupportPillarsRef | None = Field(default=None, json_schema_extra={'object_list': ['WindowGapSupportPillars'], 'note': 'If left blank, it will be considered that gap does not have support pillars'})

    @property
    def gas_or_gas_mixture_ref(self) -> WindowMaterialGas | WindowMaterialGasMixture | None:
        v = self.gas_or_gas_mixture
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowGasAndGasMixtures'])

    @property
    def deflection_state_ref(self) -> WindowGapDeflectionState | None:
        v = self.deflection_state
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowGapDeflectionStates'])

    @property
    def support_pillar_ref(self) -> WindowGapSupportPillar | None:
        v = self.support_pillar
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['WindowGapSupportPillars'])


class WindowMaterialGapEquivalentLayer(IDFBaseModel):
    """Gas material properties that are used in Windows Equivalent Layer References
only WindowMaterial:Gas properties"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Gap:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    gas_type: Literal['AIR', 'ARGON', 'CUSTOM', 'KRYPTON', 'XENON'] = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    gap_vent_type: Literal['Sealed', 'VentedIndoor', 'VentedOutdoor'] = Field(..., json_schema_extra={'note': 'Sealed means the gap is enclosed and gas tight, i.e., no venting to indoor or outdoor environment. VentedIndoor means the gap is vented to indoor environment, and VentedOutdoor means the gap is ven...'})
    conductivity_coefficient_a: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K', 'note': 'Used only if Gas Type = Custom'})
    conductivity_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K2', 'note': 'Used only if Gas Type = Custom'})
    conductivity_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K3', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_a: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'kg/m-s', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'kg/m-s-K', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'kg/m-s-K2', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_a: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'J/kg-K', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'J/kg-K2', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'J/kg-K3', 'note': 'Used only if Gas Type = Custom'})
    molecular_weight: float | None = Field(default=None, ge=20.0, le=200.0, json_schema_extra={'units': 'g/mol', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_ratio: float | None = Field(default=None, gt=1.0, json_schema_extra={'note': 'Used only if Gas Type = Custom'})


class WindowMaterialGas(IDFBaseModel):
    """Gas material properties that are used in Windows or Glass Doors"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Gas"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    gas_type: Literal['Air', 'Argon', 'Custom', 'Krypton', 'Xenon'] = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    conductivity_coefficient_a: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K', 'note': 'Used only if Gas Type = Custom'})
    conductivity_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K2', 'note': 'Used only if Gas Type = Custom'})
    conductivity_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'W/m-K3', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_a: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'kg/m-s', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'kg/m-s-K', 'note': 'Used only if Gas Type = Custom'})
    viscosity_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'kg/m-s-K2', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_a: float | None = Field(default=None, gt=0.0, json_schema_extra={'units': 'J/kg-K', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_b: float | None = Field(default=None, json_schema_extra={'units': 'J/kg-K2', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_coefficient_c: float | None = Field(default=None, json_schema_extra={'units': 'J/kg-K3', 'note': 'Used only if Gas Type = Custom'})
    molecular_weight: float | None = Field(default=None, ge=20.0, le=200.0, json_schema_extra={'units': 'g/mol', 'note': 'Used only if Gas Type = Custom'})
    specific_heat_ratio: float | None = Field(default=None, gt=1.0, json_schema_extra={'note': 'Used only if Gas Type = Custom'})


class WindowMaterialGasMixture(IDFBaseModel):
    """Gas mixtures that are used in Windows or Glass Doors"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:GasMixture"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    number_of_gases_in_mixture: int = Field(..., ge=1, le=4)
    gas_1_type: Literal['Air', 'Argon', 'Krypton', 'Xenon'] = Field(...)
    gas_1_fraction: float = Field(..., le=1.0, gt=0.0)
    gas_2_type: Literal['Air', 'Argon', 'Krypton', 'Xenon'] = Field(...)
    gas_2_fraction: float = Field(..., le=1.0, gt=0.0)
    gas_3_type: Literal['Air', 'Argon', 'Krypton', 'Xenon'] | None = Field(default=None)
    gas_3_fraction: float | None = Field(default=None, le=1.0, gt=0.0)
    gas_4_type: Literal['Air', 'Argon', 'Krypton', 'Xenon'] | None = Field(default=None)
    gas_4_fraction: float | None = Field(default=None, le=1.0, gt=0.0)


class WindowMaterialGlazing(IDFBaseModel):
    """Glass material properties for Windows or Glass Doors
Transmittance/Reflectance input method."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Glazing"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    optical_data_type: Literal['BSDF', 'Spectral', 'SpectralAndAngle', 'SpectralAverage'] = Field(...)
    window_glass_spectral_data_set_name: SpectralDataSetsRef | None = Field(default=None, json_schema_extra={'object_list': ['SpectralDataSets'], 'note': 'Used only when Optical Data Type = Spectral'})
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    solar_transmittance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_solar_reflectance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage Front Side is side closest to outdoor air'})
    back_side_solar_reflectance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage Back Side is side closest to zone air'})
    visible_transmittance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_visible_reflectance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage'})
    back_side_visible_reflectance_at_normal_incidence: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'note': 'Used only when Optical Data Type = SpectralAverage'})
    infrared_transmittance_at_normal_incidence: float | None = Field(default=0.0, ge=0.0, le=1.0)
    front_side_infrared_hemispherical_emissivity: float | None = Field(default=0.84, gt=0.0, lt=1.0)
    back_side_infrared_hemispherical_emissivity: float | None = Field(default=0.84, gt=0.0, lt=1.0)
    conductivity: float | None = Field(default=0.9, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    dirt_correction_factor_for_solar_and_visible_transmittance: float | None = Field(default=1.0, le=1.0, gt=0.0)
    solar_diffusing: Literal['', 'No', 'Yes'] | None = Field(default='No')
    young_s_modulus: float | None = Field(default=72000000000.0, gt=0.0, json_schema_extra={'units': 'Pa', 'note': 'coefficient used for deflection calculations. Used only with complex fenestration when deflection model is set to TemperatureAndPressureInput'})
    poisson_s_ratio: float | None = Field(default=0.22, gt=0.0, lt=1.0, json_schema_extra={'note': 'coefficient used for deflection calculations. Used only with complex fenestration when deflection model is set to TemperatureAndPressureInput'})
    window_glass_spectral_and_incident_angle_transmittance_data_set_table_name: BivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['BivariateFunctions'], 'note': 'Used only when Optical Data Type = SpectralAndAngle'})
    window_glass_spectral_and_incident_angle_front_reflectance_data_set_table_name: BivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['BivariateFunctions'], 'note': 'Used only when Optical Data Type = SpectralAndAngle'})
    window_glass_spectral_and_incident_angle_back_reflectance_data_set_table_name: BivariateFunctionsRef | None = Field(default=None, json_schema_extra={'object_list': ['BivariateFunctions'], 'note': 'Used only when Optical Data Type = SpectralAndAngle'})

    @property
    def window_glass_spectral_data_set(self) -> MaterialPropertyGlazingSpectralData | None:
        v = self.window_glass_spectral_data_set_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['SpectralDataSets'])

    @property
    def window_glass_spectral_and_incident_angle_transmittance_data_set_table(self) -> IDFBaseModel | None:
        v = self.window_glass_spectral_and_incident_angle_transmittance_data_set_table_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def window_glass_spectral_and_incident_angle_front_reflectance_data_set_table(self) -> IDFBaseModel | None:
        v = self.window_glass_spectral_and_incident_angle_front_reflectance_data_set_table_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def window_glass_spectral_and_incident_angle_back_reflectance_data_set_table(self) -> IDFBaseModel | None:
        v = self.window_glass_spectral_and_incident_angle_back_reflectance_data_set_table_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['BivariateFunctions'])


class WindowMaterialGlazingEquivalentLayer(IDFBaseModel):
    """Glass material properties for Windows or Glass Doors
Transmittance/Reflectance input method."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Glazing:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    optical_data_type: Literal['', 'Spectral', 'SpectralAverage'] | None = Field(default='SpectralAverage', json_schema_extra={'note': 'Spectral is not currently supported and SpectralAverage is the default.'})
    window_glass_spectral_data_set_name: SpectralDataSetsRef | None = Field(default=None, json_schema_extra={'object_list': ['SpectralDataSets'], 'note': 'Spectral data is not currently supported. Used only when Optical Data Type = Spectral'})
    front_side_beam_beam_solar_transmittance: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    back_side_beam_beam_solar_transmittance: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_beam_beam_solar_reflectance: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Front Side is side closest to outdoor air'})
    back_side_beam_beam_solar_reflectance: float = Field(..., ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Back Side is side closest to zone air'})
    front_side_beam_beam_visible_solar_transmittance: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    back_side_beam_beam_visible_solar_transmittance: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_beam_beam_visible_solar_reflectance: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Front Side is side closest to outdoor air'})
    back_side_beam_beam_visible_solar_reflectance: float | None = Field(default=None, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Back Side is side closest to zone air'})
    front_side_beam_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    back_side_beam_diffuse_solar_transmittance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_beam_diffuse_solar_reflectance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Front Side is side closest to outdoor air'})
    back_side_beam_diffuse_solar_reflectance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Back Side is side closest to zone air'})
    front_side_beam_diffuse_visible_solar_transmittance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    back_side_beam_diffuse_visible_solar_transmittance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage'})
    front_side_beam_diffuse_visible_solar_reflectance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Front Side is side closest to outdoor air'})
    back_side_beam_diffuse_visible_solar_reflectance: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage Back Side is side closest to zone air'})
    diffuse_diffuse_solar_transmittance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage If this field is autocalculate, then the diffuse-diffuse solar transmittance is automatically estimated from other inputs and used in subsequent c...'})
    front_side_diffuse_diffuse_solar_reflectance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage If this field is autocalculate, then the front diffuse-diffuse solar reflectance is automatically estimated from other inputs and used in subseque...'})
    back_side_diffuse_diffuse_solar_reflectance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage If this field is autocalculate, then the back diffuse-diffuse solar reflectance is automatically estimated from other inputs and used in subsequen...'})
    diffuse_diffuse_visible_solar_transmittance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage This input field is not used currently.'})
    front_side_diffuse_diffuse_visible_solar_reflectance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage This input field is not used currently.'})
    back_side_diffuse_diffuse_visible_solar_reflectance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'Used only when Optical Data Type = SpectralAverage This input field is not used currently.'})
    infrared_transmittance_applies_to_front_and_back: float | None = Field(default=0.0, validation_alias='infrared_transmittance_applies_to_front_and_back_', ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The long-wave hemispherical transmittance of the glazing. Assumed to be the same for both sides of the glazing.'})
    front_side_infrared_emissivity: float | None = Field(default=0.84, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side long-wave hemispherical emissivity of the glazing.'})
    back_side_infrared_emissivity: float | None = Field(default=0.84, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side long-wave hemispherical emissivity of the glazing.'})
    thermal_resistance: float | None = Field(default=0.158, gt=0.0, json_schema_extra={'units': 'm2-K/W', 'note': 'This is the R-Value in SI for the glass. The default value is an approximation for a single layer of glass at 1/4" inch thickness. This field is used only for movable insulation defined with this m...'})

    @property
    def window_glass_spectral_data_set(self) -> MaterialPropertyGlazingSpectralData | None:
        v = self.window_glass_spectral_data_set_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError("Not bound to IDF")
        return idf._resolve_forward(v, ['SpectralDataSets'])


class WindowMaterialGlazingGroupThermochromic(IDFBaseModel):
    """thermochromic glass at different temperatures"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:GlazingGroup:Thermochromic"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    temperature_data: list[WindowMaterialGlazingGroupThermochromicTemperatureDataItem] | None = Field(default=None)


class WindowMaterialGlazingRefractionExtinctionMethod(IDFBaseModel):
    """Glass material properties for Windows or Glass Doors Index of
Refraction/Extinction Coefficient input method Not to be used for coated
glass"""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Glazing:RefractionExtinctionMethod"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    solar_index_of_refraction: float = Field(..., gt=1.0)
    solar_extinction_coefficient: float = Field(..., gt=0.0, json_schema_extra={'units': '1/m'})
    visible_index_of_refraction: float = Field(..., gt=1.0)
    visible_extinction_coefficient: float = Field(..., gt=0.0, json_schema_extra={'units': '1/m'})
    infrared_transmittance_at_normal_incidence: float | None = Field(default=0.0, ge=0.0, lt=1.0)
    infrared_hemispherical_emissivity: float | None = Field(default=0.84, gt=0.0, lt=1.0, json_schema_extra={'note': 'Emissivity of front and back side assumed equal'})
    conductivity: float | None = Field(default=0.9, gt=0.0, json_schema_extra={'units': 'W/m-K'})
    dirt_correction_factor_for_solar_and_visible_transmittance: float | None = Field(default=1.0, le=1.0, gt=0.0)
    solar_diffusing: Literal['', 'No', 'Yes'] | None = Field(default='No')


class WindowMaterialScreen(IDFBaseModel):
    """Window screen physical properties. Can only be located on the exterior side
of a window construction."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Screen"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(..., json_schema_extra={'note': 'Enter a unique name for this window screen material.'})
    reflected_beam_transmittance_accounting_method: Literal['', 'DoNotModel', 'ModelAsDiffuse', 'ModelAsDirectBeam'] | None = Field(default='ModelAsDiffuse', json_schema_extra={'note': 'Select the method used to account for the beam solar reflected off the material surface.'})
    diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Diffuse reflectance of the screen material over the entire solar radiation spectrum. Assumed to be the same for both sides of the screen.'})
    diffuse_visible_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Diffuse visible reflectance of the screen material averaged over the solar spectrum and weighted by the response of the human eye. Assumed to be the same for both sides of the screen.'})
    thermal_hemispherical_emissivity: float | None = Field(default=0.9, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Long-wave emissivity of the screen material. Assumed to be the same for both sides of the screen.'})
    conductivity: float | None = Field(default=221.0, gt=0.0, json_schema_extra={'units': 'W/m-K', 'note': 'Thermal conductivity of the screen material. Default is for aluminum.'})
    screen_material_spacing: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'Spacing assumed to be the same in both directions.'})
    screen_material_diameter: float = Field(..., gt=0.0, json_schema_extra={'units': 'm', 'note': 'Diameter assumed to be the same in both directions.'})
    screen_to_glass_distance: float | None = Field(default=0.025, ge=0.001, le=1.0, json_schema_extra={'units': 'm', 'note': 'Distance from the window screen to the adjacent glass surface.'})
    top_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Effective area for air flow at the top of the screen divided by the perpendicular area between the glass and the top of the screen.'})
    bottom_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Effective area for air flow at the bottom of the screen divided by the perpendicular area between the glass and the bottom of the screen.'})
    left_side_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Effective area for air flow at the left side of the screen divided by the perpendicular area between the glass and the left side of the screen.'})
    right_side_opening_multiplier: float | None = Field(default=0.0, ge=0.0, le=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Effective area for air flow at the right side of the screen divided by the perpendicular area between the glass and the right side of the screen.'})
    angle_of_resolution_for_screen_transmittance_output_map: Literal[0, 1, 2, 3, 5] | Literal[''] | None = Field(default=0, json_schema_extra={'units': 'deg', 'note': 'Select the resolution of azimuth and altitude angles for the screen transmittance map. A value of 0 means no transmittance map will be generated. Valid values for this field are 0, 1, 2, 3 and 5.'})


class WindowMaterialScreenEquivalentLayer(IDFBaseModel):
    """Equivalent layer window screen physical properties. Can only be located on
the exterior side of a window construction."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Screen:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(..., json_schema_extra={'note': 'Enter a unique name for this window screen material.'})
    screen_beam_beam_solar_transmittance: float | Literal['', 'Autocalculate'] | None = Field(default='Autocalculate', json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam transmittance of the screen material at normal incidence. This input field is the same as the material openness area fraction and can be autocalculated from the wire spacing and wire ...'})
    screen_beam_diffuse_solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse solar transmittance of the screen material at normal incidence averaged over the entire spectrum of solar radiation. Assumed to be the same for both sides of the screen.'})
    screen_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse solar reflectance of the screen material at normal incidence averaged over the entire spectrum of solar radiation. Assumed to be the same for both sides of the screen.'})
    screen_beam_beam_visible_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam visible transmittance of the screen material at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for both sides of the screen.'})
    screen_beam_diffuse_visible_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse visible transmittance of the screen material at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for both sides of the screen.'})
    screen_beam_diffuse_visible_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Beam-diffuse visible reflectance of the screen material at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for both sides of the screen.'})
    screen_infrared_transmittance: float | None = Field(default=0.02, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The long-wave hemispherical transmittance of the screen material. Assumed to be the same for both sides of the screen.'})
    screen_infrared_emissivity: float | None = Field(default=0.93, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The long-wave hemispherical emissivity of the screen material. Assumed to be the same for both sides of the screen.'})
    screen_wire_spacing: float | None = Field(default=0.025, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Spacing assumed to be the same in both directions.'})
    screen_wire_diameter: float | None = Field(default=0.005, gt=0.0, json_schema_extra={'units': 'm', 'note': 'Diameter assumed to be the same in both directions.'})


class WindowMaterialShade(IDFBaseModel):
    """Specifies the properties of window shade materials. Reflectance and
emissivity properties are assumed to be the same on both sides of the shade.
Shades are considered to be perfect diffusers (all transmitted and reflected
radiation is hemispherically-diffuse) independent of angle of incidence."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Shade"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Assumed independent of incidence angle'})
    solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Assumed same for both sides Assumed independent of incidence angle'})
    visible_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Assumed independent of incidence angle'})
    visible_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'Assumed same for both sides Assumed independent of incidence angle'})
    infrared_hemispherical_emissivity: float = Field(..., gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless'})
    infrared_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless'})
    thickness: float = Field(..., gt=0.0, json_schema_extra={'units': 'm'})
    conductivity: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m-K'})
    shade_to_glass_distance: float | None = Field(default=0.05, ge=0.001, le=1.0, json_schema_extra={'units': 'm'})
    top_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    bottom_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    left_side_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    right_side_opening_multiplier: float | None = Field(default=0.5, ge=0.0, le=1.0)
    airflow_permeability: float | None = Field(default=0.0, ge=0.0, le=0.8, json_schema_extra={'units': 'dimensionless'})


class WindowMaterialShadeEquivalentLayer(IDFBaseModel):
    """Specifies the properties of equivalent layer window shade material Shades
are considered to be perfect diffusers (all transmitted and reflected
radiation is hemispherically-diffuse) independent of angle of incidence.
Shade represents roller blinds."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:Shade:EquivalentLayer"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    shade_beam_beam_solar_transmittance: float | None = Field(default=0.0, ge=0.0, le=0.8, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam solar transmittance at normal incidence. This value is the same as the openness area fraction of the shade material. Assumed to be the same for front and back sides.'})
    front_side_shade_beam_diffuse_solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar transmittance at normal incidence averaged over the entire spectrum of solar radiation.'})
    back_side_shade_beam_diffuse_solar_transmittance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar transmittance at normal incidence averaged over the entire spectrum of solar radiation.'})
    front_side_shade_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side beam-diffuse solar reflectance at normal incidence averaged over the entire spectrum of solar radiation.'})
    back_side_shade_beam_diffuse_solar_reflectance: float = Field(..., ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side beam-diffuse solar reflectance at normal incidence averaged over the entire spectrum of solar radiation.'})
    shade_beam_beam_visible_transmittance_at_normal_incidence: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-beam visible transmittance at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for front and back sides of the shade.'})
    shade_beam_diffuse_visible_transmittance_at_normal_incidence: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse visible transmittance at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for front and back sides of the shade.'})
    shade_beam_diffuse_visible_reflectance_at_normal_incidence: float | None = Field(default=None, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The beam-diffuse visible reflectance at normal incidence averaged over the visible spectrum range of solar radiation. Assumed to be the same for front and back sides of the shade.'})
    shade_material_infrared_transmittance: float | None = Field(default=0.05, ge=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The long-wave transmittance of the shade material at zero shade openness. Assumed to be the same for front and back sides of the shade.'})
    front_side_shade_material_infrared_emissivity: float | None = Field(default=0.91, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The front side long-wave emissivity of the shade material at zero shade openness. Openness fraction is used to calculate the effective emissivity value.'})
    back_side_shade_material_infrared_emissivity: float | None = Field(default=0.91, gt=0.0, lt=1.0, json_schema_extra={'units': 'dimensionless', 'note': 'The back side long-wave emissivity of the shade material at zero shade openness. Openness fraction is used to calculate the effective emissivity value.'})


class WindowMaterialSimpleGlazingSystem(IDFBaseModel):
    """Alternate method of describing windows This window material object is used
to define an entire glazing system using simple performance parameters."""

    _idf_object_type: ClassVar[str] = "WindowMaterial:SimpleGlazingSystem"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    u_factor: float = Field(..., gt=0.0, json_schema_extra={'units': 'W/m2-K', 'note': 'Enter U-Factor including film coefficients'})
    solar_heat_gain_coefficient: float = Field(..., gt=0.0, lt=1.0, json_schema_extra={'note': 'SHGC at Normal Incidence'})
    visible_transmittance: float | None = Field(default=None, gt=0.0, lt=1.0, json_schema_extra={'note': 'VT at Normal Incidence optional'})


class WindowThermalModelParams(IDFBaseModel):
    """object is used to select which thermal model should be used in tarcog
simulations"""

    _idf_object_type: ClassVar[str] = "WindowThermalModel:Params"
    _provider_fields: ClassVar[frozenset[str]] = frozenset({"name"})
    name: str = Field(...)
    standard: Literal['', 'EN673Declared', 'EN673Design', 'ISO15099'] | None = Field(default='ISO15099')
    thermal_model: Literal['', 'ConvectiveScalarModel_NoSDThickness', 'ConvectiveScalarModel_withSDThickness', 'ISO15099', 'ScaledCavityWidth'] | None = Field(default='ISO15099')
    sdscalar: float | None = Field(default=1.0, ge=0.0, le=1.0)
    deflection_model: Literal['', 'MeasuredDeflection', 'NoDeflection', 'TemperatureAndPressureInput'] | None = Field(default='NoDeflection')
    vacuum_pressure_limit: float | None = Field(default=13.238, gt=0.0, json_schema_extra={'units': 'Pa'})
    initial_temperature: float | None = Field(default=25.0, gt=0.0, json_schema_extra={'units': 'C', 'note': 'This is temperature in time of window fabrication'})
    initial_pressure: float | None = Field(default=101325.0, gt=0.0, json_schema_extra={'units': 'Pa', 'note': 'This is pressure in time of window fabrication'})


class WindowsCalculationEngine(IDFBaseModel):
    """Describes which window model will be used in calculations. Built in windows
model will use algorithms that are part of EnergyPlus, while
ExternalWindowsModel will use Windows-CalcEngine library to perform optical
and thermal performances of windows and doors."""

    _idf_object_type: ClassVar[str] = "WindowsCalculationEngine"
    windows_engine: Literal['', 'BuiltInWindowsModel', 'ExternalWindowsModel'] | None = Field(default='BuiltInWindowsModel')

