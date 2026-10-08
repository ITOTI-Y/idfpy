# Files and dictionaries

An `IDF` is a container of model objects keyed by object type and name. It
reads and writes both the classic IDF text format and epJSON.

## Loading and saving

```python
from pathlib import Path

from idfpy import IDF

idf = IDF.load(Path('model.idf'))       # IDF text
idf = IDF.load(Path('model.epjson'))    # epJSON, chosen by extension

idf.save(Path('out.idf'))                         # default: IDF text
idf.save(Path('out.epjson'), output_type='epjson')
```

## Adding, querying and removing objects

```python
from idfpy.models import Lights, Zone

idf.add(Zone(name='Office'))            # ValueError if 'Office' already exists

idf.get(Zone, 'Office')                 # Zone | None
idf.has('Zone', 'Office')               # True
idf.all_of_type(Lights)                 # dict[str, Lights], keyed by name
list(idf.types())                       # object types present in the model

idf.remove(Zone, 'Office')              # also unregisters its references
```

Objects without a name field, such as `Version` or `Timestep`, receive an
internal key automatically when added.

Type names are checked: a misspelt type raises `UnknownObjectTypeError`
instead of silently returning nothing. Pass `strict=False` to get `None` or an
empty result instead.

```python
idf.get('BuildingSurface:detailed', 'Wall1')
# UnknownObjectTypeError: Unknown object type: 'BuildingSurface:detailed'. ...
```

## Dictionaries for LLM tool calls

`to_dict()` returns the epJSON structure, object type → object name →
fields, which maps directly onto JSON tool arguments. Only fields that were
set explicitly are included, which keeps the payload small.

```python
data = idf.to_dict()
# {'Building': {'MyBuilding': {'north_axis': 0.0, 'terrain': 'Suburbs'}},
#  'Zone': {'Zone1': {'multiplier': 2}}, ...}

idf = IDF.from_dict(data)
```

`merge_dict()` applies a partial dictionary to an existing model. The merge is
atomic: every object is validated before anything changes, so a rejected tool
call leaves the model untouched.

```python
idf.merge_dict(
    {'Zone': {'Zone2': {'multiplier': 3}}},
    on_conflict='replace',   # 'raise' (default), 'replace' or 'skip'
)
```

Field names may use either the Python `snake_case` names or the original
schema keys.

## Logging

idfpy logs through Loguru. Messages at `INFO` and above are visible by
default; per-object progress uses the `TRACE` level and needs an explicit
sink:

```python
from loguru import logger

logger.add('idfpy.log', level='TRACE')
```
