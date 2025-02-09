"""Module to expose more detailed version info for the installed `numtype`."""

import importlib.metadata
from typing import Final

__all__ = ["__version__"]
__version__: Final = importlib.metadata.version(__package__ or __file__.split("/")[-1])
