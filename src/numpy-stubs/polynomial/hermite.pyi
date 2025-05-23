from typing import Final, Literal as L
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

from ._polybase import ABCPolyBase
from .legendre import (
    leg2poly as herm2poly,
    legadd as hermadd,
    legcompanion as hermcompanion,
    legder as hermder,
    legdiv as hermdiv,
    legfit as hermfit,
    legfromroots as hermfromroots,
    leggauss as hermgauss,
    leggrid2d as hermgrid2d,
    leggrid3d as hermgrid3d,
    legint as hermint,
    legline as hermline,
    legmul as hermmul,
    legmulx as hermmulx,
    legpow as hermpow,
    legroots as hermroots,
    legsub as hermsub,
    legtrim as hermtrim,
    legval as hermval,
    legval2d as hermval2d,
    legval3d as hermval3d,
    legvander as hermvander,
    legvander2d as hermvander2d,
    legvander3d as hermvander3d,
    legweight as hermweight,
    poly2leg as poly2herm,
)

__all__ = [
    "Hermite",
    "herm2poly",
    "hermadd",
    "hermcompanion",
    "hermder",
    "hermdiv",
    "hermdomain",
    "hermfit",
    "hermfromroots",
    "hermgauss",
    "hermgrid2d",
    "hermgrid3d",
    "hermint",
    "hermline",
    "hermmul",
    "hermmulx",
    "hermone",
    "hermpow",
    "hermroots",
    "hermsub",
    "hermtrim",
    "hermval",
    "hermval2d",
    "hermval3d",
    "hermvander",
    "hermvander2d",
    "hermvander3d",
    "hermweight",
    "hermx",
    "hermzero",
    "poly2herm",
]

###

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)

###

hermdomain: Final[_nt.Array1D[np.float64]] = ...
hermzero: Final[_nt.Array1D[np.intp]] = ...
hermone: Final[_nt.Array1D[np.intp]] = ...
hermx: Final[_nt.Array1D[np.intp]] = ...

class Hermite(ABCPolyBase):
    domain: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: _nt.Array1D[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["H"] = "H"  # pyright: ignore[reportIncompatibleMethodOverride]

def _normed_hermite_n(x: _nt.Array[np.float64, _ShapeT], n: int | np.intp) -> _nt.Array[np.float64, _ShapeT]: ...
