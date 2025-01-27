from collections.abc import Callable
from contextlib import _GeneratorContextManager
from typing import Any, Literal, SupportsIndex, TypeAlias, TypedDict, type_check_only

import numpy as np
from numpy._typing import NDArray, _CharLike_co, _FloatLike_co

_FloatMode: TypeAlias = Literal["fixed", "unique", "maxprec", "maxprec_equal"]
_Sign: TypeAlias = Literal["-", "+", " "]
_Legacy: TypeAlias = Literal[False, "1.13", "1.21"]
_Trim: TypeAlias = Literal["k", ".", "0", "-"]

@type_check_only
class _FormatDict(TypedDict, total=False):
    bool: Callable[[np.bool], str]
    int: Callable[[np.integer], str]
    timedelta: Callable[[np.timedelta64], str]
    datetime: Callable[[np.datetime64], str]
    float: Callable[[np.floating], str]
    longfloat: Callable[[np.longdouble], str]
    complexfloat: Callable[[np.complexfloating], str]
    longcomplexfloat: Callable[[np.clongdouble], str]
    void: Callable[[np.void], str]
    numpystr: Callable[[_CharLike_co], str]
    object: Callable[[object], str]
    all: Callable[[object], str]
    int_kind: Callable[[np.integer], str]
    float_kind: Callable[[np.floating], str]
    complex_kind: Callable[[np.complexfloating], str]
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
    sign: _Sign
    floatmode: _FloatMode
    legacy: _Legacy

def set_printoptions(
    precision: SupportsIndex | None = ...,
    threshold: int | None = ...,
    edgeitems: int | None = ...,
    linewidth: int | None = ...,
    suppress: bool | None = ...,
    nanstr: str | None = ...,
    infstr: str | None = ...,
    formatter: _FormatDict | None = ...,
    sign: _Sign | None = ...,
    floatmode: _FloatMode | None = ...,
    *,
    legacy: _Legacy | None = ...,
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
    sign: _Sign | None = ...,
    floatmode: _FloatMode | None = ...,
    suffix: str = ...,
    legacy: _Legacy | None = ...,
) -> str: ...
def format_float_scientific(
    x: _FloatLike_co,
    precision: int | None = ...,
    unique: bool = ...,
    trim: _Trim = ...,
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
    trim: _Trim = ...,
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
    sign: _Sign | None = ...,
    floatmode: _FloatMode | None = ...,
    *,
    legacy: _Legacy | None = ...,
) -> _GeneratorContextManager[_FormatOptions]: ...
