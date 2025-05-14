from typing import Any, Generic, Protocol, Self, TypeAlias, final, type_check_only
from typing_extensions import TypeAliasType, TypeVar

from ._shape import Shape, Shape0, Shape0N, Shape1, Shape1N, Shape2, Shape2N, Shape3, Shape3N, Shape4, Shape4N

__all__ = [
    "HasRankGE",
    "HasRankLE",
    "Rank",
    "Rank0",
    "Rank0N",
    "Rank1",
    "Rank1N",
    "Rank2",
    "Rank2N",
    "Rank3",
    "Rank3N",
    "Rank4",
    "Rank4N",
]

###

_Shape00: TypeAlias = Shape0
_Shape01: TypeAlias = _Shape00 | Shape1
_Shape02: TypeAlias = _Shape01 | Shape2
_Shape03: TypeAlias = _Shape02 | Shape3
_Shape04: TypeAlias = _Shape03 | Shape4

###

_UpperT = TypeVar("_UpperT", bound=Shape)
_LowerT = TypeVar("_LowerT", bound=Shape)
_RankT = TypeVar("_RankT", bound=Shape, default=Any)

HasRankLE = TypeAliasType(
    "HasRankLE",
    _HasShape[Shape0 | _HasOwnShape[_UpperT] | _CanBroadcast[Any, _UpperT, _RankT]],
    type_params=(_UpperT, _RankT),
)
HasRankGE = TypeAliasType(
    "HasRankGE",
    _HasShape[_LowerT | _CanBroadcast[_LowerT, Any, _RankT]],
    type_params=(_LowerT, _RankT),
)

###

_ShapeT_co = TypeVar("_ShapeT_co", bound=Shape | _HasOwnShape | _CanBroadcast, covariant=True)

@type_check_only
class _HasShape(Protocol[_ShapeT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...

_FromT_contra = TypeVar("_FromT_contra", default=Any, contravariant=True)
_ToT_contra = TypeVar("_ToT_contra", bound=Shape, default=Any, contravariant=True)
_EquivT_co = TypeVar("_EquivT_co", bound=Shape, default=Any, covariant=True)

@final
@type_check_only
class _CanBroadcast(Protocol[_FromT_contra, _ToT_contra, _EquivT_co]):
    def __broadcast__(self, from_: _FromT_contra, to: _ToT_contra, /) -> _EquivT_co: ...

# This double shape-type parameter is a sneaky way to annotate a doubly-bound nominal type range,
# e.g. `_HasOwnShape[Shape2N, Shape0N]` accepts `Shape2N`, `Shape1N`, and `Shape0N`, but
# rejects `Shape3N` and `Shape1`. Besides brevity, it also works around several mypy bugs that
# are related to "unions vs joins".

_OwnShapeT_contra = TypeVar("_OwnShapeT_contra", bound=Shape, default=Any, contravariant=True)
_OwnShapeT_co = TypeVar("_OwnShapeT_co", bound=Shape, default=_OwnShapeT_contra, covariant=True)
_OwnShapeT = TypeVar("_OwnShapeT", bound=tuple[Any, ...], default=Any)

@final
@type_check_only
class _HasOwnShape(Protocol[_OwnShapeT_contra, _OwnShapeT_co]):
    def __own_shape__(self, shape: _OwnShapeT_contra, /) -> _OwnShapeT_co: ...

###
# TODO(jorenham): embed the array-like types, e.g. `Sequence[Sequence[T]]`

@type_check_only
class _BaseRank(Generic[_FromT_contra, _OwnShapeT, _ToT_contra]):
    def __broadcast__(self, from_: _FromT_contra, to: _ToT_contra, /) -> Self: ...
    def __own_shape__(self, shape: _OwnShapeT, /) -> _OwnShapeT: ...

@type_check_only
class _BaseRankM(
    _BaseRank[_FromT_contra | _HasOwnShape[_ToT_contra, Shape], _OwnShapeT, _ToT_contra],
    Generic[_FromT_contra, _OwnShapeT, _ToT_contra],
): ...

@final
@type_check_only
class Rank0(_BaseRankM[_Shape00, Shape0, Shape0N], tuple[()]): ...

@final
@type_check_only
class Rank1(_BaseRankM[_Shape01, Shape1, Shape1N], tuple[int]): ...

@final
@type_check_only
class Rank2(_BaseRankM[_Shape02, Shape2, Shape2N], tuple[int, int]): ...

@final
@type_check_only
class Rank3(_BaseRankM[_Shape03, Shape3, Shape3N], tuple[int, int, int]): ...

@final
@type_check_only
class Rank4(_BaseRankM[_Shape04, Shape4, Shape4N], tuple[int, int, int, int]): ...

# this emulates `AnyOf`, rather than a `Union`.
@type_check_only
class _BaseRankMToN(_BaseRank[Shape0N, _OwnShapeT, _OwnShapeT], Generic[_OwnShapeT]): ...

@final
@type_check_only
class Rank(_BaseRankMToN[Shape0N], tuple[int, ...]): ...

@final
@type_check_only
class Rank1N(_BaseRankMToN[Shape1N], tuple[int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank2N(_BaseRankMToN[Shape2N], tuple[int, int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank3N(_BaseRankMToN[Shape3N], tuple[int, int, int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank4N(_BaseRankMToN[Shape4N], tuple[int, int, int, int, *tuple[int, ...]]): ...

Rank0N: TypeAlias = Rank
