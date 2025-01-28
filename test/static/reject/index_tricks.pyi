import numpy as np

AR_LIKE_i: list[int]
AR_LIKE_f: list[float]

np.fill_diagonal(AR_LIKE_f, 2)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.diag_indices(1.0)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.ndindex([1, 2, 3])  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.unravel_index(AR_LIKE_f, (1, 2, 3))  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.ravel_multi_index(  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
    AR_LIKE_i,
    (1, 2, 3),
    mode="bob",  # pyright: ignore[reportArgumentType]
)

np.mgrid[1]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
np.mgrid[...]  # type: ignore[index]  # pyright: ignore[reportArgumentType]

np.ogrid[1]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
np.ogrid[...]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
