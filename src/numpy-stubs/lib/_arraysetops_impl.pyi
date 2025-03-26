from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import TypeVar, deprecated

import numpy as np
from _numtype import (
    Array,
    Array1D,
    CoComplex128_nd,
    CoComplex_nd,
    CoDateTime_nd,
    CoFloat64_nd,
    CoFloating_nd,
    CoInt64_nd,
    CoInteger_nd,
    CoTimeDelta_nd,
    ToBool_nd,
    ToComplex128_nd,
    ToFloat64_nd,
    ToInt_nd,
    ToObject_nd,
    _ToArray_nd,
)
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
    np.timedelta64,
    np.datetime64,
    np.object_,
    np.bytes_,
    np.str_,
    np.void,
)

_IntersectResult: TypeAlias = tuple[Array1D[_ScalarT], Array1D[np.intp], Array1D[np.intp]]

###

class UniqueAllResult(NamedTuple, Generic[_ScalarT]):
    values: Array1D[_ScalarT]
    indices: Array1D[np.intp]
    inverse_indices: Array[np.intp]
    counts: Array1D[np.intp]

class UniqueCountsResult(NamedTuple, Generic[_ScalarT]):
    values: Array1D[_ScalarT]
    counts: Array1D[np.intp]

class UniqueInverseResult(NamedTuple, Generic[_ScalarT]):
    values: Array1D[_ScalarT]
    inverse_indices: Array[np.intp]

#
@overload
def ediff1d(
    ary: ToBool_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array1D[np.int8]: ...
@overload
def ediff1d(
    ary: ToInt_nd,
    to_end: CoInteger_nd | None = None,
    to_begin: CoInteger_nd | None = None,
) -> Array1D[np.intp]: ...
@overload
def ediff1d(
    ary: ToFloat64_nd,
    to_end: CoFloating_nd | None = None,
    to_begin: CoFloating_nd | None = None,
) -> Array1D[np.float64]: ...
@overload
def ediff1d(
    ary: ToComplex128_nd,
    to_end: CoComplex_nd | None = None,
    to_begin: CoComplex_nd | None = None,
) -> Array1D[np.complex128]: ...
@overload
def ediff1d(
    ary: CoDateTime_nd,
    to_end: CoTimeDelta_nd | None = None,
    to_begin: CoTimeDelta_nd | None = None,
) -> Array1D[np.timedelta64]: ...
@overload
def ediff1d(
    ary: ToObject_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array1D[np.object_]: ...
@overload
def ediff1d(
    ary: _ToArray_nd[_CoNumberT],
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array1D[_CoNumberT]: ...
@overload
def ediff1d(
    ary: CoComplex_nd | CoTimeDelta_nd,
    to_end: CoComplex_nd | CoTimeDelta_nd | None = None,
    to_begin: CoComplex_nd | CoTimeDelta_nd | None = None,
) -> Array1D[Any]: ...

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
) -> Array[_ScalarT]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> Array[Any]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False] = False,
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[False] = False,
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    *,
    return_inverse: L[False] = False,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[False] = False,
    *,
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = False,
    *,
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: _ArrayLike[_ScalarT],
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[_ScalarT], Array[np.intp], Array[np.intp], Array[np.intp]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True],
    return_inverse: L[True],
    return_counts: L[True],
    axis: CanIndex | None = None,
    *,
    equal_nan: bool = True,
) -> tuple[Array[Any], Array[np.intp], Array[np.intp], Array[np.intp]]: ...

#
@overload
def unique_all(x: ToBool_nd) -> UniqueAllResult[np.bool]: ...
@overload
def unique_all(x: ToInt_nd) -> UniqueAllResult[np.intp]: ...
@overload
def unique_all(x: ToFloat64_nd) -> UniqueAllResult[np.float64]: ...
@overload
def unique_all(x: ToComplex128_nd) -> UniqueAllResult[np.complex128]: ...
@overload
def unique_all(x: _ArrayLike[_ScalarT]) -> UniqueAllResult[_ScalarT]: ...
@overload
def unique_all(x: ArrayLike) -> UniqueAllResult: ...

#
@overload
def unique_counts(x: ToBool_nd) -> UniqueCountsResult[np.bool]: ...
@overload
def unique_counts(x: ToInt_nd) -> UniqueCountsResult[np.intp]: ...
@overload
def unique_counts(x: ToFloat64_nd) -> UniqueCountsResult[np.float64]: ...
@overload
def unique_counts(x: ToComplex128_nd) -> UniqueCountsResult[np.complex128]: ...
@overload
def unique_counts(x: _ArrayLike[_ScalarT]) -> UniqueCountsResult[_ScalarT]: ...
@overload
def unique_counts(x: ArrayLike) -> UniqueCountsResult: ...

#
@overload
def unique_inverse(x: ToBool_nd) -> UniqueInverseResult[np.bool]: ...
@overload
def unique_inverse(x: ToInt_nd) -> UniqueInverseResult[np.intp]: ...
@overload
def unique_inverse(x: ToFloat64_nd) -> UniqueInverseResult[np.float64]: ...
@overload
def unique_inverse(x: ToComplex128_nd) -> UniqueInverseResult[np.complex128]: ...
@overload
def unique_inverse(x: _ArrayLike[_ScalarT]) -> UniqueInverseResult[_ScalarT]: ...
@overload
def unique_inverse(x: ArrayLike) -> UniqueInverseResult: ...

#
@overload
def unique_values(x: ToBool_nd) -> Array1D[np.bool]: ...
@overload
def unique_values(x: ToInt_nd) -> Array1D[np.intp]: ...
@overload
def unique_values(x: ToFloat64_nd) -> Array1D[np.float64]: ...
@overload
def unique_values(x: ToComplex128_nd) -> Array1D[np.complex128]: ...
@overload
def unique_values(x: _ArrayLike[_ScalarT]) -> Array1D[_ScalarT]: ...
@overload
def unique_values(x: ArrayLike) -> Array1D[Any]: ...

#
@overload
def intersect1d(
    ar1: ToFloat64_nd,
    ar2: CoFloat64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.float64]: ...
@overload
def intersect1d(
    ar1: ToFloat64_nd,
    ar2: CoFloat64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.float64]: ...
@overload
def intersect1d(
    ar1: CoFloat64_nd,
    ar2: ToFloat64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.float64]: ...
@overload
def intersect1d(
    ar1: CoFloat64_nd,
    ar2: ToFloat64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.float64]: ...
@overload
def intersect1d(
    ar1: ToBool_nd,
    ar2: ToBool_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.bool]: ...
@overload
def intersect1d(
    ar1: ToBool_nd,
    ar2: ToBool_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.bool]: ...
@overload
def intersect1d(
    ar1: ToInt_nd,
    ar2: CoInt64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.intp]: ...
@overload
def intersect1d(
    ar1: ToInt_nd,
    ar2: CoInt64_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.intp]: ...
@overload
def intersect1d(
    ar1: CoInt64_nd,
    ar2: ToInt_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.intp]: ...
@overload
def intersect1d(
    ar1: CoInt64_nd,
    ar2: ToInt_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.intp]: ...
@overload
def intersect1d(
    ar1: ToComplex128_nd,
    ar2: CoComplex128_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.complex128]: ...
@overload
def intersect1d(
    ar1: ToComplex128_nd,
    ar2: CoComplex128_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.complex128]: ...
@overload
def intersect1d(
    ar1: CoComplex128_nd,
    ar2: ToComplex128_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array1D[np.complex128]: ...
@overload
def intersect1d(
    ar1: CoComplex128_nd,
    ar2: ToComplex128_nd,
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
) -> Array1D[_AnyScalarT]: ...
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
) -> Array1D[Any]: ...
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
def union1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd) -> Array1D[np.float64]: ...
@overload
def union1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd) -> Array1D[np.float64]: ...
@overload
def union1d(ar1: ToBool_nd, ar2: ToBool_nd) -> Array1D[np.bool]: ...
@overload
def union1d(ar1: ToInt_nd, ar2: CoInt64_nd) -> Array1D[np.intp]: ...
@overload
def union1d(ar1: CoInt64_nd, ar2: ToInt_nd) -> Array1D[np.intp]: ...
@overload
def union1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd) -> Array1D[np.complex128]: ...
@overload
def union1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd) -> Array1D[np.complex128]: ...
@overload
def union1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT]) -> Array1D[_AnyScalarT]: ...
@overload
def union1d(ar1: ArrayLike, ar2: ArrayLike) -> Array1D[Any]: ...

#
@overload
def setxor1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd, assume_unique: bool = False) -> Array1D[np.float64]: ...
@overload
def setxor1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd, assume_unique: bool = False) -> Array1D[np.float64]: ...
@overload
def setxor1d(ar1: ToBool_nd, ar2: ToBool_nd, assume_unique: bool = False) -> Array1D[np.bool]: ...
@overload
def setxor1d(ar1: ToInt_nd, ar2: CoInt64_nd, assume_unique: bool = False) -> Array1D[np.intp]: ...
@overload
def setxor1d(ar1: CoInt64_nd, ar2: ToInt_nd, assume_unique: bool = False) -> Array1D[np.intp]: ...
@overload
def setxor1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd, assume_unique: bool = False) -> Array1D[np.complex128]: ...
@overload
def setxor1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd, assume_unique: bool = False) -> Array1D[np.complex128]: ...
@overload
def setxor1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> Array1D[_AnyScalarT]: ...
@overload
def setxor1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> Array1D[Any]: ...

#
@overload
def setdiff1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd, assume_unique: bool = False) -> Array1D[np.float64]: ...
@overload
def setdiff1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd, assume_unique: bool = False) -> Array1D[np.float64]: ...
@overload
def setdiff1d(ar1: ToBool_nd, ar2: ToBool_nd, assume_unique: bool = False) -> Array1D[np.bool]: ...
@overload
def setdiff1d(ar1: ToInt_nd, ar2: CoInt64_nd, assume_unique: bool = False) -> Array1D[np.intp]: ...
@overload
def setdiff1d(ar1: CoInt64_nd, ar2: ToInt_nd, assume_unique: bool = False) -> Array1D[np.intp]: ...
@overload
def setdiff1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd, assume_unique: bool = False) -> Array1D[np.complex128]: ...
@overload
def setdiff1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd, assume_unique: bool = False) -> Array1D[np.complex128]: ...
@overload
def setdiff1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> Array1D[_AnyScalarT]: ...
@overload
def setdiff1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> Array1D[Any]: ...

#
def isin(
    element: ArrayLike,
    test_elements: ArrayLike,
    assume_unique: bool = False,
    invert: bool = False,
    *,
    kind: L["sort", "table"] | None = None,
) -> Array[np.bool]: ...

#
@deprecated("Use 'isin' instead")
def in1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = False,
    invert: bool = False,
    *,
    kind: L["sort", "table"] | None = None,
) -> Array1D[np.bool]: ...
