import abc
import numbers
from collections.abc import Iterator, Mapping, Sequence
from decimal import Decimal
from typing import Any, ClassVar, Final, Generic, Literal, SupportsIndex, TypeAlias, overload
from typing_extensions import LiteralString, Self, TypeIs, TypeVar

import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLikeNumber_co, _FloatLike_co, _NumberLike_co

from ._polytypes import (
    _AnyInt,
    _Array2,
    _ArrayLikeCoefObject_co,
    _ArrayLikeCoef_co,
    _CoefLike_co,
    _CoefSeries,
    _Series,
    _SeriesLikeCoef_co,
    _SeriesLikeInt_co,
    _Tuple2,
)

__all__: Final[Sequence[str]] = ("ABCPolyBase",)

_NameT_co = TypeVar("_NameT_co", bound=LiteralString | None, default=LiteralString | None, covariant=True)
_PolyT = TypeVar("_PolyT", bound=ABCPolyBase)

_AnyOther: TypeAlias = ABCPolyBase | _CoefLike_co | _SeriesLikeCoef_co
_Hundred: TypeAlias = Literal[100]

class ABCPolyBase(abc.ABC, Generic[_NameT_co]):
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]
    __array_ufunc__: ClassVar[None]

    maxpower: ClassVar[_Hundred]
    _superscript_mapping: ClassVar[Mapping[int, str]]
    _subscript_mapping: ClassVar[Mapping[int, str]]
    _use_unicode: ClassVar[bool]

    basis_name: _NameT_co
    coef: _CoefSeries
    domain: _Array2[np.inexact]
    window: _Array2[np.inexact]

    _symbol: LiteralString
    @property
    def symbol(self, /) -> LiteralString: ...

    #
    def __init__(
        self,
        /,
        coef: _SeriesLikeCoef_co,
        domain: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> None: ...

    #
    @overload
    def __call__(self, /, arg: _PolyT) -> _PolyT: ...
    @overload
    def __call__(self, /, arg: _NumberLike_co | numbers.Complex | Decimal | np.object_) -> np.float64 | np.complex128: ...
    @overload
    def __call__(self, /, arg: _ArrayLikeNumber_co) -> npt.NDArray[np.float64 | np.complex128]: ...
    @overload
    def __call__(self, /, arg: _ArrayLikeCoefObject_co) -> npt.NDArray[np.object_]: ...

    #
    def __format__(self, fmt_str: str, /) -> str: ...
    def __eq__(self, x: object, /) -> bool: ...
    def __ne__(self, x: object, /) -> bool: ...
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __add__(self, x: _AnyOther, /) -> Self: ...
    def __sub__(self, x: _AnyOther, /) -> Self: ...
    def __mul__(self, x: _AnyOther, /) -> Self: ...
    def __truediv__(self, x: _AnyOther, /) -> Self: ...
    def __floordiv__(self, x: _AnyOther, /) -> Self: ...
    def __mod__(self, x: _AnyOther, /) -> Self: ...
    def __divmod__(self, x: _AnyOther, /) -> _Tuple2[Self]: ...
    def __pow__(self, x: _AnyOther, /) -> Self: ...
    def __radd__(self, x: _AnyOther, /) -> Self: ...
    def __rsub__(self, x: _AnyOther, /) -> Self: ...
    def __rmul__(self, x: _AnyOther, /) -> Self: ...
    def __rtruediv__(self, x: _AnyOther, /) -> Self: ...
    def __rfloordiv__(self, x: _AnyOther, /) -> Self: ...
    def __rmod__(self, x: _AnyOther, /) -> Self: ...
    def __rdivmod__(self, x: _AnyOther, /) -> _Tuple2[Self]: ...
    def __len__(self, /) -> int: ...
    def __iter__(self, /) -> Iterator[np.inexact | object]: ...
    def __getstate__(self, /) -> dict[str, Any]: ...
    def __setstate__(self, dict: dict[str, Any], /) -> None: ...

    #
    def has_samecoef(self, /, other: ABCPolyBase) -> bool: ...
    def has_samedomain(self, /, other: ABCPolyBase) -> bool: ...
    def has_samewindow(self, /, other: ABCPolyBase) -> bool: ...
    def has_sametype(self, /, other: object) -> TypeIs[Self]: ...

    #
    def copy(self, /) -> Self: ...
    def degree(self, /) -> int: ...
    def cutdeg(self, /) -> Self: ...
    def trim(self, /, tol: _FloatLike_co = ...) -> Self: ...
    def truncate(self, /, size: _AnyInt) -> Self: ...
    @overload
    def convert(
        self,
        /,
        domain: _SeriesLikeCoef_co | None,
        kind: type[_PolyT],
        window: _SeriesLikeCoef_co | None = ...,
    ) -> _PolyT: ...
    @overload
    def convert(
        self,
        /,
        domain: _SeriesLikeCoef_co | None = ...,
        *,
        kind: type[_PolyT],
        window: _SeriesLikeCoef_co | None = ...,
    ) -> _PolyT: ...
    @overload
    def convert(
        self,
        /,
        domain: _SeriesLikeCoef_co | None = ...,
        kind: None = ...,
        window: _SeriesLikeCoef_co | None = ...,
    ) -> Self: ...
    def mapparms(self, /) -> _Tuple2[Any]: ...
    def integ(
        self,
        /,
        m: SupportsIndex = ...,
        k: _CoefLike_co | _SeriesLikeCoef_co = ...,
        lbnd: _CoefLike_co | None = ...,
    ) -> Self: ...
    def deriv(self, /, m: SupportsIndex = ...) -> Self: ...
    def roots(self, /) -> _CoefSeries: ...
    def linspace(
        self,
        /,
        n: SupportsIndex = ...,
        domain: _SeriesLikeCoef_co | None = ...,
    ) -> _Tuple2[_Series[np.float64 | np.complex128]]: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: _SeriesLikeCoef_co,
        y: _SeriesLikeCoef_co,
        deg: int | _SeriesLikeInt_co,
        domain: _SeriesLikeCoef_co | None = ...,
        rcond: _FloatLike_co = ...,
        full: Literal[False] = ...,
        w: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> Self: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: _SeriesLikeCoef_co,
        y: _SeriesLikeCoef_co,
        deg: int | _SeriesLikeInt_co,
        domain: _SeriesLikeCoef_co | None = ...,
        rcond: _FloatLike_co = ...,
        *,
        full: Literal[True],
        w: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: _SeriesLikeCoef_co,
        y: _SeriesLikeCoef_co,
        deg: int | _SeriesLikeInt_co,
        domain: _SeriesLikeCoef_co | None,
        rcond: _FloatLike_co,
        full: Literal[True],
        w: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...
    @classmethod
    def fromroots(
        cls,
        roots: _ArrayLikeCoef_co,
        domain: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> Self: ...
    @classmethod
    def identity(
        cls,
        domain: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> Self: ...
    @classmethod
    def basis(
        cls,
        deg: _AnyInt,
        domain: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
        symbol: str = ...,
    ) -> Self: ...
    @classmethod
    def cast(
        cls,
        series: ABCPolyBase,
        domain: _SeriesLikeCoef_co | None = ...,
        window: _SeriesLikeCoef_co | None = ...,
    ) -> Self: ...
    @classmethod
    def _str_term_unicode(cls, /, i: str, arg_str: str) -> str: ...
    @staticmethod
    def _str_term_ascii(i: str, arg_str: str) -> str: ...
    @staticmethod
    def _repr_latex_term(i: str, arg_str: str, needs_parens: bool) -> str: ...
