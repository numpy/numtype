# @generated 2025-04-13T21:19:18Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

b1_nd: npt.NDArray[np.bool]
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
S_nd: npt.NDArray[np.bytes_]
U_nd: npt.NDArray[np.str_]
T_nd: np.ndarray[tuple[int, ...], np.dtypes.StringDType]

b_py: bool
i_py: int
f_py: float
c_py: complex
S_py: bytes
U_py: str

###

assert_type(b1_nd + b1_nd, npt.NDArray[np.bool])
assert_type(b1_nd + i1_nd, npt.NDArray[np.int8])
assert_type(b1_nd + i2_nd, npt.NDArray[np.int16])
assert_type(b1_nd + i4_nd, npt.NDArray[np.int32])
assert_type(b1_nd + i8_nd, npt.NDArray[np.int64])
assert_type(b1_nd + u1_nd, npt.NDArray[np.uint8])
assert_type(b1_nd + u2_nd, npt.NDArray[np.uint16])
assert_type(b1_nd + u4_nd, npt.NDArray[np.uint32])
assert_type(b1_nd + u8_nd, npt.NDArray[np.uint64])
assert_type(b1_nd + f2_nd, npt.NDArray[np.float16])
assert_type(b1_nd + f4_nd, npt.NDArray[np.float32])
assert_type(b1_nd + f8_nd, npt.NDArray[np.float64])
assert_type(b1_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(b1_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(b1_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(b1_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(b1_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(b1_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(b1_nd + O_nd, npt.NDArray[np.object_])
b1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b1_nd + b_py, npt.NDArray[np.bool])
assert_type(b1_nd + i_py, npt.NDArray[np.int64])
assert_type(b1_nd + f_py, npt.NDArray[np.float64])
assert_type(b1_nd + c_py, npt.NDArray[np.complex128])
b1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
b1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + b1_nd, npt.NDArray[np.bool])
assert_type(i_py + b1_nd, npt.NDArray[np.int64])
assert_type(f_py + b1_nd, npt.NDArray[np.float64])
assert_type(c_py + b1_nd, npt.NDArray[np.complex128])
U_py + b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1_nd + b1_nd, npt.NDArray[np.int8])
assert_type(i1_nd + i1_nd, npt.NDArray[np.int8])
assert_type(i1_nd + i2_nd, npt.NDArray[np.int16])
assert_type(i1_nd + i4_nd, npt.NDArray[np.int32])
assert_type(i1_nd + i8_nd, npt.NDArray[np.int64])
assert_type(i1_nd + u1_nd, npt.NDArray[np.int16])
assert_type(i1_nd + u2_nd, npt.NDArray[np.int32])
assert_type(i1_nd + u4_nd, npt.NDArray[np.int64])
assert_type(i1_nd + u8_nd, npt.NDArray[np.float64])
assert_type(i1_nd + f2_nd, npt.NDArray[np.float16])
assert_type(i1_nd + f4_nd, npt.NDArray[np.float32])
assert_type(i1_nd + f8_nd, npt.NDArray[np.float64])
assert_type(i1_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(i1_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(i1_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(i1_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(i1_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(i1_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(i1_nd + O_nd, npt.NDArray[np.object_])
i1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1_nd + b_py, npt.NDArray[np.int8])
assert_type(i1_nd + i_py, npt.NDArray[np.int8])
assert_type(i1_nd + f_py, npt.NDArray[np.float64])
assert_type(i1_nd + c_py, npt.NDArray[np.complex128])
i1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i1_nd, npt.NDArray[np.int8])
assert_type(i_py + i1_nd, npt.NDArray[np.int8])
assert_type(f_py + i1_nd, npt.NDArray[np.float64])
assert_type(c_py + i1_nd, npt.NDArray[np.complex128])
U_py + i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2_nd + b1_nd, npt.NDArray[np.int16])
assert_type(i2_nd + i1_nd, npt.NDArray[np.int16])
assert_type(i2_nd + i2_nd, npt.NDArray[np.int16])
assert_type(i2_nd + i4_nd, npt.NDArray[np.int32])
assert_type(i2_nd + i8_nd, npt.NDArray[np.int64])
assert_type(i2_nd + u1_nd, npt.NDArray[np.int16])
assert_type(i2_nd + u2_nd, npt.NDArray[np.int32])
assert_type(i2_nd + u4_nd, npt.NDArray[np.int64])
assert_type(i2_nd + u8_nd, npt.NDArray[np.float64])
assert_type(i2_nd + f2_nd, npt.NDArray[np.float32])
assert_type(i2_nd + f4_nd, npt.NDArray[np.float32])
assert_type(i2_nd + f8_nd, npt.NDArray[np.float64])
assert_type(i2_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(i2_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(i2_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(i2_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(i2_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(i2_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(i2_nd + O_nd, npt.NDArray[np.object_])
i2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2_nd + b_py, npt.NDArray[np.int16])
assert_type(i2_nd + i_py, npt.NDArray[np.int16])
assert_type(i2_nd + f_py, npt.NDArray[np.float64])
assert_type(i2_nd + c_py, npt.NDArray[np.complex128])
i2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i2_nd, npt.NDArray[np.int16])
assert_type(i_py + i2_nd, npt.NDArray[np.int16])
assert_type(f_py + i2_nd, npt.NDArray[np.float64])
assert_type(c_py + i2_nd, npt.NDArray[np.complex128])
U_py + i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4_nd + b1_nd, npt.NDArray[np.int32])
assert_type(i4_nd + i1_nd, npt.NDArray[np.int32])
assert_type(i4_nd + i2_nd, npt.NDArray[np.int32])
assert_type(i4_nd + i4_nd, npt.NDArray[np.int32])
assert_type(i4_nd + i8_nd, npt.NDArray[np.int64])
assert_type(i4_nd + u1_nd, npt.NDArray[np.int32])
assert_type(i4_nd + u2_nd, npt.NDArray[np.int32])
assert_type(i4_nd + u4_nd, npt.NDArray[np.int64])
assert_type(i4_nd + u8_nd, npt.NDArray[np.float64])
assert_type(i4_nd + f2_nd, npt.NDArray[np.float64])
assert_type(i4_nd + f4_nd, npt.NDArray[np.float64])
assert_type(i4_nd + f8_nd, npt.NDArray[np.float64])
assert_type(i4_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(i4_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(i4_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(i4_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(i4_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(i4_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(i4_nd + O_nd, npt.NDArray[np.object_])
i4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4_nd + b_py, npt.NDArray[np.int32])
assert_type(i4_nd + i_py, npt.NDArray[np.int32])
assert_type(i4_nd + f_py, npt.NDArray[np.float64])
assert_type(i4_nd + c_py, npt.NDArray[np.complex128])
i4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i4_nd, npt.NDArray[np.int32])
assert_type(i_py + i4_nd, npt.NDArray[np.int32])
assert_type(f_py + i4_nd, npt.NDArray[np.float64])
assert_type(c_py + i4_nd, npt.NDArray[np.complex128])
U_py + i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8_nd + b1_nd, npt.NDArray[np.int64])
assert_type(i8_nd + i1_nd, npt.NDArray[np.int64])
assert_type(i8_nd + i2_nd, npt.NDArray[np.int64])
assert_type(i8_nd + i4_nd, npt.NDArray[np.int64])
assert_type(i8_nd + i8_nd, npt.NDArray[np.int64])
assert_type(i8_nd + u1_nd, npt.NDArray[np.int64])
assert_type(i8_nd + u2_nd, npt.NDArray[np.int64])
assert_type(i8_nd + u4_nd, npt.NDArray[np.int64])
assert_type(i8_nd + u8_nd, npt.NDArray[np.float64])
assert_type(i8_nd + f2_nd, npt.NDArray[np.float64])
assert_type(i8_nd + f4_nd, npt.NDArray[np.float64])
assert_type(i8_nd + f8_nd, npt.NDArray[np.float64])
assert_type(i8_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(i8_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(i8_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(i8_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(i8_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(i8_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(i8_nd + O_nd, npt.NDArray[np.object_])
i8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8_nd + b_py, npt.NDArray[np.int64])
assert_type(i8_nd + i_py, npt.NDArray[np.int64])
assert_type(i8_nd + f_py, npt.NDArray[np.float64])
assert_type(i8_nd + c_py, npt.NDArray[np.complex128])
i8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + i8_nd, npt.NDArray[np.int64])
assert_type(i_py + i8_nd, npt.NDArray[np.int64])
assert_type(f_py + i8_nd, npt.NDArray[np.float64])
assert_type(c_py + i8_nd, npt.NDArray[np.complex128])
U_py + i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1_nd + b1_nd, npt.NDArray[np.uint8])
assert_type(u1_nd + i1_nd, npt.NDArray[np.int16])
assert_type(u1_nd + i2_nd, npt.NDArray[np.int16])
assert_type(u1_nd + i4_nd, npt.NDArray[np.int32])
assert_type(u1_nd + i8_nd, npt.NDArray[np.int64])
assert_type(u1_nd + u1_nd, npt.NDArray[np.uint8])
assert_type(u1_nd + u2_nd, npt.NDArray[np.uint16])
assert_type(u1_nd + u4_nd, npt.NDArray[np.uint32])
assert_type(u1_nd + u8_nd, npt.NDArray[np.uint64])
assert_type(u1_nd + f2_nd, npt.NDArray[np.float16])
assert_type(u1_nd + f4_nd, npt.NDArray[np.float32])
assert_type(u1_nd + f8_nd, npt.NDArray[np.float64])
assert_type(u1_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(u1_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(u1_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(u1_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(u1_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(u1_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(u1_nd + O_nd, npt.NDArray[np.object_])
u1_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u1_nd + b_py, npt.NDArray[np.uint8])
assert_type(u1_nd + i_py, npt.NDArray[np.uint8])
assert_type(u1_nd + f_py, npt.NDArray[np.float64])
assert_type(u1_nd + c_py, npt.NDArray[np.complex128])
u1_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u1_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u1_nd, npt.NDArray[np.uint8])
assert_type(i_py + u1_nd, npt.NDArray[np.uint8])
assert_type(f_py + u1_nd, npt.NDArray[np.float64])
assert_type(c_py + u1_nd, npt.NDArray[np.complex128])
U_py + u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2_nd + b1_nd, npt.NDArray[np.uint16])
assert_type(u2_nd + i1_nd, npt.NDArray[np.int32])
assert_type(u2_nd + i2_nd, npt.NDArray[np.int32])
assert_type(u2_nd + i4_nd, npt.NDArray[np.int32])
assert_type(u2_nd + i8_nd, npt.NDArray[np.int64])
assert_type(u2_nd + u1_nd, npt.NDArray[np.uint16])
assert_type(u2_nd + u2_nd, npt.NDArray[np.uint16])
assert_type(u2_nd + u4_nd, npt.NDArray[np.uint32])
assert_type(u2_nd + u8_nd, npt.NDArray[np.uint64])
assert_type(u2_nd + f2_nd, npt.NDArray[np.float32])
assert_type(u2_nd + f4_nd, npt.NDArray[np.float32])
assert_type(u2_nd + f8_nd, npt.NDArray[np.float64])
assert_type(u2_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(u2_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(u2_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(u2_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(u2_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(u2_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(u2_nd + O_nd, npt.NDArray[np.object_])
u2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u2_nd + b_py, npt.NDArray[np.uint16])
assert_type(u2_nd + i_py, npt.NDArray[np.uint16])
assert_type(u2_nd + f_py, npt.NDArray[np.float64])
assert_type(u2_nd + c_py, npt.NDArray[np.complex128])
u2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u2_nd, npt.NDArray[np.uint16])
assert_type(i_py + u2_nd, npt.NDArray[np.uint16])
assert_type(f_py + u2_nd, npt.NDArray[np.float64])
assert_type(c_py + u2_nd, npt.NDArray[np.complex128])
U_py + u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4_nd + b1_nd, npt.NDArray[np.uint32])
assert_type(u4_nd + i1_nd, npt.NDArray[np.int64])
assert_type(u4_nd + i2_nd, npt.NDArray[np.int64])
assert_type(u4_nd + i4_nd, npt.NDArray[np.int64])
assert_type(u4_nd + i8_nd, npt.NDArray[np.int64])
assert_type(u4_nd + u1_nd, npt.NDArray[np.uint32])
assert_type(u4_nd + u2_nd, npt.NDArray[np.uint32])
assert_type(u4_nd + u4_nd, npt.NDArray[np.uint32])
assert_type(u4_nd + u8_nd, npt.NDArray[np.uint64])
assert_type(u4_nd + f2_nd, npt.NDArray[np.float64])
assert_type(u4_nd + f4_nd, npt.NDArray[np.float64])
assert_type(u4_nd + f8_nd, npt.NDArray[np.float64])
assert_type(u4_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(u4_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(u4_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(u4_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(u4_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(u4_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(u4_nd + O_nd, npt.NDArray[np.object_])
u4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u4_nd + b_py, npt.NDArray[np.uint32])
assert_type(u4_nd + i_py, npt.NDArray[np.uint32])
assert_type(u4_nd + f_py, npt.NDArray[np.float64])
assert_type(u4_nd + c_py, npt.NDArray[np.complex128])
u4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u4_nd, npt.NDArray[np.uint32])
assert_type(i_py + u4_nd, npt.NDArray[np.uint32])
assert_type(f_py + u4_nd, npt.NDArray[np.float64])
assert_type(c_py + u4_nd, npt.NDArray[np.complex128])
U_py + u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8_nd + b1_nd, npt.NDArray[np.uint64])
assert_type(u8_nd + i1_nd, npt.NDArray[np.float64])
assert_type(u8_nd + i2_nd, npt.NDArray[np.float64])
assert_type(u8_nd + i4_nd, npt.NDArray[np.float64])
assert_type(u8_nd + i8_nd, npt.NDArray[np.float64])
assert_type(u8_nd + u1_nd, npt.NDArray[np.uint64])
assert_type(u8_nd + u2_nd, npt.NDArray[np.uint64])
assert_type(u8_nd + u4_nd, npt.NDArray[np.uint64])
assert_type(u8_nd + u8_nd, npt.NDArray[np.uint64])
assert_type(u8_nd + f2_nd, npt.NDArray[np.float64])
assert_type(u8_nd + f4_nd, npt.NDArray[np.float64])
assert_type(u8_nd + f8_nd, npt.NDArray[np.float64])
assert_type(u8_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(u8_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(u8_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(u8_nd + cld_nd, npt.NDArray[np.clongdouble])
assert_type(u8_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(u8_nd + m8_nd, npt.NDArray[np.timedelta64])
assert_type(u8_nd + O_nd, npt.NDArray[np.object_])
u8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8_nd + b_py, npt.NDArray[np.uint64])
assert_type(u8_nd + i_py, npt.NDArray[np.uint64])
assert_type(u8_nd + f_py, npt.NDArray[np.float64])
assert_type(u8_nd + c_py, npt.NDArray[np.complex128])
u8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + u8_nd, npt.NDArray[np.uint64])
assert_type(i_py + u8_nd, npt.NDArray[np.uint64])
assert_type(f_py + u8_nd, npt.NDArray[np.float64])
assert_type(c_py + u8_nd, npt.NDArray[np.complex128])
U_py + u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2_nd + b1_nd, npt.NDArray[np.float16])
assert_type(f2_nd + i1_nd, npt.NDArray[np.float16])
assert_type(f2_nd + i2_nd, npt.NDArray[np.float32])
assert_type(f2_nd + i4_nd, npt.NDArray[np.float64])
assert_type(f2_nd + i8_nd, npt.NDArray[np.float64])
assert_type(f2_nd + u1_nd, npt.NDArray[np.float16])
assert_type(f2_nd + u2_nd, npt.NDArray[np.float32])
assert_type(f2_nd + u4_nd, npt.NDArray[np.float64])
assert_type(f2_nd + u8_nd, npt.NDArray[np.float64])
assert_type(f2_nd + f2_nd, npt.NDArray[np.float16])
assert_type(f2_nd + f4_nd, npt.NDArray[np.float32])
assert_type(f2_nd + f8_nd, npt.NDArray[np.float64])
assert_type(f2_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(f2_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(f2_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(f2_nd + cld_nd, npt.NDArray[np.clongdouble])
f2_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd + O_nd, npt.NDArray[np.object_])
f2_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f2_nd + b_py, npt.NDArray[np.float16])
assert_type(f2_nd + i_py, npt.NDArray[np.float16])
assert_type(f2_nd + f_py, npt.NDArray[np.float16])
assert_type(f2_nd + c_py, npt.NDArray[np.complex64])
f2_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f2_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f2_nd, npt.NDArray[np.float16])
assert_type(i_py + f2_nd, npt.NDArray[np.float16])
assert_type(f_py + f2_nd, npt.NDArray[np.float16])
assert_type(c_py + f2_nd, npt.NDArray[np.complex64])
U_py + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4_nd + b1_nd, npt.NDArray[np.float32])
assert_type(f4_nd + i1_nd, npt.NDArray[np.float32])
assert_type(f4_nd + i2_nd, npt.NDArray[np.float32])
assert_type(f4_nd + i4_nd, npt.NDArray[np.float64])
assert_type(f4_nd + i8_nd, npt.NDArray[np.float64])
assert_type(f4_nd + u1_nd, npt.NDArray[np.float32])
assert_type(f4_nd + u2_nd, npt.NDArray[np.float32])
assert_type(f4_nd + u4_nd, npt.NDArray[np.float64])
assert_type(f4_nd + u8_nd, npt.NDArray[np.float64])
assert_type(f4_nd + f2_nd, npt.NDArray[np.float32])
assert_type(f4_nd + f4_nd, npt.NDArray[np.float32])
assert_type(f4_nd + f8_nd, npt.NDArray[np.float64])
assert_type(f4_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(f4_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(f4_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(f4_nd + cld_nd, npt.NDArray[np.clongdouble])
f4_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd + O_nd, npt.NDArray[np.object_])
f4_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f4_nd + b_py, npt.NDArray[np.float32])
assert_type(f4_nd + i_py, npt.NDArray[np.float32])
assert_type(f4_nd + f_py, npt.NDArray[np.float32])
assert_type(f4_nd + c_py, npt.NDArray[np.complex64])
f4_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f4_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f4_nd, npt.NDArray[np.float32])
assert_type(i_py + f4_nd, npt.NDArray[np.float32])
assert_type(f_py + f4_nd, npt.NDArray[np.float32])
assert_type(c_py + f4_nd, npt.NDArray[np.complex64])
U_py + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8_nd + b1_nd, npt.NDArray[np.float64])
assert_type(f8_nd + i1_nd, npt.NDArray[np.float64])
assert_type(f8_nd + i2_nd, npt.NDArray[np.float64])
assert_type(f8_nd + i4_nd, npt.NDArray[np.float64])
assert_type(f8_nd + i8_nd, npt.NDArray[np.float64])
assert_type(f8_nd + u1_nd, npt.NDArray[np.float64])
assert_type(f8_nd + u2_nd, npt.NDArray[np.float64])
assert_type(f8_nd + u4_nd, npt.NDArray[np.float64])
assert_type(f8_nd + u8_nd, npt.NDArray[np.float64])
assert_type(f8_nd + f2_nd, npt.NDArray[np.float64])
assert_type(f8_nd + f4_nd, npt.NDArray[np.float64])
assert_type(f8_nd + f8_nd, npt.NDArray[np.float64])
assert_type(f8_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(f8_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(f8_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(f8_nd + cld_nd, npt.NDArray[np.clongdouble])
f8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd + O_nd, npt.NDArray[np.object_])
f8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(f8_nd + b_py, npt.NDArray[np.float64])
assert_type(f8_nd + i_py, npt.NDArray[np.float64])
assert_type(f8_nd + f_py, npt.NDArray[np.float64])
assert_type(f8_nd + c_py, npt.NDArray[np.complex128])
f8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + f8_nd, npt.NDArray[np.float64])
assert_type(i_py + f8_nd, npt.NDArray[np.float64])
assert_type(f_py + f8_nd, npt.NDArray[np.float64])
assert_type(c_py + f8_nd, npt.NDArray[np.complex128])
U_py + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(fld_nd + b1_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + i1_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + i2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + i4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + i8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + u1_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + u2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + u4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + u8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + f2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + f4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + f8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + fld_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd + c8_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd + c16_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd + cld_nd, npt.NDArray[np.clongdouble])
fld_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd + O_nd, npt.NDArray[np.object_])
fld_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(fld_nd + b_py, npt.NDArray[np.longdouble])
assert_type(fld_nd + i_py, npt.NDArray[np.longdouble])
assert_type(fld_nd + f_py, npt.NDArray[np.longdouble])
assert_type(fld_nd + c_py, npt.NDArray[np.clongdouble])
fld_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
fld_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + fld_nd, npt.NDArray[np.longdouble])
assert_type(i_py + fld_nd, npt.NDArray[np.longdouble])
assert_type(f_py + fld_nd, npt.NDArray[np.longdouble])
assert_type(c_py + fld_nd, npt.NDArray[np.clongdouble])
U_py + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8_nd + b1_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + i1_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + i2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + i4_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + i8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + u1_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + u2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + u4_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + u8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + f2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + f4_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + f8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + fld_nd, npt.NDArray[np.clongdouble])
assert_type(c8_nd + c8_nd, npt.NDArray[np.complex64])
assert_type(c8_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(c8_nd + cld_nd, npt.NDArray[np.clongdouble])
c8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c8_nd + O_nd, npt.NDArray[np.object_])
c8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c8_nd + b_py, npt.NDArray[np.complex64])
assert_type(c8_nd + i_py, npt.NDArray[np.complex64])
assert_type(c8_nd + f_py, npt.NDArray[np.complex64])
assert_type(c8_nd + c_py, npt.NDArray[np.complex64])
c8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + c8_nd, npt.NDArray[np.complex64])
assert_type(i_py + c8_nd, npt.NDArray[np.complex64])
assert_type(f_py + c8_nd, npt.NDArray[np.complex64])
assert_type(c_py + c8_nd, npt.NDArray[np.complex64])
U_py + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16_nd + b1_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + i1_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + i2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + i4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + i8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + u1_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + u2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + u4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + u8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + f2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + f4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + f8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + fld_nd, npt.NDArray[np.clongdouble])
assert_type(c16_nd + c8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + c16_nd, npt.NDArray[np.complex128])
assert_type(c16_nd + cld_nd, npt.NDArray[np.clongdouble])
c16_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c16_nd + O_nd, npt.NDArray[np.object_])
c16_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(c16_nd + b_py, npt.NDArray[np.complex128])
assert_type(c16_nd + i_py, npt.NDArray[np.complex128])
assert_type(c16_nd + f_py, npt.NDArray[np.complex128])
assert_type(c16_nd + c_py, npt.NDArray[np.complex128])
c16_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c16_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + c16_nd, npt.NDArray[np.complex128])
assert_type(i_py + c16_nd, npt.NDArray[np.complex128])
assert_type(f_py + c16_nd, npt.NDArray[np.complex128])
assert_type(c_py + c16_nd, npt.NDArray[np.complex128])
U_py + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld_nd + b1_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + i1_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + i2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + i4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + i8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + u1_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + u2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + u4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + u8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + f2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + f4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + f8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + fld_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + c8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + c16_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd + cld_nd, npt.NDArray[np.clongdouble])
cld_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(cld_nd + O_nd, npt.NDArray[np.object_])
cld_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(cld_nd + b_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd + i_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd + f_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd + c_py, npt.NDArray[np.clongdouble])
cld_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
cld_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + cld_nd, npt.NDArray[np.clongdouble])
assert_type(i_py + cld_nd, npt.NDArray[np.clongdouble])
assert_type(f_py + cld_nd, npt.NDArray[np.clongdouble])
assert_type(c_py + cld_nd, npt.NDArray[np.clongdouble])
U_py + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8_nd + b1_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + i1_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + i2_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + i4_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + i8_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + u1_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + u2_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + u4_nd, npt.NDArray[np.datetime64])
assert_type(M8_nd + u8_nd, npt.NDArray[np.datetime64])
M8_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(M8_nd + m8_nd, npt.NDArray[np.datetime64])
M8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(M8_nd + b_py, npt.NDArray[np.datetime64])
assert_type(M8_nd + i_py, npt.NDArray[np.datetime64])
M8_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
M8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + M8_nd, npt.NDArray[np.datetime64])
assert_type(i_py + M8_nd, npt.NDArray[np.datetime64])
f_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_py + M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd + b1_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + i1_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + i2_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + i4_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + i8_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + u1_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + u2_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + u4_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd + u8_nd, npt.NDArray[np.timedelta64])
m8_nd + f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd + M8_nd, npt.NDArray[np.datetime64])
assert_type(m8_nd + m8_nd, npt.NDArray[np.timedelta64])
m8_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd + b_py, npt.NDArray[np.timedelta64])
assert_type(m8_nd + i_py, npt.NDArray[np.timedelta64])
m8_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd + U_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(b_py + m8_nd, npt.NDArray[np.timedelta64])
assert_type(i_py + m8_nd, npt.NDArray[np.timedelta64])
f_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_py + m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(O_nd + b1_nd, npt.NDArray[np.object_])
assert_type(O_nd + i1_nd, npt.NDArray[np.object_])
assert_type(O_nd + i2_nd, npt.NDArray[np.object_])
assert_type(O_nd + i4_nd, npt.NDArray[np.object_])
assert_type(O_nd + i8_nd, npt.NDArray[np.object_])
assert_type(O_nd + u1_nd, npt.NDArray[np.object_])
assert_type(O_nd + u2_nd, npt.NDArray[np.object_])
assert_type(O_nd + u4_nd, npt.NDArray[np.object_])
assert_type(O_nd + u8_nd, npt.NDArray[np.object_])
assert_type(O_nd + f2_nd, npt.NDArray[np.object_])
assert_type(O_nd + f4_nd, npt.NDArray[np.object_])
assert_type(O_nd + f8_nd, npt.NDArray[np.object_])
assert_type(O_nd + fld_nd, npt.NDArray[np.object_])
assert_type(O_nd + c8_nd, npt.NDArray[np.object_])
assert_type(O_nd + c16_nd, npt.NDArray[np.object_])
assert_type(O_nd + cld_nd, npt.NDArray[np.object_])
assert_type(O_nd + O_nd, npt.NDArray[np.object_])
assert_type(O_nd + S_nd, npt.NDArray[np.object_])
assert_type(O_nd + U_nd, npt.NDArray[np.object_])

assert_type(O_nd + b_py, npt.NDArray[np.object_])
assert_type(O_nd + i_py, npt.NDArray[np.object_])
assert_type(O_nd + f_py, npt.NDArray[np.object_])
assert_type(O_nd + c_py, npt.NDArray[np.object_])
assert_type(O_nd + S_py, npt.NDArray[np.object_])
assert_type(O_nd + U_py, npt.NDArray[np.object_])

assert_type(b_py + O_nd, npt.NDArray[np.object_])
assert_type(i_py + O_nd, npt.NDArray[np.object_])
assert_type(f_py + O_nd, npt.NDArray[np.object_])
assert_type(c_py + O_nd, npt.NDArray[np.object_])
assert_type(U_py + O_nd, npt.NDArray[np.object_])

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
assert_type(S_nd + O_nd, npt.NDArray[np.object_])
assert_type(S_nd + S_nd, npt.NDArray[np.bytes_])
S_nd + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

S_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
S_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(S_nd + S_py, npt.NDArray[np.bytes_])
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
assert_type(U_nd + O_nd, npt.NDArray[np.object_])
U_nd + S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_nd + U_nd, npt.NDArray[np.str_])
assert_type(U_nd + T_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])

U_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
U_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_nd + U_py, npt.NDArray[np.str_])

b_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_py + U_nd, npt.NDArray[np.str_])

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
assert_type(T_nd + U_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])
assert_type(T_nd + T_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])

T_nd + b_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + i_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + f_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
T_nd + S_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(T_nd + U_py, np.ndarray[tuple[int, ...], np.dtypes.StringDType])

b_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py + T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(U_py + T_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])
