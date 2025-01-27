from collections.abc import Callable

# Using a private class is by no means ideal, but it is simply a consequence
# of a `contextlib.context` returning an instance of aforementioned class
from contextlib import _GeneratorContextManager
from typing import Any, Literal, SupportsIndex, TypeAlias, TypedDict, type_check_only

import numpy as np
from numpy import (
    clongdouble,
    complexfloating,
    datetime64,
    floating,
    integer,
    longdouble,
    timedelta64,
    void,
)
from numpy._typing import NDArray, _CharLike_co, _FloatLike_co

_FloatMode: TypeAlias = Literal["fixed", "unique", "maxprec", "maxprec_equal"]

@type_check_only
class _FormatDict(TypedDict, total=False):
    bool: Callable[[np.bool], str]
    int: Callable[[integer[Any]], str]
    timedelta: Callable[[timedelta64], str]
    datetime: Callable[[datetime64], str]
    float: Callable[[floating[Any]], str]
    longfloat: Callable[[longdouble], str]
    complexfloat: Callable[[complexfloating[Any, Any]], str]
    longcomplexfloat: Callable[[clongdouble], str]
    void: Callable[[void], str]
    numpystr: Callable[[_CharLike_co], str]
    object: Callable[[object], str]
    all: Callable[[object], str]
    int_kind: Callable[[integer[Any]], str]
    float_kind: Callable[[floating[Any]], str]
    complex_kind: Callable[[complexfloating[Any, Any]], str]
    str_kind: Callable[[_CharLike_co], str]

@type_check_only
class _FormatOptions(TypedDict):
    precision: int
    threshold: int
    edgeitems: int
    linewidth: int
    suppress: bool
    nanstr: str
    infstr: str
    formatter: _FormatDict | None
    sign: Literal["-", "+", " "]
    floatmode: _FloatMode
    legacy: Literal[False, "1.13", "1.21"]

def set_printoptions(
    precision: SupportsIndex | None = ...,
    threshold: int | None = ...,
    edgeitems: int | None = ...,
    linewidth: int | None = ...,
    suppress: bool | None = ...,
    nanstr: str | None = ...,
    infstr: str | None = ...,
    formatter: _FormatDict | None = ...,
    sign: Literal["-", "+", " "] | None = ...,
    floatmode: _FloatMode | None = ...,
    *,
    legacy: Literal[False, "1.13", "1.21"] | None = ...,
    override_repr: Callable[[NDArray[Any]], str] | None = ...,
) -> None: ...
def get_printoptions() -> _FormatOptions: ...
def array2string(
    a: NDArray[Any],
    max_line_width: int | None = ...,
    precision: SupportsIndex | None = ...,
    suppress_small: bool | None = ...,
    separator: str = ...,
    prefix: str = ...,
    # NOTE: With the `style` argument being deprecated,
    # all arguments between `formatter` and `suffix` are de facto
    # keyworld-only arguments
    *,
    formatter: _FormatDict | None = ...,
    threshold: int | None = ...,
    edgeitems: int | None = ...,
    sign: Literal["-", "+", " "] | None = ...,
    floatmode: _FloatMode | None = ...,
    suffix: str = ...,
    legacy: Literal[False, "1.13", "1.21"] | None = ...,
) -> str: ...
def format_float_scientific(
    x: _FloatLike_co,
    precision: int | None = ...,
    unique: bool = ...,
    trim: Literal["k", ".", "0", "-"] = ...,
    sign: bool = ...,
    pad_left: int | None = ...,
    exp_digits: int | None = ...,
    min_digits: int | None = ...,
) -> str: ...
def format_float_positional(
    x: _FloatLike_co,
    precision: int | None = ...,
    unique: bool = ...,
    fractional: bool = ...,
    trim: Literal["k", ".", "0", "-"] = ...,
    sign: bool = ...,
    pad_left: int | None = ...,
    pad_right: int | None = ...,
    min_digits: int | None = ...,
) -> str: ...
def array_repr(
    arr: NDArray[Any],
    max_line_width: int | None = ...,
    precision: SupportsIndex | None = ...,
    suppress_small: bool | None = ...,
) -> str: ...
def array_str(
    a: NDArray[Any],
    max_line_width: int | None = ...,
    precision: SupportsIndex | None = ...,
    suppress_small: bool | None = ...,
) -> str: ...
def printoptions(
    precision: SupportsIndex | None = ...,
    threshold: int | None = ...,
    edgeitems: int | None = ...,
    linewidth: int | None = ...,
    suppress: bool | None = ...,
    nanstr: str | None = ...,
    infstr: str | None = ...,
    formatter: _FormatDict | None = ...,
    sign: Literal["-", "+", " "] | None = ...,
    floatmode: _FloatMode | None = ...,
    *,
    legacy: Literal[False, "1.13", "1.21"] | None = ...,
) -> _GeneratorContextManager[_FormatOptions]: ...
