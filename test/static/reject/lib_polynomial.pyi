import numpy as np
import numpy.typing as npt

AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
AR_O: npt.NDArray[np.object_]
AR_U: npt.NDArray[np.str_]

poly_obj: np.poly1d

###

5**poly_obj  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

np.polymul(AR_f8, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polydiv(AR_f8, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.polyint(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyint(AR_f8, m=1j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.polyder(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyder(AR_f8, m=1j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.polyfit(AR_O, AR_f8, 1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyfit(AR_f8, AR_f8, 1, rcond=1j)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyfit(AR_f8, AR_f8, 1, w=AR_c16)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyfit(AR_f8, AR_f8, 1, cov="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.polyval(AR_f8, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polyadd(AR_f8, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.polysub(AR_f8, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
