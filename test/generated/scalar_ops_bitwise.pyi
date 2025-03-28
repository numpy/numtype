# @generated 2025-03-27T23:46:59Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np

###
# scalars

b_py: bool
i_py: int
f_py: float
c_py: complex

b1: np.bool
u8: np.uint8
u16: np.uint16
u32: np.uint32
u64: np.uint64
i8: np.int8
i16: np.int16
i32: np.int32
i64: np.int64
f16: np.float16
f32: np.float32
f64: np.float64
f64l: np.longdouble
c32: np.complex64
c64: np.complex128
c64l: np.clongdouble
M64: np.datetime64
m64: np.timedelta64

u: np.unsignedinteger
i: np.signedinteger
f: np.floating
c: np.complexfloating

###
# __[r]lshift__

assert_type(b1 << b_py, np.int8)
assert_type(b1 << i_py, np.int_)
b1 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 << b1, np.int8)
assert_type(b1 << u8, np.uint8)
assert_type(b1 << u16, np.uint16)
assert_type(b1 << u32, np.uint32)
assert_type(b1 << u64, np.uint64)
assert_type(b1 << i8, np.int8)
assert_type(b1 << i16, np.int16)
assert_type(b1 << i32, np.int32)
assert_type(b1 << i64, np.int64)
b1 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 << u, np.unsignedinteger)
assert_type(b1 << i, np.signedinteger)
b1 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 << b_py, np.uint8)
assert_type(u8 << i_py, np.uint8)
u8 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 << b1, np.uint8)
assert_type(u8 << u8, np.uint8)
assert_type(u8 << u16, np.uint16)
assert_type(u8 << u32, np.uint32)
assert_type(u8 << u64, np.uint64)
assert_type(u8 << i8, np.int16)
assert_type(u8 << i16, np.int16)
assert_type(u8 << i32, np.int32)
assert_type(u8 << i64, np.int64)
u8 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 << u, np.unsignedinteger)
assert_type(u8 << i, np.signedinteger)
u8 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 << b_py, np.uint16)
assert_type(u16 << i_py, np.uint16)
u16 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 << b1, np.uint16)
assert_type(u16 << u8, np.uint16)
assert_type(u16 << u16, np.uint16)
assert_type(u16 << u32, np.uint32)
assert_type(u16 << u64, np.uint64)
assert_type(u16 << i8, np.int32)
assert_type(u16 << i16, np.int32)
assert_type(u16 << i32, np.int32)
assert_type(u16 << i64, np.int64)
u16 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 << u, np.unsignedinteger)
assert_type(u16 << i, np.signedinteger)
u16 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 << b_py, np.uint32)
assert_type(u32 << i_py, np.uint32)
u32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 << b1, np.uint32)
assert_type(u32 << u8, np.uint32)
assert_type(u32 << u16, np.uint32)
assert_type(u32 << u32, np.uint32)
assert_type(u32 << u64, np.uint64)
assert_type(u32 << i8, np.int64)
assert_type(u32 << i16, np.int64)
assert_type(u32 << i32, np.int64)
assert_type(u32 << i64, np.int64)
u32 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 << u, np.unsignedinteger)
assert_type(u32 << i, np.int64)
u32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 << b_py, np.uint64)
assert_type(u64 << i_py, np.uint64)
u64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 << b1, np.uint64)
assert_type(u64 << u8, np.uint64)
assert_type(u64 << u16, np.uint64)
assert_type(u64 << u32, np.uint64)
assert_type(u64 << u64, np.uint64)
u64 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 << u, np.uint64)
u64 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 << b_py, np.int8)
assert_type(i8 << i_py, np.int8)
i8 << f_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
i8 << c_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << b1, np.int8)
assert_type(i8 << u8, np.int16)
assert_type(i8 << u16, np.int32)
assert_type(i8 << u32, np.int64)
i8 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << i8, np.int8)
assert_type(i8 << i16, np.int16)
assert_type(i8 << i32, np.int32)
assert_type(i8 << i64, np.int64)
i8 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 << u, np.signedinteger)
assert_type(i8 << i, np.signedinteger)
i8 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 << b_py, np.int16)
assert_type(i16 << i_py, np.int16)
i16 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 << b1, np.int16)
assert_type(i16 << u8, np.int16)
assert_type(i16 << u16, np.int32)
assert_type(i16 << u32, np.int64)
i16 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 << i8, np.int16)
assert_type(i16 << i16, np.int16)
assert_type(i16 << i32, np.int32)
assert_type(i16 << i64, np.int64)
i16 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 << u, np.signedinteger)
assert_type(i16 << i, np.signedinteger)
i16 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 << b_py, np.int32)
assert_type(i32 << i_py, np.int32)
i32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 << b1, np.int32)
assert_type(i32 << u8, np.int32)
assert_type(i32 << u16, np.int32)
assert_type(i32 << u32, np.int64)
i32 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 << i8, np.int32)
assert_type(i32 << i16, np.int32)
assert_type(i32 << i32, np.int32)
assert_type(i32 << i64, np.int64)
i32 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 << u, np.signedinteger)
assert_type(i32 << i, np.signedinteger)
i32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 << b_py, np.int64)
assert_type(i64 << i_py, np.int64)
i64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 << b1, np.int64)
assert_type(i64 << u8, np.int64)
assert_type(i64 << u16, np.int64)
assert_type(i64 << u32, np.int64)
i64 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 << i8, np.int64)
assert_type(i64 << i16, np.int64)
assert_type(i64 << i32, np.int64)
assert_type(i64 << i64, np.int64)
i64 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 << u, np.int64)
assert_type(i64 << i, np.int64)
i64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f16 << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f32 << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64l << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u << b_py, np.unsignedinteger)
assert_type(u << i_py, np.unsignedinteger)
u << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u << b1, np.unsignedinteger)
assert_type(u << u8, np.unsignedinteger)
assert_type(u << u16, np.unsignedinteger)
assert_type(u << u32, np.unsignedinteger)
assert_type(u << u64, np.uint64)
assert_type(u << i8, np.signedinteger)
assert_type(u << i16, np.signedinteger)
assert_type(u << i32, np.signedinteger)
assert_type(u << i64, np.int64)
u << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u << u, np.unsignedinteger)
assert_type(u << i, np.signedinteger)
u << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i << b_py, np.signedinteger)
assert_type(i << i_py, np.signedinteger)
i << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i << b1, np.signedinteger)
assert_type(i << u8, np.signedinteger)
assert_type(i << u16, np.signedinteger)
assert_type(i << u32, np.int64)
i << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i << i8, np.signedinteger)
assert_type(i << i16, np.signedinteger)
assert_type(i << i32, np.signedinteger)
assert_type(i << i64, np.int64)
i << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i << u, np.signedinteger)
assert_type(i << i, np.signedinteger)
i << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c << b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c << c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]rshift__

assert_type(b1 >> b_py, np.int8)
assert_type(b1 >> i_py, np.int_)
b1 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 >> b1, np.int8)
assert_type(b1 >> u8, np.uint8)
assert_type(b1 >> u16, np.uint16)
assert_type(b1 >> u32, np.uint32)
assert_type(b1 >> u64, np.uint64)
assert_type(b1 >> i8, np.int8)
assert_type(b1 >> i16, np.int16)
assert_type(b1 >> i32, np.int32)
assert_type(b1 >> i64, np.int64)
b1 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 >> u, np.unsignedinteger)
assert_type(b1 >> i, np.signedinteger)
b1 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 >> b_py, np.uint8)
assert_type(u8 >> i_py, np.uint8)
u8 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 >> b1, np.uint8)
assert_type(u8 >> u8, np.uint8)
assert_type(u8 >> u16, np.uint16)
assert_type(u8 >> u32, np.uint32)
assert_type(u8 >> u64, np.uint64)
assert_type(u8 >> i8, np.int16)
assert_type(u8 >> i16, np.int16)
assert_type(u8 >> i32, np.int32)
assert_type(u8 >> i64, np.int64)
u8 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 >> u, np.unsignedinteger)
assert_type(u8 >> i, np.signedinteger)
u8 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 >> b_py, np.uint16)
assert_type(u16 >> i_py, np.uint16)
u16 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 >> b1, np.uint16)
assert_type(u16 >> u8, np.uint16)
assert_type(u16 >> u16, np.uint16)
assert_type(u16 >> u32, np.uint32)
assert_type(u16 >> u64, np.uint64)
assert_type(u16 >> i8, np.int32)
assert_type(u16 >> i16, np.int32)
assert_type(u16 >> i32, np.int32)
assert_type(u16 >> i64, np.int64)
u16 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 >> u, np.unsignedinteger)
assert_type(u16 >> i, np.signedinteger)
u16 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 >> b_py, np.uint32)
assert_type(u32 >> i_py, np.uint32)
u32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 >> b1, np.uint32)
assert_type(u32 >> u8, np.uint32)
assert_type(u32 >> u16, np.uint32)
assert_type(u32 >> u32, np.uint32)
assert_type(u32 >> u64, np.uint64)
assert_type(u32 >> i8, np.int64)
assert_type(u32 >> i16, np.int64)
assert_type(u32 >> i32, np.int64)
assert_type(u32 >> i64, np.int64)
u32 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 >> u, np.unsignedinteger)
assert_type(u32 >> i, np.int64)
u32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 >> b_py, np.uint64)
assert_type(u64 >> i_py, np.uint64)
u64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 >> b1, np.uint64)
assert_type(u64 >> u8, np.uint64)
assert_type(u64 >> u16, np.uint64)
assert_type(u64 >> u32, np.uint64)
assert_type(u64 >> u64, np.uint64)
u64 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 >> u, np.uint64)
u64 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 >> b_py, np.int8)
assert_type(i8 >> i_py, np.int8)
i8 >> f_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
i8 >> c_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> b1, np.int8)
assert_type(i8 >> u8, np.int16)
assert_type(i8 >> u16, np.int32)
assert_type(i8 >> u32, np.int64)
i8 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> i8, np.int8)
assert_type(i8 >> i16, np.int16)
assert_type(i8 >> i32, np.int32)
assert_type(i8 >> i64, np.int64)
i8 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 >> u, np.signedinteger)
assert_type(i8 >> i, np.signedinteger)
i8 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 >> b_py, np.int16)
assert_type(i16 >> i_py, np.int16)
i16 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 >> b1, np.int16)
assert_type(i16 >> u8, np.int16)
assert_type(i16 >> u16, np.int32)
assert_type(i16 >> u32, np.int64)
i16 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 >> i8, np.int16)
assert_type(i16 >> i16, np.int16)
assert_type(i16 >> i32, np.int32)
assert_type(i16 >> i64, np.int64)
i16 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 >> u, np.signedinteger)
assert_type(i16 >> i, np.signedinteger)
i16 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 >> b_py, np.int32)
assert_type(i32 >> i_py, np.int32)
i32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 >> b1, np.int32)
assert_type(i32 >> u8, np.int32)
assert_type(i32 >> u16, np.int32)
assert_type(i32 >> u32, np.int64)
i32 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 >> i8, np.int32)
assert_type(i32 >> i16, np.int32)
assert_type(i32 >> i32, np.int32)
assert_type(i32 >> i64, np.int64)
i32 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 >> u, np.signedinteger)
assert_type(i32 >> i, np.signedinteger)
i32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 >> b_py, np.int64)
assert_type(i64 >> i_py, np.int64)
i64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 >> b1, np.int64)
assert_type(i64 >> u8, np.int64)
assert_type(i64 >> u16, np.int64)
assert_type(i64 >> u32, np.int64)
i64 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 >> i8, np.int64)
assert_type(i64 >> i16, np.int64)
assert_type(i64 >> i32, np.int64)
assert_type(i64 >> i64, np.int64)
i64 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 >> u, np.int64)
assert_type(i64 >> i, np.int64)
i64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f16 >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f32 >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64l >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u >> b_py, np.unsignedinteger)
assert_type(u >> i_py, np.unsignedinteger)
u >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u >> b1, np.unsignedinteger)
assert_type(u >> u8, np.unsignedinteger)
assert_type(u >> u16, np.unsignedinteger)
assert_type(u >> u32, np.unsignedinteger)
assert_type(u >> u64, np.uint64)
assert_type(u >> i8, np.signedinteger)
assert_type(u >> i16, np.signedinteger)
assert_type(u >> i32, np.signedinteger)
assert_type(u >> i64, np.int64)
u >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u >> u, np.unsignedinteger)
assert_type(u >> i, np.signedinteger)
u >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i >> b_py, np.signedinteger)
assert_type(i >> i_py, np.signedinteger)
i >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i >> b1, np.signedinteger)
assert_type(i >> u8, np.signedinteger)
assert_type(i >> u16, np.signedinteger)
assert_type(i >> u32, np.int64)
i >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i >> i8, np.signedinteger)
assert_type(i >> i16, np.signedinteger)
assert_type(i >> i32, np.signedinteger)
assert_type(i >> i64, np.int64)
i >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i >> u, np.signedinteger)
assert_type(i >> i, np.signedinteger)
i >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c >> b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c >> c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]and__

assert_type(b1 & b_py, np.bool)
assert_type(b1 & i_py, np.int_)
b1 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 & b1, np.bool)
assert_type(b1 & u8, np.uint8)
assert_type(b1 & u16, np.uint16)
assert_type(b1 & u32, np.uint32)
assert_type(b1 & u64, np.uint64)
assert_type(b1 & i8, np.int8)
assert_type(b1 & i16, np.int16)
assert_type(b1 & i32, np.int32)
assert_type(b1 & i64, np.int64)
b1 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 & u, np.unsignedinteger)
assert_type(b1 & i, np.signedinteger)
b1 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 & b_py, np.uint8)
assert_type(u8 & i_py, np.uint8)
u8 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 & b1, np.uint8)
assert_type(u8 & u8, np.uint8)
assert_type(u8 & u16, np.uint16)
assert_type(u8 & u32, np.uint32)
assert_type(u8 & u64, np.uint64)
assert_type(u8 & i8, np.int16)
assert_type(u8 & i16, np.int16)
assert_type(u8 & i32, np.int32)
assert_type(u8 & i64, np.int64)
u8 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 & u, np.unsignedinteger)
assert_type(u8 & i, np.signedinteger)
u8 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 & b_py, np.uint16)
assert_type(u16 & i_py, np.uint16)
u16 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 & b1, np.uint16)
assert_type(u16 & u8, np.uint16)
assert_type(u16 & u16, np.uint16)
assert_type(u16 & u32, np.uint32)
assert_type(u16 & u64, np.uint64)
assert_type(u16 & i8, np.int32)
assert_type(u16 & i16, np.int32)
assert_type(u16 & i32, np.int32)
assert_type(u16 & i64, np.int64)
u16 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 & u, np.unsignedinteger)
assert_type(u16 & i, np.signedinteger)
u16 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 & b_py, np.uint32)
assert_type(u32 & i_py, np.uint32)
u32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 & b1, np.uint32)
assert_type(u32 & u8, np.uint32)
assert_type(u32 & u16, np.uint32)
assert_type(u32 & u32, np.uint32)
assert_type(u32 & u64, np.uint64)
assert_type(u32 & i8, np.int64)
assert_type(u32 & i16, np.int64)
assert_type(u32 & i32, np.int64)
assert_type(u32 & i64, np.int64)
u32 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 & u, np.unsignedinteger)
assert_type(u32 & i, np.int64)
u32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 & b_py, np.uint64)
assert_type(u64 & i_py, np.uint64)
u64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 & b1, np.uint64)
assert_type(u64 & u8, np.uint64)
assert_type(u64 & u16, np.uint64)
assert_type(u64 & u32, np.uint64)
assert_type(u64 & u64, np.uint64)
u64 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 & u, np.uint64)
u64 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 & b_py, np.int8)
assert_type(i8 & i_py, np.int8)
i8 & f_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
i8 & c_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & b1, np.int8)
assert_type(i8 & u8, np.int16)
assert_type(i8 & u16, np.int32)
assert_type(i8 & u32, np.int64)
i8 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & i8, np.int8)
assert_type(i8 & i16, np.int16)
assert_type(i8 & i32, np.int32)
assert_type(i8 & i64, np.int64)
i8 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 & u, np.signedinteger)
assert_type(i8 & i, np.signedinteger)
i8 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 & b_py, np.int16)
assert_type(i16 & i_py, np.int16)
i16 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 & b1, np.int16)
assert_type(i16 & u8, np.int16)
assert_type(i16 & u16, np.int32)
assert_type(i16 & u32, np.int64)
i16 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 & i8, np.int16)
assert_type(i16 & i16, np.int16)
assert_type(i16 & i32, np.int32)
assert_type(i16 & i64, np.int64)
i16 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 & u, np.signedinteger)
assert_type(i16 & i, np.signedinteger)
i16 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 & b_py, np.int32)
assert_type(i32 & i_py, np.int32)
i32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 & b1, np.int32)
assert_type(i32 & u8, np.int32)
assert_type(i32 & u16, np.int32)
assert_type(i32 & u32, np.int64)
i32 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 & i8, np.int32)
assert_type(i32 & i16, np.int32)
assert_type(i32 & i32, np.int32)
assert_type(i32 & i64, np.int64)
i32 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 & u, np.signedinteger)
assert_type(i32 & i, np.signedinteger)
i32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 & b_py, np.int64)
assert_type(i64 & i_py, np.int64)
i64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 & b1, np.int64)
assert_type(i64 & u8, np.int64)
assert_type(i64 & u16, np.int64)
assert_type(i64 & u32, np.int64)
i64 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 & i8, np.int64)
assert_type(i64 & i16, np.int64)
assert_type(i64 & i32, np.int64)
assert_type(i64 & i64, np.int64)
i64 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 & u, np.int64)
assert_type(i64 & i, np.int64)
i64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f16 & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f32 & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64l & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u & b_py, np.unsignedinteger)
assert_type(u & i_py, np.unsignedinteger)
u & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u & b1, np.unsignedinteger)
assert_type(u & u8, np.unsignedinteger)
assert_type(u & u16, np.unsignedinteger)
assert_type(u & u32, np.unsignedinteger)
assert_type(u & u64, np.uint64)
assert_type(u & i8, np.signedinteger)
assert_type(u & i16, np.signedinteger)
assert_type(u & i32, np.signedinteger)
assert_type(u & i64, np.int64)
u & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u & u, np.unsignedinteger)
assert_type(u & i, np.signedinteger)
u & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i & b_py, np.signedinteger)
assert_type(i & i_py, np.signedinteger)
i & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i & b1, np.signedinteger)
assert_type(i & u8, np.signedinteger)
assert_type(i & u16, np.signedinteger)
assert_type(i & u32, np.int64)
i & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i & i8, np.signedinteger)
assert_type(i & i16, np.signedinteger)
assert_type(i & i32, np.signedinteger)
assert_type(i & i64, np.int64)
i & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i & u, np.signedinteger)
assert_type(i & i, np.signedinteger)
i & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c & b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c & c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]xor__

assert_type(b1 ^ b_py, np.bool)
assert_type(b1 ^ i_py, np.int_)
b1 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 ^ b1, np.bool)
assert_type(b1 ^ u8, np.uint8)
assert_type(b1 ^ u16, np.uint16)
assert_type(b1 ^ u32, np.uint32)
assert_type(b1 ^ u64, np.uint64)
assert_type(b1 ^ i8, np.int8)
assert_type(b1 ^ i16, np.int16)
assert_type(b1 ^ i32, np.int32)
assert_type(b1 ^ i64, np.int64)
b1 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 ^ u, np.unsignedinteger)
assert_type(b1 ^ i, np.signedinteger)
b1 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 ^ b_py, np.uint8)
assert_type(u8 ^ i_py, np.uint8)
u8 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 ^ b1, np.uint8)
assert_type(u8 ^ u8, np.uint8)
assert_type(u8 ^ u16, np.uint16)
assert_type(u8 ^ u32, np.uint32)
assert_type(u8 ^ u64, np.uint64)
assert_type(u8 ^ i8, np.int16)
assert_type(u8 ^ i16, np.int16)
assert_type(u8 ^ i32, np.int32)
assert_type(u8 ^ i64, np.int64)
u8 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 ^ u, np.unsignedinteger)
assert_type(u8 ^ i, np.signedinteger)
u8 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 ^ b_py, np.uint16)
assert_type(u16 ^ i_py, np.uint16)
u16 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 ^ b1, np.uint16)
assert_type(u16 ^ u8, np.uint16)
assert_type(u16 ^ u16, np.uint16)
assert_type(u16 ^ u32, np.uint32)
assert_type(u16 ^ u64, np.uint64)
assert_type(u16 ^ i8, np.int32)
assert_type(u16 ^ i16, np.int32)
assert_type(u16 ^ i32, np.int32)
assert_type(u16 ^ i64, np.int64)
u16 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 ^ u, np.unsignedinteger)
assert_type(u16 ^ i, np.signedinteger)
u16 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 ^ b_py, np.uint32)
assert_type(u32 ^ i_py, np.uint32)
u32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 ^ b1, np.uint32)
assert_type(u32 ^ u8, np.uint32)
assert_type(u32 ^ u16, np.uint32)
assert_type(u32 ^ u32, np.uint32)
assert_type(u32 ^ u64, np.uint64)
assert_type(u32 ^ i8, np.int64)
assert_type(u32 ^ i16, np.int64)
assert_type(u32 ^ i32, np.int64)
assert_type(u32 ^ i64, np.int64)
u32 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 ^ u, np.unsignedinteger)
assert_type(u32 ^ i, np.int64)
u32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 ^ b_py, np.uint64)
assert_type(u64 ^ i_py, np.uint64)
u64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 ^ b1, np.uint64)
assert_type(u64 ^ u8, np.uint64)
assert_type(u64 ^ u16, np.uint64)
assert_type(u64 ^ u32, np.uint64)
assert_type(u64 ^ u64, np.uint64)
u64 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 ^ u, np.uint64)
u64 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 ^ b_py, np.int8)
assert_type(i8 ^ i_py, np.int8)
i8 ^ f_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
i8 ^ c_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ b1, np.int8)
assert_type(i8 ^ u8, np.int16)
assert_type(i8 ^ u16, np.int32)
assert_type(i8 ^ u32, np.int64)
i8 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ i8, np.int8)
assert_type(i8 ^ i16, np.int16)
assert_type(i8 ^ i32, np.int32)
assert_type(i8 ^ i64, np.int64)
i8 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 ^ u, np.signedinteger)
assert_type(i8 ^ i, np.signedinteger)
i8 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 ^ b_py, np.int16)
assert_type(i16 ^ i_py, np.int16)
i16 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 ^ b1, np.int16)
assert_type(i16 ^ u8, np.int16)
assert_type(i16 ^ u16, np.int32)
assert_type(i16 ^ u32, np.int64)
i16 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 ^ i8, np.int16)
assert_type(i16 ^ i16, np.int16)
assert_type(i16 ^ i32, np.int32)
assert_type(i16 ^ i64, np.int64)
i16 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 ^ u, np.signedinteger)
assert_type(i16 ^ i, np.signedinteger)
i16 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 ^ b_py, np.int32)
assert_type(i32 ^ i_py, np.int32)
i32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 ^ b1, np.int32)
assert_type(i32 ^ u8, np.int32)
assert_type(i32 ^ u16, np.int32)
assert_type(i32 ^ u32, np.int64)
i32 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 ^ i8, np.int32)
assert_type(i32 ^ i16, np.int32)
assert_type(i32 ^ i32, np.int32)
assert_type(i32 ^ i64, np.int64)
i32 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 ^ u, np.signedinteger)
assert_type(i32 ^ i, np.signedinteger)
i32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 ^ b_py, np.int64)
assert_type(i64 ^ i_py, np.int64)
i64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 ^ b1, np.int64)
assert_type(i64 ^ u8, np.int64)
assert_type(i64 ^ u16, np.int64)
assert_type(i64 ^ u32, np.int64)
i64 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 ^ i8, np.int64)
assert_type(i64 ^ i16, np.int64)
assert_type(i64 ^ i32, np.int64)
assert_type(i64 ^ i64, np.int64)
i64 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 ^ u, np.int64)
assert_type(i64 ^ i, np.int64)
i64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f16 ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f32 ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64l ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u ^ b_py, np.unsignedinteger)
assert_type(u ^ i_py, np.unsignedinteger)
u ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u ^ b1, np.unsignedinteger)
assert_type(u ^ u8, np.unsignedinteger)
assert_type(u ^ u16, np.unsignedinteger)
assert_type(u ^ u32, np.unsignedinteger)
assert_type(u ^ u64, np.uint64)
assert_type(u ^ i8, np.signedinteger)
assert_type(u ^ i16, np.signedinteger)
assert_type(u ^ i32, np.signedinteger)
assert_type(u ^ i64, np.int64)
u ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u ^ u, np.unsignedinteger)
assert_type(u ^ i, np.signedinteger)
u ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i ^ b_py, np.signedinteger)
assert_type(i ^ i_py, np.signedinteger)
i ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i ^ b1, np.signedinteger)
assert_type(i ^ u8, np.signedinteger)
assert_type(i ^ u16, np.signedinteger)
assert_type(i ^ u32, np.int64)
i ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i ^ i8, np.signedinteger)
assert_type(i ^ i16, np.signedinteger)
assert_type(i ^ i32, np.signedinteger)
assert_type(i ^ i64, np.int64)
i ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i ^ u, np.signedinteger)
assert_type(i ^ i, np.signedinteger)
i ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c ^ b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c ^ c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]or__

assert_type(b1 | b_py, np.bool)
assert_type(b1 | i_py, np.int_)
b1 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 | b1, np.bool)
assert_type(b1 | u8, np.uint8)
assert_type(b1 | u16, np.uint16)
assert_type(b1 | u32, np.uint32)
assert_type(b1 | u64, np.uint64)
assert_type(b1 | i8, np.int8)
assert_type(b1 | i16, np.int16)
assert_type(b1 | i32, np.int32)
assert_type(b1 | i64, np.int64)
b1 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 | u, np.unsignedinteger)
assert_type(b1 | i, np.signedinteger)
b1 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 | b_py, np.uint8)
assert_type(u8 | i_py, np.uint8)
u8 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 | b1, np.uint8)
assert_type(u8 | u8, np.uint8)
assert_type(u8 | u16, np.uint16)
assert_type(u8 | u32, np.uint32)
assert_type(u8 | u64, np.uint64)
assert_type(u8 | i8, np.int16)
assert_type(u8 | i16, np.int16)
assert_type(u8 | i32, np.int32)
assert_type(u8 | i64, np.int64)
u8 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 | u, np.unsignedinteger)
assert_type(u8 | i, np.signedinteger)
u8 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 | b_py, np.uint16)
assert_type(u16 | i_py, np.uint16)
u16 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 | b1, np.uint16)
assert_type(u16 | u8, np.uint16)
assert_type(u16 | u16, np.uint16)
assert_type(u16 | u32, np.uint32)
assert_type(u16 | u64, np.uint64)
assert_type(u16 | i8, np.int32)
assert_type(u16 | i16, np.int32)
assert_type(u16 | i32, np.int32)
assert_type(u16 | i64, np.int64)
u16 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 | u, np.unsignedinteger)
assert_type(u16 | i, np.signedinteger)
u16 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 | b_py, np.uint32)
assert_type(u32 | i_py, np.uint32)
u32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 | b1, np.uint32)
assert_type(u32 | u8, np.uint32)
assert_type(u32 | u16, np.uint32)
assert_type(u32 | u32, np.uint32)
assert_type(u32 | u64, np.uint64)
assert_type(u32 | i8, np.int64)
assert_type(u32 | i16, np.int64)
assert_type(u32 | i32, np.int64)
assert_type(u32 | i64, np.int64)
u32 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 | u, np.unsignedinteger)
assert_type(u32 | i, np.int64)
u32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 | b_py, np.uint64)
assert_type(u64 | i_py, np.uint64)
u64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 | b1, np.uint64)
assert_type(u64 | u8, np.uint64)
assert_type(u64 | u16, np.uint64)
assert_type(u64 | u32, np.uint64)
assert_type(u64 | u64, np.uint64)
u64 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 | u, np.uint64)
u64 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 | b_py, np.int8)
assert_type(i8 | i_py, np.int8)
i8 | f_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
i8 | c_py  # type: ignore[type-var]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | b1, np.int8)
assert_type(i8 | u8, np.int16)
assert_type(i8 | u16, np.int32)
assert_type(i8 | u32, np.int64)
i8 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | i8, np.int8)
assert_type(i8 | i16, np.int16)
assert_type(i8 | i32, np.int32)
assert_type(i8 | i64, np.int64)
i8 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 | u, np.signedinteger)
assert_type(i8 | i, np.signedinteger)
i8 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 | b_py, np.int16)
assert_type(i16 | i_py, np.int16)
i16 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 | b1, np.int16)
assert_type(i16 | u8, np.int16)
assert_type(i16 | u16, np.int32)
assert_type(i16 | u32, np.int64)
i16 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 | i8, np.int16)
assert_type(i16 | i16, np.int16)
assert_type(i16 | i32, np.int32)
assert_type(i16 | i64, np.int64)
i16 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 | u, np.signedinteger)
assert_type(i16 | i, np.signedinteger)
i16 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 | b_py, np.int32)
assert_type(i32 | i_py, np.int32)
i32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 | b1, np.int32)
assert_type(i32 | u8, np.int32)
assert_type(i32 | u16, np.int32)
assert_type(i32 | u32, np.int64)
i32 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 | i8, np.int32)
assert_type(i32 | i16, np.int32)
assert_type(i32 | i32, np.int32)
assert_type(i32 | i64, np.int64)
i32 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 | u, np.signedinteger)
assert_type(i32 | i, np.signedinteger)
i32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 | b_py, np.int64)
assert_type(i64 | i_py, np.int64)
i64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 | b1, np.int64)
assert_type(i64 | u8, np.int64)
assert_type(i64 | u16, np.int64)
assert_type(i64 | u32, np.int64)
i64 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 | i8, np.int64)
assert_type(i64 | i16, np.int64)
assert_type(i64 | i32, np.int64)
assert_type(i64 | i64, np.int64)
i64 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 | u, np.int64)
assert_type(i64 | i, np.int64)
i64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f16 | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f32 | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64 | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f64l | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u | b_py, np.unsignedinteger)
assert_type(u | i_py, np.unsignedinteger)
u | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u | b1, np.unsignedinteger)
assert_type(u | u8, np.unsignedinteger)
assert_type(u | u16, np.unsignedinteger)
assert_type(u | u32, np.unsignedinteger)
assert_type(u | u64, np.uint64)
assert_type(u | i8, np.signedinteger)
assert_type(u | i16, np.signedinteger)
assert_type(u | i32, np.signedinteger)
assert_type(u | i64, np.int64)
u | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u | u, np.unsignedinteger)
assert_type(u | i, np.signedinteger)
u | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i | b_py, np.signedinteger)
assert_type(i | i_py, np.signedinteger)
i | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i | b1, np.signedinteger)
assert_type(i | u8, np.signedinteger)
assert_type(i | u16, np.signedinteger)
assert_type(i | u32, np.int64)
i | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i | i8, np.signedinteger)
assert_type(i | i16, np.signedinteger)
assert_type(i | i32, np.signedinteger)
assert_type(i | i64, np.int64)
i | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i | u, np.signedinteger)
assert_type(i | i, np.signedinteger)
i | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c | b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c | c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
