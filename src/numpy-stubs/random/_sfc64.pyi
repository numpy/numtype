from typing import TypedDict, type_check_only

import numpy as np
from numpy._typing import NDArray, _ArrayLikeInt_co
from numpy.random.bit_generator import BitGenerator, SeedSequence

@type_check_only
class _SFC64Internal(TypedDict):
    state: NDArray[np.uint64]

@type_check_only
class _SFC64State(TypedDict):
    bit_generator: str
    state: _SFC64Internal
    has_uint32: int
    uinteger: int

class SFC64(BitGenerator):
    def __init__(self, seed: _ArrayLikeInt_co | SeedSequence | None = ...) -> None: ...
    @property
    def state(self) -> _SFC64State: ...
    @state.setter
    def state(self, state: _SFC64State, /) -> None: ...
