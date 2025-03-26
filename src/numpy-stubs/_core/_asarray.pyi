from collections.abc import Iterable
from typing import Any, Final, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import ToBool_nd, ToBytes_nd, ToComplex128_nd, ToFloat64_nd, ToInt_nd, ToObject_nd, ToStr_nd
from numpy._typing import DTypeLike, NDArray, _ArrayLike, _DTypeLike, _SupportsArrayFunc as _Like

__all__ = ["require"]

###

_ArrayT = TypeVar("_ArrayT", bound=NDArray[Any])
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
    a: _ArrayT,
    dtype: None = None,
    requirements: _ToReqs | None = None,
    *,
    like: _Like | None = None,
) -> _ArrayT: ...
@overload
def require(
    a: ToBool_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.bool]: ...
@overload
def require(
    a: ToInt_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.intp]: ...
@overload
def require(
    a: ToFloat64_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.float64]: ...
@overload
def require(
    a: ToComplex128_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.complex128]: ...
@overload
def require(
    a: ToBytes_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.bytes_]: ...
@overload
def require(
    a: ToStr_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.str_]: ...
@overload
def require(
    a: ToObject_nd,
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[np.object_]: ...
@overload
def require(
    a: _ArrayLike[_ScalarT],
    dtype: None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def require(
    a: object,
    dtype: _DTypeLike[_ScalarT],
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[_ScalarT]: ...
@overload
def require(
    a: object,
    dtype: DTypeLike | None = None,
    requirements: _ToReqsE | None = None,
    *,
    like: _Like | None = None,
) -> NDArray[Any]: ...
