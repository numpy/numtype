from io import StringIO
from typing import assert_type

import _numtype as _nt
import numpy as np
from numpy.lib import array_utils

AR: _nt.Array[np.float64]
AR_DICT: dict[str, _nt.Array[np.float64]]
FILE: StringIO

def func(a: int) -> bool: ...

assert_type(array_utils.byte_bounds(AR), tuple[int, int])
assert_type(array_utils.byte_bounds(np.float64()), tuple[int, int])

assert_type(np.info(1, output=FILE), None)
