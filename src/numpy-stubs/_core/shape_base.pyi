from collections.abc import Sequence
from typing import Any, SupportsIndex, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import ArrayLike, DTypeLike, NDArray, _ArrayLike, _DTypeLike

__all__ = ["atleast_1d", "atleast_2d", "atleast_3d", "block", "hstack", "stack", "unstack", "vstack"]

_SCT = TypeVar("_SCT", bound=np.generic)
_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])

#
@overload
def atleast_1d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_1d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_1d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def atleast_2d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_2d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_2d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def atleast_3d(arys: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def atleast_3d(arys: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_3d(*arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def vstack(tup: Sequence[_ArrayLike[_SCT]], *, dtype: None = ..., casting: np._CastingKind = ...) -> NDArray[_SCT]: ...
@overload
def vstack(tup: Sequence[ArrayLike], *, dtype: _DTypeLike[_SCT], casting: np._CastingKind = ...) -> NDArray[_SCT]: ...
@overload
def vstack(tup: Sequence[ArrayLike], *, dtype: DTypeLike = ..., casting: np._CastingKind = ...) -> NDArray[Any]: ...

#
@overload
def hstack(tup: Sequence[_ArrayLike[_SCT]], *, dtype: None = ..., casting: np._CastingKind = ...) -> NDArray[_SCT]: ...
@overload
def hstack(tup: Sequence[ArrayLike], *, dtype: _DTypeLike[_SCT], casting: np._CastingKind = ...) -> NDArray[_SCT]: ...
@overload
def hstack(tup: Sequence[ArrayLike], *, dtype: DTypeLike = ..., casting: np._CastingKind = ...) -> NDArray[Any]: ...

#
@overload
def stack(
    arrays: Sequence[_ArrayLike[_SCT]],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: np._CastingKind = ...,
) -> NDArray[_SCT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: _DTypeLike[_SCT],
    casting: np._CastingKind = ...,
) -> NDArray[_SCT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: None = ...,
    *,
    dtype: DTypeLike = ...,
    casting: np._CastingKind = ...,
) -> NDArray[Any]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = ...,
    out: _ArrayT = ...,
    *,
    dtype: DTypeLike = ...,
    casting: np._CastingKind = ...,
) -> _ArrayT: ...

#
@overload
def unstack(array: _ArrayLike[_SCT], /, *, axis: int = ...) -> tuple[NDArray[_SCT], ...]: ...
@overload
def unstack(array: ArrayLike, /, *, axis: int = ...) -> tuple[NDArray[Any], ...]: ...

#
@overload
def block(arrays: _ArrayLike[_SCT]) -> NDArray[_SCT]: ...
@overload
def block(arrays: ArrayLike) -> NDArray[Any]: ...
