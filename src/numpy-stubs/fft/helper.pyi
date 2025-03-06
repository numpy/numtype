from typing import Any
from typing_extensions import deprecated

from numpy._typing import ArrayLike, NDArray, _ShapeLike

from ._helper import _Device, _IntLike, integer_types as integer_types

__all__ = ["fftfreq", "fftshift", "ifftshift", "rfftfreq"]

###

@deprecated("Please use `numpy.fft.fftshift` instead.")
def fftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> NDArray[Any]: ...
@deprecated("Please use `numpy.fft.ifftshift` instead.")
def ifftshift(x: ArrayLike, axes: _ShapeLike | None = None) -> NDArray[Any]: ...
@deprecated("Please use `numpy.fft.fftfreq` instead.")
def fftfreq(n: _IntLike, d: ArrayLike = 1.0, device: _Device = None) -> NDArray[Any]: ...
@deprecated("Please use `numpy.fft.rfftfreq` instead.")
def rfftfreq(n: _IntLike, d: ArrayLike = 1.0, device: _Device = None) -> NDArray[Any]: ...
