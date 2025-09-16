import sys
from builtins import bool as py_bool
from typing import Any, Final, Literal as L, TypeAlias, TypedDict, type_check_only

# ruff: noqa: ICN003
from numpy import (
    bool,
    bool_,
    byte,
    bytes_,
    cdouble,
    character,
    clongdouble,
    complex64,
    complex128,
    complex192,
    complex256,
    complexfloating,
    csingle,
    datetime64,
    double,
    dtype,
    flexible,
    float16,
    float32,
    float64,
    float96,
    float128,
    floating,
    generic,
    half,
    inexact,
    int8,
    int16,
    int32,
    int64,
    int_,
    intc,
    integer,
    intp,
    long,
    longdouble,
    longlong,
    number,
    object_,
    short,
    signedinteger,
    single,
    str_,
    timedelta64,
    ubyte,
    uint,
    uint8,
    uint16,
    uint32,
    uint64,
    uintc,
    uintp,
    ulong,
    ulonglong,
    unsignedinteger,
    ushort,
    void,
)
from numpy._typing import DTypeLike

from ._type_aliases import sctypeDict as sctypeDict
from .multiarray import busday_count, busday_offset, busdaycalendar, datetime_as_string, datetime_data, is_busday

__all__ = [
    "ScalarType",
    "bool",
    "bool_",
    "busday_count",
    "busday_offset",
    "busdaycalendar",
    "byte",
    "bytes_",
    "cdouble",
    "character",
    "clongdouble",
    "complex64",
    "complex128",
    "complex192",
    "complex256",
    "complexfloating",
    "csingle",
    "datetime64",
    "datetime_as_string",
    "datetime_data",
    "double",
    "flexible",
    "float16",
    "float32",
    "float64",
    "float96",
    "float128",
    "floating",
    "generic",
    "half",
    "inexact",
    "int8",
    "int16",
    "int32",
    "int64",
    "int_",
    "intc",
    "integer",
    "intp",
    "is_busday",
    "isdtype",
    "issubdtype",
    "long",
    "longdouble",
    "longlong",
    "number",
    "object_",
    "short",
    "signedinteger",
    "single",
    "str_",
    "timedelta64",
    "typecodes",
    "ubyte",
    "uint",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "uintc",
    "uintp",
    "ulong",
    "ulonglong",
    "unsignedinteger",
    "ushort",
    "void",
]

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

# pyright: reportRedeclaration=false
# NOTE: The orders of float64/longdouble, int32/int64, and timedelta64/datetime64 are platform dependent.
# NOTE: We assume 64-bit platforms here.
if sys.platform == "darwin":
    _ScalarTypeTuple: TypeAlias = tuple[
        type[int],
        type[float],
        type[complex],
        type[py_bool],
        type[bytes],
        type[str],
        type[memoryview[Any]],
        type[Any],  # TODO: bool_?
        type[complex64],
        type[complex128],
        type[clongdouble],
        type[float16],
        type[float32],
        type[longdouble],
        type[float64],
        type[int8],
        type[int16],
        type[int32],
        type[int64],
        type[Any],  # TODO: longlong?
        type[datetime64[Any]],
        type[timedelta64[Any]],
        type[object_],
        type[bytes_],
        type[str_],
        type[uint8],
        type[uint16],
        type[uint32],
        type[uint64],
        type[Any],  # TODO: ulonglong?
        type[void],
    ]
elif sys.platform == "win32":
    _ScalarTypeTuple: TypeAlias = tuple[
        type[int],
        type[float],
        type[complex],
        type[py_bool],
        type[bytes],
        type[str],
        type[memoryview[Any]],
        type[Any],  # TODO: bool_?
        type[complex64],
        type[complex128],
        type[clongdouble],
        type[float16],
        type[float32],
        type[float64],
        type[longdouble],
        type[int8],
        type[int16],
        type[int32],
        type[Any],  # TODO: intc?
        type[int64],
        type[datetime64[Any]],
        type[timedelta64[Any]],
        type[object_],
        type[bytes_],
        type[str_],
        type[uint8],
        type[uint16],
        type[Any],  # TODO: uintc?
        type[uint32],
        type[uint64],
        type[void],
    ]
else:  # linux (presumed)
    _ScalarTypeTuple: TypeAlias = tuple[
        type[int],
        type[float],
        type[complex],
        type[py_bool],
        type[bytes],
        type[str],
        type[memoryview[Any]],
        type[bool_[Any]],
        type[complex64],
        type[complex128],
        type[clongdouble],
        type[float16],
        type[float32],
        type[float64],
        type[longdouble],
        type[int8],
        type[int16],
        type[int32],
        type[int64],
        type[longlong],
        type[timedelta64[Any]],
        type[datetime64[Any]],
        type[object_],
        type[bytes_],
        type[str_],
        type[uint8],
        type[uint16],
        type[uint32],
        type[uint64],
        type[ulonglong],
        type[void],
    ]

ScalarType: Final[_ScalarTypeTuple] = ...
typeDict: Final = sctypeDict

def isdtype(dtype: dtype | type, kind: DTypeLike | tuple[DTypeLike, ...]) -> py_bool: ...
def issubdtype(arg1: DTypeLike, arg2: DTypeLike) -> py_bool: ...
