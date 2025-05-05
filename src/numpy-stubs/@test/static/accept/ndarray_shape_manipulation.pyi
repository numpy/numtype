from typing import assert_type

import _numtype as _nt
import numpy as np

nd: _nt.Array[np.int64]

# reshape
assert_type(nd.reshape(None), _nt.Array[np.int64])
assert_type(nd.reshape(4), _nt.Array1D[np.int64])
assert_type(nd.reshape((4,)), _nt.Array1D[np.int64])
assert_type(nd.reshape(2, 2), _nt.Array2D[np.int64])
assert_type(nd.reshape((2, 2)), _nt.Array2D[np.int64])
assert_type(nd.reshape((2, 2), order="C"), _nt.Array2D[np.int64])
assert_type(nd.reshape(4, order="C"), _nt.Array1D[np.int64])

# resize does not return a value

# transpose
assert_type(nd.transpose(), _nt.Array[np.int64])
assert_type(nd.transpose(1, 0), _nt.Array[np.int64])
assert_type(nd.transpose((1, 0)), _nt.Array[np.int64])

# swapaxes
assert_type(nd.swapaxes(0, 1), _nt.Array[np.int64])

# flatten
assert_type(nd.flatten(), _nt.Array1D[np.int64])
assert_type(nd.flatten("C"), _nt.Array1D[np.int64])

# ravel
assert_type(nd.ravel(), _nt.Array1D[np.int64])
assert_type(nd.ravel("C"), _nt.Array1D[np.int64])

# squeeze
assert_type(nd.squeeze(), _nt.Array[np.int64])
assert_type(nd.squeeze(0), _nt.Array[np.int64])
assert_type(nd.squeeze((0, 2)), _nt.Array[np.int64])
