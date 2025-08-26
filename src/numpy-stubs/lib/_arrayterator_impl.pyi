# pyright: reportIncompatibleMethodOverride=false

from collections.abc import Generator
from types import EllipsisType
from typing import Any, Final, Generic, TypeAlias, overload
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np

__all__ = ["Arrayterator"]

###

# TODO: use `Shape` instead of `AnyShape` once python/mypy#19110 is fixed
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.AnyShape, default=_nt.Shape, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_AnyIndex: TypeAlias = EllipsisType | int | slice | tuple[EllipsisType | int | slice, ...]

###

# NOTE: In reality `Arrayterator` does not actually inherit from `ndarray`, but its `__getattr__ method does wrap
# around the former and thus has access to all its methods
class Arrayterator(np.ndarray[_ShapeT_co, _DTypeT_co], Generic[_ShapeT_co, _DTypeT_co]):
    var: np.ndarray[_ShapeT_co, _DTypeT_co]  # type: ignore[assignment]
    buf_size: Final[int | None]
    start: Final[list[int]]
    stop: Final[list[int]]
    step: Final[list[int]]

    # unlike ndarray, the Arrayterator shape has no setter
    @property  # type: ignore[misc]
    @override
    # NOTE: This constrained typevar use is a workaround for a mypy bug
    # def shape(self: _nt.HasInnerShape[_ShapeT] | ndarray[_ShapeT2]) -> _ShapeT | _ShapeT2: ...  # noqa: ERA001
    def shape(self) -> _ShapeT_co: ...

    #
    @property
    @override
    def flat(self: Arrayterator[Any, np.dtype[_ScalarT]]) -> Generator[_ScalarT]: ...  # type: ignore[override]

    #
    def __init__(self, /, var: np.ndarray[_ShapeT_co, _DTypeT_co], buf_size: int | None = None) -> None: ...  # pyright: ignore[reportInconsistentConstructor]
    @override
    def __getitem__(self, index: _AnyIndex, /) -> Arrayterator[_nt.AnyShape, _DTypeT_co]: ...  # type: ignore[override]
    @override
    def __iter__(self) -> Generator[np.ndarray[_nt.AnyShape, _DTypeT_co]]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __array__(
        self, /, dtype: _DTypeT_co | None = None, copy: bool | None = None
    ) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __array__(self, /, dtype: _DTypeT, copy: bool | None = None) -> np.ndarray[_ShapeT_co, _DTypeT]: ...
