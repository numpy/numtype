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
    Self,
    SupportsIndex as CanIndex,
    SupportsInt as CanInt,
    TypeAlias,
    TypedDict,
    final,
    overload,
    type_check_only,
)
from typing_extensions import Buffer, CapsuleType, TypeAliasType, TypeVar, Unpack, deprecated

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy import _AnyShapeT, _CanSeekTellFileNo, _CastingKind, _ModeKind, _OrderCF, _OrderKACF  # noqa: ICN003
from numpy._globals import _CopyMode
from numpy._typing import (
    _ArrayLike,
    _ArrayLikeAnyString_co,
    _ArrayLikeNumber_co,
    _DTypeLike,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc as _CanArrayFunc,
    _SupportsDType as _HasDType,
)

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

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_NumericT = TypeVar("_NumericT", bound=_nt.co_complex | np.timedelta64 | np.object_)
_SafeScalarT = TypeVar("_SafeScalarT", bound=_nt.co_complex | np.timedelta64 | np.datetime64 | np.flexible)

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_ArrayT_co = TypeVar("_ArrayT_co", bound=_nt.Array, default=_nt.Array, covariant=True)
_Array1T = TypeVar("_Array1T", bound=_nt.Array[Any, _nt.Shape1N])
_Array2T = TypeVar("_Array2T", bound=_nt.Array[Any, _nt.Shape2N])

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
_OpFlag: TypeAlias = L[
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
_OpFlags: TypeAlias = Sequence[_OpFlag]
_OpAxes: TypeAlias = Sequence[CanIndex] | None

_ShapeLike1D: TypeAlias = CanIndex | tuple[CanIndex]
_ShapeLike2D: TypeAlias = tuple[CanIndex, CanIndex]
_ShapeLike3D: TypeAlias = tuple[CanIndex, CanIndex, CanIndex]

_FlatIterIndex0: TypeAlias = int | np.integer
_FlatIterIndex: TypeAlias = _FlatIterIndex0 | tuple[_FlatIterIndex0]
_FlatIterSlice0: TypeAlias = slice | EllipsisType | _nt.ToInteger_nd
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
_CmpOp: TypeAlias = L["<", "<=", "==", ">=", ">", "!="]
_BitOrder: TypeAlias = L["big", "little"]

_Ignored: TypeAlias = object
_Copy: TypeAlias = py_bool | L[2] | _CopyMode
_WeekMask: TypeAlias = str | Sequence[L[0, 1] | py_bool | np.bool]

_ToInt: TypeAlias = int | _nt.co_integer
_ToDT64: TypeAlias = int | np.datetime64 | _nt.co_integer
_ToTD64: TypeAlias = int | _nt.co_timedelta
_ToFloat: TypeAlias = float | _nt.co_float
_ToComplex: TypeAlias = complex | _nt.co_complex

_ToDate: TypeAlias = _ToDT64 | dt.date | str  # accepts strings like "1993-06-29"
_ToDelta: TypeAlias = np.timedelta64 | dt.timedelta | CanIndex | CanInt | str  # accepts same strings as `builtins.int`
_ToDateArray = TypeAliasType(
    "_ToDateArray", _ArrayLike[np.datetime64 | np.integer | np.floating | np.character] | _nt.Sequence1ND[_ToDate]
)
_ToDeltaArray = TypeAliasType("_ToDeltaArray", _ArrayLike[np.timedelta64 | np.integer] | _nt.Sequence1ND[_ToDelta])

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
    like: _CanArrayFunc | None

@type_check_only
class _KwargsCL(TypedDict, total=False):
    copy: _Copy | None
    like: _CanArrayFunc | None

@type_check_only
class _KwargsDL(TypedDict, total=False):
    device: _Device | None
    like: _CanArrayFunc | None

@type_check_only
class _KwargsDCL(TypedDict, total=False):
    device: _Device | None
    copy: _Copy | None
    like: _CanArrayFunc | None

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
    def iters(self) -> tuple[flatiter[_nt.Array[Incomplete]], ...]: ...
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
    def shape(self) -> _nt.Shape: ...

    #
    def __new__(cls, *args: _nt.ToGeneric_nd) -> Self: ...

    #
    def __iter__(self) -> Self: ...
    def __next__(self) -> tuple[Incomplete, ...]: ...

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
    def __next__(self: flatiter[_nt.Array[_ScalarT]]) -> _ScalarT: ...

    #
    @overload
    def __getitem__(self: flatiter[_nt.Array[_SafeScalarT]], i: _FlatIterIndex, /) -> _SafeScalarT: ...
    @overload
    def __getitem__(self: flatiter[_nt.Array[np.object_]], i: _FlatIterIndex, /) -> Incomplete: ...
    @overload
    def __getitem__(self, i: _FlatIterSlice, /) -> _ArrayT_co: ...
    def __setitem__(self, i: _FlatIterIndex | _FlatIterSlice, value: object, /) -> None: ...

    #
    @overload
    def __array__(self: flatiter[_nt.Array[_ScalarT]], dtype: None = None, /) -> _nt.Array1D[_ScalarT]: ...
    @overload
    def __array__(self, dtype: _DTypeLike[_ScalarT], /) -> _nt.Array1D[_ScalarT]: ...
    @overload
    def __array__(self, dtype: npt.DTypeLike | None = None, /) -> _nt.Array1D[Incomplete]: ...

@final
class nditer:
    @overload
    def __init__(
        self,
        /,
        op: _nt.ToGeneric_nd,
        flags: Sequence[_IterFlag] | None = None,
        op_flags: _OpFlags | None = None,
        op_dtypes: _nt.ToDType | None = None,
        order: _OrderKACF = "K",
        casting: _CastingKind = "safe",
        op_axes: _OpAxes = None,
        itershape: _ShapeLike | None = None,
        buffersize: CanIndex = 0,
    ) -> None: ...
    @overload
    def __init__(
        self,
        /,
        op: Sequence[_nt.ToGeneric_nd | None],
        flags: Sequence[_IterFlag] | None = None,
        op_flags: Sequence[_OpFlags] | None = None,
        op_dtypes: Sequence[_nt.ToDType | None] | None = None,
        order: _OrderKACF = "K",
        casting: _CastingKind = "safe",
        op_axes: Sequence[_OpAxes] | None = None,
        itershape: _ShapeLike | None = None,
        buffersize: CanIndex = 0,
    ) -> None: ...

    #
    @property
    def dtypes(self) -> tuple[np.dtype[Incomplete], *tuple[np.dtype[Incomplete], ...]]: ...
    @property
    def shape(self) -> _nt.Shape: ...
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
    def index(self) -> int: ...  # might raise ValueError
    @property
    def multi_index(self) -> _nt.Shape: ...  # might raise ValueError
    @property
    def iterindex(self) -> int: ...
    @property
    def itersize(self) -> int: ...
    @property
    def iterrange(self) -> tuple[int, int]: ...
    @property
    def itviews(self) -> tuple[_nt.Array[Incomplete], *tuple[_nt.Array[Incomplete], ...]]: ...
    @property
    def operands(self) -> tuple[_nt.Array[Incomplete], *tuple[_nt.Array[Incomplete], ...]]: ...

    #
    def __enter__(self) -> Self: ...
    def __exit__(self, t: type[BaseException] | None, e: BaseException | None, tb: TracebackType | None, /) -> None: ...
    def close(self) -> None: ...
    def reset(self) -> None: ...
    def enable_external_loop(self) -> None: ...
    def remove_axis(self, i: CanIndex, /) -> None: ...
    def remove_multi_index(self) -> None: ...
    def debug_print(self) -> None: ...
    def iternext(self) -> py_bool: ...

    #
    def __copy__(self) -> Self: ...
    def copy(self) -> Self: ...

    #
    def __iter__(self) -> Self: ...

    # returns either a single array or a tuple of multiple arrays
    def __next__(self) -> _nt.Array[Incomplete] | Incomplete: ...
    @property
    def value(self) -> _nt.Array[Incomplete] | Incomplete: ...

    #
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: CanIndex, /) -> _nt.Array[Incomplete]: ...
    @overload
    def __getitem__(self, index: slice, /) -> tuple[_nt.Array[Incomplete], ...]: ...
    @overload
    def __setitem__(self, index: CanIndex, value: _nt.ToGeneric_nd, /) -> None: ...
    @overload
    def __setitem__(self, index: slice, value: Sequence[_nt.ToGeneric_nd], /) -> None: ...

#
@overload
def nested_iters(
    op: _nt.ToGeneric_nd,
    axes: Sequence[Sequence[CanIndex]],
    flags: Sequence[_IterFlag] | None = None,
    op_flags: _OpFlags | None = None,
    op_dtypes: _nt.ToDType | None = None,
    order: _OrderKACF = "K",
    casting: _CastingKind = "safe",
    buffersize: CanIndex = 0,
) -> tuple[nditer, ...]: ...
@overload
def nested_iters(
    op: Sequence[_nt.ToGeneric_nd | None],
    axes: Sequence[Sequence[CanIndex]],
    flags: Sequence[_IterFlag] | None = None,
    op_flags: Sequence[_OpFlags] | None = None,
    op_dtypes: Sequence[_nt.ToDType | None] | None = None,
    order: _OrderKACF = "K",
    casting: _CastingKind = "safe",
    buffersize: CanIndex = 0,
) -> tuple[nditer, ...]: ...

###

#
def set_datetimeparse_function(*args: Incomplete, **kwargs: Incomplete) -> None: ...
def set_typeDict(dict: Mapping[str, np.dtype]) -> None: ...

#
def get_handler_name(a: _nt.Array = ..., /) -> str | None: ...
def get_handler_version(a: _nt.Array = ..., /) -> int | None: ...

###

# NOTE: Keep in sync with `zeros` and `.numeric.ones`
@overload  # 1d shape, default dtype (float64)
def empty(
    shape: _ShapeLike1D, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def empty(
    shape: _ShapeLike1D, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def empty(
    shape: _ShapeLike1D, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def empty(
    shape: _ShapeLike1D, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[Incomplete]: ...
@overload  # known shape, default dtype (float64)
def empty(
    shape: _AnyShapeT, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def empty(  # type: ignore[overload-overlap]
    shape: _AnyShapeT, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def empty(
    shape: _AnyShapeT, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def empty(
    shape: _AnyShapeT, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[Incomplete, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def empty(
    shape: _ShapeLike, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[np.float64]: ...
@overload  # unknown shape, known dtype
def empty(
    shape: _ShapeLike, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[Incomplete, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def empty(
    shape: _ShapeLike, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def empty(
    shape: _ShapeLike, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[Incomplete]: ...

# NOTE: Keep in sync with `empty` (below) and `numpy._core.numeric.ones`
@overload  # 1d shape, default dtype (float64)
def zeros(
    shape: _ShapeLike1D, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def zeros(
    shape: _ShapeLike1D, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def zeros(
    shape: _ShapeLike1D, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def zeros(
    shape: _ShapeLike1D, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[Incomplete]: ...
@overload  # known shape, default dtype (float64)
def zeros(
    shape: _AnyShapeT, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def zeros(  # type: ignore[overload-overlap]
    shape: _AnyShapeT, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def zeros(
    shape: _AnyShapeT, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def zeros(
    shape: _AnyShapeT, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[Incomplete, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def zeros(
    shape: _ShapeLike, dtype: _nt.ToDTypeFloat64 = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[np.float64]: ...
@overload  # unknown shape, known dtype
def zeros(
    shape: _ShapeLike, dtype: _DTypeT | _HasDType[_DTypeT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> np.ndarray[Incomplete, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def zeros(
    shape: _ShapeLike, dtype: _DTypeLike[_ScalarT], order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def zeros(
    shape: _ShapeLike, dtype: npt.DTypeLike = ..., order: _OrderCF = "C", **kwargs: Unpack[_KwargsDL]
) -> _nt.Array[Incomplete]: ...

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
    dtype: _DTypeT | _HasDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.bool_],
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.bool_]: ...
@overload  # bool 0d array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: _nt.ToBool_0d,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def empty_like(
    prototype: _nt.ToBool_1ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def empty_like(
    prototype: _nt.ToBool_2ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def empty_like(
    prototype: _nt.ToBool_3ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.bool_]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.intp],
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # int 0d array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: _nt.ToInt_0d,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.intp]: ...
@overload  # int 1d array-like
def empty_like(
    prototype: _nt.ToInt_1ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # int 2d array-like
def empty_like(
    prototype: _nt.ToInt_2ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.intp]: ...
@overload  # int 3d array-like
def empty_like(
    prototype: _nt.ToInt_3ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.intp]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.float64],
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # float 0d array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: _nt.ToFloat64_0d,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.float64]: ...
@overload  # float 1d array-like
def empty_like(
    prototype: _nt.ToFloat64_1ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # float 2d array-like
def empty_like(
    prototype: _nt.ToFloat64_2ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.float64]: ...
@overload  # float 3d array-like
def empty_like(
    prototype: _nt.ToFloat64_3ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.float64]: ...
@overload  # complex 0d array-like
def empty_like(  # type: ignore[overload-overlap]
    prototype: _nt.ToComplex128_0d,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.complex128]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.complex128],
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # complex 1d array-like
def empty_like(
    prototype: _nt.ToComplex128_1ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def empty_like(
    prototype: _nt.ToComplex128_2ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def empty_like(
    prototype: _nt.ToComplex128_3ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def empty_like(  # type: ignore[overload-overlap]
    prototype: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def empty_like(
    prototype: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # given shape, given dtype
def empty_like(  # type: ignore[overload-overlap]
    prototype: object,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def empty_like(
    prototype: object,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[Incomplete, _DTypeT]: ...
@overload  # given shape, given scalar-type
def empty_like(
    prototype: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def empty_like(
    prototype: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # bool array-like
def empty_like(
    prototype: _nt.ToBool_nd,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.bool_]: ...
@overload  # int array-like
def empty_like(
    prototype: _nt.ToInt_nd,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # float array-like
def empty_like(
    prototype: _nt.ToFloat64_nd,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex array-like
def empty_like(
    prototype: _nt.ToComplex128_nd,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def empty_like(
    prototype: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[Incomplete, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def empty_like(
    prototype: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[Incomplete]: ...

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
) -> _nt.Array[_ScalarT]: ...
@overload
def array(
    object: _ScalarLike_co,
    dtype: _DTypeLike[_ScalarT],
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _nt.Array0D[_ScalarT]: ...
@overload
def array(
    object: _ScalarLike_co,
    dtype: npt.DTypeLike | None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: L[0] = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _nt.Array0D[Incomplete]: ...
@overload
def array(
    object: object,
    dtype: _DTypeLike[_ScalarT],
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: int = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _nt.Array[_ScalarT]: ...
@overload
def array(
    object: object,
    dtype: npt.DTypeLike | None = None,
    *,
    order: _OrderKACF = "K",
    subok: bool = False,
    ndmin: int = 0,
    **kwargs: Unpack[_KwargsCL],
) -> _nt.Array[Incomplete]: ...

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
    a: _ArrayLike[_ScalarT], dtype: None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[_ScalarT]: ...
@overload
def asarray(
    a: _ScalarLike_co, dtype: _DTypeLike[_ScalarT], order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array0D[_ScalarT]: ...
@overload
def asarray(
    a: _ScalarLike_co, dtype: npt.DTypeLike | None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array0D[Incomplete]: ...
@overload
def asarray(
    a: object, dtype: _DTypeLike[_ScalarT], order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[_ScalarT]: ...
@overload
def asarray(
    a: object, dtype: npt.DTypeLike | None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[Incomplete]: ...

#
@overload
def asanyarray(a: _ArrayT, dtype: None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]) -> _ArrayT: ...
@overload
def asanyarray(
    a: _CanArray[_ArrayT], dtype: None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _ArrayT: ...
@overload
def asanyarray(
    a: _ArrayLike[_ScalarT], dtype: None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[_ScalarT]: ...
@overload
def asanyarray(
    a: object, dtype: _DTypeLike[_ScalarT], order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[_ScalarT]: ...
@overload
def asanyarray(
    a: object, dtype: npt.DTypeLike | None = None, order: _OrderKACF = None, **kwargs: Unpack[_KwargsDCL]
) -> _nt.Array[Incomplete]: ...

# keep in sync with asfortranarray
@overload
def ascontiguousarray(
    a: _CanArray[_nt.Array[_ScalarT, _ShapeT]], dtype: None = None, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def ascontiguousarray(
    a: _ArrayLike[_ScalarT], dtype: None = None, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT]: ...
@overload
def ascontiguousarray(a: object, dtype: None = None, *, like: _nt.Array[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def ascontiguousarray(a: object, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsL]) -> _nt.Array[_ScalarT]: ...
@overload
def ascontiguousarray(
    a: object, dtype: npt.DTypeLike | None = None, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[Incomplete]: ...

# keep in sync with ascontiguousarray
@overload
def asfortranarray(
    a: _CanArray[_nt.Array[_ScalarT, _ShapeT]], dtype: None = None, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT, _ShapeT]: ...
@overload
def asfortranarray(a: _ArrayLike[_ScalarT], dtype: None = None, **kwargs: Unpack[_KwargsL]) -> _nt.Array[_ScalarT]: ...
@overload
def asfortranarray(a: object, dtype: None = None, *, like: _nt.Array[_ScalarT]) -> _nt.Array[_ScalarT]: ...
@overload
def asfortranarray(a: object, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsL]) -> _nt.Array[_ScalarT]: ...
@overload
def asfortranarray(
    a: object, dtype: npt.DTypeLike | None = None, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[Incomplete]: ...

# `sep` is a de facto mandatory argument, as its default value is deprecated
@overload
def fromstring(
    string: bytes | str,
    dtype: type[_nt.JustFloat] | None = ...,
    count: CanIndex = -1,
    *,
    sep: str,
    **kwargs: Unpack[_KwargsL],
) -> _nt.Array[np.float64]: ...
@overload
def fromstring(
    string: bytes | str, dtype: _DTypeLike[_ScalarT], count: CanIndex = -1, *, sep: str, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT]: ...
@overload
def fromstring(
    string: bytes | str, dtype: npt.DTypeLike = ..., count: CanIndex = -1, *, sep: str, like: _nt.Array[_ScalarT]
) -> _nt.Array[_ScalarT]: ...
@overload
def fromstring(
    string: bytes | str, dtype: npt.DTypeLike, count: CanIndex = -1, *, sep: str, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[Incomplete]: ...

#
@overload
def fromfile(
    file: _ToFile, *, count: CanIndex = -1, sep: str = "", offset: CanIndex = 0, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[np.float64]: ...
@overload
def fromfile(
    file: _ToFile,
    dtype: _DTypeLike[_ScalarT],
    count: CanIndex = -1,
    sep: str = "",
    offset: CanIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> _nt.Array[_ScalarT]: ...
@overload
def fromfile(
    file: _ToFile,
    dtype: npt.DTypeLike,
    count: CanIndex = -1,
    sep: str = "",
    offset: CanIndex = 0,
    **kwargs: Unpack[_KwargsL],
) -> _nt.Array[Incomplete]: ...

#
@overload
def fromiter(
    iter: Iterable[object], dtype: _DTypeLike[_ScalarT], count: CanIndex = -1, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT]: ...
@overload
def fromiter(
    iter: Iterable[object], dtype: npt.DTypeLike, count: CanIndex = -1, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[Incomplete]: ...

#
@overload
def frombuffer(
    buffer: Buffer, *, count: CanIndex = -1, offset: CanIndex = 0, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[np.float64]: ...
@overload
def frombuffer(
    buffer: Buffer, dtype: _DTypeLike[_ScalarT], count: CanIndex = -1, offset: CanIndex = 0, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[_ScalarT]: ...
@overload
def frombuffer(
    buffer: Buffer, dtype: npt.DTypeLike, count: CanIndex = -1, offset: CanIndex = 0, **kwargs: Unpack[_KwargsL]
) -> _nt.Array[Incomplete]: ...

#
def from_dlpack(x: _CanDLPack, /, *, copy: py_bool | None = None, **kwargs: Unpack[_KwargsD]) -> _nt.Array: ...

###

#
@overload  # (stop, dtype=_)
def arange(stop: object, *, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsDL]) -> _nt.Array1D[_ScalarT]: ...
@overload  # (start, stop step, dtype)
def arange(
    start: object, stop: object, step: object, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[_ScalarT]: ...
@overload  # (start, stop, step?, dtype=)
def arange(
    start: object, stop: object, step: object = ..., *, dtype: _DTypeLike[_ScalarT], **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[_ScalarT]: ...
@overload  # (stop: int)
def arange(
    stop: int | np.intp, *, dtype: _nt.ToDTypeInt64 | None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.intp]: ...
@overload  # (start: int, stop: int, step?: int)
def arange(
    start: int | np.intp,
    stop: int | np.intp,
    step: int | np.intp = ...,
    dtype: _nt.ToDTypeInt64 | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> _nt.Array1D[np.intp]: ...
@overload  # (stop: float, dtype=f64-like)
def arange(stop: float, *, dtype: _nt.ToDTypeFloat64, **kwargs: Unpack[_KwargsDL]) -> _nt.Array1D[np.float64]: ...
@overload  # (start: float, stop: float, step?: float, dtype=f64-like)
def arange(
    start: float, stop: float, step: float = ..., *, dtype: _nt.ToDTypeFloat64, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.float64]: ...
@overload  # (start: float, stop: float, step: float, dtype=f64-like)
def arange(
    start: float, stop: float, step: float, dtype: _nt.ToDTypeFloat64, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.float64]: ...
@overload  # (stop: float)
def arange(
    stop: _nt.JustFloat, *, dtype: _nt.ToDTypeFloat64 | None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.float64]: ...
@overload  # (start: float, stop: float, step?: float)
def arange(
    start: _nt.JustFloat,
    stop: float,
    step: float = ...,
    dtype: _nt.ToDTypeFloat64 | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> _nt.Array1D[np.float64]: ...
@overload  # (start: float, stop: float, step?: float)
def arange(
    start: float,
    stop: _nt.JustFloat,
    step: float = ...,
    dtype: _nt.ToDTypeFloat64 | None = None,
    **kwargs: Unpack[_KwargsDL],
) -> _nt.Array1D[np.float64]: ...
@overload  # int-like
def arange(stop: _ToInt, *, dtype: None = None, **kwargs: Unpack[_KwargsDL]) -> _nt.Array1D[np.signedinteger]: ...
@overload  # int-like
def arange(
    start: _ToInt, stop: _ToInt, step: _ToInt = ..., dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.signedinteger]: ...
@overload  # float-like
def arange(
    stop: _ToFloat, *, dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.floating | np.signedinteger]: ...
@overload  # float-like
def arange(
    start: _ToFloat, stop: _ToFloat, step: _ToFloat = ..., dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.floating | np.signedinteger]: ...
@overload  # timedelta64
def arange(stop: np.timedelta64, *, dtype: None = None, **kwargs: Unpack[_KwargsDL]) -> _nt.Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: _ToTD64, stop: np.timedelta64, step: _ToTD64 = ..., dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.timedelta64]: ...
@overload  # timedelta64
def arange(
    start: np.timedelta64, stop: _ToTD64, step: _ToTD64 = ..., dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.timedelta64]: ...
@overload  # datetime64  (requires both start and stop)
def arange(
    start: np.datetime64, stop: np.datetime64, step: _ToDT64 = ..., dtype: None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[np.datetime64]: ...
@overload  # fallback
def arange(stop: object, *, dtype: npt.DTypeLike, **kwargs: Unpack[_KwargsDL]) -> _nt.Array1D[Incomplete]: ...
@overload  # fallback
def arange(
    start: object, stop: object, step: object = ..., dtype: npt.DTypeLike | None = None, **kwargs: Unpack[_KwargsDL]
) -> _nt.Array1D[Incomplete]: ...

###

#
@overload
def concatenate(
    arrays: _ArrayLike[_ScalarT],
    /,
    axis: CanIndex | None = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _nt.Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[_ArrayLike[_ScalarT]],
    /,
    axis: CanIndex | None = 0,
    out: None = None,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _nt.Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: CanIndex | None,
    out: _ArrayT,
    *,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: CanIndex | None = 0,
    *,
    out: _ArrayT,
    dtype: None = None,
    casting: _CastingKind = "same_kind",
) -> _ArrayT: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: CanIndex | None = 0,
    out: None = None,
    *,
    dtype: _DTypeLike[_ScalarT],
    casting: _CastingKind = "same_kind",
) -> _nt.Array[_ScalarT]: ...
@overload
def concatenate(
    arrays: SupportsLenAndGetItem[npt.ArrayLike],
    /,
    axis: CanIndex | None = 0,
    out: None = None,
    *,
    dtype: npt.DTypeLike | None = None,
    casting: _CastingKind = "same_kind",
) -> _nt.Array[Incomplete]: ...

#
def unpackbits(
    a: _nt.Array[np.uint8], /, axis: CanIndex | None = None, count: CanIndex | None = None, bitorder: _BitOrder = "big"
) -> _nt.Array[np.uint8]: ...
def packbits(
    a: _nt.CoInteger_nd, /, axis: CanIndex | None = None, bitorder: _BitOrder = "big"
) -> _nt.Array[np.uint8]: ...

#
def copyto(dst: _nt.Array, src: npt.ArrayLike, casting: _CastingKind = "same_kind") -> None: ...

#
@overload
def where(condition: npt.ArrayLike, /) -> tuple[_nt.Array[np.intp], ...]: ...
@overload
def where(condition: npt.ArrayLike, x: _ArrayLike[_ScalarT], y: _ArrayLike[_ScalarT], /) -> _nt.Array[_ScalarT]: ...
@overload
def where(condition: npt.ArrayLike, x: npt.ArrayLike, y: npt.ArrayLike, /) -> _nt.Array[Incomplete]: ...

#
def putmask(a: _nt.Array, /, mask: _nt.ToBool_nd, values: npt.ArrayLike) -> None: ...

#
@overload
def unravel_index(indices: _ToInt, shape: _ShapeLike, order: _OrderCF = "C") -> tuple[np.intp, ...]: ...
@overload
def unravel_index(
    indices: _nt.ToInteger_1nd, shape: _ShapeLike, order: _OrderCF = "C"
) -> tuple[_nt.Array[np.intp], ...]: ...

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
    multi_index: Sequence[_nt.ToInteger_1nd],
    dims: _ShapeLike,
    mode: _ModeKind | tuple[_ModeKind, ...] = "raise",
    order: _OrderCF = "C",
) -> _nt.Array[np.intp]: ...

###

#
def shares_memory(a: object, b: object, /, max_work: L[0, 1] | None = None) -> bool: ...
def may_share_memory(a: object, b: object, /, max_work: L[0, 1] | None = None) -> bool: ...
def can_cast(from_: npt.ArrayLike | npt.DTypeLike, to: npt.DTypeLike, casting: _CastingKind = "safe") -> bool: ...

#
def min_scalar_type(a: npt.ArrayLike, /) -> np.dtype[Incomplete]: ...
def result_type(*arrays_and_dtypes: npt.ArrayLike | npt.DTypeLike) -> np.dtype[Incomplete]: ...
def promote_types(type1: npt.DTypeLike, type2: npt.DTypeLike, /) -> np.dtype[Incomplete]: ...

#
@overload
def dot(a: npt.ArrayLike, b: npt.ArrayLike, out: None = None) -> Incomplete: ...
@overload
def dot(a: npt.ArrayLike, b: npt.ArrayLike, out: _ArrayT) -> _ArrayT: ...

#
@overload
def vdot(a: _ArrayLike[_NumericT], b: _ArrayLike[_NumericT], /) -> _NumericT: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
@overload
def vdot(a: _nt.CoInteger_nd, b: _nt.CoInteger_nd, /) -> np.signedinteger: ...
@overload
def vdot(a: _nt.CoFloating_nd, b: _nt.CoFloating_nd, /) -> np.floating | np.signedinteger: ...
@overload
def vdot(a: _ArrayLikeNumber_co, b: _ArrayLikeNumber_co, /) -> np.inexact | np.signedinteger: ...

#
@overload
def inner(a: _ScalarT, b: _ScalarT, /) -> _ScalarT: ...
@overload
def inner(a: _nt.Array1D[_ScalarT], b: _nt.Array1D[_ScalarT], /) -> _ScalarT: ...
@overload
def inner(a: npt.ArrayLike, b: npt.ArrayLike, /) -> Incomplete: ...

#
@overload
def interp(
    x: _ToFloat,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> np.float64: ...
@overload
def interp(
    x: _nt.Array[np.floating | np.integer, _ShapeT],
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> _nt.Array[np.float64, _ShapeT]: ...
@overload
def interp(
    x: _nt.Sequence1ND[_ToFloat],
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> _nt.Array[np.float64]: ...
@overload
def interp(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _nt.CoFloating_nd,
    left: _ToFloat | None = None,
    right: _ToFloat | None = None,
) -> np.float64 | _nt.Array[np.float64]: ...

#
@overload
def interp_complex(
    x: _ToFloat,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> np.complex128: ...
@overload
def interp_complex(
    x: _nt.Array[np.floating | np.integer, _ShapeT],
    xp: _nt.CoFloating_nd,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> _nt.Array[np.complex128, _ShapeT]: ...
@overload
def interp_complex(
    x: _nt.Sequence1ND[_ToFloat],
    xp: _nt.CoFloating_nd,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> _nt.Array[np.complex128]: ...
@overload
def interp_complex(
    x: _nt.CoFloating_nd,
    xp: _nt.CoFloating_nd,
    fp: _ArrayLikeNumber_co,
    left: _ToComplex | None = None,
    right: _ToComplex | None = None,
) -> np.complex128 | _nt.Array[np.complex128]: ...

#
def count_nonzero(a: npt.ArrayLike, /) -> np.intp: ...

#
def bincount(
    x: _nt.CoInteger_nd, /, weights: _nt.CoFloating_nd | None = None, minlength: CanIndex = 0
) -> _nt.Array[np.intp]: ...

#
@overload  # 1d -> 0d
def lexsort(keys: _nt.ToGeneric_1ds, axis: CanIndex = -1) -> np.intp: ...
@overload  # 2d -> 1d
def lexsort(keys: _nt.ToGeneric_2ds, axis: CanIndex = -1) -> _nt.Array1D[np.intp]: ...
@overload
def lexsort(keys: npt.ArrayLike, axis: CanIndex = -1) -> Incomplete: ...

###

#
@final
class busdaycalendar:
    @property
    def weekmask(self) -> _nt.Array1D[np.bool]: ...
    @property
    def holidays(self) -> _nt.Array1D[np.datetime64[dt.datetime]]: ...
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
) -> _nt.Array[np.bool]: ...
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
) -> np.intp: ...
@overload
def busday_count(
    begindates: _ToDate | _ToDateArray,
    enddates: _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> _nt.Array[np.intp]: ...
@overload
def busday_count(
    begindates: _ToDateArray,
    enddates: _ToDate | _ToDateArray,
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> _nt.Array[np.intp]: ...
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
) -> _nt.Array[np.datetime64[dt.datetime]]: ...
@overload
def busday_offset(
    dates: _ToDateArray,
    offsets: _ToDelta | _ToDeltaArray,
    roll: _Roll = "raise",
    weekmask: _WeekMask = "1111100",
    holidays: _ToDateArray | None = None,
    busdaycal: busdaycalendar | None = None,
    out: None = None,
) -> _nt.Array[np.datetime64[dt.datetime]]: ...
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
    arr: _nt.Array[np.datetime64],
    unit: L["auto"] | _TimeUnit | None = None,
    timezone: _TimeZone = "naive",
    casting: _CastingKind = "same_kind",
) -> _nt.Array[np.str_]: ...

#
def datetime_data(dtype: str | _DTypeLike[np.datetime64 | np.timedelta64], /) -> tuple[str, int]: ...

###

# keep in sync with correlate2
@overload
def correlate(a: _ArrayLike[_NumericT], v: _ArrayLike[_NumericT], mode: _CorrMode = 0) -> _nt.Array1D[_NumericT]: ...
@overload
def correlate(a: npt.ArrayLike, v: npt.ArrayLike, mode: _CorrMode = 0) -> _nt.Array1D[Incomplete]: ...

# keep in sync with correlate
@overload
def correlate2(a: _ArrayLike[_NumericT], v: _ArrayLike[_NumericT], mode: _CorrMode = 0) -> _nt.Array1D[_NumericT]: ...
@overload
def correlate2(a: npt.ArrayLike, v: npt.ArrayLike, mode: _CorrMode = 0) -> _nt.Array1D[Incomplete]: ...

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
) -> Incomplete: ...

###

@overload
def scalar(dtype: np.dtype[np.object_], obj: object) -> Incomplete: ...
@overload
def scalar(dtype: np.dtypes.StringDType, obj: _nt.StringArray[Any, Any]) -> str: ...
@overload
def scalar(dtype: np.dtype[_SafeScalarT]) -> _SafeScalarT: ...
@overload
def scalar(dtype: np.dtype[_SafeScalarT], obj: bytes) -> _SafeScalarT: ...

###

@overload
def compare_chararrays(a1: _nt.ToStr_nd, a2: _nt.ToStr_nd, cmp: _CmpOp, rstrip: bool) -> _nt.Array[np.bool]: ...
@overload
def compare_chararrays(a1: _nt.ToBytes_nd, a2: _nt.ToBytes_nd, cmp: _CmpOp, rstrip: bool) -> _nt.Array[np.bool]: ...

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
def _monotonicity(x: _nt.CoFloating_nd) -> L[0, 1]: ...
def _place(input: npt.ArrayLike, mask: _nt.ToBool_nd, vals: npt.ArrayLike) -> None: ...
def _reconstruct(subtype: type[_nt.Array], shape: _AnyShapeT, dtype: _DTypeT) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
def _vec_string(a: _ArrayLikeAnyString_co, dtype: npt.DTypeLike, attr: str, /) -> _nt.Array[Incomplete]: ...
