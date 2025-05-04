import _ctypes as _ct
import ctypes as ct
from _typeshed import StrOrBytesPath
from collections.abc import Iterable, Sequence
from typing import Any, ClassVar, Generic, Literal as L, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._core._internal import _ctypes
from numpy._core.multiarray import flagsobj
from numpy._typing import _ArrayLike, _DTypeLike, _ShapeLike, _VoidDTypeLike
from numpy._typing._char_codes import _LongCodes, _ULongCodes

__all__ = ["as_array", "as_ctypes", "as_ctypes_type", "c_intp", "load_library", "ndpointer"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.Shape, default=_nt.Shape, covariant=True)
_DTypeT0_co = TypeVar("_DTypeT0_co", bound=np.dtype | None, default=None, covariant=True)
_ShapeT0_co = TypeVar("_ShapeT0_co", bound=_nt.Shape | None, default=None, covariant=True)

_FlagsKind: TypeAlias = L[
    "C", "C_CONTIGUOUS", "CONTIGUOUS",
    "F", "F_CONTIGUOUS", "FORTRAN",
    "A", "ALIGNED",
    "W", "WRITEABLE",
    "O", "OWNDATA",
    "X", "WRITEBACKIFCOPY",
]  # fmt: skip

###

_CT = TypeVar("_CT", bound=ct._CData)
_CT_co = TypeVar("_CT_co", bound=ct._CData, covariant=True)

@type_check_only
class _HasCType(Protocol[_CT_co]):
    @property
    def __ctype__(self, /) -> _CT_co: ...

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
    def from_param(cls: type[_ndptr], obj: _nt.Array[Any]) -> _ctypes[int]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class _concrete_ndptr(_ndptr[_DTypeT_co, _ShapeT_co], Generic[_DTypeT_co, _ShapeT_co]):
    def _check_retval_(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    @property
    def contents(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...

def load_library(libname: StrOrBytesPath, loader_path: StrOrBytesPath) -> ct.CDLL: ...

#
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
) -> type[_concrete_ndptr[np.dtype]]: ...
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
) -> type[_ndptr[np.dtype]]: ...

#
@overload
def as_array(obj: ct._PointerLike, shape: Sequence[int]) -> _nt.Array[Any]: ...
@overload
def as_array(obj: _ArrayLike[_ScalarT], shape: _ShapeLike | None = ...) -> _nt.Array[_ScalarT]: ...
@overload
def as_array(obj: object, shape: _ShapeLike | None = ...) -> _nt.Array[Any]: ...

#
def as_ctypes(obj: _HasCType[_CT]) -> _CT: ...

#
@overload
def as_ctypes_type(dtype: _nt.ToDTypeBool) -> type[ct.c_bool]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeInt8) -> type[ct.c_int8]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeUInt8) -> type[ct.c_uint8]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeInt16) -> type[ct.c_int16]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeUInt16) -> type[ct.c_uint16]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeInt32) -> type[ct.c_int32]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeUInt32) -> type[ct.c_uint32]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeInt64) -> type[ct.c_int64]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeUInt64) -> type[ct.c_uint64]: ...
@overload
def as_ctypes_type(dtype: type[ct.c_long] | _LongCodes) -> type[ct.c_long]: ...
@overload
def as_ctypes_type(dtype: type[ct.c_ulong] | _ULongCodes) -> type[ct.c_ulong]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeFloat32) -> type[ct.c_float]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeFloat64) -> type[ct.c_double]: ...
@overload
def as_ctypes_type(dtype: _nt.ToDTypeLongDouble) -> type[ct.c_longdouble]: ...
@overload
def as_ctypes_type(dtype: _VoidDTypeLike) -> _ct._UnionType | _ct._PyCStructType: ...
@overload
def as_ctypes_type(dtype: str) -> type: ...
