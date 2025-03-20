from typing import Any, Final, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    Array,
    Array1D,
    CFloating32,
    CFloating64,
    CFloatingLD,
    FloatingLD,
    JustComplex,
    _CoComplex,
    _CoFloat64,
    _CoFloating,
)
from numpy._typing import ArrayLike, _ArrayLike, _ArrayLikeFloat_co, _ShapeLike

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

###

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Device: TypeAlias = L["cpu"]
_Int: TypeAlias = int | np.integer
_CFloating64Max: TypeAlias = CFloating32 | CFloating64

###

integer_types: Final[tuple[type[int], type[np.integer]]] = ...

# keep in sync with `ifftshift`
@overload
def fftshift(x: _ArrayLike[_ScalarT], axes: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def fftshift(x: _ArrayLikeFloat_co, axes: _ShapeLike | None = None) -> Array[np.floating]: ...
@overload
def fftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> Array[Any]: ...

# keep in sync with `fftshift`
@overload
def ifftshift(x: _ArrayLike[_ScalarT], axes: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def ifftshift(x: _ArrayLikeFloat_co, axes: _ShapeLike | None = None) -> Array[np.floating]: ...
@overload
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> Array[Any]: ...

# keep in sync with `rfftfreq`
@overload  # 0d +float64 -> 1d float64
def fftfreq(n: _Int, d: float | _CoFloat64 = 1.0, device: _Device | None = None) -> Array1D[np.float64]: ...
@overload  # 0d longdouble -> 1d longdouble
def fftfreq(n: _Int, d: FloatingLD, device: _Device | None = None) -> Array1D[np.longdouble]: ...
@overload  # 0d complex{64,128} -> 1d complex128
def fftfreq(n: _Int, d: _CFloating64Max | JustComplex, device: _Device | None = None) -> Array1D[np.complex128]: ...
@overload  # 0d clongdouble -> 1d clongdouble
def fftfreq(n: _Int, d: CFloatingLD, device: _Device | None = None) -> Array1D[np.clongdouble]: ...
@overload  # Nd +float64 -> Nd float64
def fftfreq(n: _Int, d: Array[_CoFloat64, _ShapeT], device: _Device | None = None) -> Array[np.float64, _ShapeT]: ...
@overload  # Nd complex{64,128} -> Nd complex128
def fftfreq(n: _Int, d: Array[_CFloating64Max, _ShapeT], device: _Device | None = None) -> Array[np.complex128, _ShapeT]: ...
@overload  # Nd longdouble -> Nd longdouble
def fftfreq(n: _Int, d: Array[FloatingLD, _ShapeT], device: _Device | None = None) -> Array[np.longdouble, _ShapeT]: ...
@overload  # Nd complex longdouble -> Nd complex longdouble
def fftfreq(n: _Int, d: Array[CFloatingLD, _ShapeT], device: _Device | None = None) -> Array[np.clongdouble, _ShapeT]: ...
@overload  # ?d +floating -> Nd floating
def fftfreq(n: _Int, d: float | _CoFloating | Array[_CoFloating] = 1.0, device: _Device | None = None) -> Array[np.floating]: ...
@overload  # ?d +complex -> Nd inexact
def fftfreq(n: _Int, d: complex | _CoComplex | Array[_CoComplex] = 1.0, device: _Device | None = None) -> Array[np.inexact]: ...

# keep in sync with `fftfreq`
@overload  # 0d +float64 -> 1d float64
def rfftfreq(n: _Int, d: float | _CoFloat64 = 1.0, device: _Device | None = None) -> Array1D[np.float64]: ...
@overload  # 0d longdouble -> 1d longdouble
def rfftfreq(n: _Int, d: FloatingLD, device: _Device | None = None) -> Array1D[np.longdouble]: ...
@overload  # 0d complex{64,128} -> 1d complex128
def rfftfreq(n: _Int, d: _CFloating64Max | JustComplex, device: _Device | None = None) -> Array1D[np.complex128]: ...
@overload  # 0d clongdouble -> 1d clongdouble
def rfftfreq(n: _Int, d: CFloatingLD, device: _Device | None = None) -> Array1D[np.clongdouble]: ...
@overload  # Nd +float64 -> Nd float64
def rfftfreq(n: _Int, d: Array[_CoFloat64, _ShapeT], device: _Device | None = None) -> Array[np.float64, _ShapeT]: ...
@overload  # Nd complex{64,128} -> Nd complex128
def rfftfreq(n: _Int, d: Array[_CFloating64Max, _ShapeT], device: _Device | None = None) -> Array[np.complex128, _ShapeT]: ...
@overload  # Nd longdouble -> Nd longdouble
def rfftfreq(n: _Int, d: Array[FloatingLD, _ShapeT], device: _Device | None = None) -> Array[np.longdouble, _ShapeT]: ...
@overload  # Nd complex longdouble -> Nd complex longdouble
def rfftfreq(n: _Int, d: Array[CFloatingLD, _ShapeT], device: _Device | None = None) -> Array[np.clongdouble, _ShapeT]: ...
@overload  # ?d +floating -> Nd floating
def rfftfreq(n: _Int, d: float | _CoFloating | Array[_CoFloating] = 1.0, device: _Device | None = None) -> Array[np.floating]: ...
@overload  # ?d +complex -> Nd inexact
def rfftfreq(n: _Int, d: complex | _CoComplex | Array[_CoComplex] = 1.0, device: _Device | None = None) -> Array[np.inexact]: ...
