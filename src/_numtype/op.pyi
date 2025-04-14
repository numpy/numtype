from typing import Any, Protocol, override
from typing_extensions import TypeVar

__all__ = [  # noqa: RUF022
    "CanEq",
    "CanNe",
    "CanLt",
    "CanLe",
    "CanGt",
    "CanGe",
    "CanAdd",
    "CanRAdd",
    "CanSub",
    "CanRSub",
    "CanMul",
    "CanRMul",
    "CanMatmul",
    "CanRMatmul",
    "CanPow",
    "CanRPow",
    "CanTruediv",
    "CanRTruediv",
    "CanFloordiv",
    "CanRFloordiv",
    "CanMod",
    "CanRMod",
    "CanDivmod",
    "CanRDivmod",
    "CanLshift",
    "CanRLshift",
    "CanRshift",
    "CanRRshift",
    "CanAnd",
    "CanRAnd",
    "CanXor",
    "CanRXor",
    "CanOr",
    "CanROr",
]  # fmt:

###

_T_contra = TypeVar("_T_contra", contravariant=True, default=object)
_T_co = TypeVar("_T_co", covariant=True, default=Any)

###

class CanEq(Protocol[_T_contra, _T_co]):
    @override
    def __eq__(self, x: _T_contra, /) -> _T_co: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class CanNe(Protocol[_T_contra, _T_co]):
    @override
    def __ne__(self, x: _T_contra, /) -> _T_co: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class CanLt(Protocol[_T_contra, _T_co]):
    def __lt__(self, x: _T_contra, /) -> _T_co: ...

class CanLe(Protocol[_T_contra, _T_co]):
    def __le__(self, x: _T_contra, /) -> _T_co: ...

class CanGt(Protocol[_T_contra, _T_co]):
    def __gt__(self, x: _T_contra, /) -> _T_co: ...

class CanGe(Protocol[_T_contra, _T_co]):
    def __ge__(self, x: _T_contra, /) -> _T_co: ...

###

class CanAdd(Protocol[_T_contra, _T_co]):
    def __add__(self, x: _T_contra, /) -> _T_co: ...

class CanRAdd(Protocol[_T_contra, _T_co]):
    def __radd__(self, x: _T_contra, /) -> _T_co: ...

class CanSub(Protocol[_T_contra, _T_co]):
    def __sub__(self, x: _T_contra, /) -> _T_co: ...

class CanRSub(Protocol[_T_contra, _T_co]):
    def __rsub__(self, x: _T_contra, /) -> _T_co: ...

class CanMul(Protocol[_T_contra, _T_co]):
    def __mul__(self, x: _T_contra, /) -> _T_co: ...

class CanRMul(Protocol[_T_contra, _T_co]):
    def __rmul__(self, x: _T_contra, /) -> _T_co: ...

class CanMatmul(Protocol[_T_contra, _T_co]):
    def __matmul__(self, x: _T_contra, /) -> _T_co: ...

class CanRMatmul(Protocol[_T_contra, _T_co]):
    def __rmatmul__(self, x: _T_contra, /) -> _T_co: ...

class CanPow(Protocol[_T_contra, _T_co]):
    def __pow__(self, exp: _T_contra, /) -> _T_co: ...

class CanRPow(Protocol[_T_contra, _T_co]):
    def __rpow__(self, x: _T_contra, /) -> _T_co: ...

class CanTruediv(Protocol[_T_contra, _T_co]):
    def __truediv__(self, x: _T_contra, /) -> _T_co: ...

class CanRTruediv(Protocol[_T_contra, _T_co]):
    def __rtruediv__(self, x: _T_contra, /) -> _T_co: ...

###

class CanFloordiv(Protocol[_T_contra, _T_co]):
    def __floordiv__(self, x: _T_contra, /) -> _T_co: ...

class CanRFloordiv(Protocol[_T_contra, _T_co]):
    def __rfloordiv__(self, x: _T_contra, /) -> _T_co: ...

class CanMod(Protocol[_T_contra, _T_co]):
    def __mod__(self, x: _T_contra, /) -> _T_co: ...

class CanRMod(Protocol[_T_contra, _T_co]):
    def __rmod__(self, x: _T_contra, /) -> _T_co: ...

class CanDivmod(Protocol[_T_contra, _T_co]):
    def __divmod__(self, x: _T_contra, /) -> _T_co: ...

class CanRDivmod(Protocol[_T_contra, _T_co]):
    def __rdivmod__(self, x: _T_contra, /) -> _T_co: ...

###

class CanLshift(Protocol[_T_contra, _T_co]):
    def __lshift__(self, x: _T_contra, /) -> _T_co: ...

class CanRLshift(Protocol[_T_contra, _T_co]):
    def __rlshift__(self, x: _T_contra, /) -> _T_co: ...

class CanRshift(Protocol[_T_contra, _T_co]):
    def __rshift__(self, x: _T_contra, /) -> _T_co: ...

class CanRRshift(Protocol[_T_contra, _T_co]):
    def __rrshift__(self, x: _T_contra, /) -> _T_co: ...

class CanAnd(Protocol[_T_contra, _T_co]):
    def __and__(self, x: _T_contra, /) -> _T_co: ...

class CanRAnd(Protocol[_T_contra, _T_co]):
    def __rand__(self, x: _T_contra, /) -> _T_co: ...

class CanXor(Protocol[_T_contra, _T_co]):
    def __xor__(self, x: _T_contra, /) -> _T_co: ...

class CanRXor(Protocol[_T_contra, _T_co]):
    def __rxor__(self, x: _T_contra, /) -> _T_co: ...

class CanOr(Protocol[_T_contra, _T_co]):
    def __or__(self, x: _T_contra, /) -> _T_co: ...

class CanROr(Protocol[_T_contra, _T_co]):
    def __ror__(self, x: _T_contra, /) -> _T_co: ...
