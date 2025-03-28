from typing import TypeAlias

import numpy as np

__all__ = [
    "inexact32",
    "inexact64",
    "inexact64l",
    "integer8",
    "integer16",
    "integer32",
    "integer64",
    "integer_l",
    "number16",
    "number32",
    "number64",
]

###
# Sized abstract scalar type aliases.

integer8: TypeAlias = np.uint8 | np.int8
integer16: TypeAlias = np.uint16 | np.int16
integer32: TypeAlias = np.uint32 | np.int32
integer_l: TypeAlias = np.ulong | np.long
integer64: TypeAlias = np.uint64 | np.int64

inexact32: TypeAlias = np.complex64 | np.float32
inexact64: TypeAlias = np.complex128 | np.float64
inexact64l: TypeAlias = np.clongdouble | np.longdouble

number16: TypeAlias = np.float16 | integer16
number32: TypeAlias = inexact32 | integer32
number64: TypeAlias = inexact64 | integer64
