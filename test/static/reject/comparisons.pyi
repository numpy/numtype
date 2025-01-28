import numpy as np
import numpy.typing as npt

AR_i: npt.NDArray[np.int_]
AR_f: npt.NDArray[np.float64]
AR_c: npt.NDArray[np.complex128]
AR_M: npt.NDArray[np.datetime64]
AR_m: npt.NDArray[np.timedelta64]

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

AR_M > AR_i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > AR_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > ""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M > b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
