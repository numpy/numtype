from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    Concatenate,
    Literal as L,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import ParamSpec, TypeIs, TypeVar, deprecated

import numpy as np
from numpy import vectorize  # noqa: ICN003
from numpy._core.multiarray import bincount
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeDT64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
    _ComplexLike_co,
    _DTypeLike,
    _FloatLike_co,
    _NestedSequence,
    _NumberLike_co,
    _ScalarLike_co,
    _ShapeLike,
)

__all__ = [
    "angle",
    "append",
    "asarray_chkfinite",
    "average",
    "bartlett",
    "bincount",
    "blackman",
    "copy",
    "corrcoef",
    "cov",
    "delete",
    "diff",
    "digitize",
    "extract",
    "flip",
    "gradient",
    "hamming",
    "hanning",
    "i0",
    "insert",
    "interp",
    "iterable",
    "kaiser",
    "median",
    "meshgrid",
    "percentile",
    "piecewise",
    "place",
    "quantile",
    "rot90",
    "select",
    "sinc",
    "sort_complex",
    "trapezoid",
    "trapz",
    "trim_zeros",
    "unwrap",
    "vectorize",
]

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_Pss = ParamSpec("_Pss")
_SCT = TypeVar("_SCT", bound=np.generic)
_SCT_fcm = TypeVar("_SCT_fcm", bound=np.inexact | np.timedelta64)
_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])

_2Tuple: TypeAlias = tuple[_T, _T]
_MethodKind: TypeAlias = L[
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
    "lower",
    "higher",
    "midpoint",
    "nearest",
]

@type_check_only
class _SupportsRMulFloat(Protocol[_T_co]):
    def __rmul__(self, other: float, /) -> _T_co: ...

@type_check_only
class _TrimZerosSequence(Protocol[_T_co]):
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, key: int, /) -> object: ...
    @overload
    def __getitem__(self, key: slice, /) -> _T_co: ...

###

@overload
def rot90(m: _ArrayLike[_SCT], k: int = ..., axes: tuple[int, int] = ...) -> NDArray[_SCT]: ...
@overload
def rot90(m: ArrayLike, k: int = ..., axes: tuple[int, int] = ...) -> NDArray[Any]: ...

#
@overload
def flip(m: _SCT, axis: None = ...) -> _SCT: ...
@overload
def flip(m: _ScalarLike_co, axis: None = ...) -> Any: ...
@overload
def flip(m: _ArrayLike[_SCT], axis: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def flip(m: ArrayLike, axis: _ShapeLike | None = ...) -> NDArray[Any]: ...

#
def iterable(y: object) -> TypeIs[Iterable[Any]]: ...

#
@overload
def average(
    a: _ArrayLikeFloat_co,
    axis: None = ...,
    weights: _ArrayLikeFloat_co | None = ...,
    returned: L[False] = ...,
    keepdims: L[False] = ...,
) -> np.floating: ...
@overload
def average(
    a: _ArrayLikeComplex_co,
    axis: None = ...,
    weights: _ArrayLikeComplex_co | None = ...,
    returned: L[False] = ...,
    keepdims: L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: _ArrayLikeObject_co,
    axis: None = ...,
    weights: Any | None = ...,
    returned: L[False] = ...,
    keepdims: L[False] = ...,
) -> Any: ...
@overload
def average(
    a: _ArrayLikeFloat_co,
    axis: None = ...,
    weights: _ArrayLikeFloat_co | None = ...,
    returned: L[True] = ...,
    keepdims: L[False] = ...,
) -> _2Tuple[np.floating]: ...
@overload
def average(
    a: _ArrayLikeComplex_co,
    axis: None = ...,
    weights: _ArrayLikeComplex_co | None = ...,
    returned: L[True] = ...,
    keepdims: L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: _ArrayLikeObject_co,
    axis: None = ...,
    weights: Any | None = ...,
    returned: L[True] = ...,
    keepdims: L[False] = ...,
) -> _2Tuple[Any]: ...
@overload
def average(
    a: _ArrayLikeComplex_co | _ArrayLikeObject_co,
    axis: _ShapeLike | None = ...,
    weights: Any | None = ...,
    returned: L[False] = ...,
    keepdims: bool = ...,
) -> Any: ...
@overload
def average(
    a: _ArrayLikeComplex_co | _ArrayLikeObject_co,
    axis: _ShapeLike | None = ...,
    weights: Any | None = ...,
    returned: L[True] = ...,
    keepdims: bool = ...,
) -> _2Tuple[Any]: ...

#
@overload
def asarray_chkfinite(a: _ArrayLike[_SCT], dtype: None = ..., order: np._OrderKACF = ...) -> NDArray[_SCT]: ...
@overload
def asarray_chkfinite(a: object, dtype: None = ..., order: np._OrderKACF = ...) -> NDArray[Any]: ...
@overload
def asarray_chkfinite(a: Any, dtype: _DTypeLike[_SCT], order: np._OrderKACF = ...) -> NDArray[_SCT]: ...
@overload
def asarray_chkfinite(a: Any, dtype: DTypeLike, order: np._OrderKACF = ...) -> NDArray[Any]: ...

#
@overload
def piecewise(
    x: _ArrayLike[_SCT],
    condlist: _ArrayLike[np.bool_] | Sequence[_ArrayLikeBool_co],
    funclist: Sequence[Callable[Concatenate[NDArray[_SCT], _Pss], NDArray[_SCT | Any]] | _SCT | object],
    /,
    *args: _Pss.args,
    **kw: _Pss.kwargs,
) -> NDArray[_SCT]: ...
@overload
def piecewise(
    x: ArrayLike,
    condlist: _ArrayLike[np.bool_] | Sequence[_ArrayLikeBool_co],
    funclist: Sequence[Callable[Concatenate[NDArray[Any], _Pss], NDArray[Any]] | object],
    /,
    *args: _Pss.args,
    **kw: _Pss.kwargs,
) -> NDArray[Any]: ...

#
def select(condlist: Sequence[ArrayLike], choicelist: Sequence[ArrayLike], default: ArrayLike = ...) -> NDArray[Any]: ...

#
@overload
def copy(a: _ArrayT, order: np._OrderKACF, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: _ArrayT, order: np._OrderKACF = ..., *, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: _ArrayLike[_SCT], order: np._OrderKACF = ..., subok: L[False] = ...) -> NDArray[_SCT]: ...
@overload
def copy(a: ArrayLike, order: np._OrderKACF = ..., subok: L[False] = ...) -> NDArray[Any]: ...

#
def gradient(f: ArrayLike, *varargs: ArrayLike, axis: _ShapeLike | None = ..., edge_order: L[1, 2] = ...) -> Any: ...

#
@overload
def diff(a: _T, n: L[0], axis: SupportsIndex = ..., prepend: ArrayLike = ..., append: ArrayLike = ...) -> _T: ...
@overload
def diff(
    a: ArrayLike,
    n: int = ...,
    axis: SupportsIndex = ...,
    prepend: ArrayLike = ...,
    append: ArrayLike = ...,
) -> NDArray[Any]: ...

#
@overload  # float scalar
def interp(
    x: _FloatLike_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _FloatLike_co | None = None,
    right: _FloatLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> np.float64: ...
@overload  # float array
def interp(
    x: NDArray[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _FloatLike_co | None = None,
    right: _FloatLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.float64]: ...
@overload  # float scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _FloatLike_co | None = None,
    right: _FloatLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.float64] | np.float64: ...
@overload  # complex scalar
def interp(
    x: _FloatLike_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLike[np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> np.complex128: ...
@overload  # complex or float scalar
def interp(
    x: _FloatLike_co,
    xp: _ArrayLikeFloat_co,
    fp: Sequence[complex | np.ccomplexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> np.complex128 | np.float64: ...
@overload  # complex array
def interp(
    x: NDArray[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLike[np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.complex128]: ...
@overload  # complex or float array
def interp(
    x: NDArray[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: Sequence[complex | np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.complex128 | np.float64]: ...
@overload  # complex scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLike[np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.complex128] | np.complex128: ...
@overload  # complex or float scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> NDArray[np.complex128 | np.float64] | np.complex128 | np.float64: ...

#
@overload
def angle(z: _ComplexLike_co, deg: bool = ...) -> np.floating: ...
@overload
def angle(z: np.object_, deg: bool = ...) -> Any: ...
@overload
def angle(z: _ArrayLikeComplex_co, deg: bool = ...) -> NDArray[np.floating]: ...
@overload
def angle(z: _ArrayLikeObject_co, deg: bool = ...) -> NDArray[np.object_]: ...

#
@overload
def unwrap(
    p: _ArrayLikeFloat_co,
    discont: float | None = ...,
    axis: int = ...,
    *,
    period: float = ...,
) -> NDArray[np.floating]: ...
@overload
def unwrap(
    p: _ArrayLikeObject_co,
    discont: float | None = ...,
    axis: int = ...,
    *,
    period: float = ...,
) -> NDArray[np.object_]: ...

#
def sort_complex(a: ArrayLike) -> NDArray[np.complexfloating]: ...
def trim_zeros(filt: _TrimZerosSequence[_T], trim: L["f", "b", "fb", "bf"] = ...) -> _T: ...

#
@overload
def extract(condition: ArrayLike, arr: _ArrayLike[_SCT]) -> NDArray[_SCT]: ...
@overload
def extract(condition: ArrayLike, arr: ArrayLike) -> NDArray[Any]: ...

#
def place(arr: NDArray[Any], mask: ArrayLike, vals: Any) -> None: ...

#
@overload
def cov(
    m: _ArrayLikeFloat_co,
    y: _ArrayLikeFloat_co | None = ...,
    rowvar: bool = ...,
    bias: bool = ...,
    ddof: SupportsIndex | SupportsInt | None = ...,
    fweights: ArrayLike | None = ...,
    aweights: ArrayLike | None = ...,
    *,
    dtype: None = ...,
) -> NDArray[np.floating]: ...
@overload
def cov(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    bias: bool = ...,
    ddof: SupportsIndex | SupportsInt | None = ...,
    fweights: ArrayLike | None = ...,
    aweights: ArrayLike | None = ...,
    *,
    dtype: None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def cov(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    bias: bool = ...,
    ddof: SupportsIndex | SupportsInt | None = ...,
    fweights: ArrayLike | None = ...,
    aweights: ArrayLike | None = ...,
    *,
    dtype: _DTypeLike[_SCT],
) -> NDArray[_SCT]: ...
@overload
def cov(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    bias: bool = ...,
    ddof: SupportsIndex | SupportsInt | None = ...,
    fweights: ArrayLike | None = ...,
    aweights: ArrayLike | None = ...,
    *,
    dtype: DTypeLike,
) -> NDArray[Any]: ...

# NOTE `bias` and `ddof` have been deprecated
@overload
def corrcoef(
    m: _ArrayLikeFloat_co,
    y: _ArrayLikeFloat_co | None = ...,
    rowvar: bool = ...,
    *,
    dtype: None = ...,
) -> NDArray[np.floating]: ...
@overload
def corrcoef(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    *,
    dtype: None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def corrcoef(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    *,
    dtype: _DTypeLike[_SCT],
) -> NDArray[_SCT]: ...
@overload
def corrcoef(
    m: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co | None = ...,
    rowvar: bool = ...,
    *,
    dtype: DTypeLike,
) -> NDArray[Any]: ...

#
def blackman(M: _FloatLike_co) -> NDArray[np.floating]: ...
def bartlett(M: _FloatLike_co) -> NDArray[np.floating]: ...
def hanning(M: _FloatLike_co) -> NDArray[np.floating]: ...
def hamming(M: _FloatLike_co) -> NDArray[np.floating]: ...
def i0(x: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...
def kaiser(M: _FloatLike_co, beta: _FloatLike_co) -> NDArray[np.floating]: ...

#
@overload
def sinc(x: _FloatLike_co) -> np.floating: ...
@overload
def sinc(x: _ComplexLike_co) -> np.complexfloating: ...
@overload
def sinc(x: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...
@overload
def sinc(x: _ArrayLikeComplex_co) -> NDArray[np.complexfloating]: ...

#
@overload
def median(
    a: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    keepdims: L[False] = ...,
) -> np.floating: ...
@overload
def median(
    a: _ArrayLikeComplex_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    keepdims: L[False] = ...,
) -> np.complexfloating: ...
@overload
def median(
    a: _ArrayLikeTD64_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    keepdims: L[False] = ...,
) -> np.timedelta64: ...
@overload
def median(
    a: _ArrayLikeObject_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    keepdims: L[False] = ...,
) -> Any: ...
@overload
def median(
    a: _ArrayLikeFloat_co | _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    axis: _ShapeLike | None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    keepdims: bool = ...,
) -> Any: ...
@overload
def median(
    a: _ArrayLikeFloat_co | _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    axis: _ShapeLike | None,
    out: _ArrayT,
    /,
    overwrite_input: bool = ...,
    keepdims: bool = ...,
) -> _ArrayT: ...
@overload
def median(
    a: _ArrayLikeFloat_co | _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    axis: _ShapeLike | None = ...,
    *,
    out: _ArrayT,
    overwrite_input: bool = ...,
    keepdims: bool = ...,
) -> _ArrayT: ...

#
@overload
def percentile(
    a: _ArrayLikeFloat_co,
    q: _FloatLike_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> np.floating: ...
@overload
def percentile(
    a: _ArrayLikeComplex_co,
    q: _FloatLike_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> np.complexfloating: ...
@overload
def percentile(
    a: _ArrayLikeTD64_co,
    q: _FloatLike_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> np.timedelta64: ...
@overload
def percentile(
    a: _ArrayLikeDT64_co,
    q: _FloatLike_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> np.datetime64: ...
@overload
def percentile(
    a: _ArrayLikeObject_co,
    q: _FloatLike_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> Any: ...
@overload
def percentile(
    a: _ArrayLikeFloat_co,
    q: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.floating]: ...
@overload
def percentile(
    a: _ArrayLikeComplex_co,
    q: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def percentile(
    a: _ArrayLikeTD64_co,
    q: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.timedelta64]: ...
@overload
def percentile(
    a: _ArrayLikeDT64_co,
    q: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.datetime64]: ...
@overload
def percentile(
    a: _ArrayLikeObject_co,
    q: _ArrayLikeFloat_co,
    axis: None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: L[False] = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.object_]: ...
@overload
def percentile(
    a: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeDT64_co | _ArrayLikeObject_co,
    q: _ArrayLikeFloat_co,
    axis: _ShapeLike | None = ...,
    out: None = ...,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: bool = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> Any: ...
@overload
def percentile(
    a: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeDT64_co | _ArrayLikeObject_co,
    q: _ArrayLikeFloat_co,
    axis: _ShapeLike | None,
    out: _ArrayT,
    /,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: bool = ...,
    *,
    weights: _ArrayLikeFloat_co | None = ...,
) -> _ArrayT: ...
@overload
def percentile(
    a: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeDT64_co | _ArrayLikeObject_co,
    q: _ArrayLikeFloat_co,
    axis: _ShapeLike | None = ...,
    *,
    out: _ArrayT,
    overwrite_input: bool = ...,
    method: _MethodKind = ...,
    keepdims: bool = ...,
    weights: _ArrayLikeFloat_co | None = ...,
) -> _ArrayT: ...

# NOTE: Not an alias, but they do have identical signatures
# (that we can reuse)
quantile = percentile

@overload
def trapezoid(
    y: Sequence[_FloatLike_co],
    x: Sequence[_FloatLike_co] | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> np.float64: ...
@overload
def trapezoid(
    y: Sequence[_ComplexLike_co],
    x: Sequence[_ComplexLike_co] | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> np.complex128: ...
@overload
def trapezoid(
    y: _ArrayLike[np.bool_ | np.integer],
    x: _ArrayLike[np.bool_ | np.integer] | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> np.float64 | NDArray[np.float64]: ...
@overload
def trapezoid(
    y: _ArrayLikeObject_co,
    x: _ArrayLikeFloat_co | _ArrayLikeObject_co | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> float | NDArray[np.object_]: ...
@overload
def trapezoid(
    y: _ArrayLike[_SCT_fcm],
    x: _ArrayLike[_SCT_fcm] | _ArrayLikeInt_co | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> _SCT_fcm | NDArray[_SCT_fcm]: ...
@overload
def trapezoid(
    y: Sequence[_SupportsRMulFloat[_T]],
    x: Sequence[_SupportsRMulFloat[_T] | _T] | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> _T: ...
@overload
def trapezoid(
    y: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    x: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co | None = ...,
    dx: float = ...,
    axis: SupportsIndex = ...,
) -> np.inexact | np.timedelta64 | NDArray[np.inexact | np.timedelta64 | np.object_]: ...

#
@deprecated("Use 'trapezoid' instead")
def trapz(
    y: ArrayLike,
    x: ArrayLike | None = None,
    dx: float = 1.0,
    axis: int = -1,
) -> np.inexact | np.timedelta64 | NDArray[np.inexact | np.timedelta64 | np.object_]: ...

#
def meshgrid(*xi: ArrayLike, copy: bool = ..., sparse: bool = ..., indexing: L["xy", "ij"] = ...) -> tuple[NDArray[Any], ...]: ...

#
@overload
def delete(arr: _ArrayLike[_SCT], obj: slice | _ArrayLikeInt_co, axis: SupportsIndex | None = ...) -> NDArray[_SCT]: ...
@overload
def delete(arr: ArrayLike, obj: slice | _ArrayLikeInt_co, axis: SupportsIndex | None = ...) -> NDArray[Any]: ...

#
@overload
def insert(
    arr: _ArrayLike[_SCT],
    obj: slice | _ArrayLikeInt_co,
    values: ArrayLike,
    axis: SupportsIndex | None = ...,
) -> NDArray[_SCT]: ...
@overload
def insert(
    arr: ArrayLike,
    obj: slice | _ArrayLikeInt_co,
    values: ArrayLike,
    axis: SupportsIndex | None = ...,
) -> NDArray[Any]: ...

#
def append(arr: ArrayLike, values: ArrayLike, axis: SupportsIndex | None = ...) -> NDArray[Any]: ...

#
@overload
def digitize(x: _FloatLike_co, bins: _ArrayLikeFloat_co, right: bool = ...) -> np.int_: ...
@overload
def digitize(x: _ArrayLikeFloat_co, bins: _ArrayLikeFloat_co, right: bool = ...) -> NDArray[np.int_]: ...
