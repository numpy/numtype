import numpy as np
import numpy.typing as npt

AR_U: npt.NDArray[np.str_]
AR_S: npt.NDArray[np.bytes_]

# TODO(jorenham)
# np.char.equal(AR_U, AR_S)
# np.char.not_equal(AR_U, AR_S)
# np.char.greater_equal(AR_U, AR_S)
# np.char.greater(AR_U, AR_S)
# np.char.less_equal(AR_U, AR_S)
# np.char.less(AR_U, AR_S)

# np.char.isdecimal(AR_S)
# np.char.isnumeric(AR_S)

np.char.equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.char.not_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.char.greater_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.char.less_equal(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.char.greater(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.char.less(AR_S, AR_U, dtype=int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.char.encode(AR_S)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.char.decode(AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.char.join(AR_U, b"_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.join(AR_S, "_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.strip(AR_U, chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.lstrip(AR_U, chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rstrip(AR_U, chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.strip(AR_S, chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.lstrip(AR_S, chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rstrip(AR_S, chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.partition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rpartition(AR_U, b"a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.partition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rpartition(AR_S, "a")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.replace(AR_U, b"_", b"-")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.replace(AR_S, "_", "-")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.split(AR_U, b"_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rsplit(AR_U, b"_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.split(AR_S, "_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rsplit(AR_S, "_")  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.count(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.count(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.endswith(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.startswith(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.endswith(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.startswith(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.find(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rfind(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.find(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rfind(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]

np.char.index(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rindex(AR_U, b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.index(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
np.char.rindex(AR_S, "a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue,reportArgumentType]
