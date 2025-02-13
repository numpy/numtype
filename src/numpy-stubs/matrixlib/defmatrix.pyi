from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np
from numpy import matrix  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, NDArray

__all__ = ["asmatrix", "bmat", "matrix"]

def bmat(
    obj: str | Sequence[ArrayLike] | NDArray[Any],
    ldict: Mapping[str, Any] | None = ...,
    gdict: Mapping[str, Any] | None = ...,
) -> np.matrix[tuple[int, int], Any]: ...
def asmatrix(data: ArrayLike, dtype: DTypeLike = ...) -> matrix[tuple[int, int], Any]: ...

mat = asmatrix
