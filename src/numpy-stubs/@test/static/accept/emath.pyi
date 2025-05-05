from typing import assert_type

import _numtype as _nt
import numpy as np

AR_f8: _nt.Array[np.float64]
AR_c16: _nt.Array[np.complex128]
f8: np.float64
c16: np.complex128

assert_type(np.emath.logn(f8, 2), np.inexact)
assert_type(np.emath.logn(AR_f8, 4), _nt.Array[np.inexact])
assert_type(np.emath.logn(f8, 1j), np.complexfloating)
assert_type(np.emath.logn(AR_c16, 1.5), _nt.Array[np.complexfloating])

assert_type(np.emath.power(f8, 2), np.inexact)
assert_type(np.emath.power(AR_f8, 4), _nt.Array[np.inexact])
assert_type(np.emath.power(f8, 2j), np.complexfloating)
assert_type(np.emath.power(AR_c16, 1.5), _nt.Array[np.complexfloating])
