import numpy as np
import numpy.typing as npt

AR_i8: npt.NDArray[np.int64]

np.rec.fromarrays(1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.rec.fromarrays(  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
    [1, 2, 3],
    dtype=[("f8", "f8")],
    formats=["f8", "f8"],  # pyright: ignore[reportArgumentType]
)

np.rec.fromrecords(AR_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.rec.fromrecords(  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
    [(1.5,)],
    dtype=[("f8", "f8")],
    formats=["f8", "f8"],  # pyright: ignore[reportArgumentType]
)

np.rec.fromstring("string", dtype=[("f8", "f8")])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.rec.fromstring(b"bytes")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.rec.fromstring(  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
    b"(1.5,)",
    dtype=[("f8", "f8")],
    formats=["f8", "f8"],  # pyright: ignore[reportArgumentType]
)

with open("test", encoding="utf-8") as f:
    np.rec.fromfile(f, dtype=[("f8", "f8")])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
