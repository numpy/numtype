import decimal
import fractions
from typing import TypeAlias
from typing_extensions import assert_type

import _numtype as _nt
import numpy as np
import numpy.typing as npt

###
# Type aliases

BoolND: TypeAlias = npt.NDArray[np.bool]

###
# Values

b: bool
i: int
f: float
c: complex

i_tuple: tuple[int, ...]

b1: np.bool
i4: np.int32
u4: np.uint32
i8: np.int64
u8: np.uint64
f4: np.float32
f8: np.float64
c8: np.complex64
c16: np.complex128
dt: np.datetime64
td: np.timedelta64

i8_1d: np.ndarray[_nt.Shape1, np.dtype[np.int64]]

###
# object-like comparisons

assert_type(i8 > fractions.Fraction(1, 5), np.bool)
assert_type(i8 > [fractions.Fraction(1, 5)], BoolND)
assert_type(i8 > decimal.Decimal("1.5"), np.bool)
assert_type(i8 > [decimal.Decimal("1.5")], BoolND)

###
# Time structures

assert_type(dt > dt, np.bool)

assert_type(td > td, np.bool)
assert_type(td > i, np.bool)
assert_type(td > i4, np.bool)
assert_type(td > i8, np.bool)

assert_type(td > i8_1d, BoolND)
assert_type(td > i_tuple, BoolND)
assert_type(i8_1d > i_tuple, BoolND)
assert_type(td < i8_1d, BoolND)
assert_type(td < i_tuple, BoolND)
assert_type(i_tuple > i8_1d, BoolND)

###
# boolean

assert_type(b1 > b, np.bool)
assert_type(b1 > b1, np.bool)
assert_type(b1 > i, np.bool)
assert_type(b1 > i8, np.bool)
assert_type(b1 > i4, np.bool)
assert_type(b1 > u8, np.bool)
assert_type(b1 > u4, np.bool)
assert_type(b1 > f, np.bool)
assert_type(b1 > f8, np.bool)
assert_type(b1 > f4, np.bool)
assert_type(b1 > c, np.bool)
assert_type(b1 > c16, np.bool)
assert_type(b1 > c8, np.bool)
assert_type(b1 > i8_1d, BoolND)
assert_type(b1 > i_tuple, BoolND)

###
# Complex

assert_type(c16 > c16, np.bool)
assert_type(c16 > f8, np.bool)
assert_type(c16 > i8, np.bool)
assert_type(c16 > c8, np.bool)
assert_type(c16 > f4, np.bool)
assert_type(c16 > i4, np.bool)
assert_type(c16 > b1, np.bool)
assert_type(c16 > b, np.bool)
assert_type(c16 > c, np.bool)
assert_type(c16 > f, np.bool)
assert_type(c16 > i, np.bool)
assert_type(c16 > i8_1d, BoolND)
assert_type(c16 > i_tuple, BoolND)

assert_type(c16 > c16, np.bool)
assert_type(f8 > c16, np.bool)
assert_type(i8 > c16, np.bool)
assert_type(c8 > c16, np.bool)
assert_type(f4 > c16, np.bool)
assert_type(i4 > c16, np.bool)
assert_type(b1 > c16, np.bool)
assert_type(b > c16, np.bool)
assert_type(c > c16, np.bool)
assert_type(f > c16, np.bool)
assert_type(i > c16, np.bool)
assert_type(c16 < i8_1d, BoolND)
assert_type(c16 < i_tuple, BoolND)

assert_type(c8 > c16, np.bool)
assert_type(c8 > f8, np.bool)
assert_type(c8 > i8, np.bool)
assert_type(c8 > c8, np.bool)
assert_type(c8 > f4, np.bool)
assert_type(c8 > i4, np.bool)
assert_type(c8 > b1, np.bool)
assert_type(c8 > b, np.bool)
assert_type(c8 > c, np.bool)
assert_type(c8 > f, np.bool)
assert_type(c8 > i, np.bool)
assert_type(c8 > i8_1d, BoolND)
assert_type(c8 > i_tuple, BoolND)

assert_type(c16 > c8, np.bool)
assert_type(f8 > c8, np.bool)
assert_type(i8 > c8, np.bool)
assert_type(c8 > c8, np.bool)
assert_type(f4 > c8, np.bool)
assert_type(i4 > c8, np.bool)
assert_type(b1 > c8, np.bool)
assert_type(b > c8, np.bool)
assert_type(c > c8, np.bool)
assert_type(f > c8, np.bool)
assert_type(i > c8, np.bool)
assert_type(c8 < i8_1d, BoolND)
assert_type(c8 < i_tuple, BoolND)

###
# Float

assert_type(f8 > f8, np.bool)
assert_type(f8 > i8, np.bool)
assert_type(f8 > f4, np.bool)
assert_type(f8 > i4, np.bool)
assert_type(f8 > b1, np.bool)
assert_type(f8 > b, np.bool)
assert_type(f8 > c, np.bool)
assert_type(f8 > f, np.bool)
assert_type(f8 > i, np.bool)
assert_type(f8 > i8_1d, BoolND)
assert_type(f8 > i_tuple, BoolND)

assert_type(f8 > f8, np.bool)
assert_type(i8 > f8, np.bool)
assert_type(f4 > f8, np.bool)
assert_type(i4 > f8, np.bool)
assert_type(b1 > f8, np.bool)
assert_type(b > f8, np.bool)
assert_type(c > f8, np.bool)
assert_type(f > f8, np.bool)  # pyright: ignore[reportAssertTypeFailure]  # builtins.bool
assert_type(i > f8, np.bool)
assert_type(f8 < i8_1d, BoolND)
assert_type(f8 < i_tuple, BoolND)

assert_type(f4 > f8, np.bool)
assert_type(f4 > i8, np.bool)
assert_type(f4 > f4, np.bool)
assert_type(f4 > i4, np.bool)
assert_type(f4 > b1, np.bool)
assert_type(f4 > b, np.bool)
assert_type(f4 > c, np.bool)
assert_type(f4 > f, np.bool)
assert_type(f4 > i, np.bool)
assert_type(f4 > i8_1d, BoolND)
assert_type(f4 > i_tuple, BoolND)

assert_type(f8 > f4, np.bool)
assert_type(i8 > f4, np.bool)
assert_type(f4 > f4, np.bool)
assert_type(i4 > f4, np.bool)
assert_type(b1 > f4, np.bool)
assert_type(b > f4, np.bool)
assert_type(c > f4, np.bool)
assert_type(f > f4, np.bool)
assert_type(i > f4, np.bool)
assert_type(f4 < i8_1d, BoolND)
assert_type(f4 < i_tuple, BoolND)

###
# Int

assert_type(i8 > i8, np.bool)
assert_type(i8 > u8, np.bool)
assert_type(i8 > i4, np.bool)
assert_type(i8 > u4, np.bool)
assert_type(i8 > b1, np.bool)
assert_type(i8 > b, np.bool)
assert_type(i8 > c, np.bool)
assert_type(i8 > f, np.bool)
assert_type(i8 > i, np.bool)
assert_type(i8 > i8_1d, BoolND)
assert_type(i8 > i_tuple, BoolND)

assert_type(u8 > u8, np.bool)
assert_type(u8 > i4, np.bool)
assert_type(u8 > u4, np.bool)
assert_type(u8 > b1, np.bool)
assert_type(u8 > b, np.bool)
assert_type(u8 > c, np.bool)
assert_type(u8 > f, np.bool)
assert_type(u8 > i, np.bool)
assert_type(u8 > i8_1d, BoolND)
assert_type(u8 > i_tuple, BoolND)

assert_type(i8 > i8, np.bool)
assert_type(u8 > i8, np.bool)
assert_type(i4 > i8, np.bool)
assert_type(u4 > i8, np.bool)
assert_type(b1 > i8, np.bool)
assert_type(b > i8, np.bool)
assert_type(c > i8, np.bool)
assert_type(f > i8, np.bool)
assert_type(i > i8, np.bool)
assert_type(i8 < i8_1d, BoolND)
assert_type(i8 < i_tuple, BoolND)

assert_type(u8 > u8, np.bool)
assert_type(i4 > u8, np.bool)
assert_type(u4 > u8, np.bool)
assert_type(b1 > u8, np.bool)
assert_type(b > u8, np.bool)
assert_type(c > u8, np.bool)
assert_type(f > u8, np.bool)
assert_type(i > u8, np.bool)
assert_type(u8 < i8_1d, BoolND)
assert_type(u8 < i_tuple, BoolND)

assert_type(i4 > i8, np.bool)
assert_type(i4 > i4, np.bool)
assert_type(i4 > i, np.bool)
assert_type(i4 > b1, np.bool)
assert_type(i4 > b, np.bool)
assert_type(i4 > i8_1d, BoolND)
assert_type(i4 > i_tuple, BoolND)

assert_type(u4 > i8, np.bool)
assert_type(u4 > i4, np.bool)
assert_type(u4 > u8, np.bool)
assert_type(u4 > u4, np.bool)
assert_type(u4 > i, np.bool)
assert_type(u4 > b1, np.bool)
assert_type(u4 > b, np.bool)
assert_type(u4 > i8_1d, BoolND)
assert_type(u4 > i_tuple, BoolND)

assert_type(i8 > i4, np.bool)
assert_type(i4 > i4, np.bool)
assert_type(i > i4, np.bool)
assert_type(b1 > i4, np.bool)
assert_type(b > i4, np.bool)
assert_type(i4 < i8_1d, BoolND)
assert_type(i4 < i_tuple, BoolND)

assert_type(i8 > u4, np.bool)
assert_type(i4 > u4, np.bool)
assert_type(u8 > u4, np.bool)
assert_type(u4 > u4, np.bool)
assert_type(b1 > u4, np.bool)
assert_type(b > u4, np.bool)
assert_type(i > u4, np.bool)
assert_type(u4 < i8_1d, BoolND)
assert_type(u4 < i_tuple, BoolND)
