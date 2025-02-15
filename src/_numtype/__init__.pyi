# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
from typing import Any, TypeAlias, final, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar

import numpy as np

###
# Type parameters

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_BuiltinT = TypeVar("_BuiltinT")
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)

###
# Protocols

# A slimmed down version of `_NestedSequence`, based on `optype.numpy.SequenceND`.
# https://github.com/jorenham/optype
@type_check_only
class SequenceND(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    def __getitem__(self, index: int, /) -> _T_co | SequenceND[_T_co]: ...
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
_ToStr: TypeAlias = np.character[Any]  # rougly equivalent to `str_ | bytes_`
_ToObject: TypeAlias = np.generic

###
# Array-likes

# Faster & non-overlapping analogues of `_ArrayLike` and `_DualArrayLike`, respectively.
_To1_nd: TypeAlias = CanLenArray[_ScalarT] | SequenceND[CanLenArray[_ScalarT]]
_To2_nd: TypeAlias = SequenceND[_ScalarT | _T] | _To1_nd[_ScalarT]

# Non-overlapping versions of `numpy._typing._ArrayLike{}_co` with concise names.
# Based on the "ToJust*ND" array-like aliases of `optype.numpy`:
# https://github.com/jorenham/optype#array-likes
AsBool_nd = TypeAliasType("AsBool_nd", _To2_nd[_AsBool, bool])
AsInt8_nd = TypeAliasType("AsInt8_nd", _To1_nd[_AsInt8])
AsInt16_nd = TypeAliasType("AsInt16_nd", _To1_nd[_AsInt16])
AsInt32_nd = TypeAliasType("AsInt32_nd", _To1_nd[_AsInt32])
AsInt64_nd = TypeAliasType("AsInt64_nd", _To1_nd[_AsInt64])
AsLong_nd = TypeAliasType("AsLong_nd", _To1_nd[_AsLong])
AsIntP_nd = TypeAliasType("AsIntP_nd", _To2_nd[_AsIntP, Is[int]])
AsLongLong_nd = TypeAliasType("AsLongLong_nd", _To1_nd[_AsLongLong])
AsUInt8_nd = TypeAliasType("AsUInt8_nd", _To1_nd[_AsUInt8])
AsUInt16_nd = TypeAliasType("AsUInt16_nd", _To1_nd[_AsUInt16])
AsUInt32_nd = TypeAliasType("AsUInt32_nd", _To1_nd[_AsUInt32])
AsUInt64_nd = TypeAliasType("AsUInt64_nd", _To1_nd[_AsUInt64])
AsULong_nd = TypeAliasType("AsULong_nd", _To1_nd[_AsULong])
AsUIntP_nd = TypeAliasType("AsUIntP_nd", _To1_nd[_AsUIntP])
AsULongLong_nd = TypeAliasType("AsULongLong_nd", _To1_nd[_AsULongLong])
AsFloat16_nd = TypeAliasType("AsFloat16_nd", _To1_nd[_AsFloat16])
AsFloat32_nd = TypeAliasType("AsFloat32_nd", _To1_nd[_AsFloat32])
AsFloat64_nd = TypeAliasType("AsFloat64_nd", _To2_nd[_AsFloat64, Is[float]])
AsLongDouble_nd = TypeAliasType("AsLongDouble_nd", _To1_nd[_AsLongDouble])
AsComplex64_nd = TypeAliasType("AsComplex64_nd", _To1_nd[_AsComplex64])
AsComplex128_nd = TypeAliasType("AsComplex128_nd", _To2_nd[_AsComplex128, Is[complex]])
AsCLongDouble_nd = TypeAliasType("AsCLongDouble_nd", _To1_nd[_AsCLongDouble])
AsTimeDelta_nd = TypeAliasType("AsTimeDelta_nd", _To1_nd[_AsTimeDelta])
AsDateTime_nd = TypeAliasType("AsDateTime_nd", _To1_nd[_AsDateTime])
AsBytes_nd = TypeAliasType("AsBytes_nd", _To2_nd[_AsBytes, bytes])
AsStr_nd = TypeAliasType("AsStr_nd", _To2_nd[_AsStr, str])
AsObject_nd = TypeAliasType("AsObject_nd", _To1_nd[_AsObject])

AsSignedInteger_nd = TypeAliasType("AsSignedInteger_nd", _To2_nd[np.signedinteger, Is[int]])
AsUnsignedInteger_nd = TypeAliasType("AsUnsignedInteger_nd", _To1_nd[np.unsignedinteger])
AsInteger_nd = TypeAliasType("AsInteger_nd", _To2_nd[np.integer, Is[int]])
AsFloating_nd = TypeAliasType("AsFloating_nd", _To2_nd[np.floating, Is[float]])
AsComplexFloating_nd = TypeAliasType("AsComplexFloating_nd", _To2_nd[np.complexfloating, Is[complex]])
AsInexact_nd = TypeAliasType("AsInexact_nd", _To2_nd[np.inexact, Is[float] | Is[complex]])
AsNumber_nd = TypeAliasType("AsNumber_nd", _To2_nd[np.number, Is[int] | Is[float] | Is[complex]])
AsCharacter_nd = TypeAliasType("AsCharacter_nd", _To2_nd[np.character, bytes | str])

# Coercible scalar-likes
_To_0d: TypeAlias = _ScalarT | CanArray[_ScalarT, tuple[()]]
ToBool_0d = TypeAliasType("ToBool_0d", bool | _To_0d[_ToBool])
ToInt8_0d = TypeAliasType("ToInt8_0d", bool | _To_0d[_ToInt8])
ToInt16_0d = TypeAliasType("ToInt16_0d", bool | _To_0d[_ToInt16])
ToInt32_0d = TypeAliasType("ToInt32_0d", bool | _To_0d[_ToInt32])
ToInt64_0d = TypeAliasType("ToInt64_0d", int | _To_0d[_ToInt64])
ToIntP_0d = TypeAliasType("ToIntP_0d", int | _To_0d[_ToIntP])
ToLong_0d = TypeAliasType("ToLong_0d", bool | _To_0d[_ToLong])
ToLongLong_0d = TypeAliasType("ToLongLong_0d", bool | _To_0d[_ToLongLong])
ToUInt8_0d = TypeAliasType("ToUInt8_0d", bool | _To_0d[_ToUInt8])
ToUInt16_0d = TypeAliasType("ToUInt16_0d", bool | _To_0d[_ToUInt16])
ToUInt32_0d = TypeAliasType("ToUInt32_0d", bool | _To_0d[_ToUInt32])
ToUInt64_0d = TypeAliasType("ToUInt64_0d", bool | _To_0d[_ToUInt64])
ToUIntP_0d = TypeAliasType("ToUIntP_0d", bool | _To_0d[_ToUIntP])
ToULong_0d = TypeAliasType("ToULong_0d", bool | _To_0d[_ToULong])
ToULongLong_0d = TypeAliasType("ToULongLong_0d", bool | _To_0d[_ToULongLong])
ToFloat16_0d = TypeAliasType("ToFloat16_0d", bool | _To_0d[_ToFloat16])
ToFloat32_0d = TypeAliasType("ToFloat32_0d", bool | _To_0d[_ToFloat32])
ToFloat64_0d = TypeAliasType("ToFloat64_0d", bool | _To_0d[_ToFloat64])
ToLongDouble_0d = TypeAliasType("ToLongDouble_0d", bool | _To_0d[_ToLongDouble])
ToComplex64_0d = TypeAliasType("ToComplex64_0d", bool | _To_0d[_ToComplex64])
ToComplex128_0d = TypeAliasType("ToComplex128_0d", bool | _To_0d[_ToComplex128])
ToCLongDouble_0d = TypeAliasType("ToCLongDouble_0d", bool | _To_0d[_ToCLongDouble])
ToTimeDelta_0d = TypeAliasType("ToTimeDelta_0d", bool | _To_0d[_ToTimeDelta])
ToDateTime_0d = TypeAliasType("ToDateTime_0d", bool | _To_0d[_ToDateTime])
ToBytes_0d = TypeAliasType("ToBytes_0d", bool | _To_0d[_ToBytes])
ToStr_0d = TypeAliasType("ToStr_0d", bool | _To_0d[_ToStr])
ToObject_0d = TypeAliasType("ToObject_0d", bool | _To_0d[_ToObject])

# Coercible array-likes
ToBool_nd = TypeAliasType("ToBool_nd", _To2_nd[_ToBool, bool])
ToInt8_nd = TypeAliasType("ToInt8_nd", _To2_nd[_ToInt8, bool])
ToInt16_nd = TypeAliasType("ToInt16_nd", _To2_nd[_ToInt16, bool])
ToInt32_nd = TypeAliasType("ToInt32_nd", _To2_nd[_ToInt32, bool])
ToInt64_nd = TypeAliasType("ToInt64_nd", _To2_nd[_ToInt64, int])
ToLong_nd = TypeAliasType("ToLong_nd", _To2_nd[_ToLong, bool])
ToIntP_nd = TypeAliasType("ToIntP_nd", _To2_nd[_ToIntP, int])
ToLongLong_nd = TypeAliasType("ToLongLong_nd", _To2_nd[_ToLongLong, int])
ToUInt8_nd = TypeAliasType("ToUInt8_nd", _To2_nd[_ToUInt8, bool])
ToUInt16_nd = TypeAliasType("ToUInt16_nd", _To2_nd[_ToUInt16, bool])
ToUInt32_nd = TypeAliasType("ToUInt32_nd", _To2_nd[_ToUInt32, bool])
ToUInt64_nd = TypeAliasType("ToUInt64_nd", _To2_nd[_ToUInt64, bool])
ToULong_nd = TypeAliasType("ToULong_nd", _To2_nd[_ToULong, bool])
ToUIntP_nd = TypeAliasType("ToUIntP_nd", _To2_nd[_ToUIntP, bool])
ToULongLong_nd = TypeAliasType("ToULongLong_nd", _To2_nd[_ToULongLong, bool])
ToFloat16_nd = TypeAliasType("ToFloat16_nd", _To2_nd[_ToFloat16, bool])
ToFloat32_nd = TypeAliasType("ToFloat32_nd", _To2_nd[_ToFloat32, bool])
ToFloat64_nd = TypeAliasType("ToFloat64_nd", _To2_nd[_ToFloat64, float])
ToLongDouble_nd = TypeAliasType("ToLongDouble_nd", _To2_nd[_ToLongDouble, float])
ToComplex64_nd = TypeAliasType("ToComplex64_nd", _To2_nd[_ToComplex64, bool])
ToComplex128_nd = TypeAliasType("ToComplex128_nd", _To2_nd[_ToComplex128, complex])
ToCLongDouble_nd = TypeAliasType("ToCLongDouble_nd", _To2_nd[_ToCLongDouble, complex])
ToTimeDelta_nd = TypeAliasType("ToTimeDelta_nd", _To2_nd[_ToTimeDelta, int])
ToDateTime_nd = TypeAliasType("ToDateTime_nd", _To1_nd[_ToDateTime])
ToBytes_nd = TypeAliasType("ToBytes_nd", _To2_nd[_ToBytes, bytes])
ToStr_nd = TypeAliasType("ToStr_nd", _To2_nd[_ToStr, bytes | str])
ToObject_nd = TypeAliasType("ToObject_nd", _To2_nd[_ToObject, object])

# A Generic scalar-like type alias for builtin scalar types, so that `ScalarLike[int]`
# matches `np.integer` and `np.bool` scalar types, rejects `3.14` and `np.float32(42)`.
ScalarLike = TypeAliasType("ScalarLike", _BuiltinT | np.generic[_BuiltinT], type_params=(_BuiltinT,))

# A Generic array-like type alias for builtin scalar types, so that `ArrayLike[int]`
# matches array-likes with `np.integer` and `np.bool` scalar types, but rejects "bare"
# scalars and float array-likes.
ArrayLike = TypeAliasType("ArrayLike", _To2_nd[np.generic[_BuiltinT], _BuiltinT], type_params=(_BuiltinT,))
