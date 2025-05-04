from typing import TypeAlias, TypeVar, assert_type

import _numtype as _nt
import numpy as np

m: np.ma.MaskedArray[tuple[int], np.dtype[np.float64]]

assert_type(m.shape, tuple[int])

assert_type(m.dtype, np.dtype[np.float64])

assert_type(int(m), int)
assert_type(float(m), float)

_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
MaskedNDArray: TypeAlias = _nt.MArray[_ScalarT_co]

class MaskedNDArraySubclass(MaskedNDArray[np.complex128]): ...

MAR_b: MaskedNDArray[np.bool]
MAR_f4: MaskedNDArray[np.float32]
MAR_i8: MaskedNDArray[np.int64]
MAR_subclass: MaskedNDArraySubclass
MAR_1d: _nt.MArray0D
