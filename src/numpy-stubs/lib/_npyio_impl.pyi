import types
import zipfile
from _typeshed import Incomplete, StrOrBytesPath, StrPath, SupportsKeysAndGetItem, SupportsRead, SupportsWrite
from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, Sequence
from re import Pattern
from typing import IO, Any, ClassVar, Generic, Literal as L, Protocol, Self, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar, deprecated, override

import _numtype as _nt
import numpy as np
from numpy._core.multiarray import packbits, unpackbits
from numpy._globals import _NoValueType
from numpy._typing import ArrayLike, DTypeLike, _DTypeLike, _SupportsArrayFunc
from numpy.ma.mrecords import MaskedRecords

from ._datasource import DataSource as DataSource

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

###

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)

_FName: TypeAlias = StrPath | Iterable[str] | Iterable[bytes]
_FNameRead: TypeAlias = StrPath | SupportsRead[str] | SupportsRead[bytes]
_FNameWrite: TypeAlias = StrPath | SupportsWrite[bytes]

_Converter: TypeAlias = Callable[[str], Incomplete]

@type_check_only
class _SupportsReadSeek(SupportsRead[_T_co], Protocol[_T_co]):
    def seek(self, offset: int, whence: int, /) -> object: ...

###

# undocumented
class BagObj(Generic[_T_co]):
    def __init__(self, /, obj: SupportsKeysAndGetItem[str, _T_co]) -> None: ...
    @override
    def __getattribute__(self, key: str, /) -> _T_co: ...
    @override
    def __dir__(self) -> list[str]: ...

# exported in numpy.lib.nppyio
class NpzFile(Mapping[str, _nt.Array[_ScalarT_co]]):
    _MAX_REPR_ARRAY_COUNT: ClassVar[int] = 5

    zip: zipfile.ZipFile | None
    fid: IO[str] | None
    files: list[str]
    allow_pickle: bool
    pickle_kwargs: Mapping[str, Any] | None
    f: BagObj[NpzFile[_ScalarT_co]] | None

    #
    def __init__(
        self,
        /,
        fid: IO[Any],
        own_fid: bool = False,
        allow_pickle: bool = False,
        pickle_kwargs: Mapping[str, object] | None = None,
        *,
        max_header_size: int = 10_000,
    ) -> None: ...

    #
    def __del__(self) -> None: ...

    #
    def __enter__(self) -> Self: ...
    def __exit__(
        self, cls: type[BaseException] | None, e: BaseException | None, tb: types.TracebackType | None, /
    ) -> None: ...

    #
    @override
    def __len__(self) -> int: ...
    @override
    def __iter__(self) -> Iterator[str]: ...
    @override
    def __getitem__(self, key: str, /) -> _nt.Array[_ScalarT_co]: ...

    #
    @overload
    def get(self, key: str, default: None = None, /) -> _nt.Array[_ScalarT_co] | None: ...
    @overload
    def get(self, key: str, default: _nt.Array[_ScalarT_co] | _T, /) -> _nt.Array[_ScalarT_co] | _T: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def close(self) -> None: ...

# NOTE: Returns `NpzFile` if file is a zip file; returns `ndarray`/`memmap` otherwise
def load(
    file: StrOrBytesPath | _SupportsReadSeek[bytes],
    mmap_mode: L["r+", "r", "w+", "c"] | None = None,
    allow_pickle: bool = False,
    fix_imports: bool = True,
    encoding: L["ASCII", "latin1", "bytes"] = "ASCII",
    *,
    max_header_size: int = 10_000,
) -> Any: ...

#
@overload
def save(file: _FNameWrite, arr: ArrayLike, allow_pickle: bool = True, fix_imports: _NoValueType = ...) -> None: ...
@overload
@deprecated("The 'fix_imports' flag is deprecated in NumPy 2.1.")
def save(file: _FNameWrite, arr: ArrayLike, allow_pickle: bool, fix_imports: bool) -> None: ...
@overload
@deprecated("The 'fix_imports' flag is deprecated in NumPy 2.1.")
def save(file: _FNameWrite, arr: ArrayLike, allow_pickle: bool = True, *, fix_imports: bool) -> None: ...

#
def savez(file: _FNameWrite, *args: ArrayLike, allow_pickle: bool = True, **kwds: ArrayLike) -> None: ...

#
def savez_compressed(file: _FNameWrite, *args: ArrayLike, allow_pickle: bool = True, **kwds: ArrayLike) -> None: ...

# File-like objects only have to implement `__iter__` and,
# optionally, `encoding`
@overload
def loadtxt(
    fname: _FName,
    dtype: None = None,
    comments: str | Sequence[str] | None = "#",
    delimiter: str | None = None,
    converters: Mapping[int | str, _Converter] | _Converter | None = None,
    skiprows: int = 0,
    usecols: int | Sequence[int] | None = None,
    unpack: bool = False,
    ndmin: L[0, 1, 2] = 0,
    encoding: str | None = None,
    max_rows: int | None = None,
    *,
    quotechar: str | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def loadtxt(
    fname: _FName,
    dtype: _DTypeLike[_ScalarT],
    comments: str | Sequence[str] | None = "#",
    delimiter: str | None = None,
    converters: Mapping[int | str, _Converter] | _Converter | None = None,
    skiprows: int = 0,
    usecols: int | Sequence[int] | None = None,
    unpack: bool = False,
    ndmin: L[0, 1, 2] = 0,
    encoding: str | None = None,
    max_rows: int | None = None,
    *,
    quotechar: str | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def loadtxt(
    fname: _FName,
    dtype: DTypeLike,
    comments: str | Sequence[str] | None = "#",
    delimiter: str | None = None,
    converters: Mapping[int | str, _Converter] | _Converter | None = None,
    skiprows: int = 0,
    usecols: int | Sequence[int] | None = None,
    unpack: bool = False,
    ndmin: L[0, 1, 2] = 0,
    encoding: str | None = None,
    max_rows: int | None = None,
    *,
    quotechar: str | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array: ...

#
def savetxt(
    fname: StrPath | _FNameWrite,
    X: ArrayLike,
    fmt: str | Sequence[str] = "%.18e",
    delimiter: str = " ",
    newline: str = "\n",
    header: str = "",
    footer: str = "",
    comments: str = "# ",
    encoding: str | None = None,
) -> None: ...

#
@overload
def fromregex(
    file: _FNameRead, regexp: str | bytes | Pattern[Any], dtype: _DTypeLike[_ScalarT], encoding: str | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def fromregex(
    file: _FNameRead, regexp: str | bytes | Pattern[Any], dtype: DTypeLike, encoding: str | None = None
) -> _nt.Array: ...

#
@overload
def genfromtxt(
    fname: _FName,
    dtype: type[float] = ...,
    comments: str = "#",
    delimiter: str | int | Iterable[int] | None = None,
    skip_header: int = 0,
    skip_footer: int = 0,
    converters: Mapping[int | str, _Converter] | None = None,
    missing_values: Collection[str] | None = None,
    filling_values: Collection[object] | None = None,
    usecols: Sequence[int] | None = None,
    names: L[True] | str | Collection[str] | None = None,
    excludelist: Sequence[str] | None = None,
    deletechars: str = " !#$%&'()*+,-./:;<=>?@[\\]^{|}~",
    replace_space: str = "_",
    autostrip: bool = False,
    case_sensitive: bool | L["upper", "lower"] = True,
    defaultfmt: str = "f%i",
    unpack: bool | None = None,
    usemask: bool = False,
    loose: bool = True,
    invalid_raise: bool = True,
    max_rows: int | None = None,
    encoding: str | None = None,
    *,
    ndmin: L[0, 1, 2] = 0,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def genfromtxt(
    fname: _FName,
    dtype: _DTypeLike[_ScalarT],
    comments: str = "#",
    delimiter: str | int | Iterable[int] | None = None,
    skip_header: int = 0,
    skip_footer: int = 0,
    converters: Mapping[int | str, _Converter] | None = None,
    missing_values: Collection[str] | None = None,
    filling_values: Collection[object] | None = None,
    usecols: Sequence[int] | None = None,
    names: L[True] | str | Collection[str] | None = None,
    excludelist: Sequence[str] | None = None,
    deletechars: str = " !#$%&'()*+,-./:;<=>?@[\\]^{|}~",
    replace_space: str = "_",
    autostrip: bool = False,
    case_sensitive: bool | L["upper", "lower"] = True,
    defaultfmt: str = "f%i",
    unpack: bool | None = None,
    usemask: bool = False,
    loose: bool = True,
    invalid_raise: bool = True,
    max_rows: int | None = None,
    encoding: str | None = None,
    *,
    ndmin: L[0, 1, 2] = 0,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def genfromtxt(
    fname: _FName,
    dtype: DTypeLike | None = ...,
    comments: str = "#",
    delimiter: str | int | Iterable[int] | None = None,
    skip_header: int = 0,
    skip_footer: int = 0,
    converters: Mapping[int | str, _Converter] | None = None,
    missing_values: Collection[str] | None = None,
    filling_values: Collection[object] | None = None,
    usecols: Sequence[int] | None = None,
    names: L[True] | str | Collection[str] | None = None,
    excludelist: Sequence[str] | None = None,
    deletechars: str = " !#$%&'()*+,-./:;<=>?@[\\]^{|}~",
    replace_space: str = "_",
    autostrip: bool = False,
    case_sensitive: bool | L["upper", "lower"] = True,
    defaultfmt: str = "f%i",
    unpack: bool | None = None,
    usemask: bool = False,
    loose: bool = True,
    invalid_raise: bool = True,
    max_rows: int | None = None,
    encoding: str | None = None,
    *,
    ndmin: L[0, 1, 2] = 0,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array: ...

#
@overload
def recfromtxt(fname: _FName, *, usemask: L[False] = False, **kw: object) -> np.recarray[Any, np.dtype[np.record]]: ...
@overload
def recfromtxt(fname: _FName, *, usemask: L[True], **kw: object) -> MaskedRecords[Any, np.dtype[np.void]]: ...

#
@overload
def recfromcsv(fname: _FName, *, usemask: L[False] = False, **kw: object) -> np.recarray[Any, np.dtype[np.record]]: ...
@overload
def recfromcsv(fname: _FName, *, usemask: L[True], **kw: object) -> MaskedRecords[Any, np.dtype[np.void]]: ...
