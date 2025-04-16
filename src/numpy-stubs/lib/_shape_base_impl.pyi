from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from typing import Any, Concatenate, Protocol, SupportsIndex as CanIndex, TypeAlias, overload, type_check_only
from typing_extensions import ParamSpec, TypeVar, deprecated

import _numtype as _nt
import numpy as np
from numpy import _CastingKind  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike as _ToArray, _ShapeLike as _ToShape

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

_Tss = ParamSpec("_Tss")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_ArrayList: TypeAlias = list[_nt.Array[_ScalarT]]

# Signature of `__array_wrap__`
@type_check_only
class _DoesArrayWrap(Protocol):
    def __call__(
        self,
        array: _nt.Array,
        context: tuple[np.ufunc, tuple[Any, ...], int] | None = ...,
        return_scalar: bool = ...,
        /,
    ) -> Any: ...

@type_check_only
class _CanArrayWrap(Protocol):
    @property
    def __array_wrap__(self) -> _DoesArrayWrap: ...

###

#
def take_along_axis(
    arr: _ScalarT | _nt.Array[_ScalarT],
    indices: _nt.Array[np.integer],
    axis: int | None,
) -> _nt.Array[_ScalarT]: ...

#
def put_along_axis(
    arr: _nt.Array[_ScalarT],
    indices: _nt.Array[np.integer],
    values: ArrayLike,
    axis: int | None,
) -> None: ...

#
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[_nt.Array, _Tss], _ToArray[_ScalarT]],
    axis: CanIndex,
    arr: ArrayLike,
    *args: _Tss.args,
    **kwargs: _Tss.kwargs,
) -> _nt.Array[_ScalarT]: ...
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[_nt.Array, _Tss], Any],
    axis: CanIndex,
    arr: ArrayLike,
    *args: _Tss.args,
    **kwargs: _Tss.kwargs,
) -> _nt.Array[Incomplete]: ...

#
def apply_over_axes(
    func: Callable[[_nt.Array, int], _nt.Array[_ScalarT]],
    a: ArrayLike,
    axes: int | Sequence[int],
) -> _nt.Array[_ScalarT]: ...

#
@overload
def expand_dims(a: _ToArray[_ScalarT], axis: _ToShape) -> _nt.Array[_ScalarT]: ...
@overload
def expand_dims(a: ArrayLike, axis: _ToShape) -> _nt.Array[Incomplete]: ...

# Deprecated in NumPy 2.0, 2023-08-1
@deprecated("`row_stack` alias is deprecated. Use `np.vstack` directly.")
def row_stack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike | None = None,
    casting: _CastingKind = "same_kind",
) -> _nt.Array[Incomplete]: ...

#
@overload
def column_stack(tup: Sequence[_ToArray[_ScalarT]]) -> _nt.Array[_ScalarT]: ...
@overload
def column_stack(tup: Sequence[ArrayLike]) -> _nt.Array[Incomplete]: ...

#
@overload
def dstack(tup: Sequence[_ToArray[_ScalarT]]) -> _nt.Array[_ScalarT]: ...
@overload
def dstack(tup: Sequence[ArrayLike]) -> _nt.Array[Incomplete]: ...

#
@overload
def array_split(ary: _ToArray[_ScalarT], indices_or_sections: _ToShape, axis: CanIndex = 0) -> _ArrayList[_ScalarT]: ...
@overload
def array_split(ary: ArrayLike, indices_or_sections: _ToShape, axis: CanIndex = 0) -> list[_nt.Array[Incomplete]]: ...

#
@overload
def split(ary: _ToArray[_ScalarT], indices_or_sections: _ToShape, axis: CanIndex = 0) -> _ArrayList[_ScalarT]: ...
@overload
def split(ary: ArrayLike, indices_or_sections: _ToShape, axis: CanIndex = 0) -> list[_nt.Array[Incomplete]]: ...

#
@overload
def hsplit(ary: _ToArray[_ScalarT], indices_or_sections: _ToShape) -> _ArrayList[_ScalarT]: ...
@overload
def hsplit(ary: ArrayLike, indices_or_sections: _ToShape) -> list[_nt.Array[Incomplete]]: ...

#
@overload
def vsplit(ary: _ToArray[_ScalarT], indices_or_sections: _ToShape) -> _ArrayList[_ScalarT]: ...
@overload
def vsplit(ary: ArrayLike, indices_or_sections: _ToShape) -> list[_nt.Array[Incomplete]]: ...

#
@overload
def dsplit(ary: _ToArray[_ScalarT], indices_or_sections: _ToShape) -> _ArrayList[_ScalarT]: ...
@overload
def dsplit(ary: ArrayLike, indices_or_sections: _ToShape) -> list[_nt.Array[Incomplete]]: ...

#
@overload
def get_array_wrap(*args: _CanArrayWrap) -> _DoesArrayWrap: ...
@overload
def get_array_wrap(*args: object) -> _DoesArrayWrap | None: ...

#
@overload
def kron(a: _nt.ToBool_nd, b: _nt.ToBool_nd) -> _nt.Array[np.bool]: ...
@overload
def kron(a: _nt.ToUInteger_nd, b: _nt.CoUInt64_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def kron(a: _nt.CoUInt64_nd, b: _nt.ToUInteger_nd) -> _nt.Array[np.unsignedinteger]: ...
@overload
def kron(a: _nt.ToSInteger_nd, b: _nt.CoInt64_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def kron(a: _nt.CoInt64_nd, b: _nt.ToSInteger_nd) -> _nt.Array[np.signedinteger]: ...
@overload
def kron(a: _nt.ToFloating_nd, b: _nt.CoFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def kron(a: _nt.CoFloating_nd, b: _nt.ToFloating_nd) -> _nt.Array[np.floating]: ...
@overload
def kron(a: _nt.ToComplex_nd, b: _nt.CoComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def kron(a: _nt.CoComplex_nd, b: _nt.ToComplex_nd) -> _nt.Array[np.complexfloating]: ...
@overload
def kron(a: _nt.ToObject_nd, b: _nt.ToObject_nd) -> _nt.Array[np.object_]: ...

#
@overload
def tile(A: _ToArray[_ScalarT], reps: int | Sequence[int]) -> _nt.Array[_ScalarT]: ...
@overload
def tile(A: ArrayLike, reps: int | Sequence[int]) -> _nt.Array[Incomplete]: ...
