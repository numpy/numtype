import sys
from collections.abc import Callable, Collection, Sequence
from typing import Any, Protocol, TypeAlias, runtime_checkable
from typing_extensions import TypeVar

import numpy as np
from numpy.dtypes import StringDType

from ._nbit_base import _64Bit
from ._nested_sequence import _NestedSequence
from ._shape import _Shape

if sys.version_info >= (3, 12):
    from collections.abc import Buffer as _Buffer
else:
    class _Buffer(Protocol):
        def __buffer__(self, flags: int, /) -> memoryview: ...

_T = TypeVar("_T")
_ScalarType = TypeVar("_ScalarType", bound=np.generic)
_ScalarType_co = TypeVar("_ScalarType_co", bound=np.generic, covariant=True)
_DType = TypeVar("_DType", bound=np.dtype[Any])
_DType_co = TypeVar("_DType_co", covariant=True, bound=np.dtype[Any])

NDArray: TypeAlias = np.ndarray[_Shape, np.dtype[_ScalarType_co]]

# The `_SupportsArray` protocol only cares about the default dtype
# (i.e. `dtype=None` or no `dtype` parameter at all) of the to-be returned
# array.
# Concrete implementations of the protocol are responsible for adding
# any and all remaining overloads
@runtime_checkable
class _SupportsArray(Protocol[_DType_co]):
    def __array__(self, /) -> np.ndarray[Any, _DType_co]: ...

@runtime_checkable
class _SupportsArrayFunc(Protocol):
    def __array_function__(
        self,
        func: Callable[..., Any],
        types: Collection[type[Any]],
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> object: ...

_FiniteNestedSequence: TypeAlias = (
    _T | Sequence[_T] | Sequence[Sequence[_T]] | Sequence[Sequence[Sequence[_T]]] | Sequence[Sequence[Sequence[Sequence[_T]]]]
)

# A subset of `npt.ArrayLike` that can be parametrized w.r.t. `np.generic`
_ArrayLike: TypeAlias = _SupportsArray[np.dtype[_ScalarType]] | _NestedSequence[_SupportsArray[np.dtype[_ScalarType]]]

# A union representing array-like objects; consists of two typevars:
# One representing types that can be parametrized w.r.t. `np.dtype`
# and another one for the rest
_DualArrayLike: TypeAlias = _SupportsArray[_DType] | _T | _NestedSequence[_T] | _NestedSequence[_SupportsArray[_DType]]

ArrayLike: TypeAlias = _Buffer | _DualArrayLike[np.dtype[Any], complex | str | bytes]

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

__Float64_co: TypeAlias = np.floating[_64Bit] | np.float32 | np.float16 | np.integer | np.bool
__Complex128_co: TypeAlias = np.complexfloating[_64Bit] | np.complex64 | __Float64_co
_ArrayLikeFloat64_co: TypeAlias = _DualArrayLike[np.dtype[__Float64_co], float]
_ArrayLikeComplex128_co: TypeAlias = _DualArrayLike[np.dtype[__Complex128_co], complex]

# NOTE: This includes `builtins.bool`, but not `numpy.bool`.
_ArrayLikeInt: TypeAlias = _DualArrayLike[np.dtype[np.integer], int]
