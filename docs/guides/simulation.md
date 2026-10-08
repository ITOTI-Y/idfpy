# Running simulations

`idfpy.sim` runs the EnergyPlus executable, so EnergyPlus must be installed.
By default the `energyplus` command on `PATH` is used; pass `energyplus_bin`
to choose another installation.

## One simulation

```python
from pathlib import Path

from idfpy.sim import simulate

result = simulate(
    Path('model.idf'),
    weather=Path('weather.epw'),
    output_dir=Path('results'),
    annual=True,  # -a
    readvars=True,  # -r, convert ESO output to CSV
)
```

`simulate` also accepts an in-memory `IDF`. It is written to a temporary file
first, so `output_dir` is required in that case:

```python
result = simulate(idf, weather=Path('weather.epw'), output_dir=Path('results'))
```

HVACTemplate objects are expanded with ExpandObjects unless you pass
`expand_objects=False`.

## Reading the result

```python
result.success  # True when EnergyPlus exited with code 0
result.return_code
result.end_message  # contents of eplusout.end
result.err  # ErrSummary parsed from eplusout.err, or None

if result.err:
    print(result.err.warning_count, result.err.severe_count, result.err.has_fatal)
```

## Many simulations

`simulate_batch` runs jobs concurrently, by default on all but one CPU core.

```python
from idfpy.sim import SimJob, simulate_batch

jobs = [
    SimJob(
        idf=Path(f'variant_{i}.idf'),
        weather=Path('weather.epw'),
        output_dir=Path(f'results/{i}'),
    )
    for i in range(8)
]
results = simulate_batch(jobs, max_concurrent=4)
failed = [job.idf for job, r in zip(jobs, results) if not r.success]
```

Inside an existing event loop use `async_simulate` and
`async_simulate_batch`, which take the same arguments.
