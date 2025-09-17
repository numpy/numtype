# @generated 2025-09-17T05:36:51Z with tool/testgen.py
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

assert_type(b1_nd.__divmod__(b1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(b1_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(b1_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(b1_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(b1_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(b1_nd.__divmod__(u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(b1_nd.__divmod__(u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(b1_nd.__divmod__(u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(b1_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(b1_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(b1_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(b1_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(b1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(b1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(b1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(b1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(u_nd.__rdivmod__(b1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(f_nd.__rdivmod__(b1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(b1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(b1_nd.__divmod__(b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(b1_nd.__divmod__(i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(b1_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(b1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(b1_nd.__rdivmod__(b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(b1_nd.__rdivmod__(i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(b1_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, b1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i1_nd.__divmod__(b1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i1_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i1_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i1_nd.__divmod__(u1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i1_nd.__divmod__(u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i1_nd.__divmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i1_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i1_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(i1_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(i1_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(i1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(i1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    u_nd.__rdivmod__(i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(f_nd.__rdivmod__(i1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    iu_nd.__rdivmod__(i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(i1_nd.__divmod__(b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__divmod__(i_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i1_nd.__rdivmod__(b_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__rdivmod__(i_py), tuple[_nt.Array[np.int8], _nt.Array[np.int8]])
assert_type(i1_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i2_nd.__divmod__(b1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i2_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i2_nd.__divmod__(u1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i2_nd.__divmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i2_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i2_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(i2_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(i2_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(i2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(i2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    u_nd.__rdivmod__(i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(f_nd.__rdivmod__(i2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    iu_nd.__rdivmod__(i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(i2_nd.__divmod__(b_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(i_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i2_nd.__rdivmod__(b_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__rdivmod__(i_py), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(i2_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i4_nd.__divmod__(b1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i4_nd.__divmod__(u1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(u2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i4_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i4_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i4_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i4_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(i4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(i4_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    u_nd.__rdivmod__(i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(f_nd.__rdivmod__(i4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    iu_nd.__rdivmod__(i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(i4_nd.__divmod__(b_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(i_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i4_nd.__rdivmod__(b_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__rdivmod__(i_py), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(i4_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i8_nd.__divmod__(b1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(u1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(u2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i8_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i8_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i8_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(i8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u_nd.__rdivmod__(i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(f_nd.__rdivmod__(i8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])

assert_type(i8_nd.__divmod__(b_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i8_nd.__rdivmod__(b_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__rdivmod__(i_py), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i8_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u1_nd.__divmod__(b1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(u1_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int16], _nt.Array[np.int16]])
assert_type(u1_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(u1_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u1_nd.__divmod__(u1_nd), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__divmod__(u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u1_nd.__divmod__(u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u1_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u1_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(u1_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(u1_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(u1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u1_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u1_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(u1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(u_nd.__rdivmod__(u1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(f_nd.__rdivmod__(u1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(u1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(u1_nd.__divmod__(b_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__divmod__(i_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u1_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u1_nd.__rdivmod__(b_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__rdivmod__(i_py), tuple[_nt.Array[np.uint8], _nt.Array[np.uint8]])
assert_type(u1_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u1_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u2_nd.__divmod__(b1_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(u2_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(u2_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int32], _nt.Array[np.int32]])
assert_type(u2_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u2_nd.__divmod__(u1_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__divmod__(u2_nd), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__divmod__(u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u2_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u2_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(u2_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(u2_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(u2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(u2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(u_nd.__rdivmod__(u2_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(f_nd.__rdivmod__(u2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(u2_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(u2_nd.__divmod__(b_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__divmod__(i_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u2_nd.__rdivmod__(b_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__rdivmod__(i_py), tuple[_nt.Array[np.uint16], _nt.Array[np.uint16]])
assert_type(u2_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u4_nd.__divmod__(b1_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(i1_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u4_nd.__divmod__(i2_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u4_nd.__divmod__(i4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u4_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u4_nd.__divmod__(u1_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(u2_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(u4_nd), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u4_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u4_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u4_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(u4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(u_nd.__rdivmod__(u4_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(f_nd.__rdivmod__(u4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(u4_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])

assert_type(u4_nd.__divmod__(b_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(i_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u4_nd.__rdivmod__(b_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__rdivmod__(i_py), tuple[_nt.Array[np.uint32], _nt.Array[np.uint32]])
assert_type(u4_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u8_nd.__divmod__(b1_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(i1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(i2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(u1_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(u2_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(u4_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u8_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(u8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u_nd.__rdivmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(f_nd.__rdivmod__(u8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(u8_nd), tuple[_nt.Array[np.uint64 | np.float64], _nt.Array[np.uint64 | np.float64]])

assert_type(u8_nd.__divmod__(b_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(i_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u8_nd.__rdivmod__(b_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__rdivmod__(i_py), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u8_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f2_nd.__divmod__(b1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(i1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(i2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f2_nd.__divmod__(i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f2_nd.__divmod__(i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f2_nd.__divmod__(u1_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(u2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f2_nd.__divmod__(u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f2_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f2_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f2_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(f2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f2_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f2_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(u_nd.__rdivmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__rdivmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(f2_nd.__divmod__(b_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(i_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__divmod__(f_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
divmod(f2_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f2_nd.__rdivmod__(b_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__rdivmod__(i_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
assert_type(f2_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float16], _nt.Array[np.float16]])
divmod(c_py, f2_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f4_nd.__divmod__(b1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(i1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(i2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f4_nd.__divmod__(i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f4_nd.__divmod__(u1_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(u2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f4_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f4_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(f4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f4_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f4_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(u_nd.__rdivmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__rdivmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(f4_nd.__divmod__(b_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(i_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__divmod__(f_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
divmod(f4_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f4_nd.__rdivmod__(b_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__rdivmod__(i_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
assert_type(f4_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float32], _nt.Array[np.float32]])
divmod(c_py, f4_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f8_nd.__divmod__(b1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(i1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(i2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(i4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(u1_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(u2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(u4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(f2_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(f4_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(f8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f8_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f8_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__rdivmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(u_nd.__rdivmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f_nd.__rdivmod__(f8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])

assert_type(f8_nd.__divmod__(b_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(i_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(f8_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f8_nd.__rdivmod__(b_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__rdivmod__(i_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(f8_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, f8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(fld_nd.__divmod__(b1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(i1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(i2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(i4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(i8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(u1_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(u2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(u4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(u8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(f2_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(f4_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(f8_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(fld_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(fld_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(fld_nd.__divmod__(i_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(u_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(f_nd.__rdivmod__(fld_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(iu_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])

assert_type(fld_nd.__divmod__(b_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(i_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__divmod__(f_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(fld_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(fld_nd.__rdivmod__(b_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__rdivmod__(i_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
assert_type(fld_nd.__rdivmod__(f_py), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
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
assert_type(m8_nd.__divmod__(m8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.timedelta64]])
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

assert_type(i_nd.__divmod__(b1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(i1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(i2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(i4_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i_nd.__divmod__(u1_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(u2_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(u4_nd), tuple[_nt.Array[np.int64], _nt.Array[np.int64]])
assert_type(i_nd.__divmod__(u8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(i_nd.__divmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(i_nd.__divmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(i_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(i_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(i_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(i_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(i_nd.__divmod__(i_nd), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(
    i_nd.__divmod__(u_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(f_nd.__rdivmod__(i_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(
    iu_nd.__rdivmod__(i_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)

assert_type(i_nd.__divmod__(b_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(i_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(i_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(i_nd.__rdivmod__(b_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__rdivmod__(i_py), tuple[_nt.Array[np.signedinteger], _nt.Array[np.signedinteger]])
assert_type(i_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, i_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u_nd.__divmod__(b1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(
    u_nd.__divmod__(i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    u_nd.__divmod__(i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    u_nd.__divmod__(i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(u_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(u_nd.__divmod__(u1_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__divmod__(u2_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__divmod__(u4_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64], _nt.Array[np.uint64]])
assert_type(u_nd.__divmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(u_nd.__divmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(u_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(u_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(u_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(u_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(
    u_nd.__divmod__(i_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(u_nd.__divmod__(u_nd), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(f_nd.__rdivmod__(u_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__rdivmod__(u_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])

assert_type(u_nd.__divmod__(b_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__divmod__(i_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(u_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(u_nd.__rdivmod__(b_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__rdivmod__(i_py), tuple[_nt.Array[np.unsignedinteger], _nt.Array[np.unsignedinteger]])
assert_type(u_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, u_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f_nd.__divmod__(b1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(i1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(i2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(i4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(i8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(u1_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(u2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(u4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(u8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(f8_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(fld_nd.__rdivmod__(f_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(f_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(f_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(f_nd.__divmod__(i_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(u_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(f_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(iu_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])

assert_type(f_nd.__divmod__(b_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(i_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__divmod__(f_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
divmod(f_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(f_nd.__rdivmod__(b_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__rdivmod__(i_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(f_nd.__rdivmod__(f_py), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
divmod(c_py, f_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(iu_nd.__divmod__(b1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(
    iu_nd.__divmod__(i1_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    iu_nd.__divmod__(i2_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(
    iu_nd.__divmod__(i4_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(iu_nd.__divmod__(i8_nd), tuple[_nt.Array[np.int64 | np.float64], _nt.Array[np.int64 | np.float64]])
assert_type(iu_nd.__divmod__(u1_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__divmod__(u2_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__divmod__(u4_nd), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__divmod__(u8_nd), tuple[_nt.Array[np.uint64 | np.float64], _nt.Array[np.uint64 | np.float64]])
assert_type(iu_nd.__divmod__(f2_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__divmod__(f4_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__divmod__(f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(fld_nd.__rdivmod__(iu_nd), tuple[_nt.Array[np.longdouble], _nt.Array[np.longdouble]])
divmod(iu_nd, c16_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
divmod(iu_nd, m8_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
assert_type(
    i_nd.__rdivmod__(iu_nd), tuple[_nt.Array[np.signedinteger | np.float64], _nt.Array[np.signedinteger | np.float64]]
)
assert_type(iu_nd.__divmod__(u_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])
assert_type(f_nd.__rdivmod__(iu_nd), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(iu_nd.__divmod__(iu_nd), tuple[_nt.Array[np.integer | np.float64], _nt.Array[np.integer | np.float64]])

assert_type(iu_nd.__divmod__(b_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__divmod__(i_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__divmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(iu_nd, c_py)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]

assert_type(iu_nd.__rdivmod__(b_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__rdivmod__(i_py), tuple[_nt.Array[np.integer], _nt.Array[np.integer]])
assert_type(iu_nd.__rdivmod__(f_py), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
divmod(c_py, iu_nd)  # type: ignore[operator]  # pyright: ignore[reportArgumentType, reportCallIssue]
