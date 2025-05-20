from collections.abc import Sequence
from typing import TypeAlias, assert_type

import _numtype as _nt
import numpy as np
import numpy.polynomial as npp

_Float64_1d: TypeAlias = _nt.Array1D[np.float64]
_Float64_nd: TypeAlias = _nt.Array[np.float64]
_Floating_nd: TypeAlias = _nt.Array[np.floating]
_Complex128_1d: TypeAlias = _nt.Array1D[np.complex128]
_Complex128_nd: TypeAlias = _nt.Array[np.complex128]
_ComplexFloating_nd: TypeAlias = _nt.Array[np.complexfloating]
_Object_1d: TypeAlias = _nt.Array1D[np.object_]
_Object_nd: TypeAlias = _nt.Array[np.object_]

AR_b: _nt.Array[np.bool]
AR_u4: _nt.Array[np.uint32]
AR_i8: _nt.Array[np.int64]
AR_f8: _Float64_nd
AR_c16: _Complex128_nd
AR_O: _Object_nd

PS_poly: npp.Polynomial
PS_cheb: npp.Chebyshev

assert_type(npp.polynomial.polyroots(AR_f8), _Float64_1d)
assert_type(npp.polynomial.polyroots(AR_c16), _Complex128_1d)
assert_type(npp.polynomial.polyroots(AR_O), _Object_1d)

assert_type(npp.polynomial.polyfromroots(AR_f8), _Float64_1d)
assert_type(npp.polynomial.polyfromroots(AR_c16), _Complex128_1d)
assert_type(npp.polynomial.polyfromroots(AR_O), _Object_1d)

assert_type(npp.polynomial.polyadd(AR_u4, AR_b), _Float64_1d)
assert_type(npp.polynomial.polyadd(AR_i8, AR_i8), _Float64_1d)
assert_type(npp.polynomial.polyadd(AR_f8, AR_i8), _Float64_1d)
assert_type(npp.polynomial.polyadd(AR_i8, AR_c16), _Complex128_1d)
assert_type(npp.polynomial.polyadd(AR_O, AR_O), _Object_1d)

assert_type(npp.polynomial.polymulx(AR_u4), _Float64_1d)
assert_type(npp.polynomial.polymulx(AR_i8), _Float64_1d)
assert_type(npp.polynomial.polymulx(AR_f8), _Float64_1d)
assert_type(npp.polynomial.polymulx(AR_c16), _Complex128_1d)
assert_type(npp.polynomial.polymulx(AR_O), _Object_1d)

assert_type(npp.polynomial.polypow(AR_u4, 2), _Float64_1d)
assert_type(npp.polynomial.polypow(AR_i8, 2), _Float64_1d)
assert_type(npp.polynomial.polypow(AR_f8, 2), _Float64_1d)
assert_type(npp.polynomial.polypow(AR_c16, 2), _Complex128_1d)
assert_type(npp.polynomial.polypow(AR_O, 2), _Object_1d)

assert_type(npp.polynomial.polyder(AR_f8), _Float64_nd)
assert_type(npp.polynomial.polyder(AR_c16), _Complex128_nd)
assert_type(npp.polynomial.polyder(AR_O, m=2), _Object_nd)

assert_type(npp.polynomial.polyint(AR_f8), _Float64_nd)
assert_type(npp.polynomial.polyint(AR_f8, k=AR_c16), _ComplexFloating_nd)
assert_type(npp.polynomial.polyint(AR_O, m=2), _Object_nd)

assert_type(npp.polynomial.polyval(AR_b, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval(AR_u4, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval(AR_i8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyval(AR_f8, AR_i8), _Float64_nd)
assert_type(npp.polynomial.polyval(AR_i8, AR_c16), _ComplexFloating_nd)
assert_type(npp.polynomial.polyval(AR_O, AR_O), _Object_nd)

assert_type(npp.polynomial.polyval2d(AR_b, AR_b, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval2d(AR_u4, AR_u4, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval2d(AR_i8, AR_i8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyval2d(AR_f8, AR_f8, AR_i8), _Float64_nd)
assert_type(npp.polynomial.polyval2d(AR_i8, AR_i8, AR_c16), _ComplexFloating_nd)
assert_type(npp.polynomial.polyval2d(AR_O, AR_O, AR_O), _Object_nd)

assert_type(npp.polynomial.polyval3d(AR_b, AR_b, AR_b, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval3d(AR_u4, AR_u4, AR_u4, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyval3d(AR_i8, AR_i8, AR_i8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyval3d(AR_f8, AR_f8, AR_f8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyval3d(AR_i8, AR_i8, AR_i8, AR_c16), _ComplexFloating_nd)
assert_type(npp.polynomial.polyval3d(AR_O, AR_O, AR_O, AR_O), _Object_nd)

assert_type(npp.polynomial.polyvalfromroots(AR_b, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyvalfromroots(AR_u4, AR_b), _Floating_nd)
assert_type(npp.polynomial.polyvalfromroots(AR_i8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyvalfromroots(AR_f8, AR_i8), _Floating_nd)
assert_type(npp.polynomial.polyvalfromroots(AR_i8, AR_c16), _ComplexFloating_nd)
assert_type(npp.polynomial.polyvalfromroots(AR_O, AR_O), _Object_nd)

assert_type(npp.polynomial.polyvander(AR_f8, 3), _Float64_nd)
assert_type(npp.polynomial.polyvander(AR_c16, 3), _Complex128_nd)
assert_type(npp.polynomial.polyvander(AR_O, 3), _Object_nd)

assert_type(npp.polynomial.polyvander2d(AR_f8, AR_f8, [4, 2]), _Float64_nd)
assert_type(npp.polynomial.polyvander2d(AR_c16, AR_c16, [4, 2]), _ComplexFloating_nd)
assert_type(npp.polynomial.polyvander2d(AR_O, AR_O, [4, 2]), _Object_nd)

assert_type(npp.polynomial.polyvander3d(AR_f8, AR_f8, AR_f8, [4, 3, 2]), _Float64_nd)
assert_type(npp.polynomial.polyvander3d(AR_c16, AR_c16, AR_c16, [4, 3, 2]), _ComplexFloating_nd)
assert_type(npp.polynomial.polyvander3d(AR_O, AR_O, AR_O, [4, 3, 2]), _Object_nd)

assert_type(npp.polynomial.polyfit(AR_f8, AR_f8, 2), _Float64_nd)
assert_type(npp.polynomial.polyfit(AR_f8, AR_i8, 1, full=True), tuple[_Float64_nd, Sequence[np.inexact | np.int32]])
assert_type(npp.polynomial.polyfit(AR_c16, AR_f8, 2), _ComplexFloating_nd)
assert_type(npp.polynomial.polyfit(AR_f8, AR_c16, 1, full=True)[0], _ComplexFloating_nd)

assert_type(npp.chebyshev.chebgauss(2), tuple[_Float64_1d, _Float64_1d])

assert_type(npp.chebyshev.chebweight(AR_f8), _Float64_nd)
assert_type(npp.chebyshev.chebweight(AR_c16), _Complex128_nd)
assert_type(npp.chebyshev.chebweight(AR_O), _Object_nd)

assert_type(npp.chebyshev.poly2cheb(AR_f8), _Float64_1d)
assert_type(npp.chebyshev.poly2cheb(AR_c16), _Complex128_1d)
assert_type(npp.chebyshev.poly2cheb(AR_O), _Object_1d)

assert_type(npp.chebyshev.cheb2poly(AR_f8), _Float64_1d)
assert_type(npp.chebyshev.cheb2poly(AR_c16), _Complex128_1d)
assert_type(npp.chebyshev.cheb2poly(AR_O), _Object_1d)

assert_type(npp.chebyshev.chebpts1(6), _Float64_1d)
assert_type(npp.chebyshev.chebpts2(6), _Float64_1d)

assert_type(npp.chebyshev.chebinterpolate(np.tanh, 3), _Float64_nd)
