from collections.abc import Generator
from typing import assert_type

import _numtype as _nt
import numpy as np

AR_i8: _nt.Array[np.int64]
ar_iter: np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]]

###

assert_type(ar_iter.var, _nt.Array[np.int64])
assert_type(ar_iter.buf_size, int | None)
assert_type(ar_iter.start, list[int])
assert_type(ar_iter.stop, list[int])
assert_type(ar_iter.step, list[int])
assert_type(ar_iter.shape, tuple[int, ...])
assert_type(ar_iter.flat, Generator[np.int64, None, None])

assert_type(ar_iter.__array__(), _nt.Array[np.int64])

for i in ar_iter:
    assert_type(i, _nt.Array[np.int64])

assert_type(ar_iter[0], np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]])
assert_type(ar_iter[...], np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]])
assert_type(ar_iter[:], np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]])
assert_type(ar_iter[0, 0, 0], np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]])
assert_type(ar_iter[..., 0, :], np.lib.Arrayterator[tuple[int, ...], np.dtype[np.int64]])
