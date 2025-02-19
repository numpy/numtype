from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Protocol, TypeAlias, TypedDict, runtime_checkable
from typing_extensions import Required, TypeVar

import numpy as np

from ._char_codes import (
    _BoolCodes,
    _BytesCodes,
    _ComplexFloatingCodes,
    _DT64Codes,
    _FloatingCodes,
    _NumberCodes,
    _ObjectCodes,
    _SignedIntegerCodes,
    _StrCodes,
    _TD64Codes,
    _UnsignedIntegerCodes,
    _VoidCodes,
)
from ._shape import _ShapeLike

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT_co = TypeVar("_DTypeT_co", covariant=True, bound=np.dtype[Any])

# TODO(jorenham): Actually annotate this
_DTypeLikeNested: TypeAlias = Incomplete

class _DTypeDict(TypedDict, total=False):
    names: Required[Sequence[str]]
    formats: Required[Sequence[_DTypeLikeNested]]
    itemsize: int
    aligned: bool
    offsets: Sequence[int]
    # Only `str` elements are usable as indexing aliases,
    # but `titles` can in principle accept any object
    titles: Sequence[str | Any]

# A protocol for anything with the dtype attribute
@runtime_checkable
class _SupportsDType(Protocol[_DTypeT_co]):
    @property
    def dtype(self) -> _DTypeT_co: ...

# A subset of `npt.DTypeLike` that can be parametrized w.r.t. `np.generic`
_DTypeLike: TypeAlias = type[_ScalarT] | np.dtype[_ScalarT] | _SupportsDType[np.dtype[_ScalarT]]

# Would create a dtype[np.void]
_VoidDTypeLike: TypeAlias = tuple[_DTypeLikeNested, int | _ShapeLike | _DTypeLikeNested] | list[Any] | _DTypeDict

# Aliases for commonly used dtype-like objects.
# Note that the precision of `np.number` subclasses is ignored herein.
_DTypeLikeBool: TypeAlias = type[bool] | _DTypeLike[np.bool] | _BoolCodes
_DTypeLikeUInt: TypeAlias = _DTypeLike[np.unsignedinteger] | _UnsignedIntegerCodes
_DTypeLikeInt: TypeAlias = type[int] | _DTypeLike[np.signedinteger] | _SignedIntegerCodes
_DTypeLikeFloat: TypeAlias = type[float] | _DTypeLike[np.floating] | _FloatingCodes
_DTypeLikeComplex: TypeAlias = type[complex] | _DTypeLike[np.complexfloating] | _ComplexFloatingCodes
_DTypeLikeDT64: TypeAlias = _DTypeLike[np.timedelta64] | _TD64Codes
_DTypeLikeTD64: TypeAlias = _DTypeLike[np.datetime64] | _DT64Codes
_DTypeLikeStr: TypeAlias = type[str] | _DTypeLike[np.str_] | _StrCodes
_DTypeLikeBytes: TypeAlias = type[bytes] | _DTypeLike[np.bytes_] | _BytesCodes
_DTypeLikeVoid: TypeAlias = _DTypeLike[np.void] | _VoidCodes | _VoidDTypeLike
_DTypeLikeObject: TypeAlias = type | _DTypeLike[np.object_] | _ObjectCodes

_DTypeLikeComplex_co: TypeAlias = type[complex] | _DTypeLike[np.number] | _NumberCodes | _BoolCodes

# NOTE: while it is possible to provide the dtype as a dict of
# dtype-like objects (e.g. `{'field1': ..., 'field2': ..., ...}`),
# this syntax is officially discouraged and
# therefore not included in the type-union defining `DTypeLike`.
#
# See https://github.com/numpy/numpy/issues/16891 for more details.

# Anything that can be coerced into numpy.dtype.
# Reference: https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html
DTypeLike: TypeAlias = str | _DTypeLike[Any] | _VoidDTypeLike | None
