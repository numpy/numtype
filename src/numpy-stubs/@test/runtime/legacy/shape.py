from typing import TYPE_CHECKING, Any, NamedTuple

import numpy as np

if TYPE_CHECKING:
    import _numtype as _nt


# Subtype of tuple[int, int]
class XYGrid(NamedTuple):
    x_axis: int
    y_axis: int


# Test variance of _ShapeType_co
def accepts_2d(a: "np.ndarray[_nt.Shape2, Any]") -> None:
    return None


accepts_2d(np.empty(XYGrid(2, 2)))
accepts_2d(np.zeros(XYGrid(2, 2), dtype=int))
accepts_2d(np.ones(XYGrid(2, 2), dtype=int))
accepts_2d(np.full(XYGrid(2, 2), fill_value=5, dtype=int))
