from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
f8: np.float64
c16: np.complex128

assert_type(np.emath.logn(f8, 2), np.inexact)
assert_type(np.emath.logn(AR_f8, 4), npt.NDArray[np.inexact])
assert_type(np.emath.logn(f8, 1j), np.complexfloating)
assert_type(np.emath.logn(AR_c16, 1.5), npt.NDArray[np.complexfloating])

assert_type(np.emath.power(f8, 2), np.inexact)
assert_type(np.emath.power(AR_f8, 4), npt.NDArray[np.inexact])
assert_type(np.emath.power(f8, 2j), np.complexfloating)
assert_type(np.emath.power(AR_c16, 1.5), npt.NDArray[np.complexfloating])
