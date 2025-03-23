import numpy as np
import numpy._typing as npt

class Index:
    def __index__(self) -> int: ...

ix: Index
a: np.flatiter[npt.NDArray[np.float64]]
supports_array: npt._SupportsArray[np.dtype[np.float64]]

###

a.base = int  # type: ignore[assignment,misc]  # pyright: ignore[reportAttributeAccessIssue]
a.coords = ()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue]
a.index = 0  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue]

a.copy(order="C")  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]

a[np.True_]  # type: ignore[index]  # pyright: ignore[reportArgumentType, reportCallIssue]
a[ix]  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
a[supports_array]  # type: ignore[index]  # pyright: ignore[reportArgumentType, reportCallIssue]
