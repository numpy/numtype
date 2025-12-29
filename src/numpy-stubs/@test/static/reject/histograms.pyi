import _numtype as _nt
import numpy as np

AR_i8: _nt.Array[np.int64]
AR_f8: _nt.Array[np.float64]

np.histogram_bin_edges(AR_i8, range=(0, 1, 2))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.histogram(AR_i8, range=(0, 1, 2))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.histogramdd(AR_i8, range=(0, 1))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.histogramdd(AR_i8, range=[(0, 1, 2)])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType, reportCallIssue]
