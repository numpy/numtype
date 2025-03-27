# @generated 2025-03-27T04:33:16Z with tool/testgen.py
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
assert_type(b1 // u, np.unsignedinteger)
assert_type(b1 // i, np.signedinteger)
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
assert_type(u8 // u, np.unsignedinteger)
assert_type(u8 // i, np.signedinteger)
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
assert_type(u16 // u, np.unsignedinteger)
assert_type(u16 // i, np.signedinteger)
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
assert_type(u32 // u, np.unsignedinteger)
assert_type(u32 // i, np.int64)
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
assert_type(u64 // u, np.uint64)
assert_type(u64 // i, np.float64)
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
assert_type(i8 // u, np.number)
assert_type(i8 // i, np.signedinteger)
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
assert_type(i16 // u, np.number)
assert_type(i16 // i, np.signedinteger)
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
assert_type(i32 // u, np.number)
assert_type(i32 // i, np.signedinteger)
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
assert_type(i64 // u, np.number)
assert_type(i64 // i, np.int64)
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
assert_type(f16 // u, np.floating)
assert_type(f16 // i, np.floating)
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
assert_type(f32 // u, np.floating)
assert_type(f32 // i, np.floating)
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
assert_type(f64 // u, np.float64)
assert_type(f64 // i, np.float64)
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
assert_type(f64l // u, np.longdouble)
assert_type(f64l // i, np.longdouble)
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
c32 // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
c64 // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
c64l // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
assert_type(m64 // u, np.timedelta64)
assert_type(m64 // i, np.timedelta64)
assert_type(m64 // f, np.timedelta64)

assert_type(u // b_py, np.unsignedinteger)
assert_type(u // i_py, np.unsignedinteger)
assert_type(u // f_py, np.float64)
u // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u // b1, np.unsignedinteger)
assert_type(u // u8, np.unsignedinteger)
assert_type(u // u16, np.unsignedinteger)
assert_type(u // u32, np.unsignedinteger)
assert_type(u // u64, np.uint64)
assert_type(u // i8, np.number)
assert_type(u // i16, np.number)
assert_type(u // i32, np.number)
assert_type(u // i64, np.number)
assert_type(u // f16, np.floating)
assert_type(u // f32, np.floating)
assert_type(u // f64, np.float64)
assert_type(u // f64l, np.longdouble)
u // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u // u, np.unsignedinteger)
assert_type(u // i, np.number)
assert_type(u // f, np.floating)
u // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i // b_py, np.signedinteger)
assert_type(i // i_py, np.signedinteger)
assert_type(i // f_py, np.float64)
i // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i // b1, np.signedinteger)
assert_type(i // u8, np.signedinteger)
assert_type(i // u16, np.signedinteger)
assert_type(i // u32, np.int64)
assert_type(i // u64, np.float64)
assert_type(i // i8, np.signedinteger)
assert_type(i // i16, np.signedinteger)
assert_type(i // i32, np.signedinteger)
assert_type(i // i64, np.int64)
assert_type(i // f16, np.floating)
assert_type(i // f32, np.floating)
assert_type(i // f64, np.float64)
assert_type(i // f64l, np.longdouble)
i // c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i // c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i // c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i // u, np.number)
assert_type(i // i, np.signedinteger)
assert_type(i // f, np.floating)
i // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

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
assert_type(f // u, np.floating)
assert_type(f // i, np.floating)
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
c // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
assert_type(b1 % u, np.unsignedinteger)
assert_type(b1 % i, np.signedinteger)
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
assert_type(u8 % u, np.unsignedinteger)
assert_type(u8 % i, np.signedinteger)
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
assert_type(u16 % u, np.unsignedinteger)
assert_type(u16 % i, np.signedinteger)
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
assert_type(u32 % u, np.unsignedinteger)
assert_type(u32 % i, np.int64)
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
assert_type(u64 % u, np.uint64)
assert_type(u64 % i, np.float64)
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
assert_type(i8 % u, np.number)
assert_type(i8 % i, np.signedinteger)
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
assert_type(i16 % u, np.number)
assert_type(i16 % i, np.signedinteger)
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
assert_type(i32 % u, np.number)
assert_type(i32 % i, np.signedinteger)
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
assert_type(i64 % u, np.number)
assert_type(i64 % i, np.int64)
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
assert_type(f16 % u, np.floating)
assert_type(f16 % i, np.floating)
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
assert_type(f32 % u, np.floating)
assert_type(f32 % i, np.floating)
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
assert_type(f64 % u, np.float64)
assert_type(f64 % i, np.float64)
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
assert_type(f64l % u, np.longdouble)
assert_type(f64l % i, np.longdouble)
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
c32 % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c32 % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
c64 % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64 % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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
c64l % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c64l % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m64 % m64, np.timedelta64)

assert_type(u % b_py, np.unsignedinteger)
assert_type(u % i_py, np.unsignedinteger)
assert_type(u % f_py, np.float64)
u % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u % b1, np.unsignedinteger)
assert_type(u % u8, np.unsignedinteger)
assert_type(u % u16, np.unsignedinteger)
assert_type(u % u32, np.unsignedinteger)
assert_type(u % u64, np.uint64)
assert_type(u % i8, np.number)
assert_type(u % i16, np.number)
assert_type(u % i32, np.number)
assert_type(u % i64, np.number)
assert_type(u % f16, np.floating)
assert_type(u % f32, np.floating)
assert_type(u % f64, np.float64)
assert_type(u % f64l, np.longdouble)
u % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u % u, np.unsignedinteger)
assert_type(u % i, np.number)
assert_type(u % f, np.floating)
u % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i % b_py, np.signedinteger)
assert_type(i % i_py, np.signedinteger)
assert_type(i % f_py, np.float64)
i % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i % b1, np.signedinteger)
assert_type(i % u8, np.signedinteger)
assert_type(i % u16, np.signedinteger)
assert_type(i % u32, np.int64)
assert_type(i % u64, np.float64)
assert_type(i % i8, np.signedinteger)
assert_type(i % i16, np.signedinteger)
assert_type(i % i32, np.signedinteger)
assert_type(i % i64, np.int64)
assert_type(i % f16, np.floating)
assert_type(i % f32, np.floating)
assert_type(i % f64, np.float64)
assert_type(i % f64l, np.longdouble)
i % c32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i % c64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i % c64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i % u, np.number)
assert_type(i % i, np.signedinteger)
assert_type(i % f, np.floating)
i % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

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
assert_type(f % u, np.floating)
assert_type(f % i, np.floating)
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
c % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]divmod__

assert_type(divmod(b1, b_py), tuple[np.int8, np.int8])
assert_type(divmod(b1, i_py), tuple[np.int64, np.int64])
assert_type(divmod(b1, f_py), tuple[np.float64, np.float64])
divmod(b1, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1, b1), tuple[np.int8, np.int8])
assert_type(divmod(b1, u8), tuple[np.uint8, np.uint8])
assert_type(divmod(b1, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(b1, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(b1, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(b1, i8), tuple[np.int8, np.int8])
assert_type(divmod(b1, i16), tuple[np.int16, np.int16])
assert_type(divmod(b1, i32), tuple[np.int32, np.int32])
assert_type(divmod(b1, i64), tuple[np.int64, np.int64])
assert_type(divmod(b1, f16), tuple[np.float16, np.float16])
assert_type(divmod(b1, f32), tuple[np.float32, np.float32])
assert_type(divmod(b1, f64), tuple[np.float64, np.float64])
assert_type(divmod(b1, f64l), tuple[np.longdouble, np.longdouble])
divmod(b1, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(b1, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(b1, f), tuple[np.floating, np.floating])
divmod(b1, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u8, b_py), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, i_py), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, f_py), tuple[np.float64, np.float64])
divmod(u8, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8, b1), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, u8), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(u8, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u8, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u8, i8), tuple[np.int16, np.int16])
assert_type(divmod(u8, i16), tuple[np.int16, np.int16])
assert_type(divmod(u8, i32), tuple[np.int32, np.int32])
assert_type(divmod(u8, i64), tuple[np.int64, np.int64])
assert_type(divmod(u8, f16), tuple[np.float16, np.float16])
assert_type(divmod(u8, f32), tuple[np.float32, np.float32])
assert_type(divmod(u8, f64), tuple[np.float64, np.float64])
assert_type(divmod(u8, f64l), tuple[np.longdouble, np.longdouble])
divmod(u8, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u8, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(u8, f), tuple[np.floating, np.floating])
divmod(u8, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u16, b_py), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, i_py), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, f_py), tuple[np.float64, np.float64])
divmod(u16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u16, b1), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, u8), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u16, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u16, i8), tuple[np.int32, np.int32])
assert_type(divmod(u16, i16), tuple[np.int32, np.int32])
assert_type(divmod(u16, i32), tuple[np.int32, np.int32])
assert_type(divmod(u16, i64), tuple[np.int64, np.int64])
assert_type(divmod(u16, f16), tuple[np.float32, np.float32])
assert_type(divmod(u16, f32), tuple[np.float32, np.float32])
assert_type(divmod(u16, f64), tuple[np.float64, np.float64])
assert_type(divmod(u16, f64l), tuple[np.longdouble, np.longdouble])
divmod(u16, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u16, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u16, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u16, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u16, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(u16, f), tuple[np.floating, np.floating])
divmod(u16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u32, b_py), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, i_py), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, f_py), tuple[np.float64, np.float64])
divmod(u32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u32, b1), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u8), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u16), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u32, i8), tuple[np.int64, np.int64])
assert_type(divmod(u32, i16), tuple[np.int64, np.int64])
assert_type(divmod(u32, i32), tuple[np.int64, np.int64])
assert_type(divmod(u32, i64), tuple[np.int64, np.int64])
assert_type(divmod(u32, f16), tuple[np.float64, np.float64])
assert_type(divmod(u32, f32), tuple[np.float64, np.float64])
assert_type(divmod(u32, f64), tuple[np.float64, np.float64])
assert_type(divmod(u32, f64l), tuple[np.longdouble, np.longdouble])
divmod(u32, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u32, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u32, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u32, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u32, i), tuple[np.int64, np.int64])
assert_type(divmod(u32, f), tuple[np.floating, np.floating])
divmod(u32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u64, b_py), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, i_py), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, f_py), tuple[np.float64, np.float64])
divmod(u64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u64, b1), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u8), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u16), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u32), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, i8), tuple[np.float64, np.float64])
assert_type(divmod(u64, i16), tuple[np.float64, np.float64])
assert_type(divmod(u64, i32), tuple[np.float64, np.float64])
assert_type(divmod(u64, i64), tuple[np.float64, np.float64])
assert_type(divmod(u64, f16), tuple[np.float64, np.float64])
assert_type(divmod(u64, f32), tuple[np.float64, np.float64])
assert_type(divmod(u64, f64), tuple[np.float64, np.float64])
assert_type(divmod(u64, f64l), tuple[np.longdouble, np.longdouble])
divmod(u64, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u64, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u64, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u64, u), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, i), tuple[np.float64, np.float64])
assert_type(divmod(u64, f), tuple[np.floating, np.floating])
divmod(u64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i8, b_py), tuple[np.int8, np.int8])
assert_type(divmod(i8, i_py), tuple[np.int8, np.int8])
assert_type(divmod(i8, f_py), tuple[np.float64, np.float64])
divmod(i8, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8, b1), tuple[np.int8, np.int8])
assert_type(divmod(i8, u8), tuple[np.int16, np.int16])
assert_type(divmod(i8, u16), tuple[np.int32, np.int32])
assert_type(divmod(i8, u32), tuple[np.int64, np.int64])
assert_type(divmod(i8, u64), tuple[np.float64, np.float64])
assert_type(divmod(i8, i8), tuple[np.int8, np.int8])
assert_type(divmod(i8, i16), tuple[np.int16, np.int16])
assert_type(divmod(i8, i32), tuple[np.int32, np.int32])
assert_type(divmod(i8, i64), tuple[np.int64, np.int64])
assert_type(divmod(i8, f16), tuple[np.float16, np.float16])
assert_type(divmod(i8, f32), tuple[np.float32, np.float32])
assert_type(divmod(i8, f64), tuple[np.float64, np.float64])
assert_type(divmod(i8, f64l), tuple[np.longdouble, np.longdouble])
divmod(i8, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8, u), tuple[np.number, np.number])
assert_type(divmod(i8, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i8, f), tuple[np.floating, np.floating])
divmod(i8, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i16, b_py), tuple[np.int16, np.int16])
assert_type(divmod(i16, i_py), tuple[np.int16, np.int16])
assert_type(divmod(i16, f_py), tuple[np.float64, np.float64])
divmod(i16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i16, b1), tuple[np.int16, np.int16])
assert_type(divmod(i16, u8), tuple[np.int16, np.int16])
assert_type(divmod(i16, u16), tuple[np.int32, np.int32])
assert_type(divmod(i16, u32), tuple[np.int64, np.int64])
assert_type(divmod(i16, u64), tuple[np.float64, np.float64])
assert_type(divmod(i16, i8), tuple[np.int16, np.int16])
assert_type(divmod(i16, i16), tuple[np.int16, np.int16])
assert_type(divmod(i16, i32), tuple[np.int32, np.int32])
assert_type(divmod(i16, i64), tuple[np.int64, np.int64])
assert_type(divmod(i16, f16), tuple[np.float32, np.float32])
assert_type(divmod(i16, f32), tuple[np.float32, np.float32])
assert_type(divmod(i16, f64), tuple[np.float64, np.float64])
assert_type(divmod(i16, f64l), tuple[np.longdouble, np.longdouble])
divmod(i16, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i16, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i16, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i16, u), tuple[np.number, np.number])
assert_type(divmod(i16, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i16, f), tuple[np.floating, np.floating])
divmod(i16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i32, b_py), tuple[np.int32, np.int32])
assert_type(divmod(i32, i_py), tuple[np.int32, np.int32])
assert_type(divmod(i32, f_py), tuple[np.float64, np.float64])
divmod(i32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i32, b1), tuple[np.int32, np.int32])
assert_type(divmod(i32, u8), tuple[np.int32, np.int32])
assert_type(divmod(i32, u16), tuple[np.int32, np.int32])
assert_type(divmod(i32, u32), tuple[np.int64, np.int64])
assert_type(divmod(i32, u64), tuple[np.float64, np.float64])
assert_type(divmod(i32, i8), tuple[np.int32, np.int32])
assert_type(divmod(i32, i16), tuple[np.int32, np.int32])
assert_type(divmod(i32, i32), tuple[np.int32, np.int32])
assert_type(divmod(i32, i64), tuple[np.int64, np.int64])
assert_type(divmod(i32, f16), tuple[np.float64, np.float64])
assert_type(divmod(i32, f32), tuple[np.float64, np.float64])
assert_type(divmod(i32, f64), tuple[np.float64, np.float64])
assert_type(divmod(i32, f64l), tuple[np.longdouble, np.longdouble])
divmod(i32, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i32, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i32, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i32, u), tuple[np.number, np.number])
assert_type(divmod(i32, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i32, f), tuple[np.floating, np.floating])
divmod(i32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i64, b_py), tuple[np.int64, np.int64])
assert_type(divmod(i64, i_py), tuple[np.int64, np.int64])
assert_type(divmod(i64, f_py), tuple[np.float64, np.float64])
divmod(i64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i64, b1), tuple[np.int64, np.int64])
assert_type(divmod(i64, u8), tuple[np.int64, np.int64])
assert_type(divmod(i64, u16), tuple[np.int64, np.int64])
assert_type(divmod(i64, u32), tuple[np.int64, np.int64])
assert_type(divmod(i64, u64), tuple[np.float64, np.float64])
assert_type(divmod(i64, i8), tuple[np.int64, np.int64])
assert_type(divmod(i64, i16), tuple[np.int64, np.int64])
assert_type(divmod(i64, i32), tuple[np.int64, np.int64])
assert_type(divmod(i64, i64), tuple[np.int64, np.int64])
assert_type(divmod(i64, f16), tuple[np.float64, np.float64])
assert_type(divmod(i64, f32), tuple[np.float64, np.float64])
assert_type(divmod(i64, f64), tuple[np.float64, np.float64])
assert_type(divmod(i64, f64l), tuple[np.longdouble, np.longdouble])
divmod(i64, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i64, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i64, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i64, u), tuple[np.number, np.number])
assert_type(divmod(i64, i), tuple[np.int64, np.int64])
assert_type(divmod(i64, f), tuple[np.floating, np.floating])
divmod(i64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f16, b_py), tuple[np.float16, np.float16])
assert_type(divmod(f16, i_py), tuple[np.float16, np.float16])
assert_type(divmod(f16, f_py), tuple[np.float16, np.float16])
divmod(f16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f16, b1), tuple[np.float16, np.float16])
assert_type(divmod(f16, u8), tuple[np.float16, np.float16])
assert_type(divmod(f16, u16), tuple[np.float32, np.float32])
assert_type(divmod(f16, u32), tuple[np.float64, np.float64])
assert_type(divmod(f16, u64), tuple[np.float64, np.float64])
assert_type(divmod(f16, i8), tuple[np.float16, np.float16])
assert_type(divmod(f16, i16), tuple[np.float32, np.float32])
assert_type(divmod(f16, i32), tuple[np.float64, np.float64])
assert_type(divmod(f16, i64), tuple[np.float64, np.float64])
assert_type(divmod(f16, f16), tuple[np.float16, np.float16])
assert_type(divmod(f16, f32), tuple[np.float32, np.float32])
assert_type(divmod(f16, f64), tuple[np.float64, np.float64])
assert_type(divmod(f16, f64l), tuple[np.longdouble, np.longdouble])
divmod(f16, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f16, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f16, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f16, u), tuple[np.floating, np.floating])
assert_type(divmod(f16, i), tuple[np.floating, np.floating])
assert_type(divmod(f16, f), tuple[np.floating, np.floating])
divmod(f16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f32, b_py), tuple[np.float32, np.float32])
assert_type(divmod(f32, i_py), tuple[np.float32, np.float32])
assert_type(divmod(f32, f_py), tuple[np.float32, np.float32])
divmod(f32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f32, b1), tuple[np.float32, np.float32])
assert_type(divmod(f32, u8), tuple[np.float32, np.float32])
assert_type(divmod(f32, u16), tuple[np.float32, np.float32])
assert_type(divmod(f32, u32), tuple[np.float64, np.float64])
assert_type(divmod(f32, u64), tuple[np.float64, np.float64])
assert_type(divmod(f32, i8), tuple[np.float32, np.float32])
assert_type(divmod(f32, i16), tuple[np.float32, np.float32])
assert_type(divmod(f32, i32), tuple[np.float64, np.float64])
assert_type(divmod(f32, i64), tuple[np.float64, np.float64])
assert_type(divmod(f32, f16), tuple[np.float32, np.float32])
assert_type(divmod(f32, f32), tuple[np.float32, np.float32])
assert_type(divmod(f32, f64), tuple[np.float64, np.float64])
assert_type(divmod(f32, f64l), tuple[np.longdouble, np.longdouble])
divmod(f32, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f32, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f32, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f32, u), tuple[np.floating, np.floating])
assert_type(divmod(f32, i), tuple[np.floating, np.floating])
assert_type(divmod(f32, f), tuple[np.floating, np.floating])
divmod(f32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f64, b_py), tuple[np.float64, np.float64])
assert_type(divmod(f64, i_py), tuple[np.float64, np.float64])
assert_type(divmod(f64, f_py), tuple[np.float64, np.float64])
divmod(f64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64, b1), tuple[np.float64, np.float64])
assert_type(divmod(f64, u8), tuple[np.float64, np.float64])
assert_type(divmod(f64, u16), tuple[np.float64, np.float64])
assert_type(divmod(f64, u32), tuple[np.float64, np.float64])
assert_type(divmod(f64, u64), tuple[np.float64, np.float64])
assert_type(divmod(f64, i8), tuple[np.float64, np.float64])
assert_type(divmod(f64, i16), tuple[np.float64, np.float64])
assert_type(divmod(f64, i32), tuple[np.float64, np.float64])
assert_type(divmod(f64, i64), tuple[np.float64, np.float64])
assert_type(divmod(f64, f16), tuple[np.float64, np.float64])
assert_type(divmod(f64, f32), tuple[np.float64, np.float64])
assert_type(divmod(f64, f64), tuple[np.float64, np.float64])
assert_type(divmod(f64, f64l), tuple[np.longdouble, np.longdouble])
divmod(f64, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64, u), tuple[np.float64, np.float64])
assert_type(divmod(f64, i), tuple[np.float64, np.float64])
assert_type(divmod(f64, f), tuple[np.floating, np.floating])
divmod(f64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f64l, b_py), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i_py), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f_py), tuple[np.longdouble, np.longdouble])
divmod(f64l, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64l, b1), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u8), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i8), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f64l), tuple[np.longdouble, np.longdouble])
divmod(f64l, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64l, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64l, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64l, u), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f), tuple[np.longdouble, np.longdouble])
divmod(f64l, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c32, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c64, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c64l, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c64l, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(m64, m64), tuple[np.int64, np.timedelta64])

assert_type(divmod(u, b_py), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, i_py), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, f_py), tuple[np.float64, np.float64])
divmod(u, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u, b1), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u8), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u16), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u32), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u, i8), tuple[np.number, np.number])
assert_type(divmod(u, i16), tuple[np.number, np.number])
assert_type(divmod(u, i32), tuple[np.number, np.number])
assert_type(divmod(u, i64), tuple[np.number, np.number])
assert_type(divmod(u, f16), tuple[np.floating, np.floating])
assert_type(divmod(u, f32), tuple[np.floating, np.floating])
assert_type(divmod(u, f64), tuple[np.float64, np.float64])
assert_type(divmod(u, f64l), tuple[np.longdouble, np.longdouble])
divmod(u, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, i), tuple[np.number, np.number])
assert_type(divmod(u, f), tuple[np.floating, np.floating])
divmod(u, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i, b_py), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i_py), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, f_py), tuple[np.float64, np.float64])
divmod(i, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i, b1), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u8), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u16), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u32), tuple[np.int64, np.int64])
assert_type(divmod(i, u64), tuple[np.float64, np.float64])
assert_type(divmod(i, i8), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i16), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i32), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i64), tuple[np.int64, np.int64])
assert_type(divmod(i, f16), tuple[np.floating, np.floating])
assert_type(divmod(i, f32), tuple[np.floating, np.floating])
assert_type(divmod(i, f64), tuple[np.float64, np.float64])
assert_type(divmod(i, f64l), tuple[np.longdouble, np.longdouble])
divmod(i, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i, u), tuple[np.number, np.number])
assert_type(divmod(i, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, f), tuple[np.floating, np.floating])
divmod(i, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f, b_py), tuple[np.floating, np.floating])
assert_type(divmod(f, i_py), tuple[np.floating, np.floating])
assert_type(divmod(f, f_py), tuple[np.floating, np.floating])
divmod(f, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f, b1), tuple[np.floating, np.floating])
assert_type(divmod(f, u8), tuple[np.floating, np.floating])
assert_type(divmod(f, u16), tuple[np.floating, np.floating])
assert_type(divmod(f, u32), tuple[np.floating, np.floating])
assert_type(divmod(f, u64), tuple[np.floating, np.floating])
assert_type(divmod(f, i8), tuple[np.floating, np.floating])
assert_type(divmod(f, i16), tuple[np.floating, np.floating])
assert_type(divmod(f, i32), tuple[np.floating, np.floating])
assert_type(divmod(f, i64), tuple[np.floating, np.floating])
assert_type(divmod(f, f16), tuple[np.floating, np.floating])
assert_type(divmod(f, f32), tuple[np.floating, np.floating])
assert_type(divmod(f, f64), tuple[np.floating, np.floating])
assert_type(divmod(f, f64l), tuple[np.longdouble, np.longdouble])
divmod(f, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f, u), tuple[np.floating, np.floating])
assert_type(divmod(f, i), tuple[np.floating, np.floating])
assert_type(divmod(f, f), tuple[np.floating, np.floating])
divmod(f, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
