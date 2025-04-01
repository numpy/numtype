from typing import TypeAlias
from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt

AR_u: npt.NDArray[np.uint32]
AR_U: npt.NDArray[np.str_]
AR_LIKE_b: list[bool]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]

###

assert_type(np.fix(AR_u), npt.NDArray[np.uint32])
assert_type(np.fix(AR_LIKE_b), npt.NDArray[np.bool])
assert_type(np.fix(AR_LIKE_i), npt.NDArray[np.intp])
assert_type(np.fix(AR_LIKE_f), npt.NDArray[np.float64])
assert_type(np.fix(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])

assert_type(np.isposinf(AR_u), npt.NDArray[np.bool])
assert_type(np.isposinf(AR_LIKE_b), _Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_i), _Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f), _Array1D[np.bool])
assert_type(np.isposinf(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])

assert_type(np.isneginf(AR_u), npt.NDArray[np.bool])
assert_type(np.isneginf(AR_LIKE_b), _Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_i), _Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f), _Array1D[np.bool])
assert_type(np.isneginf(AR_LIKE_f, out=AR_U), npt.NDArray[np.str_])
