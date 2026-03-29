"""Reference validation error types."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RefError:
    """Single broken reference."""

    object_type: str
    object_name: str
    field_name: str
    ref_group: str
    referenced_name: str
    error_type: str  # "missing" | "type_mismatch"
    detail: str

    def __str__(self) -> str:
        return (
            f'[{self.error_type}] {self.object_type}/{self.object_name}'
            f'.{self.field_name}: {self.detail}'
        )


class RefValidationError(Exception):
    """Raised by IDF.validate_or_raise() when references are broken."""

    def __init__(self, errors: list[RefError]) -> None:
        self.errors = errors
        summary = f'{len(errors)} broken reference(s)'
        details = '\n'.join(f'  {e}' for e in errors[:20])
        if len(errors) > 20:
            details += f'\n  ... and {len(errors) - 20} more'
        super().__init__(f'{summary}:\n{details}')
