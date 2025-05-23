from typing import assert_type

import _numtype as _nt
import numpy as np

a: np.flatiter[_nt.Array[np.str_]]
a_1d: np.flatiter[_nt.Array1D[np.bytes_]]

assert_type(a.base, _nt.Array[np.str_])
assert_type(a.copy(), _nt.Array[np.str_])
assert_type(a.coords, tuple[int, ...])
assert_type(a.index, int)
assert_type(iter(a), np.flatiter[_nt.Array[np.str_]])
assert_type(next(a), np.str_)
assert_type(a[0], np.str_)
assert_type(a[[0, 1, 2]], _nt.Array[np.str_])
assert_type(a[...], _nt.Array[np.str_])
assert_type(a[:], _nt.Array[np.str_])
assert_type(a[...,], _nt.Array[np.str_])
assert_type(a[0,], np.str_)

assert_type(a.__array__(), _nt.Array1D[np.str_])
assert_type(a.__array__(np.dtype(np.float64)), _nt.Array1D[np.float64])
assert_type(a_1d.__array__(), _nt.Array1D[np.bytes_])
assert_type(a_1d.__array__(np.dtype(np.float64)), _nt.Array1D[np.float64])

a[0] = "a"
a[:5] = "a"
a[...] = "a"
a[...,] = "a"
