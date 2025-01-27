from collections.abc import Mapping
from typing import Any, Literal as L, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import numpy as np
from numpy._typing import ArrayLike, NDArray, _ArrayLike, _ArrayLikeInt

__all__ = ["pad"]

###

_SCT = TypeVar("_SCT", bound=np.generic)

_ModeKind: TypeAlias = L[
    "constant",
    "edge",
    "linear_ramp",
    "maximum",
    "mean",
    "median",
    "minimum",
    "reflect",
    "symmetric",
    "wrap",
    "empty",
]

@type_check_only
class _ModeFunc(Protocol):
    def __call__(self, vector: NDArray[Any], pad: tuple[int, int], iaxis: int, kwargs: Mapping[str, object], /) -> None: ...

###

# TODO: In practice each keyword argument is exclusive to one or more
# specific modes. Consider adding more overloads to express this in the future.
@overload
def pad(
    array: _ArrayLike[_SCT],
    pad_width: _ArrayLikeInt,
    mode: _ModeKind = ...,
    *,
    stat_length: _ArrayLikeInt | None = ...,
    constant_values: ArrayLike = ...,
    end_values: ArrayLike = ...,
    reflect_type: L["odd", "even"] = ...,
) -> NDArray[_SCT]: ...
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
) -> NDArray[Any]: ...
@overload
def pad(array: _ArrayLike[_SCT], pad_width: _ArrayLikeInt, mode: _ModeFunc, **kwargs: object) -> NDArray[_SCT]: ...
@overload
def pad(array: ArrayLike, pad_width: _ArrayLikeInt, mode: _ModeFunc, **kwargs: object) -> NDArray[Any]: ...
