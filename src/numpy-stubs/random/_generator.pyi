from collections.abc import Callable
from typing import Any, Literal, TypeAlias, overload

import numpy as np
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _DTypeLike,
    _DTypeLikeBool,
    _DoubleCodes,
    _Float32Codes,
    _Float64Codes,
    _FloatLike_co,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCodes,
    _ShapeLike,
    _SingleCodes,
    _SupportsDType,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCodes,
)
from numpy.random import BitGenerator, RandomState, SeedSequence

_DTypeLikeFloat32: TypeAlias = _DTypeLike[np.float32] | _Float32Codes | _SingleCodes
_DTypeLikeFloat64: TypeAlias = _DTypeLike[np.float64] | type[float] | _Float64Codes | _DoubleCodes

class Generator:
    def __init__(self, bit_generator: BitGenerator) -> None: ...
    def __getstate__(self) -> None: ...
    def __setstate__(self, state: dict[str, Any] | None) -> None: ...
    def __reduce__(self) -> tuple[Callable[[BitGenerator], Generator], tuple[BitGenerator], None]: ...
    @property
    def bit_generator(self) -> BitGenerator: ...
    def spawn(self, n_children: int) -> list[Generator]: ...
    def bytes(self, length: int) -> bytes: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: _DTypeLikeFloat32 | _DTypeLikeFloat64 = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: _ShapeLike = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        *,
        out: NDArray[np.float64] = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat32 = ...,
        out: NDArray[np.float32] | None = ...,
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_normal(  # type: ignore[misc]
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def permutation(self, x: int, axis: int = ...) -> NDArray[np.int64]: ...
    @overload
    def permutation(self, x: ArrayLike, axis: int = ...) -> NDArray[Any]: ...
    @overload
    def standard_exponential(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: _DTypeLikeFloat32 | _DTypeLikeFloat64 = ...,
        method: Literal["zig", "inv"] = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_exponential(
        self,
        size: _ShapeLike = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        *,
        out: NDArray[np.float64] = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        size: _ShapeLike = ...,
        *,
        method: Literal["zig", "inv"] = ...,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat32 = ...,
        method: Literal["zig", "inv"] = ...,
        out: NDArray[np.float32] | None = ...,
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_exponential(
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat64 = ...,
        method: Literal["zig", "inv"] = ...,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def random(  # type: ignore[misc]
        self,
        size: None = ...,
        dtype: _DTypeLikeFloat32 | _DTypeLikeFloat64 = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def random(
        self,
        *,
        out: NDArray[np.float64] = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def random(
        self,
        size: _ShapeLike = ...,
        *,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def random(
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat32 = ...,
        out: NDArray[np.float32] | None = ...,
    ) -> NDArray[np.float32]: ...
    @overload
    def random(
        self,
        size: _ShapeLike = ...,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def beta(
        self,
        a: _FloatLike_co,
        b: _FloatLike_co,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def beta(self, a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def exponential(self, scale: _FloatLike_co = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def exponential(self, scale: _ArrayLikeFloat_co = ..., size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        *,
        endpoint: bool = ...,
    ) -> int: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: type[bool] = ...,
        endpoint: bool = ...,
    ) -> bool: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: type[np.bool] = ...,
        endpoint: bool = ...,
    ) -> np.bool: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: type[int] = ...,
        endpoint: bool = ...,
    ) -> int: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.uint8] | type[np.uint8] | _UInt8Codes | _SupportsDType[np.dtype[np.uint8]] = ...,
        endpoint: bool = ...,
    ) -> np.uint8: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.uint16] | type[np.uint16] | _UInt16Codes | _SupportsDType[np.dtype[np.uint16]] = ...,
        endpoint: bool = ...,
    ) -> np.uint16: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.uint32] | type[np.uint32] | _UInt32Codes | _SupportsDType[np.dtype[np.uint32]] = ...,
        endpoint: bool = ...,
    ) -> np.uint32: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.uint64] | type[np.uint64] | _UIntCodes | _SupportsDType[np.dtype[np.uint64]] = ...,
        endpoint: bool = ...,
    ) -> np.uint64: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.uint64] | type[np.uint64] | _UInt64Codes | _SupportsDType[np.dtype[np.uint64]] = ...,
        endpoint: bool = ...,
    ) -> np.uint64: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.int8] | type[np.int8] | _Int8Codes | _SupportsDType[np.dtype[np.int8]] = ...,
        endpoint: bool = ...,
    ) -> np.int8: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.int16] | type[np.int16] | _Int16Codes | _SupportsDType[np.dtype[np.int16]] = ...,
        endpoint: bool = ...,
    ) -> np.int16: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.int32] | type[np.int32] | _Int32Codes | _SupportsDType[np.dtype[np.int32]] = ...,
        endpoint: bool = ...,
    ) -> np.int32: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: type[int | np.int_] | np.dtype[np.int_] | _IntCodes | _SupportsDType[np.dtype[np.int_]] = ...,
        endpoint: bool = ...,
    ) -> np.int_: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: int,
        high: int | None = ...,
        size: None = ...,
        dtype: np.dtype[np.int64] | type[np.int64] | _Int64Codes | _SupportsDType[np.dtype[np.int64]] = ...,
        endpoint: bool = ...,
    ) -> np.int64: ...
    @overload
    def integers(  # type: ignore[misc]
        self, low: _ArrayLikeInt_co, high: _ArrayLikeInt_co | None = ..., size: _ShapeLike | None = ..., *, endpoint: bool = ...
    ) -> NDArray[np.int64]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: _DTypeLikeBool = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.bool]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.int8] | type[np.int8] | _Int8Codes | _SupportsDType[np.dtype[np.int8]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.int8]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.int16] | type[np.int16] | _Int16Codes | _SupportsDType[np.dtype[np.int16]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.int16]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.int32] | type[np.int32] | _Int32Codes | _SupportsDType[np.dtype[np.int32]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.int32]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.int64] | type[np.int64] | _Int64Codes | _SupportsDType[np.dtype[np.int64]] | None = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.int64]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.uint8] | type[np.uint8] | _UInt8Codes | _SupportsDType[np.dtype[np.uint8]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.uint8]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.uint16] | type[np.uint16] | _UInt16Codes | _SupportsDType[np.dtype[np.uint16]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.uint16]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.uint32] | type[np.uint32] | _UInt32Codes | _SupportsDType[np.dtype[np.uint32]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.uint32]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.uint64] | type[np.uint64] | _UInt64Codes | _SupportsDType[np.dtype[np.uint64]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.uint64]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: type[int | np.int_] | np.dtype[np.int_] | _IntCodes | _SupportsDType[np.dtype[np.int_]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.int_]: ...
    @overload
    def integers(  # type: ignore[misc]
        self,
        low: _ArrayLikeInt_co,
        high: _ArrayLikeInt_co | None = ...,
        size: _ShapeLike | None = ...,
        dtype: np.dtype[np.uint64] | type[np.uint64] | _UIntCodes | _SupportsDType[np.dtype[np.uint64]] = ...,
        endpoint: bool = ...,
    ) -> NDArray[np.uint64]: ...
    # TODO: Use a TypeVar _T here to get away from Any output?
    #       Should be int->NDArray[np.int64], ArrayLike[_T] -> _T | NDArray[Any]
    @overload
    def choice(
        self,
        a: int,
        size: None = ...,
        replace: bool = ...,
        p: _ArrayLikeFloat_co | None = ...,
        axis: int = ...,
        shuffle: bool = ...,
    ) -> int: ...
    @overload
    def choice(
        self,
        a: int,
        size: _ShapeLike = ...,
        replace: bool = ...,
        p: _ArrayLikeFloat_co | None = ...,
        axis: int = ...,
        shuffle: bool = ...,
    ) -> NDArray[np.int64]: ...
    @overload
    def choice(
        self,
        a: ArrayLike,
        size: None = ...,
        replace: bool = ...,
        p: _ArrayLikeFloat_co | None = ...,
        axis: int = ...,
        shuffle: bool = ...,
    ) -> Any: ...
    @overload
    def choice(
        self,
        a: ArrayLike,
        size: _ShapeLike = ...,
        replace: bool = ...,
        p: _ArrayLikeFloat_co | None = ...,
        axis: int = ...,
        shuffle: bool = ...,
    ) -> NDArray[Any]: ...
    @overload
    def uniform(
        self,
        low: _FloatLike_co = ...,
        high: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def uniform(
        self,
        low: _ArrayLikeFloat_co = ...,
        high: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def normal(
        self,
        loc: _FloatLike_co = ...,
        scale: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def normal(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_gamma(  # type: ignore[misc]
        self,
        shape: _FloatLike_co,
        size: None = ...,
        dtype: _DTypeLikeFloat32 | _DTypeLikeFloat64 = ...,
        out: None = ...,
    ) -> float: ...
    @overload
    def standard_gamma(
        self,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        shape: _ArrayLikeFloat_co,
        *,
        out: NDArray[np.float64] = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
        dtype: _DTypeLikeFloat32 = ...,
        out: NDArray[np.float32] | None = ...,
    ) -> NDArray[np.float32]: ...
    @overload
    def standard_gamma(
        self,
        shape: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
        dtype: _DTypeLikeFloat64 = ...,
        out: NDArray[np.float64] | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def gamma(self, shape: _FloatLike_co, scale: _FloatLike_co = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def gamma(
        self,
        shape: _ArrayLikeFloat_co,
        scale: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def f(self, dfnum: _FloatLike_co, dfden: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def f(self, dfnum: _ArrayLikeFloat_co, dfden: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def noncentral_f(self, dfnum: _FloatLike_co, dfden: _FloatLike_co, nonc: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def noncentral_f(
        self,
        dfnum: _ArrayLikeFloat_co,
        dfden: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def chisquare(self, df: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def chisquare(self, df: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def noncentral_chisquare(self, df: _FloatLike_co, nonc: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def noncentral_chisquare(
        self,
        df: _ArrayLikeFloat_co,
        nonc: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def standard_t(self, df: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def standard_t(self, df: _ArrayLikeFloat_co, size: None = ...) -> NDArray[np.float64]: ...
    @overload
    def standard_t(self, df: _ArrayLikeFloat_co, size: _ShapeLike = ...) -> NDArray[np.float64]: ...
    @overload
    def vonmises(self, mu: _FloatLike_co, kappa: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def vonmises(
        self,
        mu: _ArrayLikeFloat_co,
        kappa: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def pareto(self, a: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def pareto(self, a: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def weibull(self, a: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def weibull(self, a: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def power(self, a: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def power(self, a: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def standard_cauchy(self, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def standard_cauchy(self, size: _ShapeLike = ...) -> NDArray[np.float64]: ...
    @overload
    def laplace(
        self,
        loc: _FloatLike_co = ...,
        scale: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def laplace(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def gumbel(
        self,
        loc: _FloatLike_co = ...,
        scale: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def gumbel(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def logistic(
        self,
        loc: _FloatLike_co = ...,
        scale: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def logistic(
        self,
        loc: _ArrayLikeFloat_co = ...,
        scale: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def lognormal(
        self,
        mean: _FloatLike_co = ...,
        sigma: _FloatLike_co = ...,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def lognormal(
        self,
        mean: _ArrayLikeFloat_co = ...,
        sigma: _ArrayLikeFloat_co = ...,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def rayleigh(self, scale: _FloatLike_co = ..., size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def rayleigh(self, scale: _ArrayLikeFloat_co = ..., size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def wald(self, mean: _FloatLike_co, scale: _FloatLike_co, size: None = ...) -> float: ...  # type: ignore[misc]
    @overload
    def wald(self, mean: _ArrayLikeFloat_co, scale: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    @overload
    def triangular(
        self,
        left: _FloatLike_co,
        mode: _FloatLike_co,
        right: _FloatLike_co,
        size: None = ...,
    ) -> float: ...  # type: ignore[misc]
    @overload
    def triangular(
        self,
        left: _ArrayLikeFloat_co,
        mode: _ArrayLikeFloat_co,
        right: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.float64]: ...
    @overload
    def binomial(self, n: int, p: _FloatLike_co, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def binomial(self, n: _ArrayLikeInt_co, p: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    @overload
    def negative_binomial(self, n: _FloatLike_co, p: _FloatLike_co, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def negative_binomial(
        self,
        n: _ArrayLikeFloat_co,
        p: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.int64]: ...
    @overload
    def poisson(self, lam: _FloatLike_co = ..., size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def poisson(self, lam: _ArrayLikeFloat_co = ..., size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    @overload
    def zipf(self, a: _FloatLike_co, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def zipf(self, a: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    @overload
    def geometric(self, p: _FloatLike_co, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def geometric(self, p: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    @overload
    def hypergeometric(self, ngood: int, nbad: int, nsample: int, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def hypergeometric(
        self,
        ngood: _ArrayLikeInt_co,
        nbad: _ArrayLikeInt_co,
        nsample: _ArrayLikeInt_co,
        size: _ShapeLike | None = ...,
    ) -> NDArray[np.int64]: ...
    @overload
    def logseries(self, p: _FloatLike_co, size: None = ...) -> int: ...  # type: ignore[misc]
    @overload
    def logseries(self, p: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    def multivariate_normal(
        self,
        mean: _ArrayLikeFloat_co,
        cov: _ArrayLikeFloat_co,
        size: _ShapeLike | None = ...,
        check_valid: Literal["warn", "raise", "ignore"] = ...,
        tol: float = ...,
        *,
        method: Literal["svd", "eigh", "cholesky"] = ...,
    ) -> NDArray[np.float64]: ...
    def multinomial(self, n: _ArrayLikeInt_co, pvals: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.int64]: ...
    def multivariate_hypergeometric(
        self,
        colors: _ArrayLikeInt_co,
        nsample: int,
        size: _ShapeLike | None = ...,
        method: Literal["marginals", "count"] = ...,
    ) -> NDArray[np.int64]: ...
    def dirichlet(self, alpha: _ArrayLikeFloat_co, size: _ShapeLike | None = ...) -> NDArray[np.float64]: ...
    def permuted(self, x: ArrayLike, *, axis: int | None = ..., out: NDArray[Any] | None = ...) -> NDArray[Any]: ...
    def shuffle(self, x: ArrayLike, axis: int = ...) -> None: ...

def default_rng(seed: _ArrayLikeInt_co | SeedSequence | BitGenerator | Generator | RandomState | None = ...) -> Generator: ...
