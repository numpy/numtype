from collections.abc import Callable, Sequence
from typing import Any, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _DTypeLike,
    _SupportsArray,
    _SupportsArrayFunc,
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
_SCT = TypeVar("_SCT", bound=np.generic)

# The returned arrays dtype must be compatible with `np.equal`
_MaskFunc: TypeAlias = Callable[
    [NDArray[np.int_], _T],
    NDArray[np.number | np.bool | np.timedelta64 | np.datetime64 | np.object_],
]

@overload
def fliplr(m: _ArrayLike[_SCT]) -> NDArray[_SCT]: ...
@overload
def fliplr(m: ArrayLike) -> NDArray[Any]: ...
@overload
def flipud(m: _ArrayLike[_SCT]) -> NDArray[_SCT]: ...
@overload
def flipud(m: ArrayLike) -> NDArray[Any]: ...
@overload
def eye(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: None = ...,
    order: np._OrderCF = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def eye(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: _DTypeLike[_SCT] = ...,
    order: np._OrderCF = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def eye(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: DTypeLike = ...,
    order: np._OrderCF = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def diag(v: _ArrayLike[_SCT], k: int = ...) -> NDArray[_SCT]: ...
@overload
def diag(v: ArrayLike, k: int = ...) -> NDArray[Any]: ...
@overload
def diagflat(v: _ArrayLike[_SCT], k: int = ...) -> NDArray[_SCT]: ...
@overload
def diagflat(v: ArrayLike, k: int = ...) -> NDArray[Any]: ...
@overload
def tri(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: None = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def tri(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: _DTypeLike[_SCT] = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def tri(
    N: int,
    M: int | None = ...,
    k: int = ...,
    dtype: DTypeLike = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def tril(v: _ArrayLike[_SCT], k: int = ...) -> NDArray[_SCT]: ...
@overload
def tril(v: ArrayLike, k: int = ...) -> NDArray[Any]: ...
@overload
def triu(v: _ArrayLike[_SCT], k: int = ...) -> NDArray[_SCT]: ...
@overload
def triu(v: ArrayLike, k: int = ...) -> NDArray[Any]: ...
@overload
def vander(x: _ArrayLikeInt_co, N: int | None = ..., increasing: bool = ...) -> NDArray[np.signedinteger]: ...
@overload
def vander(x: _ArrayLikeFloat_co, N: int | None = ..., increasing: bool = ...) -> NDArray[np.floating]: ...
@overload
def vander(x: _ArrayLikeComplex_co, N: int | None = ..., increasing: bool = ...) -> NDArray[np.complexfloating]: ...
@overload
def vander(x: _ArrayLikeObject_co, N: int | None = ..., increasing: bool = ...) -> NDArray[np.object_]: ...

_Int_co: TypeAlias = np.integer | np.bool
_Float_co: TypeAlias = np.floating | _Int_co
_Number_co: TypeAlias = np.number | np.bool

_ArrayLike1D: TypeAlias = _SupportsArray[np.dtype[_SCT]] | Sequence[_SCT]
_ArrayLike2D: TypeAlias = _SupportsArray[np.dtype[_SCT]] | Sequence[_ArrayLike1D[_SCT]]

_ArrayLike1DInt_co: TypeAlias = _SupportsArray[np.dtype[_Int_co]] | Sequence[int | _Int_co]
_ArrayLike1DFloat_co: TypeAlias = _SupportsArray[np.dtype[_Float_co]] | Sequence[float | int | _Float_co]
_ArrayLike2DFloat_co: TypeAlias = _SupportsArray[np.dtype[_Float_co]] | Sequence[_ArrayLike1DFloat_co]
_ArrayLike1DNumber_co: TypeAlias = _SupportsArray[np.dtype[_Number_co]] | Sequence[int | float | complex | _Number_co]

_SCT_complex = TypeVar("_SCT_complex", bound=np.complexfloating)
_SCT_inexact = TypeVar("_SCT_inexact", bound=np.inexact)
_SCT_numeric = TypeVar("_SCT_numeric", bound=_Number_co)

@overload
def histogram2d(
    x: _ArrayLike1D[_SCT_complex],
    y: _ArrayLike1D[_SCT_complex | _Float_co],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_complex],
    NDArray[_SCT_complex],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1D[_SCT_complex | _Float_co],
    y: _ArrayLike1D[_SCT_complex],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_complex],
    NDArray[_SCT_complex],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1D[_SCT_inexact],
    y: _ArrayLike1D[_SCT_inexact | _Int_co],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_inexact],
    NDArray[_SCT_inexact],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1D[_SCT_inexact | _Int_co],
    y: _ArrayLike1D[_SCT_inexact],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_inexact],
    NDArray[_SCT_inexact],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DInt_co | Sequence[float | int],
    y: _ArrayLike1DInt_co | Sequence[float | int],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.float64],
    NDArray[np.float64],
]: ...
@overload
def histogram2d(
    x: Sequence[complex | float | int],
    y: Sequence[complex | float | int],
    bins: int | Sequence[int] = ...,
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.complex128 | np.float64],
    NDArray[np.complex128 | np.float64],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DNumber_co,
    y: _ArrayLike1DNumber_co,
    bins: _ArrayLike1D[_SCT_numeric] | Sequence[_ArrayLike1D[_SCT_numeric]],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_numeric],
    NDArray[_SCT_numeric],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1D[_SCT_inexact],
    y: _ArrayLike1D[_SCT_inexact],
    bins: Sequence[_ArrayLike1D[_SCT_numeric] | int],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_numeric | _SCT_inexact],
    NDArray[_SCT_numeric | _SCT_inexact],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DInt_co | Sequence[float | int],
    y: _ArrayLike1DInt_co | Sequence[float | int],
    bins: Sequence[_ArrayLike1D[_SCT_numeric] | int],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_numeric | np.float64],
    NDArray[_SCT_numeric | np.float64],
]: ...
@overload
def histogram2d(
    x: Sequence[complex | float | int],
    y: Sequence[complex | float | int],
    bins: Sequence[_ArrayLike1D[_SCT_numeric] | int],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[_SCT_numeric | np.complex128 | np.float64],
    NDArray[_SCT_numeric | np.complex128 | np.float64],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DNumber_co,
    y: _ArrayLike1DNumber_co,
    bins: Sequence[Sequence[bool]],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.bool],
    NDArray[np.bool],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DNumber_co,
    y: _ArrayLike1DNumber_co,
    bins: Sequence[Sequence[int | bool]],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.int_ | np.bool],
    NDArray[np.int_ | np.bool],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DNumber_co,
    y: _ArrayLike1DNumber_co,
    bins: Sequence[Sequence[float | int | bool]],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.float64 | np.int_ | np.bool],
    NDArray[np.float64 | np.int_ | np.bool],
]: ...
@overload
def histogram2d(
    x: _ArrayLike1DNumber_co,
    y: _ArrayLike1DNumber_co,
    bins: Sequence[Sequence[complex | float | int | bool]],
    range: _ArrayLike2DFloat_co | None = ...,
    density: bool | None = ...,
    weights: _ArrayLike1DFloat_co | None = ...,
) -> tuple[
    NDArray[np.float64],
    NDArray[np.complex128 | np.float64 | np.int_ | np.bool],
    NDArray[np.complex128 | np.float64 | np.int_ | np.bool],
]: ...

# NOTE: we're assuming/demanding here the `mask_func` returns
# an ndarray of shape `(n, n)`; otherwise there is the possibility
# of the output tuple having more or less than 2 elements
@overload
def mask_indices(
    n: int,
    mask_func: _MaskFunc[int],
    k: int = ...,
) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
@overload
def mask_indices(
    n: int,
    mask_func: _MaskFunc[_T],
    k: _T,
) -> tuple[NDArray[np.intp], NDArray[np.intp]]: ...
def tril_indices(
    n: int,
    k: int = ...,
    m: int | None = ...,
) -> tuple[NDArray[np.int_], NDArray[np.int_]]: ...
def tril_indices_from(
    arr: NDArray[Any],
    k: int = ...,
) -> tuple[NDArray[np.int_], NDArray[np.int_]]: ...
def triu_indices(
    n: int,
    k: int = ...,
    m: int | None = ...,
) -> tuple[NDArray[np.int_], NDArray[np.int_]]: ...
def triu_indices_from(
    arr: NDArray[Any],
    k: int = ...,
) -> tuple[NDArray[np.int_], NDArray[np.int_]]: ...
