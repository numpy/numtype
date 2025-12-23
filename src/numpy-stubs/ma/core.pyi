from _typeshed import Incomplete
from collections.abc import Callable, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Generic,
    Literal as L,
    Never,
    Protocol,
    Self,
    SupportsIndex as CanIndex,
    TypeAlias,
    TypedDict,
    overload,
    type_check_only,
)
from typing_extensions import Buffer, TypeVar, Unpack, override

import _numtype as _nt
import numpy as np
from numpy import _OrderACF, _OrderKACF, amax, amin, bool_, expand_dims  # noqa: ICN003
from numpy._globals import _NoValueType
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    _ArrayLike,
    _DTypeLike,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc as _CanArrayFunc,
    _SupportsDType as _HasDType,
)

__all__ = [
    "MAError",
    "MaskError",
    "MaskType",
    "MaskedArray",
    "abs",
    "absolute",
    "add",
    "all",
    "allclose",
    "allequal",
    "alltrue",
    "amax",
    "amin",
    "angle",
    "anom",
    "anomalies",
    "any",
    "append",
    "arange",
    "arccos",
    "arccosh",
    "arcsin",
    "arcsinh",
    "arctan",
    "arctan2",
    "arctanh",
    "argmax",
    "argmin",
    "argsort",
    "around",
    "array",
    "asanyarray",
    "asarray",
    "bitwise_and",
    "bitwise_or",
    "bitwise_xor",
    "bool_",
    "ceil",
    "choose",
    "clip",
    "common_fill_value",
    "compress",
    "compressed",
    "concatenate",
    "conjugate",
    "convolve",
    "copy",
    "correlate",
    "cos",
    "cosh",
    "count",
    "cumprod",
    "cumsum",
    "default_fill_value",
    "diag",
    "diagonal",
    "diff",
    "divide",
    "empty",
    "empty_like",
    "equal",
    "exp",
    "expand_dims",
    "fabs",
    "filled",
    "fix_invalid",
    "flatten_mask",
    "flatten_structured_array",
    "floor",
    "floor_divide",
    "fmod",
    "frombuffer",
    "fromflex",
    "fromfunction",
    "getdata",
    "getmask",
    "getmaskarray",
    "greater",
    "greater_equal",
    "harden_mask",
    "hypot",
    "identity",
    "ids",
    "indices",
    "inner",
    "innerproduct",
    "isMA",
    "isMaskedArray",
    "is_mask",
    "is_masked",
    "isarray",
    "left_shift",
    "less",
    "less_equal",
    "log",
    "log2",
    "log10",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "make_mask",
    "make_mask_descr",
    "make_mask_none",
    "mask_or",
    "masked",
    "masked_array",
    "masked_equal",
    "masked_greater",
    "masked_greater_equal",
    "masked_inside",
    "masked_invalid",
    "masked_less",
    "masked_less_equal",
    "masked_not_equal",
    "masked_object",
    "masked_outside",
    "masked_print_option",
    "masked_singleton",
    "masked_values",
    "masked_where",
    "max",
    "maximum",
    "maximum_fill_value",
    "mean",
    "min",
    "minimum",
    "minimum_fill_value",
    "mod",
    "multiply",
    "mvoid",
    "ndim",
    "negative",
    "nomask",
    "nonzero",
    "not_equal",
    "ones",
    "ones_like",
    "outer",
    "outerproduct",
    "power",
    "prod",
    "product",
    "ptp",
    "put",
    "putmask",
    "ravel",
    "remainder",
    "repeat",
    "reshape",
    "resize",
    "right_shift",
    "round",
    "round_",
    "set_fill_value",
    "shape",
    "sin",
    "sinh",
    "size",
    "soften_mask",
    "sometrue",
    "sort",
    "sqrt",
    "squeeze",
    "std",
    "subtract",
    "sum",
    "swapaxes",
    "take",
    "tan",
    "tanh",
    "trace",
    "transpose",
    "true_divide",
    "var",
    "where",
    "zeros",
    "zeros_like",
]

_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=np.ndarray[Any, Any], covariant=True)
_MArrayT = TypeVar("_MArrayT", bound=MaskedArray[Any, Any])
_UFuncT_co = TypeVar("_UFuncT_co", bound=np.ufunc, default=np.ufunc, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
# TODO: use `Shape` instead of `AnyShape` once python/mypy#19110 is fixed
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.AnyShape, default=_nt.Shape, covariant=True)

_ToInt: TypeAlias = int | _nt.co_integer
_ToTD64: TypeAlias = int | _nt.co_timedelta
_ToFloat: TypeAlias = float | _nt.co_float

_ArangeScalar: TypeAlias = np.integer | np.floating | np.datetime64 | np.timedelta64
_ArangeScalarT = TypeVar("_ArangeScalarT", bound=_ArangeScalar)

_ShapeLike1D: TypeAlias = CanIndex | tuple[CanIndex]
_ShapeLike2D: TypeAlias = tuple[CanIndex, CanIndex]
_ShapeLike3D: TypeAlias = tuple[CanIndex, CanIndex, CanIndex]

_Device: TypeAlias = L["cpu"]

@type_check_only
class _UFuncKwargs(TypedDict, total=False):
    where: _nt.ToBool_nd | None
    order: _OrderKACF
    subok: bool
    signature: str | tuple[str | None, ...]
    casting: np._CastingKind

@type_check_only
class _CanArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

###

MaskType: Final[type[np.bool_]] = ...
nomask: np.bool_[L[False]] = ...
masked_print_option: Final[_MaskedPrintOption] = ...

###

class MaskedArrayFutureWarning(FutureWarning): ...
class MAError(Exception): ...
class MaskError(MAError): ...

###

@type_check_only
class _DomainBase:
    @overload
    def __call__(self, /, x: _nt.ToGeneric_0d) -> np.bool_: ...
    @overload
    def __call__(self, /, x: _nt.ToGeneric_1nd) -> _nt.Array[np.bool_]: ...

class _DomainCheckInterval(_DomainBase):
    a: Final[float]
    b: Final[float]
    def __init__(self, /, a: float, b: float) -> None: ...

class _DomainTan(_DomainBase):
    eps: Final[float]
    def __init__(self, /, eps: float) -> None: ...

class _DomainGreater(_DomainBase):
    critical_value: Final[float]
    def __init__(self, /, critical_value: float) -> None: ...

class _DomainGreaterEqual(_DomainBase):
    critical_value: Final[float]
    def __init__(self, /, critical_value: float) -> None: ...

class _DomainSafeDivide:
    tolerance: float
    def __init__(self, /, tolerance: float | None = None) -> None: ...
    def __call__(self, /, a: _nt.ToGeneric_nd, b: _nt.ToGeneric_nd) -> _nt.Array[Incomplete]: ...

###

class _MaskedUFunc(Generic[_UFuncT_co]):
    f: _UFuncT_co
    __name__: str
    __qualname__: str
    def __init__(self, /, ufunc: _UFuncT_co) -> None: ...

class _MaskedUnaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    __doc__: str
    domain: _DomainBase
    fill: Incomplete
    def __init__(self, /, mufunc: _UFuncT_co, fill: Incomplete = 0, domain: _DomainBase | None = None) -> None: ...
    def __call__(self, /, a: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

class _MaskedBinaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    __doc__: str
    fillx: Incomplete
    filly: Incomplete
    def __init__(self, mbfunc: _UFuncT_co, fillx: Incomplete = 0, filly: Incomplete = 0) -> None: ...
    def __call__(self, /, a: Incomplete, b: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

    #
    def reduce(self, target: Incomplete, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    def outer(self, a: Incomplete, b: Incomplete) -> MaskedArray: ...
    def accumulate(self, target: Incomplete, axis: Incomplete = ...) -> MaskedArray: ...

class _DomainedBinaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    __doc__: str
    domain: _DomainBase
    fillx: Incomplete
    filly: Incomplete
    def __init__(
        self, /, dbfunc: _UFuncT_co, domain: _DomainBase, fillx: Incomplete = 0, filly: Incomplete = 0
    ) -> None: ...
    def __call__(self, /, a: Incomplete, b: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

class _extrema_operation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    __doc__: str
    compare: Incomplete
    fill_value_func: Incomplete
    def __init__(self, ufunc: _UFuncT_co, compare: Incomplete, fill_value: Incomplete) -> None: ...
    def __call__(self, /, a: Incomplete, b: Incomplete) -> Incomplete: ...
    def reduce(self, /, target: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
    def outer(self, /, a: Incomplete, b: Incomplete) -> MaskedArray: ...

###

class _MaskedPrintOption:
    def __init__(self, /, display: Incomplete) -> None: ...
    def display(self) -> Incomplete: ...
    def set_display(self, /, s: Incomplete) -> None: ...
    def enabled(self) -> bool: ...
    def enable(self, /, shrink: Incomplete = 1) -> None: ...

class MaskedIterator:
    ma: Incomplete
    dataiter: Incomplete
    maskiter: Incomplete
    def __init__(self, /, ma: Incomplete) -> None: ...
    def __iter__(self) -> Incomplete: ...
    def __getitem__(self, indx: Incomplete, /) -> Incomplete: ...
    def __setitem__(self, index: Incomplete, value: Incomplete, /) -> None: ...
    def __next__(self) -> Incomplete: ...

class MaskedArray(np.ndarray[_ShapeT_co, _DTypeT_co]):
    __array_priority__: ClassVar[float] = 15  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @property
    def mask(self) -> Incomplete: ...
    @mask.setter
    def mask(self, value: Incomplete, /) -> None: ...

    #
    @property
    def recordmask(self) -> _nt.Array[np.bool_]: ...
    @recordmask.setter
    def recordmask(self, mask: Never, /) -> None: ...

    #
    @property
    def hardmask(self) -> Incomplete: ...
    @property
    def sharedmask(self) -> Incomplete: ...
    @property
    def baseclass(self) -> Incomplete: ...

    #
    @property  # type: ignore[explicit-override]
    @override
    def flat(self) -> Incomplete: ...
    @flat.setter
    def flat(self, value: Incomplete) -> Incomplete: ...

    #
    @property
    @override
    def data(self) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def get_fill_value(self) -> Incomplete: ...
    def set_fill_value(self, /, value: Incomplete = None) -> Incomplete: ...
    @property
    def fill_value(self) -> Incomplete: ...
    @fill_value.setter
    def fill_value(self, value: Incomplete = None, /) -> Incomplete: ...

    #
    @property  # type: ignore[misc]
    @override
    def imag(self) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    def get_imag(self) -> Incomplete: ...

    #
    @property  # type: ignore[misc]
    @override
    def real(self) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    def get_real(self) -> Incomplete: ...

    #
    @property
    @override
    def mT(self) -> Self: ...
    @property
    @override
    def T(self) -> Self: ...

    #
    def __new__(
        cls,
        data: Incomplete | None = None,
        mask: Incomplete = ...,
        dtype: Incomplete = None,
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: Incomplete = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderACF | None = None,
    ) -> Self: ...

    #
    @override
    def __array_finalize__(self, /, obj: Incomplete) -> None: ...
    @override
    def __array_wrap__(
        self, /, obj: Incomplete, context: Incomplete | None = None, return_scalar: bool = False
    ) -> Incomplete: ...
    def __setmask__(self, /, mask: Incomplete, copy: bool = False) -> None: ...

    #
    @override
    def __getitem__(self, indx: Incomplete, /) -> Incomplete: ...
    @override
    def __setitem__(self, indx: Incomplete, value: Incomplete, /) -> None: ...

    #
    @override
    def __eq__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __ne__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __ge__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __gt__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __le__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __lt__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __add__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __radd__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __sub__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __rsub__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __mul__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __rmul__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __truediv__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __rtruediv__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __floordiv__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __rfloordiv__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __pow__(self, other: Incomplete, /) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __rpow__(self, other: Incomplete, /) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __iadd__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    @override
    def __isub__(self, other: Incomplete, /) -> Self: ...
    @override
    def __imul__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    @override
    def __ifloordiv__(self, other: Incomplete, /) -> Self: ...
    @override
    def __itruediv__(self, other: Incomplete, /) -> Self: ...
    @override
    def __ipow__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]

    #
    @override
    def __reduce__(self) -> Incomplete: ...
    @override
    def __deepcopy__(self, /, memo: Incomplete = ...) -> Self: ...

    #
    @override
    def view(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, /, dtype: Incomplete = None, type: Incomplete = None, fill_value: Incomplete = None
    ) -> Incomplete: ...
    def harden_mask(self) -> Incomplete: ...
    def soften_mask(self) -> Incomplete: ...
    def unshare_mask(self) -> Incomplete: ...
    def shrink_mask(self) -> Incomplete: ...
    def filled(self, /, fill_value: Incomplete = None) -> Incomplete: ...
    def compressed(self) -> Incomplete: ...
    @override
    def compress(self, /, condition: Incomplete, axis: Incomplete = None, out: Incomplete = None) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def count(self, axis: Incomplete = None, keepdims: Incomplete = ...) -> Incomplete: ...
    @override
    def ravel(self, order: Incomplete = ...) -> Incomplete: ...
    @override
    def reshape(self, *s: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    @override
    def resize(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, newshape: Incomplete, refcheck: Incomplete = ..., order: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def put(self, indices: Incomplete, values: Incomplete, mode: Incomplete = ...) -> Incomplete: ...
    def ids(self) -> Incomplete: ...
    def iscontiguous(self) -> Incomplete: ...
    @override
    def all(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def any(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def trace(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        offset: Incomplete = ...,
        axis1: Incomplete = ...,
        axis2: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
    ) -> Incomplete: ...
    @override
    def dot(self, b: Incomplete, out: Incomplete = ..., strict: Incomplete = ...) -> Incomplete: ...

    #
    @override
    def sum(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def cumsum(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def prod(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    product = prod
    @override
    def cumprod(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def mean(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    def anom(self, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    @override
    def var(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: float = 0,
        keepdims: Incomplete = ...,
        mean: Incomplete = ...,
    ) -> Incomplete: ...
    @override
    def std(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: float = 0,
        keepdims: Incomplete = ...,
        mean: Incomplete = ...,
    ) -> Incomplete: ...

    #
    @override
    def round(self, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def sort(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = -1,
        kind: Incomplete | None = None,
        order: Incomplete | None = None,
        endwith: bool = True,
        fill_value: Incomplete | None = None,
        *,
        stable: bool = False,
    ) -> Incomplete: ...
    @override
    def argsort(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        kind: Incomplete | None = None,
        order: Incomplete | None = None,
        endwith: bool = True,
        fill_value: Incomplete | None = None,
        *,
        stable: bool = False,
    ) -> Incomplete: ...

    #
    @override
    def min(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def argmin(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., fill_value: Incomplete = ..., out: Incomplete = ..., *, keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def max(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def argmax(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., fill_value: Incomplete = ..., out: Incomplete = ..., *, keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def ptp(  # pyright: ignore[reportIncompatibleVariableOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def partition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    @override
    def argpartition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

    #
    @override
    def take(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, /, indices: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., mode: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def copy(self, /, order: _OrderKACF = "C") -> Self: ...

    #
    diagonal: Incomplete
    flatten: Incomplete
    repeat: Incomplete
    squeeze: Incomplete
    swapaxes: Incomplete
    transpose: Incomplete

    #
    def toflex(self) -> Incomplete: ...
    def torecords(self) -> Incomplete: ...
    @override
    def tolist(self, fill_value: Incomplete | None = None) -> Incomplete: ...
    @override
    def tobytes(self, /, fill_value: Incomplete | None = None, order: _OrderKACF = "C") -> bytes: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tofile(self, /, fid: Incomplete, sep: str = "", format: str = "%s") -> Incomplete: ...

class mvoid(MaskedArray[_ShapeT_co, _DTypeT_co]):
    def __new__(
        self,  # noqa: PLW0211
        data: Incomplete,
        mask: Incomplete = ...,
        dtype: Incomplete = ...,
        fill_value: Incomplete = ...,
        hardmask: Incomplete = ...,
        copy: bool = ...,
        subok: bool = ...,
    ) -> Self: ...
    @override
    def __getitem__(self, indx: Incomplete, /) -> Incomplete: ...
    @override
    def __setitem__(self, indx: Incomplete, value: Incomplete, /) -> None: ...
    @override
    def __iter__(self) -> Incomplete: ...
    @override
    def __len__(self) -> int: ...

    #
    @override
    def filled(self, fill_value: Incomplete = ...) -> Incomplete: ...
    @override
    def tolist(self) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

# 0D float64 array
class MaskedConstant(MaskedArray[_nt.Rank0, np.dtype[np.float64]]):
    def __new__(cls) -> Self: ...
    @override
    def __array_wrap__(  # type: ignore[override]
        self, /, obj: Incomplete, context: Incomplete | None = None, return_scalar: bool = False
    ) -> _nt.MArray0D[np.float64]: ...
    @override
    def __format__(self, format_spec: str, /) -> str: ...

    # no-ops
    @override
    def __iadd__(self, other: object, /) -> Self: ...  # type: ignore[override]
    @override
    def __isub__(self, other: object, /) -> Self: ...  # type: ignore[override]
    @override
    def __imul__(self, other: object, /) -> Self: ...  # type: ignore[override]
    @override
    def __ifloordiv__(self, other: object, /) -> Self: ...  # type: ignore[override]
    @override
    def __itruediv__(self, other: object, /) -> Self: ...  # type: ignore[override]
    @override
    def __ipow__(self, other: object, /) -> Self: ...  # type: ignore[override]

    #
    @override
    def __reduce__(self) -> tuple[type[Self], tuple[()]]: ...
    @override
    def __copy__(self) -> Self: ...
    @override
    def __deepcopy__(self, /, memo: object) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def copy(self, /, *args: object, **kwargs: object) -> Incomplete: ...

# TODO: sync with upstream
class _frommethod:
    __name__: str
    __doc__: str
    reversed: Incomplete
    def __init__(self, methodname: Incomplete, reversed: Incomplete = ...) -> None: ...
    def __call__(self, a: Incomplete, *args: Incomplete, **params: Incomplete) -> Incomplete: ...
    def getdoc(self) -> Incomplete: ...

# TODO: sync with `MaskedArray` methods
def harden_mask(a: _MArrayT) -> _MArrayT: ...
def soften_mask(a: _MArrayT) -> _MArrayT: ...
def shrink_mask(a: _MArrayT) -> _MArrayT: ...
def ids(a: ArrayLike) -> tuple[int, int]: ...

# keep in sync with `ndarray.nonzero`
def nonzero(a: ArrayLike) -> tuple[_nt.Array1D[np.intp], ...]: ...

# TODO: sync with `MaskedArray.ravel`
@overload
def ravel(a: np.ndarray[Any, _DTypeT], order: _OrderKACF = "C") -> MaskedArray[_nt.Rank1, _DTypeT]: ...
@overload
def ravel(a: _ArrayLike[_ScalarT], order: _OrderKACF = "C") -> _nt.MArray1D[_ScalarT]: ...
@overload
def ravel(a: ArrayLike, order: _OrderKACF = "C") -> _nt.MArray1D[Incomplete]: ...

# keep roughly in sync with `lib._function_base_impl.copy`
@overload
def copy(a: _MArrayT, order: _OrderKACF = "C") -> _MArrayT: ...
@overload
def copy(a: np.ndarray[_ShapeT, _DTypeT], order: _OrderKACF = "C") -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload
def copy(a: _ArrayLike[_ScalarT], order: _OrderKACF = "C") -> _nt.MArray[_ScalarT]: ...
@overload
def copy(a: ArrayLike, order: _OrderKACF = "C") -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.diagonal`
@overload
def diagonal(
    a: _nt._ToArray_nd[_ScalarT], offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
) -> _nt.MArray[_ScalarT]: ...
@overload
def diagonal(
    a: ArrayLike, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.repeat`
@overload
def repeat(
    a: _nt._ToArray_nd[_ScalarT], repeats: _nt.CoInteger_nd, axis: CanIndex | None = None
) -> _nt.MArray[_ScalarT]: ...
@overload
def repeat(a: ArrayLike, repeats: _nt.CoInteger_nd, axis: CanIndex | None = None) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.swapaxes`
@overload
def swapaxes(a: _nt._ToArray_nd[_ScalarT], axis1: CanIndex, axis2: CanIndex) -> _nt.MArray[_ScalarT]: ...
@overload
def swapaxes(a: ArrayLike, axis1: CanIndex, axis2: CanIndex) -> _nt.MArray[Incomplete]: ...

# TODO: roughly sync with `MaskedArray.anom`
# The `MaskedArray.anom` definition is specific to `MaskedArray`, so we need
# additional overloads to cover the array-like input here.
@overload  # a: MaskedArray, dtype=None
def anom(a: _MArrayT, axis: CanIndex | None = None, dtype: None = None) -> _MArrayT: ...
@overload  # a: array-like, dtype=None
def anom(a: _ArrayLike[_ScalarT], axis: CanIndex | None = None, dtype: None = None) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: dtype-like (positional)
def anom(a: ArrayLike, axis: CanIndex | None, dtype: _DTypeLike[_ScalarT]) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: dtype-like (keyword)
def anom(a: ArrayLike, axis: CanIndex | None = None, *, dtype: _DTypeLike[_ScalarT]) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: unknown dtype-like (positional)
def anom(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike) -> _nt.MArray[Incomplete]: ...
@overload  # a: unknown array-like, dtype: unknown dtype-like (keyword)
def anom(a: ArrayLike, axis: CanIndex | None = None, *, dtype: DTypeLike) -> _nt.MArray[Incomplete]: ...

anomalies = anom

# TODO: sync with `MaskedArray.all`
# Keep in sync with `any`
@overload
def all(a: ArrayLike, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> np.bool: ...
@overload
def all(a: ArrayLike, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[np.bool]: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]
) -> _nt.MArray[np.bool]: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
) -> np.bool | _nt.MArray[np.bool]: ...
@overload
def all(a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.any`
# Keep in sync with `all`
@overload
def any(a: ArrayLike, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> np.bool: ...
@overload
def any(a: ArrayLike, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[np.bool]: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]
) -> _nt.MArray[np.bool]: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
) -> np.bool | _nt.MArray[np.bool]: ...
@overload
def any(a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.compress`
# NOTE: The `MaskedArray.compress` definition uses its `DTypeT_co` type parameter,
# which wouldn't work here for array-like inputs, so we need additional overloads.
@overload
def compress(
    condition: _nt.ToBool_nd, a: _ArrayLike[_ScalarT], axis: None = None, out: None = None
) -> _nt.MArray1D[_ScalarT]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: _ArrayLike[_ScalarT], axis: _ShapeLike, out: None = None
) -> _nt.MArray[_ScalarT]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: ArrayLike, axis: None = None, out: None = None
) -> _nt.MArray1D[Incomplete]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

# TODO: sync with `MaskedArray.cumsum`
# Keep in sync with `cumprod`
@overload  # out: None (default)
def cumsum(
    a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload  # out: ndarray (positional)
def cumsum(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload  # out: ndarray (kwarg)
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

# TODO: sync with `MaskedArray.cumprod`
# Keep in sync with `cumsum`
@overload  # out: None (default)
def cumprod(
    a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload  # out: ndarray (positional)
def cumprod(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload  # out: ndarray (kwarg)
def cumprod(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

mean: _frommethod
sum: _frommethod

prod: _frommethod
product: _frommethod

trace: _frommethod

std: _frommethod
var: _frommethod

count: _frommethod

argmin: _frommethod
argmax: _frommethod

minimum: _extrema_operation
maximum: _extrema_operation

#
def array(
    data: Incomplete,
    dtype: Incomplete = ...,
    copy: Incomplete = ...,
    order: Incomplete = ...,
    mask: Incomplete = ...,
    fill_value: Incomplete = ...,
    keep_mask: Incomplete = ...,
    hard_mask: Incomplete = ...,
    shrink: Incomplete = ...,
    subok: Incomplete = ...,
    ndmin: Incomplete = ...,
) -> Incomplete: ...

#
@overload
def min(
    obj: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: L[False] | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def min(
    obj: ArrayLike,
    axis: None,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

#
def max(
    obj: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    fill_value: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...
def ptp(
    obj: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    fill_value: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...

#
def take(
    a: Incomplete, indices: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., mode: Incomplete = ...
) -> Incomplete: ...
def power(a: Incomplete, b: Incomplete, third: Incomplete = ...) -> Incomplete: ...
def argsort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
    *,
    stable: Incomplete = ...,
) -> Incomplete: ...
def sort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
    *,
    stable: Incomplete = ...,
) -> Incomplete: ...
def compressed(x: Incomplete) -> Incomplete: ...
def concatenate(arrays: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def diag(v: Incomplete, k: Incomplete = ...) -> Incomplete: ...
def left_shift(a: Incomplete, n: Incomplete) -> Incomplete: ...
def right_shift(a: Incomplete, n: Incomplete) -> Incomplete: ...
def put(a: Incomplete, indices: Incomplete, values: Incomplete, mode: Incomplete = ...) -> Incomplete: ...
def putmask(a: Incomplete, mask: Incomplete, values: Incomplete) -> Incomplete: ...
def transpose(a: Incomplete, axes: Incomplete = ...) -> Incomplete: ...
def reshape(a: Incomplete, new_shape: Incomplete, order: Incomplete = ...) -> Incomplete: ...
def resize(x: Incomplete, new_shape: Incomplete) -> Incomplete: ...
def ndim(obj: Incomplete) -> Incomplete: ...
def shape(obj: Incomplete) -> Incomplete: ...
def size(obj: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def diff(
    a: Incomplete, /, n: Incomplete = ..., axis: Incomplete = ..., prepend: Incomplete = ..., append: Incomplete = ...
) -> Incomplete: ...
def where(condition: Incomplete, x: Incomplete = ..., y: Incomplete = ...) -> Incomplete: ...
def choose(indices: Incomplete, choices: Incomplete, out: Incomplete = ..., mode: Incomplete = ...) -> Incomplete: ...
def round_(a: Incomplete, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
def inner(a: Incomplete, b: Incomplete) -> Incomplete: ...
def outer(a: Incomplete, b: Incomplete) -> Incomplete: ...
def correlate(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def convolve(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def allequal(a: Incomplete, b: Incomplete, fill_value: Incomplete = ...) -> Incomplete: ...
def allclose(
    a: Incomplete, b: Incomplete, masked_equal: Incomplete = ..., rtol: Incomplete = ..., atol: Incomplete = ...
) -> Incomplete: ...
def asarray(a: Incomplete, dtype: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...
def asanyarray(a: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def fromflex(fxarray: Incomplete) -> Incomplete: ...
def make_mask_descr(ndtype: Incomplete) -> Incomplete: ...
def getmask(a: Incomplete) -> Incomplete: ...
def getmaskarray(arr: Incomplete) -> Incomplete: ...
def is_mask(m: Incomplete) -> Incomplete: ...
def make_mask(
    m: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ..., dtype: Incomplete = ...
) -> Incomplete: ...
def make_mask_none(newshape: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def mask_or(m1: Incomplete, m2: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ...) -> Incomplete: ...
def flatten_mask(mask: Incomplete) -> Incomplete: ...
def masked_where(condition: Incomplete, a: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_greater(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_greater_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_less(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_less_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_not_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_inside(x: Incomplete, v1: Incomplete, v2: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_outside(x: Incomplete, v1: Incomplete, v2: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_object(x: Incomplete, value: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ...) -> Incomplete: ...
def masked_values(
    x: Incomplete,
    value: Incomplete,
    rtol: Incomplete = ...,
    atol: Incomplete = ...,
    copy: Incomplete = ...,
    shrink: Incomplete = ...,
) -> Incomplete: ...
def masked_invalid(a: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def flatten_structured_array(a: Incomplete) -> Incomplete: ...
def append(a: Incomplete, b: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def dot(a: Incomplete, b: Incomplete, strict: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
def default_fill_value(obj: Incomplete) -> Incomplete: ...
def minimum_fill_value(obj: Incomplete) -> Incomplete: ...
def maximum_fill_value(obj: Incomplete) -> Incomplete: ...
def set_fill_value(a: Incomplete, fill_value: Incomplete) -> Incomplete: ...
def common_fill_value(a: Incomplete, b: Incomplete) -> Incomplete: ...
def filled(a: Incomplete, fill_value: Incomplete | None = None) -> Incomplete: ...
def getdata(a: Incomplete, subok: bool = True) -> Incomplete: ...
def fix_invalid(
    a: Incomplete, mask: Incomplete = ..., copy: bool = True, fill_value: Incomplete | None = None
) -> Incomplete: ...
def is_masked(x: Incomplete) -> Incomplete: ...
def isMaskedArray(x: Incomplete) -> Incomplete: ...

#
masked: Final[MaskedConstant] = ...
masked_singleton: Final[MaskedConstant] = ...
masked_array = MaskedArray

#
isarray = isMaskedArray
isMA = isMaskedArray
round = round_
innerproduct = inner
outerproduct = outer
get_mask = getmask
get_data = getdata

exp: _MaskedUnaryOperation
conjugate: _MaskedUnaryOperation
sin: _MaskedUnaryOperation
cos: _MaskedUnaryOperation
arctan: _MaskedUnaryOperation
arcsinh: _MaskedUnaryOperation
sinh: _MaskedUnaryOperation
cosh: _MaskedUnaryOperation
tanh: _MaskedUnaryOperation
abs: _MaskedUnaryOperation
absolute: _MaskedUnaryOperation
angle: _MaskedUnaryOperation
fabs: _MaskedUnaryOperation
negative: _MaskedUnaryOperation
floor: _MaskedUnaryOperation
ceil: _MaskedUnaryOperation
around: _MaskedUnaryOperation
logical_not: _MaskedUnaryOperation
sqrt: _MaskedUnaryOperation
log: _MaskedUnaryOperation
log2: _MaskedUnaryOperation
log10: _MaskedUnaryOperation
tan: _MaskedUnaryOperation
arcsin: _MaskedUnaryOperation
arccos: _MaskedUnaryOperation
arccosh: _MaskedUnaryOperation
arctanh: _MaskedUnaryOperation

add: _MaskedBinaryOperation
subtract: _MaskedBinaryOperation
multiply: _MaskedBinaryOperation
arctan2: _MaskedBinaryOperation
equal: _MaskedBinaryOperation
not_equal: _MaskedBinaryOperation
less_equal: _MaskedBinaryOperation
greater_equal: _MaskedBinaryOperation
less: _MaskedBinaryOperation
greater: _MaskedBinaryOperation
logical_and: _MaskedBinaryOperation

def alltrue(
    target: _nt.ToGeneric_nd, axis: CanIndex | None = 0, dtype: _nt.ToDTypeBool | None = None
) -> Incomplete: ...

logical_or: _MaskedBinaryOperation

def sometrue(
    target: _nt.ToGeneric_nd, axis: CanIndex | None = 0, dtype: _nt.ToDTypeBool | None = None
) -> Incomplete: ...

logical_xor: _MaskedBinaryOperation
bitwise_and: _MaskedBinaryOperation
bitwise_or: _MaskedBinaryOperation
bitwise_xor: _MaskedBinaryOperation
hypot: _MaskedBinaryOperation

divide: _DomainedBinaryOperation
true_divide: _DomainedBinaryOperation
floor_divide: _DomainedBinaryOperation
remainder: _DomainedBinaryOperation
fmod: _DomainedBinaryOperation
mod: _DomainedBinaryOperation

# internal wrapper functions for the functions below
def _convert2ma(
    funcname: str, np_ret: str, np_ma_ret: str, params: dict[str, Any] | None = None
) -> Callable[..., Any]: ...

# keep in sync with `_core.multiarray.arange`
@overload  # (int-like, int-like?, int-like?)
def arange(
    start_or_stop: _ToInt,
    /,
    stop: _ToInt | None = None,
    step: _ToInt | None = 1,
    *,
    dtype: _nt.ToDTypeInt64 | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: int | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.int64]: ...
@overload  # (float, float-like?, float-like?)
def arange(
    start_or_stop: float | np.floating,
    /,
    stop: _ToFloat | None = None,
    step: _ToFloat | None = 1,
    *,
    dtype: type[float] | _DTypeLike[np.float64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64 | Any]: ...
@overload  # (float-like, float, float-like?)
def arange(
    start_or_stop: _ToFloat,
    /,
    stop: float | np.floating,
    step: _ToFloat | None = 1,
    *,
    dtype: type[float] | _DTypeLike[np.float64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64 | Any]: ...
@overload  # (timedelta, timedelta-like?, timedelta-like?)
def arange(
    start_or_stop: np.timedelta64,
    /,
    stop: _ToTD64 | None = None,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.timedelta64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: _ToTD64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.timedelta64[Incomplete]]: ...
@overload  # (timedelta-like, timedelta, timedelta-like?)
def arange(
    start_or_stop: _ToTD64,
    /,
    stop: np.timedelta64,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.timedelta64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: _ToTD64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.timedelta64[Incomplete]]: ...
@overload  # (datetime, datetime, timedelta-like) (requires both start and stop)
def arange(
    start_or_stop: np.datetime64,
    /,
    stop: np.datetime64,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.datetime64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: np.datetime64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.datetime64[Incomplete]]: ...
@overload  # dtype=<known>
def arange(
    start_or_stop: _ArangeScalar | float,
    /,
    stop: _ArangeScalar | float | None = None,
    step: _ArangeScalar | float | None = 1,
    *,
    dtype: _DTypeLike[_ArangeScalarT],
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[_ArangeScalarT]: ...
@overload  # dtype=<unknown>
def arange(
    start_or_stop: _ArangeScalar | float,
    /,
    stop: _ArangeScalar | float | None = None,
    step: _ArangeScalar | float | None = 1,
    *,
    dtype: DTypeLike | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[Incomplete]: ...

# based on `_core.fromnumeric.clip`
@overload
def clip(
    a: _ScalarT,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _ScalarT: ...
@overload
def clip(
    a: _nt.Array[_ScalarT],
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _nt.MArray[_ScalarT]: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | None,
    a_max: ArrayLike | None,
    out: _MArrayT,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _MArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    *,
    out: _MArrayT,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _MArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> Incomplete: ...

# keep in sync with `_core._multiarray_umath.empty`
@overload  # 1d shape, default dtype (float64)
def empty(
    shape: _ShapeLike1D,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64]: ...
@overload  # 1d shape, known dtype
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def empty(
    shape: _ShapeLike1D,
    dtype: DTypeLike = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[Incomplete]: ...
@overload  # known shape, default dtype (float64)
def empty(
    shape: _ShapeT,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.float64, _ShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def empty(
    shape: _ShapeT,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def empty(
    shape: _ShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # known shape, unknown scalar-type
def empty(
    shape: _ShapeT,
    dtype: DTypeLike = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete, _ShapeT]: ...
@overload  # unknown shape, default dtype
def empty(
    shape: _ShapeLike,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.float64]: ...
@overload  # unknown shape, known dtype
def empty(
    shape: _ShapeLike,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[Incomplete, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def empty(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def empty(
    shape: _ShapeLike,
    dtype: DTypeLike = ...,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core._multiarray_umath.empty_like`
@overload  # known array, subok=True
def empty_like(
    prototype: _MArrayT,
    /,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _MArrayT: ...
@overload  # array-like with known shape and type
def empty_like(
    prototype: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    /,
    dtype: _DTypeT | _HasDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.bool_],
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.bool_]: ...
@overload  # bool 0d array-like
def empty_like(
    prototype: _nt.ToBool_0d,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.bool_]: ...
@overload  # bool 1d array-like
def empty_like(
    prototype: _nt.ToBool_1ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.bool_]: ...
@overload  # bool 2d array-like
def empty_like(
    prototype: _nt.ToBool_2ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.bool_]: ...
@overload  # bool 3d array-like
def empty_like(
    prototype: _nt.ToBool_3ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.bool_]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(  # type: ignore[overload-overlap]  # python/mypy#19908
    prototype: _nt._ToArray_nnd[np.intp],
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.intp]: ...
@overload  # int 0d array-like
def empty_like(
    prototype: _nt.ToInt_0d,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.intp]: ...
@overload  # int 1d array-like
def empty_like(
    prototype: _nt.ToInt_1ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.intp]: ...
@overload  # int 2d array-like
def empty_like(
    prototype: _nt.ToInt_2ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.intp]: ...
@overload  # int 3d array-like
def empty_like(
    prototype: _nt.ToInt_3ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.intp]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(  # type: ignore[overload-overlap]  # python/mypy#19908
    prototype: _nt._ToArray_nnd[np.float64],
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.float64]: ...
@overload  # float 0d array-like
def empty_like(
    prototype: _nt.ToFloat64_0d,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.float64]: ...
@overload  # float 1d array-like
def empty_like(
    prototype: _nt.ToFloat64_1ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.float64]: ...
@overload  # float 2d array-like
def empty_like(
    prototype: _nt.ToFloat64_2ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.float64]: ...
@overload  # float 3d array-like
def empty_like(
    prototype: _nt.ToFloat64_3ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.float64]: ...
@overload  # complex 0d array-like
def empty_like(
    prototype: _nt.ToComplex128_0d,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.complex128]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.complex128],
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.complex128]: ...
@overload  # complex 1d array-like
def empty_like(
    prototype: _nt.ToComplex128_1ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.complex128]: ...
@overload  # complex 2d array-like
def empty_like(
    prototype: _nt.ToComplex128_2ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.complex128]: ...
@overload  # complex 3d array-like
def empty_like(
    prototype: _nt.ToComplex128_3ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def empty_like(
    prototype: _ArrayLike[_ScalarT],
    /,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def empty_like(
    prototype: _ArrayLike[_ScalarT],
    /,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload  # given shape, given dtype
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> MaskedArray[Incomplete, _DTypeT]: ...
@overload  # given shape, given scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # unknown shape, given scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload  # bool array-like
def empty_like(
    prototype: _nt.ToBool_nd,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.bool_]: ...
@overload  # int array-like
def empty_like(
    prototype: _nt.ToInt_nd,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.intp]: ...
@overload  # float array-like
def empty_like(
    prototype: _nt.ToFloat64_nd,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.float64]: ...
@overload  # complex array-like
def empty_like(
    prototype: _nt.ToComplex128_nd,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[Incomplete, _ShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[Incomplete]: ...

# This is a bit of a hack to avoid having to duplicate all those `empty` overloads for
# `ones` and `zeros`, that relies on the fact that empty/zeros/ones have identical
# type signatures, but may cause some type-checkers to report incorrect names in case
# of user errors. Mypy and Pyright seem to handle this just fine.
ones = empty
ones_like = empty_like
zeros = empty
zeros_like = empty_like

# keep in sync with `_core._multiarray_umath.frombuffer`
@overload
def frombuffer(
    buffer: Buffer, *, count: CanIndex = -1, offset: CanIndex = 0, like: _CanArrayFunc | None = None
) -> _nt.MArray[np.float64]: ...
@overload
def frombuffer(
    buffer: Buffer,
    dtype: _DTypeLike[_ScalarT],
    count: CanIndex = -1,
    offset: CanIndex = 0,
    *,
    like: _CanArrayFunc | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload
def frombuffer(
    buffer: Buffer, dtype: DTypeLike, count: CanIndex = -1, offset: CanIndex = 0, *, like: _CanArrayFunc | None = None
) -> _nt.MArray[Incomplete]: ...

# keep roughly in sync with `_core.numeric.fromfunction`
def fromfunction(
    function: Callable[..., np.ndarray[_ShapeT, _DTypeT]],
    shape: Sequence[int],
    *,
    dtype: DTypeLike | None = ...,  # = float
    like: _CanArrayFunc | None = None,
    **kwargs: object,
) -> MaskedArray[_ShapeT, _DTypeT]: ...

# keep roughly in sync with `_core.numeric.identity`
@overload
def identity(
    n: int,
    dtype: _nt.ToDTypeFloat64 | None = None,
    *,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[np.float64]: ...
@overload
def identity(
    n: int,
    dtype: _DTypeLike[_ScalarT],
    *,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[_ScalarT]: ...
@overload
def identity(
    n: int,
    dtype: DTypeLike | None = None,
    *,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[Incomplete]: ...

# keep roughly in sync with `_core.numeric.indices`
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt] = ...,
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.intp]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt],
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt] = ...,
    *,
    sparse: L[True],
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: _DTypeLike[_ScalarT],
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: _DTypeLike[_ScalarT],
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[_ScalarT], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike = ...,
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike,
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[Incomplete], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike = ...,
    *,
    sparse: L[True],
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[Incomplete], ...]: ...

# keep roughly in sync with `_core.fromnumeric.squeeze`
@overload  # workaround for microsoft/pyright#10232
def squeeze(
    a: _ScalarT, axis: _ShapeLike | None = None, *, fill_value: complex | None = None, hardmask: bool = False
) -> _nt.MArray0D[_ScalarT]: ...
@overload  # workaround for microsoft/pyright#10232
def squeeze(
    a: _nt._ToArray_nnd[_ScalarT],
    axis: _ShapeLike | None = None,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def squeeze(
    a: _nt._ToArray_nd[_ScalarT],
    axis: _ShapeLike | None = None,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def squeeze(
    a: ArrayLike, axis: _ShapeLike | None = None, *, fill_value: complex | None = None, hardmask: bool = False
) -> _nt.MArray[Incomplete]: ...
