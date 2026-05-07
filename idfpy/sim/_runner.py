"""Async simulation runner core."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import TYPE_CHECKING

import anyio
from anyio.streams.text import TextReceiveStream
from loguru import logger

from .config import SimJob
from .result import SimResult

if TYPE_CHECKING:
    from collections.abc import Iterator


def _build_cmd(
    idf_path: Path,
    weather: Path,
    output_dir: Path,
    energyplus_bin: str,
    *,
    expand_objects: bool,
    design_day: bool,
    annual: bool,
    readvars: bool,
) -> list[str]:
    """Build EnergyPlus command line arguments."""
    cmd = [energyplus_bin]
    if expand_objects:
        cmd.append('-x')
    if readvars:
        cmd.append('-r')
    if design_day:
        cmd.append('-D')
    if annual:
        cmd.append('-a')
    cmd.extend(['-w', str(weather), '-d', str(output_dir), str(idf_path)])
    return cmd


@contextmanager
def _resolve_idf(idf: object) -> Iterator[Path]:
    """Resolve IDF object or Path to a file path.

    Context manager that yields the resolved path. When *idf* is an IDF
    object, a temporary directory is created, the model is saved into it,
    and the directory is cleaned up on exit.
    """
    if isinstance(idf, Path):
        if not idf.exists():
            raise FileNotFoundError(f'IDF file not found: {idf}')
        yield idf
        return

    # Duck-type check for IDF objects with a save() method
    save = getattr(idf, 'save', None)
    if save is None:
        raise TypeError(f'Expected Path or IDF object, got {type(idf).__name__}')

    tmp_dir = tempfile.TemporaryDirectory()
    try:
        tmp_path = Path(tmp_dir.name) / 'model.idf'
        save(tmp_path)
        yield tmp_path
    finally:
        tmp_dir.cleanup()


async def _run_one(
    idf_path: Path,
    weather: Path,
    output_dir: Path,
    energyplus_bin: str,
    *,
    expand_objects: bool = True,
    design_day: bool = False,
    annual: bool = False,
    readvars: bool = False,
    echo: bool = True,
) -> SimResult:
    """Run a single EnergyPlus simulation (async core).

    Uses TextReceiveStream for line-buffered stdout reading, ensuring
    complete lines in echo mode and faithful stdout capture.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = _build_cmd(
        idf_path,
        weather,
        output_dir,
        energyplus_bin,
        expand_objects=expand_objects,
        design_day=design_day,
        annual=annual,
        readvars=readvars,
    )

    logger.info('Running: {}', ' '.join(cmd))

    lines: list[str] = []
    async with await anyio.open_process(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    ) as proc:
        assert proc.stdout is not None  # noqa: S101
        async for line in TextReceiveStream(proc.stdout):
            lines.append(line)
            if echo:
                sys.stdout.write(line)
                sys.stdout.flush()

    if proc.returncode == 0:
        logger.info('EnergyPlus completed successfully')
    else:
        logger.error('EnergyPlus failed with code {}', proc.returncode)

    return SimResult(
        return_code=proc.returncode if proc.returncode is not None else -1,
        output_dir=output_dir,
        stdout=''.join(lines),
    )


async def _batch(
    jobs: list[SimJob],
    max_concurrent: int,
    energyplus_bin: str,
    *,
    expand_objects: bool = True,
    readvars: bool = False,
    echo: bool = False,
) -> list[SimResult]:
    """Run multiple simulations concurrently.

    Uses CapacityLimiter to control concurrent EnergyPlus processes
    and create_task_group for structured concurrency. Individual task
    exceptions are caught and recorded as failed SimResults.
    """
    # Pre-compute output dirs and validate uniqueness
    output_dirs: list[Path] = []
    for i, job in enumerate(jobs):
        output_dirs.append(
            job.output_dir.resolve()
            if job.output_dir
            else Path(f'run_{i:04d}').resolve()
        )
    seen: dict[Path, int] = {}
    for i, d in enumerate(output_dirs):
        if d in seen:
            raise ValueError(f'Duplicate output_dir {d} for jobs {seen[d]} and {i}')
        seen[d] = i

    limiter = anyio.CapacityLimiter(max_concurrent)
    results: list[SimResult | None] = [None] * len(jobs)

    async def _run_indexed(index: int, job: SimJob) -> None:
        output_dir = output_dirs[index]
        try:
            async with limiter:
                results[index] = await _run_one(
                    idf_path=job.idf,
                    weather=job.weather,
                    output_dir=output_dir,
                    energyplus_bin=energyplus_bin,
                    expand_objects=expand_objects,
                    design_day=job.design_day,
                    annual=job.annual,
                    readvars=readvars,
                    echo=echo,
                )
        except Exception as exc:
            logger.error('Job {} ({}) failed: {}', index, job.idf, exc)
            results[index] = SimResult(
                return_code=-1,
                output_dir=output_dir,
                stdout=str(exc),
            )

    async with anyio.create_task_group() as tg:
        for i, job in enumerate(jobs):
            tg.start_soon(_run_indexed, i, job)

    return results  # ty: ignore[invalid-return-type]
