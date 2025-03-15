from typing import Any
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

i8: np.int64
f8: np.float64
AR_f8: npt.NDArray[np.float64]
AR_i8: npt.NDArray[np.int64]
AR_bool: npt.NDArray[np.bool_]

assert_type(np.absolute.types, list[str])

assert_type(np.absolute(f8), Any)
assert_type(np.absolute(AR_f8), npt.NDArray[Any])
assert_type(np.absolute.at(AR_f8, AR_i8), None)

assert_type(np.add(f8, f8), Any)
assert_type(np.add(AR_f8, f8), npt.NDArray[Any])
assert_type(np.add.at(AR_f8, AR_i8, f8), None)
assert_type(np.add.reduce(AR_f8, axis=0), Any)
assert_type(np.add.accumulate(AR_f8), npt.NDArray[Any])
assert_type(np.add.reduceat(AR_f8, AR_i8), npt.NDArray[Any])
assert_type(np.add.outer(AR_f8, f8), npt.NDArray[Any])

assert_type(np.frexp(f8), tuple[Any, Any])
assert_type(np.frexp(AR_f8), tuple[npt.NDArray[Any], npt.NDArray[Any]])

assert_type(np.divmod(f8, f8), tuple[Any, Any])
assert_type(np.divmod(AR_f8, f8), tuple[npt.NDArray[Any], npt.NDArray[Any]])

assert_type(np.matmul(AR_f8, AR_f8), Any)
assert_type(np.matmul(AR_f8, AR_f8, axes=[(0, 1), (0, 1), (0, 1)]), Any)

assert_type(np.vecdot(AR_f8, AR_f8), Any)

assert_type(np.bitwise_count(i8), Any)
assert_type(np.bitwise_count(AR_i8), npt.NDArray[Any])

assert_type(np.isnan(f8), np.bool_)
assert_type(np.isnan(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isnan(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.isnat(f8), np.bool_)
assert_type(np.isnat(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isnat(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.isinf(f8), np.bool_)
assert_type(np.isinf(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isinf(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.isfinite(f8), np.bool_)
assert_type(np.isfinite(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isfinite(AR_f8, out=AR_bool), npt.NDArray[np.bool_])
