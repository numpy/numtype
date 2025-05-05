import _ctypes as _ct
import ctypes as ct
from typing import Any, assert_type

import _numtype as _nt
import numpy as np

###

AR_b1: _nt.Array[np.bool]
AR_i1: _nt.Array[np.int8]
AR_i2: _nt.Array[np.int16]
AR_i4: _nt.Array[np.int32]
AR_i8: _nt.Array[np.int64]
AR_q: _nt.Array[np.longlong]
AR_u1: _nt.Array[np.uint8]
AR_u2: _nt.Array[np.uint16]
AR_u4: _nt.Array[np.uint32]
AR_u8: _nt.Array[np.uint64]
AR_L: _nt.Array[np.ulong]
AR_f4: _nt.Array[np.float32]
AR_f8: _nt.Array[np.float64]
AR_g: _nt.Array[np.longdouble]

pointer: ct._Pointer[Any]

###

assert_type(np.ctypeslib.c_intp(), np.ctypeslib.c_intp)

assert_type(np.ctypeslib.ndpointer(), type[np.ctypeslib._ndptr[None]])
assert_type(np.ctypeslib.ndpointer(dtype=np.float64), type[np.ctypeslib._ndptr[np.dtype[np.float64]]])
assert_type(np.ctypeslib.ndpointer(dtype=float), type[np.ctypeslib._ndptr[np.dtype]])
assert_type(np.ctypeslib.ndpointer(shape=(10, 3)), type[np.ctypeslib._ndptr[None]])
assert_type(np.ctypeslib.ndpointer(np.int64, shape=(10, 3)), type[np.ctypeslib._concrete_ndptr[np.dtype[np.int64]]])
assert_type(np.ctypeslib.ndpointer(int, shape=(1,)), type[np.ctypeslib._concrete_ndptr[np.dtype]])

assert_type(np.ctypeslib.as_ctypes_type(np.bool), type[ct.c_bool])
assert_type(np.ctypeslib.as_ctypes_type(np.ubyte), type[ct.c_uint8])
assert_type(np.ctypeslib.as_ctypes_type(np.ushort), type[ct.c_uint16])
assert_type(np.ctypeslib.as_ctypes_type(np.uintc), type[ct.c_uint32])
assert_type(np.ctypeslib.as_ctypes_type(np.ulonglong), type[ct.c_uint64])
assert_type(np.ctypeslib.as_ctypes_type(np.byte), type[ct.c_int8])
assert_type(np.ctypeslib.as_ctypes_type(np.short), type[ct.c_int16])
assert_type(np.ctypeslib.as_ctypes_type(np.intc), type[ct.c_int32])
assert_type(np.ctypeslib.as_ctypes_type(np.longlong), type[ct.c_int64])
assert_type(np.ctypeslib.as_ctypes_type(np.single), type[ct.c_float])
assert_type(np.ctypeslib.as_ctypes_type(np.double), type[ct.c_double])
assert_type(np.ctypeslib.as_ctypes_type(ct.c_double), type[ct.c_double])
assert_type(np.ctypeslib.as_ctypes_type("q"), type[ct.c_int64])
assert_type(np.ctypeslib.as_ctypes_type([("i8", np.int64), ("f8", np.float64)]), _ct._UnionType | _ct._PyCStructType)
assert_type(np.ctypeslib.as_ctypes_type("i8"), type[ct.c_int64])
assert_type(np.ctypeslib.as_ctypes_type("f8"), type[ct.c_double])

assert_type(np.ctypeslib.as_ctypes(AR_b1.take(0)), ct.c_bool)
assert_type(np.ctypeslib.as_ctypes(AR_u1.take(0)), ct.c_uint8)
assert_type(np.ctypeslib.as_ctypes(AR_u2.take(0)), ct.c_uint16)
assert_type(np.ctypeslib.as_ctypes(AR_u4.take(0)), ct.c_uint32)

assert_type(np.ctypeslib.as_ctypes(AR_i1.take(0)), ct.c_int8)
assert_type(np.ctypeslib.as_ctypes(AR_i2.take(0)), ct.c_int16)
assert_type(np.ctypeslib.as_ctypes(AR_i4.take(0)), ct.c_int32)
assert_type(np.ctypeslib.as_ctypes(AR_i8.take(0)), ct.c_int64)
assert_type(np.ctypeslib.as_ctypes(AR_f4.take(0)), ct.c_float)
assert_type(np.ctypeslib.as_ctypes(AR_f8.take(0)), ct.c_double)
assert_type(np.ctypeslib.as_ctypes(AR_b1), ct.Array[ct.c_bool])
assert_type(np.ctypeslib.as_ctypes(AR_u1), ct.Array[ct.c_uint8])
assert_type(np.ctypeslib.as_ctypes(AR_u2), ct.Array[ct.c_uint16])
assert_type(np.ctypeslib.as_ctypes(AR_u4), ct.Array[ct.c_uint32])
assert_type(np.ctypeslib.as_ctypes(AR_i1), ct.Array[ct.c_int8])
assert_type(np.ctypeslib.as_ctypes(AR_i2), ct.Array[ct.c_int16])
assert_type(np.ctypeslib.as_ctypes(AR_i4), ct.Array[ct.c_int32])
assert_type(np.ctypeslib.as_ctypes(AR_i8), ct.Array[ct.c_int64])
assert_type(np.ctypeslib.as_ctypes(AR_f4), ct.Array[ct.c_float])
assert_type(np.ctypeslib.as_ctypes(AR_f8), ct.Array[ct.c_double])

assert_type(np.ctypeslib.as_array(AR_u1), _nt.Array[np.ubyte])
assert_type(np.ctypeslib.as_array(1), _nt.Array[Any])
assert_type(np.ctypeslib.as_array(pointer), _nt.Array[Any])
