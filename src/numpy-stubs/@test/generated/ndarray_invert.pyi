# @generated 2025-04-14T17:00:04Z with tool/testgen.py
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
f8_nd: npt.NDArray[np.float64]
c16_nd: npt.NDArray[np.complex128]
O_nd: npt.NDArray[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
iu_nd: npt.NDArray[np.integer]

###

assert_type(~b1_nd, npt.NDArray[np.bool])
assert_type(~i1_nd, npt.NDArray[np.int8])
assert_type(~i2_nd, npt.NDArray[np.int16])
assert_type(~i4_nd, npt.NDArray[np.int32])
assert_type(~i8_nd, npt.NDArray[np.int64])
assert_type(~u1_nd, npt.NDArray[np.uint8])
assert_type(~u2_nd, npt.NDArray[np.uint16])
assert_type(~u4_nd, npt.NDArray[np.uint32])
assert_type(~u8_nd, npt.NDArray[np.uint64])
~f8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
~c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(~O_nd, npt.NDArray[np.object_])
assert_type(~i_nd, npt.NDArray[np.signedinteger])
assert_type(~u_nd, npt.NDArray[np.unsignedinteger])
assert_type(~iu_nd, npt.NDArray[np.integer])
