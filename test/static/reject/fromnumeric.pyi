import numpy as np
import numpy.typing as npt

b1: np.bool
AR_b1: npt.NDArray[np.bool]
AR_U: npt.NDArray[np.str_]
AR_M: npt.NDArray[np.datetime64]

###

np.take(b1, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.take(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.take(AR_b1, out=1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.take(AR_b1, mode="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.reshape(b1, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.reshape(AR_b1, 1, order="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.choose(b1, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.choose(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.choose(AR_b1, mode="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.repeat(b1, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.repeat(AR_b1, 1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.swapaxes(AR_b1, None, 1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.swapaxes(AR_b1, 1, [0])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.transpose(AR_b1, axes=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.partition(b1, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.partition(b1, 0, axis="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.partition(AR_b1, 0, kind="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.partition(AR_b1, 0, order=range(5))  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.argpartition(b1, None)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.argpartition(b1, 0, axis="bob")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.argpartition(AR_b1, 0, kind="bob")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.argpartition(AR_b1, 0, order=range(5))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.sort(AR_b1, axis="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.sort(AR_b1, kind="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.sort(AR_b1, order=range(5))  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.argsort(AR_b1, axis="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.argsort(AR_b1, kind="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.argsort(AR_b1, order=range(5))  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.argmax(AR_b1, axis="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.argmax(AR_b1, kind="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.argmin(AR_b1, axis="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.argmin(AR_b1, kind="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.searchsorted(AR_b1[0], 0, side="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.searchsorted(AR_b1[0], 0, sorter=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.resize(AR_b1, 1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.squeeze(AR_b1, 1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.diagonal(AR_b1, offset=None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.diagonal(AR_b1, axis1="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.diagonal(AR_b1, axis2=[])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.trace(AR_b1, offset=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.trace(AR_b1, axis1="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.trace(AR_b1, axis2=[])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]

np.ravel(b1, order="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.nonzero(0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.compress([True], AR_b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.clip(b1, 1, 2, out=1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.sum(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.sum(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.sum(b1, initial=[1])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.all(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.all(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.all(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.any(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.any(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.any(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.cumsum(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.cumsum(b1, dtype=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.cumsum(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.ptp(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.ptp(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.ptp(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.amax(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amax(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amax(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amax(b1, initial=[1.0])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amax(b1, where=[1.0])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.amin(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amin(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amin(b1, out=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amin(b1, initial=[1.0])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.amin(b1, where=[1.0])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.prod(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.prod(b1, out=False)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.prod(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.prod(b1, initial=int)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.prod(b1, where=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.prod(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.cumprod(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.cumprod(b1, out=False)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.cumprod(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.size(b1, axis=1.0)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.around(b1, decimals=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.around(b1, out=type)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.around(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.mean(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.mean(b1, out=False)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.mean(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.mean(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.mean(AR_M)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.std(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.std(b1, out=False)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.std(b1, ddof="test")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.std(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.std(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.var(b1, axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.var(b1, out=False)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.var(b1, ddof="test")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.var(b1, keepdims=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.var(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
