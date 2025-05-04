import datetime as dt
from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Sequence
from typing import (
    Concatenate,
    Final,
    Literal as L,
    LiteralString,
    Protocol,
    SupportsIndex as CanIndex,
    SupportsInt,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import ParamSpec, TypeIs, TypeVar, deprecated

import _numtype as _nt
import numpy as np
from numpy import _OrderKACF as _Order  # noqa: ICN003
from numpy._core.multiarray import bincount
from numpy._globals import _NoValueType
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike, _DTypeLike, _ShapeLike

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

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT1 = TypeVar("_ScalarT1", bound=np.generic)
_ScalarT2 = TypeVar("_ScalarT2", bound=np.generic)
_NumberT = TypeVar("_NumberT", bound=np.number)

_2Tuple: TypeAlias = tuple[_T, _T]
_ToInt: TypeAlias = CanIndex | SupportsInt
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
    pyfunc: Callable[..., Incomplete]
    cache: Final[bool]
    signature: Final[LiteralString | None]
    otypes: Final[LiteralString | None]
    excluded: Final[set[int | str]]

    #
    def __init__(
        self,
        /,
        pyfunc: Callable[..., Incomplete] | _NoValueType = ...,
        otypes: str | Iterable[DTypeLike] | None = None,
        doc: str | None = None,
        excluded: Iterable[int | str] | None = None,
        cache: bool = False,
        signature: str | None = None,
    ) -> None: ...

    #
    def __call__(self, /, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

###

#
@overload
def rot90(m: _ArrayLike[_ScalarT], k: int = 1, axes: tuple[int, int] = (0, 1)) -> _nt.Array[_ScalarT]: ...
@overload
def rot90(m: ArrayLike, k: int = 1, axes: tuple[int, int] = (0, 1)) -> _nt.Array[Incomplete]: ...

#
@overload
def flip(m: _ScalarT, axis: None = None) -> _ScalarT: ...
@overload
def flip(m: _nt.ToGeneric_0d, axis: None = None) -> Incomplete: ...
@overload
def flip(m: _nt._ToArray_1nd[_ScalarT], axis: _ShapeLike | None = None) -> _nt.Array[_ScalarT]: ...
@overload
def flip(m: _nt.ToGeneric_1nd, axis: _ShapeLike | None = None) -> _nt.Array[Incomplete]: ...

#
def iterable(y: object) -> TypeIs[Iterable[Incomplete]]: ...

#
@overload
def average(
    a: _nt.ToFloat64_nd | _nt.CoInteger_nd,
    axis: None = None,
    weights: _nt.CoFloat64_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.float64: ...
@overload
def average(
    a: _nt.ToFloat64_nd | _nt.CoInteger_nd,
    axis: None,
    weights: _nt.CoFloat64_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType = ...,
) -> _2Tuple[np.float64]: ...
@overload
def average(
    a: _nt.ToFloat64_nd | _nt.CoInteger_nd,
    axis: None = None,
    weights: _nt.CoFloat64_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.float64]: ...
@overload
def average(
    a: _nt.CoFloating_nd,
    axis: None = None,
    weights: _nt.CoFloating_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.floating: ...
@overload
def average(
    a: _nt.CoFloating_nd,
    axis: None,
    weights: _nt.CoFloating_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.floating]: ...
@overload
def average(
    a: _nt.CoFloating_nd,
    axis: None = None,
    weights: _nt.CoFloating_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.floating]: ...
@overload
def average(
    a: _nt.ToComplex_nd,
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: _nt.CoComplex_nd,
    axis: None,
    weights: _nt.ToComplex_nd,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: _nt.CoComplex_nd,
    axis: None = None,
    *,
    weights: _nt.ToComplex_nd,
    returned: L[False] = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def average(
    a: _nt.ToComplex_nd,
    axis: None,
    weights: _nt.CoComplex_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: _nt.CoComplex_nd,
    axis: None,
    weights: _nt.ToComplex_nd,
    returned: L[True],
    *,
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: _nt.ToComplex_nd,
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: _nt.CoComplex_nd,
    axis: None = None,
    *,
    weights: _nt.ToComplex_nd,
    returned: L[True],
    keepdims: _NoValueType | L[False] = ...,
) -> _2Tuple[np.complexfloating]: ...
@overload
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    weights: _nt.CoComplex_nd | _nt.ToObject_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: _NoValueType | bool = ...,
) -> Incomplete: ...
@overload
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    weights: _nt.CoComplex_nd | _nt.ToObject_nd | None,
    returned: L[True],
    *,
    keepdims: _NoValueType | bool = ...,
) -> _2Tuple[Incomplete]: ...
@overload
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    weights: _nt.CoComplex_nd | _nt.ToObject_nd | None = None,
    *,
    returned: L[True],
    keepdims: _NoValueType | bool = ...,
) -> _2Tuple[Incomplete]: ...

#
@overload
def asarray_chkfinite(a: _nt.ToBool_nd, dtype: None = None, order: _Order | None = None) -> _nt.Array[np.bool]: ...
@overload
def asarray_chkfinite(a: _nt.ToInt_nd, dtype: None = None, order: _Order | None = None) -> _nt.Array[np.intp]: ...
@overload
def asarray_chkfinite(
    a: _nt.ToFloat64_0d, dtype: None = None, order: _Order | None = None
) -> _nt.Array[np.float64]: ...
@overload
def asarray_chkfinite(
    a: _nt.ToComplex128_nd, dtype: None = None, order: _Order | None = None
) -> _nt.Array[np.complex128]: ...
@overload
def asarray_chkfinite(a: _nt.ToBytes_nd, dtype: None = None, order: _Order | None = None) -> _nt.Array[np.bytes_]: ...
@overload
def asarray_chkfinite(a: _nt.ToStr_nd, dtype: None = None, order: _Order | None = None) -> _nt.Array[np.str_]: ...
@overload
def asarray_chkfinite(
    a: _ArrayLike[_ScalarT], dtype: None = None, order: _Order | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: _DTypeLike[_ScalarT], order: _Order | None = None) -> _nt.Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: None = None, order: _Order | None = None) -> _nt.Array[Incomplete]: ...
@overload
def asarray_chkfinite(a: object, dtype: DTypeLike, order: _Order | None = None) -> _nt.Array[Incomplete]: ...

#
@overload
def piecewise(
    x: _ArrayLike[_ScalarT],
    condlist: _nt.ToBool_nd,
    funclist: Sequence[Callable[Concatenate[_nt.Array1D[_ScalarT], _Tss], _nt.Array] | _ScalarT | object],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> _nt.Array[_ScalarT]: ...
@overload
def piecewise(
    x: ArrayLike,
    condlist: _nt.ToBool_nd,
    funclist: Sequence[Callable[Concatenate[_nt.Array1D, _Tss], _nt.Array] | object],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> _nt.Array[Incomplete]: ...

#
@overload
def select(
    condlist: Sequence[ArrayLike],
    choicelist: Sequence[_ArrayLike[_ScalarT]],
    default: ArrayLike = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def select(
    condlist: Sequence[ArrayLike],
    choicelist: Sequence[ArrayLike],
    default: ArrayLike = 0,
) -> _nt.Array[Incomplete]: ...

#
@overload
def copy(a: _ArrayT, order: _Order, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: _ArrayT, order: _Order = "K", *, subok: L[True]) -> _ArrayT: ...
@overload
def copy(
    a: _nt.CanLenArray[_ScalarT, _ShapeT], order: _Order = "K", subok: L[False] = False
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def copy(a: _ArrayLike[_ScalarT], order: _Order = "K", subok: L[False] = False) -> _nt.Array[_ScalarT]: ...
@overload
def copy(a: ArrayLike, order: _Order = "K", subok: L[False] = False) -> _nt.Array[Incomplete]: ...

#
@overload
def gradient(
    f: _nt.ToGeneric_0d,
    *varargs: ArrayLike,
    axis: _ShapeLike | None = None,
    edge_order: L[1, 2] = 1,
) -> tuple[()]: ...
@overload
def gradient(
    f: ArrayLike,
    *varargs: ArrayLike,
    axis: _ShapeLike | None = None,
    edge_order: L[1, 2] = 1,
) -> Incomplete: ...

#
@overload
def diff(  # type: ignore[overload-overlap]
    a: _T,
    n: L[0],
    axis: CanIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _T: ...
@overload
def diff(
    a: _nt._ToArray_1nd[_NumberT],
    n: int = 1,
    axis: CanIndex = -1,
    prepend: _ArrayLike[_NumberT] | _NoValueType = ...,
    append: _ArrayLike[_NumberT] | _NoValueType = ...,
) -> _nt.Array[_NumberT]: ...
@overload
def diff(
    a: _nt.ToGeneric_1nd,
    n: int = 1,
    axis: CanIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array[Incomplete]: ...

#
@overload  # float scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> np.float64: ...
@overload  # float array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.float64] | np.float64: ...
@overload  # complex scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> np.complex128: ...
@overload  # complex or float scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: Sequence[complex | np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.inexact64: ...
@overload  # complex array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex or float array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: Sequence[complex | np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[_nt.inexact64]: ...
@overload  # complex scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.complex128] | np.complex128: ...
@overload  # complex or float scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoComplex_nd,
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[_nt.inexact64] | _nt.inexact64: ...

#
@overload
def angle(z: _nt.CoComplex_0d, deg: bool = False) -> np.floating: ...
@overload
def angle(z: _nt.CoComplex_1nd, deg: bool = False) -> _nt.Array[np.floating]: ...
@overload
def angle(z: np.object_, deg: bool = False) -> Incomplete: ...
@overload
def angle(z: _nt.ToObject_1nd, deg: bool = False) -> _nt.Array[np.object_]: ...

#
@overload
def unwrap(
    p: _nt.CoFloating_nd,
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,
) -> _nt.Array[np.floating]: ...
@overload
def unwrap(
    p: _nt.ToObject_nd,
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,
) -> _nt.Array[np.object_]: ...

#
def sort_complex(a: ArrayLike) -> _nt.Array[np.complexfloating]: ...

#
@overload
def trim_zeros(filt: _CanLenAndGetSlice[_T], trim: L["f", "b", "fb", "bf"] = "fb", axis: None = None) -> _T: ...
@overload
def trim_zeros(
    filt: _nt.ToGeneric_1nd, trim: L["f", "b", "fb", "bf"] = "fb", axis: _ShapeLike | None = None
) -> _nt.Array[Incomplete]: ...

#
@overload
def extract(condition: ArrayLike, arr: _ArrayLike[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def extract(condition: ArrayLike, arr: ArrayLike) -> _nt.Array[Incomplete]: ...

#
def place(arr: _nt.Array[Incomplete], mask: ArrayLike, vals: Incomplete) -> None: ...

#
@overload
def cov(
    m: _nt.CoFloat64_1nd,
    y: _nt.CoFloat64_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeFloat64 | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def cov(
    m: _nt.ToLongDouble_1nd,
    y: _nt.CoFloating_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeLongDouble | None = None,
) -> _nt.Array[np.longdouble]: ...
@overload
def cov(
    m: _nt.CoFloating_1nd,
    y: _nt.ToLongDouble_1nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeLongDouble | None = None,
) -> _nt.Array[np.longdouble]: ...
@overload
def cov(
    m: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    y: _nt.CoComplex128_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def cov(
    m: _nt.CoComplex128_1nd,
    y: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def cov(
    m: _nt.ToCLongDouble_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeCLongDouble | None = None,
) -> _nt.Array[np.clongdouble]: ...
@overload
def cov(
    m: _nt.CoComplex_1nd,
    y: _nt.ToCLongDouble_1nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _nt.ToDTypeCLongDouble | None = None,
) -> _nt.Array[np.clongdouble]: ...
@overload
def cov(
    m: _nt.CoComplex_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> _nt.Array[_ScalarT]: ...
@overload
def cov(
    m: _nt.CoComplex_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: _ToInt | None = None,
    fweights: _nt.ToInteger_1d | None = None,
    aweights: _nt.CoFloating_1d | None = None,
    *,
    dtype: DTypeLike,
) -> _nt.Array[Incomplete]: ...

# NOTE `bias` and `ddof` are deprecated and ignored
@overload
def corrcoef(
    x: _nt.CoFloat64_1nd,
    y: _nt.CoFloat64_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeFloat64 | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def corrcoef(
    x: _nt.ToLongDouble_1nd,
    y: _nt.CoFloating_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeLongDouble | None = None,
) -> _nt.Array[np.longdouble]: ...
@overload
def corrcoef(
    x: _nt.CoFloating_1nd,
    y: _nt.ToLongDouble_1nd,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeLongDouble | None = None,
) -> _nt.Array[np.longdouble]: ...
@overload
def corrcoef(
    x: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    y: _nt.CoComplex128_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def corrcoef(
    x: _nt.CoComplex128_1nd,
    y: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def corrcoef(
    x: _nt.ToCLongDouble_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeCLongDouble | None = None,
) -> _nt.Array[np.clongdouble]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd,
    y: _nt.ToCLongDouble_1nd,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _nt.ToDTypeCLongDouble | None = None,
) -> _nt.Array[np.clongdouble]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> _nt.Array[_ScalarT]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    bias: _NoValueType = ...,
    ddof: _NoValueType = ...,
    *,
    dtype: DTypeLike | None = None,
) -> _nt.Array[Incomplete]: ...

#
def blackman(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def bartlett(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def hanning(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def hamming(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def kaiser(M: _nt.CoFloating_0d, beta: _nt.ToFloating_0d) -> _nt.Array1D[np.floating]: ...
def i0(x: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...

#
@overload
def sinc(x: _nt.CoFloating_0d) -> np.floating: ...
@overload
def sinc(x: _nt.ToComplex_0d) -> np.complexfloating: ...
@overload
def sinc(x: _nt.CoFloating_1nd) -> _nt.Array[np.floating]: ...
@overload
def sinc(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...

# keep in sync with `lib._nanfunctions_impl.nanmedian`
@overload
def median(
    a: _nt.CoFloating_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.floating: ...
@overload
def median(
    a: _nt.ToComplex_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.complexfloating: ...
@overload
def median(
    a: _nt.ToTimeDelta_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.timedelta64: ...
@overload
def median(
    a: _nt.ToObject_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> Incomplete: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> Incomplete: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> _ArrayT: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
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
    a: _nt.CoFloating_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.floating: ...
@overload
def percentile(
    a: _nt.CoFloating_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.floating]: ...
@overload
def percentile(
    a: _nt.ToComplex_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.complexfloating: ...
@overload
def percentile(
    a: _nt.ToComplex_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.complexfloating]: ...
@overload
def percentile(
    a: _nt.ToTimeDelta_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.timedelta64: ...
@overload
def percentile(
    a: _nt.ToTimeDelta_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.timedelta64]: ...
@overload
def percentile(
    a: _nt.ToDateTime_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.datetime64: ...
@overload
def percentile(
    a: _nt.ToDateTime_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.datetime64]: ...
@overload
def percentile(
    a: _nt.ToObject_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Incomplete: ...
@overload
def percentile(
    a: _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.object_]: ...
@overload
def percentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Incomplete: ...
@overload
def percentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...
@overload
def percentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...

# NOTE: Not an alias, but they do have identical signatures (that we can reuse)
quantile = percentile

@overload
def trapezoid(
    y: _nt._ToArray2_1ds[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_1ds[np.float64 | _nt.co_integer, float] | None = None,
    dx: _nt.CoFloat64_0d = 1.0,
    axis: CanIndex = -1,
) -> np.float64: ...
@overload
def trapezoid(
    y: _nt._ToArray2_2nd[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_1nd[np.float64 | _nt.co_integer, float] | None = None,
    dx: _nt.CoFloat64_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.float64]: ...
@overload
def trapezoid(
    y: _nt._ToArray2_1nd[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_2nd[np.float64 | _nt.co_integer, float],
    dx: _nt.CoFloat64_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.float64]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1ds,
    x: _nt.CoFloating_1ds | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.floating: ...
@overload
def trapezoid(
    y: _nt.CoFloating_2nd,
    x: _nt.CoFloating_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1nd,
    x: _nt.CoFloating_2nd,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1nd,
    x: _nt.CoFloating_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.floating | _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1ds,
    x: _nt.CoComplex_1ds | None = None,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: _nt.ToComplex_2nd,
    x: _nt.CoComplex_1nd | None = None,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1nd,
    x: _nt.CoComplex_2nd,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1nd,
    x: _nt.CoComplex_1nd | None = None,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> np.complexfloating | _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1ds,
    x: _nt.ToComplex_1ds,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: _nt.CoComplex_2nd,
    x: _nt.ToComplex_1nd,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1nd,
    x: _nt.ToComplex_2nd,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1nd,
    x: _nt.ToComplex_1nd,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> np.complexfloating | _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1ds,
    x: _nt.CoTimeDelta_1ds | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_2nd,
    x: _nt.CoTimeDelta_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1nd,
    x: _nt.CoTimeDelta_2nd,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1nd,
    x: _nt.CoTimeDelta_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.timedelta64 | _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1ds,
    x: _nt.ToTimeDelta_1ds,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_2nd,
    x: _nt.ToTimeDelta_1nd,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1nd,
    x: _nt.ToTimeDelta_2nd,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1nd,
    x: _nt.ToTimeDelta_1nd,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> np.timedelta64 | _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: Sequence[dt.timedelta],
    x: Sequence[dt.timedelta] | _nt.CoFloating_1ds | None = None,
    dx: _nt.CoComplex_0d = 1.0,
    axis: CanIndex = -1,
) -> dt.timedelta: ...
@overload
def trapezoid(
    y: Sequence[_CanRMulFloat[_T]],
    x: Sequence[_CanRMulFloat[_T]] | Sequence[_T] | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> _T: ...
@overload
def trapezoid(
    y: _nt.ToObject_1nd | _nt.CoComplex_1nd,
    x: _nt.ToObject_1nd | _nt.CoComplex_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: CanIndex = -1,
) -> Incomplete: ...

#
@deprecated("Use 'trapezoid' instead")
def trapz(y: ArrayLike, x: ArrayLike | None = None, dx: float = 1.0, axis: int = -1) -> Incomplete: ...

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
) -> tuple[_nt.Array1D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array1D]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT1],
    x1: _ArrayLike[_ScalarT2],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array2D[_ScalarT1], _nt.Array2D[_ScalarT2]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: _ArrayLike[_ScalarT],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array2D[Incomplete], _nt.Array2D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT],
    x1: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array2D[_ScalarT], _nt.Array2D[Incomplete]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array2D[Incomplete], _nt.Array2D[Incomplete]]: ...
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
) -> tuple[_nt.Array3D[Incomplete], _nt.Array3D[Incomplete], _nt.Array3D[Incomplete]]: ...
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
) -> tuple[
    _nt.Array4D[Incomplete],
    _nt.Array4D[Incomplete],
    _nt.Array4D[Incomplete],
    _nt.Array4D[Incomplete],
]: ...
@overload
def meshgrid(
    *xi: ArrayLike,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array[Incomplete], ...]: ...

#
@overload
def delete(
    arr: _ArrayLike[_ScalarT],
    obj: slice | _nt.CoInteger_nd,
    axis: CanIndex | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def delete(
    arr: ArrayLike,
    obj: slice | _nt.CoInteger_nd,
    axis: CanIndex | None = None,
) -> _nt.Array[Incomplete]: ...

#
@overload
def insert(
    arr: _ArrayLike[_ScalarT],
    obj: slice | _nt.CoInteger_nd,
    values: ArrayLike,
    axis: CanIndex | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def insert(
    arr: ArrayLike,
    obj: slice | _nt.CoInteger_nd,
    values: ArrayLike,
    axis: CanIndex | None = None,
) -> _nt.Array[Incomplete]: ...

#
def append(arr: ArrayLike, values: ArrayLike, axis: CanIndex | None = ...) -> _nt.Array[Incomplete]: ...

#
@overload
def digitize(x: _nt.CoFloating_0d, bins: _nt.CoFloating_1d, right: bool = False) -> np.intp: ...
@overload
def digitize(x: _nt.CoFloating_1nd, bins: _nt.CoFloating_1d, right: bool = False) -> _nt.Array[np.intp]: ...
@overload
def digitize(x: _nt.CoFloating_nd, bins: _nt.CoFloating_1d, right: bool = False) -> np.intp | _nt.Array[np.intp]: ...
