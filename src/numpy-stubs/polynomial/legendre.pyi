from typing import Final, Literal as L, SupportsIndex as CanIndex, overload

import _numtype as _nt
import numpy as np

from ._polybase import ABCPolyBase
from .polynomial import (
    polyadd as legadd,
    polycompanion as legcompanion,
    polyder as legder,
    polydiv as legdiv,
    polyfit as legfit,
    polyfromroots as legfromroots,
    polygrid2d as leggrid2d,
    polygrid3d as leggrid3d,
    polyint as legint,
    polyline as legline,
    polymul as legmul,
    polymulx as legmulx,
    polypow as legpow,
    polyroots as legroots,
    polysub as legsub,
    polytrim as legtrim,
    polyval as legval,
    polyval2d as legval2d,
    polyval3d as legval3d,
    polyvander as legvander,
    polyvander2d as legvander2d,
    polyvander3d as legvander3d,
)

__all__ = [
    "Legendre",
    "leg2poly",
    "legadd",
    "legcompanion",
    "legder",
    "legdiv",
    "legdomain",
    "legfit",
    "legfromroots",
    "leggauss",
    "leggrid2d",
    "leggrid3d",
    "legint",
    "legline",
    "legmul",
    "legmulx",
    "legone",
    "legpow",
    "legroots",
    "legsub",
    "legtrim",
    "legval",
    "legval2d",
    "legval3d",
    "legvander",
    "legvander2d",
    "legvander3d",
    "legweight",
    "legx",
    "legzero",
    "poly2leg",
]

###

legdomain: Final[_nt.Array1D[np.float64]] = ...
legzero: Final[_nt.Array1D[np.int_]] = ...
legone: Final[_nt.Array1D[np.int_]] = ...
legx: Final[_nt.Array1D[np.int_]] = ...

###

class Legendre(ABCPolyBase):
    domain: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["P"] = "P"  # pyright: ignore[reportIncompatibleMethodOverride]

###
@overload
def poly2leg(pol: _nt.ToFloat64_1d | _nt.CoInteger_1d) -> _nt.Array1D[np.float64]: ...
@overload
def poly2leg(pol: _nt.CoFloating_1d) -> _nt.Array1D[np.floating]: ...
@overload
def poly2leg(pol: _nt.ToComplex128_1d) -> _nt.Array1D[np.complex128]: ...
@overload
def poly2leg(pol: _nt.ToComplex_1d) -> _nt.Array1D[np.complexfloating]: ...
@overload
def poly2leg(pol: _nt.CoComplex_1d) -> _nt.Array1D[np.inexact]: ...
@overload
def poly2leg(pol: _nt.ToObject_1d) -> _nt.Array1D[np.object_]: ...

#
@overload
def leg2poly(c: _nt.ToFloat64_1d | _nt.CoInteger_1d) -> _nt.Array1D[np.float64]: ...
@overload
def leg2poly(c: _nt.CoFloating_1d) -> _nt.Array1D[np.floating]: ...
@overload
def leg2poly(c: _nt.ToComplex128_1d) -> _nt.Array1D[np.complex128]: ...
@overload
def leg2poly(c: _nt.ToComplex_1d) -> _nt.Array1D[np.complexfloating]: ...
@overload
def leg2poly(c: _nt.CoComplex_1d) -> _nt.Array1D[np.inexact]: ...
@overload
def leg2poly(c: _nt.ToObject_1d) -> _nt.Array1D[np.object_]: ...

#
@overload
def legweight(x: _nt.CoFloating_nd) -> _nt.Array[np.float64]: ...
@overload
def legweight(x: _nt.ToComplex_nd) -> _nt.Array[np.complex128]: ...
@overload
def legweight(x: _nt.ToObject_nd) -> _nt.Array[np.object_]: ...

#
def leggauss(deg: CanIndex) -> tuple[_nt.Array1D[np.float64], _nt.Array1D[np.float64]]: ...
