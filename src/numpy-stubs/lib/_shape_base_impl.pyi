from collections.abc import Callable, Sequence
from typing import Any, Concatenate, Protocol, SupportsIndex, overload, type_check_only
from typing_extensions import ParamSpec, TypeVar, deprecated

import numpy as np
from _numtype import (
    CoComplex_nd,
    CoFloating_nd,
    CoInt64_nd,
    CoUInt64_nd,
    ToBool_nd,
    ToComplex_nd,
    ToFloating_nd,
    ToObject_nd,
    ToSInteger_nd,
    ToUInteger_nd,
)
from numpy import _CastingKind  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, NDArray, _ArrayLike, _ShapeLike

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

# Signature of `__array_wrap__`
@type_check_only
class _DoesArrayWrap(Protocol):
    def __call__(
        self,
        array: NDArray[Any],
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
def take_along_axis(arr: _ScalarT | NDArray[_ScalarT], indices: NDArray[np.integer], axis: int | None) -> NDArray[_ScalarT]: ...

#
def put_along_axis(arr: NDArray[_ScalarT], indices: NDArray[np.integer], values: ArrayLike, axis: int | None) -> None: ...

#
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[NDArray[Any], _Tss], _ArrayLike[_ScalarT]],
    axis: SupportsIndex,
    arr: ArrayLike,
    *args: _Tss.args,
    **kwargs: _Tss.kwargs,
) -> NDArray[_ScalarT]: ...
@overload
def apply_along_axis(
    func1d: Callable[Concatenate[NDArray[Any], _Tss], Any],
    axis: SupportsIndex,
    arr: ArrayLike,
    *args: _Tss.args,
    **kwargs: _Tss.kwargs,
) -> NDArray[Any]: ...

#
def apply_over_axes(
    func: Callable[[NDArray[Any], int], NDArray[_ScalarT]],
    a: ArrayLike,
    axes: int | Sequence[int],
) -> NDArray[_ScalarT]: ...

#
@overload
def expand_dims(a: _ArrayLike[_ScalarT], axis: _ShapeLike) -> NDArray[_ScalarT]: ...
@overload
def expand_dims(a: ArrayLike, axis: _ShapeLike) -> NDArray[Any]: ...

# Deprecated in NumPy 2.0, 2023-08-1
@deprecated("`row_stack` alias is deprecated. Use `np.vstack` directly.")
def row_stack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike | None = None,
    casting: _CastingKind = "same_kind",
) -> NDArray[Any]: ...

#
@overload
def column_stack(tup: Sequence[_ArrayLike[_ScalarT]]) -> NDArray[_ScalarT]: ...
@overload
def column_stack(tup: Sequence[ArrayLike]) -> NDArray[Any]: ...

#
@overload
def dstack(tup: Sequence[_ArrayLike[_ScalarT]]) -> NDArray[_ScalarT]: ...
@overload
def dstack(tup: Sequence[ArrayLike]) -> NDArray[Any]: ...

#
@overload
def array_split(
    ary: _ArrayLike[_ScalarT],
    indices_or_sections: _ShapeLike,
    axis: SupportsIndex = 0,
) -> list[NDArray[_ScalarT]]: ...
@overload
def array_split(ary: ArrayLike, indices_or_sections: _ShapeLike, axis: SupportsIndex = 0) -> list[NDArray[Any]]: ...

#
@overload
def split(ary: _ArrayLike[_ScalarT], indices_or_sections: _ShapeLike, axis: SupportsIndex = 0) -> list[NDArray[_ScalarT]]: ...
@overload
def split(ary: ArrayLike, indices_or_sections: _ShapeLike, axis: SupportsIndex = 0) -> list[NDArray[Any]]: ...

#
@overload
def hsplit(ary: _ArrayLike[_ScalarT], indices_or_sections: _ShapeLike) -> list[NDArray[_ScalarT]]: ...
@overload
def hsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...

#
@overload
def vsplit(ary: _ArrayLike[_ScalarT], indices_or_sections: _ShapeLike) -> list[NDArray[_ScalarT]]: ...
@overload
def vsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...

#
@overload
def dsplit(ary: _ArrayLike[_ScalarT], indices_or_sections: _ShapeLike) -> list[NDArray[_ScalarT]]: ...
@overload
def dsplit(ary: ArrayLike, indices_or_sections: _ShapeLike) -> list[NDArray[Any]]: ...

#
@overload
def get_array_wrap(*args: _CanArrayWrap) -> _DoesArrayWrap: ...
@overload
def get_array_wrap(*args: object) -> _DoesArrayWrap | None: ...

#
@overload
def kron(a: ToBool_nd, b: ToBool_nd) -> NDArray[np.bool]: ...
@overload
def kron(a: ToUInteger_nd, b: CoUInt64_nd) -> NDArray[np.unsignedinteger]: ...
@overload
def kron(a: CoUInt64_nd, b: ToUInteger_nd) -> NDArray[np.unsignedinteger]: ...
@overload
def kron(a: ToSInteger_nd, b: CoInt64_nd) -> NDArray[np.signedinteger]: ...
@overload
def kron(a: CoInt64_nd, b: ToSInteger_nd) -> NDArray[np.signedinteger]: ...
@overload
def kron(a: ToFloating_nd, b: CoFloating_nd) -> NDArray[np.floating]: ...
@overload
def kron(a: CoFloating_nd, b: ToFloating_nd) -> NDArray[np.floating]: ...
@overload
def kron(a: ToComplex_nd, b: CoComplex_nd) -> NDArray[np.complexfloating]: ...
@overload
def kron(a: CoComplex_nd, b: ToComplex_nd) -> NDArray[np.complexfloating]: ...
@overload
def kron(a: ToObject_nd, b: ToObject_nd) -> NDArray[np.object_]: ...

#
@overload
def tile(A: _ArrayLike[_ScalarT], reps: int | Sequence[int]) -> NDArray[_ScalarT]: ...
@overload
def tile(A: ArrayLike, reps: int | Sequence[int]) -> NDArray[Any]: ...
