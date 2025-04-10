from collections.abc import Mapping
from types import EllipsisType
from typing import Any, ClassVar, SupportsIndex as CanIndex, TypeAlias, overload
from typing_extensions import Self, TypeVar, override

import numpy as np
from _numtype import (
    Array,
    JustBytes,
    JustComplex,
    JustFloat,
    JustInt,
    JustStr,
    Matrix,
    Sequence3ND,
    ToBool_nd,
    ToBytes_nd,
    ToComplex128_nd,
    ToFloat64_nd,
    ToGeneric_3nd,
    ToGeneric_nd,
    ToInt_nd,
    ToInteger_1nd,
    ToObject_nd,
    ToStr_nd,
    _ToArray_1nd,
    _ToArray_nd,
)
from numpy import _CanItem, _OrderKACF  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, _ArrayLikeInt_co, _DTypeLike

__all__ = ["asmatrix", "bmat", "matrix"]

###

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=Array)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_2D, default=_2D, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)

_2D: TypeAlias = tuple[int, int]

_ToIndex1: TypeAlias = slice | EllipsisType | ToInteger_1nd | None
_ToIndex2: TypeAlias = tuple[_ToIndex1, _ToIndex1 | CanIndex] | tuple[_ToIndex1 | CanIndex, _ToIndex1]

_ToAxis: TypeAlias = CanIndex | tuple[()] | tuple[CanIndex] | tuple[CanIndex, CanIndex]

###

class matrix(np.ndarray[_ShapeT_co, _DTypeT_co]):
    __array_priority__: ClassVar[float] = 10.0  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def __new__(subtype, data: ArrayLike, dtype: DTypeLike | None = None, copy: bool = ...) -> Matrix: ...

    #
    @overload  # type: ignore[override]
    def __getitem__(self, key: CanIndex | _ArrayLikeInt_co | tuple[CanIndex | _ArrayLikeInt_co, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndex1 | _ToIndex2, /) -> matrix[_2D, _DTypeT_co]: ...
    @overload
    def __getitem__(self: Array[np.void], key: str, /) -> matrix[_ShapeT_co, np.dtype]: ...
    @overload
    def __getitem__(self: Array[np.void], key: list[str], /) -> matrix[_ShapeT_co, np.dtype[np.void]]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __mul__(self, other: ArrayLike, /) -> Matrix: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rmul__(self, other: ArrayLike, /) -> Matrix: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __imul__(self, other: ArrayLike, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __pow__(self, other: ArrayLike, /) -> Matrix: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rpow__(self, other: ArrayLike, /) -> Matrix: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ipow__(self, other: ArrayLike, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def sum(self, /, axis: None = None, dtype: DTypeLike | None = None, out: None = None) -> Any: ...
    @overload
    def sum(self, /, axis: _ToAxis, dtype: DTypeLike | None = None, out: None = None) -> Matrix: ...
    @overload
    def sum(self, /, axis: _ToAxis | None, dtype: DTypeLike, out: _ArrayT) -> _ArrayT: ...
    @overload
    def sum(self, /, axis: _ToAxis | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def mean(self, /, axis: None = None, dtype: DTypeLike | None = None, out: None = None) -> Any: ...
    @overload
    def mean(self, /, axis: _ToAxis, dtype: DTypeLike | None = None, out: None = None) -> Matrix: ...
    @overload
    def mean(self, /, axis: _ToAxis | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def mean(self, /, axis: _ToAxis | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def std(self, /, axis: None = None, dtype: DTypeLike | None = None, out: None = None, ddof: float = 0) -> Any: ...
    @overload
    def std(self, /, axis: _ToAxis, dtype: DTypeLike | None = None, out: None = None, ddof: float = 0) -> Matrix: ...
    @overload
    def std(self, /, axis: _ToAxis | None, dtype: DTypeLike | None, out: _ArrayT, ddof: float = 0) -> _ArrayT: ...
    @overload
    def std(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: _ToAxis | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
    ) -> _ArrayT: ...

    #
    @overload  # type: ignore[override]
    def var(self, /, axis: None = None, dtype: DTypeLike | None = None, out: None = None, ddof: float = 0) -> Any: ...
    @overload
    def var(self, /, axis: _ToAxis, dtype: DTypeLike | None = None, out: None = None, ddof: float = 0) -> Matrix: ...
    @overload
    def var(self, /, axis: _ToAxis | None, dtype: DTypeLike | None, out: _ArrayT, ddof: float = 0) -> _ArrayT: ...
    @overload
    def var(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: _ToAxis | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
    ) -> _ArrayT: ...

    #
    @overload  # type: ignore[override]
    def prod(self, /, axis: None = None, dtype: DTypeLike | None = None, out: None = None) -> Any: ...
    @overload
    def prod(self, /, axis: _ToAxis, dtype: DTypeLike | None = None, out: None = None) -> Matrix: ...
    @overload
    def prod(self, /, axis: _ToAxis | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def prod(self, /, axis: _ToAxis | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def any(self, /, axis: None = None, out: None = None) -> np.bool: ...
    @overload
    def any(self, /, axis: _ToAxis, out: None = None) -> Matrix[np.bool]: ...
    @overload
    def any(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def any(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def all(self, /, axis: None = None, out: None = None) -> np.bool: ...
    @overload
    def all(self, /, axis: _ToAxis, out: None = None) -> Matrix[np.bool]: ...
    @overload
    def all(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def all(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def max(self: Array[_ScalarT], /, axis: None = None, out: None = None) -> _ScalarT: ...
    @overload
    def max(self, /, axis: _ToAxis, out: None = None) -> matrix[_2D, _DTypeT_co]: ...
    @overload
    def max(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def max(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def min(self: Array[_ScalarT], /, axis: None = None, out: None = None) -> _ScalarT: ...
    @overload
    def min(self, /, axis: _ToAxis, out: None = None) -> matrix[_2D, _DTypeT_co]: ...
    @overload
    def min(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def min(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def argmax(self: Array[_ScalarT], /, axis: None = None, out: None = None) -> np.intp: ...
    @overload
    def argmax(self, /, axis: _ToAxis, out: None = None) -> Matrix[np.intp]: ...
    @overload
    def argmax(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def argmax(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def argmin(self: Array[_ScalarT], /, axis: None = None, out: None = None) -> np.intp: ...
    @overload
    def argmin(self, /, axis: _ToAxis, out: None = None) -> Matrix[np.intp]: ...
    @overload
    def argmin(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def argmin(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def ptp(self: Array[_ScalarT], /, axis: None = None, out: None = None) -> _ScalarT: ...
    @overload
    def ptp(self, /, axis: _ToAxis, out: None = None) -> matrix[_2D, _DTypeT_co]: ...
    @overload
    def ptp(self, /, axis: _ToAxis | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def ptp(self, /, axis: _ToAxis | None = None, *, out: _ArrayT) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleVariableOverride]

    #
    @override
    def tolist(self: _CanItem[_T], /) -> list[list[_T]]: ...  # type: ignore[override]

    #
    @override
    def squeeze(self, /, axis: _ToAxis | None = None) -> matrix[_2D, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def ravel(self, /, order: _OrderKACF = "C") -> matrix[_2D, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def flatten(self, /, order: _OrderKACF = "C") -> matrix[_2D, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @property
    @override
    def T(self) -> matrix[_2D, _DTypeT_co]: ...  # type: ignore[override]
    def getT(self) -> matrix[_2D, _DTypeT_co]: ...

    #
    @property
    def H(self) -> matrix[_2D, _DTypeT_co]: ...
    def getH(self) -> matrix[_2D, _DTypeT_co]: ...

    #
    @property
    def I(self) -> Matrix: ...
    def getI(self) -> Matrix: ...

    #
    @property
    def A(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    def getA(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @property
    def A1(self) -> np.ndarray[tuple[int], _DTypeT_co]: ...
    def getA1(self) -> np.ndarray[tuple[int], _DTypeT_co]: ...

#
@overload
def bmat(
    obj: str,
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix: ...
@overload
def bmat(
    obj: _ToArray_1nd[_ScalarT],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[_ScalarT]: ...
@overload
def bmat(
    obj: Sequence3ND[bool],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.bool]: ...
@overload
def bmat(
    obj: Sequence3ND[JustInt],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.intp]: ...
@overload
def bmat(
    obj: Sequence3ND[JustFloat],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.float64]: ...
@overload
def bmat(
    obj: Sequence3ND[JustComplex],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.complex128]: ...
@overload
def bmat(
    obj: Sequence3ND[JustBytes],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.bytes_]: ...
@overload
def bmat(
    obj: Sequence3ND[JustStr],
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix[np.str_]: ...
@overload
def bmat(
    obj: ToGeneric_3nd,
    ldict: Mapping[str, Any] | None = None,
    gdict: Mapping[str, Any] | None = None,
) -> Matrix: ...

#
@overload
def asmatrix(data: _ToArray_nd[_ScalarT], dtype: None = None) -> Matrix[_ScalarT]: ...  # type: ignore[overload-overlap]
@overload
def asmatrix(data: ToGeneric_nd, dtype: _DTypeLike[_ScalarT]) -> Matrix[_ScalarT]: ...
@overload
def asmatrix(data: ToBool_nd, dtype: None = None) -> Matrix[np.bool]: ...
@overload
def asmatrix(data: ToInt_nd, dtype: None = None) -> Matrix[np.intp]: ...
@overload
def asmatrix(data: ToFloat64_nd, dtype: None = None) -> Matrix[np.float64]: ...
@overload
def asmatrix(data: ToObject_nd, dtype: None = None) -> Matrix[np.object_]: ...
@overload
def asmatrix(data: ToComplex128_nd, dtype: None = None) -> Matrix[np.complex128]: ...
@overload
def asmatrix(data: ToBytes_nd, dtype: None = None) -> Matrix[np.bytes_]: ...
@overload
def asmatrix(data: ToStr_nd, dtype: None = None) -> Matrix[np.str_]: ...
@overload
def asmatrix(data: ToGeneric_nd, dtype: DTypeLike | None) -> Matrix: ...
