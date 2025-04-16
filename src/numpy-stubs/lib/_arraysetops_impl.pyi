from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import TypeVar, deprecated

import _numtype as _nt
import numpy as np
from numpy._typing import ArrayLike, _ArrayLike

__all__ = [
    "ediff1d",
    "in1d",
    "intersect1d",
    "isin",
    "setdiff1d",
    "setxor1d",
    "union1d",
    "unique",
    "unique_all",
    "unique_counts",
    "unique_inverse",
    "unique_values",
]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_CoNumberT = TypeVar("_CoNumberT", bound=np.number | np.timedelta64 | np.object_)

_AnyScalarT = TypeVar(
    "_AnyScalarT",
    np.bool,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.float16,
    np.float32,
    np.float64,
    np.longdouble,
    np.complex64,
    np.complex128,
    np.clongdouble,
    np.object_,
    np.bytes_,
    np.str_,
    np.void,
    np.datetime64,
    np.timedelta64,
)

_IntersectResult: TypeAlias = tuple[_nt.Array1D[_ScalarT], _nt.Array1D[np.intp], _nt.Array1D[np.intp]]

###

class UniqueAllResult(NamedTuple, Generic[_ScalarT]):
    values: _nt.Array1D[_ScalarT]
    indices: _nt.Array1D[np.intp]
    inverse_indices: _nt.Array[np.intp]
    counts: _nt.Array1D[np.intp]

class UniqueCountsResult(NamedTuple, Generic[_ScalarT]):
    values: _nt.Array1D[_ScalarT]
    counts: _nt.Array1D[np.intp]

class UniqueInverseResult(NamedTuple, Generic[_ScalarT]):
    values: _nt.Array1D[_ScalarT]
    inverse_indices: _nt.Array[np.intp]

#
@overload
def ediff1d(
    ary: _nt.ToBool_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> _nt.Array1D[np.int8]: ...
@overload
def ediff1d(
    ary: _nt.ToInt_nd,
    to_end: _nt.CoInteger_nd | None = None,
    to_begin: _nt.CoInteger_nd | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload
def ediff1d(
    ary: _nt.ToFloat64_nd,
    to_end: _nt.CoFloating_nd | None = None,
    to_begin: _nt.CoFloating_nd | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload
def ediff1d(
    ary: _nt.ToComplex128_nd,
    to_end: _nt.CoComplex_nd | None = None,
    to_begin: _nt.CoComplex_nd | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload
def ediff1d(
    ary: _nt.CoDateTime_nd,
    to_end: _nt.CoTimeDelta_nd | None = None,
    to_begin: _nt.CoTimeDelta_nd | None = None,
) -> _nt.Array1D[np.timedelta64]: ...
@overload
def ediff1d(
    ary: _nt.ToObject_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> _nt.Array1D[np.object_]: ...
@overload
def ediff1d(
    ary: _nt._ToArray_nd[_CoNumberT],
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> _nt.Array1D[_CoNumberT]: ...
@overload
def ediff1d(
    ary: _nt.CoComplex_nd | _nt.CoTimeDelta_nd,
    to_end: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | None = None,
    to_begin: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | None = None,
) -> _nt.Array1D[Any]: ...

#
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> _nt.Array[_ScalarT]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> _nt.Array[Any]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    *,
    return_inverse: L[False] = False,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[_ScalarT], _nt.Array[np.intp], _nt.Array[np.intp], _nt.Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp], _nt.Array[np.intp]]: ...

#
@overload
def unique_all(x: _nt.ToBool_nd) -> UniqueAllResult[np.bool]: ...
@overload
def unique_all(x: _nt.ToInt_nd) -> UniqueAllResult[np.intp]: ...
@overload
def unique_all(x: _nt.ToFloat64_nd) -> UniqueAllResult[np.float64]: ...
@overload
def unique_all(x: _nt.ToComplex128_nd) -> UniqueAllResult[np.complex128]: ...
@overload
def unique_all(x: _ArrayLike[_ScalarT]) -> UniqueAllResult[_ScalarT]: ...
@overload
def unique_all(x: ArrayLike) -> UniqueAllResult: ...

#
@overload
def unique_counts(x: _nt.ToBool_nd) -> UniqueCountsResult[np.bool]: ...
@overload
def unique_counts(x: _nt.ToInt_nd) -> UniqueCountsResult[np.intp]: ...
@overload
def unique_counts(x: _nt.ToFloat64_nd) -> UniqueCountsResult[np.float64]: ...
@overload
def unique_counts(x: _nt.ToComplex128_nd) -> UniqueCountsResult[np.complex128]: ...
@overload
def unique_counts(x: _ArrayLike[_ScalarT]) -> UniqueCountsResult[_ScalarT]: ...
@overload
def unique_counts(x: ArrayLike) -> UniqueCountsResult: ...

#
@overload
def unique_inverse(x: _nt.ToBool_nd) -> UniqueInverseResult[np.bool]: ...
@overload
def unique_inverse(x: _nt.ToInt_nd) -> UniqueInverseResult[np.intp]: ...
@overload
def unique_inverse(x: _nt.ToFloat64_nd) -> UniqueInverseResult[np.float64]: ...
@overload
def unique_inverse(x: _nt.ToComplex128_nd) -> UniqueInverseResult[np.complex128]: ...
@overload
def unique_inverse(x: _ArrayLike[_ScalarT]) -> UniqueInverseResult[_ScalarT]: ...
@overload
def unique_inverse(x: ArrayLike) -> UniqueInverseResult: ...

#
@overload
def unique_values(x: _nt.ToBool_nd) -> _nt.Array1D[np.bool]: ...
@overload
def unique_values(x: _nt.ToInt_nd) -> _nt.Array1D[np.intp]: ...
@overload
def unique_values(x: _nt.ToFloat64_nd) -> _nt.Array1D[np.float64]: ...
@overload
def unique_values(x: _nt.ToComplex128_nd) -> _nt.Array1D[np.complex128]: ...
@overload
def unique_values(x: _ArrayLike[_ScalarT]) -> _nt.Array1D[_ScalarT]: ...
@overload
def unique_values(x: ArrayLike) -> _nt.Array1D[Any]: ...

#
@overload
def intersect1d(
    ar1: _nt.ToFloat64_nd,
    ar2: _nt.CoFloat64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.float64]: ...
@overload
def intersect1d(
    ar1: _nt.ToFloat64_nd,
    ar2: _nt.CoFloat64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.float64]: ...
@overload
def intersect1d(
    ar1: _nt.CoFloat64_nd,
    ar2: _nt.ToFloat64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.float64]: ...
@overload
def intersect1d(
    ar1: _nt.CoFloat64_nd,
    ar2: _nt.ToFloat64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.float64]: ...
@overload
def intersect1d(
    ar1: _nt.ToBool_nd,
    ar2: _nt.ToBool_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.bool]: ...
@overload
def intersect1d(
    ar1: _nt.ToBool_nd,
    ar2: _nt.ToBool_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.bool]: ...
@overload
def intersect1d(
    ar1: _nt.ToInt_nd,
    ar2: _nt.CoInt64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.intp]: ...
@overload
def intersect1d(
    ar1: _nt.ToInt_nd,
    ar2: _nt.CoInt64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.intp]: ...
@overload
def intersect1d(
    ar1: _nt.CoInt64_nd,
    ar2: _nt.ToInt_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.intp]: ...
@overload
def intersect1d(
    ar1: _nt.CoInt64_nd,
    ar2: _nt.ToInt_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.intp]: ...
@overload
def intersect1d(
    ar1: _nt.ToComplex128_nd,
    ar2: _nt.CoComplex128_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def intersect1d(
    ar1: _nt.ToComplex128_nd,
    ar2: _nt.CoComplex128_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.complex128]: ...
@overload
def intersect1d(
    ar1: _nt.CoComplex128_nd,
    ar2: _nt.ToComplex128_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def intersect1d(
    ar1: _nt.CoComplex128_nd,
    ar2: _nt.ToComplex128_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.complex128]: ...
@overload
def intersect1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[_AnyScalarT]: ...
@overload
def intersect1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[_AnyScalarT]: ...
@overload
def intersect1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> _nt.Array1D[Any]: ...
@overload
def intersect1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult: ...

#
@overload
def union1d(ar1: _nt.ToFloat64_nd, ar2: _nt.CoFloat64_nd) -> _nt.Array1D[np.float64]: ...
@overload
def union1d(ar1: _nt.CoFloat64_nd, ar2: _nt.ToFloat64_nd) -> _nt.Array1D[np.float64]: ...
@overload
def union1d(ar1: _nt.ToBool_nd, ar2: _nt.ToBool_nd) -> _nt.Array1D[np.bool]: ...
@overload
def union1d(ar1: _nt.ToInt_nd, ar2: _nt.CoInt64_nd) -> _nt.Array1D[np.intp]: ...
@overload
def union1d(ar1: _nt.CoInt64_nd, ar2: _nt.ToInt_nd) -> _nt.Array1D[np.intp]: ...
@overload
def union1d(ar1: _nt.ToComplex128_nd, ar2: _nt.CoComplex128_nd) -> _nt.Array1D[np.complex128]: ...
@overload
def union1d(ar1: _nt.CoComplex128_nd, ar2: _nt.ToComplex128_nd) -> _nt.Array1D[np.complex128]: ...
@overload
def union1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT]) -> _nt.Array1D[_AnyScalarT]: ...
@overload
def union1d(ar1: ArrayLike, ar2: ArrayLike) -> _nt.Array1D[Any]: ...

#
@overload
def setxor1d(ar1: _nt.ToFloat64_nd, ar2: _nt.CoFloat64_nd, assume_unique: bool = False) -> _nt.Array1D[np.float64]: ...
@overload
def setxor1d(ar1: _nt.CoFloat64_nd, ar2: _nt.ToFloat64_nd, assume_unique: bool = False) -> _nt.Array1D[np.float64]: ...
@overload
def setxor1d(ar1: _nt.ToBool_nd, ar2: _nt.ToBool_nd, assume_unique: bool = False) -> _nt.Array1D[np.bool]: ...
@overload
def setxor1d(ar1: _nt.ToInt_nd, ar2: _nt.CoInt64_nd, assume_unique: bool = False) -> _nt.Array1D[np.intp]: ...
@overload
def setxor1d(ar1: _nt.CoInt64_nd, ar2: _nt.ToInt_nd, assume_unique: bool = False) -> _nt.Array1D[np.intp]: ...
@overload
def setxor1d(
    ar1: _nt.ToComplex128_nd,
    ar2: _nt.CoComplex128_nd,
    assume_unique: bool = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def setxor1d(
    ar1: _nt.CoComplex128_nd,
    ar2: _nt.ToComplex128_nd,
    assume_unique: bool = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def setxor1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> _nt.Array1D[_AnyScalarT]: ...
@overload
def setxor1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> _nt.Array1D[Any]: ...

#
@overload
def setdiff1d(ar1: _nt.ToFloat64_nd, ar2: _nt.CoFloat64_nd, assume_unique: bool = False) -> _nt.Array1D[np.float64]: ...
@overload
def setdiff1d(ar1: _nt.CoFloat64_nd, ar2: _nt.ToFloat64_nd, assume_unique: bool = False) -> _nt.Array1D[np.float64]: ...
@overload
def setdiff1d(ar1: _nt.ToBool_nd, ar2: _nt.ToBool_nd, assume_unique: bool = False) -> _nt.Array1D[np.bool]: ...
@overload
def setdiff1d(ar1: _nt.ToInt_nd, ar2: _nt.CoInt64_nd, assume_unique: bool = False) -> _nt.Array1D[np.intp]: ...
@overload
def setdiff1d(ar1: _nt.CoInt64_nd, ar2: _nt.ToInt_nd, assume_unique: bool = False) -> _nt.Array1D[np.intp]: ...
@overload
def setdiff1d(
    ar1: _nt.ToComplex128_nd,
    ar2: _nt.CoComplex128_nd,
    assume_unique: bool = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def setdiff1d(
    ar1: _nt.CoComplex128_nd,
    ar2: _nt.ToComplex128_nd,
    assume_unique: bool = False,
) -> _nt.Array1D[np.complex128]: ...
@overload
def setdiff1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> _nt.Array1D[_AnyScalarT]: ...
@overload
def setdiff1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> _nt.Array1D[Any]: ...

#
def isin(
    element: ArrayLike,
    test_elements: ArrayLike,
    assume_unique: bool = False,
    invert: bool = False,
    *,
    kind: L["sort", "table"] | None = None,
) -> _nt.Array[np.bool]: ...

#
@deprecated("Use 'isin' instead")
def in1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = False,
    invert: bool = False,
    *,
    kind: L["sort", "table"] | None = None,
) -> _nt.Array1D[np.bool]: ...
