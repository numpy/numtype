import numpy as np

###

class Test1:
    not_dtype: np.dtype[np.float64]

class Test2:
    dtype: type[float]

###

t1: Test1
t2: Test2
t3: dict[str, tuple[type[int | float], int]]

###

np.dtype(t1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.dtype(t2)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.dtype(t3)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
