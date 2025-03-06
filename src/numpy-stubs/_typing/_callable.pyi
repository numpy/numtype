from typing import Any, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import numpy as np

from ._array_like import NDArray
from ._nested_sequence import _NestedSequence

_T = TypeVar("_T")
_T1_contra = TypeVar("_T1_contra", contravariant=True)
_T2_contra = TypeVar("_T2_contra", contravariant=True)

_2Tuple: TypeAlias = tuple[_T, _T]

###

@type_check_only
class _CanLT(Protocol):
    def __lt__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanLE(Protocol):
    def __le__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanGT(Protocol):
    def __gt__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanGE(Protocol):
    def __ge__(self, x: Any, /) -> Any: ...

@type_check_only
class _ComparisonOpLT(Protocol[_T1_contra, _T2_contra]):
    @overload
    def __call__(self, x: _T1_contra, /) -> np.bool: ...
    @overload
    def __call__(self, x: _T2_contra, /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _NestedSequence[_CanGT], /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _CanGT, /) -> np.bool: ...

@type_check_only
class _ComparisonOpLE(Protocol[_T1_contra, _T2_contra]):
    @overload
    def __call__(self, x: _T1_contra, /) -> np.bool: ...
    @overload
    def __call__(self, x: _T2_contra, /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _NestedSequence[_CanGE], /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _CanGE, /) -> np.bool: ...

@type_check_only
class _ComparisonOpGT(Protocol[_T1_contra, _T2_contra]):
    @overload
    def __call__(self, x: _T1_contra, /) -> np.bool: ...
    @overload
    def __call__(self, x: _T2_contra, /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _NestedSequence[_CanLT], /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _CanLT, /) -> np.bool: ...

@type_check_only
class _ComparisonOpGE(Protocol[_T1_contra, _T2_contra]):
    @overload
    def __call__(self, x: _T1_contra, /) -> np.bool: ...
    @overload
    def __call__(self, x: _T2_contra, /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _NestedSequence[_CanLE], /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _CanLE, /) -> np.bool: ...
