from typing import Any, Never, TypeAlias
from typing_extensions import TypeAliasType

__all__ = [
    "AnyShape",
    "NeitherShape",
    "Shape",
    "Shape0",
    "Shape0N",
    "Shape1",
    "Shape1N",
    "Shape2",
    "Shape2N",
    "Shape3",
    "Shape3N",
    "Shape4",
    "Shape4N",
    "ShapeN",
]

Shape = TypeAliasType("Shape", tuple[int, ...])
AnyShape = TypeAliasType("AnyShape", tuple[Any, ...])
NeitherShape = TypeAliasType("NeitherShape", tuple[Never, ...])

# TODO: remove `| Rank0` once python/mypy#19110 is fixed
Shape0 = TypeAliasType("Shape0", tuple[()])
Shape1 = TypeAliasType("Shape1", tuple[int])
Shape2 = TypeAliasType("Shape2", tuple[int, int])
Shape3 = TypeAliasType("Shape3", tuple[int, int, int])
Shape4 = TypeAliasType("Shape4", tuple[int, int, int, int])
ShapeN: TypeAlias = Shape

Shape0N: TypeAlias = Shape
Shape1N = TypeAliasType("Shape1N", tuple[int, *tuple[int, ...]])
Shape2N = TypeAliasType("Shape2N", tuple[int, int, *tuple[int, ...]])
Shape3N = TypeAliasType("Shape3N", tuple[int, int, int, *tuple[int, ...]])
Shape4N = TypeAliasType("Shape4N", tuple[int, int, int, int, *tuple[int, ...]])
