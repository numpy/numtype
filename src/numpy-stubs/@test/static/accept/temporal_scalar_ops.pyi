# Type tests for datetime64/timedelta64 operations using representative subtype cases

import datetime as dt
from typing import assert_type

import numpy as np

DT = np.datetime64
TD = np.timedelta64

dt_default: DT
dt_none: DT[None]
dt_int: DT[int]
dt_datetime: DT[dt.datetime]
dt_date: DT[dt.date]

td_default: TD
td_none: TD[None]
td_int: TD[int]
td_timedelta: TD[dt.timedelta]

assert_type(dt_default + td_default, DT)
assert_type(dt_default + td_none, DT[None])
# mypy incorrectly infers this as "timedelta64[Any]" but pyright behaves correctly
assert_type(dt_none + td_default, DT[None])  # type: ignore[assert-type]
assert_type(dt_int + td_int, DT[int])
assert_type(dt_datetime + td_timedelta, DT[dt.datetime])
assert_type(dt_date + td_timedelta, DT[dt.date])

assert_type(dt_default - td_default, DT)
assert_type(dt_default - td_none, DT[None])
assert_type(dt_none - td_default, DT[None])  # type: ignore[assert-type]
assert_type(dt_int - td_int, DT[int])
assert_type(dt_datetime - td_timedelta, DT[dt.datetime])
assert_type(dt_date - td_timedelta, DT[dt.date])
assert_type(dt_date - td_int, DT[dt.date | int])

assert_type(dt_default - dt_default, TD)
assert_type(dt_none - dt_default, TD[None])  # type: ignore[assert-type]
assert_type(dt_int - dt_int, TD[int])
assert_type(dt_datetime - dt_datetime, TD[dt.timedelta])
assert_type(dt_date - dt_date, TD[dt.timedelta])

assert_type(td_default + td_default, TD)
assert_type(td_none + td_default, TD[None])  # type: ignore[assert-type]
assert_type(td_int + td_int, TD[int])
assert_type(td_timedelta + td_timedelta, TD[dt.timedelta])

assert_type(td_default - td_default, TD)
assert_type(td_none - td_default, TD[None])  # type: ignore[assert-type]
assert_type(td_int - td_int, TD[int])
assert_type(td_timedelta - td_timedelta, TD[dt.timedelta])

assert_type(td_default / td_default, np.float64)
assert_type(td_none / td_default, np.float64)

assert_type(td_default % td_default, TD)
assert_type(td_none % td_default, TD[None])  # type: ignore[assert-type]

assert_type(td_default * 0, TD)
assert_type(td_none * 0, TD[None])
assert_type(td_int * 0, TD[int])
assert_type(td_timedelta * 0, TD[dt.timedelta])

assert_type(0 * td_default, TD)
assert_type(0 * td_none, TD[None])
assert_type(0 * td_int, TD[int])
assert_type(0 * td_timedelta, TD[dt.timedelta])

assert_type(td_default / 0, TD)
assert_type(td_none / 0, TD[None])
assert_type(td_int / 0, TD[int])
assert_type(td_timedelta / 0, TD[dt.timedelta])
