from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Protocol, Required, TypeAlias, TypedDict, type_check_only
from typing_extensions import TypeVar

import numpy as np

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_DTypeT_co = TypeVar("_DTypeT_co", covariant=True, bound=np.dtype)

# TODO(jorenham): Actually annotate this
_DTypeLikeNested: TypeAlias = Incomplete

@type_check_only
class _DTypeDict(TypedDict, total=False):
    names: Required[Sequence[str]]
    formats: Required[Sequence[_DTypeLikeNested]]
    itemsize: int
    aligned: bool
    offsets: Sequence[int]
    # Only `str` elements are usable as indexing aliases,
    # but `titles` can in principle accept any object
    titles: Sequence[Any]

@type_check_only
class _HasDTypeLegacy(Protocol[_DTypeT_co]):
    @property
    def dtype(self, /) -> _DTypeT_co: ...

@type_check_only
class _HasDType(Protocol[_DTypeT_co]):
    @property
    def __numpy_dtype__(self, /) -> _DTypeT_co: ...

_SupportsDType: TypeAlias = _HasDType[_DTypeT] | _HasDTypeLegacy[_DTypeT]

# A subset of `npt.DTypeLike` that can be parametrized w.r.t. `np.generic`
_DTypeLike: TypeAlias = type[_ScalarT] | np.dtype[_ScalarT] | _SupportsDType[np.dtype[_ScalarT]]

# Would create a dtype[np.void]
_VoidDTypeLike: TypeAlias = tuple[Any, Any] | list[Any] | _DTypeDict

# NOTE: while it is possible to provide the dtype as a dict of
# dtype-like objects (e.g. `{'field1': ..., 'field2': ..., ...}`),
# this syntax is officially discouraged and
# therefore not included in the type-union defining `DTypeLike`.
#
# See https://github.com/numpy/numpy/issues/16891 for more details.

# Anything that can be coerced into numpy.dtype.
# Reference: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
DTypeLike: TypeAlias = str | bytes | _DTypeLike[Any] | _VoidDTypeLike
