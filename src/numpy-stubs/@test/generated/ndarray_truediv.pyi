# @generated 2025-04-14T13:48:50Z with tool/testgen.py
from typing_extensions import assert_type

import numpy as np
import numpy.typing as npt

###

i8_nd: npt.NDArray[np.int64]
f2_nd: npt.NDArray[np.float16]
f4_nd: npt.NDArray[np.float32]
f8_nd: npt.NDArray[np.float64]
fld_nd: npt.NDArray[np.longdouble]
c8_nd: npt.NDArray[np.complex64]
c16_nd: npt.NDArray[np.complex128]
cld_nd: npt.NDArray[np.clongdouble]
m8_nd: npt.NDArray[np.timedelta64]
O_nd: npt.NDArray[np.object_]
f_nd: npt.NDArray[np.floating]
c_nd: npt.NDArray[np.complexfloating]
fc_nd: npt.NDArray[np.inexact]

i_py: int
f_py: float
c_py: complex

###

assert_type(i8_nd / i8_nd, npt.NDArray[np.float64])
assert_type(i8_nd / f2_nd, npt.NDArray[np.float64])
assert_type(i8_nd / f4_nd, npt.NDArray[np.float64])
assert_type(i8_nd / f8_nd, npt.NDArray[np.float64])
assert_type(i8_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(i8_nd / c8_nd, npt.NDArray[np.complex128])
assert_type(i8_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(i8_nd / cld_nd, npt.NDArray[np.clongdouble])
i8_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(i8_nd / O_nd, npt.NDArray[np.object_])
assert_type(i8_nd / f_nd, npt.NDArray[np.floating])
assert_type(i8_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(i8_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(i8_nd / i_py, npt.NDArray[np.float64])
assert_type(i8_nd / f_py, npt.NDArray[np.float64])
assert_type(i8_nd / c_py, npt.NDArray[np.complex128])

assert_type(i_py / i8_nd, npt.NDArray[np.float64])
assert_type(f_py / i8_nd, npt.NDArray[np.float64])
assert_type(c_py / i8_nd, npt.NDArray[np.complex128])

assert_type(f2_nd / i8_nd, npt.NDArray[np.float64])
assert_type(f2_nd / f2_nd, npt.NDArray[np.float16])
assert_type(f2_nd / f4_nd, npt.NDArray[np.float32])
assert_type(f2_nd / f8_nd, npt.NDArray[np.float64])
assert_type(f2_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(f2_nd / c8_nd, npt.NDArray[np.complex64])
assert_type(f2_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(f2_nd / cld_nd, npt.NDArray[np.clongdouble])
f2_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f2_nd / O_nd, npt.NDArray[np.object_])
assert_type(f2_nd / f_nd, npt.NDArray[np.floating])
assert_type(f2_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(f2_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(f2_nd / i_py, npt.NDArray[np.float16])
assert_type(f2_nd / f_py, npt.NDArray[np.float16])
assert_type(f2_nd / c_py, npt.NDArray[np.complex64])

assert_type(i_py / f2_nd, npt.NDArray[np.float16])
assert_type(f_py / f2_nd, npt.NDArray[np.float16])
assert_type(c_py / f2_nd, npt.NDArray[np.complex64])

assert_type(f4_nd / i8_nd, npt.NDArray[np.float64])
assert_type(f4_nd / f2_nd, npt.NDArray[np.float32])
assert_type(f4_nd / f4_nd, npt.NDArray[np.float32])
assert_type(f4_nd / f8_nd, npt.NDArray[np.float64])
assert_type(f4_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(f4_nd / c8_nd, npt.NDArray[np.complex64])
assert_type(f4_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(f4_nd / cld_nd, npt.NDArray[np.clongdouble])
f4_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f4_nd / O_nd, npt.NDArray[np.object_])
assert_type(f4_nd / f_nd, npt.NDArray[np.floating])
assert_type(f4_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(f4_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(f4_nd / i_py, npt.NDArray[np.float32])
assert_type(f4_nd / f_py, npt.NDArray[np.float32])
assert_type(f4_nd / c_py, npt.NDArray[np.complex64])

assert_type(i_py / f4_nd, npt.NDArray[np.float32])
assert_type(f_py / f4_nd, npt.NDArray[np.float32])
assert_type(c_py / f4_nd, npt.NDArray[np.complex64])

assert_type(f8_nd / i8_nd, npt.NDArray[np.float64])
assert_type(f8_nd / f2_nd, npt.NDArray[np.float64])
assert_type(f8_nd / f4_nd, npt.NDArray[np.float64])
assert_type(f8_nd / f8_nd, npt.NDArray[np.float64])
assert_type(f8_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(f8_nd / c8_nd, npt.NDArray[np.complex128])
assert_type(f8_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(f8_nd / cld_nd, npt.NDArray[np.clongdouble])
f8_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f8_nd / O_nd, npt.NDArray[np.object_])
assert_type(f8_nd / f_nd, npt.NDArray[np.floating])
assert_type(f8_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(f8_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(f8_nd / i_py, npt.NDArray[np.float64])
assert_type(f8_nd / f_py, npt.NDArray[np.float64])
assert_type(f8_nd / c_py, npt.NDArray[np.complex128])

assert_type(i_py / f8_nd, npt.NDArray[np.float64])
assert_type(f_py / f8_nd, npt.NDArray[np.float64])
assert_type(c_py / f8_nd, npt.NDArray[np.complex128])

assert_type(fld_nd / i8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / f2_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / f4_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / f8_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / c8_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd / c16_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd / cld_nd, npt.NDArray[np.clongdouble])
fld_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fld_nd / O_nd, npt.NDArray[np.object_])
assert_type(fld_nd / f_nd, npt.NDArray[np.longdouble])
assert_type(fld_nd / c_nd, npt.NDArray[np.clongdouble])
assert_type(fld_nd / fc_nd, npt.NDArray[np.longdouble | np.clongdouble])

assert_type(fld_nd / i_py, npt.NDArray[np.longdouble])
assert_type(fld_nd / f_py, npt.NDArray[np.longdouble])
assert_type(fld_nd / c_py, npt.NDArray[np.clongdouble])

assert_type(i_py / fld_nd, npt.NDArray[np.longdouble])
assert_type(f_py / fld_nd, npt.NDArray[np.longdouble])
assert_type(c_py / fld_nd, npt.NDArray[np.clongdouble])

assert_type(c8_nd / i8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd / f2_nd, npt.NDArray[np.complex64])
assert_type(c8_nd / f4_nd, npt.NDArray[np.complex64])
assert_type(c8_nd / f8_nd, npt.NDArray[np.complex128])
assert_type(c8_nd / fld_nd, npt.NDArray[np.clongdouble])
assert_type(c8_nd / c8_nd, npt.NDArray[np.complex64])
assert_type(c8_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(c8_nd / cld_nd, npt.NDArray[np.clongdouble])
c8_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c8_nd / O_nd, npt.NDArray[np.object_])
assert_type(c8_nd / f_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(c8_nd / fc_nd, npt.NDArray[np.complexfloating])

assert_type(c8_nd / i_py, npt.NDArray[np.complex64])
assert_type(c8_nd / f_py, npt.NDArray[np.complex64])
assert_type(c8_nd / c_py, npt.NDArray[np.complex64])

assert_type(i_py / c8_nd, npt.NDArray[np.complex64])
assert_type(f_py / c8_nd, npt.NDArray[np.complex64])
assert_type(c_py / c8_nd, npt.NDArray[np.complex64])

assert_type(c16_nd / i8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / f2_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / f4_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / f8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / fld_nd, npt.NDArray[np.clongdouble])
assert_type(c16_nd / c8_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / c16_nd, npt.NDArray[np.complex128])
assert_type(c16_nd / cld_nd, npt.NDArray[np.clongdouble])
c16_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c16_nd / O_nd, npt.NDArray[np.object_])
assert_type(c16_nd / f_nd, npt.NDArray[np.complexfloating])
assert_type(c16_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(c16_nd / fc_nd, npt.NDArray[np.complexfloating])

assert_type(c16_nd / i_py, npt.NDArray[np.complex128])
assert_type(c16_nd / f_py, npt.NDArray[np.complex128])
assert_type(c16_nd / c_py, npt.NDArray[np.complex128])

assert_type(i_py / c16_nd, npt.NDArray[np.complex128])
assert_type(f_py / c16_nd, npt.NDArray[np.complex128])
assert_type(c_py / c16_nd, npt.NDArray[np.complex128])

assert_type(cld_nd / i8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / f2_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / f4_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / f8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / fld_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / c8_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / c16_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / cld_nd, npt.NDArray[np.clongdouble])
cld_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(cld_nd / O_nd, npt.NDArray[np.object_])
assert_type(cld_nd / f_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / c_nd, npt.NDArray[np.clongdouble])
assert_type(cld_nd / fc_nd, npt.NDArray[np.clongdouble])

assert_type(cld_nd / i_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd / f_py, npt.NDArray[np.clongdouble])
assert_type(cld_nd / c_py, npt.NDArray[np.clongdouble])

assert_type(i_py / cld_nd, npt.NDArray[np.clongdouble])
assert_type(f_py / cld_nd, npt.NDArray[np.clongdouble])
assert_type(c_py / cld_nd, npt.NDArray[np.clongdouble])

assert_type(m8_nd / i8_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd / f2_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd / f4_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd / f8_nd, npt.NDArray[np.timedelta64])
assert_type(m8_nd / fld_nd, npt.NDArray[np.timedelta64])
m8_nd / c8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd / c16_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd / cld_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(m8_nd / m8_nd, npt.NDArray[np.float64])
assert_type(m8_nd / f_nd, npt.NDArray[np.timedelta64])
m8_nd / c_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
m8_nd / fc_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(m8_nd / i_py, npt.NDArray[np.timedelta64])
assert_type(m8_nd / f_py, npt.NDArray[np.timedelta64])
m8_nd / c_py  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

i_py / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f_py / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
c_py / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

assert_type(O_nd / i8_nd, npt.NDArray[np.object_])
assert_type(O_nd / f2_nd, npt.NDArray[np.object_])
assert_type(O_nd / f4_nd, npt.NDArray[np.object_])
assert_type(O_nd / f8_nd, npt.NDArray[np.object_])
assert_type(O_nd / fld_nd, npt.NDArray[np.object_])
assert_type(O_nd / c8_nd, npt.NDArray[np.object_])
assert_type(O_nd / c16_nd, npt.NDArray[np.object_])
assert_type(O_nd / cld_nd, npt.NDArray[np.object_])
assert_type(O_nd / O_nd, npt.NDArray[np.object_])
assert_type(O_nd / f_nd, npt.NDArray[np.object_])
assert_type(O_nd / c_nd, npt.NDArray[np.object_])
assert_type(O_nd / fc_nd, npt.NDArray[np.object_])

assert_type(O_nd / i_py, npt.NDArray[np.object_])
assert_type(O_nd / f_py, npt.NDArray[np.object_])
assert_type(O_nd / c_py, npt.NDArray[np.object_])

assert_type(i_py / O_nd, npt.NDArray[np.object_])
assert_type(f_py / O_nd, npt.NDArray[np.object_])
assert_type(c_py / O_nd, npt.NDArray[np.object_])

assert_type(f_nd / i8_nd, npt.NDArray[np.floating])
assert_type(f_nd / f2_nd, npt.NDArray[np.floating])
assert_type(f_nd / f4_nd, npt.NDArray[np.floating])
assert_type(f_nd / f8_nd, npt.NDArray[np.floating])
assert_type(f_nd / fld_nd, npt.NDArray[np.longdouble])
assert_type(f_nd / c8_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd / c16_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd / cld_nd, npt.NDArray[np.clongdouble])
f_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(f_nd / O_nd, npt.NDArray[np.object_])
assert_type(f_nd / f_nd, npt.NDArray[np.floating])
assert_type(f_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(f_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(f_nd / i_py, npt.NDArray[np.floating])
assert_type(f_nd / f_py, npt.NDArray[np.floating])
assert_type(f_nd / c_py, npt.NDArray[np.complexfloating])

assert_type(i_py / f_nd, npt.NDArray[np.floating])
assert_type(f_py / f_nd, npt.NDArray[np.floating])
assert_type(c_py / f_nd, npt.NDArray[np.complexfloating])

assert_type(c_nd / i8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / f2_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / f4_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / f8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / fld_nd, npt.NDArray[np.clongdouble])
assert_type(c_nd / c8_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / c16_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / cld_nd, npt.NDArray[np.clongdouble])
c_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(c_nd / O_nd, npt.NDArray[np.object_])
assert_type(c_nd / f_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(c_nd / fc_nd, npt.NDArray[np.complexfloating])

assert_type(c_nd / i_py, npt.NDArray[np.complexfloating])
assert_type(c_nd / f_py, npt.NDArray[np.complexfloating])
assert_type(c_nd / c_py, npt.NDArray[np.complexfloating])

assert_type(i_py / c_nd, npt.NDArray[np.complexfloating])
assert_type(f_py / c_nd, npt.NDArray[np.complexfloating])
assert_type(c_py / c_nd, npt.NDArray[np.complexfloating])

assert_type(fc_nd / i8_nd, npt.NDArray[np.inexact])
assert_type(fc_nd / f2_nd, npt.NDArray[np.inexact])
assert_type(fc_nd / f4_nd, npt.NDArray[np.inexact])
assert_type(fc_nd / f8_nd, npt.NDArray[np.inexact])
assert_type(fc_nd / fld_nd, npt.NDArray[np.longdouble | np.clongdouble])
assert_type(fc_nd / c8_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd / c16_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd / cld_nd, npt.NDArray[np.clongdouble])
fc_nd / m8_nd  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
assert_type(fc_nd / O_nd, npt.NDArray[np.object_])
assert_type(fc_nd / f_nd, npt.NDArray[np.inexact])
assert_type(fc_nd / c_nd, npt.NDArray[np.complexfloating])
assert_type(fc_nd / fc_nd, npt.NDArray[np.inexact])

assert_type(fc_nd / i_py, npt.NDArray[np.inexact])
assert_type(fc_nd / f_py, npt.NDArray[np.inexact])
assert_type(fc_nd / c_py, npt.NDArray[np.complexfloating])

assert_type(i_py / fc_nd, npt.NDArray[np.inexact])
assert_type(f_py / fc_nd, npt.NDArray[np.inexact])
assert_type(c_py / fc_nd, npt.NDArray[np.complexfloating])
