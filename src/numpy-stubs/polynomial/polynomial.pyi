from collections.abc import Sequence
from typing import Any, Final, Literal as L, Protocol, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import Self, TypeVar, override

import numpy as np
from _numtype import (
    Array,
    Array1D,
    Array2D,
    CoComplex128_0d,
    CoComplex128_1d,
    CoComplex_0d,
    CoComplex_1d,
    CoComplex_1nd,
    CoComplex_nd,
    CoFloat64_0d,
    CoFloat64_1d,
    CoFloat64_1nd,
    CoFloat64_nd,
    CoFloating_0d,
    CoFloating_1d,
    CoFloating_1nd,
    CoFloating_nd,
    CoInt64_0d,
    CoInteger_0d,
    CoInteger_1d,
    CoInteger_nd,
    ToComplex128_0d,
    ToComplex128_1d,
    ToComplex128_nd,
    ToComplex_0d,
    ToComplex_1d,
    ToComplex_1nd,
    ToComplex_nd,
    ToFloat64_0d,
    ToFloat64_1d,
    ToFloat64_1nd,
    ToFloat64_nd,
    ToFloating_0d,
    ToFloating_1d,
    ToFloating_nd,
    ToInt_0d,
    ToObject_0d,
    ToObject_1d,
    ToObject_1nd,
    ToObject_nd,
    ToReal_1d,
    _ToArray2_1d,
    _ToArray2_nd,
)

from ._polybase import ABCPolyBase
from .polyutils import trimcoef as polytrim

__all__ = [
    "Polynomial",
    "polyadd",
    "polycompanion",
    "polyder",
    "polydiv",
    "polydomain",
    "polyfit",
    "polyfromroots",
    "polygrid2d",
    "polygrid3d",
    "polyint",
    "polyline",
    "polymul",
    "polymulx",
    "polyone",
    "polypow",
    "polyroots",
    "polysub",
    "polytrim",
    "polyval",
    "polyval2d",
    "polyval3d",
    "polyvalfromroots",
    "polyvander",
    "polyvander2d",
    "polyvander3d",
    "polyx",
    "polyzero",
]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Indices: TypeAlias = Sequence[SupportsIndex]
_ArrayAndFitResult: TypeAlias = tuple[Array[_ScalarT], Sequence[np.inexact | np.int32]]

_ToNumeric_0d: TypeAlias = ToComplex_0d | ToObject_0d | _SupportsCoefOps
_ToNumeric_1d: TypeAlias = _ToArray2_1d[np.number | np.bool | np.object_, complex | _SupportsCoefOps]
_ToNumeric_nd: TypeAlias = _ToArray2_nd[np.number | np.bool | np.object_, complex | _SupportsCoefOps]

# compatible with e.g. int, float, complex, Decimal, Fraction, and ABCPolyBase
@type_check_only
class _SupportsCoefOps(Protocol):
    @override
    def __eq__(self, x: object, /) -> bool: ...
    @override
    def __ne__(self, x: object, /) -> bool: ...
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __add__(self, x: Any, /) -> Self: ...
    def __sub__(self, x: Any, /) -> Self: ...
    def __mul__(self, x: Any, /) -> Self: ...
    def __pow__(self, x: Any, /) -> Self | float: ...
    def __radd__(self, x: Any, /) -> Self: ...
    def __rsub__(self, x: Any, /) -> Self: ...
    def __rmul__(self, x: Any, /) -> Self: ...

###

polydomain: Final[Array1D[np.float64]] = ...
polyzero: Final[Array1D[np.intp]] = ...
polyone: Final[Array1D[np.intp]] = ...
polyx: Final[Array1D[np.intp]] = ...

###

class Polynomial(ABCPolyBase):
    domain: Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: None = None  # pyright: ignore[reportIncompatibleMethodOverride]

###

#
@overload
def polyline(off: ToInt_0d, scl: CoInt64_0d) -> Array1D[np.intp]: ...
@overload
def polyline(off: CoInt64_0d, scl: ToInt_0d) -> Array1D[np.intp]: ...
@overload
def polyline(off: CoInteger_0d, scl: CoInteger_0d) -> Array1D[np.integer]: ...
@overload
def polyline(off: ToFloat64_0d, scl: CoFloat64_0d) -> Array1D[np.float64]: ...
@overload
def polyline(off: CoFloat64_0d, scl: ToFloat64_0d) -> Array1D[np.float64]: ...
@overload
def polyline(off: ToFloating_0d, scl: CoFloating_0d) -> Array1D[np.floating]: ...
@overload
def polyline(off: CoFloating_0d, scl: ToFloating_0d) -> Array1D[np.floating]: ...
@overload
def polyline(off: ToComplex128_0d, scl: CoComplex128_0d) -> Array1D[np.complex128]: ...
@overload
def polyline(off: CoComplex128_0d, scl: ToComplex128_0d) -> Array1D[np.complex128]: ...
@overload
def polyline(off: ToComplex_0d, scl: CoComplex_0d) -> Array1D[np.complexfloating]: ...
@overload
def polyline(off: CoComplex_0d, scl: ToComplex_0d) -> Array1D[np.complexfloating]: ...
@overload
def polyline(off: CoComplex_0d, scl: CoComplex_0d) -> Array1D[np.number]: ...
@overload
def polyline(off: ToObject_0d, scl: ToObject_0d) -> Array1D[np.object_]: ...

#
@overload
def polyfromroots(roots: ToFloat64_1d | CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polyfromroots(roots: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polyfromroots(roots: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polyfromroots(roots: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polyfromroots(roots: CoComplex_1d) -> Array1D[np.inexact]: ...
@overload
def polyfromroots(roots: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polyadd(c1: CoInteger_1d, c2: CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polyadd(c1: ToFloat64_1d, c2: CoFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polyadd(c1: CoFloat64_1d, c2: ToFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polyadd(c1: ToReal_1d, c2: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polyadd(c1: CoFloating_1d, c2: ToReal_1d) -> Array1D[np.floating]: ...
@overload
def polyadd(c1: ToComplex128_1d, c2: CoComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polyadd(c1: CoComplex128_1d, c2: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polyadd(c1: ToComplex_1d, c2: CoComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polyadd(c1: CoComplex_1d, c2: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polyadd(c1: ToObject_1d, c2: _ToNumeric_1d) -> Array1D[np.object_]: ...
@overload
def polyadd(c1: _ToNumeric_1d, c2: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polysub(c1: CoInteger_1d, c2: CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polysub(c1: ToFloat64_1d, c2: CoFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polysub(c1: CoFloat64_1d, c2: ToFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polysub(c1: ToReal_1d, c2: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polysub(c1: CoFloating_1d, c2: ToReal_1d) -> Array1D[np.floating]: ...
@overload
def polysub(c1: ToComplex128_1d, c2: CoComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polysub(c1: CoComplex128_1d, c2: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polysub(c1: ToComplex_1d, c2: CoComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polysub(c1: CoComplex_1d, c2: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polysub(c1: ToObject_1d, c2: _ToNumeric_1d) -> Array1D[np.object_]: ...
@overload
def polysub(c1: _ToNumeric_1d, c2: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polymulx(c: ToFloat64_1d | CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polymulx(c: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polymulx(c: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polymulx(c: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polymulx(c: CoComplex_1d) -> Array1D[np.inexact]: ...
@overload
def polymulx(c: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polymul(c1: CoInteger_1d, c2: CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polymul(c1: ToFloat64_1d, c2: CoFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polymul(c1: CoFloat64_1d, c2: ToFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polymul(c1: ToReal_1d, c2: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polymul(c1: CoFloating_1d, c2: ToReal_1d) -> Array1D[np.floating]: ...
@overload
def polymul(c1: ToComplex128_1d, c2: CoComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polymul(c1: CoComplex128_1d, c2: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polymul(c1: ToComplex_1d, c2: CoComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polymul(c1: CoComplex_1d, c2: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polymul(c1: ToObject_1d, c2: _ToNumeric_1d) -> Array1D[np.object_]: ...
@overload
def polymul(c1: _ToNumeric_1d, c2: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polydiv(c1: CoInteger_1d, c2: CoInteger_1d) -> Array1D[np.float64]: ...
@overload
def polydiv(c1: ToFloat64_1d, c2: CoFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polydiv(c1: CoFloat64_1d, c2: ToFloat64_1d) -> Array1D[np.float64]: ...
@overload
def polydiv(c1: ToReal_1d, c2: CoFloating_1d) -> Array1D[np.floating]: ...
@overload
def polydiv(c1: CoFloating_1d, c2: ToReal_1d) -> Array1D[np.floating]: ...
@overload
def polydiv(c1: ToComplex128_1d, c2: CoComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polydiv(c1: CoComplex128_1d, c2: ToComplex128_1d) -> Array1D[np.complex128]: ...
@overload
def polydiv(c1: ToComplex_1d, c2: CoComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polydiv(c1: CoComplex_1d, c2: ToComplex_1d) -> Array1D[np.complexfloating]: ...
@overload
def polydiv(c1: ToObject_1d, c2: _ToNumeric_1d) -> Array1D[np.object_]: ...
@overload
def polydiv(c1: _ToNumeric_1d, c2: ToObject_1d) -> Array1D[np.object_]: ...

#
@overload
def polypow(c: ToFloat64_1d | CoInteger_nd, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.float64]: ...
@overload
def polypow(c: CoFloating_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.floating]: ...
@overload
def polypow(c: ToComplex128_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.complex128]: ...
@overload
def polypow(c: ToComplex_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.complexfloating]: ...
@overload
def polypow(c: CoComplex_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.inexact]: ...
@overload
def polypow(c: ToObject_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array1D[np.object_]: ...

#
@overload
def polyder(
    c: ToFloat64_nd | CoInteger_nd,
    m: SupportsIndex = 1,
    scl: CoFloating_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.float64]: ...
@overload
def polyder(c: ToFloating_nd, m: SupportsIndex = 1, scl: CoFloating_0d = 1, axis: SupportsIndex = 0) -> Array[np.floating]: ...
@overload
def polyder(c: ToComplex128_nd, m: SupportsIndex = 1, scl: CoComplex_0d = 1, axis: SupportsIndex = 0) -> Array[np.complex128]: ...
@overload
def polyder(
    c: ToComplex_nd,
    m: SupportsIndex = 1,
    scl: CoComplex_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.complexfloating]: ...
@overload
def polyder(c: CoComplex_nd, m: SupportsIndex = 1, scl: CoComplex_0d = 1, axis: SupportsIndex = 0) -> Array[np.inexact]: ...
@overload
def polyder(c: ToObject_nd, m: SupportsIndex = 1, scl: _ToNumeric_0d = 1, axis: SupportsIndex = 0) -> Array[np.object_]: ...

#
@overload
def polyint(
    c: ToFloat64_nd | CoInteger_nd,
    m: SupportsIndex = 1,
    k: CoFloat64_0d | CoFloat64_1d = [],
    lbnd: CoFloating_0d = 0,
    scl: CoFloating_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.float64]: ...
@overload
def polyint(
    c: CoFloating_nd,
    m: SupportsIndex = 1,
    k: CoFloating_0d | CoFloating_1d = [],
    lbnd: CoFloating_0d = 0,
    scl: CoFloating_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.floating]: ...
@overload
def polyint(
    c: ToComplex_nd,
    m: SupportsIndex = 1,
    k: CoComplex_0d | CoComplex_1d = [],
    lbnd: CoComplex_0d = 0,
    scl: CoComplex_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.complexfloating]: ...
@overload
def polyint(
    c: CoComplex_nd,
    m: SupportsIndex,
    k: ToComplex_0d | ToComplex_1d,
    lbnd: CoComplex_0d = 0,
    scl: CoComplex_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.complexfloating]: ...
@overload
def polyint(
    c: CoComplex_nd,
    m: SupportsIndex = 1,
    *,
    k: ToComplex_0d | ToComplex_1d,
    lbnd: CoComplex_0d = 0,
    scl: CoComplex_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.complexfloating]: ...
@overload
def polyint(
    c: ToObject_nd,
    m: SupportsIndex = 1,
    k: _ToNumeric_0d | _ToNumeric_1d = [],
    lbnd: _ToNumeric_0d = 0,
    scl: _ToNumeric_0d = 1,
    axis: SupportsIndex = 0,
) -> Array[np.object_]: ...

#
@overload
def polyvalfromroots(x: CoFloating_0d, r: CoFloating_0d, tensor: bool = True) -> np.floating: ...
@overload
def polyvalfromroots(x: CoFloating_1nd, r: CoFloating_nd, tensor: bool = True) -> Array[np.floating]: ...
@overload
def polyvalfromroots(x: CoFloating_nd, r: CoFloating_1nd, tensor: bool = True) -> Array[np.floating]: ...
@overload
def polyvalfromroots(x: ToComplex_0d, r: CoComplex_0d, tensor: bool = True) -> np.complexfloating: ...
@overload
def polyvalfromroots(x: CoComplex_0d, r: ToComplex_0d, tensor: bool = True) -> np.complexfloating: ...
@overload
def polyvalfromroots(x: ToComplex_1nd, r: CoComplex_nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyvalfromroots(x: ToComplex_nd, r: CoComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyvalfromroots(x: CoComplex_1nd, r: ToComplex_nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyvalfromroots(x: CoComplex_nd, r: ToComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyvalfromroots(x: ToObject_1nd, r: _ToNumeric_nd, tensor: bool = True) -> Array[np.object_]: ...
@overload
def polyvalfromroots(x: _ToNumeric_nd, r: ToObject_1nd, tensor: bool = True) -> Array[np.object_]: ...

#
@overload
def polyval(x: CoInteger_0d, c: CoInteger_1d, tensor: bool = True) -> np.float64: ...
@overload
def polyval(x: ToFloat64_0d, c: CoFloat64_1d, tensor: bool = True) -> np.float64: ...
@overload
def polyval(x: CoFloat64_0d, c: ToFloat64_1d, tensor: bool = True) -> np.float64: ...
@overload
def polyval(x: CoFloating_0d, c: CoFloating_1d, tensor: bool = True) -> np.floating: ...
@overload
def polyval(x: ToComplex_0d, c: CoComplex_1d, tensor: bool = True) -> np.complexfloating: ...
@overload
def polyval(x: CoComplex_0d, c: ToComplex_1d, tensor: bool = True) -> np.complexfloating: ...
@overload
def polyval(x: ToFloat64_1nd, c: CoFloat64_1nd, tensor: bool = True) -> Array[np.float64]: ...
@overload
def polyval(x: CoFloat64_1nd, c: ToFloat64_1nd, tensor: bool = True) -> Array[np.float64]: ...
@overload
def polyval(x: CoFloating_1nd, c: CoFloating_1nd, tensor: bool = True) -> Array[np.floating]: ...
@overload
def polyval(x: ToComplex_1nd, c: CoComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyval(x: CoComplex_1nd, c: ToComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...
@overload
def polyval(x: ToObject_1nd, c: _ToNumeric_nd, tensor: bool = True) -> Array[np.object_]: ...
@overload
def polyval(x: _ToNumeric_nd, c: ToObject_1nd, tensor: bool = True) -> Array[np.object_]: ...

#
@overload
def polyval2d(x: CoInteger_0d, y: CoInteger_0d, c: CoInteger_1d) -> np.float64: ...
@overload
def polyval2d(x: ToFloat64_0d, y: CoFloat64_0d, c: CoFloat64_1d) -> np.float64: ...
@overload
def polyval2d(x: CoFloat64_0d, y: ToFloat64_0d, c: CoFloat64_1d) -> np.float64: ...
@overload
def polyval2d(x: CoFloat64_0d, y: CoFloat64_0d, c: ToFloat64_1d) -> np.float64: ...
@overload
def polyval2d(x: CoFloating_0d, y: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...
@overload
def polyval2d(x: ToComplex_0d, y: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polyval2d(x: CoComplex_0d, y: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polyval2d(x: CoComplex_0d, y: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...
@overload
def polyval2d(x: ToFloat64_1nd, y: CoFloat64_nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: CoFloat64_1nd, y: ToFloat64_nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: CoFloat64_1nd, y: CoFloat64_nd, c: ToFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: ToFloat64_nd, y: CoFloat64_1nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: CoFloat64_nd, y: ToFloat64_1nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: CoFloat64_nd, y: CoFloat64_1nd, c: ToFloat64_1nd) -> Array[np.float64]: ...
@overload
def polyval2d(x: CoFloating_1nd, y: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval2d(x: CoFloating_nd, y: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval2d(x: ToComplex_1nd, y: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: CoComplex_1nd, y: ToComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: CoComplex_1nd, y: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: ToComplex_nd, y: CoComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: CoComplex_nd, y: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: CoComplex_nd, y: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval2d(x: ToObject_1nd, y: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polyval2d(x: _ToNumeric_nd, y: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...

# keep in sync with *val2d
@overload
def polygrid2d(x: CoInteger_0d, y: CoInteger_0d, c: CoInteger_1d) -> np.float64: ...
@overload
def polygrid2d(x: ToFloat64_0d, y: CoFloat64_0d, c: CoFloat64_1d) -> np.float64: ...
@overload
def polygrid2d(x: CoFloat64_0d, y: ToFloat64_0d, c: CoFloat64_1d) -> np.float64: ...
@overload
def polygrid2d(x: CoFloat64_0d, y: CoFloat64_0d, c: ToFloat64_1d) -> np.float64: ...
@overload
def polygrid2d(x: CoFloating_0d, y: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...
@overload
def polygrid2d(x: ToComplex_0d, y: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polygrid2d(x: CoComplex_0d, y: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polygrid2d(x: CoComplex_0d, y: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...
@overload
def polygrid2d(x: ToFloat64_1nd, y: CoFloat64_nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: CoFloat64_1nd, y: ToFloat64_nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: CoFloat64_1nd, y: CoFloat64_nd, c: ToFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: ToFloat64_nd, y: CoFloat64_1nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: CoFloat64_nd, y: ToFloat64_1nd, c: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: CoFloat64_nd, y: CoFloat64_1nd, c: ToFloat64_1nd) -> Array[np.float64]: ...
@overload
def polygrid2d(x: CoFloating_1nd, y: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polygrid2d(x: CoFloating_nd, y: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polygrid2d(x: ToComplex_1nd, y: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: CoComplex_1nd, y: ToComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: CoComplex_1nd, y: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: ToComplex_nd, y: CoComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: CoComplex_nd, y: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: CoComplex_nd, y: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid2d(x: ToObject_1nd, y: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polygrid2d(x: _ToNumeric_nd, y: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...

#
@overload
def polyval3d(x: CoFloating_0d, y: CoFloating_0d, z: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...
@overload
def polyval3d(x: CoFloating_1nd, y: CoFloating_nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval3d(x: CoFloating_nd, y: CoFloating_1nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval3d(x: CoFloating_nd, y: CoFloating_nd, z: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval3d(x: ToComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polyval3d(x: CoComplex_0d, y: ToComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polyval3d(x: CoComplex_0d, y: CoComplex_0d, z: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polyval3d(x: CoComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...
@overload
def polyval3d(x: ToComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: CoComplex_nd, y: ToComplex_1nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: CoComplex_nd, y: CoComplex_nd, z: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: CoComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: CoComplex_nd, y: CoComplex_1nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: CoComplex_nd, y: CoComplex_nd, z: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval3d(x: ToObject_1nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polyval3d(x: ToObject_1nd, y: ToObject_1nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polyval3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polyval3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: ToObject_1nd) -> Array[np.object_]: ...

# keep in sync with *val3d
@overload
def polygrid3d(x: CoFloating_0d, y: CoFloating_0d, z: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...
@overload
def polygrid3d(x: CoFloating_1nd, y: CoFloating_nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polygrid3d(x: CoFloating_nd, y: CoFloating_1nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polygrid3d(x: CoFloating_nd, y: CoFloating_nd, z: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polygrid3d(x: ToComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polygrid3d(x: CoComplex_0d, y: ToComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polygrid3d(x: CoComplex_0d, y: CoComplex_0d, z: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...
@overload
def polygrid3d(x: CoComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...
@overload
def polygrid3d(x: ToComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: CoComplex_nd, y: ToComplex_1nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: CoComplex_nd, y: CoComplex_nd, z: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: CoComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: CoComplex_nd, y: CoComplex_1nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: CoComplex_nd, y: CoComplex_nd, z: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polygrid3d(x: ToObject_1nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polygrid3d(x: ToObject_1nd, y: ToObject_1nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polygrid3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
@overload
def polygrid3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: ToObject_1nd) -> Array[np.object_]: ...

#
@overload
def polyvander(x: ToFloat64_nd | CoInteger_nd, deg: SupportsIndex) -> Array[np.float64]: ...
@overload
def polyvander(x: CoFloating_nd, deg: SupportsIndex) -> Array[np.floating]: ...
@overload
def polyvander(x: ToComplex128_nd, deg: SupportsIndex) -> Array[np.complex128]: ...
@overload
def polyvander(x: ToComplex_nd, deg: SupportsIndex) -> Array[np.complexfloating]: ...
@overload
def polyvander(x: CoComplex_nd, deg: SupportsIndex) -> Array[np.inexact]: ...
@overload
def polyvander(x: ToObject_nd, deg: SupportsIndex) -> Array[np.object_]: ...
@overload
def polyvander(x: _ToNumeric_nd, deg: SupportsIndex) -> Array[Any]: ...

#
@overload
def polyvander2d(x: CoInteger_nd, y: CoInteger_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander2d(x: ToFloat64_nd, y: CoFloat64_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander2d(x: CoFloat64_nd, y: ToFloat64_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander2d(x: CoFloating_nd, y: CoFloating_nd, deg: _Indices) -> Array[np.floating]: ...
@overload
def polyvander2d(x: ToComplex_nd, y: CoComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...
@overload
def polyvander2d(x: CoComplex_nd, y: ToComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...
@overload
def polyvander2d(x: ToObject_nd, y: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
@overload
def polyvander2d(x: _ToNumeric_nd, y: ToObject_nd, deg: _Indices) -> Array[np.object_]: ...
@overload
def polyvander2d(x: _ToNumeric_nd, y: _ToNumeric_nd, deg: _Indices) -> Array[Any]: ...

#
@overload
def polyvander3d(x: CoInteger_nd, y: CoInteger_nd, z: CoInteger_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander3d(x: ToFloat64_nd, y: CoFloat64_nd, z: CoFloat64_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander3d(x: CoFloat64_nd, y: ToFloat64_nd, z: CoFloat64_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander3d(x: CoFloat64_nd, y: CoFloat64_nd, z: ToFloat64_nd, deg: _Indices) -> Array[np.float64]: ...
@overload
def polyvander3d(x: CoFloating_nd, y: CoFloating_nd, z: CoFloating_nd, deg: _Indices) -> Array[np.floating]: ...
@overload
def polyvander3d(x: ToComplex_nd, y: CoComplex_nd, z: CoComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...
@overload
def polyvander3d(x: CoComplex_nd, y: ToComplex_nd, z: CoComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...
@overload
def polyvander3d(x: CoComplex_nd, y: CoComplex_nd, z: ToComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...
@overload
def polyvander3d(x: ToObject_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
@overload
def polyvander3d(x: _ToNumeric_nd, y: ToObject_nd, z: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
@overload
def polyvander3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: ToObject_nd, deg: _Indices) -> Array[np.object_]: ...
@overload
def polyvander3d(x: _ToNumeric_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, deg: _Indices) -> Array[Any]: ...

#
@overload
def polyfit(
    x: ToFloat64_1d | CoInteger_1d,
    y: ToFloat64_nd | CoInteger_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    full: L[False] = False,
    w: ToFloating_1d | None = None,
) -> Array[np.float64]: ...
@overload
def polyfit(
    x: ToFloat64_1d | CoInteger_1d,
    y: ToFloat64_nd | CoInteger_nd,
    deg: int | CoInteger_1d,
    rcond: float | None,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.float64]: ...
@overload
def polyfit(
    x: ToFloat64_1d | CoInteger_1d,
    y: ToFloat64_nd | CoInteger_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.float64]: ...
@overload
def polyfit(
    x: ToFloating_1d,
    y: CoFloating_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    full: L[False] = False,
    w: ToFloating_1d | None = None,
) -> Array[np.floating]: ...
@overload
def polyfit(
    x: ToFloating_1d,
    y: CoFloating_nd,
    deg: int | CoInteger_1d,
    rcond: float | None,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.floating]: ...
@overload
def polyfit(
    x: ToFloating_1d,
    y: CoFloating_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.floating]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    full: L[False] = False,
    w: ToFloating_1d | None = None,
) -> Array[np.complexfloating]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    full: L[False] = False,
    w: ToFloating_1d | None = None,
) -> Array[np.complexfloating]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.complexfloating]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.complexfloating]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.complexfloating]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.complexfloating]: ...
@overload
def polyfit(
    x: ToObject_1d,
    y: _ToNumeric_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    full: L[False] = False,
    w: ToFloating_1d | None = None,
) -> Array[np.object_]: ...
@overload
def polyfit(
    x: _ToNumeric_1d,
    y: ToObject_nd,
    deg: int | CoInteger_1d,
    rcond: float | None,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.object_]: ...
@overload
def polyfit(
    x: ToObject_1d,
    y: _ToNumeric_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.object_]: ...
@overload
def polyfit(
    x: _ToNumeric_1d,
    y: ToObject_nd,
    deg: int | CoInteger_1d,
    rcond: float | None = None,
    *,
    full: L[True],
    w: ToFloating_1d | None = None,
) -> _ArrayAndFitResult[np.object_]: ...

#
@overload
def polycompanion(c: CoFloating_1d) -> Array2D[np.float64]: ...
@overload
def polycompanion(c: ToComplex_1d) -> Array2D[np.complex128]: ...
@overload
def polycompanion(c: ToObject_1d) -> Array2D[np.object_]: ...

#
@overload
def polyroots(c: CoFloating_1d) -> Array1D[np.float64]: ...
@overload
def polyroots(c: ToComplex_1d) -> Array1D[np.complex128]: ...
@overload
def polyroots(c: ToObject_1d) -> Array1D[np.object_]: ...
