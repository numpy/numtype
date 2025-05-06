from typing import Any, TypeAlias, assert_type
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape, default=_nt.Shape)

_BytesArray: TypeAlias = np.char.chararray[_ShapeT, np.dtype[np.bytes_]]
_StrArray: TypeAlias = np.char.chararray[_ShapeT, np.dtype[np.str_]]

###

AR_U: _StrArray
AR_S: _BytesArray

assert_type(AR_U == AR_U, _nt.Array[np.bool])
assert_type(AR_S == AR_S, _nt.Array[np.bool])

assert_type(AR_U != AR_U, _nt.Array[np.bool])
assert_type(AR_S != AR_S, _nt.Array[np.bool])

assert_type(AR_U >= AR_U, _nt.Array[np.bool])
assert_type(AR_S >= AR_S, _nt.Array[np.bool])

assert_type(AR_U <= AR_U, _nt.Array[np.bool])
assert_type(AR_S <= AR_S, _nt.Array[np.bool])

assert_type(AR_U > AR_U, _nt.Array[np.bool])
assert_type(AR_S > AR_S, _nt.Array[np.bool])

assert_type(AR_U < AR_U, _nt.Array[np.bool])
assert_type(AR_S < AR_S, _nt.Array[np.bool])

assert_type(AR_U * 5, _StrArray)
assert_type(AR_S * [5], _BytesArray)

assert_type(AR_U % "test", _StrArray)
assert_type(AR_S % b"test", _BytesArray)

assert_type(AR_U.capitalize(), _StrArray)
assert_type(AR_S.capitalize(), _BytesArray)

assert_type(AR_U.center(5), _StrArray)
assert_type(AR_S.center([2, 3, 4], b"a"), _BytesArray)

assert_type(AR_U.encode(), _BytesArray)
assert_type(AR_S.decode(), _StrArray)

assert_type(AR_U.expandtabs(), _StrArray)
assert_type(AR_S.expandtabs(tabsize=4), _BytesArray)

assert_type(AR_U.join("_"), _StrArray)
assert_type(AR_S.join([b"_", b""]), _BytesArray)

assert_type(AR_U.ljust(5), _StrArray)
assert_type(AR_S.ljust([4, 3, 1], fillchar=[b"a", b"b", b"c"]), _BytesArray)
assert_type(AR_U.rjust(5), _StrArray)
assert_type(AR_S.rjust([4, 3, 1], fillchar=[b"a", b"b", b"c"]), _BytesArray)

assert_type(AR_U.lstrip(), _StrArray)
assert_type(AR_S.lstrip(chars=b"_"), _BytesArray)
assert_type(AR_U.rstrip(), _StrArray)
assert_type(AR_S.rstrip(chars=b"_"), _BytesArray)
assert_type(AR_U.strip(), _StrArray)
assert_type(AR_S.strip(chars=b"_"), _BytesArray)

assert_type(AR_U.partition("\n"), _StrArray)
assert_type(AR_S.partition([b"a", b"b", b"c"]), _BytesArray)
assert_type(AR_U.rpartition("\n"), _StrArray)
assert_type(AR_S.rpartition([b"a", b"b", b"c"]), _BytesArray)

assert_type(AR_U.replace("_", "-"), _StrArray)
assert_type(AR_S.replace([b"_", b""], [b"a", b"b"]), _BytesArray)

assert_type(AR_U.split("_"), _nt.Array[np.object_])
assert_type(AR_S.split(maxsplit=[1, 2, 3]), _nt.Array[np.object_])
assert_type(AR_U.rsplit("_"), _nt.Array[np.object_])
assert_type(AR_S.rsplit(maxsplit=[1, 2, 3]), _nt.Array[np.object_])

assert_type(AR_U.splitlines(), _nt.Array[np.object_])
assert_type(AR_S.splitlines(keepends=[True, True, False]), _nt.Array[np.object_])

assert_type(AR_U.swapcase(), _StrArray)
assert_type(AR_S.swapcase(), _BytesArray)

assert_type(AR_U.title(), _StrArray)
assert_type(AR_S.title(), _BytesArray)

assert_type(AR_U.upper(), _StrArray)
assert_type(AR_S.upper(), _BytesArray)

assert_type(AR_U.zfill(5), _StrArray[Any])
assert_type(AR_S.zfill([2, 3, 4]), _BytesArray[Any])

assert_type(AR_U.count("a", start=[1, 2, 3]), _nt.Array[np.int_])
assert_type(AR_S.count([b"a", b"b", b"c"], end=9), _nt.Array[np.int_])

assert_type(AR_U.endswith("a", start=[1, 2, 3]), _nt.Array[np.bool])
assert_type(AR_S.endswith([b"a", b"b", b"c"], end=9), _nt.Array[np.bool])
assert_type(AR_U.startswith("a", start=[1, 2, 3]), _nt.Array[np.bool])
assert_type(AR_S.startswith([b"a", b"b", b"c"], end=9), _nt.Array[np.bool])

assert_type(AR_U.find("a", start=[1, 2, 3]), _nt.Array[np.int_])
assert_type(AR_S.find([b"a", b"b", b"c"], end=9), _nt.Array[np.int_])
assert_type(AR_U.rfind("a", start=[1, 2, 3]), _nt.Array[np.int_])
assert_type(AR_S.rfind([b"a", b"b", b"c"], end=9), _nt.Array[np.int_])

assert_type(AR_U.index("a", start=[1, 2, 3]), _nt.Array[np.int_])
assert_type(AR_S.index([b"a", b"b", b"c"], end=9), _nt.Array[np.int_])
assert_type(AR_U.rindex("a", start=[1, 2, 3]), _nt.Array[np.int_])
assert_type(AR_S.rindex([b"a", b"b", b"c"], end=9), _nt.Array[np.int_])

assert_type(AR_U.isalpha(), _nt.Array[np.bool])
assert_type(AR_S.isalpha(), _nt.Array[np.bool])

assert_type(AR_U.isalnum(), _nt.Array[np.bool])
assert_type(AR_S.isalnum(), _nt.Array[np.bool])

assert_type(AR_U.isdecimal(), _nt.Array[np.bool])
assert_type(AR_S.isdecimal(), _nt.Array[np.bool])

assert_type(AR_U.isdigit(), _nt.Array[np.bool])
assert_type(AR_S.isdigit(), _nt.Array[np.bool])

assert_type(AR_U.islower(), _nt.Array[np.bool])
assert_type(AR_S.islower(), _nt.Array[np.bool])

assert_type(AR_U.isnumeric(), _nt.Array[np.bool])
assert_type(AR_S.isnumeric(), _nt.Array[np.bool])

assert_type(AR_U.isspace(), _nt.Array[np.bool])
assert_type(AR_S.isspace(), _nt.Array[np.bool])

assert_type(AR_U.istitle(), _nt.Array[np.bool])
assert_type(AR_S.istitle(), _nt.Array[np.bool])

assert_type(AR_U.isupper(), _nt.Array[np.bool])
assert_type(AR_S.isupper(), _nt.Array[np.bool])

assert_type(AR_U.__array_finalize__(object()), None)
assert_type(AR_S.__array_finalize__(object()), None)
