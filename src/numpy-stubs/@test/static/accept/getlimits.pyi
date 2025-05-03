from typing import Literal, assert_type

import numpy as np

f: float
f8: np.float64
c8: np.complex64

i: int
i8: np.int64
u4: np.uint32

finfo_f8: np.finfo[np.float64]
iinfo_i8: np.iinfo[np.int64]

assert_type(np.finfo(f), np.finfo[np.float64])
assert_type(np.finfo(f8), np.finfo[np.float64])
assert_type(np.finfo(c8), np.finfo[np.float32])
assert_type(np.finfo("f2"), np.finfo[np.float16])

assert_type(finfo_f8.dtype, np.dtype[np.float64])
assert_type(finfo_f8.bits, Literal[2, 4, 8, 12, 16])
assert_type(finfo_f8.eps, np.float64)
assert_type(finfo_f8.epsneg, np.float64)
assert_type(finfo_f8.iexp, int)
assert_type(finfo_f8.machep, int)
assert_type(finfo_f8.max, np.float64)
assert_type(finfo_f8.maxexp, int)
assert_type(finfo_f8.min, np.float64)
assert_type(finfo_f8.minexp, int)
assert_type(finfo_f8.negep, int)
assert_type(finfo_f8.nexp, int)
assert_type(finfo_f8.nmant, int)
assert_type(finfo_f8.precision, int)
assert_type(finfo_f8.resolution, np.float64)
assert_type(finfo_f8.tiny, np.float64)
assert_type(finfo_f8.smallest_normal, np.float64)
assert_type(finfo_f8.smallest_subnormal, np.float64)

assert_type(np.iinfo(i), np.iinfo[np.int_])
assert_type(np.iinfo(i8), np.iinfo[np.int64])
assert_type(np.iinfo(u4), np.iinfo[np.uint32])
assert_type(np.iinfo("i2"), np.iinfo[np.int16])

assert_type(iinfo_i8.dtype, np.dtype[np.int64])
assert_type(iinfo_i8.kind, Literal["i", "u"])
assert_type(iinfo_i8.bits, Literal[8, 16, 32, 64])
assert_type(iinfo_i8.key, Literal["i8", "i16", "i32", "i64", "u8", "u16", "u32", "u64"])
assert_type(iinfo_i8.min, int)
assert_type(iinfo_i8.max, int)
