from typing import Any, assert_type

import _numtype as _nt
import numpy as np

mat_i8: _nt.Matrix[np.int64]
arr_f8: _nt.Array[np.float64]

i_3d: list[list[list[int]]]

###

assert_type(mat_i8 * 5, _nt.Matrix)
assert_type(5 * mat_i8, _nt.Matrix)
mat_i8 *= 5

assert_type(mat_i8**5, _nt.Matrix)
mat_i8 **= 5

assert_type(mat_i8.sum(), Any)
assert_type(mat_i8.mean(), Any)
assert_type(mat_i8.std(), Any)
assert_type(mat_i8.var(), Any)
assert_type(mat_i8.prod(), Any)
assert_type(mat_i8.any(), np.bool)
assert_type(mat_i8.all(), np.bool)
assert_type(mat_i8.max(), np.int64)
assert_type(mat_i8.min(), np.int64)
assert_type(mat_i8.argmax(), np.intp)
assert_type(mat_i8.argmin(), np.intp)
assert_type(mat_i8.ptp(), np.int64)

assert_type(mat_i8.sum(axis=0), _nt.Matrix)
assert_type(mat_i8.mean(axis=0), _nt.Matrix)
assert_type(mat_i8.std(axis=0), _nt.Matrix)
assert_type(mat_i8.var(axis=0), _nt.Matrix)
assert_type(mat_i8.prod(axis=0), _nt.Matrix)
assert_type(mat_i8.any(axis=0), _nt.Matrix[np.bool_])
assert_type(mat_i8.all(axis=0), _nt.Matrix[np.bool_])
assert_type(mat_i8.max(axis=0), _nt.Matrix[np.int64])
assert_type(mat_i8.min(axis=0), _nt.Matrix[np.int64])
assert_type(mat_i8.argmax(axis=0), _nt.Matrix[np.intp])
assert_type(mat_i8.argmin(axis=0), _nt.Matrix[np.intp])
assert_type(mat_i8.ptp(axis=0), _nt.Matrix[np.int64])

assert_type(mat_i8.sum(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.mean(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.std(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.var(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.prod(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.any(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.all(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.max(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.min(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.argmax(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.argmin(out=arr_f8), _nt.Array[np.float64])
assert_type(mat_i8.ptp(out=arr_f8), _nt.Array[np.float64])

assert_type(mat_i8.T, _nt.Matrix[np.int64])
assert_type(mat_i8.I, _nt.Matrix)
assert_type(mat_i8.A, _nt.Array2D[np.int64])
assert_type(mat_i8.A1, _nt.Array1D[np.int64])
assert_type(mat_i8.H, _nt.Matrix[np.int64])
assert_type(mat_i8.getT(), _nt.Matrix[np.int64])
assert_type(mat_i8.getI(), _nt.Matrix)
assert_type(mat_i8.getA(), _nt.Array2D[np.int64])
assert_type(mat_i8.getA1(), _nt.Array1D[np.int64])
assert_type(mat_i8.getH(), _nt.Matrix[np.int64])

assert_type(np.bmat(arr_f8), _nt.Matrix[np.float64])
assert_type(np.bmat(i_3d), _nt.Matrix[np.intp])
assert_type(np.bmat("mat"), _nt.Matrix)

assert_type(np.asmatrix(arr_f8, dtype=np.int64), _nt.Matrix[np.int64])
