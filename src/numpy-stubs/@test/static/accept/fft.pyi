from typing import assert_type

import _numtype as _nt
import numpy as np

###

f8_1d: _nt.Array1D[np.float64]
f8_nd: _nt.Array[np.float64]
f16_1d: _nt.Array1D[np.longdouble]
f16_nd: _nt.Array[np.longdouble]

c8_1d: _nt.Array1D[np.complex64]
c8_nd: _nt.Array[np.complex64]
c16_1d: _nt.Array1D[np.complex128]
c16_nd: _nt.Array[np.complex128]
c32_1d: _nt.Array1D[np.clongdouble]
c32_nd: _nt.Array[np.clongdouble]

b_1d: list[bool]
i_1d: list[int]
f_1d: list[float]
c_1d: list[complex]
S_1d: list[bytes]
U_1d: list[str]

b_3d: list[list[list[bool]]]
i_3d: list[list[list[int]]]
f_3d: list[list[list[float]]]
c_3d: list[list[list[complex]]]
S_3d: list[list[list[bytes]]]
U_3d: list[list[list[str]]]

###

# keep in sync with `ifftshift` (same signature)
assert_type(np.fft.fftshift(b_1d), _nt.Array1D[np.bool])
assert_type(np.fft.fftshift(i_1d), _nt.Array1D[np.intp])
assert_type(np.fft.fftshift(f_1d), _nt.Array1D[np.float64])
assert_type(np.fft.fftshift(c_1d, axes=0), _nt.Array1D[np.complex128])
assert_type(np.fft.fftshift(U_1d, axes=(0,)), _nt.Array1D[np.str_])
assert_type(np.fft.fftshift(S_1d, axes=(0,)), _nt.Array1D[np.bytes_])
assert_type(np.fft.fftshift(b_3d), _nt.Array[np.bool])
assert_type(np.fft.fftshift(i_3d), _nt.Array[np.intp])
assert_type(np.fft.fftshift(f_3d), _nt.Array[np.float64])
assert_type(np.fft.fftshift(c_3d), _nt.Array[np.complex128])
assert_type(np.fft.fftshift(U_3d), _nt.Array[np.str_])
assert_type(np.fft.fftshift(S_3d), _nt.Array[np.bytes_])
assert_type(np.fft.fftshift(f8_1d), _nt.Array1D[np.float64])
assert_type(np.fft.fftshift(f8_nd), _nt.Array[np.float64])
assert_type(np.fft.fftshift(c8_1d), _nt.Array1D[np.complex64])
assert_type(np.fft.fftshift(c32_nd), _nt.Array[np.clongdouble])

assert_type(np.fft.ifftshift(b_1d), _nt.Array1D[np.bool])
assert_type(np.fft.ifftshift(i_1d), _nt.Array1D[np.intp])
assert_type(np.fft.ifftshift(f_1d), _nt.Array1D[np.float64])
assert_type(np.fft.ifftshift(c_1d, axes=0), _nt.Array1D[np.complex128])
assert_type(np.fft.ifftshift(U_1d, axes=(0,)), _nt.Array1D[np.str_])
assert_type(np.fft.ifftshift(S_1d, axes=(0,)), _nt.Array1D[np.bytes_])
assert_type(np.fft.ifftshift(b_3d), _nt.Array[np.bool])
assert_type(np.fft.ifftshift(i_3d), _nt.Array[np.intp])
assert_type(np.fft.ifftshift(f_3d), _nt.Array[np.float64])
assert_type(np.fft.ifftshift(c_3d), _nt.Array[np.complex128])
assert_type(np.fft.ifftshift(U_3d), _nt.Array[np.str_])
assert_type(np.fft.ifftshift(S_3d), _nt.Array[np.bytes_])
assert_type(np.fft.ifftshift(f8_1d), _nt.Array1D[np.float64])
assert_type(np.fft.ifftshift(f8_nd), _nt.Array[np.float64])
assert_type(np.fft.ifftshift(c8_1d), _nt.Array1D[np.complex64])
assert_type(np.fft.ifftshift(c32_nd), _nt.Array[np.clongdouble])

###

# keep in sync with `rfftfreq` (same signature)
assert_type(np.fft.fftfreq(5, 0.1), _nt.Array1D[np.float64])
assert_type(np.fft.fftfreq(5, f8_1d), _nt.Array1D[np.float64])
assert_type(np.fft.fftfreq(5, f16_1d), _nt.Array1D[np.longdouble])
assert_type(np.fft.fftfreq(5, 0.1j), _nt.Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c8_1d), _nt.Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c16_1d), _nt.Array1D[np.complex128])
assert_type(np.fft.fftfreq(5, c32_1d), _nt.Array1D[np.clongdouble])
assert_type(np.fft.fftfreq(5, f8_nd), _nt.Array[np.float64])
assert_type(np.fft.fftfreq(5, f16_nd), _nt.Array[np.longdouble])
assert_type(np.fft.fftfreq(5, c8_nd), _nt.Array[np.complex128])
assert_type(np.fft.fftfreq(5, c16_nd), _nt.Array[np.complex128])
assert_type(np.fft.fftfreq(5, c32_nd), _nt.Array[np.clongdouble])

assert_type(np.fft.rfftfreq(5, 0.1), _nt.Array1D[np.float64])
assert_type(np.fft.rfftfreq(5, f8_1d), _nt.Array1D[np.float64])
assert_type(np.fft.rfftfreq(5, f16_1d), _nt.Array1D[np.longdouble])
assert_type(np.fft.rfftfreq(5, 0.1j), _nt.Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c8_1d), _nt.Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c16_1d), _nt.Array1D[np.complex128])
assert_type(np.fft.rfftfreq(5, c32_1d), _nt.Array1D[np.clongdouble])
assert_type(np.fft.rfftfreq(5, f8_nd), _nt.Array[np.float64])
assert_type(np.fft.rfftfreq(5, f16_nd), _nt.Array[np.longdouble])
assert_type(np.fft.rfftfreq(5, c8_nd), _nt.Array[np.complex128])
assert_type(np.fft.rfftfreq(5, c16_nd), _nt.Array[np.complex128])
assert_type(np.fft.rfftfreq(5, c32_nd), _nt.Array[np.clongdouble])

###

assert_type(np.fft.fft(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.ifft(f8_nd, axis=1), _nt.Array[np.complex128])
assert_type(np.fft.rfft(f8_nd, n=None), _nt.Array[np.complex128])
assert_type(np.fft.irfft(f8_nd, norm="ortho"), _nt.Array[np.float64])
assert_type(np.fft.hfft(f8_nd, n=2), _nt.Array[np.float64])
assert_type(np.fft.ihfft(f8_nd), _nt.Array[np.complex128])

assert_type(np.fft.fftn(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.ifftn(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.rfftn(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.irfftn(f8_nd), _nt.Array[np.float64])

assert_type(np.fft.rfft2(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.ifft2(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.fft2(f8_nd), _nt.Array[np.complex128])
assert_type(np.fft.irfft2(f8_nd), _nt.Array[np.float64])
