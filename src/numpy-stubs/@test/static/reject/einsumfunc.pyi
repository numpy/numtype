import _numtype as _nt
import numpy as np

###

AR_i: _nt.Array[np.int64]
AR_f: _nt.Array[np.float64]
AR_m: _nt.Array[np.timedelta64]
AR_U: _nt.Array[np.str_]

###

np.einsum("i,i->i", AR_i, AR_m)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.einsum("i,i->i", AR_f, AR_f, dtype=np.int32)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.einsum("i,i->i", AR_i, AR_i, out=AR_U)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.einsum("i,i->i", AR_i, AR_i, out=AR_U, casting="unsafe")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
