import datetime as dt
from typing import Literal as L
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

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

AR_b: npt.NDArray[np.bool]
AR_m: npt.NDArray[np.timedelta64]

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

assert_type(AR_m % m, npt.NDArray[np.timedelta64])
assert_type(m % AR_m, npt.NDArray[np.timedelta64])

# NOTE: `builtins.divmod` cannot be used because of
# https://github.com/microsoft/pyright/issues/9896

assert_type(m.__divmod__(m), tuple[np.int64, np.timedelta64])
assert_type(m.__divmod__(m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(m.__divmod__(m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(m.__divmod__(m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(m_nat.__divmod__(m), tuple[np.int64, np.timedelta64[None]])
assert_type(m_int.__divmod__(m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(m_int.__divmod__(m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(m_int.__divmod__(m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(m_int.__divmod__(m_td), tuple[np.int64, np.timedelta64[int | None]])
assert_type(m_td.__divmod__(m_nat), tuple[np.int64, np.timedelta64[None]])
assert_type(m_td.__divmod__(m_int0), tuple[np.int64, np.timedelta64[None]])
assert_type(m_td.__divmod__(m_int), tuple[np.int64, np.timedelta64[int | None]])
assert_type(m_td.__divmod__(m_td), tuple[np.int64, np.timedelta64[dt.timedelta | None]])

assert_type(divmod(AR_m, m), tuple[npt.NDArray[np.int64], npt.NDArray[np.timedelta64]])
assert_type(divmod(m, AR_m), tuple[npt.NDArray[np.int64], npt.NDArray[np.timedelta64]])

# Bool
assert_type(b_ % b, np.int8)
assert_type(b_ % i, np.intp)
assert_type(b_ % f, np.float64)
assert_type(b_ % b_, np.int8)
assert_type(b_ % i8, np.int64)
assert_type(b_ % u8, np.uint64)
assert_type(b_ % f8, np.float64)
assert_type(b_ % AR_b, npt.NDArray[np.int8])

assert_type(b_.__divmod__(b_), tuple[np.int8, np.int8])
assert_type(b_.__divmod__(b), tuple[np.int8, np.int8])
assert_type(b_.__divmod__(i), tuple[np.intp, np.intp])
assert_type(b_.__divmod__(f), tuple[np.float64, np.float64])
assert_type(b_.__divmod__(i8), tuple[np.int64, np.int64])
assert_type(b_.__divmod__(u8), tuple[np.uint64, np.uint64])
assert_type(b_.__divmod__(f8), tuple[np.float64, np.float64])
# assert_type(b_.__divmod__(AR_b), tuple[np.float64, np.float64])

assert_type(b % b_, np.int8)
assert_type(i % b_, np.intp)
assert_type(f % b_, np.float64)
assert_type(b_ % b_, np.int8)
assert_type(i8 % b_, np.int64)
assert_type(u8 % b_, np.uint64)
assert_type(f8 % b_, np.float64)
assert_type(AR_b % b_, npt.NDArray[np.int8])

assert_type(b_.__rdivmod__(b), tuple[np.int8, np.int8])
assert_type(b_.__rdivmod__(i), tuple[np.intp, np.intp])
assert_type(b_.__rdivmod__(f), tuple[np.float64, np.float64])
assert_type(b_.__rdivmod__(i8), tuple[np.int64, np.int64])
assert_type(b_.__rdivmod__(u8), tuple[np.uint64, np.uint64])
assert_type(b_.__rdivmod__(f8), tuple[np.float64, np.float64])
assert_type(AR_b.__rdivmod__(b_), tuple[npt.NDArray[np.int8], npt.NDArray[np.int8]])

# int

assert_type(i8 % b, np.int64)
assert_type(i8 % i, np.int64)
assert_type(i8 % f, np.int64 | np.float64)
assert_type(i8 % i8, np.int64)
assert_type(i8 % f8, np.float64)
assert_type(i4 % i8, np.int64)
assert_type(i4 % f8, np.float64)
assert_type(i4 % i4, np.int32)
assert_type(i4 % f4, np.float64)
assert_type(i8 % AR_b, npt.NDArray[np.int64])

assert_type(i8.__divmod__(b), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(i), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(f), tuple[np.int64, np.int64] | tuple[np.float64, np.float64])
assert_type(i8.__divmod__(i4), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(i8), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(f8), tuple[np.float64, np.float64])
assert_type(i8.__divmod__(f4), tuple[np.float64, np.float64])
assert_type(i4.__divmod__(i4), tuple[np.int32, np.int32])
assert_type(divmod(i8, AR_b), tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]])

assert_type(b % i8, np.int64)
assert_type(f % i8, np.int64 | np.float64)
assert_type(i8 % i8, np.int64)
assert_type(f8 % i8, np.float64)
assert_type(i8 % i4, np.int64)
assert_type(f8 % i4, np.float64)
assert_type(i4 % i4, np.int32)
assert_type(f4 % i4, np.float64)
assert_type(AR_b % i8, npt.NDArray[np.int64])

assert_type(i8.__divmod__(b), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(f), tuple[np.int64, np.int64] | tuple[np.float64, np.float64])
assert_type(i8.__divmod__(i8), tuple[np.int64, np.int64])
assert_type(i8.__divmod__(f8), tuple[np.float64, np.float64])
# assert_type(i8.__divmod__(i4), tuple[np.int32, np.int32])
assert_type(i4.__divmod__(i8), tuple[np.int64, np.int64])
assert_type(f4.__divmod__(i8), tuple[np.float64, np.float64])
assert_type(f4.__divmod__(i4), tuple[np.float64, np.float64])
assert_type(AR_b.__divmod__(i8), tuple[npt.NDArray[np.int64], npt.NDArray[np.int64]])

# float

assert_type(f8 % b, np.float64)
assert_type(f8 % f, np.float64)
assert_type(i8 % f4, np.float64)
assert_type(f4 % f4, np.float32)
assert_type(f8 % AR_b, npt.NDArray[np.float64])

assert_type(divmod(f8, b), tuple[np.float64, np.float64])
assert_type(divmod(f8, f), tuple[np.float64, np.float64])
assert_type(divmod(f8, f8), tuple[np.float64, np.float64])
assert_type(divmod(f8, f4), tuple[np.float64, np.float64])
assert_type(divmod(f4, f4), tuple[np.float32, np.float32])
assert_type(AR_b.__rdivmod__(f8), tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]])

assert_type(b % f8, np.float64)
assert_type(f % f8, np.float64)  # pyright: ignore[reportAssertTypeFailure]  # pyright incorrectly infers `builtins.float`
assert_type(f8 % f8, np.float64)
assert_type(f8 % f8, np.float64)
assert_type(f4 % f4, np.float32)
assert_type(AR_b % f8, npt.NDArray[np.float64])

assert_type(divmod(b, f8), tuple[np.float64, np.float64])
assert_type(divmod(f8, f8), tuple[np.float64, np.float64])
assert_type(divmod(f4, f4), tuple[np.float32, np.float32])
assert_type(f8.__rdivmod__(f), tuple[np.float64, np.float64])
assert_type(f8.__rdivmod__(f4), tuple[np.float64, np.float64])
assert_type(AR_b.__divmod__(f8), tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]])
