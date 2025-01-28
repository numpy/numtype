from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt
from numpy._typing import _32Bit, _64Bit

_NBT1 = TypeVar("_NBT1", bound=npt.NBitBase)
_NBT2 = TypeVar("_NBT2", bound=npt.NBitBase)

def add(a: np.floating[_NBT1], b: np.integer[_NBT2]) -> np.floating[_NBT1 | _NBT2]: ...

i8: np.int64
i4: np.int32
f8: np.float64
f4: np.float32

assert_type(add(f8, i8), np.floating[_64Bit])
assert_type(add(f4, i8), np.floating[_32Bit | _64Bit])
assert_type(add(f8, i4), np.floating[_32Bit | _64Bit])
assert_type(add(f4, i4), np.floating[_32Bit])
