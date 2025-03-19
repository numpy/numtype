from typing import Final

from numpy._typing._ufunc import (
    _Call11Bool,
    _Call11Isnat,
    _Call11Logical,
    _Call21Bool,
    _Call21Logical,
    _gufunc_2_1,
    _ufunc_1_1,
    _ufunc_1_2,
    _ufunc_2_1,
    _ufunc_2_2,
)

from . import _multiarray_umath as _multiarray_umath
from ._multiarray_umath import (
    _UFUNC_API as _UFUNC_API,
    _add_newdoc_ufunc as _add_newdoc_ufunc,
    _center as _center,
    _expandtabs as _expandtabs,
    _expandtabs_length as _expandtabs_length,
    _extobj_contextvar as _extobj_contextvar,
    _get_extobj_dict as _get_extobj_dict,
    _ljust as _ljust,
    _lstrip_chars as _lstrip_chars,
    _lstrip_whitespace as _lstrip_whitespace,
    _make_extobj as _make_extobj,
    _ones_like as _ones_like,
    _partition as _partition,
    _partition_index as _partition_index,
    _replace as _replace,
    _rjust as _rjust,
    _rpartition as _rpartition,
    _rpartition_index as _rpartition_index,
    _rstrip_chars as _rstrip_chars,
    _rstrip_whitespace as _rstrip_whitespace,
    _strip_chars as _strip_chars,
    _strip_whitespace as _strip_whitespace,
    _zfill as _zfill,
    e,
    euler_gamma,
    frompyfunc,
    isalnum as isalnum,
    isalpha as isalpha,
    isdecimal as isdecimal,
    isdigit as isdigit,
    islower as islower,
    isnumeric as isnumeric,
    isspace as isspace,
    istitle as istitle,
    isupper as isupper,
    pi,
    str_len as str_len,
)

__all__ = [
    "absolute",
    "add",
    "arccos",
    "arccosh",
    "arcsin",
    "arcsinh",
    "arctan",
    "arctan2",
    "arctanh",
    "bitwise_and",
    "bitwise_count",
    "bitwise_or",
    "bitwise_xor",
    "cbrt",
    "ceil",
    "conj",
    "conjugate",
    "copysign",
    "cos",
    "cosh",
    "deg2rad",
    "degrees",
    "divide",
    "divmod",
    "e",
    "equal",
    "euler_gamma",
    "exp",
    "exp2",
    "expm1",
    "fabs",
    "float_power",
    "floor",
    "floor_divide",
    "fmax",
    "fmin",
    "fmod",
    "frexp",
    "frompyfunc",
    "gcd",
    "greater",
    "greater_equal",
    "heaviside",
    "hypot",
    "invert",
    "isfinite",
    "isinf",
    "isnan",
    "isnat",
    "lcm",
    "ldexp",
    "left_shift",
    "less",
    "less_equal",
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
    "matvec",
    "maximum",
    "minimum",
    "mod",
    "modf",
    "multiply",
    "negative",
    "nextafter",
    "not_equal",
    "pi",
    "positive",
    "power",
    "rad2deg",
    "radians",
    "reciprocal",
    "remainder",
    "right_shift",
    "rint",
    "sign",
    "signbit",
    "sin",
    "sinh",
    "spacing",
    "sqrt",
    "square",
    "subtract",
    "tan",
    "tanh",
    "true_divide",
    "trunc",
    "vecdot",
    "vecmat",
]

###

# TODO(jorenham): Individual ufunc signature annotations
# https://github.com/numpy/numtype/issues/230

# Signature notation:
# - {_} => union type
# - [u] => BHILQ
# - [i] => bhilq
# - [f] => efdg
# - [c] => FDG
# - $1  => type of first argument

###
# 1 in, 1 out

# {Mm} -> ?
isnat: Final[_ufunc_1_1[_Call11Isnat]] = ...

# {[f]} -> ?
signbit: Final[_ufunc_1_1] = ...
isfinite: Final[_ufunc_1_1[_Call11Bool]] = ...
isinf: Final[_ufunc_1_1[_Call11Bool]] = ...

# {[f]T} -> ?
isnan: Final[_ufunc_1_1[_Call11Bool]] = ...

# {?[uifc]O} -> ?
# O -> O
logical_not: Final[_ufunc_1_1[_Call11Logical]] = ...

# {[ui]} -> B
# O -> O
bitwise_count: Final[_ufunc_1_1] = ...

# {[f]} -> $1
spacing: Final[_ufunc_1_1] = ...

# {[f]O} -> $1
cbrt: Final[_ufunc_1_1] = ...
deg2rad: Final[_ufunc_1_1] = ...
degrees: Final[_ufunc_1_1] = ...
fabs: Final[_ufunc_1_1] = ...
rad2deg: Final[_ufunc_1_1] = ...
radians: Final[_ufunc_1_1] = ...

# {[fc]O} -> $1
arccos: Final[_ufunc_1_1] = ...
arccosh: Final[_ufunc_1_1] = ...
arcsin: Final[_ufunc_1_1] = ...
arcsinh: Final[_ufunc_1_1] = ...
arctan: Final[_ufunc_1_1] = ...
arctanh: Final[_ufunc_1_1] = ...
cos: Final[_ufunc_1_1] = ...
cosh: Final[_ufunc_1_1] = ...
exp: Final[_ufunc_1_1] = ...
exp2: Final[_ufunc_1_1] = ...
expm1: Final[_ufunc_1_1] = ...
log: Final[_ufunc_1_1] = ...
log2: Final[_ufunc_1_1] = ...
log10: Final[_ufunc_1_1] = ...
log1p: Final[_ufunc_1_1] = ...
rint: Final[_ufunc_1_1] = ...
sin: Final[_ufunc_1_1] = ...
sinh: Final[_ufunc_1_1] = ...
sqrt: Final[_ufunc_1_1] = ...
tan: Final[_ufunc_1_1] = ...
tanh: Final[_ufunc_1_1] = ...

# {?[ui]O} -> $1
invert: Final[_ufunc_1_1] = ...

# {?[uif]O} -> $1
ceil: Final[_ufunc_1_1] = ...
floor: Final[_ufunc_1_1] = ...
trunc: Final[_ufunc_1_1] = ...

# {?[uif]Om} -> $1
# F -> f
# D -> d
# G -> g
absolute: Final[_ufunc_1_1] = ...

# {[uifc]O} -> $1
conjugate: Final[_ufunc_1_1] = ...
conj = conjugate
reciprocal: Final[_ufunc_1_1] = ...
square: Final[_ufunc_1_1] = ...

# {[uifc]mO} -> $1
negative: Final[_ufunc_1_1] = ...
positive: Final[_ufunc_1_1] = ...
sign: Final[_ufunc_1_1] = ...

###
# 1-in, 2-out

# {[f]} -> $1, i
frexp: Final[_ufunc_1_2] = ...

# {[f]} -> $1, $1
modf: Final[_ufunc_1_2] = ...

###
# 2-in, 1-out

# {?[uifc]OSUTV}, $1 -> ?
logical_and: Final[_ufunc_2_1[_Call21Logical]] = ...
logical_or: Final[_ufunc_2_1[_Call21Logical]] = ...
logical_xor: Final[_ufunc_2_1[_Call21Logical]] = ...

# {?[uifc]MmOSUT}, $1 -> ?, (also accepts dtype: O)
equal: Final[_ufunc_2_1[_Call21Bool]] = ...
not_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
greater: Final[_ufunc_2_1[_Call21Bool]] = ...
greater_equal: Final[_ufunc_2_1[_Call21Bool]] = ...
less: Final[_ufunc_2_1[_Call21Bool]] = ...
less_equal: Final[_ufunc_2_1[_Call21Bool]] = ...

# {[f]}, {il} -> $1
ldexp: Final[_ufunc_2_1] = ...

# {dgDG}, $1 -> $1
float_power: Final[_ufunc_2_1] = ...

# {[f]}, $1 -> $1
copysign: Final[_ufunc_2_1] = ...
heaviside: Final[_ufunc_2_1] = ...
logaddexp: Final[_ufunc_2_1] = ...
logaddexp2: Final[_ufunc_2_1] = ...
nextafter: Final[_ufunc_2_1] = ...

# {[f]O}, $1 -> $1
arctan2: Final[_ufunc_2_1] = ...
hypot: Final[_ufunc_2_1] = ...

# {[fc]mO}, $1 -> $1
divide: Final[_ufunc_2_1] = ...
true_divide = divide

# {[ui]O}, $1 -> $1
gcd: Final[_ufunc_2_1] = ...
lcm: Final[_ufunc_2_1] = ...
left_shift: Final[_ufunc_2_1] = ...
right_shift: Final[_ufunc_2_1] = ...

# {?[ui]O}, $1 -> $1
bitwise_and: Final[_ufunc_2_1] = ...
bitwise_or: Final[_ufunc_2_1] = ...
bitwise_xor: Final[_ufunc_2_1] = ...

# {[uif]O}, $1 -> $1
fmod: Final[_ufunc_2_1] = ...

# {[uif]mO}, $1 -> $1
floor_divide: Final[_ufunc_2_1] = ...
remainder: Final[_ufunc_2_1] = ...
mod = remainder

# {[uifc]O}, $1 -> $1
power: Final[_ufunc_2_1] = ...

# {?[uifc]O}, $1 -> $1
matmul: Final[_gufunc_2_1] = ...  # (n?, k), (k, m?) -> (n?, m?)
matvec: Final[_gufunc_2_1] = ...  # (m, n), (n) -> (m)
vecdot: Final[_gufunc_2_1] = ...  # (n), (n) -> ()
vecmat: Final[_gufunc_2_1] = ...  # (n), (n, m) -> (m)

# {?[uifc]mO}, $1 -> $1
multiply: Final[_ufunc_2_1] = ...
subtract: Final[_ufunc_2_1] = ...

# {?[uifc]MmO}, $1 -> $1
fmax: Final[_ufunc_2_1] = ...
fmin: Final[_ufunc_2_1] = ...

# {?[uifc]MmOT}, $1 -> $1
maximum: Final[_ufunc_2_1] = ...
minimum: Final[_ufunc_2_1] = ...

# {?[uifc]MmOSUT}, $1 -> $1
add: Final[_ufunc_2_1] = ...

###
# 2-in, 2-out

# {[uif]}, $1 -> $1, $1
# m, m -> q, m
divmod: Final[_ufunc_2_2] = ...
