# Validating models

Validation happens at two levels.

## Field values

Every model is a Pydantic model, so values are checked when an object is
constructed and whenever a field is assigned: numeric ranges, allowed choices
and required fields come straight from the EnergyPlus schema.

```python
from idfpy.models import Zone

zone = Zone(name='Zone1')
zone.multiplier = 0
# ValidationError: multiplier — Input should be greater than or equal to 1
```

Choice fields accept any letter case, as EnergyPlus does, and store the
canonical spelling:

```python
from idfpy.models import Building

Building(name='B', terrain='suburbs').terrain  # 'Suburbs'
```

## Cross-object references

A name that points at a missing object, or at an object of the wrong type,
only shows up once the whole model is assembled. `validate()` checks every
reference in one pass and returns the problems:

```python
errors = idf.validate()
for error in errors:
    print(error)
# [missing] Lights/OffLights.schedule_name: "BadSched" not found in any of [ScheduleNames]
```

To stop on the first broken set of references instead:

```python
from idfpy import RefValidationError

try:
    idf.validate_or_raise()
except RefValidationError as exc:
    print(f'{len(exc.errors)} broken reference(s)')
```
