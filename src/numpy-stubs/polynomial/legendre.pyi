from typing import Final, Literal as L

import numpy as np
from _numtype import Array_1d

from ._polybase import ABCPolyBase
from ._polytypes import (
    _FuncBinOp,
    _FuncCompanion,
    _FuncDer,
    _FuncFit,
    _FuncFromRoots,
    _FuncGauss,
    _FuncInteg,
    _FuncLine,
    _FuncPoly2Ortho,
    _FuncPow,
    _FuncRoots,
    _FuncUnOp,
    _FuncVal,
    _FuncVal2D,
    _FuncVal3D,
    _FuncValFromRoots,
    _FuncVander,
    _FuncVander2D,
    _FuncVander3D,
    _FuncWeight,
)
from .polyutils import trimcoef as legtrim

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

legdomain: Final[Array_1d[np.float64]] = ...
legzero: Final[Array_1d[np.int_]] = ...
legone: Final[Array_1d[np.int_]] = ...
legx: Final[Array_1d[np.int_]] = ...

poly2leg: Final[_FuncPoly2Ortho[L["poly2leg"]]] = ...
leg2poly: Final[_FuncUnOp[L["leg2poly"]]] = ...
legline: Final[_FuncLine[L["legline"]]] = ...
legfromroots: Final[_FuncFromRoots[L["legfromroots"]]] = ...
legadd: Final[_FuncBinOp[L["legadd"]]] = ...
legsub: Final[_FuncBinOp[L["legsub"]]] = ...
legmulx: Final[_FuncUnOp[L["legmulx"]]] = ...
legmul: Final[_FuncBinOp[L["legmul"]]] = ...
legdiv: Final[_FuncBinOp[L["legdiv"]]] = ...
legpow: Final[_FuncPow[L["legpow"]]] = ...
legder: Final[_FuncDer[L["legder"]]] = ...
legint: Final[_FuncInteg[L["legint"]]] = ...
legval: Final[_FuncVal[L["legval"]]] = ...
legval2d: Final[_FuncVal2D[L["legval2d"]]] = ...
legval3d: Final[_FuncVal3D[L["legval3d"]]] = ...
legvalfromroots: Final[_FuncValFromRoots[L["legvalfromroots"]]] = ...
leggrid2d: Final[_FuncVal2D[L["leggrid2d"]]] = ...
leggrid3d: Final[_FuncVal3D[L["leggrid3d"]]] = ...
legvander: Final[_FuncVander[L["legvander"]]] = ...
legvander2d: Final[_FuncVander2D[L["legvander2d"]]] = ...
legvander3d: Final[_FuncVander3D[L["legvander3d"]]] = ...
legfit: Final[_FuncFit[L["legfit"]]] = ...
legcompanion: Final[_FuncCompanion[L["legcompanion"]]] = ...
legroots: Final[_FuncRoots[L["legroots"]]] = ...
leggauss: Final[_FuncGauss[L["leggauss"]]] = ...
legweight: Final[_FuncWeight[L["legweight"]]] = ...

class Legendre(ABCPolyBase):
    domain: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    window: Array_1d[np.float64] = ...  # pyright: ignore[reportIncompatibleMethodOverride]
    basis_name: L["P"] = "P"  # pyright: ignore[reportIncompatibleMethodOverride]
