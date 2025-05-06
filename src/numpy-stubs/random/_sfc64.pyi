from typing import TypedDict, type_check_only

import _numtype as _nt
import numpy as np
from numpy.random.bit_generator import BitGenerator

__all__ = ["SFC64"]

###

@type_check_only
class _SFC64Internal(TypedDict):
    state: _nt.Array[np.uint64]

@type_check_only
class _SFC64State(TypedDict):
    bit_generator: str
    state: _SFC64Internal
    has_uint32: int
    uinteger: int

###

class SFC64(BitGenerator[_SFC64State]): ...
