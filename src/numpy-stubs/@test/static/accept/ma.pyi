from typing import Any, TypeAlias, TypeVar
from typing_extensions import assert_type

import numpy as np
from numpy._typing import _Shape

m: np.ma.MaskedArray[tuple[int], np.dtype[np.float64]]

assert_type(m.shape, tuple[int])

assert_type(m.dtype, np.dtype[np.float64])

assert_type(int(m), int)
assert_type(float(m), float)

_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
MaskedNDArray: TypeAlias = np.ma.MaskedArray[_Shape, np.dtype[_ScalarT_co]]

class MaskedNDArraySubclass(MaskedNDArray[np.complex128]): ...

MAR_b: MaskedNDArray[np.bool]
MAR_f4: MaskedNDArray[np.float32]
MAR_i8: MaskedNDArray[np.int64]
MAR_subclass: MaskedNDArraySubclass
MAR_1d: np.ma.MaskedArray[tuple[int], np.dtype[Any]]
