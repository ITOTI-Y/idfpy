"""idfpy - EnergyPlus IDF models and file handling.

Type-safe Pydantic models for all EnergyPlus IDF object types,
plus IDF file read/write functionality.

Generated from Energy+.schema.epJSON version 25.1.
"""

from importlib.metadata import version

from idfpy.idf import IDF
from idfpy.models._base import IDFBaseModel

__version__ = version('idfpy')
__all__ = ['IDF', 'IDFBaseModel', '__version__']
