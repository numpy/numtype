# ruff: noqa: PYI010
import _numtype as _nt
import numpy as np

f8: np.float64
AR_f8: _nt.Array[np.float64]
AR_M: _nt.Array[np.datetime64]
AR_b: _nt.Array[np.bool]

f_0d: float
U_0d: str
U_1d: list[str]

ctypes_obj = AR_f8.ctypes

###

# NOTE: mypy stops analysis after something returns `NoReturn`; wrapping them in functions works around this

def test_argpartition() -> None:
    f8.argpartition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_diagonal() -> None:
    f8.diagonal()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_trace() -> None:
    f8.trace()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_dot() -> None:
    f8.dot(1)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_nonzero() -> None:
    f8.nonzero()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_partition() -> None:
    f8.partition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_setfield() -> None:
    f8.setfield(2, np.float64)  # type: ignore[arg-type, misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

def test_sort() -> None:
    f8.sort()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

AR_b.__index__()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

AR_f8[f_0d]  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
AR_f8[U_0d]  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
AR_f8[U_1d]  # type: ignore[index]  # pyright: ignore[reportArgumentType, reportCallIssue]
