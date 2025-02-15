# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
from typing import Any, TypeAlias, final, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar

import numpy as np

###
# Type parameters

_T = TypeVar("_T", default=Any)
_T_co = TypeVar("_T_co", covariant=True)
_BuiltinT = TypeVar("_BuiltinT")
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...], default=tuple[int, ...])
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)

###
# Protocols

# A slimmed down version of `collections.abc.Sequence`, for faster type-checking.
@type_check_only
class Sequence_1d(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

# A slimmed down version of `_NestedSequence`, based on `optype.numpy.SequenceND`.
# https://github.com/jorenham/optype
@type_check_only
class Sequence_nd(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | Sequence_nd[_T_co]: ...
    def __contains__(self, x: object, /) -> bool: ...
    def index(self, value: Any, /) -> int: ...

@type_check_only
class CanArray(Protocol[_ScalarT_co, _ShapeT_co]):
    def __array__(self, /) -> np.ndarray[_ShapeT_co, np.dtype[_ScalarT_co]]: ...

# A shape-typed version of `numpy._typing._CanArray`, parametrized by the
# scalar-type and shape-type, and excludes `np.generic` scalars (through `__len__`).
@type_check_only
class CanLenArray(CanArray[_ScalarT_co, _ShapeT_co], Protocol[_ScalarT_co, _ShapeT_co]):
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

###
# Helper aliases

_AsBool: TypeAlias = np.bool[Any]
_AsInt8: TypeAlias = np.int8
_AsInt16: TypeAlias = np.int16
_AsInt32: TypeAlias = np.int32
_AsInt64: TypeAlias = np.int64
_AsLong: TypeAlias = np.long
_AsIntP: TypeAlias = np.intp
_AsLongLong: TypeAlias = np.longlong
_AsUInt8: TypeAlias = np.uint8
_AsUInt16: TypeAlias = np.uint16
_AsUInt32: TypeAlias = np.uint32
_AsUInt64: TypeAlias = np.uint64
_AsULong: TypeAlias = np.ulong
_AsUIntP: TypeAlias = np.uintp
_AsULongLong: TypeAlias = np.ulonglong
_AsFloat16: TypeAlias = np.float16
_AsFloat32: TypeAlias = np.float32
_AsFloat64: TypeAlias = np.float64
_AsLongDouble: TypeAlias = np.longdouble | np.float96 | np.float128
_AsComplex64: TypeAlias = np.complex64
_AsComplex128: TypeAlias = np.complex128
_AsCLongDouble: TypeAlias = np.clongdouble | np.complex192 | np.complex256
_AsTimeDelta: TypeAlias = np.timedelta64[Any]
_AsDateTime: TypeAlias = np.datetime64[Any]
_AsBytes: TypeAlias = np.bytes_
_AsStr: TypeAlias = np.str_
_AsObject: TypeAlias = np.object_

_ToBool: TypeAlias = _AsBool
_ToInt8: TypeAlias = _AsInt8 | _ToBool
_ToInt16: TypeAlias = _AsInt16 | _AsUInt8 | _ToInt8
_ToInt32: TypeAlias = _AsInt32 | _AsUInt16 | _ToInt16
_ToInt64: TypeAlias = _AsInt64 | _AsUInt32 | _ToInt32
_ToLong: TypeAlias = _AsLong | _ToInt32
_ToIntP: TypeAlias = _AsIntP | _ToLong
_ToLongLong: TypeAlias = np.signedinteger | _ToUInt32
_ToUInt8: TypeAlias = _AsUInt8 | _ToBool
_ToUInt16: TypeAlias = _AsUInt16 | _ToUInt8
_ToUInt32: TypeAlias = _AsUInt32 | _ToUInt16
_ToUInt64: TypeAlias = _AsUInt64 | _ToUInt32
_ToULong: TypeAlias = _AsULong | _ToUInt32
_ToUIntP: TypeAlias = _AsUIntP | _ToULong
_ToULongLong: TypeAlias = np.unsignedinteger | _ToBool
_ToFloat16: TypeAlias = _AsFloat16 | _AsUInt8 | _AsInt16 | _ToBool
_ToFloat32: TypeAlias = _AsFloat32 | _AsUInt16 | np.int16 | _ToFloat16
_ToFloat64: TypeAlias = _AsFloat64 | _AsFloat32 | _AsFloat16 | np.integer | _ToBool
_ToLongDouble: TypeAlias = np.floating | np.integer | _ToBool
_ToComplex64: TypeAlias = _AsComplex64 | _ToFloat32
_ToComplex128: TypeAlias = _AsComplex128 | _AsComplex64 | _ToFloat64
_ToCLongDouble: TypeAlias = np.number | _ToBool
_ToTimeDelta: TypeAlias = _AsTimeDelta | np.integer | _ToBool
_ToDateTime: TypeAlias = _AsDateTime | _AsTimeDelta  # scalars may also accepts `integer | _ToBool`
_ToBytes: TypeAlias = _AsBytes
_ToStr: TypeAlias = np.character  # rougly equivalent to `str_ | bytes_`
_ToObject: TypeAlias = np.generic

_To1_0d: TypeAlias = _ScalarT | CanArray[_ScalarT, tuple[()]]
_To2_0d: TypeAlias = _ScalarT | _T | CanArray[_ScalarT, tuple[()]]

_To1_1d: TypeAlias = CanLenArray[_ScalarT, tuple[int]] | Sequence_1d[_To1_0d[_ScalarT]]
_To2_1d: TypeAlias = CanLenArray[_ScalarT, tuple[int]] | Sequence_1d[_To2_0d[_ScalarT, _T]]

_To1_2d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int]] | Sequence_1d[_To1_1d[_ScalarT]]
_To2_2d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int]] | Sequence_1d[_To2_1d[_ScalarT, _T]]

_To1_3d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int, int]] | Sequence_1d[_To1_2d[_ScalarT]]
_To2_3d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int, int]] | Sequence_1d[_To2_2d[_ScalarT, _T]]

_To1_nd: TypeAlias = CanLenArray[_ScalarT] | Sequence_nd[CanLenArray[_ScalarT]]
_To2_nd: TypeAlias = CanLenArray[_ScalarT] | Sequence_nd[_T | _ScalarT] | Sequence_nd[CanLenArray[_ScalarT]]

###
# Array-likes

# Non-overlapping scalar- and array-like aliases for all scalar types.
AsBool_0d = TypeAliasType("AsBool_0d", _To2_0d[_AsBool, bool])
AsBool_1d = TypeAliasType("AsBool_1d", _To2_1d[_AsBool, bool])
AsBool_2d = TypeAliasType("AsBool_2d", _To2_2d[_AsBool, bool])
AsBool_3d = TypeAliasType("AsBool_3d", _To2_3d[_AsBool, bool])
AsBool_nd = TypeAliasType("AsBool_nd", _To2_nd[_AsBool, bool])

AsInt8_0d = TypeAliasType("AsInt8_0d", _To1_0d[_AsInt8])
AsInt8_1d = TypeAliasType("AsInt8_1d", _To1_1d[_AsInt8])
AsInt8_2d = TypeAliasType("AsInt8_2d", _To1_2d[_AsInt8])
AsInt8_3d = TypeAliasType("AsInt8_3d", _To1_3d[_AsInt8])
AsInt8_nd = TypeAliasType("AsInt8_nd", _To1_nd[_AsInt8])

AsInt16_0d = TypeAliasType("AsInt16_0d", _To1_0d[_AsInt16])
AsInt16_1d = TypeAliasType("AsInt16_1d", _To1_1d[_AsInt16])
AsInt16_2d = TypeAliasType("AsInt16_2d", _To1_2d[_AsInt16])
AsInt16_3d = TypeAliasType("AsInt16_3d", _To1_3d[_AsInt16])
AsInt16_nd = TypeAliasType("AsInt16_nd", _To1_nd[_AsInt16])

AsInt32_0d = TypeAliasType("AsInt32_0d", _To1_0d[_AsInt32])
AsInt32_1d = TypeAliasType("AsInt32_1d", _To1_1d[_AsInt32])
AsInt32_2d = TypeAliasType("AsInt32_2d", _To1_2d[_AsInt32])
AsInt32_3d = TypeAliasType("AsInt32_3d", _To1_3d[_AsInt32])
AsInt32_nd = TypeAliasType("AsInt32_nd", _To1_nd[_AsInt32])

AsInt64_0d = TypeAliasType("AsInt64_0d", _To1_0d[_AsInt64])
AsInt64_1d = TypeAliasType("AsInt64_1d", _To1_1d[_AsInt64])
AsInt64_2d = TypeAliasType("AsInt64_2d", _To1_2d[_AsInt64])
AsInt64_3d = TypeAliasType("AsInt64_3d", _To1_3d[_AsInt64])
AsInt64_nd = TypeAliasType("AsInt64_nd", _To1_nd[_AsInt64])

AsLong_0d = TypeAliasType("AsLong_0d", _To1_0d[_AsLong])
AsLong_1d = TypeAliasType("AsLong_1d", _To1_1d[_AsLong])
AsLong_2d = TypeAliasType("AsLong_2d", _To1_2d[_AsLong])
AsLong_3d = TypeAliasType("AsLong_3d", _To1_3d[_AsLong])
AsLong_nd = TypeAliasType("AsLong_nd", _To1_nd[_AsLong])

AsIntP_0d = TypeAliasType("AsIntP_0d", _To2_0d[_AsIntP, Is[int]])
AsIntP_1d = TypeAliasType("AsIntP_1d", _To2_1d[_AsIntP, Is[int]])
AsIntP_2d = TypeAliasType("AsIntP_2d", _To2_2d[_AsIntP, Is[int]])
AsIntP_3d = TypeAliasType("AsIntP_3d", _To2_3d[_AsIntP, Is[int]])
AsIntP_nd = TypeAliasType("AsIntP_nd", _To2_nd[_AsIntP, Is[int]])

AsLongLong_0d = TypeAliasType("AsLongLong_0d", _To1_0d[_AsLongLong])
AsLongLong_1d = TypeAliasType("AsLongLong_1d", _To1_1d[_AsLongLong])
AsLongLong_2d = TypeAliasType("AsLongLong_2d", _To1_2d[_AsLongLong])
AsLongLong_3d = TypeAliasType("AsLongLong_3d", _To1_3d[_AsLongLong])
AsLongLong_nd = TypeAliasType("AsLongLong_nd", _To1_nd[_AsLongLong])

AsUInt8_0d = TypeAliasType("AsUInt8_0d", _To1_0d[_AsUInt8])
AsUInt8_1d = TypeAliasType("AsUInt8_1d", _To1_1d[_AsUInt8])
AsUInt8_2d = TypeAliasType("AsUInt8_2d", _To1_2d[_AsUInt8])
AsUInt8_3d = TypeAliasType("AsUInt8_3d", _To1_3d[_AsUInt8])
AsUInt8_nd = TypeAliasType("AsUInt8_nd", _To1_nd[_AsUInt8])

AsUInt16_0d = TypeAliasType("AsUInt16_0d", _To1_0d[_AsUInt16])
AsUInt16_1d = TypeAliasType("AsUInt16_1d", _To1_1d[_AsUInt16])
AsUInt16_2d = TypeAliasType("AsUInt16_2d", _To1_2d[_AsUInt16])
AsUInt16_3d = TypeAliasType("AsUInt16_3d", _To1_3d[_AsUInt16])
AsUInt16_nd = TypeAliasType("AsUInt16_nd", _To1_nd[_AsUInt16])

AsUInt32_0d = TypeAliasType("AsUInt32_0d", _To1_0d[_AsUInt32])
AsUInt32_1d = TypeAliasType("AsUInt32_1d", _To1_1d[_AsUInt32])
AsUInt32_2d = TypeAliasType("AsUInt32_2d", _To1_2d[_AsUInt32])
AsUInt32_3d = TypeAliasType("AsUInt32_3d", _To1_3d[_AsUInt32])
AsUInt32_nd = TypeAliasType("AsUInt32_nd", _To1_nd[_AsUInt32])

AsUInt64_0d = TypeAliasType("AsUInt64_0d", _To1_0d[_AsUInt64])
AsUInt64_1d = TypeAliasType("AsUInt64_1d", _To1_1d[_AsUInt64])
AsUInt64_2d = TypeAliasType("AsUInt64_2d", _To1_2d[_AsUInt64])
AsUInt64_3d = TypeAliasType("AsUInt64_3d", _To1_3d[_AsUInt64])
AsUInt64_nd = TypeAliasType("AsUInt64_nd", _To1_nd[_AsUInt64])

AsULong_0d = TypeAliasType("AsULong_0d", _To1_0d[_AsULong])
AsULong_1d = TypeAliasType("AsULong_1d", _To1_1d[_AsULong])
AsULong_2d = TypeAliasType("AsULong_2d", _To1_2d[_AsULong])
AsULong_3d = TypeAliasType("AsULong_3d", _To1_3d[_AsULong])
AsULong_nd = TypeAliasType("AsULong_nd", _To1_nd[_AsULong])

AsUIntP_0d = TypeAliasType("AsUIntP_0d", _To1_0d[_AsUIntP])
AsUIntP_1d = TypeAliasType("AsUIntP_1d", _To1_1d[_AsUIntP])
AsUIntP_2d = TypeAliasType("AsUIntP_2d", _To1_2d[_AsUIntP])
AsUIntP_3d = TypeAliasType("AsUIntP_3d", _To1_3d[_AsUIntP])
AsUIntP_nd = TypeAliasType("AsUIntP_nd", _To1_nd[_AsUIntP])

AsULongLong_0d = TypeAliasType("AsULongLong_0d", _To1_0d[_AsULongLong])
AsULongLong_1d = TypeAliasType("AsULongLong_1d", _To1_1d[_AsULongLong])
AsULongLong_2d = TypeAliasType("AsULongLong_2d", _To1_2d[_AsULongLong])
AsULongLong_3d = TypeAliasType("AsULongLong_3d", _To1_3d[_AsULongLong])
AsULongLong_nd = TypeAliasType("AsULongLong_nd", _To1_nd[_AsULongLong])

AsFloat16_0d = TypeAliasType("AsFloat16_0d", _To1_0d[_AsFloat16])
AsFloat16_1d = TypeAliasType("AsFloat16_1d", _To1_1d[_AsFloat16])
AsFloat16_2d = TypeAliasType("AsFloat16_2d", _To1_2d[_AsFloat16])
AsFloat16_3d = TypeAliasType("AsFloat16_3d", _To1_3d[_AsFloat16])
AsFloat16_nd = TypeAliasType("AsFloat16_nd", _To1_nd[_AsFloat16])

AsFloat32_0d = TypeAliasType("AsFloat32_0d", _To1_0d[_AsFloat32])
AsFloat32_1d = TypeAliasType("AsFloat32_1d", _To1_1d[_AsFloat32])
AsFloat32_2d = TypeAliasType("AsFloat32_2d", _To1_2d[_AsFloat32])
AsFloat32_3d = TypeAliasType("AsFloat32_3d", _To1_3d[_AsFloat32])
AsFloat32_nd = TypeAliasType("AsFloat32_nd", _To1_nd[_AsFloat32])

AsFloat64_0d = TypeAliasType("AsFloat64_0d", _To2_0d[_AsFloat64, Is[float]])
AsFloat64_1d = TypeAliasType("AsFloat64_1d", _To2_1d[_AsFloat64, Is[float]])
AsFloat64_2d = TypeAliasType("AsFloat64_2d", _To2_2d[_AsFloat64, Is[float]])
AsFloat64_3d = TypeAliasType("AsFloat64_3d", _To2_3d[_AsFloat64, Is[float]])
AsFloat64_nd = TypeAliasType("AsFloat64_nd", _To2_nd[_AsFloat64, Is[float]])

AsLongDouble_0d = TypeAliasType("AsLongDouble_0d", _To1_0d[_AsLongDouble])
AsLongDouble_1d = TypeAliasType("AsLongDouble_1d", _To1_1d[_AsLongDouble])
AsLongDouble_2d = TypeAliasType("AsLongDouble_2d", _To1_2d[_AsLongDouble])
AsLongDouble_3d = TypeAliasType("AsLongDouble_3d", _To1_3d[_AsLongDouble])
AsLongDouble_nd = TypeAliasType("AsLongDouble_nd", _To1_nd[_AsLongDouble])

AsComplex64_0d = TypeAliasType("AsComplex64_0d", _To1_0d[_AsComplex64])
AsComplex64_1d = TypeAliasType("AsComplex64_1d", _To1_1d[_AsComplex64])
AsComplex64_2d = TypeAliasType("AsComplex64_2d", _To1_2d[_AsComplex64])
AsComplex64_3d = TypeAliasType("AsComplex64_3d", _To1_3d[_AsComplex64])
AsComplex64_nd = TypeAliasType("AsComplex64_nd", _To1_nd[_AsComplex64])

AsComplex128_0d = TypeAliasType("AsComplex128_0d", _To2_0d[_AsComplex128, Is[complex]])
AsComplex128_1d = TypeAliasType("AsComplex128_1d", _To2_1d[_AsComplex128, Is[complex]])
AsComplex128_2d = TypeAliasType("AsComplex128_2d", _To2_2d[_AsComplex128, Is[complex]])
AsComplex128_3d = TypeAliasType("AsComplex128_3d", _To2_3d[_AsComplex128, Is[complex]])
AsComplex128_nd = TypeAliasType("AsComplex128_nd", _To2_nd[_AsComplex128, Is[complex]])

AsCLongDouble_0d = TypeAliasType("AsCLongDouble_0d", _To1_0d[_AsCLongDouble])
AsCLongDouble_1d = TypeAliasType("AsCLongDouble_1d", _To1_1d[_AsCLongDouble])
AsCLongDouble_2d = TypeAliasType("AsCLongDouble_2d", _To1_2d[_AsCLongDouble])
AsCLongDouble_3d = TypeAliasType("AsCLongDouble_3d", _To1_3d[_AsCLongDouble])
AsCLongDouble_nd = TypeAliasType("AsCLongDouble_nd", _To1_nd[_AsCLongDouble])

AsTimeDelta_0d = TypeAliasType("AsTimeDelta_0d", _To1_0d[_AsTimeDelta])
AsTimeDelta_1d = TypeAliasType("AsTimeDelta_1d", _To1_1d[_AsTimeDelta])
AsTimeDelta_2d = TypeAliasType("AsTimeDelta_2d", _To1_2d[_AsTimeDelta])
AsTimeDelta_3d = TypeAliasType("AsTimeDelta_3d", _To1_3d[_AsTimeDelta])
AsTimeDelta_nd = TypeAliasType("AsTimeDelta_nd", _To1_nd[_AsTimeDelta])

AsDateTime_0d = TypeAliasType("AsDateTime_0d", _To1_0d[_AsDateTime])
AsDateTime_1d = TypeAliasType("AsDateTime_1d", _To1_1d[_AsDateTime])
AsDateTime_2d = TypeAliasType("AsDateTime_2d", _To1_2d[_AsDateTime])
AsDateTime_3d = TypeAliasType("AsDateTime_3d", _To1_3d[_AsDateTime])
AsDateTime_nd = TypeAliasType("AsDateTime_nd", _To1_nd[_AsDateTime])

AsBytes_0d = TypeAliasType("AsBytes_0d", _To2_0d[_AsBytes, bytes])
AsBytes_1d = TypeAliasType("AsBytes_1d", _To2_1d[_AsBytes, bytes])
AsBytes_2d = TypeAliasType("AsBytes_2d", _To2_2d[_AsBytes, bytes])
AsBytes_3d = TypeAliasType("AsBytes_3d", _To2_3d[_AsBytes, bytes])
AsBytes_nd = TypeAliasType("AsBytes_nd", _To2_nd[_AsBytes, bytes])

AsStr_0d = TypeAliasType("AsStr_0d", _To2_0d[_AsStr, str])
AsStr_1d = TypeAliasType("AsStr_1d", _To2_1d[_AsStr, str])
AsStr_2d = TypeAliasType("AsStr_2d", _To2_2d[_AsStr, str])
AsStr_3d = TypeAliasType("AsStr_3d", _To2_3d[_AsStr, str])
AsStr_nd = TypeAliasType("AsStr_nd", _To2_nd[_AsStr, str])

AsObject_0d = TypeAliasType("AsObject_0d", _To1_0d[_AsObject])
AsObject_1d = TypeAliasType("AsObject_1d", _To1_1d[_AsObject])
AsObject_2d = TypeAliasType("AsObject_2d", _To1_2d[_AsObject])
AsObject_3d = TypeAliasType("AsObject_3d", _To1_3d[_AsObject])
AsObject_nd = TypeAliasType("AsObject_nd", _To1_nd[_AsObject])

# Non-overlapping versions of `numpy._typing._ArrayLike{}_co` with concise names.
# Based on the "ToJust*ND" array-like aliases of `optype.numpy`:
# https://github.com/jorenham/optype#array-likes

AsUnsignedInteger_0d = TypeAliasType("AsUnsignedInteger_0d", _To1_0d[np.unsignedinteger])
AsUnsignedInteger_1d = TypeAliasType("AsUnsignedInteger_1d", _To1_1d[np.unsignedinteger])
AsUnsignedInteger_2d = TypeAliasType("AsUnsignedInteger_2d", _To1_2d[np.unsignedinteger])
AsUnsignedInteger_3d = TypeAliasType("AsUnsignedInteger_3d", _To1_3d[np.unsignedinteger])
AsUnsignedInteger_nd = TypeAliasType("AsUnsignedInteger_nd", _To1_nd[np.unsignedinteger])

AsSignedInteger_0d = TypeAliasType("AsSignedInteger_0d", _To2_0d[np.signedinteger, Is[int]])
AsSignedInteger_1d = TypeAliasType("AsSignedInteger_1d", _To2_1d[np.signedinteger, Is[int]])
AsSignedInteger_2d = TypeAliasType("AsSignedInteger_2d", _To2_2d[np.signedinteger, Is[int]])
AsSignedInteger_3d = TypeAliasType("AsSignedInteger_3d", _To2_3d[np.signedinteger, Is[int]])
AsSignedInteger_nd = TypeAliasType("AsSignedInteger_nd", _To2_nd[np.signedinteger, Is[int]])

AsInteger_0d = TypeAliasType("AsInteger_0d", _To2_0d[np.integer, Is[int]])
AsInteger_1d = TypeAliasType("AsInteger_1d", _To2_1d[np.integer, Is[int]])
AsInteger_2d = TypeAliasType("AsInteger_2d", _To2_2d[np.integer, Is[int]])
AsInteger_3d = TypeAliasType("AsInteger_3d", _To2_3d[np.integer, Is[int]])
AsInteger_nd = TypeAliasType("AsInteger_nd", _To2_nd[np.integer, Is[int]])

AsFloating_0d = TypeAliasType("AsFloating_0d", _To2_0d[np.floating, Is[float]])
AsFloating_1d = TypeAliasType("AsFloating_1d", _To2_1d[np.floating, Is[float]])
AsFloating_2d = TypeAliasType("AsFloating_2d", _To2_2d[np.floating, Is[float]])
AsFloating_3d = TypeAliasType("AsFloating_3d", _To2_3d[np.floating, Is[float]])
AsFloating_nd = TypeAliasType("AsFloating_nd", _To2_nd[np.floating, Is[float]])

AsComplexFloating_0d = TypeAliasType("AsComplexFloating_0d", _To2_0d[np.complexfloating, Is[complex]])
AsComplexFloating_1d = TypeAliasType("AsComplexFloating_1d", _To2_1d[np.complexfloating, Is[complex]])
AsComplexFloating_2d = TypeAliasType("AsComplexFloating_2d", _To2_2d[np.complexfloating, Is[complex]])
AsComplexFloating_3d = TypeAliasType("AsComplexFloating_3d", _To2_3d[np.complexfloating, Is[complex]])
AsComplexFloating_nd = TypeAliasType("AsComplexFloating_nd", _To2_nd[np.complexfloating, Is[complex]])

AsInexact_0d = TypeAliasType("AsInexact_0d", _To2_0d[np.inexact, Is[float] | Is[complex]])
AsInexact_1d = TypeAliasType("AsInexact_1d", _To2_1d[np.inexact, Is[float] | Is[complex]])
AsInexact_2d = TypeAliasType("AsInexact_2d", _To2_2d[np.inexact, Is[float] | Is[complex]])
AsInexact_3d = TypeAliasType("AsInexact_3d", _To2_3d[np.inexact, Is[float] | Is[complex]])
AsInexact_nd = TypeAliasType("AsInexact_nd", _To2_nd[np.inexact, Is[float] | Is[complex]])

AsNumber_0d = TypeAliasType("AsNumber_0d", _To2_0d[np.number, Is[int] | Is[float] | Is[complex]])
AsNumber_1d = TypeAliasType("AsNumber_1d", _To2_1d[np.number, Is[int] | Is[float] | Is[complex]])
AsNumber_2d = TypeAliasType("AsNumber_2d", _To2_2d[np.number, Is[int] | Is[float] | Is[complex]])
AsNumber_3d = TypeAliasType("AsNumber_3d", _To2_3d[np.number, Is[int] | Is[float] | Is[complex]])
AsNumber_nd = TypeAliasType("AsNumber_nd", _To2_nd[np.number, Is[int] | Is[float] | Is[complex]])

# Coercible (overlapping) scalar- and array-likes
ToBool_0d = TypeAliasType("ToBool_0d", _To2_0d[_ToBool, bool])
ToBool_1d = TypeAliasType("ToBool_1d", _To2_1d[_ToBool, bool])
ToBool_2d = TypeAliasType("ToBool_2d", _To2_2d[_ToBool, bool])
ToBool_3d = TypeAliasType("ToBool_3d", _To2_3d[_ToBool, bool])
ToBool_nd = TypeAliasType("ToBool_nd", _To2_nd[_ToBool, bool])

ToInt8_0d = TypeAliasType("ToInt8_0d", _To2_0d[_ToInt8, bool])
ToInt8_1d = TypeAliasType("ToInt8_1d", _To2_1d[_ToInt8, bool])
ToInt8_2d = TypeAliasType("ToInt8_2d", _To2_2d[_ToInt8, bool])
ToInt8_3d = TypeAliasType("ToInt8_3d", _To2_3d[_ToInt8, bool])
ToInt8_nd = TypeAliasType("ToInt8_nd", _To2_nd[_ToInt8, bool])

ToInt16_0d = TypeAliasType("ToInt16_0d", _To2_0d[_ToInt16, bool])
ToInt16_1d = TypeAliasType("ToInt16_1d", _To2_1d[_ToInt16, bool])
ToInt16_2d = TypeAliasType("ToInt16_2d", _To2_2d[_ToInt16, bool])
ToInt16_3d = TypeAliasType("ToInt16_3d", _To2_3d[_ToInt16, bool])
ToInt16_nd = TypeAliasType("ToInt16_nd", _To2_nd[_ToInt16, bool])

ToInt32_0d = TypeAliasType("ToInt32_0d", _To2_0d[_ToInt32, bool])
ToInt32_1d = TypeAliasType("ToInt32_1d", _To2_1d[_ToInt32, bool])
ToInt32_2d = TypeAliasType("ToInt32_2d", _To2_2d[_ToInt32, bool])
ToInt32_3d = TypeAliasType("ToInt32_3d", _To2_3d[_ToInt32, bool])
ToInt32_nd = TypeAliasType("ToInt32_nd", _To2_nd[_ToInt32, bool])

ToInt64_0d = TypeAliasType("ToInt64_0d", _To2_0d[_ToInt64, int])
ToInt64_1d = TypeAliasType("ToInt64_1d", _To2_1d[_ToInt64, int])
ToInt64_2d = TypeAliasType("ToInt64_2d", _To2_2d[_ToInt64, int])
ToInt64_3d = TypeAliasType("ToInt64_3d", _To2_3d[_ToInt64, int])
ToInt64_nd = TypeAliasType("ToInt64_nd", _To2_nd[_ToInt64, int])

ToLong_0d = TypeAliasType("ToLong_0d", _To2_0d[_ToLong, bool])
ToLong_1d = TypeAliasType("ToLong_1d", _To2_1d[_ToLong, bool])
ToLong_2d = TypeAliasType("ToLong_2d", _To2_2d[_ToLong, bool])
ToLong_3d = TypeAliasType("ToLong_3d", _To2_3d[_ToLong, bool])
ToLong_nd = TypeAliasType("ToLong_nd", _To2_nd[_ToLong, bool])

ToIntP_0d = TypeAliasType("ToIntP_0d", _To2_0d[_ToIntP, int])
ToIntP_1d = TypeAliasType("ToIntP_1d", _To2_1d[_ToIntP, int])
ToIntP_2d = TypeAliasType("ToIntP_2d", _To2_2d[_ToIntP, int])
ToIntP_3d = TypeAliasType("ToIntP_3d", _To2_3d[_ToIntP, int])
ToIntP_nd = TypeAliasType("ToIntP_nd", _To2_nd[_ToIntP, int])

ToLongLong_0d = TypeAliasType("ToLongLong_0d", _To2_0d[_ToLongLong, int])
ToLongLong_1d = TypeAliasType("ToLongLong_1d", _To2_1d[_ToLongLong, int])
ToLongLong_2d = TypeAliasType("ToLongLong_2d", _To2_2d[_ToLongLong, int])
ToLongLong_3d = TypeAliasType("ToLongLong_3d", _To2_3d[_ToLongLong, int])
ToLongLong_nd = TypeAliasType("ToLongLong_nd", _To2_nd[_ToLongLong, int])

ToUInt8_0d = TypeAliasType("ToUInt8_0d", _To2_0d[_ToUInt8, bool])
ToUInt8_1d = TypeAliasType("ToUInt8_1d", _To2_1d[_ToUInt8, bool])
ToUInt8_2d = TypeAliasType("ToUInt8_2d", _To2_2d[_ToUInt8, bool])
ToUInt8_3d = TypeAliasType("ToUInt8_3d", _To2_3d[_ToUInt8, bool])
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _To2_nd[_ToUInt8, bool])

ToUInt16_0d = TypeAliasType("ToUInt16_0d", _To2_0d[_ToUInt16, bool])
ToUInt16_1d = TypeAliasType("ToUInt16_1d", _To2_1d[_ToUInt16, bool])
ToUInt16_2d = TypeAliasType("ToUInt16_2d", _To2_2d[_ToUInt16, bool])
ToUInt16_3d = TypeAliasType("ToUInt16_3d", _To2_3d[_ToUInt16, bool])
ToUInt16_nd = TypeAliasType("ToUInt16_nd", _To2_nd[_ToUInt16, bool])

ToUInt32_0d = TypeAliasType("ToUInt32_0d", _To2_0d[_ToUInt32, bool])
ToUInt32_1d = TypeAliasType("ToUInt32_1d", _To2_1d[_ToUInt32, bool])
ToUInt32_2d = TypeAliasType("ToUInt32_2d", _To2_2d[_ToUInt32, bool])
ToUInt32_3d = TypeAliasType("ToUInt32_3d", _To2_3d[_ToUInt32, bool])
ToUInt32_nd = TypeAliasType("ToUInt32_nd", _To2_nd[_ToUInt32, bool])

ToUInt64_0d = TypeAliasType("ToUInt64_0d", _To2_0d[_ToUInt64, bool])
ToUInt64_1d = TypeAliasType("ToUInt64_1d", _To2_1d[_ToUInt64, bool])
ToUInt64_2d = TypeAliasType("ToUInt64_2d", _To2_2d[_ToUInt64, bool])
ToUInt64_3d = TypeAliasType("ToUInt64_3d", _To2_3d[_ToUInt64, bool])
ToUInt64_nd = TypeAliasType("ToUInt64_nd", _To2_nd[_ToUInt64, bool])

ToULong_0d = TypeAliasType("ToULong_0d", _To2_0d[_ToULong, bool])
ToULong_1d = TypeAliasType("ToULong_1d", _To2_1d[_ToULong, bool])
ToULong_2d = TypeAliasType("ToULong_2d", _To2_2d[_ToULong, bool])
ToULong_3d = TypeAliasType("ToULong_3d", _To2_3d[_ToULong, bool])
ToULong_nd = TypeAliasType("ToULong_nd", _To2_nd[_ToULong, bool])

ToUIntP_0d = TypeAliasType("ToUIntP_0d", _To2_0d[_ToUIntP, bool])
ToUIntP_1d = TypeAliasType("ToUIntP_1d", _To2_1d[_ToUIntP, bool])
ToUIntP_2d = TypeAliasType("ToUIntP_2d", _To2_2d[_ToUIntP, bool])
ToUIntP_3d = TypeAliasType("ToUIntP_3d", _To2_3d[_ToUIntP, bool])
ToUIntP_nd = TypeAliasType("ToUIntP_nd", _To2_nd[_ToUIntP, bool])

ToULongLong_0d = TypeAliasType("ToULongLong_0d", _To2_0d[_ToULongLong, bool])
ToULongLong_1d = TypeAliasType("ToULongLong_1d", _To2_1d[_ToULongLong, bool])
ToULongLong_2d = TypeAliasType("ToULongLong_2d", _To2_2d[_ToULongLong, bool])
ToULongLong_3d = TypeAliasType("ToULongLong_3d", _To2_3d[_ToULongLong, bool])
ToULongLong_nd = TypeAliasType("ToULongLong_nd", _To2_nd[_ToULongLong, bool])

ToFloat16_0d = TypeAliasType("ToFloat16_0d", _To2_0d[_ToFloat16, bool])
ToFloat16_1d = TypeAliasType("ToFloat16_1d", _To2_1d[_ToFloat16, bool])
ToFloat16_2d = TypeAliasType("ToFloat16_2d", _To2_2d[_ToFloat16, bool])
ToFloat16_3d = TypeAliasType("ToFloat16_3d", _To2_3d[_ToFloat16, bool])
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _To2_nd[_ToFloat16, bool])

ToFloat32_0d = TypeAliasType("ToFloat32_0d", _To2_0d[_ToFloat32, bool])
ToFloat32_1d = TypeAliasType("ToFloat32_1d", _To2_1d[_ToFloat32, bool])
ToFloat32_2d = TypeAliasType("ToFloat32_2d", _To2_2d[_ToFloat32, bool])
ToFloat32_3d = TypeAliasType("ToFloat32_3d", _To2_3d[_ToFloat32, bool])
ToFloat32_nd = TypeAliasType("ToFloat32_nd", _To2_nd[_ToFloat32, bool])

ToFloat64_0d = TypeAliasType("ToFloat64_0d", _To2_0d[_ToFloat64, float])
ToFloat64_1d = TypeAliasType("ToFloat64_1d", _To2_1d[_ToFloat64, float])
ToFloat64_2d = TypeAliasType("ToFloat64_2d", _To2_2d[_ToFloat64, float])
ToFloat64_3d = TypeAliasType("ToFloat64_3d", _To2_3d[_ToFloat64, float])
ToFloat64_nd = TypeAliasType("ToFloat64_nd", _To2_nd[_ToFloat64, float])

ToLongDouble_0d = TypeAliasType("ToLongDouble_0d", _To2_0d[_ToLongDouble, float])
ToLongDouble_1d = TypeAliasType("ToLongDouble_1d", _To2_1d[_ToLongDouble, float])
ToLongDouble_2d = TypeAliasType("ToLongDouble_2d", _To2_2d[_ToLongDouble, float])
ToLongDouble_3d = TypeAliasType("ToLongDouble_3d", _To2_3d[_ToLongDouble, float])
ToLongDouble_nd = TypeAliasType("ToLongDouble_nd", _To2_nd[_ToLongDouble, float])

ToComplex64_0d = TypeAliasType("ToComplex64_0d", _To2_0d[_ToComplex64, bool])
ToComplex64_1d = TypeAliasType("ToComplex64_1d", _To2_1d[_ToComplex64, bool])
ToComplex64_2d = TypeAliasType("ToComplex64_2d", _To2_2d[_ToComplex64, bool])
ToComplex64_3d = TypeAliasType("ToComplex64_3d", _To2_3d[_ToComplex64, bool])
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _To2_nd[_ToComplex64, bool])

ToComplex128_0d = TypeAliasType("ToComplex128_0d", _To2_0d[_ToComplex128, complex])
ToComplex128_1d = TypeAliasType("ToComplex128_1d", _To2_1d[_ToComplex128, complex])
ToComplex128_2d = TypeAliasType("ToComplex128_2d", _To2_2d[_ToComplex128, complex])
ToComplex128_3d = TypeAliasType("ToComplex128_3d", _To2_3d[_ToComplex128, complex])
ToComplex128_nd = TypeAliasType("ToComplex128_nd", _To2_nd[_ToComplex128, complex])

ToCLongDouble_0d = TypeAliasType("ToCLongDouble_0d", _To2_0d[_ToCLongDouble, complex])
ToCLongDouble_1d = TypeAliasType("ToCLongDouble_1d", _To2_1d[_ToCLongDouble, complex])
ToCLongDouble_2d = TypeAliasType("ToCLongDouble_2d", _To2_2d[_ToCLongDouble, complex])
ToCLongDouble_3d = TypeAliasType("ToCLongDouble_3d", _To2_3d[_ToCLongDouble, complex])
ToCLongDouble_nd = TypeAliasType("ToCLongDouble_nd", _To2_nd[_ToCLongDouble, complex])

ToTimeDelta_0d = TypeAliasType("ToTimeDelta_0d", _To2_0d[_ToTimeDelta, int])
ToTimeDelta_1d = TypeAliasType("ToTimeDelta_1d", _To2_1d[_ToTimeDelta, int])
ToTimeDelta_2d = TypeAliasType("ToTimeDelta_2d", _To2_2d[_ToTimeDelta, int])
ToTimeDelta_3d = TypeAliasType("ToTimeDelta_3d", _To2_3d[_ToTimeDelta, int])
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _To2_nd[_ToTimeDelta, int])

ToDateTime_0d = TypeAliasType("ToDateTime_0d", _To1_0d[_ToDateTime])
ToDateTime_1d = TypeAliasType("ToDateTime_1d", _To1_1d[_ToDateTime])
ToDateTime_2d = TypeAliasType("ToDateTime_2d", _To1_2d[_ToDateTime])
ToDateTime_3d = TypeAliasType("ToDateTime_3d", _To1_3d[_ToDateTime])
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _To1_nd[_ToDateTime])

ToBytes_0d = TypeAliasType("ToBytes_0d", _To2_0d[_ToBytes, bytes])
ToBytes_1d = TypeAliasType("ToBytes_1d", _To2_1d[_ToBytes, bytes])
ToBytes_2d = TypeAliasType("ToBytes_2d", _To2_2d[_ToBytes, bytes])
ToBytes_3d = TypeAliasType("ToBytes_3d", _To2_3d[_ToBytes, bytes])
ToBytes_nd = TypeAliasType("ToBytes_nd", _To2_nd[_ToBytes, bytes])

ToStr_0d = TypeAliasType("ToStr_0d", _To2_0d[_ToStr, bytes | str])
ToStr_1d = TypeAliasType("ToStr_1d", _To2_1d[_ToStr, bytes | str])
ToStr_2d = TypeAliasType("ToStr_2d", _To2_2d[_ToStr, bytes | str])
ToStr_3d = TypeAliasType("ToStr_3d", _To2_3d[_ToStr, bytes | str])
ToStr_nd = TypeAliasType("ToStr_nd", _To2_nd[_ToStr, bytes | str])

ToObject_0d = TypeAliasType("ToObject_0d", _To2_0d[_ToObject, object])
ToObject_1d = TypeAliasType("ToObject_1d", _To2_1d[_ToObject, object])
ToObject_2d = TypeAliasType("ToObject_2d", _To2_2d[_ToObject, object])
ToObject_3d = TypeAliasType("ToObject_3d", _To2_3d[_ToObject, object])
ToObject_nd = TypeAliasType("ToObject_nd", _To2_nd[_ToObject, object])

# `npt.NDArray` variant with (optional) 2nd shape-typing parameter
Array = TypeAliasType("Array", np.ndarray[_ShapeT, np.dtype[_ScalarT]], type_params=(_ScalarT, _ShapeT))
Array_0d = TypeAliasType("Array_0d", np.ndarray[tuple[()], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_1d = TypeAliasType("Array_1d", np.ndarray[tuple[int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_2d = TypeAliasType("Array_2d", np.ndarray[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array_3d = TypeAliasType("Array_3d", np.ndarray[tuple[int, int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

# A Generic scalar-like type alias for builtin scalar types, so that `ScalarLike[int]`
# matches `np.integer` and `np.bool` scalar types, rejects `3.14` and `np.float32(42)`.
ScalarLike = TypeAliasType("ScalarLike", _BuiltinT | np.generic[_BuiltinT], type_params=(_BuiltinT,))

# A Generic array-like type alias for builtin scalar types, so that `ArrayLike[int]`
# matches array-likes with `np.integer` and `np.bool` scalar types, but rejects "bare"
# scalars and float array-likes.
ArrayLike = TypeAliasType("ArrayLike", _To2_nd[np.generic[_BuiltinT], _BuiltinT], type_params=(_BuiltinT,))
