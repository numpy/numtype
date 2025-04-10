# Interface to the NEP 50 "safe" promotion rules that are embedded within the numeric
# scalar types as the type-check-only `__promote__` method.
# https://numpy.org/neps/nep-0050-scalar-promotion.html

from typing import Any, Protocol, type_check_only
from typing_extensions import TypeAliasType, TypeVar

import numpy as np

__all__ = ["CanCast0D", "CanCastND", "CanNEP50", "MatchND", "PromoteWith", "PromoteWith0D"]

_T_co = TypeVar("_T_co", covariant=True)
_BelowT_contra = TypeVar("_BelowT_contra", bound=np.generic, contravariant=True)
_AboveT_contra = TypeVar("_AboveT_contra", bound=np.generic, contravariant=True, default=Any)
_OtherT_contra = TypeVar("_OtherT_contra", contravariant=True)
_MatchT_co = TypeVar("_MatchT_co", bound=np.generic, covariant=True, default=Any)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)

@type_check_only
class CanNEP50(Protocol[_BelowT_contra, _AboveT_contra, _MatchT_co]):
    def __nep50__(self, below: _BelowT_contra, above: _AboveT_contra, /) -> _MatchT_co: ...

@type_check_only
class _CanNEP50Rule0(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule0__(self, other: _OtherT_contra, /) -> _T_co: ...

@type_check_only
class _CanNEP50Rule1(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule1__(self, other: _OtherT_contra, /) -> _T_co: ...

@type_check_only
class _CanNEP50Rule2(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule2__(self, other: _OtherT_contra, /) -> _T_co: ...

@type_check_only
class _CanNEP50Rule3(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule3__(self, other: _OtherT_contra, /) -> _T_co: ...

@type_check_only
class _CanNEP50Rule4(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule4__(self, other: _OtherT_contra, /) -> _T_co: ...

@type_check_only
class _CanNEP50Rule5(Protocol[_OtherT_contra, _T_co]):
    def __nep50_rule5__(self, other: _OtherT_contra, /) -> _T_co: ...

_WithT = TypeVar("_WithT")
_OutT = TypeVar("_OutT", bound=np.generic)

PromoteWith = TypeAliasType(
    "PromoteWith",
    _CanNEP50Rule0[_WithT, _OutT]
    | _CanNEP50Rule1[_WithT, _OutT]
    | _CanNEP50Rule2[_WithT, _OutT]
    | _CanNEP50Rule3[_WithT, _OutT]
    | _CanNEP50Rule4[_WithT, _OutT]
    | _CanNEP50Rule5[_WithT, _OutT],
    type_params=(_WithT, _OutT),
)
PromoteWith0D = TypeAliasType(
    "PromoteWith0D",
    MatchND[tuple[()], PromoteWith[_WithT, _OutT]],
    type_params=(_WithT, _OutT),
)

###

@type_check_only
class _HasType(Protocol[_T_co]):
    @property
    def type(self, /) -> type[_T_co]: ...

@type_check_only
class MatchND(Protocol[_ShapeT_co, _T_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _HasType[_T_co]: ...

# TODO(jorenham): Rename these

@type_check_only
class CanCast0D(Protocol[_BelowT_contra, _AboveT_contra, _MatchT_co]):
    @property
    def shape(self, /) -> tuple[()]: ...
    @property
    def dtype(self, /) -> _HasType[CanNEP50[_BelowT_contra, _AboveT_contra, _MatchT_co]]: ...

@type_check_only
class CanCastND(Protocol[_ShapeT_co, _BelowT_contra, _AboveT_contra, _MatchT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _HasType[CanNEP50[_BelowT_contra, _AboveT_contra, _MatchT_co]]: ...
