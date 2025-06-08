from typing import Any, Final, TypedDict, type_check_only

import _numtype as _nt
import numpy as np

from ._linalg import fortran_int

###

@type_check_only
class _GELSD(TypedDict):
    m: int
    n: int
    nrhs: int
    lda: int
    ldb: int
    rank: int
    lwork: int
    info: int

@type_check_only
class _DGELSD(_GELSD):
    dgelsd_: int
    rcond: float

@type_check_only
class _ZGELSD(_GELSD):
    zgelsd_: int

@type_check_only
class _GEQRF(TypedDict):
    m: int
    n: int
    lda: int
    lwork: int
    info: int

@type_check_only
class _DGEQRF(_GEQRF):
    dgeqrf_: int

@type_check_only
class _ZGEQRF(_GEQRF):
    zgeqrf_: int

@type_check_only
class _DORGQR(TypedDict):
    dorgqr_: int
    info: int

@type_check_only
class _ZUNGQR(TypedDict):
    zungqr_: int
    info: int

###

_ilp64: Final[bool] = ...

class LapackError(Exception): ...

def dgelsd(
    m: int,
    n: int,
    nrhs: int,
    a: _nt.Array[np.float64],
    lda: int,
    b: _nt.Array[np.float64],
    ldb: int,
    s: _nt.Array[np.float64],
    rcond: float,
    rank: int,
    work: _nt.Array[np.float64],
    lwork: int,
    iwork: _nt.Array[fortran_int],
    info: int,
) -> _DGELSD: ...
def zgelsd(
    m: int,
    n: int,
    nrhs: int,
    a: _nt.Array[np.complex128],
    lda: int,
    b: _nt.Array[np.complex128],
    ldb: int,
    s: _nt.Array[np.float64],
    rcond: float,
    rank: int,
    work: _nt.Array[np.complex128],
    lwork: int,
    rwork: _nt.Array[np.float64],
    iwork: _nt.Array[fortran_int],
    info: int,
) -> _ZGELSD: ...

#
def dgeqrf(
    m: int,
    n: int,
    a: _nt.Array[np.float64],  # in/out, shape: (lda, n)
    lda: int,
    tau: _nt.Array[np.float64],  # out, shape: (min(m, n),)
    work: _nt.Array[np.float64],  # out, shape: (max(1, lwork),)
    lwork: int,
    info: int,  # out
) -> _DGEQRF: ...
def zgeqrf(
    m: int,
    n: int,
    a: _nt.Array[np.complex128],  # in/out, shape: (lda, n)
    lda: int,
    tau: _nt.Array[np.complex128],  # out, shape: (min(m, n),)
    work: _nt.Array[np.complex128],  # out, shape: (max(1, lwork),)
    lwork: int,
    info: int,  # out
) -> _ZGEQRF: ...

#
def dorgqr(
    m: int,  # >=0
    n: int,  # m >= n >= 0
    k: int,  # n >= k >= 0
    a: _nt.Array[np.float64],  # in/out, shape: (lda, n)
    lda: int,  # >= max(1, m)
    tau: _nt.Array[np.float64],  # in, shape: (k,)
    work: _nt.Array[np.float64],  # out, shape: (max(1, lwork),)
    lwork: int,
    info: int,  # out
) -> _DORGQR: ...
def zungqr(
    m: int,
    n: int,
    k: int,
    a: _nt.Array[np.complex128],
    lda: int,
    tau: _nt.Array[np.complex128],
    work: _nt.Array[np.complex128],
    lwork: int,
    info: int,
) -> _ZUNGQR: ...

#
def xerbla(srname: Any, info: int) -> None: ...
