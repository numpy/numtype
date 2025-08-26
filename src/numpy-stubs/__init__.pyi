import ctypes as ct
import datetime as dt
import sys
from _typeshed import Incomplete, StrOrBytesPath, SupportsFlush, SupportsLenAndGetItem, SupportsWrite
from builtins import bool as py_bool
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from types import EllipsisType, GenericAlias, GetSetDescriptorType, MappingProxyType, ModuleType
from typing import (
    Any,
    ClassVar,
    Concatenate,
    Final,
    Generic,
    Literal as L,
    LiteralString,
    Never,
    Self,
    SupportsAbs,
    SupportsComplex as CanComplex,
    SupportsFloat as CanFloat,
    SupportsIndex as CanIndex,
    SupportsInt as CanInt,
    TypeAlias,
    TypedDict,
    final,
    overload,
    type_check_only,
)
from typing_extensions import Buffer, CapsuleType, Protocol, TypeVar, deprecated, override

import _numtype as _nt

from . import (
    __config__ as __config__,
    _array_api_info as _array_api_info,
    _core as _core,
    _globals as _globals,
    _typing as _typing,
    char,
    core,
    ctypeslib,
    dtypes,
    exceptions,
    f2py,
    fft,
    lib,
    linalg,
    ma,
    matlib as matlib,
    matrixlib as matrixlib,
    polynomial,
    random,
    rec,
    strings,
    testing,
    typing,
    version as version,
)
from .__config__ import show as show_config
from ._array_api_info import __array_namespace_info__
from ._core import (
    False_,
    ScalarType,
    True_,
    all,
    allclose,
    amax,
    amin,
    any,
    arange,
    argmax,
    argmin,
    argpartition,
    argsort,
    argwhere,
    around,
    array,
    array2string,
    array_equal,
    array_equiv,
    array_repr,
    array_str,
    asanyarray,
    asarray,
    ascontiguousarray,
    asfortranarray,
    astype,
    atleast_1d,
    atleast_2d,
    atleast_3d,
    base_repr,
    binary_repr,
    block,
    broadcast,
    busday_count,
    busday_offset,
    busdaycalendar,
    can_cast,
    choose,
    clip,
    compress,
    concat,
    concatenate,
    convolve,
    copyto,
    correlate,
    count_nonzero,
    cross,
    cumprod,
    cumsum,
    cumulative_prod,
    cumulative_sum,
    datetime_as_string,
    datetime_data,
    diagonal,
    dot,
    e,
    einsum,
    einsum_path,
    empty,
    empty_like,
    euler_gamma,
    finfo,
    flatiter,
    flatnonzero,
    format_float_positional,
    format_float_scientific,
    from_dlpack,
    frombuffer,
    fromfile,
    fromfunction,
    fromiter,
    frompyfunc,
    fromstring,
    full,
    full_like,
    geomspace,
    get_printoptions,
    getbufsize,
    geterr,
    geterrcall,
    hstack,
    identity,
    iinfo,
    indices,
    inf,
    inner,
    is_busday,
    isclose,
    isdtype,
    isfortran,
    isscalar,
    issubdtype,
    lexsort,
    linspace,
    little_endian,
    logspace,
    matrix_transpose,
    max,
    may_share_memory,
    mean,
    min,
    min_scalar_type,
    moveaxis,
    nan,
    ndim,
    nditer,
    nested_iters,
    newaxis,
    nonzero,
    ones,
    ones_like,
    outer,
    partition,
    permute_dims,
    pi,
    printoptions,
    prod,
    promote_types,
    ptp,
    put,
    putmask,
    ravel,
    recarray,
    record,
    repeat,
    require,
    reshape,
    resize,
    result_type,
    roll,
    rollaxis,
    round,
    sctypeDict,
    searchsorted,
    set_printoptions,
    setbufsize,
    seterr,
    seterrcall,
    shape,
    shares_memory,
    size,
    sort,
    squeeze,
    stack,
    std,
    sum,
    swapaxes,
    take,
    tensordot,
    trace,
    transpose,
    typecodes,
    unstack,
    var,
    vdot,
    vstack,
    where,
    zeros,
    zeros_like,
)
from ._core._internal import _ctypes
from ._core._ufunc_config import errstate
from ._core.memmap import memmap
from ._core.multiarray import bincount, flagsobj, packbits, unpackbits
from ._core.umath import (
    absolute,
    absolute as abs,
    add,
    arccos,
    arccos as acos,
    arccosh,
    arccosh as acosh,
    arcsin,
    arcsin as asin,
    arcsinh,
    arcsinh as asinh,
    arctan,
    arctan as atan,
    arctan2,
    arctan2 as atan2,
    arctanh,
    arctanh as atanh,
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
    equal,
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
    gcd,
    greater,
    greater_equal,
    heaviside,
    hypot,
    invert,
    invert as bitwise_invert,
    invert as bitwise_not,
    isfinite,
    isinf,
    isnan,
    isnat,
    lcm,
    ldexp,
    left_shift,
    left_shift as bitwise_left_shift,
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
    matmul,
    matvec,
    maximum,
    minimum,
    mod,
    modf,
    multiply,
    negative,
    nextafter,
    not_equal,
    positive,
    power,
    power as pow,
    rad2deg,
    radians,
    reciprocal,
    remainder,
    right_shift,
    right_shift as bitwise_right_shift,
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
from ._expired_attrs_2_0 import __expired_attributes__ as __expired_attributes__
from ._globals import _CopyMode as _CopyMode, _NoValue as _NoValue
from ._pytesttester import PytestTester
from ._typing import (
    ArrayLike,
    DTypeLike,
    _ArrayLikeDT64_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
    _DTypeLike,
    _DTypeLikeVoid,
    _NestedSequence,
    _NumberLike_co,
    _ScalarLike_co,
    _ShapeLike,
    _TD64Like_co,
)
from .lib import scimath as emath
from .lib._arraypad_impl import pad
from .lib._arraysetops_impl import (
    ediff1d,
    in1d,
    intersect1d,
    isin,
    setdiff1d,
    setxor1d,
    union1d,
    unique,
    unique_all,
    unique_counts,
    unique_inverse,
    unique_values,
)
from .lib._function_base_impl import (
    angle,
    append,
    asarray_chkfinite,
    average,
    bartlett,
    blackman,
    copy,
    corrcoef,
    cov,
    delete,
    diff,
    digitize,
    extract,
    flip,
    gradient,
    hamming,
    hanning,
    i0,
    insert,
    interp,
    iterable,
    kaiser,
    median,
    meshgrid,
    percentile,
    piecewise,
    place,
    quantile,
    rot90,
    select,
    sinc,
    sort_complex,
    trapezoid,
    trapz,
    trim_zeros,
    unwrap,
    vectorize,
)
from .lib._histograms_impl import histogram, histogram_bin_edges, histogramdd
from .lib._index_tricks_impl import (
    c_,
    diag_indices,
    diag_indices_from,
    fill_diagonal,
    index_exp,
    ix_,
    mgrid,
    ndenumerate,
    ndindex,
    ogrid,
    r_,
    ravel_multi_index,
    s_,
    unravel_index,
)
from .lib._nanfunctions_impl import (
    nanargmax,
    nanargmin,
    nancumprod,
    nancumsum,
    nanmax,
    nanmean,
    nanmedian,
    nanmin,
    nanpercentile,
    nanprod,
    nanquantile,
    nanstd,
    nansum,
    nanvar,
)
from .lib._npyio_impl import fromregex, genfromtxt, load, loadtxt, save, savetxt, savez, savez_compressed
from .lib._polynomial_impl import (
    poly,
    poly1d,
    polyadd,
    polyder,
    polydiv,
    polyfit,
    polyint,
    polymul,
    polysub,
    polyval,
    roots,
)
from .lib._shape_base_impl import (
    apply_along_axis,
    apply_over_axes,
    array_split,
    column_stack,
    dsplit,
    dstack,
    expand_dims,
    hsplit,
    kron,
    put_along_axis,
    row_stack,
    split,
    take_along_axis,
    tile,
    vsplit,
)
from .lib._stride_tricks_impl import broadcast_arrays, broadcast_shapes, broadcast_to
from .lib._twodim_base_impl import (
    diag,
    diagflat,
    eye,
    fliplr,
    flipud,
    histogram2d,
    mask_indices,
    tri,
    tril,
    tril_indices,
    tril_indices_from,
    triu,
    triu_indices,
    triu_indices_from,
    vander,
)
from .lib._type_check_impl import (
    common_type,
    imag,
    iscomplex,
    iscomplexobj,
    isreal,
    isrealobj,
    mintypecode,
    nan_to_num,
    real,
    real_if_close,
    typename,
)
from .lib._ufunclike_impl import fix, isneginf, isposinf
from .lib._utils_impl import get_include, info, show_runtime
from .matrixlib import asmatrix, bmat, matrix
from .version import __version__

__all__ = [  # noqa: RUF022
    # __numpy_submodules__
    "char", "core", "ctypeslib", "dtypes", "exceptions", "f2py", "fft", "lib", "linalg", "ma", "polynomial", "random",
    "rec", "strings", "test", "testing", "typing",
    # _core.*
    "False_", "ScalarType", "True_", "abs", "absolute", "acos", "acosh", "add", "all", "allclose", "amax", "amin",
    "any", "arange", "arccos", "arccosh", "arcsin", "arcsinh", "arctan", "arctan2", "arctanh", "argmax", "argmin",
    "argpartition", "argsort", "argwhere", "around", "array", "array2string", "array_equal", "array_equiv",
    "array_repr", "array_str", "asanyarray", "asarray", "ascontiguousarray", "asfortranarray", "asin", "asinh",
    "astype", "atan", "atan2", "atanh", "atleast_1d", "atleast_2d", "atleast_3d", "base_repr", "binary_repr",
    "bitwise_and", "bitwise_count", "bitwise_invert", "bitwise_left_shift", "bitwise_not", "bitwise_or",
    "bitwise_right_shift", "bitwise_xor", "block", "bool", "bool_", "broadcast", "busday_count", "busday_offset",
    "busdaycalendar", "byte", "bytes_", "can_cast", "cbrt", "cdouble", "ceil", "character", "choose", "clip",
    "clongdouble", "complex64", "complex128", "complex192", "complex256", "complexfloating", "compress", "concat",
    "concatenate", "conj", "conjugate", "convolve", "copysign", "copyto", "correlate", "cos", "cosh", "count_nonzero",
    "cross", "csingle", "cumprod", "cumsum", "cumulative_prod", "cumulative_sum", "datetime64", "datetime_as_string",
    "datetime_data", "deg2rad", "degrees", "diagonal", "divide", "divmod", "dot", "double", "dtype", "e", "einsum",
    "einsum_path", "empty", "empty_like", "equal", "errstate", "euler_gamma", "exp", "exp2", "expm1", "fabs", "finfo",
    "flatiter", "flatnonzero", "flexible", "float16", "float32", "float64", "float96", "float128", "float_power",
    "floating", "floor", "floor_divide", "fmax", "fmin", "fmod", "format_float_positional", "format_float_scientific",
    "frexp", "from_dlpack", "frombuffer", "fromfile", "fromfunction", "fromiter", "frompyfunc", "fromstring", "full",
    "full_like", "gcd", "generic", "geomspace", "get_printoptions", "getbufsize", "geterr", "geterrcall", "greater",
    "greater_equal", "half", "heaviside", "hstack", "hypot", "identity", "iinfo", "indices", "inexact", "inf", "inner",
    "int8", "int16", "int32", "int64", "int_", "intc", "integer", "intp", "invert", "is_busday", "isclose", "isdtype",
    "isfinite", "isfortran", "isinf", "isnan", "isnat", "isscalar", "issubdtype", "lcm", "ldexp", "left_shift", "less",
    "less_equal", "lexsort", "linspace", "little_endian", "log", "log10", "log1p", "log2", "logaddexp", "logaddexp2",
    "logical_and", "logical_not", "logical_or", "logical_xor", "logspace", "long", "longdouble", "longlong", "matmul",
    "matrix_transpose", "matvec", "max", "maximum", "may_share_memory", "mean", "memmap", "min", "min_scalar_type",
    "minimum", "mod", "modf", "moveaxis", "multiply", "nan", "ndarray", "ndim", "nditer", "negative", "nested_iters",
    "newaxis", "nextafter", "nonzero", "not_equal", "number", "object_", "ones", "ones_like", "outer", "partition",
    "permute_dims", "pi", "positive", "pow", "power", "printoptions", "prod", "promote_types", "ptp", "put", "putmask",
    "rad2deg", "radians", "ravel", "recarray", "reciprocal", "record", "remainder", "repeat", "require", "reshape",
    "resize", "result_type", "right_shift", "rint", "roll", "rollaxis", "round", "sctypeDict", "searchsorted",
    "set_printoptions", "setbufsize", "seterr", "seterrcall", "shape", "shares_memory", "short", "sign", "signbit",
    "signedinteger", "sin", "single", "sinh", "size", "sort", "spacing", "sqrt", "square", "squeeze", "stack", "std",
    "str_", "subtract", "sum", "swapaxes", "take", "tan", "tanh", "tensordot", "timedelta64", "trace", "transpose",
    "true_divide", "trunc", "typecodes", "ubyte", "ufunc", "uint", "uint16", "uint32", "uint64", "uint64", "uint8",
    "uintc", "uintp", "ulong", "ulonglong", "unsignedinteger", "unstack", "ushort", "var", "vdot", "vecdot", "vecmat",
    "void", "vstack", "where", "zeros", "zeros_like",
    # matrixlib.*
    "matrix", "bmat", "asmatrix",
    # lib._arraypad_impl.*
    "pad",
    # lib._arraysetops_impl.*
    "ediff1d", "in1d", "intersect1d", "isin", "setdiff1d", "setxor1d", "union1d", "unique", "unique_all",
    "unique_counts", "unique_inverse", "unique_values",
    # lib._function_base_impl.*
    "angle", "append", "asarray_chkfinite", "average", "bartlett", "bincount", "blackman", "copy", "corrcoef", "cov",
    "delete", "diff", "digitize", "extract", "flip", "gradient", "hamming", "hanning", "i0", "insert", "interp",
    "iterable", "kaiser", "median", "meshgrid", "percentile", "piecewise", "place", "quantile", "rot90", "select",
    "sinc", "sort_complex", "trapezoid", "trapz", "trim_zeros", "unwrap", "vectorize",
    # lib._histograms_impl.*
    "histogram", "histogram_bin_edges", "histogramdd",
    # lib._index_tricks_impl.*
    "c_", "diag_indices", "diag_indices_from", "fill_diagonal", "index_exp", "ix_", "mgrid", "ndenumerate", "ndindex",
    "ogrid", "r_", "ravel_multi_index", "s_", "unravel_index",
    # lib._nanfunctions_impl.*
    "nanargmax", "nanargmin", "nancumprod", "nancumsum", "nanmax", "nanmean", "nanmedian", "nanmin", "nanpercentile",
    "nanprod", "nanquantile", "nanstd", "nansum", "nanvar",
    # lib._npyio_impl.*
    "fromregex", "genfromtxt", "load", "loadtxt", "packbits", "save", "savetxt", "savez", "savez_compressed",
    "unpackbits",
    # lib._polynomial_impl.*
    "poly", "poly1d", "polyadd", "polyder", "polydiv", "polyfit", "polyint", "polymul", "polysub", "polyval", "roots",
    # lib._scimath_impl
    "emath",
    # lib._shape_base_impl
    "apply_along_axis", "apply_over_axes", "array_split", "row_stack", "column_stack", "dsplit", "dstack",
    "expand_dims", "hsplit", "kron", "put_along_axis", "split", "take_along_axis", "tile", "vsplit",
    # lib._stride_tricks_impl.*
    "broadcast_arrays", "broadcast_shapes", "broadcast_to",
    # lib._twodim_base_impl
    "diag", "diagflat", "eye", "fliplr", "flipud", "histogram2d", "mask_indices", "tri", "tril", "tril_indices",
    "tril_indices_from", "triu", "triu_indices", "triu_indices_from", "vander",
    # lib._type_check_impl
    "common_type", "imag", "iscomplex", "iscomplexobj", "isreal", "isrealobj", "mintypecode", "nan_to_num", "real",
    "real_if_close", "typename",
    # lib._ufunclike_impl
    "fix", "isneginf", "isposinf",
    # lib._utils_impl
    "get_include", "info", "show_runtime",
    # __config__.*
    "show_config",
    # _array_api_info.*
    "__array_namespace_info__",
    # version.*
    "__version__",
]  # fmt: skip

###
# Constrained types (for internal use only)

_AnyShapeT = TypeVar(
    "_AnyShapeT",
    _nt.Shape0,
    _nt.Shape1,
    _nt.Shape2,
    _nt.Shape3,
    _nt.Shape4,
    _nt.Shape4N,
    _nt.Shape3N,
    _nt.Shape2N,
    _nt.Shape1N,
    _nt.Shape0N,
)
_AnyItemT = TypeVar("_AnyItemT", bool, int, float, complex, bytes, str, dt.datetime, dt.date, dt.timedelta)
_AnyNumberItemT = TypeVar("_AnyNumberItemT", int, float, complex)

###
# Type parameters (for internal use only)

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_RealT_co = TypeVar("_RealT_co", covariant=True)
_ImagT_co = TypeVar("_ImagT_co", covariant=True)

_DTypeT = TypeVar("_DTypeT", bound=dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=dtype, default=dtype, covariant=True)
_FlexDTypeT = TypeVar("_FlexDTypeT", bound=dtype[flexible])

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_IntegralArrayT = TypeVar("_IntegralArrayT", bound=_nt.Array[_nt.co_integer | object_])
_NumericArrayT = TypeVar("_NumericArrayT", bound=_nt.Array[number | timedelta64 | object_])

_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_ShapeT2 = TypeVar("_ShapeT2", bound=_nt.Shape)
# TODO(jorenham): use `Shape` instead of `AnyShape` once python/mypy#19110 is fixed
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.AnyShape, covariant=True)
_Shape1NDT = TypeVar("_Shape1NDT", bound=_nt.Shape1N)

_ScalarT = TypeVar("_ScalarT", bound=generic)
_SelfScalarT = TypeVar("_SelfScalarT", bound=generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=generic, default=Any, covariant=True)
_IntegralT = TypeVar("_IntegralT", bound=bool_ | integer | object_)
_RealScalarT = TypeVar("_RealScalarT", bound=bool_ | integer | floating | object_)
_RealNumberT = TypeVar("_RealNumberT", bound=integer | floating)
_IntegerT = TypeVar("_IntegerT", bound=integer)
_CoIntegerT = TypeVar("_CoIntegerT", bound=bool_ | integer)
_FloatingT = TypeVar("_FloatingT", bound=floating)
_CoFloatingT = TypeVar("_CoFloatingT", bound=bool_ | integer | floating)
_ComplexFloatT = TypeVar("_ComplexFloatT", bound=complexfloating)
_InexactT = TypeVar("_InexactT", bound=inexact)
_NumberT = TypeVar("_NumberT", bound=number)
_NumericT = TypeVar("_NumericT", bound=number | timedelta64)
_CoNumberT = TypeVar("_CoNumberT", bound=bool_ | number)
_CharT = TypeVar("_CharT", bound=character)
_CharDTypeT = TypeVar("_CharDTypeT", bound=dtype[character])

_ItemT_co = TypeVar("_ItemT_co", default=Any, covariant=True)
_BoolItemT_co = TypeVar("_BoolItemT_co", bound=py_bool, default=py_bool, covariant=True)
_NumberItemT_co = TypeVar("_NumberItemT_co", bound=complex, default=Any, covariant=True)
_InexactItemT_co = TypeVar("_InexactItemT_co", bound=complex, default=Any, covariant=True)
_FlexItemT_co = TypeVar(
    "_FlexItemT_co", bound=bytes | str | tuple[object, ...], default=bytes | str | tuple[Any, ...], covariant=True
)
_CharacterItemT_co = TypeVar("_CharacterItemT_co", bound=bytes | str, default=bytes | str, covariant=True)
_TD64ItemT_co = TypeVar(
    "_TD64ItemT_co", bound=dt.timedelta | int | None, default=dt.timedelta | int | None, covariant=True
)
_DT64ItemT_co = TypeVar("_DT64ItemT_co", bound=dt.date | int | None, default=dt.date | int | None, covariant=True)
_TD64UnitT = TypeVar("_TD64UnitT", bound=_TD64Unit, default=_TD64Unit)

_IntSizeT_co = TypeVar("_IntSizeT_co", bound=L[1, 2, 4, 8], covariant=True)
_FloatSizeT_co = TypeVar("_FloatSizeT_co", bound=L[2, 4, 8, 12, 16], covariant=True)

###
# Type Aliases (for internal use only)

_SubModule: TypeAlias = L[
    "char",
    "core",
    "ctypeslib",
    "dtypes",
    "exceptions",
    "f2py",
    "fft",
    "lib",
    "linalg",
    "ma",
    "polynomial",
    "random",
    "rec",
    "strings",
    "test",
    "testing",
    "typing",
]
_UFuncMethod: TypeAlias = L["__call__", "reduce", "reduceat", "accumulate", "outer", "at"]

_Tuple2: TypeAlias = tuple[_T, _T]
_IntOrInts: TypeAlias = int | tuple[int, ...]
_MetaData: TypeAlias = dict[str, Any]

_JustSignedInteger: TypeAlias = _nt.Just[signedinteger]
_JustUnsignedInteger: TypeAlias = _nt.Just[unsignedinteger]
_JustInteger: TypeAlias = _nt.Just[integer]
_JustFloating: TypeAlias = _nt.Just[floating]
_JustComplexFloating: TypeAlias = _nt.Just[complexfloating]
_JustInexact: TypeAlias = _nt.Just[inexact]
_JustNumber: TypeAlias = _nt.Just[number]
_JustBuiltinScalar: TypeAlias = int | _nt.JustFloat | _nt.JustComplex | _nt.JustBytes | _nt.JustStr

_AbstractInexact: TypeAlias = _JustInexact | _JustFloating | _JustComplexFloating
_AbstractInteger: TypeAlias = _JustInteger | _JustSignedInteger | _JustUnsignedInteger

_I32_min: TypeAlias = int32 | int64
_I16_min: TypeAlias = int16 | _I32_min
_I16_max: TypeAlias = int16 | int8
_F32_min: TypeAlias = float32 | float64 | longdouble
_F32_max: TypeAlias = float32 | float16
_F64_max: TypeAlias = float64 | _F32_max
_C128_min: TypeAlias = complex128 | clongdouble
_C128_max: TypeAlias = complex64 | complex128
_Integer32_min: TypeAlias = _nt.integer32 | _nt.integer64
_Inexact64_min: TypeAlias = _nt.inexact64 | _nt.inexact64l
_Inexact64_max: TypeAlias = _F64_max | _C128_max

_ArrayInteger_co: TypeAlias = _nt.Array[_nt.co_integer]
_ArrayComplex_co: TypeAlias = _nt.Array[_nt.co_complex]
_ArrayTD64_co: TypeAlias = _nt.Array[_nt.co_timedelta]

_ToIndex: TypeAlias = CanIndex | slice | EllipsisType | _nt.CoInteger_1nd | None
_ToIndices: TypeAlias = _ToIndex | tuple[_ToIndex, ...]

_Axis0D: TypeAlias = L[0, -1] | tuple[()]

_PyBoolND: TypeAlias = _nt.SequenceND[py_bool]
_PyCoIntND: TypeAlias = _nt.SequenceND[int]
_PyCoFloatND: TypeAlias = _nt.SequenceND[float]
_PyCoComplexND: TypeAlias = _nt.SequenceND[complex]
_PyIntND: TypeAlias = _nt.SequenceND[_nt.JustInt]
_PyFloatND: TypeAlias = _nt.SequenceND[_nt.JustFloat]
_PyComplexND: TypeAlias = _nt.SequenceND[_nt.JustComplex]

# can be anything, is case-insensitive, and only the first character matters
_ByteOrder: TypeAlias = L[
    "S",                 # swap the current order (default)
    "<", "L", "little",  # little-endian
    ">", "B", "big",     # big endian
    "=", "N", "native",  # native order
    "|", "I",            # ignore
]  # fmt: skip
_DTypeKind: TypeAlias = L["b", "i", "u", "f", "c", "m", "M", "O", "S", "U", "V", "T"]
_DTypeChar: TypeAlias = L[
    "?",  # bool
    "b",  # byte
    "B",  # ubyte
    "h",  # short
    "H",  # ushort
    "i",  # intc
    "I",  # uintc
    "l",  # long
    "L",  # ulong
    "q",  # longlong
    "Q",  # ulonglong
    "e",  # half
    "f",  # single
    "d",  # double
    "g",  # longdouble
    "F",  # csingle
    "D",  # cdouble
    "G",  # clongdouble
    "O",  # object
    "S",  # bytes_ (S0)
    "a",  # bytes_ (deprecated)
    "U",  # str_
    "V",  # void
    "M",  # datetime64
    "m",  # timedelta64
    "c",  # bytes_ (S1)
    "T",  # StringDType
]
_DTypeNum: TypeAlias = L[
    0,  # bool
    1,  # byte
    2,  # ubyte
    3,  # short
    4,  # ushort
    5,  # intc
    6,  # uintc
    7,  # long
    8,  # ulong
    9,  # longlong
    10,  # ulonglong
    23,  # half
    11,  # single
    12,  # double
    13,  # longdouble
    14,  # csingle
    15,  # cdouble
    16,  # clongdouble
    17,  # object
    18,  # bytes_
    19,  # str_
    20,  # void
    21,  # datetime64
    22,  # timedelta64
    25,  # no type
    256,  # user-defined
    2056,  # StringDType
]
_DTypeBuiltinKind: TypeAlias = L[0, 1, 2]

_ArrayAPIVersion: TypeAlias = L["2021.12", "2022.12", "2023.12"]
_Device: TypeAlias = L["cpu"]

_OrderCF: TypeAlias = L["C", "F"] | None  # noqa: PYI047
_OrderACF: TypeAlias = L["A", "C", "F"] | None
_OrderKACF: TypeAlias = L["K", "A", "C", "F"] | None

_FutureScalar: TypeAlias = L["bytes", "str", "object"]
_ByteOrderChar: TypeAlias = L["<", ">", "=", "|"]
_CastingKind: TypeAlias = L["no", "equiv", "safe", "same_kind", "unsafe"]
_ModeKind: TypeAlias = L["raise", "wrap", "clip"]
_PartitionKind: TypeAlias = L["introselect"]
_SortSide: TypeAlias = L["left", "right"]
_SortKind: TypeAlias = L[
    "Q", "quick", "quicksort",
    "M", "merge", "mergesort",
    "H", "heap", "heapsort",
    "S", "stable", "stablesort",
]  # fmt: skip

_Bool0: TypeAlias = bool_[L[False]]
_Bool1: TypeAlias = bool_[L[True]]
_ToFalse: TypeAlias = L[False] | bool_[L[False]]
_ToTrue: TypeAlias = L[True] | bool_[L[True]]

_ConvertibleToInt: TypeAlias = CanInt | CanIndex | bytes | str
_ConvertibleToFloat: TypeAlias = CanFloat | CanIndex | bytes | str
_ConvertibleToComplex: TypeAlias = complex | CanComplex | CanFloat | CanIndex | bytes | str
_ConvertibleToTD64: TypeAlias = dt.timedelta | int | bytes | str | character | number | timedelta64 | bool_ | None
_ConvertibleToDT64: TypeAlias = dt.date | int | bytes | str | character | number | datetime64 | bool_ | None

_DT64Date: TypeAlias = _HasDateAttributes | L["TODAY", "today", b"TODAY", b"today"]
_DT64Now: TypeAlias = L["NOW", "now", b"NOW", b"now"]
_NaTValue: TypeAlias = L["NAT", "NaT", "nat", b"NAT", b"NaT", b"nat"]

_MonthUnit: TypeAlias = L["Y", "M", b"Y", b"M"]
_DayUnit: TypeAlias = L["W", "D", b"W", b"D"]
_DateUnit: TypeAlias = L[_MonthUnit, _DayUnit]
_NativeTimeUnit: TypeAlias = L["h", "m", "s", "ms", "us", "μs", b"h", b"m", b"s", b"ms", b"us"]
_IntTimeUnit: TypeAlias = L["ns", "ps", "fs", "as", b"ns", b"ps", b"fs", b"as"]
_TimeUnit: TypeAlias = L[_NativeTimeUnit, _IntTimeUnit]
_NativeTD64Unit: TypeAlias = L[_DayUnit, _NativeTimeUnit]
_IntTD64Unit: TypeAlias = L[_MonthUnit, _IntTimeUnit]
_TD64Unit: TypeAlias = L[_DateUnit, _TimeUnit]
_TimeUnitSpec: TypeAlias = _TD64UnitT | tuple[_TD64UnitT, CanIndex]

_ToReal: TypeAlias = float | CanComplex | CanFloat | CanIndex
_ToImag: TypeAlias = float | CanFloat | CanIndex

_DTypeDescr: TypeAlias = (
    list[tuple[str, str]]
    | list[tuple[str, str, tuple[int, ...]]]
    | list[tuple[str, str] | tuple[str, str, tuple[int, ...]]]
)

###
# TypedDict's (for internal use only)

@type_check_only
class _FormerAttrsDict(TypedDict):
    object: LiteralString
    float: LiteralString
    complex: LiteralString
    str: LiteralString
    int: LiteralString

###
# Protocols (for internal use only)

@type_check_only
class _CanSeekTellFileNo(SupportsFlush, Protocol):
    # Protocol for representing file-like-objects accepted by `ndarray.tofile` and `fromfile`
    def fileno(self) -> CanIndex: ...
    def tell(self) -> CanIndex: ...
    def seek(self, offset: int, whence: int, /) -> object: ...

@type_check_only
class _CanItem(Protocol[_T_co]):
    def item(self, /) -> _T_co: ...

@type_check_only
class _HasShapeAndItem(Protocol[_ShapeT_co, _T_co]):
    @property
    def __inner_shape__(self, /) -> _ShapeT_co: ...
    def item(self, /) -> _T_co: ...

@type_check_only
class _HasDType(Protocol[_T_co]):
    @property
    def dtype(self, /) -> _T_co: ...

@type_check_only
class _HasShapeAndDType(Protocol[_ShapeT_co, _T_co]):
    @property
    def __inner_shape__(self, /) -> _ShapeT_co: ...
    @property
    def dtype(self, /) -> _T_co: ...

@type_check_only
class _HasReal(Protocol[_RealT_co]):
    @property
    def real(self, /) -> _RealT_co: ...

@type_check_only
class _HasImag(Protocol[_ImagT_co]):
    @property
    def imag(self, /) -> _ImagT_co: ...

@type_check_only
class _HasType(Protocol[_T_co]):
    @property
    def type(self, /) -> type[_T_co]: ...

_HasTypeWithItem: TypeAlias = _HasType[_CanItem[_T]]
_HasTypeWithReal: TypeAlias = _HasType[_HasReal[_T]]
_HasTypeWithImag: TypeAlias = _HasType[_HasImag[_T]]

_HasDTypeWithItem: TypeAlias = _HasDType[_HasTypeWithItem[_T]]
_HasDTypeWithReal: TypeAlias = _HasDType[_HasTypeWithReal[_T]]
_HasDTypeWithImag: TypeAlias = _HasDType[_HasTypeWithImag[_T]]

_CT = TypeVar("_CT", bound=ct._SimpleCData[Any])
_CT_co = TypeVar("_CT_co", bound=ct._SimpleCData[Any], covariant=True)

@type_check_only
class _HasCType(Protocol[_CT_co]):
    @property
    def __ctype__(self, /) -> _CT_co: ...

@type_check_only
class _HasDateAttributes(Protocol):
    # The `datetime64` constructors requires an object with the three attributes below,
    # and thus supports datetime duck typing
    @property
    def day(self) -> int: ...
    @property
    def month(self) -> int: ...
    @property
    def year(self) -> int: ...

###
# Mixins (for internal use only)

@type_check_only
class _RealMixin:
    @property
    def real(self) -> Self: ...
    @property
    def imag(self) -> Self: ...

@type_check_only
class _RoundMixin:
    @overload
    def __round__(self, /, ndigits: None = None) -> int: ...
    @overload
    def __round__(self, /, ndigits: CanIndex) -> Self: ...

@type_check_only
class _IntegralMixin(_RealMixin):
    @property
    def numerator(self) -> Self: ...
    @property
    def denominator(self) -> L[1]: ...
    def is_integer(self, /) -> L[True]: ...

_ScalarLikeT_contra = TypeVar("_ScalarLikeT_contra", contravariant=True)
_ArrayLikeT_contra = TypeVar("_ArrayLikeT_contra", contravariant=True)

@type_check_only
class _CmpOpMixin(Generic[_ScalarLikeT_contra, _ArrayLikeT_contra]):
    @overload
    def __lt__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __lt__(self, x: _ArrayLikeT_contra | _NestedSequence[_nt.op.CanGt], /) -> _nt.Array[bool_]: ...
    @overload
    def __lt__(self, x: _nt.op.CanGt, /) -> bool_: ...

    #
    @overload
    def __le__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __le__(self, x: _ArrayLikeT_contra | _NestedSequence[_nt.op.CanGe], /) -> _nt.Array[bool_]: ...
    @overload
    def __le__(self, x: _nt.op.CanGe, /) -> bool_: ...

    #
    @overload
    def __gt__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __gt__(self, x: _ArrayLikeT_contra | _NestedSequence[_nt.op.CanLt], /) -> _nt.Array[bool_]: ...
    @overload
    def __gt__(self, x: _nt.op.CanLt, /) -> bool_: ...

    #
    @overload
    def __ge__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __ge__(self, x: _ArrayLikeT_contra | _NestedSequence[_nt.op.CanLe], /) -> _nt.Array[bool_]: ...
    @overload
    def __ge__(self, x: _nt.op.CanLe, /) -> bool_: ...

@type_check_only
class _IntMixin(Generic[_IntSizeT_co]):
    @property
    def itemsize(self) -> _IntSizeT_co: ...
    @property
    def nbytes(self) -> _IntSizeT_co: ...

    #
    @override
    def __hash__(self, /) -> int: ...
    def __index__(self, /) -> int: ...
    def bit_count(self, /) -> int: ...

@type_check_only
class _FloatMixin(Generic[_FloatSizeT_co]):
    @property
    def itemsize(self) -> _FloatSizeT_co: ...
    @property
    def nbytes(self) -> _FloatSizeT_co: ...

    #
    @override
    def __hash__(self, /) -> int: ...
    def is_integer(self, /) -> py_bool: ...
    def as_integer_ratio(self, /) -> tuple[int, int]: ...

###
# NumType only: Does not exist at runtime!

__numtype__: Final = True

###
# Public, but not explicitly exported in __all__
__NUMPY_SETUP__: Final = False
__numpy_submodules__: Final[set[_SubModule]] = ...
__former_attrs__: Final[_FormerAttrsDict] = ...
__future_scalars__: Final[set[_FutureScalar]] = ...
__array_api_version__: Final = "2024.12"
test: Final[PytestTester] = ...

###
# Public API

@type_check_only
class _DTypeMeta(type):
    @property
    def type(cls, /) -> type[generic] | None: ...
    @property
    def _abstract(cls, /) -> bool: ...
    @property
    def _is_numeric(cls, /) -> bool: ...
    @property
    def _parametric(cls, /) -> bool: ...
    @property
    def _legacy(cls, /) -> bool: ...

@final
class dtype(Generic[_ScalarT_co], metaclass=_DTypeMeta):
    names: tuple[str, ...] | None

    @property
    def alignment(self) -> int: ...
    @property
    def base(self) -> dtype: ...
    @property
    def byteorder(self) -> _ByteOrderChar: ...
    @property
    def char(self) -> _DTypeChar: ...
    @property
    def descr(self) -> _DTypeDescr: ...
    @property
    def fields(self) -> MappingProxyType[LiteralString, tuple[dtype, int] | tuple[dtype, int, Any]] | None: ...
    @property
    def flags(self) -> int: ...
    @property
    def hasobject(self) -> py_bool: ...
    @property
    def isbuiltin(self) -> _DTypeBuiltinKind: ...
    @property
    def isnative(self) -> py_bool: ...
    @property
    def isalignedstruct(self) -> py_bool: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def kind(self) -> _DTypeKind: ...
    @property
    def metadata(self) -> MappingProxyType[str, Any] | None: ...
    @property
    def name(self) -> LiteralString: ...
    @property
    def num(self) -> _DTypeNum: ...
    @property
    def shape(self) -> _nt.Shape0: ...
    @property
    def ndim(self) -> int: ...
    @property
    def subdtype(self) -> tuple[dtype, tuple[int, ...]] | None: ...

    #
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeBool, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.BoolDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeInt8, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Int8DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeUInt8, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.UInt8DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeInt16, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Int16DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeUInt16, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.UInt16DType: ...
    @overload
    def __new__(  # type: ignore[overload-overlap]
        cls, dtype: _nt.ToDTypeLong, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.LongDType: ...
    @overload
    def __new__(  # type: ignore[overload-overlap]
        cls, dtype: _nt.ToDTypeULong, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.ULongDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeInt32, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Int32DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeUInt32, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.UInt32DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeInt64, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Int64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeUInt64, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.UInt64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeFloat16, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Float16DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeFloat32, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Float32DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeFloat64 | None, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Float64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeLongDouble, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.LongDoubleDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeComplex64, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Complex64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeComplex128, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.Complex128DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeCLongDouble, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.CLongDoubleDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeObject, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.ObjectDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeBytes, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.BytesDType: ...
    @overload
    def __new__(  # type: ignore[overload-overlap]
        cls, dtype: _nt.ToDTypeStr, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.StrDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeVoid, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.VoidDType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeDateTime64, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.DateTime64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeTimeDelta64, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.TimeDelta64DType: ...
    @overload
    def __new__(
        cls, dtype: _nt.ToDTypeString, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtypes.StringDType: ...
    @overload
    def __new__(
        cls, dtype: _DTypeLike[_ScalarT_co], align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> Self: ...
    @overload
    def __new__(
        cls, dtype: DTypeLike, align: py_bool = False, copy: py_bool = False, metadata: _MetaData = ...
    ) -> dtype: ...

    #
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

    #
    @override
    def __hash__(self, /) -> int: ...

    # Explicitly defined `__eq__` and `__ne__` to get around mypy's `strict_equality` option;
    # even though their signatures are identical to their `object`-based counterpart
    @override
    def __eq__(self, other: object, /) -> py_bool: ...
    @override
    def __ne__(self, other: object, /) -> py_bool: ...

    #
    def __gt__(self, other: DTypeLike, /) -> py_bool: ...
    def __ge__(self, other: DTypeLike, /) -> py_bool: ...
    def __lt__(self, other: DTypeLike, /) -> py_bool: ...
    def __le__(self, other: DTypeLike, /) -> py_bool: ...

    # NOTE: In the future 1-based multiplications will also yield `flexible` dtypes
    @overload
    def __mul__(self: _DTypeT, value: L[1], /) -> _DTypeT: ...
    @overload
    def __mul__(self: _FlexDTypeT, value: CanIndex, /) -> _FlexDTypeT: ...
    @overload
    def __mul__(self, value: CanIndex, /) -> dtype[void]: ...

    # NOTE: `__rmul__` seems to be broken when used in combination with literals as of mypy 0.902.
    # Set the return-type to `dtype` for now for non-flexible dtypes.
    @overload
    def __rmul__(self: _FlexDTypeT, value: CanIndex, /) -> _FlexDTypeT: ...
    @overload
    def __rmul__(self, value: CanIndex, /) -> dtype: ...

    #
    @overload
    def __getitem__(self: dtype[void], key: list[str], /) -> dtype[void]: ...
    @overload
    def __getitem__(self: dtype[void], key: str | CanIndex, /) -> dtype: ...

    #
    def newbyteorder(self, new_order: _ByteOrder = ..., /) -> Self: ...

    # place these at the bottom to avoid shadowing the `type` and `str` builtins
    @property
    def str(self) -> LiteralString: ...
    @property
    def type(self) -> type[_ScalarT_co]: ...

@type_check_only
class _ArrayOrScalarCommon:
    # remnants of numpy<2 methods
    itemset: ClassVar[GetSetDescriptorType]
    newbyteorder: ClassVar[GetSetDescriptorType]
    ptp: ClassVar[GetSetDescriptorType]

    @property
    def real(self, /) -> Any: ...
    @property
    def imag(self, /) -> Any: ...
    @property
    def T(self) -> Self: ...
    @property
    def mT(self) -> Self: ...
    @property
    def data(self) -> memoryview: ...
    @property
    def flags(self) -> flagsobj: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def nbytes(self) -> int: ...
    @property
    def device(self) -> _Device: ...

    # typeshed forces us to lie about this on python<3.12
    def __buffer__(self, flags: int, /) -> memoryview: ...

    #
    @property
    def __array_interface__(self) -> _MetaData: ...
    @property
    def __array_priority__(self) -> float: ...
    @property
    def __array_struct__(self) -> CapsuleType: ...  # builtins.PyCapsule

    #
    def __bool__(self, /) -> py_bool: ...
    def __int__(self, /) -> int: ...
    def __float__(self, /) -> float: ...

    #
    @override
    def __eq__(self, other: object, /) -> Any: ...
    @override
    def __ne__(self, other: object, /) -> Any: ...

    #
    def copy(self, order: _OrderKACF = ...) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: dict[int, Any] | None, /) -> Self: ...
    def __setstate__(self, state: tuple[CanIndex, _ShapeLike, _DTypeT_co, bool_, bytes | list[Any]], /) -> None: ...
    def __array_namespace__(self, /, *, api_version: _ArrayAPIVersion | None = None) -> ModuleType: ...

    #
    def dump(self, file: StrOrBytesPath | SupportsWrite[bytes]) -> None: ...
    def dumps(self) -> bytes: ...
    @deprecated("tostring() is deprecated. Use tobytes() instead.")
    def tostring(self, order: _OrderKACF = "C") -> bytes: ...
    def tobytes(self, order: _OrderKACF = "C") -> bytes: ...
    def tofile(self, fid: StrOrBytesPath | _CanSeekTellFileNo, sep: str = ..., format: str = ...) -> None: ...
    def tolist(self) -> Any: ...
    def to_device(self, device: _Device, /, *, stream: int | Any | None = ...) -> Self: ...

    # NOTE: for `generic`, these two methods don't do anything
    def fill(self, value: _ScalarLike_co, /) -> None: ...
    def put(self, /, indices: _nt.CoInteger_nd, values: ArrayLike, mode: _ModeKind = "raise") -> None: ...

    # NOTE: even on `generic` this seems to work
    def setflags(
        self, /, write: py_bool | None = None, align: py_bool | None = None, uic: py_bool | None = None
    ) -> None: ...

    #
    def conj(self) -> Self: ...
    def conjugate(self) -> Self: ...

    #
    @overload
    def max(
        self,
        /,
        axis: _ShapeLike | None = None,
        out: None = None,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> Incomplete: ...
    @overload
    def max(
        self,
        /,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def max(
        self,
        /,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload  # axis=None (default), out=None (default), keepdims=False (default)
    def argmax(self, /, axis: None = None, out: None = None, *, keepdims: L[False] = False) -> intp: ...
    @overload  # axis=index, out=None (default)
    def argmax(self, /, axis: CanIndex, out: None = None, *, keepdims: py_bool = False) -> Incomplete: ...
    @overload  # axis=index, out=ndarray
    def argmax(self, /, axis: CanIndex | None, out: _ArrayT, *, keepdims: py_bool = False) -> _ArrayT: ...
    @overload
    def argmax(self, /, axis: CanIndex | None = None, *, out: _ArrayT, keepdims: py_bool = False) -> _ArrayT: ...

    #
    @overload
    def min(
        self,
        /,
        axis: _ShapeLike | None = None,
        out: None = None,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> Incomplete: ...
    @overload
    def min(
        self,
        /,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def min(
        self,
        /,
        axis: _ShapeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload  # axis=None (default), out=None (default), keepdims=False (default)
    def argmin(self, /, axis: None = None, out: None = None, *, keepdims: L[False] = False) -> intp: ...
    @overload  # axis=index, out=None (default)
    def argmin(self, /, axis: CanIndex, out: None = None, *, keepdims: py_bool = False) -> Incomplete: ...
    @overload  # axis=index, out=ndarray
    def argmin(self, /, axis: CanIndex | None, out: _ArrayT, *, keepdims: py_bool = False) -> _ArrayT: ...
    @overload
    def argmin(self, /, axis: CanIndex | None = None, *, out: _ArrayT, keepdims: py_bool = False) -> _ArrayT: ...

    #
    @overload  # out=None (default)
    def round(self, /, decimals: CanIndex = 0, out: None = None) -> Self: ...
    @overload  # out=ndarray
    def round(self, /, decimals: CanIndex, out: _ArrayT) -> _ArrayT: ...
    @overload
    def round(self, /, decimals: CanIndex = 0, *, out: _ArrayT) -> _ArrayT: ...

    #
    @overload  # out=None (default)
    def choose(self, /, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> _nt.Array: ...
    @overload  # out=ndarray
    def choose(self, /, choices: ArrayLike, out: _ArrayT, mode: _ModeKind = "raise") -> _ArrayT: ...

    # TODO: Annotate kwargs with an unpacked `TypedDict`
    @overload  # out: None (default)
    def clip(
        self, /, min: ArrayLike, max: ArrayLike | None = None, out: None = None, **kwargs: object
    ) -> _nt.Array: ...
    @overload
    def clip(self, /, min: None, max: ArrayLike, out: None = None, **kwargs: object) -> _nt.Array: ...
    @overload
    def clip(self, /, min: None = None, *, max: ArrayLike, out: None = None, **kwargs: object) -> _nt.Array: ...
    @overload  # out: ndarray
    def clip(self, /, min: ArrayLike, max: ArrayLike | None, out: _ArrayT, **kwargs: object) -> _ArrayT: ...
    @overload
    def clip(self, /, min: ArrayLike, max: ArrayLike | None = None, *, out: _ArrayT, **kwargs: object) -> _ArrayT: ...
    @overload
    def clip(self, /, min: None, max: ArrayLike, out: _ArrayT, **kwargs: object) -> _ArrayT: ...
    @overload
    def clip(self, /, min: None = None, *, max: ArrayLike, out: _ArrayT, **kwargs: object) -> _ArrayT: ...

    #
    @overload
    def compress(self, /, condition: _nt.CoInteger_nd, axis: CanIndex | None = None, out: None = None) -> _nt.Array: ...
    @overload
    def compress(self, /, condition: _nt.CoInteger_nd, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def compress(self, /, condition: _nt.CoInteger_nd, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

    #
    @overload  # out: None (default)
    def cumprod(
        self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
    ) -> _nt.Array: ...
    @overload  # out: ndarray
    def cumprod(self, /, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def cumprod(self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

    #

    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 0,
        where: _nt.ToBool_nd = True,
    ) -> Any: ...
    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 0,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def sum(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 0,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload  # out: None (default)
    def cumsum(
        self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
    ) -> _nt.Array: ...
    @overload  # out: ndarray
    def cumsum(self, /, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def cumsum(self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

    #
    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 1,
        where: _nt.ToBool_nd = True,
    ) -> Any: ...
    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 1,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def prod(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = 1,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload
    def mean(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> Any: ...
    @overload
    def mean(
        self,
        /,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def mean(
        self,
        /,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        keepdims: py_bool = False,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload
    def std(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        ddof: float = 0,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> Any: ...
    @overload
    def std(
        self,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> _ArrayT: ...
    @overload
    def std(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: py_bool = False,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> _ArrayT: ...

    #
    @overload
    def var(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
        ddof: float = 0,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> Any: ...
    @overload
    def var(
        self,
        axis: _ShapeLike | None,
        dtype: DTypeLike | None,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: py_bool = False,
        *,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> _ArrayT: ...
    @overload
    def var(
        self,
        axis: _ShapeLike | None = None,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
        ddof: float = 0,
        keepdims: py_bool = False,
        where: _nt.ToBool_nd = True,
        mean: _nt.CoComplex_nd = ...,
        correction: float = ...,
    ) -> _ArrayT: ...

#
class ndarray(_ArrayOrScalarCommon, Generic[_ShapeT_co, _DTypeT_co]):
    __hash__: ClassVar[None]  # type: ignore[assignment]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @property
    @type_check_only
    def __inner_shape__(self, /) -> _ShapeT_co: ...
    @property
    @type_check_only
    def __ctype__(self: _HasDType[_HasType[_HasCType[_CT]]], /) -> ct.Array[_CT]: ...

    #
    @property
    def base(self) -> _nt.Array | None: ...

    #
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...

    #
    @property
    # NOTE: This constrained typevar use is a workaround for a mypy bug
    # def shape(self: _nt.HasInnerShape[_ShapeT] | ndarray[_ShapeT2]) -> _ShapeT | _ShapeT2: ...  # noqa: ERA001
    def shape(self: ndarray[_AnyShapeT]) -> _AnyShapeT: ...
    @shape.setter
    def shape(self: _nt.HasInnerShape[_ShapeT] | ndarray[_ShapeT2], shape: _ShapeT | _ShapeT2, /) -> None: ...

    #
    @property
    def strides(self) -> tuple[int, ...]: ...
    @strides.setter
    def strides(self, value: tuple[int, ...], /) -> None: ...

    #
    @property  # type: ignore[explicit-override]
    @override
    def real(self: _HasDTypeWithReal[_ScalarT], /) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @real.setter
    @override
    def real(self, value: ArrayLike, /) -> None: ...

    #
    @property  # type: ignore[explicit-override]
    @override
    def imag(self: _HasDTypeWithImag[_ScalarT], /) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @imag.setter
    def imag(self, value: ArrayLike, /) -> None: ...

    #
    @property
    def flat(self) -> flatiter[Self]: ...
    @property
    def ctypes(self) -> _ctypes[int]: ...

    #
    def __new__(
        cls,
        shape: _ShapeLike,
        dtype: DTypeLike = float,  # noqa: PYI011
        buffer: Buffer | None = None,
        offset: CanIndex = 0,
        strides: _ShapeLike | None = None,
        order: _OrderKACF | None = None,
    ) -> Self: ...

    #
    def __class_getitem__(cls, item: object, /) -> GenericAlias: ...

    #
    @overload
    def __array__(self, /, *, copy: bool | None = None) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __array__(self, dtype: _DTypeT, /, *, copy: bool | None = None) -> ndarray[_ShapeT_co, _DTypeT]: ...

    #
    def __array_finalize__(self, obj: _nt.Array | Any, /) -> None: ...
    def __array_ufunc__(self, ufunc: ufunc, method: _UFuncMethod, /, *inputs: object, **kwargs: object) -> Any: ...
    def __array_function__(
        self, /, func: Callable[..., Any], types: Iterable[type], args: Iterable[Any], kwargs: Mapping[str, Any]
    ) -> Any: ...
    def __array_wrap__(
        self,
        array: ndarray[_ShapeT, _DTypeT],
        context: tuple[ufunc, tuple[object, ...], int] | None = ...,
        return_scalar: py_bool = ...,
        /,
    ) -> ndarray[_ShapeT, _DTypeT]: ...

    #
    @overload
    def __getitem__(
        self, key: _ArrayInteger_co | tuple[_ArrayInteger_co, ...], /
    ) -> ndarray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self, key: CanIndex | tuple[CanIndex, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndices, /) -> ndarray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self: _nt.Array[void], key: str, /) -> ndarray[_ShapeT_co]: ...
    @overload
    def __getitem__(self: _nt.Array[void], key: list[str], /) -> _nt.Array[void, _ShapeT_co]: ...

    #
    @overload  # flexible | object_ | bool
    def __setitem__(
        self: ndarray[Any, dtype[bool_ | object_ | flexible] | dtypes.StringDType], key: _ToIndices, value: object, /
    ) -> None: ...
    @overload  # integer
    def __setitem__(
        self: _nt.Array[integer], key: _ToIndices, value: _nt.SequenceND[_ConvertibleToInt] | _nt.CoInteger_nd, /
    ) -> None: ...
    @overload  # floating
    def __setitem__(
        self: _nt.Array[floating],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToFloat | None] | _nt.CoFloating_nd,
        /,
    ) -> None: ...
    @overload  # complexfloating
    def __setitem__(
        self: _nt.Array[complexfloating],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToComplex | None] | _nt.CoComplex_nd,
        /,
    ) -> None: ...
    @overload  # timedelta64
    def __setitem__(
        self: _nt.Array[timedelta64], key: _ToIndices, value: _nt.SequenceND[_ConvertibleToTD64], /
    ) -> None: ...
    @overload  # datetime64
    def __setitem__(
        self: _nt.Array[datetime64], key: _ToIndices, value: _nt.SequenceND[_ConvertibleToDT64], /
    ) -> None: ...
    @overload  # void
    def __setitem__(self: _nt.Array[void], key: str | list[str], value: object, /) -> None: ...
    @overload  # catch-all
    def __setitem__(self, key: _ToIndices, value: ArrayLike, /) -> None: ...

    #
    def __complex__(self: _nt.Array[_nt.co_number | object_], /) -> complex: ...
    def __index__(self: _nt.Array[integer], /) -> int: ...

    #
    def __len__(self) -> int: ...
    def __contains__(self, value: object, /) -> py_bool: ...

    #
    @overload  # == 1-d & object_
    def __iter__(self: _nt.Array1D[object_], /) -> Iterator[Any]: ...
    @overload  # == 1-d
    def __iter__(self: _nt.Array1D[_ScalarT], /) -> Iterator[_ScalarT]: ...
    @overload  # >= 2-d
    def __iter__(self: _nt.Array[_ScalarT, _nt.Shape2N], /) -> Iterator[_nt.Array[_ScalarT]]: ...
    @overload  # ?-d
    def __iter__(self, /) -> Iterator[Any]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __eq__(self, other: _ScalarLike_co | ndarray[_ShapeT_co], /) -> _nt.Array[bool_, _ShapeT_co]: ...
    @overload
    def __eq__(self, other: object, /) -> _nt.Array[bool_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __ne__(self, other: _ScalarLike_co | ndarray[_ShapeT_co], /) -> _nt.Array[bool_, _ShapeT_co]: ...
    @overload
    def __ne__(self, other: object, /) -> _nt.Array[bool_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __lt__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __lt__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __lt__(self: _nt.Array[datetime64], other: _ArrayLikeDT64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __lt__(self: _nt.Array[object_], other: object, /) -> _nt.Array[bool_]: ...
    @overload
    def __lt__(self, other: _ArrayLikeObject_co, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __le__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __le__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __le__(self: _nt.Array[datetime64], other: _ArrayLikeDT64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __le__(self: _nt.Array[object_], other: object, /) -> _nt.Array[bool_]: ...
    @overload
    def __le__(self, other: _ArrayLikeObject_co, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __gt__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __gt__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __gt__(self: _nt.Array[datetime64], other: _ArrayLikeDT64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __gt__(self: _nt.Array[object_], other: object, /) -> _nt.Array[bool_]: ...
    @overload
    def __gt__(self, other: _ArrayLikeObject_co, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __ge__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __ge__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __ge__(self: _nt.Array[datetime64], other: _ArrayLikeDT64_co, /) -> _nt.Array[bool_]: ...
    @overload
    def __ge__(self: _nt.Array[object_], other: object, /) -> _nt.Array[bool_]: ...
    @overload
    def __ge__(self, other: _ArrayLikeObject_co, /) -> _nt.Array[bool_]: ...

    #
    def __abs__(
        self: _HasShapeAndDType[_ShapeT, _HasType[SupportsAbs[_ScalarT]]], /
    ) -> _nt.Array[_ScalarT, _ShapeT]: ...
    def __neg__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019
    def __pos__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019
    def __invert__(self: _IntegralArrayT, /) -> _IntegralArrayT: ...  # noqa: PYI019

    #
    @overload
    def __add__(self: _nt.Array[_ScalarT], x: _nt.Casts[_ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.Array[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __add__(self: _nt.Array[datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __add__(self: _nt.Array[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __add__(self: _nt.Array[object_, Any], x: object, /) -> _nt.Array[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __add__(self: _nt.Array[str_], x: _nt.ToString_nd[_T], /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __add__(self: _nt.StringArrayND[_T], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __add__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRAdd[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload
    def __radd__(self: _nt.Array[_ScalarT], x: _nt.Casts[_ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.Array[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.Array[datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __radd__(self: _nt.Array[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __radd__(self: _nt.Array[object_, Any], x: object, /) -> _nt.Array[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __radd__(self: _nt.Array[str_], x: _nt.ToString_nd[_T], /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __radd__(self: _nt.StringArrayND[_T], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __radd__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanAdd[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload  # type: ignore[misc]
    def __iadd__(self: _nt.Array[_ScalarT], x: _nt.Casts[_ScalarT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[bool_], x: _PyBoolND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[number], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[inexact], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[complexfloating], x: _PyCoComplexND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[datetime64], x: _nt.CoTimeDelta_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _nt.StringArrayND[_T], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRAdd[_AnyItemT, _AnyItemT]], /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __sub__(self: _nt.Array[_NumericT], x: _nt.Casts[_NumericT], /) -> _nt.Array[_NumericT]: ...
    @overload
    def __sub__(self: _nt.Array[_CoNumberT], x: _nt.CastsWith[_CoNumberT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithBuiltin[_T, _NumericT], x: _nt.SequenceND[_T], /) -> _nt.Array[_NumericT]: ...
    @overload
    def __sub__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.Array[datetime64], x: _nt.ToDateTime_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __sub__(self: _nt.Array[datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __sub__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...
    @overload
    def __sub__(
        self: _nt.Array[generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanRSub[_AnyNumberItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload
    def __rsub__(self: _nt.Array[_NumericT], x: _nt.Casts[_NumericT], /) -> _nt.Array[_NumericT]: ...
    @overload
    def __rsub__(self: _nt.Array[_CoNumberT], x: _nt.CastsWith[_CoNumberT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithBuiltin[_T, _NumericT], x: _nt.SequenceND[_T], /) -> _nt.Array[_NumericT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.Array[datetime64], x: _nt.ToDateTime_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __rsub__(self: _nt.Array[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.Array[datetime64]: ...
    @overload
    def __rsub__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...
    @overload
    def __rsub__(
        self: _nt.Array[generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanSub[_AnyNumberItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload  # type: ignore[misc]
    def __isub__(self: _nt.Array[_ScalarT], x: _nt.Casts[_ScalarT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.Array[number], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.Array[inexact], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.Array[complexfloating], x: _PyCoComplexND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.Array[datetime64], x: _nt.CoTimeDelta_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _nt.Array[generic[_AnyNumberItemT]],
        x: _nt.Sequence1ND[_nt.op.CanRSub[_AnyNumberItemT, _AnyNumberItemT]],
        /,
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mul__(self: _nt.Array[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __mul__(self: _nt.Array[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithInt[_ScalarT], x: _PyCoIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.Array[timedelta64], x: _nt.ToFloating_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __mul__(self: _nt.Array[object_, Any], x: object, /) -> _nt.Array[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __mul__(self: _nt.Array[integer], x: _nt.ToString_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __mul__(self: _nt.StringArrayND[_T], x: _nt.ToInteger_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __mul__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMul[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload
    def __rmul__(self: _nt.Array[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __rmul__(self: _nt.Array[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithInt[_ScalarT], x: _PyCoIntND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.Array[timedelta64], x: _nt.ToFloating_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __rmul__(self: _nt.Array[object_, Any], x: object, /) -> _nt.Array[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __rmul__(self: _nt.Array[integer], x: _nt.ToString_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __rmul__(self: _nt.StringArrayND[_T], x: _nt.ToInteger_nd, /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __rmul__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanMul[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...

    #
    @overload  # type: ignore[misc]
    def __imul__(self: _nt.Array[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[bool_], x: _PyBoolND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[number], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[inexact], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[complexfloating], x: _PyCoComplexND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[timedelta64], x: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.StringArrayND[_T], x: _nt.ToInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMul[_AnyItemT, _AnyItemT]], /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    # TODO(jorenham): Support the "1d @ 1d -> scalar" case
    # https://github.com/numpy/numtype/issues/197
    # NOTE: For builtin scalars, __matmul__ does not use the standard NEP 50 casting rules
    @overload
    def __matmul__(self: _nt.Array[_CoNumberT], x: _nt.CastsArray[_CoNumberT], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __matmul__(
        self: _nt.Array[_CoNumberT], x: _nt.CastsWithArray[_CoNumberT, _ScalarT], /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __matmul__(self: _nt.Array[_CoNumberT], x: _nt.Sequence1ND[py_bool], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __matmul__(self: _nt.Array[_nt.co_int64], x: _nt.Sequence1ND[_nt.JustInt], /) -> _nt.Array[intp]: ...
    @overload
    def __matmul__(
        self: _HasDType[_HasType[_JustUnsignedInteger | _JustInteger]], x: _nt.Sequence1ND[_nt.JustInt], /
    ) -> _nt.Array[intp | float64]: ...
    @overload
    def __matmul__(self: _nt.Array[uint64 | _F64_max], x: _nt.Sequence1ND[float], /) -> _nt.Array[float64]: ...
    @overload
    def __matmul__(self: _nt.Array[_C128_max], x: _nt.Sequence1ND[complex], /) -> _nt.Array[complex128]: ...
    @overload
    def __matmul__(
        self: _nt.Array[_Inexact64_max], x: _nt.Sequence1ND[_nt.JustComplex], /
    ) -> _nt.Array[complex128]: ...
    @overload
    def __matmul__(self: _nt.CastsWithInt[_ScalarT], x: _nt.Sequence1ND[_nt.JustInt], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __matmul__(self: _nt.CastsWithFloat[_ScalarT], x: _nt.Sequence1ND[_nt.JustFloat], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __matmul__(
        self: _nt.CastsWithComplex[_ScalarT], x: _nt.Sequence1ND[_nt.JustComplex], /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __matmul__(
        self: _nt.Array[object_], x: _nt.ToObject_1nd | _nt.Sequence1ND[object], /
    ) -> _nt.Array[object_]: ...

    # keep in sync with __matmul__
    @overload
    def __rmatmul__(self: _nt.Array[_CoNumberT], x: _nt.CastsArray[_CoNumberT], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __rmatmul__(
        self: _nt.Array[_CoNumberT], x: _nt.CastsWithArray[_CoNumberT, _ScalarT], /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmatmul__(self: _nt.Array[_CoNumberT], x: _nt.Sequence1ND[py_bool], /) -> _nt.Array[_CoNumberT]: ...
    @overload
    def __rmatmul__(self: _nt.Array[_nt.co_int64], x: _nt.Sequence1ND[_nt.JustInt], /) -> _nt.Array[intp]: ...
    @overload
    def __rmatmul__(
        self: _HasDType[_HasType[_JustUnsignedInteger | _JustInteger]], x: _nt.Sequence1ND[_nt.JustInt], /
    ) -> _nt.Array[intp | float64]: ...
    @overload
    def __rmatmul__(self: _nt.Array[uint64 | _F64_max], x: _nt.Sequence1ND[float], /) -> _nt.Array[float64]: ...
    @overload
    def __rmatmul__(self: _nt.Array[_C128_max], x: _nt.Sequence1ND[complex], /) -> _nt.Array[complex128]: ...
    @overload
    def __rmatmul__(
        self: _nt.Array[_Inexact64_max], x: _nt.Sequence1ND[_nt.JustComplex], /
    ) -> _nt.Array[complex128]: ...
    @overload
    def __rmatmul__(self: _nt.CastsWithInt[_ScalarT], x: _nt.Sequence1ND[_nt.JustInt], /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmatmul__(
        self: _nt.CastsWithFloat[_ScalarT], x: _nt.Sequence1ND[_nt.JustFloat], /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmatmul__(
        self: _nt.CastsWithComplex[_ScalarT], x: _nt.Sequence1ND[_nt.JustComplex], /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rmatmul__(
        self: _nt.Array[object_], x: _nt.ToObject_1nd | _nt.Sequence1ND[object], /
    ) -> _nt.Array[object_]: ...

    #
    @overload
    def __pow__(self: _nt.Array[_NumberT], x: _nt.Casts[_NumberT], k: None = None, /) -> _nt.Array[_NumberT]: ...
    @overload
    def __pow__(self: _nt.Array[bool_], x: _nt.ToBool_nd, k: None = None, /) -> _nt.Array[int8]: ...
    @overload
    def __pow__(
        self: _nt.Array[_NumberT], x: _nt.CastsWith[_NumberT, _ScalarT], k: None = None, /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __pow__(self: _nt.CastsWithInt[_NumberT], x: _PyCoIntND, k: None = None, /) -> _nt.Array[_NumberT]: ...
    @overload
    def __pow__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, k: None = None, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __pow__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, k: None = None, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __pow__(self: _nt.Array[object_], x: object, k: None = None, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rpow__(self: _nt.Array[_NumberT], x: _nt.Casts[_NumberT], k: None = None, /) -> _nt.Array[_NumberT]: ...
    @overload
    def __rpow__(self: _nt.Array[bool_], x: _nt.ToBool_nd, k: None = None, /) -> _nt.Array[int8]: ...
    @overload
    def __rpow__(
        self: _nt.Array[_NumberT], x: _nt.CastsWith[_NumberT, _ScalarT], k: None = None, /
    ) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rpow__(self: _nt.CastsWithInt[_NumberT], x: _PyCoIntND, k: None = None, /) -> _nt.Array[_NumberT]: ...
    @overload
    def __rpow__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, k: None = None, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rpow__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, k: None = None, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rpow__(self: _nt.Array[object_], x: object, k: None = None, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ipow__(self: _nt.Array[_NumberT], x: _nt.Casts[_NumberT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.Array[number], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.Array[inexact], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.Array[complexfloating], x: _PyCoComplexND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __truediv__(
        self: _HasDType[_HasType[_JustNumber]], x: _nt.CoFloat64_nd | _HasDType[_HasType[_JustNumber]], /
    ) -> _nt.Array[inexact]: ...
    @overload
    def __truediv__(self: _nt.Array[_InexactT], x: _nt.Casts[_InexactT], /) -> _nt.Array[_InexactT]: ...
    @overload
    def __truediv__(self: _nt.Array[_ScalarT], x: _nt.CastsWith[_ScalarT, _InexactT], /) -> _nt.Array[_InexactT]: ...  # type: ignore[overload-overlap]
    @overload
    def __truediv__(self: _nt.CastsWithFloat[_ScalarT], x: _PyCoFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __truediv__(self: _nt.Array[_nt.co_integer], x: _nt.CoInteger_nd, /) -> _nt.Array[float64]: ...
    @overload
    def __truediv__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[float64]: ...
    @overload
    def __truediv__(
        self: _nt.Array[timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> _nt.Array[timedelta64]: ...
    @overload
    def __truediv__(
        self: _nt.Array[generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanRTruediv[_AnyNumberItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __truediv__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rtruediv__(
        self: _HasDType[_HasType[_JustNumber]], x: _nt.CoFloat64_nd | _HasDType[_HasType[_JustNumber]], /
    ) -> _nt.Array[inexact]: ...
    @overload
    def __rtruediv__(self: _nt.Array[_InexactT], x: _nt.Casts[_InexactT], /) -> _nt.Array[_InexactT]: ...
    @overload
    def __rtruediv__(self: _nt.Array[_ScalarT], x: _nt.CastsWith[_ScalarT, _InexactT], /) -> _nt.Array[_InexactT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rtruediv__(self: _nt.CastsWithFloat[_ScalarT], x: _PyCoFloatND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.Array[_ScalarT]: ...
    @overload
    def __rtruediv__(self: _nt.Array[_nt.co_integer], x: _nt.CoInteger_nd, /) -> _nt.Array[float64]: ...
    @overload
    def __rtruediv__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[float64]: ...
    @overload
    def __rtruediv__(self: _nt.Array[integer | floating], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __rtruediv__(
        self: _nt.Array[generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanTruediv[_AnyNumberItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __rtruediv__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __itruediv__(self: _nt.Array[_InexactT], x: _nt.Casts[_InexactT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: _nt.Array[inexact], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: _nt.Array[complexfloating], x: _PyCoComplexND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.Array[timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.Array[generic[_AnyNumberItemT]],
        x: _nt.Sequence1ND[_nt.op.CanRTruediv[_AnyNumberItemT, _AnyNumberItemT]],
        /,
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __floordiv__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __floordiv__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.Array[_RealNumberT]: ...
    @overload
    def __floordiv__(
        self: _nt.Array[_RealNumberT], x: _nt.CastsWith[_RealNumberT, _RealScalarT], /
    ) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[int64]: ...
    @overload
    def __floordiv__(
        self: _nt.Array[timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> _nt.Array[timedelta64]: ...
    @overload
    def __floordiv__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRFloordiv[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __floordiv__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rfloordiv__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __rfloordiv__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.Array[_RealNumberT]: ...
    @overload
    def __rfloordiv__(
        self: _nt.Array[_RealNumberT], x: _nt.CastsWith[_RealNumberT, _RealScalarT], /
    ) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[int64]: ...
    @overload
    def __rfloordiv__(self: _nt.Array[integer | floating], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __rfloordiv__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanFloordiv[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __rfloordiv__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ifloordiv__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT], /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: _nt.Array[integer], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: _nt.Array[floating], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.Array[timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRFloordiv[_AnyItemT, _AnyItemT]], /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mod__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __mod__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.Array[_RealNumberT]: ...
    @overload
    def __mod__(
        self: _nt.Array[_CoFloatingT], x: _nt.CastsWith[_CoFloatingT, _RealScalarT], /
    ) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __mod__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __mod__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __mod__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __mod__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMod[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __mod__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rmod__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __rmod__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.Array[_RealNumberT]: ...
    @overload
    def __rmod__(
        self: _nt.Array[_CoFloatingT], x: _nt.CastsWith[_CoFloatingT, _RealScalarT], /
    ) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rmod__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rmod__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.Array[_RealScalarT]: ...
    @overload
    def __rmod__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.Array[timedelta64]: ...
    @overload
    def __rmod__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanMod[_AnyItemT]], /
    ) -> _nt.Array[Incomplete]: ...
    @overload
    def __rmod__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imod__(self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: _nt.Array[integer], x: _PyCoIntND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: _nt.Array[floating], x: _PyCoFloatND, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(
        self: _nt.Array[generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMod[_AnyItemT, _AnyItemT]], /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __divmod__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _Tuple2[_nt.Array[int8]]: ...
    @overload
    def __divmod__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _Tuple2[_nt.Array[_RealNumberT]]: ...
    @overload
    def __divmod__(
        self: _nt.Array[_CoFloatingT], x: _nt.CastsWith[_CoFloatingT, _RealScalarT], /
    ) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __divmod__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __divmod__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __divmod__(
        self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /
    ) -> tuple[_nt.Array[int64], _nt.Array[timedelta64]]: ...
    @overload
    def __divmod__(self: _nt.Array[object_], x: object, /) -> _Tuple2[_nt.Array[object_]]: ...

    #
    @overload
    def __rdivmod__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _Tuple2[_nt.Array[int8]]: ...
    @overload
    def __rdivmod__(
        self: _nt.Array[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _Tuple2[_nt.Array[_RealNumberT]]: ...
    @overload
    def __rdivmod__(
        self: _nt.Array[_CoFloatingT], x: _nt.CastsWith[_CoFloatingT, _RealScalarT], /
    ) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __rdivmod__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __rdivmod__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _Tuple2[_nt.Array[_RealScalarT]]: ...
    @overload
    def __rdivmod__(
        self: _nt.Array[timedelta64], x: _nt.ToTimeDelta_nd, /
    ) -> tuple[_nt.Array[int64], _nt.Array[timedelta64]]: ...
    @overload
    def __rdivmod__(self: _nt.Array[object_], x: object, /) -> _Tuple2[_nt.Array[object_]]: ...

    #
    @overload
    def __lshift__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __lshift__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __lshift__(self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __lshift__(self: _nt.Array[_IntegerT], x: _nt.CastsWith[_IntegerT, _IntegralT], /) -> _nt.Array[_IntegralT]: ...
    @overload
    def __lshift__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rlshift__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __rlshift__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __rlshift__(self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rlshift__(
        self: _nt.Array[_IntegerT], x: _nt.CastsWith[_IntegerT, _IntegralT], /
    ) -> _nt.Array[_IntegralT]: ...
    @overload
    def __rlshift__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ilshift__(
        self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ilshift__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __rshift__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __rshift__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __rshift__(self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rshift__(self: _nt.Array[_IntegerT], x: _nt.CastsWith[_IntegerT, _IntegralT], /) -> _nt.Array[_IntegralT]: ...
    @overload
    def __rshift__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rrshift__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> _nt.Array[int8]: ...
    @overload
    def __rrshift__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __rrshift__(self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rrshift__(
        self: _nt.Array[_IntegerT], x: _nt.CastsWith[_IntegerT, _IntegralT], /
    ) -> _nt.Array[_IntegralT]: ...
    @overload
    def __rrshift__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __irshift__(
        self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __irshift__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __and__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __and__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __and__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __and__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __and__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rand__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __rand__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rand__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __rand__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rand__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __iand__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(
        self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __xor__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __xor__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __xor__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __xor__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __xor__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __rxor__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __rxor__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rxor__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __rxor__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __rxor__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ixor__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(
        self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __or__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __or__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __or__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __or__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __or__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload
    def __ror__(self: _nt.Array[bool_], x: _PyIntND, /) -> _nt.Array[intp]: ...
    @overload
    def __ror__(self: _nt.Array[_IntegerT], x: _PyCoIntND, /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __ror__(self: _nt.Array[_CoIntegerT], x: _nt.Casts[_CoIntegerT] | _PyBoolND, /) -> _nt.Array[_CoIntegerT]: ...
    @overload
    def __ror__(self: _nt.Array[_CoIntegerT], x: _nt.CastsWith[_CoIntegerT, _IntegerT], /) -> _nt.Array[_IntegerT]: ...
    @overload
    def __ror__(self: _nt.Array[object_], x: object, /) -> _nt.Array[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ior__(self: _nt.Array[bool_], x: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(
        self: _nt.Array[_IntegerT], x: _nt.Casts[_IntegerT] | _PyCoIntND, /
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(self: _nt.Array[object_], x: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    def __dlpack__(
        self: _nt.Array[number],
        /,
        *,
        stream: int | Any | None = None,
        max_version: tuple[int, int] | None = None,
        dl_device: tuple[int, int] | None = None,
        copy: py_bool | None = None,
    ) -> CapsuleType: ...

    #
    def __dlpack_device__(self, /) -> tuple[L[1], L[0]]: ...

    #
    @overload  # special casing for `StringDType`, which has no scalar type
    def item(self: ndarray[Any, dtypes.StringDType], /) -> str: ...
    @overload
    def item(self: ndarray[Any, dtypes.StringDType], arg0: CanIndex | tuple[CanIndex, ...] = ..., /) -> str: ...
    @overload
    def item(self: ndarray[Any, dtypes.StringDType], /, *args: CanIndex) -> str: ...
    @overload  # use the same output type as that of the underlying `generic`
    def item(self: _HasDTypeWithItem[_T], /) -> _T: ...
    @overload
    def item(self: _HasDTypeWithItem[_T], arg0: CanIndex | tuple[CanIndex, ...] = ..., /) -> _T: ...
    @overload
    def item(self: _HasDTypeWithItem[_T], /, *args: CanIndex) -> _T: ...

    #
    @override
    @overload  # workaround for python/mypy#19110
    def tolist(self: _HasShapeAndItem[_nt.Rank0, _T], /) -> _T: ...  # type: ignore[overload-overlap]
    @overload  # workaround for microsoft/pyright#10232
    def tolist(self: ndarray[_nt.NeitherShape], /) -> Any: ...
    @overload
    def tolist(self: _HasShapeAndItem[_nt.Shape0, _T], /) -> _T: ...
    @overload
    def tolist(self: _HasShapeAndItem[_nt.Shape1, _T], /) -> list[_T]: ...
    @overload
    def tolist(self: _HasShapeAndItem[_nt.Shape2, _T], /) -> list[list[_T]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[_nt.Shape3, _T], /) -> list[list[list[_T]]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[_nt.Shape4, _T], /) -> list[list[list[list[_T]]]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[Any, _T], /) -> Any: ...

    #
    @overload
    def resize(self, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(self: ndarray[_ShapeT], new_shape: _ShapeT, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(self: ndarray[_nt.Shape1], n0: CanIndex, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(self: ndarray[_nt.Shape2], n0: CanIndex, n1: CanIndex, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(
        self: ndarray[_nt.Shape3], n0: CanIndex, n1: CanIndex, n2: CanIndex, /, *, refcheck: py_bool = True
    ) -> None: ...
    @overload
    def resize(
        self: ndarray[_nt.Shape4],
        n0: CanIndex,
        n1: CanIndex,
        n2: CanIndex,
        n3: CanIndex,
        /,
        *,
        refcheck: py_bool = True,
    ) -> None: ...

    #
    def swapaxes(self, /, axis1: CanIndex, axis2: CanIndex) -> Self: ...
    def squeeze(self, /, axis: CanIndex | tuple[CanIndex, ...] | None = None) -> ndarray[_nt.AnyShape, _DTypeT_co]: ...
    def byteswap(self, /, inplace: py_bool = False) -> Self: ...

    #
    @overload
    def transpose(self, axes: _ShapeLike | None, /) -> Self: ...
    @overload
    def transpose(self, /, *axes: CanIndex) -> Self: ...

    # NOTE: always raises when called on `generic`.
    @overload  # this overload is a workaround for microsoft/pyright#10232
    def diagonal(  # type: ignore[overload-overlap]
        self: ndarray[_nt.NeitherShape, _DTypeT], /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.AnyShape, _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[_nt.Shape2, _DTypeT], /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.Rank1, _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[_nt.Shape3, _DTypeT], /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.Rank2, _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[_nt.Shape4, _DTypeT], /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.Rank3, _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[_nt.Shape4N, _DTypeT], /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.Rank3N, _DTypeT]: ...
    @overload
    def diagonal(
        self, /, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
    ) -> ndarray[_nt.AnyShape, _DTypeT_co]: ...

    #
    @overload
    def all(
        self, /, axis: None = None, out: None = None, keepdims: L[False, 0] = False, *, where: _nt.ToBool_nd = True
    ) -> bool_: ...
    @overload
    def all(
        self,
        /,
        axis: _IntOrInts | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_ | _nt.Array[bool_]: ...
    @overload
    def all(
        self, /, axis: _IntOrInts | None, out: _ArrayT, keepdims: CanIndex = False, *, where: _nt.ToBool_nd = True
    ) -> _ArrayT: ...
    @overload
    def all(
        self,
        /,
        axis: _IntOrInts | None = None,
        *,
        out: _ArrayT,
        keepdims: CanIndex = False,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload
    def any(
        self, axis: None = None, out: None = None, keepdims: L[False, 0] = False, *, where: _nt.ToBool_nd = True
    ) -> bool_: ...
    @overload
    def any(
        self,
        axis: _IntOrInts | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_ | _nt.Array[bool_]: ...
    @overload
    def any(
        self, axis: _IntOrInts | None, out: _ArrayT, keepdims: CanIndex = False, *, where: _nt.ToBool_nd = True
    ) -> _ArrayT: ...
    @overload
    def any(
        self, axis: _IntOrInts | None = None, *, out: _ArrayT, keepdims: CanIndex = False, where: _nt.ToBool_nd = True
    ) -> _ArrayT: ...

    #
    def argpartition(
        self,
        kth: _nt.CoInteger_nd,
        axis: CanIndex | None = ...,
        kind: _PartitionKind = ...,
        order: str | Sequence[str] | None = ...,
    ) -> _nt.Array[intp]: ...

    # 1D + 1D returns a scalar; # all other with at least 1 non-0D array return an ndarray.
    @overload
    def dot(self, b: _ScalarLike_co, out: None = ...) -> _nt.Array: ...
    @overload
    def dot(self, b: ArrayLike, out: None = ...) -> Any: ...
    @overload
    def dot(self, b: ArrayLike, out: _ArrayT) -> _ArrayT: ...

    # `nonzero()` is deprecated for 0d arrays/generics
    def nonzero(self) -> tuple[_nt.Array[intp], ...]: ...

    #
    @overload
    def searchsorted(
        self, /, v: _ScalarLike_co, side: _SortSide = "left", sorter: _nt.CoInteger_nd | None = None
    ) -> intp: ...
    @overload
    def searchsorted(
        self, /, v: ndarray[_ShapeT], side: _SortSide = "left", sorter: _nt.CoInteger_nd | None = None
    ) -> _nt.Array[intp, _ShapeT]: ...
    @overload
    def searchsorted(
        self, /, v: _NestedSequence[_ScalarLike_co], side: _SortSide = "left", sorter: _nt.CoInteger_nd | None = None
    ) -> _nt.Array[intp]: ...
    @overload
    def searchsorted(
        self, /, v: ArrayLike, side: _SortSide = "left", sorter: _nt.CoInteger_nd | None = None
    ) -> intp | _nt.Array[intp]: ...

    #
    @overload
    def sort(
        self, /, axis: CanIndex = -1, kind: _SortKind | None = None, order: None = None, *, stable: bool | None = None
    ) -> None: ...
    @overload
    def sort(
        self: _nt.Array[void, Any],
        /,
        axis: CanIndex = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        *,
        stable: bool | None = None,
    ) -> None: ...

    #
    @overload
    def argsort(
        self, /, axis: CanIndex = -1, kind: _SortKind | None = None, order: None = None, *, stable: bool | None = None
    ) -> _nt.Array[intp, _ShapeT_co]: ...
    @overload
    def argsort(
        self, /, axis: None, kind: _SortKind | None = None, order: None = None, *, stable: bool | None = None
    ) -> _nt.Array1D[intp]: ...
    @overload
    def argsort(
        self: _nt.Array[void, _ShapeT],
        /,
        axis: CanIndex = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        *,
        stable: bool | None = None,
    ) -> _nt.Array[intp, _ShapeT]: ...
    @overload
    def argsort(
        self: _nt.Array[void, Any],
        /,
        axis: None,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        *,
        stable: bool | None = None,
    ) -> _nt.Array1D[intp]: ...

    #
    @overload
    def partition(
        self, /, kth: _nt.CoInteger_nd, axis: CanIndex = -1, kind: _PartitionKind = "introselect", order: None = None
    ) -> None: ...
    @overload
    def partition(
        self: _nt.Array[void, Any],
        /,
        kth: _nt.CoInteger_nd,
        axis: CanIndex = -1,
        kind: _PartitionKind = "introselect",
        order: str | Sequence[str] | None = None,
    ) -> None: ...

    #
    @overload  # 2d, dtype: None
    def trace(
        self: _nt.Array2D[_ScalarT],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: None = None,
        out: None = None,
    ) -> _ScalarT: ...
    @overload  # 2d, dtype: dtype[T], /
    def trace(
        self: _nt.Array2D[Any],
        /,
        offset: CanIndex,
        axis1: CanIndex,
        axis2: CanIndex,
        dtype: _DTypeLike[_ScalarT],
        out: None = None,
    ) -> _ScalarT: ...
    @overload  # 2d, *, dtype: dtype[T]
    def trace(
        self: _nt.Array2D[Any],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        *,
        dtype: _DTypeLike[_ScalarT],
        out: None = None,
    ) -> _ScalarT: ...
    @overload  # ?d, out: T, /
    def trace(
        self, /, offset: CanIndex, axis1: CanIndex, axis2: CanIndex, dtype: DTypeLike | None, out: _ArrayT
    ) -> _ArrayT: ...
    @overload  # ?d, *, out: T
    def trace(
        self,
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload  # ?d, dtype: ?
    def trace(
        self,
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: DTypeLike | None = None,
        out: None = None,
    ) -> Any: ...

    #
    @overload
    def take(
        self: _nt.Array[_ScalarT],
        /,
        indices: _nt.CoInteger_0d,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> _ScalarT: ...
    @overload
    def take(
        self, /, indices: _nt.CoInteger_nd, axis: CanIndex | None = None, out: None = None, mode: _ModeKind = "raise"
    ) -> ndarray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def take(
        self, /, indices: _nt.CoInteger_nd, axis: CanIndex | None, out: _ArrayT, mode: _ModeKind = "raise"
    ) -> _ArrayT: ...
    @overload
    def take(
        self, /, indices: _nt.CoInteger_nd, axis: CanIndex | None = None, *, out: _ArrayT, mode: _ModeKind = "raise"
    ) -> _ArrayT: ...

    #
    @overload
    def repeat(self, /, repeats: _nt.CoInteger_nd, axis: None = None) -> ndarray[_nt.Rank1, _DTypeT_co]: ...
    @overload
    def repeat(
        self: ndarray[_AnyShapeT, _DTypeT], /, repeats: _nt.CoInteger_nd, axis: CanIndex
    ) -> ndarray[_AnyShapeT, _DTypeT]: ...

    #
    def flatten(self, /, order: _OrderKACF = "C") -> ndarray[_nt.Rank1, _DTypeT_co]: ...
    def ravel(self, /, order: _OrderKACF = "C") -> ndarray[_nt.Rank1, _DTypeT_co]: ...

    #
    @overload  # (None)
    def reshape(self, shape: None, /, *, order: _OrderACF = "C", copy: py_bool | None = None) -> Self: ...
    @overload  # (empty_sequence)
    def reshape(  # type: ignore[overload-overlap]  # mypy false positive
        self, shape: Sequence[Never] | _nt.Shape0, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank0, _DTypeT_co]: ...
    @overload  # (index)
    def reshape(
        self, size1: CanIndex | _nt.Shape1, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank1, _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self, size1: _nt.Shape2, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self, size1: CanIndex, size2: CanIndex, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (index, index, index)
    def reshape(
        self, size1: _nt.Shape3, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank3, _DTypeT_co]: ...
    @overload  # (index, index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[_nt.Rank3, _DTypeT_co]: ...
    @overload  # (index, index, index, index)
    def reshape(
        self, size1: _nt.Shape4, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[_nt.Rank4, _DTypeT_co]: ...
    @overload  # (index, index, index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        size4: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[_nt.Rank4, _DTypeT_co]: ...
    @overload  # (int, *(index, ...))
    def reshape(
        self, size0: CanIndex, /, *shape: CanIndex, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[Incomplete, _DTypeT_co]: ...
    @overload  # (sequence[index])
    def reshape(
        self, shape: Sequence[CanIndex], /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> ndarray[Incomplete, _DTypeT_co]: ...

    #
    @overload
    def astype(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        order: _OrderKACF = "K",
        casting: _CastingKind = "unsafe",
        subok: py_bool = True,
        copy: py_bool | _CopyMode = True,
    ) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @overload
    def astype(
        self,
        /,
        dtype: DTypeLike,
        order: _OrderKACF = "K",
        casting: _CastingKind = "unsafe",
        subok: py_bool = True,
        copy: py_bool | _CopyMode = True,
    ) -> ndarray[_ShapeT_co]: ...

    # the special casings work around the lack of higher-kinded typing (HKT) support in Python
    @overload  # ()
    def view(self, /) -> Self: ...
    @overload  # (dtype: T)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT]) -> ndarray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T])
    def view(self, /, dtype: _DTypeLike[_ScalarT]) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @overload  # (type: matrix)
    def view(self, /, *, type: type[matrix]) -> matrix[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (_: matrix)
    def view(self, /, dtype: type[matrix]) -> matrix[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (dtype: T, type: matrix)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT], type: type[matrix]) -> matrix[_nt.Rank2, _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: matrix)
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[matrix]) -> _nt.Matrix[_ScalarT]: ...
    @overload  # (type: recarray)
    def view(self, /, *, type: type[recarray]) -> recarray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: recarray)
    def view(self, /, dtype: type[recarray]) -> recarray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (dtype: T, type: recarray)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT], type: type[recarray]) -> recarray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: recarray)
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[recarray]) -> recarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload  # (type: char.chararray)
    def view(
        self: ndarray[_ShapeT, _CharDTypeT], /, *, type: type[char.chararray]
    ) -> char.chararray[_ShapeT, _CharDTypeT]: ...
    @overload  # (_: char.chararray)
    def view(
        self: ndarray[_ShapeT, _CharDTypeT], /, dtype: type[char.chararray]
    ) -> char.chararray[_ShapeT, _CharDTypeT]: ...
    @overload  # (dtype: T, type: char.chararray)
    def view(
        self, /, dtype: _CharDTypeT | _HasDType[_CharDTypeT], type: type[char.chararray]
    ) -> char.chararray[_ShapeT_co, _CharDTypeT]: ...
    @overload  # (dtype: dtype[T], type: char.chararray)
    def view(
        self, /, dtype: _DTypeLike[_CharT], type: type[char.chararray]
    ) -> char.chararray[_ShapeT_co, dtype[_CharT]]: ...
    @overload  # (type: MaskedArray)
    def view(self, /, *, type: type[ma.MaskedArray]) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: MaskedArray)
    def view(self, /, dtype: type[ma.MaskedArray]) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (dtype: T, type: MaskedArray)
    def view(
        self, /, dtype: _DTypeT | _HasDType[_DTypeT], type: type[ma.MaskedArray]
    ) -> ma.MaskedArray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: MaskedArray)
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[ma.MaskedArray]) -> _nt.MArray[_ScalarT, _ShapeT_co]: ...
    @overload  # (type: T)
    def view(self, /, *, type: type[_ArrayT]) -> _ArrayT: ...
    @overload  # (_: T)
    def view(self, /, dtype: type[_ArrayT]) -> _ArrayT: ...
    @overload  # (dtype: ?)
    def view(self, /, dtype: DTypeLike) -> ndarray[_ShapeT_co]: ...
    @overload  # (dtype: ?, type: type[T])
    def view(self, /, dtype: DTypeLike, type: type[_ArrayT]) -> _ArrayT: ...

    #
    @overload
    def getfield(self, /, dtype: _DTypeLike[_ScalarT], offset: CanIndex = 0) -> _nt.Array[_ScalarT]: ...
    @overload
    def getfield(self, /, dtype: DTypeLike, offset: CanIndex = 0) -> _nt.Array: ...

    #
    def setfield(self, /, val: ArrayLike, dtype: DTypeLike, offset: CanIndex = 0) -> None: ...

    # keep `dtype` at the bottom to avoid shadowing
    @property
    def dtype(self) -> _DTypeT_co: ...

# NOTE: while `generic` is not technically an instance of `ABCMeta`,
# the `@abc.abstractmethod` decorator is herein used to (forcefully) deny
# the creation of `generic` instances.
# The `# type: ignore` comments are necessary to silence mypy errors regarding
# the missing `ABCMeta` metaclass.
# See https://github.com/numpy/numpy-stubs/pull/80 for more details.
class generic(_ArrayOrScalarCommon, Generic[_ItemT_co]):
    @property
    @type_check_only
    def __inner_shape__(self, /) -> _nt.Rank0: ...
    @property
    def shape(self) -> _nt.Shape0: ...
    @property
    def strides(self) -> tuple[()]: ...
    @property
    def ndim(self) -> L[0]: ...
    @property
    def size(self) -> L[1]: ...
    @property
    def base(self) -> None: ...
    @property
    def flat(self) -> flatiter[_nt.Array1D[Self]]: ...

    #
    @override
    @overload
    def __eq__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __eq__(self, other: ndarray[_ShapeT], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_1nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __eq__(self, other: object, /) -> Any: ...

    #
    @override
    @overload
    def __ne__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __ne__(self, other: ndarray[_ShapeT], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_1nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __ne__(self, other: object, /) -> Any: ...

    #
    @overload
    def __array__(self, dtype: None = None, /) -> _nt.Array0D[Self]: ...
    @overload
    def __array__(self, dtype: _DTypeT, /) -> ndarray[_nt.Rank0, _DTypeT]: ...

    #
    @overload
    def __array_wrap__(
        self,
        array: _nt.Array0D[_ScalarT],
        context: tuple[ufunc, tuple[object, ...], int] | None = None,
        return_scalar: L[True] = True,
        /,
    ) -> _ScalarT: ...
    @overload
    def __array_wrap__(
        self,
        array: ndarray[_Shape1NDT, _DTypeT],
        context: tuple[ufunc, tuple[object, ...], int] | None = None,
        return_scalar: py_bool = True,
        /,
    ) -> ndarray[_Shape1NDT, _DTypeT]: ...
    @overload
    def __array_wrap__(
        self,
        array: ndarray[_ShapeT, _DTypeT],
        context: tuple[ufunc, tuple[object, ...], int] | None,
        return_scalar: L[False],
        /,
    ) -> ndarray[_ShapeT, _DTypeT]: ...
    @overload
    def __array_wrap__(
        self,
        array: _nt.Array[_ScalarT, _ShapeT],
        context: tuple[ufunc, tuple[object, ...], int] | None = None,
        return_scalar: py_bool = True,
        /,
    ) -> _ScalarT | _nt.Array[_ScalarT, _ShapeT]: ...

    #
    @overload
    def item(self, /) -> _ItemT_co: ...
    @overload
    def item(self, arg0: L[0, -1] | tuple[L[0, -1]] | tuple[()], /) -> _ItemT_co: ...
    @override
    def tolist(self, /) -> _ItemT_co: ...

    # NOTE: these technically exist, but will always raise when called
    def trace(  # type: ignore[misc]
        self: Never,
        /,
        offset: Never = ...,
        axis1: Never = ...,
        axis2: Never = ...,
        dtype: Never = ...,
        out: Never = ...,
    ) -> Never: ...
    def diagonal(self: Never, /, offset: Never = ..., axis1: Never = ..., axis2: Never = ...) -> Never: ...  # type: ignore[misc]
    def swapaxes(self: Never, /, axis1: Never, axis2: Never) -> Never: ...  # type: ignore[misc]
    def sort(self: Never, /, axis: Never = ..., kind: Never = ..., order: Never = ...) -> Never: ...  # type: ignore[misc]
    def nonzero(self: Never, /) -> Never: ...  # type: ignore[misc]
    def setfield(self: Never, /, val: Never, dtype: Never, offset: Never = ...) -> None: ...  # type: ignore[misc]
    def searchsorted(self: Never, /, v: Never, side: Never = ..., sorter: Never = ...) -> Never: ...  # type: ignore[misc]

    # NOTE: this wont't raise, but won't do anything either
    def resize(self, new_shape: L[0, -1] | tuple[L[0, -1]] | tuple[()], /, *, refcheck: py_bool = False) -> None: ...

    #
    def byteswap(self, /, inplace: L[False] = False) -> Self: ...

    #
    @overload
    def astype(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        order: _OrderKACF = "K",
        casting: _CastingKind = "unsafe",
        subok: py_bool = True,
        copy: py_bool | _CopyMode = True,
    ) -> _ScalarT: ...
    @overload
    def astype(
        self,
        /,
        dtype: DTypeLike,
        order: _OrderKACF = "K",
        casting: _CastingKind = "unsafe",
        subok: py_bool = True,
        copy: py_bool | _CopyMode = True,
    ) -> Incomplete: ...

    #
    @overload
    def view(self, /) -> Self: ...
    @overload
    def view(self, /, dtype: type[_nt.Array]) -> Self: ...
    @overload
    def view(self, /, *, type: type[_nt.Array]) -> Self: ...
    @overload
    def view(self, /, dtype: _DTypeLike[_ScalarT]) -> _ScalarT: ...
    @overload
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[_nt.Array]) -> _ScalarT: ...
    @overload
    def view(self, /, dtype: DTypeLike) -> Incomplete: ...
    @overload
    def view(self, /, dtype: DTypeLike, type: type[_nt.Array]) -> Incomplete: ...

    #
    @overload
    def getfield(self, /, dtype: _DTypeLike[_ScalarT], offset: CanIndex = 0) -> _ScalarT: ...
    @overload
    def getfield(self, /, dtype: DTypeLike, offset: CanIndex = 0) -> Incomplete: ...

    #
    @overload
    def take(
        self, /, indices: _nt.CoInteger_0d, axis: CanIndex | None = None, out: None = None, mode: _ModeKind = "raise"
    ) -> Self: ...
    @overload
    def take(
        self,
        /,
        indices: _NestedSequence[CanIndex],
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> _nt.Array[Self]: ...
    @overload
    def take(
        self, /, indices: _nt.CoInteger_nd, axis: CanIndex | None, out: _ArrayT, mode: _ModeKind = "raise"
    ) -> _ArrayT: ...
    @overload
    def take(
        self, /, indices: _nt.CoInteger_nd, axis: CanIndex | None = None, *, out: _ArrayT, mode: _ModeKind = "raise"
    ) -> _ArrayT: ...

    #
    def repeat(self, /, repeats: _nt.CoInteger_nd, axis: CanIndex | None = None) -> _nt.Array[Self]: ...

    #
    def flatten(self, /, order: _OrderKACF = "C") -> _nt.Array1D[Self]: ...
    def ravel(self, /, order: _OrderKACF = "C") -> _nt.Array1D[Self]: ...
    def squeeze(self, axis: L[0] | tuple[()] | None = None) -> Self: ...
    def transpose(self, axes: tuple[()] | None = None, /) -> Self: ...

    #
    @overload  # (() | [])
    def reshape(
        self, shape: tuple[()] | list[Never], /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> Self: ...
    @overload  # (Sequence[index, ...])  # not recommended
    def reshape(
        self, shape: Sequence[CanIndex], /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> Self | _nt.Array[Self]: ...
    @overload  # _(index)
    def reshape(
        self, size1: CanIndex, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> _nt.Array1D[Self]: ...
    @overload  # _(index, index)
    def reshape(
        self, size1: CanIndex, size2: CanIndex, /, *, order: _OrderACF = "C", copy: py_bool | None = None
    ) -> _nt.Array2D[Self]: ...
    @overload  # _(index, index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> _nt.Array3D[Self]: ...
    @overload  # _(index, index, index, index, *index)  # ndim >= 5
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        size4: CanIndex,
        /,
        *sizes5_: CanIndex,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> _nt.Array[Self, _nt.Rank4N]: ...

    #
    @overload
    def all(
        self,
        /,
        axis: _Axis0D | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_0d = True,
    ) -> bool_: ...
    @overload
    def all(
        self,
        /,
        axis: _Axis0D | None,
        out: _nt.Array0D[_ScalarT],
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_0d = True,
    ) -> _ScalarT: ...
    @overload
    def all(
        self,
        /,
        axis: _Axis0D | None = None,
        *,
        out: _nt.Array0D[_ScalarT],
        keepdims: CanIndex = False,
        where: _nt.ToBool_0d = True,
    ) -> _ScalarT: ...
    @overload
    def any(
        self,
        /,
        axis: _Axis0D | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_0d = True,
    ) -> bool_: ...
    @overload
    def any(
        self,
        /,
        axis: _Axis0D | None,
        out: _nt.Array0D[_ScalarT],
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_0d = True,
    ) -> _ScalarT: ...
    @overload
    def any(
        self,
        /,
        axis: _Axis0D | None = None,
        *,
        out: _nt.Array0D[_ScalarT],
        keepdims: CanIndex = False,
        where: _nt.ToBool_0d = True,
    ) -> _ScalarT: ...

    #
    def argsort(
        self,
        /,
        axis: CanIndex | None = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        *,
        stable: bool | None = None,
    ) -> _nt.Array1D[intp]: ...

    # Keep `dtype` at the bottom to avoid name conflicts with `dtype`
    @property
    def dtype(self) -> dtype[Self]: ...

# NOTE: Naming it `bool_` results in less unreadable type-checker output
class bool_(generic[_BoolItemT_co], Generic[_BoolItemT_co]):
    @overload
    def __new__(cls, value: L[False, 0] | _Bool0 = ..., /) -> _Bool0: ...
    @overload
    def __new__(cls, value: L[True, 1] | _Bool1, /) -> _Bool1: ...
    @overload
    def __new__(cls, value: object, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_bool: ...

    #
    @type_check_only
    def __nep50__(self, below: _nt.co_number | timedelta64, above: Never, /) -> bool_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[py_bool, bool_]: ...
    @type_check_only
    def __nep50_int__(self, /) -> intp: ...
    @type_check_only
    def __nep50_float__(self, /) -> float64: ...
    @type_check_only
    def __nep50_complex__(self, /) -> complex128: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.BoolDType: ...  # type: ignore[override]
    @property
    @override
    def itemsize(self) -> L[1]: ...
    @property
    @override
    def nbytes(self) -> L[1]: ...
    @property
    @override
    def real(self) -> Self: ...
    @property
    @override
    def imag(self) -> _Bool0: ...

    #
    @override
    def __hash__(self, /) -> int: ...
    @override
    def __bool__(self, /) -> _BoolItemT_co: ...
    @override
    def __int__(self, /) -> L[0, 1]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __eq__(self: _Bool0, other: _ToFalse, /) -> _Bool1: ...
    @overload
    def __eq__(self: _Bool1, other: _ToFalse, /) -> _Bool0: ...
    @overload
    def __eq__(self, other: _ToTrue, /) -> Self: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __eq__(self, other: ndarray[_ShapeT], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_1nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __eq__(self, other: object, /) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __ne__(self: _Bool0, other: _ToTrue, /) -> _Bool1: ...
    @overload
    def __ne__(self: _Bool1, other: _ToTrue, /) -> _Bool0: ...
    @overload
    def __ne__(self, other: _ToFalse, /) -> Self: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __ne__(self, other: ndarray[_ShapeT], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_1nd, /) -> _nt.Array[bool_]: ...
    @overload
    def __ne__(self, other: object, /) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __lt__(self: _Bool0, x: _ToTrue, /) -> _Bool1: ...
    @overload
    def __lt__(self: _Bool1, x: py_bool | bool_, /) -> _Bool0: ...
    @overload
    def __lt__(self, x: _ToFalse, /) -> _Bool0: ...
    @overload
    def __lt__(self, x: _nt.CoComplex_0d, /) -> bool_: ...
    @overload
    def __lt__(self, x: _nt.CoComplex_1nd, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __le__(self: _Bool0, x: py_bool | bool_, /) -> _Bool1: ...
    @overload
    def __le__(self: _Bool1, x: _ToFalse, /) -> _Bool0: ...
    @overload
    def __le__(self, x: _ToTrue, /) -> _Bool1: ...
    @overload
    def __le__(self, x: _nt.CoComplex_0d, /) -> bool_: ...
    @overload
    def __le__(self, x: _nt.CoComplex_1nd, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __gt__(self: _Bool0, x: py_bool | bool_, /) -> _Bool0: ...
    @overload
    def __gt__(self, x: _ToTrue, /) -> _Bool0: ...
    @overload
    def __gt__(self, x: _ToFalse, /) -> Self: ...
    @overload
    def __gt__(self, x: _nt.CoComplex_0d, /) -> bool_: ...
    @overload
    def __gt__(self, x: _nt.CoComplex_1nd, /) -> _nt.Array[bool_]: ...

    #
    @overload
    def __ge__(self: _Bool0, x: _ToTrue, /) -> _Bool0: ...
    @overload
    def __ge__(self: _Bool1, x: py_bool | bool_, /) -> _Bool1: ...
    @overload
    def __ge__(self, x: _ToFalse, /) -> _Bool1: ...
    @overload
    def __ge__(self, x: _nt.CoComplex_0d, /) -> bool_: ...
    @overload
    def __ge__(self, x: _nt.CoComplex_1nd, /) -> _nt.Array[bool_]: ...

    #
    def __abs__(self, /) -> Self: ...

    # NOTE: same boolean logic as __or__
    @overload
    def __add__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __add__(self: _Bool1, x: py_bool | bool_, /) -> _Bool1: ...
    @overload
    def __add__(self, x: _ToFalse, /) -> Self: ...
    @overload
    def __add__(self, x: _ToTrue, /) -> _Bool1: ...
    @overload
    def __add__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __add__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __add__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __add__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __radd__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __radd__(self: _Bool1, x: py_bool, /) -> _Bool1: ...
    @overload
    def __radd__(self, x: L[False], /) -> Self: ...
    @overload
    def __radd__(self, x: L[True], /) -> _Bool1: ...
    @overload
    def __radd__(self, x: py_bool, /) -> bool_: ...
    @overload
    def __radd__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __radd__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __radd__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __sub__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __sub__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __sub__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __sub__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __rsub__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __rsub__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __rsub__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __rsub__(self, x: _nt.JustComplex, /) -> complex128: ...

    # NOTE: same boolean logic as __and__
    @overload
    def __mul__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __mul__(self: _Bool0, x: py_bool | bool_, /) -> _Bool0: ...
    @overload
    def __mul__(self, x: _ToFalse, /) -> _Bool0: ...
    @overload
    def __mul__(self, x: _ToTrue, /) -> Self: ...
    @overload
    def __mul__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __mul__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __mul__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __mul__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __rmul__(self, x: _NumberT, /) -> _NumberT: ...
    @overload
    def __rmul__(self: _Bool0, x: py_bool, /) -> _Bool0: ...
    @overload
    def __rmul__(self, x: L[False], /) -> _Bool0: ...
    @overload
    def __rmul__(self, x: L[True], /) -> Self: ...
    @overload
    def __rmul__(self, x: py_bool, /) -> bool_: ...
    @overload
    def __rmul__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __rmul__(self, x: _nt.JustFloat, /) -> float64: ...
    @overload
    def __rmul__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __pow__(self, x: _NumberT, mod: None = None, /) -> _NumberT: ...
    @overload
    def __pow__(self, x: py_bool | bool_, mod: None = None, /) -> int8: ...
    @overload
    def __pow__(self, x: _nt.JustInt, mod: None = None, /) -> intp: ...
    @overload
    def __pow__(self, x: _nt.JustFloat, mod: None = None, /) -> float64: ...
    @overload
    def __pow__(self, x: _nt.JustComplex, mod: None = None, /) -> complex128: ...

    #
    @overload
    def __rpow__(self, x: _NumberT, mod: None = None, /) -> _NumberT: ...
    @overload
    def __rpow__(self, x: py_bool, mod: None = None, /) -> int8: ...
    @overload
    def __rpow__(self, x: _nt.JustInt, mod: None = None, /) -> intp: ...
    @overload
    def __rpow__(self, x: _nt.JustFloat, mod: None = None, /) -> float64: ...
    @overload
    def __rpow__(self, x: _nt.JustComplex, mod: None = None, /) -> complex128: ...

    #
    @overload
    def __truediv__(self, x: _InexactT, /) -> _InexactT: ...
    @overload
    def __truediv__(self, x: _nt.CoFloat64_0d, /) -> float64: ...
    @overload
    def __truediv__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __rtruediv__(self, x: _InexactT, /) -> _InexactT: ...
    @overload
    def __rtruediv__(self, x: _nt.CoFloat64_0d, /) -> float64: ...
    @overload
    def __rtruediv__(self, x: _nt.JustComplex, /) -> complex128: ...

    #
    @overload
    def __floordiv__(self, x: _RealNumberT, /) -> _RealNumberT: ...
    @overload
    def __floordiv__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __floordiv__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __floordiv__(self, x: _nt.JustFloat, /) -> float64: ...

    #
    @overload
    def __rfloordiv__(self, x: _RealNumberT, /) -> _RealNumberT: ...
    @overload
    def __rfloordiv__(self, x: py_bool, /) -> int8: ...
    @overload
    def __rfloordiv__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __rfloordiv__(self, x: _nt.JustFloat, /) -> float64: ...

    # keep in sync with __floordiv__
    @overload
    def __mod__(self, x: _RealNumberT, /) -> _RealNumberT: ...
    @overload
    def __mod__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __mod__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __mod__(self, x: _nt.JustFloat, /) -> float64: ...

    # keep in sync with __rfloordiv__
    @overload
    def __rmod__(self, x: _RealNumberT, /) -> _RealNumberT: ...
    @overload
    def __rmod__(self, x: py_bool, /) -> int8: ...
    @overload
    def __rmod__(self, x: _nt.JustInt, /) -> intp: ...
    @overload
    def __rmod__(self, x: _nt.JustFloat, /) -> float64: ...

    # keep in sync with __mod__
    @overload
    def __divmod__(self, x: _RealNumberT, /) -> _Tuple2[_RealNumberT]: ...
    @overload
    def __divmod__(self, x: py_bool | bool_, /) -> _Tuple2[int8]: ...
    @overload
    def __divmod__(self, x: _nt.JustInt, /) -> _Tuple2[intp]: ...
    @overload
    def __divmod__(self, x: _nt.JustFloat, /) -> _Tuple2[float64]: ...

    # keep in sync with __rmod__
    @overload
    def __rdivmod__(self, x: _RealNumberT, /) -> _Tuple2[_RealNumberT]: ...
    @overload
    def __rdivmod__(self, x: py_bool, /) -> _Tuple2[int8]: ...
    @overload
    def __rdivmod__(self, x: _nt.JustInt, /) -> _Tuple2[intp]: ...
    @overload
    def __rdivmod__(self, x: _nt.JustFloat, /) -> _Tuple2[float64]: ...

    #
    @overload
    def __lshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __lshift__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __lshift__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __rlshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rlshift__(self, x: py_bool, /) -> int8: ...
    @overload
    def __rlshift__(self, x: _nt.JustInt, /) -> intp: ...

    # keep in sync with __lshift__
    @overload
    def __rshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rshift__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __rshift__(self, x: _nt.JustInt, /) -> intp: ...

    # keep in sync with __rlshift__
    @overload
    def __rrshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rrshift__(self, x: py_bool, /) -> int8: ...
    @overload
    def __rrshift__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __invert__(self: _Bool0, /) -> _Bool1: ...
    @overload
    def __invert__(self: _Bool1, /) -> _Bool0: ...
    @overload
    def __invert__(self, /) -> bool_: ...

    #
    @overload
    def __and__(self: _Bool0, x: py_bool | bool_, /) -> _Bool0: ...
    @overload
    def __and__(self, x: _ToFalse, /) -> _Bool0: ...
    @overload
    def __and__(self, x: _ToTrue, /) -> Self: ...
    @overload
    def __and__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __and__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __and__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __rand__(self: _Bool0, x: py_bool, /) -> _Bool0: ...
    @overload
    def __rand__(self, x: L[False], /) -> _Bool0: ...
    @overload
    def __rand__(self, x: L[True], /) -> Self: ...
    @overload
    def __rand__(self, x: py_bool, /) -> bool_: ...
    @overload
    def __rand__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rand__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __xor__(self: _Bool0, x: _ToTrue, /) -> _Bool1: ...
    @overload
    def __xor__(self: _Bool1, x: _ToTrue, /) -> _Bool0: ...
    @overload
    def __xor__(self, x: _ToFalse, /) -> Self: ...
    @overload
    def __xor__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __xor__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __xor__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __rxor__(self: _Bool0, x: L[True], /) -> _Bool1: ...
    @overload
    def __rxor__(self: _Bool1, x: L[True], /) -> _Bool0: ...
    @overload
    def __rxor__(self, x: L[False], /) -> Self: ...
    @overload
    def __rxor__(self, x: py_bool, /) -> bool_: ...
    @overload
    def __rxor__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rxor__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __or__(self: _Bool1, x: py_bool | bool_, /) -> _Bool1: ...
    @overload
    def __or__(self, x: _ToFalse, /) -> Self: ...
    @overload
    def __or__(self, x: _ToTrue, /) -> _Bool1: ...
    @overload
    def __or__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __or__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __or__(self, x: _nt.JustInt, /) -> intp: ...

    #
    @overload
    def __ror__(self: _Bool1, x: py_bool, /) -> _Bool1: ...
    @overload
    def __ror__(self, x: L[False], /) -> Self: ...
    @overload
    def __ror__(self, x: L[True], /) -> _Bool1: ...
    @overload
    def __ror__(self, x: py_bool, /) -> bool_: ...
    @overload
    def __ror__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __ror__(self, x: _nt.JustInt, /) -> intp: ...

bool = bool_

class number(_CmpOpMixin[_nt.CoComplex_0d, _nt.CoComplex_1nd], generic[_NumberItemT_co], Generic[_NumberItemT_co]):
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[int, Self]: ...
    @final
    @type_check_only
    def __nep50_int__(self, /) -> Self: ...
    @type_check_only
    def __nep50_float__(self, /) -> inexact: ...
    @type_check_only
    def __nep50_complex__(self, /) -> complexfloating: ...
    @type_check_only
    def __nep50_rule6__(self, other: _JustNumber, /) -> number: ...

    #
    @property
    @override
    def itemsize(self) -> int: ...

    #
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

    #
    def __abs__(self, /) -> number: ...
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...

    #
    @overload
    def __add__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __add__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __add__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __add__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __radd__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __radd__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __radd__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __radd__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __sub__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __sub__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __sub__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __sub__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __rsub__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rsub__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __rsub__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __rsub__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __mul__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __mul__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __mul__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __mul__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __rmul__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rmul__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __rmul__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __rmul__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __pow__(self, x: _nt.CastsScalar[Self] | int, mod: None = None, /) -> Self: ...
    @overload
    def __pow__(self, x: _nt.CastsWithScalar[Self, _ScalarT], mod: None = None, /) -> _ScalarT: ...
    @overload
    def __pow__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, mod: None = None, /) -> _InexactT: ...
    @overload
    def __pow__(
        self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, mod: None = None, /
    ) -> _ComplexFloatT: ...

    # keep in sync with __add__
    @overload
    def __rpow__(self, x: _nt.CastsScalar[Self] | int, mod: None = None, /) -> Self: ...
    @overload
    def __rpow__(self, x: _nt.CastsWithScalar[Self, _ScalarT], mod: None = None, /) -> _ScalarT: ...
    @overload
    def __rpow__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, mod: None = None, /) -> _InexactT: ...
    @overload
    def __rpow__(
        self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, mod: None = None, /
    ) -> _ComplexFloatT: ...

    #
    @overload
    def __truediv__(self, x: _nt.CoFloat64_0d | _nt.CastsScalar[Self] | _JustNumber, /) -> inexact: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

    #
    @overload
    def __rtruediv__(self, x: _nt.CoFloat64_0d | _nt.CastsScalar[Self] | _JustNumber, /) -> inexact: ...
    @overload
    def __rtruediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...

# NOTE: at least ~95% of the relevant platforms are 64-bit at the moment, and this
# increases over time. Assuming that this *always* holds significantly reduces the
# complexity of the `[u]intp` and `[u]long` type definitions.

class integer(_IntegralMixin, _RoundMixin, number[int]):
    @type_check_only
    def __nep50__(
        self, below: timedelta64 | _Inexact64_min | _JustFloating | _JustInexact, above: bool_, /
    ) -> integer: ...
    @final
    @override
    @type_check_only
    def __nep50_float__(self, /) -> float64: ...
    @final
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex128: ...
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger | float64: ...
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer | float64: ...

    #
    @override
    def __abs__(self, /) -> Self: ...
    def __invert__(self, /) -> Self: ...

    #
    @override  # type: ignore[override]
    @overload
    def __truediv__(self, x: _nt.CoInteger_0d | float, /) -> float64: ...
    @overload
    def __truediv__(self, x: _nt.JustComplex, /) -> complex128: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __rtruediv__(self, x: _nt.CoInteger_0d | float, /) -> float64: ...
    @overload
    def __rtruediv__(self, x: _nt.JustComplex, /) -> complex128: ...
    @overload
    def __rtruediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __floordiv__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __floordiv__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _RealScalarT: ...
    @overload
    def __floordiv__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...

    #
    @overload
    def __rfloordiv__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rfloordiv__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _RealScalarT: ...
    @overload
    def __rfloordiv__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...

    #
    @overload
    def __mod__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __mod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _RealScalarT: ...
    @overload
    def __mod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...

    #
    @overload
    def __rmod__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rmod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _RealScalarT: ...
    @overload
    def __rmod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...

    #
    @overload
    def __divmod__(self, x: _nt.CastsScalar[Self] | int, /) -> _Tuple2[Self]: ...
    @overload
    def __divmod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _Tuple2[_RealScalarT]: ...
    @overload
    def __divmod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _Tuple2[_InexactT]: ...

    #
    @overload
    def __rdivmod__(self, x: _nt.CastsScalar[Self] | int, /) -> _Tuple2[Self]: ...
    @overload
    def __rdivmod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _Tuple2[_RealScalarT]: ...
    @overload
    def __rdivmod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _Tuple2[_InexactT]: ...

    #
    @overload
    def __lshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __lshift__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __rlshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rlshift__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __rshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rshift__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __rrshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rrshift__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __and__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __and__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __rand__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rand__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __xor__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __xor__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __rxor__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rxor__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __or__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __or__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

    #
    @overload
    def __ror__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __ror__(self, x: _nt.CastsWithScalar[Self, _IntegralT], /) -> _IntegralT: ...

class signedinteger(integer):
    @type_check_only
    @override
    def __nep50__(
        self, below: int64 | timedelta64 | _Inexact64_min | _JustFloating | _JustInexact, above: bool_, /
    ) -> signedinteger: ...
    @type_check_only
    def __nep50_rule0__(self, other: uint32, /) -> int64: ...
    @type_check_only
    def __nep50_rule1__(self, other: uint64, /) -> float64: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger | _JustUnsignedInteger, /) -> signedinteger | float64: ...

class int8(_IntMixin[L[1]], signedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_int8: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: signedinteger | timedelta64 | inexact | _JustFloating | _JustInexact, above: bool_, /
    ) -> int8: ...
    @type_check_only
    def __nep50_rule2__(self, other: uint8, /) -> int16: ...
    @type_check_only
    def __nep50_rule3__(self, other: uint16, /) -> int32: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Int8DType: ...

byte = int8

class int16(_IntMixin[L[2]], signedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_int16: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self,
        below: _I16_min | timedelta64 | _F32_min | _JustFloating | complexfloating | _JustInexact,
        above: _nt.co_integer8,
        /,
    ) -> int16: ...
    @type_check_only
    def __nep50_rule2__(self, other: uint16, /) -> int32: ...
    @type_check_only
    def __nep50_rule3__(self, other: float16, /) -> float32: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Int16DType: ...

short = int16

class int32(_IntMixin[L[4]], signedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_int32: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: _I32_min | timedelta64 | _Inexact64_min | _JustFloating | _JustInexact, above: _nt.co_integer16, /
    ) -> int32: ...
    @override
    @type_check_only
    def __nep50_rule1__(self, other: uint64 | float16 | float32, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustComplexFloating, /) -> complexfloating: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Int32DType: ...

intc = int32

class int64(_IntMixin[L[8]], signedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_int64: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: int64 | timedelta64 | _Inexact64_min | _JustFloating | _JustInexact, above: _nt.co_integer32, /
    ) -> int64: ...
    @override
    @type_check_only
    def __nep50_rule1__(self, other: uint64 | float16 | float32, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustComplexFloating, /) -> complexfloating: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger | signedinteger, /) -> Self: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger | _JustUnsignedInteger, /) -> Self | float64: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Int64DType: ...

if sys.platform == "win32":
    long: TypeAlias = int32  # pyright: ignore[reportRedeclaration]  # noqa: PYI042
else:
    long: TypeAlias = int64  # pyright: ignore[reportRedeclaration]  # noqa: PYI042

longlong = int64

intp = int64
int_ = intp

class unsignedinteger(integer):
    @type_check_only
    @override
    def __nep50__(
        self, below: uint64 | timedelta64 | _Inexact64_min | _JustFloating | _JustInexact, above: bool_, /
    ) -> unsignedinteger: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustUnsignedInteger, /) -> unsignedinteger: ...

class uint8(_IntMixin[L[1]], unsignedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_uint8: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: _I16_min | unsignedinteger | timedelta64 | _JustFloating | inexact | _JustInexact, above: bool_, /
    ) -> uint8: ...
    @type_check_only
    def __nep50_rule0__(self, other: int8, /) -> int16: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.UInt8DType: ...

ubyte = uint8

class uint16(_IntMixin[L[2]], unsignedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_uint16: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self,
        below: uint16 | _Integer32_min | timedelta64 | _F32_min | _JustFloating | complexfloating | _JustInexact,
        above: _nt.co_uint8,
        /,
    ) -> uint16: ...
    @type_check_only
    def __nep50_rule0__(self, other: _I16_max, /) -> int32: ...
    @type_check_only
    def __nep50_rule1__(self, other: float16, /) -> float32: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.UInt16DType: ...

ushort = uint16

class uint32(_IntMixin[L[4]], unsignedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_uint32: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: uint32 | _nt.integer64 | timedelta64 | _Inexact64_min | _AbstractInexact, above: _nt.co_uint16, /
    ) -> uint32: ...
    @type_check_only
    def __nep50_rule1__(self, other: float16 | float32, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: signedinteger | _JustSignedInteger, /) -> int64: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.UInt32DType: ...

uintc = uint32

class uint64(_IntMixin[L[8]], unsignedinteger):
    def __new__(cls, value: _ConvertibleToInt = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_uint64: ...

    #
    @override
    @type_check_only
    def __nep50__(
        self, below: uint64 | timedelta64 | _Inexact64_min | _AbstractInexact, above: _nt.co_uint32, /
    ) -> uint64: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustUnsignedInteger, /) -> uint64: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger | signedinteger | float16 | float32, /) -> float64: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> uint64 | float64: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.UInt64DType: ...

if sys.platform == "win32":
    ulong: TypeAlias = uint32  # pyright: ignore[reportRedeclaration]  # noqa: PYI042
else:
    ulong: TypeAlias = uintp  # pyright: ignore[reportRedeclaration]  # noqa: PYI042

ulonglong = uint64

uintp = uint64
uint = uintp

class inexact(number[_InexactItemT_co], Generic[_InexactItemT_co]):
    @type_check_only
    def __nep50__(self, below: clongdouble, above: _nt.co_integer8, /) -> inexact: ...
    @final
    @override
    @type_check_only
    def __nep50_float__(self, /) -> Self: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> inexact: ...
    @type_check_only
    def __nep50_rule4__(self, other: _JustComplexFloating, /) -> complexfloating: ...
    @override
    @type_check_only
    def __nep50_rule6__(self, other: _JustInexact | _JustNumber, /) -> inexact: ...

    #
    @override
    def __abs__(self, /) -> floating: ...

    #
    @override  # type: ignore[override]
    @overload
    def __truediv__(self, x: int | _nt.JustFloat | _nt.CastsScalar[Self], /) -> Self: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __rtruediv__(self, x: int | _nt.JustFloat | _nt.CastsScalar[Self], /) -> Self: ...
    @overload
    def __rtruediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ComplexFloatT], x: _nt.JustComplex, /) -> _ComplexFloatT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class floating(_RealMixin, _RoundMixin, inexact[float]):
    @override
    @type_check_only
    def __nep50__(self, below: _nt.inexact64l, above: _nt.co_integer8, /) -> floating: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> floating: ...

    #
    @override
    def __abs__(self, /) -> Self: ...

    #
    @overload
    def __floordiv__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> Self: ...
    @overload
    def __floordiv__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _FloatingT: ...

    #
    @overload
    def __rfloordiv__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> Self: ...
    @overload
    def __rfloordiv__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _FloatingT: ...

    #
    @overload
    def __mod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> Self: ...
    @overload
    def __mod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _FloatingT: ...

    #
    @overload
    def __rmod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> Self: ...
    @overload
    def __rmod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _FloatingT: ...

    #
    @overload
    def __divmod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> _Tuple2[Self]: ...
    @overload
    def __divmod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _Tuple2[_FloatingT]: ...

    #
    @overload
    def __rdivmod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> _Tuple2[Self]: ...
    @overload
    def __rdivmod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _Tuple2[_FloatingT]: ...

class float16(_FloatMixin[L[2]], floating):
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: inexact, above: _nt.co_integer8, /) -> float16: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex64: ...
    @type_check_only
    def __nep50_rule0__(self, other: _nt.integer16, /) -> float32: ...
    @type_check_only
    def __nep50_rule1__(self, other: _nt.integer32 | _nt.integer64, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: _AbstractInteger, /) -> floating: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Float16DType: ...

half = float16

class float32(_FloatMixin[L[4]], floating):
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_float: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: _F32_min | complexfloating, above: float16 | _nt.co_integer16, /) -> float32: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex64: ...
    @type_check_only
    def __nep50_rule1__(self, other: _nt.integer32 | _nt.integer64, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: _AbstractInteger, /) -> floating: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Float32DType: ...

single = float32

class float64(_FloatMixin[L[8]], floating, float):  # type: ignore[misc]
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_double: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: _Inexact64_min, above: _F32_max | _nt.co_integer, /) -> float64: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex128: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @classmethod
    def __getformat__(cls, typestr: L["double", "float"], /) -> str: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Float64DType: ...
    @property
    @override
    def real(self) -> Self: ...
    @property
    @override
    def imag(self) -> Self: ...

    #
    @override
    def __getnewargs__(self, /) -> tuple[float]: ...
    @override
    def __abs__(self, /) -> float64: ...
    @override
    def conjugate(self) -> Self: ...

double = float64

class longdouble(_FloatMixin[L[12, 16]], floating):
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...

    #
    @property
    @type_check_only
    def __ctype__(self) -> ct.c_longdouble: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: longdouble | clongdouble, above: _nt.co_float64, /) -> longdouble: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> longdouble: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: complexfloating | _JustComplexFloating, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule6__(self, other: _JustInexact | _JustNumber, /) -> longdouble | clongdouble: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.LongDoubleDType: ...

    #
    @override  # type: ignore[override]
    @overload
    def item(self, /) -> Self: ...
    @overload
    def item(self, arg0: L[0, -1] | tuple[L[0, -1]] | tuple[()], /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def tolist(self, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

float96 = longdouble
float128 = longdouble

class complexfloating(inexact[complex]):
    @override
    @type_check_only
    def __nep50__(self, below: clongdouble, above: _F32_max | _nt.co_integer16, /) -> complexfloating: ...
    @final
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> Self: ...
    @type_check_only
    def __nep50_rule2__(self, other: _AbstractInteger, /) -> complexfloating: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> complexfloating: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustComplexFloating, /) -> complexfloating: ...
    @override
    @type_check_only
    def __nep50_rule6__(self, other: _JustInexact | _JustNumber, /) -> complexfloating: ...

    #
    @property
    @override
    def real(self) -> floating: ...
    @property
    @override
    def imag(self) -> floating: ...

    #
    @override
    def __abs__(self, /) -> floating: ...

class complex64(complexfloating):
    @overload
    def __new__(cls, real: _ConvertibleToComplex | None = 0, /) -> Self: ...
    @overload
    def __new__(cls, real: _ToReal = 0, imag: _ToImag = 0, /) -> Self: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: complexfloating, above: _F32_max | _nt.co_integer16, /) -> complex64: ...
    @type_check_only
    def __nep50_rule0__(self, other: _nt.integer32 | _nt.integer64 | float64, /) -> complex128: ...
    @type_check_only
    def __nep50_rule1__(self, other: longdouble, /) -> clongdouble: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Complex64DType: ...
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...
    @property
    @override
    def real(self) -> float32: ...
    @property
    @override
    def imag(self) -> float32: ...

    #
    @override
    def __abs__(self, /) -> float32: ...
    @override
    def __hash__(self, /) -> int: ...

    #
    def __complex__(self, /) -> complex: ...

csingle = complex64

class complex128(complexfloating, complex):
    @overload
    def __new__(cls, real: _ConvertibleToComplex | None = 0, /) -> Self: ...
    @overload
    def __new__(cls, real: _ToReal = 0, imag: _ToImag = 0, /) -> Self: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: _C128_min, above: complex64 | _F64_max | _nt.co_integer, /) -> complex128: ...
    @type_check_only
    def __nep50_rule1__(self, other: longdouble, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule2__(self, other: integer | _AbstractInteger, /) -> complex128: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.Complex128DType: ...
    @property
    @override
    def itemsize(self) -> L[16]: ...
    @property
    @override
    def nbytes(self) -> L[16]: ...
    @property
    @override
    def real(self) -> float64: ...
    @property
    @override
    def imag(self) -> float64: ...

    #
    @override
    def __abs__(self, /) -> float64: ...
    @override
    def __hash__(self, /) -> int: ...
    @override
    def conjugate(self) -> Self: ...

    #
    def __getnewargs__(self, /) -> tuple[float, float]: ...

cdouble = complex128

class clongdouble(complexfloating):
    @overload
    def __new__(cls, real: _ConvertibleToComplex | None = 0, /) -> Self: ...
    @overload
    def __new__(cls, real: _ToReal = 0, imag: _ToImag = 0, /) -> Self: ...

    #
    @override
    @type_check_only
    def __nep50__(self, below: clongdouble, above: _nt.co_number, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule2__(self, other: _AbstractInteger, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustComplexFloating, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule6__(self, other: _JustInexact | _JustNumber, /) -> clongdouble: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.CLongDoubleDType: ...
    @property
    @override
    def itemsize(self) -> L[24, 32]: ...
    @property
    @override
    def nbytes(self) -> L[24, 32]: ...
    @property
    @override
    def real(self) -> longdouble: ...
    @property
    @override
    def imag(self) -> longdouble: ...

    #
    @override  # type: ignore[override]
    @overload
    def item(self, /) -> Self: ...
    @overload
    def item(self, arg0: L[0, -1] | tuple[L[0, -1]] | tuple[()], /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def tolist(self, /) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __abs__(self, /) -> longdouble: ...
    @override
    def __hash__(self, /) -> int: ...

    #
    def __complex__(self, /) -> complex: ...

complex192 = clongdouble
complex256 = clongdouble

# NOTE: The `object_` constructor returns the passed object, so instances with type `object_` cannot exists at runtime.
# NOTE: Because mypy does not fully support `__new__`, `object_` can't be made generic.
@final
class object_(_RealMixin, generic[Any]):
    @overload
    def __new__(cls, nothing_to_see_here: None = None, /) -> None: ...  # type: ignore[misc]
    @overload
    def __new__(cls, stringy: str, /) -> str: ...  # type: ignore[misc]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __new__(cls, stringy: bytes, /) -> bytes: ...  # type: ignore[misc]
    @overload
    def __new__(cls, array: ndarray[_ShapeT], /) -> _nt.Array[Self, _ShapeT]: ...  # type: ignore[misc]
    @overload
    def __new__(cls, sequence: SupportsLenAndGetItem[object], /) -> _nt.Array[Self]: ...  # type: ignore[misc]
    @overload
    def __new__(cls, value: _T, /) -> _T: ...  # type: ignore[misc]
    @overload  # catch-all
    def __new__(cls, value: Any = ..., /) -> object | _nt.Array[Self]: ...  # type: ignore[misc]

    #
    @type_check_only
    def __nep50__(self, below: object_, above: _nt.co_number | character, /) -> object_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_JustBuiltinScalar, object_]: ...

    #
    @override
    def __hash__(self, /) -> int: ...
    def __abs__(self, /) -> object_: ...
    def __call__(self, /, *args: object, **kwargs: object) -> Incomplete: ...

    if sys.version_info >= (3, 12):
        def __release_buffer__(self, buffer: memoryview, /) -> None: ...

    @property
    @override
    def dtype(self) -> dtypes.ObjectDType: ...

@final
class flexible(_RealMixin, generic[_FlexItemT_co], Generic[_FlexItemT_co]): ...

class character(flexible[_CharacterItemT_co], Generic[_CharacterItemT_co]): ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]

class bytes_(character[bytes], bytes):  # type: ignore[misc]
    @overload
    def __new__(cls, s: str, /, encoding: str, errors: str = "strict") -> Self: ...
    @overload
    def __new__(cls, o: object = b"", /) -> Self: ...

    #
    @type_check_only
    def __nep50__(self, below: bytes_ | object_, above: Never, /) -> bytes_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_nt.JustBytes, bytes_]: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.BytesDType: ...

class str_(character[str], str):  # type: ignore[misc]
    @overload
    def __new__(cls, value: object = "", /) -> Self: ...
    @overload
    def __new__(cls, value: bytes, /, encoding: str = "utf-8", errors: str = "strict") -> Self: ...

    #
    @type_check_only
    def __nep50__(self, below: str_ | object_, above: Never, /) -> str_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_nt.JustStr, str_]: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.StrDType: ...

class void(flexible[bytes | tuple[Any, ...]]):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    @overload
    def __new__(cls, value: _nt.CoInteger_0d | bytes, /, dtype: None = None) -> Self: ...
    @overload
    def __new__(cls, value: Any, /, dtype: _DTypeLikeVoid) -> Self: ...

    #
    @type_check_only
    def __nep50__(self, below: object_, from_: Never, /) -> void: ...

    #
    @overload
    def __getitem__(self, key: str | CanIndex, /) -> Any: ...
    @overload
    def __getitem__(self, key: list[str], /) -> void: ...
    def __setitem__(self, key: str | list[str] | CanIndex, value: ArrayLike, /) -> None: ...
    @override
    def setfield(self, val: ArrayLike, dtype: DTypeLike, offset: int = ...) -> None: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.VoidDType: ...

class datetime64(
    _RealMixin, _CmpOpMixin[datetime64, _ArrayLikeDT64_co], generic[_DT64ItemT_co], Generic[_DT64ItemT_co]
):
    @overload
    def __new__(cls, /) -> datetime64[None]: ...
    @overload
    def __new__(cls, value: datetime64[_DT64ItemT_co], /) -> Self: ...
    @overload
    def __new__(cls, value: _NaTValue | None, format: _TimeUnitSpec = ..., /) -> datetime64[None]: ...
    @overload
    def __new__(cls, value: dt.datetime, /) -> datetime64[dt.datetime]: ...
    @overload
    def __new__(cls, value: dt.date, /) -> datetime64[dt.date]: ...
    @overload
    def __new__(cls, value: _DT64Now, format: _TimeUnitSpec[_NativeTimeUnit] = ..., /) -> datetime64[dt.datetime]: ...
    @overload
    def __new__(cls, value: _DT64Date, format: _TimeUnitSpec[_DateUnit] = ..., /) -> datetime64[dt.date]: ...
    @overload
    def __new__(cls, value: int | dt.date, format: _TimeUnitSpec[_IntTimeUnit], /) -> datetime64[int]: ...
    @overload
    def __new__(cls, value: int | dt.date, format: _TimeUnitSpec[_NativeTimeUnit], /) -> datetime64[dt.datetime]: ...
    @overload
    def __new__(cls, value: int | dt.date, format: _TimeUnitSpec[_DateUnit], /) -> datetime64[dt.date]: ...
    @overload
    def __new__(cls, value: bytes | str, format: _TimeUnitSpec[_IntTimeUnit], /) -> datetime64[int | None]: ...
    @overload
    def __new__(
        cls, value: bytes | str, format: _TimeUnitSpec[_NativeTimeUnit], /
    ) -> datetime64[dt.datetime | None]: ...
    @overload
    def __new__(cls, value: bytes | str, format: _TimeUnitSpec[_DateUnit], /) -> datetime64[dt.date | None]: ...
    @overload
    def __new__(cls, value: bytes | str | dt.date | None, format: _TimeUnitSpec = ..., /) -> Self: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.DateTime64DType: ...  # type: ignore[override]
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...

    #
    @overload
    def __add__(self, x: int | _nt.co_integer, /) -> Self: ...
    @overload
    def __add__(self, x: timedelta64[None], /) -> datetime64[None]: ...
    @overload
    def __add__(self: datetime64[None], x: timedelta64, /) -> datetime64[None]: ...
    @overload
    def __add__(self: datetime64[int], x: timedelta64[int | dt.timedelta], /) -> datetime64[int]: ...
    @overload
    def __add__(self: datetime64[int | dt.date], x: timedelta64[int], /) -> datetime64[int]: ...
    @overload
    def __add__(self: datetime64[dt.datetime], x: timedelta64[dt.timedelta], /) -> datetime64[dt.datetime]: ...
    @overload
    def __add__(self: datetime64[dt.date], x: timedelta64[dt.timedelta], /) -> datetime64[dt.date]: ...
    @overload
    def __add__(self, x: _TD64Like_co, /) -> datetime64: ...

    #
    @overload
    def __radd__(self, x: int | _nt.co_integer, /) -> Self: ...
    @overload
    def __radd__(self, x: timedelta64[None], /) -> datetime64[None]: ...
    @overload
    def __radd__(self: datetime64[None], x: timedelta64, /) -> datetime64[None]: ...
    @overload
    def __radd__(self: datetime64[int], x: timedelta64[int | dt.timedelta], /) -> datetime64[int]: ...
    @overload
    def __radd__(self: datetime64[int | dt.date], x: timedelta64[int], /) -> datetime64[int]: ...
    @overload
    def __radd__(self: datetime64[dt.datetime], x: timedelta64[dt.timedelta], /) -> datetime64[dt.datetime]: ...
    @overload
    def __radd__(self: datetime64[dt.date], x: timedelta64[dt.timedelta], /) -> datetime64[dt.date]: ...
    @overload
    def __radd__(self, x: _TD64Like_co, /) -> datetime64: ...

    #
    @overload
    def __sub__(self, x: int | _nt.co_integer, /) -> Self: ...
    @overload
    def __sub__(self, x: datetime64[None], /) -> timedelta64[None]: ...
    @overload
    def __sub__(self, x: timedelta64[None], /) -> datetime64[None]: ...
    @overload
    def __sub__(self: datetime64[dt.date], x: dt.date, /) -> dt.timedelta: ...
    @overload
    def __sub__(self: datetime64[None], x: datetime64, /) -> timedelta64[None]: ...
    @overload
    def __sub__(self: datetime64[None], x: timedelta64, /) -> datetime64[None]: ...
    @overload
    def __sub__(self: datetime64[int], x: datetime64[int | dt.date], /) -> timedelta64[int]: ...
    @overload
    def __sub__(self: datetime64[int], x: timedelta64[int | dt.timedelta], /) -> datetime64[int]: ...
    @overload
    def __sub__(self: datetime64[dt.datetime], x: datetime64[int], /) -> timedelta64[int]: ...
    @overload
    def __sub__(self: datetime64[dt.datetime], x: timedelta64[int], /) -> datetime64[int]: ...
    @overload
    def __sub__(self: datetime64[dt.datetime], x: timedelta64[dt.timedelta], /) -> datetime64[dt.datetime]: ...
    @overload
    def __sub__(self: datetime64[dt.date], x: datetime64[dt.date], /) -> timedelta64[dt.timedelta]: ...
    @overload
    def __sub__(self: datetime64[dt.date], x: timedelta64[dt.timedelta], /) -> datetime64[dt.date]: ...
    @overload
    def __sub__(self: datetime64[dt.date], x: timedelta64[int], /) -> datetime64[dt.date | int]: ...
    @overload
    def __sub__(self, x: _TD64Like_co, /) -> datetime64: ...
    @overload
    def __sub__(self, x: datetime64, /) -> timedelta64: ...

    #
    def __rsub__(self: datetime64[dt.date], x: dt.date, /) -> dt.timedelta: ...

class timedelta64(
    _CmpOpMixin[_nt.CoTimeDelta_0d, _nt.CoTimeDelta_1nd], _IntegralMixin, generic[_TD64ItemT_co], Generic[_TD64ItemT_co]
):
    @overload
    def __new__(cls, value: dt.timedelta | timedelta64[dt.timedelta], /) -> timedelta64[dt.timedelta]: ...
    @overload
    def __new__(cls, value: L[0] = ..., format: _TimeUnitSpec[_IntTD64Unit] = ..., /) -> timedelta64[L[0]]: ...
    @overload
    def __new__(
        cls, value: _nt.CoInteger_0d | timedelta64[int], format: _TimeUnitSpec[_IntTD64Unit] = ..., /
    ) -> timedelta64[int]: ...
    @overload
    def __new__(cls, value: dt.timedelta, format: _TimeUnitSpec[_IntTimeUnit], /) -> timedelta64[int]: ...
    @overload
    def __new__(
        cls, value: int | integer | bool_ | timedelta64[dt.timedelta | int], format: _TimeUnitSpec[_NativeTD64Unit], /
    ) -> timedelta64[dt.timedelta]: ...
    @overload
    def __new__(
        cls, value: _NaTValue | timedelta64[None] | None, format: _TimeUnitSpec = ..., /
    ) -> timedelta64[None]: ...
    @overload
    def __new__(cls, value: _ConvertibleToTD64, format: _TimeUnitSpec = ..., /) -> timedelta64[Any]: ...

    #
    @type_check_only
    def __nep50__(self, below: timedelta64, above: _nt.co_integer, /) -> timedelta64: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[int, timedelta64]: ...

    #
    @property
    @override
    def dtype(self) -> dtypes.TimeDelta64DType: ...  # type: ignore[override]
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...

    # inherited at runtime from `signedinteger`
    def __class_getitem__(cls, type_arg: type | object, /) -> GenericAlias: ...

    # NOTE: Only a limited number of units support conversion
    # to builtin scalar types: `Y`, `M`, `ns`, `ps`, `fs`, `as`
    @override
    def __int__(self: timedelta64[int], /) -> int: ...
    @override
    def __float__(self: timedelta64[int], /) -> float: ...

    #
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __abs__(self, /) -> Self: ...

    #
    @overload
    def __add__(self, x: Self | _nt.CoInteger_0d, /) -> Self: ...
    @overload
    def __add__(self, x: timedelta64[None], /) -> timedelta64[None]: ...
    @overload
    def __add__(self: timedelta64[None], x: _TD64Like_co, /) -> timedelta64[None]: ...
    @overload
    def __add__(self: timedelta64[int], x: timedelta64[int | dt.timedelta], /) -> timedelta64[int]: ...
    @overload
    def __add__(self: timedelta64[int], x: timedelta64, /) -> timedelta64[int | None]: ...
    @overload
    def __add__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __add__(self: timedelta64[dt.timedelta], x: dt.datetime, /) -> dt.datetime: ...
    @overload
    def __add__(self: timedelta64[dt.timedelta], x: dt.date, /) -> dt.date: ...

    #
    @overload
    def __radd__(self, x: _nt.CoInteger_0d, /) -> Self: ...
    @overload
    def __radd__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __radd__(self: timedelta64[dt.timedelta], x: dt.datetime, /) -> dt.datetime: ...
    @overload
    def __radd__(self: timedelta64[dt.timedelta], x: dt.date, /) -> dt.date: ...

    #
    @overload
    def __mul__(self, x: int | _nt.co_integer, /) -> Self: ...
    @overload
    def __mul__(self, x: _nt.JustFloat | floating, /) -> timedelta64[_TD64ItemT_co | None]: ...

    #
    @overload
    def __rmul__(self, x: int | _nt.co_integer, /) -> Self: ...
    @overload
    def __rmul__(self, x: _nt.JustFloat | floating, /) -> timedelta64[_TD64ItemT_co | None]: ...

    #
    @overload
    def __sub__(self, b: Self | _nt.CoInteger_0d, /) -> Self: ...
    @overload
    def __sub__(self, b: timedelta64[None], /) -> timedelta64[None]: ...
    @overload
    def __sub__(self: timedelta64[dt.timedelta], b: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __sub__(self: timedelta64[None], b: _TD64Like_co, /) -> timedelta64[None]: ...
    @overload
    def __sub__(self: timedelta64[int], b: timedelta64[int | dt.timedelta], /) -> timedelta64[int]: ...
    @overload
    def __sub__(self: timedelta64[int], b: timedelta64, /) -> timedelta64[int | None]: ...

    #
    @overload
    def __rsub__(self, a: _nt.CoInteger_0d, /) -> Self: ...
    @overload
    def __rsub__(self, a: timedelta64[None], /) -> timedelta64[None]: ...
    @overload
    def __rsub__(self: timedelta64[dt.timedelta], a: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __rsub__(self: timedelta64[dt.timedelta], a: dt.datetime, /) -> dt.datetime: ...
    @overload
    def __rsub__(self: timedelta64[dt.timedelta], a: dt.date, /) -> dt.date: ...

    #
    @overload
    def __truediv__(self, b: timedelta64, /) -> float64: ...
    @overload
    def __truediv__(self, b: _nt.JustInt | integer, /) -> Self: ...
    @overload
    def __truediv__(self, b: _nt.JustFloat | floating, /) -> timedelta64[_TD64ItemT_co | None]: ...
    @overload
    def __truediv__(self: timedelta64[dt.timedelta], b: dt.timedelta, /) -> float: ...

    #
    @overload
    def __rtruediv__(self, a: timedelta64, /) -> float64: ...
    @overload
    def __rtruediv__(self: timedelta64[dt.timedelta], a: dt.timedelta, /) -> float: ...

    #
    @overload
    def __floordiv__(self, b: timedelta64, /) -> int64: ...
    @overload
    def __floordiv__(self, b: _nt.JustInt | integer, /) -> Self: ...
    @overload
    def __floordiv__(self, b: _nt.JustFloat | floating, /) -> timedelta64[_TD64ItemT_co | None]: ...
    @overload
    def __floordiv__(self: timedelta64[dt.timedelta], b: dt.timedelta, /) -> int: ...

    #
    @overload
    def __rfloordiv__(self, a: timedelta64, /) -> int64: ...
    @overload
    def __rfloordiv__(self: timedelta64[dt.timedelta], a: dt.timedelta, /) -> int: ...

    #
    @overload
    def __mod__(self, x: timedelta64[L[0] | None], /) -> timedelta64[None]: ...
    @overload
    def __mod__(self: timedelta64[None], x: timedelta64, /) -> timedelta64[None]: ...
    @overload
    def __mod__(self, x: timedelta64[int], /) -> timedelta64[int | None]: ...
    @overload
    def __mod__(self: timedelta64[int], x: timedelta64, /) -> timedelta64[int | None]: ...
    @overload
    def __mod__(
        self: timedelta64[dt.timedelta], x: timedelta64[dt.timedelta], /
    ) -> timedelta64[dt.timedelta | None]: ...
    @overload
    def __mod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __mod__(self, x: timedelta64, /) -> timedelta64: ...

    # the L[0] makes __mod__ non-commutative, which the first two overloads reflect
    @overload
    def __rmod__(self, x: timedelta64[None], /) -> timedelta64[None]: ...  # type: ignore[misc]
    @overload
    def __rmod__(self: timedelta64[L[0] | None], x: timedelta64, /) -> timedelta64[None]: ...
    @overload
    def __rmod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> dt.timedelta: ...

    # keep in sync with __mod__
    @overload
    def __divmod__(self, x: timedelta64[L[0] | None], /) -> tuple[int64, timedelta64[None]]: ...
    @overload
    def __divmod__(self: timedelta64[None], x: timedelta64, /) -> tuple[int64, timedelta64[None]]: ...
    @overload
    def __divmod__(self, x: timedelta64[int], /) -> tuple[int64, timedelta64[int | None]]: ...
    @overload
    def __divmod__(self: timedelta64[int], x: timedelta64, /) -> tuple[int64, timedelta64[int | None]]: ...
    @overload
    def __divmod__(
        self: timedelta64[dt.timedelta], x: timedelta64[dt.timedelta], /
    ) -> tuple[int64, timedelta64[dt.timedelta | None]]: ...
    @overload
    def __divmod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> tuple[int, dt.timedelta]: ...
    @overload
    def __divmod__(self, x: timedelta64, /) -> tuple[int64, timedelta64]: ...

    # keep in sync with __rmod__
    @overload
    def __rdivmod__(self, x: timedelta64[None], /) -> tuple[int64, timedelta64[None]]: ...  # type: ignore[misc]
    @overload
    def __rdivmod__(self: timedelta64[L[0] | None], x: timedelta64, /) -> tuple[int64, timedelta64[None]]: ...
    @overload
    def __rdivmod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> tuple[int, dt.timedelta]: ...

###
# ufuncs (s See `numpy._typing._ufunc` for more concrete nin-/nout-specific stubs)

_CallT_co = TypeVar(
    "_CallT_co",
    bound=Callable[Concatenate[Never, ...], object],
    default=Callable[Concatenate[Any, ...], Any],
    covariant=True,
)
_AtT_co = TypeVar(
    "_AtT_co",
    bound=Callable[Concatenate[Never, Never, ...], None],
    default=Callable[Concatenate[Any, Any, ...], None],
    covariant=True,
)
_ReduceT_co = TypeVar(
    "_ReduceT_co",
    bound=Callable[Concatenate[Never, ...], object],
    default=Callable[Concatenate[Any, ...], Any],
    covariant=True,
)
_ReduceAtT_co = TypeVar(
    "_ReduceAtT_co",
    bound=Callable[Concatenate[Never, Never, ...], object],
    default=Callable[Concatenate[Any, Any, ...], _nt.Array[Any]],
    covariant=True,
)
_AccumulateT_co = TypeVar(
    "_AccumulateT_co",
    bound=Callable[Concatenate[Never, ...], object],
    default=Callable[Concatenate[Any, ...], ndarray[Any]],
    covariant=True,
)
_OuterT_co = TypeVar(
    "_OuterT_co",
    bound=Callable[Concatenate[Never, Never, ...], object],
    default=Callable[Concatenate[Any, Any, ...], Any],
    covariant=True,
)

@final
class ufunc(Generic[_CallT_co, _AtT_co, _ReduceT_co, _ReduceAtT_co, _AccumulateT_co, _OuterT_co]):
    __call__: _CallT_co  # method
    at: _AtT_co  # method
    reduce: _ReduceT_co  # method
    reduceat: _ReduceAtT_co  # method
    accumulate: _AccumulateT_co  # method
    outer: _OuterT_co  # method

    @property
    def __name__(self) -> str: ...
    @property
    @override
    def __qualname__(self) -> str: ...  # type: ignore[misc]  # pyright: ignore[reportIncompatibleVariableOverride]
    @property
    @override
    def __doc__(self) -> str: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleVariableOverride]

    #
    @property
    def nin(self) -> int: ...
    @property
    def nout(self) -> int: ...
    @property
    def nargs(self) -> int: ...
    @property
    def ntypes(self) -> int: ...
    @property
    def types(self) -> list[str]: ...
    @property  # in numpy this is one of `{0, -1, -inf, True, None}`
    def identity(self) -> Any | None: ...
    @property
    def signature(self) -> str | None: ...

    #
    def resolve_dtypes(
        self,
        /,
        dtypes: tuple[dtype | type | None, ...],
        *,
        signature: tuple[dtype | None, ...] | None = None,
        casting: _CastingKind | None = None,
        reduction: py_bool = False,
    ) -> tuple[dtype, ...]: ...

#  NOTE: the individual ufuncs are defined in `numpy-stubs/_core/umath.pyi`
