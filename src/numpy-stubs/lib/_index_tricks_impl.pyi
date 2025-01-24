from collections.abc import Sequence
from typing import (
    Any,
    Generic,
    Literal,
    SupportsIndex,
    TypeVar,
    overload,
)

import numpy as np
from numpy import (
    bytes_,
    complex128,
    dtype,
    float64,
    int_,
    # Circumvent a naming conflict with `AxisConcatenator.matrix`
    matrix as _Matrix,
    ndarray,
    ndenumerate,
    ndindex,
    str_,
)
from numpy._core.multiarray import ravel_multi_index, unravel_index
from numpy._typing import (
    # Arrays
    ArrayLike,
    # DTypes
    DTypeLike,
    NDArray,
    _FiniteNestedSequence,
    _NestedSequence,
    # Shapes
    _Shape,
    _SupportsDType,
)

__all__ = [
    "c_",
    "diag_indices",
    "diag_indices_from",
    "fill_diagonal",
    "index_exp",
    "ix_",
    "mgrid",
    "ndenumerate",
    "ndindex",
    "ogrid",
    "r_",
    "ravel_multi_index",
    "s_",
    "unravel_index",
]

_T = TypeVar("_T")
_DType = TypeVar("_DType", bound=dtype[Any])
_BoolType = TypeVar("_BoolType", Literal[True], Literal[False])
_TupType = TypeVar("_TupType", bound=tuple[Any, ...])
_ArrayType = TypeVar("_ArrayType", bound=NDArray[Any])

@overload
def ix_(*args: _FiniteNestedSequence[_SupportsDType[_DType]]) -> tuple[ndarray[_Shape, _DType], ...]: ...
@overload
def ix_(*args: str | _NestedSequence[str]) -> tuple[NDArray[str_], ...]: ...
@overload
def ix_(*args: bytes | _NestedSequence[bytes]) -> tuple[NDArray[bytes_], ...]: ...
@overload
def ix_(*args: bool | _NestedSequence[bool]) -> tuple[NDArray[np.bool], ...]: ...
@overload
def ix_(*args: int | _NestedSequence[int]) -> tuple[NDArray[int_], ...]: ...
@overload
def ix_(*args: float | _NestedSequence[float]) -> tuple[NDArray[float64], ...]: ...
@overload
def ix_(*args: complex | _NestedSequence[complex]) -> tuple[NDArray[complex128], ...]: ...

class nd_grid(Generic[_BoolType]):
    sparse: _BoolType
    def __init__(self, sparse: _BoolType = ...) -> None: ...
    @overload
    def __getitem__(
        self: nd_grid[Literal[False]],
        key: slice | Sequence[slice],
    ) -> NDArray[Any]: ...
    @overload
    def __getitem__(
        self: nd_grid[Literal[True]],
        key: slice | Sequence[slice],
    ) -> tuple[NDArray[Any], ...]: ...

class MGridClass(nd_grid[Literal[False]]):
    def __init__(self) -> None: ...

mgrid: MGridClass

class OGridClass(nd_grid[Literal[True]]):
    def __init__(self) -> None: ...

ogrid: OGridClass

class AxisConcatenator:
    axis: int
    matrix: bool
    ndmin: int
    trans1d: int
    def __init__(
        self,
        axis: int = ...,
        matrix: bool = ...,
        ndmin: int = ...,
        trans1d: int = ...,
    ) -> None: ...
    @staticmethod
    @overload
    def concatenate(  # type: ignore[misc]
        *a: ArrayLike, axis: SupportsIndex = ..., out: None = ...
    ) -> NDArray[Any]: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: SupportsIndex = ..., out: _ArrayType = ...) -> _ArrayType: ...
    @staticmethod
    def makemat(data: ArrayLike, dtype: DTypeLike = ..., copy: bool = ...) -> _Matrix[Any, Any]: ...

    # TODO: Sort out this `__getitem__` method
    def __getitem__(self, key: Any) -> Any: ...

class RClass(AxisConcatenator):
    axis: Literal[0]
    matrix: Literal[False]
    ndmin: Literal[1]
    trans1d: Literal[-1]
    def __init__(self) -> None: ...

r_: RClass

class CClass(AxisConcatenator):
    axis: Literal[-1]
    matrix: Literal[False]
    ndmin: Literal[2]
    trans1d: Literal[0]
    def __init__(self) -> None: ...

c_: CClass

class IndexExpression(Generic[_BoolType]):
    maketuple: _BoolType
    def __init__(self, maketuple: _BoolType) -> None: ...
    @overload
    def __getitem__(self, item: _TupType) -> _TupType: ...  # type: ignore[misc]
    @overload
    def __getitem__(self: IndexExpression[Literal[True]], item: _T) -> tuple[_T]: ...
    @overload
    def __getitem__(self: IndexExpression[Literal[False]], item: _T) -> _T: ...

index_exp: IndexExpression[Literal[True]]
s_: IndexExpression[Literal[False]]

def fill_diagonal(a: NDArray[Any], val: Any, wrap: bool = ...) -> None: ...
def diag_indices(n: int, ndim: int = ...) -> tuple[NDArray[int_], ...]: ...
def diag_indices_from(arr: ArrayLike) -> tuple[NDArray[int_], ...]: ...

# NOTE: see `numpy/__init__.pyi` for `ndenumerate` and `ndindex`
