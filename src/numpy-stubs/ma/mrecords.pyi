from _typeshed import Incomplete
from typing import Any
from typing_extensions import Self, TypeVar, override

import numpy as np

from . import MaskedArray

__all__ = ["MaskedRecords", "addfield", "fromarrays", "fromrecords", "fromtextfile", "mrecarray"]

_ShapeType_co = TypeVar("_ShapeType_co", covariant=True, bound=tuple[int, ...])
_DType_co = TypeVar("_DType_co", bound=np.dtype[Any], covariant=True)

class MaskedRecords(MaskedArray[_ShapeType_co, _DType_co]):
    _mask: Any
    _fill_value: Any
    def __new__(
        cls,
        shape: Incomplete,
        dtype: Incomplete = ...,
        buf: Incomplete = ...,
        offset: Incomplete = ...,
        strides: Incomplete = ...,
        formats: Incomplete = ...,
        names: Incomplete = ...,
        titles: Incomplete = ...,
        byteorder: Incomplete = ...,
        aligned: Incomplete = ...,
        mask: Incomplete = ...,
        hard_mask: Incomplete = ...,
        fill_value: Incomplete = ...,
        keep_mask: Incomplete = ...,
        copy: Incomplete = ...,
        **options: Incomplete,
    ) -> Self: ...
    @property
    def _data(self) -> Incomplete: ...
    @property
    def _fieldmask(self) -> Incomplete: ...
    @override
    def __array_finalize__(self, obj: Incomplete) -> Incomplete: ...
    @override
    def __len__(self) -> int: ...
    @override
    def __getattribute__(self, attr: Incomplete) -> Incomplete: ...
    @override
    def __setattr__(self, attr: Incomplete, val: Incomplete) -> None: ...
    @override
    def __getitem__(self, indx: Incomplete) -> Incomplete: ...
    @override
    def __setitem__(self, indx: Incomplete, value: Incomplete) -> None: ...
    @override
    def view(self, dtype: Incomplete = ..., type: Incomplete = ...) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def harden_mask(self) -> Incomplete: ...
    @override
    def soften_mask(self) -> Incomplete: ...
    @override
    def copy(self) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tolist(self, fill_value: Incomplete = ...) -> Incomplete: ...
    @override
    def __reduce__(self) -> Incomplete: ...

def fromarrays(
    arraylist: Incomplete,
    dtype: Incomplete = ...,
    shape: Incomplete = ...,
    formats: Incomplete = ...,
    names: Incomplete = ...,
    titles: Incomplete = ...,
    aligned: Incomplete = ...,
    byteorder: Incomplete = ...,
    fill_value: Incomplete = ...,
) -> Incomplete: ...
def fromrecords(
    reclist: Incomplete,
    dtype: Incomplete = ...,
    shape: Incomplete = ...,
    formats: Incomplete = ...,
    names: Incomplete = ...,
    titles: Incomplete = ...,
    aligned: Incomplete = ...,
    byteorder: Incomplete = ...,
    fill_value: Incomplete = ...,
    mask: Incomplete = ...,
) -> Incomplete: ...
def fromtextfile(
    fname: Incomplete,
    delimiter: Incomplete = ...,
    commentchar: Incomplete = ...,
    missingchar: Incomplete = ...,
    varnames: Incomplete = ...,
    vartypes: Incomplete = ...,
    *,
    delimitor: Incomplete = ...,
) -> Incomplete: ...
def addfield(mrecord: Incomplete, newfield: Incomplete, newfieldname: Incomplete = ...) -> Incomplete: ...

mrecarray = MaskedRecords
