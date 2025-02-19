from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal as L, NoReturn, Protocol, SupportsIndex as CanIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar, TypedDict, Unpack, deprecated

import numpy as np
from _numtype import (
    Array,
    Array_0d,
    Array_1d,
    CanArray,
    CanArraySized,
    CoFloating_nd,
    CoInteger_0d,
    CoInteger_1nd,
    CoInteger_nd,
    CoNumber_1nd,
    CoNumber_nd,
    Is,
    ToAny_1nd,
    ToBool_0d,
    ToBool_1nd,
    ToBool_nd,
    ToBytes_nd,
    ToCFloating_nd,
    ToComplex128_nd,
    ToFloat64_nd,
    ToFloating_nd,
    ToIntP_nd,
    ToInteger_1d,
    ToNumber_nd,
    ToObject_0d,
    ToObject_1nd,
    ToObject_nd,
    ToSInteger_nd,
    ToStr_nd,
    ToTimeDelta_nd,
    ToUInteger_nd,
    _ToArray_0d,
    _ToArray_1ds,
    _ToArray_1nd,
)
from numpy import _CastingKind, _ModeKind, _OrderACF, _OrderKACF, _SortKind, _SortSide  # noqa: ICN003
from numpy._globals import _NoValueType
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeInt_co,
    _DTypeLike,
    _IntLike_co,
    _NumberLike_co,
    _ScalarLike_co,
    _ShapeLike,
)

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

_AnyShapeT0 = TypeVar(
    "_AnyShapeT0",
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

_ToGeneric_0d: TypeAlias = _ToArray_0d[np.generic, _PyScalar]
_ToGeneric_1ds: TypeAlias = _ToArray_1ds[np.generic, _PyScalar]

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
    where: _ArrayLikeBool_co | None
    order: _OrderKACF
    subok: bool
    signature: str | tuple[str | None, ...]
    casting: _CastingKind

###

@overload
def take(
    a: _ArrayLike[_ScalarT],
    indices: _IntLike_co,
    axis: None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> _ScalarT: ...
@overload
def take(
    a: _ArrayLike[_ScalarT],
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Array[_ScalarT]: ...
@overload
def take(
    a: ArrayLike,
    indices: _IntLike_co,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Any: ...
@overload
def take(
    a: ArrayLike,
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Array[Any]: ...
@overload
def take(
    a: ArrayLike,
    indices: CoInteger_1nd,
    axis: CanIndex | None = None,
    *,
    out: _ArrayT,
    mode: _ModeKind = "raise",
) -> _ArrayT: ...

#
def put(a: _CanPut[_IndT_contra, _VT_contra, _RT_co], ind: _IndT_contra, v: _VT_contra, mode: _ModeKind = "raise") -> _RT_co: ...

#
@overload
def choose(a: CoInteger_nd, choices: ArrayLike, out: _ArrayT, mode: _ModeKind = "raise") -> _ArrayT: ...
@overload
def choose(a: CoInteger_0d, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> Any: ...
@overload
def choose(a: CoInteger_1nd, choices: _ArrayLike[_ScalarT], out: None = None, mode: _ModeKind = "raise") -> Array[_ScalarT]: ...
@overload
def choose(a: CoInteger_1nd, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> Array[Any]: ...

#
@overload
def reshape(  # shape: index
    a: _ArrayLike[_ScalarT],
    /,
    shape: CanIndex,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> np.ndarray[tuple[int], np.dtype[_ScalarT]]: ...
@overload
def reshape(  # shape: (int, ...) @ np._AnyShapeT
    a: _ArrayLike[_ScalarT],
    /,
    shape: _AnyShapeT0,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[_ScalarT, _AnyShapeT0]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: _ArrayLike[_ScalarT],
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
def reshape(  # shape: (int, ...) @ np._AnyShapeT
    a: ArrayLike,
    /,
    shape: _AnyShapeT0,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[Any, _AnyShapeT0]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: ArrayLike,
    /,
    shape: Sequence[CanIndex],
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> Array[Any]: ...
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
) -> Array[Any]: ...

#
@overload
def swapaxes(a: _ArrayLike[_ScalarT], axis1: CanIndex, axis2: CanIndex) -> Array[_ScalarT]: ...
@overload
def swapaxes(a: ArrayLike, axis1: CanIndex, axis2: CanIndex) -> Array[Any]: ...

#
@overload
def repeat(a: _ArrayLike[_ScalarT], repeats: _ArrayLikeInt_co, axis: CanIndex | None = None) -> Array[_ScalarT]: ...
@overload
def repeat(a: ArrayLike, repeats: _ArrayLikeInt_co, axis: CanIndex | None = None) -> Array[Any]: ...

#
@overload
def transpose(a: _ArrayLike[_ScalarT], axes: _ShapeLike | None = ...) -> Array[_ScalarT]: ...
@overload
def transpose(a: ArrayLike, axes: _ShapeLike | None = ...) -> Array[Any]: ...

#
@overload
def matrix_transpose(x: _ArrayLike[_ScalarT]) -> Array[_ScalarT]: ...
@overload
def matrix_transpose(x: ArrayLike) -> Array[Any]: ...

#
@overload
def partition(
    a: _ArrayLike[_ScalarT],
    kth: _ArrayLikeInt_co,
    axis: CanIndex | None = None,
    kind: np._PartitionKind = ...,
    order: _Order | None = ...,
) -> Array[_ScalarT]: ...
@overload
def partition(
    a: ArrayLike,
    kth: _ArrayLikeInt_co,
    axis: CanIndex | None = None,
    kind: np._PartitionKind = ...,
    order: _Order | None = ...,
) -> Array[Any]: ...
def argpartition(
    a: ArrayLike,
    kth: _ArrayLikeInt_co,
    axis: CanIndex | None = None,
    kind: np._PartitionKind = ...,
    order: _Order | None = ...,
) -> Array[np.int_]: ...

#
@overload  # known shape, known dtype, axis=<given>
def sort(
    a: CanArraySized[_ScalarT, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[_ScalarT, _ShapeT]: ...
@overload  # 0d, known dtype, axis=None
def sort(
    a: _ScalarT | CanArray[_ScalarT, tuple[()]],
    axis: None,
    kind: CanIndex | None = -1,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array_1d[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=<given>
def sort(
    a: _ArrayLike[_ScalarT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=None
def sort(
    a: _ArrayLike[_ScalarT],
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array_1d[_ScalarT]: ...
@overload  # unknown shape, unknown dtype, axis=<given>
def sort(
    a: ArrayLike,
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[Any]: ...
@overload  # unknown shape, unknown dtype, axis=None
def sort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array_1d[Any]: ...

#
@overload  # known shape
def argsort(
    a: CanArraySized[Any, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array[np.intp, _ShapeT]: ...
@overload  # 0d or 1d array-like
def argsort(
    a: _ToGeneric_0d | _ToGeneric_1ds,
    axis: CanIndex | None = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array_1d[np.intp]: ...
@overload  # axis=None
def argsort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> Array_1d[np.intp]: ...
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
    a: _ToGeneric_0d | _ToGeneric_1ds,
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
    out: Array[Any] | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload  # 0d or 1d , keepdims=False
def argmin(
    a: _ToGeneric_0d | _ToGeneric_1ds,
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
    out: Array[Any] | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload
def searchsorted(a: ArrayLike, v: _ScalarLike_co, side: _SortSide = "left", sorter: ToInteger_1d | None = None) -> np.intp: ...
@overload
def searchsorted(a: ArrayLike, v: ToAny_1nd, side: _SortSide = "left", sorter: ToInteger_1d | None = None) -> Array[np.intp]: ...

#
@overload
def resize(a: _ArrayLike[_ScalarT], new_shape: CanIndex) -> Array_1d[_ScalarT]: ...
@overload
def resize(a: _ArrayLike[_ScalarT], new_shape: _AnyShapeT0) -> Array[_ScalarT, _AnyShapeT0]: ...
@overload
def resize(a: _ArrayLike[_ScalarT], new_shape: Sequence[CanIndex]) -> Array[_ScalarT]: ...
@overload
def resize(a: ArrayLike, new_shape: CanIndex) -> Array_1d[Any]: ...
@overload
def resize(a: ArrayLike, new_shape: _AnyShapeT0) -> Array[Any, _AnyShapeT0]: ...
@overload
def resize(a: ArrayLike, new_shape: Sequence[CanIndex]) -> Array[Any]: ...

#
@overload
def squeeze(a: _ToArray_0d[_ScalarT], axis: _ShapeLike | None = None) -> Array_0d[_ScalarT]: ...
@overload
def squeeze(a: _ArrayLike[_ScalarT], axis: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def squeeze(a: ArrayLike, axis: _ShapeLike | None = None) -> Array[Any]: ...

#
@overload
def diagonal(a: _ArrayLike[_ScalarT], offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1) -> Array[_ScalarT]: ...
@overload
def diagonal(a: ArrayLike, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1) -> Array[Any]: ...

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
def ravel(a: _ArrayLike[_ScalarT], order: _OrderKACF = "C") -> Array_1d[_ScalarT]: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def ravel(a: ToBytes_nd, order: _OrderKACF = "C") -> Array_1d[np.bytes_]: ...
@overload
def ravel(a: ToStr_nd, order: _OrderKACF = "C") -> Array_1d[np.str_]: ...
@overload
def ravel(a: ToBool_nd, order: _OrderKACF = "C") -> Array_1d[np.bool]: ...
@overload
def ravel(a: ToIntP_nd, order: _OrderKACF = "C") -> Array_1d[np.int_ | np.bool]: ...
@overload
def ravel(a: ToFloat64_nd, order: _OrderKACF = "C") -> Array_1d[np.float64]: ...
@overload
def ravel(a: ToComplex128_nd, order: _OrderKACF = "C") -> Array_1d[np.complex128]: ...
@overload
def ravel(a: ArrayLike, order: _OrderKACF = "C") -> Array_1d[Any]: ...

#
@overload
def nonzero(a: np.generic | np.ndarray[tuple[()], Any]) -> NoReturn: ...
@overload
def nonzero(a: _ArrayLike[Any]) -> tuple[Array[np.int_], ...]: ...

#
@overload
def shape(a: _HasShape[_ShapeT]) -> _ShapeT: ...
@overload
def shape(a: _PyScalar) -> tuple[()]: ...
@overload
def shape(a: _PyArray[_ToGeneric_0d] | memoryview | bytearray) -> tuple[int]: ...
@overload
def shape(a: _PyArray[_PyArray[_ToGeneric_0d]]) -> tuple[int, int]: ...
@overload
def shape(a: _PyArray[_PyArray[_PyArray[_ToGeneric_0d]]]) -> tuple[int, int, int]: ...
@overload
def shape(a: ArrayLike) -> tuple[int, ...]: ...

#
@overload
def compress(
    condition: _ArrayLikeBool_co,
    a: _ArrayLike[_ScalarT],
    axis: CanIndex | None = None,
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def compress(condition: _ArrayLikeBool_co, a: ArrayLike, axis: CanIndex | None = None, out: None = None) -> Array[Any]: ...
@overload
def compress(condition: _ArrayLikeBool_co, a: ArrayLike, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
@overload
def compress(condition: _ArrayLikeBool_co, a: ArrayLike, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def clip(
    a: _ScalarT,
    a_min: ToNumber_nd | _NoValueType | None = ...,
    a_max: ToNumber_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ScalarT: ...
@overload
def clip(
    a: _ScalarLike_co,
    a_min: ToNumber_nd | _NoValueType | None = ...,
    a_max: ToNumber_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Any: ...
@overload
def clip(
    a: _ToArray_1nd[_ScalarT],
    a_min: ToNumber_nd | _NoValueType | None = ...,
    a_max: ToNumber_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Array[_ScalarT]: ...
@overload
def clip(
    a: _ToArray_1nd[Any, _PyScalar],
    a_min: ToNumber_nd | _NoValueType | None = ...,
    a_max: ToNumber_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Array[Any]: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ToNumber_nd | _NoValueType | None,
    a_max: ToNumber_nd | _NoValueType | None,
    out: _ArrayT,
    *,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ToNumber_nd | _NoValueType | None = ...,
    a_max: ToNumber_nd | _NoValueType | None = ...,
    *,
    out: _ArrayT,
    min: ToNumber_nd | _NoValueType | None = ...,
    max: ToNumber_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...

#
@overload
def sum(
    a: _ArrayLike[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: _ArrayLike[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> Any: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def all(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> np.bool: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: CanIndex = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> np.bool | Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: CanIndex = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> _ArrayT: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: CanIndex = False,
    where: _ArrayLikeBool_co = True,
) -> _ArrayT: ...

#
@overload
def any(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> np.bool: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: CanIndex = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> np.bool | Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: CanIndex = False,
    *,
    where: _ArrayLikeBool_co = True,
) -> _ArrayT: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: CanIndex = False,
    where: _ArrayLikeBool_co = True,
) -> _ArrayT: ...

#
@overload
def cumsum(a: _ArrayLike[_ScalarT], axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[_ScalarT]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: None = None, out: None = None) -> Array[Any]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, *, dtype: _DTypeLike[_ScalarT], out: None = None) -> Array[_ScalarT]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> Array[Any]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def cumulative_sum(
    x: _ArrayLike[_ScalarT],
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
) -> Array[Any]: ...
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
) -> Array[Any]: ...
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
def ptp(a: _ArrayLike[_ScalarT], axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> _ScalarT: ...
@overload
def ptp(a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...) -> Any: ...
@overload
def ptp(a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...

#
@overload
def amax(
    a: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> Any: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def amin(
    a: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> Any: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _NumberLike_co | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: `np.prod()``: For object arrays `initial` does not necessarily
# have to be a numerical scalar.
# The only requirement is that it is compatible
# with the `.__mul__()` method(s) of the passed array's elements.

# Note that the same situation holds for all wrappers around
# `np.ufunc.reduce`, e.g. `np.sum()` (`.__add__()`).
@overload
def prod(  # type: ignore[overload-overlap]
    a: ToBool_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> np.int_: ...
@overload
def prod(  # type: ignore[overload-overlap]
    a: ToUInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> np.uint64: ...
@overload
def prod(
    a: ToSInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> np.int64: ...
@overload
def prod(
    a: ToFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> np.floating: ...
@overload
def prod(
    a: ToCFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> np.complexfloating: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: bool = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> Any: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    out: None = None,
    keepdims: bool = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> Any: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: bool = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ArrayT: ...
@overload
def prod(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    *,
    out: _ArrayT,
    keepdims: bool = ...,
    initial: _NumberLike_co = ...,
    where: _ArrayLikeBool_co = ...,
) -> _ArrayT: ...

#
@overload
def cumprod(  # type: ignore[overload-overlap]
    a: ToBool_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.int_]: ...
@overload
def cumprod(  # type: ignore[overload-overlap]
    a: ToUInteger_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.uint64]: ...
@overload
def cumprod(  # type: ignore[overload-overlap]
    a: ToSInteger_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.int64]: ...
@overload
def cumprod(  # type: ignore[overload-overlap]
    a: ToFloating_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.floating]: ...
@overload
def cumprod(  # type: ignore[overload-overlap]
    a: ToCFloating_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.complexfloating]: ...
@overload
def cumprod(
    a: ToObject_nd,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
) -> Array[np.object_]: ...
@overload
def cumprod(
    a: CoNumber_nd | ToObject_nd,
    axis: CanIndex | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def cumprod(
    a: CoNumber_nd | ToObject_nd,
    axis: CanIndex | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> Array[_ScalarT]: ...
@overload
def cumprod(
    a: CoNumber_nd | ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
) -> Array[Any]: ...
@overload
def cumprod(
    a: CoNumber_nd | ToObject_nd,
    axis: CanIndex | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def cumprod(
    a: CoNumber_nd | ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def cumulative_prod(  # type: ignore[overload-overlap]
    x: ToBool_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.int_]: ...
@overload
def cumulative_prod(  # type: ignore[overload-overlap]
    x: ToUInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.uint64]: ...
@overload
def cumulative_prod(  # type: ignore[overload-overlap]
    x: ToSInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.int64]: ...
@overload
def cumulative_prod(  # type: ignore[overload-overlap]
    x: ToFloating_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[np.floating]: ...
@overload
def cumulative_prod(  # type: ignore[overload-overlap]
    x: ToCFloating_nd,
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
    x: CoNumber_nd | ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    include_initial: bool = False,
) -> Array[_ScalarT]: ...
@overload
def cumulative_prod(
    x: CoNumber_nd | ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    include_initial: bool = False,
) -> Array[Any]: ...
@overload
def cumulative_prod(
    x: CoNumber_nd | ToObject_nd,
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
def around(a: ToBool_0d, decimals: CanIndex = 0, out: None = None) -> np.float16: ...  # type: ignore[overload-overlap]
@overload
def around(a: ToBool_1nd, decimals: CanIndex = 0, out: None = None) -> Array[np.float16]: ...  # type: ignore[overload-overlap]
@overload
def around(a: _ToArray_0d[_NumberT], decimals: CanIndex = 0, out: None = None) -> _NumberT: ...  # type: ignore[overload-overlap]
@overload
def around(a: _ToArray_1nd[_NumberT], decimals: CanIndex = 0, out: None = None) -> Array[_NumberT]: ...
@overload
def around(a: Is[int], decimals: CanIndex = 0, out: None = None) -> np.intp: ...
@overload
def around(a: Is[float], decimals: CanIndex = 0, out: None = None) -> np.float64: ...
@overload
def around(a: Is[complex], decimals: CanIndex = 0, out: None = None) -> np.complex128: ...
@overload
def around(a: ToObject_0d, decimals: CanIndex = 0, out: None = None) -> Any: ...
@overload
def around(a: CoNumber_nd | ToObject_nd, decimals: CanIndex, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: CoNumber_nd | ToObject_nd, decimals: CanIndex = 0, *, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: CoNumber_1nd | ToObject_1nd, decimals: CanIndex = 0, out: None = None) -> Array[Any]: ...

#
@overload
def mean(  # type: ignore[overload-overlap]
    a: CoFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> np.floating: ...
@overload
def mean(  # type: ignore[overload-overlap]
    a: ToCFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> np.complexfloating: ...
@overload
def mean(
    a: ToTimeDelta_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> np.timedelta64: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> Any: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ScalarT | Array[_ScalarT]: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> Any: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def mean(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def std(
    a: _ArrayLikeComplex_co,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: _ArrayLikeComplex_co | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...

#
@overload
def var(
    a: _ArrayLikeComplex_co,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: _ArrayLikeComplex_co | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: CoNumber_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _ArrayLikeBool_co | _NoValueType = ...,
    mean: CoNumber_nd | ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...

max = amax
min = amin
round = around
