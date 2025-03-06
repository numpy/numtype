import io
import pickle as pickle
from _typeshed import FileDescriptorOrPath, Incomplete, OpenTextMode
from builtins import bytes  # noqa: UP029
from collections.abc import Iterable, Sequence
from os import PathLike as os_PathLike, fspath as os_fspath  # noqa: ICN003
from pathlib import Path as Path
from types import ModuleType, TracebackType
from typing import IO, Any, Final, Generic, TypeGuard, overload
from typing_extensions import TypeIs, TypeVar

__all__ = [
    "Path",
    "asbytes",
    "asbytes_nested",
    "asstr",
    "asunicode",
    "asunicode_nested",
    "basestring",
    "bytes",
    "contextlib_nullcontext",
    "getexception",
    "integer_types",
    "is_pathlib_path",
    "isfileobj",
    "long",
    "npy_load_module",
    "open_latin1",
    "os_PathLike",
    "os_fspath",
    "pickle",
    "sixu",
    "strchar",
    "unicode",
]

###

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True, default=None)

###

long = int
unicode = str
basestring = str
integer_types: Final[tuple[type[int]]] = ...
strchar: Final = "U"

class contextlib_nullcontext(Generic[_T_co]):
    enter_result: Incomplete
    def __init__(self, /, enter_result: _T_co | None = None) -> None: ...
    def __enter__(self, /) -> _T_co: ...
    def __exit__(self, cls: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, /) -> None: ...

#
def asstr(s: object) -> str: ...
def asunicode(s: object) -> str: ...
def asbytes(s: object) -> bytes: ...

#
@overload
def asbytes_nested(x: bytes | str) -> bytes: ...
@overload
def asbytes_nested(x: Iterable[bytes]) -> Sequence[bytes]: ...
@overload
def asbytes_nested(x: Iterable[Iterable[bytes]]) -> Sequence[Sequence[bytes]]: ...
@overload
def asbytes_nested(x: Iterable[object]) -> Any: ...

#
@overload
def asunicode_nested(x: bytes | str) -> str: ...
@overload
def asunicode_nested(x: Iterable[bytes | str]) -> Sequence[str]: ...
@overload
def asunicode_nested(x: Iterable[object]) -> Sequence[Any]: ...

# NOTE: don't use `TypeIs` here; even `f` is of this type, this function might still return `False`.
def isfileobj(f: object) -> TypeGuard[io.FileIO | io.BufferedReader | io.BufferedWriter]: ...

#
def is_pathlib_path(obj: object) -> TypeIs[Path]: ...

#
@overload
def open_latin1(filename: FileDescriptorOrPath, mode: OpenTextMode = "r") -> io.TextIOWrapper: ...
@overload
def open_latin1(filename: FileDescriptorOrPath, mode: str = "r") -> IO[Any]: ...

#
def sixu(s: _T) -> _T: ...

#
def getexception() -> BaseException: ...

#
def npy_load_module(name: str, fn: str, info: None = None) -> ModuleType: ...
