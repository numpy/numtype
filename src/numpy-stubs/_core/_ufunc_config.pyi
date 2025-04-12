from _typeshed import SupportsWrite
from collections.abc import Callable
from types import TracebackType
from typing import Any, Literal, TypeAlias, TypeVar, TypedDict, type_check_only

__all__ = ["errstate", "getbufsize", "geterr", "geterrcall", "setbufsize", "seterr", "seterrcall"]

_CallableT = TypeVar("_CallableT", bound=Callable[..., object])

_ErrKind: TypeAlias = Literal["ignore", "warn", "raise", "call", "print", "log"]
_ErrFunc: TypeAlias = Callable[[str, int], Any]
_ErrCall: TypeAlias = _ErrFunc | SupportsWrite[str]

@type_check_only
class _ErrDict(TypedDict):
    divide: _ErrKind
    over: _ErrKind
    under: _ErrKind
    invalid: _ErrKind

###

class _unspecified: ...

class errstate:
    __slots__ = "_all", "_call", "_divide", "_invalid", "_over", "_token", "_under"

    def __init__(
        self,
        /,
        *,
        call: _ErrCall | _unspecified = ...,
        all: _ErrKind | None = None,
        divide: _ErrKind | None = None,
        over: _ErrKind | None = None,
        under: _ErrKind | None = None,
        invalid: _ErrKind | None = None,
    ) -> None: ...
    def __call__(self, /, func: _CallableT) -> _CallableT: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self, cls: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, /
    ) -> None: ...

def seterr(
    all: _ErrKind | None = None,
    divide: _ErrKind | None = None,
    over: _ErrKind | None = None,
    under: _ErrKind | None = None,
    invalid: _ErrKind | None = None,
) -> _ErrDict: ...
def geterr() -> _ErrDict: ...
def setbufsize(size: int) -> int: ...
def getbufsize() -> int: ...
def seterrcall(func: _ErrCall | None) -> _ErrCall | None: ...
def geterrcall() -> _ErrCall | None: ...
