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
    SupportsComplex as CanComplex,
    SupportsFloat as CanFloat,
    SupportsIndex as CanIndex,
    SupportsInt as CanInt,
    TypeAlias,
    TypedDict,
    final,
    overload,
    runtime_checkable,
    type_check_only,
)
from typing_extensions import CapsuleType, LiteralString, Never, Protocol, Self, TypeVar, Unpack, deprecated, override

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
from ._expired_attrs_2_0 import __expired_attributes__ as __expired_attributes__
from ._globals import _CopyMode
from ._pytesttester import PytestTester
from ._typing import (
    ArrayLike,
    DTypeLike,
    NBitBase,
    NDArray,
    _8Bit,
    _16Bit,
    _32Bit,
    _64Bit,
    _96Bit,
    _128Bit,
    _ArrayLike,
    _ArrayLikeBool_co,
    _ArrayLikeComplex128_co,
    _ArrayLikeComplex_co,
    _ArrayLikeDT64_co,
    _ArrayLikeFloat64_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt,
    _ArrayLikeInt_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
    _ArrayLikeUInt_co,
    _CharLike_co,
    _ComplexFloatingCodes,
    _DTypeLike,
    _DTypeLikeVoid,
    _IntLike_co,
    _NBitIntP,
    _NBitLong,
    _NBitLongDouble,
    _NBitLongLong,
    _NestedSequence,
    _NumberLike_co,
    _ScalarLike_co,
    _ShapeLike,
    _TD64Like_co,
    _VoidDTypeLike,
)
from ._typing._callable import (
    _BoolDivMod,
    _BoolMod,
    _BoolOp,
    _BoolSub,
    _BoolTrueDiv,
    _ComparisonOpGE,
    _ComparisonOpGT,
    _ComparisonOpLE,
    _ComparisonOpLT,
)
from ._typing._char_codes import (
    _BoolCodes,
    _BytesCodes,
    _CLongDoubleCodes,
    _CharacterCodes,
    _Complex64Codes,
    _Complex128Codes,
    _Complex192Codes,
    _Complex256Codes,
    _DT64Codes,
    _FlexibleCodes,
    _Float16Codes,
    _Float32Codes,
    _Float64Codes,
    _Float96Codes,
    _Float128Codes,
    _FloatingCodes,
    _GenericCodes,
    _InexactCodes,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntPCodes,
    _IntegerCodes,
    _LongCodes,
    _LongDoubleCodes,
    _LongLongCodes,
    _NumberCodes,
    _ObjectCodes,
    _SignedIntegerCodes,
    _StrCodes,
    _StringCodes,
    _TD64Codes,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntPCodes,
    _ULongCodes,
    _ULongLongCodes,
    _UnsignedIntegerCodes,
    _VoidCodes,
)
from ._typing._ufunc import _Call21Bool, _gufunc_2_1, _ufunc_1_1, _ufunc_1_2, _ufunc_2_1, _ufunc_2_2
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
from .lib._polynomial_impl import poly, poly1d, polyadd, polyder, polydiv, polyfit, polyint, polymul, polysub, polyval, roots
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

@runtime_checkable
class _Buffer(Protocol):
    def __buffer__(self, flags: int, /) -> memoryview: ...

if sys.version_info >= (3, 12):
    _SupportsBuffer: TypeAlias = _Buffer
else:
    import array as _array
    import mmap as _mmap

    from numpy import distutils as distutils  # noqa: ICN003

    _SupportsBuffer: TypeAlias = (
        _Buffer | bytes | bytearray | memoryview | _array.array[Any] | _mmap.mmap | NDArray[Any] | generic
    )

__all__ = [  # noqa: RUF022
    # __numpy_submodules__
    "char", "core", "ctypeslib", "dtypes", "exceptions", "f2py", "fft", "lib", "linalg", "ma", "polynomial", "random", "rec",
    "strings", "test", "testing", "typing",
    # _core.*
    "False_", "ScalarType", "True_", "abs", "absolute", "acos", "acosh", "add", "all", "allclose", "amax", "amin", "any",
    "arange", "arccos", "arccosh", "arcsin", "arcsinh", "arctan", "arctan2", "arctanh", "argmax", "argmin", "argpartition",
    "argsort", "argwhere", "around", "array", "array2string", "array_equal", "array_equiv", "array_repr", "array_str",
    "asanyarray", "asarray", "ascontiguousarray", "asfortranarray", "asin", "asinh", "astype", "atan", "atan2", "atanh",
    "atleast_1d", "atleast_2d", "atleast_3d", "base_repr", "binary_repr", "bitwise_and", "bitwise_count", "bitwise_invert",
    "bitwise_left_shift", "bitwise_not", "bitwise_or", "bitwise_right_shift", "bitwise_xor", "block", "bool", "bool_",
    "broadcast", "busday_count", "busday_offset", "busdaycalendar", "byte", "bytes_", "can_cast", "cbrt", "cdouble", "ceil",
    "character", "choose", "clip", "clongdouble", "complex128", "complex192", "complex256", "complex64", "complexfloating",
    "compress", "concat", "concatenate", "conj", "conjugate", "convolve", "copysign", "copyto", "correlate", "cos", "cosh",
    "count_nonzero", "cross", "csingle", "cumprod", "cumsum", "cumulative_prod", "cumulative_sum", "datetime64",
    "datetime_as_string", "datetime_data", "deg2rad", "degrees", "diagonal", "divide", "divmod", "dot", "double", "dtype", "e",
    "einsum", "einsum_path", "empty", "empty_like", "equal", "errstate", "euler_gamma", "exp", "exp2", "expm1", "fabs", "finfo",
    "flatiter", "flatnonzero", "flexible", "float128", "float16", "float32", "float64", "float96", "float_power", "floating",
    "floor", "floor_divide", "fmax", "fmin", "fmod", "format_float_positional", "format_float_scientific", "frexp", "from_dlpack",
    "frombuffer", "fromfile", "fromfunction", "fromiter", "frompyfunc", "fromstring", "full", "full_like", "gcd", "generic",
    "geomspace", "get_printoptions", "getbufsize", "geterr", "geterrcall", "greater", "greater_equal", "half", "heaviside",
    "hstack", "hypot", "identity", "iinfo", "indices", "inexact", "inf", "inner", "int8", "int16", "int32", "int64", "int_",
    "intc", "integer", "intp", "invert", "is_busday", "isclose", "isdtype", "isfinite", "isfortran", "isinf", "isnan", "isnat",
    "isscalar", "issubdtype", "lcm", "ldexp", "left_shift", "less", "less_equal", "lexsort", "linspace", "little_endian", "log",
    "log10", "log1p", "log2", "logaddexp", "logaddexp2", "logical_and", "logical_not", "logical_or", "logical_xor", "logspace",
    "long", "longdouble", "longlong", "matmul", "matrix_transpose", "matvec", "max", "maximum", "may_share_memory", "mean",
    "memmap", "min", "min_scalar_type", "minimum", "mod", "modf", "moveaxis", "multiply", "nan", "ndarray", "ndim", "nditer",
    "negative", "nested_iters", "newaxis", "nextafter", "nonzero", "not_equal", "number", "object_", "ones", "ones_like", "outer",
    "partition", "permute_dims", "pi", "positive", "pow", "power", "printoptions", "prod", "promote_types", "ptp", "put",
    "putmask", "rad2deg", "radians", "ravel", "recarray", "reciprocal", "record", "remainder", "repeat", "require", "reshape",
    "resize", "result_type", "right_shift", "rint", "roll", "rollaxis", "round", "sctypeDict", "searchsorted", "set_printoptions",
    "setbufsize", "seterr", "seterrcall", "shape", "shares_memory", "short", "sign", "signbit", "signedinteger", "sin", "single",
    "sinh", "size", "sort", "spacing", "sqrt", "square", "squeeze", "stack", "std", "str_", "subtract", "sum", "swapaxes", "take",
    "tan", "tanh", "tensordot", "timedelta64", "trace", "transpose", "true_divide", "trunc", "typecodes", "ubyte", "ufunc",
    "uint", "uint16", "uint32", "uint64", "uint64", "uint8", "uintc", "uintp", "ulong", "ulonglong", "unsignedinteger", "unstack",
    "ushort", "var", "vdot", "vecdot", "vecmat", "void", "vstack", "where", "zeros", "zeros_like",
    # matrixlib.*
    "matrix", "bmat", "asmatrix",
    # lib._arraypad_impl.*
    "pad",
    # lib._arraysetops_impl.*
    "ediff1d", "in1d", "intersect1d", "isin", "setdiff1d", "setxor1d", "union1d", "unique", "unique_all", "unique_counts",
    "unique_inverse", "unique_values",
    # lib._function_base_impl.*
    "angle", "append", "asarray_chkfinite", "average", "bartlett", "bincount", "blackman", "copy", "corrcoef", "cov", "delete",
    "diff", "digitize", "extract", "flip", "gradient", "hamming", "hanning", "i0", "insert", "interp", "iterable", "kaiser",
    "median", "meshgrid", "percentile", "piecewise", "place", "quantile", "rot90", "select", "sinc", "sort_complex", "trapezoid",
    "trapz", "trim_zeros", "unwrap", "vectorize",
    # lib._histograms_impl.*
    "histogram", "histogram_bin_edges", "histogramdd",
    # lib._index_tricks_impl.*
    "c_", "diag_indices", "diag_indices_from", "fill_diagonal", "index_exp", "ix_", "mgrid", "ndenumerate", "ndindex", "ogrid",
    "r_", "ravel_multi_index", "s_", "unravel_index",
    # lib._nanfunctions_impl.*
    "nanargmax", "nanargmin", "nancumprod", "nancumsum", "nanmax", "nanmean", "nanmedian", "nanmin", "nanpercentile", "nanprod",
    "nanquantile", "nanstd", "nansum", "nanvar",
    # lib._npyio_impl.*
    "fromregex", "genfromtxt", "load", "loadtxt", "packbits", "save", "savetxt", "savez", "savez_compressed", "unpackbits",
    # lib._polynomial_impl.*
    "poly", "poly1d", "polyadd", "polyder", "polydiv", "polyfit", "polyint", "polymul", "polysub", "polyval", "roots",
    # lib._scimath_impl
    "emath",
    # lib._shape_base_impl
    "apply_along_axis", "apply_over_axes", "array_split", "row_stack", "column_stack", "dsplit", "dstack", "expand_dims",
    "hsplit", "kron", "put_along_axis", "split", "take_along_axis", "tile", "vsplit",
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
    tuple[()],  # 0-d
    tuple[int],  # 1-d
    tuple[int, int],  # 2-d
    tuple[int, int, int],  # 3-d
    tuple[int, int, int, int],  # 4-d
    tuple[int, int, int, int, int],  # 5-d
    tuple[int, int, int, int, int, int],  # 6-d
    tuple[int, int, int, int, int, int, int],  # 7-d
    tuple[int, int, int, int, int, int, int, int],  # 8-d
    tuple[int, ...],  # N-d
)
_AnyNBitInexact = TypeVar("_AnyNBitInexact", _16Bit, _32Bit, _64Bit, _NBitLongDouble)
_AnyTD64Item = TypeVar("_AnyTD64Item", dt.timedelta, int, None, dt.timedelta | int | None)
_AnyDT64Arg = TypeVar("_AnyDT64Arg", dt.datetime, dt.date, None)
_AnyDate = TypeVar("_AnyDate", dt.date, dt.datetime)
_AnyDateOrTime = TypeVar("_AnyDateOrTime", dt.date, dt.datetime, dt.timedelta)

###
# Type parameters (for internal use only)

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
_RealT_co = TypeVar("_RealT_co", covariant=True)
_ImagT_co = TypeVar("_ImagT_co", covariant=True)

_DTypeT = TypeVar("_DTypeT", bound=dtype[Any])
_DTypeT_co = TypeVar("_DTypeT_co", bound=dtype[Any], covariant=True)
_FlexDTypeT = TypeVar("_FlexDTypeT", bound=dtype[flexible])

_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])
_IntegralArrayT = TypeVar("_IntegralArrayT", bound=NDArray[integer | bool_ | object_])
_RealArrayT = TypeVar("_RealArrayT", bound=NDArray[floating | integer | timedelta64 | bool_ | object_])
_NumericArrayT = TypeVar("_NumericArrayT", bound=NDArray[number | timedelta64 | object_])

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], covariant=True)
_ShapeT_1nd = TypeVar("_ShapeT_1nd", bound=tuple[int, Unpack[tuple[int, ...]]])
_1NShapeT = TypeVar("_1NShapeT", bound=tuple[L[1], Unpack[tuple[L[1], ...]]])  # (1,) | (1, 1) | (1, 1, 1) | ...

_ScalarT = TypeVar("_ScalarT", bound=generic)
_ScalarT_co = TypeVar("_ScalarT_co", bound=generic, covariant=True)
_NumberT = TypeVar("_NumberT", bound=number)
_RealNumberT = TypeVar("_RealNumberT", bound=floating | integer)
_IntegerT = TypeVar("_IntegerT", bound=integer)
_SignedIntegerT = TypeVar("_SignedIntegerT", bound=signedinteger)
_UnsignedIntegerT = TypeVar("_UnsignedIntegerT", bound=unsignedinteger)
_CharT = TypeVar("_CharT", bound=character)

_NBitT = TypeVar("_NBitT", bound=NBitBase, default=Any)
_NBitT1 = TypeVar("_NBitT1", bound=NBitBase, default=Any)
_NBitT2 = TypeVar("_NBitT2", bound=NBitBase, default=_NBitT1)

_ItemT_co = TypeVar("_ItemT_co", default=Any, covariant=True)
_BoolItemT = TypeVar("_BoolItemT", bound=py_bool)
_BoolItemT_co = TypeVar("_BoolItemT_co", bound=py_bool, default=py_bool, covariant=True)
_NumberItemT_co = TypeVar("_NumberItemT_co", bound=complex, default=Any, covariant=True)
_InexactItemT_co = TypeVar("_InexactItemT_co", bound=complex, default=Any, covariant=True)
_FlexItemT_co = TypeVar(
    "_FlexItemT_co",
    bound=_CharLike_co | tuple[object, ...],
    default=_CharLike_co | tuple[Any, ...],
    covariant=True,
)
_CharacterItemT_co = TypeVar("_CharacterItemT_co", bound=_CharLike_co, default=_CharLike_co, covariant=True)
_TD64ItemT = TypeVar("_TD64ItemT", bound=dt.timedelta | int | None)
_TD64ItemT_co = TypeVar("_TD64ItemT_co", bound=dt.timedelta | int | None, default=dt.timedelta | int | None, covariant=True)
_DT64ItemT = TypeVar("_DT64ItemT", bound=dt.date | int | None)
_DT64ItemT_co = TypeVar("_DT64ItemT_co", bound=dt.date | int | None, default=dt.date | int | None, covariant=True)
_TD64UnitT = TypeVar("_TD64UnitT", bound=_TD64Unit, default=_TD64Unit)

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

_Falsy: TypeAlias = L[False, 0] | bool_[L[False]]
_Truthy: TypeAlias = L[True, 1] | bool_[L[True]]

_1D: TypeAlias = tuple[int]
_2Tuple: TypeAlias = tuple[_T, _T]

_ArrayUInt_co: TypeAlias = NDArray[unsignedinteger | bool_]
_ArrayInt_co: TypeAlias = NDArray[integer | bool_]
_ArrayFloat64_co: TypeAlias = NDArray[floating[_64Bit] | float32 | float16 | integer | bool_]
_ArrayFloat_co: TypeAlias = NDArray[floating | integer | bool_]
_ArrayComplex128_co: TypeAlias = NDArray[number[_64Bit] | number[_32Bit] | float16 | integer | bool_]
_ArrayComplex_co: TypeAlias = NDArray[number | bool_]
_ArrayTD64_co: TypeAlias = NDArray[timedelta64 | integer | bool_]

_Float64_co: TypeAlias = float | floating[_64Bit] | float32 | float16 | integer | bool_
_Complex64_co: TypeAlias = inexact[_32Bit] | number[_16Bit] | number[_8Bit] | py_bool | bool_
_Complex128_co: TypeAlias = complex | number[_64Bit] | _Complex64_co

_ToIndex: TypeAlias = CanIndex | slice | EllipsisType | _ArrayLikeInt_co | None
_ToIndices: TypeAlias = _ToIndex | tuple[_ToIndex, ...]

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

_ConvertibleToInt: TypeAlias = CanInt | CanIndex | _CharLike_co
_ConvertibleToFloat: TypeAlias = CanFloat | CanIndex | _CharLike_co
_ConvertibleToComplex: TypeAlias = complex | CanComplex | CanFloat | CanIndex | _CharLike_co
_ConvertibleToTD64: TypeAlias = dt.timedelta | int | _CharLike_co | character | number | timedelta64 | bool_ | None
_ConvertibleToDT64: TypeAlias = dt.date | int | _CharLike_co | character | number | datetime64 | bool_ | None

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

_BinOperandComplex128_co: TypeAlias = complex | floating[_64Bit] | integer[_64Bit] | integer[_32Bit]
_ToReal: TypeAlias = float | CanComplex | CanFloat | CanIndex
_ToImag: TypeAlias = float | CanFloat | CanIndex

_DTypeDescr: TypeAlias = (
    list[tuple[str, str]] | list[tuple[str, str, tuple[int, ...]]] | list[tuple[str, str] | tuple[str, str, tuple[int, ...]]]
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
    def base(self) -> dtype[Any]: ...
    @property
    def byteorder(self) -> _ByteOrderChar: ...
    @property
    def char(self) -> _DTypeChar: ...
    @property
    def descr(self) -> _DTypeDescr: ...
    @property
    def fields(self) -> MappingProxyType[LiteralString, tuple[dtype[Any], int] | tuple[dtype[Any], int, Any]] | None: ...
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
    def subdtype(self) -> tuple[dtype[Any], tuple[int, ...]] | None: ...

    # `None` results in the default dtype
    @overload
    def __new__(
        cls,
        dtype: type[float64] | None,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float64]: ...

    # Overload for `dtype` instances, scalar types, and instances that have a
    # `dtype: dtype[_SCT]` attribute
    @overload
    def __new__(  # type: ignore[overload-overlap]
        cls,
        dtype: _DTypeLike[_ScalarT],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        dtype: type[py_bool | bool_ | ct.c_bool] | _BoolCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[bool_]: ...
    # NOTE: `_: type[int]` also accepts `type[int | bool]`
    @overload
    def __new__(
        cls,
        dtype: type[int | int_ | bool_],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[int_ | bool_]: ...
    @overload  # NOTE: `_: type[float]` also accepts `type[float64 | int | bool]`
    def __new__(
        cls,
        dtype: type[float | int_ | bool_] | None,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float64 | int_ | bool_]: ...
    @overload  # NOTE: `_: type[complex]` also accepts `type[complex128 | float64 | float | ...]`
    def __new__(
        cls,
        dtype: type[complex | int_ | bool_],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complex128 | float64 | int_ | bool_]: ...
    @overload
    def __new__(
        cls,
        dtype: type[bytes | ct.c_char] | _BytesCodes,  # also includes `type[bytes_]`
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[bytes_]: ...
    @overload
    def __new__(
        cls,
        dtype: type[str] | _StrCodes,  # also includes `type[str_]`
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[str_]: ...
    # NOTE: These `memoryview` overloads assume PEP 688, which requires mypy to be run with the `--strict-bytes` flag..
    # Pyright / Pylance requires setting `disableBytesTypePromotions=true` if not in strict mode.
    @overload
    def __new__(
        cls,
        dtype: type[memoryview | void] | _VoidCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[void]: ...
    @overload
    def __new__(
        cls,
        dtype: type[_BuiltinObjectLike | object_ | ct.py_object[Any]] | _ObjectCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[object_]: ...
    @overload  # Unions of builtins.
    def __new__(
        cls,
        dtype: type[bytes | str],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[character]: ...
    @overload
    def __new__(
        cls,
        dtype: type[bytes | str | memoryview],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[flexible]: ...
    @overload
    def __new__(
        cls,
        dtype: type[complex | bytes | str | memoryview | _BuiltinObjectLike],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[bool_ | int_ | float64 | complex128 | flexible | object_]: ...
    @overload  # `unsignedinteger` string-based representations and ctypes
    def __new__(
        cls,
        dtype: _UInt8Codes | type[ct.c_uint8 | ct.c_ubyte],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[uint8]: ...
    @overload
    def __new__(
        cls,
        dtype: _UInt16Codes | type[ct.c_uint16 | ct.c_ushort],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[uint16]: ...
    @overload
    def __new__(
        cls,
        dtype: _UInt32Codes | type[ct.c_uint32 | ct.c_uint],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[uint32]: ...
    @overload
    def __new__(
        cls,
        dtype: _UInt64Codes | type[ct.c_uint64],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[uint64]: ...
    @overload  # NOTE: This assumes `uint_ptr_t == size_t`, which almost always holds
    def __new__(
        cls,
        dtype: type[ct.c_void_p | ct.c_size_t] | _UIntPCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[uintp]: ...
    @overload
    def __new__(
        cls,
        dtype: _ULongCodes | type[ct.c_ulong],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[ulong]: ...
    @overload
    def __new__(
        cls,
        dtype: _ULongLongCodes | type[ct.c_ulonglong],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[ulonglong]: ...
    @overload  # `signedinteger` string-based representations and ctypes
    def __new__(
        cls,
        dtype: _Int8Codes | type[ct.c_int8 | ct.c_byte],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[int8]: ...
    @overload
    def __new__(
        cls,
        dtype: _Int16Codes | type[ct.c_int16 | ct.c_short],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[int16]: ...
    @overload
    def __new__(
        cls,
        dtype: _Int32Codes | type[ct.c_int32 | ct.c_int],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[int32]: ...
    @overload
    def __new__(
        cls,
        dtype: _Int64Codes | type[ct.c_int64],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[int64]: ...
    @overload
    def __new__(
        cls,
        dtype: _IntPCodes | type[ct.c_ssize_t],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[intp]: ...
    @overload
    def __new__(
        cls,
        dtype: _LongCodes | type[ct.c_long],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[long]: ...
    @overload
    def __new__(
        cls,
        dtype: _LongLongCodes | type[ct.c_longlong],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[longlong]: ...
    @overload  # `floating` string-based representations and ctypes
    def __new__(
        cls,
        dtype: _Float16Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float16]: ...
    @overload
    def __new__(
        cls,
        dtype: _Float32Codes | type[ct.c_float],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float32]: ...
    @overload
    def __new__(
        cls,
        dtype: _Float64Codes | type[ct.c_double],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float64]: ...
    @overload
    def __new__(
        cls,
        dtype: _Float96Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float96]: ...
    @overload
    def __new__(
        cls,
        dtype: _Float128Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[float128]: ...
    @overload
    def __new__(
        cls,
        dtype: _LongDoubleCodes | type[ct.c_longdouble],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[longdouble]: ...
    @overload  # `complexfloating` string-based representations
    def __new__(
        cls,
        dtype: _Complex64Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complex64]: ...
    @overload
    def __new__(
        cls,
        dtype: _Complex128Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complex128]: ...
    @overload
    def __new__(
        cls,
        dtype: _Complex192Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complex192]: ...
    @overload
    def __new__(
        cls,
        dtype: _Complex256Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complex256]: ...
    @overload
    def __new__(
        cls,
        dtype: _CLongDoubleCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[clongdouble]: ...
    @overload  # miscellaneous string-based representations and ctypes
    def __new__(
        cls,
        dtype: _TD64Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[timedelta64]: ...
    @overload
    def __new__(
        cls,
        dtype: _DT64Codes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[datetime64]: ...
    @overload
    def __new__(
        cls,
        dtype: _VoidDTypeLike,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[void]: ...
    @overload  # `StringDType` requires special treatment because it has no scalar type
    def __new__(
        cls,
        dtype: dtypes.StringDType | _StringCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtypes.StringDType: ...
    @overload  # combined char-codes and ctypes, analogous to the scalar-type hierarchy
    def __new__(
        cls,
        dtype: _UnsignedIntegerCodes | _UnsignedIntegerCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[unsignedinteger]: ...
    @overload
    def __new__(
        cls,
        dtype: _SignedIntegerCodes | _SignedIntegerCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[signedinteger]: ...
    @overload
    def __new__(
        cls,
        dtype: _IntegerCodes | _IntegerCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[integer]: ...
    @overload
    def __new__(
        cls,
        dtype: _FloatingCodes | _FloatingCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[floating]: ...
    @overload
    def __new__(
        cls,
        dtype: _ComplexFloatingCodes,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[complexfloating]: ...
    @overload
    def __new__(
        cls,
        dtype: _InexactCodes | _FloatingCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[inexact]: ...
    @overload
    def __new__(
        cls,
        dtype: _NumberCodes | _NumberCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[number]: ...
    @overload
    def __new__(
        cls,
        dtype: _CharacterCodes | type[ct.c_char],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[character]: ...
    @overload
    def __new__(
        cls,
        dtype: _FlexibleCodes | type[ct.c_char],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[flexible]: ...
    @overload
    def __new__(
        cls,
        dtype: _GenericCodes | _GenericCType,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[generic]: ...
    @overload  # handle strings that can't be expressed as literals; i.e. "S9", "m8[3s]", ...
    def __new__(
        cls,
        dtype: bytes | str,
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[Any]: ...
    @overload
    def __new__(
        cls,
        dtype: type[object],
        align: py_bool = False,
        copy: py_bool = False,
        metadata: dict[str, Any] = ...,
    ) -> dtype[object_ | Any]: ...

    #
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

    #
    def __hash__(self, /) -> int: ...

    # Explicitly defined `__eq__` and `__ne__` to get around mypy's `strict_equality` option; even though their signatures are
    # identical to their `object`-based counterpart
    def __eq__(self, other: object, /) -> py_bool: ...
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
    # Set the return-type to `dtype[Any]` for now for non-flexible dtypes.
    @overload
    def __rmul__(self: _FlexDTypeT, value: CanIndex, /) -> _FlexDTypeT: ...
    @overload
    def __rmul__(self, value: CanIndex, /) -> dtype[Any]: ...

    #
    @overload
    def __getitem__(self: dtype[void], key: list[str], /) -> dtype[void]: ...
    @overload
    def __getitem__(self: dtype[void], key: str | CanIndex, /) -> dtype[Any]: ...

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

    if sys.version_info >= (3, 12):
        def __buffer__(self, flags: int, /) -> memoryview: ...

    #
    @property
    def __array_interface__(self) -> dict[str, Any]: ...
    @property
    def __array_priority__(self) -> float: ...
    @property
    def __array_struct__(self) -> CapsuleType: ...  # builtins.PyCapsule

    #
    def __bool__(self, /) -> py_bool: ...
    def __int__(self, /) -> int: ...
    def __float__(self, /) -> float: ...

    #
    def __eq__(self, other: object, /) -> Any: ...
    def __ne__(self, other: object, /) -> Any: ...

    #
    def __setstate__(self, state: tuple[CanIndex, _ShapeLike, _DTypeT_co, bool_, bytes | list[Any]], /) -> None: ...

    #
    def copy(self, order: _OrderKACF = ...) -> Self: ...
    def __copy__(self) -> Self: ...
    def __deepcopy__(self, memo: dict[int, Any] | None, /) -> Self: ...

    #
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
    def put(self, /, indices: _ArrayLikeInt_co, values: ArrayLike, mode: _ModeKind = "raise") -> None: ...

    # NOTE: even on `generic` this seems to work
    def setflags(self, /, write: py_bool | None = None, align: py_bool | None = None, uic: py_bool | None = None) -> None: ...

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
        where: _ArrayLikeBool_co = True,
    ) -> Any: ...
    @overload
    def max(
        self,
        /,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
    ) -> Any: ...
    @overload
    def min(
        self,
        /,
        axis: _ShapeLike | None,
        out: _ArrayT,
        keepdims: py_bool = False,
        initial: _NumberLike_co = ...,
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
    def clip(self, /, min: ArrayLike, max: ArrayLike | None = None, out: None = None, **kwargs: object) -> NDArray[Any]: ...
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
    def compress(self, /, condition: _ArrayLikeInt_co, axis: CanIndex | None = None, out: None = None) -> NDArray[Any]: ...
    @overload
    def compress(self, /, condition: _ArrayLikeInt_co, axis: CanIndex | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def compress(self, /, condition: _ArrayLikeInt_co, axis: CanIndex | None = None, *, out: _ArrayT) -> _ArrayT: ...

    #
    @overload  # out: None (default)
    def cumprod(self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> NDArray[Any]: ...
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
    ) -> _ArrayT: ...

    #
    @overload  # out: None (default)
    def cumsum(self, /, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None) -> NDArray[Any]: ...
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
        where: _ArrayLikeBool_co = True,
        mean: _ArrayLikeNumber_co = ...,
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
    def real(self: _HasDTypeWithReal[_ScalarT], /) -> ndarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @real.setter
    def real(self, value: ArrayLike, /) -> None: ...

    #
    @property
    def imag(self: _HasDTypeWithImag[_ScalarT], /) -> ndarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @imag.setter
    def imag(self, value: ArrayLike, /) -> None: ...

    #
    @property
    def flat(self) -> flatiter[Self]: ...

    #
    @property
    def ctypes(self) -> _ctypes[int]: ...

    #
    def __new__(
        cls,
        shape: _ShapeLike,
        dtype: DTypeLike = float,  # noqa: PYI011
        buffer: _SupportsBuffer | None = None,
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
    def __array_ufunc__(self, ufunc: ufunc, method: _UFuncMethod, /, *inputs: object, **kwargs: object) -> Any: ...

    #
    def __array_function__(
        self,
        /,
        func: Callable[..., Any],
        types: Iterable[type],
        args: Iterable[Any],
        kwargs: Mapping[str, Any],
    ) -> Any: ...

    #
    def __array_wrap__(
        self,
        array: ndarray[_ShapeT, _DTypeT],
        context: tuple[ufunc, tuple[object, ...], int] | None = ...,
        return_scalar: py_bool = ...,
        /,
    ) -> ndarray[_ShapeT, _DTypeT]: ...

    #
    def __array_finalize__(self, obj: NDArray[Any] | Any, /) -> None: ...

    #
    @overload
    def __getitem__(self, key: _ArrayInt_co | tuple[_ArrayInt_co, ...], /) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def __getitem__(self, key: CanIndex | tuple[CanIndex, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndices, /) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def __getitem__(self: NDArray[void], key: str, /) -> ndarray[_ShapeT_co, dtype[Any]]: ...
    @overload
    def __getitem__(self: NDArray[void], key: list[str], /) -> ndarray[_ShapeT_co, dtype[void]]: ...

    #
    @overload  # flexible | object_ | bool
    def __setitem__(
        self: ndarray[Any, dtype[flexible | object_ | bool_] | dtypes.StringDType],
        key: _ToIndices,
        value: object,
        /,
    ) -> None: ...
    @overload  # integer
    def __setitem__(
        self: NDArray[integer],
        key: _ToIndices,
        value: _ConvertibleToInt | _NestedSequence[_ConvertibleToInt] | _ArrayLikeInt_co,
        /,
    ) -> None: ...
    @overload  # floating
    def __setitem__(
        self: NDArray[floating],
        key: _ToIndices,
        value: _ConvertibleToFloat | _NestedSequence[_ConvertibleToFloat | None] | _ArrayLikeFloat_co | None,
        /,
    ) -> None: ...
    @overload  # complexfloating
    def __setitem__(
        self: NDArray[complexfloating],
        key: _ToIndices,
        value: _ConvertibleToComplex | _NestedSequence[_ConvertibleToComplex | None] | _ArrayLikeNumber_co | None,
        /,
    ) -> None: ...
    @overload  # timedelta64
    def __setitem__(
        self: NDArray[timedelta64],
        key: _ToIndices,
        value: _ConvertibleToTD64 | _NestedSequence[_ConvertibleToTD64],
        /,
    ) -> None: ...
    @overload  # datetime64
    def __setitem__(
        self: NDArray[datetime64],
        key: _ToIndices,
        value: _ConvertibleToDT64 | _NestedSequence[_ConvertibleToDT64],
        /,
    ) -> None: ...
    @overload  # void
    def __setitem__(self: NDArray[void], key: str | list[str], value: object, /) -> None: ...
    @overload  # catch-all
    def __setitem__(self, key: _ToIndices, value: ArrayLike, /) -> None: ...

    #
    def __complex__(self: NDArray[number | bool_ | object_], /) -> complex: ...
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
    def __iter__(self: ndarray[tuple[int, int, Unpack[tuple[int, ...]]], dtype[_ScalarT]], /) -> Iterator[NDArray[_ScalarT]]: ...
    @overload  # ?-d
    def __iter__(self, /) -> Iterator[Any]: ...

    # The last overload is for catching recursive objects whose
    # nesting is too deep.
    # The first overload is for catching `bytes` (as they are a subtype of
    # `Sequence[int]`) and `str`. As `str` is a recursive sequence of
    # strings, it will pass through the final overload otherwise

    @overload
    def __lt__(self: _ArrayComplex_co, other: _ArrayLikeNumber_co, /) -> NDArray[bool_]: ...
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
    def __le__(self: _ArrayComplex_co, other: _ArrayLikeNumber_co, /) -> NDArray[bool_]: ...
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
    def __gt__(self: _ArrayComplex_co, other: _ArrayLikeNumber_co, /) -> NDArray[bool_]: ...
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
    def __ge__(self: _ArrayComplex_co, other: _ArrayLikeNumber_co, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: _ArrayTD64_co, other: _ArrayLikeTD64_co, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: NDArray[datetime64], other: _ArrayLikeDT64_co, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self: NDArray[object_], other: object, /) -> NDArray[bool_]: ...
    @overload
    def __ge__(self, other: _ArrayLikeObject_co, /) -> NDArray[bool_]: ...

    # Unary ops

    @overload
    def __abs__(
        self: ndarray[_ShapeT, dtype[complexfloating[_AnyNBitInexact]]],
        /,
    ) -> ndarray[_ShapeT, dtype[floating[_AnyNBitInexact]]]: ...
    @overload
    def __abs__(self: _RealArrayT, /) -> _RealArrayT: ...

    #
    def __invert__(self: _IntegralArrayT, /) -> _IntegralArrayT: ...  # noqa: PYI019
    def __neg__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019
    def __pos__(self: _NumericArrayT, /) -> _NumericArrayT: ...  # noqa: PYI019

    # Binary ops

    #
    @overload
    def __add__(self: NDArray[_NumberT], rhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __add__(self: NDArray[_NumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __add__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __add__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __add__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __add__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __add__(self: NDArray[complexfloating[_64Bit]], rhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __add__(self: _ArrayComplex128_co, rhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __add__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __add__(self: _ArrayLikeUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __add__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __add__(self: _ArrayLikeInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __add__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __add__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __add__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __add__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __add__(self: NDArray[bool_ | number], rhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __add__(self: NDArray[timedelta64], rhs: _ArrayLikeTD64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __add__(self: _ArrayTD64_co, rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __add__(self: _ArrayTD64_co, rhs: _ArrayLikeDT64_co, /) -> NDArray[datetime64]: ...
    @overload
    def __add__(self: NDArray[datetime64], rhs: _ArrayLikeTD64_co, /) -> NDArray[datetime64]: ...
    @overload
    def __add__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __add__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __add__
    @overload
    def __radd__(self: NDArray[_NumberT], lhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...  # type: ignore[misc]
    @overload
    def __radd__(self: NDArray[_NumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __radd__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __radd__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __radd__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __radd__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __radd__(self: NDArray[complexfloating[_64Bit]], lhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __radd__(self: _ArrayComplex128_co, lhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __radd__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __radd__(self: _ArrayLikeUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __radd__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __radd__(self: _ArrayLikeInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __radd__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __radd__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __radd__(self: NDArray[complexfloating], lhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __radd__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __radd__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __radd__(self: NDArray[timedelta64], lhs: _ArrayLikeTD64_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __radd__(self: _ArrayTD64_co, lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __radd__(self: _ArrayTD64_co, lhs: _ArrayLikeDT64_co, /) -> NDArray[datetime64]: ...
    @overload
    def __radd__(self: NDArray[datetime64], lhs: _ArrayLikeTD64_co, /) -> NDArray[datetime64]: ...
    @overload
    def __radd__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __radd__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __iadd__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: NDArray[datetime64 | timedelta64], rhs: _ArrayLikeTD64_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __sub__(self: NDArray[_NumberT], rhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __sub__(self: NDArray[_NumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __sub__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __sub__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> Never: ...
    @overload
    def __sub__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __sub__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __sub__(self: NDArray[complexfloating[_64Bit]], rhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __sub__(self: _ArrayComplex128_co, rhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __sub__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __sub__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: NDArray[integer], rhs: _NestedSequence[int], /) -> NDArray[signedinteger]: ...
    @overload
    def __sub__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __sub__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __sub__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __sub__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __sub__(self: NDArray[bool_ | number], rhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
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
    def __rsub__(self: NDArray[_NumberT], lhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...  # type: ignore[misc]
    @overload
    def __rsub__(self: NDArray[_NumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __rsub__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rsub__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> Never: ...
    @overload
    def __rsub__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rsub__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rsub__(self: NDArray[complexfloating[_64Bit]], lhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __rsub__(self: _ArrayComplex128_co, lhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __rsub__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rsub__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: NDArray[integer], lhs: _NestedSequence[int], /) -> NDArray[signedinteger]: ...
    @overload
    def __rsub__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rsub__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rsub__(self: NDArray[complexfloating], lhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __rsub__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __rsub__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
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
    def __isub__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[datetime64 | timedelta64], rhs: _ArrayLikeTD64_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mul__(self: NDArray[_NumberT], rhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __mul__(self: NDArray[_NumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __mul__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __mul__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __mul__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __mul__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __mul__(self: NDArray[complexfloating[_64Bit]], rhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __mul__(self: _ArrayComplex128_co, rhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __mul__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mul__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mul__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __mul__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __mul__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __mul__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __mul__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __mul__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __mul__(self: NDArray[bool_ | number], rhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __mul__(self: NDArray[timedelta64], rhs: _ArrayLikeFloat_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __mul__(self: _ArrayFloat_co, rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __mul__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __mul__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __mul__
    @overload
    def __rmul__(self: NDArray[_NumberT], lhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...  # type: ignore[misc]
    @overload
    def __rmul__(self: NDArray[_NumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __rmul__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rmul__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __rmul__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rmul__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rmul__(self: NDArray[complexfloating[_64Bit]], lhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __rmul__(self: _ArrayComplex128_co, lhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __rmul__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmul__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmul__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmul__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __rmul__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rmul__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rmul__(self: NDArray[complexfloating], lhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmul__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __rmul__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __rmul__(self: NDArray[timedelta64], lhs: _ArrayLikeFloat_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __rmul__(self: _ArrayFloat_co, lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rmul__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmul__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imul__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[floating | timedelta64], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    # TODO(jorenham): Support the "1d @ 1d -> scalar" case
    # https://github.com/numpy/numtype/issues/197
    @overload
    def __matmul__(self: NDArray[_NumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __matmul__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __matmul__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __matmul__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __matmul__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __matmul__(self: NDArray[complexfloating[_64Bit]], rhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __matmul__(self: _ArrayComplex128_co, rhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __matmul__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __matmul__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __matmul__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __matmul__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __matmul__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __matmul__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __matmul__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __matmul__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __matmul__(self: NDArray[bool_ | number], rhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __matmul__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __matmul__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __matmul__
    @overload
    def __rmatmul__(self: NDArray[_NumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_NumberT]: ...
    @overload
    def __rmatmul__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], /) -> NDArray[_NumberT]: ...
    @overload
    def __rmatmul__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __rmatmul__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rmatmul__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rmatmul__(self: NDArray[complexfloating[_64Bit]], lhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __rmatmul__(self: _ArrayComplex128_co, lhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __rmatmul__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmatmul__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmatmul__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmatmul__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __rmatmul__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rmatmul__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rmatmul__(self: NDArray[complexfloating], lhs: _ArrayLikeComplex_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __rmatmul__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __rmatmul__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __rmatmul__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmatmul__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imatmul__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imatmul__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __truediv__(self: _ArrayInt_co, rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: _ArrayFloat64_co, rhs: _ArrayLikeInt_co | _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: NDArray[complexfloating[_64Bit]], rhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __truediv__(self: _ArrayComplex128_co, rhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __truediv__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __truediv__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __truediv__(self: NDArray[complexfloating], rhs: _ArrayLikeNumber_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __truediv__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __truediv__(self: NDArray[inexact], rhs: _ArrayLikeNumber_co, /) -> NDArray[inexact]: ...
    @overload
    def __truediv__(self: NDArray[number], rhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[float64]: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _ArrayLikeBool_co, /) -> Never: ...
    @overload
    def __truediv__(self: NDArray[timedelta64], rhs: _ArrayLikeFloat_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __truediv__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __truediv__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rtruediv__(self: _ArrayInt_co, lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rtruediv__(self: _ArrayFloat64_co, lhs: _ArrayLikeInt_co | _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rtruediv__(self: NDArray[complexfloating[_64Bit]], lhs: _ArrayLikeComplex128_co, /) -> NDArray[complex128]: ...
    @overload
    def __rtruediv__(self: _ArrayComplex128_co, lhs: _ArrayLike[complexfloating[_64Bit]], /) -> NDArray[complex128]: ...
    @overload
    def __rtruediv__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rtruediv__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rtruediv__(self: NDArray[complexfloating], lhs: _ArrayLikeNumber_co, /) -> NDArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], /) -> NDArray[complexfloating]: ...
    @overload
    def __rtruediv__(self: NDArray[inexact], lhs: _ArrayLikeNumber_co, /) -> NDArray[inexact]: ...
    @overload
    def __rtruediv__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, /) -> NDArray[Incomplete]: ...
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
    def __itruediv__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[timedelta64], rhs: _ArrayLikeInt, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    # the pyright error appears to be a false positive
    @overload
    def __floordiv__(self: NDArray[_RealNumberT], rhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_RealNumberT]]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __floordiv__(self: NDArray[_RealNumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __floordiv__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __floordiv__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __floordiv__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __floordiv__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __floordiv__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __floordiv__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __floordiv__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __floordiv__(self: NDArray[floating | integer], rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __floordiv__(self: _ArrayLikeFloat_co, rhs: _ArrayLikeFloat_co, /) -> NDArray[Incomplete]: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[int64]: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _ArrayLikeBool_co, /) -> Never: ...
    @overload
    def __floordiv__(self: NDArray[timedelta64], rhs: _ArrayLikeFloat_co, /) -> NDArray[timedelta64]: ...
    @overload
    def __floordiv__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __floordiv__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rfloordiv__(self: NDArray[_RealNumberT], lhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_RealNumberT]]: ...  # type: ignore[overload-overlap, misc]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rfloordiv__(self: NDArray[_RealNumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rfloordiv__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rfloordiv__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rfloordiv__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rfloordiv__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rfloordiv__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rfloordiv__(self: NDArray[floating | integer], lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rfloordiv__(self: _ArrayLikeFloat_co, lhs: _ArrayLikeFloat_co, /) -> NDArray[Incomplete]: ...
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
    def __ifloordiv__(self: NDArray[integer | timedelta64], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __mod__(self: NDArray[_RealNumberT], rhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_RealNumberT]]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __mod__(self: NDArray[_RealNumberT], rhs: _ArrayLikeBool_co, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __mod__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __mod__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __mod__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mod__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __mod__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __mod__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __mod__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __mod__(self: NDArray[floating | integer], rhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __mod__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __mod__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __mod__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    # keep in sync with __mod__
    @overload
    def __rmod__(self: NDArray[_RealNumberT], lhs: int | bool_, /) -> ndarray[_ShapeT_co, dtype[_RealNumberT]]: ...  # type: ignore[overload-overlap, misc]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rmod__(self: NDArray[_RealNumberT], lhs: _ArrayLikeBool_co, /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmod__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> NDArray[_RealNumberT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rmod__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __rmod__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> NDArray[float64]: ...
    @overload
    def __rmod__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> NDArray[float64]: ...
    @overload
    def __rmod__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmod__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rmod__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rmod__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> NDArray[signedinteger]: ...
    @overload
    def __rmod__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> NDArray[floating]: ...
    @overload
    def __rmod__(self: NDArray[floating | integer], lhs: _ArrayLike[floating], /) -> NDArray[floating]: ...
    @overload
    def __rmod__(self: NDArray[timedelta64], lhs: _ArrayLike[timedelta64], /) -> NDArray[timedelta64]: ...
    @overload
    def __rmod__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rmod__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __imod__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[timedelta64], rhs: _ArrayLike[timedelta64], /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imod__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __divmod__(self: NDArray[_RealNumberT], rhs: int | bool_, /) -> _2Tuple[ndarray[_ShapeT_co, dtype[_RealNumberT]]]: ...  # type: ignore[overload-overlap]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __divmod__(self: NDArray[_RealNumberT], rhs: _ArrayLikeBool_co, /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __divmod__(self: NDArray[bool_], rhs: _ArrayLike[_RealNumberT], /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __divmod__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> _2Tuple[NDArray[int8]]: ...
    @overload
    def __divmod__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __divmod__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __divmod__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __divmod__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __divmod__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __divmod__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __divmod__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __divmod__(self: NDArray[floating | integer], rhs: _ArrayLike[floating], /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __divmod__(
        self: NDArray[timedelta64],
        rhs: _ArrayLike[timedelta64],
        /,
    ) -> tuple[NDArray[int64], NDArray[timedelta64]]: ...

    # keep in sync with __divmod__
    @overload
    def __rdivmod__(self: NDArray[_RealNumberT], lhs: int | bool_, /) -> _2Tuple[ndarray[_ShapeT_co, dtype[_RealNumberT]]]: ...  # type: ignore[overload-overlap, misc]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rdivmod__(self: NDArray[_RealNumberT], lhs: _ArrayLikeBool_co, /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self: NDArray[bool_], lhs: _ArrayLike[_RealNumberT], /) -> _2Tuple[NDArray[_RealNumberT]]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> _2Tuple[NDArray[int8]]: ...
    @overload
    def __rdivmod__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __rdivmod__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], /) -> _2Tuple[NDArray[float64]]: ...
    @overload
    def __rdivmod__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __rdivmod__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], /) -> _2Tuple[NDArray[unsignedinteger]]: ...
    @overload
    def __rdivmod__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __rdivmod__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], /) -> _2Tuple[NDArray[signedinteger]]: ...
    @overload
    def __rdivmod__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __rdivmod__(self: NDArray[floating | integer], lhs: _ArrayLike[floating], /) -> _2Tuple[NDArray[floating]]: ...
    @overload
    def __rdivmod__(
        self: NDArray[timedelta64],
        lhs: _ArrayLike[timedelta64],
        /,
    ) -> tuple[NDArray[int64], NDArray[timedelta64]]: ...

    #
    @overload
    def __pow__(self: NDArray[_NumberT], rhs: int | bool_, mod: None = None, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __pow__(self: NDArray[_NumberT], rhs: _ArrayLikeBool_co, mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __pow__(self: NDArray[bool_], rhs: _ArrayLike[_NumberT], mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __pow__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, mod: None = None, /) -> NDArray[int8]: ...
    @overload
    def __pow__(self: NDArray[floating[_64Bit]], rhs: _ArrayLikeFloat64_co, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __pow__(self: _ArrayFloat64_co, rhs: _ArrayLike[floating[_64Bit]], mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __pow__(
        self: NDArray[complexfloating[_64Bit]],
        rhs: _ArrayLikeComplex128_co,
        mod: None = None,
        /,
    ) -> NDArray[complex128]: ...
    @overload
    def __pow__(
        self: _ArrayComplex128_co,
        rhs: _ArrayLike[complexfloating[_64Bit]],
        mod: None = None,
        /,
    ) -> NDArray[complex128]: ...
    @overload
    def __pow__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __pow__(self: _ArrayUInt_co, rhs: _ArrayLike[unsignedinteger], mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __pow__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __pow__(self: _ArrayInt_co, rhs: _ArrayLike[signedinteger], mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __pow__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __pow__(self: _ArrayFloat_co, rhs: _ArrayLike[floating], mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __pow__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __pow__(self: _ArrayComplex_co, rhs: _ArrayLike[complexfloating], mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __pow__(self: NDArray[bool_ | number], rhs: _ArrayLikeNumber_co, mod: None = None, /) -> NDArray[Incomplete]: ...
    @overload
    def __pow__(self: NDArray[object_], rhs: object, mod: None = None, /) -> NDArray[object_]: ...
    @overload
    def __pow__(self, rhs: _ArrayLikeObject_co, mod: None = None, /) -> NDArray[object_]: ...

    #
    @overload
    def __rpow__(self: NDArray[_NumberT], lhs: int | bool_, mod: None = None, /) -> ndarray[_ShapeT_co, dtype[_NumberT]]: ...
    @overload
    def __rpow__(self: NDArray[_NumberT], lhs: _ArrayLikeBool_co, mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __rpow__(self: NDArray[bool_], lhs: _ArrayLike[_NumberT], mod: None = None, /) -> NDArray[_NumberT]: ...
    @overload
    def __rpow__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, mod: None = None, /) -> NDArray[int8]: ...
    @overload
    def __rpow__(self: NDArray[floating[_64Bit]], lhs: _ArrayLikeFloat64_co, mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __rpow__(self: _ArrayFloat64_co, lhs: _ArrayLike[floating[_64Bit]], mod: None = None, /) -> NDArray[float64]: ...
    @overload
    def __rpow__(
        self: NDArray[complexfloating[_64Bit]],
        lhs: _ArrayLikeComplex128_co,
        mod: None = None,
        /,
    ) -> NDArray[complex128]: ...
    @overload
    def __rpow__(
        self: _ArrayComplex128_co,
        lhs: _ArrayLike[complexfloating[_64Bit]],
        mod: None = None,
        /,
    ) -> NDArray[complex128]: ...
    @overload
    def __rpow__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rpow__(self: _ArrayUInt_co, lhs: _ArrayLike[unsignedinteger], mod: None = None, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rpow__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __rpow__(self: _ArrayInt_co, lhs: _ArrayLike[signedinteger], mod: None = None, /) -> NDArray[signedinteger]: ...
    @overload
    def __rpow__(self: NDArray[floating], lhs: _ArrayLikeFloat_co, mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __rpow__(self: _ArrayFloat_co, lhs: _ArrayLike[floating], mod: None = None, /) -> NDArray[floating]: ...
    @overload
    def __rpow__(self: NDArray[complexfloating], lhs: _ArrayLikeComplex_co, mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __rpow__(self: _ArrayComplex_co, lhs: _ArrayLike[complexfloating], mod: None = None, /) -> NDArray[complexfloating]: ...
    @overload
    def __rpow__(self: NDArray[bool_ | number], lhs: _ArrayLikeNumber_co, mod: None = None, /) -> NDArray[Incomplete]: ...
    @overload
    def __rpow__(self: NDArray[object_], lhs: object, mod: None = None, /) -> NDArray[object_]: ...
    @overload
    def __rpow__(self, lhs: _ArrayLikeObject_co, mod: None = None, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ipow__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[floating], rhs: _ArrayLikeFloat_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[complexfloating], rhs: _ArrayLikeComplex_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __lshift__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __lshift__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __lshift__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __lshift__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __lshift__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __lshift__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rlshift__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __rlshift__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rlshift__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rlshift__(self: NDArray[integer], lhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __rlshift__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rlshift__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ilshift__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ilshift__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __rshift__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __rshift__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rshift__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rshift__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __rshift__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rshift__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rrshift__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[int8]: ...
    @overload
    def __rrshift__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rrshift__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rrshift__(self: NDArray[integer], lhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __rrshift__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rrshift__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __irshift__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __irshift__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __and__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __and__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __and__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __and__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __and__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __and__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rand__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __rand__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rand__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rand__(self: NDArray[integer], lhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __rand__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rand__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __iand__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iand__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __xor__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __xor__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __xor__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __xor__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __xor__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __xor__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __rxor__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __rxor__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __rxor__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __rxor__(self: NDArray[integer], lhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __rxor__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __rxor__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ixor__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ixor__(self: NDArray[object_], rhs: object, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    @overload
    def __or__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __or__(self: NDArray[unsignedinteger], rhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __or__(self: NDArray[signedinteger], rhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __or__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __or__(self: NDArray[object_], rhs: object, /) -> NDArray[object_]: ...
    @overload
    def __or__(self, rhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload
    def __ror__(self: NDArray[bool_], lhs: _ArrayLikeBool_co, /) -> NDArray[bool_]: ...
    @overload
    def __ror__(self: NDArray[unsignedinteger], lhs: _ArrayLikeUInt_co, /) -> NDArray[unsignedinteger]: ...
    @overload
    def __ror__(self: NDArray[signedinteger], lhs: _ArrayLikeInt_co, /) -> NDArray[signedinteger]: ...
    @overload
    def __ror__(self: NDArray[integer], lhs: _ArrayLikeInt_co, /) -> NDArray[integer]: ...
    @overload
    def __ror__(self: NDArray[object_], lhs: object, /) -> NDArray[object_]: ...
    @overload
    def __ror__(self, lhs: _ArrayLikeObject_co, /) -> NDArray[object_]: ...

    #
    @overload  # type: ignore[misc]
    def __ior__(self: NDArray[bool_], rhs: _ArrayLikeBool_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ior__(self: NDArray[integer], rhs: _ArrayLikeInt_co, /) -> ndarray[_ShapeT_co, _DTypeT_co]: ...
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
    def resize(self: ndarray[tuple[int, int], Any], n0: CanIndex, n1: CanIndex, /, *, refcheck: py_bool = True) -> None: ...
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
    def swapaxes(self: ndarray[_AnyShapeT, _DTypeT], /, axis1: CanIndex, axis2: CanIndex) -> ndarray[_AnyShapeT, _DTypeT]: ...
    def squeeze(self, /, axis: CanIndex | tuple[CanIndex, ...] | None = None) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
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
        where: _ArrayLikeBool_co = True,
    ) -> bool_: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _ArrayLikeBool_co = True,
    ) -> bool_ | NDArray[bool_]: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None,
        out: _ArrayT,
        keepdims: CanIndex = False,
        *,
        where: _ArrayLikeBool_co = True,
    ) -> _ArrayT: ...
    @overload
    def all(
        self,
        /,
        axis: int | tuple[int, ...] | None = None,
        *,
        out: _ArrayT,
        keepdims: CanIndex = False,
        where: _ArrayLikeBool_co = True,
    ) -> _ArrayT: ...

    #
    @overload
    def any(
        self,
        axis: None = None,
        out: None = None,
        keepdims: L[False, 0] = False,
        *,
        where: _ArrayLikeBool_co = True,
    ) -> bool_: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: _ArrayLikeBool_co = True,
    ) -> bool_ | NDArray[bool_]: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None,
        out: _ArrayT,
        keepdims: CanIndex = False,
        *,
        where: _ArrayLikeBool_co = True,
    ) -> _ArrayT: ...
    @overload
    def any(
        self,
        axis: int | tuple[int, ...] | None = None,
        *,
        out: _ArrayT,
        keepdims: CanIndex = False,
        where: _ArrayLikeBool_co = True,
    ) -> _ArrayT: ...

    #
    def argpartition(
        self,
        kth: _ArrayLikeInt_co,
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
        sorter: _ArrayLikeInt_co | None = None,
    ) -> intp: ...
    @overload
    def searchsorted(
        self,
        /,
        v: ndarray[_ShapeT, Any],
        side: _SortSide = "left",
        sorter: _ArrayLikeInt_co | None = None,
    ) -> ndarray[_ShapeT, dtype[intp]]: ...
    @overload
    def searchsorted(
        self,
        /,
        v: _NestedSequence[_ScalarLike_co],
        side: _SortSide = "left",
        sorter: _ArrayLikeInt_co | None = None,
    ) -> NDArray[intp]: ...
    @overload
    def searchsorted(
        self,
        /,
        v: ArrayLike,
        side: _SortSide = "left",
        sorter: _ArrayLikeInt_co | None = None,
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
    ) -> ndarray[tuple[int], dtype[intp]]: ...
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
    ) -> ndarray[tuple[int], dtype[intp]]: ...

    #
    @overload
    def partition(
        self,
        /,
        kth: _ArrayLikeInt_co,
        axis: CanIndex = -1,
        kind: _PartitionKind = "introselect",
        order: None = None,
    ) -> None: ...
    @overload
    def partition(
        self: ndarray[Any, dtype[void]],
        /,
        kth: _ArrayLikeInt_co,
        axis: CanIndex = -1,
        kind: _PartitionKind = "introselect",
        order: str | Sequence[str] | None = None,
    ) -> None: ...

    #
    @overload  # 2d, dtype: None
    def trace(
        self: ndarray[tuple[int, int], dtype[_ScalarT]],
        /,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: None = None,
        out: None = None,
    ) -> _ScalarT: ...
    @overload  # 2d, dtype: dtype[T], /
    def trace(
        self: ndarray[tuple[int, int], Any],
        /,
        offset: CanIndex,
        axis1: CanIndex,
        axis2: CanIndex,
        dtype: _DTypeLike[_ScalarT],
        out: None = None,
    ) -> _ScalarT: ...
    @overload  # 2d, *, dtype: dtype[T]
    def trace(
        self: ndarray[tuple[int, int], Any],
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
        indices: _IntLike_co,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> _ScalarT: ...
    @overload
    def take(
        self,
        /,
        indices: _ArrayLikeInt_co,
        axis: CanIndex | None = None,
        out: None = None,
        mode: _ModeKind = "raise",
    ) -> ndarray[tuple[int, ...], _DTypeT_co]: ...
    @overload
    def take(
        self,
        /,
        indices: _ArrayLikeInt_co,
        axis: CanIndex | None,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...
    @overload
    def take(
        self,
        /,
        indices: _ArrayLikeInt_co,
        axis: CanIndex | None = None,
        *,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...

    #
    @overload
    def repeat(self, /, repeats: _ArrayLikeInt_co, axis: None = None) -> ndarray[tuple[int], _DTypeT_co]: ...
    @overload
    def repeat(
        self: ndarray[_AnyShapeT, _DTypeT],
        /,
        repeats: _ArrayLikeInt_co,
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
    ) -> ndarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload
    def astype(
        self,
        /,
        dtype: DTypeLike,
        order: _OrderKACF = "K",
        casting: _CastingKind = "unsafe",
        subok: py_bool = True,
        copy: py_bool | _CopyMode = True,
    ) -> ndarray[_ShapeT_co, dtype[Any]]: ...

    # the special casings work around the lack of higher-kinded typing (HKT) support in Python
    @overload  # ()
    def view(self, /) -> Self: ...
    @overload  # (dtype: T)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT]) -> ndarray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[T])
    def view(self, /, dtype: _DTypeLike[_ScalarT]) -> ndarray[_ShapeT_co, dtype[_ScalarT]]: ...
    @overload  # (type: matrix)
    def view(self, /, *, type: type[matrix[Any, Any]]) -> matrix[tuple[int, int], _DTypeT_co]: ...
    @overload  # (_: matrix)
    def view(self, /, dtype: type[matrix[Any, Any]]) -> matrix[tuple[int, int], _DTypeT_co]: ...
    @overload  # (dtype: T, type: matrix)
    def view(self, /, dtype: _DTypeT | _HasDType[_DTypeT], type: type[matrix[Any, Any]]) -> matrix[tuple[int, int], _DTypeT]: ...
    @overload  # (dtype: dtype[T], type: matrix)
    def view(self, /, dtype: _DTypeLike[_ScalarT], type: type[matrix[Any, Any]]) -> matrix[tuple[int, int], dtype[_ScalarT]]: ...
    @overload  # (type: recarray)
    def view(self, /, *, type: type[recarray[Any, Any]]) -> recarray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: recarray)
    def view(self, /, dtype: type[recarray[Any, Any]]) -> recarray[_ShapeT_co, _DTypeT_co]: ...
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
    def view(self, /, *, type: type[ma.MaskedArray[Any, Any]]) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload  # (_: MaskedArray)
    def view(self, /, dtype: type[ma.MaskedArray[Any, Any]]) -> ma.MaskedArray[_ShapeT_co, _DTypeT_co]: ...
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
    def view(self, /, dtype: DTypeLike) -> ndarray[_ShapeT_co, dtype[Any]]: ...
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
    def flat(self) -> flatiter[ndarray[tuple[int], dtype[Self]]]: ...

    #
    @abc.abstractmethod
    def __init__(self, /, *args: Any, **kwargs: Any) -> None: ...

    if sys.version_info >= (3, 12):
        def __buffer__(self, flags: int, /) -> memoryview: ...

    #
    @overload
    def __array__(self, dtype: None = None, /) -> ndarray[tuple[()], dtype[Self]]: ...
    @overload
    def __array__(self, dtype: _DTypeT, /) -> ndarray[tuple[()], _DTypeT]: ...

    #
    @overload
    def __array_wrap__(
        self,
        array: ndarray[tuple[()], dtype[_ScalarT]],
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
        indices: _IntLike_co,
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
        indices: _ArrayLikeInt_co,
        axis: CanIndex | None,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...
    @overload
    def take(
        self,
        /,
        indices: _ArrayLikeInt_co,
        axis: CanIndex | None = None,
        *,
        out: _ArrayT,
        mode: _ModeKind = "raise",
    ) -> _ArrayT: ...

    #
    def repeat(self, /, repeats: _ArrayLikeInt_co, axis: CanIndex | None = None) -> NDArray[Self]: ...

    #
    def flatten(self, /, order: _OrderKACF = "C") -> ndarray[tuple[int], dtype[Self]]: ...
    def ravel(self, /, order: _OrderKACF = "C") -> ndarray[tuple[int], dtype[Self]]: ...
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
    ) -> Self | ndarray[tuple[L[1], ...], dtype[Self]]: ...
    @overload  # _(index)
    def reshape(
        self,
        size1: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[L[1]], dtype[Self]]: ...
    @overload  # _(index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        /,
        *,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[L[1], L[1]], dtype[Self]]: ...
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
    ) -> ndarray[tuple[L[1], L[1], L[1]], dtype[Self]]: ...
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
    ) -> ndarray[tuple[L[1], L[1], L[1], L[1]], dtype[Self]]: ...
    @overload  # _(index, index, index, index, index, *index)  # ndim >= 5
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        size4: CanIndex,
        size5: CanIndex,
        /,
        *sizes6_: CanIndex,
        order: _OrderACF = "C",
        copy: py_bool | None = None,
    ) -> ndarray[tuple[L[1], L[1], L[1], L[1], L[1], Unpack[tuple[L[1], ...]]], dtype[Self]]: ...

    #
    @overload
    def all(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
    ) -> bool_: ...
    @overload
    def all(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None,
        out: ndarray[tuple[()], dtype[_ScalarT]],
        keepdims: CanIndex = False,
        *,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
    ) -> _ScalarT: ...
    @overload
    def all(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None = None,
        *,
        out: ndarray[tuple[()], dtype[_ScalarT]],
        keepdims: CanIndex = False,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
    ) -> _ScalarT: ...
    @overload
    def any(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None = None,
        out: None = None,
        keepdims: CanIndex = False,
        *,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
    ) -> bool_: ...
    @overload
    def any(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None,
        out: ndarray[tuple[()], dtype[_ScalarT]],
        keepdims: CanIndex = False,
        *,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
    ) -> _ScalarT: ...
    @overload
    def any(
        self,
        /,
        axis: L[0, -1] | tuple[()] | None = None,
        *,
        out: ndarray[tuple[()], dtype[_ScalarT]],
        keepdims: CanIndex = False,
        where: py_bool | bool_ | ndarray[tuple[()], dtype[bool_]] = True,
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
    ) -> ndarray[tuple[int], dtype[intp]]: ...

    # Keep `dtype` at the bottom to avoid name conflicts with `dtype`
    @property
    def dtype(self) -> dtype[Self]: ...

class number(generic[_NumberItemT_co], Generic[_NBitT, _NumberItemT_co]):
    @abc.abstractmethod
    def __init__(self, value: _NumberItemT_co, /) -> None: ...

    #
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

    #
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __abs__(self, /) -> number[_NBitT]: ...

    #
    def __add__(self, x: Any, /) -> number: ...
    def __radd__(self, x: Any, /) -> number: ...
    def __sub__(self, x: Any, /) -> number: ...
    def __rsub__(self, x: Any, /) -> number: ...
    def __mul__(self, x: Any, /) -> number: ...
    def __rmul__(self, x: Any, /) -> number: ...
    def __pow__(self, x: Any, mod: None = None, /) -> number: ...
    def __rpow__(self, x: Any, mod: None = None, /) -> number: ...
    def __truediv__(self, x: Any, /) -> inexact: ...
    def __rtruediv__(self, x: Any, /) -> inexact: ...
    def __floordiv__(self: number[Any, float], x: Any, /) -> floating | integer: ...
    def __rfloordiv__(self: number[Any, float], x: Any, /) -> floating | integer: ...

    __lt__: _ComparisonOpLT[_NumberLike_co, _ArrayLikeNumber_co]
    __le__: _ComparisonOpLE[_NumberLike_co, _ArrayLikeNumber_co]
    __gt__: _ComparisonOpGT[_NumberLike_co, _ArrayLikeNumber_co]
    __ge__: _ComparisonOpGE[_NumberLike_co, _ArrayLikeNumber_co]

class bool(generic[_BoolItemT_co], Generic[_BoolItemT_co]):
    @property
    def itemsize(self) -> L[1]: ...
    @property
    def nbytes(self) -> L[1]: ...
    @property
    def real(self) -> Self: ...
    @property
    def imag(self) -> bool_[L[False]]: ...

    #
    @overload
    def __init__(self: bool_[L[False]], value: _Falsy = ..., /) -> None: ...
    @overload
    def __init__(self: bool_[L[True]], value: _Truthy, /) -> None: ...
    @overload
    def __init__(self: bool_[py_bool], value: object, /) -> None: ...

    #
    def __hash__(self, /) -> int: ...

    #
    def __bool__(self, /) -> _BoolItemT_co: ...

    #
    @deprecated("In future, it will be an error for 'np.bool' scalars to be interpreted as an index")
    def __index__(self, /) -> L[0, 1]: ...

    #
    @overload
    def __int__(self: bool_[L[False]], /) -> L[0]: ...
    @overload
    def __int__(self: bool_[L[True]], /) -> L[1]: ...
    @overload
    def __int__(self: bool_[py_bool], /) -> L[0, 1]: ...

    __lt__: _ComparisonOpLT[_NumberLike_co, _ArrayLikeNumber_co]
    __le__: _ComparisonOpLE[_NumberLike_co, _ArrayLikeNumber_co]
    __gt__: _ComparisonOpGT[_NumberLike_co, _ArrayLikeNumber_co]
    __ge__: _ComparisonOpGE[_NumberLike_co, _ArrayLikeNumber_co]

    def __abs__(self) -> Self: ...

    __add__: _BoolOp[bool_]
    __radd__: _BoolOp[bool_]
    __mul__: _BoolOp[bool_]
    __rmul__: _BoolOp[bool_]
    __sub__: _BoolSub
    __rsub__: _BoolSub
    __truediv__: _BoolTrueDiv
    __rtruediv__: _BoolTrueDiv
    __floordiv__: _BoolOp[int8]
    __rfloordiv__: _BoolOp[int8]

    @overload
    def __pow__(self, x: _NumberT, mod: None = None, /) -> _NumberT: ...
    @overload
    def __pow__(self, x: bool_ | py_bool, mod: None = None, /) -> int8: ...
    @overload
    def __pow__(self, x: int, mod: None = None, /) -> intp | int8: ...
    @overload
    def __pow__(self, x: float, mod: None = None, /) -> float64 | intp | int8: ...
    @overload
    def __pow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | intp | int8: ...

    #
    @overload
    def __rpow__(self, x: _NumberT, mod: None = None, /) -> _NumberT: ...
    @overload
    def __rpow__(self, x: bool_ | py_bool, mod: None = None, /) -> int8: ...
    @overload
    def __rpow__(self, x: int, mod: None = None, /) -> intp | int8: ...
    @overload
    def __rpow__(self, x: float, mod: None = None, /) -> float64 | intp | int8: ...
    @overload
    def __rpow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | intp | int8: ...

    __mod__: _BoolMod
    __rmod__: _BoolMod
    __divmod__: _BoolDivMod
    __rdivmod__: _BoolDivMod

    @overload
    def __lshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __lshift__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __lshift__(self, x: int, /) -> int8 | intp: ...
    __rlshift__ = __lshift__

    @overload
    def __rshift__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __rshift__(self, x: py_bool | bool_, /) -> int8: ...
    @overload
    def __rshift__(self, x: int, /) -> int8 | intp: ...
    __rrshift__ = __rshift__

    @overload
    def __invert__(self: bool_[L[False]], /) -> bool_[L[True]]: ...
    @overload
    def __invert__(self: bool_[L[True]], /) -> bool_[L[False]]: ...
    @overload
    def __invert__(self, /) -> bool_: ...

    #
    @overload
    def __and__(self: bool_[L[False]], x: py_bool | bool_, /) -> bool_[L[False]]: ...
    @overload
    def __and__(self, x: L[False] | bool_[L[False]], /) -> bool_[L[False]]: ...
    @overload
    def __and__(self, x: L[True] | bool_[L[True]], /) -> Self: ...
    @overload
    def __and__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __and__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __and__(self, x: int, /) -> bool_ | intp: ...
    __rand__ = __and__

    @overload
    def __xor__(self: bool_[L[False]], x: _BoolItemT | bool_[_BoolItemT], /) -> bool_[_BoolItemT]: ...
    @overload
    def __xor__(self: bool_[L[True]], x: L[True] | bool_[L[True]], /) -> bool_[L[False]]: ...
    @overload
    def __xor__(self, x: L[False] | bool_[L[False]], /) -> Self: ...
    @overload
    def __xor__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __xor__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __xor__(self, x: int, /) -> bool_ | intp: ...
    __rxor__ = __xor__

    @overload
    def __or__(self: bool_[L[True]], x: py_bool | bool_, /) -> bool_[L[True]]: ...
    @overload
    def __or__(self, x: L[False] | bool_[L[False]], /) -> Self: ...
    @overload
    def __or__(self, x: L[True] | bool_[L[True]], /) -> bool_[L[True]]: ...
    @overload
    def __or__(self, x: py_bool | bool_, /) -> bool_: ...
    @overload
    def __or__(self, x: _IntegerT, /) -> _IntegerT: ...
    @overload
    def __or__(self, x: int, /) -> bool_ | intp: ...
    __ror__ = __or__

# NOTE: The `object_` constructor returns the passed object, so instances with type
# `object_` cannot exists (at runtime).
# NOTE: Because mypy has some long-standing bugs related to `__new__`, `object_` can't
# be made generic.
@final
class object_(_RealMixin, generic[Any]):
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
    def __hash__(self, /) -> int: ...
    def __call__(self, /, *args: object, **kwargs: object) -> Any: ...

    if sys.version_info >= (3, 12):
        def __release_buffer__(self, buffer: memoryview, /) -> None: ...

class integer(_IntegralMixin, _RoundMixin, number[_NBitT, int]):
    @abc.abstractmethod
    def __init__(self, value: _ConvertibleToInt = ..., /) -> None: ...

    #
    def __abs__(self, /) -> Self: ...
    def __invert__(self, /) -> Self: ...

    #
    @overload
    def __radd__(self, x: int, /) -> Self: ...
    @overload
    def __radd__(self, x: floating[_64Bit], /) -> float64: ...  # type: ignore[misc]
    @overload
    def __radd__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __radd__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __radd__(self, x: complex, /) -> complex128 | float64 | Self: ...

    # keep in sync with __radd__
    @overload
    def __rsub__(self, x: int, /) -> Self: ...
    @overload
    def __rsub__(self, x: floating[_64Bit], /) -> float64: ...  # type: ignore[misc]
    @overload
    def __rsub__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __rsub__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __rsub__(self, x: complex, /) -> complex128 | float64 | Self: ...

    # keep in sync with __radd__
    @overload
    def __rmul__(self, x: int, /) -> Self: ...
    @overload
    def __rmul__(self, x: floating[_64Bit], /) -> float64: ...  # type: ignore[misc]
    @overload
    def __rmul__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __rmul__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __rmul__(self, x: complex, /) -> complex128 | float64 | Self: ...

    #
    @overload
    def __rpow__(self, x: int, mod: None = None, /) -> Self: ...
    @overload
    def __rpow__(self, x: floating[_64Bit], mod: None = None, /) -> float64: ...  # type: ignore[misc]
    @overload
    def __rpow__(self, x: float, mod: None = None, /) -> float64 | Self: ...
    @overload
    def __rpow__(self, x: complexfloating[_64Bit], mod: None = None, /) -> complex128: ...
    @overload
    def __rpow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | Self: ...

    #
    @overload
    def __truediv__(self, x: bool_ | integer | float, /) -> float64: ...
    @overload
    def __truediv__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __truediv__(self, x: complex, /) -> float64 | complex128: ...

    #
    @overload
    def __rtruediv__(self, x: float, /) -> float64: ...
    @overload
    def __rtruediv__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __rtruediv__(self, x: complex, /) -> float64 | complex128: ...

    # keep in sync with __radd__ (minus complex)
    @overload
    def __rfloordiv__(self, x: int, /) -> Self: ...
    @overload
    def __rfloordiv__(self, x: floating[_64Bit], /) -> float64: ...  # type: ignore[misc]
    @overload
    def __rfloordiv__(self, x: float, /) -> float64 | Self: ...

    #
    @overload
    def __mod__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __mod__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __mod__(self, x: float, /) -> Self | float64: ...
    @overload
    def __mod__(self, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __mod__(self, x: integer, /) -> integer: ...

    #
    @overload
    def __rmod__(self, x: int, /) -> Self: ...
    @overload
    def __rmod__(self, x: floating[_64Bit], /) -> float64: ...  # type: ignore[misc]
    @overload
    def __rmod__(self, x: float, /) -> Self | float64: ...

    #
    @overload
    def __divmod__(self, x: Self | int8 | int | bool_, /) -> _2Tuple[Self]: ...
    @overload
    def __divmod__(self, x: floating[_64Bit], /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self, x: float, /) -> _2Tuple[Self] | _2Tuple[float64]: ...
    @overload
    def __divmod__(self, x: signedinteger, /) -> _2Tuple[signedinteger]: ...
    @overload
    def __divmod__(self, x: integer, /) -> _2Tuple[integer]: ...

    #
    @overload
    def __rdivmod__(self, x: int, /) -> _2Tuple[Self]: ...
    @overload
    def __rdivmod__(self, x: floating[_64Bit], /) -> _2Tuple[float64]: ...  # type: ignore[misc]
    @overload
    def __rdivmod__(self, x: float, /) -> _2Tuple[Self] | _2Tuple[float64]: ...

    #
    @overload
    def __lshift__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __lshift__(self, x: _IntLike_co, /) -> integer: ...
    def __rlshift__(self, x: int, /) -> Self: ...

    #
    @overload
    def __rshift__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __rshift__(self, x: _IntLike_co, /) -> integer: ...
    def __rrshift__(self, x: int, /) -> Self: ...

    #
    @overload
    def __and__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __and__(self, x: _IntLike_co, /) -> integer: ...
    def __rand__(self, x: int, /) -> Self: ...

    #
    @overload
    def __or__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __or__(self, x: _IntLike_co, /) -> integer: ...
    def __ror__(self, x: int, /) -> Self: ...

    #
    @overload
    def __xor__(self, x: Self | int8 | int | bool_, /) -> Self: ...
    @overload
    def __xor__(self, x: _IntLike_co, /) -> integer: ...
    def __rxor__(self, x: int, /) -> Self: ...

class signedinteger(integer[_NBitT]):
    def __init__(self, value: _ConvertibleToInt = ..., /) -> None: ...

    # TODO(jorenham): These don't exist here; move to concrete subtypes once we have them
    # https://github.com/numpy/numtype/issues/136
    def __index__(self, /) -> int: ...
    def __hash__(self, /) -> int: ...
    def bit_count(self, /) -> int: ...

    #
    @overload
    def __add__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __add__(self, x: int64, /) -> int64: ...
    @overload
    def __add__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __add__(self: int32, x: int8 | int16 | int32, /) -> int32: ...
    @overload
    def __add__(self: int16, x: int32, /) -> int32: ...
    @overload
    def __add__(self: int16, x: int8 | int16, /) -> int16: ...
    @overload
    def __add__(self: int8, x: _SignedIntegerT, /) -> _SignedIntegerT: ...
    @overload
    def __add__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __add__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __add__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __add__(self, x: complex, /) -> complex128 | float64 | Self: ...

    #  keep in sync with __add__
    @overload
    def __sub__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __sub__(self, x: int64, /) -> int64: ...
    @overload
    def __sub__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __sub__(self: int32, x: int8 | int16 | int32, /) -> int32: ...
    @overload
    def __sub__(self: int16, x: int32, /) -> int32: ...
    @overload
    def __sub__(self: int16, x: int8 | int16, /) -> int16: ...
    @overload
    def __sub__(self: int8, x: _SignedIntegerT, /) -> _SignedIntegerT: ...
    @overload
    def __sub__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __sub__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __sub__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __sub__(self, x: complex, /) -> complex128 | float64 | Self: ...

    #  keep in sync with __add__
    @overload
    def __mul__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __mul__(self, x: int64, /) -> int64: ...
    @overload
    def __mul__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __mul__(self: int32, x: int8 | int16 | int32, /) -> int32: ...
    @overload
    def __mul__(self: int16, x: int32, /) -> int32: ...
    @overload
    def __mul__(self: int16, x: int8 | int16, /) -> int16: ...
    @overload
    def __mul__(self: int8, x: _SignedIntegerT, /) -> _SignedIntegerT: ...
    @overload
    def __mul__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __mul__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __mul__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __mul__(self, x: complex, /) -> complex128 | float64 | Self: ...

    #  keep in sync with __add__
    @overload
    def __pow__(self, x: Self | int | int8 | bool_, mod: None = None, /) -> Self: ...
    @overload
    def __pow__(self, x: int64, mod: None = None, /) -> int64: ...
    @overload
    def __pow__(self: int64, x: signedinteger, mod: None = None, /) -> int64: ...
    @overload
    def __pow__(self: int32, x: int8 | int16 | int32, mod: None = None, /) -> int32: ...
    @overload
    def __pow__(self: int16, x: int32, mod: None = None, /) -> int32: ...
    @overload
    def __pow__(self: int16, x: int8 | int16, mod: None = None, /) -> int16: ...
    @overload
    def __pow__(self: int8, x: _SignedIntegerT, mod: None = None, /) -> _SignedIntegerT: ...
    @overload
    def __pow__(self, x: floating[_64Bit], mod: None = None, /) -> float64: ...
    @overload
    def __pow__(self, x: complexfloating[_64Bit], mod: None = None, /) -> complex128: ...
    @overload
    def __pow__(self, x: float, mod: None = None, /) -> float64 | Self: ...
    @overload
    def __pow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | Self: ...

    #  keep in sync with __add__ (minus complex)
    @overload
    def __floordiv__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __floordiv__(self, x: int64, /) -> int64: ...
    @overload
    def __floordiv__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __floordiv__(self: int32, x: int8 | int16 | int32, /) -> int32: ...
    @overload
    def __floordiv__(self: int16, x: int32, /) -> int32: ...
    @overload
    def __floordiv__(self: int16, x: int8 | int16, /) -> int16: ...
    @overload
    def __floordiv__(self: int8, x: _SignedIntegerT, /) -> _SignedIntegerT: ...
    @overload
    def __floordiv__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __floordiv__(self, x: float, /) -> float64 | Self: ...

    #
    @overload  # type: ignore[override]
    def __mod__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __mod__(self, x: int64, /) -> int64: ...
    @overload
    def __mod__(self: int64, x: floating[_64Bit] | float32 | float16, /) -> float64: ...
    @overload
    def __mod__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __mod__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __mod__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __mod__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __mod__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __mod__(self, x: int | signedinteger, /) -> signedinteger: ...
    @overload
    def __mod__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __mod__(self, x: float, /) -> Self | float64: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with `__mod__`
    @overload  # type: ignore[override]
    def __divmod__(self, x: Self | int | int8 | bool_, /) -> _2Tuple[Self]: ...
    @overload
    def __divmod__(self, x: int64, /) -> _2Tuple[int64]: ...
    @overload
    def __divmod__(self: int64, x: floating[_64Bit] | float32 | float16, /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self: int64, x: signedinteger, /) -> _2Tuple[int64]: ...
    @overload
    def __divmod__(self: int32, x: int32 | int16 | int8, /) -> _2Tuple[int32]: ...
    @overload
    def __divmod__(self: int32 | int16 | int8, x: int32, /) -> _2Tuple[int32]: ...
    @overload
    def __divmod__(self: int16, x: int16 | int8, /) -> _2Tuple[int16]: ...
    @overload
    def __divmod__(self: int8, x: int16, /) -> _2Tuple[int16]: ...
    @overload
    def __divmod__(self, x: int | signedinteger, /) -> _2Tuple[signedinteger]: ...
    @overload
    def __divmod__(self, x: floating[_64Bit], /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self, x: float, /) -> _2Tuple[Self] | _2Tuple[float64]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __lshift__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __lshift__(self, x: int64, /) -> int64: ...
    @overload
    def __lshift__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __lshift__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __lshift__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __lshift__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __lshift__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __lshift__(self, x: signedinteger, /) -> signedinteger: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __lshift__
    @overload  # type: ignore[override]
    def __rshift__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __rshift__(self, x: int64, /) -> int64: ...
    @overload
    def __rshift__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __rshift__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rshift__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __rshift__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __rshift__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __rshift__(self, x: signedinteger, /) -> signedinteger: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __lshift__
    @overload  # type: ignore[override]
    def __and__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __and__(self, x: int64, /) -> int64: ...
    @overload
    def __and__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __and__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __and__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __and__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __and__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __and__(self, x: signedinteger, /) -> signedinteger: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __lshift__
    @overload  # type: ignore[override]
    def __xor__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __xor__(self, x: int64, /) -> int64: ...
    @overload
    def __xor__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __xor__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __xor__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __xor__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __xor__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __xor__(self, x: signedinteger, /) -> signedinteger: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __lshift__
    @overload  # type: ignore[override]
    def __or__(self, x: Self | int | int8 | bool_, /) -> Self: ...
    @overload
    def __or__(self, x: int64, /) -> int64: ...
    @overload
    def __or__(self: int64, x: signedinteger, /) -> int64: ...
    @overload
    def __or__(self: int32, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __or__(self: int32 | int16 | int8, x: int32, /) -> int32: ...
    @overload
    def __or__(self: int16, x: int16 | int8, /) -> int16: ...
    @overload
    def __or__(self: int8, x: int16, /) -> int16: ...
    @overload
    def __or__(self, x: signedinteger, /) -> signedinteger: ...  # pyright: ignore[reportIncompatibleMethodOverride]

class unsignedinteger(integer[_NBitT]):
    def __init__(self, value: _ConvertibleToInt = ..., /) -> None: ...

    # TODO(jorenham): These don't exist here; move to concrete subtypes once we have them
    # https://github.com/numpy/numtype/issues/136
    def __index__(self, /) -> int: ...
    def __hash__(self, /) -> int: ...
    def bit_count(self, /) -> int: ...

    #
    @overload
    def __add__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __add__(self, x: uint64, /) -> uint64: ...
    @overload
    def __add__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __add__(self: uint64 | uint32, x: floating[_64Bit] | float32 | float16, /) -> float64: ...
    @overload
    def __add__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __add__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __add__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __add__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __add__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __add__(self: uint16, x: float32 | float16, /) -> float32: ...
    @overload
    def __add__(self: uint16, x: uint32, /) -> uint32: ...
    @overload
    def __add__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __add__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __add__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __add__(self: uint8, x: float16, /) -> float16: ...
    @overload
    def __add__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __add__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __add__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __add__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __add__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __add__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __add__(self, x: datetime64[_DT64ItemT], /) -> datetime64[_DT64ItemT]: ...
    @overload
    def __add__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __add__(self, x: object_, /) -> object_: ...
    @overload
    def __add__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __add__(self, x: complex, /) -> complex128 | float64 | Self: ...

    #
    @overload  # type: ignore[override]
    def __radd__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __radd__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __radd__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __radd__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __radd__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __radd__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __radd__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __radd__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __radd__(self, x: datetime64[_DT64ItemT], /) -> datetime64[_DT64ItemT]: ...
    @overload
    def __radd__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __radd__(self, x: object_, /) -> object_: ...
    @overload
    def __radd__(self, x: int, /) -> Self: ...
    @overload
    def __radd__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __radd__(self, x: complex, /) -> complex128 | float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __add__
    @overload
    def __sub__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __sub__(self, x: uint64, /) -> uint64: ...
    @overload
    def __sub__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __sub__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __sub__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __sub__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __sub__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __sub__(self: uint16, x: uint32, /) -> uint32: ...
    @overload
    def __sub__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __sub__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __sub__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __sub__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __sub__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __sub__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __sub__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __sub__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __sub__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __sub__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __sub__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __sub__(self, x: object_, /) -> object_: ...
    @overload
    def __sub__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __sub__(self, x: complex, /) -> complex128 | float64 | Self: ...

    # keep in sync with __radd__
    @overload  # type: ignore[override]
    def __rsub__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __rsub__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rsub__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rsub__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __rsub__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __rsub__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rsub__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __rsub__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __rsub__(self, x: datetime64[_DT64ItemT], /) -> datetime64[_DT64ItemT]: ...
    @overload
    def __rsub__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __rsub__(self, x: object_, /) -> object_: ...
    @overload
    def __rsub__(self, x: int, /) -> Self: ...
    @overload
    def __rsub__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __rsub__(self, x: complex, /) -> complex128 | float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __add__
    @overload
    def __mul__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __mul__(self, x: uint64, /) -> uint64: ...
    @overload
    def __mul__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __mul__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __mul__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __mul__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __mul__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __mul__(self: uint16, x: uint32, /) -> uint32: ...
    @overload
    def __mul__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __mul__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __mul__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __mul__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __mul__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __mul__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __mul__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __mul__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __mul__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __mul__(self, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __mul__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __mul__(self, x: object_, /) -> object_: ...
    @overload
    def __mul__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __mul__(self, x: complex, /) -> complex128 | float64 | Self: ...

    # keep in sync with __radd__
    @overload  # type: ignore[override]
    def __rmul__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __rmul__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rmul__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rmul__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __rmul__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __rmul__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rmul__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __rmul__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __rmul__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __rmul__(self, x: object_, /) -> object_: ...
    @overload
    def __rmul__(self, x: int, /) -> Self: ...
    @overload
    def __rmul__(self, x: float, /) -> float64 | Self: ...
    @overload
    def __rmul__(self, x: complex, /) -> complex128 | float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __mul__ (minus the timedeltaa64)
    @overload
    def __pow__(self, x: Self | int | uint8 | bool_, mod: None = None, /) -> Self: ...
    @overload
    def __pow__(self, x: uint64, mod: None = None, /) -> uint64: ...
    @overload
    def __pow__(self: uint64, x: signedinteger, mod: None = None, /) -> float64: ...
    @overload
    def __pow__(self: uint64, x: unsignedinteger | bool_, mod: None = None, /) -> uint64: ...
    @overload
    def __pow__(self: uint32, x: signedinteger, mod: None = None, /) -> int64: ...
    @overload
    def __pow__(self: uint32 | uint16 | uint8, x: int64, mod: None = None, /) -> int64: ...
    @overload
    def __pow__(self: uint32, x: uint32 | uint16 | uint8, mod: None = None, /) -> uint32: ...
    @overload
    def __pow__(self: uint16, x: uint32, mod: None = None, /) -> uint32: ...
    @overload
    def __pow__(self: uint16, x: int16 | int8, mod: None = None, /) -> int32: ...
    @overload
    def __pow__(self: uint16 | uint8, x: int32, mod: None = None, /) -> int32: ...
    @overload
    def __pow__(self: uint16, x: uint16 | uint8, mod: None = None, /) -> uint16: ...
    @overload
    def __pow__(self: uint8, x: _UnsignedIntegerT, mod: None = None, /) -> _UnsignedIntegerT: ...
    @overload
    def __pow__(self: uint8, x: int16 | int8, mod: None = None, /) -> int16: ...
    @overload
    def __pow__(self, x: unsignedinteger, mod: None = None, /) -> unsignedinteger: ...
    @overload
    def __pow__(self, x: signedinteger, mod: None = None, /) -> float64 | signedinteger: ...
    @overload
    def __pow__(self, x: integer, mod: None = None, /) -> float64 | integer: ...
    @overload
    def __pow__(self, x: floating[_64Bit], mod: None = None, /) -> float64: ...
    @overload
    def __pow__(self, x: complexfloating[_64Bit], mod: None = None, /) -> complex128: ...
    @overload
    def __pow__(self, x: object_, mod: None = None, /) -> object_: ...
    @overload
    def __pow__(self, x: float, mod: None = None, /) -> float64 | Self: ...
    @overload
    def __pow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | Self: ...

    # keep in sync with __rmul__ (minus the timedeltaa64)
    @overload  # type: ignore[override]
    def __rpow__(self: uint64, x: signedinteger, mod: None = None, /) -> float64: ...
    @overload
    def __rpow__(self: uint32, x: signedinteger, mod: None = None, /) -> int64: ...
    @overload
    def __rpow__(self: uint32 | uint16 | uint8, x: int64, mod: None = None, /) -> int64: ...
    @overload
    def __rpow__(self: uint16, x: int16 | int8, mod: None = None, /) -> int32: ...
    @overload
    def __rpow__(self: uint16 | uint8, x: int32, mod: None = None, /) -> int32: ...
    @overload
    def __rpow__(self: uint8, x: int16 | int8, mod: None = None, /) -> int16: ...
    @overload
    def __rpow__(self, x: signedinteger, mod: None = None, /) -> float64 | signedinteger: ...
    @overload
    def __rpow__(self, x: integer, mod: None = None, /) -> float64 | integer: ...
    @overload
    def __rpow__(self, x: object_, mod: None = None, /) -> object_: ...
    @overload
    def __rpow__(self, x: int, mod: None = None, /) -> Self: ...
    @overload
    def __rpow__(self, x: float, mod: None = None, /) -> float64 | Self: ...
    @overload
    def __rpow__(self, x: complex, mod: None = None, /) -> complex128 | float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __pow__ (minus the complex overloads)
    @overload
    def __floordiv__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __floordiv__(self, x: uint64, /) -> uint64: ...
    @overload
    def __floordiv__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __floordiv__(self: uint64, x: unsignedinteger, /) -> uint64: ...
    @overload
    def __floordiv__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __floordiv__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __floordiv__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __floordiv__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __floordiv__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __floordiv__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __floordiv__(self: uint16 | uint8, x: uint16, /) -> uint16: ...
    @overload
    def __floordiv__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __floordiv__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __floordiv__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __floordiv__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __floordiv__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __floordiv__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __floordiv__(self, x: object_, /) -> object_: ...
    @overload
    def __floordiv__(self, x: float, /) -> float64 | Self: ...

    # keep in sync with __rpow__ (minus the complex overloads)
    @overload  # type: ignore[override]
    def __rfloordiv__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __rfloordiv__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rfloordiv__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rfloordiv__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __rfloordiv__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __rfloordiv__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rfloordiv__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __rfloordiv__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __rfloordiv__(self, x: object_, /) -> object_: ...
    @overload
    def __rfloordiv__(self, x: int, /) -> Self: ...
    @overload
    def __rfloordiv__(self, x: float, /) -> float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __floordiv__
    @overload  # type: ignore[override]
    def __mod__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __mod__(self, x: uint64, /) -> uint64: ...
    @overload
    def __mod__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __mod__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __mod__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __mod__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __mod__(self: uint16, x: uint32, /) -> uint32: ...
    @overload
    def __mod__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __mod__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __mod__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __mod__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __mod__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __mod__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __mod__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __mod__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __mod__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __mod__(self, x: floating[_64Bit], /) -> float64: ...
    @overload
    def __mod__(self, x: object_, /) -> object_: ...
    @overload
    def __mod__(self, x: float, /) -> float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __rfloordiv__
    @overload  # type: ignore[override]
    def __rmod__(self: uint64, x: signedinteger, /) -> float64: ...
    @overload
    def __rmod__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rmod__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rmod__(self: uint16, x: int16 | int8, /) -> int32: ...
    @overload
    def __rmod__(self: uint16 | uint8, x: int32, /) -> int32: ...
    @overload
    def __rmod__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rmod__(self, x: signedinteger, /) -> float64 | signedinteger: ...
    @overload
    def __rmod__(self, x: integer, /) -> float64 | integer: ...
    @overload
    def __rmod__(self, x: object_, /) -> object_: ...
    @overload
    def __rmod__(self, x: int, /) -> Self: ...
    @overload
    def __rmod__(self, x: float, /) -> float64 | Self: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with `__mod__` (minus `object_`)
    @overload  # type: ignore[override]
    def __divmod__(self, x: Self | int | uint8 | bool_, /) -> _2Tuple[Self]: ...
    @overload
    def __divmod__(self, x: uint64, /) -> _2Tuple[uint64]: ...
    @overload
    def __divmod__(self: uint64, x: signedinteger, /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self: uint64, x: unsignedinteger | bool_, /) -> _2Tuple[uint64]: ...
    @overload
    def __divmod__(self: uint32, x: signedinteger, /) -> _2Tuple[int64]: ...
    @overload
    def __divmod__(self: uint32 | uint16 | uint8, x: int64, /) -> _2Tuple[int64]: ...
    @overload
    def __divmod__(self: uint32, x: uint32 | uint16 | uint8, /) -> _2Tuple[uint32]: ...
    @overload
    def __divmod__(self: uint16, x: uint32, /) -> _2Tuple[uint32]: ...
    @overload
    def __divmod__(self: uint16, x: int16 | int8, /) -> _2Tuple[int32]: ...
    @overload
    def __divmod__(self: uint16 | uint8, x: int32, /) -> _2Tuple[int32]: ...
    @overload
    def __divmod__(self: uint16, x: uint16 | uint8, /) -> _2Tuple[uint16]: ...
    @overload
    def __divmod__(self: uint8, x: _UnsignedIntegerT, /) -> _2Tuple[_UnsignedIntegerT]: ...
    @overload
    def __divmod__(self: uint8, x: int16 | int8, /) -> _2Tuple[int16]: ...
    @overload
    def __divmod__(self, x: unsignedinteger, /) -> _2Tuple[unsignedinteger]: ...
    @overload
    def __divmod__(self, x: signedinteger, /) -> _2Tuple[float64] | _2Tuple[signedinteger]: ...
    @overload
    def __divmod__(self, x: integer, /) -> _2Tuple[float64] | _2Tuple[integer]: ...
    @overload
    def __divmod__(self, x: floating[_64Bit], /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self, x: float, /) -> _2Tuple[float64] | _2Tuple[Self]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with `__rmod__` (minus `object_`)
    @overload  # type: ignore[override]
    def __rdivmod__(self: uint64, x: signedinteger, /) -> _2Tuple[float64]: ...
    @overload
    def __rdivmod__(self: uint32, x: signedinteger, /) -> _2Tuple[int64]: ...
    @overload
    def __rdivmod__(self: uint32 | uint16 | uint8, x: int64, /) -> _2Tuple[int64]: ...
    @overload
    def __rdivmod__(self: uint16, x: int16 | int8, /) -> _2Tuple[int32]: ...
    @overload
    def __rdivmod__(self: uint16 | uint8, x: int32, /) -> _2Tuple[int32]: ...
    @overload
    def __rdivmod__(self: uint8, x: int16 | int8, /) -> _2Tuple[int16]: ...
    @overload
    def __rdivmod__(self, x: signedinteger, /) -> _2Tuple[signedinteger] | _2Tuple[float64]: ...
    @overload
    def __rdivmod__(self, x: integer, /) -> _2Tuple[integer] | _2Tuple[float64]: ...
    @overload
    def __rdivmod__(self, x: int, /) -> _2Tuple[Self]: ...
    @overload
    def __rdivmod__(self, x: float, /) -> _2Tuple[float64] | _2Tuple[Self]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload  # type: ignore[override]
    def __lshift__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __lshift__(self, x: uint64, /) -> uint64: ...
    @overload
    def __lshift__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __lshift__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __lshift__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __lshift__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __lshift__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __lshift__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __lshift__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __lshift__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __lshift__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __lshift__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __lshift__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __lshift__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __lshift__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @overload
    def __rlshift__(self, x: int, /) -> Self: ...
    @overload
    def __rlshift__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rlshift__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rlshift__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rlshift__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __rlshift__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rlshift__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __rlshift__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...

    # keep in sync with __lshift__
    @overload  # type: ignore[override]
    def __rshift__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __rshift__(self, x: uint64, /) -> uint64: ...
    @overload
    def __rshift__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __rshift__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rshift__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rshift__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __rshift__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __rshift__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rshift__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __rshift__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __rshift__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __rshift__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rshift__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __rshift__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __rshift__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __rlshift__
    @overload
    def __rrshift__(self, x: int, /) -> Self: ...
    @overload
    def __rrshift__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rrshift__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rrshift__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rrshift__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __rrshift__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rrshift__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __rrshift__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...

    # keep in sync with __rshift__
    @overload  # type: ignore[override]
    def __and__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __and__(self, x: uint64, /) -> uint64: ...
    @overload
    def __and__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __and__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __and__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __and__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __and__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __and__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __and__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __and__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __and__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __and__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __and__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __and__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __and__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __rrshift__
    @overload
    def __rand__(self, x: int, /) -> Self: ...
    @overload
    def __rand__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rand__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rand__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rand__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __rand__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rand__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __rand__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...

    # keep in sync with __and__
    @overload  # type: ignore[override]
    def __xor__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __xor__(self, x: uint64, /) -> uint64: ...
    @overload
    def __xor__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __xor__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __xor__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __xor__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __xor__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __xor__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __xor__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __xor__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __xor__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __xor__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __xor__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __xor__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __xor__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __rand__
    @overload
    def __rxor__(self, x: int, /) -> Self: ...
    @overload
    def __rxor__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __rxor__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __rxor__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __rxor__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __rxor__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __rxor__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __rxor__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...

    # keep in sync with __xor__
    @overload  # type: ignore[override]
    def __or__(self, x: Self | int | uint8 | bool_, /) -> Self: ...
    @overload
    def __or__(self, x: uint64, /) -> uint64: ...
    @overload
    def __or__(self: uint64, x: unsignedinteger | bool_, /) -> uint64: ...
    @overload
    def __or__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __or__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __or__(self: uint32, x: uint32 | uint16 | uint8, /) -> uint32: ...
    @overload
    def __or__(self: uint32 | uint16 | uint8, x: uint32, /) -> uint32: ...
    @overload
    def __or__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __or__(self: uint16, x: uint16 | uint8, /) -> uint16: ...
    @overload
    def __or__(self: uint8, x: _UnsignedIntegerT, /) -> _UnsignedIntegerT: ...
    @overload
    def __or__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __or__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __or__(self, x: unsignedinteger, /) -> unsignedinteger: ...
    @overload
    def __or__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __or__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # keep in sync with __rxor__
    @overload
    def __ror__(self, x: int, /) -> Self: ...
    @overload
    def __ror__(self: uint32, x: signedinteger, /) -> int64: ...
    @overload
    def __ror__(self: uint32 | uint16 | uint8, x: int64, /) -> int64: ...
    @overload
    def __ror__(self: uint16, x: int32 | int16 | int8, /) -> int32: ...
    @overload
    def __ror__(self: uint8, x: int32, /) -> int32: ...
    @overload
    def __ror__(self: uint8, x: int16 | int8, /) -> int16: ...
    @overload
    def __ror__(self: uint32 | uint16 | uint8, x: signedinteger, /) -> signedinteger: ...
    @overload
    def __ror__(self: uint32 | uint16 | uint8, x: integer, /) -> integer: ...

class inexact(number[_NBitT, _InexactItemT_co], Generic[_NBitT, _InexactItemT_co]):
    @abc.abstractmethod
    def __init__(self, value: _InexactItemT_co | None = ..., /) -> None: ...
    @override
    def __abs__(self, /) -> floating[_NBitT]: ...

class floating(_RealMixin, _RoundMixin, inexact[_NBitT, float]):
    def __init__(self, value: _ConvertibleToFloat | None = ..., /) -> None: ...

    # TODO(jorenham): These don't exist here; move to concrete subtypes once we have them
    # https://github.com/numpy/numtype/issues/136
    def __hash__(self, /) -> int: ...
    def is_integer(self, /) -> py_bool: ...
    def as_integer_ratio(self, /) -> tuple[int, int]: ...

    #
    @overload
    def __add__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __add__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self, x: clongdouble, /) -> clongdouble: ...
    @overload
    def __add__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __add__(self: longdouble, x: complexfloating, /) -> clongdouble: ...
    @overload
    def __add__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __add__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __add__(self: floating[_64Bit], x: complexfloating[_64Bit] | complexfloating[_32Bit], /) -> complex128: ...
    @overload
    def __add__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __add__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __add__(self: float32 | float16, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __add__(self: float32 | float16, x: complexfloating[_32Bit], /) -> complex64: ...
    @overload
    def __add__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __add__(self, x: floating | integer | bool_, /) -> floating: ...
    @overload
    def __add__(self, x: number | bool_, /) -> inexact: ...

    #
    @overload
    def __radd__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __radd__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __radd__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __radd__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __radd__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __radd__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __radd__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...
    @overload
    def __radd__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __radd__(self, x: integer, /) -> floating: ...
    @overload
    def __radd__(self, x: number, /) -> inexact: ...

    # keep in sync with `__add__`
    @overload
    def __sub__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __sub__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self, x: clongdouble, /) -> clongdouble: ...
    @overload
    def __sub__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __sub__(self: longdouble, x: complexfloating, /) -> clongdouble: ...
    @overload
    def __sub__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __sub__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __sub__(self: floating[_64Bit], x: complexfloating[_64Bit] | complexfloating[_32Bit], /) -> complex128: ...
    @overload
    def __sub__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __sub__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __sub__(self: float32 | float16, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __sub__(self: float32 | float16, x: complexfloating[_32Bit], /) -> complex64: ...
    @overload
    def __sub__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __sub__(self, x: floating | integer | bool_, /) -> floating: ...
    @overload
    def __sub__(self, x: number | bool_, /) -> inexact: ...

    # keep in sync with `__radd__`
    @overload
    def __rsub__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __rsub__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __rsub__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __rsub__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __rsub__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __rsub__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __rsub__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...
    @overload
    def __rsub__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __rsub__(self, x: integer, /) -> floating: ...
    @overload
    def __rsub__(self, x: number, /) -> inexact: ...

    # keep in sync with `__add__` (plus a `timedelta64` overload)
    @overload
    def __mul__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __mul__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self, x: clongdouble, /) -> clongdouble: ...
    @overload
    def __mul__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __mul__(self: longdouble, x: complexfloating, /) -> clongdouble: ...
    @overload
    def __mul__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __mul__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __mul__(self: floating[_64Bit], x: complexfloating[_64Bit] | complexfloating[_32Bit], /) -> complex128: ...
    @overload
    def __mul__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __mul__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __mul__(self: float32 | float16, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __mul__(self: float32 | float16, x: complexfloating[_32Bit], /) -> complex64: ...
    @overload
    def __mul__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __mul__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __mul__(self, x: floating | integer | bool_, /) -> floating: ...
    @overload
    def __mul__(self, x: number | bool_, /) -> inexact: ...

    # keep in sync with `__radd__` (plus a `timedelta64` overload)
    @overload
    def __rmul__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __rmul__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __rmul__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __rmul__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __rmul__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __rmul__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __rmul__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...
    @overload
    def __rmul__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __rmul__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __rmul__(self, x: integer, /) -> floating: ...
    @overload
    def __rmul__(self, x: number, /) -> inexact: ...

    # keep in sync with `__mul__` (minus the `timedelta64` overloads)
    @overload
    def __pow__(
        self: float32 | float16,
        x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit],
        mod: None = None,
        /,
    ) -> float64: ...
    @overload
    def __pow__(self, x: float | Self | float16 | integer[_8Bit] | bool_, mod: None = None, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self, x: longdouble, mod: None = None, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __pow__(self, x: clongdouble, mod: None = None, /) -> clongdouble: ...
    @overload
    def __pow__(self: longdouble, x: floating | integer | bool_, mod: None = None, /) -> longdouble: ...
    @overload
    def __pow__(self: longdouble, x: complexfloating, mod: None = None, /) -> clongdouble: ...
    @overload
    def __pow__(self: longdouble, x: complex, mod: None = None, /) -> clongdouble | longdouble: ...
    @overload
    def __pow__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, mod: None = None, /) -> float64: ...
    @overload
    def __pow__(
        self: floating[_64Bit],
        x: complexfloating[_64Bit] | complexfloating[_32Bit],
        mod: None = None,
        /,
    ) -> complex128: ...
    @overload
    def __pow__(self: floating[_64Bit], x: complex, mod: None = None, /) -> complex128 | float64: ...
    @overload
    def __pow__(self: float32 | float16, x: float32 | integer[_16Bit], mod: None = None, /) -> float32: ...
    @overload
    def __pow__(self: float32 | float16, x: complexfloating[_64Bit], mod: None = None, /) -> complex128: ...
    @overload
    def __pow__(self: float32 | float16, x: complexfloating[_32Bit], mod: None = None, /) -> complex64: ...
    @overload
    def __pow__(self: float32 | float16, x: complex, mod: None = None, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __pow__(self, x: floating | integer | bool_, mod: None = None, /) -> floating: ...
    @overload
    def __pow__(self, x: number | bool_, mod: None = None, /) -> inexact: ...

    # keep in sync with `__rmul__` (minus the `timedelta64` overloads)
    @overload
    def __rpow__(self, x: float | Self | float16 | integer[_8Bit] | bool_, mod: None = None, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rpow__(self, x: longdouble, mod: None = None, /) -> longdouble: ...
    @overload
    def __rpow__(self: longdouble, x: integer, mod: None = None, /) -> longdouble: ...
    @overload
    def __rpow__(self: longdouble, x: complex, mod: None = None, /) -> clongdouble | longdouble: ...
    @overload
    def __rpow__(self: floating[_64Bit], x: integer, mod: None = None, /) -> float64: ...
    @overload
    def __rpow__(self: floating[_64Bit], x: complex, mod: None = None, /) -> complex128 | float64: ...
    @overload
    def __rpow__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], mod: None = None, /) -> float64: ...
    @overload
    def __rpow__(self: float32 | float16, x: integer[_16Bit], mod: None = None, /) -> float32: ...
    @overload
    def __rpow__(self: float32 | float16, x: complex, mod: None = None, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __rpow__(self, x: integer, mod: None = None, /) -> floating: ...
    @overload
    def __rpow__(self, x: number, mod: None = None, /) -> inexact: ...

    # keep in sync with `__pow__`
    @overload
    def __truediv__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __truediv__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __truediv__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __truediv__(self, x: clongdouble, /) -> clongdouble: ...
    @overload
    def __truediv__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __truediv__(self: longdouble, x: complexfloating, /) -> clongdouble: ...
    @overload
    def __truediv__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __truediv__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __truediv__(self: floating[_64Bit], x: complexfloating[_64Bit] | complexfloating[_32Bit], /) -> complex128: ...
    @overload
    def __truediv__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __truediv__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __truediv__(self: float32 | float16, x: complexfloating[_64Bit], /) -> complex128: ...
    @overload
    def __truediv__(self: float32 | float16, x: complexfloating[_32Bit], /) -> complex64: ...
    @overload
    def __truediv__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __truediv__(self, x: floating | integer | bool_, /) -> floating: ...
    @overload
    def __truediv__(self, x: number | bool_, /) -> inexact: ...

    # keep in sync with `__rpow__` (plus a `timedelta64` overload)
    @overload
    def __rtruediv__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rtruediv__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __rtruediv__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __rtruediv__(self: longdouble, x: complex, /) -> clongdouble | longdouble: ...
    @overload
    def __rtruediv__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __rtruediv__(self: floating[_64Bit], x: complex, /) -> complex128 | float64: ...
    @overload
    def __rtruediv__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __rtruediv__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...
    @overload
    def __rtruediv__(self: float32 | float16, x: complex, /) -> complex64 | floating[_NBitT]: ...
    @overload
    def __rtruediv__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __rtruediv__(self, x: integer, /) -> floating: ...
    @overload
    def __rtruediv__(self, x: number, /) -> inexact: ...

    # keep in sync with `__truediv__` (minus the complex overloads)
    @overload
    def __floordiv__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __floordiv__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __floordiv__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __floordiv__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __floordiv__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __floordiv__(self, x: floating | integer | bool_, /) -> floating: ...

    # keep in sync with `__rtruediv__` (minus the complex overloads)
    @overload
    def __rfloordiv__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rfloordiv__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __rfloordiv__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __rfloordiv__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __rfloordiv__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __rfloordiv__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...
    @overload
    def __rfloordiv__(self, x: timedelta64[_TD64ItemT], /) -> timedelta64[_TD64ItemT]: ...
    @overload
    def __rfloordiv__(self, x: integer, /) -> floating: ...

    # keep in sync with `__floordiv__`
    @overload
    def __mod__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __mod__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self, x: longdouble, /) -> longdouble: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self: longdouble, x: floating | integer | bool_, /) -> longdouble: ...
    @overload
    def __mod__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> float64: ...
    @overload
    def __mod__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> float32: ...
    @overload
    def __mod__(self, x: floating | integer | bool_, /) -> floating: ...

    # keep in sync with `__rfloordiv__` (minus the `md->m` overload for `timedelta64`)
    @overload
    def __rmod__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> Self: ...  # type: ignore[overload-overlap]
    @overload
    def __rmod__(self, x: longdouble, /) -> longdouble: ...
    @overload
    def __rmod__(self: longdouble, x: integer, /) -> longdouble: ...
    @overload
    def __rmod__(self: floating[_64Bit], x: integer, /) -> float64: ...
    @overload
    def __rmod__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> float64: ...
    @overload
    def __rmod__(self: float32 | float16, x: integer[_16Bit], /) -> float32: ...  # type: ignore[misc]
    @overload
    def __rmod__(self, x: integer, /) -> floating: ...

    # keep in sync with `__mod__`
    @overload
    def __divmod__(self: float32 | float16, x: floating[_64Bit] | integer[_64Bit] | integer[_32Bit], /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> _2Tuple[Self]: ...  # type: ignore[overload-overlap]
    @overload
    def __divmod__(self, x: longdouble, /) -> _2Tuple[longdouble]: ...  # type: ignore[overload-overlap]
    @overload
    def __divmod__(self: longdouble, x: floating | integer | bool_, /) -> _2Tuple[longdouble]: ...
    @overload
    def __divmod__(self: floating[_64Bit], x: floating[_64Bit] | float32 | float16 | integer, /) -> _2Tuple[float64]: ...
    @overload
    def __divmod__(self: float32 | float16, x: float32 | integer[_16Bit], /) -> _2Tuple[float32]: ...

    # keep in sync with `__rmod__`
    @overload
    def __rdivmod__(self, x: float | Self | float16 | integer[_8Bit] | bool_, /) -> _2Tuple[Self]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self, x: longdouble, /) -> _2Tuple[longdouble]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self: longdouble, x: integer, /) -> _2Tuple[longdouble]: ...  # type: ignore[overload-overlap]
    @overload
    def __rdivmod__(self: floating[_64Bit], x: float32 | float16 | integer, /) -> _2Tuple[float64]: ...  # type: ignore[misc]
    @overload
    def __rdivmod__(self: float32 | float16, x: integer[_64Bit] | integer[_32Bit], /) -> _2Tuple[float64]: ...
    @overload
    def __rdivmod__(self: float32 | float16, x: integer[_16Bit], /) -> _2Tuple[float32]: ...  # type: ignore[misc]

class float64(floating[_64Bit], float):  # type: ignore[misc]
    @property
    @override
    def itemsize(self) -> L[8]: ...
    @property
    @override
    def nbytes(self) -> L[8]: ...
    @property
    @override
    def real(self) -> Self: ...
    @property
    @override
    def imag(self) -> Self: ...

    #
    @override
    def conjugate(self) -> Self: ...
    @override
    def is_integer(self, /) -> py_bool: ...
    @override
    def as_integer_ratio(self, /) -> tuple[int, int]: ...

    #
    def __new__(cls, x: _ConvertibleToFloat | None = 0, /) -> Self: ...
    @classmethod
    def __getformat__(cls, typestr: L["double", "float"], /) -> str: ...
    def __getnewargs__(self, /) -> tuple[float]: ...

    #
    @override
    def __abs__(self, /) -> float64: ...

# The main reason for `complexfloating` having two typevars is cosmetic.
# It is used to clarify why `complex128`s precision is `_64Bit`, the latter
# describing the two 64 bit floats representing its real and imaginary component
class complexfloating(inexact[_NBitT1, complex], Generic[_NBitT1, _NBitT2]):
    @property
    def real(self) -> floating[_NBitT1]: ...
    @property
    def imag(self) -> floating[_NBitT2]: ...

    #
    @overload
    def __init__(self, real: _ConvertibleToComplex | None = 0, /) -> None: ...
    @overload
    def __init__(self, real: _ToReal = 0, imag: _ToImag = 0, /) -> None: ...

    # TODO(jorenham): These don't exist here; move to concrete subtypes once we have them
    # https://github.com/numpy/numtype/issues/136
    def __hash__(self, /) -> int: ...
    def __complex__(self, /) -> complex: ...

    #
    @deprecated("The Python built-in `round` is deprecated for complex scalars, and will raise a `TypeError` in a future release")
    def __round__(self, /, ndigits: CanIndex | None = None) -> Self: ...

    #
    @override
    def __abs__(self, /) -> floating[_NBitT1]: ...

    #
    @overload
    def __add__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...
    @overload
    def __add__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __add__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __add__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __add__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __add__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __add__(self, x: complex, /) -> Self: ...

    #
    @overload
    def __radd__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...  # type: ignore[misc]
    @overload
    def __radd__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __radd__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __radd__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __radd__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __radd__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __radd__(self, x: complex, /) -> Self: ...

    # keep in sync with `__add__`
    @overload
    def __sub__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...
    @overload
    def __sub__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __sub__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __sub__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __sub__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __sub__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __sub__(self, x: complex, /) -> Self: ...

    # keep in sync with `__radd__`
    @overload
    def __rsub__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...  # type: ignore[misc]
    @overload
    def __rsub__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __rsub__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __rsub__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __rsub__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __rsub__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __rsub__(self, x: complex, /) -> Self: ...

    # keep in sync with `__add__`
    @overload
    def __mul__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...
    @overload
    def __mul__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __mul__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __mul__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __mul__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __mul__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __mul__(self, x: complex, /) -> Self: ...

    # keep in sync with `__radd__`
    @overload
    def __rmul__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...  # type: ignore[misc]
    @overload
    def __rmul__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __rmul__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __rmul__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __rmul__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __rmul__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __rmul__(self, x: complex, /) -> Self: ...

    # keep in sync with `__add__`
    @overload
    def __pow__(self, x: inexact[_NBitT1] | _Complex64_co, mod: None = None, /) -> Self: ...
    @overload
    def __pow__(self, x: inexact[_128Bit] | inexact[_96Bit], mod: None = None, /) -> clongdouble: ...
    @overload
    def __pow__(
        self: complexfloating[_128Bit] | complexfloating[_96Bit],
        x: number,
        mod: None = None,
        /,
    ) -> clongdouble: ...
    @overload
    def __pow__(  # type: ignore[overload-overlap]
        self: complexfloating[_64Bit],
        x: inexact[_64Bit] | inexact[_32Bit] | integer,
        mod: None = None,
        /,
    ) -> complex128: ...
    @overload
    def __pow__(
        self: complexfloating[_32Bit],
        x: number[_64Bit] | integer[_32Bit],
        mod: None = None,
        /,
    ) -> complex128: ...
    @overload
    def __pow__(
        self: complexfloating[_32Bit],
        x: inexact[_32Bit] | number[_16Bit] | number[_8Bit],
        mod: None = None,
        /,
    ) -> complex64: ...
    @overload
    def __pow__(self, x: complex, mod: None = None, /) -> Self: ...

    # keep in sync with `__radd__`
    @overload
    def __rpow__(self, x: inexact[_NBitT1] | _Complex64_co, mod: None = None, /) -> Self: ...
    @overload
    def __rpow__(self, x: inexact[_128Bit] | inexact[_96Bit], mod: None = None, /) -> clongdouble: ...
    @overload
    def __rpow__(
        self: complexfloating[_128Bit] | complexfloating[_96Bit],
        x: number,
        mod: None = None,
        /,
    ) -> clongdouble: ...
    @overload
    def __rpow__(  # type: ignore[overload-overlap]
        self: complexfloating[_64Bit],
        x: inexact[_64Bit] | inexact[_32Bit] | integer,
        mod: None = None,
        /,
    ) -> complex128: ...
    @overload
    def __rpow__(
        self: complexfloating[_32Bit],
        x: number[_64Bit] | integer[_32Bit],
        mod: None = None,
        /,
    ) -> complex128: ...
    @overload
    def __rpow__(
        self: complexfloating[_32Bit],
        x: inexact[_32Bit] | number[_16Bit] | number[_8Bit],
        mod: None = None,
        /,
    ) -> complex64: ...
    @overload
    def __rpow__(self, x: complex, mod: None = None, /) -> Self: ...

    # keep in sync with `__add__`
    @overload
    def __truediv__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...
    @overload
    def __truediv__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __truediv__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __truediv__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __truediv__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __truediv__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __truediv__(self, x: complex, /) -> Self: ...

    # keep in sync with `__radd__`
    @overload
    def __rtruediv__(self, x: inexact[_NBitT1] | _Complex64_co, /) -> Self: ...
    @overload
    def __rtruediv__(self, x: inexact[_128Bit] | inexact[_96Bit], /) -> clongdouble: ...
    @overload
    def __rtruediv__(self: complexfloating[_128Bit] | complexfloating[_96Bit], x: number, /) -> clongdouble: ...
    @overload
    def __rtruediv__(self: complexfloating[_64Bit], x: inexact[_64Bit] | inexact[_32Bit] | integer, /) -> complex128: ...  # type: ignore[overload-overlap]
    @overload
    def __rtruediv__(self: complexfloating[_32Bit], x: number[_64Bit] | integer[_32Bit], /) -> complex128: ...
    @overload
    def __rtruediv__(self: complexfloating[_32Bit], x: inexact[_32Bit] | number[_16Bit] | number[_8Bit], /) -> complex64: ...
    @overload
    def __rtruediv__(self, x: complex, /) -> Self: ...

    # NOTE: Without these, mypy will use the `misc` error code instead of `opererator`
    # when attempting to floordiv a complex
    @override
    def __floordiv__(self, x: Never, /) -> Never: ...
    @override
    def __rfloordiv__(self, x: Never, /) -> Never: ...

class complex128(complexfloating[_64Bit], complex):
    @property
    def itemsize(self) -> L[16]: ...
    @property
    def nbytes(self) -> L[16]: ...
    @property
    def real(self) -> float64: ...
    @property
    def imag(self) -> float64: ...

    #
    @overload
    def __new__(cls, real: _ConvertibleToComplex | None = 0, /) -> Self: ...
    @overload
    def __new__(cls, real: _ToReal = 0, imag: _ToImag = 0, /) -> Self: ...
    def __getnewargs__(self, /) -> tuple[float, float]: ...
    @override
    def __abs__(self, /) -> float64: ...
    @override
    def conjugate(self) -> Self: ...

class timedelta64(_IntegralMixin, generic[_TD64ItemT_co], Generic[_TD64ItemT_co]):
    @property
    def itemsize(self) -> L[8]: ...
    @property
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
    def __init__(self: timedelta64[int], value: _IntLike_co, format: _TimeUnitSpec[_IntTD64Unit] = ..., /) -> None: ...
    @overload
    def __init__(self: timedelta64[int], value: dt.timedelta, format: _TimeUnitSpec[_IntTimeUnit], /) -> None: ...
    @overload
    def __init__(
        self: timedelta64[dt.timedelta],
        value: dt.timedelta | _IntLike_co,
        format: _TimeUnitSpec[_NativeTD64Unit] = ...,
        /,
    ) -> None: ...
    @overload
    def __init__(self, value: _ConvertibleToTD64, format: _TimeUnitSpec = ..., /) -> None: ...

    # inherited at runtime from `signedinteger`
    def __class_getitem__(cls, type_arg: type | object, /) -> GenericAlias: ...

    # NOTE: Only a limited number of units support conversion
    # to builtin scalar types: `Y`, `M`, `ns`, `ps`, `fs`, `as`
    def __int__(self: timedelta64[int], /) -> int: ...
    def __float__(self: timedelta64[int], /) -> float: ...

    #
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __abs__(self, /) -> Self: ...

    #
    @overload
    def __add__(self, x: Self | _IntLike_co, /) -> Self: ...
    @overload
    def __add__(self, x: timedelta64[None], /) -> timedelta64[None]: ...
    @overload
    def __add__(self: timedelta64[None], x: _TD64Like_co, /) -> timedelta64[None]: ...
    @overload
    def __add__(self: timedelta64[int], x: timedelta64[int | dt.timedelta], /) -> timedelta64[int]: ...
    @overload
    def __add__(self: timedelta64[int], x: timedelta64, /) -> timedelta64[int | None]: ...
    @overload
    def __add__(self: timedelta64[dt.timedelta], x: _AnyDateOrTime, /) -> _AnyDateOrTime: ...
    __radd__ = __add__

    #
    @overload
    def __mul__(self: timedelta64[_AnyTD64Item], x: int | integer | bool_, /) -> timedelta64[_AnyTD64Item]: ...
    @overload
    def __mul__(self: timedelta64[_AnyTD64Item], x: float | floating, /) -> timedelta64[_AnyTD64Item | None]: ...
    @overload
    def __mul__(self, x: float | floating | integer | bool_, /) -> timedelta64: ...
    __rmul__ = __mul__

    #
    @overload
    def __sub__(self, b: Self | _IntLike_co, /) -> Self: ...
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
    def __rsub__(self, a: _IntLike_co, /) -> Self: ...  # type: ignore[misc]
    @overload
    def __rsub__(self, a: timedelta64[None], /) -> timedelta64[None]: ...
    @overload
    def __rsub__(self, a: datetime64[None], /) -> datetime64[None]: ...  # type: ignore[misc]
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
    def __truediv__(self, b: int | integer, /) -> Self: ...
    @overload
    def __truediv__(self, b: float | floating, /) -> timedelta64[_TD64ItemT_co | None]: ...
    @overload
    def __truediv__(self, b: float | floating | integer, /) -> timedelta64: ...
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
    def __floordiv__(self, b: int | integer, /) -> Self: ...
    @overload
    def __floordiv__(self, b: float | floating | integer, /) -> timedelta64[_TD64ItemT_co | None]: ...
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
    def __mod__(self: timedelta64[int], x: timedelta64[int | dt.timedelta], /) -> timedelta64[int | None]: ...
    @overload
    def __mod__(self: timedelta64[dt.timedelta], x: timedelta64[_AnyTD64Item], /) -> timedelta64[_AnyTD64Item | None]: ...  # type: ignore[overload-overlap]
    @overload
    def __mod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> dt.timedelta: ...
    @overload
    def __mod__(self, x: timedelta64[int], /) -> timedelta64[int | None]: ...
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
    def __divmod__(self: timedelta64[int], x: timedelta64[int | dt.timedelta], /) -> tuple[int64, timedelta64[int | None]]: ...
    @overload
    def __divmod__(  # type: ignore[overload-overlap]
        self: timedelta64[dt.timedelta],
        x: timedelta64[_AnyTD64Item],
        /,
    ) -> tuple[int64, timedelta64[_AnyTD64Item | None]]: ...
    @overload
    def __divmod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> tuple[int, dt.timedelta]: ...
    @overload
    def __divmod__(self, x: timedelta64[int], /) -> tuple[int64, timedelta64[int | None]]: ...
    @overload
    def __divmod__(self, x: timedelta64, /) -> tuple[int64, timedelta64]: ...

    # keep in sync with __rmod__
    @overload
    def __rdivmod__(self, x: timedelta64[None], /) -> tuple[int64, timedelta64[None]]: ...  # type: ignore[misc]
    @overload
    def __rdivmod__(self: timedelta64[L[0] | None], x: timedelta64, /) -> tuple[int64, timedelta64[None]]: ...
    @overload
    def __rdivmod__(self: timedelta64[dt.timedelta], x: dt.timedelta, /) -> tuple[int, dt.timedelta]: ...

    __lt__: _ComparisonOpLT[_TD64Like_co, _ArrayLikeTD64_co]
    __le__: _ComparisonOpLE[_TD64Like_co, _ArrayLikeTD64_co]
    __gt__: _ComparisonOpGT[_TD64Like_co, _ArrayLikeTD64_co]
    __ge__: _ComparisonOpGE[_TD64Like_co, _ArrayLikeTD64_co]

class datetime64(_RealMixin, generic[_DT64ItemT_co], Generic[_DT64ItemT_co]):
    @property
    def itemsize(self) -> L[8]: ...
    @property
    def nbytes(self) -> L[8]: ...

    #
    @overload
    def __init__(self, value: datetime64[_DT64ItemT_co], /) -> None: ...
    @overload
    def __init__(self: datetime64[_AnyDT64Arg], value: _AnyDT64Arg, /) -> None: ...
    @overload
    def __init__(self: datetime64[None], value: _NaTValue | None = ..., format: _TimeUnitSpec = ..., /) -> None: ...
    @overload
    def __init__(self: datetime64[dt.datetime], value: _DT64Now, format: _TimeUnitSpec[_NativeTimeUnit] = ..., /) -> None: ...
    @overload
    def __init__(self: datetime64[dt.date], value: _DT64Date, format: _TimeUnitSpec[_DateUnit] = ..., /) -> None: ...
    @overload
    def __init__(self: datetime64[int], value: int | bytes | str | dt.date, format: _TimeUnitSpec[_IntTimeUnit], /) -> None: ...
    @overload
    def __init__(
        self: datetime64[dt.datetime],
        value: int | bytes | str | dt.date,
        format: _TimeUnitSpec[_NativeTimeUnit],
        /,
    ) -> None: ...
    @overload
    def __init__(self: datetime64[dt.date], value: int | bytes | str | dt.date, format: _TimeUnitSpec[_DateUnit], /) -> None: ...
    @overload
    def __init__(self, value: bytes | str | dt.date | None, format: _TimeUnitSpec = ..., /) -> None: ...

    #
    @overload
    def __add__(self, x: int | integer | bool_, /) -> Self: ...
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
    __radd__ = __add__

    @overload
    def __sub__(self, x: int | integer | bool_, /) -> Self: ...
    @overload
    def __sub__(self, x: datetime64[None], /) -> timedelta64[None]: ...
    @overload
    def __sub__(self, x: timedelta64[None], /) -> datetime64[None]: ...
    @overload
    def __sub__(self: datetime64[_AnyDate], x: _AnyDate, /) -> dt.timedelta: ...
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
    def __rsub__(self: datetime64[_AnyDate], x: _AnyDate, /) -> dt.timedelta: ...

    __lt__: _ComparisonOpLT[datetime64, _ArrayLikeDT64_co]
    __le__: _ComparisonOpLE[datetime64, _ArrayLikeDT64_co]
    __gt__: _ComparisonOpGT[datetime64, _ArrayLikeDT64_co]
    __ge__: _ComparisonOpGE[datetime64, _ArrayLikeDT64_co]

@final
class flexible(_RealMixin, generic[_FlexItemT_co], Generic[_FlexItemT_co]):  # type: ignore[misc]
    @abc.abstractmethod
    def __init__(self, /, *args: Any, **kwargs: Any) -> None: ...

class void(flexible[bytes | tuple[Any, ...]]):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    @overload
    def __init__(self, value: _IntLike_co | bytes, /, dtype: None = None) -> None: ...
    @overload
    def __init__(self, value: Any, /, dtype: _DTypeLikeVoid) -> None: ...

    #
    @overload
    def __getitem__(self, key: str | CanIndex, /) -> Any: ...
    @overload
    def __getitem__(self, key: list[str], /) -> void: ...

    #
    def __setitem__(self, key: str | list[str] | CanIndex, value: ArrayLike, /) -> None: ...

    #
    def setfield(self, val: ArrayLike, dtype: DTypeLike, offset: int = ...) -> None: ...

class character(flexible[_CharacterItemT_co], Generic[_CharacterItemT_co]):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    @abc.abstractmethod
    def __init__(self, value: _CharacterItemT_co = ..., /) -> None: ...

class bytes_(character[bytes], bytes):  # type: ignore[misc]
    @overload
    def __new__(cls, o: object = ..., /) -> Self: ...
    @overload
    def __new__(cls, s: str, /, encoding: str, errors: str = ...) -> Self: ...

    #
    @overload
    def __init__(self, o: object = ..., /) -> None: ...
    @overload
    def __init__(self, s: str, /, encoding: str, errors: str = ...) -> None: ...

class str_(character[str], str):  # type: ignore[misc]
    @overload
    def __new__(cls, value: object = ..., /) -> Self: ...
    @overload
    def __new__(cls, value: bytes, /, encoding: str = ..., errors: str = ...) -> Self: ...

    #
    @overload
    def __init__(self, value: object = ..., /) -> None: ...
    @overload
    def __init__(self, value: bytes, /, encoding: str = ..., errors: str = ...) -> None: ...

# TODO(jorenham): concrete subtyping
# https://github.com/numpy/numtype/issues/136
int8: TypeAlias = signedinteger[_8Bit]
int16: TypeAlias = signedinteger[_16Bit]
int32: TypeAlias = signedinteger[_32Bit]
int64: TypeAlias = signedinteger[_64Bit]
intp: TypeAlias = signedinteger[_NBitIntP]
long: TypeAlias = signedinteger[_NBitLong]
longlong: TypeAlias = signedinteger[_NBitLongLong]

uint8: TypeAlias = unsignedinteger[_8Bit]
uint16: TypeAlias = unsignedinteger[_16Bit]
uint32: TypeAlias = unsignedinteger[_32Bit]
uint64: TypeAlias = unsignedinteger[_64Bit]
uintp: TypeAlias = unsignedinteger[_NBitIntP]
ulong: TypeAlias = unsignedinteger[_NBitLong]
ulonglong: TypeAlias = unsignedinteger[_NBitLongLong]

float16: TypeAlias = floating[_16Bit]
float32: TypeAlias = floating[_32Bit]
float96: TypeAlias = floating[_96Bit]
float128: TypeAlias = floating[_128Bit]
longdouble: TypeAlias = floating[_NBitLongDouble]

complex64: TypeAlias = complexfloating[_32Bit]
complex192: TypeAlias = complexfloating[_96Bit]
complex256: TypeAlias = complexfloating[_128Bit]
clongdouble: TypeAlias = complexfloating[_NBitLongDouble]

# NOTE: These should NOT be `Final` or a `TypeAlias`!
bool_ = bool
byte = int8
ubyte = uint8
short = int16
ushort = uint16
intc = int32
uintc = uint32
int_ = intp
uint = uintp
half = float16
single = float32
double = float64
csingle = complex64
cdouble = complex128

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
    default=Callable[Concatenate[Any, Any, ...], ndarray[Any, dtype[Any]]],
    covariant=True,
)
_AccumulateT_co = TypeVar(
    "_AccumulateT_co",
    bound=Callable[Concatenate[Never, ...], object],
    default=Callable[Concatenate[Any, ...], ndarray[Any, dtype[Any]]],
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
    def __qualname__(self) -> str: ...  # pyright: ignore[reportIncompatibleVariableOverride]
    @property
    def __doc__(self) -> str: ...  # type: ignore[override] # pyright: ignore[reportIncompatibleVariableOverride]

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
        dtypes: tuple[dtype[Any] | type | None, ...],
        *,
        signature: tuple[dtype[Any] | None, ...] | None = None,
        casting: _CastingKind | None = None,
        reduction: py_bool = False,
    ) -> tuple[dtype[Any], ...]: ...

# TODO(jorenham): individual ufunc signature annotations
# https://github.com/numpy/numtype/issues/230

absolute: Final[_ufunc_1_1] = ...
arccos: Final[_ufunc_1_1] = ...
arccosh: Final[_ufunc_1_1] = ...
arcsin: Final[_ufunc_1_1] = ...
arcsinh: Final[_ufunc_1_1] = ...
arctan: Final[_ufunc_1_1] = ...
arctanh: Final[_ufunc_1_1] = ...
bitwise_count: Final[_ufunc_1_1] = ...
cbrt: Final[_ufunc_1_1] = ...
ceil: Final[_ufunc_1_1] = ...
conjugate: Final[_ufunc_1_1] = ...
cos: Final[_ufunc_1_1] = ...
cosh: Final[_ufunc_1_1] = ...
deg2rad: Final[_ufunc_1_1] = ...
degrees: Final[_ufunc_1_1] = ...
exp: Final[_ufunc_1_1] = ...
exp2: Final[_ufunc_1_1] = ...
expm1: Final[_ufunc_1_1] = ...
fabs: Final[_ufunc_1_1] = ...
floor: Final[_ufunc_1_1] = ...
invert: Final[_ufunc_1_1] = ...
isfinite: Final[_ufunc_1_1] = ...
isinf: Final[_ufunc_1_1] = ...
isnan: Final[_ufunc_1_1] = ...
isnat: Final[_ufunc_1_1] = ...
log: Final[_ufunc_1_1] = ...
log2: Final[_ufunc_1_1] = ...
log10: Final[_ufunc_1_1] = ...
log1p: Final[_ufunc_1_1] = ...
logical_not: Final[_ufunc_1_1] = ...
negative: Final[_ufunc_1_1] = ...
positive: Final[_ufunc_1_1] = ...
rad2deg: Final[_ufunc_1_1] = ...
radians: Final[_ufunc_1_1] = ...
reciprocal: Final[_ufunc_1_1] = ...
rint: Final[_ufunc_1_1] = ...
sign: Final[_ufunc_1_1] = ...
signbit: Final[_ufunc_1_1] = ...
sin: Final[_ufunc_1_1] = ...
sinh: Final[_ufunc_1_1] = ...
spacing: Final[_ufunc_1_1] = ...
sqrt: Final[_ufunc_1_1] = ...
square: Final[_ufunc_1_1] = ...
tan: Final[_ufunc_1_1] = ...
tanh: Final[_ufunc_1_1] = ...
trunc: Final[_ufunc_1_1] = ...
abs = absolute
acos = arccos
acosh = arccosh
asin = arcsin
asinh = arcsinh
atan = arctan
atanh = arctanh
bitwise_not = invert
bitwise_invert = invert
conj = conjugate

frexp: Final[_ufunc_1_2] = ...
modf: Final[_ufunc_1_2] = ...

equal: Final[_ufunc_2_1[_Call21Bool]] = ...
not_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
greater: Final[_ufunc_2_1[_Call21Bool]] = ...
greater_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
less: Final[_ufunc_2_1[_Call21Bool]] = ...
less_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
add: Final[_ufunc_2_1] = ...
arctan2: Final[_ufunc_2_1] = ...
bitwise_and: Final[_ufunc_2_1] = ...
bitwise_or: Final[_ufunc_2_1] = ...
bitwise_xor: Final[_ufunc_2_1] = ...
copysign: Final[_ufunc_2_1] = ...
divide: Final[_ufunc_2_1] = ...
float_power: Final[_ufunc_2_1] = ...
floor_divide: Final[_ufunc_2_1] = ...
fmax: Final[_ufunc_2_1] = ...
fmin: Final[_ufunc_2_1] = ...
fmod: Final[_ufunc_2_1] = ...
gcd: Final[_ufunc_2_1] = ...
heaviside: Final[_ufunc_2_1] = ...
hypot: Final[_ufunc_2_1] = ...
lcm: Final[_ufunc_2_1] = ...
ldexp: Final[_ufunc_2_1] = ...
left_shift: Final[_ufunc_2_1] = ...
logaddexp: Final[_ufunc_2_1] = ...
logaddexp2: Final[_ufunc_2_1] = ...
logical_and: Final[_ufunc_2_1] = ...
logical_or: Final[_ufunc_2_1] = ...
logical_xor: Final[_ufunc_2_1] = ...
maximum: Final[_ufunc_2_1] = ...
minimum: Final[_ufunc_2_1] = ...
mod: Final[_ufunc_2_1] = ...
multiply: Final[_ufunc_2_1] = ...
nextafter: Final[_ufunc_2_1] = ...
power: Final[_ufunc_2_1] = ...
remainder: Final[_ufunc_2_1] = ...
right_shift: Final[_ufunc_2_1] = ...
subtract: Final[_ufunc_2_1] = ...
atan2 = arctan2
bitwise_left_shift = left_shift
bitwise_right_shift = right_shift
pow = power
true_divide = divide

divmod: Final[_ufunc_2_2] = ...

matmul: Final[_gufunc_2_1] = ...  # (n?, k), (k, m?) -> (n?, m?)
matvec: Final[_gufunc_2_1] = ...  # (m, n), (n) -> (m)
vecmat: Final[_gufunc_2_1] = ...  # (n), (n, m) -> (m)
vecdot: Final[_gufunc_2_1] = ...  # (n), (n) -> ()
