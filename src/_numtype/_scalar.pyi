from typing import TypeAlias

import numpy as np
from numpy._typing import _nbit_base as bits

__all__ = [
    "cfloating32",
    "cfloating64",
    "cfloating64l",
    "floating16",
    "floating32",
    "floating64",
    "floating64l",
    "inexact16",
    "inexact32",
    "inexact64",
    "inexact64l",
    "integer8",
    "integer16",
    "integer32",
    "integer64",
    "integer_p",
    "number8",
    "number16",
    "number32",
    "number64",
    "number64l",
]

###
# Sized abstract scalar type aliases.
# NOTE: These should only be used to annotate _input_, never _output_.

signed8: TypeAlias = np.signedinteger[bits._8]  # `int8` and `byte`
signed16: TypeAlias = np.signedinteger[bits._16]  # `int16` and `short`
signed32: TypeAlias = np.signedinteger[bits._32]  # `int32`, `intc`, maybe `long`, and sometimes `intp`
signed64: TypeAlias = np.signedinteger[bits._64]  # `int64` and `longlong`, maybe `long`, and usually `intp`

integer8: TypeAlias = np.integer[bits._8]  # `[u]int8` and `[u]byte`
integer16: TypeAlias = np.integer[bits._16]  # `[u]int16` and `[u]short`
integer32: TypeAlias = np.integer[bits._32]  # `[u]int32`, `[u]intc`, maybe `[u]long`, and sometimes `[u]intp`
integer64: TypeAlias = np.integer[bits._64]  # `[u]int64` and `[u]longlong`, maybe `u[long]`, and usually `[u]intp`
integer_p: TypeAlias = np.integer[bits._32_64]  # `[u]long`, and always `[u]intp``

floating16: TypeAlias = np.floating[bits._16]  # `float16` and `half`
floating32: TypeAlias = np.floating[bits._32]  # `float32` and `single`
floating64: TypeAlias = np.floating[bits._64]  # `float64` and `double`
floating64l: TypeAlias = np.floating[bits._LD]  # `longdouble`, `float96`, and `float128`

cfloating32: TypeAlias = np.complexfloating[bits._32]  # `complex64` and `csingle`
cfloating64: TypeAlias = np.complexfloating[bits._64]  # `complex128` and `cdouble`
cfloating64l: TypeAlias = np.complexfloating[bits._LD]  # `clongdouble`, `complex192`, and `complex256`

inexact16: TypeAlias = np.inexact[bits._16]  # `floating16`
inexact32: TypeAlias = np.inexact[bits._32]  # `floating32` and `Cfloating32`
inexact64: TypeAlias = np.inexact[bits._64]  # `floating64` and `Cfloating64`
inexact64l: TypeAlias = np.inexact[bits._LD]  # `floatingLD` and `CfloatingLD`

number8: TypeAlias = np.number[bits._8]  # `integer8`
number16: TypeAlias = np.number[bits._16]  # `integer16` and `float16`
number32: TypeAlias = np.number[bits._32]  # `integer32` and `inexact32`
number64: TypeAlias = np.number[bits._64]  # `integer64` and `inexact64`
number64l: TypeAlias = np.number[bits._LD]  # `inexact64l`
