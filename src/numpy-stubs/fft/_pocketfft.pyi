from collections.abc import Sequence
from typing import Literal as L, TypeAlias

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLikeNumber_co

__all__ = [
    "fft",
    "fft2",
    "fftn",
    "hfft",
    "ifft",
    "ifft2",
    "ifftn",
    "ihfft",
    "irfft",
    "irfft2",
    "irfftn",
    "rfft",
    "rfft2",
    "rfftn",
]

_NormKind: TypeAlias = L["backward", "ortho", "forward"] | None

def fft(
    a: npt.ArrayLike,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def ifft(
    a: npt.ArrayLike,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def rfft(
    a: npt.ArrayLike,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def irfft(
    a: npt.ArrayLike,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...

# Input array must be compatible with `np.conjugate`
def hfft(
    a: _ArrayLikeNumber_co,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...
def ihfft(
    a: npt.ArrayLike,
    n: int | None = None,
    axis: int = -1,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def fftn(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def ifftn(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def rfftn(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def irfftn(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...
def fft2(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def ifft2(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def rfft2(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.complex128] | None = None,
) -> _nt.Array[np.complex128]: ...
def irfft2(
    a: npt.ArrayLike,
    s: Sequence[int] | None = None,
    axes: Sequence[int] | None = None,
    norm: _NormKind = None,
    out: _nt.Array[np.float64] | None = None,
) -> _nt.Array[np.float64]: ...
