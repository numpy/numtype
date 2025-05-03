from typing_extensions import TypeAliasType

__all__ = [
    "Shape",
    "Shape0",
    "Shape1",
    "Shape1_",
    "Shape2",
    "Shape2_",
    "Shape3",
    "Shape3_",
    "Shape4",
    "Shape4_",
]

Shape = TypeAliasType("Shape", tuple[int, ...])
Shape0 = TypeAliasType("Shape0", tuple[()])
Shape1 = TypeAliasType("Shape1", tuple[int])
Shape2 = TypeAliasType("Shape2", tuple[int, int])
Shape3 = TypeAliasType("Shape3", tuple[int, int, int])
Shape4 = TypeAliasType("Shape4", tuple[int, int, int, int])

Shape1_ = TypeAliasType("Shape1_", tuple[int, *tuple[int, ...]])
Shape2_ = TypeAliasType("Shape2_", tuple[int, int, *tuple[int, ...]])
Shape3_ = TypeAliasType("Shape3_", tuple[int, int, int, *tuple[int, ...]])
Shape4_ = TypeAliasType("Shape4_", tuple[int, int, int, int, *tuple[int, ...]])
