from collections.abc import Iterable, Sequence
from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex as CanIndex, SupportsInt, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    Array,
    Array_2d,
    AtLeast2D,
    CanArraySized,
    CoBool_1nd,
    CoComplex64_1nd,
    CoComplex128_0d,
    CoComplex128_1d,
    CoComplex128_1ds,
    CoComplex128_1nd,
    CoComplex128_2ds,
    CoComplex128_3nd,
    CoComplex128_nd,
    CoComplex_1ds,
    CoComplex_1nd,
    CoComplex_2ds,
    CoComplex_2nd,
    CoComplex_3nd,
    CoFloat64_1d,
    CoFloat64_1ds,
    CoFloat64_1nd,
    CoFloating_1ds,
    CoFloating_1nd,
    CoIntP_1d,
    CoIntP_1ds,
    CoIntP_1nd,
    CoInteger_1d,
    CoInteger_1ds,
    CoInteger_1nd,
    CoTimeDelta_1d,
    Is,
    Sequence_2d,
    Sequence_2nd,
    Sequence_3nd,
    Sequence_nd,
    ToBool_1d,
    ToBool_1ds,
    ToBool_1nd,
    ToBool_2nd,
    ToCharacter_1nd,
    ToComplex64_1d,
    ToComplex64_1nd,
    ToComplex64_2ds,
    ToComplex64_3nd,
    ToComplex128_1d,
    ToComplex128_1ds,
    ToComplex128_1nd,
    ToComplex128_2ds,
    ToComplex128_2nd,
    ToComplex128_3nd,
    ToComplex_1ds,
    ToComplex_1nd,
    ToComplex_2nd,
    ToFloat16_1nd,
    ToFloat16_2ds,
    ToFloat16_3nd,
    ToFloat32_1d,
    ToFloat32_1nd,
    ToFloat32_2ds,
    ToFloat32_3nd,
    ToFloat64_1d,
    ToFloat64_1ds,
    ToFloat64_1nd,
    ToFloat64_2nd,
    ToFloating_1ds,
    ToFloating_1nd,
    ToFloating_2nd,
    ToFloating_nd,
    ToGeneric_1nd,
    ToIntP_1d,
    ToIntP_1ds,
    ToIntP_1nd,
    ToIntP_2nd,
    ToInteger_1d,
    ToInteger_1ds,
    ToInteger_1nd,
    ToInteger_2nd,
    ToNumber_1d,
    ToObject_0d,
    ToObject_1d,
    ToObject_1nd,
    ToTimeDelta_1d,
    ToTimeDelta_1nd,
    ToUInteger_1nd,
    _ToArray1_1d,
    _ToArray1_1ds,
    _ToArray1_1nd,
    _ToArray1_2ds,
    _ToArray1_2nd,
    _ToArray1_3nd,
    _ToArray_1nd,
    _ToArray_2ds,
    _ToArray_3nd,
)
from numpy._core.fromnumeric import matrix_transpose
from numpy._core.numeric import tensordot, vecdot
from numpy._typing import DTypeLike, _32Bit, _64Bit, _DTypeLike as _ToDType

__all__ = [
    "LinAlgError",
    "cholesky",
    "cond",
    "cross",
    "det",
    "diagonal",
    "eig",
    "eigh",
    "eigvals",
    "eigvalsh",
    "inv",
    "lstsq",
    "matmul",
    "matrix_norm",
    "matrix_power",
    "matrix_rank",
    "matrix_transpose",
    "multi_dot",
    "norm",
    "outer",
    "pinv",
    "qr",
    "slogdet",
    "solve",
    "svd",
    "svdvals",
    "tensordot",
    "tensorinv",
    "tensorsolve",
    "trace",
    "vecdot",
    "vector_norm",
]

###

_SafeFloating: TypeAlias = np.float32 | np.float64
_SafeInexact: TypeAlias = _SafeFloating | np.complex64 | np.complex128

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=Array[Any])
_Shape2T = TypeVar("_Shape2T", bound=AtLeast2D)

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=np.integer)
_FloatingT = TypeVar("_FloatingT", bound=np.floating)
_NumberT = TypeVar("_NumberT", bound=np.number)

_FloatingT_co = TypeVar("_FloatingT_co", bound=np.floating, default=np.floating, covariant=True)
_InexactT_co = TypeVar("_InexactT_co", bound=np.inexact, default=np.inexact, covariant=True)

_FloatingNDT_co = TypeVar("_FloatingNDT_co", bound=np.floating | Array[np.floating], default=Any, covariant=True)
_InexactNDT_co = TypeVar("_InexactNDT_co", bound=np.inexact | Array[np.inexact], default=Any, covariant=True)

_AnyNumberT = TypeVar(
    "_AnyNumberT",
    np.int_,
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
    np.float16,
    np.float32,
    np.float64,
    np.longdouble,
    np.complex64,
    np.complex128,
    np.clongdouble,
)

_False: TypeAlias = L[False]
_True: TypeAlias = L[True]

_2Tuple: TypeAlias = tuple[_T, _T]
_ToInt: TypeAlias = SupportsInt | CanIndex

_Ax2: TypeAlias = _ToInt | _2Tuple[_ToInt]
_Axes: TypeAlias = Iterable[int]

_ArrayOrScalar: TypeAlias = _ScalarT | Array[_ScalarT]
_Ord: TypeAlias = L[1, -1, 2, -2, "fro", "nuc"] | float
_UPLO: TypeAlias = L["L", "U", "l", "u"]

_ToArray_2nd_ish: TypeAlias = CanArraySized[_ScalarT] | Sequence[Sequence_nd[_ScalarT]] | Sequence_nd[CanArraySized[_ScalarT]]

_ToFloat64_1nd: TypeAlias = _ToArray_1nd[np.floating[_64Bit] | np.integer | np.bool, float]
_ToFloat64_2ds: TypeAlias = _ToArray_2ds[np.floating[_64Bit] | np.integer | np.bool, float]
_ToFloat64_3nd: TypeAlias = _ToArray_3nd[np.floating[_64Bit] | np.integer | np.bool, float]

_ToInexact32_1nd: TypeAlias = _ToArray1_1nd[np.inexact[_32Bit]]
_ToInexact32_2ds: TypeAlias = _ToArray1_2ds[np.inexact[_32Bit]]
_ToInexact32_3nd: TypeAlias = _ToArray1_3nd[np.inexact[_32Bit]]

_ToInexact64_1nd: TypeAlias = _ToArray_1nd[np.inexact[_64Bit] | np.integer | np.bool, complex]
_ToInexact64_2ds: TypeAlias = _ToArray_2ds[np.inexact[_64Bit] | np.integer | np.bool, complex]
_ToInexact64_3nd: TypeAlias = _ToArray_3nd[np.inexact[_64Bit] | np.integer | np.bool, complex]

_ToInexactLD_1nd: TypeAlias = _ToArray1_1nd[np.longdouble | np.clongdouble]
_ToInexactLD_2ds: TypeAlias = _ToArray1_2ds[np.longdouble | np.clongdouble]
_ToInexactLD_3nd: TypeAlias = _ToArray1_3nd[np.longdouble | np.clongdouble]

_ToUnsafe64_1nd: TypeAlias = _ToArray_1nd[np.inexact[_64Bit] | np.integer | np.bool | np.character, complex | bytes | str]
_ToUnsafe64_2ds: TypeAlias = _ToArray_2ds[np.inexact[_64Bit] | np.integer | np.bool | np.character, complex | bytes | str]
_ToUnsafe64_3nd: TypeAlias = _ToArray_3nd[np.inexact[_64Bit] | np.integer | np.bool | np.character, complex | bytes | str]

_Array_2nd: TypeAlias = Array[_ScalarT, AtLeast2D]

_LstSqResult: TypeAlias = tuple[Array[_ScalarT], Array[_FloatingT], np.int32, Array[_FloatingT]]

###

class EigResult(NamedTuple, Generic[_InexactT_co]):
    eigenvalues: Array[_InexactT_co]
    eigenvectors: _Array_2nd[_InexactT_co]

class EighResult(NamedTuple, Generic[_FloatingT_co, _InexactT_co]):
    eigenvalues: Array[_FloatingT_co]
    eigenvectors: _Array_2nd[_InexactT_co]

class QRResult(NamedTuple, Generic[_InexactT_co]):
    Q: _Array_2nd[_InexactT_co]
    R: _Array_2nd[_InexactT_co]

class SVDResult(NamedTuple, Generic[_FloatingT_co, _InexactT_co]):
    U: _Array_2nd[_InexactT_co]
    S: Array[_FloatingT_co]
    Vh: _Array_2nd[_InexactT_co]

class SlogdetResult(NamedTuple, Generic[_FloatingNDT_co, _InexactNDT_co]):
    sign: _InexactNDT_co
    logabsdet: _FloatingNDT_co

class LinAlgError(ValueError): ...

# keep in sync with `solve`
@overload
def tensorsolve(a: _ToFloat64_1nd, b: CoFloat64_1nd, axes: _Axes | None = None) -> Array[np.float64]: ...
@overload
def tensorsolve(a: CoFloat64_1nd, b: _ToFloat64_1nd, axes: _Axes | None = None) -> Array[np.float64]: ...
@overload
def tensorsolve(a: ToComplex128_1nd, b: CoComplex128_1nd, axes: _Axes | None = None) -> Array[np.complex128]: ...
@overload
def tensorsolve(a: CoComplex128_1nd, b: ToComplex128_1nd, axes: _Axes | None = None) -> Array[np.complex128]: ...
@overload
def tensorsolve(a: ToFloat32_1nd, b: ToFloat32_1nd, axes: _Axes | None = None) -> Array[np.float32]: ...
@overload
def tensorsolve(a: ToComplex64_1nd, b: ToComplex64_1nd, axes: _Axes | None = None) -> Array[np.complex64]: ...
@overload
def tensorsolve(a: CoFloat64_1nd, b: CoFloat64_1nd, axes: _Axes | None = None) -> Array[np.floating]: ...
@overload
def tensorsolve(a: CoComplex128_1nd, b: CoComplex128_1nd, axes: _Axes | None = None) -> Array[np.inexact]: ...

# keep in sync with `tensorsolve`
@overload
def solve(a: _ToFloat64_1nd, b: CoFloat64_1nd) -> Array[np.float64]: ...
@overload
def solve(a: CoFloat64_1nd, b: _ToFloat64_1nd) -> Array[np.float64]: ...
@overload
def solve(a: ToComplex128_1nd, b: CoComplex128_1nd) -> Array[np.complex128]: ...
@overload
def solve(a: CoComplex128_1nd, b: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload
def solve(a: ToFloat32_1nd, b: ToFloat32_1nd) -> Array[np.float32]: ...
@overload
def solve(a: ToComplex64_1nd, b: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload
def solve(a: CoFloat64_1nd, b: CoFloat64_1nd) -> Array[np.floating]: ...
@overload
def solve(a: CoComplex128_1nd, b: CoComplex128_1nd) -> Array[np.inexact]: ...

# keep in sync with `inv`
@overload
def tensorinv(a: _ToFloat64_1nd, ind: int = 2) -> _Array_2nd[np.float64]: ...
@overload
def tensorinv(a: ToComplex128_1nd, ind: int = 2) -> _Array_2nd[np.complex128]: ...
@overload
def tensorinv(a: ToFloat32_1nd, ind: int = 2) -> _Array_2nd[np.float32]: ...
@overload
def tensorinv(a: ToComplex64_1nd, ind: int = 2) -> _Array_2nd[np.complex64]: ...
@overload
def tensorinv(a: CoFloat64_1nd, ind: int = 2) -> _Array_2nd[np.floating]: ...
@overload
def tensorinv(a: CoComplex128_1nd, ind: int = 2) -> _Array_2nd[np.inexact]: ...

# keep in sync with `tensorinv`
@overload
def inv(a: _ToFloat64_1nd) -> _Array_2nd[np.float64]: ...
@overload
def inv(a: ToComplex128_1nd) -> _Array_2nd[np.complex128]: ...
@overload
def inv(a: ToFloat32_1nd) -> _Array_2nd[np.float32]: ...
@overload
def inv(a: ToComplex64_1nd) -> _Array_2nd[np.complex64]: ...
@overload
def inv(a: CoFloat64_1nd) -> _Array_2nd[np.floating]: ...
@overload
def inv(a: CoComplex128_1nd) -> _Array_2nd[np.inexact]: ...

#
@overload
def pinv(
    a: _ToFloat64_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.float64]: ...
@overload
def pinv(
    a: ToComplex128_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.complex128]: ...
@overload
def pinv(
    a: ToFloat32_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.float32]: ...
@overload
def pinv(
    a: ToComplex64_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.complex64]: ...
@overload
def pinv(
    a: CoFloat64_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.floating]: ...
@overload
def pinv(
    a: CoComplex128_1nd,
    rcond: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> _Array_2nd[np.inexact]: ...

_PosInt: TypeAlias = L[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_NegInt: TypeAlias = L[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]

#
@overload
def matrix_power(a: CanArraySized[_NumberT, _Shape2T], n: _PosInt) -> Array[_NumberT, _Shape2T]: ...  # type: ignore[overload-overlap]
@overload
def matrix_power(a: CoBool_1nd, n: _PosInt) -> _Array_2nd[np.bool]: ...
@overload
def matrix_power(a: ToIntP_1nd, n: _PosInt) -> _Array_2nd[np.intp]: ...  # type: ignore[overload-overlap]
@overload
def matrix_power(a: CoInteger_1nd, n: _NegInt) -> _Array_2nd[np.float64]: ...
@overload
def matrix_power(a: ToFloat64_1nd, n: CanIndex) -> _Array_2nd[np.float64]: ...  # type: ignore[overload-overlap]
@overload
def matrix_power(a: ToComplex128_1nd, n: CanIndex) -> _Array_2nd[np.complex128]: ...  # type: ignore[overload-overlap]
@overload
def matrix_power(a: ToFloat32_1nd, n: CanIndex) -> _Array_2nd[np.float32]: ...
@overload
def matrix_power(a: ToComplex64_1nd, n: CanIndex) -> _Array_2nd[np.complex64]: ...
@overload
def matrix_power(a: ToObject_1nd, n: CanIndex) -> _Array_2nd[np.object_]: ...  # type: ignore[overload-overlap]
@overload
def matrix_power(a: ToUInteger_1nd, n: _PosInt) -> _Array_2nd[np.unsignedinteger]: ...
@overload
def matrix_power(a: ToInteger_1nd, n: _PosInt) -> _Array_2nd[np.integer]: ...
@overload
def matrix_power(a: CoComplex128_1nd, n: _NegInt) -> _Array_2nd[np.inexact]: ...
@overload
def matrix_power(a: CoComplex_1nd | ToObject_1nd, n: CanIndex) -> _Array_2nd[Any]: ...

#
@overload
def cholesky(a: _ToFloat64_1nd) -> _Array_2nd[np.float64]: ...
@overload
def cholesky(a: ToComplex128_1nd) -> _Array_2nd[np.complex128]: ...
@overload
def cholesky(a: ToFloat32_1nd) -> _Array_2nd[np.float32]: ...
@overload
def cholesky(a: ToComplex64_1nd) -> _Array_2nd[np.complex64]: ...
@overload
def cholesky(a: CoFloat64_1nd) -> _Array_2nd[np.floating]: ...
@overload
def cholesky(a: CoComplex128_1nd) -> _Array_2nd[np.inexact]: ...

#
@overload
def outer(x1: _ToArray1_1d[_IntegerT], x2: _ToArray1_1d[_IntegerT], /) -> Array_2d[_IntegerT]: ...
@overload
def outer(x1: ToBool_1d, x2: ToBool_1d, /) -> Array_2d[np.bool]: ...
@overload
def outer(x1: ToIntP_1d, x2: CoIntP_1d, /) -> Array_2d[np.intp]: ...
@overload
def outer(x1: CoIntP_1d, x2: ToIntP_1d, /) -> Array_2d[np.intp]: ...
@overload
def outer(x1: ToFloat64_1d, x2: CoFloat64_1d, /) -> Array_2d[np.float64]: ...
@overload
def outer(x1: CoFloat64_1d, x2: ToFloat64_1d, /) -> Array_2d[np.float64]: ...
@overload
def outer(x1: ToComplex128_1d, x2: CoComplex128_1d, /) -> Array_2d[np.complex128]: ...
@overload
def outer(x1: CoComplex128_1d, x2: ToComplex128_1d, /) -> Array_2d[np.complex128]: ...
@overload
def outer(x1: ToTimeDelta_1d, x2: CoTimeDelta_1d, /) -> Array_2d[np.timedelta64]: ...
@overload
def outer(x1: CoTimeDelta_1d, x2: ToTimeDelta_1d, /) -> Array_2d[np.timedelta64]: ...
@overload
def outer(x1: ToFloat32_1d, x2: ToFloat32_1d, /) -> Array_2d[np.float32]: ...
@overload
def outer(x1: ToComplex64_1d, x2: ToComplex64_1d, /) -> Array_2d[np.complex64]: ...
@overload
def outer(x1: ToObject_1d, x2: ToObject_1d, /) -> Array_2d[np.object_]: ...
@overload
def outer(x1: ToInteger_1d, x2: CoInteger_1d, /) -> Array_2d[np.integer]: ...
@overload
def outer(x1: CoInteger_1d, x2: ToInteger_1d, /) -> Array_2d[np.integer]: ...
@overload
def outer(x1: ToNumber_1d, x2: ToNumber_1d, /) -> Array_2d[Any]: ...

#
@overload
def multi_dot(arrays: Iterable[_ToArray1_1ds[_AnyNumberT]], *, out: None = None) -> _AnyNumberT: ...  # type: ignore[overload-overlap]
@overload
def multi_dot(arrays: Iterable[_ToArray1_2nd[_AnyNumberT]], *, out: None = None) -> Array[_AnyNumberT]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[bool]], *, out: None = None) -> np.bool: ...
@overload
def multi_dot(arrays: Iterable[Sequence_2nd[bool]], *, out: None = None) -> Array[np.bool]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[Is[int]]], *, out: None = None) -> np.intp: ...
@overload
def multi_dot(arrays: Iterable[Sequence_2nd[Is[int]]], *, out: None = None) -> Array[np.intp]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[Is[float]]], *, out: None = None) -> np.float64: ...
@overload
def multi_dot(arrays: Iterable[Sequence_2nd[Is[float]]], *, out: None = None) -> Array[np.float64]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[Is[complex]]], *, out: None = None) -> np.complex128: ...
@overload
def multi_dot(arrays: Iterable[Sequence_2nd[Is[complex]]], *, out: None = None) -> Array[np.complex128]: ...
@overload
def multi_dot(arrays: Iterable[CoComplex_1nd], *, out: _ArrayT) -> _ArrayT: ...
@overload
def multi_dot(arrays: Iterable[CoComplex_1nd | ToTimeDelta_1nd | ToObject_1nd], *, out: None = None) -> Any: ...

# pyright false positive in case of typevar constraints
@overload
def cross(  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    x1: _ToArray1_1nd[_AnyNumberT],
    x2: _ToArray1_1nd[_AnyNumberT],
    /,
    *,
    axis: int = -1,
) -> Array[_AnyNumberT]: ...
@overload
def cross(x1: CoBool_1nd, x2: CoBool_1nd, /, *, axis: int = -1) -> Array[np.bool]: ...
@overload
def cross(x1: ToIntP_1nd, x2: CoIntP_1nd, /, *, axis: int = -1) -> Array[np.intp]: ...
@overload
def cross(x1: CoIntP_1nd, x2: ToIntP_1nd, /, *, axis: int = -1) -> Array[np.intp]: ...
@overload
def cross(x1: ToFloat64_1nd, x2: CoFloat64_1nd, /, *, axis: int = -1) -> Array[np.float64]: ...
@overload
def cross(x1: CoFloat64_1nd, x2: ToFloat64_1nd, /, *, axis: int = -1) -> Array[np.float64]: ...
@overload
def cross(x1: ToComplex128_1nd, x2: CoComplex128_1nd, /, *, axis: int = -1) -> Array[np.complex128]: ...
@overload
def cross(x1: CoComplex128_1nd, x2: ToComplex128_1nd, /, *, axis: int = -1) -> Array[np.complex128]: ...
@overload
def cross(x1: ToInteger_1nd, x2: CoInteger_1nd, /, *, axis: int = -1) -> Array[np.integer]: ...
@overload
def cross(x1: CoInteger_1nd, x2: ToInteger_1nd, /, *, axis: int = -1) -> Array[np.integer]: ...
@overload
def cross(x1: ToFloating_1nd, x2: CoFloating_1nd, /, *, axis: int = -1) -> Array[np.floating]: ...
@overload
def cross(x1: CoFloating_1nd, x2: ToFloating_1nd, /, *, axis: int = -1) -> Array[np.floating]: ...
@overload
def cross(x1: ToComplex_1nd, x2: CoComplex_1nd, /, *, axis: int = -1) -> Array[np.complexfloating]: ...
@overload
def cross(x1: CoComplex_1nd, x2: ToComplex_1nd, /, *, axis: int = -1) -> Array[np.complexfloating]: ...
@overload
def cross(x1: CoComplex_1nd, x2: CoComplex_1nd, /, *, axis: int = -1) -> Array[Any]: ...

# pyright false positive in case of typevar constraints
@overload
def matmul(x1: _ToArray1_1ds[_AnyNumberT], x2: _ToArray1_1ds[_AnyNumberT], /) -> _AnyNumberT: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: _ToArray1_2nd[_AnyNumberT], x2: _ToArray1_1nd[_AnyNumberT], /) -> Array[_AnyNumberT]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: _ToArray1_1nd[_AnyNumberT], x2: _ToArray1_2nd[_AnyNumberT], /) -> Array[_AnyNumberT]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: ToBool_1ds, x2: ToBool_1ds, /) -> np.bool: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToBool_2nd, x2: ToBool_1nd, /) -> Array[np.bool]: ...
@overload
def matmul(x1: ToBool_1nd, x2: ToBool_2nd, /) -> Array[np.bool]: ...
@overload
def matmul(x1: ToIntP_1ds, x2: CoIntP_1ds, /) -> np.intp: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoIntP_1ds, x2: ToIntP_1ds, /) -> np.intp: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToIntP_2nd, x2: CoIntP_1nd, /) -> Array[np.intp]: ...
@overload
def matmul(x1: CoIntP_1nd, x2: ToIntP_2nd, /) -> Array[np.intp]: ...
@overload
def matmul(x1: ToFloat64_1ds, x2: CoFloat64_1ds, /) -> np.float64: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoFloat64_1ds, x2: ToFloat64_1ds, /) -> np.float64: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToFloat64_2nd, x2: CoFloat64_1nd, /) -> Array[np.float64]: ...
@overload
def matmul(x1: CoFloat64_1nd, x2: ToFloat64_2nd, /) -> Array[np.float64]: ...
@overload
def matmul(x1: ToComplex128_1ds, x2: CoComplex128_1ds, /) -> np.complex128: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoComplex128_1ds, x2: ToComplex128_1ds, /) -> np.complex128: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToComplex128_2nd, x2: CoComplex128_1nd, /) -> Array[np.complex128]: ...
@overload
def matmul(x1: CoComplex128_1nd, x2: ToComplex128_2nd, /) -> Array[np.complex128]: ...
@overload
def matmul(x1: ToInteger_1ds, x2: CoInteger_1ds, /) -> np.integer: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoInteger_1ds, x2: ToInteger_1ds, /) -> np.integer: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToInteger_2nd, x2: CoInteger_1nd, /) -> Array[np.integer]: ...
@overload
def matmul(x1: CoInteger_1nd, x2: ToInteger_2nd, /) -> Array[np.integer]: ...
@overload
def matmul(x1: ToFloating_1ds, x2: CoFloating_1ds, /) -> np.floating: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoFloating_1ds, x2: ToFloating_1ds, /) -> np.floating: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToFloating_2nd, x2: CoFloating_1nd, /) -> Array[np.floating]: ...
@overload
def matmul(x1: CoFloating_1nd, x2: ToFloating_2nd, /) -> Array[np.floating]: ...
@overload
def matmul(x1: ToComplex_1ds, x2: CoComplex_1ds, /) -> np.complexfloating: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: CoComplex_1ds, x2: ToComplex_1ds, /) -> np.complexfloating: ...  # type: ignore[overload-overlap]
@overload
def matmul(x1: ToComplex_2nd, x2: CoComplex_1nd, /) -> Array[np.complexfloating]: ...
@overload
def matmul(x1: CoComplex_1nd, x2: ToComplex_2nd, /) -> Array[np.complexfloating]: ...
@overload
def matmul(x1: CoComplex_2nd, x2: CoComplex_1nd, /) -> Array[Any]: ...
@overload
def matmul(x1: CoComplex_1nd, x2: CoComplex_2nd, /) -> Array[Any]: ...
@overload
def matmul(x1: CoComplex_1nd, x2: CoComplex_1nd, /) -> Any: ...

#
@overload  # float64
def eig(a: _ToFloat64_1nd) -> EigResult[np.float64] | EigResult[np.complex128]: ...
@overload  # complex128
def eig(a: ToComplex128_1nd) -> EigResult[np.complex128]: ...
@overload  # complex64
def eig(a: ToComplex64_1nd) -> EigResult[np.complex64]: ...
@overload  # float32
def eig(a: ToFloat32_1nd) -> EigResult[np.float32] | EigResult[np.complex64]: ...
@overload  # +complex128
def eig(a: CoComplex128_1nd) -> EigResult: ...

#
@overload  # float64
def eigvals(a: _ToFloat64_1nd) -> Array[np.float64] | Array[np.complex128]: ...
@overload  # complex128
def eigvals(a: ToComplex128_1nd) -> Array[np.complex128]: ...
@overload  # complex64
def eigvals(a: ToComplex64_1nd) -> Array[np.complex64]: ...
@overload  # float32
def eigvals(a: ToFloat32_1nd) -> Array[np.float32] | Array[np.complex64]: ...
@overload  # +complex128
def eigvals(a: CoComplex128_1nd) -> Array[np.inexact]: ...

#
@overload  # float64
def eigh(a: _ToFloat64_1nd, UPLO: _UPLO = "L") -> EighResult[np.float64, np.float64]: ...
@overload  # complex128
def eigh(a: ToComplex128_1nd, UPLO: _UPLO = "L") -> EighResult[np.float64, np.complex128]: ...
@overload  # float32
def eigh(a: ToFloat32_1nd, UPLO: _UPLO = "L") -> EighResult[np.float32, np.float32]: ...
@overload  # complex64
def eigh(a: ToComplex64_1nd, UPLO: _UPLO = "L") -> EighResult[np.float32, np.complex64]: ...
@overload  # +complex128
def eigh(a: CoComplex128_1nd, UPLO: _UPLO = "L") -> EighResult: ...

#
@overload  # float64 | complex128
def eigvalsh(a: _ToInexact64_1nd, UPLO: _UPLO = "L") -> Array[np.float64]: ...
@overload  # float32 | complex64
def eigvalsh(a: _ToInexact32_1nd, UPLO: _UPLO = "L") -> Array[np.float32]: ...
@overload  # +complex128
def eigvalsh(a: CoComplex128_1nd, UPLO: _UPLO = "L") -> Array[np.floating]: ...

#
@overload  # float64, reduced|complete
def qr(a: _ToFloat64_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.float64]: ...
@overload  # float64, raw
def qr(a: _ToFloat64_1nd, mode: L["raw"]) -> _2Tuple[_Array_2nd[np.float64]]: ...
@overload  # float64, r
def qr(a: _ToFloat64_1nd, mode: L["r"]) -> _Array_2nd[np.float64]: ...
@overload  # complex128, reduced|complete
def qr(a: ToComplex128_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.complex128]: ...
@overload  # complex128, raw
def qr(a: ToComplex128_1nd, mode: L["raw"]) -> _2Tuple[_Array_2nd[np.complex128]]: ...
@overload  # complex128, r
def qr(a: ToComplex128_1nd, mode: L["r"]) -> _Array_2nd[np.complex128]: ...
@overload  # float32, reduced|complete
def qr(a: ToFloat32_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.float32]: ...
@overload  # float32, raw
def qr(a: ToFloat32_1nd, mode: L["raw"]) -> _2Tuple[_Array_2nd[np.float32]]: ...
@overload  # float32, r
def qr(a: ToFloat32_1nd, mode: L["r"]) -> _Array_2nd[np.float32]: ...
@overload  # complex64, reduced|complete
def qr(a: ToComplex64_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.complex64]: ...
@overload  # complex64, raw
def qr(a: ToComplex64_1nd, mode: L["raw"]) -> _2Tuple[_Array_2nd[np.complex64]]: ...
@overload  # complex64, r
def qr(a: ToComplex64_1nd, mode: L["r"]) -> _Array_2nd[np.complex64]: ...
@overload  # +complex128, reduced|complete
def qr(a: CoComplex128_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.inexact]: ...
@overload  # +complex128, raw
def qr(a: CoComplex128_1nd, mode: L["raw"]) -> _2Tuple[_Array_2nd[np.inexact]]: ...
@overload  # +complex128, r
def qr(a: CoComplex128_1nd, mode: L["r"]) -> _Array_2nd[np.inexact]: ...

#
@overload  # float64 | complex128, compute_uv=False (positional)
def svd(
    a: _ToInexact64_1nd,
    full_matrices: bool,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.float64]: ...
@overload  # float64 | complex128, compute_uv=False (keyword)
def svd(
    a: _ToInexact64_1nd,
    full_matrices: bool = True,
    *,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.float64]: ...
@overload  # float64, compute_uv=True
def svd(
    a: _ToFloat64_1nd,
    full_matrices: bool = True,
    compute_uv: _True = True,
    hermitian: bool = False,
) -> SVDResult[np.float64, np.float64]: ...
@overload  # complex128, compute_uv=True
def svd(
    a: ToComplex128_1nd,
    full_matrices: bool = True,
    compute_uv: _True = True,
    hermitian: bool = False,
) -> SVDResult[np.float64, np.complex128]: ...
@overload  # float32, compute_uv=True
def svd(
    a: ToFloat32_1nd,
    full_matrices: bool = True,
    compute_uv: _True = True,
    hermitian: bool = False,
) -> SVDResult[np.float32, np.float32]: ...
@overload  # float32 | complex64, compute_uv=False (positional)
def svd(
    a: _ToInexact32_1nd,
    full_matrices: bool,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.float32]: ...
@overload  # float32 | complex64, compute_uv=False (keyword)
def svd(
    a: _ToInexact32_1nd,
    full_matrices: bool = True,
    *,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.float32]: ...
@overload  # complex64, compute_uv=True
def svd(
    a: ToComplex64_1nd,
    full_matrices: bool = True,
    compute_uv: _True = True,
    hermitian: bool = False,
) -> SVDResult[np.float32, np.complex64]: ...
@overload  # +complex128, compute_uv=True
def svd(
    a: CoComplex128_1nd,
    full_matrices: bool = True,
    compute_uv: _True = True,
    hermitian: bool = False,
) -> SVDResult: ...
@overload  # +complex128, compute_uv=False (positional)
def svd(
    a: CoComplex128_1nd,
    full_matrices: bool,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.floating]: ...
@overload  # +complex128, compute_uv=False (keyword)
def svd(
    a: CoComplex128_1nd,
    full_matrices: bool = True,
    *,
    compute_uv: _False,
    hermitian: bool = False,
) -> Array[np.floating]: ...

#
@overload  # float64 | complex128
def svdvals(x: _ToInexact64_1nd, /) -> Array[np.float64]: ...
@overload  # floaat32 | complex64
def svdvals(x: _ToInexact32_1nd, /) -> Array[np.float32]: ...
@overload  # +complex128
def svdvals(x: CoComplex128_1nd, /) -> Array[np.floating]: ...

#
@overload  # <2d +complex128
def matrix_rank(
    A: CoComplex128_0d | CoComplex128_1ds,
    tol: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> L[0, 1]: ...
@overload  # 2d +complex128
def matrix_rank(  # type: ignore[overload-overlap]
    A: CoComplex128_2ds,
    tol: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> np.intp: ...
@overload  # >2d +complex128
def matrix_rank(
    A: CoComplex128_3nd,
    tol: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> Array[np.intp]: ...
@overload  # nd +complex128
def matrix_rank(
    A: CoComplex128_nd,
    tol: ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: ToFloating_nd | None = None,
) -> Any: ...

#
@overload  # 2d float64 | complex128
def cond(x: _ToInexact64_2ds, p: _Ord | None = None) -> np.float64: ...  # type: ignore[overload-overlap]
@overload  # 2d float32 | complex64
def cond(x: _ToInexact32_2ds, p: _Ord | None = None) -> np.float32: ...  # type: ignore[overload-overlap]
@overload  # 2d +complex128
def cond(x: CoComplex128_2ds, p: _Ord | None = None) -> np.floating: ...  # type: ignore[overload-overlap]
@overload  # >2d float64 | complex128
def cond(x: _ToInexact64_3nd, p: _Ord | None = None) -> Array[np.float64]: ...
@overload  # >2d float32 | complex64
def cond(x: _ToInexact32_3nd, p: _Ord | None = None) -> Array[np.float32]: ...
@overload  # >2d +complex128
def cond(x: CoComplex128_3nd, p: _Ord | None = None) -> Array[np.floating]: ...
@overload  # +complex128
def cond(x: CoComplex128_1nd, p: _Ord | None = None) -> Any: ...

# keep in sync with `det`
@overload  # 2d float64
def slogdet(a: _ToFloat64_2ds) -> SlogdetResult[np.float64, np.float64]: ...  # type: ignore[overload-overlap]
@overload  # 2d float32
def slogdet(a: ToFloat32_2ds) -> SlogdetResult[np.float32, np.float32]: ...  # type: ignore[overload-overlap]
@overload  # 2d complex128
def slogdet(a: ToComplex128_2ds) -> SlogdetResult[np.float64, np.complex128]: ...  # type: ignore[overload-overlap]
@overload  # 2d complex64
def slogdet(a: ToComplex64_2ds) -> SlogdetResult[np.float32, np.complex64]: ...  # type: ignore[overload-overlap]
@overload  # >2d float64
def slogdet(a: _ToFloat64_3nd) -> SlogdetResult[Array[np.float64], Array[np.float64]]: ...
@overload  # >2d float32
def slogdet(a: ToFloat32_3nd) -> SlogdetResult[Array[np.float32], Array[np.float32]]: ...
@overload  # >2d complex128
def slogdet(a: ToComplex128_3nd) -> SlogdetResult[Array[np.float64], Array[np.complex128]]: ...
@overload  # >2d complex64
def slogdet(a: ToComplex64_3nd) -> SlogdetResult[Array[np.float32], Array[np.complex64]]: ...
@overload  # +complex128
def slogdet(a: CoComplex128_1nd) -> SlogdetResult[Any, Any]: ...

#
@overload  # 2d float64
def det(a: _ToFloat64_2ds) -> np.float64: ...  # type: ignore[overload-overlap]
@overload  # 2d float32
def det(a: ToFloat32_2ds) -> np.float32: ...  # type: ignore[overload-overlap]
@overload  # 2d complex128
def det(a: ToComplex128_2ds) -> np.complex128: ...  # type: ignore[overload-overlap]
@overload  # 2d complex64
def det(a: ToComplex64_2ds) -> np.complex64: ...  # type: ignore[overload-overlap]
@overload  # >2d float64
def det(a: _ToFloat64_3nd) -> Array[np.float64]: ...
@overload  # >2d float32
def det(a: ToFloat32_3nd) -> Array[np.float32]: ...
@overload  # >2d complex128
def det(a: ToComplex128_3nd) -> Array[np.complex128]: ...
@overload  # >2d complex64
def det(a: ToComplex64_3nd) -> Array[np.complex64]: ...
@overload  # +complex128
def det(a: CoComplex128_1nd) -> Any: ...

#
@overload  # float64, +float64
def lstsq(a: _ToFloat64_1nd, b: CoFloat64_1nd, rcond: float | None = None) -> _LstSqResult[np.float64, np.float64]: ...
@overload  # +float64, float64
def lstsq(a: CoFloat64_1nd, b: _ToFloat64_1nd, rcond: float | None = None) -> _LstSqResult[np.float64, np.float64]: ...
@overload  # float32, float32
def lstsq(a: ToFloat32_1nd, b: ToFloat32_1nd, rcond: float | None = None) -> _LstSqResult[np.float32, np.float32]: ...
@overload  # complex128, +complex128
def lstsq(  # type: ignore[overload-overlap]
    a: ToComplex128_1nd,
    b: CoComplex128_1nd,
    rcond: float | None = None,
) -> _LstSqResult[np.complex128, np.float64]: ...
@overload  # +complex128, complex128
def lstsq(  # type: ignore[overload-overlap]
    a: CoComplex128_1nd,
    b: ToComplex128_1nd,
    rcond: float | None = None,
) -> _LstSqResult[np.complex128, np.float64]: ...
@overload  # complex64, +complex64
def lstsq(
    a: ToComplex64_1nd,
    b: CoComplex64_1nd,
    rcond: float | None = None,
) -> _LstSqResult[np.complex64, np.float32]: ...
@overload  # +complex64, complex64
def lstsq(
    a: CoComplex64_1nd,
    b: ToComplex64_1nd,
    rcond: float | None = None,
) -> _LstSqResult[np.complex64, np.float32]: ...
@overload  # +complex128, +complex128
def lstsq(
    a: CoComplex128_1nd,
    b: CoComplex128_1nd,
    rcond: float | None = None,
) -> _LstSqResult[np.inexact, np.floating]: ...

#
@overload  # float64 | complex128 | character, axis=None, keepdims=False
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float64: ...
@overload  # float64 | complex128 | character, keepdims=True (keyword)
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True) -> _Array_2nd[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # float64 | complex128 | character, axis=<given> (positional)
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> Array[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # float64 | complex128 | character, axis=<given> (keyword)
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False) -> Array[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # float16, axis=None, keepdims=False
def norm(x: ToFloat16_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float16: ...
@overload  # float16, keepdims=True (keyword)
def norm(x: ToFloat16_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True) -> _Array_2nd[np.float16]: ...
@overload  # float16, axis=<given> (keyword)
def norm(x: ToFloat16_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False) -> Array[np.float16]: ...  # type: ignore[overload-overlap]
@overload  # float32 | complex64, axis=None, keepdims=False
def norm(x: _ToInexact32_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float32: ...
@overload  # float32 | complex64, keepdims=True (keyword)
def norm(
    x: _ToInexact32_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array_2nd[np.float32]: ...
@overload  # float32 | complex64, axis=<given> (positional)
def norm(x: _ToInexact32_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> Array[np.float32]: ...  # type: ignore[overload-overlap]
@overload  # float32 | complex64, axis=<given> (keyword)
def norm(x: _ToInexact32_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False) -> Array[np.float32]: ...  # type: ignore[overload-overlap]
@overload  # longdouble | clongdouble, axis=None, keepdims=False
def norm(x: _ToInexactLD_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.longdouble: ...
@overload  # longdouble | clongdouble, keepdims=True (keyword)
def norm(
    x: _ToInexactLD_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array_2nd[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given> (positional)
def norm(x: _ToInexactLD_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> Array[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given> (keyword)
def norm(x: _ToInexactLD_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False) -> Array[np.longdouble]: ...
@overload  # +number, axis=None, keepdims=False
def norm(x: CoComplex_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.floating: ...
@overload  # +number, keepdims=True
def norm(x: CoComplex_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True) -> _Array_2nd[np.floating]: ...
@overload  # +number, axis=<given> (positional)
def norm(x: CoComplex_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> Array[np.floating]: ...
@overload  # +number, axis=<given> (keyword)
def norm(x: CoComplex_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False) -> Array[np.floating]: ...
@overload  # +number
def norm(x: CoComplex_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, keepdims: bool = False) -> Any: ...

#
@overload  # 2d float64 | complex128 | character
def matrix_norm(x: _ToUnsafe64_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float64: ...  # type: ignore[overload-overlap]
@overload  # nd float64 | complex128 | character, keepdims=True
def matrix_norm(x: _ToUnsafe64_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array_2nd[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # >2d float64 | complex128 | character
def matrix_norm(x: _ToUnsafe64_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Array[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # 2d float16
def matrix_norm(x: ToFloat16_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float16: ...  # type: ignore[overload-overlap]
@overload  # nd float16, keepdims=True
def matrix_norm(x: ToFloat16_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array_2nd[np.float16]: ...  # type: ignore[overload-overlap]
@overload  # >2d float16
def matrix_norm(x: ToFloat16_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Array[np.float16]: ...  # type: ignore[overload-overlap]
@overload  # 2d float32 | complex64, keepdims=True
def matrix_norm(x: _ToInexact32_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float32: ...  # type: ignore[overload-overlap]
@overload  # nd float32 | complex64, keepdims=True
def matrix_norm(x: _ToInexact32_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array_2nd[np.float32]: ...  # type: ignore[overload-overlap]
@overload  # >2d float32 | complex64
def matrix_norm(x: _ToInexact32_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Array[np.float32]: ...  # type: ignore[overload-overlap]
@overload  # 2d longdouble | clongdouble
def matrix_norm(x: _ToInexactLD_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.longdouble: ...  # type: ignore[overload-overlap]
@overload  # nd longdouble | clongdouble, keepdims=True
def matrix_norm(x: _ToInexactLD_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array_2nd[np.longdouble]: ...
@overload  # >2d longdouble | clongdouble
def matrix_norm(x: _ToInexactLD_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Array[np.longdouble]: ...
@overload  # 2d +number
def matrix_norm(x: CoComplex_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.floating: ...  # type: ignore[overload-overlap]
@overload  # nd +number, keepdims=True
def matrix_norm(x: CoComplex_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array_2nd[np.floating]: ...
@overload  # >2d +number
def matrix_norm(x: CoComplex_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Array[np.floating]: ...
@overload  # nd +number
def matrix_norm(x: CoComplex_1nd | ToCharacter_1nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Any: ...

#
@overload  # float64 | complex128 | character, axis=None, keepdims=False
def vector_norm(x: _ToUnsafe64_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2) -> np.float64: ...
@overload  # float64 | complex128 | character, keepdims=True
def vector_norm(x: _ToUnsafe64_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2) -> Array[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # float64 | complex128 | character, axis=<given>
def vector_norm(x: _ToUnsafe64_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2) -> Array[np.float64]: ...  # type: ignore[overload-overlap]
@overload  # float16, axis=None, keepdims=False
def vector_norm(x: ToFloat16_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2) -> np.float16: ...
@overload  # float16, keepdims=True
def vector_norm(x: ToFloat16_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2) -> Array[np.float16]: ...
@overload  # float16, axis=<given>
def vector_norm(x: ToFloat16_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2) -> Array[np.float16]: ...
@overload  # float32 | complex64, axis=None, keepdims=False
def vector_norm(x: _ToInexact32_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2) -> np.float32: ...
@overload  # float32 | complex64, keepdims=True
def vector_norm(x: _ToInexact32_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2) -> Array[np.float32]: ...
@overload  # float32 | complex64, axis=<given>
def vector_norm(x: _ToInexact32_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2) -> Array[np.float32]: ...
@overload  # longdouble | clongdouble, axis=None, keepdims=False
def vector_norm(x: _ToInexactLD_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2) -> np.longdouble: ...
@overload  # longdouble | clongdouble, keepdims=True
def vector_norm(x: _ToInexactLD_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2) -> Array[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given>
def vector_norm(x: _ToInexactLD_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2) -> Array[np.longdouble]: ...
@overload  # +number, axis=None, keepdims=False
def vector_norm(x: CoComplex_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2) -> np.floating: ...
@overload  # +number, keepdims=True
def vector_norm(x: CoComplex_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2) -> Array[np.floating]: ...
@overload  # +number, axis=<given>
def vector_norm(x: CoComplex_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2) -> Array[np.floating]: ...
@overload  # +number
def vector_norm(x: CoComplex_1nd, /, *, axis: _Ax2 | None = None, keepdims: bool = False, ord: float = 2) -> Any: ...

#
@overload
def diagonal(x: Sequence_2nd[ToObject_0d], /, *, offset: CanIndex = 0) -> Array[np.object_]: ...
@overload
def diagonal(x: _ToArray1_2ds[_ScalarT], /, *, offset: CanIndex = 0) -> Array[_ScalarT, tuple[int]]: ...
@overload
def diagonal(x: _ToArray_2nd_ish[_ScalarT], /, *, offset: CanIndex = 0) -> Array[_ScalarT]: ...
@overload
def diagonal(x: Sequence_2nd[bool], /, *, offset: CanIndex = 0) -> Array[np.bool]: ...
@overload
def diagonal(x: Sequence_2nd[Is[int]], /, *, offset: CanIndex = 0) -> Array[np.int_]: ...
@overload
def diagonal(x: Sequence_2nd[Is[float]], /, *, offset: CanIndex = 0) -> Array[np.float64]: ...
@overload
def diagonal(x: Sequence_2nd[Is[complex]], /, *, offset: CanIndex = 0) -> Array[np.complex128]: ...
@overload
def diagonal(x: Sequence_2nd[Is[bytes]], /, *, offset: CanIndex = 0) -> Array[np.bytes_]: ...
@overload
def diagonal(x: Sequence_2nd[Is[str]], /, *, offset: CanIndex = 0) -> Array[np.str_]: ...
@overload
def diagonal(x: ToGeneric_1nd, /, *, offset: CanIndex = 0) -> Array[Any]: ...

#
@overload
def trace(x: _ToArray1_2ds[_ScalarT], /, *, offset: CanIndex = 0, dtype: None = None) -> _ScalarT: ...  # type: ignore[overload-overlap]
@overload
def trace(x: _ToArray1_3nd[_ScalarT], /, *, offset: CanIndex = 0, dtype: None = None) -> Array[_ScalarT]: ...
@overload
def trace(x: Sequence_2d[bool], /, *, offset: CanIndex = 0, dtype: None = None) -> np.bool: ...
@overload
def trace(x: Sequence_3nd[bool], /, *, offset: CanIndex = 0, dtype: None = None) -> Array[np.bool]: ...
@overload
def trace(x: Sequence_2d[Is[int]], /, *, offset: CanIndex = 0, dtype: None = None) -> np.int_: ...
@overload
def trace(x: Sequence_3nd[Is[int]], /, *, offset: CanIndex = 0, dtype: None = None) -> Array[np.int_]: ...
@overload
def trace(x: Sequence_2d[Is[float]], /, *, offset: CanIndex = 0, dtype: None = None) -> np.float64: ...
@overload
def trace(x: Sequence_3nd[Is[float]], /, *, offset: CanIndex = 0, dtype: None = None) -> Array[np.float64]: ...
@overload
def trace(x: Sequence_2d[Is[complex]], /, *, offset: CanIndex = 0, dtype: None = None) -> np.complex128: ...
@overload
def trace(x: Sequence_3nd[Is[complex]], /, *, offset: CanIndex = 0, dtype: None = None) -> Array[np.complex128]: ...
@overload
def trace(x: CoComplex_2ds, /, *, offset: CanIndex = 0, dtype: _ToDType[_ScalarT]) -> _ScalarT: ...  # type: ignore[overload-overlap]
@overload
def trace(x: CoComplex_3nd, /, *, offset: CanIndex = 0, dtype: _ToDType[_ScalarT]) -> Array[_ScalarT]: ...
@overload
def trace(x: CoComplex_3nd, /, *, offset: CanIndex = 0, dtype: DTypeLike | None = None) -> Array[Any]: ...
@overload
def trace(x: CoComplex_1nd, /, *, offset: CanIndex = 0, dtype: DTypeLike | None = None) -> Any: ...
