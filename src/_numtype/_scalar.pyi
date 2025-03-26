from typing import TypeAlias

import numpy as np
from numpy._typing import _nbit_base as bits

__all__ = [
    "inexact16",
    "inexact32",
    "inexact64",
    "inexact64l",
    "integer8",
    "integer16",
    "integer32",
    "integer64",
    "integer_l",
    "number8",
    "number16",
    "number32",
    "number64",
    "number64l",
]

###
# Sized abstract scalar type aliases.
# NOTE: These should only be used to annotate _input_, never _output_.

integer8: TypeAlias = np.integer[bits._8]  # `[u]int8` and `[u]byte`
integer16: TypeAlias = np.integer[bits._16]  # `[u]int16` and `[u]short`
integer32: TypeAlias = np.integer[bits._32]  # `[u]int32`, `[u]intc`, maybe `[u]long`, and sometimes `[u]intp`
integer64: TypeAlias = np.integer[bits._64]  # `[u]int64` and `[u]longlong`, maybe `u[long]`, and usually `[u]intp`
integer_l: TypeAlias = np.integer[bits._32_64]  # `[u]long`, and always `[u]intp``

inexact16: TypeAlias = np.inexact[bits._16]  # `floating16`
inexact32: TypeAlias = np.inexact[bits._32]  # `floating32` and `Cfloating32`
inexact64: TypeAlias = np.inexact[bits._64]  # `floating64` and `Cfloating64`
inexact64l: TypeAlias = np.inexact[bits._64L]  # `floatingLD` and `CfloatingLD`

number8: TypeAlias = np.number[bits._8]  # `integer8`
number16: TypeAlias = np.number[bits._16]  # `integer16` and `float16`
number32: TypeAlias = np.number[bits._32]  # `integer32` and `inexact32`
number64: TypeAlias = np.number[bits._64]  # `integer64` and `inexact64`
number64l: TypeAlias = np.number[bits._64L]  # `inexact64l`
