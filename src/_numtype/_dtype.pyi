import ctypes as ct
from typing import Any, TypeAlias, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar

import numpy as np
from numpy._typing._char_codes import (
    _BoolCodes,
    _BytesCodes,
    _CLongDoubleCodes,
    _Complex64Codes,
    _Complex128Codes,
    _DT64Codes,
    _Float16Codes,
    _Float32Codes,
    _Float64Codes,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntPCodes,
    _LongCodes,
    _LongDoubleCodes,
    _ObjectCodes,
    _StrCodes,
    _StringCodes,
    _TD64Codes,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntPCodes,
    _ULongCodes,
    _VoidCodes,
)
from numpy._typing._dtype_like import _VoidDTypeLike

from ._just import JustBytes, JustComplex, JustFloat, JustInt, JustObject, JustStr

__all__ = [
    "ToDType",
    "ToDTypeBool",
    "ToDTypeBytes",
    "ToDTypeCLongDouble",
    "ToDTypeComplex64",
    "ToDTypeComplex128",
    "ToDTypeDateTime64",
    "ToDTypeFloat16",
    "ToDTypeFloat32",
    "ToDTypeFloat64",
    "ToDTypeInt8",
    "ToDTypeInt16",
    "ToDTypeInt32",
    "ToDTypeInt64",
    "ToDTypeLong",
    "ToDTypeLongDouble",
    "ToDTypeObject",
    "ToDTypeStr",
    "ToDTypeString",
    "ToDTypeTimeDelta64",
    "ToDTypeUInt8",
    "ToDTypeUInt16",
    "ToDTypeUInt32",
    "ToDTypeUInt64",
    "ToDTypeULong",
    "ToDTypeVoid",
    "_ToDType",
    "_ToDType2",
]

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True, default=Any)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True, default=np.dtype)

@type_check_only
class _HasDType(Protocol[_DTypeT_co]):
    @property
    def dtype(self) -> _DTypeT_co: ...

@type_check_only
class _HasDTypeOf(Protocol[_ScalarT_co]):
    @property
    def dtype(self) -> np.dtype[_ScalarT_co]: ...

_ToDType = TypeAliasType(
    "_ToDType", type[_ScalarT] | np.dtype[_ScalarT] | _HasDTypeOf[_ScalarT], type_params=(_ScalarT,)
)
_ToDType2 = TypeAliasType(
    "_ToDType2", type[_ScalarT | _T] | np.dtype[_ScalarT] | _HasDTypeOf[_ScalarT], type_params=(_ScalarT, _T)
)

_C_i16: TypeAlias = ct.c_int16 | ct.c_short
_C_u16: TypeAlias = ct.c_uint16 | ct.c_ushort
_C_i32: TypeAlias = ct.c_int32 | ct.c_int
_C_u32: TypeAlias = ct.c_uint32 | ct.c_uint
_C_i64: TypeAlias = ct.c_int64 | ct.c_longlong | ct.c_ssize_t
_C_u64: TypeAlias = ct.c_uint64 | ct.c_ulonglong | ct.c_size_t | ct.c_void_p

ToDTypeBool: TypeAlias = _ToDType2[np.bool, ct.c_bool | bool] | _BoolCodes
ToDTypeInt8: TypeAlias = _ToDType2[np.int8, ct.c_int8] | _Int8Codes
ToDTypeUInt8: TypeAlias = _ToDType2[np.uint8, ct.c_uint8] | _UInt8Codes
ToDTypeInt16: TypeAlias = _ToDType2[np.int16, _C_i16] | _Int16Codes
ToDTypeUInt16: TypeAlias = _ToDType2[np.uint16, _C_u16] | _UInt16Codes
ToDTypeInt32: TypeAlias = _ToDType2[np.int32, _C_i32] | _Int32Codes
ToDTypeUInt32: TypeAlias = _ToDType2[np.uint32, _C_u32] | _UInt32Codes
ToDTypeInt64: TypeAlias = _ToDType2[np.int64, _C_i64 | JustInt] | _Int64Codes | _IntPCodes
ToDTypeUInt64: TypeAlias = _ToDType2[np.uint64, _C_u64] | _UInt64Codes | _UIntPCodes
ToDTypeULong: TypeAlias = np.dtypes.ULongDType | type[ct.c_ulong] | _ULongCodes
ToDTypeLong: TypeAlias = np.dtypes.LongDType | type[ct.c_long] | _LongCodes
ToDTypeFloat16: TypeAlias = _ToDType[np.float16] | _Float16Codes
ToDTypeFloat32: TypeAlias = _ToDType2[np.float32, ct.c_float] | _Float32Codes
ToDTypeFloat64: TypeAlias = _ToDType2[np.float64, ct.c_double | JustFloat] | _Float64Codes
ToDTypeLongDouble: TypeAlias = _ToDType2[np.longdouble, ct.c_longdouble] | _LongDoubleCodes
ToDTypeComplex64: TypeAlias = _ToDType[np.complex64] | _Complex64Codes
ToDTypeComplex128: TypeAlias = _ToDType2[np.complex128, JustComplex] | _Complex128Codes
ToDTypeCLongDouble: TypeAlias = _ToDType[np.clongdouble] | _CLongDoubleCodes
ToDTypeObject: TypeAlias = _ToDType2[np.object_, ct.py_object[Any] | JustObject] | _ObjectCodes
ToDTypeBytes: TypeAlias = _ToDType2[np.bytes_, ct.c_char | JustBytes] | _BytesCodes
ToDTypeStr: TypeAlias = _ToDType2[np.str_, JustStr] | _StrCodes
ToDTypeVoid: TypeAlias = _ToDType2[np.void, memoryview] | _VoidDTypeLike | _VoidCodes
ToDTypeDateTime64: TypeAlias = _ToDType[np.datetime64] | _DT64Codes
ToDTypeTimeDelta64: TypeAlias = _ToDType[np.timedelta64] | _TD64Codes
ToDTypeString: TypeAlias = np.dtypes.StringDType | _HasDType[np.dtypes.StringDType] | _StringCodes
ToDType: TypeAlias = str | type | _HasDTypeOf[Any] | _VoidDTypeLike
