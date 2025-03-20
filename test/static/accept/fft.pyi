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
assert_type(np.fft.fftshift([False, True]), Array1D[np.bool])
assert_type(np.fft.fftshift([1, 2]), Array1D[np.intp])
assert_type(np.fft.fftshift([0.1, 0.2]), Array1D[np.float64])
assert_type(np.fft.fftshift([1j, 2j], axes=0), Array1D[np.complex128])
assert_type(np.fft.fftshift(["a", "b"], axes=(0,)), Array1D[np.str_])
assert_type(np.fft.fftshift([b"a", b"b"], axes=(0,)), Array1D[np.bytes_])
assert_type(np.fft.fftshift([[[False, True]]]), npt.NDArray[np.bool])
assert_type(np.fft.fftshift([[[1, 2]]]), npt.NDArray[np.intp])
assert_type(np.fft.fftshift([[[0.1, 0.2]]]), npt.NDArray[np.float64])
assert_type(np.fft.fftshift([[[1j, 2j]]]), npt.NDArray[np.complex128])
assert_type(np.fft.fftshift([[["a", "b"]]]), npt.NDArray[np.str_])
assert_type(np.fft.fftshift([[[b"a", b"b"]]]), npt.NDArray[np.bytes_])
assert_type(np.fft.fftshift(f8_1d), Array1D[np.float64])
assert_type(np.fft.fftshift(f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.fftshift(c8_1d), Array1D[np.complex64])
assert_type(np.fft.fftshift(c32_nd), npt.NDArray[np.clongdouble])

assert_type(np.fft.ifftshift([False, True]), Array1D[np.bool])
assert_type(np.fft.ifftshift([1, 2]), Array1D[np.intp])
assert_type(np.fft.ifftshift([0.1, 0.2]), Array1D[np.float64])
assert_type(np.fft.ifftshift([1j, 2j], axes=0), Array1D[np.complex128])
assert_type(np.fft.ifftshift(["a", "b"], axes=(0,)), Array1D[np.str_])
assert_type(np.fft.ifftshift([b"a", b"b"], axes=(0,)), Array1D[np.bytes_])
assert_type(np.fft.ifftshift([[[False, True]]]), npt.NDArray[np.bool])
assert_type(np.fft.ifftshift([[[1, 2]]]), npt.NDArray[np.intp])
assert_type(np.fft.ifftshift([[[0.1, 0.2]]]), npt.NDArray[np.float64])
assert_type(np.fft.ifftshift([[[1j, 2j]]]), npt.NDArray[np.complex128])
assert_type(np.fft.ifftshift([[["a", "b"]]]), npt.NDArray[np.str_])
assert_type(np.fft.ifftshift([[[b"a", b"b"]]]), npt.NDArray[np.bytes_])
assert_type(np.fft.ifftshift(f8_1d), Array1D[np.float64])
assert_type(np.fft.ifftshift(f8_nd), npt.NDArray[np.float64])
assert_type(np.fft.ifftshift(c8_1d), Array1D[np.complex64])
assert_type(np.fft.ifftshift(c32_nd), npt.NDArray[np.clongdouble])

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
