from typing import TypedDict, type_check_only
from typing_extensions import Self

import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLikeInt_co
from numpy.random.bit_generator import BitGenerator

__all__ = ["MT19937"]

###

@type_check_only
class _MT19937Internal(TypedDict):
    key: npt.NDArray[np.uint32]
    pos: int

@type_check_only
class _MT19937State(TypedDict):
    bit_generator: str
    state: _MT19937Internal

###

class MT19937(BitGenerator[_MT19937State]):
    def _legacy_seeding(self, seed: _ArrayLikeInt_co) -> None: ...
    def jumped(self, jumps: int = ...) -> Self: ...
