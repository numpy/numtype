from collections.abc import Container, Iterable
from typing import Any, Literal as L, TypeVar, overload

import numpy as np
from numpy._typing import ArrayLike, NBitBase, NDArray, _64Bit, _ArrayLike, _ScalarLike_co, _SupportsDType

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

_T = TypeVar("_T")
_SCT = TypeVar("_SCT", bound=np.generic)
_NBit1 = TypeVar("_NBit1", bound=NBitBase)
_NBit2 = TypeVar("_NBit2", bound=NBitBase)

def mintypecode(
    typechars: Iterable[str | ArrayLike],
    typeset: Container[str] = ...,
    default: str = ...,
) -> str: ...
@overload
def real(val: np._HasRealAndImag[_T, Any]) -> _T: ...
@overload
def real(val: ArrayLike) -> NDArray[Any]: ...
@overload
def imag(val: np._HasRealAndImag[Any, _T]) -> _T: ...
@overload
def imag(val: ArrayLike) -> NDArray[Any]: ...
@overload
def iscomplex(x: _ScalarLike_co) -> np.bool: ...  # type: ignore[misc]
@overload
def iscomplex(x: ArrayLike) -> NDArray[np.bool]: ...
@overload
def isreal(x: _ScalarLike_co) -> np.bool: ...  # type: ignore[misc]
@overload
def isreal(x: ArrayLike) -> NDArray[np.bool]: ...
def iscomplexobj(x: _SupportsDType[np.dtype[Any]] | ArrayLike) -> bool: ...
def isrealobj(x: _SupportsDType[np.dtype[Any]] | ArrayLike) -> bool: ...
@overload
def nan_to_num(  # type: ignore[misc]
    x: _SCT,
    copy: bool = ...,
    nan: float = ...,
    posinf: float | None = ...,
    neginf: float | None = ...,
) -> _SCT: ...
@overload
def nan_to_num(
    x: _ScalarLike_co,
    copy: bool = ...,
    nan: float = ...,
    posinf: float | None = ...,
    neginf: float | None = ...,
) -> Any: ...
@overload
def nan_to_num(
    x: _ArrayLike[_SCT],
    copy: bool = ...,
    nan: float = ...,
    posinf: float | None = ...,
    neginf: float | None = ...,
) -> NDArray[_SCT]: ...
@overload
def nan_to_num(
    x: ArrayLike,
    copy: bool = ...,
    nan: float = ...,
    posinf: float | None = ...,
    neginf: float | None = ...,
) -> NDArray[Any]: ...

# If one passes a complex array to `real_if_close`, then one is reasonably
# expected to verify the output dtype (so we can return an unsafe union here)

@overload
def real_if_close(a: _ArrayLike[np.complexfloating[_NBit1]], tol: float = ...) -> NDArray[np.inexact[_NBit1]]: ...
@overload
def real_if_close(a: _ArrayLike[_SCT], tol: float = ...) -> NDArray[_SCT]: ...
@overload
def real_if_close(a: ArrayLike, tol: float = ...) -> NDArray[Any]: ...
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
@overload
def common_type(*arrays: _SupportsDType[np.dtype[np.integer]]) -> type[np.float64]: ...
@overload
def common_type(*arrays: _SupportsDType[np.dtype[np.floating[_NBit1]]]) -> type[np.floating[_NBit1]]: ...
@overload
def common_type(*arrays: _SupportsDType[np.dtype[np.integer | np.floating[_NBit1]]]) -> type[np.floating[_NBit1 | _64Bit]]: ...
@overload
def common_type(*arrays: _SupportsDType[np.dtype[np.inexact[_NBit1]]]) -> type[np.complexfloating[_NBit1]]: ...
@overload
def common_type(
    *arrays: _SupportsDType[np.dtype[np.integer | np.floating[_NBit1] | np.complexfloating[_NBit2]]],
) -> type[np.complexfloating[_64Bit | _NBit1 | _NBit2]]: ...
