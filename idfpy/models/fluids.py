"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Fluid Properties
"""

from __future__ import annotations

from typing import Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    FluidAndGlycolNamesRef,
    FluidNamesRef,
    FluidPropertyTemperaturesRef,
)


class FluidPropertiesConcentration(IDFBaseModel):
    """fluid properties for water/other fluid mixtures"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:Concentration'
    fluid_name: FluidNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidNames'],
            'note': 'should not be any of the defaults (Water, EthyleneGlycol, or PropyleneGlycol)',
        },
    )
    fluid_property_type: (
        Literal['Conductivity', 'Density', 'SpecificHeat', 'Viscosity'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Density Units are kg/m3 SpecificHeat Units are J/kg-K Conductivity Units are W/m-K Viscosity Units are N-s/m2'
        },
    )
    temperature_values_name: FluidPropertyTemperaturesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidPropertyTemperatures'],
            'note': 'Enter the name of a FluidProperties:Temperatures object.',
        },
    )
    concentration: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'units': 'dimensionless',
            'note': 'Glycol concentration for this list of properties entered as a fraction',
        },
    )
    property_value_1: float | None = Field(default=None)
    property_value_2: float | None = Field(default=None)
    property_value_3: float | None = Field(default=None)
    property_value_4: float | None = Field(default=None)
    property_value_5: float | None = Field(default=None)
    property_value_6: float | None = Field(default=None)
    property_value_7: float | None = Field(default=None)
    property_value_8: float | None = Field(default=None)
    property_value_9: float | None = Field(default=None)
    property_value_10: float | None = Field(default=None)
    property_value_11: float | None = Field(default=None)
    property_value_12: float | None = Field(default=None)
    property_value_13: float | None = Field(default=None)
    property_value_14: float | None = Field(default=None)
    property_value_15: float | None = Field(default=None)
    property_value_16: float | None = Field(default=None)
    property_value_17: float | None = Field(default=None)
    property_value_18: float | None = Field(default=None)
    property_value_19: float | None = Field(default=None)
    property_value_20: float | None = Field(default=None)
    property_value_21: float | None = Field(default=None)
    property_value_22: float | None = Field(default=None)
    property_value_23: float | None = Field(default=None)
    property_value_24: float | None = Field(default=None)
    property_value_25: float | None = Field(default=None)
    property_value_26: float | None = Field(default=None)
    property_value_27: float | None = Field(default=None)
    property_value_28: float | None = Field(default=None)
    property_value_29: float | None = Field(default=None)
    property_value_30: float | None = Field(default=None)
    property_value_31: float | None = Field(default=None)
    property_value_32: float | None = Field(default=None)
    property_value_33: float | None = Field(default=None)
    property_value_34: float | None = Field(default=None)
    property_value_35: float | None = Field(default=None)
    property_value_36: float | None = Field(default=None)
    property_value_37: float | None = Field(default=None)
    property_value_38: float | None = Field(default=None)
    property_value_39: float | None = Field(default=None)
    property_value_40: float | None = Field(default=None)
    property_value_41: float | None = Field(default=None)
    property_value_42: float | None = Field(default=None)
    property_value_43: float | None = Field(default=None)
    property_value_44: float | None = Field(default=None)
    property_value_45: float | None = Field(default=None)
    property_value_46: float | None = Field(default=None)
    property_value_47: float | None = Field(default=None)
    property_value_48: float | None = Field(default=None)
    property_value_49: float | None = Field(default=None)
    property_value_50: float | None = Field(default=None)
    property_value_51: float | None = Field(default=None)
    property_value_52: float | None = Field(default=None)
    property_value_53: float | None = Field(default=None)
    property_value_54: float | None = Field(default=None)
    property_value_55: float | None = Field(default=None)
    property_value_56: float | None = Field(default=None)
    property_value_57: float | None = Field(default=None)
    property_value_58: float | None = Field(default=None)
    property_value_59: float | None = Field(default=None)
    property_value_60: float | None = Field(default=None)
    property_value_61: float | None = Field(default=None)
    property_value_62: float | None = Field(default=None)
    property_value_63: float | None = Field(default=None)
    property_value_64: float | None = Field(default=None)
    property_value_65: float | None = Field(default=None)
    property_value_66: float | None = Field(default=None)
    property_value_67: float | None = Field(default=None)
    property_value_68: float | None = Field(default=None)
    property_value_69: float | None = Field(default=None)
    property_value_70: float | None = Field(default=None)
    property_value_71: float | None = Field(default=None)
    property_value_72: float | None = Field(default=None)
    property_value_73: float | None = Field(default=None)
    property_value_74: float | None = Field(default=None)
    property_value_75: float | None = Field(default=None)
    property_value_76: float | None = Field(default=None)
    property_value_77: float | None = Field(default=None)
    property_value_78: float | None = Field(default=None)
    property_value_79: float | None = Field(default=None)
    property_value_80: float | None = Field(default=None)
    property_value_81: float | None = Field(default=None)
    property_value_82: float | None = Field(default=None)
    property_value_83: float | None = Field(default=None)
    property_value_84: float | None = Field(default=None)
    property_value_85: float | None = Field(default=None)
    property_value_86: float | None = Field(default=None)
    property_value_87: float | None = Field(default=None)
    property_value_88: float | None = Field(default=None)
    property_value_89: float | None = Field(default=None)
    property_value_90: float | None = Field(default=None)
    property_value_91: float | None = Field(default=None)
    property_value_92: float | None = Field(default=None)
    property_value_93: float | None = Field(default=None)
    property_value_94: float | None = Field(default=None)
    property_value_95: float | None = Field(default=None)
    property_value_96: float | None = Field(default=None)
    property_value_97: float | None = Field(default=None)
    property_value_98: float | None = Field(default=None)
    property_value_99: float | None = Field(default=None)
    property_value_100: float | None = Field(default=None)
    property_value_101: float | None = Field(default=None)
    property_value_102: float | None = Field(default=None)
    property_value_103: float | None = Field(default=None)
    property_value_104: float | None = Field(default=None)
    property_value_105: float | None = Field(default=None)
    property_value_106: float | None = Field(default=None)
    property_value_107: float | None = Field(default=None)
    property_value_108: float | None = Field(default=None)
    property_value_109: float | None = Field(default=None)
    property_value_110: float | None = Field(default=None)
    property_value_111: float | None = Field(default=None)
    property_value_112: float | None = Field(default=None)
    property_value_113: float | None = Field(default=None)
    property_value_114: float | None = Field(default=None)
    property_value_115: float | None = Field(default=None)
    property_value_116: float | None = Field(default=None)
    property_value_117: float | None = Field(default=None)
    property_value_118: float | None = Field(default=None)
    property_value_119: float | None = Field(default=None)
    property_value_120: float | None = Field(default=None)
    property_value_121: float | None = Field(default=None)
    property_value_122: float | None = Field(default=None)
    property_value_123: float | None = Field(default=None)
    property_value_124: float | None = Field(default=None)
    property_value_125: float | None = Field(default=None)
    property_value_126: float | None = Field(default=None)
    property_value_127: float | None = Field(default=None)
    property_value_128: float | None = Field(default=None)
    property_value_129: float | None = Field(default=None)
    property_value_130: float | None = Field(default=None)
    property_value_131: float | None = Field(default=None)
    property_value_132: float | None = Field(default=None)
    property_value_133: float | None = Field(default=None)
    property_value_134: float | None = Field(default=None)
    property_value_135: float | None = Field(default=None)
    property_value_136: float | None = Field(default=None)
    property_value_137: float | None = Field(default=None)
    property_value_138: float | None = Field(default=None)
    property_value_139: float | None = Field(default=None)
    property_value_140: float | None = Field(default=None)
    property_value_141: float | None = Field(default=None)
    property_value_142: float | None = Field(default=None)
    property_value_143: float | None = Field(default=None)
    property_value_144: float | None = Field(default=None)
    property_value_145: float | None = Field(default=None)
    property_value_146: float | None = Field(default=None)
    property_value_147: float | None = Field(default=None)
    property_value_148: float | None = Field(default=None)
    property_value_149: float | None = Field(default=None)
    property_value_150: float | None = Field(default=None)
    property_value_151: float | None = Field(default=None)
    property_value_152: float | None = Field(default=None)
    property_value_153: float | None = Field(default=None)
    property_value_154: float | None = Field(default=None)
    property_value_155: float | None = Field(default=None)
    property_value_156: float | None = Field(default=None)
    property_value_157: float | None = Field(default=None)
    property_value_158: float | None = Field(default=None)
    property_value_159: float | None = Field(default=None)
    property_value_160: float | None = Field(default=None)
    property_value_161: float | None = Field(default=None)
    property_value_162: float | None = Field(default=None)
    property_value_163: float | None = Field(default=None)
    property_value_164: float | None = Field(default=None)
    property_value_165: float | None = Field(default=None)
    property_value_166: float | None = Field(default=None)
    property_value_167: float | None = Field(default=None)
    property_value_168: float | None = Field(default=None)
    property_value_169: float | None = Field(default=None)
    property_value_170: float | None = Field(default=None)
    property_value_171: float | None = Field(default=None)
    property_value_172: float | None = Field(default=None)
    property_value_173: float | None = Field(default=None)
    property_value_174: float | None = Field(default=None)
    property_value_175: float | None = Field(default=None)
    property_value_176: float | None = Field(default=None)
    property_value_177: float | None = Field(default=None)
    property_value_178: float | None = Field(default=None)
    property_value_179: float | None = Field(default=None)
    property_value_180: float | None = Field(default=None)
    property_value_181: float | None = Field(default=None)
    property_value_182: float | None = Field(default=None)
    property_value_183: float | None = Field(default=None)
    property_value_184: float | None = Field(default=None)
    property_value_185: float | None = Field(default=None)
    property_value_186: float | None = Field(default=None)
    property_value_187: float | None = Field(default=None)
    property_value_188: float | None = Field(default=None)
    property_value_189: float | None = Field(default=None)
    property_value_190: float | None = Field(default=None)
    property_value_191: float | None = Field(default=None)
    property_value_192: float | None = Field(default=None)
    property_value_193: float | None = Field(default=None)
    property_value_194: float | None = Field(default=None)
    property_value_195: float | None = Field(default=None)
    property_value_196: float | None = Field(default=None)
    property_value_197: float | None = Field(default=None)
    property_value_198: float | None = Field(default=None)
    property_value_199: float | None = Field(default=None)
    property_value_200: float | None = Field(default=None)
    property_value_201: float | None = Field(default=None)
    property_value_202: float | None = Field(default=None)
    property_value_203: float | None = Field(default=None)
    property_value_204: float | None = Field(default=None)
    property_value_205: float | None = Field(default=None)
    property_value_206: float | None = Field(default=None)
    property_value_207: float | None = Field(default=None)
    property_value_208: float | None = Field(default=None)
    property_value_209: float | None = Field(default=None)
    property_value_210: float | None = Field(default=None)
    property_value_211: float | None = Field(default=None)
    property_value_212: float | None = Field(default=None)
    property_value_213: float | None = Field(default=None)
    property_value_214: float | None = Field(default=None)
    property_value_215: float | None = Field(default=None)
    property_value_216: float | None = Field(default=None)
    property_value_217: float | None = Field(default=None)
    property_value_218: float | None = Field(default=None)
    property_value_219: float | None = Field(default=None)
    property_value_220: float | None = Field(default=None)
    property_value_221: float | None = Field(default=None)
    property_value_222: float | None = Field(default=None)
    property_value_223: float | None = Field(default=None)
    property_value_224: float | None = Field(default=None)
    property_value_225: float | None = Field(default=None)
    property_value_226: float | None = Field(default=None)
    property_value_227: float | None = Field(default=None)
    property_value_228: float | None = Field(default=None)
    property_value_229: float | None = Field(default=None)
    property_value_230: float | None = Field(default=None)
    property_value_231: float | None = Field(default=None)
    property_value_232: float | None = Field(default=None)
    property_value_233: float | None = Field(default=None)
    property_value_234: float | None = Field(default=None)
    property_value_235: float | None = Field(default=None)
    property_value_236: float | None = Field(default=None)
    property_value_237: float | None = Field(default=None)
    property_value_238: float | None = Field(default=None)
    property_value_239: float | None = Field(default=None)
    property_value_240: float | None = Field(default=None)
    property_value_241: float | None = Field(default=None)
    property_value_242: float | None = Field(default=None)
    property_value_243: float | None = Field(default=None)
    property_value_244: float | None = Field(default=None)
    property_value_245: float | None = Field(default=None)
    property_value_246: float | None = Field(default=None)
    property_value_247: float | None = Field(default=None)
    property_value_248: float | None = Field(default=None)
    property_value_249: float | None = Field(default=None)
    property_value_250: float | None = Field(default=None)


class FluidPropertiesGlycolConcentration(IDFBaseModel):
    """glycol and what concentration it is"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:GlycolConcentration'
    name: str = Field(...)
    glycol_type: Literal[
        'EthyleneGlycol', 'PropyleneGlycol', 'UserDefinedGlycolType'
    ] = Field(
        ...,
        json_schema_extra={
            'note': 'or UserDefined Fluid (must show up as a glycol in FluidProperties:Name object)'
        },
    )
    user_defined_glycol_name: FluidAndGlycolNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['FluidAndGlycolNames']}
    )
    glycol_concentration: float | None = Field(default=None, ge=0.0, le=1.0)


class FluidPropertiesName(IDFBaseModel):
    """potential fluid name/type in the input file repeat this object for each
    fluid"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:Name'
    fluid_name: str = Field(...)
    fluid_type: Literal['Glycol', 'Refrigerant'] = Field(...)


class FluidPropertiesSaturated(IDFBaseModel):
    """fluid properties for the saturated region"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:Saturated'
    fluid_name: FluidNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['FluidNames']}
    )
    fluid_property_type: (
        Literal['Density', 'Enthalpy', 'Pressure', 'SpecificHeat'] | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'Enthalpy Units are J/kg Density Units are kg/m3 SpecificHeat Units are J/kg-K Pressure Units are Pa'
        },
    )
    fluid_phase: Literal['Fluid', 'FluidGas'] | None = Field(
        default=None,
        json_schema_extra={'note': 'Fluid=saturated fluid FluidGas=saturated vapor'},
    )
    temperature_values_name: FluidPropertyTemperaturesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidPropertyTemperatures'],
            'note': 'Enter the name of a FluidProperties:Temperatures object.',
        },
    )
    property_value_1: float | None = Field(default=None)
    property_value_2: float | None = Field(default=None)
    property_value_3: float | None = Field(default=None)
    property_value_4: float | None = Field(default=None)
    property_value_5: float | None = Field(default=None)
    property_value_6: float | None = Field(default=None)
    property_value_7: float | None = Field(default=None)
    property_value_8: float | None = Field(default=None)
    property_value_9: float | None = Field(default=None)
    property_value_10: float | None = Field(default=None)
    property_value_11: float | None = Field(default=None)
    property_value_12: float | None = Field(default=None)
    property_value_13: float | None = Field(default=None)
    property_value_14: float | None = Field(default=None)
    property_value_15: float | None = Field(default=None)
    property_value_16: float | None = Field(default=None)
    property_value_17: float | None = Field(default=None)
    property_value_18: float | None = Field(default=None)
    property_value_19: float | None = Field(default=None)
    property_value_20: float | None = Field(default=None)
    property_value_21: float | None = Field(default=None)
    property_value_22: float | None = Field(default=None)
    property_value_23: float | None = Field(default=None)
    property_value_24: float | None = Field(default=None)
    property_value_25: float | None = Field(default=None)
    property_value_26: float | None = Field(default=None)
    property_value_27: float | None = Field(default=None)
    property_value_28: float | None = Field(default=None)
    property_value_29: float | None = Field(default=None)
    property_value_30: float | None = Field(default=None)
    property_value_31: float | None = Field(default=None)
    property_value_32: float | None = Field(default=None)
    property_value_33: float | None = Field(default=None)
    property_value_34: float | None = Field(default=None)
    property_value_35: float | None = Field(default=None)
    property_value_36: float | None = Field(default=None)
    property_value_37: float | None = Field(default=None)
    property_value_38: float | None = Field(default=None)
    property_value_39: float | None = Field(default=None)
    property_value_40: float | None = Field(default=None)
    property_value_41: float | None = Field(default=None)
    property_value_42: float | None = Field(default=None)
    property_value_43: float | None = Field(default=None)
    property_value_44: float | None = Field(default=None)
    property_value_45: float | None = Field(default=None)
    property_value_46: float | None = Field(default=None)
    property_value_47: float | None = Field(default=None)
    property_value_48: float | None = Field(default=None)
    property_value_49: float | None = Field(default=None)
    property_value_50: float | None = Field(default=None)
    property_value_51: float | None = Field(default=None)
    property_value_52: float | None = Field(default=None)
    property_value_53: float | None = Field(default=None)
    property_value_54: float | None = Field(default=None)
    property_value_55: float | None = Field(default=None)
    property_value_56: float | None = Field(default=None)
    property_value_57: float | None = Field(default=None)
    property_value_58: float | None = Field(default=None)
    property_value_59: float | None = Field(default=None)
    property_value_60: float | None = Field(default=None)
    property_value_61: float | None = Field(default=None)
    property_value_62: float | None = Field(default=None)
    property_value_63: float | None = Field(default=None)
    property_value_64: float | None = Field(default=None)
    property_value_65: float | None = Field(default=None)
    property_value_66: float | None = Field(default=None)
    property_value_67: float | None = Field(default=None)
    property_value_68: float | None = Field(default=None)
    property_value_69: float | None = Field(default=None)
    property_value_70: float | None = Field(default=None)
    property_value_71: float | None = Field(default=None)
    property_value_72: float | None = Field(default=None)
    property_value_73: float | None = Field(default=None)
    property_value_74: float | None = Field(default=None)
    property_value_75: float | None = Field(default=None)
    property_value_76: float | None = Field(default=None)
    property_value_77: float | None = Field(default=None)
    property_value_78: float | None = Field(default=None)
    property_value_79: float | None = Field(default=None)
    property_value_80: float | None = Field(default=None)
    property_value_81: float | None = Field(default=None)
    property_value_82: float | None = Field(default=None)
    property_value_83: float | None = Field(default=None)
    property_value_84: float | None = Field(default=None)
    property_value_85: float | None = Field(default=None)
    property_value_86: float | None = Field(default=None)
    property_value_87: float | None = Field(default=None)
    property_value_88: float | None = Field(default=None)
    property_value_89: float | None = Field(default=None)
    property_value_90: float | None = Field(default=None)
    property_value_91: float | None = Field(default=None)
    property_value_92: float | None = Field(default=None)
    property_value_93: float | None = Field(default=None)
    property_value_94: float | None = Field(default=None)
    property_value_95: float | None = Field(default=None)
    property_value_96: float | None = Field(default=None)
    property_value_97: float | None = Field(default=None)
    property_value_98: float | None = Field(default=None)
    property_value_99: float | None = Field(default=None)
    property_value_100: float | None = Field(default=None)
    property_value_101: float | None = Field(default=None)
    property_value_102: float | None = Field(default=None)
    property_value_103: float | None = Field(default=None)
    property_value_104: float | None = Field(default=None)
    property_value_105: float | None = Field(default=None)
    property_value_106: float | None = Field(default=None)
    property_value_107: float | None = Field(default=None)
    property_value_108: float | None = Field(default=None)
    property_value_109: float | None = Field(default=None)
    property_value_110: float | None = Field(default=None)
    property_value_111: float | None = Field(default=None)
    property_value_112: float | None = Field(default=None)
    property_value_113: float | None = Field(default=None)
    property_value_114: float | None = Field(default=None)
    property_value_115: float | None = Field(default=None)
    property_value_116: float | None = Field(default=None)
    property_value_117: float | None = Field(default=None)
    property_value_118: float | None = Field(default=None)
    property_value_119: float | None = Field(default=None)
    property_value_120: float | None = Field(default=None)
    property_value_121: float | None = Field(default=None)
    property_value_122: float | None = Field(default=None)
    property_value_123: float | None = Field(default=None)
    property_value_124: float | None = Field(default=None)
    property_value_125: float | None = Field(default=None)
    property_value_126: float | None = Field(default=None)
    property_value_127: float | None = Field(default=None)
    property_value_128: float | None = Field(default=None)
    property_value_129: float | None = Field(default=None)
    property_value_130: float | None = Field(default=None)
    property_value_131: float | None = Field(default=None)
    property_value_132: float | None = Field(default=None)
    property_value_133: float | None = Field(default=None)
    property_value_134: float | None = Field(default=None)
    property_value_135: float | None = Field(default=None)
    property_value_136: float | None = Field(default=None)
    property_value_137: float | None = Field(default=None)
    property_value_138: float | None = Field(default=None)
    property_value_139: float | None = Field(default=None)
    property_value_140: float | None = Field(default=None)
    property_value_141: float | None = Field(default=None)
    property_value_142: float | None = Field(default=None)
    property_value_143: float | None = Field(default=None)
    property_value_144: float | None = Field(default=None)
    property_value_145: float | None = Field(default=None)
    property_value_146: float | None = Field(default=None)
    property_value_147: float | None = Field(default=None)
    property_value_148: float | None = Field(default=None)
    property_value_149: float | None = Field(default=None)
    property_value_150: float | None = Field(default=None)
    property_value_151: float | None = Field(default=None)
    property_value_152: float | None = Field(default=None)
    property_value_153: float | None = Field(default=None)
    property_value_154: float | None = Field(default=None)
    property_value_155: float | None = Field(default=None)
    property_value_156: float | None = Field(default=None)
    property_value_157: float | None = Field(default=None)
    property_value_158: float | None = Field(default=None)
    property_value_159: float | None = Field(default=None)
    property_value_160: float | None = Field(default=None)
    property_value_161: float | None = Field(default=None)
    property_value_162: float | None = Field(default=None)
    property_value_163: float | None = Field(default=None)
    property_value_164: float | None = Field(default=None)
    property_value_165: float | None = Field(default=None)
    property_value_166: float | None = Field(default=None)
    property_value_167: float | None = Field(default=None)
    property_value_168: float | None = Field(default=None)
    property_value_169: float | None = Field(default=None)
    property_value_170: float | None = Field(default=None)
    property_value_171: float | None = Field(default=None)
    property_value_172: float | None = Field(default=None)
    property_value_173: float | None = Field(default=None)
    property_value_174: float | None = Field(default=None)
    property_value_175: float | None = Field(default=None)
    property_value_176: float | None = Field(default=None)
    property_value_177: float | None = Field(default=None)
    property_value_178: float | None = Field(default=None)
    property_value_179: float | None = Field(default=None)
    property_value_180: float | None = Field(default=None)
    property_value_181: float | None = Field(default=None)
    property_value_182: float | None = Field(default=None)
    property_value_183: float | None = Field(default=None)
    property_value_184: float | None = Field(default=None)
    property_value_185: float | None = Field(default=None)
    property_value_186: float | None = Field(default=None)
    property_value_187: float | None = Field(default=None)
    property_value_188: float | None = Field(default=None)
    property_value_189: float | None = Field(default=None)
    property_value_190: float | None = Field(default=None)
    property_value_191: float | None = Field(default=None)
    property_value_192: float | None = Field(default=None)
    property_value_193: float | None = Field(default=None)
    property_value_194: float | None = Field(default=None)
    property_value_195: float | None = Field(default=None)
    property_value_196: float | None = Field(default=None)
    property_value_197: float | None = Field(default=None)
    property_value_198: float | None = Field(default=None)
    property_value_199: float | None = Field(default=None)
    property_value_200: float | None = Field(default=None)
    property_value_201: float | None = Field(default=None)
    property_value_202: float | None = Field(default=None)
    property_value_203: float | None = Field(default=None)
    property_value_204: float | None = Field(default=None)
    property_value_205: float | None = Field(default=None)
    property_value_206: float | None = Field(default=None)
    property_value_207: float | None = Field(default=None)
    property_value_208: float | None = Field(default=None)
    property_value_209: float | None = Field(default=None)
    property_value_210: float | None = Field(default=None)
    property_value_211: float | None = Field(default=None)
    property_value_212: float | None = Field(default=None)
    property_value_213: float | None = Field(default=None)
    property_value_214: float | None = Field(default=None)
    property_value_215: float | None = Field(default=None)
    property_value_216: float | None = Field(default=None)
    property_value_217: float | None = Field(default=None)
    property_value_218: float | None = Field(default=None)
    property_value_219: float | None = Field(default=None)
    property_value_220: float | None = Field(default=None)
    property_value_221: float | None = Field(default=None)
    property_value_222: float | None = Field(default=None)
    property_value_223: float | None = Field(default=None)
    property_value_224: float | None = Field(default=None)
    property_value_225: float | None = Field(default=None)
    property_value_226: float | None = Field(default=None)
    property_value_227: float | None = Field(default=None)
    property_value_228: float | None = Field(default=None)
    property_value_229: float | None = Field(default=None)
    property_value_230: float | None = Field(default=None)
    property_value_231: float | None = Field(default=None)
    property_value_232: float | None = Field(default=None)
    property_value_233: float | None = Field(default=None)
    property_value_234: float | None = Field(default=None)
    property_value_235: float | None = Field(default=None)
    property_value_236: float | None = Field(default=None)
    property_value_237: float | None = Field(default=None)
    property_value_238: float | None = Field(default=None)
    property_value_239: float | None = Field(default=None)
    property_value_240: float | None = Field(default=None)
    property_value_241: float | None = Field(default=None)
    property_value_242: float | None = Field(default=None)
    property_value_243: float | None = Field(default=None)
    property_value_244: float | None = Field(default=None)
    property_value_245: float | None = Field(default=None)
    property_value_246: float | None = Field(default=None)
    property_value_247: float | None = Field(default=None)
    property_value_248: float | None = Field(default=None)
    property_value_249: float | None = Field(default=None)
    property_value_250: float | None = Field(default=None)


class FluidPropertiesSuperheated(IDFBaseModel):
    """fluid properties for the superheated region"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:Superheated'
    fluid_name: FluidNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['FluidNames']}
    )
    fluid_property_type: Literal['Density', 'Enthalpy'] | None = Field(
        default=None,
        json_schema_extra={'note': 'Enthalpy Units are J/kg Density Units are kg/m3'},
    )
    temperature_values_name: FluidPropertyTemperaturesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['FluidPropertyTemperatures'],
            'note': 'Enter the name of a FluidProperties:Temperatures object.',
        },
    )
    pressure: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'Pa',
            'note': 'pressure for this list of properties',
        },
    )
    property_value_1: float | None = Field(default=None)
    property_value_2: float | None = Field(default=None)
    property_value_3: float | None = Field(default=None)
    property_value_4: float | None = Field(default=None)
    property_value_5: float | None = Field(default=None)
    property_value_6: float | None = Field(default=None)
    property_value_7: float | None = Field(default=None)
    property_value_8: float | None = Field(default=None)
    property_value_9: float | None = Field(default=None)
    property_value_10: float | None = Field(default=None)
    property_value_11: float | None = Field(default=None)
    property_value_12: float | None = Field(default=None)
    property_value_13: float | None = Field(default=None)
    property_value_14: float | None = Field(default=None)
    property_value_15: float | None = Field(default=None)
    property_value_16: float | None = Field(default=None)
    property_value_17: float | None = Field(default=None)
    property_value_18: float | None = Field(default=None)
    property_value_19: float | None = Field(default=None)
    property_value_20: float | None = Field(default=None)
    property_value_21: float | None = Field(default=None)
    property_value_22: float | None = Field(default=None)
    property_value_23: float | None = Field(default=None)
    property_value_24: float | None = Field(default=None)
    property_value_25: float | None = Field(default=None)
    property_value_26: float | None = Field(default=None)
    property_value_27: float | None = Field(default=None)
    property_value_28: float | None = Field(default=None)
    property_value_29: float | None = Field(default=None)
    property_value_30: float | None = Field(default=None)
    property_value_31: float | None = Field(default=None)
    property_value_32: float | None = Field(default=None)
    property_value_33: float | None = Field(default=None)
    property_value_34: float | None = Field(default=None)
    property_value_35: float | None = Field(default=None)
    property_value_36: float | None = Field(default=None)
    property_value_37: float | None = Field(default=None)
    property_value_38: float | None = Field(default=None)
    property_value_39: float | None = Field(default=None)
    property_value_40: float | None = Field(default=None)
    property_value_41: float | None = Field(default=None)
    property_value_42: float | None = Field(default=None)
    property_value_43: float | None = Field(default=None)
    property_value_44: float | None = Field(default=None)
    property_value_45: float | None = Field(default=None)
    property_value_46: float | None = Field(default=None)
    property_value_47: float | None = Field(default=None)
    property_value_48: float | None = Field(default=None)
    property_value_49: float | None = Field(default=None)
    property_value_50: float | None = Field(default=None)
    property_value_51: float | None = Field(default=None)
    property_value_52: float | None = Field(default=None)
    property_value_53: float | None = Field(default=None)
    property_value_54: float | None = Field(default=None)
    property_value_55: float | None = Field(default=None)
    property_value_56: float | None = Field(default=None)
    property_value_57: float | None = Field(default=None)
    property_value_58: float | None = Field(default=None)
    property_value_59: float | None = Field(default=None)
    property_value_60: float | None = Field(default=None)
    property_value_61: float | None = Field(default=None)
    property_value_62: float | None = Field(default=None)
    property_value_63: float | None = Field(default=None)
    property_value_64: float | None = Field(default=None)
    property_value_65: float | None = Field(default=None)
    property_value_66: float | None = Field(default=None)
    property_value_67: float | None = Field(default=None)
    property_value_68: float | None = Field(default=None)
    property_value_69: float | None = Field(default=None)
    property_value_70: float | None = Field(default=None)
    property_value_71: float | None = Field(default=None)
    property_value_72: float | None = Field(default=None)
    property_value_73: float | None = Field(default=None)
    property_value_74: float | None = Field(default=None)
    property_value_75: float | None = Field(default=None)
    property_value_76: float | None = Field(default=None)
    property_value_77: float | None = Field(default=None)
    property_value_78: float | None = Field(default=None)
    property_value_79: float | None = Field(default=None)
    property_value_80: float | None = Field(default=None)
    property_value_81: float | None = Field(default=None)
    property_value_82: float | None = Field(default=None)
    property_value_83: float | None = Field(default=None)
    property_value_84: float | None = Field(default=None)
    property_value_85: float | None = Field(default=None)
    property_value_86: float | None = Field(default=None)
    property_value_87: float | None = Field(default=None)
    property_value_88: float | None = Field(default=None)
    property_value_89: float | None = Field(default=None)
    property_value_90: float | None = Field(default=None)
    property_value_91: float | None = Field(default=None)
    property_value_92: float | None = Field(default=None)
    property_value_93: float | None = Field(default=None)
    property_value_94: float | None = Field(default=None)
    property_value_95: float | None = Field(default=None)
    property_value_96: float | None = Field(default=None)
    property_value_97: float | None = Field(default=None)
    property_value_98: float | None = Field(default=None)
    property_value_99: float | None = Field(default=None)
    property_value_100: float | None = Field(default=None)
    property_value_101: float | None = Field(default=None)
    property_value_102: float | None = Field(default=None)
    property_value_103: float | None = Field(default=None)
    property_value_104: float | None = Field(default=None)
    property_value_105: float | None = Field(default=None)
    property_value_106: float | None = Field(default=None)
    property_value_107: float | None = Field(default=None)
    property_value_108: float | None = Field(default=None)
    property_value_109: float | None = Field(default=None)
    property_value_110: float | None = Field(default=None)
    property_value_111: float | None = Field(default=None)
    property_value_112: float | None = Field(default=None)
    property_value_113: float | None = Field(default=None)
    property_value_114: float | None = Field(default=None)
    property_value_115: float | None = Field(default=None)
    property_value_116: float | None = Field(default=None)
    property_value_117: float | None = Field(default=None)
    property_value_118: float | None = Field(default=None)
    property_value_119: float | None = Field(default=None)
    property_value_120: float | None = Field(default=None)
    property_value_121: float | None = Field(default=None)
    property_value_122: float | None = Field(default=None)
    property_value_123: float | None = Field(default=None)
    property_value_124: float | None = Field(default=None)
    property_value_125: float | None = Field(default=None)
    property_value_126: float | None = Field(default=None)
    property_value_127: float | None = Field(default=None)
    property_value_128: float | None = Field(default=None)
    property_value_129: float | None = Field(default=None)
    property_value_130: float | None = Field(default=None)
    property_value_131: float | None = Field(default=None)
    property_value_132: float | None = Field(default=None)
    property_value_133: float | None = Field(default=None)
    property_value_134: float | None = Field(default=None)
    property_value_135: float | None = Field(default=None)
    property_value_136: float | None = Field(default=None)
    property_value_137: float | None = Field(default=None)
    property_value_138: float | None = Field(default=None)
    property_value_139: float | None = Field(default=None)
    property_value_140: float | None = Field(default=None)
    property_value_141: float | None = Field(default=None)
    property_value_142: float | None = Field(default=None)
    property_value_143: float | None = Field(default=None)
    property_value_144: float | None = Field(default=None)
    property_value_145: float | None = Field(default=None)
    property_value_146: float | None = Field(default=None)
    property_value_147: float | None = Field(default=None)
    property_value_148: float | None = Field(default=None)
    property_value_149: float | None = Field(default=None)
    property_value_150: float | None = Field(default=None)
    property_value_151: float | None = Field(default=None)
    property_value_152: float | None = Field(default=None)
    property_value_153: float | None = Field(default=None)
    property_value_154: float | None = Field(default=None)
    property_value_155: float | None = Field(default=None)
    property_value_156: float | None = Field(default=None)
    property_value_157: float | None = Field(default=None)
    property_value_158: float | None = Field(default=None)
    property_value_159: float | None = Field(default=None)
    property_value_160: float | None = Field(default=None)
    property_value_161: float | None = Field(default=None)
    property_value_162: float | None = Field(default=None)
    property_value_163: float | None = Field(default=None)
    property_value_164: float | None = Field(default=None)
    property_value_165: float | None = Field(default=None)
    property_value_166: float | None = Field(default=None)
    property_value_167: float | None = Field(default=None)
    property_value_168: float | None = Field(default=None)
    property_value_169: float | None = Field(default=None)
    property_value_170: float | None = Field(default=None)
    property_value_171: float | None = Field(default=None)
    property_value_172: float | None = Field(default=None)
    property_value_173: float | None = Field(default=None)
    property_value_174: float | None = Field(default=None)
    property_value_175: float | None = Field(default=None)
    property_value_176: float | None = Field(default=None)
    property_value_177: float | None = Field(default=None)
    property_value_178: float | None = Field(default=None)
    property_value_179: float | None = Field(default=None)
    property_value_180: float | None = Field(default=None)
    property_value_181: float | None = Field(default=None)
    property_value_182: float | None = Field(default=None)
    property_value_183: float | None = Field(default=None)
    property_value_184: float | None = Field(default=None)
    property_value_185: float | None = Field(default=None)
    property_value_186: float | None = Field(default=None)
    property_value_187: float | None = Field(default=None)
    property_value_188: float | None = Field(default=None)
    property_value_189: float | None = Field(default=None)
    property_value_190: float | None = Field(default=None)
    property_value_191: float | None = Field(default=None)
    property_value_192: float | None = Field(default=None)
    property_value_193: float | None = Field(default=None)
    property_value_194: float | None = Field(default=None)
    property_value_195: float | None = Field(default=None)
    property_value_196: float | None = Field(default=None)
    property_value_197: float | None = Field(default=None)
    property_value_198: float | None = Field(default=None)
    property_value_199: float | None = Field(default=None)
    property_value_200: float | None = Field(default=None)
    property_value_201: float | None = Field(default=None)
    property_value_202: float | None = Field(default=None)
    property_value_203: float | None = Field(default=None)
    property_value_204: float | None = Field(default=None)
    property_value_205: float | None = Field(default=None)
    property_value_206: float | None = Field(default=None)
    property_value_207: float | None = Field(default=None)
    property_value_208: float | None = Field(default=None)
    property_value_209: float | None = Field(default=None)
    property_value_210: float | None = Field(default=None)
    property_value_211: float | None = Field(default=None)
    property_value_212: float | None = Field(default=None)
    property_value_213: float | None = Field(default=None)
    property_value_214: float | None = Field(default=None)
    property_value_215: float | None = Field(default=None)
    property_value_216: float | None = Field(default=None)
    property_value_217: float | None = Field(default=None)
    property_value_218: float | None = Field(default=None)
    property_value_219: float | None = Field(default=None)
    property_value_220: float | None = Field(default=None)
    property_value_221: float | None = Field(default=None)
    property_value_222: float | None = Field(default=None)
    property_value_223: float | None = Field(default=None)
    property_value_224: float | None = Field(default=None)
    property_value_225: float | None = Field(default=None)
    property_value_226: float | None = Field(default=None)
    property_value_227: float | None = Field(default=None)
    property_value_228: float | None = Field(default=None)
    property_value_229: float | None = Field(default=None)
    property_value_230: float | None = Field(default=None)
    property_value_231: float | None = Field(default=None)
    property_value_232: float | None = Field(default=None)
    property_value_233: float | None = Field(default=None)
    property_value_234: float | None = Field(default=None)
    property_value_235: float | None = Field(default=None)
    property_value_236: float | None = Field(default=None)
    property_value_237: float | None = Field(default=None)
    property_value_238: float | None = Field(default=None)
    property_value_239: float | None = Field(default=None)
    property_value_240: float | None = Field(default=None)
    property_value_241: float | None = Field(default=None)
    property_value_242: float | None = Field(default=None)
    property_value_243: float | None = Field(default=None)
    property_value_244: float | None = Field(default=None)
    property_value_245: float | None = Field(default=None)
    property_value_246: float | None = Field(default=None)
    property_value_247: float | None = Field(default=None)
    property_value_248: float | None = Field(default=None)
    property_value_249: float | None = Field(default=None)
    property_value_250: float | None = Field(default=None)


class FluidPropertiesTemperatures(IDFBaseModel):
    """property values for fluid properties list of up to 250 temperatures, note
    that number of property values must match the number of properties in other
    words, there must be a one-to-one correspondence between the property values
    in this list and the actual properties list in other syntax degrees C (for
    all temperature inputs)"""

    _idf_object_type: ClassVar[str] = 'FluidProperties:Temperatures'
    name: str | None = Field(default=None)
    temperature_1: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_2: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_3: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_4: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_5: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_6: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_7: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_8: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_9: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_10: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_11: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_12: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_13: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_14: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_15: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_16: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_17: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_18: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_19: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_20: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_21: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_22: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_23: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_24: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_25: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_26: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_27: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_28: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_29: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_30: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_31: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_32: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_33: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_34: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_35: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_36: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_37: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_38: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_39: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_40: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_41: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_42: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_43: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_44: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_45: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_46: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_47: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_48: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_49: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_50: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_51: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_52: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_53: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_54: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_55: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_56: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_57: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_58: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_59: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_60: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_61: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_62: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_63: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_64: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_65: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_66: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_67: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_68: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_69: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_70: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_71: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_72: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_73: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_74: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_75: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_76: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_77: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_78: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_79: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_80: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_81: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_82: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_83: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_84: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_85: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_86: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_87: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_88: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_89: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_90: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_91: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_92: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_93: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_94: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_95: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_96: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_97: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_98: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_99: float | None = Field(default=None, json_schema_extra={'units': 'C'})
    temperature_100: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_101: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_102: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_103: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_104: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_105: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_106: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_107: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_108: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_109: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_110: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_111: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_112: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_113: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_114: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_115: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_116: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_117: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_118: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_119: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_120: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_121: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_122: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_123: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_124: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_125: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_126: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_127: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_128: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_129: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_130: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_131: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_132: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_133: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_134: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_135: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_136: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_137: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_138: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_139: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_140: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_141: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_142: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_143: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_144: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_145: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_146: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_147: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_148: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_149: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_150: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_151: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_152: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_153: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_154: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_155: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_156: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_157: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_158: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_159: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_160: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_161: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_162: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_163: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_164: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_165: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_166: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_167: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_168: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_169: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_170: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_171: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_172: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_173: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_174: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_175: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_176: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_177: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_178: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_179: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_180: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_181: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_182: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_183: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_184: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_185: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_186: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_187: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_188: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_189: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_190: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_191: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_192: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_193: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_194: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_195: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_196: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_197: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_198: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_199: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_200: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_201: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_202: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_203: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_204: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_205: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_206: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_207: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_208: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_209: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_210: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_211: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_212: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_213: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_214: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_215: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_216: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_217: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_218: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_219: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_220: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_221: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_222: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_223: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_224: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_225: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_226: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_227: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_228: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_229: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_230: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_231: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_232: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_233: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_234: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_235: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_236: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_237: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_238: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_239: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_240: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_241: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_242: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_243: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_244: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_245: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_246: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_247: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_248: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_249: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
    temperature_250: float | None = Field(
        default=None, json_schema_extra={'units': 'C'}
    )
