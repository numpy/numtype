import ctypes as ct
from _typeshed import StrOrBytesPath
from collections.abc import Iterable, Sequence
from typing import Any, ClassVar, Generic, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._core._internal import _ctypes
from numpy._core.multiarray import flagsobj
from numpy._typing import (
    DTypeLike,
    NDArray,
    _ArrayLike,
    _BoolCodes,
    _ByteCodes,
    _DTypeLike,
    _DoubleCodes,
    _IntCCodes,
    _LongCodes,
    _LongDoubleCodes,
    _LongLongCodes,
    _Shape,
    _ShapeLike,
    _ShortCodes,
    _SingleCodes,
    _UByteCodes,
    _UIntCCodes,
    _ULongCodes,
    _ULongLongCodes,
    _UShortCodes,
    _VoidDTypeLike,
)

__all__ = ["as_array", "as_ctypes", "as_ctypes_type", "c_intp", "load_library", "ndpointer"]

###

_SCT = TypeVar("_SCT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ShapeT = TypeVar("_ShapeT", bound=_Shape)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[Any], covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_Shape, default=_Shape, covariant=True)
_DTypeT0_co = TypeVar("_DTypeT0_co", bound=np.dtype[Any] | None, default=None, covariant=True)
_ShapeT0_co = TypeVar("_ShapeT0_co", bound=_Shape | None, default=None, covariant=True)

_FlagsKind: TypeAlias = L[
    "C_CONTIGUOUS",
    "CONTIGUOUS",
    "C",
    "F_CONTIGUOUS",
    "FORTRAN",
    "F",
    "ALIGNED",
    "A",
    "WRITEABLE",
    "W",
    "OWNDATA",
    "O",
    "WRITEBACKIFCOPY",
    "X",
]

class _ndptr(ct.c_void_p, Generic[_DTypeT0_co, _ShapeT0_co]):
    # In practice these 4 classvars are defined in the dynamic class
    # returned by `ndpointer`
    _dtype_: _DTypeT0_co
    _shape_: _ShapeT0_co
    _ndim_: ClassVar[int | None]
    _flags_: ClassVar[list[_FlagsKind] | None]

    @overload
    @classmethod
    def from_param(cls: type[_ndptr[_DTypeT, _ShapeT]], obj: np.ndarray[_ShapeT, _DTypeT]) -> _ctypes[int]: ...
    @overload
    @classmethod
    def from_param(cls: type[_ndptr], obj: NDArray[Any]) -> _ctypes[int]: ...

class _concrete_ndptr(_ndptr[_DTypeT_co, _ShapeT_co], Generic[_DTypeT_co, _ShapeT_co]):
    @property
    def contents(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...

def load_library(libname: StrOrBytesPath, loader_path: StrOrBytesPath) -> ct.CDLL: ...

c_intp = ct.c_ssize_t

@overload
def ndpointer(
    dtype: None = ...,
    ndim: int = ...,
    shape: _ShapeLike | None = ...,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_ndptr[None]]: ...
@overload
def ndpointer(
    dtype: _DTypeLike[_SCT],
    ndim: int = ...,
    *,
    shape: _ShapeLike,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_concrete_ndptr[np.dtype[_SCT]]]: ...
@overload
def ndpointer(
    dtype: DTypeLike,
    ndim: int = ...,
    *,
    shape: _ShapeLike,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_concrete_ndptr[np.dtype[Any]]]: ...
@overload
def ndpointer(
    dtype: _DTypeLike[_SCT],
    ndim: int = ...,
    shape: None = ...,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_ndptr[np.dtype[_SCT]]]: ...
@overload
def ndpointer(
    dtype: DTypeLike,
    ndim: int = ...,
    shape: None = ...,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_ndptr[np.dtype[Any]]]: ...
@overload
def as_ctypes_type(dtype: _BoolCodes | _DTypeLike[np.bool] | type[ct.c_bool]) -> type[ct.c_bool]: ...
@overload
def as_ctypes_type(dtype: _ByteCodes | _DTypeLike[np.byte] | type[ct.c_byte]) -> type[ct.c_byte]: ...
@overload
def as_ctypes_type(dtype: _ShortCodes | _DTypeLike[np.short] | type[ct.c_short]) -> type[ct.c_short]: ...
@overload
def as_ctypes_type(dtype: _IntCCodes | _DTypeLike[np.intc] | type[ct.c_int]) -> type[ct.c_int]: ...
@overload
def as_ctypes_type(dtype: _LongCodes | _DTypeLike[np.long] | type[ct.c_long]) -> type[ct.c_long]: ...
@overload
def as_ctypes_type(dtype: type[int]) -> type[c_intp]: ...
@overload
def as_ctypes_type(dtype: _LongLongCodes | _DTypeLike[np.longlong] | type[ct.c_longlong]) -> type[ct.c_longlong]: ...
@overload
def as_ctypes_type(dtype: _UByteCodes | _DTypeLike[np.ubyte] | type[ct.c_ubyte]) -> type[ct.c_ubyte]: ...
@overload
def as_ctypes_type(dtype: _UShortCodes | _DTypeLike[np.ushort] | type[ct.c_ushort]) -> type[ct.c_ushort]: ...
@overload
def as_ctypes_type(dtype: _UIntCCodes | _DTypeLike[np.uintc] | type[ct.c_uint]) -> type[ct.c_uint]: ...
@overload
def as_ctypes_type(dtype: _ULongCodes | _DTypeLike[np.ulong] | type[ct.c_ulong]) -> type[ct.c_ulong]: ...
@overload
def as_ctypes_type(dtype: _ULongLongCodes | _DTypeLike[np.ulonglong] | type[ct.c_ulonglong]) -> type[ct.c_ulonglong]: ...
@overload
def as_ctypes_type(dtype: _SingleCodes | _DTypeLike[np.single] | type[ct.c_float]) -> type[ct.c_float]: ...
@overload
def as_ctypes_type(dtype: _DoubleCodes | _DTypeLike[np.double] | type[float | ct.c_double]) -> type[ct.c_double]: ...
@overload
def as_ctypes_type(dtype: _LongDoubleCodes | _DTypeLike[np.longdouble] | type[ct.c_longdouble]) -> type[ct.c_longdouble]: ...
@overload
def as_ctypes_type(dtype: _VoidDTypeLike) -> type[Any]: ...  # `ctypes.Union` or `ctypes.Structure`
@overload
def as_ctypes_type(dtype: str) -> type[Any]: ...
@overload
def as_array(obj: ct._PointerLike, shape: Sequence[int]) -> NDArray[Any]: ...
@overload
def as_array(obj: _ArrayLike[_SCT], shape: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def as_array(obj: object, shape: _ShapeLike | None = ...) -> NDArray[Any]: ...
@overload
def as_ctypes(obj: np.bool) -> ct.c_bool: ...
@overload
def as_ctypes(obj: np.byte) -> ct.c_byte: ...
@overload
def as_ctypes(obj: np.short) -> ct.c_short: ...
@overload
def as_ctypes(obj: np.intc) -> ct.c_int: ...
@overload
def as_ctypes(obj: np.long) -> ct.c_long: ...
@overload
def as_ctypes(obj: np.longlong) -> ct.c_longlong: ...
@overload
def as_ctypes(obj: np.ubyte) -> ct.c_ubyte: ...
@overload
def as_ctypes(obj: np.ushort) -> ct.c_ushort: ...
@overload
def as_ctypes(obj: np.uintc) -> ct.c_uint: ...
@overload
def as_ctypes(obj: np.ulong) -> ct.c_ulong: ...
@overload
def as_ctypes(obj: np.ulonglong) -> ct.c_ulonglong: ...
@overload
def as_ctypes(obj: np.single) -> ct.c_float: ...
@overload
def as_ctypes(obj: np.double) -> ct.c_double: ...
@overload
def as_ctypes(obj: np.longdouble) -> ct.c_longdouble: ...
@overload
def as_ctypes(obj: np.void) -> Any: ...  # `ctypes.Union` or `ctypes.Structure`
@overload
def as_ctypes(obj: NDArray[np.bool]) -> ct.Array[ct.c_bool]: ...
@overload
def as_ctypes(obj: NDArray[np.byte]) -> ct.Array[ct.c_byte]: ...
@overload
def as_ctypes(obj: NDArray[np.short]) -> ct.Array[ct.c_short]: ...
@overload
def as_ctypes(obj: NDArray[np.intc]) -> ct.Array[ct.c_int]: ...
@overload
def as_ctypes(obj: NDArray[np.long]) -> ct.Array[ct.c_long]: ...
@overload
def as_ctypes(obj: NDArray[np.longlong]) -> ct.Array[ct.c_longlong]: ...
@overload
def as_ctypes(obj: NDArray[np.ubyte]) -> ct.Array[ct.c_ubyte]: ...
@overload
def as_ctypes(obj: NDArray[np.ushort]) -> ct.Array[ct.c_ushort]: ...
@overload
def as_ctypes(obj: NDArray[np.uintc]) -> ct.Array[ct.c_uint]: ...
@overload
def as_ctypes(obj: NDArray[np.ulong]) -> ct.Array[ct.c_ulong]: ...
@overload
def as_ctypes(obj: NDArray[np.ulonglong]) -> ct.Array[ct.c_ulonglong]: ...
@overload
def as_ctypes(obj: NDArray[np.single]) -> ct.Array[ct.c_float]: ...
@overload
def as_ctypes(obj: NDArray[np.double]) -> ct.Array[ct.c_double]: ...
@overload
def as_ctypes(obj: NDArray[np.longdouble]) -> ct.Array[ct.c_longdouble]: ...
@overload
def as_ctypes(obj: NDArray[np.void]) -> ct.Array[Any]: ...  # `ctypes.Union` or `ctypes.Structure`
