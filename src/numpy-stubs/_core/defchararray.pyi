from _typeshed import ConvertibleToInt, Incomplete
from typing import Any, Literal as L, Never, Self, SupportsIndex, TypeAlias, overload
from typing_extensions import Buffer, TypeAliasType, TypeVar, override

import _numtype as _nt
import numpy as np
from numpy import _OrderKACF as _Order, _SortKind  # noqa: ICN003
from numpy._typing import (
    _ArrayLikeAnyString_co as _ToAnyCharND,
    _ArrayLikeString_co as _ToStringND,
    _ShapeLike as _ToShape,
)

from ._multiarray_umath import compare_chararrays
from .strings import (
    capitalize,
    center,
    count,
    decode,
    encode,
    endswith,
    expandtabs,
    find,
    index,
    ljust,
    lower,
    lstrip,
    mod,
    multiply,
    partition,
    replace,
    rfind,
    rindex,
    rjust,
    rpartition,
    rstrip,
    startswith,
    str_len,
    strip,
    swapcase,
    title,
    translate,
    upper,
    zfill,
)
from .umath import (
    add,
    equal,
    greater,
    greater_equal,
    isalnum,
    isalpha,
    isdecimal,
    isdigit,
    islower,
    isnumeric,
    isspace,
    istitle,
    isupper,
    less,
    less_equal,
    not_equal,
)

__all__ = [
    "add",
    "array",
    "asarray",
    "capitalize",
    "center",
    "chararray",
    "compare_chararrays",
    "count",
    "decode",
    "encode",
    "endswith",
    "equal",
    "expandtabs",
    "find",
    "greater",
    "greater_equal",
    "index",
    "isalnum",
    "isalpha",
    "isdecimal",
    "isdigit",
    "islower",
    "isnumeric",
    "isspace",
    "istitle",
    "isupper",
    "join",
    "less",
    "less_equal",
    "ljust",
    "lower",
    "lstrip",
    "mod",
    "multiply",
    "not_equal",
    "partition",
    "replace",
    "rfind",
    "rindex",
    "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    "startswith",
    "str_len",
    "strip",
    "swapcase",
    "title",
    "translate",
    "upper",
    "zfill",
]

###

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape, default=_nt.Shape)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.Shape, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[np.character], default=np.dtype[Any], covariant=True)
_CharT = TypeVar("_CharT", bound=np.character, default=Any)

_CharArray = TypeAliasType("_CharArray", chararray[_ShapeT, np.dtype[_CharT]], type_params=(_CharT, _ShapeT))
_BytesArray: TypeAlias = _CharArray[np.bytes_, _ShapeT]
_StrArray: TypeAlias = _CharArray[np.str_, _ShapeT]

_BoolND: TypeAlias = _nt.Array[np.bool, _ShapeT]
_IntND: TypeAlias = _nt.Array[np.intp, _ShapeT]
_ObjectND: TypeAlias = _nt.Array[np.object_, _ShapeT]

###

# re-exported in `numpy.char`
class chararray(np.ndarray[_ShapeT_co, _DTypeT_co]):
    __module__: L["numpy.char"] = "numpy.char"

    @overload  # unicode=False (default)
    def __new__(
        subtype,
        shape: _ToShape,
        itemsize: ConvertibleToInt = 1,
        unicode: L[False] = False,
        buffer: Buffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _Order = "C",
    ) -> _BytesArray: ...
    @overload  # unicode=True (positional)
    def __new__(
        subtype,
        shape: _ToShape,
        itemsize: ConvertibleToInt,
        unicode: L[True],
        buffer: Buffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _Order = "C",
    ) -> _StrArray: ...
    @overload  # unicode=True (keyword)
    def __new__(
        subtype,
        shape: _ToShape,
        itemsize: ConvertibleToInt = 1,
        *,
        unicode: L[True],
        buffer: Buffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _Order = "C",
    ) -> _StrArray: ...

    #
    @override
    def __eq__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ne__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ge__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __gt__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __lt__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __le__(self, other: _nt.ToCharacter_nd, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __add__(self: _StrArray, rhs: _nt.ToStr_nd, /) -> _StrArray: ...
    @overload
    def __add__(self: _BytesArray, rhs: _nt.ToBytes_nd, /) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    #
    @overload  # type: ignore[override]
    def __radd__(self: _StrArray, lhs: _nt.ToStr_nd, /) -> _StrArray: ...
    @overload
    def __radd__(self: _BytesArray, lhs: _nt.ToBytes_nd, /) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __mul__(self, rhs: _nt.ToInteger_0d, /) -> Self: ...
    @overload
    def __mul__(self, rhs: _nt.ToInteger_nd, /) -> chararray[_nt.Shape, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @overload  # type: ignore[override]
    def __rmul__(self, lhs: int, /) -> Self: ...
    @overload
    def __rmul__(self, lhs: _nt.ToInteger_nd, /) -> chararray[_nt.Shape, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __mod__(self, rhs: object, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rmod__(self: Never, rhs: Never, /) -> Any: ...  # type: ignore[misc, override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def argsort(
        self, /, axis: SupportsIndex = -1, kind: _SortKind | None = None, order: None = None
    ) -> _nt.Array[np.intp, _ShapeT_co]: ...
    @overload
    def argsort(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, /, axis: None, kind: _SortKind | None = None, order: None = None
    ) -> _nt.Array1D[np.intp]: ...

    #
    def decode(
        self: _BytesArray, /, encoding: str | None = None, errors: str | None = None
    ) -> _StrArray[_ShapeT_co]: ...
    def encode(
        self: _StrArray, /, encoding: str | None = None, errors: str | None = None
    ) -> _BytesArray[_ShapeT_co]: ...

    #
    @overload
    def center(self: _StrArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def center(self: _BytesArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def count(
        self: _StrArray, /, sub: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...
    @overload
    def count(
        self: _BytesArray, /, sub: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...

    #
    @overload
    def endswith(
        self: _StrArray, /, suffix: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _BoolND: ...
    @overload
    def endswith(
        self: _BytesArray, /, suffix: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _BoolND: ...

    #
    @overload
    def expandtabs(self, /, tabsize: _nt.ToInteger_0d = 8) -> Self: ...
    @overload
    def expandtabs(self, /, tabsize: _nt.ToInteger_nd) -> chararray[_nt.Shape, _DTypeT_co]: ...

    #
    @overload
    def find(
        self: _StrArray, /, sub: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...
    @overload
    def find(
        self: _BytesArray, /, sub: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...

    #
    @overload
    def index(
        self: _StrArray, /, sub: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...
    @overload
    def index(
        self: _BytesArray, /, sub: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...

    #
    @overload
    def join(self: _StrArray, /, seq: _nt.ToStr_nd) -> _StrArray: ...
    @overload
    def join(self: _BytesArray, /, seq: _nt.ToBytes_nd) -> _BytesArray: ...

    #
    @overload
    def ljust(self: _StrArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def ljust(self: _BytesArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def lstrip(self: _StrArray, /, chars: _nt.ToStr_nd | None = None) -> _StrArray: ...
    @overload
    def lstrip(self: _BytesArray, /, chars: _nt.ToBytes_nd | None = None) -> _BytesArray: ...

    #
    @overload  # type: ignore[override]
    def partition(self: _StrArray, /, sep: _nt.ToStr_nd) -> _StrArray: ...
    @overload
    def partition(self: _BytesArray, /, sep: _nt.ToBytes_nd) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def replace(
        self: _StrArray, /, old: _nt.ToStr_nd, new: _nt.ToStr_nd, count: _nt.ToInteger_nd | None = None
    ) -> _StrArray: ...
    @overload
    def replace(
        self: _BytesArray, /, old: _nt.ToBytes_nd, new: _nt.ToBytes_nd, count: _nt.ToInteger_nd | None = None
    ) -> _BytesArray: ...

    #
    @overload
    def rfind(
        self: _StrArray, /, sub: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...
    @overload
    def rfind(
        self: _BytesArray, /, sub: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...

    #
    @overload
    def rindex(
        self: _StrArray, /, sub: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...
    @overload
    def rindex(
        self: _BytesArray, /, sub: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _IntND: ...

    #
    @overload
    def rjust(self: _StrArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def rjust(self: _BytesArray, /, width: _nt.ToInteger_nd, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def rpartition(self: _StrArray, /, sep: _nt.ToStr_nd) -> _StrArray: ...
    @overload
    def rpartition(self: _BytesArray, /, sep: _nt.ToBytes_nd) -> _BytesArray: ...

    #
    @overload
    def rsplit(
        self: _StrArray, /, sep: _nt.ToStr_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
    ) -> _ObjectND: ...
    @overload
    def rsplit(
        self: _BytesArray, /, sep: _nt.ToBytes_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
    ) -> _ObjectND: ...

    #
    @overload
    def rstrip(self: _StrArray, /, chars: _nt.ToStr_nd | None = None) -> _StrArray: ...
    @overload
    def rstrip(self: _BytesArray, /, chars: _nt.ToBytes_nd | None = None) -> _BytesArray: ...

    #
    @overload
    def split(
        self: _StrArray, /, sep: _nt.ToStr_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
    ) -> _ObjectND: ...
    @overload
    def split(
        self: _BytesArray, /, sep: _nt.ToBytes_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
    ) -> _ObjectND: ...

    #
    def splitlines(self, /, keepends: _nt.ToBool_nd | None = None) -> _ObjectND: ...

    #
    @overload
    def startswith(
        self: _StrArray, /, prefix: _nt.ToStr_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _BoolND: ...
    @overload
    def startswith(
        self: _BytesArray, /, prefix: _nt.ToBytes_nd, start: _nt.ToInteger_nd = 0, end: _nt.ToInteger_nd | None = None
    ) -> _BoolND: ...

    #
    @overload
    def strip(self: _StrArray, /, chars: _nt.ToStr_nd | None = None) -> _StrArray: ...
    @overload
    def strip(self: _BytesArray, /, chars: _nt.ToBytes_nd | None = None) -> _BytesArray: ...

    #
    @overload
    def translate(self: _StrArray, /, table: _nt.ToStr_nd, deletechars: _nt.ToStr_nd | None = None) -> _StrArray: ...
    @overload
    def translate(
        self: _BytesArray, /, table: _nt.ToBytes_nd, deletechars: _nt.ToBytes_nd | None = None
    ) -> _BytesArray: ...

    #
    def zfill(self, /, width: _nt.ToInteger_nd) -> chararray[Incomplete, _DTypeT_co]: ...
    def capitalize(self) -> Self: ...
    def title(self) -> Self: ...
    def swapcase(self) -> Self: ...
    def lower(self) -> Self: ...
    def upper(self) -> Self: ...

    #
    def isalnum(self) -> _BoolND[_ShapeT_co]: ...
    def isalpha(self) -> _BoolND[_ShapeT_co]: ...
    def isdigit(self) -> _BoolND[_ShapeT_co]: ...
    def islower(self) -> _BoolND[_ShapeT_co]: ...
    def isspace(self) -> _BoolND[_ShapeT_co]: ...
    def istitle(self) -> _BoolND[_ShapeT_co]: ...
    def isupper(self) -> _BoolND[_ShapeT_co]: ...
    def isnumeric(self) -> _BoolND[_ShapeT_co]: ...
    def isdecimal(self) -> _BoolND[_ShapeT_co]: ...

#
@overload
def join(sep: _nt.ToStr_nd, seq: _nt.ToStr_nd) -> _nt.Array[np.str_]: ...
@overload
def join(sep: _nt.ToBytes_nd, seq: _nt.ToBytes_nd) -> _nt.Array[np.bytes_]: ...
@overload
def join(sep: _nt.ToString_nd, seq: _nt.ToString_nd) -> _nt.StringArrayND: ...
@overload
def join(sep: _ToStringND, seq: _ToStringND) -> _nt.Array[np.str_] | _nt.StringArrayND: ...

#
@overload
def split(a: _nt.ToStr_nd, sep: _nt.ToStr_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None) -> _ObjectND: ...
@overload
def split(
    a: _nt.ToBytes_nd, sep: _nt.ToBytes_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
) -> _ObjectND: ...
@overload
def split(
    a: _nt.ToString_nd, sep: _nt.ToString_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
) -> _ObjectND: ...
@overload
def split(a: _ToStringND, sep: _ToStringND | None = None, maxsplit: _nt.ToInteger_nd | None = None) -> _ObjectND: ...

#
@overload
def rsplit(a: _nt.ToStr_nd, sep: _nt.ToStr_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None) -> _ObjectND: ...
@overload
def rsplit(
    a: _nt.ToBytes_nd, sep: _nt.ToBytes_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
) -> _ObjectND: ...
@overload
def rsplit(
    a: _nt.ToString_nd, sep: _nt.ToString_nd | None = None, maxsplit: _nt.ToInteger_nd | None = None
) -> _ObjectND: ...
@overload
def rsplit(a: _ToStringND, sep: _ToStringND | None = None, maxsplit: _nt.ToInteger_nd | None = None) -> _ObjectND: ...

#
def splitlines(a: _ToAnyCharND, keepends: _nt.ToBool_nd | None = None) -> _ObjectND: ...

#
@overload  # str array-like
def array(  # type: ignore[overload-overlap]
    obj: _nt.ToStr_nd,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _StrArray: ...
@overload  # bytes array-like
def array(  # type: ignore[overload-overlap]
    obj: _nt.ToBytes_nd,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _BytesArray: ...
@overload  # unicode=False
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    *,
    unicode: L[False],
    order: _Order | None = None,
) -> _BytesArray: ...
@overload  # unicode=True
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    *,
    unicode: L[True],
    order: _Order | None = None,
) -> _StrArray: ...
@overload  # fallback
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _CharArray: ...

#
@overload  # str array-like
def asarray(  # type: ignore[overload-overlap]
    obj: _nt.ToStr_nd, itemsize: int | None = None, unicode: bool | None = None, order: _Order | None = None
) -> _StrArray: ...
@overload  # bytes array-like
def asarray(  # type: ignore[overload-overlap]
    obj: _nt.ToBytes_nd, itemsize: int | None = None, unicode: bool | None = None, order: _Order | None = None
) -> _BytesArray: ...
@overload  # unicode=False
def asarray(
    obj: object, itemsize: int | None = None, *, unicode: L[False], order: _Order | None = None
) -> _BytesArray: ...
@overload  # unicode=True
def asarray(
    obj: object, itemsize: int | None = None, *, unicode: L[True], order: _Order | None = None
) -> _StrArray: ...
@overload  # falback
def asarray(
    obj: object, itemsize: int | None = None, unicode: bool | None = None, order: _Order | None = None
) -> _CharArray: ...
