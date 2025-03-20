from typing import TypeAlias, TypeVar
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
Array: TypeAlias = np.ndarray[_ShapeT, np.dtype[_ScalarT]]
Array1D: TypeAlias = Array[tuple[int], _ScalarT]

###

f0: float
f0_1d: list[float]

f8_1d: Array1D[np.float64]
f8_nd: npt.NDArray[np.float64]
f16_1d: Array1D[np.longdouble]
f16_nd: npt.NDArray[np.longdouble]

c8_1d: Array1D[np.complex64]
c8_nd: npt.NDArray[np.complex64]
c16_1d: Array1D[np.complex128]
c16_nd: npt.NDArray[np.complex128]
c32_1d: Array1D[np.clongdouble]
c32_nd: npt.NDArray[np.clongdouble]

###

# keep in sync with `ifftshift` (same signature)
assert_type(np.fft.fftshift(f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.fftshift(f0_1d, axes=0), npt.NDArray[np.floating])

assert_type(np.fft.ifftshift(f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.ifftshift(f0_1d, axes=0), npt.NDArray[np.floating])

###

# keep in sync with `rfftfreq` (same signature)
assert_type(np.fft.fftfreq(5, 0.1), Array1D[np.float64])
assert_type(np.fft.fftfreq(5, f8_1d), Array1D[np.float64])
assert_type(np.fft.fftfreq(5, f16_1d), Array1D[np.longdouble])
assert_type(np.fft.fftfreq(5, 0.1j), Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c8_1d), Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c16_1d), Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c32_1d), Array1D[np.clongdouble])
assert_type(np.fft.fftfreq(5, f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.fftfreq(5, f16_nd), npt.NDArray[np.longdouble])
assert_type(np.fft.fftfreq(5, c8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.fftfreq(5, c16_nd), npt.NDArray[np.complex128])
assert_type(np.fft.fftfreq(5, c32_nd), npt.NDArray[np.clongdouble])

assert_type(np.fft.rfftfreq(5, 0.1), Array1D[np.float64])
assert_type(np.fft.rfftfreq(5, f8_1d), Array1D[np.float64])
assert_type(np.fft.rfftfreq(5, f16_1d), Array1D[np.longdouble])
assert_type(np.fft.rfftfreq(5, 0.1j), Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c8_1d), Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c16_1d), Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c32_1d), Array1D[np.clongdouble])
assert_type(np.fft.rfftfreq(5, f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.rfftfreq(5, f16_nd), npt.NDArray[np.longdouble])
assert_type(np.fft.rfftfreq(5, c8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.rfftfreq(5, c16_nd), npt.NDArray[np.complex128])
assert_type(np.fft.rfftfreq(5, c32_nd), npt.NDArray[np.clongdouble])

###

assert_type(np.fft.fft(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.ifft(f8_nd, axis=1), npt.NDArray[np.complex128])
assert_type(np.fft.rfft(f8_nd, n=None), npt.NDArray[np.complex128])
assert_type(np.fft.irfft(f8_nd, norm="ortho"), npt.NDArray[np.float64])
assert_type(np.fft.hfft(f8_nd, n=2), npt.NDArray[np.float64])
assert_type(np.fft.ihfft(f8_nd), npt.NDArray[np.complex128])

assert_type(np.fft.fftn(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.ifftn(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.rfftn(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.irfftn(f8_nd), npt.NDArray[np.float64])

assert_type(np.fft.rfft2(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.ifft2(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.fft2(f8_nd), npt.NDArray[np.complex128])
assert_type(np.fft.irfft2(f8_nd), npt.NDArray[np.float64])
