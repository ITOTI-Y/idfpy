"""Simulation result models."""

from __future__ import annotations

import re
from pathlib import Path

from pydantic import BaseModel, ConfigDict


class ErrSummary(BaseModel):
    """Parsed summary of an eplusout.err file."""

    warnings: list[str]
    severe_errors: list[str]
    fatal_errors: list[str]

    @property
    def warning_count(self) -> int:
        return len(self.warnings)

    @property
    def severe_count(self) -> int:
        return len(self.severe_errors)

    @property
    def has_fatal(self) -> bool:
        return len(self.fatal_errors) > 0

    @classmethod
    def from_file(cls, path: Path) -> ErrSummary:
        """Parse an eplusout.err file into structured summary."""
        text = path.read_text(encoding='utf-8', errors='replace')
        warnings: list[str] = []
        severe_errors: list[str] = []
        fatal_errors: list[str] = []

        for match in re.finditer(r'\*\*\s*(Warning|Severe|Fatal)\s*\*\*\s*(.*)', text):
            category, message = match.group(1), match.group(2).strip()
            if category == 'Warning':
                warnings.append(message)
            elif category == 'Severe':
                severe_errors.append(message)
            elif category == 'Fatal':
                fatal_errors.append(message)

        return cls(
            warnings=warnings,
            severe_errors=severe_errors,
            fatal_errors=fatal_errors,
        )


class SimResult(BaseModel):
    """EnergyPlus simulation result."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    return_code: int
    output_dir: Path
    stdout: str

    @property
    def success(self) -> bool:
        return self.return_code == 0

    @property
    def end_message(self) -> str | None:
        """Read eplusout.end file content."""
        end_file = self.output_dir / 'eplusout.end'
        if end_file.exists():
            return end_file.read_text().strip()
        return None

    @property
    def err(self) -> ErrSummary | None:
        """Parse eplusout.err file summary."""
        err_file = self.output_dir / 'eplusout.err'
        if not err_file.exists():
            return None
        return ErrSummary.from_file(err_file)
