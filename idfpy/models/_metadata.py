"""Unified per-class metadata cache for IDF model introspection.

Eliminates repeated runtime type reflection by computing and caching
all type-annotation-derived metadata once per model class.
"""

from __future__ import annotations

import types
from dataclasses import dataclass
from typing import Annotated, Any, Union, get_args, get_origin

from idfpy.models._base import IDFBaseModel


def _find_list_item_class(annotation: Any) -> type[IDFBaseModel] | None:
    """Extract the IDFBaseModel item class from a list type annotation.

    Handles list[X], list[X] | None, Annotated[list[X], ...], etc.

    Returns:
        The item class if the annotation is a list of IDFBaseModel subclass,
        None otherwise.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is list and args:
        item_type = args[0]
        if isinstance(item_type, type) and issubclass(item_type, IDFBaseModel):
            return item_type
        return None

    if origin is Union or isinstance(annotation, types.UnionType):
        for arg in args:
            result = _find_list_item_class(arg)
            if result is not None:
                return result

    if origin is Annotated and args:
        return _find_list_item_class(args[0])

    return None


@dataclass(frozen=True, slots=True)
class ModelMetadata:
    """Per-class metadata computed once from type annotations."""

    # Field names that are list-typed (extensible fields)
    list_field_names: frozenset[str]
    # For each list field: the IDFBaseModel item class
    list_item_classes: dict[str, type[IDFBaseModel]]
    # For each list field item class: ordered field names
    list_item_field_names: dict[str, list[str]]
    # Whether this model has a 'name' field
    has_name_field: bool
    # field_name → validation_alias (only where alias differs and no alias set)
    validation_alias_remap: dict[str, str]
    # field_name → {lowercase_value: canonical_value} for Literal fields
    literal_case_maps: dict[str, dict[str, str | int]]
    # REF_CONSUMERS for this class (empty dict if not a consumer)
    consumer_fields: dict[str, list[str]]
    # Provider fields (frozenset, forwarded from ClassVar)
    provider_fields: frozenset[str]


_cache: dict[type, ModelMetadata] = {}


def get_model_metadata(cls: type[IDFBaseModel]) -> ModelMetadata:
    """Get or build the metadata cache for a model class."""
    meta = _cache.get(cls)
    if meta is not None:
        return meta
    meta = _build_metadata(cls)
    _cache[cls] = meta
    return meta


def _build_metadata(cls: type[IDFBaseModel]) -> ModelMetadata:
    """Build metadata by inspecting model fields once."""
    from idfpy.models._ref_meta import REF_CONSUMERS

    # Reuse existing per-class caches for hot-path validators
    list_field_names = cls._get_list_field_names()
    literal_case_maps = cls._get_literal_case_maps()

    # Build additional metadata in a single pass
    list_item_classes: dict[str, type[IDFBaseModel]] = {}
    list_item_field_names: dict[str, list[str]] = {}
    validation_alias_remap: dict[str, str] = {}

    for field_name, field_info in cls.model_fields.items():
        # List item classes for extensible fields
        if field_name in list_field_names:
            item_class = _find_list_item_class(field_info.annotation)
            if item_class is not None:
                list_item_classes[field_name] = item_class
                list_item_field_names[field_name] = list(item_class.model_fields.keys())

        # Validation alias remapping
        va = field_info.validation_alias
        if isinstance(va, str) and va != field_name and not field_info.alias:
            validation_alias_remap[field_name] = va

    return ModelMetadata(
        list_field_names=list_field_names,
        list_item_classes=list_item_classes,
        list_item_field_names=list_item_field_names,
        has_name_field='name' in cls.model_fields,
        validation_alias_remap=validation_alias_remap,
        literal_case_maps=literal_case_maps,
        consumer_fields=REF_CONSUMERS.get(cls.__name__, {}),
        provider_fields=cls._provider_fields,
    )
