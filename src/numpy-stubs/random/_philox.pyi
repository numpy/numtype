from typing import TypedDict, type_check_only
from typing_extensions import Self

import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLikeInt_co
from numpy.random.bit_generator import BitGenerator, SeedSequence

__all__ = ["Philox"]

###

@type_check_only
class _PhiloxInternal(TypedDict):
    counter: npt.NDArray[np.uint64]
    key: npt.NDArray[np.uint64]

@type_check_only
class _PhiloxState(TypedDict):
    bit_generator: str
    state: _PhiloxInternal
    buffer: npt.NDArray[np.uint64]
    buffer_pos: int
    has_uint32: int
    uinteger: int

###

class Philox(BitGenerator[_PhiloxState]):
    def __init__(
        self,
        /,
        seed: _ArrayLikeInt_co | SeedSequence | None = None,
        counter: _ArrayLikeInt_co | None = None,
        key: _ArrayLikeInt_co | None = None,
    ) -> None: ...
    def jumped(self, jumps: int = ...) -> Self: ...
    def advance(self, delta: int) -> Self: ...
