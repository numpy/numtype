from builtins import bool as py_bool
from collections.abc import Callable, Sequence
from typing import (
    Any,
    Final,
    Literal as L,
    NoReturn,
    Protocol,
    SupportsAbs,
    SupportsIndex,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import TypeIs, TypeVar

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy import _AnyShapeT, _OrderCF, _OrderKACF, ufunc  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike, _DTypeLike, _ShapeLike, _SupportsArrayFunc, _SupportsDType
from numpy.lib._array_utils_impl import normalize_axis_tuple as normalize_axis_tuple

from ._asarray import require
from ._ufunc_config import errstate, getbufsize, geterr, geterrcall, setbufsize, seterr, seterrcall
from .arrayprint import (
    array2string,
    array_repr,
    array_str,
    format_float_positional,
    format_float_scientific,
    get_printoptions,
    printoptions,
    set_printoptions,
)
from .fromnumeric import (
    all,
    amax,
    amin,
    any,
    argmax,
    argmin,
    argpartition,
    argsort,
    around,
    choose,
    clip,
    compress,
    cumprod,
    cumsum,
    cumulative_prod,
    cumulative_sum,
    diagonal,
    matrix_transpose,
    max,
    mean,
    min,
    ndim,
    nonzero,
    partition,
    prod,
    ptp,
    put,
    ravel,
    repeat,
    reshape,
    resize,
    round,
    searchsorted,
    shape,
    size,
    sort,
    squeeze,
    std,
    sum,
    swapaxes,
    take,
    trace,
    transpose,
    var,
)
from .multiarray import (
    ALLOW_THREADS as ALLOW_THREADS,
    BUFSIZE as BUFSIZE,
    CLIP as CLIP,
    MAXDIMS as MAXDIMS,
    MAY_SHARE_BOUNDS as MAY_SHARE_BOUNDS,
    MAY_SHARE_EXACT as MAY_SHARE_EXACT,
    RAISE as RAISE,
    WRAP as WRAP,
    arange,
    array,
    asanyarray,
    asarray,
    ascontiguousarray,
    asfortranarray,
    broadcast,
    can_cast,
    concatenate,
    copyto,
    dot,
    dtype,
    empty,
    empty_like,
    flatiter,
    from_dlpack,
    frombuffer,
    fromfile,
    fromiter,
    fromstring,
    inner,
    lexsort,
    matmul,
    may_share_memory,
    min_scalar_type,
    ndarray,
    nditer,
    nested_iters,
    normalize_axis_index as normalize_axis_index,
    promote_types,
    putmask,
    result_type,
    shares_memory,
    vdot,
    where,
    zeros,
)
from .numerictypes import (
    ScalarType,
    bool,
    bool_,
    busday_count,
    busday_offset,
    busdaycalendar,
    byte,
    bytes_,
    cdouble,
    character,
    clongdouble,
    complex64,
    complex128,
    complex192,
    complex256,
    complexfloating,
    csingle,
    datetime64,
    datetime_as_string,
    datetime_data,
    double,
    flexible,
    float16,
    float32,
    float64,
    float96,
    float128,
    floating,
    generic,
    half,
    inexact,
    int8,
    int16,
    int32,
    int64,
    int_,
    intc,
    integer,
    intp,
    is_busday,
    isdtype,
    issubdtype,
    long,
    longdouble,
    longlong,
    number,
    object_,
    short,
    signedinteger,
    single,
    str_,
    timedelta64,
    typecodes,
    ubyte,
    uint,
    uint8,
    uint16,
    uint32,
    uint64,
    uintc,
    uintp,
    ulong,
    ulonglong,
    unsignedinteger,
    ushort,
    void,
)
from .umath import (
    absolute,
    add,
    arccos,
    arccosh,
    arcsin,
    arcsinh,
    arctan,
    arctan2,
    arctanh,
    bitwise_and,
    bitwise_count,
    bitwise_or,
    bitwise_xor,
    cbrt,
    ceil,
    conj,
    conjugate,
    copysign,
    cos,
    cosh,
    deg2rad,
    degrees,
    divide,
    divmod,
    e,
    equal,
    euler_gamma,
    exp,
    exp2,
    expm1,
    fabs,
    float_power,
    floor,
    floor_divide,
    fmax,
    fmin,
    fmod,
    frexp,
    frompyfunc,
    gcd,
    greater,
    greater_equal,
    heaviside,
    hypot,
    invert,
    isfinite,
    isinf,
    isnan,
    isnat,
    lcm,
    ldexp,
    left_shift,
    less,
    less_equal,
    log,
    log1p,
    log2,
    log10,
    logaddexp,
    logaddexp2,
    logical_and,
    logical_not,
    logical_or,
    logical_xor,
    matvec,
    maximum,
    minimum,
    mod,
    modf,
    multiply,
    negative,
    nextafter,
    not_equal,
    pi,
    positive,
    power,
    rad2deg,
    radians,
    reciprocal,
    remainder,
    right_shift,
    rint,
    sign,
    signbit,
    sin,
    sinh,
    spacing,
    sqrt,
    square,
    subtract,
    tan,
    tanh,
    true_divide,
    trunc,
    vecdot,
    vecmat,
)

__all__ = [
    "False_",
    "ScalarType",
    "True_",
    "absolute",
    "add",
    "all",
    "allclose",
    "amax",
    "amin",
    "any",
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
    "argpartition",
    "argsort",
    "argwhere",
    "around",
    "array",
    "array2string",
    "array_equal",
    "array_equiv",
    "array_repr",
    "array_str",
    "asanyarray",
    "asarray",
    "ascontiguousarray",
    "asfortranarray",
    "astype",
    "base_repr",
    "binary_repr",
    "bitwise_and",
    "bitwise_count",
    "bitwise_not",
    "bitwise_or",
    "bitwise_xor",
    "bool",
    "bool_",
    "broadcast",
    "busday_count",
    "busday_offset",
    "busdaycalendar",
    "byte",
    "bytes_",
    "can_cast",
    "cbrt",
    "cdouble",
    "ceil",
    "character",
    "choose",
    "clip",
    "clongdouble",
    "complex64",
    "complex128",
    "complex192",
    "complex256",
    "complexfloating",
    "compress",
    "concatenate",
    "conj",
    "conjugate",
    "convolve",
    "copysign",
    "copyto",
    "correlate",
    "cos",
    "cosh",
    "count_nonzero",
    "cross",
    "csingle",
    "cumprod",
    "cumsum",
    "cumulative_prod",
    "cumulative_sum",
    "datetime64",
    "datetime_as_string",
    "datetime_data",
    "deg2rad",
    "degrees",
    "diagonal",
    "divide",
    "divmod",
    "dot",
    "double",
    "dtype",
    "e",
    "empty",
    "empty_like",
    "equal",
    "errstate",
    "euler_gamma",
    "exp",
    "exp2",
    "expm1",
    "fabs",
    "flatiter",
    "flatnonzero",
    "flexible",
    "float16",
    "float32",
    "float64",
    "float96",
    "float128",
    "float_power",
    "floating",
    "floor",
    "floor_divide",
    "fmax",
    "fmin",
    "fmod",
    "format_float_positional",
    "format_float_scientific",
    "frexp",
    "from_dlpack",
    "frombuffer",
    "fromfile",
    "fromfunction",
    "fromiter",
    "frompyfunc",
    "fromstring",
    "full",
    "full_like",
    "gcd",
    "generic",
    "get_printoptions",
    "getbufsize",
    "geterr",
    "geterrcall",
    "greater",
    "greater_equal",
    "half",
    "heaviside",
    "hypot",
    "identity",
    "indices",
    "inexact",
    "inf",
    "inner",
    "int8",
    "int16",
    "int32",
    "int64",
    "int_",
    "intc",
    "integer",
    "intp",
    "invert",
    "is_busday",
    "isclose",
    "isdtype",
    "isfinite",
    "isfortran",
    "isinf",
    "isnan",
    "isnat",
    "isscalar",
    "issubdtype",
    "lcm",
    "ldexp",
    "left_shift",
    "less",
    "less_equal",
    "lexsort",
    "little_endian",
    "log",
    "log1p",
    "log2",
    "log10",
    "logaddexp",
    "logaddexp2",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "long",
    "longdouble",
    "longlong",
    "matmul",
    "matrix_transpose",
    "matvec",
    "max",
    "maximum",
    "may_share_memory",
    "mean",
    "min",
    "min_scalar_type",
    "minimum",
    "mod",
    "modf",
    "moveaxis",
    "multiply",
    "nan",
    "ndarray",
    "ndim",
    "nditer",
    "negative",
    "nested_iters",
    "newaxis",
    "nextafter",
    "nonzero",
    "not_equal",
    "number",
    "object_",
    "ones",
    "ones_like",
    "outer",
    "partition",
    "pi",
    "positive",
    "power",
    "printoptions",
    "prod",
    "promote_types",
    "ptp",
    "put",
    "putmask",
    "rad2deg",
    "radians",
    "ravel",
    "reciprocal",
    "remainder",
    "repeat",
    "require",
    "reshape",
    "resize",
    "result_type",
    "right_shift",
    "rint",
    "roll",
    "rollaxis",
    "round",
    "searchsorted",
    "set_printoptions",
    "setbufsize",
    "seterr",
    "seterrcall",
    "shape",
    "shares_memory",
    "short",
    "sign",
    "signbit",
    "signedinteger",
    "sin",
    "single",
    "sinh",
    "size",
    "sort",
    "spacing",
    "sqrt",
    "square",
    "squeeze",
    "std",
    "str_",
    "subtract",
    "sum",
    "swapaxes",
    "take",
    "tan",
    "tanh",
    "tensordot",
    "timedelta64",
    "trace",
    "transpose",
    "true_divide",
    "trunc",
    "typecodes",
    "ubyte",
    "ufunc",
    "uint",
    "uint8",
    "uint16",
    "uint32",
    "uint64",
    "uintc",
    "uintp",
    "ulong",
    "ulonglong",
    "unsignedinteger",
    "ushort",
    "var",
    "vdot",
    "vecdot",
    "vecdot",
    "vecmat",
    "void",
    "where",
    "zeros",
    "zeros_like",
]
###

_T = TypeVar("_T")
_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=np.ndarray[Any, Any], covariant=True)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_ShapeLike1D: TypeAlias = SupportsIndex | tuple[SupportsIndex]
_ShapeLike2D: TypeAlias = tuple[SupportsIndex, SupportsIndex]
_ShapeLike3D: TypeAlias = tuple[SupportsIndex, SupportsIndex, SupportsIndex]

_PyScalar: TypeAlias = complex | str | bytes
_Device: TypeAlias = L["cpu"]
_Mode: TypeAlias = L["valid", "same", "full"]
_Axes: TypeAlias = int | tuple[_ShapeLike, _ShapeLike]

@type_check_only
class _CanArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

###

bitwise_not = invert
newaxis: Final[None] = None

little_endian: Final[py_bool] = ...

inf: Final[float] = ...
nan: Final[float] = ...
False_: Final[np.bool[L[False]]] = ...
True_: Final[np.bool[L[True]]] = ...

###

# NOTE: Keep in sync with `empty` and `zeros` in `._multiarray_umath.ones`
@overload  # 1d shape, default dtype (float64)
def ones(
    shape: _ShapeLike1D,
    dtype: _nt.ToDTypeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def ones(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def ones(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def ones(
    shape: _ShapeLike1D,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D: ...
@overload  # known shape, default dtype (float64)
def ones(
    shape: _AnyShapeT,
    dtype: _nt.ToDTypeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, known dtype
def ones(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def ones(
    shape: _AnyShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def ones(
    shape: _AnyShapeT,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def ones(
    shape: _ShapeLike,
    dtype: _nt.ToDTypeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # unknown shape, known dtype
def ones(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[Any, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def ones(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def ones(
    shape: _ShapeLike,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array: ...

# NOTE: keep in sync with `ones` (but note that `full` has 18 additional overloads)
# NOTE: The mypy [overload-overlap] errors are false-positives that are caused by a
#   bug that's related to constrained type-vars.
@overload  # 1d shape, known fill scalar-type
def full(
    shape: _ShapeLike1D,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # 1d shape, bool fill
def full(
    shape: _ShapeLike1D,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.bool]: ...
@overload  # 1d shape, int fill
def full(
    shape: _ShapeLike1D,
    fill_value: _nt.JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # 1d shape, float fill
def full(
    shape: _ShapeLike1D,
    fill_value: _nt.JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # 1d shape, complex fill
def full(
    shape: _ShapeLike1D,
    fill_value: _nt.JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload  # 1d shape, known dtype
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[_ScalarT]: ...
@overload  # 1d shape, float64 dtype
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # 1d shape, unknown dtype
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array1D: ...
@overload  # known shape, known fill scalar-type
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, bool fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.bool, _AnyShapeT]: ...
@overload  # known shape, int fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: _nt.JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.intp, _AnyShapeT]: ...
@overload  # known shape, float fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: _nt.JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, complex fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: _nt.JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.complex128, _AnyShapeT]: ...
@overload  # known shape, known scalar-type
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # known shape, known dtype
def full(
    shape: _AnyShapeT,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, float64
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, unknown dtype
def full(
    shape: _AnyShapeT,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, known fill scalar-type
def full(
    shape: _ShapeLike,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, bool fill
def full(
    shape: _ShapeLike,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.bool]: ...
@overload  # unknown shape, int fill
def full(
    shape: _ShapeLike,
    fill_value: _nt.JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # unknown shape, float fill
def full(
    shape: _ShapeLike,
    fill_value: _nt.JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # unknown shape, complex fill
def full(
    shape: _ShapeLike,
    fill_value: _nt.JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # unknown shape, known dtype
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[Any, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # unknown shape, float64
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # unknown shape, unknown dtype
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> _nt.Array: ...

# NOTE: Keep in sync with `ones_like` and `._multiarray_umath.empty_like`
@overload  # known array, subok=True
def zeros_like(
    a: _ArrayT,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _ArrayT: ...
@overload  # array-like with known shape and type
def zeros_like(
    a: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    dtype: _DTypeT | _SupportsDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload  # bool 0d array-like
def zeros_like(
    a: _nt.ToBool_0d,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def zeros_like(
    a: _nt.ToBool_1ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def zeros_like(
    a: _nt.ToBool_2ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def zeros_like(
    a: _nt.ToBool_3ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.bool_]: ...
@overload  # int 0d array-like
def zeros_like(
    a: _nt.ToInt_0d,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.intp]: ...
@overload  # int 1d array-like
def zeros_like(
    a: _nt.ToInt_1ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # int 2d array-like
def zeros_like(
    a: _nt.ToInt_2ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.intp]: ...
@overload  # int 3d array-like
def zeros_like(
    a: _nt.ToInt_3ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.intp]: ...
@overload  # float 0d array-like
def zeros_like(
    a: _nt.ToFloat64_0d,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.float64]: ...
@overload  # float 1d array-like
def zeros_like(
    a: _nt.ToFloat64_1ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # float 2d array-like
def zeros_like(
    a: _nt.ToFloat64_2ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.float64]: ...
@overload  # float 3d array-like
def zeros_like(
    a: _nt.ToFloat64_3ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.float64]: ...
@overload  # complex 0d array-like
def zeros_like(
    a: _nt.ToComplex128_0d,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def zeros_like(
    a: _nt.ToComplex128_1ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def zeros_like(
    a: _nt.ToComplex128_2ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def zeros_like(
    a: _nt.ToComplex128_3ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def zeros_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def zeros_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # given shape, given dtype
def zeros_like(  # type: ignore[overload-overlap]
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def zeros_like(
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[Any, _DTypeT]: ...
@overload  # given shape, given scalar-type
def zeros_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def zeros_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # bool array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: _nt.ToBool_nd,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.bool_]: ...
@overload  # int array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: _nt.ToInt_nd,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # float array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: _nt.ToFloat64_nd,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: _nt.ToComplex128_nd,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def zeros_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def zeros_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array: ...

# NOTE: Keep in sync with `zeros_like` and `._multiarray_umath.empty_like`
@overload  # known array, subok=True
def ones_like(
    a: _ArrayT,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _ArrayT: ...
@overload  # array-like with known shape and type
def ones_like(
    a: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    dtype: _DTypeT | _SupportsDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload  # bool 0d array-like
def ones_like(
    a: _nt.ToBool_0d,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def ones_like(
    a: _nt.ToBool_1ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def ones_like(
    a: _nt.ToBool_2ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def ones_like(
    a: _nt.ToBool_3ds,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.bool_]: ...
@overload  # int 0d array-like
def ones_like(
    a: _nt.ToInt_0d,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.intp]: ...
@overload  # int 1d array-like
def ones_like(
    a: _nt.ToInt_1ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # int 2d array-like
def ones_like(
    a: _nt.ToInt_2ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.intp]: ...
@overload  # int 3d array-like
def ones_like(
    a: _nt.ToInt_3ds,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.intp]: ...
@overload  # float 0d array-like
def ones_like(
    a: _nt.ToFloat64_0d,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.float64]: ...
@overload  # float 1d array-like
def ones_like(
    a: _nt.ToFloat64_1ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # float 2d array-like
def ones_like(
    a: _nt.ToFloat64_2ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.float64]: ...
@overload  # float 3d array-like
def ones_like(
    a: _nt.ToFloat64_3ds,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.float64]: ...
@overload  # complex 0d array-like
def ones_like(
    a: _nt.ToComplex128_0d,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def ones_like(
    a: _nt.ToComplex128_1ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def ones_like(
    a: _nt.ToComplex128_2ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def ones_like(
    a: _nt.ToComplex128_3ds,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def ones_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def ones_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # given shape, given dtype
def ones_like(  # type: ignore[overload-overlap]
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def ones_like(
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[Any, _DTypeT]: ...
@overload  # given shape, given scalar-type
def ones_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def ones_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # bool array-like
def ones_like(  # type: ignore[overload-overlap]
    a: _nt.ToBool_nd,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.bool_]: ...
@overload  # int array-like
def ones_like(  # type: ignore[overload-overlap]
    a: _nt.ToInt_nd,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # float array-like
def ones_like(  # type: ignore[overload-overlap]
    a: _nt.ToFloat64_nd,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex array-like
def ones_like(  # type: ignore[overload-overlap]
    a: _nt.ToComplex128_nd,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def ones_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def ones_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array: ...

# NOTE: Keep in sync with `{zeros,ones}_like` and `._multiarray_umath.empty_like`
@overload  # known array, subok=True
def full_like(
    a: _ArrayT,
    fill_value: object,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _ArrayT: ...
@overload  # array-like with known shape and type
def full_like(
    a: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[_ShapeT, _DTypeT]: ...
@overload  # bool 0d array-like
def full_like(
    a: _nt.ToBool_0d,
    fill_value: object,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def full_like(
    a: _nt.ToBool_1ds,
    fill_value: object,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def full_like(
    a: _nt.ToBool_2ds,
    fill_value: object,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def full_like(
    a: _nt.ToBool_3ds,
    fill_value: object,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.bool_]: ...
@overload  # int 0d array-like
def full_like(
    a: _nt.ToInt_0d,
    fill_value: object,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.intp]: ...
@overload  # int 1d array-like
def full_like(
    a: _nt.ToInt_1ds,
    fill_value: object,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.intp]: ...
@overload  # int 2d array-like
def full_like(
    a: _nt.ToInt_2ds,
    fill_value: object,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.intp]: ...
@overload  # int 3d array-like
def full_like(
    a: _nt.ToInt_3ds,
    fill_value: object,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.intp]: ...
@overload  # float 0d array-like
def full_like(
    a: _nt.ToFloat64_0d,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.float64]: ...
@overload  # float 1d array-like
def full_like(
    a: _nt.ToFloat64_1ds,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.float64]: ...
@overload  # float 2d array-like
def full_like(
    a: _nt.ToFloat64_2ds,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.float64]: ...
@overload  # float 3d array-like
def full_like(
    a: _nt.ToFloat64_3ds,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.float64]: ...
@overload  # complex 0d array-like
def full_like(
    a: _nt.ToComplex128_0d,
    fill_value: object,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def full_like(
    a: _nt.ToComplex128_1ds,
    fill_value: object,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def full_like(
    a: _nt.ToComplex128_2ds,
    fill_value: object,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def full_like(
    a: _nt.ToComplex128_3ds,
    fill_value: object,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def full_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    fill_value: object,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def full_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    fill_value: object,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # given shape, given dtype
def full_like(  # type: ignore[overload-overlap]
    a: object,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> np.ndarray[_AnyShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def full_like(
    a: object,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[Any, _DTypeT]: ...
@overload  # given shape, given scalar-type
def full_like(
    a: object,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def full_like(
    a: object,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[_ScalarT]: ...
@overload  # bool array-like
def full_like(  # type: ignore[overload-overlap]
    a: _nt.ToBool_nd,
    fill_value: object,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.bool_]: ...
@overload  # int array-like
def full_like(  # type: ignore[overload-overlap]
    a: _nt.ToInt_nd,
    fill_value: object,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.intp]: ...
@overload  # float array-like
def full_like(  # type: ignore[overload-overlap]
    a: _nt.ToFloat64_nd,
    fill_value: object,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.float64]: ...
@overload  # complex array-like
def full_like(  # type: ignore[overload-overlap]
    a: _nt.ToComplex128_nd,
    fill_value: object,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def full_like(
    a: object,
    fill_value: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> _nt.Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def full_like(
    a: object,
    fill_value: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.Array: ...

#
@overload
def count_nonzero(a: ArrayLike, axis: None = None, *, keepdims: L[False] = False) -> int: ...
@overload
def count_nonzero(a: ArrayLike, axis: _ShapeLike | None = None, *, keepdims: py_bool = False) -> Any: ...

#
def flatnonzero(a: ArrayLike) -> _nt.Array1D[np.intp]: ...
def argwhere(a: ArrayLike) -> _nt.Array[np.intp]: ...

#
def isfortran(a: _nt.Array | np.generic) -> py_bool: ...

#
@overload
def correlate(a: _nt.ToBool_1d, v: _nt.ToBool_1d, mode: _Mode = "valid") -> _nt.Array1D[np.bool]: ...
@overload
def correlate(a: _nt.ToUInteger_1d, v: _nt.CoUInt64_1d, mode: _Mode = "valid") -> _nt.Array1D[np.unsignedinteger]: ...
@overload
def correlate(
    a: _nt.CoUInt64_1d, v: _nt.ToUInteger_1d, mode: _Mode = "valid"
) -> _nt.Array1D[np.unsignedinteger]: ...  #
@overload
def correlate(a: _nt.ToSInteger_1d, v: _nt.CoInt64_1d, mode: _Mode = "valid") -> _nt.Array1D[np.signedinteger]: ...
@overload
def correlate(a: _nt.CoInt64_1d, v: _nt.ToSInteger_1d, mode: _Mode = "valid") -> _nt.Array1D[np.signedinteger]: ...
@overload
def correlate(a: _nt.ToFloating_1d, v: _nt.CoFloating_1d, mode: _Mode = "valid") -> _nt.Array1D[np.floating]: ...
@overload
def correlate(a: _nt.CoFloating_1d, v: _nt.ToFloating_1d, mode: _Mode = "valid") -> _nt.Array1D[np.floating]: ...
@overload
def correlate(a: _nt.ToComplex_1d, v: _nt.CoComplex_1d, mode: _Mode = "valid") -> _nt.Array1D[np.complexfloating]: ...
@overload
def correlate(a: _nt.CoComplex_1d, v: _nt.ToComplex_1d, mode: _Mode = "valid") -> _nt.Array1D[np.complexfloating]: ...
@overload
def correlate(a: _nt.ToTimeDelta_1d, v: _nt.CoTimeDelta_1d, mode: _Mode = "valid") -> _nt.Array1D[np.timedelta64]: ...
@overload
def correlate(a: _nt.CoTimeDelta_1d, v: _nt.ToTimeDelta_1d, mode: _Mode = "valid") -> _nt.Array1D[np.timedelta64]: ...
@overload
def correlate(a: _nt.ToObject_1d, v: _nt.ToObject_1d, mode: _Mode = "valid") -> _nt.Array1D[np.object_]: ...
@overload
def correlate(
    a: _nt.CoComplex_1d | _nt.CoTimeDelta_1d | _nt.ToObject_1d,
    v: _nt.CoComplex_1d | _nt.CoTimeDelta_1d | _nt.ToObject_1d,
    mode: _Mode = "valid",
) -> _nt.Array1D[Any]: ...

#
@overload
def convolve(a: _nt.ToBool_1d, v: _nt.ToBool_1d, mode: _Mode = "valid") -> _nt.Array1D[np.bool]: ...
@overload
def convolve(a: _nt.ToUInteger_1d, v: _nt.CoUInt64_1d, mode: _Mode = "valid") -> _nt.Array1D[np.unsignedinteger]: ...
@overload
def convolve(a: _nt.CoUInt64_1d, v: _nt.ToUInteger_1d, mode: _Mode = "valid") -> _nt.Array1D[np.unsignedinteger]: ...
@overload
def convolve(a: _nt.ToSInteger_1d, v: _nt.CoInt64_1d, mode: _Mode = "valid") -> _nt.Array1D[np.signedinteger]: ...
@overload
def convolve(a: _nt.CoInt64_1d, v: _nt.ToSInteger_1d, mode: _Mode = "valid") -> _nt.Array1D[np.signedinteger]: ...
@overload
def convolve(a: _nt.ToFloating_1d, v: _nt.CoFloating_1d, mode: _Mode = "valid") -> _nt.Array1D[np.floating]: ...
@overload
def convolve(a: _nt.CoFloating_1d, v: _nt.ToFloating_1d, mode: _Mode = "valid") -> _nt.Array1D[np.floating]: ...
@overload
def convolve(a: _nt.ToComplex_1d, v: _nt.CoComplex_1d, mode: _Mode = "valid") -> _nt.Array1D[np.complexfloating]: ...
@overload
def convolve(a: _nt.CoComplex_1d, v: _nt.ToComplex_1d, mode: _Mode = "valid") -> _nt.Array1D[np.complexfloating]: ...
@overload
def convolve(a: _nt.ToTimeDelta_1d, v: _nt.CoTimeDelta_1d, mode: _Mode = "valid") -> _nt.Array1D[np.timedelta64]: ...
@overload
def convolve(a: _nt.CoTimeDelta_1d, v: _nt.ToTimeDelta_1d, mode: _Mode = "valid") -> _nt.Array1D[np.timedelta64]: ...
@overload
def convolve(a: _nt.ToObject_1d, v: _nt.ToObject_1d, mode: _Mode = "valid") -> _nt.Array1D[np.object_]: ...
@overload
def convolve(
    a: _nt.CoComplex_1d | _nt.CoTimeDelta_1d | _nt.ToObject_1d,
    v: _nt.CoComplex_1d | _nt.CoTimeDelta_1d | _nt.ToObject_1d,
    mode: _Mode = "valid",
) -> _nt.Array1D[Any]: ...

#
@overload
def outer(a: _nt.ToBool_nd, b: _nt.ToBool_nd, out: None = None) -> _nt.Array2D[np.bool]: ...
@overload
def outer(a: _nt.ToUInteger_nd, b: _nt.CoUInt64_nd, out: None = None) -> _nt.Array2D[np.unsignedinteger]: ...
@overload
def outer(a: _nt.CoUInt64_nd, b: _nt.ToUInteger_nd, out: None = None) -> _nt.Array2D[np.unsignedinteger]: ...
@overload
def outer(a: _nt.ToSInteger_nd, b: _nt.CoInt64_nd, out: None = None) -> _nt.Array2D[np.signedinteger]: ...
@overload
def outer(a: _nt.CoInt64_nd, b: _nt.ToSInteger_nd, out: None = None) -> _nt.Array2D[np.signedinteger]: ...
@overload
def outer(a: _nt.ToFloating_nd, b: _nt.CoFloating_nd, out: None = None) -> _nt.Array2D[np.floating]: ...
@overload
def outer(a: _nt.CoFloating_nd, b: _nt.ToFloating_nd, out: None = None) -> _nt.Array2D[np.floating]: ...
@overload
def outer(a: _nt.ToComplex_nd, b: _nt.CoComplex_nd, out: None = None) -> _nt.Array2D[np.complexfloating]: ...
@overload
def outer(a: _nt.CoComplex_nd, b: _nt.ToComplex_nd, out: None = None) -> _nt.Array2D[np.complexfloating]: ...
@overload
def outer(a: _nt.ToTimeDelta_nd, b: _nt.CoTimeDelta_nd, out: None = None) -> _nt.Array2D[np.timedelta64]: ...
@overload
def outer(a: _nt.CoTimeDelta_nd, b: _nt.ToTimeDelta_nd, out: None = None) -> _nt.Array2D[np.timedelta64]: ...
@overload
def outer(a: _nt.ToObject_nd, b: _nt.ToObject_nd, out: None = None) -> _nt.Array2D[np.object_]: ...
@overload
def outer(
    a: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    b: _nt.CoComplex_nd | _nt.CoTimeDelta_nd | _nt.ToObject_nd,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def tensordot(a: _nt.ToBool_1nd, b: _nt.ToBool_1nd, axes: _Axes = 2) -> _nt.Array[np.bool]: ...
@overload
def tensordot(a: _nt.ToUInteger_1nd, b: _nt.CoUInt64_1nd, axes: _Axes = 2) -> _nt.Array[np.unsignedinteger]: ...
@overload
def tensordot(a: _nt.CoUInt64_1nd, b: _nt.ToUInteger_1nd, axes: _Axes = 2) -> _nt.Array[np.unsignedinteger]: ...
@overload
def tensordot(a: _nt.ToSInteger_1nd, b: _nt.CoInt64_1nd, axes: _Axes = 2) -> _nt.Array[np.signedinteger]: ...
@overload
def tensordot(a: _nt.CoInt64_1nd, b: _nt.ToSInteger_1nd, axes: _Axes = 2) -> _nt.Array[np.signedinteger]: ...
@overload
def tensordot(a: _nt.ToFloating_1nd, b: _nt.CoFloating_1nd, axes: _Axes = 2) -> _nt.Array[np.floating]: ...
@overload
def tensordot(a: _nt.CoFloating_1nd, b: _nt.ToFloating_1nd, axes: _Axes = 2) -> _nt.Array[np.floating]: ...
@overload
def tensordot(a: _nt.ToComplex_1nd, b: _nt.CoComplex_1nd, axes: _Axes = 2) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(a: _nt.CoComplex_1nd, b: _nt.ToComplex_1nd, axes: _Axes = 2) -> _nt.Array[np.complexfloating]: ...
@overload
def tensordot(a: _nt.ToTimeDelta_1nd, b: _nt.CoTimeDelta_1nd, axes: _Axes = 2) -> _nt.Array[np.timedelta64]: ...
@overload
def tensordot(a: _nt.CoTimeDelta_1nd, b: _nt.ToTimeDelta_1nd, axes: _Axes = 2) -> _nt.Array[np.timedelta64]: ...
@overload
def tensordot(a: _nt.ToObject_1nd, b: _nt.ToObject_1nd, axes: _Axes = 2) -> _nt.Array[np.object_]: ...
@overload
def tensordot(
    a: _nt.CoComplex_1nd | _nt.CoTimeDelta_1nd | _nt.ToObject_1nd,
    b: _nt.CoComplex_1nd | _nt.CoTimeDelta_1nd | _nt.ToObject_1nd,
    axes: _Axes = 2,
) -> _nt.Array[Any]: ...

#
@overload
def roll(a: _ArrayLike[_ScalarT], shift: _ShapeLike, axis: _ShapeLike | None = None) -> _nt.Array[_ScalarT]: ...
@overload
def roll(a: ArrayLike, shift: _ShapeLike, axis: _ShapeLike | None = None) -> _nt.Array: ...

#
def rollaxis(a: _nt.Array[_ScalarT], axis: int, start: int = ...) -> _nt.Array[_ScalarT]: ...
def moveaxis(a: _nt.Array[_ScalarT], source: _ShapeLike, destination: _ShapeLike) -> _nt.Array[_ScalarT]: ...

#
@overload
def cross(
    a: _nt.ToBool_1nd,
    b: _nt.ToBool_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> NoReturn: ...
@overload
def cross(
    a: _nt.ToUInteger_1nd,
    b: _nt.CoUInt64_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.unsignedinteger]: ...
@overload
def cross(
    a: _nt.CoUInt64_1nd,
    b: _nt.ToUInteger_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.unsignedinteger]: ...
@overload
def cross(
    a: _nt.ToSInteger_1nd,
    b: _nt.CoInt64_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.signedinteger]: ...
@overload
def cross(
    a: _nt.CoInt64_1nd,
    b: _nt.ToSInteger_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.signedinteger]: ...
@overload
def cross(
    a: _nt.ToFloating_1nd,
    b: _nt.CoFloating_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.floating]: ...
@overload
def cross(
    a: _nt.CoFloating_1nd,
    b: _nt.ToFloating_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.floating]: ...
@overload
def cross(
    a: _nt.ToComplex_1nd,
    b: _nt.CoComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.complexfloating]: ...
@overload
def cross(
    a: _nt.CoComplex_1nd,
    b: _nt.ToComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[np.complexfloating]: ...
@overload
def cross(
    a: _nt.CoComplex_1nd,
    b: _nt.CoComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> _nt.Array[Any]: ...

#
@overload
def indices(
    dimensions: _nt.ToInteger_1d, dtype: type[_nt.JustInt] = ..., sparse: L[False] = False
) -> _nt.Array[np.intp]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d, dtype: type[_nt.JustInt], sparse: L[True]
) -> tuple[_nt.Array[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d, dtype: type[_nt.JustInt] = ..., *, sparse: L[True]
) -> tuple[_nt.Array[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d, dtype: _DTypeLike[_ScalarT], sparse: L[False] = False
) -> _nt.Array[_ScalarT]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d, dtype: _DTypeLike[_ScalarT], sparse: L[True]
) -> tuple[_nt.Array[_ScalarT], ...]: ...
@overload
def indices(dimensions: _nt.ToInteger_1d, dtype: DTypeLike = ..., sparse: L[False] = False) -> _nt.Array: ...
@overload
def indices(dimensions: _nt.ToInteger_1d, dtype: DTypeLike, sparse: L[True]) -> tuple[_nt.Array, ...]: ...
@overload
def indices(dimensions: _nt.ToInteger_1d, dtype: DTypeLike = ..., *, sparse: L[True]) -> tuple[_nt.Array, ...]: ...

#
def fromfunction(
    function: Callable[..., _T],
    shape: Sequence[int],
    *,
    dtype: DTypeLike = ...,
    like: _SupportsArrayFunc | None = None,
    **kwargs: object,
) -> _T: ...

#
def isscalar(element: object) -> TypeIs[np.generic | _PyScalar]: ...

#
def binary_repr(num: SupportsIndex, width: int | None = None) -> str: ...
def base_repr(number: SupportsAbs[float], base: float = 2, padding: SupportsIndex = 0) -> str: ...

#
@overload
def identity(n: int, dtype: None = None, *, like: _SupportsArrayFunc | None = None) -> _nt.Array2D[np.float64]: ...
@overload
def identity(
    n: int, dtype: _DTypeLike[_ScalarT], *, like: _SupportsArrayFunc | None = None
) -> _nt.Array2D[_ScalarT]: ...
@overload
def identity(n: int, dtype: DTypeLike, *, like: _SupportsArrayFunc | None = None) -> _nt.Array2D: ...

#
def allclose(
    a: ArrayLike, b: ArrayLike, rtol: ArrayLike = ..., atol: ArrayLike = ..., equal_nan: py_bool = ...
) -> py_bool: ...

#
@overload
def isclose(
    a: _nt.ToGeneric_0d,
    b: _nt.ToGeneric_0d,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> np.bool: ...
@overload
def isclose(
    a: _nt.ToGeneric_1nd,
    b: _nt.ToGeneric_nd,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> _nt.Array[np.bool]: ...
@overload
def isclose(
    a: _nt.ToGeneric_nd,
    b: _nt.ToGeneric_1nd,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> _nt.Array[np.bool]: ...

#
def array_equal(a1: ArrayLike, a2: ArrayLike, equal_nan: py_bool = False) -> py_bool: ...
def array_equiv(a1: ArrayLike, a2: ArrayLike) -> py_bool: ...

#
@overload
def astype(
    x: _nt.Array[Any, _ShapeT],
    dtype: _DTypeLike[_ScalarT],
    /,
    *,
    copy: py_bool = True,
    device: _Device | None = None,
) -> ndarray[_ShapeT, dtype[_ScalarT]]: ...
@overload
def astype(
    x: _nt.Array[Any, _ShapeT],
    dtype: DTypeLike,
    /,
    *,
    copy: py_bool = True,
    device: _Device | None = None,
) -> ndarray[_ShapeT, dtype]: ...
