from typing import Any, NoReturn, Protocol, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar

import numpy as np

from . import NBitBase
from ._array_like import NDArray
from ._nbit import _NBitLongDouble
from ._nbit_base import _16Bit, _32Bit
from ._nested_sequence import _NestedSequence
from ._scalars import _BoolLike_co, _IntLike_co

_T = TypeVar("_T")
_T1_contra = TypeVar("_T1_contra", contravariant=True)
_T2_contra = TypeVar("_T2_contra", contravariant=True)

_NBitT = TypeVar("_NBitT", bound=NBitBase)
_NBitT1 = TypeVar("_NBitT1", bound=NBitBase)

_RealT = TypeVar("_RealT", bound=np.integer | np.floating)
_InexactT = TypeVar("_InexactT", bound=np.inexact)
_NumberT = TypeVar("_NumberT", bound=np.number)
_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)

_2Tuple: TypeAlias = tuple[_T, _T]

###

@type_check_only
class _BoolOp(Protocol[_ScalarT_co]):
    @overload
    def __call__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __call__(self, x: bool | np.bool, /) -> _ScalarT_co: ...
    @overload
    def __call__(self, x: int, /) -> _ScalarT_co | np.int_: ...
    @overload
    def __call__(self, x: int | float, /) -> _ScalarT_co | np.int_ | np.float64: ...
    @overload
    def __call__(self, x: int | float | complex, /) -> _ScalarT_co | np.int_ | np.float64 | np.complex128: ...

@type_check_only
class _BoolSub(Protocol):
    # Note that `x: bool` is absent here
    @overload
    def __call__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __call__(self, x: bool, /) -> NoReturn: ...
    @overload
    def __call__(self, x: int, /) -> np.int_: ...
    @overload
    def __call__(self, x: int | float, /) -> np.int_ | np.float64: ...
    @overload
    def __call__(self, x: int | float | complex, /) -> np.int_ | np.float64 | np.complex128: ...

@type_check_only
class _BoolTrueDiv(Protocol):
    @overload
    def __call__(self, x: _InexactT, /) -> _InexactT: ...
    @overload
    def __call__(self, x: int | float | _IntLike_co, /) -> np.float64: ...
    @overload
    def __call__(self, x: int | float | complex, /) -> np.float64 | np.complex128: ...

@type_check_only
class _BoolMod(Protocol):
    @overload
    def __call__(self, x: _RealT, /) -> _RealT: ...
    @overload
    def __call__(self, x: _BoolLike_co, /) -> np.int8: ...
    @overload
    def __call__(self, x: int, /) -> np.int8 | np.int_: ...
    @overload
    def __call__(self, x: int | float, /) -> np.int8 | np.int_ | np.float64: ...

@type_check_only
class _BoolDivMod(Protocol):
    @overload
    def __call__(self, x: _RealT, /) -> _2Tuple[_RealT]: ...
    @overload
    def __call__(self, x: _BoolLike_co, /) -> _2Tuple[np.int8]: ...
    @overload
    def __call__(self, x: int, /) -> _2Tuple[np.int8] | _2Tuple[np.int_]: ...
    @overload
    def __call__(self, x: int | float, /) -> _2Tuple[np.int8] | _2Tuple[np.int_] | _2Tuple[np.float64]: ...

###

@type_check_only
class _FloatOp(Protocol[_NBitT]):
    @overload
    def __call__(self, x: np.bool | np.uint8 | int, /) -> np.floating[_NBitT]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self: _FloatOp[_16Bit] | _FloatOp[_32Bit], x: np.uint16 | np.int32 | np.float32, /) -> np.float32: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self: _FloatOp[_16Bit] | _FloatOp[_32Bit],
        x: np.uint32 | np.uint64 | np.uint | np.int64 | np.float64,
        /,
    ) -> np.float64: ...
    @overload
    def __call__(self: _FloatOp[_16Bit] | _FloatOp[_32Bit], x: np.complex64, /) -> np.complex64: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self: _FloatOp[_16Bit] | _FloatOp[_32Bit], x: np.complex128, /) -> np.complex128: ...
    @overload
    def __call__(self: _FloatOp[_NBitLongDouble], x: np.integer | np.floating, /) -> np.longdouble: ...
    @overload
    def __call__(self, x: np.longdouble, /) -> np.longdouble: ...
    @overload
    def __call__(self: _FloatOp[_NBitLongDouble], x: np.complexfloating, /) -> np.clongdouble: ...
    @overload
    def __call__(self, x: np.signedinteger[_NBitT1] | np.floating[_NBitT1], /) -> np.floating[_NBitT | _NBitT1]: ...
    @overload
    def __call__(self, x: int | float, /) -> np.floating[_NBitT]: ...
    @overload
    def __call__(self, x: int | float | complex, /) -> np.floating[_NBitT] | np.complexfloating[_NBitT]: ...

@type_check_only
class _FloatMod(Protocol[_NBitT]):
    @overload
    def __call__(self, x: np.bool | np.uint8 | int | float, /) -> np.floating[_NBitT]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self: _FloatMod[_16Bit] | _FloatMod[_32Bit], x: np.uint16 | np.int32 | np.float32, /) -> np.float32: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self: _FloatMod[_16Bit] | _FloatMod[_32Bit],
        x: np.uint32 | np.uint64 | np.uint | np.int64 | np.float64,
        /,
    ) -> np.float64: ...
    @overload
    def __call__(self: _FloatMod[_NBitLongDouble], x: np.integer | np.floating, /) -> np.longdouble: ...
    @overload
    def __call__(self, x: np.signedinteger[_NBitT1] | np.floating[_NBitT1], /) -> np.floating[_NBitT | _NBitT1]: ...

class _FloatDivMod(Protocol[_NBitT]):
    @overload
    def __call__(self, x: np.bool | np.uint8 | int | float, /) -> _2Tuple[np.floating[_NBitT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self: _FloatDivMod[_16Bit] | _FloatDivMod[_32Bit],
        x: np.uint16 | np.int32 | np.float32,
        /,
    ) -> _2Tuple[np.float32]: ...
    @overload
    def __call__(
        self: _FloatDivMod[_16Bit] | _FloatDivMod[_32Bit],
        x: np.uint32 | np.uint64 | np.uint | np.int64 | np.float64,
        /,
    ) -> _2Tuple[np.float64]: ...
    @overload
    def __call__(self: _FloatDivMod[_NBitLongDouble], x: np.integer | np.floating, /) -> _2Tuple[np.longdouble]: ...
    @overload
    def __call__(self, x: np.signedinteger[_NBitT1] | np.floating[_NBitT1], /) -> _2Tuple[np.floating[_NBitT | _NBitT1]]: ...

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
    def __call__(self, x: _NestedSequence[_CanGT], /) -> NDArray[np.bool]: ...
    @overload
    def __call__(self, x: _CanGT, /) -> np.bool: ...
