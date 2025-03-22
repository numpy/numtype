from typing import Any
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

i8: np.int64
f4: np.float32
f8: np.float64
dt64: np.datetime64
td64: np.timedelta64
AR_f4: npt.NDArray[np.float32]
AR_f8: npt.NDArray[np.float64]
AR_i8: npt.NDArray[np.int64]
AR_bool: npt.NDArray[np.bool_]
AR_dt64: npt.NDArray[np.datetime64]
AR_td64: npt.NDArray[np.timedelta64]

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

assert_type(np.isnat(dt64), np.bool_)
assert_type(np.isnat(td64), np.bool_)
assert_type(np.isnat([td64, td64]), npt.NDArray[np.bool_])
assert_type(np.isnat([td64, td64], out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.isnat(AR_dt64), npt.NDArray[np.bool_])
assert_type(np.isnat(AR_dt64, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.isnat(AR_td64), npt.NDArray[np.bool_])
assert_type(np.isnat(AR_td64, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.isinf(f8), np.bool_)
assert_type(np.isinf(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isinf(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.isfinite(f8), np.bool_)
assert_type(np.isfinite(AR_f8), npt.NDArray[np.bool_])
assert_type(np.isfinite(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.logical_not(True), np.bool_)
assert_type(np.logical_not(AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_not(AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_not(AR_bool, dtype=np.object_), npt.NDArray[np.object_] | bool)

assert_type(np.logical_and(True, True), np.bool_)
assert_type(np.logical_and(AR_bool, AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_and(AR_bool, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_and(AR_i8, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_and(AR_bool, AR_i8), npt.NDArray[np.bool_])
assert_type(np.logical_and(AR_bool, AR_bool, dtype=np.object_), npt.NDArray[np.object_])

assert_type(np.logical_or(True, True), np.bool_)
assert_type(np.logical_or(AR_bool, AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_or(AR_bool, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_or(AR_i8, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_or(AR_bool, AR_i8), npt.NDArray[np.bool_])
assert_type(np.logical_or(AR_bool, AR_bool, dtype=np.object_), npt.NDArray[np.object_])

assert_type(np.logical_xor(True, True), np.bool_)
assert_type(np.logical_xor(AR_bool, AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_xor(AR_bool, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_xor(AR_i8, AR_bool, out=AR_bool), npt.NDArray[np.bool_])
assert_type(np.logical_xor(AR_bool, AR_i8), npt.NDArray[np.bool_])
assert_type(np.logical_xor(AR_bool, AR_bool, dtype=np.object_), npt.NDArray[np.object_])

assert_type(np.spacing(f4), np.floating)
assert_type(np.spacing(f8), np.float64)
assert_type(np.spacing(AR_f8), npt.NDArray[np.float64])
assert_type(np.spacing(AR_f4), npt.NDArray[np.floating])
assert_type(np.spacing(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.signbit(f8), np.bool_)
assert_type(np.signbit(AR_f8), npt.NDArray[np.bool_])
assert_type(np.signbit(AR_f8, out=AR_bool), npt.NDArray[np.bool_])

assert_type(np.cbrt(f8), np.float64)
assert_type(np.cbrt(f8, dtype=np.float64), np.float64)
assert_type(np.cbrt(AR_f8), npt.NDArray[np.float64])
assert_type(np.cbrt(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.deg2rad(f8), np.float64)
assert_type(np.deg2rad(f8, dtype=np.float64), np.float64)
assert_type(np.deg2rad(AR_f8), npt.NDArray[np.float64])
assert_type(np.deg2rad(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.degrees(f8), np.float64)
assert_type(np.degrees(f8, dtype=np.float64), np.float64)
assert_type(np.degrees(AR_f8), npt.NDArray[np.float64])
assert_type(np.degrees(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.fabs(f8), np.float64)
assert_type(np.fabs(f8, dtype=np.float64), np.float64)
assert_type(np.fabs(AR_f8), npt.NDArray[np.float64])
assert_type(np.fabs(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.rad2deg(f8), np.float64)
assert_type(np.rad2deg(f8, dtype=np.float64), np.float64)
assert_type(np.rad2deg(AR_f8), npt.NDArray[np.float64])
assert_type(np.rad2deg(AR_f8, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.radians(f8), np.float64)
assert_type(np.radians(f8, dtype=np.float64), np.float64)
assert_type(np.radians(AR_f8), npt.NDArray[np.float64])
assert_type(np.radians(AR_f8, out=AR_f8), npt.NDArray[np.float64])
