from typing import TypeAlias, overload

import numpy as np
from numpy._typing import (
    NDArray,
    _ArrayLikeAnyString_co as ToAnyStringND,
    _ArrayLikeBytes_co as ToBytesND,
    _ArrayLikeInt_co as ToIntND,
    _ArrayLikeStr_co as ToStrND,
    _ArrayLikeString_co as ToStringND,
    _NestedSequence,
    _SupportsArray,
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
    str_len,
)

__all__ = [
    "add",
    "capitalize",
    "center",
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
    "rstrip",
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

_StringArrayLike: TypeAlias = (
    _SupportsArray[np.dtypes.StringDType] | _NestedSequence[_SupportsArray[np.dtypes.StringDType]]
)

_BoolArray: TypeAlias = NDArray[np.bool]
_IntArray: TypeAlias = NDArray[np.int_]
_BytesArray: TypeAlias = NDArray[np.bytes_]
_StrArray: TypeAlias = NDArray[np.str_]
_StringArray: TypeAlias = np.ndarray[tuple[int, ...], np.dtypes.StringDType]

###

#
@overload
def startswith(a: ToStrND, prefix: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def startswith(a: ToBytesND, prefix: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def startswith(a: ToStringND, prefix: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...

#
@overload
def endswith(a: ToStrND, suffix: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def endswith(a: ToBytesND, suffix: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...
@overload
def endswith(a: ToStringND, suffix: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolArray: ...

###

#
@overload
def find(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def find(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def find(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def rfind(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rfind(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rfind(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def index(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def index(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def index(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def rindex(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rindex(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def rindex(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

#
@overload
def count(a: ToStrND, sub: ToStrND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def count(a: ToBytesND, sub: ToBytesND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...
@overload
def count(a: ToStringND, sub: ToStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntArray: ...

###

#
def decode(a: ToBytesND, encoding: str | None = None, errors: str | None = None) -> _StrArray: ...
def encode(a: ToStrND | ToStringND, encoding: str | None = None, errors: str | None = None) -> _BytesArray: ...

###
# NOTE: The ignored `overload-overlap` mypy errors are false positives

#
@overload
def multiply(a: ToStrND, i: ToIntND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def multiply(a: ToBytesND, i: ToIntND) -> _BytesArray: ...
@overload
def multiply(a: _StringArrayLike, i: ToIntND) -> _StringArray: ...
@overload
def multiply(a: ToStringND, i: ToIntND) -> _StrArray | _StringArray: ...

#
@overload
def mod(a: ToStrND, values: object) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def mod(a: ToBytesND, values: object) -> _BytesArray: ...
@overload
def mod(a: _StringArrayLike, values: object) -> _StringArray: ...
@overload
def mod(a: ToStringND, values: object) -> _StrArray | _StringArray: ...

#
@overload
def expandtabs(a: ToStrND, tabsize: ToIntND = 8) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def expandtabs(a: ToBytesND, tabsize: ToIntND = 8) -> _BytesArray: ...
@overload
def expandtabs(a: _StringArrayLike, tabsize: ToIntND = 8) -> _StringArray: ...
@overload
def expandtabs(a: ToStringND, tabsize: ToIntND = 8) -> _StrArray | _StringArray: ...

#
@overload
def center(a: ToStrND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def center(a: ToBytesND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesArray: ...
@overload
def center(a: _StringArrayLike, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StringArray: ...
@overload
def center(a: ToStringND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray | _StringArray: ...

#
@overload
def ljust(a: ToStrND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def ljust(a: ToBytesND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesArray: ...
@overload
def ljust(a: _StringArrayLike, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StringArray: ...
@overload
def ljust(a: ToStringND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray | _StringArray: ...

#
@overload
def rjust(a: ToStrND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def rjust(a: ToBytesND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesArray: ...
@overload
def rjust(a: _StringArrayLike, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StringArray: ...
@overload
def rjust(a: ToStringND, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrArray | _StringArray: ...

#
@overload
def lstrip(a: ToStrND, chars: ToStrND | None = None) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def lstrip(a: ToBytesND, chars: ToBytesND | None = None) -> _BytesArray: ...
@overload
def lstrip(a: _StringArrayLike, chars: ToStringND | None = None) -> _StringArray: ...
@overload
def lstrip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def rstrip(a: ToStrND, chars: ToStrND | None = None) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def rstrip(a: ToBytesND, chars: ToBytesND | None = None) -> _BytesArray: ...
@overload
def rstrip(a: _StringArrayLike, chars: ToStringND | None = None) -> _StringArray: ...
@overload
def rstrip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def strip(a: ToStrND, chars: ToStrND | None = None) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def strip(a: ToBytesND, chars: ToBytesND | None = None) -> _BytesArray: ...
@overload
def strip(a: _StringArrayLike, chars: ToStringND | None = None) -> _StringArray: ...
@overload
def strip(a: ToStringND, chars: ToStringND | None = None) -> _StrArray | _StringArray: ...

#
@overload
def zfill(a: ToStrND, width: ToIntND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def zfill(a: ToBytesND, width: ToIntND) -> _BytesArray: ...
@overload
def zfill(a: _StringArrayLike, width: ToIntND) -> _StringArray: ...
@overload
def zfill(a: ToStringND, width: ToIntND) -> _StrArray | _StringArray: ...

#
@overload
def upper(a: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def upper(a: ToBytesND) -> _BytesArray: ...
@overload
def upper(a: _StringArrayLike) -> _StringArray: ...
@overload
def upper(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def lower(a: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def lower(a: ToBytesND) -> _BytesArray: ...
@overload
def lower(a: _StringArrayLike) -> _StringArray: ...
@overload
def lower(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def swapcase(a: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def swapcase(a: ToBytesND) -> _BytesArray: ...
@overload
def swapcase(a: _StringArrayLike) -> _StringArray: ...
@overload
def swapcase(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def capitalize(a: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def capitalize(a: ToBytesND) -> _BytesArray: ...
@overload
def capitalize(a: _StringArrayLike) -> _StringArray: ...
@overload
def capitalize(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def title(a: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def title(a: ToBytesND) -> _BytesArray: ...
@overload
def title(a: _StringArrayLike) -> _StringArray: ...
@overload
def title(a: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def replace(a: ToStrND, old: ToStrND, new: ToStrND, count: ToIntND = -1) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def replace(a: ToBytesND, old: ToBytesND, new: ToBytesND, count: ToIntND = -1) -> _BytesArray: ...
@overload
def replace(a: _StringArrayLike, old: ToStringND, new: ToStringND, count: ToIntND = -1) -> _StringArray: ...
@overload
def replace(a: ToStringND, old: ToStringND, new: ToStringND, count: ToIntND = -1) -> _StrArray | _StringArray: ...

#
@overload
def partition(a: ToStrND, sep: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def partition(a: ToBytesND, sep: ToBytesND) -> _BytesArray: ...
@overload
def partition(a: _StringArrayLike, sep: ToStringND) -> _StringArray: ...
@overload
def partition(a: ToStringND, sep: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def rpartition(a: ToStrND, sep: ToStrND) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def rpartition(a: ToBytesND, sep: ToBytesND) -> _BytesArray: ...
@overload
def rpartition(a: _StringArrayLike, sep: ToStringND) -> _StringArray: ...
@overload
def rpartition(a: ToStringND, sep: ToStringND) -> _StrArray | _StringArray: ...

#
@overload
def translate(a: ToStrND, table: str, deletechars: str | None = None) -> _StrArray: ...  # type: ignore[overload-overlap]
@overload
def translate(a: ToBytesND, table: str, deletechars: str | None = None) -> _BytesArray: ...
@overload
def translate(a: _StringArrayLike, table: str, deletechars: str | None = None) -> _StringArray: ...
@overload
def translate(a: ToStringND, table: str, deletechars: str | None = None) -> _StrArray | _StringArray: ...
