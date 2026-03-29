"""Base class for all EnergyPlus IDF object models."""

from __future__ import annotations

import types
import weakref
from typing import Annotated, Any, ClassVar, Literal, Union, get_args, get_origin

from pydantic import BaseModel, ConfigDict, PrivateAttr, model_validator


def _extract_literal_values(annotation: Any) -> list[str | int]:
    """Extract all string and int Literal values from a type annotation.

    Handles Union, Optional, Annotated wrappers.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is Literal:
        return [a for a in args if isinstance(a, (str, int))]

    if origin is Union or isinstance(annotation, types.UnionType):
        result: list[str | int] = []
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
    # Cached per-class: field_name -> {lowercase_value: canonical_value}
    _literal_case_maps: ClassVar[dict[str, dict[str, str | int]]] = {}
    _idf_ref: weakref.ref | None = PrivateAttr(default=None)

    @property
    def _idf(self) -> Any:
        """Get bound IDF container, or None if unbound."""
        if self._idf_ref is None:
            return None
        return self._idf_ref()

    @classmethod
    def _get_literal_case_maps(cls) -> dict[str, dict[str, str | int]]:
        """Get or build the literal case-mapping cache for this class."""
        if '_literal_case_maps' not in cls.__dict__:
            maps: dict[str, dict[str, str | int]] = {}
            for field_name, field_info in cls.model_fields.items():
                literal_values = _extract_literal_values(field_info.annotation)
                if literal_values:
                    case_map: dict[str, str | int] = {}
                    for v in literal_values:
                        if isinstance(v, str):
                            case_map[v.lower()] = v
                        elif isinstance(v, int):
                            case_map[str(v)] = v
                    if case_map:
                        maps[field_name] = case_map
            cls._literal_case_maps = maps
        return cls._literal_case_maps

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

        literal_maps = cls._get_literal_case_maps()
        if not literal_maps:
            return data

        for field_name, case_map in literal_maps.items():
            value = data.get(field_name)
            if not isinstance(value, str):
                continue
            matched = case_map.get(value) or case_map.get(value.lower())
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

    def referencing(
        self,
        consumer_type: str | type[IDFBaseModel] | None = None,
    ) -> list[IDFBaseModel]:
        """Find objects that reference this object.

        Args:
            consumer_type: EnergyPlus object type string
                (e.g., "BuildingSurface:Detailed"), model class, or None.
                When None, returns all objects across every type.

        Returns:
            List of objects whose ref fields point to this object.

        Raises:
            RuntimeError: If not bound to an IDF container.
        """
        idf = self._idf
        if idf is None:
            raise RuntimeError('Not bound to IDF container')
        if consumer_type is None:
            return idf._find_all_referencing(self)
        if isinstance(consumer_type, type):
            consumer_type = consumer_type._idf_object_type
        return idf._find_referencing(self, consumer_type)

    def to_idf_dict(self) -> dict[str, Any]:
        """Convert model to IDF-compatible dictionary.

        Exports all non-None fields with their original names.

        Returns:
            Dictionary suitable for IDF/epJSON serialization.
        """
        return self.model_dump(exclude_none=True, by_alias=True)
