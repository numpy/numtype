from collections.abc import Callable
from typing import Any

from setuptools import Distribution

from .extension import Extension as Extension

have_setuptools: bool
numpy_cmdclass: dict[str, Callable[..., Any]]

def get_distribution(always: bool = False) -> Distribution | None: ...
def setup(**attr: object) -> Distribution: ...
