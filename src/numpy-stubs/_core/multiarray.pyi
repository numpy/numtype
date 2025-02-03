import datetime as dt
from _typeshed import StrOrBytesPath, SupportsLenAndGetItem
from collections.abc import Callable, Iterable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Literal as L,
    Protocol,
    SupportsIndex,
    TypeAlias,
    TypedDict,
    final,
    overload,
    type_check_only,
)
from typing_extensions import CapsuleType, TypeVar, Unpack

import numpy as np
from numpy import (  # noqa: ICN003
    broadcast,
    busdaycalendar,
    correlate,
    count_nonzero,
    dtype,
    einsum as c_einsum,
    flatiter,
    from_dlpack,
    interp,
    matmul,
    ndarray,
    nditer,
    ufunc,
    vecdot,
)
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeBytes_co,
    _ArrayLikeComplex_co,
    _ArrayLikeDT64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeStr_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _DTypeLike,
    _FloatLike_co,
    _IntLike_co,
    _NestedSequence,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc,
    _SupportsDType,
    _TD64Like_co,
)
from numpy._typing._ufunc import _2PTuple, _PyFunc_Nin1P_Nout2P, _PyFunc_Nin1_Nout1, _PyFunc_Nin2_Nout1, _PyFunc_Nin3P_Nout1
from numpy.lib._array_utils_impl import normalize_axis_index

__all__ = [
    "ALLOW_THREADS",
    "BUFSIZE",
    "CLIP",
    "DATETIMEUNITS",
    "ITEM_HASOBJECT",
    "ITEM_IS_POINTER",
    "LIST_PICKLE",
    "MAXDIMS",
    "MAY_SHARE_BOUNDS",
    "MAY_SHARE_EXACT",
    "NEEDS_INIT",
    "NEEDS_PYAPI",
    "RAISE",
    "USE_GETITEM",
    "USE_SETITEM",
    "WRAP",
    "_ARRAY_API",
    "_flagdict",
    "_monotonicity",
    "_place",
    "_reconstruct",
    "_vec_string",
    "add_docstring",
    "arange",
    "array",
    "asanyarray",
    "asarray",
    "ascontiguousarray",
    "asfortranarray",
    "bincount",
    "broadcast",
    "busday_count",
    "busday_offset",
    "busdaycalendar",
    "c_einsum",
    "can_cast",
    "compare_chararrays",
    "concatenate",
    "copyto",
    "correlate",
    "correlate2",
    "count_nonzero",
    "datetime_as_string",
    "datetime_data",
    "dot",
    "dragon4_positional",
    "dragon4_scientific",
    "dtype",
    "empty",
    "empty_like",
    "error",
    "flagsobj",
    "flatiter",
    "format_longfloat",
    "from_dlpack",
    "frombuffer",
    "fromfile",
    "fromiter",
    "fromstring",
    "get_handler_name",
    "get_handler_version",
    "inner",
    "interp",
    "interp_complex",
    "is_busday",
    "lexsort",
    "matmul",
    "may_share_memory",
    "min_scalar_type",
    "ndarray",
    "nditer",
    "nested_iters",
    "normalize_axis_index",
    "packbits",
    "promote_types",
    "putmask",
    "ravel_multi_index",
    "result_type",
    "scalar",
    "set_datetimeparse_function",
    "set_typeDict",
    "shares_memory",
    "typeinfo",
    "unpackbits",
    "unravel_index",
    "vdot",
    "vecdot",
    "where",
    "zeros",
]

_ReturnT = TypeVar("_ReturnT")
_IdentityT = TypeVar("_IdentityT")

_SCT = TypeVar("_SCT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_ArrayT = TypeVar("_ArrayT", bound=ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=ndarray[Any, Any], covariant=True)

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

_Array1D: TypeAlias = ndarray[tuple[int], dtype[_SCT]]
_Array: TypeAlias = ndarray[_ShapeT, dtype[_SCT]]

# Valid time units
_UnitKind: TypeAlias = L["Y", "M", "D", "h", "m", "s", "ms", "us", "μs", "ns", "ps", "fs", "as"]

# `raise` is deliberately excluded
_RollKind: TypeAlias = L["nat", "forward", "following", "backward", "preceding", "modifiedfollowing", "modifiedpreceding"]

@type_check_only
class _SupportsArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

@type_check_only
class _KwargsEmpty(TypedDict, total=False):
    device: L["cpu"] | None
    like: _SupportsArrayFunc | None

@type_check_only
class _ConstructorEmpty(Protocol):
    # 1-D shape
    @overload
    def __call__(
        self,
        /,
        shape: int,
        dtype: None = ...,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[int], np.float64]: ...
    @overload
    def __call__(
        self,
        /,
        shape: int,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[tuple[int], _DTypeT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: int,
        dtype: type[_SCT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[int], _SCT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: int,
        dtype: DTypeLike,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[tuple[int], Any]: ...

    # known shape
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeT,
        dtype: None = ...,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, np.float64]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeT,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[_ShapeT, _DTypeT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeT,
        dtype: type[_SCT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, _SCT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeT,
        dtype: DTypeLike,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> _Array[_ShapeT, Any]: ...

    # unknown shape
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeLike,
        dtype: None = ...,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[np.float64]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeLike,
        dtype: _DTypeT | _SupportsDType[_DTypeT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> ndarray[Any, _DTypeT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeLike,
        dtype: type[_SCT],
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[_SCT]: ...
    @overload
    def __call__(
        self,
        /,
        shape: _ShapeLike,
        dtype: DTypeLike,
        order: np._OrderCF = ...,
        **kwargs: Unpack[_KwargsEmpty],
    ) -> NDArray[Any]: ...

error: Final = Exception

# from ._multiarray_umath
ITEM_HASOBJECT: Final = 1
LIST_PICKLE: Final = 2
ITEM_IS_POINTER: Final = 4
NEEDS_INIT: Final = 8
NEEDS_PYAPI: Final = 16
USE_GETITEM: Final = 32
USE_SETITEM: Final = 64
DATETIMEUNITS: Final[CapsuleType]
_ARRAY_API: Final[CapsuleType]
_flagdict: Final[dict[str, int]]
_monotonicity: Final[Callable[..., object]]
_place: Final[Callable[..., object]]
_reconstruct: Final[Callable[..., object]]
_vec_string: Final[Callable[..., object]]
correlate2: Final[Callable[..., object]]
dragon4_positional: Final[Callable[..., object]]
dragon4_scientific: Final[Callable[..., object]]
interp_complex: Final[Callable[..., object]]
set_datetimeparse_function: Final[Callable[..., object]]

def get_handler_name(a: NDArray[Any] = ..., /) -> str | None: ...
def get_handler_version(a: NDArray[Any] = ..., /) -> int | None: ...
def format_longfloat(x: np.longdouble, precision: int) -> str: ...
def scalar(dtype: _DTypeT, object: bytes | object = ...) -> ndarray[tuple[()], _DTypeT]: ...
def set_typeDict(dict_: dict[str, np.dtype[Any]], /) -> None: ...

typeinfo: Final[dict[str, np.dtype[np.generic]]]

ALLOW_THREADS: Final[int]  # 0 or 1 (system-specific)
BUFSIZE: L[8192]
CLIP: L[0]
WRAP: L[1]
RAISE: L[2]
MAXDIMS: L[32]
MAY_SHARE_BOUNDS: L[0]
MAY_SHARE_EXACT: L[-1]
tracemalloc_domain: L[389047]

zeros: Final[_ConstructorEmpty]
empty: Final[_ConstructorEmpty]

@overload
def empty_like(
    prototype: _ArrayT,
    dtype: None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> _ArrayT: ...
@overload
def empty_like(
    prototype: _ArrayLike[_SCT],
    dtype: None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def empty_like(
    prototype: object,
    dtype: None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[Any]: ...
@overload
def empty_like(
    prototype: Any,
    dtype: _DTypeLike[_SCT],
    order: np._OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[_SCT]: ...
@overload
def empty_like(
    prototype: Any,
    dtype: DTypeLike,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    shape: _ShapeLike | None = ...,
    *,
    device: L["cpu"] | None = ...,
) -> NDArray[Any]: ...

#
@overload
def array(
    object: _ArrayT,
    dtype: None = ...,
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: L[True],
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def array(
    object: _SupportsArray[_ArrayT],
    dtype: None = ...,
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: L[True],
    ndmin: L[0] = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def array(
    object: _ArrayLike[_SCT],
    dtype: None = ...,
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def array(
    object: object,
    dtype: None = ...,
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def array(
    object: Any,
    dtype: _DTypeLike[_SCT],
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def array(
    object: Any,
    dtype: DTypeLike,
    *,
    copy: bool | np._CopyMode | None = ...,
    order: np._OrderKACF = ...,
    subok: bool = ...,
    ndmin: int = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def unravel_index(
    indices: _IntLike_co,
    shape: _ShapeLike,
    order: np._OrderCF = ...,
) -> tuple[np.int_, ...]: ...
@overload
def unravel_index(
    indices: _ArrayLikeInt_co,
    shape: _ShapeLike,
    order: np._OrderCF = ...,
) -> tuple[NDArray[np.int_], ...]: ...

#
@overload
def ravel_multi_index(
    multi_index: Sequence[_IntLike_co],
    dims: Sequence[SupportsIndex],
    mode: np._ModeKind | tuple[np._ModeKind, ...] = ...,
    order: np._OrderCF = ...,
) -> np.int_: ...
@overload
def ravel_multi_index(
    multi_index: Sequence[_ArrayLikeInt_co],
    dims: Sequence[SupportsIndex],
    mode: np._ModeKind | tuple[np._ModeKind, ...] = ...,
    order: np._OrderCF = ...,
) -> NDArray[np.int_]: ...

# NOTE: Allow any sequence of array-like objects
@overload
def concatenate(
    arrays: _ArrayLike[_SCT],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: np._CastingKind | None = ...,
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: None = ...,
    casting: np._CastingKind | None = ...,
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: _DTypeLike[_SCT],
    casting: np._CastingKind | None = ...,
) -> NDArray[_SCT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: None = ...,
    *,
    dtype: DTypeLike,
    casting: np._CastingKind | None = ...,
) -> NDArray[Any]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[ArrayLike],
    /,
    axis: SupportsIndex | None = ...,
    out: _ArrayT = ...,
    *,
    dtype: DTypeLike = ...,
    casting: np._CastingKind | None = ...,
) -> _ArrayT: ...

#
def inner(a: ArrayLike, b: ArrayLike, /) -> Any: ...

#
@overload
def where(condition: ArrayLike, /) -> tuple[NDArray[np.int_], ...]: ...
@overload
def where(condition: ArrayLike, x: ArrayLike, y: ArrayLike, /) -> NDArray[Any]: ...

#
def lexsort(keys: ArrayLike, axis: SupportsIndex | None = ...) -> Any: ...
def can_cast(from_: ArrayLike | DTypeLike, to: DTypeLike, casting: np._CastingKind | None = ...) -> bool: ...
def min_scalar_type(a: ArrayLike, /) -> dtype[Any]: ...
def result_type(*arrays_and_dtypes: ArrayLike | DTypeLike) -> dtype[Any]: ...

#
@overload
def dot(a: ArrayLike, b: ArrayLike, out: None = ...) -> Any: ...
@overload
def dot(a: ArrayLike, b: ArrayLike, out: _ArrayT) -> _ArrayT: ...

#
@overload
def vdot(a: _ArrayLikeBool_co, b: _ArrayLikeBool_co, /) -> np.bool: ...
@overload
def vdot(a: _ArrayLikeUInt_co, b: _ArrayLikeUInt_co, /) -> np.unsignedinteger: ...
@overload
def vdot(a: _ArrayLikeInt_co, b: _ArrayLikeInt_co, /) -> np.signedinteger: ...
@overload
def vdot(a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, /) -> np.floating: ...
@overload
def vdot(a: _ArrayLikeComplex_co, b: _ArrayLikeComplex_co, /) -> np.complexfloating: ...
@overload
def vdot(a: _ArrayLikeTD64_co, b: _ArrayLikeTD64_co, /) -> np.timedelta64: ...
@overload
def vdot(a: _ArrayLikeObject_co, b: Any, /) -> Any: ...
@overload
def vdot(a: Any, b: _ArrayLikeObject_co, /) -> Any: ...

#
def bincount(x: ArrayLike, /, weights: ArrayLike | None = ..., minlength: SupportsIndex = ...) -> NDArray[np.int_]: ...

#
def copyto(
    dst: NDArray[Any],
    src: ArrayLike,
    casting: np._CastingKind | None = ...,
    where: _ArrayLikeBool_co | None = ...,
) -> None: ...

#
def putmask(a: NDArray[Any], /, mask: _ArrayLikeBool_co, values: ArrayLike) -> None: ...

#
def packbits(
    a: _ArrayLikeInt_co,
    /,
    axis: SupportsIndex | None = ...,
    bitorder: L["big", "little"] = ...,
) -> NDArray[np.uint8]: ...

#
def unpackbits(
    a: _ArrayLike[np.uint8],
    /,
    axis: SupportsIndex | None = ...,
    count: SupportsIndex | None = ...,
    bitorder: L["big", "little"] = ...,
) -> NDArray[np.uint8]: ...

#
def shares_memory(a: object, b: object, /, max_work: int | None = ...) -> bool: ...
def may_share_memory(a: object, b: object, /, max_work: int | None = ...) -> bool: ...

#
@overload
def asarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asarray(
    a: object,
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def asarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asarray(
    a: Any,
    dtype: DTypeLike,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def asanyarray(
    a: _ArrayT,  # Preserve subclass-information
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _ArrayT: ...
@overload
def asanyarray(
    a: _ArrayLike[_SCT],
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asanyarray(
    a: object,
    dtype: None = ...,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...
@overload
def asanyarray(
    a: Any,
    dtype: _DTypeLike[_SCT],
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def asanyarray(
    a: Any,
    dtype: DTypeLike,
    order: np._OrderKACF = ...,
    *,
    device: L["cpu"] | None = ...,
    copy: bool | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def ascontiguousarray(a: _ArrayLike[_SCT], dtype: None = ..., *, like: _SupportsArrayFunc | None = ...) -> NDArray[_SCT]: ...
@overload
def ascontiguousarray(a: object, dtype: None = ..., *, like: _SupportsArrayFunc | None = ...) -> NDArray[Any]: ...
@overload
def ascontiguousarray(a: Any, dtype: _DTypeLike[_SCT], *, like: _SupportsArrayFunc | None = ...) -> NDArray[_SCT]: ...
@overload
def ascontiguousarray(a: Any, dtype: DTypeLike, *, like: _SupportsArrayFunc | None = ...) -> NDArray[Any]: ...

#
@overload
def asfortranarray(a: _ArrayLike[_SCT], dtype: None = ..., *, like: _SupportsArrayFunc | None = ...) -> NDArray[_SCT]: ...
@overload
def asfortranarray(a: object, dtype: None = ..., *, like: _SupportsArrayFunc | None = ...) -> NDArray[Any]: ...
@overload
def asfortranarray(a: Any, dtype: _DTypeLike[_SCT], *, like: _SupportsArrayFunc | None = ...) -> NDArray[_SCT]: ...
@overload
def asfortranarray(a: Any, dtype: DTypeLike, *, like: _SupportsArrayFunc | None = ...) -> NDArray[Any]: ...

#
def promote_types(type1: DTypeLike, type2: DTypeLike, /) -> dtype[Any]: ...

# `sep` is a de facto mandatory argument, as its default value is deprecated
@overload
def fromstring(
    string: str | bytes,
    dtype: None = ...,
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def fromstring(
    string: str | bytes,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromstring(
    string: str | bytes,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    *,
    sep: str,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def frompyfunc(
    func: Callable[[Any], _ReturnT],
    /,
    nin: L[1],
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin1_Nout1[_ReturnT, None]: ...
@overload
def frompyfunc(
    func: Callable[[Any], _ReturnT],
    /,
    nin: L[1],
    nout: L[1],
    *,
    identity: _IdentityT,
) -> _PyFunc_Nin1_Nout1[_ReturnT, _IdentityT]: ...
@overload
def frompyfunc(
    func: Callable[[Any, Any], _ReturnT],
    /,
    nin: L[2],
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin2_Nout1[_ReturnT, None]: ...
@overload
def frompyfunc(
    func: Callable[[Any, Any], _ReturnT],
    /,
    nin: L[2],
    nout: L[1],
    *,
    identity: _IdentityT,
) -> _PyFunc_Nin2_Nout1[_ReturnT, _IdentityT]: ...
@overload
def frompyfunc(
    func: Callable[..., _ReturnT],
    /,
    nin: SupportsIndex,
    nout: L[1],
    *,
    identity: None = ...,
) -> _PyFunc_Nin3P_Nout1[_ReturnT, None, int]: ...
@overload
def frompyfunc(
    func: Callable[..., _ReturnT],
    /,
    nin: SupportsIndex,
    nout: L[1],
    *,
    identity: _IdentityT,
) -> _PyFunc_Nin3P_Nout1[_ReturnT, _IdentityT, int]: ...
@overload
def frompyfunc(
    func: Callable[..., _2PTuple[_ReturnT]],
    /,
    nin: SupportsIndex,
    nout: SupportsIndex,
    *,
    identity: None = ...,
) -> _PyFunc_Nin1P_Nout2P[_ReturnT, None, int, int]: ...
@overload
def frompyfunc(
    func: Callable[..., _2PTuple[_ReturnT]],
    /,
    nin: SupportsIndex,
    nout: SupportsIndex,
    *,
    identity: _IdentityT,
) -> _PyFunc_Nin1P_Nout2P[_ReturnT, _IdentityT, int, int]: ...
@overload
def frompyfunc(
    func: Callable[..., Any],
    /,
    nin: SupportsIndex,
    nout: SupportsIndex,
    *,
    identity: object | None = ...,
) -> ufunc: ...

#
@overload
def fromfile(
    file: StrOrBytesPath | np._SupportsFileMethods,
    dtype: None = ...,
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def fromfile(
    file: StrOrBytesPath | np._SupportsFileMethods,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromfile(
    file: StrOrBytesPath | np._SupportsFileMethods,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    sep: str = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def fromiter(
    iter: Iterable[Any],
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def fromiter(
    iter: Iterable[Any],
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def frombuffer(
    buffer: np._SupportsBuffer,
    dtype: None = ...,
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[np.float64]: ...
@overload
def frombuffer(
    buffer: np._SupportsBuffer,
    dtype: _DTypeLike[_SCT],
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[_SCT]: ...
@overload
def frombuffer(
    buffer: np._SupportsBuffer,
    dtype: DTypeLike,
    count: SupportsIndex = ...,
    offset: SupportsIndex = ...,
    *,
    like: _SupportsArrayFunc | None = ...,
) -> NDArray[Any]: ...

#
@overload
def arange(
    stop: _IntLike_co,
    /,
    *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.signedinteger]: ...
@overload
def arange(
    start: _IntLike_co,
    stop: _IntLike_co,
    step: _IntLike_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.signedinteger]: ...
@overload
def arange(
    stop: _FloatLike_co,
    /,
    *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.floating]: ...
@overload
def arange(
    start: _FloatLike_co,
    stop: _FloatLike_co,
    step: _FloatLike_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.floating]: ...
@overload
def arange(
    stop: _TD64Like_co,
    /,
    *,
    dtype: None = ...,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.timedelta64]: ...
@overload
def arange(
    start: _TD64Like_co,
    stop: _TD64Like_co,
    step: _TD64Like_co = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.timedelta64]: ...
@overload
def arange(  # both start and stop must always be specified for np.datetime64
    start: np.datetime64,
    stop: np.datetime64,
    step: np.datetime64 = ...,
    dtype: None = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[np.datetime64]: ...
@overload
def arange(
    stop: object,
    /,
    *,
    dtype: _DTypeLike[_SCT],
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[_SCT]: ...
@overload
def arange(
    start: object,
    stop: object,
    step: object = ...,
    dtype: _DTypeLike[_SCT] = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[_SCT]: ...
@overload
def arange(
    stop: object,
    /,
    *,
    dtype: DTypeLike,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[Any]: ...
@overload
def arange(
    start: object,
    stop: object,
    step: object = ...,
    dtype: DTypeLike = ...,
    *,
    device: L["cpu"] | None = ...,
    like: _SupportsArrayFunc | None = ...,
) -> _Array1D[Any]: ...

#
def datetime_data(dtype: str | _DTypeLike[np.datetime64] | _DTypeLike[np.timedelta64], /) -> tuple[str, int]: ...

# The datetime functions perform unsafe casts to `np.datetime64[D]`,
# so a lot of different argument types are allowed here

@overload
def busday_count(
    begindates: _ScalarLike_co | dt.date,
    enddates: _ScalarLike_co | dt.date,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> np.int_: ...
@overload
def busday_count(
    begindates: ArrayLike | dt.date | _NestedSequence[dt.date],
    enddates: ArrayLike | dt.date | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[np.int_]: ...
@overload
def busday_count(
    begindates: ArrayLike | dt.date | _NestedSequence[dt.date],
    enddates: ArrayLike | dt.date | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...

# `roll="raise"` is (more or less?) equivalent to `casting="safe"`
@overload
def busday_offset(
    dates: np.datetime64 | dt.date,
    offsets: _TD64Like_co | dt.timedelta,
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> np.datetime64: ...
@overload
def busday_offset(
    dates: _ArrayLike[np.datetime64] | dt.date | _NestedSequence[dt.date],
    offsets: _ArrayLikeTD64_co | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[np.datetime64]: ...
@overload
def busday_offset(
    dates: _ArrayLike[np.datetime64] | dt.date | _NestedSequence[dt.date],
    offsets: _ArrayLikeTD64_co | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: L["raise"] = ...,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...
@overload
def busday_offset(
    dates: _ScalarLike_co | dt.date,
    offsets: _ScalarLike_co | dt.timedelta,
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> np.datetime64: ...
@overload
def busday_offset(
    dates: ArrayLike | dt.date | _NestedSequence[dt.date],
    offsets: ArrayLike | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[np.datetime64]: ...
@overload
def busday_offset(
    dates: ArrayLike | dt.date | _NestedSequence[dt.date],
    offsets: ArrayLike | dt.timedelta | _NestedSequence[dt.timedelta],
    roll: _RollKind,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...
@overload
def is_busday(
    dates: _ScalarLike_co | dt.date,
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> np.bool: ...
@overload
def is_busday(
    dates: ArrayLike | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: None = ...,
) -> NDArray[np.bool]: ...
@overload
def is_busday(
    dates: ArrayLike | _NestedSequence[dt.date],
    weekmask: ArrayLike = ...,
    holidays: ArrayLike | dt.date | _NestedSequence[dt.date] | None = ...,
    busdaycal: busdaycalendar | None = ...,
    out: _ArrayT = ...,
) -> _ArrayT: ...
@overload
def datetime_as_string(
    arr: np.datetime64 | dt.date,
    unit: L["auto"] | _UnitKind | None = ...,
    timezone: L["naive", "UTC", "local"] | dt.tzinfo = ...,
    casting: np._CastingKind = ...,
) -> np.str_: ...
@overload
def datetime_as_string(
    arr: _ArrayLikeDT64_co | _NestedSequence[dt.date],
    unit: L["auto"] | _UnitKind | None = ...,
    timezone: L["naive", "UTC", "local"] | dt.tzinfo = ...,
    casting: np._CastingKind = ...,
) -> NDArray[np.str_]: ...
@overload
def compare_chararrays(
    a1: _ArrayLikeStr_co,
    a2: _ArrayLikeStr_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> NDArray[np.bool]: ...
@overload
def compare_chararrays(
    a1: _ArrayLikeBytes_co,
    a2: _ArrayLikeBytes_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> NDArray[np.bool]: ...
def add_docstring(obj: Callable[..., Any], docstring: str, /) -> None: ...

_GetItemKeys: TypeAlias = L[
    "C",
    "CONTIGUOUS",
    "C_CONTIGUOUS",
    "F",
    "FORTRAN",
    "F_CONTIGUOUS",
    "W",
    "WRITEABLE",
    "B",
    "BEHAVED",
    "O",
    "OWNDATA",
    "A",
    "ALIGNED",
    "X",
    "WRITEBACKIFCOPY",
    "CA",
    "CARRAY",
    "FA",
    "FARRAY",
    "FNC",
    "FORC",
]
_SetItemKeys: TypeAlias = L[
    "A",
    "ALIGNED",
    "W",
    "WRITEABLE",
    "X",
    "WRITEBACKIFCOPY",
]

@final
class flagsobj:
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]
    aligned: bool
    writeable: bool
    writebackifcopy: bool
    @property
    def behaved(self) -> bool: ...
    @property
    def c_contiguous(self) -> bool: ...
    @property
    def carray(self) -> bool: ...
    @property
    def contiguous(self) -> bool: ...
    @property
    def f_contiguous(self) -> bool: ...
    @property
    def farray(self) -> bool: ...
    @property
    def fnc(self) -> bool: ...
    @property
    def forc(self) -> bool: ...
    @property
    def fortran(self) -> bool: ...
    @property
    def num(self) -> int: ...
    @property
    def owndata(self) -> bool: ...
    def __getitem__(self, key: _GetItemKeys) -> bool: ...
    def __setitem__(self, key: _SetItemKeys, value: bool) -> None: ...

def nested_iters(
    op: ArrayLike | Sequence[ArrayLike],
    axes: Sequence[Sequence[SupportsIndex]],
    flags: Sequence[np._NDIterFlagsKind] | None = ...,
    op_flags: Sequence[Sequence[np._NDIterFlagsOp]] | None = ...,
    op_dtypes: DTypeLike | Sequence[DTypeLike] = ...,
    order: np._OrderKACF = ...,
    casting: np._CastingKind = ...,
    buffersize: SupportsIndex = ...,
) -> tuple[nditer, ...]: ...
