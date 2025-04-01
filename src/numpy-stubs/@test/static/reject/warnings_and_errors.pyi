import numpy.exceptions as ex

ex.AxisError(1.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
ex.AxisError(1, ndim=2.0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
ex.AxisError(2, msg_prefix=404)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
