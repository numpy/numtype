# @generated 2025-03-27T02:38:39Z with tool/testgen.py
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

f: np.floating
c: np.complexfloating

###
# __[r]floordiv__

assert_type(b1 // b_py, np.int8)
assert_type(b1 // i_py, np.int_)
assert_type(b1 // f_py, np.float64)
b1 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 // b1, np.int8)
assert_type(b1 // u8, np.uint8)
assert_type(b1 // u16, np.uint16)
assert_type(b1 // u32, np.uint32)
assert_type(b1 // u64, np.uint64)
assert_type(b1 // i8, np.int8)
assert_type(b1 // i16, np.int16)
assert_type(b1 // i32, np.int32)
assert_type(b1 // i64, np.int64)
assert_type(b1 // f16, np.float16)
assert_type(b1 // f32, np.float32)
assert_type(b1 // f64, np.float64)
assert_type(b1 // f64l, np.longdouble)
b1 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 // f, np.floating)
b1 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 // b_py, np.uint8)
assert_type(u8 // i_py, np.uint8)
assert_type(u8 // f_py, np.float64)
u8 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 // b1, np.uint8)
assert_type(u8 // u8, np.uint8)
assert_type(u8 // u16, np.uint16)
assert_type(u8 // u32, np.uint32)
assert_type(u8 // u64, np.uint64)
assert_type(u8 // i8, np.int16)
assert_type(u8 // i16, np.int16)
assert_type(u8 // i32, np.int32)
assert_type(u8 // i64, np.int64)
assert_type(u8 // f16, np.float16)
assert_type(u8 // f32, np.float32)
assert_type(u8 // f64, np.float64)
assert_type(u8 // f64l, np.longdouble)
u8 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 // f, np.floating)
u8 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 // b_py, np.uint16)
assert_type(u16 // i_py, np.uint16)
assert_type(u16 // f_py, np.float64)
u16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 // b1, np.uint16)
assert_type(u16 // u8, np.uint16)
assert_type(u16 // u16, np.uint16)
assert_type(u16 // u32, np.uint32)
assert_type(u16 // u64, np.uint64)
assert_type(u16 // i8, np.int32)
assert_type(u16 // i16, np.int32)
assert_type(u16 // i32, np.int32)
assert_type(u16 // i64, np.int64)
assert_type(u16 // f16, np.float32)
assert_type(u16 // f32, np.float32)
assert_type(u16 // f64, np.float64)
assert_type(u16 // f64l, np.longdouble)
u16 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 // f, np.floating)
u16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 // b_py, np.uint32)
assert_type(u32 // i_py, np.uint32)
assert_type(u32 // f_py, np.float64)
u32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 // b1, np.uint32)
assert_type(u32 // u8, np.uint32)
assert_type(u32 // u16, np.uint32)
assert_type(u32 // u32, np.uint32)
assert_type(u32 // u64, np.uint64)
assert_type(u32 // i8, np.int64)
assert_type(u32 // i16, np.int64)
assert_type(u32 // i32, np.int64)
assert_type(u32 // i64, np.int64)
assert_type(u32 // f16, np.float64)
assert_type(u32 // f32, np.float64)
assert_type(u32 // f64, np.float64)
assert_type(u32 // f64l, np.longdouble)
u32 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 // f, np.floating)
u32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 // b_py, np.uint64)
assert_type(u64 // i_py, np.uint64)
assert_type(u64 // f_py, np.float64)
u64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 // b1, np.uint64)
assert_type(u64 // u8, np.uint64)
assert_type(u64 // u16, np.uint64)
assert_type(u64 // u32, np.uint64)
assert_type(u64 // u64, np.uint64)
assert_type(u64 // i8, np.float64)
assert_type(u64 // i16, np.float64)
assert_type(u64 // i32, np.float64)
assert_type(u64 // i64, np.float64)
assert_type(u64 // f16, np.float64)
assert_type(u64 // f32, np.float64)
assert_type(u64 // f64, np.float64)
assert_type(u64 // f64l, np.longdouble)
u64 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 // f, np.floating)
u64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 // b_py, np.int8)
assert_type(i8 // i_py, np.int8)
assert_type(i8 // f_py, np.float64)
i8 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 // b1, np.int8)
assert_type(i8 // u8, np.int16)
assert_type(i8 // u16, np.int32)
assert_type(i8 // u32, np.int64)
assert_type(i8 // u64, np.float64)
assert_type(i8 // i8, np.int8)
assert_type(i8 // i16, np.int16)
assert_type(i8 // i32, np.int32)
assert_type(i8 // i64, np.int64)
assert_type(i8 // f16, np.float16)
assert_type(i8 // f32, np.float32)
assert_type(i8 // f64, np.float64)
assert_type(i8 // f64l, np.longdouble)
i8 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 // f, np.floating)
i8 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 // b_py, np.int16)
assert_type(i16 // i_py, np.int16)
assert_type(i16 // f_py, np.float64)
i16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 // b1, np.int16)
assert_type(i16 // u8, np.int16)
assert_type(i16 // u16, np.int32)
assert_type(i16 // u32, np.int64)
assert_type(i16 // u64, np.float64)
assert_type(i16 // i8, np.int16)
assert_type(i16 // i16, np.int16)
assert_type(i16 // i32, np.int32)
assert_type(i16 // i64, np.int64)
assert_type(i16 // f16, np.float32)
assert_type(i16 // f32, np.float32)
assert_type(i16 // f64, np.float64)
assert_type(i16 // f64l, np.longdouble)
i16 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 // f, np.floating)
i16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 // b_py, np.int32)
assert_type(i32 // i_py, np.int32)
assert_type(i32 // f_py, np.float64)
i32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 // b1, np.int32)
assert_type(i32 // u8, np.int32)
assert_type(i32 // u16, np.int32)
assert_type(i32 // u32, np.int64)
assert_type(i32 // u64, np.float64)
assert_type(i32 // i8, np.int32)
assert_type(i32 // i16, np.int32)
assert_type(i32 // i32, np.int32)
assert_type(i32 // i64, np.int64)
assert_type(i32 // f16, np.float64)
assert_type(i32 // f32, np.float64)
assert_type(i32 // f64, np.float64)
assert_type(i32 // f64l, np.longdouble)
i32 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 // f, np.floating)
i32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 // b_py, np.int64)
assert_type(i64 // i_py, np.int64)
assert_type(i64 // f_py, np.float64)
i64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 // b1, np.int64)
assert_type(i64 // u8, np.int64)
assert_type(i64 // u16, np.int64)
assert_type(i64 // u32, np.int64)
assert_type(i64 // u64, np.float64)
assert_type(i64 // i8, np.int64)
assert_type(i64 // i16, np.int64)
assert_type(i64 // i32, np.int64)
assert_type(i64 // i64, np.int64)
assert_type(i64 // f16, np.float64)
assert_type(i64 // f32, np.float64)
assert_type(i64 // f64, np.float64)
assert_type(i64 // f64l, np.longdouble)
i64 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 // f, np.floating)
i64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f16 // b_py, np.float16)
assert_type(f16 // i_py, np.float16)
assert_type(f16 // f_py, np.float16)
f16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 // b1, np.float16)
assert_type(f16 // u8, np.float16)
assert_type(f16 // u16, np.float32)
assert_type(f16 // u32, np.float64)
assert_type(f16 // u64, np.float64)
assert_type(f16 // i8, np.float16)
assert_type(f16 // i16, np.float32)
assert_type(f16 // i32, np.float64)
assert_type(f16 // i64, np.float64)
assert_type(f16 // f16, np.float16)
assert_type(f16 // f32, np.float32)
assert_type(f16 // f64, np.float64)
assert_type(f16 // f64l, np.longdouble)
f16 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 // f, np.floating)
f16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f32 // b_py, np.float32)
assert_type(f32 // i_py, np.float32)
assert_type(f32 // f_py, np.float32)
f32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 // b1, np.float32)
assert_type(f32 // u8, np.float32)
assert_type(f32 // u16, np.float32)
assert_type(f32 // u32, np.float64)
assert_type(f32 // u64, np.float64)
assert_type(f32 // i8, np.float32)
assert_type(f32 // i16, np.float32)
assert_type(f32 // i32, np.float64)
assert_type(f32 // i64, np.float64)
assert_type(f32 // f16, np.float32)
assert_type(f32 // f32, np.float32)
assert_type(f32 // f64, np.float64)
assert_type(f32 // f64l, np.longdouble)
f32 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 // f, np.floating)
f32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64 // b_py, np.float64)
assert_type(f64 // i_py, np.float64)
assert_type(f64 // f_py, np.float64)
f64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 // b1, np.float64)
assert_type(f64 // u8, np.float64)
assert_type(f64 // u16, np.float64)
assert_type(f64 // u32, np.float64)
assert_type(f64 // u64, np.float64)
assert_type(f64 // i8, np.float64)
assert_type(f64 // i16, np.float64)
assert_type(f64 // i32, np.float64)
assert_type(f64 // i64, np.float64)
assert_type(f64 // f16, np.float64)
assert_type(f64 // f32, np.float64)
assert_type(f64 // f64, np.float64)
assert_type(f64 // f64l, np.longdouble)
f64 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 // f, np.floating)
f64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64l // b_py, np.longdouble)
assert_type(f64l // i_py, np.longdouble)
assert_type(f64l // f_py, np.longdouble)
f64l // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l // b1, np.longdouble)
assert_type(f64l // u8, np.longdouble)
assert_type(f64l // u16, np.longdouble)
assert_type(f64l // u32, np.longdouble)
assert_type(f64l // u64, np.longdouble)
assert_type(f64l // i8, np.longdouble)
assert_type(f64l // i16, np.longdouble)
assert_type(f64l // i32, np.longdouble)
assert_type(f64l // i64, np.longdouble)
assert_type(f64l // f16, np.longdouble)
assert_type(f64l // f32, np.longdouble)
assert_type(f64l // f64, np.longdouble)
assert_type(f64l // f64l, np.longdouble)
f64l // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l // f, np.longdouble)
f64l // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m64 // i_py, np.timedelta64)
assert_type(m64 // f_py, np.timedelta64)
assert_type(m64 // u8, np.timedelta64)
assert_type(m64 // u16, np.timedelta64)
assert_type(m64 // u32, np.timedelta64)
assert_type(m64 // u64, np.timedelta64)
assert_type(m64 // i8, np.timedelta64)
assert_type(m64 // i16, np.timedelta64)
assert_type(m64 // i32, np.timedelta64)
assert_type(m64 // i64, np.timedelta64)
assert_type(m64 // f16, np.timedelta64)
assert_type(m64 // f32, np.timedelta64)
assert_type(m64 // f64, np.timedelta64)
assert_type(m64 // f64l, np.timedelta64)
assert_type(m64 // m64, np.int64)
assert_type(m64 // f, np.timedelta64)

assert_type(f // b_py, np.floating)
assert_type(f // i_py, np.floating)
assert_type(f // f_py, np.floating)
f // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f // b1, np.floating)
assert_type(f // u8, np.floating)
assert_type(f // u16, np.floating)
assert_type(f // u32, np.floating)
assert_type(f // u64, np.floating)
assert_type(f // i8, np.floating)
assert_type(f // i16, np.floating)
assert_type(f // i32, np.floating)
assert_type(f // i64, np.floating)
assert_type(f // f16, np.floating)
assert_type(f // f32, np.floating)
assert_type(f // f64, np.floating)
assert_type(f // f64l, np.longdouble)
f // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f // f, np.floating)
f // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]mod__

assert_type(b1 % b_py, np.int8)
assert_type(b1 % i_py, np.int_)
assert_type(b1 % f_py, np.float64)
b1 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 % b1, np.int8)
assert_type(b1 % u8, np.uint8)
assert_type(b1 % u16, np.uint16)
assert_type(b1 % u32, np.uint32)
assert_type(b1 % u64, np.uint64)
assert_type(b1 % i8, np.int8)
assert_type(b1 % i16, np.int16)
assert_type(b1 % i32, np.int32)
assert_type(b1 % i64, np.int64)
assert_type(b1 % f16, np.float16)
assert_type(b1 % f32, np.float32)
assert_type(b1 % f64, np.float64)
assert_type(b1 % f64l, np.longdouble)
b1 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 % f, np.floating)
b1 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 % b_py, np.uint8)
assert_type(u8 % i_py, np.uint8)
assert_type(u8 % f_py, np.float64)
u8 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 % b1, np.uint8)
assert_type(u8 % u8, np.uint8)
assert_type(u8 % u16, np.uint16)
assert_type(u8 % u32, np.uint32)
assert_type(u8 % u64, np.uint64)
assert_type(u8 % i8, np.int16)
assert_type(u8 % i16, np.int16)
assert_type(u8 % i32, np.int32)
assert_type(u8 % i64, np.int64)
assert_type(u8 % f16, np.float16)
assert_type(u8 % f32, np.float32)
assert_type(u8 % f64, np.float64)
assert_type(u8 % f64l, np.longdouble)
u8 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 % f, np.floating)
u8 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 % b_py, np.uint16)
assert_type(u16 % i_py, np.uint16)
assert_type(u16 % f_py, np.float64)
u16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 % b1, np.uint16)
assert_type(u16 % u8, np.uint16)
assert_type(u16 % u16, np.uint16)
assert_type(u16 % u32, np.uint32)
assert_type(u16 % u64, np.uint64)
assert_type(u16 % i8, np.int32)
assert_type(u16 % i16, np.int32)
assert_type(u16 % i32, np.int32)
assert_type(u16 % i64, np.int64)
assert_type(u16 % f16, np.float32)
assert_type(u16 % f32, np.float32)
assert_type(u16 % f64, np.float64)
assert_type(u16 % f64l, np.longdouble)
u16 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 % f, np.floating)
u16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 % b_py, np.uint32)
assert_type(u32 % i_py, np.uint32)
assert_type(u32 % f_py, np.float64)
u32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 % b1, np.uint32)
assert_type(u32 % u8, np.uint32)
assert_type(u32 % u16, np.uint32)
assert_type(u32 % u32, np.uint32)
assert_type(u32 % u64, np.uint64)
assert_type(u32 % i8, np.int64)
assert_type(u32 % i16, np.int64)
assert_type(u32 % i32, np.int64)
assert_type(u32 % i64, np.int64)
assert_type(u32 % f16, np.float64)
assert_type(u32 % f32, np.float64)
assert_type(u32 % f64, np.float64)
assert_type(u32 % f64l, np.longdouble)
u32 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 % f, np.floating)
u32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 % b_py, np.uint64)
assert_type(u64 % i_py, np.uint64)
assert_type(u64 % f_py, np.float64)
u64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 % b1, np.uint64)
assert_type(u64 % u8, np.uint64)
assert_type(u64 % u16, np.uint64)
assert_type(u64 % u32, np.uint64)
assert_type(u64 % u64, np.uint64)
assert_type(u64 % i8, np.float64)
assert_type(u64 % i16, np.float64)
assert_type(u64 % i32, np.float64)
assert_type(u64 % i64, np.float64)
assert_type(u64 % f16, np.float64)
assert_type(u64 % f32, np.float64)
assert_type(u64 % f64, np.float64)
assert_type(u64 % f64l, np.longdouble)
u64 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 % f, np.floating)
u64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 % b_py, np.int8)
assert_type(i8 % i_py, np.int8)
assert_type(i8 % f_py, np.float64)
i8 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 % b1, np.int8)
assert_type(i8 % u8, np.int16)
assert_type(i8 % u16, np.int32)
assert_type(i8 % u32, np.int64)
assert_type(i8 % u64, np.float64)
assert_type(i8 % i8, np.int8)
assert_type(i8 % i16, np.int16)
assert_type(i8 % i32, np.int32)
assert_type(i8 % i64, np.int64)
assert_type(i8 % f16, np.float16)
assert_type(i8 % f32, np.float32)
assert_type(i8 % f64, np.float64)
assert_type(i8 % f64l, np.longdouble)
i8 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 % f, np.floating)
i8 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 % b_py, np.int16)
assert_type(i16 % i_py, np.int16)
assert_type(i16 % f_py, np.float64)
i16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 % b1, np.int16)
assert_type(i16 % u8, np.int16)
assert_type(i16 % u16, np.int32)
assert_type(i16 % u32, np.int64)
assert_type(i16 % u64, np.float64)
assert_type(i16 % i8, np.int16)
assert_type(i16 % i16, np.int16)
assert_type(i16 % i32, np.int32)
assert_type(i16 % i64, np.int64)
assert_type(i16 % f16, np.float32)
assert_type(i16 % f32, np.float32)
assert_type(i16 % f64, np.float64)
assert_type(i16 % f64l, np.longdouble)
i16 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 % f, np.floating)
i16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 % b_py, np.int32)
assert_type(i32 % i_py, np.int32)
assert_type(i32 % f_py, np.float64)
i32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 % b1, np.int32)
assert_type(i32 % u8, np.int32)
assert_type(i32 % u16, np.int32)
assert_type(i32 % u32, np.int64)
assert_type(i32 % u64, np.float64)
assert_type(i32 % i8, np.int32)
assert_type(i32 % i16, np.int32)
assert_type(i32 % i32, np.int32)
assert_type(i32 % i64, np.int64)
assert_type(i32 % f16, np.float64)
assert_type(i32 % f32, np.float64)
assert_type(i32 % f64, np.float64)
assert_type(i32 % f64l, np.longdouble)
i32 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 % f, np.floating)
i32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 % b_py, np.int64)
assert_type(i64 % i_py, np.int64)
assert_type(i64 % f_py, np.float64)
i64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 % b1, np.int64)
assert_type(i64 % u8, np.int64)
assert_type(i64 % u16, np.int64)
assert_type(i64 % u32, np.int64)
assert_type(i64 % u64, np.float64)
assert_type(i64 % i8, np.int64)
assert_type(i64 % i16, np.int64)
assert_type(i64 % i32, np.int64)
assert_type(i64 % i64, np.int64)
assert_type(i64 % f16, np.float64)
assert_type(i64 % f32, np.float64)
assert_type(i64 % f64, np.float64)
assert_type(i64 % f64l, np.longdouble)
i64 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 % f, np.floating)
i64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f16 % b_py, np.float16)
assert_type(f16 % i_py, np.float16)
assert_type(f16 % f_py, np.float16)
f16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 % b1, np.float16)
assert_type(f16 % u8, np.float16)
assert_type(f16 % u16, np.float32)
assert_type(f16 % u32, np.float64)
assert_type(f16 % u64, np.float64)
assert_type(f16 % i8, np.float16)
assert_type(f16 % i16, np.float32)
assert_type(f16 % i32, np.float64)
assert_type(f16 % i64, np.float64)
assert_type(f16 % f16, np.float16)
assert_type(f16 % f32, np.float32)
assert_type(f16 % f64, np.float64)
assert_type(f16 % f64l, np.longdouble)
f16 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 % f, np.floating)
f16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f32 % b_py, np.float32)
assert_type(f32 % i_py, np.float32)
assert_type(f32 % f_py, np.float32)
f32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 % b1, np.float32)
assert_type(f32 % u8, np.float32)
assert_type(f32 % u16, np.float32)
assert_type(f32 % u32, np.float64)
assert_type(f32 % u64, np.float64)
assert_type(f32 % i8, np.float32)
assert_type(f32 % i16, np.float32)
assert_type(f32 % i32, np.float64)
assert_type(f32 % i64, np.float64)
assert_type(f32 % f16, np.float32)
assert_type(f32 % f32, np.float32)
assert_type(f32 % f64, np.float64)
assert_type(f32 % f64l, np.longdouble)
f32 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 % f, np.floating)
f32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64 % b_py, np.float64)
assert_type(f64 % i_py, np.float64)
assert_type(f64 % f_py, np.float64)
f64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 % b1, np.float64)
assert_type(f64 % u8, np.float64)
assert_type(f64 % u16, np.float64)
assert_type(f64 % u32, np.float64)
assert_type(f64 % u64, np.float64)
assert_type(f64 % i8, np.float64)
assert_type(f64 % i16, np.float64)
assert_type(f64 % i32, np.float64)
assert_type(f64 % i64, np.float64)
assert_type(f64 % f16, np.float64)
assert_type(f64 % f32, np.float64)
assert_type(f64 % f64, np.float64)
assert_type(f64 % f64l, np.longdouble)
f64 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 % f, np.floating)
f64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64l % b_py, np.longdouble)
assert_type(f64l % i_py, np.longdouble)
assert_type(f64l % f_py, np.longdouble)
f64l % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l % b1, np.longdouble)
assert_type(f64l % u8, np.longdouble)
assert_type(f64l % u16, np.longdouble)
assert_type(f64l % u32, np.longdouble)
assert_type(f64l % u64, np.longdouble)
assert_type(f64l % i8, np.longdouble)
assert_type(f64l % i16, np.longdouble)
assert_type(f64l % i32, np.longdouble)
assert_type(f64l % i64, np.longdouble)
assert_type(f64l % f16, np.longdouble)
assert_type(f64l % f32, np.longdouble)
assert_type(f64l % f64, np.longdouble)
assert_type(f64l % f64l, np.longdouble)
f64l % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l % f, np.longdouble)
f64l % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c32 % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64 % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c64l % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m64 % m64, np.timedelta64)

assert_type(f % b_py, np.floating)
assert_type(f % i_py, np.floating)
assert_type(f % f_py, np.floating)
f % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f % b1, np.floating)
assert_type(f % u8, np.floating)
assert_type(f % u16, np.floating)
assert_type(f % u32, np.floating)
assert_type(f % u64, np.floating)
assert_type(f % i8, np.floating)
assert_type(f % i16, np.floating)
assert_type(f % i32, np.floating)
assert_type(f % i64, np.floating)
assert_type(f % f16, np.floating)
assert_type(f % f32, np.floating)
assert_type(f % f64, np.floating)
assert_type(f % f64l, np.longdouble)
f % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f % f, np.floating)
f % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
