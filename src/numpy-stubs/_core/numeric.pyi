from builtins import bool as py_bool
from collections.abc import Callable, Sequence
from typing import Any, Final, Literal as L, NoReturn, Protocol, SupportsAbs, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeIs, TypeVar

import numpy as np
import numpy.typing as npt
from _numtype import (
    Array,
    Array0D,
    Array1D,
    Array2D,
    Array3D,
    CoComplex_1d,
    CoComplex_1nd,
    CoComplex_nd,
    CoFloating_1d,
    CoFloating_1nd,
    CoFloating_nd,
    CoInt64_1d,
    CoInt64_1nd,
    CoInt64_nd,
    CoTimeDelta_1d,
    CoTimeDelta_1nd,
    CoTimeDelta_nd,
    CoUInt64_1d,
    CoUInt64_1nd,
    CoUInt64_nd,
    JustComplex,
    JustFloat,
    JustInt,
    ToBool_0d,
    ToBool_1d,
    ToBool_1ds,
    ToBool_1nd,
    ToBool_2ds,
    ToBool_3ds,
    ToBool_nd,
    ToComplex128_0d,
    ToComplex128_1ds,
    ToComplex128_2ds,
    ToComplex128_3ds,
    ToComplex128_nd,
    ToComplex_1d,
    ToComplex_1nd,
    ToComplex_nd,
    ToFloat64_0d,
    ToFloat64_1ds,
    ToFloat64_2ds,
    ToFloat64_3ds,
    ToFloat64_nd,
    ToFloating_1d,
    ToFloating_1nd,
    ToFloating_nd,
    ToGeneric_0d,
    ToGeneric_1nd,
    ToGeneric_nd,
    ToIntP_0d,
    ToIntP_1ds,
    ToIntP_2ds,
    ToIntP_3ds,
    ToIntP_nd,
    ToInteger_1d,
    ToObject_1d,
    ToObject_1nd,
    ToObject_nd,
    ToSInteger_1d,
    ToSInteger_1nd,
    ToSInteger_nd,
    ToTimeDelta_1d,
    ToTimeDelta_1nd,
    ToTimeDelta_nd,
    ToUInteger_1d,
    ToUInteger_1nd,
    ToUInteger_nd,
)
from numpy import _AnyShapeT, _OrderCF, _OrderKACF, ufunc  # noqa: ICN003
from numpy._typing import ArrayLike, DTypeLike, _ArrayLike, _DTypeLike, _ShapeLike, _SupportsArrayFunc, _SupportsDType
from numpy._typing._char_codes import _BoolCodes, _Complex128Codes, _Float64Codes, _IntPCodes
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
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_ShapeLike1D: TypeAlias = SupportsIndex | tuple[SupportsIndex]
_ShapeLike2D: TypeAlias = tuple[SupportsIndex, SupportsIndex]
_ShapeLike3D: TypeAlias = tuple[SupportsIndex, SupportsIndex, SupportsIndex]

_DTypeLikeBool: TypeAlias = type[bool] | _DTypeLike[np.bool] | _BoolCodes
_DTypeLikeIntP: TypeAlias = type[JustInt] | _IntPCodes
_DTypeLikeFloat64: TypeAlias = type[JustFloat] | _DTypeLike[np.float64] | _Float64Codes | None
_DTypeLikeComplex128: TypeAlias = type[JustComplex] | _DTypeLike[np.complex128] | _Complex128Codes

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
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.float64]: ...
@overload  # 1d shape, known dtype
def ones(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def ones(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def ones(
    shape: _ShapeLike1D,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D: ...
@overload  # known shape, default dtype (float64)
def ones(
    shape: _AnyShapeT,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64, _AnyShapeT]: ...
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
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, unknown scalar-type
def ones(
    shape: _AnyShapeT,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, default dtype
def ones(
    shape: _ShapeLike,
    dtype: _DTypeLikeFloat64 = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64]: ...
@overload  # unknown shape, known dtype
def ones(
    shape: _ShapeLike,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def ones(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def ones(
    shape: _ShapeLike,
    dtype: npt.DTypeLike = ...,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array: ...

# NOTE: keep in sync with `ones` (but note that `full` has 18 additional overloads)
# NOTE: The mypy [overload-overlap] errors are false-positives that are caused by a
#   bug that's related to constrained type-vars.
@overload  # 1d shape, known fill scalar-type
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike1D,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[_ScalarT]: ...
@overload  # 1d shape, bool fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike1D,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.bool]: ...
@overload  # 1d shape, int fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike1D,
    fill_value: JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.intp]: ...
@overload  # 1d shape, float fill
def full(
    shape: _ShapeLike1D,
    fill_value: JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.float64]: ...
@overload  # 1d shape, complex fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike1D,
    fill_value: JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.complex128]: ...
@overload  # 1d shape, known dtype
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[tuple[int], _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[_ScalarT]: ...
@overload  # 1d shape, float64 dtype
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: _DTypeLikeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D[np.float64]: ...
@overload  # 1d shape, unknown dtype
def full(
    shape: _ShapeLike1D,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array1D: ...
@overload  # known shape, known fill scalar-type
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, bool fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.bool, _AnyShapeT]: ...
@overload  # known shape, int fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.intp, _AnyShapeT]: ...
@overload  # known shape, float fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, complex fill
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.complex128, _AnyShapeT]: ...
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
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # known shape, float64
def full(  # type: ignore[overload-overlap]
    shape: _AnyShapeT,
    fill_value: object,
    dtype: _DTypeLikeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64, _AnyShapeT]: ...
@overload  # known shape, unknown dtype
def full(
    shape: _AnyShapeT,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, known fill scalar-type
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike,
    fill_value: _ScalarT,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[_ScalarT]: ...
@overload  # unknown shape, bool fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike,
    fill_value: py_bool,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.bool]: ...
@overload  # unknown shape, int fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike,
    fill_value: JustInt,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.intp]: ...
@overload  # unknown shape, float fill
def full(
    shape: _ShapeLike,
    fill_value: JustFloat,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64]: ...
@overload  # unknown shape, complex fill
def full(  # type: ignore[overload-overlap]
    shape: _ShapeLike,
    fill_value: JustComplex,
    dtype: None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.complex128]: ...
@overload  # unknown shape, known dtype
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[_ScalarT]: ...
@overload  # unknown shape, float64
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: _DTypeLikeFloat64,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array[np.float64]: ...
@overload  # unknown shape, unknown dtype
def full(
    shape: _ShapeLike,
    fill_value: object,
    dtype: DTypeLike | None = None,
    order: _OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _SupportsArrayFunc | None = None,
) -> Array: ...

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
    a: ToBool_0d,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def zeros_like(
    a: ToBool_1ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def zeros_like(
    a: ToBool_2ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def zeros_like(
    a: ToBool_3ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.bool_]: ...
@overload  # int 0d array-like
def zeros_like(
    a: ToIntP_0d,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.intp]: ...
@overload  # int 1d array-like
def zeros_like(
    a: ToIntP_1ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.intp]: ...
@overload  # int 2d array-like
def zeros_like(
    a: ToIntP_2ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.intp]: ...
@overload  # int 3d array-like
def zeros_like(
    a: ToIntP_3ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.intp]: ...
@overload  # float 0d array-like
def zeros_like(
    a: ToFloat64_0d,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.float64]: ...
@overload  # float 1d array-like
def zeros_like(
    a: ToFloat64_1ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.float64]: ...
@overload  # float 2d array-like
def zeros_like(
    a: ToFloat64_2ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.float64]: ...
@overload  # float 3d array-like
def zeros_like(
    a: ToFloat64_3ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.float64]: ...
@overload  # complex 0d array-like
def zeros_like(
    a: ToComplex128_0d,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def zeros_like(
    a: ToComplex128_1ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def zeros_like(
    a: ToComplex128_2ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def zeros_like(
    a: ToComplex128_3ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def zeros_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def zeros_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
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
def zeros_like(  # type: ignore[overload-overlap]
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # given shape, given scalar-type
def zeros_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def zeros_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
@overload  # bool array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: ToBool_nd,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.bool_]: ...
@overload  # int array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: ToIntP_nd,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.intp]: ...
@overload  # float array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: ToFloat64_nd,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.float64]: ...
@overload  # complex array-like
def zeros_like(  # type: ignore[overload-overlap]
    a: ToComplex128_nd,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def zeros_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def zeros_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array: ...

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
    a: ToBool_0d,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def ones_like(
    a: ToBool_1ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def ones_like(
    a: ToBool_2ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def ones_like(
    a: ToBool_3ds,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.bool_]: ...
@overload  # int 0d array-like
def ones_like(
    a: ToIntP_0d,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.intp]: ...
@overload  # int 1d array-like
def ones_like(
    a: ToIntP_1ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.intp]: ...
@overload  # int 2d array-like
def ones_like(
    a: ToIntP_2ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.intp]: ...
@overload  # int 3d array-like
def ones_like(
    a: ToIntP_3ds,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.intp]: ...
@overload  # float 0d array-like
def ones_like(
    a: ToFloat64_0d,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.float64]: ...
@overload  # float 1d array-like
def ones_like(
    a: ToFloat64_1ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.float64]: ...
@overload  # float 2d array-like
def ones_like(
    a: ToFloat64_2ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.float64]: ...
@overload  # float 3d array-like
def ones_like(
    a: ToFloat64_3ds,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.float64]: ...
@overload  # complex 0d array-like
def ones_like(
    a: ToComplex128_0d,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def ones_like(
    a: ToComplex128_1ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def ones_like(
    a: ToComplex128_2ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def ones_like(
    a: ToComplex128_3ds,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def ones_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def ones_like(  # type: ignore[overload-overlap]
    a: _ArrayLike[_ScalarT],
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
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
def ones_like(  # type: ignore[overload-overlap]
    a: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
@overload  # given shape, given scalar-type
def ones_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[_ScalarT, _AnyShapeT]: ...
@overload  # unknown shape, given scalar-type
def ones_like(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[_ScalarT]: ...
@overload  # bool array-like
def ones_like(  # type: ignore[overload-overlap]
    a: ToBool_nd,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.bool_]: ...
@overload  # int array-like
def ones_like(  # type: ignore[overload-overlap]
    a: ToIntP_nd,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.intp]: ...
@overload  # float array-like
def ones_like(  # type: ignore[overload-overlap]
    a: ToFloat64_nd,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.float64]: ...
@overload  # complex array-like
def ones_like(  # type: ignore[overload-overlap]
    a: ToComplex128_nd,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def ones_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    *,
    shape: _AnyShapeT,
    device: _Device | None = None,
) -> Array[Any, _AnyShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def ones_like(
    a: object,
    dtype: npt.DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array: ...

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
    a: ToBool_0d,
    fill_value: object,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.bool_]: ...
@overload  # bool 1d array-like
def full_like(
    a: ToBool_1ds,
    fill_value: object,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.bool_]: ...
@overload  # bool 2d array-like
def full_like(
    a: ToBool_2ds,
    fill_value: object,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.bool_]: ...
@overload  # bool 3d array-like
def full_like(
    a: ToBool_3ds,
    fill_value: object,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.bool_]: ...
@overload  # int 0d array-like
def full_like(
    a: ToIntP_0d,
    fill_value: object,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.intp]: ...
@overload  # int 1d array-like
def full_like(
    a: ToIntP_1ds,
    fill_value: object,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.intp]: ...
@overload  # int 2d array-like
def full_like(
    a: ToIntP_2ds,
    fill_value: object,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.intp]: ...
@overload  # int 3d array-like
def full_like(
    a: ToIntP_3ds,
    fill_value: object,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.intp]: ...
@overload  # float 0d array-like
def full_like(
    a: ToFloat64_0d,
    fill_value: object,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.float64]: ...
@overload  # float 1d array-like
def full_like(
    a: ToFloat64_1ds,
    fill_value: object,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.float64]: ...
@overload  # float 2d array-like
def full_like(
    a: ToFloat64_2ds,
    fill_value: object,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.float64]: ...
@overload  # float 3d array-like
def full_like(
    a: ToFloat64_3ds,
    fill_value: object,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.float64]: ...
@overload  # complex 0d array-like
def full_like(
    a: ToComplex128_0d,
    fill_value: object,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> Array0D[np.complex128]: ...
@overload  # complex 1d array-like
def full_like(
    a: ToComplex128_1ds,
    fill_value: object,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> Array1D[np.complex128]: ...
@overload  # complex 2d array-like
def full_like(
    a: ToComplex128_2ds,
    fill_value: object,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> Array2D[np.complex128]: ...
@overload  # complex 3d array-like
def full_like(
    a: ToComplex128_3ds,
    fill_value: object,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> Array3D[np.complex128]: ...
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
) -> Array[_ScalarT, _AnyShapeT]: ...
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
) -> Array[_ScalarT]: ...
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
def full_like(  # type: ignore[overload-overlap]
    a: object,
    fill_value: object,
    dtype: _DTypeT | _SupportsDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> np.ndarray[tuple[int, ...], _DTypeT]: ...
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
) -> Array[_ScalarT, _AnyShapeT]: ...
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
) -> Array[_ScalarT]: ...
@overload  # bool array-like
def full_like(  # type: ignore[overload-overlap]
    a: ToBool_nd,
    fill_value: object,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.bool_]: ...
@overload  # int array-like
def full_like(  # type: ignore[overload-overlap]
    a: ToIntP_nd,
    fill_value: object,
    dtype: _DTypeLikeIntP | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.intp]: ...
@overload  # float array-like
def full_like(  # type: ignore[overload-overlap]
    a: ToFloat64_nd,
    fill_value: object,
    dtype: _DTypeLikeFloat64 = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.float64]: ...
@overload  # complex array-like
def full_like(  # type: ignore[overload-overlap]
    a: ToComplex128_nd,
    fill_value: object,
    dtype: _DTypeLikeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: py_bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> Array[np.complex128]: ...
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
) -> Array[Any, _AnyShapeT]: ...
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
) -> Array: ...

#
@overload
def count_nonzero(a: ArrayLike, axis: None = None, *, keepdims: L[False] = False) -> int: ...
@overload
def count_nonzero(a: ArrayLike, axis: _ShapeLike | None = None, *, keepdims: py_bool = False) -> Any: ...

#
def flatnonzero(a: ArrayLike) -> Array1D[np.intp]: ...
def argwhere(a: ArrayLike) -> Array[np.intp]: ...

#
def isfortran(a: Array | np.generic) -> py_bool: ...

#
@overload
def correlate(a: ToBool_1d, v: ToBool_1d, mode: _Mode = "valid") -> Array1D[np.bool]: ...
@overload
def correlate(a: ToUInteger_1d, v: CoUInt64_1d, mode: _Mode = "valid") -> Array1D[np.unsignedinteger]: ...
@overload
def correlate(a: CoUInt64_1d, v: ToUInteger_1d, mode: _Mode = "valid") -> Array1D[np.unsignedinteger]: ...  #
@overload
def correlate(a: ToSInteger_1d, v: CoInt64_1d, mode: _Mode = "valid") -> Array1D[np.signedinteger]: ...
@overload
def correlate(a: CoInt64_1d, v: ToSInteger_1d, mode: _Mode = "valid") -> Array1D[np.signedinteger]: ...
@overload
def correlate(a: ToFloating_1d, v: CoFloating_1d, mode: _Mode = "valid") -> Array1D[np.floating]: ...
@overload
def correlate(a: CoFloating_1d, v: ToFloating_1d, mode: _Mode = "valid") -> Array1D[np.floating]: ...
@overload
def correlate(a: ToComplex_1d, v: CoComplex_1d, mode: _Mode = "valid") -> Array1D[np.complexfloating]: ...
@overload
def correlate(a: CoComplex_1d, v: ToComplex_1d, mode: _Mode = "valid") -> Array1D[np.complexfloating]: ...
@overload
def correlate(a: ToTimeDelta_1d, v: CoTimeDelta_1d, mode: _Mode = "valid") -> Array1D[np.timedelta64]: ...
@overload
def correlate(a: CoTimeDelta_1d, v: ToTimeDelta_1d, mode: _Mode = "valid") -> Array1D[np.timedelta64]: ...
@overload
def correlate(a: ToObject_1d, v: ToObject_1d, mode: _Mode = "valid") -> Array1D[np.object_]: ...
@overload
def correlate(
    a: CoComplex_1d | CoTimeDelta_1d | ToObject_1d,
    v: CoComplex_1d | CoTimeDelta_1d | ToObject_1d,
    mode: _Mode = "valid",
) -> Array1D[Any]: ...

#
@overload
def convolve(a: ToBool_1d, v: ToBool_1d, mode: _Mode = "valid") -> Array1D[np.bool]: ...
@overload
def convolve(a: ToUInteger_1d, v: CoUInt64_1d, mode: _Mode = "valid") -> Array1D[np.unsignedinteger]: ...
@overload
def convolve(a: CoUInt64_1d, v: ToUInteger_1d, mode: _Mode = "valid") -> Array1D[np.unsignedinteger]: ...
@overload
def convolve(a: ToSInteger_1d, v: CoInt64_1d, mode: _Mode = "valid") -> Array1D[np.signedinteger]: ...
@overload
def convolve(a: CoInt64_1d, v: ToSInteger_1d, mode: _Mode = "valid") -> Array1D[np.signedinteger]: ...
@overload
def convolve(a: ToFloating_1d, v: CoFloating_1d, mode: _Mode = "valid") -> Array1D[np.floating]: ...
@overload
def convolve(a: CoFloating_1d, v: ToFloating_1d, mode: _Mode = "valid") -> Array1D[np.floating]: ...
@overload
def convolve(a: ToComplex_1d, v: CoComplex_1d, mode: _Mode = "valid") -> Array1D[np.complexfloating]: ...
@overload
def convolve(a: CoComplex_1d, v: ToComplex_1d, mode: _Mode = "valid") -> Array1D[np.complexfloating]: ...
@overload
def convolve(a: ToTimeDelta_1d, v: CoTimeDelta_1d, mode: _Mode = "valid") -> Array1D[np.timedelta64]: ...
@overload
def convolve(a: CoTimeDelta_1d, v: ToTimeDelta_1d, mode: _Mode = "valid") -> Array1D[np.timedelta64]: ...
@overload
def convolve(a: ToObject_1d, v: ToObject_1d, mode: _Mode = "valid") -> Array1D[np.object_]: ...
@overload
def convolve(
    a: CoComplex_1d | CoTimeDelta_1d | ToObject_1d,
    v: CoComplex_1d | CoTimeDelta_1d | ToObject_1d,
    mode: _Mode = "valid",
) -> Array1D[Any]: ...

#
@overload
def outer(a: ToBool_nd, b: ToBool_nd, out: None = None) -> Array2D[np.bool]: ...
@overload
def outer(a: ToUInteger_nd, b: CoUInt64_nd, out: None = None) -> Array2D[np.unsignedinteger]: ...
@overload
def outer(a: CoUInt64_nd, b: ToUInteger_nd, out: None = None) -> Array2D[np.unsignedinteger]: ...
@overload
def outer(a: ToSInteger_nd, b: CoInt64_nd, out: None = None) -> Array2D[np.signedinteger]: ...
@overload
def outer(a: CoInt64_nd, b: ToSInteger_nd, out: None = None) -> Array2D[np.signedinteger]: ...
@overload
def outer(a: ToFloating_nd, b: CoFloating_nd, out: None = None) -> Array2D[np.floating]: ...
@overload
def outer(a: CoFloating_nd, b: ToFloating_nd, out: None = None) -> Array2D[np.floating]: ...
@overload
def outer(a: ToComplex_nd, b: CoComplex_nd, out: None = None) -> Array2D[np.complexfloating]: ...
@overload
def outer(a: CoComplex_nd, b: ToComplex_nd, out: None = None) -> Array2D[np.complexfloating]: ...
@overload
def outer(a: ToTimeDelta_nd, b: CoTimeDelta_nd, out: None = None) -> Array2D[np.timedelta64]: ...
@overload
def outer(a: CoTimeDelta_nd, b: ToTimeDelta_nd, out: None = None) -> Array2D[np.timedelta64]: ...
@overload
def outer(a: ToObject_nd, b: ToObject_nd, out: None = None) -> Array2D[np.object_]: ...
@overload
def outer(
    a: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    b: CoComplex_nd | CoTimeDelta_nd | ToObject_nd,
    out: _ArrayT,
) -> _ArrayT: ...

#
@overload
def tensordot(a: ToBool_1nd, b: ToBool_1nd, axes: _Axes = 2) -> Array[np.bool]: ...
@overload
def tensordot(a: ToUInteger_1nd, b: CoUInt64_1nd, axes: _Axes = 2) -> Array[np.unsignedinteger]: ...
@overload
def tensordot(a: CoUInt64_1nd, b: ToUInteger_1nd, axes: _Axes = 2) -> Array[np.unsignedinteger]: ...
@overload
def tensordot(a: ToSInteger_1nd, b: CoInt64_1nd, axes: _Axes = 2) -> Array[np.signedinteger]: ...
@overload
def tensordot(a: CoInt64_1nd, b: ToSInteger_1nd, axes: _Axes = 2) -> Array[np.signedinteger]: ...
@overload
def tensordot(a: ToFloating_1nd, b: CoFloating_1nd, axes: _Axes = 2) -> Array[np.floating]: ...
@overload
def tensordot(a: CoFloating_1nd, b: ToFloating_1nd, axes: _Axes = 2) -> Array[np.floating]: ...
@overload
def tensordot(a: ToComplex_1nd, b: CoComplex_1nd, axes: _Axes = 2) -> Array[np.complexfloating]: ...
@overload
def tensordot(a: CoComplex_1nd, b: ToComplex_1nd, axes: _Axes = 2) -> Array[np.complexfloating]: ...
@overload
def tensordot(a: ToTimeDelta_1nd, b: CoTimeDelta_1nd, axes: _Axes = 2) -> Array[np.timedelta64]: ...
@overload
def tensordot(a: CoTimeDelta_1nd, b: ToTimeDelta_1nd, axes: _Axes = 2) -> Array[np.timedelta64]: ...
@overload
def tensordot(a: ToObject_1nd, b: ToObject_1nd, axes: _Axes = 2) -> Array[np.object_]: ...
@overload
def tensordot(
    a: CoComplex_1nd | CoTimeDelta_1nd | ToObject_1nd,
    b: CoComplex_1nd | CoTimeDelta_1nd | ToObject_1nd,
    axes: _Axes = 2,
) -> Array[Any]: ...

#
@overload
def roll(a: _ArrayLike[_ScalarT], shift: _ShapeLike, axis: _ShapeLike | None = None) -> Array[_ScalarT]: ...
@overload
def roll(a: ArrayLike, shift: _ShapeLike, axis: _ShapeLike | None = None) -> Array: ...

#
def rollaxis(a: Array[_ScalarT], axis: int, start: int = ...) -> Array[_ScalarT]: ...
def moveaxis(a: Array[_ScalarT], source: _ShapeLike, destination: _ShapeLike) -> Array[_ScalarT]: ...

#
@overload
def cross(
    a: ToBool_1nd,
    b: ToBool_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> NoReturn: ...
@overload
def cross(
    a: ToUInteger_1nd,
    b: CoUInt64_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.unsignedinteger]: ...
@overload
def cross(
    a: CoUInt64_1nd,
    b: ToUInteger_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.unsignedinteger]: ...
@overload
def cross(
    a: ToSInteger_1nd,
    b: CoInt64_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.signedinteger]: ...
@overload
def cross(
    a: CoInt64_1nd,
    b: ToSInteger_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.signedinteger]: ...
@overload
def cross(
    a: ToFloating_1nd,
    b: CoFloating_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.floating]: ...
@overload
def cross(
    a: CoFloating_1nd,
    b: ToFloating_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.floating]: ...
@overload
def cross(
    a: ToComplex_1nd,
    b: CoComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.complexfloating]: ...
@overload
def cross(
    a: CoComplex_1nd,
    b: ToComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[np.complexfloating]: ...
@overload
def cross(
    a: CoComplex_1nd,
    b: CoComplex_1nd,
    axisa: int = -1,
    axisb: int = -1,
    axisc: int = -1,
    axis: int | None = None,
) -> Array[Any]: ...

#
@overload
def indices(dimensions: ToInteger_1d, dtype: type[JustInt] = ..., sparse: L[False] = False) -> Array[np.intp]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: type[JustInt], sparse: L[True]) -> tuple[Array[np.intp], ...]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: type[JustInt] = ..., *, sparse: L[True]) -> tuple[Array[np.intp], ...]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: _DTypeLike[_ScalarT], sparse: L[False] = False) -> Array[_ScalarT]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: _DTypeLike[_ScalarT], sparse: L[True]) -> tuple[Array[_ScalarT], ...]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: DTypeLike = ..., sparse: L[False] = False) -> Array: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: DTypeLike, sparse: L[True]) -> tuple[Array, ...]: ...
@overload
def indices(dimensions: ToInteger_1d, dtype: DTypeLike = ..., *, sparse: L[True]) -> tuple[Array, ...]: ...

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
def identity(n: int, dtype: None = None, *, like: _SupportsArrayFunc | None = None) -> Array2D[np.float64]: ...
@overload
def identity(n: int, dtype: _DTypeLike[_ScalarT], *, like: _SupportsArrayFunc | None = None) -> Array2D[_ScalarT]: ...
@overload
def identity(n: int, dtype: DTypeLike, *, like: _SupportsArrayFunc | None = None) -> Array2D: ...

#
def allclose(a: ArrayLike, b: ArrayLike, rtol: ArrayLike = ..., atol: ArrayLike = ..., equal_nan: py_bool = ...) -> py_bool: ...

#
@overload
def isclose(
    a: ToGeneric_0d,
    b: ToGeneric_0d,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> np.bool: ...
@overload
def isclose(
    a: ToGeneric_1nd,
    b: ToGeneric_nd,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> Array[np.bool]: ...
@overload
def isclose(
    a: ToGeneric_nd,
    b: ToGeneric_1nd,
    rtol: ArrayLike = 1e-5,
    atol: ArrayLike = 1e-8,
    equal_nan: py_bool = False,
) -> Array[np.bool]: ...

#
def array_equal(a1: ArrayLike, a2: ArrayLike, equal_nan: py_bool = False) -> py_bool: ...
def array_equiv(a1: ArrayLike, a2: ArrayLike) -> py_bool: ...

#
@overload
def astype(
    x: Array[Any, _ShapeT],
    dtype: _DTypeLike[_ScalarT],
    /,
    *,
    copy: py_bool = True,
    device: _Device | None = None,
) -> ndarray[_ShapeT, dtype[_ScalarT]]: ...
@overload
def astype(
    x: Array[Any, _ShapeT],
    dtype: DTypeLike,
    /,
    *,
    copy: py_bool = True,
    device: _Device | None = None,
) -> ndarray[_ShapeT, dtype]: ...
