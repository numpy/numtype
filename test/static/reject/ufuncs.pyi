import numpy as np
import numpy.typing as npt

AR_f8: npt.NDArray[np.float64]

np.sin.nin + "foo"  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

np.sin(1, foo="bar")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.abs(None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.add(1, 1, 1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.add(1, 1, axis=0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.matmul(AR_f8, AR_f8, where=True)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.frexp(AR_f8, out=None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.frexp(AR_f8, out=AR_f8)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.absolute.outer()  # type: ignore[call-arg, misc]  # pyright: ignore[reportCallIssue]
np.frexp.outer()  # type: ignore[call-arg, misc]  # pyright: ignore[reportCallIssue]
np.divmod.outer()  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.matmul.outer()  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.absolute.reduceat()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.frexp.reduceat()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.divmod.reduceat()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.matmul.reduceat()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]

np.absolute.reduce()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.frexp.reduce()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.divmod.reduce()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.matmul.reduce()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]

np.absolute.accumulate()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.frexp.accumulate()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.divmod.accumulate()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.matmul.accumulate()  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]

np.frexp.at()  # type: ignore[call-arg, misc]  # pyright: ignore[reportCallIssue]
np.divmod.at()  # type: ignore[call-arg, misc]  # pyright: ignore[reportCallIssue]
np.matmul.at()  # type: ignore[call-arg, misc]  # pyright: ignore[reportCallIssue]
