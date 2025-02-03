import builtins
from collections.abc import Callable
from typing import Any, Final, Literal, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
import numpy.typing as npt
from numpy._typing import (
    _ArrayLike,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _BoolCodes,
    _DTypeLike,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCodes,
    _ShapeLike,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCodes,
)
from numpy.random.bit_generator import BitGenerator

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=np.bool | np.integer)

_LegacyState: TypeAlias = tuple[str, npt.NDArray[np.uint32], int, int, float]

###

class RandomState:
    _bit_generator: Final[BitGenerator]

    def __init__(self, /, seed: _ArrayLikeInt_co | BitGenerator[Any] | None = ...) -> None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, /, state: dict[str, Any]) -> None: ...
    def __reduce__(self) -> tuple[Callable[[BitGenerator], RandomState], tuple[BitGenerator], dict[str, Any]]: ...
    @overload
    def get_state(self, /, legacy: Literal[False]) -> dict[str, Any]: ...
    @overload
    def get_state(self, /, legacy: Literal[True] = True) -> _LegacyState: ...
    def set_state(self, /, state: dict[str, Any] | _LegacyState) -> None: ...
    def seed(self, /, seed: _ArrayLikeFloat_co | None = None) -> None: ...
    def bytes(self, /, length: int) -> builtins.bytes: ...

    #
    @overload
    def choice(
        self,
        /,
        a: int,
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> int: ...
    @overload
    def choice(
        self,
        /,
        a: _ArrayLike[_ScalarT],
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> _ScalarT: ...
    @overload
    def choice(
        self,
        /,
        a: npt.ArrayLike,
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> Any: ...
    @overload
    def choice(
        self,
        /,
        a: int,
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def choice(
        self,
        /,
        a: _ArrayLike[_ScalarT],
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> npt.NDArray[_ScalarT]: ...
    @overload
    def choice(
        self,
        /,
        a: npt.ArrayLike,
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
    ) -> npt.NDArray[Any]: ...

    #
    def shuffle(self, /, x: npt.ArrayLike) -> None: ...

    #
    @overload
    def permutation(self, /, x: int) -> npt.NDArray[np.int_]: ...
    @overload
    def permutation(self, /, x: _ArrayLike[_ScalarT]) -> npt.NDArray[_ScalarT]: ...
    @overload
    def permutation(self, /, x: npt.ArrayLike) -> npt.NDArray[Any]: ...

    ###
    # continuous

    #
    @overload
    def rand(self) -> float: ...
    @overload
    def rand(self, arg0: int, /, *args: int) -> npt.NDArray[np.float64]: ...

    #
    @overload
    def randn(self) -> float: ...
    @overload
    def randn(self, arg0: int, /, *args: int) -> npt.NDArray[np.float64]: ...

    #
    @overload
    def random_sample(self, /, size: None = None) -> float: ...
    @overload
    def random_sample(self, /, size: _ShapeLike) -> npt.NDArray[np.float64]: ...

    #
    @overload
    def random(self, /, size: None = None) -> float: ...
    @overload
    def random(self, /, size: _ShapeLike) -> npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def uniform(self, /, low: float = 0.0, high: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def uniform(self, /, low: _ArrayLikeFloat_co, high: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def uniform(
        self,
        /,
        low: _ArrayLikeFloat_co = 0.0,
        high: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def uniform(
        self,
        /,
        low: _ArrayLikeFloat_co = 0.0,
        high: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def triangular(self, /, left: float, mode: float, right: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def triangular(
        self,
        /,
        left: _ArrayLikeFloat_co,
        mode: _ArrayLikeFloat_co,
        right: _ArrayLikeFloat_co,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def triangular(
        self,
        /,
        left: _ArrayLikeFloat_co,
        mode: _ArrayLikeFloat_co,
        right: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def beta(self, /, a: float, b: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def beta(self, /, a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def beta(
        self,
        /,
        a: _ArrayLikeFloat_co,
        b: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_exponential(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_exponential(self, /, size: _ShapeLike) -> npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def exponential(self, /, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def exponential(self, /, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def exponential(self, /, scale: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def exponential(
        self,
        /,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def laplace(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def laplace(self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def laplace(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def laplace(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def logistic(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def logistic(self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def logistic(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def logistic(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def power(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def power(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def power(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def pareto(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def pareto(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def pareto(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def gumbel(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gumbel(self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def gumbel(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def gumbel(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def weibull(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def weibull(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def weibull(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def rayleigh(self, /, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def rayleigh(self, /, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def rayleigh(self, /, scale: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def rayleigh(self, /, scale: _ArrayLikeFloat_co = 1.0, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def chisquare(self, /, df: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def chisquare(self, /, df: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def chisquare(self, /, df: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def noncentral_chisquare(self, /, df: float, nonc: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def noncentral_chisquare(
        self,
        /,
        df: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def noncentral_chisquare(
        self,
        /,
        df: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_normal(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_normal(self, /, size: _ShapeLike) -> npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def normal(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def normal(self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def normal(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def normal(
        self,
        /,
        loc: _ArrayLikeFloat_co = 0.0,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def lognormal(self, /, mean: float = 0.0, sigma: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def lognormal(self, /, mean: _ArrayLikeFloat_co, sigma: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def lognormal(
        self,
        /,
        mean: _ArrayLikeFloat_co = 0.0,
        sigma: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def lognormal(
        self,
        /,
        mean: _ArrayLikeFloat_co = 0.0,
        sigma: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def vonmises(self, /, mu: float, kappa: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def vonmises(self, /, mu: _ArrayLikeFloat_co, kappa: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def vonmises(
        self,
        /,
        mu: _ArrayLikeFloat_co,
        kappa: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_cauchy(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_cauchy(self, /, size: _ShapeLike) -> npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_t(self, /, df: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_t(self, /, df: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def standard_t(self, /, df: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_gamma(self, /, shape: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_gamma(self, /, shape: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def standard_gamma(self, /, shape: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def gamma(self, /, shape: float, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gamma(self, /, shape: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        scale: _ArrayLikeFloat_co = 1.0,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        scale: _ArrayLikeFloat_co = 1.0,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def f(self, /, dfnum: float, dfden: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def f(self, /, dfnum: _ArrayLikeFloat_co, dfden: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def f(
        self,
        /,
        dfnum: _ArrayLikeFloat_co,
        dfden: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def noncentral_f(self, /, dfnum: float, dfden: float, nonc: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def noncentral_f(
        self,
        /,
        dfnum: _ArrayLikeFloat_co,
        dfden: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike,
    ) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def noncentral_f(
        self,
        /,
        dfnum: _ArrayLikeFloat_co,
        dfden: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def wald(self, /, mean: float, scale: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def wald(self, /, mean: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def wald(
        self,
        /,
        mean: _ArrayLikeFloat_co,
        scale: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> float | npt.NDArray[np.float64]: ...

    ###
    # discrete

    #
    @overload
    def tomaxint(self, /, size: None = None) -> int: ...
    @overload  # Generates long values, but stores it in a 64bit int
    def tomaxint(self, /, size: _ShapeLike) -> npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def random_integers(self, /, low: int, high: int | None = None, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def random_integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None,
        size: _ShapeLike,
    ) -> npt.NDArray[np.int_]: ...
    @overload  # size: (int, ...)  (keyword)
    def random_integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def random_integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # shape: None (default)
    def randint(self, /, low: int, high: int | None = None, size: None = None) -> int: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: type[bool]) -> bool: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: type[int]) -> int: ...  # type: ignore[overload-overlap]
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _DTypeLike[_IntegerT]) -> _IntegerT: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _BoolCodes) -> np.bool: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _IntCodes) -> np.int_: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _UIntCodes) -> np.uint: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _Int8Codes) -> np.int8: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _UInt8Codes) -> np.uint8: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _Int16Codes) -> np.int16: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _UInt16Codes) -> np.uint16: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _Int32Codes) -> np.int32: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _UInt32Codes) -> np.uint32: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _Int64Codes) -> np.int64: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _UInt64Codes) -> np.uint64: ...
    @overload  # size: _ShapeLike (positional)
    def randint(self, /, low: _ArrayLikeInt_co, high: _ArrayLikeInt_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _DTypeLike[np.bool] | type[bool] | _BoolCodes,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
    ) -> npt.NDArray[_IntegerT]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _IntCodes,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: type[int],
    ) -> npt.NDArray[np.bool | np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UIntCodes,
    ) -> npt.NDArray[np.uint]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int8Codes,
    ) -> npt.NDArray[np.int8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt8Codes,
    ) -> npt.NDArray[np.uint8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int16Codes,
    ) -> npt.NDArray[np.int16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt16Codes,
    ) -> npt.NDArray[np.uint16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int32Codes,
    ) -> npt.NDArray[np.int32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt32Codes,
    ) -> npt.NDArray[np.uint32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int64Codes,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt64Codes,
    ) -> npt.NDArray[np.uint64]: ...
    @overload  # size: _ShapeLike (keyword)
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
    ) -> npt.NDArray[_IntegerT]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: type[bool] | _BoolCodes,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _IntCodes,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def randint(  # type: ignore[overload-overlap]
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: type[int],
    ) -> npt.NDArray[np.bool | np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UIntCodes,
    ) -> npt.NDArray[np.uint]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int8Codes,
    ) -> npt.NDArray[np.int8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt8Codes,
    ) -> npt.NDArray[np.uint8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int16Codes,
    ) -> npt.NDArray[np.int16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt16Codes,
    ) -> npt.NDArray[np.uint16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int32Codes,
    ) -> npt.NDArray[np.int32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt32Codes,
    ) -> npt.NDArray[np.uint32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int64Codes,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt64Codes,
    ) -> npt.NDArray[np.uint64]: ...
    @overload  # fallback
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[bool],
    ) -> bool | npt.NDArray[np.bool]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[int],
    ) -> int | npt.NDArray[np.bool | np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLike[_IntegerT],
    ) -> _IntegerT | npt.NDArray[_IntegerT]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _BoolCodes,
    ) -> np.bool | npt.NDArray[np.bool]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _IntCodes,
    ) -> np.int_ | npt.NDArray[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UIntCodes,
    ) -> np.uint | npt.NDArray[np.uint]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int8Codes,
    ) -> np.int8 | npt.NDArray[np.int8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt8Codes,
    ) -> np.uint8 | npt.NDArray[np.uint8]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int16Codes,
    ) -> np.int16 | npt.NDArray[np.int16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt16Codes,
    ) -> np.uint16 | npt.NDArray[np.uint16]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int32Codes,
    ) -> np.int32 | npt.NDArray[np.int32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt32Codes,
    ) -> np.uint32 | npt.NDArray[np.uint32]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int64Codes,
    ) -> np.int64 | npt.NDArray[np.int64]: ...
    @overload
    def randint(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt64Codes,
    ) -> np.uint64 | npt.NDArray[np.uint64]: ...

    #
    @overload  # size: None  (default)
    def binomial(self, /, n: int, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def binomial(self, /, n: _ArrayLikeInt_co, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def binomial(
        self,
        /,
        n: _ArrayLikeInt_co,
        p: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def negative_binomial(self, /, n: float, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def negative_binomial(self, /, n: _ArrayLikeFloat_co, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def negative_binomial(
        self,
        /,
        n: _ArrayLikeFloat_co,
        p: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def poisson(self, /, lam: float = 1.0, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def poisson(self, /, lam: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # size: (int, ...)  (keyword)
    def poisson(self, /, lam: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def poisson(self, /, lam: _ArrayLikeFloat_co = 1.0, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def zipf(self, /, a: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def zipf(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def zipf(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def geometric(self, /, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def geometric(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def geometric(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def hypergeometric(self, /, ngood: int, nbad: int, nsample: int, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def hypergeometric(
        self,
        /,
        ngood: _ArrayLikeInt_co,
        nbad: _ArrayLikeInt_co,
        nsample: _ArrayLikeInt_co,
        size: _ShapeLike,
    ) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def hypergeometric(
        self,
        /,
        ngood: _ArrayLikeInt_co,
        nbad: _ArrayLikeInt_co,
        nsample: _ArrayLikeInt_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int_]: ...

    #
    @overload  # size: None  (default)
    def logseries(self, /, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def logseries(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int_]: ...
    @overload  # fallback
    def logseries(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int_]: ...

    ###
    # multivariate

    #
    def multivariate_normal(
        self,
        /,
        mean: _ArrayLikeFloat_co,
        cov: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
        check_valid: Literal["warn", "raise", "ignore"] = "warn",
        tol: float = 1e-8,
    ) -> npt.NDArray[np.float64]: ...

    #
    def dirichlet(self, /, alpha: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> npt.NDArray[np.float64]: ...

    #
    def multinomial(
        self,
        /,
        n: _ArrayLikeInt_co,
        pvals: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> npt.NDArray[np.int_]: ...

###

_rand: RandomState

beta = _rand.beta
binomial = _rand.binomial
bytes = _rand.bytes
chisquare = _rand.chisquare
choice = _rand.choice
dirichlet = _rand.dirichlet
exponential = _rand.exponential
f = _rand.f
gamma = _rand.gamma
get_state = _rand.get_state
geometric = _rand.geometric
gumbel = _rand.gumbel
hypergeometric = _rand.hypergeometric
laplace = _rand.laplace
logistic = _rand.logistic
lognormal = _rand.lognormal
logseries = _rand.logseries
multinomial = _rand.multinomial
multivariate_normal = _rand.multivariate_normal
negative_binomial = _rand.negative_binomial
noncentral_chisquare = _rand.noncentral_chisquare
noncentral_f = _rand.noncentral_f
normal = _rand.normal
pareto = _rand.pareto
permutation = _rand.permutation
poisson = _rand.poisson
power = _rand.power
rand = _rand.rand
randint = _rand.randint
randn = _rand.randn
random = _rand.random
random_integers = _rand.random_integers
random_sample = _rand.random_sample
rayleigh = _rand.rayleigh
seed = _rand.seed
set_state = _rand.set_state
shuffle = _rand.shuffle
standard_cauchy = _rand.standard_cauchy
standard_exponential = _rand.standard_exponential
standard_gamma = _rand.standard_gamma
standard_normal = _rand.standard_normal
standard_t = _rand.standard_t
triangular = _rand.triangular
uniform = _rand.uniform
vonmises = _rand.vonmises
wald = _rand.wald
weibull = _rand.weibull
zipf = _rand.zipf
# Two legacy that are trivial wrappers around random_sample
sample = _rand.random_sample
ranf = _rand.random_sample

def set_bit_generator(bitgen: BitGenerator[Any]) -> None: ...
def get_bit_generator() -> BitGenerator: ...
