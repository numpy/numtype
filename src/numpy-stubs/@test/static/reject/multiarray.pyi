import _numtype as _nt
import numpy as np

AR_LIKE_f: list[float]

i8: np.int64
M: np.datetime64

AR_b: _nt.Array[np.bool]
AR_u1: _nt.Array[np.uint8]
AR_i8: _nt.Array[np.int64]
AR_f8: _nt.Array[np.float64]
AR_M: _nt.Array[np.datetime64]

def func(a: int) -> None: ...

###

np.where(AR_b, 1)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.can_cast(AR_f8, 1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.vdot(AR_M, AR_M)  # type: ignore[type-var]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.copyto(AR_LIKE_f, AR_f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.putmask(AR_LIKE_f, [True, True, False], 1.5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.packbits(AR_f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.packbits(AR_u1, bitorder=">")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.unpackbits(AR_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.unpackbits(AR_u1, bitorder=">")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.shares_memory(1, 1, max_work=i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.may_share_memory(1, 1, max_work=i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.arange(M)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.datetime_data(int)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.datetime_as_string("2012")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.char.compare_chararrays("a", b"a", "==", False)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.nested_iters([AR_i8, AR_i8])  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.nested_iters([AR_i8, AR_i8], 0)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.nested_iters([AR_i8, AR_i8], [0])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType]
np.nested_iters([AR_i8, AR_i8], [[0], [1]], flags=["test"])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType]
np.nested_iters([AR_i8, AR_i8], [[0], [1]], op_flags=[["test"]])  # type: ignore[list-item]  # pyright: ignore[reportArgumentType]
np.nested_iters([AR_i8, AR_i8], [[0], [1]], buffersize=1.0)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
