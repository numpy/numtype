from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Final, Generic, Literal, SupportsIndex, overload
from typing_extensions import TypeVar

import numpy as np
from numpy import ndenumerate, ndindex  # noqa: ICN003
from numpy._core.multiarray import ravel_multi_index, unravel_index
from numpy._typing import ArrayLike, DTypeLike, NDArray, _FiniteNestedSequence, _NestedSequence, _Shape, _SupportsDType

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
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_BoolT_co = TypeVar("_BoolT_co", bound=bool, default=bool, covariant=True)
_TupleT = TypeVar("_TupleT", bound=tuple[object, ...])
_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])

@overload
def ix_(*args: _FiniteNestedSequence[_SupportsDType[_DTypeT]]) -> tuple[np.ndarray[_Shape, _DTypeT], ...]: ...
@overload
def ix_(*args: str | _NestedSequence[str]) -> tuple[NDArray[np.str_], ...]: ...
@overload
def ix_(*args: bytes | _NestedSequence[bytes]) -> tuple[NDArray[np.bytes_], ...]: ...
@overload
def ix_(*args: bool | _NestedSequence[bool]) -> tuple[NDArray[np.bool], ...]: ...
@overload
def ix_(*args: int | _NestedSequence[int]) -> tuple[NDArray[np.int_], ...]: ...
@overload
def ix_(*args: float | _NestedSequence[float]) -> tuple[NDArray[np.float64], ...]: ...
@overload
def ix_(*args: complex | _NestedSequence[complex]) -> tuple[NDArray[np.complex128], ...]: ...

class nd_grid(Generic[_BoolT_co]):
    sparse: _BoolT_co
    def __init__(self, sparse: _BoolT_co = ...) -> None: ...
    @overload
    def __getitem__(self: nd_grid[Literal[False]], key: slice | Sequence[slice]) -> NDArray[Any]: ...
    @overload
    def __getitem__(self: nd_grid[Literal[True]], key: slice | Sequence[slice]) -> tuple[NDArray[Any], ...]: ...

class MGridClass(nd_grid[Literal[False]]):
    def __init__(self) -> None: ...

mgrid: Final[MGridClass] = ...

class OGridClass(nd_grid[Literal[True]]):
    def __init__(self) -> None: ...

ogrid: Final[OGridClass] = ...

class AxisConcatenator:
    axis: int
    matrix: bool
    ndmin: int
    trans1d: int
    def __init__(self, axis: int = ..., matrix: bool = ..., ndmin: int = ..., trans1d: int = ...) -> None: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: SupportsIndex = ..., out: None = ...) -> NDArray[Any]: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: SupportsIndex = ..., out: _ArrayT) -> _ArrayT: ...
    @staticmethod
    def makemat(data: ArrayLike, dtype: DTypeLike = ..., copy: bool = ...) -> np.matrix[Any, Any]: ...
    def __getitem__(self, key: Incomplete, /) -> Incomplete: ...

class RClass(AxisConcatenator):
    axis: Literal[0]
    matrix: Literal[False]
    ndmin: Literal[1]
    trans1d: Literal[-1]
    def __init__(self) -> None: ...

r_: Final[RClass] = ...

class CClass(AxisConcatenator):
    axis: Literal[-1]
    matrix: Literal[False]
    ndmin: Literal[2]
    trans1d: Literal[0]
    def __init__(self) -> None: ...

c_: Final[CClass] = ...

class IndexExpression(Generic[_BoolT_co]):
    maketuple: _BoolT_co
    def __init__(self, maketuple: _BoolT_co) -> None: ...
    @overload
    def __getitem__(self, item: _TupleT) -> _TupleT: ...  # type: ignore[misc]
    @overload
    def __getitem__(self: IndexExpression[Literal[True]], item: _T) -> tuple[_T]: ...
    @overload
    def __getitem__(self: IndexExpression[Literal[False]], item: _T) -> _T: ...

index_exp: Final[IndexExpression[Literal[True]]] = ...
s_: Final[IndexExpression[Literal[False]]] = ...

def fill_diagonal(a: NDArray[Any], val: Any, wrap: bool = ...) -> None: ...
def diag_indices(n: int, ndim: int = ...) -> tuple[NDArray[np.int_], ...]: ...
def diag_indices_from(arr: ArrayLike) -> tuple[NDArray[np.int_], ...]: ...
