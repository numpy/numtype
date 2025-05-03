from collections.abc import Callable, Iterable
from typing import Concatenate, Final, Literal as L, Self, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

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
_NumericT = TypeVar("_NumericT", bound=np.number | np.object_)

_Args: TypeAlias = Iterable[object]
_Func: TypeAlias = Callable[Concatenate[_nt.Array1D[np.float64], ...], _T]

###

chebdomain: Final[_nt.Array1D[np.float64]] = ...
chebzero: Final[_nt.Array1D[np.intp]] = ...
chebone: Final[_nt.Array1D[np.intp]] = ...
chebx: Final[_nt.Array1D[np.intp]] = ...

class Chebyshev(ABCPolyBase):
    domain: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["T"] = "T"  # pyright: ignore[reportIncompatibleMethodOverride]

    @classmethod
    def interpolate(
        cls,
        func: np.ufunc | _Func[_nt.CoComplex_1d],
        deg: _nt.CoInteger_0d,
        domain: _nt.CoComplex_1d | None = None,
        args: _Args = (),
    ) -> Self: ...

#
@overload
def chebinterpolate(func: np.ufunc, deg: _nt.CoInteger_0d, args: _Args = ()) -> _nt.Array[np.float64]: ...
@overload
def chebinterpolate(
    func: _Func[_nt._ToArray_1d[_NumericT]], deg: _nt.CoInteger_0d, args: _Args = ()
) -> _nt.Array1D[_NumericT]: ...

#
def chebpts1(npts: CanIndex) -> _nt.Array1D[np.float64]: ...
def chebpts2(npts: CanIndex) -> _nt.Array1D[np.float64]: ...

#
def _cseries_to_zseries(c: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...
def _zseries_to_cseries(zs: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...

#
def _zseries_mul(z1: _nt.Array[_NumericT], z2: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...
def _zseries_div(z1: _nt.Array[_NumericT], z2: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...

#
def _zseries_der(zs: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...
def _zseries_int(zs: _nt.Array[_NumericT]) -> _nt.Array1D[_NumericT]: ...
