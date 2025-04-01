from typing import Any, TypeAlias, type_check_only
from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]
_Array2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_ScalarT]]

###

@type_check_only
class SubArray(npt.NDArray[np.int64]): ...

ints: list[int]
i8: np.int64

AR_b: npt.NDArray[np.bool]
AR_u8: npt.NDArray[np.uint64]
AR_i8: npt.NDArray[np.int64]
AR_i8_sub: SubArray
AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
AR_m: npt.NDArray[np.timedelta64]
AR_O: npt.NDArray[np.object_]

###

assert_type(np.count_nonzero(i8), int)
assert_type(np.count_nonzero(AR_i8), int)
assert_type(np.count_nonzero(ints), int)
assert_type(np.count_nonzero(AR_i8, keepdims=True), Any)
assert_type(np.count_nonzero(AR_i8, axis=0), Any)

assert_type(np.isfortran(i8), bool)
assert_type(np.isfortran(AR_i8), bool)

assert_type(np.argwhere(i8), npt.NDArray[np.intp])
assert_type(np.argwhere(AR_i8), npt.NDArray[np.intp])

assert_type(np.flatnonzero(i8), _Array1D[np.intp])
assert_type(np.flatnonzero(AR_i8), _Array1D[np.intp])

assert_type(np.correlate(ints, AR_i8, mode="valid"), _Array1D[np.signedinteger])
assert_type(np.correlate(AR_i8, AR_i8, mode="same"), _Array1D[np.signedinteger])
assert_type(np.correlate(AR_b, AR_b), _Array1D[np.bool])
assert_type(np.correlate(AR_b, AR_u8), _Array1D[np.unsignedinteger])
assert_type(np.correlate(AR_i8, AR_b), _Array1D[np.signedinteger])
assert_type(np.correlate(AR_i8, AR_f8), _Array1D[np.floating])
assert_type(np.correlate(AR_i8, AR_c16), _Array1D[np.complexfloating])
assert_type(np.correlate(AR_i8, AR_m), _Array1D[np.timedelta64])
assert_type(np.correlate(AR_O, AR_O), _Array1D[np.object_])

assert_type(np.convolve(ints, AR_i8, mode="valid"), _Array1D[np.signedinteger])
assert_type(np.convolve(AR_i8, AR_i8, mode="same"), _Array1D[np.signedinteger])
assert_type(np.convolve(AR_b, AR_b), _Array1D[np.bool])
assert_type(np.convolve(AR_b, AR_u8), _Array1D[np.unsignedinteger])
assert_type(np.convolve(AR_i8, AR_b), _Array1D[np.signedinteger])
assert_type(np.convolve(AR_i8, AR_f8), _Array1D[np.floating])
assert_type(np.convolve(AR_i8, AR_c16), _Array1D[np.complexfloating])
assert_type(np.convolve(AR_i8, AR_m), _Array1D[np.timedelta64])
assert_type(np.convolve(AR_O, AR_O), _Array1D[np.object_])

assert_type(np.outer(i8, AR_i8), _Array2D[np.signedinteger])
assert_type(np.outer(ints, AR_i8), _Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_i8), _Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_i8, out=AR_i8_sub), SubArray)
assert_type(np.outer(AR_b, AR_b), _Array2D[np.bool])
assert_type(np.outer(AR_b, AR_u8), _Array2D[np.unsignedinteger])
assert_type(np.outer(AR_i8, AR_b), _Array2D[np.signedinteger])
assert_type(np.outer(AR_i8, AR_f8), _Array2D[np.floating])
assert_type(np.outer(AR_i8, AR_c16), _Array2D[np.complexfloating])
assert_type(np.outer(AR_i8, AR_m), _Array2D[np.timedelta64])
assert_type(np.outer(AR_O, AR_O), _Array2D[np.object_])

assert_type(np.tensordot(ints, AR_i8), npt.NDArray[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8), npt.NDArray[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8, axes=0), npt.NDArray[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_i8, axes=(0, 1)), npt.NDArray[np.signedinteger])
assert_type(np.tensordot(AR_b, AR_b), npt.NDArray[np.bool])
assert_type(np.tensordot(AR_b, AR_u8), npt.NDArray[np.unsignedinteger])
assert_type(np.tensordot(AR_i8, AR_b), npt.NDArray[np.signedinteger])
assert_type(np.tensordot(AR_i8, AR_f8), npt.NDArray[np.floating])
assert_type(np.tensordot(AR_i8, AR_c16), npt.NDArray[np.complexfloating])
assert_type(np.tensordot(AR_i8, AR_m), npt.NDArray[np.timedelta64])
assert_type(np.tensordot(AR_O, AR_O), npt.NDArray[np.object_])

assert_type(np.isscalar(i8), bool)
assert_type(np.isscalar(AR_i8), bool)
assert_type(np.isscalar(ints), bool)

assert_type(np.roll(AR_i8, 1), npt.NDArray[np.int64])
assert_type(np.roll(AR_i8, (1, 2)), npt.NDArray[np.int64])
assert_type(np.roll(ints, 1), npt.NDArray[Any])

assert_type(np.rollaxis(AR_i8, 0, 1), npt.NDArray[np.int64])

assert_type(np.moveaxis(AR_i8, 0, 1), npt.NDArray[np.int64])
assert_type(np.moveaxis(AR_i8, (0, 1), (1, 2)), npt.NDArray[np.int64])

assert_type(np.cross(ints, AR_i8), npt.NDArray[np.signedinteger])
assert_type(np.cross(AR_i8, AR_i8), npt.NDArray[np.signedinteger])
assert_type(np.cross(AR_b, AR_u8), npt.NDArray[np.unsignedinteger])
assert_type(np.cross(AR_i8, AR_b), npt.NDArray[np.signedinteger])
assert_type(np.cross(AR_i8, AR_f8), npt.NDArray[np.floating])
assert_type(np.cross(AR_i8, AR_c16), npt.NDArray[np.complexfloating])

assert_type(np.indices([0, 1, 2]), npt.NDArray[np.int_])
assert_type(np.indices([0, 1, 2], sparse=True), tuple[npt.NDArray[np.int_], ...])
assert_type(np.indices([0, 1, 2], dtype=np.float64), npt.NDArray[np.float64])
assert_type(np.indices([0, 1, 2], sparse=True, dtype=np.float64), tuple[npt.NDArray[np.float64], ...])
assert_type(np.indices([0, 1, 2], dtype=float), npt.NDArray[Any])
assert_type(np.indices([0, 1, 2], sparse=True, dtype=float), tuple[npt.NDArray[Any], ...])

assert_type(np.binary_repr(1), str)

assert_type(np.base_repr(1), str)

assert_type(np.allclose(i8, AR_i8), bool)
assert_type(np.allclose(ints, AR_i8), bool)
assert_type(np.allclose(AR_i8, AR_i8), bool)

assert_type(np.isclose(i8, i8), np.bool)
assert_type(np.isclose(i8, AR_i8), npt.NDArray[np.bool])
assert_type(np.isclose(ints, AR_i8), npt.NDArray[np.bool])
assert_type(np.isclose(AR_i8, AR_i8), npt.NDArray[np.bool])

assert_type(np.array_equal(i8, AR_i8), bool)
assert_type(np.array_equal(ints, AR_i8), bool)
assert_type(np.array_equal(AR_i8, AR_i8), bool)

assert_type(np.array_equiv(i8, AR_i8), bool)
assert_type(np.array_equiv(ints, AR_i8), bool)
assert_type(np.array_equiv(AR_i8, AR_i8), bool)
