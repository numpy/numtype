import _numtype as _nt
import numpy as np
from numpy.lib import stride_tricks

AR_f8: _nt.Array[np.float64]

###

stride_tricks.as_strided(AR_f8, shape=8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
stride_tricks.as_strided(AR_f8, strides=8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
stride_tricks.sliding_window_view(AR_f8, axis=(1,))  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
