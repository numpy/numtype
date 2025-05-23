import _numtype as _nt
import numpy as np

b_ = np.bool()
dt = np.datetime64(0, "D")
td = np.timedelta64(0, "D")

AR_b: _nt.Array[np.bool]
AR_u: _nt.Array[np.uint32]
AR_i: _nt.Array[np.int64]
AR_f: _nt.Array[np.longdouble]
AR_c: _nt.Array[np.complex128]
AR_m: _nt.Array[np.timedelta64]
AR_M: _nt.Array[np.datetime64]

AR_LIKE_b: list[bool]
AR_LIKE_u: list[np.uint32]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]
AR_LIKE_c: list[complex]
AR_LIKE_m: list[np.timedelta64]
AR_LIKE_M: list[np.datetime64]

u8: np.uint64
i4_nd: _nt.Array[np.int32]

# Array subtraction

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

AR_m // AR_LIKE_b  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
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

AR_u *= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_i *= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_f *= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_f *= AR_LIKE_m  # type: ignore[arg-type]  # pyright: ignore[reportOperatorIssue, reportUnknownVariableType]

# Array power

AR_b **= AR_LIKE_b  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_u  # type: ignore[arg-type]  # pyright: ignore[reportOperatorIssue, reportUnknownVariableType]
AR_b **= AR_LIKE_i  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_b **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_u **= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_u **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_i **= AR_LIKE_f  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]
AR_i **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

AR_f **= AR_LIKE_c  # type: ignore[arg-type]  # pyright: ignore[reportAssignmentType]

# will raise `TypeError` at runtime
u8 << i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 >> i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 | i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 ^ i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
u8 & i4_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
