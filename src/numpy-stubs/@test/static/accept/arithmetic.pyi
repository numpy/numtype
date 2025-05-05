import datetime as dt
from typing import assert_type

import _numtype as _nt
import numpy as np

i: int
i8: np.int64

M8: np.datetime64
M8_none: np.datetime64[None]
date: dt.date
time: dt.datetime

m8: np.timedelta64
m8_none: np.timedelta64[None]
m8_int: np.timedelta64[int]
m8_delta: np.timedelta64[dt.timedelta]
delta: dt.timedelta

AR_Any: _nt.Array

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

assert_type(AR_Any + 2, _nt.Array)
