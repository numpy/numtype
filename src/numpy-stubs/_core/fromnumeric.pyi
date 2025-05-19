from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal as L, Protocol, SupportsIndex as CanIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar, TypedDict, Unpack, deprecated

import _numtype as _nt
import numpy as np
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

_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_NumberT = TypeVar("_NumberT", bound=np.number | np.object_)
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

_Order: TypeAlias = str | Sequence[str]

@type_check_only
class _CanPut(Protocol[_IndT_contra, _VT_contra, _RT_co]):
    def put(self, ind: _IndT_contra, v: _VT_contra, /, *, mode: _ModeKind) -> _RT_co: ...

@type_check_only
class UFuncKwargs(TypedDict, total=False):
    where: _nt.ToBool_nd | None
    order: _OrderKACF
    subok: bool
    signature: str | tuple[str | None, ...]
    casting: _CastingKind

###

@overload
def take(
    a: _nt._ToArray_nd[_ScalarT],
    indices: _nt.CoInteger_0d,
    axis: None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> _ScalarT: ...
@overload
def take(
    a: _nt._ToArray_nd[_ScalarT],
    indices: _nt.CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> _nt.Array[_ScalarT]: ...
@overload
def take(
    a: ArrayLike,
    indices: _nt.CoInteger_1nd,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> _nt.Array[Incomplete]: ...
@overload
def take(
    a: ArrayLike,
    indices: _nt.CoInteger_1nd,
    axis: CanIndex | None = None,
    *,
    out: _ArrayT,
    mode: _ModeKind = "raise",
) -> _ArrayT: ...
@overload
def take(
    a: ArrayLike,
    indices: _nt.CoInteger_0d,
    axis: CanIndex | None = None,
    out: None = None,
    mode: _ModeKind = "raise",
) -> Incomplete: ...

#
def put(
    a: _CanPut[_IndT_contra, _VT_contra, _RT_co], ind: _IndT_contra, v: _VT_contra, mode: _ModeKind = "raise"
) -> _RT_co: ...

#
@overload
def choose(a: _nt.CoInteger_nd, choices: ArrayLike, out: _ArrayT, mode: _ModeKind = "raise") -> _ArrayT: ...
@overload
def choose(a: _nt.CoInteger_0d, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> Incomplete: ...
@overload
def choose(
    a: _nt.CoInteger_1nd, choices: _nt._ToArray_nd[_ScalarT], out: None = None, mode: _ModeKind = "raise"
) -> _nt.Array[_ScalarT]: ...
@overload
def choose(
    a: _nt.CoInteger_1nd, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise"
) -> _nt.Array[Incomplete]: ...

#
@overload  # shape: index
def reshape(
    a: _nt._ToArray_nd[_ScalarT],
    /,
    shape: CanIndex,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # shape: _AnyShape
def reshape(
    a: _nt._ToArray_nd[_ScalarT],
    /,
    shape: _AnyShapeT,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: _nt._ToArray_nd[_ScalarT],
    /,
    shape: Sequence[CanIndex],
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # shape: index
def reshape(
    a: ArrayLike,
    /,
    shape: CanIndex,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array1D[Incomplete]: ...
@overload
def reshape(  # shape: _AnyShape
    a: ArrayLike,
    /,
    shape: _AnyShapeT,
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array[Incomplete, _AnyShapeT]: ...
@overload  # shape: Sequence[index]
def reshape(
    a: ArrayLike,
    /,
    shape: Sequence[CanIndex],
    order: _OrderACF = "C",
    *,
    newshape: None = None,
    copy: bool | None = None,
) -> _nt.Array[Incomplete]: ...
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
) -> _nt.Array[Incomplete]: ...

#
@overload
def swapaxes(a: _nt._ToArray_nd[_ScalarT], axis1: CanIndex, axis2: CanIndex) -> _nt.Array[_ScalarT]: ...
@overload
def swapaxes(a: ArrayLike, axis1: CanIndex, axis2: CanIndex) -> _nt.Array[Incomplete]: ...

#
@overload
def repeat(
    a: _nt._ToArray_nd[_ScalarT], repeats: _nt.CoInteger_nd, axis: CanIndex | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def repeat(a: ArrayLike, repeats: _nt.CoInteger_nd, axis: CanIndex | None = None) -> _nt.Array[Incomplete]: ...

#
@overload
def transpose(a: _nt._ToArray_nd[_ScalarT], axes: _ShapeLike | None = ...) -> _nt.Array[_ScalarT]: ...
@overload
def transpose(a: ArrayLike, axes: _ShapeLike | None = ...) -> _nt.Array[Incomplete]: ...

#
@overload
def matrix_transpose(x: _nt._ToArray_nd[_ScalarT], /) -> _nt.Array[_ScalarT]: ...
@overload
def matrix_transpose(x: ArrayLike, /) -> _nt.Array[Incomplete]: ...

#
@overload
def partition(
    a: _nt._ToArray_nd[_ScalarT],
    kth: _nt.ToInteger_nd,
    axis: CanIndex | None = None,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def partition(
    a: ArrayLike,
    kth: _nt.ToInteger_nd,
    axis: CanIndex | None = None,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> _nt.Array[Incomplete]: ...

#
def argpartition(
    a: ArrayLike,
    kth: _nt.ToInteger_nd,
    axis: CanIndex | None = -1,
    kind: _PartitionKind = "introselect",
    order: _Order | None = None,
) -> _nt.Array[np.intp]: ...

#
@overload  # known shape, known dtype, axis=<given>
def sort(
    a: _nt.CanLenArray[_ScalarT, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload  # 0d, known dtype, axis=None
def sort(
    a: _nt.CanArray0D[_ScalarT],
    axis: None,
    kind: CanIndex | None = -1,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=<given>
def sort(
    a: _nt._ToArray_nd[_ScalarT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, known dtype, axis=None
def sort(
    a: _nt._ToArray_nd[_ScalarT],
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # unknown shape, unknown dtype, axis=<given>
def sort(
    a: ArrayLike,
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array[Incomplete]: ...
@overload  # unknown shape, unknown dtype, axis=None
def sort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array1D[Any]: ...

#
@overload  # known shape
def argsort(
    a: _nt.CanLenArray[Any, _ShapeT],
    axis: CanIndex = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array[np.intp, _ShapeT]: ...
@overload  # 0d or 1d array-like
def argsort(
    a: _nt.ToGeneric_0d | _nt.ToGeneric_1ds,
    axis: CanIndex | None = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # axis=None
def argsort(
    a: ArrayLike,
    axis: None,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # fallback
def argsort(
    a: ArrayLike,
    axis: CanIndex | None = -1,
    kind: _SortKind | None = None,
    order: _Order | None = None,
    *,
    stable: bool | None = None,
) -> _nt.Array[np.intp]: ...

#
@overload  # 0d or 1d , keepdims=False
def argmax(
    a: _nt.ToGeneric_0d | _nt.ToGeneric_1ds,
    axis: CanIndex,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # axis=None, keepdims=False
def argmax(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # keepdims=True
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: None = None,
    *,
    keepdims: L[True],
) -> _nt.Array[np.intp]: ...
@overload  # out=<given> (positional)
def argmax(
    a: ArrayLike,
    axis: CanIndex | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload  # out=<given> (keyword)
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload  # fallback
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: _nt.Array | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload  # 0d or 1d , keepdims=False
def argmin(
    a: _nt.ToGeneric_0d | _nt.ToGeneric_1ds,
    axis: CanIndex,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # axis=None, keepdims=False
def argmin(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload  # keepdims=True
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: None = None,
    *,
    keepdims: L[True],
) -> _nt.Array[np.intp]: ...
@overload  # out=<given> (positional)
def argmin(
    a: ArrayLike,
    axis: CanIndex | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload  # out=<given> (keyword)
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload  # fallback
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    out: _nt.Array | None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...

#
@overload
def searchsorted(
    a: ArrayLike,
    v: _nt.ToGeneric_0d,
    side: _SortSide = "left",
    sorter: _nt.ToInteger_1d | None = None,
) -> np.intp: ...
@overload
def searchsorted(
    a: ArrayLike,
    v: _nt.ToGeneric_1nd,
    side: _SortSide = "left",
    sorter: _nt.ToInteger_1d | None = None,
) -> _nt.Array[np.intp]: ...

#
@overload
def resize(a: _nt._ToArray_nd[_ScalarT], new_shape: CanIndex) -> _nt.Array1D[_ScalarT]: ...
@overload
def resize(a: _nt._ToArray_nd[_ScalarT], new_shape: _AnyShapeT) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload
def resize(a: _nt._ToArray_nd[_ScalarT], new_shape: Sequence[CanIndex]) -> _nt.Array[_ScalarT]: ...
@overload
def resize(a: ArrayLike, new_shape: CanIndex) -> _nt.Array1D[Any]: ...
@overload
def resize(a: ArrayLike, new_shape: _AnyShapeT) -> _nt.Array[Any, _AnyShapeT]: ...
@overload
def resize(a: ArrayLike, new_shape: Sequence[CanIndex]) -> _nt.Array[Incomplete]: ...

#
@overload
def squeeze(a: _nt.CanArray0D[_ScalarT], axis: _ShapeLike | None = None) -> _nt.Array0D[_ScalarT]: ...
@overload
def squeeze(a: _nt._ToArray_nd[_ScalarT], axis: _ShapeLike | None = None) -> _nt.Array[_ScalarT]: ...
@overload
def squeeze(a: ArrayLike, axis: _ShapeLike | None = None) -> _nt.Array[Incomplete]: ...

#
@overload
def diagonal(
    a: _nt._ToArray_nd[_ScalarT], offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
) -> _nt.Array[_ScalarT]: ...
@overload
def diagonal(a: ArrayLike, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1) -> _nt.Array[Incomplete]: ...

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
def ravel(a: _nt._ToArray_nd[_ScalarT], order: _OrderKACF = "C") -> _nt.Array1D[_ScalarT]: ...  # type: ignore[overload-overlap]
@overload
def ravel(a: _nt.ToBytes_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.bytes_]: ...
@overload
def ravel(a: _nt.ToStr_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.str_]: ...
@overload
def ravel(a: _nt.ToBool_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.bool]: ...
@overload
def ravel(a: _nt.ToInt_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.intp]: ...
@overload
def ravel(a: _nt.ToFloat64_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.float64]: ...
@overload
def ravel(a: _nt.ToComplex128_nd, order: _OrderKACF = "C") -> _nt.Array1D[np.complex128]: ...
@overload
def ravel(a: ArrayLike, order: _OrderKACF = "C") -> _nt.Array1D[Any]: ...

#
def nonzero(a: _nt.ToGeneric_1nd) -> tuple[_nt.Array[np.int_], ...]: ...

#
@overload
def shape(a: _nt.HasInnerShape[_ShapeT]) -> _ShapeT: ...
@overload
def shape(a: np.ndarray[_ShapeT]) -> _ShapeT: ...
@overload
def shape(a: _nt.ToGeneric_0d) -> _nt.Shape0: ...
@overload
def shape(a: _nt.ToGeneric_1ds) -> _nt.Shape1: ...
@overload
def shape(a: _nt.ToGeneric_2ds) -> _nt.Shape2: ...
@overload
def shape(a: _nt.ToGeneric_3ds) -> _nt.Shape3: ...
@overload
def shape(a: _nt.ToGeneric_nd) -> _nt.Shape: ...

#
@overload
def compress(
    condition: _nt.ToBool_nd, a: _nt._ToArray_nd[_ScalarT], axis: CanIndex | None = None, out: None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: ArrayLike, axis: CanIndex | None = None, out: None = None
) -> _nt.Array[Incomplete]: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def clip(
    a: _ScalarT,
    a_min: _nt.CoComplex_nd | _NoValueType | None = ...,
    a_max: _nt.CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ScalarT: ...
@overload
def clip(
    a: _nt._ToArray_1nd[_ScalarT],
    a_min: _nt.CoComplex_nd | _NoValueType | None = ...,
    a_max: _nt.CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _nt.Array[_ScalarT]: ...
@overload
def clip(
    a: _nt.ToGeneric_1nd,
    a_min: _nt.CoComplex_nd | _NoValueType | None = ...,
    a_max: _nt.CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _nt.Array[Incomplete]: ...
@overload
def clip(
    a: _nt.ToGeneric_0d,
    a_min: _nt.CoComplex_nd | _NoValueType | None = ...,
    a_max: _nt.CoComplex_nd | _NoValueType | None = ...,
    out: None = None,
    *,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> Incomplete: ...
@overload
def clip(
    a: ArrayLike,
    a_min: _nt.CoComplex_nd | _NoValueType | None,
    a_max: _nt.CoComplex_nd | _NoValueType | None,
    out: _ArrayT,
    *,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: _nt.CoComplex_nd | _NoValueType | None = ...,
    a_max: _nt.CoComplex_nd | _NoValueType | None = ...,
    *,
    out: _ArrayT,
    min: _nt.CoComplex_nd | _NoValueType | None = ...,
    max: _nt.CoComplex_nd | _NoValueType | None = ...,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[UFuncKwargs],
) -> _ArrayT: ...

#
@overload
def sum(
    a: _nt._ToArray_nd[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: _nt._ToArray_nd[_ScalarT],
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT | _nt.Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT | _nt.Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT | _nt.Array[_ScalarT]: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> Incomplete: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def all(
    a: _nt.ToGeneric_1ds,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def all(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: None,
    keepdims: L[True, 1],
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _nt.Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    *,
    keepdims: L[True, 1],
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _nt.Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool | _nt.Array[np.bool]: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def all(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

# keep in sync with `all`
@overload
def any(
    a: _nt.ToGeneric_1ds,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def any(
    a: ArrayLike,
    axis: None = None,
    out: None = None,
    keepdims: L[False, 0] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: None,
    keepdims: L[True, 1],
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _nt.Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    *,
    keepdims: L[True, 1],
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _nt.Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    out: None = None,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.bool | _nt.Array[np.bool]: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None,
    out: _ArrayT,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def any(
    a: ArrayLike,
    axis: int | tuple[int, ...] | None = None,
    *,
    out: _ArrayT,
    keepdims: _nt.ToBool_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def cumsum(
    a: _nt._ToArray_nd[_ScalarT], axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def cumsum(
    a: ArrayLike, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[Incomplete]: ...
@overload
def cumsum(
    a: ArrayLike, axis: CanIndex | None = None, *, dtype: _DTypeLike[_ScalarT], out: None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def cumsum(
    a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
) -> _nt.Array[Incomplete]: ...
@overload
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

#
@overload
def cumulative_sum(
    x: _nt._ToArray_nd[_ScalarT],
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[_ScalarT]: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[Incomplete]: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[_ScalarT]: ...
@overload
def cumulative_sum(
    x: ArrayLike,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[Incomplete]: ...
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
def ptp(
    a: _nt._ToArray_nd[_ScalarT], axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...
) -> _ScalarT: ...
@overload
def ptp(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
) -> Incomplete: ...
@overload
def ptp(
    a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...

#
@overload
def amax(
    a: _nt._ToArray_nd[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> Incomplete: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amax(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

#
@overload
def amin(
    a: _nt._ToArray_nd[_ScalarT],
    axis: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> Incomplete: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def amin(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    initial: _nt.CoComplex_0d | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: `np.prod()``: For object arrays `initial` does not necessarily have to be a numerical scalar.
# The only requirement is that it is compatible with the `.__mul__()` method(s) of the passed array's elements.
# Note that the same situation holds for all wrappers around `np.ufunc.reduce`, e.g. `np.sum()` (`.__add__()`).
@overload
def prod(
    a: _nt.ToBool_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> np.int_: ...
@overload
def prod(
    a: _nt.ToUInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> np.uint64: ...
@overload
def prod(
    a: _nt.ToSInteger_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> np.int64: ...
@overload
def prod(
    a: _nt.ToFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> np.floating: ...
@overload
def prod(
    a: _nt.ToComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> np.complexfloating: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> Incomplete: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: _NoValueType | L[False] = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> _ScalarT: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    out: None = None,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> Incomplete: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> _ArrayT: ...
@overload
def prod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: DTypeLike | None = ...,
    *,
    out: _ArrayT,
    keepdims: _NoValueType | bool = ...,
    initial: _NoValueType | _nt.CoComplex_0d = ...,
    where: _NoValueType | _nt.ToBool_nd = ...,
) -> _ArrayT: ...

#
@overload
def cumprod(
    a: _nt.ToBool_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.int_]: ...
@overload
def cumprod(
    a: _nt.ToUInteger_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.uint64]: ...
@overload
def cumprod(
    a: _nt.ToSInteger_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.int64]: ...
@overload
def cumprod(
    a: _nt.ToFloating_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.floating]: ...
@overload
def cumprod(
    a: _nt.ToComplex_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.complexfloating]: ...
@overload
def cumprod(
    a: _nt.ToObject_nd, axis: CanIndex | None = None, dtype: None = None, out: None = None
) -> _nt.Array[np.object_]: ...
@overload
def cumprod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: CanIndex | None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def cumprod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: CanIndex | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def cumprod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
) -> _nt.Array[Incomplete]: ...
@overload
def cumprod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: CanIndex | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def cumprod(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def cumulative_prod(
    x: _nt.ToBool_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.int_]: ...
@overload
def cumulative_prod(
    x: _nt.ToUInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.uint64]: ...
@overload
def cumulative_prod(
    x: _nt.ToSInteger_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.int64]: ...
@overload
def cumulative_prod(
    x: _nt.ToFloating_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.floating]: ...
@overload
def cumulative_prod(
    x: _nt.ToComplex_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.complexfloating]: ...
@overload
def cumulative_prod(
    x: _nt.ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[np.object_]: ...
@overload
def cumulative_prod(
    x: _nt.CoComplex_nd | _nt.ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[_ScalarT]: ...
@overload
def cumulative_prod(
    x: _nt.CoComplex_nd | _nt.ToObject_nd,
    /,
    *,
    axis: CanIndex | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    include_initial: bool = False,
) -> _nt.Array[Incomplete]: ...
@overload
def cumulative_prod(
    x: _nt.CoComplex_nd | _nt.ToObject_nd,
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
def around(a: _nt.ToBool_0d, decimals: CanIndex = 0, out: None = None) -> np.float16: ...
@overload
def around(a: _nt.ToBool_1nd, decimals: CanIndex = 0, out: None = None) -> _nt.Array[np.float16]: ...
@overload
def around(a: _nt.CanArray0D[_NumberT], decimals: CanIndex = 0, out: None = None) -> _NumberT: ...
@overload
def around(a: _nt._ToArray_1nd[_NumberT], decimals: CanIndex = 0, out: None = None) -> _nt.Array[_NumberT]: ...
@overload
def around(a: _nt.JustInt, decimals: CanIndex = 0, out: None = None) -> np.intp: ...
@overload
def around(a: _nt.JustFloat, decimals: CanIndex = 0, out: None = None) -> np.float64: ...
@overload
def around(a: _nt.JustComplex, decimals: CanIndex = 0, out: None = None) -> np.complex128: ...
@overload
def around(a: _nt.CoComplex_nd, decimals: CanIndex, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: _nt.CoComplex_nd, decimals: CanIndex = 0, *, out: _ArrayT) -> _ArrayT: ...
@overload
def around(a: _nt.CoComplex_1nd, decimals: CanIndex = 0, out: _nt.Array | None = None) -> _nt.Array[Incomplete]: ...

#
@overload
def mean(
    a: _nt.CoFloating_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.floating: ...
@overload
def mean(
    a: _nt.ToComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.complexfloating: ...
@overload
def mean(
    a: _nt.ToTimeDelta_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> np.timedelta64: ...
@overload
def mean(
    a: _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> Any: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: L[False] | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT | _nt.Array[_ScalarT]: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    keepdims: bool | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ScalarT | _nt.Array[_ScalarT]: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def mean(
    a: _nt.CoComplex_nd | _nt.ToTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: _nt.Array | None = None,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
) -> Incomplete: ...

#
@overload
def std(
    a: _nt.CoComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def std(
    a: _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def std(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def std(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: _nt.Array | None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Incomplete: ...

#
@overload
def var(
    a: _nt.CoComplex_nd,
    axis: None = None,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> np.floating: ...
@overload
def var(
    a: _nt.ToObject_nd,
    axis: _ShapeLike | None = ...,
    dtype: None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Any: ...
@overload
def var(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    out: None = None,
    ddof: float = 0,
    keepdims: L[False] | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def var(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: _nt.Array | None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    *,
    where: _nt.ToBool_nd | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _nt.ToObject_nd | _NoValueType = ...,
    correction: float | _NoValueType = ...,
) -> Incomplete: ...

max = amax
min = amin
round = around
