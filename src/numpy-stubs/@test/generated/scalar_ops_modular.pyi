# @generated 2025-05-03T21:24:40Z with tool/testgen.py
from typing import assert_type

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
f16: np.float16
f32: np.float32
f64: np.float64
f64l: np.longdouble
c128: np.complex128
m64: np.timedelta64

i: np.signedinteger
u: np.unsignedinteger
f: np.floating
c: np.complexfloating
iu: np.integer
fc: np.inexact
iufc: np.number

###
# __[r]floordiv__

assert_type(b1 // b_py, np.int8)
assert_type(b1 // i_py, np.int_)
assert_type(b1 // f_py, np.float64)
b1 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 // b1, np.int8)
assert_type(b1 // i8, np.int8)
assert_type(b1 // i16, np.int16)
assert_type(b1 // i32, np.int32)
assert_type(b1 // i64, np.int64)
assert_type(b1 // u8, np.uint8)
assert_type(b1 // u16, np.uint16)
assert_type(b1 // u32, np.uint32)
assert_type(b1 // u64, np.uint64)
assert_type(b1 // f16, np.float16)
assert_type(b1 // f32, np.float32)
assert_type(b1 // f64, np.float64)
assert_type(b1 // f64l, np.longdouble)
b1 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 // i, np.signedinteger)
assert_type(b1 // u, np.unsignedinteger)
assert_type(b1 // f, np.floating)
b1 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 // iu, np.integer)
b1 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 // b_py, np.int8)
assert_type(i8 // i_py, np.int8)
assert_type(i8 // f_py, np.float64)
i8 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 // b1, np.int8)
assert_type(i8 // i8, np.int8)
assert_type(i8 // i16, np.int16)
assert_type(i8 // i32, np.int32)
assert_type(i8 // i64, np.int64)
assert_type(i8 // u8, np.int16)
assert_type(i8 // u16, np.int32)
assert_type(i8 // u32, np.int64)
assert_type(i8 // u64, np.float64)
assert_type(i8 // f16, np.float16)
assert_type(i8 // f32, np.float32)
assert_type(i8 // f64, np.float64)
assert_type(i8 // f64l, np.longdouble)
i8 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 // i, np.signedinteger)
assert_type(i8 // u, np.signedinteger | np.float64)
assert_type(i8 // f, np.floating)
i8 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 // iu, np.signedinteger | np.float64)
i8 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 // b_py, np.int16)
assert_type(i16 // i_py, np.int16)
assert_type(i16 // f_py, np.float64)
i16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 // b1, np.int16)
assert_type(i16 // i8, np.int16)
assert_type(i16 // i16, np.int16)
assert_type(i16 // i32, np.int32)
assert_type(i16 // i64, np.int64)
assert_type(i16 // u8, np.int16)
assert_type(i16 // u16, np.int32)
assert_type(i16 // u32, np.int64)
assert_type(i16 // u64, np.float64)
assert_type(i16 // f16, np.float32)
assert_type(i16 // f32, np.float32)
assert_type(i16 // f64, np.float64)
assert_type(i16 // f64l, np.longdouble)
i16 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 // i, np.signedinteger)
assert_type(i16 // u, np.signedinteger | np.float64)
assert_type(i16 // f, np.floating)
i16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 // iu, np.signedinteger | np.float64)
i16 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 // b_py, np.int32)
assert_type(i32 // i_py, np.int32)
assert_type(i32 // f_py, np.float64)
i32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 // b1, np.int32)
assert_type(i32 // i8, np.int32)
assert_type(i32 // i16, np.int32)
assert_type(i32 // i32, np.int32)
assert_type(i32 // i64, np.int64)
assert_type(i32 // u8, np.int32)
assert_type(i32 // u16, np.int32)
assert_type(i32 // u32, np.int64)
assert_type(i32 // u64, np.float64)
assert_type(i32 // f16, np.float64)
assert_type(i32 // f32, np.float64)
assert_type(i32 // f64, np.float64)
assert_type(i32 // f64l, np.longdouble)
i32 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 // i, np.signedinteger)
assert_type(i32 // u, np.signedinteger | np.float64)
assert_type(i32 // f, np.floating)
i32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 // iu, np.signedinteger | np.float64)
i32 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 // b_py, np.int64)
assert_type(i64 // i_py, np.int64)
assert_type(i64 // f_py, np.float64)
i64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 // b1, np.int64)
assert_type(i64 // i8, np.int64)
assert_type(i64 // i16, np.int64)
assert_type(i64 // i32, np.int64)
assert_type(i64 // i64, np.int64)
assert_type(i64 // u8, np.int64)
assert_type(i64 // u16, np.int64)
assert_type(i64 // u32, np.int64)
assert_type(i64 // u64, np.float64)
assert_type(i64 // f16, np.float64)
assert_type(i64 // f32, np.float64)
assert_type(i64 // f64, np.float64)
assert_type(i64 // f64l, np.longdouble)
i64 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 // i, np.int64)
assert_type(i64 // u, np.int64 | np.float64)
assert_type(i64 // f, np.floating)
i64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 // iu, np.int64 | np.float64)
i64 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 // b_py, np.uint8)
assert_type(u8 // i_py, np.uint8)
assert_type(u8 // f_py, np.float64)
u8 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 // b1, np.uint8)
assert_type(u8 // i8, np.int16)
assert_type(u8 // i16, np.int16)
assert_type(u8 // i32, np.int32)
assert_type(u8 // i64, np.int64)
assert_type(u8 // u8, np.uint8)
assert_type(u8 // u16, np.uint16)
assert_type(u8 // u32, np.uint32)
assert_type(u8 // u64, np.uint64)
assert_type(u8 // f16, np.float16)
assert_type(u8 // f32, np.float32)
assert_type(u8 // f64, np.float64)
assert_type(u8 // f64l, np.longdouble)
u8 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 // i, np.signedinteger)
assert_type(u8 // u, np.unsignedinteger)
assert_type(u8 // f, np.floating)
u8 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 // iu, np.integer)
u8 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 // b_py, np.uint16)
assert_type(u16 // i_py, np.uint16)
assert_type(u16 // f_py, np.float64)
u16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 // b1, np.uint16)
assert_type(u16 // i8, np.int32)
assert_type(u16 // i16, np.int32)
assert_type(u16 // i32, np.int32)
assert_type(u16 // i64, np.int64)
assert_type(u16 // u8, np.uint16)
assert_type(u16 // u16, np.uint16)
assert_type(u16 // u32, np.uint32)
assert_type(u16 // u64, np.uint64)
assert_type(u16 // f16, np.float32)
assert_type(u16 // f32, np.float32)
assert_type(u16 // f64, np.float64)
assert_type(u16 // f64l, np.longdouble)
u16 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 // i, np.signedinteger)
assert_type(u16 // u, np.unsignedinteger)
assert_type(u16 // f, np.floating)
u16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 // iu, np.integer)
u16 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 // b_py, np.uint32)
assert_type(u32 // i_py, np.uint32)
assert_type(u32 // f_py, np.float64)
u32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 // b1, np.uint32)
assert_type(u32 // i8, np.int64)
assert_type(u32 // i16, np.int64)
assert_type(u32 // i32, np.int64)
assert_type(u32 // i64, np.int64)
assert_type(u32 // u8, np.uint32)
assert_type(u32 // u16, np.uint32)
assert_type(u32 // u32, np.uint32)
assert_type(u32 // u64, np.uint64)
assert_type(u32 // f16, np.float64)
assert_type(u32 // f32, np.float64)
assert_type(u32 // f64, np.float64)
assert_type(u32 // f64l, np.longdouble)
u32 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 // i, np.int64)
assert_type(u32 // u, np.unsignedinteger)
assert_type(u32 // f, np.floating)
u32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 // iu, np.integer)
u32 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 // b_py, np.uint64)
assert_type(u64 // i_py, np.uint64)
assert_type(u64 // f_py, np.float64)
u64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 // b1, np.uint64)
assert_type(u64 // i8, np.float64)
assert_type(u64 // i16, np.float64)
assert_type(u64 // i32, np.float64)
assert_type(u64 // i64, np.float64)
assert_type(u64 // u8, np.uint64)
assert_type(u64 // u16, np.uint64)
assert_type(u64 // u32, np.uint64)
assert_type(u64 // u64, np.uint64)
assert_type(u64 // f16, np.float64)
assert_type(u64 // f32, np.float64)
assert_type(u64 // f64, np.float64)
assert_type(u64 // f64l, np.longdouble)
u64 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 // i, np.float64)
assert_type(u64 // u, np.uint64)
assert_type(u64 // f, np.floating)
u64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 // iu, np.uint64 | np.float64)
u64 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f16 // b_py, np.float16)
assert_type(f16 // i_py, np.float16)
assert_type(f16 // f_py, np.float16)
f16 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 // b1, np.float16)
assert_type(f16 // i8, np.float16)
assert_type(f16 // i16, np.float32)
assert_type(f16 // i32, np.float64)
assert_type(f16 // i64, np.float64)
assert_type(f16 // u8, np.float16)
assert_type(f16 // u16, np.float32)
assert_type(f16 // u32, np.float64)
assert_type(f16 // u64, np.float64)
assert_type(f16 // f16, np.float16)
assert_type(f16 // f32, np.float32)
assert_type(f16 // f64, np.float64)
assert_type(f16 // f64l, np.longdouble)
f16 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 // i, np.floating)
assert_type(f16 // u, np.floating)
assert_type(f16 // f, np.floating)
f16 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 // iu, np.floating)
f16 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f32 // b_py, np.float32)
assert_type(f32 // i_py, np.float32)
assert_type(f32 // f_py, np.float32)
f32 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 // b1, np.float32)
assert_type(f32 // i8, np.float32)
assert_type(f32 // i16, np.float32)
assert_type(f32 // i32, np.float64)
assert_type(f32 // i64, np.float64)
assert_type(f32 // u8, np.float32)
assert_type(f32 // u16, np.float32)
assert_type(f32 // u32, np.float64)
assert_type(f32 // u64, np.float64)
assert_type(f32 // f16, np.float32)
assert_type(f32 // f32, np.float32)
assert_type(f32 // f64, np.float64)
assert_type(f32 // f64l, np.longdouble)
f32 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 // i, np.floating)
assert_type(f32 // u, np.floating)
assert_type(f32 // f, np.floating)
f32 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 // iu, np.floating)
f32 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64 // b_py, np.float64)
assert_type(f64 // i_py, np.float64)
assert_type(f64 // f_py, np.float64)
f64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 // b1, np.float64)
assert_type(f64 // i8, np.float64)
assert_type(f64 // i16, np.float64)
assert_type(f64 // i32, np.float64)
assert_type(f64 // i64, np.float64)
assert_type(f64 // u8, np.float64)
assert_type(f64 // u16, np.float64)
assert_type(f64 // u32, np.float64)
assert_type(f64 // u64, np.float64)
assert_type(f64 // f16, np.float64)
assert_type(f64 // f32, np.float64)
assert_type(f64 // f64, np.float64)
assert_type(f64 // f64l, np.longdouble)
f64 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 // i, np.float64)
assert_type(f64 // u, np.float64)
assert_type(f64 // f, np.floating)
f64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 // iu, np.float64)
f64 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64l // b_py, np.longdouble)
assert_type(f64l // i_py, np.longdouble)
assert_type(f64l // f_py, np.longdouble)
f64l // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l // b1, np.longdouble)
assert_type(f64l // i8, np.longdouble)
assert_type(f64l // i16, np.longdouble)
assert_type(f64l // i32, np.longdouble)
assert_type(f64l // i64, np.longdouble)
assert_type(f64l // u8, np.longdouble)
assert_type(f64l // u16, np.longdouble)
assert_type(f64l // u32, np.longdouble)
assert_type(f64l // u64, np.longdouble)
assert_type(f64l // f16, np.longdouble)
assert_type(f64l // f32, np.longdouble)
assert_type(f64l // f64, np.longdouble)
assert_type(f64l // f64l, np.longdouble)
f64l // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l // i, np.longdouble)
assert_type(f64l // u, np.longdouble)
assert_type(f64l // f, np.longdouble)
f64l // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l // iu, np.longdouble)
f64l // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m64 // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m64 // i_py, np.timedelta64)
assert_type(m64 // f_py, np.timedelta64)
m64 // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m64 // i8, np.timedelta64)
assert_type(m64 // i16, np.timedelta64)
assert_type(m64 // i32, np.timedelta64)
assert_type(m64 // i64, np.timedelta64)
assert_type(m64 // u8, np.timedelta64)
assert_type(m64 // u16, np.timedelta64)
assert_type(m64 // u32, np.timedelta64)
assert_type(m64 // u64, np.timedelta64)
assert_type(m64 // f16, np.timedelta64)
assert_type(m64 // f32, np.timedelta64)
assert_type(m64 // f64, np.timedelta64)
assert_type(m64 // f64l, np.timedelta64)
m64 // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m64 // m64, np.int64)
assert_type(m64 // i, np.timedelta64)
assert_type(m64 // u, np.timedelta64)
assert_type(m64 // f, np.timedelta64)
m64 // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m64 // iu, np.timedelta64)
m64 // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i // b_py, np.signedinteger)
assert_type(i // i_py, np.signedinteger)
assert_type(i // f_py, np.float64)
i // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i // b1, np.signedinteger)
assert_type(i // i8, np.signedinteger)
assert_type(i // i16, np.signedinteger)
assert_type(i // i32, np.signedinteger)
assert_type(i // i64, np.int64)
assert_type(i // u8, np.signedinteger)
assert_type(i // u16, np.signedinteger)
assert_type(i // u32, np.int64)
assert_type(i // u64, np.float64)
assert_type(i // f16, np.floating)
assert_type(i // f32, np.floating)
assert_type(i // f64, np.float64)
assert_type(i // f64l, np.longdouble)
i // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i // i, np.signedinteger)
assert_type(i // u, np.signedinteger | np.float64)
assert_type(i // f, np.floating)
i // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i // iu, np.signedinteger | np.float64)
i // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u // b_py, np.unsignedinteger)
assert_type(u // i_py, np.unsignedinteger)
assert_type(u // f_py, np.float64)
u // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u // b1, np.unsignedinteger)
assert_type(u // i8, np.signedinteger | np.float64)
assert_type(u // i16, np.signedinteger | np.float64)
assert_type(u // i32, np.signedinteger | np.float64)
assert_type(u // i64, np.int64 | np.float64)
assert_type(u // u8, np.unsignedinteger)
assert_type(u // u16, np.unsignedinteger)
assert_type(u // u32, np.unsignedinteger)
assert_type(u // u64, np.uint64)
assert_type(u // f16, np.floating)
assert_type(u // f32, np.floating)
assert_type(u // f64, np.float64)
assert_type(u // f64l, np.longdouble)
u // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u // i, np.signedinteger | np.float64)
assert_type(u // u, np.unsignedinteger)
assert_type(u // f, np.floating)
u // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u // iu, np.integer | np.float64)
u // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f // b_py, np.floating)
assert_type(f // i_py, np.floating)
assert_type(f // f_py, np.floating)
f // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f // b1, np.floating)
assert_type(f // i8, np.floating)
assert_type(f // i16, np.floating)
assert_type(f // i32, np.floating)
assert_type(f // i64, np.floating)
assert_type(f // u8, np.floating)
assert_type(f // u16, np.floating)
assert_type(f // u32, np.floating)
assert_type(f // u64, np.floating)
assert_type(f // f16, np.floating)
assert_type(f // f32, np.floating)
assert_type(f // f64, np.floating)
assert_type(f // f64l, np.longdouble)
f // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f // i, np.floating)
assert_type(f // u, np.floating)
assert_type(f // f, np.floating)
f // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f // iu, np.floating)
f // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu // b_py, np.integer)
assert_type(iu // i_py, np.integer)
assert_type(iu // f_py, np.float64)
iu // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu // b1, np.integer)
assert_type(iu // i8, np.signedinteger | np.float64)
assert_type(iu // i16, np.signedinteger | np.float64)
assert_type(iu // i32, np.signedinteger | np.float64)
assert_type(iu // i64, np.int64 | np.float64)
assert_type(iu // u8, np.integer)
assert_type(iu // u16, np.integer)
assert_type(iu // u32, np.integer)
assert_type(iu // u64, np.uint64 | np.float64)
assert_type(iu // f16, np.floating)
assert_type(iu // f32, np.floating)
assert_type(iu // f64, np.float64)
assert_type(iu // f64l, np.longdouble)
iu // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu // i, np.signedinteger | np.float64)
assert_type(iu // u, np.integer | np.float64)
assert_type(iu // f, np.floating)
iu // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu // iu, np.integer | np.float64)
iu // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc // b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc // iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]mod__

assert_type(b1 % b_py, np.int8)
assert_type(b1 % i_py, np.int_)
assert_type(b1 % f_py, np.float64)
b1 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 % b1, np.int8)
assert_type(b1 % i8, np.int8)
assert_type(b1 % i16, np.int16)
assert_type(b1 % i32, np.int32)
assert_type(b1 % i64, np.int64)
assert_type(b1 % u8, np.uint8)
assert_type(b1 % u16, np.uint16)
assert_type(b1 % u32, np.uint32)
assert_type(b1 % u64, np.uint64)
assert_type(b1 % f16, np.float16)
assert_type(b1 % f32, np.float32)
assert_type(b1 % f64, np.float64)
assert_type(b1 % f64l, np.longdouble)
b1 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 % i, np.signedinteger)
assert_type(b1 % u, np.unsignedinteger)
assert_type(b1 % f, np.floating)
b1 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1 % iu, np.integer)
b1 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8 % b_py, np.int8)
assert_type(i8 % i_py, np.int8)
assert_type(i8 % f_py, np.float64)
i8 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 % b1, np.int8)
assert_type(i8 % i8, np.int8)
assert_type(i8 % i16, np.int16)
assert_type(i8 % i32, np.int32)
assert_type(i8 % i64, np.int64)
assert_type(i8 % u8, np.int16)
assert_type(i8 % u16, np.int32)
assert_type(i8 % u32, np.int64)
assert_type(i8 % u64, np.float64)
assert_type(i8 % f16, np.float16)
assert_type(i8 % f32, np.float32)
assert_type(i8 % f64, np.float64)
assert_type(i8 % f64l, np.longdouble)
i8 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 % i, np.signedinteger)
assert_type(i8 % u, np.signedinteger | np.float64)
assert_type(i8 % f, np.floating)
i8 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8 % iu, np.signedinteger | np.float64)
i8 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i16 % b_py, np.int16)
assert_type(i16 % i_py, np.int16)
assert_type(i16 % f_py, np.float64)
i16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 % b1, np.int16)
assert_type(i16 % i8, np.int16)
assert_type(i16 % i16, np.int16)
assert_type(i16 % i32, np.int32)
assert_type(i16 % i64, np.int64)
assert_type(i16 % u8, np.int16)
assert_type(i16 % u16, np.int32)
assert_type(i16 % u32, np.int64)
assert_type(i16 % u64, np.float64)
assert_type(i16 % f16, np.float32)
assert_type(i16 % f32, np.float32)
assert_type(i16 % f64, np.float64)
assert_type(i16 % f64l, np.longdouble)
i16 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 % i, np.signedinteger)
assert_type(i16 % u, np.signedinteger | np.float64)
assert_type(i16 % f, np.floating)
i16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i16 % iu, np.signedinteger | np.float64)
i16 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i16 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i32 % b_py, np.int32)
assert_type(i32 % i_py, np.int32)
assert_type(i32 % f_py, np.float64)
i32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 % b1, np.int32)
assert_type(i32 % i8, np.int32)
assert_type(i32 % i16, np.int32)
assert_type(i32 % i32, np.int32)
assert_type(i32 % i64, np.int64)
assert_type(i32 % u8, np.int32)
assert_type(i32 % u16, np.int32)
assert_type(i32 % u32, np.int64)
assert_type(i32 % u64, np.float64)
assert_type(i32 % f16, np.float64)
assert_type(i32 % f32, np.float64)
assert_type(i32 % f64, np.float64)
assert_type(i32 % f64l, np.longdouble)
i32 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 % i, np.signedinteger)
assert_type(i32 % u, np.signedinteger | np.float64)
assert_type(i32 % f, np.floating)
i32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i32 % iu, np.signedinteger | np.float64)
i32 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i32 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i64 % b_py, np.int64)
assert_type(i64 % i_py, np.int64)
assert_type(i64 % f_py, np.float64)
i64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 % b1, np.int64)
assert_type(i64 % i8, np.int64)
assert_type(i64 % i16, np.int64)
assert_type(i64 % i32, np.int64)
assert_type(i64 % i64, np.int64)
assert_type(i64 % u8, np.int64)
assert_type(i64 % u16, np.int64)
assert_type(i64 % u32, np.int64)
assert_type(i64 % u64, np.float64)
assert_type(i64 % f16, np.float64)
assert_type(i64 % f32, np.float64)
assert_type(i64 % f64, np.float64)
assert_type(i64 % f64l, np.longdouble)
i64 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 % i, np.int64)
assert_type(i64 % u, np.int64 | np.float64)
assert_type(i64 % f, np.floating)
i64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i64 % iu, np.int64 | np.float64)
i64 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i64 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8 % b_py, np.uint8)
assert_type(u8 % i_py, np.uint8)
assert_type(u8 % f_py, np.float64)
u8 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 % b1, np.uint8)
assert_type(u8 % i8, np.int16)
assert_type(u8 % i16, np.int16)
assert_type(u8 % i32, np.int32)
assert_type(u8 % i64, np.int64)
assert_type(u8 % u8, np.uint8)
assert_type(u8 % u16, np.uint16)
assert_type(u8 % u32, np.uint32)
assert_type(u8 % u64, np.uint64)
assert_type(u8 % f16, np.float16)
assert_type(u8 % f32, np.float32)
assert_type(u8 % f64, np.float64)
assert_type(u8 % f64l, np.longdouble)
u8 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 % i, np.signedinteger)
assert_type(u8 % u, np.unsignedinteger)
assert_type(u8 % f, np.floating)
u8 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8 % iu, np.integer)
u8 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u16 % b_py, np.uint16)
assert_type(u16 % i_py, np.uint16)
assert_type(u16 % f_py, np.float64)
u16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 % b1, np.uint16)
assert_type(u16 % i8, np.int32)
assert_type(u16 % i16, np.int32)
assert_type(u16 % i32, np.int32)
assert_type(u16 % i64, np.int64)
assert_type(u16 % u8, np.uint16)
assert_type(u16 % u16, np.uint16)
assert_type(u16 % u32, np.uint32)
assert_type(u16 % u64, np.uint64)
assert_type(u16 % f16, np.float32)
assert_type(u16 % f32, np.float32)
assert_type(u16 % f64, np.float64)
assert_type(u16 % f64l, np.longdouble)
u16 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 % i, np.signedinteger)
assert_type(u16 % u, np.unsignedinteger)
assert_type(u16 % f, np.floating)
u16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u16 % iu, np.integer)
u16 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u16 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u32 % b_py, np.uint32)
assert_type(u32 % i_py, np.uint32)
assert_type(u32 % f_py, np.float64)
u32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 % b1, np.uint32)
assert_type(u32 % i8, np.int64)
assert_type(u32 % i16, np.int64)
assert_type(u32 % i32, np.int64)
assert_type(u32 % i64, np.int64)
assert_type(u32 % u8, np.uint32)
assert_type(u32 % u16, np.uint32)
assert_type(u32 % u32, np.uint32)
assert_type(u32 % u64, np.uint64)
assert_type(u32 % f16, np.float64)
assert_type(u32 % f32, np.float64)
assert_type(u32 % f64, np.float64)
assert_type(u32 % f64l, np.longdouble)
u32 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 % i, np.int64)
assert_type(u32 % u, np.unsignedinteger)
assert_type(u32 % f, np.floating)
u32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u32 % iu, np.integer)
u32 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u32 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u64 % b_py, np.uint64)
assert_type(u64 % i_py, np.uint64)
assert_type(u64 % f_py, np.float64)
u64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 % b1, np.uint64)
assert_type(u64 % i8, np.float64)
assert_type(u64 % i16, np.float64)
assert_type(u64 % i32, np.float64)
assert_type(u64 % i64, np.float64)
assert_type(u64 % u8, np.uint64)
assert_type(u64 % u16, np.uint64)
assert_type(u64 % u32, np.uint64)
assert_type(u64 % u64, np.uint64)
assert_type(u64 % f16, np.float64)
assert_type(u64 % f32, np.float64)
assert_type(u64 % f64, np.float64)
assert_type(u64 % f64l, np.longdouble)
u64 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 % i, np.float64)
assert_type(u64 % u, np.uint64)
assert_type(u64 % f, np.floating)
u64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u64 % iu, np.uint64 | np.float64)
u64 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u64 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f16 % b_py, np.float16)
assert_type(f16 % i_py, np.float16)
assert_type(f16 % f_py, np.float16)
f16 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 % b1, np.float16)
assert_type(f16 % i8, np.float16)
assert_type(f16 % i16, np.float32)
assert_type(f16 % i32, np.float64)
assert_type(f16 % i64, np.float64)
assert_type(f16 % u8, np.float16)
assert_type(f16 % u16, np.float32)
assert_type(f16 % u32, np.float64)
assert_type(f16 % u64, np.float64)
assert_type(f16 % f16, np.float16)
assert_type(f16 % f32, np.float32)
assert_type(f16 % f64, np.float64)
assert_type(f16 % f64l, np.longdouble)
f16 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 % i, np.floating)
assert_type(f16 % u, np.floating)
assert_type(f16 % f, np.floating)
f16 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f16 % iu, np.floating)
f16 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f16 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f32 % b_py, np.float32)
assert_type(f32 % i_py, np.float32)
assert_type(f32 % f_py, np.float32)
f32 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 % b1, np.float32)
assert_type(f32 % i8, np.float32)
assert_type(f32 % i16, np.float32)
assert_type(f32 % i32, np.float64)
assert_type(f32 % i64, np.float64)
assert_type(f32 % u8, np.float32)
assert_type(f32 % u16, np.float32)
assert_type(f32 % u32, np.float64)
assert_type(f32 % u64, np.float64)
assert_type(f32 % f16, np.float32)
assert_type(f32 % f32, np.float32)
assert_type(f32 % f64, np.float64)
assert_type(f32 % f64l, np.longdouble)
f32 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 % i, np.floating)
assert_type(f32 % u, np.floating)
assert_type(f32 % f, np.floating)
f32 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f32 % iu, np.floating)
f32 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f32 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64 % b_py, np.float64)
assert_type(f64 % i_py, np.float64)
assert_type(f64 % f_py, np.float64)
f64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 % b1, np.float64)
assert_type(f64 % i8, np.float64)
assert_type(f64 % i16, np.float64)
assert_type(f64 % i32, np.float64)
assert_type(f64 % i64, np.float64)
assert_type(f64 % u8, np.float64)
assert_type(f64 % u16, np.float64)
assert_type(f64 % u32, np.float64)
assert_type(f64 % u64, np.float64)
assert_type(f64 % f16, np.float64)
assert_type(f64 % f32, np.float64)
assert_type(f64 % f64, np.float64)
assert_type(f64 % f64l, np.longdouble)
f64 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 % i, np.float64)
assert_type(f64 % u, np.float64)
assert_type(f64 % f, np.floating)
f64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64 % iu, np.float64)
f64 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f64l % b_py, np.longdouble)
assert_type(f64l % i_py, np.longdouble)
assert_type(f64l % f_py, np.longdouble)
f64l % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l % b1, np.longdouble)
assert_type(f64l % i8, np.longdouble)
assert_type(f64l % i16, np.longdouble)
assert_type(f64l % i32, np.longdouble)
assert_type(f64l % i64, np.longdouble)
assert_type(f64l % u8, np.longdouble)
assert_type(f64l % u16, np.longdouble)
assert_type(f64l % u32, np.longdouble)
assert_type(f64l % u64, np.longdouble)
assert_type(f64l % f16, np.longdouble)
assert_type(f64l % f32, np.longdouble)
assert_type(f64l % f64, np.longdouble)
assert_type(f64l % f64l, np.longdouble)
f64l % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l % i, np.longdouble)
assert_type(f64l % u, np.longdouble)
assert_type(f64l % f, np.longdouble)
f64l % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f64l % iu, np.longdouble)
f64l % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f64l % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c128 % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c128 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m64 % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m64 % m64, np.timedelta64)
m64 % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m64 % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i % b_py, np.signedinteger)
assert_type(i % i_py, np.signedinteger)
assert_type(i % f_py, np.float64)
i % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i % b1, np.signedinteger)
assert_type(i % i8, np.signedinteger)
assert_type(i % i16, np.signedinteger)
assert_type(i % i32, np.signedinteger)
assert_type(i % i64, np.int64)
assert_type(i % u8, np.signedinteger)
assert_type(i % u16, np.signedinteger)
assert_type(i % u32, np.int64)
assert_type(i % u64, np.float64)
assert_type(i % f16, np.floating)
assert_type(i % f32, np.floating)
assert_type(i % f64, np.float64)
assert_type(i % f64l, np.longdouble)
i % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i % i, np.signedinteger)
assert_type(i % u, np.signedinteger | np.float64)
assert_type(i % f, np.floating)
i % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i % iu, np.signedinteger | np.float64)
i % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u % b_py, np.unsignedinteger)
assert_type(u % i_py, np.unsignedinteger)
assert_type(u % f_py, np.float64)
u % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u % b1, np.unsignedinteger)
assert_type(u % i8, np.signedinteger | np.float64)
assert_type(u % i16, np.signedinteger | np.float64)
assert_type(u % i32, np.signedinteger | np.float64)
assert_type(u % i64, np.int64 | np.float64)
assert_type(u % u8, np.unsignedinteger)
assert_type(u % u16, np.unsignedinteger)
assert_type(u % u32, np.unsignedinteger)
assert_type(u % u64, np.uint64)
assert_type(u % f16, np.floating)
assert_type(u % f32, np.floating)
assert_type(u % f64, np.float64)
assert_type(u % f64l, np.longdouble)
u % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u % i, np.signedinteger | np.float64)
assert_type(u % u, np.unsignedinteger)
assert_type(u % f, np.floating)
u % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u % iu, np.integer | np.float64)
u % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f % b_py, np.floating)
assert_type(f % i_py, np.floating)
assert_type(f % f_py, np.floating)
f % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f % b1, np.floating)
assert_type(f % i8, np.floating)
assert_type(f % i16, np.floating)
assert_type(f % i32, np.floating)
assert_type(f % i64, np.floating)
assert_type(f % u8, np.floating)
assert_type(f % u16, np.floating)
assert_type(f % u32, np.floating)
assert_type(f % u64, np.floating)
assert_type(f % f16, np.floating)
assert_type(f % f32, np.floating)
assert_type(f % f64, np.floating)
assert_type(f % f64l, np.longdouble)
f % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f % i, np.floating)
assert_type(f % u, np.floating)
assert_type(f % f, np.floating)
f % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f % iu, np.floating)
f % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu % b_py, np.integer)
assert_type(iu % i_py, np.integer)
assert_type(iu % f_py, np.float64)
iu % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu % b1, np.integer)
assert_type(iu % i8, np.signedinteger | np.float64)
assert_type(iu % i16, np.signedinteger | np.float64)
assert_type(iu % i32, np.signedinteger | np.float64)
assert_type(iu % i64, np.int64 | np.float64)
assert_type(iu % u8, np.integer)
assert_type(iu % u16, np.integer)
assert_type(iu % u32, np.integer)
assert_type(iu % u64, np.uint64 | np.float64)
assert_type(iu % f16, np.floating)
assert_type(iu % f32, np.floating)
assert_type(iu % f64, np.float64)
assert_type(iu % f64l, np.longdouble)
iu % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu % i, np.signedinteger | np.float64)
assert_type(iu % u, np.integer | np.float64)
assert_type(iu % f, np.floating)
iu % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu % iu, np.integer | np.float64)
iu % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

fc % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

iufc % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % u8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % u16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % u32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % u64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f16  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f32  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f64l  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % c128  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % m64  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % iu  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % fc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc % iufc  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

###
# __[r]divmod__

assert_type(divmod(b1, b_py), tuple[np.int8, np.int8])
assert_type(divmod(b1, i_py), tuple[np.int64, np.int64])
assert_type(divmod(b1, f_py), tuple[np.float64, np.float64])
divmod(b1, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1, b1), tuple[np.int8, np.int8])
assert_type(divmod(b1, i8), tuple[np.int8, np.int8])
assert_type(divmod(b1, i16), tuple[np.int16, np.int16])
assert_type(divmod(b1, i32), tuple[np.int32, np.int32])
assert_type(divmod(b1, i64), tuple[np.int64, np.int64])
assert_type(divmod(b1, u8), tuple[np.uint8, np.uint8])
assert_type(divmod(b1, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(b1, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(b1, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(b1, f16), tuple[np.float16, np.float16])
assert_type(divmod(b1, f32), tuple[np.float32, np.float32])
assert_type(divmod(b1, f64), tuple[np.float64, np.float64])
assert_type(divmod(b1, f64l), tuple[np.longdouble, np.longdouble])
divmod(b1, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(b1, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(b1, f), tuple[np.floating, np.floating])
divmod(b1, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1, iu), tuple[np.integer, np.integer])
divmod(b1, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i8, b_py), tuple[np.int8, np.int8])
assert_type(divmod(i8, i_py), tuple[np.int8, np.int8])
assert_type(divmod(i8, f_py), tuple[np.float64, np.float64])
divmod(i8, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8, b1), tuple[np.int8, np.int8])
assert_type(divmod(i8, i8), tuple[np.int8, np.int8])
assert_type(divmod(i8, i16), tuple[np.int16, np.int16])
assert_type(divmod(i8, i32), tuple[np.int32, np.int32])
assert_type(divmod(i8, i64), tuple[np.int64, np.int64])
assert_type(divmod(i8, u8), tuple[np.int16, np.int16])
assert_type(divmod(i8, u16), tuple[np.int32, np.int32])
assert_type(divmod(i8, u32), tuple[np.int64, np.int64])
assert_type(divmod(i8, u64), tuple[np.float64, np.float64])
assert_type(divmod(i8, f16), tuple[np.float16, np.float16])
assert_type(divmod(i8, f32), tuple[np.float32, np.float32])
assert_type(divmod(i8, f64), tuple[np.float64, np.float64])
assert_type(divmod(i8, f64l), tuple[np.longdouble, np.longdouble])
divmod(i8, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i8, u), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(i8, f), tuple[np.floating, np.floating])
divmod(i8, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8, iu), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
divmod(i8, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i16, b_py), tuple[np.int16, np.int16])
assert_type(divmod(i16, i_py), tuple[np.int16, np.int16])
assert_type(divmod(i16, f_py), tuple[np.float64, np.float64])
divmod(i16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i16, b1), tuple[np.int16, np.int16])
assert_type(divmod(i16, i8), tuple[np.int16, np.int16])
assert_type(divmod(i16, i16), tuple[np.int16, np.int16])
assert_type(divmod(i16, i32), tuple[np.int32, np.int32])
assert_type(divmod(i16, i64), tuple[np.int64, np.int64])
assert_type(divmod(i16, u8), tuple[np.int16, np.int16])
assert_type(divmod(i16, u16), tuple[np.int32, np.int32])
assert_type(divmod(i16, u32), tuple[np.int64, np.int64])
assert_type(divmod(i16, u64), tuple[np.float64, np.float64])
assert_type(divmod(i16, f16), tuple[np.float32, np.float32])
assert_type(divmod(i16, f32), tuple[np.float32, np.float32])
assert_type(divmod(i16, f64), tuple[np.float64, np.float64])
assert_type(divmod(i16, f64l), tuple[np.longdouble, np.longdouble])
divmod(i16, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i16, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i16, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i16, u), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(i16, f), tuple[np.floating, np.floating])
divmod(i16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i16, iu), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
divmod(i16, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i16, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i32, b_py), tuple[np.int32, np.int32])
assert_type(divmod(i32, i_py), tuple[np.int32, np.int32])
assert_type(divmod(i32, f_py), tuple[np.float64, np.float64])
divmod(i32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i32, b1), tuple[np.int32, np.int32])
assert_type(divmod(i32, i8), tuple[np.int32, np.int32])
assert_type(divmod(i32, i16), tuple[np.int32, np.int32])
assert_type(divmod(i32, i32), tuple[np.int32, np.int32])
assert_type(divmod(i32, i64), tuple[np.int64, np.int64])
assert_type(divmod(i32, u8), tuple[np.int32, np.int32])
assert_type(divmod(i32, u16), tuple[np.int32, np.int32])
assert_type(divmod(i32, u32), tuple[np.int64, np.int64])
assert_type(divmod(i32, u64), tuple[np.float64, np.float64])
assert_type(divmod(i32, f16), tuple[np.float64, np.float64])
assert_type(divmod(i32, f32), tuple[np.float64, np.float64])
assert_type(divmod(i32, f64), tuple[np.float64, np.float64])
assert_type(divmod(i32, f64l), tuple[np.longdouble, np.longdouble])
divmod(i32, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i32, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i32, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i32, u), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(i32, f), tuple[np.floating, np.floating])
divmod(i32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i32, iu), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
divmod(i32, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i32, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i64, b_py), tuple[np.int64, np.int64])
assert_type(divmod(i64, i_py), tuple[np.int64, np.int64])
assert_type(divmod(i64, f_py), tuple[np.float64, np.float64])
divmod(i64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i64, b1), tuple[np.int64, np.int64])
assert_type(divmod(i64, i8), tuple[np.int64, np.int64])
assert_type(divmod(i64, i16), tuple[np.int64, np.int64])
assert_type(divmod(i64, i32), tuple[np.int64, np.int64])
assert_type(divmod(i64, i64), tuple[np.int64, np.int64])
assert_type(divmod(i64, u8), tuple[np.int64, np.int64])
assert_type(divmod(i64, u16), tuple[np.int64, np.int64])
assert_type(divmod(i64, u32), tuple[np.int64, np.int64])
assert_type(divmod(i64, u64), tuple[np.float64, np.float64])
assert_type(divmod(i64, f16), tuple[np.float64, np.float64])
assert_type(divmod(i64, f32), tuple[np.float64, np.float64])
assert_type(divmod(i64, f64), tuple[np.float64, np.float64])
assert_type(divmod(i64, f64l), tuple[np.longdouble, np.longdouble])
divmod(i64, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i64, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i64, i), tuple[np.int64, np.int64])
assert_type(divmod(i64, u), tuple[np.int64 | np.float64, np.int64 | np.float64])
assert_type(divmod(i64, f), tuple[np.floating, np.floating])
divmod(i64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i64, iu), tuple[np.int64 | np.float64, np.int64 | np.float64])
divmod(i64, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i64, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u8, b_py), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, i_py), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, f_py), tuple[np.float64, np.float64])
divmod(u8, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8, b1), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, i8), tuple[np.int16, np.int16])
assert_type(divmod(u8, i16), tuple[np.int16, np.int16])
assert_type(divmod(u8, i32), tuple[np.int32, np.int32])
assert_type(divmod(u8, i64), tuple[np.int64, np.int64])
assert_type(divmod(u8, u8), tuple[np.uint8, np.uint8])
assert_type(divmod(u8, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(u8, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u8, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u8, f16), tuple[np.float16, np.float16])
assert_type(divmod(u8, f32), tuple[np.float32, np.float32])
assert_type(divmod(u8, f64), tuple[np.float64, np.float64])
assert_type(divmod(u8, f64l), tuple[np.longdouble, np.longdouble])
divmod(u8, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(u8, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u8, f), tuple[np.floating, np.floating])
divmod(u8, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8, iu), tuple[np.integer, np.integer])
divmod(u8, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u16, b_py), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, i_py), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, f_py), tuple[np.float64, np.float64])
divmod(u16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u16, b1), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, i8), tuple[np.int32, np.int32])
assert_type(divmod(u16, i16), tuple[np.int32, np.int32])
assert_type(divmod(u16, i32), tuple[np.int32, np.int32])
assert_type(divmod(u16, i64), tuple[np.int64, np.int64])
assert_type(divmod(u16, u8), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, u16), tuple[np.uint16, np.uint16])
assert_type(divmod(u16, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u16, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u16, f16), tuple[np.float32, np.float32])
assert_type(divmod(u16, f32), tuple[np.float32, np.float32])
assert_type(divmod(u16, f64), tuple[np.float64, np.float64])
assert_type(divmod(u16, f64l), tuple[np.longdouble, np.longdouble])
divmod(u16, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u16, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u16, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(u16, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u16, f), tuple[np.floating, np.floating])
divmod(u16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u16, iu), tuple[np.integer, np.integer])
divmod(u16, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u16, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u32, b_py), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, i_py), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, f_py), tuple[np.float64, np.float64])
divmod(u32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u32, b1), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, i8), tuple[np.int64, np.int64])
assert_type(divmod(u32, i16), tuple[np.int64, np.int64])
assert_type(divmod(u32, i32), tuple[np.int64, np.int64])
assert_type(divmod(u32, i64), tuple[np.int64, np.int64])
assert_type(divmod(u32, u8), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u16), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u32), tuple[np.uint32, np.uint32])
assert_type(divmod(u32, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u32, f16), tuple[np.float64, np.float64])
assert_type(divmod(u32, f32), tuple[np.float64, np.float64])
assert_type(divmod(u32, f64), tuple[np.float64, np.float64])
assert_type(divmod(u32, f64l), tuple[np.longdouble, np.longdouble])
divmod(u32, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u32, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u32, i), tuple[np.int64, np.int64])
assert_type(divmod(u32, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u32, f), tuple[np.floating, np.floating])
divmod(u32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u32, iu), tuple[np.integer, np.integer])
divmod(u32, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u32, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u64, b_py), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, i_py), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, f_py), tuple[np.float64, np.float64])
divmod(u64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u64, b1), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, i8), tuple[np.float64, np.float64])
assert_type(divmod(u64, i16), tuple[np.float64, np.float64])
assert_type(divmod(u64, i32), tuple[np.float64, np.float64])
assert_type(divmod(u64, i64), tuple[np.float64, np.float64])
assert_type(divmod(u64, u8), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u16), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u32), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, f16), tuple[np.float64, np.float64])
assert_type(divmod(u64, f32), tuple[np.float64, np.float64])
assert_type(divmod(u64, f64), tuple[np.float64, np.float64])
assert_type(divmod(u64, f64l), tuple[np.longdouble, np.longdouble])
divmod(u64, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u64, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u64, i), tuple[np.float64, np.float64])
assert_type(divmod(u64, u), tuple[np.uint64, np.uint64])
assert_type(divmod(u64, f), tuple[np.floating, np.floating])
divmod(u64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u64, iu), tuple[np.uint64 | np.float64, np.uint64 | np.float64])
divmod(u64, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u64, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f16, b_py), tuple[np.float16, np.float16])
assert_type(divmod(f16, i_py), tuple[np.float16, np.float16])
assert_type(divmod(f16, f_py), tuple[np.float16, np.float16])
divmod(f16, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f16, b1), tuple[np.float16, np.float16])
assert_type(divmod(f16, i8), tuple[np.float16, np.float16])
assert_type(divmod(f16, i16), tuple[np.float32, np.float32])
assert_type(divmod(f16, i32), tuple[np.float64, np.float64])
assert_type(divmod(f16, i64), tuple[np.float64, np.float64])
assert_type(divmod(f16, u8), tuple[np.float16, np.float16])
assert_type(divmod(f16, u16), tuple[np.float32, np.float32])
assert_type(divmod(f16, u32), tuple[np.float64, np.float64])
assert_type(divmod(f16, u64), tuple[np.float64, np.float64])
assert_type(divmod(f16, f16), tuple[np.float16, np.float16])
assert_type(divmod(f16, f32), tuple[np.float32, np.float32])
assert_type(divmod(f16, f64), tuple[np.float64, np.float64])
assert_type(divmod(f16, f64l), tuple[np.longdouble, np.longdouble])
divmod(f16, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f16, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f16, i), tuple[np.floating, np.floating])
assert_type(divmod(f16, u), tuple[np.floating, np.floating])
assert_type(divmod(f16, f), tuple[np.floating, np.floating])
divmod(f16, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f16, iu), tuple[np.floating, np.floating])
divmod(f16, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f16, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f32, b_py), tuple[np.float32, np.float32])
assert_type(divmod(f32, i_py), tuple[np.float32, np.float32])
assert_type(divmod(f32, f_py), tuple[np.float32, np.float32])
divmod(f32, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f32, b1), tuple[np.float32, np.float32])
assert_type(divmod(f32, i8), tuple[np.float32, np.float32])
assert_type(divmod(f32, i16), tuple[np.float32, np.float32])
assert_type(divmod(f32, i32), tuple[np.float64, np.float64])
assert_type(divmod(f32, i64), tuple[np.float64, np.float64])
assert_type(divmod(f32, u8), tuple[np.float32, np.float32])
assert_type(divmod(f32, u16), tuple[np.float32, np.float32])
assert_type(divmod(f32, u32), tuple[np.float64, np.float64])
assert_type(divmod(f32, u64), tuple[np.float64, np.float64])
assert_type(divmod(f32, f16), tuple[np.float32, np.float32])
assert_type(divmod(f32, f32), tuple[np.float32, np.float32])
assert_type(divmod(f32, f64), tuple[np.float64, np.float64])
assert_type(divmod(f32, f64l), tuple[np.longdouble, np.longdouble])
divmod(f32, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f32, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f32, i), tuple[np.floating, np.floating])
assert_type(divmod(f32, u), tuple[np.floating, np.floating])
assert_type(divmod(f32, f), tuple[np.floating, np.floating])
divmod(f32, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f32, iu), tuple[np.floating, np.floating])
divmod(f32, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f32, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f64, b_py), tuple[np.float64, np.float64])
assert_type(divmod(f64, i_py), tuple[np.float64, np.float64])
assert_type(divmod(f64, f_py), tuple[np.float64, np.float64])
divmod(f64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64, b1), tuple[np.float64, np.float64])
assert_type(divmod(f64, i8), tuple[np.float64, np.float64])
assert_type(divmod(f64, i16), tuple[np.float64, np.float64])
assert_type(divmod(f64, i32), tuple[np.float64, np.float64])
assert_type(divmod(f64, i64), tuple[np.float64, np.float64])
assert_type(divmod(f64, u8), tuple[np.float64, np.float64])
assert_type(divmod(f64, u16), tuple[np.float64, np.float64])
assert_type(divmod(f64, u32), tuple[np.float64, np.float64])
assert_type(divmod(f64, u64), tuple[np.float64, np.float64])
assert_type(divmod(f64, f16), tuple[np.float64, np.float64])
assert_type(divmod(f64, f32), tuple[np.float64, np.float64])
assert_type(divmod(f64, f64), tuple[np.float64, np.float64])
assert_type(divmod(f64, f64l), tuple[np.longdouble, np.longdouble])
divmod(f64, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64, i), tuple[np.float64, np.float64])
assert_type(divmod(f64, u), tuple[np.float64, np.float64])
assert_type(divmod(f64, f), tuple[np.floating, np.floating])
divmod(f64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64, iu), tuple[np.float64, np.float64])
divmod(f64, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f64l, b_py), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i_py), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f_py), tuple[np.longdouble, np.longdouble])
divmod(f64l, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64l, b1), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i8), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, i64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u8), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f16), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f32), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f64), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f64l), tuple[np.longdouble, np.longdouble])
divmod(f64l, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64l, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64l, i), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, u), tuple[np.longdouble, np.longdouble])
assert_type(divmod(f64l, f), tuple[np.longdouble, np.longdouble])
divmod(f64l, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f64l, iu), tuple[np.longdouble, np.longdouble])
divmod(f64l, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f64l, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c128, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, iu)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c128, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(m64, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(m64, m64), tuple[np.int64, np.timedelta64])
divmod(m64, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, iu)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m64, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i, b_py), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i_py), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, f_py), tuple[np.float64, np.float64])
divmod(i, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i, b1), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i8), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i16), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i32), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, i64), tuple[np.int64, np.int64])
assert_type(divmod(i, u8), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u16), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u32), tuple[np.int64, np.int64])
assert_type(divmod(i, u64), tuple[np.float64, np.float64])
assert_type(divmod(i, f16), tuple[np.floating, np.floating])
assert_type(divmod(i, f32), tuple[np.floating, np.floating])
assert_type(divmod(i, f64), tuple[np.float64, np.float64])
assert_type(divmod(i, f64l), tuple[np.longdouble, np.longdouble])
divmod(i, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i, i), tuple[np.signedinteger, np.signedinteger])
assert_type(divmod(i, u), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(i, f), tuple[np.floating, np.floating])
divmod(i, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i, iu), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
divmod(i, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u, b_py), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, i_py), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, f_py), tuple[np.float64, np.float64])
divmod(u, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u, b1), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, i8), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(u, i16), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(u, i32), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(u, i64), tuple[np.int64 | np.float64, np.int64 | np.float64])
assert_type(divmod(u, u8), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u16), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u32), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, u64), tuple[np.uint64, np.uint64])
assert_type(divmod(u, f16), tuple[np.floating, np.floating])
assert_type(divmod(u, f32), tuple[np.floating, np.floating])
assert_type(divmod(u, f64), tuple[np.float64, np.float64])
assert_type(divmod(u, f64l), tuple[np.longdouble, np.longdouble])
divmod(u, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u, i), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(u, u), tuple[np.unsignedinteger, np.unsignedinteger])
assert_type(divmod(u, f), tuple[np.floating, np.floating])
divmod(u, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u, iu), tuple[np.integer | np.float64, np.integer | np.float64])
divmod(u, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f, b_py), tuple[np.floating, np.floating])
assert_type(divmod(f, i_py), tuple[np.floating, np.floating])
assert_type(divmod(f, f_py), tuple[np.floating, np.floating])
divmod(f, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f, b1), tuple[np.floating, np.floating])
assert_type(divmod(f, i8), tuple[np.floating, np.floating])
assert_type(divmod(f, i16), tuple[np.floating, np.floating])
assert_type(divmod(f, i32), tuple[np.floating, np.floating])
assert_type(divmod(f, i64), tuple[np.floating, np.floating])
assert_type(divmod(f, u8), tuple[np.floating, np.floating])
assert_type(divmod(f, u16), tuple[np.floating, np.floating])
assert_type(divmod(f, u32), tuple[np.floating, np.floating])
assert_type(divmod(f, u64), tuple[np.floating, np.floating])
assert_type(divmod(f, f16), tuple[np.floating, np.floating])
assert_type(divmod(f, f32), tuple[np.floating, np.floating])
assert_type(divmod(f, f64), tuple[np.floating, np.floating])
assert_type(divmod(f, f64l), tuple[np.longdouble, np.longdouble])
divmod(f, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f, i), tuple[np.floating, np.floating])
assert_type(divmod(f, u), tuple[np.floating, np.floating])
assert_type(divmod(f, f), tuple[np.floating, np.floating])
divmod(f, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f, iu), tuple[np.floating, np.floating])
divmod(f, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, iu)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(iu, b_py), tuple[np.integer, np.integer])
assert_type(divmod(iu, i_py), tuple[np.integer, np.integer])
assert_type(divmod(iu, f_py), tuple[np.float64, np.float64])
divmod(iu, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(iu, b1), tuple[np.integer, np.integer])
assert_type(divmod(iu, i8), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(iu, i16), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(iu, i32), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(iu, i64), tuple[np.int64 | np.float64, np.int64 | np.float64])
assert_type(divmod(iu, u8), tuple[np.integer, np.integer])
assert_type(divmod(iu, u16), tuple[np.integer, np.integer])
assert_type(divmod(iu, u32), tuple[np.integer, np.integer])
assert_type(divmod(iu, u64), tuple[np.uint64 | np.float64, np.uint64 | np.float64])
assert_type(divmod(iu, f16), tuple[np.floating, np.floating])
assert_type(divmod(iu, f32), tuple[np.floating, np.floating])
assert_type(divmod(iu, f64), tuple[np.float64, np.float64])
assert_type(divmod(iu, f64l), tuple[np.longdouble, np.longdouble])
divmod(iu, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iu, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(iu, i), tuple[np.signedinteger | np.float64, np.signedinteger | np.float64])
assert_type(divmod(iu, u), tuple[np.integer | np.float64, np.integer | np.float64])
assert_type(divmod(iu, f), tuple[np.floating, np.floating])
divmod(iu, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(iu, iu), tuple[np.integer | np.float64, np.integer | np.float64])
divmod(iu, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iu, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(fc, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, iu)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fc, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(iufc, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, b1)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, u8)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, u16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, u32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, u64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f16)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f32)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f64l)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, c128)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, m64)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, i)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, u)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, f)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, c)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, iu)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, fc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iufc, iufc)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
