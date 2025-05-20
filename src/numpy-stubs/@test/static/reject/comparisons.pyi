import _numtype as _nt
import numpy as np

AR_i: _nt.Array[np.int_]
AR_f: _nt.Array[np.float64]
AR_c: _nt.Array[np.complex128]
AR_M: _nt.Array[np.datetime64]
AR_m: _nt.Array[np.timedelta64]

###

AR_i > AR_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_i > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_i > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_f > AR_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f > AR_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_c > AR_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c > AR_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_m > AR_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m > AR_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m > AR_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

# ruff: noqa: SIM300  # (flake8-simplify: yoda-conditions)

AR_M > AR_i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
