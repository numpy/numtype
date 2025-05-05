from typing import assert_type
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

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

assert_type(np.fliplr(AR_b), _nt.Array[np.bool])
assert_type(np.fliplr(AR_LIKE_b), _nt.Array)

assert_type(np.flipud(AR_b), _nt.Array[np.bool])
assert_type(np.flipud(AR_LIKE_b), _nt.Array)

assert_type(np.eye(10), _nt.Array[np.float64])
assert_type(np.eye(10, M=20, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.eye(10, k=2, dtype=int), _nt.Array)

assert_type(np.diag(AR_b), _nt.Array[np.bool])
assert_type(np.diag(AR_LIKE_b, k=0), _nt.Array)

assert_type(np.diagflat(AR_b), _nt.Array[np.bool])
assert_type(np.diagflat(AR_LIKE_b, k=0), _nt.Array)

assert_type(np.tri(10), _nt.Array[np.float64])
assert_type(np.tri(10, M=20, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.tri(10, k=2, dtype=int), _nt.Array)

assert_type(np.tril(AR_b), _nt.Array[np.bool])
assert_type(np.tril(AR_LIKE_b, k=0), _nt.Array[np.bool])

assert_type(np.triu(AR_b), _nt.Array[np.bool])
assert_type(np.triu(AR_LIKE_b, k=0), _nt.Array[np.bool])

assert_type(np.vander(AR_b), _nt.Array[np.intp])
assert_type(np.vander(AR_u), _nt.Array[np.signedinteger])
assert_type(np.vander(AR_i, N=2), _nt.Array[np.signedinteger])
assert_type(np.vander(AR_f, increasing=True), _nt.Array[np.floating])
assert_type(np.vander(AR_c), _nt.Array[np.complexfloating])
assert_type(np.vander(AR_O), _nt.Array[np.object_])

assert_type(
    np.histogram2d(AR_LIKE_c, AR_LIKE_c),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.complex128 | np.float64],
        _nt.Array[np.complex128 | np.float64],
    ],
)
assert_type(
    np.histogram2d(AR_i, AR_b),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(
    np.histogram2d(AR_f, AR_i),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(
    np.histogram2d(AR_i, AR_f),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(
    np.histogram2d(AR_f, AR_c, weights=AR_LIKE_b),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.complex128],
        _nt.Array[np.complex128],
    ],
)
assert_type(
    np.histogram2d(AR_f, AR_c, bins=8),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.complex128],
        _nt.Array[np.complex128],
    ],
)
assert_type(
    np.histogram2d(AR_c, AR_f, bins=(8, 5)),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.complex128],
        _nt.Array[np.complex128],
    ],
)
assert_type(
    np.histogram2d(AR_c, AR_i, bins=AR_u),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.uint64],
        _nt.Array[np.uint64],
    ],
)
assert_type(
    np.histogram2d(AR_c, AR_c, bins=(AR_u, AR_u)),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.uint64],
        _nt.Array[np.uint64],
    ],
)
assert_type(
    np.histogram2d(AR_c, AR_c, bins=(AR_b, 8)),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.bool | np.complex128],
        _nt.Array[np.bool | np.complex128],
    ],
)

assert_type(np.mask_indices(10, func1), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])
assert_type(np.mask_indices(8, func2, "0"), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])

assert_type(np.tril_indices(10), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])
assert_type(np.triu_indices(10), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])

assert_type(np.tril_indices_from(AR_b), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])
assert_type(np.triu_indices_from(AR_b), tuple[_nt.Array[np.intp], _nt.Array[np.intp]])
