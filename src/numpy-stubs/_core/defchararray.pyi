from _typeshed import ConvertibleToInt
from typing import Any, Literal as L, SupportsIndex, TypeAlias, overload
from typing_extensions import Never, Self, TypeVar, override

import numpy as np
from numpy import _OrderKACF as _Order, _SortKind, _SupportsBuffer  # noqa: ICN003
from numpy._typing import (
    NDArray,
    _ArrayLikeAnyString_co as _ToAnyCharND,
    _ArrayLikeBool_co as _ToBoolND,
    _ArrayLikeBytes_co as _ToBytesND,
    _ArrayLikeInt_co as _ToIntND,
    _ArrayLikeStr_co as _ToStrND,
    _ArrayLikeString_co as _ToStringND,
    _IntLike_co as _ToInt,
    _ShapeLike as _ToShape,
    _SupportsArray as _CanArray,
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

_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[np.character], covariant=True)
_CharT = TypeVar("_CharT", bound=np.character, default=Any)

_CharArray: TypeAlias = chararray[tuple[int, ...], np.dtype[_CharT]]
_CharArray1D: TypeAlias = chararray[tuple[int], np.dtype[_CharT]]

_BytesArray: TypeAlias = _CharArray[np.bytes_]
_StrArray: TypeAlias = _CharArray[np.str_]

_BoolND: TypeAlias = NDArray[np.bool]
_IntND: TypeAlias = NDArray[np.intp]
_BytesND: TypeAlias = NDArray[np.bytes_]
_StrND: TypeAlias = NDArray[np.str_]
_ObjectND: TypeAlias = NDArray[np.object_]
_StringND: TypeAlias = np.ndarray[tuple[int, ...], np.dtypes.StringDType]
_CanStringND: TypeAlias = _CanArray[np.dtypes.StringDType]

_ToCharND: TypeAlias = _ToStrND | _ToBytesND

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
        buffer: _SupportsBuffer | None = None,
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
        buffer: _SupportsBuffer | None = None,
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
        buffer: _SupportsBuffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _Order = "C",
    ) -> _StrArray: ...

    #
    @override
    def __eq__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ne__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ge__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __gt__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __lt__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __le__(self, other: _ToCharND, /) -> _BoolND: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __add__(self: _StrArray, rhs: _ToStrND, /) -> _StrArray: ...
    @overload
    def __add__(self: _BytesArray, rhs: _ToBytesND, /) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    #
    @overload  # type: ignore[override]
    def __radd__(self: _StrArray, lhs: _ToStrND, /) -> _StrArray: ...
    @overload
    def __radd__(self: _BytesArray, lhs: _ToBytesND, /) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __mul__(self, rhs: _ToIntND, /) -> chararray[tuple[int, ...], _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rmul__(self, lhs: _ToIntND, /) -> chararray[tuple[int, ...], _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __mod__(self, rhs: object, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rmod__(self: Never, rhs: Never, /) -> Any: ...  # type: ignore[override, misc]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def argsort(
        self,
        /,
        axis: SupportsIndex = -1,
        kind: _SortKind | None = None,
        order: None = None,
    ) -> np.ndarray[_ShapeT_co, np.dtype[np.intp]]: ...
    @overload
    def argsort(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: None,
        kind: _SortKind | None = None,
        order: None = None,
    ) -> np.ndarray[tuple[int], np.dtype[np.intp]]: ...

    #
    def decode(
        self: _BytesArray,
        /,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> chararray[_ShapeT_co, np.dtype[np.str_]]: ...
    def encode(
        self: _StrArray,
        /,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> chararray[_ShapeT_co, np.dtype[np.bytes_]]: ...

    #
    @overload
    def center(self: _StrArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def center(self: _BytesArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def count(self: _StrArray, /, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...
    @overload
    def count(self: _BytesArray, /, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...

    #
    @overload
    def endswith(self: _StrArray, /, suffix: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _BoolND: ...
    @overload
    def endswith(self: _BytesArray, /, suffix: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _BoolND: ...

    #
    @overload
    def expandtabs(self, /, tabsize: _ToInt = 8) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def expandtabs(self, /, tabsize: _ToIntND) -> chararray[tuple[int, ...], _DTypeT_co]: ...

    #
    @overload
    def find(self: _StrArray, /, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...
    @overload
    def find(self: _BytesArray, /, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...

    #
    @overload
    def index(self: _StrArray, /, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...
    @overload
    def index(self: _BytesArray, /, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...

    #
    @overload
    def join(self: _StrArray, /, seq: _ToStrND) -> _StrArray: ...
    @overload
    def join(self: _BytesArray, /, seq: _ToBytesND) -> _BytesArray: ...

    #
    @overload
    def ljust(self: _StrArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def ljust(self: _BytesArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def lstrip(self: _StrArray, /, chars: _ToStrND | None = None) -> _StrArray: ...
    @overload
    def lstrip(self: _BytesArray, /, chars: _ToBytesND | None = None) -> _BytesArray: ...

    #
    @overload  # type: ignore[override]
    def partition(self: _StrArray, /, sep: _ToStrND) -> _StrArray: ...
    @overload
    def partition(self: _BytesArray, /, sep: _ToBytesND) -> _BytesArray: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def replace(self: _StrArray, /, old: _ToStrND, new: _ToStrND, count: _ToIntND | None = None) -> _StrArray: ...
    @overload
    def replace(self: _BytesArray, /, old: _ToBytesND, new: _ToBytesND, count: _ToIntND | None = None) -> _BytesArray: ...

    #
    @overload
    def rfind(self: _StrArray, /, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...
    @overload
    def rfind(self: _BytesArray, /, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...

    #
    @overload
    def rindex(self: _StrArray, /, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...
    @overload
    def rindex(self: _BytesArray, /, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _IntND: ...

    #
    @overload
    def rjust(self: _StrArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrArray: ...
    @overload
    def rjust(self: _BytesArray, /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _BytesArray: ...

    #
    @overload
    def rpartition(self: _StrArray, /, sep: _ToStrND) -> _StrArray: ...
    @overload
    def rpartition(self: _BytesArray, /, sep: _ToBytesND) -> _BytesArray: ...

    #
    @overload
    def rsplit(self: _StrArray, /, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
    @overload
    def rsplit(self: _BytesArray, /, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...

    #
    @overload
    def rstrip(self: _StrArray, /, chars: _ToStrND | None = None) -> _StrArray: ...
    @overload
    def rstrip(self: _BytesArray, /, chars: _ToBytesND | None = None) -> _BytesArray: ...

    #
    @overload
    def split(self: _StrArray, /, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
    @overload
    def split(self: _BytesArray, /, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...

    #
    def splitlines(self, /, keepends: _ToBoolND | None = None) -> _ObjectND: ...

    #
    @overload
    def startswith(self: _StrArray, /, prefix: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _BoolND: ...
    @overload
    def startswith(self: _BytesArray, /, prefix: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> _BoolND: ...

    #
    @overload
    def strip(self: _StrArray, /, chars: _ToStrND | None = None) -> _StrArray: ...
    @overload
    def strip(self: _BytesArray, /, chars: _ToBytesND | None = None) -> _BytesArray: ...

    #
    @overload
    def translate(self: _StrArray, /, table: _ToStrND, deletechars: _ToStrND | None = None) -> _StrArray: ...
    @overload
    def translate(self: _BytesArray, /, table: _ToBytesND, deletechars: _ToBytesND | None = None) -> _BytesArray: ...

    #
    def zfill(self, /, width: _ToIntND) -> chararray[tuple[int, ...], _DTypeT_co]: ...
    def capitalize(self) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    def title(self) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    def swapcase(self) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    def lower(self) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    def upper(self) -> chararray[_ShapeT_co, _DTypeT_co]: ...

    #
    def isalnum(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isalpha(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isdigit(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def islower(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isspace(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def istitle(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isupper(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isnumeric(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...
    def isdecimal(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool]]: ...

#
@overload
def join(sep: _ToStrND, seq: _ToStrND) -> _StrND: ...  # type: ignore[overload-overlap]
@overload
def join(sep: _ToBytesND, seq: _ToBytesND) -> _BytesND: ...
@overload
def join(sep: _CanStringND, seq: _CanStringND) -> _StringND: ...
@overload
def join(sep: _ToStringND, seq: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def split(a: _ToStrND, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def split(a: _ToBytesND, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def split(a: _CanStringND, sep: _CanStringND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def split(a: _ToStringND, sep: _ToStringND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...

#
@overload
def rsplit(a: _ToStrND, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def rsplit(a: _ToBytesND, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def rsplit(a: _CanStringND, sep: _CanStringND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...
@overload
def rsplit(a: _ToStringND, sep: _ToStringND | None = None, maxsplit: _ToIntND | None = None) -> _ObjectND: ...

#
def splitlines(a: _ToAnyCharND, keepends: _ToBoolND | None = None) -> _ObjectND: ...

#
@overload  # str array-like
def array(  # type: ignore[overload-overlap]
    obj: _ToStrND,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _StrArray: ...
@overload  # bytes array-like
def array(  # type: ignore[overload-overlap]
    obj: _ToBytesND,
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
    obj: _ToStrND,
    itemsize: int | None = None,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _StrArray: ...
@overload  # bytes array-like
def asarray(  # type: ignore[overload-overlap]
    obj: _ToBytesND,
    itemsize: int | None = None,
    unicode: bool | None = None,
    order: _Order | None = None,
) -> _BytesArray: ...
@overload  # unicode=False
def asarray(obj: object, itemsize: int | None = None, *, unicode: L[False], order: _Order | None = None) -> _BytesArray: ...
@overload  # unicode=True
def asarray(obj: object, itemsize: int | None = None, *, unicode: L[True], order: _Order | None = None) -> _StrArray: ...
@overload  # falback
def asarray(obj: object, itemsize: int | None = None, unicode: bool | None = None, order: _Order | None = None) -> _CharArray: ...
