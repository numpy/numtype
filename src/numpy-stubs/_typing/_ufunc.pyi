from collections.abc import Callable, Sequence
from typing import (
    Any,
    Concatenate,
    Literal as L,
    Protocol,
    SupportsIndex,
    TypeAlias,
    TypedDict,
    overload,
    type_check_only,
)
from typing_extensions import Never, TypeAliasType, TypeVar, Unpack

import numpy as np
from numpy import _CastingKind, _OrderKACF  # noqa: ICN003
from numpy._typing import _NestedSequence

from ._array_like import ArrayLike, NDArray, _ArrayLikeBool_co, _ArrayLikeInt_co
from ._dtype_like import DTypeLike, _DTypeLike
from ._scalars import _ScalarLike_co
from ._shape import _ShapeLike

###
# type parameters

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=_AnyArray)
_ArrayT1 = TypeVar("_ArrayT1", bound=_AnyArray)
_ArrayT2 = TypeVar("_ArrayT2", bound=_AnyArray)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_OutT = TypeVar("_OutT")
_OutT_co = TypeVar("_OutT_co", default=Any, covariant=True)
_OutT1 = TypeVar("_OutT1", default=Any)
_OutT1_co = TypeVar("_OutT1_co", covariant=True)
_OutT2 = TypeVar("_OutT2", default=Any)
_OutT2_co = TypeVar("_OutT2_co", covariant=True)

###
# helper types

_Tuple2: TypeAlias = tuple[_T, _T]
_Tuple3: TypeAlias = tuple[_T, _T, _T]
_Tuple4: TypeAlias = tuple[_T, _T, _T, _T]
_Tuple2_: TypeAlias = tuple[_T, _T, Unpack[tuple[_T, ...]]]
_Tuple3_: TypeAlias = tuple[_T, _T, _T, Unpack[tuple[_T, ...]]]
_Tuple4_: TypeAlias = tuple[_T, _T, _T, _T, Unpack[tuple[_T, ...]]]
_Out1: TypeAlias = _T | tuple[_T]
_AnyArray: TypeAlias = NDArray[Any]
_UFuncMethod: TypeAlias = L["__call__", "reduce", "reduceat", "accumulate", "outer", "at"]

###
# helper protocols

@type_check_only
class _CanArrayUFunc(Protocol[_OutT_co]):
    def __array_ufunc__(self, ufunc: np.ufunc, method: _UFuncMethod, /, *args: Any, **kwds: Any) -> _OutT_co: ...

###
# typeddicts for kwargs

@type_check_only
class _KwargsCommon(TypedDict, total=False):
    casting: _CastingKind
    order: _OrderKACF
    subok: bool

@type_check_only
class _Kwargs2(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple2[DTypeLike] | str | None

@type_check_only
class _Kwargs3(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple3[DTypeLike] | str | None

@type_check_only
class _Kwargs4(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple4[DTypeLike] | str | None

@type_check_only
class _Kwargs3_(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple3_[DTypeLike] | str | None

@type_check_only
class _Kwargs4_(_KwargsCommon, total=False):
    where: _ArrayLikeBool_co | None
    signature: _Tuple4_[DTypeLike] | str | None

@type_check_only
class _Kwargs2_g(_KwargsCommon, total=False):
    signature: _Tuple2[DTypeLike] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

@type_check_only
class _Kwargs3_g(_KwargsCommon, total=False):
    signature: _Tuple3[DTypeLike] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

###
# ufunc method signatures

@type_check_only
class _Call11(Protocol):
    @overload  # (scalar, dtype: dtype[T]) -> T
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs2],
    ) -> _ScalarT: ...
    @overload  # (scalar) -> ?
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> Any: ...
    @overload  # (array, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[?] | ?
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _AnyArray: ...
    @overload  # (array-like) -> Array[?] | ?
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _AnyArray | Any: ...
    @overload  # (?) -> ?
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _Call11Bool(Protocol):
    @overload  # (scalar) -> bool
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> np.bool: ...
    @overload  # (array-like, out: T) -> T
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload  # (array) -> Array[bool] | bool
    def __call__(
        self,
        x: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like) -> Array[bool] | bool
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> NDArray[np.bool] | np.bool: ...

@type_check_only
class _Call12(Protocol):
    @overload
    def __call__(
        self,
        x: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: None = None,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: tuple[None, None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: _AnyArray,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x: _CanArrayUFunc,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _Tuple2[Any]: ...

@type_check_only
class _Call21Bool(Protocol):
    @overload  # (scalar, scalar) -> bool
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> np.bool: ...
    @overload  # (array-like, array) -> Array[bool]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray | _NestedSequence[_ScalarLike_co],
        /,
        out: _Out1[_AnyArray] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array, array-like) -> Array[bool]
    def __call__(
        self,
        x1: _AnyArray | _NestedSequence[_ScalarLike_co],
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[np.bool]: ...
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array-like, array-like) -> Array[bool] | bool
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> np.bool | NDArray[np.bool]: ...

@type_check_only
class _Call21(Protocol):
    @overload  # (scalar, scalar, dtype: type[T]) -> T
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ScalarT: ...
    @overload  # (scalar, scalar) -> ?
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> Any: ...
    @overload  # (array-like, array, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        /,
        out: None = None,
        *,
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, array) -> Array[?]
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...
    @overload  # (array, array-like) -> Array[?]
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array-like, array-like) -> Array[?] | ?
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray | Any: ...

@type_check_only
class _Call22(Protocol):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_ScalarT]: ...
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[Any]: ...
    @overload
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        out1: NDArray[_ScalarT] | None = None,
        out2: NDArray[_ScalarT] | None = None,
        /,
        *,
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        out1: NDArray[_ScalarT] | None = None,
        out2: NDArray[_ScalarT] | None = None,
        /,
        *,
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        dtype: _DTypeLike[_ScalarT],
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload
    def __call__(
        self,
        x1: _AnyArray,
        x2: ArrayLike,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _AnyArray,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: _ArrayT1,
        out2: None = None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike | _CanArrayUFunc,
        x2: ArrayLike | _CanArrayUFunc,
        out1: _AnyArray | None = None,
        out2: _AnyArray | None = None,
        /,
        *,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[Any]: ...

@type_check_only
class _Call11_g(Protocol):
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs2_g],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_AnyArray | None] = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2_g],
    ) -> Any: ...

@type_check_only
class _Call12_g(Protocol):
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        out: _Tuple2[None] = (None, None),
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[Any, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...

@type_check_only
class _Call21_g(Protocol):
    # scalar for 1D array-likes; ndarray otherwise
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_ArrayT],
        *,
        dtype: None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _Out1[_AnyArray | None] = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_g],
    ) -> Any: ...

@type_check_only
class _Call11_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x: _ScalarLike_co,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _Call21_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc,
        x2: _CanArrayUFunc | ArrayLike,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> Any: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _CanArrayUFunc,
        /,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3],
    ) -> Any: ...

@type_check_only
class _Call3n1_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        x3: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _OutT_co | NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _ArrayT | tuple[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        x2: _CanArrayUFunc | ArrayLike,
        x3: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Out1[_AnyArray] | None = None,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs4_],
    ) -> Any: ...

@type_check_only
class _Call1n2_py(Protocol[_OutT1_co, _OutT2_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: tuple[None, None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_OutT1_co, _OutT2_co]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: tuple[None, None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_OutT1_co | NDArray[np.object_], _OutT2_co | NDArray[np.object_]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Tuple2[_AnyArray | None] = (None, None),
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3_],
    ) -> Any: ...

@type_check_only
class _Call1n2n_py(Protocol[_OutT_co]):
    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: _Tuple2_[None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_OutT_co]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _Tuple2_[None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_OutT_co | NDArray[np.object_]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _Tuple2_[_ArrayT],
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> _Tuple2_[_ArrayT]: ...
    @overload
    def __call__(
        self,
        x1: _CanArrayUFunc | ArrayLike,
        /,
        *xs: _CanArrayUFunc | ArrayLike,
        out: _Tuple2_[_AnyArray | None] = ...,
        dtype: DTypeLike | None = None,
        **kwargs: Unpack[_Kwargs3_],
    ) -> Any: ...

_AtE: TypeAlias = Callable[Concatenate[Never, Never, ...], None]
_At1: TypeAlias = Callable[[_CanArrayUFunc, _ArrayLikeInt_co], None]
_At2: TypeAlias = Callable[[_CanArrayUFunc, _ArrayLikeInt_co, ArrayLike], None]

@type_check_only
class _ReduceE(Protocol):
    def __call__(self, array: Never, /) -> Any: ...

@type_check_only
class _Reduce2(Protocol):
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: _ShapeLike | None = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
        keepdims: bool = False,
        initial: _ScalarLike_co | None = ...,
        where: _ArrayLikeBool_co = True,
    ) -> Any: ...

@type_check_only
class _AccumulateE(Protocol):
    def __call__(self, array: Never, /) -> Any: ...

@type_check_only
class _Accumulate2(Protocol):
    @overload
    def __call__(self, array: ArrayLike, /, axis: SupportsIndex, dtype: None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def __call__(self, array: ArrayLike, /, axis: SupportsIndex = 0, dtype: None = None, *, out: _ArrayT) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        axis: SupportsIndex = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
    ) -> _AnyArray: ...

@type_check_only
class _ReduceAtE(Protocol):
    def __call__(self, array: Never, indices: Never, /) -> Any: ...

@type_check_only
class _ReduceAt2(Protocol):
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex,
        dtype: None,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        dtype: None = None,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        /,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: NDArray[_ScalarT] | None = None,
    ) -> NDArray[_ScalarT]: ...
    @overload
    def __call__(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        /,
        axis: SupportsIndex = 0,
        dtype: DTypeLike | None = None,
        out: _AnyArray | None = None,
    ) -> _AnyArray: ...

_OuterE: TypeAlias = Callable[[Never, Never], Any]

@type_check_only
class _Outer1(Protocol):
    @overload  # (array-like, array-like, out: T) -> T
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: _Out1[_ArrayT],
        **kwds: Unpack[_Kwargs3],
    ) -> _ArrayT: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: _Out1[NDArray[_ScalarT]] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> NDArray[_ScalarT]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: DTypeLike | None = None,
        out: _Out1[_AnyArray] | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> _AnyArray: ...

@type_check_only
class _Outer2(Protocol):
    @overload  # (array-like, array-like, out: (T1, None)) -> (T1, Array[?])
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[_ArrayT1, None],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _AnyArray]: ...
    @overload  # (array-like, array-like, out: (None, T2)) -> (Array[?], T2)
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[None, _ArrayT2],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_AnyArray, _ArrayT2]: ...
    @overload  # (array-like, array-like, out: (T1, T2)) -> (T1, T2)
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: None = None,
        out: tuple[_ArrayT1, _ArrayT2],
        **kwds: Unpack[_Kwargs4],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload  # (array, array-like, dtype: dtype[T]) -> Array[T]
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: _Tuple2[NDArray[_ScalarT] | None] = (None, None),
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[NDArray[_ScalarT]]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def __call__(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        dtype: DTypeLike | None = None,
        out: _Tuple2[_AnyArray | None] = (None, None),
        **kwds: Unpack[_Kwargs4],
    ) -> _Tuple2[_AnyArray]: ...

###
# specific ufunc aliases

_CallT11 = TypeVar("_CallT11", bound=Callable[Concatenate[Any, ...], object], default=_Call11)
_CallT12 = TypeVar("_CallT12", bound=Callable[Concatenate[Any, ...], tuple[object, object]], default=_Call12)
_CallT21 = TypeVar("_CallT21", bound=Callable[Concatenate[Any, Any, ...], object], default=_Call21)
_CallT22 = TypeVar("_CallT22", bound=Callable[Concatenate[Any, Any, ...], tuple[object, object]], default=_Call22)

_ufunc_1_1 = TypeAliasType(
    "_ufunc_1_1",
    np.ufunc[_CallT11, _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT11,),
)
_ufunc_1_2 = TypeAliasType(
    "_ufunc_1_2",
    np.ufunc[_CallT12, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT12,),
)
_ufunc_2_1 = TypeAliasType(
    "_ufunc_2_1",
    np.ufunc[_CallT21, _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1],
    type_params=(_CallT21,),
)
_ufunc_2_2 = TypeAliasType(
    "_ufunc_2_2",
    np.ufunc[_CallT22, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer2],
    type_params=(_CallT22,),
)

#

_CallT11G = TypeVar("_CallT11G", bound=Callable[Concatenate[Any, ...], object], default=_Call11_g)
_CallT12G = TypeVar("_CallT12G", bound=Callable[Concatenate[Any, ...], object], default=_Call12_g)
_CallT21G = TypeVar("_CallT21G", bound=Callable[Concatenate[Any, ...], object], default=_Call21_g)

_gufunc_1_1 = TypeAliasType(
    "_gufunc_1_1",
    np.ufunc[_CallT11G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT11G,),
)
_gufunc_1_2 = TypeAliasType(
    "_gufunc_1_2",
    np.ufunc[_CallT12G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_CallT12G,),
)
_gufunc_2_1 = TypeAliasType(
    "_gufunc_2_1",
    np.ufunc[_CallT21G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _Outer1],
    type_params=(_CallT21G,),
)

#

_pyfunc_1_1 = TypeAliasType(
    "_pyfunc_1_1",
    np.ufunc[_Call11_py[_OutT], _At1, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)
_pyfunc_2_1 = TypeAliasType(
    "_pyfunc_2_1",
    np.ufunc[_Call21_py[_OutT], _At2, _Reduce2, _ReduceAt2, _Accumulate2, _Outer1],
    type_params=(_OutT,),
)
_pyfunc_3n_1 = TypeAliasType(
    "_pyfunc_3n_1",
    np.ufunc[_Call3n1_py[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)
_pyfunc_1n_2 = TypeAliasType(
    "_pyfunc_1n_2",
    np.ufunc[_Call1n2_py[_OutT1, _OutT2], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT1, _OutT2),
)
_pyfunc_1n_2n = TypeAliasType(
    "_pyfunc_1n_2n",
    np.ufunc[_Call1n2n_py[_OutT], _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE],
    type_params=(_OutT,),
)
