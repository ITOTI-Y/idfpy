"""Tests for the unified per-class metadata cache."""

from idfpy.models._metadata import ModelMetadata, get_model_metadata


def test_zone_metadata():
    from idfpy.models.thermal_zones import Zone

    meta = get_model_metadata(Zone)
    assert isinstance(meta, ModelMetadata)
    assert meta.has_name_field is True
    assert meta.list_field_names == frozenset()
    assert meta.list_item_classes == {}
    assert meta.list_item_field_names == {}
    assert isinstance(meta.provider_fields, frozenset)


def test_surface_extensible_metadata():
    from idfpy.models.thermal_zones import BuildingSurfaceDetailed

    meta = get_model_metadata(BuildingSurfaceDetailed)
    assert 'vertices' in meta.list_field_names
    assert 'vertices' in meta.list_item_classes
    item_cls = meta.list_item_classes['vertices']
    assert item_cls.__name__ == 'BuildingSurfaceDetailedVerticesItem'
    assert 'vertex_x_coordinate' in meta.list_item_field_names['vertices']


def test_cache_identity():
    from idfpy.models.thermal_zones import Zone

    meta1 = get_model_metadata(Zone)
    meta2 = get_model_metadata(Zone)
    assert meta1 is meta2


def test_literal_case_maps():
    from idfpy.models.thermal_zones import BuildingSurfaceDetailed

    meta = get_model_metadata(BuildingSurfaceDetailed)
    # BuildingSurface:Detailed has Literal fields like surface_type
    assert isinstance(meta.literal_case_maps, dict)


def test_validation_alias_remap():
    """Verify alias_remap captures validation_alias fields correctly."""
    from idfpy.models._metadata import get_model_metadata
    from idfpy.models.thermal_zones import Zone

    meta = get_model_metadata(Zone)
    # All remapped fields should have string keys and values
    for k, v in meta.validation_alias_remap.items():
        assert isinstance(k, str)
        assert isinstance(v, str)
        assert k != v


def test_consumer_fields():
    from idfpy.models.thermal_zones import BuildingSurfaceDetailed

    meta = get_model_metadata(BuildingSurfaceDetailed)
    # BuildingSurface:Detailed references zones, surfaces, etc.
    assert isinstance(meta.consumer_fields, dict)
    # It should have at least zone_name as a consumer field
    assert any('zone_name' in k for k in meta.consumer_fields)


def test_frozen_metadata():
    from idfpy.models.thermal_zones import Zone

    meta = get_model_metadata(Zone)
    # ModelMetadata is frozen — mutation should raise
    try:
        meta.has_name_field = False  # type: ignore
        raise AssertionError('Should have raised FrozenInstanceError')
    except AttributeError:
        pass
