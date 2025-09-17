import datetime as dt
from typing import Literal as L, assert_type

import _numtype as _nt
import numpy as np

f8: np.float64
i8: np.int64
u8: np.uint64

f4: np.float32
i4: np.int32
u4: np.uint32

m: np.timedelta64
m_nat: np.timedelta64[None]
m_int0: np.timedelta64[L[0]]
m_int: np.timedelta64[int]
m_td: np.timedelta64[dt.timedelta]

b_: np.bool

b: bool
i: int
f: float

AR_b: _nt.Array[np.bool]
AR_m: _nt.Array[np.timedelta64]

# Time structures

assert_type(m % m, np.timedelta64)
assert_type(m % m_nat, np.timedelta64[None])
assert_type(m % m_int0, np.timedelta64[None])
assert_type(m % m_int, np.timedelta64[int | None])
assert_type(m_nat % m, np.timedelta64[None])
assert_type(m_int % m_nat, np.timedelta64[None])
assert_type(m_int % m_int0, np.timedelta64[None])
assert_type(m_int % m_int, np.timedelta64[int | None])
assert_type(m_int % m_td, np.timedelta64[int | None])
assert_type(m_td % m_nat, np.timedelta64[None])
assert_type(m_td % m_int0, np.timedelta64[None])
assert_type(m_td % m_int, np.timedelta64[int | None])
assert_type(m_td % m_td, np.timedelta64[dt.timedelta | None])

assert_type(AR_m % m, _nt.Array[np.timedelta64])
assert_type(m % AR_m, _nt.Array[np.timedelta64])

# NOTE: `builtins.divmod` can not always be used because of a recurrent pyright bug
# (microsoft/pyright#9896, microsoft/pyright#10849, microsoft/pyright#10899)

assert_type(divmod(m, m), tuple[np.int64, np.timedelta64])
assert_type(divmod(m, m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m, m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m, m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(divmod(m_nat, m), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m_int, m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m_int, m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m_int, m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(divmod(m_int, m_td), tuple[np.int64, np.timedelta64[int | None]])
assert_type(divmod(m_td, m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m_td, m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(divmod(m_td, m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(divmod(m_td, m_td), tuple[np.int64, np.timedelta64[dt.timedelta | None]])

assert_type(divmod(AR_m, m), tuple[_nt.Array[np.int64], _nt.Array[np.timedelta64]])
assert_type(divmod(m, AR_m), tuple[_nt.Array[np.int64], _nt.Array[np.timedelta64]])

# Bool
assert_type(b_ % b, np.int8)
assert_type(b_ % i, np.intp)
assert_type(b_ % f, np.float64)
assert_type(b_ % b_, np.int8)
assert_type(b_ % i8, np.int64)
assert_type(b_ % u8, np.uint64)
assert_type(b_ % f8, np.float64)
assert_type(b_ % AR_b, _nt.Array[np.int8])

assert_type(divmod(b_, b_), tuple[np.int8, np.int8])
assert_type(divmod(b_, b), tuple[np.int8, np.int8])
assert_type(divmod(b_, i), tuple[np.intp, np.intp])
assert_type(divmod(b_, f), tuple[np.float64, np.float64])
assert_type(divmod(b_, i8), tuple[np.int64, np.int64])
assert_type(divmod(b_, u8), tuple[np.uint64, np.uint64])
assert_type(divmod(b_, f8), tuple[np.float64, np.float64])
assert_type(divmod(b_, AR_b), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])

assert_type(b % b_, np.int8)
assert_type(i % b_, np.intp)
assert_type(f % b_, np.float64)
assert_type(b_ % b_, np.int8)
assert_type(i8 % b_, np.int64)
assert_type(u8 % b_, np.uint64)
assert_type(f8 % b_, np.float64)
assert_type(AR_b % b_, _nt.Array[np.int8])

assert_type(divmod(b_, b), tuple[np.int8, np.int8])
assert_type(divmod(b_, i), tuple[np.intp, np.intp])
assert_type(divmod(b_, f), tuple[np.float64, np.float64])
assert_type(divmod(b_, i8), tuple[np.int64, np.int64])
assert_type(divmod(b_, u8), tuple[np.uint64, np.uint64])
assert_type(divmod(b_, f8), tuple[np.float64, np.float64])
assert_type(divmod(AR_b, b_), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])

# int

assert_type(i8 % b, np.int64)
assert_type(i8 % i, np.int64)
assert_type(i8 % f, np.float64)
assert_type(i8 % i8, np.int64)
assert_type(i8 % f8, np.float64)
assert_type(i4 % i8, np.int64)
assert_type(i4 % f8, np.float64)
assert_type(i4 % i4, np.int32)
assert_type(i4 % f4, np.float64)
assert_type(i8 % AR_b, _nt.Array[np.int64])

assert_type(divmod(i8, b), tuple[np.int64, np.int64])
assert_type(divmod(i8, i), tuple[np.int64, np.int64])
assert_type(divmod(i8, f), tuple[np.float64, np.float64])
assert_type(divmod(i8, i4), tuple[np.int64, np.int64])
assert_type(divmod(i8, i8), tuple[np.int64, np.int64])
assert_type(divmod(i8, f8), tuple[np.float64, np.float64])
assert_type(divmod(i8, f4), tuple[np.float64, np.float64])
assert_type(divmod(i4, i4), tuple[np.int32, np.int32])
assert_type(divmod(i8, AR_b), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])

assert_type(b % i8, np.int64)
assert_type(f % i8, np.float64)
assert_type(i8 % i8, np.int64)
assert_type(f8 % i8, np.float64)
assert_type(i8 % i4, np.int64)
assert_type(f8 % i4, np.float64)
assert_type(i4 % i4, np.int32)
assert_type(f4 % i4, np.float64)
assert_type(AR_b % i8, _nt.Array[np.int64])

assert_type(divmod(i8, b), tuple[np.int64, np.int64])
assert_type(divmod(i8, f), tuple[np.float64, np.float64])
assert_type(divmod(i8, i8), tuple[np.int64, np.int64])
assert_type(divmod(i8, f8), tuple[np.float64, np.float64])
assert_type(divmod(i8, i4), tuple[np.int64, np.int64])
assert_type(divmod(i4, i8), tuple[np.int64, np.int64])
assert_type(divmod(f4, i8), tuple[np.float64, np.float64])
assert_type(divmod(f4, i4), tuple[np.float64, np.float64])
assert_type(divmod(AR_b, i8), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])

# float

assert_type(f8 % b, np.float64)
assert_type(f8 % f, np.float64)
assert_type(i8 % f4, np.float64)
assert_type(f4 % f4, np.float32)
assert_type(f8 % AR_b, _nt.Array[np.float64])

assert_type(divmod(f8, b), tuple[np.float64, np.float64])
assert_type(divmod(f8, f), tuple[np.float64, np.float64])
assert_type(divmod(f8, f8), tuple[np.float64, np.float64])
assert_type(divmod(f8, f4), tuple[np.float64, np.float64])
assert_type(divmod(f4, f4), tuple[np.float32, np.float32])
assert_type(divmod(f8, AR_b), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])

assert_type(b % f8, np.float64)
assert_type(f % f8, np.float64)  # pyright: ignore[reportAssertTypeFailure]  # pyright incorrectly infers `builtins.float`
assert_type(f8 % f8, np.float64)
assert_type(f8 % f8, np.float64)
assert_type(f4 % f4, np.float32)
assert_type(AR_b % f8, _nt.Array[np.float64])

assert_type(divmod(b, f8), tuple[np.float64, np.float64])
assert_type(divmod(f8, f8), tuple[np.float64, np.float64])
assert_type(divmod(f4, f4), tuple[np.float32, np.float32])
assert_type(divmod(f, f8), tuple[np.float64, np.float64])  # pyright: ignore[reportAssertTypeFailure]
assert_type(divmod(f4, f8), tuple[np.float64, np.float64])
assert_type(divmod(AR_b, f8), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
