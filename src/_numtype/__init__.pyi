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

###
# Type constraints (bijective type mappings)

ShapeC = TypeVar(  # noqa: PYI001
    "ShapeC",
    NDim0,
    NDim1,
    NDim1 | NDim0,
    NDim2,
    NDim2 | NDim1,
    NDim2 | NDim1 | NDim0,
    NDim3,
    NDim3 | NDim2,
    NDim3 | NDim2 | NDim1,
    NDim3 | NDim2 | NDim1 | NDim0,
    NDim3p,
    NDim2p,
    NDim1p,
    tuple[int, ...],
    default=tuple[int, ...],
)
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

# A slimmed down version of `_NestedSequence`, based on `optype.numpy.SequenceND`.
# https://github.com/jorenham/optype
@type_check_only
class Sequence_nd(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | Sequence_nd[_T_co]: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

@type_check_only
class Can(Protocol[_ScalarT_co, _ShapeT_co]):
    def __array__(self, /) -> np.ndarray[_ShapeT_co, np.dtype[_ScalarT_co]]: ...

# A shape-typed version of `numpy._typing._Can`, parametrized by the
# scalar-type and shape-type, and excludes `np.generic` scalars (through `__len__`).
@type_check_only
class CanLen(Can[_ScalarT_co, _ShapeT_co], Protocol[_ScalarT_co, _ShapeT_co]):
    def __len__(self, /) -> int: ...

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
# Helper aliases

_PyReal: TypeAlias = Is[int] | Is[float]
_PyInexact: TypeAlias = Is[float] | Is[complex]
_PyNumber: TypeAlias = Is[int] | _PyInexact
_PyCharacter: TypeAlias = Is[bytes] | Is[str]
_PyObject: TypeAlias = (  # anything that will always result in something with a `object_` dtype
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
    | set[Any]
    | frozenset[Any]
    | dict[Any, Any]
)

_AsFloat64: TypeAlias = np.floating[_64Bit]
_AsComplex128: TypeAlias = np.complexfloating[_64Bit]

_ToBool: TypeAlias = np.generic[bool]
_ToUInt8: TypeAlias = np.uint8 | _ToBool
_ToUInt16: TypeAlias = np.uint16 | _ToUInt8
_ToUInt32: TypeAlias = np.uint32 | _ToUInt16
_ToUInt64: TypeAlias = np.uint64 | _ToUInt32
_ToULong: TypeAlias = np.ulong | _ToUInt32
_ToUIntP: TypeAlias = np.uintp | _ToULong
_ToULongLong: TypeAlias = np.unsignedinteger | _ToBool
_ToInt8: TypeAlias = np.int8 | _ToBool
_ToInt16: TypeAlias = np.int16 | np.uint8 | _ToInt8
_ToInt32: TypeAlias = np.int32 | np.uint16 | _ToInt16
_ToInt64: TypeAlias = np.int64 | np.uint32 | _ToInt32
_ToLong: TypeAlias = np.long | _ToInt32
_ToIntP: TypeAlias = np.intp | _ToLong
_ToLongLong: TypeAlias = np.signedinteger | _ToUInt32
_ToInteger: TypeAlias = np.generic[int]
_ToFloat16: TypeAlias = np.float16 | np.uint8 | np.int16 | _ToBool
_ToFloat32: TypeAlias = np.float32 | np.uint16 | np.int16 | _ToFloat16
_ToFloat64: TypeAlias = _AsFloat64 | np.float32 | np.float16 | _ToInteger
_ToFloating: TypeAlias = np.generic[float | int]
_ToComplex64: TypeAlias = np.complex64 | _ToFloat32
_ToComplex128: TypeAlias = _AsComplex128 | np.complex64 | _ToFloat64
_ToNumber: TypeAlias = np.generic[complex | float | int]
_ToTimeDelta: TypeAlias = np.timedelta64[Any] | _ToInteger
_ToDateTime: TypeAlias = np.datetime64[Any] | np.timedelta64[Any]  # scalars may also accepts `integer | _ToBool`
_ToBytes: TypeAlias = np.character[bytes]
_ToStr: TypeAlias = np.character
_ToObject: TypeAlias = np.generic

_To1_0d: TypeAlias = _ScalarT | Can[_ScalarT, tuple[()]]
_To2_0d: TypeAlias = _ScalarT | _T | Can[_ScalarT, tuple[()]]

_To1_1d: TypeAlias = CanLen[_ScalarT, tuple[int]] | Sequence[_To1_0d[_ScalarT]]
_To2_1d: TypeAlias = CanLen[_ScalarT, tuple[int]] | Sequence[_To2_0d[_ScalarT, _T]]

_To1_2d: TypeAlias = CanLen[_ScalarT, tuple[int, int]] | Sequence[_To1_1d[_ScalarT]]
_To2_2d: TypeAlias = CanLen[_ScalarT, tuple[int, int]] | Sequence[_To2_1d[_ScalarT, _T]]

_To1_3d: TypeAlias = CanLen[_ScalarT, tuple[int, int, int]] | Sequence[_To1_2d[_ScalarT]]
_To2_3d: TypeAlias = CanLen[_ScalarT, tuple[int, int, int]] | Sequence[_To2_2d[_ScalarT, _T]]

_To1_nd: TypeAlias = CanLen[_ScalarT] | Sequence_nd[CanLen[_ScalarT]]
_To2_nd: TypeAlias = CanLen[_ScalarT] | Sequence_nd[_T | _ScalarT] | Sequence_nd[CanLen[_ScalarT]]

###
# Shaped array aliases

NDim0: TypeAlias = tuple[()]
NDim1: TypeAlias = tuple[int]
NDim2: TypeAlias = tuple[int, int]
NDim3: TypeAlias = tuple[int, int, int]

NDim: TypeAlias = tuple[int, ...]
NDim1p: TypeAlias = tuple[int, Unpack[tuple[int, ...]]]
NDim2p: TypeAlias = tuple[int, int, Unpack[tuple[int, ...]]]
NDim3p: TypeAlias = tuple[int, int, int, Unpack[tuple[int, ...]]]

Array = TypeAliasType("Array", np.ndarray[ShapeC, np.dtype[_ScalarT]], type_params=(_ScalarT, ShapeC))
Array0 = TypeAliasType("Array0", np.ndarray[NDim0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array1 = TypeAliasType("Array1", np.ndarray[NDim1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array2 = TypeAliasType("Array2", np.ndarray[NDim2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array3 = TypeAliasType("Array3", np.ndarray[NDim3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

MArray = TypeAliasType("MArray", np.ma.MaskedArray[ShapeC, np.dtype[_ScalarT]], type_params=(_ScalarT, ShapeC))
MArray0 = TypeAliasType("MArray0", np.ma.MaskedArray[NDim0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray1 = TypeAliasType("MArray1", np.ma.MaskedArray[NDim1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray2 = TypeAliasType("MArray2", np.ma.MaskedArray[NDim2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray3 = TypeAliasType("MArray3", np.ma.MaskedArray[NDim3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

Matrix = TypeAliasType("Matrix", np.matrix[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

###
# Non-overlapping scalar- and array-like aliases for all scalar types.

AsBool = TypeAliasType("AsBool", _To2_0d[np.bool, bool])
AsBool_1d = TypeAliasType("AsBool_1d", _To2_1d[np.bool, bool])
AsBool_2d = TypeAliasType("AsBool_2d", _To2_2d[np.bool, bool])
AsBool_3d = TypeAliasType("AsBool_3d", _To2_3d[np.bool, bool])
AsBool_nd = TypeAliasType("AsBool_nd", _To2_nd[np.bool, bool])

# unsigned integers
AsUInt8 = TypeAliasType("AsUInt8", _To1_0d[np.uint8])
AsUInt8_1d = TypeAliasType("AsUInt8_1d", _To1_1d[np.uint8])
AsUInt8_2d = TypeAliasType("AsUInt8_2d", _To1_2d[np.uint8])
AsUInt8_3d = TypeAliasType("AsUInt8_3d", _To1_3d[np.uint8])
AsUInt8_nd = TypeAliasType("AsUInt8_nd", _To1_nd[np.uint8])

AsUInt16 = TypeAliasType("AsUInt16", _To1_0d[np.uint16])
AsUInt16_1d = TypeAliasType("AsUInt16_1d", _To1_1d[np.uint16])
AsUInt16_2d = TypeAliasType("AsUInt16_2d", _To1_2d[np.uint16])
AsUInt16_3d = TypeAliasType("AsUInt16_3d", _To1_3d[np.uint16])
AsUInt16_nd = TypeAliasType("AsUInt16_nd", _To1_nd[np.uint16])

AsUInt32 = TypeAliasType("AsUInt32", _To1_0d[np.uint32])
AsUInt32_1d = TypeAliasType("AsUInt32_1d", _To1_1d[np.uint32])
AsUInt32_2d = TypeAliasType("AsUInt32_2d", _To1_2d[np.uint32])
AsUInt32_3d = TypeAliasType("AsUInt32_3d", _To1_3d[np.uint32])
AsUInt32_nd = TypeAliasType("AsUInt32_nd", _To1_nd[np.uint32])

AsUInt64 = TypeAliasType("AsUInt64", _To1_0d[np.uint64])
AsUInt64_1d = TypeAliasType("AsUInt64_1d", _To1_1d[np.uint64])
AsUInt64_2d = TypeAliasType("AsUInt64_2d", _To1_2d[np.uint64])
AsUInt64_3d = TypeAliasType("AsUInt64_3d", _To1_3d[np.uint64])
AsUInt64_nd = TypeAliasType("AsUInt64_nd", _To1_nd[np.uint64])

AsULong = TypeAliasType("AsULong", _To1_0d[np.ulong])
AsULong_1d = TypeAliasType("AsULong_1d", _To1_1d[np.ulong])
AsULong_2d = TypeAliasType("AsULong_2d", _To1_2d[np.ulong])
AsULong_3d = TypeAliasType("AsULong_3d", _To1_3d[np.ulong])
AsULong_nd = TypeAliasType("AsULong_nd", _To1_nd[np.ulong])

AsUIntP = TypeAliasType("AsUIntP", _To1_0d[np.uintp])
AsUIntP_1d = TypeAliasType("AsUIntP_1d", _To1_1d[np.uintp])
AsUIntP_2d = TypeAliasType("AsUIntP_2d", _To1_2d[np.uintp])
AsUIntP_3d = TypeAliasType("AsUIntP_3d", _To1_3d[np.uintp])
AsUIntP_nd = TypeAliasType("AsUIntP_nd", _To1_nd[np.uintp])

AsULongLong = TypeAliasType("AsULongLong", _To1_0d[np.ulonglong])
AsULongLong_1d = TypeAliasType("AsULongLong_1d", _To1_1d[np.ulonglong])
AsULongLong_2d = TypeAliasType("AsULongLong_2d", _To1_2d[np.ulonglong])
AsULongLong_3d = TypeAliasType("AsULongLong_3d", _To1_3d[np.ulonglong])
AsULongLong_nd = TypeAliasType("AsULongLong_nd", _To1_nd[np.ulonglong])

AsUInteger = TypeAliasType("AsUInteger", _To1_0d[np.unsignedinteger])
AsUInteger_1d = TypeAliasType("AsUInteger_1d", _To1_1d[np.unsignedinteger])
AsUInteger_2d = TypeAliasType("AsUInteger_2d", _To1_2d[np.unsignedinteger])
AsUInteger_3d = TypeAliasType("AsUInteger_3d", _To1_3d[np.unsignedinteger])
AsUInteger_nd = TypeAliasType("AsUInteger_nd", _To1_nd[np.unsignedinteger])

# signed integers
AsInt8 = TypeAliasType("AsInt8", _To1_0d[np.int8])
AsInt8_1d = TypeAliasType("AsInt8_1d", _To1_1d[np.int8])
AsInt8_2d = TypeAliasType("AsInt8_2d", _To1_2d[np.int8])
AsInt8_3d = TypeAliasType("AsInt8_3d", _To1_3d[np.int8])
AsInt8_nd = TypeAliasType("AsInt8_nd", _To1_nd[np.int8])

AsInt16 = TypeAliasType("AsInt16", _To1_0d[np.int16])
AsInt16_1d = TypeAliasType("AsInt16_1d", _To1_1d[np.int16])
AsInt16_2d = TypeAliasType("AsInt16_2d", _To1_2d[np.int16])
AsInt16_3d = TypeAliasType("AsInt16_3d", _To1_3d[np.int16])
AsInt16_nd = TypeAliasType("AsInt16_nd", _To1_nd[np.int16])

AsInt32 = TypeAliasType("AsInt32", _To1_0d[np.int32])
AsInt32_1d = TypeAliasType("AsInt32_1d", _To1_1d[np.int32])
AsInt32_2d = TypeAliasType("AsInt32_2d", _To1_2d[np.int32])
AsInt32_3d = TypeAliasType("AsInt32_3d", _To1_3d[np.int32])
AsInt32_nd = TypeAliasType("AsInt32_nd", _To1_nd[np.int32])

AsInt64 = TypeAliasType("AsInt64", _To1_0d[np.int64])
AsInt64_1d = TypeAliasType("AsInt64_1d", _To1_1d[np.int64])
AsInt64_2d = TypeAliasType("AsInt64_2d", _To1_2d[np.int64])
AsInt64_3d = TypeAliasType("AsInt64_3d", _To1_3d[np.int64])
AsInt64_nd = TypeAliasType("AsInt64_nd", _To1_nd[np.int64])

AsLong = TypeAliasType("AsLong", _To1_0d[np.long])
AsLong_1d = TypeAliasType("AsLong_1d", _To1_1d[np.long])
AsLong_2d = TypeAliasType("AsLong_2d", _To1_2d[np.long])
AsLong_3d = TypeAliasType("AsLong_3d", _To1_3d[np.long])
AsLong_nd = TypeAliasType("AsLong_nd", _To1_nd[np.long])

AsIntP = TypeAliasType("AsIntP", _To2_0d[np.intp, Is[int]])
AsIntP_1d = TypeAliasType("AsIntP_1d", _To2_1d[np.intp, Is[int]])
AsIntP_2d = TypeAliasType("AsIntP_2d", _To2_2d[np.intp, Is[int]])
AsIntP_3d = TypeAliasType("AsIntP_3d", _To2_3d[np.intp, Is[int]])
AsIntP_nd = TypeAliasType("AsIntP_nd", _To2_nd[np.intp, Is[int]])

AsLongLong = TypeAliasType("AsLongLong", _To1_0d[np.longlong])
AsLongLong_1d = TypeAliasType("AsLongLong_1d", _To1_1d[np.longlong])
AsLongLong_2d = TypeAliasType("AsLongLong_2d", _To1_2d[np.longlong])
AsLongLong_3d = TypeAliasType("AsLongLong_3d", _To1_3d[np.longlong])
AsLongLong_nd = TypeAliasType("AsLongLong_nd", _To1_nd[np.longlong])

AsSInteger = TypeAliasType("AsSInteger", _To2_0d[np.signedinteger, Is[int]])
AsSInteger_1d = TypeAliasType("AsSInteger_1d", _To2_1d[np.signedinteger, Is[int]])
AsSInteger_2d = TypeAliasType("AsSInteger_2d", _To2_2d[np.signedinteger, Is[int]])
AsSInteger_3d = TypeAliasType("AsSInteger_3d", _To2_3d[np.signedinteger, Is[int]])
AsSInteger_nd = TypeAliasType("AsSInteger_nd", _To2_nd[np.signedinteger, Is[int]])

# integers
AsInteger = TypeAliasType("AsInteger", _To2_0d[np.integer, Is[int]])
AsInteger_1d = TypeAliasType("AsInteger_1d", _To2_1d[np.integer, Is[int]])
AsInteger_2d = TypeAliasType("AsInteger_2d", _To2_2d[np.integer, Is[int]])
AsInteger_3d = TypeAliasType("AsInteger_3d", _To2_3d[np.integer, Is[int]])
AsInteger_nd = TypeAliasType("AsInteger_nd", _To2_nd[np.integer, Is[int]])

# real floats
AsFloat16 = TypeAliasType("AsFloat16", _To1_0d[np.float16])
AsFloat16_1d = TypeAliasType("AsFloat16_1d", _To1_1d[np.float16])
AsFloat16_2d = TypeAliasType("AsFloat16_2d", _To1_2d[np.float16])
AsFloat16_3d = TypeAliasType("AsFloat16_3d", _To1_3d[np.float16])
AsFloat16_nd = TypeAliasType("AsFloat16_nd", _To1_nd[np.float16])

AsFloat32 = TypeAliasType("AsFloat32", _To1_0d[np.float32])
AsFloat32_1d = TypeAliasType("AsFloat32_1d", _To1_1d[np.float32])
AsFloat32_2d = TypeAliasType("AsFloat32_2d", _To1_2d[np.float32])
AsFloat32_3d = TypeAliasType("AsFloat32_3d", _To1_3d[np.float32])
AsFloat32_nd = TypeAliasType("AsFloat32_nd", _To1_nd[np.float32])

AsFloat = TypeAliasType("AsFloat", _To2_0d[_AsFloat64, Is[float]])
AsFloat_1d = TypeAliasType("AsFloat_1d", _To2_1d[_AsFloat64, Is[float]])
AsFloat_2d = TypeAliasType("AsFloat_2d", _To2_2d[_AsFloat64, Is[float]])
AsFloat_3d = TypeAliasType("AsFloat_3d", _To2_3d[_AsFloat64, Is[float]])
AsFloat_nd = TypeAliasType("AsFloat_nd", _To2_nd[_AsFloat64, Is[float]])

AsLongDouble = TypeAliasType("AsLongDouble", _To1_0d[np.longdouble])
AsLongDouble_1d = TypeAliasType("AsLongDouble_1d", _To1_1d[np.longdouble])
AsLongDouble_2d = TypeAliasType("AsLongDouble_2d", _To1_2d[np.longdouble])
AsLongDouble_3d = TypeAliasType("AsLongDouble_3d", _To1_3d[np.longdouble])
AsLongDouble_nd = TypeAliasType("AsLongDouble_nd", _To1_nd[np.longdouble])

AsFloating = TypeAliasType("AsFloating", _To2_0d[np.floating, Is[float]])
AsFloating_1d = TypeAliasType("AsFloating_1d", _To2_1d[np.floating, Is[float]])
AsFloating_2d = TypeAliasType("AsFloating_2d", _To2_2d[np.floating, Is[float]])
AsFloating_3d = TypeAliasType("AsFloating_3d", _To2_3d[np.floating, Is[float]])
AsFloating_nd = TypeAliasType("AsFloating_nd", _To2_nd[np.floating, Is[float]])

# complex floats
AsComplex64 = TypeAliasType("AsComplex64", _To1_0d[np.complex64])
AsComplex64_1d = TypeAliasType("AsComplex64_1d", _To1_1d[np.complex64])
AsComplex64_2d = TypeAliasType("AsComplex64_2d", _To1_2d[np.complex64])
AsComplex64_3d = TypeAliasType("AsComplex64_3d", _To1_3d[np.complex64])
AsComplex64_nd = TypeAliasType("AsComplex64_nd", _To1_nd[np.complex64])

AsComplex = TypeAliasType("AsComplex", _To2_0d[_AsComplex128, Is[complex]])
AsComplex_1d = TypeAliasType("AsComplex_1d", _To2_1d[_AsComplex128, Is[complex]])
AsComplex_2d = TypeAliasType("AsComplex_2d", _To2_2d[_AsComplex128, Is[complex]])
AsComplex_3d = TypeAliasType("AsComplex_3d", _To2_3d[_AsComplex128, Is[complex]])
AsComplex_nd = TypeAliasType("AsComplex_nd", _To2_nd[_AsComplex128, Is[complex]])

AsCLongDouble = TypeAliasType("AsCLongDouble", _To1_0d[np.clongdouble])
AsCLongDouble_1d = TypeAliasType("AsCLongDouble_1d", _To1_1d[np.clongdouble])
AsCLongDouble_2d = TypeAliasType("AsCLongDouble_2d", _To1_2d[np.clongdouble])
AsCLongDouble_3d = TypeAliasType("AsCLongDouble_3d", _To1_3d[np.clongdouble])
AsCLongDouble_nd = TypeAliasType("AsCLongDouble_nd", _To1_nd[np.clongdouble])

AsCFloating = TypeAliasType("AsCFloating", _To2_0d[np.complexfloating, Is[complex]])
AsCFloating_1d = TypeAliasType("AsCFloating_1d", _To2_1d[np.complexfloating, Is[complex]])
AsCFloating_2d = TypeAliasType("AsCFloating_2d", _To2_2d[np.complexfloating, Is[complex]])
AsCFloating_3d = TypeAliasType("AsCFloating_3d", _To2_3d[np.complexfloating, Is[complex]])
AsCFloating_nd = TypeAliasType("AsCFloating_nd", _To2_nd[np.complexfloating, Is[complex]])

# integers and real floats
AsReal = TypeAliasType("AsReal", _To2_0d[np.number[Any, float | int], _PyReal])
AsReal_1d = TypeAliasType("AsReal_1d", _To2_1d[np.number[Any, float | int], _PyReal])
AsReal_2d = TypeAliasType("AsReal_2d", _To2_2d[np.number[Any, float | int], _PyReal])
AsReal_3d = TypeAliasType("AsReal_3d", _To2_3d[np.number[Any, float | int], _PyReal])
AsReal_nd = TypeAliasType("AsReal_nd", _To2_nd[np.number[Any, float | int], _PyReal])

# real- and complex floats
AsInexact = TypeAliasType("AsInexact", _To2_0d[np.inexact, _PyInexact])
AsInexact_1d = TypeAliasType("AsInexact_1d", _To2_1d[np.inexact, _PyInexact])
AsInexact_2d = TypeAliasType("AsInexact_2d", _To2_2d[np.inexact, _PyInexact])
AsInexact_3d = TypeAliasType("AsInexact_3d", _To2_3d[np.inexact, _PyInexact])
AsInexact_nd = TypeAliasType("AsInexact_nd", _To2_nd[np.inexact, _PyInexact])

# integers, real- and complex floats
AsNumber = TypeAliasType("AsNumber", _To2_0d[np.number, _PyNumber])
AsNumber_1d = TypeAliasType("AsNumber_1d", _To2_1d[np.number, _PyNumber])
AsNumber_2d = TypeAliasType("AsNumber_2d", _To2_2d[np.number, _PyNumber])
AsNumber_3d = TypeAliasType("AsNumber_3d", _To2_3d[np.number, _PyNumber])
AsNumber_nd = TypeAliasType("AsNumber_nd", _To2_nd[np.number, _PyNumber])

# temporal
AsTimeDelta = TypeAliasType("AsTimeDelta", _To1_0d[np.timedelta64])
AsTimeDelta_1d = TypeAliasType("AsTimeDelta_1d", _To1_1d[np.timedelta64])
AsTimeDelta_2d = TypeAliasType("AsTimeDelta_2d", _To1_2d[np.timedelta64])
AsTimeDelta_3d = TypeAliasType("AsTimeDelta_3d", _To1_3d[np.timedelta64])
AsTimeDelta_nd = TypeAliasType("AsTimeDelta_nd", _To1_nd[np.timedelta64])

AsDateTime = TypeAliasType("AsDateTime", _To1_0d[np.datetime64])
AsDateTime_1d = TypeAliasType("AsDateTime_1d", _To1_1d[np.datetime64])
AsDateTime_2d = TypeAliasType("AsDateTime_2d", _To1_2d[np.datetime64])
AsDateTime_3d = TypeAliasType("AsDateTime_3d", _To1_3d[np.datetime64])
AsDateTime_nd = TypeAliasType("AsDateTime_nd", _To1_nd[np.datetime64])

# fixed strings
AsBytes = TypeAliasType("AsBytes", _To2_0d[np.character[bytes], Is[bytes]])
AsBytes_1d = TypeAliasType("AsBytes_1d", _To2_1d[np.character[bytes], Is[bytes]])
AsBytes_2d = TypeAliasType("AsBytes_2d", _To2_2d[np.character[bytes], Is[bytes]])
AsBytes_3d = TypeAliasType("AsBytes_3d", _To2_3d[np.character[bytes], Is[bytes]])
AsBytes_nd = TypeAliasType("AsBytes_nd", _To2_nd[np.character[bytes], Is[bytes]])

AsStr = TypeAliasType("AsStr", _To2_0d[np.character[str], Is[str]])
AsStr_1d = TypeAliasType("AsStr_1d", _To2_1d[np.character[str], Is[str]])
AsStr_2d = TypeAliasType("AsStr_2d", _To2_2d[np.character[str], Is[str]])
AsStr_3d = TypeAliasType("AsStr_3d", _To2_3d[np.character[str], Is[str]])
AsStr_nd = TypeAliasType("AsStr_nd", _To2_nd[np.character[str], Is[str]])

AsCharacter = TypeAliasType("AsCharacter", _To2_0d[np.character, _PyCharacter])
AsCharacter_1d = TypeAliasType("AsCharacter_1d", _To2_1d[np.character, _PyCharacter])
AsCharacter_2d = TypeAliasType("AsCharacter_2d", _To2_2d[np.character, _PyCharacter])
AsCharacter_3d = TypeAliasType("AsCharacter_3d", _To2_3d[np.character, _PyCharacter])
AsCharacter_nd = TypeAliasType("AsCharacter_nd", _To2_nd[np.character, _PyCharacter])

# python object
AsObject = TypeAliasType("AsObject", _To2_0d[np.object_, _PyObject])
AsObject_1d = TypeAliasType("AsObject_1d", _To2_1d[np.object_, _PyObject])
AsObject_2d = TypeAliasType("AsObject_2d", _To2_2d[np.object_, _PyObject])
AsObject_3d = TypeAliasType("AsObject_3d", _To2_3d[np.object_, _PyObject])
AsObject_nd = TypeAliasType("AsObject_nd", _To2_nd[np.object_, _PyObject])

###
# Coercible (overlapping) scalar- and array-likes

ToBool = TypeAliasType("ToBool", _To2_0d[_ToBool, bool])
ToBool_1d = TypeAliasType("ToBool_1d", _To2_1d[_ToBool, bool])
ToBool_2d = TypeAliasType("ToBool_2d", _To2_2d[_ToBool, bool])
ToBool_3d = TypeAliasType("ToBool_3d", _To2_3d[_ToBool, bool])
ToBool_nd = TypeAliasType("ToBool_nd", _To2_nd[_ToBool, bool])

# signed integers
ToInt8 = TypeAliasType("ToInt8", _To2_0d[_ToInt8, bool])
ToInt8_1d = TypeAliasType("ToInt8_1d", _To2_1d[_ToInt8, bool])
ToInt8_2d = TypeAliasType("ToInt8_2d", _To2_2d[_ToInt8, bool])
ToInt8_3d = TypeAliasType("ToInt8_3d", _To2_3d[_ToInt8, bool])
ToInt8_nd = TypeAliasType("ToInt8_nd", _To2_nd[_ToInt8, bool])

ToInt16 = TypeAliasType("ToInt16", _To2_0d[_ToInt16, bool])
ToInt16_1d = TypeAliasType("ToInt16_1d", _To2_1d[_ToInt16, bool])
ToInt16_2d = TypeAliasType("ToInt16_2d", _To2_2d[_ToInt16, bool])
ToInt16_3d = TypeAliasType("ToInt16_3d", _To2_3d[_ToInt16, bool])
ToInt16_nd = TypeAliasType("ToInt16_nd", _To2_nd[_ToInt16, bool])

ToInt32 = TypeAliasType("ToInt32", _To2_0d[_ToInt32, bool])
ToInt32_1d = TypeAliasType("ToInt32_1d", _To2_1d[_ToInt32, bool])
ToInt32_2d = TypeAliasType("ToInt32_2d", _To2_2d[_ToInt32, bool])
ToInt32_3d = TypeAliasType("ToInt32_3d", _To2_3d[_ToInt32, bool])
ToInt32_nd = TypeAliasType("ToInt32_nd", _To2_nd[_ToInt32, bool])

ToInt64 = TypeAliasType("ToInt64", _To2_0d[_ToInt64, int])
ToInt64_1d = TypeAliasType("ToInt64_1d", _To2_1d[_ToInt64, int])
ToInt64_2d = TypeAliasType("ToInt64_2d", _To2_2d[_ToInt64, int])
ToInt64_3d = TypeAliasType("ToInt64_3d", _To2_3d[_ToInt64, int])
ToInt64_nd = TypeAliasType("ToInt64_nd", _To2_nd[_ToInt64, int])

ToLong = TypeAliasType("ToLong", _To2_0d[_ToLong, bool])
ToLong_1d = TypeAliasType("ToLong_1d", _To2_1d[_ToLong, bool])
ToLong_2d = TypeAliasType("ToLong_2d", _To2_2d[_ToLong, bool])
ToLong_3d = TypeAliasType("ToLong_3d", _To2_3d[_ToLong, bool])
ToLong_nd = TypeAliasType("ToLong_nd", _To2_nd[_ToLong, bool])

ToIntP = TypeAliasType("ToIntP", _To2_0d[_ToIntP, int])
ToIntP_1d = TypeAliasType("ToIntP_1d", _To2_1d[_ToIntP, int])
ToIntP_2d = TypeAliasType("ToIntP_2d", _To2_2d[_ToIntP, int])
ToIntP_3d = TypeAliasType("ToIntP_3d", _To2_3d[_ToIntP, int])
ToIntP_nd = TypeAliasType("ToIntP_nd", _To2_nd[_ToIntP, int])

ToLongLong = TypeAliasType("ToLongLong", _To2_0d[_ToLongLong, int])
ToLongLong_1d = TypeAliasType("ToLongLong_1d", _To2_1d[_ToLongLong, int])
ToLongLong_2d = TypeAliasType("ToLongLong_2d", _To2_2d[_ToLongLong, int])
ToLongLong_3d = TypeAliasType("ToLongLong_3d", _To2_3d[_ToLongLong, int])
ToLongLong_nd = TypeAliasType("ToLongLong_nd", _To2_nd[_ToLongLong, int])

# unsigned integers
ToUInt8 = TypeAliasType("ToUInt8", _To2_0d[_ToUInt8, bool])
ToUInt8_1d = TypeAliasType("ToUInt8_1d", _To2_1d[_ToUInt8, bool])
ToUInt8_2d = TypeAliasType("ToUInt8_2d", _To2_2d[_ToUInt8, bool])
ToUInt8_3d = TypeAliasType("ToUInt8_3d", _To2_3d[_ToUInt8, bool])
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _To2_nd[_ToUInt8, bool])

ToUInt16 = TypeAliasType("ToUInt16", _To2_0d[_ToUInt16, bool])
ToUInt16_1d = TypeAliasType("ToUInt16_1d", _To2_1d[_ToUInt16, bool])
ToUInt16_2d = TypeAliasType("ToUInt16_2d", _To2_2d[_ToUInt16, bool])
ToUInt16_3d = TypeAliasType("ToUInt16_3d", _To2_3d[_ToUInt16, bool])
ToUInt16_nd = TypeAliasType("ToUInt16_nd", _To2_nd[_ToUInt16, bool])

ToUInt32 = TypeAliasType("ToUInt32", _To2_0d[_ToUInt32, bool])
ToUInt32_1d = TypeAliasType("ToUInt32_1d", _To2_1d[_ToUInt32, bool])
ToUInt32_2d = TypeAliasType("ToUInt32_2d", _To2_2d[_ToUInt32, bool])
ToUInt32_3d = TypeAliasType("ToUInt32_3d", _To2_3d[_ToUInt32, bool])
ToUInt32_nd = TypeAliasType("ToUInt32_nd", _To2_nd[_ToUInt32, bool])

ToUInt64 = TypeAliasType("ToUInt64", _To2_0d[_ToUInt64, bool])
ToUInt64_1d = TypeAliasType("ToUInt64_1d", _To2_1d[_ToUInt64, bool])
ToUInt64_2d = TypeAliasType("ToUInt64_2d", _To2_2d[_ToUInt64, bool])
ToUInt64_3d = TypeAliasType("ToUInt64_3d", _To2_3d[_ToUInt64, bool])
ToUInt64_nd = TypeAliasType("ToUInt64_nd", _To2_nd[_ToUInt64, bool])

ToULong = TypeAliasType("ToULong", _To2_0d[_ToULong, bool])
ToULong_1d = TypeAliasType("ToULong_1d", _To2_1d[_ToULong, bool])
ToULong_2d = TypeAliasType("ToULong_2d", _To2_2d[_ToULong, bool])
ToULong_3d = TypeAliasType("ToULong_3d", _To2_3d[_ToULong, bool])
ToULong_nd = TypeAliasType("ToULong_nd", _To2_nd[_ToULong, bool])

ToUIntP = TypeAliasType("ToUIntP", _To2_0d[_ToUIntP, bool])
ToUIntP_1d = TypeAliasType("ToUIntP_1d", _To2_1d[_ToUIntP, bool])
ToUIntP_2d = TypeAliasType("ToUIntP_2d", _To2_2d[_ToUIntP, bool])
ToUIntP_3d = TypeAliasType("ToUIntP_3d", _To2_3d[_ToUIntP, bool])
ToUIntP_nd = TypeAliasType("ToUIntP_nd", _To2_nd[_ToUIntP, bool])

ToULongLong = TypeAliasType("ToULongLong", _To2_0d[_ToULongLong, bool])
ToULongLong_1d = TypeAliasType("ToULongLong_1d", _To2_1d[_ToULongLong, bool])
ToULongLong_2d = TypeAliasType("ToULongLong_2d", _To2_2d[_ToULongLong, bool])
ToULongLong_3d = TypeAliasType("ToULongLong_3d", _To2_3d[_ToULongLong, bool])
ToULongLong_nd = TypeAliasType("ToULongLong_nd", _To2_nd[_ToULongLong, bool])

# real floats
ToFloat16 = TypeAliasType("ToFloat16", _To2_0d[_ToFloat16, bool])
ToFloat16_1d = TypeAliasType("ToFloat16_1d", _To2_1d[_ToFloat16, bool])
ToFloat16_2d = TypeAliasType("ToFloat16_2d", _To2_2d[_ToFloat16, bool])
ToFloat16_3d = TypeAliasType("ToFloat16_3d", _To2_3d[_ToFloat16, bool])
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _To2_nd[_ToFloat16, bool])

ToFloat32 = TypeAliasType("ToFloat32", _To2_0d[_ToFloat32, bool])
ToFloat32_1d = TypeAliasType("ToFloat32_1d", _To2_1d[_ToFloat32, bool])
ToFloat32_2d = TypeAliasType("ToFloat32_2d", _To2_2d[_ToFloat32, bool])
ToFloat32_3d = TypeAliasType("ToFloat32_3d", _To2_3d[_ToFloat32, bool])
ToFloat32_nd = TypeAliasType("ToFloat32_nd", _To2_nd[_ToFloat32, bool])

ToFloat64 = TypeAliasType("ToFloat64", _To2_0d[_ToFloat64, float])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _To2_1d[_ToFloat64, float])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _To2_2d[_ToFloat64, float])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _To2_3d[_ToFloat64, float])
ToFloat64_nd = TypeAliasType("ToFloat64_nd", _To2_nd[_ToFloat64, float])

ToFloating = TypeAliasType("ToFloating", _To2_0d[_ToFloating, float])
ToFloating_1d = TypeAliasType("ToFloating_1d", _To2_1d[_ToFloating, float])
ToFloating_2d = TypeAliasType("ToFloating_2d", _To2_2d[_ToFloating, float])
ToFloating_3d = TypeAliasType("ToFloating_3d", _To2_3d[_ToFloating, float])
ToFloating_nd = TypeAliasType("ToFloating_nd", _To2_nd[_ToFloating, float])

# complex floats
ToComplex64 = TypeAliasType("ToComplex64", _To2_0d[_ToComplex64, bool])
ToComplex64_1d = TypeAliasType("ToComplex64_1d", _To2_1d[_ToComplex64, bool])
ToComplex64_2d = TypeAliasType("ToComplex64_2d", _To2_2d[_ToComplex64, bool])
ToComplex64_3d = TypeAliasType("ToComplex64_3d", _To2_3d[_ToComplex64, bool])
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _To2_nd[_ToComplex64, bool])

ToComplex128 = TypeAliasType("ToComplex128", _To2_0d[_ToComplex128, complex])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _To2_1d[_ToComplex128, complex])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _To2_2d[_ToComplex128, complex])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _To2_3d[_ToComplex128, complex])
ToComplex128_nd = TypeAliasType("ToComplex128_nd", _To2_nd[_ToComplex128, complex])

ToComplexFloating = TypeAliasType("ToComplexFloating", _To2_0d[_ToNumber, complex])
ToComplexFloating_1d = TypeAliasType("ToComplexFloating_1d", _To2_1d[_ToNumber, complex])
ToComplexFloating_2d = TypeAliasType("ToComplexFloating_2d", _To2_2d[_ToNumber, complex])
ToComplexFloating_3d = TypeAliasType("ToComplexFloating_3d", _To2_3d[_ToNumber, complex])
ToComplexFloating_nd = TypeAliasType("ToComplexFloating_nd", _To2_nd[_ToNumber, complex])

ToTimeDelta = TypeAliasType("ToTimeDelta", _To2_0d[_ToTimeDelta, int])
ToTimeDelta_1d = TypeAliasType("ToTimeDelta_1d", _To2_1d[_ToTimeDelta, int])
ToTimeDelta_2d = TypeAliasType("ToTimeDelta_2d", _To2_2d[_ToTimeDelta, int])
ToTimeDelta_3d = TypeAliasType("ToTimeDelta_3d", _To2_3d[_ToTimeDelta, int])
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _To2_nd[_ToTimeDelta, int])

ToDateTime = TypeAliasType("ToDateTime", _To1_0d[_ToDateTime])
ToDateTime_1d = TypeAliasType("ToDateTime_1d", _To1_1d[_ToDateTime])
ToDateTime_2d = TypeAliasType("ToDateTime_2d", _To1_2d[_ToDateTime])
ToDateTime_3d = TypeAliasType("ToDateTime_3d", _To1_3d[_ToDateTime])
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _To1_nd[_ToDateTime])

ToBytes = TypeAliasType("ToBytes", _To2_0d[_ToBytes, Is[bytes]])
ToBytes_1d = TypeAliasType("ToBytes_1d", _To2_1d[_ToBytes, Is[bytes]])
ToBytes_2d = TypeAliasType("ToBytes_2d", _To2_2d[_ToBytes, Is[bytes]])
ToBytes_3d = TypeAliasType("ToBytes_3d", _To2_3d[_ToBytes, Is[bytes]])
ToBytes_nd = TypeAliasType("ToBytes_nd", _To2_nd[_ToBytes, Is[bytes]])

ToStr = TypeAliasType("ToStr", _To2_0d[_ToStr, _PyCharacter])
ToStr_1d = TypeAliasType("ToStr_1d", _To2_1d[_ToStr, _PyCharacter])
ToStr_2d = TypeAliasType("ToStr_2d", _To2_2d[_ToStr, _PyCharacter])
ToStr_3d = TypeAliasType("ToStr_3d", _To2_3d[_ToStr, _PyCharacter])
ToStr_nd = TypeAliasType("ToStr_nd", _To2_nd[_ToStr, _PyCharacter])

ToGeneric = TypeAliasType("ToGeneric", _To2_0d[_ToObject, object])
ToGeneric_1d = TypeAliasType("ToGeneric_1d", _To2_1d[_ToObject, object])
ToGeneric_2d = TypeAliasType("ToGeneric_2d", _To2_2d[_ToObject, object])
ToGeneric_3d = TypeAliasType("ToGeneric_3d", _To2_3d[_ToObject, object])
ToGeneric_nd = TypeAliasType("ToGeneric_nd", _To2_nd[_ToObject, object])

###
# `npt.ND` variant with (optional) 2nd shape-typing parameter

ScalarLike = TypeAliasType("ScalarLike", _To2_0d[np.generic[ItemC], ItemC], type_params=(ItemC,))
ArrayLike = TypeAliasType("ArrayLike", _To2_nd[np.generic[ItemC], ItemC], type_params=(ItemC,))
ArrayLike1D = TypeAliasType("ArrayLike1D", _To2_1d[np.generic[ItemC], ItemC], type_params=(ItemC,))
ArrayLike2D = TypeAliasType("ArrayLike2D", _To2_2d[np.generic[ItemC], ItemC], type_params=(ItemC,))
ArrayLike3D = TypeAliasType("ArrayLike3D", _To2_3d[np.generic[ItemC], ItemC], type_params=(ItemC,))

###
# DType-likes
# TODO
