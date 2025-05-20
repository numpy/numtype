# Shape-typed array aliases

from typing import Any, Never
from typing_extensions import TypeAliasType, TypeVar

import numpy as np

from ._rank import Rank0, Rank1, Rank2, Rank3, Rank4
from ._shape import AnyShape, Shape

__all__ = [
    "Array",
    "Array0D",
    "Array1D",
    "Array2D",
    "Array3D",
    "Array4D",
    "MArray",
    "MArray0D",
    "MArray1D",
    "MArray2D",
    "MArray3D",
    "Matrix",
    "StringArray",
    "StringArray0D",
    "StringArray1D",
    "StringArray2D",
    "StringArray3D",
    "StringArrayND",
]

###

# TODO: use `Shape` instead of `AnyShape` once python/mypy#19110 is fixed
_RankT = TypeVar("_RankT", bound=AnyShape, default=Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_NaT = TypeVar("_NaT", default=Never)

###

Array = TypeAliasType("Array", np.ndarray[_RankT, np.dtype[_ScalarT]], type_params=(_ScalarT, _RankT))
Array0D = TypeAliasType("Array0D", np.ndarray[Rank0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array1D = TypeAliasType("Array1D", np.ndarray[Rank1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array2D = TypeAliasType("Array2D", np.ndarray[Rank2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array3D = TypeAliasType("Array3D", np.ndarray[Rank3, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array4D = TypeAliasType("Array4D", np.ndarray[Rank4, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

Matrix = TypeAliasType("Matrix", np.matrix[Rank2, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

MArray = TypeAliasType("MArray", np.ma.MaskedArray[_RankT, np.dtype[_ScalarT]], type_params=(_ScalarT, _RankT))
MArray0D = TypeAliasType("MArray0D", np.ma.MaskedArray[Rank0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray1D = TypeAliasType("MArray1D", np.ma.MaskedArray[Rank1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray2D = TypeAliasType("MArray2D", np.ma.MaskedArray[Rank2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray3D = TypeAliasType("MArray3D", np.ma.MaskedArray[Rank3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

StringArray = TypeAliasType("StringArray", np.ndarray[_RankT, np.dtypes.StringDType[_NaT]], type_params=(_RankT, _NaT))
StringArray0D = TypeAliasType("StringArray0D", np.ndarray[Rank0, np.dtypes.StringDType[_NaT]], type_params=(_NaT,))
StringArray1D = TypeAliasType("StringArray1D", np.ndarray[Rank1, np.dtypes.StringDType[_NaT]], type_params=(_NaT,))
StringArray2D = TypeAliasType("StringArray2D", np.ndarray[Rank2, np.dtypes.StringDType[_NaT]], type_params=(_NaT,))
StringArray3D = TypeAliasType("StringArray3D", np.ndarray[Rank3, np.dtypes.StringDType[_NaT]], type_params=(_NaT,))
StringArrayND = TypeAliasType("StringArrayND", np.ndarray[Shape, np.dtypes.StringDType[_NaT]], type_params=(_NaT,))
