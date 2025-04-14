# mypy: disable-error-code=override
# ^ there are >100 false positives; we'll just rely on pyright in

import abc
import ctypes as ct
import datetime as dt
import sys
from _typeshed import Incomplete, StrOrBytesPath, SupportsFlush, SupportsLenAndGetItem, SupportsWrite
from builtins import bool as py_bool
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from decimal import Decimal
from fractions import Fraction
from types import EllipsisType, GenericAlias, GetSetDescriptorType, MappingProxyType, ModuleType
from typing import (
    Any,
    ClassVar,
    Concatenate,
    Final,
    Generic,
    Literal as L,
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
from typing_extensions import (
    Buffer,
    CapsuleType,
    LiteralString,
    Never,
    Protocol,
    Self,
    TypeVar,
    Unpack,
    deprecated,
    override,
)

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
from ._globals import _CopyMode
from ._pytesttester import PytestTester
from ._typing import (
    ArrayLike,
    DTypeLike,
    NBitBase,
    NDArray,
    _ArrayLike,
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
    _nbit_base as _n,
)
from ._typing._char_codes import _LongCodes, _ULongCodes
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
    "clongdouble", "complex128", "complex192", "complex256", "complex64", "complexfloating", "compress", "concat",
    "concatenate", "conj", "conjugate", "convolve", "copysign", "copyto", "correlate", "cos", "cosh", "count_nonzero",
    "cross", "csingle", "cumprod", "cumsum", "cumulative_prod", "cumulative_sum", "datetime64", "datetime_as_string",
    "datetime_data", "deg2rad", "degrees", "diagonal", "divide", "divmod", "dot", "double", "dtype", "e", "einsum",
    "einsum_path", "empty", "empty_like", "equal", "errstate", "euler_gamma", "exp", "exp2", "expm1", "fabs", "finfo",
    "flatiter", "flatnonzero", "flexible", "float128", "float16", "float32", "float64", "float96", "float_power",
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
    tuple[()],
    tuple[int],
    tuple[int, int],
    tuple[int, int, int],
    tuple[int, int, int, int],
    tuple[int, ...],
)

###
# Type parameters (for internal use only)

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_RealT_co = TypeVar("_RealT_co", covariant=True)
_ImagT_co = TypeVar("_ImagT_co", covariant=True)

_DTypeT = TypeVar("_DTypeT", bound=dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=dtype, covariant=True)
_FlexDTypeT = TypeVar("_FlexDTypeT", bound=dtype[flexible])

_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])
_IntegralArrayT = TypeVar("_IntegralArrayT", bound=NDArray[_nt.co_integer | object_])
_NumericArrayT = TypeVar("_NumericArrayT", bound=NDArray[number | timedelta64 | object_])

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_ShapeT_1nd = TypeVar("_ShapeT_1nd", bound=tuple[int, Unpack[tuple[int, ...]]])
_1NShapeT = TypeVar("_1NShapeT", bound=tuple[L[1], Unpack[tuple[L[1], ...]]])  # (1,) | (1, 1) | (1, 1, 1) | ...

_ScalarT = TypeVar("_ScalarT", bound=generic)
_SelfScalarT = TypeVar("_SelfScalarT", bound=generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=generic, default=Any, covariant=True)
_IntScalarT = TypeVar("_IntScalarT", bound=bool_ | integer | object_)
_RealNumberT = TypeVar("_RealNumberT", bound=integer | floating)
_RealScalarT = TypeVar("_RealScalarT", bound=bool_ | integer | floating | object_)
_IntegerT = TypeVar("_IntegerT", bound=integer)
_FloatingT = TypeVar("_FloatingT", bound=floating)
_ComplexFloatingT = TypeVar("_ComplexFloatingT", bound=complexfloating)
_InexactT = TypeVar("_InexactT", bound=inexact)
_NumberT = TypeVar("_NumberT", bound=number)
_CharT = TypeVar("_CharT", bound=character)

_BitT = TypeVar("_BitT", bound=NBitBase, default=Any)  # pyright: ignore[reportDeprecated]
_BitT1 = TypeVar("_BitT1", bound=NBitBase, default=Any)  # pyright: ignore[reportDeprecated]
_BitT2 = TypeVar("_BitT2", bound=NBitBase, default=_BitT1)  # pyright: ignore[reportDeprecated]

_ItemT_co = TypeVar("_ItemT_co", default=Any, covariant=True)
_BoolItemT_co = TypeVar("_BoolItemT_co", bound=py_bool, default=py_bool, covariant=True)
_NumberItemT_co = TypeVar("_NumberItemT_co", bound=complex, default=Any, covariant=True)
_InexactItemT_co = TypeVar("_InexactItemT_co", bound=complex, default=Any, covariant=True)
_FlexItemT_co = TypeVar(
    "_FlexItemT_co",
    bound=bytes | str | tuple[object, ...],
    default=bytes | str | tuple[Any, ...],
    covariant=True,
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
_ExpiredAttribute: TypeAlias = L[
    "DataSource",
    "Inf",
    "Infinity",
    "NINF",
    "NZERO",
    "NaN",
    "PINF",
    "PZERO",
    "add_docstring",
    "add_newdoc",
    "add_newdoc_ufunc",
    "alltrue",
    "asfarray",
    "byte_bounds",
    "cast",
    "cfloat",
    "clongfloat",
    "compare_chararrays",
    "compat",
    "complex_",
    "deprecate",
    "deprecate_with_doc",
    "disp",
    "fastCopyAndTranspose",
    "find_common_type",
    "float_",
    "format_parser",
    "get_array_wrap",
    "geterrobj",
    "infty",
    "issctype",
    "issubclass_",
    "issubsctype",
    "longcomplex",
    "longfloat",
    "lookfor",
    "mat",
    "maximum_sctype",
    "nbytes",
    "obj2sctype",
    "recfromcsv",
    "recfromtxt",
    "round_",
    "safe_eval",
    "sctype2char",
    "sctypes",
    "set_numeric_ops",
    "set_string_function",
    "seterrobj",
    "singlecomplex",
    "sometrue",
    "source",
    "string_",
    "tracemalloc_domain",
    "unicode_",
    "who",
]
_UFuncMethod: TypeAlias = L["__call__", "reduce", "reduceat", "accumulate", "outer", "at"]

_2Tuple: TypeAlias = tuple[_T, _T]
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
_AbstractNumber: TypeAlias = _JustNumber | _AbstractInteger | _AbstractInexact

_int32_min: TypeAlias = int32 | int64
_int16_min: TypeAlias = int16 | _int32_min
_int16_max: TypeAlias = int16 | int8
_int32_max: TypeAlias = int32 | _int16_max
_float32_min: TypeAlias = float32 | float64 | longdouble
_float32_max: TypeAlias = float32 | float16
_float64_max: TypeAlias = float64 | _float32_max
_complex128_min: TypeAlias = complex128 | clongdouble
_integer32_min: TypeAlias = _nt.integer32 | _nt.integer64
_inexact64_min: TypeAlias = _nt.inexact64 | _nt.inexact64l

_ArrayUInt_co: TypeAlias = NDArray[_nt.co_uint64]
_ArrayInt_co: TypeAlias = NDArray[_nt.co_int64]
_ArrayInteger_co: TypeAlias = NDArray[_nt.co_integer]
_ArrayFloat64_co: TypeAlias = NDArray[_nt.co_float64]
_ArrayFloat_co: TypeAlias = NDArray[_nt.co_float]
_ArrayComplex128_co: TypeAlias = NDArray[_nt.co_complex128]
_ArrayComplex_co: TypeAlias = NDArray[_nt.co_complex]
_ArrayTD64_co: TypeAlias = NDArray[_nt.co_timedelta]

_ToIndex: TypeAlias = CanIndex | slice | EllipsisType | _nt.CoInteger_1nd | None
_ToIndices: TypeAlias = _ToIndex | tuple[_ToIndex, ...]

_Axis0D: TypeAlias = L[0, -1] | tuple[()]

_UnsignedIntegerCType: TypeAlias = type[
    ct.c_uint8 | ct.c_uint16 | ct.c_uint32 | ct.c_uint64
    | ct.c_ushort | ct.c_uint | ct.c_ulong | ct.c_ulonglong
    | ct.c_size_t | ct.c_void_p
]  # fmt: skip
_SignedIntegerCType: TypeAlias = type[
    ct.c_int8 | ct.c_int16 | ct.c_int32 | ct.c_int64
    | ct.c_short | ct.c_int | ct.c_long | ct.c_longlong
    | ct.c_ssize_t
]  # fmt: skip
_FloatingCType: TypeAlias = type[ct.c_float | ct.c_double | ct.c_longdouble]
_IntegerCType: TypeAlias = _UnsignedIntegerCType | _SignedIntegerCType
_NumberCType: TypeAlias = _IntegerCType
_GenericCType: TypeAlias = _NumberCType | type[ct.c_bool | ct.c_char | ct.py_object[Any]]

# some commonly used builtin types that are known to result in a
# `dtype[object_]`, when their *type* is passed to the `dtype` constructor
# NOTE: `builtins.object` should not be included here
_BuiltinObjectLike: TypeAlias = Decimal | Fraction

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

_OrderCF: TypeAlias = L["C", "F"] | None
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

_BinOperandComplex128_co: TypeAlias = complex | float64 | _integer32_min
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
    def shape(self, /) -> _ShapeT_co: ...
    def item(self, /) -> _T_co: ...

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

@type_check_only
class _HasDType(Protocol[_T_co]):
    @property
    def dtype(self, /) -> _T_co: ...

_HasDTypeWithItem: TypeAlias = _HasDType[_HasTypeWithItem[_T]]
_HasDTypeWithReal: TypeAlias = _HasDType[_HasTypeWithReal[_T]]
_HasDTypeWithImag: TypeAlias = _HasDType[_HasTypeWithImag[_T]]

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

@type_check_only
class _CanLT(Protocol):
    def __lt__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanLE(Protocol):
    def __le__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanGT(Protocol):
    def __gt__(self, x: Any, /) -> Any: ...

@type_check_only
class _CanGE(Protocol):
    def __ge__(self, x: Any, /) -> Any: ...

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
    def __lt__(self, x: _ArrayLikeT_contra | _NestedSequence[_CanGT], /) -> NDArray[bool_]: ...
    @overload
    def __lt__(self, x: _CanGT, /) -> bool_: ...

    #
    @overload
    def __le__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __le__(self, x: _ArrayLikeT_contra | _NestedSequence[_CanGE], /) -> NDArray[bool_]: ...
    @overload
    def __le__(self, x: _CanGE, /) -> bool_: ...

    #
    @overload
    def __gt__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __gt__(self, x: _ArrayLikeT_contra | _NestedSequence[_CanLT], /) -> NDArray[bool_]: ...
    @overload
    def __gt__(self, x: _CanLT, /) -> bool_: ...

    #
    @overload
    def __ge__(self, x: _ScalarLikeT_contra, /) -> bool_: ...
    @overload
    def __ge__(self, x: _ArrayLikeT_contra | _NestedSequence[_CanLE], /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self, x: _CanLE, /) -> bool_: ...

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
__array_api_version__: Final = "2023.12"
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
    def shape(self) -> tuple[int, ...]: ...
    @property
    def ndim(self) -> int: ...
    @property
    def subdtype(self) -> tuple[dtype, tuple[int, ...]] | None: ...

    #
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeBool,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.BoolDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeInt8,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Int8DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeUInt8,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.UByteDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeInt16,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Int16DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeUInt16,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.UInt16DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeInt32,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Int32DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeUInt32,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.UInt32DType: ...
    @overload
    def __new__(
        cls,
        dtype: type[ct.c_long] | _LongCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.LongDType: ...
    @overload
    def __new__(
        cls,
        dtype: type[ct.c_ulong] | _ULongCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.ULongDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeInt64,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Int64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeUInt64,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.UInt64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeFloat16,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Float16DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeFloat32,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Float32DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeFloat64 | None,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Float64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeLongDouble,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.LongDoubleDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeComplex64,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Complex64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeComplex128,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.Complex128DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeCLongDouble,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.CLongDoubleDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeObject,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.ObjectDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeBytes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.BytesDType: ...
    @overload
    def __new__(  # type: ignore[overload-overlap]
        cls,
        dtype: _nt.ToDTypeStr,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.StrDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeVoid,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.VoidDType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeDateTime64,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.DateTime64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeTimeDelta64,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.TimeDelta64DType: ...
    @overload
    def __new__(
        cls,
        dtype: _nt.ToDTypeString,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> dtypes.StringDType: ...
    @overload
    def __new__(
        cls,
        dtype: _DTypeLike[_ScalarT_co],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
    ) -> Self: ...
    @overload
    def __new__(
        cls,
        dtype: DTypeLike,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: _MetaData = ...,
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
    ) -> Any: ...
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
    def argmax(self, /, axis: CanIndex, out: None = None, *, keepdims: py_bool = False) -> Any: ...
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
    ) -> Any: ...
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
    def argmin(self, /, axis: CanIndex, out: None = None, *, keepdims: py_bool = False) -> Any: ...
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
    def choose(self, /, choices: ArrayLike, out: None = None, mode: _ModeKind = "raise") -> NDArray[Any]: ...
    @overload  # out=ndarray
    def choose(self, /, choices: ArrayLike, out: _ArrayT, mode: _ModeKind = "raise") -> _ArrayT: ...

    # TODO: Annotate kwargs with an unpacked `TypedDict`
    @overload  # out: None (default)
    def clip(
        self,
        /,
        min: ArrayLike,
        max: ArrayLike | None = None,
        out: None = None,
        **kwargs: object,
    ) -> NDArray[Any]: ...
    @overload
    def clip(self, /, min: None, max: ArrayLike, out: None = None, **kwargs: object) -> NDArray[Any]: ...
    @overload
    def clip(self, /, min: None = None, *, max: ArrayLike, out: None = None, **kwargs: object) -> NDArray[Any]: ...
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
    def compress(
        self,
        /,
        condition: _nt.CoInteger_nd,
        axis: CanIndex | None = None,
        out: None = None,
    ) -> NDArray[Any]: ...
    @overload
    def compress(self, /, condition: _nt.CoInteger_nd, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def compress(self, /, condition: _nt.CoInteger_nd, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

    #
    @overload  # out: None (default)
    def cumprod(
        self,
        /,
        axis: CanIndex | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
    ) -> NDArray[Any]: ...
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
        self,
        /,
        axis: CanIndex | None = None,
        dtype: DTypeLike | None = None,
        out: None = None,
    ) -> NDArray[Any]: ...
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
    def base(self) -> NDArray[Any] | None: ...

    #
    @property
    def ndim(self) -> int: ...
    @property
    def size(self) -> int: ...

    #
    @property
    def shape(self) -> _ShapeT_co: ...
    @shape.setter
    def shape(self: ndarray[_ShapeT, Any], shape: _ShapeT, /) -> None: ...

    #
    @property
    def strides(self) -> tuple[int, ...]: ...
    @strides.setter
    def strides(self, value: tuple[int, ...], /) -> None: ...

    #
    @property
    @override
    def real(self: _HasDTypeWithReal[_ScalarT], /) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @real.setter
    @override
    def real(self, value: ArrayLike, /) -> None: ...

    #
    @property
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
    def __array_finalize__(self, obj: NDArray[Any] | Any, /) -> None: ...
    def __array_ufunc__(self, ufunc: ufunc, method: _UFuncMethod, /, *inputs: object, **kwargs: object) -> Any: ...
    def __array_function__(
        self,
        /,
        func: Callable[..., Any],
        types: Iterable[type],
        args: Iterable[Any],
        kwargs: Mapping[str, Any],
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
        self,
        key: _ArrayInteger_co | tuple[_ArrayInteger_co, ...],
        /,
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def __getitem__(self, key: CanIndex | tuple[CanIndex, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndices, /) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def __getitem__(self: NDArray[void], key: str, /) -> ndarray[_ShapeT_co, dtype]: ...
    @overload
    def __getitem__(self: NDArray[void], key: list[str], /) -> _nt.Array[void, _ShapeT_co]: ...

    #
    @overload  # flexible | object_ | bool
    def __setitem__(
        self: ndarray[Any, dtype[bool_ | object_ | flexible] | dtypes.StringDType],
        key: _ToIndices,
        value: object,
        /,
    ) -> None: ...
    @overload  # integer
    def __setitem__(
        self: NDArray[integer],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToInt] | _nt.CoInteger_nd,
        /,
    ) -> None: ...
    @overload  # floating
    def __setitem__(
        self: NDArray[floating],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToFloat | None] | _nt.CoFloating_nd,
        /,
    ) -> None: ...
    @overload  # complexfloating
    def __setitem__(
        self: NDArray[complexfloating],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToComplex | None] | _nt.CoComplex_nd,
        /,
    ) -> None: ...
    @overload  # timedelta64
    def __setitem__(
        self: NDArray[timedelta64],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToTD64],
        /,
    ) -> None: ...
    @overload  # datetime64
    def __setitem__(
        self: NDArray[datetime64],
        key: _ToIndices,
        value: _nt.SequenceND[_ConvertibleToDT64],
        /,
    ) -> None: ...
    @overload  # void
    def __setitem__(self: NDArray[void], key: str | list[str], value: object, /) -> None: ...
    @overload  # catch-all
    def __setitem__(self, key: _ToIndices, value: ArrayLike, /) -> None: ...

    #
    def __complex__(self: NDArray[_nt.co_number | object_], /) -> complex: ...
    def __index__(self: NDArray[integer], /) -> int: ...

    #
    def __len__(self) -> int: ...
    def __contains__(self, value: object, /) -> py_bool: ...

    #
    @overload  # == 1-d & object_
    def __iter__(self: ndarray[tuple[int], dtype[object_]], /) -> Iterator[Any]: ...
    @overload  # == 1-d
    def __iter__(self: ndarray[tuple[int], dtype[_ScalarT]], /) -> Iterator[_ScalarT]: ...
    @overload  # >= 2-d
    def __iter__(self: ndarray[_nt.AtLeast2D, dtype[_ScalarT]], /) -> Iterator[NDArray[_ScalarT]]: ...
    @overload  # ?-d
    def __iter__(self, /) -> Iterator[Any]: ...

    #
    @overload
    def __eq__(self, other: _ScalarLike_co | ndarray[_ShapeT_co, dtype], /) -> _nt.Array[bool_, _ShapeT_co]: ...
    @overload
    def __eq__(self, other: object, /) -> NDArray[bool_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __ne__(self, other: _ScalarLike_co | ndarray[_ShapeT_co, dtype], /) -> _nt.Array[bool_, _ShapeT_co]: ...
    @overload
    def __ne__(self, other: object, /) -> NDArray[bool_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __lt__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> NDArray[bool_]: ...
    @overload
    def __lt__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> NDArray[bool_]: ...
    @overload
    def __lt__(self: NDArray[datetime64], other: _ArrayLikeDT64_co, /) -> NDArray[bool_]: ...
    @overload
    def __lt__(self: NDArray[object_], other: object, /) -> NDArray[bool_]: ...
    @overload
    def __lt__(self, other: _ArrayLikeObject_co, /) -> NDArray[bool_]: ...

    #
    @overload
    def __le__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> NDArray[bool_]: ...
    @overload
    def __le__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> NDArray[bool_]: ...
    @overload
    def __le__(self: NDArray[datetime64], other: _ArrayLikeDT64_co, /) -> NDArray[bool_]: ...
    @overload
    def __le__(self: NDArray[object_], other: object, /) -> NDArray[bool_]: ...
    @overload
    def __le__(self, other: _ArrayLikeObject_co, /) -> NDArray[bool_]: ...

    #
    @overload
    def __gt__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> NDArray[bool_]: ...
    @overload
    def __gt__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> NDArray[bool_]: ...
    @overload
    def __gt__(self: NDArray[datetime64], other: _ArrayLikeDT64_co, /) -> NDArray[bool_]: ...
    @overload
    def __gt__(self: NDArray[object_], other: object, /) -> NDArray[bool_]: ...
    @overload
    def __gt__(self, other: _ArrayLikeObject_co, /) -> NDArray[bool_]: ...

    #
    @overload
    def __ge__(self: _ArrayComplex_co, other: _nt.CoComplex_nd, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: NDArray[datetime64], other: _ArrayLikeDT64_co, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: NDArray[object_], other: object, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self, other: _ArrayLikeObject_co, /) -> NDArray[bool_]: ...

    # Unary ops

    def __abs__(self: _HasDType[_HasType[SupportsAbs[_ScalarT]]], /) -> _nt.Array[_ScalarT, _ShapeT_co]: ...

    #
    def __invert__(self: _IntegralArrayT, /) -> _IntegralArrayT: ...  # noqa: PYI019
    def __neg__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019
    def __pos__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019

    # Binary ops

    #
    @overload
    def __add__(self: NDArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> NDArray[_ScalarT]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: NDArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> NDArray[_ScalarT]: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> NDArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithInt[_ScalarT], x: _nt.SequenceND[_nt.JustInt], /) -> NDArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithFloat[_ScalarT], x: _nt.SequenceND[_nt.JustFloat], /) -> NDArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithComplex[_ScalarT], x: _nt.SequenceND[_nt.JustComplex], /) -> NDArray[_ScalarT]: ...
    @overload
    def __add__(self: NDArray[datetime64], x: _nt.CoTimeDelta_nd, /) -> NDArray[datetime64]: ...
    @overload
    def __add__(self: NDArray[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> NDArray[datetime64]: ...
    @overload
    def __add__(self: NDArray[object_], x: object, /) -> NDArray[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __add__(self: NDArray[str_], x: _nt.ToString_nd[_T], /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __add__(self: _nt.StringArrayND[_T], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /) -> _nt.StringArrayND[_T]: ...

    # keep in sync with __add__
    @overload
    def __radd__(self: NDArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> NDArray[_ScalarT]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: NDArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /) -> NDArray[_ScalarT]: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> NDArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithInt[_ScalarT], x: _nt.SequenceND[_nt.JustInt], /) -> NDArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithFloat[_ScalarT], x: _nt.SequenceND[_nt.JustFloat], /) -> NDArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithComplex[_ScalarT], x: _nt.SequenceND[_nt.JustComplex], /) -> NDArray[_ScalarT]: ...
    @overload
    def __radd__(self: NDArray[datetime64], x: _nt.CoTimeDelta_nd, /) -> NDArray[datetime64]: ...
    @overload
    def __radd__(self: NDArray[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> NDArray[datetime64]: ...
    @overload
    def __radd__(self: NDArray[object_], x: object, /) -> NDArray[object_]: ...  # type: ignore[overload-cannot-match]
    @overload
    def __radd__(self: NDArray[str_], x: _nt.ToString_nd[_T], /) -> _nt.StringArrayND[_T]: ...
    @overload
    def __radd__(self: _nt.StringArrayND[_T], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /) -> _nt.StringArrayND[_T]: ...

    #
    @overload
    def __sub__(self: NDArray[_NumberT], rhs: int | bool_, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __sub__(self: NDArray[_NumberT], rhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __sub__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __sub__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> Never: ...
    @overload
    def __sub__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __sub__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __sub__(self: NDArray[complex128], rhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __sub__(self: _ArrayComplex128_co, rhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __sub__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __sub__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __sub__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: NDArray[integer], rhs: _NestedSequence[_nt.JustInt], /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __sub__(self: _ArrayFloat_co, rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __sub__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __sub__(self: _ArrayComplex_co, rhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __sub__(self: NDArray[_nt.co_number], rhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __sub__(self: NDArray[timedelta64], rhs: _ArrayLikeTD64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __sub__(self: _ArrayTD64_co, rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __sub__(self: NDArray[datetime64], rhs: _ArrayLikeDT64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __sub__(self: NDArray[datetime64], rhs: _ArrayLikeTD64_co, /) -> NDArray[datetime64]: ...
    @overload
    def __sub__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __sub__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __sub__, minus the (datetime64, timedelta64) case
    @overload
    def __rsub__(self: NDArray[_NumberT], lhs: int | bool_, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __rsub__(self: NDArray[_NumberT], lhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __rsub__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rsub__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> Never: ...
    @overload
    def __rsub__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rsub__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rsub__(self: NDArray[complex128], lhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rsub__(self: _ArrayComplex128_co, lhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rsub__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rsub__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rsub__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: NDArray[integer], lhs: _NestedSequence[_nt.JustInt], /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rsub__(self: _ArrayFloat_co, lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rsub__(self: NDArray[complexfloating], lhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rsub__(self: _ArrayComplex_co, lhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rsub__(self: NDArray[_nt.co_number], lhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __rsub__(self: NDArray[timedelta64], lhs: _ArrayLikeTD64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __rsub__(self: _ArrayTD64_co, lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rsub__(self: NDArray[datetime64], lhs: _ArrayLikeDT64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __rsub__(self: _ArrayTD64_co, lhs: _ArrayLike[datetime64], /) -> NDArray[datetime64]: ...
    @overload
    def __rsub__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rsub__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __isub__(self: NDArray[integer], rhs: _nt.CoInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: NDArray[datetime64 | timedelta64],
        rhs: _ArrayLikeTD64_co,
        /,
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mul__(self: NDArray[_NumberT], rhs: int | bool_, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __mul__(self: NDArray[_NumberT], rhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __mul__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __mul__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __mul__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __mul__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __mul__(self: NDArray[complex128], rhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __mul__(self: _ArrayComplex128_co, rhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __mul__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mul__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mul__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __mul__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __mul__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __mul__(self: _ArrayFloat_co, rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __mul__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __mul__(self: _ArrayComplex_co, rhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __mul__(self: NDArray[_nt.co_number], rhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __mul__(self: NDArray[timedelta64], rhs: _nt.CoFloating_nd, /) -> NDArray[timedelta64]: ...
    @overload
    def __mul__(self: _ArrayFloat_co, rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __mul__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __mul__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __mul__
    @overload
    def __rmul__(self: NDArray[_NumberT], lhs: int | bool_, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __rmul__(self: NDArray[_NumberT], lhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __rmul__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rmul__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __rmul__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmul__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmul__(self: NDArray[complex128], lhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rmul__(self: _ArrayComplex128_co, lhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rmul__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmul__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmul__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmul__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmul__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmul__(self: _ArrayFloat_co, lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmul__(self: NDArray[complexfloating], lhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmul__(self: _ArrayComplex_co, lhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmul__(self: NDArray[_nt.co_number], lhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __rmul__(self: NDArray[timedelta64], lhs: _nt.CoFloating_nd, /) -> NDArray[timedelta64]: ...
    @overload
    def __rmul__(self: _ArrayFloat_co, lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rmul__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmul__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imul__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[integer], rhs: _nt.CoInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: NDArray[floating | timedelta64],
        rhs: _nt.CoFloating_nd,
        /,
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    # TODO(jorenham): Support the "1d @ 1d -> scalar" case
    # https://github.com/numpy/numtype/issues/197
    @overload
    def __matmul__(self: NDArray[_NumberT], rhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __matmul__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __matmul__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __matmul__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __matmul__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __matmul__(self: NDArray[complex128], rhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __matmul__(self: _ArrayComplex128_co, rhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __matmul__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __matmul__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __matmul__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __matmul__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __matmul__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __matmul__(self: _ArrayFloat_co, rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __matmul__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __matmul__(self: _ArrayComplex_co, rhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __matmul__(self: NDArray[_nt.co_number], rhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __matmul__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __matmul__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __matmul__
    @overload
    def __rmatmul__(self: NDArray[_NumberT], lhs: _nt.ToBool_nd, /) -> NDArray[_NumberT]: ...
    @overload
    def __rmatmul__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rmatmul__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __rmatmul__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmatmul__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmatmul__(self: NDArray[complex128], lhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rmatmul__(self: _ArrayComplex128_co, lhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rmatmul__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmatmul__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmatmul__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmatmul__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmatmul__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmatmul__(self: _ArrayFloat_co, lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmatmul__(self: NDArray[complexfloating], lhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmatmul__(self: _ArrayComplex_co, lhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmatmul__(self: NDArray[_nt.co_number], lhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __rmatmul__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmatmul__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imatmul__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[integer], rhs: _nt.CoInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __truediv__(self: _ArrayInteger_co, rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: _ArrayFloat64_co, rhs: _nt.CoInteger_nd | _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: NDArray[complex128], rhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __truediv__(self: _ArrayComplex128_co, rhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __truediv__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __truediv__(self: _ArrayFloat_co, rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __truediv__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __truediv__(self: _ArrayComplex_co, rhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __truediv__(self: NDArray[inexact], rhs: _nt.CoComplex_nd, /) -> NDArray[inexact]: ...
    @overload
    def __truediv__(self: NDArray[number], rhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _nt.ToBool_nd, /) -> Never: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _nt.CoFloating_nd, /) -> NDArray[timedelta64]: ...
    @overload
    def __truediv__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __truediv__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rtruediv__(self: _ArrayInteger_co, lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rtruediv__(self: _ArrayFloat64_co, lhs: _nt.CoInteger_nd | _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rtruediv__(self: NDArray[complex128], lhs: _nt.CoComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rtruediv__(self: _ArrayComplex128_co, lhs: _nt.ToComplex128_nd, /) -> NDArray[complex128]: ...
    @overload
    def __rtruediv__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rtruediv__(self: _ArrayFloat_co, lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rtruediv__(self: NDArray[complexfloating], lhs: _nt.CoComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: _ArrayComplex_co, lhs: _nt.ToComplex_nd, /) -> NDArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: NDArray[inexact], lhs: _nt.CoComplex_nd, /) -> NDArray[inexact]: ...
    @overload
    def __rtruediv__(self: NDArray[_nt.co_number], lhs: _nt.CoComplex_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __rtruediv__(self: NDArray[timedelta64], lhs: _ArrayLike[timedelta64], /) -> NDArray[float64]: ...
    @overload
    def __rtruediv__(self: NDArray[integer | floating], lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rtruediv__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rtruediv__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __itruediv__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[timedelta64], rhs: _nt.ToInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    # the pyright error appears to be a false positive
    @overload
    def __floordiv__(self: NDArray[_RealNumberT], rhs: int | bool_, /) -> _nt.Array[_RealNumberT, _ShapeT_co]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __floordiv__(self: NDArray[_RealNumberT], rhs: _nt.ToBool_nd, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...
    @overload
    def __floordiv__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __floordiv__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __floordiv__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __floordiv__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __floordiv__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __floordiv__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __floordiv__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __floordiv__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __floordiv__(self: NDArray[floating | integer], rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __floordiv__(self: _nt.CoFloating_nd, rhs: _nt.CoFloating_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[int64]: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _nt.ToBool_nd, /) -> Never: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _nt.CoFloating_nd, /) -> NDArray[timedelta64]: ...
    @overload
    def __floordiv__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __floordiv__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rfloordiv__(self: NDArray[_RealNumberT], lhs: int | bool_, /) -> _nt.Array[_RealNumberT, _ShapeT_co]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rfloordiv__(self: NDArray[_RealNumberT], lhs: _nt.ToBool_nd, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...
    @overload
    def __rfloordiv__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __rfloordiv__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rfloordiv__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rfloordiv__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rfloordiv__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rfloordiv__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rfloordiv__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating | integer], lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rfloordiv__(self: _nt.CoFloating_nd, lhs: _nt.CoFloating_nd, /) -> NDArray[Incomplete]: ...
    @overload
    def __rfloordiv__(self: NDArray[timedelta64], lhs: _ArrayLike[timedelta64], /) -> NDArray[int64]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating | integer], lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rfloordiv__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rfloordiv__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ifloordiv__(
        self: NDArray[integer | timedelta64],
        rhs: _nt.CoInteger_nd,
        /,
    ) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mod__(self: NDArray[_RealNumberT], rhs: int | bool_, /) -> _nt.Array[_RealNumberT, _ShapeT_co]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __mod__(self: NDArray[_RealNumberT], rhs: _nt.ToBool_nd, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...
    @overload
    def __mod__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __mod__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __mod__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __mod__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mod__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mod__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __mod__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __mod__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __mod__(self: NDArray[floating | integer], rhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __mod__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __mod__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __mod__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __mod__
    @overload
    def __rmod__(self: NDArray[_RealNumberT], lhs: int | bool_, /) -> _nt.Array[_RealNumberT, _ShapeT_co]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rmod__(self: NDArray[_RealNumberT], lhs: _nt.ToBool_nd, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmod__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...
    @overload
    def __rmod__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __rmod__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmod__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> NDArray[float64]: ...
    @overload
    def __rmod__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmod__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmod__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmod__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmod__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmod__(self: NDArray[floating | integer], lhs: _nt.ToFloating_nd, /) -> NDArray[floating]: ...
    @overload
    def __rmod__(self: NDArray[timedelta64], lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rmod__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmod__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imod__(self: NDArray[integer], rhs: _nt.CoInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __divmod__(  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
        self: NDArray[_RealNumberT],
        rhs: int | bool_,
        /,
    ) -> _2Tuple[_nt.Array[_RealNumberT, _ShapeT_co]]: ...
    @overload
    def __divmod__(self: NDArray[_RealNumberT], rhs: _nt.ToBool_nd, /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __divmod__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> _2Tuple[NDArray[_RealNumberT]]: ...
    @overload
    def __divmod__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> _2Tuple[NDArray[int8]]: ...
    @overload
    def __divmod__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __divmod__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __divmod__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __divmod__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __divmod__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __divmod__(self: _ArrayInt_co, rhs: _nt.ToSInteger_nd, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __divmod__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __divmod__(self: NDArray[floating | integer], rhs: _nt.ToFloating_nd, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __divmod__(
        self: NDArray[timedelta64],
        rhs: _ArrayLike[timedelta64],
        /,
    ) -> tuple[NDArray[int64], NDArray[timedelta64]]: ...

    # keep in sync with __divmod__
    @overload
    def __rdivmod__(  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
        self: NDArray[_RealNumberT],
        lhs: int | bool_,
        /,
    ) -> _2Tuple[_nt.Array[_RealNumberT, _ShapeT_co]]: ...
    @overload
    def __rdivmod__(self: NDArray[_RealNumberT], lhs: _nt.ToBool_nd, /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> _2Tuple[NDArray[_RealNumberT]]: ...
    @overload
    def __rdivmod__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> _2Tuple[NDArray[int8]]: ...
    @overload
    def __rdivmod__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __rdivmod__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __rdivmod__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __rdivmod__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __rdivmod__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __rdivmod__(self: _ArrayInt_co, lhs: _nt.ToSInteger_nd, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __rdivmod__(self: NDArray[floating], lhs: _nt.CoFloating_nd, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __rdivmod__(self: NDArray[floating | integer], lhs: _nt.ToFloating_nd, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __rdivmod__(
        self: NDArray[timedelta64],
        lhs: _ArrayLike[timedelta64],
        /,
    ) -> tuple[NDArray[int64], NDArray[timedelta64]]: ...

    #
    @overload
    def __pow__(self: NDArray[_NumberT], rhs: int | bool_, mod: None = None, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __pow__(self: NDArray[_NumberT], rhs: _nt.ToBool_nd, mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __pow__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __pow__(self: NDArray[bool_], rhs: _nt.ToBool_nd, mod: None = None, /) -> NDArray[int8]: ...
    @overload
    def __pow__(self: NDArray[float64], rhs: _nt.CoFloat64_nd, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __pow__(self: _ArrayFloat64_co, rhs: _nt.ToFloat64_nd, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __pow__(self: NDArray[complex128], rhs: _nt.CoComplex128_nd, mod: None = None, /) -> NDArray[complex128]: ...
    @overload
    def __pow__(self: _ArrayComplex128_co, rhs: _nt.ToComplex128_nd, mod: None = None, /) -> NDArray[complex128]: ...
    @overload
    def __pow__(
        self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, mod: None = None, /
    ) -> NDArray[unsignedinteger]: ...
    @overload
    def __pow__(self: _ArrayUInt_co, rhs: _nt.ToUInteger_nd, mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __pow__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __pow__(self: _ArrayInteger_co, rhs: _nt.ToSInteger_nd, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __pow__(self: NDArray[floating], rhs: _nt.CoFloating_nd, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __pow__(self: _ArrayFloat_co, rhs: _nt.ToFloating_nd, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __pow__(
        self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, mod: None = None, /
    ) -> NDArray[complexfloating]: ...
    @overload
    def __pow__(self: _ArrayComplex_co, rhs: _nt.ToComplex_nd, mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __pow__(self: NDArray[_nt.co_number], rhs: _nt.CoComplex_nd, mod: None = None, /) -> NDArray[Incomplete]: ...
    @overload
    def __pow__(self: NDArray[object_], rhs: object, mod: None = None, /) -> NDArray[object_]: ...
    @overload
    def __pow__(self, rhs: _ArrayLikeObject_co, mod: None = None, /) -> NDArray[object_]: ...

    #
    @overload
    def __rpow__(self: NDArray[_NumberT], lhs: int | bool_, mod: None = None, /) -> _nt.Array[_NumberT, _ShapeT_co]: ...
    @overload
    def __rpow__(self: NDArray[_NumberT], lhs: _nt.ToBool_nd, mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __rpow__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __rpow__(self: NDArray[bool_], lhs: _nt.ToBool_nd, mod: None = None, /) -> NDArray[int8]: ...
    @overload
    def __rpow__(self: NDArray[float64], lhs: _nt.CoFloat64_nd, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __rpow__(self: _ArrayFloat64_co, lhs: _nt.ToFloat64_nd, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __rpow__(self: NDArray[complex128], lhs: _nt.CoComplex128_nd, mod: None = None, /) -> NDArray[complex128]: ...
    @overload
    def __rpow__(self: _ArrayComplex128_co, lhs: _nt.ToComplex128_nd, mod: None = None, /) -> NDArray[complex128]: ...
    @overload
    def __rpow__(
        self: NDArray[unsignedinteger],
        lhs: _nt.CoUInt64_nd,
        mod: None = None,
        /,
    ) -> NDArray[unsignedinteger]: ...
    @overload
    def __rpow__(self: _ArrayUInt_co, lhs: _nt.ToUInteger_nd, mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rpow__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __rpow__(self: _ArrayInteger_co, lhs: _nt.ToSInteger_nd, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __rpow__(self: NDArray[floating], lhs: _nt.CoFloating_nd, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __rpow__(self: _ArrayFloat_co, lhs: _nt.ToFloating_nd, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __rpow__(
        self: NDArray[complexfloating],
        lhs: _nt.CoComplex_nd,
        mod: None = None,
        /,
    ) -> NDArray[complexfloating]: ...
    @overload
    def __rpow__(self: _ArrayComplex_co, lhs: _nt.ToComplex_nd, mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __rpow__(self: NDArray[_nt.co_number], lhs: _nt.CoComplex_nd, mod: None = None, /) -> NDArray[Incomplete]: ...
    @overload
    def __rpow__(self: NDArray[object_], lhs: object, mod: None = None, /) -> NDArray[object_]: ...
    @overload
    def __rpow__(self, lhs: _ArrayLikeObject_co, mod: None = None, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ipow__(self: NDArray[integer], rhs: _nt.CoInteger_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[floating], rhs: _nt.CoFloating_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[complexfloating], rhs: _nt.CoComplex_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __lshift__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __lshift__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __lshift__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __lshift__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __lshift__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __lshift__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rlshift__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __rlshift__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rlshift__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rlshift__(self: NDArray[integer], lhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __rlshift__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rlshift__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ilshift__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ilshift__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ilshift__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __rshift__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __rshift__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rshift__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rshift__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __rshift__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rshift__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rrshift__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[int8]: ...
    @overload
    def __rrshift__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rrshift__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rrshift__(self: NDArray[integer], lhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __rrshift__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rrshift__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __irshift__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __irshift__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __irshift__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __and__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __and__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __and__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __and__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __and__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __and__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rand__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __rand__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rand__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rand__(self: NDArray[integer], lhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __rand__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rand__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __iand__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __xor__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __xor__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __xor__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __xor__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __xor__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __xor__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rxor__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __rxor__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rxor__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __rxor__(self: NDArray[integer], lhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __rxor__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rxor__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ixor__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __or__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __or__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __or__(self: NDArray[signedinteger], rhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __or__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __or__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __or__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __ror__(self: NDArray[bool_], lhs: _nt.ToBool_nd, /) -> NDArray[bool_]: ...
    @overload
    def __ror__(self: NDArray[unsignedinteger], lhs: _nt.CoUInt64_nd, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __ror__(self: NDArray[signedinteger], lhs: _nt.CoInt64_nd, /) -> NDArray[signedinteger]: ...
    @overload
    def __ror__(self: NDArray[integer], lhs: _nt.CoInt64_nd, /) -> NDArray[integer]: ...
    @overload
    def __ror__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __ror__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ior__(self: NDArray[bool_], rhs: _nt.ToBool_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(self: NDArray[unsignedinteger], rhs: _nt.CoUInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(self: NDArray[integer], rhs: _nt.CoInt64_nd, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    def __dlpack__(
        self: NDArray[number],
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
    @overload
    def tolist(self: _HasShapeAndItem[tuple[()], _T], /) -> _T: ...
    @overload
    def tolist(self: _HasShapeAndItem[tuple[int], _T], /) -> list[_T]: ...
    @overload
    def tolist(self: _HasShapeAndItem[tuple[int, int], _T], /) -> list[list[_T]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[tuple[int, int, int], _T], /) -> list[list[list[_T]]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[tuple[int, int, int, int], _T], /) -> list[list[list[list[_T]]]]: ...
    @overload
    def tolist(self: _HasShapeAndItem[Any, _T], /) -> Any: ...

    #
    @overload
    def resize(self, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(self: ndarray[_ShapeT, Any], new_shape: _ShapeT, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(self: ndarray[tuple[int], Any], n0: CanIndex, /, *, refcheck: py_bool = True) -> None: ...
    @overload
    def resize(
        self: _nt.Array2D[Any],
        n0: CanIndex,
        n1: CanIndex,
        /,
        *,
        refcheck: py_bool = True,
    ) -> None: ...
    @overload
    def resize(
        self: ndarray[tuple[int, int, int], Any],
        n0: CanIndex,
        n1: CanIndex,
        n2: CanIndex,
        /,
        *,
        refcheck: py_bool = True,
    ) -> None: ...

    #
    def swapaxes(
        self: ndarray[_AnyShapeT, _DTypeT],
        /,
        axis1: CanIndex,
        axis2: CanIndex,
    ) -> ndarray[_AnyShapeT, _DTypeT]: ...
    def squeeze(
        self,
        /,
        axis: CanIndex | tuple[CanIndex, ...] | None = None,
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    def byteswap(self, /, inplace: py_bool = False) -> Self: ...

    #
    @overload
    def transpose(self, axes: _ShapeLike | None, /) -> Self: ...
    @overload
    def transpose(self, /, *axes: CanIndex) -> Self: ...

    # NOTE: always raises when called on `generic`.
    @overload
    def diagonal(
        self: ndarray[tuple[int, int], _DTypeT],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
    ) -> ndarray[tuple[int], _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[tuple[int, int, int], _DTypeT],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
    ) -> ndarray[tuple[int, int], _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[tuple[int, int, int, int], _DTypeT],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
    ) -> ndarray[tuple[int, int, int], _DTypeT]: ...
    @overload
    def diagonal(
        self: ndarray[tuple[int, ...], _DTypeT],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
    ) -> ndarray[tuple[int, ...], _DTypeT]: ...

    #
    @overload
    def all(
        self,
        /,
        axis: None = None,
        out: None = None,
        keepdims: L[False, 0] = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_ | NDArray[bool_]: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None,
        out: _ArrayT,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None = None,
        *,
        out: _ArrayT,
        keepdims: CanIndex = False,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    @overload
    def any(
        self,
        axis: None = None,
        out: None = None,
        keepdims: L[False, 0] = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> bool_ | NDArray[bool_]: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None,
        out: _ArrayT,
        keepdims: CanIndex = False,
        *,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None = None,
        *,
        out: _ArrayT,
        keepdims: CanIndex = False,
        where: _nt.ToBool_nd = True,
    ) -> _ArrayT: ...

    #
    def argpartition(
        self,
        kth: _nt.CoInteger_nd,
        axis: CanIndex | None = ...,
        kind: _PartitionKind = ...,
        order: str | Sequence[str] | None = ...,
    ) -> NDArray[intp]: ...

    # 1D + 1D returns a scalar; # all other with at least 1 non-0D array return an ndarray.
    @overload
    def dot(self, b: _ScalarLike_co, out: None = ...) -> NDArray[Any]: ...
    @overload
    def dot(self, b: ArrayLike, out: None = ...) -> Any: ...
    @overload
    def dot(self, b: ArrayLike, out: _ArrayT) -> _ArrayT: ...

    # `nonzero()` is deprecated for 0d arrays/generics
    def nonzero(self) -> tuple[NDArray[intp], ...]: ...

    #
    @overload
    def searchsorted(
        self,
        /,
        v: _ScalarLike_co,
        side: _SortSide = "left",
        sorter: _nt.CoInteger_nd | None = None,
    ) -> intp: ...
    @overload
    def searchsorted(
        self,
        /,
        v: ndarray[_ShapeT, Any],
        side: _SortSide = "left",
        sorter: _nt.CoInteger_nd | None = None,
    ) -> ndarray[_ShapeT, dtype[intp]]: ...
    @overload
    def searchsorted(
        self,
        /,
        v: _NestedSequence[_ScalarLike_co],
        side: _SortSide = "left",
        sorter: _nt.CoInteger_nd | None = None,
    ) -> NDArray[intp]: ...
    @overload
    def searchsorted(
        self,
        /,
        v: ArrayLike,
        side: _SortSide = "left",
        sorter: _nt.CoInteger_nd | None = None,
    ) -> intp | NDArray[intp]: ...

    #
    @overload
    def sort(
        self,
        /,
        axis: CanIndex = -1,
        kind: _SortKind | None = None,
        order: None = None,
        *,
        stable: bool | None = None,
    ) -> None: ...
    @overload
    def sort(
        self: ndarray[Any, dtype[void]],
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
        self,
        /,
        axis: CanIndex = -1,
        kind: _SortKind | None = None,
        order: None = None,
        *,
        stable: bool | None = None,
    ) -> ndarray[_ShapeT_co, dtype[intp]]: ...
    @overload
    def argsort(
        self,
        /,
        axis: None,
        kind: _SortKind | None = None,
        order: None = None,
        *,
        stable: bool | None = None,
    ) -> _nt.Array1D[intp]: ...
    @overload
    def argsort(
        self: ndarray[_ShapeT, dtype[void]],
        /,
        axis: CanIndex = -1,
        kind: _SortKind | None = None,
        order: str | Sequence[str] | None = None,
        *,
        stable: bool | None = None,
    ) -> ndarray[_ShapeT_co, dtype[intp]]: ...
    @overload
    def argsort(
        self: ndarray[Any, dtype[void]],
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
        self,
        /,
        kth: _nt.CoInteger_nd,
        axis: CanIndex = -1,
        kind: _PartitionKind = "introselect",
        order: None = None,
    ) -> None: ...
    @overload
    def partition(
        self: ndarray[Any, dtype[void]],
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
        self,
        /,
        offset: CanIndex,
        axis1: CanIndex,
        axis2: CanIndex,
        dtype: DTypeLike | None,
        out: _ArrayT,
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
        self: NDArray[_ScalarT],
        /,
        indices: _nt.CoInteger_0d,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> _ScalarT: ...
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_nd,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_nd,
        axis: CanIndex | None,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_nd,
        axis: CanIndex | None = None,
        *,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...

    #
    @overload
    def repeat(self, /, repeats: _nt.CoInteger_nd, axis: None = None) -> ndarray[tuple[int], _DTypeT_co]: ...
    @overload
    def repeat(
        self: ndarray[_AnyShapeT, _DTypeT],
        /,
        repeats: _nt.CoInteger_nd,
        axis: CanIndex,
    ) -> ndarray[_AnyShapeT, _DTypeT]: ...

    #
    def flatten(self, /, order: _OrderKACF = "C") -> ndarray[tuple[int], _DTypeT_co]: ...
    def ravel(self, /, order: _OrderKACF = "C") -> ndarray[tuple[int], _DTypeT_co]: ...

    #
    @overload  # (None)
    def reshape(self, shape: None, /, *, order: _OrderACF = "C", copy: py_bool | None = None) -> Self: ...
    @overload  # (empty_sequence)
    def reshape(  # type: ignore[overload-overlap]  # mypy false positive
        self,
        shape: Sequence[Never],
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[()], _DTypeT_co]: ...
    @overload  # (() | (int) | (int, int) | ....)  # up to 8-d
    def reshape(
        self,
        shape: _AnyShapeT,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[_AnyShapeT, _DTypeT_co]: ...
    @overload  # (index)
    def reshape(
        self,
        size1: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[int], _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[int, int], _DTypeT_co]: ...
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
    ) -> ndarray[tuple[int, int, int], _DTypeT_co]: ...
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
    ) -> ndarray[tuple[int, int, int, int], _DTypeT_co]: ...
    @overload  # (int, *(index, ...))
    def reshape(
        self,
        size0: CanIndex,
        /,
        *shape: CanIndex,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload  # (sequence[index])
    def reshape(
        self,
        shape: Sequence[CanIndex],
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...

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
    ) -> ndarray[_ShapeT_co, dtype]: ...

    # the special casings work around the lack of higher-kinded typing (HKT) support in Python
    @overload  # ()
    def view(self, /) -> Self: ...
    @overload  # (dtype: T)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT]) -> ndarray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T])
    def view(self, /, dtype: _DTypeLike[_ScalarT]) -> _nt.Array[_ScalarT, _ShapeT_co]: ...
    @overload  # (type: matrix)
    def view(self, /, *, type: type[matrix[Any, Any]]) -> matrix[tuple[int, int], _DTypeT_co]: ...
    @overload  # (_: matrix)
    def view(self, /, dtype: type[matrix[Any, Any]]) -> matrix[tuple[int, int], _DTypeT_co]: ...
    @overload  # (dtype: T, type: matrix)
    def view(
        self,
        /,
        dtype: _DTypeT | _HasDType[_DTypeT],
        type: type[matrix[Any, Any]],
    ) -> matrix[tuple[int, int], _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: matrix)
    def view(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        type: type[matrix[Any, Any]],
    ) -> matrix[tuple[int, int], dtype[_ScalarT]]: ...
    @overload  # (type: recarray)
    def view(
        self,
        /,
        *,
        type: type[recarray[Any, Any]],
    ) -> recarray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: recarray)
    def view(
        self,
        /,
        dtype: type[recarray[Any, Any]],
    ) -> recarray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (dtype: T, type: recarray)
    def view(
        self,
        /,
        dtype: _DTypeT | _HasDType[_DTypeT],
        type: type[recarray[Any, Any]],
    ) -> recarray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: recarray)
    def view(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        type: type[recarray[Any, Any]],
    ) -> recarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload  # (type: char.chararray)
    def view(
        self: ndarray[_ShapeT, dtype[_CharT]],
        /,
        *,
        type: type[char.chararray[Any, Any]],
    ) -> char.chararray[_ShapeT, dtype[_CharT]]: ...
    @overload  # (_: char.chararray)
    def view(
        self: ndarray[_ShapeT, dtype[_CharT]],
        /,
        dtype: type[char.chararray[Any, Any]],
    ) -> char.chararray[_ShapeT, dtype[_CharT]]: ...
    @overload  # (dtype: dtype[T], type: char.chararray)
    def view(
        self,
        /,
        dtype: _DTypeLike[_CharT],
        type: type[char.chararray[Any, Any]],
    ) -> char.chararray[_ShapeT_co, dtype[_CharT]]: ...
    @overload  # (type: MaskedArray)
    def view(
        self,
        /,
        *,
        type: type[ma.MaskedArray[Any, Any]],
    ) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: MaskedArray)
    def view(
        self,
        /,
        dtype: type[ma.MaskedArray[Any, Any]],
    ) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (dtype: T, type: MaskedArray)
    def view(
        self,
        /,
        dtype: _DTypeT | _HasDType[_DTypeT],
        type: type[ma.MaskedArray[Any, Any]],
    ) -> ma.MaskedArray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: MaskedArray)
    def view(
        self,
        /,
        dtype: _DTypeLike[_ScalarT],
        type: type[ma.MaskedArray[Any, Any]],
    ) -> ma.MaskedArray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload  # (type: T)
    def view(self, /, *, type: type[_ArrayT]) -> _ArrayT: ...
    @overload  # (_: T)
    def view(self, /, dtype: type[_ArrayT]) -> _ArrayT: ...
    @overload  # (dtype: ?)
    def view(self, /, dtype: DTypeLike) -> ndarray[_ShapeT_co, dtype]: ...
    @overload  # (dtype: ?, type: type[T])
    def view(self, /, dtype: DTypeLike, type: type[_ArrayT]) -> _ArrayT: ...

    #
    @overload
    def getfield(self, /, dtype: _DTypeLike[_ScalarT], offset: CanIndex = 0) -> NDArray[_ScalarT]: ...
    @overload
    def getfield(self, /, dtype: DTypeLike, offset: CanIndex = 0) -> NDArray[Any]: ...

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
    def base(self) -> None: ...
    @property
    def ndim(self) -> L[0]: ...
    @property
    def size(self) -> L[1]: ...
    @property
    def shape(self) -> tuple[()]: ...
    @property
    def strides(self) -> tuple[()]: ...
    @property
    def flat(self) -> flatiter[_nt.Array1D[Self]]: ...

    #
    @abc.abstractmethod
    def __init__(self, /, *args: Any, **kwargs: Any) -> None: ...

    #
    @overload
    def __eq__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __eq__(self, other: ndarray[_ShapeT, Any], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_1nd, /) -> NDArray[bool_]: ...
    @overload
    def __eq__(self, other: object, /) -> Any: ...

    #
    @overload
    def __ne__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __ne__(self, other: ndarray[_ShapeT, Any], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_1nd, /) -> NDArray[bool_]: ...
    @overload
    def __ne__(self, other: object, /) -> Any: ...

    #
    @overload
    def __array__(self, dtype: None = None, /) -> ndarray[tuple[()], dtype[Self]]: ...
    @overload
    def __array__(self, dtype: _DTypeT, /) -> ndarray[tuple[()], _DTypeT]: ...

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
        array: ndarray[_ShapeT_1nd, _DTypeT],
        context: tuple[ufunc, tuple[object, ...], int] | None = None,
        return_scalar: py_bool = True,
        /,
    ) -> ndarray[_ShapeT_1nd, _DTypeT]: ...
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
        array: ndarray[_ShapeT, dtype[_ScalarT]],
        context: tuple[ufunc, tuple[object, ...], int] | None = None,
        return_scalar: py_bool = True,
        /,
    ) -> _ScalarT | ndarray[_ShapeT, dtype[_ScalarT]]: ...

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
    ) -> Any: ...

    #
    @overload
    def view(self, /) -> Self: ...
    @overload
    def view(self, /, dtype: type[NDArray[Any]]) -> Self: ...
    @overload
    def view(self, /, *, type: type[NDArray[Any]]) -> Self: ...
    @overload
    def view(self, /, dtype: _DTypeLike[_ScalarT]) -> _ScalarT: ...
    @overload
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[NDArray[Any]]) -> _ScalarT: ...
    @overload
    def view(self, /, dtype: DTypeLike) -> Any: ...
    @overload
    def view(self, /, dtype: DTypeLike, type: type[NDArray[Any]]) -> Any: ...

    #
    @overload
    def getfield(self, /, dtype: _DTypeLike[_ScalarT], offset: CanIndex = 0) -> _ScalarT: ...
    @overload
    def getfield(self, /, dtype: DTypeLike, offset: CanIndex = 0) -> Any: ...

    #
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_0d,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> Self: ...
    @overload
    def take(
        self,
        /,
        indices: _NestedSequence[CanIndex],
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> NDArray[Self]: ...
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_nd,
        axis: CanIndex | None,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...
    @overload
    def take(
        self,
        /,
        indices: _nt.CoInteger_nd,
        axis: CanIndex | None = None,
        *,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...

    #
    def repeat(self, /, repeats: _nt.CoInteger_nd, axis: CanIndex | None = None) -> NDArray[Self]: ...

    #
    def flatten(self, /, order: _OrderKACF = "C") -> _nt.Array1D[Self]: ...
    def ravel(self, /, order: _OrderKACF = "C") -> _nt.Array1D[Self]: ...
    def squeeze(self, axis: L[0] | tuple[()] | None = None) -> Self: ...
    def transpose(self, axes: tuple[()] | None = None, /) -> Self: ...

    #
    @overload  # (() | [])
    def reshape(
        self,
        shape: tuple[()] | list[Never],
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> Self: ...
    @overload  # ((1, *(1, ...))@_ShapeType)
    def reshape(
        self,
        shape: _1NShapeT,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[_1NShapeT, dtype[Self]]: ...
    @overload  # (Sequence[index, ...])  # not recommended
    def reshape(
        self,
        shape: Sequence[CanIndex],
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> Self | _nt.Array[Self]: ...
    @overload  # _(index)
    def reshape(
        self,
        size1: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> _nt.Array1D[Self]: ...
    @overload  # _(index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
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
    @overload  # _(index, index, index, index)
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
    ) -> _nt.Array4D[Self]: ...
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
    ) -> _nt.Array[Self, _nt.AtLeast4D]: ...

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
    @overload
    def __init__(self: _Bool0, value: L[False, 0] | _Bool0 = ..., /) -> None: ...
    @overload
    def __init__(self: _Bool1, value: L[True, 1] | _Bool1, /) -> None: ...
    @overload
    def __init__(self, value: object, /) -> None: ...

    #
    @override
    def __hash__(self, /) -> int: ...
    @override
    def __bool__(self, /) -> _BoolItemT_co: ...
    @override
    def __int__(self, /) -> L[0, 1]: ...
    @deprecated("It will be an error for 'np.bool' scalars to be interpreted as an index in NumPy 2.3.0")
    def __index__(self, /) -> L[0, 1]: ...

    #
    @overload
    def __eq__(self: _Bool0, other: _ToFalse, /) -> _Bool1: ...
    @overload
    def __eq__(self: _Bool1, other: _ToFalse, /) -> _Bool0: ...
    @overload
    def __eq__(self, other: _ToTrue, /) -> Self: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __eq__(self, other: ndarray[_ShapeT, Any], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __eq__(self, other: _nt.ToGeneric_1nd, /) -> NDArray[bool_]: ...
    @overload
    def __eq__(self, other: object, /) -> Any: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __ne__(self: _Bool0, other: _ToTrue, /) -> _Bool1: ...
    @overload
    def __ne__(self: _Bool1, other: _ToTrue, /) -> _Bool0: ...
    @overload
    def __ne__(self, other: _ToFalse, /) -> Self: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_0d, /) -> bool_: ...
    @overload
    def __ne__(self, other: ndarray[_ShapeT, Any], /) -> _nt.Array[bool_, _ShapeT]: ...
    @overload
    def __ne__(self, other: _nt.ToGeneric_1nd, /) -> NDArray[bool_]: ...
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
    def __lt__(self, x: _nt.CoComplex_1nd, /) -> NDArray[bool_]: ...

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
    def __le__(self, x: _nt.CoComplex_1nd, /) -> NDArray[bool_]: ...

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
    def __gt__(self, x: _nt.CoComplex_1nd, /) -> NDArray[bool_]: ...

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
    def __ge__(self, x: _nt.CoComplex_1nd, /) -> NDArray[bool_]: ...

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
    def __divmod__(self, x: _RealNumberT, /) -> _2Tuple[_RealNumberT]: ...
    @overload
    def __divmod__(self, x: py_bool | bool_, /) -> _2Tuple[int8]: ...
    @overload
    def __divmod__(self, x: _nt.JustInt, /) -> _2Tuple[intp]: ...
    @overload
    def __divmod__(self, x: _nt.JustFloat, /) -> _2Tuple[float64]: ...

    # keep in sync with __rmod__
    @overload
    def __rdivmod__(self, x: _RealNumberT, /) -> _2Tuple[_RealNumberT]: ...
    @overload
    def __rdivmod__(self, x: py_bool, /) -> _2Tuple[int8]: ...
    @overload
    def __rdivmod__(self, x: _nt.JustInt, /) -> _2Tuple[intp]: ...
    @overload
    def __rdivmod__(self, x: _nt.JustFloat, /) -> _2Tuple[float64]: ...

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

# TODO(jorenham): Move these protocols to _numtype

class number(
    _CmpOpMixin[_nt.CoComplex_0d, _nt.CoComplex_1nd],
    generic[_NumberItemT_co],
    Generic[_BitT, _NumberItemT_co],
):
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[int, Self]: ...
    @final
    @type_check_only
    def __nep50_int__(self, /) -> Self: ...
    @abc.abstractmethod
    @type_check_only
    def __nep50_float__(self, /) -> inexact: ...
    @abc.abstractmethod
    @type_check_only
    def __nep50_complex__(self, /) -> complexfloating: ...
    #
    @type_check_only
    def __nep50_rule6__(self, other: _JustNumber, /) -> number: ...

    #
    @property
    @override
    def itemsize(self) -> int: ...

    #
    @abc.abstractmethod
    def __init__(self, value: _NumberItemT_co, /) -> None: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

    #
    def __abs__(self, /) -> number[_BitT]: ...
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
    def __add__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __radd__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __radd__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __radd__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __radd__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __sub__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __sub__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __sub__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __sub__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __rsub__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rsub__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __rsub__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __rsub__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __mul__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __mul__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __mul__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __mul__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __rmul__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rmul__(self, x: _nt.CastsWithScalar[Self, _ScalarT], /) -> _ScalarT: ...
    @overload
    def __rmul__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _InexactT: ...
    @overload
    def __rmul__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __pow__(self, x: _nt.CastsScalar[Self] | int, mod: None = None, /) -> Self: ...
    @overload
    def __pow__(self, x: _nt.CastsWithScalar[Self, _ScalarT], mod: None = None, /) -> _ScalarT: ...
    @overload
    def __pow__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, mod: None = None, /) -> _InexactT: ...
    @overload
    def __pow__(
        self: _nt.CastsWithComplex[_ComplexFloatingT],
        x: _nt.JustComplex,
        mod: None = None,
        /,
    ) -> _ComplexFloatingT: ...

    # keep in sync with __add__
    @overload
    def __rpow__(self, x: _nt.CastsScalar[Self] | int, mod: None = None, /) -> Self: ...
    @overload
    def __rpow__(self, x: _nt.CastsWithScalar[Self, _ScalarT], mod: None = None, /) -> _ScalarT: ...
    @overload
    def __rpow__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, mod: None = None, /) -> _InexactT: ...
    @overload
    def __rpow__(
        self: _nt.CastsWithComplex[_ComplexFloatingT],
        x: _nt.JustComplex,
        mod: None = None,
        /,
    ) -> _ComplexFloatingT: ...

    #
    @overload
    def __truediv__(self, x: _nt.CoFloat64_0d | _nt.CastsScalar[Self] | _JustNumber, /) -> inexact: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

    #
    @overload
    def __rtruediv__(self, x: _nt.CoFloat64_0d | _nt.CastsScalar[Self] | _JustNumber, /) -> inexact: ...
    @overload
    def __rtruediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...

# NOTE: at least ~95% of the relevant platforms are 64-bit at the moment, and this
# increases over time. Assuming that this *always* holds significantly reduces the
# complexity of the `[u]intp` and `[u]long` type definitions.

class integer(_IntegralMixin, _RoundMixin, number[_BitT, int]):
    @abc.abstractmethod
    @type_check_only
    def __nep50__(
        self,
        below: timedelta64 | _inexact64_min | _JustFloating | _JustInexact,
        above: bool_,
        /,
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
    def __init__(self, value: _ConvertibleToInt = ..., /) -> None: ...

    #
    @override
    def __abs__(self, /) -> Self: ...
    def __invert__(self, /) -> Self: ...

    #
    @overload
    def __truediv__(self, x: _nt.CoInteger_0d | float, /) -> float64: ...
    @overload
    def __truediv__(self, x: _nt.JustComplex, /) -> complex128: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    #
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
    def __divmod__(self, x: _nt.CastsScalar[Self] | int, /) -> _2Tuple[Self]: ...
    @overload
    def __divmod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _2Tuple[_RealScalarT]: ...
    @overload
    def __divmod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _2Tuple[_InexactT]: ...
    #
    @overload
    def __rdivmod__(self, x: _nt.CastsScalar[Self] | int, /) -> _2Tuple[Self]: ...
    @overload
    def __rdivmod__(self, x: _nt.CastsWithScalar[Self, _RealScalarT], /) -> _2Tuple[_RealScalarT]: ...
    @overload
    def __rdivmod__(self: _nt.CastsWithFloat[_InexactT], x: _nt.JustFloat, /) -> _2Tuple[_InexactT]: ...

    #
    @overload
    def __lshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __lshift__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...
    #
    @overload
    def __rlshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rlshift__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...

    #
    @overload
    def __rshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rshift__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...
    #
    @overload
    def __rrshift__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rrshift__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...

    #
    @overload
    def __and__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __and__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...
    #
    @overload
    def __rand__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rand__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...

    #
    @overload
    def __xor__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __xor__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...
    #
    @overload
    def __rxor__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __rxor__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...

    #
    @overload
    def __or__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __or__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...
    #
    @overload
    def __ror__(self, x: _nt.CastsScalar[Self] | int, /) -> Self: ...
    @overload
    def __ror__(self, x: _nt.CastsWithScalar[Self, _IntScalarT], /) -> _IntScalarT: ...

class signedinteger(integer[_BitT]):
    @abc.abstractmethod
    @type_check_only
    @override
    def __nep50__(
        self,
        below: int64 | timedelta64 | _inexact64_min | _JustFloating | _JustInexact,
        above: bool_,
        /,
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

class int8(_IntMixin[L[1]], signedinteger[_n._8]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: signedinteger | timedelta64 | inexact | _JustFloating | _JustInexact,
        above: bool_,
        /,
    ) -> int8: ...
    @type_check_only
    def __nep50_rule2__(self, other: uint8, /) -> int16: ...
    @type_check_only
    def __nep50_rule3__(self, other: uint16, /) -> int32: ...

byte = int8

class int16(_IntMixin[L[2]], signedinteger[_n._16]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: _int16_min | timedelta64 | _float32_min | _JustFloating | complexfloating | _JustInexact,
        above: _nt.co_integer8,
        /,
    ) -> int16: ...
    @type_check_only
    def __nep50_rule2__(self, other: uint16, /) -> int32: ...
    @type_check_only
    def __nep50_rule3__(self, other: float16, /) -> float32: ...

short = int16

class int32(_IntMixin[L[4]], signedinteger[_n._32]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: _int32_min | timedelta64 | _inexact64_min | _JustFloating | _JustInexact,
        above: _nt.co_integer16,
        /,
    ) -> int32: ...
    @override
    @type_check_only
    def __nep50_rule1__(self, other: uint64 | float16 | float32, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustComplexFloating, /) -> complexfloating: ...

intc = int32

class int64(_IntMixin[L[8]], signedinteger[_n._64]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: int64 | timedelta64 | _inexact64_min | _JustFloating | _JustInexact,
        above: _nt.co_integer32,
        /,
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

if sys.platform == "win32":
    long: TypeAlias = int32  # pyright: ignore[reportRedeclaration]
else:
    long: TypeAlias = int64  # pyright: ignore[reportRedeclaration]

longlong = int64

intp = int64
int_ = intp

class unsignedinteger(integer[_BitT]):
    @abc.abstractmethod
    @type_check_only
    @override
    def __nep50__(
        self,
        below: uint64 | timedelta64 | _inexact64_min | _JustFloating | _JustInexact,
        above: bool_,
        /,
    ) -> unsignedinteger: ...
    @type_check_only
    def __nep50_rule3__(self, other: _JustUnsignedInteger, /) -> unsignedinteger: ...

class uint8(_IntMixin[L[1]], unsignedinteger[_n._8]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: _int16_min | unsignedinteger | timedelta64 | _JustFloating | inexact | _JustInexact,
        above: bool_,
        /,
    ) -> uint8: ...
    @type_check_only
    def __nep50_rule0__(self, other: int8, /) -> int16: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer: ...

ubyte = uint8

class uint16(_IntMixin[L[2]], unsignedinteger[_n._16]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: uint16 | _integer32_min | timedelta64 | _float32_min | _JustFloating | complexfloating | _JustInexact,
        above: _nt.co_uint8,
        /,
    ) -> uint16: ...
    @type_check_only
    def __nep50_rule0__(self, other: _int16_max, /) -> int32: ...
    @type_check_only
    def __nep50_rule1__(self, other: float16, /) -> float32: ...
    @override
    @type_check_only
    def __nep50_rule4__(self, other: _JustSignedInteger, /) -> signedinteger: ...
    @override
    @type_check_only
    def __nep50_rule5__(self, other: _JustInteger, /) -> integer: ...

ushort = uint16

class uint32(_IntMixin[L[4]], unsignedinteger[_n._32]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: uint32 | _nt.integer64 | timedelta64 | _inexact64_min | _AbstractInexact,
        above: _nt.co_uint16,
        /,
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

uintc = uint32

class uint64(_IntMixin[L[8]], unsignedinteger[_n._64]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: uint64 | timedelta64 | _inexact64_min | _AbstractInexact,
        above: _nt.co_uint32,
        /,
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

if sys.platform == "win32":
    ulong: TypeAlias = uint32  # pyright: ignore[reportRedeclaration]
else:
    ulong: TypeAlias = uintp  # pyright: ignore[reportRedeclaration]

ulonglong = uint64

uintp = uint64
uint = uintp

class inexact(number[_BitT, _InexactItemT_co], Generic[_BitT, _InexactItemT_co]):
    @abc.abstractmethod
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
    @abc.abstractmethod
    def __init__(self, value: _InexactItemT_co | None = ..., /) -> None: ...
    @abc.abstractmethod
    @override
    def __abs__(self, /) -> floating: ...

    #
    @overload
    def __truediv__(self, x: int | _nt.JustFloat | _nt.CastsScalar[Self], /) -> Self: ...
    @overload
    def __truediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    #
    @overload
    def __rtruediv__(self, x: int | _nt.JustFloat | _nt.CastsScalar[Self], /) -> Self: ...
    @overload
    def __rtruediv__(self, x: _nt.CastsWithScalar[Self, _InexactT], /) -> _InexactT: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ComplexFloatingT], x: _nt.JustComplex, /) -> _ComplexFloatingT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class floating(_RealMixin, _RoundMixin, inexact[_BitT, float]):
    @abc.abstractmethod
    @override
    @type_check_only
    def __nep50__(self, below: _nt.inexact64l, above: _nt.co_integer8, /) -> floating: ...
    @override
    @type_check_only
    def __nep50_rule3__(self, other: _JustFloating, /) -> floating: ...

    #
    @override
    def __init__(self, value: _ConvertibleToFloat | None = ..., /) -> None: ...
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
    def __divmod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> _2Tuple[Self]: ...
    @overload
    def __divmod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _2Tuple[_FloatingT]: ...
    #
    @overload
    def __rdivmod__(self, x: _nt.CastsScalar[Self] | int | _nt.JustFloat, /) -> _2Tuple[Self]: ...
    @overload
    def __rdivmod__(self, x: _nt.CastsWithScalar[Self, _FloatingT], /) -> _2Tuple[_FloatingT]: ...

class float16(_FloatMixin[L[2]], floating[_n._16]):
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

half = float16

class float32(_FloatMixin[L[4]], floating[_n._32]):
    @override
    @type_check_only
    def __nep50__(self, below: _float32_min | complexfloating, above: float16 | _nt.co_integer16, /) -> float32: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex64: ...
    @type_check_only
    def __nep50_rule1__(self, other: _nt.integer32 | _nt.integer64, /) -> float64: ...
    @type_check_only
    def __nep50_rule2__(self, other: _AbstractInteger, /) -> floating: ...

single = float32

class float64(_FloatMixin[L[8]], floating[_n._64], float):  # type: ignore[misc]
    @override
    @type_check_only
    def __nep50__(self, below: _inexact64_min, above: _float32_max | _nt.co_integer, /) -> float64: ...
    @override
    @type_check_only
    def __nep50_complex__(self, /) -> complex128: ...
    @type_check_only
    def __nep50_rule2__(self, other: complex64, /) -> complex128: ...

    #
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...
    @classmethod
    def __getformat__(cls, typestr: L["double", "float"], /) -> str: ...

    #
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

class longdouble(_FloatMixin[L[12, 16]], floating[_n._64L]):
    @override
    @type_check_only
    def __nep50__(
        self,
        below: longdouble | clongdouble,
        above: _nt.co_float64,
        /,
    ) -> longdouble: ...
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
    @overload
    def item(self, /) -> Self: ...
    @overload
    def item(self, arg0: L[0, -1] | tuple[L[0, -1]] | tuple[()], /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tolist(self, /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

float96 = longdouble
float128 = longdouble

class complexfloating(inexact[_BitT1, complex], Generic[_BitT1, _BitT2]):
    @abc.abstractmethod
    @override
    @type_check_only
    def __nep50__(self, below: clongdouble, above: _float32_max | _nt.co_integer16, /) -> complexfloating: ...
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
    @overload
    def __init__(self, real: _ConvertibleToComplex | None = 0, /) -> None: ...
    @overload
    def __init__(self, real: _ToReal = 0, imag: _ToImag = 0, /) -> None: ...

    #
    @property
    @abc.abstractmethod
    @override
    def real(self) -> floating: ...
    @property
    @abc.abstractmethod
    @override
    def imag(self) -> floating: ...

    #
    @abc.abstractmethod
    @override
    def __abs__(self, /) -> floating: ...

    #
    @deprecated(
        "The Python built-in `round` is deprecated for complex scalars, "
        "and will raise a `TypeError` in a future release"
    )
    def __round__(self, /, ndigits: CanIndex | None = None) -> Self: ...

class complex64(complexfloating[_n._32]):
    @override
    @type_check_only
    def __nep50__(self, below: complexfloating, above: _float32_max | _nt.co_integer16, /) -> complex64: ...
    @type_check_only
    def __nep50_rule0__(self, other: _nt.integer32 | _nt.integer64 | float64, /) -> complex128: ...
    @type_check_only
    def __nep50_rule1__(self, other: longdouble, /) -> clongdouble: ...

    #
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

class complex128(complexfloating[_n._64], complex):  # type: ignore[misc]
    @override
    @type_check_only
    def __nep50__(self, below: _complex128_min, above: complex64 | _float64_max | _nt.co_integer, /) -> complex128: ...
    @type_check_only
    def __nep50_rule1__(self, other: longdouble, /) -> clongdouble: ...
    @override
    @type_check_only
    def __nep50_rule2__(self, other: integer | _AbstractInteger, /) -> complex128: ...

    #
    @overload
    def __new__(cls, real: _ConvertibleToComplex | None = 0, /) -> Self: ...
    @overload
    def __new__(cls, real: _ToReal = 0, imag: _ToImag = 0, /) -> Self: ...

    #
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

class clongdouble(complexfloating[_n._64L]):
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
    @overload
    def item(self, /) -> Self: ...
    @overload
    def item(self, arg0: L[0, -1] | tuple[L[0, -1]] | tuple[()], /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tolist(self, /) -> Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

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
    @type_check_only
    def __nep50__(self, below: object_, above: _nt.co_number | character, /) -> object_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_JustBuiltinScalar, object_]: ...

    #
    @overload
    def __new__(cls, nothing_to_see_here: None = None, /) -> None: ...  # type: ignore[misc]
    @overload
    def __new__(cls, stringy: str, /) -> str: ...  # type: ignore[misc]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __new__(cls, stringy: bytes, /) -> bytes: ...  # type: ignore[misc]
    @overload
    def __new__(cls, array: ndarray[_ShapeT, Any], /) -> ndarray[_ShapeT, dtype[Self]]: ...  # type: ignore[misc]
    @overload
    def __new__(cls, sequence: SupportsLenAndGetItem[object], /) -> NDArray[Self]: ...  # type: ignore[misc]
    @overload
    def __new__(cls, value: _T, /) -> _T: ...  # type: ignore[misc]
    @overload  # catch-all
    def __new__(cls, value: Any = ..., /) -> object | NDArray[Self]: ...  # type: ignore[misc]

    #
    def __init__(self, value: object = ..., /) -> None: ...
    @override
    def __hash__(self, /) -> int: ...
    def __abs__(self, /) -> object_: ...
    def __call__(self, /, *args: object, **kwargs: object) -> Any: ...

    if sys.version_info >= (3, 12):
        def __release_buffer__(self, buffer: memoryview, /) -> None: ...

@final
class flexible(_RealMixin, generic[_FlexItemT_co], Generic[_FlexItemT_co]):  # type: ignore[misc]
    @abc.abstractmethod
    def __init__(self, /, *args: Any, **kwargs: Any) -> None: ...

class character(flexible[_CharacterItemT_co], Generic[_CharacterItemT_co]):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    @abc.abstractmethod
    def __init__(self, value: _CharacterItemT_co = ..., /) -> None: ...

class bytes_(character[bytes], bytes):  # type: ignore[misc]
    @type_check_only
    def __nep50__(self, below: bytes_ | object_, above: Never, /) -> bytes_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_nt.JustBytes, bytes_]: ...

    #
    @overload
    def __new__(cls, s: str, /, encoding: str, errors: str = "strict") -> Self: ...
    @overload
    def __new__(cls, o: object = b"", /) -> Self: ...
    @overload
    def __init__(self, s: str, /, encoding: str, errors: str = "strict") -> None: ...
    @overload
    def __init__(self, o: object = b"", /) -> None: ...

class str_(character[str], str):  # type: ignore[misc]
    @type_check_only
    def __nep50__(self, below: str_ | object_, above: Never, /) -> str_: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[_nt.JustStr, str_]: ...

    #
    @overload
    def __new__(cls, value: object = "", /) -> Self: ...
    @overload
    def __new__(cls, value: bytes, /, encoding: str = "utf-8", errors: str = "strict") -> Self: ...
    @overload
    def __init__(self, value: object = "", /) -> None: ...
    @overload
    def __init__(self, value: bytes, /, encoding: str = "utf-8", errors: str = "strict") -> None: ...

class void(flexible[bytes | tuple[Any, ...]]):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    @type_check_only
    def __nep50__(self, below: object_, from_: Never, /) -> void: ...

    #
    @overload
    def __init__(self, value: _nt.CoInteger_0d | bytes, /, dtype: None = None) -> None: ...
    @overload
    def __init__(self, value: Any, /, dtype: _DTypeLikeVoid) -> None: ...
    @overload
    def __getitem__(self, key: str | CanIndex, /) -> Any: ...
    @overload
    def __getitem__(self, key: list[str], /) -> void: ...
    def __setitem__(self, key: str | list[str] | CanIndex, value: ArrayLike, /) -> None: ...
    @override
    def setfield(self, val: ArrayLike, dtype: DTypeLike, offset: int = ...) -> None: ...

class datetime64(
    _RealMixin,
    _CmpOpMixin[datetime64, _ArrayLikeDT64_co],
    generic[_DT64ItemT_co],
    Generic[_DT64ItemT_co],
):
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...

    #
    @overload
    def __init__(self, value: datetime64[_DT64ItemT_co], /) -> None: ...
    @overload
    def __init__(self: datetime64[None], value: _NaTValue | None = ..., format: _TimeUnitSpec = ..., /) -> None: ...
    @overload
    def __init__(self: datetime64[dt.datetime], value: dt.datetime, /) -> None: ...
    @overload
    def __init__(self: datetime64[dt.date], value: dt.date, /) -> None: ...
    @overload
    def __init__(
        self: datetime64[dt.datetime],
        value: _DT64Now,
        format: _TimeUnitSpec[_NativeTimeUnit] = ...,
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: datetime64[dt.date],
        value: _DT64Date,
        format: _TimeUnitSpec[_DateUnit] = ...,
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: datetime64[int],
        value: int | bytes | str | dt.date,
        format: _TimeUnitSpec[_IntTimeUnit],
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: datetime64[dt.datetime],
        value: int | bytes | str | dt.date,
        format: _TimeUnitSpec[_NativeTimeUnit],
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: datetime64[dt.date],
        value: int | bytes | str | dt.date,
        format: _TimeUnitSpec[_DateUnit],
        /,
    ) -> None: ...
    @overload
    def __init__(self, value: bytes | str | dt.date | None, format: _TimeUnitSpec = ..., /) -> None: ...

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
    _CmpOpMixin[_nt.CoTimeDelta_0d, _nt.CoTimeDelta_1nd],
    _IntegralMixin,
    generic[_TD64ItemT_co],
    Generic[_TD64ItemT_co],
):
    @type_check_only
    def __nep50__(self, below: timedelta64, above: _nt.co_integer, /) -> timedelta64: ...
    @type_check_only
    def __nep50_builtin__(self, /) -> tuple[int, timedelta64]: ...

    #
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...

    #
    @overload
    def __init__(self, value: _TD64ItemT_co | timedelta64[_TD64ItemT_co], /) -> None: ...
    @overload
    def __init__(self: timedelta64[L[0]], /) -> None: ...
    @overload
    def __init__(self: timedelta64[None], value: _NaTValue | None, format: _TimeUnitSpec, /) -> None: ...
    @overload
    def __init__(self: timedelta64[L[0]], value: L[0], format: _TimeUnitSpec[_IntTD64Unit] = ..., /) -> None: ...
    @overload
    def __init__(
        self: timedelta64[int],
        value: _nt.CoInteger_0d,
        format: _TimeUnitSpec[_IntTD64Unit] = ...,
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: timedelta64[int],
        value: dt.timedelta,
        format: _TimeUnitSpec[_IntTimeUnit],
        /,
    ) -> None: ...
    @overload
    def __init__(
        self: timedelta64[dt.timedelta],
        value: _TD64Like_co,
        format: _TimeUnitSpec[_NativeTD64Unit] = ...,
        /,
    ) -> None: ...
    @overload
    def __init__(self, value: _ConvertibleToTD64, format: _TimeUnitSpec = ..., /) -> None: ...

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
        self: timedelta64[dt.timedelta],
        x: timedelta64[dt.timedelta],
        /,
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
        self: timedelta64[dt.timedelta],
        x: timedelta64[dt.timedelta],
        /,
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
    default=Callable[Concatenate[Any, Any, ...], ndarray[Any, dtype]],
    covariant=True,
)
_AccumulateT_co = TypeVar(
    "_AccumulateT_co",
    bound=Callable[Concatenate[Never, ...], object],
    default=Callable[Concatenate[Any, ...], ndarray[Any, dtype]],
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
    def __doc__(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride]

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
