from typing import Any, TypeAlias

import numpy as np

from ._scalar import (
    floating16,
    floating32,
    floating64,
    inexact32,
    integer8,
    integer16,
    integer32,
    number8,
    number16,
    number32,
    number64,
)

__all__ = [
    "co_complex",
    "co_complex64",
    "co_complex128",
    "co_datetime",
    "co_float",
    "co_float16",
    "co_float32",
    "co_float64",
    "co_int8",
    "co_int16",
    "co_int32",
    "co_int64",
    "co_integer",
    "co_integer8",
    "co_integer16",
    "co_integer32",
    "co_integer64",
    "co_intp",
    "co_long",
    "co_number",
    "co_timedelta",
    "co_uint8",
    "co_uint16",
    "co_uint32",
    "co_uint64",
    "co_uintp",
    "co_ulong",
]

###
# Coercible (overlapping) scalar- and array-likes
# See https://github.com/numpy/numtype/issues/366 for the scalar promotion table and
# https://numpy.org/neps/nep-0050-scalar-promotion.html for the official specification.

co_bool: TypeAlias = np.bool_[Any]

co_integer8: TypeAlias = integer8 | co_bool
co_integer16: TypeAlias = integer16 | co_integer8
co_integer32: TypeAlias = integer32 | co_integer16
co_integer64: TypeAlias = np.integer | co_bool
co_integer = co_integer64

co_int8: TypeAlias = np.int8 | co_bool
co_int16: TypeAlias = np.int16 | co_integer8
co_int32: TypeAlias = np.int32 | co_integer16
co_long: TypeAlias = np.long | co_int32
co_intp: TypeAlias = np.intp | co_long
co_int64: TypeAlias = np.signedinteger | co_integer32

co_uint8: TypeAlias = np.uint8 | co_bool
co_uint16: TypeAlias = np.uint16 | co_uint8
co_uint32: TypeAlias = np.uint32 | co_uint16
co_ulong: TypeAlias = np.ulong | co_uint32
co_uintp: TypeAlias = np.uintp | co_ulong
co_uint64: TypeAlias = np.unsignedinteger | co_bool

co_float16: TypeAlias = floating16 | co_integer8
co_float32: TypeAlias = floating32 | floating16 | co_integer16
co_float64: TypeAlias = floating64 | floating32 | floating16 | co_integer64
co_float: TypeAlias = np.floating | co_integer

co_complex64: TypeAlias = inexact32 | number16 | number8
co_complex128: TypeAlias = number64 | number32 | number16 | co_integer
co_complex: TypeAlias = np.number | co_bool
co_number = co_complex

co_timedelta: TypeAlias = np.timedelta64 | co_integer
co_datetime: TypeAlias = np.datetime64 | np.timedelta64  # not transitive
