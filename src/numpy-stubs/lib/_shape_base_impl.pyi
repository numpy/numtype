from collections.abc import Callable, Sequence
from typing import Any, Concatenate, Protocol, SupportsIndex, overload, type_check_only
from typing_extensions import ParamSpec, TypeVar

import numpy as np
from numpy._core.shape_base import vstack as row_stack
from numpy._typing import (
    ArrayLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeUInt_co,
    _ShapeLike,
)

__all__ = [
    "apply_along_axis",
    "apply_over_axes",
    "array_split",
    "column_stack",
    "dsplit",
    "dstack",
    "expand_dims",
    "hsplit",
    "kron",
    "put_along_axis",
    "row_stack",
    "split",
    "take_along_axis",
    "tile",
    "vsplit",
]

_P = ParamSpec("_P")
_SCT = TypeVar("_SCT", bound=np.generic)

# Signature of `__array_wrap__`
@type_check_only
class _ArrayWrap(Protocol):
    def __call__(
        self,
        array: NDArray[Any],
        context: tuple[np.ufunc, tuple[Any, ...], int] | None = ...,
        return_scalar: bool = ...,
        /,
    ) -> Any: ...

@type_check_only
class _SupportsArrayWrap(Protocol):
    @property
    def __array_wrap__(self) -> _ArrayWrap: ...

def take_along_axis(arr: _SCT | NDArray[_SCT], indices: NDArray[np.integer], axis: int | None) -> NDArray[_SCT]: ...
def put_along_axis(arr: NDArray[_SCT], indices: NDArray[np.integer], values: ArrayLike, axis: int | None) -> None: ...
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[NDArray[Any], _P], _ArrayLike[_SCT]],
    axis: SupportsIndex,
    arr: ArrayLike,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> NDArray[_SCT]: ...
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[NDArray[Any], _P], Any],
    axis: SupportsIndex,
    arr: ArrayLike,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> NDArray[Any]: ...
def apply_over_axes(
    func: Callable[[NDArray[Any], int], NDArray[_SCT]],
    a: ArrayLike,
    axes: int | Sequence[int],
) -> NDArray[_SCT]: ...
@overload
def expand_dims(a: _ArrayLike[_SCT], axis: _ShapeLike) -> NDArray[_SCT]: ...
@overload
def expand_dims(a: ArrayLike, axis: _ShapeLike) -> NDArray[Any]: ...
@overload
def column_stack(tup: Sequence[_ArrayLike[_SCT]]) -> NDArray[_SCT]: ...
@overload
def column_stack(tup: Sequence[ArrayLike]) -> NDArray[Any]: ...
@overload
def dstack(tup: Sequence[_ArrayLike[_SCT]]) -> NDArray[_SCT]: ...
@overload
def dstack(tup: Sequence[ArrayLike]) -> NDArray[Any]: ...
@overload
def array_split(ary: _ArrayLike[_SCT], indices_or_sections: _ShapeLike, axis: SupportsIndex = ...) -> list[NDArray[_SCT]]: ...
@overload
def array_split(ary: ArrayLike, indices_or_sections: _ShapeLike, axis: SupportsIndex = ...) -> list[NDArray[Any]]: ...
@overload
def split(ary: _ArrayLike[_SCT], indices_or_sections: _ShapeLike, axis: SupportsIndex = ...) -> list[NDArray[_SCT]]: ...
@overload
def split(ary: ArrayLike, indices_or_sections: _ShapeLike, axis: SupportsIndex = ...) -> list[NDArray[Any]]: ...
@overload
def hsplit(ary: _ArrayLike[_SCT], indices_or_sections: _ShapeLike) -> list[NDArray[_SCT]]: ...
@overload
def hsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...
@overload
def vsplit(ary: _ArrayLike[_SCT], indices_or_sections: _ShapeLike) -> list[NDArray[_SCT]]: ...
@overload
def vsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...
@overload
def dsplit(ary: _ArrayLike[_SCT], indices_or_sections: _ShapeLike) -> list[NDArray[_SCT]]: ...
@overload
def dsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...
@overload
def get_array_wrap(*args: _SupportsArrayWrap) -> _ArrayWrap: ...
@overload
def get_array_wrap(*args: object) -> _ArrayWrap | None: ...
@overload
def kron(a: _ArrayLikeBool_co, b: _ArrayLikeBool_co) -> NDArray[np.bool]: ...  # type: ignore[misc]
@overload
def kron(a: _ArrayLikeUInt_co, b: _ArrayLikeUInt_co) -> NDArray[np.unsignedinteger]: ...  # type: ignore[misc]
@overload
def kron(a: _ArrayLikeInt_co, b: _ArrayLikeInt_co) -> NDArray[np.signedinteger]: ...  # type: ignore[misc]
@overload
def kron(a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co) -> NDArray[np.floating]: ...  # type: ignore[misc]
@overload
def kron(a: _ArrayLikeComplex_co, b: _ArrayLikeComplex_co) -> NDArray[np.complexfloating]: ...
@overload
def kron(a: _ArrayLikeObject_co, b: Any) -> NDArray[np.object_]: ...
@overload
def kron(a: Any, b: _ArrayLikeObject_co) -> NDArray[np.object_]: ...
@overload
def tile(A: _ArrayLike[_SCT], reps: int | Sequence[int]) -> NDArray[_SCT]: ...
@overload
def tile(A: ArrayLike, reps: int | Sequence[int]) -> NDArray[Any]: ...
