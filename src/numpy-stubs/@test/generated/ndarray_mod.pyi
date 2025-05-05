# @generated 2025-05-05T19:48:41Z with tool/testgen.py
from typing import assert_type

import _numtype as _nt
import numpy as np
import numpy.typing as npt

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
O_nd: _nt.Array[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
f_nd: npt.NDArray[np.floating]
iu_nd: npt.NDArray[np.integer]

b_py: bool
i_py: int
f_py: float
c_py: complex

###

assert_type(b1_nd % b1_nd, _nt.Array[np.int8])
assert_type(b1_nd % i1_nd, _nt.Array[np.int8])
assert_type(b1_nd % i2_nd, _nt.Array[np.int16])
assert_type(b1_nd % i4_nd, _nt.Array[np.int32])
assert_type(b1_nd % i8_nd, _nt.Array[np.int64])
assert_type(b1_nd % u1_nd, _nt.Array[np.uint8])
assert_type(b1_nd % u2_nd, _nt.Array[np.uint16])
assert_type(b1_nd % u4_nd, _nt.Array[np.uint32])
assert_type(b1_nd % u8_nd, _nt.Array[np.uint64])
assert_type(b1_nd % f2_nd, _nt.Array[np.float16])
assert_type(b1_nd % f4_nd, _nt.Array[np.float32])
assert_type(b1_nd % f8_nd, _nt.Array[np.float64])
assert_type(b1_nd % fld_nd, _nt.Array[np.longdouble])
b1_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1_nd % O_nd, _nt.Array[np.object_])
assert_type(b1_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(b1_nd % u_nd, _nt.Array[np.unsignedinteger])
assert_type(b1_nd % f_nd, _nt.Array[np.floating])
assert_type(b1_nd % iu_nd, _nt.Array[np.integer])

assert_type(b1_nd % b_py, _nt.Array[np.int8])
assert_type(b1_nd % i_py, _nt.Array[np.int64])
assert_type(b1_nd % f_py, _nt.Array[np.float64])
b1_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % b1_nd, _nt.Array[np.int8])
assert_type(i_py % b1_nd, _nt.Array[np.int64])
assert_type(f_py % b1_nd, _nt.Array[np.float64])
c_py % b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1_nd % b1_nd, _nt.Array[np.int8])
assert_type(i1_nd % i1_nd, _nt.Array[np.int8])
assert_type(i1_nd % i2_nd, _nt.Array[np.int16])
assert_type(i1_nd % i4_nd, _nt.Array[np.int32])
assert_type(i1_nd % i8_nd, _nt.Array[np.int64])
assert_type(i1_nd % u1_nd, _nt.Array[np.int16])
assert_type(i1_nd % u2_nd, _nt.Array[np.int32])
assert_type(i1_nd % u4_nd, _nt.Array[np.int64])
assert_type(i1_nd % u8_nd, _nt.Array[np.float64])
assert_type(i1_nd % f2_nd, _nt.Array[np.float16])
assert_type(i1_nd % f4_nd, _nt.Array[np.float32])
assert_type(i1_nd % f8_nd, _nt.Array[np.float64])
assert_type(i1_nd % fld_nd, _nt.Array[np.longdouble])
i1_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1_nd % O_nd, _nt.Array[np.object_])
assert_type(i1_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(i1_nd % u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i1_nd % f_nd, _nt.Array[np.floating])
assert_type(i1_nd % iu_nd, _nt.Array[np.signedinteger | np.float64])

assert_type(i1_nd % b_py, _nt.Array[np.int8])
assert_type(i1_nd % i_py, _nt.Array[np.int8])
assert_type(i1_nd % f_py, _nt.Array[np.float64])
i1_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % i1_nd, _nt.Array[np.int8])
assert_type(i_py % i1_nd, _nt.Array[np.int8])
assert_type(f_py % i1_nd, _nt.Array[np.float64])
c_py % i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2_nd % b1_nd, _nt.Array[np.int16])
assert_type(i2_nd % i1_nd, _nt.Array[np.int16])
assert_type(i2_nd % i2_nd, _nt.Array[np.int16])
assert_type(i2_nd % i4_nd, _nt.Array[np.int32])
assert_type(i2_nd % i8_nd, _nt.Array[np.int64])
assert_type(i2_nd % u1_nd, _nt.Array[np.int16])
assert_type(i2_nd % u2_nd, _nt.Array[np.int32])
assert_type(i2_nd % u4_nd, _nt.Array[np.int64])
assert_type(i2_nd % u8_nd, _nt.Array[np.float64])
assert_type(i2_nd % f2_nd, _nt.Array[np.float32])
assert_type(i2_nd % f4_nd, _nt.Array[np.float32])
assert_type(i2_nd % f8_nd, _nt.Array[np.float64])
assert_type(i2_nd % fld_nd, _nt.Array[np.longdouble])
i2_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2_nd % O_nd, _nt.Array[np.object_])
assert_type(i2_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(i2_nd % u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i2_nd % f_nd, _nt.Array[np.floating])
assert_type(i2_nd % iu_nd, _nt.Array[np.signedinteger | np.float64])

assert_type(i2_nd % b_py, _nt.Array[np.int16])
assert_type(i2_nd % i_py, _nt.Array[np.int16])
assert_type(i2_nd % f_py, _nt.Array[np.float64])
i2_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % i2_nd, _nt.Array[np.int16])
assert_type(i_py % i2_nd, _nt.Array[np.int16])
assert_type(f_py % i2_nd, _nt.Array[np.float64])
c_py % i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4_nd % b1_nd, _nt.Array[np.int32])
assert_type(i4_nd % i1_nd, _nt.Array[np.int32])
assert_type(i4_nd % i2_nd, _nt.Array[np.int32])
assert_type(i4_nd % i4_nd, _nt.Array[np.int32])
assert_type(i4_nd % i8_nd, _nt.Array[np.int64])
assert_type(i4_nd % u1_nd, _nt.Array[np.int32])
assert_type(i4_nd % u2_nd, _nt.Array[np.int32])
assert_type(i4_nd % u4_nd, _nt.Array[np.int64])
assert_type(i4_nd % u8_nd, _nt.Array[np.float64])
assert_type(i4_nd % f2_nd, _nt.Array[np.float64])
assert_type(i4_nd % f4_nd, _nt.Array[np.float64])
assert_type(i4_nd % f8_nd, _nt.Array[np.float64])
assert_type(i4_nd % fld_nd, _nt.Array[np.longdouble])
i4_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4_nd % O_nd, _nt.Array[np.object_])
assert_type(i4_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(i4_nd % u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i4_nd % f_nd, _nt.Array[np.floating])
assert_type(i4_nd % iu_nd, _nt.Array[np.signedinteger | np.float64])

assert_type(i4_nd % b_py, _nt.Array[np.int32])
assert_type(i4_nd % i_py, _nt.Array[np.int32])
assert_type(i4_nd % f_py, _nt.Array[np.float64])
i4_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % i4_nd, _nt.Array[np.int32])
assert_type(i_py % i4_nd, _nt.Array[np.int32])
assert_type(f_py % i4_nd, _nt.Array[np.float64])
c_py % i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8_nd % b1_nd, _nt.Array[np.int64])
assert_type(i8_nd % i1_nd, _nt.Array[np.int64])
assert_type(i8_nd % i2_nd, _nt.Array[np.int64])
assert_type(i8_nd % i4_nd, _nt.Array[np.int64])
assert_type(i8_nd % i8_nd, _nt.Array[np.int64])
assert_type(i8_nd % u1_nd, _nt.Array[np.int64])
assert_type(i8_nd % u2_nd, _nt.Array[np.int64])
assert_type(i8_nd % u4_nd, _nt.Array[np.int64])
assert_type(i8_nd % u8_nd, _nt.Array[np.float64])
assert_type(i8_nd % f2_nd, _nt.Array[np.float64])
assert_type(i8_nd % f4_nd, _nt.Array[np.float64])
assert_type(i8_nd % f8_nd, _nt.Array[np.float64])
assert_type(i8_nd % fld_nd, _nt.Array[np.longdouble])
i8_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8_nd % O_nd, _nt.Array[np.object_])
assert_type(i8_nd % i_nd, _nt.Array[np.int64])
assert_type(i8_nd % u_nd, _nt.Array[np.int64 | np.float64])
assert_type(i8_nd % f_nd, _nt.Array[np.floating])
assert_type(i8_nd % iu_nd, _nt.Array[np.int64 | np.float64])

assert_type(i8_nd % b_py, _nt.Array[np.int64])
assert_type(i8_nd % i_py, _nt.Array[np.int64])
assert_type(i8_nd % f_py, _nt.Array[np.float64])
i8_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % i8_nd, _nt.Array[np.int64])
assert_type(i_py % i8_nd, _nt.Array[np.int64])
assert_type(f_py % i8_nd, _nt.Array[np.float64])
c_py % i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1_nd % b1_nd, _nt.Array[np.uint8])
assert_type(u1_nd % i1_nd, _nt.Array[np.int16])
assert_type(u1_nd % i2_nd, _nt.Array[np.int16])
assert_type(u1_nd % i4_nd, _nt.Array[np.int32])
assert_type(u1_nd % i8_nd, _nt.Array[np.int64])
assert_type(u1_nd % u1_nd, _nt.Array[np.uint8])
assert_type(u1_nd % u2_nd, _nt.Array[np.uint16])
assert_type(u1_nd % u4_nd, _nt.Array[np.uint32])
assert_type(u1_nd % u8_nd, _nt.Array[np.uint64])
assert_type(u1_nd % f2_nd, _nt.Array[np.float16])
assert_type(u1_nd % f4_nd, _nt.Array[np.float32])
assert_type(u1_nd % f8_nd, _nt.Array[np.float64])
assert_type(u1_nd % fld_nd, _nt.Array[np.longdouble])
u1_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u1_nd % O_nd, _nt.Array[np.object_])
assert_type(u1_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(u1_nd % u_nd, _nt.Array[np.unsignedinteger])
assert_type(u1_nd % f_nd, _nt.Array[np.floating])
assert_type(u1_nd % iu_nd, _nt.Array[np.integer])

assert_type(u1_nd % b_py, _nt.Array[np.uint8])
assert_type(u1_nd % i_py, _nt.Array[np.uint8])
assert_type(u1_nd % f_py, _nt.Array[np.float64])
u1_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % u1_nd, _nt.Array[np.uint8])
assert_type(i_py % u1_nd, _nt.Array[np.uint8])
assert_type(f_py % u1_nd, _nt.Array[np.float64])
c_py % u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2_nd % b1_nd, _nt.Array[np.uint16])
assert_type(u2_nd % i1_nd, _nt.Array[np.int32])
assert_type(u2_nd % i2_nd, _nt.Array[np.int32])
assert_type(u2_nd % i4_nd, _nt.Array[np.int32])
assert_type(u2_nd % i8_nd, _nt.Array[np.int64])
assert_type(u2_nd % u1_nd, _nt.Array[np.uint16])
assert_type(u2_nd % u2_nd, _nt.Array[np.uint16])
assert_type(u2_nd % u4_nd, _nt.Array[np.uint32])
assert_type(u2_nd % u8_nd, _nt.Array[np.uint64])
assert_type(u2_nd % f2_nd, _nt.Array[np.float32])
assert_type(u2_nd % f4_nd, _nt.Array[np.float32])
assert_type(u2_nd % f8_nd, _nt.Array[np.float64])
assert_type(u2_nd % fld_nd, _nt.Array[np.longdouble])
u2_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u2_nd % O_nd, _nt.Array[np.object_])
assert_type(u2_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(u2_nd % u_nd, _nt.Array[np.unsignedinteger])
assert_type(u2_nd % f_nd, _nt.Array[np.floating])
assert_type(u2_nd % iu_nd, _nt.Array[np.integer])

assert_type(u2_nd % b_py, _nt.Array[np.uint16])
assert_type(u2_nd % i_py, _nt.Array[np.uint16])
assert_type(u2_nd % f_py, _nt.Array[np.float64])
u2_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % u2_nd, _nt.Array[np.uint16])
assert_type(i_py % u2_nd, _nt.Array[np.uint16])
assert_type(f_py % u2_nd, _nt.Array[np.float64])
c_py % u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4_nd % b1_nd, _nt.Array[np.uint32])
assert_type(u4_nd % i1_nd, _nt.Array[np.int64])
assert_type(u4_nd % i2_nd, _nt.Array[np.int64])
assert_type(u4_nd % i4_nd, _nt.Array[np.int64])
assert_type(u4_nd % i8_nd, _nt.Array[np.int64])
assert_type(u4_nd % u1_nd, _nt.Array[np.uint32])
assert_type(u4_nd % u2_nd, _nt.Array[np.uint32])
assert_type(u4_nd % u4_nd, _nt.Array[np.uint32])
assert_type(u4_nd % u8_nd, _nt.Array[np.uint64])
assert_type(u4_nd % f2_nd, _nt.Array[np.float64])
assert_type(u4_nd % f4_nd, _nt.Array[np.float64])
assert_type(u4_nd % f8_nd, _nt.Array[np.float64])
assert_type(u4_nd % fld_nd, _nt.Array[np.longdouble])
u4_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u4_nd % O_nd, _nt.Array[np.object_])
assert_type(u4_nd % i_nd, _nt.Array[np.int64])
assert_type(u4_nd % u_nd, _nt.Array[np.unsignedinteger])
assert_type(u4_nd % f_nd, _nt.Array[np.floating])
assert_type(u4_nd % iu_nd, _nt.Array[np.integer])

assert_type(u4_nd % b_py, _nt.Array[np.uint32])
assert_type(u4_nd % i_py, _nt.Array[np.uint32])
assert_type(u4_nd % f_py, _nt.Array[np.float64])
u4_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % u4_nd, _nt.Array[np.uint32])
assert_type(i_py % u4_nd, _nt.Array[np.uint32])
assert_type(f_py % u4_nd, _nt.Array[np.float64])
c_py % u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8_nd % b1_nd, _nt.Array[np.uint64])
assert_type(u8_nd % i1_nd, _nt.Array[np.float64])
assert_type(u8_nd % i2_nd, _nt.Array[np.float64])
assert_type(u8_nd % i4_nd, _nt.Array[np.float64])
assert_type(u8_nd % i8_nd, _nt.Array[np.float64])
assert_type(u8_nd % u1_nd, _nt.Array[np.uint64])
assert_type(u8_nd % u2_nd, _nt.Array[np.uint64])
assert_type(u8_nd % u4_nd, _nt.Array[np.uint64])
assert_type(u8_nd % u8_nd, _nt.Array[np.uint64])
assert_type(u8_nd % f2_nd, _nt.Array[np.float64])
assert_type(u8_nd % f4_nd, _nt.Array[np.float64])
assert_type(u8_nd % f8_nd, _nt.Array[np.float64])
assert_type(u8_nd % fld_nd, _nt.Array[np.longdouble])
u8_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8_nd % O_nd, _nt.Array[np.object_])
assert_type(u8_nd % i_nd, _nt.Array[np.float64])
assert_type(u8_nd % u_nd, _nt.Array[np.uint64])
assert_type(u8_nd % f_nd, _nt.Array[np.floating])
assert_type(u8_nd % iu_nd, _nt.Array[np.uint64 | np.float64])

assert_type(u8_nd % b_py, _nt.Array[np.uint64])
assert_type(u8_nd % i_py, _nt.Array[np.uint64])
assert_type(u8_nd % f_py, _nt.Array[np.float64])
u8_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % u8_nd, _nt.Array[np.uint64])
assert_type(i_py % u8_nd, _nt.Array[np.uint64])
assert_type(f_py % u8_nd, _nt.Array[np.float64])
c_py % u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2_nd % b1_nd, _nt.Array[np.float16])
assert_type(f2_nd % i1_nd, _nt.Array[np.float16])
assert_type(f2_nd % i2_nd, _nt.Array[np.float32])
assert_type(f2_nd % i4_nd, _nt.Array[np.float64])
assert_type(f2_nd % i8_nd, _nt.Array[np.float64])
assert_type(f2_nd % u1_nd, _nt.Array[np.float16])
assert_type(f2_nd % u2_nd, _nt.Array[np.float32])
assert_type(f2_nd % u4_nd, _nt.Array[np.float64])
assert_type(f2_nd % u8_nd, _nt.Array[np.float64])
assert_type(f2_nd % f2_nd, _nt.Array[np.float16])
assert_type(f2_nd % f4_nd, _nt.Array[np.float32])
assert_type(f2_nd % f8_nd, _nt.Array[np.float64])
assert_type(f2_nd % fld_nd, _nt.Array[np.longdouble])
f2_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd % O_nd, _nt.Array[np.object_])
assert_type(f2_nd % i_nd, _nt.Array[np.floating])
assert_type(f2_nd % u_nd, _nt.Array[np.floating])
assert_type(f2_nd % f_nd, _nt.Array[np.floating])
assert_type(f2_nd % iu_nd, _nt.Array[np.floating])

assert_type(f2_nd % b_py, _nt.Array[np.float16])
assert_type(f2_nd % i_py, _nt.Array[np.float16])
assert_type(f2_nd % f_py, _nt.Array[np.float16])
f2_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % f2_nd, _nt.Array[np.float16])
assert_type(i_py % f2_nd, _nt.Array[np.float16])
assert_type(f_py % f2_nd, _nt.Array[np.float16])
c_py % f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4_nd % b1_nd, _nt.Array[np.float32])
assert_type(f4_nd % i1_nd, _nt.Array[np.float32])
assert_type(f4_nd % i2_nd, _nt.Array[np.float32])
assert_type(f4_nd % i4_nd, _nt.Array[np.float64])
assert_type(f4_nd % i8_nd, _nt.Array[np.float64])
assert_type(f4_nd % u1_nd, _nt.Array[np.float32])
assert_type(f4_nd % u2_nd, _nt.Array[np.float32])
assert_type(f4_nd % u4_nd, _nt.Array[np.float64])
assert_type(f4_nd % u8_nd, _nt.Array[np.float64])
assert_type(f4_nd % f2_nd, _nt.Array[np.float32])
assert_type(f4_nd % f4_nd, _nt.Array[np.float32])
assert_type(f4_nd % f8_nd, _nt.Array[np.float64])
assert_type(f4_nd % fld_nd, _nt.Array[np.longdouble])
f4_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd % O_nd, _nt.Array[np.object_])
assert_type(f4_nd % i_nd, _nt.Array[np.floating])
assert_type(f4_nd % u_nd, _nt.Array[np.floating])
assert_type(f4_nd % f_nd, _nt.Array[np.floating])
assert_type(f4_nd % iu_nd, _nt.Array[np.floating])

assert_type(f4_nd % b_py, _nt.Array[np.float32])
assert_type(f4_nd % i_py, _nt.Array[np.float32])
assert_type(f4_nd % f_py, _nt.Array[np.float32])
f4_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % f4_nd, _nt.Array[np.float32])
assert_type(i_py % f4_nd, _nt.Array[np.float32])
assert_type(f_py % f4_nd, _nt.Array[np.float32])
c_py % f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8_nd % b1_nd, _nt.Array[np.float64])
assert_type(f8_nd % i1_nd, _nt.Array[np.float64])
assert_type(f8_nd % i2_nd, _nt.Array[np.float64])
assert_type(f8_nd % i4_nd, _nt.Array[np.float64])
assert_type(f8_nd % i8_nd, _nt.Array[np.float64])
assert_type(f8_nd % u1_nd, _nt.Array[np.float64])
assert_type(f8_nd % u2_nd, _nt.Array[np.float64])
assert_type(f8_nd % u4_nd, _nt.Array[np.float64])
assert_type(f8_nd % u8_nd, _nt.Array[np.float64])
assert_type(f8_nd % f2_nd, _nt.Array[np.float64])
assert_type(f8_nd % f4_nd, _nt.Array[np.float64])
assert_type(f8_nd % f8_nd, _nt.Array[np.float64])
assert_type(f8_nd % fld_nd, _nt.Array[np.longdouble])
f8_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd % O_nd, _nt.Array[np.object_])
assert_type(f8_nd % i_nd, _nt.Array[np.float64])
assert_type(f8_nd % u_nd, _nt.Array[np.float64])
assert_type(f8_nd % f_nd, _nt.Array[np.floating])
assert_type(f8_nd % iu_nd, _nt.Array[np.float64])

assert_type(f8_nd % b_py, _nt.Array[np.float64])
assert_type(f8_nd % i_py, _nt.Array[np.float64])
assert_type(f8_nd % f_py, _nt.Array[np.float64])
f8_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % f8_nd, _nt.Array[np.float64])
assert_type(i_py % f8_nd, _nt.Array[np.float64])
assert_type(f_py % f8_nd, _nt.Array[np.float64])
c_py % f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(fld_nd % b1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % i1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % i2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % i4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % i8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % u1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % u2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % u4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % u8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % f2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % f4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % f8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % fld_nd, _nt.Array[np.longdouble])
fld_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd % O_nd, _nt.Array[np.object_])
assert_type(fld_nd % i_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % u_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % f_nd, _nt.Array[np.longdouble])
assert_type(fld_nd % iu_nd, _nt.Array[np.longdouble])

assert_type(fld_nd % b_py, _nt.Array[np.longdouble])
assert_type(fld_nd % i_py, _nt.Array[np.longdouble])
assert_type(fld_nd % f_py, _nt.Array[np.longdouble])
fld_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % fld_nd, _nt.Array[np.longdouble])
assert_type(i_py % fld_nd, _nt.Array[np.longdouble])
assert_type(f_py % fld_nd, _nt.Array[np.longdouble])
c_py % fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c16_nd % b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

c16_nd % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd % i_py  # 🐴  # pyright: ignore[reportOperatorIssue]
c16_nd % f_py  # 🐴  # pyright: ignore[reportOperatorIssue]
c16_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

b_py % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py % c16_nd  # 🐴  # pyright: ignore[reportOperatorIssue]
f_py % c16_nd  # 🐴  # pyright: ignore[reportOperatorIssue]
c_py % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m8_nd % b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd % m8_nd, _nt.Array[np.timedelta64])
m8_nd % i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

m8_nd % b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

b_py % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(O_nd % b1_nd, _nt.Array[np.object_])
assert_type(O_nd % i1_nd, _nt.Array[np.object_])
assert_type(O_nd % i2_nd, _nt.Array[np.object_])
assert_type(O_nd % i4_nd, _nt.Array[np.object_])
assert_type(O_nd % i8_nd, _nt.Array[np.object_])
assert_type(O_nd % u1_nd, _nt.Array[np.object_])
assert_type(O_nd % u2_nd, _nt.Array[np.object_])
assert_type(O_nd % u4_nd, _nt.Array[np.object_])
assert_type(O_nd % u8_nd, _nt.Array[np.object_])
assert_type(O_nd % f2_nd, _nt.Array[np.object_])
assert_type(O_nd % f4_nd, _nt.Array[np.object_])
assert_type(O_nd % f8_nd, _nt.Array[np.object_])
assert_type(O_nd % fld_nd, _nt.Array[np.object_])
assert_type(O_nd % O_nd, _nt.Array[np.object_])
assert_type(O_nd % i_nd, _nt.Array[np.object_])
assert_type(O_nd % u_nd, _nt.Array[np.object_])
assert_type(O_nd % f_nd, _nt.Array[np.object_])
assert_type(O_nd % iu_nd, _nt.Array[np.object_])

assert_type(O_nd % b_py, _nt.Array[np.object_])
assert_type(O_nd % i_py, _nt.Array[np.object_])
assert_type(O_nd % f_py, _nt.Array[np.object_])

###

assert_type(b_py % O_nd, _nt.Array[np.object_])
assert_type(i_py % O_nd, _nt.Array[np.object_])
assert_type(f_py % O_nd, _nt.Array[np.object_])

###

assert_type(i_nd % b1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % i1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % i2_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % i4_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % i8_nd, _nt.Array[np.int64])
assert_type(i_nd % u1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % u2_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % u4_nd, _nt.Array[np.int64])
assert_type(i_nd % u8_nd, _nt.Array[np.float64])
assert_type(i_nd % f2_nd, _nt.Array[np.floating])
assert_type(i_nd % f4_nd, _nt.Array[np.floating])
assert_type(i_nd % f8_nd, _nt.Array[np.float64])
assert_type(i_nd % fld_nd, _nt.Array[np.longdouble])
i_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i_nd % O_nd, _nt.Array[np.object_])
assert_type(i_nd % i_nd, _nt.Array[np.signedinteger])
assert_type(i_nd % u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i_nd % f_nd, _nt.Array[np.floating])
assert_type(i_nd % iu_nd, _nt.Array[np.signedinteger | np.float64])

assert_type(i_nd % b_py, _nt.Array[np.signedinteger])
assert_type(i_nd % i_py, _nt.Array[np.signedinteger])
assert_type(i_nd % f_py, _nt.Array[np.float64])
i_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % i_nd, _nt.Array[np.signedinteger])
assert_type(i_py % i_nd, _nt.Array[np.signedinteger])
assert_type(f_py % i_nd, _nt.Array[np.float64])
c_py % i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u_nd % b1_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd % i1_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd % i2_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd % i4_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd % i8_nd, _nt.Array[np.int64 | np.float64])
assert_type(u_nd % u1_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd % u2_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd % u4_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd % u8_nd, _nt.Array[np.uint64])
assert_type(u_nd % f2_nd, _nt.Array[np.floating])
assert_type(u_nd % f4_nd, _nt.Array[np.floating])
assert_type(u_nd % f8_nd, _nt.Array[np.float64])
assert_type(u_nd % fld_nd, _nt.Array[np.longdouble])
u_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u_nd % O_nd, _nt.Array[np.object_])
assert_type(u_nd % i_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd % u_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd % f_nd, _nt.Array[np.floating])
assert_type(u_nd % iu_nd, _nt.Array[np.integer | np.float64])

assert_type(u_nd % b_py, _nt.Array[np.unsignedinteger])
assert_type(u_nd % i_py, _nt.Array[np.unsignedinteger])
assert_type(u_nd % f_py, _nt.Array[np.float64])
u_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % u_nd, _nt.Array[np.unsignedinteger])
assert_type(i_py % u_nd, _nt.Array[np.unsignedinteger])
assert_type(f_py % u_nd, _nt.Array[np.float64])
c_py % u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f_nd % b1_nd, _nt.Array[np.floating])
assert_type(f_nd % i1_nd, _nt.Array[np.floating])
assert_type(f_nd % i2_nd, _nt.Array[np.floating])
assert_type(f_nd % i4_nd, _nt.Array[np.floating])
assert_type(f_nd % i8_nd, _nt.Array[np.floating])
assert_type(f_nd % u1_nd, _nt.Array[np.floating])
assert_type(f_nd % u2_nd, _nt.Array[np.floating])
assert_type(f_nd % u4_nd, _nt.Array[np.floating])
assert_type(f_nd % u8_nd, _nt.Array[np.floating])
assert_type(f_nd % f2_nd, _nt.Array[np.floating])
assert_type(f_nd % f4_nd, _nt.Array[np.floating])
assert_type(f_nd % f8_nd, _nt.Array[np.floating])
assert_type(f_nd % fld_nd, _nt.Array[np.longdouble])
f_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f_nd % O_nd, _nt.Array[np.object_])
assert_type(f_nd % i_nd, _nt.Array[np.floating])
assert_type(f_nd % u_nd, _nt.Array[np.floating])
assert_type(f_nd % f_nd, _nt.Array[np.floating])
assert_type(f_nd % iu_nd, _nt.Array[np.floating])

assert_type(f_nd % b_py, _nt.Array[np.floating])
assert_type(f_nd % i_py, _nt.Array[np.floating])
assert_type(f_nd % f_py, _nt.Array[np.floating])
f_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % f_nd, _nt.Array[np.floating])
assert_type(i_py % f_nd, _nt.Array[np.floating])
assert_type(f_py % f_nd, _nt.Array[np.floating])
c_py % f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu_nd % b1_nd, _nt.Array[np.integer])
assert_type(iu_nd % i1_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd % i2_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd % i4_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd % i8_nd, _nt.Array[np.int64 | np.float64])
assert_type(iu_nd % u1_nd, _nt.Array[np.integer])
assert_type(iu_nd % u2_nd, _nt.Array[np.integer])
assert_type(iu_nd % u4_nd, _nt.Array[np.integer])
assert_type(iu_nd % u8_nd, _nt.Array[np.uint64 | np.float64])
assert_type(iu_nd % f2_nd, _nt.Array[np.floating])
assert_type(iu_nd % f4_nd, _nt.Array[np.floating])
assert_type(iu_nd % f8_nd, _nt.Array[np.float64])
assert_type(iu_nd % fld_nd, _nt.Array[np.longdouble])
iu_nd % c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd % m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu_nd % O_nd, _nt.Array[np.object_])
assert_type(iu_nd % i_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd % u_nd, _nt.Array[np.integer | np.float64])
assert_type(iu_nd % f_nd, _nt.Array[np.floating])
assert_type(iu_nd % iu_nd, _nt.Array[np.integer | np.float64])

assert_type(iu_nd % b_py, _nt.Array[np.integer])
assert_type(iu_nd % i_py, _nt.Array[np.integer])
assert_type(iu_nd % f_py, _nt.Array[np.float64])
iu_nd % c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py % iu_nd, _nt.Array[np.integer])
assert_type(i_py % iu_nd, _nt.Array[np.integer])
assert_type(f_py % iu_nd, _nt.Array[np.float64])
c_py % iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
