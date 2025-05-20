from collections.abc import Callable, Collection
from typing import Any, Protocol, TypeAlias, runtime_checkable
from typing_extensions import Buffer, TypeVar

import _numtype as _nt
import numpy as np
from numpy.dtypes import StringDType

from ._nested_sequence import _NestedSequence

_T = TypeVar("_T")
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, covariant=True)

NDArray: TypeAlias = np.ndarray[_nt.Shape, np.dtype[_ScalarT_co]]

# The `_SupportsArray` protocol only cares about the default dtype
# (i.e. `dtype=None` or no `dtype` parameter at all) of the to-be returned
# array.
# Concrete implementations of the protocol are responsible for adding
# any and all remaining overloads
@runtime_checkable
class _SupportsArray(Protocol[_DTypeT_co]):
    def __array__(self, /) -> np.ndarray[Any, _DTypeT_co]: ...

@runtime_checkable
class _SupportsArrayFunc(Protocol):  # noqa: PYI046
    def __array_function__(
        self,
        func: Callable[..., Any],
        types: Collection[type[Any]],
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> object: ...

# A subset of `npt.ArrayLike` that can be parametrized w.r.t. `np.generic`
_ArrayLike: TypeAlias = _SupportsArray[np.dtype[_ScalarT]] | _NestedSequence[_SupportsArray[np.dtype[_ScalarT]]]

# A union representing array-like objects; consists of two typevars:
# One representing types that can be parametrized w.r.t. `np.dtype`
# and another one for the rest
_DualArrayLike: TypeAlias = (
    _SupportsArray[_DTypeT] | _T | _NestedSequence[_T] | _NestedSequence[_SupportsArray[_DTypeT]]
)

ArrayLike: TypeAlias = _DualArrayLike[np.dtype, complex | str | bytes] | Buffer

# TODO(jorenham): get rid of this in favor of the ones in `_numtype`
# https://github.com/numpy/numtype/issues/568

# ruff: noqa: PYI047

# `ArrayLike<X>_co`: array-like objects that can be coerced into `X`
# given the casting rules `same_kind`
_ArrayLikeBool_co: TypeAlias = _DualArrayLike[np.dtype[np.bool], bool]
_ArrayLikeUInt_co: TypeAlias = _DualArrayLike[np.dtype[np.unsignedinteger | np.bool], bool]
_ArrayLikeInt_co: TypeAlias = _DualArrayLike[np.dtype[np.integer | np.bool], int]
_ArrayLikeFloat_co: TypeAlias = _DualArrayLike[np.dtype[np.floating | np.integer | np.bool], float]
_ArrayLikeComplex_co: TypeAlias = _DualArrayLike[np.dtype[np.bool | np.number], complex]
_ArrayLikeNumber_co: TypeAlias = _ArrayLikeComplex_co
_ArrayLikeTD64_co: TypeAlias = _DualArrayLike[np.dtype[np.timedelta64 | np.integer | np.bool], int]
_ArrayLikeDT64_co: TypeAlias = _ArrayLike[np.datetime64]
_ArrayLikeObject_co: TypeAlias = _ArrayLike[np.object_]
_ArrayLikeVoid_co: TypeAlias = _ArrayLike[np.void]
_ArrayLikeStr_co: TypeAlias = _DualArrayLike[np.dtype[np.str_], str]
_ArrayLikeBytes_co: TypeAlias = _DualArrayLike[np.dtype[np.bytes_], bytes]
_ArrayLikeString_co: TypeAlias = _DualArrayLike[StringDType, str]
_ArrayLikeAnyString_co: TypeAlias = _DualArrayLike[StringDType | np.dtype[np.character], bytes | str]

__Float64_co: TypeAlias = np.float64 | np.float32 | np.float16 | np.integer | np.bool
__Complex128_co: TypeAlias = np.complex128 | np.complex64 | __Float64_co
_ArrayLikeFloat64_co: TypeAlias = _DualArrayLike[np.dtype[__Float64_co], float]
_ArrayLikeComplex128_co: TypeAlias = _DualArrayLike[np.dtype[__Complex128_co], complex]

# NOTE: This includes `builtins.bool`, but not `numpy.bool`.
_ArrayLikeInt: TypeAlias = _DualArrayLike[np.dtype[np.integer], int]
