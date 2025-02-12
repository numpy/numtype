from typing import TypeAlias
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

BytesArray: TypeAlias = npt.NDArray[np.bytes_]
StrArray: TypeAlias = npt.NDArray[np.str_]
StringArray: TypeAlias = np.ndarray[tuple[int, ...], np.dtypes.StringDType]

AR_S: BytesArray
AR_U: StrArray
AR_T: StringArray
AR_SUT: BytesArray | StrArray | StringArray

assert_type(np.char.equal(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.equal(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.equal(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.not_equal(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.not_equal(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.not_equal(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.greater_equal(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.greater_equal(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.greater_equal(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.less_equal(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.less_equal(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.less_equal(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.greater(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.greater(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.greater(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.less(AR_U, AR_U), npt.NDArray[np.bool])
assert_type(np.char.less(AR_S, AR_S), npt.NDArray[np.bool])
assert_type(np.char.less(AR_T, AR_T), npt.NDArray[np.bool])

assert_type(np.char.multiply(AR_U, 5), StrArray)
assert_type(np.char.multiply(AR_U, 5), StrArray)
assert_type(np.char.multiply(AR_S, [5, 4, 3]), BytesArray)
assert_type(np.char.multiply(AR_T, 5), StringArray)

assert_type(np.char.mod(AR_U, "test"), StrArray)
assert_type(np.char.mod(AR_S, "test"), BytesArray)
assert_type(np.char.mod(AR_T, "test"), StringArray)

assert_type(np.char.capitalize(AR_U), StrArray)
assert_type(np.char.capitalize(AR_S), BytesArray)
assert_type(np.char.capitalize(AR_T), StringArray)

assert_type(np.char.center(AR_U, 5), StrArray)
assert_type(np.char.center(AR_S, [2, 3, 4], b"a"), BytesArray)
assert_type(np.char.center(AR_T, 5), StringArray)

assert_type(np.char.encode(AR_U), BytesArray)
assert_type(np.char.encode(AR_T), BytesArray)
assert_type(np.char.decode(AR_S), StrArray)

assert_type(np.char.expandtabs(AR_U), StrArray)
assert_type(np.char.expandtabs(AR_S, tabsize=4), BytesArray)
assert_type(np.char.expandtabs(AR_T), StringArray)

assert_type(np.char.join(AR_U, "_"), StrArray)
assert_type(np.char.join(AR_S, [b"_", b""]), BytesArray)
assert_type(np.char.join(AR_T, "_"), StrArray | StringArray)

assert_type(np.char.ljust(AR_U, 5), StrArray)
assert_type(np.char.ljust(AR_S, [4, 3, 1], fillchar=[b"a", b"b", b"c"]), BytesArray)
assert_type(np.char.ljust(AR_T, 5), StringArray)
assert_type(np.char.ljust(AR_T, [4, 2, 1], fillchar=["a", "b", "c"]), StringArray)

assert_type(np.char.rjust(AR_U, 5), StrArray)
assert_type(np.char.rjust(AR_S, [4, 3, 1], fillchar=[b"a", b"b", b"c"]), BytesArray)
assert_type(np.char.rjust(AR_T, 5), StringArray)
assert_type(np.char.rjust(AR_T, [4, 2, 1], fillchar=["a", "b", "c"]), StringArray)

assert_type(np.char.lstrip(AR_U), StrArray)
assert_type(np.char.lstrip(AR_S, b"_"), BytesArray)
assert_type(np.char.lstrip(AR_T), StringArray)
assert_type(np.char.lstrip(AR_T, "_"), StrArray | StringArray)

assert_type(np.char.rstrip(AR_U), StrArray)
assert_type(np.char.rstrip(AR_S, b"_"), BytesArray)
assert_type(np.char.rstrip(AR_T), StringArray)
assert_type(np.char.rstrip(AR_T, "_"), StrArray | StringArray)

assert_type(np.char.strip(AR_U), StrArray)
assert_type(np.char.strip(AR_S, b"_"), BytesArray)
assert_type(np.char.strip(AR_T), StringArray)
assert_type(np.char.strip(AR_T, "_"), StrArray | StringArray)

assert_type(np.char.count(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.count(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.int_])
assert_type(np.char.count(AR_T, AR_T, start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.count(AR_T, ["a", "b", "c"], end=9), npt.NDArray[np.int_])

assert_type(np.char.partition(AR_U, "\n"), StrArray)
assert_type(np.char.partition(AR_S, [b"a", b"b", b"c"]), BytesArray)
assert_type(np.char.partition(AR_T, "\n"), StrArray | StringArray)

assert_type(np.char.rpartition(AR_U, "\n"), StrArray)
assert_type(np.char.rpartition(AR_S, [b"a", b"b", b"c"]), BytesArray)
assert_type(np.char.rpartition(AR_T, "\n"), StrArray | StringArray)

assert_type(np.char.replace(AR_U, "_", "-"), StrArray)
assert_type(np.char.replace(AR_S, [b"_", b""], [b"a", b"b"]), BytesArray)
assert_type(np.char.replace(AR_T, "_", "_"), StrArray | StringArray)

assert_type(np.char.split(AR_U, "_"), npt.NDArray[np.object_])
assert_type(np.char.split(AR_S, maxsplit=[1, 2, 3]), npt.NDArray[np.object_])
assert_type(np.char.split(AR_T, "_"), npt.NDArray[np.object_])

assert_type(np.char.rsplit(AR_U, "_"), npt.NDArray[np.object_])
assert_type(np.char.rsplit(AR_S, maxsplit=[1, 2, 3]), npt.NDArray[np.object_])
assert_type(np.char.rsplit(AR_T, "_"), npt.NDArray[np.object_])

assert_type(np.char.splitlines(AR_U), npt.NDArray[np.object_])
assert_type(np.char.splitlines(AR_S, keepends=[True, True, False]), npt.NDArray[np.object_])
assert_type(np.char.splitlines(AR_T), npt.NDArray[np.object_])

assert_type(np.char.lower(AR_U), StrArray)
assert_type(np.char.lower(AR_S), BytesArray)
assert_type(np.char.lower(AR_T), StringArray)

assert_type(np.char.upper(AR_U), StrArray)
assert_type(np.char.upper(AR_S), BytesArray)
assert_type(np.char.upper(AR_T), StringArray)

assert_type(np.char.swapcase(AR_U), StrArray)
assert_type(np.char.swapcase(AR_S), BytesArray)
assert_type(np.char.swapcase(AR_T), StringArray)

assert_type(np.char.title(AR_U), StrArray)
assert_type(np.char.title(AR_S), BytesArray)
assert_type(np.char.title(AR_T), StringArray)

assert_type(np.char.translate(AR_U, ""), StrArray)
assert_type(np.char.translate(AR_S, ""), BytesArray)
assert_type(np.char.translate(AR_T, ""), StringArray)

assert_type(np.char.zfill(AR_U, 5), StrArray)
assert_type(np.char.zfill(AR_S, [2, 3, 4]), BytesArray)
assert_type(np.char.zfill(AR_T, 5), StringArray)

assert_type(np.char.endswith(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.bool])
assert_type(np.char.endswith(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.bool])
assert_type(np.char.endswith(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.bool])

assert_type(np.char.startswith(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.bool])
assert_type(np.char.startswith(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.bool])
assert_type(np.char.startswith(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.bool])

assert_type(np.char.find(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.find(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.int_])
assert_type(np.char.find(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.int_])

assert_type(np.char.rfind(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.rfind(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.int_])
assert_type(np.char.rfind(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.int_])

assert_type(np.char.index(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.index(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.int_])
assert_type(np.char.index(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.int_])

assert_type(np.char.rindex(AR_U, "a", start=[1, 2, 3]), npt.NDArray[np.int_])
assert_type(np.char.rindex(AR_S, [b"a", b"b", b"c"], end=9), npt.NDArray[np.int_])
assert_type(np.char.rindex(AR_T, "a", start=[1, 2, 3]), npt.NDArray[np.int_])

assert_type(np.char.isdecimal(AR_U), npt.NDArray[np.bool])
assert_type(np.char.isdecimal(AR_T), npt.NDArray[np.bool])

assert_type(np.char.isnumeric(AR_U), npt.NDArray[np.bool])
assert_type(np.char.isnumeric(AR_T), npt.NDArray[np.bool])

assert_type(np.char.isalpha(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.isalnum(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.isdigit(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.islower(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.isspace(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.istitle(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.isupper(AR_SUT), npt.NDArray[np.bool])
assert_type(np.char.str_len(AR_SUT), npt.NDArray[np.int_])

assert_type(np.char.array(AR_U), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
assert_type(np.char.array(AR_S, order="K"), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.array("bob", copy=True), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
assert_type(np.char.array(b"bob", itemsize=5), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.array(1, unicode=False), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.array(1, unicode=True), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])

assert_type(np.char.asarray(AR_U), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
assert_type(np.char.asarray(AR_S, order="K"), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.asarray("bob"), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
assert_type(np.char.asarray(b"bob", itemsize=5), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.asarray(1, unicode=False), np.char.chararray[tuple[int, ...], np.dtype[np.bytes_]])
assert_type(np.char.asarray(1, unicode=True), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
