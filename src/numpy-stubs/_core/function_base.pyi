from _typeshed import Incomplete
from typing import Any, Literal as L, SupportsIndex, TypeVar, overload

import _numtype as _nt
import numpy as np
from numpy._typing import DTypeLike, NDArray, _DTypeLike

__all__ = ["geomspace", "linspace", "logspace"]

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

###

@overload
def linspace(
    start: _nt.CoFloat64_nd,
    stop: _nt.CoFloat64_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[np.float64]: ...
@overload
def linspace(
    start: _nt.CoFloating_nd,
    stop: _nt.CoFloating_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[np.float64 | Any]: ...
@overload
def linspace(
    start: _nt.ToComplex128_nd,
    stop: _nt.CoComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[np.complex128]: ...
@overload
def linspace(
    start: _nt.CoComplex128_nd,
    stop: _nt.ToComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[np.complex128]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[np.complex128 | Any]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex,
    endpoint: bool,
    retstep: L[False],
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: DTypeLike | None = None,
    axis: SupportsIndex = 0,
    *,
    device: L["cpu"] | None = None,
) -> NDArray[Incomplete]: ...
@overload
def linspace(
    start: _nt.CoFloat64_nd,
    stop: _nt.CoFloat64_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[np.float64], np.float64]: ...
@overload
def linspace(
    start: _nt.CoFloating_nd,
    stop: _nt.CoFloating_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[np.floating], np.floating]: ...
@overload
def linspace(
    start: _nt.ToComplex128_nd,
    stop: _nt.CoComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[np.complex128], np.complex128]: ...
@overload
def linspace(
    start: _nt.CoComplex128_nd,
    stop: _nt.ToComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[np.complex128], np.complex128]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[np.complex128 | Any], np.complex128 | Any]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[_ScalarT], _ScalarT]: ...
@overload
def linspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: DTypeLike | None = None,
    axis: SupportsIndex = 0,
    device: L["cpu"] | None = None,
) -> tuple[NDArray[Incomplete], Incomplete]: ...

#
@overload
def logspace(
    start: _nt.CoFloat64_nd,
    stop: _nt.CoFloat64_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoFloat64_nd = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.float64]: ...
@overload
def logspace(
    start: _nt.CoFloating_nd,
    stop: _nt.CoFloating_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoFloating_nd = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.float64 | Any]: ...
@overload
def logspace(
    start: _nt.ToComplex128_nd,
    stop: _nt.CoComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoComplex_nd = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128]: ...
@overload
def logspace(
    start: _nt.CoComplex128_nd,
    stop: _nt.ToComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoComplex_nd = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128]: ...
@overload
def logspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoComplex_nd = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128 | Any]: ...
@overload
def logspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex,
    endpoint: bool,
    base: _nt.CoComplex_nd,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> NDArray[_ScalarT]: ...
@overload
def logspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoFloating_nd = 10.0,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> NDArray[_ScalarT]: ...
@overload
def logspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _nt.CoComplex_nd = 10.0,
    dtype: DTypeLike | None = None,
    axis: SupportsIndex = 0,
) -> NDArray[Incomplete]: ...

#
@overload
def geomspace(
    start: _nt.CoFloat64_nd,
    stop: _nt.CoFloat64_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.float64]: ...
@overload
def geomspace(
    start: _nt.CoFloating_nd,
    stop: _nt.CoFloating_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.float64 | Any]: ...
@overload
def geomspace(
    start: _nt.ToComplex128_nd,
    stop: _nt.CoComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128]: ...
@overload
def geomspace(
    start: _nt.CoComplex128_nd,
    stop: _nt.ToComplex128_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128]: ...
@overload
def geomspace(
    start: _nt.ToComplex_nd,
    stop: _nt.ToComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> NDArray[np.complex128 | Any]: ...
@overload
def geomspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex,
    endpoint: bool,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> NDArray[_ScalarT]: ...
@overload
def geomspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> NDArray[_ScalarT]: ...
@overload
def geomspace(
    start: _nt.CoComplex_nd,
    stop: _nt.CoComplex_nd,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: DTypeLike | None = None,
    axis: SupportsIndex = 0,
) -> NDArray[Incomplete]: ...

#
def add_newdoc(
    place: str, obj: str, doc: str | tuple[str, str] | list[tuple[str, str]], warn_on_python: bool = True
) -> None: ...
