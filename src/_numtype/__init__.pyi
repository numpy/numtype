# Internal type-check-only types, that may be moved to the `numtype` public API in the
# future.

# NOTE: The `TypeAliasType` backport is used to avoid long type-checker error messages.
from collections.abc import Sequence
from typing import Any, TypeAlias, final, type_check_only
from typing_extensions import Protocol, TypeAliasType, TypeVar, Unpack

import numpy as np

###
# Type parameters

_T = TypeVar("_T", default=Any)
_T_co = TypeVar("_T_co", covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)

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

_PyInexact: TypeAlias = Is[float] | Is[complex]
_PyNumber: TypeAlias = Is[int] | _PyInexact

_ToBool: TypeAlias = np.bool[Any]
_ToInt8: TypeAlias = np.int8 | _ToBool
_ToInt16: TypeAlias = np.int16 | np.uint8 | _ToInt8
_ToInt32: TypeAlias = np.int32 | np.uint16 | _ToInt16
_ToInt64: TypeAlias = np.int64 | np.uint32 | _ToInt32
_ToLong: TypeAlias = np.long | _ToInt32
_ToIntP: TypeAlias = np.intp | _ToLong
_ToLongLong: TypeAlias = np.signedinteger | _ToUInt32
_ToUInt8: TypeAlias = np.uint8 | _ToBool
_ToUInt16: TypeAlias = np.uint16 | _ToUInt8
_ToUInt32: TypeAlias = np.uint32 | _ToUInt16
_ToUInt64: TypeAlias = np.uint64 | _ToUInt32
_ToULong: TypeAlias = np.ulong | _ToUInt32
_ToUIntP: TypeAlias = np.uintp | _ToULong
_ToULongLong: TypeAlias = np.unsignedinteger | _ToBool
_ToFloat16: TypeAlias = np.float16 | np.uint8 | np.int16 | _ToBool
_ToFloat32: TypeAlias = np.float32 | np.uint16 | np.int16 | _ToFloat16
_ToFloat64: TypeAlias = np.float64 | np.float32 | np.float16 | np.integer | _ToBool
_ToLongDouble: TypeAlias = np.floating | np.integer | _ToBool
_ToComplex64: TypeAlias = np.complex64 | _ToFloat32
_ToComplex128: TypeAlias = np.complex128 | np.complex64 | _ToFloat64
_ToCLongDouble: TypeAlias = np.number | _ToBool
_ToTimeDelta: TypeAlias = np.timedelta64[Any] | np.integer | _ToBool
_ToDateTime: TypeAlias = np.datetime64[Any] | np.timedelta64[Any]  # scalars may also accepts `integer | _ToBool`
_ToBytes: TypeAlias = np.bytes_
_ToStr: TypeAlias = np.character  # rougly equivalent to `str_ | bytes_`
_ToObject: TypeAlias = np.generic

_To1_0d: TypeAlias = _ScalarT | CanArray[_ScalarT, tuple[()]]
_To2_0d: TypeAlias = _ScalarT | _T | CanArray[_ScalarT, tuple[()]]

_To1_1d: TypeAlias = CanLenArray[_ScalarT, tuple[int]] | Sequence[_To1_0d[_ScalarT]]
_To2_1d: TypeAlias = CanLenArray[_ScalarT, tuple[int]] | Sequence[_To2_0d[_ScalarT, _T]]

_To1_2d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int]] | Sequence[_To1_1d[_ScalarT]]
_To2_2d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int]] | Sequence[_To2_1d[_ScalarT, _T]]

_To1_3d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int, int]] | Sequence[_To1_2d[_ScalarT]]
_To2_3d: TypeAlias = CanLenArray[_ScalarT, tuple[int, int, int]] | Sequence[_To2_2d[_ScalarT, _T]]

_To1_nd: TypeAlias = CanLenArray[_ScalarT] | Sequence_nd[CanLenArray[_ScalarT]]
_To2_nd: TypeAlias = CanLenArray[_ScalarT] | Sequence_nd[_T | _ScalarT] | Sequence_nd[CanLenArray[_ScalarT]]

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

AnyShapeC = TypeVar(  # noqa: PYI001
    "AnyShapeC",
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

Array = TypeAliasType("Array", np.ndarray[AnyShapeC, np.dtype[_ScalarT]], type_params=(_ScalarT, AnyShapeC))
Array0 = TypeAliasType("Array0", np.ndarray[NDim0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array1 = TypeAliasType("Array1", np.ndarray[NDim1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array2 = TypeAliasType("Array2", np.ndarray[NDim2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array3 = TypeAliasType("Array3", np.ndarray[NDim3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

MArray = TypeAliasType("MArray", np.ma.MaskedArray[AnyShapeC, np.dtype[_ScalarT]], type_params=(_ScalarT, AnyShapeC))
MArray0 = TypeAliasType("MArray0", np.ma.MaskedArray[NDim0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray1 = TypeAliasType("MArray1", np.ma.MaskedArray[NDim1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray2 = TypeAliasType("MArray2", np.ma.MaskedArray[NDim2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray3 = TypeAliasType("MArray3", np.ma.MaskedArray[NDim3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

Matrix = TypeAliasType("Matrix", np.matrix[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

###
# Array-likes

# Non-overlapping scalar- and array-like aliases for all scalar types.
As0D_bool = TypeAliasType("As0D_bool", _To2_0d[np.bool, bool])
As1D_bool = TypeAliasType("As1D_bool", _To2_1d[np.bool, bool])
As2D_bool = TypeAliasType("As2D_bool", _To2_2d[np.bool, bool])
As3D_bool = TypeAliasType("As3D_bool", _To2_3d[np.bool, bool])
AsND_bool = TypeAliasType("AsND_bool", _To2_nd[np.bool, bool])

As0D_int8 = TypeAliasType("As0D_int8", _To1_0d[np.int8])
As1D_int8 = TypeAliasType("As1D_int8", _To1_1d[np.int8])
As2D_int8 = TypeAliasType("As2D_int8", _To1_2d[np.int8])
As3D_int8 = TypeAliasType("As3D_int8", _To1_3d[np.int8])
AsND_int8 = TypeAliasType("AsND_int8", _To1_nd[np.int8])

As0D_int16 = TypeAliasType("As0D_int16", _To1_0d[np.int16])
As1D_int16 = TypeAliasType("As1D_int16", _To1_1d[np.int16])
As2D_int16 = TypeAliasType("As2D_int16", _To1_2d[np.int16])
As3D_int16 = TypeAliasType("As3D_int16", _To1_3d[np.int16])
AsND_int16 = TypeAliasType("AsND_int16", _To1_nd[np.int16])

As0D_int32 = TypeAliasType("As0D_int32", _To1_0d[np.int32])
As1D_int32 = TypeAliasType("As1D_int32", _To1_1d[np.int32])
As2D_int32 = TypeAliasType("As2D_int32", _To1_2d[np.int32])
As3D_int32 = TypeAliasType("As3D_int32", _To1_3d[np.int32])
AsND_int32 = TypeAliasType("AsND_int32", _To1_nd[np.int32])

As0D_int64 = TypeAliasType("As0D_int64", _To1_0d[np.int64])
As1D_int64 = TypeAliasType("As1D_int64", _To1_1d[np.int64])
As2D_int64 = TypeAliasType("As2D_int64", _To1_2d[np.int64])
As3D_int64 = TypeAliasType("As3D_int64", _To1_3d[np.int64])
AsND_int64 = TypeAliasType("AsND_int64", _To1_nd[np.int64])

As0D_long = TypeAliasType("As0D_long", _To1_0d[np.long])
As1D_long = TypeAliasType("As1D_long", _To1_1d[np.long])
As2D_long = TypeAliasType("As2D_long", _To1_2d[np.long])
As3D_long = TypeAliasType("As3D_long", _To1_3d[np.long])
AsND_long = TypeAliasType("AsND_long", _To1_nd[np.long])

As0D_intp = TypeAliasType("As0D_intp", _To2_0d[np.intp, Is[int]])
As1D_intp = TypeAliasType("As1D_intp", _To2_1d[np.intp, Is[int]])
As2D_intp = TypeAliasType("As2D_intp", _To2_2d[np.intp, Is[int]])
As3D_intp = TypeAliasType("As3D_intp", _To2_3d[np.intp, Is[int]])
AsND_intp = TypeAliasType("AsND_intp", _To2_nd[np.intp, Is[int]])

As0D_longlong = TypeAliasType("As0D_longlong", _To1_0d[np.longlong])
As1D_longlong = TypeAliasType("As1D_longlong", _To1_1d[np.longlong])
As2D_longlong = TypeAliasType("As2D_longlong", _To1_2d[np.longlong])
As3D_longlong = TypeAliasType("As3D_longlong", _To1_3d[np.longlong])
AsND_longlong = TypeAliasType("AsND_longlong", _To1_nd[np.longlong])

As0D_uint8 = TypeAliasType("As0D_uint8", _To1_0d[np.uint8])
As1D_uint8 = TypeAliasType("As1D_uint8", _To1_1d[np.uint8])
As2D_uint8 = TypeAliasType("As2D_uint8", _To1_2d[np.uint8])
As3D_uint8 = TypeAliasType("As3D_uint8", _To1_3d[np.uint8])
AsND_uint8 = TypeAliasType("AsND_uint8", _To1_nd[np.uint8])

As0D_uint16 = TypeAliasType("As0D_uint16", _To1_0d[np.uint16])
As1D_uint16 = TypeAliasType("As1D_uint16", _To1_1d[np.uint16])
As2D_uint16 = TypeAliasType("As2D_uint16", _To1_2d[np.uint16])
As3D_uint16 = TypeAliasType("As3D_uint16", _To1_3d[np.uint16])
AsND_uint16 = TypeAliasType("AsND_uint16", _To1_nd[np.uint16])

As0D_uint32 = TypeAliasType("As0D_uint32", _To1_0d[np.uint32])
As1D_uint32 = TypeAliasType("As1D_uint32", _To1_1d[np.uint32])
As2D_uint32 = TypeAliasType("As2D_uint32", _To1_2d[np.uint32])
As3D_uint32 = TypeAliasType("As3D_uint32", _To1_3d[np.uint32])
AsND_uint32 = TypeAliasType("AsND_uint32", _To1_nd[np.uint32])

As0D_uint64 = TypeAliasType("As0D_uint64", _To1_0d[np.uint64])
As1D_uint64 = TypeAliasType("As1D_uint64", _To1_1d[np.uint64])
As2D_uint64 = TypeAliasType("As2D_uint64", _To1_2d[np.uint64])
As3D_uint64 = TypeAliasType("As3D_uint64", _To1_3d[np.uint64])
AsND_uint64 = TypeAliasType("AsND_uint64", _To1_nd[np.uint64])

As0D_ulong = TypeAliasType("As0D_ulong", _To1_0d[np.ulong])
As1D_ulong = TypeAliasType("As1D_ulong", _To1_1d[np.ulong])
As2D_ulong = TypeAliasType("As2D_ulong", _To1_2d[np.ulong])
As3D_ulong = TypeAliasType("As3D_ulong", _To1_3d[np.ulong])
AsND_ulong = TypeAliasType("AsND_ulong", _To1_nd[np.ulong])

As0D_uintp = TypeAliasType("As0D_uintp", _To1_0d[np.uintp])
As1D_uintp = TypeAliasType("As1D_uintp", _To1_1d[np.uintp])
As2D_uintp = TypeAliasType("As2D_uintp", _To1_2d[np.uintp])
As3D_uintp = TypeAliasType("As3D_uintp", _To1_3d[np.uintp])
AsND_uintp = TypeAliasType("AsND_uintp", _To1_nd[np.uintp])

As0D_ulonglong = TypeAliasType("As0D_ulonglong", _To1_0d[np.ulonglong])
As1D_ulonglong = TypeAliasType("As1D_ulonglong", _To1_1d[np.ulonglong])
As2D_ulonglong = TypeAliasType("As2D_ulonglong", _To1_2d[np.ulonglong])
As3D_ulonglong = TypeAliasType("As3D_ulonglong", _To1_3d[np.ulonglong])
AsND_ulonglong = TypeAliasType("AsND_ulonglong", _To1_nd[np.ulonglong])

As0D_float16 = TypeAliasType("As0D_float16", _To1_0d[np.float16])
As1D_float16 = TypeAliasType("As1D_float16", _To1_1d[np.float16])
As2D_float16 = TypeAliasType("As2D_float16", _To1_2d[np.float16])
As3D_float16 = TypeAliasType("As3D_float16", _To1_3d[np.float16])
AsND_float16 = TypeAliasType("AsND_float16", _To1_nd[np.float16])

As0D_float32 = TypeAliasType("As0D_float32", _To1_0d[np.float32])
As1D_float32 = TypeAliasType("As1D_float32", _To1_1d[np.float32])
As2D_float32 = TypeAliasType("As2D_float32", _To1_2d[np.float32])
As3D_float32 = TypeAliasType("As3D_float32", _To1_3d[np.float32])
AsND_float32 = TypeAliasType("AsND_float32", _To1_nd[np.float32])

As0D_float64 = TypeAliasType("As0D_float64", _To2_0d[np.float64, Is[float]])
As1D_float64 = TypeAliasType("As1D_float64", _To2_1d[np.float64, Is[float]])
As2D_float64 = TypeAliasType("As2D_float64", _To2_2d[np.float64, Is[float]])
As3D_float64 = TypeAliasType("As3D_float64", _To2_3d[np.float64, Is[float]])
AsND_float64 = TypeAliasType("AsND_float64", _To2_nd[np.float64, Is[float]])

As0D_longdouble = TypeAliasType("As0D_longdouble", _To1_0d[np.longdouble])
As1D_longdouble = TypeAliasType("As1D_longdouble", _To1_1d[np.longdouble])
As2D_longdouble = TypeAliasType("As2D_longdouble", _To1_2d[np.longdouble])
As3D_longdouble = TypeAliasType("As3D_longdouble", _To1_3d[np.longdouble])
AsND_longdouble = TypeAliasType("AsND_longdouble", _To1_nd[np.longdouble])

As0D_complex64 = TypeAliasType("As0D_complex64", _To1_0d[np.complex64])
As1D_complex64 = TypeAliasType("As1D_complex64", _To1_1d[np.complex64])
As2D_complex64 = TypeAliasType("As2D_complex64", _To1_2d[np.complex64])
As3D_complex64 = TypeAliasType("As3D_complex64", _To1_3d[np.complex64])
AsND_complex64 = TypeAliasType("AsND_complex64", _To1_nd[np.complex64])

As0D_complex128 = TypeAliasType("As0D_complex128", _To2_0d[np.complex128, Is[complex]])
As1D_complex128 = TypeAliasType("As1D_complex128", _To2_1d[np.complex128, Is[complex]])
As2D_complex128 = TypeAliasType("As2D_complex128", _To2_2d[np.complex128, Is[complex]])
As3D_complex128 = TypeAliasType("As3D_complex128", _To2_3d[np.complex128, Is[complex]])
AsND_complex128 = TypeAliasType("AsND_complex128", _To2_nd[np.complex128, Is[complex]])

As0D_clongdouble = TypeAliasType("As0D_clongdouble", _To1_0d[np.clongdouble])
As1D_clongdouble = TypeAliasType("As1D_clongdouble", _To1_1d[np.clongdouble])
As2D_clongdouble = TypeAliasType("As2D_clongdouble", _To1_2d[np.clongdouble])
As3D_clongdouble = TypeAliasType("As3D_clongdouble", _To1_3d[np.clongdouble])
AsND_clongdouble = TypeAliasType("AsND_clongdouble", _To1_nd[np.clongdouble])

As0D_timedelta = TypeAliasType("As0D_timedelta", _To1_0d[np.timedelta64])
As1D_timedelta = TypeAliasType("As1D_timedelta", _To1_1d[np.timedelta64])
As2D_timedelta = TypeAliasType("As2D_timedelta", _To1_2d[np.timedelta64])
As3D_timedelta = TypeAliasType("As3D_timedelta", _To1_3d[np.timedelta64])
AsND_timedelta = TypeAliasType("AsND_timedelta", _To1_nd[np.timedelta64])

As0D_datetime = TypeAliasType("As0D_datetime", _To1_0d[np.datetime64])
As1D_datetime = TypeAliasType("As1D_datetime", _To1_1d[np.datetime64])
As2D_datetime = TypeAliasType("As2D_datetime", _To1_2d[np.datetime64])
As3D_datetime = TypeAliasType("As3D_datetime", _To1_3d[np.datetime64])
AsND_datetime = TypeAliasType("AsND_datetime", _To1_nd[np.datetime64])

As0D_bytes = TypeAliasType("As0D_bytes", _To2_0d[np.bytes_, bytes])
As1D_bytes = TypeAliasType("As1D_bytes", _To2_1d[np.bytes_, bytes])
As2D_bytes = TypeAliasType("As2D_bytes", _To2_2d[np.bytes_, bytes])
As3D_bytes = TypeAliasType("As3D_bytes", _To2_3d[np.bytes_, bytes])
AsND_bytes = TypeAliasType("AsND_bytes", _To2_nd[np.bytes_, bytes])

As0D_str = TypeAliasType("As0D_str", _To2_0d[np.str_, str])
As1D_str = TypeAliasType("As1D_str", _To2_1d[np.str_, str])
As2D_str = TypeAliasType("As2D_str", _To2_2d[np.str_, str])
As3D_str = TypeAliasType("As3D_str", _To2_3d[np.str_, str])
AsND_str = TypeAliasType("AsND_str", _To2_nd[np.str_, str])

As0D_object = TypeAliasType("As0D_object", _To1_0d[np.object_])
As1D_object = TypeAliasType("As1D_object", _To1_1d[np.object_])
As2D_object = TypeAliasType("As2D_object", _To1_2d[np.object_])
As3D_object = TypeAliasType("As3D_object", _To1_3d[np.object_])
AsND_object = TypeAliasType("AsND_object", _To1_nd[np.object_])

As0D_unsignedinteger = TypeAliasType("As0D_unsignedinteger", _To1_0d[np.unsignedinteger])
As1D_unsignedinteger = TypeAliasType("As1D_unsignedinteger", _To1_1d[np.unsignedinteger])
As2D_unsignedinteger = TypeAliasType("As2D_unsignedinteger", _To1_2d[np.unsignedinteger])
As3D_unsignedinteger = TypeAliasType("As3D_unsignedinteger", _To1_3d[np.unsignedinteger])
AsND_unsignedinteger = TypeAliasType("AsND_unsignedinteger", _To1_nd[np.unsignedinteger])

As0D_signedinteger = TypeAliasType("As0D_signedinteger", _To2_0d[np.signedinteger, Is[int]])
As1D_signedinteger = TypeAliasType("As1D_signedinteger", _To2_1d[np.signedinteger, Is[int]])
As2D_signedinteger = TypeAliasType("As2D_signedinteger", _To2_2d[np.signedinteger, Is[int]])
As3D_signedinteger = TypeAliasType("As3D_signedinteger", _To2_3d[np.signedinteger, Is[int]])
AsND_signedinteger = TypeAliasType("AsND_signedinteger", _To2_nd[np.signedinteger, Is[int]])

As0D_integer = TypeAliasType("As0D_integer", _To2_0d[np.integer, Is[int]])
As1D_integer = TypeAliasType("As1D_integer", _To2_1d[np.integer, Is[int]])
As2D_integer = TypeAliasType("As2D_integer", _To2_2d[np.integer, Is[int]])
As3D_integer = TypeAliasType("As3D_integer", _To2_3d[np.integer, Is[int]])
AsND_integer = TypeAliasType("AsND_integer", _To2_nd[np.integer, Is[int]])

As0D_floating = TypeAliasType("As0D_floating", _To2_0d[np.floating, Is[float]])
As1D_floating = TypeAliasType("As1D_floating", _To2_1d[np.floating, Is[float]])
As2D_floating = TypeAliasType("As2D_floating", _To2_2d[np.floating, Is[float]])
As3D_floating = TypeAliasType("As3D_floating", _To2_3d[np.floating, Is[float]])
AsND_floating = TypeAliasType("AsND_floating", _To2_nd[np.floating, Is[float]])

As0D_complexfloating = TypeAliasType("As0D_complexfloating", _To2_0d[np.complexfloating, Is[complex]])
As1D_complexfloating = TypeAliasType("As1D_complexfloating", _To2_1d[np.complexfloating, Is[complex]])
As2D_complexfloating = TypeAliasType("As2D_complexfloating", _To2_2d[np.complexfloating, Is[complex]])
As3D_complexfloating = TypeAliasType("As3D_complexfloating", _To2_3d[np.complexfloating, Is[complex]])
AsND_complexfloating = TypeAliasType("AsND_complexfloating", _To2_nd[np.complexfloating, Is[complex]])

As0D_inexact = TypeAliasType("As0D_inexact", _To2_0d[np.inexact, _PyInexact])
As1D_inexact = TypeAliasType("As1D_inexact", _To2_1d[np.inexact, _PyInexact])
As2D_inexact = TypeAliasType("As2D_inexact", _To2_2d[np.inexact, _PyInexact])
As3D_inexact = TypeAliasType("As3D_inexact", _To2_3d[np.inexact, _PyInexact])
AsND_inexact = TypeAliasType("AsND_inexact", _To2_nd[np.inexact, _PyInexact])

As0D_number = TypeAliasType("As0D_number", _To2_0d[np.number, _PyNumber])
As1D_number = TypeAliasType("As1D_number", _To2_1d[np.number, _PyNumber])
As2D_number = TypeAliasType("As2D_number", _To2_2d[np.number, _PyNumber])
As3D_number = TypeAliasType("As3D_number", _To2_3d[np.number, _PyNumber])
AsND_number = TypeAliasType("AsND_number", _To2_nd[np.number, _PyNumber])

# `npt.NDArray` variant with (optional) 2nd shape-typing parameter
ToND = TypeAliasType("ToND", np.ndarray[AnyShapeC, np.dtype[_ScalarT]], type_params=(_ScalarT, AnyShapeC))
To0D = TypeAliasType("To0D", np.ndarray[tuple[()], np.dtype[_ScalarT]], type_params=(_ScalarT,))
To1D = TypeAliasType("To1D", np.ndarray[tuple[int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
To2D = TypeAliasType("To2D", np.ndarray[tuple[int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))
To3D = TypeAliasType("To3D", np.ndarray[tuple[int, int, int], np.dtype[_ScalarT]], type_params=(_ScalarT,))

# Coercible (overlapping) scalar- and array-likes
To0D_bool = TypeAliasType("To0D_bool", _To2_0d[_ToBool, bool])
To1D_bool = TypeAliasType("To1D_bool", _To2_1d[_ToBool, bool])
To2D_bool = TypeAliasType("To2D_bool", _To2_2d[_ToBool, bool])
To3D_bool = TypeAliasType("To3D_bool", _To2_3d[_ToBool, bool])
ToND_bool = TypeAliasType("ToND_bool", _To2_nd[_ToBool, bool])

To0D_int8 = TypeAliasType("To0D_int8", _To2_0d[_ToInt8, bool])
To1D_int8 = TypeAliasType("To1D_int8", _To2_1d[_ToInt8, bool])
To2D_int8 = TypeAliasType("To2D_int8", _To2_2d[_ToInt8, bool])
To3D_int8 = TypeAliasType("To3D_int8", _To2_3d[_ToInt8, bool])
ToND_int8 = TypeAliasType("ToND_int8", _To2_nd[_ToInt8, bool])

To0D_int16 = TypeAliasType("To0D_int16", _To2_0d[_ToInt16, bool])
To1D_int16 = TypeAliasType("To1D_int16", _To2_1d[_ToInt16, bool])
To2D_int16 = TypeAliasType("To2D_int16", _To2_2d[_ToInt16, bool])
To3D_int16 = TypeAliasType("To3D_int16", _To2_3d[_ToInt16, bool])
ToND_int16 = TypeAliasType("ToND_int16", _To2_nd[_ToInt16, bool])

To0D_int32 = TypeAliasType("To0D_int32", _To2_0d[_ToInt32, bool])
To1D_int32 = TypeAliasType("To1D_int32", _To2_1d[_ToInt32, bool])
To2D_int32 = TypeAliasType("To2D_int32", _To2_2d[_ToInt32, bool])
To3D_int32 = TypeAliasType("To3D_int32", _To2_3d[_ToInt32, bool])
ToND_int32 = TypeAliasType("ToND_int32", _To2_nd[_ToInt32, bool])

To0D_int64 = TypeAliasType("To0D_int64", _To2_0d[_ToInt64, int])
To1D_int64 = TypeAliasType("To1D_int64", _To2_1d[_ToInt64, int])
To2D_int64 = TypeAliasType("To2D_int64", _To2_2d[_ToInt64, int])
To3D_int64 = TypeAliasType("To3D_int64", _To2_3d[_ToInt64, int])
ToND_int64 = TypeAliasType("ToND_int64", _To2_nd[_ToInt64, int])

To0D_long = TypeAliasType("To0D_long", _To2_0d[_ToLong, bool])
To1D_long = TypeAliasType("To1D_long", _To2_1d[_ToLong, bool])
To2D_long = TypeAliasType("To2D_long", _To2_2d[_ToLong, bool])
To3D_long = TypeAliasType("To3D_long", _To2_3d[_ToLong, bool])
ToND_long = TypeAliasType("ToND_long", _To2_nd[_ToLong, bool])

To0D_intp = TypeAliasType("To0D_intp", _To2_0d[_ToIntP, int])
To1D_intp = TypeAliasType("To1D_intp", _To2_1d[_ToIntP, int])
To2D_intp = TypeAliasType("To2D_intp", _To2_2d[_ToIntP, int])
To3D_intp = TypeAliasType("To3D_intp", _To2_3d[_ToIntP, int])
ToND_intp = TypeAliasType("ToND_intp", _To2_nd[_ToIntP, int])

To0D_longlong = TypeAliasType("To0D_longlong", _To2_0d[_ToLongLong, int])
To1D_longlong = TypeAliasType("To1D_longlong", _To2_1d[_ToLongLong, int])
To2D_longlong = TypeAliasType("To2D_longlong", _To2_2d[_ToLongLong, int])
To3D_longlong = TypeAliasType("To3D_longlong", _To2_3d[_ToLongLong, int])
ToND_longlong = TypeAliasType("ToND_longlong", _To2_nd[_ToLongLong, int])

To0D_uint8 = TypeAliasType("To0D_uint8", _To2_0d[_ToUInt8, bool])
To1D_uint8 = TypeAliasType("To1D_uint8", _To2_1d[_ToUInt8, bool])
To2D_uint8 = TypeAliasType("To2D_uint8", _To2_2d[_ToUInt8, bool])
To3D_uint8 = TypeAliasType("To3D_uint8", _To2_3d[_ToUInt8, bool])
ToND_uint8 = TypeAliasType("ToND_uint8", _To2_nd[_ToUInt8, bool])

To0D_uint16 = TypeAliasType("To0D_uint16", _To2_0d[_ToUInt16, bool])
To1D_uint16 = TypeAliasType("To1D_uint16", _To2_1d[_ToUInt16, bool])
To2D_uint16 = TypeAliasType("To2D_uint16", _To2_2d[_ToUInt16, bool])
To3D_uint16 = TypeAliasType("To3D_uint16", _To2_3d[_ToUInt16, bool])
ToND_uint16 = TypeAliasType("ToND_uint16", _To2_nd[_ToUInt16, bool])

To0D_uint32 = TypeAliasType("To0D_uint32", _To2_0d[_ToUInt32, bool])
To1D_uint32 = TypeAliasType("To1D_uint32", _To2_1d[_ToUInt32, bool])
To2D_uint32 = TypeAliasType("To2D_uint32", _To2_2d[_ToUInt32, bool])
To3D_uint32 = TypeAliasType("To3D_uint32", _To2_3d[_ToUInt32, bool])
ToND_uint32 = TypeAliasType("ToND_uint32", _To2_nd[_ToUInt32, bool])

To0D_uint64 = TypeAliasType("To0D_uint64", _To2_0d[_ToUInt64, bool])
To1D_uint64 = TypeAliasType("To1D_uint64", _To2_1d[_ToUInt64, bool])
To2D_uint64 = TypeAliasType("To2D_uint64", _To2_2d[_ToUInt64, bool])
To3D_uint64 = TypeAliasType("To3D_uint64", _To2_3d[_ToUInt64, bool])
ToND_uint64 = TypeAliasType("ToND_uint64", _To2_nd[_ToUInt64, bool])

To0D_ulong = TypeAliasType("To0D_ulong", _To2_0d[_ToULong, bool])
To1D_ulong = TypeAliasType("To1D_ulong", _To2_1d[_ToULong, bool])
To2D_ulong = TypeAliasType("To2D_ulong", _To2_2d[_ToULong, bool])
To3D_ulong = TypeAliasType("To3D_ulong", _To2_3d[_ToULong, bool])
ToND_ulong = TypeAliasType("ToND_ulong", _To2_nd[_ToULong, bool])

To0D_uintp = TypeAliasType("To0D_uintp", _To2_0d[_ToUIntP, bool])
To1D_uintp = TypeAliasType("To1D_uintp", _To2_1d[_ToUIntP, bool])
To2D_uintp = TypeAliasType("To2D_uintp", _To2_2d[_ToUIntP, bool])
To3D_uintp = TypeAliasType("To3D_uintp", _To2_3d[_ToUIntP, bool])
ToND_uintp = TypeAliasType("ToND_uintp", _To2_nd[_ToUIntP, bool])

To0D_ulonglong = TypeAliasType("To0D_ulonglong", _To2_0d[_ToULongLong, bool])
To1D_ulonglong = TypeAliasType("To1D_ulonglong", _To2_1d[_ToULongLong, bool])
To2D_ulonglong = TypeAliasType("To2D_ulonglong", _To2_2d[_ToULongLong, bool])
To3D_ulonglong = TypeAliasType("To3D_ulonglong", _To2_3d[_ToULongLong, bool])
ToND_ulonglong = TypeAliasType("ToND_ulonglong", _To2_nd[_ToULongLong, bool])

To0D_float16 = TypeAliasType("To0D_float16", _To2_0d[_ToFloat16, bool])
To1D_float16 = TypeAliasType("To1D_float16", _To2_1d[_ToFloat16, bool])
To2D_float16 = TypeAliasType("To2D_float16", _To2_2d[_ToFloat16, bool])
To3D_float16 = TypeAliasType("To3D_float16", _To2_3d[_ToFloat16, bool])
ToND_float16 = TypeAliasType("ToND_float16", _To2_nd[_ToFloat16, bool])

To0D_float32 = TypeAliasType("To0D_float32", _To2_0d[_ToFloat32, bool])
To1D_float32 = TypeAliasType("To1D_float32", _To2_1d[_ToFloat32, bool])
To2D_float32 = TypeAliasType("To2D_float32", _To2_2d[_ToFloat32, bool])
To3D_float32 = TypeAliasType("To3D_float32", _To2_3d[_ToFloat32, bool])
ToND_float32 = TypeAliasType("ToND_float32", _To2_nd[_ToFloat32, bool])

To0D_float64 = TypeAliasType("To0D_float64", _To2_0d[_ToFloat64, float])
To1D_float64 = TypeAliasType("To1D_float64", _To2_1d[_ToFloat64, float])
To2D_float64 = TypeAliasType("To2D_float64", _To2_2d[_ToFloat64, float])
To3D_float64 = TypeAliasType("To3D_float64", _To2_3d[_ToFloat64, float])
ToND_float64 = TypeAliasType("ToND_float64", _To2_nd[_ToFloat64, float])

To0D_longdouble = TypeAliasType("To0D_longdouble", _To2_0d[_ToLongDouble, float])
To1D_longdouble = TypeAliasType("To1D_longdouble", _To2_1d[_ToLongDouble, float])
To2D_longdouble = TypeAliasType("To2D_longdouble", _To2_2d[_ToLongDouble, float])
To3D_longdouble = TypeAliasType("To3D_longdouble", _To2_3d[_ToLongDouble, float])
ToND_longdouble = TypeAliasType("ToND_longdouble", _To2_nd[_ToLongDouble, float])

To0D_complex64 = TypeAliasType("To0D_complex64", _To2_0d[_ToComplex64, bool])
To1D_complex64 = TypeAliasType("To1D_complex64", _To2_1d[_ToComplex64, bool])
To2D_complex64 = TypeAliasType("To2D_complex64", _To2_2d[_ToComplex64, bool])
To3D_complex64 = TypeAliasType("To3D_complex64", _To2_3d[_ToComplex64, bool])
ToND_complex64 = TypeAliasType("ToND_complex64", _To2_nd[_ToComplex64, bool])

To0D_complex128 = TypeAliasType("To0D_complex128", _To2_0d[_ToComplex128, complex])
To1D_complex128 = TypeAliasType("To1D_complex128", _To2_1d[_ToComplex128, complex])
To2D_complex128 = TypeAliasType("To2D_complex128", _To2_2d[_ToComplex128, complex])
To3D_complex128 = TypeAliasType("To3D_complex128", _To2_3d[_ToComplex128, complex])
ToND_complex128 = TypeAliasType("ToND_complex128", _To2_nd[_ToComplex128, complex])

To0D_clongdouble = TypeAliasType("To0D_clongdouble", _To2_0d[_ToCLongDouble, complex])
To1D_clongdouble = TypeAliasType("To1D_clongdouble", _To2_1d[_ToCLongDouble, complex])
To2D_clongdouble = TypeAliasType("To2D_clongdouble", _To2_2d[_ToCLongDouble, complex])
To3D_clongdouble = TypeAliasType("To3D_clongdouble", _To2_3d[_ToCLongDouble, complex])
ToND_clongdouble = TypeAliasType("ToND_clongdouble", _To2_nd[_ToCLongDouble, complex])

To0D_timedelta = TypeAliasType("To0D_timedelta", _To2_0d[_ToTimeDelta, int])
To1D_timedelta = TypeAliasType("To1D_timedelta", _To2_1d[_ToTimeDelta, int])
To2D_timedelta = TypeAliasType("To2D_timedelta", _To2_2d[_ToTimeDelta, int])
To3D_timedelta = TypeAliasType("To3D_timedelta", _To2_3d[_ToTimeDelta, int])
ToND_timedelta = TypeAliasType("ToND_timedelta", _To2_nd[_ToTimeDelta, int])

To0D_datetime = TypeAliasType("To0D_datetime", _To1_0d[_ToDateTime])
To1D_datetime = TypeAliasType("To1D_datetime", _To1_1d[_ToDateTime])
To2D_datetime = TypeAliasType("To2D_datetime", _To1_2d[_ToDateTime])
To3D_datetime = TypeAliasType("To3D_datetime", _To1_3d[_ToDateTime])
ToND_datetime = TypeAliasType("ToND_datetime", _To1_nd[_ToDateTime])

To0D_bytes = TypeAliasType("To0D_bytes", _To2_0d[_ToBytes, bytes])
To1D_bytes = TypeAliasType("To1D_bytes", _To2_1d[_ToBytes, bytes])
To2D_bytes = TypeAliasType("To2D_bytes", _To2_2d[_ToBytes, bytes])
To3D_bytes = TypeAliasType("To3D_bytes", _To2_3d[_ToBytes, bytes])
ToND_bytes = TypeAliasType("ToND_bytes", _To2_nd[_ToBytes, bytes])

To0D_str = TypeAliasType("To0D_str", _To2_0d[_ToStr, bytes | str])
To1D_str = TypeAliasType("To1D_str", _To2_1d[_ToStr, bytes | str])
To2D_str = TypeAliasType("To2D_str", _To2_2d[_ToStr, bytes | str])
To3D_str = TypeAliasType("To3D_str", _To2_3d[_ToStr, bytes | str])
ToND_str = TypeAliasType("ToND_str", _To2_nd[_ToStr, bytes | str])

To0D_object = TypeAliasType("To0D_object", _To2_0d[_ToObject, object])
To1D_object = TypeAliasType("To1D_object", _To2_1d[_ToObject, object])
To2D_object = TypeAliasType("To2D_object", _To2_2d[_ToObject, object])
To3D_object = TypeAliasType("To3D_object", _To2_3d[_ToObject, object])
ToND_object = TypeAliasType("ToND_object", _To2_nd[_ToObject, object])

###
# DType-likes
# TODO
