from typing import Final, Literal as L, SupportsIndex as CanIndex, overload

import numpy as np
from _numtype import (
    Array,
    Array_1d,
    CoComplex_1d,
    CoFloating_1d,
    CoFloating_nd,
    CoInteger_1d,
    ToComplex128_1d,
    ToComplex_1d,
    ToComplex_nd,
    ToFloat64_1d,
    ToObject_1d,
    ToObject_nd,
)

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

legdomain: Final[Array_1d[np.float64]] = ...
legzero: Final[Array_1d[np.int_]] = ...
legone: Final[Array_1d[np.int_]] = ...
legx: Final[Array_1d[np.int_]] = ...

###

class Legendre(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["P"] = "P"  # pyright: ignore[reportIncompatibleMethodOverride]

###
@overload
def poly2leg(pol: ToFloat64_1d | CoInteger_1d) -> Array_1d[np.float64]: ...
@overload
def poly2leg(pol: CoFloating_1d) -> Array_1d[np.floating]: ...
@overload
def poly2leg(pol: ToComplex128_1d) -> Array_1d[np.complex128]: ...
@overload
def poly2leg(pol: ToComplex_1d) -> Array_1d[np.complexfloating]: ...
@overload
def poly2leg(pol: CoComplex_1d) -> Array_1d[np.inexact]: ...
@overload
def poly2leg(pol: ToObject_1d) -> Array_1d[np.object_]: ...

#
@overload
def leg2poly(c: ToFloat64_1d | CoInteger_1d) -> Array_1d[np.float64]: ...
@overload
def leg2poly(c: CoFloating_1d) -> Array_1d[np.floating]: ...
@overload
def leg2poly(c: ToComplex128_1d) -> Array_1d[np.complex128]: ...
@overload
def leg2poly(c: ToComplex_1d) -> Array_1d[np.complexfloating]: ...
@overload
def leg2poly(c: CoComplex_1d) -> Array_1d[np.inexact]: ...
@overload
def leg2poly(c: ToObject_1d) -> Array_1d[np.object_]: ...

#
@overload
def legweight(x: CoFloating_nd) -> Array[np.float64]: ...
@overload
def legweight(x: ToComplex_nd) -> Array[np.complex128]: ...
@overload
def legweight(x: ToObject_nd) -> Array[np.object_]: ...

#
def leggauss(deg: CanIndex) -> tuple[Array_1d[np.float64], Array_1d[np.float64]]: ...
