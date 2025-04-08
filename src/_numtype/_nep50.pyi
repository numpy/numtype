# Interface to the NEP 50 "safe" promotion rules that are embedded within the numeric
# scalar types as the type-check-only `__promote__` method.
# https://numpy.org/neps/nep-0050-scalar-promotion.html

from typing import Any, Protocol, type_check_only
from typing_extensions import TypeVar

import numpy as np

__all__ = ["CanCast", "CanCast0D", "CanCastND"]

_T_co = TypeVar("_T_co", covariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_ToScalarT_contra = TypeVar("_ToScalarT_contra", bound=np.generic, contravariant=True)
_FromScalarT_contra = TypeVar("_FromScalarT_contra", bound=np.generic, contravariant=True, default=Any)
_SelfScalarT_co = TypeVar("_SelfScalarT_co", bound=np.generic, covariant=True, default=Any)

@type_check_only
class _HasType(Protocol[_T_co]):
    @property
    def type(self, /) -> type[_T_co]: ...

@type_check_only
class CanCast(Protocol[_ToScalarT_contra, _FromScalarT_contra, _SelfScalarT_co]):
    def __nep50__(self, to: _ToScalarT_contra, from_: _FromScalarT_contra, /) -> _SelfScalarT_co: ...

@type_check_only
class CanCast0D(Protocol[_ToScalarT_contra, _FromScalarT_contra, _SelfScalarT_co]):
    @property
    def shape(self, /) -> tuple[()]: ...
    @property
    def dtype(self, /) -> _HasType[CanCast[_ToScalarT_contra, _FromScalarT_contra, _SelfScalarT_co]]: ...

@type_check_only
class CanCastND(Protocol[_ShapeT_co, _ToScalarT_contra, _FromScalarT_contra, _SelfScalarT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _HasType[CanCast[_ToScalarT_contra, _FromScalarT_contra, _SelfScalarT_co]]: ...
