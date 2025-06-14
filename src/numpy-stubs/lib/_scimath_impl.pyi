from typing import TypeAlias, overload

import _numtype as _nt
import numpy as np

__all__ = ["arccos", "arcsin", "arctanh", "log", "log2", "log10", "logn", "power", "sqrt"]

###

_ToScalar_iu4_iu8: TypeAlias = _nt.integer32 | _nt.integer64 | _nt.JustInt
_ToScalar_i4_i8: TypeAlias = np.int32 | np.int64 | _nt.JustInt
_ToScalar_u4_u8: TypeAlias = np.uint32 | np.uint64

_ToArray_iu1: TypeAlias = _nt._ToArray_1nd[_nt.integer8]
_ToArray_iu2: TypeAlias = _nt._ToArray_1nd[_nt.integer16]
_ToArray_iu4_iu8: TypeAlias = _nt._ToArray2_1nd[_nt.integer32 | _nt.integer64, _nt.JustInt]
_ToArray_i4_i8: TypeAlias = _nt._ToArray2_1nd[np.int32 | np.int64, _nt.JustInt]
_ToArray_u4_u8: TypeAlias = _nt._ToArray_1nd[np.uint32 | np.uint64]

###

# NOTE: This module is publically re-exported as `numpy.emath`
# NOTE: All signatures are weird: https://github.com/numpy/numpy/issues/28367
# NOTE: The signatures of sqrt, log, log2, and log10 are identical
# NOTE: all ignored mypy [overload-overlap] errors are false positives (meet vs join)

#
@overload
def sqrt(x: bool | np.bool_) -> np.float16: ...
@overload
def sqrt(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def sqrt(x: np.uint16) -> np.float32: ...
@overload
def sqrt(x: np.uint8) -> np.float16: ...
@overload
def sqrt(x: _nt.co_uint64) -> np.floating: ...
@overload
def sqrt(x: _ToScalar_i4_i8) -> _nt.inexact64: ...
@overload
def sqrt(x: np.int16) -> _nt.inexact32: ...
@overload
def sqrt(x: np.int8) -> np.float16 | np.complex64: ...
@overload
def sqrt(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def sqrt(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def sqrt(x: np.float32) -> _nt.inexact32: ...
@overload
def sqrt(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def sqrt(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def sqrt(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def sqrt(x: np.complex64) -> np.complex64: ...
@overload
def sqrt(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def sqrt(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def sqrt(x: _nt.ToBool_1nd) -> _nt.Array[np.float16]: ...
@overload
def sqrt(x: _ToArray_u4_u8) -> _nt.Array[np.float64]: ...
@overload
def sqrt(x: _nt.ToUInt16_1nd) -> _nt.Array[np.float32]: ...
@overload
def sqrt(x: _nt.ToUInt8_1nd) -> _nt.Array[np.float16]: ...
@overload
def sqrt(x: _nt.CoUInt64_1nd) -> _nt.Array[np.floating]: ...
@overload
def sqrt(x: _ToArray_i4_i8) -> _nt.Array[_nt.inexact64]: ...
@overload
def sqrt(x: _nt.ToInt16_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def sqrt(x: _nt.ToInt8_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def sqrt(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def sqrt(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def sqrt(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def sqrt(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def sqrt(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def sqrt(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def sqrt(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def sqrt(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def sqrt(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log(x: bool | np.bool_) -> np.float16: ...
@overload
def log(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log(x: np.uint16) -> np.float32: ...
@overload
def log(x: np.uint8) -> np.float16: ...
@overload
def log(x: _nt.co_uint64) -> np.floating: ...
@overload
def log(x: _ToScalar_i4_i8) -> _nt.inexact64: ...
@overload
def log(x: np.int16) -> _nt.inexact32: ...
@overload
def log(x: np.int8) -> np.float16 | np.complex64: ...
@overload
def log(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def log(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def log(x: np.float32) -> _nt.inexact32: ...
@overload
def log(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def log(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def log(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def log(x: np.complex64) -> np.complex64: ...
@overload
def log(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def log(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def log(x: _nt.ToBool_1nd) -> _nt.Array[np.float16]: ...
@overload
def log(x: _ToArray_u4_u8) -> _nt.Array[np.float64]: ...
@overload
def log(x: _nt.ToUInt16_1nd) -> _nt.Array[np.float32]: ...
@overload
def log(x: _nt.ToUInt8_1nd) -> _nt.Array[np.float16]: ...
@overload
def log(x: _nt.CoUInt64_1nd) -> _nt.Array[np.floating]: ...
@overload
def log(x: _ToArray_i4_i8) -> _nt.Array[_nt.inexact64]: ...
@overload
def log(x: _nt.ToInt16_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log(x: _nt.ToInt8_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def log(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def log(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def log(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def log(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def log(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def log(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def log(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def log(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log10(x: bool | np.bool_) -> np.float16: ...
@overload
def log10(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log10(x: np.uint16) -> np.float32: ...
@overload
def log10(x: np.uint8) -> np.float16: ...
@overload
def log10(x: _nt.co_uint64) -> np.floating: ...
@overload
def log10(x: _ToScalar_i4_i8) -> _nt.inexact64: ...
@overload
def log10(x: np.int16) -> _nt.inexact32: ...
@overload
def log10(x: np.int8) -> np.float16 | np.complex64: ...
@overload
def log10(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def log10(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def log10(x: np.float32) -> _nt.inexact32: ...
@overload
def log10(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def log10(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def log10(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def log10(x: np.complex64) -> np.complex64: ...
@overload
def log10(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def log10(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def log10(x: _nt.ToBool_1nd) -> _nt.Array[np.float16]: ...
@overload
def log10(x: _ToArray_u4_u8) -> _nt.Array[np.float64]: ...
@overload
def log10(x: _nt.ToUInt16_1nd) -> _nt.Array[np.float32]: ...
@overload
def log10(x: _nt.ToUInt8_1nd) -> _nt.Array[np.float16]: ...
@overload
def log10(x: _nt.CoUInt64_1nd) -> _nt.Array[np.floating]: ...
@overload
def log10(x: _ToArray_i4_i8) -> _nt.Array[_nt.inexact64]: ...
@overload
def log10(x: _nt.ToInt16_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log10(x: _nt.ToInt8_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def log10(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def log10(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def log10(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log10(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def log10(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def log10(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def log10(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def log10(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def log10(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# signature is equivalent to `sqrt`
@overload
def log2(x: bool | np.bool_) -> np.float16: ...
@overload
def log2(x: _ToScalar_u4_u8) -> np.float64: ...
@overload
def log2(x: np.uint16) -> np.float32: ...
@overload
def log2(x: np.uint8) -> np.float16: ...
@overload
def log2(x: _nt.co_uint64) -> np.floating: ...
@overload
def log2(x: _ToScalar_i4_i8) -> _nt.inexact64: ...
@overload
def log2(x: np.int16) -> _nt.inexact32: ...
@overload
def log2(x: np.int8) -> np.float16 | np.complex64: ...
@overload
def log2(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def log2(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def log2(x: np.float32) -> _nt.inexact32: ...
@overload
def log2(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def log2(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def log2(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def log2(x: np.complex64) -> np.complex64: ...
@overload
def log2(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def log2(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def log2(x: _nt.ToBool_1nd) -> _nt.Array[np.float16]: ...
@overload
def log2(x: _ToArray_u4_u8) -> _nt.Array[np.float64]: ...
@overload
def log2(x: _nt.ToUInt16_1nd) -> _nt.Array[np.float32]: ...
@overload
def log2(x: _nt.ToUInt8_1nd) -> _nt.Array[np.float16]: ...
@overload
def log2(x: _nt.CoUInt64_1nd) -> _nt.Array[np.floating]: ...
@overload
def log2(x: _ToArray_i4_i8) -> _nt.Array[_nt.inexact64]: ...
@overload
def log2(x: _nt.ToInt16_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log2(x: _nt.ToInt8_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def log2(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def log2(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def log2(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def log2(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def log2(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def log2(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def log2(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def log2(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def log2(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# NOTE: The signatures of arccos, arcsin, and arctanh are identical

#
@overload
def arccos(x: bool | np.bool_) -> np.float16 | np.complex64: ...
@overload
def arccos(x: _ToScalar_iu4_iu8) -> _nt.inexact64: ...
@overload
def arccos(x: _nt.integer16) -> _nt.inexact32: ...
@overload
def arccos(x: _nt.integer8) -> np.float16 | np.complex64: ...
@overload
def arccos(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def arccos(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def arccos(x: np.float32) -> _nt.inexact32: ...
@overload
def arccos(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def arccos(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def arccos(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def arccos(x: np.complex64) -> np.complex64: ...
@overload
def arccos(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def arccos(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def arccos(x: _nt.ToBool_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arccos(x: _ToArray_iu4_iu8) -> _nt.Array[_nt.inexact64]: ...
@overload
def arccos(x: _ToArray_iu2) -> _nt.Array[_nt.inexact32]: ...
@overload
def arccos(x: _ToArray_iu1) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arccos(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def arccos(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def arccos(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def arccos(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def arccos(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def arccos(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def arccos(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def arccos(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def arccos(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# signature is equivalent to `arccos`
@overload
def arcsin(x: bool | np.bool_) -> np.float16 | np.complex64: ...
@overload
def arcsin(x: _ToScalar_iu4_iu8) -> _nt.inexact64: ...
@overload
def arcsin(x: _nt.integer16) -> _nt.inexact32: ...
@overload
def arcsin(x: _nt.integer8) -> np.float16 | np.complex64: ...
@overload
def arcsin(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def arcsin(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def arcsin(x: np.float32) -> _nt.inexact32: ...
@overload
def arcsin(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def arcsin(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def arcsin(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def arcsin(x: np.complex64) -> np.complex64: ...
@overload
def arcsin(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def arcsin(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def arcsin(x: _nt.ToBool_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arcsin(x: _ToArray_iu4_iu8) -> _nt.Array[_nt.inexact64]: ...
@overload
def arcsin(x: _ToArray_iu2) -> _nt.Array[_nt.inexact32]: ...
@overload
def arcsin(x: _ToArray_iu1) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arcsin(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def arcsin(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def arcsin(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def arcsin(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def arcsin(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def arcsin(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def arcsin(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def arcsin(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def arcsin(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

# signature is equivalent to `arccos`
@overload
def arctanh(x: bool | np.bool_) -> np.float16 | np.complex64: ...
@overload
def arctanh(x: _ToScalar_iu4_iu8) -> _nt.inexact64: ...
@overload
def arctanh(x: _nt.integer16) -> _nt.inexact32: ...
@overload
def arctanh(x: _nt.integer8) -> np.float16 | np.complex64: ...
@overload
def arctanh(x: _nt.JustFloat | np.float64) -> _nt.inexact64: ...
@overload
def arctanh(x: np.longdouble) -> np.longdouble | np.complex128: ...
@overload
def arctanh(x: np.float32) -> _nt.inexact32: ...
@overload
def arctanh(x: np.float16) -> np.float16 | np.complex128: ...
@overload
def arctanh(x: _nt.JustComplex | np.complex128) -> np.complex128: ...
@overload
def arctanh(x: np.clongdouble) -> np.complex128 | np.clongdouble: ...
@overload
def arctanh(x: np.complex64) -> np.complex64: ...
@overload
def arctanh(x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def arctanh(x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def arctanh(x: _nt.ToBool_1nd) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arctanh(x: _ToArray_iu4_iu8) -> _nt.Array[_nt.inexact64]: ...
@overload
def arctanh(x: _ToArray_iu2) -> _nt.Array[_nt.inexact32]: ...
@overload
def arctanh(x: _ToArray_iu1) -> _nt.Array[np.float16 | np.complex64]: ...
@overload
def arctanh(x: _nt.ToFloat64_1nd) -> _nt.Array[_nt.inexact64]: ...
@overload
def arctanh(x: _nt.ToLongDouble_1nd) -> _nt.Array[np.longdouble | np.complex128]: ...
@overload
def arctanh(x: _nt.ToFloat32_1nd) -> _nt.Array[_nt.inexact32]: ...
@overload
def arctanh(x: _nt.ToFloat16_1nd) -> _nt.Array[np.float16 | np.complex128]: ...
@overload
def arctanh(x: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def arctanh(x: _nt.ToCLongDouble_1nd) -> _nt.Array[np.complex128 | np.clongdouble]: ...
@overload
def arctanh(x: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def arctanh(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def arctanh(x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...

#
@overload
def logn(n: _nt.co_uint8, x: _nt.co_uint8) -> np.float16: ...
@overload
def logn(n: np.uint64, x: _nt.co_uint64) -> np.floating: ...
@overload
def logn(n: _nt.JustComplex | np.complexfloating, x: complex | _nt.co_complex) -> np.complexfloating: ...
@overload
def logn(n: complex | _nt.co_complex, x: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def logn(n: complex | _nt.co_complex, x: complex | _nt.co_complex) -> np.inexact: ...
@overload
def logn(n: _nt.CoUInt8_nd, x: _nt.CoUInt8_1nd) -> _nt.Array[np.float16]: ...
@overload
def logn(n: _nt.CoUInt8_1nd, x: _nt.CoUInt8_nd) -> _nt.Array[np.float16]: ...
@overload
def logn(n: _nt.CoUInt64_nd, x: _nt.CoUInt64_1nd) -> _nt.Array[np.floating]: ...
@overload
def logn(n: _nt.CoUInt64_1nd, x: _nt.CoUInt64_nd) -> _nt.Array[np.floating]: ...
@overload
def logn(n: _nt.ToComplex_nd, x: _nt.CoComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def logn(n: _nt.ToComplex_1nd, x: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def logn(n: _nt.CoComplex_nd, x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def logn(n: _nt.CoComplex_1nd, x: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def logn(n: _nt.CoComplex_nd, x: _nt.CoComplex_1nd) -> _nt.Array[np.inexact]: ...
@overload
def logn(n: _nt.CoComplex_1nd, x: _nt.CoComplex_nd) -> _nt.Array[np.inexact]: ...

#
@overload
def power(x: _nt.co_int8, p: _nt.co_int8) -> np.int8: ...
@overload
def power(x: np.unsignedinteger, p: np.uint64) -> np.unsignedinteger: ...
@overload
def power(x: np.uint64, p: np.unsignedinteger) -> np.unsignedinteger: ...
@overload
def power(x: np.uint64, p: _nt.JustInt | np.signedinteger) -> np.signedinteger | np.float64: ...
@overload
def power(x: np.uint64, p: _nt.JustFloat | np.floating) -> np.floating: ...
@overload
def power(x: _nt.JustInt | np.signedinteger, p: np.uint64) -> np.signedinteger | np.complexfloating: ...
@overload
def power(x: _nt.JustInt | np.signedinteger, p: int | _nt.co_integer) -> np.signedinteger | np.inexact: ...
@overload
def power(x: _nt.JustFloat | np.floating, p: float | _nt.co_float) -> np.inexact: ...
@overload
def power(x: float | _nt.co_float, p: _nt.JustFloat | np.floating) -> np.inexact: ...
@overload
def power(x: _nt.JustComplex | np.complexfloating, p: complex | _nt.co_complex) -> np.complexfloating: ...
@overload
def power(x: complex | _nt.co_complex, p: _nt.JustComplex | np.complexfloating) -> np.complexfloating: ...
@overload
def power(x: _nt.CoInt8_nd, p: _nt.CoInt8_1nd) -> _nt.Array[np.int8]: ...
@overload
def power(x: _nt.CoInt8_1nd, p: _nt.CoInt8_nd) -> _nt.Array[np.int8]: ...
@overload
def power(x: _nt.ToUInteger_1nd, p: _nt.CoUInt64_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def power(x: _nt.CoUInt64_1nd, p: _nt.ToUInteger_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def power(x: _nt.CoUInt64_1nd, p: _nt.ToSInteger_nd) -> _nt.Array[np.signedinteger | np.float64]: ...
@overload
def power(x: _nt.CoUInt64_nd, p: _nt.ToSInteger_1nd) -> _nt.Array[np.signedinteger | np.float64]: ...
@overload
def power(x: _nt.CoUInt64_1nd, p: _nt.ToFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def power(x: _nt.CoUInt64_nd, p: _nt.ToFloating_1nd) -> _nt.Array[np.floating]: ...
@overload
def power(x: _nt.ToUInteger_nd, p: _nt.CoUInt64_1nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def power(x: _nt.CoUInt64_nd, p: _nt.ToUInteger_1nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def power(x: _nt.ToSInteger_1nd, p: _nt.CoUInt64_nd) -> _nt.Array[np.signedinteger | np.complexfloating]: ...
@overload
def power(x: _nt.ToSInteger_nd, p: _nt.CoUInt64_1nd) -> _nt.Array[np.signedinteger | np.complexfloating]: ...
@overload
def power(x: _nt.ToSInteger_1nd, p: _nt.CoInteger_nd) -> _nt.Array[np.signedinteger | np.inexact]: ...
@overload
def power(x: _nt.ToSInteger_nd, p: _nt.CoInteger_1nd) -> _nt.Array[np.signedinteger | np.inexact]: ...
@overload
def power(x: _nt.ToFloating_1nd, p: _nt.CoFloating_nd) -> _nt.Array[np.inexact]: ...
@overload
def power(x: _nt.ToFloating_nd, p: _nt.CoFloating_1nd) -> _nt.Array[np.inexact]: ...
@overload
def power(x: _nt.CoFloating_1nd, p: _nt.ToFloating_nd) -> _nt.Array[np.inexact]: ...
@overload
def power(x: _nt.CoFloating_nd, p: _nt.ToFloating_1nd) -> _nt.Array[np.inexact]: ...
@overload
def power(x: _nt.CoComplex_nd, p: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def power(x: _nt.CoComplex_1nd, p: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def power(x: _nt.ToComplex_nd, p: _nt.CoComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def power(x: _nt.ToComplex_1nd, p: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
