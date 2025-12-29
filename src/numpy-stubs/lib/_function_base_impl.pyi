import datetime as dt
from _typeshed import ConvertibleToInt, Incomplete
from collections.abc import Callable, Iterable, Iterator, Sequence
from typing import (
    Any,
    Concatenate,
    Final,
    Literal as L,
    LiteralString,
    Never,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import ParamSpec, TypeIs, TypeVar

import _numtype as _nt
import numpy as np
from numpy import _OrderKACF as _Order  # noqa: ICN003
from numpy._core.multiarray import bincount
from numpy._globals import _NoValueType
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike, _DTypeLike, _ShapeLike

__all__ = [
    "angle",
    "append",
    "asarray_chkfinite",
    "average",
    "bartlett",
    "bincount",
    "blackman",
    "copy",
    "corrcoef",
    "cov",
    "delete",
    "diff",
    "digitize",
    "extract",
    "flip",
    "gradient",
    "hamming",
    "hanning",
    "i0",
    "insert",
    "interp",
    "iterable",
    "kaiser",
    "median",
    "meshgrid",
    "percentile",
    "piecewise",
    "place",
    "quantile",
    "rot90",
    "select",
    "sinc",
    "sort_complex",
    "trapezoid",
    "trim_zeros",
    "unwrap",
    "vectorize",
]

###

_Tss = ParamSpec("_Tss")
_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT1 = TypeVar("_ScalarT1", bound=np.generic)
_ScalarT2 = TypeVar("_ScalarT2", bound=np.generic)
_FloatingT = TypeVar("_FloatingT", bound=np.floating)
_InexactT = TypeVar("_InexactT", bound=np.inexact)
_InexactTimeT = TypeVar("_InexactTimeT", bound=np.inexact | np.timedelta64)
_InexactDateTimeT = TypeVar("_InexactDateTimeT", bound=np.inexact | np.timedelta64 | np.datetime64)
_ScalarNumericT = TypeVar("_ScalarNumericT", bound=np.inexact | np.timedelta64 | np.object_)
_TrapezoidScalarT = TypeVar("_TrapezoidScalarT", bound=np.inexact | np.timedelta64)
_AnyDoubleT = TypeVar("_AnyDoubleT", bound=np.float64 | np.longdouble | np.complex128 | np.clongdouble)

_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])
_ArrayFloatingT = TypeVar("_ArrayFloatingT", bound=_nt.Array[np.floating])
_ArrayFloatObjT = TypeVar("_ArrayFloatObjT", bound=_nt.Array[np.floating | np.object_])
_ArrayComplexT = TypeVar("_ArrayComplexT", bound=_nt.Array[np.complexfloating])
_ArrayInexactT = TypeVar("_ArrayInexactT", bound=_nt.Array[np.inexact])
_ArrayNumericT = TypeVar("_ArrayNumericT", bound=_nt.Array[np.inexact | np.timedelta64 | np.object_])

# workaround for mypy and pyright not following the typing spec for overloads
_ArrayNoD: TypeAlias = np.ndarray[tuple[Never, Never, Never, Never], np.dtype[_ScalarT]]

# non-trivial scalar-types that will become `complex128` in `sort_complex()`,
# i.e. all numeric scalar types except for `[u]int{8,16} | longdouble`
_SortsToComplex128: TypeAlias = (
    np.bool
    | np.int32
    | np.uint32
    | np.int64
    | np.uint64
    | np.float16
    | np.float32
    | np.float64
    | np.timedelta64
    | np.object_
)

_Mesh2: TypeAlias = tuple[_nt.Array2D[_ScalarT], _nt.Array2D[_ScalarT1]]
_Mesh3: TypeAlias = tuple[_nt.Array3D[_ScalarT], _nt.Array3D[_ScalarT1], _nt.Array3D[_ScalarT2]]

_Tuple2: TypeAlias = tuple[_T, _T]
_PercentileMethod: TypeAlias = L[
    "inverted_cdf",
    "averaged_inverted_cdf",
    "closest_observation",
    "interpolated_inverted_cdf",
    "hazen",
    "weibull",
    "linear",
    "median_unbiased",
    "normal_unbiased",
    "lower",
    "higher",
    "midpoint",
    "nearest",
]
_Indexing: TypeAlias = L["xy", "ij"]

# The resulting value will be used as `y[cond] = func(vals, *args, **kw)`, so in can
# return any (usually 1d) array-like or scalar-like compatible with the input.
_PiecewiseFunction: TypeAlias = Callable[Concatenate[_nt.Array[_ScalarT], _Tss], ArrayLike]
_PiecewiseFunctions: TypeAlias = _SizedIterable[_PiecewiseFunction[_ScalarT, _Tss] | np.generic | complex]

@type_check_only
class _TrimZerosSequence(Protocol[_T_co]):
    def __len__(self, /) -> int: ...
    @overload
    def __getitem__(self, key: int, /) -> object: ...
    @overload
    def __getitem__(self, key: slice, /) -> _T_co: ...

@type_check_only
class _CanRMulFloat(Protocol[_T_co]):
    def __rmul__(self, other: float, /) -> _T_co: ...

@type_check_only
class _SizedIterable(Protocol[_T_co]):
    def __iter__(self) -> Iterator[_T_co]: ...
    def __len__(self) -> int: ...

###

class vectorize:
    __doc__: str | None
    __module__: L["numpy"] = "numpy"
    pyfunc: Callable[..., Incomplete]

    cache: Final[bool]
    signature: Final[LiteralString | None]
    otypes: Final[LiteralString | None]
    excluded: Final[set[int | str]]

    #
    def __init__(
        self,
        /,
        pyfunc: Callable[..., Incomplete] | _NoValueType = ...,
        otypes: str | Iterable[DTypeLike] | None = None,
        doc: str | None = None,
        excluded: Iterable[int | str] | None = None,
        cache: bool = False,
        signature: str | None = None,
    ) -> None: ...

    #
    def __call__(self, /, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

###

#
@overload
def rot90(m: _ArrayT, k: int = 1, axes: tuple[int, int] = (0, 1)) -> _ArrayT: ...
@overload
def rot90(m: _ArrayLike[_ScalarT], k: int = 1, axes: tuple[int, int] = (0, 1)) -> _nt.Array[_ScalarT]: ...
@overload
def rot90(m: ArrayLike, k: int = 1, axes: tuple[int, int] = (0, 1)) -> _nt.Array[Incomplete]: ...

# NOTE: Technically `flip` also accept scalars, but that has no effect and complicates
# the overloads significantly, so we ignore that case here.
@overload
def flip(m: _ArrayT, axis: int | tuple[int, ...] | None = None) -> _ArrayT: ...
@overload
def flip(m: _ArrayLike[_ScalarT], axis: int | tuple[int, ...] | None = None) -> _nt.Array[_ScalarT]: ...
@overload
def flip(m: ArrayLike, axis: int | tuple[int, ...] | None = None) -> _nt.Array[Incomplete]: ...

#
def iterable(y: object) -> TypeIs[Iterable[Any]]: ...

# NOTE: This assumes that if `axis` is given the input is at least 2d, and will
# therefore always return an array.
# NOTE: This assumes that if `keepdims=True` the input is at least 1d, and will
# therefore always return an array.
@overload  # inexact array, keepdims=True
def average(
    a: _ArrayInexactT,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[True],
) -> _ArrayInexactT: ...
@overload  # inexact array, returned=True keepdims=True
def average(
    a: _ArrayInexactT,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[True],
) -> _Tuple2[_ArrayInexactT]: ...
@overload  # inexact array-like, axis=None
def average(
    a: _ArrayLike[_InexactT],
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> _InexactT: ...
@overload  # inexact array-like, axis=<given>
def average(
    a: _ArrayLike[_InexactT],
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> _nt.Array[_InexactT]: ...
@overload  # inexact array-like, keepdims=True
def average(
    a: _ArrayLike[_InexactT],
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[True],
) -> _nt.Array[_InexactT]: ...
@overload  # inexact array-like, axis=None, returned=True
def average(
    a: _ArrayLike[_InexactT],
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[_InexactT]: ...
@overload  # inexact array-like, axis=<given>, returned=True
def average(
    a: _ArrayLike[_InexactT],
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[_nt.Array[_InexactT]]: ...
@overload  # inexact array-like, returned=True, keepdims=True
def average(
    a: _ArrayLike[_InexactT],
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[True],
) -> _Tuple2[_nt.Array[_InexactT]]: ...
@overload  # bool or integer array-like, axis=None
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: None = None,
    weights: _nt.CoFloating_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.float64: ...
@overload  # bool or integer array-like, axis=<given>
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoFloating_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> _nt.Array[np.float64]: ...
@overload  # bool or integer array-like, keepdims=True
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoFloating_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[True],
) -> _nt.Array[np.float64]: ...
@overload  # bool or integer array-like, axis=None, returned=True
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: None = None,
    weights: _nt.CoFloating_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[np.float64]: ...
@overload  # bool or integer array-like, axis=<given>, returned=True
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoFloating_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[_nt.Array[np.float64]]: ...
@overload  # bool or integer array-like, returned=True, keepdims=True
def average(
    a: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoFloating_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[True],
) -> _Tuple2[_nt.Array[np.float64]]: ...
@overload  # complex array-like, axis=None
def average(
    a: _nt.ToComplex128_1nd,
    axis: None = None,
    weights: _nt.CoComplex_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.complex128: ...
@overload  # complex array-like, axis=<given>
def average(
    a: _nt.ToComplex128_1nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> _nt.Array[np.complex128]: ...
@overload  # complex array-like, keepdims=True
def average(
    a: _nt.ToComplex128_1nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_1nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[True],
) -> _nt.Array[np.complex128]: ...
@overload  # complex array-like, axis=None, returned=True
def average(
    a: _nt.ToComplex128_1nd,
    axis: None = None,
    weights: _nt.CoComplex_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[np.complex128]: ...
@overload  # complex array-like, axis=<given>, returned=True
def average(
    a: _nt.ToComplex128_1nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[_nt.Array[np.complex128]]: ...
@overload  # complex array-like, keepdims=True, returned=True
def average(
    a: _nt.ToComplex128_1nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_1nd | None = None,
    *,
    returned: L[True],
    keepdims: L[True],
) -> _Tuple2[_nt.Array[np.complex128]]: ...
@overload  # unknown, axis=None
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> Any: ...
@overload  # unknown, axis=<given>
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.ndarray: ...
@overload  # unknown, keepdims=True
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    returned: L[False] = False,
    *,
    keepdims: L[True],
) -> np.ndarray: ...
@overload  # unknown, axis=None, returned=True
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[Any]: ...
@overload  # unknown, axis=<given>, returned=True
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: int | tuple[int, ...],
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[False] | _NoValueType = ...,
) -> _Tuple2[np.ndarray]: ...
@overload  # unknown, returned=True, keepdims=True
def average(
    a: _nt.CoComplex_nd | _nt.ToObject_nd,
    axis: int | tuple[int, ...] | None = None,
    weights: _nt.CoComplex_nd | None = None,
    *,
    returned: L[True],
    keepdims: L[True],
) -> _Tuple2[np.ndarray]: ...

#
@overload
def asarray_chkfinite(a: _ArrayT, dtype: None = None, order: _Order = None) -> _ArrayT: ...
@overload
def asarray_chkfinite(
    a: np.ndarray[_ShapeT], dtype: _DTypeLike[_ScalarT], order: _Order = None
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def asarray_chkfinite(a: _ArrayLike[_ScalarT], dtype: None = None, order: _Order = None) -> _nt.Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: _DTypeLike[_ScalarT], order: _Order = None) -> _nt.Array[_ScalarT]: ...
@overload
def asarray_chkfinite(a: object, dtype: DTypeLike | None = None, order: _Order = None) -> _nt.Array[Incomplete]: ...

# NOTE: Contrary to the documentation, scalars are also accepted and treated as
# `[condlist]`. And even though the documentation says these should be boolean, in
# practice anything that `np.array(condlist, dtype=bool)` accepts will work, i.e. any
# array-like.
@overload
def piecewise(
    x: _nt.Array[_ScalarT, _ShapeT],
    condlist: ArrayLike,
    funclist: _PiecewiseFunctions[Any, _Tss],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def piecewise(
    x: _ArrayLike[_ScalarT],
    condlist: ArrayLike,
    funclist: _PiecewiseFunctions[Any, _Tss],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> _nt.Array[_ScalarT]: ...
@overload
def piecewise(
    x: ArrayLike,
    condlist: ArrayLike,
    funclist: _PiecewiseFunctions[_ScalarT, _Tss],
    *args: _Tss.args,
    **kw: _Tss.kwargs,
) -> _nt.Array[_ScalarT]: ...

# NOTE: unlike `extract`, passing non-boolean conditions for `condlist` will raise an
# error at runtime
@overload
def select(
    condlist: _SizedIterable[_nt.ToBool_nd], choicelist: Sequence[_ArrayT], default: ArrayLike = 0
) -> _ArrayT: ...
@overload
def select(
    condlist: _SizedIterable[_nt.ToBool_nd],
    choicelist: Sequence[_ArrayLike[_ScalarT]] | _nt.Array[_ScalarT],
    default: ArrayLike = 0,
) -> _nt.Array[_ScalarT]: ...
@overload
def select(
    condlist: _SizedIterable[_nt.ToBool_nd], choicelist: Sequence[ArrayLike], default: ArrayLike = 0
) -> np.ndarray: ...

# keep roughly in sync with `ma.core.copy`
@overload
def copy(a: _ArrayT, order: _Order, subok: L[True]) -> _ArrayT: ...
@overload
def copy(a: _ArrayT, order: _Order = "K", *, subok: L[True]) -> _ArrayT: ...
@overload
def copy(
    a: _nt.CanLenArray[_ScalarT, _ShapeT], order: _Order = "K", subok: L[False] = False
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def copy(a: _ArrayLike[_ScalarT], order: _Order = "K", subok: L[False] = False) -> _nt.Array[_ScalarT]: ...
@overload
def copy(a: ArrayLike, order: _Order = "K", subok: L[False] = False) -> _nt.Array[Incomplete]: ...

#
@overload  # ?d, known inexact scalar-type
def gradient(
    f: _ArrayNoD[_InexactTimeT],
    *varargs: _nt.CoComplex_nd,
    axis: _ShapeLike | None = None,
    edge_order: L[1, 2] = 1,
    # `| Any` instead of ` | tuple` is returned to avoid several mypy_primer errors
) -> _nt.Array1D[_InexactTimeT] | Any: ...
@overload  # 1d, known inexact scalar-type
def gradient(
    f: _nt.Array1D[_InexactTimeT], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _nt.Array1D[_InexactTimeT]: ...
@overload  # 2d, known inexact scalar-type
def gradient(
    f: _nt.Array2D[_InexactTimeT], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh2[_InexactTimeT, _InexactTimeT]: ...
@overload  # 3d, known inexact scalar-type
def gradient(
    f: _nt.Array3D[_InexactTimeT], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh3[_InexactTimeT, _InexactTimeT, _InexactTimeT]: ...
@overload  # ?d, datetime64 scalar-type
def gradient(
    f: _ArrayNoD[np.datetime64], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _nt.Array1D[np.timedelta64] | tuple[_nt.Array[np.timedelta64], ...]: ...
@overload  # 1d, datetime64 scalar-type
def gradient(
    f: _nt.Array1D[np.datetime64], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _nt.Array1D[np.timedelta64]: ...
@overload  # 2d, datetime64 scalar-type
def gradient(
    f: _nt.Array2D[np.datetime64], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh2[np.timedelta64, np.timedelta64]: ...
@overload  # 3d, datetime64 scalar-type
def gradient(
    f: _nt.Array3D[np.datetime64], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh3[np.timedelta64, np.timedelta64, np.timedelta64]: ...
@overload  # 1d float-like
def gradient(
    f: Sequence[float], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _nt.Array1D[np.float64]: ...
@overload  # 2d float-like
def gradient(
    f: _nt.Sequence2D[float], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh2[np.float64, np.float64]: ...
@overload  # 3d float-like
def gradient(
    f: _nt.Sequence3D[float], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh3[np.float64, np.float64, np.float64]: ...
@overload  # 1d complex-like  (the `list` avoids overlap with the float-like overload)
def gradient(
    f: list[complex], *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _nt.Array1D[np.complex128]: ...
@overload  # 2d float-like
def gradient(
    f: _nt.ToComplex128_2ds, *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh2[np.complex128, np.complex128]: ...
@overload  # 3d float-like
def gradient(
    f: _nt.ToComplex128_3ds, *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> _Mesh3[np.complex128, np.complex128, np.complex128]: ...
@overload  # fallback
def gradient(
    f: ArrayLike, *varargs: _nt.CoComplex_nd, axis: _ShapeLike | None = None, edge_order: L[1, 2] = 1
) -> Incomplete: ...

#
@overload  # known array-type
def diff(
    a: _ArrayNumericT,
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _ArrayNumericT: ...
@overload  # known shape, datetime64
def diff(
    a: _nt.Array[np.datetime64, _ShapeT],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array[np.timedelta64, _ShapeT]: ...
@overload  # unknown shape, known scalar-type
def diff(
    a: _ArrayLike[_ScalarNumericT],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array[_ScalarNumericT]: ...
@overload  # unknown shape, datetime64
def diff(
    a: _ArrayLike[np.datetime64],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array[np.timedelta64]: ...
@overload  # 1d int
def diff(
    a: Sequence[int],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array1D[np.int_]: ...
@overload  # 2d int
def diff(
    a: _nt.Sequence2D[int],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array2D[np.int_]: ...
@overload  # 1d float  (the `list` avoids overlap with the `int` overloads)
def diff(
    a: list[float],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array1D[np.float64]: ...
@overload  # 2d float
def diff(
    a: Sequence[list[float]],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array2D[np.float64]: ...
@overload  # 1d complex  (the `list` avoids overlap with the `int` overloads)
def diff(
    a: list[complex],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array1D[np.complex128]: ...
@overload  # 2d complex
def diff(
    a: Sequence[list[complex]],
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array2D[np.complex128]: ...
@overload  # unknown shape, unknown scalar-type
def diff(
    a: ArrayLike,
    n: int = 1,
    axis: SupportsIndex = -1,
    prepend: ArrayLike | _NoValueType = ...,
    append: ArrayLike | _NoValueType = ...,
) -> _nt.Array[Incomplete]: ...

#
@overload  # float scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> np.float64: ...
@overload  # float array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _nt.CoFloating_0d | None = None,
    right: _nt.CoFloating_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.float64] | np.float64: ...
@overload  # complex scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> np.complex128: ...
@overload  # complex or float scalar
def interp(
    x: _nt.CoFloating_0d,
    xp: _nt.CoFloating_nd,
    fp: Sequence[complex | np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.inexact64: ...
@overload  # complex array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex or float array
def interp(
    x: _nt.CoFloating_1nd,
    xp: _nt.CoFloating_nd,
    fp: Sequence[complex | np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[_nt.inexact64]: ...
@overload  # complex scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLike[np.complexfloating],
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[np.complex128] | np.complex128: ...
@overload  # complex or float scalar or array
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoComplex_nd,
    left: _nt.CoComplex_0d | None = None,
    right: _nt.CoComplex_0d | None = None,
    period: _nt.CoFloating_0d | None = None,
) -> _nt.Array[_nt.inexact64] | _nt.inexact64: ...

#
@overload  # 0d T: floating -> 0d T
def angle(z: _FloatingT, deg: bool = False) -> _FloatingT: ...
@overload  # 0d complex | float | ~integer -> 0d float64
def angle(z: complex | _nt.co_integer, deg: bool = False) -> np.float64: ...
@overload  # 0d complex64 -> 0d float32
def angle(z: np.complex64, deg: bool = False) -> np.float32: ...
@overload  # 0d clongdouble -> 0d longdouble
def angle(z: np.clongdouble, deg: bool = False) -> np.longdouble: ...
@overload  # T: nd floating -> T
def angle(z: _ArrayFloatingT, deg: bool = False) -> _ArrayFloatingT: ...
@overload  # nd T: complex128 | ~integer -> nd float64
def angle(
    z: _nt.Array[np.complex128 | _nt.co_integer, _ShapeT], deg: bool = False
) -> _nt.Array[np.float64, _ShapeT]: ...
@overload  # nd T: complex64 -> nd float32
def angle(z: _nt.Array[np.complex64, _ShapeT], deg: bool = False) -> _nt.Array[np.float32, _ShapeT]: ...
@overload  # nd T: clongdouble -> nd longdouble
def angle(z: _nt.Array[np.clongdouble, _ShapeT], deg: bool = False) -> _nt.Array[np.longdouble, _ShapeT]: ...
@overload  # 1d complex -> 1d float64
def angle(z: Sequence[complex], deg: bool = False) -> _nt.Array1D[np.float64]: ...
@overload  # 2d complex -> 2d float64
def angle(z: _nt.Sequence2D[complex], deg: bool = False) -> _nt.Array2D[np.float64]: ...
@overload  # 3d complex -> 3d float64
def angle(z: _nt.Sequence3D[complex], deg: bool = False) -> _nt.Array3D[np.float64]: ...
@overload  # fallback
def angle(z: _nt.CoComplex_nd, deg: bool = False) -> _nt.Array[np.floating] | Any: ...

#
@overload  # known array-type
def unwrap(
    p: _ArrayFloatObjT,
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _ArrayFloatObjT: ...
@overload  # known shape, float64
def unwrap(
    p: _nt.Array[np.float64 | _nt.co_integer, _ShapeT],
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _nt.Array[np.float64, _ShapeT]: ...
@overload  # 1d float64-like
def unwrap(
    p: Sequence[float | np.float64 | _nt.co_integer],
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _nt.Array1D[np.float64]: ...
@overload  # 2d float64-like
def unwrap(
    p: _nt.Sequence2D[float | np.float64 | _nt.co_integer],
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _nt.Array2D[np.float64]: ...
@overload  # 3d float64-like
def unwrap(
    p: _nt.Sequence3D[float | np.float64 | _nt.co_integer],
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _nt.Array3D[np.float64]: ...
@overload  # ?d, float64
def unwrap(
    p: _nt.Sequence1ND[float] | _ArrayLike[np.float64 | _nt.co_integer],
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> _nt.Array[np.float64]: ...
@overload  # fallback
def unwrap(
    p: _nt.CoFloating_nd | _nt.ToObject_nd,
    discont: float | None = None,
    axis: int = -1,
    *,
    period: float = ...,  # = τ
) -> np.ndarray: ...

#
@overload
def sort_complex(a: _ArrayComplexT) -> _ArrayComplexT: ...
@overload  # complex64, shape known
def sort_complex(
    a: _nt.Array[np.int8 | np.uint8 | np.int16 | np.uint16, _ShapeT],
) -> _nt.Array[np.complex64, _ShapeT]: ...
@overload  # complex64, shape unknown
def sort_complex(a: _ArrayLike[np.int8 | np.uint8 | np.int16 | np.uint16]) -> _nt.Array[np.complex64]: ...
@overload  # complex128, shape known
def sort_complex(a: _nt.Array[_SortsToComplex128, _ShapeT]) -> _nt.Array[np.complex128, _ShapeT]: ...
@overload  # complex128, shape unknown
def sort_complex(a: _ArrayLike[_SortsToComplex128]) -> _nt.Array[np.complex128]: ...
@overload  # clongdouble, shape known
def sort_complex(a: _nt.Array[np.longdouble, _ShapeT]) -> _nt.Array[np.clongdouble, _ShapeT]: ...
@overload  # clongdouble, shape unknown
def sort_complex(a: _ArrayLike[np.longdouble]) -> _nt.Array[np.clongdouble]: ...

#
def trim_zeros(
    filt: _TrimZerosSequence[_T], trim: L["f", "b", "fb", "bf"] = "fb", axis: _ShapeLike | None = None
) -> _T: ...

# NOTE: condition is usually boolean, but anything with zero/non-zero semantics works
@overload
def extract(condition: ArrayLike, arr: _ArrayLike[_ScalarT]) -> _nt.Array1D[_ScalarT]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.Sequence1ND[bool]) -> _nt.Array1D[np.bool]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.SequenceND[list[int]]) -> _nt.Array1D[np.int_]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.SequenceND[list[float]]) -> _nt.Array1D[np.float64]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.SequenceND[list[complex]]) -> _nt.Array1D[np.complex128]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.Sequence1ND[bytes]) -> _nt.Array1D[np.bytes_]: ...
@overload
def extract(condition: ArrayLike, arr: _nt.Sequence1ND[str]) -> _nt.Array1D[np.str_]: ...
@overload
def extract(condition: ArrayLike, arr: ArrayLike) -> _nt.Array1D[Incomplete]: ...

#
def place(arr: np.ndarray, mask: ConvertibleToInt | Sequence[ConvertibleToInt], vals: ArrayLike) -> None: ...

# NOTE: keep in sync with `corrcoef`
@overload  # ?d, known inexact scalar-type >=64 precision, y=<given>.
def cov(
    m: _ArrayLike[_AnyDoubleT],
    y: _ArrayLike[_AnyDoubleT],
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: None = None,
) -> _nt.Array2D[_AnyDoubleT]: ...
@overload  # ?d, known inexact scalar-type >=64 precision, y=None -> 0d or 2d
def cov(
    m: _ArrayNoD[_AnyDoubleT],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_AnyDoubleT] | None = None,
) -> _nt.Array[_AnyDoubleT]: ...
@overload  # 1d, known inexact scalar-type >=64 precision, y=None
def cov(
    m: _nt.Array1D[_AnyDoubleT],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_AnyDoubleT] | None = None,
) -> _nt.Array0D[_AnyDoubleT]: ...
@overload  # nd, known inexact scalar-type >=64 precision, y=None -> 0d or 2d
def cov(
    m: _ArrayLike[_AnyDoubleT],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_AnyDoubleT] | None = None,
) -> _nt.Array[_AnyDoubleT]: ...
@overload  # nd, casts to float64, y=<given>
def cov(
    m: _nt.Array[np.float32 | np.float16 | _nt.co_integer] | Sequence[float] | _nt.Sequence2D[float],
    y: _nt.Array[np.float32 | np.float16 | _nt.co_integer] | Sequence[float] | _nt.Sequence2D[float],
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.float64] | None = None,
) -> _nt.Array2D[np.float64]: ...
@overload  # ?d or 2d, casts to float64, y=None -> 0d or 2d
def cov(
    m: _ArrayNoD[np.float32 | np.float16 | _nt.co_integer] | _nt.Sequence2D[float],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # 1d, casts to float64, y=None
def cov(
    m: _nt.Array1D[np.float32 | np.float16 | _nt.co_integer] | Sequence[float],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.float64] | None = None,
) -> _nt.Array0D[np.float64]: ...
@overload  # nd, casts to float64, y=None -> 0d or 2d
def cov(
    m: _ArrayLike[np.float32 | np.float16 | _nt.co_integer],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # 1d complex, y=<given>  (`list` avoids overlap with float overloads)
def cov(
    m: list[complex] | Sequence[list[complex]],
    y: list[complex] | Sequence[list[complex]],
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.complex128] | None = None,
) -> _nt.Array2D[np.complex128]: ...
@overload  # 1d complex, y=None
def cov(
    m: list[complex],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.complex128] | None = None,
) -> _nt.Array0D[np.complex128]: ...
@overload  # 2d complex, y=None -> 0d or 2d
def cov(
    m: Sequence[list[complex]],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # 1d complex-like, y=None, dtype=<known>
def cov(
    m: Sequence[complex | _nt.co_complex],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> _nt.Array0D[_ScalarT]: ...
@overload  # nd complex-like, y=<given>, dtype=<known>
def cov(
    m: _nt.CoComplex_nd,
    y: _nt.CoComplex_nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> _nt.Array2D[_ScalarT]: ...
@overload  # nd complex-like, y=None, dtype=<known> -> 0d or 2d
def cov(
    m: _nt.CoComplex_nd,
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
) -> _nt.Array[_ScalarT]: ...
@overload  # nd complex-like, y=<given>, dtype=?
def cov(
    m: _nt.CoComplex_nd,
    y: _nt.CoComplex_nd,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: DTypeLike | None = None,
) -> _nt.Array2D[Incomplete]: ...
@overload  # 1d complex-like, y=None, dtype=?
def cov(
    m: Sequence[complex | _nt.co_complex],
    y: None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: DTypeLike | None = None,
) -> _nt.Array0D[Incomplete]: ...
@overload  # nd complex-like, dtype=?
def cov(
    m: _nt.CoComplex_nd,
    y: _nt.CoComplex_nd | None = None,
    rowvar: bool = True,
    bias: bool = False,
    ddof: SupportsIndex | SupportsInt | None = None,
    fweights: _nt.ToInteger_1nd | None = None,
    aweights: _nt.CoFloating_1nd | None = None,
    *,
    dtype: DTypeLike | None = None,
) -> _nt.Array[Incomplete]: ...

#
@overload
def corrcoef(
    x: _nt.CoFloat64_1nd,
    y: _nt.CoFloat64_1nd | None = None,
    rowvar: bool = True,
    *,
    dtype: _nt.ToDTypeFloat64 | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def corrcoef(
    x: _nt.ToLongDouble_1nd,
    y: _nt.CoFloating_1nd | None = None,
    rowvar: bool = True,
    *,
    dtype: _nt.ToDTypeLongDouble | None = None,
) -> _nt.Array[np.longdouble]: ...
@overload
def corrcoef(
    x: _nt.CoFloating_1nd, y: _nt.ToLongDouble_1nd, rowvar: bool = True, *, dtype: _nt.ToDTypeLongDouble | None = None
) -> _nt.Array[np.longdouble]: ...
@overload
def corrcoef(
    x: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    y: _nt.CoComplex128_1nd | None = None,
    rowvar: bool = True,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def corrcoef(
    x: _nt.CoComplex128_1nd,
    y: _nt.ToComplex128_1nd | _nt.ToComplex64_1nd,
    rowvar: bool = True,
    *,
    dtype: _nt.ToDTypeComplex128 | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def corrcoef(
    x: _nt.ToCLongDouble_1nd,
    y: _nt.CoComplex_1nd | None = None,
    rowvar: bool = True,
    *,
    dtype: _nt.ToDTypeCLongDouble | None = None,
) -> _nt.Array[np.clongdouble]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd, y: _nt.ToCLongDouble_1nd, rowvar: bool = True, *, dtype: _nt.ToDTypeCLongDouble | None = None
) -> _nt.Array[np.clongdouble]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd, y: _nt.CoComplex_1nd | None = None, rowvar: bool = True, *, dtype: _DTypeLike[_ScalarT]
) -> _nt.Array[_ScalarT]: ...
@overload
def corrcoef(
    x: _nt.CoComplex_1nd, y: _nt.CoComplex_1nd | None = None, rowvar: bool = True, *, dtype: DTypeLike | None = None
) -> _nt.Array[Incomplete]: ...

#
def blackman(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def bartlett(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def hanning(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def hamming(M: _nt.CoFloating_0d) -> _nt.Array1D[np.floating]: ...
def kaiser(M: _nt.CoFloating_0d, beta: _nt.ToFloating_0d) -> _nt.Array1D[np.floating]: ...
def i0(x: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...

#
@overload
def sinc(x: _nt.co_float | float) -> np.floating: ...
@overload
def sinc(x: np.complexfloating | _nt.JustComplex) -> np.complexfloating: ...
@overload
def sinc(x: _nt.CoFloating_1nd) -> _nt.Array[np.floating]: ...
@overload
def sinc(x: _nt.ToComplex_1nd) -> _nt.Array[np.complexfloating]: ...

# keep in sync with `lib._nanfunctions_impl.nanmedian`
@overload
def median(
    a: _nt.CoFloating_nd, axis: None = None, out: None = None, overwrite_input: bool = False, keepdims: L[False] = False
) -> np.floating: ...
@overload
def median(
    a: _nt.ToComplex_nd, axis: None = None, out: None = None, overwrite_input: bool = False, keepdims: L[False] = False
) -> np.complexfloating: ...
@overload
def median(
    a: _nt.ToTimeDelta_nd,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: L[False] = False,
) -> np.timedelta64: ...
@overload
def median(
    a: _nt.ToObject_nd, axis: None = None, out: None = None, overwrite_input: bool = False, keepdims: L[False] = False
) -> Incomplete: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> Incomplete: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> _ArrayT: ...
@overload
def median(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    keepdims: bool = False,
) -> _ArrayT: ...

# NOTE: keep in sync with `quantile`
@overload  # inexact, scalar, axis=None
def percentile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _InexactDateTimeT: ...
@overload  # inexact, scalar, axis=<given>
def percentile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # inexact, scalar, keepdims=True
def percentile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # inexact, array, axis=None
def percentile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT, _ShapeT]: ...
@overload  # inexact, array-like
def percentile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # float, scalar, axis=None
def percentile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> np.float64: ...
@overload  # float, scalar, axis=<given>
def percentile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float, scalar, keepdims=True
def percentile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float, array, axis=None
def percentile(
    a: _nt.CastsArray[np.float64],
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64, _ShapeT]: ...
@overload  # float, array-like
def percentile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex, scalar, axis=None
def percentile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> np.complex128: ...
@overload  # complex, scalar, axis=<given>
def percentile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex, scalar, keepdims=True
def percentile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex, array, axis=None
def percentile(
    a: _nt.ToComplex128_1nd,
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128, _ShapeT]: ...
@overload  # complex, array-like
def percentile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # object_, scalar, axis=None
def percentile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> Any: ...
@overload  # object_, scalar, axis=<given>
def percentile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # object_, scalar, keepdims=True
def percentile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # object_, array, axis=None
def percentile(
    a: _nt.ToObject_1nd,
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_, _ShapeT]: ...
@overload  # object_, array-like
def percentile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # out=<given> (keyword)
def percentile(
    a: ArrayLike,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _ArrayT: ...
@overload  # out=<given> (positional)
def percentile(
    a: ArrayLike,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    weights: _nt.CoFloating_1nd | None = None,
) -> _ArrayT: ...
@overload  # fallback
def percentile(
    a: _nt.CoComplex_1nd | _nt.ToObject_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> Incomplete: ...

# NOTE: keep in sync with `percentile`
@overload  # inexact, scalar, axis=None
def quantile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _InexactDateTimeT: ...
@overload  # inexact, scalar, axis=<given>
def quantile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # inexact, scalar, keepdims=True
def quantile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # inexact, array, axis=None
def quantile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT, _ShapeT]: ...
@overload  # inexact, array-like
def quantile(
    a: _ArrayLike[_InexactDateTimeT],
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[_InexactDateTimeT]: ...
@overload  # float, scalar, axis=None
def quantile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> np.float64: ...
@overload  # float, scalar, axis=<given>
def quantile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float, scalar, keepdims=True
def quantile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float, array, axis=None
def quantile(
    a: _nt.CastsArray[np.float64],
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64, _ShapeT]: ...
@overload  # float, array-like
def quantile(
    a: _nt.CastsArray[np.float64],
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex, scalar, axis=None
def quantile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> np.complex128: ...
@overload  # complex, scalar, axis=<given>
def quantile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex, scalar, keepdims=True
def quantile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex, array, axis=None
def quantile(
    a: _nt.ToComplex128_1nd,
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128, _ShapeT]: ...
@overload  # complex, array-like
def quantile(
    a: _nt.ToComplex128_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # object_, scalar, axis=None
def quantile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> Any: ...
@overload  # object_, scalar, axis=<given>
def quantile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # object_, scalar, keepdims=True
def quantile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_0d,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    *,
    keepdims: L[True],
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # object_, array, axis=None
def quantile(
    a: _nt.ToObject_1nd,
    q: _nt.Array[_nt.co_float, _ShapeT],
    axis: None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: L[False] = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_, _ShapeT]: ...
@overload  # object_, array-like
def quantile(
    a: _nt.ToObject_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _nt.Array[np.object_]: ...
@overload  # out=<given> (keyword)
def quantile(
    a: ArrayLike,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> _ArrayT: ...
@overload  # out=<given> (positional)
def quantile(
    a: ArrayLike,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    weights: _nt.CoFloating_1nd | None = None,
) -> _ArrayT: ...
@overload  # fallback
def quantile(
    a: _nt.CoComplex_1nd | _nt.ToObject_1nd,
    q: _nt.CoFloating_1nd,
    axis: _ShapeLike | None = None,
    out: None = None,
    overwrite_input: bool = False,
    method: _PercentileMethod = "linear",
    keepdims: bool = False,
    *,
    weights: _nt.CoFloating_1nd | None = None,
) -> Incomplete: ...

#
@overload  # workaround for microsoft/pyright#10232
def trapezoid(
    y: _nt._ToArray_nnd[np.float64 | _nt.co_integer],
    x: _nt._ToArray_nnd[np.float64 | _nt.co_integer] | None = None,
    dx: _nt.CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.float64 | _nt.Array[np.float64]: ...
@overload  # workaround for microsoft/pyright#10232
def trapezoid(
    y: _nt._ToArray_nnd[_TrapezoidScalarT],
    x: _nt.Casts[_TrapezoidScalarT, _nt.NeitherShape] | None = None,
    dx: _nt.CastsScalar[_TrapezoidScalarT] | float = 1.0,
    axis: SupportsIndex = -1,
) -> _TrapezoidScalarT | _nt.Array[_TrapezoidScalarT]: ...
@overload  # workaround for microsoft/pyright#10232
def trapezoid(
    y: _nt.Casts[_TrapezoidScalarT, _nt.NeitherShape],
    x: _nt._ToArray_nnd[_TrapezoidScalarT],
    dx: _nt.CastsScalar[_TrapezoidScalarT] | float = 1.0,
    axis: SupportsIndex = -1,
) -> _TrapezoidScalarT | _nt.Array[_TrapezoidScalarT]: ...
@overload
def trapezoid(
    y: _nt._ToArray2_1ds[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_1ds[np.float64 | _nt.co_integer, float] | None = None,
    dx: _nt.CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> np.float64: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1ds, x: _nt.CoFloating_1ds | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.floating: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1ds, x: _nt.CoComplex_1ds | None = None, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1ds, x: _nt.ToComplex_1ds, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> np.complexfloating: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1ds, x: _nt.CoTimeDelta_1ds | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1ds, x: _nt.ToTimeDelta_1ds, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.timedelta64: ...
@overload
def trapezoid(
    y: Sequence[dt.timedelta],
    x: Sequence[dt.timedelta] | _nt.CoFloating_1ds | None = None,
    dx: _nt.CoComplex_0d = 1.0,
    axis: SupportsIndex = -1,
) -> dt.timedelta: ...
@overload
def trapezoid(
    y: _nt._ToArray2_2nd[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_1nd[np.float64 | _nt.co_integer, float] | None = None,
    dx: _nt.CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> _nt.Array[np.float64]: ...
@overload
def trapezoid(
    y: _nt._ToArray2_1nd[np.float64 | _nt.co_integer, float],
    x: _nt._ToArray2_2nd[np.float64 | _nt.co_integer, float],
    dx: _nt.CoFloat64_0d = 1.0,
    axis: SupportsIndex = -1,
) -> _nt.Array[np.float64]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_2nd, x: _nt.CoFloating_1nd | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1nd, x: _nt.CoFloating_2nd, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_2nd, x: _nt.CoComplex_1nd | None = None, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1nd, x: _nt.CoComplex_2nd, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_2nd, x: _nt.ToComplex_1nd, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1nd, x: _nt.ToComplex_2nd, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_2nd, x: _nt.CoTimeDelta_1nd | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1nd, x: _nt.CoTimeDelta_2nd, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_2nd, x: _nt.ToTimeDelta_1nd, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1nd, x: _nt.ToTimeDelta_2nd, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoFloating_1nd, x: _nt.CoFloating_1nd | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.floating | _nt.Array[np.floating]: ...
@overload
def trapezoid(
    y: _nt.ToComplex_1nd, x: _nt.CoComplex_1nd | None = None, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> np.complexfloating | _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.CoComplex_1nd, x: _nt.ToComplex_1nd, dx: _nt.CoComplex_0d = 1.0, axis: SupportsIndex = -1
) -> np.complexfloating | _nt.Array[np.complexfloating]: ...
@overload
def trapezoid(
    y: _nt.ToTimeDelta_1nd, x: _nt.CoTimeDelta_1nd | None = None, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.timedelta64 | _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: _nt.CoTimeDelta_1nd, x: _nt.ToTimeDelta_1nd, dx: _nt.CoFloating_0d = 1.0, axis: SupportsIndex = -1
) -> np.timedelta64 | _nt.Array[np.timedelta64]: ...
@overload
def trapezoid(
    y: Sequence[_CanRMulFloat[_T]],
    x: Sequence[_CanRMulFloat[_T]] | Sequence[_T] | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> _T: ...
@overload
def trapezoid(
    y: _nt.ToObject_1nd | _nt.CoComplex_1nd,
    x: _nt.ToObject_1nd | _nt.CoComplex_1nd | None = None,
    dx: _nt.CoFloating_0d = 1.0,
    axis: SupportsIndex = -1,
) -> Incomplete: ...

#
@overload
def meshgrid(*, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy") -> tuple[()]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT], /, *, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array1D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: ArrayLike, /, *, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array1D]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT1],
    x1: _ArrayLike[_ScalarT2],
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array2D[_ScalarT1], _nt.Array2D[_ScalarT2]]: ...
@overload
def meshgrid(
    x0: ArrayLike, x1: _ArrayLike[_ScalarT], /, *, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array2D[Incomplete], _nt.Array2D[_ScalarT]]: ...
@overload
def meshgrid(
    x0: _ArrayLike[_ScalarT], x1: ArrayLike, /, *, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array2D[_ScalarT], _nt.Array2D[Incomplete]]: ...
@overload
def meshgrid(
    x0: ArrayLike, x1: ArrayLike, /, *, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array2D[Incomplete], _nt.Array2D[Incomplete]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    x2: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array3D[Incomplete], _nt.Array3D[Incomplete], _nt.Array3D[Incomplete]]: ...
@overload
def meshgrid(
    x0: ArrayLike,
    x1: ArrayLike,
    x2: ArrayLike,
    x3: ArrayLike,
    /,
    *,
    copy: bool = True,
    sparse: bool = False,
    indexing: _Indexing = "xy",
) -> tuple[_nt.Array4D[Incomplete], _nt.Array4D[Incomplete], _nt.Array4D[Incomplete], _nt.Array4D[Incomplete]]: ...
@overload
def meshgrid(
    *xi: ArrayLike, copy: bool = True, sparse: bool = False, indexing: _Indexing = "xy"
) -> tuple[_nt.Array[Incomplete], ...]: ...

#
@overload
def delete(
    arr: _ArrayLike[_ScalarT], obj: slice | _nt.CoInteger_nd, axis: SupportsIndex | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def delete(
    arr: ArrayLike, obj: slice | _nt.CoInteger_nd, axis: SupportsIndex | None = None
) -> _nt.Array[Incomplete]: ...

#
@overload
def insert(
    arr: _ArrayLike[_ScalarT], obj: slice | _nt.CoInteger_nd, values: ArrayLike, axis: SupportsIndex | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def insert(
    arr: ArrayLike, obj: slice | _nt.CoInteger_nd, values: ArrayLike, axis: SupportsIndex | None = None
) -> _nt.Array[Incomplete]: ...

#
def append(arr: ArrayLike, values: ArrayLike, axis: SupportsIndex | None = ...) -> _nt.Array[Incomplete]: ...

#
@overload  # workaround for microsoft/pyright#10232
def digitize(x: _nt._ToArray_nnd[_nt.co_float], bins: _nt.CoFloating_1d, right: bool = False) -> _nt.Array[np.intp]: ...  # type: ignore[overload-overlap] # python/mypy#19908
@overload
def digitize(x: _nt.CoFloating_0d, bins: _nt.CoFloating_1d, right: bool = False) -> np.intp: ...
@overload
def digitize(x: _nt.CoFloating_1nd, bins: _nt.CoFloating_1d, right: bool = False) -> _nt.Array[np.intp]: ...
@overload
def digitize(x: _nt.CoFloating_nd, bins: _nt.CoFloating_1d, right: bool = False) -> np.intp | _nt.Array[np.intp]: ...
