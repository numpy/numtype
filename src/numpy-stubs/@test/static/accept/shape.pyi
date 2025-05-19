from typing import Any, NamedTuple, assert_type

import numpy as np

# Subtype of tuple[int, int]
class XYGrid(NamedTuple):
    x_axis: int
    y_axis: int

arr: np.ndarray[XYGrid, Any]

# NOTE(jorenham): mypy 1.15 ignores the typevar constraints, and incorrectly infers `XYGrid``
assert_type(arr.shape, tuple[int, int])  # type: ignore[assert-type]
