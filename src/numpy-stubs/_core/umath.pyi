from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from types import EllipsisType
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
from typing_extensions import TypeAliasType, TypeVar, Unpack

import _numtype as _nt
import numpy as np
from numpy import _CastingKind, _OrderKACF  # noqa: ICN003
from numpy._typing import (
    _DTypeLike as _ToDType,
    _DTypeLikeComplex as _ToDTypeComplex,
    _DTypeLikeFloat as _ToDTypeFloat,
    _ShapeLike,
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
    "matmul",
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

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_ArrayT1 = TypeVar("_ArrayT1", bound=_nt.Array)
_ArrayT2 = TypeVar("_ArrayT2", bound=_nt.Array)

_BoolArrayT = TypeVar("_BoolArrayT", bound=_BoolND)
_FloatArrayT = TypeVar("_FloatArrayT", bound=_FloatND)
_InexactArrayT = TypeVar("_InexactArrayT", bound=_nt.Array[np.inexact])

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
_FloatT = TypeVar("_FloatT", bound=np.floating)

_OutT = TypeVar("_OutT")
_OutT_co = TypeVar("_OutT_co", default=Any, covariant=True)
_OutT1 = TypeVar("_OutT1")
_OutT1_co = TypeVar("_OutT1_co", covariant=True)
_OutT2 = TypeVar("_OutT2")
_OutT2_co = TypeVar("_OutT2_co", covariant=True)

###
# helper types

_Tuple2: TypeAlias = tuple[_T, _T]
_Tuple3: TypeAlias = tuple[_T, _T, _T]
_Tuple4: TypeAlias = tuple[_T, _T, _T, _T]
_Tuple2_: TypeAlias = tuple[_T, _T, *tuple[_T, ...]]
_Tuple3_: TypeAlias = tuple[_T, _T, _T, *tuple[_T, ...]]
_Tuple4_: TypeAlias = tuple[_T, _T, _T, _T, *tuple[_T, ...]]

_Out1: TypeAlias = _T | tuple[_T]
_Out2: TypeAlias = _Tuple2[_T]
_UFuncMethod: TypeAlias = L["__call__", "reduce", "reduceat", "accumulate", "outer", "at"]

_Eq1: TypeAlias = L[1, True]
_Eq2: TypeAlias = L[2]
_Ge3 = TypeAliasType("_Ge3", L[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
_Ge1: TypeAlias = _Eq1 | _Ge2
_Ge2: TypeAlias = _Eq2 | _Ge3

_ToScalar: TypeAlias = np.generic | complex | _nt.JustBytes | _nt.JustStr
_ToFloat64: TypeAlias = _nt.JustFloat | np.float64
_ToComplex128: TypeAlias = _nt.JustComplex | np.complex128
_ToComplex: TypeAlias = _nt.JustComplex | np.complexfloating
_ToStringLike: TypeAlias = bytes | str | np.character

_CoFloat: TypeAlias = float | _nt.co_float
_CoComplex: TypeAlias = complex | _nt.co_complex

_ToDTypeInexact: TypeAlias = _ToDTypeFloat | _ToDTypeComplex

_BoolND: TypeAlias = _nt.Array[np.bool_]
_Float64ND: TypeAlias = _nt.Array[np.float64]
_Complex128ND: TypeAlias = _nt.Array[np.complex128]
_FloatND: TypeAlias = _nt.Array[np.floating]
_ComplexND: TypeAlias = _nt.Array[np.complexfloating]
_ObjectND: TypeAlias = _nt.Array[np.object_]

###
# helper protocols

@type_check_only
class _CanArrayUFunc(Protocol[_OutT_co]):
    def __array_ufunc__(self, ufunc: np.ufunc, method: _UFuncMethod, /, *args: object, **kw: object) -> _OutT_co: ...

###
# typeddicts for kwargs

@type_check_only
class _KwargsCommon(TypedDict, total=False):
    casting: _CastingKind
    order: _OrderKACF
    subok: bool

@type_check_only
class _Kwargs2(_KwargsCommon, total=False):
    where: _nt.ToBool_nd | None
    signature: _Tuple2[_nt.ToDType] | str | None

@type_check_only
class _Kwargs3(_KwargsCommon, total=False):
    where: _nt.ToBool_nd | None
    signature: _Tuple3[_nt.ToDType] | str | None

@type_check_only
class _Kwargs4(_KwargsCommon, total=False):
    where: _nt.ToBool_nd | None
    signature: _Tuple4[_nt.ToDType] | str | None

@type_check_only
class _Kwargs3_(_KwargsCommon, total=False):
    where: _nt.ToBool_nd | None
    signature: _Tuple3_[_nt.ToDType] | str | None

@type_check_only
class _Kwargs4_(_KwargsCommon, total=False):
    where: _nt.ToBool_nd | None
    signature: _Tuple4_[_nt.ToDType] | str | None

@type_check_only
class _Kwargs3_g(_KwargsCommon, total=False):
    signature: _Tuple3[_nt.ToDType] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

###
# ufunc method signatures

@type_check_only
class _Call11(Protocol):
    @overload  # 0d, dtype: T
    def __call__(
        self, x: _ToScalar, /, out: _Out1[None] = None, *, dtype: _ToDType[_ScalarT], **kw: Unpack[_Kwargs2]
    ) -> _ScalarT: ...
    @overload  # 0d
    def __call__(
        self, x: _ToScalar, /, out: _Out1[None] = None, *, dtype: _nt.ToDType | None = None, **kw: Unpack[_Kwargs2]
    ) -> Incomplete: ...
    @overload  # ?d, out: T
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: _Out1[_ArrayT], *, dtype: _nt.ToDType | None = None, **kw: Unpack[_Kwargs2]
    ) -> _ArrayT: ...
    @overload  # ?d, out=..., dtype: T
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: EllipsisType, *, dtype: _ToDType[_ScalarT], **kw: Unpack[_Kwargs2]
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # nd, dtype: T
    def __call__(
        self,
        x: _nt.ToGeneric_1nd,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # nd
    def __call__(
        self,
        x: _nt.ToGeneric_1nd,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d, out=...
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: EllipsisType, *, dtype: _nt.ToDType | None = None, **kw: Unpack[_Kwargs2]
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d
    def __call__(
        self,
        x: _nt.ToGeneric_nd,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete] | Incomplete: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _Call11Bool(Protocol):
    @overload  # 0d
    def __call__(
        self, x: _ToScalar, /, out: _Out1[None] = None, *, dtype: _nt.ToDTypeBool | None = None, **kw: Unpack[_Kwargs2]
    ) -> np.bool_: ...
    @overload  # nd, out: T
    def __call__(
        self,
        x: _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolArrayT],
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolArrayT: ...
    @overload  # nd
    def __call__(
        self,
        x: _nt.ToGeneric_1nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload  # ?d, out=...
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: EllipsisType, *, dtype: _nt.ToDTypeBool | None = None, **kw: Unpack[_Kwargs2]
    ) -> _BoolND: ...
    @overload  # ?d
    def __call__(
        self,
        x: _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND | Incomplete: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_BoolND | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _Call11Float(Protocol):
    @overload  # 0d float64
    def __call__(
        self,
        x: float | _nt.co_integer,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> np.float64: ...
    @overload  # 0d floating
    def __call__(
        self, x: _CoFloat, /, out: _Out1[None] = None, *, dtype: _ToDTypeFloat | None = None, **kw: Unpack[_Kwargs2]
    ) -> np.floating: ...
    @overload  # nd float64
    def __call__(
        self,
        x: _nt.ToFloat64_1nd | _nt.CoInteger_1nd,
        /,
        out: _Out1[_Float64ND | None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Float64ND: ...
    @overload  # ?d float64, out=...
    def __call__(
        self,
        x: _nt.ToFloat64_nd | _nt.CoInteger_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Float64ND: ...
    @overload  # ?d floating, out: T
    def __call__(
        self, x: _nt.CoFloating_nd, /, out: _Out1[_FloatArrayT], *, dtype: None = None, **kw: Unpack[_Kwargs2]
    ) -> _FloatArrayT: ...
    @overload  # nd floating
    def __call__(
        self,
        x: _nt.CoFloating_1nd,
        /,
        out: _Out1[_FloatND | None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _FloatND: ...
    @overload  # ?d floating
    def __call__(
        self, x: _nt.CoFloating_nd, /, out: EllipsisType, *, dtype: _ToDTypeFloat | None = None, **kw: Unpack[_Kwargs2]
    ) -> _FloatND: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_FloatND | None] | EllipsisType = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _Call11Inexact(Protocol):
    @overload  # 0d float64
    def __call__(
        self,
        x: float | _nt.co_integer,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> np.float64: ...
    @overload  # 0d complex128
    def __call__(
        self,
        x: _ToComplex128,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeComplex128 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> np.complex128: ...
    @overload  # 0d floating
    def __call__(
        self, x: _CoFloat, /, out: _Out1[None] = None, *, dtype: _ToDTypeFloat | None = None, **kw: Unpack[_Kwargs2]
    ) -> np.floating: ...
    @overload  # 0d complexfloating
    def __call__(
        self, x: _ToComplex, /, out: _Out1[None] = None, *, dtype: _ToDTypeComplex | None = None, **kw: Unpack[_Kwargs2]
    ) -> np.complexfloating: ...
    @overload  # ?d +complexfloating, out: bound nd complexfloating
    def __call__(
        self,
        x: _nt.CoComplex_nd,
        /,
        out: _Out1[_InexactArrayT],
        *,
        dtype: _ToDTypeInexact | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _InexactArrayT: ...
    @overload  # nd float64
    def __call__(
        self,
        x: _nt.ToFloat64_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Float64ND: ...
    @overload  # ?d float64, out=...
    def __call__(
        self,
        x: _nt.ToFloat64_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Float64ND: ...
    @overload  # nd complex128
    def __call__(
        self,
        x: _nt.ToComplex128_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeComplex128 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Complex128ND: ...
    @overload  # ?d complex128, out=...
    def __call__(
        self,
        x: _nt.ToComplex128_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeComplex128 | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _Complex128ND: ...
    @overload  # nd +floating
    def __call__(
        self,
        x: _nt.CoFloating_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _FloatND: ...
    @overload  # ?d +floating, out=...
    def __call__(
        self, x: _nt.CoFloating_nd, /, out: EllipsisType, *, dtype: _ToDTypeFloat | None = None, **kw: Unpack[_Kwargs2]
    ) -> _FloatND: ...
    @overload  # nd complexfloating
    def __call__(
        self,
        x: _nt.ToComplex_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeComplex | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _ComplexND: ...
    @overload  # ?d complexfloating
    def __call__(
        self, x: _nt.ToComplex_nd, /, out: EllipsisType, *, dtype: _ToDTypeComplex | None = None, **kw: Unpack[_Kwargs2]
    ) -> _ComplexND: ...
    @overload  # nd +complexfloating
    def __call__(
        self,
        x: _nt.CoComplex_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeInexact | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d +complexfloating
    def __call__(
        self,
        x: _nt.CoComplex_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeInexact | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete] | Incomplete: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_FloatND | None] | EllipsisType = None,
        *,
        dtype: _ToDTypeInexact | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _CallIsNat(Protocol):
    @overload  # 0d datetime64 | timedelta64
    def __call__(
        self,
        x: _nt.co_datetime,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> np.bool_: ...
    @overload  # nd datetime64 | timedelta64
    def __call__(
        self,
        x: _nt.CoDateTime_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload  # ?d datetime64 | timedelta64, out: T
    def __call__(
        self,
        x: _nt.CoDateTime_nd,
        /,
        out: _Out1[_BoolArrayT],
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolArrayT: ...
    @overload  # ?d datetime64 | timedelta64, out=...
    def __call__(
        self,
        x: _nt.CoDateTime_1nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _CallSignbit(Protocol):
    @overload  # 0d floating
    def __call__(
        self, x: _CoFloat, /, out: _Out1[None] = None, *, dtype: _nt.ToDTypeBool | None = None, **kw: Unpack[_Kwargs2]
    ) -> np.bool_: ...
    @overload  # nd +floating
    def __call__(
        self,
        x: _nt.CoFloating_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload  # ?d floating, out: T
    def __call__(
        self,
        x: _nt.CoFloating_nd,
        /,
        out: _Out1[_BoolArrayT],
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolArrayT: ...
    @overload  # ?d floating, out=...
    def __call__(
        self,
        x: _nt.CoFloating_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_BoolND | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _CallLogical(Protocol):
    @overload
    def __call__(  # 0d generic, dtype: np.object_
        self, x: _ToScalar, /, out: _Out1[None] = None, *, dtype: _nt.ToDTypeObject, **kwargs: Unpack[_Kwargs2]
    ) -> bool: ...
    @overload
    def __call__(  # 0d +number
        self,
        x: _CoComplex,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> np.bool_: ...
    @overload
    def __call__(  # nd object_
        self,
        x: _nt.ToObject_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeObject | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ObjectND: ...
    @overload
    def __call__(  # ?d object_, out=...
        self,
        x: _nt.ToObject_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeObject | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ObjectND: ...
    @overload
    def __call__(  # nd +number | object, dtype: np.object_
        self,
        x: _nt.CoComplex_1nd | _nt.ToObject_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeObject,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ObjectND: ...
    @overload
    def __call__(  # ?d +number | object, out=..., dtype: np.object_
        self,
        x: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeObject,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ObjectND: ...
    @overload
    def __call__(  # ?d +number | object, out: T
        self,
        x: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # nd +number
    def __call__(
        self,
        x: _nt.CoComplex_1nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload
    def __call__(  # ?d +number, out=...
        self,
        x: _nt.CoComplex_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _BoolND: ...
    @overload
    def __call__(  # nd +number | object
        self,
        x: _nt.CoComplex_1nd | _nt.ToObject_1nd,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __call__(  # ?d +number | object, out=...
        self,
        x: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __call__(  # ?d +number | object
        self,
        x: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _nt.Array[Incomplete] | Incomplete: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_BoolND | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _Call11String(Protocol[_ScalarT_co]):
    @overload  # 0d string-like
    def __call__(
        self, x: _ToStringLike, /, out: _Out1[None] = None, *, dtype: None = None, **kw: Unpack[_Kwargs2]
    ) -> _ScalarT_co: ...
    @overload  # nd string-like
    def __call__(
        self,
        x: _nt.ToString_1nd | _nt.ToCharacter_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[_ScalarT_co]: ...
    @overload  # ?d string-like, out: T
    def __call__(
        self,
        x: _nt.ToString_nd | _nt.ToCharacter_nd,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # ?d string-like, out=...
    def __call__(
        self,
        x: _nt.ToString_nd | _nt.ToCharacter_nd,
        /,
        out: EllipsisType,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[_ScalarT_co]: ...
    @overload  # ?d string-like, dtype: T
    def __call__(
        self,
        x: _nt.ToString_1nd | _nt.ToCharacter_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d string-like, out=..., dtype: T
    def __call__(
        self,
        x: _nt.ToString_nd | _nt.ToCharacter_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs2],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?
    def __call__(
        self,
        x: _nt.ToString_nd | _nt.ToCharacter_nd | _CanArrayUFunc,
        /,
        out: _Out1[None] | EllipsisType = None,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _Call12(Protocol):
    @overload  # 0d, dtype: T
    def __call__(
        self, x: _ToScalar, /, *, out: _Out2[None] = ..., dtype: _ToDType[_ScalarT], **kw: Unpack[_Kwargs3]
    ) -> _Out2[_ScalarT]: ...
    @overload  # 0d
    def __call__(
        self, x: _ToScalar, /, *, out: _Out2[None] = ..., dtype: _nt.ToDType | None = None, **kw: Unpack[_Kwargs3]
    ) -> _Out2[Incomplete]: ...
    @overload  # ?d, out: (T1, None)
    def __call__(
        self, x: _nt.ToGeneric_nd, /, *, out: tuple[_ArrayT1, None], dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> tuple[_ArrayT1, _nt.Array]: ...
    @overload  # ?d, out: (None, T2)
    def __call__(
        self, x: _nt.ToGeneric_nd, /, *, out: tuple[None, _ArrayT2], dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> tuple[_nt.Array, _ArrayT2]: ...
    @overload  # ?d, out: (T1, T2)
    def __call__(
        self, x: _nt.ToGeneric_nd, /, *, out: tuple[_ArrayT1, _ArrayT2], dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload  # ?d, out=...
    def __call__(
        self, x: _nt.ToGeneric_nd, /, *, out: EllipsisType, dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> tuple[_nt.Array[Incomplete], _nt.Array[Incomplete]]: ...
    @overload  # ?d, out=..., dtype: T
    def __call__(
        self, x: _nt.ToGeneric_nd, /, *, out: EllipsisType, dtype: _ToDType[_ScalarT], **kw: Unpack[_Kwargs3]
    ) -> tuple[_nt.Array[_ScalarT], _nt.Array[_ScalarT]]: ...
    @overload  # nd, dtype: T
    def __call__(
        self, x: _nt.ToGeneric_1nd, /, *, out: _Out2[None] = ..., dtype: _ToDType[_ScalarT], **kw: Unpack[_Kwargs3]
    ) -> _Out2[_nt.Array[_ScalarT]]: ...
    @overload  # nd
    def __call__(
        self,
        x: _nt.ToGeneric_1nd,
        /,
        *,
        out: _Out2[_nt.Array | None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Out2[_nt.Array[Incomplete]]: ...
    @overload  # ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out2[_nt.Array | None] | EllipsisType = ...,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Out2[Incomplete]: ...

@type_check_only
class _Call21(Protocol):
    @overload  # 0d, 0d, dtype: T
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs3],
    ) -> _ScalarT: ...
    @overload  # 0d, 0d
    def __call__(
        self, x1: _ToScalar, x2: _ToScalar, /, out: _Out1[None] = None, *, dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> Incomplete: ...
    @overload  # ?d, ?d, out: T
    def __call__(
        self, x1: _nt.ToGeneric_nd, x2: _nt.ToGeneric_nd, /, out: _ArrayT, *, dtype: None = None, **kw: Unpack[_Kwargs3]
    ) -> _ArrayT: ...
    @overload  # ?d, nd, dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # nd, ?d, dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d, ?d, out=..., dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d, nd
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # nd, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d, ?d, out=...
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: EllipsisType,
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        x2: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> Incomplete: ...

@type_check_only
class _Call21Bool(Protocol):
    @overload  # 0d, 0d
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.bool_: ...
    @overload  # ?d, ?d, out: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolArrayT],
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolArrayT: ...
    @overload  # ?d, nd
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # nd, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # ?d, ?d, out=...
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # ?d, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolND | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND | Incomplete: ...
    @overload  # ?
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        x2: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        out: _Out1[_BoolND | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> Incomplete: ...

@type_check_only
class _Call21Float(Protocol):
    @overload  # 0d float64 | +integer, 0d float64 | +integer
    def __call__(
        self,
        x1: float | _nt.co_integer,
        x2: float | _nt.co_integer,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.float64: ...
    @overload  # 0d +float64, 0d ~float64
    def __call__(
        self,
        x1: _CoFloat,
        x2: _ToFloat64,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.float64: ...
    @overload  # 0d ~float64, 0d +float64
    def __call__(
        self,
        x1: _ToFloat64,
        x2: _CoFloat,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.float64: ...
    @overload  # 0d +floating, 0d +floating
    def __call__(
        self,
        x1: _CoFloat,
        x2: _CoFloat,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.floating: ...
    @overload  # ?d +floating, ?d +floating, out: T
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_nd,
        /,
        out: _Out1[_FloatArrayT],
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _FloatArrayT: ...
    @overload  # ?d +float64, nd ~float64
    def __call__(
        self,
        x1: _nt.CoFloat64_nd,
        x2: _nt.ToFloat64_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Float64ND: ...
    @overload  # nd ~float64, ?d +float64
    def __call__(
        self,
        x1: _nt.ToFloat64_1nd,
        x2: _nt.CoFloat64_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Float64ND: ...
    @overload  # ?d +float64, ?d ~float64, out=...
    def __call__(
        self,
        x1: _nt.CoFloat64_nd,
        x2: _nt.ToFloat64_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Float64ND: ...
    @overload  # ?d ~float64, ?d +float64, out=...
    def __call__(
        self,
        x1: _nt.ToFloat64_nd,
        x2: _nt.CoFloat64_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeFloat64 | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _Float64ND: ...
    @overload  # ?d +floating, ?d +floating, out=..., dtype: T
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _ToDType[_FloatT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_FloatT]: ...
    @overload  # ?d +floating, nd +floating, dtype: T
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_FloatT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_FloatT]: ...
    @overload  # nd +floating, ?d +floating, dtype: T
    def __call__(
        self,
        x1: _nt.CoFloating_1nd,
        x2: _nt.CoFloating_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDType[_FloatT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_FloatT]: ...
    @overload  # ?d +floating, nd ~floating
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _FloatND: ...
    @overload  # nd ~floating, ?d +floating
    def __call__(
        self,
        x1: _nt.CoFloating_1nd,
        x2: _nt.CoFloating_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _FloatND: ...
    @overload  # ?d +floating, ?d +floating, out=...
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _FloatND: ...
    @overload  # ?d +floating, ?d +floating
    def __call__(
        self,
        x1: _nt.CoFloating_nd,
        x2: _nt.CoFloating_nd,
        /,
        out: _Out1[_FloatND | None] = None,
        *,
        dtype: _ToDTypeFloat | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _FloatND | Incomplete: ...

# only used for private ufuncs
@type_check_only
class _Call21String(Protocol):
    @overload  # 0d string-like, 0d string-like
    def __call__(
        self,
        x1: _ToStringLike,
        x2: _ToStringLike,
        /,
        out: _nt.Array[Incomplete] | None = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> Incomplete: ...
    @overload  # nd string-like, ?d string-like
    def __call__(
        self,
        x1: _nt.ToString_1nd | _nt.ToCharacter_1nd,
        x2: _nt.ToString_nd | _nt.ToCharacter_nd,
        /,
        out: _nt.Array[Incomplete] | None = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d string-like, nd string-like
    def __call__(
        self,
        x1: _nt.ToString_nd | _nt.ToCharacter_nd,
        x2: _nt.ToString_1nd | _nt.ToCharacter_1nd,
        /,
        out: _nt.Array[Incomplete] | None = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...
    @overload  # ?d string-like, ?d string-like, out=...
    def __call__(
        self,
        x1: _nt.ToString_nd | _nt.ToCharacter_nd,
        x2: _nt.ToString_nd | _nt.ToCharacter_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...

@type_check_only
class _Call21Logical(Protocol):
    @overload  # 0d +number | object, 0d +number | object, dtype: object_
    def __call__(
        self,
        x1: _CoComplex | _nt._PyObject,
        x2: _CoComplex | _nt._PyObject,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeObject,
        **kw: Unpack[_Kwargs3],
    ) -> bool: ...
    @overload  # 0d +number, 0d +number
    def __call__(
        self,
        x1: _CoComplex,
        x2: _CoComplex,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> np.bool_: ...
    @overload  # ?d +number | object_, nd +number | object_, dtype: object_
    def __call__(
        self,
        x1: _nt.CoComplex_nd | _nt.ToObject_nd,
        x2: _nt.CoComplex_1nd | _nt.ToObject_1nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeObject,
        **kw: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload  # nd +number | object_, ?d +number | object_, dtype: object_
    def __call__(
        self,
        x1: _nt.CoComplex_1nd | _nt.ToObject_1nd,
        x2: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: _Out1[None] = None,
        *,
        dtype: _nt.ToDTypeObject,
        **kw: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload  # ?d +number | object_, ?d +number | object_, out=..., dtype: object_
    def __call__(
        self,
        x1: _nt.CoComplex_nd | _nt.ToObject_nd,
        x2: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeObject,
        **kw: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload  # nd +number | object_, nd +number | object_, out: bound nd array
    def __call__(
        self,
        x1: _nt.CoComplex_nd | _nt.ToObject_nd,
        x2: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: _Out1[_BoolArrayT],
        *,
        dtype: None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolArrayT: ...
    @overload  # ?d +number, nd +number
    def __call__(
        self,
        x1: _nt.CoComplex_nd,
        x2: _nt.CoComplex_1nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # nd +number, ?d +number
    def __call__(
        self,
        x1: _nt.CoComplex_1nd,
        x2: _nt.CoComplex_nd,
        /,
        out: _Out1[_BoolND | None] = None,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # ?d +number, ?d +number, out=...
    def __call__(
        self,
        x1: _nt.CoComplex_nd,
        x2: _nt.CoComplex_nd,
        /,
        out: EllipsisType,
        *,
        dtype: _nt.ToDTypeBool | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _BoolND: ...
    @overload  # ?d +number | object_, ?d +number | object_
    def __call__(
        self,
        x1: _nt.CoComplex_nd | _nt.ToObject_nd,
        x2: _nt.CoComplex_nd | _nt.ToObject_nd,
        /,
        out: _Out1[_nt.Array[Incomplete]] | EllipsisType | None = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete] | Incomplete: ...

# NOTE: Positional `out` arguments are are intentionally not supported
@type_check_only
class _Call22(Protocol):
    @overload  # 0d, 0d, dtype: bounTd
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        /,
        *,
        out: _Out2[None] = ...,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_ScalarT]: ...
    @overload  # 0d, 0d
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        /,
        *,
        out: _Out2[None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[Incomplete]: ...
    @overload  # nd, ?d, dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: _Out2[_nt.Array[_ScalarT] | None] = ...,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[_ScalarT]]: ...
    @overload  # ?d, nd, dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        *,
        out: _Out2[_nt.Array[_ScalarT] | None] = ...,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[_ScalarT]]: ...
    @overload  # ?d, ?d, out=..., dtype: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: EllipsisType,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[_ScalarT]]: ...
    @overload  # ?d, ?d, out: (T1, None)
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kw: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, Incomplete]: ...
    @overload  # ?d, ?d, out: (None, T2)
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kw: Unpack[_Kwargs4],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload  # ?d, ?d, out: (T1, T2)
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kw: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload  # nd, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: _Out2[None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[Incomplete]]: ...
    @overload  # ?d, nd
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        *,
        out: _Out2[None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[Incomplete]]: ...
    @overload  # ?d, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        *,
        out: EllipsisType,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[Incomplete]]: ...
    @overload  # ?, ?
    def __call__(
        self,
        x1: _nt.ToGeneric_nd | _CanArrayUFunc,
        x2: _nt.ToGeneric_nd | _CanArrayUFunc,
        /,
        *,
        out: _Out2[_nt.Array | None] | EllipsisType = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[Incomplete]: ...

# scalar for 1D array-likes; ndarray otherwise
@type_check_only
class _Call21G(Protocol):
    @overload  # ?d, ?d, out: T
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_g],
    ) -> _ArrayT: ...
    @overload  # ?d, ?d
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        *,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_g],
    ) -> Incomplete: ...

_AtE: TypeAlias = Callable[Concatenate[Any, Any, ...], None]
_At1: TypeAlias = Callable[[_CanArrayUFunc, _nt.CoInteger_nd], None]
_At2: TypeAlias = Callable[[_CanArrayUFunc, _nt.CoInteger_nd, _nt.ToGeneric_nd], None]

@type_check_only
class _ReduceE(Protocol):
    def __call__(self, a: Incomplete, /) -> Incomplete: ...

@type_check_only
class _Reduce2(Protocol):
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        /,
        axis: _ShapeLike | None = 0,
        dtype: _nt.ToDType | None = None,
        out: _nt.Array | EllipsisType | None = None,
        keepdims: bool = False,
        initial: _ToScalar | None = ...,
        where: _nt.ToBool_nd = True,
    ) -> Incomplete: ...

@type_check_only
class _AccumulateE(Protocol):
    def __call__(self, a: Incomplete, /) -> Incomplete: ...

@type_check_only
class _Accumulate2(Protocol):
    @overload  # ?d, out: T, /
    def __call__(self, a: _nt.ToGeneric_nd, /, axis: SupportsIndex, dtype: None, out: _ArrayT) -> _ArrayT: ...
    @overload  # ?d, *, out: T
    def __call__(
        self, a: _nt.ToGeneric_nd, /, axis: SupportsIndex = 0, dtype: None = None, *, out: _ArrayT
    ) -> _ArrayT: ...
    @overload  # ?d, dtype: T, /
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        /,
        axis: SupportsIndex,
        dtype: _ToDType[_ScalarT],
        out: _nt.Array[_ScalarT] | EllipsisType | None = None,
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d, *, dtype: T
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _ToDType[_ScalarT],
        out: _Out1[None] | EllipsisType = None,
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        /,
        axis: SupportsIndex = 0,
        dtype: _nt.ToDType | None = None,
        out: _nt.Array | EllipsisType | None = None,
    ) -> _nt.Array[Incomplete]: ...

@type_check_only
class _ReduceAtE(Protocol):
    def __call__(self, a: Incomplete, ixs: Incomplete, /) -> Incomplete: ...

@type_check_only
class _ReduceAt2(Protocol):
    @overload
    def __call__(
        self, a: _nt.ToGeneric_nd, ixs: _nt.CoInteger_nd, /, axis: SupportsIndex, dtype: None, out: _ArrayT
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        ixs: _nt.CoInteger_nd,
        /,
        axis: SupportsIndex = 0,
        dtype: None = None,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        ixs: _nt.CoInteger_nd,
        /,
        axis: SupportsIndex,
        dtype: _ToDType[_ScalarT],
        out: _nt.Array[_ScalarT] | EllipsisType | None = None,
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        ixs: _nt.CoInteger_nd,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _ToDType[_ScalarT],
        out: _nt.Array[_ScalarT] | EllipsisType | None = None,
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __call__(
        self,
        a: _nt.ToGeneric_nd,
        ixs: _nt.CoInteger_nd,
        /,
        out: _nt.Array | EllipsisType | None = None,
        axis: SupportsIndex = 0,
        dtype: _nt.ToDType | None = None,
    ) -> _nt.Array[Incomplete]: ...

_OuterE: TypeAlias = Callable[[Incomplete, Incomplete], Incomplete]

@type_check_only
class _Outer1(Protocol):
    @overload  # ?d, ?d, out: T
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        out: _Out1[_ArrayT],
        dtype: None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # ?d, ?d, dtype: T
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        out: _Out1[_nt.Array[_ScalarT] | None] | EllipsisType = None,
        dtype: _ToDType[_ScalarT],
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[_ScalarT]: ...
    @overload  # ?d, ?d
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3],
    ) -> _nt.Array[Incomplete]: ...

@type_check_only
class _Outer2(Protocol):
    @overload  # ?d, ?d, out: (T1, None)
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        dtype: _nt.ToDType | None = None,
        out: tuple[_ArrayT1, None],
        **kw: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _nt.Array[Incomplete]]: ...
    @overload  # ?d, ?d, out: (None, T2)
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        dtype: _nt.ToDType | None = None,
        out: tuple[None, _ArrayT2],
        **kw: Unpack[_Kwargs4],
    ) -> tuple[_nt.Array[Incomplete], _ArrayT2]: ...
    @overload  # ?d, ?d, out: (T1, T2)
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        dtype: _nt.ToDType | None = None,
        out: tuple[_ArrayT1, _ArrayT2],
        **kw: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload  # ?d, ?d, dtype: T
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        dtype: _ToDType[_ScalarT],
        out: _Out2[_nt.Array[_ScalarT] | None] | EllipsisType = ...,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[_ScalarT]]: ...
    @overload  # ?d, ?d
    def __call__(
        self,
        A: _nt.ToGeneric_nd,
        B: _nt.ToGeneric_nd,
        /,
        *,
        dtype: _nt.ToDType | None = None,
        out: _Out2[_nt.Array | None] | EllipsisType = ...,
        **kw: Unpack[_Kwargs4],
    ) -> _Out2[_nt.Array[Incomplete]]: ...

###
# specific ufunc aliases

_F11T = TypeVar("_F11T", bound=Callable[Concatenate[Incomplete, ...], Incomplete], default=_Call11)
_FT12 = TypeVar("_FT12", bound=Callable[Concatenate[Incomplete, ...], tuple[Incomplete, Incomplete]], default=_Call12)
_F21T = TypeVar("_F21T", bound=Callable[Concatenate[Incomplete, Incomplete, ...], Incomplete], default=_Call21)
_G21T = TypeVar("_G21T", bound=Callable[Concatenate[Incomplete, ...], Incomplete], default=_Call21G)
_F22T = TypeVar(
    "_F22T", bound=Callable[Concatenate[Incomplete, Incomplete, ...], tuple[Incomplete, Incomplete]], default=_Call22
)

_ufunc11 = TypeAliasType(
    "_ufunc11", np.ufunc[_F11T, _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE], type_params=(_F11T,)
)
_ufunc12 = TypeAliasType(
    "_ufunc12", np.ufunc[_FT12, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE], type_params=(_FT12,)
)
_ufunc21 = TypeAliasType(
    "_ufunc21", np.ufunc[_F21T, _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1], type_params=(_F21T,)
)
_gufunc21 = TypeAliasType(
    "_gufunc21", np.ufunc[_G21T, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer1], type_params=(_G21T,)
)
_ufunc22 = TypeAliasType(
    "_ufunc22", np.ufunc[_F22T, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer2], type_params=(_F22T,)
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
isnat: Final[_ufunc11[_CallIsNat]] = ...

# {[f]} -> ?
signbit: Final[_ufunc11[_CallSignbit]] = ...

# {?[uifc]Mm} -> ?
isfinite: Final[_ufunc11[_Call11Bool]] = ...
isinf: Final[_ufunc11[_Call11Bool]] = ...

# {[f]T} -> ?
isnan: Final[_ufunc11[_Call11Bool]] = ...

# {?[uifc]O} -> ?
# O -> O
logical_not: Final[_ufunc11[_CallLogical]] = ...

# {UT} -> ?
isnumeric: _ufunc11[_Call11String[np.bool_]]
isdecimal: _ufunc11[_Call11String[np.bool_]]

# {SUT} -> ?
isalnum: _ufunc11[_Call11String[np.bool_]]
isalpha: _ufunc11[_Call11String[np.bool_]]
isdigit: _ufunc11[_Call11String[np.bool_]]
islower: _ufunc11[_Call11String[np.bool_]]
isspace: _ufunc11[_Call11String[np.bool_]]
istitle: _ufunc11[_Call11String[np.bool_]]
isupper: _ufunc11[_Call11String[np.bool_]]

# {SUT} -> n
str_len: _ufunc11[_Call11String[np.intp]]

# {[ui]} -> B
# O -> O
bitwise_count: Final[_ufunc11] = ...

# {[f]} -> $1
spacing: Final[_ufunc11[_Call11Float]] = ...

# {[f]O} -> $1
# Note: https://github.com/numpy/numtype/pull/373#pullrequestreview-2708079543
cbrt: Final[_ufunc11[_Call11Float]] = ...
deg2rad: Final[_ufunc11[_Call11Float]] = ...
degrees: Final[_ufunc11[_Call11Float]] = ...
fabs: Final[_ufunc11[_Call11Float]] = ...
rad2deg: Final[_ufunc11[_Call11Float]] = ...
radians: Final[_ufunc11[_Call11Float]] = ...

# {[fc]O} -> $1
arccos: Final[_ufunc11[_Call11Inexact]] = ...
arccosh: Final[_ufunc11[_Call11Inexact]] = ...
arcsin: Final[_ufunc11[_Call11Inexact]] = ...
arcsinh: Final[_ufunc11[_Call11Inexact]] = ...
arctan: Final[_ufunc11[_Call11Inexact]] = ...
arctanh: Final[_ufunc11[_Call11Inexact]] = ...
cos: Final[_ufunc11[_Call11Inexact]] = ...
cosh: Final[_ufunc11[_Call11Inexact]] = ...
exp: Final[_ufunc11[_Call11Inexact]] = ...
exp2: Final[_ufunc11[_Call11Inexact]] = ...
expm1: Final[_ufunc11[_Call11Inexact]] = ...
log: Final[_ufunc11[_Call11Inexact]] = ...
log2: Final[_ufunc11[_Call11Inexact]] = ...
log10: Final[_ufunc11[_Call11Inexact]] = ...
log1p: Final[_ufunc11[_Call11Inexact]] = ...
rint: Final[_ufunc11[_Call11Inexact]] = ...
sin: Final[_ufunc11[_Call11Inexact]] = ...
sinh: Final[_ufunc11[_Call11Inexact]] = ...
sqrt: Final[_ufunc11[_Call11Inexact]] = ...
tan: Final[_ufunc11[_Call11Inexact]] = ...
tanh: Final[_ufunc11[_Call11Inexact]] = ...

# {?[ui]O} -> $1
invert: Final[_ufunc11] = ...

# {?[uif]O} -> $1
ceil: Final[_ufunc11] = ...
floor: Final[_ufunc11] = ...
trunc: Final[_ufunc11] = ...

# {?[uif]Om} -> $1
# F -> f
# D -> d
# G -> g
absolute: Final[_ufunc11] = ...

# {[uifc]O} -> $1
conjugate: Final[_ufunc11] = ...
conj = conjugate
reciprocal: Final[_ufunc11] = ...
square: Final[_ufunc11] = ...

# {[uifc]mO} -> $1
negative: Final[_ufunc11] = ...
positive: Final[_ufunc11] = ...
sign: Final[_ufunc11] = ...

# {SUT} -> $1
_lstrip_whitespace: _ufunc11[_Call11String[Any]]
_rstrip_whitespace: _ufunc11[_Call11String[Any]]
_strip_whitespace: _ufunc11[_Call11String[Any]]

# {?[uifc]MmO} -> $1
_ones_like: _ufunc11

###
# 1-in, 2-out

# {[f]} -> $1, i
frexp: Final[_ufunc12] = ...

# {[f]} -> $1, $1
modf: Final[_ufunc12] = ...

###
# 2-in, 1-out

# {?[uifc]OSUTV}, $1 -> ?
logical_and: Final[_ufunc21[_Call21Logical]] = ...
logical_or: Final[_ufunc21[_Call21Logical]] = ...
logical_xor: Final[_ufunc21[_Call21Logical]] = ...

# {?[uifc]MmOSUT}, $1 -> ?, (also accepts dtype: O)
equal: Final[_ufunc21[_Call21Bool]] = ...
not_equal: Final[_ufunc21[_Call21Bool]] = ...
greater: Final[_ufunc21[_Call21Bool]] = ...
greater_equal: Final[_ufunc21[_Call21Bool]] = ...
less: Final[_ufunc21[_Call21Bool]] = ...
less_equal: Final[_ufunc21[_Call21Bool]] = ...

# {[f]}, {il} -> $1
ldexp: Final[_ufunc21] = ...

# {dgDG}, $1 -> $1
float_power: Final[_ufunc21] = ...

# {[f]}, $1 -> $1
copysign: Final[_ufunc21[_Call21Float]] = ...
heaviside: Final[_ufunc21[_Call21Float]] = ...
logaddexp: Final[_ufunc21[_Call21Float]] = ...
logaddexp2: Final[_ufunc21[_Call21Float]] = ...
nextafter: Final[_ufunc21[_Call21Float]] = ...

# {[f]O}, $1 -> $1
arctan2: Final[_ufunc21] = ...
hypot: Final[_ufunc21] = ...

# {[fc]mO}, $1 -> $1
divide: Final[_ufunc21] = ...
true_divide = divide

# {[ui]O}, $1 -> $1
gcd: Final[_ufunc21] = ...
lcm: Final[_ufunc21] = ...
left_shift: Final[_ufunc21] = ...
right_shift: Final[_ufunc21] = ...

# {?[ui]O}, $1 -> $1
bitwise_and: Final[_ufunc21] = ...
bitwise_or: Final[_ufunc21] = ...
bitwise_xor: Final[_ufunc21] = ...

# {[uif]O}, $1 -> $1
fmod: Final[_ufunc21] = ...

# {[uif]mO}, $1 -> $1
floor_divide: Final[_ufunc21] = ...
remainder: Final[_ufunc21] = ...
mod = remainder

# {[uifc]O}, $1 -> $1
power: Final[_ufunc21] = ...

# {?[uifc]O}, $1 -> $1
matmul: Final[_gufunc21] = ...  # (n?, k), (k, m?) -> (n?, m?)
matvec: Final[_gufunc21] = ...  # (m, n), (n) -> (m)
vecdot: Final[_gufunc21] = ...  # (n), (n) -> ()
vecmat: Final[_gufunc21] = ...  # (n), (n, m) -> (m)

# {?[uifc]mO}, $1 -> $1
multiply: Final[_ufunc21] = ...
subtract: Final[_ufunc21] = ...

# {?[uifc]MmO}, $1 -> $1
fmax: Final[_ufunc21] = ...
fmin: Final[_ufunc21] = ...

# {?[uifc]MmOT}, $1 -> $1
maximum: Final[_ufunc21] = ...
minimum: Final[_ufunc21] = ...

# {?[uifc]MmOSUT}, $1 -> $1
add: Final[_ufunc21] = ...

_expandtabs: _ufunc21
_expandtabs_length: _ufunc21
_lstrip_chars: _ufunc21[_Call21String]
_rstrip_chars: _ufunc21[_Call21String]
_strip_chars: _ufunc21[_Call21String]
_zfill: _ufunc21

###
# 2-in, 2-out

# {[uif]}, $1 -> $1, $1
# m, m -> q, m
divmod: Final[_ufunc22] = ...

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
class _PyCall11(Protocol[_OutT_co]):
    @overload
    def __call__(
        self, x: _ToScalar, /, out: _Out1[None] = None, dtype: _nt.ToDType | None = None, **kwargs: Unpack[_Kwargs2]
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x: _nt.ToGeneric_1nd,
        /,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: _Out1[_ArrayT], dtype: _nt.ToDType | None = None, **kwargs: Unpack[_Kwargs2]
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self, x: _nt.ToGeneric_nd, /, out: EllipsisType, dtype: _nt.ToDType | None = None, **kwargs: Unpack[_Kwargs2]
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> Incomplete: ...

@type_check_only
class _PyCall21(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        /,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        /,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: EllipsisType,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        /,
        out: _Out1[_ArrayT],
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        x2: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> Incomplete: ...

@type_check_only
class _PyCall3N1(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ToScalar,
        x2: _ToScalar,
        x3: _ToScalar,
        /,
        *xs: _ToScalar,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        x3: _nt.ToGeneric_1nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_1nd,
        x3: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        x2: _nt.ToGeneric_nd,
        x3: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Out1[None] = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        x3: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Out1[_ArrayT],
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        x2: _nt.ToGeneric_nd,
        x3: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: EllipsisType,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ObjectND: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        x2: _CanArrayUFunc | _nt.ToGeneric_nd,
        x3: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        *xs: _CanArrayUFunc | _nt.ToGeneric_nd,
        out: _Out1[_nt.Array | None] | EllipsisType = None,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> Incomplete: ...

@type_check_only
class _PyCall1N2(Protocol[_OutT1_co, _OutT2_co]):
    @overload
    def __call__(
        self,
        x1: _ToScalar,
        /,
        *xs: _ToScalar,
        out: tuple[None, None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_],
    ) -> tuple[_OutT1_co, _OutT2_co]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: tuple[None, None] = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_],
    ) -> tuple[_ObjectND, _ObjectND]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: EllipsisType,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_],
    ) -> tuple[_ObjectND, _ObjectND]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        *xs: _CanArrayUFunc | _nt.ToGeneric_nd,
        out: _Out2[_nt.Array | None] | EllipsisType = ...,
        dtype: _nt.ToDType | None = None,
        **kw: Unpack[_Kwargs3_],
    ) -> Incomplete: ...

@type_check_only
class _PyCall1N2N(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ToScalar,
        /,
        *xs: _ToScalar,
        out: _Tuple2_[None] = ...,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_OutT_co]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_1nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Tuple2_[None] = ...,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_ObjectND]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: _Tuple2_[_ArrayT],
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_ArrayT]: ...
    @overload
    def __call__(
        self,
        x1: _nt.ToGeneric_nd,
        /,
        *xs: _nt.ToGeneric_nd,
        out: EllipsisType,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_ObjectND]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | _nt.ToGeneric_nd,
        /,
        *xs: _CanArrayUFunc | _nt.ToGeneric_nd,
        out: _Tuple2_[_nt.Array | None] | EllipsisType = ...,
        dtype: _nt.ToDType | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> Incomplete: ...

_pyfunc11 = TypeAliasType(
    "_pyfunc11", np.ufunc[_PyCall11[_OutT], _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE], type_params=(_OutT,)
)
_pyfunc21 = TypeAliasType(
    "_pyfunc21", np.ufunc[_PyCall21[_OutT], _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1], type_params=(_OutT,)
)
_pyfunc3n1 = TypeAliasType(
    "_pyfunc3n1", np.ufunc[_PyCall3N1[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE], type_params=(_OutT,)
)
_pyfunc1n2 = TypeAliasType(
    "_pyfunc1n2",
    np.ufunc[_PyCall1N2[_OutT1, _OutT2], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT1, _OutT2),
)
_pyfunc1n2n = TypeAliasType(
    "_pyfunc1n2n", np.ufunc[_PyCall1N2N[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE], type_params=(_OutT,)
)

# NOTE: We can't use e.g. `Concatenate[Any, ...]`, as that causes mypy to reject every function...
@overload  # (a) -> T
def frompyfunc(
    f: Callable[[Incomplete], _T], /, nin: _Eq1, nout: _Eq1, *, identity: object = None
) -> _pyfunc11[_T]: ...
@overload  # (a, b) -> T
def frompyfunc(
    f: Callable[[Incomplete, Incomplete], _T], /, nin: _Eq2, nout: _Eq1, *, identity: object = None
) -> _pyfunc21[_T]: ...
@overload  # (a, b, c, ...) -> T
def frompyfunc(f: Callable[..., _T], /, nin: _Ge3, nout: _Eq1, *, identity: object = None) -> _pyfunc3n1[_T]: ...
@overload  # (a, ...) -> (T1, T2)
def frompyfunc(  # type: ignore[overload-overlap]  # mypy-only false positive
    f: Callable[..., tuple[_T1, _T2]], /, nin: _Ge1, nout: _Eq2, *, identity: object = None
) -> _pyfunc1n2[_T1, _T2]: ...
@overload  # (a, ...) -> (T1, T2, *(T, ...))
def frompyfunc(
    f: Callable[..., tuple[_T1, _T2, *tuple[_T, ...]]], /, nin: _Ge1, nout: _Ge2, *, identity: object = None
) -> _pyfunc1n2n[_T1 | _T2 | _T]: ...
@overload
def frompyfunc(
    f: Callable[..., Incomplete], /, nin: SupportsIndex, nout: SupportsIndex, *, identity: object = None
) -> np.ufunc: ...
