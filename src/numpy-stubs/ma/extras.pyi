from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Final, SupportsIndex, final, overload
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike, _DTypeLike, _ShapeLike
from numpy.lib._function_base_impl import average
from numpy.lib._index_tricks_impl import AxisConcatenator

from .core import dot

__all__ = [
    "apply_along_axis",
    "apply_over_axes",
    "atleast_1d",
    "atleast_2d",
    "atleast_3d",
    "average",
    "clump_masked",
    "clump_unmasked",
    "column_stack",
    "compress_cols",
    "compress_nd",
    "compress_rowcols",
    "compress_rows",
    "corrcoef",
    "count_masked",
    "cov",
    "diagflat",
    "dot",
    "dstack",
    "ediff1d",
    "flatnotmasked_contiguous",
    "flatnotmasked_edges",
    "hsplit",
    "hstack",
    "in1d",
    "intersect1d",
    "isin",
    "mask_cols",
    "mask_rowcols",
    "mask_rows",
    "masked_all",
    "masked_all_like",
    "median",
    "mr_",
    "ndenumerate",
    "notmasked_contiguous",
    "notmasked_edges",
    "polyfit",
    "row_stack",
    "setdiff1d",
    "setxor1d",
    "stack",
    "union1d",
    "unique",
    "vander",
    "vstack",
]

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_SCT0 = TypeVar("_SCT0", bound=np.generic)
_SCT1 = TypeVar("_SCT1", bound=np.generic)

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array[Any])

_Array1T = TypeVar("_Array1T", bound=_nt.MArray[Any, _nt.Shape1N])
_Array1T0 = TypeVar("_Array1T0", bound=_nt.MArray[Any, _nt.Shape1N])
_Array1T1 = TypeVar("_Array1T1", bound=_nt.MArray[Any, _nt.Shape1N])

_Array2T = TypeVar("_Array2T", bound=_nt.MArray[Any, _nt.Shape2N])
_Array2T0 = TypeVar("_Array2T0", bound=_nt.MArray[Any, _nt.Shape2N])
_Array2T1 = TypeVar("_Array2T1", bound=_nt.MArray[Any, _nt.Shape2N])

_Array3T = TypeVar("_Array3T", bound=_nt.MArray[Any, _nt.Shape3N])
_Array3T0 = TypeVar("_Array3T0", bound=_nt.MArray[Any, _nt.Shape3N])
_Array3T1 = TypeVar("_Array3T1", bound=_nt.MArray[Any, _nt.Shape3N])

###

class MAxisConcatenator(AxisConcatenator):
    __slots__ = ()

    @staticmethod
    @override
    def concatenate(arrays: Incomplete, axis: int = 0) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @classmethod
    @override
    def makemat(cls, arr: Incomplete) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleVariableOverride]

@final
class mr_class(MAxisConcatenator):
    __slots__ = ()

    def __init__(self) -> None: ...

def count_masked(arr: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def masked_all(shape: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def masked_all_like(arr: Incomplete) -> Incomplete: ...
def apply_along_axis(
    func1d: Incomplete, axis: Incomplete, arr: Incomplete, *args: Incomplete, **kwargs: Incomplete
) -> Incomplete: ...
def apply_over_axes(func: Incomplete, a: Incomplete, axes: Incomplete) -> Incomplete: ...
def median(
    a: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    overwrite_input: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...
def compress_nd(x: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def compress_rowcols(x: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def compress_rows(a: Incomplete) -> Incomplete: ...
def compress_cols(a: Incomplete) -> Incomplete: ...
def mask_rows(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def mask_cols(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def ediff1d(arr: Incomplete, to_end: Incomplete = ..., to_begin: Incomplete = ...) -> Incomplete: ...
def unique(ar1: Incomplete, return_index: Incomplete = ..., return_inverse: Incomplete = ...) -> Incomplete: ...
def intersect1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def setxor1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def in1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ..., invert: Incomplete = ...) -> Incomplete: ...
def isin(
    element: Incomplete, test_elements: Incomplete, assume_unique: Incomplete = ..., invert: Incomplete = ...
) -> Incomplete: ...
def union1d(ar1: Incomplete, ar2: Incomplete) -> Incomplete: ...
def setdiff1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def cov(
    x: Incomplete,
    y: Incomplete = ...,
    rowvar: Incomplete = ...,
    bias: Incomplete = ...,
    allow_masked: Incomplete = ...,
    ddof: Incomplete = ...,
) -> Incomplete: ...
def corrcoef(x: Incomplete, y: Incomplete = None, rowvar: bool = True, allow_masked: bool = True) -> Incomplete: ...
def ndenumerate(a: Incomplete, compressed: Incomplete = ...) -> Incomplete: ...
def flatnotmasked_edges(a: Incomplete) -> Incomplete: ...
def notmasked_edges(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def flatnotmasked_contiguous(a: Incomplete) -> Incomplete: ...
def notmasked_contiguous(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def clump_unmasked(a: Incomplete) -> Incomplete: ...
def clump_masked(a: Incomplete) -> Incomplete: ...
def vander(x: Incomplete, n: Incomplete = ...) -> Incomplete: ...
def polyfit(
    x: Incomplete,
    y: Incomplete,
    deg: Incomplete,
    rcond: Incomplete = ...,
    full: Incomplete = ...,
    w: Incomplete = ...,
    cov: Incomplete = ...,
) -> Incomplete: ...

mr_: Final[mr_class] = ...

# keep in sync with `numpy._core.shape_base.atleast_1d`
@overload
def atleast_1d(a0: _Array1T, /) -> _Array1T: ...
@overload
def atleast_1d(a0: _Array1T0, a1: _Array1T1, /) -> tuple[_Array1T0, _Array1T1]: ...
@overload
def atleast_1d(a0: _Array1T, a1: _Array1T, /, *arys: _Array1T) -> tuple[_Array1T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_1d(a0: _ArrayLike[_ScalarT], /) -> _nt.MArray[_ScalarT]: ...
@overload
def atleast_1d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[_nt.MArray[_SCT0], _nt.MArray[_SCT1]]: ...
@overload
def atleast_1d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[_nt.MArray[_ScalarT], ...]: ...
@overload
def atleast_1d(a0: ArrayLike, /) -> _nt.MArray[Any]: ...
@overload
def atleast_1d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[_nt.MArray[Any], _nt.MArray[Any]]: ...
@overload
def atleast_1d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[_nt.MArray[Any], ...]: ...

# keep in sync with `numpy._core.shape_base.atleast_2d`
@overload
def atleast_2d(a0: _Array2T, /) -> _Array2T: ...
@overload
def atleast_2d(a0: _Array2T0, a1: _Array2T1, /) -> tuple[_Array2T0, _Array2T1]: ...
@overload
def atleast_2d(a0: _Array2T, a1: _Array2T, /, *arys: _Array2T) -> tuple[_Array2T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_2d(a0: _ArrayLike[_ScalarT], /) -> _nt.MArray[_ScalarT]: ...
@overload
def atleast_2d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[_nt.MArray[_SCT0], _nt.MArray[_SCT1]]: ...
@overload
def atleast_2d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[_nt.MArray[_ScalarT], ...]: ...
@overload
def atleast_2d(a0: ArrayLike, /) -> _nt.MArray[Any]: ...
@overload
def atleast_2d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[_nt.MArray[Any], _nt.MArray[Any]]: ...
@overload
def atleast_2d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[_nt.MArray[Any], ...]: ...

# keep in sync with `numpy._core.shape_base.atleast_2d`
@overload
def atleast_3d(a0: _Array3T, /) -> _Array3T: ...
@overload
def atleast_3d(a0: _Array3T0, a1: _Array3T1, /) -> tuple[_Array3T0, _Array3T1]: ...
@overload
def atleast_3d(a0: _Array3T, a1: _Array3T, /, *arys: _Array3T) -> tuple[_Array3T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_3d(a0: _ArrayLike[_ScalarT], /) -> _nt.MArray[_ScalarT]: ...
@overload
def atleast_3d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[_nt.MArray[_SCT0], _nt.MArray[_SCT1]]: ...
@overload
def atleast_3d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[_nt.MArray[_ScalarT], ...]: ...
@overload
def atleast_3d(a0: ArrayLike, /) -> _nt.MArray[Any]: ...
@overload
def atleast_3d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[_nt.MArray[Any], _nt.MArray[Any]]: ...
@overload
def atleast_3d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[_nt.MArray[Any], ...]: ...

# keep in sync with `numpy._core.shape_base.vstack`
@overload
def vstack(
    tup: Sequence[_ArrayLike[_ScalarT]], *, dtype: None = None, casting: np._CastingKind = "same_kind"
) -> _nt.MArray[_ScalarT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike], *, dtype: _DTypeLike[_ScalarT], casting: np._CastingKind = "same_kind"
) -> _nt.MArray[_ScalarT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike], *, dtype: DTypeLike | None = None, casting: np._CastingKind = "same_kind"
) -> _nt.MArray[Any]: ...

row_stack = vstack

# keep in sync with `numpy._core.shape_base.hstack`
@overload
def hstack(
    tup: Sequence[_ArrayLike[_ScalarT]], *, dtype: None = None, casting: np._CastingKind = "same_kind"
) -> _nt.MArray[_ScalarT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike], *, dtype: _DTypeLike[_ScalarT], casting: np._CastingKind = "same_kind"
) -> _nt.MArray[_ScalarT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike], *, dtype: DTypeLike | None = None, casting: np._CastingKind = "same_kind"
) -> _nt.MArray[Any]: ...

# keep in sync with `numpy._core.shape_base_impl.column_stack`
@overload
def column_stack(tup: Sequence[_ArrayLike[_ScalarT]]) -> _nt.MArray[_ScalarT]: ...
@overload
def column_stack(tup: Sequence[ArrayLike]) -> _nt.MArray[Incomplete]: ...

# keep in sync with `numpy._core.shape_base_impl.dstack`
@overload
def dstack(tup: Sequence[_ArrayLike[_ScalarT]]) -> _nt.MArray[_ScalarT]: ...
@overload
def dstack(tup: Sequence[ArrayLike]) -> _nt.MArray[Incomplete]: ...

# keep in sync with `numpy._core.shape_base.stack`
@overload
def stack(
    arrays: Sequence[_ArrayLike[_ScalarT]],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: np._CastingKind = "same_kind",
) -> _nt.Array[_ScalarT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: np._CastingKind = "same_kind",
) -> _nt.Array[_ScalarT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> _nt.Array[Any]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex,
    out: _ArrayT,
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    *,
    out: _ArrayT,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> _ArrayT: ...

# keep in sync with `numpy._core.shape_base_impl.hsplit`
@overload
def hsplit(ary: _ArrayLike[_ScalarT], indices_or_sections: _ShapeLike) -> list[_nt.MArray[_ScalarT]]: ...
@overload
def hsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[_nt.MArray[Incomplete]]: ...

# keep in sync with `numpy._core.twodim_base_impl.hsplit`
@overload
def diagflat(v: _ArrayLike[_ScalarT], k: int = 0) -> _nt.MArray[_ScalarT]: ...
@overload
def diagflat(v: ArrayLike, k: int = 0) -> _nt.MArray[Incomplete]: ...
def mask_rowcols(a: Incomplete, axis: Incomplete | None = None) -> _nt.MArray[Incomplete]: ...
