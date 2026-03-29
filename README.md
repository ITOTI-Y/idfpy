# idfpy

Type-safe [Pydantic](https://docs.pydantic.dev/) models for **all** [EnergyPlus](https://energyplus.net/) IDF object types, plus IDF file read/write and simulation execution.

Auto-generated from `Energy+.schema.epJSON` version **25.2.0**.

## Features

- **858 object types** as Pydantic v2 models with full validation
- **275 reference types** with cross-object validation
- **Forward navigation** — `surface.zone` resolves a reference field to the target object
- **Reverse navigation** — `zone.referencing("Lights")` finds all objects that reference a given object
- **Reference validation** — `idf.validate()` batch-checks all cross-object references for existence and type compatibility
- **Case-insensitive** Literal field matching (EnergyPlus IDF is case-insensitive)
- **Extensible field** support (vertices, schedule data, etc.)
- **IDF read/write** with positional field ordering
- **epJSON read/write** with auto-detection by file extension
- **`to_dict()` / `from_dict()`** for in-memory dict conversion (ideal for LLM tool calls)
- **EnergyPlus simulation** execution with ExpandObjects support
- Accepts both `snake_case` and original EnergyPlus schema key names

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

### Container mutation

```python
idf.remove('Zone', 'Zone1')  # unbinds + unregisters references
```

## License

MIT
