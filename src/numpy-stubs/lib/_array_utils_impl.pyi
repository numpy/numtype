from collections.abc import Iterable, Mapping
from typing import Any, Protocol, type_check_only

__all__ = ["byte_bounds", "normalize_axis_index", "normalize_axis_tuple"]

###

@type_check_only
class _HasSizeAndArrayInterface(Protocol):
    @property
    def size(self, /) -> int: ...
    @property  # `TypedDict` cannot be used because it rejects `dict[str, Any]`
    def __array_interface__(self, /) -> Mapping[str, Any]: ...

###

# NOTE: In practice `byte_bounds` can (potentially) take any object
# implementing the `__array_interface__` protocol. The caveat is
# that certain keys, marked as optional in the spec, must be present for
#  `byte_bounds`. This concerns `"strides"` and `"data"`.
def byte_bounds(a: _HasSizeAndArrayInterface) -> tuple[int, int]: ...

###
def normalize_axis_index(axis: int, ndim: int, msg_prefix: str | None = None) -> int: ...
def normalize_axis_tuple(
    axis: int | Iterable[int],
    ndim: int,
    argname: str | None = None,
    allow_duplicate: bool = False,
) -> tuple[int, ...]: ...
