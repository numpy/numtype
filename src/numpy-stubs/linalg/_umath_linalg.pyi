from collections.abc import Callable, Sequence
from typing import Any, Concatenate, Final, Protocol, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import TypeVar, Unpack

import _numtype as _nt
import numpy as np
from numpy._core.umath import (
    _AccumulateE,
    _AtE,
    _KwargsCommon,
    _Out1,
    _OuterE,
    _ReduceAtE,
    _ReduceE,
    _Tuple2,
    _gufunc21,
)
from numpy._typing import ArrayLike, DTypeLike

###

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_ArrayT1 = TypeVar("_ArrayT1", bound=_nt.Array)
_ArrayT2 = TypeVar("_ArrayT2", bound=_nt.Array)

_CallT11G = TypeVar("_CallT11G", bound=Callable[Concatenate[Any, ...], object], default=_Call11)
_CallT12G = TypeVar("_CallT12G", bound=Callable[Concatenate[Any, ...], object], default=_Call12)

_GUFunc1: TypeAlias = np.ufunc[_CallT11G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE]
_GUFunc2: TypeAlias = np.ufunc[_CallT12G, _AtE, _ReduceE, _ReduceAtE, _AccumulateE, _OuterE]

@type_check_only
class _Kwargs2(_KwargsCommon, total=False):
    signature: _Tuple2[DTypeLike] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

@type_check_only
class _Kwargs3(_KwargsCommon, total=False):
    signature: tuple[DTypeLike | None, DTypeLike | None, DTypeLike | None] | str | None
    axes: Sequence[_Tuple2[SupportsIndex]]
    axis: SupportsIndex

@type_check_only
class _Call11(Protocol):
    @overload
    def __call__(
        self, x: ArrayLike, /, out: _Out1[_ArrayT], *, dtype: None = None, **kwds: Unpack[_Kwargs2]
    ) -> _ArrayT: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        /,
        out: _Out1[_nt.Array | None] = None,
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs2],
    ) -> Any: ...

@type_check_only
class _Call12(Protocol):
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        out: _Tuple2[None] = (None, None),
        *,
        dtype: DTypeLike | None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[Any, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[None, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, None],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None = None,
        out2: None = None,
        /,
        *,
        out: tuple[_ArrayT1, _ArrayT2],
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: None,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[Any, _ArrayT2]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: None,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, Any]: ...
    @overload
    def __call__(
        self,
        x: ArrayLike,
        out1: _ArrayT1,
        out2: _ArrayT2,
        /,
        *,
        out: _Tuple2[None] = (None, None),
        dtype: None = None,
        **kwds: Unpack[_Kwargs3],
    ) -> tuple[_ArrayT1, _ArrayT2]: ...

###

__version__: Final[str] = ...
_ilp64: Final[bool] = ...

# (m,m) -> ()
det: Final[_GUFunc1] = ...
# (m,m) -> (m)
cholesky_lo: Final[_GUFunc1] = ...
cholesky_up: Final[_GUFunc1] = ...
eigvals: Final[_GUFunc1] = ...
eigvalsh_lo: Final[_GUFunc1] = ...
eigvalsh_up: Final[_GUFunc1] = ...
# (m,m) -> (m,m)
inv: Final[_GUFunc1] = ...
# (m,n) -> (p)
qr_r_raw: Final[_GUFunc1] = ...
svd: Final[_GUFunc1] = ...

# (m,m) -> (), ()
slogdet: Final[_GUFunc2] = ...
# (m,m) -> (m), (m,m)
eig: Final[_GUFunc2] = ...
eigh_lo: Final[_GUFunc2] = ...
eigh_up: Final[_GUFunc2] = ...

# (m,n), (n) -> (m,m)
qr_complete: Final[_gufunc21] = ...
# (m,n), (k) -> (m,k)
qr_reduced: Final[_gufunc21] = ...
# (m,m), (m,n) -> (m,n)
solve: Final[_gufunc21] = ...
# (m,m), (m) -> (m)
solve1: Final[_gufunc21] = ...

# (m,n) -> (m,m), (p), (n,n)
svd_f: Final[np.ufunc] = ...
# (m,n) -> (m,p), (p), (p,n)
svd_s: Final[np.ufunc] = ...

# (m,n), (m,k), () -> (n,k), (k), (), (p)
lstsq: Final[np.ufunc] = ...
