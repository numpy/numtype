from collections.abc import Iterator
from typing import Any, LiteralString, assert_type

import _numtype as _nt
import numpy as np

###

AR_b: _nt.Array[np.bool]
AR_u4: _nt.Array[np.uint32]
AR_i8: _nt.Array[np.int64]
AR_f8: _nt.Array[np.float64]
AR_c16: _nt.Array[np.complex128]
AR_O: _nt.Array[np.object_]

poly_obj: np.poly1d

###

assert_type(poly_obj.variable, LiteralString)
assert_type(poly_obj.order, int)
assert_type(poly_obj.o, int)
assert_type(poly_obj.roots, _nt.Array1D[np.inexact])
assert_type(poly_obj.r, _nt.Array1D[np.inexact])
assert_type(poly_obj.coeffs, _nt.Array1D)
assert_type(poly_obj.c, _nt.Array1D)
assert_type(poly_obj.coef, _nt.Array1D)
assert_type(poly_obj.coefficients, _nt.Array1D)
assert_type(poly_obj.__hash__, None)

assert_type(poly_obj(1), Any)
assert_type(poly_obj([1]), _nt.Array)
assert_type(poly_obj(poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail

assert_type(len(poly_obj), int)
assert_type(-poly_obj, np.poly1d)
assert_type(+poly_obj, np.poly1d)

assert_type(poly_obj * 5, np.poly1d)
assert_type(5 * poly_obj, np.poly1d)
assert_type(poly_obj + 5, np.poly1d)
assert_type(5 + poly_obj, np.poly1d)
assert_type(poly_obj - 5, np.poly1d)
assert_type(5 - poly_obj, np.poly1d)
assert_type(poly_obj**1, np.poly1d)
assert_type(poly_obj**1.0, np.poly1d)
assert_type(poly_obj / 5, np.poly1d)
assert_type(5 / poly_obj, np.poly1d)

assert_type(poly_obj[0], Any)
poly_obj[0] = 5
assert_type(iter(poly_obj), Iterator[Any])
assert_type(poly_obj.deriv(), np.poly1d)
assert_type(poly_obj.integ(), np.poly1d)

assert_type(np.poly(poly_obj), _nt.Array1D[np.float64])  # type: ignore[assert-type]  # mypy fail
assert_type(np.poly(AR_f8), _nt.Array1D[np.float64])
assert_type(np.poly(AR_c16), _nt.Array1D[np.complex128])

assert_type(np.polyint(poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polyint(AR_f8), _nt.Array1D[np.float64])
assert_type(np.polyint(AR_f8, k=AR_c16), _nt.Array1D[np.complex128])
assert_type(np.polyint(AR_O, m=2), _nt.Array1D[np.object_])

assert_type(np.polyder(poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polyder(AR_f8), _nt.Array1D[np.float64])
assert_type(np.polyder(AR_c16), _nt.Array1D[np.complex128])
assert_type(np.polyder(AR_O, m=2), _nt.Array1D[np.object_])

assert_type(np.polyfit(AR_f8, AR_f8, 2), _nt.Array[np.float64])
assert_type(
    np.polyfit(AR_f8, AR_i8, 1, full=True),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.float64],
        _nt.Array[np.int32],
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(
    np.polyfit(AR_u4, AR_f8, 1.0, cov="unscaled"),
    tuple[
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(np.polyfit(AR_c16, AR_f8, 2), _nt.Array[np.complex128])
assert_type(
    np.polyfit(AR_f8, AR_c16, 1, full=True),
    tuple[
        _nt.Array[np.complex128],
        _nt.Array[np.float64],
        _nt.Array[np.int32],
        _nt.Array[np.float64],
        _nt.Array[np.float64],
    ],
)
assert_type(
    np.polyfit(AR_u4, AR_c16, 1.0, cov=True),
    tuple[
        _nt.Array[np.complex128],
        _nt.Array[np.complex128],
    ],
)

assert_type(np.polyval(AR_b, AR_b), _nt.Array[np.bool])
assert_type(np.polyval(AR_u4, AR_b), _nt.Array[np.unsignedinteger])
assert_type(np.polyval(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.polyval(AR_f8, AR_i8), _nt.Array[np.floating])
assert_type(np.polyval(AR_i8, AR_c16), _nt.Array[np.complexfloating])
assert_type(np.polyval(AR_O, AR_O), _nt.Array[np.object_])

assert_type(np.polyadd(poly_obj, AR_i8), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polyadd(AR_f8, poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polyadd(AR_b, AR_b), _nt.Array[np.bool])
assert_type(np.polyadd(AR_u4, AR_b), _nt.Array[np.unsignedinteger])
assert_type(np.polyadd(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.polyadd(AR_f8, AR_i8), _nt.Array[np.floating])
assert_type(np.polyadd(AR_i8, AR_c16), _nt.Array[np.complexfloating])
assert_type(np.polyadd(AR_O, AR_O), _nt.Array[np.object_])

assert_type(np.polysub(poly_obj, AR_i8), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polysub(AR_f8, poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polysub(AR_u4, AR_b), _nt.Array[np.unsignedinteger])
assert_type(np.polysub(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.polysub(AR_f8, AR_i8), _nt.Array[np.floating])
assert_type(np.polysub(AR_i8, AR_c16), _nt.Array[np.complexfloating])
assert_type(np.polysub(AR_O, AR_O), _nt.Array[np.object_])

assert_type(np.polymul(poly_obj, AR_i8), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polymul(AR_f8, poly_obj), np.poly1d)  # type: ignore[assert-type]  # mypy fail
assert_type(np.polymul(AR_b, AR_b), _nt.Array[np.bool])
assert_type(np.polymul(AR_u4, AR_b), _nt.Array[np.unsignedinteger])
assert_type(np.polymul(AR_i8, AR_i8), _nt.Array[np.signedinteger])
assert_type(np.polymul(AR_f8, AR_i8), _nt.Array[np.floating])
assert_type(np.polymul(AR_i8, AR_c16), _nt.Array[np.complexfloating])
assert_type(np.polymul(AR_O, AR_O), _nt.Array[np.object_])

assert_type(np.polydiv(poly_obj, AR_i8), tuple[np.poly1d, np.poly1d])  # type: ignore[assert-type]  # mypy fail
assert_type(np.polydiv(AR_f8, poly_obj), tuple[np.poly1d, np.poly1d])  # type: ignore[assert-type]  # mypy fail
assert_type(np.polydiv(AR_b, AR_b), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(np.polydiv(AR_u4, AR_b), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(np.polydiv(AR_i8, AR_i8), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(np.polydiv(AR_f8, AR_i8), tuple[_nt.Array[np.floating], _nt.Array[np.floating]])
assert_type(np.polydiv(AR_i8, AR_c16), tuple[_nt.Array[np.complexfloating], _nt.Array[np.complexfloating]])
assert_type(np.polydiv(AR_O, AR_O), tuple[_nt.Array, _nt.Array])
