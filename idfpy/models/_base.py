"""Base class for all EnergyPlus IDF object models."""

from __future__ import annotations

import types
from typing import Annotated, Any, ClassVar, Literal, Union, get_args, get_origin

from pydantic import BaseModel, ConfigDict, model_validator


def _extract_literal_values(annotation: Any) -> list[str]:
    """Extract all string Literal values from a type annotation.

    Handles Union, Optional, Annotated wrappers.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is Literal:
        return [a for a in args if isinstance(a, str)]

    if origin is Union or isinstance(annotation, types.UnionType):
        result: list[str] = []
        for arg in get_args(annotation):
            result.extend(_extract_literal_values(arg))
        return result

    if origin is Annotated:
        return _extract_literal_values(args[0])

    return []


class IDFBaseModel(BaseModel):
    """Base class for all IDF object models.

    Provides common configuration and utility methods for IDF objects.

    Attributes:
        _idf_object_type: Class variable storing the original EnergyPlus object
            type name (e.g., "BuildingSurface:Detailed"). Override in subclasses.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra='forbid',
        validate_assignment=True,
        str_strip_whitespace=True,
    )

    _idf_object_type: ClassVar[str] = ''

    @model_validator(mode='before')
    @classmethod
    def _normalize_literal_case(cls, data: Any) -> Any:
        """Normalize string values to match Literal field case.

        EnergyPlus IDF files are case-insensitive, but Pydantic Literal
        types require exact case. This validator maps input values to the
        correct case before validation.
        """
        if not isinstance(data, dict):
            return data

        for field_name, field_info in cls.model_fields.items():
            if field_name not in data:
                continue
            value = data[field_name]
            if not isinstance(value, str):
                continue

            literal_values = _extract_literal_values(field_info.annotation)
            if not literal_values:
                continue

            lower_map = {v.lower(): v for v in literal_values}
            matched = lower_map.get(value.lower())
            if matched is not None:
                data[field_name] = matched

        return data

    @classmethod
    def idf_object_type(cls) -> str:
        """Get the EnergyPlus IDF object type name.

        Returns:
            Original object type name (e.g., "Zone", "BuildingSurface:Detailed").
        """
        return cls._idf_object_type

    def to_idf_dict(self) -> dict[str, Any]:
        """Convert model to IDF-compatible dictionary.

        Exports all non-None fields with their original names.

        Returns:
            Dictionary suitable for IDF/epJSON serialization.
        """
        return self.model_dump(exclude_none=True, by_alias=True)
