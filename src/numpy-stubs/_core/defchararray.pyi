from _typeshed import ConvertibleToInt
from typing import Any, Literal as L, SupportsIndex, TypeAlias, overload
from typing_extensions import Self, TypeVar, override

import numpy as np
import numpy.typing as npt
from numpy import _OrderKACF, _SupportsBuffer  # noqa: ICN003
from numpy._typing import (
    _ArrayLikeAnyString_co as _ToAnyCharND,
    _ArrayLikeBool_co as _ToBoolND,
    _ArrayLikeBytes_co as _ToBytesND,
    _ArrayLikeInt_co as _ToIntND,
    _ArrayLikeStr_co as _ToStrND,
    _ArrayLikeString_co as _ToStringND,
    _IntLike_co as _ToInt,
    _Shape,
    _ShapeLike as _ToShape,
    _SupportsArray as _CanArray,
)

from ._multiarray_umath import compare_chararrays
from .strings import str_len

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
_CharT = TypeVar("_CharT", bound=np.character)

_CharArray: TypeAlias = chararray[tuple[int, ...], np.dtype[_CharT]]
_CharArray1D: TypeAlias = chararray[tuple[int], np.dtype[_CharT]]

_ToCharND: TypeAlias = _ToStrND | _ToBytesND

_StrND: TypeAlias = npt.NDArray[np.str_]
_StringND: TypeAlias = np.ndarray[_Shape, np.dtypes.StringDType]
_CanStringND: TypeAlias = _CanArray[np.dtypes.StringDType]

###

# re-exported in `numpy.char`
class chararray(np.ndarray[_ShapeT_co, _DTypeT_co]):
    __module__: L["numpy.char"] = "numpy.char"

    @overload  # unicode=False (default)
    def __new__(
        cls,
        shape: _ToShape,
        itemsize: ConvertibleToInt = 1,
        unicode: L[False] = False,
        buffer: _SupportsBuffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _OrderKACF = "C",
    ) -> chararray[_Shape, np.dtype[np.bytes_]]: ...
    @overload  # unicode=True (positional)
    def __new__(
        cls,
        shape: _ToShape,
        itemsize: ConvertibleToInt,
        unicode: L[True],
        buffer: _SupportsBuffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _OrderKACF = "C",
    ) -> chararray[_Shape, np.dtype[np.str_]]: ...
    @overload  # unicode=True (keyword)
    def __new__(
        cls,
        shape: _ToShape,
        itemsize: ConvertibleToInt = 1,
        *,
        unicode: L[True],
        buffer: _SupportsBuffer | None = None,
        offset: SupportsIndex = 0,
        strides: _ToShape | None = None,
        order: _OrderKACF = "C",
    ) -> chararray[_Shape, np.dtype[np.str_]]: ...

    #
    @override
    def __eq__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ne__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ge__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __gt__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __lt__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __le__(self, other: _ToCharND, /) -> npt.NDArray[np.bool]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __add__(self: _CharArray[np.str_], rhs: _ToStrND, /) -> _CharArray[np.str_]: ...
    @overload
    def __add__(self: _CharArray[np.bytes_], rhs: _ToBytesND, /) -> _CharArray[np.bytes_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    #
    @overload  # type: ignore[override]
    def __radd__(self: _CharArray[np.str_], lhs: _ToStrND, /) -> _CharArray[np.str_]: ...
    @overload
    def __radd__(self: _CharArray[np.bytes_], lhs: _ToBytesND, /) -> _CharArray[np.bytes_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __mul__(self, rhs: _ToIntND, /) -> chararray[_Shape, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rmul__(self, lhs: _ToIntND, /) -> chararray[_Shape, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __mod__(self, rhs: object, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def decode(
        self: _CharArray[np.bytes_],
        /,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> chararray[_ShapeT_co, np.dtype[np.str_]]: ...
    def encode(
        self: _CharArray[np.str_],
        /,
        encoding: str | None = None,
        errors: str | None = None,
    ) -> chararray[_ShapeT_co, np.dtype[np.bytes_]]: ...

    #
    @overload
    def center(self: _CharArray[np.str_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.str_]: ...
    @overload
    def center(self: _CharArray[np.bytes_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.bytes_]: ...

    #
    @overload
    def count(
        self: _CharArray[np.str_],
        /,
        sub: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def count(
        self: _CharArray[np.bytes_],
        /,
        sub: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...

    #
    @overload
    def endswith(
        self: _CharArray[np.str_],
        /,
        suffix: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def endswith(
        self: _CharArray[np.bytes_],
        /,
        suffix: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.bool]: ...

    #
    @overload
    def expandtabs(self, /, tabsize: _ToInt = 8) -> chararray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def expandtabs(self, /, tabsize: _ToIntND) -> chararray[_Shape, _DTypeT_co]: ...

    #
    @overload
    def find(
        self: _CharArray[np.str_],
        /,
        sub: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def find(
        self: _CharArray[np.bytes_],
        /,
        sub: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...

    #
    @overload
    def index(
        self: _CharArray[np.str_],
        /,
        sub: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def index(
        self: _CharArray[np.bytes_],
        /,
        sub: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...

    #
    @overload
    def join(self: _CharArray[np.str_], /, seq: _ToStrND) -> _CharArray[np.str_]: ...
    @overload
    def join(self: _CharArray[np.bytes_], /, seq: _ToBytesND) -> _CharArray[np.bytes_]: ...

    #
    @overload
    def ljust(self: _CharArray[np.str_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.str_]: ...
    @overload
    def ljust(self: _CharArray[np.bytes_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.bytes_]: ...

    #
    @overload
    def lstrip(self: _CharArray[np.str_], /, chars: _ToStrND | None = None) -> _CharArray[np.str_]: ...
    @overload
    def lstrip(self: _CharArray[np.bytes_], /, chars: _ToBytesND | None = None) -> _CharArray[np.bytes_]: ...

    #
    @overload  # type: ignore[override]
    def partition(self: _CharArray[np.str_], /, sep: _ToStrND) -> _CharArray[np.str_]: ...
    @overload
    def partition(self: _CharArray[np.bytes_], /, sep: _ToBytesND) -> _CharArray[np.bytes_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def replace(
        self: _CharArray[np.str_],
        /,
        old: _ToStrND,
        new: _ToStrND,
        count: _ToIntND | None = None,
    ) -> _CharArray[np.str_]: ...
    @overload
    def replace(
        self: _CharArray[np.bytes_],
        /,
        old: _ToBytesND,
        new: _ToBytesND,
        count: _ToIntND | None = None,
    ) -> _CharArray[np.bytes_]: ...

    #
    @overload
    def rfind(
        self: _CharArray[np.str_],
        /,
        sub: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def rfind(
        self: _CharArray[np.bytes_],
        /,
        sub: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...

    #
    @overload
    def rindex(
        self: _CharArray[np.str_],
        /,
        sub: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def rindex(
        self: _CharArray[np.bytes_],
        /,
        sub: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.int_]: ...

    #
    @overload
    def rjust(self: _CharArray[np.str_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.str_]: ...
    @overload
    def rjust(self: _CharArray[np.bytes_], /, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _CharArray[np.bytes_]: ...

    #
    @overload
    def rpartition(self: _CharArray[np.str_], /, sep: _ToStrND) -> _CharArray[np.str_]: ...
    @overload
    def rpartition(self: _CharArray[np.bytes_], /, sep: _ToBytesND) -> _CharArray[np.bytes_]: ...

    #
    @overload
    def rsplit(
        self: _CharArray[np.str_],
        /,
        sep: _ToStrND | None = None,
        maxsplit: _ToIntND | None = None,
    ) -> npt.NDArray[np.object_]: ...
    @overload
    def rsplit(
        self: _CharArray[np.bytes_],
        /,
        sep: _ToBytesND | None = None,
        maxsplit: _ToIntND | None = None,
    ) -> npt.NDArray[np.object_]: ...

    #
    @overload
    def rstrip(self: _CharArray[np.str_], /, chars: _ToStrND | None = None) -> _CharArray[np.str_]: ...
    @overload
    def rstrip(self: _CharArray[np.bytes_], /, chars: _ToBytesND | None = None) -> _CharArray[np.bytes_]: ...

    #
    @overload
    def split(
        self: _CharArray[np.str_],
        /,
        sep: _ToStrND | None = None,
        maxsplit: _ToIntND | None = None,
    ) -> npt.NDArray[np.object_]: ...
    @overload
    def split(
        self: _CharArray[np.bytes_],
        /,
        sep: _ToBytesND | None = None,
        maxsplit: _ToIntND | None = None,
    ) -> npt.NDArray[np.object_]: ...

    #
    def splitlines(self, /, keepends: _ToBoolND | None = ...) -> npt.NDArray[np.object_]: ...

    #
    @overload
    def startswith(
        self: _CharArray[np.str_],
        /,
        prefix: _ToStrND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def startswith(
        self: _CharArray[np.bytes_],
        /,
        prefix: _ToBytesND,
        start: _ToIntND = 0,
        end: _ToIntND | None = None,
    ) -> npt.NDArray[np.bool]: ...

    #
    @overload
    def strip(self: _CharArray[np.str_], /, chars: _ToStrND | None = None) -> _CharArray[np.str_]: ...
    @overload
    def strip(self: _CharArray[np.bytes_], /, chars: _ToBytesND | None = None) -> _CharArray[np.bytes_]: ...

    #
    @overload
    def translate(
        self: _CharArray[np.str_],
        /,
        table: _ToStrND,
        deletechars: _ToStrND | None = None,
    ) -> _CharArray[np.str_]: ...
    @overload
    def translate(
        self: _CharArray[np.bytes_],
        /,
        table: _ToBytesND,
        deletechars: _ToBytesND | None = None,
    ) -> _CharArray[np.bytes_]: ...

    #
    def zfill(self, /, width: _ToIntND) -> chararray[_Shape, _DTypeT_co]: ...
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

# Comparison
@overload
def equal(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def equal(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def equal(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def not_equal(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def not_equal(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def not_equal(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def greater_equal(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def greater_equal(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def greater_equal(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def less_equal(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def less_equal(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def less_equal(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def greater(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def greater(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def greater(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def less(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.bool]: ...
@overload
def less(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bool]: ...
@overload
def less(x1: _ToStringND, x2: _ToStringND) -> npt.NDArray[np.bool]: ...

#
@overload
def add(x1: _ToStrND, x2: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def add(x1: _ToBytesND, x2: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def add(x1: _CanStringND, x2: _CanStringND) -> _StringND: ...
@overload
def add(x1: _ToStringND, x2: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def multiply(a: _ToStrND, i: _ToIntND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def multiply(a: _ToBytesND, i: _ToIntND) -> npt.NDArray[np.bytes_]: ...
@overload
def multiply(a: _CanStringND, i: _ToIntND) -> _StringND: ...
@overload
def multiply(a: _ToStringND, i: _ToIntND) -> _StrND | _StringND: ...

#
@overload
def mod(a: _ToStrND, value: Any) -> npt.NDArray[np.str_]: ...
@overload
def mod(a: _ToBytesND, value: Any) -> npt.NDArray[np.bytes_]: ...
@overload
def mod(a: _CanStringND, value: Any) -> _StringND: ...
@overload
def mod(a: _ToStringND, value: Any) -> _StrND | _StringND: ...

#
@overload
def capitalize(a: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def capitalize(a: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def capitalize(a: _CanStringND) -> _StringND: ...
@overload
def capitalize(a: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def center(a: _ToStrND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def center(a: _ToBytesND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.bytes_]: ...
@overload
def center(a: _CanStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StringND: ...
@overload
def center(a: _ToStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrND | _StringND: ...

#
def decode(a: _ToBytesND, encoding: str | None = None, errors: str | None = None) -> npt.NDArray[np.str_]: ...
def encode(a: _ToStrND | _ToStringND, encoding: str | None = None, errors: str | None = None) -> npt.NDArray[np.bytes_]: ...

#
@overload
def expandtabs(a: _ToStrND, tabsize: _ToIntND = 8) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def expandtabs(a: _ToBytesND, tabsize: _ToIntND = 8) -> npt.NDArray[np.bytes_]: ...
@overload
def expandtabs(a: _CanStringND, tabsize: _ToIntND = 8) -> _StringND: ...
@overload
def expandtabs(a: _ToStringND, tabsize: _ToIntND = 8) -> _StrND | _StringND: ...

#
@overload
def join(sep: _ToStrND, seq: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def join(sep: _ToBytesND, seq: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def join(sep: _CanStringND, seq: _CanStringND) -> _StringND: ...
@overload
def join(sep: _ToStringND, seq: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def ljust(a: _ToStrND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def ljust(a: _ToBytesND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.bytes_]: ...
@overload
def ljust(a: _CanStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StringND: ...
@overload
def ljust(a: _ToStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrND | _StringND: ...

#
@overload
def lower(a: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def lower(a: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def lower(a: _CanStringND) -> _StringND: ...
@overload
def lower(a: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def lstrip(a: _ToStrND, chars: _ToStrND | None = None) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def lstrip(a: _ToBytesND, chars: _ToBytesND | None = None) -> npt.NDArray[np.bytes_]: ...
@overload
def lstrip(a: _CanStringND, chars: _CanStringND | None = None) -> _StringND: ...
@overload
def lstrip(a: _ToStringND, chars: _ToStringND | None = None) -> _StrND | _StringND: ...

#
@overload
def partition(a: _ToStrND, sep: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def partition(a: _ToBytesND, sep: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def partition(a: _CanStringND, sep: _CanStringND) -> _StringND: ...
@overload
def partition(a: _ToStringND, sep: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def replace(a: _ToStrND, old: _ToStrND, new: _ToStrND, count: _ToIntND | None = None) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def replace(a: _ToBytesND, old: _ToBytesND, new: _ToBytesND, count: _ToIntND | None = None) -> npt.NDArray[np.bytes_]: ...
@overload
def replace(a: _CanStringND, old: _CanStringND, new: _CanStringND, count: _ToIntND = ...) -> _StringND: ...
@overload
def replace(a: _ToStringND, old: _ToStringND, new: _ToStringND, count: _ToIntND = ...) -> _StrND | _StringND: ...

#
@overload
def rjust(a: _ToStrND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def rjust(a: _ToBytesND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> npt.NDArray[np.bytes_]: ...
@overload
def rjust(a: _CanStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StringND: ...
@overload
def rjust(a: _ToStringND, width: _ToIntND, fillchar: _ToAnyCharND = " ") -> _StrND | _StringND: ...

#
@overload
def rpartition(a: _ToStrND, sep: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def rpartition(a: _ToBytesND, sep: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def rpartition(a: _CanStringND, sep: _CanStringND) -> _StringND: ...
@overload
def rpartition(a: _ToStringND, sep: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def rsplit(a: _ToStrND, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def rsplit(a: _ToBytesND, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def rsplit(a: _CanStringND, sep: _CanStringND | None = ..., maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def rsplit(a: _ToStringND, sep: _ToStringND | None = ..., maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...

#
@overload
def rstrip(a: _ToStrND, chars: _ToStrND | None = None) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def rstrip(a: _ToBytesND, chars: _ToBytesND | None = None) -> npt.NDArray[np.bytes_]: ...
@overload
def rstrip(a: _CanStringND, chars: _CanStringND | None = None) -> _StringND: ...
@overload
def rstrip(a: _ToStringND, chars: _ToStringND | None = None) -> _StrND | _StringND: ...

#
@overload
def split(a: _ToStrND, sep: _ToStrND | None = None, maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def split(a: _ToBytesND, sep: _ToBytesND | None = None, maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def split(a: _CanStringND, sep: _CanStringND | None = ..., maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...
@overload
def split(a: _ToStringND, sep: _ToStringND | None = ..., maxsplit: _ToIntND | None = None) -> npt.NDArray[np.object_]: ...

#
def splitlines(a: _ToAnyCharND, keepends: _ToBoolND | None = ...) -> npt.NDArray[np.object_]: ...

#
@overload
def strip(a: _ToStrND, chars: _ToStrND | None = None) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def strip(a: _ToBytesND, chars: _ToBytesND | None = None) -> npt.NDArray[np.bytes_]: ...
@overload
def strip(a: _CanStringND, chars: _CanStringND | None = None) -> _StringND: ...
@overload
def strip(a: _ToStringND, chars: _ToStringND | None = None) -> _StrND | _StringND: ...

#
@overload
def swapcase(a: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def swapcase(a: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def swapcase(a: _CanStringND) -> _StringND: ...
@overload
def swapcase(a: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def title(a: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def title(a: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def title(a: _CanStringND) -> _StringND: ...
@overload
def title(a: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def translate(a: _ToStrND, table: str, deletechars: str | None = ...) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def translate(a: _ToBytesND, table: str, deletechars: str | None = ...) -> npt.NDArray[np.bytes_]: ...
@overload
def translate(a: _CanStringND, table: str, deletechars: str | None = ...) -> _StringND: ...
@overload
def translate(a: _ToStringND, table: str, deletechars: str | None = ...) -> _StrND | _StringND: ...

#
@overload
def upper(a: _ToStrND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def upper(a: _ToBytesND) -> npt.NDArray[np.bytes_]: ...
@overload
def upper(a: _CanStringND) -> _StringND: ...
@overload
def upper(a: _ToStringND) -> _StrND | _StringND: ...

#
@overload
def zfill(a: _ToStrND, width: _ToIntND) -> npt.NDArray[np.str_]: ...  # type: ignore[overload-overlap]
@overload
def zfill(a: _ToBytesND, width: _ToIntND) -> npt.NDArray[np.bytes_]: ...
@overload
def zfill(a: _CanStringND, width: _ToIntND) -> _StringND: ...
@overload
def zfill(a: _ToStringND, width: _ToIntND) -> _StrND | _StringND: ...

# String information
@overload
def count(a: _ToStrND, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def count(a: _ToBytesND, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def count(a: _ToStringND, sub: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...

#
@overload
def endswith(a: _ToStrND, suffix: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...
@overload
def endswith(a: _ToBytesND, suffix: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...
@overload
def endswith(a: _ToStringND, suffix: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...

#
@overload
def find(a: _ToStrND, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def find(a: _ToBytesND, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def find(a: _ToStringND, sub: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...

#
@overload
def index(a: _ToStrND, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def index(a: _ToBytesND, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def index(a: _ToStringND, sub: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...

#
def isalpha(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def isalnum(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def isdecimal(a: _ToStrND | _ToStringND) -> npt.NDArray[np.bool]: ...
def isdigit(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def islower(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def isnumeric(a: _ToStrND | _ToStringND) -> npt.NDArray[np.bool]: ...
def isspace(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def istitle(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...
def isupper(a: _ToAnyCharND) -> npt.NDArray[np.bool]: ...

#
@overload
def rfind(a: _ToStrND, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def rfind(a: _ToBytesND, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def rfind(a: _ToStringND, sub: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...

#
@overload
def rindex(a: _ToStrND, sub: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def rindex(a: _ToBytesND, sub: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...
@overload
def rindex(a: _ToStringND, sub: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.int_]: ...

#
@overload
def startswith(a: _ToStrND, prefix: _ToStrND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...
@overload
def startswith(a: _ToBytesND, prefix: _ToBytesND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...
@overload
def startswith(a: _ToStringND, suffix: _ToStringND, start: _ToIntND = 0, end: _ToIntND | None = None) -> npt.NDArray[np.bool]: ...
@overload  # str array-like
def array(  # type: ignore[overload-overlap]
    obj: _ToStrND,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.str_]: ...
@overload  # bytes array-like
def array(  # type: ignore[overload-overlap]
    obj: _ToBytesND,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_]: ...
@overload  # unicode=False
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    *,
    unicode: L[False],
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_]: ...
@overload  # unicode=True
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    *,
    unicode: L[True],
    order: _OrderKACF | None = None,
) -> _CharArray[np.str_]: ...
@overload  # fallback
def array(
    obj: object,
    itemsize: int | None = None,
    copy: bool = True,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_ | np.str_]: ...

#
@overload  # str array-like
def asarray(  # type: ignore[overload-overlap]
    obj: _ToStrND,
    itemsize: int | None = None,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.str_]: ...
@overload  # bytes array-like
def asarray(  # type: ignore[overload-overlap]
    obj: _ToBytesND,
    itemsize: int | None = None,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_]: ...
@overload  # unicode=False
def asarray(
    obj: object,
    itemsize: int | None = None,
    *,
    unicode: L[False],
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_]: ...
@overload  # unicode=True
def asarray(
    obj: object,
    itemsize: int | None = None,
    *,
    unicode: L[True],
    order: _OrderKACF | None = None,
) -> _CharArray[np.str_]: ...
@overload  # falback
def asarray(
    obj: object,
    itemsize: int | None = None,
    unicode: bool | None = None,
    order: _OrderKACF | None = None,
) -> _CharArray[np.bytes_ | np.str_]: ...
