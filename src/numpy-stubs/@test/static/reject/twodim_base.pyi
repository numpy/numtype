import _numtype as _nt
import numpy as np

def func1(ar: _nt.Array, a: int) -> _nt.Array[np.str_]: ...
def func2(ar: _nt.Array, a: float) -> float: ...

AR_b: _nt.Array[np.bool]
AR_m: _nt.Array[np.timedelta64]

AR_LIKE_b: list[bool]

np.eye(10, M=20.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.eye(10, k=2.5, dtype=int)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.diag(AR_b, k=0.5)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.diagflat(AR_b, k=0.5)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.tri(10, M=20.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.tri(10, k=2.5, dtype=int)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.tril(AR_b, k=0.5)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.triu(AR_b, k=0.5)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.vander(AR_m)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.histogram2d(AR_m)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.mask_indices(10, func1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.mask_indices(10, func2, 10.5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
