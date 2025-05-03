from typing import Any, TypeAlias, assert_type

import numpy as np
import numpy.typing as npt

_1D: TypeAlias = tuple[int]  # noqa: PYI042
_2D: TypeAlias = tuple[int, int]  # noqa: PYI042

mat: np.matrix[_2D, np.dtype[np.int64]]
ar_f8: npt.NDArray[np.float64]

i_3d: list[list[list[int]]]

###

assert_type(mat * 5, np.matrix[_2D, np.dtype])
assert_type(5 * mat, np.matrix[_2D, np.dtype])
mat *= 5

assert_type(mat**5, np.matrix[_2D, np.dtype])
mat **= 5

assert_type(mat.sum(), Any)
assert_type(mat.mean(), Any)
assert_type(mat.std(), Any)
assert_type(mat.var(), Any)
assert_type(mat.prod(), Any)
assert_type(mat.any(), np.bool)
assert_type(mat.all(), np.bool)
assert_type(mat.max(), np.int64)
assert_type(mat.min(), np.int64)
assert_type(mat.argmax(), np.intp)
assert_type(mat.argmin(), np.intp)
assert_type(mat.ptp(), np.int64)

assert_type(mat.sum(axis=0), np.matrix[_2D, np.dtype])
assert_type(mat.mean(axis=0), np.matrix[_2D, np.dtype])
assert_type(mat.std(axis=0), np.matrix[_2D, np.dtype])
assert_type(mat.var(axis=0), np.matrix[_2D, np.dtype])
assert_type(mat.prod(axis=0), np.matrix[_2D, np.dtype])
assert_type(mat.any(axis=0), np.matrix[_2D, np.dtype[np.bool]])
assert_type(mat.all(axis=0), np.matrix[_2D, np.dtype[np.bool]])
assert_type(mat.max(axis=0), np.matrix[_2D, np.dtype[np.int64]])
assert_type(mat.min(axis=0), np.matrix[_2D, np.dtype[np.int64]])
assert_type(mat.argmax(axis=0), np.matrix[_2D, np.dtype[np.intp]])
assert_type(mat.argmin(axis=0), np.matrix[_2D, np.dtype[np.intp]])
assert_type(mat.ptp(axis=0), np.matrix[_2D, np.dtype[np.int64]])

assert_type(mat.sum(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.mean(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.std(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.var(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.prod(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.any(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.all(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.max(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.min(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.argmax(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.argmin(out=ar_f8), npt.NDArray[np.float64])
assert_type(mat.ptp(out=ar_f8), npt.NDArray[np.float64])

assert_type(mat.T, np.matrix[_2D, np.dtype[np.int64]])
assert_type(mat.I, np.matrix[_2D, np.dtype])
assert_type(mat.A, np.ndarray[_2D, np.dtype[np.int64]])
assert_type(mat.A1, np.ndarray[_1D, np.dtype[np.int64]])
assert_type(mat.H, np.matrix[_2D, np.dtype[np.int64]])
assert_type(mat.getT(), np.matrix[_2D, np.dtype[np.int64]])
assert_type(mat.getI(), np.matrix[_2D, np.dtype])
assert_type(mat.getA(), np.ndarray[_2D, np.dtype[np.int64]])
assert_type(mat.getA1(), np.ndarray[_1D, np.dtype[np.int64]])
assert_type(mat.getH(), np.matrix[_2D, np.dtype[np.int64]])

assert_type(np.bmat(ar_f8), np.matrix[_2D, np.dtype[np.float64]])
assert_type(np.bmat(i_3d), np.matrix[_2D, np.dtype[np.intp]])
assert_type(np.bmat("mat"), np.matrix[_2D, np.dtype])

assert_type(np.asmatrix(ar_f8, dtype=np.int64), np.matrix[_2D, np.dtype[np.int64]])
