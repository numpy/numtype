import types
import zipfile
from _typeshed import StrOrBytesPath, StrPath, SupportsKeysAndGetItem, SupportsRead, SupportsWrite
from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence
from re import Pattern
from typing import IO, Any, Generic, Literal as L, Protocol, overload, type_check_only
from typing_extensions import Self, TypeVar, deprecated

import numpy as np
from numpy._core.multiarray import packbits, unpackbits
from numpy._typing import ArrayLike, DTypeLike, NDArray, _DTypeLike, _SupportsArrayFunc
from numpy.ma.mrecords import MaskedRecords

__all__ = [
    "fromregex",
    "genfromtxt",
    "load",
    "loadtxt",
    "packbits",
    "save",
    "savetxt",
    "savez",
    "savez_compressed",
    "unpackbits",
]

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_SCT = TypeVar("_SCT", bound=np.generic)

@type_check_only
class _SupportsReadSeek(SupportsRead[_T_co], Protocol[_T_co]):
    def seek(self, offset: int, whence: int, /) -> object: ...

class BagObj(Generic[_T_co]):
    def __init__(self, obj: SupportsKeysAndGetItem[str, _T_co]) -> None: ...
    def __getattribute__(self, key: str) -> _T_co: ...
    def __dir__(self) -> list[str]: ...

class NpzFile(Mapping[str, NDArray[Any]]):
    zip: zipfile.ZipFile
    fid: IO[str] | None
    files: list[str]
    allow_pickle: bool
    pickle_kwargs: Mapping[str, Any] | None
    _MAX_REPR_ARRAY_COUNT: int
    # Represent `f` as a mutable property so we can access the type of `self`
    @property
    def f(self: _T) -> BagObj[_T]: ...
    @f.setter
    def f(self: _T, value: BagObj[_T], /) -> None: ...
    def __init__(
        self,
        fid: IO[str],
        own_fid: bool = ...,
        allow_pickle: bool = ...,
        pickle_kwargs: Mapping[str, object] | None = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, cls: type[BaseException] | None, e: BaseException | None, tb: types.TracebackType | None, /) -> None: ...
    def close(self) -> None: ...
    def __del__(self) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str, /) -> NDArray[Any]: ...
    def __contains__(self, key: str, /) -> bool: ...

class DataSource:
    def __init__(self, destpath: StrPath | None = ...) -> None: ...
    def __del__(self) -> None: ...
    def abspath(self, path: str) -> str: ...
    def exists(self, path: str) -> bool: ...

    # Whether the file-object is opened in string or bytes mode (by default)
    # depends on the file-extension of `path`
    def open(self, path: str, mode: str = ..., encoding: str | None = ..., newline: str | None = ...) -> IO[Any]: ...

# NOTE: Returns a `NpzFile` if file is a zip file;
# returns an `ndarray`/`memmap` otherwise
def load(
    file: StrOrBytesPath | _SupportsReadSeek[bytes],
    mmap_mode: L["r+", "r", "w+", "c"] | None = ...,
    allow_pickle: bool = ...,
    fix_imports: bool = ...,
    encoding: L["ASCII", "latin1", "bytes"] = ...,
) -> Any: ...
@overload
def save(file: StrPath | SupportsWrite[bytes], arr: ArrayLike, allow_pickle: bool = ...) -> None: ...
@overload
@deprecated("The 'fix_imports' flag is deprecated in NumPy 2.1.")
def save(file: StrPath | SupportsWrite[bytes], arr: ArrayLike, allow_pickle: bool = ..., *, fix_imports: bool) -> None: ...
@overload
@deprecated("The 'fix_imports' flag is deprecated in NumPy 2.1.")
def save(file: StrPath | SupportsWrite[bytes], arr: ArrayLike, allow_pickle: bool, fix_imports: bool) -> None: ...
def savez(file: StrPath | SupportsWrite[bytes], *args: ArrayLike, allow_pickle: bool = ..., **kwds: ArrayLike) -> None: ...
def savez_compressed(
    file: StrPath | SupportsWrite[bytes],
    *args: ArrayLike,
    allow_pickle: bool = ...,
    **kwds: ArrayLike,
) -> None: ...

# File-like objects only have to implement `__iter__` and,
# optionally, `encoding`
@overload
def loadtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: None = ...,
    comments: str | Sequence[str] | None = ...,
    delimiter: str | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | Callable[[str], Any] | None = ...,
    skiprows: int = ...,
    usecols: int | Sequence[int] | None = ...,
    unpack: bool = ...,
    ndmin: L[0, 1, 2] = ...,
    encoding: str | None = ...,
    max_rows: int | None = ...,
    *,
    quotechar: str | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def loadtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: _DTypeLike[_SCT],
    comments: str | Sequence[str] | None = ...,
    delimiter: str | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | Callable[[str], Any] | None = ...,
    skiprows: int = ...,
    usecols: int | Sequence[int] | None = ...,
    unpack: bool = ...,
    ndmin: L[0, 1, 2] = ...,
    encoding: str | None = ...,
    max_rows: int | None = ...,
    *,
    quotechar: str | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def loadtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: DTypeLike,
    comments: str | Sequence[str] | None = ...,
    delimiter: str | None = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | Callable[[str], Any] | None = ...,
    skiprows: int = ...,
    usecols: int | Sequence[int] | None = ...,
    unpack: bool = ...,
    ndmin: L[0, 1, 2] = ...,
    encoding: str | None = ...,
    max_rows: int | None = ...,
    *,
    quotechar: str | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
def savetxt(
    fname: StrPath | SupportsWrite[str] | SupportsWrite[bytes],
    X: ArrayLike,
    fmt: str | Sequence[str] = ...,
    delimiter: str = ...,
    newline: str = ...,
    header: str = ...,
    footer: str = ...,
    comments: str = ...,
    encoding: str | None = ...,
) -> None: ...
@overload
def fromregex(
    file: StrPath | SupportsRead[str] | SupportsRead[bytes],
    regexp: str | bytes | Pattern[Any],
    dtype: _DTypeLike[_SCT],
    encoding: str | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromregex(
    file: StrPath | SupportsRead[str] | SupportsRead[bytes],
    regexp: str | bytes | Pattern[Any],
    dtype: DTypeLike,
    encoding: str | None = ...,
) -> NDArray[Any]: ...
@overload
def genfromtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: None = ...,
    comments: str = ...,
    delimiter: str | int | Iterable[int] | None = ...,
    skip_header: int = ...,
    skip_footer: int = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | None = ...,
    missing_values: Any = ...,
    filling_values: Any = ...,
    usecols: Sequence[int] | None = ...,
    names: L[True] | str | Collection[str] | None = ...,
    excludelist: Sequence[str] | None = ...,
    deletechars: str = ...,
    replace_space: str = ...,
    autostrip: bool = ...,
    case_sensitive: bool | L["upper", "lower"] = ...,
    defaultfmt: str = ...,
    unpack: bool | None = ...,
    usemask: bool = ...,
    loose: bool = ...,
    invalid_raise: bool = ...,
    max_rows: int | None = ...,
    encoding: str = ...,
    *,
    ndmin: L[0, 1, 2] = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def genfromtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: _DTypeLike[_SCT],
    comments: str = ...,
    delimiter: str | int | Iterable[int] | None = ...,
    skip_header: int = ...,
    skip_footer: int = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | None = ...,
    missing_values: Any = ...,
    filling_values: Any = ...,
    usecols: Sequence[int] | None = ...,
    names: L[True] | str | Collection[str] | None = ...,
    excludelist: Sequence[str] | None = ...,
    deletechars: str = ...,
    replace_space: str = ...,
    autostrip: bool = ...,
    case_sensitive: bool | L["upper", "lower"] = ...,
    defaultfmt: str = ...,
    unpack: bool | None = ...,
    usemask: bool = ...,
    loose: bool = ...,
    invalid_raise: bool = ...,
    max_rows: int | None = ...,
    encoding: str = ...,
    *,
    ndmin: L[0, 1, 2] = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def genfromtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    dtype: DTypeLike,
    comments: str = ...,
    delimiter: str | int | Iterable[int] | None = ...,
    skip_header: int = ...,
    skip_footer: int = ...,
    converters: Mapping[int | str, Callable[[str], Any]] | None = ...,
    missing_values: Any = ...,
    filling_values: Any = ...,
    usecols: Sequence[int] | None = ...,
    names: L[True] | str | Collection[str] | None = ...,
    excludelist: Sequence[str] | None = ...,
    deletechars: str = ...,
    replace_space: str = ...,
    autostrip: bool = ...,
    case_sensitive: bool | L["upper", "lower"] = ...,
    defaultfmt: str = ...,
    unpack: bool | None = ...,
    usemask: bool = ...,
    loose: bool = ...,
    invalid_raise: bool = ...,
    max_rows: int | None = ...,
    encoding: str = ...,
    *,
    ndmin: L[0, 1, 2] = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def recfromtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    *,
    usemask: L[False] = ...,
    **kwargs: object,
) -> np.recarray[Any, np.dtype[np.record]]: ...
@overload
def recfromtxt(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    *,
    usemask: L[True],
    **kwargs: object,
) -> MaskedRecords[Any, np.dtype[np.void]]: ...
@overload
def recfromcsv(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    *,
    usemask: L[False] = ...,
    **kwargs: object,
) -> np.recarray[Any, np.dtype[np.record]]: ...
@overload
def recfromcsv(
    fname: StrPath | Iterable[str] | Iterable[bytes],
    *,
    usemask: L[True],
    **kwargs: object,
) -> MaskedRecords[Any, np.dtype[np.void]]: ...
