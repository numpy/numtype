from collections.abc import Callable, Sequence
from typing import Any, Literal as L, NoReturn, SupportsAbs, SupportsIndex, TypeAlias, overload
from typing_extensions import TypeIs, TypeVar, Unpack

import numpy as np
import numpy.typing as npt
from numpy import (  # noqa: ICN003
    False_,
    True_,
    _AnyShapeT,
    _OrderCF,
    _OrderKACF,
    bitwise_not,
    broadcast,
    dtype,
    flatiter,
    from_dlpack,
    inf,
    little_endian,
    matmul,
    nan,
    ndarray,
    nditer,
    newaxis,
    ufunc,
    vecdot,
)
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _ArrayLikeUnknown,
    _DTypeLike,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc,
)

from ._multiarray_umath import _Array, _Array1D, _FloatType, _KwargsD, _KwargsDL
from .multiarray import (
    arange,
    array,
    asanyarray,
    asarray,
    ascontiguousarray,
    asfortranarray,
    can_cast,
    concatenate,
    copyto,
    dot,
    empty,
    empty_like,
    frombuffer,
    fromfile,
    fromiter,
    fromstring,
    inner,
    lexsort,
    may_share_memory,
    min_scalar_type,
    nested_iters,
    promote_types,
    putmask,
    result_type,
    shares_memory,
    vdot,
    where,
    zeros,
)

__all__ = [
    "False_",
    "True_",
    "allclose",
    "arange",
    "argwhere",
    "array",
    "array_equal",
    "array_equiv",
    "asanyarray",
    "asarray",
    "ascontiguousarray",
    "asfortranarray",
    "astype",
    "base_repr",
    "binary_repr",
    "bitwise_not",
    "broadcast",
    "can_cast",
    "concatenate",
    "convolve",
    "copyto",
    "correlate",
    "count_nonzero",
    "cross",
    "dot",
    "dtype",
    "empty",
    "empty_like",
    "flatiter",
    "flatnonzero",
    "from_dlpack",
    "frombuffer",
    "fromfile",
    "fromfunction",
    "fromiter",
    "fromstring",
    "full",
    "full_like",
    "identity",
    "indices",
    "inf",
    "inner",
    "isclose",
    "isfortran",
    "isscalar",
    "lexsort",
    "little_endian",
    "matmul",
    "may_share_memory",
    "min_scalar_type",
    "moveaxis",
    "nan",
    "ndarray",
    "nditer",
    "nested_iters",
    "newaxis",
    "ones",
    "ones_like",
    "outer",
    "promote_types",
    "putmask",
    "result_type",
    "roll",
    "rollaxis",
    "shares_memory",
    "tensordot",
    "ufunc",
    "vdot",
    "vecdot",
    "where",
    "zeros",
    "zeros_like",
]

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

_CorrelateMode: TypeAlias = L["valid", "same", "full"]

###

# keep in sync with `empty` and `zeros` in `._multiarray_umath.ones`
@overload  # 1d
def ones(
    shape: int | tuple[int],
    dtype: _FloatType | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D[np.float64]: ...
@overload
def ones(
    shape: int | tuple[int],
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D[_ScalarT]: ...
@overload
def ones(
    shape: int | tuple[int],
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D: ...
@overload  # known shape
def ones(
    shape: _AnyShapeT,
    dtype: _FloatType | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[np.float64, _AnyShapeT]: ...
@overload
def ones(
    shape: _AnyShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[_ScalarT, _AnyShapeT]: ...
@overload
def ones(
    shape: _AnyShapeT,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[Any, _AnyShapeT]: ...
@overload  # unknown shape
def ones(
    shape: _ShapeLike,
    dtype: _FloatType | None = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[np.float64]: ...
@overload
def ones(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[_ScalarT]: ...
@overload
def ones(
    shape: _ShapeLike,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array: ...

# keep in sync with `ones`
@overload
def full(
    shape: int | tuple[int],
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D[_ScalarT]: ...
@overload
def full(
    shape: int | tuple[int],
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D[_ScalarT]: ...
@overload
def full(
    shape: int | tuple[int],
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array1D: ...
@overload
def full(
    shape: _ShapeT,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[_ScalarT, _ShapeT]: ...
@overload
def full(
    shape: _ShapeT,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[_ScalarT, _ShapeT]: ...
@overload
def full(
    shape: _ShapeT,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array[Any, _ShapeT]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> NDArray[_ScalarT]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> NDArray[_ScalarT]: ...
@overload
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> _Array: ...

#
@overload
def zeros_like(
    a: _ArrayT,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _ArrayT: ...
@overload
def zeros_like(
    a: _ArrayLike[_ScalarT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def zeros_like(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...
@overload
def zeros_like(
    a: Any,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def zeros_like(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...

#
@overload
def ones_like(
    a: _ArrayT,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _ArrayT: ...
@overload
def ones_like(
    a: _ArrayLike[_ScalarT],
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def ones_like(
    a: object,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...
@overload
def ones_like(
    a: Any,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def ones_like(
    a: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...

#
@overload
def full_like(
    a: _ArrayT,
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: L[True] = ...,
    shape: None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _ArrayT: ...
@overload
def full_like(
    a: _ArrayLike[_ScalarT],
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def full_like(
    a: object,
    fill_value: Any,
    dtype: None = ...,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...
@overload
def full_like(
    a: Any,
    fill_value: Any,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> NDArray[_ScalarT]: ...
@overload
def full_like(
    a: Any,
    fill_value: Any,
    dtype: DTypeLike,
    order: _OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    **kwargs: Unpack[_KwargsD],
) -> _Array: ...

#
@overload
def count_nonzero(a: ArrayLike, axis: None = ..., *, keepdims: L[False] = ...) -> int: ...
@overload
def count_nonzero(a: ArrayLike, axis: _ShapeLike = ..., *, keepdims: bool = ...) -> Any: ...

#
def isfortran(a: _Array | np.generic) -> bool: ...
def argwhere(a: ArrayLike) -> NDArray[np.int_]: ...
def flatnonzero(a: ArrayLike) -> NDArray[np.int_]: ...

#
@overload
def correlate(a: _ArrayLikeUnknown, v: _ArrayLikeUnknown, mode: _CorrelateMode = ...) -> _Array: ...
@overload
def correlate(a: _ArrayLikeBool_co, v: _ArrayLikeBool_co, mode: _CorrelateMode = ...) -> NDArray[np.bool]: ...
@overload
def correlate(a: _ArrayLikeUInt_co, v: _ArrayLikeUInt_co, mode: _CorrelateMode = ...) -> NDArray[np.unsignedinteger]: ...
@overload
def correlate(a: _ArrayLikeInt_co, v: _ArrayLikeInt_co, mode: _CorrelateMode = ...) -> NDArray[np.signedinteger]: ...
@overload
def correlate(a: _ArrayLikeFloat_co, v: _ArrayLikeFloat_co, mode: _CorrelateMode = ...) -> NDArray[np.floating]: ...
@overload
def correlate(a: _ArrayLikeComplex_co, v: _ArrayLikeComplex_co, mode: _CorrelateMode = ...) -> NDArray[np.complexfloating]: ...
@overload
def correlate(a: _ArrayLikeTD64_co, v: _ArrayLikeTD64_co, mode: _CorrelateMode = ...) -> NDArray[np.timedelta64]: ...
@overload
def correlate(a: _ArrayLikeObject_co, v: _ArrayLikeObject_co, mode: _CorrelateMode = ...) -> NDArray[np.object_]: ...

#
@overload
def convolve(a: _ArrayLikeUnknown, v: _ArrayLikeUnknown, mode: _CorrelateMode = ...) -> _Array: ...
@overload
def convolve(a: _ArrayLikeBool_co, v: _ArrayLikeBool_co, mode: _CorrelateMode = ...) -> NDArray[np.bool]: ...
@overload
def convolve(a: _ArrayLikeUInt_co, v: _ArrayLikeUInt_co, mode: _CorrelateMode = ...) -> NDArray[np.unsignedinteger]: ...
@overload
def convolve(a: _ArrayLikeInt_co, v: _ArrayLikeInt_co, mode: _CorrelateMode = ...) -> NDArray[np.signedinteger]: ...
@overload
def convolve(a: _ArrayLikeFloat_co, v: _ArrayLikeFloat_co, mode: _CorrelateMode = ...) -> NDArray[np.floating]: ...
@overload
def convolve(a: _ArrayLikeComplex_co, v: _ArrayLikeComplex_co, mode: _CorrelateMode = ...) -> NDArray[np.complexfloating]: ...
@overload
def convolve(a: _ArrayLikeTD64_co, v: _ArrayLikeTD64_co, mode: _CorrelateMode = ...) -> NDArray[np.timedelta64]: ...
@overload
def convolve(a: _ArrayLikeObject_co, v: _ArrayLikeObject_co, mode: _CorrelateMode = ...) -> NDArray[np.object_]: ...

#
@overload
def outer(a: _ArrayLikeUnknown, b: _ArrayLikeUnknown, out: None = ...) -> _Array: ...
@overload
def outer(a: _ArrayLikeBool_co, b: _ArrayLikeBool_co, out: None = ...) -> NDArray[np.bool]: ...
@overload
def outer(a: _ArrayLikeUInt_co, b: _ArrayLikeUInt_co, out: None = ...) -> NDArray[np.unsignedinteger]: ...
@overload
def outer(a: _ArrayLikeInt_co, b: _ArrayLikeInt_co, out: None = ...) -> NDArray[np.signedinteger]: ...
@overload
def outer(a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, out: None = ...) -> NDArray[np.floating]: ...
@overload
def outer(a: _ArrayLikeComplex_co, b: _ArrayLikeComplex_co, out: None = ...) -> NDArray[np.complexfloating]: ...
@overload
def outer(a: _ArrayLikeTD64_co, b: _ArrayLikeTD64_co, out: None = ...) -> NDArray[np.timedelta64]: ...
@overload
def outer(a: _ArrayLikeObject_co, b: _ArrayLikeObject_co, out: None = ...) -> NDArray[np.object_]: ...
@overload
def outer(
    a: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    b: _ArrayLikeComplex_co | _ArrayLikeTD64_co | _ArrayLikeObject_co,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def tensordot(
    a: _ArrayLikeUnknown,
    b: _ArrayLikeUnknown,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> _Array: ...
@overload
def tensordot(
    a: _ArrayLikeBool_co,
    b: _ArrayLikeBool_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.bool]: ...
@overload
def tensordot(
    a: _ArrayLikeUInt_co,
    b: _ArrayLikeUInt_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.unsignedinteger]: ...
@overload
def tensordot(
    a: _ArrayLikeInt_co,
    b: _ArrayLikeInt_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.signedinteger]: ...
@overload
def tensordot(
    a: _ArrayLikeFloat_co,
    b: _ArrayLikeFloat_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.floating]: ...
@overload
def tensordot(
    a: _ArrayLikeComplex_co,
    b: _ArrayLikeComplex_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def tensordot(
    a: _ArrayLikeTD64_co,
    b: _ArrayLikeTD64_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.timedelta64]: ...
@overload
def tensordot(
    a: _ArrayLikeObject_co,
    b: _ArrayLikeObject_co,
    axes: int | tuple[_ShapeLike, _ShapeLike] = ...,
) -> NDArray[np.object_]: ...

#
@overload
def roll(a: _ArrayLike[_ScalarT], shift: _ShapeLike, axis: _ShapeLike | None = ...) -> NDArray[_ScalarT]: ...
@overload
def roll(a: ArrayLike, shift: _ShapeLike, axis: _ShapeLike | None = ...) -> _Array: ...

#
def rollaxis(a: NDArray[_ScalarT], axis: int, start: int = ...) -> NDArray[_ScalarT]: ...
def moveaxis(a: NDArray[_ScalarT], source: _ShapeLike, destination: _ShapeLike) -> NDArray[_ScalarT]: ...

#
@overload
def cross(
    x1: _ArrayLikeUnknown,
    x2: _ArrayLikeUnknown,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> _Array: ...
@overload
def cross(
    x1: _ArrayLikeBool_co,
    x2: _ArrayLikeBool_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NoReturn: ...
@overload
def cross(
    x1: _ArrayLikeUInt_co,
    x2: _ArrayLikeUInt_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NDArray[np.unsignedinteger]: ...
@overload
def cross(
    x1: _ArrayLikeInt_co,
    x2: _ArrayLikeInt_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NDArray[np.signedinteger]: ...
@overload
def cross(
    x1: _ArrayLikeFloat_co,
    x2: _ArrayLikeFloat_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NDArray[np.floating]: ...
@overload
def cross(
    x1: _ArrayLikeComplex_co,
    x2: _ArrayLikeComplex_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NDArray[np.complexfloating]: ...
@overload
def cross(
    x1: _ArrayLikeObject_co,
    x2: _ArrayLikeObject_co,
    axisa: int = ...,
    axisb: int = ...,
    axisc: int = ...,
    axis: int | None = ...,
) -> NDArray[np.object_]: ...

#
@overload
def indices(
    dimensions: Sequence[int],
    dtype: type[int] = ...,
    sparse: L[False] = ...,
) -> NDArray[np.int_]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: type[int] = ...,
    sparse: L[True] = ...,
) -> tuple[NDArray[np.int_], ...]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: _DTypeLike[_ScalarT],
    sparse: L[False] = ...,
) -> NDArray[_ScalarT]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: _DTypeLike[_ScalarT],
    sparse: L[True],
) -> tuple[NDArray[_ScalarT], ...]: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: DTypeLike,
    sparse: L[False] = ...,
) -> _Array: ...
@overload
def indices(
    dimensions: Sequence[int],
    dtype: DTypeLike,
    sparse: L[True],
) -> tuple[_Array, ...]: ...

#
def fromfunction(
    function: Callable[..., _T],
    shape: Sequence[int],
    *,
    dtype: DTypeLike = ...,
    like: _SupportsArrayFunc = ...,
    **kwargs: object,
) -> _T: ...

#
def isscalar(element: object) -> TypeIs[np.generic | int | float | complex | str | bytes]: ...

#
def binary_repr(num: SupportsIndex, width: int | None = ...) -> str: ...

#
def base_repr(number: SupportsAbs[float], base: float = ..., padding: SupportsIndex = ...) -> str: ...

#
@overload
def identity(n: int, dtype: None = ..., *, like: _SupportsArrayFunc = ...) -> NDArray[np.float64]: ...
@overload
def identity(n: int, dtype: _DTypeLike[_ScalarT], *, like: _SupportsArrayFunc = ...) -> NDArray[_ScalarT]: ...
@overload
def identity(n: int, dtype: DTypeLike, *, like: _SupportsArrayFunc = ...) -> _Array: ...

#
def allclose(a: ArrayLike, b: ArrayLike, rtol: ArrayLike = ..., atol: ArrayLike = ..., equal_nan: bool = ...) -> bool: ...

#
@overload
def isclose(
    a: _ScalarLike_co,
    b: _ScalarLike_co,
    rtol: ArrayLike = ...,
    atol: ArrayLike = ...,
    equal_nan: bool = ...,
) -> np.bool: ...
@overload
def isclose(
    a: ArrayLike,
    b: ArrayLike,
    rtol: ArrayLike = ...,
    atol: ArrayLike = ...,
    equal_nan: bool = ...,
) -> NDArray[np.bool]: ...

#
def array_equal(a1: ArrayLike, a2: ArrayLike, equal_nan: bool = ...) -> bool: ...
def array_equiv(a1: ArrayLike, a2: ArrayLike) -> bool: ...

#
@overload
def astype(
    x: ndarray[_ShapeT, dtype[Any]],
    dtype: _DTypeLike[_ScalarT],
    /,
    *,
    copy: bool = True,
    **kwargs: Unpack[_KwargsD],
) -> ndarray[_ShapeT, dtype[_ScalarT]]: ...
@overload
def astype(
    x: ndarray[_ShapeT, dtype[Any]],
    dtype: DTypeLike,
    /,
    *,
    copy: bool = True,
    **kwargs: Unpack[_KwargsD],
) -> ndarray[_ShapeT, dtype[Any]]: ...
