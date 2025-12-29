from typing import Any, Literal, assert_type

import _numtype as _nt
import numpy as np

f8: np.float64
f: float

# NOTE: Avoid importing the platform specific `np.float128` type
AR_i8: _nt.Array[np.int64]
AR_i4: _nt.Array[np.int32]
AR_f2: _nt.Array[np.float16]
AR_f8: _nt.Array[np.float64]
AR_f16: _nt.Array[np.longdouble]
AR_c8: _nt.Array[np.complex64]
AR_c16: _nt.Array[np.complex128]

AR_LIKE_i: list[int]

class ComplexObj:
    real: slice
    imag: slice

assert_type(np.mintypecode(["f8"], typeset="qfQF"), str)

assert_type(np.real(ComplexObj()), slice)
assert_type(np.real(AR_f8), _nt.Array[np.float64])
assert_type(np.real(AR_c16), _nt.Array[np.float64])
assert_type(np.real(AR_LIKE_i), _nt.Array[Any])

assert_type(np.imag(ComplexObj()), slice)
assert_type(np.imag(AR_f8), _nt.Array[np.float64])
assert_type(np.imag(AR_c16), _nt.Array[np.float64])
assert_type(np.imag(AR_LIKE_i), _nt.Array[Any])

assert_type(np.iscomplex(f8), np.bool)
assert_type(np.iscomplex(AR_f8), _nt.Array[np.bool])
assert_type(np.iscomplex(AR_LIKE_i), _nt.Array[np.bool])

assert_type(np.isreal(f8), np.bool)
assert_type(np.isreal(AR_f8), _nt.Array[np.bool])
assert_type(np.isreal(AR_LIKE_i), _nt.Array[np.bool])

assert_type(np.iscomplexobj(f8), bool)
assert_type(np.isrealobj(f8), bool)

assert_type(np.nan_to_num(f8), np.float64)
assert_type(np.nan_to_num(f, copy=True), Any)
assert_type(np.nan_to_num(AR_f8, nan=1.5), _nt.Array[np.float64])
assert_type(np.nan_to_num(AR_LIKE_i, posinf=9999), _nt.Array)

assert_type(np.real_if_close(AR_f8), _nt.Array[np.float64])
assert_type(np.real_if_close(AR_c8), _nt.Array[np.float32 | np.complex64])
assert_type(np.real_if_close(AR_c16), _nt.Array[np.float64 | np.complex128])
assert_type(np.real_if_close(AR_LIKE_i), _nt.Array)

assert_type(np.typename("h"), Literal["short"])
assert_type(np.typename("B"), Literal["unsigned char"])
assert_type(np.typename("V"), Literal["void"])
assert_type(np.typename("S1"), Literal["character"])

assert_type(np.common_type(AR_i4), type[np.float64])
assert_type(np.common_type(AR_f2), type[np.float16])
assert_type(np.common_type(AR_f2, AR_i4), type[np.float64])
assert_type(np.common_type(AR_f16, AR_i4), type[np.longdouble])
assert_type(np.common_type(AR_c8, AR_f2), type[np.complex64])
assert_type(np.common_type(AR_f2, AR_c8, AR_i4), type[np.complexfloating])
