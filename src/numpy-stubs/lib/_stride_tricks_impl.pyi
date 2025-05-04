from collections.abc import Iterable
from typing import Any, SupportsIndex, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._typing import ArrayLike, _ArrayLike, _ShapeLike

__all__ = ["broadcast_arrays", "broadcast_shapes", "broadcast_to"]

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

class DummyArray:
    __array_interface__: dict[str, Any]
    base: _nt.Array | None
    def __init__(self, interface: dict[str, Any], base: _nt.Array | None = ...) -> None: ...

@overload
def as_strided(
    x: _ArrayLike[_ScalarT],
    shape: Iterable[int] | None = ...,
    strides: Iterable[int] | None = ...,
    subok: bool = ...,
    writeable: bool = ...,
) -> _nt.Array[_ScalarT]: ...
@overload
def as_strided(
    x: ArrayLike,
    shape: Iterable[int] | None = ...,
    strides: Iterable[int] | None = ...,
    subok: bool = ...,
    writeable: bool = ...,
) -> _nt.Array: ...
@overload
def sliding_window_view(
    x: _ArrayLike[_ScalarT],
    window_shape: _ShapeLike,
    axis: SupportsIndex | None = ...,
    *,
    subok: bool = ...,
    writeable: bool = ...,
) -> _nt.Array[_ScalarT]: ...
@overload
def sliding_window_view(
    x: ArrayLike,
    window_shape: _ShapeLike,
    axis: SupportsIndex | None = ...,
    *,
    subok: bool = ...,
    writeable: bool = ...,
) -> _nt.Array: ...
@overload
def broadcast_to(array: _ArrayLike[_ScalarT], shape: _ShapeLike, subok: bool = ...) -> _nt.Array[_ScalarT]: ...
@overload
def broadcast_to(array: ArrayLike, shape: _ShapeLike, subok: bool = ...) -> _nt.Array: ...
def broadcast_shapes(*args: _ShapeLike) -> _nt.Shape: ...
def broadcast_arrays(*args: ArrayLike, subok: bool = ...) -> tuple[_nt.Array, ...]: ...
