from typing import Any, Generic, Protocol, Self, TypeAlias, final, type_check_only
from typing_extensions import TypeAliasType, TypeVar, TypeVarTuple, override

from ._shape import AnyShape, Shape, Shape0, Shape1, Shape1N, Shape2, Shape2N, Shape3, Shape3N, Shape4, Shape4N

__all__ = [
    "HasInnerShape",
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

_Shape01: TypeAlias = Shape0 | Shape1
_Shape02: TypeAlias = _Shape01 | Shape2
_Shape03: TypeAlias = _Shape02 | Shape3
_Shape04: TypeAlias = _Shape03 | Shape4

###

# TODO(jorenham): remove `| Rank0 | Rank` once python/mypy#19110 is fixed
_UpperT = TypeVar("_UpperT", bound=Shape | Rank0 | Rank)
_LowerT = TypeVar("_LowerT", bound=Shape | Rank0 | Rank)
_RankT = TypeVar("_RankT", bound=Shape, default=Any)

# TODO(jorenham): remove `| Rank0 | Rank` once python/mypy#19110 is fixed
_RankLE: TypeAlias = _CanBroadcast[Any, _UpperT, _RankT] | Shape0 | Rank0 | Rank
# TODO(jorenham): remove `| Rank` once python/mypy#19110 is fixed
_RankGE: TypeAlias = _CanBroadcast[_LowerT, Any, _RankT] | _LowerT | Rank

HasRankLE = TypeAliasType("HasRankLE", _HasInnerShape[_RankLE[_UpperT, _RankT]], type_params=(_UpperT, _RankT))
HasRankGE = TypeAliasType("HasRankGE", _HasInnerShape[_RankGE[_LowerT, _RankT]], type_params=(_LowerT, _RankT))

_ShapeT = TypeVar("_ShapeT", bound=Shape)

# for unwrapping potential rank types as shape tuples
HasInnerShape = TypeAliasType("HasInnerShape", _HasInnerShape[_HasOwnShape[Any, _ShapeT]], type_params=(_ShapeT,))

###

_ShapeLikeT_co = TypeVar("_ShapeLikeT_co", bound=Shape | _HasOwnShape | _CanBroadcast[Any, Any], covariant=True)

_FromT_contra = TypeVar("_FromT_contra", contravariant=True)
_ToT_contra = TypeVar("_ToT_contra", bound=tuple[Any, ...], contravariant=True)
_EquivT_co = TypeVar("_EquivT_co", bound=Shape, default=Any, covariant=True)

# __broadcast__ is the type-check-only interface order of ranks
@final
@type_check_only
class _CanBroadcast(Protocol[_FromT_contra, _ToT_contra, _EquivT_co]):
    def __broadcast__(self, from_: _FromT_contra, to: _ToT_contra, /) -> _EquivT_co: ...

# __inner_shape__ is similar to `shape`, but directly exposes the `Rank` type.
@final
@type_check_only
class _HasInnerShape(Protocol[_ShapeLikeT_co]):
    @property
    def __inner_shape__(self, /) -> _ShapeLikeT_co: ...

_OwnShapeT_contra = TypeVar("_OwnShapeT_contra", bound=tuple[Any, ...], default=Any, contravariant=True)
_OwnShapeT_co = TypeVar("_OwnShapeT_co", bound=Shape, default=_OwnShapeT_contra, covariant=True)

# This double shape-type parameter is a sneaky way to annotate a doubly-bound nominal type range,
# e.g. `_HasOwnShape[Shape2N, Shape0N]` accepts `Shape2N`, `Shape1N`, and `Shape0N`, but
# rejects `Shape3N` and `Shape1`. Besides brevity, it also works around several mypy bugs that
# are related to "unions vs joins".
@final
@type_check_only
class _HasOwnShape(Protocol[_OwnShapeT_contra, _OwnShapeT_co]):
    def __own_shape__(self, shape: _OwnShapeT_contra, /) -> _OwnShapeT_co: ...

###
# TODO(jorenham): embed the array-like types, e.g. `Sequence[Sequence[T]]`

_Ts = TypeVarTuple("_Ts")  # should only contain `int`s

# https://github.com/python/mypy/issues/19093
@type_check_only
class BaseRank(tuple[*_Ts], Generic[*_Ts]):
    def __broadcast__(self, from_: tuple[*_Ts], to: tuple[*_Ts], /) -> Self: ...
    def __own_shape__(self, shape: tuple[*_Ts], /) -> tuple[*_Ts]: ...

@final
@type_check_only
class Rank0(BaseRank[()]):
    @override
    def __broadcast__(self, from_: Shape0 | _HasOwnShape[Shape, Any], to: Shape, /) -> Self: ...

@final
@type_check_only
class Rank1(BaseRank[int]):
    @override
    def __broadcast__(self, from_: _Shape01 | _HasOwnShape[Shape1N, Any], to: Shape1N, /) -> Self: ...

@final
@type_check_only
class Rank2(BaseRank[int, int]):
    @override
    def __broadcast__(self, from_: _Shape02 | _HasOwnShape[Shape2N, Any], to: Shape2N, /) -> Self: ...

@final
@type_check_only
class Rank3(BaseRank[int, int, int]):
    @override
    def __broadcast__(self, from_: _Shape03 | _HasOwnShape[Shape3N, Any], to: Shape3N, /) -> Self: ...

@final
@type_check_only
class Rank4(BaseRank[int, int, int, int]):
    @override
    def __broadcast__(self, from_: _Shape04 | _HasOwnShape[Shape4N, Any], to: Shape4N, /) -> Self: ...

# these emulates `AnyOf` (gradual union), rather than a `Union`.

@final
@type_check_only
class Rank(BaseRank[*tuple[int, ...]]):
    @override
    def __broadcast__(self, from_: AnyShape, to: tuple[*_Ts], /) -> Self: ...

@final
@type_check_only
class Rank1N(BaseRank[int, *tuple[int, ...]]):
    @override
    def __broadcast__(self, from_: AnyShape, to: Shape1N, /) -> Self: ...

@final
@type_check_only
class Rank2N(BaseRank[int, int, *tuple[int, ...]]):
    @override
    def __broadcast__(self, from_: AnyShape, to: Shape2N, /) -> Self: ...

@final
@type_check_only
class Rank3N(BaseRank[int, int, int, *tuple[int, ...]]):
    @override
    def __broadcast__(self, from_: AnyShape, to: Shape3N, /) -> Self: ...

@final
@type_check_only
class Rank4N(BaseRank[int, int, int, int, *tuple[int, ...]]):
    @override
    def __broadcast__(self, from_: AnyShape, to: Shape4N, /) -> Self: ...

Rank0N: TypeAlias = Rank
