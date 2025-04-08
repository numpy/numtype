from typing import Any, Protocol, TypeAlias, type_check_only
from typing_extensions import TypeVar

import numpy as np

from ._scalar import inexact32, integer8, integer16, integer32, number16, number32, number64

__all__ = [
    "CanPromote",
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
    "co_long",
    "co_number",
    "co_timedelta",
    "co_uint8",
    "co_uint16",
    "co_uint32",
    "co_uint64",
    "co_ulong",
]

_T_co = TypeVar("_T_co", covariant=True)
_ToT_contra = TypeVar("_ToT_contra", bound=np.generic, contravariant=True)
_FromT_contra = TypeVar("_FromT_contra", bound=np.generic, contravariant=True, default=Any)
_SelfT_co = TypeVar("_SelfT_co", bound=np.generic, covariant=True, default=Any)

@type_check_only
class _HasType(Protocol[_T_co]):
    @property
    def type(self, /) -> type[_T_co]: ...

@type_check_only
class _CanPromote(Protocol[_ToT_contra, _FromT_contra, _SelfT_co]):
    def __promote__(self, to: _ToT_contra, from_: _FromT_contra, /) -> _SelfT_co: ...

@type_check_only
class CanPromote(Protocol[_ToT_contra, _FromT_contra, _SelfT_co]):
    @property
    def shape(self, /) -> tuple[()]: ...
    @property
    def dtype(self, /) -> _HasType[_CanPromote[_ToT_contra, _FromT_contra, _SelfT_co]]: ...

###
# Coercible (overlapping) scalar- and array-likes
# See https://github.com/numpy/numtype/issues/366 for the scalar promotion table and
# https://numpy.org/neps/nep-0050-scalar-promotion.html for the official specification.

co_integer8: TypeAlias = integer8 | np.bool
co_integer16: TypeAlias = integer16 | co_integer8
co_integer32: TypeAlias = integer32 | co_integer16
co_integer64: TypeAlias = np.integer | np.bool
co_integer = co_integer64

co_int8: TypeAlias = np.int8 | np.bool
co_int16: TypeAlias = np.int16 | co_integer8
co_int32: TypeAlias = np.int32 | co_integer16
co_long: TypeAlias = np.long | co_int32
co_int64: TypeAlias = np.signedinteger | co_integer32

co_uint8: TypeAlias = np.uint8 | np.bool
co_uint16: TypeAlias = np.uint16 | co_uint8
co_uint32: TypeAlias = np.uint32 | co_uint16
co_ulong: TypeAlias = np.ulong | co_uint32
co_uint64: TypeAlias = np.unsignedinteger | np.bool

co_float16: TypeAlias = np.float16 | co_integer8
co_float32: TypeAlias = np.float32 | np.float16 | co_integer16
co_float64: TypeAlias = np.float64 | np.float32 | np.float16 | co_integer64
co_float: TypeAlias = np.floating | co_integer

co_complex64: TypeAlias = inexact32 | number16 | integer8
co_complex128: TypeAlias = number64 | number32 | number16 | co_integer
co_complex: TypeAlias = np.number | np.bool
co_number = co_complex

co_timedelta: TypeAlias = np.timedelta64 | co_integer
co_datetime: TypeAlias = np.datetime64 | np.timedelta64  # not transitive
