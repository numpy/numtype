from typing import Final, Literal as L
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

from ._polybase import ABCPolyBase
from .legendre import (
    leg2poly as herme2poly,
    legadd as hermeadd,
    legcompanion as hermecompanion,
    legder as hermeder,
    legdiv as hermediv,
    legfit as hermefit,
    legfromroots as hermefromroots,
    leggauss as hermegauss,
    leggrid2d as hermegrid2d,
    leggrid3d as hermegrid3d,
    legint as hermeint,
    legline as hermeline,
    legmul as hermemul,
    legmulx as hermemulx,
    legpow as hermepow,
    legroots as hermeroots,
    legsub as hermesub,
    legtrim as hermetrim,
    legval as hermeval,
    legval2d as hermeval2d,
    legval3d as hermeval3d,
    legvander as hermevander,
    legvander2d as hermevander2d,
    legvander3d as hermevander3d,
    legweight as hermeweight,
    poly2leg as poly2herme,
)

__all__ = [
    "HermiteE",
    "herme2poly",
    "hermeadd",
    "hermecompanion",
    "hermeder",
    "hermediv",
    "hermedomain",
    "hermefit",
    "hermefromroots",
    "hermegauss",
    "hermegrid2d",
    "hermegrid3d",
    "hermeint",
    "hermeline",
    "hermemul",
    "hermemulx",
    "hermeone",
    "hermepow",
    "hermeroots",
    "hermesub",
    "hermetrim",
    "hermeval",
    "hermeval2d",
    "hermeval3d",
    "hermevander",
    "hermevander2d",
    "hermevander3d",
    "hermeweight",
    "hermex",
    "hermezero",
    "poly2herme",
]

###

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)

###

hermedomain: Final[_nt.Array1D[np.float64]] = ...
hermezero: Final[_nt.Array1D[np.int_]] = ...
hermeone: Final[_nt.Array1D[np.int_]] = ...
hermex: Final[_nt.Array1D[np.int_]] = ...

class HermiteE(ABCPolyBase):
    domain: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["He"] = "He"  # pyright: ignore[reportIncompatibleMethodOverride]

def _normed_hermite_e_n(x: _nt.Array[np.float64, _ShapeT], n: int | np.intp) -> _nt.Array[np.float64, _ShapeT]: ...
