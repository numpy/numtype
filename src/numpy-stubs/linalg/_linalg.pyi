from collections.abc import Iterable, Sequence
from typing import Any, Generic, Literal as L, NamedTuple, SupportsIndex as CanIndex, SupportsInt, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._core.fromnumeric import matrix_transpose
from numpy._core.numeric import vecdot
from numpy._globals import _NoValueType
from numpy._typing import DTypeLike, _DTypeLike as _ToDType

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

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=_nt.Array[Any])
_Shape2NDT = TypeVar("_Shape2NDT", bound=_nt.Shape2N)

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_IntegerT = TypeVar("_IntegerT", bound=np.integer)
_FloatingT = TypeVar("_FloatingT", bound=np.floating)
_NumberT = TypeVar("_NumberT", bound=np.number)
_NativeScalarT = TypeVar(
    "_NativeScalarT", bound=_nt.co_number | np.flexible | np.datetime64 | np.timedelta64
)  # no object_
_Inexact32T = TypeVar("_Inexact32T", bound=_nt.inexact32)

_FloatingT_co = TypeVar("_FloatingT_co", bound=np.floating, default=np.floating, covariant=True)
_InexactT_co = TypeVar("_InexactT_co", bound=np.inexact, default=Any, covariant=True)

_FloatingNDT_co = TypeVar("_FloatingNDT_co", bound=np.floating | _nt.Array[np.floating], default=Any, covariant=True)
_InexactNDT_co = TypeVar("_InexactNDT_co", bound=np.inexact | _nt.Array[np.inexact], default=Any, covariant=True)

_AnyNumberT = TypeVar(
    "_AnyNumberT",
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.long,
    np.ulong,
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

###

_Option: TypeAlias = _T | _NoValueType

_False: TypeAlias = L[False]
_True: TypeAlias = L[True]

_Tuple2: TypeAlias = tuple[_T, _T]
_ToInt: TypeAlias = SupportsInt | CanIndex

_Ax2: TypeAlias = _ToInt | _Tuple2[_ToInt]
_Axes: TypeAlias = Iterable[int]

_Ord: TypeAlias = L[1, -1, 2, -2, "fro", "nuc"] | float
_UPLO: TypeAlias = L["L", "U", "l", "u"]

_ToArray_2nd_ish: TypeAlias = (
    _nt.CanLenArrayND[_ScalarT] | Sequence[_nt.Sequence1ND[_ScalarT]] | _nt.Sequence1ND[_nt.CanLenArrayND[_ScalarT]]
)

_ToFloat64_1nd: TypeAlias = _nt._ToArray2_1nd[np.float64 | _nt.co_integer, float]
_ToFloat64_2ds: TypeAlias = _nt._ToArray2_2ds[np.float64 | _nt.co_integer, float]
_ToFloat64_3nd: TypeAlias = _nt._ToArray2_3nd[np.float64 | _nt.co_integer, float]

_Toinexact32_1nd: TypeAlias = _nt._ToArray_1nd[_nt.inexact32]
_Toinexact32_2ds: TypeAlias = _nt._ToArray_2ds[_nt.inexact32]
_Toinexact32_3nd: TypeAlias = _nt._ToArray_3nd[_nt.inexact32]

_Toinexact64_1nd: TypeAlias = _nt._ToArray2_1nd[_nt.inexact64 | _nt.co_integer, complex]
_Toinexact64_2ds: TypeAlias = _nt._ToArray2_2ds[_nt.inexact64 | _nt.co_integer, complex]
_Toinexact64_3nd: TypeAlias = _nt._ToArray2_3nd[_nt.inexact64 | _nt.co_integer, complex]

_Toinexact64l_1nd: TypeAlias = _nt._ToArray_1nd[_nt.inexact64l]
_Toinexact64l_2ds: TypeAlias = _nt._ToArray_2ds[_nt.inexact64l]
_Toinexact64l_3nd: TypeAlias = _nt._ToArray_3nd[_nt.inexact64l]

_Unsafe64: TypeAlias = _nt.inexact64 | _nt.co_integer | np.character[Any]
_ToUnsafe64_1nd: TypeAlias = _nt._ToArray2_1nd[_Unsafe64, complex | _nt._PyCharacter]
_ToUnsafe64_2ds: TypeAlias = _nt._ToArray2_2ds[_Unsafe64, complex | _nt._PyCharacter]
_ToUnsafe64_3nd: TypeAlias = _nt._ToArray2_3nd[_Unsafe64, complex | _nt._PyCharacter]

_Array2ND: TypeAlias = _nt.Array[_ScalarT, _nt.Shape2N]

_LstSqResult: TypeAlias = tuple[_nt.Array[_ScalarT], _nt.Array[_FloatingT], np.int32, _nt.Array[_FloatingT]]

###

fortran_int = np.intc

class EigResult(NamedTuple, Generic[_InexactT_co]):
    eigenvalues: _nt.Array[_InexactT_co]
    eigenvectors: _Array2ND[_InexactT_co]

class EighResult(NamedTuple, Generic[_FloatingT_co, _InexactT_co]):
    eigenvalues: _nt.Array[_FloatingT_co]
    eigenvectors: _Array2ND[_InexactT_co]

class QRResult(NamedTuple, Generic[_InexactT_co]):
    Q: _Array2ND[_InexactT_co]
    R: _Array2ND[_InexactT_co]

class SVDResult(NamedTuple, Generic[_FloatingT_co, _InexactT_co]):
    U: _Array2ND[_InexactT_co]
    S: _nt.Array[_FloatingT_co]
    Vh: _Array2ND[_InexactT_co]

class SlogdetResult(NamedTuple, Generic[_FloatingNDT_co, _InexactNDT_co]):
    sign: _InexactNDT_co
    logabsdet: _FloatingNDT_co

class LinAlgError(ValueError): ...

# keep in sync with `numpy._core.numeric.tensordot`
@overload
def tensordot(x1: _nt.ToBool_1nd, x2: _nt.ToBool_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.bool]: ...
@overload
def tensordot(x1: _nt.ToUInteger_1nd, x2: _nt.CoUInt64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.unsignedinteger]: ...
@overload
def tensordot(x1: _nt.CoUInt64_1nd, x2: _nt.ToUInteger_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.unsignedinteger]: ...
@overload
def tensordot(x1: _nt.ToInt64_1nd, x2: _nt.CoInt64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.int64]: ...
@overload
def tensordot(x1: _nt.CoInt64_1nd, x2: _nt.ToInt64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.int64]: ...
@overload
def tensordot(x1: _nt.ToSInteger_1nd, x2: _nt.CoInt64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.signedinteger]: ...
@overload
def tensordot(x1: _nt.CoInt64_1nd, x2: _nt.ToSInteger_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.signedinteger]: ...
@overload
def tensordot(x1: _nt.ToFloat64_1nd, x2: _nt.CoFloat64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.float64]: ...
@overload
def tensordot(x1: _nt.CoFloat64_1nd, x2: _nt.ToFloat64_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.float64]: ...
@overload
def tensordot(x1: _nt.ToFloating_1nd, x2: _nt.CoFloating_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.floating]: ...
@overload
def tensordot(x1: _nt.CoFloating_1nd, x2: _nt.ToFloating_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.floating]: ...
@overload
def tensordot(
    x1: _nt.ToComplex128_1nd, x2: _nt.CoComplex128_1nd, /, *, axes: _Ax2 = 2
) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(
    x1: _nt.CoComplex128_1nd, x2: _nt.ToComplex128_1nd, /, *, axes: _Ax2 = 2
) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(x1: _nt.ToComplex_1nd, x2: _nt.CoComplex_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(x1: _nt.CoComplex_1nd, x2: _nt.ToComplex_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(x1: _nt.ToTimeDelta_1nd, x2: _nt.CoTimeDelta_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.timedelta64]: ...
@overload
def tensordot(x1: _nt.CoTimeDelta_1nd, x2: _nt.ToTimeDelta_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.timedelta64]: ...
@overload
def tensordot(x1: _nt.ToObject_1nd, x2: _nt.ToObject_1nd, /, *, axes: _Ax2 = 2) -> _nt.Array[np.object_]: ...
@overload
def tensordot(
    x1: _nt.CoComplex_1nd | _nt.CoTimeDelta_1nd | _nt.ToObject_1nd,
    x2: _nt.CoComplex_1nd | _nt.CoTimeDelta_1nd | _nt.ToObject_1nd,
    /,
    *,
    axes: _Ax2 = 2,
) -> _nt.Array[Any]: ...

# keep in sync with `solve`
@overload
def tensorsolve(a: _ToFloat64_1nd, b: _nt.CoFloat64_1nd, axes: _Axes | None = None) -> _nt.Array[np.float64]: ...
@overload
def tensorsolve(a: _nt.CoFloat64_1nd, b: _ToFloat64_1nd, axes: _Axes | None = None) -> _nt.Array[np.float64]: ...
@overload
def tensorsolve(
    a: _nt.ToComplex128_1nd, b: _nt.CoComplex128_1nd, axes: _Axes | None = None
) -> _nt.Array[np.complex128]: ...
@overload
def tensorsolve(
    a: _nt.CoComplex128_1nd, b: _nt.ToComplex128_1nd, axes: _Axes | None = None
) -> _nt.Array[np.complex128]: ...
@overload
def tensorsolve(a: _nt.ToFloat32_1nd, b: _nt.ToFloat32_1nd, axes: _Axes | None = None) -> _nt.Array[np.float32]: ...
@overload
def tensorsolve(
    a: _nt.ToComplex64_1nd, b: _nt.ToComplex64_1nd, axes: _Axes | None = None
) -> _nt.Array[np.complex64]: ...
@overload
def tensorsolve(a: _nt.CoComplex128_1nd, b: _nt.CoComplex128_1nd, axes: _Axes | None = None) -> _nt.Array[Any]: ...

# keep in sync with `tensorsolve`
@overload
def solve(a: _ToFloat64_1nd, b: _ToFloat64_1nd) -> _nt.Array[np.float64]: ...
@overload
def solve(a: _nt.ToFloat64_1nd, b: _nt.CoFloat64_1nd) -> _nt.Array[np.float64]: ...
@overload
def solve(a: _nt.CoFloat64_1nd, b: _nt.ToFloat64_1nd) -> _nt.Array[np.float64]: ...
@overload
def solve(a: _nt.ToComplex128_1nd, b: _nt.CoComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def solve(a: _nt.CoComplex128_1nd, b: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload
def solve(a: _nt.ToFloat32_1nd, b: _nt.CoFloat32_1nd) -> _nt.Array[np.float32]: ...
@overload
def solve(a: _nt.CoFloat32_1nd, b: _nt.ToFloat32_1nd) -> _nt.Array[np.float32]: ...
@overload
def solve(a: _nt.ToComplex64_1nd, b: _nt.CoComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def solve(a: _nt.CoComplex64_1nd, b: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload
def solve(a: _nt.CoComplex128_1nd, b: _nt.CoComplex128_1nd) -> _nt.Array[Any]: ...

# TODO(jorenham): increase to `_2nd` once python/mypy#19110 is fixed
# keep in sync with `inv`
@overload
def tensorinv(a: _ToFloat64_1nd, ind: int = 2) -> _Array2ND[np.float64]: ...
@overload
def tensorinv(a: _nt._ToArray_1nd[_Inexact32T], ind: int = 2) -> _Array2ND[_Inexact32T]: ...
@overload
def tensorinv(a: _nt.ToComplex128_1nd, ind: int = 2) -> _Array2ND[np.complex128]: ...
@overload
def tensorinv(a: _nt.CoComplex128_1nd, ind: int = 2) -> _Array2ND[Any]: ...

# keep in sync with `tensorinv`
@overload  # castable to float64
def inv(a: _ToFloat64_1nd) -> _Array2ND[np.float64]: ...
@overload  # float32 | complex64
def inv(a: _nt._ToArray_1nd[_Inexact32T]) -> _Array2ND[_Inexact32T]: ...
@overload  # complex | complex128
def inv(a: _nt.ToComplex128_1nd) -> _Array2ND[np.complex128]: ...
@overload  # fallback
def inv(a: _nt.CoComplex128_1nd) -> _Array2ND[Any]: ...

#
@overload
def pinv(
    a: _ToFloat64_1nd,
    rcond: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _Option[_nt.ToFloating_nd] = ...,
) -> _Array2ND[np.float64]: ...
@overload
def pinv(
    a: _nt.ToComplex128_1nd,
    rcond: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _Option[_nt.ToFloating_nd] = ...,
) -> _Array2ND[np.complex128]: ...
@overload
def pinv(
    a: _nt.ToFloat32_1nd,
    rcond: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _Option[_nt.ToFloating_nd] = ...,
) -> _Array2ND[np.float32]: ...
@overload
def pinv(
    a: _nt.ToComplex64_1nd,
    rcond: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _Option[_nt.ToFloating_nd] = ...,
) -> _Array2ND[np.complex64]: ...
@overload
def pinv(
    a: _nt.CoComplex128_1nd,
    rcond: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _Option[_nt.ToFloating_nd] = ...,
) -> _Array2ND[Any]: ...

_PosInt: TypeAlias = L[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
_NegInt: TypeAlias = L[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16]

#
@overload  # workaround for microsoft/pyright#10232
def matrix_power(a: _nt.CastsArray[np.float64, _nt.NeitherShape], n: CanIndex) -> _Array2ND[np.float64]: ...
@overload  # workaround for microsoft/pyright#10232
def matrix_power(a: _nt.CastsWithArray[np.float64, _NumberT, _nt.NeitherShape], n: CanIndex) -> _Array2ND[_NumberT]: ...
@overload
def matrix_power(a: _nt.CanLenArray[_NumberT, _Shape2NDT], n: _PosInt) -> _nt.Array[_NumberT, _Shape2NDT]: ...
@overload
def matrix_power(a: _nt.ToBool_1nd, n: _PosInt) -> _Array2ND[np.bool]: ...
@overload
def matrix_power(a: _nt.ToInt_1nd, n: _PosInt) -> _Array2ND[np.intp]: ...
@overload
def matrix_power(a: _nt.CoInteger_1nd, n: _NegInt) -> _Array2ND[np.float64]: ...
@overload
def matrix_power(a: _nt.ToFloat64_1nd, n: CanIndex) -> _Array2ND[np.float64]: ...
@overload
def matrix_power(a: _nt.ToComplex128_1nd, n: CanIndex) -> _Array2ND[np.complex128]: ...
@overload
def matrix_power(a: _nt._ToArray_1nd[_Inexact32T], n: CanIndex) -> _Array2ND[_Inexact32T]: ...
@overload
def matrix_power(a: _nt.ToObject_1nd, n: CanIndex) -> _Array2ND[np.object_]: ...
@overload
def matrix_power(a: _nt.ToUInteger_1nd, n: _PosInt) -> _Array2ND[np.unsignedinteger]: ...
@overload
def matrix_power(a: _nt.ToInteger_1nd, n: _PosInt) -> _Array2ND[np.integer]: ...
@overload
def matrix_power(a: _nt.CoComplex_1nd | _nt.ToObject_1nd, n: CanIndex) -> _Array2ND[Any]: ...

#
@overload
def cholesky(a: _ToFloat64_1nd, /, *, upper: bool = False) -> _Array2ND[np.float64]: ...
@overload
def cholesky(a: _nt._ToArray_1nd[_Inexact32T], /, *, upper: bool = False) -> _Array2ND[_Inexact32T]: ...
@overload
def cholesky(a: _nt.ToComplex128_1nd, /, *, upper: bool = False) -> _Array2ND[np.complex128]: ...
@overload
def cholesky(a: _nt.CoComplex128_1nd, /, *, upper: bool = False) -> _Array2ND[Any]: ...

#
@overload
def outer(x1: _nt.ToBool_1d, x2: _nt.ToBool_1d, /) -> _nt.Array2D[np.bool]: ...
@overload
def outer(x1: _nt.ToInt_1d, x2: _nt.CoInt64_1d, /) -> _nt.Array2D[np.intp]: ...
@overload
def outer(x1: _nt.CoInt64_1d, x2: _nt.ToInt_1d, /) -> _nt.Array2D[np.intp]: ...
@overload
def outer(x1: _nt._ToArray_1d[_IntegerT], x2: _nt._ToArray_1d[_IntegerT], /) -> _nt.Array2D[_IntegerT]: ...
@overload
def outer(x1: _nt.ToFloat32_1d, x2: _nt.ToFloat32_1d, /) -> _nt.Array2D[np.float32]: ...
@overload
def outer(x1: _nt.ToFloat64_1d, x2: _nt.CoFloat64_1d, /) -> _nt.Array2D[np.float64]: ...
@overload
def outer(x1: _nt.CoFloat64_1d, x2: _nt.ToFloat64_1d, /) -> _nt.Array2D[np.float64]: ...
@overload
def outer(x1: _nt.ToComplex64_1d, x2: _nt.ToComplex64_1d, /) -> _nt.Array2D[np.complex64]: ...
@overload
def outer(x1: _nt.ToComplex128_1d, x2: _nt.CoComplex128_1d, /) -> _nt.Array2D[np.complex128]: ...
@overload
def outer(x1: _nt.CoComplex128_1d, x2: _nt.ToComplex128_1d, /) -> _nt.Array2D[np.complex128]: ...
@overload
def outer(x1: _nt.ToTimeDelta_1d, x2: _nt.CoTimeDelta_1d, /) -> _nt.Array2D[np.timedelta64]: ...
@overload
def outer(x1: _nt.CoTimeDelta_1d, x2: _nt.ToTimeDelta_1d, /) -> _nt.Array2D[np.timedelta64]: ...
@overload
def outer(x1: _nt.ToObject_1d, x2: _nt.ToObject_1d, /) -> _nt.Array2D[np.object_]: ...
@overload
def outer(x1: _nt.ToInteger_1d, x2: _nt.CoInteger_1d, /) -> _nt.Array2D[np.integer]: ...
@overload
def outer(x1: _nt.CoInteger_1d, x2: _nt.ToInteger_1d, /) -> _nt.Array2D[np.integer]: ...
@overload
def outer(x1: _nt.ToNumber_1d, x2: _nt.ToNumber_1d, /) -> _nt.Array2D[Any]: ...

#
@overload  # workaround for microsoft/pyright#10232
def multi_dot(arrays: Iterable[_nt._ToArray_nnd[_nt.co_number]], *, out: None = None) -> Any: ...
@overload
def multi_dot(arrays: Iterable[_nt._ToArray_1ds[_AnyNumberT]], *, out: None = None) -> _AnyNumberT: ...
@overload
def multi_dot(arrays: Iterable[_nt._ToArray_2nd[_AnyNumberT]], *, out: None = None) -> _nt.Array[_AnyNumberT]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[bool]], *, out: None = None) -> np.bool: ...
@overload
def multi_dot(arrays: Iterable[_nt.Sequence2ND[bool]], *, out: None = None) -> _nt.Array[np.bool]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[_nt.JustInt]], *, out: None = None) -> np.intp: ...
@overload
def multi_dot(arrays: Iterable[_nt.Sequence2ND[_nt.JustInt]], *, out: None = None) -> _nt.Array[np.intp]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[_nt.JustFloat]], *, out: None = None) -> np.float64: ...
@overload
def multi_dot(arrays: Iterable[_nt.Sequence2ND[_nt.JustFloat]], *, out: None = None) -> _nt.Array[np.float64]: ...
@overload
def multi_dot(arrays: Iterable[Sequence[_nt.JustComplex]], *, out: None = None) -> np.complex128: ...
@overload
def multi_dot(arrays: Iterable[_nt.Sequence2ND[_nt.JustComplex]], *, out: None = None) -> _nt.Array[np.complex128]: ...
@overload
def multi_dot(arrays: Iterable[_nt.CoComplex_1nd], *, out: _ArrayT) -> _ArrayT: ...
@overload
def multi_dot(
    arrays: Iterable[_nt.CoComplex_1nd | _nt.ToTimeDelta_1nd | _nt.ToObject_1nd], *, out: None = None
) -> Any: ...

# pyright false positive in case of typevar constraints
@overload
def cross(  # pyright: ignore[reportOverlappingOverload]
    x1: _nt._ToArray_1nd[_AnyNumberT], x2: _nt._ToArray_1nd[_AnyNumberT], /, *, axis: int = -1
) -> _nt.Array[_AnyNumberT]: ...
@overload
def cross(x1: _nt.ToBool_1nd, x2: _nt.ToBool_1nd, /, *, axis: int = -1) -> _nt.Array[np.bool]: ...
@overload
def cross(x1: _nt.ToInt_1nd, x2: _nt.CoInt64_1nd, /, *, axis: int = -1) -> _nt.Array[np.intp]: ...
@overload
def cross(x1: _nt.CoInt64_1nd, x2: _nt.ToInt_1nd, /, *, axis: int = -1) -> _nt.Array[np.intp]: ...
@overload
def cross(x1: _nt.ToFloat64_1nd, x2: _nt.CoFloat64_1nd, /, *, axis: int = -1) -> _nt.Array[np.float64]: ...
@overload
def cross(x1: _nt.CoFloat64_1nd, x2: _nt.ToFloat64_1nd, /, *, axis: int = -1) -> _nt.Array[np.float64]: ...
@overload
def cross(x1: _nt.ToComplex128_1nd, x2: _nt.CoComplex128_1nd, /, *, axis: int = -1) -> _nt.Array[np.complex128]: ...
@overload
def cross(x1: _nt.CoComplex128_1nd, x2: _nt.ToComplex128_1nd, /, *, axis: int = -1) -> _nt.Array[np.complex128]: ...
@overload
def cross(x1: _nt.ToInteger_1nd, x2: _nt.CoInteger_1nd, /, *, axis: int = -1) -> _nt.Array[np.integer]: ...
@overload
def cross(x1: _nt.CoInteger_1nd, x2: _nt.ToInteger_1nd, /, *, axis: int = -1) -> _nt.Array[np.integer]: ...
@overload
def cross(x1: _nt.ToFloating_1nd, x2: _nt.CoFloating_1nd, /, *, axis: int = -1) -> _nt.Array[np.floating]: ...
@overload
def cross(x1: _nt.CoFloating_1nd, x2: _nt.ToFloating_1nd, /, *, axis: int = -1) -> _nt.Array[np.floating]: ...
@overload
def cross(x1: _nt.ToComplex_1nd, x2: _nt.CoComplex_1nd, /, *, axis: int = -1) -> _nt.Array[np.complexfloating]: ...
@overload
def cross(x1: _nt.CoComplex_1nd, x2: _nt.ToComplex_1nd, /, *, axis: int = -1) -> _nt.Array[np.complexfloating]: ...
@overload
def cross(x1: _nt.CoComplex_1nd, x2: _nt.CoComplex_1nd, /, *, axis: int = -1) -> _nt.Array[Any]: ...

# pyright false positive in case of typevar constraints
@overload  # workaround for microsoft/pyright#10232
def matmul(x1: _nt._ToArray_nnd[_nt.co_number], x2: _nt._ToArray_nnd[_nt.co_number], /) -> Any: ...
@overload
def matmul(x1: _nt._ToArray_1ds[_AnyNumberT], x2: _nt._ToArray_1ds[_AnyNumberT], /) -> _AnyNumberT: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: _nt._ToArray_2nd[_AnyNumberT], x2: _nt._ToArray_1nd[_AnyNumberT], /) -> _nt.Array[_AnyNumberT]: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: _nt._ToArray_1nd[_AnyNumberT], x2: _nt._ToArray_2nd[_AnyNumberT], /) -> _nt.Array[_AnyNumberT]: ...  # pyright: ignore[reportOverlappingOverload]
@overload
def matmul(x1: _nt.ToBool_1ds, x2: _nt.ToBool_1ds, /) -> np.bool: ...
@overload
def matmul(x1: _nt.ToBool_2nd, x2: _nt.ToBool_1nd, /) -> _nt.Array[np.bool]: ...
@overload
def matmul(x1: _nt.ToBool_1nd, x2: _nt.ToBool_2nd, /) -> _nt.Array[np.bool]: ...
@overload
def matmul(x1: _nt.ToInt_1ds, x2: _nt.CoInt64_1ds, /) -> np.intp: ...
@overload
def matmul(x1: _nt.CoInt64_1ds, x2: _nt.ToInt_1ds, /) -> np.intp: ...
@overload
def matmul(x1: _nt.ToInt_2nd, x2: _nt.CoInt64_1nd, /) -> _nt.Array[np.intp]: ...
@overload
def matmul(x1: _nt.CoInt64_1nd, x2: _nt.ToInt_2nd, /) -> _nt.Array[np.intp]: ...
@overload
def matmul(x1: _nt.ToFloat64_1ds, x2: _nt.CoFloat64_1ds, /) -> np.float64: ...
@overload
def matmul(x1: _nt.CoFloat64_1ds, x2: _nt.ToFloat64_1ds, /) -> np.float64: ...
@overload
def matmul(x1: _nt.ToFloat64_2nd, x2: _nt.CoFloat64_1nd, /) -> _nt.Array[np.float64]: ...
@overload
def matmul(x1: _nt.CoFloat64_1nd, x2: _nt.ToFloat64_2nd, /) -> _nt.Array[np.float64]: ...
@overload
def matmul(x1: _nt.ToComplex128_1ds, x2: _nt.CoComplex128_1ds, /) -> np.complex128: ...
@overload
def matmul(x1: _nt.CoComplex128_1ds, x2: _nt.ToComplex128_1ds, /) -> np.complex128: ...
@overload
def matmul(x1: _nt.ToComplex128_2nd, x2: _nt.CoComplex128_1nd, /) -> _nt.Array[np.complex128]: ...
@overload
def matmul(x1: _nt.CoComplex128_1nd, x2: _nt.ToComplex128_2nd, /) -> _nt.Array[np.complex128]: ...
@overload
def matmul(x1: _nt.ToInteger_1ds, x2: _nt.CoInteger_1ds, /) -> np.integer: ...
@overload
def matmul(x1: _nt.CoInteger_1ds, x2: _nt.ToInteger_1ds, /) -> np.integer: ...
@overload
def matmul(x1: _nt.ToInteger_2nd, x2: _nt.CoInteger_1nd, /) -> _nt.Array[np.integer]: ...
@overload
def matmul(x1: _nt.CoInteger_1nd, x2: _nt.ToInteger_2nd, /) -> _nt.Array[np.integer]: ...
@overload
def matmul(x1: _nt.ToFloating_1ds, x2: _nt.CoFloating_1ds, /) -> np.floating: ...
@overload
def matmul(x1: _nt.CoFloating_1ds, x2: _nt.ToFloating_1ds, /) -> np.floating: ...
@overload
def matmul(x1: _nt.ToFloating_2nd, x2: _nt.CoFloating_1nd, /) -> _nt.Array[np.floating]: ...
@overload
def matmul(x1: _nt.CoFloating_1nd, x2: _nt.ToFloating_2nd, /) -> _nt.Array[np.floating]: ...
@overload
def matmul(x1: _nt.ToComplex_1ds, x2: _nt.CoComplex_1ds, /) -> np.complexfloating: ...
@overload
def matmul(x1: _nt.CoComplex_1ds, x2: _nt.ToComplex_1ds, /) -> np.complexfloating: ...
@overload
def matmul(x1: _nt.ToComplex_2nd, x2: _nt.CoComplex_1nd, /) -> _nt.Array[np.complexfloating]: ...
@overload
def matmul(x1: _nt.CoComplex_1nd, x2: _nt.ToComplex_2nd, /) -> _nt.Array[np.complexfloating]: ...
@overload
def matmul(x1: _nt.CoComplex_2nd, x2: _nt.CoComplex_1nd, /) -> _nt.Array[Any]: ...
@overload
def matmul(x1: _nt.CoComplex_1nd, x2: _nt.CoComplex_2nd, /) -> _nt.Array[Any]: ...
@overload
def matmul(x1: _nt.CoComplex_1nd, x2: _nt.CoComplex_1nd, /) -> Any: ...

#
@overload  # float64
def eig(a: _ToFloat64_1nd) -> EigResult[np.float64] | EigResult[np.complex128]: ...
@overload  # complex128
def eig(a: _nt.ToComplex128_1nd) -> EigResult[np.complex128]: ...
@overload  # complex64
def eig(a: _nt.ToComplex64_1nd) -> EigResult[np.complex64]: ...
@overload  # float32
def eig(a: _nt.ToFloat32_1nd) -> EigResult[np.float32] | EigResult[np.complex64]: ...
@overload  # +complex128
def eig(a: _nt.CoComplex128_1nd) -> EigResult: ...

#
@overload  # float64
def eigvals(a: _ToFloat64_1nd) -> _nt.Array[np.float64] | _nt.Array[np.complex128]: ...
@overload  # complex128
def eigvals(a: _nt.ToComplex128_1nd) -> _nt.Array[np.complex128]: ...
@overload  # complex64
def eigvals(a: _nt.ToComplex64_1nd) -> _nt.Array[np.complex64]: ...
@overload  # float32
def eigvals(a: _nt.ToFloat32_1nd) -> _nt.Array[np.float32] | _nt.Array[np.complex64]: ...
@overload  # +complex128
def eigvals(a: _nt.CoComplex128_1nd) -> _nt.Array[Any]: ...

#
@overload  # float64
def eigh(a: _ToFloat64_1nd, UPLO: _UPLO = "L") -> EighResult[np.float64, np.float64]: ...
@overload  # float32
def eigh(a: _nt._ToArray_1nd[_Inexact32T], UPLO: _UPLO = "L") -> EighResult[np.float32, _Inexact32T]: ...
@overload  # complex128
def eigh(a: _nt.ToComplex128_1nd, UPLO: _UPLO = "L") -> EighResult[np.float64, np.complex128]: ...
@overload  # +complex128
def eigh(a: _nt.CoComplex128_1nd, UPLO: _UPLO = "L") -> EighResult: ...

#
@overload  # float64 | complex128
def eigvalsh(a: _Toinexact64_1nd, UPLO: _UPLO = "L") -> _nt.Array[np.float64]: ...
@overload  # float32 | complex64
def eigvalsh(a: _Toinexact32_1nd, UPLO: _UPLO = "L") -> _nt.Array[np.float32]: ...
@overload  # +complex128
def eigvalsh(a: _nt.CoComplex128_1nd, UPLO: _UPLO = "L") -> _nt.Array[np.floating]: ...

#
@overload  # float64, reduced|complete
def qr(a: _ToFloat64_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.float64]: ...
@overload  # float64, raw
def qr(a: _ToFloat64_1nd, mode: L["raw"]) -> _Tuple2[_Array2ND[np.float64]]: ...
@overload  # float64, r
def qr(a: _ToFloat64_1nd, mode: L["r"]) -> _Array2ND[np.float64]: ...
@overload  # float32 + complex64, reduced|complete
def qr(a: _nt._ToArray_1nd[_Inexact32T], mode: L["reduced", "complete"] = "reduced") -> QRResult[_Inexact32T]: ...
@overload  # float32 + complex64, raw
def qr(a: _nt._ToArray_1nd[_Inexact32T], mode: L["raw"]) -> _Tuple2[_Array2ND[_Inexact32T]]: ...
@overload  # float32 + complex64, r
def qr(a: _nt._ToArray_1nd[_Inexact32T], mode: L["r"]) -> _Array2ND[_Inexact32T]: ...
@overload  # complex128, reduced|complete
def qr(a: _nt.ToComplex128_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[np.complex128]: ...
@overload  # complex128, raw
def qr(a: _nt.ToComplex128_1nd, mode: L["raw"]) -> _Tuple2[_Array2ND[np.complex128]]: ...
@overload  # complex128, r
def qr(a: _nt.ToComplex128_1nd, mode: L["r"]) -> _Array2ND[np.complex128]: ...
@overload  # +complex128, reduced|complete
def qr(a: _nt.CoComplex128_1nd, mode: L["reduced", "complete"] = "reduced") -> QRResult[Any]: ...
@overload  # +complex128, raw
def qr(a: _nt.CoComplex128_1nd, mode: L["raw"]) -> _Tuple2[_Array2ND[Any]]: ...
@overload  # +complex128, r
def qr(a: _nt.CoComplex128_1nd, mode: L["r"]) -> _Array2ND[Any]: ...

#
@overload  # float64 | complex128, compute_uv=False (positional)
def svd(
    a: _Toinexact64_1nd, full_matrices: bool, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.float64]: ...
@overload  # float64 | complex128, compute_uv=False (keyword)
def svd(
    a: _Toinexact64_1nd, full_matrices: bool = True, *, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.float64]: ...
@overload  # float64, compute_uv=True
def svd(
    a: _ToFloat64_1nd, full_matrices: bool = True, compute_uv: _True = True, hermitian: bool = False
) -> SVDResult[np.float64, np.float64]: ...
@overload  # complex128, compute_uv=True
def svd(
    a: _nt.ToComplex128_1nd, full_matrices: bool = True, compute_uv: _True = True, hermitian: bool = False
) -> SVDResult[np.float64, np.complex128]: ...
@overload  # float32 + complex64, compute_uv=True
def svd(
    a: _nt._ToArray_1nd[_Inexact32T], full_matrices: bool = True, compute_uv: _True = True, hermitian: bool = False
) -> SVDResult[np.float32, _Inexact32T]: ...
@overload  # float32 | complex64, compute_uv=False (positional)
def svd(
    a: _Toinexact32_1nd, full_matrices: bool, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.float32]: ...
@overload  # float32 | complex64, compute_uv=False (keyword)
def svd(
    a: _Toinexact32_1nd, full_matrices: bool = True, *, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.float32]: ...
@overload  # +complex128, compute_uv=True
def svd(
    a: _nt.CoComplex128_1nd, full_matrices: bool = True, compute_uv: _True = True, hermitian: bool = False
) -> SVDResult: ...
@overload  # +complex128, compute_uv=False (positional)
def svd(
    a: _nt.CoComplex128_1nd, full_matrices: bool, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.floating]: ...
@overload  # +complex128, compute_uv=False (keyword)
def svd(
    a: _nt.CoComplex128_1nd, full_matrices: bool = True, *, compute_uv: _False, hermitian: bool = False
) -> _nt.Array[np.floating]: ...

#
@overload  # float64 | complex128
def svdvals(x: _Toinexact64_1nd, /) -> _nt.Array[np.float64]: ...
@overload  # floaat32 | complex64
def svdvals(x: _Toinexact32_1nd, /) -> _nt.Array[np.float32]: ...
@overload  # +complex128
def svdvals(x: _nt.CoComplex128_1nd, /) -> _nt.Array[np.floating]: ...

#
@overload  # workaround for microsoft/pyright#10232
def matrix_rank(
    A: _nt._ToArray_nnd[_nt.co_complex128],
    tol: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _nt.ToFloating_nd | None = None,
) -> Any: ...
@overload  # <2d +complex128
def matrix_rank(
    A: _nt.CoComplex128_0d | _nt.CoComplex128_1ds,
    tol: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _nt.ToFloating_nd | None = None,
) -> L[0, 1]: ...
@overload  # 2d +complex128
def matrix_rank(
    A: _nt.CoComplex128_2ds,
    tol: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _nt.ToFloating_nd | None = None,
) -> np.intp: ...
@overload  # >2d +complex128
def matrix_rank(
    A: _nt.CoComplex128_3nd,
    tol: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _nt.ToFloating_nd | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # nd +complex128
def matrix_rank(
    A: _nt.CoComplex128_nd,
    tol: _nt.ToFloating_nd | None = None,
    hermitian: bool = False,
    *,
    rtol: _nt.ToFloating_nd | None = None,
) -> Any: ...

#
@overload  # workaround for microsoft/pyright#10232
def cond(x: _nt._ToArray_nnd[_nt.co_complex128], p: _Ord | None = None) -> Any: ...
@overload  # 2d float64 | complex128
def cond(x: _Toinexact64_2ds, p: _Ord | None = None) -> np.float64: ...
@overload  # 2d float32 | complex64
def cond(x: _Toinexact32_2ds, p: _Ord | None = None) -> np.float32: ...
@overload  # 2d +complex128
def cond(x: _nt.CoComplex128_2ds, p: _Ord | None = None) -> np.floating: ...
@overload  # >2d float64 | complex128
def cond(x: _Toinexact64_3nd, p: _Ord | None = None) -> _nt.Array[np.float64]: ...
@overload  # >2d float32 | complex64
def cond(x: _Toinexact32_3nd, p: _Ord | None = None) -> _nt.Array[np.float32]: ...
@overload  # >2d +complex128
def cond(x: _nt.CoComplex128_3nd, p: _Ord | None = None) -> _nt.Array[np.floating]: ...
@overload  # +complex128
def cond(x: _nt.CoComplex128_1nd, p: _Ord | None = None) -> Any: ...

# keep in sync with `det`
@overload  # # workaround for microsoft/pyright#10232
def slogdet(a: _nt._ToArray_nnd[_nt.co_complex128]) -> SlogdetResult: ...
@overload  # 2d float64
def slogdet(a: _ToFloat64_2ds) -> SlogdetResult[np.float64, np.float64]: ...
@overload  # 2d float32 + complex64
def slogdet(a: _nt._ToArray_2ds[_Inexact32T]) -> SlogdetResult[np.float32, _Inexact32T]: ...
@overload  # 2d complex128
def slogdet(a: _nt.ToComplex128_2ds) -> SlogdetResult[np.float64, np.complex128]: ...
@overload  # >2d float64
def slogdet(a: _ToFloat64_3nd) -> SlogdetResult[_nt.Array[np.float64], _nt.Array[np.float64]]: ...
@overload  # >2d float32 + complex64
def slogdet(a: _nt._ToArray_3nd[_Inexact32T]) -> SlogdetResult[_nt.Array[np.float32], _nt.Array[_Inexact32T]]: ...
@overload  # >2d complex128
def slogdet(a: _nt.ToComplex128_3nd) -> SlogdetResult[_nt.Array[np.float64], _nt.Array[np.complex128]]: ...
@overload  # +complex128
def slogdet(a: _nt.CoComplex128_1nd) -> SlogdetResult: ...

#
@overload  # workaround for microsoft/pyright#10232
def det(a: _nt._ToArray_nnd[_nt.co_complex128]) -> Any: ...
@overload  # 2d float64
def det(a: _ToFloat64_2ds) -> np.float64: ...
@overload  # 2d float32 + complex64
def det(a: _nt._ToArray_2ds[_Inexact32T]) -> _Inexact32T: ...
@overload  # 2d complex128
def det(a: _nt.ToComplex128_2ds) -> np.complex128: ...
@overload  # >2d float64
def det(a: _ToFloat64_3nd) -> _nt.Array[np.float64]: ...
@overload  # >2d float32 + complex64
def det(a: _nt._ToArray_3nd[_Inexact32T]) -> _nt.Array[_Inexact32T]: ...
@overload  # >2d complex128
def det(a: _nt.ToComplex128_3nd) -> _nt.Array[np.complex128]: ...
@overload  # +complex128
def det(a: _nt.CoComplex128_1nd) -> Any: ...

#
@overload  # float64, +float64
def lstsq(
    a: _ToFloat64_1nd, b: _nt.CoFloat64_1nd, rcond: float | None = None
) -> _LstSqResult[np.float64, np.float64]: ...
@overload  # +float64, float64
def lstsq(
    a: _nt.CoFloat64_1nd, b: _ToFloat64_1nd, rcond: float | None = None
) -> _LstSqResult[np.float64, np.float64]: ...
@overload  # float32, float32
def lstsq(
    a: _nt.ToFloat32_1nd, b: _nt.ToFloat32_1nd, rcond: float | None = None
) -> _LstSqResult[np.float32, np.float32]: ...
@overload  # complex128, +complex128
def lstsq(
    a: _nt.ToComplex128_1nd, b: _nt.CoComplex128_1nd, rcond: float | None = None
) -> _LstSqResult[np.complex128, np.float64]: ...
@overload  # +complex128, complex128
def lstsq(
    a: _nt.CoComplex128_1nd, b: _nt.ToComplex128_1nd, rcond: float | None = None
) -> _LstSqResult[np.complex128, np.float64]: ...
@overload  # complex64, +complex64
def lstsq(
    a: _nt.ToComplex64_1nd, b: _nt.CoComplex64_1nd, rcond: float | None = None
) -> _LstSqResult[np.complex64, np.float32]: ...
@overload  # +complex64, complex64
def lstsq(
    a: _nt.CoComplex64_1nd, b: _nt.ToComplex64_1nd, rcond: float | None = None
) -> _LstSqResult[np.complex64, np.float32]: ...
@overload  # +complex128, +complex128
def lstsq(
    a: _nt.CoComplex128_1nd, b: _nt.CoComplex128_1nd, rcond: float | None = None
) -> _LstSqResult[Any, np.floating]: ...

#
@overload  # float64 | complex128 | character, axis=None, keepdims=False
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float64: ...
@overload  # float64 | complex128 | character, keepdims=True (keyword)
def norm(
    x: _ToUnsafe64_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array2ND[np.float64]: ...
@overload  # float64 | complex128 | character, axis=<given> (positional)
def norm(x: _ToUnsafe64_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> _nt.Array[np.float64]: ...
@overload  # float64 | complex128 | character, axis=<given> (keyword)
def norm(
    x: _ToUnsafe64_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False
) -> _nt.Array[np.float64]: ...
@overload  # float16, axis=None, keepdims=False
def norm(x: _nt.ToFloat16_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float16: ...
@overload  # float16, keepdims=True (keyword)
def norm(
    x: _nt.ToFloat16_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array2ND[np.float16]: ...
@overload  # float16, axis=<given> (keyword)
def norm(
    x: _nt.ToFloat16_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False
) -> _nt.Array[np.float16]: ...
@overload  # float32 | complex64, axis=None, keepdims=False
def norm(x: _Toinexact32_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.float32: ...
@overload  # float32 | complex64, keepdims=True (keyword)
def norm(
    x: _Toinexact32_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array2ND[np.float32]: ...
@overload  # float32 | complex64, axis=<given> (positional)
def norm(x: _Toinexact32_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> _nt.Array[np.float32]: ...
@overload  # float32 | complex64, axis=<given> (keyword)
def norm(
    x: _Toinexact32_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False
) -> _nt.Array[np.float32]: ...
@overload  # longdouble | clongdouble, axis=None, keepdims=False
def norm(
    x: _Toinexact64l_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False
) -> np.longdouble: ...
@overload  # longdouble | clongdouble, keepdims=True (keyword)
def norm(
    x: _Toinexact64l_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array2ND[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given> (positional)
def norm(x: _Toinexact64l_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> _nt.Array[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given> (keyword)
def norm(
    x: _Toinexact64l_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False
) -> _nt.Array[np.longdouble]: ...
@overload  # +number, axis=None, keepdims=False
def norm(x: _nt.CoComplex_1nd, ord: _Ord | None = None, axis: None = None, keepdims: _False = False) -> np.floating: ...
@overload  # +number, keepdims=True
def norm(
    x: _nt.CoComplex_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, *, keepdims: _True
) -> _Array2ND[np.floating]: ...
@overload  # +number, axis=<given> (positional)
def norm(x: _nt.CoComplex_1nd, ord: _Ord | None, axis: _Ax2, keepdims: bool = False) -> _nt.Array[np.floating]: ...
@overload  # +number, axis=<given> (keyword)
def norm(
    x: _nt.CoComplex_1nd, ord: _Ord | None = None, *, axis: _Ax2, keepdims: bool = False
) -> _nt.Array[np.floating]: ...
@overload  # +number
def norm(x: _nt.CoComplex_1nd, ord: _Ord | None = None, axis: _Ax2 | None = None, keepdims: bool = False) -> Any: ...

#
@overload  # workaround for microsoft/pyright#10232
def matrix_norm(
    x: _nt._ToArray_nnd[_nt.co_number | np.character[Any]], /, *, keepdims: bool = False, ord: _Ord = "fro"
) -> Any: ...
@overload  # 2d float16
def matrix_norm(x: _nt.ToFloat16_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float16: ...  # type: ignore[overload-overlap]
@overload  # 2d float32 | complex64, keepdims=True
def matrix_norm(x: _Toinexact32_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float32: ...  # type: ignore[overload-overlap]
@overload  # 2d float64 | complex128 | character
def matrix_norm(x: _ToUnsafe64_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.float64: ...  # type: ignore[overload-overlap]
@overload  # 2d longdouble | clongdouble
def matrix_norm(x: _Toinexact64l_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.longdouble: ...  # type: ignore[overload-overlap]
@overload  # 2d +number
def matrix_norm(x: _nt.CoComplex_2ds, /, *, keepdims: bool = False, ord: _Ord = "fro") -> np.floating: ...  # type: ignore[overload-overlap]
@overload  # nd float16, keepdims=True
def matrix_norm(x: _nt.ToFloat16_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array2ND[np.float16]: ...
@overload  # nd float32 | complex64, keepdims=True
def matrix_norm(x: _Toinexact32_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array2ND[np.float32]: ...
@overload  # nd float64 | complex128 | character, keepdims=True
def matrix_norm(x: _ToUnsafe64_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array2ND[np.float64]: ...
@overload  # nd longdouble | clongdouble, keepdims=True
def matrix_norm(x: _Toinexact64l_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array2ND[np.longdouble]: ...
@overload  # nd +number, keepdims=True
def matrix_norm(x: _nt.CoComplex_1nd, /, *, keepdims: _True, ord: _Ord = "fro") -> _Array2ND[np.floating]: ...
@overload  # >2d float16
def matrix_norm(x: _nt.ToFloat16_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> _nt.Array[np.float16]: ...
@overload  # >2d float32 | complex64
def matrix_norm(x: _Toinexact32_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> _nt.Array[np.float32]: ...
@overload  # >2d float64 | complex128 | character
def matrix_norm(x: _ToUnsafe64_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> _nt.Array[np.float64]: ...
@overload  # >2d longdouble | clongdouble
def matrix_norm(x: _Toinexact64l_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> _nt.Array[np.longdouble]: ...
@overload  # >2d +number
def matrix_norm(x: _nt.CoComplex_3nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> _nt.Array[np.floating]: ...
@overload  # nd +number
def matrix_norm(x: _nt.CoComplex_1nd | _nt.ToCharacter_1nd, /, *, keepdims: bool = False, ord: _Ord = "fro") -> Any: ...

#
@overload  # float64 | complex128 | character, axis=None, keepdims=False
def vector_norm(
    x: _ToUnsafe64_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2
) -> np.float64: ...
@overload  # float64 | complex128 | character, keepdims=True
def vector_norm(
    x: _ToUnsafe64_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2
) -> _nt.Array[np.float64]: ...
@overload  # float64 | complex128 | character, axis=<given>
def vector_norm(
    x: _ToUnsafe64_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2
) -> _nt.Array[np.float64]: ...
@overload  # float16, axis=None, keepdims=False
def vector_norm(
    x: _nt.ToFloat16_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2
) -> np.float16: ...
@overload  # float16, keepdims=True
def vector_norm(
    x: _nt.ToFloat16_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2
) -> _nt.Array[np.float16]: ...
@overload  # float16, axis=<given>
def vector_norm(
    x: _nt.ToFloat16_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2
) -> _nt.Array[np.float16]: ...
@overload  # float32 | complex64, axis=None, keepdims=False
def vector_norm(
    x: _Toinexact32_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2
) -> np.float32: ...
@overload  # float32 | complex64, keepdims=True
def vector_norm(
    x: _Toinexact32_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2
) -> _nt.Array[np.float32]: ...
@overload  # float32 | complex64, axis=<given>
def vector_norm(
    x: _Toinexact32_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2
) -> _nt.Array[np.float32]: ...
@overload  # longdouble | clongdouble, axis=None, keepdims=False
def vector_norm(
    x: _Toinexact64l_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2
) -> np.longdouble: ...
@overload  # longdouble | clongdouble, keepdims=True
def vector_norm(
    x: _Toinexact64l_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2
) -> _nt.Array[np.longdouble]: ...
@overload  # longdouble | clongdouble, axis=<given>
def vector_norm(
    x: _Toinexact64l_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2
) -> _nt.Array[np.longdouble]: ...
@overload  # +number, axis=None, keepdims=False
def vector_norm(
    x: _nt.CoComplex_1nd, /, *, axis: None = None, keepdims: _False = False, ord: float = 2
) -> np.floating: ...
@overload  # +number, keepdims=True
def vector_norm(
    x: _nt.CoComplex_1nd, /, *, axis: _Ax2 | None = None, keepdims: _True, ord: float = 2
) -> _nt.Array[np.floating]: ...
@overload  # +number, axis=<given>
def vector_norm(
    x: _nt.CoComplex_1nd, /, *, axis: _Ax2, keepdims: bool = False, ord: float = 2
) -> _nt.Array[np.floating]: ...
@overload  # +number
def vector_norm(
    x: _nt.CoComplex_1nd, /, *, axis: _Ax2 | None = None, keepdims: bool = False, ord: float = 2
) -> Any: ...

#
@overload
def diagonal(x: _nt.ToObject_2nd, /, *, offset: CanIndex = 0) -> _nt.Array[np.object_]: ...
@overload
def diagonal(x: _nt._ToArray_2ds[_NativeScalarT], /, *, offset: CanIndex = 0) -> _nt.Array1D[_NativeScalarT]: ...
@overload
def diagonal(x: _ToArray_2nd_ish[_NativeScalarT], /, *, offset: CanIndex = 0) -> _nt.Array[_NativeScalarT]: ...
@overload
def diagonal(x: _nt.Sequence2ND[bool], /, *, offset: CanIndex = 0) -> _nt.Array[np.bool]: ...
@overload
def diagonal(x: _nt.Sequence2ND[_nt.JustInt], /, *, offset: CanIndex = 0) -> _nt.Array[np.intp]: ...
@overload
def diagonal(x: _nt.Sequence2ND[_nt.JustFloat], /, *, offset: CanIndex = 0) -> _nt.Array[np.float64]: ...
@overload
def diagonal(x: _nt.Sequence2ND[_nt.JustComplex], /, *, offset: CanIndex = 0) -> _nt.Array[np.complex128]: ...
@overload
def diagonal(x: _nt.Sequence2ND[_nt.JustBytes], /, *, offset: CanIndex = 0) -> _nt.Array[np.bytes_]: ...
@overload
def diagonal(x: _nt.Sequence2ND[_nt.JustStr], /, *, offset: CanIndex = 0) -> _nt.Array[np.str_]: ...
@overload
def diagonal(x: _nt.ToGeneric_1nd, /, *, offset: CanIndex = 0) -> _nt.Array[Any]: ...

#
@overload
def trace(x: _nt._ToArray_2ds[_ScalarT], /, *, offset: CanIndex = 0, dtype: None = None) -> _ScalarT: ...
@overload
def trace(x: _nt._ToArray_3nd[_ScalarT], /, *, offset: CanIndex = 0, dtype: None = None) -> _nt.Array[_ScalarT]: ...
@overload
def trace(x: _nt.Sequence2D[bool], /, *, offset: CanIndex = 0, dtype: None = None) -> np.bool: ...
@overload
def trace(x: _nt.Sequence3ND[bool], /, *, offset: CanIndex = 0, dtype: None = None) -> _nt.Array[np.bool]: ...
@overload
def trace(x: _nt.Sequence2D[_nt.JustInt], /, *, offset: CanIndex = 0, dtype: None = None) -> np.intp: ...
@overload
def trace(x: _nt.Sequence3ND[_nt.JustInt], /, *, offset: CanIndex = 0, dtype: None = None) -> _nt.Array[np.intp]: ...
@overload
def trace(x: _nt.Sequence2D[_nt.JustFloat], /, *, offset: CanIndex = 0, dtype: None = None) -> np.float64: ...
@overload
def trace(
    x: _nt.Sequence3ND[_nt.JustFloat], /, *, offset: CanIndex = 0, dtype: None = None
) -> _nt.Array[np.float64]: ...
@overload
def trace(x: _nt.Sequence2D[_nt.JustComplex], /, *, offset: CanIndex = 0, dtype: None = None) -> np.complex128: ...
@overload
def trace(
    x: _nt.Sequence3ND[_nt.JustComplex], /, *, offset: CanIndex = 0, dtype: None = None
) -> _nt.Array[np.complex128]: ...
@overload
def trace(x: _nt.CoComplex_2ds, /, *, offset: CanIndex = 0, dtype: _ToDType[_ScalarT]) -> _ScalarT: ...
@overload
def trace(x: _nt.CoComplex_3nd, /, *, offset: CanIndex = 0, dtype: _ToDType[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def trace(x: _nt.CoComplex_3nd, /, *, offset: CanIndex = 0, dtype: DTypeLike | None = None) -> _nt.Array[Any]: ...
@overload
def trace(x: _nt.CoComplex_1nd, /, *, offset: CanIndex = 0, dtype: DTypeLike | None = None) -> Any: ...
