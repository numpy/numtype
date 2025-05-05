import _numtype as _nt
import numpy as np

AR_i8: _nt.Array[np.int64]

np.pad(AR_i8, 2, mode="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
