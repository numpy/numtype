# ruff: noqa: F811
import _contextvars
import datetime as dt
from _typeshed import Incomplete, StrOrBytesPath, SupportsLenAndGetItem
from builtins import bool as py_bool
from collections.abc import Callable, Iterable, Mapping, Sequence
from types import EllipsisType, TracebackType
from typing import (
    Any,
    ClassVar,
    Final,
    Generic,
    Literal as L,
    Protocol,
    SupportsIndex,
    SupportsInt,
    TypeAlias,
    TypedDict,
    final,
    overload,
    type_check_only,
)
from typing_extensions import Buffer, CapsuleType, Self, TypeAliasType, TypeVar, Unpack, deprecated

import numpy as np
import numpy.typing as npt
from _numtype import (
    Array,
    Array0D,
    Array1D,
    Array2D,
    Array3D,
    AtLeast1D,
    AtLeast2D,
    JustComplex,
    JustFloat,
    JustInt,
    ToBool_0d,
    ToBool_1ds,
    ToBool_2ds,
    ToBool_3ds,
    ToBool_nd,
    ToComplex128_0d,
    ToComplex128_1ds,
    ToComplex128_2ds,
    ToComplex128_3ds,
    ToComplex128_nd,
    ToFloat64_0d,
    ToFloat64_1ds,
    ToFloat64_2ds,
    ToFloat64_3ds,
    ToFloat64_nd,
    ToInt_0d,
    ToInt_1ds,
    ToInt_2ds,
    ToInt_3ds,
    ToInt_nd,
)
from numpy import _AnyShapeT, _CanSeekTellFileNo, _CastingKind, _ModeKind, _OrderCF, _OrderKACF  # noqa: ICN003
from numpy._globals import _CopyMode
from numpy._typing import (
    _ArrayLike,
    _ArrayLikeAnyString_co,
    _ArrayLikeBool_co,
    _ArrayLikeBytes_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeStr_co,
    _DTypeLike,
    _NestedSequence,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc,
    _SupportsDType,
)
from numpy._typing._char_codes import _BoolCodes, _Complex128Codes, _Float64Codes, _IntPCodes

# needed for stubtest
from .umath import (
    clip as clip,
    count as count,
    endswith as endswith,
    find as find,
    index as index,
    rfind as rfind,
    rindex as rindex,
    startswith as startswith,
)

###

_T_contra = TypeVar("_T_contra", default=None, contravariant=True)

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_NumericT = TypeVar("_NumericT", bound=np.bool | np.number | np.timedelta64 | np.object_)
_SafeScalarT = TypeVar("_SafeScalarT", bound=np.bool | np.number | np.flexible | np.timedelta64 | np.datetime64)  # no `object_`

_DTypeT = TypeVar("_DTypeT", bound=np.dtype)

_ArrayT = TypeVar("_ArrayT", bound=Array)
_Array1T = TypeVar("_Array1T", bound=Array[Any, AtLeast1D])
_Array2T = TypeVar("_Array2T", bound=Array[Any, AtLeast2D])
_ArrayT_co = TypeVar("_ArrayT_co", bound=Array, default=Array, covariant=True)

###

_FlagWrite: TypeAlias = L[
    "A", "ALIGNED",
    "W", "WRITEABLE",
    "X", "WRITEBACKIFCOPY",
]  # fmt: skip
_FlagRead: TypeAlias = L[
    "C", "CONTIGUOUS", "C_CONTIGUOUS",
    "F", "FORTRAN", "F_CONTIGUOUS",
    "B", "BEHAVED",
    "O", "OWNDATA",
    "CA", "CARRAY",
    "FA", "FARRAY",
    "FNC", "FORC",
    _FlagWrite,
]  # fmt: skip

_IterFlag: TypeAlias = L[
    "buffered",
    "c_index",
    "f_index",
    "multi_index",
    "common_dtype",
    "copy_if_overlap",
    "delay_bufalloc",
    "external_loop",
    "grow_inner",
    "growinner",
    "ranged",
    "refs_ok",
    "reduce_ok",
    "zerosize_ok",
]
_IterFlagOp: TypeAlias = L[
    "readonly", "writeonly", "readwrite",
    "no_broadcast",
    "config",
    "aligned",
    "nbo",
    "copy", "updateifcopy",
    "allocate",
    "no_subtype",
    "arraymask", "writemasked",
    "overlap_assume_elementwise",
    "virtual",  # undocumented
]  # fmt: skip

_ShapeLike1D: TypeAlias = SupportsIndex | tuple[SupportsIndex]
_ShapeLike2D: TypeAlias = tuple[SupportsIndex, SupportsIndex]
_ShapeLike3D: TypeAlias = tuple[SupportsIndex, SupportsIndex, SupportsIndex]

_DTypeLikeBool: TypeAlias = type[bool] | _DTypeLike[np.bool] | _BoolCodes
_DTypeLikeIntP: TypeAlias = type[JustInt] | _IntPCodes
_DTypeLikeFloat64: TypeAlias = type[JustFloat] | _DTypeLike[np.float64] | _Float64Codes | None
_DTypeLikeComplex128: TypeAlias = type[JustComplex] | _DTypeLike[np.complex128] | _Complex128Codes

_FlatIterIndex0: TypeAlias = int | np.integer
_FlatIterIndex: TypeAlias = _FlatIterIndex0 | tuple[_FlatIterIndex0]
_FlatIterSlice0: TypeAlias = slice | EllipsisType | _ArrayLikeInt
_FlatIterSlice: TypeAlias = _FlatIterSlice0 | tuple[_FlatIterSlice0]

_Device: TypeAlias = L["cpu"]
_Roll = TypeAliasType(
    "_Roll",
    L["raise", "nat", "forward", "backward", "preceding", "following", "modifiedfollowing", "modifiedpreceding"],
)
_TimeUnit: TypeAlias = L["Y", "M", "D", "h", "m", "s", "ms", "us", "μs", "ns", "ps", "fs", "as"]
_TimeZone: TypeAlias = L["naive", "UTC", "local"] | dt.tzinfo
_CorrMode: TypeAlias = L[0, "valid", 1, "same", 2, "full"]
_ExtObjValue: TypeAlias = L["ignore", "warn", "raise", "call", "print", "log"]

_Ignored: TypeAlias = object
_Copy: TypeAlias = py_bool | L[2] | _CopyMode
_WeekMask: TypeAlias = str | Sequence[L[0, 1] | py_bool | np.bool]

_ToInt: TypeAlias = int | np.integer | np.bool
_ToDT64: TypeAlias = np.datetime64[Any] | _ToInt
_ToTD64: TypeAlias = np.timedelta64[Any] | _ToInt
_ToFloat: TypeAlias = float | np.floating | np.integer | np.bool
_ToComplex: TypeAlias = complex | np.number | np.bool

_ToDate: TypeAlias = _ToDT64 | dt.date | str  # accepts strings like "1993-06-29"
_ToDelta: TypeAlias = (
    np.timedelta64[Any] | SupportsIndex | SupportsInt | dt.timedelta | str
)  # accepts same strings as `builtins.int`
_ToDateArray = TypeAliasType(
    "_ToDateArray",
    _ArrayLike[np.datetime64[Any] | np.floating | np.integer | np.character]
    | _NestedSequence[_ToDT64 | dt.date]
    | _NestedSequence[str],
)
_ToDeltaArray = TypeAliasType(
    "_ToDeltaArray",
    _ArrayLike[np.timedelta64[Any] | np.integer] | _NestedSequence[_ToDelta],
)

_ToFile: TypeAlias = StrOrBytesPath | _CanSeekTellFileNo

###

@type_check_only
class _CanArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

@type_check_only
class _CanDLPack(Protocol[_T_contra]):
    def __dlpack__(self, /, *, stream: _T_contra | None = None) -> CapsuleType: ...

@type_check_only
class _CanWriteErr(Protocol):
    def write(self, err: str, flag: int, /) -> _Ignored: ...

@type_check_only
class _HasDoc(Protocol):
    __doc__: str | None

###

@type_check_only
class _KwargsD(TypedDict, total=False):
    device: _Device | None

@type_check_only
class _KwargsL(TypedDict, total=False):
    like: _SupportsArrayFunc | None

@type_check_only
class _KwargsCL(TypedDict, total=False):
    copy: _Copy | None
    like: _SupportsArrayFunc | None

@type_check_only
class _KwargsDL(TypedDict, total=False):
    device: _Device | None
    like: _SupportsArrayFunc | None

@type_check_only
class _KwargsDCL(TypedDict, total=False):
    device: _Device | None
    copy: _Copy | None
    like: _SupportsArrayFunc | None

@type_check_only
class _ExtObjDict(TypedDict):
    divide: _ExtObjValue
    over: _ExtObjValue
    under: _ExtObjValue
    invalid: _ExtObjValue
    call: Callable[[str, int], _Ignored] | _CanWriteErr | None
    bufsize: int

###

__version__: Final[str] = ...

DATETIMEUNITS: Final[CapsuleType] = ...
_ARRAY_API: Final[CapsuleType] = ...
_UFUNC_API: Final[CapsuleType] = ...

ALLOW_THREADS: Final = 1
BUFSIZE: Final = 8_192

CLIP: Final = 0
ITEM_HASOBJECT: Final = 1
LIST_PICKLE: Final = 2
ITEM_IS_POINTER: Final = 4
NEEDS_INIT: Final = 8
NEEDS_PYAPI: Final = 16
USE_GETITEM: Final = 32
USE_SETITEM: Final = 64

RAISE: Final = 2
WRAP: Final = 1

MAXDIMS: Final = 64

MAY_SHARE_BOUNDS: Final = 0
MAY_SHARE_EXACT: Final = -1

FPE_DIVIDEBYZERO: Final = 1
FPE_OVERFLOW: Final = 2
FPE_UNDERFLOW: Final = 4
FPE_INVALID: Final = 8

FLOATING_POINT_SUPPORT: Final = 1

UFUNC_PYVALS_NAME: Final = "UFUNC_PYVALS"
UFUNC_BUFSIZE_DEFAULT: Final = 8192

PINF: Final[float] = ...
NINF: Final[float] = ...
PZERO: Final = 0.0
NZERO: Final = -0.0
NAN: Final[float] = ...

###

# using `Final` or `TypeAlias` will break stubtest
error = Exception

tracemalloc_domain: Final[int] = ...
_extobj_contextvar: _contextvars.ContextVar[CapsuleType]

__cpu_baseline__: Final[list[str]] = ...
__cpu_dispatch__: Final[list[str]] = ...
__cpu_features__: Final[dict[str, bool]] = ...
__cpu_targets_info__: Final[dict[str, dict[str, dict[str, str]]]] = ...

typeinfo: Final[dict[str, np.dtype]] = ...
_flagdict: Final[dict[str, int]] = ...

e: Final[float] = ...
euler_gamma: Final[float] = ...
pi: Final[float] = ...

@final
class flagsobj:
    __hash__: ClassVar[None] = None  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]
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
    def __getitem__(self, key: _FlagRead, /) -> bool: ...
    def __setitem__(self, key: _FlagWrite, value: bool, /) -> None: ...

###

@final
class broadcast:
    @property
    def iters(self) -> tuple[flatiter[Any], ...]: ...
    @property
    def index(self) -> int: ...
    @property
    def nd(self) -> int: ...
    @property
    def ndim(self) -> int: ...
    @property
    def numiter(self) -> int: ...
    @property
    def size(self) -> int: ...
    @property
    def shape(self) -> tuple[int, ...]: ...

    #
    def __new__(cls, *args: npt.ArrayLike) -> Self: ...

    #
    def __next__(self) -> tuple[Any, ...]: ...
    def __iter__(self) -> Self: ...

    #
    def reset(self) -> None: ...

@final
class flatiter(Generic[_ArrayT_co]):
    __hash__: ClassVar[None] = None  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

    @property
    def base(self) -> _ArrayT_co: ...
    @property
    def coords(self) -> tuple[int, ...]: ...
    @property
    def index(self) -> int: ...

    #
    def copy(self) -> _ArrayT_co: ...

    #
    def __len__(self) -> int: ...
    def __iter__(self) -> Self: ...
    def __next__(self: flatiter[Array[_ScalarT]]) -> _ScalarT: ...

    #
    @overload
    def __getitem__(self: flatiter[Array[_SafeScalarT]], i: _FlatIterIndex, /) -> _SafeScalarT: ...
    @overload
    def __getitem__(self: flatiter[Array[np.object_]], i: _FlatIterIndex, /) -> Any: ...
    @overload
    def __getitem__(self, i: _FlatIterSlice, /) -> _ArrayT_co: ...
    def __setitem__(self, i: _FlatIterIndex | _FlatIterSlice, value: object, /) -> None: ...

    #
    @overload
    def __array__(self: flatiter[Array[_ScalarT]], dtype: None = None, /) -> Array1D[_ScalarT]: ...
    @overload
    def __array__(self, dtype: _DTypeLike[_ScalarT], /) -> Array1D[_ScalarT]: ...
    @overload
    def __array__(self, dtype: npt.DTypeLike | None = None, /) -> Array1D: ...

@final
class nditer:
    @property
    def dtypes(self) -> tuple[np.dtype, ...]: ...
    @property
    def shape(self) -> tuple[int, ...]: ...
    @property
    def ndim(self) -> int: ...

    #
    @property
    def finished(self) -> py_bool: ...
    @property
    def has_delayed_bufalloc(self) -> py_bool: ...
    @property
    def has_index(self) -> py_bool: ...
    @property
    def has_multi_index(self) -> py_bool: ...
    @property
    def iterationneedsapi(self) -> py_bool: ...

    #
    @property
    def nop(self) -> int: ...
    @property
    def index(self) -> int: ...
    @property
    def multi_index(self) -> tuple[int, ...]: ...
    @property
    def iterindex(self) -> int: ...
    @property
    def itersize(self) -> int: ...
    @property
    def iterrange(self) -> tuple[int, ...]: ...
    @property
    def itviews(self) -> tuple[Array, ...]: ...
    @property
    def operands(self) -> tuple[Array, ...]: ...
    @property
    def value(self) -> tuple[Array, ...]: ...

    #
    def __init__(
        self,
        /,
        op: Sequence[npt.ArrayLike | None] | npt.ArrayLike,
        flags: Sequence[_IterFlag] | None = None,
        op_flags: Sequence[Sequence[_IterFlagOp]] | None = None,
        op_dtypes: Sequence[npt.DTypeLike] | npt.DTypeLike = None,
        order: _OrderKACF = "K",
        casting: _CastingKind = "safe",
        op_axes: Sequence[Sequence[SupportsIndex]] | None = None,
        itershape: _ShapeLike | None = None,
        buffersize: SupportsIndex = 0,
    ) -> None: ...

    #
    def __enter__(self) -> Self: ...
    def __exit__(self, cls: type[BaseException] | None, exc: BaseException | None, tb: TracebackType | None, /) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...

    #
    def __len__(self) -> int: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> tuple[Array, ...]: ...
    def iternext(self) -> py_bool: ...

    #
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> Array: ...
    @overload
    def __getitem__(self, index: slice, /) -> tuple[Array, ...]: ...
    def __setitem__(self, index: slice | SupportsIndex, value: npt.ArrayLike, /) -> None: ...

    #
    def __copy__(self) -> Self: ...
    def copy(self) -> nditer: ...

    # .
    def debug_print(self) -> None: ...
    def enable_external_loop(self) -> None: ...

    #
    def remove_axis(self, i: SupportsIndex, /) -> None: ...
    def remove_multi_index(self) -> None: ...

def nested_iters(
    op: Sequence[npt.ArrayLike] | npt.ArrayLike,
    axes: Sequence[Sequence[SupportsIndex]],
    flags: Sequence[_IterFlag] | None = None,
    op_flags: Sequence[Sequence[_IterFlagOp]] | None = None,
    op_dtypes: Sequence[npt.DTypeLike] | npt.DTypeLike = None,
    order: _OrderKACF = "K",
    casting: _CastingKind = "safe",
    buffersize: SupportsIndex = 0,
) -> tuple[nditer, ...]: ...

###

#
def set_datetimeparse_function(*args: Incomplete, **kwargs: Incomplete) -> None: ...
def set_typeDict(dict: Mapping[str, np.dtype]) -> None: ...

#
def get_handler_name(a: Array = ..., /) -> str | None: ...
def get_handler_version(a: Array = ..., /) -> int | None: ...

###

# NOTE: Keep in sync with `zeros` and `.numeric.ones`
@overload  # 1d shape, default dtype (float64)
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def empty(
    shape: _ShapeLike1D,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D: ...
@overload  # known shape, default dtype (float64)
def empty(
    shape: _AnyShapeT,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def empty(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def empty(
    shape: _AnyShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def empty(
    shape: _AnyShapeT,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def empty(
    shape: _ShapeLike,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[np.float64]: ...
@overload  # unknown shape, known dtype
def empty(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def empty(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def empty(
    shape: _ShapeLike,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array: ...

# NOTE: Keep in sync with `empty` (below) and `numpy._core.numeric.ones`
@overload  # 1d shape, default dtype (float64)
def zeros(
    shape: _ShapeLike1D,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def zeros(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def zeros(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def zeros(
    shape: _ShapeLike1D,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array1D: ...
@overload  # known shape, default dtype (float64)
def zeros(
    shape: _AnyShapeT,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def zeros(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def zeros(
    shape: _AnyShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def zeros(
    shape: _AnyShapeT,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def zeros(
    shape: _ShapeLike,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[np.float64]: ...
@overload  # unknown shape, known dtype
def zeros(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def zeros(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def zeros(
    shape: _ShapeLike,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    **kwargs: Unpack[_KwargsDL],
) -> Array: ...

# NOTE: Keep in sync with `.numeric.{zeros,ones}_like` (all 30 overloads...)
@overload  # known array, subok=True
def empty_like(
    prototype: _ArrayT,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _ArrayT: ...
@overload  # array-like with known shape and type
def empty_like(
    prototype: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    dtype: _DTypeT | _SupportsDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload  # bool 0d array-like
def empty_like(
    prototype: ToBool_0d,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def empty_like(
    prototype: ToBool_1ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def empty_like(
    prototype: ToBool_2ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def empty_like(
    prototype: ToBool_3ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.bool_]: ...
@overload  # int 0d array-like
def empty_like(
    prototype: ToInt_0d,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.intp]: ...
@overload  # int 1d array-like
def empty_like(
    prototype: ToInt_1ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.intp]: ...
@overload  # int 2d array-like
def empty_like(
    prototype: ToInt_2ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.intp]: ...
@overload  # int 3d array-like
def empty_like(
    prototype: ToInt_3ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.intp]: ...
@overload  # float 0d array-like
def empty_like(
    prototype: ToFloat64_0d,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.float64]: ...
@overload  # float 1d array-like
def empty_like(
    prototype: ToFloat64_1ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.float64]: ...
@overload  # float 2d array-like
def empty_like(
    prototype: ToFloat64_2ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.float64]: ...
@overload  # float 3d array-like
def empty_like(
    prototype: ToFloat64_3ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.float64]: ...
@overload  # complex 0d array-like
def empty_like(
    prototype: ToComplex128_0d,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def empty_like(
    prototype: ToComplex128_1ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def empty_like(
    prototype: ToComplex128_2ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def empty_like(
    prototype: ToComplex128_3ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def empty_like(  # type: ignore[overload-overlap]
    prototype: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def empty_like(  # type: ignore[overload-overlap]
    prototype: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
@overload  # given shape, given dtype
def empty_like(  # type: ignore[overload-overlap]
    prototype: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def empty_like(  # type: ignore[overload-overlap]
    prototype: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # given shape, given scalar-type
def empty_like(
    prototype: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def empty_like(
    prototype: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
@overload  # bool array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: ToBool_nd,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.bool_]: ...
@overload  # int array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: ToInt_nd,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.intp]: ...
@overload  # float array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: ToFloat64_nd,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.float64]: ...
@overload  # complex array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: ToComplex128_nd,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def empty_like(
    prototype: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def empty_like(
    prototype: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array: ...

#
@overload
def array(
    object: _ArrayT,
    dtype: None = None,
    *,
    order: _OrderKACF = "K",
    subok: L[True],
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _ArrayT: ...
@overload
def array(
    object: _Array1T,
    dtype: None = None,
    *,
    order: _OrderKACF = "K",
    subok: L[True],
    ndmin: L[0, 1] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _Array1T: ...
@overload
def array(
    object: _Array2T,
    dtype: None = None,
    *,
    order: _OrderKACF = "K",
    subok: L[True],
    ndmin: L[0, 1, 2] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _Array2T: ...
@overload
def array(
    object: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    dtype: None = None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload
def array(
    object: _ArrayLike[_ScalarT],
    dtype: None = None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: int = 0,
    **kwargs: Unpack[_KwargsCL],
) -> Array[_ScalarT]: ...
@overload
def array(
    object: _ScalarLike_co,
    dtype: _DTypeLike[_ScalarT],
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> Array[_ScalarT, tuple[()]]: ...
@overload
def array(
    object: _ScalarLike_co,
    dtype: npt.DTypeLike | None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> Array[Any, tuple[()]]: ...
@overload
def array(
    object: object,
    dtype: _DTypeLike[_ScalarT],
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: int = 0,
    **kwargs: Unpack[_KwargsCL],
) -> Array[_ScalarT]: ...
@overload
def array(
    object: object,
    dtype: npt.DTypeLike | None = None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: int = 0,
    **kwargs: Unpack[_KwargsCL],
) -> Array: ...

#
@overload
def asarray(
    a: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    dtype: None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload
def asarray(
    a: _ArrayLike[_ScalarT],
    dtype: None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[_ScalarT]: ...
@overload
def asarray(
    a: _ScalarLike_co,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[_ScalarT, tuple[()]]: ...
@overload
def asarray(
    a: _ScalarLike_co,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[Any, tuple[()]]: ...
@overload
def asarray(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[_ScalarT]: ...
@overload
def asarray(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array: ...

#
@overload
def asanyarray(
    a: _ArrayT,
    dtype: None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> _ArrayT: ...
@overload
def asanyarray(
    a: _CanArray[_ArrayT],
    dtype: None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> _ArrayT: ...
@overload
def asanyarray(
    a: _ArrayLike[_ScalarT],
    dtype: None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[_ScalarT]: ...
@overload
def asanyarray(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array[_ScalarT]: ...
@overload
def asanyarray(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = None,
    **kwargs: Unpack[_KwargsDCL],
) -> Array: ...

# keep in sync with asfortranarray
@overload
def ascontiguousarray(
    a: _CanArray[Array[_ScalarT, _ShapeT]],
    dtype: None = None,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT, _ShapeT]: ...
@overload
def ascontiguousarray(a: _ArrayLike[_ScalarT], dtype: None = None, **kwargs: Unpack[_KwargsL]) -> Array[_ScalarT]: ...
@overload
def ascontiguousarray(a: object, dtype: None = None, *, like: Array[_ScalarT]) -> Array[_ScalarT]: ...
@overload
def ascontiguousarray(a: object, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsL]) -> Array[_ScalarT]: ...
@overload
def ascontiguousarray(a: object, dtype: npt.DTypeLike | None = None, **kwargs: Unpack[_KwargsL]) -> Array: ...

# keep in sync with ascontiguousarray
@overload
def asfortranarray(
    a: _CanArray[Array[_ScalarT, _ShapeT]],
    dtype: None = None,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT, _ShapeT]: ...
@overload
def asfortranarray(a: _ArrayLike[_ScalarT], dtype: None = None, **kwargs: Unpack[_KwargsL]) -> Array[_ScalarT]: ...
@overload
def asfortranarray(a: object, dtype: None = None, *, like: Array[_ScalarT]) -> Array[_ScalarT]: ...
@overload
def asfortranarray(a: object, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsL]) -> Array[_ScalarT]: ...
@overload
def asfortranarray(a: object, dtype: npt.DTypeLike | None = None, **kwargs: Unpack[_KwargsL]) -> Array: ...

# `sep` is a de facto mandatory argument, as its default value is deprecated
@overload
def fromstring(
    string: bytes | str,
    dtype: type[JustFloat] | None = ...,
    count: SupportsIndex = -1,
    *,
    sep: str,
    **kwargs: Unpack[_KwargsL],
) -> Array[np.float64]: ...
@overload
def fromstring(
    string: bytes | str,
    dtype: _DTypeLike[_ScalarT],
    count: SupportsIndex = -1,
    *,
    sep: str,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT]: ...
@overload
def fromstring(
    string: bytes | str,
    dtype: npt.DTypeLike = ...,
    count: SupportsIndex = -1,
    *,
    sep: str,
    like: Array[_ScalarT],
) -> Array[_ScalarT]: ...
@overload
def fromstring(
    string: bytes | str,
    dtype: npt.DTypeLike,
    count: SupportsIndex = -1,
    *,
    sep: str,
    **kwargs: Unpack[_KwargsL],
) -> Array: ...

#
@overload
def fromfile(
    file: _ToFile,
    *,
    count: SupportsIndex = -1,
    sep: str = "",
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array[np.float64]: ...
@overload
def fromfile(
    file: _ToFile,
    dtype: _DTypeLike[_ScalarT],
    count: SupportsIndex = -1,
    sep: str = "",
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT]: ...
@overload
def fromfile(
    file: _ToFile,
    dtype: npt.DTypeLike,
    count: SupportsIndex = -1,
    sep: str = "",
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array: ...

#
@overload
def fromiter(
    iter: Iterable[object],
    dtype: _DTypeLike[_ScalarT],
    count: SupportsIndex = -1,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT]: ...
@overload
def fromiter(
    iter: Iterable[object],
    dtype: npt.DTypeLike,
    count: SupportsIndex = -1,
    **kwargs: Unpack[_KwargsL],
) -> Array: ...

#
@overload
def frombuffer(
    buffer: Buffer,
    *,
    count: SupportsIndex = -1,
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array[np.float64]: ...
@overload
def frombuffer(
    buffer: Buffer,
    dtype: _DTypeLike[_ScalarT],
    count: SupportsIndex = -1,
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array[_ScalarT]: ...
@overload
def frombuffer(
    buffer: Buffer,
    dtype: npt.DTypeLike,
    count: SupportsIndex = -1,
    offset: SupportsIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> Array: ...

#
def from_dlpack(x: _CanDLPack, /, *, copy: py_bool | None = None, **kwargs: Unpack[_KwargsD]) -> Array: ...

###

#
@overload  # (stop, dtype=_)
def arange(stop: object, *, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsDL]) -> Array1D[_ScalarT]: ...
@overload  # (start, stop step, dtype)
def arange(
    start: object,
    stop: object,
    step: object,
    dtype: _DTypeLike[_ScalarT],
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[_ScalarT]: ...
@overload  # (start, stop, step?, dtype=)
def arange(
    start: object,
    stop: object,
    step: object = ...,
    *,
    dtype: _DTypeLike[_ScalarT],
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[_ScalarT]: ...
@overload  # (stop: int)
def arange(
    stop: int | np.int_,
    *,
    dtype: _DTypeLike[np.int_] | type[int] | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.int_]: ...
@overload  # (start: int, stop: int, step?: int)
def arange(
    start: int | np.int_,
    stop: int | np.int_,
    step: int | np.int_ = ...,
    dtype: _DTypeLike[np.int_] | type[int] | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.int_]: ...
@overload  # (stop: float)
def arange(
    stop: float | np.float64,
    *,
    dtype: _DTypeLike[np.float64] | type[float] | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.float64 | np.int_]: ...
@overload  # (start: float, stop: float, step?: float)
def arange(
    start: float | np.float64,
    stop: float | np.float64,
    step: float | np.float64 = ...,
    dtype: _DTypeLike[np.float64] | type[float] | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.float64 | np.int_]: ...
@overload  # int-like
def arange(
    stop: _ToInt,
    *,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.signedinteger]: ...
@overload  # int-like
def arange(
    start: _ToInt,
    stop: _ToInt,
    step: _ToInt = ...,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.signedinteger]: ...
@overload  # float-like
def arange(
    stop: _ToFloat,
    *,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.floating | np.signedinteger]: ...
@overload  # float-like
def arange(
    start: _ToFloat,
    stop: _ToFloat,
    step: _ToFloat = ...,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.floating | np.signedinteger]: ...
@overload  # timedelta64
def arange(
    stop: np.timedelta64,
    *,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: _ToTD64,
    stop: np.timedelta64,
    step: _ToTD64 = ...,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: np.timedelta64,
    stop: _ToTD64,
    step: _ToTD64 = ...,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.timedelta64]: ...
@overload  # datetime64  (requires both start and stop)
def arange(
    start: np.datetime64,
    stop: np.datetime64,
    step: _ToDT64 = ...,
    dtype: None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[np.datetime64]: ...
@overload  # fallback
def arange(
    stop: object,
    *,
    dtype: npt.DTypeLike,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[Any]: ...
@overload  # fallback
def arange(
    start: object,
    stop: object,
    step: object = ...,
    dtype: npt.DTypeLike | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> Array1D[Any]: ...

###

#
@overload
def concatenate(
    arrays: _ArrayLike[_ScalarT],
    /,
    axis: SupportsIndex | None = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[_ArrayLike[_ScalarT]],
    /,
    axis: SupportsIndex | None = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: SupportsIndex | None,
    out: _ArrayT,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: SupportsIndex | None = 0,
    *,
    out: _ArrayT,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: SupportsIndex | None = 0,
    out: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: _CastingKind = "same_kind",
) -> Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: SupportsIndex | None = 0,
    out: None = None,
    *,
    dtype: npt.DTypeLike | None = None,
    casting: _CastingKind = "same_kind",
) -> Array: ...

#
def unpackbits(
    a: Array[np.uint8],
    /,
    axis: SupportsIndex | None = None,
    count: SupportsIndex | None = None,
    bitorder: L["big", "little"] = "big",
) -> Array[np.uint8]: ...

#
def packbits(
    a: _ArrayLikeInt_co,
    /,
    axis: SupportsIndex | None = None,
    bitorder: L["big", "little"] = "big",
) -> Array[np.uint8]: ...

#
def copyto(
    dst: Array,
    src: npt.ArrayLike,
    casting: _CastingKind = "same_kind",
    where: _ArrayLikeBool_co | None = True,
) -> None: ...

#
@overload
def where(condition: npt.ArrayLike, /) -> tuple[Array[np.int_], ...]: ...
@overload
def where(condition: npt.ArrayLike, x: _ArrayLike[_ScalarT], y: _ArrayLike[_ScalarT], /) -> Array[_ScalarT]: ...
@overload
def where(condition: npt.ArrayLike, x: npt.ArrayLike, y: npt.ArrayLike, /) -> Array: ...

#
def putmask(a: Array, /, mask: _ArrayLikeBool_co, values: npt.ArrayLike) -> None: ...

#
@overload
def unravel_index(indices: _ToInt, shape: _ShapeLike, order: _OrderCF = "C") -> tuple[np.intp, ...]: ...
@overload
def unravel_index(
    indices: _ArrayLike[np.integer] | _NestedSequence[_ToInt] | _NestedSequence[_ArrayLike[np.integer]],
    shape: _ShapeLike,
    order: _OrderCF = "C",
) -> tuple[Array[np.intp], ...]: ...

#
@overload
def ravel_multi_index(
    multi_index: Sequence[_ToInt],
    dims: _ShapeLike,
    mode: _ModeKind | tuple[_ModeKind, ...] = "raise",
    order: _OrderCF = "C",
) -> np.intp: ...
@overload
def ravel_multi_index(
    multi_index: Sequence[_ArrayLike[np.integer] | _NestedSequence[np.integer | int]],
    dims: _ShapeLike,
    mode: _ModeKind | tuple[_ModeKind, ...] = "raise",
    order: _OrderCF = "C",
) -> Array[np.intp]: ...

###

#
def shares_memory(a: object, b: object, /, max_work: L[0, 1] | None = None) -> bool: ...
def may_share_memory(a: object, b: object, /, max_work: L[0, 1] | None = None) -> bool: ...
def can_cast(from_: npt.ArrayLike | npt.DTypeLike, to: npt.DTypeLike, casting: _CastingKind = "safe") -> bool: ...

#
def min_scalar_type(a: npt.ArrayLike, /) -> np.dtype: ...
def result_type(*arrays_and_dtypes: npt.ArrayLike | npt.DTypeLike) -> np.dtype: ...
def promote_types(type1: npt.DTypeLike, type2: npt.DTypeLike, /) -> np.dtype: ...

#
@overload
def dot(a: npt.ArrayLike, b: npt.ArrayLike, out: None = None) -> Any: ...
@overload
def dot(a: npt.ArrayLike, b: npt.ArrayLike, out: _ArrayT) -> _ArrayT: ...

#
@overload
def vdot(a: _ArrayLike[_NumericT], b: _ArrayLike[_NumericT], /) -> _NumericT: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def vdot(a: _ArrayLikeInt_co, b: _ArrayLikeInt_co, /) -> np.signedinteger: ...
@overload
def vdot(a: _ArrayLikeFloat_co, b: _ArrayLikeFloat_co, /) -> np.floating | np.signedinteger: ...
@overload
def vdot(a: _ArrayLikeNumber_co, b: _ArrayLikeNumber_co, /) -> np.inexact | np.signedinteger: ...

#
@overload
def inner(a: _ScalarT, b: _ScalarT, /) -> _ScalarT: ...
@overload
def inner(a: Array1D[_ScalarT], b: Array1D[_ScalarT], /) -> _ScalarT: ...
@overload
def inner(a: npt.ArrayLike, b: npt.ArrayLike, /) -> Incomplete: ...

#
@overload
def interp(
    x: _ToFloat,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> np.float64: ...
@overload
def interp(
    x: Array[np.floating | np.integer, _ShapeT],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> Array[np.float64, _ShapeT]: ...
@overload
def interp(
    x: _NestedSequence[_ToFloat],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> Array[np.float64]: ...
@overload
def interp(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeFloat_co,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> np.float64 | Array[np.float64]: ...

#
@overload
def interp_complex(
    x: _ToFloat,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> np.complex128: ...
@overload
def interp_complex(
    x: Array[np.floating | np.integer, _ShapeT],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> Array[np.complex128, _ShapeT]: ...
@overload
def interp_complex(
    x: _NestedSequence[_ToFloat],
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> Array[np.complex128]: ...
@overload
def interp_complex(
    x: _ArrayLikeFloat_co,
    xp: _ArrayLikeFloat_co,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> np.complex128 | Array[np.complex128]: ...

#
def count_nonzero(a: object, /) -> int: ...
def bincount(
    x: _ArrayLikeInt_co,
    /,
    weights: _ArrayLikeFloat_co | None = None,
    minlength: SupportsIndex = 0,
) -> Array[np.intp]: ...

#
@overload  # 2d -> 1d
def lexsort(
    keys: Array[Any, tuple[int, int]] | Sequence[Sequence[np.generic | complex | float | int]],
    axis: SupportsIndex = -1,
) -> Array1D[np.intp]: ...
@overload  # 1d -> 0d
def lexsort(keys: Array1D | Sequence[np.generic | complex | float | int], axis: SupportsIndex = -1) -> np.intp: ...
@overload  # TODO(jorenham)
def lexsort(keys: npt.ArrayLike, axis: SupportsIndex = -1) -> Incomplete: ...

###

#
@final
class busdaycalendar:
    @property
    def weekmask(self) -> Array1D[np.bool]: ...
    @property
    def holidays(self) -> Array1D[np.datetime64[dt.datetime]]: ...
    def __init__(self, /, weekmask: _WeekMask = "1111100", holidays: _ToDateArray | None = None) -> None: ...

#
@overload
def is_busday(
    dates: _ToDate,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.bool: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> Array[np.bool]: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def is_busday(
    dates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def busday_count(
    begindates: _ToDate,
    enddates: _ToDate,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.int_: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> Array[np.int_]: ...
@overload
def busday_count(
    begindates: _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> Array[np.int_]: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def busday_offset(
    dates: _ToDate,
    offsets: _ToDelta,
    roll: _Roll = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> np.datetime64[dt.datetime]: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDeltaArray,
    roll: _Roll = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> Array[np.datetime64[dt.datetime]]: ...
@overload
def busday_offset(
    dates: _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _Roll = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> Array[np.datetime64[dt.datetime]]: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _Roll,
    weekmask: _WeekMask,
    holidays: _ToDateArray | None,
    busdaycal: busdaycalendar | None,
    out: _ArrayT,
) -> _ArrayT: ...
@overload
def busday_offset(
    dates: _ToDate | _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _Roll = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def datetime_as_string(
    arr: np.datetime64,
    unit: L["auto"] | _TimeUnit | None = None,
    timezone: _TimeZone = "naive",
    casting: _CastingKind = "same_kind",
) -> np.str_: ...
@overload
def datetime_as_string(
    arr: npt.NDArray[np.datetime64],
    unit: L["auto"] | _TimeUnit | None = None,
    timezone: _TimeZone = "naive",
    casting: _CastingKind = "same_kind",
) -> Array[np.str_]: ...

#
def datetime_data(dtype: str | _DTypeLike[np.datetime64 | np.timedelta64], /) -> tuple[str, int]: ...

###

# keep in sync with correlate2
@overload
def correlate(a: _ArrayLike[_NumericT], v: _ArrayLike[_NumericT], mode: _CorrMode = 0) -> Array1D[_NumericT]: ...
@overload
def correlate(a: npt.ArrayLike, v: npt.ArrayLike, mode: _CorrMode = 0) -> Array1D: ...

# keep in sync with correlate
@overload
def correlate2(a: _ArrayLike[_NumericT], v: _ArrayLike[_NumericT], mode: _CorrMode = 0) -> Array1D[_NumericT]: ...
@overload
def correlate2(a: npt.ArrayLike, v: npt.ArrayLike, mode: _CorrMode = 0) -> Array1D: ...

#
@overload
def c_einsum(
    subscripts: str,
    *operands: npt.ArrayLike,
    out: _ArrayT,
    dtype: None = None,
    order: _OrderKACF = "K",
    casting: _CastingKind = "safe",
) -> _ArrayT: ...
@overload
def c_einsum(
    subscripts: str,
    *operands: npt.ArrayLike,
    out: None = None,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    casting: _CastingKind = "safe",
) -> Any: ...

###

@overload
def scalar(dtype: np.dtype[np.object_], obj: object) -> Any: ...
@overload
def scalar(dtype: np.dtypes.StringDType, obj: np.ndarray[Any, np.dtypes.StringDType]) -> str: ...
@overload
def scalar(dtype: np.dtype[_SafeScalarT]) -> _SafeScalarT: ...
@overload
def scalar(dtype: np.dtype[_SafeScalarT], obj: bytes) -> _SafeScalarT: ...

###

@overload
def compare_chararrays(
    a1: _ArrayLikeStr_co,
    a2: _ArrayLikeStr_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> Array[np.bool]: ...
@overload
def compare_chararrays(
    a1: _ArrayLikeBytes_co,
    a2: _ArrayLikeBytes_co,
    cmp: L["<", "<=", "==", ">=", ">", "!="],
    rstrip: bool,
) -> Array[np.bool]: ...

###

def add_docstring(obj: Callable[..., object] | _HasDoc, docstring: str, /) -> None: ...

#
@deprecated("_add_newdoc_ufunc is deprecated. Use `ufunc.__doc__ = newdoc` instead.")
def _add_newdoc_ufunc(ufunc: np.ufunc, new_docstring: str, /) -> None: ...

###

def dragon4_positional(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
def dragon4_scientific(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
def format_longfloat(*args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

###

#
def _get_madvise_hugepage() -> bool: ...
def _set_madvise_hugepage(enabled: bool, /) -> bool: ...
def _get_ndarray_c_version() -> int: ...

#

def _get_extobj_dict() -> _ExtObjDict: ...
def _make_extobj() -> CapsuleType: ...

#
def _monotonicity(x: _ArrayLikeFloat_co) -> L[0, 1]: ...
def _place(input: npt.ArrayLike, mask: _ArrayLikeBool_co, vals: npt.ArrayLike) -> None: ...
def _reconstruct(
    subtype: type[Array],
    shape: _AnyShapeT,
    dtype: _DTypeT,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
def _vec_string(a: _ArrayLikeAnyString_co, dtype: npt.DTypeLike, attr: str, /) -> Array: ...
