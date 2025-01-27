from typing import Any, Literal as L, NoReturn, SupportsIndex, SupportsInt, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from numpy import poly1d  # noqa: ICN003
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeUInt_co,
)

_T = TypeVar("_T")

_2Tup: TypeAlias = tuple[_T, _T]
_5Tup: TypeAlias = tuple[_T, NDArray[np.float64], NDArray[np.int32], NDArray[np.float64], NDArray[np.float64]]

__all__ = ["poly", "poly1d", "polyadd", "polyder", "polydiv", "polyfit", "polyint", "polymul", "polysub", "polyval", "roots"]

def poly(seq_of_zeros: ArrayLike) -> NDArray[np.floating]: ...

# Returns either a float or complex array depending on the input values.
# See `np.linalg.eigvals`.
def roots(p: ArrayLike) -> NDArray[np.inexact]: ...
@overload
def polyint(
    p: np.poly1d,
    m: SupportsInt | SupportsIndex = ...,
    k: _ArrayLikeComplex_co | _ArrayLikeObject_co | None = ...,
) -> np.poly1d: ...
@overload
def polyint(
    p: _ArrayLikeFloat_co,
    m: SupportsInt | SupportsIndex = ...,
    k: _ArrayLikeFloat_co | None = ...,
) -> NDArray[np.floating]: ...
@overload
def polyint(
    p: _ArrayLikeComplex_co,
    m: SupportsInt | SupportsIndex = ...,
    k: _ArrayLikeComplex_co | None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def polyint(
    p: _ArrayLikeObject_co,
    m: SupportsInt | SupportsIndex = ...,
    k: _ArrayLikeObject_co | None = ...,
) -> NDArray[np.object_]: ...
@overload
def polyder(p: np.poly1d, m: SupportsInt | SupportsIndex = ...) -> np.poly1d: ...
@overload
def polyder(p: _ArrayLikeFloat_co, m: SupportsInt | SupportsIndex = ...) -> NDArray[np.floating]: ...
@overload
def polyder(p: _ArrayLikeComplex_co, m: SupportsInt | SupportsIndex = ...) -> NDArray[np.complexfloating]: ...
@overload
def polyder(p: _ArrayLikeObject_co, m: SupportsInt | SupportsIndex = ...) -> NDArray[np.object_]: ...
@overload
def polyfit(
    x: _ArrayLikeFloat_co,
    y: _ArrayLikeFloat_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[False] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: L[False] = ...,
) -> NDArray[np.float64]: ...
@overload
def polyfit(
    x: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[False] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: L[False] = ...,
) -> NDArray[np.complex128]: ...
@overload
def polyfit(
    x: _ArrayLikeFloat_co,
    y: _ArrayLikeFloat_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[False] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: L[True, "unscaled"] = ...,
) -> _2Tup[NDArray[np.float64]]: ...
@overload
def polyfit(
    x: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[False] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: L[True, "unscaled"] = ...,
) -> _2Tup[NDArray[np.complex128]]: ...
@overload
def polyfit(
    x: _ArrayLikeFloat_co,
    y: _ArrayLikeFloat_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[True] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: bool | L["unscaled"] = ...,
) -> _5Tup[NDArray[np.float64]]: ...
@overload
def polyfit(
    x: _ArrayLikeComplex_co,
    y: _ArrayLikeComplex_co,
    deg: SupportsIndex | SupportsInt,
    rcond: float | None = ...,
    full: L[True] = ...,
    w: _ArrayLikeFloat_co | None = ...,
    cov: bool | L["unscaled"] = ...,
) -> _5Tup[NDArray[np.complex128]]: ...
@overload
def polyval(p: _ArrayLikeBool_co, x: _ArrayLikeBool_co) -> NDArray[np.int64]: ...
@overload
def polyval(p: _ArrayLikeUInt_co, x: _ArrayLikeUInt_co) -> NDArray[np.unsignedinteger]: ...
@overload
def polyval(p: _ArrayLikeInt_co, x: _ArrayLikeInt_co) -> NDArray[np.signedinteger]: ...
@overload
def polyval(p: _ArrayLikeFloat_co, x: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...
@overload
def polyval(p: _ArrayLikeComplex_co, x: _ArrayLikeComplex_co) -> NDArray[np.complexfloating]: ...
@overload
def polyval(p: _ArrayLikeObject_co, x: _ArrayLikeObject_co) -> NDArray[np.object_]: ...
@overload
def polyadd(a1: np.poly1d, a2: _ArrayLikeComplex_co | _ArrayLikeObject_co) -> np.poly1d: ...
@overload
def polyadd(a1: _ArrayLikeComplex_co | _ArrayLikeObject_co, a2: np.poly1d) -> np.poly1d: ...
@overload
def polyadd(a1: _ArrayLikeBool_co, a2: _ArrayLikeBool_co) -> NDArray[np.bool]: ...
@overload
def polyadd(a1: _ArrayLikeUInt_co, a2: _ArrayLikeUInt_co) -> NDArray[np.unsignedinteger]: ...
@overload
def polyadd(a1: _ArrayLikeInt_co, a2: _ArrayLikeInt_co) -> NDArray[np.signedinteger]: ...
@overload
def polyadd(a1: _ArrayLikeFloat_co, a2: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...
@overload
def polyadd(a1: _ArrayLikeComplex_co, a2: _ArrayLikeComplex_co) -> NDArray[np.complexfloating]: ...
@overload
def polyadd(a1: _ArrayLikeObject_co, a2: _ArrayLikeObject_co) -> NDArray[np.object_]: ...
@overload
def polysub(a1: np.poly1d, a2: _ArrayLikeComplex_co | _ArrayLikeObject_co) -> np.poly1d: ...
@overload
def polysub(a1: _ArrayLikeComplex_co | _ArrayLikeObject_co, a2: np.poly1d) -> np.poly1d: ...
@overload
def polysub(a1: _ArrayLikeBool_co, a2: _ArrayLikeBool_co) -> NoReturn: ...
@overload
def polysub(a1: _ArrayLikeUInt_co, a2: _ArrayLikeUInt_co) -> NDArray[np.unsignedinteger]: ...
@overload
def polysub(a1: _ArrayLikeInt_co, a2: _ArrayLikeInt_co) -> NDArray[np.signedinteger]: ...
@overload
def polysub(a1: _ArrayLikeFloat_co, a2: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...
@overload
def polysub(a1: _ArrayLikeComplex_co, a2: _ArrayLikeComplex_co) -> NDArray[np.complexfloating]: ...
@overload
def polysub(a1: _ArrayLikeObject_co, a2: _ArrayLikeObject_co) -> NDArray[np.object_]: ...

# NOTE: Not an alias, but they do have the same signature (that we can reuse)
polymul = polyadd

@overload
def polydiv(u: np.poly1d, v: _ArrayLikeComplex_co | _ArrayLikeObject_co) -> _2Tup[np.poly1d]: ...
@overload
def polydiv(u: _ArrayLikeComplex_co | _ArrayLikeObject_co, v: np.poly1d) -> _2Tup[np.poly1d]: ...
@overload
def polydiv(u: _ArrayLikeFloat_co, v: _ArrayLikeFloat_co) -> _2Tup[NDArray[np.floating]]: ...
@overload
def polydiv(u: _ArrayLikeComplex_co, v: _ArrayLikeComplex_co) -> _2Tup[NDArray[np.complexfloating]]: ...
@overload
def polydiv(u: _ArrayLikeObject_co, v: _ArrayLikeObject_co) -> _2Tup[NDArray[Any]]: ...
