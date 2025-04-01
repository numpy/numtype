import numpy as np
import numpy.typing as npt

AR_U: npt.NDArray[np.str_]
AR_S: npt.NDArray[np.bytes_]

# TODO(jorenham)

# np.strings.equal(AR_U, AR_S)
# np.strings.not_equal(AR_U, AR_S)
# np.strings.greater_equal(AR_U, AR_S)
# np.strings.greater(AR_U, AR_S)
# np.strings.less_equal(AR_U, AR_S)
# np.strings.less(AR_U, AR_S)

# np.strings.isdecimal(AR_S)
# np.strings.isnumeric(AR_S)

np.strings.equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.not_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.greater_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.less_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.greater(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.less(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.encode(AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.strings.decode(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.strings.lstrip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.lstrip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.strip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.strip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rstrip(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rstrip(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.partition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.partition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rpartition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rpartition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.count(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.count(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.endswith(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.endswith(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.startswith(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.startswith(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.find(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.find(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rfind(AR_U, b"a", [1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rfind(AR_S, "a", 0, 9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.index(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.index(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rindex(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.rindex(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.strings.replace(AR_U, b"_", b"-", 10)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.strings.replace(AR_S, "_", "-", 1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
