import numpy as np

class Test(np.nditer): ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]

np.nditer([0, 1], flags=["test"])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.nditer([0, 1], op_flags=[["test"]])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.nditer([0, 1], itershape=(1.0,))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.nditer([0, 1], buffersize=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
