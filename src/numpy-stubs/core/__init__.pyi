from numpy import _core as _core  # noqa: ICN003
from numpy._core import (
    # _dtype,
    # _dtype_ctypes,
    _internal,
    _multiarray_umath,
    # TODO(jorenham):
    # add mirror modules of `_core` in the `core` namespace
    arrayprint,
    defchararray,
    einsumfunc,
    fromnumeric,
    function_base,
    getlimits,
    multiarray,
    numeric,
    numerictypes,
    # overrides,
    records,
    shape_base,
    umath,
)

__all__ = [
    # "_dtype",
    # "_dtype_ctypes",
    "_internal",
    "_multiarray_umath",
    "arrayprint",
    "defchararray",
    "einsumfunc",
    "fromnumeric",
    "function_base",
    "getlimits",
    "multiarray",
    "numeric",
    "numerictypes",
    # "overrides",
    "records",
    "shape_base",
    "umath",
]

# TODO(jorenham): stub `_core.overrides`
# https://github.com/numpy/numtype/issues/48

# TODO(jorenham): stub `_core._dtype_ctypes`
# https://github.com/numpy/numtype/issues/54

# TODO(jorenham): stub `_core._dtype`
# https://github.com/numpy/numtype/issues/55
