from collections.abc import Sequence
from typing import Any, SupportsIndex, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._typing import ArrayLike, DTypeLike, NDArray, _ArrayLike, _DTypeLike

__all__ = ["atleast_1d", "atleast_2d", "atleast_3d", "block", "hstack", "stack", "unstack", "vstack"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_SCT0 = TypeVar("_SCT0", bound=np.generic)
_SCT1 = TypeVar("_SCT1", bound=np.generic)

_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])

_Array1T = TypeVar("_Array1T", bound=np.ndarray[_nt.Shape1_, np.dtype])
_Array1T0 = TypeVar("_Array1T0", bound=np.ndarray[_nt.Shape1_, np.dtype])
_Array1T1 = TypeVar("_Array1T1", bound=np.ndarray[_nt.Shape1_, np.dtype])

_Array2T = TypeVar("_Array2T", bound=np.ndarray[_nt.Shape2_, np.dtype])
_Array2T0 = TypeVar("_Array2T0", bound=np.ndarray[_nt.Shape2_, np.dtype])
_Array2T1 = TypeVar("_Array2T1", bound=np.ndarray[_nt.Shape2_, np.dtype])

_Array3T = TypeVar("_Array3T", bound=np.ndarray[_nt.Shape3_, np.dtype])
_Array3T0 = TypeVar("_Array3T0", bound=np.ndarray[_nt.Shape3_, np.dtype])
_Array3T1 = TypeVar("_Array3T1", bound=np.ndarray[_nt.Shape3_, np.dtype])

###

#
@overload
def atleast_1d(a0: _Array1T, /) -> _Array1T: ...
@overload
def atleast_1d(a0: _Array1T0, a1: _Array1T1, /) -> tuple[_Array1T0, _Array1T1]: ...
@overload
def atleast_1d(a0: _Array1T, a1: _Array1T, /, *arys: _Array1T) -> tuple[_Array1T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_1d(a0: _ArrayLike[_ScalarT], /) -> NDArray[_ScalarT]: ...
@overload
def atleast_1d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[NDArray[_SCT0], NDArray[_SCT1]]: ...
@overload
def atleast_1d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[NDArray[_ScalarT], ...]: ...
@overload
def atleast_1d(a0: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_1d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[NDArray[Any], NDArray[Any]]: ...
@overload
def atleast_1d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def atleast_2d(a0: _Array2T, /) -> _Array2T: ...
@overload
def atleast_2d(a0: _Array2T0, a1: _Array2T1, /) -> tuple[_Array2T0, _Array2T1]: ...
@overload
def atleast_2d(a0: _Array2T, a1: _Array2T, /, *arys: _Array2T) -> tuple[_Array2T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_2d(a0: _ArrayLike[_ScalarT], /) -> NDArray[_ScalarT]: ...
@overload
def atleast_2d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[NDArray[_SCT0], NDArray[_SCT1]]: ...
@overload
def atleast_2d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[NDArray[_ScalarT], ...]: ...
@overload
def atleast_2d(a0: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_2d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[NDArray[Any], NDArray[Any]]: ...
@overload
def atleast_2d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def atleast_3d(a0: _Array3T, /) -> _Array3T: ...
@overload
def atleast_3d(a0: _Array3T0, a1: _Array3T1, /) -> tuple[_Array3T0, _Array3T1]: ...
@overload
def atleast_3d(a0: _Array3T, a1: _Array3T, /, *arys: _Array3T) -> tuple[_Array3T, ...]: ...  # type: ignore[overload-overlap]
@overload
def atleast_3d(a0: _ArrayLike[_ScalarT], /) -> NDArray[_ScalarT]: ...
@overload
def atleast_3d(a0: _ArrayLike[_SCT0], a2: _ArrayLike[_SCT1], /) -> tuple[NDArray[_SCT0], NDArray[_SCT1]]: ...
@overload
def atleast_3d(
    a0: _ArrayLike[_ScalarT], a2: _ArrayLike[_ScalarT], /, *arys: _ArrayLike[_ScalarT]
) -> tuple[NDArray[_ScalarT], ...]: ...
@overload
def atleast_3d(a0: ArrayLike, /) -> NDArray[Any]: ...
@overload
def atleast_3d(a0: ArrayLike, a2: ArrayLike, /) -> tuple[NDArray[Any], NDArray[Any]]: ...
@overload
def atleast_3d(a0: ArrayLike, a2: ArrayLike, /, *arys: ArrayLike) -> tuple[NDArray[Any], ...]: ...

#
@overload
def vstack(
    tup: Sequence[_ArrayLike[_ScalarT]],
    *,
    dtype: None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def vstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[Any]: ...

#
@overload
def hstack(
    tup: Sequence[_ArrayLike[_ScalarT]],
    *,
    dtype: None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def hstack(
    tup: Sequence[ArrayLike],
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[Any]: ...

#
@overload
def stack(
    arrays: Sequence[_ArrayLike[_ScalarT]],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: np._CastingKind = "same_kind",
) -> NDArray[_ScalarT]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    out: None = None,
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> NDArray[Any]: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex,
    out: _ArrayT,
    *,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def stack(
    arrays: Sequence[ArrayLike],
    axis: SupportsIndex = 0,
    *,
    out: _ArrayT,
    dtype: DTypeLike | None = None,
    casting: np._CastingKind = "same_kind",
) -> _ArrayT: ...

#
@overload
def unstack(array: _ArrayLike[_ScalarT], /, *, axis: SupportsIndex = 0) -> tuple[NDArray[_ScalarT], ...]: ...
@overload
def unstack(array: ArrayLike, /, *, axis: SupportsIndex = 0) -> tuple[NDArray[Any], ...]: ...

#
@overload
def block(arrays: _ArrayLike[_ScalarT]) -> NDArray[_ScalarT]: ...
@overload
def block(arrays: ArrayLike) -> NDArray[Any]: ...
