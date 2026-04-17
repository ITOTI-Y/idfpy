"""Exception and error types for idfpy."""

from __future__ import annotations

from dataclasses import dataclass


class UnknownObjectTypeError(ValueError):
    """Raised when an object type name or class cannot be resolved.

    Raised by IDF query methods (``get`` / ``has`` / ``all_of_type`` /
    ``remove``) and :meth:`IDFBaseModel.referencing` when ``strict=True``
    (the default) and the input key does not map to any EnergyPlus
    object type.

    Attributes:
        key: The input key that failed resolution (``type`` or ``str``).
    """

    def __init__(self, key: type | str) -> None:
        self.key = key
        repr_str = key.__name__ if isinstance(key, type) else repr(key)
        super().__init__(
            f'Unknown object type: {repr_str}. Must be a subclass of '
            f'IDFBaseModel, an EnergyPlus object type name '
            f'(e.g., "Zone", "BuildingSurface:Detailed"), or a Python '
            f'class name (e.g., "Zone", "BuildingSurfaceDetailed").'
        )


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
