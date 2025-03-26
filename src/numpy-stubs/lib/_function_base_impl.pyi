import datetime as dt
from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    Concatenate,
    Final,
    Literal as L,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import LiteralString, ParamSpec, TypeIs, TypeVar, deprecated

import numpy as np
from _numtype import (
    Array,
    Array1D,
    Array2D,
    Array3D,
    Array4D,
    CanLenArray,
    CoComplex_0d,
    CoComplex_1ds,
    CoComplex_1nd,
    CoComplex_2nd,
    CoComplex_nd,
    CoDateTime_nd,
    CoFloat64_0d,
    CoFloat64_nd,
    CoFloating_0d,
    CoFloating_1d,
    CoFloating_1ds,
    CoFloating_1nd,
    CoFloating_2nd,
    CoFloating_nd,
    CoInteger_nd,
    CoTimeDelta_1ds,
    CoTimeDelta_1nd,
    CoTimeDelta_2nd,
    CoTimeDelta_nd,
    ToBool_nd,
    ToBytes_nd,
    ToComplex128_nd,
    ToComplex_0d,
    ToComplex_1ds,
    ToComplex_1nd,
    ToComplex_2nd,
    ToComplex_nd,
    ToDateTime_nd,
    ToFloat64_0d,
    ToFloat64_nd,
    ToFloating_0d,
    ToGeneric_0d,
    ToGeneric_1nd,
    ToIntP_nd,
    ToObject_1nd,
    ToObject_nd,
    ToStr_nd,
    ToTimeDelta_1ds,
    ToTimeDelta_1nd,
    ToTimeDelta_2nd,
    ToTimeDelta_nd,
    _ToArray2_1ds,
    _ToArray2_1nd,
    _ToArray2_2nd,
    _ToArray_1nd,
)
from numpy import _OrderKACF  # noqa: ICN003
from numpy._core.multiarray import bincount
from numpy._globals import _NoValueType
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    _ArrayLike,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
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

###

_Tss = ParamSpec("_Tss")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_ArrayT = TypeVar("_ArrayT", bound=Array)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT1 = TypeVar("_ScalarT1", bound=np.generic)
_ScalarT2 = TypeVar("_ScalarT2", bound=np.generic)
_NumberT = TypeVar("_NumberT", bound=np.number)

_2Tuple: TypeAlias = tuple[_T, _T]
_ToInt: TypeAlias = SupportsIndex | SupportsInt
_PercentileMethod: TypeAlias = L[
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
_Indexing: TypeAlias = L["xy", "ij"]

@type_check_only
class _CanRMulFloat(Protocol[_T_co]):
    def __rmul__(self, other: float, /) -> _T_co: ...

@type_check_only
class _CanLenAndGetSlice(Protocol[_T_co]):
    def __len__(self) -> int: ...
    def __getitem__(self, key: slice, /) -> _T_co: ...

###

class vectorize:
    __doc__: str | None
    pyfunc: Callable[..., Any]
    cache: Final[bool]
    signature: Final[LiteralString | None]
    otypes: Final[LiteralString | None]
    excluded: Final[set[int | str]]

    #
    def __init__(
        self,
        /,
        pyfunc: Callable[..., Any] | _NoValueType = ...,
        otypes: str | Iterable[DTypeLike] | None = None,
        doc: str | None = None,
        excluded: Iterable[int | str] | None = None,
        cache: bool = False,
        signature: str | None = None,
    ) -> None: ...

    #
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any: ...

###

#
@overload
def rot90(m: _ArrayLike[_ScalarT], k: int = 1, axes: tuple[int, int] = (0, 1)) -> Array[_ScalarT]: ...
@overload
def rot90(m: ArrayLike, k: int = 1, axes: tuple[int, int] = (0, 1)) -> Array: ...

#
@overload
def flip(m: _ScalarT, axis: None = None) -> _ScalarT: ...
@overload
def flip(m: _ScalarLike_co, axis: None = None) -> Any: ...
@overload
def flip(m: _ToArray_1nd[_ScalarT], axis: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def flip(m: ToGeneric_1nd, axis: _ShapeLike | None = None) -> Array: ...

#
def iterable(y: object) -> TypeIs[Iterable[Any]]: ...

#
@overload
def average(
    a: ToFloat64_nd | CoInteger_nd,
    axis: None = None,
    weights: CoFloat64_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.float64: ...
@overload
def average(
    a: ToFloat64_nd | CoInteger_nd,
    axis: None,
    weights: CoFloat64_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType = ...,
) -> _2Tuple[np.float64]: ...
@overload
def average(
    a: ToFloat64_nd | CoInteger_nd,
    axis: None = None,
    weights: CoFloat64_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.float64]: ...
@overload
def average(
    a: CoFloating_nd,
    axis: None = None,
    weights: CoFloating_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.floating: ...
@overload
def average(
    a: CoFloating_nd,
    axis: None,
    weights: CoFloating_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.floating]: ...
@overload
def average(
    a: CoFloating_nd,
    axis: None = None,
    weights: CoFloating_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.floating]: ...
@overload
def average(
    a: ToComplex_nd,
    axis: None = None,
    weights: CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: CoComplex_nd,
    axis: None,
    weights: ToComplex_nd,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: CoComplex_nd,
    axis: None = None,
    *,
    weights: ToComplex_nd,
    returned: L[False] = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: ToComplex_nd,
    axis: None,
    weights: CoComplex_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: CoComplex_nd,
    axis: None,
    weights: ToComplex_nd,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: ToComplex_nd,
    axis: None = None,
    weights: CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: CoComplex_nd,
    axis: None = None,
    *,
    weights: ToComplex_nd,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    weights: CoComplex_nd | ToObject_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | bool = ...,
) -> Any: ...
@overload
def average(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None,
    weights: CoComplex_nd | ToObject_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | bool = ...,
) -> _2Tuple[Any]: ...
@overload
def average(
    a: CoComplex_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    weights: CoComplex_nd | ToObject_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | bool = ...,
) -> _2Tuple[Any]: ...

#
@overload
def asarray_chkfinite(a: ToBool_nd, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.bool]: ...
@overload
def asarray_chkfinite(a: ToIntP_nd, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.intp]: ...
@overload
def asarray_chkfinite(a: ToFloat64_0d, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.float64]: ...
@overload
def asarray_chkfinite(a: ToComplex128_nd, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.complex128]: ...
@overload
def asarray_chkfinite(a: ToBytes_nd, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.bytes_]: ...
@overload
def asarray_chkfinite(a: ToStr_nd, dtype: None = None, order: _OrderKACF | None = None) -> Array[np.str_]: ...
@overload
def asarray_chkfinite(a: _ArrayLike[_ScalarT], dtype: None = None, order: _OrderKACF | None = None) -> Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: _DTypeLike[_ScalarT], order: _OrderKACF | None = None) -> Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: None = None, order: _OrderKACF | None = None) -> Array: ...
@overload
def asarray_chkfinite(a: object, dtype: DTypeLike, order: _OrderKACF | None = None) -> Array: ...

#
@overload
def piecewise(
    x: _ArrayLike[_ScalarT],
    condlist: ToBool_nd,
    funclist: Sequence[Callable[Concatenate[Array1D[_ScalarT], _Tss], Array] | _ScalarT | object],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> Array[_ScalarT]: ...
@overload
def piecewise(
    x: ArrayLike,
    condlist: ToBool_nd,
    funclist: Sequence[Callable[Concatenate[Array1D, _Tss], Array] | object],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> Array: ...

#
@overload
def select(
    condlist: Sequence[ArrayLike],
    choicelist: Sequence[_ArrayLike[_ScalarT]],
    default: ArrayLike = 0,
) -> Array[_ScalarT]: ...
@overload
def select(condlist: Sequence[ArrayLike], choicelist: Sequence[ArrayLike], default: ArrayLike = 0) -> Array: ...

#
@overload
def copy(a: _ArrayT, order: _OrderKACF, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: _ArrayT, order: _OrderKACF = "K", *, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: CanLenArray[_ScalarT, _ShapeT], order: _OrderKACF = "K", subok: L[False] = False) -> Array[_ScalarT, _ShapeT]: ...
@overload
def copy(a: _ArrayLike[_ScalarT], order: _OrderKACF = "K", subok: L[False] = False) -> Array[_ScalarT]: ...
@overload
def copy(a: ArrayLike, order: _OrderKACF = "K", subok: L[False] = False) -> Array: ...

#
@overload
def gradient(f: ToGeneric_0d, *varargs: ArrayLike, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1) -> tuple[()]: ...
@overload
def gradient(f: ArrayLike, *varargs: ArrayLike, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1) -> Any: ...

#
@overload
def diff(  # type: ignore[overload-overlap]
    a: _T,
    n: L[0],
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _T: ...
@overload
def diff(
    a: _ToArray_1nd[_NumberT],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: _ArrayLike[_NumberT] | _NoValueType = ...,
    append: _ArrayLike[_NumberT] | _NoValueType = ...,
) -> Array[_NumberT]: ...
@overload
def diff(
    a: ToGeneric_1nd,
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> Array: ...

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
    x: Array[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _FloatLike_co | None = None,
    right: _FloatLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.float64]: ...
@overload  # float scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _FloatLike_co | None = None,
    right: _FloatLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.float64] | np.float64: ...
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
    fp: Sequence[complex | np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> np.complex128 | np.float64: ...
@overload  # complex array
def interp(
    x: Array[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLike[np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.complex128]: ...
@overload  # complex or float array
def interp(
    x: Array[np.floating | np.integer | np.bool] | _NestedSequence[_FloatLike_co],
    xp: _ArrayLikeFloat_co,
    fp: Sequence[complex | np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.complex128 | np.float64]: ...
@overload  # complex scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLike[np.complexfloating],
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.complex128] | np.complex128: ...
@overload  # complex or float scalar or array
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _NumberLike_co | None = None,
    right: _NumberLike_co | None = None,
    period: _FloatLike_co | None = None,
) -> Array[np.complex128 | np.float64] | np.complex128 | np.float64: ...

#
@overload
def angle(z: CoComplex_0d, deg: bool = False) -> np.floating: ...
@overload
def angle(z: CoComplex_1nd, deg: bool = False) -> Array[np.floating]: ...
@overload
def angle(z: np.object_, deg: bool = False) -> Any: ...
@overload
def angle(z: ToObject_1nd, deg: bool = False) -> Array[np.object_]: ...

#
@overload
def unwrap(p: _ArrayLikeFloat_co, discont: float | None = None, axis: int = -1, *, period: float = ...) -> Array[np.floating]: ...
@overload
def unwrap(p: _ArrayLikeObject_co, discont: float | None = None, axis: int = -1, *, period: float = ...) -> Array[np.object_]: ...

#
def sort_complex(a: ArrayLike) -> Array[np.complexfloating]: ...

#
@overload
def trim_zeros(filt: _CanLenAndGetSlice[_T], trim: L["f", "b", "fb", "bf"] = "fb", axis: None = None) -> _T: ...
@overload
def trim_zeros(filt: ToGeneric_1nd, trim: L["f", "b", "fb", "bf"] = "fb", axis: _ShapeLike | None = None) -> Array: ...

#
@overload
def extract(condition: ArrayLike, arr: _ArrayLike[_ScalarT]) -> Array[_ScalarT]: ...
@overload
def extract(condition: ArrayLike, arr: ArrayLike) -> Array: ...

#
def place(arr: Array, mask: ArrayLike, vals: Any) -> None: ...

#
@overload
def cov(
    m: CoFloating_1nd,
    y: CoFloating_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: ArrayLike | None = None,
    aweights: ArrayLike | None = None,
    *,
    dtype: None = None,
) -> Array[np.floating]: ...
@overload
def cov(
    m: ToComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: ArrayLike | None = None,
    aweights: ArrayLike | None = None,
    *,
    dtype: None = None,
) -> Array[np.complexfloating]: ...
@overload
def cov(
    m: CoComplex_1nd,
    y: ToComplex_1nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: ArrayLike | None = None,
    aweights: ArrayLike | None = None,
    *,
    dtype: None = None,
) -> Array[np.complexfloating]: ...
@overload
def cov(
    m: CoComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: ArrayLike | None = None,
    aweights: ArrayLike | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> Array[_ScalarT]: ...
@overload
def cov(
    m: CoComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: ArrayLike | None = None,
    aweights: ArrayLike | None = None,
    *,
    dtype: DTypeLike,
) -> Array: ...

# NOTE `bias` and `ddof` are deprecated and ignored
@overload
def corrcoef(
    x: CoFloating_1nd,
    y: CoFloating_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: None = None,
) -> Array[np.floating]: ...
@overload
def corrcoef(
    x: ToComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: None = None,
) -> Array[np.complexfloating]: ...
@overload
def corrcoef(
    x: CoComplex_1nd,
    y: ToComplex_1nd,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: None = None,
) -> Array[np.complexfloating]: ...
@overload
def corrcoef(
    x: CoComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> Array[_ScalarT]: ...
@overload
def corrcoef(
    x: CoComplex_1nd,
    y: CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: DTypeLike | None = None,
) -> Array: ...

#
def blackman(M: CoFloating_0d) -> Array1D[np.floating]: ...
def bartlett(M: CoFloating_0d) -> Array1D[np.floating]: ...
def hanning(M: CoFloating_0d) -> Array1D[np.floating]: ...
def hamming(M: CoFloating_0d) -> Array1D[np.floating]: ...
def kaiser(M: CoFloating_0d, beta: ToFloating_0d) -> Array1D[np.floating]: ...
def i0(x: CoFloating_nd) -> Array[np.floating]: ...

#
@overload
def sinc(x: CoFloating_0d) -> np.floating: ...
@overload
def sinc(x: ToComplex_0d) -> np.complexfloating: ...
@overload
def sinc(x: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def sinc(x: ToComplex_1nd) -> Array[np.complexfloating]: ...

# keep in sync with `lib._nanfunctions_impl.nanmedian`
@overload
def median(
    a: CoFloating_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.floating: ...
@overload
def median(
    a: ToComplex_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.complexfloating: ...
@overload
def median(
    a: ToTimeDelta_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.timedelta64: ...
@overload
def median(
    a: ToObject_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> Any: ...
@overload
def median(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> Any: ...
@overload
def median(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> _ArrayT: ...
@overload
def median(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> _ArrayT: ...

# keep in sync with `lib._nanfunctions_impl.nanpercentile`
# TODO(jorenham): deprecate interpolation
# TODO(jorenham): deprecate only allow weights if method="inverted_cdf"
@overload
def percentile(
    a: CoFloating_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.floating: ...
@overload
def percentile(
    a: CoFloating_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.floating]: ...
@overload
def percentile(
    a: ToComplex_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.complexfloating: ...
@overload
def percentile(
    a: ToComplex_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.complexfloating]: ...
@overload
def percentile(
    a: ToTimeDelta_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.timedelta64: ...
@overload
def percentile(
    a: ToTimeDelta_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.timedelta64]: ...
@overload
def percentile(
    a: ToDateTime_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.datetime64: ...
@overload
def percentile(
    a: ToDateTime_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.datetime64]: ...
@overload
def percentile(
    a: ToObject_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def percentile(
    a: ToObject_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.object_]: ...
@overload
def percentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def percentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...
@overload
def percentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...

# NOTE: Not an alias, but they do have identical signatures (that we can reuse)
quantile = percentile

@overload
def trapezoid(
    y: _ToArray2_1ds[np.float64 | np.integer | np.bool[Any], float],
    x: _ToArray2_1ds[np.float64 | np.integer | np.bool[Any], float] | None = None,
    dx: CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.float64: ...
@overload
def trapezoid(
    y: _ToArray2_2nd[np.float64 | np.integer | np.bool[Any], float],
    x: _ToArray2_1nd[np.float64 | np.integer | np.bool[Any], float] | None = None,
    dx: CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.float64]: ...
@overload
def trapezoid(
    y: _ToArray2_1nd[np.float64 | np.integer | np.bool[Any], float],
    x: _ToArray2_2nd[np.float64 | np.integer | np.bool[Any], float],
    dx: CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.float64]: ...
@overload
def trapezoid(
    y: CoFloating_1ds,
    x: CoFloating_1ds | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.floating: ...
@overload
def trapezoid(
    y: CoFloating_2nd,
    x: CoFloating_1nd | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.floating]: ...
@overload
def trapezoid(
    y: CoFloating_1nd,
    x: CoFloating_2nd,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.floating]: ...
@overload
def trapezoid(
    y: CoFloating_1nd,
    x: CoFloating_1nd | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.floating | Array[np.floating]: ...
@overload
def trapezoid(
    y: ToComplex_1ds,
    x: CoComplex_1ds | None = None,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: ToComplex_2nd,
    x: CoComplex_1nd | None = None,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: ToComplex_1nd,
    x: CoComplex_2nd,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: ToComplex_1nd,
    x: CoComplex_1nd | None = None,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.complexfloating | Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: CoComplex_1ds,
    x: ToComplex_1ds,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: CoComplex_2nd,
    x: ToComplex_1nd,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: CoComplex_1nd,
    x: ToComplex_2nd,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: CoComplex_1nd,
    x: ToComplex_1nd,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.complexfloating | Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: ToTimeDelta_1ds,
    x: CoTimeDelta_1ds | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: ToTimeDelta_2nd,
    x: CoTimeDelta_1nd | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: ToTimeDelta_1nd,
    x: CoTimeDelta_2nd,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: ToTimeDelta_1nd,
    x: CoTimeDelta_1nd | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.timedelta64 | Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: CoTimeDelta_1ds,
    x: ToTimeDelta_1ds,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: CoTimeDelta_2nd,
    x: ToTimeDelta_1nd,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: CoTimeDelta_1nd,
    x: ToTimeDelta_2nd,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: CoTimeDelta_1nd,
    x: ToTimeDelta_1nd,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.timedelta64 | Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: Sequence[dt.timedelta],
    x: Sequence[dt.timedelta] | CoFloating_1ds | None = None,
    dx: CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> dt.timedelta: ...
@overload
def trapezoid(
    y: Sequence[_CanRMulFloat[_T]],
    x: Sequence[_CanRMulFloat[_T]] | Sequence[_T] | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> _T: ...
@overload
def trapezoid(
    y: ToObject_1nd | CoComplex_1nd,
    x: ToObject_1nd | CoComplex_1nd | None = None,
    dx: CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Any: ...

#
@deprecated("Use 'trapezoid' instead")
def trapz(y: ArrayLike, x: ArrayLike | None = None, dx: float = 1.0, axis: int = -1) -> Any: ...

#
@overload
def meshgrid(
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[()]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array1D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array1D]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT1],
    x1: _ArrayLike[_ScalarT2],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array2D[_ScalarT1], Array2D[_ScalarT2]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: _ArrayLike[_ScalarT],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array2D, Array2D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT],
    x1: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array2D[_ScalarT], Array2D]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array2D, Array2D]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    x2: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array3D, Array3D, Array3D]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    x2: ArrayLike,
    x3: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array4D, Array4D, Array4D, Array4D]: ...
@overload
def meshgrid(
    *xi: ArrayLike,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[Array, ...]: ...

#
@overload
def delete(arr: _ArrayLike[_ScalarT], obj: slice | _ArrayLikeInt_co, axis: SupportsIndex | None = None) -> Array[_ScalarT]: ...
@overload
def delete(arr: ArrayLike, obj: slice | _ArrayLikeInt_co, axis: SupportsIndex | None = None) -> Array: ...

#
@overload
def insert(
    arr: _ArrayLike[_ScalarT],
    obj: slice | CoInteger_nd,
    values: ArrayLike,
    axis: SupportsIndex | None = None,
) -> Array[_ScalarT]: ...
@overload
def insert(
    arr: ArrayLike,
    obj: slice | CoInteger_nd,
    values: ArrayLike,
    axis: SupportsIndex | None = None,
) -> Array: ...

#
def append(arr: ArrayLike, values: ArrayLike, axis: SupportsIndex | None = ...) -> Array: ...

#
@overload
def digitize(x: CoFloating_0d, bins: CoFloating_1d, right: bool = False) -> np.intp: ...
@overload
def digitize(x: CoFloating_1nd, bins: CoFloating_1d, right: bool = False) -> Array[np.intp]: ...
@overload
def digitize(x: CoFloating_nd, bins: CoFloating_1d, right: bool = False) -> np.intp | Array[np.intp]: ...
