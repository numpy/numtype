import datetime as dt
from typing import Any
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

i: int
i8: np.int64

M8: np.datetime64
M8_none: np.datetime64[None]
M8_date: np.datetime64[dt.date]
M8_time: np.datetime64[dt.datetime]
M8_int: np.datetime64[int]
date: dt.date
time: dt.datetime

m8: np.timedelta64
m8_none: np.timedelta64[None]
m8_int: np.timedelta64[int]
m8_delta: np.timedelta64[dt.timedelta]
delta: dt.timedelta

AR_b: npt.NDArray[np.bool]
AR_u: npt.NDArray[np.uint32]
AR_i: npt.NDArray[np.int64]
AR_f: npt.NDArray[np.float64]
AR_m: npt.NDArray[np.timedelta64]
AR_O: npt.NDArray[np.object_]
AR_Any: npt.NDArray[Any]

AR_LIKE_b: list[bool]
AR_LIKE_u: list[np.uint32]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]
AR_LIKE_m: list[np.timedelta64]
AR_LIKE_M: list[np.datetime64]
AR_LIKE_O: list[np.object_]

# Array floor division

assert_type(AR_b // AR_LIKE_b, npt.NDArray[np.int8])
assert_type(AR_b // AR_LIKE_u, npt.NDArray[np.uint32])
assert_type(AR_b // AR_LIKE_i, npt.NDArray[np.signedinteger])
assert_type(AR_b // AR_LIKE_f, npt.NDArray[np.float64])
assert_type(AR_b // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_b // AR_b, npt.NDArray[np.int8])
assert_type(AR_LIKE_u // AR_b, npt.NDArray[np.uint32])
assert_type(AR_LIKE_i // AR_b, npt.NDArray[np.signedinteger])
assert_type(AR_LIKE_f // AR_b, npt.NDArray[np.float64])
assert_type(AR_LIKE_O // AR_b, npt.NDArray[np.object_])

assert_type(AR_u // AR_LIKE_b, npt.NDArray[np.uint32])
assert_type(AR_u // AR_LIKE_u, npt.NDArray[np.unsignedinteger])
assert_type(AR_u // AR_LIKE_i, npt.NDArray[np.signedinteger])
assert_type(AR_u // AR_LIKE_f, npt.NDArray[np.float64])
assert_type(AR_u // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_b // AR_u, npt.NDArray[np.uint32])
assert_type(AR_LIKE_u // AR_u, npt.NDArray[np.unsignedinteger])
assert_type(AR_LIKE_i // AR_u, npt.NDArray[np.signedinteger])
assert_type(AR_LIKE_f // AR_u, npt.NDArray[np.float64])
assert_type(AR_LIKE_m // AR_u, npt.NDArray[np.timedelta64])
assert_type(AR_LIKE_O // AR_u, npt.NDArray[np.object_])

assert_type(AR_i // AR_LIKE_b, npt.NDArray[np.int64])
assert_type(AR_i // AR_LIKE_u, npt.NDArray[np.signedinteger])
assert_type(AR_i // AR_LIKE_i, npt.NDArray[np.signedinteger])
assert_type(AR_i // AR_LIKE_f, npt.NDArray[np.float64])
assert_type(AR_i // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_b // AR_i, npt.NDArray[np.int64])
assert_type(AR_LIKE_u // AR_i, npt.NDArray[np.signedinteger])
assert_type(AR_LIKE_i // AR_i, npt.NDArray[np.signedinteger])
assert_type(AR_LIKE_f // AR_i, npt.NDArray[np.float64])
assert_type(AR_LIKE_m // AR_i, npt.NDArray[np.timedelta64])
assert_type(AR_LIKE_O // AR_i, npt.NDArray[np.object_])

assert_type(AR_f // AR_LIKE_b, npt.NDArray[np.float64])
assert_type(AR_f // AR_LIKE_u, npt.NDArray[np.float64])
assert_type(AR_f // AR_LIKE_i, npt.NDArray[np.float64])
assert_type(AR_f // AR_LIKE_f, npt.NDArray[np.float64])
assert_type(AR_f // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_b // AR_f, npt.NDArray[np.float64])
assert_type(AR_LIKE_u // AR_f, npt.NDArray[np.float64])
assert_type(AR_LIKE_i // AR_f, npt.NDArray[np.float64])
assert_type(AR_LIKE_f // AR_f, npt.NDArray[np.float64])
assert_type(AR_LIKE_m // AR_f, npt.NDArray[np.timedelta64])
assert_type(AR_LIKE_O // AR_f, npt.NDArray[np.object_])

assert_type(AR_m // AR_LIKE_u, npt.NDArray[np.timedelta64])
assert_type(AR_m // AR_LIKE_i, npt.NDArray[np.timedelta64])
assert_type(AR_m // AR_LIKE_f, npt.NDArray[np.timedelta64])
assert_type(AR_m // AR_LIKE_m, npt.NDArray[np.int64])
assert_type(AR_m // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_m // AR_m, npt.NDArray[np.int64])
assert_type(AR_LIKE_O // AR_m, npt.NDArray[np.object_])

assert_type(AR_O // AR_LIKE_b, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_u, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_i, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_f, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_m, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_M, npt.NDArray[np.object_])
assert_type(AR_O // AR_LIKE_O, npt.NDArray[np.object_])

assert_type(AR_LIKE_b // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_u // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_i // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_f // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_m // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_M // AR_O, npt.NDArray[np.object_])
assert_type(AR_LIKE_O // AR_O, npt.NDArray[np.object_])

# Time structures

assert_type(m8 // m8, np.int64)
assert_type(m8 % m8, np.timedelta64)
assert_type(divmod(m8, m8), tuple[np.int64, np.timedelta64])

assert_type(M8_none + m8, np.datetime64[None])
assert_type(M8_none + i, np.datetime64[None])
assert_type(M8_none + i8, np.datetime64[None])
assert_type(M8_none - M8, np.timedelta64[None])
assert_type(M8_none - m8, np.datetime64[None])
assert_type(M8_none - i, np.datetime64[None])
assert_type(M8_none - i8, np.datetime64[None])

assert_type(m8_none + m8, np.timedelta64[None])
assert_type(m8_none + i, np.timedelta64[None])
assert_type(m8_none + i8, np.timedelta64[None])
assert_type(m8_none - i, np.timedelta64[None])
assert_type(m8_none - i8, np.timedelta64[None])

assert_type(m8_int + i, np.timedelta64[int])
assert_type(m8_int + m8_delta, np.timedelta64[int])
assert_type(m8_int + m8, np.timedelta64[int | None])
assert_type(m8_int - i, np.timedelta64[int])
assert_type(m8_int - m8_delta, np.timedelta64[int])
assert_type(m8_int - m8, np.timedelta64[int | None])

assert_type(m8_delta + date, dt.date)
assert_type(m8_delta + time, dt.datetime)
assert_type(m8_delta + delta, dt.timedelta)
assert_type(m8_delta - delta, dt.timedelta)
assert_type(m8_delta / delta, float)
assert_type(m8_delta // delta, int)
assert_type(m8_delta % delta, dt.timedelta)
# workaround for https://github.com/microsoft/pyright/issues/9663
assert_type(m8_delta.__divmod__(delta), tuple[int, dt.timedelta])

# Any

assert_type(AR_Any + 2, npt.NDArray[Any])
