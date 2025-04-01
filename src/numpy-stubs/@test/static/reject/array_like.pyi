import numpy as np
from numpy._typing import ArrayLike

class A: ...

x1: ArrayLike = (i for i in range(10))  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
x2: ArrayLike = A()  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
x3: ArrayLike = {1: "foo", 2: "bar"}  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

scalar = np.int64(1)
scalar.__array__(dtype=np.float64)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
array = np.array([1])
array.__array__(dtype=np.float64)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
