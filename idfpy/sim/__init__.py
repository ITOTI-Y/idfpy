"""EnergyPlus simulation runner.

Public API:
    simulate        — run a single simulation (sync)
    simulate_batch  — run multiple simulations concurrently (sync)
    async_simulate  — single simulation (async)
    async_simulate_batch — batch simulation (async)
"""

from __future__ import annotations

from pathlib import Path

import anyio

from ._runner import _batch, _resolve_idf, _run_one
from .config import SimJob
from .result import ErrSummary, SimResult

__all__ = [
    'ErrSummary',
    'SimJob',
    'SimResult',
    'async_simulate',
    'async_simulate_batch',
    'simulate',
    'simulate_batch',
]


def simulate(
    idf: object,
    weather: Path,
    *,
    output_dir: Path | None = None,
    energyplus_bin: str = 'energyplus',
    design_day: bool = False,
    annual: bool = False,
    expand_objects: bool = True,
    echo: bool = True,
) -> SimResult:
    """Run a single EnergyPlus simulation (sync).

    Args:
        idf: IDF object or Path to IDF file.
        weather: Path to EPW weather file.
        output_dir: Output directory. Defaults to the IDF file's parent
            when *idf* is a Path. Required when *idf* is an in-memory IDF
            object (raises ValueError if omitted).
        energyplus_bin: Path to EnergyPlus executable.
        design_day: Run design-day-only simulation (-D).
        annual: Run annual simulation (-a).
        expand_objects: Expand HVACTemplate objects (-x).
        echo: Print EnergyPlus output to terminal in real time.
    """
    return anyio.run(
        lambda: async_simulate(
            idf,
            weather,
            output_dir=output_dir,
            energyplus_bin=energyplus_bin,
            design_day=design_day,
            annual=annual,
            expand_objects=expand_objects,
            echo=echo,
        )
    )


def simulate_batch(
    jobs: list[SimJob],
    *,
    max_concurrent: int = 4,
    energyplus_bin: str = 'energyplus',
    expand_objects: bool = True,
    echo: bool = False,
) -> list[SimResult]:
    """Run multiple EnergyPlus simulations concurrently (sync).

    Args:
        jobs: List of simulation jobs.
        max_concurrent: Maximum concurrent EnergyPlus processes.
        energyplus_bin: Path to EnergyPlus executable.
        expand_objects: Expand HVACTemplate objects (-x).
        echo: Print EnergyPlus output to terminal.
    """
    return anyio.run(
        lambda: async_simulate_batch(
            jobs,
            max_concurrent=max_concurrent,
            energyplus_bin=energyplus_bin,
            expand_objects=expand_objects,
            echo=echo,
        )
    )


async def async_simulate(
    idf: object,
    weather: Path,
    *,
    output_dir: Path | None = None,
    energyplus_bin: str = 'energyplus',
    design_day: bool = False,
    annual: bool = False,
    expand_objects: bool = True,
    echo: bool = True,
) -> SimResult:
    """Run a single EnergyPlus simulation (async).

    Same interface as simulate() but meant to be awaited inside an
    existing event loop. *output_dir* is required when *idf* is an
    in-memory IDF object; it defaults to the file's parent only when
    *idf* is a Path.
    """
    if output_dir is None and not isinstance(idf, Path):
        raise ValueError(
            'output_dir is required when idf is an IDF object '
            '(temp IDF directory is cleaned up after simulation)'
        )

    with _resolve_idf(idf) as idf_path:
        if output_dir is None:
            output_dir = idf_path.parent

        return await _run_one(
            idf_path,
            weather,
            output_dir,
            energyplus_bin,
            expand_objects=expand_objects,
            design_day=design_day,
            annual=annual,
            echo=echo,
        )


async def async_simulate_batch(
    jobs: list[SimJob],
    *,
    max_concurrent: int = 4,
    energyplus_bin: str = 'energyplus',
    expand_objects: bool = True,
    echo: bool = False,
) -> list[SimResult]:
    """Run multiple EnergyPlus simulations concurrently (async).

    Same interface as simulate_batch() but meant to be awaited
    inside an existing event loop.
    """
    return await _batch(
        jobs,
        max_concurrent,
        energyplus_bin,
        expand_objects=expand_objects,
        echo=echo,
    )
