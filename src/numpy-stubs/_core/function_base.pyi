from typing import Any, Literal as L, SupportsIndex, TypeVar, overload

import numpy as np
from numpy._typing import DTypeLike, NDArray, _ArrayLikeComplex_co, _ArrayLikeFloat_co, _DTypeLike

__all__ = ["geomspace", "linspace", "logspace"]

_SCT = TypeVar("_SCT", bound=np.generic)

@overload
def linspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[False] = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[np.floating]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[False] = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[False] = ...,
    dtype: _DTypeLike[_SCT] = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[False] = ...,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[Any]: ...
@overload
def linspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[True] = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> tuple[NDArray[np.floating], np.floating]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[True] = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> tuple[NDArray[np.complexfloating], np.complexfloating]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[True] = ...,
    dtype: _DTypeLike[_SCT] = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> tuple[NDArray[_SCT], _SCT]: ...
@overload
def linspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    retstep: L[True] = ...,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = ...,
    *,
    device: L["cpu"] | None = ...,
) -> tuple[NDArray[Any], Any]: ...

#
@overload
def logspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    base: _ArrayLikeFloat_co = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
) -> NDArray[np.floating]: ...
@overload
def logspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    base: _ArrayLikeComplex_co = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def logspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    base: _ArrayLikeComplex_co = ...,
    dtype: _DTypeLike[_SCT] = ...,
    axis: SupportsIndex = ...,
) -> NDArray[_SCT]: ...
@overload
def logspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    base: _ArrayLikeComplex_co = ...,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = ...,
) -> NDArray[Any]: ...

#
@overload
def geomspace(
    start: _ArrayLikeFloat_co,
    stop: _ArrayLikeFloat_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
) -> NDArray[np.floating]: ...
@overload
def geomspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    dtype: None = ...,
    axis: SupportsIndex = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def geomspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    dtype: _DTypeLike[_SCT] = ...,
    axis: SupportsIndex = ...,
) -> NDArray[_SCT]: ...
@overload
def geomspace(
    start: _ArrayLikeComplex_co,
    stop: _ArrayLikeComplex_co,
    num: SupportsIndex = ...,
    endpoint: bool = ...,
    dtype: DTypeLike = ...,
    axis: SupportsIndex = ...,
) -> NDArray[Any]: ...

#
def add_newdoc(place: str, obj: str, doc: str | tuple[str, str] | list[tuple[str, str]], warn_on_python: bool = ...) -> None: ...
