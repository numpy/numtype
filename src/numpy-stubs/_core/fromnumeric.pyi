from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal as L, Protocol, SupportsIndex as CanIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar, TypedDict, Unpack, deprecated

import numpy as np
from _numtype import (
    Array,
    Array0D,
    Array1D,
    CanArray0D,
    CanLenArray,
    CoComplex_0d,
    CoComplex_1nd,
    CoComplex_nd,
    CoFloating_nd,
    CoInteger_0d,
    CoInteger_1nd,
    CoInteger_nd,
    Is,
    ToBool_0d,
    ToBool_1nd,
    ToBool_nd,
    ToBytes_nd,
    ToComplex128_nd,
    ToComplex_nd,
    ToFloat64_nd,
    ToFloating_nd,
    ToGeneric_0d,
    ToGeneric_1ds,
    ToGeneric_1nd,
    ToIntP_nd,
    ToInteger_1d,
    ToInteger_nd,
    ToObject_nd,
    ToSInteger_nd,
    ToStr_nd,
    ToTimeDelta_nd,
    ToUInteger_nd,
    _ToArray_1nd,
    _ToArray_nd,
)
from numpy import _CastingKind, _ModeKind, _OrderACF, _OrderKACF, _PartitionKind, _SortKind, _SortSide  # noqa: ICN003
from numpy._globals import _NoValueType
from numpy._typing import ArrayLike, DTypeLike, _DTypeLike, _ShapeLike

__all__ = [
    "all",
    "amax",
    "amin",
    "any",
    "argmax",
    "argmin",
    "argpartition",
    "argsort",
    "around",
    "choose",
    "clip",
    "compress",
    "cumprod",
    "cumsum",
    "cumulative_prod",
    "cumulative_sum",
    "diagonal",
    "matrix_transpose",
    "max",
    "mean",
    "min",
    "ndim",
    "nonzero",
    "partition",
    "prod",
    "ptp",
    "put",
    "ravel",
    "repeat",
    "reshape",
    "resize",
    "round",
    "searchsorted",
    "shape",
    "size",
    "sort",
    "squeeze",
    "std",
    "sum",
    "swapaxes",
    "take",
    "trace",
    "transpose",
    "var",
]

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_NumberT = TypeVar("_NumberT", bound=np.number | np.object_)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_IndT_contra = TypeVar("_IndT_contra", contravariant=True)
_VT_contra = TypeVar("_VT_contra", contravariant=True)
_RT_co = TypeVar("_RT_co", covariant=True)

_AnyShapeT = TypeVar(
    "_AnyShapeT",
    tuple[()],
    tuple[int],
    tuple[int, int],
    tuple[int, int, int],
    tuple[int, int, int, int],
    tuple[int, int, int, int, int],
    tuple[int, int, int, int, int, int],
    tuple[int, int, int, int, int, int, int],
    tuple[int, int, int, int, int, int, int, int],
    tuple[int, ...],
)

_PyArray: TypeAlias = list[_T] | tuple[_T, ...]
_PyScalar: TypeAlias = complex | bytes | str

_Order: TypeAlias = str | Sequence[str]

@type_check_only
class _CanPut(Protocol[_IndT_contra, _VT_contra, _RT_co]):
    def put(self, ind: _IndT_contra, v: _VT_contra, /, *, mode: _ModeKind) -> _RT_co: ...

@type_check_only
class _HasShape(Protocol[_ShapeT_co]):
    # NOTE: it matters that `self` is positional only
    @property
    def shape(self, /) -> _ShapeT_co: ...

@type_check_only
class UFuncKwargs(TypedDict, total=False):
    where: ToBool_nd | None
    order: _OrderKACF
    subok: bool
    signature: str | tuple[str | None, ...]
    casting: _CastingKind

###

@overload
def take(
    a: _ToArray_nd[_ScalarT],
    indices: CoInteger_0d,
    axis: None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> _ScalarT: ...
@overload
def take(
    a: _ToArray_nd[_ScalarT],
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Array[_ScalarT]: ...
@overload
def take(
    a: ArrayLike,
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Array: ...
@overload
def take(
    a: ArrayLike,
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    *,
    out: _ArrayT,
    mode: _ModeKind = "raise",
) -> _ArrayT: ...
@overload
def take(
    a: ArrayLike,
    indices: CoInteger_0d,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Any: ...

#
def put(a: _CanPut[_IndT_contra, _VT_contra, _RT_co], ind: _IndT_contra, v: _VT_contra, mode: _ModeKind = "raise") -> _RT_co: ...

#
@overload
def choose(a: CoInteger_nd, choices: ArrayLike, out: _ArrayT, mode: _ModeKind = "raise") -> _ArrayT: ...
@overload
def choose(a: CoInteger_0d, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> Any: ...
@overload
def choose(a: CoInteger_1nd, choices: _ToArray_nd[_ScalarT], out: None = None, mode: _ModeKind = "raise") -> Array[_ScalarT]: ...
@overload
def choose(a: CoInteger_1nd, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> Array: ...

#
@overload  # shape: index
def reshape(
    a: _ToArray_nd[_ScalarT],
    /,
    shape: CanIndex,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> np.ndarray[tuple[int], np.dtype[_ScalarT]]: ...
@overload  # shape: _AnyShape
def reshape(
    a: _ToArray_nd[_ScalarT],
    /,
    shape: _AnyShapeT,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: _ToArray_nd[_ScalarT],
    /,
    shape: Sequence[CanIndex],
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[_ScalarT]: ...
@overload  # shape: index
def reshape(
    a: ArrayLike,
    /,
    shape: CanIndex,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[Any, tuple[int]]: ...
@overload
def reshape(  # shape: _AnyShape
    a: ArrayLike,
    /,
    shape: _AnyShapeT,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: ArrayLike,
    /,
    shape: Sequence[CanIndex],
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array: ...
@overload
@deprecated("`newshape` is deprecated, `shape` instead. (deprecated in NumPy 2.1)")
def reshape(
    a: ArrayLike,
    /,
    shape: None = None,
    order: _OrderACF = "C",
    *,
    newshape: _ShapeLike,
    copy: bool | None = None,
) -> Array: ...

#
@overload
def swapaxes(a: _ToArray_nd[_ScalarT], axis1: CanIndex, axis2: CanIndex) -> Array[_ScalarT]: ...
@overload
def swapaxes(a: ArrayLike, axis1: CanIndex, axis2: CanIndex) -> Array: ...

#
@overload
def repeat(a: _ToArray_nd[_ScalarT], repeats: CoInteger_nd, axis: CanIndex | None = None) -> Array[_ScalarT]: ...
@overload
def repeat(a: ArrayLike, repeats: CoInteger_nd, axis: CanIndex | None = None) -> Array: ...

#
@overload
def transpose(a: _ToArray_nd[_ScalarT], axes: _ShapeLike | None = ...) -> Array[_ScalarT]: ...
@overload
def transpose(a: ArrayLike, axes: _ShapeLike | None = ...) -> Array: ...

#
@overload
def matrix_transpose(x: _ToArray_nd[_ScalarT], /) -> Array[_ScalarT]: ...
@overload
def matrix_transpose(x: ArrayLike, /) -> Array: ...

#
@overload
def partition(
    a: _ToArray_nd[_ScalarT],
    kth: ToInteger_nd,
    axis: CanIndex | None = None,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> Array[_ScalarT]: ...
@overload
def partition(
    a: ArrayLike,
    kth: ToInteger_nd,
    axis: CanIndex | None = None,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> Array: ...

#
def argpartition(
    a: ArrayLike,
    kth: ToInteger_nd,
    axis: CanIndex | None = -1,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> Array[np.intp]: ...

#
@overload  # known shape, known dtype, axis=<given>
def sort(
    a: CanLenArray[_ScalarT, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[_ScalarT, _ShapeT]: ...
@overload  # 0d, known dtype, axis=None
def sort(
    a: CanArray0D[_ScalarT],
    axis: None,
    kind: CanIndex | None = -1,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array1D[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=<given>
def sort(
    a: _ToArray_nd[_ScalarT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=None
def sort(
    a: _ToArray_nd[_ScalarT],
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array1D[_ScalarT]: ...
@overload  # unknown shape, unknown dtype, axis=<given>
def sort(
    a: ArrayLike,
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array: ...
@overload  # unknown shape, unknown dtype, axis=None
def sort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array1D[Any]: ...

#
@overload  # known shape
def argsort(
    a: CanLenArray[Any, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[np.intp, _ShapeT]: ...
@overload  # 0d or 1d array-like
def argsort(
    a: ToGeneric_0d | ToGeneric_1ds,
    axis: CanIndex | None = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array1D[np.intp]: ...
@overload  # axis=None
def argsort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array1D[np.intp]: ...
@overload  # fallback
def argsort(
    a: ArrayLike,
    axis: CanIndex | None = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[np.intp]: ...

#
@overload  # 0d or 1d , keepdims=False
def argmax(
    a: ToGeneric_0d | ToGeneric_1ds,
    axis: CanIndex,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # axis=None, keepdims=False
def argmax(a: ArrayLike, axis: None = None, out: None = None, *, keepdims: L[False] | _NoValueType = ...) -> np.intp: ...
@overload  # keepdims=True
def argmax(a: ArrayLike, axis: CanIndex | None = None, out: None = None, *, keepdims: L[True]) -> Array[np.intp]: ...
@overload  # out=<given> (positional)
def argmax(a: ArrayLike, axis: CanIndex | None, out: _ArrayT, *, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload  # out=<given> (keyword)
def argmax(a: ArrayLike, axis: CanIndex | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload  # fallback
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: Array | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload  # 0d or 1d , keepdims=False
def argmin(
    a: ToGeneric_0d | ToGeneric_1ds,
    axis: CanIndex,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # axis=None, keepdims=False
def argmin(a: ArrayLike, axis: None = None, out: None = None, *, keepdims: L[False] | _NoValueType = ...) -> np.intp: ...
@overload  # keepdims=True
def argmin(a: ArrayLike, axis: CanIndex | None = None, out: None = None, *, keepdims: L[True]) -> Array[np.intp]: ...
@overload  # out=<given> (positional)
def argmin(a: ArrayLike, axis: CanIndex | None, out: _ArrayT, *, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload  # out=<given> (keyword)
def argmin(a: ArrayLike, axis: CanIndex | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload  # fallback
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: Array | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload
def searchsorted(
    a: ArrayLike,
    v: ToGeneric_0d,
    side: _SortSide = "left",
    sorter: ToInteger_1d | None = None,
) -> np.intp: ...
@overload
def searchsorted(
    a: ArrayLike,
    v: ToGeneric_1nd,
    side: _SortSide = "left",
    sorter: ToInteger_1d | None = None,
) -> Array[np.intp]: ...

#
@overload
def resize(a: _ToArray_nd[_ScalarT], new_shape: CanIndex) -> Array1D[_ScalarT]: ...
@overload
def resize(a: _ToArray_nd[_ScalarT], new_shape: _AnyShapeT) -> Array[_ScalarT, _AnyShapeT]: ...
@overload
def resize(a: _ToArray_nd[_ScalarT], new_shape: Sequence[CanIndex]) -> Array[_ScalarT]: ...
@overload
def resize(a: ArrayLike, new_shape: CanIndex) -> Array1D[Any]: ...
@overload
def resize(a: ArrayLike, new_shape: _AnyShapeT) -> Array[Any, _AnyShapeT]: ...
@overload
def resize(a: ArrayLike, new_shape: Sequence[CanIndex]) -> Array: ...

#
@overload
def squeeze(a: CanArray0D[_ScalarT], axis: _ShapeLike | None = None) -> Array0D[_ScalarT]: ...
@overload
def squeeze(a: _ToArray_nd[_ScalarT], axis: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def squeeze(a: ArrayLike, axis: _ShapeLike | None = None) -> Array: ...

#
@overload
def diagonal(a: _ToArray_nd[_ScalarT], offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1) -> Array[_ScalarT]: ...
@overload
def diagonal(a: ArrayLike, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1) -> Array: ...

#
@overload
def trace(
    a: ArrayLike,
    offset: CanIndex = 0,
    axis1: CanIndex = 0,
    axis2: CanIndex = 1,
    dtype: DTypeLike | None = None,
    out: None = None,
) -> Incomplete: ...
@overload
def trace(
    a: ArrayLike,
    offset: CanIndex,
    axis1: CanIndex,
    axis2: CanIndex,
    dtype: DTypeLike | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def trace(
    a: ArrayLike,
    offset: CanIndex = 0,
    axis1: CanIndex = 0,
    axis2: CanIndex = 1,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def ravel(a: _ToArray_nd[_ScalarT], order: _OrderKACF = "C") -> Array1D[_ScalarT]: ...  # type: ignore[overload-overlap]
@overload
def ravel(a: ToBytes_nd, order: _OrderKACF = "C") -> Array1D[np.bytes_]: ...
@overload
def ravel(a: ToStr_nd, order: _OrderKACF = "C") -> Array1D[np.str_]: ...
@overload
def ravel(a: ToBool_nd, order: _OrderKACF = "C") -> Array1D[np.bool]: ...
@overload
def ravel(a: ToIntP_nd, order: _OrderKACF = "C") -> Array1D[np.intp]: ...
@overload
def ravel(a: ToFloat64_nd, order: _OrderKACF = "C") -> Array1D[np.float64]: ...
@overload
def ravel(a: ToComplex128_nd, order: _OrderKACF = "C") -> Array1D[np.complex128]: ...
@overload
def ravel(a: ArrayLike, order: _OrderKACF = "C") -> Array1D[Any]: ...

#
def nonzero(a: ToGeneric_1nd) -> tuple[Array[np.int_], ...]: ...

#
@overload
def shape(a: _HasShape[_ShapeT]) -> _ShapeT: ...
@overload
def shape(a: _PyScalar) -> tuple[()]: ...
@overload
def shape(a: _PyArray[ToGeneric_0d] | memoryview | bytearray) -> tuple[int]: ...
@overload
def shape(a: _PyArray[_PyArray[ToGeneric_0d]]) -> tuple[int, int]: ...
@overload
def shape(a: _PyArray[_PyArray[_PyArray[ToGeneric_0d]]]) -> tuple[int, int, int]: ...
@overload
def shape(a: ArrayLike) -> tuple[int, ...]: ...

#
@overload
def compress(
    condition: ToBool_nd,
    a: _ToArray_nd[_ScalarT],
    axis: CanIndex | None = None,
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def compress(condition: ToBool_nd, a: ArrayLike, axis: CanIndex | None = None, out: None = None) -> Array: ...
@overload
def compress(condition: ToBool_nd, a: ArrayLike, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
@overload
def compress(condition: ToBool_nd, a: ArrayLike, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def clip(
    a: _ScalarT,
    a_min: CoComplex_nd | _NoValueType | None = ...,
    a_max: CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ScalarT: ...
@overload
def clip(
    a: _ToArray_1nd[_ScalarT],
    a_min: CoComplex_nd | _NoValueType | None = ...,
    a_max: CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Array[_ScalarT]: ...
@overload
def clip(
    a: ToGeneric_1nd,
    a_min: CoComplex_nd | _NoValueType | None = ...,
    a_max: CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Array: ...
@overload
def clip(
    a: ToGeneric_0d,
    a_min: CoComplex_nd | _NoValueType | None = ...,
    a_max: CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Any: ...
@overload
def clip(
    a: ArrayLike,
    a_min: CoComplex_nd | _NoValueType | None,
    a_max: CoComplex_nd | _NoValueType | None,
    out: _ArrayT,
    *,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: CoComplex_nd | _NoValueType | None = ...,
    a_max: CoComplex_nd | _NoValueType | None = ...,
    *,
    out: _ArrayT,
    min: CoComplex_nd | _NoValueType | None = ...,
    max: CoComplex_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...

#
@overload
def sum(
    a: _ToArray_nd[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: _ToArray_nd[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> Any: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def all(
    a: ToGeneric_1ds,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def all(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: None,
    keepdims: L[True, 1],
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    *,
    keepdims: L[True, 1],
    where: ToBool_nd | _NoValueType = ...,
) -> Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: ToBool_0d | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool | Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: ToBool_0d | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: ToBool_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

# keep in sync with `all`
@overload
def any(
    a: ToGeneric_1ds,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def any(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: None,
    keepdims: L[True, 1],
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    *,
    keepdims: L[True, 1],
    where: ToBool_nd | _NoValueType = ...,
) -> Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: ToBool_0d | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.bool | Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: ToBool_0d | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: ToBool_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def cumsum(a: _ToArray_nd[_ScalarT], axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[_ScalarT]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, *, dtype: _DTypeLike[_ScalarT], out: None = None) -> Array[_ScalarT]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> Array: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def cumulative_sum(
    x: _ToArray_nd[_ScalarT],
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[_ScalarT]: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    include_initial: bool = False,
) -> Array[_ScalarT]: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: _ArrayT,
    include_initial: bool = False,
) -> _ArrayT: ...

#
@overload
def ptp(a: _ToArray_nd[_ScalarT], axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> _ScalarT: ...
@overload
def ptp(a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...) -> Any: ...
@overload
def ptp(a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...

#
@overload
def amax(
    a: _ToArray_nd[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> Any: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def amin(
    a: _ToArray_nd[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> Any: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: CoComplex_0d | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: `np.prod()``: For object arrays `initial` does not necessarily have to be a numerical scalar.
# The only requirement is that it is compatible with the `.__mul__()` method(s) of the passed array's elements.
# Note that the same situation holds for all wrappers around `np.ufunc.reduce`, e.g. `np.sum()` (`.__add__()`).
@overload
def prod(
    a: ToBool_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> np.int_: ...
@overload
def prod(
    a: ToUInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> np.uint64: ...
@overload
def prod(
    a: ToSInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> np.int64: ...
@overload
def prod(
    a: ToFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> np.floating: ...
@overload
def prod(
    a: ToComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> np.complexfloating: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> Any: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    out: None = None,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> Any: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> _ArrayT: ...
@overload
def prod(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    *,
    out: _ArrayT,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | CoComplex_0d = ...,
    where: _NoValueType | ToBool_nd = ...,
) -> _ArrayT: ...

#
@overload
def cumprod(a: ToBool_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.int_]: ...
@overload
def cumprod(a: ToUInteger_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.uint64]: ...
@overload
def cumprod(a: ToSInteger_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.int64]: ...
@overload
def cumprod(a: ToFloating_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.floating]: ...
@overload
def cumprod(a: ToComplex_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.complexfloating]: ...
@overload
def cumprod(a: ToObject_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[np.object_]: ...
@overload
def cumprod(
    a: CoComplex_nd | ToObject_nd,
    axis: CanIndex | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def cumprod(
    a: CoComplex_nd | ToObject_nd,
    axis: CanIndex | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def cumprod(
    a: CoComplex_nd | ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
) -> Array: ...
@overload
def cumprod(
    a: CoComplex_nd | ToObject_nd,
    axis: CanIndex | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def cumprod(
    a: CoComplex_nd | ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def cumulative_prod(
    x: ToBool_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.int_]: ...
@overload
def cumulative_prod(
    x: ToUInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.uint64]: ...
@overload
def cumulative_prod(
    x: ToSInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.int64]: ...
@overload
def cumulative_prod(
    x: ToFloating_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.floating]: ...
@overload
def cumulative_prod(
    x: ToComplex_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.complexfloating]: ...
@overload
def cumulative_prod(
    x: ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.object_]: ...
@overload
def cumulative_prod(
    x: CoComplex_nd | ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    include_initial: bool = False,
) -> Array[_ScalarT]: ...
@overload
def cumulative_prod(
    x: CoComplex_nd | ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array: ...
@overload
def cumulative_prod(
    x: CoComplex_nd | ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: _ArrayT,
    include_initial: bool = False,
) -> _ArrayT: ...

#
def ndim(a: ArrayLike) -> int: ...
def size(a: ArrayLike, axis: int | None = None) -> int: ...

#
@overload
def around(a: ToBool_0d, decimals: CanIndex = 0, out: None = None) -> np.float16: ...
@overload
def around(a: ToBool_1nd, decimals: CanIndex = 0, out: None = None) -> Array[np.float16]: ...
@overload
def around(a: CanArray0D[_NumberT], decimals: CanIndex = 0, out: None = None) -> _NumberT: ...
@overload
def around(a: _ToArray_1nd[_NumberT], decimals: CanIndex = 0, out: None = None) -> Array[_NumberT]: ...
@overload
def around(a: Is[int], decimals: CanIndex = 0, out: None = None) -> np.intp: ...
@overload
def around(a: Is[float], decimals: CanIndex = 0, out: None = None) -> np.float64: ...
@overload
def around(a: Is[complex], decimals: CanIndex = 0, out: None = None) -> np.complex128: ...
@overload
def around(a: CoComplex_nd, decimals: CanIndex, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: CoComplex_nd, decimals: CanIndex = 0, *, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: CoComplex_1nd, decimals: CanIndex = 0, out: Array | None = None) -> Array: ...

#
@overload
def mean(
    a: CoFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.floating: ...
@overload
def mean(
    a: ToComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.complexfloating: ...
@overload
def mean(
    a: ToTimeDelta_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> np.timedelta64: ...
@overload
def mean(
    a: ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> Any: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def mean(
    a: CoComplex_nd | ToTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: Array | None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
) -> Any: ...

#
@overload
def std(
    a: CoComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def std(
    a: ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def std(
    a: CoComplex_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: CoComplex_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: Array | None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...

#
@overload
def var(
    a: CoComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def var(
    a: ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def var(
    a: CoComplex_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: CoComplex_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: Array | None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: ToBool_nd | _NoValueType = ...,
    mean: CoComplex_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...

max = amax
min = amin
round = around
