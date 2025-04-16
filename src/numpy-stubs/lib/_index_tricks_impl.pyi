from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, ClassVar, Final, Generic, Literal as L, SupportsIndex as CanIndex, TypeAlias, final, overload
from typing_extensions import Self, TypeVar, deprecated

import _numtype as _nt
import numpy as np
from numpy._core.multiarray import ravel_multi_index, unravel_index
from numpy._typing import ArrayLike, _SupportsDType as _HasDType

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
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, default=Any, covariant=True)
_TupleT = TypeVar("_TupleT", bound=tuple[object, ...])
_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)

_BoolT_co = TypeVar("_BoolT_co", bound=bool, default=bool, covariant=True)

_AxisT_co = TypeVar("_AxisT_co", bound=int, default=L[0], covariant=True)
_MatrixT_co = TypeVar("_MatrixT_co", bound=bool, default=L[False], covariant=True)
_NDMinT_co = TypeVar("_NDMinT_co", bound=int, default=L[1], covariant=True)
_Trans1DT_co = TypeVar("_Trans1DT_co", bound=int, default=L[-1], covariant=True)

_Arrays: TypeAlias = tuple[_nt.Array[_ScalarT], ...]

###

class ndenumerate(Generic[_ScalarT_co]):
    @overload
    def __init__(self: ndenumerate[_ScalarT], /, arr: _nt._ToArray_nd[_ScalarT]) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.bytes_], /, arr: _nt.ToBytes_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.str_], /, arr: _nt.ToStr_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.bool], /, arr: _nt.ToBool_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.intp], /, arr: _nt.ToInt_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.float64], /, arr: _nt.ToFloat64_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.complex128], /, arr: _nt.ToComplex128_nd) -> None: ...
    @overload
    def __init__(self: ndenumerate[np.object_], /, arr: _nt.ToObject_nd) -> None: ...

    # The first overload is a (semi-)workaround for a mypy bug (tested with v1.10 and v1.11)
    @overload
    def __next__(
        self: ndenumerate[_nt.co_number | np.flexible | np.datetime64 | np.timedelta64],
        /,
    ) -> tuple[tuple[int, ...], _ScalarT_co]: ...
    @overload
    def __next__(self: ndenumerate[np.object_], /) -> tuple[tuple[int, ...], Any]: ...
    @overload
    def __next__(self, /) -> tuple[tuple[int, ...], _ScalarT_co]: ...

    #
    def __iter__(self) -> Self: ...

class ndindex:
    @overload
    def __init__(self, shape: tuple[CanIndex, ...], /) -> None: ...
    @overload
    def __init__(self, /, *shape: CanIndex) -> None: ...

    #
    def __iter__(self) -> Self: ...
    def __next__(self) -> tuple[int, ...]: ...
    @deprecated("Deprecated since 1.20.0.")
    def ndincr(self, /) -> None: ...

class nd_grid(Generic[_BoolT_co]):
    sparse: _BoolT_co
    def __init__(self, sparse: _BoolT_co = ...) -> None: ...
    @overload
    def __getitem__(self: nd_grid[L[False]], key: slice | Sequence[slice]) -> _nt.Array: ...
    @overload
    def __getitem__(self: nd_grid[L[True]], key: slice | Sequence[slice]) -> tuple[_nt.Array, ...]: ...

@final
class MGridClass(nd_grid[L[False]]):
    def __init__(self) -> None: ...

@final
class OGridClass(nd_grid[L[True]]):
    def __init__(self) -> None: ...

class AxisConcatenator(Generic[_AxisT_co, _MatrixT_co, _NDMinT_co, _Trans1DT_co]):
    __slots__ = "axis", "matrix", "ndmin", "trans1d"

    makemat: ClassVar[type[np.matrix[tuple[int, int], np.dtype]]]

    axis: _AxisT_co
    matrix: _MatrixT_co
    trans1d: _Trans1DT_co
    ndmin: _NDMinT_co

    #
    def __init__(
        self,
        /,
        axis: _AxisT_co = ...,
        matrix: _MatrixT_co = ...,
        ndmin: _NDMinT_co = ...,
        trans1d: _Trans1DT_co = ...,
    ) -> None: ...

    # TODO(jorenham): annotate this
    def __getitem__(self, key: Incomplete, /) -> Incomplete: ...
    def __len__(self, /) -> L[0]: ...

    #
    @staticmethod
    @overload
    def concatenate(
        *a: _nt._ToArray_nd[_ScalarT],
        axis: CanIndex | None = 0,
        out: None = None,
    ) -> _nt.Array[_ScalarT]: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: CanIndex | None = 0, out: _ArrayT) -> _ArrayT: ...
    @staticmethod
    @overload
    def concatenate(*a: ArrayLike, axis: CanIndex | None = 0, out: None = None) -> _nt.Array: ...

@final
class RClass(AxisConcatenator[L[0], L[False], L[1], L[-1]]):
    def __init__(self, /) -> None: ...

@final
class CClass(AxisConcatenator[L[-1], L[False], L[2], L[0]]):
    def __init__(self, /) -> None: ...

class IndexExpression(Generic[_BoolT_co]):
    maketuple: _BoolT_co
    def __init__(self, /, maketuple: _BoolT_co) -> None: ...
    #
    @overload
    def __getitem__(self, item: _TupleT, /) -> _TupleT: ...  # type: ignore[overload-overlap]
    @overload
    def __getitem__(self: IndexExpression[L[False]], item: _T, /) -> _T: ...
    @overload
    def __getitem__(self: IndexExpression[L[True]], item: _T, /) -> tuple[_T]: ...
    @overload
    def __getitem__(self, item: _T, /) -> _T | tuple[_T]: ...

@overload
def ix_(*args: _nt.SequenceND[_HasDType[_DTypeT]]) -> tuple[np.ndarray[tuple[int, ...], _DTypeT], ...]: ...
@overload
def ix_(*args: _nt.SequenceND[bool]) -> _Arrays[np.bool]: ...
@overload
def ix_(*args: _nt.SequenceND[_nt.JustInt]) -> _Arrays[np.intp]: ...
@overload
def ix_(*args: _nt.SequenceND[_nt.JustFloat]) -> _Arrays[np.float64]: ...
@overload
def ix_(*args: _nt.SequenceND[_nt.JustComplex]) -> _Arrays[np.complex128]: ...
@overload
def ix_(*args: _nt.SequenceND[_nt.JustBytes]) -> _Arrays[np.bytes_]: ...
@overload
def ix_(*args: _nt.SequenceND[_nt.JustStr]) -> _Arrays[np.str_]: ...
@overload  # the redundant overloads below are a workaround for a mypy bug
def ix_(*args: _nt.SequenceND[int]) -> _Arrays[np.intp | np.bool]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload
def ix_(*args: _nt.SequenceND[float]) -> _Arrays[np.float64 | np.intp | np.bool]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
@overload
def ix_(*args: _nt.SequenceND[complex]) -> _Arrays[np.complex128 | np.float64 | np.intp | np.bool]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]

#
def fill_diagonal(a: _nt.Array, val: Any, wrap: bool = False) -> None: ...
def diag_indices(n: int, ndim: int = 2) -> _Arrays[np.intp]: ...
def diag_indices_from(arr: ArrayLike) -> _Arrays[np.intp]: ...

###

mgrid: Final[MGridClass] = ...
ogrid: Final[OGridClass] = ...

r_: Final[RClass] = ...
c_: Final[CClass] = ...

index_exp: Final[IndexExpression[L[True]]] = ...
s_: Final[IndexExpression[L[False]]] = ...
