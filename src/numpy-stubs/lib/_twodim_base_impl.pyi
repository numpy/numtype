from collections.abc import Callable, Sequence
from typing import Any, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    CoComplex_1d,
    CoFloat64_1d,
    Is,
    ToBool_1d,
    ToComplex_1d,
    ToFloat64_2d,
    ToFloating_1d,
    ToIntP_1d,
    ToInteger_1d,
    ToObject_1d,
    _ToArray1_1d,
)
from numpy import _OrderCF  # noqa: ICN003
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _DTypeLike,
    _SupportsArrayFunc as _CanArrayFunc,
)

__all__ = [
    "diag",
    "diagflat",
    "eye",
    "fliplr",
    "flipud",
    "histogram2d",
    "mask_indices",
    "tri",
    "tril",
    "tril_indices",
    "tril_indices_from",
    "triu",
    "triu_indices",
    "triu_indices_from",
    "vander",
]

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ComplexT = TypeVar("_ComplexT", bound=np.complexfloating)
_InexactT = TypeVar("_InexactT", bound=np.inexact)
_NumericT = TypeVar("_NumericT", bound=_CoComplex)

# The returned arrays dtype must be compatible with `np.equal`
_MaskFunc: TypeAlias = Callable[
    [NDArray[np.intp], _T],
    NDArray[np.number | np.bool | np.timedelta64 | np.datetime64 | np.object_],
]

_CoInt: TypeAlias = np.integer | np.bool
_CoFloat: TypeAlias = np.floating | _CoInt
_CoComplex: TypeAlias = np.number | np.bool

###

@overload
def fliplr(m: _ArrayLike[_ScalarT]) -> NDArray[_ScalarT]: ...
@overload
def fliplr(m: ArrayLike) -> NDArray[Any]: ...

#
@overload
def flipud(m: _ArrayLike[_ScalarT]) -> NDArray[_ScalarT]: ...
@overload
def flipud(m: ArrayLike) -> NDArray[Any]: ...

#
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: type[Is[float]] | None = ...,
    order: _OrderCF = "C",
    *,
    device: L["cpu"] | None = None,
    like: _CanArrayFunc | None = None,
) -> NDArray[np.float64]: ...
@overload
def eye(
    N: int,
    M: int | None,
    k: int,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: L["cpu"] | None = None,
    like: _CanArrayFunc | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    *,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    device: L["cpu"] | None = None,
    like: _CanArrayFunc | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: L["cpu"] | None = None,
    like: _CanArrayFunc | None = None,
) -> NDArray[Any]: ...

#
@overload
def diag(v: _ArrayLike[_ScalarT], k: int = 0) -> NDArray[_ScalarT]: ...
@overload
def diag(v: ArrayLike, k: int = 0) -> NDArray[Any]: ...

#
@overload
def diagflat(v: _ArrayLike[_ScalarT], k: int = 0) -> NDArray[_ScalarT]: ...
@overload
def diagflat(v: ArrayLike, k: int = 0) -> NDArray[Any]: ...

#
@overload
def tri(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: type[Is[float]] | None = ...,
    *,
    like: _CanArrayFunc | None = None,
) -> NDArray[np.float64]: ...
@overload
def tri(
    N: int,
    M: int | None,
    k: int,
    dtype: _DTypeLike[_ScalarT],
    *,
    like: _CanArrayFunc | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def tri(
    N: int,
    M: int | None = None,
    k: int = 0,
    *,
    dtype: _DTypeLike[_ScalarT],
    like: _CanArrayFunc | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def tri(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: DTypeLike = ...,
    *,
    like: _CanArrayFunc | None = None,
) -> NDArray[Any]: ...

#
@overload
def tril(v: _ArrayLike[_ScalarT], k: int = 0) -> NDArray[_ScalarT]: ...
@overload
def tril(v: ArrayLike, k: int = 0) -> NDArray[Any]: ...

#
@overload
def triu(v: _ArrayLike[_ScalarT], k: int = 0) -> NDArray[_ScalarT]: ...
@overload
def triu(v: ArrayLike, k: int = 0) -> NDArray[Any]: ...

#
@overload
def vander(x: ToBool_1d, N: int | None = None, increasing: bool = False) -> NDArray[np.intp]: ...
@overload
def vander(x: ToInteger_1d, N: int | None = None, increasing: bool = False) -> NDArray[np.signedinteger]: ...
@overload
def vander(x: ToFloating_1d, N: int | None = None, increasing: bool = False) -> NDArray[np.floating]: ...
@overload
def vander(x: ToComplex_1d, N: int | None = None, increasing: bool = False) -> NDArray[np.complexfloating]: ...
@overload
def vander(x: ToObject_1d, N: int | None = None, increasing: bool = False) -> NDArray[np.object_]: ...
@overload
def histogram2d(
    x: _ToArray1_1d[_ComplexT],
    y: _ToArray1_1d[_ComplexT | _CoFloat],
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_ComplexT], NDArray[_ComplexT]]: ...
@overload
def histogram2d(
    x: _ToArray1_1d[_ComplexT | _CoFloat],
    y: _ToArray1_1d[_ComplexT],
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_ComplexT], NDArray[_ComplexT]]: ...
@overload
def histogram2d(
    x: _ToArray1_1d[_InexactT],
    y: _ToArray1_1d[_InexactT | _CoInt],
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_InexactT], NDArray[_InexactT]]: ...
@overload
def histogram2d(
    x: _ToArray1_1d[_InexactT | _CoInt],
    y: _ToArray1_1d[_InexactT],
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_InexactT], NDArray[_InexactT]]: ...
@overload
def histogram2d(
    x: CoFloat64_1d,
    y: CoFloat64_1d,
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.float64], NDArray[np.float64]]: ...
@overload
def histogram2d(
    x: Sequence[complex],
    y: Sequence[complex],
    bins: int | Sequence[int] = 10,
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.complex128 | np.float64], NDArray[np.complex128 | np.float64]]: ...
@overload
def histogram2d(
    x: CoComplex_1d,
    y: CoComplex_1d,
    bins: _ToArray1_1d[_NumericT] | Sequence[_ToArray1_1d[_NumericT]],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_NumericT], NDArray[_NumericT]]: ...
@overload
def histogram2d(
    x: _ToArray1_1d[_InexactT],
    y: _ToArray1_1d[_InexactT],
    bins: Sequence[_ToArray1_1d[_NumericT] | int],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_NumericT | _InexactT], NDArray[_NumericT | _InexactT]]: ...
@overload
def histogram2d(
    x: ToIntP_1d | Sequence[float],
    y: ToIntP_1d | Sequence[float],
    bins: Sequence[_ToArray1_1d[_NumericT] | int],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[_NumericT | np.float64], NDArray[_NumericT | np.float64]]: ...
@overload
def histogram2d(
    x: Sequence[complex],
    y: Sequence[complex],
    bins: Sequence[_ToArray1_1d[_NumericT] | int],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[
    NDArray[np.float64],
    NDArray[_NumericT | np.complex128 | np.float64],
    NDArray[_NumericT | np.complex128 | np.float64],
]: ...
@overload
def histogram2d(
    x: CoComplex_1d,
    y: CoComplex_1d,
    bins: Sequence[Sequence[bool]],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.bool], NDArray[np.bool]]: ...
@overload
def histogram2d(
    x: CoComplex_1d,
    y: CoComplex_1d,
    bins: Sequence[Sequence[int]],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.intp | np.bool], NDArray[np.intp | np.bool]]: ...
@overload
def histogram2d(
    x: CoComplex_1d,
    y: CoComplex_1d,
    bins: Sequence[Sequence[float]],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[NDArray[np.float64], NDArray[np.float64 | np.intp | np.bool], NDArray[np.float64 | np.intp | np.bool]]: ...
@overload
def histogram2d(
    x: CoComplex_1d,
    y: CoComplex_1d,
    bins: Sequence[Sequence[complex]],
    range: ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: CoFloat64_1d | None = None,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.complex128 | np.float64 | np.intp | np.bool],
    NDArray[np.complex128 | np.float64 | np.intp | np.bool],
]: ...

# NOTE: we're assuming/demanding here the `mask_func` returns
# an ndarray of shape `(n, n)`; otherwise there is the possibility
# of the output tuple having more or less than 2 elements
@overload
def mask_indices(n: int, mask_func: _MaskFunc[int], k: int = 0) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
@overload
def mask_indices(n: int, mask_func: _MaskFunc[_T], k: _T) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...

#
def tril_indices(n: int, k: int = 0, m: int | None = None) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
def triu_indices(n: int, k: int = 0, m: int | None = None) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
def tril_indices_from(arr: NDArray[Any], k: int = 0) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
def triu_indices_from(arr: NDArray[Any], k: int = 0) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
