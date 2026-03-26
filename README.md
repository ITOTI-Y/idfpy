# idfpy

Type-safe [Pydantic](https://docs.pydantic.dev/) models for **all** [EnergyPlus](https://energyplus.net/) IDF object types, plus IDF file read/write and simulation execution.

Auto-generated from `Energy+.schema.epJSON` version **25.1.0**.

## Features

- **858 object types** as Pydantic v2 models with full validation
- **275 reference types** with cross-object validation
- **Case-insensitive** Literal field matching (EnergyPlus IDF is case-insensitive)
- **Extensible field** support (vertices, schedule data, etc.)
- **IDF read/write** with positional field ordering
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

# Save
idf.save(Path('output.idf'))

# Load existing IDF
idf = IDF.load(Path('existing.idf'))
print(f'{len(idf)} objects loaded')

# Run simulation
idf.run(
    idf_path=Path('model.idf'),
    weather_path=Path('weather.epw'),
    output_dir=Path('results/'),
)
```

## License

MIT
