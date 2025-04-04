import numpy as np

m: np.ma.MaskedArray[tuple[int], np.dtype[np.float64]]

m.argmin(axis=1.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmin(keepdims=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmin(out=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmin(fill_value=lambda x: 27)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]s

np.ma.argmin(m, axis=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmin(m, axis=(1,))  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmin(m, keepdims=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmin(m, out=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmin(m, fill_value=lambda x: 27)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]

m.argmax(axis=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmax(keepdims=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmax(out=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
m.argmax(fill_value=lambda x: 27)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]

np.ma.argmax(m, axis=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmax(m, axis=(0,))  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmax(m, keepdims=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmax(m, out=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.ma.argmax(m, fill_value=lambda x: 27)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
