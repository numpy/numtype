from typing_extensions import deprecated

import _numtype as _nt
from numpy._typing import ArrayLike, _ShapeLike

from ._helper import _Device, _Int, integer_types as integer_types

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

###

@deprecated("Please use `numpy.fft.fftshift` instead.")
def fftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> _nt.Array: ...
@deprecated("Please use `numpy.fft.ifftshift` instead.")
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> _nt.Array: ...
@deprecated("Please use `numpy.fft.fftfreq` instead.")
def fftfreq(n: _Int, d: ArrayLike = 1.0, device: _Device | None = None) -> _nt.Array: ...
@deprecated("Please use `numpy.fft.rfftfreq` instead.")
def rfftfreq(n: _Int, d: ArrayLike = 1.0, device: _Device | None = None) -> _nt.Array: ...
