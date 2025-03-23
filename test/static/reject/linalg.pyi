import numpy as np
import numpy.typing as npt

AR_f8: npt.NDArray[np.float64]
AR_O: npt.NDArray[np.object_]
AR_M: npt.NDArray[np.datetime64]

###

np.linalg.inv(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.pinv(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.tensorinv(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.solve(AR_O, AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.tensorsolve(AR_O, AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.matrix_rank(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.matrix_power(AR_M, 5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.cholesky(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.qr(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.qr(AR_f8, mode="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.svd(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.eig(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.eigh(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.eigh(AR_O, UPLO="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.eigvals(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.eigvalsh(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.eigvalsh(AR_O, UPLO="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.cond(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.cond(AR_f8, p="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.det(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.linalg.slogdet(AR_O)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.norm(AR_f8, ord="bob")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.linalg.multi_dot([AR_M])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType, reportCallIssue]
