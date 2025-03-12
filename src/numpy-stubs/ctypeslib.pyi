import _ctypes as _ct
import ctypes as ct
from _typeshed import StrOrBytesPath
from collections.abc import Iterable, Sequence
from typing import Any, ClassVar, Generic, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import Just
from numpy._core._internal import _ctypes
from numpy._core.multiarray import flagsobj
from numpy._typing import NDArray, _ArrayLike, _BoolCodes, _DTypeLike, _Shape, _ShapeLike, _VoidDTypeLike
from numpy._typing._char_codes import (
    _Float32Codes,
    _Float64Codes,
    _Float96Codes,
    _Float128Codes,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntPCodes,
    _LongCodes,
    _LongDoubleCodes,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntPCodes,
    _ULongCodes,
)

__all__ = ["as_array", "as_ctypes", "as_ctypes_type", "c_intp", "load_library", "ndpointer"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ShapeT = TypeVar("_ShapeT", bound=_Shape)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[Any], covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_Shape, default=_Shape, covariant=True)
_DTypeT0_co = TypeVar("_DTypeT0_co", bound=np.dtype[Any] | None, default=None, covariant=True)
_ShapeT0_co = TypeVar("_ShapeT0_co", bound=_Shape | None, default=None, covariant=True)

_FlagsKind: TypeAlias = L[
    "C", "C_CONTIGUOUS", "CONTIGUOUS",
    "F", "F_CONTIGUOUS", "FORTRAN",
    "A", "ALIGNED",
    "W", "WRITEABLE",
    "O", "OWNDATA",
    "X", "WRITEBACKIFCOPY",
]  # fmt: skip

###

c_intp = ct.c_ssize_t

class _ndptr(ct.c_void_p, Generic[_DTypeT0_co, _ShapeT0_co]):
    # In practice these 4 classvars are defined in the dynamic class
    # returned by `ndpointer`
    _dtype_: _DTypeT0_co
    _shape_: _ShapeT0_co
    _ndim_: ClassVar[int | None]
    _flags_: ClassVar[list[_FlagsKind] | None]

    @overload  # type: ignore[override]
    @classmethod
    def from_param(cls: type[_ndptr[_DTypeT, _ShapeT]], obj: np.ndarray[_ShapeT, _DTypeT]) -> _ctypes[int]: ...
    @overload
    @classmethod
    def from_param(cls: type[_ndptr], obj: NDArray[Any]) -> _ctypes[int]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class _concrete_ndptr(_ndptr[_DTypeT_co, _ShapeT_co], Generic[_DTypeT_co, _ShapeT_co]):
    def _check_retval_(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    @property
    def contents(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...

def load_library(libname: StrOrBytesPath, loader_path: StrOrBytesPath) -> ct.CDLL: ...
@overload
def ndpointer(
    dtype: None = None,
    ndim: int | None = None,
    shape: _ShapeLike | None = None,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = None,
) -> type[_ndptr[None]]: ...
@overload
def ndpointer(
    dtype: _DTypeLike[_ScalarT],
    ndim: int | None = None,
    *,
    shape: _ShapeLike,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = None,
) -> type[_concrete_ndptr[np.dtype[_ScalarT]]]: ...
@overload
def ndpointer(
    dtype: type | str,
    ndim: int | None = None,
    *,
    shape: _ShapeLike,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = None,
) -> type[_concrete_ndptr[np.dtype[Any]]]: ...
@overload
def ndpointer(
    dtype: _DTypeLike[_ScalarT],
    ndim: int | None = None,
    shape: None = None,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = None,
) -> type[_ndptr[np.dtype[_ScalarT]]]: ...
@overload
def ndpointer(
    dtype: type | str,
    ndim: int | None = None,
    shape: None = None,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = None,
) -> type[_ndptr[np.dtype[Any]]]: ...

#
@overload
def as_array(obj: ct._PointerLike, shape: Sequence[int]) -> NDArray[Any]: ...
@overload
def as_array(obj: _ArrayLike[_ScalarT], shape: _ShapeLike | None = ...) -> NDArray[_ScalarT]: ...
@overload
def as_array(obj: object, shape: _ShapeLike | None = ...) -> NDArray[Any]: ...

# NOTE: The overlapping overloads ignores are a temporary workaround for the non-unique
# intp/long/longlong issues, and otherwise mypy false positives.
# NOTE: `as_ctypes` doesn't support `void` values at the moment
@overload  # bool
def as_ctypes(obj: np.bool) -> ct.c_bool: ...
@overload
def as_ctypes(obj: NDArray[np.bool]) -> ct.Array[ct.c_bool]: ...
@overload  # int8 / byte
def as_ctypes(obj: np.int8) -> ct.c_byte: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.int8]) -> ct.Array[ct.c_byte]: ...  # type: ignore[overload-overlap]
@overload  # int16 / short
def as_ctypes(obj: np.int16) -> ct.c_short: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.int16]) -> ct.Array[ct.c_short]: ...  # type: ignore[overload-overlap]
@overload  # int32 / int[c]
def as_ctypes(obj: np.int32) -> ct.c_int: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.int32]) -> ct.Array[ct.c_int]: ...  # type: ignore[overload-overlap]
@overload  # intp / ssize_t (alias for `int`, `long` or `longlong`)
def as_ctypes(obj: np.intp) -> ct.c_ssize_t: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.intp]) -> ct.Array[ct.c_ssize_t]: ...  # pyright: ignore[reportOverlappingOverload]
@overload  # long
def as_ctypes(obj: np.long) -> ct.c_long: ...  # type: ignore[overload-cannot-match]   # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.long]) -> ct.Array[ct.c_long]: ...  # type: ignore[overload-cannot-match]   # pyright: ignore[reportOverlappingOverload]
@overload  # int64 / longlong (which might be an alias for for `long`)
def as_ctypes(obj: np.int64) -> ct.c_longlong: ...  # type: ignore[overload-cannot-match]   # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.int64 | np.longlong]) -> ct.Array[ct.c_longlong]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload  # uint8 / ubyte
def as_ctypes(obj: np.uint8) -> ct.c_ubyte: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.uint8]) -> ct.Array[ct.c_ubyte]: ...  # type: ignore[overload-overlap]
@overload  # uint16 / ushort
def as_ctypes(obj: np.uint16) -> ct.c_ushort: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.uint16]) -> ct.Array[ct.c_ushort]: ...  # type: ignore[overload-overlap]
@overload  # uint32 / uint
def as_ctypes(obj: np.uint32) -> ct.c_uint: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.uint32]) -> ct.Array[ct.c_uint]: ...  # type: ignore[overload-overlap]
@overload  # uintp / size_t
def as_ctypes(obj: np.uintp) -> ct.c_size_t: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.uintp]) -> ct.Array[ct.c_size_t]: ...  # pyright: ignore[reportOverlappingOverload]
@overload  # ulong
def as_ctypes(obj: np.ulong) -> ct.c_ulong: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.ulong]) -> ct.Array[ct.c_ulong]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload  # uint64 / ulonglong
def as_ctypes(obj: np.uint64) -> ct.c_ulonglong: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes(obj: NDArray[np.uint64]) -> ct.Array[ct.c_ulonglong]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload  # float32 / single / float
def as_ctypes(obj: np.float32) -> ct.c_float: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.float32]) -> ct.Array[ct.c_float]: ...  # type: ignore[overload-overlap]
@overload  # float64 / double
def as_ctypes(obj: np.float64 | np.double) -> ct.c_double: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes(obj: NDArray[np.float64 | np.double]) -> ct.Array[ct.c_double]: ...  # type: ignore[overload-overlap]
@overload  # float96 / float128 / longdouble
def as_ctypes(obj: np.float96 | np.float128 | np.longdouble) -> ct.c_longdouble: ...
@overload
def as_ctypes(obj: NDArray[np.float96 | np.float128 | np.longdouble]) -> ct.Array[ct.c_longdouble]: ...

#
@overload
def as_ctypes_type(dtype: _DTypeLike[np.bool] | type[ct.c_bool] | _BoolCodes) -> type[ct.c_bool]: ...
@overload
def as_ctypes_type(dtype: _DTypeLike[np.int8] | type[ct.c_int8 | ct.c_byte] | _Int8Codes) -> type[ct.c_byte]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.int16] | type[ct.c_int16 | ct.c_short] | _Int16Codes) -> type[ct.c_short]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.int32] | type[ct.c_int32 | ct.c_int] | _Int32Codes) -> type[ct.c_int]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.intp] | type[Just[int] | ct.c_ssize_t] | _IntPCodes) -> type[ct.c_ssize_t]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.long] | type[ct.c_long] | _LongCodes) -> type[ct.c_long]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.int64] | type[ct.c_int64 | ct.c_longlong] | _Int64Codes) -> type[ct.c_longlong]: ...
@overload
def as_ctypes_type(dtype: _DTypeLike[np.uint8] | type[ct.c_uint8 | ct.c_ubyte] | _UInt8Codes) -> type[ct.c_ubyte]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.uint16] | type[ct.c_uint16 | ct.c_ushort] | _UInt16Codes) -> type[ct.c_ushort]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.uint32] | type[ct.c_uint32 | ct.c_uint] | _UInt32Codes) -> type[ct.c_uint]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.uintp] | type[ct.c_size_t] | _UIntPCodes) -> type[ct.c_size_t]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.ulong] | type[ct.c_ulong] | _ULongCodes) -> type[ct.c_ulong]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.uint64] | type[ct.c_uint64 | ct.c_ulonglong] | _UInt64Codes) -> type[ct.c_ulonglong]: ...
@overload
def as_ctypes_type(dtype: _DTypeLike[np.float32 | np.single] | type[ct.c_float] | _Float32Codes) -> type[ct.c_float]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(dtype: _DTypeLike[np.float64 | np.double] | type[ct.c_double] | _Float64Codes) -> type[ct.c_double]: ...  # type: ignore[overload-overlap]
@overload
def as_ctypes_type(
    dtype: (
        _DTypeLike[np.float96 | np.float128 | np.longdouble]
        | type[ct.c_longdouble]
        | _Float96Codes
        | _Float128Codes
        | _LongDoubleCodes
    ),
) -> type[ct.c_longdouble]: ...
@overload
def as_ctypes_type(dtype: _VoidDTypeLike) -> _ct._UnionType | _ct._PyCStructType: ...
@overload
def as_ctypes_type(dtype: str) -> type: ...
