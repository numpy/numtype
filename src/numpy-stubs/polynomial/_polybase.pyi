import abc
from collections.abc import Iterator, Mapping, Sequence
from typing import Any, ClassVar, Literal, Self, SupportsIndex, TypeAlias, overload
from typing_extensions import TypeIs, TypeVar, override

import _numtype as _nt
import numpy as np

from .polynomial import _ToNumeric_0d, _ToNumeric_nd

__all__ = ["ABCPolyBase"]

###

_T = TypeVar("_T")
_PolyT = TypeVar("_PolyT", bound=ABCPolyBase)

_Tuple2: TypeAlias = tuple[_T, _T]
_AnyOther: TypeAlias = ABCPolyBase | _ToNumeric_0d | _nt.CoComplex_1d
_Hundred: TypeAlias = Literal[100]

###

class ABCPolyBase(abc.ABC):
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]
    __array_ufunc__: ClassVar[None]

    maxpower: ClassVar[_Hundred]
    _superscript_mapping: ClassVar[Mapping[int, str]]
    _subscript_mapping: ClassVar[Mapping[int, str]]
    _use_unicode: ClassVar[bool]
    _symbol: str

    coef: _nt.Array1D[np.inexact | np.object_]

    @property
    def symbol(self, /) -> str: ...

    #
    @property
    @abc.abstractmethod
    def basis_name(self, /) -> str | None: ...
    @property
    @abc.abstractmethod
    def domain(self, /) -> _nt.Array1D[np.inexact]: ...
    @property
    @abc.abstractmethod
    def window(self, /) -> _nt.Array1D[np.inexact]: ...

    #
    def __init__(
        self,
        /,
        coef: _nt.CoComplex_1d,
        domain: _nt.CoComplex_1d | None = None,
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> None: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def __call__(self, /, arg: _PolyT) -> _PolyT: ...
    @overload
    def __call__(self, /, arg: _nt._ToArray_nnd[_nt.co_complex]) -> _nt.Array[_nt.inexact64]: ...
    @overload
    def __call__(self, /, arg: _nt.CoComplex_0d) -> _nt.inexact64: ...
    @overload
    def __call__(self, /, arg: _nt.CoComplex_1nd) -> _nt.Array[_nt.inexact64]: ...
    @overload
    def __call__(self, /, arg: _nt.ToObject_1nd) -> _nt.Array[np.object_]: ...
    @overload
    def __call__(self, /, arg: _nt.ToObject_nd) -> Any: ...

    #
    @override
    def __format__(self, fmt_str: str, /) -> str: ...
    @override
    def __eq__(self, x: object, /) -> bool: ...
    @override
    def __ne__(self, x: object, /) -> bool: ...
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __add__(self, x: _AnyOther, /) -> Self: ...
    def __sub__(self, x: _AnyOther, /) -> Self: ...
    def __mul__(self, x: _AnyOther, /) -> Self: ...
    def __truediv__(self, x: _AnyOther, /) -> Self: ...
    def __floordiv__(self, x: _AnyOther, /) -> Self: ...
    def __mod__(self, x: _AnyOther, /) -> Self: ...
    def __divmod__(self, x: _AnyOther, /) -> tuple[Self, Self]: ...
    def __pow__(self, x: _AnyOther, /) -> Self: ...
    def __radd__(self, x: _AnyOther, /) -> Self: ...
    def __rsub__(self, x: _AnyOther, /) -> Self: ...
    def __rmul__(self, x: _AnyOther, /) -> Self: ...
    def __rtruediv__(self, x: _AnyOther, /) -> Self: ...
    def __rfloordiv__(self, x: _AnyOther, /) -> Self: ...
    def __rdiv__(self, x: _AnyOther, /) -> Self: ...
    def __rmod__(self, x: _AnyOther, /) -> Self: ...
    def __rdivmod__(self, x: _AnyOther, /) -> tuple[Self, Self]: ...
    def __len__(self, /) -> int: ...
    def __iter__(self, /) -> Iterator[np.inexact | object]: ...
    @override
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
    def cutdeg(self, /, deg: int) -> Self: ...
    def trim(self, /, tol: _nt.CoFloating_nd = 0) -> Self: ...
    def truncate(self, /, size: SupportsIndex) -> Self: ...

    #
    @overload
    def convert(
        self, /, domain: _nt.CoComplex_1d | None = None, kind: None = None, window: _nt.CoComplex_1d | None = None
    ) -> Self: ...
    @overload
    def convert(
        self, /, domain: _nt.CoComplex_1d | None, kind: type[_PolyT], window: _nt.CoComplex_1d | None = None
    ) -> _PolyT: ...
    @overload
    def convert(
        self, /, domain: _nt.CoComplex_1d | None = None, *, kind: type[_PolyT], window: _nt.CoComplex_1d | None = None
    ) -> _PolyT: ...

    #
    def mapparms(self, /) -> tuple[Any, Any]: ...
    def integ(
        self, /, m: SupportsIndex = 1, k: _ToNumeric_0d | _nt.CoComplex_1d = [], lbnd: _ToNumeric_0d | None = None
    ) -> Self: ...
    def deriv(self, /, m: SupportsIndex = 1) -> Self: ...
    def roots(self, /) -> _nt.Array1D[_nt.inexact64]: ...
    def linspace(
        self, /, n: SupportsIndex = 100, domain: _nt.CoComplex_1d | None = None
    ) -> _Tuple2[_nt.Array1D[_nt.inexact64]]: ...

    #
    @overload
    @classmethod
    def fit(
        cls,
        x: _nt.CoComplex_1d,
        y: _nt.CoComplex_1d,
        deg: _nt.CoInteger_0d | _nt.CoInteger_1d,
        domain: _nt.CoComplex_1d | None = None,
        rcond: _nt.CoFloating_nd | None = None,
        full: Literal[False] = False,
        w: _nt.CoComplex_1d | None = None,
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: _nt.CoComplex_1d,
        y: _nt.CoComplex_1d,
        deg: _nt.CoInteger_0d | _nt.CoInteger_1d,
        domain: _nt.CoComplex_1d | None,
        rcond: _nt.CoFloating_nd | None,
        full: Literal[True],
        w: _nt.CoComplex_1d | None = None,
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: _nt.CoComplex_1d,
        y: _nt.CoComplex_1d,
        deg: _nt.CoInteger_0d | _nt.CoInteger_1d,
        domain: _nt.CoComplex_1d | None = None,
        rcond: _nt.CoFloating_nd | None = None,
        *,
        full: Literal[True],
        w: _nt.CoComplex_1d | None = None,
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...

    #
    @classmethod
    def fromroots(
        cls,
        roots: _ToNumeric_nd,
        domain: _nt.CoComplex_1d | None = [],
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @classmethod
    def identity(
        cls, domain: _nt.CoComplex_1d | None = None, window: _nt.CoComplex_1d | None = None, symbol: str = "x"
    ) -> Self: ...
    @classmethod
    def basis(
        cls,
        deg: SupportsIndex,
        domain: _nt.CoComplex_1d | None = None,
        window: _nt.CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @classmethod
    def cast(
        cls, series: ABCPolyBase, domain: _nt.CoComplex_1d | None = None, window: _nt.CoComplex_1d | None = None
    ) -> Self: ...

    #
    @classmethod
    def _str_term_unicode(cls, /, i: str, arg_str: str) -> str: ...
    @classmethod
    def _str_term_ascii(cls, i: str, arg_str: str) -> str: ...
    @classmethod
    def _repr_latex_term(cls, i: str, arg_str: str, needs_parens: bool) -> str: ...
