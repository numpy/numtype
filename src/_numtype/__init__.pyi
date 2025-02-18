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

AtLeast0D: TypeAlias = tuple[int, ...]
AtLeast1D = TypeAliasType("AtLeast1D", tuple[int, Unpack[tuple[int, ...]]])
AtLeast2D = TypeAliasType("AtLeast2D", tuple[int, int, Unpack[tuple[int, ...]]])
AtLeast3D = TypeAliasType("AtLeast3D", tuple[int, int, int, Unpack[tuple[int, ...]]])
AtLeast4D = TypeAliasType("AtLeast4D", tuple[int, int, int, int, Unpack[tuple[int, ...]]])

###
# Shape-typed sequences

# A slimmed down version of `_NestedSequence`, based on `optype.numpy.SequenceND`.
# https://github.com/jorenham/optype
@type_check_only
class Sequence_nd(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | Sequence_nd[_T_co]: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

# we can't use a custom Sequence type due to some mypy bug
Sequence_2d: TypeAlias = Sequence[Sequence[_T]]
Sequence_3d: TypeAlias = Sequence[Sequence_2d[_T]]

# nested sequences with at least k dims, e.g. `2nd` denotes a dimensionality in the interval [2, n]
Sequence_1nd: TypeAlias = Sequence_nd[_T]
Sequence_2nd: TypeAlias = Sequence[Sequence_nd[_T]]
Sequence_3nd: TypeAlias = Sequence[Sequence_2nd[_T]]
Sequence_4nd: TypeAlias = Sequence[Sequence_3nd[_T]]

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

_ToArray_nd: TypeAlias = CanArray[_ScalarT] | _ToT | Sequence_nd[_ToT | _ScalarT] | Sequence_nd[CanArray[_ScalarT]]
_ToArray_0d = TypeAliasType("_ToArray_0d", _ToT | CanArray[_ScalarT, tuple[()]], type_params=(_ScalarT, _ToT))

# don't require matching shape-types by default
_ToArray_1d: TypeAlias = CanArraySized[_ScalarT] | Sequence[_ToArray_0d[_ScalarT, _ToT]]
_ToArray_2d: TypeAlias = CanArraySized[_ScalarT] | Sequence[_ToArray_1d[_ScalarT, _ToT]]
_ToArray_3d: TypeAlias = CanArraySized[_ScalarT] | Sequence[_ToArray_2d[_ScalarT, _ToT]]

# requires ndarray to be shape-types (the `s` suffix stands for "strict")
_ToArray_1ds: TypeAlias = CanArraySized[_ScalarT, tuple[int]] | Sequence[_ToArray_0d[_ScalarT, _ToT]]
_ToArray_2ds: TypeAlias = CanArraySized[_ScalarT, tuple[int, int]] | Sequence[_ToArray_1ds[_ScalarT, _ToT]]
_ToArray_3ds: TypeAlias = CanArraySized[_ScalarT, tuple[int, int, int]] | Sequence[_ToArray_2ds[_ScalarT, _ToT]]

# requires a lower bound on dimensionality, e.g. `_2nd` denotes `ndin` within `[2, n]`
_ToArray_1nd: TypeAlias = CanArraySized[_ScalarT] | Sequence_nd[_ToT | _ScalarT] | Sequence_nd[CanArray[_ScalarT]]
_ToArray_2nd: TypeAlias = CanArraySized[_ScalarT, AtLeast2D] | Sequence[_ToArray_1nd[_ScalarT, _ToT]]
_ToArray_3nd: TypeAlias = CanArraySized[_ScalarT, AtLeast3D] | Sequence[_ToArray_2nd[_ScalarT, _ToT]]

###
# Non-overlapping scalar- and array-like aliases for all scalar types.

# bool
_ToBool: TypeAlias = np.bool[Any]
ToBool_nd = TypeAliasType("ToBool_nd", _ToArray_nd[_ToBool, bool])
ToBool_0d = TypeAliasType("ToBool_0d", _ToArray_0d[_ToBool, bool])
ToBool_1d = TypeAliasType("ToBool_1d", _ToArray_1d[_ToBool, bool])
ToBool_2d = TypeAliasType("ToBool_2d", _ToArray_2d[_ToBool, bool])
ToBool_3d = TypeAliasType("ToBool_3d", _ToArray_3d[_ToBool, bool])
ToBool_1ds = TypeAliasType("ToBool_1ds", _ToArray_1ds[_ToBool, bool])
ToBool_2ds = TypeAliasType("ToBool_2ds", _ToArray_2ds[_ToBool, bool])
ToBool_3ds = TypeAliasType("ToBool_3ds", _ToArray_3ds[_ToBool, bool])
ToBool_1nd = TypeAliasType("ToBool_1nd", _ToArray_1nd[_ToBool, bool])
ToBool_2nd = TypeAliasType("ToBool_2nd", _ToArray_2nd[_ToBool, bool])
ToBool_3nd = TypeAliasType("ToBool_3nd", _ToArray_3nd[_ToBool, bool])

# unsigned integers
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _ToArray_nd[np.uint8])
ToUInt8_0d = TypeAliasType("ToUInt8_0d", _ToArray_0d[np.uint8])
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
ToUInt16_0d = TypeAliasType("ToUInt16_0d", _ToArray_0d[np.uint16])
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
ToUInt32_0d = TypeAliasType("ToUInt32_0d", _ToArray_0d[np.uint32])
ToUInt32_1d = TypeAliasType("ToUInt32_1d", _ToArray_1d[np.uint32])
ToUInt32_2d = TypeAliasType("ToUInt32_2d", _ToArray_2d[np.uint32])
ToUInt32_3d = TypeAliasType("ToUInt32_3d", _ToArray_3d[np.uint32])
ToUInt32_1ds = TypeAliasType("ToUInt32_1ds", _ToArray_1ds[np.uint32])
ToUInt32_2ds = TypeAliasType("ToUInt32_2ds", _ToArray_2ds[np.uint32])
ToUInt32_3ds = TypeAliasType("ToUInt32_3ds", _ToArray_3ds[np.uint32])
ToUInt32_1nd = TypeAliasType("ToUInt32_1nd", _ToArray_1nd[np.uint32])
ToUInt32_2nd = TypeAliasType("ToUInt32_2nd", _ToArray_2nd[np.uint32])
ToUInt32_3nd = TypeAliasType("ToUInt32_3nd", _ToArray_3nd[np.uint32])

ToUInt64_nd = TypeAliasType("ToUInt64_nd", _ToArray_nd[np.uint64])
ToUInt64_0d = TypeAliasType("ToUInt64_0d", _ToArray_0d[np.uint64])
ToUInt64_1d = TypeAliasType("ToUInt64_1d", _ToArray_1d[np.uint64])
ToUInt64_2d = TypeAliasType("ToUInt64_2d", _ToArray_2d[np.uint64])
ToUInt64_3d = TypeAliasType("ToUInt64_3d", _ToArray_3d[np.uint64])
ToUInt64_1ds = TypeAliasType("ToUInt64_1ds", _ToArray_1ds[np.uint64])
ToUInt64_2ds = TypeAliasType("ToUInt64_2ds", _ToArray_2ds[np.uint64])
ToUInt64_3ds = TypeAliasType("ToUInt64_3ds", _ToArray_3ds[np.uint64])
ToUInt64_1nd = TypeAliasType("ToUInt64_1nd", _ToArray_1nd[np.uint64])
ToUInt64_2nd = TypeAliasType("ToUInt64_2nd", _ToArray_2nd[np.uint64])
ToUInt64_3nd = TypeAliasType("ToUInt64_3nd", _ToArray_3nd[np.uint64])

ToULong_nd = TypeAliasType("ToULong_nd", _ToArray_nd[np.ulong])
ToULong_0d = TypeAliasType("ToULong_0d", _ToArray_0d[np.ulong])
ToULong_1d = TypeAliasType("ToULong_1d", _ToArray_1d[np.ulong])
ToULong_2d = TypeAliasType("ToULong_2d", _ToArray_2d[np.ulong])
ToULong_3d = TypeAliasType("ToULong_3d", _ToArray_3d[np.ulong])
ToULong_1ds = TypeAliasType("ToULong_1ds", _ToArray_1ds[np.ulong])
ToULong_2ds = TypeAliasType("ToULong_2ds", _ToArray_2ds[np.ulong])
ToULong_3ds = TypeAliasType("ToULong_3ds", _ToArray_3ds[np.ulong])
ToULong_1nd = TypeAliasType("ToULong_1nd", _ToArray_1nd[np.ulong])
ToULong_2nd = TypeAliasType("ToULong_2nd", _ToArray_2nd[np.ulong])
ToULong_3nd = TypeAliasType("ToULong_3nd", _ToArray_3nd[np.ulong])

ToUIntP_nd = TypeAliasType("ToUIntP_nd", _ToArray_nd[np.uintp])
ToUIntP_0d = TypeAliasType("ToUIntP_0d", _ToArray_0d[np.uintp])
ToUIntP_1d = TypeAliasType("ToUIntP_1d", _ToArray_1d[np.uintp])
ToUIntP_2d = TypeAliasType("ToUIntP_2d", _ToArray_2d[np.uintp])
ToUIntP_3d = TypeAliasType("ToUIntP_3d", _ToArray_3d[np.uintp])
ToUIntP_1ds = TypeAliasType("ToUIntP_1ds", _ToArray_1ds[np.uintp])
ToUIntP_2ds = TypeAliasType("ToUIntP_2ds", _ToArray_2ds[np.uintp])
ToUIntP_3ds = TypeAliasType("ToUIntP_3ds", _ToArray_3ds[np.uintp])
ToUIntP_1nd = TypeAliasType("ToUIntP_1nd", _ToArray_1nd[np.uintp])
ToUIntP_2nd = TypeAliasType("ToUIntP_2nd", _ToArray_2nd[np.uintp])
ToUIntP_3nd = TypeAliasType("ToUIntP_3nd", _ToArray_3nd[np.uintp])

ToULongLong_nd = TypeAliasType("ToULongLong_nd", _ToArray_nd[np.ulonglong])
ToULongLong_0d = TypeAliasType("ToULongLong_0d", _ToArray_0d[np.ulonglong])
ToULongLong_1d = TypeAliasType("ToULongLong_1d", _ToArray_1d[np.ulonglong])
ToULongLong_2d = TypeAliasType("ToULongLong_2d", _ToArray_2d[np.ulonglong])
ToULongLong_3d = TypeAliasType("ToULongLong_3d", _ToArray_3d[np.ulonglong])
ToULongLong_1ds = TypeAliasType("ToULongLong_1ds", _ToArray_1ds[np.ulonglong])
ToULongLong_2ds = TypeAliasType("ToULongLong_2ds", _ToArray_2ds[np.ulonglong])
ToULongLong_3ds = TypeAliasType("ToULongLong_3ds", _ToArray_3ds[np.ulonglong])
ToULongLong_1nd = TypeAliasType("ToULongLong_1nd", _ToArray_1nd[np.ulonglong])
ToULongLong_2nd = TypeAliasType("ToULongLong_2nd", _ToArray_2nd[np.ulonglong])
ToULongLong_3nd = TypeAliasType("ToULongLong_3nd", _ToArray_3nd[np.ulonglong])

ToUInteger_nd = TypeAliasType("ToUInteger_nd", _ToArray_nd[np.unsignedinteger])
ToUInteger_0d = TypeAliasType("ToUInteger_0d", _ToArray_0d[np.unsignedinteger])
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
ToInt8_0d = TypeAliasType("ToInt8_0d", _ToArray_0d[np.int8])
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
ToInt16_0d = TypeAliasType("ToInt16_0d", _ToArray_0d[np.int16])
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
ToInt32_0d = TypeAliasType("ToInt32_0d", _ToArray_0d[np.int32])
ToInt32_1d = TypeAliasType("ToInt32_1d", _ToArray_1d[np.int32])
ToInt32_2d = TypeAliasType("ToInt32_2d", _ToArray_2d[np.int32])
ToInt32_3d = TypeAliasType("ToInt32_3d", _ToArray_3d[np.int32])
ToInt32_1ds = TypeAliasType("ToInt32_1ds", _ToArray_1ds[np.int32])
ToInt32_2ds = TypeAliasType("ToInt32_2ds", _ToArray_2ds[np.int32])
ToInt32_3ds = TypeAliasType("ToInt32_3ds", _ToArray_3ds[np.int32])
ToInt32_1nd = TypeAliasType("ToInt32_1nd", _ToArray_1nd[np.int32])
ToInt32_2nd = TypeAliasType("ToInt32_2nd", _ToArray_2nd[np.int32])
ToInt32_3nd = TypeAliasType("ToInt32_3nd", _ToArray_3nd[np.int32])

ToInt64_nd = TypeAliasType("ToInt64_nd", _ToArray_nd[np.int64])
ToInt64_0d = TypeAliasType("ToInt64_0d", _ToArray_0d[np.int64])
ToInt64_1d = TypeAliasType("ToInt64_1d", _ToArray_1d[np.int64])
ToInt64_2d = TypeAliasType("ToInt64_2d", _ToArray_2d[np.int64])
ToInt64_3d = TypeAliasType("ToInt64_3d", _ToArray_3d[np.int64])
ToInt64_1ds = TypeAliasType("ToInt64_1ds", _ToArray_1ds[np.int64])
ToInt64_2ds = TypeAliasType("ToInt64_2ds", _ToArray_2ds[np.int64])
ToInt64_3ds = TypeAliasType("ToInt64_3ds", _ToArray_3ds[np.int64])
ToInt64_1nd = TypeAliasType("ToInt64_1nd", _ToArray_1nd[np.int64])
ToInt64_2nd = TypeAliasType("ToInt64_2nd", _ToArray_2nd[np.int64])
ToInt64_3nd = TypeAliasType("ToInt64_3nd", _ToArray_3nd[np.int64])

ToLong_nd = TypeAliasType("ToLong_nd", _ToArray_nd[np.long])
ToLong_0d = TypeAliasType("ToLong_0d", _ToArray_0d[np.long])
ToLong_1d = TypeAliasType("ToLong_1d", _ToArray_1d[np.long])
ToLong_2d = TypeAliasType("ToLong_2d", _ToArray_2d[np.long])
ToLong_3d = TypeAliasType("ToLong_3d", _ToArray_3d[np.long])
ToLong_1ds = TypeAliasType("ToLong_1ds", _ToArray_1ds[np.long])
ToLong_2ds = TypeAliasType("ToLong_2ds", _ToArray_2ds[np.long])
ToLong_3ds = TypeAliasType("ToLong_3ds", _ToArray_3ds[np.long])
ToLong_1nd = TypeAliasType("ToLong_1nd", _ToArray_1nd[np.long])
ToLong_2nd = TypeAliasType("ToLong_2nd", _ToArray_2nd[np.long])
ToLong_3nd = TypeAliasType("ToLong_3nd", _ToArray_3nd[np.long])

_ToIntP: TypeAlias = np.intp | Is[int]
ToIntP_nd = TypeAliasType("ToIntP_nd", _ToArray_nd[np.intp, _ToIntP])
ToIntP_0d = TypeAliasType("ToIntP_0d", _ToArray_0d[np.intp, _ToIntP])
ToIntP_1d = TypeAliasType("ToIntP_1d", _ToArray_1d[np.intp, _ToIntP])
ToIntP_2d = TypeAliasType("ToIntP_2d", _ToArray_2d[np.intp, _ToIntP])
ToIntP_3d = TypeAliasType("ToIntP_3d", _ToArray_3d[np.intp, _ToIntP])
ToIntP_1ds = TypeAliasType("ToIntP_1ds", _ToArray_1ds[np.intp, _ToIntP])
ToIntP_2ds = TypeAliasType("ToIntP_2ds", _ToArray_2ds[np.intp, _ToIntP])
ToIntP_3ds = TypeAliasType("ToIntP_3ds", _ToArray_3ds[np.intp, _ToIntP])
ToIntP_1nd = TypeAliasType("ToIntP_1nd", _ToArray_1nd[np.intp, _ToIntP])
ToIntP_2nd = TypeAliasType("ToIntP_2nd", _ToArray_2nd[np.intp, _ToIntP])
ToIntP_3nd = TypeAliasType("ToIntP_3nd", _ToArray_3nd[np.intp, _ToIntP])

ToLongLong_nd = TypeAliasType("ToLongLong_nd", _ToArray_nd[np.longlong])
ToLongLong_0d = TypeAliasType("ToLongLong_0d", _ToArray_0d[np.longlong])
ToLongLong_1d = TypeAliasType("ToLongLong_1d", _ToArray_1d[np.longlong])
ToLongLong_2d = TypeAliasType("ToLongLong_2d", _ToArray_2d[np.longlong])
ToLongLong_3d = TypeAliasType("ToLongLong_3d", _ToArray_3d[np.longlong])
ToLongLong_1ds = TypeAliasType("ToLongLong_1ds", _ToArray_1ds[np.longlong])
ToLongLong_2ds = TypeAliasType("ToLongLong_2ds", _ToArray_2ds[np.longlong])
ToLongLong_3ds = TypeAliasType("ToLongLong_3ds", _ToArray_3ds[np.longlong])
ToLongLong_1nd = TypeAliasType("ToLongLong_1nd", _ToArray_1nd[np.longlong])
ToLongLong_2nd = TypeAliasType("ToLongLong_2nd", _ToArray_2nd[np.longlong])
ToLongLong_3nd = TypeAliasType("ToLongLong_3nd", _ToArray_3nd[np.longlong])

_ToInteger: TypeAlias = np.signedinteger | Is[int]
ToSInteger_nd = TypeAliasType("ToSInteger_nd", _ToArray_nd[np.signedinteger, _ToInteger])
ToSInteger_0d = TypeAliasType("ToSInteger_0d", _ToArray_0d[np.signedinteger, _ToInteger])
ToSInteger_1d = TypeAliasType("ToSInteger_1d", _ToArray_1d[np.signedinteger, _ToInteger])
ToSInteger_2d = TypeAliasType("ToSInteger_2d", _ToArray_2d[np.signedinteger, _ToInteger])
ToSInteger_3d = TypeAliasType("ToSInteger_3d", _ToArray_3d[np.signedinteger, _ToInteger])
ToSInteger_1ds = TypeAliasType("ToSInteger_1ds", _ToArray_1ds[np.signedinteger, _ToInteger])
ToSInteger_2ds = TypeAliasType("ToSInteger_2ds", _ToArray_2ds[np.signedinteger, _ToInteger])
ToSInteger_3ds = TypeAliasType("ToSInteger_3ds", _ToArray_3ds[np.signedinteger, _ToInteger])
ToSInteger_1nd = TypeAliasType("ToSInteger_1nd", _ToArray_1nd[np.signedinteger, _ToInteger])
ToSInteger_2nd = TypeAliasType("ToSInteger_2nd", _ToArray_2nd[np.signedinteger, _ToInteger])
ToSInteger_3nd = TypeAliasType("ToSInteger_3nd", _ToArray_3nd[np.signedinteger, _ToInteger])

# integers
ToInteger_nd = TypeAliasType("ToInteger_nd", _ToArray_nd[np.integer, Is[int]])
ToInteger_0d = TypeAliasType("ToInteger_0d", _ToArray_0d[np.integer, Is[int]])
ToInteger_1d = TypeAliasType("ToInteger_1d", _ToArray_1d[np.integer, Is[int]])
ToInteger_2d = TypeAliasType("ToInteger_2d", _ToArray_2d[np.integer, Is[int]])
ToInteger_3d = TypeAliasType("ToInteger_3d", _ToArray_3d[np.integer, Is[int]])
ToInteger_1ds = TypeAliasType("ToInteger_1ds", _ToArray_1ds[np.integer, Is[int]])
ToInteger_2ds = TypeAliasType("ToInteger_2ds", _ToArray_2ds[np.integer, Is[int]])
ToInteger_3ds = TypeAliasType("ToInteger_3ds", _ToArray_3ds[np.integer, Is[int]])
ToInteger_1nd = TypeAliasType("ToInteger_1nd", _ToArray_1nd[np.integer, Is[int]])
ToInteger_2nd = TypeAliasType("ToInteger_2nd", _ToArray_2nd[np.integer, Is[int]])
ToInteger_3nd = TypeAliasType("ToInteger_3nd", _ToArray_3nd[np.integer, Is[int]])

# real floats
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _ToArray_nd[np.float16])
ToFloat16_0d = TypeAliasType("ToFloat16_0d", _ToArray_0d[np.float16])
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
ToFloat32_0d = TypeAliasType("ToFloat32_0d", _ToArray_0d[np.float32])
ToFloat32_1d = TypeAliasType("ToFloat32_1d", _ToArray_1d[np.float32])
ToFloat32_2d = TypeAliasType("ToFloat32_2d", _ToArray_2d[np.float32])
ToFloat32_3d = TypeAliasType("ToFloat32_3d", _ToArray_3d[np.float32])
ToFloat32_1ds = TypeAliasType("ToFloat32_1ds", _ToArray_1ds[np.float32])
ToFloat32_2ds = TypeAliasType("ToFloat32_2ds", _ToArray_2ds[np.float32])
ToFloat32_3ds = TypeAliasType("ToFloat32_3ds", _ToArray_3ds[np.float32])
ToFloat32_1nd = TypeAliasType("ToFloat32_1nd", _ToArray_1nd[np.float32])
ToFloat32_2nd = TypeAliasType("ToFloat32_2nd", _ToArray_2nd[np.float32])
ToFloat32_3nd = TypeAliasType("ToFloat32_3nd", _ToArray_3nd[np.float32])

_ToFloat64: TypeAlias = np.floating[_64Bit]
ToFloat64_nd = TypeAliasType("ToFloat64_nd", _ToArray_nd[_ToFloat64, Is[float]])
ToFloat64_0d = TypeAliasType("ToFloat64_0d", _ToArray_0d[_ToFloat64, Is[float]])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _ToArray_1d[_ToFloat64, Is[float]])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _ToArray_2d[_ToFloat64, Is[float]])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _ToArray_3d[_ToFloat64, Is[float]])
ToFloat64_1ds = TypeAliasType("ToFloat64_1ds", _ToArray_1ds[_ToFloat64, Is[float]])
ToFloat64_2ds = TypeAliasType("ToFloat64_2ds", _ToArray_2ds[_ToFloat64, Is[float]])
ToFloat64_3ds = TypeAliasType("ToFloat64_3ds", _ToArray_3ds[_ToFloat64, Is[float]])
ToFloat64_1nd = TypeAliasType("ToFloat64_1nd", _ToArray_1nd[_ToFloat64, Is[float]])
ToFloat64_2nd = TypeAliasType("ToFloat64_2nd", _ToArray_2nd[_ToFloat64, Is[float]])
ToFloat64_3nd = TypeAliasType("ToFloat64_3nd", _ToArray_3nd[_ToFloat64, Is[float]])

ToLongDouble_nd = TypeAliasType("ToLongDouble_nd", _ToArray_nd[np.longdouble])
ToLongDouble_0d = TypeAliasType("ToLongDouble_0d", _ToArray_0d[np.longdouble])
ToLongDouble_1d = TypeAliasType("ToLongDouble_1d", _ToArray_1d[np.longdouble])
ToLongDouble_2d = TypeAliasType("ToLongDouble_2d", _ToArray_2d[np.longdouble])
ToLongDouble_3d = TypeAliasType("ToLongDouble_3d", _ToArray_3d[np.longdouble])
ToLongDouble_1ds = TypeAliasType("ToLongDouble_1ds", _ToArray_1ds[np.longdouble])
ToLongDouble_2ds = TypeAliasType("ToLongDouble_2ds", _ToArray_2ds[np.longdouble])
ToLongDouble_3ds = TypeAliasType("ToLongDouble_3ds", _ToArray_3ds[np.longdouble])
ToLongDouble_1nd = TypeAliasType("ToLongDouble_1nd", _ToArray_1nd[np.longdouble])
ToLongDouble_2nd = TypeAliasType("ToLongDouble_2nd", _ToArray_2nd[np.longdouble])
ToLongDouble_3nd = TypeAliasType("ToLongDouble_3nd", _ToArray_3nd[np.longdouble])

ToFloating_nd = TypeAliasType("ToFloating_nd", _ToArray_nd[np.floating, Is[float]])
ToFloating_0d = TypeAliasType("ToFloating_0d", _ToArray_0d[np.floating, Is[float]])
ToFloating_1d = TypeAliasType("ToFloating_1d", _ToArray_1d[np.floating, Is[float]])
ToFloating_2d = TypeAliasType("ToFloating_2d", _ToArray_2d[np.floating, Is[float]])
ToFloating_3d = TypeAliasType("ToFloating_3d", _ToArray_3d[np.floating, Is[float]])
ToFloating_1ds = TypeAliasType("ToFloating_1ds", _ToArray_1ds[np.floating, Is[float]])
ToFloating_2ds = TypeAliasType("ToFloating_2ds", _ToArray_2ds[np.floating, Is[float]])
ToFloating_3ds = TypeAliasType("ToFloating_3ds", _ToArray_3ds[np.floating, Is[float]])
ToFloating_1nd = TypeAliasType("ToFloating_1nd", _ToArray_1nd[np.floating, Is[float]])
ToFloating_2nd = TypeAliasType("ToFloating_2nd", _ToArray_2nd[np.floating, Is[float]])
ToFloating_3nd = TypeAliasType("ToFloating_3nd", _ToArray_3nd[np.floating, Is[float]])

# complex floats
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _ToArray_nd[np.complex64])
ToComplex64_0d = TypeAliasType("ToComplex64_0d", _ToArray_0d[np.complex64])
ToComplex64_1d = TypeAliasType("ToComplex64_1d", _ToArray_1d[np.complex64])
ToComplex64_2d = TypeAliasType("ToComplex64_2d", _ToArray_2d[np.complex64])
ToComplex64_3d = TypeAliasType("ToComplex64_3d", _ToArray_3d[np.complex64])
ToComplex64_1ds = TypeAliasType("ToComplex64_1ds", _ToArray_1ds[np.complex64])
ToComplex64_2ds = TypeAliasType("ToComplex64_2ds", _ToArray_2ds[np.complex64])
ToComplex64_3ds = TypeAliasType("ToComplex64_3ds", _ToArray_3ds[np.complex64])
ToComplex64_1nd = TypeAliasType("ToComplex64_1nd", _ToArray_1nd[np.complex64])
ToComplex64_2nd = TypeAliasType("ToComplex64_2nd", _ToArray_2nd[np.complex64])
ToComplex64_3nd = TypeAliasType("ToComplex64_3nd", _ToArray_3nd[np.complex64])

_ToComplex128: TypeAlias = np.complexfloating[_64Bit]
ToComplex128_nd = TypeAliasType("ToComplex128_nd", _ToArray_nd[_ToComplex128, Is[complex]])
ToComplex128_0d = TypeAliasType("ToComplex128_0d", _ToArray_0d[_ToComplex128, Is[complex]])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _ToArray_1d[_ToComplex128, Is[complex]])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _ToArray_2d[_ToComplex128, Is[complex]])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _ToArray_3d[_ToComplex128, Is[complex]])
ToComplex128_1ds = TypeAliasType("ToComplex128_1ds", _ToArray_1ds[_ToComplex128, Is[complex]])
ToComplex128_2ds = TypeAliasType("ToComplex128_2ds", _ToArray_2ds[_ToComplex128, Is[complex]])
ToComplex128_3ds = TypeAliasType("ToComplex128_3ds", _ToArray_3ds[_ToComplex128, Is[complex]])
ToComplex128_1nd = TypeAliasType("ToComplex128_1nd", _ToArray_1nd[_ToComplex128, Is[complex]])
ToComplex128_2nd = TypeAliasType("ToComplex128_2nd", _ToArray_2nd[_ToComplex128, Is[complex]])
ToComplex128_3nd = TypeAliasType("ToComplex128_3nd", _ToArray_3nd[_ToComplex128, Is[complex]])

ToCLongDouble_nd = TypeAliasType("ToCLongDouble_nd", _ToArray_nd[np.clongdouble])
ToCLongDouble_0d = TypeAliasType("ToCLongDouble_0d", _ToArray_0d[np.clongdouble])
ToCLongDouble_1d = TypeAliasType("ToCLongDouble_1d", _ToArray_1d[np.clongdouble])
ToCLongDouble_2d = TypeAliasType("ToCLongDouble_2d", _ToArray_2d[np.clongdouble])
ToCLongDouble_3d = TypeAliasType("ToCLongDouble_3d", _ToArray_3d[np.clongdouble])
ToCLongDouble_1ds = TypeAliasType("ToCLongDouble_1ds", _ToArray_1ds[np.clongdouble])
ToCLongDouble_2ds = TypeAliasType("ToCLongDouble_2ds", _ToArray_2ds[np.clongdouble])
ToCLongDouble_3ds = TypeAliasType("ToCLongDouble_3ds", _ToArray_3ds[np.clongdouble])
ToCLongDouble_1nd = TypeAliasType("ToCLongDouble_1nd", _ToArray_1nd[np.clongdouble])
ToCLongDouble_2nd = TypeAliasType("ToCLongDouble_2nd", _ToArray_2nd[np.clongdouble])
ToCLongDouble_3nd = TypeAliasType("ToCLongDouble_3nd", _ToArray_3nd[np.clongdouble])

ToCFloating_nd = TypeAliasType("ToCFloating_nd", _ToArray_nd[np.complexfloating, Is[complex]])
ToCFloating_0d = TypeAliasType("ToCFloating_0d", _ToArray_0d[np.complexfloating, Is[complex]])
ToCFloating_1d = TypeAliasType("ToCFloating_1d", _ToArray_1d[np.complexfloating, Is[complex]])
ToCFloating_2d = TypeAliasType("ToCFloating_2d", _ToArray_2d[np.complexfloating, Is[complex]])
ToCFloating_3d = TypeAliasType("ToCFloating_3d", _ToArray_3d[np.complexfloating, Is[complex]])
ToCFloating_1ds = TypeAliasType("ToCFloating_1ds", _ToArray_1ds[np.complexfloating, Is[complex]])
ToCFloating_2ds = TypeAliasType("ToCFloating_2ds", _ToArray_2ds[np.complexfloating, Is[complex]])
ToCFloating_3ds = TypeAliasType("ToCFloating_3ds", _ToArray_3ds[np.complexfloating, Is[complex]])
ToCFloating_1nd = TypeAliasType("ToCFloating_1nd", _ToArray_1nd[np.complexfloating, Is[complex]])
ToCFloating_2nd = TypeAliasType("ToCFloating_2nd", _ToArray_2nd[np.complexfloating, Is[complex]])
ToCFloating_3nd = TypeAliasType("ToCFloating_3nd", _ToArray_3nd[np.complexfloating, Is[complex]])

# integers, real- and complex floats
ToNumber_nd = TypeAliasType("ToNumber_nd", _ToArray_nd[np.number, _PyNumber])
ToNumber_0d = TypeAliasType("ToNumber_0d", _ToArray_0d[np.number, _PyNumber])
ToNumber_1d = TypeAliasType("ToNumber_1d", _ToArray_1d[np.number, _PyNumber])
ToNumber_2d = TypeAliasType("ToNumber_2d", _ToArray_2d[np.number, _PyNumber])
ToNumber_3d = TypeAliasType("ToNumber_3d", _ToArray_3d[np.number, _PyNumber])
ToNumber_1ds = TypeAliasType("ToNumber_1ds", _ToArray_1ds[np.number, _PyNumber])
ToNumber_2ds = TypeAliasType("ToNumber_2ds", _ToArray_2ds[np.number, _PyNumber])
ToNumber_3ds = TypeAliasType("ToNumber_3ds", _ToArray_3ds[np.number, _PyNumber])
ToNumber_1nd = TypeAliasType("ToNumber_1nd", _ToArray_1nd[np.number, _PyNumber])
ToNumber_2nd = TypeAliasType("ToNumber_2nd", _ToArray_2nd[np.number, _PyNumber])
ToNumber_3nd = TypeAliasType("ToNumber_3nd", _ToArray_3nd[np.number, _PyNumber])

# integers and real floats
ToReal_nd = TypeAliasType("ToReal_nd", _ToArray_nd[np.number[Any, float | int], _PyReal])
ToReal_0d = TypeAliasType("ToReal_0d", _ToArray_0d[np.number[Any, float | int], _PyReal])
ToReal_1d = TypeAliasType("ToReal_1d", _ToArray_1d[np.number[Any, float | int], _PyReal])
ToReal_2d = TypeAliasType("ToReal_2d", _ToArray_2d[np.number[Any, float | int], _PyReal])
ToReal_3d = TypeAliasType("ToReal_3d", _ToArray_3d[np.number[Any, float | int], _PyReal])
ToReal_1ds = TypeAliasType("ToReal_1ds", _ToArray_1ds[np.number[Any, float | int], _PyReal])
ToReal_2ds = TypeAliasType("ToReal_2ds", _ToArray_2ds[np.number[Any, float | int], _PyReal])
ToReal_3ds = TypeAliasType("ToReal_3ds", _ToArray_3ds[np.number[Any, float | int], _PyReal])
ToReal_1nd = TypeAliasType("ToReal_1nd", _ToArray_1nd[np.number[Any, float | int], _PyReal])
ToReal_2nd = TypeAliasType("ToReal_2nd", _ToArray_2nd[np.number[Any, float | int], _PyReal])
ToReal_3nd = TypeAliasType("ToReal_3nd", _ToArray_3nd[np.number[Any, float | int], _PyReal])

# real- and complex floats
ToInexact_nd = TypeAliasType("ToInexact_nd", _ToArray_nd[np.inexact, _PyInexact])
ToInexact_0d = TypeAliasType("ToInexact_0d", _ToArray_0d[np.inexact, _PyInexact])
ToInexact_1d = TypeAliasType("ToInexact_1d", _ToArray_1d[np.inexact, _PyInexact])
ToInexact_2d = TypeAliasType("ToInexact_2d", _ToArray_2d[np.inexact, _PyInexact])
ToInexact_3d = TypeAliasType("ToInexact_3d", _ToArray_3d[np.inexact, _PyInexact])
ToInexact_1ds = TypeAliasType("ToInexact_1ds", _ToArray_1ds[np.inexact, _PyInexact])
ToInexact_2ds = TypeAliasType("ToInexact_2ds", _ToArray_2ds[np.inexact, _PyInexact])
ToInexact_3ds = TypeAliasType("ToInexact_3ds", _ToArray_3ds[np.inexact, _PyInexact])
ToInexact_1nd = TypeAliasType("ToInexact_1nd", _ToArray_1nd[np.inexact, _PyInexact])
ToInexact_2nd = TypeAliasType("ToInexact_2nd", _ToArray_2nd[np.inexact, _PyInexact])
ToInexact_3nd = TypeAliasType("ToInexact_3nd", _ToArray_3nd[np.inexact, _PyInexact])

# temporal
_ToTimeDelta: TypeAlias = np.timedelta64[Any]
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _ToArray_nd[np.timedelta64])
ToTimeDelta_0d = TypeAliasType("ToTimeDelta_0d", _ToArray_0d[np.timedelta64])
ToTimeDelta_1d = TypeAliasType("ToTimeDelta_1d", _ToArray_1d[np.timedelta64])
ToTimeDelta_2d = TypeAliasType("ToTimeDelta_2d", _ToArray_2d[np.timedelta64])
ToTimeDelta_3d = TypeAliasType("ToTimeDelta_3d", _ToArray_3d[np.timedelta64])
ToTimeDelta_1ds = TypeAliasType("ToTimeDelta_1ds", _ToArray_1ds[np.timedelta64])
ToTimeDelta_2ds = TypeAliasType("ToTimeDelta_2ds", _ToArray_2ds[np.timedelta64])
ToTimeDelta_3ds = TypeAliasType("ToTimeDelta_3ds", _ToArray_3ds[np.timedelta64])
ToTimeDelta_1nd = TypeAliasType("ToTimeDelta_1nd", _ToArray_1nd[np.timedelta64])
ToTimeDelta_2nd = TypeAliasType("ToTimeDelta_2nd", _ToArray_2nd[np.timedelta64])
ToTimeDelta_3nd = TypeAliasType("ToTimeDelta_3nd", _ToArray_3nd[np.timedelta64])

_ToDateTime: TypeAlias = np.datetime64[Any]
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _ToArray_nd[np.datetime64])
ToDateTime_0d = TypeAliasType("ToDateTime_0d", _ToArray_0d[np.datetime64])
ToDateTime_1d = TypeAliasType("ToDateTime_1d", _ToArray_1d[np.datetime64])
ToDateTime_2d = TypeAliasType("ToDateTime_2d", _ToArray_2d[np.datetime64])
ToDateTime_3d = TypeAliasType("ToDateTime_3d", _ToArray_3d[np.datetime64])
ToDateTime_1ds = TypeAliasType("ToDateTime_1ds", _ToArray_1ds[np.datetime64])
ToDateTime_2ds = TypeAliasType("ToDateTime_2ds", _ToArray_2ds[np.datetime64])
ToDateTime_3ds = TypeAliasType("ToDateTime_3ds", _ToArray_3ds[np.datetime64])
ToDateTime_1nd = TypeAliasType("ToDateTime_1nd", _ToArray_1nd[np.datetime64])
ToDateTime_2nd = TypeAliasType("ToDateTime_2nd", _ToArray_2nd[np.datetime64])
ToDateTime_3nd = TypeAliasType("ToDateTime_3nd", _ToArray_3nd[np.datetime64])

# fixed strings
_ToBytes: TypeAlias = np.character[bytes]
ToBytes_nd = TypeAliasType("ToBytes_nd", _ToArray_nd[_ToBytes, Is[bytes]])
ToBytes_0d = TypeAliasType("ToBytes_0d", _ToArray_0d[_ToBytes, Is[bytes]])
ToBytes_1d = TypeAliasType("ToBytes_1d", _ToArray_1d[_ToBytes, Is[bytes]])
ToBytes_2d = TypeAliasType("ToBytes_2d", _ToArray_2d[_ToBytes, Is[bytes]])
ToBytes_3d = TypeAliasType("ToBytes_3d", _ToArray_3d[_ToBytes, Is[bytes]])
ToBytes_1ds = TypeAliasType("ToBytes_1ds", _ToArray_1ds[_ToBytes, Is[bytes]])
ToBytes_2ds = TypeAliasType("ToBytes_2ds", _ToArray_2ds[_ToBytes, Is[bytes]])
ToBytes_3ds = TypeAliasType("ToBytes_3ds", _ToArray_3ds[_ToBytes, Is[bytes]])
ToBytes_1nd = TypeAliasType("ToBytes_1nd", _ToArray_1nd[_ToBytes, Is[bytes]])
ToBytes_2nd = TypeAliasType("ToBytes_2nd", _ToArray_2nd[_ToBytes, Is[bytes]])
ToBytes_3nd = TypeAliasType("ToBytes_3nd", _ToArray_3nd[_ToBytes, Is[bytes]])

_ToStr: TypeAlias = np.character[str]
ToStr_nd = TypeAliasType("ToStr_nd", _ToArray_nd[_ToStr, Is[str]])
ToStr_0d = TypeAliasType("ToStr_0d", _ToArray_0d[_ToStr, Is[str]])
ToStr_1d = TypeAliasType("ToStr_1d", _ToArray_1d[_ToStr, Is[str]])
ToStr_2d = TypeAliasType("ToStr_2d", _ToArray_2d[_ToStr, Is[str]])
ToStr_3d = TypeAliasType("ToStr_3d", _ToArray_3d[_ToStr, Is[str]])
ToStr_1ds = TypeAliasType("ToStr_1ds", _ToArray_1ds[_ToStr, Is[str]])
ToStr_2ds = TypeAliasType("ToStr_2ds", _ToArray_2ds[_ToStr, Is[str]])
ToStr_3ds = TypeAliasType("ToStr_3ds", _ToArray_3ds[_ToStr, Is[str]])
ToStr_1nd = TypeAliasType("ToStr_1nd", _ToArray_1nd[_ToStr, Is[str]])
ToStr_2nd = TypeAliasType("ToStr_2nd", _ToArray_2nd[_ToStr, Is[str]])
ToStr_3nd = TypeAliasType("ToStr_3nd", _ToArray_3nd[_ToStr, Is[str]])

ToCharacter_nd = TypeAliasType("ToCharacter_nd", _ToArray_nd[np.character, _PyCharacter])
ToCharacter_0d = TypeAliasType("ToCharacter_0d", _ToArray_0d[np.character, _PyCharacter])
ToCharacter_1d = TypeAliasType("ToCharacter_1d", _ToArray_1d[np.character, _PyCharacter])
ToCharacter_2d = TypeAliasType("ToCharacter_2d", _ToArray_2d[np.character, _PyCharacter])
ToCharacter_3d = TypeAliasType("ToCharacter_3d", _ToArray_3d[np.character, _PyCharacter])
ToCharacter_1ds = TypeAliasType("ToCharacter_1ds", _ToArray_1ds[np.character, _PyCharacter])
ToCharacter_2ds = TypeAliasType("ToCharacter_2ds", _ToArray_2ds[np.character, _PyCharacter])
ToCharacter_3ds = TypeAliasType("ToCharacter_3ds", _ToArray_3ds[np.character, _PyCharacter])
ToCharacter_1nd = TypeAliasType("ToCharacter_1nd", _ToArray_1nd[np.character, _PyCharacter])
ToCharacter_2nd = TypeAliasType("ToCharacter_2nd", _ToArray_2nd[np.character, _PyCharacter])
ToCharacter_3nd = TypeAliasType("ToCharacter_3nd", _ToArray_3nd[np.character, _PyCharacter])

# python object
ToObject_nd = TypeAliasType("ToObject_nd", _ToArray_nd[np.object_, _PyObject])
ToObject_0d = TypeAliasType("ToObject_0d", _ToArray_0d[np.object_, _PyObject])
ToObject_1d = TypeAliasType("ToObject_1d", _ToArray_1d[np.object_, _PyObject])
ToObject_2d = TypeAliasType("ToObject_2d", _ToArray_2d[np.object_, _PyObject])
ToObject_3d = TypeAliasType("ToObject_3d", _ToArray_3d[np.object_, _PyObject])
ToObject_1ds = TypeAliasType("ToObject_1ds", _ToArray_1ds[np.object_, _PyObject])
ToObject_2ds = TypeAliasType("ToObject_2ds", _ToArray_2ds[np.object_, _PyObject])
ToObject_3ds = TypeAliasType("ToObject_3ds", _ToArray_3ds[np.object_, _PyObject])
ToObject_1nd = TypeAliasType("ToObject_1nd", _ToArray_1nd[np.object_, _PyObject])
ToObject_2nd = TypeAliasType("ToObject_2nd", _ToArray_2nd[np.object_, _PyObject])
ToObject_3nd = TypeAliasType("ToObject_3nd", _ToArray_3nd[np.object_, _PyObject])

# any scalar
ToAny_nd = TypeAliasType("ToAny_nd", _ToArray_nd[np.generic, object])
ToAny_0d = TypeAliasType("ToAny_0d", _ToArray_0d[np.generic, object])
ToAny_1d = TypeAliasType("ToAny_1d", _ToArray_1d[np.generic, object])
ToAny_2d = TypeAliasType("ToAny_2d", _ToArray_2d[np.generic, object])
ToAny_3d = TypeAliasType("ToAny_3d", _ToArray_3d[np.generic, object])
ToAny_1ds = TypeAliasType("ToAny_1ds", _ToArray_1ds[np.generic, object])
ToAny_2ds = TypeAliasType("ToAny_2ds", _ToArray_2ds[np.generic, object])
ToAny_3ds = TypeAliasType("ToAny_3ds", _ToArray_3ds[np.generic, object])
ToAny_1nd = TypeAliasType("ToAny_1nd", _ToArray_1nd[np.generic, object])
ToAny_2nd = TypeAliasType("ToAny_2nd", _ToArray_2nd[np.generic, object])
ToAny_3nd = TypeAliasType("ToAny_3nd", _ToArray_3nd[np.generic, object])

###
# Coercible (overlapping) scalar- and array-likes

# bool
CoBool_nd = TypeAliasType("CoBool_nd", _ToArray_nd[_ToBool, bool])
CoBool_0d = TypeAliasType("CoBool_0d", _ToArray_0d[_ToBool, bool])
CoBool_1d = TypeAliasType("CoBool_1d", _ToArray_1d[_ToBool, bool])
CoBool_2d = TypeAliasType("CoBool_2d", _ToArray_2d[_ToBool, bool])
CoBool_3d = TypeAliasType("CoBool_3d", _ToArray_3d[_ToBool, bool])
CoBool_1ds = TypeAliasType("CoBool_1ds", _ToArray_1ds[_ToBool, bool])
CoBool_2ds = TypeAliasType("CoBool_2ds", _ToArray_2ds[_ToBool, bool])
CoBool_3ds = TypeAliasType("CoBool_3ds", _ToArray_3ds[_ToBool, bool])
CoBool_1nd = TypeAliasType("CoBool_1nd", _ToArray_1nd[_ToBool, bool])
CoBool_2nd = TypeAliasType("CoBool_2nd", _ToArray_2nd[_ToBool, bool])
CoBool_3nd = TypeAliasType("CoBool_3nd", _ToArray_3nd[_ToBool, bool])

# unsigned integers
_CoUInt8: TypeAlias = np.uint8 | _ToBool
CoUInt8_nd = TypeAliasType("CoUInt8_nd", _ToArray_nd[_CoUInt8, bool])
CoUInt8_0d = TypeAliasType("CoUInt8_0d", _ToArray_0d[_CoUInt8, bool])
CoUInt8_1d = TypeAliasType("CoUInt8_1d", _ToArray_1d[_CoUInt8, bool])
CoUInt8_2d = TypeAliasType("CoUInt8_2d", _ToArray_2d[_CoUInt8, bool])
CoUInt8_3d = TypeAliasType("CoUInt8_3d", _ToArray_3d[_CoUInt8, bool])
CoUInt8_1ds = TypeAliasType("CoUInt8_1ds", _ToArray_1ds[_CoUInt8, bool])
CoUInt8_2ds = TypeAliasType("CoUInt8_2ds", _ToArray_2ds[_CoUInt8, bool])
CoUInt8_3ds = TypeAliasType("CoUInt8_3ds", _ToArray_3ds[_CoUInt8, bool])
CoUInt8_1nd = TypeAliasType("CoUInt8_1nd", _ToArray_1nd[_CoUInt8, bool])
CoUInt8_2nd = TypeAliasType("CoUInt8_2nd", _ToArray_2nd[_CoUInt8, bool])
CoUInt8_3nd = TypeAliasType("CoUInt8_3nd", _ToArray_3nd[_CoUInt8, bool])

_CoUInt16: TypeAlias = np.uint16 | _CoUInt8
CoUInt16_nd = TypeAliasType("CoUInt16_nd", _ToArray_nd[_CoUInt16, bool])
CoUInt16_0d = TypeAliasType("CoUInt16_0d", _ToArray_0d[_CoUInt16, bool])
CoUInt16_1d = TypeAliasType("CoUInt16_1d", _ToArray_1d[_CoUInt16, bool])
CoUInt16_2d = TypeAliasType("CoUInt16_2d", _ToArray_2d[_CoUInt16, bool])
CoUInt16_3d = TypeAliasType("CoUInt16_3d", _ToArray_3d[_CoUInt16, bool])
CoUInt16_1ds = TypeAliasType("CoUInt16_1ds", _ToArray_1ds[_CoUInt16, bool])
CoUInt16_2ds = TypeAliasType("CoUInt16_2ds", _ToArray_2ds[_CoUInt16, bool])
CoUInt16_3ds = TypeAliasType("CoUInt16_3ds", _ToArray_3ds[_CoUInt16, bool])
CoUInt16_1nd = TypeAliasType("CoUInt16_1nd", _ToArray_1nd[_CoUInt16, bool])
CoUInt16_2nd = TypeAliasType("CoUInt16_2nd", _ToArray_2nd[_CoUInt16, bool])
CoUInt16_3nd = TypeAliasType("CoUInt16_3nd", _ToArray_3nd[_CoUInt16, bool])

_CoUInt32: TypeAlias = np.uint32 | _CoUInt16
CoUInt32_nd = TypeAliasType("CoUInt32_nd", _ToArray_nd[_CoUInt32, bool])
CoUInt32_0d = TypeAliasType("CoUInt32_0d", _ToArray_0d[_CoUInt32, bool])
CoUInt32_1d = TypeAliasType("CoUInt32_1d", _ToArray_1d[_CoUInt32, bool])
CoUInt32_2d = TypeAliasType("CoUInt32_2d", _ToArray_2d[_CoUInt32, bool])
CoUInt32_3d = TypeAliasType("CoUInt32_3d", _ToArray_3d[_CoUInt32, bool])
CoUInt32_1ds = TypeAliasType("CoUInt32_1ds", _ToArray_1ds[_CoUInt32, bool])
CoUInt32_2ds = TypeAliasType("CoUInt32_2ds", _ToArray_2ds[_CoUInt32, bool])
CoUInt32_3ds = TypeAliasType("CoUInt32_3ds", _ToArray_3ds[_CoUInt32, bool])
CoUInt32_1nd = TypeAliasType("CoUInt32_1nd", _ToArray_1nd[_CoUInt32, bool])
CoUInt32_2nd = TypeAliasType("CoUInt32_2nd", _ToArray_2nd[_CoUInt32, bool])
CoUInt32_3nd = TypeAliasType("CoUInt32_3nd", _ToArray_3nd[_CoUInt32, bool])

_CoUInt64: TypeAlias = np.uint64 | _CoUInt32
CoUInt64_nd = TypeAliasType("CoUInt64_nd", _ToArray_nd[_CoUInt64, bool])
CoUInt64_0d = TypeAliasType("CoUInt64_0d", _ToArray_0d[_CoUInt64, bool])
CoUInt64_1d = TypeAliasType("CoUInt64_1d", _ToArray_1d[_CoUInt64, bool])
CoUInt64_2d = TypeAliasType("CoUInt64_2d", _ToArray_2d[_CoUInt64, bool])
CoUInt64_3d = TypeAliasType("CoUInt64_3d", _ToArray_3d[_CoUInt64, bool])
CoUInt64_1ds = TypeAliasType("CoUInt64_1ds", _ToArray_1ds[_CoUInt64, bool])
CoUInt64_2ds = TypeAliasType("CoUInt64_2ds", _ToArray_2ds[_CoUInt64, bool])
CoUInt64_3ds = TypeAliasType("CoUInt64_3ds", _ToArray_3ds[_CoUInt64, bool])
CoUInt64_1nd = TypeAliasType("CoUInt64_1nd", _ToArray_1nd[_CoUInt64, bool])
CoUInt64_2nd = TypeAliasType("CoUInt64_2nd", _ToArray_2nd[_CoUInt64, bool])
CoUInt64_3nd = TypeAliasType("CoUInt64_3nd", _ToArray_3nd[_CoUInt64, bool])

_CoULong: TypeAlias = np.ulong | _CoUInt32
CoULong_nd = TypeAliasType("CoULong_nd", _ToArray_nd[_CoULong, bool])
CoULong_0d = TypeAliasType("CoULong_0d", _ToArray_0d[_CoULong, bool])
CoULong_1d = TypeAliasType("CoULong_1d", _ToArray_1d[_CoULong, bool])
CoULong_2d = TypeAliasType("CoULong_2d", _ToArray_2d[_CoULong, bool])
CoULong_3d = TypeAliasType("CoULong_3d", _ToArray_3d[_CoULong, bool])
CoULong_1ds = TypeAliasType("CoULong_1ds", _ToArray_1ds[_CoULong, bool])
CoULong_2ds = TypeAliasType("CoULong_2ds", _ToArray_2ds[_CoULong, bool])
CoULong_3ds = TypeAliasType("CoULong_3ds", _ToArray_3ds[_CoULong, bool])
CoULong_1nd = TypeAliasType("CoULong_1nd", _ToArray_1nd[_CoULong, bool])
CoULong_2nd = TypeAliasType("CoULong_2nd", _ToArray_2nd[_CoULong, bool])
CoULong_3nd = TypeAliasType("CoULong_3nd", _ToArray_3nd[_CoULong, bool])

_CoUIntP: TypeAlias = np.uintp | _CoULong
CoUIntP_nd = TypeAliasType("CoUIntP_nd", _ToArray_nd[_CoUIntP, bool])
CoUIntP_0d = TypeAliasType("CoUIntP_0d", _ToArray_0d[_CoUIntP, bool])
CoUIntP_1d = TypeAliasType("CoUIntP_1d", _ToArray_1d[_CoUIntP, bool])
CoUIntP_2d = TypeAliasType("CoUIntP_2d", _ToArray_2d[_CoUIntP, bool])
CoUIntP_3d = TypeAliasType("CoUIntP_3d", _ToArray_3d[_CoUIntP, bool])
CoUIntP_1ds = TypeAliasType("CoUIntP_1ds", _ToArray_1ds[_CoUIntP, bool])
CoUIntP_2ds = TypeAliasType("CoUIntP_2ds", _ToArray_2ds[_CoUIntP, bool])
CoUIntP_3ds = TypeAliasType("CoUIntP_3ds", _ToArray_3ds[_CoUIntP, bool])
CoUIntP_1nd = TypeAliasType("CoUIntP_1nd", _ToArray_1nd[_CoUIntP, bool])
CoUIntP_2nd = TypeAliasType("CoUIntP_2nd", _ToArray_2nd[_CoUIntP, bool])
CoUIntP_3nd = TypeAliasType("CoUIntP_3nd", _ToArray_3nd[_CoUIntP, bool])

_CoULongLong: TypeAlias = np.unsignedinteger | _ToBool
CoULongLong_nd = TypeAliasType("CoULongLong_nd", _ToArray_nd[_CoULongLong, bool])
CoULongLong_0d = TypeAliasType("CoULongLong_0d", _ToArray_0d[_CoULongLong, bool])
CoULongLong_1d = TypeAliasType("CoULongLong_1d", _ToArray_1d[_CoULongLong, bool])
CoULongLong_2d = TypeAliasType("CoULongLong_2d", _ToArray_2d[_CoULongLong, bool])
CoULongLong_3d = TypeAliasType("CoULongLong_3d", _ToArray_3d[_CoULongLong, bool])
CoULongLong_1ds = TypeAliasType("CoULongLong_1ds", _ToArray_1ds[_CoULongLong, bool])
CoULongLong_2ds = TypeAliasType("CoULongLong_2ds", _ToArray_2ds[_CoULongLong, bool])
CoULongLong_3ds = TypeAliasType("CoULongLong_3ds", _ToArray_3ds[_CoULongLong, bool])
CoULongLong_1nd = TypeAliasType("CoULongLong_1nd", _ToArray_1nd[_CoULongLong, bool])
CoULongLong_2nd = TypeAliasType("CoULongLong_2nd", _ToArray_2nd[_CoULongLong, bool])
CoULongLong_3nd = TypeAliasType("CoULongLong_3nd", _ToArray_3nd[_CoULongLong, bool])

# signed integers
_CoInt8: TypeAlias = np.int8 | _ToBool
CoInt8_nd = TypeAliasType("CoInt8_nd", _ToArray_nd[_CoInt8, bool])
CoInt8_0d = TypeAliasType("CoInt8_0d", _ToArray_0d[_CoInt8, bool])
CoInt8_1d = TypeAliasType("CoInt8_1d", _ToArray_1d[_CoInt8, bool])
CoInt8_2d = TypeAliasType("CoInt8_2d", _ToArray_2d[_CoInt8, bool])
CoInt8_3d = TypeAliasType("CoInt8_3d", _ToArray_3d[_CoInt8, bool])
CoInt8_1ds = TypeAliasType("CoInt8_1ds", _ToArray_1ds[_CoInt8, bool])
CoInt8_2ds = TypeAliasType("CoInt8_2ds", _ToArray_2ds[_CoInt8, bool])
CoInt8_3ds = TypeAliasType("CoInt8_3ds", _ToArray_3ds[_CoInt8, bool])
CoInt8_1nd = TypeAliasType("CoInt8_1nd", _ToArray_1nd[_CoInt8, bool])
CoInt8_2nd = TypeAliasType("CoInt8_2nd", _ToArray_2nd[_CoInt8, bool])
CoInt8_3nd = TypeAliasType("CoInt8_3nd", _ToArray_3nd[_CoInt8, bool])

_CoInt16: TypeAlias = np.int16 | np.uint8 | _CoInt8
CoInt16_nd = TypeAliasType("CoInt16_nd", _ToArray_nd[_CoInt16, bool])
CoInt16_0d = TypeAliasType("CoInt16_0d", _ToArray_0d[_CoInt16, bool])
CoInt16_1d = TypeAliasType("CoInt16_1d", _ToArray_1d[_CoInt16, bool])
CoInt16_2d = TypeAliasType("CoInt16_2d", _ToArray_2d[_CoInt16, bool])
CoInt16_3d = TypeAliasType("CoInt16_3d", _ToArray_3d[_CoInt16, bool])
CoInt16_1ds = TypeAliasType("CoInt16_1ds", _ToArray_1ds[_CoInt16, bool])
CoInt16_2ds = TypeAliasType("CoInt16_2ds", _ToArray_2ds[_CoInt16, bool])
CoInt16_3ds = TypeAliasType("CoInt16_3ds", _ToArray_3ds[_CoInt16, bool])
CoInt16_1nd = TypeAliasType("CoInt16_1nd", _ToArray_1nd[_CoInt16, bool])
CoInt16_2nd = TypeAliasType("CoInt16_2nd", _ToArray_2nd[_CoInt16, bool])
CoInt16_3nd = TypeAliasType("CoInt16_3nd", _ToArray_3nd[_CoInt16, bool])

_CoInt32: TypeAlias = np.int32 | np.uint16 | _CoInt16
CoInt32_nd = TypeAliasType("CoInt32_nd", _ToArray_nd[_CoInt32, bool])
CoInt32_0d = TypeAliasType("CoInt32_0d", _ToArray_0d[_CoInt32, bool])
CoInt32_1d = TypeAliasType("CoInt32_1d", _ToArray_1d[_CoInt32, bool])
CoInt32_2d = TypeAliasType("CoInt32_2d", _ToArray_2d[_CoInt32, bool])
CoInt32_3d = TypeAliasType("CoInt32_3d", _ToArray_3d[_CoInt32, bool])
CoInt32_1ds = TypeAliasType("CoInt32_1ds", _ToArray_1ds[_CoInt32, bool])
CoInt32_2ds = TypeAliasType("CoInt32_2ds", _ToArray_2ds[_CoInt32, bool])
CoInt32_3ds = TypeAliasType("CoInt32_3ds", _ToArray_3ds[_CoInt32, bool])
CoInt32_1nd = TypeAliasType("CoInt32_1nd", _ToArray_1nd[_CoInt32, bool])
CoInt32_2nd = TypeAliasType("CoInt32_2nd", _ToArray_2nd[_CoInt32, bool])
CoInt32_3nd = TypeAliasType("CoInt32_3nd", _ToArray_3nd[_CoInt32, bool])

_CoInt64: TypeAlias = np.int64 | np.uint32 | _CoInt32
CoInt64_nd = TypeAliasType("CoInt64_nd", _ToArray_nd[_CoInt64, int])
CoInt64_0d = TypeAliasType("CoInt64_0d", _ToArray_0d[_CoInt64, int])
CoInt64_1d = TypeAliasType("CoInt64_1d", _ToArray_1d[_CoInt64, int])
CoInt64_2d = TypeAliasType("CoInt64_2d", _ToArray_2d[_CoInt64, int])
CoInt64_3d = TypeAliasType("CoInt64_3d", _ToArray_3d[_CoInt64, int])
CoInt64_1ds = TypeAliasType("CoInt64_1ds", _ToArray_1ds[_CoInt64, int])
CoInt64_2ds = TypeAliasType("CoInt64_2ds", _ToArray_2ds[_CoInt64, int])
CoInt64_3ds = TypeAliasType("CoInt64_3ds", _ToArray_3ds[_CoInt64, int])
CoInt64_1nd = TypeAliasType("CoInt64_1nd", _ToArray_1nd[_CoInt64, int])
CoInt64_2nd = TypeAliasType("CoInt64_2nd", _ToArray_2nd[_CoInt64, int])
CoInt64_3nd = TypeAliasType("CoInt64_3nd", _ToArray_3nd[_CoInt64, int])

_CoLong: TypeAlias = np.long | _CoInt32
CoLong_nd = TypeAliasType("CoLong_nd", _ToArray_nd[_CoLong, bool])
CoLong_0d = TypeAliasType("CoLong_0d", _ToArray_0d[_CoLong, bool])
CoLong_1d = TypeAliasType("CoLong_1d", _ToArray_1d[_CoLong, bool])
CoLong_2d = TypeAliasType("CoLong_2d", _ToArray_2d[_CoLong, bool])
CoLong_3d = TypeAliasType("CoLong_3d", _ToArray_3d[_CoLong, bool])
CoLong_1ds = TypeAliasType("CoLong_1ds", _ToArray_1ds[_CoLong, bool])
CoLong_2ds = TypeAliasType("CoLong_2ds", _ToArray_2ds[_CoLong, bool])
CoLong_3ds = TypeAliasType("CoLong_3ds", _ToArray_3ds[_CoLong, bool])
CoLong_1nd = TypeAliasType("CoLong_1nd", _ToArray_1nd[_CoLong, bool])
CoLong_2nd = TypeAliasType("CoLong_2nd", _ToArray_2nd[_CoLong, bool])
CoLong_3nd = TypeAliasType("CoLong_3nd", _ToArray_3nd[_CoLong, bool])

_CoIntP: TypeAlias = np.intp | _CoLong
CoIntP_nd = TypeAliasType("CoIntP_nd", _ToArray_nd[_CoIntP, int])
CoIntP_0d = TypeAliasType("CoIntP_0d", _ToArray_0d[_CoIntP, int])
CoIntP_1d = TypeAliasType("CoIntP_1d", _ToArray_1d[_CoIntP, int])
CoIntP_2d = TypeAliasType("CoIntP_2d", _ToArray_2d[_CoIntP, int])
CoIntP_3d = TypeAliasType("CoIntP_3d", _ToArray_3d[_CoIntP, int])
CoIntP_1ds = TypeAliasType("CoIntP_1ds", _ToArray_1ds[_CoIntP, int])
CoIntP_2ds = TypeAliasType("CoIntP_2ds", _ToArray_2ds[_CoIntP, int])
CoIntP_3ds = TypeAliasType("CoIntP_3ds", _ToArray_3ds[_CoIntP, int])
CoIntP_1nd = TypeAliasType("CoIntP_1nd", _ToArray_1nd[_CoIntP, int])
CoIntP_2nd = TypeAliasType("CoIntP_2nd", _ToArray_2nd[_CoIntP, int])
CoIntP_3nd = TypeAliasType("CoIntP_3nd", _ToArray_3nd[_CoIntP, int])

_CoLongLong: TypeAlias = np.signedinteger | _CoUInt32
CoLongLong_nd = TypeAliasType("CoLongLong_nd", _ToArray_nd[_CoLongLong, int])
CoLongLong_0d = TypeAliasType("CoLongLong_0d", _ToArray_0d[_CoLongLong, int])
CoLongLong_1d = TypeAliasType("CoLongLong_1d", _ToArray_1d[_CoLongLong, int])
CoLongLong_2d = TypeAliasType("CoLongLong_2d", _ToArray_2d[_CoLongLong, int])
CoLongLong_3d = TypeAliasType("CoLongLong_3d", _ToArray_3d[_CoLongLong, int])
CoLongLong_1ds = TypeAliasType("CoLongLong_1ds", _ToArray_1ds[_CoLongLong, int])
CoLongLong_2ds = TypeAliasType("CoLongLong_2ds", _ToArray_2ds[_CoLongLong, int])
CoLongLong_3ds = TypeAliasType("CoLongLong_3ds", _ToArray_3ds[_CoLongLong, int])
CoLongLong_1nd = TypeAliasType("CoLongLong_1nd", _ToArray_1nd[_CoLongLong, int])
CoLongLong_2nd = TypeAliasType("CoLongLong_2nd", _ToArray_2nd[_CoLongLong, int])
CoLongLong_3nd = TypeAliasType("CoLongLong_3nd", _ToArray_3nd[_CoLongLong, int])

_CoInteger: TypeAlias = np.integer | _ToBool
CoInteger_nd = TypeAliasType("CoInteger_nd", _ToArray_nd[_CoInteger, int])
CoInteger_0d = TypeAliasType("CoInteger_0d", _ToArray_0d[_CoInteger, int])
CoInteger_1d = TypeAliasType("CoInteger_1d", _ToArray_1d[_CoInteger, int])
CoInteger_2d = TypeAliasType("CoInteger_2d", _ToArray_2d[_CoInteger, int])
CoInteger_3d = TypeAliasType("CoInteger_3d", _ToArray_3d[_CoInteger, int])
CoInteger_1ds = TypeAliasType("CoInteger_1ds", _ToArray_1ds[_CoInteger, int])
CoInteger_2ds = TypeAliasType("CoInteger_2ds", _ToArray_2ds[_CoInteger, int])
CoInteger_3ds = TypeAliasType("CoInteger_3ds", _ToArray_3ds[_CoInteger, int])
CoInteger_1nd = TypeAliasType("CoInteger_1nd", _ToArray_1nd[_CoInteger, int])
CoInteger_2nd = TypeAliasType("CoInteger_2nd", _ToArray_2nd[_CoInteger, int])
CoInteger_3nd = TypeAliasType("CoInteger_3nd", _ToArray_3nd[_CoInteger, int])

# real floats

_CoFloat16: TypeAlias = np.float16 | np.uint8 | np.int16 | _ToBool
CoFloat16_nd = TypeAliasType("CoFloat16_nd", _ToArray_nd[_CoFloat16, bool])
CoFloat16_0d = TypeAliasType("CoFloat16_0d", _ToArray_0d[_CoFloat16, bool])
CoFloat16_1d = TypeAliasType("CoFloat16_1d", _ToArray_1d[_CoFloat16, bool])
CoFloat16_2d = TypeAliasType("CoFloat16_2d", _ToArray_2d[_CoFloat16, bool])
CoFloat16_3d = TypeAliasType("CoFloat16_3d", _ToArray_3d[_CoFloat16, bool])
CoFloat16_1ds = TypeAliasType("CoFloat16_1ds", _ToArray_1ds[_CoFloat16, bool])
CoFloat16_2ds = TypeAliasType("CoFloat16_2ds", _ToArray_2ds[_CoFloat16, bool])
CoFloat16_3ds = TypeAliasType("CoFloat16_3ds", _ToArray_3ds[_CoFloat16, bool])
CoFloat16_1nd = TypeAliasType("CoFloat16_1nd", _ToArray_1nd[_CoFloat16, bool])
CoFloat16_2nd = TypeAliasType("CoFloat16_2nd", _ToArray_2nd[_CoFloat16, bool])
CoFloat16_3nd = TypeAliasType("CoFloat16_3nd", _ToArray_3nd[_CoFloat16, bool])

_CoFloat32: TypeAlias = np.float32 | np.uint16 | np.int16 | _CoFloat16
CoFloat32_nd = TypeAliasType("CoFloat32_nd", _ToArray_nd[_CoFloat32, bool])
CoFloat32_0d = TypeAliasType("CoFloat32_0d", _ToArray_0d[_CoFloat32, bool])
CoFloat32_1d = TypeAliasType("CoFloat32_1d", _ToArray_1d[_CoFloat32, bool])
CoFloat32_2d = TypeAliasType("CoFloat32_2d", _ToArray_2d[_CoFloat32, bool])
CoFloat32_3d = TypeAliasType("CoFloat32_3d", _ToArray_3d[_CoFloat32, bool])
CoFloat32_1ds = TypeAliasType("CoFloat32_1ds", _ToArray_1ds[_CoFloat32, bool])
CoFloat32_2ds = TypeAliasType("CoFloat32_2ds", _ToArray_2ds[_CoFloat32, bool])
CoFloat32_3ds = TypeAliasType("CoFloat32_3ds", _ToArray_3ds[_CoFloat32, bool])
CoFloat32_1nd = TypeAliasType("CoFloat32_1nd", _ToArray_1nd[_CoFloat32, bool])
CoFloat32_2nd = TypeAliasType("CoFloat32_2nd", _ToArray_2nd[_CoFloat32, bool])
CoFloat32_3nd = TypeAliasType("CoFloat32_3nd", _ToArray_3nd[_CoFloat32, bool])

_CoFloat64: TypeAlias = _ToFloat64 | np.float32 | np.float16 | _CoInteger
CoFloat64_nd = TypeAliasType("CoFloat64_nd", _ToArray_nd[_CoFloat64, float])
CoFloat64_0d = TypeAliasType("CoFloat64_0d", _ToArray_0d[_CoFloat64, float])
CoFloat64_1d = TypeAliasType("CoFloat64_1d", _ToArray_1d[_CoFloat64, float])
CoFloat64_2d = TypeAliasType("CoFloat64_2d", _ToArray_2d[_CoFloat64, float])
CoFloat64_3d = TypeAliasType("CoFloat64_3d", _ToArray_3d[_CoFloat64, float])
CoFloat64_1ds = TypeAliasType("CoFloat64_1ds", _ToArray_1ds[_CoFloat64, float])
CoFloat64_2ds = TypeAliasType("CoFloat64_2ds", _ToArray_2ds[_CoFloat64, float])
CoFloat64_3ds = TypeAliasType("CoFloat64_3ds", _ToArray_3ds[_CoFloat64, float])
CoFloat64_1nd = TypeAliasType("CoFloat64_1nd", _ToArray_1nd[_CoFloat64, float])
CoFloat64_2nd = TypeAliasType("CoFloat64_2nd", _ToArray_2nd[_CoFloat64, float])
CoFloat64_3nd = TypeAliasType("CoFloat64_3nd", _ToArray_3nd[_CoFloat64, float])

_CoFloating: TypeAlias = np.floating | np.integer | _ToBool
CoFloating_nd = TypeAliasType("CoFloating_nd", _ToArray_nd[_CoFloating, float])
CoFloating_0d = TypeAliasType("CoFloating_0d", _ToArray_0d[_CoFloating, float])
CoFloating_1d = TypeAliasType("CoFloating_1d", _ToArray_1d[_CoFloating, float])
CoFloating_2d = TypeAliasType("CoFloating_2d", _ToArray_2d[_CoFloating, float])
CoFloating_3d = TypeAliasType("CoFloating_3d", _ToArray_3d[_CoFloating, float])
CoFloating_1ds = TypeAliasType("CoFloating_1ds", _ToArray_1ds[_CoFloating, float])
CoFloating_2ds = TypeAliasType("CoFloating_2ds", _ToArray_2ds[_CoFloating, float])
CoFloating_3ds = TypeAliasType("CoFloating_3ds", _ToArray_3ds[_CoFloating, float])
CoFloating_1nd = TypeAliasType("CoFloating_1nd", _ToArray_1nd[_CoFloating, float])
CoFloating_2nd = TypeAliasType("CoFloating_2nd", _ToArray_2nd[_CoFloating, float])
CoFloating_3nd = TypeAliasType("CoFloating_3nd", _ToArray_3nd[_CoFloating, float])

# complex floats
_CoComplex64: TypeAlias = np.complex64 | _CoFloat32
CoComplex64_nd = TypeAliasType("CoComplex64_nd", _ToArray_nd[_CoComplex64, bool])
CoComplex64_0d = TypeAliasType("CoComplex64_0d", _ToArray_0d[_CoComplex64, bool])
CoComplex64_1d = TypeAliasType("CoComplex64_1d", _ToArray_1d[_CoComplex64, bool])
CoComplex64_2d = TypeAliasType("CoComplex64_2d", _ToArray_2d[_CoComplex64, bool])
CoComplex64_3d = TypeAliasType("CoComplex64_3d", _ToArray_3d[_CoComplex64, bool])
CoComplex64_1ds = TypeAliasType("CoComplex64_1ds", _ToArray_1ds[_CoComplex64, bool])
CoComplex64_2ds = TypeAliasType("CoComplex64_2ds", _ToArray_2ds[_CoComplex64, bool])
CoComplex64_3ds = TypeAliasType("CoComplex64_3ds", _ToArray_3ds[_CoComplex64, bool])
CoComplex64_1nd = TypeAliasType("CoComplex64_1nd", _ToArray_1nd[_CoComplex64, bool])
CoComplex64_2nd = TypeAliasType("CoComplex64_2nd", _ToArray_2nd[_CoComplex64, bool])
CoComplex64_3nd = TypeAliasType("CoComplex64_3nd", _ToArray_3nd[_CoComplex64, bool])

_CoComplex128: TypeAlias = _ToComplex128 | np.complex64 | _CoFloat64
CoComplex128_nd = TypeAliasType("CoComplex128_nd", _ToArray_nd[_CoComplex128, complex])
CoComplex128_0d = TypeAliasType("CoComplex128_0d", _ToArray_0d[_CoComplex128, complex])
CoComplex128_1d = TypeAliasType("CoComplex128_1d", _ToArray_1d[_CoComplex128, complex])
CoComplex128_2d = TypeAliasType("CoComplex128_2d", _ToArray_2d[_CoComplex128, complex])
CoComplex128_3d = TypeAliasType("CoComplex128_3d", _ToArray_3d[_CoComplex128, complex])
CoComplex128_1ds = TypeAliasType("CoComplex128_1ds", _ToArray_1ds[_CoComplex128, complex])
CoComplex128_2ds = TypeAliasType("CoComplex128_2ds", _ToArray_2ds[_CoComplex128, complex])
CoComplex128_3ds = TypeAliasType("CoComplex128_3ds", _ToArray_3ds[_CoComplex128, complex])
CoComplex128_1nd = TypeAliasType("CoComplex128_1nd", _ToArray_1nd[_CoComplex128, complex])
CoComplex128_2nd = TypeAliasType("CoComplex128_2nd", _ToArray_2nd[_CoComplex128, complex])
CoComplex128_3nd = TypeAliasType("CoComplex128_3nd", _ToArray_3nd[_CoComplex128, complex])

_CoNumber: TypeAlias = np.number | _ToBool
CoNumber_nd = TypeAliasType("CoNumber_nd", _ToArray_nd[_CoNumber, complex])
CoNumber_0d = TypeAliasType("CoNumber_0d", _ToArray_0d[_CoNumber, complex])
CoNumber_1d = TypeAliasType("CoNumber_1d", _ToArray_1d[_CoNumber, complex])
CoNumber_2d = TypeAliasType("CoNumber_2d", _ToArray_2d[_CoNumber, complex])
CoNumber_3d = TypeAliasType("CoNumber_3d", _ToArray_3d[_CoNumber, complex])
CoNumber_1ds = TypeAliasType("CoNumber_1ds", _ToArray_1ds[_CoNumber, complex])
CoNumber_2ds = TypeAliasType("CoNumber_2ds", _ToArray_2ds[_CoNumber, complex])
CoNumber_3ds = TypeAliasType("CoNumber_3ds", _ToArray_3ds[_CoNumber, complex])
CoNumber_1nd = TypeAliasType("CoNumber_1nd", _ToArray_1nd[_CoNumber, complex])
CoNumber_2nd = TypeAliasType("CoNumber_2nd", _ToArray_2nd[_CoNumber, complex])
CoNumber_3nd = TypeAliasType("CoNumber_3nd", _ToArray_3nd[_CoNumber, complex])

# temporal
_CoTimeDelta: TypeAlias = _ToTimeDelta | _CoInteger
CoTimeDelta_nd = TypeAliasType("CoTimeDelta_nd", _ToArray_nd[_CoTimeDelta, int])
CoTimeDelta_0d = TypeAliasType("CoTimeDelta_0d", _ToArray_0d[_CoTimeDelta, int])
CoTimeDelta_1d = TypeAliasType("CoTimeDelta_1d", _ToArray_1d[_CoTimeDelta, int])
CoTimeDelta_2d = TypeAliasType("CoTimeDelta_2d", _ToArray_2d[_CoTimeDelta, int])
CoTimeDelta_3d = TypeAliasType("CoTimeDelta_3d", _ToArray_3d[_CoTimeDelta, int])
CoTimeDelta_1ds = TypeAliasType("CoTimeDelta_1ds", _ToArray_1ds[_CoTimeDelta, int])
CoTimeDelta_2ds = TypeAliasType("CoTimeDelta_2ds", _ToArray_2ds[_CoTimeDelta, int])
CoTimeDelta_3ds = TypeAliasType("CoTimeDelta_3ds", _ToArray_3ds[_CoTimeDelta, int])
CoTimeDelta_1nd = TypeAliasType("CoTimeDelta_1nd", _ToArray_1nd[_CoTimeDelta, int])
CoTimeDelta_2nd = TypeAliasType("CoTimeDelta_2nd", _ToArray_2nd[_CoTimeDelta, int])
CoTimeDelta_3nd = TypeAliasType("CoTimeDelta_3nd", _ToArray_3nd[_CoTimeDelta, int])

_CoDateTime: TypeAlias = _ToDateTime | _ToTimeDelta
CoDateTime_nd = TypeAliasType("CoDateTime_nd", _ToArray_nd[_CoDateTime])
CoDateTime_0d = TypeAliasType("CoDateTime_0d", _ToArray_0d[_CoDateTime])
CoDateTime_1d = TypeAliasType("CoDateTime_1d", _ToArray_1d[_CoDateTime])
CoDateTime_2d = TypeAliasType("CoDateTime_2d", _ToArray_2d[_CoDateTime])
CoDateTime_3d = TypeAliasType("CoDateTime_3d", _ToArray_3d[_CoDateTime])
CoDateTime_1ds = TypeAliasType("CoDateTime_1ds", _ToArray_1ds[_CoDateTime])
CoDateTime_2ds = TypeAliasType("CoDateTime_2ds", _ToArray_2ds[_CoDateTime])
CoDateTime_3ds = TypeAliasType("CoDateTime_3ds", _ToArray_3ds[_CoDateTime])
CoDateTime_1nd = TypeAliasType("CoDateTime_1nd", _ToArray_1nd[_CoDateTime])
CoDateTime_2nd = TypeAliasType("CoDateTime_2nd", _ToArray_2nd[_CoDateTime])
CoDateTime_3nd = TypeAliasType("CoDateTime_3nd", _ToArray_3nd[_CoDateTime])

# fixed strings
_CoBytes: TypeAlias = _ToBytes
CoBytes_nd = TypeAliasType("CoBytes_nd", _ToArray_nd[_CoBytes, Is[bytes]])
CoBytes_0d = TypeAliasType("CoBytes_0d", _ToArray_0d[_CoBytes, Is[bytes]])
CoBytes_1d = TypeAliasType("CoBytes_1d", _ToArray_1d[_CoBytes, Is[bytes]])
CoBytes_2d = TypeAliasType("CoBytes_2d", _ToArray_2d[_CoBytes, Is[bytes]])
CoBytes_3d = TypeAliasType("CoBytes_3d", _ToArray_3d[_CoBytes, Is[bytes]])
CoBytes_1ds = TypeAliasType("CoBytes_1ds", _ToArray_1ds[_CoBytes, Is[bytes]])
CoBytes_2ds = TypeAliasType("CoBytes_2ds", _ToArray_2ds[_CoBytes, Is[bytes]])
CoBytes_3ds = TypeAliasType("CoBytes_3ds", _ToArray_3ds[_CoBytes, Is[bytes]])
CoBytes_1nd = TypeAliasType("CoBytes_1nd", _ToArray_1nd[_CoBytes, Is[bytes]])
CoBytes_2nd = TypeAliasType("CoBytes_2nd", _ToArray_2nd[_CoBytes, Is[bytes]])
CoBytes_3nd = TypeAliasType("CoBytes_3nd", _ToArray_3nd[_CoBytes, Is[bytes]])

_CoStr: TypeAlias = np.character
CoStr_nd = TypeAliasType("CoStr_nd", _ToArray_nd[_CoStr, _PyCharacter])
CoStr_0d = TypeAliasType("CoStr_0d", _ToArray_0d[_CoStr, _PyCharacter])
CoStr_1d = TypeAliasType("CoStr_1d", _ToArray_1d[_CoStr, _PyCharacter])
CoStr_2d = TypeAliasType("CoStr_2d", _ToArray_2d[_CoStr, _PyCharacter])
CoStr_3d = TypeAliasType("CoStr_3d", _ToArray_3d[_CoStr, _PyCharacter])
CoStr_1ds = TypeAliasType("CoStr_1ds", _ToArray_1ds[_CoStr, _PyCharacter])
CoStr_2ds = TypeAliasType("CoStr_2ds", _ToArray_2ds[_CoStr, _PyCharacter])
CoStr_3ds = TypeAliasType("CoStr_3ds", _ToArray_3ds[_CoStr, _PyCharacter])
CoStr_1nd = TypeAliasType("CoStr_1nd", _ToArray_1nd[_CoStr, _PyCharacter])
CoStr_2nd = TypeAliasType("CoStr_2nd", _ToArray_2nd[_CoStr, _PyCharacter])
CoStr_3nd = TypeAliasType("CoStr_3nd", _ToArray_3nd[_CoStr, _PyCharacter])

###
# DType-likes
# TODO
