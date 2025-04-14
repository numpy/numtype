# @generated 2025-04-14T02:39:22Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

i1_nd: npt.NDArray[np.int8]
i2_nd: npt.NDArray[np.int16]
i4_nd: npt.NDArray[np.int32]
i8_nd: npt.NDArray[np.int64]
u1_nd: npt.NDArray[np.uint8]
u2_nd: npt.NDArray[np.uint16]
u4_nd: npt.NDArray[np.uint32]
u8_nd: npt.NDArray[np.uint64]
f2_nd: npt.NDArray[np.float16]
f4_nd: npt.NDArray[np.float32]
f8_nd: npt.NDArray[np.float64]
fld_nd: npt.NDArray[np.longdouble]
c8_nd: npt.NDArray[np.complex64]
c16_nd: npt.NDArray[np.complex128]
cld_nd: npt.NDArray[np.clongdouble]
M8_nd: npt.NDArray[np.datetime64]
m8_nd: npt.NDArray[np.timedelta64]
O_nd: npt.NDArray[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
f_nd: npt.NDArray[np.floating]
c_nd: npt.NDArray[np.complexfloating]
iu_nd: npt.NDArray[np.integer]
fc_nd: npt.NDArray[np.inexact]
iufc_nd: npt.NDArray[np.number]

i_py: int
f_py: float
c_py: complex

###

assert_type(i1_nd - i1_nd, npt.NDArray[np.int8])
assert_type(i1_nd - i2_nd, npt.NDArray[np.int16])
assert_type(i1_nd - i4_nd, npt.NDArray[np.int32])
assert_type(i1_nd - i8_nd, npt.NDArray[np.int64])
assert_type(i1_nd - u1_nd, npt.NDArray[np.int16])
assert_type(i1_nd - u2_nd, npt.NDArray[np.int32])
assert_type(i1_nd - u4_nd, npt.NDArray[np.int64])
assert_type(i1_nd - u8_nd, npt.NDArray[np.float64])
assert_type(i1_nd - f2_nd, npt.NDArray[np.float16])
assert_type(i1_nd - f4_nd, npt.NDArray[np.float32])
assert_type(i1_nd - f8_nd, npt.NDArray[np.float64])
assert_type(i1_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(i1_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(i1_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(i1_nd - cld_nd, npt.NDArray[np.clongdouble])
i1_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(i1_nd - O_nd, npt.NDArray[np.object_])
assert_type(i1_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(i1_nd - u_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i1_nd - f_nd, npt.NDArray[np.floating])
assert_type(i1_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(i1_nd - iu_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i1_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(i1_nd - iufc_nd, npt.NDArray[np.number])

assert_type(i1_nd - i_py, npt.NDArray[np.int8])
assert_type(i1_nd - f_py, npt.NDArray[np.float64])
assert_type(i1_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - i1_nd, npt.NDArray[np.int8])
assert_type(f_py - i1_nd, npt.NDArray[np.float64])
assert_type(c_py - i1_nd, npt.NDArray[np.complex128])

assert_type(i2_nd - i1_nd, npt.NDArray[np.int16])
assert_type(i2_nd - i2_nd, npt.NDArray[np.int16])
assert_type(i2_nd - i4_nd, npt.NDArray[np.int32])
assert_type(i2_nd - i8_nd, npt.NDArray[np.int64])
assert_type(i2_nd - u1_nd, npt.NDArray[np.int16])
assert_type(i2_nd - u2_nd, npt.NDArray[np.int32])
assert_type(i2_nd - u4_nd, npt.NDArray[np.int64])
assert_type(i2_nd - u8_nd, npt.NDArray[np.float64])
assert_type(i2_nd - f2_nd, npt.NDArray[np.float32])
assert_type(i2_nd - f4_nd, npt.NDArray[np.float32])
assert_type(i2_nd - f8_nd, npt.NDArray[np.float64])
assert_type(i2_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(i2_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(i2_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(i2_nd - cld_nd, npt.NDArray[np.clongdouble])
i2_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(i2_nd - O_nd, npt.NDArray[np.object_])
assert_type(i2_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(i2_nd - u_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i2_nd - f_nd, npt.NDArray[np.floating])
assert_type(i2_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(i2_nd - iu_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i2_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(i2_nd - iufc_nd, npt.NDArray[np.number])

assert_type(i2_nd - i_py, npt.NDArray[np.int16])
assert_type(i2_nd - f_py, npt.NDArray[np.float64])
assert_type(i2_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - i2_nd, npt.NDArray[np.int16])
assert_type(f_py - i2_nd, npt.NDArray[np.float64])
assert_type(c_py - i2_nd, npt.NDArray[np.complex128])

assert_type(i4_nd - i1_nd, npt.NDArray[np.int32])
assert_type(i4_nd - i2_nd, npt.NDArray[np.int32])
assert_type(i4_nd - i4_nd, npt.NDArray[np.int32])
assert_type(i4_nd - i8_nd, npt.NDArray[np.int64])
assert_type(i4_nd - u1_nd, npt.NDArray[np.int32])
assert_type(i4_nd - u2_nd, npt.NDArray[np.int32])
assert_type(i4_nd - u4_nd, npt.NDArray[np.int64])
assert_type(i4_nd - u8_nd, npt.NDArray[np.float64])
assert_type(i4_nd - f2_nd, npt.NDArray[np.float64])
assert_type(i4_nd - f4_nd, npt.NDArray[np.float64])
assert_type(i4_nd - f8_nd, npt.NDArray[np.float64])
assert_type(i4_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(i4_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(i4_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(i4_nd - cld_nd, npt.NDArray[np.clongdouble])
i4_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(i4_nd - O_nd, npt.NDArray[np.object_])
assert_type(i4_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(i4_nd - u_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i4_nd - f_nd, npt.NDArray[np.floating])
assert_type(i4_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(i4_nd - iu_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i4_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(i4_nd - iufc_nd, npt.NDArray[np.number])

assert_type(i4_nd - i_py, npt.NDArray[np.int32])
assert_type(i4_nd - f_py, npt.NDArray[np.float64])
assert_type(i4_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - i4_nd, npt.NDArray[np.int32])
assert_type(f_py - i4_nd, npt.NDArray[np.float64])
assert_type(c_py - i4_nd, npt.NDArray[np.complex128])

assert_type(i8_nd - i1_nd, npt.NDArray[np.int64])
assert_type(i8_nd - i2_nd, npt.NDArray[np.int64])
assert_type(i8_nd - i4_nd, npt.NDArray[np.int64])
assert_type(i8_nd - i8_nd, npt.NDArray[np.int64])
assert_type(i8_nd - u1_nd, npt.NDArray[np.int64])
assert_type(i8_nd - u2_nd, npt.NDArray[np.int64])
assert_type(i8_nd - u4_nd, npt.NDArray[np.int64])
assert_type(i8_nd - u8_nd, npt.NDArray[np.float64])
assert_type(i8_nd - f2_nd, npt.NDArray[np.float64])
assert_type(i8_nd - f4_nd, npt.NDArray[np.float64])
assert_type(i8_nd - f8_nd, npt.NDArray[np.float64])
assert_type(i8_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(i8_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(i8_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(i8_nd - cld_nd, npt.NDArray[np.clongdouble])
i8_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(i8_nd - O_nd, npt.NDArray[np.object_])
assert_type(i8_nd - i_nd, npt.NDArray[np.int64])
assert_type(i8_nd - u_nd, npt.NDArray[np.int64 | np.float64])
assert_type(i8_nd - f_nd, npt.NDArray[np.floating])
assert_type(i8_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(i8_nd - iu_nd, npt.NDArray[np.int64 | np.float64])
assert_type(i8_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(i8_nd - iufc_nd, npt.NDArray[np.number])

assert_type(i8_nd - i_py, npt.NDArray[np.int64])
assert_type(i8_nd - f_py, npt.NDArray[np.float64])
assert_type(i8_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - i8_nd, npt.NDArray[np.int64])
assert_type(f_py - i8_nd, npt.NDArray[np.float64])
assert_type(c_py - i8_nd, npt.NDArray[np.complex128])

assert_type(u1_nd - i1_nd, npt.NDArray[np.int16])
assert_type(u1_nd - i2_nd, npt.NDArray[np.int16])
assert_type(u1_nd - i4_nd, npt.NDArray[np.int32])
assert_type(u1_nd - i8_nd, npt.NDArray[np.int64])
assert_type(u1_nd - u1_nd, npt.NDArray[np.uint8])
assert_type(u1_nd - u2_nd, npt.NDArray[np.uint16])
assert_type(u1_nd - u4_nd, npt.NDArray[np.uint32])
assert_type(u1_nd - u8_nd, npt.NDArray[np.uint64])
assert_type(u1_nd - f2_nd, npt.NDArray[np.float16])
assert_type(u1_nd - f4_nd, npt.NDArray[np.float32])
assert_type(u1_nd - f8_nd, npt.NDArray[np.float64])
assert_type(u1_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(u1_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(u1_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(u1_nd - cld_nd, npt.NDArray[np.clongdouble])
u1_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u1_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(u1_nd - O_nd, npt.NDArray[np.object_])
assert_type(u1_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(u1_nd - u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u1_nd - f_nd, npt.NDArray[np.floating])
assert_type(u1_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(u1_nd - iu_nd, npt.NDArray[np.integer])
assert_type(u1_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(u1_nd - iufc_nd, npt.NDArray[np.number])

assert_type(u1_nd - i_py, npt.NDArray[np.uint8])
assert_type(u1_nd - f_py, npt.NDArray[np.float64])
assert_type(u1_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - u1_nd, npt.NDArray[np.uint8])
assert_type(f_py - u1_nd, npt.NDArray[np.float64])
assert_type(c_py - u1_nd, npt.NDArray[np.complex128])

assert_type(u2_nd - i1_nd, npt.NDArray[np.int32])
assert_type(u2_nd - i2_nd, npt.NDArray[np.int32])
assert_type(u2_nd - i4_nd, npt.NDArray[np.int32])
assert_type(u2_nd - i8_nd, npt.NDArray[np.int64])
assert_type(u2_nd - u1_nd, npt.NDArray[np.uint16])
assert_type(u2_nd - u2_nd, npt.NDArray[np.uint16])
assert_type(u2_nd - u4_nd, npt.NDArray[np.uint32])
assert_type(u2_nd - u8_nd, npt.NDArray[np.uint64])
assert_type(u2_nd - f2_nd, npt.NDArray[np.float32])
assert_type(u2_nd - f4_nd, npt.NDArray[np.float32])
assert_type(u2_nd - f8_nd, npt.NDArray[np.float64])
assert_type(u2_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(u2_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(u2_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(u2_nd - cld_nd, npt.NDArray[np.clongdouble])
u2_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u2_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(u2_nd - O_nd, npt.NDArray[np.object_])
assert_type(u2_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(u2_nd - u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u2_nd - f_nd, npt.NDArray[np.floating])
assert_type(u2_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(u2_nd - iu_nd, npt.NDArray[np.integer])
assert_type(u2_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(u2_nd - iufc_nd, npt.NDArray[np.number])

assert_type(u2_nd - i_py, npt.NDArray[np.uint16])
assert_type(u2_nd - f_py, npt.NDArray[np.float64])
assert_type(u2_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - u2_nd, npt.NDArray[np.uint16])
assert_type(f_py - u2_nd, npt.NDArray[np.float64])
assert_type(c_py - u2_nd, npt.NDArray[np.complex128])

assert_type(u4_nd - i1_nd, npt.NDArray[np.int64])
assert_type(u4_nd - i2_nd, npt.NDArray[np.int64])
assert_type(u4_nd - i4_nd, npt.NDArray[np.int64])
assert_type(u4_nd - i8_nd, npt.NDArray[np.int64])
assert_type(u4_nd - u1_nd, npt.NDArray[np.uint32])
assert_type(u4_nd - u2_nd, npt.NDArray[np.uint32])
assert_type(u4_nd - u4_nd, npt.NDArray[np.uint32])
assert_type(u4_nd - u8_nd, npt.NDArray[np.uint64])
assert_type(u4_nd - f2_nd, npt.NDArray[np.float64])
assert_type(u4_nd - f4_nd, npt.NDArray[np.float64])
assert_type(u4_nd - f8_nd, npt.NDArray[np.float64])
assert_type(u4_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(u4_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(u4_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(u4_nd - cld_nd, npt.NDArray[np.clongdouble])
u4_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u4_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(u4_nd - O_nd, npt.NDArray[np.object_])
assert_type(u4_nd - i_nd, npt.NDArray[np.int64])
assert_type(u4_nd - u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u4_nd - f_nd, npt.NDArray[np.floating])
assert_type(u4_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(u4_nd - iu_nd, npt.NDArray[np.integer])
assert_type(u4_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(u4_nd - iufc_nd, npt.NDArray[np.number])

assert_type(u4_nd - i_py, npt.NDArray[np.uint32])
assert_type(u4_nd - f_py, npt.NDArray[np.float64])
assert_type(u4_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - u4_nd, npt.NDArray[np.uint32])
assert_type(f_py - u4_nd, npt.NDArray[np.float64])
assert_type(c_py - u4_nd, npt.NDArray[np.complex128])

assert_type(u8_nd - i1_nd, npt.NDArray[np.float64])
assert_type(u8_nd - i2_nd, npt.NDArray[np.float64])
assert_type(u8_nd - i4_nd, npt.NDArray[np.float64])
assert_type(u8_nd - i8_nd, npt.NDArray[np.float64])
assert_type(u8_nd - u1_nd, npt.NDArray[np.uint64])
assert_type(u8_nd - u2_nd, npt.NDArray[np.uint64])
assert_type(u8_nd - u4_nd, npt.NDArray[np.uint64])
assert_type(u8_nd - u8_nd, npt.NDArray[np.uint64])
assert_type(u8_nd - f2_nd, npt.NDArray[np.float64])
assert_type(u8_nd - f4_nd, npt.NDArray[np.float64])
assert_type(u8_nd - f8_nd, npt.NDArray[np.float64])
assert_type(u8_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(u8_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(u8_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(u8_nd - cld_nd, npt.NDArray[np.clongdouble])
u8_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(u8_nd - O_nd, npt.NDArray[np.object_])
assert_type(u8_nd - i_nd, npt.NDArray[np.float64])
assert_type(u8_nd - u_nd, npt.NDArray[np.uint64])
assert_type(u8_nd - f_nd, npt.NDArray[np.floating])
assert_type(u8_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(u8_nd - iu_nd, npt.NDArray[np.uint64 | np.float64])
assert_type(u8_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(u8_nd - iufc_nd, npt.NDArray[np.number])

assert_type(u8_nd - i_py, npt.NDArray[np.uint64])
assert_type(u8_nd - f_py, npt.NDArray[np.float64])
assert_type(u8_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - u8_nd, npt.NDArray[np.uint64])
assert_type(f_py - u8_nd, npt.NDArray[np.float64])
assert_type(c_py - u8_nd, npt.NDArray[np.complex128])

assert_type(f2_nd - i1_nd, npt.NDArray[np.float16])
assert_type(f2_nd - i2_nd, npt.NDArray[np.float32])
assert_type(f2_nd - i4_nd, npt.NDArray[np.float64])
assert_type(f2_nd - i8_nd, npt.NDArray[np.float64])
assert_type(f2_nd - u1_nd, npt.NDArray[np.float16])
assert_type(f2_nd - u2_nd, npt.NDArray[np.float32])
assert_type(f2_nd - u4_nd, npt.NDArray[np.float64])
assert_type(f2_nd - u8_nd, npt.NDArray[np.float64])
assert_type(f2_nd - f2_nd, npt.NDArray[np.float16])
assert_type(f2_nd - f4_nd, npt.NDArray[np.float32])
assert_type(f2_nd - f8_nd, npt.NDArray[np.float64])
assert_type(f2_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(f2_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(f2_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(f2_nd - cld_nd, npt.NDArray[np.clongdouble])
f2_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd - O_nd, npt.NDArray[np.object_])
assert_type(f2_nd - i_nd, npt.NDArray[np.floating])
assert_type(f2_nd - u_nd, npt.NDArray[np.floating])
assert_type(f2_nd - f_nd, npt.NDArray[np.floating])
assert_type(f2_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(f2_nd - iu_nd, npt.NDArray[np.floating])
assert_type(f2_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(f2_nd - iufc_nd, npt.NDArray[np.inexact])

assert_type(f2_nd - i_py, npt.NDArray[np.float16])
assert_type(f2_nd - f_py, npt.NDArray[np.float16])
assert_type(f2_nd - c_py, npt.NDArray[np.complex64])

assert_type(i_py - f2_nd, npt.NDArray[np.float16])
assert_type(f_py - f2_nd, npt.NDArray[np.float16])
assert_type(c_py - f2_nd, npt.NDArray[np.complex64])

assert_type(f4_nd - i1_nd, npt.NDArray[np.float32])
assert_type(f4_nd - i2_nd, npt.NDArray[np.float32])
assert_type(f4_nd - i4_nd, npt.NDArray[np.float64])
assert_type(f4_nd - i8_nd, npt.NDArray[np.float64])
assert_type(f4_nd - u1_nd, npt.NDArray[np.float32])
assert_type(f4_nd - u2_nd, npt.NDArray[np.float32])
assert_type(f4_nd - u4_nd, npt.NDArray[np.float64])
assert_type(f4_nd - u8_nd, npt.NDArray[np.float64])
assert_type(f4_nd - f2_nd, npt.NDArray[np.float32])
assert_type(f4_nd - f4_nd, npt.NDArray[np.float32])
assert_type(f4_nd - f8_nd, npt.NDArray[np.float64])
assert_type(f4_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(f4_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(f4_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(f4_nd - cld_nd, npt.NDArray[np.clongdouble])
f4_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd - O_nd, npt.NDArray[np.object_])
assert_type(f4_nd - i_nd, npt.NDArray[np.floating])
assert_type(f4_nd - u_nd, npt.NDArray[np.floating])
assert_type(f4_nd - f_nd, npt.NDArray[np.floating])
assert_type(f4_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(f4_nd - iu_nd, npt.NDArray[np.floating])
assert_type(f4_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(f4_nd - iufc_nd, npt.NDArray[np.inexact])

assert_type(f4_nd - i_py, npt.NDArray[np.float32])
assert_type(f4_nd - f_py, npt.NDArray[np.float32])
assert_type(f4_nd - c_py, npt.NDArray[np.complex64])

assert_type(i_py - f4_nd, npt.NDArray[np.float32])
assert_type(f_py - f4_nd, npt.NDArray[np.float32])
assert_type(c_py - f4_nd, npt.NDArray[np.complex64])

assert_type(f8_nd - i1_nd, npt.NDArray[np.float64])
assert_type(f8_nd - i2_nd, npt.NDArray[np.float64])
assert_type(f8_nd - i4_nd, npt.NDArray[np.float64])
assert_type(f8_nd - i8_nd, npt.NDArray[np.float64])
assert_type(f8_nd - u1_nd, npt.NDArray[np.float64])
assert_type(f8_nd - u2_nd, npt.NDArray[np.float64])
assert_type(f8_nd - u4_nd, npt.NDArray[np.float64])
assert_type(f8_nd - u8_nd, npt.NDArray[np.float64])
assert_type(f8_nd - f2_nd, npt.NDArray[np.float64])
assert_type(f8_nd - f4_nd, npt.NDArray[np.float64])
assert_type(f8_nd - f8_nd, npt.NDArray[np.float64])
assert_type(f8_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(f8_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(f8_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(f8_nd - cld_nd, npt.NDArray[np.clongdouble])
f8_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd - O_nd, npt.NDArray[np.object_])
assert_type(f8_nd - i_nd, npt.NDArray[np.float64])
assert_type(f8_nd - u_nd, npt.NDArray[np.float64])
assert_type(f8_nd - f_nd, npt.NDArray[np.floating])
assert_type(f8_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(f8_nd - iu_nd, npt.NDArray[np.float64])
assert_type(f8_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(f8_nd - iufc_nd, npt.NDArray[np.inexact])

assert_type(f8_nd - i_py, npt.NDArray[np.float64])
assert_type(f8_nd - f_py, npt.NDArray[np.float64])
assert_type(f8_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - f8_nd, npt.NDArray[np.float64])
assert_type(f_py - f8_nd, npt.NDArray[np.float64])
assert_type(c_py - f8_nd, npt.NDArray[np.complex128])

assert_type(fld_nd - i1_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - i2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - i4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - i8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - u1_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - u2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - u4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - u8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - f2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - f4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - f8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - c8_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd - c16_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd - cld_nd, npt.NDArray[np.clongdouble])
fld_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd - O_nd, npt.NDArray[np.object_])
assert_type(fld_nd - i_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - u_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - f_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - c_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd - iu_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd - fc_nd, npt.NDArray[np.longdouble | np.clongdouble])
assert_type(fld_nd - iufc_nd, npt.NDArray[np.longdouble | np.clongdouble])

assert_type(fld_nd - i_py, npt.NDArray[np.longdouble])
assert_type(fld_nd - f_py, npt.NDArray[np.longdouble])
assert_type(fld_nd - c_py, npt.NDArray[np.clongdouble])

assert_type(i_py - fld_nd, npt.NDArray[np.longdouble])
assert_type(f_py - fld_nd, npt.NDArray[np.longdouble])
assert_type(c_py - fld_nd, npt.NDArray[np.clongdouble])

assert_type(c8_nd - i1_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - i2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - i4_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - i8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - u1_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - u2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - u4_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - u8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - f2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - f4_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - f8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - fld_nd, npt.NDArray[np.clongdouble])
assert_type(c8_nd - c8_nd, npt.NDArray[np.complex64])
assert_type(c8_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(c8_nd - cld_nd, npt.NDArray[np.clongdouble])
c8_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c8_nd - O_nd, npt.NDArray[np.object_])
assert_type(c8_nd - i_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - u_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - f_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - iu_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - fc_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd - iufc_nd, npt.NDArray[np.complexfloating])

assert_type(c8_nd - i_py, npt.NDArray[np.complex64])
assert_type(c8_nd - f_py, npt.NDArray[np.complex64])
assert_type(c8_nd - c_py, npt.NDArray[np.complex64])

assert_type(i_py - c8_nd, npt.NDArray[np.complex64])
assert_type(f_py - c8_nd, npt.NDArray[np.complex64])
assert_type(c_py - c8_nd, npt.NDArray[np.complex64])

assert_type(c16_nd - i1_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - i2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - i4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - i8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - u1_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - u2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - u4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - u8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - f2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - f4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - f8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - fld_nd, npt.NDArray[np.clongdouble])
assert_type(c16_nd - c8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - cld_nd, npt.NDArray[np.clongdouble])
c16_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c16_nd - O_nd, npt.NDArray[np.object_])
assert_type(c16_nd - i_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - u_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - f_nd, npt.NDArray[np.complexfloating])
assert_type(c16_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(c16_nd - iu_nd, npt.NDArray[np.complex128])
assert_type(c16_nd - fc_nd, npt.NDArray[np.complexfloating])
assert_type(c16_nd - iufc_nd, npt.NDArray[np.complexfloating])

assert_type(c16_nd - i_py, npt.NDArray[np.complex128])
assert_type(c16_nd - f_py, npt.NDArray[np.complex128])
assert_type(c16_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - c16_nd, npt.NDArray[np.complex128])
assert_type(f_py - c16_nd, npt.NDArray[np.complex128])
assert_type(c_py - c16_nd, npt.NDArray[np.complex128])

assert_type(cld_nd - i1_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - i2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - i4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - i8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - u1_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - u2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - u4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - u8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - f2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - f4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - f8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - fld_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - c8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - c16_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - cld_nd, npt.NDArray[np.clongdouble])
cld_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(cld_nd - O_nd, npt.NDArray[np.object_])
assert_type(cld_nd - i_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - u_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - f_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - c_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - iu_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - fc_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd - iufc_nd, npt.NDArray[np.clongdouble])

assert_type(cld_nd - i_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd - f_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd - c_py, npt.NDArray[np.clongdouble])

assert_type(i_py - cld_nd, npt.NDArray[np.clongdouble])
assert_type(f_py - cld_nd, npt.NDArray[np.clongdouble])
assert_type(c_py - cld_nd, npt.NDArray[np.clongdouble])

assert_type(M8_nd - i1_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - i2_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - i4_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - i8_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - u1_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - u2_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - u4_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - u8_nd, npt.NDArray[np.datetime64])
M8_nd - f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd - M8_nd, npt.NDArray[np.timedelta64])
assert_type(M8_nd - m8_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - i_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd - u_nd, npt.NDArray[np.datetime64])
M8_nd - f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd - iu_nd, npt.NDArray[np.datetime64])
M8_nd - fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8_nd - i_py, npt.NDArray[np.datetime64])
M8_nd - f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd - c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

i_py - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd - i1_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - i2_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - i4_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - i8_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - u1_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - u2_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - u4_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - u8_nd, npt.NDArray[np.timedelta64])
m8_nd - f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - i_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd - u_nd, npt.NDArray[np.timedelta64])
m8_nd - f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd - iu_nd, npt.NDArray[np.timedelta64])
m8_nd - fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd - i_py, npt.NDArray[np.timedelta64])
m8_nd - f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd - c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i_py - m8_nd, npt.NDArray[np.timedelta64])
f_py - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(O_nd - i1_nd, npt.NDArray[np.object_])
assert_type(O_nd - i2_nd, npt.NDArray[np.object_])
assert_type(O_nd - i4_nd, npt.NDArray[np.object_])
assert_type(O_nd - i8_nd, npt.NDArray[np.object_])
assert_type(O_nd - u1_nd, npt.NDArray[np.object_])
assert_type(O_nd - u2_nd, npt.NDArray[np.object_])
assert_type(O_nd - u4_nd, npt.NDArray[np.object_])
assert_type(O_nd - u8_nd, npt.NDArray[np.object_])
assert_type(O_nd - f2_nd, npt.NDArray[np.object_])
assert_type(O_nd - f4_nd, npt.NDArray[np.object_])
assert_type(O_nd - f8_nd, npt.NDArray[np.object_])
assert_type(O_nd - fld_nd, npt.NDArray[np.object_])
assert_type(O_nd - c8_nd, npt.NDArray[np.object_])
assert_type(O_nd - c16_nd, npt.NDArray[np.object_])
assert_type(O_nd - cld_nd, npt.NDArray[np.object_])
assert_type(O_nd - O_nd, npt.NDArray[np.object_])
assert_type(O_nd - i_nd, npt.NDArray[np.object_])
assert_type(O_nd - u_nd, npt.NDArray[np.object_])
assert_type(O_nd - f_nd, npt.NDArray[np.object_])
assert_type(O_nd - c_nd, npt.NDArray[np.object_])
assert_type(O_nd - iu_nd, npt.NDArray[np.object_])
assert_type(O_nd - fc_nd, npt.NDArray[np.object_])
assert_type(O_nd - iufc_nd, npt.NDArray[np.object_])

assert_type(O_nd - i_py, npt.NDArray[np.object_])
assert_type(O_nd - f_py, npt.NDArray[np.object_])
assert_type(O_nd - c_py, npt.NDArray[np.object_])

assert_type(i_py - O_nd, npt.NDArray[np.object_])
assert_type(f_py - O_nd, npt.NDArray[np.object_])
assert_type(c_py - O_nd, npt.NDArray[np.object_])

assert_type(i_nd - i1_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - i2_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - i4_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - i8_nd, npt.NDArray[np.int64])
assert_type(i_nd - u1_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - u2_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - u4_nd, npt.NDArray[np.int64])
assert_type(i_nd - u8_nd, npt.NDArray[np.float64])
assert_type(i_nd - f2_nd, npt.NDArray[np.floating])
assert_type(i_nd - f4_nd, npt.NDArray[np.floating])
assert_type(i_nd - f8_nd, npt.NDArray[np.float64])
assert_type(i_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(i_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(i_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(i_nd - cld_nd, npt.NDArray[np.clongdouble])
i_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(i_nd - O_nd, npt.NDArray[np.object_])
assert_type(i_nd - i_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd - u_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i_nd - f_nd, npt.NDArray[np.floating])
assert_type(i_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(i_nd - iu_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(i_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(i_nd - iufc_nd, npt.NDArray[np.number])

assert_type(i_nd - i_py, npt.NDArray[np.signedinteger])
assert_type(i_nd - f_py, npt.NDArray[np.float64])
assert_type(i_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - i_nd, npt.NDArray[np.signedinteger])
assert_type(f_py - i_nd, npt.NDArray[np.float64])
assert_type(c_py - i_nd, npt.NDArray[np.complex128])

assert_type(u_nd - i1_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(u_nd - i2_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(u_nd - i4_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(u_nd - i8_nd, npt.NDArray[np.int64 | np.float64])
assert_type(u_nd - u1_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd - u2_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd - u4_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd - u8_nd, npt.NDArray[np.uint64])
assert_type(u_nd - f2_nd, npt.NDArray[np.floating])
assert_type(u_nd - f4_nd, npt.NDArray[np.floating])
assert_type(u_nd - f8_nd, npt.NDArray[np.float64])
assert_type(u_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(u_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(u_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(u_nd - cld_nd, npt.NDArray[np.clongdouble])
u_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(u_nd - O_nd, npt.NDArray[np.object_])
assert_type(u_nd - i_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(u_nd - u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd - f_nd, npt.NDArray[np.floating])
assert_type(u_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(u_nd - iu_nd, npt.NDArray[np.integer | np.float64])
assert_type(u_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(u_nd - iufc_nd, npt.NDArray[np.number])

assert_type(u_nd - i_py, npt.NDArray[np.unsignedinteger])
assert_type(u_nd - f_py, npt.NDArray[np.float64])
assert_type(u_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - u_nd, npt.NDArray[np.unsignedinteger])
assert_type(f_py - u_nd, npt.NDArray[np.float64])
assert_type(c_py - u_nd, npt.NDArray[np.complex128])

assert_type(f_nd - i1_nd, npt.NDArray[np.floating])
assert_type(f_nd - i2_nd, npt.NDArray[np.floating])
assert_type(f_nd - i4_nd, npt.NDArray[np.floating])
assert_type(f_nd - i8_nd, npt.NDArray[np.floating])
assert_type(f_nd - u1_nd, npt.NDArray[np.floating])
assert_type(f_nd - u2_nd, npt.NDArray[np.floating])
assert_type(f_nd - u4_nd, npt.NDArray[np.floating])
assert_type(f_nd - u8_nd, npt.NDArray[np.floating])
assert_type(f_nd - f2_nd, npt.NDArray[np.floating])
assert_type(f_nd - f4_nd, npt.NDArray[np.floating])
assert_type(f_nd - f8_nd, npt.NDArray[np.floating])
assert_type(f_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(f_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd - c16_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd - cld_nd, npt.NDArray[np.clongdouble])
f_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f_nd - O_nd, npt.NDArray[np.object_])
assert_type(f_nd - i_nd, npt.NDArray[np.floating])
assert_type(f_nd - u_nd, npt.NDArray[np.floating])
assert_type(f_nd - f_nd, npt.NDArray[np.floating])
assert_type(f_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd - iu_nd, npt.NDArray[np.floating])
assert_type(f_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(f_nd - iufc_nd, npt.NDArray[np.inexact])

assert_type(f_nd - i_py, npt.NDArray[np.floating])
assert_type(f_nd - f_py, npt.NDArray[np.floating])
assert_type(f_nd - c_py, npt.NDArray[np.complexfloating])

assert_type(i_py - f_nd, npt.NDArray[np.floating])
assert_type(f_py - f_nd, npt.NDArray[np.floating])
assert_type(c_py - f_nd, npt.NDArray[np.complexfloating])

assert_type(c_nd - i1_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - i2_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - i4_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - i8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - u1_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - u2_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - u4_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - u8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - f2_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - f4_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - f8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - fld_nd, npt.NDArray[np.clongdouble])
assert_type(c_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - c16_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - cld_nd, npt.NDArray[np.clongdouble])
c_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c_nd - O_nd, npt.NDArray[np.object_])
assert_type(c_nd - i_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - u_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - f_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - iu_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - fc_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd - iufc_nd, npt.NDArray[np.complexfloating])

assert_type(c_nd - i_py, npt.NDArray[np.complexfloating])
assert_type(c_nd - f_py, npt.NDArray[np.complexfloating])
assert_type(c_nd - c_py, npt.NDArray[np.complexfloating])

assert_type(i_py - c_nd, npt.NDArray[np.complexfloating])
assert_type(f_py - c_nd, npt.NDArray[np.complexfloating])
assert_type(c_py - c_nd, npt.NDArray[np.complexfloating])

assert_type(iu_nd - i1_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(iu_nd - i2_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(iu_nd - i4_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(iu_nd - i8_nd, npt.NDArray[np.int64 | np.float64])
assert_type(iu_nd - u1_nd, npt.NDArray[np.integer])
assert_type(iu_nd - u2_nd, npt.NDArray[np.integer])
assert_type(iu_nd - u4_nd, npt.NDArray[np.integer])
assert_type(iu_nd - u8_nd, npt.NDArray[np.uint64 | np.float64])
assert_type(iu_nd - f2_nd, npt.NDArray[np.floating])
assert_type(iu_nd - f4_nd, npt.NDArray[np.floating])
assert_type(iu_nd - f8_nd, npt.NDArray[np.float64])
assert_type(iu_nd - fld_nd, npt.NDArray[np.longdouble])
assert_type(iu_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(iu_nd - c16_nd, npt.NDArray[np.complex128])
assert_type(iu_nd - cld_nd, npt.NDArray[np.clongdouble])
iu_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu_nd - m8_nd, npt.NDArray[np.timedelta64])
assert_type(iu_nd - O_nd, npt.NDArray[np.object_])
assert_type(iu_nd - i_nd, npt.NDArray[np.signedinteger | np.float64])
assert_type(iu_nd - u_nd, npt.NDArray[np.integer | np.float64])
assert_type(iu_nd - f_nd, npt.NDArray[np.floating])
assert_type(iu_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(iu_nd - iu_nd, npt.NDArray[np.integer | np.float64])
assert_type(iu_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(iu_nd - iufc_nd, npt.NDArray[np.number])

assert_type(iu_nd - i_py, npt.NDArray[np.integer])
assert_type(iu_nd - f_py, npt.NDArray[np.float64])
assert_type(iu_nd - c_py, npt.NDArray[np.complex128])

assert_type(i_py - iu_nd, npt.NDArray[np.integer])
assert_type(f_py - iu_nd, npt.NDArray[np.float64])
assert_type(c_py - iu_nd, npt.NDArray[np.complex128])

assert_type(fc_nd - i1_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - i2_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - i4_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - i8_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - u1_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - u2_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - u4_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - u8_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - f2_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - f4_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - f8_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - fld_nd, npt.NDArray[np.longdouble | np.clongdouble])
assert_type(fc_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd - c16_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd - cld_nd, npt.NDArray[np.clongdouble])
fc_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fc_nd - O_nd, npt.NDArray[np.object_])
assert_type(fc_nd - i_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - u_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - f_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd - iu_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(fc_nd - iufc_nd, npt.NDArray[np.inexact])

assert_type(fc_nd - i_py, npt.NDArray[np.inexact])
assert_type(fc_nd - f_py, npt.NDArray[np.inexact])
assert_type(fc_nd - c_py, npt.NDArray[np.complexfloating])

assert_type(i_py - fc_nd, npt.NDArray[np.inexact])
assert_type(f_py - fc_nd, npt.NDArray[np.inexact])
assert_type(c_py - fc_nd, npt.NDArray[np.complexfloating])

assert_type(iufc_nd - i1_nd, npt.NDArray[np.number])
assert_type(iufc_nd - i2_nd, npt.NDArray[np.number])
assert_type(iufc_nd - i4_nd, npt.NDArray[np.number])
assert_type(iufc_nd - i8_nd, npt.NDArray[np.number])
assert_type(iufc_nd - u1_nd, npt.NDArray[np.number])
assert_type(iufc_nd - u2_nd, npt.NDArray[np.number])
assert_type(iufc_nd - u4_nd, npt.NDArray[np.number])
assert_type(iufc_nd - u8_nd, npt.NDArray[np.number])
assert_type(iufc_nd - f2_nd, npt.NDArray[np.inexact])
assert_type(iufc_nd - f4_nd, npt.NDArray[np.inexact])
assert_type(iufc_nd - f8_nd, npt.NDArray[np.inexact])
assert_type(iufc_nd - fld_nd, npt.NDArray[np.longdouble | np.clongdouble])
assert_type(iufc_nd - c8_nd, npt.NDArray[np.complexfloating])
assert_type(iufc_nd - c16_nd, npt.NDArray[np.complexfloating])
assert_type(iufc_nd - cld_nd, npt.NDArray[np.clongdouble])
iufc_nd - M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc_nd - m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iufc_nd - O_nd, npt.NDArray[np.object_])
assert_type(iufc_nd - i_nd, npt.NDArray[np.number])
assert_type(iufc_nd - u_nd, npt.NDArray[np.number])
assert_type(iufc_nd - f_nd, npt.NDArray[np.inexact])
assert_type(iufc_nd - c_nd, npt.NDArray[np.complexfloating])
assert_type(iufc_nd - iu_nd, npt.NDArray[np.number])
assert_type(iufc_nd - fc_nd, npt.NDArray[np.inexact])
assert_type(iufc_nd - iufc_nd, npt.NDArray[np.number])

assert_type(iufc_nd - i_py, npt.NDArray[np.number])
assert_type(iufc_nd - f_py, npt.NDArray[np.inexact])
assert_type(iufc_nd - c_py, npt.NDArray[np.complexfloating])

assert_type(i_py - iufc_nd, npt.NDArray[np.number])
assert_type(f_py - iufc_nd, npt.NDArray[np.inexact])
assert_type(c_py - iufc_nd, npt.NDArray[np.complexfloating])
