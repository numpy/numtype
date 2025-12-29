import builtins
from collections.abc import Callable
from typing import Any, Final, Literal, TypeAlias, overload
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLike, _BoolCodes, _DTypeLike, _ShapeLike
from numpy.random.bit_generator import BitGenerator

__all__ = [
    "RandomState",
    "beta",
    "binomial",
    "bytes",
    "chisquare",
    "choice",
    "dirichlet",
    "exponential",
    "f",
    "gamma",
    "geometric",
    "get_bit_generator",
    "get_state",
    "gumbel",
    "hypergeometric",
    "laplace",
    "logistic",
    "lognormal",
    "logseries",
    "multinomial",
    "multivariate_normal",
    "negative_binomial",
    "noncentral_chisquare",
    "noncentral_f",
    "normal",
    "pareto",
    "permutation",
    "poisson",
    "power",
    "rand",
    "randint",
    "randn",
    "random",
    "random_integers",
    "random_sample",
    "ranf",
    "rayleigh",
    "sample",
    "seed",
    "set_bit_generator",
    "set_state",
    "shuffle",
    "standard_cauchy",
    "standard_exponential",
    "standard_gamma",
    "standard_normal",
    "standard_t",
    "triangular",
    "uniform",
    "vonmises",
    "wald",
    "weibull",
    "zipf",
]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=np.bool | np.integer)

_LegacyState: TypeAlias = tuple[str, _nt.Array[np.uint32], int, int, float]

###

class RandomState:
    _bit_generator: Final[BitGenerator]

    def __init__(self, /, seed: _nt.CoInteger_nd | BitGenerator[Any] | None = None) -> None: ...
    @override
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, /, state: dict[str, Any]) -> None: ...
    @override
    def __reduce__(self) -> tuple[Callable[[BitGenerator], RandomState], tuple[BitGenerator], dict[str, Any]]: ...

    #
    @overload
    def get_state(self, /, legacy: Literal[False]) -> dict[str, Any]: ...
    @overload
    def get_state(self, /, legacy: Literal[True] = True) -> _LegacyState: ...
    def set_state(self, /, state: dict[str, Any] | _LegacyState) -> None: ...
    def seed(self, /, seed: _nt.CoFloating_nd | None = None) -> None: ...
    def bytes(self, /, length: int) -> builtins.bytes: ...

    #
    @overload
    def choice(self, /, a: int, size: None = None, replace: bool = True, p: _nt.CoFloating_nd | None = None) -> int: ...
    @overload
    def choice(
        self, /, a: _ArrayLike[_ScalarT], size: None = None, replace: bool = True, p: _nt.CoFloating_nd | None = None
    ) -> _ScalarT: ...
    @overload
    def choice(
        self, /, a: npt.ArrayLike, size: None = None, replace: bool = True, p: _nt.CoFloating_nd | None = None
    ) -> Any: ...
    @overload
    def choice(
        self, /, a: int, size: _ShapeLike, replace: bool = True, p: _nt.CoFloating_nd | None = None
    ) -> _nt.Array[np.int_]: ...
    @overload
    def choice(
        self, /, a: _ArrayLike[_ScalarT], size: _ShapeLike, replace: bool = True, p: _nt.CoFloating_nd | None = None
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def choice(
        self, /, a: npt.ArrayLike, size: _ShapeLike, replace: bool = True, p: _nt.CoFloating_nd | None = None
    ) -> _nt.Array[Any]: ...

    #
    def shuffle(self, /, x: npt.ArrayLike) -> None: ...

    #
    @overload
    def permutation(self, /, x: int) -> _nt.Array[np.int_]: ...
    @overload
    def permutation(self, /, x: _ArrayLike[_ScalarT]) -> _nt.Array[_ScalarT]: ...
    @overload
    def permutation(self, /, x: npt.ArrayLike) -> _nt.Array[Any]: ...

    ###
    # continuous

    #
    @overload
    def rand(self) -> float: ...
    @overload
    def rand(self, arg0: int, /, *args: int) -> _nt.Array[np.float64]: ...

    #
    @overload
    def randn(self) -> float: ...
    @overload
    def randn(self, arg0: int, /, *args: int) -> _nt.Array[np.float64]: ...

    #
    @overload
    def random_sample(self, /, size: None = None) -> float: ...
    @overload
    def random_sample(self, /, size: _ShapeLike) -> _nt.Array[np.float64]: ...

    #
    @overload
    def random(self, /, size: None = None) -> float: ...
    @overload
    def random(self, /, size: _ShapeLike) -> _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def uniform(self, /, low: float = 0.0, high: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def uniform(
        self, /, low: _nt.CoFloating_nd, high: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def uniform(
        self, /, low: _nt.CoFloating_nd = 0.0, high: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def uniform(
        self, /, low: _nt.CoFloating_nd = 0.0, high: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def triangular(self, /, left: float, mode: float, right: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def triangular(
        self, /, left: _nt.CoFloating_nd, mode: _nt.CoFloating_nd, right: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def triangular(
        self,
        /,
        left: _nt.CoFloating_nd,
        mode: _nt.CoFloating_nd,
        right: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def beta(self, /, a: float, b: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def beta(self, /, a: _nt.CoFloating_nd, b: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def beta(
        self, /, a: _nt.CoFloating_nd, b: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_exponential(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_exponential(self, /, size: _ShapeLike) -> _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def exponential(self, /, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def exponential(self, /, scale: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def exponential(self, /, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def exponential(
        self, /, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def laplace(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def laplace(
        self, /, loc: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def laplace(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def laplace(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def logistic(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def logistic(
        self, /, loc: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def logistic(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def logistic(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def power(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def power(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def power(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def pareto(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def pareto(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def pareto(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def gumbel(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gumbel(
        self, /, loc: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def gumbel(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def gumbel(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def weibull(self, /, a: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def weibull(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def weibull(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def rayleigh(self, /, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def rayleigh(self, /, scale: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def rayleigh(self, /, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def rayleigh(
        self, /, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def chisquare(self, /, df: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def chisquare(self, /, df: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def chisquare(self, /, df: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def noncentral_chisquare(self, /, df: float, nonc: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def noncentral_chisquare(
        self, /, df: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def noncentral_chisquare(
        self, /, df: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_normal(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_normal(self, /, size: _ShapeLike) -> _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def normal(self, /, loc: float = 0.0, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def normal(
        self, /, loc: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def normal(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def normal(
        self, /, loc: _nt.CoFloating_nd = 0.0, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def lognormal(self, /, mean: float = 0.0, sigma: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def lognormal(
        self, /, mean: _nt.CoFloating_nd, sigma: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def lognormal(
        self, /, mean: _nt.CoFloating_nd = 0.0, sigma: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def lognormal(
        self, /, mean: _nt.CoFloating_nd = 0.0, sigma: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def vonmises(self, /, mu: float, kappa: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def vonmises(
        self, /, mu: _nt.CoFloating_nd, kappa: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def vonmises(
        self, /, mu: _nt.CoFloating_nd, kappa: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_cauchy(self, /, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_cauchy(self, /, size: _ShapeLike) -> _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_t(self, /, df: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_t(self, /, df: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def standard_t(self, /, df: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def standard_gamma(self, /, shape: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_gamma(self, /, shape: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def standard_gamma(
        self, /, shape: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def gamma(self, /, shape: float, scale: float = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gamma(
        self, /, shape: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def gamma(
        self, /, shape: _nt.CoFloating_nd, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def gamma(
        self, /, shape: _nt.CoFloating_nd, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def f(self, /, dfnum: float, dfden: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def f(self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def noncentral_f(self, /, dfnum: float, dfden: float, nonc: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def noncentral_f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def noncentral_f(
        self,
        /,
        dfnum: _nt.CoFloating_nd,
        dfden: _nt.CoFloating_nd,
        nonc: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # size: None  (default)
    def wald(self, /, mean: float, scale: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def wald(self, /, mean: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def wald(
        self, /, mean: _nt.CoFloating_nd, scale: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    ###
    # discrete

    #
    @overload
    def tomaxint(self, /, size: None = None) -> int: ...
    @overload  # Generates long values, but stores it in a 64bit int
    def tomaxint(self, /, size: _ShapeLike) -> _nt.Array[np.int64]: ...

    #
    @overload  # size: None  (default)
    def random_integers(self, /, low: int, high: int | None = None, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def random_integers(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd | None, size: _ShapeLike
    ) -> _nt.Array[np.int_]: ...
    @overload  # size: (int, ...)  (keyword)
    def random_integers(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd | None = None, *, size: _ShapeLike
    ) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def random_integers(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd | None = None, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # shape: None (default)
    def randint(self, /, low: int, high: int | None = None, size: None = None) -> int: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: type[bool]) -> bool: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: type[_nt.JustInt]) -> int: ...
    @overload
    def randint(  # type: ignore[overload-overlap]
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _DTypeLike[_IntegerT]
    ) -> _IntegerT: ...
    @overload
    def randint(self, /, low: int, high: int | None = None, size: None = None, *, dtype: _BoolCodes) -> np.bool: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeInt8
    ) -> np.int8: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeUInt8
    ) -> np.uint8: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeInt16
    ) -> np.int16: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeUInt16
    ) -> np.uint16: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeInt32
    ) -> np.int32: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeUInt32
    ) -> np.uint32: ...
    @overload
    def randint(  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeInt64
    ) -> int | np.int64: ...
    @overload
    def randint(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeUInt64
    ) -> np.uint64: ...
    @overload  # size: _ShapeLike (positional)
    def randint(self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeBool
    ) -> _nt.Array[np.bool]: ...
    @overload
    def randint(  # type: ignore[overload-overlap]
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _DTypeLike[_IntegerT]
    ) -> _nt.Array[_IntegerT]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeInt8
    ) -> _nt.Array[np.int8]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeUInt8
    ) -> _nt.Array[np.uint8]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeInt16
    ) -> _nt.Array[np.int16]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeUInt16
    ) -> _nt.Array[np.uint16]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeInt32
    ) -> _nt.Array[np.int32]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeUInt32
    ) -> _nt.Array[np.uint32]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeInt64
    ) -> _nt.Array[np.int64]: ...
    @overload
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd, size: _ShapeLike, dtype: _nt.ToDTypeUInt64
    ) -> _nt.Array[np.uint64]: ...
    @overload  # size: _ShapeLike (keyword)
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd | None = None, *, size: _ShapeLike
    ) -> _nt.Array[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeBool,
    ) -> _nt.Array[np.bool]: ...
    @overload
    def randint(  # type: ignore[overload-overlap]
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
    ) -> _nt.Array[_IntegerT]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt8,
    ) -> _nt.Array[np.int8]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt8,
    ) -> _nt.Array[np.uint8]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt16,
    ) -> _nt.Array[np.int16]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt16,
    ) -> _nt.Array[np.uint16]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt32,
    ) -> _nt.Array[np.int32]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt32,
    ) -> _nt.Array[np.uint32]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt64,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt64,
    ) -> _nt.Array[np.uint64]: ...
    @overload  # fallback
    def randint(
        self, /, low: _nt.CoInteger_nd, high: _nt.CoInteger_nd | None = None, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int_]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[bool],
    ) -> bool | _nt.Array[np.bool]: ...
    @overload
    def randint(  # type: ignore[overload-overlap]
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLike[_IntegerT],
    ) -> _IntegerT | _nt.Array[_IntegerT]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _BoolCodes,
    ) -> np.bool | _nt.Array[np.bool]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt8,
    ) -> np.int8 | _nt.Array[np.int8]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt8,
    ) -> np.uint8 | _nt.Array[np.uint8]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt16,
    ) -> np.int16 | _nt.Array[np.int16]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt16,
    ) -> np.uint16 | _nt.Array[np.uint16]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt32,
    ) -> np.int32 | _nt.Array[np.int32]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt32,
    ) -> np.uint32 | _nt.Array[np.uint32]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt64,
    ) -> int | np.int64 | _nt.Array[np.int64]: ...
    @overload
    def randint(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt64,
    ) -> np.uint64 | _nt.Array[np.uint64]: ...

    #
    @overload  # size: None  (default)
    def binomial(self, /, n: int, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def binomial(self, /, n: _nt.CoInteger_nd, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def binomial(
        self, /, n: _nt.CoInteger_nd, p: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def negative_binomial(self, /, n: float, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def negative_binomial(
        self, /, n: _nt.CoFloating_nd, p: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def negative_binomial(
        self, /, n: _nt.CoFloating_nd, p: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def poisson(self, /, lam: float = 1.0, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def poisson(self, /, lam: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # size: (int, ...)  (keyword)
    def poisson(self, /, lam: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def poisson(self, /, lam: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def zipf(self, /, a: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def zipf(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def zipf(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def geometric(self, /, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def geometric(self, /, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def geometric(self, /, p: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def hypergeometric(self, /, ngood: int, nbad: int, nsample: int, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def hypergeometric(
        self, /, ngood: _nt.CoInteger_nd, nbad: _nt.CoInteger_nd, nsample: _nt.CoInteger_nd, size: _ShapeLike
    ) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def hypergeometric(
        self,
        /,
        ngood: _nt.CoInteger_nd,
        nbad: _nt.CoInteger_nd,
        nsample: _nt.CoInteger_nd,
        size: _ShapeLike | None = None,
    ) -> int | _nt.Array[np.int_]: ...

    #
    @overload  # size: None  (default)
    def logseries(self, /, p: float, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def logseries(self, /, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int_]: ...
    @overload  # fallback
    def logseries(self, /, p: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int_]: ...

    ###
    # multivariate

    #
    def multivariate_normal(
        self,
        /,
        mean: _nt.CoFloating_nd,
        cov: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
        check_valid: Literal["warn", "raise", "ignore"] = "warn",
        tol: float = 1e-8,
    ) -> _nt.Array[np.float64]: ...

    #
    def dirichlet(self, /, alpha: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> _nt.Array[np.float64]: ...

    #
    def multinomial(
        self, /, n: _nt.CoInteger_nd, pvals: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> _nt.Array[np.int_]: ...

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
