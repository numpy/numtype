from collections.abc import Iterable
from typing import Any

import numpy as np
import numpy.typing as npt

__all__ = ["byte_bounds", "normalize_axis_index", "normalize_axis_tuple"]

# NOTE: In practice `byte_bounds` can (potentially) take any object
# implementing the `__array_interface__` protocol. The caveat is
# that certain keys, marked as optional in the spec, must be present for
#  `byte_bounds`. This concerns `"strides"` and `"data"`.
def byte_bounds(a: np.generic | npt.NDArray[Any]) -> tuple[int, int]: ...
def normalize_axis_index(axis: int = ..., ndim: int = ..., msg_prefix: str | None = ...) -> int: ...
def normalize_axis_tuple(
    axis: int | Iterable[int],
    ndim: int = ...,
    argname: str | None = ...,
    allow_duplicate: bool | None = ...,
) -> tuple[int, int]: ...
