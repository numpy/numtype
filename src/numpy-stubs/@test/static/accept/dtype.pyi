import ctypes as ct
from typing import LiteralString, assert_type

import numpy as np

dtype_U: np.dtype[np.str_]
dtype_V: np.dtype[np.void]
dtype_i8: np.dtypes.Int64DType

py_int_co: type[int]
py_float_co: type[float]
py_complex_co: type[complex]
py_object: type
py_character: type[str | bytes]
py_flexible: type[str | bytes | memoryview]

ct_floating: type[ct.c_float | ct.c_double | ct.c_longdouble]
ct_number: type[ct.c_uint8 | ct.c_float]
ct_generic: type[ct.c_bool | ct.c_char]

dt_string: np.dtypes.StringDType

assert_type(np.dtype(np.float64), np.dtypes.Float64DType)
assert_type(np.dtype(np.float64, metadata={"test": "test"}), np.dtypes.Float64DType)
assert_type(np.dtype(np.int64), np.dtypes.Int64DType)

# String aliases
assert_type(np.dtype("bool"), np.dtypes.BoolDType)
assert_type(np.dtype("int32"), np.dtypes.Int32DType)
assert_type(np.dtype("int64"), np.dtypes.Int64DType)
assert_type(np.dtype("float32"), np.dtypes.Float32DType)
assert_type(np.dtype("float64"), np.dtypes.Float64DType)
assert_type(np.dtype("bytes"), np.dtypes.BytesDType)
assert_type(np.dtype("str"), np.dtypes.StrDType)

# Python types
assert_type(np.dtype(bool), np.dtypes.BoolDType)
assert_type(np.dtype(int), np.dtypes.Int64DType)
assert_type(np.dtype(float), np.dtypes.Float64DType)
assert_type(np.dtype(complex), np.dtypes.Complex128DType)
assert_type(np.dtype(object), np.dtypes.ObjectDType)
assert_type(np.dtype(str), np.dtypes.StrDType)
assert_type(np.dtype(bytes), np.dtypes.BytesDType)
assert_type(np.dtype(memoryview), np.dtypes.VoidDType)

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
assert_type(np.dtype("u1"), np.dtypes.UInt8DType)
assert_type(np.dtype("int_"), np.dtypes.Int64DType)
assert_type(np.dtype("longlong"), np.dtypes.Int64DType)
assert_type(np.dtype(">g"), np.dtypes.LongDoubleDType)

# ctypes
assert_type(np.dtype(ct.c_bool), np.dtypes.BoolDType)
assert_type(np.dtype(ct.c_uint32), np.dtypes.UInt32DType)
assert_type(np.dtype(ct.c_ssize_t), np.dtypes.Int64DType)
assert_type(np.dtype(ct.c_longlong), np.dtypes.Int64DType)
assert_type(np.dtype(ct.c_double), np.dtypes.Float64DType)
assert_type(np.dtype(ct.py_object), np.dtypes.ObjectDType)
assert_type(np.dtype(ct.c_char), np.dtypes.BytesDType)

# Special case for None
assert_type(np.dtype(None), np.dtypes.Float64DType)

# Dypes of dtypes
assert_type(np.dtype(np.dtype(np.float64)), np.dtypes.Float64DType)

# Parameterized dtypes
assert_type(np.dtype("S8"), np.dtype)

# Void
assert_type(np.dtype(("U", 10)), np.dtypes.VoidDType)

# StringDType
assert_type(np.dtype(dt_string), np.dtypes.StringDType)
assert_type(np.dtype("T"), np.dtypes.StringDType)
assert_type(np.dtype("=T"), np.dtypes.StringDType)
assert_type(np.dtype("|T"), np.dtypes.StringDType)

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
assert_type(dtype_i8 * 1, np.dtypes.Int64DType)
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
