# @generated 2025-04-11T21:26:38Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np

###
# scalars

b_py: bool
i_py: int
f_py: float
c_py: complex

b1: np.bool
i8: np.int8
i16: np.int16
i32: np.int32
i64: np.int64
u8: np.uint8
u16: np.uint16
u32: np.uint32
u64: np.uint64
f64: np.float64
c128: np.complex128

i: np.signedinteger
u: np.unsignedinteger
f: np.floating
c: np.complexfloating
iu: np.integer
fc: np.inexact
iufc: np.number

###
# __[r]lshift__

assert_type(b1 << b_py, np.int8)
assert_type(b1 << i_py, np.int_)
b1 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 << b1, np.int8)
assert_type(b1 << i8, np.int8)
assert_type(b1 << i16, np.int16)
assert_type(b1 << i32, np.int32)
assert_type(b1 << i64, np.int64)
assert_type(b1 << u8, np.uint8)
assert_type(b1 << u16, np.uint16)
assert_type(b1 << u32, np.uint32)
assert_type(b1 << u64, np.uint64)
b1 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 << i, np.signedinteger)
assert_type(b1 << u, np.unsignedinteger)
b1 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 << iu, np.integer)
b1 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 << b_py, np.int8)
assert_type(i8 << i_py, np.int8)
i8 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << b1, np.int8)
assert_type(i8 << i8, np.int8)
assert_type(i8 << i16, np.int16)
assert_type(i8 << i32, np.int32)
assert_type(i8 << i64, np.int64)
assert_type(i8 << u8, np.int16)
assert_type(i8 << u16, np.int32)
assert_type(i8 << u32, np.int64)
i8 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << i, np.signedinteger)
i8 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 << b_py, np.int16)
assert_type(i16 << i_py, np.int16)
i16 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 << b1, np.int16)
assert_type(i16 << i8, np.int16)
assert_type(i16 << i16, np.int16)
assert_type(i16 << i32, np.int32)
assert_type(i16 << i64, np.int64)
assert_type(i16 << u8, np.int16)
assert_type(i16 << u16, np.int32)
assert_type(i16 << u32, np.int64)
i16 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 << i, np.signedinteger)
i16 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 << b_py, np.int32)
assert_type(i32 << i_py, np.int32)
i32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 << b1, np.int32)
assert_type(i32 << i8, np.int32)
assert_type(i32 << i16, np.int32)
assert_type(i32 << i32, np.int32)
assert_type(i32 << i64, np.int64)
assert_type(i32 << u8, np.int32)
assert_type(i32 << u16, np.int32)
assert_type(i32 << u32, np.int64)
i32 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 << i, np.signedinteger)
i32 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 << b_py, np.int64)
assert_type(i64 << i_py, np.int64)
i64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 << b1, np.int64)
assert_type(i64 << i8, np.int64)
assert_type(i64 << i16, np.int64)
assert_type(i64 << i32, np.int64)
assert_type(i64 << i64, np.int64)
assert_type(i64 << u8, np.int64)
assert_type(i64 << u16, np.int64)
assert_type(i64 << u32, np.int64)
i64 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 << i, np.int64)
i64 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 << b_py, np.uint8)
assert_type(u8 << i_py, np.uint8)
u8 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 << b1, np.uint8)
assert_type(u8 << i8, np.int16)
assert_type(u8 << i16, np.int16)
assert_type(u8 << i32, np.int32)
assert_type(u8 << i64, np.int64)
assert_type(u8 << u8, np.uint8)
assert_type(u8 << u16, np.uint16)
assert_type(u8 << u32, np.uint32)
assert_type(u8 << u64, np.uint64)
u8 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 << i, np.signedinteger)
assert_type(u8 << u, np.unsignedinteger)
u8 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 << iu, np.integer)
u8 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 << b_py, np.uint16)
assert_type(u16 << i_py, np.uint16)
u16 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 << b1, np.uint16)
assert_type(u16 << i8, np.int32)
assert_type(u16 << i16, np.int32)
assert_type(u16 << i32, np.int32)
assert_type(u16 << i64, np.int64)
assert_type(u16 << u8, np.uint16)
assert_type(u16 << u16, np.uint16)
assert_type(u16 << u32, np.uint32)
assert_type(u16 << u64, np.uint64)
u16 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 << i, np.signedinteger)
assert_type(u16 << u, np.unsignedinteger)
u16 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 << iu, np.integer)
u16 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 << b_py, np.uint32)
assert_type(u32 << i_py, np.uint32)
u32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 << b1, np.uint32)
assert_type(u32 << i8, np.int64)
assert_type(u32 << i16, np.int64)
assert_type(u32 << i32, np.int64)
assert_type(u32 << i64, np.int64)
assert_type(u32 << u8, np.uint32)
assert_type(u32 << u16, np.uint32)
assert_type(u32 << u32, np.uint32)
assert_type(u32 << u64, np.uint64)
u32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 << i, np.int64)
assert_type(u32 << u, np.unsignedinteger)
u32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 << iu, np.integer)
u32 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 << b_py, np.uint64)
assert_type(u64 << i_py, np.uint64)
u64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 << b1, np.uint64)
u64 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 << u8, np.uint64)
assert_type(u64 << u16, np.uint64)
assert_type(u64 << u32, np.uint64)
assert_type(u64 << u64, np.uint64)
u64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 << u, np.uint64)
u64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i << b_py, np.signedinteger)
assert_type(i << i_py, np.signedinteger)
assert_type(i << b1, np.signedinteger)
assert_type(i << i8, np.signedinteger)
assert_type(i << i16, np.signedinteger)
assert_type(i << i32, np.signedinteger)
assert_type(i << i64, np.int64)
assert_type(i << u8, np.signedinteger)
assert_type(i << u16, np.signedinteger)
assert_type(i << u32, np.int64)
i << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i << i, np.signedinteger)

assert_type(u << b_py, np.unsignedinteger)
assert_type(u << i_py, np.unsignedinteger)
assert_type(u << b1, np.unsignedinteger)
u << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u << u8, np.unsignedinteger)
assert_type(u << u16, np.unsignedinteger)
assert_type(u << u32, np.unsignedinteger)
assert_type(u << u64, np.uint64)
assert_type(u << u, np.unsignedinteger)

f << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu << b_py, np.integer)
assert_type(iu << i_py, np.integer)
assert_type(iu << b1, np.integer)
iu << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu << u8, np.integer)
assert_type(iu << u16, np.integer)
assert_type(iu << u32, np.integer)
iu << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]rshift__

assert_type(b1 >> b_py, np.int8)
assert_type(b1 >> i_py, np.int_)
b1 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 >> b1, np.int8)
assert_type(b1 >> i8, np.int8)
assert_type(b1 >> i16, np.int16)
assert_type(b1 >> i32, np.int32)
assert_type(b1 >> i64, np.int64)
assert_type(b1 >> u8, np.uint8)
assert_type(b1 >> u16, np.uint16)
assert_type(b1 >> u32, np.uint32)
assert_type(b1 >> u64, np.uint64)
b1 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 >> i, np.signedinteger)
assert_type(b1 >> u, np.unsignedinteger)
b1 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 >> iu, np.integer)
b1 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 >> b_py, np.int8)
assert_type(i8 >> i_py, np.int8)
i8 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> b1, np.int8)
assert_type(i8 >> i8, np.int8)
assert_type(i8 >> i16, np.int16)
assert_type(i8 >> i32, np.int32)
assert_type(i8 >> i64, np.int64)
assert_type(i8 >> u8, np.int16)
assert_type(i8 >> u16, np.int32)
assert_type(i8 >> u32, np.int64)
i8 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> i, np.signedinteger)
i8 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 >> b_py, np.int16)
assert_type(i16 >> i_py, np.int16)
i16 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 >> b1, np.int16)
assert_type(i16 >> i8, np.int16)
assert_type(i16 >> i16, np.int16)
assert_type(i16 >> i32, np.int32)
assert_type(i16 >> i64, np.int64)
assert_type(i16 >> u8, np.int16)
assert_type(i16 >> u16, np.int32)
assert_type(i16 >> u32, np.int64)
i16 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 >> i, np.signedinteger)
i16 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 >> b_py, np.int32)
assert_type(i32 >> i_py, np.int32)
i32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 >> b1, np.int32)
assert_type(i32 >> i8, np.int32)
assert_type(i32 >> i16, np.int32)
assert_type(i32 >> i32, np.int32)
assert_type(i32 >> i64, np.int64)
assert_type(i32 >> u8, np.int32)
assert_type(i32 >> u16, np.int32)
assert_type(i32 >> u32, np.int64)
i32 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 >> i, np.signedinteger)
i32 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 >> b_py, np.int64)
assert_type(i64 >> i_py, np.int64)
i64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 >> b1, np.int64)
assert_type(i64 >> i8, np.int64)
assert_type(i64 >> i16, np.int64)
assert_type(i64 >> i32, np.int64)
assert_type(i64 >> i64, np.int64)
assert_type(i64 >> u8, np.int64)
assert_type(i64 >> u16, np.int64)
assert_type(i64 >> u32, np.int64)
i64 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 >> i, np.int64)
i64 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 >> b_py, np.uint8)
assert_type(u8 >> i_py, np.uint8)
u8 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 >> b1, np.uint8)
assert_type(u8 >> i8, np.int16)
assert_type(u8 >> i16, np.int16)
assert_type(u8 >> i32, np.int32)
assert_type(u8 >> i64, np.int64)
assert_type(u8 >> u8, np.uint8)
assert_type(u8 >> u16, np.uint16)
assert_type(u8 >> u32, np.uint32)
assert_type(u8 >> u64, np.uint64)
u8 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 >> i, np.signedinteger)
assert_type(u8 >> u, np.unsignedinteger)
u8 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 >> iu, np.integer)
u8 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 >> b_py, np.uint16)
assert_type(u16 >> i_py, np.uint16)
u16 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 >> b1, np.uint16)
assert_type(u16 >> i8, np.int32)
assert_type(u16 >> i16, np.int32)
assert_type(u16 >> i32, np.int32)
assert_type(u16 >> i64, np.int64)
assert_type(u16 >> u8, np.uint16)
assert_type(u16 >> u16, np.uint16)
assert_type(u16 >> u32, np.uint32)
assert_type(u16 >> u64, np.uint64)
u16 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 >> i, np.signedinteger)
assert_type(u16 >> u, np.unsignedinteger)
u16 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 >> iu, np.integer)
u16 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 >> b_py, np.uint32)
assert_type(u32 >> i_py, np.uint32)
u32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 >> b1, np.uint32)
assert_type(u32 >> i8, np.int64)
assert_type(u32 >> i16, np.int64)
assert_type(u32 >> i32, np.int64)
assert_type(u32 >> i64, np.int64)
assert_type(u32 >> u8, np.uint32)
assert_type(u32 >> u16, np.uint32)
assert_type(u32 >> u32, np.uint32)
assert_type(u32 >> u64, np.uint64)
u32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 >> i, np.int64)
assert_type(u32 >> u, np.unsignedinteger)
u32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 >> iu, np.integer)
u32 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 >> b_py, np.uint64)
assert_type(u64 >> i_py, np.uint64)
u64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 >> b1, np.uint64)
u64 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 >> u8, np.uint64)
assert_type(u64 >> u16, np.uint64)
assert_type(u64 >> u32, np.uint64)
assert_type(u64 >> u64, np.uint64)
u64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 >> u, np.uint64)
u64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i >> b_py, np.signedinteger)
assert_type(i >> i_py, np.signedinteger)
assert_type(i >> b1, np.signedinteger)
assert_type(i >> i8, np.signedinteger)
assert_type(i >> i16, np.signedinteger)
assert_type(i >> i32, np.signedinteger)
assert_type(i >> i64, np.int64)
assert_type(i >> u8, np.signedinteger)
assert_type(i >> u16, np.signedinteger)
assert_type(i >> u32, np.int64)
i >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i >> i, np.signedinteger)

assert_type(u >> b_py, np.unsignedinteger)
assert_type(u >> i_py, np.unsignedinteger)
assert_type(u >> b1, np.unsignedinteger)
u >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u >> u8, np.unsignedinteger)
assert_type(u >> u16, np.unsignedinteger)
assert_type(u >> u32, np.unsignedinteger)
assert_type(u >> u64, np.uint64)
assert_type(u >> u, np.unsignedinteger)

f >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu >> b_py, np.integer)
assert_type(iu >> i_py, np.integer)
assert_type(iu >> b1, np.integer)
iu >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu >> u8, np.integer)
assert_type(iu >> u16, np.integer)
assert_type(iu >> u32, np.integer)
iu >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]and__

assert_type(b1 & b_py, np.bool)
assert_type(b1 & i_py, np.int_)
b1 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 & b1, np.bool)
assert_type(b1 & i8, np.int8)
assert_type(b1 & i16, np.int16)
assert_type(b1 & i32, np.int32)
assert_type(b1 & i64, np.int64)
assert_type(b1 & u8, np.uint8)
assert_type(b1 & u16, np.uint16)
assert_type(b1 & u32, np.uint32)
assert_type(b1 & u64, np.uint64)
b1 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 & i, np.signedinteger)
assert_type(b1 & u, np.unsignedinteger)
b1 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 & iu, np.integer)
b1 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 & b_py, np.int8)
assert_type(i8 & i_py, np.int8)
i8 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & b1, np.int8)
assert_type(i8 & i8, np.int8)
assert_type(i8 & i16, np.int16)
assert_type(i8 & i32, np.int32)
assert_type(i8 & i64, np.int64)
assert_type(i8 & u8, np.int16)
assert_type(i8 & u16, np.int32)
assert_type(i8 & u32, np.int64)
i8 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & i, np.signedinteger)
i8 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 & b_py, np.int16)
assert_type(i16 & i_py, np.int16)
i16 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 & b1, np.int16)
assert_type(i16 & i8, np.int16)
assert_type(i16 & i16, np.int16)
assert_type(i16 & i32, np.int32)
assert_type(i16 & i64, np.int64)
assert_type(i16 & u8, np.int16)
assert_type(i16 & u16, np.int32)
assert_type(i16 & u32, np.int64)
i16 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 & i, np.signedinteger)
i16 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 & b_py, np.int32)
assert_type(i32 & i_py, np.int32)
i32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 & b1, np.int32)
assert_type(i32 & i8, np.int32)
assert_type(i32 & i16, np.int32)
assert_type(i32 & i32, np.int32)
assert_type(i32 & i64, np.int64)
assert_type(i32 & u8, np.int32)
assert_type(i32 & u16, np.int32)
assert_type(i32 & u32, np.int64)
i32 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 & i, np.signedinteger)
i32 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 & b_py, np.int64)
assert_type(i64 & i_py, np.int64)
i64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 & b1, np.int64)
assert_type(i64 & i8, np.int64)
assert_type(i64 & i16, np.int64)
assert_type(i64 & i32, np.int64)
assert_type(i64 & i64, np.int64)
assert_type(i64 & u8, np.int64)
assert_type(i64 & u16, np.int64)
assert_type(i64 & u32, np.int64)
i64 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 & i, np.int64)
i64 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 & b_py, np.uint8)
assert_type(u8 & i_py, np.uint8)
u8 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 & b1, np.uint8)
assert_type(u8 & i8, np.int16)
assert_type(u8 & i16, np.int16)
assert_type(u8 & i32, np.int32)
assert_type(u8 & i64, np.int64)
assert_type(u8 & u8, np.uint8)
assert_type(u8 & u16, np.uint16)
assert_type(u8 & u32, np.uint32)
assert_type(u8 & u64, np.uint64)
u8 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 & i, np.signedinteger)
assert_type(u8 & u, np.unsignedinteger)
u8 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 & iu, np.integer)
u8 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 & b_py, np.uint16)
assert_type(u16 & i_py, np.uint16)
u16 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 & b1, np.uint16)
assert_type(u16 & i8, np.int32)
assert_type(u16 & i16, np.int32)
assert_type(u16 & i32, np.int32)
assert_type(u16 & i64, np.int64)
assert_type(u16 & u8, np.uint16)
assert_type(u16 & u16, np.uint16)
assert_type(u16 & u32, np.uint32)
assert_type(u16 & u64, np.uint64)
u16 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 & i, np.signedinteger)
assert_type(u16 & u, np.unsignedinteger)
u16 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 & iu, np.integer)
u16 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 & b_py, np.uint32)
assert_type(u32 & i_py, np.uint32)
u32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 & b1, np.uint32)
assert_type(u32 & i8, np.int64)
assert_type(u32 & i16, np.int64)
assert_type(u32 & i32, np.int64)
assert_type(u32 & i64, np.int64)
assert_type(u32 & u8, np.uint32)
assert_type(u32 & u16, np.uint32)
assert_type(u32 & u32, np.uint32)
assert_type(u32 & u64, np.uint64)
u32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 & i, np.int64)
assert_type(u32 & u, np.unsignedinteger)
u32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 & iu, np.integer)
u32 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 & b_py, np.uint64)
assert_type(u64 & i_py, np.uint64)
u64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 & b1, np.uint64)
u64 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 & u8, np.uint64)
assert_type(u64 & u16, np.uint64)
assert_type(u64 & u32, np.uint64)
assert_type(u64 & u64, np.uint64)
u64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 & u, np.uint64)
u64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i & b_py, np.signedinteger)
assert_type(i & i_py, np.signedinteger)
assert_type(i & b1, np.signedinteger)
assert_type(i & i8, np.signedinteger)
assert_type(i & i16, np.signedinteger)
assert_type(i & i32, np.signedinteger)
assert_type(i & i64, np.int64)
assert_type(i & u8, np.signedinteger)
assert_type(i & u16, np.signedinteger)
assert_type(i & u32, np.int64)
i & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i & i, np.signedinteger)

assert_type(u & b_py, np.unsignedinteger)
assert_type(u & i_py, np.unsignedinteger)
assert_type(u & b1, np.unsignedinteger)
u & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u & u8, np.unsignedinteger)
assert_type(u & u16, np.unsignedinteger)
assert_type(u & u32, np.unsignedinteger)
assert_type(u & u64, np.uint64)
assert_type(u & u, np.unsignedinteger)

f & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu & b_py, np.integer)
assert_type(iu & i_py, np.integer)
assert_type(iu & b1, np.integer)
iu & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu & u8, np.integer)
assert_type(iu & u16, np.integer)
assert_type(iu & u32, np.integer)
iu & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]xor__

assert_type(b1 ^ b_py, np.bool)
assert_type(b1 ^ i_py, np.int_)
b1 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 ^ b1, np.bool)
assert_type(b1 ^ i8, np.int8)
assert_type(b1 ^ i16, np.int16)
assert_type(b1 ^ i32, np.int32)
assert_type(b1 ^ i64, np.int64)
assert_type(b1 ^ u8, np.uint8)
assert_type(b1 ^ u16, np.uint16)
assert_type(b1 ^ u32, np.uint32)
assert_type(b1 ^ u64, np.uint64)
b1 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 ^ i, np.signedinteger)
assert_type(b1 ^ u, np.unsignedinteger)
b1 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 ^ iu, np.integer)
b1 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 ^ b_py, np.int8)
assert_type(i8 ^ i_py, np.int8)
i8 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ b1, np.int8)
assert_type(i8 ^ i8, np.int8)
assert_type(i8 ^ i16, np.int16)
assert_type(i8 ^ i32, np.int32)
assert_type(i8 ^ i64, np.int64)
assert_type(i8 ^ u8, np.int16)
assert_type(i8 ^ u16, np.int32)
assert_type(i8 ^ u32, np.int64)
i8 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ i, np.signedinteger)
i8 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 ^ b_py, np.int16)
assert_type(i16 ^ i_py, np.int16)
i16 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 ^ b1, np.int16)
assert_type(i16 ^ i8, np.int16)
assert_type(i16 ^ i16, np.int16)
assert_type(i16 ^ i32, np.int32)
assert_type(i16 ^ i64, np.int64)
assert_type(i16 ^ u8, np.int16)
assert_type(i16 ^ u16, np.int32)
assert_type(i16 ^ u32, np.int64)
i16 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 ^ i, np.signedinteger)
i16 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 ^ b_py, np.int32)
assert_type(i32 ^ i_py, np.int32)
i32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 ^ b1, np.int32)
assert_type(i32 ^ i8, np.int32)
assert_type(i32 ^ i16, np.int32)
assert_type(i32 ^ i32, np.int32)
assert_type(i32 ^ i64, np.int64)
assert_type(i32 ^ u8, np.int32)
assert_type(i32 ^ u16, np.int32)
assert_type(i32 ^ u32, np.int64)
i32 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 ^ i, np.signedinteger)
i32 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 ^ b_py, np.int64)
assert_type(i64 ^ i_py, np.int64)
i64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 ^ b1, np.int64)
assert_type(i64 ^ i8, np.int64)
assert_type(i64 ^ i16, np.int64)
assert_type(i64 ^ i32, np.int64)
assert_type(i64 ^ i64, np.int64)
assert_type(i64 ^ u8, np.int64)
assert_type(i64 ^ u16, np.int64)
assert_type(i64 ^ u32, np.int64)
i64 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 ^ i, np.int64)
i64 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 ^ b_py, np.uint8)
assert_type(u8 ^ i_py, np.uint8)
u8 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 ^ b1, np.uint8)
assert_type(u8 ^ i8, np.int16)
assert_type(u8 ^ i16, np.int16)
assert_type(u8 ^ i32, np.int32)
assert_type(u8 ^ i64, np.int64)
assert_type(u8 ^ u8, np.uint8)
assert_type(u8 ^ u16, np.uint16)
assert_type(u8 ^ u32, np.uint32)
assert_type(u8 ^ u64, np.uint64)
u8 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 ^ i, np.signedinteger)
assert_type(u8 ^ u, np.unsignedinteger)
u8 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 ^ iu, np.integer)
u8 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 ^ b_py, np.uint16)
assert_type(u16 ^ i_py, np.uint16)
u16 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 ^ b1, np.uint16)
assert_type(u16 ^ i8, np.int32)
assert_type(u16 ^ i16, np.int32)
assert_type(u16 ^ i32, np.int32)
assert_type(u16 ^ i64, np.int64)
assert_type(u16 ^ u8, np.uint16)
assert_type(u16 ^ u16, np.uint16)
assert_type(u16 ^ u32, np.uint32)
assert_type(u16 ^ u64, np.uint64)
u16 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 ^ i, np.signedinteger)
assert_type(u16 ^ u, np.unsignedinteger)
u16 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 ^ iu, np.integer)
u16 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 ^ b_py, np.uint32)
assert_type(u32 ^ i_py, np.uint32)
u32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 ^ b1, np.uint32)
assert_type(u32 ^ i8, np.int64)
assert_type(u32 ^ i16, np.int64)
assert_type(u32 ^ i32, np.int64)
assert_type(u32 ^ i64, np.int64)
assert_type(u32 ^ u8, np.uint32)
assert_type(u32 ^ u16, np.uint32)
assert_type(u32 ^ u32, np.uint32)
assert_type(u32 ^ u64, np.uint64)
u32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 ^ i, np.int64)
assert_type(u32 ^ u, np.unsignedinteger)
u32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 ^ iu, np.integer)
u32 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 ^ b_py, np.uint64)
assert_type(u64 ^ i_py, np.uint64)
u64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 ^ b1, np.uint64)
u64 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 ^ u8, np.uint64)
assert_type(u64 ^ u16, np.uint64)
assert_type(u64 ^ u32, np.uint64)
assert_type(u64 ^ u64, np.uint64)
u64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 ^ u, np.uint64)
u64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i ^ b_py, np.signedinteger)
assert_type(i ^ i_py, np.signedinteger)
assert_type(i ^ b1, np.signedinteger)
assert_type(i ^ i8, np.signedinteger)
assert_type(i ^ i16, np.signedinteger)
assert_type(i ^ i32, np.signedinteger)
assert_type(i ^ i64, np.int64)
assert_type(i ^ u8, np.signedinteger)
assert_type(i ^ u16, np.signedinteger)
assert_type(i ^ u32, np.int64)
i ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i ^ i, np.signedinteger)

assert_type(u ^ b_py, np.unsignedinteger)
assert_type(u ^ i_py, np.unsignedinteger)
assert_type(u ^ b1, np.unsignedinteger)
u ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u ^ u8, np.unsignedinteger)
assert_type(u ^ u16, np.unsignedinteger)
assert_type(u ^ u32, np.unsignedinteger)
assert_type(u ^ u64, np.uint64)
assert_type(u ^ u, np.unsignedinteger)

f ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu ^ b_py, np.integer)
assert_type(iu ^ i_py, np.integer)
assert_type(iu ^ b1, np.integer)
iu ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu ^ u8, np.integer)
assert_type(iu ^ u16, np.integer)
assert_type(iu ^ u32, np.integer)
iu ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]or__

assert_type(b1 | b_py, np.bool)
assert_type(b1 | i_py, np.int_)
b1 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 | b1, np.bool)
assert_type(b1 | i8, np.int8)
assert_type(b1 | i16, np.int16)
assert_type(b1 | i32, np.int32)
assert_type(b1 | i64, np.int64)
assert_type(b1 | u8, np.uint8)
assert_type(b1 | u16, np.uint16)
assert_type(b1 | u32, np.uint32)
assert_type(b1 | u64, np.uint64)
b1 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 | i, np.signedinteger)
assert_type(b1 | u, np.unsignedinteger)
b1 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 | iu, np.integer)
b1 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 | b_py, np.int8)
assert_type(i8 | i_py, np.int8)
i8 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | b1, np.int8)
assert_type(i8 | i8, np.int8)
assert_type(i8 | i16, np.int16)
assert_type(i8 | i32, np.int32)
assert_type(i8 | i64, np.int64)
assert_type(i8 | u8, np.int16)
assert_type(i8 | u16, np.int32)
assert_type(i8 | u32, np.int64)
i8 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | i, np.signedinteger)
i8 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 | b_py, np.int16)
assert_type(i16 | i_py, np.int16)
i16 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 | b1, np.int16)
assert_type(i16 | i8, np.int16)
assert_type(i16 | i16, np.int16)
assert_type(i16 | i32, np.int32)
assert_type(i16 | i64, np.int64)
assert_type(i16 | u8, np.int16)
assert_type(i16 | u16, np.int32)
assert_type(i16 | u32, np.int64)
i16 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 | i, np.signedinteger)
i16 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 | b_py, np.int32)
assert_type(i32 | i_py, np.int32)
i32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 | b1, np.int32)
assert_type(i32 | i8, np.int32)
assert_type(i32 | i16, np.int32)
assert_type(i32 | i32, np.int32)
assert_type(i32 | i64, np.int64)
assert_type(i32 | u8, np.int32)
assert_type(i32 | u16, np.int32)
assert_type(i32 | u32, np.int64)
i32 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 | i, np.signedinteger)
i32 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 | b_py, np.int64)
assert_type(i64 | i_py, np.int64)
i64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 | b1, np.int64)
assert_type(i64 | i8, np.int64)
assert_type(i64 | i16, np.int64)
assert_type(i64 | i32, np.int64)
assert_type(i64 | i64, np.int64)
assert_type(i64 | u8, np.int64)
assert_type(i64 | u16, np.int64)
assert_type(i64 | u32, np.int64)
i64 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 | i, np.int64)
i64 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 | b_py, np.uint8)
assert_type(u8 | i_py, np.uint8)
u8 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 | b1, np.uint8)
assert_type(u8 | i8, np.int16)
assert_type(u8 | i16, np.int16)
assert_type(u8 | i32, np.int32)
assert_type(u8 | i64, np.int64)
assert_type(u8 | u8, np.uint8)
assert_type(u8 | u16, np.uint16)
assert_type(u8 | u32, np.uint32)
assert_type(u8 | u64, np.uint64)
u8 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 | i, np.signedinteger)
assert_type(u8 | u, np.unsignedinteger)
u8 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 | iu, np.integer)
u8 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 | b_py, np.uint16)
assert_type(u16 | i_py, np.uint16)
u16 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 | b1, np.uint16)
assert_type(u16 | i8, np.int32)
assert_type(u16 | i16, np.int32)
assert_type(u16 | i32, np.int32)
assert_type(u16 | i64, np.int64)
assert_type(u16 | u8, np.uint16)
assert_type(u16 | u16, np.uint16)
assert_type(u16 | u32, np.uint32)
assert_type(u16 | u64, np.uint64)
u16 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 | i, np.signedinteger)
assert_type(u16 | u, np.unsignedinteger)
u16 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 | iu, np.integer)
u16 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 | b_py, np.uint32)
assert_type(u32 | i_py, np.uint32)
u32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 | b1, np.uint32)
assert_type(u32 | i8, np.int64)
assert_type(u32 | i16, np.int64)
assert_type(u32 | i32, np.int64)
assert_type(u32 | i64, np.int64)
assert_type(u32 | u8, np.uint32)
assert_type(u32 | u16, np.uint32)
assert_type(u32 | u32, np.uint32)
assert_type(u32 | u64, np.uint64)
u32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 | i, np.int64)
assert_type(u32 | u, np.unsignedinteger)
u32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 | iu, np.integer)
u32 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 | b_py, np.uint64)
assert_type(u64 | i_py, np.uint64)
u64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 | b1, np.uint64)
u64 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 | u8, np.uint64)
assert_type(u64 | u16, np.uint64)
assert_type(u64 | u32, np.uint64)
assert_type(u64 | u64, np.uint64)
u64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 | u, np.uint64)
u64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i | b_py, np.signedinteger)
assert_type(i | i_py, np.signedinteger)
assert_type(i | b1, np.signedinteger)
assert_type(i | i8, np.signedinteger)
assert_type(i | i16, np.signedinteger)
assert_type(i | i32, np.signedinteger)
assert_type(i | i64, np.int64)
assert_type(i | u8, np.signedinteger)
assert_type(i | u16, np.signedinteger)
assert_type(i | u32, np.int64)
i | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i | i, np.signedinteger)

assert_type(u | b_py, np.unsignedinteger)
assert_type(u | i_py, np.unsignedinteger)
assert_type(u | b1, np.unsignedinteger)
u | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u | u8, np.unsignedinteger)
assert_type(u | u16, np.unsignedinteger)
assert_type(u | u32, np.unsignedinteger)
assert_type(u | u64, np.uint64)
assert_type(u | u, np.unsignedinteger)

f | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu | b_py, np.integer)
assert_type(iu | i_py, np.integer)
assert_type(iu | b1, np.integer)
iu | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu | u8, np.integer)
assert_type(iu | u16, np.integer)
assert_type(iu | u32, np.integer)
iu | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
