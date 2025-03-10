# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
import datetime as dt
import decimal
import fractions
from collections.abc import Sequence
from typing import Any, ClassVar, TypeAlias, final, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy._typing import _8Bit, _16Bit, _32Bit, _64Bit, _NBitLongDouble

###
# Type parameters

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
_ScalarT0 = TypeVar("_ScalarT0", bound=np.generic, default=Any)
_ToT = TypeVar("_ToT")

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

# Type-check-only equivalent of `optype.Just`, see https://github.com/jorenham/optype#just
@type_check_only
@final  # the pyright and mypy errors are false positives because of this @final
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
class SequenceND(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | SequenceND[_T_co]: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

# we can't use a custom Sequence type due to some mypy bug
Sequence2D: TypeAlias = Sequence[Sequence[_T]]
Sequence3D: TypeAlias = Sequence[Sequence[Sequence[_T]]]

# nested sequences with at least k dims, e.g. `2nd` denotes a dimensionality in the interval [2, n]
# NOTE: The seemingly redundant `Sequence`s are required to work around a pyright bug
Sequence1ND: TypeAlias = Sequence[_T] | Sequence[SequenceND[_T]]
Sequence2ND: TypeAlias = Sequence[Sequence[_T]] | Sequence[Sequence[SequenceND[_T]]]
Sequence3ND: TypeAlias = Sequence[Sequence[Sequence[_T]]] | Sequence[Sequence[Sequence[SequenceND[_T]]]]

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
MArray3D = TypeAliasType("MArray3D", np.ma.MaskedArray[tuple[int, int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))

Matrix = TypeAliasType("Matrix", np.matrix[tuple[int, int], np.dtype[_ScalarT0]], type_params=(_ScalarT0,))

###
# sized abstract scalar type aliases

Floating64: TypeAlias = np.floating[_64Bit]  # accepts `float64` and `double`
CFloating64: TypeAlias = np.complexfloating[_64Bit, _64Bit]  # accepts `complex128` and `cdouble`

Integer8: TypeAlias = np.integer[_8Bit]  # accepts `int8`, `byte`, `uint8`, and `ubyte`
Integer16: TypeAlias = np.integer[_16Bit]  # accepts `int16`, `short`, `uint16`, and `ushort`
Integer32: TypeAlias = np.integer[_32Bit]  # accepts `int32`, `intc`, `uint32`, and `uintc`
Integer64: TypeAlias = np.integer[_64Bit]  # accepts `int64`, `longlong`, `uint64`, and `ulonglong`

Inexact16: TypeAlias = np.inexact[_16Bit]  # accepts `float16` and `half`
Inexact32: TypeAlias = np.inexact[_32Bit]  # accepts `float32`, `single`, `complex64`, and `csingle`
Inexact64: TypeAlias = np.inexact[_64Bit]  # accepts `float64`, `double`, `complex128`, and `cdouble`
InexactLD: TypeAlias = np.inexact[_NBitLongDouble]  # accepts `longdouble` and `clongdouble`

Number8: TypeAlias = np.number[_8Bit]  # accepts `Integer8`
Number16: TypeAlias = np.number[_16Bit]  # accepts `Integer16` and `float16`
Number32: TypeAlias = np.number[_32Bit]  # accepts `Integer32` and `Inexact32`
Number64: TypeAlias = np.number[_64Bit]  # accepts `Integer64` and `Inexact64`

###
# helper aliases

_PyReal: TypeAlias = Is[int] | Is[float]
_PyInexact: TypeAlias = Is[float] | Is[complex]
_PyNumber: TypeAlias = Is[int] | _PyInexact
_PyCharacter: TypeAlias = Is[bytes] | Is[str]
# anything immutable that results in an `object_` dtype
_PyObject: TypeAlias = dt.time | decimal.Decimal | fractions.Fraction
_PyScalar: TypeAlias = complex | _PyCharacter | _PyObject

_ToArray2_0d: TypeAlias = CanArray0D[_ScalarT] | _ToT
_ToArray_nd: TypeAlias = CanArrayND[_ScalarT] | Sequence1ND[CanArrayND[_ScalarT]]
_ToArray2_nd: TypeAlias = CanArrayND[_ScalarT] | _ToT | Sequence1ND[_ToT | CanArrayND[_ScalarT]]

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

ToUIntP_nd = TypeAliasType("ToUIntP_nd", _ToArray_nd[np.uintp])
ToUIntP_0d = TypeAliasType("ToUIntP_0d", CanArray0D[np.uintp])
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
ToULongLong_0d = TypeAliasType("ToULongLong_0d", CanArray0D[np.ulonglong])
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

ToIntP_nd = TypeAliasType("ToIntP_nd", _ToArray2_nd[np.intp, Is[int]])
ToIntP_0d = TypeAliasType("ToIntP_0d", _ToArray2_0d[np.intp, Is[int]])
ToIntP_1d = TypeAliasType("ToIntP_1d", _ToArray2_1d[np.intp, Is[int]])
ToIntP_2d = TypeAliasType("ToIntP_2d", _ToArray2_2d[np.intp, Is[int]])
ToIntP_3d = TypeAliasType("ToIntP_3d", _ToArray2_3d[np.intp, Is[int]])
ToIntP_1ds = TypeAliasType("ToIntP_1ds", _ToArray2_1ds[np.intp, Is[int]])
ToIntP_2ds = TypeAliasType("ToIntP_2ds", _ToArray2_2ds[np.intp, Is[int]])
ToIntP_3ds = TypeAliasType("ToIntP_3ds", _ToArray2_3ds[np.intp, Is[int]])
ToIntP_1nd = TypeAliasType("ToIntP_1nd", _ToArray2_1nd[np.intp, Is[int]])
ToIntP_2nd = TypeAliasType("ToIntP_2nd", _ToArray2_2nd[np.intp, Is[int]])
ToIntP_3nd = TypeAliasType("ToIntP_3nd", _ToArray2_3nd[np.intp, Is[int]])

ToLongLong_nd = TypeAliasType("ToLongLong_nd", _ToArray_nd[np.longlong])
ToLongLong_0d = TypeAliasType("ToLongLong_0d", CanArray0D[np.longlong])
ToLongLong_1d = TypeAliasType("ToLongLong_1d", _ToArray_1d[np.longlong])
ToLongLong_2d = TypeAliasType("ToLongLong_2d", _ToArray_2d[np.longlong])
ToLongLong_3d = TypeAliasType("ToLongLong_3d", _ToArray_3d[np.longlong])
ToLongLong_1ds = TypeAliasType("ToLongLong_1ds", _ToArray_1ds[np.longlong])
ToLongLong_2ds = TypeAliasType("ToLongLong_2ds", _ToArray_2ds[np.longlong])
ToLongLong_3ds = TypeAliasType("ToLongLong_3ds", _ToArray_3ds[np.longlong])
ToLongLong_1nd = TypeAliasType("ToLongLong_1nd", _ToArray_1nd[np.longlong])
ToLongLong_2nd = TypeAliasType("ToLongLong_2nd", _ToArray_2nd[np.longlong])
ToLongLong_3nd = TypeAliasType("ToLongLong_3nd", _ToArray_3nd[np.longlong])

ToSInteger_nd = TypeAliasType("ToSInteger_nd", _ToArray2_nd[np.signedinteger, Is[int]])
ToSInteger_0d = TypeAliasType("ToSInteger_0d", _ToArray2_0d[np.signedinteger, Is[int]])
ToSInteger_1d = TypeAliasType("ToSInteger_1d", _ToArray2_1d[np.signedinteger, Is[int]])
ToSInteger_2d = TypeAliasType("ToSInteger_2d", _ToArray2_2d[np.signedinteger, Is[int]])
ToSInteger_3d = TypeAliasType("ToSInteger_3d", _ToArray2_3d[np.signedinteger, Is[int]])
ToSInteger_1ds = TypeAliasType("ToSInteger_1ds", _ToArray2_1ds[np.signedinteger, Is[int]])
ToSInteger_2ds = TypeAliasType("ToSInteger_2ds", _ToArray2_2ds[np.signedinteger, Is[int]])
ToSInteger_3ds = TypeAliasType("ToSInteger_3ds", _ToArray2_3ds[np.signedinteger, Is[int]])
ToSInteger_1nd = TypeAliasType("ToSInteger_1nd", _ToArray2_1nd[np.signedinteger, Is[int]])
ToSInteger_2nd = TypeAliasType("ToSInteger_2nd", _ToArray2_2nd[np.signedinteger, Is[int]])
ToSInteger_3nd = TypeAliasType("ToSInteger_3nd", _ToArray2_3nd[np.signedinteger, Is[int]])

# integers
ToInteger_nd = TypeAliasType("ToInteger_nd", _ToArray2_nd[np.integer, Is[int]])
ToInteger_0d = TypeAliasType("ToInteger_0d", _ToArray2_0d[np.integer, Is[int]])
ToInteger_1d = TypeAliasType("ToInteger_1d", _ToArray2_1d[np.integer, Is[int]])
ToInteger_2d = TypeAliasType("ToInteger_2d", _ToArray2_2d[np.integer, Is[int]])
ToInteger_3d = TypeAliasType("ToInteger_3d", _ToArray2_3d[np.integer, Is[int]])
ToInteger_1ds = TypeAliasType("ToInteger_1ds", _ToArray2_1ds[np.integer, Is[int]])
ToInteger_2ds = TypeAliasType("ToInteger_2ds", _ToArray2_2ds[np.integer, Is[int]])
ToInteger_3ds = TypeAliasType("ToInteger_3ds", _ToArray2_3ds[np.integer, Is[int]])
ToInteger_1nd = TypeAliasType("ToInteger_1nd", _ToArray2_1nd[np.integer, Is[int]])
ToInteger_2nd = TypeAliasType("ToInteger_2nd", _ToArray2_2nd[np.integer, Is[int]])
ToInteger_3nd = TypeAliasType("ToInteger_3nd", _ToArray2_3nd[np.integer, Is[int]])

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

ToFloat64_nd = TypeAliasType("ToFloat64_nd", _ToArray2_nd[Floating64, Is[float]])
ToFloat64_0d = TypeAliasType("ToFloat64_0d", _ToArray2_0d[Floating64, Is[float]])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _ToArray2_1d[Floating64, Is[float]])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _ToArray2_2d[Floating64, Is[float]])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _ToArray2_3d[Floating64, Is[float]])
ToFloat64_1ds = TypeAliasType("ToFloat64_1ds", _ToArray2_1ds[Floating64, Is[float]])
ToFloat64_2ds = TypeAliasType("ToFloat64_2ds", _ToArray2_2ds[Floating64, Is[float]])
ToFloat64_3ds = TypeAliasType("ToFloat64_3ds", _ToArray2_3ds[Floating64, Is[float]])
ToFloat64_1nd = TypeAliasType("ToFloat64_1nd", _ToArray2_1nd[Floating64, Is[float]])
ToFloat64_2nd = TypeAliasType("ToFloat64_2nd", _ToArray2_2nd[Floating64, Is[float]])
ToFloat64_3nd = TypeAliasType("ToFloat64_3nd", _ToArray2_3nd[Floating64, Is[float]])

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

ToFloating_nd = TypeAliasType("ToFloating_nd", _ToArray2_nd[np.floating, Is[float]])
ToFloating_0d = TypeAliasType("ToFloating_0d", _ToArray2_0d[np.floating, Is[float]])
ToFloating_1d = TypeAliasType("ToFloating_1d", _ToArray2_1d[np.floating, Is[float]])
ToFloating_2d = TypeAliasType("ToFloating_2d", _ToArray2_2d[np.floating, Is[float]])
ToFloating_3d = TypeAliasType("ToFloating_3d", _ToArray2_3d[np.floating, Is[float]])
ToFloating_1ds = TypeAliasType("ToFloating_1ds", _ToArray2_1ds[np.floating, Is[float]])
ToFloating_2ds = TypeAliasType("ToFloating_2ds", _ToArray2_2ds[np.floating, Is[float]])
ToFloating_3ds = TypeAliasType("ToFloating_3ds", _ToArray2_3ds[np.floating, Is[float]])
ToFloating_1nd = TypeAliasType("ToFloating_1nd", _ToArray2_1nd[np.floating, Is[float]])
ToFloating_2nd = TypeAliasType("ToFloating_2nd", _ToArray2_2nd[np.floating, Is[float]])
ToFloating_3nd = TypeAliasType("ToFloating_3nd", _ToArray2_3nd[np.floating, Is[float]])

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

ToComplex128_nd = TypeAliasType("ToComplex128_nd", _ToArray2_nd[CFloating64, Is[complex]])
ToComplex128_0d = TypeAliasType("ToComplex128_0d", _ToArray2_0d[CFloating64, Is[complex]])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _ToArray2_1d[CFloating64, Is[complex]])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _ToArray2_2d[CFloating64, Is[complex]])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _ToArray2_3d[CFloating64, Is[complex]])
ToComplex128_1ds = TypeAliasType("ToComplex128_1ds", _ToArray2_1ds[CFloating64, Is[complex]])
ToComplex128_2ds = TypeAliasType("ToComplex128_2ds", _ToArray2_2ds[CFloating64, Is[complex]])
ToComplex128_3ds = TypeAliasType("ToComplex128_3ds", _ToArray2_3ds[CFloating64, Is[complex]])
ToComplex128_1nd = TypeAliasType("ToComplex128_1nd", _ToArray2_1nd[CFloating64, Is[complex]])
ToComplex128_2nd = TypeAliasType("ToComplex128_2nd", _ToArray2_2nd[CFloating64, Is[complex]])
ToComplex128_3nd = TypeAliasType("ToComplex128_3nd", _ToArray2_3nd[CFloating64, Is[complex]])

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

ToComplex_nd = TypeAliasType("ToComplex_nd", _ToArray2_nd[np.complexfloating, Is[complex]])
ToComplex_0d = TypeAliasType("ToComplex_0d", _ToArray2_0d[np.complexfloating, Is[complex]])
ToComplex_1d = TypeAliasType("ToComplex_1d", _ToArray2_1d[np.complexfloating, Is[complex]])
ToComplex_2d = TypeAliasType("ToComplex_2d", _ToArray2_2d[np.complexfloating, Is[complex]])
ToComplex_3d = TypeAliasType("ToComplex_3d", _ToArray2_3d[np.complexfloating, Is[complex]])
ToComplex_1ds = TypeAliasType("ToComplex_1ds", _ToArray2_1ds[np.complexfloating, Is[complex]])
ToComplex_2ds = TypeAliasType("ToComplex_2ds", _ToArray2_2ds[np.complexfloating, Is[complex]])
ToComplex_3ds = TypeAliasType("ToComplex_3ds", _ToArray2_3ds[np.complexfloating, Is[complex]])
ToComplex_1nd = TypeAliasType("ToComplex_1nd", _ToArray2_1nd[np.complexfloating, Is[complex]])
ToComplex_2nd = TypeAliasType("ToComplex_2nd", _ToArray2_2nd[np.complexfloating, Is[complex]])
ToComplex_3nd = TypeAliasType("ToComplex_3nd", _ToArray2_3nd[np.complexfloating, Is[complex]])

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
ToBytes_nd = TypeAliasType("ToBytes_nd", _ToArray2_nd[_ToBytes, Is[bytes]])
ToBytes_0d = TypeAliasType("ToBytes_0d", _ToArray2_0d[_ToBytes, Is[bytes]])
ToBytes_1d = TypeAliasType("ToBytes_1d", _ToArray2_1d[_ToBytes, Is[bytes]])
ToBytes_2d = TypeAliasType("ToBytes_2d", _ToArray2_2d[_ToBytes, Is[bytes]])
ToBytes_3d = TypeAliasType("ToBytes_3d", _ToArray2_3d[_ToBytes, Is[bytes]])
ToBytes_1ds = TypeAliasType("ToBytes_1ds", _ToArray2_1ds[_ToBytes, Is[bytes]])
ToBytes_2ds = TypeAliasType("ToBytes_2ds", _ToArray2_2ds[_ToBytes, Is[bytes]])
ToBytes_3ds = TypeAliasType("ToBytes_3ds", _ToArray2_3ds[_ToBytes, Is[bytes]])
ToBytes_1nd = TypeAliasType("ToBytes_1nd", _ToArray2_1nd[_ToBytes, Is[bytes]])
ToBytes_2nd = TypeAliasType("ToBytes_2nd", _ToArray2_2nd[_ToBytes, Is[bytes]])
ToBytes_3nd = TypeAliasType("ToBytes_3nd", _ToArray2_3nd[_ToBytes, Is[bytes]])

_ToStr: TypeAlias = np.character[str]
ToStr_nd = TypeAliasType("ToStr_nd", _ToArray2_nd[_ToStr, Is[str]])
ToStr_0d = TypeAliasType("ToStr_0d", _ToArray2_0d[_ToStr, Is[str]])
ToStr_1d = TypeAliasType("ToStr_1d", _ToArray2_1d[_ToStr, Is[str]])
ToStr_2d = TypeAliasType("ToStr_2d", _ToArray2_2d[_ToStr, Is[str]])
ToStr_3d = TypeAliasType("ToStr_3d", _ToArray2_3d[_ToStr, Is[str]])
ToStr_1ds = TypeAliasType("ToStr_1ds", _ToArray2_1ds[_ToStr, Is[str]])
ToStr_2ds = TypeAliasType("ToStr_2ds", _ToArray2_2ds[_ToStr, Is[str]])
ToStr_3ds = TypeAliasType("ToStr_3ds", _ToArray2_3ds[_ToStr, Is[str]])
ToStr_1nd = TypeAliasType("ToStr_1nd", _ToArray2_1nd[_ToStr, Is[str]])
ToStr_2nd = TypeAliasType("ToStr_2nd", _ToArray2_2nd[_ToStr, Is[str]])
ToStr_3nd = TypeAliasType("ToStr_3nd", _ToArray2_3nd[_ToStr, Is[str]])

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

###
# Coercible (overlapping) scalar- and array-likes

_CoInteger8: TypeAlias = Integer8 | _ToBool
_CoInteger16: TypeAlias = Integer16 | _CoInteger8
_CoInteger32: TypeAlias = Integer32 | _CoInteger16
_CoNumber16: TypeAlias = Number16 | _CoInteger8

_CoInt8: TypeAlias = np.int8 | _ToBool
_CoUInt8: TypeAlias = np.uint8 | _ToBool
_CoInt16: TypeAlias = np.int16 | _CoInteger8
_CoUInt16: TypeAlias = np.uint16 | _CoUInt8
_CoInt32: TypeAlias = np.int32 | _CoInteger16
_CoUInt32: TypeAlias = np.uint32 | _CoUInt16
_CoLong: TypeAlias = np.long | _CoInt32
_CoULong: TypeAlias = np.ulong | _CoUInt32
_CoIntP: TypeAlias = np.intp | _CoInt32
_CoUIntP: TypeAlias = np.uintp | _CoUInt32
_CoInt64: TypeAlias = np.int64 | _CoInteger32
_CoUInt64: TypeAlias = np.uint64 | _CoUInt32
_CoSInteger: TypeAlias = np.signedinteger | _CoInteger32
_CoUInteger: TypeAlias = np.unsignedinteger | _ToBool
_CoInteger: TypeAlias = np.integer | _ToBool

_CoFloat16: TypeAlias = np.float16 | _CoInteger8
_CoFloat32: TypeAlias = np.float32 | _CoNumber16
_CoFloat64: TypeAlias = Floating64 | np.float32 | Number16 | _CoInteger
_CoFloating: TypeAlias = np.floating | _CoInteger

_CoComplex64: TypeAlias = Number32 | _CoNumber16
_CoComplex128: TypeAlias = Number64 | _CoComplex64
_CoComplex: TypeAlias = np.number | _ToBool

_CoTimeDelta: TypeAlias = _ToTimeDelta | _CoInteger
_CoDateTime: TypeAlias = _ToDateTime | _ToTimeDelta

# unsigned integers
CoUInt8_nd = TypeAliasType("CoUInt8_nd", _ToArray2_nd[_CoUInt8, bool])
CoUInt8_0d = TypeAliasType("CoUInt8_0d", _ToArray2_0d[_CoUInt8, bool])
CoUInt8_1d = TypeAliasType("CoUInt8_1d", _ToArray2_1d[_CoUInt8, bool])
CoUInt8_2d = TypeAliasType("CoUInt8_2d", _ToArray2_2d[_CoUInt8, bool])
CoUInt8_3d = TypeAliasType("CoUInt8_3d", _ToArray2_3d[_CoUInt8, bool])
CoUInt8_1ds = TypeAliasType("CoUInt8_1ds", _ToArray2_1ds[_CoUInt8, bool])
CoUInt8_2ds = TypeAliasType("CoUInt8_2ds", _ToArray2_2ds[_CoUInt8, bool])
CoUInt8_3ds = TypeAliasType("CoUInt8_3ds", _ToArray2_3ds[_CoUInt8, bool])
CoUInt8_1nd = TypeAliasType("CoUInt8_1nd", _ToArray2_1nd[_CoUInt8, bool])
CoUInt8_2nd = TypeAliasType("CoUInt8_2nd", _ToArray2_2nd[_CoUInt8, bool])
CoUInt8_3nd = TypeAliasType("CoUInt8_3nd", _ToArray2_3nd[_CoUInt8, bool])

CoUInt16_nd = TypeAliasType("CoUInt16_nd", _ToArray2_nd[_CoUInt16, bool])
CoUInt16_0d = TypeAliasType("CoUInt16_0d", _ToArray2_0d[_CoUInt16, bool])
CoUInt16_1d = TypeAliasType("CoUInt16_1d", _ToArray2_1d[_CoUInt16, bool])
CoUInt16_2d = TypeAliasType("CoUInt16_2d", _ToArray2_2d[_CoUInt16, bool])
CoUInt16_3d = TypeAliasType("CoUInt16_3d", _ToArray2_3d[_CoUInt16, bool])
CoUInt16_1ds = TypeAliasType("CoUInt16_1ds", _ToArray2_1ds[_CoUInt16, bool])
CoUInt16_2ds = TypeAliasType("CoUInt16_2ds", _ToArray2_2ds[_CoUInt16, bool])
CoUInt16_3ds = TypeAliasType("CoUInt16_3ds", _ToArray2_3ds[_CoUInt16, bool])
CoUInt16_1nd = TypeAliasType("CoUInt16_1nd", _ToArray2_1nd[_CoUInt16, bool])
CoUInt16_2nd = TypeAliasType("CoUInt16_2nd", _ToArray2_2nd[_CoUInt16, bool])
CoUInt16_3nd = TypeAliasType("CoUInt16_3nd", _ToArray2_3nd[_CoUInt16, bool])

CoUInt32_nd = TypeAliasType("CoUInt32_nd", _ToArray2_nd[_CoUInt32, bool])
CoUInt32_0d = TypeAliasType("CoUInt32_0d", _ToArray2_0d[_CoUInt32, bool])
CoUInt32_1d = TypeAliasType("CoUInt32_1d", _ToArray2_1d[_CoUInt32, bool])
CoUInt32_2d = TypeAliasType("CoUInt32_2d", _ToArray2_2d[_CoUInt32, bool])
CoUInt32_3d = TypeAliasType("CoUInt32_3d", _ToArray2_3d[_CoUInt32, bool])
CoUInt32_1ds = TypeAliasType("CoUInt32_1ds", _ToArray2_1ds[_CoUInt32, bool])
CoUInt32_2ds = TypeAliasType("CoUInt32_2ds", _ToArray2_2ds[_CoUInt32, bool])
CoUInt32_3ds = TypeAliasType("CoUInt32_3ds", _ToArray2_3ds[_CoUInt32, bool])
CoUInt32_1nd = TypeAliasType("CoUInt32_1nd", _ToArray2_1nd[_CoUInt32, bool])
CoUInt32_2nd = TypeAliasType("CoUInt32_2nd", _ToArray2_2nd[_CoUInt32, bool])
CoUInt32_3nd = TypeAliasType("CoUInt32_3nd", _ToArray2_3nd[_CoUInt32, bool])

CoUInt64_nd = TypeAliasType("CoUInt64_nd", _ToArray2_nd[_CoUInt64, bool])
CoUInt64_0d = TypeAliasType("CoUInt64_0d", _ToArray2_0d[_CoUInt64, bool])
CoUInt64_1d = TypeAliasType("CoUInt64_1d", _ToArray2_1d[_CoUInt64, bool])
CoUInt64_2d = TypeAliasType("CoUInt64_2d", _ToArray2_2d[_CoUInt64, bool])
CoUInt64_3d = TypeAliasType("CoUInt64_3d", _ToArray2_3d[_CoUInt64, bool])
CoUInt64_1ds = TypeAliasType("CoUInt64_1ds", _ToArray2_1ds[_CoUInt64, bool])
CoUInt64_2ds = TypeAliasType("CoUInt64_2ds", _ToArray2_2ds[_CoUInt64, bool])
CoUInt64_3ds = TypeAliasType("CoUInt64_3ds", _ToArray2_3ds[_CoUInt64, bool])
CoUInt64_1nd = TypeAliasType("CoUInt64_1nd", _ToArray2_1nd[_CoUInt64, bool])
CoUInt64_2nd = TypeAliasType("CoUInt64_2nd", _ToArray2_2nd[_CoUInt64, bool])
CoUInt64_3nd = TypeAliasType("CoUInt64_3nd", _ToArray2_3nd[_CoUInt64, bool])

CoULong_nd = TypeAliasType("CoULong_nd", _ToArray2_nd[_CoULong, bool])
CoULong_0d = TypeAliasType("CoULong_0d", _ToArray2_0d[_CoULong, bool])
CoULong_1d = TypeAliasType("CoULong_1d", _ToArray2_1d[_CoULong, bool])
CoULong_2d = TypeAliasType("CoULong_2d", _ToArray2_2d[_CoULong, bool])
CoULong_3d = TypeAliasType("CoULong_3d", _ToArray2_3d[_CoULong, bool])
CoULong_1ds = TypeAliasType("CoULong_1ds", _ToArray2_1ds[_CoULong, bool])
CoULong_2ds = TypeAliasType("CoULong_2ds", _ToArray2_2ds[_CoULong, bool])
CoULong_3ds = TypeAliasType("CoULong_3ds", _ToArray2_3ds[_CoULong, bool])
CoULong_1nd = TypeAliasType("CoULong_1nd", _ToArray2_1nd[_CoULong, bool])
CoULong_2nd = TypeAliasType("CoULong_2nd", _ToArray2_2nd[_CoULong, bool])
CoULong_3nd = TypeAliasType("CoULong_3nd", _ToArray2_3nd[_CoULong, bool])

CoUIntP_nd = TypeAliasType("CoUIntP_nd", _ToArray2_nd[_CoUIntP, bool])
CoUIntP_0d = TypeAliasType("CoUIntP_0d", _ToArray2_0d[_CoUIntP, bool])
CoUIntP_1d = TypeAliasType("CoUIntP_1d", _ToArray2_1d[_CoUIntP, bool])
CoUIntP_2d = TypeAliasType("CoUIntP_2d", _ToArray2_2d[_CoUIntP, bool])
CoUIntP_3d = TypeAliasType("CoUIntP_3d", _ToArray2_3d[_CoUIntP, bool])
CoUIntP_1ds = TypeAliasType("CoUIntP_1ds", _ToArray2_1ds[_CoUIntP, bool])
CoUIntP_2ds = TypeAliasType("CoUIntP_2ds", _ToArray2_2ds[_CoUIntP, bool])
CoUIntP_3ds = TypeAliasType("CoUIntP_3ds", _ToArray2_3ds[_CoUIntP, bool])
CoUIntP_1nd = TypeAliasType("CoUIntP_1nd", _ToArray2_1nd[_CoUIntP, bool])
CoUIntP_2nd = TypeAliasType("CoUIntP_2nd", _ToArray2_2nd[_CoUIntP, bool])
CoUIntP_3nd = TypeAliasType("CoUIntP_3nd", _ToArray2_3nd[_CoUIntP, bool])

CoUInteger_nd = TypeAliasType("CoUInteger_nd", _ToArray2_nd[_CoUInteger, bool])
CoUInteger_0d = TypeAliasType("CoUInteger_0d", _ToArray2_0d[_CoUInteger, bool])
CoUInteger_1d = TypeAliasType("CoUInteger_1d", _ToArray2_1d[_CoUInteger, bool])
CoUInteger_2d = TypeAliasType("CoUInteger_2d", _ToArray2_2d[_CoUInteger, bool])
CoUInteger_3d = TypeAliasType("CoUInteger_3d", _ToArray2_3d[_CoUInteger, bool])
CoUInteger_1ds = TypeAliasType("CoUInteger_1ds", _ToArray2_1ds[_CoUInteger, bool])
CoUInteger_2ds = TypeAliasType("CoUInteger_2ds", _ToArray2_2ds[_CoUInteger, bool])
CoUInteger_3ds = TypeAliasType("CoUInteger_3ds", _ToArray2_3ds[_CoUInteger, bool])
CoUInteger_1nd = TypeAliasType("CoUInteger_1nd", _ToArray2_1nd[_CoUInteger, bool])
CoUInteger_2nd = TypeAliasType("CoUInteger_2nd", _ToArray2_2nd[_CoUInteger, bool])
CoUInteger_3nd = TypeAliasType("CoUInteger_3nd", _ToArray2_3nd[_CoUInteger, bool])

# signed integers
CoInt8_nd = TypeAliasType("CoInt8_nd", _ToArray2_nd[_CoInt8, bool])
CoInt8_0d = TypeAliasType("CoInt8_0d", _ToArray2_0d[_CoInt8, bool])
CoInt8_1d = TypeAliasType("CoInt8_1d", _ToArray2_1d[_CoInt8, bool])
CoInt8_2d = TypeAliasType("CoInt8_2d", _ToArray2_2d[_CoInt8, bool])
CoInt8_3d = TypeAliasType("CoInt8_3d", _ToArray2_3d[_CoInt8, bool])
CoInt8_1ds = TypeAliasType("CoInt8_1ds", _ToArray2_1ds[_CoInt8, bool])
CoInt8_2ds = TypeAliasType("CoInt8_2ds", _ToArray2_2ds[_CoInt8, bool])
CoInt8_3ds = TypeAliasType("CoInt8_3ds", _ToArray2_3ds[_CoInt8, bool])
CoInt8_1nd = TypeAliasType("CoInt8_1nd", _ToArray2_1nd[_CoInt8, bool])
CoInt8_2nd = TypeAliasType("CoInt8_2nd", _ToArray2_2nd[_CoInt8, bool])
CoInt8_3nd = TypeAliasType("CoInt8_3nd", _ToArray2_3nd[_CoInt8, bool])

CoInt16_nd = TypeAliasType("CoInt16_nd", _ToArray2_nd[_CoInt16, bool])
CoInt16_0d = TypeAliasType("CoInt16_0d", _ToArray2_0d[_CoInt16, bool])
CoInt16_1d = TypeAliasType("CoInt16_1d", _ToArray2_1d[_CoInt16, bool])
CoInt16_2d = TypeAliasType("CoInt16_2d", _ToArray2_2d[_CoInt16, bool])
CoInt16_3d = TypeAliasType("CoInt16_3d", _ToArray2_3d[_CoInt16, bool])
CoInt16_1ds = TypeAliasType("CoInt16_1ds", _ToArray2_1ds[_CoInt16, bool])
CoInt16_2ds = TypeAliasType("CoInt16_2ds", _ToArray2_2ds[_CoInt16, bool])
CoInt16_3ds = TypeAliasType("CoInt16_3ds", _ToArray2_3ds[_CoInt16, bool])
CoInt16_1nd = TypeAliasType("CoInt16_1nd", _ToArray2_1nd[_CoInt16, bool])
CoInt16_2nd = TypeAliasType("CoInt16_2nd", _ToArray2_2nd[_CoInt16, bool])
CoInt16_3nd = TypeAliasType("CoInt16_3nd", _ToArray2_3nd[_CoInt16, bool])

CoInt32_nd = TypeAliasType("CoInt32_nd", _ToArray2_nd[_CoInt32, bool])
CoInt32_0d = TypeAliasType("CoInt32_0d", _ToArray2_0d[_CoInt32, bool])
CoInt32_1d = TypeAliasType("CoInt32_1d", _ToArray2_1d[_CoInt32, bool])
CoInt32_2d = TypeAliasType("CoInt32_2d", _ToArray2_2d[_CoInt32, bool])
CoInt32_3d = TypeAliasType("CoInt32_3d", _ToArray2_3d[_CoInt32, bool])
CoInt32_1ds = TypeAliasType("CoInt32_1ds", _ToArray2_1ds[_CoInt32, bool])
CoInt32_2ds = TypeAliasType("CoInt32_2ds", _ToArray2_2ds[_CoInt32, bool])
CoInt32_3ds = TypeAliasType("CoInt32_3ds", _ToArray2_3ds[_CoInt32, bool])
CoInt32_1nd = TypeAliasType("CoInt32_1nd", _ToArray2_1nd[_CoInt32, bool])
CoInt32_2nd = TypeAliasType("CoInt32_2nd", _ToArray2_2nd[_CoInt32, bool])
CoInt32_3nd = TypeAliasType("CoInt32_3nd", _ToArray2_3nd[_CoInt32, bool])

CoInt64_nd = TypeAliasType("CoInt64_nd", _ToArray2_nd[_CoInt64, int])
CoInt64_0d = TypeAliasType("CoInt64_0d", _ToArray2_0d[_CoInt64, int])
CoInt64_1d = TypeAliasType("CoInt64_1d", _ToArray2_1d[_CoInt64, int])
CoInt64_2d = TypeAliasType("CoInt64_2d", _ToArray2_2d[_CoInt64, int])
CoInt64_3d = TypeAliasType("CoInt64_3d", _ToArray2_3d[_CoInt64, int])
CoInt64_1ds = TypeAliasType("CoInt64_1ds", _ToArray2_1ds[_CoInt64, int])
CoInt64_2ds = TypeAliasType("CoInt64_2ds", _ToArray2_2ds[_CoInt64, int])
CoInt64_3ds = TypeAliasType("CoInt64_3ds", _ToArray2_3ds[_CoInt64, int])
CoInt64_1nd = TypeAliasType("CoInt64_1nd", _ToArray2_1nd[_CoInt64, int])
CoInt64_2nd = TypeAliasType("CoInt64_2nd", _ToArray2_2nd[_CoInt64, int])
CoInt64_3nd = TypeAliasType("CoInt64_3nd", _ToArray2_3nd[_CoInt64, int])

CoLong_nd = TypeAliasType("CoLong_nd", _ToArray2_nd[_CoLong, bool])
CoLong_0d = TypeAliasType("CoLong_0d", _ToArray2_0d[_CoLong, bool])
CoLong_1d = TypeAliasType("CoLong_1d", _ToArray2_1d[_CoLong, bool])
CoLong_2d = TypeAliasType("CoLong_2d", _ToArray2_2d[_CoLong, bool])
CoLong_3d = TypeAliasType("CoLong_3d", _ToArray2_3d[_CoLong, bool])
CoLong_1ds = TypeAliasType("CoLong_1ds", _ToArray2_1ds[_CoLong, bool])
CoLong_2ds = TypeAliasType("CoLong_2ds", _ToArray2_2ds[_CoLong, bool])
CoLong_3ds = TypeAliasType("CoLong_3ds", _ToArray2_3ds[_CoLong, bool])
CoLong_1nd = TypeAliasType("CoLong_1nd", _ToArray2_1nd[_CoLong, bool])
CoLong_2nd = TypeAliasType("CoLong_2nd", _ToArray2_2nd[_CoLong, bool])
CoLong_3nd = TypeAliasType("CoLong_3nd", _ToArray2_3nd[_CoLong, bool])

CoIntP_nd = TypeAliasType("CoIntP_nd", _ToArray2_nd[_CoIntP, int])
CoIntP_0d = TypeAliasType("CoIntP_0d", _ToArray2_0d[_CoIntP, int])
CoIntP_1d = TypeAliasType("CoIntP_1d", _ToArray2_1d[_CoIntP, int])
CoIntP_2d = TypeAliasType("CoIntP_2d", _ToArray2_2d[_CoIntP, int])
CoIntP_3d = TypeAliasType("CoIntP_3d", _ToArray2_3d[_CoIntP, int])
CoIntP_1ds = TypeAliasType("CoIntP_1ds", _ToArray2_1ds[_CoIntP, int])
CoIntP_2ds = TypeAliasType("CoIntP_2ds", _ToArray2_2ds[_CoIntP, int])
CoIntP_3ds = TypeAliasType("CoIntP_3ds", _ToArray2_3ds[_CoIntP, int])
CoIntP_1nd = TypeAliasType("CoIntP_1nd", _ToArray2_1nd[_CoIntP, int])
CoIntP_2nd = TypeAliasType("CoIntP_2nd", _ToArray2_2nd[_CoIntP, int])
CoIntP_3nd = TypeAliasType("CoIntP_3nd", _ToArray2_3nd[_CoIntP, int])

CoSInteger_nd = TypeAliasType("CoSInteger_nd", _ToArray2_nd[_CoSInteger, int])
CoSInteger_0d = TypeAliasType("CoSInteger_0d", _ToArray2_0d[_CoSInteger, int])
CoSInteger_1d = TypeAliasType("CoSInteger_1d", _ToArray2_1d[_CoSInteger, int])
CoSInteger_2d = TypeAliasType("CoSInteger_2d", _ToArray2_2d[_CoSInteger, int])
CoSInteger_3d = TypeAliasType("CoSInteger_3d", _ToArray2_3d[_CoSInteger, int])
CoSInteger_1ds = TypeAliasType("CoSInteger_1ds", _ToArray2_1ds[_CoSInteger, int])
CoSInteger_2ds = TypeAliasType("CoSInteger_2ds", _ToArray2_2ds[_CoSInteger, int])
CoSInteger_3ds = TypeAliasType("CoSInteger_3ds", _ToArray2_3ds[_CoSInteger, int])
CoSInteger_1nd = TypeAliasType("CoSInteger_1nd", _ToArray2_1nd[_CoSInteger, int])
CoSInteger_2nd = TypeAliasType("CoSInteger_2nd", _ToArray2_2nd[_CoSInteger, int])
CoSInteger_3nd = TypeAliasType("CoSInteger_3nd", _ToArray2_3nd[_CoSInteger, int])

CoInteger_nd = TypeAliasType("CoInteger_nd", _ToArray2_nd[_CoInteger, int])
CoInteger_0d = TypeAliasType("CoInteger_0d", _ToArray2_0d[_CoInteger, int])
CoInteger_1d = TypeAliasType("CoInteger_1d", _ToArray2_1d[_CoInteger, int])
CoInteger_2d = TypeAliasType("CoInteger_2d", _ToArray2_2d[_CoInteger, int])
CoInteger_3d = TypeAliasType("CoInteger_3d", _ToArray2_3d[_CoInteger, int])
CoInteger_1ds = TypeAliasType("CoInteger_1ds", _ToArray2_1ds[_CoInteger, int])
CoInteger_2ds = TypeAliasType("CoInteger_2ds", _ToArray2_2ds[_CoInteger, int])
CoInteger_3ds = TypeAliasType("CoInteger_3ds", _ToArray2_3ds[_CoInteger, int])
CoInteger_1nd = TypeAliasType("CoInteger_1nd", _ToArray2_1nd[_CoInteger, int])
CoInteger_2nd = TypeAliasType("CoInteger_2nd", _ToArray2_2nd[_CoInteger, int])
CoInteger_3nd = TypeAliasType("CoInteger_3nd", _ToArray2_3nd[_CoInteger, int])

# real floats

CoFloat16_nd = TypeAliasType("CoFloat16_nd", _ToArray2_nd[_CoFloat16, bool])
CoFloat16_0d = TypeAliasType("CoFloat16_0d", _ToArray2_0d[_CoFloat16, bool])
CoFloat16_1d = TypeAliasType("CoFloat16_1d", _ToArray2_1d[_CoFloat16, bool])
CoFloat16_2d = TypeAliasType("CoFloat16_2d", _ToArray2_2d[_CoFloat16, bool])
CoFloat16_3d = TypeAliasType("CoFloat16_3d", _ToArray2_3d[_CoFloat16, bool])
CoFloat16_1ds = TypeAliasType("CoFloat16_1ds", _ToArray2_1ds[_CoFloat16, bool])
CoFloat16_2ds = TypeAliasType("CoFloat16_2ds", _ToArray2_2ds[_CoFloat16, bool])
CoFloat16_3ds = TypeAliasType("CoFloat16_3ds", _ToArray2_3ds[_CoFloat16, bool])
CoFloat16_1nd = TypeAliasType("CoFloat16_1nd", _ToArray2_1nd[_CoFloat16, bool])
CoFloat16_2nd = TypeAliasType("CoFloat16_2nd", _ToArray2_2nd[_CoFloat16, bool])
CoFloat16_3nd = TypeAliasType("CoFloat16_3nd", _ToArray2_3nd[_CoFloat16, bool])

CoFloat32_nd = TypeAliasType("CoFloat32_nd", _ToArray2_nd[_CoFloat32, bool])
CoFloat32_0d = TypeAliasType("CoFloat32_0d", _ToArray2_0d[_CoFloat32, bool])
CoFloat32_1d = TypeAliasType("CoFloat32_1d", _ToArray2_1d[_CoFloat32, bool])
CoFloat32_2d = TypeAliasType("CoFloat32_2d", _ToArray2_2d[_CoFloat32, bool])
CoFloat32_3d = TypeAliasType("CoFloat32_3d", _ToArray2_3d[_CoFloat32, bool])
CoFloat32_1ds = TypeAliasType("CoFloat32_1ds", _ToArray2_1ds[_CoFloat32, bool])
CoFloat32_2ds = TypeAliasType("CoFloat32_2ds", _ToArray2_2ds[_CoFloat32, bool])
CoFloat32_3ds = TypeAliasType("CoFloat32_3ds", _ToArray2_3ds[_CoFloat32, bool])
CoFloat32_1nd = TypeAliasType("CoFloat32_1nd", _ToArray2_1nd[_CoFloat32, bool])
CoFloat32_2nd = TypeAliasType("CoFloat32_2nd", _ToArray2_2nd[_CoFloat32, bool])
CoFloat32_3nd = TypeAliasType("CoFloat32_3nd", _ToArray2_3nd[_CoFloat32, bool])

CoFloat64_nd = TypeAliasType("CoFloat64_nd", _ToArray2_nd[_CoFloat64, float])
CoFloat64_0d = TypeAliasType("CoFloat64_0d", _ToArray2_0d[_CoFloat64, float])
CoFloat64_1d = TypeAliasType("CoFloat64_1d", _ToArray2_1d[_CoFloat64, float])
CoFloat64_2d = TypeAliasType("CoFloat64_2d", _ToArray2_2d[_CoFloat64, float])
CoFloat64_3d = TypeAliasType("CoFloat64_3d", _ToArray2_3d[_CoFloat64, float])
CoFloat64_1ds = TypeAliasType("CoFloat64_1ds", _ToArray2_1ds[_CoFloat64, float])
CoFloat64_2ds = TypeAliasType("CoFloat64_2ds", _ToArray2_2ds[_CoFloat64, float])
CoFloat64_3ds = TypeAliasType("CoFloat64_3ds", _ToArray2_3ds[_CoFloat64, float])
CoFloat64_1nd = TypeAliasType("CoFloat64_1nd", _ToArray2_1nd[_CoFloat64, float])
CoFloat64_2nd = TypeAliasType("CoFloat64_2nd", _ToArray2_2nd[_CoFloat64, float])
CoFloat64_3nd = TypeAliasType("CoFloat64_3nd", _ToArray2_3nd[_CoFloat64, float])

CoFloating_nd = TypeAliasType("CoFloating_nd", _ToArray2_nd[_CoFloating, float])
CoFloating_0d = TypeAliasType("CoFloating_0d", _ToArray2_0d[_CoFloating, float])
CoFloating_1d = TypeAliasType("CoFloating_1d", _ToArray2_1d[_CoFloating, float])
CoFloating_2d = TypeAliasType("CoFloating_2d", _ToArray2_2d[_CoFloating, float])
CoFloating_3d = TypeAliasType("CoFloating_3d", _ToArray2_3d[_CoFloating, float])
CoFloating_1ds = TypeAliasType("CoFloating_1ds", _ToArray2_1ds[_CoFloating, float])
CoFloating_2ds = TypeAliasType("CoFloating_2ds", _ToArray2_2ds[_CoFloating, float])
CoFloating_3ds = TypeAliasType("CoFloating_3ds", _ToArray2_3ds[_CoFloating, float])
CoFloating_1nd = TypeAliasType("CoFloating_1nd", _ToArray2_1nd[_CoFloating, float])
CoFloating_2nd = TypeAliasType("CoFloating_2nd", _ToArray2_2nd[_CoFloating, float])
CoFloating_3nd = TypeAliasType("CoFloating_3nd", _ToArray2_3nd[_CoFloating, float])

# complex floats
CoComplex64_nd = TypeAliasType("CoComplex64_nd", _ToArray2_nd[_CoComplex64, bool])
CoComplex64_0d = TypeAliasType("CoComplex64_0d", _ToArray2_0d[_CoComplex64, bool])
CoComplex64_1d = TypeAliasType("CoComplex64_1d", _ToArray2_1d[_CoComplex64, bool])
CoComplex64_2d = TypeAliasType("CoComplex64_2d", _ToArray2_2d[_CoComplex64, bool])
CoComplex64_3d = TypeAliasType("CoComplex64_3d", _ToArray2_3d[_CoComplex64, bool])
CoComplex64_1ds = TypeAliasType("CoComplex64_1ds", _ToArray2_1ds[_CoComplex64, bool])
CoComplex64_2ds = TypeAliasType("CoComplex64_2ds", _ToArray2_2ds[_CoComplex64, bool])
CoComplex64_3ds = TypeAliasType("CoComplex64_3ds", _ToArray2_3ds[_CoComplex64, bool])
CoComplex64_1nd = TypeAliasType("CoComplex64_1nd", _ToArray2_1nd[_CoComplex64, bool])
CoComplex64_2nd = TypeAliasType("CoComplex64_2nd", _ToArray2_2nd[_CoComplex64, bool])
CoComplex64_3nd = TypeAliasType("CoComplex64_3nd", _ToArray2_3nd[_CoComplex64, bool])

CoComplex128_nd = TypeAliasType("CoComplex128_nd", _ToArray2_nd[_CoComplex128, complex])
CoComplex128_0d = TypeAliasType("CoComplex128_0d", _ToArray2_0d[_CoComplex128, complex])
CoComplex128_1d = TypeAliasType("CoComplex128_1d", _ToArray2_1d[_CoComplex128, complex])
CoComplex128_2d = TypeAliasType("CoComplex128_2d", _ToArray2_2d[_CoComplex128, complex])
CoComplex128_3d = TypeAliasType("CoComplex128_3d", _ToArray2_3d[_CoComplex128, complex])
CoComplex128_1ds = TypeAliasType("CoComplex128_1ds", _ToArray2_1ds[_CoComplex128, complex])
CoComplex128_2ds = TypeAliasType("CoComplex128_2ds", _ToArray2_2ds[_CoComplex128, complex])
CoComplex128_3ds = TypeAliasType("CoComplex128_3ds", _ToArray2_3ds[_CoComplex128, complex])
CoComplex128_1nd = TypeAliasType("CoComplex128_1nd", _ToArray2_1nd[_CoComplex128, complex])
CoComplex128_2nd = TypeAliasType("CoComplex128_2nd", _ToArray2_2nd[_CoComplex128, complex])
CoComplex128_3nd = TypeAliasType("CoComplex128_3nd", _ToArray2_3nd[_CoComplex128, complex])

CoComplex_nd = TypeAliasType("CoComplex_nd", _ToArray2_nd[_CoComplex, complex])
CoComplex_0d = TypeAliasType("CoComplex_0d", _ToArray2_0d[_CoComplex, complex])
CoComplex_1d = TypeAliasType("CoComplex_1d", _ToArray2_1d[_CoComplex, complex])
CoComplex_2d = TypeAliasType("CoComplex_2d", _ToArray2_2d[_CoComplex, complex])
CoComplex_3d = TypeAliasType("CoComplex_3d", _ToArray2_3d[_CoComplex, complex])
CoComplex_1ds = TypeAliasType("CoComplex_1ds", _ToArray2_1ds[_CoComplex, complex])
CoComplex_2ds = TypeAliasType("CoComplex_2ds", _ToArray2_2ds[_CoComplex, complex])
CoComplex_3ds = TypeAliasType("CoComplex_3ds", _ToArray2_3ds[_CoComplex, complex])
CoComplex_1nd = TypeAliasType("CoComplex_1nd", _ToArray2_1nd[_CoComplex, complex])
CoComplex_2nd = TypeAliasType("CoComplex_2nd", _ToArray2_2nd[_CoComplex, complex])
CoComplex_3nd = TypeAliasType("CoComplex_3nd", _ToArray2_3nd[_CoComplex, complex])

# temporal
CoTimeDelta_nd = TypeAliasType("CoTimeDelta_nd", _ToArray2_nd[_CoTimeDelta, int])
CoTimeDelta_0d = TypeAliasType("CoTimeDelta_0d", _ToArray2_0d[_CoTimeDelta, int])
CoTimeDelta_1d = TypeAliasType("CoTimeDelta_1d", _ToArray2_1d[_CoTimeDelta, int])
CoTimeDelta_2d = TypeAliasType("CoTimeDelta_2d", _ToArray2_2d[_CoTimeDelta, int])
CoTimeDelta_3d = TypeAliasType("CoTimeDelta_3d", _ToArray2_3d[_CoTimeDelta, int])
CoTimeDelta_1ds = TypeAliasType("CoTimeDelta_1ds", _ToArray2_1ds[_CoTimeDelta, int])
CoTimeDelta_2ds = TypeAliasType("CoTimeDelta_2ds", _ToArray2_2ds[_CoTimeDelta, int])
CoTimeDelta_3ds = TypeAliasType("CoTimeDelta_3ds", _ToArray2_3ds[_CoTimeDelta, int])
CoTimeDelta_1nd = TypeAliasType("CoTimeDelta_1nd", _ToArray2_1nd[_CoTimeDelta, int])
CoTimeDelta_2nd = TypeAliasType("CoTimeDelta_2nd", _ToArray2_2nd[_CoTimeDelta, int])
CoTimeDelta_3nd = TypeAliasType("CoTimeDelta_3nd", _ToArray2_3nd[_CoTimeDelta, int])

CoDateTime_nd = TypeAliasType("CoDateTime_nd", _ToArray_nd[_CoDateTime])
CoDateTime_0d = TypeAliasType("CoDateTime_0d", CanArray0D[_CoDateTime])
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
CoBytes_nd = TypeAliasType("CoBytes_nd", _ToArray2_nd[_ToBytes, Is[bytes]])
CoBytes_0d = TypeAliasType("CoBytes_0d", _ToArray2_0d[_ToBytes, Is[bytes]])
CoBytes_1d = TypeAliasType("CoBytes_1d", _ToArray2_1d[_ToBytes, Is[bytes]])
CoBytes_2d = TypeAliasType("CoBytes_2d", _ToArray2_2d[_ToBytes, Is[bytes]])
CoBytes_3d = TypeAliasType("CoBytes_3d", _ToArray2_3d[_ToBytes, Is[bytes]])
CoBytes_1ds = TypeAliasType("CoBytes_1ds", _ToArray2_1ds[_ToBytes, Is[bytes]])
CoBytes_2ds = TypeAliasType("CoBytes_2ds", _ToArray2_2ds[_ToBytes, Is[bytes]])
CoBytes_3ds = TypeAliasType("CoBytes_3ds", _ToArray2_3ds[_ToBytes, Is[bytes]])
CoBytes_1nd = TypeAliasType("CoBytes_1nd", _ToArray2_1nd[_ToBytes, Is[bytes]])
CoBytes_2nd = TypeAliasType("CoBytes_2nd", _ToArray2_2nd[_ToBytes, Is[bytes]])
CoBytes_3nd = TypeAliasType("CoBytes_3nd", _ToArray2_3nd[_ToBytes, Is[bytes]])

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
# TODO
