# @generated 2025-05-05T23:12:15Z with tool/testgen.py
from typing import assert_type

import _numtype as _nt
import numpy as np

###

b1_nd: _nt.Array[np.bool]
i1_nd: _nt.Array[np.int8]
i2_nd: _nt.Array[np.int16]
i4_nd: _nt.Array[np.int32]
i8_nd: _nt.Array[np.int64]
u1_nd: _nt.Array[np.uint8]
u2_nd: _nt.Array[np.uint16]
u4_nd: _nt.Array[np.uint32]
u8_nd: _nt.Array[np.uint64]
f2_nd: _nt.Array[np.float16]
f4_nd: _nt.Array[np.float32]
f8_nd: _nt.Array[np.float64]
fld_nd: _nt.Array[np.longdouble]
c16_nd: _nt.Array[np.complex128]
m8_nd: _nt.Array[np.timedelta64]
i_nd: _nt.Array[np.signedinteger]
u_nd: _nt.Array[np.unsignedinteger]
f_nd: _nt.Array[np.floating]
iu_nd: _nt.Array[np.integer]

b_py: bool
i_py: int
f_py: float
c_py: complex

###

###

assert_type(divmod(b1_nd, b1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(b1_nd, i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(b1_nd, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(b1_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(b1_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(b1_nd, u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(b1_nd, u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(b1_nd, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(b1_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(b1_nd, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(b1_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(b1_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(b1_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(b1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(b1_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(b1_nd, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(b1_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(b1_nd, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(divmod(b1_nd, b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(b1_nd, i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(b1_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(b1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, b1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i_py, b1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(f_py, b1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, b1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i1_nd, b1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i1_nd, i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i1_nd, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i1_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i1_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i1_nd, u1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i1_nd, u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i1_nd, u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i1_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i1_nd, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(i1_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(i1_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i1_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i1_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    divmod(i1_nd, u_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(i1_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    divmod(i1_nd, iu_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(divmod(i1_nd, b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i1_nd, i_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i1_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(i_py, i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(divmod(f_py, i1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i2_nd, b1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, i1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i2_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i2_nd, u1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i2_nd, u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i2_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i2_nd, f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(i2_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(i2_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i2_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i2_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    divmod(i2_nd, u_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(i2_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    divmod(i2_nd, iu_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(divmod(i2_nd, b_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, i_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i2_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(i_py, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(f_py, i2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i4_nd, b1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, i1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, i2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i4_nd, u1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i4_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i4_nd, f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i4_nd, f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i4_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i4_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i4_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    divmod(i4_nd, u_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(i4_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    divmod(i4_nd, iu_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(divmod(i4_nd, b_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, i_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i4_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(i_py, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(f_py, i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i8_nd, b1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, i1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, i2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, i4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, u1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, u2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i8_nd, f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i8_nd, f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i8_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i8_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i8_nd, i_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, u_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(divmod(i8_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(i8_nd, iu_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])

assert_type(divmod(i8_nd, b_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i8_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i_py, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(f_py, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u1_nd, b1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(u1_nd, i1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(u1_nd, i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(divmod(u1_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(u1_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u1_nd, u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(u1_nd, u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u1_nd, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u1_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u1_nd, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(u1_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(u1_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u1_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u1_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(u1_nd, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u1_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u1_nd, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(divmod(u1_nd, b_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(u1_nd, i_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(u1_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(i_py, u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(divmod(f_py, u1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u2_nd, b1_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u2_nd, i1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(u2_nd, i2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(u2_nd, i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(divmod(u2_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u2_nd, u1_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u2_nd, u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u2_nd, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u2_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u2_nd, f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(u2_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(u2_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u2_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u2_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(u2_nd, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u2_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u2_nd, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(divmod(u2_nd, b_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u2_nd, i_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(u2_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(i_py, u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(divmod(f_py, u2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u4_nd, b1_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, i1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u4_nd, i2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u4_nd, i4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u4_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u4_nd, u1_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, u2_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u4_nd, f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u4_nd, f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u4_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u4_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u4_nd, i_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(u4_nd, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u4_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u4_nd, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(divmod(u4_nd, b_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, i_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(u4_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(i_py, u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(divmod(f_py, u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u8_nd, b1_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, i1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, i2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, u1_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, u2_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, u4_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(u8_nd, i_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u8_nd, u_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u8_nd, iu_nd), tuple[_nt.Array[np.uint64 | np.float64], _nt.Array[np.uint64 | np.float64]])

assert_type(divmod(u8_nd, b_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, i_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u8_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(i_py, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(f_py, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f2_nd, b1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, i1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, i2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f2_nd, i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f2_nd, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f2_nd, u1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, u2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f2_nd, u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f2_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f2_nd, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f2_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f2_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f2_nd, i_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f2_nd, u_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f2_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f2_nd, iu_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(divmod(f2_nd, b_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, i_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f2_nd, f_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
divmod(f2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(i_py, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(divmod(f_py, f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
divmod(c_py, f2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f4_nd, b1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, i1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, i2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f4_nd, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f4_nd, u1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, u2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f4_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f4_nd, f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f4_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f4_nd, i_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f4_nd, u_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f4_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f4_nd, iu_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(divmod(f4_nd, b_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, i_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f4_nd, f_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
divmod(f4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(i_py, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(divmod(f_py, f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
divmod(c_py, f4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f8_nd, b1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, i1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, i2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, u1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, u2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f8_nd, i_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, u_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f8_nd, iu_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])

assert_type(divmod(f8_nd, b_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, i_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f8_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(f8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i_py, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(f_py, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, f8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(fld_nd, b1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, i1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, i2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, i4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, i8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, u1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, u2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, u4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, u8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, f2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, f4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, f8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(fld_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fld_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(fld_nd, i_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, u_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, f_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, iu_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])

assert_type(divmod(fld_nd, b_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, i_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(fld_nd, f_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(fld_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(i_py, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(divmod(f_py, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(c_py, fld_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c16_nd, b1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, u1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, u2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, u4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, u8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, f2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, f4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, f8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, fld_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, u_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, f_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, iu_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(c16_nd, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, i_py)  # 🐴  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, f_py)  # 🐴  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c16_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(b_py, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i_py, c16_nd)  # 🐴  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f_py, c16_nd)  # 🐴  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c_py, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(m8_nd, b1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, i1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, i2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, i4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, i8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, u1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, u2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, u4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, u8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, f2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, f4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, f8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, fld_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(m8_nd, m8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.timedelta64]])
divmod(m8_nd, i_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, u_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, f_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, iu_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(m8_nd, b_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, i_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, f_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(m8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

divmod(b_py, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i_py, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f_py, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(c_py, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(i_nd, b1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, i1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, i2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, i4_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i_nd, u1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, u2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(divmod(i_nd, u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i_nd, f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(i_nd, f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(i_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(i_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(i_nd, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    divmod(i_nd, u_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(i_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    divmod(i_nd, iu_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(divmod(i_nd, b_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, i_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(i_py, i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(divmod(f_py, i_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(u_nd, b1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(
    divmod(u_nd, i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    divmod(u_nd, i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    divmod(u_nd, i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(u_nd, i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(divmod(u_nd, u1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, u2_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, u4_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(divmod(u_nd, f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u_nd, f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(u_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(
    divmod(u_nd, i_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(u_nd, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(u_nd, iu_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])

assert_type(divmod(u_nd, b_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, i_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(u_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(i_py, u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(divmod(f_py, u_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(f_nd, b1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, i1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, i2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, i4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, i8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, u1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, u2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, u4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, u8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, f8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(divmod(f_nd, i_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, u_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, iu_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(divmod(f_nd, b_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, i_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_nd, f_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
divmod(f_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(i_py, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(f_py, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
divmod(c_py, f_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(iu_nd, b1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(
    divmod(iu_nd, i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    divmod(iu_nd, i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    divmod(iu_nd, i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(iu_nd, i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(divmod(iu_nd, u1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(iu_nd, u2_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(iu_nd, u4_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(iu_nd, u8_nd), tuple[_nt.Array[np.uint64 | np.float64], _nt.Array[np.uint64 | np.float64]])
assert_type(divmod(iu_nd, f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(iu_nd, f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(iu_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(divmod(iu_nd, fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(iu_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iu_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(
    divmod(iu_nd, i_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(divmod(iu_nd, u_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])
assert_type(divmod(iu_nd, f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(divmod(iu_nd, iu_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])

assert_type(divmod(iu_nd, b_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(iu_nd, i_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(iu_nd, f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(iu_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(divmod(b_py, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(i_py, iu_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(divmod(f_py, iu_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, iu_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
