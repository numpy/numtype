from typing import Any, Final, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import ArrayLike, NDArray, _ArrayLike, _ArrayLikeComplex_co, _ArrayLikeFloat_co, _ShapeLike

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Device: TypeAlias = L["cpu"] | None
_IntLike: TypeAlias = int | np.integer

###

integer_types: Final[tuple[type[int], type[np.integer]]] = ...

###

@overload
def fftshift(x: _ArrayLike[_ScalarT], axes: _ShapeLike | None = None) -> NDArray[_ScalarT]: ...
@overload
def fftshift(x: _ArrayLikeFloat_co, axes: _ShapeLike | None = None) -> NDArray[np.floating]: ...
@overload
def fftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> NDArray[Any]: ...

#
@overload
def ifftshift(x: _ArrayLike[_ScalarT], axes: _ShapeLike | None = None) -> NDArray[_ScalarT]: ...
@overload
def ifftshift(x: _ArrayLikeFloat_co, axes: _ShapeLike | None = None) -> NDArray[np.floating]: ...
@overload
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> NDArray[Any]: ...

#
@overload
def fftfreq(n: _IntLike, d: _ArrayLikeFloat_co = 1.0, device: _Device = None) -> NDArray[np.floating]: ...
@overload
def fftfreq(n: _IntLike, d: _ArrayLikeComplex_co = 1.0, device: _Device = None) -> NDArray[np.inexact]: ...

#
@overload
def rfftfreq(n: _IntLike, d: _ArrayLikeFloat_co = 1.0, device: _Device = None) -> NDArray[np.floating]: ...
@overload
def rfftfreq(n: _IntLike, d: _ArrayLikeComplex_co = 1.0, device: _Device = None) -> NDArray[np.inexact]: ...
