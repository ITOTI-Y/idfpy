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
ITERATIONS = 20
WARMUP = 3


def _bench(
    label: str,
    func: object,
    iterations: int = ITERATIONS,
    warmup: int = WARMUP,
) -> float:
    """Run func() *iterations* times (after warmup) and print timing stats.

    Returns median time in ms.
    """
    for _ in range(warmup):
        func()  # type: ignore

    rss_before = (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if HAS_RESOURCE else 0
    )

    times_ms: list[float] = []
    for _ in range(iterations):
        t0 = time.perf_counter_ns()
        func()  # type: ignore
        elapsed_ms = (time.perf_counter_ns() - t0) / 1e6
        times_ms.append(elapsed_ms)

    rss_after = (
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if HAS_RESOURCE else 0
    )
    rss_delta = rss_after - rss_before

    mean = statistics.mean(times_ms)
    median = statistics.median(times_ms)
    p95 = sorted(times_ms)[int(len(times_ms) * 0.95)]
    rss_str = f'  RSS delta: +{rss_delta}KB' if HAS_RESOURCE else ''
    print(
        f'  {label:40s}  mean={mean:8.2f}ms  median={median:8.2f}ms'
        f'  p95={p95:8.2f}ms{rss_str}'
    )
    return median


# ── Core benchmarks ─────────────────────────────────────────


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


# ── Micro-benchmarks ───────────────────────────────────────


def bench_parse_only() -> None:
    """Benchmark _parse_idf_content() in isolation (no file I/O)."""
    content = TEST_IDF.read_text(encoding='utf-8')

    def _parse() -> None:
        IDF._parse_idf_content(content)

    _bench('parse only (no file I/O)', _parse)


def bench_to_dict_only(idf: IDF) -> None:
    """Benchmark to_dict() in isolation."""
    _bench('to_dict only', idf.to_dict)


def bench_from_dict_only(idf: IDF) -> None:
    """Benchmark from_dict() in isolation."""
    data = idf.to_dict()

    def _from_dict() -> None:
        IDF.from_dict(data)

    _bench('from_dict only', _from_dict)


def bench_format_object(idf: IDF) -> None:
    """Benchmark _format_object() for a single object with extensible fields."""
    from idfpy.models import get_field_order

    # Find an object with extensible fields (e.g., BuildingSurface:Detailed)
    surfaces = idf.all_of_type('BuildingSurface:Detailed')
    if not surfaces:
        print('  [skip] no BuildingSurface:Detailed in test file')
        return
    surface = next(iter(surfaces.values()))
    field_order = get_field_order('BuildingSurface:Detailed')

    def _format() -> None:
        idf._format_object(surface, 'BuildingSurface:Detailed', field_order)

    _bench('format_object (extensible)', _format)


def bench_cascade_rename(idf: IDF) -> None:
    """Benchmark cascade rename of a zone."""
    zones = idf.all_of_type('Zone')
    if not zones:
        print('  [skip] no zones in test file')
        return
    zone_name = next(iter(zones.keys()))
    zone = zones[zone_name]

    counter = 0

    def _rename() -> None:
        nonlocal counter
        counter += 1
        zone.name = f'{zone_name}_bench_{counter}'

    _bench('cascade rename', _rename)
    # Restore original name
    zone.name = zone_name


# ── Main ────────────────────────────────────────────────────


def main() -> None:
    print(
        f'=== idfpy benchmark ({TEST_IDF.name}, {ITERATIONS} iters,'
        f' {WARMUP} warmup) ===\n'
    )

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

    print('\n--- Micro-benchmarks ---\n')

    bench_parse_only()
    bench_to_dict_only(idf)
    bench_from_dict_only(idf)
    bench_format_object(idf)
    bench_cascade_rename(idf)

    if HAS_RESOURCE:
        ru_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        print(f'\n  Peak RSS: {ru_after} KB  (delta: +{ru_after - ru_before} KB)')
    else:
        print('\n  Peak RSS: [unavailable on this platform]')


if __name__ == '__main__':
    main()
