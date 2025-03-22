from collections.abc import Callable, Sequence
from typing import (
    Any,
    Concatenate,
    Final,
    Literal as L,
    Protocol,
    SupportsIndex,
    TypeAlias,
    TypedDict,
    overload,
    type_check_only,
)
from typing_extensions import Never, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy import _CastingKind, _OrderKACF  # noqa: ICN003
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _DTypeLike,
    _DTypeLikeBool,
    _DTypeLikeFloat,
    _FloatLike_co,
    _NestedSequence,
    _NumberLike_co,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArray,
)

from . import _multiarray_umath as _multiarray_umath
from ._multiarray_umath import (
    _UFUNC_API as _UFUNC_API,
    _add_newdoc_ufunc as _add_newdoc_ufunc,
    _extobj_contextvar as _extobj_contextvar,
    _get_extobj_dict as _get_extobj_dict,
    _make_extobj as _make_extobj,
    e,
    euler_gamma,
    pi,
)

__all__ = [
    "absolute",
    "add",
    "arccos",
    "arccosh",
    "arcsin",
    "arcsinh",
    "arctan",
    "arctan2",
    "arctanh",
    "bitwise_and",
    "bitwise_count",
    "bitwise_or",
    "bitwise_xor",
    "cbrt",
    "ceil",
    "conj",
    "conjugate",
    "copysign",
    "cos",
    "cosh",
    "deg2rad",
    "degrees",
    "divide",
    "divmod",
    "e",
    "equal",
    "euler_gamma",
    "exp",
    "exp2",
    "expm1",
    "fabs",
    "float_power",
    "floor",
    "floor_divide",
    "fmax",
    "fmin",
    "fmod",
    "frexp",
    "frompyfunc",
    "gcd",
    "greater",
    "greater_equal",
    "heaviside",
    "hypot",
    "invert",
    "isfinite",
    "isinf",
    "isnan",
    "isnat",
    "lcm",
    "ldexp",
    "left_shift",
    "less",
    "less_equal",
    "log",
    "log1p",
    "log2",
    "log10",
    "logaddexp",
    "logaddexp2",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "matvec",
    "maximum",
    "minimum",
    "mod",
    "modf",
    "multiply",
    "negative",
    "nextafter",
    "not_equal",
    "pi",
    "positive",
    "power",
    "rad2deg",
    "radians",
    "reciprocal",
    "remainder",
    "right_shift",
    "rint",
    "sign",
    "signbit",
    "sin",
    "sinh",
    "spacing",
    "sqrt",
    "square",
    "subtract",
    "tan",
    "tanh",
    "true_divide",
    "trunc",
    "vecdot",
    "vecmat",
]

###
# type parameters

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

_ArrayT = TypeVar("_ArrayT", bound=_AnyArray)
_ArrayT1 = TypeVar("_ArrayT1", bound=_AnyArray)
_ArrayT2 = TypeVar("_ArrayT2", bound=_AnyArray)

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)

_OutT = TypeVar("_OutT")
_OutT_co = TypeVar("_OutT_co", default=Any, covariant=True)
_OutT1 = TypeVar("_OutT1", default=Any)
_OutT1_co = TypeVar("_OutT1_co", covariant=True)
_OutT2 = TypeVar("_OutT2", default=Any)
_OutT2_co = TypeVar("_OutT2_co", covariant=True)

###
# helper types

_Tuple2: TypeAlias = tuple[_T, _T]
_Tuple3: TypeAlias = tuple[_T, _T, _T]
_Tuple4: TypeAlias = tuple[_T, _T, _T, _T]
_Tuple2_: TypeAlias = tuple[_T, _T, Unpack[tuple[_T, ...]]]
_Tuple3_: TypeAlias = tuple[_T, _T, _T, Unpack[tuple[_T, ...]]]
_Tuple4_: TypeAlias = tuple[_T, _T, _T, _T, Unpack[tuple[_T, ...]]]

_Out1: TypeAlias = _T | tuple[_T]
_AnyArray: TypeAlias = NDArray[Any]
_UFuncMethod: TypeAlias = L["__call__", "reduce", "reduceat", "accumulate", "outer", "at"]

_TimeLike: TypeAlias = np.datetime64 | np.timedelta64

_SupportsStringLikeArray: TypeAlias = _SupportsArray[np.dtypes.StringDType | np.dtype[np.character]]
_ToCharStringND: TypeAlias = (
    _SupportsStringLikeArray
    | _NestedSequence[_SupportsStringLikeArray]
    | list[str]
    | list[bytes]
    | _NestedSequence[list[str]]
    | _NestedSequence[list[bytes]]
)

###
# helper protocols

@type_check_only
class _CanArrayUFunc(Protocol[_OutT_co]):
    def __array_ufunc__(self, ufunc: np.ufunc, method: _UFuncMethod, /, *args: Any, **kwds: Any) -> _OutT_co: ...

###
# typeddicts for kwargs

@type_check_only
class _KwargsCommon(TypedDict, total=False):
    casting: _CastingKind
    order: _OrderKACF
    subok: bool

@type_check_only
class _Kwargs2(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple2[DTypeLike] | str | None

@type_check_only
class _Kwargs3(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple3[DTypeLike] | str | None

@type_check_only
class _Kwargs4(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple4[DTypeLike] | str | None

@type_check_only
class _Kwargs3_(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple3_[DTypeLike] | str | None

@type_check_only
class _Kwargs4_(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple4_[DTypeLike] | str | None

@type_check_only
class _Kwargs3_g(_KwargsCommon, total=False):
    signature: _Tuple3[DTypeLike] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

###
# ufunc method signatures

@type_check_only
class _Call11(Protocol):
    @overload  # (scalar, dtype: dtype[T]) -> T
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs2],
    ) -> _ScalarT: ...
    @overload  # (scalar) -> ?
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> Any: ...
    @overload  # (array, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[?] | ?
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _AnyArray: ...
    @overload  # (array-like) -> Array[?] | ?
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _AnyArray | Any: ...
    @overload  # (?) -> ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _Call11Bool(Protocol):
    @overload  # (scalar) -> bool
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.bool: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[bool]
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like) -> Array[bool] | bool
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool] | np.bool: ...

@type_check_only
class _Call11Float(Protocol):
    @overload  # (float) -> float64
    def __call__(
        self,
        x: float,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeFloat | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.float64: ...
    @overload  # (scalar) -> float
    def __call__(
        self,
        x: _FloatLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeFloat | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.floating: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: _ArrayLikeFloat_co,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _DTypeLikeFloat | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (NDArray[float64] | _NestedSequence[float]) -> NDArray[float64]
    def __call__(
        self,
        x: NDArray[np.float64] | _NestedSequence[float],
        /,
        out: _Out1[NDArray[np.float64]] | None = None,
        *,
        dtype: _DTypeLikeFloat | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.float64]: ...
    @overload  # (array) -> Array[float]
    def __call__(
        self,
        x: NDArray[np.floating] | _NestedSequence[np.floating],
        /,
        out: _Out1[NDArray[np.floating]] | None = None,
        *,
        dtype: _DTypeLikeFloat | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.floating]: ...

@type_check_only
class _Call11Isnat(Protocol):
    @overload  # (scalar) -> bool
    def __call__(
        self,
        x: _TimeLike,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.bool: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: _ArrayLike[_TimeLike],
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[bool]
    def __call__(
        self,
        x: NDArray[_TimeLike] | _NestedSequence[_TimeLike],
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool]: ...

@type_check_only
class _Call11Signbit(Protocol):
    @overload  # (scalar) -> bool
    def __call__(
        self,
        x: _FloatLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.bool: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: _ArrayLikeFloat_co,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[bool]
    def __call__(
        self,
        x: NDArray[np.floating] | _NestedSequence[np.floating],
        /,
        out: _Out1[NDArray[np.floating]] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool]: ...

@type_check_only
class _Call11Logical(Protocol):
    @overload
    def __call__(  # (scalar, dtype: np.object_) -> bool
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[np.object_],
        **kwargs: Unpack[_Kwargs2],
    ) -> bool: ...
    @overload
    def __call__(  # (scalar) -> np.bool
        self,
        x: _NumberLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> np.bool: ...
    @overload
    def __call__(  # (array-like, dtype: np.object_) -> np.object_
        self,
        x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[np.object_],
        **kwargs: Unpack[_Kwargs2],
    ) -> NDArray[np.object_] | bool: ...
    @overload
    def __call__(  # (array-like, out: T) -> T
        self,
        x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[bool]
    def __call__(
        self,
        x: NDArray[np.bool | np.number] | _NestedSequence[np.bool | np.number],
        /,
        out: _Out1[NDArray[np.bool]] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool]: ...
    @overload
    def __call__(  # (array-like) -> Array[bool] | bool
        self,
        x: _ArrayLikeNumber_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> NDArray[np.bool] | np.bool: ...
    @overload
    def __call__(  # (?) -> ?
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _UFunc11String(Protocol[_ScalarT_co]):
    @overload
    def __call__(
        self,
        x: bytes | str,
        /,
        out: None = None,
        *,
        where: bool = True,
        casting: _CastingKind = "same_kind",
        order: _OrderKACF = "K",
        dtype: _DTypeLikeBool | None = None,
        subok: bool = True,
        signature: str | tuple[DTypeLike, _DTypeLikeBool] | None = None,
    ) -> _ScalarT_co: ...
    @overload
    def __call__(
        self,
        x: _ToCharStringND,
        /,
        out: None = None,
        *,
        where: bool = True,
        casting: _CastingKind = "same_kind",
        order: _OrderKACF = "K",
        dtype: _DTypeLikeBool | None = None,
        subok: bool = True,
        signature: str | tuple[DTypeLike, _DTypeLikeBool] | None = None,
    ) -> NDArray[_ScalarT_co]: ...

@type_check_only
class _Call12(Protocol):
    @overload
    def __call__(
        self,
        x: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: None = None,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: _AnyArray,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x: _CanArrayUFunc,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[Any]: ...

@type_check_only
class _Call21Bool(Protocol):
    @overload  # (scalar, scalar) -> bool
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> np.bool: ...
    @overload  # (array-like, array) -> Array[bool]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray | _NestedSequence[_ScalarLike_co],
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array, array-like) -> Array[bool]
    def __call__(
        self,
        x1: _AnyArray | _NestedSequence[_ScalarLike_co],
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array-like, array-like) -> Array[bool] | bool
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> np.bool | NDArray[np.bool]: ...

@type_check_only
class _Call21Logical(Protocol):
    @overload  # (scalar, scalar, dtype: np.object_) -> np.object_
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[np.object_],
        **kwds: Unpack[_Kwargs3],
    ) -> bool: ...
    @overload  # (scalar, scalar) -> bool
    def __call__(
        self,
        x1: _NumberLike_co,
        x2: _NumberLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> np.bool: ...
    @overload  # (array-like, array, dtype: object_) -> Array[object_]
    def __call__(
        self,
        x1: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        x2: _AnyArray,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[np.object_],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.object_]: ...
    @overload  # (array, array-like, dtype: object_) -> Array[object_]
    def __call__(
        self,
        x1: _AnyArray,
        x2: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[np.object_],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.object_]: ...
    @overload  # (array-like, array, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: _ArrayLikeNumber_co,
        x2: NDArray[np.bool | np.number] | _NestedSequence[np.bool | np.number],
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: NDArray[np.bool | np.number] | _NestedSequence[np.bool | np.number],
        x2: _ArrayLikeNumber_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        x1: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        x2: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array-like, array) -> Array[?]
    def __call__(
        self,
        x1: _ArrayLikeNumber_co,
        x2: NDArray[np.bool | np.number] | _NestedSequence[np.bool | np.number | complex],
        /,
        out: _Out1[NDArray[np.bool]] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array, array-like) -> Array[?]
    def __call__(
        self,
        x1: NDArray[np.bool | np.number] | _NestedSequence[np.bool | np.number | complex],
        x2: _ArrayLikeNumber_co,
        /,
        out: _Out1[NDArray[np.bool]] | None = None,
        *,
        dtype: _DTypeLikeBool | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like, array-like) -> Array[?] | ?
    def __call__(
        self,
        x1: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        x2: _ArrayLikeNumber_co | _ArrayLikeObject_co,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> Any: ...

@type_check_only
class _Call21(Protocol):
    @overload  # (scalar, scalar, dtype: type[T]) -> T
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ScalarT: ...
    @overload  # (scalar, scalar) -> ?
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> Any: ...
    @overload  # (array-like, array, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, array) -> Array[?]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...
    @overload  # (array, array-like) -> Array[?]
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array-like, array-like) -> Array[?] | ?
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray | Any: ...

@type_check_only
class _Call22(Protocol):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_ScalarT]: ...
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[Any]: ...
    @overload
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        out1: NDArray[_ScalarT] | None = None,
        out2: NDArray[_ScalarT] | None = None,
        /,
        *,
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        out1: NDArray[_ScalarT] | None = None,
        out2: NDArray[_ScalarT] | None = None,
        /,
        *,
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: _ArrayT1,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike | _CanArrayUFunc,
        x2: ArrayLike | _CanArrayUFunc,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[Any]: ...

@type_check_only
class _Call21_g(Protocol):
    # scalar for 1D array-likes; ndarray otherwise
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray | None] = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> Any: ...

_AtE: TypeAlias = Callable[Concatenate[Never, Never, ...], None]
_At1: TypeAlias = Callable[[_CanArrayUFunc, _ArrayLikeInt_co], None]
_At2: TypeAlias = Callable[[_CanArrayUFunc, _ArrayLikeInt_co, ArrayLike], None]

@type_check_only
class _ReduceE(Protocol):
    def __call__(self, array: Never, /) -> Any: ...

@type_check_only
class _Reduce2(Protocol):
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: _ShapeLike | None = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
        keepdims: bool = False,
        initial: _ScalarLike_co | None = ...,
        where: _ArrayLikeBool_co = True,
    ) -> Any: ...

@type_check_only
class _AccumulateE(Protocol):
    def __call__(self, array: Never, /) -> Any: ...

@type_check_only
class _Accumulate2(Protocol):
    @overload
    def __call__(self, array: ArrayLike, /, axis: SupportsIndex, dtype: None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def __call__(self, array: ArrayLike, /, axis: SupportsIndex = 0, dtype: None = None, *, out: _ArrayT) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
    ) -> _AnyArray: ...

@type_check_only
class _ReduceAtE(Protocol):
    def __call__(self, array: Never, indices: Never, /) -> Any: ...

@type_check_only
class _ReduceAt2(Protocol):
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex,
        dtype: None,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        dtype: None = None,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
    ) -> _AnyArray: ...

_OuterE: TypeAlias = Callable[[Never, Never], Any]

@type_check_only
class _Outer1(Protocol):
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: _Out1[_ArrayT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: _Out1[NDArray[_ScalarT]] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: DTypeLike | None = None,
        out: _Out1[_AnyArray] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...

@type_check_only
class _Outer2(Protocol):
    @overload  # (array-like, array-like, out: (T1, None)) -> (T1, Array[?])
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[_ArrayT1, None],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload  # (array-like, array-like, out: (None, T2)) -> (Array[?], T2)
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[None, _ArrayT2],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload  # (array-like, array-like, out: (T1, T2)) -> (T1, T2)
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[_ArrayT1, _ArrayT2],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: DTypeLike | None = None,
        out: _Tuple2[_AnyArray | None] = (None, None),
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...

###
# specific ufunc aliases

_CallT11 = TypeVar("_CallT11", bound=Callable[Concatenate[Any, ...], object], default=_Call11)
_CallT12 = TypeVar("_CallT12", bound=Callable[Concatenate[Any, ...], tuple[object, object]], default=_Call12)
_CallT21 = TypeVar("_CallT21", bound=Callable[Concatenate[Any, Any, ...], object], default=_Call21)
_CallT21G = TypeVar("_CallT21G", bound=Callable[Concatenate[Any, ...], object], default=_Call21_g)
_CallT22 = TypeVar("_CallT22", bound=Callable[Concatenate[Any, Any, ...], tuple[object, object]], default=_Call22)

_ufunc_1_1 = TypeAliasType(
    "_ufunc_1_1",
    np.ufunc[_CallT11, _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT11,),
)
_ufunc_1_2 = TypeAliasType(
    "_ufunc_1_2",
    np.ufunc[_CallT12, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT12,),
)
_ufunc_2_1 = TypeAliasType(
    "_ufunc_2_1",
    np.ufunc[_CallT21, _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1],
    type_params=(_CallT21,),
)
_gufunc_2_1 = TypeAliasType(
    "_gufunc_2_1",
    np.ufunc[_CallT21G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer1],
    type_params=(_CallT21G,),
)
_ufunc_2_2 = TypeAliasType(
    "_ufunc_2_2",
    np.ufunc[_CallT22, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer2],
    type_params=(_CallT22,),
)

###
# ufuncs

# Signature notation:
# - {_} => union type
# - [u] => BHILQ
# - [i] => bhilq
# - [f] => efdg
# - [c] => FDG
# - $1  => type of first argument

###
# 1 in, 1 out

# {Mm} -> ?
isnat: Final[_ufunc_1_1[_Call11Isnat]] = ...

# {[f]} -> ?
signbit: Final[_ufunc_1_1[_Call11Signbit]] = ...

# {?[uifc]Mm} -> ?
isfinite: Final[_ufunc_1_1[_Call11Bool]] = ...
isinf: Final[_ufunc_1_1[_Call11Bool]] = ...

# {[f]T} -> ?
isnan: Final[_ufunc_1_1[_Call11Bool]] = ...

# {?[uifc]O} -> ?
# O -> O
logical_not: Final[_ufunc_1_1[_Call11Logical]] = ...

# {UT} -> ?
isnumeric: _ufunc_1_1[_UFunc11String[np.bool]]
isdecimal: _ufunc_1_1[_UFunc11String[np.bool]]

# {SUT} -> ?
isalnum: _ufunc_1_1[_UFunc11String[np.bool]]
isalpha: _ufunc_1_1[_UFunc11String[np.bool]]
isdigit: _ufunc_1_1[_UFunc11String[np.bool]]
islower: _ufunc_1_1[_UFunc11String[np.bool]]
isspace: _ufunc_1_1[_UFunc11String[np.bool]]
istitle: _ufunc_1_1[_UFunc11String[np.bool]]
isupper: _ufunc_1_1[_UFunc11String[np.bool]]

# {SUT} -> n
str_len: _ufunc_1_1[_UFunc11String[np.intp]]

# {[ui]} -> B
# O -> O
bitwise_count: Final[_ufunc_1_1] = ...

# {[f]} -> $1
spacing: Final[_ufunc_1_1[_Call11Float]] = ...

# {[f]O} -> $1
cbrt: Final[_ufunc_1_1] = ...
deg2rad: Final[_ufunc_1_1] = ...
degrees: Final[_ufunc_1_1] = ...
fabs: Final[_ufunc_1_1] = ...
rad2deg: Final[_ufunc_1_1] = ...
radians: Final[_ufunc_1_1] = ...

# {[fc]O} -> $1
arccos: Final[_ufunc_1_1] = ...
arccosh: Final[_ufunc_1_1] = ...
arcsin: Final[_ufunc_1_1] = ...
arcsinh: Final[_ufunc_1_1] = ...
arctan: Final[_ufunc_1_1] = ...
arctanh: Final[_ufunc_1_1] = ...
cos: Final[_ufunc_1_1] = ...
cosh: Final[_ufunc_1_1] = ...
exp: Final[_ufunc_1_1] = ...
exp2: Final[_ufunc_1_1] = ...
expm1: Final[_ufunc_1_1] = ...
log: Final[_ufunc_1_1] = ...
log2: Final[_ufunc_1_1] = ...
log10: Final[_ufunc_1_1] = ...
log1p: Final[_ufunc_1_1] = ...
rint: Final[_ufunc_1_1] = ...
sin: Final[_ufunc_1_1] = ...
sinh: Final[_ufunc_1_1] = ...
sqrt: Final[_ufunc_1_1] = ...
tan: Final[_ufunc_1_1] = ...
tanh: Final[_ufunc_1_1] = ...

# {?[ui]O} -> $1
invert: Final[_ufunc_1_1] = ...

# {?[uif]O} -> $1
ceil: Final[_ufunc_1_1] = ...
floor: Final[_ufunc_1_1] = ...
trunc: Final[_ufunc_1_1] = ...

# {?[uif]Om} -> $1
# F -> f
# D -> d
# G -> g
absolute: Final[_ufunc_1_1] = ...

# {[uifc]O} -> $1
conjugate: Final[_ufunc_1_1] = ...
conj = conjugate
reciprocal: Final[_ufunc_1_1] = ...
square: Final[_ufunc_1_1] = ...

# {[uifc]mO} -> $1
negative: Final[_ufunc_1_1] = ...
positive: Final[_ufunc_1_1] = ...
sign: Final[_ufunc_1_1] = ...

# {SUT} -> $1
_lstrip_whitespace: _ufunc_1_1
_rstrip_whitespace: _ufunc_1_1
_strip_whitespace: _ufunc_1_1

# {?[uifc]MmO} -> $1
_ones_like: _ufunc_1_1

###
# 1-in, 2-out

# {[f]} -> $1, i
frexp: Final[_ufunc_1_2] = ...

# {[f]} -> $1, $1
modf: Final[_ufunc_1_2] = ...

###
# 2-in, 1-out

# {?[uifc]OSUTV}, $1 -> ?
logical_and: Final[_ufunc_2_1[_Call21Logical]] = ...
logical_or: Final[_ufunc_2_1[_Call21Logical]] = ...
logical_xor: Final[_ufunc_2_1[_Call21Logical]] = ...

# {?[uifc]MmOSUT}, $1 -> ?, (also accepts dtype: O)
equal: Final[_ufunc_2_1[_Call21Bool]] = ...
not_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
greater: Final[_ufunc_2_1[_Call21Bool]] = ...
greater_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
less: Final[_ufunc_2_1[_Call21Bool]] = ...
less_equal: Final[_ufunc_2_1[_Call21Bool]] = ...

# {[f]}, {il} -> $1
ldexp: Final[_ufunc_2_1] = ...

# {dgDG}, $1 -> $1
float_power: Final[_ufunc_2_1] = ...

# {[f]}, $1 -> $1
copysign: Final[_ufunc_2_1] = ...
heaviside: Final[_ufunc_2_1] = ...
logaddexp: Final[_ufunc_2_1] = ...
logaddexp2: Final[_ufunc_2_1] = ...
nextafter: Final[_ufunc_2_1] = ...

# {[f]O}, $1 -> $1
arctan2: Final[_ufunc_2_1] = ...
hypot: Final[_ufunc_2_1] = ...

# {[fc]mO}, $1 -> $1
divide: Final[_ufunc_2_1] = ...
true_divide = divide

# {[ui]O}, $1 -> $1
gcd: Final[_ufunc_2_1] = ...
lcm: Final[_ufunc_2_1] = ...
left_shift: Final[_ufunc_2_1] = ...
right_shift: Final[_ufunc_2_1] = ...

# {?[ui]O}, $1 -> $1
bitwise_and: Final[_ufunc_2_1] = ...
bitwise_or: Final[_ufunc_2_1] = ...
bitwise_xor: Final[_ufunc_2_1] = ...

# {[uif]O}, $1 -> $1
fmod: Final[_ufunc_2_1] = ...

# {[uif]mO}, $1 -> $1
floor_divide: Final[_ufunc_2_1] = ...
remainder: Final[_ufunc_2_1] = ...
mod = remainder

# {[uifc]O}, $1 -> $1
power: Final[_ufunc_2_1] = ...

# {?[uifc]O}, $1 -> $1
matmul: Final[_gufunc_2_1] = ...  # (n?, k), (k, m?) -> (n?, m?)
matvec: Final[_gufunc_2_1] = ...  # (m, n), (n) -> (m)
vecdot: Final[_gufunc_2_1] = ...  # (n), (n) -> ()
vecmat: Final[_gufunc_2_1] = ...  # (n), (n, m) -> (m)

# {?[uifc]mO}, $1 -> $1
multiply: Final[_ufunc_2_1] = ...
subtract: Final[_ufunc_2_1] = ...

# {?[uifc]MmO}, $1 -> $1
fmax: Final[_ufunc_2_1] = ...
fmin: Final[_ufunc_2_1] = ...

# {?[uifc]MmOT}, $1 -> $1
maximum: Final[_ufunc_2_1] = ...
minimum: Final[_ufunc_2_1] = ...

# {?[uifc]MmOSUT}, $1 -> $1
add: Final[_ufunc_2_1] = ...

_expandtabs: _ufunc_2_1
_expandtabs_length: _ufunc_2_1
_lstrip_chars: _ufunc_2_1
_rstrip_chars: _ufunc_2_1
_strip_chars: _ufunc_2_1
_zfill: _ufunc_2_1

###
# 2-in, 2-out

# {[uif]}, $1 -> $1, $1
# m, m -> q, m
divmod: Final[_ufunc_2_2] = ...

###
# 3-in, 1-out

clip: np.ufunc
_center: np.ufunc
_ljust: np.ufunc
_rjust: np.ufunc

###
# 3-in, 3-out

_partition_index: np.ufunc
_rpartition_index: np.ufunc

###
# 4-in, 1-out

count: np.ufunc
endswith: np.ufunc
startswith: np.ufunc
find: np.ufunc
rfind: np.ufunc
index: np.ufunc
rindex: np.ufunc
_partition: np.ufunc
_rpartition: np.ufunc
_replace: np.ufunc

###
# frompyfunc

@type_check_only
class _Call11_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _Call21_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc,
        x2: _CanArrayUFunc | ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> Any: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> Any: ...

@type_check_only
class _Call3N1_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        x3: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        x2: _CanArrayUFunc | ArrayLike,
        x3: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> Any: ...

@type_check_only
class _Call1N2_py(Protocol[_OutT1_co, _OutT2_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: tuple[None, None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_OutT1_co, _OutT2_co]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: tuple[None, None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_OutT1_co | NDArray[np.object_], _OutT2_co | NDArray[np.object_]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> Any: ...

@type_check_only
class _Call1N2N_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: _Tuple2_[None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_OutT_co]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _Tuple2_[None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_OutT_co | NDArray[np.object_]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _Tuple2_[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_ArrayT]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Tuple2_[_AnyArray | None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> Any: ...

_3P = TypeAliasType("_3P", L[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
_2: TypeAlias = L[2]
_2P: TypeAlias = _2 | _3P
_1: TypeAlias = L[True, 1]
_1P: TypeAlias = _1 | _2P

_pyfunc_1_1 = TypeAliasType(
    "_pyfunc_1_1",
    np.ufunc[_Call11_py[_OutT], _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)
_pyfunc_2_1 = TypeAliasType(
    "_pyfunc_2_1",
    np.ufunc[_Call21_py[_OutT], _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1],
    type_params=(_OutT,),
)
_pyfunc_3n_1 = TypeAliasType(
    "_pyfunc_3n_1",
    np.ufunc[_Call3N1_py[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)
_pyfunc_1n_2 = TypeAliasType(
    "_pyfunc_1n_2",
    np.ufunc[_Call1N2_py[_OutT1, _OutT2], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT1, _OutT2),
)
_pyfunc_1n_2n = TypeAliasType(
    "_pyfunc_1n_2n",
    np.ufunc[_Call1N2N_py[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)

# NOTE: We can't use e.g. `Concatenate[Any, ...]`, as that causes mypy to reject every function...
@overload  # (a) -> T
def frompyfunc(f: Callable[[Any], _T], /, nin: _1, nout: _1, *, identity: object = None) -> _pyfunc_1_1[_T]: ...
@overload  # (a, b) -> T
def frompyfunc(f: Callable[[Any, Any], _T], /, nin: _2, nout: _1, *, identity: object = None) -> _pyfunc_2_1[_T]: ...
@overload  # (a, b, c, ...) -> T
def frompyfunc(f: Callable[..., _T], /, nin: _3P, nout: _1, *, identity: object = None) -> _pyfunc_3n_1[_T]: ...
@overload  # (a, ...) -> (T1, T2)
def frompyfunc(  # type: ignore[overload-overlap]  # mypy-only false positive
    f: Callable[..., tuple[_T1, _T2]],
    /,
    nin: _1P,
    nout: _2,
    *,
    identity: object = None,
) -> _pyfunc_1n_2[_T1, _T2]: ...
@overload  # (a, ...) -> (T1, T2, *(T, ...))
def frompyfunc(
    f: Callable[..., tuple[_T1, _T2, Unpack[tuple[_T, ...]]]],
    /,
    nin: _1P,
    nout: _2P,
    *,
    identity: object = None,
) -> _pyfunc_1n_2n[_T1 | _T2 | _T]: ...
@overload
def frompyfunc(f: Callable[..., Any], /, nin: SupportsIndex, nout: SupportsIndex, *, identity: object = None) -> np.ufunc: ...
