# Interface to the NEP 50 "safe" promotion rules that are associated with the numeric
# scalar types as the type-check-only `__nep50*__` methods.
# https://numpy.org/neps/nep-0050-scalar-promotion.html

from typing import Any, Protocol, TypeAlias, type_check_only
from typing_extensions import TypeAliasType, TypeVar

import numpy as np
from numpy._typing import _NestedSequence  # noqa: PLC2701

from . import _shape
from ._rank import Rank0

__all__ = [
    "Casts",
    "CastsArray",
    "CastsScalar",
    "CastsWith",
    "CastsWithArray",
    "CastsWithBuiltin",
    "CastsWithComplex",
    "CastsWithFloat",
    "CastsWithInt",
    "CastsWithScalar",
]

###

_LikeT = TypeVar("_LikeT")
_LikeT_co = TypeVar("_LikeT_co", covariant=True)

_BuitinT = TypeVar("_BuitinT")
_BuitinT_co = TypeVar("_BuitinT_co", covariant=True)

_ScalarIn: TypeAlias = np.generic | str
_OtherScalarT = TypeVar("_OtherScalarT", bound=_ScalarIn)
_ScalarInT_contra = TypeVar("_ScalarInT_contra", bound=_ScalarIn, contravariant=True)

_ScalarOut: TypeAlias = np.generic
_IntoScalarT = TypeVar("_IntoScalarT", bound=_ScalarOut, default=Any)
_ScalarOutT_co = TypeVar("_ScalarOutT_co", bound=_ScalarOut, covariant=True)
_ScalarOutT_contra = TypeVar("_ScalarOutT_contra", bound=_ScalarOut, contravariant=True)

_ShapeT = TypeVar("_ShapeT", bound=_shape.Shape, default=Any)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_shape.Shape, covariant=True)

###

@type_check_only
class _CanNEP50(Protocol[_ScalarOutT_contra, _ScalarInT_contra, _ScalarOutT_co]):
    def __nep50__(self, into: _ScalarOutT_contra, from_: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

# Due to limitations in mypy/pyright, we cannot combine these individual `__nep50_rule__` into a single
# overloaded method.

@type_check_only
class _CanNEP50Rule0(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule0__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule1(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule1__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule2(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule2__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule3(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule3__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule4(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule4__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule5(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule5__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Rule6(Protocol[_ScalarInT_contra, _ScalarOutT_co]):
    def __nep50_rule6__(self, other: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

#
@type_check_only
class _CanNEP50Builtin(Protocol[_BuitinT_co, _ScalarOutT_co]):
    def __nep50_builtin__(self, /) -> tuple[_BuitinT_co, _ScalarOutT_co]: ...

@type_check_only
class _CanNEP50Bool(Protocol[_ScalarOutT_co]):
    def __nep50_bool__(self, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Int(Protocol[_ScalarOutT_co]):
    def __nep50_int__(self, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Float(Protocol[_ScalarOutT_co]):
    def __nep50_float__(self, /) -> _ScalarOutT_co: ...

@type_check_only
class _CanNEP50Complex(Protocol[_ScalarOutT_co]):
    def __nep50_complex__(self, /) -> _ScalarOutT_co: ...

#
@type_check_only
class _HasType(Protocol[_LikeT_co]):
    @property
    def type(self, /) -> type[_LikeT_co]: ...

@type_check_only
class _LikeNumeric(Protocol[_LikeT_co, _ShapeT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _HasType[_LikeT_co]: ...

@type_check_only
class _LikeArray(Protocol[_LikeT_co, _ShapeT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _HasType[_LikeT_co]: ...
    def __len__(self, /) -> int: ...

@type_check_only
class _LikeScalar(Protocol[_LikeT_co]):
    @property
    def __inner_shape__(self, /) -> Rank0: ...
    @property
    def dtype(self, /) -> _HasType[_LikeT_co]: ...

###

_SequenceND: TypeAlias = _LikeT | _NestedSequence[_LikeT]

# Accepts anything with `.shape` and `.dtype` if its `dtype.type` scalar-type can be safe-cast into `_IntoScalarT`.
# E.g. `Casts[np.int16]` will accept arrays or scalars of `np.uint8` and `np.bool`, but not `np.uint16` or `np.float32`.
# An optional second `_ShapeT` type-parameter can be used to further restrict the rank (shape-type).
Casts = TypeAliasType(
    "Casts", _SequenceND[_LikeNumeric[_CanNEP50[_IntoScalarT, Any, Any], _ShapeT]], type_params=(_IntoScalarT, _ShapeT)
)
# Same as `Casts`, but only for array-like types, rejecting "bare" scalars like `np.float64`.
CastsArray = TypeAliasType(
    "CastsArray",
    _SequenceND[_LikeArray[_CanNEP50[_IntoScalarT, Any, Any], _ShapeT]],
    type_params=(_IntoScalarT, _ShapeT),
)
# Same as `Casts`, but only for scalar-like types, rejecting array-like types, including zero-dimensional arrays.
CastsScalar = TypeAliasType("CastsScalar", _LikeScalar[_CanNEP50[_IntoScalarT, Any, Any]], type_params=(_IntoScalarT,))

_CastWith: TypeAlias = (
    _CanNEP50[Any, _OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule0[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule1[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule2[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule3[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule4[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule5[_OtherScalarT, _IntoScalarT]
    | _CanNEP50Rule6[_OtherScalarT, _IntoScalarT]
)
# Accepts anything with `.shape` and `.dtype` if its `dtype.type` scalar-type can be safe-cast into `_IntoScalarT`
# together with `_OtherScalarT` according to any of the NEP 50 rules. Accepts both array-likes and scalars.
CastsWith = TypeAliasType(
    "CastsWith",
    _SequenceND[_LikeNumeric[_CastWith[_OtherScalarT, _IntoScalarT], _ShapeT]],
    type_params=(_OtherScalarT, _IntoScalarT, _ShapeT),
)
# Same as `CastsWith`, but only for array-like types, rejecting "bare" scalars like `np.float64`.
CastsWithArray = TypeAliasType(
    "CastsWithArray",
    _SequenceND[_LikeArray[_CastWith[_OtherScalarT, _IntoScalarT], _ShapeT]],
    type_params=(_OtherScalarT, _IntoScalarT, _ShapeT),
)
# Same as `CastsWith`, but only for scalar-like types, rejecting array-like types, including zero-dimensional arrays.
CastsWithScalar = TypeAliasType(
    "CastsWithScalar", _LikeScalar[_CastWith[_OtherScalarT, _IntoScalarT]], type_params=(_OtherScalarT, _IntoScalarT)
)

#
CastsWithBuiltin: TypeAlias = _LikeNumeric[_CanNEP50Builtin[_BuitinT, _IntoScalarT], _ShapeT]
CastsWithBool: TypeAlias = _LikeNumeric[_CanNEP50Bool[_IntoScalarT], _ShapeT]
CastsWithInt: TypeAlias = _LikeNumeric[_CanNEP50Int[_IntoScalarT], _ShapeT]
CastsWithFloat: TypeAlias = _LikeNumeric[_CanNEP50Float[_IntoScalarT], _ShapeT]
CastsWithComplex: TypeAlias = _LikeNumeric[_CanNEP50Complex[_IntoScalarT], _ShapeT]
