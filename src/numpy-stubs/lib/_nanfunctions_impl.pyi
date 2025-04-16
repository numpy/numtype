from _typeshed import Incomplete
from typing import Any, Literal as L, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
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

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)

###

# keep in sync with `lib._function_base_impl.median`
@overload
def nanmedian(
    a: _nt.CoFloating_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.floating: ...
@overload
def nanmedian(
    a: _nt.ToComplex_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.complexfloating: ...
@overload
def nanmedian(
    a: _nt.ToTimeDelta_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> np.timedelta64: ...
@overload
def nanmedian(
    a: _nt.ToObject_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | L[False] = ...,
) -> Incomplete: ...
@overload
def nanmedian(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> Incomplete: ...
@overload
def nanmedian(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> _ArrayT: ...
@overload
def nanmedian(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: _NoValueType | bool = ...,
) -> _ArrayT: ...

# keep in sync with `lib._function_base_impl.percentile`
@overload
def nanpercentile(
    a: _nt.CoFloating_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.floating: ...
@overload
def nanpercentile(
    a: _nt.CoFloating_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.floating]: ...
@overload
def nanpercentile(
    a: _nt.ToComplex_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.complexfloating: ...
@overload
def nanpercentile(
    a: _nt.ToComplex_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.complexfloating]: ...
@overload
def nanpercentile(
    a: _nt.ToTimeDelta_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.timedelta64: ...
@overload
def nanpercentile(
    a: _nt.ToTimeDelta_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.timedelta64]: ...
@overload
def nanpercentile(
    a: _nt.ToDateTime_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> np.datetime64: ...
@overload
def nanpercentile(
    a: _nt.ToDateTime_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.datetime64]: ...
@overload
def nanpercentile(
    a: _nt.ToObject_nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def nanpercentile(
    a: _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | L[False] = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _nt.Array[np.object_]: ...
@overload
def nanpercentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> Any: ...
@overload
def nanpercentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...
@overload
def nanpercentile(
    a: _nt.CoComplex_nd | _nt.CoDateTime_nd | _nt.ToObject_nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: _NoValueType | bool = ...,
    *,
    weights: _nt.CoFloating_1nd | None = None,
    interpolation: None = None,
) -> _ArrayT: ...

nanquantile = nanpercentile
