import builtins
from collections.abc import Callable
from typing import Any, Literal, TypeAlias, overload
from typing_extensions import TypeVar, override

import numpy as np
import numpy.typing as npt
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _BoolCodes,
    _DTypeLike,
    _DoubleCodes,
    _Float32Codes,
    _Float64Codes,
    _FloatLike_co,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCodes,
    _NestedSequence,
    _ShapeLike,
    _SingleCodes,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCodes,
)
from numpy.random import BitGenerator, RandomState, SeedSequence

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=np.bool | np.integer)

_DTypeLikeFloat32: TypeAlias = _DTypeLike[np.float32] | _Float32Codes | _SingleCodes
_DTypeLikeFloat64: TypeAlias = _DTypeLike[np.float64] | type[float] | _Float64Codes | _DoubleCodes
_DTypeLikeFloat: TypeAlias = _DTypeLikeFloat32 | _DTypeLikeFloat64

_ExpMethod: TypeAlias = Literal["zig", "inv"]

_ToRNG: TypeAlias = (
    int
    | np.integer
    | np.timedelta64
    | NDArray[np.integer | np.timedelta64 | np.flexible | np.object_]
    | _NestedSequence[int]
    | SeedSequence
    | BitGenerator[Any]
    | Generator
    | RandomState
    | None
)

###

class Generator:
    def __init__(self, /, bit_generator: BitGenerator[Any]) -> None: ...
    @override
    def __getstate__(self) -> None: ...
    def __setstate__(self, state: dict[str, Any] | None) -> None: ...
    @override
    def __reduce__(self) -> tuple[Callable[[BitGenerator], Generator], tuple[BitGenerator], None]: ...

    #
    @property
    def bit_generator(self) -> BitGenerator: ...
    def spawn(self, /, n_children: int) -> list[Generator]: ...
    def bytes(self, /, length: int) -> builtins.bytes: ...

    ###
    # resampling

    #
    def shuffle(self, x: ArrayLike, axis: int = 0) -> None: ...

    #
    def permuted(self, x: ArrayLike, *, axis: int | None = None, out: NDArray[Any] | None = None) -> NDArray[Any]: ...

    #
    @overload
    def permutation(self, /, x: int, axis: int = 0) -> npt.NDArray[np.int64]: ...
    @overload
    def permutation(self, /, x: _ArrayLike[_ScalarT], axis: int = 0) -> npt.NDArray[_ScalarT]: ...
    @overload
    def permutation(self, /, x: npt.ArrayLike, axis: int = 0) -> npt.NDArray[Any]: ...

    #
    @overload
    def choice(
        self,
        /,
        a: int,
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> int: ...
    @overload
    def choice(
        self,
        /,
        a: _ArrayLike[_ScalarT],
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> _ScalarT: ...
    @overload
    def choice(
        self,
        /,
        a: npt.ArrayLike,
        size: None = None,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> Any: ...
    @overload
    def choice(
        self,
        /,
        a: int,
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def choice(
        self,
        /,
        a: _ArrayLike[_ScalarT],
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> npt.NDArray[_ScalarT]: ...
    @overload
    def choice(
        self,
        /,
        a: npt.ArrayLike,
        size: _ShapeLike,
        replace: bool = True,
        p: _ArrayLikeFloat_co | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> npt.NDArray[Any]: ...

    ###
    # continuous

    #
    @overload
    def random(self, /, size: None = None, dtype: _DTypeLikeFloat = ..., out: None = None) -> float: ...
    @overload
    def random(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat64 = ...,
        *,
        out: NDArray[np.float64],
    ) -> NDArray[np.float64]: ...
    @overload
    def random(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = None,
    ) -> NDArray[np.float64]: ...
    @overload
    def random(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat32 = ...,
        *,
        out: NDArray[np.float32],
    ) -> NDArray[np.float32]: ...
    @overload
    def random(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat32,
        out: NDArray[np.float32] | None = None,
    ) -> NDArray[np.float32]: ...

    #
    @overload  # size: None  (default)
    def uniform(self, /, low: _FloatLike_co = 0.0, high: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def uniform(
        self, /, low: _ArrayLikeFloat_co, high: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def triangular(
        self, /, left: _FloatLike_co, mode: _FloatLike_co, right: _FloatLike_co, size: None = None
    ) -> float: ...
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
    def beta(self, /, a: _FloatLike_co, b: _FloatLike_co, size: None = None) -> float: ...
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
    @overload
    def standard_exponential(
        self,
        /,
        size: None = None,
        dtype: _DTypeLikeFloat = ...,
        method: _ExpMethod = "zig",
        out: None = None,
    ) -> float: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat64 = ...,
        method: _ExpMethod = "zig",
        *,
        out: NDArray[np.float64],
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat64 = ...,
        method: _ExpMethod = "zig",
        out: NDArray[np.float64] | None = None,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat32 = ...,
        method: _ExpMethod = "zig",
        *,
        out: NDArray[np.float32],
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat32,
        method: _ExpMethod = "zig",
        out: NDArray[np.float32] | None = None,
    ) -> NDArray[np.float32]: ...

    #
    @overload
    def exponential(self, /, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload
    def exponential(self, /, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> NDArray[np.float64]: ...
    @overload
    def exponential(self, /, scale: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> NDArray[np.float64]: ...
    @overload
    def exponential(
        self, /, scale: _ArrayLikeFloat_co = 1.0, size: _ShapeLike | None = None
    ) -> float | NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def laplace(self, /, loc: _FloatLike_co = 0.0, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def laplace(
        self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def logistic(self, /, loc: _FloatLike_co = 0.0, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def logistic(
        self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def power(self, /, a: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def power(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def power(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def pareto(self, /, a: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def pareto(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def pareto(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def gumbel(self, /, loc: _FloatLike_co = 0.0, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gumbel(
        self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def weibull(self, /, a: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def weibull(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def weibull(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def rayleigh(self, /, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def rayleigh(self, /, scale: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def rayleigh(self, /, scale: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def rayleigh(
        self, /, scale: _ArrayLikeFloat_co = 1.0, size: _ShapeLike | None = None
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def chisquare(self, /, df: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def chisquare(self, /, df: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.float64]: ...
    @overload  # fallback
    def chisquare(
        self, /, df: _ArrayLikeFloat_co, size: _ShapeLike | None = None
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload  # size: None  (default)
    def noncentral_chisquare(self, /, df: _FloatLike_co, nonc: _FloatLike_co, size: None = None) -> float: ...
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
    @overload
    def standard_normal(self, /, size: None = None, dtype: _DTypeLikeFloat = ..., out: None = None) -> float: ...
    @overload
    def standard_normal(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat64 = ...,
        *,
        out: NDArray[np.float64],
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_normal(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = None,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_normal(
        self,
        /,
        size: _ShapeLike | None = ...,
        dtype: _DTypeLikeFloat32 = ...,
        *,
        out: NDArray[np.float32],
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_normal(
        self,
        /,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat32,
        out: NDArray[np.float32] | None = None,
    ) -> NDArray[np.float32]: ...

    #
    @overload  # size: None  (default)
    def normal(self, /, loc: _FloatLike_co = 0.0, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def normal(
        self, /, loc: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def lognormal(self, /, mean: _FloatLike_co = 0.0, sigma: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def lognormal(
        self, /, mean: _ArrayLikeFloat_co, sigma: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def vonmises(self, /, mu: _FloatLike_co, kappa: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def vonmises(
        self, /, mu: _ArrayLikeFloat_co, kappa: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def standard_t(
        self, /, df: _ArrayLikeFloat_co, size: _ShapeLike | None = None
    ) -> float | npt.NDArray[np.float64]: ...

    #
    @overload
    def standard_gamma(
        self,
        /,
        shape: _FloatLike_co,
        size: None = None,
        dtype: _DTypeLikeFloat = ...,
        out: None = None,
    ) -> float: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat64 = ...,
        *,
        out: NDArray[np.float64],
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = None,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = None,
    ) -> float | NDArray[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike,
        dtype: _DTypeLikeFloat32,
        out: NDArray[np.float32] | None = None,
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLikeFloat32,
        out: NDArray[np.float32],
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLikeFloat32,
        out: None = None,
    ) -> float | NDArray[np.float32]: ...

    #
    @overload  # size: None  (default)
    def gamma(self, /, shape: _FloatLike_co, scale: _FloatLike_co = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def gamma(
        self, /, shape: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def f(self, /, dfnum: _FloatLike_co, dfden: _FloatLike_co, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def f(
        self, /, dfnum: _ArrayLikeFloat_co, dfden: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    def noncentral_f(
        self,
        /,
        dfnum: _FloatLike_co,
        dfden: _FloatLike_co,
        nonc: _FloatLike_co,
        size: None = None,
    ) -> float: ...
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
    def wald(
        self, /, mean: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.float64]: ...
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
    @overload  # shape: None (default)
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> np.int64: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: type[bool],
        endpoint: bool = False,
    ) -> bool: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: type[int],
        endpoint: bool = False,
    ) -> int: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> _IntegerT: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _BoolCodes,
        endpoint: bool = False,
    ) -> np.bool: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _IntCodes,
        endpoint: bool = False,
    ) -> np.int_: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _UIntCodes,
        endpoint: bool = False,
    ) -> np.uint: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _Int8Codes,
        endpoint: bool = False,
    ) -> np.int8: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _UInt8Codes,
        endpoint: bool = False,
    ) -> np.uint8: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _Int16Codes,
        endpoint: bool = False,
    ) -> np.int16: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _UInt16Codes,
        endpoint: bool = False,
    ) -> np.uint16: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _Int32Codes,
        endpoint: bool = False,
    ) -> np.int32: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _UInt32Codes,
        endpoint: bool = False,
    ) -> np.uint32: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _Int64Codes,
        endpoint: bool = False,
    ) -> np.int64: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _UInt64Codes,
        endpoint: bool = False,
    ) -> np.uint64: ...
    @overload  # size: _ShapeLike (positional)
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> npt.NDArray[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: type[bool] | _BoolCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _IntCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: type[int],
        endpoint: bool = False,
    ) -> npt.NDArray[np.bool | np.int_]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UIntCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int8Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt8Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int16Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt16Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int32Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt32Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _Int64Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co,
        size: _ShapeLike,
        dtype: _UInt64Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint64]: ...
    @overload  # size: _ShapeLike (keyword)
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> npt.NDArray[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: type[bool] | _BoolCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _IntCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int_]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: type[int],
        endpoint: bool = False,
    ) -> npt.NDArray[np.bool | np.int_]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UIntCodes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int8Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt8Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int16Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt16Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int32Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt32Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _Int64Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        *,
        size: _ShapeLike,
        dtype: _UInt64Codes,
        endpoint: bool = False,
    ) -> npt.NDArray[np.uint64]: ...
    @overload  # fallback
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> np.int64 | npt.NDArray[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[bool],
        endpoint: bool = False,
    ) -> bool | npt.NDArray[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[int],
        endpoint: bool = False,
    ) -> int | npt.NDArray[np.bool | np.int_]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> _IntegerT | npt.NDArray[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _BoolCodes,
        endpoint: bool = False,
    ) -> np.bool | npt.NDArray[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _IntCodes,
        endpoint: bool = False,
    ) -> np.int_ | npt.NDArray[np.int_]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UIntCodes,
        endpoint: bool = False,
    ) -> np.uint | npt.NDArray[np.uint]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int8Codes,
        endpoint: bool = False,
    ) -> np.int8 | npt.NDArray[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt8Codes,
        endpoint: bool = False,
    ) -> np.uint8 | npt.NDArray[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int16Codes,
        endpoint: bool = False,
    ) -> np.int16 | npt.NDArray[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt16Codes,
        endpoint: bool = False,
    ) -> np.uint16 | npt.NDArray[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int32Codes,
        endpoint: bool = False,
    ) -> np.int32 | npt.NDArray[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt32Codes,
        endpoint: bool = False,
    ) -> np.uint32 | npt.NDArray[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _Int64Codes,
        endpoint: bool = False,
    ) -> np.int64 | npt.NDArray[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _UInt64Codes,
        endpoint: bool = False,
    ) -> np.uint64 | npt.NDArray[np.uint64]: ...

    #
    @overload  # size: None  (default)
    def binomial(self, /, n: int, p: _FloatLike_co, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def binomial(self, /, n: _ArrayLikeInt_co, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def binomial(
        self,
        /,
        n: _ArrayLikeInt_co,
        p: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def negative_binomial(self, /, n: _FloatLike_co, p: _FloatLike_co, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def negative_binomial(
        self, /, n: _ArrayLikeFloat_co, p: _ArrayLikeFloat_co, size: _ShapeLike
    ) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def negative_binomial(
        self,
        /,
        n: _ArrayLikeFloat_co,
        p: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def poisson(self, /, lam: _FloatLike_co = 1.0, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def poisson(self, /, lam: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # size: (int, ...)  (keyword)
    def poisson(self, /, lam: _ArrayLikeFloat_co = 1.0, *, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def poisson(
        self, /, lam: _ArrayLikeFloat_co = 1.0, size: _ShapeLike | None = None
    ) -> int | npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def zipf(self, /, a: _FloatLike_co, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def zipf(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def zipf(self, /, a: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def geometric(self, /, p: _FloatLike_co, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def geometric(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def geometric(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int64]: ...

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
    ) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def hypergeometric(
        self,
        /,
        ngood: _ArrayLikeInt_co,
        nbad: _ArrayLikeInt_co,
        nsample: _ArrayLikeInt_co,
        size: _ShapeLike | None = None,
    ) -> int | npt.NDArray[np.int64]: ...

    #
    @overload  # size: None  (default)
    def logseries(self, /, p: _FloatLike_co, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def logseries(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike) -> npt.NDArray[np.int64]: ...
    @overload  # fallback
    def logseries(self, /, p: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> int | npt.NDArray[np.int64]: ...

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
        *,
        method: Literal["svd", "eigh", "cholesky"] = "svd",
    ) -> NDArray[np.float64]: ...

    #
    def dirichlet(self, /, alpha: _ArrayLikeFloat_co, size: _ShapeLike | None = None) -> NDArray[np.float64]: ...

    #
    def multinomial(
        self,
        /,
        n: _ArrayLikeInt_co,
        pvals: _ArrayLikeFloat_co,
        size: _ShapeLike | None = None,
    ) -> NDArray[np.int64]: ...

    #
    def multivariate_hypergeometric(
        self,
        colors: _ArrayLikeInt_co,
        nsample: int,
        size: _ShapeLike | None = None,
        method: Literal["marginals", "count"] = "marginals",
    ) -> NDArray[np.int64]: ...

#
def default_rng(seed: _ToRNG = None) -> Generator: ...
