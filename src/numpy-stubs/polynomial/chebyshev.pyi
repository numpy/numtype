from collections.abc import Callable, Iterable
from typing import Any, Concatenate, Final, Literal as L, overload
from typing_extensions import Self, TypeVar

import numpy as np
from _numtype import Array, Array_1d, CoComplex_1d
from numpy._typing import _IntLike_co

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
    _FuncPts,
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
    _ToNumeric_1d,
)
from .polyutils import trimcoef as chebtrim

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

_SCT = TypeVar("_SCT", bound=np.number | np.object_)
_RT = TypeVar("_RT", bound=np.number | np.bool | np.object_)

###

def _cseries_to_zseries(c: Array[_SCT]) -> Array_1d[_SCT]: ...
def _zseries_to_cseries(zs: Array[_SCT]) -> Array_1d[_SCT]: ...
def _zseries_mul(z1: Array[_SCT], z2: Array[_SCT]) -> Array_1d[_SCT]: ...
def _zseries_div(z1: Array[_SCT], z2: Array[_SCT]) -> Array_1d[_SCT]: ...
def _zseries_der(zs: Array[_SCT]) -> Array_1d[_SCT]: ...
def _zseries_int(zs: Array[_SCT]) -> Array_1d[_SCT]: ...

poly2cheb: Final[_FuncPoly2Ortho[L["poly2cheb"]]] = ...
cheb2poly: Final[_FuncUnOp[L["cheb2poly"]]] = ...

chebdomain: Final[Array_1d[np.float64]] = ...
chebzero: Final[Array_1d[np.int_]] = ...
chebone: Final[Array_1d[np.int_]] = ...
chebx: Final[Array_1d[np.int_]] = ...

chebline: Final[_FuncLine[L["chebline"]]] = ...
chebfromroots: Final[_FuncFromRoots[L["chebfromroots"]]] = ...
chebadd: Final[_FuncBinOp[L["chebadd"]]] = ...
chebsub: Final[_FuncBinOp[L["chebsub"]]] = ...
chebmulx: Final[_FuncUnOp[L["chebmulx"]]] = ...
chebmul: Final[_FuncBinOp[L["chebmul"]]] = ...
chebdiv: Final[_FuncBinOp[L["chebdiv"]]] = ...
chebpow: Final[_FuncPow[L["chebpow"]]] = ...
chebder: Final[_FuncDer[L["chebder"]]] = ...
chebint: Final[_FuncInteg[L["chebint"]]] = ...
chebval: Final[_FuncVal[L["chebval"]]] = ...
chebval2d: Final[_FuncVal2D[L["chebval2d"]]] = ...
chebval3d: Final[_FuncVal3D[L["chebval3d"]]] = ...
chebvalfromroots: Final[_FuncValFromRoots[L["chebvalfromroots"]]] = ...
chebgrid2d: Final[_FuncVal2D[L["chebgrid2d"]]] = ...
chebgrid3d: Final[_FuncVal3D[L["chebgrid3d"]]] = ...
chebvander: Final[_FuncVander[L["chebvander"]]] = ...
chebvander2d: Final[_FuncVander2D[L["chebvander2d"]]] = ...
chebvander3d: Final[_FuncVander3D[L["chebvander3d"]]] = ...
chebfit: Final[_FuncFit[L["chebfit"]]] = ...
chebcompanion: Final[_FuncCompanion[L["chebcompanion"]]] = ...
chebroots: Final[_FuncRoots[L["chebroots"]]] = ...
chebgauss: Final[_FuncGauss[L["chebgauss"]]] = ...
chebweight: Final[_FuncWeight[L["chebweight"]]] = ...
chebpts1: Final[_FuncPts[L["chebpts1"]]] = ...
chebpts2: Final[_FuncPts[L["chebpts2"]]] = ...

#
@overload
def chebinterpolate(func: np.ufunc, deg: _IntLike_co, args: tuple[()] = ...) -> Array[Any]: ...
@overload
def chebinterpolate(func: Callable[[Array[np.float64]], _RT], deg: _IntLike_co, args: tuple[()] = ...) -> Array[_RT]: ...
@overload
def chebinterpolate(
    func: Callable[Concatenate[Array[np.float64], ...], _RT],
    deg: _IntLike_co,
    args: Iterable[Any],
) -> Array[_RT]: ...

class Chebyshev(ABCPolyBase[L["T"]]):
    @overload
    @classmethod
    def interpolate(
        cls,
        func: Callable[[Array[np.float64]], _ToNumeric_1d],
        deg: _IntLike_co,
        domain: CoComplex_1d | None = ...,
        args: tuple[()] = ...,
    ) -> Self: ...
    @overload
    @classmethod
    def interpolate(
        cls,
        func: Callable[Concatenate[Array[np.float64], ...], _ToNumeric_1d],
        deg: _IntLike_co,
        domain: CoComplex_1d | None = ...,
        *,
        args: Iterable[Any],
    ) -> Self: ...
    @overload
    @classmethod
    def interpolate(
        cls,
        func: Callable[Concatenate[Array[np.float64], ...], _ToNumeric_1d],
        deg: _IntLike_co,
        domain: CoComplex_1d | None,
        args: Iterable[Any],
    ) -> Self: ...
