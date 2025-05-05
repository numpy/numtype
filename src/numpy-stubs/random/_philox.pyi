from typing import Self, TypedDict, type_check_only

import _numtype as _nt
import numpy as np
from numpy.random.bit_generator import BitGenerator, SeedSequence

__all__ = ["Philox"]

###

@type_check_only
class _PhiloxInternal(TypedDict):
    counter: _nt.Array[np.uint64]
    key: _nt.Array[np.uint64]

@type_check_only
class _PhiloxState(TypedDict):
    bit_generator: str
    state: _PhiloxInternal
    buffer: _nt.Array[np.uint64]
    buffer_pos: int
    has_uint32: int
    uinteger: int

###

class Philox(BitGenerator[_PhiloxState]):
    def __init__(
        self,
        /,
        seed: _nt.ToInteger_nd | SeedSequence | None = None,
        counter: _nt.ToInteger_nd | None = None,
        key: _nt.ToInteger_nd | None = None,
    ) -> None: ...
    def jumped(self, jumps: int = ...) -> Self: ...
    def advance(self, delta: int) -> Self: ...
