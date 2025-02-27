from typing import TypeAlias

import numpy as np

from . import _96Bit, _128Bit

float96: TypeAlias = np.floating[_96Bit]
float128: TypeAlias = np.floating[_128Bit]
complex192: TypeAlias = np.complexfloating[_96Bit]
complex256: TypeAlias = np.complexfloating[_128Bit]
