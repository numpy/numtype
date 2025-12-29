from _typeshed import Incomplete
from typing import Any, Self
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np

from . import MaskedArray

__all__ = ["MaskedRecords", "addfield", "fromarrays", "fromrecords", "fromtextfile", "mrecarray"]

_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.Shape, default=_nt.AnyShape, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)

###

class MaskedRecords(MaskedArray[_ShapeT_co, _DTypeT_co]):
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

    #
    @property
    def _data(self) -> Incomplete: ...
    @property
    def _fieldmask(self) -> Incomplete: ...

    #
    @override
    def __array_finalize__(self, obj: Incomplete) -> Incomplete: ...

    #
    @override
    def __len__(self) -> int: ...

    #
    @override
    def __getattribute__(self, attr: Incomplete) -> Incomplete: ...
    @override
    def __setattr__(self, attr: Incomplete, val: Incomplete) -> None: ...

    #
    @override
    def __getitem__(self, indx: Incomplete) -> Incomplete: ...
    @override
    def __setitem__(self, indx: Incomplete, value: Incomplete) -> None: ...

    #
    @override
    def __reduce__(self) -> Incomplete: ...

    #
    @override
    def view(self, dtype: Incomplete | None = None, type: Incomplete | None = None) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def harden_mask(self) -> Incomplete: ...
    @override
    def soften_mask(self) -> Incomplete: ...
    @override
    def copy(self) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tolist(self, fill_value: Incomplete | None = None) -> Incomplete: ...

mrecarray = MaskedRecords

def fromarrays(
    arraylist: Incomplete,
    dtype: Incomplete | None = None,
    shape: Incomplete | None = None,
    formats: Incomplete | None = None,
    names: Incomplete | None = None,
    titles: Incomplete | None = None,
    aligned: bool = False,
    byteorder: Incomplete | None = None,
    fill_value: Incomplete | None = None,
) -> Incomplete: ...

#
def fromrecords(
    reclist: Incomplete,
    dtype: Incomplete | None = None,
    shape: Incomplete | None = None,
    formats: Incomplete | None = None,
    names: Incomplete | None = None,
    titles: Incomplete | None = None,
    aligned: bool = False,
    byteorder: Incomplete | None = None,
    fill_value: Incomplete | None = None,
    mask: Incomplete = ...,
) -> Incomplete: ...

#
def fromtextfile(
    fname: Incomplete,
    delimiter: Incomplete | None = None,
    commentchar: str = "#",
    missingchar: str = "",
    varnames: Incomplete | None = None,
    vartypes: Incomplete | None = None,
) -> Incomplete: ...

#
def addfield(mrecord: Incomplete, newfield: Incomplete, newfieldname: Incomplete | None = None) -> Incomplete: ...
