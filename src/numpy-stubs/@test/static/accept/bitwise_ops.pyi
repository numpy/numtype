from typing_extensions import assert_type

import numpy as np

###

b1: np.bool
i4: np.int32
u4: np.uint32
i8: np.int64
u8: np.uint64

###

assert_type(~b1, np.bool)
assert_type(~i4, np.int32)
assert_type(~u4, np.uint32)
assert_type(~i8, np.int64)
assert_type(~u8, np.uint64)
