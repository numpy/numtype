from typing import Any, Literal as L, TypeVar, overload

from numpy import complexfloating, floating, generic, integer
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ShapeLike,
)

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

_SCT = TypeVar("_SCT", bound=generic)

@overload
def fftshift(x: _ArrayLike[_SCT], axes: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def fftshift(x: ArrayLike, axes: _ShapeLike | None = ...) -> NDArray[Any]: ...
@overload
def ifftshift(x: _ArrayLike[_SCT], axes: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = ...) -> NDArray[Any]: ...
@overload
def fftfreq(
    n: int | integer[Any],
    d: _ArrayLikeFloat_co = ...,
    device: L["cpu"] | None = ...,
) -> NDArray[floating[Any]]: ...
@overload
def fftfreq(
    n: int | integer[Any],
    d: _ArrayLikeComplex_co = ...,
    device: L["cpu"] | None = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
@overload
def rfftfreq(
    n: int | integer[Any],
    d: _ArrayLikeFloat_co = ...,
    device: L["cpu"] | None = ...,
) -> NDArray[floating[Any]]: ...
@overload
def rfftfreq(
    n: int | integer[Any],
    d: _ArrayLikeComplex_co = ...,
    device: L["cpu"] | None = ...,
) -> NDArray[complexfloating[Any, Any]]: ...
