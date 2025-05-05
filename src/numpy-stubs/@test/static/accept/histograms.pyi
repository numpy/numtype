from typing import assert_type

import _numtype as _nt
import numpy as np

AR_i8: _nt.Array[np.int64]
AR_f8: _nt.Array[np.float64]

assert_type(np.histogram_bin_edges(AR_i8, bins="auto"), _nt.Array)
assert_type(np.histogram_bin_edges(AR_i8, bins="rice", range=(0, 3)), _nt.Array)
assert_type(np.histogram_bin_edges(AR_i8, bins="scott", weights=AR_f8), _nt.Array)

assert_type(np.histogram(AR_i8, bins="auto"), tuple[_nt.Array, _nt.Array])
assert_type(np.histogram(AR_i8, bins="rice", range=(0, 3)), tuple[_nt.Array, _nt.Array])
assert_type(np.histogram(AR_i8, bins="scott", weights=AR_f8), tuple[_nt.Array, _nt.Array])
assert_type(np.histogram(AR_f8, bins=1, density=True), tuple[_nt.Array, _nt.Array])

assert_type(np.histogramdd(AR_i8, bins=[1]), tuple[_nt.Array, tuple[_nt.Array, ...]])
assert_type(np.histogramdd(AR_i8, range=[(0, 3)]), tuple[_nt.Array, tuple[_nt.Array, ...]])
assert_type(np.histogramdd(AR_i8, weights=AR_f8), tuple[_nt.Array, tuple[_nt.Array, ...]])
assert_type(np.histogramdd(AR_f8, density=True), tuple[_nt.Array, tuple[_nt.Array, ...]])
