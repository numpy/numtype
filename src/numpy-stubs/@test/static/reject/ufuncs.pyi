import _numtype as _nt
import numpy as np

i8: np.int64
AR_f8: _nt.Array[np.float64]
dt64: np.datetime64
AR_dt64: _nt.Array[np.datetime64]

np.sin.nin + "foo"  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

np.sin(1, foo="bar")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.abs(None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.add(1, 1, 1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.add(1, 1, axis=0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.matmul(AR_f8, AR_f8, where=True)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.frexp(AR_f8, out=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.frexp(AR_f8, out=AR_f8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

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

np.isnan(i8, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isnat(i8, dtype=np.int64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isnat(i8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isinf(i8, dtype=np.int64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.isfinite(i8, dtype=np.int64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.logical_not(i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logical_not(dt64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.logical_and(dt64, dt64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logical_and(dt64, dt64, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.logical_or(dt64, dt64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logical_or(dt64, dt64, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.logical_xor(dt64, dt64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logical_xor(dt64, dt64, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.spacing(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.spacing(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.signbit(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.signbit(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.cbrt(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.cbrt(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.deg2rad(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.deg2rad(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.degrees(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.degrees(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.fabs(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.fabs(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.rad2deg(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.rad2deg(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.radians(dt64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.radians(AR_f8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.copysign(i8, i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.heaviside(i8, i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logaddexp(i8, i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.logaddexp2(i8, i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.nextafter(i8, i8, dtype=np.datetime64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
