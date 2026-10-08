# Extensions

Extensions add computed properties to generated models. They are mixed into
the model classes at code generation time, so editors auto-complete them like
ordinary fields.

## Geometry

Surface objects gain geometry computed from their vertices with Newell's
method:

```python
surface = idf.get('BuildingSurface:Detailed', 'Wall1')

surface.area                # 30.0, in m²
surface.normal              # (0.0, -1.0, 0.0), outward unit normal
surface.centroid            # (5.0, 0.0, 1.5)
surface.tilt                # 90.0, degrees from horizontal
surface.azimuth             # 180.0, degrees clockwise from north
surface.perimeter
surface.bounding_box
surface.is_convex
surface.vertices_as_tuples  # [(0, 0, 3), (0, 0, 0), (10, 0, 0), (10, 0, 3)]
```

Supported types: `BuildingSurface:Detailed`, `FenestrationSurface:Detailed`,
`Floor:Detailed`, `RoofCeiling:Detailed`, `Wall:Detailed`,
`Shading:Building:Detailed`, `Shading:Site:Detailed` and
`Shading:Zone:Detailed`.

## Constructions

`Construction` gains `layers`, `is_window_construction` and
`is_opaque_construction`; see [Navigating references](navigation.md#constructions-and-layers).

## Writing a plugin

An extension is a sub-package of `idfpy.ext` that exposes `MIXIN_MAP`,
mapping generated class names to mixin classes:

```python
# idfpy/ext/thermal/__init__.py
from .mixins import ThermalPropertyMixin

MIXIN_MAP: dict[str, type] = {
    'BuildingSurfaceDetailed': ThermalPropertyMixin,
}
```

```python
# idfpy/ext/thermal/mixins.py
class ThermalPropertyMixin:
    @property
    def u_value(self) -> float:
        """U-value of the surface construction, in W/(m²·K)."""
        ...
```

Regenerate the models so the code generator injects the mixin:

```bash
idfpy codegen --schema Energy+.schema.epJSON --output idfpy/models
```
