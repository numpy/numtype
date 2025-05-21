import _numtype as _nt
import numpy as np

AR_c: _nt.Array[np.complex128]
AR_m: _nt.Array[np.timedelta64]
AR_M: _nt.Array[np.datetime64]
AR_O: _nt.Array[np.object_]

np.fix(AR_c)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.fix(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.fix(AR_M)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.isposinf(AR_c)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isposinf(AR_m)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isposinf(AR_M)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isposinf(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.isneginf(AR_c)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isneginf(AR_m)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isneginf(AR_M)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isneginf(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
