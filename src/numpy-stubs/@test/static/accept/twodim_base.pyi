from typing import Any, TypeAlias, assert_type
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Histogram2D: TypeAlias = tuple[_nt.Array2D[np.float64], _nt.Array1D[_ScalarT], _nt.Array1D[_ScalarT]]

def func1(ar: _nt.Array[_ScalarT], a: int) -> _nt.Array[_ScalarT]: ...
def func2(ar: _nt.Array[np.number], a: str) -> _nt.Array[np.float64]: ...

AR_b: _nt.Array[np.bool]
AR_u: _nt.Array[np.uint64]
AR_i: _nt.Array[np.int64]
AR_f: _nt.Array[np.float64]
AR_c: _nt.Array[np.complex128]
AR_O: _nt.Array[np.object_]

AR_LIKE_b: list[bool]
AR_LIKE_c: list[complex]

###

assert_type(np.fliplr(AR_b), _nt.Array[np.bool])
assert_type(np.fliplr(AR_LIKE_b), _nt.Array)

assert_type(np.flipud(AR_b), _nt.Array[np.bool])
assert_type(np.flipud(AR_LIKE_b), _nt.Array)

assert_type(np.eye(10), _nt.Array2D[np.float64])
assert_type(np.eye(10, M=20, dtype=np.int64), _nt.Array2D[np.int64])
assert_type(np.eye(10, k=2, dtype=int), _nt.Array2D)

assert_type(np.diag(AR_b), _nt.Array[np.bool])
assert_type(np.diag(AR_LIKE_b, k=0), _nt.Array2D)

assert_type(np.diagflat(AR_b), _nt.Array2D[np.bool])
assert_type(np.diagflat(AR_LIKE_b, k=0), _nt.Array2D)

assert_type(np.tri(10), _nt.Array2D[np.float64])
assert_type(np.tri(10, M=20, dtype=np.int64), _nt.Array2D[np.int64])
assert_type(np.tri(10, k=2, dtype=int), _nt.Array2D)

assert_type(np.tril(AR_b), _nt.Array[np.bool])
assert_type(np.tril(AR_LIKE_b, k=0), _nt.Array[np.bool])

assert_type(np.triu(AR_b), _nt.Array[np.bool])
assert_type(np.triu(AR_LIKE_b, k=0), _nt.Array[np.bool])

assert_type(np.vander(AR_b), _nt.Array2D[np.intp])
assert_type(np.vander(AR_u), _nt.Array2D[np.int_])
assert_type(np.vander(AR_i, N=2), _nt.Array2D[np.int_])
assert_type(np.vander(AR_f, increasing=True), _nt.Array2D[np.float64])
assert_type(np.vander(AR_c), _nt.Array2D[np.complex128])
assert_type(np.vander(AR_O), _nt.Array2D[np.object_])

assert_type(np.histogram2d(AR_LIKE_c, AR_LIKE_c), _Histogram2D[np.complex128 | Any])
assert_type(np.histogram2d(AR_f, AR_i), _Histogram2D[np.float64])
assert_type(np.histogram2d(AR_i, AR_f), _Histogram2D[np.float64])
assert_type(np.histogram2d(AR_f, AR_c, weights=AR_LIKE_b), _Histogram2D[np.complex128])
assert_type(np.histogram2d(AR_f, AR_c, bins=8), _Histogram2D[np.complex128])
assert_type(np.histogram2d(AR_c, AR_f, bins=(8, 5)), _Histogram2D[np.complex128])
assert_type(np.histogram2d(AR_c, AR_i, bins=AR_u), _Histogram2D[np.uint64])
assert_type(np.histogram2d(AR_c, AR_c, bins=(AR_u, AR_u)), _Histogram2D[np.uint64])
assert_type(np.histogram2d(AR_c, AR_c, bins=(AR_b, 8)), _Histogram2D[np.bool | np.complex128])

assert_type(np.mask_indices(10, func1), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])
assert_type(np.mask_indices(8, func2, "0"), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])

assert_type(np.tril_indices(10), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])
assert_type(np.triu_indices(10), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])

assert_type(np.tril_indices_from(AR_b), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])
assert_type(np.triu_indices_from(AR_b), tuple[_nt.Array1D[np.intp], _nt.Array1D[np.intp]])
