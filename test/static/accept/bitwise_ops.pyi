from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

b: bool
i: int

b1: np.bool
i4: np.int32
u4: np.uint32
i8: np.int64
u8: np.uint64

i4_nd: npt.NDArray[np.int32]

###

assert_type(i8 << i8, np.int64)
assert_type(i8 >> i8, np.int64)
assert_type(i8 | i8, np.int64)
assert_type(i8 ^ i8, np.int64)
assert_type(i8 & i8, np.int64)

assert_type(i8 << i4_nd, npt.NDArray[np.signedinteger])
assert_type(i8 >> i4_nd, npt.NDArray[np.signedinteger])
assert_type(i8 | i4_nd, npt.NDArray[np.signedinteger])
assert_type(i8 ^ i4_nd, npt.NDArray[np.signedinteger])
assert_type(i8 & i4_nd, npt.NDArray[np.signedinteger])

assert_type(i4 << i4, np.int32)
assert_type(i4 >> i4, np.int32)
assert_type(i4 | i4, np.int32)
assert_type(i4 ^ i4, np.int32)
assert_type(i4 & i4, np.int32)

assert_type(i8 << i4, np.int64)
assert_type(i8 >> i4, np.int64)
assert_type(i8 | i4, np.int64)
assert_type(i8 ^ i4, np.int64)
assert_type(i8 & i4, np.int64)

assert_type(i8 << b1, np.int64)
assert_type(i8 >> b1, np.int64)
assert_type(i8 | b1, np.int64)
assert_type(i8 ^ b1, np.int64)
assert_type(i8 & b1, np.int64)

assert_type(i8 << b, np.int64)
assert_type(i8 >> b, np.int64)
assert_type(i8 | b, np.int64)
assert_type(i8 ^ b, np.int64)
assert_type(i8 & b, np.int64)

assert_type(u8 << u8, np.uint64)
assert_type(u8 >> u8, np.uint64)
assert_type(u8 | u8, np.uint64)
assert_type(u8 ^ u8, np.uint64)
assert_type(u8 & u8, np.uint64)

assert_type(u8 << i4_nd, npt.NDArray[np.signedinteger])
assert_type(u8 >> i4_nd, npt.NDArray[np.signedinteger])
assert_type(u8 | i4_nd, npt.NDArray[np.signedinteger])
assert_type(u8 ^ i4_nd, npt.NDArray[np.signedinteger])
assert_type(u8 & i4_nd, npt.NDArray[np.signedinteger])

assert_type(u4 << u4, np.uint32)
assert_type(u4 >> u4, np.uint32)
assert_type(u4 | u4, np.uint32)
assert_type(u4 ^ u4, np.uint32)
assert_type(u4 & u4, np.uint32)

assert_type(u4 << i4, np.int64)
assert_type(u4 >> i4, np.int64)
assert_type(u4 | i4, np.int64)
assert_type(u4 ^ i4, np.int64)
assert_type(u4 & i4, np.int64)

assert_type(u4 << i, np.uint32)
assert_type(u4 >> i, np.uint32)
assert_type(u4 | i, np.uint32)
assert_type(u4 ^ i, np.uint32)
assert_type(u4 & i, np.uint32)

assert_type(u8 << b1, np.uint64)
assert_type(u8 >> b1, np.uint64)
assert_type(u8 | b1, np.uint64)
assert_type(u8 ^ b1, np.uint64)
assert_type(u8 & b1, np.uint64)

assert_type(u8 << b, np.uint64)
assert_type(u8 >> b, np.uint64)
assert_type(u8 | b, np.uint64)
assert_type(u8 ^ b, np.uint64)
assert_type(u8 & b, np.uint64)

assert_type(b1 << b1, np.int8)
assert_type(b1 >> b1, np.int8)
assert_type(b1 | b1, np.bool)
assert_type(b1 ^ b1, np.bool)
assert_type(b1 & b1, np.bool)

assert_type(b1 << i4_nd, npt.NDArray[np.signedinteger])
assert_type(b1 >> i4_nd, npt.NDArray[np.signedinteger])
assert_type(b1 | i4_nd, npt.NDArray[np.signedinteger])
assert_type(b1 ^ i4_nd, npt.NDArray[np.signedinteger])
assert_type(b1 & i4_nd, npt.NDArray[np.signedinteger])

assert_type(b1 << b, np.int8)
assert_type(b1 >> b, np.int8)
assert_type(b1 | b, np.bool)
assert_type(b1 ^ b, np.bool)
assert_type(b1 & b, np.bool)

assert_type(b1 << i, np.intp)
assert_type(b1 >> i, np.intp)
assert_type(b1 | i, np.intp)
assert_type(b1 ^ i, np.intp)
assert_type(b1 & i, np.intp)

assert_type(~i8, np.int64)
assert_type(~i4, np.int32)
assert_type(~u8, np.uint64)
assert_type(~u4, np.uint32)
assert_type(~b1, np.bool)
assert_type(~i4_nd, npt.NDArray[np.int32])
