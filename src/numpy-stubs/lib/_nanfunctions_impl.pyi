from typing import Any, Literal as L, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    Array,
    CoComplex_nd,
    CoDateTime_nd,
    CoFloating_0d,
    CoFloating_1nd,
    CoFloating_nd,
    CoTimeDelta_nd,
    ToComplex_nd,
    ToDateTime_nd,
    ToObject_nd,
    ToTimeDelta_nd,
)
from numpy._core.fromnumeric import (
    amax as nanmax,
    amin as nanmin,
    argmax as nanargmax,
    argmin as nanargmin,
    cumprod as nancumprod,
    cumsum as nancumsum,
    mean as nanmean,
    prod as nanprod,
    std as nanstd,
    sum as nansum,
    var as nanvar,
)
from numpy._globals import _NoValueType
from numpy._typing import _ShapeLike

from ._function_base_impl import _PercentileMethod

__all__ = [
    "nanargmax",
    "nanargmin",
    "nancumprod",
    "nancumsum",
    "nanmax",
    "nanmean",
    "nanmedian",
    "nanmin",
    "nanpercentile",
    "nanprod",
    "nanquantile",
    "nanstd",
    "nansum",
    "nanvar",
]

###

_ArrayT = TypeVar("_ArrayT", bound=Array)

###

# keep in sync with `lib._function_base_impl.median`
@overload
def nanmedian(
    a: CoFloating_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.floating: ...
@overload
def nanmedian(
    a: ToComplex_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def nanmedian(
    a: ToTimeDelta_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.timedelta64: ...
@overload
def nanmedian(
    a: ToObject_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> Any: ...
@overload
def nanmedian(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> Any: ...
@overload
def nanmedian(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> _ArrayT: ...
@overload
def nanmedian(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> _ArrayT: ...

# keep in sync with `lib._function_base_impl.percentile`
@overload
def nanpercentile(
    a: CoFloating_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.floating: ...
@overload
def nanpercentile(
    a: CoFloating_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.floating]: ...
@overload
def nanpercentile(
    a: ToComplex_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.complexfloating: ...
@overload
def nanpercentile(
    a: ToComplex_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.complexfloating]: ...
@overload
def nanpercentile(
    a: ToTimeDelta_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.timedelta64: ...
@overload
def nanpercentile(
    a: ToTimeDelta_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.timedelta64]: ...
@overload
def nanpercentile(
    a: ToDateTime_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.datetime64: ...
@overload
def nanpercentile(
    a: ToDateTime_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.datetime64]: ...
@overload
def nanpercentile(
    a: ToObject_nd,
    q: CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def nanpercentile(
    a: ToObject_nd,
    q: CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Array[np.object_]: ...
@overload
def nanpercentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def nanpercentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...
@overload
def nanpercentile(
    a: CoComplex_nd | CoDateTime_nd | ToObject_nd,
    q: CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    *,
    weights: CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...

nanquantile = nanpercentile
