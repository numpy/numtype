import ctypes as ct
from typing_extensions import LiteralString, assert_type

import numpy as np
from numpy.dtypes import StringDType

dtype_U: np.dtype[np.str_]
dtype_V: np.dtype[np.void]
dtype_i8: np.dtype[np.int64]

py_int_co: type[int]
py_float_co: type[float]
py_complex_co: type[complex]
py_object: type
py_character: type[str | bytes]
py_flexible: type[str | bytes | memoryview]

ct_floating: type[ct.c_float | ct.c_double | ct.c_longdouble]
ct_number: type[ct.c_uint8 | ct.c_float]
ct_generic: type[ct.c_bool | ct.c_char]

dt_string: StringDType

assert_type(np.dtype(np.float64), np.dtype[np.float64])
assert_type(np.dtype(np.float64, metadata={"test": "test"}), np.dtype[np.float64])
assert_type(np.dtype(np.int64), np.dtype[np.int64])

# String aliases
assert_type(np.dtype("bool"), np.dtype[np.bool])
assert_type(np.dtype("int32"), np.dtype[np.int32])
assert_type(np.dtype("int64"), np.dtype[np.int64])
assert_type(np.dtype("float32"), np.dtype[np.float32])
assert_type(np.dtype("float64"), np.dtype[np.float64])
assert_type(np.dtype("bytes"), np.dtype[np.bytes_])
assert_type(np.dtype("str"), np.dtype[np.str_])

# Python types
assert_type(np.dtype(bool), np.dtype[np.bool])
assert_type(np.dtype(int), np.dtype[np.int_])
assert_type(np.dtype(float), np.dtype[np.float64])
assert_type(np.dtype(complex), np.dtype[np.complex128])
assert_type(np.dtype(object), np.dtype[np.object_])
assert_type(np.dtype(str), np.dtype[np.str_])
assert_type(np.dtype(bytes), np.dtype[np.bytes_])
assert_type(np.dtype(memoryview), np.dtype[np.void])

assert_type(np.dtype(np.signedinteger), np.dtype[np.signedinteger])
assert_type(np.dtype(np.unsignedinteger), np.dtype[np.unsignedinteger])
assert_type(np.dtype(np.integer), np.dtype[np.integer])
assert_type(np.dtype(np.floating), np.dtype[np.floating])
assert_type(np.dtype(np.complexfloating), np.dtype[np.complexfloating])
assert_type(np.dtype(np.inexact), np.dtype[np.inexact])
assert_type(np.dtype(np.number), np.dtype[np.number])
# NOTE: `character` and `flexible` always fail on mypy because of some mypy bug
assert_type(np.dtype(np.generic), np.dtype[np.generic])

# char-codes
assert_type(np.dtype("u1"), np.dtype[np.uint8])
assert_type(np.dtype("int_"), np.dtype[np.intp])
assert_type(np.dtype("longlong"), np.dtype[np.longlong])
assert_type(np.dtype(">g"), np.dtype[np.longdouble])

# ctypes
assert_type(np.dtype(ct.c_bool), np.dtype[np.bool])
assert_type(np.dtype(ct.c_uint32), np.dtype[np.uint32])
assert_type(np.dtype(ct.c_ssize_t), np.dtype[np.intp])
assert_type(np.dtype(ct.c_longlong), np.dtype[np.longlong])
assert_type(np.dtype(ct.c_double), np.dtype[np.double])
assert_type(np.dtype(ct.py_object), np.dtype[np.object_])
assert_type(np.dtype(ct.c_char), np.dtype[np.bytes_])

# Special case for None
assert_type(np.dtype(None), np.dtype[np.float64])

# Dypes of dtypes
assert_type(np.dtype(np.dtype(np.float64)), np.dtype[np.float64])
assert_type(np.dtype(np.dtype(np.inexact)), np.dtype[np.inexact])

# Parameterized dtypes
assert_type(np.dtype("S8"), np.dtype)

# Void
assert_type(np.dtype(("U", 10)), np.dtype[np.void])

# StringDType
assert_type(np.dtype(dt_string), StringDType)
assert_type(np.dtype("T"), StringDType)
assert_type(np.dtype("=T"), StringDType)
assert_type(np.dtype("|T"), StringDType)

# Methods and attributes
assert_type(dtype_U.base, np.dtype)
assert_type(dtype_U.subdtype, tuple[np.dtype, tuple[int, ...]] | None)
assert_type(dtype_U.newbyteorder(), np.dtype[np.str_])
assert_type(dtype_U.type, type[np.str_])
assert_type(dtype_U.name, LiteralString)
assert_type(dtype_U.names, tuple[str, ...] | None)

assert_type(dtype_U * 0, np.dtype[np.str_])
assert_type(dtype_U * 1, np.dtype[np.str_])
assert_type(dtype_U * 2, np.dtype[np.str_])

assert_type(dtype_i8 * 0, np.dtype[np.void])
assert_type(dtype_i8 * 1, np.dtype[np.int64])
assert_type(dtype_i8 * 2, np.dtype[np.void])

assert_type(0 * dtype_U, np.dtype[np.str_])
assert_type(1 * dtype_U, np.dtype[np.str_])
assert_type(2 * dtype_U, np.dtype[np.str_])

assert_type(0 * dtype_i8, np.dtype)
assert_type(1 * dtype_i8, np.dtype)
assert_type(2 * dtype_i8, np.dtype)

assert_type(dtype_V["f0"], np.dtype)
assert_type(dtype_V[0], np.dtype)
assert_type(dtype_V[["f0", "f1"]], np.dtype[np.void])
assert_type(dtype_V[["f0"]], np.dtype[np.void])
