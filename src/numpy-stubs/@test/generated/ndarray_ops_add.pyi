# @generated 2025-04-09T20:54:28Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

array_b1_nd: npt.NDArray[np.bool]
array_i1_nd: npt.NDArray[np.int8]
array_i2_nd: npt.NDArray[np.int16]
array_i4_nd: npt.NDArray[np.int32]
array_i8_nd: npt.NDArray[np.int64]
array_u1_nd: npt.NDArray[np.uint8]
array_u2_nd: npt.NDArray[np.uint16]
array_u4_nd: npt.NDArray[np.uint32]
array_u8_nd: npt.NDArray[np.uint64]
array_f2_nd: npt.NDArray[np.float16]
array_f4_nd: npt.NDArray[np.float32]
array_f8_nd: npt.NDArray[np.float64]
array_fld_nd: npt.NDArray[np.longdouble]
array_c8_nd: npt.NDArray[np.complex64]
array_c16_nd: npt.NDArray[np.complex128]
array_cld_nd: npt.NDArray[np.clongdouble]
array_M8_nd: npt.NDArray[np.datetime64]
array_m8_nd: npt.NDArray[np.timedelta64]
array_O_nd: npt.NDArray[np.object_]
array_S_nd: npt.NDArray[np.bytes_]
array_U_nd: npt.NDArray[np.str_]
array_T_nd: np.ndarray[tuple[int, ...], np.dtypes.StringDType]

###

assert_type(array_b1_nd + array_b1_nd, npt.NDArray[np.bool])
assert_type(array_b1_nd + array_i1_nd, npt.NDArray[np.int8])
assert_type(array_b1_nd + array_i2_nd, npt.NDArray[np.int16])
assert_type(array_b1_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_b1_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_b1_nd + array_u1_nd, npt.NDArray[np.uint8])
assert_type(array_b1_nd + array_u2_nd, npt.NDArray[np.uint16])
assert_type(array_b1_nd + array_u4_nd, npt.NDArray[np.uint32])
assert_type(array_b1_nd + array_u8_nd, npt.NDArray[np.uint64])
assert_type(array_b1_nd + array_f2_nd, npt.NDArray[np.float16])
assert_type(array_b1_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_b1_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_b1_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_b1_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_b1_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_b1_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_b1_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_b1_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_b1_nd + array_O_nd, npt.NDArray[np.object_])
array_b1_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_b1_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_b1_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_i1_nd + array_b1_nd, npt.NDArray[np.int8])
assert_type(array_i1_nd + array_i1_nd, npt.NDArray[np.int8])
assert_type(array_i1_nd + array_i2_nd, npt.NDArray[np.int16])
assert_type(array_i1_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_i1_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_i1_nd + array_u1_nd, npt.NDArray[np.int16])
assert_type(array_i1_nd + array_u2_nd, npt.NDArray[np.int32])
assert_type(array_i1_nd + array_u4_nd, npt.NDArray[np.int64])
assert_type(array_i1_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_i1_nd + array_f2_nd, npt.NDArray[np.float16])
assert_type(array_i1_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_i1_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_i1_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_i1_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_i1_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_i1_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_i1_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_i1_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_i1_nd + array_O_nd, npt.NDArray[np.object_])
array_i1_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i1_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i1_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_i2_nd + array_b1_nd, npt.NDArray[np.int16])
assert_type(array_i2_nd + array_i1_nd, npt.NDArray[np.int16])
assert_type(array_i2_nd + array_i2_nd, npt.NDArray[np.int16])
assert_type(array_i2_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_i2_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_i2_nd + array_u1_nd, npt.NDArray[np.int16])
assert_type(array_i2_nd + array_u2_nd, npt.NDArray[np.int32])
assert_type(array_i2_nd + array_u4_nd, npt.NDArray[np.int64])
assert_type(array_i2_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_i2_nd + array_f2_nd, npt.NDArray[np.float32])
assert_type(array_i2_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_i2_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_i2_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_i2_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_i2_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_i2_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_i2_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_i2_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_i2_nd + array_O_nd, npt.NDArray[np.object_])
array_i2_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i2_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i2_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_i4_nd + array_b1_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_i1_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_i2_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_i4_nd + array_u1_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_u2_nd, npt.NDArray[np.int32])
assert_type(array_i4_nd + array_u4_nd, npt.NDArray[np.int64])
assert_type(array_i4_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_i4_nd + array_f2_nd, npt.NDArray[np.float64])
assert_type(array_i4_nd + array_f4_nd, npt.NDArray[np.float64])
assert_type(array_i4_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_i4_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_i4_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_i4_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_i4_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_i4_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_i4_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_i4_nd + array_O_nd, npt.NDArray[np.object_])
array_i4_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i4_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i4_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_i8_nd + array_b1_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_i1_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_i2_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_i4_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_u1_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_u2_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_u4_nd, npt.NDArray[np.int64])
assert_type(array_i8_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_i8_nd + array_f2_nd, npt.NDArray[np.float64])
assert_type(array_i8_nd + array_f4_nd, npt.NDArray[np.float64])
assert_type(array_i8_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_i8_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_i8_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_i8_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_i8_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_i8_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_i8_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_i8_nd + array_O_nd, npt.NDArray[np.object_])
array_i8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_i8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_u1_nd + array_b1_nd, npt.NDArray[np.uint8])
assert_type(array_u1_nd + array_i1_nd, npt.NDArray[np.int16])
assert_type(array_u1_nd + array_i2_nd, npt.NDArray[np.int16])
assert_type(array_u1_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_u1_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_u1_nd + array_u1_nd, npt.NDArray[np.uint8])
assert_type(array_u1_nd + array_u2_nd, npt.NDArray[np.uint16])
assert_type(array_u1_nd + array_u4_nd, npt.NDArray[np.uint32])
assert_type(array_u1_nd + array_u8_nd, npt.NDArray[np.uint64])
assert_type(array_u1_nd + array_f2_nd, npt.NDArray[np.float16])
assert_type(array_u1_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_u1_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_u1_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_u1_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_u1_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_u1_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_u1_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_u1_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_u1_nd + array_O_nd, npt.NDArray[np.object_])
array_u1_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u1_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u1_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_u2_nd + array_b1_nd, npt.NDArray[np.uint16])
assert_type(array_u2_nd + array_i1_nd, npt.NDArray[np.int32])
assert_type(array_u2_nd + array_i2_nd, npt.NDArray[np.int32])
assert_type(array_u2_nd + array_i4_nd, npt.NDArray[np.int32])
assert_type(array_u2_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_u2_nd + array_u1_nd, npt.NDArray[np.uint16])
assert_type(array_u2_nd + array_u2_nd, npt.NDArray[np.uint16])
assert_type(array_u2_nd + array_u4_nd, npt.NDArray[np.uint32])
assert_type(array_u2_nd + array_u8_nd, npt.NDArray[np.uint64])
assert_type(array_u2_nd + array_f2_nd, npt.NDArray[np.float32])
assert_type(array_u2_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_u2_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_u2_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_u2_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_u2_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_u2_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_u2_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_u2_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_u2_nd + array_O_nd, npt.NDArray[np.object_])
array_u2_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u2_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u2_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_u4_nd + array_b1_nd, npt.NDArray[np.uint32])
assert_type(array_u4_nd + array_i1_nd, npt.NDArray[np.int64])
assert_type(array_u4_nd + array_i2_nd, npt.NDArray[np.int64])
assert_type(array_u4_nd + array_i4_nd, npt.NDArray[np.int64])
assert_type(array_u4_nd + array_i8_nd, npt.NDArray[np.int64])
assert_type(array_u4_nd + array_u1_nd, npt.NDArray[np.uint32])
assert_type(array_u4_nd + array_u2_nd, npt.NDArray[np.uint32])
assert_type(array_u4_nd + array_u4_nd, npt.NDArray[np.uint32])
assert_type(array_u4_nd + array_u8_nd, npt.NDArray[np.uint64])
assert_type(array_u4_nd + array_f2_nd, npt.NDArray[np.float64])
assert_type(array_u4_nd + array_f4_nd, npt.NDArray[np.float64])
assert_type(array_u4_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_u4_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_u4_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_u4_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_u4_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_u4_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_u4_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_u4_nd + array_O_nd, npt.NDArray[np.object_])
array_u4_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u4_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u4_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_u8_nd + array_b1_nd, npt.NDArray[np.uint64])
assert_type(array_u8_nd + array_i1_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_i2_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_i4_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_i8_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_u1_nd, npt.NDArray[np.uint64])
assert_type(array_u8_nd + array_u2_nd, npt.NDArray[np.uint64])
assert_type(array_u8_nd + array_u4_nd, npt.NDArray[np.uint64])
assert_type(array_u8_nd + array_u8_nd, npt.NDArray[np.uint64])
assert_type(array_u8_nd + array_f2_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_f4_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_u8_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_u8_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_u8_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_u8_nd + array_cld_nd, npt.NDArray[np.clongdouble])
assert_type(array_u8_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_u8_nd + array_m8_nd, npt.NDArray[np.timedelta64])
assert_type(array_u8_nd + array_O_nd, npt.NDArray[np.object_])
array_u8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_u8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_f2_nd + array_b1_nd, npt.NDArray[np.float16])
assert_type(array_f2_nd + array_i1_nd, npt.NDArray[np.float16])
assert_type(array_f2_nd + array_i2_nd, npt.NDArray[np.float32])
assert_type(array_f2_nd + array_i4_nd, npt.NDArray[np.float64])
assert_type(array_f2_nd + array_i8_nd, npt.NDArray[np.float64])
assert_type(array_f2_nd + array_u1_nd, npt.NDArray[np.float16])
assert_type(array_f2_nd + array_u2_nd, npt.NDArray[np.float32])
assert_type(array_f2_nd + array_u4_nd, npt.NDArray[np.float64])
assert_type(array_f2_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_f2_nd + array_f2_nd, npt.NDArray[np.float16])
assert_type(array_f2_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_f2_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_f2_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_f2_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_f2_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_f2_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_f2_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f2_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_f2_nd + array_O_nd, npt.NDArray[np.object_])
array_f2_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f2_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f2_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_f4_nd + array_b1_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_i1_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_i2_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_i4_nd, npt.NDArray[np.float64])
assert_type(array_f4_nd + array_i8_nd, npt.NDArray[np.float64])
assert_type(array_f4_nd + array_u1_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_u2_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_u4_nd, npt.NDArray[np.float64])
assert_type(array_f4_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_f4_nd + array_f2_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_f4_nd, npt.NDArray[np.float32])
assert_type(array_f4_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_f4_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_f4_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_f4_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_f4_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_f4_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f4_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_f4_nd + array_O_nd, npt.NDArray[np.object_])
array_f4_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f4_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f4_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_f8_nd + array_b1_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_i1_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_i2_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_i4_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_i8_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_u1_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_u2_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_u4_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_u8_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_f2_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_f4_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_f8_nd, npt.NDArray[np.float64])
assert_type(array_f8_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_f8_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_f8_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_f8_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_f8_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f8_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_f8_nd + array_O_nd, npt.NDArray[np.object_])
array_f8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_f8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_fld_nd + array_b1_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_i1_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_i2_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_i4_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_i8_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_u1_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_u2_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_u4_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_u8_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_f2_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_f4_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_f8_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_fld_nd, npt.NDArray[np.longdouble])
assert_type(array_fld_nd + array_c8_nd, npt.NDArray[np.clongdouble])
assert_type(array_fld_nd + array_c16_nd, npt.NDArray[np.clongdouble])
assert_type(array_fld_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_fld_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_fld_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_fld_nd + array_O_nd, npt.NDArray[np.object_])
array_fld_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_fld_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_fld_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_c8_nd + array_b1_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_i1_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_i2_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_i4_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_i8_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_u1_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_u2_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_u4_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_u8_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_f2_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_f4_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_f8_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_fld_nd, npt.NDArray[np.clongdouble])
assert_type(array_c8_nd + array_c8_nd, npt.NDArray[np.complex64])
assert_type(array_c8_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_c8_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_c8_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c8_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_c8_nd + array_O_nd, npt.NDArray[np.object_])
array_c8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_c16_nd + array_b1_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_i1_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_i2_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_i4_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_i8_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_u1_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_u2_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_u4_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_u8_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_f2_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_f4_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_f8_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_fld_nd, npt.NDArray[np.clongdouble])
assert_type(array_c16_nd + array_c8_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_c16_nd, npt.NDArray[np.complex128])
assert_type(array_c16_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_c16_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c16_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_c16_nd + array_O_nd, npt.NDArray[np.object_])
array_c16_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c16_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_c16_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_cld_nd + array_b1_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_i1_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_i2_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_i4_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_i8_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_u1_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_u2_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_u4_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_u8_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_f2_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_f4_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_f8_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_fld_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_c8_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_c16_nd, npt.NDArray[np.clongdouble])
assert_type(array_cld_nd + array_cld_nd, npt.NDArray[np.clongdouble])
array_cld_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_cld_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_cld_nd + array_O_nd, npt.NDArray[np.object_])
array_cld_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_cld_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_cld_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_M8_nd + array_b1_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_i1_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_i2_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_i4_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_i8_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_u1_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_u2_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_u4_nd, npt.NDArray[np.datetime64])
assert_type(array_M8_nd + array_u8_nd, npt.NDArray[np.datetime64])
array_M8_nd + array_f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_M8_nd + array_m8_nd, npt.NDArray[np.datetime64])
array_M8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_M8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_m8_nd + array_b1_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_i1_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_i2_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_i4_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_i8_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_u1_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_u2_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_u4_nd, npt.NDArray[np.timedelta64])
assert_type(array_m8_nd + array_u8_nd, npt.NDArray[np.timedelta64])
array_m8_nd + array_f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_m8_nd + array_M8_nd, npt.NDArray[np.datetime64])
assert_type(array_m8_nd + array_m8_nd, npt.NDArray[np.timedelta64])
array_m8_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_m8_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(array_O_nd + array_b1_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_i1_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_i2_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_i4_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_i8_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_u1_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_u2_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_u4_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_u8_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_f2_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_f4_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_f8_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_fld_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_c8_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_c16_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_cld_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_O_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_S_nd, npt.NDArray[np.object_])
assert_type(array_O_nd + array_U_nd, npt.NDArray[np.object_])

array_S_nd + array_b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_S_nd + array_O_nd, npt.NDArray[np.object_])
assert_type(array_S_nd + array_S_nd, npt.NDArray[np.bytes_])
array_S_nd + array_U_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_S_nd + array_T_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

array_U_nd + array_b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_U_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_U_nd + array_O_nd, npt.NDArray[np.object_])
array_U_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_U_nd + array_U_nd, npt.NDArray[np.str_])
assert_type(array_U_nd + array_T_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])

array_T_nd + array_b1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_u1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_u2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_u4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_f2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_f4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_fld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_M8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
array_T_nd + array_S_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(array_T_nd + array_U_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])
assert_type(array_T_nd + array_T_nd, np.ndarray[tuple[int, ...], np.dtypes.StringDType])
