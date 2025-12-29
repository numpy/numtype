from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal as L, SupportsIndex, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _NestedSequence,
)

__all__ = ["histogram", "histogram_bin_edges", "histogramdd"]

###

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_InexactT = TypeVar("_InexactT", bound=np.inexact)
_InexactObjectT = TypeVar("_InexactObjectT", bound=np.inexact | np.object_)
_WeightsT = TypeVar("_WeightsT", bound=np.bool | np.number | np.timedelta64)

_BinKind: TypeAlias = L["auto", "fd", "doane", "scott", "stone", "rice", "sturges", "sqrt"]

_Range: TypeAlias = tuple[float, float]
_NestedList: TypeAlias = list[_T] | _NestedSequence[list[_T]]

_WeightsLike: TypeAlias = _ArrayLikeComplex_co | _ArrayLikeObject_co
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]
_HistogramResult: TypeAlias = tuple[_Array1D[_WeightsT], _Array1D[_ScalarT]]

###

# NOTE: The return type can also be complex or `object_`, not only floating like the docstring suggests.
@overload  # dtype +float64
def histogram_bin_edges(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    weights: _WeightsLike | None = None,
) -> _Array1D[np.float64]: ...
@overload  # dtype ~complex
def histogram_bin_edges(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    weights: _WeightsLike | None = None,
) -> _Array1D[np.complex128]: ...
@overload  # dtype known
def histogram_bin_edges(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    weights: _WeightsLike | None = None,
) -> _Array1D[_InexactObjectT]: ...
@overload  # dtype unknown
def histogram_bin_edges(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    weights: _WeightsLike | None = None,
) -> _Array1D[Incomplete]: ...

# There are 4 groups of 2 + 3 overloads (2 for density=True, 3 for density=False) = 20 in total
@overload  # a: +float64, density: True (keyword), weights: +float | None (default)
def histogram(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLikeFloat_co | None = None,
) -> _HistogramResult[np.float64, np.float64]: ...
@overload  # a: +float64, density: True (keyword), weights: +complex
def histogram(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLike[np.complexfloating] | _NestedList[complex],
) -> _HistogramResult[np.complex128, np.float64]: ...
@overload  # a: +float64, density: False (default), weights: ~int | None (default)
def histogram(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    weights: _NestedSequence[int] | None = None,
) -> _HistogramResult[np.intp, np.float64]: ...
@overload  # a: +float64, density: False (default), weights: known (keyword)
def histogram(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _ArrayLike[_WeightsT],
) -> _HistogramResult[_WeightsT, np.float64]: ...
@overload  # a: +float64, density: False (default), weights: unknown (keyword)
def histogram(
    a: _ArrayLikeInt_co | _NestedSequence[float],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _WeightsLike,
) -> _HistogramResult[Incomplete, np.float64]: ...
@overload  # a: ~complex, density: True (keyword), weights: +float | None (default)
def histogram(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLikeFloat_co | None = None,
) -> _HistogramResult[np.float64, np.complex128]: ...
@overload  # a: ~complex, density: True (keyword), weights: +complex
def histogram(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLike[np.complexfloating] | _NestedList[complex],
) -> _HistogramResult[np.complex128, np.complex128]: ...
@overload  # a: ~complex, density: False (default), weights: ~int | None (default)
def histogram(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    weights: _NestedSequence[int] | None = None,
) -> _HistogramResult[np.intp, np.complex128]: ...
@overload  # a: ~complex, density: False (default), weights: known (keyword)
def histogram(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _ArrayLike[_WeightsT],
) -> _HistogramResult[_WeightsT, np.complex128]: ...
@overload  # a: ~complex, density: False (default), weights: unknown (keyword)
def histogram(
    a: _NestedList[complex],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _WeightsLike,
) -> _HistogramResult[Incomplete, np.complex128]: ...
@overload  # a: known, density: True (keyword), weights: +float | None (default)
def histogram(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLikeFloat_co | None = None,
) -> _HistogramResult[np.float64, _InexactObjectT]: ...
@overload  # a: known, density: True (keyword), weights: +complex
def histogram(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLike[np.complexfloating] | _NestedList[complex],
) -> _HistogramResult[np.complex128, _InexactObjectT]: ...
@overload  # a: known, density: False (default), weights: ~int | None (default)
def histogram(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    weights: _NestedSequence[int] | None = None,
) -> _HistogramResult[np.intp, _InexactObjectT]: ...
@overload  # a: known, density: False (default), weights: known (keyword)
def histogram(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _ArrayLike[_WeightsT],
) -> _HistogramResult[_WeightsT, _InexactObjectT]: ...
@overload  # a: known, density: False (default), weights: unknown (keyword)
def histogram(
    a: _ArrayLike[_InexactObjectT],
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _WeightsLike,
) -> _HistogramResult[Incomplete, _InexactObjectT]: ...
@overload  # a: unknown, density: True (keyword), weights: +float | None (default)
def histogram(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLikeFloat_co | None = None,
) -> _HistogramResult[np.float64, Incomplete]: ...
@overload  # a: unknown, density: True (keyword), weights: +complex
def histogram(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    *,
    density: L[True],
    weights: _ArrayLike[np.complexfloating] | _NestedList[complex],
) -> _HistogramResult[np.complex128, Incomplete]: ...
@overload  # a: unknown, density: False (default), weights: int | None (default)
def histogram(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    weights: _NestedSequence[int] | None = None,
) -> _HistogramResult[np.intp, Incomplete]: ...
@overload  # a: unknown, density: False (default), weights: known (keyword)
def histogram(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _ArrayLike[_WeightsT],
) -> _HistogramResult[_WeightsT, Incomplete]: ...
@overload  # a: unknown, density: False (default), weights: unknown (keyword)
def histogram(
    a: _ArrayLikeComplex_co,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: _Range | None = None,
    density: L[False] | None = None,
    *,
    weights: _WeightsLike,
) -> _HistogramResult[Incomplete, Incomplete]: ...

# unlike `histogram`, `weights` must be safe-castable to f64
@overload  # dtype +float64
def histogramdd(
    sample: _ArrayLikeInt_co | _NestedSequence[float] | _ArrayLikeObject_co,
    bins: SupportsIndex | ArrayLike = 10,
    range: Sequence[_Range] | None = None,
    density: bool | None = None,
    weights: _ArrayLikeFloat64_co | None = None,
) -> tuple[NDArray[np.float64], tuple[_Array1D[np.float64], ...]]: ...
@overload  # dtype ~complex
def histogramdd(
    sample: _NestedList[complex],
    bins: SupportsIndex | ArrayLike = 10,
    range: Sequence[_Range] | None = None,
    density: bool | None = None,
    weights: _ArrayLikeFloat64_co | None = None,
) -> tuple[NDArray[np.float64], tuple[_Array1D[np.complex128], ...]]: ...
@overload  # dtype known
def histogramdd(
    sample: _ArrayLike[_InexactT],
    bins: SupportsIndex | ArrayLike = 10,
    range: Sequence[_Range] | None = None,
    density: bool | None = None,
    weights: _ArrayLikeFloat64_co | None = None,
) -> tuple[NDArray[np.float64], tuple[_Array1D[_InexactT], ...]]: ...
@overload  # dtype unknown
def histogramdd(
    sample: _ArrayLikeComplex_co,
    bins: SupportsIndex | ArrayLike = 10,
    range: Sequence[_Range] | None = None,
    density: bool | None = None,
    weights: _ArrayLikeFloat64_co | None = None,
) -> tuple[NDArray[np.float64], tuple[_Array1D[Any], ...]]: ...
