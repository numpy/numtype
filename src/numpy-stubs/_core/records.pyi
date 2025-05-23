from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Iterable, Sequence
from typing import IO, Any, ClassVar, Literal as L, Protocol, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import Buffer, TypeVar, override

import _numtype as _nt
import numpy as np
from numpy import _ByteOrder, _OrderKACF  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, _ArrayLikeVoid_co, _ShapeLike

__all__ = [
    "array",
    "find_duplicate",
    "format_parser",
    "fromarrays",
    "fromfile",
    "fromrecords",
    "fromstring",
    "recarray",
    "record",
]

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.Shape, default=_nt.Shape, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype[Any], covariant=True)

# TODO(jorenham): Use `_nt.Shape` instead of `Any` as shape-type
_RecArray: TypeAlias = recarray[Any, np.dtype[_ScalarT]]

@type_check_only
class _SupportsReadInto(Protocol):
    def seek(self, offset: int, whence: int, /) -> object: ...
    def tell(self, /) -> int: ...
    def readinto(self, buffer: memoryview, /) -> int: ...

###

# exported in `numpy.rec`
class format_parser:
    dtype: np.dtype[np.void]
    def __init__(
        self,
        /,
        formats: DTypeLike,
        names: str | Sequence[str] | None,
        titles: str | Sequence[str] | None,
        aligned: bool = False,
        byteorder: _ByteOrder | None = None,
    ) -> None: ...

class record(np.void):  # type: ignore[misc]
    __name__: ClassVar[L["record"]] = "record"
    __module__: L["numpy"] = "numpy"

    def pprint(self) -> str: ...
    @override
    def __getattribute__(self, attr: str, /) -> Any: ...
    @override
    def __setattr__(self, attr: str, val: ArrayLike, /) -> None: ...
    @overload
    def __getitem__(self, key: str | SupportsIndex, /) -> Incomplete: ...
    @overload
    def __getitem__(self, key: list[str], /) -> record: ...

# exported in `numpy.rec`
class recarray(np.ndarray[_ShapeT_co, _DTypeT_co]):
    @overload
    def __new__(
        subtype,
        shape: _ShapeLike,
        dtype: None = None,
        buf: Buffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ShapeLike | None = None,
        *,
        formats: DTypeLike,
        names: str | Sequence[str] | None = None,
        titles: str | Sequence[str] | None = None,
        byteorder: _ByteOrder | None = None,
        aligned: bool = False,
        order: _OrderKACF = "C",
    ) -> _RecArray[record]: ...
    @overload
    def __new__(
        subtype,
        shape: _ShapeLike,
        dtype: DTypeLike,
        buf: Buffer | None = None,
        offset: SupportsIndex = ...,
        strides: _ShapeLike | None = None,
        formats: None = None,
        names: None = None,
        titles: None = None,
        byteorder: None = None,
        aligned: L[False] = False,
        order: _OrderKACF = "C",
    ) -> _RecArray[Incomplete]: ...
    @override
    def __getattribute__(self, attr: str, /) -> Any: ...
    @override
    def __setattr__(self, attr: str, val: ArrayLike, /) -> None: ...
    @override
    def __array_finalize__(self, /, obj: object) -> None: ...

    #
    @overload
    def field(self, /, attr: int | str, val: ArrayLike) -> None: ...
    @overload
    def field(self, /, attr: int | str, val: None = None) -> Incomplete: ...

# exported in `numpy.rec`
def find_duplicate(list: Iterable[_T]) -> list[_T]: ...

# exported in `numpy.rec`
@overload
def fromarrays(
    arrayList: Iterable[ArrayLike],
    dtype: DTypeLike | None = None,
    shape: _ShapeLike | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
) -> _RecArray[Incomplete]: ...
@overload
def fromarrays(
    arrayList: Iterable[ArrayLike],
    dtype: None = None,
    shape: _ShapeLike | None = None,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
) -> _RecArray[record]: ...

# exported in `numpy.rec`
@overload
def fromrecords(
    recList: _ArrayLikeVoid_co | _nt.SequenceND[tuple[Incomplete, ...]],
    dtype: DTypeLike | None = None,
    shape: _ShapeLike | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
) -> _RecArray[record]: ...
@overload
def fromrecords(
    recList: _ArrayLikeVoid_co | _nt.SequenceND[tuple[Incomplete, ...]],
    dtype: None = None,
    shape: _ShapeLike | None = None,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
) -> _RecArray[record]: ...

# exported in `numpy.rec`
@overload
def fromstring(
    datastring: Buffer,
    dtype: DTypeLike,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
) -> _RecArray[record]: ...
@overload
def fromstring(
    datastring: Buffer,
    dtype: None = None,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
) -> _RecArray[record]: ...

#
def get_remaining_size(fd: IO[Any]) -> int: ...  # undocumented

# exported in `numpy.rec`
@overload
def fromfile(
    fd: StrOrBytesPath | _SupportsReadInto,
    dtype: DTypeLike,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
) -> _RecArray[Incomplete]: ...
@overload
def fromfile(
    fd: StrOrBytesPath | _SupportsReadInto,
    dtype: None = None,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
) -> _RecArray[record]: ...

# exported in `numpy.rec`
@overload
def array(  # type: ignore[overload-overlap]
    obj: _ScalarT | _nt.Array[_ScalarT],
    dtype: None = None,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
    copy: bool = True,
) -> _RecArray[_ScalarT]: ...
@overload
def array(
    obj: ArrayLike,
    dtype: DTypeLike,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
    copy: bool = True,
) -> _RecArray[Incomplete]: ...
@overload
def array(
    obj: ArrayLike,
    dtype: None = None,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
    copy: bool = True,
) -> _RecArray[record]: ...
@overload
def array(
    obj: None,
    dtype: DTypeLike,
    shape: _ShapeLike,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
    copy: bool = True,
) -> _RecArray[Incomplete]: ...
@overload
def array(
    obj: None,
    dtype: None = None,
    *,
    shape: _ShapeLike,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
    copy: bool = True,
) -> _RecArray[record]: ...
@overload
def array(
    obj: _SupportsReadInto,
    dtype: DTypeLike,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    formats: None = None,
    names: None = None,
    titles: None = None,
    aligned: bool = False,
    byteorder: None = None,
    copy: bool = True,
) -> _RecArray[Incomplete]: ...
@overload
def array(
    obj: _SupportsReadInto,
    dtype: None = None,
    shape: _ShapeLike | None = None,
    offset: int = 0,
    strides: tuple[int, ...] | None = None,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = None,
    titles: str | Sequence[str] | None = None,
    aligned: bool = False,
    byteorder: _ByteOrder | None = None,
    copy: bool = True,
) -> _RecArray[record]: ...
