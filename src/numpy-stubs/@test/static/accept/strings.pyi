from typing import TypeAlias, assert_type

import _numtype as _nt
import numpy as np

_BoolArray: TypeAlias = _nt.Array[np.bool_]
_IntArray: TypeAlias = _nt.Array[np.int_]
_BytesArray: TypeAlias = _nt.Array[np.bytes_]
_StrArray: TypeAlias = _nt.Array[np.str_]

AR_S: _BytesArray
AR_U: _StrArray
AR_T: _nt.StringArray

assert_type(np.strings.equal(AR_U, AR_U), _BoolArray)
assert_type(np.strings.equal(AR_S, AR_S), _BoolArray)
assert_type(np.strings.equal(AR_T, AR_T), _BoolArray)
assert_type(np.strings.equal(AR_S, AR_U, dtype=np.bool_), _BoolArray)

assert_type(np.strings.not_equal(AR_U, AR_U), _BoolArray)
assert_type(np.strings.not_equal(AR_S, AR_S), _BoolArray)
assert_type(np.strings.not_equal(AR_T, AR_T), _BoolArray)
assert_type(np.strings.not_equal(AR_S, AR_U, dtype=np.bool_), _BoolArray)

assert_type(np.strings.greater_equal(AR_U, AR_U), _BoolArray)
assert_type(np.strings.greater_equal(AR_S, AR_S), _BoolArray)
assert_type(np.strings.greater_equal(AR_T, AR_T), _BoolArray)
assert_type(np.strings.greater_equal(AR_S, AR_U, dtype=np.bool_), _BoolArray)

assert_type(np.strings.less_equal(AR_U, AR_U), _BoolArray)
assert_type(np.strings.less_equal(AR_S, AR_S), _BoolArray)
assert_type(np.strings.less_equal(AR_T, AR_T), _BoolArray)
assert_type(np.strings.less_equal(AR_S, AR_U, dtype=np.bool_), _BoolArray)

assert_type(np.strings.greater(AR_U, AR_U), _BoolArray)
assert_type(np.strings.greater(AR_S, AR_S), _BoolArray)
assert_type(np.strings.greater(AR_T, AR_T), _BoolArray)
assert_type(np.strings.greater(AR_S, AR_U, dtype=np.bool_), _BoolArray)

assert_type(np.strings.less(AR_U, AR_U), _BoolArray)
assert_type(np.strings.less(AR_S, AR_S), _BoolArray)
assert_type(np.strings.less(AR_T, AR_T), _BoolArray)
assert_type(np.strings.less(AR_S, AR_U, dtype=np.bool_), _BoolArray)

# TODO(jorenham): https://github.com/numpy/numtype/issues/230
# ruff: noqa: ERA001
# assert_type(np.strings.add(AR_U, AR_U), _StrArray)
# assert_type(np.strings.add(AR_S, AR_S), _BytesArray)
# assert_type(np.strings.add(AR_T, AR_T), _nt.StringArray)

assert_type(np.strings.multiply(AR_U, 5), _StrArray)
assert_type(np.strings.multiply(AR_S, [5, 4, 3]), _BytesArray)
assert_type(np.strings.multiply(AR_T, 5), _nt.StringArray)

assert_type(np.strings.mod(AR_U, "test"), _StrArray)
assert_type(np.strings.mod(AR_S, "test"), _BytesArray)
assert_type(np.strings.mod(AR_T, "test"), _nt.StringArray)

assert_type(np.strings.capitalize(AR_U), _StrArray)
assert_type(np.strings.capitalize(AR_S), _BytesArray)
assert_type(np.strings.capitalize(AR_T), _nt.StringArray)

assert_type(np.strings.center(AR_U, 5), _StrArray)
assert_type(np.strings.center(AR_S, [2, 3, 4], b"a"), _BytesArray)
assert_type(np.strings.center(AR_T, 5), _nt.StringArray)

assert_type(np.strings.encode(AR_U), _BytesArray)
assert_type(np.strings.encode(AR_T), _BytesArray)
assert_type(np.strings.decode(AR_S), _StrArray)

assert_type(np.strings.expandtabs(AR_U), _StrArray)
assert_type(np.strings.expandtabs(AR_S, tabsize=4), _BytesArray)
assert_type(np.strings.expandtabs(AR_T), _nt.StringArray)

assert_type(np.strings.ljust(AR_U, 5), _StrArray)
assert_type(np.strings.ljust(AR_S, [4, 3, 1], fillchar=[b"a", b"b", b"c"]), _BytesArray)
assert_type(np.strings.ljust(AR_T, 5), _nt.StringArray)
assert_type(np.strings.ljust(AR_T, [4, 2, 1], fillchar=["a", "b", "c"]), _nt.StringArray)

assert_type(np.strings.rjust(AR_U, 5), _StrArray)
assert_type(np.strings.rjust(AR_S, [4, 3, 1], fillchar=[b"a", b"b", b"c"]), _BytesArray)
assert_type(np.strings.rjust(AR_T, 5), _nt.StringArray)
assert_type(np.strings.rjust(AR_T, [4, 2, 1], fillchar=["a", "b", "c"]), _nt.StringArray)

assert_type(np.strings.lstrip(AR_U), _StrArray)
assert_type(np.strings.lstrip(AR_S, b"_"), _BytesArray)
assert_type(np.strings.lstrip(AR_T), _nt.StringArray)
assert_type(np.strings.lstrip(AR_T, "_"), _nt.StringArray)

assert_type(np.strings.rstrip(AR_U), _StrArray)
assert_type(np.strings.rstrip(AR_S, b"_"), _BytesArray)
assert_type(np.strings.rstrip(AR_T), _nt.StringArray)
assert_type(np.strings.rstrip(AR_T, "_"), _nt.StringArray)

assert_type(np.strings.strip(AR_U), _StrArray)
assert_type(np.strings.strip(AR_S, b"_"), _BytesArray)
assert_type(np.strings.strip(AR_T), _nt.StringArray)
assert_type(np.strings.strip(AR_T, "_"), _nt.StringArray)

assert_type(np.strings.count(AR_U, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.count(AR_S, [b"a", b"b", b"c"], end=9), _IntArray)
assert_type(np.strings.count(AR_T, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.count(AR_T, ["a", "b", "c"], end=9), _IntArray)

assert_type(np.strings.partition(AR_U, "\n"), _StrArray)
assert_type(np.strings.partition(AR_S, [b"a", b"b", b"c"]), _BytesArray)
assert_type(np.strings.partition(AR_T, "\n"), _nt.StringArray)

assert_type(np.strings.rpartition(AR_U, "\n"), _StrArray)
assert_type(np.strings.rpartition(AR_S, [b"a", b"b", b"c"]), _BytesArray)
assert_type(np.strings.rpartition(AR_T, "\n"), _nt.StringArray)

assert_type(np.strings.replace(AR_U, "_", "-"), _StrArray)
assert_type(np.strings.replace(AR_S, [b"_", b""], [b"a", b"b"]), _BytesArray)
assert_type(np.strings.replace(AR_T, "_", "_"), _nt.StringArray)

assert_type(np.strings.lower(AR_U), _StrArray)
assert_type(np.strings.lower(AR_S), _BytesArray)
assert_type(np.strings.lower(AR_T), _nt.StringArray)

assert_type(np.strings.upper(AR_U), _StrArray)
assert_type(np.strings.upper(AR_S), _BytesArray)
assert_type(np.strings.upper(AR_T), _nt.StringArray)

assert_type(np.strings.swapcase(AR_U), _StrArray)
assert_type(np.strings.swapcase(AR_S), _BytesArray)
assert_type(np.strings.swapcase(AR_T), _nt.StringArray)

assert_type(np.strings.title(AR_U), _StrArray)
assert_type(np.strings.title(AR_S), _BytesArray)
assert_type(np.strings.title(AR_T), _nt.StringArray)

assert_type(np.strings.zfill(AR_U, 5), _StrArray)
assert_type(np.strings.zfill(AR_S, [2, 3, 4]), _BytesArray)
assert_type(np.strings.zfill(AR_T, 5), _nt.StringArray)

assert_type(np.strings.endswith(AR_U, "a", start=[1, 2, 3]), _BoolArray)
assert_type(np.strings.endswith(AR_S, [b"a", b"b", b"c"], end=9), _BoolArray)
assert_type(np.strings.endswith(AR_T, "a", start=[1, 2, 3]), _BoolArray)

assert_type(np.strings.startswith(AR_U, "a", start=[1, 2, 3]), _BoolArray)
assert_type(np.strings.startswith(AR_S, [b"a", b"b", b"c"], end=9), _BoolArray)
assert_type(np.strings.startswith(AR_T, "a", start=[1, 2, 3]), _BoolArray)

assert_type(np.strings.find(AR_U, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.find(AR_S, [b"a", b"b", b"c"], end=9), _IntArray)
assert_type(np.strings.find(AR_T, "a", start=[1, 2, 3]), _IntArray)

assert_type(np.strings.rfind(AR_U, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.rfind(AR_S, [b"a", b"b", b"c"], end=9), _IntArray)
assert_type(np.strings.rfind(AR_T, "a", start=[1, 2, 3]), _IntArray)

assert_type(np.strings.index(AR_U, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.index(AR_S, [b"a", b"b", b"c"], end=9), _IntArray)
assert_type(np.strings.index(AR_T, "a", start=[1, 2, 3]), _IntArray)

assert_type(np.strings.rindex(AR_U, "a", start=[1, 2, 3]), _IntArray)
assert_type(np.strings.rindex(AR_S, [b"a", b"b", b"c"], end=9), _IntArray)
assert_type(np.strings.rindex(AR_T, "a", start=[1, 2, 3]), _IntArray)

assert_type(np.strings.isalpha(AR_U), _BoolArray)
assert_type(np.strings.isalpha(AR_S), _BoolArray)
assert_type(np.strings.isalpha(AR_T), _BoolArray)

assert_type(np.strings.isalnum(AR_U), _BoolArray)
assert_type(np.strings.isalnum(AR_S), _BoolArray)
assert_type(np.strings.isalnum(AR_T), _BoolArray)

assert_type(np.strings.isdecimal(AR_U), _BoolArray)
assert_type(np.strings.isdecimal(AR_T), _BoolArray)

assert_type(np.strings.isdigit(AR_U), _BoolArray)
assert_type(np.strings.isdigit(AR_S), _BoolArray)
assert_type(np.strings.isdigit(AR_T), _BoolArray)

assert_type(np.strings.islower(AR_U), _BoolArray)
assert_type(np.strings.islower(AR_S), _BoolArray)
assert_type(np.strings.islower(AR_T), _BoolArray)

assert_type(np.strings.isnumeric(AR_U), _BoolArray)
assert_type(np.strings.isnumeric(AR_T), _BoolArray)

assert_type(np.strings.isspace(AR_U), _BoolArray)
assert_type(np.strings.isspace(AR_S), _BoolArray)
assert_type(np.strings.isspace(AR_T), _BoolArray)

assert_type(np.strings.istitle(AR_U), _BoolArray)
assert_type(np.strings.istitle(AR_S), _BoolArray)
assert_type(np.strings.istitle(AR_T), _BoolArray)

assert_type(np.strings.isupper(AR_U), _BoolArray)
assert_type(np.strings.isupper(AR_S), _BoolArray)
assert_type(np.strings.isupper(AR_T), _BoolArray)

assert_type(np.strings.str_len(AR_U), _IntArray)
assert_type(np.strings.str_len(AR_S), _IntArray)
assert_type(np.strings.str_len(AR_T), _IntArray)

assert_type(np.strings.translate(AR_U, ""), _StrArray)
assert_type(np.strings.translate(AR_S, ""), _BytesArray)
assert_type(np.strings.translate(AR_T, ""), _nt.StringArray)
