import abc
import sys
from collections.abc import Iterator, Mapping, Sequence
from typing import Any, ClassVar, Final, Literal, SupportsIndex, TypeAlias, overload
from typing_extensions import Self, TypeIs, TypeVar, override

import numpy as np
import numpy.typing as npt
from _numtype import (
    Array1D,
    CoComplex_0d,
    CoComplex_1d,
    CoComplex_1nd,
    CoInteger_0d,
    CoInteger_1d,
    ToObject_0d,
    ToObject_1nd,
)
from numpy._typing import _FloatLike_co

from .polynomial import _ToNumeric_0d, _ToNumeric_nd

__all__: Final[Sequence[str]] = ("ABCPolyBase",)

###

_PolyT = TypeVar("_PolyT", bound=ABCPolyBase)

_AnyOther: TypeAlias = ABCPolyBase | _ToNumeric_0d | CoComplex_1d
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

    coef: Array1D[np.inexact | np.object_]

    @property
    def symbol(self, /) -> str: ...

    #
    @property
    @abc.abstractmethod
    def basis_name(self, /) -> str | None: ...
    @property
    @abc.abstractmethod
    def domain(self, /) -> Array1D[np.inexact]: ...
    @property
    @abc.abstractmethod
    def window(self, /) -> Array1D[np.inexact]: ...

    #
    def __init__(
        self,
        /,
        coef: CoComplex_1d,
        domain: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> None: ...

    #
    @overload
    def __call__(self, /, arg: _PolyT) -> _PolyT: ...
    @overload
    def __call__(self, /, arg: CoComplex_0d) -> np.float64 | np.complex128: ...
    @overload
    def __call__(self, /, arg: CoComplex_1nd) -> npt.NDArray[np.float64 | np.complex128]: ...
    @overload
    def __call__(self, /, arg: ToObject_0d) -> Any: ...
    @overload
    def __call__(self, /, arg: ToObject_1nd) -> npt.NDArray[np.object_]: ...

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

    if sys.version_info >= (3, 11):
        @override
        def __getstate__(self, /) -> dict[str, Any]: ...

    else:
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
    def trim(self, /, tol: _FloatLike_co = 0) -> Self: ...
    def truncate(self, /, size: SupportsIndex) -> Self: ...

    #
    @overload
    def convert(
        self, /, domain: CoComplex_1d | None = None, kind: None = None, window: CoComplex_1d | None = None
    ) -> Self: ...
    @overload
    def convert(
        self, /, domain: CoComplex_1d | None, kind: type[_PolyT], window: CoComplex_1d | None = None
    ) -> _PolyT: ...
    @overload
    def convert(
        self,
        /,
        domain: CoComplex_1d | None = None,
        *,
        kind: type[_PolyT],
        window: CoComplex_1d | None = None,
    ) -> _PolyT: ...

    #
    def mapparms(self, /) -> tuple[Any, Any]: ...
    def integ(
        self, /, m: SupportsIndex = 1, k: _ToNumeric_0d | CoComplex_1d = [], lbnd: _ToNumeric_0d | None = None
    ) -> Self: ...
    def deriv(self, /, m: SupportsIndex = 1) -> Self: ...
    def roots(self, /) -> Array1D[np.float64] | Array1D[np.complex128]: ...
    def linspace(
        self,
        /,
        n: SupportsIndex = 100,
        domain: CoComplex_1d | None = None,
    ) -> tuple[Array1D[np.float64 | np.complex128], Array1D[np.float64 | np.complex128]]: ...

    #
    @overload
    @classmethod
    def fit(
        cls,
        x: CoComplex_1d,
        y: CoComplex_1d,
        deg: CoInteger_0d | CoInteger_1d,
        domain: CoComplex_1d | None = None,
        rcond: _FloatLike_co | None = None,
        full: Literal[False] = False,
        w: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: CoComplex_1d,
        y: CoComplex_1d,
        deg: CoInteger_0d | CoInteger_1d,
        domain: CoComplex_1d | None,
        rcond: _FloatLike_co | None,
        full: Literal[True],
        w: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...
    @overload
    @classmethod
    def fit(
        cls,
        x: CoComplex_1d,
        y: CoComplex_1d,
        deg: CoInteger_0d | CoInteger_1d,
        domain: CoComplex_1d | None = None,
        rcond: _FloatLike_co | None = None,
        *,
        full: Literal[True],
        w: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> tuple[Self, Sequence[np.inexact | np.int32]]: ...

    #
    @classmethod
    def fromroots(
        cls,
        roots: _ToNumeric_nd,
        domain: CoComplex_1d | None = [],
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @classmethod
    def identity(
        cls,
        domain: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @classmethod
    def basis(
        cls,
        deg: SupportsIndex,
        domain: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
        symbol: str = "x",
    ) -> Self: ...
    @classmethod
    def cast(
        cls,
        series: ABCPolyBase,
        domain: CoComplex_1d | None = None,
        window: CoComplex_1d | None = None,
    ) -> Self: ...

    #
    @classmethod
    def _str_term_unicode(cls, /, i: str, arg_str: str) -> str: ...
    @classmethod
    def _str_term_ascii(cls, i: str, arg_str: str) -> str: ...
    @classmethod
    def _repr_latex_term(cls, i: str, arg_str: str, needs_parens: bool) -> str: ...
