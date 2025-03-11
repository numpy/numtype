# @generated 2025-03-11T03:12:57Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np

###

SC_u1: np.uint8
SC_u2: np.uint16
SC_u4: np.uint32
SC_u8: np.uint64
SC_i1: np.int8
SC_i2: np.int16
SC_i4: np.int32
SC_i8: np.int64
SC_f2: np.float16
SC_f4: np.float32
SC_f8: np.float64
SC_g: np.longdouble
SC_c8: np.complex64
SC_c16: np.complex128
SC_G: np.clongdouble

###
# np.emath.sqrt

assert_type(np.emath.sqrt(SC_u1), np.float16)
assert_type(np.emath.sqrt(SC_u2), np.float32)
assert_type(np.emath.sqrt(SC_u4), np.float64)
assert_type(np.emath.sqrt(SC_u8), np.float64)
assert_type(np.emath.sqrt(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.sqrt(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.sqrt(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.sqrt(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.sqrt(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.sqrt(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.sqrt(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.sqrt(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.sqrt(SC_c8), np.complex64)
assert_type(np.emath.sqrt(SC_c16), np.complex128)
assert_type(np.emath.sqrt(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.log

assert_type(np.emath.log(SC_u1), np.float16)
assert_type(np.emath.log(SC_u2), np.float32)
assert_type(np.emath.log(SC_u4), np.float64)
assert_type(np.emath.log(SC_u8), np.float64)
assert_type(np.emath.log(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.log(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.log(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.log(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.log(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.log(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.log(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.log(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.log(SC_c8), np.complex64)
assert_type(np.emath.log(SC_c16), np.complex128)
assert_type(np.emath.log(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.log2

assert_type(np.emath.log2(SC_u1), np.float16)
assert_type(np.emath.log2(SC_u2), np.float32)
assert_type(np.emath.log2(SC_u4), np.float64)
assert_type(np.emath.log2(SC_u8), np.float64)
assert_type(np.emath.log2(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.log2(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.log2(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.log2(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.log2(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.log2(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.log2(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.log2(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.log2(SC_c8), np.complex64)
assert_type(np.emath.log2(SC_c16), np.complex128)
assert_type(np.emath.log2(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.log10

assert_type(np.emath.log10(SC_u1), np.float16)
assert_type(np.emath.log10(SC_u2), np.float32)
assert_type(np.emath.log10(SC_u4), np.float64)
assert_type(np.emath.log10(SC_u8), np.float64)
assert_type(np.emath.log10(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.log10(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.log10(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.log10(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.log10(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.log10(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.log10(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.log10(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.log10(SC_c8), np.complex64)
assert_type(np.emath.log10(SC_c16), np.complex128)
assert_type(np.emath.log10(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.arccos

assert_type(np.emath.arccos(SC_u1), np.float16 | np.complex64)
assert_type(np.emath.arccos(SC_u2), np.float32 | np.complex64)
assert_type(np.emath.arccos(SC_u4), np.float64 | np.complex128)
assert_type(np.emath.arccos(SC_u8), np.float64 | np.complex128)
assert_type(np.emath.arccos(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.arccos(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.arccos(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.arccos(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.arccos(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.arccos(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.arccos(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.arccos(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.arccos(SC_c8), np.complex64)
assert_type(np.emath.arccos(SC_c16), np.complex128)
assert_type(np.emath.arccos(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.arcsin

assert_type(np.emath.arcsin(SC_u1), np.float16 | np.complex64)
assert_type(np.emath.arcsin(SC_u2), np.float32 | np.complex64)
assert_type(np.emath.arcsin(SC_u4), np.float64 | np.complex128)
assert_type(np.emath.arcsin(SC_u8), np.float64 | np.complex128)
assert_type(np.emath.arcsin(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.arcsin(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.arcsin(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.arcsin(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.arcsin(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.arcsin(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.arcsin(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.arcsin(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.arcsin(SC_c8), np.complex64)
assert_type(np.emath.arcsin(SC_c16), np.complex128)
assert_type(np.emath.arcsin(SC_G), np.complex128 | np.clongdouble)

###
# np.emath.arctanh

assert_type(np.emath.arctanh(SC_u1), np.float16 | np.complex64)
assert_type(np.emath.arctanh(SC_u2), np.float32 | np.complex64)
assert_type(np.emath.arctanh(SC_u4), np.float64 | np.complex128)
assert_type(np.emath.arctanh(SC_u8), np.float64 | np.complex128)
assert_type(np.emath.arctanh(SC_i1), np.float16 | np.complex64)
assert_type(np.emath.arctanh(SC_i2), np.float32 | np.complex64)
assert_type(np.emath.arctanh(SC_i4), np.float64 | np.complex128)
assert_type(np.emath.arctanh(SC_i8), np.float64 | np.complex128)
assert_type(np.emath.arctanh(SC_f2), np.float16 | np.complex128)
assert_type(np.emath.arctanh(SC_f4), np.float32 | np.complex64)
assert_type(np.emath.arctanh(SC_f8), np.float64 | np.complex128)
assert_type(np.emath.arctanh(SC_g), np.longdouble | np.complex128)
assert_type(np.emath.arctanh(SC_c8), np.complex64)
assert_type(np.emath.arctanh(SC_c16), np.complex128)
assert_type(np.emath.arctanh(SC_G), np.complex128 | np.clongdouble)
