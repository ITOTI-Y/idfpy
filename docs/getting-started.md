# Getting started

## Installation

idfpy needs Python 3.12 or newer. EnergyPlus itself is only required for
running simulations; reading, editing and validating models works without it.

=== "pip"

    ```bash
    pip install "idfpy==26.2.*"
    ```

=== "uv"

    ```bash
    uv add "idfpy==26.2.*"
    ```

Pick the idfpy series that matches the EnergyPlus version of your models.
The installed version reports the EnergyPlus schema it was generated from:

```python
from idfpy import IDF

IDF().version  # '26.2'
```

## Load, edit, save

```python
from pathlib import Path

from idfpy import IDF
from idfpy.models import Zone

idf = IDF.load(Path('existing.idf'))  # format detected from the extension

zone = idf.get(Zone, 'Zone1')  # typed as Zone | None
zone.multiplier = 2  # validated on assignment

idf.save(Path('modified.idf'))
```

Query methods accept the model class, its Python class name
(`'BuildingSurfaceDetailed'`) or the EnergyPlus type name
(`'BuildingSurface:Detailed'`). Passing the class keeps precise types in your
editor.

## Run a simulation

```python
from pathlib import Path

from idfpy.sim import simulate

result = simulate(
    Path('modified.idf'),
    weather=Path('USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw'),
    output_dir=Path('results'),
)
print(result.success, result.err.severe_count if result.err else None)
```

## Where next

- [Files and dictionaries](guides/files.md) covers every way in and out of an `IDF`.
- [Navigating references](guides/navigation.md) shows how objects point at each other.
- The [object reference](reference/index.md) lists every field of every object type.
