from collections.abc import Iterable
from typing import Any, Final, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy._typing import _SupportsArrayFunc as _Like

__all__ = ["require"]

###

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array[Any])
_ScalarT = TypeVar("_ScalarT", bound=np.generic[Any])

_Req: TypeAlias = L[
    "C", "C_CONTIGUOUS", "CONTIGUOUS",
    "F", "F_CONTIGUOUS", "FORTRAN",
    "A", "ALIGNED",
    "W", "WRITEABLE",
    "O", "OWNDATA",
]  # fmt: skip
_ReqE: TypeAlias = L[_Req, "E", "ENSUREARRAY"]
_ToReqs: TypeAlias = _Req | Iterable[_Req]
_ToReqsE: TypeAlias = _ReqE | Iterable[_ReqE]

###

POSSIBLE_FLAGS: Final[dict[_ReqE, L["C", "F", "A", "W", "O", "E"]]]

@overload
def require(
    a: _ArrayT, dtype: None = None, requirements: _ToReqs | None = None, *, like: _Like | None = None
) -> _ArrayT: ...
@overload
def require(
    a: _nt.ToBool_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.bool]: ...
@overload
def require(
    a: _nt.ToInt_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.intp]: ...
@overload
def require(
    a: _nt.ToFloat64_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.float64]: ...
@overload
def require(
    a: _nt.ToComplex128_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.complex128]: ...
@overload
def require(
    a: _nt.ToBytes_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.bytes_]: ...
@overload
def require(
    a: _nt.ToStr_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.str_]: ...
@overload
def require(
    a: _nt.ToObject_nd, dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[np.object_]: ...
@overload
def require(
    a: _nt._ToArray_nd[_ScalarT], dtype: None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def require(
    a: object, dtype: _nt._ToDType[_ScalarT], requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[_ScalarT]: ...
@overload
def require(
    a: object, dtype: _nt.ToDType | None = None, requirements: _ToReqsE | None = None, *, like: _Like | None = None
) -> _nt.Array[Any]: ...
