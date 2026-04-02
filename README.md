# idfpy

[![PyPI](https://img.shields.io/pypi/v/idfpy)](https://pypi.org/project/idfpy/)
[![Python 3.12+](https://img.shields.io/pypi/pyversions/idfpy)](https://pypi.org/project/idfpy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![EnergyPlus 25.2](https://img.shields.io/badge/EnergyPlus-25.2-orange)](https://energyplus.net/)
[![Autoupdate](https://github.com/ITOTI-Y/idfpy/actions/workflows/update-models.yml/badge.svg)](https://github.com/ITOTI-Y/idfpy/actions/workflows/update-models.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/itoti-y/idfpy)

Type-safe [Pydantic](https://docs.pydantic.dev/) models for **all** [EnergyPlus](https://energyplus.net/) IDF object types, plus IDF file read/write and simulation execution, optimized for LLM tool calling and IDE auto-completion.

Auto-generated from `Energy+.schema.epJSON` version **25.2.0**.

## Features

- **960+ object types** as Pydantic v2 models with full validation
- **275 reference types** with cross-object validation
- **Forward navigation** — `surface.zone` resolves a reference field to the target object
- **Reverse navigation** — `zone.referencing("Lights")` finds all objects that reference a given object
- **Reference validation** — `idf.validate()` batch-checks all cross-object references for existence and type compatibility
- **Extension plugin system** — `surface.area`, `.normal`, `.centroid` via auto-discovered geometry mixins with full IDE support
- **Case-insensitive** Literal field matching (EnergyPlus IDF is case-insensitive)
- **Extensible field** support (vertices, schedule data, etc.)
- **IDF read/write** with positional field ordering
- **epJSON read/write** with auto-detection by file extension
- **`to_dict()` / `from_dict()`** for in-memory dict conversion (ideal for LLM tool calls)
- **EnergyPlus simulation** execution with ExpandObjects support
- Accepts both `snake_case` and original EnergyPlus schema key names

## Why idfpy over eppy?

|  | idfpy | eppy |
|---|:---:|:---:|
| No EnergyPlus IDD required at runtime | ✅ | ❌ |
| Type-safe field validation | ✅ Pydantic v2 | ❌ |
| epJSON read/write | ✅ | ❌ |
| Cross-reference validation | ✅ 275 ref groups | ❌ |
| Forward/reverse navigation | ✅ 2847 properties | ❌ |
| Surface geometry (area/normal) | ✅ ext plugin | ❌ |
| `to_dict()` / `from_dict()` for LLM | ✅ | ❌ |
| Dependencies | 4 (pydantic, jinja2, loguru, typer) | 12+ (lxml, pyparsing...) |

## Installation

```bash
pip install idfpy
```

## Quick Start

```python
from pathlib import Path
from idfpy import IDF
from idfpy.models.simulation import Version, Building
from idfpy.models.thermal_zones import Zone

# Create an IDF
idf = IDF()
idf.add(Version())
idf.add(Building(name='MyBuilding', north_axis=0.0))
idf.add(Zone(name='Zone1'))

# Save as IDF
idf.save(Path('output.idf'))

# Save as epJSON
idf.save(Path('output.epjson'), output_type='epjson')

# Load (auto-detects format by extension)
idf = IDF.load(Path('existing.idf'))      # IDF format
idf = IDF.load(Path('existing.epjson'))    # epJSON format

# Run simulation
idf.run(
    idf_path=Path('model.idf'),
    weather_path=Path('weather.epw'),
    output_dir=Path('results/'),
)
```

### In-memory dict conversion

```python
from pathlib import Path
from idfpy import IDF

idf = IDF.load(Path('model.idf'))

# IDF → dict (epJSON structure)
data = idf.to_dict()
# {
#   "Building": {"MyBuilding": {"north_axis": 0.0, "terrain": "Suburbs"}},
#   "Zone": {"Zone1": {"direction_of_relative_north": 0.0}},
#   ...
# }

# dict → IDF
idf = IDF.from_dict(data)
```

### Object navigation

Every reference field generates a `@property` for forward navigation. Reverse navigation is available via `referencing()`.

```python
from pathlib import Path
from idfpy import IDF

idf = IDF.load(Path('model.idf'))

# Forward navigation — resolve reference to target object
surface = idf.get('BuildingSurface:Detailed', 'Wall1')
surface.zone_name        # "Zone1" (raw string, always works)
surface.zone             # Zone object (resolved via IDF)
surface.construction     # Construction object

# Reverse navigation — find all objects referencing a given object
zone = idf.get('Zone', 'Zone1')
zone.referencing('BuildingSurface:Detailed')  # → [Wall1, Wall2, ...]
zone.referencing('Lights')                     # → [OfficeLights, ...]

# Chained navigation
zone.referencing('BuildingSurface:Detailed')[0].construction
```

### Reference validation

```python
from idfpy import IDF, RefValidationError

idf = IDF.load(Path('model.idf'))

# Batch check all cross-object references
errors = idf.validate()
for e in errors:
    print(e)
# [missing] Lights/OffLights.schedule_name: "BadSched" not found in any of [ScheduleNames]

# Or raise on first broken reference set
try:
    idf.validate_or_raise()
except RefValidationError as exc:
    print(f"{len(exc.errors)} broken reference(s)")
```

## Real-world Example
```python
from pathlib import Path
from idfpy import IDF

# Load a DOE reference building
idf = IDF.load(Path("LargeOffice.idf"))

# Modify all exterior walls' insulation
for con_name, con in idf.all_of_type("Construction").items():
    layer = con.outside_layer_ref
    if layer and hasattr(layer, "conductivity"):
        print(f"{con.name}: k={layer.conductivity} W/m·K")

# Validate all references
errors = idf.validate()
print(f"{len(errors)} broken references")
```

### Geometry extensions

Surface models include geometry properties via the built-in `ext.geometry` plugin — area, normal vector, and centroid are computed from vertices using Newell's method, with full IDE autocompletion.

```python
from idfpy import IDF
from pathlib import Path

idf = IDF.load(Path('model.idf'))

surface = idf.get('BuildingSurface:Detailed', 'Wall1')
surface.area               # 30.0 (m²)
surface.normal             # (0.0, -1.0, 0.0) — outward unit normal
surface.centroid           # (5.0, 0.0, 1.5)
surface.vertices_as_tuples # [(0,0,3), (0,0,0), (10,0,0), (10,0,3)]

window = idf.get('FenestrationSurface:Detailed', 'Win1')
window.area                # 16.0 (m²)
```

Supported surface types: `BuildingSurface:Detailed`, `FenestrationSurface:Detailed`, `Floor:Detailed`, `RoofCeiling:Detailed`, `Wall:Detailed`, `Shading:Building:Detailed`, `Shading:Site:Detailed`, `Shading:Zone:Detailed`.

#### Creating custom plugins

Extensions live in `idfpy/ext/` as sub-packages. Each plugin exposes a `MIXIN_MAP` that the code generator auto-discovers:

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
        """Compute U-value from construction layers."""
        ...
```

After adding a plugin, re-run `idfpy codegen` to regenerate models — the mixin is injected into the class hierarchy and IDE autocompletion works immediately.

### Container mutation

```python
idf.remove('Zone', 'Zone1')  # unbinds + unregisters references
```

## License

MIT
