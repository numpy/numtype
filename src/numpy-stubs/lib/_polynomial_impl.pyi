from collections.abc import Iterator
from typing import Any, ClassVar, Generic, Literal as L, SupportsIndex, SupportsInt, TypeAlias, overload
from typing_extensions import LiteralString, Self, TypeVar

import numpy as np
from _numtype import (
    Array,
    Array_1d,
    CoComplex128_0d,
    CoComplex128_1d,
    CoComplex128_2d,
    CoComplex_0d,
    CoComplex_1d,
    CoComplex_1nd,
    CoComplex_2d,
    CoComplex_nd,
    CoFloat64_0d,
    CoFloat64_1d,
    CoFloating_0d,
    CoFloating_1d,
    CoFloating_1nd,
    CoFloating_2d,
    CoFloating_nd,
    CoInteger_0d,
    CoInteger_1d,
    CoInteger_1nd,
    CoInteger_2d,
    CoSInteger_0d,
    CoSInteger_1d,
    CoSInteger_1nd,
    CoSInteger_nd,
    CoUInteger_0d,
    CoUInteger_1d,
    CoUInteger_1nd,
    CoUInteger_nd,
    Is,
    ToBool_0d,
    ToBool_1d,
    ToBool_1nd,
    ToBool_nd,
    ToCLongDouble_1d,
    ToComplex64_0d,
    ToComplex64_1d,
    ToComplex64_2d,
    ToComplex128_0d,
    ToComplex128_1d,
    ToComplex128_2d,
    ToComplex_0d,
    ToComplex_1d,
    ToComplex_1nd,
    ToComplex_2d,
    ToComplex_nd,
    ToFloat32_1d,
    ToFloat32_2d,
    ToFloat64_1d,
    ToFloat64_2d,
    ToFloating_0d,
    ToFloating_1d,
    ToFloating_1nd,
    ToFloating_nd,
    ToInteger_0d,
    ToInteger_1nd,
    ToLongDouble_1d,
    ToObject_1d,
    ToObject_1nd,
    ToObject_2d,
    ToObject_nd,
    ToSInteger_0d,
    ToSInteger_1d,
    ToSInteger_1nd,
    ToSInteger_nd,
    ToUInteger_0d,
    ToUInteger_1d,
    ToUInteger_1nd,
    ToUInteger_nd,
    _ToArray1_1d,
    _ToArray_1d,
)
from numpy._typing import ArrayLike

__all__ = [
    "poly",
    "poly1d",
    "polyadd",
    "polyder",
    "polydiv",
    "polyfit",
    "polyint",
    "polymul",
    "polymul",
    "polysub",
    "polyval",
    "roots",
]

###

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.number | np.bool | np.object_)
_NumberT = TypeVar("_NumberT", bound=np.number)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.number | np.bool | np.object_, default=Any, covariant=True)

_ToInt: TypeAlias = SupportsInt | SupportsIndex
_Tuple2: TypeAlias = tuple[_T, _T]
_Tuple_didd: TypeAlias = tuple[_T, Array[np.float64], Array[np.int32], Array[np.float64], Array[np.float64]]

###

class poly1d(Generic[_ScalarT_co]):
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

    @property
    def variable(self) -> LiteralString: ...
    @property
    def order(self) -> int: ...
    @property
    def o(self) -> int: ...
    @property
    def roots(self) -> Array_1d[np.inexact]: ...
    @property
    def r(self) -> Array_1d[np.inexact]: ...

    #
    @property
    def coefficients(self) -> Array_1d[_ScalarT_co]: ...
    @coefficients.setter
    def coefficients(self: poly1d[_ScalarT], c: Array[_ScalarT], /) -> None: ...

    #
    @property
    def coeffs(self) -> Array_1d[_ScalarT_co]: ...
    @coeffs.setter
    def coeffs(self: poly1d[_ScalarT], c: Array[_ScalarT], /) -> None: ...

    #
    @property
    def coef(self) -> Array_1d[_ScalarT_co]: ...
    @coef.setter
    def coef(self: poly1d[_ScalarT], c: Array[_ScalarT], /) -> None: ...

    #
    @property
    def c(self) -> Array_1d[_ScalarT_co]: ...
    @c.setter
    def c(self: poly1d[_ScalarT], c: Array[_ScalarT], /) -> None: ...

    #
    @overload
    def __init__(self, /, c_or_r: poly1d[_ScalarT_co], r: bool = False, variable: str | None = None) -> None: ...
    @overload
    def __init__(self, /, c_or_r: _ToArray1_1d[_ScalarT_co], r: L[False] = False, variable: str | None = None) -> None: ...
    @overload
    def __init__(self, /, c_or_r: CoComplex_1d, r: L[True], variable: str | None = None) -> None: ...

    #
    @overload
    def __array__(self, /, t: None = None, copy: bool | None = None) -> Array_1d[_ScalarT_co]: ...
    @overload
    def __array__(self, /, t: np.dtype[_ScalarT], copy: bool | None = None) -> Array_1d[_ScalarT]: ...

    #
    @overload
    def __call__(self, /, val: poly1d) -> poly1d: ...
    @overload
    def __call__(self: poly1d[np.object_], /, val: CoComplex_0d) -> Any: ...
    @overload
    def __call__(self: poly1d[np.bool], /, val: ToBool_0d) -> np.bool: ...
    @overload
    def __call__(self: poly1d[np.integer], /, val: CoInteger_0d) -> np.integer: ...
    @overload
    def __call__(self: poly1d[np.integer | np.bool], /, val: ToInteger_0d) -> np.integer: ...
    @overload
    def __call__(self: poly1d[np.floating], /, val: CoFloating_0d) -> np.floating: ...
    @overload
    def __call__(self: poly1d[np.floating | np.integer | np.bool], /, val: ToFloating_0d) -> np.floating: ...
    @overload
    def __call__(self: poly1d[np.complexfloating], /, val: CoComplex_0d) -> np.complexfloating: ...
    @overload
    def __call__(self: poly1d[np.number | np.bool], /, val: ToComplex_0d) -> np.complexfloating: ...
    @overload
    def __call__(self: poly1d[np.object_], /, val: CoComplex_1nd | ToObject_1nd) -> Array[Any]: ...
    @overload
    def __call__(self: poly1d[np.bool], /, val: ToBool_1nd) -> Array[np.bool]: ...
    @overload
    def __call__(self: poly1d[np.integer], /, val: CoInteger_1nd) -> Array[np.integer]: ...
    @overload
    def __call__(self: poly1d[np.integer | np.bool], /, val: ToInteger_1nd) -> Array[np.integer]: ...
    @overload
    def __call__(self: poly1d[np.floating], /, val: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self: poly1d[np.floating | np.integer | np.bool], /, val: ToFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self: poly1d[np.complexfloating], /, val: CoComplex_1nd) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self: poly1d[np.number | np.bool], /, val: ToComplex_1nd) -> Array[np.complexfloating]: ...

    #
    def __len__(self) -> int: ...

    #
    @overload
    def __iter__(self: poly1d[np.object_]) -> Iterator[Any]: ...
    @overload
    def __iter__(self) -> Iterator[_ScalarT_co]: ...

    #
    @overload
    def __getitem__(self: poly1d[np.object_], val: int, /) -> Any: ...
    @overload
    def __getitem__(self, val: int, /) -> _ScalarT_co: ...

    #
    def __setitem__(self, key: int, val: object, /) -> None: ...

    #
    def __pos__(self) -> Self: ...
    @overload
    def __neg__(self: poly1d[_NumberT]) -> poly1d[_NumberT]: ...
    @overload
    def __neg__(self: poly1d[np.object_]) -> poly1d[np.object_]: ...

    #
    def __add__(self, other: ArrayLike, /) -> poly1d: ...
    def __radd__(self, other: ArrayLike, /) -> poly1d: ...

    #
    def __mul__(self, other: ArrayLike, /) -> poly1d: ...
    def __rmul__(self, other: ArrayLike, /) -> poly1d: ...

    #
    def __sub__(self, other: ArrayLike, /) -> poly1d: ...
    def __rsub__(self, other: ArrayLike, /) -> poly1d: ...

    #
    def __pow__(self, val: CoFloating_0d, /) -> poly1d: ...  # Integral floats are accepted

    #
    def __div__(self, other: ArrayLike, /) -> poly1d: ...
    def __rdiv__(self, other: ArrayLike, /) -> poly1d: ...
    def __truediv__(self, other: ArrayLike, /) -> poly1d: ...
    def __rtruediv__(self, other: ArrayLike, /) -> poly1d: ...

    #
    @overload
    def deriv(self: poly1d[_NumberT], /, m: _ToInt = 1) -> poly1d[_NumberT]: ...
    @overload
    def deriv(self: poly1d[np.bool], /, m: _ToInt = 1) -> poly1d[np.intp]: ...
    @overload
    def deriv(self: poly1d[np.object_], /, m: _ToInt = 1) -> poly1d[np.object_]: ...

    #
    def integ(self, /, m: _ToInt = 1, k: CoComplex_0d | CoComplex_1d | ToObject_1d | None = None) -> poly1d: ...

###

#
@overload
def poly(seq_of_zeros: poly1d) -> Array_1d[np.float64]: ...
@overload
def poly(seq_of_zeros: CoInteger_1d | CoInteger_2d) -> Array_1d[np.float64]: ...
@overload
def poly(seq_of_zeros: ToFloat64_1d | ToFloat64_2d) -> Array_1d[np.float64]: ...  # type: ignore[overload-overlap]
@overload
def poly(seq_of_zeros: ToComplex128_1d | ToComplex128_2d) -> Array_1d[np.complex128]: ...  # type: ignore[overload-overlap]
@overload
def poly(seq_of_zeros: ToFloat32_1d | ToFloat32_2d) -> Array_1d[np.float32]: ...
@overload
def poly(seq_of_zeros: ToComplex64_1d | ToComplex64_2d) -> Array_1d[np.complex64]: ...
@overload
def poly(seq_of_zeros: ToObject_1d | ToObject_2d) -> Array_1d[np.object_]: ...
@overload
def poly(seq_of_zeros: CoComplex128_1d | CoComplex128_2d) -> Array_1d[np.inexact]: ...

# returns either a float or complex array depending on the input values. See `np.linalg.eigvals`.
@overload
def roots(p: CoInteger_1d) -> Array_1d[np.float64 | np.complex128]: ...
@overload
def roots(p: ToFloat64_1d) -> Array_1d[np.float64 | np.complex128]: ...  # type: ignore[overload-overlap]
@overload
def roots(p: ToComplex128_1d) -> Array_1d[np.complex128]: ...  # type: ignore[overload-overlap]
@overload
def roots(p: ToFloat32_1d) -> Array_1d[np.float32 | np.complex64]: ...
@overload
def roots(p: ToComplex64_1d) -> Array_1d[np.complex64]: ...
@overload
def roots(p: CoComplex128_1d) -> Array_1d[np.inexact]: ...

#
@overload
def polyder(p: poly1d, m: _ToInt = 1) -> poly1d: ...
@overload
def polyder(p: CoInteger_1d, m: _ToInt = 1) -> Array_1d[np.intp]: ...
@overload
def polyder(p: _ToArray_1d[np.float64 | np.float32 | np.float16, Is[float]], m: _ToInt = 1) -> Array_1d[np.float64]: ...
@overload
def polyder(p: _ToArray_1d[np.complex128 | np.complex64, Is[complex]], m: _ToInt = 1) -> Array_1d[np.complex128]: ...
@overload
def polyder(p: ToLongDouble_1d, m: _ToInt = 1) -> Array_1d[np.longdouble]: ...  # type: ignore[overload-overlap]
@overload
def polyder(p: ToCLongDouble_1d, m: _ToInt = 1) -> Array_1d[np.clongdouble]: ...  # type: ignore[overload-overlap]
@overload
def polyder(p: ToObject_1d, m: _ToInt = 1) -> Array_1d[np.object_]: ...
@overload
def polyder(p: CoComplex128_1d, m: _ToInt = 1) -> Array_1d[np.complex128 | np.float64 | np.intp]: ...

#
@overload
def polyint(p: poly1d, m: _ToInt = 1, k: CoComplex_nd | ToObject_nd | None = None) -> poly1d: ...
@overload
def polyint(
    p: CoFloat64_1d,
    m: _ToInt = 1,
    k: CoFloat64_0d | CoFloat64_1d | None = None,
) -> Array_1d[np.float64]: ...
@overload
def polyint(
    p: ToLongDouble_1d,
    m: _ToInt = 1,
    k: CoFloating_0d | CoFloating_1d | None = None,
) -> Array_1d[np.longdouble]: ...
@overload
def polyint(
    p: ToComplex128_1d | ToComplex64_1d,
    m: _ToInt = 1,
    k: CoComplex128_0d | CoComplex128_1d | None = None,
) -> Array_1d[np.complex128]: ...
@overload
def polyint(
    p: CoComplex128_1d,
    m: _ToInt,
    k: ToComplex128_0d | ToComplex128_1d | ToComplex64_0d | ToComplex64_1d,
) -> Array_1d[np.complex128]: ...
@overload
def polyint(
    p: CoComplex128_1d,
    m: _ToInt = 1,
    *,
    k: ToComplex128_0d | ToComplex128_1d | ToComplex64_0d | ToComplex64_1d,
) -> Array_1d[np.complex128]: ...
@overload
def polyint(
    p: ToCLongDouble_1d,
    m: _ToInt = 1,
    k: CoComplex_0d | CoComplex_1d | None = None,
) -> Array_1d[np.clongdouble]: ...
@overload
def polyint(
    p: ToObject_1d,
    m: _ToInt = 1,
    k: CoComplex_0d | CoComplex_1d | ToObject_1d | None = None,
) -> Array_1d[np.object_]: ...

#
@overload
def polyfit(
    x: CoFloating_1d,
    y: CoFloating_1d | CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    cov: L[False] = False,
) -> Array[np.float64]: ...
@overload
def polyfit(
    x: CoFloating_1d,
    y: CoFloating_1d | CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[Array[np.float64]]: ...
@overload
def polyfit(
    x: CoFloating_1d,
    y: CoFloating_1d | CoFloating_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.float64]]: ...
@overload
def polyfit(
    x: CoFloating_1d,
    y: CoFloating_1d | CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.float64]]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_1d | ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    cov: L[False] = False,
) -> Array[np.complex128]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_1d | ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[Array[np.complex128]]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_1d | ToComplex_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.complex128]]: ...
@overload
def polyfit(
    x: CoComplex_1d,
    y: ToComplex_1d | ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.complex128]]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_1d | CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    cov: L[False] = False,
) -> Array[np.complex128]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_1d | CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[Array[np.complex128]]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_1d | CoComplex_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.complex128]]: ...
@overload
def polyfit(
    x: ToComplex_1d,
    y: CoComplex_1d | CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[Array[np.complex128]]: ...

#
@overload
def polyval(p: ToBool_1d, x: ToBool_0d) -> np.bool: ...
@overload
def polyval(p: ToUInteger_1d, x: CoUInteger_0d) -> np.unsignedinteger: ...
@overload
def polyval(p: CoUInteger_1d, x: ToUInteger_0d) -> np.unsignedinteger: ...
@overload
def polyval(p: ToSInteger_1d, x: CoSInteger_0d) -> np.signedinteger: ...
@overload
def polyval(p: CoSInteger_1d, x: ToSInteger_0d) -> np.signedinteger: ...
@overload
def polyval(p: ToFloating_1d, x: CoFloating_0d) -> np.floating: ...
@overload
def polyval(p: CoFloating_1d, x: ToFloating_0d) -> np.floating: ...
@overload
def polyval(p: ToComplex_1d, x: CoComplex_0d) -> np.complexfloating: ...
@overload
def polyval(p: CoComplex_1d, x: ToComplex_0d) -> np.complexfloating: ...
@overload
def polyval(p: ToBool_1d, x: ToBool_1nd) -> Array[np.bool]: ...
@overload
def polyval(p: ToUInteger_1d, x: CoUInteger_1nd) -> Array[np.unsignedinteger]: ...
@overload
def polyval(p: CoUInteger_1d, x: ToUInteger_1nd) -> Array[np.unsignedinteger]: ...
@overload
def polyval(p: ToSInteger_1d, x: CoSInteger_1nd) -> Array[np.signedinteger]: ...
@overload
def polyval(p: CoSInteger_1d, x: ToSInteger_1nd) -> Array[np.signedinteger]: ...
@overload
def polyval(p: ToFloating_1d, x: CoFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval(p: CoFloating_1d, x: ToFloating_1nd) -> Array[np.floating]: ...
@overload
def polyval(p: ToComplex_1d, x: CoComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval(p: CoComplex_1d, x: ToComplex_1nd) -> Array[np.complexfloating]: ...
@overload
def polyval(p: ToObject_1d, x: ToObject_1nd) -> Array[np.object_]: ...

#
@overload
def polyadd(a1: poly1d, a2: CoComplex_nd | ToObject_nd) -> poly1d: ...
@overload
def polyadd(a1: CoComplex_nd | ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polyadd(a1: ToBool_nd, a2: ToBool_nd) -> Array[np.bool]: ...
@overload
def polyadd(a1: ToUInteger_nd, a2: CoUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polyadd(a1: CoUInteger_nd, a2: ToUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polyadd(a1: ToSInteger_nd, a2: CoSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polyadd(a1: CoSInteger_nd, a2: ToSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polyadd(a1: ToFloating_nd, a2: CoFloating_nd) -> Array[np.floating]: ...
@overload
def polyadd(a1: CoFloating_nd, a2: ToFloating_nd) -> Array[np.floating]: ...
@overload
def polyadd(a1: ToComplex_nd, a2: CoComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polyadd(a1: CoComplex_nd, a2: ToComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polyadd(a1: ToObject_nd, a2: ToObject_nd) -> Array[np.object_]: ...

# keep in sync with polymul
@overload
def polymul(a1: poly1d, a2: CoComplex_nd | ToObject_nd) -> poly1d: ...
@overload
def polymul(a1: CoComplex_nd | ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polymul(a1: ToBool_nd, a2: ToBool_nd) -> Array[np.bool]: ...
@overload
def polymul(a1: ToUInteger_nd, a2: CoUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polymul(a1: CoUInteger_nd, a2: ToUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polymul(a1: ToSInteger_nd, a2: CoSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polymul(a1: CoSInteger_nd, a2: ToSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polymul(a1: ToFloating_nd, a2: CoFloating_nd) -> Array[np.floating]: ...
@overload
def polymul(a1: CoFloating_nd, a2: ToFloating_nd) -> Array[np.floating]: ...
@overload
def polymul(a1: ToComplex_nd, a2: CoComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polymul(a1: CoComplex_nd, a2: ToComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polymul(a1: ToObject_nd, a2: ToObject_nd) -> Array[np.object_]: ...

#
@overload
def polysub(a1: poly1d, a2: CoComplex_nd | ToObject_nd) -> poly1d: ...
@overload
def polysub(a1: CoComplex_nd | ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polysub(a1: ToUInteger_nd, a2: CoUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polysub(a1: CoUInteger_nd, a2: ToUInteger_nd) -> Array[np.unsignedinteger]: ...
@overload
def polysub(a1: ToSInteger_nd, a2: CoSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polysub(a1: CoSInteger_nd, a2: ToSInteger_nd) -> Array[np.signedinteger]: ...
@overload
def polysub(a1: ToFloating_nd, a2: CoFloating_nd) -> Array[np.floating]: ...
@overload
def polysub(a1: CoFloating_nd, a2: ToFloating_nd) -> Array[np.floating]: ...
@overload
def polysub(a1: ToComplex_nd, a2: CoComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polysub(a1: CoComplex_nd, a2: ToComplex_nd) -> Array[np.complexfloating]: ...
@overload
def polysub(a1: ToObject_nd, a2: ToObject_nd) -> Array[np.object_]: ...

#
@overload
def polydiv(u: poly1d, v: CoComplex_nd | ToObject_nd) -> _Tuple2[poly1d]: ...
@overload
def polydiv(u: CoComplex_nd | ToObject_nd, v: poly1d) -> _Tuple2[poly1d]: ...
@overload
def polydiv(u: CoFloating_nd, v: CoFloating_nd) -> _Tuple2[Array[np.floating]]: ...
@overload
def polydiv(u: ToComplex_nd, v: CoComplex_nd) -> _Tuple2[Array[np.complexfloating]]: ...
@overload
def polydiv(u: CoComplex_nd, v: ToComplex_nd) -> _Tuple2[Array[np.complexfloating]]: ...
@overload
def polydiv(u: ToObject_nd, v: ToObject_nd) -> _Tuple2[Array[Any]]: ...
