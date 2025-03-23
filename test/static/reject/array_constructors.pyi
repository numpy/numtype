import numpy as np
import numpy.typing as npt

a: npt.NDArray[np.float64]
generator = (i for i in range(10))

np.require(a, requirements=1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.require(a, requirements="TEST")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.zeros("test")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.zeros()  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.ones("test")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.ones()  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.array(0, float, True)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.linspace(None, "bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linspace(0, 2, num=10.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linspace(0, 2, endpoint="True")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linspace(0, 2, retstep=b"False")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linspace(0, 2, dtype=0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linspace(0, 2, axis=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.logspace(None, "bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logspace(0, 2, base=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.geomspace(None, "bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.stack(generator)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.hstack({1, 2})  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.vstack(1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.array([1], like=1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
