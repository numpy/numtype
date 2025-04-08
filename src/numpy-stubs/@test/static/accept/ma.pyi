import math
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

assert_type(MAR_b.argmin(), np.intp)
assert_type(MAR_f4.argmin(), np.intp)
assert_type(MAR_f4.argmax(fill_value=math.tau, keepdims=False), np.intp)
assert_type(MAR_b.argmin(axis=0), Any)
assert_type(MAR_f4.argmin(axis=0), Any)
assert_type(MAR_b.argmin(keepdims=True), Any)
assert_type(MAR_f4.argmin(out=MAR_subclass), MaskedNDArraySubclass)
assert_type(MAR_f4.argmin(None, None, out=MAR_subclass), MaskedNDArraySubclass)

assert_type(np.ma.argmin(MAR_b), np.intp)
assert_type(np.ma.argmin(MAR_f4), np.intp)
assert_type(np.ma.argmin(MAR_f4, fill_value=math.tau, keepdims=False), np.intp)
assert_type(np.ma.argmin(MAR_b, axis=0), Any)
assert_type(np.ma.argmin(MAR_f4, axis=0), Any)
assert_type(np.ma.argmin(MAR_b, keepdims=True), Any)

assert_type(MAR_b.argmax(), np.intp)
assert_type(MAR_f4.argmax(), np.intp)
assert_type(MAR_f4.argmax(fill_value=math.tau, keepdims=False), np.intp)
assert_type(MAR_b.argmax(axis=0), Any)
assert_type(MAR_f4.argmax(axis=0), Any)
assert_type(MAR_b.argmax(keepdims=True), Any)
assert_type(MAR_f4.argmax(out=MAR_subclass), MaskedNDArraySubclass)
assert_type(MAR_f4.argmax(None, None, out=MAR_subclass), MaskedNDArraySubclass)

assert_type(np.ma.argmax(MAR_b), np.intp)
assert_type(np.ma.argmax(MAR_f4), np.intp)
assert_type(np.ma.argmax(MAR_f4, fill_value=math.tau, keepdims=False), np.intp)
assert_type(np.ma.argmax(MAR_b, axis=0), Any)
assert_type(np.ma.argmax(MAR_f4, axis=0), Any)
assert_type(np.ma.argmax(MAR_b, keepdims=True), Any)
