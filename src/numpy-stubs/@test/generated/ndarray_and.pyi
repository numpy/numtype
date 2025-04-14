# @generated 2025-04-14T22:23:26Z with tool/testgen.py
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
O_nd: npt.NDArray[np.object_]
i_nd: npt.NDArray[np.signedinteger]
u_nd: npt.NDArray[np.unsignedinteger]
iu_nd: npt.NDArray[np.integer]

b_py: bool
i_py: int

###

assert_type(b1_nd & b1_nd, npt.NDArray[np.bool])
assert_type(b1_nd & i1_nd, npt.NDArray[np.int8])
assert_type(b1_nd & i2_nd, npt.NDArray[np.int16])
assert_type(b1_nd & i4_nd, npt.NDArray[np.int32])
assert_type(b1_nd & i8_nd, npt.NDArray[np.int64])
assert_type(b1_nd & u1_nd, npt.NDArray[np.uint8])
assert_type(b1_nd & u2_nd, npt.NDArray[np.uint16])
assert_type(b1_nd & u4_nd, npt.NDArray[np.uint32])
assert_type(b1_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(b1_nd & O_nd, npt.NDArray[np.object_])
assert_type(b1_nd & i_nd, npt.NDArray[np.signedinteger])
assert_type(b1_nd & u_nd, npt.NDArray[np.unsignedinteger])
assert_type(b1_nd & iu_nd, npt.NDArray[np.integer])

assert_type(b1_nd & b_py, npt.NDArray[np.bool])
assert_type(b1_nd & i_py, npt.NDArray[np.int64])

assert_type(b_py & b1_nd, npt.NDArray[np.bool])
assert_type(i_py & b1_nd, npt.NDArray[np.int64])

assert_type(i1_nd & b1_nd, npt.NDArray[np.int8])
assert_type(i1_nd & i1_nd, npt.NDArray[np.int8])
assert_type(i1_nd & i2_nd, npt.NDArray[np.int16])
assert_type(i1_nd & i4_nd, npt.NDArray[np.int32])
assert_type(i1_nd & i8_nd, npt.NDArray[np.int64])
assert_type(i1_nd & u1_nd, npt.NDArray[np.int16])
assert_type(i1_nd & u2_nd, npt.NDArray[np.int32])
assert_type(i1_nd & u4_nd, npt.NDArray[np.int64])
i1_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i1_nd & O_nd, npt.NDArray[np.object_])
assert_type(i1_nd & i_nd, npt.NDArray[np.signedinteger])
i1_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i1_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i1_nd & b_py, npt.NDArray[np.int8])
assert_type(i1_nd & i_py, npt.NDArray[np.int8])

assert_type(b_py & i1_nd, npt.NDArray[np.int8])
assert_type(i_py & i1_nd, npt.NDArray[np.int8])

assert_type(i2_nd & b1_nd, npt.NDArray[np.int16])
assert_type(i2_nd & i1_nd, npt.NDArray[np.int16])
assert_type(i2_nd & i2_nd, npt.NDArray[np.int16])
assert_type(i2_nd & i4_nd, npt.NDArray[np.int32])
assert_type(i2_nd & i8_nd, npt.NDArray[np.int64])
assert_type(i2_nd & u1_nd, npt.NDArray[np.int16])
assert_type(i2_nd & u2_nd, npt.NDArray[np.int32])
assert_type(i2_nd & u4_nd, npt.NDArray[np.int64])
i2_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i2_nd & O_nd, npt.NDArray[np.object_])
assert_type(i2_nd & i_nd, npt.NDArray[np.signedinteger])
i2_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i2_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i2_nd & b_py, npt.NDArray[np.int16])
assert_type(i2_nd & i_py, npt.NDArray[np.int16])

assert_type(b_py & i2_nd, npt.NDArray[np.int16])
assert_type(i_py & i2_nd, npt.NDArray[np.int16])

assert_type(i4_nd & b1_nd, npt.NDArray[np.int32])
assert_type(i4_nd & i1_nd, npt.NDArray[np.int32])
assert_type(i4_nd & i2_nd, npt.NDArray[np.int32])
assert_type(i4_nd & i4_nd, npt.NDArray[np.int32])
assert_type(i4_nd & i8_nd, npt.NDArray[np.int64])
assert_type(i4_nd & u1_nd, npt.NDArray[np.int32])
assert_type(i4_nd & u2_nd, npt.NDArray[np.int32])
assert_type(i4_nd & u4_nd, npt.NDArray[np.int64])
i4_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i4_nd & O_nd, npt.NDArray[np.object_])
assert_type(i4_nd & i_nd, npt.NDArray[np.signedinteger])
i4_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i4_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i4_nd & b_py, npt.NDArray[np.int32])
assert_type(i4_nd & i_py, npt.NDArray[np.int32])

assert_type(b_py & i4_nd, npt.NDArray[np.int32])
assert_type(i_py & i4_nd, npt.NDArray[np.int32])

assert_type(i8_nd & b1_nd, npt.NDArray[np.int64])
assert_type(i8_nd & i1_nd, npt.NDArray[np.int64])
assert_type(i8_nd & i2_nd, npt.NDArray[np.int64])
assert_type(i8_nd & i4_nd, npt.NDArray[np.int64])
assert_type(i8_nd & i8_nd, npt.NDArray[np.int64])
assert_type(i8_nd & u1_nd, npt.NDArray[np.int64])
assert_type(i8_nd & u2_nd, npt.NDArray[np.int64])
assert_type(i8_nd & u4_nd, npt.NDArray[np.int64])
i8_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8_nd & O_nd, npt.NDArray[np.object_])
assert_type(i8_nd & i_nd, npt.NDArray[np.int64])
i8_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i8_nd & b_py, npt.NDArray[np.int64])
assert_type(i8_nd & i_py, npt.NDArray[np.int64])

assert_type(b_py & i8_nd, npt.NDArray[np.int64])
assert_type(i_py & i8_nd, npt.NDArray[np.int64])

assert_type(u1_nd & b1_nd, npt.NDArray[np.uint8])
assert_type(u1_nd & i1_nd, npt.NDArray[np.int16])
assert_type(u1_nd & i2_nd, npt.NDArray[np.int16])
assert_type(u1_nd & i4_nd, npt.NDArray[np.int32])
assert_type(u1_nd & i8_nd, npt.NDArray[np.int64])
assert_type(u1_nd & u1_nd, npt.NDArray[np.uint8])
assert_type(u1_nd & u2_nd, npt.NDArray[np.uint16])
assert_type(u1_nd & u4_nd, npt.NDArray[np.uint32])
assert_type(u1_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(u1_nd & O_nd, npt.NDArray[np.object_])
assert_type(u1_nd & i_nd, npt.NDArray[np.signedinteger])
assert_type(u1_nd & u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u1_nd & iu_nd, npt.NDArray[np.integer])

assert_type(u1_nd & b_py, npt.NDArray[np.uint8])
assert_type(u1_nd & i_py, npt.NDArray[np.uint8])

assert_type(b_py & u1_nd, npt.NDArray[np.uint8])
assert_type(i_py & u1_nd, npt.NDArray[np.uint8])

assert_type(u2_nd & b1_nd, npt.NDArray[np.uint16])
assert_type(u2_nd & i1_nd, npt.NDArray[np.int32])
assert_type(u2_nd & i2_nd, npt.NDArray[np.int32])
assert_type(u2_nd & i4_nd, npt.NDArray[np.int32])
assert_type(u2_nd & i8_nd, npt.NDArray[np.int64])
assert_type(u2_nd & u1_nd, npt.NDArray[np.uint16])
assert_type(u2_nd & u2_nd, npt.NDArray[np.uint16])
assert_type(u2_nd & u4_nd, npt.NDArray[np.uint32])
assert_type(u2_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(u2_nd & O_nd, npt.NDArray[np.object_])
assert_type(u2_nd & i_nd, npt.NDArray[np.signedinteger])
assert_type(u2_nd & u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u2_nd & iu_nd, npt.NDArray[np.integer])

assert_type(u2_nd & b_py, npt.NDArray[np.uint16])
assert_type(u2_nd & i_py, npt.NDArray[np.uint16])

assert_type(b_py & u2_nd, npt.NDArray[np.uint16])
assert_type(i_py & u2_nd, npt.NDArray[np.uint16])

assert_type(u4_nd & b1_nd, npt.NDArray[np.uint32])
assert_type(u4_nd & i1_nd, npt.NDArray[np.int64])
assert_type(u4_nd & i2_nd, npt.NDArray[np.int64])
assert_type(u4_nd & i4_nd, npt.NDArray[np.int64])
assert_type(u4_nd & i8_nd, npt.NDArray[np.int64])
assert_type(u4_nd & u1_nd, npt.NDArray[np.uint32])
assert_type(u4_nd & u2_nd, npt.NDArray[np.uint32])
assert_type(u4_nd & u4_nd, npt.NDArray[np.uint32])
assert_type(u4_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(u4_nd & O_nd, npt.NDArray[np.object_])
assert_type(u4_nd & i_nd, npt.NDArray[np.int64])
assert_type(u4_nd & u_nd, npt.NDArray[np.unsignedinteger])
assert_type(u4_nd & iu_nd, npt.NDArray[np.integer])

assert_type(u4_nd & b_py, npt.NDArray[np.uint32])
assert_type(u4_nd & i_py, npt.NDArray[np.uint32])

assert_type(b_py & u4_nd, npt.NDArray[np.uint32])
assert_type(i_py & u4_nd, npt.NDArray[np.uint32])

assert_type(u8_nd & b1_nd, npt.NDArray[np.uint64])
u8_nd & i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd & i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd & i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8_nd & i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8_nd & u1_nd, npt.NDArray[np.uint64])
assert_type(u8_nd & u2_nd, npt.NDArray[np.uint64])
assert_type(u8_nd & u4_nd, npt.NDArray[np.uint64])
assert_type(u8_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(u8_nd & O_nd, npt.NDArray[np.object_])
u8_nd & i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u8_nd & u_nd, npt.NDArray[np.uint64])
u8_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u8_nd & b_py, npt.NDArray[np.uint64])
assert_type(u8_nd & i_py, npt.NDArray[np.uint64])

assert_type(b_py & u8_nd, npt.NDArray[np.uint64])
assert_type(i_py & u8_nd, npt.NDArray[np.uint64])

assert_type(O_nd & b1_nd, npt.NDArray[np.object_])
assert_type(O_nd & i1_nd, npt.NDArray[np.object_])
assert_type(O_nd & i2_nd, npt.NDArray[np.object_])
assert_type(O_nd & i4_nd, npt.NDArray[np.object_])
assert_type(O_nd & i8_nd, npt.NDArray[np.object_])
assert_type(O_nd & u1_nd, npt.NDArray[np.object_])
assert_type(O_nd & u2_nd, npt.NDArray[np.object_])
assert_type(O_nd & u4_nd, npt.NDArray[np.object_])
assert_type(O_nd & u8_nd, npt.NDArray[np.object_])
assert_type(O_nd & O_nd, npt.NDArray[np.object_])
assert_type(O_nd & i_nd, npt.NDArray[np.object_])
assert_type(O_nd & u_nd, npt.NDArray[np.object_])
assert_type(O_nd & iu_nd, npt.NDArray[np.object_])

assert_type(O_nd & b_py, npt.NDArray[np.object_])
assert_type(O_nd & i_py, npt.NDArray[np.object_])

assert_type(b_py & O_nd, npt.NDArray[np.object_])
assert_type(i_py & O_nd, npt.NDArray[np.object_])

assert_type(i_nd & b1_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & i1_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & i2_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & i4_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & i8_nd, npt.NDArray[np.int64])
assert_type(i_nd & u1_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & u2_nd, npt.NDArray[np.signedinteger])
assert_type(i_nd & u4_nd, npt.NDArray[np.int64])
i_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i_nd & O_nd, npt.NDArray[np.object_])
assert_type(i_nd & i_nd, npt.NDArray[np.signedinteger])
i_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(i_nd & b_py, npt.NDArray[np.signedinteger])
assert_type(i_nd & i_py, npt.NDArray[np.signedinteger])

assert_type(b_py & i_nd, npt.NDArray[np.signedinteger])
assert_type(i_py & i_nd, npt.NDArray[np.signedinteger])

assert_type(u_nd & b1_nd, npt.NDArray[np.unsignedinteger])
u_nd & i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd & i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd & i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u_nd & i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u_nd & u1_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd & u2_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd & u4_nd, npt.NDArray[np.unsignedinteger])
assert_type(u_nd & u8_nd, npt.NDArray[np.uint64])
assert_type(u_nd & O_nd, npt.NDArray[np.object_])
u_nd & i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(u_nd & u_nd, npt.NDArray[np.unsignedinteger])
u_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(u_nd & b_py, npt.NDArray[np.unsignedinteger])
assert_type(u_nd & i_py, npt.NDArray[np.unsignedinteger])

assert_type(b_py & u_nd, npt.NDArray[np.unsignedinteger])
assert_type(i_py & u_nd, npt.NDArray[np.unsignedinteger])

assert_type(iu_nd & b1_nd, npt.NDArray[np.integer])
iu_nd & i1_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd & i2_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd & i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd & i8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu_nd & u1_nd, npt.NDArray[np.integer])
assert_type(iu_nd & u2_nd, npt.NDArray[np.integer])
assert_type(iu_nd & u4_nd, npt.NDArray[np.integer])
iu_nd & u8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(iu_nd & O_nd, npt.NDArray[np.object_])
iu_nd & i_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd & u_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
iu_nd & iu_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(iu_nd & b_py, npt.NDArray[np.integer])
assert_type(iu_nd & i_py, npt.NDArray[np.integer])

assert_type(b_py & iu_nd, npt.NDArray[np.integer])
assert_type(i_py & iu_nd, npt.NDArray[np.integer])
