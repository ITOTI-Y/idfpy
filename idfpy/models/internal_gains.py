"""Auto-generated EnergyPlus IDF models.

DO NOT EDIT MANUALLY.
Generated from Energy+.schema.epJSON version 25.1.
Group: Internal Gains
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, ClassVar, Literal  # noqa: F401

from pydantic import Field

from ._base import IDFBaseModel
from ._refs import (
    AllHeatTranAngFacNamesRef,
    AllHeatTranSurfNamesRef,
    BivariateFunctionsRef,
    FloorSurfaceNamesRef,
    RoomAirNodesRef,
    ScheduleNamesRef,
    SpaceAndSpaceListNamesRef,
    SpaceNamesRef,
    SurfaceNamesRef,
    SurfAndSubSurfNamesRef,
    UnivariateFunctionsRef,
    ZoneAndZoneListNamesRef,
    ZoneNamesRef,
)

if TYPE_CHECKING:
    from .room_air import RoomAirNode
    from .thermal_zones import (
        BuildingSurfaceDetailed,
        FloorAdiabatic,
        FloorDetailed,
        FloorGroundContact,
        FloorInterzone,
        Space,
        SpaceList,
        Zone,
        ZoneList,
    )


class ComfortViewFactorAngles(IDFBaseModel):
    """Used to specify radiant view factors for thermal comfort calculations. Note
    that the following angle factor fractions must sum up to 1.0 All surfaces
    must be in the same enclosure."""

    _idf_object_type: ClassVar[str] = 'ComfortViewFactorAngles'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str | None = Field(default=None)
    surface_1_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_1: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_2_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_2: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_3_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_3: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_4_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_4: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_5_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_5: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_6_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_6: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_7_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_7: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_8_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_8: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_9_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_9: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_10_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_10: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_11_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_11: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_12_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_12: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_13_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_13: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_14_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_14: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_15_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_15: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_16_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_16: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_17_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_17: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_18_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_18: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_19_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_19: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_20_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_20: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_21_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_21: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_22_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_22: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_23_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_23: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_24_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_24: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_25_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_25: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_26_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_26: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_27_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_27: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_28_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_28: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_29_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_29: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_30_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_30: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_31_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_31: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_32_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_32: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_33_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_33: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_34_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_34: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_35_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_35: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_36_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_36: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_37_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_37: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_38_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_38: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_39_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_39: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_40_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_40: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_41_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_41: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_42_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_42: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_43_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_43: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_44_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_44: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_45_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_45: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_46_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_46: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_47_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_47: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_48_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_48: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_49_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_49: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_50_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_50: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_51_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_51: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_52_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_52: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_53_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_53: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_54_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_54: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_55_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_55: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_56_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_56: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_57_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_57: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_58_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_58: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_59_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_59: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_60_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_60: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_61_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_61: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_62_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_62: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_63_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_63: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_64_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_64: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_65_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_65: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_66_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_66: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_67_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_67: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_68_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_68: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_69_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_69: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_70_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_70: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_71_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_71: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_72_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_72: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_73_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_73: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_74_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_74: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_75_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_75: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_76_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_76: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_77_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_77: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_78_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_78: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_79_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_79: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_80_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_80: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_81_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_81: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_82_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_82: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_83_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_83: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_84_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_84: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_85_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_85: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_86_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_86: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_87_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_87: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_88_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_88: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_89_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_89: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_90_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_90: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_91_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_91: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_92_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_92: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_93_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_93: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_94_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_94: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_95_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_95: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_96_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_96: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_97_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_97: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_98_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_98: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_99_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_99: float | None = Field(default=None, ge=0.0, le=1.0)
    surface_100_name: AllHeatTranSurfNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['AllHeatTranSurfNames']}
    )
    angle_factor_100: float | None = Field(default=None, ge=0.0, le=1.0)

    @property
    def surface_1(self) -> IDFBaseModel | None:
        v = self.surface_1_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_2(self) -> IDFBaseModel | None:
        v = self.surface_2_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_3(self) -> IDFBaseModel | None:
        v = self.surface_3_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_4(self) -> IDFBaseModel | None:
        v = self.surface_4_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_5(self) -> IDFBaseModel | None:
        v = self.surface_5_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_6(self) -> IDFBaseModel | None:
        v = self.surface_6_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_7(self) -> IDFBaseModel | None:
        v = self.surface_7_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_8(self) -> IDFBaseModel | None:
        v = self.surface_8_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_9(self) -> IDFBaseModel | None:
        v = self.surface_9_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_10(self) -> IDFBaseModel | None:
        v = self.surface_10_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_11(self) -> IDFBaseModel | None:
        v = self.surface_11_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_12(self) -> IDFBaseModel | None:
        v = self.surface_12_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_13(self) -> IDFBaseModel | None:
        v = self.surface_13_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_14(self) -> IDFBaseModel | None:
        v = self.surface_14_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_15(self) -> IDFBaseModel | None:
        v = self.surface_15_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_16(self) -> IDFBaseModel | None:
        v = self.surface_16_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_17(self) -> IDFBaseModel | None:
        v = self.surface_17_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_18(self) -> IDFBaseModel | None:
        v = self.surface_18_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_19(self) -> IDFBaseModel | None:
        v = self.surface_19_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_20(self) -> IDFBaseModel | None:
        v = self.surface_20_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_21(self) -> IDFBaseModel | None:
        v = self.surface_21_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_22(self) -> IDFBaseModel | None:
        v = self.surface_22_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_23(self) -> IDFBaseModel | None:
        v = self.surface_23_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_24(self) -> IDFBaseModel | None:
        v = self.surface_24_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_25(self) -> IDFBaseModel | None:
        v = self.surface_25_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_26(self) -> IDFBaseModel | None:
        v = self.surface_26_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_27(self) -> IDFBaseModel | None:
        v = self.surface_27_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_28(self) -> IDFBaseModel | None:
        v = self.surface_28_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_29(self) -> IDFBaseModel | None:
        v = self.surface_29_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_30(self) -> IDFBaseModel | None:
        v = self.surface_30_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_31(self) -> IDFBaseModel | None:
        v = self.surface_31_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_32(self) -> IDFBaseModel | None:
        v = self.surface_32_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_33(self) -> IDFBaseModel | None:
        v = self.surface_33_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_34(self) -> IDFBaseModel | None:
        v = self.surface_34_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_35(self) -> IDFBaseModel | None:
        v = self.surface_35_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_36(self) -> IDFBaseModel | None:
        v = self.surface_36_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_37(self) -> IDFBaseModel | None:
        v = self.surface_37_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_38(self) -> IDFBaseModel | None:
        v = self.surface_38_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_39(self) -> IDFBaseModel | None:
        v = self.surface_39_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_40(self) -> IDFBaseModel | None:
        v = self.surface_40_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_41(self) -> IDFBaseModel | None:
        v = self.surface_41_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_42(self) -> IDFBaseModel | None:
        v = self.surface_42_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_43(self) -> IDFBaseModel | None:
        v = self.surface_43_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_44(self) -> IDFBaseModel | None:
        v = self.surface_44_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_45(self) -> IDFBaseModel | None:
        v = self.surface_45_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_46(self) -> IDFBaseModel | None:
        v = self.surface_46_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_47(self) -> IDFBaseModel | None:
        v = self.surface_47_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_48(self) -> IDFBaseModel | None:
        v = self.surface_48_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_49(self) -> IDFBaseModel | None:
        v = self.surface_49_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_50(self) -> IDFBaseModel | None:
        v = self.surface_50_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_51(self) -> IDFBaseModel | None:
        v = self.surface_51_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_52(self) -> IDFBaseModel | None:
        v = self.surface_52_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_53(self) -> IDFBaseModel | None:
        v = self.surface_53_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_54(self) -> IDFBaseModel | None:
        v = self.surface_54_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_55(self) -> IDFBaseModel | None:
        v = self.surface_55_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_56(self) -> IDFBaseModel | None:
        v = self.surface_56_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_57(self) -> IDFBaseModel | None:
        v = self.surface_57_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_58(self) -> IDFBaseModel | None:
        v = self.surface_58_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_59(self) -> IDFBaseModel | None:
        v = self.surface_59_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_60(self) -> IDFBaseModel | None:
        v = self.surface_60_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_61(self) -> IDFBaseModel | None:
        v = self.surface_61_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_62(self) -> IDFBaseModel | None:
        v = self.surface_62_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_63(self) -> IDFBaseModel | None:
        v = self.surface_63_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_64(self) -> IDFBaseModel | None:
        v = self.surface_64_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_65(self) -> IDFBaseModel | None:
        v = self.surface_65_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_66(self) -> IDFBaseModel | None:
        v = self.surface_66_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_67(self) -> IDFBaseModel | None:
        v = self.surface_67_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_68(self) -> IDFBaseModel | None:
        v = self.surface_68_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_69(self) -> IDFBaseModel | None:
        v = self.surface_69_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_70(self) -> IDFBaseModel | None:
        v = self.surface_70_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_71(self) -> IDFBaseModel | None:
        v = self.surface_71_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_72(self) -> IDFBaseModel | None:
        v = self.surface_72_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_73(self) -> IDFBaseModel | None:
        v = self.surface_73_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_74(self) -> IDFBaseModel | None:
        v = self.surface_74_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_75(self) -> IDFBaseModel | None:
        v = self.surface_75_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_76(self) -> IDFBaseModel | None:
        v = self.surface_76_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_77(self) -> IDFBaseModel | None:
        v = self.surface_77_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_78(self) -> IDFBaseModel | None:
        v = self.surface_78_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_79(self) -> IDFBaseModel | None:
        v = self.surface_79_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_80(self) -> IDFBaseModel | None:
        v = self.surface_80_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_81(self) -> IDFBaseModel | None:
        v = self.surface_81_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_82(self) -> IDFBaseModel | None:
        v = self.surface_82_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_83(self) -> IDFBaseModel | None:
        v = self.surface_83_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_84(self) -> IDFBaseModel | None:
        v = self.surface_84_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_85(self) -> IDFBaseModel | None:
        v = self.surface_85_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_86(self) -> IDFBaseModel | None:
        v = self.surface_86_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_87(self) -> IDFBaseModel | None:
        v = self.surface_87_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_88(self) -> IDFBaseModel | None:
        v = self.surface_88_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_89(self) -> IDFBaseModel | None:
        v = self.surface_89_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_90(self) -> IDFBaseModel | None:
        v = self.surface_90_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_91(self) -> IDFBaseModel | None:
        v = self.surface_91_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_92(self) -> IDFBaseModel | None:
        v = self.surface_92_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_93(self) -> IDFBaseModel | None:
        v = self.surface_93_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_94(self) -> IDFBaseModel | None:
        v = self.surface_94_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_95(self) -> IDFBaseModel | None:
        v = self.surface_95_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_96(self) -> IDFBaseModel | None:
        v = self.surface_96_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_97(self) -> IDFBaseModel | None:
        v = self.surface_97_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_98(self) -> IDFBaseModel | None:
        v = self.surface_98_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_99(self) -> IDFBaseModel | None:
        v = self.surface_99_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])

    @property
    def surface_100(self) -> IDFBaseModel | None:
        v = self.surface_100_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranSurfNames'])


class ElectricEquipment(IDFBaseModel):
    """Sets internal gains for electric equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ElectricEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to design level of electric equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal['', 'EquipmentLevel', 'Watts/Area', 'Watts/Person'] | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of electric equipment for this set of attributes Choices: EquipmentLevel => Equipment Level -- simply enter watts of equipment Wa...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    watts_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class ElectricEquipmentITEAirCooled(IDFBaseModel):
    """This object describes air-cooled electric information technology equipment
    (ITE) which has variable power consumption as a function of loading and
    temperature. If a Zone comprised of more than one Space is specified then
    this definition applies to all applicable spaces, and each instance will be
    named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ElectricEquipment:ITE:AirCooled'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_space_name: SpaceNamesRef | ZoneNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceNames', 'ZoneNames'],
            'note': 'ZoneList and SpaceList names are not allowed.',
        },
    )
    air_flow_calculation_method: (
        Literal['', 'FlowControlWithApproachTemperatures', 'FlowFromSystem'] | None
    ) = Field(
        default='FlowFromSystem',
        json_schema_extra={
            'note': 'The specified method is used to calculate the IT inlet temperature and zone return air temperature. If FlowFromSystem is chosen, the zone is assumed to be well-mixed. If FlowControlWithApproachTemp...'
        },
    )
    design_power_input_calculation_method: (
        Literal['', 'Watts/Area', 'Watts/Unit'] | None
    ) = Field(
        default='Watts/Unit',
        json_schema_extra={
            'note': 'The entered calculation method is used to specify the design power input Watts/Unit => Watts per Unit -- Design Power = Watts per Unit * Number of Units Watts/Area => Watts per Floor Area -- Design...'
        },
    )
    watts_per_unit: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    number_of_units: float | None = Field(default=1.0, ge=0.0)
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    design_power_input_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Operating schedule for this equipment, fraction applied to the design power input, generally (0.0 - 1.0) If this field is blank, the schedule is assumed to always be 1.0.',
        },
    )
    cpu_loading_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'CPU loading schedule for this equipment as a fraction from 0.0 (idle) to 1.0 (full load). If this field is blank, the schedule is assumed to always be 1.0.',
        },
    )
    cpu_power_input_function_of_loading_and_air_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the CPU power input as a function of CPU loading (x) and air inlet node temperature (y). This curve (table) should equal 1.0 a...',
        },
    )
    design_fan_power_input_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'The fraction of the total power input at design conditions which is for the cooling fan(s)'
        },
    )
    design_fan_air_flow_rate_per_power_input: float = Field(
        ...,
        ge=0.0,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'The cooling fan air flow rate per total electric power input at design conditions',
        },
    )
    air_flow_function_of_loading_and_air_temperature_curve_name: BivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the cooling air flow rate as a function of CPU loading (x) and air inlet node temperature (y). This curve (table) should equal...',
        },
    )
    fan_power_input_function_of_flow_curve_name: UnivariateFunctionsRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'The name of a single-variable curve or table lookup object which modifies the cooling fan power as a function of flow fraction (x). This curve (table) should equal 1.0 at a flow fraction of 1.0.',
        },
    )
    design_entering_air_temperature: float | None = Field(
        default=15.0,
        json_schema_extra={
            'units': 'C',
            'note': 'The entering air temperature at design conditions.',
        },
    )
    environmental_class: (
        Literal['', 'A1', 'A2', 'A3', 'A4', 'B', 'C', 'H1', 'None'] | None
    ) = Field(
        default='None',
        json_schema_extra={
            'note': 'Specifies the allowable operating conditions for the air inlet conditions. Used for reporting time outside allowable conditions.'
        },
    )
    air_inlet_connection_type: (
        Literal['', 'AdjustedSupply', 'RoomAirModel', 'ZoneAirNode'] | None
    ) = Field(
        default='AdjustedSupply',
        json_schema_extra={
            'note': 'Specifies the type of connection between the zone and the ITE air inlet node. AdjustedSupply = ITE inlet temperature will be the current Supply Air Node temperature adjusted by the current recircul...'
        },
    )
    air_inlet_room_air_model_node_name: RoomAirNodesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RoomAirNodes'],
            'note': 'Name of a RoomAir:Node object which is connected to the ITE air inlet.',
        },
    )
    air_outlet_room_air_model_node_name: RoomAirNodesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['RoomAirNodes'],
            'note': 'Name of a RoomAir:Node object which is connected to the ITE air outlet.',
        },
    )
    supply_air_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the supply air inlet node serving this ITE. Required if the Air Node Connection Type = AdjustedSupply. Also required if Calculation Method = FlowControlWithApproachTemperatures. Also requir...'
        },
    )
    design_recirculation_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=0.5,
        json_schema_extra={
            'note': 'The recirculation fraction for this equipment at design conditions. This field is used only if the Air Node Connection Type = AdjustedSupply. The default is 0.0 (no recirculation). This field is on...'
        },
    )
    recirculation_function_of_loading_and_supply_temperature_curve_name: (
        BivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['BivariateFunctions'],
            'note': 'The name of a two-variable curve or table lookup object which modifies the recirculation fraction as a function of CPU loading (x) and supply air node temperature (y). This curve (table) should equ...',
        },
    )
    design_electric_power_supply_efficiency: float | None = Field(
        default=1.0,
        le=1.0,
        gt=0.0,
        json_schema_extra={
            'note': 'The efficiency of the power supply system serving this ITE'
        },
    )
    electric_power_supply_efficiency_function_of_part_load_ratio_curve_name: (
        UnivariateFunctionsRef | None
    ) = Field(
        default=None,
        json_schema_extra={
            'object_list': ['UnivariateFunctions'],
            'note': 'The name of a single-variable curve or table lookup object which modifies the electric power supply efficiency as a function of part-load ratio (x). This curve (table) should equal 1.0 at full load...',
        },
    )
    fraction_of_electric_power_supply_losses_to_zone: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Fraction of the electric power supply losses which are a heat gain to the zone If this field is <1.0, the remainder of the losses are assumed to be lost to the outdoors.'
        },
    )
    cpu_end_use_subcategory: str | None = Field(
        default='ITE-CPU',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    fan_end_use_subcategory: str | None = Field(
        default='ITE-Fans',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    electric_power_supply_end_use_subcategory: str | None = Field(
        default='ITE-UPS',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    supply_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The difference of the IT inlet temperature from the AHU supply air temperature. Either Supply Temperature Difference or Supply Temperature Difference Schedule is required if Air Flow Calculation Me...',
        },
    )
    supply_temperature_difference_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The difference schedule of the IT inlet temperature from the AHU supply air temperature. Either Supply Temperature Difference or Supply Temperature Difference Schedule is required if Air Flow Calcu...',
        },
    )
    return_temperature_difference: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'deltaC',
            'note': 'The difference of the the actual AHU return air temperature to the IT equipment outlet temperature. Either Return Temperature Difference or Return Temperature Difference Schedule is required if Air...',
        },
    )
    return_temperature_difference_schedule: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'The difference schedule of the actual AHU return air temperature to the IT equipment outlet temperature. Either Return Temperature Difference or Return Temperature Difference Schedule is required i...',
        },
    )

    @property
    def zone_or_space(self) -> Space | Zone | None:
        v = self.zone_or_space_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SpaceNames', 'ZoneNames'])

    @property
    def design_power_input_schedule(self) -> IDFBaseModel | None:
        v = self.design_power_input_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cpu_loading_schedule(self) -> IDFBaseModel | None:
        v = self.cpu_loading_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cpu_power_input_function_of_loading_and_air_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.cpu_power_input_function_of_loading_and_air_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def air_flow_function_of_loading_and_air_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.air_flow_function_of_loading_and_air_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def fan_power_input_function_of_flow_curve(self) -> IDFBaseModel | None:
        v = self.fan_power_input_function_of_flow_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def air_inlet_room_air_model_node(self) -> RoomAirNode | None:
        v = self.air_inlet_room_air_model_node_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['RoomAirNodes'])

    @property
    def air_outlet_room_air_model_node(self) -> RoomAirNode | None:
        v = self.air_outlet_room_air_model_node_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['RoomAirNodes'])

    @property
    def recirculation_function_of_loading_and_supply_temperature_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.recirculation_function_of_loading_and_supply_temperature_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['BivariateFunctions'])

    @property
    def electric_power_supply_efficiency_function_of_part_load_ratio_curve(
        self,
    ) -> IDFBaseModel | None:
        v = self.electric_power_supply_efficiency_function_of_part_load_ratio_curve_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['UnivariateFunctions'])

    @property
    def supply_temperature_difference_schedule_ref(self) -> IDFBaseModel | None:
        v = self.supply_temperature_difference_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def return_temperature_difference_schedule_ref(self) -> IDFBaseModel | None:
        v = self.return_temperature_difference_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class GasEquipment(IDFBaseModel):
    """Sets internal gains and contaminant rates for gas equipment in the zone. If
    a ZoneList, SpaceList, or a Zone comprised of more than one Space is
    specified then this definition applies to all applicable spaces, and each
    instance will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'GasEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of gas equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of gas equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipment Watt...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    carbon_dioxide_generation_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=4e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of power input The default value assumes the equipment is fully vented. For unvented equipment, a suggested value is 3.45E-8 m3/s-W. This value is converted from a natu...',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class HotWaterEquipment(IDFBaseModel):
    """Sets internal gains for hot water equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'HotWaterEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of hot water equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of hot water equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipmen...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class IndoorLivingWall(IDFBaseModel):
    """Indoor greenery systems such as indoor living walls are panels of plants,
    which grow hydroponically or from substrates. The living wall structures can
    be either free-standing or attached to walls. The IndoorLivingWall module
    directly connects with inside surface heat balance, zone air heat balance,
    and zone air moisture balance."""

    _idf_object_type: ClassVar[str] = 'IndoorLivingWall'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['SurfaceNames'],
            'note': 'Name of the wall partition where indoor green is located.',
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)',
        },
    )
    evapotranspiration_calculation_method: (
        Literal['', 'Penman-Monteith', 'Stanghellini'] | None
    ) = Field(
        default='Penman-Monteith',
        json_schema_extra={
            'note': 'Model selection for calculating evapotranspiration of indoor greenery system. This rate can also be actuated with user-defined calculations, see EMS application guide for actuator details.'
        },
    )
    lighting_method: Literal['Daylight', 'LED', 'LED-Daylight'] | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Three different methods are provided here (LED; Daylight; LED-Daylight)'
        },
    )
    led_intensity_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    daylighting_control_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'If daylighting is used in the selected lighting methods (Daylight or LED-Daylight), users should define an object of Daylighting:Control to obtain the daylighting illuminance level and an object fo...'
        },
    )
    led_daylight_targeted_lighting_intensity_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'This field defines targeted LED intensity level for indoor living wall systems. The schedule values can be any positive number representing targeted photosynthetic photon flux density (PPFD). Based...',
            },
        )
    )
    total_leaf_area: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm2',
            'note': 'The value is the one-sided leaf area of an indoor living wall. Based on the users’ input, LAI is calculated as the ratio of the total leaf area and the partition wall area. Typical LAIs are 1.0 for...',
        },
    )
    led_nominal_intensity: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'umol/m2-s',
            'note': 'The value represents photosynthetic photon flux density (PPFD) of LED grow light. PPFD is measured in micro-mole per m2 per second (umol/m2-s) which establishes exactly how many photosynthetically ...',
        },
    )
    led_nominal_power: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'W',
            'note': 'This field defines nominal total LED power for an indoor living wall system.',
        },
    )
    radiant_fraction_of_led_lights: float | None = Field(
        default=0.6,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This field defines the fraction of radiation from LED lights'
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
        return idf._resolve_forward(v, ['SurfaceNames'])

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def led_intensity_schedule(self) -> IDFBaseModel | None:
        v = self.led_intensity_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def led_daylight_targeted_lighting_intensity_schedule(self) -> IDFBaseModel | None:
        v = self.led_daylight_targeted_lighting_intensity_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class Lights(IDFBaseModel):
    """Sets internal gains for lights in the zone. If a ZoneList, SpaceList, or a
    Zone comprised of more than one Space is specified then this definition
    applies to all applicable spaces, and each instance will be named with the
    Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'Lights'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to design level of lights, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal['', 'LightingLevel', 'Watts/Area', 'Watts/Person'] | None
    ) = Field(
        default='LightingLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of lights for this set of attributes Choices: LightingLevel => Lighting Level -- simply enter watts of lights Watts/Area => Watts...'
        },
    )
    lighting_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    watts_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    watts_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    return_air_fraction: float | None = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'Used only for sizing calculation if return-air-fraction coefficients are specified.'
        },
    )
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_visible: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_replaceable: float | None = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'For Daylighting:Controls must be 0 or 1:  0 = no dimming control, 1 = full dimming control'
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )
    return_air_fraction_calculated_from_plenum_temperature: (
        Literal['', 'No', 'Yes'] | None
    ) = Field(default='No')
    return_air_fraction_function_of_plenum_temperature_coefficient_1: float | None = (
        Field(
            default=0.0,
            ge=0.0,
            json_schema_extra={
                'note': 'Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)'
            },
        )
    )
    return_air_fraction_function_of_plenum_temperature_coefficient_2: float | None = (
        Field(
            default=0.0,
            ge=0.0,
            json_schema_extra={
                'units': '1/K',
                'note': 'Used only if Return Air Fraction Is Calculated from Plenum Temperature = Yes Equation is Return Air Fraction = Coefficient#1 - Coefficient#2 X PlenumTemp(degC)',
            },
        )
    )
    return_air_heat_gain_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the return air node for this heat gain. If left blank, defaults to the first return air node for the zone. Leave this field blank when using a ZoneList name.'
        },
    )
    exhaust_air_heat_gain_node_name: str | None = Field(
        default=None,
        json_schema_extra={
            'note': 'Name of the exhaust air node for this heat gain. If the node name is entered, return heat gain will be shared by both return and exhaust air nodes. The air properties of both nodes are weighted by ...'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class OtherEquipment(IDFBaseModel):
    """Sets internal gains or losses for \"other\" equipment in the zone. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'OtherEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    fuel_type: (
        Literal[
            '',
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
            'None',
            'OtherFuel1',
            'OtherFuel2',
            'Propane',
        ]
        | None
    ) = Field(default='None')
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of other equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of other equipment. to set a loss, use a negative value in the following fields. for this set of attributes Choices: EquipmentLev...'
        },
    )
    design_level: float | None = Field(default=None, json_schema_extra={'units': 'W'})
    power_per_floor_area: float | None = Field(
        default=None, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    carbon_dioxide_generation_rate: float | None = Field(
        default=0.0,
        ge=0.0,
        le=4e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of power input The default value assumes the equipment is fully vented.',
        },
    )
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class People(IDFBaseModel):
    """Sets internal gains and contaminant rates for occupants in the zone. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'People'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    number_of_people_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule should be fraction applied to number of people (0.0 - 1.0)',
        },
    )
    number_of_people_calculation_method: (
        Literal['', 'Area/Person', 'People', 'People/Area'] | None
    ) = Field(
        default='People',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum number of people for this set of attributes (i.e. sensible fraction, schedule, etc) Choices: People -- simply enter number of occupants....'
        },
    )
    number_of_people: float | None = Field(default=None, ge=0.0)
    people_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'person/m2'}
    )
    floor_area_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm2/person'}
    )
    fraction_radiant: float | None = Field(
        default=0.3,
        ge=0.0,
        le=1.0,
        json_schema_extra={
            'note': 'This is radiant fraction of the sensible heat released by people in a zone. This value will be multiplied by the total sensible heat released by people yields the amount of long wavelength radiatio...'
        },
    )
    sensible_heat_fraction: float | Literal['', 'Autocalculate'] | None = Field(
        default='Autocalculate',
        json_schema_extra={
            'note': 'if input, overrides program calculated sensible/latent split'
        },
    )
    activity_level_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Note that W has to be converted to mets in TC routine units in schedule are W/person',
        },
    )
    carbon_dioxide_generation_rate: float | None = Field(
        default=3.82e-08,
        ge=0.0,
        le=3.82e-07,
        json_schema_extra={
            'units': 'm3/s-W',
            'note': 'CO2 generation rate per unit of activity level. The default value is obtained from ASHRAE Std 62.1 at 0.0084 cfm/met/person over the general adult population.',
        },
    )
    enable_ashrae_55_comfort_warnings: Literal['', 'No', 'Yes'] | None = Field(
        default='No'
    )
    mean_radiant_temperature_calculation_type: (
        Literal['', 'AngleFactor', 'EnclosureAveraged', 'SurfaceWeighted'] | None
    ) = Field(
        default='EnclosureAveraged',
        json_schema_extra={'note': 'optional (only required for thermal comfort runs)'},
    )
    surface_name_angle_factor_list_name: AllHeatTranAngFacNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['AllHeatTranAngFacNames'],
            'note': 'optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    work_efficiency_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in schedule are 0.0 to 1.0 optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    clothing_insulation_calculation_method: (
        Literal[
            '',
            'CalculationMethodSchedule',
            'ClothingInsulationSchedule',
            'DynamicClothingModelASHRAE55',
        ]
        | None
    ) = Field(default='ClothingInsulationSchedule')
    clothing_insulation_calculation_method_schedule_name: ScheduleNamesRef | None = (
        Field(
            default=None,
            json_schema_extra={
                'object_list': ['ScheduleNames'],
                'note': 'a schedule value of 1 for the Scheduled method, and 2 for the DynamicClothingModelASHRAE55 method',
            },
        )
    )
    clothing_insulation_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'use "Clo" from ASHRAE or Thermal Comfort guides optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    air_velocity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in the schedule are m/s optional (only required for runs of thermal comfort models: Fanger, Pierce, KSU, CoolingEffectASH55 and AnkleDraftASH55)',
        },
    )
    thermal_comfort_model_1_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (only needed for people thermal comfort results reporting)'
        },
    )
    thermal_comfort_model_2_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (second type of thermal comfort model and results reporting)'
        },
    )
    thermal_comfort_model_3_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (third thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_4_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (fourth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_5_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (fifth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_6_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (sixth thermal comfort model and report type)'
        },
    )
    thermal_comfort_model_7_type: (
        Literal[
            'AdaptiveASH55',
            'AdaptiveCEN15251',
            'AnkleDraftASH55',
            'CoolingEffectASH55',
            'Fanger',
            'KSU',
            'Pierce',
        ]
        | None
    ) = Field(
        default=None,
        json_schema_extra={
            'note': 'optional (seventh thermal comfort model and report type)'
        },
    )
    ankle_level_air_velocity_schedule_name: ScheduleNamesRef | None = Field(
        default=None,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in the schedule are m/s this is the schedule of the air speed at the 0.1 m above the floor optional (only required for runs of thermal comfort models AnkleDraftASH55)',
        },
    )
    cold_stress_temperature_threshold: float | None = Field(
        default=15.56,
        json_schema_extra={
            'units': 'C',
            'note': 'this is the indoor safe temperature threshold for cold stress',
        },
    )
    heat_stress_temperature_threshold: float | None = Field(
        default=30.0,
        json_schema_extra={
            'units': 'C',
            'note': 'this is the indoor safe temperature threshold for heat stress',
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        )

    @property
    def number_of_people_schedule(self) -> IDFBaseModel | None:
        v = self.number_of_people_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def activity_level_schedule(self) -> IDFBaseModel | None:
        v = self.activity_level_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def surface_angle_factor_list(self) -> IDFBaseModel | None:
        v = self.surface_name_angle_factor_list_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['AllHeatTranAngFacNames'])

    @property
    def work_efficiency_schedule(self) -> IDFBaseModel | None:
        v = self.work_efficiency_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def clothing_insulation_calculation_method_schedule(self) -> IDFBaseModel | None:
        v = self.clothing_insulation_calculation_method_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def clothing_insulation_schedule(self) -> IDFBaseModel | None:
        v = self.clothing_insulation_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def air_velocity_schedule(self) -> IDFBaseModel | None:
        v = self.air_velocity_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def ankle_level_air_velocity_schedule(self) -> IDFBaseModel | None:
        v = self.ankle_level_air_velocity_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class SteamEquipment(IDFBaseModel):
    """Sets internal gains for steam equipment in the zone. If a ZoneList,
    SpaceList, or a Zone comprised of more than one Space is specified then this
    definition applies to all applicable spaces, and each instance will be named
    with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'SteamEquipment'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to design level of steam equipment, generally (0.0 - 1.0)',
        },
    )
    design_level_calculation_method: (
        Literal[
            '',
            'EquipmentLevel',
            'Power/Area',
            'Power/Person',
            'Watts/Area',
            'Watts/Person',
        ]
        | None
    ) = Field(
        default='EquipmentLevel',
        json_schema_extra={
            'note': 'The entered calculation method is used to create the maximum amount of steam equipment for this set of attributes Choices: EquipmentLevel => Design Level -- simply enter power input of equipment Wa...'
        },
    )
    design_level: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W'}
    )
    power_per_floor_area: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/m2'}
    )
    power_per_person: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'W/person'}
    )
    fraction_latent: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    fraction_lost: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class SurfaceContaminantSourceAndSinkGenericBoundaryLayerDiffusion(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:BoundaryLayerDiffusion'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    mass_transfer_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )
    henry_adsorption_constant_or_partition_coefficient: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 'dimensionless'}
    )

    @property
    def surface(self) -> IDFBaseModel | None:
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['SurfaceNames'])

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class SurfaceContaminantSourceAndSinkGenericDepositionVelocitySink(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:DepositionVelocitySink'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    surface_name: SurfaceNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfaceNames']}
    )
    deposition_velocity: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
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
        return idf._resolve_forward(v, ['SurfaceNames'])

    @property
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class SurfaceContaminantSourceAndSinkGenericPressureDriven(IDFBaseModel):
    """Simulate generic contaminant source driven by the pressure difference across
    a surface."""

    _idf_object_type: ClassVar[str] = (
        'SurfaceContaminantSourceAndSink:Generic:PressureDriven'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    surface_name: SurfAndSubSurfNamesRef = Field(
        ..., json_schema_extra={'object_list': ['SurfAndSubSurfNames']}
    )
    design_generation_rate_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    generation_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate Coefficient',
        },
    )
    generation_exponent: float | None = Field(
        default=None, le=1.0, gt=0.0, json_schema_extra={'units': 'dimensionless'}
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
    def generation_schedule(self) -> IDFBaseModel | None:
        v = self.generation_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class SwimmingPoolIndoor(IDFBaseModel):
    """Specifies an indoor swimming pools linked to a floor surface. The pool is
    assumed to cover the entire floor to which it is linked."""

    _idf_object_type: ClassVar[str] = 'SwimmingPool:Indoor'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    surface_name: FloorSurfaceNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['FloorSurfaceNames'],
            'note': 'Name of the floor surface where the pool is located.',
        },
    )
    average_depth: float = Field(..., json_schema_extra={'units': 'm'})
    activity_factor_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    make_up_water_supply_schedule_name: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cover_schedule_name: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    cover_evaporation_factor: float | None = Field(default=0.0, ge=0.0, le=1.0)
    cover_convection_factor: float | None = Field(default=0.0, ge=0.0, le=1.0)
    cover_short_wavelength_radiation_factor: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    cover_long_wavelength_radiation_factor: float | None = Field(
        default=0.0, ge=0.0, le=1.0
    )
    pool_water_inlet_node: str = Field(...)
    pool_water_outlet_node: str = Field(...)
    pool_heating_system_maximum_water_flow_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    pool_miscellaneous_equipment_power: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={
            'units': 'W/(m3/s)',
            'note': 'Power input per pool water flow rate',
        },
    )
    setpoint_temperature_schedule: ScheduleNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ScheduleNames']}
    )
    maximum_number_of_people: float = Field(..., ge=0.0)
    people_schedule: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )
    people_heat_gain_schedule: ScheduleNamesRef | None = Field(
        default=None, json_schema_extra={'object_list': ['ScheduleNames']}
    )

    @property
    def surface(
        self,
    ) -> (
        BuildingSurfaceDetailed
        | FloorAdiabatic
        | FloorDetailed
        | FloorGroundContact
        | FloorInterzone
        | None
    ):
        v = self.surface_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['FloorSurfaceNames'])

    @property
    def activity_factor_schedule(self) -> IDFBaseModel | None:
        v = self.activity_factor_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def make_up_water_supply_schedule(self) -> IDFBaseModel | None:
        v = self.make_up_water_supply_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def cover_schedule(self) -> IDFBaseModel | None:
        v = self.cover_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def setpoint_temperature_schedule_ref(self) -> IDFBaseModel | None:
        v = self.setpoint_temperature_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def people_schedule_ref(self) -> IDFBaseModel | None:
        v = self.people_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def people_heat_gain_schedule_ref(self) -> IDFBaseModel | None:
        v = self.people_heat_gain_schedule
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneBaseboardOutdoorTemperatureControlled(IDFBaseModel):
    """Specifies outside temperature-controlled electric baseboard heating. If a
    ZoneList, SpaceList, or a Zone comprised of more than one Space is specified
    then this definition applies to all applicable spaces, and each instance
    will be named with the Space Name plus this Object Name."""

    _idf_object_type: ClassVar[str] = 'ZoneBaseboard:OutdoorTemperatureControlled'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_or_zonelist_or_space_or_spacelist_name: (
        SpaceAndSpaceListNamesRef | ZoneAndZoneListNamesRef
    ) = Field(
        ...,
        json_schema_extra={
            'object_list': ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'units in Schedule should be fraction applied to capacity of the baseboard heat equipment, generally (0.0 - 1.0)',
        },
    )
    capacity_at_low_temperature: float = Field(
        ..., gt=0.0, json_schema_extra={'units': 'W'}
    )
    low_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    capacity_at_high_temperature: float = Field(
        ..., ge=0.0, json_schema_extra={'units': 'W'}
    )
    high_temperature: float = Field(..., json_schema_extra={'units': 'C'})
    fraction_radiant: float | None = Field(default=0.0, ge=0.0, le=1.0)
    end_use_subcategory: str | None = Field(
        default='General',
        json_schema_extra={
            'note': 'Any text may be used here to categorize the end-uses in the ABUPS End Uses by Subcategory table.'
        },
    )

    @property
    def zone_or_zonelist_or_space_or_spacelist(
        self,
    ) -> Space | SpaceList | Zone | ZoneList | None:
        v = self.zone_or_zonelist_or_space_or_spacelist_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(
            v, ['SpaceAndSpaceListNames', 'ZoneAndZoneListNames']
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


class ZoneContaminantSourceAndSinkCarbonDioxide(IDFBaseModel):
    """Represents internal CO2 gains and sinks in the zone."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:CarbonDioxide'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate: float | None = Field(
        default=None,
        json_schema_extra={
            'units': 'm3/s',
            'note': 'Positive values represent sources and negative values represent sinks.',
        },
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate',
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
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneContaminantSourceAndSinkGenericConstant(IDFBaseModel):
    """Sets internal generic contaminant gains and sinks in a zone with constant
    values."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:Constant'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'The values represent source.'},
    )
    generation_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate',
        },
    )
    design_removal_coefficient: float | None = Field(
        default=None,
        ge=0.0,
        json_schema_extra={'units': 'm3/s', 'note': 'The value represent sink.'},
    )
    removal_schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design removal Coefficient',
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
    def generation_schedule(self) -> IDFBaseModel | None:
        v = self.generation_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])

    @property
    def removal_schedule(self) -> IDFBaseModel | None:
        v = self.removal_schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneContaminantSourceAndSinkGenericCutoffModel(IDFBaseModel):
    """Simulate generic contaminant source driven by the cutoff concentration
    model."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:CutoffModel'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    design_generation_rate_coefficient: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Design Generation Rate Coefficient',
        },
    )
    cutoff_generic_contaminant_at_which_emission_ceases: float | None = Field(
        default=None,
        gt=0.0,
        json_schema_extra={
            'units': 'ppm',
            'note': 'When the zone concentration level is greater than the cutoff level, emission stops, and the source level is zero.',
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
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneContaminantSourceAndSinkGenericDecaySource(IDFBaseModel):
    """Simulate generic contaminant source driven by the cutoff concentration
    model."""

    _idf_object_type: ClassVar[str] = 'ZoneContaminantSourceAndSink:Generic:DecaySource'
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    initial_emission_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm3/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
        },
    )
    delay_time_constant: float | None = Field(
        default=None, gt=0.0, json_schema_extra={'units': 's'}
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
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])


class ZoneContaminantSourceAndSinkGenericDepositionRateSink(IDFBaseModel):
    """Simulate generic contaminant source driven by the boundary layer diffusion
    controlled model."""

    _idf_object_type: ClassVar[str] = (
        'ZoneContaminantSourceAndSink:Generic:DepositionRateSink'
    )
    _provider_fields: ClassVar[frozenset[str]] = frozenset({'name'})
    name: str = Field(...)
    zone_name: ZoneNamesRef = Field(
        ..., json_schema_extra={'object_list': ['ZoneNames']}
    )
    deposition_rate: float | None = Field(
        default=None, ge=0.0, json_schema_extra={'units': 'm/s'}
    )
    schedule_name: ScheduleNamesRef = Field(
        ...,
        json_schema_extra={
            'object_list': ['ScheduleNames'],
            'note': 'Value in this schedule should be a fraction (generally 0.0 - 1.0) applied to the Initial Emission Rate. When the value is equal to 1.0, the time will be reset to zero.',
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
    def schedule(self) -> IDFBaseModel | None:
        v = self.schedule_name
        if not v:
            return None
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF')
        return idf._resolve_forward(v, ['ScheduleNames'])
