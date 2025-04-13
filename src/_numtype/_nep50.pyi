# Interface to the NEP 50 "safe" promotion rules that are embedded within the numeric
# scalar types as the type-check-only `__promote__` method.
# https://numpy.org/neps/nep-0050-scalar-promotion.html

from typing import Any, Protocol, TypeAlias, type_check_only
from typing_extensions import TypeAliasType, TypeVar

import numpy as np

__all__ = [
    "Casts",
    "CastsArray",
    "CastsScalar",
    "CastsWith",
    "CastsWithArray",
    "CastsWithComplex",
    "CastsWithFloat",
    "CastsWithInt",
    "CastsWithScalar",
]

###

_LikeT_co = TypeVar("_LikeT_co", covariant=True)

_ScalarIn: TypeAlias = np.generic | str
_ScalarInT = TypeVar("_ScalarInT", bound=_ScalarIn)
_ScalarInT_contra = TypeVar("_ScalarInT_contra", bound=_ScalarIn, contravariant=True)

_ScalarOut: TypeAlias = np.generic
_ScalarOutT = TypeVar("_ScalarOutT", bound=_ScalarOut, default=Any)
_ScalarOutT_co = TypeVar("_ScalarOutT_co", bound=_ScalarOut, covariant=True)
_ScalarOutT_contra = TypeVar("_ScalarOutT_contra", bound=_ScalarOut, contravariant=True)

_Shape: TypeAlias = tuple[int, ...]
_ShapeT = TypeVar("_ShapeT", bound=_Shape, default=_Shape)
_ShapeT_co = TypeVar("_ShapeT_co", bound=_Shape, covariant=True)

###

@type_check_only
class _CanNEP50(Protocol[_ScalarOutT_contra, _ScalarInT_contra, _ScalarOutT_co]):
    def __nep50__(self, below: _ScalarOutT_contra, above: _ScalarInT_contra, /) -> _ScalarOutT_co: ...

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
    def shape(self, /) -> tuple[()]: ...
    @property
    def dtype(self, /) -> _HasType[_LikeT_co]: ...

###

Casts = TypeAliasType(
    "Casts",
    _LikeNumeric[_CanNEP50[_ScalarOutT, Any, Any], _ShapeT],
    type_params=(_ScalarOutT, _ShapeT),
)
CastsArray = TypeAliasType(
    "CastsArray",
    _LikeArray[_CanNEP50[_ScalarOutT, Any, Any], _ShapeT],
    type_params=(_ScalarOutT, _ShapeT),
)
CastsScalar = TypeAliasType(
    "CastsScalar",
    _LikeScalar[_CanNEP50[_ScalarOutT, Any, Any]],
    type_params=(_ScalarOutT,),
)

#
_CastWith: TypeAlias = (
    _CanNEP50[Any, _ScalarInT, _ScalarOutT]
    | _CanNEP50Rule0[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule1[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule2[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule3[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule4[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule5[_ScalarInT, _ScalarOutT]
    | _CanNEP50Rule6[_ScalarInT, _ScalarOutT]
)
CastsWith = TypeAliasType(
    "CastsWith",
    _LikeNumeric[_CastWith[_ScalarInT, _ScalarOutT], _ShapeT],
    type_params=(_ScalarInT, _ScalarOutT, _ShapeT),
)
CastsWithArray = TypeAliasType(
    "CastsWithArray",
    _LikeArray[_CastWith[_ScalarInT, _ScalarOutT], _ShapeT],
    type_params=(_ScalarInT, _ScalarOutT, _ShapeT),
)
CastsWithScalar = TypeAliasType(
    "CastsWithScalar",
    _LikeScalar[_CastWith[_ScalarInT, _ScalarOutT]],
    type_params=(_ScalarInT, _ScalarOutT),
)

#
CastsWithBool: TypeAlias = _CanNEP50Bool[_ScalarOutT]
CastsWithInt: TypeAlias = _CanNEP50Int[_ScalarOutT]
CastsWithFloat: TypeAlias = _CanNEP50Float[_ScalarOutT]
CastsWithComplex: TypeAlias = _CanNEP50Complex[_ScalarOutT]
