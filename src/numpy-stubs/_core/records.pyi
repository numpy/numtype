from _typeshed import Incomplete, StrOrBytesPath
from collections.abc import Iterable, Sequence
from types import EllipsisType
from typing import Any, Literal, Protocol, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLikeInt_co,
    _ArrayLikeVoid_co,
    _NestedSequence,
    _Shape,
    _ShapeLike,
)

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
_SCT = TypeVar("_SCT", bound=np.generic)
_DType_co = TypeVar("_DType_co", bound=np.dtype[Any], covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)

_RecArray: TypeAlias = recarray[Any, np.dtype[_SCT]]

@type_check_only
class _SupportsReadInto(Protocol):
    def seek(self, offset: int, whence: int, /) -> object: ...
    def tell(self, /) -> int: ...
    def readinto(self, buffer: memoryview, /) -> int: ...

class record(np.void):
    def pprint(self) -> str: ...
    def __getattribute__(self, attr: str, /) -> Any: ...
    def __setattr__(self, attr: str, val: ArrayLike, /) -> None: ...
    @overload
    def __getitem__(self, key: str | SupportsIndex, /) -> Any: ...
    @overload
    def __getitem__(self, key: list[str], /) -> record: ...

class recarray(np.ndarray[_ShapeT_co, _DType_co]):
    # NOTE: While not strictly mandatory, we're demanding here that arguments
    # for the `format_parser`- and `dtype`-based dtype constructors are
    # mutually exclusive
    @overload
    def __new__(
        cls,
        shape: _ShapeLike,
        dtype: None = ...,
        buf: np._SupportsBuffer | None = ...,
        offset: SupportsIndex = ...,
        strides: _ShapeLike | None = ...,
        *,
        formats: DTypeLike,
        names: str | Sequence[str] | None = ...,
        titles: str | Sequence[str] | None = ...,
        byteorder: np._ByteOrder | None = ...,
        aligned: bool = ...,
        order: np._OrderKACF = ...,
    ) -> _RecArray[record]: ...
    @overload
    def __new__(
        cls,
        shape: _ShapeLike,
        dtype: DTypeLike,
        buf: np._SupportsBuffer | None = ...,
        offset: SupportsIndex = ...,
        strides: _ShapeLike | None = ...,
        formats: None = ...,
        names: None = ...,
        titles: None = ...,
        byteorder: None = ...,
        aligned: Literal[False] = ...,
        order: np._OrderKACF = ...,
    ) -> _RecArray[Any]: ...
    def __array_finalize__(self, obj: Incomplete) -> None: ...
    def __getattribute__(self, attr: str) -> Any: ...
    def __setattr__(self, attr: str, val: ArrayLike) -> None: ...
    @overload
    def __getitem__(self, indx: (SupportsIndex | _ArrayLikeInt_co | tuple[SupportsIndex | _ArrayLikeInt_co, ...])) -> Any: ...
    @overload
    def __getitem__(
        self: _RecArray[np.void],
        indx: slice
        | EllipsisType
        | SupportsIndex
        | _ArrayLikeInt_co
        | tuple[slice | EllipsisType | _ArrayLikeInt_co | SupportsIndex | None, ...]
        | None,
    ) -> recarray[_Shape, _DType_co]: ...
    @overload
    def __getitem__(
        self,
        indx: slice
        | EllipsisType
        | SupportsIndex
        | _ArrayLikeInt_co
        | tuple[slice | EllipsisType | _ArrayLikeInt_co | SupportsIndex | None, ...]
        | None,
    ) -> np.ndarray[_Shape, _DType_co]: ...
    @overload
    def __getitem__(self, indx: str) -> NDArray[Any]: ...
    @overload
    def __getitem__(self, indx: list[str]) -> recarray[_ShapeT_co, np.dtype[record]]: ...
    @overload
    def field(self, attr: int | str, val: None = ...) -> Any: ...
    @overload
    def field(self, attr: int | str, val: ArrayLike) -> None: ...

class format_parser:
    dtype: np.dtype[np.void]
    def __init__(
        self,
        formats: DTypeLike,
        names: str | Sequence[str] | None,
        titles: str | Sequence[str] | None,
        aligned: bool = ...,
        byteorder: np._ByteOrder | None = ...,
    ) -> None: ...

@overload
def fromarrays(
    arrayList: Iterable[ArrayLike],
    dtype: DTypeLike = ...,
    shape: _ShapeLike | None = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
) -> _RecArray[Any]: ...
@overload
def fromarrays(
    arrayList: Iterable[ArrayLike],
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
) -> _RecArray[record]: ...
@overload
def fromrecords(
    recList: _ArrayLikeVoid_co | tuple[Any, ...] | _NestedSequence[tuple[Any, ...]],
    dtype: DTypeLike = ...,
    shape: _ShapeLike | None = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
) -> _RecArray[record]: ...
@overload
def fromrecords(
    recList: _ArrayLikeVoid_co | tuple[Any, ...] | _NestedSequence[tuple[Any, ...]],
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    *,
    formats: DTypeLike = ...,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
) -> _RecArray[record]: ...
@overload
def fromstring(
    datastring: np._SupportsBuffer,
    dtype: DTypeLike,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
) -> _RecArray[record]: ...
@overload
def fromstring(
    datastring: np._SupportsBuffer,
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
) -> _RecArray[record]: ...
@overload
def fromfile(
    fd: StrOrBytesPath | _SupportsReadInto,
    dtype: DTypeLike,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
) -> _RecArray[Any]: ...
@overload
def fromfile(
    fd: StrOrBytesPath | _SupportsReadInto,
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
) -> _RecArray[record]: ...
@overload
def array(
    obj: _SCT | NDArray[_SCT],
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
    copy: bool = ...,
) -> _RecArray[_SCT]: ...
@overload
def array(
    obj: ArrayLike,
    dtype: DTypeLike,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
    copy: bool = ...,
) -> _RecArray[Any]: ...
@overload
def array(
    obj: ArrayLike,
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
    copy: bool = ...,
) -> _RecArray[record]: ...
@overload
def array(
    obj: None,
    dtype: DTypeLike,
    shape: _ShapeLike,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
    copy: bool = ...,
) -> _RecArray[Any]: ...
@overload
def array(
    obj: None,
    dtype: None = ...,
    *,
    shape: _ShapeLike,
    offset: int = ...,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
    copy: bool = ...,
) -> _RecArray[record]: ...
@overload
def array(
    obj: _SupportsReadInto,
    dtype: DTypeLike,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    formats: None = ...,
    names: None = ...,
    titles: None = ...,
    aligned: bool = ...,
    byteorder: None = ...,
    copy: bool = ...,
) -> _RecArray[Any]: ...
@overload
def array(
    obj: _SupportsReadInto,
    dtype: None = ...,
    shape: _ShapeLike | None = ...,
    offset: int = ...,
    *,
    formats: DTypeLike,
    names: str | Sequence[str] | None = ...,
    titles: str | Sequence[str] | None = ...,
    aligned: bool = ...,
    byteorder: np._ByteOrder | None = ...,
    copy: bool = ...,
) -> _RecArray[record]: ...
def find_duplicate(list: Iterable[_T]) -> list[_T]: ...
