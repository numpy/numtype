from collections.abc import Generator, Iterator
from types import EllipsisType
from typing import Any, TypeAlias, TypeVar

import numpy as np

__all__ = ["Arrayterator"]

_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[Any], covariant=True)
_SCT = TypeVar("_SCT", bound=np.generic)

_AnyIndex: TypeAlias = EllipsisType | int | slice | tuple[EllipsisType | int | slice, ...]

###

# NOTE: In reality `Arrayterator` does not actually inherit from `ndarray`, # but its `__getattr__ method does wrap around the
# former and thus has access to all its methods
class Arrayterator(np.ndarray[_ShapeT_co, _DTypeT_co]):
    var: np.ndarray[_ShapeT_co, _DTypeT_co]  # type: ignore[assignment]
    buf_size: int | None
    start: list[int]
    stop: list[int]
    step: list[int]

    @property
    def shape(self) -> _ShapeT_co: ...
    @property
    def flat(self: Arrayterator[Any, np.dtype[_SCT]]) -> Generator[_SCT]: ...

    #
    def __init__(self, var: np.ndarray[_ShapeT_co, _DTypeT_co], buf_size: int | None = ...) -> None: ...
    def __array__(self, dtype: None = ..., copy: bool | None = ...) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    def __getitem__(self, index: _AnyIndex, /) -> Arrayterator[Any, _DTypeT_co]: ...
    def __iter__(self) -> Iterator[np.ndarray[Any, _DTypeT_co]]: ...
