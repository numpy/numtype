from typing import Any, Literal as L, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import ArrayLike, NDArray, _ArrayLike, _ArrayLikeComplex_co, _ArrayLikeFloat_co, _ShapeLike

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

_SCT = TypeVar("_SCT", bound=np.generic)

#
@overload
def fftshift(x: _ArrayLike[_SCT], axes: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def fftshift(x: ArrayLike, axes: _ShapeLike | None = ...) -> NDArray[Any]: ...

#
@overload
def ifftshift(x: _ArrayLike[_SCT], axes: _ShapeLike | None = ...) -> NDArray[_SCT]: ...
@overload
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = ...) -> NDArray[Any]: ...

#
@overload
def fftfreq(n: int | np.integer, d: _ArrayLikeFloat_co = ..., device: L["cpu"] | None = ...) -> NDArray[np.floating]: ...
@overload
def fftfreq(n: int | np.integer, d: _ArrayLikeComplex_co = ..., device: L["cpu"] | None = ...) -> NDArray[np.inexact]: ...

#
@overload
def rfftfreq(n: int | np.integer, d: _ArrayLikeFloat_co = ..., device: L["cpu"] | None = ...) -> NDArray[np.floating]: ...
@overload
def rfftfreq(n: int | np.integer, d: _ArrayLikeComplex_co = ..., device: L["cpu"] | None = ...) -> NDArray[np.inexact]: ...
