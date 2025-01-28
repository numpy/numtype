from typing import Any

import numpy as np
import numpy.typing as npt

b_ = np.bool()
dt = np.datetime64(0, "D")
td = np.timedelta64(0, "D")

AR_b: npt.NDArray[np.bool]
AR_u: npt.NDArray[np.uint32]
AR_i: npt.NDArray[np.int64]
AR_f: npt.NDArray[np.longdouble]
AR_c: npt.NDArray[np.complex128]
AR_m: npt.NDArray[np.timedelta64]
AR_M: npt.NDArray[np.datetime64]

ANY: Any

AR_LIKE_b: list[bool]
AR_LIKE_u: list[np.uint32]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]
AR_LIKE_c: list[complex]
AR_LIKE_m: list[np.timedelta64]
AR_LIKE_M: list[np.datetime64]

# Array subtraction

# NOTE: mypys `NoReturn` errors are, unfortunately, not that great
_1 = AR_b - AR_LIKE_b  # type: ignore[var-annotated]
_2 = AR_LIKE_b - AR_b  # type: ignore[var-annotated]
AR_i - b""  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_f - AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f - AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c - AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c - AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_m - AR_LIKE_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M - AR_LIKE_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m - AR_LIKE_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M - AR_LIKE_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_m - AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_LIKE_m - AR_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

# array floor division

AR_M // AR_LIKE_b  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_u  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_i  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_f  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_b // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_u // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_i // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_m // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_M // AR_LIKE_M  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

_3 = AR_m // AR_LIKE_b  # type: ignore[var-annotated]
AR_m // AR_LIKE_c  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

AR_b // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_u // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_i // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_f // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
AR_c // AR_LIKE_m  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

# Array multiplication

AR_b *= AR_LIKE_u  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b *= AR_LIKE_i  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b *= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_u *= AR_LIKE_i  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u *= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_i *= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_f *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_f *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

# Array power

AR_b **= AR_LIKE_b  # type: ignore[misc]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_u  # type: ignore[misc]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_i  # type: ignore[misc]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_f  # type: ignore[misc]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_c  # type: ignore[misc]  # pyright: ignore[reportAssignmentType]

AR_u **= AR_LIKE_i  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u **= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_i **= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_f **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

# Scalars

b_ - b_  # type: ignore[call-overload]  # pyright: ignore[reportOperatorIssue]

dt + dt  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
td - dt  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
td % 1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
td / dt  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
td % dt  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

-b_  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
+b_  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
