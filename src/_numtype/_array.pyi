# Shape-typed array aliases

from typing import Any, Never
from typing_extensions import TypeAliasType, TypeVar

import numpy as np

from ._shape import Shape, Shape0, Shape1, Shape2, Shape3, Shape4

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

_ShapeT = TypeVar("_ShapeT", bound=Shape, default=Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_NaT = TypeVar("_NaT", default=Never)

###

Array = TypeAliasType("Array", np.ndarray[_ShapeT, np.dtype[_ScalarT]], type_params=(_ScalarT, _ShapeT))
Array0D = TypeAliasType("Array0D", np.ndarray[Shape0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array1D = TypeAliasType("Array1D", np.ndarray[Shape1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array2D = TypeAliasType("Array2D", np.ndarray[Shape2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array3D = TypeAliasType("Array3D", np.ndarray[Shape3, np.dtype[_ScalarT]], type_params=(_ScalarT,))
Array4D = TypeAliasType("Array4D", np.ndarray[Shape4, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

Matrix = TypeAliasType("Matrix", np.matrix[Shape2, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

MArray = TypeAliasType("MArray", np.ma.MaskedArray[_ShapeT, np.dtype[_ScalarT]], type_params=(_ScalarT, _ShapeT))
MArray0D = TypeAliasType("MArray0D", np.ma.MaskedArray[Shape0, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray1D = TypeAliasType("MArray1D", np.ma.MaskedArray[Shape1, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray2D = TypeAliasType("MArray2D", np.ma.MaskedArray[Shape2, np.dtype[_ScalarT]], type_params=(_ScalarT,))
MArray3D = TypeAliasType("MArray3D", np.ma.MaskedArray[Shape3, np.dtype[_ScalarT]], type_params=(_ScalarT,))

###

StringArray = TypeAliasType(
    "StringArray",
    np.ndarray[_ShapeT, np.dtypes.StringDType[_NaT]],
    type_params=(_ShapeT, _NaT),
)
StringArray0D = TypeAliasType(
    "StringArray0D",
    np.ndarray[Shape0, np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray1D = TypeAliasType(
    "StringArray1D",
    np.ndarray[Shape1, np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray2D = TypeAliasType(
    "StringArray2D",
    np.ndarray[Shape2, np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArray3D = TypeAliasType(
    "StringArray3D",
    np.ndarray[Shape3, np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
StringArrayND = TypeAliasType(
    "StringArrayND",
    np.ndarray[Shape, np.dtypes.StringDType[_NaT]],
    type_params=(_NaT,),
)
