from typing import Any, NamedTuple

import numpy as np


# Subtype of tuple[int, int]
class XYGrid(NamedTuple):
    x_axis: int
    y_axis: int


# Test variance of _ShapeType_co
def accepts_2d(a: np.ndarray[tuple[int, int], Any]) -> None:
    return None
