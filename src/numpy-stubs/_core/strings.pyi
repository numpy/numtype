from typing import TypeAlias, overload

import _numtype as _nt
import numpy as np
from numpy._typing import _ArrayLikeAnyString_co as ToAnyStringND, _ArrayLikeInt_co as ToIntND

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

_BoolND: TypeAlias = _nt.Array[np.bool_]
_IntND: TypeAlias = _nt.Array[np.int_]
_BytesND: TypeAlias = _nt.Array[np.bytes_]
_StrND: TypeAlias = _nt.Array[np.str_]

_CoStringND: TypeAlias = _nt.ToString_nd | _nt.ToStr_nd

###

#
@overload
def startswith(
    a: _nt.ToBytes_nd, prefix: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None
) -> _BoolND: ...
@overload
def startswith(a: _CoStringND, prefix: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolND: ...

#
@overload
def endswith(a: _nt.ToBytes_nd, suffix: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolND: ...
@overload
def endswith(a: _CoStringND, suffix: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _BoolND: ...

###

#
@overload
def find(a: _nt.ToBytes_nd, sub: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def find(a: _CoStringND, sub: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...

#
@overload
def rfind(a: _nt.ToBytes_nd, sub: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def rfind(a: _CoStringND, sub: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...

#
@overload
def index(a: _nt.ToBytes_nd, sub: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def index(a: _CoStringND, sub: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def rindex(a: _nt.ToBytes_nd, sub: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def rindex(a: _CoStringND, sub: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...

#
@overload
def count(a: _nt.ToBytes_nd, sub: _nt.ToBytes_nd, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...
@overload
def count(a: _CoStringND, sub: _CoStringND, start: ToIntND = 0, end: ToIntND | None = None) -> _IntND: ...

###

#
def decode(a: _nt.ToBytes_nd, encoding: str | None = None, errors: str | None = None) -> _StrND: ...
def encode(a: _CoStringND, encoding: str | None = None, errors: str | None = None) -> _BytesND: ...

###

#
@overload
def upper(a: _nt.ToStr_nd) -> _StrND: ...
@overload
def upper(a: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def upper(a: _nt.ToString_nd) -> _nt.StringArray: ...

#
@overload
def lower(a: _nt.ToStr_nd) -> _StrND: ...
@overload
def lower(a: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def lower(a: _nt.ToString_nd) -> _nt.StringArray: ...

#
@overload
def swapcase(a: _nt.ToStr_nd) -> _StrND: ...
@overload
def swapcase(a: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def swapcase(a: _nt.ToString_nd) -> _nt.StringArray: ...

#
@overload
def capitalize(a: _nt.ToStr_nd) -> _StrND: ...
@overload
def capitalize(a: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def capitalize(a: _nt.ToString_nd) -> _nt.StringArray: ...

#
@overload
def title(a: _nt.ToStr_nd) -> _StrND: ...
@overload
def title(a: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def title(a: _nt.ToString_nd) -> _nt.StringArray: ...

#
@overload
def multiply(a: _nt.ToStr_nd, i: ToIntND) -> _StrND: ...
@overload
def multiply(a: _nt.ToBytes_nd, i: ToIntND) -> _BytesND: ...
@overload
def multiply(a: _nt.ToString_nd, i: ToIntND) -> _nt.StringArray: ...

#
@overload
def expandtabs(a: _nt.ToStr_nd, tabsize: ToIntND = 8) -> _StrND: ...
@overload
def expandtabs(a: _nt.ToBytes_nd, tabsize: ToIntND = 8) -> _BytesND: ...
@overload
def expandtabs(a: _nt.ToString_nd, tabsize: ToIntND = 8) -> _nt.StringArray: ...

#
@overload
def center(a: _nt.ToStr_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrND: ...
@overload
def center(a: _nt.ToBytes_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesND: ...
@overload
def center(a: _nt.ToString_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _nt.StringArray: ...

#
@overload
def ljust(a: _nt.ToStr_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrND: ...
@overload
def ljust(a: _nt.ToBytes_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesND: ...
@overload
def ljust(a: _nt.ToString_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _nt.StringArray: ...

#
@overload
def rjust(a: _nt.ToStr_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _StrND: ...
@overload
def rjust(a: _nt.ToBytes_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _BytesND: ...
@overload
def rjust(a: _nt.ToString_nd, width: ToIntND, fillchar: ToAnyStringND = " ") -> _nt.StringArray: ...

#
@overload
def zfill(a: _nt.ToStr_nd, width: ToIntND) -> _StrND: ...
@overload
def zfill(a: _nt.ToBytes_nd, width: ToIntND) -> _BytesND: ...
@overload
def zfill(a: _nt.ToString_nd, width: ToIntND) -> _nt.StringArray: ...

#
@overload
def mod(a: _nt.ToStr_nd, values: object) -> _StrND: ...
@overload
def mod(a: _nt.ToBytes_nd, values: object) -> _BytesND: ...
@overload
def mod(a: _nt.ToString_nd, values: object) -> _nt.StringArray: ...

#
@overload
def translate(a: _nt.ToStr_nd, table: str, deletechars: str | None = None) -> _StrND: ...
@overload
def translate(a: _nt.ToBytes_nd, table: str, deletechars: str | None = None) -> _BytesND: ...
@overload
def translate(a: _nt.ToString_nd, table: str, deletechars: str | None = None) -> _nt.StringArray: ...

#
@overload
def lstrip(a: _nt.ToStr_nd, chars: _nt.ToStr_nd | None = None) -> _StrND: ...
@overload
def lstrip(a: _nt.ToBytes_nd, chars: _nt.ToBytes_nd | None = None) -> _BytesND: ...
@overload
def lstrip(a: _nt.ToString_nd, chars: _CoStringND | None = None) -> _nt.StringArray: ...
@overload
def lstrip(a: _CoStringND, chars: _CoStringND | None = None) -> _StrND | _nt.StringArray: ...

#
@overload
def rstrip(a: _nt.ToStr_nd, chars: _nt.ToStr_nd | None = None) -> _StrND: ...
@overload
def rstrip(a: _nt.ToBytes_nd, chars: _nt.ToBytes_nd | None = None) -> _BytesND: ...
@overload
def rstrip(a: _nt.ToString_nd, chars: _CoStringND | None = None) -> _nt.StringArray: ...
@overload
def rstrip(a: _CoStringND, chars: _CoStringND | None = None) -> _StrND | _nt.StringArray: ...

#
@overload
def strip(a: _nt.ToStr_nd, chars: _nt.ToStr_nd | None = None) -> _StrND: ...
@overload
def strip(a: _nt.ToBytes_nd, chars: _nt.ToBytes_nd | None = None) -> _BytesND: ...
@overload
def strip(a: _nt.ToString_nd, chars: _CoStringND | None = None) -> _nt.StringArray: ...
@overload
def strip(a: _CoStringND, chars: _CoStringND | None = None) -> _StrND | _nt.StringArray: ...

#
@overload
def replace(a: _nt.ToStr_nd, old: _nt.ToStr_nd, new: _nt.ToStr_nd, count: ToIntND = -1) -> _StrND: ...
@overload
def replace(a: _nt.ToBytes_nd, old: _nt.ToBytes_nd, new: _nt.ToBytes_nd, count: ToIntND = -1) -> _BytesND: ...
@overload
def replace(a: _nt.ToString_nd, old: _CoStringND, new: _CoStringND, count: ToIntND = -1) -> _nt.StringArray: ...
@overload
def replace(a: _CoStringND, old: _CoStringND, new: _CoStringND, count: ToIntND = -1) -> _StrND | _nt.StringArray: ...

#
@overload
def partition(a: _nt.ToStr_nd, sep: _nt.ToStr_nd) -> _StrND: ...
@overload
def partition(a: _nt.ToBytes_nd, sep: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def partition(a: _nt.ToString_nd, sep: _CoStringND) -> _nt.StringArray: ...
@overload
def partition(a: _CoStringND, sep: _CoStringND) -> _StrND | _nt.StringArray: ...

#
@overload
def rpartition(a: _nt.ToStr_nd, sep: _nt.ToStr_nd) -> _StrND: ...
@overload
def rpartition(a: _nt.ToBytes_nd, sep: _nt.ToBytes_nd) -> _BytesND: ...
@overload
def rpartition(a: _nt.ToString_nd, sep: _CoStringND) -> _nt.StringArray: ...
@overload
def rpartition(a: _CoStringND, sep: _CoStringND) -> _StrND | _nt.StringArray: ...
