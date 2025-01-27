from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex, TypeVar, overload
from typing_extensions import deprecated

import numpy as np
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeDT64_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
)

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

_SCT = TypeVar("_SCT", bound=np.generic)
_NumberT = TypeVar("_NumberT", bound=np.number)

# Explicitly set all allowed values to prevent accidental castings to
# abstract dtypes (their common super-type).
#
# Only relevant if two or more arguments are parametrized, (e.g. `setdiff1d`)
# which could result in, for example, `int64` and `float64`producing a
# `number[_64Bit]` array
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

class UniqueAllResult(NamedTuple, Generic[_SCT]):
    values: NDArray[_SCT]
    indices: NDArray[np.int_]
    inverse_indices: NDArray[np.int_]
    counts: NDArray[np.int_]

class UniqueCountsResult(NamedTuple, Generic[_SCT]):
    values: NDArray[_SCT]
    counts: NDArray[np.int_]

class UniqueInverseResult(NamedTuple, Generic[_SCT]):
    values: NDArray[_SCT]
    inverse_indices: NDArray[np.int_]

@overload
def ediff1d(ary: _ArrayLikeBool_co, to_end: ArrayLike | None = ..., to_begin: ArrayLike | None = ...) -> NDArray[np.int8]: ...
@overload
def ediff1d(ary: _ArrayLike[_NumberT], to_end: ArrayLike | None = ..., to_begin: ArrayLike | None = ...) -> NDArray[_NumberT]: ...
@overload
def ediff1d(
    ary: _ArrayLikeDT64_co | _ArrayLikeTD64_co,
    to_end: ArrayLike | None = ...,
    to_begin: ArrayLike | None = ...,
) -> NDArray[np.timedelta64]: ...
@overload
def ediff1d(
    ary: _ArrayLikeObject_co,
    to_end: ArrayLike | None = ...,
    to_begin: ArrayLike | None = ...,
) -> NDArray[np.object_]: ...
@overload
def ediff1d(ary: _ArrayLikeNumber_co, to_end: ArrayLike | None = ..., to_begin: ArrayLike | None = ...) -> NDArray[Any]: ...

#
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[False] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> NDArray[_SCT]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> NDArray[Any]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[True] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[False] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[False] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[True] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[False] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[True] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True] = ...,
    return_inverse: L[False] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[False] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[False] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: _ArrayLike[_SCT],
    return_index: L[True] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[_SCT], NDArray[np.int_], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def unique(
    ar: ArrayLike,
    return_index: L[True] = ...,
    return_inverse: L[True] = ...,
    return_counts: L[True] = ...,
    axis: SupportsIndex | None = ...,
    *,
    equal_nan: bool = ...,
) -> tuple[NDArray[Any], NDArray[np.int_], NDArray[np.int_], NDArray[np.int_]]: ...

#
@overload
def unique_all(x: _ArrayLike[_SCT], /) -> UniqueAllResult[_SCT]: ...
@overload
def unique_all(x: ArrayLike, /) -> UniqueAllResult[Any]: ...

#
@overload
def unique_counts(x: _ArrayLike[_SCT], /) -> UniqueCountsResult[_SCT]: ...
@overload
def unique_counts(x: ArrayLike, /) -> UniqueCountsResult[Any]: ...

#
@overload
def unique_inverse(x: _ArrayLike[_SCT], /) -> UniqueInverseResult[_SCT]: ...
@overload
def unique_inverse(x: ArrayLike, /) -> UniqueInverseResult[Any]: ...

#
@overload
def unique_values(x: _ArrayLike[_SCT], /) -> NDArray[_SCT]: ...
@overload
def unique_values(x: ArrayLike, /) -> NDArray[Any]: ...

#
@overload
def intersect1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = ...,
    return_indices: L[False] = ...,
) -> NDArray[_AnyScalarT]: ...
@overload
def intersect1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = ...,
    return_indices: L[False] = ...,
) -> NDArray[Any]: ...
@overload
def intersect1d(
    ar1: _ArrayLike[_AnyScalarT],
    ar2: _ArrayLike[_AnyScalarT],
    assume_unique: bool = ...,
    return_indices: L[True] = ...,
) -> tuple[NDArray[_AnyScalarT], NDArray[np.int_], NDArray[np.int_]]: ...
@overload
def intersect1d(
    ar1: ArrayLike,
    ar2: ArrayLike,
    assume_unique: bool = ...,
    return_indices: L[True] = ...,
) -> tuple[NDArray[Any], NDArray[np.int_], NDArray[np.int_]]: ...

#
@overload
def setxor1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT], assume_unique: bool = ...) -> NDArray[_AnyScalarT]: ...
@overload
def setxor1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = ...) -> NDArray[Any]: ...

#
def isin(
    element: ArrayLike,
    test_elements: ArrayLike,
    assume_unique: bool = ...,
    invert: bool = ...,
    *,
    kind: str | None = ...,
) -> NDArray[np.bool]: ...

#
@deprecated("Use 'isin' instead")
def in1d(
    element: ArrayLike,
    test_elements: ArrayLike,
    assume_unique: bool = ...,
    invert: bool = ...,
    *,
    kind: str | None = ...,
) -> NDArray[np.bool]: ...

#
@overload
def union1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT]) -> NDArray[_AnyScalarT]: ...
@overload
def union1d(ar1: ArrayLike, ar2: ArrayLike) -> NDArray[Any]: ...
@overload
def setdiff1d(ar1: _ArrayLike[_AnyScalarT], ar2: _ArrayLike[_AnyScalarT], assume_unique: bool = ...) -> NDArray[_AnyScalarT]: ...
@overload
def setdiff1d(ar1: ArrayLike, ar2: ArrayLike, assume_unique: bool = ...) -> NDArray[Any]: ...
