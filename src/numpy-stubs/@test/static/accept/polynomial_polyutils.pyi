from collections.abc import Sequence
from decimal import Decimal
from fractions import Fraction
from typing import Any, TypeAlias, assert_type
from typing_extensions import TypeVar

import numpy as np
import numpy.polynomial.polyutils as pu
import numpy.typing as npt

###

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]

_Floating1D: TypeAlias = _Array1D[np.floating]
_Complex1D: TypeAlias = _Array1D[np.complexfloating]
_Object1D: TypeAlias = _Array1D[np.object_]

_Tuple2: TypeAlias = tuple[_T, _T]

###

num_int: int
num_float: float
num_complex: complex
# will result in an `object_` dtype
num_object: Decimal | Fraction

sct_int: np.int_
sct_float: np.float64
sct_complex: np.complex128
sct_object: np.object_  # doesn't exist at runtime

arr_int: npt.NDArray[np.int_]
arr_float: npt.NDArray[np.float64]
arr_complex: npt.NDArray[np.complex128]
arr_object: npt.NDArray[np.object_]

seq_num_int: Sequence[int]
seq_num_float: Sequence[float]
seq_num_complex: Sequence[complex]
seq_num_object: Sequence[Decimal | Fraction]

seq_sct_int: Sequence[np.int_]
seq_sct_float: Sequence[np.float64]
seq_sct_complex: Sequence[np.complex128]
seq_sct_object: Sequence[np.object_]

seq_arr_int: Sequence[npt.NDArray[np.int_]]
seq_arr_float: Sequence[npt.NDArray[np.float64]]
seq_arr_complex: Sequence[npt.NDArray[np.complex128]]
seq_arr_object: Sequence[npt.NDArray[np.object_]]

seq_seq_num_int: Sequence[Sequence[int]]
seq_seq_num_float: Sequence[Sequence[float]]
seq_seq_num_complex: Sequence[Sequence[complex]]
seq_seq_num_object: Sequence[Sequence[Decimal | Fraction]]

seq_seq_sct_int: Sequence[Sequence[np.int_]]
seq_seq_sct_float: Sequence[Sequence[np.float64]]
seq_seq_sct_complex: Sequence[Sequence[np.complex128]]
seq_seq_sct_object: Sequence[Sequence[np.object_]]  # doesn't exist at runtime

# as_series

assert_type(pu.as_series(arr_int), list[_Floating1D])
assert_type(pu.as_series(arr_float), list[_Floating1D])
assert_type(pu.as_series(arr_complex), list[_Complex1D])
assert_type(pu.as_series(arr_object), list[_Object1D])

assert_type(pu.as_series(seq_num_int), list[_Floating1D])
assert_type(pu.as_series(seq_num_float), list[_Floating1D])
assert_type(pu.as_series(seq_num_complex), list[_Complex1D])
assert_type(pu.as_series(seq_num_object), list[_Object1D])

assert_type(pu.as_series(seq_sct_int), list[_Floating1D])
assert_type(pu.as_series(seq_sct_float), list[_Floating1D])
assert_type(pu.as_series(seq_sct_complex), list[_Complex1D])
assert_type(pu.as_series(seq_sct_object), list[_Object1D])

assert_type(pu.as_series(seq_arr_int), list[_Floating1D])
assert_type(pu.as_series(seq_arr_float), list[_Floating1D])
assert_type(pu.as_series(seq_arr_complex), list[_Complex1D])
assert_type(pu.as_series(seq_arr_object), list[_Object1D])

assert_type(pu.as_series(seq_seq_num_int), list[_Floating1D])
assert_type(pu.as_series(seq_seq_num_float), list[_Floating1D])
assert_type(pu.as_series(seq_seq_num_complex), list[_Complex1D])
assert_type(pu.as_series(seq_seq_num_object), list[_Object1D])

assert_type(pu.as_series(seq_seq_sct_int), list[_Floating1D])
assert_type(pu.as_series(seq_seq_sct_float), list[_Floating1D])
assert_type(pu.as_series(seq_seq_sct_complex), list[_Complex1D])
assert_type(pu.as_series(seq_seq_sct_object), list[_Object1D])

# trimcoef

assert_type(pu.trimcoef(num_int), _Floating1D)
assert_type(pu.trimcoef(num_float), _Floating1D)
assert_type(pu.trimcoef(num_complex), _Complex1D)
assert_type(pu.trimcoef(num_object), _Object1D)
assert_type(pu.trimcoef(num_object), _Object1D)

assert_type(pu.trimcoef(sct_int), _Floating1D)
assert_type(pu.trimcoef(sct_float), _Floating1D)
assert_type(pu.trimcoef(sct_complex), _Complex1D)
assert_type(pu.trimcoef(sct_object), _Object1D)

assert_type(pu.trimcoef(arr_int), _Floating1D)
assert_type(pu.trimcoef(arr_float), _Floating1D)
assert_type(pu.trimcoef(arr_complex), _Complex1D)
assert_type(pu.trimcoef(arr_object), _Object1D)

assert_type(pu.trimcoef(seq_num_int), _Floating1D)
assert_type(pu.trimcoef(seq_num_float), _Floating1D)
assert_type(pu.trimcoef(seq_num_complex), _Complex1D)
assert_type(pu.trimcoef(seq_num_object), _Object1D)

assert_type(pu.trimcoef(seq_sct_int), _Floating1D)
assert_type(pu.trimcoef(seq_sct_float), _Floating1D)
assert_type(pu.trimcoef(seq_sct_complex), _Complex1D)
assert_type(pu.trimcoef(seq_sct_object), _Object1D)

# getdomain

assert_type(pu.getdomain(num_int), _Array1D[np.float64])
assert_type(pu.getdomain(num_float), _Array1D[np.float64])
assert_type(pu.getdomain(num_complex), _Array1D[np.complex128])
assert_type(pu.getdomain(num_object), _Object1D)
assert_type(pu.getdomain(num_object), _Object1D)

assert_type(pu.getdomain(sct_int), _Array1D[np.float64])
assert_type(pu.getdomain(sct_float), _Array1D[np.float64])
assert_type(pu.getdomain(sct_complex), _Array1D[np.complex128])
assert_type(pu.getdomain(sct_object), _Object1D)

assert_type(pu.getdomain(arr_int), _Array1D[np.float64])
assert_type(pu.getdomain(arr_float), _Array1D[np.float64])
assert_type(pu.getdomain(arr_complex), _Array1D[np.complex128])
assert_type(pu.getdomain(arr_object), _Object1D)

assert_type(pu.getdomain(seq_num_int), _Array1D[np.float64])
assert_type(pu.getdomain(seq_num_float), _Array1D[np.float64])
assert_type(pu.getdomain(seq_num_complex), _Array1D[np.complex128])
assert_type(pu.getdomain(seq_num_object), _Object1D)

assert_type(pu.getdomain(seq_sct_int), _Array1D[np.float64])
assert_type(pu.getdomain(seq_sct_float), _Array1D[np.float64])
assert_type(pu.getdomain(seq_sct_complex), _Array1D[np.complex128])
assert_type(pu.getdomain(seq_sct_object), _Object1D)

# mapparms

assert_type(pu.mapparms(seq_num_int, seq_num_int), _Tuple2[float])
assert_type(pu.mapparms(seq_num_int, seq_num_float), _Tuple2[float])
assert_type(pu.mapparms(seq_num_float, seq_num_float), _Tuple2[float])
assert_type(pu.mapparms(seq_num_float, seq_num_complex), _Tuple2[complex])
assert_type(pu.mapparms(seq_num_complex, seq_num_complex), _Tuple2[complex])
assert_type(pu.mapparms(seq_num_complex, seq_num_object), _Tuple2[Any])
assert_type(pu.mapparms(seq_num_object, seq_num_object), _Tuple2[Any])

assert_type(pu.mapparms(seq_sct_int, seq_sct_int), _Tuple2[np.floating])
assert_type(pu.mapparms(seq_sct_int, seq_sct_float), _Tuple2[np.floating])
assert_type(pu.mapparms(seq_sct_float, seq_sct_float), _Tuple2[float])
assert_type(pu.mapparms(seq_sct_float, seq_sct_complex), _Tuple2[complex])
assert_type(pu.mapparms(seq_sct_complex, seq_sct_complex), _Tuple2[complex])
assert_type(pu.mapparms(seq_sct_complex, seq_sct_object), _Tuple2[Any])
assert_type(pu.mapparms(seq_sct_object, seq_sct_object), _Tuple2[Any])

assert_type(pu.mapparms(arr_int, arr_int), _Tuple2[np.floating])
assert_type(pu.mapparms(arr_int, arr_float), _Tuple2[np.floating])
assert_type(pu.mapparms(arr_float, arr_float), _Tuple2[np.floating])
assert_type(pu.mapparms(arr_float, arr_complex), _Tuple2[np.complexfloating])
assert_type(pu.mapparms(arr_complex, arr_complex), _Tuple2[np.complexfloating])
assert_type(pu.mapparms(arr_complex, arr_object), _Tuple2[Any])
assert_type(pu.mapparms(arr_object, arr_object), _Tuple2[Any])

# mapdomain

assert_type(pu.mapdomain(num_int, seq_num_int, seq_num_int), np.floating)
assert_type(pu.mapdomain(num_int, seq_num_int, seq_num_float), np.floating)
assert_type(pu.mapdomain(num_int, seq_num_float, seq_num_float), np.floating)
assert_type(pu.mapdomain(num_float, seq_num_float, seq_num_float), np.floating)
assert_type(pu.mapdomain(num_float, seq_num_float, seq_num_complex), np.complexfloating)
assert_type(pu.mapdomain(num_float, seq_num_complex, seq_num_complex), np.complexfloating)
assert_type(pu.mapdomain(num_complex, seq_num_complex, seq_num_complex), np.complexfloating)
assert_type(pu.mapdomain(num_complex, seq_num_complex, seq_num_object), Any)
assert_type(pu.mapdomain(num_complex, seq_num_object, seq_num_object), Any)
assert_type(pu.mapdomain(num_object, seq_num_object, seq_num_object), Any)

assert_type(pu.mapdomain(seq_num_int, seq_num_int, seq_num_int), _Floating1D)
assert_type(pu.mapdomain(seq_num_int, seq_num_int, seq_num_float), _Floating1D)
assert_type(pu.mapdomain(seq_num_int, seq_num_float, seq_num_float), _Floating1D)
assert_type(pu.mapdomain(seq_num_float, seq_num_float, seq_num_float), _Floating1D)
assert_type(pu.mapdomain(seq_num_float, seq_num_float, seq_num_complex), _Complex1D)
assert_type(pu.mapdomain(seq_num_float, seq_num_complex, seq_num_complex), _Complex1D)
assert_type(pu.mapdomain(seq_num_complex, seq_num_complex, seq_num_complex), _Complex1D)
assert_type(pu.mapdomain(seq_num_complex, seq_num_complex, seq_num_object), _Object1D)
assert_type(pu.mapdomain(seq_num_complex, seq_num_object, seq_num_object), _Object1D)
assert_type(pu.mapdomain(seq_num_object, seq_num_object, seq_num_object), _Object1D)

assert_type(pu.mapdomain(seq_sct_int, seq_sct_int, seq_sct_int), _Floating1D)
assert_type(pu.mapdomain(seq_sct_int, seq_sct_int, seq_sct_float), _Floating1D)
assert_type(pu.mapdomain(seq_sct_int, seq_sct_float, seq_sct_float), _Floating1D)
assert_type(pu.mapdomain(seq_sct_float, seq_sct_float, seq_sct_float), _Floating1D)
assert_type(pu.mapdomain(seq_sct_float, seq_sct_float, seq_sct_complex), _Complex1D)
assert_type(pu.mapdomain(seq_sct_float, seq_sct_complex, seq_sct_complex), _Complex1D)
assert_type(pu.mapdomain(seq_sct_complex, seq_sct_complex, seq_sct_complex), _Complex1D)
assert_type(pu.mapdomain(seq_sct_complex, seq_sct_complex, seq_sct_object), _Object1D)
assert_type(pu.mapdomain(seq_sct_complex, seq_sct_object, seq_sct_object), _Object1D)
assert_type(pu.mapdomain(seq_sct_object, seq_sct_object, seq_sct_object), _Object1D)

assert_type(pu.mapdomain(arr_int, arr_int, arr_int), _Floating1D)
assert_type(pu.mapdomain(arr_int, arr_int, arr_float), _Floating1D)
assert_type(pu.mapdomain(arr_int, arr_float, arr_float), _Floating1D)
assert_type(pu.mapdomain(arr_float, arr_float, arr_float), _Floating1D)
assert_type(pu.mapdomain(arr_float, arr_float, arr_complex), _Complex1D)
assert_type(pu.mapdomain(arr_float, arr_complex, arr_complex), _Complex1D)
assert_type(pu.mapdomain(arr_complex, arr_complex, arr_complex), _Complex1D)
assert_type(pu.mapdomain(arr_complex, arr_complex, arr_object), _Object1D)
assert_type(pu.mapdomain(arr_complex, arr_object, arr_object), _Object1D)
assert_type(pu.mapdomain(arr_object, arr_object, arr_object), _Object1D)
