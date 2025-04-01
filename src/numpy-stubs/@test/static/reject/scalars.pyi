import numpy as np

f2: np.float16
f8: np.float64
c8: np.complex64

class A:
    def __float__(self) -> float: ...

###

# Construction

np.float32(3j)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.float32([1.0, 0.0, 0.0])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.complex64([])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.datetime64(0)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

np.int8(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.int16(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.int32(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.int64(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.uint8(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.uint16(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.uint32(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.uint64(A())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.void("test")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.void("test", dtype=None)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]

# pyright doesn't care?
np.generic(1)  # type: ignore[abstract]
np.number(1)  # type: ignore[abstract]
np.integer(1)  # type: ignore[abstract]
np.inexact(1)  # type: ignore[abstract]
np.character("test")  # type: ignore[abstract]
np.flexible(b"test")  # type: ignore[abstract]

np.float64(value=0.0)  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.int64(value=0)  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.uint64(value=0)  # type: ignore[call-arg]  # pyright: ignore[reportCallIssue]
np.complex128(value=0.0j)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.str_(value="bob")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.bytes_(value=b"test")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.void(value=b"test")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.bool(value=True)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.datetime64(value="2019")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.timedelta64(value=0)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.bytes_(b"hello", encoding="utf-8")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.str_("hello", encoding="utf-8")  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]

f8.item(1)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
f8.item((0, 1))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
f8.squeeze(axis=1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
f8.squeeze(axis=(0, 1))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
f8.transpose(1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

def func(a: np.float32) -> None: ...

func(f2)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
func(f8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

c8.__getnewargs__()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
f2.__getnewargs__()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
f2.hex()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
np.float16.fromhex("0x0.0p+0")  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
f2.__trunc__()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]  # noqa: PLC2801
f2.__getformat__("float")  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
