import numpy as np

m: np.ma.MaskedArray[tuple[int], np.dtype[np.float64]]

m.shape = (3, 1)  # type: ignore[assignment]
m.dtype = np.bool  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]

np.amin(m, axis=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.amin(m, keepdims=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.amin(m, out=1.0)  # type: ignore[call-overload] # pyright: ignore[reportArgumentType, reportCallIssue]
np.amin(m, fill_value=lambda x: 27)  # type: ignore[call-overload] # pyright: ignore[reportCallIssue, reportUnknownLambdaType]
