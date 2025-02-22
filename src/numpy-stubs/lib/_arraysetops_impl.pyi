from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import TypeVar, deprecated

import numpy as np
from _numtype import (
    Array,
    Array_1d,
    CoBool_nd,
    CoComplex128_nd,
    CoComplex_nd,
    CoDateTime_nd,
    CoFloat64_nd,
    CoFloating_nd,
    CoIntP_nd,
    CoInteger_nd,
    CoTimeDelta_nd,
    ToComplex128_nd,
    ToFloat64_nd,
    ToIntP_nd,
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

_IntersectResult: TypeAlias = tuple[Array_1d[_ScalarT], Array_1d[np.intp], Array_1d[np.intp]]

###

class UniqueAllResult(NamedTuple, Generic[_ScalarT]):
    values: Array_1d[_ScalarT]
    indices: Array_1d[np.intp]
    inverse_indices: Array[np.intp]
    counts: Array_1d[np.intp]

class UniqueCountsResult(NamedTuple, Generic[_ScalarT]):
    values: Array_1d[_ScalarT]
    counts: Array_1d[np.intp]

class UniqueInverseResult(NamedTuple, Generic[_ScalarT]):
    values: Array_1d[_ScalarT]
    inverse_indices: Array[np.intp]

#
@overload
def ediff1d(  # type: ignore[overload-overlap]
    ary: ToFloat64_nd,
    to_end: CoFloating_nd | None = None,
    to_begin: CoFloating_nd | None = None,
) -> Array_1d[np.float64]: ...
@overload
def ediff1d(  # type: ignore[overload-overlap]
    ary: CoBool_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array_1d[np.int8]: ...
@overload
def ediff1d(  # type: ignore[overload-overlap]
    ary: ToIntP_nd,
    to_end: CoInteger_nd | None = None,
    to_begin: CoInteger_nd | None = None,
) -> Array_1d[np.intp]: ...
@overload
def ediff1d(  # type: ignore[overload-overlap]
    ary: ToComplex128_nd,
    to_end: CoComplex_nd | None = None,
    to_begin: CoComplex_nd | None = None,
) -> Array_1d[np.complex128]: ...
@overload
def ediff1d(  # type: ignore[overload-overlap]
    ary: CoDateTime_nd,
    to_end: CoTimeDelta_nd | None = None,
    to_begin: CoTimeDelta_nd | None = None,
) -> Array_1d[np.timedelta64]: ...
@overload
def ediff1d(
    ary: ToObject_nd,
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array_1d[np.object_]: ...
@overload
def ediff1d(
    ary: _ToArray_nd[_CoNumberT],
    to_end: ArrayLike | None = None,
    to_begin: ArrayLike | None = None,
) -> Array_1d[_CoNumberT]: ...
@overload
def ediff1d(
    ary: CoComplex_nd | CoTimeDelta_nd,
    to_end: CoComplex_nd | CoTimeDelta_nd | None = None,
    to_begin: CoComplex_nd | CoTimeDelta_nd | None = None,
) -> Array_1d[Any]: ...

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
def unique_all(x: ToFloat64_nd, /) -> UniqueAllResult[np.float64]: ...
@overload
def unique_all(x: CoBool_nd, /) -> UniqueAllResult[np.bool]: ...
@overload
def unique_all(x: ToIntP_nd, /) -> UniqueAllResult[np.intp]: ...
@overload
def unique_all(x: ToComplex128_nd, /) -> UniqueAllResult[np.complex128]: ...
@overload
def unique_all(x: _ArrayLike[_ScalarT], /) -> UniqueAllResult[_ScalarT]: ...
@overload
def unique_all(x: ArrayLike, /) -> UniqueAllResult: ...

#
@overload
def unique_counts(x: ToFloat64_nd, /) -> UniqueCountsResult[np.float64]: ...
@overload
def unique_counts(x: CoBool_nd, /) -> UniqueCountsResult[np.bool]: ...
@overload
def unique_counts(x: ToIntP_nd, /) -> UniqueCountsResult[np.intp]: ...
@overload
def unique_counts(x: ToComplex128_nd, /) -> UniqueCountsResult[np.complex128]: ...
@overload
def unique_counts(x: _ArrayLike[_ScalarT], /) -> UniqueCountsResult[_ScalarT]: ...
@overload
def unique_counts(x: ArrayLike, /) -> UniqueCountsResult: ...

#
@overload
def unique_inverse(x: ToFloat64_nd, /) -> UniqueInverseResult[np.float64]: ...
@overload
def unique_inverse(x: CoBool_nd, /) -> UniqueInverseResult[np.bool]: ...
@overload
def unique_inverse(x: ToIntP_nd, /) -> UniqueInverseResult[np.intp]: ...
@overload
def unique_inverse(x: ToComplex128_nd, /) -> UniqueInverseResult[np.complex128]: ...
@overload
def unique_inverse(x: _ArrayLike[_ScalarT], /) -> UniqueInverseResult[_ScalarT]: ...
@overload
def unique_inverse(x: ArrayLike, /) -> UniqueInverseResult: ...

#
@overload
def unique_values(x: ToFloat64_nd, /) -> Array_1d[np.float64]: ...
@overload
def unique_values(x: CoBool_nd, /) -> Array_1d[np.bool]: ...
@overload
def unique_values(x: ToIntP_nd, /) -> Array_1d[np.intp]: ...
@overload
def unique_values(x: ToComplex128_nd, /) -> Array_1d[np.complex128]: ...
@overload
def unique_values(x: _ArrayLike[_ScalarT], /) -> Array_1d[_ScalarT]: ...
@overload
def unique_values(x: ArrayLike, /) -> Array_1d[Any]: ...

#
@overload
def intersect1d(
    ar1: ToFloat64_nd,
    ar2: CoFloat64_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array_1d[np.float64]: ...
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
) -> Array_1d[np.float64]: ...
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
    ar1: CoBool_nd,
    ar2: CoBool_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array_1d[np.bool]: ...
@overload
def intersect1d(
    ar1: CoBool_nd,
    ar2: CoBool_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.bool]: ...
@overload
def intersect1d(
    ar1: ToIntP_nd,
    ar2: CoIntP_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array_1d[np.intp]: ...
@overload
def intersect1d(
    ar1: ToIntP_nd,
    ar2: CoIntP_nd,
    assume_unique: bool = False,
    *,
    return_indices: L[True],
) -> _IntersectResult[np.intp]: ...
@overload
def intersect1d(
    ar1: CoIntP_nd,
    ar2: ToIntP_nd,
    assume_unique: bool = False,
    return_indices: L[False] = False,
) -> Array_1d[np.intp]: ...
@overload
def intersect1d(
    ar1: CoIntP_nd,
    ar2: ToIntP_nd,
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
) -> Array_1d[np.complex128]: ...
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
) -> Array_1d[np.complex128]: ...
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
) -> Array_1d[_AnyScalarT]: ...
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
) -> Array_1d[Any]: ...
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
def union1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def union1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def union1d(ar1: CoBool_nd, ar2: CoBool_nd, assume_unique: bool = False) -> Array_1d[np.bool]: ...
@overload
def union1d(ar1: ToIntP_nd, ar2: CoIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def union1d(ar1: CoIntP_nd, ar2: ToIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def union1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def union1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def union1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT]) -> Array_1d[_AnyScalarT]: ...
@overload
def union1d(ar1: ArrayLike, ar2: ArrayLike) -> Array_1d[Any]: ...

#
@overload
def setxor1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def setxor1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def setxor1d(ar1: CoBool_nd, ar2: CoBool_nd, assume_unique: bool = False) -> Array_1d[np.bool]: ...
@overload
def setxor1d(ar1: ToIntP_nd, ar2: CoIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def setxor1d(ar1: CoIntP_nd, ar2: ToIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def setxor1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def setxor1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def setxor1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> Array_1d[_AnyScalarT]: ...
@overload
def setxor1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> Array_1d[Any]: ...

#
@overload
def setdiff1d(ar1: ToFloat64_nd, ar2: CoFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def setdiff1d(ar1: CoFloat64_nd, ar2: ToFloat64_nd, assume_unique: bool = False) -> Array_1d[np.float64]: ...
@overload
def setdiff1d(ar1: CoBool_nd, ar2: CoBool_nd, assume_unique: bool = False) -> Array_1d[np.bool]: ...
@overload
def setdiff1d(ar1: ToIntP_nd, ar2: CoIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def setdiff1d(ar1: CoIntP_nd, ar2: ToIntP_nd, assume_unique: bool = False) -> Array_1d[np.intp]: ...
@overload
def setdiff1d(ar1: ToComplex128_nd, ar2: CoComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def setdiff1d(ar1: CoComplex128_nd, ar2: ToComplex128_nd, assume_unique: bool = False) -> Array_1d[np.complex128]: ...
@overload
def setdiff1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = False,
) -> Array_1d[_AnyScalarT]: ...
@overload
def setdiff1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = False) -> Array_1d[Any]: ...

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
) -> Array_1d[np.bool]: ...
