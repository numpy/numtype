
from typing import (
    Any,
    Generic,
    Literal,
    LiteralString,
    NoReturn,
    Protocol,
    SupportsIndex,
    TypeAlias,
    TypeVar,
    TypedDict,
    overload,
    type_check_only,
)
from typing_extensions import Unpack

import numpy as np
import numpy.typing as npt

from ._array_like import ArrayLike, _ArrayLikeBool_co, _ArrayLikeInt_co
from ._dtype_like import DTypeLike
from ._scalars import _ScalarLike_co
from ._shape import _ShapeLike

_T = TypeVar("_T")
_2Tuple: TypeAlias = tuple[_T, _T]
_3Tuple: TypeAlias = tuple[_T, _T, _T]
_4Tuple: TypeAlias = tuple[_T, _T, _T, _T]

_2PTuple: TypeAlias = tuple[_T, _T, *tuple[_T, ...]]
_3PTuple: TypeAlias = tuple[_T, _T, _T, *tuple[_T, ...]]
_4PTuple: TypeAlias = tuple[_T, _T, _T, _T, *tuple[_T, ...]]

_NTypesT_co = TypeVar("_NTypesT_co", bound=int, covariant=True)
_IdentityT_co = TypeVar("_IdentityT_co", covariant=True)
_NameT_co = TypeVar("_NameT_co", bound=LiteralString, covariant=True)
_SignatureT_co = TypeVar("_SignatureT_co", bound=LiteralString, covariant=True)

_NInT_co = TypeVar("_NInT_co", bound=int, covariant=True)
_NOutT_co = TypeVar("_NOutT_co", bound=int, covariant=True)
_OutT_co = TypeVar("_OutT_co", covariant=True)
_ArrayT = TypeVar("_ArrayT", bound=npt.NDArray[Any])

@type_check_only
class _SupportsArrayUFunc(Protocol):
    def __array_ufunc__(
        self,
        ufunc: np.ufunc,
        method: Literal["__call__", "reduce", "reduceat", "accumulate", "outer", "at"],
        *inputs: Any,
        **kwargs: Any,
    ) -> Any: ...

@type_check_only
class _UFunc3Kwargs(TypedDict, total=False):
    where: _ArrayLikeBool_co | None
    casting: np._CastingKind
    order: np._OrderKACF
    subok: bool
    signature: _3Tuple[str | None] | str | None

# NOTE: `reduce`, `accumulate`, `reduceat` and `outer` raise a ValueError for
# ufuncs that don't accept two input arguments and return one output argument.
# In such cases the respective methods return `NoReturn`

# NOTE: Similarly, `at` won't be defined for ufuncs that return
# multiple outputs; in such cases `at` is typed to return `NoReturn`

# NOTE: If 2 output types are returned then `out` must be a
# 2-tuple of arrays. Otherwise `None` or a plain array are also acceptable

# pyright: reportIncompatibleMethodOverride=false

@type_check_only
class _UFunc_Nin1_Nout1(np.ufunc, Generic[_NameT_co, _NTypesT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def __name__(self) -> _NameT_co: ...
    @property
    def __qualname__(self) -> _NameT_co: ...
    @property
    def ntypes(self) -> _NTypesT_co: ...
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[1]: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def nargs(self) -> Literal[2]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        out: None = ...,
        *,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _2Tuple[str | None] = ...,
    ) -> Any: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        *,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _2Tuple[str | None] = ...,
    ) -> npt.NDArray[Any]: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        *,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _2Tuple[str | None] = ...,
    ) -> Any: ...
    def at(self, a: _SupportsArrayUFunc, indices: _ArrayLikeInt_co, /) -> None: ...
    def reduce(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _UFunc_Nin2_Nout1(np.ufunc, Generic[_NameT_co, _NTypesT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def __name__(self) -> _NameT_co: ...
    @property
    def __qualname__(self) -> _NameT_co: ...
    @property
    def ntypes(self) -> _NTypesT_co: ...
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[2]: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def nargs(self) -> Literal[3]: ...
    @property
    def signature(self) -> None: ...

    @overload  # (scalar, scalar) -> scalar
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> Any: ...
    @overload  # (array-like, array) -> array
    def __call__(
        self,
        x1: ArrayLike,
        x2: npt.NDArray[np.generic],
        /,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array, array-like) -> array
    def __call__(
        self,
        x1: npt.NDArray[np.generic],
        x2: ArrayLike,
        /,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array-like, array-like, out=array) -> array
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]],
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any] | Any: ...
    def at(self, a: npt.NDArray[Any], indices: _ArrayLikeInt_co, b: ArrayLike, /) -> None: ...

    def reduce(
        self,
        array: ArrayLike,
        axis: _ShapeLike | None = ...,
        dtype: DTypeLike = ...,
        out: npt.NDArray[Any] | None = ...,
        keepdims: bool = ...,
        initial: Any = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> Any: ...

    def accumulate(
        self,
        array: ArrayLike,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: npt.NDArray[Any] | None = ...,
    ) -> npt.NDArray[Any]: ...

    def reduceat(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: npt.NDArray[Any] | None = ...,
    ) -> npt.NDArray[Any]: ...

    @overload  # (scalar, scalar) -> scalar
    def outer(
        self,
        A: _ScalarLike_co,
        B: _ScalarLike_co,
        /,
        *,
        out: None = None,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> Any: ...
    @overload  # (array-like, array) -> array
    def outer(
        self,
        A: ArrayLike,
        B: npt.NDArray[np.generic],
        /,
        *,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array, array-like) -> array
    def outer(
        self,
        A: npt.NDArray[np.generic],
        B: ArrayLike,
        /,
        *,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array-like, array-like, out=array) -> array
    def outer(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]],
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any]: ...
    @overload  # (array-like, array-like) -> array | scalar
    def outer(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        out: npt.NDArray[np.generic] | tuple[npt.NDArray[np.generic]] | None = None,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_UFunc3Kwargs],
    ) -> npt.NDArray[Any] | Any: ...

@type_check_only
class _UFunc_Nin1_Nout2(np.ufunc, Generic[_NameT_co, _NTypesT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def __name__(self) -> _NameT_co: ...
    @property
    def __qualname__(self) -> _NameT_co: ...
    @property
    def ntypes(self) -> _NTypesT_co: ...
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[1]: ...
    @property
    def nout(self) -> Literal[2]: ...
    @property
    def nargs(self) -> Literal[3]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        out1: None = ...,
        out2: None = ...,
        /,
        *,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _3Tuple[str | None] = ...,
    ) -> _2Tuple[Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        out1: npt.NDArray[Any] | None = ...,
        out2: npt.NDArray[Any] | None = ...,
        /,
        *,
        out: _2Tuple[npt.NDArray[Any]] = ...,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _3Tuple[str | None] = ...,
    ) -> _2Tuple[npt.NDArray[Any]]: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc,
        out1: npt.NDArray[Any] | None = ...,
        out2: npt.NDArray[Any] | None = ...,
        /,
        *,
        out: _2Tuple[npt.NDArray[Any]] = ...,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _3Tuple[str | None] = ...,
    ) -> _2Tuple[Any]: ...
    def at(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduce(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _UFunc_Nin2_Nout2(np.ufunc, Generic[_NameT_co, _NTypesT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def __name__(self) -> _NameT_co: ...
    @property
    def __qualname__(self) -> _NameT_co: ...
    @property
    def ntypes(self) -> _NTypesT_co: ...
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[2]: ...
    @property
    def nout(self) -> Literal[2]: ...
    @property
    def nargs(self) -> Literal[4]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        out1: None = ...,
        out2: None = ...,
        /,
        *,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _4Tuple[str | None] = ...,
    ) -> _2Tuple[Any]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        out1: npt.NDArray[Any] | None = ...,
        out2: npt.NDArray[Any] | None = ...,
        /,
        *,
        out: _2Tuple[npt.NDArray[Any]] = ...,
        where: _ArrayLikeBool_co | None = ...,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _4Tuple[str | None] = ...,
    ) -> _2Tuple[npt.NDArray[Any]]: ...
    def at(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduce(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _GUFunc_Nin2_Nout1(np.ufunc, Generic[_NameT_co, _NTypesT_co, _IdentityT_co, _SignatureT_co]):  # type: ignore[misc]
    @property
    def __name__(self) -> _NameT_co: ...
    @property
    def __qualname__(self) -> _NameT_co: ...
    @property
    def ntypes(self) -> _NTypesT_co: ...
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[2]: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def nargs(self) -> Literal[3]: ...
    @property
    def signature(self) -> _SignatureT_co: ...

    # Scalar for 1D array-likes; ndarray otherwise
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: None = ...,
        *,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _3Tuple[str | None] = ...,
        axes: list[_2Tuple[SupportsIndex]] = ...,
    ) -> Any: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]],
        *,
        casting: np._CastingKind = ...,
        order: np._OrderKACF = ...,
        dtype: DTypeLike = ...,
        subok: bool = ...,
        signature: str | _3Tuple[str | None] = ...,
        axes: list[_2Tuple[SupportsIndex]] = ...,
    ) -> npt.NDArray[Any]: ...
    def at(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduce(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _PyFunc_Kwargs_Nargs2(TypedDict, total=False):
    where: _ArrayLikeBool_co | None
    casting: np._CastingKind
    order: np._OrderKACF
    dtype: DTypeLike
    subok: bool
    signature: str | tuple[DTypeLike, DTypeLike]

@type_check_only
class _PyFunc_Kwargs_Nargs3(TypedDict, total=False):
    where: _ArrayLikeBool_co | None
    casting: np._CastingKind
    order: np._OrderKACF
    dtype: DTypeLike
    subok: bool
    signature: str | tuple[DTypeLike, DTypeLike, DTypeLike]

@type_check_only
class _PyFunc_Kwargs_Nargs3P(TypedDict, total=False):
    where: _ArrayLikeBool_co | None
    casting: np._CastingKind
    order: np._OrderKACF
    dtype: DTypeLike
    subok: bool
    signature: str | _3PTuple[DTypeLike]

@type_check_only
class _PyFunc_Kwargs_Nargs4P(TypedDict, total=False):
    where: _ArrayLikeBool_co | None
    casting: np._CastingKind
    order: np._OrderKACF
    dtype: DTypeLike
    subok: bool
    signature: str | _4PTuple[DTypeLike]

@type_check_only
class _PyFunc_Nin1_Nout1(np.ufunc, Generic[_OutT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[1]: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def nargs(self) -> Literal[2]: ...
    @property
    def ntypes(self) -> Literal[1]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs2],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs2],
    ) -> _OutT_co | npt.NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs2],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs2],
    ) -> Any: ...

    def at(self, a: _SupportsArrayUFunc, ixs: _ArrayLikeInt_co, /) -> None: ...
    def reduce(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _PyFunc_Nin2_Nout1(np.ufunc, Generic[_OutT_co, _IdentityT_co]):  # type: ignore[misc]
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> Literal[2]: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def nargs(self) -> Literal[3]: ...
    @property
    def ntypes(self) -> Literal[1]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        /,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _OutT_co | npt.NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        /,
        out: _ArrayT | tuple[_ArrayT],
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc,
        x2: _SupportsArrayUFunc | ArrayLike,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> Any: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: _SupportsArrayUFunc,
        /,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> Any: ...

    def at(self, a: _SupportsArrayUFunc, ixs: _ArrayLikeInt_co, b: ArrayLike, /) -> None: ...

    @overload
    def reduce(
        self,
        array: ArrayLike,
        axis: _ShapeLike | None,
        dtype: DTypeLike,
        out: _ArrayT,
        /,
        keepdims: bool = ...,
        initial: _ScalarLike_co = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> _ArrayT: ...
    @overload
    def reduce(
        self,
        /,
        array: ArrayLike,
        axis: _ShapeLike | None = ...,
        dtype: DTypeLike = ...,
        *,
        out: _ArrayT | tuple[_ArrayT],
        keepdims: bool = ...,
        initial: _ScalarLike_co = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> _ArrayT: ...
    @overload
    def reduce(
        self,
        /,
        array: ArrayLike,
        axis: _ShapeLike | None = ...,
        dtype: DTypeLike = ...,
        out: None = ...,
        *,
        keepdims: Literal[True],
        initial: _ScalarLike_co = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> npt.NDArray[np.object_]: ...
    @overload
    def reduce(
        self,
        /,
        array: ArrayLike,
        axis: _ShapeLike | None = ...,
        dtype: DTypeLike = ...,
        out: None = ...,
        keepdims: bool = ...,
        initial: _ScalarLike_co = ...,
        where: _ArrayLikeBool_co = ...,
    ) -> _OutT_co | npt.NDArray[np.object_]: ...

    @overload
    def reduceat(
        self,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex,
        dtype: DTypeLike,
        out: _ArrayT,
        /,
    ) -> _ArrayT: ...
    @overload
    def reduceat(
        self,
        /,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        *,
        out: _ArrayT | tuple[_ArrayT],
    ) -> _ArrayT: ...
    @overload
    def reduceat(
        self,
        /,
        array: ArrayLike,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: None = ...,
    ) -> npt.NDArray[np.object_]: ...
    @overload
    def reduceat(
        self,
        /,
        array: _SupportsArrayUFunc,
        indices: _ArrayLikeInt_co,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
    ) -> Any: ...

    @overload
    def accumulate(
        self,
        array: ArrayLike,
        axis: SupportsIndex,
        dtype: DTypeLike,
        out: _ArrayT,
        /,
    ) -> _ArrayT: ...
    @overload
    def accumulate(
        self,
        array: ArrayLike,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        *,
        out: _ArrayT | tuple[_ArrayT],
    ) -> _ArrayT: ...
    @overload
    def accumulate(
        self,
        /,
        array: ArrayLike,
        axis: SupportsIndex = ...,
        dtype: DTypeLike = ...,
        out: None = ...,
    ) -> npt.NDArray[np.object_]: ...

    @overload
    def outer(
        self,
        A: _ScalarLike_co,
        B: _ScalarLike_co,
        /,
        *,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _OutT_co: ...
    @overload
    def outer(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _OutT_co | npt.NDArray[np.object_]: ...
    @overload
    def outer(
        self,
        A: ArrayLike,
        B: ArrayLike,
        /,
        *,
        out: _ArrayT,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> _ArrayT: ...
    @overload
    def outer(
        self,
        A: _SupportsArrayUFunc,
        B: _SupportsArrayUFunc | ArrayLike,
        /, *,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> Any: ...
    @overload
    def outer(
        self,
        A: _ScalarLike_co,
        B: _SupportsArrayUFunc | ArrayLike,
        /, *,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3],
    ) -> Any: ...

@type_check_only
class _PyFunc_Nin3P_Nout1(np.ufunc, Generic[_OutT_co, _IdentityT_co, _NInT_co]):  # type: ignore[misc]
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> _NInT_co: ...
    @property
    def nout(self) -> Literal[1]: ...
    @property
    def ntypes(self) -> Literal[1]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        x2: _ScalarLike_co,
        x3: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs4P],
    ) -> _OutT_co: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs4P],
    ) -> _OutT_co | npt.NDArray[np.object_]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        x2: ArrayLike,
        x3: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _ArrayT | tuple[_ArrayT],
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs4P],
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc | ArrayLike,
        x2: _SupportsArrayUFunc | ArrayLike,
        x3: _SupportsArrayUFunc | ArrayLike,
        /,
        *xs: _SupportsArrayUFunc | ArrayLike,
        out: npt.NDArray[Any] | tuple[npt.NDArray[Any]] | None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs4P],
    ) -> Any: ...

    def at(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduce(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...

@type_check_only
class _PyFunc_Nin1P_Nout2P(np.ufunc, Generic[_OutT_co, _IdentityT_co, _NInT_co, _NOutT_co]):  # type: ignore[misc]
    @property
    def identity(self) -> _IdentityT_co: ...
    @property
    def nin(self) -> _NInT_co: ...
    @property
    def nout(self) -> _NOutT_co: ...
    @property
    def ntypes(self) -> Literal[1]: ...
    @property
    def signature(self) -> None: ...

    @overload
    def __call__(
        self,
        x1: _ScalarLike_co,
        /,
        *xs: _ScalarLike_co,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3P],
    ) -> _2PTuple[_OutT_co]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3P],
    ) -> _2PTuple[_OutT_co | npt.NDArray[np.object_]]: ...
    @overload
    def __call__(
        self,
        x1: ArrayLike,
        /,
        *xs: ArrayLike,
        out: _2PTuple[_ArrayT],
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3P],
    ) -> _2PTuple[_ArrayT]: ...
    @overload
    def __call__(
        self,
        x1: _SupportsArrayUFunc | ArrayLike,
        /,
        *xs: _SupportsArrayUFunc | ArrayLike,
        out: _2PTuple[npt.NDArray[Any]] | None = ...,
        **kwargs: Unpack[_PyFunc_Kwargs_Nargs3P],
    ) -> Any: ...

    def at(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduce(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def accumulate(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def reduceat(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
    def outer(self, /, *args: Any, **kwargs: Any) -> NoReturn: ...
