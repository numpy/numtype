from _typeshed import Incomplete
from typing import Literal as L, SupportsIndex, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._typing import DTypeLike, _ArrayLikeFloat_co, _ArrayLikeNumber_co, _DTypeLike

__all__ = ["geomspace", "linspace", "logspace"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Device: TypeAlias = L["cpu"]

###

@overload
def linspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.floating]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: None = None,
    axis: SupportsIndex = 0,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.inexact]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex,
    endpoint: bool,
    retstep: L[False],
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    retstep: L[False] = False,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = 0,
    *,
    device: _Device | None = None,
) -> _nt.Array[Incomplete]: ...
@overload
def linspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: _Device | None = None,
) -> tuple[_nt.Array[np.floating], np.floating]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: None = None,
    axis: SupportsIndex = 0,
    device: _Device | None = None,
) -> tuple[_nt.Array[np.inexact], np.inexact]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
    device: _Device | None = None,
) -> tuple[_nt.Array[_ScalarT], _ScalarT]: ...
@overload
def linspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    retstep: L[True],
    dtype: DTypeLike = ...,
    axis: SupportsIndex = 0,
    device: _Device | None = None,
) -> tuple[_nt.Array[Incomplete], Incomplete]: ...

#
@overload
def logspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _ArrayLikeFloat_co = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> _nt.Array[np.floating]: ...
@overload
def logspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _ArrayLikeNumber_co = 10.0,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> _nt.Array[np.inexact]: ...
@overload
def logspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex,
    endpoint: bool,
    base: _ArrayLikeNumber_co,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def logspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _ArrayLikeNumber_co = 10.0,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def logspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    base: _ArrayLikeNumber_co = 10.0,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = 0,
) -> _nt.Array[Incomplete]: ...

#
@overload
def geomspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> _nt.Array[np.floating]: ...
@overload
def geomspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: None = None,
    axis: SupportsIndex = 0,
) -> _nt.Array[np.inexact]: ...
@overload
def geomspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex,
    endpoint: bool,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def geomspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    *,
    dtype: _DTypeLike[_ScalarT],
    axis: SupportsIndex = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def geomspace(
    start: _ArrayLikeNumber_co,
    stop: _ArrayLikeNumber_co,
    num: SupportsIndex = 50,
    endpoint: bool = True,
    dtype: DTypeLike | None = None,
    axis: SupportsIndex = 0,
) -> _nt.Array[Incomplete]: ...

#
def add_newdoc(
    place: str, obj: str | None, doc: str | tuple[str, str] | list[tuple[str, str]], warn_on_python: bool = True
) -> None: ...  # undocumented
