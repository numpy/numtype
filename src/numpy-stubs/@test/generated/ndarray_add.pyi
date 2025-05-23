# @generated 2025-05-19T02:35:42Z with tool/testgen.py
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
c8_nd: _nt.Array[np.complex64]
c16_nd: _nt.Array[np.complex128]
cld_nd: _nt.Array[np.clongdouble]
M8_nd: _nt.Array[np.datetime64]
m8_nd: _nt.Array[np.timedelta64]
O_nd: _nt.Array[np.object_]
S_nd: _nt.Array[np.bytes_]
U_nd: _nt.Array[np.str_]
T_nd: np.ndarray[_nt.Shape, np.dtypes.StringDType]
i_nd: _nt.Array[np.signedinteger]
u_nd: _nt.Array[np.unsignedinteger]
f_nd: _nt.Array[np.floating]
c_nd: _nt.Array[np.complexfloating]
iu_nd: _nt.Array[np.integer]
fc_nd: _nt.Array[np.inexact]
iufc_nd: _nt.Array[np.number]

b_py: bool
i_py: int
f_py: float
c_py: complex
S_py: bytes
U_py: str

###

assert_type(b1_nd + b1_nd, _nt.Array[np.bool])
assert_type(b1_nd + i1_nd, _nt.Array[np.int8])
assert_type(b1_nd + i2_nd, _nt.Array[np.int16])
assert_type(b1_nd + i4_nd, _nt.Array[np.int32])
assert_type(b1_nd + i8_nd, _nt.Array[np.int64])
assert_type(b1_nd + u1_nd, _nt.Array[np.uint8])
assert_type(b1_nd + u2_nd, _nt.Array[np.uint16])
assert_type(b1_nd + u4_nd, _nt.Array[np.uint32])
assert_type(b1_nd + u8_nd, _nt.Array[np.uint64])
assert_type(b1_nd + f2_nd, _nt.Array[np.float16])
assert_type(b1_nd + f4_nd, _nt.Array[np.float32])
assert_type(b1_nd + f8_nd, _nt.Array[np.float64])
assert_type(b1_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(b1_nd + c8_nd, _nt.Array[np.complex64])
assert_type(b1_nd + c16_nd, _nt.Array[np.complex128])
assert_type(b1_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(b1_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(b1_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(b1_nd + O_nd, _nt.Array[np.object_])
b1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(b1_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(b1_nd + u_nd, _nt.Array[np.unsignedinteger])
assert_type(b1_nd + f_nd, _nt.Array[np.floating])
assert_type(b1_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(b1_nd + iu_nd, _nt.Array[np.integer])
assert_type(b1_nd + fc_nd, _nt.Array[np.inexact])
assert_type(b1_nd + iufc_nd, _nt.Array[np.number])

assert_type(b1_nd + b_py, _nt.Array[np.bool])
assert_type(b1_nd + i_py, _nt.Array[np.int64])
assert_type(b1_nd + f_py, _nt.Array[np.float64])
assert_type(b1_nd + c_py, _nt.Array[np.complex128])
b1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + b1_nd, _nt.Array[np.bool])
assert_type(i_py + b1_nd, _nt.Array[np.int64])
assert_type(f_py + b1_nd, _nt.Array[np.float64])
assert_type(c_py + b1_nd, _nt.Array[np.complex128])
U_py + b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1_nd + b1_nd, _nt.Array[np.int8])
assert_type(i1_nd + i1_nd, _nt.Array[np.int8])
assert_type(i1_nd + i2_nd, _nt.Array[np.int16])
assert_type(i1_nd + i4_nd, _nt.Array[np.int32])
assert_type(i1_nd + i8_nd, _nt.Array[np.int64])
assert_type(i1_nd + u1_nd, _nt.Array[np.int16])
assert_type(i1_nd + u2_nd, _nt.Array[np.int32])
assert_type(i1_nd + u4_nd, _nt.Array[np.int64])
assert_type(i1_nd + u8_nd, _nt.Array[np.float64])
assert_type(i1_nd + f2_nd, _nt.Array[np.float16])
assert_type(i1_nd + f4_nd, _nt.Array[np.float32])
assert_type(i1_nd + f8_nd, _nt.Array[np.float64])
assert_type(i1_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(i1_nd + c8_nd, _nt.Array[np.complex64])
assert_type(i1_nd + c16_nd, _nt.Array[np.complex128])
assert_type(i1_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(i1_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(i1_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(i1_nd + O_nd, _nt.Array[np.object_])
i1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(i1_nd + u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i1_nd + f_nd, _nt.Array[np.floating])
assert_type(i1_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(i1_nd + iu_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i1_nd + fc_nd, _nt.Array[np.inexact])
assert_type(i1_nd + iufc_nd, _nt.Array[np.number])

assert_type(i1_nd + b_py, _nt.Array[np.int8])
assert_type(i1_nd + i_py, _nt.Array[np.int8])
assert_type(i1_nd + f_py, _nt.Array[np.float64])
assert_type(i1_nd + c_py, _nt.Array[np.complex128])
i1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i1_nd, _nt.Array[np.int8])
assert_type(i_py + i1_nd, _nt.Array[np.int8])
assert_type(f_py + i1_nd, _nt.Array[np.float64])
assert_type(c_py + i1_nd, _nt.Array[np.complex128])
U_py + i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2_nd + b1_nd, _nt.Array[np.int16])
assert_type(i2_nd + i1_nd, _nt.Array[np.int16])
assert_type(i2_nd + i2_nd, _nt.Array[np.int16])
assert_type(i2_nd + i4_nd, _nt.Array[np.int32])
assert_type(i2_nd + i8_nd, _nt.Array[np.int64])
assert_type(i2_nd + u1_nd, _nt.Array[np.int16])
assert_type(i2_nd + u2_nd, _nt.Array[np.int32])
assert_type(i2_nd + u4_nd, _nt.Array[np.int64])
assert_type(i2_nd + u8_nd, _nt.Array[np.float64])
assert_type(i2_nd + f2_nd, _nt.Array[np.float32])
assert_type(i2_nd + f4_nd, _nt.Array[np.float32])
assert_type(i2_nd + f8_nd, _nt.Array[np.float64])
assert_type(i2_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(i2_nd + c8_nd, _nt.Array[np.complex64])
assert_type(i2_nd + c16_nd, _nt.Array[np.complex128])
assert_type(i2_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(i2_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(i2_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(i2_nd + O_nd, _nt.Array[np.object_])
i2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(i2_nd + u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i2_nd + f_nd, _nt.Array[np.floating])
assert_type(i2_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(i2_nd + iu_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i2_nd + fc_nd, _nt.Array[np.inexact])
assert_type(i2_nd + iufc_nd, _nt.Array[np.number])

assert_type(i2_nd + b_py, _nt.Array[np.int16])
assert_type(i2_nd + i_py, _nt.Array[np.int16])
assert_type(i2_nd + f_py, _nt.Array[np.float64])
assert_type(i2_nd + c_py, _nt.Array[np.complex128])
i2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i2_nd, _nt.Array[np.int16])
assert_type(i_py + i2_nd, _nt.Array[np.int16])
assert_type(f_py + i2_nd, _nt.Array[np.float64])
assert_type(c_py + i2_nd, _nt.Array[np.complex128])
U_py + i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4_nd + b1_nd, _nt.Array[np.int32])
assert_type(i4_nd + i1_nd, _nt.Array[np.int32])
assert_type(i4_nd + i2_nd, _nt.Array[np.int32])
assert_type(i4_nd + i4_nd, _nt.Array[np.int32])
assert_type(i4_nd + i8_nd, _nt.Array[np.int64])
assert_type(i4_nd + u1_nd, _nt.Array[np.int32])
assert_type(i4_nd + u2_nd, _nt.Array[np.int32])
assert_type(i4_nd + u4_nd, _nt.Array[np.int64])
assert_type(i4_nd + u8_nd, _nt.Array[np.float64])
assert_type(i4_nd + f2_nd, _nt.Array[np.float64])
assert_type(i4_nd + f4_nd, _nt.Array[np.float64])
assert_type(i4_nd + f8_nd, _nt.Array[np.float64])
assert_type(i4_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(i4_nd + c8_nd, _nt.Array[np.complex128])
assert_type(i4_nd + c16_nd, _nt.Array[np.complex128])
assert_type(i4_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(i4_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(i4_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(i4_nd + O_nd, _nt.Array[np.object_])
i4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(i4_nd + u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i4_nd + f_nd, _nt.Array[np.floating])
assert_type(i4_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(i4_nd + iu_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i4_nd + fc_nd, _nt.Array[np.inexact])
assert_type(i4_nd + iufc_nd, _nt.Array[np.number])

assert_type(i4_nd + b_py, _nt.Array[np.int32])
assert_type(i4_nd + i_py, _nt.Array[np.int32])
assert_type(i4_nd + f_py, _nt.Array[np.float64])
assert_type(i4_nd + c_py, _nt.Array[np.complex128])
i4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i4_nd, _nt.Array[np.int32])
assert_type(i_py + i4_nd, _nt.Array[np.int32])
assert_type(f_py + i4_nd, _nt.Array[np.float64])
assert_type(c_py + i4_nd, _nt.Array[np.complex128])
U_py + i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8_nd + b1_nd, _nt.Array[np.int64])
assert_type(i8_nd + i1_nd, _nt.Array[np.int64])
assert_type(i8_nd + i2_nd, _nt.Array[np.int64])
assert_type(i8_nd + i4_nd, _nt.Array[np.int64])
assert_type(i8_nd + i8_nd, _nt.Array[np.int64])
assert_type(i8_nd + u1_nd, _nt.Array[np.int64])
assert_type(i8_nd + u2_nd, _nt.Array[np.int64])
assert_type(i8_nd + u4_nd, _nt.Array[np.int64])
assert_type(i8_nd + u8_nd, _nt.Array[np.float64])
assert_type(i8_nd + f2_nd, _nt.Array[np.float64])
assert_type(i8_nd + f4_nd, _nt.Array[np.float64])
assert_type(i8_nd + f8_nd, _nt.Array[np.float64])
assert_type(i8_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(i8_nd + c8_nd, _nt.Array[np.complex128])
assert_type(i8_nd + c16_nd, _nt.Array[np.complex128])
assert_type(i8_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(i8_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(i8_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(i8_nd + O_nd, _nt.Array[np.object_])
i8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8_nd + i_nd, _nt.Array[np.int64])
assert_type(i8_nd + u_nd, _nt.Array[np.int64 | np.float64])
assert_type(i8_nd + f_nd, _nt.Array[np.floating])
assert_type(i8_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(i8_nd + iu_nd, _nt.Array[np.int64 | np.float64])
assert_type(i8_nd + fc_nd, _nt.Array[np.inexact])
assert_type(i8_nd + iufc_nd, _nt.Array[np.number])

assert_type(i8_nd + b_py, _nt.Array[np.int64])
assert_type(i8_nd + i_py, _nt.Array[np.int64])
assert_type(i8_nd + f_py, _nt.Array[np.float64])
assert_type(i8_nd + c_py, _nt.Array[np.complex128])
i8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i8_nd, _nt.Array[np.int64])
assert_type(i_py + i8_nd, _nt.Array[np.int64])
assert_type(f_py + i8_nd, _nt.Array[np.float64])
assert_type(c_py + i8_nd, _nt.Array[np.complex128])
U_py + i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1_nd + b1_nd, _nt.Array[np.uint8])
assert_type(u1_nd + i1_nd, _nt.Array[np.int16])
assert_type(u1_nd + i2_nd, _nt.Array[np.int16])
assert_type(u1_nd + i4_nd, _nt.Array[np.int32])
assert_type(u1_nd + i8_nd, _nt.Array[np.int64])
assert_type(u1_nd + u1_nd, _nt.Array[np.uint8])
assert_type(u1_nd + u2_nd, _nt.Array[np.uint16])
assert_type(u1_nd + u4_nd, _nt.Array[np.uint32])
assert_type(u1_nd + u8_nd, _nt.Array[np.uint64])
assert_type(u1_nd + f2_nd, _nt.Array[np.float16])
assert_type(u1_nd + f4_nd, _nt.Array[np.float32])
assert_type(u1_nd + f8_nd, _nt.Array[np.float64])
assert_type(u1_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(u1_nd + c8_nd, _nt.Array[np.complex64])
assert_type(u1_nd + c16_nd, _nt.Array[np.complex128])
assert_type(u1_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(u1_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(u1_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(u1_nd + O_nd, _nt.Array[np.object_])
u1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u1_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(u1_nd + u_nd, _nt.Array[np.unsignedinteger])
assert_type(u1_nd + f_nd, _nt.Array[np.floating])
assert_type(u1_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(u1_nd + iu_nd, _nt.Array[np.integer])
assert_type(u1_nd + fc_nd, _nt.Array[np.inexact])
assert_type(u1_nd + iufc_nd, _nt.Array[np.number])

assert_type(u1_nd + b_py, _nt.Array[np.uint8])
assert_type(u1_nd + i_py, _nt.Array[np.uint8])
assert_type(u1_nd + f_py, _nt.Array[np.float64])
assert_type(u1_nd + c_py, _nt.Array[np.complex128])
u1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u1_nd, _nt.Array[np.uint8])
assert_type(i_py + u1_nd, _nt.Array[np.uint8])
assert_type(f_py + u1_nd, _nt.Array[np.float64])
assert_type(c_py + u1_nd, _nt.Array[np.complex128])
U_py + u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2_nd + b1_nd, _nt.Array[np.uint16])
assert_type(u2_nd + i1_nd, _nt.Array[np.int32])
assert_type(u2_nd + i2_nd, _nt.Array[np.int32])
assert_type(u2_nd + i4_nd, _nt.Array[np.int32])
assert_type(u2_nd + i8_nd, _nt.Array[np.int64])
assert_type(u2_nd + u1_nd, _nt.Array[np.uint16])
assert_type(u2_nd + u2_nd, _nt.Array[np.uint16])
assert_type(u2_nd + u4_nd, _nt.Array[np.uint32])
assert_type(u2_nd + u8_nd, _nt.Array[np.uint64])
assert_type(u2_nd + f2_nd, _nt.Array[np.float32])
assert_type(u2_nd + f4_nd, _nt.Array[np.float32])
assert_type(u2_nd + f8_nd, _nt.Array[np.float64])
assert_type(u2_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(u2_nd + c8_nd, _nt.Array[np.complex64])
assert_type(u2_nd + c16_nd, _nt.Array[np.complex128])
assert_type(u2_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(u2_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(u2_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(u2_nd + O_nd, _nt.Array[np.object_])
u2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u2_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(u2_nd + u_nd, _nt.Array[np.unsignedinteger])
assert_type(u2_nd + f_nd, _nt.Array[np.floating])
assert_type(u2_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(u2_nd + iu_nd, _nt.Array[np.integer])
assert_type(u2_nd + fc_nd, _nt.Array[np.inexact])
assert_type(u2_nd + iufc_nd, _nt.Array[np.number])

assert_type(u2_nd + b_py, _nt.Array[np.uint16])
assert_type(u2_nd + i_py, _nt.Array[np.uint16])
assert_type(u2_nd + f_py, _nt.Array[np.float64])
assert_type(u2_nd + c_py, _nt.Array[np.complex128])
u2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u2_nd, _nt.Array[np.uint16])
assert_type(i_py + u2_nd, _nt.Array[np.uint16])
assert_type(f_py + u2_nd, _nt.Array[np.float64])
assert_type(c_py + u2_nd, _nt.Array[np.complex128])
U_py + u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4_nd + b1_nd, _nt.Array[np.uint32])
assert_type(u4_nd + i1_nd, _nt.Array[np.int64])
assert_type(u4_nd + i2_nd, _nt.Array[np.int64])
assert_type(u4_nd + i4_nd, _nt.Array[np.int64])
assert_type(u4_nd + i8_nd, _nt.Array[np.int64])
assert_type(u4_nd + u1_nd, _nt.Array[np.uint32])
assert_type(u4_nd + u2_nd, _nt.Array[np.uint32])
assert_type(u4_nd + u4_nd, _nt.Array[np.uint32])
assert_type(u4_nd + u8_nd, _nt.Array[np.uint64])
assert_type(u4_nd + f2_nd, _nt.Array[np.float64])
assert_type(u4_nd + f4_nd, _nt.Array[np.float64])
assert_type(u4_nd + f8_nd, _nt.Array[np.float64])
assert_type(u4_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(u4_nd + c8_nd, _nt.Array[np.complex128])
assert_type(u4_nd + c16_nd, _nt.Array[np.complex128])
assert_type(u4_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(u4_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(u4_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(u4_nd + O_nd, _nt.Array[np.object_])
u4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u4_nd + i_nd, _nt.Array[np.int64])
assert_type(u4_nd + u_nd, _nt.Array[np.unsignedinteger])
assert_type(u4_nd + f_nd, _nt.Array[np.floating])
assert_type(u4_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(u4_nd + iu_nd, _nt.Array[np.integer])
assert_type(u4_nd + fc_nd, _nt.Array[np.inexact])
assert_type(u4_nd + iufc_nd, _nt.Array[np.number])

assert_type(u4_nd + b_py, _nt.Array[np.uint32])
assert_type(u4_nd + i_py, _nt.Array[np.uint32])
assert_type(u4_nd + f_py, _nt.Array[np.float64])
assert_type(u4_nd + c_py, _nt.Array[np.complex128])
u4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u4_nd, _nt.Array[np.uint32])
assert_type(i_py + u4_nd, _nt.Array[np.uint32])
assert_type(f_py + u4_nd, _nt.Array[np.float64])
assert_type(c_py + u4_nd, _nt.Array[np.complex128])
U_py + u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8_nd + b1_nd, _nt.Array[np.uint64])
assert_type(u8_nd + i1_nd, _nt.Array[np.float64])
assert_type(u8_nd + i2_nd, _nt.Array[np.float64])
assert_type(u8_nd + i4_nd, _nt.Array[np.float64])
assert_type(u8_nd + i8_nd, _nt.Array[np.float64])
assert_type(u8_nd + u1_nd, _nt.Array[np.uint64])
assert_type(u8_nd + u2_nd, _nt.Array[np.uint64])
assert_type(u8_nd + u4_nd, _nt.Array[np.uint64])
assert_type(u8_nd + u8_nd, _nt.Array[np.uint64])
assert_type(u8_nd + f2_nd, _nt.Array[np.float64])
assert_type(u8_nd + f4_nd, _nt.Array[np.float64])
assert_type(u8_nd + f8_nd, _nt.Array[np.float64])
assert_type(u8_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(u8_nd + c8_nd, _nt.Array[np.complex128])
assert_type(u8_nd + c16_nd, _nt.Array[np.complex128])
assert_type(u8_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(u8_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(u8_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(u8_nd + O_nd, _nt.Array[np.object_])
u8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8_nd + i_nd, _nt.Array[np.float64])
assert_type(u8_nd + u_nd, _nt.Array[np.uint64])
assert_type(u8_nd + f_nd, _nt.Array[np.floating])
assert_type(u8_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(u8_nd + iu_nd, _nt.Array[np.uint64 | np.float64])
assert_type(u8_nd + fc_nd, _nt.Array[np.inexact])
assert_type(u8_nd + iufc_nd, _nt.Array[np.number])

assert_type(u8_nd + b_py, _nt.Array[np.uint64])
assert_type(u8_nd + i_py, _nt.Array[np.uint64])
assert_type(u8_nd + f_py, _nt.Array[np.float64])
assert_type(u8_nd + c_py, _nt.Array[np.complex128])
u8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u8_nd, _nt.Array[np.uint64])
assert_type(i_py + u8_nd, _nt.Array[np.uint64])
assert_type(f_py + u8_nd, _nt.Array[np.float64])
assert_type(c_py + u8_nd, _nt.Array[np.complex128])
U_py + u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2_nd + b1_nd, _nt.Array[np.float16])
assert_type(f2_nd + i1_nd, _nt.Array[np.float16])
assert_type(f2_nd + i2_nd, _nt.Array[np.float32])
assert_type(f2_nd + i4_nd, _nt.Array[np.float64])
assert_type(f2_nd + i8_nd, _nt.Array[np.float64])
assert_type(f2_nd + u1_nd, _nt.Array[np.float16])
assert_type(f2_nd + u2_nd, _nt.Array[np.float32])
assert_type(f2_nd + u4_nd, _nt.Array[np.float64])
assert_type(f2_nd + u8_nd, _nt.Array[np.float64])
assert_type(f2_nd + f2_nd, _nt.Array[np.float16])
assert_type(f2_nd + f4_nd, _nt.Array[np.float32])
assert_type(f2_nd + f8_nd, _nt.Array[np.float64])
assert_type(f2_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(f2_nd + c8_nd, _nt.Array[np.complex64])
assert_type(f2_nd + c16_nd, _nt.Array[np.complex128])
assert_type(f2_nd + cld_nd, _nt.Array[np.clongdouble])
f2_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd + O_nd, _nt.Array[np.object_])
f2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd + i_nd, _nt.Array[np.floating])
assert_type(f2_nd + u_nd, _nt.Array[np.floating])
assert_type(f2_nd + f_nd, _nt.Array[np.floating])
assert_type(f2_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(f2_nd + iu_nd, _nt.Array[np.floating])
assert_type(f2_nd + fc_nd, _nt.Array[np.inexact])
assert_type(f2_nd + iufc_nd, _nt.Array[np.inexact])

assert_type(f2_nd + b_py, _nt.Array[np.float16])
assert_type(f2_nd + i_py, _nt.Array[np.float16])
assert_type(f2_nd + f_py, _nt.Array[np.float16])
assert_type(f2_nd + c_py, _nt.Array[np.complex64])
f2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f2_nd, _nt.Array[np.float16])
assert_type(i_py + f2_nd, _nt.Array[np.float16])
assert_type(f_py + f2_nd, _nt.Array[np.float16])
assert_type(c_py + f2_nd, _nt.Array[np.complex64])
U_py + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4_nd + b1_nd, _nt.Array[np.float32])
assert_type(f4_nd + i1_nd, _nt.Array[np.float32])
assert_type(f4_nd + i2_nd, _nt.Array[np.float32])
assert_type(f4_nd + i4_nd, _nt.Array[np.float64])
assert_type(f4_nd + i8_nd, _nt.Array[np.float64])
assert_type(f4_nd + u1_nd, _nt.Array[np.float32])
assert_type(f4_nd + u2_nd, _nt.Array[np.float32])
assert_type(f4_nd + u4_nd, _nt.Array[np.float64])
assert_type(f4_nd + u8_nd, _nt.Array[np.float64])
assert_type(f4_nd + f2_nd, _nt.Array[np.float32])
assert_type(f4_nd + f4_nd, _nt.Array[np.float32])
assert_type(f4_nd + f8_nd, _nt.Array[np.float64])
assert_type(f4_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(f4_nd + c8_nd, _nt.Array[np.complex64])
assert_type(f4_nd + c16_nd, _nt.Array[np.complex128])
assert_type(f4_nd + cld_nd, _nt.Array[np.clongdouble])
f4_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd + O_nd, _nt.Array[np.object_])
f4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd + i_nd, _nt.Array[np.floating])
assert_type(f4_nd + u_nd, _nt.Array[np.floating])
assert_type(f4_nd + f_nd, _nt.Array[np.floating])
assert_type(f4_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(f4_nd + iu_nd, _nt.Array[np.floating])
assert_type(f4_nd + fc_nd, _nt.Array[np.inexact])
assert_type(f4_nd + iufc_nd, _nt.Array[np.inexact])

assert_type(f4_nd + b_py, _nt.Array[np.float32])
assert_type(f4_nd + i_py, _nt.Array[np.float32])
assert_type(f4_nd + f_py, _nt.Array[np.float32])
assert_type(f4_nd + c_py, _nt.Array[np.complex64])
f4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f4_nd, _nt.Array[np.float32])
assert_type(i_py + f4_nd, _nt.Array[np.float32])
assert_type(f_py + f4_nd, _nt.Array[np.float32])
assert_type(c_py + f4_nd, _nt.Array[np.complex64])
U_py + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8_nd + b1_nd, _nt.Array[np.float64])
assert_type(f8_nd + i1_nd, _nt.Array[np.float64])
assert_type(f8_nd + i2_nd, _nt.Array[np.float64])
assert_type(f8_nd + i4_nd, _nt.Array[np.float64])
assert_type(f8_nd + i8_nd, _nt.Array[np.float64])
assert_type(f8_nd + u1_nd, _nt.Array[np.float64])
assert_type(f8_nd + u2_nd, _nt.Array[np.float64])
assert_type(f8_nd + u4_nd, _nt.Array[np.float64])
assert_type(f8_nd + u8_nd, _nt.Array[np.float64])
assert_type(f8_nd + f2_nd, _nt.Array[np.float64])
assert_type(f8_nd + f4_nd, _nt.Array[np.float64])
assert_type(f8_nd + f8_nd, _nt.Array[np.float64])
assert_type(f8_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(f8_nd + c8_nd, _nt.Array[np.complex128])
assert_type(f8_nd + c16_nd, _nt.Array[np.complex128])
assert_type(f8_nd + cld_nd, _nt.Array[np.clongdouble])
f8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd + O_nd, _nt.Array[np.object_])
f8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd + i_nd, _nt.Array[np.float64])
assert_type(f8_nd + u_nd, _nt.Array[np.float64])
assert_type(f8_nd + f_nd, _nt.Array[np.floating])
assert_type(f8_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(f8_nd + iu_nd, _nt.Array[np.float64])
assert_type(f8_nd + fc_nd, _nt.Array[np.inexact])
assert_type(f8_nd + iufc_nd, _nt.Array[np.inexact])

assert_type(f8_nd + b_py, _nt.Array[np.float64])
assert_type(f8_nd + i_py, _nt.Array[np.float64])
assert_type(f8_nd + f_py, _nt.Array[np.float64])
assert_type(f8_nd + c_py, _nt.Array[np.complex128])
f8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f8_nd, _nt.Array[np.float64])
assert_type(i_py + f8_nd, _nt.Array[np.float64])
assert_type(f_py + f8_nd, _nt.Array[np.float64])
assert_type(c_py + f8_nd, _nt.Array[np.complex128])
U_py + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(fld_nd + b1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + i1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + i2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + i4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + i8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + u1_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + u2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + u4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + u8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + f2_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + f4_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + f8_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + c8_nd, _nt.Array[np.clongdouble])
assert_type(fld_nd + c16_nd, _nt.Array[np.clongdouble])
assert_type(fld_nd + cld_nd, _nt.Array[np.clongdouble])
fld_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd + O_nd, _nt.Array[np.object_])
fld_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd + i_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + u_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + f_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + c_nd, _nt.Array[np.clongdouble])
assert_type(fld_nd + iu_nd, _nt.Array[np.longdouble])
assert_type(fld_nd + fc_nd, _nt.Array[np.longdouble | np.clongdouble])
assert_type(fld_nd + iufc_nd, _nt.Array[np.longdouble | np.clongdouble])

assert_type(fld_nd + b_py, _nt.Array[np.longdouble])
assert_type(fld_nd + i_py, _nt.Array[np.longdouble])
assert_type(fld_nd + f_py, _nt.Array[np.longdouble])
assert_type(fld_nd + c_py, _nt.Array[np.clongdouble])
fld_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + fld_nd, _nt.Array[np.longdouble])
assert_type(i_py + fld_nd, _nt.Array[np.longdouble])
assert_type(f_py + fld_nd, _nt.Array[np.longdouble])
assert_type(c_py + fld_nd, _nt.Array[np.clongdouble])
U_py + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8_nd + b1_nd, _nt.Array[np.complex64])
assert_type(c8_nd + i1_nd, _nt.Array[np.complex64])
assert_type(c8_nd + i2_nd, _nt.Array[np.complex64])
assert_type(c8_nd + i4_nd, _nt.Array[np.complex128])
assert_type(c8_nd + i8_nd, _nt.Array[np.complex128])
assert_type(c8_nd + u1_nd, _nt.Array[np.complex64])
assert_type(c8_nd + u2_nd, _nt.Array[np.complex64])
assert_type(c8_nd + u4_nd, _nt.Array[np.complex128])
assert_type(c8_nd + u8_nd, _nt.Array[np.complex128])
assert_type(c8_nd + f2_nd, _nt.Array[np.complex64])
assert_type(c8_nd + f4_nd, _nt.Array[np.complex64])
assert_type(c8_nd + f8_nd, _nt.Array[np.complex128])
assert_type(c8_nd + fld_nd, _nt.Array[np.clongdouble])
assert_type(c8_nd + c8_nd, _nt.Array[np.complex64])
assert_type(c8_nd + c16_nd, _nt.Array[np.complex128])
assert_type(c8_nd + cld_nd, _nt.Array[np.clongdouble])
c8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c8_nd + O_nd, _nt.Array[np.object_])
c8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c8_nd + i_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + u_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + f_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + iu_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + fc_nd, _nt.Array[np.complexfloating])
assert_type(c8_nd + iufc_nd, _nt.Array[np.complexfloating])

assert_type(c8_nd + b_py, _nt.Array[np.complex64])
assert_type(c8_nd + i_py, _nt.Array[np.complex64])
assert_type(c8_nd + f_py, _nt.Array[np.complex64])
assert_type(c8_nd + c_py, _nt.Array[np.complex64])
c8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + c8_nd, _nt.Array[np.complex64])
assert_type(i_py + c8_nd, _nt.Array[np.complex64])
assert_type(f_py + c8_nd, _nt.Array[np.complex64])
assert_type(c_py + c8_nd, _nt.Array[np.complex64])
U_py + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16_nd + b1_nd, _nt.Array[np.complex128])
assert_type(c16_nd + i1_nd, _nt.Array[np.complex128])
assert_type(c16_nd + i2_nd, _nt.Array[np.complex128])
assert_type(c16_nd + i4_nd, _nt.Array[np.complex128])
assert_type(c16_nd + i8_nd, _nt.Array[np.complex128])
assert_type(c16_nd + u1_nd, _nt.Array[np.complex128])
assert_type(c16_nd + u2_nd, _nt.Array[np.complex128])
assert_type(c16_nd + u4_nd, _nt.Array[np.complex128])
assert_type(c16_nd + u8_nd, _nt.Array[np.complex128])
assert_type(c16_nd + f2_nd, _nt.Array[np.complex128])
assert_type(c16_nd + f4_nd, _nt.Array[np.complex128])
assert_type(c16_nd + f8_nd, _nt.Array[np.complex128])
assert_type(c16_nd + fld_nd, _nt.Array[np.clongdouble])
assert_type(c16_nd + c8_nd, _nt.Array[np.complex128])
assert_type(c16_nd + c16_nd, _nt.Array[np.complex128])
assert_type(c16_nd + cld_nd, _nt.Array[np.clongdouble])
c16_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c16_nd + O_nd, _nt.Array[np.object_])
c16_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c16_nd + i_nd, _nt.Array[np.complex128])
assert_type(c16_nd + u_nd, _nt.Array[np.complex128])
assert_type(c16_nd + f_nd, _nt.Array[np.complexfloating])
assert_type(c16_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(c16_nd + iu_nd, _nt.Array[np.complex128])
assert_type(c16_nd + fc_nd, _nt.Array[np.complexfloating])
assert_type(c16_nd + iufc_nd, _nt.Array[np.complexfloating])

assert_type(c16_nd + b_py, _nt.Array[np.complex128])
assert_type(c16_nd + i_py, _nt.Array[np.complex128])
assert_type(c16_nd + f_py, _nt.Array[np.complex128])
assert_type(c16_nd + c_py, _nt.Array[np.complex128])
c16_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + c16_nd, _nt.Array[np.complex128])
assert_type(i_py + c16_nd, _nt.Array[np.complex128])
assert_type(f_py + c16_nd, _nt.Array[np.complex128])
assert_type(c_py + c16_nd, _nt.Array[np.complex128])
U_py + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld_nd + b1_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + i1_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + i2_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + i4_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + i8_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + u1_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + u2_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + u4_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + u8_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + f2_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + f4_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + f8_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + fld_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + c8_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + c16_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + cld_nd, _nt.Array[np.clongdouble])
cld_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(cld_nd + O_nd, _nt.Array[np.object_])
cld_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(cld_nd + i_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + u_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + f_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + c_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + iu_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + fc_nd, _nt.Array[np.clongdouble])
assert_type(cld_nd + iufc_nd, _nt.Array[np.clongdouble])

assert_type(cld_nd + b_py, _nt.Array[np.clongdouble])
assert_type(cld_nd + i_py, _nt.Array[np.clongdouble])
assert_type(cld_nd + f_py, _nt.Array[np.clongdouble])
assert_type(cld_nd + c_py, _nt.Array[np.clongdouble])
cld_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + cld_nd, _nt.Array[np.clongdouble])
assert_type(i_py + cld_nd, _nt.Array[np.clongdouble])
assert_type(f_py + cld_nd, _nt.Array[np.clongdouble])
assert_type(c_py + cld_nd, _nt.Array[np.clongdouble])
U_py + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8_nd + b1_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + i1_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + i2_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + i4_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + i8_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + u1_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + u2_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + u4_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + u8_nd, _nt.Array[np.datetime64])
M8_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd + m8_nd, _nt.Array[np.datetime64])
M8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd + i_nd, _nt.Array[np.datetime64])
assert_type(M8_nd + u_nd, _nt.Array[np.datetime64])
M8_nd + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd + iu_nd, _nt.Array[np.datetime64])
M8_nd + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8_nd + b_py, _nt.Array[np.datetime64])
assert_type(M8_nd + i_py, _nt.Array[np.datetime64])
M8_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + M8_nd, _nt.Array[np.datetime64])
assert_type(i_py + M8_nd, _nt.Array[np.datetime64])
f_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd + b1_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + i1_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + i2_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + i4_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + i8_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + u1_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + u2_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + u4_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + u8_nd, _nt.Array[np.timedelta64])
m8_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(m8_nd + m8_nd, _nt.Array[np.timedelta64])
m8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd + i_nd, _nt.Array[np.timedelta64])
assert_type(m8_nd + u_nd, _nt.Array[np.timedelta64])
m8_nd + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd + iu_nd, _nt.Array[np.timedelta64])
m8_nd + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd + b_py, _nt.Array[np.timedelta64])
assert_type(m8_nd + i_py, _nt.Array[np.timedelta64])
m8_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + m8_nd, _nt.Array[np.timedelta64])
assert_type(i_py + m8_nd, _nt.Array[np.timedelta64])
f_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(O_nd + b1_nd, _nt.Array[np.object_])
assert_type(O_nd + i1_nd, _nt.Array[np.object_])
assert_type(O_nd + i2_nd, _nt.Array[np.object_])
assert_type(O_nd + i4_nd, _nt.Array[np.object_])
assert_type(O_nd + i8_nd, _nt.Array[np.object_])
assert_type(O_nd + u1_nd, _nt.Array[np.object_])
assert_type(O_nd + u2_nd, _nt.Array[np.object_])
assert_type(O_nd + u4_nd, _nt.Array[np.object_])
assert_type(O_nd + u8_nd, _nt.Array[np.object_])
assert_type(O_nd + f2_nd, _nt.Array[np.object_])
assert_type(O_nd + f4_nd, _nt.Array[np.object_])
assert_type(O_nd + f8_nd, _nt.Array[np.object_])
assert_type(O_nd + fld_nd, _nt.Array[np.object_])
assert_type(O_nd + c8_nd, _nt.Array[np.object_])
assert_type(O_nd + c16_nd, _nt.Array[np.object_])
assert_type(O_nd + cld_nd, _nt.Array[np.object_])
assert_type(O_nd + O_nd, _nt.Array[np.object_])
assert_type(O_nd + S_nd, _nt.Array[np.object_])
assert_type(O_nd + U_nd, _nt.Array[np.object_])
assert_type(O_nd + i_nd, _nt.Array[np.object_])
assert_type(O_nd + u_nd, _nt.Array[np.object_])
assert_type(O_nd + f_nd, _nt.Array[np.object_])
assert_type(O_nd + c_nd, _nt.Array[np.object_])
assert_type(O_nd + iu_nd, _nt.Array[np.object_])
assert_type(O_nd + fc_nd, _nt.Array[np.object_])
assert_type(O_nd + iufc_nd, _nt.Array[np.object_])

assert_type(O_nd + b_py, _nt.Array[np.object_])
assert_type(O_nd + i_py, _nt.Array[np.object_])
assert_type(O_nd + f_py, _nt.Array[np.object_])
assert_type(O_nd + c_py, _nt.Array[np.object_])
assert_type(O_nd + S_py, _nt.Array[np.object_])
assert_type(O_nd + U_py, _nt.Array[np.object_])

assert_type(b_py + O_nd, _nt.Array[np.object_])
assert_type(i_py + O_nd, _nt.Array[np.object_])
assert_type(f_py + O_nd, _nt.Array[np.object_])
assert_type(c_py + O_nd, _nt.Array[np.object_])
assert_type(U_py + O_nd, _nt.Array[np.object_])

S_nd + b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(S_nd + O_nd, _nt.Array[np.object_])
assert_type(S_nd + S_nd, _nt.Array[np.bytes_])
S_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

S_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(S_nd + S_py, _nt.Array[np.bytes_])
S_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

b_py + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_py + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

U_nd + b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_nd + O_nd, _nt.Array[np.object_])
U_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_nd + U_nd, _nt.Array[np.str_])
assert_type(U_nd + T_nd, np.ndarray[_nt.Shape, np.dtypes.StringDType])
U_nd + i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

U_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_nd + U_py, _nt.Array[np.str_])

b_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_py + U_nd, _nt.Array[np.str_])

T_nd + b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(T_nd + U_nd, np.ndarray[_nt.Shape, np.dtypes.StringDType])
assert_type(T_nd + T_nd, np.ndarray[_nt.Shape, np.dtypes.StringDType])
T_nd + i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

T_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(T_nd + U_py, np.ndarray[_nt.Shape, np.dtypes.StringDType])

b_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_py + T_nd, np.ndarray[_nt.Shape, np.dtypes.StringDType])

assert_type(i_nd + b1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + i1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + i2_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + i4_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + i8_nd, _nt.Array[np.int64])
assert_type(i_nd + u1_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + u2_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + u4_nd, _nt.Array[np.int64])
assert_type(i_nd + u8_nd, _nt.Array[np.float64])
assert_type(i_nd + f2_nd, _nt.Array[np.floating])
assert_type(i_nd + f4_nd, _nt.Array[np.floating])
assert_type(i_nd + f8_nd, _nt.Array[np.float64])
assert_type(i_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(i_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(i_nd + c16_nd, _nt.Array[np.complex128])
assert_type(i_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(i_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(i_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(i_nd + O_nd, _nt.Array[np.object_])
i_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i_nd + i_nd, _nt.Array[np.signedinteger])
assert_type(i_nd + u_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i_nd + f_nd, _nt.Array[np.floating])
assert_type(i_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(i_nd + iu_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(i_nd + fc_nd, _nt.Array[np.inexact])
assert_type(i_nd + iufc_nd, _nt.Array[np.number])

assert_type(i_nd + b_py, _nt.Array[np.signedinteger])
assert_type(i_nd + i_py, _nt.Array[np.signedinteger])
assert_type(i_nd + f_py, _nt.Array[np.float64])
assert_type(i_nd + c_py, _nt.Array[np.complex128])
i_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i_nd, _nt.Array[np.signedinteger])
assert_type(i_py + i_nd, _nt.Array[np.signedinteger])
assert_type(f_py + i_nd, _nt.Array[np.float64])
assert_type(c_py + i_nd, _nt.Array[np.complex128])
U_py + i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u_nd + b1_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd + i1_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd + i2_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd + i4_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd + i8_nd, _nt.Array[np.int64 | np.float64])
assert_type(u_nd + u1_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd + u2_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd + u4_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd + u8_nd, _nt.Array[np.uint64])
assert_type(u_nd + f2_nd, _nt.Array[np.floating])
assert_type(u_nd + f4_nd, _nt.Array[np.floating])
assert_type(u_nd + f8_nd, _nt.Array[np.float64])
assert_type(u_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(u_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(u_nd + c16_nd, _nt.Array[np.complex128])
assert_type(u_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(u_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(u_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(u_nd + O_nd, _nt.Array[np.object_])
u_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u_nd + i_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(u_nd + u_nd, _nt.Array[np.unsignedinteger])
assert_type(u_nd + f_nd, _nt.Array[np.floating])
assert_type(u_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(u_nd + iu_nd, _nt.Array[np.integer | np.float64])
assert_type(u_nd + fc_nd, _nt.Array[np.inexact])
assert_type(u_nd + iufc_nd, _nt.Array[np.number])

assert_type(u_nd + b_py, _nt.Array[np.unsignedinteger])
assert_type(u_nd + i_py, _nt.Array[np.unsignedinteger])
assert_type(u_nd + f_py, _nt.Array[np.float64])
assert_type(u_nd + c_py, _nt.Array[np.complex128])
u_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u_nd, _nt.Array[np.unsignedinteger])
assert_type(i_py + u_nd, _nt.Array[np.unsignedinteger])
assert_type(f_py + u_nd, _nt.Array[np.float64])
assert_type(c_py + u_nd, _nt.Array[np.complex128])
U_py + u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f_nd + b1_nd, _nt.Array[np.floating])
assert_type(f_nd + i1_nd, _nt.Array[np.floating])
assert_type(f_nd + i2_nd, _nt.Array[np.floating])
assert_type(f_nd + i4_nd, _nt.Array[np.floating])
assert_type(f_nd + i8_nd, _nt.Array[np.floating])
assert_type(f_nd + u1_nd, _nt.Array[np.floating])
assert_type(f_nd + u2_nd, _nt.Array[np.floating])
assert_type(f_nd + u4_nd, _nt.Array[np.floating])
assert_type(f_nd + u8_nd, _nt.Array[np.floating])
assert_type(f_nd + f2_nd, _nt.Array[np.floating])
assert_type(f_nd + f4_nd, _nt.Array[np.floating])
assert_type(f_nd + f8_nd, _nt.Array[np.floating])
assert_type(f_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(f_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(f_nd + c16_nd, _nt.Array[np.complexfloating])
assert_type(f_nd + cld_nd, _nt.Array[np.clongdouble])
f_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f_nd + O_nd, _nt.Array[np.object_])
f_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f_nd + i_nd, _nt.Array[np.floating])
assert_type(f_nd + u_nd, _nt.Array[np.floating])
assert_type(f_nd + f_nd, _nt.Array[np.floating])
assert_type(f_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(f_nd + iu_nd, _nt.Array[np.floating])
assert_type(f_nd + fc_nd, _nt.Array[np.inexact])
assert_type(f_nd + iufc_nd, _nt.Array[np.inexact])

assert_type(f_nd + b_py, _nt.Array[np.floating])
assert_type(f_nd + i_py, _nt.Array[np.floating])
assert_type(f_nd + f_py, _nt.Array[np.floating])
assert_type(f_nd + c_py, _nt.Array[np.complexfloating])
f_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f_nd, _nt.Array[np.floating])
assert_type(i_py + f_nd, _nt.Array[np.floating])
assert_type(f_py + f_nd, _nt.Array[np.floating])
assert_type(c_py + f_nd, _nt.Array[np.complexfloating])
U_py + f_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c_nd + b1_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + i1_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + i2_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + i4_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + i8_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + u1_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + u2_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + u4_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + u8_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + f2_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + f4_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + f8_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + fld_nd, _nt.Array[np.clongdouble])
assert_type(c_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + c16_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + cld_nd, _nt.Array[np.clongdouble])
c_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c_nd + O_nd, _nt.Array[np.object_])
c_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c_nd + i_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + u_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + f_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + iu_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + fc_nd, _nt.Array[np.complexfloating])
assert_type(c_nd + iufc_nd, _nt.Array[np.complexfloating])

assert_type(c_nd + b_py, _nt.Array[np.complexfloating])
assert_type(c_nd + i_py, _nt.Array[np.complexfloating])
assert_type(c_nd + f_py, _nt.Array[np.complexfloating])
assert_type(c_nd + c_py, _nt.Array[np.complexfloating])
c_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + c_nd, _nt.Array[np.complexfloating])
assert_type(i_py + c_nd, _nt.Array[np.complexfloating])
assert_type(f_py + c_nd, _nt.Array[np.complexfloating])
assert_type(c_py + c_nd, _nt.Array[np.complexfloating])
U_py + c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu_nd + b1_nd, _nt.Array[np.integer])
assert_type(iu_nd + i1_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd + i2_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd + i4_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd + i8_nd, _nt.Array[np.int64 | np.float64])
assert_type(iu_nd + u1_nd, _nt.Array[np.integer])
assert_type(iu_nd + u2_nd, _nt.Array[np.integer])
assert_type(iu_nd + u4_nd, _nt.Array[np.integer])
assert_type(iu_nd + u8_nd, _nt.Array[np.uint64 | np.float64])
assert_type(iu_nd + f2_nd, _nt.Array[np.floating])
assert_type(iu_nd + f4_nd, _nt.Array[np.floating])
assert_type(iu_nd + f8_nd, _nt.Array[np.float64])
assert_type(iu_nd + fld_nd, _nt.Array[np.longdouble])
assert_type(iu_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(iu_nd + c16_nd, _nt.Array[np.complex128])
assert_type(iu_nd + cld_nd, _nt.Array[np.clongdouble])
assert_type(iu_nd + M8_nd, _nt.Array[np.datetime64])
assert_type(iu_nd + m8_nd, _nt.Array[np.timedelta64])
assert_type(iu_nd + O_nd, _nt.Array[np.object_])
iu_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu_nd + i_nd, _nt.Array[np.signedinteger | np.float64])
assert_type(iu_nd + u_nd, _nt.Array[np.integer | np.float64])
assert_type(iu_nd + f_nd, _nt.Array[np.floating])
assert_type(iu_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(iu_nd + iu_nd, _nt.Array[np.integer | np.float64])
assert_type(iu_nd + fc_nd, _nt.Array[np.inexact])
assert_type(iu_nd + iufc_nd, _nt.Array[np.number])

assert_type(iu_nd + b_py, _nt.Array[np.integer])
assert_type(iu_nd + i_py, _nt.Array[np.integer])
assert_type(iu_nd + f_py, _nt.Array[np.float64])
assert_type(iu_nd + c_py, _nt.Array[np.complex128])
iu_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + iu_nd, _nt.Array[np.integer])
assert_type(i_py + iu_nd, _nt.Array[np.integer])
assert_type(f_py + iu_nd, _nt.Array[np.float64])
assert_type(c_py + iu_nd, _nt.Array[np.complex128])
U_py + iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(fc_nd + b1_nd, _nt.Array[np.inexact])
assert_type(fc_nd + i1_nd, _nt.Array[np.inexact])
assert_type(fc_nd + i2_nd, _nt.Array[np.inexact])
assert_type(fc_nd + i4_nd, _nt.Array[np.inexact])
assert_type(fc_nd + i8_nd, _nt.Array[np.inexact])
assert_type(fc_nd + u1_nd, _nt.Array[np.inexact])
assert_type(fc_nd + u2_nd, _nt.Array[np.inexact])
assert_type(fc_nd + u4_nd, _nt.Array[np.inexact])
assert_type(fc_nd + u8_nd, _nt.Array[np.inexact])
assert_type(fc_nd + f2_nd, _nt.Array[np.inexact])
assert_type(fc_nd + f4_nd, _nt.Array[np.inexact])
assert_type(fc_nd + f8_nd, _nt.Array[np.inexact])
assert_type(fc_nd + fld_nd, _nt.Array[np.longdouble | np.clongdouble])
assert_type(fc_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(fc_nd + c16_nd, _nt.Array[np.complexfloating])
assert_type(fc_nd + cld_nd, _nt.Array[np.clongdouble])
fc_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fc_nd + O_nd, _nt.Array[np.object_])
fc_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fc_nd + i_nd, _nt.Array[np.inexact])
assert_type(fc_nd + u_nd, _nt.Array[np.inexact])
assert_type(fc_nd + f_nd, _nt.Array[np.inexact])
assert_type(fc_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(fc_nd + iu_nd, _nt.Array[np.inexact])
assert_type(fc_nd + fc_nd, _nt.Array[np.inexact])
assert_type(fc_nd + iufc_nd, _nt.Array[np.inexact])

assert_type(fc_nd + b_py, _nt.Array[np.inexact])
assert_type(fc_nd + i_py, _nt.Array[np.inexact])
assert_type(fc_nd + f_py, _nt.Array[np.inexact])
assert_type(fc_nd + c_py, _nt.Array[np.complexfloating])
fc_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fc_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + fc_nd, _nt.Array[np.inexact])
assert_type(i_py + fc_nd, _nt.Array[np.inexact])
assert_type(f_py + fc_nd, _nt.Array[np.inexact])
assert_type(c_py + fc_nd, _nt.Array[np.complexfloating])
U_py + fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iufc_nd + b1_nd, _nt.Array[np.number])
assert_type(iufc_nd + i1_nd, _nt.Array[np.number])
assert_type(iufc_nd + i2_nd, _nt.Array[np.number])
assert_type(iufc_nd + i4_nd, _nt.Array[np.number])
assert_type(iufc_nd + i8_nd, _nt.Array[np.number])
assert_type(iufc_nd + u1_nd, _nt.Array[np.number])
assert_type(iufc_nd + u2_nd, _nt.Array[np.number])
assert_type(iufc_nd + u4_nd, _nt.Array[np.number])
assert_type(iufc_nd + u8_nd, _nt.Array[np.number])
assert_type(iufc_nd + f2_nd, _nt.Array[np.inexact])
assert_type(iufc_nd + f4_nd, _nt.Array[np.inexact])
assert_type(iufc_nd + f8_nd, _nt.Array[np.inexact])
assert_type(iufc_nd + fld_nd, _nt.Array[np.longdouble | np.clongdouble])
assert_type(iufc_nd + c8_nd, _nt.Array[np.complexfloating])
assert_type(iufc_nd + c16_nd, _nt.Array[np.complexfloating])
assert_type(iufc_nd + cld_nd, _nt.Array[np.clongdouble])
iufc_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iufc_nd + O_nd, _nt.Array[np.object_])
iufc_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iufc_nd + i_nd, _nt.Array[np.number])
assert_type(iufc_nd + u_nd, _nt.Array[np.number])
assert_type(iufc_nd + f_nd, _nt.Array[np.inexact])
assert_type(iufc_nd + c_nd, _nt.Array[np.complexfloating])
assert_type(iufc_nd + iu_nd, _nt.Array[np.number])
assert_type(iufc_nd + fc_nd, _nt.Array[np.inexact])
assert_type(iufc_nd + iufc_nd, _nt.Array[np.number])

assert_type(iufc_nd + b_py, _nt.Array[np.number])
assert_type(iufc_nd + i_py, _nt.Array[np.number])
assert_type(iufc_nd + f_py, _nt.Array[np.inexact])
assert_type(iufc_nd + c_py, _nt.Array[np.complexfloating])
iufc_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iufc_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + iufc_nd, _nt.Array[np.number])
assert_type(i_py + iufc_nd, _nt.Array[np.number])
assert_type(f_py + iufc_nd, _nt.Array[np.inexact])
assert_type(c_py + iufc_nd, _nt.Array[np.complexfloating])
U_py + iufc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
