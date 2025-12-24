from typing import Any, assert_type, type_check_only

import _numtype as _nt
import numpy as np

###

@type_check_only
class SubArray(np.ndarray[Any, np.dtype[np.int64]]): ...

ints: list[int]
i8: np.int64

AR_b: _nt.Array[np.bool]
AR_u8: _nt.Array[np.uint64]
AR_i8: _nt.Array[np.int64]
AR_i8_sub: SubArray
AR_f8: _nt.Array[np.float64]
AR_c16: _nt.Array[np.complex128]
AR_m: _nt.Array[np.timedelta64]
AR_O: _nt.Array[np.object_]

###

assert_type(np.count_nonzero(i8), np.intp)
assert_type(np.count_nonzero(AR_i8), np.intp)
assert_type(np.count_nonzero(ints), np.intp)
assert_type(np.count_nonzero(AR_i8, keepdims=True), Any)
assert_type(np.count_nonzero(AR_i8, axis=0), Any)

assert_type(np.isfortran(i8), bool)
assert_type(np.isfortran(AR_i8), bool)

assert_type(np.argwhere(i8), _nt.Array[np.intp])
assert_type(np.argwhere(AR_i8), _nt.Array[np.intp])

assert_type(np.flatnonzero(i8), _nt.Array1D[np.intp])
assert_type(np.flatnonzero(AR_i8), _nt.Array1D[np.intp])

assert_type(np.correlate(ints, AR_i8, mode="valid"), _nt.Array1D[np.signedinteger])
assert_type(np.correlate(AR_i8, AR_i8, mode="same"), _nt.Array1D[np.signedinteger])
assert_type(np.correlate(AR_b, AR_b), _nt.Array1D[np.bool])
assert_type(np.correlate(AR_b, AR_u8), _nt.Array1D[np.unsignedinteger])
assert_type(np.correlate(AR_i8, AR_b), _nt.Array1D[np.signedinteger])
assert_type(np.correlate(AR_i8, AR_f8), _nt.Array1D[np.floating])
assert_type(np.correlate(AR_i8, AR_c16), _nt.Array1D[np.complexfloating])
# mypy incorrectly infers this as "ndarray[Any, Any]", but pyright behaves correctly
assert_type(np.correlate(AR_i8, AR_m), _nt.Array1D[np.timedelta64])  # type: ignore[assert-type]
assert_type(np.correlate(AR_O, AR_O), _nt.Array1D[np.object_])

assert_type(np.convolve(ints, AR_i8, mode="valid"), _nt.Array1D[np.signedinteger])
assert_type(np.convolve(AR_i8, AR_i8, mode="same"), _nt.Array1D[np.signedinteger])
assert_type(np.convolve(AR_b, AR_b), _nt.Array1D[np.bool])
assert_type(np.convolve(AR_b, AR_u8), _nt.Array1D[np.unsignedinteger])
assert_type(np.convolve(AR_i8, AR_b), _nt.Array1D[np.signedinteger])
assert_type(np.convolve(AR_i8, AR_f8), _nt.Array1D[np.floating])
assert_type(np.convolve(AR_i8, AR_c16), _nt.Array1D[np.complexfloating])
# mypy incorrectly infers this as "ndarray[Any, Any]", but pyright behaves correctly
assert_type(np.convolve(AR_i8, AR_m), _nt.Array1D[np.timedelta64])  # type: ignore[assert-type]
assert_type(np.convolve(AR_O, AR_O), _nt.Array1D[np.object_])

assert_type(np.outer(i8, AR_i8), _nt.Array2D[np.signedinteger])
assert_type(np.outer(ints, AR_i8), _nt.Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_i8), _nt.Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_i8, out=AR_i8_sub), SubArray)
assert_type(np.outer(AR_b, AR_b), _nt.Array2D[np.bool])
assert_type(np.outer(AR_b, AR_u8), _nt.Array2D[np.unsignedinteger])
assert_type(np.outer(AR_i8, AR_b), _nt.Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_f8), _nt.Array2D[np.floating])
assert_type(np.outer(AR_i8, AR_c16), _nt.Array2D[np.complexfloating])
assert_type(np.outer(AR_i8, AR_m), _nt.Array2D[np.timedelta64])
assert_type(np.outer(AR_O, AR_O), _nt.Array2D[np.object_])

assert_type(np.tensordot(ints, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8, axes=0), _nt.Array[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8, axes=(0, 1)), _nt.Array[np.signedinteger])
assert_type(np.tensordot(AR_b, AR_b), _nt.Array[np.bool])
assert_type(np.tensordot(AR_b, AR_u8), _nt.Array[np.unsignedinteger])
assert_type(np.tensordot(AR_i8, AR_b), _nt.Array[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_f8), _nt.Array[np.floating])
assert_type(np.tensordot(AR_i8, AR_c16), _nt.Array[np.complexfloating])
# mypy incorrectly infers this as "ndarray[Any, Any]", but pyright behaves correctly
assert_type(np.tensordot(AR_i8, AR_m), _nt.Array[np.timedelta64])  # type: ignore[assert-type]
assert_type(np.tensordot(AR_O, AR_O), _nt.Array[np.object_])

assert_type(np.isscalar(i8), bool)
assert_type(np.isscalar(AR_i8), bool)
assert_type(np.isscalar(ints), bool)

assert_type(np.roll(AR_i8, 1), _nt.Array[np.int64])
assert_type(np.roll(AR_i8, (1, 2)), _nt.Array[np.int64])
assert_type(np.roll(ints, 1), _nt.Array[Any])

assert_type(np.rollaxis(AR_i8, 0, 1), _nt.Array[np.int64])

assert_type(np.moveaxis(AR_i8, 0, 1), _nt.Array[np.int64])
assert_type(np.moveaxis(AR_i8, (0, 1), (1, 2)), _nt.Array[np.int64])

assert_type(np.cross(ints, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.cross(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.cross(AR_b, AR_u8), _nt.Array[np.unsignedinteger])
assert_type(np.cross(AR_i8, AR_b), _nt.Array[np.signedinteger])
assert_type(np.cross(AR_i8, AR_f8), _nt.Array[np.floating])
assert_type(np.cross(AR_i8, AR_c16), _nt.Array[np.complexfloating])

assert_type(np.indices([0, 1, 2]), _nt.Array[np.int_])
assert_type(np.indices([0, 1, 2], sparse=True), tuple[_nt.Array[np.int_], ...])
assert_type(np.indices([0, 1, 2], dtype=np.float64), _nt.Array[np.float64])
assert_type(np.indices([0, 1, 2], sparse=True, dtype=np.float64), tuple[_nt.Array[np.float64], ...])
assert_type(np.indices([0, 1, 2], dtype=float), _nt.Array[Any])
assert_type(np.indices([0, 1, 2], sparse=True, dtype=float), tuple[_nt.Array[Any], ...])

assert_type(np.binary_repr(1), str)

assert_type(np.base_repr(1), str)

assert_type(np.allclose(i8, AR_i8), bool)
assert_type(np.allclose(ints, AR_i8), bool)
assert_type(np.allclose(AR_i8, AR_i8), bool)

assert_type(np.isclose(i8, i8), np.bool)
assert_type(np.isclose(i8, AR_i8), _nt.Array[np.bool])
assert_type(np.isclose(ints, AR_i8), _nt.Array[np.bool])
assert_type(np.isclose(AR_i8, AR_i8), _nt.Array[np.bool])

assert_type(np.array_equal(i8, AR_i8), bool)
assert_type(np.array_equal(ints, AR_i8), bool)
assert_type(np.array_equal(AR_i8, AR_i8), bool)

assert_type(np.array_equiv(i8, AR_i8), bool)
assert_type(np.array_equiv(ints, AR_i8), bool)
assert_type(np.array_equiv(AR_i8, AR_i8), bool)
