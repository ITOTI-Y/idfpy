# Navigating references

EnergyPlus objects refer to each other by name: a surface names its zone and
construction, a lights object names its schedule. idfpy turns those names into
navigable links once the objects live in the same `IDF`.

## Forward: what does this object use?

Every reference field gets a property without the `_name` suffix that resolves
the target object.

```python
from idfpy.models import BuildingSurfaceDetailed, Zone

surface = idf.get(BuildingSurfaceDetailed, 'Wall1')

surface.zone_name        # 'Zone1', the raw string
surface.zone             # the Zone object, or None if it is missing
surface.construction     # the Construction object

surface.referenced()     # every object this surface refers to
surface.referenced(Zone) # only the zones
```

## Backward: who uses this object?

```python
zone = idf.get(Zone, 'Zone1')

zone.referencing(BuildingSurfaceDetailed)   # surfaces in this zone
zone.referencing('Lights')                  # lights objects in this zone
```

Calls chain naturally:

```python
zone.referencing(BuildingSurfaceDetailed)[0].construction
```

The [object reference](../reference/index.md) lists, for every object type,
which types it can name and which types can name it.

## Constructions and layers

The built-in construction extension resolves layers in order and classifies
the construction:

```python
from idfpy.models import Construction

con = idf.get(Construction, 'ExtWall')
con.layers                    # [Material, Material, ...] outside to inside
con.is_window_construction    # True if the layers are window materials
con.is_opaque_construction
```
