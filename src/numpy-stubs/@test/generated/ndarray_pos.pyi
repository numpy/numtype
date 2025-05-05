# @generated 2025-05-05T19:48:40Z with tool/testgen.py
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
c8_nd: _nt.Array[np.complex64]
c16_nd: _nt.Array[np.complex128]
cld_nd: _nt.Array[np.clongdouble]
m8_nd: _nt.Array[np.timedelta64]
O_nd: _nt.Array[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
f_nd: npt.NDArray[np.floating]
c_nd: npt.NDArray[np.complexfloating]
iu_nd: npt.NDArray[np.integer]
fc_nd: npt.NDArray[np.inexact]
iufc_nd: npt.NDArray[np.number]

###

+b1_nd  # type: ignore[misc]  # pyright: ignore[reportOperatorIssue]
assert_type(+i1_nd, _nt.Array[np.int8])
assert_type(+i2_nd, _nt.Array[np.int16])
assert_type(+i4_nd, _nt.Array[np.int32])
assert_type(+i8_nd, _nt.Array[np.int64])
assert_type(+u1_nd, _nt.Array[np.uint8])
assert_type(+u2_nd, _nt.Array[np.uint16])
assert_type(+u4_nd, _nt.Array[np.uint32])
assert_type(+u8_nd, _nt.Array[np.uint64])
assert_type(+f2_nd, _nt.Array[np.float16])
assert_type(+f4_nd, _nt.Array[np.float32])
assert_type(+f8_nd, _nt.Array[np.float64])
assert_type(+fld_nd, _nt.Array[np.longdouble])
assert_type(+c8_nd, _nt.Array[np.complex64])
assert_type(+c16_nd, _nt.Array[np.complex128])
assert_type(+cld_nd, _nt.Array[np.clongdouble])
assert_type(+m8_nd, _nt.Array[np.timedelta64])
assert_type(+O_nd, _nt.Array[np.object_])
assert_type(+i_nd, _nt.Array[np.signedinteger])
assert_type(+u_nd, _nt.Array[np.unsignedinteger])
assert_type(+f_nd, _nt.Array[np.floating])
assert_type(+c_nd, _nt.Array[np.complexfloating])
assert_type(+iu_nd, _nt.Array[np.integer])
assert_type(+fc_nd, _nt.Array[np.inexact])
assert_type(+iufc_nd, _nt.Array[np.number])
