"""Simulation job configuration."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel


class SimJob(BaseModel):
    """Single simulation job definition."""

    idf: Path
    weather: Path
    output_dir: Path | None = None
    design_day: bool = False
    annual: bool = False
    output_prefix: str | None = None
