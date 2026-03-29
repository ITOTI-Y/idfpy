"""Benchmark script for idfpy hot paths.

Usage:
    uv run python benchmarks/bench_idf.py
"""

from __future__ import annotations

try:
    import resource

    HAS_RESOURCE = True
except ImportError:
    HAS_RESOURCE = False
import statistics
import tempfile
import time
from pathlib import Path

from loguru import logger

from idfpy import IDF

logger.disable('idfpy')


TEST_IDF = Path(__file__).parent.parent / 'tests' / 'test.idf'
ITERATIONS = 10


def _bench(label: str, func: object, iterations: int = ITERATIONS) -> float:
    """Run func() *iterations* times and print timing stats.

    Returns median time in ms.
    """
    times_ms: list[float] = []
    for _ in range(iterations):
        t0 = time.perf_counter_ns()
        func()  # type: ignore
        elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
        times_ms.append(elapsed_ms)

    mean = statistics.mean(times_ms)
    median = statistics.median(times_ms)
    p95 = sorted(times_ms)[int(len(times_ms) * 0.95)]
    print(
        f'  {label:40s}  mean={mean:8.2f}ms  median={median:8.2f}ms  p95={p95:8.2f}ms'
    )
    return median


def bench_load() -> IDF:
    """Benchmark IDF.load()."""
    idf: IDF = IDF()

    def _load() -> None:
        nonlocal idf
        idf = IDF.load(TEST_IDF)

    _bench('load (IDF text)', _load)
    return idf


def bench_add() -> None:
    """Benchmark bulk add of Zone objects."""
    from idfpy.models.thermal_zones import Zone

    def _add_500() -> None:
        idf = IDF()
        for i in range(500):
            idf.add(Zone(name=f'BenchZone_{i}'))

    _bench('add 500 Zones', _add_500)


def bench_validate(idf: IDF) -> None:
    """Benchmark validate()."""
    _bench('validate', idf.validate)


def bench_reverse_nav_single(idf: IDF) -> None:
    """Benchmark reverse nav for a single consumer type."""
    zones = idf.all_of_type('Zone')
    if not zones:
        print('  [skip] no zones in test file')
        return
    zone = next(iter(zones.values()))

    def _rev() -> None:
        zone.referencing('BuildingSurface:Detailed')

    _bench('reverse nav (single type)', _rev)


def bench_reverse_nav_all(idf: IDF) -> None:
    """Benchmark reverse nav across all types."""
    zones = idf.all_of_type('Zone')
    if not zones:
        print('  [skip] no zones in test file')
        return
    zone = next(iter(zones.values()))

    def _rev_all() -> None:
        zone.referencing()

    _bench('reverse nav (all types)', _rev_all)


def bench_save_idf(idf: IDF) -> None:
    """Benchmark save in IDF format."""
    with tempfile.NamedTemporaryFile(suffix='.idf', delete=False) as f:
        path = Path(f.name)

    def _save() -> None:
        idf.save(path, output_type='idf')

    _bench('save IDF', _save)
    path.unlink(missing_ok=True)


def bench_save_epjson(idf: IDF) -> None:
    """Benchmark save in epJSON format."""
    with tempfile.NamedTemporaryFile(suffix='.epjson', delete=False) as f:
        path = Path(f.name)

    def _save() -> None:
        idf.save(path, output_type='epjson')

    _bench('save epJSON', _save)
    path.unlink(missing_ok=True)


def bench_to_dict_roundtrip(idf: IDF) -> None:
    """Benchmark to_dict / from_dict roundtrip."""

    def _roundtrip() -> None:
        data = idf.to_dict()
        IDF.from_dict(data)

    _bench('to_dict / from_dict roundtrip', _roundtrip)


def main() -> None:
    print(f'=== idfpy benchmark ({TEST_IDF.name}, {ITERATIONS} iterations) ===\n')

    ru_before = (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if HAS_RESOURCE else 0
    )

    idf = bench_load()
    print(f'  (loaded {len(idf)} objects)\n')

    bench_add()
    bench_validate(idf)
    bench_reverse_nav_single(idf)
    bench_reverse_nav_all(idf)
    bench_save_idf(idf)
    bench_save_epjson(idf)
    bench_to_dict_roundtrip(idf)

    if HAS_RESOURCE:
        ru_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(f'\n  Peak RSS: {ru_after} KB  (delta: +{ru_after - ru_before} KB)')
    else:
        print('\n  Peak RSS: [unavailable on this platform]')


if __name__ == '__main__':
    main()
