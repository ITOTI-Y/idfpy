---
hide:
  - navigation
---

# idfpy

**Type-safe Pydantic models for every EnergyPlus IDF object**, plus IDF and
epJSON file handling and simulation runs, built for IDE auto-completion and
LLM tool calling.

```bash
pip install idfpy
```

<div class="grid cards" markdown>

-   :lucide-shield-check: **Validated models**

    ---

    Every EnergyPlus object type is a Pydantic v2 model generated from
    `Energy+.schema.epJSON`, with field types, ranges, choices and units.

    [:octicons-arrow-right-24: Object reference](reference/index.md)

-   :lucide-git-fork: **Reference navigation**

    ---

    Follow references forward with `surface.zone`, backwards with
    `zone.referencing("Lights")`, and check them all with `idf.validate()`.

    [:octicons-arrow-right-24: Navigating references](guides/navigation.md)

-   :lucide-file-json: **IDF and epJSON**

    ---

    Load and save both formats, and convert whole models to and from plain
    dictionaries for LLM tool calls.

    [:octicons-arrow-right-24: Files and dictionaries](guides/files.md)

-   :lucide-play: **Simulation**

    ---

    Run EnergyPlus on a file or an in-memory model, one job or a concurrent
    batch, and inspect warnings and severe errors.

    [:octicons-arrow-right-24: Running simulations](guides/simulation.md)

</div>

## A first model

```python
from pathlib import Path

from idfpy import IDF
from idfpy.models import Building, Version, Zone

idf = IDF()
idf.add(Version())
idf.add(Building(name='MyBuilding', north_axis=0.0))
idf.add(Zone(name='Zone1'))

idf.save(Path('output.idf'))
idf.save(Path('output.epjson'), output_type='epjson')
```

Invalid values fail at construction time instead of inside EnergyPlus:

```python
Zone(name='Zone1', multiplier=0)
# pydantic_core.ValidationError: 1 validation error for Zone
# multiplier
#   Input should be greater than or equal to 1
```

## EnergyPlus versions

Each idfpy release targets one EnergyPlus version: idfpy `26.2.x` models
EnergyPlus 26.2. Use the version selector in the header to read the
documentation for the release you installed.

| EnergyPlus | Install |
|---|---|
| 26.2 | `pip install "idfpy==26.2.*"` |
| 26.1 | `pip install "idfpy==26.1.*"` |
| 25.2 | `pip install "idfpy==25.2.*"` |
| 25.1 | `pip install "idfpy==25.1.*"` |
