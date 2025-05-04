from typing import Any, Protocol, Self, TypeAlias, final, type_check_only
from typing_extensions import TypeAliasType, TypeVar

from ._shape import (
    Shape,
    Shape as Shape0ToN,
    Shape0,
    Shape1,
    Shape1_ as Shape1ToN,
    Shape2,
    Shape2_ as Shape2ToN,
    Shape3,
    Shape3_ as Shape3ToN,
    Shape4,
    Shape4_ as Shape4ToN,
)

__all__ = [
    "Broadcastable",
    "Rank0",
    "Rank0ToN",
    "Rank1",
    "Rank1ToN",
    "Rank2",
    "Rank2ToN",
    "Rank3",
    "Rank3ToN",
    "Rank4",
    "Rank4ToN",
]

###

_ToT = TypeVar("_ToT", bound=Shape)
_ToT_contra = TypeVar("_ToT_contra", bound=Shape, contravariant=True)
_FromT = TypeVar("_FromT", bound=Shape)
_FromT_contra = TypeVar("_FromT_contra", bound=Shape, default=Any, contravariant=True)
_RankT = TypeVar("_RankT", bound=_HasShape[Any], default=Any)
_RankT_co = TypeVar("_RankT_co", default=Any, covariant=True)
_ShapeT_contra = TypeVar("_ShapeT_contra", contravariant=True)
_ShapeT_co = TypeVar("_ShapeT_co", covariant=True, default=_ShapeT_contra)

###

_Shape0To0: TypeAlias = Shape0
_Shape0To1: TypeAlias = _Shape0To0 | Shape1
_Shape0To2: TypeAlias = _Shape0To1 | Shape2
_Shape0To3: TypeAlias = _Shape0To2 | Shape3
_Shape0To4: TypeAlias = _Shape0To3 | Shape4

###

@type_check_only
class _CanBroadcast(Protocol[_ToT_contra, _FromT_contra, _RankT_co]):
    def __broadcast__(self, to: _ToT_contra, from_: _FromT_contra, /) -> _RankT_co: ...

# This double shape-type parameter is a sneaky way to annotate a doubly-bound nominal type range,
# e.g. `_HasShape[Shape2ToN, Shape0ToN]` accepts `Shape2ToN`, `Shape1ToN`, and `Shape0ToN`, but
# rejects `Shape3ToN` and `Shape1`. Besides brevity, it also works around several mypy bugs that
# are related to "unions vs joins".
@type_check_only
class _HasShape(Protocol[_ShapeT_contra, _ShapeT_co]):
    def __shape__(self, shape: _ShapeT_contra, /) -> _ShapeT_co: ...

###
# TODO(jorenham): embed the array-like types, e.g. `Sequence[Sequence[T]]`

@final
@type_check_only
class Rank0(tuple[()], _HasShape[Shape0, Shape0]):
    def __broadcast__(self, to: Shape0ToN, from_: _HasShape[Shape0ToN, Shape0ToN], /) -> Self: ...

@type_check_only
class Rank1(tuple[int], _HasShape[Shape1, Shape1]):
    def __broadcast__(self, to: Shape1ToN, from_: _Shape0To1 | _HasShape[Shape1ToN, Shape0ToN], /) -> Self: ...

@final
@type_check_only
class Rank2(tuple[int, int], _HasShape[Shape2, Shape2]):
    def __broadcast__(self, to: Shape2ToN, from_: _Shape0To2 | _HasShape[Shape2ToN, Shape0ToN], /) -> Self: ...

@final
@type_check_only
class Rank3(tuple[int, int, int], _HasShape[Shape3, Shape3]):
    def __broadcast__(self, to: Shape3ToN, from_: _Shape0To3 | _HasShape[Shape3ToN, Shape0ToN], /) -> Self: ...

@final
@type_check_only
class Rank4(tuple[int, int, int, int], _HasShape[Shape4, Shape4]):
    def __broadcast__(self, to: Shape4ToN, from_: _Shape0To4 | _HasShape[Shape4ToN, Shape0ToN], /) -> Self: ...

###
# These emulate `AnyOf`, rather than a `Union`.

@final
@type_check_only
class Rank0ToN(tuple[int, ...], _HasShape[Shape0ToN, Shape0ToN]):
    def __broadcast__(self, to: Shape0ToN, from_: Shape0ToN, /) -> Self: ...

@final
@type_check_only
class Rank1ToN(tuple[int, *tuple[int, ...]], _HasShape[Shape1ToN, Shape1ToN]):
    def __broadcast__(self, to: Shape1ToN, from_: Shape0ToN, /) -> Self: ...

@final
@type_check_only
class Rank2ToN(tuple[int, int, *tuple[int, ...]], _HasShape[Shape2ToN, Shape2ToN]):
    def __broadcast__(self, to: Shape2ToN, from_: Shape0ToN, /) -> Self: ...

@final
@type_check_only
class Rank3ToN(tuple[int, int, int, *tuple[int, ...]], _HasShape[Shape3ToN, Shape3ToN]):
    def __broadcast__(self, to: Shape3ToN, from_: Shape0ToN, /) -> Self: ...

@final
@type_check_only
class Rank4ToN(tuple[int, int, int, int, *tuple[int, ...]], _HasShape[Shape4ToN, Shape4ToN]):
    def __broadcast__(self, to: Shape4ToN, from_: Shape0ToN, /) -> Self: ...

###

Broadcastable = TypeAliasType("Broadcastable", _CanBroadcast[_ToT, Any, _RankT], type_params=(_ToT, _RankT))
Broadcaster = TypeAliasType("Broadcaster", _FromT | _CanBroadcast[Any, _FromT, _RankT], type_params=(_FromT, _RankT))
