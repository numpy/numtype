# NOTE: Numpy's mypy plugin is used for importing the correct
# platform-specific `ctypes._SimpleCData[int]` sub-type
import ctypes as ct
from _typeshed import StrOrBytesPath
from collections.abc import Iterable, Sequence
from ctypes import c_int64 as _c_intp
from typing import (
    Any,
    ClassVar,
    Generic,
    Literal as L,
    TypeAlias,
    TypeVar,
    overload,
)

import numpy as np
from numpy import (
    byte,
    double,
    dtype,
    generic,
    intc,
    long,
    longdouble,
    longlong,
    ndarray,
    short,
    single,
    ubyte,
    uintc,
    ulong,
    ulonglong,
    ushort,
    void,
)
from numpy._core._internal import _ctypes
from numpy._core.multiarray import flagsobj
from numpy._typing import (
    # DTypes
    DTypeLike,
    # Arrays
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
    # Shapes
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

# TODO: Add a proper `_Shape` bound once we've got variadic typevars
_DType = TypeVar("_DType", bound=dtype[Any])
_DTypeOptional = TypeVar("_DTypeOptional", bound=dtype[Any] | None)
_SCT = TypeVar("_SCT", bound=generic)

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

# TODO: Add a shape typevar once we have variadic typevars (PEP 646)
class _ndptr(ct.c_void_p, Generic[_DTypeOptional]):
    # In practice these 4 classvars are defined in the dynamic class
    # returned by `ndpointer`
    _dtype_: ClassVar[_DTypeOptional]
    _shape_: ClassVar[None]
    _ndim_: ClassVar[int | None]
    _flags_: ClassVar[list[_FlagsKind] | None]

    @overload
    @classmethod
    def from_param(cls: type[_ndptr[None]], obj: NDArray[Any]) -> _ctypes[Any]: ...
    @overload
    @classmethod
    def from_param(cls: type[_ndptr[_DType]], obj: ndarray[Any, _DType]) -> _ctypes[Any]: ...

class _concrete_ndptr(_ndptr[_DType]):
    _dtype_: ClassVar[_DType]
    _shape_: ClassVar[tuple[int, ...]]
    @property
    def contents(self) -> ndarray[_Shape, _DType]: ...

def load_library(libname: StrOrBytesPath, loader_path: StrOrBytesPath) -> ct.CDLL: ...

c_intp = _c_intp

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
) -> type[_concrete_ndptr[dtype[_SCT]]]: ...
@overload
def ndpointer(
    dtype: DTypeLike,
    ndim: int = ...,
    *,
    shape: _ShapeLike,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_concrete_ndptr[dtype[Any]]]: ...
@overload
def ndpointer(
    dtype: _DTypeLike[_SCT],
    ndim: int = ...,
    shape: None = ...,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_ndptr[dtype[_SCT]]]: ...
@overload
def ndpointer(
    dtype: DTypeLike,
    ndim: int = ...,
    shape: None = ...,
    flags: _FlagsKind | Iterable[_FlagsKind] | int | flagsobj | None = ...,
) -> type[_ndptr[dtype[Any]]]: ...
@overload
def as_ctypes_type(dtype: _BoolCodes | _DTypeLike[np.bool] | type[ct.c_bool]) -> type[ct.c_bool]: ...
@overload
def as_ctypes_type(dtype: _ByteCodes | _DTypeLike[byte] | type[ct.c_byte]) -> type[ct.c_byte]: ...
@overload
def as_ctypes_type(dtype: _ShortCodes | _DTypeLike[short] | type[ct.c_short]) -> type[ct.c_short]: ...
@overload
def as_ctypes_type(dtype: _IntCCodes | _DTypeLike[intc] | type[ct.c_int]) -> type[ct.c_int]: ...
@overload
def as_ctypes_type(dtype: _LongCodes | _DTypeLike[long] | type[ct.c_long]) -> type[ct.c_long]: ...
@overload
def as_ctypes_type(dtype: type[int]) -> type[c_intp]: ...
@overload
def as_ctypes_type(dtype: _LongLongCodes | _DTypeLike[longlong] | type[ct.c_longlong]) -> type[ct.c_longlong]: ...
@overload
def as_ctypes_type(dtype: _UByteCodes | _DTypeLike[ubyte] | type[ct.c_ubyte]) -> type[ct.c_ubyte]: ...
@overload
def as_ctypes_type(dtype: _UShortCodes | _DTypeLike[ushort] | type[ct.c_ushort]) -> type[ct.c_ushort]: ...
@overload
def as_ctypes_type(dtype: _UIntCCodes | _DTypeLike[uintc] | type[ct.c_uint]) -> type[ct.c_uint]: ...
@overload
def as_ctypes_type(dtype: _ULongCodes | _DTypeLike[ulong] | type[ct.c_ulong]) -> type[ct.c_ulong]: ...
@overload
def as_ctypes_type(dtype: _ULongLongCodes | _DTypeLike[ulonglong] | type[ct.c_ulonglong]) -> type[ct.c_ulonglong]: ...
@overload
def as_ctypes_type(dtype: _SingleCodes | _DTypeLike[single] | type[ct.c_float]) -> type[ct.c_float]: ...
@overload
def as_ctypes_type(dtype: _DoubleCodes | _DTypeLike[double] | type[float | ct.c_double]) -> type[ct.c_double]: ...
@overload
def as_ctypes_type(dtype: _LongDoubleCodes | _DTypeLike[longdouble] | type[ct.c_longdouble]) -> type[ct.c_longdouble]: ...
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
def as_ctypes(obj: byte) -> ct.c_byte: ...
@overload
def as_ctypes(obj: short) -> ct.c_short: ...
@overload
def as_ctypes(obj: intc) -> ct.c_int: ...
@overload
def as_ctypes(obj: long) -> ct.c_long: ...
@overload
def as_ctypes(obj: longlong) -> ct.c_longlong: ...
@overload
def as_ctypes(obj: ubyte) -> ct.c_ubyte: ...
@overload
def as_ctypes(obj: ushort) -> ct.c_ushort: ...
@overload
def as_ctypes(obj: uintc) -> ct.c_uint: ...
@overload
def as_ctypes(obj: ulong) -> ct.c_ulong: ...
@overload
def as_ctypes(obj: ulonglong) -> ct.c_ulonglong: ...
@overload
def as_ctypes(obj: single) -> ct.c_float: ...
@overload
def as_ctypes(obj: double) -> ct.c_double: ...
@overload
def as_ctypes(obj: longdouble) -> ct.c_longdouble: ...
@overload
def as_ctypes(obj: void) -> Any: ...  # `ctypes.Union` or `ctypes.Structure`
@overload
def as_ctypes(obj: NDArray[np.bool]) -> ct.Array[ct.c_bool]: ...
@overload
def as_ctypes(obj: NDArray[byte]) -> ct.Array[ct.c_byte]: ...
@overload
def as_ctypes(obj: NDArray[short]) -> ct.Array[ct.c_short]: ...
@overload
def as_ctypes(obj: NDArray[intc]) -> ct.Array[ct.c_int]: ...
@overload
def as_ctypes(obj: NDArray[long]) -> ct.Array[ct.c_long]: ...
@overload
def as_ctypes(obj: NDArray[longlong]) -> ct.Array[ct.c_longlong]: ...
@overload
def as_ctypes(obj: NDArray[ubyte]) -> ct.Array[ct.c_ubyte]: ...
@overload
def as_ctypes(obj: NDArray[ushort]) -> ct.Array[ct.c_ushort]: ...
@overload
def as_ctypes(obj: NDArray[uintc]) -> ct.Array[ct.c_uint]: ...
@overload
def as_ctypes(obj: NDArray[ulong]) -> ct.Array[ct.c_ulong]: ...
@overload
def as_ctypes(obj: NDArray[ulonglong]) -> ct.Array[ct.c_ulonglong]: ...
@overload
def as_ctypes(obj: NDArray[single]) -> ct.Array[ct.c_float]: ...
@overload
def as_ctypes(obj: NDArray[double]) -> ct.Array[ct.c_double]: ...
@overload
def as_ctypes(obj: NDArray[longdouble]) -> ct.Array[ct.c_longdouble]: ...
@overload
def as_ctypes(obj: NDArray[void]) -> ct.Array[Any]: ...  # `ctypes.Union` or `ctypes.Structure`
