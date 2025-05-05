from typing import assert_type

import _numtype as _nt
import numpy as np

AR_u: _nt.Array[np.uint32]
AR_U: _nt.Array[np.str_]
AR_LIKE_b: list[bool]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]

###

assert_type(np.fix(AR_u), _nt.Array[np.uint32])
assert_type(np.fix(AR_LIKE_b), _nt.Array[np.bool])
assert_type(np.fix(AR_LIKE_i), _nt.Array[np.intp])
assert_type(np.fix(AR_LIKE_f), _nt.Array[np.float64])
assert_type(np.fix(AR_LIKE_f, out=AR_U), _nt.Array[np.str_])

assert_type(np.isposinf(AR_u), _nt.Array[np.bool])
assert_type(np.isposinf(AR_LIKE_b), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_i), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f), _nt.Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f, out=AR_U), _nt.Array[np.str_])

assert_type(np.isneginf(AR_u), _nt.Array[np.bool])
assert_type(np.isneginf(AR_LIKE_b), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_i), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f), _nt.Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f, out=AR_U), _nt.Array[np.str_])
