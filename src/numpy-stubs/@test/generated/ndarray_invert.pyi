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
f8_nd: _nt.Array[np.float64]
c16_nd: _nt.Array[np.complex128]
O_nd: _nt.Array[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
iu_nd: npt.NDArray[np.integer]

###

assert_type(~b1_nd, _nt.Array[np.bool])
assert_type(~i1_nd, _nt.Array[np.int8])
assert_type(~i2_nd, _nt.Array[np.int16])
assert_type(~i4_nd, _nt.Array[np.int32])
assert_type(~i8_nd, _nt.Array[np.int64])
assert_type(~u1_nd, _nt.Array[np.uint8])
assert_type(~u2_nd, _nt.Array[np.uint16])
assert_type(~u4_nd, _nt.Array[np.uint32])
assert_type(~u8_nd, _nt.Array[np.uint64])
~f8_nd  # type: ignore[misc]  # pyright: ignore[reportOperatorIssue]
~c16_nd  # type: ignore[misc]  # pyright: ignore[reportOperatorIssue]
assert_type(~O_nd, _nt.Array[np.object_])
assert_type(~i_nd, _nt.Array[np.signedinteger])
assert_type(~u_nd, _nt.Array[np.unsignedinteger])
assert_type(~iu_nd, _nt.Array[np.integer])
