# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
import datetime as dt
import decimal
import fractions
import ipaddress as ip
import uuid
from collections.abc import Sequence
from typing import Any, ClassVar, TypeAlias, final, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy._typing import _64Bit

###
# Type parameters

_T = TypeVar("_T", default=Any)
_T_co = TypeVar("_T_co", covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)
_ToT = TypeVar("_ToT", default=_ScalarT)

###
# Type constraints (bijective type mappings)

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...], default=tuple[int, ...])

ItemC = TypeVar(  # noqa: PYI001
    "ItemC",
    bool,
    int,
    float,
    complex,
    bytes,
    str,
    bytes | str,
    complex | bytes | str,  # includes int and float (promotion)
    default=complex | bytes | str,
)

###
# Protocols

@type_check_only
class CanArray(Protocol[_ScalarT_co, _ShapeT_co]):
    def __array__(self, /) -> np.ndarray[_ShapeT_co, np.dtype[_ScalarT_co]]: ...

# A shape-typed version of `numpy._typing._Can`, parametrized by the
# scalar-type and shape-type, and excludes `np.generic` scalars (through `__len__`).
@type_check_only
class CanArraySized(CanArray[_ScalarT_co, _ShapeT_co], Protocol[_ScalarT_co, _ShapeT_co]):
    def __len__(self, /) -> int: ...

# A slimmed down version of `_NestedSequence`, based on `optype.numpy.SequenceND`.
# https://github.com/jorenham/optype
@type_check_only
class NDSequence(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | NDSequence[_T_co]: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

# Type-check-only equivalent of `optype.Just`.
# https://github.com/jorenham/optype#just
@type_check_only
@final
class Is(Protocol[_T]):
    @property  # type: ignore[override]
    def __class__(self, /) -> type[_T]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @__class__.setter
    def __class__(self, t: type[_T], /) -> None: ...

@type_check_only
class Unhashable(Protocol):
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

###
# Shape aliases

Shape: TypeAlias = tuple[int, ...]

Shape_l1d = TypeAliasType("Shape_l1d", tuple[int] | tuple[()])
Shape_l2d = TypeAliasType("Shape_l2d", tuple[int, int] | tuple[int] | tuple[()])
Shape_l3d = TypeAliasType("Shape_l3d", tuple[int, int, int] | tuple[int, int] | tuple[int] | tuple[()])

Shape_g1d = TypeAliasType("Shape_g1d", tuple[int, Unpack[tuple[int, ...]]])
Shape_g2d = TypeAliasType("Shape_g2d", tuple[int, int, Unpack[tuple[int, ...]]])
Shape_g3d = TypeAliasType("Shape_g3d", tuple[int, int, int, Unpack[tuple[int, ...]]])
Shape_g4d = TypeAliasType("Shape_g4d", tuple[int, int, int, int, Unpack[tuple[int, ...]]])

###
# Shape-typed array aliases

Array = TypeAliasType("Array", np.ndarray[_ShapeT, np.dtype[_ScalarT]], type_params=(_ScalarT, _ShapeT))
Array_0d = TypeAliasType("Array_0d", np.ndarray[tuple[()], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_1d = TypeAliasType("Array_1d", np.ndarray[tuple[int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_2d = TypeAliasType("Array_2d", np.ndarray[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_3d = TypeAliasType("Array_3d", np.ndarray[tuple[int, int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

MArray = TypeAliasType("MArray", np.ma.MaskedArray[_ShapeT, np.dtype[_ScalarT]], type_params=(_ScalarT, _ShapeT))
MArray_0d = TypeAliasType("MArray_0d", np.ma.MaskedArray[tuple[()], np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray_1d = TypeAliasType("MArray_1d", np.ma.MaskedArray[tuple[int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray_2d = TypeAliasType("MArray_2d", np.ma.MaskedArray[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray_3d = TypeAliasType("MArray_3d", np.ma.MaskedArray[tuple[int, int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

Matrix = TypeAliasType("Matrix", np.matrix[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

###
# helper aliases

_PyReal: TypeAlias = Is[int] | Is[float]
_PyInexact: TypeAlias = Is[float] | Is[complex]
_PyNumber: TypeAlias = Is[int] | _PyInexact
_PyCharacter: TypeAlias = Is[bytes] | Is[str]
_PyObject: TypeAlias = (  # anything immutable that results in an `object_` dtype
    Is[object]
    | type
    | slice
    | dt.tzinfo
    | dt.time
    | decimal.Decimal
    | fractions.Fraction
    | uuid.UUID
    | ip.IPv4Address
    | ip.IPv6Address
)

_ToArray_0d = TypeAliasType("_ToArray_0d", _ToT | CanArray[_ScalarT, tuple[()]], type_params=(_ScalarT, _ToT))
_ToArray_1d: TypeAlias = CanArraySized[_ScalarT, tuple[int]] | Sequence[_ToArray_0d[_ScalarT, _ToT]]
_ToArray_2d: TypeAlias = CanArraySized[_ScalarT, tuple[int, int]] | Sequence[_ToArray_1d[_ScalarT, _ToT]]
_ToArray_3d: TypeAlias = CanArraySized[_ScalarT, tuple[int, int, int]] | Sequence[_ToArray_2d[_ScalarT, _ToT]]
_ToArray_nd: TypeAlias = CanArraySized[_ScalarT] | NDSequence[_ToT | CanArray[_ScalarT]]

###
# Non-overlapping scalar- and array-like aliases for all scalar types.

# bool
_ToBool: TypeAlias = np.bool[Any]
ToBool_0d = TypeAliasType("ToBool_0d", _ToArray_0d[_ToBool, bool])
ToBool_1d = TypeAliasType("ToBool_1d", _ToArray_1d[_ToBool, bool])
ToBool_2d = TypeAliasType("ToBool_2d", _ToArray_2d[_ToBool, bool])
ToBool_3d = TypeAliasType("ToBool_3d", _ToArray_3d[_ToBool, bool])
ToBool_nd = TypeAliasType("ToBool_nd", _ToArray_nd[_ToBool, bool])

# unsigned integers
ToUInt8_0d = TypeAliasType("ToUInt8_0d", _ToArray_0d[np.uint8])
ToUInt8_1d = TypeAliasType("ToUInt8_1d", _ToArray_1d[np.uint8])
ToUInt8_2d = TypeAliasType("ToUInt8_2d", _ToArray_2d[np.uint8])
ToUInt8_3d = TypeAliasType("ToUInt8_3d", _ToArray_3d[np.uint8])
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _ToArray_nd[np.uint8])

ToUInt16_0d = TypeAliasType("ToUInt16_0d", _ToArray_0d[np.uint16])
ToUInt16_1d = TypeAliasType("ToUInt16_1d", _ToArray_1d[np.uint16])
ToUInt16_2d = TypeAliasType("ToUInt16_2d", _ToArray_2d[np.uint16])
ToUInt16_3d = TypeAliasType("ToUInt16_3d", _ToArray_3d[np.uint16])
ToUInt16_nd = TypeAliasType("ToUInt16_nd", _ToArray_nd[np.uint16])

ToUInt32_0d = TypeAliasType("ToUInt32_0d", _ToArray_0d[np.uint32])
ToUInt32_1d = TypeAliasType("ToUInt32_1d", _ToArray_1d[np.uint32])
ToUInt32_2d = TypeAliasType("ToUInt32_2d", _ToArray_2d[np.uint32])
ToUInt32_3d = TypeAliasType("ToUInt32_3d", _ToArray_3d[np.uint32])
ToUInt32_nd = TypeAliasType("ToUInt32_nd", _ToArray_nd[np.uint32])

ToUInt64_0d = TypeAliasType("ToUInt64_0d", _ToArray_0d[np.uint64])
ToUInt64_1d = TypeAliasType("ToUInt64_1d", _ToArray_1d[np.uint64])
ToUInt64_2d = TypeAliasType("ToUInt64_2d", _ToArray_2d[np.uint64])
ToUInt64_3d = TypeAliasType("ToUInt64_3d", _ToArray_3d[np.uint64])
ToUInt64_nd = TypeAliasType("ToUInt64_nd", _ToArray_nd[np.uint64])

ToULong_0d = TypeAliasType("ToULong_0d", _ToArray_0d[np.ulong])
ToULong_1d = TypeAliasType("ToULong_1d", _ToArray_1d[np.ulong])
ToULong_2d = TypeAliasType("ToULong_2d", _ToArray_2d[np.ulong])
ToULong_3d = TypeAliasType("ToULong_3d", _ToArray_3d[np.ulong])
ToULong_nd = TypeAliasType("ToULong_nd", _ToArray_nd[np.ulong])

ToUIntP_0d = TypeAliasType("ToUIntP_0d", _ToArray_0d[np.uintp])
ToUIntP_1d = TypeAliasType("ToUIntP_1d", _ToArray_1d[np.uintp])
ToUIntP_2d = TypeAliasType("ToUIntP_2d", _ToArray_2d[np.uintp])
ToUIntP_3d = TypeAliasType("ToUIntP_3d", _ToArray_3d[np.uintp])
ToUIntP_nd = TypeAliasType("ToUIntP_nd", _ToArray_nd[np.uintp])

ToULongLong_0d = TypeAliasType("ToULongLong_0d", _ToArray_0d[np.ulonglong])
ToULongLong_1d = TypeAliasType("ToULongLong_1d", _ToArray_1d[np.ulonglong])
ToULongLong_2d = TypeAliasType("ToULongLong_2d", _ToArray_2d[np.ulonglong])
ToULongLong_3d = TypeAliasType("ToULongLong_3d", _ToArray_3d[np.ulonglong])
ToULongLong_nd = TypeAliasType("ToULongLong_nd", _ToArray_nd[np.ulonglong])

ToUInteger_0d = TypeAliasType("ToUInteger_0d", _ToArray_0d[np.unsignedinteger])
ToUInteger_1d = TypeAliasType("ToUInteger_1d", _ToArray_1d[np.unsignedinteger])
ToUInteger_2d = TypeAliasType("ToUInteger_2d", _ToArray_2d[np.unsignedinteger])
ToUInteger_3d = TypeAliasType("ToUInteger_3d", _ToArray_3d[np.unsignedinteger])
ToUInteger_nd = TypeAliasType("ToUInteger_nd", _ToArray_nd[np.unsignedinteger])

# signed integers
ToInt8_0d = TypeAliasType("ToInt8_0d", _ToArray_0d[np.int8])
ToInt8_1d = TypeAliasType("ToInt8_1d", _ToArray_1d[np.int8])
ToInt8_2d = TypeAliasType("ToInt8_2d", _ToArray_2d[np.int8])
ToInt8_3d = TypeAliasType("ToInt8_3d", _ToArray_3d[np.int8])
ToInt8_nd = TypeAliasType("ToInt8_nd", _ToArray_nd[np.int8])

ToInt16_0d = TypeAliasType("ToInt16_0d", _ToArray_0d[np.int16])
ToInt16_1d = TypeAliasType("ToInt16_1d", _ToArray_1d[np.int16])
ToInt16_2d = TypeAliasType("ToInt16_2d", _ToArray_2d[np.int16])
ToInt16_3d = TypeAliasType("ToInt16_3d", _ToArray_3d[np.int16])
ToInt16_nd = TypeAliasType("ToInt16_nd", _ToArray_nd[np.int16])

ToInt32_0d = TypeAliasType("ToInt32_0d", _ToArray_0d[np.int32])
ToInt32_1d = TypeAliasType("ToInt32_1d", _ToArray_1d[np.int32])
ToInt32_2d = TypeAliasType("ToInt32_2d", _ToArray_2d[np.int32])
ToInt32_3d = TypeAliasType("ToInt32_3d", _ToArray_3d[np.int32])
ToInt32_nd = TypeAliasType("ToInt32_nd", _ToArray_nd[np.int32])

ToInt64_0d = TypeAliasType("ToInt64_0d", _ToArray_0d[np.int64])
ToInt64_1d = TypeAliasType("ToInt64_1d", _ToArray_1d[np.int64])
ToInt64_2d = TypeAliasType("ToInt64_2d", _ToArray_2d[np.int64])
ToInt64_3d = TypeAliasType("ToInt64_3d", _ToArray_3d[np.int64])
ToInt64_nd = TypeAliasType("ToInt64_nd", _ToArray_nd[np.int64])

ToLong_0d = TypeAliasType("ToLong_0d", _ToArray_0d[np.long])
ToLong_1d = TypeAliasType("ToLong_1d", _ToArray_1d[np.long])
ToLong_2d = TypeAliasType("ToLong_2d", _ToArray_2d[np.long])
ToLong_3d = TypeAliasType("ToLong_3d", _ToArray_3d[np.long])
ToLong_nd = TypeAliasType("ToLong_nd", _ToArray_nd[np.long])

_ToIntP: TypeAlias = np.intp | Is[int]
ToIntP_0d = TypeAliasType("ToIntP_0d", _ToArray_0d[np.intp, _ToIntP])
ToIntP_1d = TypeAliasType("ToIntP_1d", _ToArray_1d[np.intp, _ToIntP])
ToIntP_2d = TypeAliasType("ToIntP_2d", _ToArray_2d[np.intp, _ToIntP])
ToIntP_3d = TypeAliasType("ToIntP_3d", _ToArray_3d[np.intp, _ToIntP])
ToIntP_nd = TypeAliasType("ToIntP_nd", _ToArray_nd[np.intp, _ToIntP])

ToLongLong_0d = TypeAliasType("ToLongLong_0d", _ToArray_0d[np.longlong])
ToLongLong_1d = TypeAliasType("ToLongLong_1d", _ToArray_1d[np.longlong])
ToLongLong_2d = TypeAliasType("ToLongLong_2d", _ToArray_2d[np.longlong])
ToLongLong_3d = TypeAliasType("ToLongLong_3d", _ToArray_3d[np.longlong])
ToLongLong_nd = TypeAliasType("ToLongLong_nd", _ToArray_nd[np.longlong])

_ToInteger: TypeAlias = np.signedinteger | Is[int]
ToSInteger_0d = TypeAliasType("ToSInteger_0d", _ToArray_0d[np.signedinteger, _ToInteger])
ToSInteger_1d = TypeAliasType("ToSInteger_1d", _ToArray_1d[np.signedinteger, _ToInteger])
ToSInteger_2d = TypeAliasType("ToSInteger_2d", _ToArray_2d[np.signedinteger, _ToInteger])
ToSInteger_3d = TypeAliasType("ToSInteger_3d", _ToArray_3d[np.signedinteger, _ToInteger])
ToSInteger_nd = TypeAliasType("ToSInteger_nd", _ToArray_nd[np.signedinteger, _ToInteger])

# integers
ToInteger_0d = TypeAliasType("ToInteger_0d", _ToArray_0d[np.integer, Is[int]])
ToInteger_1d = TypeAliasType("ToInteger_1d", _ToArray_1d[np.integer, Is[int]])
ToInteger_2d = TypeAliasType("ToInteger_2d", _ToArray_2d[np.integer, Is[int]])
ToInteger_3d = TypeAliasType("ToInteger_3d", _ToArray_3d[np.integer, Is[int]])
ToInteger_nd = TypeAliasType("ToInteger_nd", _ToArray_nd[np.integer, Is[int]])

# real floats
ToFloat16_0d = TypeAliasType("ToFloat16_0d", _ToArray_0d[np.float16])
ToFloat16_1d = TypeAliasType("ToFloat16_1d", _ToArray_1d[np.float16])
ToFloat16_2d = TypeAliasType("ToFloat16_2d", _ToArray_2d[np.float16])
ToFloat16_3d = TypeAliasType("ToFloat16_3d", _ToArray_3d[np.float16])
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _ToArray_nd[np.float16])

ToFloat32_0d = TypeAliasType("ToFloat32_0d", _ToArray_0d[np.float32])
ToFloat32_1d = TypeAliasType("ToFloat32_1d", _ToArray_1d[np.float32])
ToFloat32_2d = TypeAliasType("ToFloat32_2d", _ToArray_2d[np.float32])
ToFloat32_3d = TypeAliasType("ToFloat32_3d", _ToArray_3d[np.float32])
ToFloat32_nd = TypeAliasType("ToFloat32_nd", _ToArray_nd[np.float32])

_ToFloat64: TypeAlias = np.floating[_64Bit]
ToFloat64_0d = TypeAliasType("ToFloat64_0d", _ToArray_0d[_ToFloat64, Is[float]])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _ToArray_1d[_ToFloat64, Is[float]])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _ToArray_2d[_ToFloat64, Is[float]])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _ToArray_3d[_ToFloat64, Is[float]])
ToFloat64_nd = TypeAliasType("ToFloat64_nd", _ToArray_nd[_ToFloat64, Is[float]])

ToLongDouble_0d = TypeAliasType("ToLongDouble_0d", _ToArray_0d[np.longdouble])
ToLongDouble_1d = TypeAliasType("ToLongDouble_1d", _ToArray_1d[np.longdouble])
ToLongDouble_2d = TypeAliasType("ToLongDouble_2d", _ToArray_2d[np.longdouble])
ToLongDouble_3d = TypeAliasType("ToLongDouble_3d", _ToArray_3d[np.longdouble])
ToLongDouble_nd = TypeAliasType("ToLongDouble_nd", _ToArray_nd[np.longdouble])

ToFloating_0d = TypeAliasType("ToFloating_0d", _ToArray_0d[np.floating, Is[float]])
ToFloating_1d = TypeAliasType("ToFloating_1d", _ToArray_1d[np.floating, Is[float]])
ToFloating_2d = TypeAliasType("ToFloating_2d", _ToArray_2d[np.floating, Is[float]])
ToFloating_3d = TypeAliasType("ToFloating_3d", _ToArray_3d[np.floating, Is[float]])
ToFloating_nd = TypeAliasType("ToFloating_nd", _ToArray_nd[np.floating, Is[float]])

# complex floats
ToComplex64_0d = TypeAliasType("ToComplex64_0d", _ToArray_0d[np.complex64])
ToComplex64_1d = TypeAliasType("ToComplex64_1d", _ToArray_1d[np.complex64])
ToComplex64_2d = TypeAliasType("ToComplex64_2d", _ToArray_2d[np.complex64])
ToComplex64_3d = TypeAliasType("ToComplex64_3d", _ToArray_3d[np.complex64])
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _ToArray_nd[np.complex64])

_ToComplex128: TypeAlias = np.complexfloating[_64Bit]
ToComplex128_0d = TypeAliasType("ToComplex128_0d", _ToArray_0d[_ToComplex128, Is[complex]])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _ToArray_1d[_ToComplex128, Is[complex]])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _ToArray_2d[_ToComplex128, Is[complex]])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _ToArray_3d[_ToComplex128, Is[complex]])
ToComplex128_nd = TypeAliasType("ToComplex128_nd", _ToArray_nd[_ToComplex128, Is[complex]])

ToCLongDouble_0d = TypeAliasType("ToCLongDouble_0d", _ToArray_0d[np.clongdouble])
ToCLongDouble_1d = TypeAliasType("ToCLongDouble_1d", _ToArray_1d[np.clongdouble])
ToCLongDouble_2d = TypeAliasType("ToCLongDouble_2d", _ToArray_2d[np.clongdouble])
ToCLongDouble_3d = TypeAliasType("ToCLongDouble_3d", _ToArray_3d[np.clongdouble])
ToCLongDouble_nd = TypeAliasType("ToCLongDouble_nd", _ToArray_nd[np.clongdouble])

ToCFloating_0d = TypeAliasType("ToCFloating_0d", _ToArray_0d[np.complexfloating, Is[complex]])
ToCFloating_1d = TypeAliasType("ToCFloating_1d", _ToArray_1d[np.complexfloating, Is[complex]])
ToCFloating_2d = TypeAliasType("ToCFloating_2d", _ToArray_2d[np.complexfloating, Is[complex]])
ToCFloating_3d = TypeAliasType("ToCFloating_3d", _ToArray_3d[np.complexfloating, Is[complex]])
ToCFloating_nd = TypeAliasType("ToCFloating_nd", _ToArray_nd[np.complexfloating, Is[complex]])

# integers, real- and complex floats
ToNumber_0d = TypeAliasType("ToNumber_0d", _ToArray_0d[np.number, _PyNumber])
ToNumber_1d = TypeAliasType("ToNumber_1d", _ToArray_1d[np.number, _PyNumber])
ToNumber_2d = TypeAliasType("ToNumber_2d", _ToArray_2d[np.number, _PyNumber])
ToNumber_3d = TypeAliasType("ToNumber_3d", _ToArray_3d[np.number, _PyNumber])
ToNumber_nd = TypeAliasType("ToNumber_nd", _ToArray_nd[np.number, _PyNumber])

# integers and real floats
ToReal_0d = TypeAliasType("ToReal_0d", _ToArray_0d[np.number[Any, float | int], _PyReal])
ToReal_1d = TypeAliasType("ToReal_1d", _ToArray_1d[np.number[Any, float | int], _PyReal])
ToReal_2d = TypeAliasType("ToReal_2d", _ToArray_2d[np.number[Any, float | int], _PyReal])
ToReal_3d = TypeAliasType("ToReal_3d", _ToArray_3d[np.number[Any, float | int], _PyReal])
ToReal_nd = TypeAliasType("ToReal_nd", _ToArray_nd[np.number[Any, float | int], _PyReal])

# real- and complex floats
ToInexact_0d = TypeAliasType("ToInexact_0d", _ToArray_0d[np.inexact, _PyInexact])
ToInexact_1d = TypeAliasType("ToInexact_1d", _ToArray_1d[np.inexact, _PyInexact])
ToInexact_2d = TypeAliasType("ToInexact_2d", _ToArray_2d[np.inexact, _PyInexact])
ToInexact_3d = TypeAliasType("ToInexact_3d", _ToArray_3d[np.inexact, _PyInexact])
ToInexact_nd = TypeAliasType("ToInexact_nd", _ToArray_nd[np.inexact, _PyInexact])

# temporal
_ToTimeDelta: TypeAlias = np.timedelta64[Any]
ToTimeDelta_0d = TypeAliasType("ToTimeDelta_0d", _ToArray_0d[np.timedelta64])
ToTimeDelta_1d = TypeAliasType("ToTimeDelta_1d", _ToArray_1d[np.timedelta64])
ToTimeDelta_2d = TypeAliasType("ToTimeDelta_2d", _ToArray_2d[np.timedelta64])
ToTimeDelta_3d = TypeAliasType("ToTimeDelta_3d", _ToArray_3d[np.timedelta64])
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _ToArray_nd[np.timedelta64])

_ToDateTime: TypeAlias = np.datetime64[Any]
ToDateTime_0d = TypeAliasType("ToDateTime_0d", _ToArray_0d[np.datetime64])
ToDateTime_1d = TypeAliasType("ToDateTime_1d", _ToArray_1d[np.datetime64])
ToDateTime_2d = TypeAliasType("ToDateTime_2d", _ToArray_2d[np.datetime64])
ToDateTime_3d = TypeAliasType("ToDateTime_3d", _ToArray_3d[np.datetime64])
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _ToArray_nd[np.datetime64])

# fixed strings
_ToBytes: TypeAlias = np.character[bytes]
ToBytes_0d = TypeAliasType("ToBytes_0d", _ToArray_0d[_ToBytes, Is[bytes]])
ToBytes_1d = TypeAliasType("ToBytes_1d", _ToArray_1d[_ToBytes, Is[bytes]])
ToBytes_2d = TypeAliasType("ToBytes_2d", _ToArray_2d[_ToBytes, Is[bytes]])
ToBytes_3d = TypeAliasType("ToBytes_3d", _ToArray_3d[_ToBytes, Is[bytes]])
ToBytes_nd = TypeAliasType("ToBytes_nd", _ToArray_nd[_ToBytes, Is[bytes]])

_ToStr: TypeAlias = np.character[str]
ToStr_0d = TypeAliasType("ToStr_0d", _ToArray_0d[_ToStr, Is[str]])
ToStr_1d = TypeAliasType("ToStr_1d", _ToArray_1d[_ToStr, Is[str]])
ToStr_2d = TypeAliasType("ToStr_2d", _ToArray_2d[_ToStr, Is[str]])
ToStr_3d = TypeAliasType("ToStr_3d", _ToArray_3d[_ToStr, Is[str]])
ToStr_nd = TypeAliasType("ToStr_nd", _ToArray_nd[_ToStr, Is[str]])

ToCharacter_0d = TypeAliasType("ToCharacter_0d", _ToArray_0d[np.character, _PyCharacter])
ToCharacter_1d = TypeAliasType("ToCharacter_1d", _ToArray_1d[np.character, _PyCharacter])
ToCharacter_2d = TypeAliasType("ToCharacter_2d", _ToArray_2d[np.character, _PyCharacter])
ToCharacter_3d = TypeAliasType("ToCharacter_3d", _ToArray_3d[np.character, _PyCharacter])
ToCharacter_nd = TypeAliasType("ToCharacter_nd", _ToArray_nd[np.character, _PyCharacter])

# python object
ToObject_0d = TypeAliasType("ToObject_0d", _ToArray_0d[np.object_, _PyObject])
ToObject_1d = TypeAliasType("ToObject_1d", _ToArray_1d[np.object_, _PyObject])
ToObject_2d = TypeAliasType("ToObject_2d", _ToArray_2d[np.object_, _PyObject])
ToObject_3d = TypeAliasType("ToObject_3d", _ToArray_3d[np.object_, _PyObject])
ToObject_nd = TypeAliasType("ToObject_nd", _ToArray_nd[np.object_, _PyObject])

# any scalar
ToAny_0d = TypeAliasType("ToAny_0d", _ToArray_0d[np.generic, object])
ToAny_1d = TypeAliasType("ToAny_1d", _ToArray_1d[np.generic, object])
ToAny_2d = TypeAliasType("ToAny_2d", _ToArray_2d[np.generic, object])
ToAny_3d = TypeAliasType("ToAny_3d", _ToArray_3d[np.generic, object])
ToAny_nd = TypeAliasType("ToAny_nd", _ToArray_nd[np.generic, object])

###
# Coercible (overlapping) scalar- and array-likes

# bool
CoBool_0d = TypeAliasType("CoBool_0d", _ToArray_0d[_ToBool, bool])
CoBool_1d = TypeAliasType("CoBool_1d", _ToArray_1d[_ToBool, bool])
CoBool_2d = TypeAliasType("CoBool_2d", _ToArray_2d[_ToBool, bool])
CoBool_3d = TypeAliasType("CoBool_3d", _ToArray_3d[_ToBool, bool])
CoBool_nd = TypeAliasType("CoBool_nd", _ToArray_nd[_ToBool, bool])

# unsigned integers
_CoUInt8: TypeAlias = np.uint8 | _ToBool
CoUInt8_0d = TypeAliasType("CoUInt8_0d", _ToArray_0d[_CoUInt8, bool])
CoUInt8_1d = TypeAliasType("CoUInt8_1d", _ToArray_1d[_CoUInt8, bool])
CoUInt8_2d = TypeAliasType("CoUInt8_2d", _ToArray_2d[_CoUInt8, bool])
CoUInt8_3d = TypeAliasType("CoUInt8_3d", _ToArray_3d[_CoUInt8, bool])
CoUInt8_nd = TypeAliasType("CoUInt8_nd", _ToArray_nd[_CoUInt8, bool])

_CoUInt16: TypeAlias = np.uint16 | _CoUInt8
CoUInt16_0d = TypeAliasType("CoUInt16_0d", _ToArray_0d[_CoUInt16, bool])
CoUInt16_1d = TypeAliasType("CoUInt16_1d", _ToArray_1d[_CoUInt16, bool])
CoUInt16_2d = TypeAliasType("CoUInt16_2d", _ToArray_2d[_CoUInt16, bool])
CoUInt16_3d = TypeAliasType("CoUInt16_3d", _ToArray_3d[_CoUInt16, bool])
CoUInt16_nd = TypeAliasType("CoUInt16_nd", _ToArray_nd[_CoUInt16, bool])

_CoUInt32: TypeAlias = np.uint32 | _CoUInt16
CoUInt32_0d = TypeAliasType("CoUInt32_0d", _ToArray_0d[_CoUInt32, bool])
CoUInt32_1d = TypeAliasType("CoUInt32_1d", _ToArray_1d[_CoUInt32, bool])
CoUInt32_2d = TypeAliasType("CoUInt32_2d", _ToArray_2d[_CoUInt32, bool])
CoUInt32_3d = TypeAliasType("CoUInt32_3d", _ToArray_3d[_CoUInt32, bool])
CoUInt32_nd = TypeAliasType("CoUInt32_nd", _ToArray_nd[_CoUInt32, bool])

_CoUInt64: TypeAlias = np.uint64 | _CoUInt32
CoUInt64_0d = TypeAliasType("CoUInt64_0d", _ToArray_0d[_CoUInt64, bool])
CoUInt64_1d = TypeAliasType("CoUInt64_1d", _ToArray_1d[_CoUInt64, bool])
CoUInt64_2d = TypeAliasType("CoUInt64_2d", _ToArray_2d[_CoUInt64, bool])
CoUInt64_3d = TypeAliasType("CoUInt64_3d", _ToArray_3d[_CoUInt64, bool])
CoUInt64_nd = TypeAliasType("CoUInt64_nd", _ToArray_nd[_CoUInt64, bool])

_CoULong: TypeAlias = np.ulong | _CoUInt32
CoULong_0d = TypeAliasType("CoULong_0d", _ToArray_0d[_CoULong, bool])
CoULong_1d = TypeAliasType("CoULong_1d", _ToArray_1d[_CoULong, bool])
CoULong_2d = TypeAliasType("CoULong_2d", _ToArray_2d[_CoULong, bool])
CoULong_3d = TypeAliasType("CoULong_3d", _ToArray_3d[_CoULong, bool])
CoULong_nd = TypeAliasType("CoULong_nd", _ToArray_nd[_CoULong, bool])

_CoUIntP: TypeAlias = np.uintp | _CoULong
CoUIntP_0d = TypeAliasType("CoUIntP_0d", _ToArray_0d[_CoUIntP, bool])
CoUIntP_1d = TypeAliasType("CoUIntP_1d", _ToArray_1d[_CoUIntP, bool])
CoUIntP_2d = TypeAliasType("CoUIntP_2d", _ToArray_2d[_CoUIntP, bool])
CoUIntP_3d = TypeAliasType("CoUIntP_3d", _ToArray_3d[_CoUIntP, bool])
CoUIntP_nd = TypeAliasType("CoUIntP_nd", _ToArray_nd[_CoUIntP, bool])

_CoULongLong: TypeAlias = np.unsignedinteger | _ToBool
CoULongLong_0d = TypeAliasType("CoULongLong_0d", _ToArray_0d[_CoULongLong, bool])
CoULongLong_1d = TypeAliasType("CoULongLong_1d", _ToArray_1d[_CoULongLong, bool])
CoULongLong_2d = TypeAliasType("CoULongLong_2d", _ToArray_2d[_CoULongLong, bool])
CoULongLong_3d = TypeAliasType("CoULongLong_3d", _ToArray_3d[_CoULongLong, bool])
CoULongLong_nd = TypeAliasType("CoULongLong_nd", _ToArray_nd[_CoULongLong, bool])

# signed integers
_CoInt8: TypeAlias = np.int8 | _ToBool
CoInt8_0d = TypeAliasType("CoInt8_0d", _ToArray_0d[_CoInt8, bool])
CoInt8_1d = TypeAliasType("CoInt8_1d", _ToArray_1d[_CoInt8, bool])
CoInt8_2d = TypeAliasType("CoInt8_2d", _ToArray_2d[_CoInt8, bool])
CoInt8_3d = TypeAliasType("CoInt8_3d", _ToArray_3d[_CoInt8, bool])
CoInt8_nd = TypeAliasType("CoInt8_nd", _ToArray_nd[_CoInt8, bool])

_CoInt16: TypeAlias = np.int16 | np.uint8 | _CoInt8
CoInt16_0d = TypeAliasType("CoInt16_0d", _ToArray_0d[_CoInt16, bool])
CoInt16_1d = TypeAliasType("CoInt16_1d", _ToArray_1d[_CoInt16, bool])
CoInt16_2d = TypeAliasType("CoInt16_2d", _ToArray_2d[_CoInt16, bool])
CoInt16_3d = TypeAliasType("CoInt16_3d", _ToArray_3d[_CoInt16, bool])
CoInt16_nd = TypeAliasType("CoInt16_nd", _ToArray_nd[_CoInt16, bool])

_CoInt32: TypeAlias = np.int32 | np.uint16 | _CoInt16
CoInt32_0d = TypeAliasType("CoInt32_0d", _ToArray_0d[_CoInt32, bool])
CoInt32_1d = TypeAliasType("CoInt32_1d", _ToArray_1d[_CoInt32, bool])
CoInt32_2d = TypeAliasType("CoInt32_2d", _ToArray_2d[_CoInt32, bool])
CoInt32_3d = TypeAliasType("CoInt32_3d", _ToArray_3d[_CoInt32, bool])
CoInt32_nd = TypeAliasType("CoInt32_nd", _ToArray_nd[_CoInt32, bool])

_CoInt64: TypeAlias = np.int64 | np.uint32 | _CoInt32
CoInt64_0d = TypeAliasType("CoInt64_0d", _ToArray_0d[_CoInt64, int])
CoInt64_1d = TypeAliasType("CoInt64_1d", _ToArray_1d[_CoInt64, int])
CoInt64_2d = TypeAliasType("CoInt64_2d", _ToArray_2d[_CoInt64, int])
CoInt64_3d = TypeAliasType("CoInt64_3d", _ToArray_3d[_CoInt64, int])
CoInt64_nd = TypeAliasType("CoInt64_nd", _ToArray_nd[_CoInt64, int])

_CoLong: TypeAlias = np.long | _CoInt32
CoLong_0d = TypeAliasType("CoLong_0d", _ToArray_0d[_CoLong, bool])
CoLong_1d = TypeAliasType("CoLong_1d", _ToArray_1d[_CoLong, bool])
CoLong_2d = TypeAliasType("CoLong_2d", _ToArray_2d[_CoLong, bool])
CoLong_3d = TypeAliasType("CoLong_3d", _ToArray_3d[_CoLong, bool])
CoLong_nd = TypeAliasType("CoLong_nd", _ToArray_nd[_CoLong, bool])

_CoIntP: TypeAlias = np.intp | _CoLong
CoIntP_0d = TypeAliasType("CoIntP_0d", _ToArray_0d[_CoIntP, int])
CoIntP_1d = TypeAliasType("CoIntP_1d", _ToArray_1d[_CoIntP, int])
CoIntP_2d = TypeAliasType("CoIntP_2d", _ToArray_2d[_CoIntP, int])
CoIntP_3d = TypeAliasType("CoIntP_3d", _ToArray_3d[_CoIntP, int])
CoIntP_nd = TypeAliasType("CoIntP_nd", _ToArray_nd[_CoIntP, int])

_CoLongLong: TypeAlias = np.signedinteger | _CoUInt32
CoLongLong_0d = TypeAliasType("CoLongLong_0d", _ToArray_0d[_CoLongLong, int])
CoLongLong_1d = TypeAliasType("CoLongLong_1d", _ToArray_1d[_CoLongLong, int])
CoLongLong_2d = TypeAliasType("CoLongLong_2d", _ToArray_2d[_CoLongLong, int])
CoLongLong_3d = TypeAliasType("CoLongLong_3d", _ToArray_3d[_CoLongLong, int])
CoLongLong_nd = TypeAliasType("CoLongLong_nd", _ToArray_nd[_CoLongLong, int])

_CoInteger: TypeAlias = np.integer | _ToBool

# real floats

_CoFloat16: TypeAlias = np.float16 | np.uint8 | np.int16 | _ToBool
CoFloat16_0d = TypeAliasType("CoFloat16_0d", _ToArray_0d[_CoFloat16, bool])
CoFloat16_1d = TypeAliasType("CoFloat16_1d", _ToArray_1d[_CoFloat16, bool])
CoFloat16_2d = TypeAliasType("CoFloat16_2d", _ToArray_2d[_CoFloat16, bool])
CoFloat16_3d = TypeAliasType("CoFloat16_3d", _ToArray_3d[_CoFloat16, bool])
CoFloat16_nd = TypeAliasType("CoFloat16_nd", _ToArray_nd[_CoFloat16, bool])

_CoFloat32: TypeAlias = np.float32 | np.uint16 | np.int16 | _CoFloat16
CoFloat32_0d = TypeAliasType("CoFloat32_0d", _ToArray_0d[_CoFloat32, bool])
CoFloat32_1d = TypeAliasType("CoFloat32_1d", _ToArray_1d[_CoFloat32, bool])
CoFloat32_2d = TypeAliasType("CoFloat32_2d", _ToArray_2d[_CoFloat32, bool])
CoFloat32_3d = TypeAliasType("CoFloat32_3d", _ToArray_3d[_CoFloat32, bool])
CoFloat32_nd = TypeAliasType("CoFloat32_nd", _ToArray_nd[_CoFloat32, bool])

_CoFloat64: TypeAlias = _ToFloat64 | np.float32 | np.float16 | _CoInteger
CoFloat64_0d = TypeAliasType("CoFloat64_0d", _ToArray_0d[_CoFloat64, float])
CoFloat64_1d = TypeAliasType("CoFloat64_1d", _ToArray_1d[_CoFloat64, float])
CoFloat64_2d = TypeAliasType("CoFloat64_2d", _ToArray_2d[_CoFloat64, float])
CoFloat64_3d = TypeAliasType("CoFloat64_3d", _ToArray_3d[_CoFloat64, float])
CoFloat64_nd = TypeAliasType("CoFloat64_nd", _ToArray_nd[_CoFloat64, float])

_CoFloating: TypeAlias = np.floating | np.integer | _ToBool
CoFloating_0d = TypeAliasType("CoFloating_0d", _ToArray_0d[_CoFloating, float])
CoFloating_1d = TypeAliasType("CoFloating_1d", _ToArray_1d[_CoFloating, float])
CoFloating_2d = TypeAliasType("CoFloating_2d", _ToArray_2d[_CoFloating, float])
CoFloating_3d = TypeAliasType("CoFloating_3d", _ToArray_3d[_CoFloating, float])
CoFloating_nd = TypeAliasType("CoFloating_nd", _ToArray_nd[_CoFloating, float])

# complex floats
_CoComplex64: TypeAlias = np.complex64 | _CoFloat32
CoComplex64_0d = TypeAliasType("CoComplex64_0d", _ToArray_0d[_CoComplex64, bool])
CoComplex64_1d = TypeAliasType("CoComplex64_1d", _ToArray_1d[_CoComplex64, bool])
CoComplex64_2d = TypeAliasType("CoComplex64_2d", _ToArray_2d[_CoComplex64, bool])
CoComplex64_3d = TypeAliasType("CoComplex64_3d", _ToArray_3d[_CoComplex64, bool])
CoComplex64_nd = TypeAliasType("CoComplex64_nd", _ToArray_nd[_CoComplex64, bool])

_CoComplex128: TypeAlias = _ToComplex128 | np.complex64 | _CoFloat64
CoComplex128_0d = TypeAliasType("CoComplex128_0d", _ToArray_0d[_CoComplex128, complex])
CoComplex128_1d = TypeAliasType("CoComplex128_1d", _ToArray_1d[_CoComplex128, complex])
CoComplex128_2d = TypeAliasType("CoComplex128_2d", _ToArray_2d[_CoComplex128, complex])
CoComplex128_3d = TypeAliasType("CoComplex128_3d", _ToArray_3d[_CoComplex128, complex])
CoComplex128_nd = TypeAliasType("CoComplex128_nd", _ToArray_nd[_CoComplex128, complex])

_CoCFloating: TypeAlias = np.number | _ToBool
CoCFloating_0d = TypeAliasType("CoCFloating_0d", _ToArray_0d[_CoCFloating, complex])
CoCFloating_1d = TypeAliasType("CoCFloating_1d", _ToArray_1d[_CoCFloating, complex])
CoCFloating_2d = TypeAliasType("CoCFloating_2d", _ToArray_2d[_CoCFloating, complex])
CoCFloating_3d = TypeAliasType("CoCFloating_3d", _ToArray_3d[_CoCFloating, complex])
CoCFloating_nd = TypeAliasType("CoCFloating_nd", _ToArray_nd[_CoCFloating, complex])

# temporal
_CoTimeDelta: TypeAlias = _ToTimeDelta | _CoInteger
CoTimeDelta_0d = TypeAliasType("CoTimeDelta_0d", _ToArray_0d[_CoTimeDelta, int])
CoTimeDelta_1d = TypeAliasType("CoTimeDelta_1d", _ToArray_1d[_CoTimeDelta, int])
CoTimeDelta_2d = TypeAliasType("CoTimeDelta_2d", _ToArray_2d[_CoTimeDelta, int])
CoTimeDelta_3d = TypeAliasType("CoTimeDelta_3d", _ToArray_3d[_CoTimeDelta, int])
CoTimeDelta_nd = TypeAliasType("CoTimeDelta_nd", _ToArray_nd[_CoTimeDelta, int])

_CoDateTime: TypeAlias = _ToDateTime | _ToTimeDelta
CoDateTime_0d = TypeAliasType("CoDateTime_0d", _ToArray_0d[_CoDateTime])
CoDateTime_1d = TypeAliasType("CoDateTime_1d", _ToArray_1d[_CoDateTime])
CoDateTime_2d = TypeAliasType("CoDateTime_2d", _ToArray_2d[_CoDateTime])
CoDateTime_3d = TypeAliasType("CoDateTime_3d", _ToArray_3d[_CoDateTime])
CoDateTime_nd = TypeAliasType("CoDateTime_nd", _ToArray_nd[_CoDateTime])

# fixed strings
_CoBytes: TypeAlias = _ToBytes
CoBytes_0d = TypeAliasType("CoBytes_0d", _ToArray_0d[_CoBytes, Is[bytes]])
CoBytes_1d = TypeAliasType("CoBytes_1d", _ToArray_1d[_CoBytes, Is[bytes]])
CoBytes_2d = TypeAliasType("CoBytes_2d", _ToArray_2d[_CoBytes, Is[bytes]])
CoBytes_3d = TypeAliasType("CoBytes_3d", _ToArray_3d[_CoBytes, Is[bytes]])
CoBytes_nd = TypeAliasType("CoBytes_nd", _ToArray_nd[_CoBytes, Is[bytes]])

_CoStr: TypeAlias = np.character
CoStr_0d = TypeAliasType("CoStr_0d", _ToArray_0d[_CoStr, _PyCharacter])
CoStr_1d = TypeAliasType("CoStr_1d", _ToArray_1d[_CoStr, _PyCharacter])
CoStr_2d = TypeAliasType("CoStr_2d", _ToArray_2d[_CoStr, _PyCharacter])
CoStr_3d = TypeAliasType("CoStr_3d", _ToArray_3d[_CoStr, _PyCharacter])
CoStr_nd = TypeAliasType("CoStr_nd", _ToArray_nd[_CoStr, _PyCharacter])

###
# DType-likes
# TODO
