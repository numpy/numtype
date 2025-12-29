from typing import Any

import numpy as np
import numpy.typing as npt

AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
AR_m: npt.NDArray[np.timedelta64]
AR_M: npt.NDArray[np.datetime64]
AR_O: npt.NDArray[np.object_]
AR_b_list: list[npt.NDArray[np.bool]]

def fn_none_i(a: None, /) -> npt.NDArray[Any]: ...
def fn_ar_i(a: npt.NDArray[np.float64], posarg: int, /) -> npt.NDArray[Any]: ...

np.average(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.select(1, [AR_f8])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.angle(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.unwrap(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.unwrap(AR_c16)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.trim_zeros(1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.place(1, [True], 1.5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.vectorize(1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.place(AR_f8, slice(None), 5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.piecewise(AR_f8, True, [fn_ar_i], "wrong")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.piecewise(AR_f8, AR_b_list, [fn_none_i])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.piecewise(AR_f8, AR_b_list, [fn_ar_i])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.piecewise(AR_f8, AR_b_list, [fn_ar_i], 3.1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.piecewise(AR_f8, AR_b_list, [fn_ar_i], 42, None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.piecewise(AR_f8, AR_b_list, [fn_ar_i], 42, _=None)  # type: ignore[list-item]  # pyright: ignore[reportCallIssue]

np.interp(AR_f8, AR_c16, AR_f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.interp(AR_c16, AR_f8, AR_f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.interp(AR_f8, AR_f8, AR_f8, period=AR_c16)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.interp(AR_f8, AR_f8, AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.cov(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.cov(AR_O)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.corrcoef(AR_m)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.corrcoef(AR_O)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.corrcoef(AR_f8, bias=True)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.corrcoef(AR_f8, ddof=2)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.blackman(1j)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.bartlett(1j)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.hanning(1j)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.hamming(1j)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.hamming(AR_c16)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.kaiser(1j, 1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.sinc(AR_O)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.median(AR_M)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.percentile(AR_f8, 50j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.percentile(AR_f8, 50, interpolation="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.quantile(AR_f8, 0.5j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.quantile(AR_f8, 0.5, interpolation="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.meshgrid(AR_f8, AR_f8, indexing="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.delete(AR_f8, AR_f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.insert(AR_f8, AR_f8, 1.5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.digitize(AR_f8, 1j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
