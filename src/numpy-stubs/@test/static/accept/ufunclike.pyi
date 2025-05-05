from typing import assert_type

import _numtype as _nt
import numpy as np
import numpy.typing as npt

AR_u: npt.NDArray[np.uint32]
AR_U: npt.NDArray[np.str_]
AR_LIKE_b: list[bool]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]

###

assert_type(np.fix(AR_u), npt.NDArray[np.uint32])
assert_type(np.fix(AR_LIKE_b), npt.NDArray[np.bool])
assert_type(np.fix(AR_LIKE_i), npt.NDArray[np.intp])
assert_type(np.fix(AR_LIKE_f), npt.NDArray[np.float64])
assert_type(np.fix(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])

assert_type(np.isposinf(AR_u), npt.NDArray[np.bool])
assert_type(np.isposinf(AR_LIKE_b), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_i), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])

assert_type(np.isneginf(AR_u), npt.NDArray[np.bool])
assert_type(np.isneginf(AR_LIKE_b), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_i), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])
