from collections.abc import Iterator
from typing import Any, ClassVar, Generic, Literal as L, SupportsIndex, SupportsInt, TypeAlias, overload
from typing_extensions import LiteralString, Self, TypeVar

import _numtype as _nt
import numpy as np
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
_ScalarT = TypeVar("_ScalarT", bound=_nt.co_complex | np.object_)
_NumberT = TypeVar("_NumberT", bound=np.number)
_ScalarT_co = TypeVar("_ScalarT_co", bound=_nt.co_complex | np.object_, default=Any, covariant=True)

_ToInt: TypeAlias = SupportsInt | SupportsIndex
_Tuple2: TypeAlias = tuple[_T, _T]
_Tuple_didd: TypeAlias = tuple[
    _T,
    _nt.Array[np.float64],
    _nt.Array[np.int32],
    _nt.Array[np.float64],
    _nt.Array[np.float64],
]

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
    def roots(self) -> _nt.Array1D[np.inexact]: ...
    @property
    def r(self) -> _nt.Array1D[np.inexact]: ...

    #
    @property
    def coefficients(self) -> _nt.Array1D[_ScalarT_co]: ...
    @coefficients.setter
    def coefficients(self: poly1d[_ScalarT], c: _nt.Array[_ScalarT], /) -> None: ...

    #
    @property
    def coeffs(self) -> _nt.Array1D[_ScalarT_co]: ...
    @coeffs.setter
    def coeffs(self: poly1d[_ScalarT], c: _nt.Array[_ScalarT], /) -> None: ...

    #
    @property
    def coef(self) -> _nt.Array1D[_ScalarT_co]: ...
    @coef.setter
    def coef(self: poly1d[_ScalarT], c: _nt.Array[_ScalarT], /) -> None: ...

    #
    @property
    def c(self) -> _nt.Array1D[_ScalarT_co]: ...
    @c.setter
    def c(self: poly1d[_ScalarT], c: _nt.Array[_ScalarT], /) -> None: ...

    #
    @overload
    def __init__(self, /, c_or_r: poly1d[_ScalarT_co], r: bool = False, variable: str | None = None) -> None: ...
    @overload
    def __init__(
        self, /, c_or_r: _nt._ToArray_1d[_ScalarT_co], r: L[False] = False, variable: str | None = None
    ) -> None: ...
    @overload
    def __init__(self, /, c_or_r: _nt.CoComplex_1d, r: L[True], variable: str | None = None) -> None: ...

    #
    @overload
    def __array__(self, /, t: None = None, copy: bool | None = None) -> _nt.Array1D[_ScalarT_co]: ...
    @overload
    def __array__(self, /, t: np.dtype[_ScalarT], copy: bool | None = None) -> _nt.Array1D[_ScalarT]: ...

    #
    @overload
    def __call__(self, /, val: poly1d) -> poly1d: ...
    @overload
    def __call__(self: poly1d[np.object_], /, val: _nt.CoComplex_0d) -> Any: ...
    @overload
    def __call__(self: poly1d[np.bool], /, val: _nt.ToBool_0d) -> np.bool: ...
    @overload
    def __call__(self: poly1d[np.integer], /, val: _nt.CoInteger_0d) -> np.integer: ...
    @overload
    def __call__(self: poly1d[np.integer | np.bool], /, val: _nt.ToInteger_0d) -> np.integer: ...
    @overload
    def __call__(self: poly1d[np.floating], /, val: _nt.CoFloating_0d) -> np.floating: ...
    @overload
    def __call__(self: poly1d[_nt.co_float], /, val: _nt.ToFloating_0d) -> np.floating: ...
    @overload
    def __call__(self: poly1d[np.complexfloating], /, val: _nt.CoComplex_0d) -> np.complexfloating: ...
    @overload
    def __call__(self: poly1d[_nt.co_complex], /, val: _nt.ToComplex_0d) -> np.complexfloating: ...
    @overload
    def __call__(self: poly1d[np.object_], /, val: _nt.CoComplex_1nd | _nt.ToObject_1nd) -> _nt.Array[Any]: ...
    @overload
    def __call__(self: poly1d[np.bool], /, val: _nt.ToBool_1nd) -> _nt.Array[np.bool]: ...
    @overload
    def __call__(self: poly1d[np.integer], /, val: _nt.CoInteger_1nd) -> _nt.Array[np.integer]: ...
    @overload
    def __call__(self: poly1d[np.integer | np.bool], /, val: _nt.ToInteger_1nd) -> _nt.Array[np.integer]: ...
    @overload
    def __call__(self: poly1d[np.floating], /, val: _nt.CoFloating_1nd) -> _nt.Array[np.floating]: ...
    @overload
    def __call__(self: poly1d[_nt.co_float], /, val: _nt.ToFloating_1nd) -> _nt.Array[np.floating]: ...
    @overload
    def __call__(self: poly1d[np.complexfloating], /, val: _nt.CoComplex_1nd) -> _nt.Array[np.complexfloating]: ...
    @overload
    def __call__(self: poly1d[_nt.co_complex], /, val: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...

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
    def __mul__(self, other: ArrayLike, /) -> poly1d: ...
    def __rmul__(self, other: ArrayLike, /) -> poly1d: ...
    def __sub__(self, other: ArrayLike, /) -> poly1d: ...
    def __rsub__(self, other: ArrayLike, /) -> poly1d: ...
    def __pow__(self, val: _nt.CoFloating_0d, /) -> poly1d: ...  # Integral floats are accepted
    def __truediv__(self, other: ArrayLike, /) -> poly1d: ...
    def __rtruediv__(self, other: ArrayLike, /) -> poly1d: ...
    def __div__(self, other: ArrayLike, /) -> poly1d: ...
    def __rdiv__(self, other: ArrayLike, /) -> poly1d: ...

    #
    @overload
    def deriv(self: poly1d[_NumberT], /, m: _ToInt = 1) -> poly1d[_NumberT]: ...
    @overload
    def deriv(self: poly1d[np.bool], /, m: _ToInt = 1) -> poly1d[np.intp]: ...
    @overload
    def deriv(self: poly1d[np.object_], /, m: _ToInt = 1) -> poly1d[np.object_]: ...

    #
    def integ(
        self, /, m: _ToInt = 1, k: _nt.CoComplex_0d | _nt.CoComplex_1d | _nt.ToObject_1d | None = 0
    ) -> poly1d: ...

###

#
@overload
def poly(seq_of_zeros: poly1d) -> _nt.Array1D[np.float64]: ...
@overload
def poly(seq_of_zeros: _nt.CoInteger_1d | _nt.CoInteger_2d) -> _nt.Array1D[np.float64]: ...
@overload
def poly(seq_of_zeros: _nt.ToFloat64_1d | _nt.ToFloat64_2d) -> _nt.Array1D[np.float64]: ...
@overload
def poly(seq_of_zeros: _nt.ToComplex128_1d | _nt.ToComplex128_2d) -> _nt.Array1D[np.complex128]: ...
@overload
def poly(seq_of_zeros: _nt.ToFloat32_1d | _nt.ToFloat32_2d) -> _nt.Array1D[np.float32]: ...
@overload
def poly(seq_of_zeros: _nt.ToComplex64_1d | _nt.ToComplex64_2d) -> _nt.Array1D[np.complex64]: ...
@overload
def poly(seq_of_zeros: _nt.ToObject_1d | _nt.ToObject_2d) -> _nt.Array1D[np.object_]: ...
@overload
def poly(seq_of_zeros: _nt.CoComplex128_1d | _nt.CoComplex128_2d) -> _nt.Array1D[np.inexact]: ...

# returns either a float or complex array depending on the input values. See `np.linalg.eigvals`.
@overload
def roots(p: _nt.CoInteger_1d) -> _nt.Array1D[_nt.inexact64]: ...
@overload
def roots(p: _nt.ToFloat64_1d) -> _nt.Array1D[_nt.inexact64]: ...
@overload
def roots(p: _nt.ToComplex128_1d) -> _nt.Array1D[np.complex128]: ...
@overload
def roots(p: _nt.ToFloat32_1d) -> _nt.Array1D[_nt.inexact32]: ...
@overload
def roots(p: _nt.ToComplex64_1d) -> _nt.Array1D[np.complex64]: ...
@overload
def roots(p: _nt.CoComplex128_1d) -> _nt.Array1D[np.inexact]: ...

#
@overload
def polyder(p: poly1d, m: _ToInt = 1) -> poly1d: ...
@overload
def polyder(p: _nt.CoInteger_1d, m: _ToInt = 1) -> _nt.Array1D[np.intp]: ...
@overload
def polyder(
    p: _nt._ToArray2_1d[np.float64 | np.float32 | np.float16, _nt.JustFloat],
    m: _ToInt = 1,
) -> _nt.Array1D[np.float64]: ...
@overload
def polyder(
    p: _nt._ToArray2_1d[np.complex128 | np.complex64, _nt.JustComplex],
    m: _ToInt = 1,
) -> _nt.Array1D[np.complex128]: ...
@overload
def polyder(p: _nt.ToLongDouble_1d, m: _ToInt = 1) -> _nt.Array1D[np.longdouble]: ...
@overload
def polyder(p: _nt.ToCLongDouble_1d, m: _ToInt = 1) -> _nt.Array1D[np.clongdouble]: ...
@overload
def polyder(p: _nt.ToObject_1d, m: _ToInt = 1) -> _nt.Array1D[np.object_]: ...
@overload
def polyder(p: _nt.CoComplex128_1d, m: _ToInt = 1) -> _nt.Array1D[np.complex128 | np.float64 | np.intp]: ...

#
@overload
def polyint(p: poly1d, m: _ToInt = 1, k: _nt.CoComplex_nd | _nt.ToObject_nd | None = None) -> poly1d: ...
@overload
def polyint(
    p: _nt.CoFloat64_1d,
    m: _ToInt = 1,
    k: _nt.CoFloat64_0d | _nt.CoFloat64_1d | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload
def polyint(
    p: _nt.ToLongDouble_1d,
    m: _ToInt = 1,
    k: _nt.CoFloating_0d | _nt.CoFloating_1d | None = None,
) -> _nt.Array1D[np.longdouble]: ...
@overload
def polyint(
    p: _nt.ToComplex128_1d | _nt.ToComplex64_1d,
    m: _ToInt = 1,
    k: _nt.CoComplex128_0d | _nt.CoComplex128_1d | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload
def polyint(
    p: _nt.CoComplex128_1d,
    m: _ToInt,
    k: _nt.ToComplex128_0d | _nt.ToComplex128_1d | _nt.ToComplex64_0d | _nt.ToComplex64_1d,
) -> _nt.Array1D[np.complex128]: ...
@overload
def polyint(
    p: _nt.CoComplex128_1d,
    m: _ToInt = 1,
    *,
    k: _nt.ToComplex128_0d | _nt.ToComplex128_1d | _nt.ToComplex64_0d | _nt.ToComplex64_1d,
) -> _nt.Array1D[np.complex128]: ...
@overload
def polyint(
    p: _nt.ToCLongDouble_1d,
    m: _ToInt = 1,
    k: _nt.CoComplex_0d | _nt.CoComplex_1d | None = None,
) -> _nt.Array1D[np.clongdouble]: ...
@overload
def polyint(
    p: _nt.ToObject_1d,
    m: _ToInt = 1,
    k: _nt.CoComplex_0d | _nt.CoComplex_1d | _nt.ToObject_1d | None = None,
) -> _nt.Array1D[np.object_]: ...

#
@overload
def polyfit(
    x: _nt.CoFloating_1d,
    y: _nt.CoFloating_1d | _nt.CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    cov: L[False] = False,
) -> _nt.Array[np.float64]: ...
@overload
def polyfit(
    x: _nt.CoFloating_1d,
    y: _nt.CoFloating_1d | _nt.CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[_nt.Array[np.float64]]: ...
@overload
def polyfit(
    x: _nt.CoFloating_1d,
    y: _nt.CoFloating_1d | _nt.CoFloating_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.float64]]: ...
@overload
def polyfit(
    x: _nt.CoFloating_1d,
    y: _nt.CoFloating_1d | _nt.CoFloating_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.float64]]: ...
@overload
def polyfit(
    x: _nt.CoComplex_1d,
    y: _nt.ToComplex_1d | _nt.ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    cov: L[False] = False,
) -> _nt.Array[np.complex128]: ...
@overload
def polyfit(
    x: _nt.CoComplex_1d,
    y: _nt.ToComplex_1d | _nt.ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[_nt.Array[np.complex128]]: ...
@overload
def polyfit(
    x: _nt.CoComplex_1d,
    y: _nt.ToComplex_1d | _nt.ToComplex_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.complex128]]: ...
@overload
def polyfit(
    x: _nt.CoComplex_1d,
    y: _nt.ToComplex_1d | _nt.ToComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.complex128]]: ...
@overload
def polyfit(
    x: _nt.ToComplex_1d,
    y: _nt.CoComplex_1d | _nt.CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    cov: L[False] = False,
) -> _nt.Array[np.complex128]: ...
@overload
def polyfit(
    x: _nt.ToComplex_1d,
    y: _nt.CoComplex_1d | _nt.CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    full: L[False] = False,
    w: _nt.CoFloating_1d | None = None,
    *,
    cov: L[True, "unscaled"],
) -> _Tuple2[_nt.Array[np.complex128]]: ...
@overload
def polyfit(
    x: _nt.ToComplex_1d,
    y: _nt.CoComplex_1d | _nt.CoComplex_2d,
    deg: _ToInt,
    rcond: float | None,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.complex128]]: ...
@overload
def polyfit(
    x: _nt.ToComplex_1d,
    y: _nt.CoComplex_1d | _nt.CoComplex_2d,
    deg: _ToInt,
    rcond: float | None = None,
    *,
    full: L[True],
    w: _nt.CoFloating_1d | None = None,
    cov: bool | L["unscaled"] = False,
) -> _Tuple_didd[_nt.Array[np.complex128]]: ...

#
@overload
def polyval(p: _nt.ToBool_1d, x: _nt.ToBool_0d) -> np.bool: ...
@overload
def polyval(p: _nt.ToUInteger_1d, x: _nt.CoUInt64_0d) -> np.unsignedinteger: ...
@overload
def polyval(p: _nt.CoUInt64_1d, x: _nt.ToUInteger_0d) -> np.unsignedinteger: ...
@overload
def polyval(p: _nt.ToSInteger_1d, x: _nt.CoInt64_0d) -> np.signedinteger: ...
@overload
def polyval(p: _nt.CoInt64_1d, x: _nt.ToSInteger_0d) -> np.signedinteger: ...
@overload
def polyval(p: _nt.ToFloating_1d, x: _nt.CoFloating_0d) -> np.floating: ...
@overload
def polyval(p: _nt.CoFloating_1d, x: _nt.ToFloating_0d) -> np.floating: ...
@overload
def polyval(p: _nt.ToComplex_1d, x: _nt.CoComplex_0d) -> np.complexfloating: ...
@overload
def polyval(p: _nt.CoComplex_1d, x: _nt.ToComplex_0d) -> np.complexfloating: ...
@overload
def polyval(p: _nt.ToBool_1d, x: _nt.ToBool_1nd) -> _nt.Array[np.bool]: ...
@overload
def polyval(p: _nt.ToUInteger_1d, x: _nt.CoUInt64_1nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polyval(p: _nt.CoUInt64_1d, x: _nt.ToUInteger_1nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polyval(p: _nt.ToSInteger_1d, x: _nt.CoInt64_1nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polyval(p: _nt.CoInt64_1d, x: _nt.ToSInteger_1nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polyval(p: _nt.ToFloating_1d, x: _nt.CoFloating_1nd) -> _nt.Array[np.floating]: ...
@overload
def polyval(p: _nt.CoFloating_1d, x: _nt.ToFloating_1nd) -> _nt.Array[np.floating]: ...
@overload
def polyval(p: _nt.ToComplex_1d, x: _nt.CoComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polyval(p: _nt.CoComplex_1d, x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polyval(p: _nt.ToObject_1d, x: _nt.ToObject_1nd) -> _nt.Array[np.object_]: ...

#
@overload
def polyadd(a1: poly1d, a2: _nt.CoComplex_nd | _nt.ToObject_nd) -> poly1d: ...
@overload
def polyadd(a1: _nt.CoComplex_nd | _nt.ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polyadd(a1: _nt.ToBool_nd, a2: _nt.ToBool_nd) -> _nt.Array[np.bool]: ...
@overload
def polyadd(a1: _nt.ToUInteger_nd, a2: _nt.CoUInt64_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polyadd(a1: _nt.CoUInt64_nd, a2: _nt.ToUInteger_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polyadd(a1: _nt.ToSInteger_nd, a2: _nt.CoInt64_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polyadd(a1: _nt.CoInt64_nd, a2: _nt.ToSInteger_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polyadd(a1: _nt.ToFloating_nd, a2: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polyadd(a1: _nt.CoFloating_nd, a2: _nt.ToFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polyadd(a1: _nt.ToComplex_nd, a2: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polyadd(a1: _nt.CoComplex_nd, a2: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polyadd(a1: _nt.ToObject_nd, a2: _nt.ToObject_nd) -> _nt.Array[np.object_]: ...

# keep in sync with polymul
@overload
def polymul(a1: poly1d, a2: _nt.CoComplex_nd | _nt.ToObject_nd) -> poly1d: ...
@overload
def polymul(a1: _nt.CoComplex_nd | _nt.ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polymul(a1: _nt.ToBool_nd, a2: _nt.ToBool_nd) -> _nt.Array[np.bool]: ...
@overload
def polymul(a1: _nt.ToUInteger_nd, a2: _nt.CoUInt64_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polymul(a1: _nt.CoUInt64_nd, a2: _nt.ToUInteger_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polymul(a1: _nt.ToSInteger_nd, a2: _nt.CoInt64_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polymul(a1: _nt.CoInt64_nd, a2: _nt.ToSInteger_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polymul(a1: _nt.ToFloating_nd, a2: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polymul(a1: _nt.CoFloating_nd, a2: _nt.ToFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polymul(a1: _nt.ToComplex_nd, a2: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polymul(a1: _nt.CoComplex_nd, a2: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polymul(a1: _nt.ToObject_nd, a2: _nt.ToObject_nd) -> _nt.Array[np.object_]: ...

#
@overload
def polysub(a1: poly1d, a2: _nt.CoComplex_nd | _nt.ToObject_nd) -> poly1d: ...
@overload
def polysub(a1: _nt.CoComplex_nd | _nt.ToObject_nd, a2: poly1d) -> poly1d: ...
@overload
def polysub(a1: _nt.ToUInteger_nd, a2: _nt.CoUInt64_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polysub(a1: _nt.CoUInt64_nd, a2: _nt.ToUInteger_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def polysub(a1: _nt.ToSInteger_nd, a2: _nt.CoInt64_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polysub(a1: _nt.CoInt64_nd, a2: _nt.ToSInteger_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def polysub(a1: _nt.ToFloating_nd, a2: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polysub(a1: _nt.CoFloating_nd, a2: _nt.ToFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def polysub(a1: _nt.ToComplex_nd, a2: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polysub(a1: _nt.CoComplex_nd, a2: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def polysub(a1: _nt.ToObject_nd, a2: _nt.ToObject_nd) -> _nt.Array[np.object_]: ...

#
@overload
def polydiv(u: poly1d, v: _nt.CoComplex_nd | _nt.ToObject_nd) -> _Tuple2[poly1d]: ...
@overload
def polydiv(u: _nt.CoComplex_nd | _nt.ToObject_nd, v: poly1d) -> _Tuple2[poly1d]: ...
@overload
def polydiv(u: _nt.CoFloating_nd, v: _nt.CoFloating_nd) -> _Tuple2[_nt.Array[np.floating]]: ...
@overload
def polydiv(u: _nt.ToComplex_nd, v: _nt.CoComplex_nd) -> _Tuple2[_nt.Array[np.complexfloating]]: ...
@overload
def polydiv(u: _nt.CoComplex_nd, v: _nt.ToComplex_nd) -> _Tuple2[_nt.Array[np.complexfloating]]: ...
@overload
def polydiv(u: _nt.ToObject_nd, v: _nt.ToObject_nd) -> _Tuple2[_nt.Array[Any]]: ...
