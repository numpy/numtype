# @generated 2025-05-03T21:24:40Z with tool/testgen.py
from typing import assert_type

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
m8_nd: npt.NDArray[np.timedelta64]
O_nd: npt.NDArray[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
f_nd: npt.NDArray[np.floating]
c_nd: npt.NDArray[np.complexfloating]
iu_nd: npt.NDArray[np.integer]
fc_nd: npt.NDArray[np.inexact]
iufc_nd: npt.NDArray[np.number]

###

-b1_nd  # type: ignore[misc]  # pyright: ignore[reportOperatorIssue]
assert_type(-i1_nd, npt.NDArray[np.int8])
assert_type(-i2_nd, npt.NDArray[np.int16])
assert_type(-i4_nd, npt.NDArray[np.int32])
assert_type(-i8_nd, npt.NDArray[np.int64])
assert_type(-u1_nd, npt.NDArray[np.uint8])
assert_type(-u2_nd, npt.NDArray[np.uint16])
assert_type(-u4_nd, npt.NDArray[np.uint32])
assert_type(-u8_nd, npt.NDArray[np.uint64])
assert_type(-f2_nd, npt.NDArray[np.float16])
assert_type(-f4_nd, npt.NDArray[np.float32])
assert_type(-f8_nd, npt.NDArray[np.float64])
assert_type(-fld_nd, npt.NDArray[np.longdouble])
assert_type(-c8_nd, npt.NDArray[np.complex64])
assert_type(-c16_nd, npt.NDArray[np.complex128])
assert_type(-cld_nd, npt.NDArray[np.clongdouble])
assert_type(-m8_nd, npt.NDArray[np.timedelta64])
assert_type(-O_nd, npt.NDArray[np.object_])
assert_type(-i_nd, npt.NDArray[np.signedinteger])
assert_type(-u_nd, npt.NDArray[np.unsignedinteger])
assert_type(-f_nd, npt.NDArray[np.floating])
assert_type(-c_nd, npt.NDArray[np.complexfloating])
assert_type(-iu_nd, npt.NDArray[np.integer])
assert_type(-fc_nd, npt.NDArray[np.inexact])
assert_type(-iufc_nd, npt.NDArray[np.number])
