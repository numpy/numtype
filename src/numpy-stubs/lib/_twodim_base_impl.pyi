from collections.abc import Callable, Sequence
from typing import Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy import _OrderCF  # noqa: ICN003
from numpy._typing import _SupportsArrayFunc as _Like

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
_CoComplexT = TypeVar("_CoComplexT", bound=_nt.co_complex)
_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)

# The returned arrays dtype must be compatible with `np.equal`
_Device: TypeAlias = L["cpu"]
_MaskFunc: TypeAlias = Callable[
    [_nt.Array[np.intp], _T], _nt.Array[_nt.co_complex | np.datetime64 | np.timedelta64 | np.object_]
]

_Sequence01D: TypeAlias = _T | Sequence[_T]
_Indices2D: TypeAlias = tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]]
_Histogram2D: TypeAlias = tuple[_nt.Array2D[np.float64], _nt.Array1D[_ScalarT], _nt.Array1D[_ScalarT]]

###

@overload
def fliplr(m: _ArrayT) -> _ArrayT: ...
@overload
def fliplr(m: _nt._ToArray_nd[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def fliplr(m: _nt.ToGeneric_nd) -> _nt.Array: ...

#
@overload
def flipud(m: _ArrayT) -> _ArrayT: ...
@overload
def flipud(m: _nt._ToArray_nd[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def flipud(m: _nt.ToGeneric_nd) -> _nt.Array: ...

#
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: _nt.ToDTypeFloat64 | None = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _Like | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def eye(
    N: int,
    M: int | None,
    k: int,
    dtype: _nt._ToDType[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _Like | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    *,
    dtype: _nt._ToDType[_ScalarT],
    order: _OrderCF = "C",
    device: _Device | None = None,
    like: _Like | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def eye(
    N: int,
    M: int | None = None,
    k: int = 0,
    dtype: _nt.ToDType = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _Like | None = None,
) -> _nt.Array: ...

#
@overload
def diag(v: _nt._ToArray_nd[_ScalarT], k: int = 0) -> _nt.Array[_ScalarT]: ...
@overload
def diag(v: _nt.ToGeneric_nd, k: int = 0) -> _nt.Array: ...

#
@overload
def diagflat(v: _nt._ToArray_nd[_ScalarT], k: int = 0) -> _nt.Array[_ScalarT]: ...
@overload
def diagflat(v: _nt.ToGeneric_nd, k: int = 0) -> _nt.Array: ...

#
@overload
def tri(
    N: int, M: int | None = None, k: int = 0, dtype: _nt.ToDTypeFloat64 | None = ..., *, like: _Like | None = None
) -> _nt.Array[np.float64]: ...
@overload
def tri(
    N: int, M: int | None, k: int, dtype: _nt._ToDType[_ScalarT], *, like: _Like | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def tri(
    N: int, M: int | None = None, k: int = 0, *, dtype: _nt._ToDType[_ScalarT], like: _Like | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def tri(
    N: int, M: int | None = None, k: int = 0, dtype: _nt.ToDType = ..., *, like: _Like | None = None
) -> _nt.Array: ...

#
@overload
def tril(m: _nt.ToBool_1nd, k: int = 0) -> _nt.Array[np.bool]: ...
@overload
def tril(m: _nt._ToArray_1nd[_ScalarT], k: int = 0) -> _nt.Array[_ScalarT]: ...
@overload
def tril(m: _nt.ToInt_1nd, k: int = 0) -> _nt.Array[np.intp]: ...
@overload
def tril(m: _nt.ToFloat64_1nd, k: int = 0) -> _nt.Array[np.float64]: ...
@overload
def tril(m: _nt.ToComplex128_1nd, k: int = 0) -> _nt.Array[np.complex128]: ...
@overload
def tril(m: _nt.ToBytes_1nd, k: int = 0) -> _nt.Array[np.bytes_]: ...
@overload
def tril(m: _nt.ToStr_1nd, k: int = 0) -> _nt.Array[np.str_]: ...
@overload
def tril(m: _nt.ToGeneric_nd, k: int = 0) -> _nt.Array: ...

#
@overload
def triu(m: _nt.ToBool_1nd, k: int = 0) -> _nt.Array[np.bool]: ...
@overload
def triu(m: _nt._ToArray_1nd[_ScalarT], k: int = 0) -> _nt.Array[_ScalarT]: ...
@overload
def triu(m: _nt.ToInt_1nd, k: int = 0) -> _nt.Array[np.intp]: ...
@overload
def triu(m: _nt.ToFloat64_1nd, k: int = 0) -> _nt.Array[np.float64]: ...
@overload
def triu(m: _nt.ToComplex128_1nd, k: int = 0) -> _nt.Array[np.complex128]: ...
@overload
def triu(m: _nt.ToBytes_1nd, k: int = 0) -> _nt.Array[np.bytes_]: ...
@overload
def triu(m: _nt.ToStr_1nd, k: int = 0) -> _nt.Array[np.str_]: ...
@overload
def triu(m: _nt.ToGeneric_nd, k: int = 0) -> _nt.Array: ...

#
@overload
def vander(x: _nt.ToBool_1d, N: int | None = None, increasing: bool = False) -> _nt.Array[np.intp]: ...
@overload
def vander(x: _nt.ToInteger_1d, N: int | None = None, increasing: bool = False) -> _nt.Array[np.signedinteger]: ...
@overload
def vander(x: _nt.ToFloating_1d, N: int | None = None, increasing: bool = False) -> _nt.Array[np.floating]: ...
@overload
def vander(x: _nt.ToComplex_1d, N: int | None = None, increasing: bool = False) -> _nt.Array[np.complexfloating]: ...
@overload
def vander(x: _nt.ToObject_1d, N: int | None = None, increasing: bool = False) -> _nt.Array[np.object_]: ...

#
@overload
def histogram2d(
    x: _nt._ToArray_1d[_ComplexT],
    y: _nt._ToArray_1d[_ComplexT | _nt.co_float],
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_ComplexT]: ...
@overload
def histogram2d(
    x: _nt._ToArray_1d[_ComplexT | _nt.co_float],
    y: _nt._ToArray_1d[_ComplexT],
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_ComplexT]: ...
@overload
def histogram2d(
    x: _nt._ToArray_1d[_InexactT],
    y: _nt._ToArray_1d[_InexactT | _nt.co_integer],
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_InexactT]: ...
@overload
def histogram2d(
    x: _nt._ToArray_1d[_InexactT | _nt.co_integer],
    y: _nt._ToArray_1d[_InexactT],
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_InexactT]: ...
@overload
def histogram2d(
    x: _nt.CoFloat64_1d,
    y: _nt.CoFloat64_1d,
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[np.float64]: ...
@overload
def histogram2d(
    x: Sequence[complex],
    y: Sequence[complex],
    bins: _Sequence01D[int] = 10,
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_nt.inexact64]: ...
@overload
def histogram2d(
    x: _nt.CoComplex_1d,
    y: _nt.CoComplex_1d,
    bins: _Sequence01D[_nt._ToArray_1d[_CoComplexT]],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_CoComplexT]: ...
@overload
def histogram2d(
    x: _nt._ToArray_1d[_InexactT],
    y: _nt._ToArray_1d[_InexactT],
    bins: Sequence[_nt._ToArray_1d[_CoComplexT] | int],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_CoComplexT | _InexactT]: ...
@overload
def histogram2d(
    x: _nt.ToInt_1d | Sequence[float],
    y: _nt.ToInt_1d | Sequence[float],
    bins: Sequence[_nt._ToArray_1d[_CoComplexT] | int],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_CoComplexT | np.float64]: ...
@overload
def histogram2d(
    x: Sequence[complex],
    y: Sequence[complex],
    bins: Sequence[_nt._ToArray_1d[_CoComplexT] | int],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[_CoComplexT | _nt.inexact64]: ...
@overload
def histogram2d(
    x: _nt.CoComplex_1d,
    y: _nt.CoComplex_1d,
    bins: _nt.Sequence2D[bool],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[np.bool]: ...
@overload
def histogram2d(
    x: _nt.CoComplex_1d,
    y: _nt.CoComplex_1d,
    bins: _nt.Sequence2D[_nt.JustInt],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[np.intp]: ...
@overload
def histogram2d(
    x: _nt.CoComplex_1d,
    y: _nt.CoComplex_1d,
    bins: _nt.Sequence2D[_nt.JustFloat],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[np.float64]: ...
@overload
def histogram2d(
    x: _nt.CoComplex_1d,
    y: _nt.CoComplex_1d,
    bins: _nt.Sequence2D[_nt.JustComplex],
    range: _nt.ToFloat64_2d | None = None,
    density: bool | None = None,
    weights: _nt.CoFloat64_1d | None = None,
) -> _Histogram2D[np.complex128]: ...

# NOTE: we're assuming/demanding here the `mask_func` returns
# an ndarray of shape `(n, n)`; otherwise there is the possibility
# of the output tuple having more or less than 2 elements
@overload
def mask_indices(n: int, mask_func: _MaskFunc[int], k: int = 0) -> _Indices2D: ...
@overload
def mask_indices(n: int, mask_func: _MaskFunc[_T], k: _T) -> _Indices2D: ...

#
def tril_indices(n: int, k: int = 0, m: int | None = None) -> _Indices2D: ...
def triu_indices(n: int, k: int = 0, m: int | None = None) -> _Indices2D: ...

#
def tril_indices_from(arr: _nt.Array, k: int = 0) -> _Indices2D: ...
def triu_indices_from(arr: _nt.Array, k: int = 0) -> _Indices2D: ...
