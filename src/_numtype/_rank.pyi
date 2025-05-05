from typing import Any, Generic, Protocol, Self, TypeAlias, final, type_check_only
from typing_extensions import TypeAliasType, TypeVar

from ._shape import (
    Shape,
    Shape as Shape0ToN,
    Shape0,
    Shape1,
    Shape1N as Shape1ToN,
    Shape2,
    Shape2N as Shape2ToN,
    Shape3,
    Shape3N as Shape3ToN,
    Shape4,
    Shape4N as Shape4ToN,
)

__all__ = [
    "Broadcasts",
    "BroadcastsTo",
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

_Shape0To0: TypeAlias = Shape0
_Shape0To1: TypeAlias = _Shape0To0 | Shape1
_Shape0To2: TypeAlias = _Shape0To1 | Shape2
_Shape0To3: TypeAlias = _Shape0To2 | Shape3
_Shape0To4: TypeAlias = _Shape0To3 | Shape4

###

_ToT = TypeVar("_ToT", bound=Shape)
_FromT = TypeVar("_FromT", bound=Shape)
_RankT = TypeVar("_RankT", bound=Shape, default=Any)

_BroadcastableShape = TypeAliasType(
    "_BroadcastableShape",
    _FromT | _CanBroadcastFrom[_FromT, _RankT],
    type_params=(_FromT, _RankT),
)

BroadcastsTo = TypeAliasType(
    "BroadcastsTo",
    _HasRank[_CanBroadcastTo[_ToT, _RankT]],
    type_params=(_ToT, _RankT),
)
Broadcasts = TypeAliasType(
    "Broadcasts",
    _HasRank[_BroadcastableShape[_FromT, _RankT]],
    type_params=(_FromT, _RankT),
)

###

_ShapeT_co = TypeVar(
    "_ShapeT_co",
    bound=Shape | _HasOwnShape | _CanBroadcastFrom | _CanBroadcastTo,
    covariant=True,
)

@type_check_only
class _HasShape(Protocol[_ShapeT_co]):
    @property
    def shape(self, /) -> _ShapeT_co: ...

_ShapeT = TypeVar("_ShapeT", bound=Shape)

@final
@type_check_only
class _HasRank(Protocol[_ShapeT_co]):
    @property
    def shape(self: _HasShape[_ShapeT], /) -> _ShapeT: ...

_FromT_contra = TypeVar("_FromT_contra", default=Any, contravariant=True)
_ToT_contra = TypeVar("_ToT_contra", bound=Shape, default=Any, contravariant=True)
_RankT_co = TypeVar("_RankT_co", bound=Shape, default=Any, covariant=True)

@final
@type_check_only
class _CanBroadcastFrom(Protocol[_FromT_contra, _RankT_co]):
    def __broadcast_from__(self, from_: _FromT_contra, /) -> _RankT_co: ...

@final
@type_check_only
class _CanBroadcastTo(Protocol[_ToT_contra, _RankT_co]):
    def __broadcast_to__(self, to: _ToT_contra, /) -> _RankT_co: ...

# This double shape-type parameter is a sneaky way to annotate a doubly-bound nominal type range,
# e.g. `_HasOwnShape[Shape2ToN, Shape0ToN]` accepts `Shape2ToN`, `Shape1ToN`, and `Shape0ToN`, but
# rejects `Shape3ToN` and `Shape1`. Besides brevity, it also works around several mypy bugs that
# are related to "unions vs joins".

_OwnShapeT_contra = TypeVar("_OwnShapeT_contra", bound=Shape, default=Any, contravariant=True)
_OwnShapeT_co = TypeVar("_OwnShapeT_co", bound=Shape, default=_OwnShapeT_contra, covariant=True)

@final
@type_check_only
class _HasOwnShape(Protocol[_OwnShapeT_contra, _OwnShapeT_co]):
    def __own_shape__(self, shape: _OwnShapeT_contra, /) -> _OwnShapeT_co: ...

###
# TODO(jorenham): embed the array-like types, e.g. `Sequence[Sequence[T]]`

_OwnShapeT = TypeVar("_OwnShapeT", bound=tuple[Any, ...], default=Any)

@type_check_only
class _BaseRank(Generic[_FromT_contra, _ToT_contra, _OwnShapeT]):
    def __broadcast_from__(self, from_: _FromT_contra, /) -> Self: ...
    def __broadcast_to__(self, to: _ToT_contra, /) -> Self: ...
    def __own_shape__(self, shape: _OwnShapeT, /) -> _OwnShapeT: ...

@type_check_only
class _BaseRankM(
    _BaseRank[_FromT_contra | _HasOwnShape[_ToT_contra, Shape], _ToT_contra, _OwnShapeT],
    Generic[_FromT_contra, _ToT_contra, _OwnShapeT],
): ...

@final
@type_check_only
class Rank0(_BaseRankM[_Shape0To0, Shape0ToN, Shape0], tuple[()]): ...

@final
@type_check_only
class Rank1(_BaseRankM[_Shape0To1, Shape1ToN, Shape1], tuple[int]): ...

@final
@type_check_only
class Rank2(_BaseRankM[_Shape0To2, Shape2ToN, Shape2], tuple[int, int]): ...

@final
@type_check_only
class Rank3(_BaseRankM[_Shape0To3, Shape3ToN, Shape3], tuple[int, int, int]): ...

@final
@type_check_only
class Rank4(_BaseRankM[_Shape0To4, Shape4ToN, Shape4], tuple[int, int, int, int]): ...

# this emulates `AnyOf`, rather than a `Union`.
@type_check_only
class _BaseRankMToN(_BaseRank[Shape0ToN, _OwnShapeT, _OwnShapeT], Generic[_OwnShapeT]): ...

@final
@type_check_only
class Rank(_BaseRankMToN[Shape0ToN], tuple[int, ...]): ...

@final
@type_check_only
class Rank1N(_BaseRankMToN[Shape1ToN], tuple[int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank2N(_BaseRankMToN[Shape2ToN], tuple[int, int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank3N(_BaseRankMToN[Shape3ToN], tuple[int, int, int, *tuple[int, ...]]): ...

@final
@type_check_only
class Rank4N(_BaseRankMToN[Shape4ToN], tuple[int, int, int, int, *tuple[int, ...]]): ...

Rank0N: TypeAlias = Rank
