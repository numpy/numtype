from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, ClassVar, Final, Generic, Literal as L, type_check_only
from typing_extensions import Never, Self, TypeVar, overload

import numpy as np
from _numtype import Array, ToGeneric_0d, ToGeneric_1nd, ToGeneric_nd
from numpy import _OrderACF, _OrderKACF, amax, amin, angle, bool_, clip, expand_dims, indices, squeeze  # noqa: ICN003

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

_UFuncT_co = TypeVar("_UFuncT_co", bound=np.ufunc, default=np.ufunc, covariant=True)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=tuple[int, ...], covariant=True)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype[Any])
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[Any], default=np.dtype[Any], covariant=True)

###

MaskType: Final[type[np.bool]] = ...
nomask: np.bool[L[False]] = ...
masked_print_option: Final[_MaskedPrintOption] = ...

###

class MaskedArrayFutureWarning(FutureWarning): ...
class MAError(Exception): ...
class MaskError(MAError): ...

###

@type_check_only
class _DomainBase:
    @overload
    def __call__(self, /, x: ToGeneric_0d) -> np.bool: ...
    @overload
    def __call__(self, /, x: ToGeneric_1nd) -> Array[np.bool]: ...

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
    def __call__(self, /, a: ToGeneric_nd, b: ToGeneric_nd) -> Array[Incomplete]: ...

###

class _MaskedUFunc(Generic[_UFuncT_co]):
    f: _UFuncT_co
    __doc__: str
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
    def __init__(self, /, dbfunc: _UFuncT_co, domain: _DomainBase, fillx: Incomplete = 0, filly: Incomplete = 0) -> None: ...
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
    def shape(self) -> _ShapeT_co: ...
    @shape.setter
    def shape(self: MaskedArray[_ShapeT], shape: _ShapeT, /) -> None: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @property
    def dtype(self) -> _DTypeT_co: ...
    @dtype.setter
    def dtype(self: MaskedArray[Any, _DTypeT], dtype: _DTypeT, /) -> None: ...

    #
    @property
    def mask(self) -> Incomplete: ...
    @mask.setter
    def mask(self, value: Incomplete, /) -> None: ...

    #
    @property
    def recordmask(self) -> Array[np.bool]: ...
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
    @property
    def flat(self) -> Incomplete: ...
    @flat.setter
    def flat(self, value: Incomplete) -> Incomplete: ...

    #
    @property
    def data(self) -> Incomplete: ...
    @data.setter
    def data(self, value: Incomplete, /) -> Incomplete: ...

    #
    def get_fill_value(self) -> Incomplete: ...
    def set_fill_value(self, /, value: Incomplete = None) -> Incomplete: ...
    @property
    def fill_value(self) -> Incomplete: ...
    @fill_value.setter
    def fill_value(self, value: Incomplete = None, /) -> Incomplete: ...

    #
    @property  # type: ignore[misc]
    def imag(self) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    def get_imag(self) -> Incomplete: ...

    #
    @property  # type: ignore[misc]
    def real(self) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    def get_real(self) -> Incomplete: ...

    #
    @property
    def mT(self) -> Self: ...

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
    def __array_finalize__(self, /, obj: Incomplete) -> None: ...
    def __array_wrap__(
        self,
        /,
        obj: Incomplete,
        context: Incomplete | None = None,
        return_scalar: bool = False,
    ) -> Incomplete: ...
    def __setmask__(self, /, mask: Incomplete, copy: bool = False) -> None: ...

    #
    def __getitem__(self, indx: Incomplete, /) -> Incomplete: ...
    def __setitem__(self, indx: Incomplete, value: Incomplete, /) -> None: ...

    #
    def __eq__(self, other: Incomplete, /) -> Incomplete: ...
    def __ne__(self, other: Incomplete, /) -> Incomplete: ...
    def __ge__(self, other: Incomplete, /) -> Incomplete: ...
    def __gt__(self, other: Incomplete, /) -> Incomplete: ...
    def __le__(self, other: Incomplete, /) -> Incomplete: ...
    def __lt__(self, other: Incomplete, /) -> Incomplete: ...
    def __add__(self, other: Incomplete, /) -> Incomplete: ...
    def __radd__(self, other: Incomplete, /) -> Incomplete: ...
    def __sub__(self, other: Incomplete, /) -> Incomplete: ...
    def __rsub__(self, other: Incomplete, /) -> Incomplete: ...
    def __mul__(self, other: Incomplete, /) -> Incomplete: ...
    def __rmul__(self, other: Incomplete, /) -> Incomplete: ...
    def __div__(self, other: Incomplete, /) -> Incomplete: ...
    def __truediv__(self, other: Incomplete, /) -> Incomplete: ...
    def __rtruediv__(self, other: Incomplete, /) -> Incomplete: ...
    def __floordiv__(self, other: Incomplete, /) -> Incomplete: ...
    def __rfloordiv__(self, other: Incomplete, /) -> Incomplete: ...
    def __pow__(self, other: Incomplete, /) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def __rpow__(self, other: Incomplete, /) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def __iadd__(self, other: Incomplete, /) -> Self: ...
    def __isub__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __imul__(self, other: Incomplete, /) -> Self: ...
    def __idiv__(self, other: Incomplete, /) -> Self: ...
    def __ifloordiv__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __itruediv__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __ipow__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]

    #
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...

    #
    def __reduce__(self) -> Incomplete: ...
    def __deepcopy__(self, /, memo: Incomplete = ...) -> Self: ...

    #
    def view(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        dtype: Incomplete = None,
        type: Incomplete = None,
        fill_value: Incomplete = None,
    ) -> Incomplete: ...
    def harden_mask(self) -> Incomplete: ...
    def soften_mask(self) -> Incomplete: ...
    def unshare_mask(self) -> Incomplete: ...
    def shrink_mask(self) -> Incomplete: ...
    def filled(self, /, fill_value: Incomplete = None) -> Incomplete: ...
    def compressed(self) -> Incomplete: ...
    def compress(self, /, condition: Incomplete, axis: Incomplete = None, out: Incomplete = None) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def count(self, axis: Incomplete = None, keepdims: Incomplete = ...) -> Incomplete: ...
    def ravel(self, order: Incomplete = ...) -> Incomplete: ...
    def reshape(self, *s: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def resize(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        newshape: Incomplete,
        refcheck: Incomplete = ...,
        order: Incomplete = ...,
    ) -> Incomplete: ...
    def put(self, indices: Incomplete, values: Incomplete, mode: Incomplete = ...) -> Incomplete: ...
    def ids(self) -> Incomplete: ...
    def iscontiguous(self) -> Incomplete: ...
    def all(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def any(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def nonzero(self) -> Incomplete: ...
    def trace(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        offset: Incomplete = ...,
        axis1: Incomplete = ...,
        axis2: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
    ) -> Incomplete: ...
    def dot(self, b: Incomplete, out: Incomplete = ..., strict: Incomplete = ...) -> Incomplete: ...

    #
    def sum(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def cumsum(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def prod(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    product = prod
    def cumprod(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def mean(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def anom(self, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    def var(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def std(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def round(self, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    def sort(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        kind: Incomplete = ...,
        order: Incomplete = ...,
        endwith: Incomplete = ...,
        fill_value: Incomplete = ...,
        stable: Incomplete = ...,
    ) -> Incomplete: ...
    def argsort(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        kind: Incomplete = ...,
        order: Incomplete = ...,
        endwith: Incomplete = ...,
        fill_value: Incomplete = ...,
        stable: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def min(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def argmin(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        fill_value: Incomplete = ...,
        out: Incomplete = ...,
        *,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def max(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def argmax(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        axis: Incomplete = ...,
        fill_value: Incomplete = ...,
        out: Incomplete = ...,
        *,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def ptp(
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def partition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def argpartition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

    #
    def take(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        indices: Incomplete,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        mode: Incomplete = ...,
    ) -> Incomplete: ...

    #
    def copy(self, /, order: _OrderKACF = "C") -> Self: ...

    #
    diagonal: Incomplete
    flatten: Incomplete
    repeat: Incomplete
    squeeze: Incomplete
    swapaxes: Incomplete
    T: Incomplete
    transpose: Incomplete

    #
    def toflex(self) -> Incomplete: ...
    def torecords(self) -> Incomplete: ...
    def tolist(self, fill_value: Incomplete = ...) -> Incomplete: ...
    def tobytes(self, fill_value: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def tofile(self, fid: Incomplete, sep: Incomplete = ..., format: Incomplete = ...) -> Incomplete: ...

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
    def __getitem__(self, indx: Incomplete, /) -> Incomplete: ...
    def __setitem__(self, indx: Incomplete, value: Incomplete, /) -> None: ...
    def __iter__(self) -> Incomplete: ...
    def __len__(self) -> int: ...

    #
    def filled(self, fill_value: Incomplete = ...) -> Incomplete: ...
    def tolist(self) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

# 0D float64 array
class MaskedConstant(MaskedArray[tuple[()], np.dtype[np.float64]]):
    def __new__(cls) -> Self: ...
    def __array_wrap__(  # type: ignore[override]
        self,
        /,
        obj: Incomplete,
        context: Incomplete | None = None,
        return_scalar: bool = False,
    ) -> MaskedArray[tuple[()], np.dtype[np.float64]]: ...
    def __format__(self, format_spec: str, /) -> str: ...

    #
    def __iop__(self, other: Incomplete, /) -> Self: ...
    def __iadd__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __isub__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __imul__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __ifloordiv__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __itruediv__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]
    def __ipow__(self, other: Incomplete, /) -> Self: ...  # type: ignore[override]

    #
    def __reduce__(self) -> tuple[type[Self], tuple[()]]: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, /, memo: object) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def copy(self, /, *args: object, **kwargs: object) -> Incomplete: ...

class _frommethod:
    __name__: str
    __doc__: str
    reversed: Incomplete
    def __init__(self, methodname: Incomplete, reversed: Incomplete = ...) -> None: ...
    def __call__(self, a: Incomplete, *args: Incomplete, **params: Incomplete) -> Incomplete: ...
    def getdoc(self) -> Incomplete: ...

class _convert2ma:
    __doc__: str
    def __init__(self, funcname: Incomplete, params: Incomplete = ...) -> None: ...
    def __call__(self, *args: Incomplete, **params: Incomplete) -> Incomplete: ...
    def getdoc(self) -> Incomplete: ...

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
def min(
    obj: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    fill_value: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...
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
    a: Incomplete,
    indices: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    mode: Incomplete = ...,
) -> Incomplete: ...
def power(a: Incomplete, b: Incomplete, third: Incomplete = ...) -> Incomplete: ...
def argsort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
    stable: Incomplete = ...,
) -> Incomplete: ...
def sort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
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
    a: Incomplete,
    /,
    n: Incomplete = ...,
    axis: Incomplete = ...,
    prepend: Incomplete = ...,
    append: Incomplete = ...,
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
    a: Incomplete,
    b: Incomplete,
    masked_equal: Incomplete = ...,
    rtol: Incomplete = ...,
    atol: Incomplete = ...,
) -> Incomplete: ...
def asarray(a: Incomplete, dtype: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...
def asanyarray(a: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def fromflex(fxarray: Incomplete) -> Incomplete: ...
def make_mask_descr(ndtype: Incomplete) -> Incomplete: ...
def getmask(a: Incomplete) -> Incomplete: ...
def getmaskarray(arr: Incomplete) -> Incomplete: ...
def is_mask(m: Incomplete) -> Incomplete: ...
def make_mask(m: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
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
def mask_rowcols(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def default_fill_value(obj: Incomplete) -> Incomplete: ...
def minimum_fill_value(obj: Incomplete) -> Incomplete: ...
def maximum_fill_value(obj: Incomplete) -> Incomplete: ...
def set_fill_value(a: Incomplete, fill_value: Incomplete) -> Incomplete: ...
def common_fill_value(a: Incomplete, b: Incomplete) -> Incomplete: ...
def filled(a: Incomplete, fill_value: Incomplete | None = None) -> Incomplete: ...
def getdata(a: Incomplete, subok: bool = True) -> Incomplete: ...
def fix_invalid(a: Incomplete, mask: Incomplete = ..., copy: bool = True, fill_value: Incomplete | None = None) -> Incomplete: ...
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
alltrue: _MaskedBinaryOperation
logical_or: _MaskedBinaryOperation
sometrue: Callable[..., Incomplete]
logical_xor: _MaskedBinaryOperation
bitwise_and: _MaskedBinaryOperation
bitwise_or: _MaskedBinaryOperation
bitwise_xor: _MaskedBinaryOperation
hypot: _MaskedBinaryOperation
divide: _MaskedBinaryOperation
true_divide: _MaskedBinaryOperation
floor_divide: _MaskedBinaryOperation
remainder: _MaskedBinaryOperation
fmod: _MaskedBinaryOperation
mod: _MaskedBinaryOperation

arange: _convert2ma
empty: _convert2ma
empty_like: _convert2ma
frombuffer: _convert2ma
fromfunction: _convert2ma
identity: _convert2ma
ones: _convert2ma
ones_like: _convert2ma
zeros: _convert2ma
zeros_like: _convert2ma

all: _frommethod
anomalies: _frommethod
anom: _frommethod
any: _frommethod
compress: _frommethod
cumprod: _frommethod
cumsum: _frommethod
copy: _frommethod
diagonal: _frommethod
harden_mask: _frommethod
ids: _frommethod
mean: _frommethod
nonzero: _frommethod
prod: _frommethod
product: _frommethod
ravel: _frommethod
repeat: _frommethod
soften_mask: _frommethod
std: _frommethod
sum: _frommethod
swapaxes: _frommethod
trace: _frommethod
var: _frommethod
count: _frommethod
argmin: _frommethod
argmax: _frommethod

minimum: _extrema_operation
maximum: _extrema_operation
