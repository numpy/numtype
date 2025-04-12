# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
import decimal
import fractions
from collections.abc import Sequence
from typing import Any, TypeAlias, type_check_only
from typing_extensions import Never, Protocol, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy._typing import _NestedSequence

from ._dtype import (
    ToDType as ToDType,
    ToDTypeBool as ToDTypeBool,
    ToDTypeBytes as ToDTypeBytes,
    ToDTypeCLongDouble as ToDTypeCLongDouble,
    ToDTypeComplex64 as ToDTypeComplex64,
    ToDTypeComplex128 as ToDTypeComplex128,
    ToDTypeDateTime64 as ToDTypeDateTime64,
    ToDTypeFloat16 as ToDTypeFloat16,
    ToDTypeFloat32 as ToDTypeFloat32,
    ToDTypeFloat64 as ToDTypeFloat64,
    ToDTypeInt8 as ToDTypeInt8,
    ToDTypeInt16 as ToDTypeInt16,
    ToDTypeInt32 as ToDTypeInt32,
    ToDTypeInt64 as ToDTypeInt64,
    ToDTypeLongDouble as ToDTypeLongDouble,
    ToDTypeObject as ToDTypeObject,
    ToDTypeStr as ToDTypeStr,
    ToDTypeString as ToDTypeString,
    ToDTypeTimeDelta64 as ToDTypeTimeDelta64,
    ToDTypeUInt8 as ToDTypeUInt8,
    ToDTypeUInt16 as ToDTypeUInt16,
    ToDTypeUInt32 as ToDTypeUInt32,
    ToDTypeUInt64 as ToDTypeUInt64,
    ToDTypeVoid as ToDTypeVoid,
)
from ._just import (
    Just as Just,
    JustBytes as JustBytes,
    JustComplex as JustComplex,
    JustDate as JustDate,
    JustFloat as JustFloat,
    JustInt as JustInt,
    JustObject as JustObject,
    JustStr as JustStr,
)
from ._nep50 import (
    CanCast0D as CanCast0D,
    CanCastND as CanCastND,
    CanNEP50 as CanNEP50,
    CanNEP50Complex as CanNEP50Complex,
    CanNEP50Float as CanNEP50Float,
    MatchND as MatchND,
    PromoteWith as PromoteWith,
    PromoteWith0D as PromoteWith0D,
)
from ._scalar import (
    inexact32 as inexact32,
    inexact64 as inexact64,
    inexact64l as inexact64l,
    integer8 as integer8,
    integer16 as integer16,
    integer32 as integer32,
    integer64 as integer64,
    integer_l as integer_l,
    number16 as number16,
    number32 as number32,
    number64 as number64,
)
from ._scalar_co import (
    co_complex as co_complex,
    co_complex64 as co_complex64,
    co_complex128 as co_complex128,
    co_datetime as co_datetime,
    co_float as co_float,
    co_float16 as co_float16,
    co_float32 as co_float32,
    co_float64 as co_float64,
    co_int8 as co_int8,
    co_int16 as co_int16,
    co_int32 as co_int32,
    co_int64 as co_int64,
    co_integer as co_integer,
    co_integer8 as co_integer8,
    co_integer16 as co_integer16,
    co_integer32 as co_integer32,
    co_integer64 as co_integer64,
    co_long as co_long,
    co_number as co_number,
    co_timedelta as co_timedelta,
    co_uint8 as co_uint8,
    co_uint16 as co_uint16,
    co_uint32 as co_uint32,
    co_uint64 as co_uint64,
    co_ulong as co_ulong,
)

###
# Type parameters

_T = TypeVar("_T")
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...], default=tuple[int, ...])
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
_ScalarT0 = TypeVar("_ScalarT0", bound=np.generic, default=Any)
_NaT = TypeVar("_NaT", default=Never)
_NaT0 = TypeVar("_NaT0", default=Any)
_NaT_co = TypeVar("_NaT_co", covariant=True)
_ToT = TypeVar("_ToT")

###
# Protocols

@type_check_only
class CanArray0D(Protocol[_ScalarT_co]):
    def __array__(self, /) -> np.ndarray[tuple[()], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanArray1D(Protocol[_ScalarT_co]):
    def __array__(self, /) -> np.ndarray[tuple[int], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanArray2D(Protocol[_ScalarT_co]):
    def __array__(self, /) -> np.ndarray[tuple[int, int], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanArray3D(Protocol[_ScalarT_co]):
    def __array__(self, /) -> np.ndarray[tuple[int, int, int], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanArrayND(Protocol[_ScalarT_co]):
    def __array__(self, /) -> np.ndarray[tuple[int, ...], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanLenArrayND(Protocol[_ScalarT_co]):
    def __len__(self, /) -> int: ...
    def __array__(self, /) -> np.ndarray[tuple[int, ...], np.dtype[_ScalarT_co]]: ...

@type_check_only
class CanLenArray(Protocol[_ScalarT_co, _ShapeT_co]):
    def __len__(self, /) -> int: ...
    def __array__(self, /) -> np.ndarray[_ShapeT_co, np.dtype[_ScalarT_co]]: ...

@type_check_only
class _CanStringArray(Protocol[_ShapeT_co, _NaT_co]):
    def __array__(self, /) -> np.ndarray[_ShapeT_co, np.dtypes.StringDType[_NaT_co]]: ...

###
# Shape aliases

AtLeast0D: TypeAlias = tuple[int, ...]
AtLeast1D = TypeAliasType("AtLeast1D", tuple[int, Unpack[tuple[int, ...]]])
AtLeast2D = TypeAliasType("AtLeast2D", tuple[int, int, Unpack[tuple[int, ...]]])
AtLeast3D = TypeAliasType("AtLeast3D", tuple[int, int, int, Unpack[tuple[int, ...]]])
AtLeast4D = TypeAliasType("AtLeast4D", tuple[int, int, int, int, Unpack[tuple[int, ...]]])

###
# Shape-typed sequences

# we can't use a custom Sequence type due to some mypy bug
Sequence2D: TypeAlias = Sequence[Sequence[_T]]
Sequence3D: TypeAlias = Sequence[Sequence[Sequence[_T]]]

# nested sequences with at least k dims, e.g. `2nd` denotes a dimensionality in the interval [2, n]
SequenceND: TypeAlias = _T | _NestedSequence[_T]
Sequence1ND: TypeAlias = _NestedSequence[_T]
Sequence2ND: TypeAlias = Sequence[_NestedSequence[_T]]
Sequence3ND: TypeAlias = Sequence[Sequence[_NestedSequence[_T]]]

###
# Shape-typed array aliases

Array = TypeAliasType("Array", np.ndarray[_ShapeT, np.dtype[_ScalarT0]], type_params=(_ScalarT0, _ShapeT))
Array0D = TypeAliasType("Array0D", np.ndarray[tuple[()], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
Array1D = TypeAliasType("Array1D", np.ndarray[tuple[int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
Array2D = TypeAliasType("Array2D", np.ndarray[tuple[int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
Array3D = TypeAliasType("Array3D", np.ndarray[tuple[int, int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
Array4D = TypeAliasType("Array4D", np.ndarray[tuple[int, int, int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))

MArray = TypeAliasType("MArray", np.ma.MaskedArray[_ShapeT, np.dtype[_ScalarT0]], type_params=(_ScalarT0, _ShapeT))
MArray0D = TypeAliasType("MArray0D", np.ma.MaskedArray[tuple[()], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
MArray1D = TypeAliasType("MArray1D", np.ma.MaskedArray[tuple[int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
MArray2D = TypeAliasType("MArray2D", np.ma.MaskedArray[tuple[int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))
MArray3D = TypeAliasType(
    "MArray3D",
    np.ma.MaskedArray[tuple[int, int, int], np.dtype[_ScalarT0]],
    type_params=(_ScalarT0,),
)

Matrix = TypeAliasType("Matrix", np.matrix[tuple[int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))

StringArray = TypeAliasType(
    "StringArray",
    np.ndarray[_ShapeT, np.dtypes.StringDType[_NaT]],
    type_params=(_ShapeT, _NaT),
)
StringArray0D = TypeAliasType(
    "StringArray0D",
    np.ndarray[tuple[()], np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray1D = TypeAliasType(
    "StringArray1D",
    np.ndarray[tuple[int], np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray2D = TypeAliasType(
    "StringArray2D",
    np.ndarray[tuple[int, int], np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray3D = TypeAliasType(
    "StringArray3D",
    np.ndarray[tuple[int, int, int], np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArrayND = TypeAliasType(
    "StringArrayND",
    np.ndarray[tuple[int, ...], np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)

###
# helper aliases

_PyReal: TypeAlias = JustInt | JustFloat
_PyInexact: TypeAlias = JustFloat | JustComplex
_PyNumber: TypeAlias = JustInt | _PyInexact
_PyCharacter: TypeAlias = JustBytes | JustStr
# anything immutable that results in an `object_` dtype
_PyObject: TypeAlias = decimal.Decimal | fractions.Fraction
_PyScalar: TypeAlias = complex | _PyCharacter | _PyObject

_ToArray2_0d: TypeAlias = CanArray0D[_ScalarT] | _ToT
_ToArray_nd: TypeAlias = SequenceND[CanArrayND[_ScalarT]]
_ToArray2_nd: TypeAlias = SequenceND[CanArrayND[_ScalarT] | _ToT]

# don't require matching shape-types by default
_ToArray_1d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[CanArray0D[_ScalarT]]
_ToArray2_1d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[_ToArray2_0d[_ScalarT, _ToT]]
_ToArray_2d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[_ToArray_1d[_ScalarT]]
_ToArray2_2d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[_ToArray2_1d[_ScalarT, _ToT]]
_ToArray_3d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[_ToArray_2d[_ScalarT]]
_ToArray2_3d: TypeAlias = CanLenArrayND[_ScalarT] | Sequence[_ToArray2_2d[_ScalarT, _ToT]]

# requires ndarray to be shape-types (the `s` suffix stands for "strict")
_ToArray_1ds: TypeAlias = CanArray1D[_ScalarT] | Sequence[CanArray0D[_ScalarT]]
_ToArray2_1ds: TypeAlias = CanArray1D[_ScalarT] | Sequence[_ToArray2_0d[_ScalarT, _ToT]]
_ToArray_2ds: TypeAlias = CanArray2D[_ScalarT] | Sequence[_ToArray_1ds[_ScalarT]]
_ToArray2_2ds: TypeAlias = CanArray2D[_ScalarT] | Sequence[_ToArray2_1ds[_ScalarT, _ToT]]
_ToArray_3ds: TypeAlias = CanArray3D[_ScalarT] | Sequence[_ToArray_2ds[_ScalarT]]
_ToArray2_3ds: TypeAlias = CanArray3D[_ScalarT] | Sequence[_ToArray2_2ds[_ScalarT, _ToT]]

# requires a lower bound on dimensionality, e.g. `_2nd` denotes `ndin` within `[2, n]`
_ToArray_1nd: TypeAlias = CanLenArrayND[_ScalarT] | Sequence1ND[CanArrayND[_ScalarT]]
_ToArray2_1nd: TypeAlias = CanLenArrayND[_ScalarT] | Sequence1ND[_ToT | CanArrayND[_ScalarT]]
_ToArray_2nd: TypeAlias = CanLenArray[_ScalarT, AtLeast2D] | Sequence[_ToArray_1nd[_ScalarT]]
_ToArray2_2nd: TypeAlias = CanLenArray[_ScalarT, AtLeast2D] | Sequence[_ToArray2_1nd[_ScalarT, _ToT]]
_ToArray_3nd: TypeAlias = CanLenArray[_ScalarT, AtLeast3D] | Sequence[_ToArray_2nd[_ScalarT]]
_ToArray2_3nd: TypeAlias = CanLenArray[_ScalarT, AtLeast3D] | Sequence[_ToArray2_2nd[_ScalarT, _ToT]]

###
# Non-overlapping scalar- and array-like aliases for all scalar types.

# bool
_ToBool: TypeAlias = np.bool[Any]
ToBool_nd = TypeAliasType("ToBool_nd", _ToArray2_nd[_ToBool, bool])
ToBool_0d = TypeAliasType("ToBool_0d", _ToArray2_0d[_ToBool, bool])
ToBool_1d = TypeAliasType("ToBool_1d", _ToArray2_1d[_ToBool, bool])
ToBool_2d = TypeAliasType("ToBool_2d", _ToArray2_2d[_ToBool, bool])
ToBool_3d = TypeAliasType("ToBool_3d", _ToArray2_3d[_ToBool, bool])
ToBool_1ds = TypeAliasType("ToBool_1ds", _ToArray2_1ds[_ToBool, bool])
ToBool_2ds = TypeAliasType("ToBool_2ds", _ToArray2_2ds[_ToBool, bool])
ToBool_3ds = TypeAliasType("ToBool_3ds", _ToArray2_3ds[_ToBool, bool])
ToBool_1nd = TypeAliasType("ToBool_1nd", _ToArray2_1nd[_ToBool, bool])
ToBool_2nd = TypeAliasType("ToBool_2nd", _ToArray2_2nd[_ToBool, bool])
ToBool_3nd = TypeAliasType("ToBool_3nd", _ToArray2_3nd[_ToBool, bool])

# unsigned integers
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _ToArray_nd[np.uint8])
ToUInt8_0d = TypeAliasType("ToUInt8_0d", CanArray0D[np.uint8])
ToUInt8_1d = TypeAliasType("ToUInt8_1d", _ToArray_1d[np.uint8])
ToUInt8_2d = TypeAliasType("ToUInt8_2d", _ToArray_2d[np.uint8])
ToUInt8_3d = TypeAliasType("ToUInt8_3d", _ToArray_3d[np.uint8])
ToUInt8_1ds = TypeAliasType("ToUInt8_1ds", _ToArray_1ds[np.uint8])
ToUInt8_2ds = TypeAliasType("ToUInt8_2ds", _ToArray_2ds[np.uint8])
ToUInt8_3ds = TypeAliasType("ToUInt8_3ds", _ToArray_3ds[np.uint8])
ToUInt8_1nd = TypeAliasType("ToUInt8_1nd", _ToArray_1nd[np.uint8])
ToUInt8_2nd = TypeAliasType("ToUInt8_2nd", _ToArray_2nd[np.uint8])
ToUInt8_3nd = TypeAliasType("ToUInt8_3nd", _ToArray_3nd[np.uint8])

ToUInt16_nd = TypeAliasType("ToUInt16_nd", _ToArray_nd[np.uint16])
ToUInt16_0d = TypeAliasType("ToUInt16_0d", CanArray0D[np.uint16])
ToUInt16_1d = TypeAliasType("ToUInt16_1d", _ToArray_1d[np.uint16])
ToUInt16_2d = TypeAliasType("ToUInt16_2d", _ToArray_2d[np.uint16])
ToUInt16_3d = TypeAliasType("ToUInt16_3d", _ToArray_3d[np.uint16])
ToUInt16_1ds = TypeAliasType("ToUInt16_1ds", _ToArray_1ds[np.uint16])
ToUInt16_2ds = TypeAliasType("ToUInt16_2ds", _ToArray_2ds[np.uint16])
ToUInt16_3ds = TypeAliasType("ToUInt16_3ds", _ToArray_3ds[np.uint16])
ToUInt16_1nd = TypeAliasType("ToUInt16_1nd", _ToArray_1nd[np.uint16])
ToUInt16_2nd = TypeAliasType("ToUInt16_2nd", _ToArray_2nd[np.uint16])
ToUInt16_3nd = TypeAliasType("ToUInt16_3nd", _ToArray_3nd[np.uint16])

ToUInt32_nd = TypeAliasType("ToUInt32_nd", _ToArray_nd[np.uint32])
ToUInt32_0d = TypeAliasType("ToUInt32_0d", CanArray0D[np.uint32])
ToUInt32_1d = TypeAliasType("ToUInt32_1d", _ToArray_1d[np.uint32])
ToUInt32_2d = TypeAliasType("ToUInt32_2d", _ToArray_2d[np.uint32])
ToUInt32_3d = TypeAliasType("ToUInt32_3d", _ToArray_3d[np.uint32])
ToUInt32_1ds = TypeAliasType("ToUInt32_1ds", _ToArray_1ds[np.uint32])
ToUInt32_2ds = TypeAliasType("ToUInt32_2ds", _ToArray_2ds[np.uint32])
ToUInt32_3ds = TypeAliasType("ToUInt32_3ds", _ToArray_3ds[np.uint32])
ToUInt32_1nd = TypeAliasType("ToUInt32_1nd", _ToArray_1nd[np.uint32])
ToUInt32_2nd = TypeAliasType("ToUInt32_2nd", _ToArray_2nd[np.uint32])
ToUInt32_3nd = TypeAliasType("ToUInt32_3nd", _ToArray_3nd[np.uint32])

ToULong_nd = TypeAliasType("ToULong_nd", _ToArray_nd[np.ulong])
ToULong_0d = TypeAliasType("ToULong_0d", CanArray0D[np.ulong])
ToULong_1d = TypeAliasType("ToULong_1d", _ToArray_1d[np.ulong])
ToULong_2d = TypeAliasType("ToULong_2d", _ToArray_2d[np.ulong])
ToULong_3d = TypeAliasType("ToULong_3d", _ToArray_3d[np.ulong])
ToULong_1ds = TypeAliasType("ToULong_1ds", _ToArray_1ds[np.ulong])
ToULong_2ds = TypeAliasType("ToULong_2ds", _ToArray_2ds[np.ulong])
ToULong_3ds = TypeAliasType("ToULong_3ds", _ToArray_3ds[np.ulong])
ToULong_1nd = TypeAliasType("ToULong_1nd", _ToArray_1nd[np.ulong])
ToULong_2nd = TypeAliasType("ToULong_2nd", _ToArray_2nd[np.ulong])
ToULong_3nd = TypeAliasType("ToULong_3nd", _ToArray_3nd[np.ulong])

ToUInt64_nd = TypeAliasType("ToUInt64_nd", _ToArray_nd[np.uint64])
ToUInt64_0d = TypeAliasType("ToUInt64_0d", CanArray0D[np.uint64])
ToUInt64_1d = TypeAliasType("ToUInt64_1d", _ToArray_1d[np.uint64])
ToUInt64_2d = TypeAliasType("ToUInt64_2d", _ToArray_2d[np.uint64])
ToUInt64_3d = TypeAliasType("ToUInt64_3d", _ToArray_3d[np.uint64])
ToUInt64_1ds = TypeAliasType("ToUInt64_1ds", _ToArray_1ds[np.uint64])
ToUInt64_2ds = TypeAliasType("ToUInt64_2ds", _ToArray_2ds[np.uint64])
ToUInt64_3ds = TypeAliasType("ToUInt64_3ds", _ToArray_3ds[np.uint64])
ToUInt64_1nd = TypeAliasType("ToUInt64_1nd", _ToArray_1nd[np.uint64])
ToUInt64_2nd = TypeAliasType("ToUInt64_2nd", _ToArray_2nd[np.uint64])
ToUInt64_3nd = TypeAliasType("ToUInt64_3nd", _ToArray_3nd[np.uint64])

ToUInteger_nd = TypeAliasType("ToUInteger_nd", _ToArray_nd[np.unsignedinteger])
ToUInteger_0d = TypeAliasType("ToUInteger_0d", CanArray0D[np.unsignedinteger])
ToUInteger_1d = TypeAliasType("ToUInteger_1d", _ToArray_1d[np.unsignedinteger])
ToUInteger_2d = TypeAliasType("ToUInteger_2d", _ToArray_2d[np.unsignedinteger])
ToUInteger_3d = TypeAliasType("ToUInteger_3d", _ToArray_3d[np.unsignedinteger])
ToUInteger_1ds = TypeAliasType("ToUInteger_1ds", _ToArray_1ds[np.unsignedinteger])
ToUInteger_2ds = TypeAliasType("ToUInteger_2ds", _ToArray_2ds[np.unsignedinteger])
ToUInteger_3ds = TypeAliasType("ToUInteger_3ds", _ToArray_3ds[np.unsignedinteger])
ToUInteger_1nd = TypeAliasType("ToUInteger_1nd", _ToArray_1nd[np.unsignedinteger])
ToUInteger_2nd = TypeAliasType("ToUInteger_2nd", _ToArray_2nd[np.unsignedinteger])
ToUInteger_3nd = TypeAliasType("ToUInteger_3nd", _ToArray_3nd[np.unsignedinteger])

# signed integers
ToInt8_nd = TypeAliasType("ToInt8_nd", _ToArray_nd[np.int8])
ToInt8_0d = TypeAliasType("ToInt8_0d", CanArray0D[np.int8])
ToInt8_1d = TypeAliasType("ToInt8_1d", _ToArray_1d[np.int8])
ToInt8_2d = TypeAliasType("ToInt8_2d", _ToArray_2d[np.int8])
ToInt8_3d = TypeAliasType("ToInt8_3d", _ToArray_3d[np.int8])
ToInt8_1ds = TypeAliasType("ToInt8_1ds", _ToArray_1ds[np.int8])
ToInt8_2ds = TypeAliasType("ToInt8_2ds", _ToArray_2ds[np.int8])
ToInt8_3ds = TypeAliasType("ToInt8_3ds", _ToArray_3ds[np.int8])
ToInt8_1nd = TypeAliasType("ToInt8_1nd", _ToArray_1nd[np.int8])
ToInt8_2nd = TypeAliasType("ToInt8_2nd", _ToArray_2nd[np.int8])
ToInt8_3nd = TypeAliasType("ToInt8_3nd", _ToArray_3nd[np.int8])

ToInt16_nd = TypeAliasType("ToInt16_nd", _ToArray_nd[np.int16])
ToInt16_0d = TypeAliasType("ToInt16_0d", CanArray0D[np.int16])
ToInt16_1d = TypeAliasType("ToInt16_1d", _ToArray_1d[np.int16])
ToInt16_2d = TypeAliasType("ToInt16_2d", _ToArray_2d[np.int16])
ToInt16_3d = TypeAliasType("ToInt16_3d", _ToArray_3d[np.int16])
ToInt16_1ds = TypeAliasType("ToInt16_1ds", _ToArray_1ds[np.int16])
ToInt16_2ds = TypeAliasType("ToInt16_2ds", _ToArray_2ds[np.int16])
ToInt16_3ds = TypeAliasType("ToInt16_3ds", _ToArray_3ds[np.int16])
ToInt16_1nd = TypeAliasType("ToInt16_1nd", _ToArray_1nd[np.int16])
ToInt16_2nd = TypeAliasType("ToInt16_2nd", _ToArray_2nd[np.int16])
ToInt16_3nd = TypeAliasType("ToInt16_3nd", _ToArray_3nd[np.int16])

ToInt32_nd = TypeAliasType("ToInt32_nd", _ToArray_nd[np.int32])
ToInt32_0d = TypeAliasType("ToInt32_0d", CanArray0D[np.int32])
ToInt32_1d = TypeAliasType("ToInt32_1d", _ToArray_1d[np.int32])
ToInt32_2d = TypeAliasType("ToInt32_2d", _ToArray_2d[np.int32])
ToInt32_3d = TypeAliasType("ToInt32_3d", _ToArray_3d[np.int32])
ToInt32_1ds = TypeAliasType("ToInt32_1ds", _ToArray_1ds[np.int32])
ToInt32_2ds = TypeAliasType("ToInt32_2ds", _ToArray_2ds[np.int32])
ToInt32_3ds = TypeAliasType("ToInt32_3ds", _ToArray_3ds[np.int32])
ToInt32_1nd = TypeAliasType("ToInt32_1nd", _ToArray_1nd[np.int32])
ToInt32_2nd = TypeAliasType("ToInt32_2nd", _ToArray_2nd[np.int32])
ToInt32_3nd = TypeAliasType("ToInt32_3nd", _ToArray_3nd[np.int32])

ToLong_nd = TypeAliasType("ToLong_nd", _ToArray_nd[np.long])
ToLong_0d = TypeAliasType("ToLong_0d", CanArray0D[np.long])
ToLong_1d = TypeAliasType("ToLong_1d", _ToArray_1d[np.long])
ToLong_2d = TypeAliasType("ToLong_2d", _ToArray_2d[np.long])
ToLong_3d = TypeAliasType("ToLong_3d", _ToArray_3d[np.long])
ToLong_1ds = TypeAliasType("ToLong_1ds", _ToArray_1ds[np.long])
ToLong_2ds = TypeAliasType("ToLong_2ds", _ToArray_2ds[np.long])
ToLong_3ds = TypeAliasType("ToLong_3ds", _ToArray_3ds[np.long])
ToLong_1nd = TypeAliasType("ToLong_1nd", _ToArray_1nd[np.long])
ToLong_2nd = TypeAliasType("ToLong_2nd", _ToArray_2nd[np.long])
ToLong_3nd = TypeAliasType("ToLong_3nd", _ToArray_3nd[np.long])

ToInt64_nd = TypeAliasType("ToInt64_nd", _ToArray_nd[np.int64])
ToInt64_0d = TypeAliasType("ToInt64_0d", CanArray0D[np.int64])
ToInt64_1d = TypeAliasType("ToInt64_1d", _ToArray_1d[np.int64])
ToInt64_2d = TypeAliasType("ToInt64_2d", _ToArray_2d[np.int64])
ToInt64_3d = TypeAliasType("ToInt64_3d", _ToArray_3d[np.int64])
ToInt64_1ds = TypeAliasType("ToInt64_1ds", _ToArray_1ds[np.int64])
ToInt64_2ds = TypeAliasType("ToInt64_2ds", _ToArray_2ds[np.int64])
ToInt64_3ds = TypeAliasType("ToInt64_3ds", _ToArray_3ds[np.int64])
ToInt64_1nd = TypeAliasType("ToInt64_1nd", _ToArray_1nd[np.int64])
ToInt64_2nd = TypeAliasType("ToInt64_2nd", _ToArray_2nd[np.int64])
ToInt64_3nd = TypeAliasType("ToInt64_3nd", _ToArray_3nd[np.int64])

ToInt_nd = TypeAliasType("ToInt_nd", _ToArray2_nd[np.intp, JustInt])
ToInt_0d = TypeAliasType("ToInt_0d", _ToArray2_0d[np.intp, JustInt])
ToInt_1d = TypeAliasType("ToInt_1d", _ToArray2_1d[np.intp, JustInt])
ToInt_2d = TypeAliasType("ToInt_2d", _ToArray2_2d[np.intp, JustInt])
ToInt_3d = TypeAliasType("ToInt_3d", _ToArray2_3d[np.intp, JustInt])
ToInt_1ds = TypeAliasType("ToInt_1ds", _ToArray2_1ds[np.intp, JustInt])
ToInt_2ds = TypeAliasType("ToInt_2ds", _ToArray2_2ds[np.intp, JustInt])
ToInt_3ds = TypeAliasType("ToInt_3ds", _ToArray2_3ds[np.intp, JustInt])
ToInt_1nd = TypeAliasType("ToInt_1nd", _ToArray2_1nd[np.intp, JustInt])
ToInt_2nd = TypeAliasType("ToInt_2nd", _ToArray2_2nd[np.intp, JustInt])
ToInt_3nd = TypeAliasType("ToInt_3nd", _ToArray2_3nd[np.intp, JustInt])

ToSInteger_nd = TypeAliasType("ToSInteger_nd", _ToArray2_nd[np.signedinteger, JustInt])
ToSInteger_0d = TypeAliasType("ToSInteger_0d", _ToArray2_0d[np.signedinteger, JustInt])
ToSInteger_1d = TypeAliasType("ToSInteger_1d", _ToArray2_1d[np.signedinteger, JustInt])
ToSInteger_2d = TypeAliasType("ToSInteger_2d", _ToArray2_2d[np.signedinteger, JustInt])
ToSInteger_3d = TypeAliasType("ToSInteger_3d", _ToArray2_3d[np.signedinteger, JustInt])
ToSInteger_1ds = TypeAliasType("ToSInteger_1ds", _ToArray2_1ds[np.signedinteger, JustInt])
ToSInteger_2ds = TypeAliasType("ToSInteger_2ds", _ToArray2_2ds[np.signedinteger, JustInt])
ToSInteger_3ds = TypeAliasType("ToSInteger_3ds", _ToArray2_3ds[np.signedinteger, JustInt])
ToSInteger_1nd = TypeAliasType("ToSInteger_1nd", _ToArray2_1nd[np.signedinteger, JustInt])
ToSInteger_2nd = TypeAliasType("ToSInteger_2nd", _ToArray2_2nd[np.signedinteger, JustInt])
ToSInteger_3nd = TypeAliasType("ToSInteger_3nd", _ToArray2_3nd[np.signedinteger, JustInt])

# integers
ToInteger_nd = TypeAliasType("ToInteger_nd", _ToArray2_nd[np.integer, JustInt])
ToInteger_0d = TypeAliasType("ToInteger_0d", _ToArray2_0d[np.integer, JustInt])
ToInteger_1d = TypeAliasType("ToInteger_1d", _ToArray2_1d[np.integer, JustInt])
ToInteger_2d = TypeAliasType("ToInteger_2d", _ToArray2_2d[np.integer, JustInt])
ToInteger_3d = TypeAliasType("ToInteger_3d", _ToArray2_3d[np.integer, JustInt])
ToInteger_1ds = TypeAliasType("ToInteger_1ds", _ToArray2_1ds[np.integer, JustInt])
ToInteger_2ds = TypeAliasType("ToInteger_2ds", _ToArray2_2ds[np.integer, JustInt])
ToInteger_3ds = TypeAliasType("ToInteger_3ds", _ToArray2_3ds[np.integer, JustInt])
ToInteger_1nd = TypeAliasType("ToInteger_1nd", _ToArray2_1nd[np.integer, JustInt])
ToInteger_2nd = TypeAliasType("ToInteger_2nd", _ToArray2_2nd[np.integer, JustInt])
ToInteger_3nd = TypeAliasType("ToInteger_3nd", _ToArray2_3nd[np.integer, JustInt])

# real floats
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _ToArray_nd[np.float16])
ToFloat16_0d = TypeAliasType("ToFloat16_0d", CanArray0D[np.float16])
ToFloat16_1d = TypeAliasType("ToFloat16_1d", _ToArray_1d[np.float16])
ToFloat16_2d = TypeAliasType("ToFloat16_2d", _ToArray_2d[np.float16])
ToFloat16_3d = TypeAliasType("ToFloat16_3d", _ToArray_3d[np.float16])
ToFloat16_1ds = TypeAliasType("ToFloat16_1ds", _ToArray_1ds[np.float16])
ToFloat16_2ds = TypeAliasType("ToFloat16_2ds", _ToArray_2ds[np.float16])
ToFloat16_3ds = TypeAliasType("ToFloat16_3ds", _ToArray_3ds[np.float16])
ToFloat16_1nd = TypeAliasType("ToFloat16_1nd", _ToArray_1nd[np.float16])
ToFloat16_2nd = TypeAliasType("ToFloat16_2nd", _ToArray_2nd[np.float16])
ToFloat16_3nd = TypeAliasType("ToFloat16_3nd", _ToArray_3nd[np.float16])

ToFloat32_nd = TypeAliasType("ToFloat32_nd", _ToArray_nd[np.float32])
ToFloat32_0d = TypeAliasType("ToFloat32_0d", CanArray0D[np.float32])
ToFloat32_1d = TypeAliasType("ToFloat32_1d", _ToArray_1d[np.float32])
ToFloat32_2d = TypeAliasType("ToFloat32_2d", _ToArray_2d[np.float32])
ToFloat32_3d = TypeAliasType("ToFloat32_3d", _ToArray_3d[np.float32])
ToFloat32_1ds = TypeAliasType("ToFloat32_1ds", _ToArray_1ds[np.float32])
ToFloat32_2ds = TypeAliasType("ToFloat32_2ds", _ToArray_2ds[np.float32])
ToFloat32_3ds = TypeAliasType("ToFloat32_3ds", _ToArray_3ds[np.float32])
ToFloat32_1nd = TypeAliasType("ToFloat32_1nd", _ToArray_1nd[np.float32])
ToFloat32_2nd = TypeAliasType("ToFloat32_2nd", _ToArray_2nd[np.float32])
ToFloat32_3nd = TypeAliasType("ToFloat32_3nd", _ToArray_3nd[np.float32])

ToFloat64_nd = TypeAliasType("ToFloat64_nd", _ToArray2_nd[np.float64, JustFloat])
ToFloat64_0d = TypeAliasType("ToFloat64_0d", _ToArray2_0d[np.float64, JustFloat])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _ToArray2_1d[np.float64, JustFloat])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _ToArray2_2d[np.float64, JustFloat])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _ToArray2_3d[np.float64, JustFloat])
ToFloat64_1ds = TypeAliasType("ToFloat64_1ds", _ToArray2_1ds[np.float64, JustFloat])
ToFloat64_2ds = TypeAliasType("ToFloat64_2ds", _ToArray2_2ds[np.float64, JustFloat])
ToFloat64_3ds = TypeAliasType("ToFloat64_3ds", _ToArray2_3ds[np.float64, JustFloat])
ToFloat64_1nd = TypeAliasType("ToFloat64_1nd", _ToArray2_1nd[np.float64, JustFloat])
ToFloat64_2nd = TypeAliasType("ToFloat64_2nd", _ToArray2_2nd[np.float64, JustFloat])
ToFloat64_3nd = TypeAliasType("ToFloat64_3nd", _ToArray2_3nd[np.float64, JustFloat])

ToLongDouble_nd = TypeAliasType("ToLongDouble_nd", _ToArray_nd[np.longdouble])
ToLongDouble_0d = TypeAliasType("ToLongDouble_0d", CanArray0D[np.longdouble])
ToLongDouble_1d = TypeAliasType("ToLongDouble_1d", _ToArray_1d[np.longdouble])
ToLongDouble_2d = TypeAliasType("ToLongDouble_2d", _ToArray_2d[np.longdouble])
ToLongDouble_3d = TypeAliasType("ToLongDouble_3d", _ToArray_3d[np.longdouble])
ToLongDouble_1ds = TypeAliasType("ToLongDouble_1ds", _ToArray_1ds[np.longdouble])
ToLongDouble_2ds = TypeAliasType("ToLongDouble_2ds", _ToArray_2ds[np.longdouble])
ToLongDouble_3ds = TypeAliasType("ToLongDouble_3ds", _ToArray_3ds[np.longdouble])
ToLongDouble_1nd = TypeAliasType("ToLongDouble_1nd", _ToArray_1nd[np.longdouble])
ToLongDouble_2nd = TypeAliasType("ToLongDouble_2nd", _ToArray_2nd[np.longdouble])
ToLongDouble_3nd = TypeAliasType("ToLongDouble_3nd", _ToArray_3nd[np.longdouble])

ToFloating_nd = TypeAliasType("ToFloating_nd", _ToArray2_nd[np.floating, JustFloat])
ToFloating_0d = TypeAliasType("ToFloating_0d", _ToArray2_0d[np.floating, JustFloat])
ToFloating_1d = TypeAliasType("ToFloating_1d", _ToArray2_1d[np.floating, JustFloat])
ToFloating_2d = TypeAliasType("ToFloating_2d", _ToArray2_2d[np.floating, JustFloat])
ToFloating_3d = TypeAliasType("ToFloating_3d", _ToArray2_3d[np.floating, JustFloat])
ToFloating_1ds = TypeAliasType("ToFloating_1ds", _ToArray2_1ds[np.floating, JustFloat])
ToFloating_2ds = TypeAliasType("ToFloating_2ds", _ToArray2_2ds[np.floating, JustFloat])
ToFloating_3ds = TypeAliasType("ToFloating_3ds", _ToArray2_3ds[np.floating, JustFloat])
ToFloating_1nd = TypeAliasType("ToFloating_1nd", _ToArray2_1nd[np.floating, JustFloat])
ToFloating_2nd = TypeAliasType("ToFloating_2nd", _ToArray2_2nd[np.floating, JustFloat])
ToFloating_3nd = TypeAliasType("ToFloating_3nd", _ToArray2_3nd[np.floating, JustFloat])

# complex floats
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _ToArray_nd[np.complex64])
ToComplex64_0d = TypeAliasType("ToComplex64_0d", CanArray0D[np.complex64])
ToComplex64_1d = TypeAliasType("ToComplex64_1d", _ToArray_1d[np.complex64])
ToComplex64_2d = TypeAliasType("ToComplex64_2d", _ToArray_2d[np.complex64])
ToComplex64_3d = TypeAliasType("ToComplex64_3d", _ToArray_3d[np.complex64])
ToComplex64_1ds = TypeAliasType("ToComplex64_1ds", _ToArray_1ds[np.complex64])
ToComplex64_2ds = TypeAliasType("ToComplex64_2ds", _ToArray_2ds[np.complex64])
ToComplex64_3ds = TypeAliasType("ToComplex64_3ds", _ToArray_3ds[np.complex64])
ToComplex64_1nd = TypeAliasType("ToComplex64_1nd", _ToArray_1nd[np.complex64])
ToComplex64_2nd = TypeAliasType("ToComplex64_2nd", _ToArray_2nd[np.complex64])
ToComplex64_3nd = TypeAliasType("ToComplex64_3nd", _ToArray_3nd[np.complex64])

ToComplex128_nd = TypeAliasType("ToComplex128_nd", _ToArray2_nd[np.complex128, JustComplex])
ToComplex128_0d = TypeAliasType("ToComplex128_0d", _ToArray2_0d[np.complex128, JustComplex])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _ToArray2_1d[np.complex128, JustComplex])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _ToArray2_2d[np.complex128, JustComplex])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _ToArray2_3d[np.complex128, JustComplex])
ToComplex128_1ds = TypeAliasType("ToComplex128_1ds", _ToArray2_1ds[np.complex128, JustComplex])
ToComplex128_2ds = TypeAliasType("ToComplex128_2ds", _ToArray2_2ds[np.complex128, JustComplex])
ToComplex128_3ds = TypeAliasType("ToComplex128_3ds", _ToArray2_3ds[np.complex128, JustComplex])
ToComplex128_1nd = TypeAliasType("ToComplex128_1nd", _ToArray2_1nd[np.complex128, JustComplex])
ToComplex128_2nd = TypeAliasType("ToComplex128_2nd", _ToArray2_2nd[np.complex128, JustComplex])
ToComplex128_3nd = TypeAliasType("ToComplex128_3nd", _ToArray2_3nd[np.complex128, JustComplex])

ToCLongDouble_nd = TypeAliasType("ToCLongDouble_nd", _ToArray_nd[np.clongdouble])
ToCLongDouble_0d = TypeAliasType("ToCLongDouble_0d", CanArray0D[np.clongdouble])
ToCLongDouble_1d = TypeAliasType("ToCLongDouble_1d", _ToArray_1d[np.clongdouble])
ToCLongDouble_2d = TypeAliasType("ToCLongDouble_2d", _ToArray_2d[np.clongdouble])
ToCLongDouble_3d = TypeAliasType("ToCLongDouble_3d", _ToArray_3d[np.clongdouble])
ToCLongDouble_1ds = TypeAliasType("ToCLongDouble_1ds", _ToArray_1ds[np.clongdouble])
ToCLongDouble_2ds = TypeAliasType("ToCLongDouble_2ds", _ToArray_2ds[np.clongdouble])
ToCLongDouble_3ds = TypeAliasType("ToCLongDouble_3ds", _ToArray_3ds[np.clongdouble])
ToCLongDouble_1nd = TypeAliasType("ToCLongDouble_1nd", _ToArray_1nd[np.clongdouble])
ToCLongDouble_2nd = TypeAliasType("ToCLongDouble_2nd", _ToArray_2nd[np.clongdouble])
ToCLongDouble_3nd = TypeAliasType("ToCLongDouble_3nd", _ToArray_3nd[np.clongdouble])

ToComplex_nd = TypeAliasType("ToComplex_nd", _ToArray2_nd[np.complexfloating, JustComplex])
ToComplex_0d = TypeAliasType("ToComplex_0d", _ToArray2_0d[np.complexfloating, JustComplex])
ToComplex_1d = TypeAliasType("ToComplex_1d", _ToArray2_1d[np.complexfloating, JustComplex])
ToComplex_2d = TypeAliasType("ToComplex_2d", _ToArray2_2d[np.complexfloating, JustComplex])
ToComplex_3d = TypeAliasType("ToComplex_3d", _ToArray2_3d[np.complexfloating, JustComplex])
ToComplex_1ds = TypeAliasType("ToComplex_1ds", _ToArray2_1ds[np.complexfloating, JustComplex])
ToComplex_2ds = TypeAliasType("ToComplex_2ds", _ToArray2_2ds[np.complexfloating, JustComplex])
ToComplex_3ds = TypeAliasType("ToComplex_3ds", _ToArray2_3ds[np.complexfloating, JustComplex])
ToComplex_1nd = TypeAliasType("ToComplex_1nd", _ToArray2_1nd[np.complexfloating, JustComplex])
ToComplex_2nd = TypeAliasType("ToComplex_2nd", _ToArray2_2nd[np.complexfloating, JustComplex])
ToComplex_3nd = TypeAliasType("ToComplex_3nd", _ToArray2_3nd[np.complexfloating, JustComplex])

# integers, real- and complex floats (no booleans)
ToNumber_nd = TypeAliasType("ToNumber_nd", _ToArray2_nd[np.number, _PyNumber])
ToNumber_0d = TypeAliasType("ToNumber_0d", _ToArray2_0d[np.number, _PyNumber])
ToNumber_1d = TypeAliasType("ToNumber_1d", _ToArray2_1d[np.number, _PyNumber])
ToNumber_2d = TypeAliasType("ToNumber_2d", _ToArray2_2d[np.number, _PyNumber])
ToNumber_3d = TypeAliasType("ToNumber_3d", _ToArray2_3d[np.number, _PyNumber])
ToNumber_1ds = TypeAliasType("ToNumber_1ds", _ToArray2_1ds[np.number, _PyNumber])
ToNumber_2ds = TypeAliasType("ToNumber_2ds", _ToArray2_2ds[np.number, _PyNumber])
ToNumber_3ds = TypeAliasType("ToNumber_3ds", _ToArray2_3ds[np.number, _PyNumber])
ToNumber_1nd = TypeAliasType("ToNumber_1nd", _ToArray2_1nd[np.number, _PyNumber])
ToNumber_2nd = TypeAliasType("ToNumber_2nd", _ToArray2_2nd[np.number, _PyNumber])
ToNumber_3nd = TypeAliasType("ToNumber_3nd", _ToArray2_3nd[np.number, _PyNumber])

# integers and real floats
ToReal_nd = TypeAliasType("ToReal_nd", _ToArray2_nd[np.number[Any, float], _PyReal])
ToReal_0d = TypeAliasType("ToReal_0d", _ToArray2_0d[np.number[Any, float], _PyReal])
ToReal_1d = TypeAliasType("ToReal_1d", _ToArray2_1d[np.number[Any, float], _PyReal])
ToReal_2d = TypeAliasType("ToReal_2d", _ToArray2_2d[np.number[Any, float], _PyReal])
ToReal_3d = TypeAliasType("ToReal_3d", _ToArray2_3d[np.number[Any, float], _PyReal])
ToReal_1ds = TypeAliasType("ToReal_1ds", _ToArray2_1ds[np.number[Any, float], _PyReal])
ToReal_2ds = TypeAliasType("ToReal_2ds", _ToArray2_2ds[np.number[Any, float], _PyReal])
ToReal_3ds = TypeAliasType("ToReal_3ds", _ToArray2_3ds[np.number[Any, float], _PyReal])
ToReal_1nd = TypeAliasType("ToReal_1nd", _ToArray2_1nd[np.number[Any, float], _PyReal])
ToReal_2nd = TypeAliasType("ToReal_2nd", _ToArray2_2nd[np.number[Any, float], _PyReal])
ToReal_3nd = TypeAliasType("ToReal_3nd", _ToArray2_3nd[np.number[Any, float], _PyReal])

# real- and complex floats
ToInexact_nd = TypeAliasType("ToInexact_nd", _ToArray2_nd[np.inexact, _PyInexact])
ToInexact_0d = TypeAliasType("ToInexact_0d", _ToArray2_0d[np.inexact, _PyInexact])
ToInexact_1d = TypeAliasType("ToInexact_1d", _ToArray2_1d[np.inexact, _PyInexact])
ToInexact_2d = TypeAliasType("ToInexact_2d", _ToArray2_2d[np.inexact, _PyInexact])
ToInexact_3d = TypeAliasType("ToInexact_3d", _ToArray2_3d[np.inexact, _PyInexact])
ToInexact_1ds = TypeAliasType("ToInexact_1ds", _ToArray2_1ds[np.inexact, _PyInexact])
ToInexact_2ds = TypeAliasType("ToInexact_2ds", _ToArray2_2ds[np.inexact, _PyInexact])
ToInexact_3ds = TypeAliasType("ToInexact_3ds", _ToArray2_3ds[np.inexact, _PyInexact])
ToInexact_1nd = TypeAliasType("ToInexact_1nd", _ToArray2_1nd[np.inexact, _PyInexact])
ToInexact_2nd = TypeAliasType("ToInexact_2nd", _ToArray2_2nd[np.inexact, _PyInexact])
ToInexact_3nd = TypeAliasType("ToInexact_3nd", _ToArray2_3nd[np.inexact, _PyInexact])

# temporal
_ToTimeDelta: TypeAlias = np.timedelta64[Any]
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _ToArray_nd[_ToTimeDelta])
ToTimeDelta_0d = TypeAliasType("ToTimeDelta_0d", CanArray0D[_ToTimeDelta])
ToTimeDelta_1d = TypeAliasType("ToTimeDelta_1d", _ToArray_1d[_ToTimeDelta])
ToTimeDelta_2d = TypeAliasType("ToTimeDelta_2d", _ToArray_2d[_ToTimeDelta])
ToTimeDelta_3d = TypeAliasType("ToTimeDelta_3d", _ToArray_3d[_ToTimeDelta])
ToTimeDelta_1ds = TypeAliasType("ToTimeDelta_1ds", _ToArray_1ds[_ToTimeDelta])
ToTimeDelta_2ds = TypeAliasType("ToTimeDelta_2ds", _ToArray_2ds[_ToTimeDelta])
ToTimeDelta_3ds = TypeAliasType("ToTimeDelta_3ds", _ToArray_3ds[_ToTimeDelta])
ToTimeDelta_1nd = TypeAliasType("ToTimeDelta_1nd", _ToArray_1nd[_ToTimeDelta])
ToTimeDelta_2nd = TypeAliasType("ToTimeDelta_2nd", _ToArray_2nd[_ToTimeDelta])
ToTimeDelta_3nd = TypeAliasType("ToTimeDelta_3nd", _ToArray_3nd[_ToTimeDelta])

_ToDateTime: TypeAlias = np.datetime64[Any]
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _ToArray_nd[_ToDateTime])
ToDateTime_0d = TypeAliasType("ToDateTime_0d", CanArray0D[_ToDateTime])
ToDateTime_1d = TypeAliasType("ToDateTime_1d", _ToArray_1d[_ToDateTime])
ToDateTime_2d = TypeAliasType("ToDateTime_2d", _ToArray_2d[_ToDateTime])
ToDateTime_3d = TypeAliasType("ToDateTime_3d", _ToArray_3d[_ToDateTime])
ToDateTime_1ds = TypeAliasType("ToDateTime_1ds", _ToArray_1ds[_ToDateTime])
ToDateTime_2ds = TypeAliasType("ToDateTime_2ds", _ToArray_2ds[_ToDateTime])
ToDateTime_3ds = TypeAliasType("ToDateTime_3ds", _ToArray_3ds[_ToDateTime])
ToDateTime_1nd = TypeAliasType("ToDateTime_1nd", _ToArray_1nd[_ToDateTime])
ToDateTime_2nd = TypeAliasType("ToDateTime_2nd", _ToArray_2nd[_ToDateTime])
ToDateTime_3nd = TypeAliasType("ToDateTime_3nd", _ToArray_3nd[_ToDateTime])

# fixed strings
_ToBytes: TypeAlias = np.character[bytes]
ToBytes_nd = TypeAliasType("ToBytes_nd", _ToArray2_nd[_ToBytes, JustBytes])
ToBytes_0d = TypeAliasType("ToBytes_0d", _ToArray2_0d[_ToBytes, JustBytes])
ToBytes_1d = TypeAliasType("ToBytes_1d", _ToArray2_1d[_ToBytes, JustBytes])
ToBytes_2d = TypeAliasType("ToBytes_2d", _ToArray2_2d[_ToBytes, JustBytes])
ToBytes_3d = TypeAliasType("ToBytes_3d", _ToArray2_3d[_ToBytes, JustBytes])
ToBytes_1ds = TypeAliasType("ToBytes_1ds", _ToArray2_1ds[_ToBytes, JustBytes])
ToBytes_2ds = TypeAliasType("ToBytes_2ds", _ToArray2_2ds[_ToBytes, JustBytes])
ToBytes_3ds = TypeAliasType("ToBytes_3ds", _ToArray2_3ds[_ToBytes, JustBytes])
ToBytes_1nd = TypeAliasType("ToBytes_1nd", _ToArray2_1nd[_ToBytes, JustBytes])
ToBytes_2nd = TypeAliasType("ToBytes_2nd", _ToArray2_2nd[_ToBytes, JustBytes])
ToBytes_3nd = TypeAliasType("ToBytes_3nd", _ToArray2_3nd[_ToBytes, JustBytes])

_ToStr: TypeAlias = np.character[str]
ToStr_nd = TypeAliasType("ToStr_nd", _ToArray2_nd[_ToStr, JustStr])
ToStr_0d = TypeAliasType("ToStr_0d", _ToArray2_0d[_ToStr, JustStr])
ToStr_1d = TypeAliasType("ToStr_1d", _ToArray2_1d[_ToStr, JustStr])
ToStr_2d = TypeAliasType("ToStr_2d", _ToArray2_2d[_ToStr, JustStr])
ToStr_3d = TypeAliasType("ToStr_3d", _ToArray2_3d[_ToStr, JustStr])
ToStr_1ds = TypeAliasType("ToStr_1ds", _ToArray2_1ds[_ToStr, JustStr])
ToStr_2ds = TypeAliasType("ToStr_2ds", _ToArray2_2ds[_ToStr, JustStr])
ToStr_3ds = TypeAliasType("ToStr_3ds", _ToArray2_3ds[_ToStr, JustStr])
ToStr_1nd = TypeAliasType("ToStr_1nd", _ToArray2_1nd[_ToStr, JustStr])
ToStr_2nd = TypeAliasType("ToStr_2nd", _ToArray2_2nd[_ToStr, JustStr])
ToStr_3nd = TypeAliasType("ToStr_3nd", _ToArray2_3nd[_ToStr, JustStr])

_ToCharacter: TypeAlias = np.character[Any]
ToCharacter_nd = TypeAliasType("ToCharacter_nd", _ToArray2_nd[_ToCharacter, _PyCharacter])
ToCharacter_0d = TypeAliasType("ToCharacter_0d", _ToArray2_0d[_ToCharacter, _PyCharacter])
ToCharacter_1d = TypeAliasType("ToCharacter_1d", _ToArray2_1d[_ToCharacter, _PyCharacter])
ToCharacter_2d = TypeAliasType("ToCharacter_2d", _ToArray2_2d[_ToCharacter, _PyCharacter])
ToCharacter_3d = TypeAliasType("ToCharacter_3d", _ToArray2_3d[_ToCharacter, _PyCharacter])
ToCharacter_1ds = TypeAliasType("ToCharacter_1ds", _ToArray2_1ds[_ToCharacter, _PyCharacter])
ToCharacter_2ds = TypeAliasType("ToCharacter_2ds", _ToArray2_2ds[_ToCharacter, _PyCharacter])
ToCharacter_3ds = TypeAliasType("ToCharacter_3ds", _ToArray2_3ds[_ToCharacter, _PyCharacter])
ToCharacter_1nd = TypeAliasType("ToCharacter_1nd", _ToArray2_1nd[_ToCharacter, _PyCharacter])
ToCharacter_2nd = TypeAliasType("ToCharacter_2nd", _ToArray2_2nd[_ToCharacter, _PyCharacter])
ToCharacter_3nd = TypeAliasType("ToCharacter_3nd", _ToArray2_3nd[_ToCharacter, _PyCharacter])

# python object
ToObject_nd = TypeAliasType("ToObject_nd", _ToArray2_nd[np.object_, _PyObject])
ToObject_0d = TypeAliasType("ToObject_0d", _ToArray2_0d[np.object_, _PyObject])
ToObject_1d = TypeAliasType("ToObject_1d", _ToArray2_1d[np.object_, _PyObject])
ToObject_2d = TypeAliasType("ToObject_2d", _ToArray2_2d[np.object_, _PyObject])
ToObject_3d = TypeAliasType("ToObject_3d", _ToArray2_3d[np.object_, _PyObject])
ToObject_1ds = TypeAliasType("ToObject_1ds", _ToArray2_1ds[np.object_, _PyObject])
ToObject_2ds = TypeAliasType("ToObject_2ds", _ToArray2_2ds[np.object_, _PyObject])
ToObject_3ds = TypeAliasType("ToObject_3ds", _ToArray2_3ds[np.object_, _PyObject])
ToObject_1nd = TypeAliasType("ToObject_1nd", _ToArray2_1nd[np.object_, _PyObject])
ToObject_2nd = TypeAliasType("ToObject_2nd", _ToArray2_2nd[np.object_, _PyObject])
ToObject_3nd = TypeAliasType("ToObject_3nd", _ToArray2_3nd[np.object_, _PyObject])

# StringDType
ToString_nd = TypeAliasType("ToString_nd", _CanStringArray[AtLeast0D, _NaT0], type_params=(_NaT0,))
ToString_1ds = TypeAliasType("ToString_1ds", _CanStringArray[tuple[int], _NaT0], type_params=(_NaT0,))
ToString_2ds = TypeAliasType("ToString_2ds", _CanStringArray[tuple[int, int], _NaT0], type_params=(_NaT0,))
ToString_3ds = TypeAliasType("ToString_3ds", _CanStringArray[tuple[int, int, int], _NaT0], type_params=(_NaT0,))
ToString_1nd = TypeAliasType("ToString_1nd", _CanStringArray[AtLeast1D, _NaT0], type_params=(_NaT0,))
ToString_2nd = TypeAliasType("ToString_2nd", _CanStringArray[AtLeast2D, _NaT0], type_params=(_NaT0,))
ToString_3nd = TypeAliasType("ToString_3nd", _CanStringArray[AtLeast3D, _NaT0], type_params=(_NaT0,))

# any scalar
ToGeneric_nd = TypeAliasType("ToGeneric_nd", _ToArray2_nd[np.generic, _PyScalar])
ToGeneric_0d = TypeAliasType("ToGeneric_0d", _ToArray2_0d[np.generic, _PyScalar])
ToGeneric_1d = TypeAliasType("ToGeneric_1d", _ToArray2_1d[np.generic, _PyScalar])
ToGeneric_2d = TypeAliasType("ToGeneric_2d", _ToArray2_2d[np.generic, _PyScalar])
ToGeneric_3d = TypeAliasType("ToGeneric_3d", _ToArray2_3d[np.generic, _PyScalar])
ToGeneric_1ds = TypeAliasType("ToGeneric_1ds", _ToArray2_1ds[np.generic, _PyScalar])
ToGeneric_2ds = TypeAliasType("ToGeneric_2ds", _ToArray2_2ds[np.generic, _PyScalar])
ToGeneric_3ds = TypeAliasType("ToGeneric_3ds", _ToArray2_3ds[np.generic, _PyScalar])
ToGeneric_1nd = TypeAliasType("ToGeneric_1nd", _ToArray2_1nd[np.generic, _PyScalar])
ToGeneric_2nd = TypeAliasType("ToGeneric_2nd", _ToArray2_2nd[np.generic, _PyScalar])
ToGeneric_3nd = TypeAliasType("ToGeneric_3nd", _ToArray2_3nd[np.generic, _PyScalar])

# unsigned integers
CoUInt8_nd = TypeAliasType("CoUInt8_nd", _ToArray2_nd[co_uint8, bool])
CoUInt8_0d = TypeAliasType("CoUInt8_0d", _ToArray2_0d[co_uint8, bool])
CoUInt8_1d = TypeAliasType("CoUInt8_1d", _ToArray2_1d[co_uint8, bool])
CoUInt8_2d = TypeAliasType("CoUInt8_2d", _ToArray2_2d[co_uint8, bool])
CoUInt8_3d = TypeAliasType("CoUInt8_3d", _ToArray2_3d[co_uint8, bool])
CoUInt8_1ds = TypeAliasType("CoUInt8_1ds", _ToArray2_1ds[co_uint8, bool])
CoUInt8_2ds = TypeAliasType("CoUInt8_2ds", _ToArray2_2ds[co_uint8, bool])
CoUInt8_3ds = TypeAliasType("CoUInt8_3ds", _ToArray2_3ds[co_uint8, bool])
CoUInt8_1nd = TypeAliasType("CoUInt8_1nd", _ToArray2_1nd[co_uint8, bool])
CoUInt8_2nd = TypeAliasType("CoUInt8_2nd", _ToArray2_2nd[co_uint8, bool])
CoUInt8_3nd = TypeAliasType("CoUInt8_3nd", _ToArray2_3nd[co_uint8, bool])

CoUInt16_nd = TypeAliasType("CoUInt16_nd", _ToArray2_nd[co_uint16, bool])
CoUInt16_0d = TypeAliasType("CoUInt16_0d", _ToArray2_0d[co_uint16, bool])
CoUInt16_1d = TypeAliasType("CoUInt16_1d", _ToArray2_1d[co_uint16, bool])
CoUInt16_2d = TypeAliasType("CoUInt16_2d", _ToArray2_2d[co_uint16, bool])
CoUInt16_3d = TypeAliasType("CoUInt16_3d", _ToArray2_3d[co_uint16, bool])
CoUInt16_1ds = TypeAliasType("CoUInt16_1ds", _ToArray2_1ds[co_uint16, bool])
CoUInt16_2ds = TypeAliasType("CoUInt16_2ds", _ToArray2_2ds[co_uint16, bool])
CoUInt16_3ds = TypeAliasType("CoUInt16_3ds", _ToArray2_3ds[co_uint16, bool])
CoUInt16_1nd = TypeAliasType("CoUInt16_1nd", _ToArray2_1nd[co_uint16, bool])
CoUInt16_2nd = TypeAliasType("CoUInt16_2nd", _ToArray2_2nd[co_uint16, bool])
CoUInt16_3nd = TypeAliasType("CoUInt16_3nd", _ToArray2_3nd[co_uint16, bool])

CoUInt32_nd = TypeAliasType("CoUInt32_nd", _ToArray2_nd[co_uint32, bool])
CoUInt32_0d = TypeAliasType("CoUInt32_0d", _ToArray2_0d[co_uint32, bool])
CoUInt32_1d = TypeAliasType("CoUInt32_1d", _ToArray2_1d[co_uint32, bool])
CoUInt32_2d = TypeAliasType("CoUInt32_2d", _ToArray2_2d[co_uint32, bool])
CoUInt32_3d = TypeAliasType("CoUInt32_3d", _ToArray2_3d[co_uint32, bool])
CoUInt32_1ds = TypeAliasType("CoUInt32_1ds", _ToArray2_1ds[co_uint32, bool])
CoUInt32_2ds = TypeAliasType("CoUInt32_2ds", _ToArray2_2ds[co_uint32, bool])
CoUInt32_3ds = TypeAliasType("CoUInt32_3ds", _ToArray2_3ds[co_uint32, bool])
CoUInt32_1nd = TypeAliasType("CoUInt32_1nd", _ToArray2_1nd[co_uint32, bool])
CoUInt32_2nd = TypeAliasType("CoUInt32_2nd", _ToArray2_2nd[co_uint32, bool])
CoUInt32_3nd = TypeAliasType("CoUInt32_3nd", _ToArray2_3nd[co_uint32, bool])

CoULong_nd = TypeAliasType("CoULong_nd", _ToArray2_nd[co_ulong, bool])
CoULong_0d = TypeAliasType("CoULong_0d", _ToArray2_0d[co_ulong, bool])
CoULong_1d = TypeAliasType("CoULong_1d", _ToArray2_1d[co_ulong, bool])
CoULong_2d = TypeAliasType("CoULong_2d", _ToArray2_2d[co_ulong, bool])
CoULong_3d = TypeAliasType("CoULong_3d", _ToArray2_3d[co_ulong, bool])
CoULong_1ds = TypeAliasType("CoULong_1ds", _ToArray2_1ds[co_ulong, bool])
CoULong_2ds = TypeAliasType("CoULong_2ds", _ToArray2_2ds[co_ulong, bool])
CoULong_3ds = TypeAliasType("CoULong_3ds", _ToArray2_3ds[co_ulong, bool])
CoULong_1nd = TypeAliasType("CoULong_1nd", _ToArray2_1nd[co_ulong, bool])
CoULong_2nd = TypeAliasType("CoULong_2nd", _ToArray2_2nd[co_ulong, bool])
CoULong_3nd = TypeAliasType("CoULong_3nd", _ToArray2_3nd[co_ulong, bool])

CoUInt64_nd = TypeAliasType("CoUInt64_nd", _ToArray2_nd[co_uint64, bool])
CoUInt64_0d = TypeAliasType("CoUInt64_0d", _ToArray2_0d[co_uint64, bool])
CoUInt64_1d = TypeAliasType("CoUInt64_1d", _ToArray2_1d[co_uint64, bool])
CoUInt64_2d = TypeAliasType("CoUInt64_2d", _ToArray2_2d[co_uint64, bool])
CoUInt64_3d = TypeAliasType("CoUInt64_3d", _ToArray2_3d[co_uint64, bool])
CoUInt64_1ds = TypeAliasType("CoUInt64_1ds", _ToArray2_1ds[co_uint64, bool])
CoUInt64_2ds = TypeAliasType("CoUInt64_2ds", _ToArray2_2ds[co_uint64, bool])
CoUInt64_3ds = TypeAliasType("CoUInt64_3ds", _ToArray2_3ds[co_uint64, bool])
CoUInt64_1nd = TypeAliasType("CoUInt64_1nd", _ToArray2_1nd[co_uint64, bool])
CoUInt64_2nd = TypeAliasType("CoUInt64_2nd", _ToArray2_2nd[co_uint64, bool])
CoUInt64_3nd = TypeAliasType("CoUInt64_3nd", _ToArray2_3nd[co_uint64, bool])

# signed integers
CoInt8_nd = TypeAliasType("CoInt8_nd", _ToArray2_nd[co_int8, bool])
CoInt8_0d = TypeAliasType("CoInt8_0d", _ToArray2_0d[co_int8, bool])
CoInt8_1d = TypeAliasType("CoInt8_1d", _ToArray2_1d[co_int8, bool])
CoInt8_2d = TypeAliasType("CoInt8_2d", _ToArray2_2d[co_int8, bool])
CoInt8_3d = TypeAliasType("CoInt8_3d", _ToArray2_3d[co_int8, bool])
CoInt8_1ds = TypeAliasType("CoInt8_1ds", _ToArray2_1ds[co_int8, bool])
CoInt8_2ds = TypeAliasType("CoInt8_2ds", _ToArray2_2ds[co_int8, bool])
CoInt8_3ds = TypeAliasType("CoInt8_3ds", _ToArray2_3ds[co_int8, bool])
CoInt8_1nd = TypeAliasType("CoInt8_1nd", _ToArray2_1nd[co_int8, bool])
CoInt8_2nd = TypeAliasType("CoInt8_2nd", _ToArray2_2nd[co_int8, bool])
CoInt8_3nd = TypeAliasType("CoInt8_3nd", _ToArray2_3nd[co_int8, bool])

CoInt16_nd = TypeAliasType("CoInt16_nd", _ToArray2_nd[co_int16, bool])
CoInt16_0d = TypeAliasType("CoInt16_0d", _ToArray2_0d[co_int16, bool])
CoInt16_1d = TypeAliasType("CoInt16_1d", _ToArray2_1d[co_int16, bool])
CoInt16_2d = TypeAliasType("CoInt16_2d", _ToArray2_2d[co_int16, bool])
CoInt16_3d = TypeAliasType("CoInt16_3d", _ToArray2_3d[co_int16, bool])
CoInt16_1ds = TypeAliasType("CoInt16_1ds", _ToArray2_1ds[co_int16, bool])
CoInt16_2ds = TypeAliasType("CoInt16_2ds", _ToArray2_2ds[co_int16, bool])
CoInt16_3ds = TypeAliasType("CoInt16_3ds", _ToArray2_3ds[co_int16, bool])
CoInt16_1nd = TypeAliasType("CoInt16_1nd", _ToArray2_1nd[co_int16, bool])
CoInt16_2nd = TypeAliasType("CoInt16_2nd", _ToArray2_2nd[co_int16, bool])
CoInt16_3nd = TypeAliasType("CoInt16_3nd", _ToArray2_3nd[co_int16, bool])

CoInt32_nd = TypeAliasType("CoInt32_nd", _ToArray2_nd[co_int32, bool])
CoInt32_0d = TypeAliasType("CoInt32_0d", _ToArray2_0d[co_int32, bool])
CoInt32_1d = TypeAliasType("CoInt32_1d", _ToArray2_1d[co_int32, bool])
CoInt32_2d = TypeAliasType("CoInt32_2d", _ToArray2_2d[co_int32, bool])
CoInt32_3d = TypeAliasType("CoInt32_3d", _ToArray2_3d[co_int32, bool])
CoInt32_1ds = TypeAliasType("CoInt32_1ds", _ToArray2_1ds[co_int32, bool])
CoInt32_2ds = TypeAliasType("CoInt32_2ds", _ToArray2_2ds[co_int32, bool])
CoInt32_3ds = TypeAliasType("CoInt32_3ds", _ToArray2_3ds[co_int32, bool])
CoInt32_1nd = TypeAliasType("CoInt32_1nd", _ToArray2_1nd[co_int32, bool])
CoInt32_2nd = TypeAliasType("CoInt32_2nd", _ToArray2_2nd[co_int32, bool])
CoInt32_3nd = TypeAliasType("CoInt32_3nd", _ToArray2_3nd[co_int32, bool])

CoLong_nd = TypeAliasType("CoLong_nd", _ToArray2_nd[co_long, bool])
CoLong_0d = TypeAliasType("CoLong_0d", _ToArray2_0d[co_long, bool])
CoLong_1d = TypeAliasType("CoLong_1d", _ToArray2_1d[co_long, bool])
CoLong_2d = TypeAliasType("CoLong_2d", _ToArray2_2d[co_long, bool])
CoLong_3d = TypeAliasType("CoLong_3d", _ToArray2_3d[co_long, bool])
CoLong_1ds = TypeAliasType("CoLong_1ds", _ToArray2_1ds[co_long, bool])
CoLong_2ds = TypeAliasType("CoLong_2ds", _ToArray2_2ds[co_long, bool])
CoLong_3ds = TypeAliasType("CoLong_3ds", _ToArray2_3ds[co_long, bool])
CoLong_1nd = TypeAliasType("CoLong_1nd", _ToArray2_1nd[co_long, bool])
CoLong_2nd = TypeAliasType("CoLong_2nd", _ToArray2_2nd[co_long, bool])
CoLong_3nd = TypeAliasType("CoLong_3nd", _ToArray2_3nd[co_long, bool])

CoInt64_nd = TypeAliasType("CoInt64_nd", _ToArray2_nd[co_int64, int])
CoInt64_0d = TypeAliasType("CoInt64_0d", _ToArray2_0d[co_int64, int])
CoInt64_1d = TypeAliasType("CoInt64_1d", _ToArray2_1d[co_int64, int])
CoInt64_2d = TypeAliasType("CoInt64_2d", _ToArray2_2d[co_int64, int])
CoInt64_3d = TypeAliasType("CoInt64_3d", _ToArray2_3d[co_int64, int])
CoInt64_1ds = TypeAliasType("CoInt64_1ds", _ToArray2_1ds[co_int64, int])
CoInt64_2ds = TypeAliasType("CoInt64_2ds", _ToArray2_2ds[co_int64, int])
CoInt64_3ds = TypeAliasType("CoInt64_3ds", _ToArray2_3ds[co_int64, int])
CoInt64_1nd = TypeAliasType("CoInt64_1nd", _ToArray2_1nd[co_int64, int])
CoInt64_2nd = TypeAliasType("CoInt64_2nd", _ToArray2_2nd[co_int64, int])
CoInt64_3nd = TypeAliasType("CoInt64_3nd", _ToArray2_3nd[co_int64, int])

CoInteger_nd = TypeAliasType("CoInteger_nd", _ToArray2_nd[co_integer, int])
CoInteger_0d = TypeAliasType("CoInteger_0d", _ToArray2_0d[co_integer, int])
CoInteger_1d = TypeAliasType("CoInteger_1d", _ToArray2_1d[co_integer, int])
CoInteger_2d = TypeAliasType("CoInteger_2d", _ToArray2_2d[co_integer, int])
CoInteger_3d = TypeAliasType("CoInteger_3d", _ToArray2_3d[co_integer, int])
CoInteger_1ds = TypeAliasType("CoInteger_1ds", _ToArray2_1ds[co_integer, int])
CoInteger_2ds = TypeAliasType("CoInteger_2ds", _ToArray2_2ds[co_integer, int])
CoInteger_3ds = TypeAliasType("CoInteger_3ds", _ToArray2_3ds[co_integer, int])
CoInteger_1nd = TypeAliasType("CoInteger_1nd", _ToArray2_1nd[co_integer, int])
CoInteger_2nd = TypeAliasType("CoInteger_2nd", _ToArray2_2nd[co_integer, int])
CoInteger_3nd = TypeAliasType("CoInteger_3nd", _ToArray2_3nd[co_integer, int])

# real floats

CoFloat16_nd = TypeAliasType("CoFloat16_nd", _ToArray2_nd[co_float16, bool])
CoFloat16_0d = TypeAliasType("CoFloat16_0d", _ToArray2_0d[co_float16, bool])
CoFloat16_1d = TypeAliasType("CoFloat16_1d", _ToArray2_1d[co_float16, bool])
CoFloat16_2d = TypeAliasType("CoFloat16_2d", _ToArray2_2d[co_float16, bool])
CoFloat16_3d = TypeAliasType("CoFloat16_3d", _ToArray2_3d[co_float16, bool])
CoFloat16_1ds = TypeAliasType("CoFloat16_1ds", _ToArray2_1ds[co_float16, bool])
CoFloat16_2ds = TypeAliasType("CoFloat16_2ds", _ToArray2_2ds[co_float16, bool])
CoFloat16_3ds = TypeAliasType("CoFloat16_3ds", _ToArray2_3ds[co_float16, bool])
CoFloat16_1nd = TypeAliasType("CoFloat16_1nd", _ToArray2_1nd[co_float16, bool])
CoFloat16_2nd = TypeAliasType("CoFloat16_2nd", _ToArray2_2nd[co_float16, bool])
CoFloat16_3nd = TypeAliasType("CoFloat16_3nd", _ToArray2_3nd[co_float16, bool])

CoFloat32_nd = TypeAliasType("CoFloat32_nd", _ToArray2_nd[co_float32, bool])
CoFloat32_0d = TypeAliasType("CoFloat32_0d", _ToArray2_0d[co_float32, bool])
CoFloat32_1d = TypeAliasType("CoFloat32_1d", _ToArray2_1d[co_float32, bool])
CoFloat32_2d = TypeAliasType("CoFloat32_2d", _ToArray2_2d[co_float32, bool])
CoFloat32_3d = TypeAliasType("CoFloat32_3d", _ToArray2_3d[co_float32, bool])
CoFloat32_1ds = TypeAliasType("CoFloat32_1ds", _ToArray2_1ds[co_float32, bool])
CoFloat32_2ds = TypeAliasType("CoFloat32_2ds", _ToArray2_2ds[co_float32, bool])
CoFloat32_3ds = TypeAliasType("CoFloat32_3ds", _ToArray2_3ds[co_float32, bool])
CoFloat32_1nd = TypeAliasType("CoFloat32_1nd", _ToArray2_1nd[co_float32, bool])
CoFloat32_2nd = TypeAliasType("CoFloat32_2nd", _ToArray2_2nd[co_float32, bool])
CoFloat32_3nd = TypeAliasType("CoFloat32_3nd", _ToArray2_3nd[co_float32, bool])

CoFloat64_nd = TypeAliasType("CoFloat64_nd", _ToArray2_nd[co_float64, float])
CoFloat64_0d = TypeAliasType("CoFloat64_0d", _ToArray2_0d[co_float64, float])
CoFloat64_1d = TypeAliasType("CoFloat64_1d", _ToArray2_1d[co_float64, float])
CoFloat64_2d = TypeAliasType("CoFloat64_2d", _ToArray2_2d[co_float64, float])
CoFloat64_3d = TypeAliasType("CoFloat64_3d", _ToArray2_3d[co_float64, float])
CoFloat64_1ds = TypeAliasType("CoFloat64_1ds", _ToArray2_1ds[co_float64, float])
CoFloat64_2ds = TypeAliasType("CoFloat64_2ds", _ToArray2_2ds[co_float64, float])
CoFloat64_3ds = TypeAliasType("CoFloat64_3ds", _ToArray2_3ds[co_float64, float])
CoFloat64_1nd = TypeAliasType("CoFloat64_1nd", _ToArray2_1nd[co_float64, float])
CoFloat64_2nd = TypeAliasType("CoFloat64_2nd", _ToArray2_2nd[co_float64, float])
CoFloat64_3nd = TypeAliasType("CoFloat64_3nd", _ToArray2_3nd[co_float64, float])

CoFloating_nd = TypeAliasType("CoFloating_nd", _ToArray2_nd[co_float, float])
CoFloating_0d = TypeAliasType("CoFloating_0d", _ToArray2_0d[co_float, float])
CoFloating_1d = TypeAliasType("CoFloating_1d", _ToArray2_1d[co_float, float])
CoFloating_2d = TypeAliasType("CoFloating_2d", _ToArray2_2d[co_float, float])
CoFloating_3d = TypeAliasType("CoFloating_3d", _ToArray2_3d[co_float, float])
CoFloating_1ds = TypeAliasType("CoFloating_1ds", _ToArray2_1ds[co_float, float])
CoFloating_2ds = TypeAliasType("CoFloating_2ds", _ToArray2_2ds[co_float, float])
CoFloating_3ds = TypeAliasType("CoFloating_3ds", _ToArray2_3ds[co_float, float])
CoFloating_1nd = TypeAliasType("CoFloating_1nd", _ToArray2_1nd[co_float, float])
CoFloating_2nd = TypeAliasType("CoFloating_2nd", _ToArray2_2nd[co_float, float])
CoFloating_3nd = TypeAliasType("CoFloating_3nd", _ToArray2_3nd[co_float, float])

# complex floats
CoComplex64_nd = TypeAliasType("CoComplex64_nd", _ToArray2_nd[co_complex64, bool])
CoComplex64_0d = TypeAliasType("CoComplex64_0d", _ToArray2_0d[co_complex64, bool])
CoComplex64_1d = TypeAliasType("CoComplex64_1d", _ToArray2_1d[co_complex64, bool])
CoComplex64_2d = TypeAliasType("CoComplex64_2d", _ToArray2_2d[co_complex64, bool])
CoComplex64_3d = TypeAliasType("CoComplex64_3d", _ToArray2_3d[co_complex64, bool])
CoComplex64_1ds = TypeAliasType("CoComplex64_1ds", _ToArray2_1ds[co_complex64, bool])
CoComplex64_2ds = TypeAliasType("CoComplex64_2ds", _ToArray2_2ds[co_complex64, bool])
CoComplex64_3ds = TypeAliasType("CoComplex64_3ds", _ToArray2_3ds[co_complex64, bool])
CoComplex64_1nd = TypeAliasType("CoComplex64_1nd", _ToArray2_1nd[co_complex64, bool])
CoComplex64_2nd = TypeAliasType("CoComplex64_2nd", _ToArray2_2nd[co_complex64, bool])
CoComplex64_3nd = TypeAliasType("CoComplex64_3nd", _ToArray2_3nd[co_complex64, bool])

CoComplex128_nd = TypeAliasType("CoComplex128_nd", _ToArray2_nd[co_complex128, complex])
CoComplex128_0d = TypeAliasType("CoComplex128_0d", _ToArray2_0d[co_complex128, complex])
CoComplex128_1d = TypeAliasType("CoComplex128_1d", _ToArray2_1d[co_complex128, complex])
CoComplex128_2d = TypeAliasType("CoComplex128_2d", _ToArray2_2d[co_complex128, complex])
CoComplex128_3d = TypeAliasType("CoComplex128_3d", _ToArray2_3d[co_complex128, complex])
CoComplex128_1ds = TypeAliasType("CoComplex128_1ds", _ToArray2_1ds[co_complex128, complex])
CoComplex128_2ds = TypeAliasType("CoComplex128_2ds", _ToArray2_2ds[co_complex128, complex])
CoComplex128_3ds = TypeAliasType("CoComplex128_3ds", _ToArray2_3ds[co_complex128, complex])
CoComplex128_1nd = TypeAliasType("CoComplex128_1nd", _ToArray2_1nd[co_complex128, complex])
CoComplex128_2nd = TypeAliasType("CoComplex128_2nd", _ToArray2_2nd[co_complex128, complex])
CoComplex128_3nd = TypeAliasType("CoComplex128_3nd", _ToArray2_3nd[co_complex128, complex])

CoComplex_nd = TypeAliasType("CoComplex_nd", _ToArray2_nd[co_complex, complex])
CoComplex_0d = TypeAliasType("CoComplex_0d", _ToArray2_0d[co_complex, complex])
CoComplex_1d = TypeAliasType("CoComplex_1d", _ToArray2_1d[co_complex, complex])
CoComplex_2d = TypeAliasType("CoComplex_2d", _ToArray2_2d[co_complex, complex])
CoComplex_3d = TypeAliasType("CoComplex_3d", _ToArray2_3d[co_complex, complex])
CoComplex_1ds = TypeAliasType("CoComplex_1ds", _ToArray2_1ds[co_complex, complex])
CoComplex_2ds = TypeAliasType("CoComplex_2ds", _ToArray2_2ds[co_complex, complex])
CoComplex_3ds = TypeAliasType("CoComplex_3ds", _ToArray2_3ds[co_complex, complex])
CoComplex_1nd = TypeAliasType("CoComplex_1nd", _ToArray2_1nd[co_complex, complex])
CoComplex_2nd = TypeAliasType("CoComplex_2nd", _ToArray2_2nd[co_complex, complex])
CoComplex_3nd = TypeAliasType("CoComplex_3nd", _ToArray2_3nd[co_complex, complex])

# temporal
CoTimeDelta_nd = TypeAliasType("CoTimeDelta_nd", _ToArray2_nd[co_timedelta, int])
CoTimeDelta_0d = TypeAliasType("CoTimeDelta_0d", _ToArray2_0d[co_timedelta, int])
CoTimeDelta_1d = TypeAliasType("CoTimeDelta_1d", _ToArray2_1d[co_timedelta, int])
CoTimeDelta_2d = TypeAliasType("CoTimeDelta_2d", _ToArray2_2d[co_timedelta, int])
CoTimeDelta_3d = TypeAliasType("CoTimeDelta_3d", _ToArray2_3d[co_timedelta, int])
CoTimeDelta_1ds = TypeAliasType("CoTimeDelta_1ds", _ToArray2_1ds[co_timedelta, int])
CoTimeDelta_2ds = TypeAliasType("CoTimeDelta_2ds", _ToArray2_2ds[co_timedelta, int])
CoTimeDelta_3ds = TypeAliasType("CoTimeDelta_3ds", _ToArray2_3ds[co_timedelta, int])
CoTimeDelta_1nd = TypeAliasType("CoTimeDelta_1nd", _ToArray2_1nd[co_timedelta, int])
CoTimeDelta_2nd = TypeAliasType("CoTimeDelta_2nd", _ToArray2_2nd[co_timedelta, int])
CoTimeDelta_3nd = TypeAliasType("CoTimeDelta_3nd", _ToArray2_3nd[co_timedelta, int])

CoDateTime_nd = TypeAliasType("CoDateTime_nd", _ToArray_nd[co_datetime])
CoDateTime_0d = TypeAliasType("CoDateTime_0d", CanArray0D[co_datetime])
CoDateTime_1d = TypeAliasType("CoDateTime_1d", _ToArray_1d[co_datetime])
CoDateTime_2d = TypeAliasType("CoDateTime_2d", _ToArray_2d[co_datetime])
CoDateTime_3d = TypeAliasType("CoDateTime_3d", _ToArray_3d[co_datetime])
CoDateTime_1ds = TypeAliasType("CoDateTime_1ds", _ToArray_1ds[co_datetime])
CoDateTime_2ds = TypeAliasType("CoDateTime_2ds", _ToArray_2ds[co_datetime])
CoDateTime_3ds = TypeAliasType("CoDateTime_3ds", _ToArray_3ds[co_datetime])
CoDateTime_1nd = TypeAliasType("CoDateTime_1nd", _ToArray_1nd[co_datetime])
CoDateTime_2nd = TypeAliasType("CoDateTime_2nd", _ToArray_2nd[co_datetime])
CoDateTime_3nd = TypeAliasType("CoDateTime_3nd", _ToArray_3nd[co_datetime])

# fixed strings
CoBytes_nd = TypeAliasType("CoBytes_nd", _ToArray2_nd[_ToBytes, JustBytes])
CoBytes_0d = TypeAliasType("CoBytes_0d", _ToArray2_0d[_ToBytes, JustBytes])
CoBytes_1d = TypeAliasType("CoBytes_1d", _ToArray2_1d[_ToBytes, JustBytes])
CoBytes_2d = TypeAliasType("CoBytes_2d", _ToArray2_2d[_ToBytes, JustBytes])
CoBytes_3d = TypeAliasType("CoBytes_3d", _ToArray2_3d[_ToBytes, JustBytes])
CoBytes_1ds = TypeAliasType("CoBytes_1ds", _ToArray2_1ds[_ToBytes, JustBytes])
CoBytes_2ds = TypeAliasType("CoBytes_2ds", _ToArray2_2ds[_ToBytes, JustBytes])
CoBytes_3ds = TypeAliasType("CoBytes_3ds", _ToArray2_3ds[_ToBytes, JustBytes])
CoBytes_1nd = TypeAliasType("CoBytes_1nd", _ToArray2_1nd[_ToBytes, JustBytes])
CoBytes_2nd = TypeAliasType("CoBytes_2nd", _ToArray2_2nd[_ToBytes, JustBytes])
CoBytes_3nd = TypeAliasType("CoBytes_3nd", _ToArray2_3nd[_ToBytes, JustBytes])

CoStr_nd = TypeAliasType("CoStr_nd", _ToArray2_nd[_ToCharacter, _PyCharacter])
CoStr_0d = TypeAliasType("CoStr_0d", _ToArray2_0d[_ToCharacter, _PyCharacter])
CoStr_1d = TypeAliasType("CoStr_1d", _ToArray2_1d[_ToCharacter, _PyCharacter])
CoStr_2d = TypeAliasType("CoStr_2d", _ToArray2_2d[_ToCharacter, _PyCharacter])
CoStr_3d = TypeAliasType("CoStr_3d", _ToArray2_3d[_ToCharacter, _PyCharacter])
CoStr_1ds = TypeAliasType("CoStr_1ds", _ToArray2_1ds[_ToCharacter, _PyCharacter])
CoStr_2ds = TypeAliasType("CoStr_2ds", _ToArray2_2ds[_ToCharacter, _PyCharacter])
CoStr_3ds = TypeAliasType("CoStr_3ds", _ToArray2_3ds[_ToCharacter, _PyCharacter])
CoStr_1nd = TypeAliasType("CoStr_1nd", _ToArray2_1nd[_ToCharacter, _PyCharacter])
CoStr_2nd = TypeAliasType("CoStr_2nd", _ToArray2_2nd[_ToCharacter, _PyCharacter])
CoStr_3nd = TypeAliasType("CoStr_3nd", _ToArray2_3nd[_ToCharacter, _PyCharacter])

###
# DType-likes
# TODO(jorenham): see
# https://github.com/numpy/numtype/issues/304
