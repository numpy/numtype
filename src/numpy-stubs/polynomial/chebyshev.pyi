from collections.abc import Callable, Iterable
from typing import Concatenate, Final, Literal as L, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import Self, TypeVar

import numpy as np
from _numtype import Array, Array_1d, CoComplex_1d, CoInteger_0d, _ToArray1_1d

from ._polybase import ABCPolyBase
from .legendre import (
    leg2poly as cheb2poly,
    legadd as chebadd,
    legcompanion as chebcompanion,
    legder as chebder,
    legdiv as chebdiv,
    legfit as chebfit,
    legfromroots as chebfromroots,
    leggauss as chebgauss,
    leggrid2d as chebgrid2d,
    leggrid3d as chebgrid3d,
    legint as chebint,
    legline as chebline,
    legmul as chebmul,
    legmulx as chebmulx,
    legpow as chebpow,
    legroots as chebroots,
    legsub as chebsub,
    legtrim as chebtrim,
    legval as chebval,
    legval2d as chebval2d,
    legval3d as chebval3d,
    legvander as chebvander,
    legvander2d as chebvander2d,
    legvander3d as chebvander3d,
    legweight as chebweight,
    poly2leg as poly2cheb,
)

__all__ = [
    "Chebyshev",
    "cheb2poly",
    "chebadd",
    "chebcompanion",
    "chebder",
    "chebdiv",
    "chebdomain",
    "chebfit",
    "chebfromroots",
    "chebgauss",
    "chebgrid2d",
    "chebgrid3d",
    "chebint",
    "chebinterpolate",
    "chebline",
    "chebmul",
    "chebmulx",
    "chebone",
    "chebpow",
    "chebpts1",
    "chebpts2",
    "chebroots",
    "chebsub",
    "chebtrim",
    "chebval",
    "chebval2d",
    "chebval3d",
    "chebvander",
    "chebvander2d",
    "chebvander3d",
    "chebweight",
    "chebx",
    "chebzero",
    "poly2cheb",
]

###

_T = TypeVar("_T")
_NumT = TypeVar("_NumT", bound=np.number | np.object_)

_Func: TypeAlias = Callable[Concatenate[Array_1d[np.float64], ...], _T]

###

chebdomain: Final[Array_1d[np.float64]] = ...
chebzero: Final[Array_1d[np.intp]] = ...
chebone: Final[Array_1d[np.intp]] = ...
chebx: Final[Array_1d[np.intp]] = ...

class Chebyshev(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["T"] = "T"  # pyright: ignore[reportIncompatibleMethodOverride]

    @classmethod
    def interpolate(
        cls,
        func: np.ufunc | _Func[CoComplex_1d],
        deg: CoInteger_0d,
        domain: CoComplex_1d | None = None,
        args: tuple[object, ...] = (),
    ) -> Self: ...

#
@overload
def chebinterpolate(func: np.ufunc, deg: CoInteger_0d, args: Iterable[object] = ()) -> Array[np.float64]: ...
@overload
def chebinterpolate(func: _Func[_ToArray1_1d[_NumT]], deg: CoInteger_0d, args: tuple[object, ...] = ()) -> Array_1d[_NumT]: ...

#
def chebpts1(npts: CanIndex) -> Array_1d[np.float64]: ...
def chebpts2(npts: CanIndex) -> Array_1d[np.float64]: ...

#
def _cseries_to_zseries(c: Array[_NumT]) -> Array_1d[_NumT]: ...
def _zseries_to_cseries(zs: Array[_NumT]) -> Array_1d[_NumT]: ...

#
def _zseries_mul(z1: Array[_NumT], z2: Array[_NumT]) -> Array_1d[_NumT]: ...
def _zseries_div(z1: Array[_NumT], z2: Array[_NumT]) -> Array_1d[_NumT]: ...

#
def _zseries_der(zs: Array[_NumT]) -> Array_1d[_NumT]: ...
def _zseries_int(zs: Array[_NumT]) -> Array_1d[_NumT]: ...
