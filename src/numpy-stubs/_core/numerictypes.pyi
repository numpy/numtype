from builtins import bool as py_bool  # noqa: I001
from typing import Final, Literal as L, TypedDict, type_check_only

import numpy as np
from numpy import (  # noqa: ICN003
    dtype,

    generic, number, integer, inexact, flexible,
    signedinteger, unsignedinteger, floating, complexfloating, character,
    bool, bool_,
    int8, int16, int32, int64, byte, short, intc, intp, int_, long, longlong,
    uint8, uint16, uint32, uint64, ubyte, ushort, uintc, uintp, uint, ulong, ulonglong,
    float16, float32, float64, float96, float128, half, single, double, longdouble,
    complex64, complex128, complex192, complex256, csingle, cdouble, clongdouble,
    object_,
    bytes_, str_, void,
    datetime64, timedelta64,
)  # fmt: skip
from numpy._typing import DTypeLike

from ._type_aliases import sctypeDict as sctypeDict
from .multiarray import busday_count, busday_offset, busdaycalendar, datetime_as_string, datetime_data, is_busday

__all__ = [  # noqa: RUF022
    "ScalarType", "typecodes",
    "isdtype", "issubdtype",
    "datetime_data", "datetime_as_string",
    "busday_offset", "busday_count", "is_busday", "busdaycalendar",
    "generic", "number", "integer", "inexact", "flexible",
    "signedinteger", "unsignedinteger", "floating", "complexfloating", "character",
    "bool", "bool_",
    "int8", "int16", "int32", "int64", "byte", "short", "intc", "intp", "int_", "long", "longlong",
    "uint8", "uint16", "uint32", "uint64", "ubyte", "ushort", "uintc", "uintp", "uint", "ulong", "ulonglong",
    "float16", "float32", "float64", "float96", "float128", "half", "single", "double", "longdouble",
    "complex64", "complex128", "complex192", "complex256", "csingle", "cdouble", "clongdouble",
    "object_",
    "bytes_", "str_", "void",
    "datetime64", "timedelta64",
]  # fmt: skip

###

@type_check_only
class _TypeCodes(TypedDict):
    Character: L["c"]
    Integer: L["bhilqnp"]
    UnsignedInteger: L["BHILQNP"]
    Float: L["efdg"]
    Complex: L["FDG"]
    AllInteger: L["bBhHiIlLqQnNpP"]
    AllFloat: L["efdgFDG"]
    Datetime: L["Mm"]
    All: L["?bhilqnpBHILQNPefdgFDGSUVOMm"]

###

typecodes: Final[_TypeCodes] = ...
ScalarType: Final[
    tuple[
        type[int],
        type[float],
        type[complex],
        type[py_bool],
        type[bytes],
        type[str],
        type[memoryview],
        type[np.bool],
        type[csingle],
        type[cdouble],
        type[clongdouble],
        type[half],
        type[single],
        type[double],
        type[longdouble],
        type[byte],
        type[short],
        type[intc],
        type[long],
        type[longlong],
        type[timedelta64],
        type[datetime64],
        type[object_],
        type[bytes_],
        type[str_],
        type[ubyte],
        type[ushort],
        type[uintc],
        type[ulong],
        type[ulonglong],
        type[void],
    ]
] = ...
typeDict: Final = sctypeDict

def isdtype(dtype: dtype | type, kind: DTypeLike | tuple[DTypeLike, ...]) -> py_bool: ...
def issubdtype(arg1: DTypeLike, arg2: DTypeLike) -> py_bool: ...
