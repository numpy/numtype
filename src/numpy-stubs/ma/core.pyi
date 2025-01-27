from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any
from typing_extensions import Self, TypeVar

import numpy as np
from numpy import amax, amin, angle, bool_, clip, expand_dims, indices, squeeze  # noqa: ICN003

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

_ShapeType_co = TypeVar("_ShapeType_co", bound=tuple[int, ...], covariant=True)
_DType_co = TypeVar("_DType_co", bound=np.dtype[Any], covariant=True)

MaskType = bool
nomask: bool

class MaskedArrayFutureWarning(FutureWarning): ...
class MAError(Exception): ...
class MaskError(MAError): ...

def default_fill_value(obj: Incomplete) -> Incomplete: ...
def minimum_fill_value(obj: Incomplete) -> Incomplete: ...
def maximum_fill_value(obj: Incomplete) -> Incomplete: ...
def set_fill_value(a: Incomplete, fill_value: Incomplete) -> Incomplete: ...
def common_fill_value(a: Incomplete, b: Incomplete) -> Incomplete: ...
def filled(a: Incomplete, fill_value: Incomplete = ...) -> Incomplete: ...
def getdata(a: Incomplete, subok: Incomplete = ...) -> Incomplete: ...

get_data = getdata

def fix_invalid(a: Incomplete, mask: Incomplete = ..., copy: Incomplete = ..., fill_value: Incomplete = ...) -> Incomplete: ...

class _MaskedUFunc:
    f: Any
    __doc__: Any
    __name__: Any
    def __init__(self, ufunc: Incomplete) -> None: ...

class _MaskedUnaryOperation(_MaskedUFunc):
    fill: Any
    domain: Any
    def __init__(self, mufunc: Incomplete, fill: Incomplete = ..., domain: Incomplete = ...) -> None: ...
    def __call__(self, a: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

class _MaskedBinaryOperation(_MaskedUFunc):
    fillx: Any
    filly: Any
    def __init__(self, mbfunc: Incomplete, fillx: Incomplete = ..., filly: Incomplete = ...) -> None: ...
    def __call__(self, a: Incomplete, b: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def reduce(self, target: Incomplete, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    def outer(self, a: Incomplete, b: Incomplete) -> Incomplete: ...
    def accumulate(self, target: Incomplete, axis: Incomplete = ...) -> Incomplete: ...

class _DomainedBinaryOperation(_MaskedUFunc):
    domain: Any
    fillx: Any
    filly: Any
    def __init__(self, dbfunc: Incomplete, domain: Incomplete, fillx: Incomplete = ..., filly: Incomplete = ...) -> None: ...
    def __call__(self, a: Incomplete, b: Incomplete, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

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
sometrue: Callable[..., Any]
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

def make_mask_descr(ndtype: Incomplete) -> Incomplete: ...
def getmask(a: Incomplete) -> Incomplete: ...

get_mask = getmask

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

class _MaskedPrintOption:
    def __init__(self, display: Incomplete) -> None: ...
    def display(self) -> Incomplete: ...
    def set_display(self, s: Incomplete) -> Incomplete: ...
    def enabled(self) -> Incomplete: ...
    def enable(self, shrink: Incomplete = ...) -> Incomplete: ...

masked_print_option: _MaskedPrintOption

def flatten_structured_array(a: Incomplete) -> Incomplete: ...

class MaskedIterator:
    ma: Any
    dataiter: Any
    maskiter: Any
    def __init__(self, ma: Incomplete) -> None: ...
    def __iter__(self) -> Incomplete: ...
    def __getitem__(self, indx: Incomplete) -> Incomplete: ...
    def __setitem__(self, index: Incomplete, value: Incomplete) -> None: ...
    def __next__(self) -> Incomplete: ...

class MaskedArray(np.ndarray[_ShapeType_co, _DType_co]):
    __array_priority__: Any
    def __new__(
        cls,
        data: Incomplete = ...,
        mask: Incomplete = ...,
        dtype: Incomplete = ...,
        copy: Incomplete = ...,
        subok: Incomplete = ...,
        ndmin: Incomplete = ...,
        fill_value: Incomplete = ...,
        keep_mask: Incomplete = ...,
        hard_mask: Incomplete = ...,
        shrink: Incomplete = ...,
        order: Incomplete = ...,
    ) -> Incomplete: ...
    def __array_finalize__(self, obj: Incomplete) -> Incomplete: ...
    def __array_wrap__(self, obj: Incomplete, context: Incomplete = ..., return_scalar: Incomplete = ...) -> Incomplete: ...
    def view(self, dtype: Incomplete = ..., type: Incomplete = ..., fill_value: Incomplete = ...) -> Incomplete: ...
    def __getitem__(self, indx: Incomplete) -> Incomplete: ...
    def __setitem__(self, indx: Incomplete, value: Incomplete) -> None: ...
    @property
    def dtype(self) -> Incomplete: ...
    @dtype.setter
    def dtype(self, dtype: Incomplete) -> Incomplete: ...
    @property
    def shape(self) -> Incomplete: ...
    @shape.setter
    def shape(self, shape: Incomplete) -> Incomplete: ...
    def __setmask__(self, mask: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
    @property
    def mask(self) -> Incomplete: ...
    @mask.setter
    def mask(self, value: Incomplete) -> Incomplete: ...
    @property
    def recordmask(self) -> Incomplete: ...
    @recordmask.setter
    def recordmask(self, mask: Incomplete) -> Incomplete: ...
    def harden_mask(self) -> Incomplete: ...
    def soften_mask(self) -> Incomplete: ...
    @property
    def hardmask(self) -> Incomplete: ...
    def unshare_mask(self) -> Incomplete: ...
    @property
    def sharedmask(self) -> Incomplete: ...
    def shrink_mask(self) -> Incomplete: ...
    @property
    def baseclass(self) -> Incomplete: ...
    data: Any
    @property
    def flat(self) -> Incomplete: ...
    @flat.setter
    def flat(self, value: Incomplete) -> Incomplete: ...
    @property
    def fill_value(self) -> Incomplete: ...
    @fill_value.setter
    def fill_value(self, value: Incomplete = ...) -> Incomplete: ...
    get_fill_value: Any
    set_fill_value: Any
    def filled(self, fill_value: Incomplete = ...) -> Incomplete: ...
    def compressed(self) -> Incomplete: ...
    def compress(self, condition: Incomplete, axis: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
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
    def __pow__(self, other: Incomplete, /) -> Incomplete: ...
    def __rpow__(self, other: Incomplete, /) -> Incomplete: ...
    def __iadd__(self, other: Incomplete, /) -> Self: ...
    def __isub__(self, other: Incomplete, /) -> Self: ...
    def __imul__(self, other: Incomplete, /) -> Self: ...
    def __idiv__(self, other: Incomplete, /) -> Self: ...
    def __ifloordiv__(self, other: Incomplete, /) -> Self: ...
    def __itruediv__(self, other: Incomplete, /) -> Self: ...
    def __ipow__(self, other: Incomplete, /) -> Self: ...
    def __float__(self) -> float: ...
    def __int__(self) -> int: ...
    @property  # type: ignore[misc]
    def imag(self) -> Incomplete: ...
    get_imag: Any
    @property  # type: ignore[misc]
    def real(self) -> Incomplete: ...
    get_real: Any
    def count(self, axis: Incomplete = ..., keepdims: Incomplete = ...) -> Incomplete: ...
    def ravel(self, order: Incomplete = ...) -> Incomplete: ...
    def reshape(self, *s: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def resize(self, newshape: Incomplete, refcheck: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...
    def put(self, indices: Incomplete, values: Incomplete, mode: Incomplete = ...) -> Incomplete: ...
    def ids(self) -> Incomplete: ...
    def iscontiguous(self) -> Incomplete: ...
    def all(self, axis: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...) -> Incomplete: ...
    def any(self, axis: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...) -> Incomplete: ...
    def nonzero(self) -> Incomplete: ...
    def trace(
        self,
        offset: Incomplete = ...,
        axis1: Incomplete = ...,
        axis2: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
    ) -> Incomplete: ...
    def dot(self, b: Incomplete, out: Incomplete = ..., strict: Incomplete = ...) -> Incomplete: ...
    def sum(
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def cumsum(self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
    def prod(
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    product: Any
    def cumprod(self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
    def mean(
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def anom(self, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    def var(
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def std(
        self,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def round(self, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
    def argsort(
        self,
        axis: Incomplete = ...,
        kind: Incomplete = ...,
        order: Incomplete = ...,
        endwith: Incomplete = ...,
        fill_value: Incomplete = ...,
        stable: Incomplete = ...,
    ) -> Incomplete: ...
    def argmin(
        self,
        axis: Incomplete = ...,
        fill_value: Incomplete = ...,
        out: Incomplete = ...,
        *,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def argmax(
        self,
        axis: Incomplete = ...,
        fill_value: Incomplete = ...,
        out: Incomplete = ...,
        *,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def sort(
        self,
        axis: Incomplete = ...,
        kind: Incomplete = ...,
        order: Incomplete = ...,
        endwith: Incomplete = ...,
        fill_value: Incomplete = ...,
        stable: Incomplete = ...,
    ) -> Incomplete: ...
    def min(
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def max(
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def ptp(
        self,
        axis: Incomplete = ...,
        out: Incomplete = ...,
        fill_value: Incomplete = ...,
        keepdims: Incomplete = ...,
    ) -> Incomplete: ...
    def partition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def argpartition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def take(self, indices: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., mode: Incomplete = ...) -> Incomplete: ...
    copy: Any
    diagonal: Any
    flatten: Any
    repeat: Any
    squeeze: Any
    swapaxes: Any
    T: Any
    transpose: Any
    @property  # type: ignore[misc]
    def mT(self) -> Incomplete: ...
    def tolist(self, fill_value: Incomplete = ...) -> Incomplete: ...
    def tobytes(self, fill_value: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...
    def tofile(self, fid: Incomplete, sep: Incomplete = ..., format: Incomplete = ...) -> Incomplete: ...
    def toflex(self) -> Incomplete: ...
    torecords: Any
    def __reduce__(self) -> Incomplete: ...
    def __deepcopy__(self, memo: Incomplete = ...) -> Incomplete: ...

class mvoid(MaskedArray[_ShapeType_co, _DType_co]):
    def __new__(
        self,
        data: Incomplete,
        mask: Incomplete = ...,
        dtype: Incomplete = ...,
        fill_value: Incomplete = ...,
        hardmask: Incomplete = ...,
        copy: Incomplete = ...,
        subok: Incomplete = ...,
    ) -> Incomplete: ...
    def __getitem__(self, indx: Incomplete) -> Incomplete: ...
    def __setitem__(self, indx: Incomplete, value: Incomplete) -> None: ...
    def __iter__(self) -> Incomplete: ...
    def __len__(self) -> int: ...
    def filled(self, fill_value: Incomplete = ...) -> Incomplete: ...
    def tolist(self) -> Incomplete: ...

def isMaskedArray(x: Incomplete) -> Incomplete: ...

isarray = isMaskedArray
isMA = isMaskedArray

# 0D float64 array
class MaskedConstant(MaskedArray[Any, np.dtype[np.float64]]):
    def __new__(cls) -> Incomplete: ...
    __class__: Any
    def __array_finalize__(self, obj: Incomplete) -> Incomplete: ...
    def __array_wrap__(self, obj: Incomplete, context: Incomplete = ..., return_scalar: Incomplete = ...) -> Incomplete: ...
    def __format__(self, format_spec: Incomplete) -> str: ...
    def __reduce__(self) -> Incomplete: ...
    def __iop__(self, other: Incomplete) -> Incomplete: ...
    __iadd__: Any
    __isub__: Any
    __imul__: Any
    __ifloordiv__: Any
    __itruediv__: Any
    __ipow__: Any
    def copy(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    def __copy__(self) -> Incomplete: ...
    def __deepcopy__(self, memo: Incomplete) -> Incomplete: ...
    def __setattr__(self, attr: Incomplete, value: Incomplete) -> None: ...

masked: MaskedConstant
masked_singleton: MaskedConstant
masked_array = MaskedArray

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
def is_masked(x: Incomplete) -> Incomplete: ...

class _extrema_operation(_MaskedUFunc):
    compare: Any
    fill_value_func: Any
    def __init__(self, ufunc: Incomplete, compare: Incomplete, fill_value: Incomplete) -> None: ...
    # NOTE: in practice `b` has a default value, but users should
    # explicitly provide a value here as the default is deprecated
    def __call__(self, a: Incomplete, b: Incomplete) -> Incomplete: ...
    def reduce(self, target: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
    def outer(self, a: Incomplete, b: Incomplete) -> Incomplete: ...

def min(
    obj: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
) -> Incomplete: ...
def max(
    obj: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
) -> Incomplete: ...
def ptp(
    obj: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
) -> Incomplete: ...

class _frommethod:
    __name__: Any
    __doc__: Any
    reversed: Any
    def __init__(self, methodname: Incomplete, reversed: Incomplete = ...) -> None: ...
    def getdoc(self) -> Incomplete: ...
    def __call__(self, a: Incomplete, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

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
    a: Incomplete, /, n: Incomplete = ..., axis: Incomplete = ..., prepend: Incomplete = ..., append: Incomplete = ...
) -> Incomplete: ...
def where(condition: Incomplete, x: Incomplete = ..., y: Incomplete = ...) -> Incomplete: ...
def choose(indices: Incomplete, choices: Incomplete, out: Incomplete = ..., mode: Incomplete = ...) -> Incomplete: ...
def round_(a: Incomplete, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...

round = round_

def inner(a: Incomplete, b: Incomplete) -> Incomplete: ...

innerproduct = inner

def outer(a: Incomplete, b: Incomplete) -> Incomplete: ...

outerproduct = outer

def correlate(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def convolve(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def allequal(a: Incomplete, b: Incomplete, fill_value: Incomplete = ...) -> Incomplete: ...
def allclose(
    a: Incomplete, b: Incomplete, masked_equal: Incomplete = ..., rtol: Incomplete = ..., atol: Incomplete = ...
) -> Incomplete: ...
def asarray(a: Incomplete, dtype: Incomplete = ..., order: Incomplete = ...) -> Incomplete: ...
def asanyarray(a: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def fromflex(fxarray: Incomplete) -> Incomplete: ...

class _convert2ma:
    __doc__: Any
    def __init__(self, funcname: Incomplete, params: Incomplete = ...) -> None: ...
    def getdoc(self) -> Incomplete: ...
    def __call__(self, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

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

def append(a: Incomplete, b: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def dot(a: Incomplete, b: Incomplete, strict: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
def mask_rowcols(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
