import sys
from collections.abc import Callable, Collection, Sequence
from typing import Any, Never as _UnknownType, Protocol, TypeAlias, TypeVar, runtime_checkable

import numpy as np
from numpy.dtypes import StringDType

from ._nbit_base import _32Bit, _64Bit
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
    def __array__(self) -> np.ndarray[Any, _DType_co]: ...

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
_DualArrayLike: TypeAlias = _SupportsArray[_DType] | _NestedSequence[_SupportsArray[_DType]] | _T | _NestedSequence[_T]

ArrayLike: TypeAlias = _Buffer | _DualArrayLike[np.dtype[Any], bool | int | float | complex | str | bytes]

# `ArrayLike<X>_co`: array-like objects that can be coerced into `X`
# given the casting rules `same_kind`
_ArrayLikeBool_co: TypeAlias = _DualArrayLike[np.dtype[np.bool], bool]
_ArrayLikeUInt_co: TypeAlias = _DualArrayLike[np.dtype[np.bool] | np.dtype[np.unsignedinteger], bool]
_ArrayLikeInt_co: TypeAlias = _DualArrayLike[np.dtype[np.bool] | np.dtype[np.integer], bool | int]
_ArrayLikeFloat_co: TypeAlias = _DualArrayLike[
    np.dtype[np.bool] | np.dtype[np.integer] | np.dtype[np.floating],
    bool | int | float,
]
_ArrayLikeComplex_co: TypeAlias = _DualArrayLike[
    (np.dtype[np.bool] | np.dtype[np.integer] | np.dtype[np.floating] | np.dtype[np.complexfloating]),
    bool | int | float | complex,
]
_ArrayLikeNumber_co: TypeAlias = _DualArrayLike[np.dtype[np.bool] | np.dtype[np.number], bool | int | float | complex]
_ArrayLikeTD64_co: TypeAlias = _DualArrayLike[np.dtype[np.bool] | np.dtype[np.integer] | np.dtype[np.timedelta64], bool | int]
_ArrayLikeDT64_co: TypeAlias = _SupportsArray[np.dtype[np.datetime64]] | _NestedSequence[_SupportsArray[np.dtype[np.datetime64]]]
_ArrayLikeObject_co: TypeAlias = _SupportsArray[np.dtype[np.object_]] | _NestedSequence[_SupportsArray[np.dtype[np.object_]]]

_ArrayLikeVoid_co: TypeAlias = _SupportsArray[np.dtype[np.void]] | _NestedSequence[_SupportsArray[np.dtype[np.void]]]
_ArrayLikeStr_co: TypeAlias = _DualArrayLike[np.dtype[np.str_], str]
_ArrayLikeBytes_co: TypeAlias = _DualArrayLike[np.dtype[np.bytes_], bytes]
_ArrayLikeString_co: TypeAlias = _DualArrayLike[StringDType, str]
_ArrayLikeAnyString_co: TypeAlias = _ArrayLikeStr_co | _ArrayLikeBytes_co | _ArrayLikeString_co

__Float64_co: TypeAlias = np.floating[_64Bit] | np.float32 | np.float16 | np.integer | np.bool
__Complex128_co: TypeAlias = np.number[_64Bit] | np.number[_32Bit] | np.float16 | np.integer | np.bool
_ArrayLikeFloat64_co: TypeAlias = _DualArrayLike[np.dtype[__Float64_co], float | int]
_ArrayLikeComplex128_co: TypeAlias = _DualArrayLike[np.dtype[__Complex128_co], complex | float | int]

# NOTE: This includes `builtins.bool`, but not `numpy.bool`.
_ArrayLikeInt: TypeAlias = _DualArrayLike[np.dtype[np.integer], int]

# Extra ArrayLike type so that pyright can deal with NDArray[Any]
# Used as the first overload, should only match NDArray[Any],
# not any actual types.
# https://github.com/numpy/numpy/pull/22193

_ArrayLikeUnknown: TypeAlias = _DualArrayLike[np.dtype[_UnknownType], _UnknownType]
