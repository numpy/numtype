from typing import Final, Literal as L

import _numtype as _nt
import numpy as np

from ._polybase import ABCPolyBase
from .legendre import (
    leg2poly as lag2poly,
    legadd as lagadd,
    legcompanion as lagcompanion,
    legder as lagder,
    legdiv as lagdiv,
    legfit as lagfit,
    legfromroots as lagfromroots,
    leggauss as laggauss,
    leggrid2d as laggrid2d,
    leggrid3d as laggrid3d,
    legint as lagint,
    legline as lagline,
    legmul as lagmul,
    legmulx as lagmulx,
    legpow as lagpow,
    legroots as lagroots,
    legsub as lagsub,
    legtrim as lagtrim,
    legval as lagval,
    legval2d as lagval2d,
    legval3d as lagval3d,
    legvander as lagvander,
    legvander2d as lagvander2d,
    legvander3d as lagvander3d,
    legweight as lagweight,
    poly2leg as poly2lag,
)

__all__ = [
    "Laguerre",
    "lag2poly",
    "lagadd",
    "lagcompanion",
    "lagder",
    "lagdiv",
    "lagdomain",
    "lagfit",
    "lagfromroots",
    "laggauss",
    "laggrid2d",
    "laggrid3d",
    "lagint",
    "lagline",
    "lagmul",
    "lagmulx",
    "lagone",
    "lagpow",
    "lagroots",
    "lagsub",
    "lagtrim",
    "lagval",
    "lagval2d",
    "lagval3d",
    "lagvander",
    "lagvander2d",
    "lagvander3d",
    "lagweight",
    "lagx",
    "lagzero",
    "poly2lag",
]

###

lagdomain: Final[_nt.Array1D[np.float64]] = ...
lagzero: Final[_nt.Array1D[np.intp]] = ...
lagone: Final[_nt.Array1D[np.intp]] = ...
lagx: Final[_nt.Array1D[np.intp]] = ...

class Laguerre(ABCPolyBase):
    domain: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["L"] = "L"  # pyright: ignore[reportIncompatibleMethodOverride]
