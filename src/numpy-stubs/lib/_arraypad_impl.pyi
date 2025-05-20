from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Literal as L, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._typing import ArrayLike, _ArrayLike, _ArrayLikeInt

__all__ = ["pad"]

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_ModeKind: TypeAlias = L[
    "constant", "edge", "linear_ramp", "maximum", "mean", "median", "minimum", "reflect", "symmetric", "wrap", "empty"
]

@type_check_only
class _ModeFunc(Protocol):
    def __call__(
        self, vector: _nt.Array[Incomplete], pad: tuple[int, int], iaxis: int, kwargs: Mapping[str, object], /
    ) -> None: ...

###

# TODO: In practice each keyword argument is exclusive to one or more
# specific modes. Consider adding more overloads to express this in the future.
@overload
def pad(
    array: _ArrayLike[_ScalarT],
    pad_width: _ArrayLikeInt,
    mode: _ModeKind = ...,
    *,
    stat_length: _ArrayLikeInt | None = ...,
    constant_values: ArrayLike = ...,
    end_values: ArrayLike = ...,
    reflect_type: L["odd", "even"] = ...,
) -> _nt.Array[_ScalarT]: ...
@overload
def pad(
    array: ArrayLike,
    pad_width: _ArrayLikeInt,
    mode: _ModeKind = ...,
    *,
    stat_length: _ArrayLikeInt | None = ...,
    constant_values: ArrayLike = ...,
    end_values: ArrayLike = ...,
    reflect_type: L["odd", "even"] = ...,
) -> _nt.Array[Incomplete]: ...
@overload
def pad(
    array: _ArrayLike[_ScalarT], pad_width: _ArrayLikeInt, mode: _ModeFunc, **kwargs: object
) -> _nt.Array[_ScalarT]: ...
@overload
def pad(array: ArrayLike, pad_width: _ArrayLikeInt, mode: _ModeFunc, **kwargs: object) -> _nt.Array[Incomplete]: ...
