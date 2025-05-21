import builtins
from collections.abc import Callable
from typing import Any, Literal, TypeAlias, overload
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLike, _BoolCodes, _DTypeLike, _ShapeLike
from numpy.random import BitGenerator, RandomState, SeedSequence

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=_nt.co_integer)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)

_DTypeLikeFloat: TypeAlias = _nt.ToDTypeFloat32 | _nt.ToDTypeFloat64
_CoInt_nnd: TypeAlias = _nt._ToArray_nnd[_nt.co_integer]
_CoFloat_nnd: TypeAlias = _nt._ToArray_nnd[_nt.co_float]

_ExpMethod: TypeAlias = Literal["zig", "inv"]

_ToRNG: TypeAlias = (
    np.integer
    | np.timedelta64
    | _nt.Array[np.integer | np.timedelta64 | np.flexible | np.object_]
    | _nt.SequenceND[int]
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
    def shuffle(self, x: npt.ArrayLike, axis: int = 0) -> None: ...

    #
    def permuted(self, x: npt.ArrayLike, *, axis: int | None = None, out: _nt.Array | None = None) -> _nt.Array: ...

    #
    @overload
    def permutation(self, /, x: int, axis: int = 0) -> _nt.Array[np.int64]: ...
    @overload
    def permutation(self, /, x: _ArrayLike[_ScalarT], axis: int = 0) -> _nt.Array[_ScalarT]: ...
    @overload
    def permutation(self, /, x: npt.ArrayLike, axis: int = 0) -> _nt.Array: ...

    #
    @overload
    def choice(
        self,
        /,
        a: int,
        size: None = None,
        replace: bool = True,
        p: _nt.CoFloating_nd | None = None,
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
        p: _nt.CoFloating_nd | None = None,
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
        p: _nt.CoFloating_nd | None = None,
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
        p: _nt.CoFloating_nd | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def choice(
        self,
        /,
        a: _ArrayLike[_ScalarT],
        size: _ShapeLike,
        replace: bool = True,
        p: _nt.CoFloating_nd | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def choice(
        self,
        /,
        a: npt.ArrayLike,
        size: _ShapeLike,
        replace: bool = True,
        p: _nt.CoFloating_nd | None = None,
        axis: int = 0,
        shuffle: bool = True,
    ) -> _nt.Array: ...

    ###
    # continuous

    #
    @overload
    def random(self, /, size: None = None, dtype: _DTypeLikeFloat = ..., out: None = None) -> float: ...
    @overload
    def random(
        self, /, size: _ShapeLike | None = None, dtype: _nt.ToDTypeFloat64 = ..., *, out: _nt.Array[np.float64, _ShapeT]
    ) -> _nt.Array[np.float64, _ShapeT]: ...
    @overload
    def random(
        self, /, size: _ShapeLike, dtype: _nt.ToDTypeFloat64 = ..., out: _nt.Array[np.float64] | None = None
    ) -> _nt.Array[np.float64]: ...
    @overload
    def random(
        self, /, size: _ShapeLike | None = None, dtype: _nt.ToDTypeFloat32 = ..., *, out: _nt.Array[np.float32, _ShapeT]
    ) -> _nt.Array[np.float32, _ShapeT]: ...
    @overload
    def random(
        self, /, size: _ShapeLike, dtype: _nt.ToDTypeFloat32, out: _nt.Array[np.float32] | None = None
    ) -> _nt.Array[np.float32]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def uniform(
        self, /, low: _CoFloat_nnd, high: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def uniform(
        self, /, low: _nt.CoFloating_nd, high: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def uniform(
        self, /, low: _nt.CoFloating_nd = 0.0, *, high: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def uniform(self, /, low: _nt.CoFloating_0d = 0.0, high: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def triangular(
        self, /, left: _CoFloat_nnd, mode: _nt.CoFloating_nd, right: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def triangular(
        self, /, left: _nt.CoFloating_nd, mode: _CoFloat_nnd, right: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def triangular(
        self, /, left: _nt.CoFloating_nd, mode: _nt.CoFloating_nd, right: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def triangular(
        self, /, left: _nt.CoFloating_0d, mode: _nt.CoFloating_0d, right: _nt.CoFloating_0d, size: None = None
    ) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def beta(self, /, a: _CoFloat_nnd, b: _nt.CoFloating_nd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def beta(self, /, a: _nt.CoFloating_nd, b: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def beta(self, /, a: _nt.CoFloating_0d, b: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def beta(self, /, a: _nt.CoFloating_nd, b: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def beta(
        self, /, a: _nt.CoFloating_nd, b: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload
    def standard_exponential(
        self, /, size: None = None, dtype: _DTypeLikeFloat = ..., method: _ExpMethod = "zig", out: None = None
    ) -> float: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _nt.ToDTypeFloat64 = ...,
        method: _ExpMethod = "zig",
        *,
        out: _nt.Array[np.float64],
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike,
        dtype: _nt.ToDTypeFloat64 = ...,
        method: _ExpMethod = "zig",
        out: _nt.Array[np.float64] | None = None,
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike | None = None,
        dtype: _nt.ToDTypeFloat32 = ...,
        method: _ExpMethod = "zig",
        *,
        out: _nt.Array[np.float32],
    ) -> _nt.Array[np.float32]: ...
    @overload
    def standard_exponential(
        self,
        /,
        size: _ShapeLike,
        dtype: _nt.ToDTypeFloat32,
        method: _ExpMethod = "zig",
        out: _nt.Array[np.float32] | None = None,
    ) -> _nt.Array[np.float32]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def exponential(self, /, scale: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload
    def exponential(self, /, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
    @overload
    def exponential(self, /, scale: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload
    def exponential(self, /, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload
    def exponential(
        self, /, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def laplace(
        self, /, loc: _CoFloat_nnd, scale: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def laplace(
        self, /, loc: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def laplace(
        self, /, loc: _nt.CoFloating_nd = 0.0, *scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def laplace(self, /, loc: _nt.CoFloating_0d = 0.0, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def logistic(
        self, /, loc: _CoFloat_nnd, scale: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def logistic(
        self, /, loc: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def logistic(
        self, /, loc: _nt.CoFloating_nd = 0.0, *, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def logistic(self, /, loc: _nt.CoFloating_0d = 0.0, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def power(self, /, a: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def power(self, /, a: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def power(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def power(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def pareto(self, /, a: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def pareto(self, /, a: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def pareto(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def pareto(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def gumbel(
        self, /, loc: _CoFloat_nnd, scale: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def gumbel(
        self, /, loc: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def gumbel(
        self, /, loc: _nt.CoFloating_nd = 0.0, *, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def gumbel(self, /, loc: _nt.CoFloating_0d = 0.0, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def weibull(self, /, a: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def weibull(self, /, a: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def weibull(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def weibull(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def rayleigh(self, /, scale: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def rayleigh(self, /, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
    @overload  # size: (int, ...)  (positional)
    def rayleigh(self, /, scale: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # size: (int, ...)  (keyword)
    def rayleigh(self, /, scale: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def rayleigh(
        self, /, scale: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def chisquare(self, /, df: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def chisquare(self, /, df: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def chisquare(self, /, df: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def chisquare(self, /, df: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def noncentral_chisquare(
        self, /, df: _CoFloat_nnd, nonc: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def noncentral_chisquare(
        self, /, df: _nt.CoFloating_nd, nonc: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def noncentral_chisquare(self, /, df: _nt.CoFloating_0d, nonc: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def noncentral_chisquare(
        self, /, df: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def noncentral_chisquare(
        self, /, df: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload
    def standard_normal(self, /, size: None = None, dtype: _DTypeLikeFloat = ..., out: None = None) -> float: ...
    @overload
    def standard_normal(
        self, /, size: _ShapeLike | None = None, dtype: _nt.ToDTypeFloat64 = ..., *, out: _nt.Array[np.float64]
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_normal(
        self, /, size: _ShapeLike, dtype: _nt.ToDTypeFloat64 = ..., out: _nt.Array[np.float64] | None = None
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_normal(
        self, /, size: _ShapeLike | None = ..., dtype: _nt.ToDTypeFloat32 = ..., *, out: _nt.Array[np.float32]
    ) -> _nt.Array[np.float32]: ...
    @overload
    def standard_normal(
        self, /, size: _ShapeLike, dtype: _nt.ToDTypeFloat32, out: _nt.Array[np.float32] | None = None
    ) -> _nt.Array[np.float32]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def normal(
        self, /, loc: _CoFloat_nnd, scale: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def normal(
        self, /, loc: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def normal(
        self, /, loc: _nt.CoFloating_nd = 0.0, *, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def normal(self, /, loc: _nt.CoFloating_0d = 0.0, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def lognormal(
        self, /, mean: _CoFloat_nnd, sigma: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def lognormal(
        self, /, mean: _nt.CoFloating_nd = 0.0, *, sigma: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def lognormal(
        self, /, mean: _nt.CoFloating_nd, sigma: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def lognormal(
        self, /, mean: _nt.CoFloating_0d = 0.0, sigma: _nt.CoFloating_0d = 1.0, size: None = None
    ) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def vonmises(
        self, /, mu: _CoFloat_nnd, kappa: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def vonmises(
        self, /, mu: _nt.CoFloating_nd, kappa: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def vonmises(self, /, mu: _nt.CoFloating_0d, kappa: _nt.CoFloating_0d, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def standard_t(self, /, df: _CoFloat_nnd, size: None = None) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def standard_t(self, /, df: float, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def standard_t(self, /, df: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def standard_t(self, /, df: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def standard_gamma(
        self, /, shape: _CoFloat_nnd, size: None = None, dtype: _nt.ToDTypeFloat64 = ..., out: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def standard_gamma(
        self, /, shape: _CoFloat_nnd, size: None = None, *, dtype: _nt.ToDTypeFloat32, out: None = None
    ) -> float | _nt.Array[np.float32]: ...
    @overload  # workaround for microsoft/pyright#10232
    def standard_gamma(
        self, /, shape: _CoFloat_nnd, size: None, dtype: _nt.ToDTypeFloat32, out: None = None
    ) -> float | _nt.Array[np.float32]: ...
    @overload
    def standard_gamma(
        self, /, shape: _nt.CoFloating_0d, size: None = None, dtype: _DTypeLikeFloat = ..., out: None = None
    ) -> float: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
        dtype: _nt.ToDTypeFloat64 = ...,
        *,
        out: _nt.Array[np.float64],
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeFloat64 = ...,
        out: _nt.Array[np.float64] | None = None,
    ) -> _nt.Array[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
        dtype: _nt.ToDTypeFloat64 = ...,
        out: _nt.Array[np.float64] | None = None,
    ) -> float | _nt.Array[np.float64]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeFloat32,
        out: _nt.Array[np.float32] | None = None,
    ) -> _nt.Array[np.float32]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeFloat32,
        out: _nt.Array[np.float32],
    ) -> _nt.Array[np.float32]: ...
    @overload
    def standard_gamma(
        self,
        /,
        shape: _nt.CoFloating_nd,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeFloat32,
        out: None = None,
    ) -> float | _nt.Array[np.float32]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def gamma(
        self, /, shape: _CoFloat_nnd, scale: _nt.CoFloating_nd = 1.0, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def gamma(
        self, /, shape: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def gamma(self, /, shape: _nt.CoFloating_0d, scale: _nt.CoFloating_0d = 1.0, size: None = None) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def f(
        self, /, dfnum: _CoFloat_nnd, dfden: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def f(self, /, dfnum: _nt.CoFloating_0d, dfden: _nt.CoFloating_0d, size: None = None) -> float: ...
    @overload  # size: (int, ...)
    def f(self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.float64]: ...
    @overload  # fallback
    def f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> float | _nt.Array[np.float64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def noncentral_f(
        self, /, dfnum: _CoFloat_nnd, dfden: _nt.CoFloating_nd, nonc: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def noncentral_f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _CoFloat_nnd, nonc: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def noncentral_f(
        self, /, dfnum: _nt.CoFloating_nd, dfden: _nt.CoFloating_nd, nonc: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # size: None  (default)
    def noncentral_f(
        self, /, dfnum: _nt.CoFloating_0d, dfden: _nt.CoFloating_0d, nonc: _nt.CoFloating_0d, size: None = None
    ) -> float: ...
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
    @overload  # workaround for microsoft/pyright#10232
    def wald(
        self, /, mean: _CoFloat_nnd, scale: _nt.CoFloating_nd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def wald(
        self, /, mean: _nt.CoFloating_nd, scale: _CoFloat_nnd, size: None = None
    ) -> float | _nt.Array[np.float64]: ...
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
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: type[bool], endpoint: bool = False
    ) -> bool: ...
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
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _BoolCodes, endpoint: bool = False
    ) -> np.bool: ...
    @overload
    def integers(
        self, /, low: int, high: int | None = None, size: None = None, *, dtype: _nt.ToDTypeInt8, endpoint: bool = False
    ) -> np.int8: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _nt.ToDTypeUInt8,
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
        dtype: _nt.ToDTypeInt16,
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
        dtype: _nt.ToDTypeUInt16,
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
        dtype: _nt.ToDTypeInt32,
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
        dtype: _nt.ToDTypeUInt32,
        endpoint: bool = False,
    ) -> np.uint32: ...
    @overload
    def integers(  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _nt.ToDTypeInt64,
        endpoint: bool = False,
    ) -> int | np.int64: ...
    @overload
    def integers(
        self,
        /,
        low: int,
        high: int | None = None,
        size: None = None,
        *,
        dtype: _nt.ToDTypeUInt64,
        endpoint: bool = False,
    ) -> np.uint64: ...
    @overload  # size: _ShapeLike (positional)
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> _nt.Array[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: type[bool] | _BoolCodes,
        endpoint: bool = False,
    ) -> _nt.Array[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt8,
        endpoint: bool = False,
    ) -> _nt.Array[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt8,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt16,
        endpoint: bool = False,
    ) -> _nt.Array[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt16,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt32,
        endpoint: bool = False,
    ) -> _nt.Array[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt32,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt64,
        endpoint: bool = False,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt64,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint64]: ...
    @overload  # size: _ShapeLike (keyword)
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[np.int64] = ...,
        endpoint: bool = False,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> _nt.Array[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: type[bool] | _BoolCodes,
        endpoint: bool = False,
    ) -> _nt.Array[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt8,
        endpoint: bool = False,
    ) -> _nt.Array[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt8,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt16,
        endpoint: bool = False,
    ) -> _nt.Array[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt16,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt32,
        endpoint: bool = False,
    ) -> _nt.Array[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt32,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeInt64,
        endpoint: bool = False,
    ) -> _nt.Array[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        *,
        size: _ShapeLike,
        dtype: _nt.ToDTypeUInt64,
        endpoint: bool = False,
    ) -> _nt.Array[np.uint64]: ...
    @overload  # fallback
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: type[bool],
        endpoint: bool = False,
    ) -> bool | _nt.Array[np.bool]: ...
    @overload
    def integers(  # type: ignore[overload-overlap]
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _DTypeLike[_IntegerT],
        endpoint: bool = False,
    ) -> _IntegerT | _nt.Array[_IntegerT]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _BoolCodes,
        endpoint: bool = False,
    ) -> np.bool | _nt.Array[np.bool]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt8,
        endpoint: bool = False,
    ) -> np.int8 | _nt.Array[np.int8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt8,
        endpoint: bool = False,
    ) -> np.uint8 | _nt.Array[np.uint8]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt16,
        endpoint: bool = False,
    ) -> np.int16 | _nt.Array[np.int16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt16,
        endpoint: bool = False,
    ) -> np.uint16 | _nt.Array[np.uint16]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt32,
        endpoint: bool = False,
    ) -> np.int32 | _nt.Array[np.int32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt32,
        endpoint: bool = False,
    ) -> np.uint32 | _nt.Array[np.uint32]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeInt64 = ...,
        endpoint: bool = False,
    ) -> int | np.int64 | _nt.Array[np.int64]: ...
    @overload
    def integers(
        self,
        /,
        low: _nt.CoInteger_nd,
        high: _nt.CoInteger_nd | None = None,
        size: _ShapeLike | None = None,
        *,
        dtype: _nt.ToDTypeUInt64,
        endpoint: bool = False,
    ) -> np.uint64 | _nt.Array[np.uint64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def binomial(self, /, n: _CoInt_nnd, p: _nt.CoFloating_nd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def binomial(self, /, n: _nt.CoInteger_nd, p: _CoFloat_nnd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def binomial(self, /, n: int, p: _nt.CoFloating_0d, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def binomial(self, /, n: _nt.CoInteger_nd, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def binomial(
        self, /, n: _nt.CoInteger_nd, p: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def negative_binomial(
        self, /, n: _CoFloat_nnd, p: _nt.CoFloating_nd, size: None = None
    ) -> int | _nt.Array[np.int64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def negative_binomial(
        self, /, n: _nt.CoFloating_nd, p: _CoFloat_nnd, size: None = None
    ) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def negative_binomial(self, /, n: _nt.CoFloating_0d, p: _nt.CoFloating_0d, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def negative_binomial(
        self, /, n: _nt.CoFloating_nd, p: _nt.CoFloating_nd, size: _ShapeLike
    ) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def negative_binomial(
        self, /, n: _nt.CoFloating_nd, p: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def poisson(self, /, lam: _CoFloat_nnd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def poisson(self, /, lam: _nt.CoFloating_0d = 1.0, size: None = None) -> int: ...
    @overload  # size: (int, ...)  (positional)
    def poisson(self, /, lam: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # size: (int, ...)  (keyword)
    def poisson(self, /, lam: _nt.CoFloating_nd = 1.0, *, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def poisson(self, /, lam: _nt.CoFloating_nd = 1.0, size: _ShapeLike | None = None) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def zipf(self, /, a: _CoFloat_nnd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def zipf(self, /, a: _nt.CoFloating_0d, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def zipf(self, /, a: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def zipf(self, /, a: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def geometric(self, /, p: _CoFloat_nnd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def geometric(self, /, p: _nt.CoFloating_0d, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def geometric(self, /, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def geometric(self, /, p: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def hypergeometric(
        self, /, ngood: _CoInt_nnd, nbad: _nt.CoInteger_nd, nsample: _nt.CoInteger_nd, size: None = None
    ) -> int | _nt.Array[np.int64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def hypergeometric(
        self, /, ngood: _nt.CoInteger_nd, nbad: _CoInt_nnd, nsample: _nt.CoInteger_nd, size: None = None
    ) -> int | _nt.Array[np.int64]: ...
    @overload  # workaround for microsoft/pyright#10232
    def hypergeometric(
        self, /, ngood: _nt.CoInteger_nd, nbad: _nt.CoInteger_nd, nsample: _CoInt_nnd, size: None = None
    ) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def hypergeometric(self, /, ngood: int, nbad: int, nsample: int, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def hypergeometric(
        self, /, ngood: _nt.CoInteger_nd, nbad: _nt.CoInteger_nd, nsample: _nt.CoInteger_nd, size: _ShapeLike
    ) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def hypergeometric(
        self,
        /,
        ngood: _nt.CoInteger_nd,
        nbad: _nt.CoInteger_nd,
        nsample: _nt.CoInteger_nd,
        size: _ShapeLike | None = None,
    ) -> int | _nt.Array[np.int64]: ...

    #
    @overload  # workaround for microsoft/pyright#10232
    def logseries(self, /, p: _CoFloat_nnd, size: None = None) -> int | _nt.Array[np.int64]: ...
    @overload  # size: None  (default)
    def logseries(self, /, p: _nt.CoFloating_0d, size: None = None) -> int: ...
    @overload  # size: (int, ...)
    def logseries(self, /, p: _nt.CoFloating_nd, size: _ShapeLike) -> _nt.Array[np.int64]: ...
    @overload  # fallback
    def logseries(self, /, p: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> int | _nt.Array[np.int64]: ...

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
        *,
        method: Literal["svd", "eigh", "cholesky"] = "svd",
    ) -> _nt.Array[np.float64]: ...

    #
    def dirichlet(self, /, alpha: _nt.CoFloating_nd, size: _ShapeLike | None = None) -> _nt.Array[np.float64]: ...

    #
    def multinomial(
        self, /, n: _nt.CoInteger_nd, pvals: _nt.CoFloating_nd, size: _ShapeLike | None = None
    ) -> _nt.Array[np.int64]: ...

    #
    def multivariate_hypergeometric(
        self,
        colors: _nt.CoInteger_nd,
        nsample: int,
        size: _ShapeLike | None = None,
        method: Literal["marginals", "count"] = "marginals",
    ) -> _nt.Array[np.int64]: ...

#
def default_rng(seed: _ToRNG = None) -> Generator: ...
