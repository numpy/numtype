from __future__ import annotations

from io import StringIO

import numpy as np
from numpy.lib import array_utils

FILE = StringIO()
AR = np.arange(10, dtype=np.float64)


def func(a: int) -> bool:
    return True


array_utils.byte_bounds(AR)
array_utils.byte_bounds(np.float64())

np.info(1, output=FILE)
