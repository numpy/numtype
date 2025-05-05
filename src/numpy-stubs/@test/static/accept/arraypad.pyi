from collections.abc import Mapping
from typing import Any, SupportsIndex, assert_type

import _numtype as _nt
import numpy as np

def mode_func(
    ar: _nt.Array[np.number],
    width: tuple[int, int],
    iaxis: SupportsIndex,
    kwargs: Mapping[str, Any],
) -> None: ...

AR_i8: _nt.Array[np.int64]
AR_f8: _nt.Array[np.float64]
AR_LIKE: list[int]

assert_type(np.pad(AR_i8, (2, 3), "constant"), _nt.Array[np.int64])
assert_type(np.pad(AR_LIKE, (2, 3), "constant"), _nt.Array)

assert_type(np.pad(AR_f8, (2, 3), mode_func), _nt.Array[np.float64])
assert_type(np.pad(AR_f8, (2, 3), mode_func, a=1, b=2), _nt.Array[np.float64])
