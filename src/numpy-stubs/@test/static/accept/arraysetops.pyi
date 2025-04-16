from typing import Any
from typing_extensions import assert_type

import _numtype as _nt
import numpy as np
from numpy.lib._arraysetops_impl import UniqueAllResult, UniqueCountsResult, UniqueInverseResult

AR_b: _nt.Array[np.bool]
AR_i_: _nt.Array[np.intp]
AR_f8: _nt.Array[np.float64]
AR_M: _nt.Array[np.datetime64]
AR_O: _nt.Array[np.object_]
AR_LIKE_i_: list[int]

###

assert_type(np.intersect1d(AR_i_, AR_i_), _nt.Array1D[np.intp])
assert_type(np.intersect1d(AR_f8, AR_i_), _nt.Array1D[np.float64])
assert_type(np.intersect1d(AR_M, AR_M, assume_unique=True), _nt.Array1D[np.datetime64])
assert_type(
    np.intersect1d(AR_f8, AR_f8, return_indices=True),
    tuple[_nt.Array1D[np.float64], _nt.Array1D[np.intp], _nt.Array1D[np.intp]],
)

assert_type(np.union1d(AR_i_, AR_i_), _nt.Array1D[np.intp])
assert_type(np.union1d(AR_f8, AR_i_), _nt.Array1D[np.float64])
assert_type(np.union1d(AR_M, AR_M), _nt.Array1D[np.datetime64])

assert_type(np.ediff1d(AR_b), _nt.Array1D[np.int8])
assert_type(np.ediff1d(AR_M), _nt.Array1D[np.timedelta64])
assert_type(np.ediff1d(AR_O), _nt.Array1D[np.object_])
assert_type(np.ediff1d(AR_i_, to_end=[1, 2, 3]), _nt.Array1D[np.intp])
assert_type(np.ediff1d(AR_LIKE_i_, to_begin=[0, 1]), _nt.Array1D[np.intp])

assert_type(np.setxor1d(AR_i_, AR_i_), _nt.Array1D[np.intp])
assert_type(np.setxor1d(AR_f8, AR_i_), _nt.Array1D[np.float64])
assert_type(np.setxor1d(AR_M, AR_M, assume_unique=True), _nt.Array1D[np.datetime64])

assert_type(np.setdiff1d(AR_i_, AR_i_), _nt.Array1D[np.intp])
assert_type(np.setdiff1d(AR_f8, AR_i_), _nt.Array1D[np.float64])
assert_type(np.setdiff1d(AR_M, AR_M, assume_unique=True), _nt.Array1D[np.datetime64])

assert_type(np.isin(AR_i_, AR_i_), _nt.Array[np.bool])
assert_type(np.isin(AR_f8, AR_i_), _nt.Array[np.bool])
assert_type(np.isin(AR_M, AR_M, assume_unique=True), _nt.Array[np.bool])
assert_type(np.isin(AR_f8, AR_LIKE_i_, invert=True), _nt.Array[np.bool])

assert_type(np.unique(AR_f8), _nt.Array[np.float64])
assert_type(np.unique(AR_f8, return_index=True), tuple[_nt.Array[np.float64], _nt.Array[np.intp]])
assert_type(np.unique(AR_f8, return_inverse=True), tuple[_nt.Array[np.float64], _nt.Array[np.intp]])
assert_type(np.unique(AR_f8, return_counts=True), tuple[_nt.Array[np.float64], _nt.Array[np.intp]])
assert_type(np.unique(AR_LIKE_i_, axis=0), _nt.Array[Any])
assert_type(np.unique(AR_LIKE_i_, return_index=True), tuple[_nt.Array[Any], _nt.Array[np.intp]])
assert_type(np.unique(AR_LIKE_i_, return_inverse=True), tuple[_nt.Array[Any], _nt.Array[np.intp]])
assert_type(np.unique(AR_LIKE_i_, return_counts=True), tuple[_nt.Array[Any], _nt.Array[np.intp]])
assert_type(
    np.unique(AR_f8, return_index=True, return_inverse=True),
    tuple[_nt.Array[np.float64], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_i_, return_index=True, return_inverse=True),
    tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_index=True, return_counts=True),
    tuple[_nt.Array[np.float64], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_i_, return_index=True, return_counts=True),
    tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_inverse=True, return_counts=True),
    tuple[_nt.Array[np.float64], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_i_, return_inverse=True, return_counts=True),
    tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_f8, return_index=True, return_inverse=True, return_counts=True),
    tuple[_nt.Array[np.float64], _nt.Array[np.intp], _nt.Array[np.intp], _nt.Array[np.intp]],
)
assert_type(
    np.unique(AR_LIKE_i_, return_index=True, return_inverse=True, return_counts=True),
    tuple[_nt.Array[Any], _nt.Array[np.intp], _nt.Array[np.intp], _nt.Array[np.intp]],
)

assert_type(np.unique_all(AR_f8), UniqueAllResult[np.float64])
assert_type(np.unique_counts(AR_f8), UniqueCountsResult[np.float64])
assert_type(np.unique_inverse(AR_f8), UniqueInverseResult[np.float64])
assert_type(np.unique_values(AR_f8), _nt.Array1D[np.float64])
assert_type(np.unique_all(AR_LIKE_i_), UniqueAllResult[np.intp])
assert_type(np.unique_counts(AR_LIKE_i_), UniqueCountsResult[np.intp])
assert_type(np.unique_inverse(AR_LIKE_i_), UniqueInverseResult[np.intp])
assert_type(np.unique_values(AR_LIKE_i_), _nt.Array1D[np.intp])
