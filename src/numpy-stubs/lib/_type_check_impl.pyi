from collections.abc import Container, Iterable
from typing import Any, Literal as L, overload, type_check_only
from typing_extensions import Protocol, TypeVar

import _numtype as _nt
import numpy as np

__all__ = [
    "common_type",
    "imag",
    "iscomplex",
    "iscomplexobj",
    "isreal",
    "isrealobj",
    "mintypecode",
    "nan_to_num",
    "real",
    "real_if_close",
    "typename",
]

###

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_RealT = TypeVar("_RealT", bound=_nt.co_number)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)

@type_check_only
class _HasReal(Protocol[_T_co]):
    @property
    def real(self, /) -> _T_co: ...

@type_check_only
class _HasImag(Protocol[_T_co]):
    @property
    def imag(self, /) -> _T_co: ...

@type_check_only
class _HasDType(Protocol[_ScalarT_co]):
    @property
    def dtype(self, /) -> np.dtype[_ScalarT_co]: ...

###

#
def mintypecode(
    typechars: Iterable[_nt.ToGeneric_nd], typeset: str | Container[str] = "GDFgdf", default: str = "d"
) -> str: ...

#
@overload
def real(val: _HasReal[_T]) -> _T: ...  # type: ignore[overload-overlap]
@overload
def real(val: _nt.ToBool_nd) -> _nt.Array[np.bool]: ...
@overload
def real(val: _nt.ToInt_nd) -> _nt.Array[np.intp]: ...
@overload
def real(val: _nt.ToFloat64_nd) -> _nt.Array[np.float64]: ...
@overload
def real(val: _nt.ToComplex128_nd) -> _nt.Array[np.complex128]: ...
@overload
def real(val: _nt.ToBytes_nd) -> _nt.Array[np.bytes_]: ...
@overload
def real(val: _nt.ToStr_nd) -> _nt.Array[np.str_]: ...
@overload
def real(val: _nt._ToArray_nd[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def real(val: _nt.ToGeneric_nd) -> _nt.Array: ...

#
@overload
def imag(val: _HasImag[_T]) -> _T: ...  # type: ignore[overload-overlap]
@overload
def imag(val: _nt.ToBool_nd) -> _nt.Array[np.bool]: ...
@overload
def imag(val: _nt.ToInt_nd) -> _nt.Array[np.intp]: ...
@overload
def imag(val: _nt.ToFloat64_nd) -> _nt.Array[np.float64]: ...
@overload
def imag(val: _nt.ToComplex128_nd) -> _nt.Array[np.complex128]: ...
@overload
def imag(val: _nt.ToBytes_nd) -> _nt.Array[np.bytes_]: ...
@overload
def imag(val: _nt.ToStr_nd) -> _nt.Array[np.str_]: ...
@overload
def imag(val: _nt._ToArray_nd[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def imag(val: _nt.ToGeneric_nd) -> _nt.Array: ...

#
@overload
def iscomplex(x: _nt.ToGeneric_1nd) -> _nt.Array[np.bool]: ...
@overload
def iscomplex(x: np.generic | _nt._PyScalar) -> np.bool: ...

#
@overload
def isreal(x: _nt.ToGeneric_1nd) -> _nt.Array[np.bool]: ...
@overload
def isreal(x: np.generic | _nt._PyScalar) -> np.bool: ...

#
def iscomplexobj(x: _HasDType[Any] | _nt.ToGeneric_nd) -> bool: ...
def isrealobj(x: _HasDType[Any] | _nt.ToGeneric_nd) -> bool: ...

#
@overload
def nan_to_num(
    x: _ScalarT, copy: bool = True, nan: float = 0.0, posinf: float | None = None, neginf: float | None = None
) -> _ScalarT: ...
@overload
def nan_to_num(
    x: _nt._ToArray_1nd[_ScalarT],
    copy: bool = True,
    nan: float = 0.0,
    posinf: float | None = None,
    neginf: float | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload
def nan_to_num(
    x: _nt.ToGeneric_0d, copy: bool = True, nan: float = 0.0, posinf: float | None = None, neginf: float | None = None
) -> Any: ...
@overload
def nan_to_num(
    x: _nt.ToGeneric_1nd, copy: bool = True, nan: float = 0.0, posinf: float | None = None, neginf: float | None = None
) -> _nt.Array: ...

# If one passes a complex array to `real_if_close`, then one is reasonably
# expected to verify the output dtype (so we can return an unsafe union here)

@overload
def real_if_close(a: _nt.ToComplex128_nd, tol: float = 100) -> _nt.Array[_nt.inexact64]: ...
@overload
def real_if_close(a: _nt.ToComplex64_nd, tol: float = 100) -> _nt.Array[_nt.inexact32]: ...
@overload
def real_if_close(a: _nt.ToCLongDouble_nd, tol: float = 100) -> _nt.Array[_nt.inexact64l]: ...
@overload
def real_if_close(a: _nt._ToArray_nd[_RealT], tol: float = 100) -> _nt.Array[_RealT]: ...
@overload
def real_if_close(a: _nt.ToGeneric_nd, tol: float = 100) -> _nt.Array: ...

#
@overload
def typename(char: L["S1"]) -> L["character"]: ...
@overload
def typename(char: L["?"]) -> L["bool"]: ...
@overload
def typename(char: L["b"]) -> L["signed char"]: ...
@overload
def typename(char: L["B"]) -> L["unsigned char"]: ...
@overload
def typename(char: L["h"]) -> L["short"]: ...
@overload
def typename(char: L["H"]) -> L["unsigned short"]: ...
@overload
def typename(char: L["i"]) -> L["integer"]: ...
@overload
def typename(char: L["I"]) -> L["unsigned integer"]: ...
@overload
def typename(char: L["l"]) -> L["long integer"]: ...
@overload
def typename(char: L["L"]) -> L["unsigned long integer"]: ...
@overload
def typename(char: L["q"]) -> L["long long integer"]: ...
@overload
def typename(char: L["Q"]) -> L["unsigned long long integer"]: ...
@overload
def typename(char: L["f"]) -> L["single precision"]: ...
@overload
def typename(char: L["d"]) -> L["double precision"]: ...
@overload
def typename(char: L["g"]) -> L["long precision"]: ...
@overload
def typename(char: L["F"]) -> L["complex single precision"]: ...
@overload
def typename(char: L["D"]) -> L["complex double precision"]: ...
@overload
def typename(char: L["G"]) -> L["complex long double precision"]: ...
@overload
def typename(char: L["S"]) -> L["string"]: ...
@overload
def typename(char: L["U"]) -> L["unicode"]: ...
@overload
def typename(char: L["V"]) -> L["void"]: ...
@overload
def typename(char: L["O"]) -> L["object"]: ...

# NOTE: mypy reports false-positive overlapping overloads
@overload
def common_type() -> type[np.float16]: ...
@overload
def common_type(a0: _HasDType[np.float16], /, *ai: _HasDType[np.float16]) -> type[np.float16]: ...
@overload
def common_type(a0: _HasDType[np.float32], /, *ai: _HasDType[np.float32 | np.float16]) -> type[np.float32]: ...
@overload
def common_type(
    a0: _HasDType[np.float64 | np.integer], /, *ai: _HasDType[np.float64 | np.float32 | np.float16 | np.integer]
) -> type[np.float64]: ...
@overload
def common_type(a0: _HasDType[np.longdouble], /, *ai: _HasDType[np.floating | np.integer]) -> type[np.longdouble]: ...
@overload
def common_type(a0: _HasDType[np.complex64], /, *ai: _HasDType[_nt.inexact32 | np.float16]) -> type[np.complex64]: ...
@overload
def common_type(
    a0: _HasDType[np.complex128], /, *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer]
) -> type[np.complex128]: ...
@overload
def common_type(a0: _HasDType[np.clongdouble], /, *ai: _HasDType[np.number]) -> type[np.clongdouble]: ...
@overload
def common_type(
    a0: _HasDType[np.float32 | np.float16], array1: _HasDType[np.float32], /, *ai: _HasDType[np.float32 | np.float16]
) -> type[np.float32]: ...
@overload
def common_type(
    a0: _HasDType[np.float64 | np.float32 | np.float16 | np.integer],
    array1: _HasDType[np.float64 | np.integer],
    /,
    *ai: _HasDType[np.float64 | np.float32 | np.float16 | np.integer],
) -> type[np.float64]: ...
@overload
def common_type(
    a0: _HasDType[np.floating | np.integer],
    array1: _HasDType[np.longdouble],
    /,
    *ai: _HasDType[np.floating | np.integer],
) -> type[np.longdouble]: ...
@overload
def common_type(
    a0: _HasDType[_nt.inexact32 | np.float16],
    array1: _HasDType[np.complex64],
    /,
    *ai: _HasDType[_nt.inexact32 | np.float16],
) -> type[np.complex64]: ...
@overload
def common_type(
    a0: _HasDType[np.float64],
    array1: _HasDType[np.complex128 | np.complex64],
    /,
    *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
) -> type[np.complex128]: ...
@overload
def common_type(
    a0: _HasDType[np.complex128 | np.complex64],
    array1: _HasDType[np.float64],
    /,
    *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
) -> type[np.complex128]: ...
@overload
def common_type(
    a0: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
    array1: _HasDType[np.complex128],
    /,
    *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
) -> type[np.complex128]: ...
@overload
def common_type(
    a0: _HasDType[np.complex128 | np.complex64],
    array1: _HasDType[np.complex128 | np.integer],
    /,
    *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
) -> type[np.complex128]: ...
@overload
def common_type(
    a0: _HasDType[np.complex128 | np.integer],
    array1: _HasDType[np.complex128 | np.complex64],
    /,
    *ai: _HasDType[_nt.inexact64 | _nt.inexact32 | np.float16 | np.integer],
) -> type[np.complex128]: ...
@overload
def common_type(
    a0: _HasDType[np.floating | np.integer], /, *ai: _HasDType[np.floating | np.integer]
) -> type[np.floating]: ...
@overload
def common_type(
    a0: _HasDType[np.number], array1: _HasDType[np.clongdouble], /, *ai: _HasDType[np.number]
) -> type[np.clongdouble]: ...
@overload
def common_type(
    a0: _HasDType[np.longdouble], array1: _HasDType[np.complexfloating], /, *ai: _HasDType[np.number]
) -> type[np.clongdouble]: ...
@overload
def common_type(
    a0: _HasDType[np.complexfloating], array1: _HasDType[np.longdouble], /, *ai: _HasDType[np.number]
) -> type[np.clongdouble]: ...
@overload
def common_type(
    a0: _HasDType[np.complexfloating], array1: _HasDType[np.number], /, *ai: _HasDType[np.number]
) -> type[np.complexfloating]: ...
@overload
def common_type(
    a0: _HasDType[np.number], array1: _HasDType[np.complexfloating], /, *ai: _HasDType[np.number]
) -> type[np.complexfloating]: ...
@overload
def common_type(
    a0: _HasDType[np.number], array1: _HasDType[np.number], /, *ai: _HasDType[np.number]
) -> type[np.inexact]: ...
