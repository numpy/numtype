from typing import Any, Literal, TypeAlias, assert_type
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy.linalg._linalg import EigResult, EighResult, QRResult, SVDResult, SlogdetResult

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_Array2ND: TypeAlias = _nt.Array[_ScalarT, _nt.Shape2N]

###

b_nd: _nt.Array[np.bool]
i8_nd: _nt.Array[np.int64]
f4_nd: _nt.Array[np.float32]
f8_nd: _nt.Array[np.float64]
c8_nd: _nt.Array[np.complex64]
c16_nd: _nt.Array[np.complex128]

O_nd: _nt.Array[np.object_]
m_nd: _nt.Array[np.timedelta64]
S_nd: _nt.Array[np.str_]

py_i_0d: int

py_b_1d: list[bool]
py_i_1d: list[int]
py_f_1d: list[float]
py_c_1d: list[complex]
py_S_1d: list[bytes]
py_U_1d: list[str]

py_b_2d: list[list[bool]]
py_i_2d: list[list[int]]
py_f_2d: list[list[float]]
py_c_2d: list[list[complex]]
py_S_2d: list[list[bytes]]
py_U_2d: list[list[str]]

py_i_3d: list[list[list[int]]]
py_f_3d: list[list[list[float]]]
py_c_3d: list[list[list[complex]]]

py_i_4d: list[list[list[list[int]]]]

###

assert_type(np.linalg.tensorsolve(i8_nd, i8_nd), _nt.Array[np.float64])
assert_type(np.linalg.tensorsolve(i8_nd, f8_nd), _nt.Array[np.float64])
assert_type(np.linalg.tensorsolve(c16_nd, f8_nd), _nt.Array[np.complex128])

assert_type(np.linalg.solve(i8_nd, i8_nd), _nt.Array[np.float64])
assert_type(np.linalg.solve(i8_nd, f8_nd), _nt.Array[np.float64])
assert_type(np.linalg.solve(c16_nd, f8_nd), _nt.Array[np.complex128])

assert_type(np.linalg.tensorinv(i8_nd), _Array2ND[np.float64])
assert_type(np.linalg.tensorinv(f4_nd), _Array2ND[np.float32])
assert_type(np.linalg.tensorinv(f8_nd), _Array2ND[np.float64])
assert_type(np.linalg.tensorinv(c8_nd), _Array2ND[np.complex64])
assert_type(np.linalg.tensorinv(c16_nd), _Array2ND[np.complex128])
assert_type(np.linalg.tensorinv(py_i_2d), _Array2ND[np.float64])
assert_type(np.linalg.tensorinv(py_f_2d), _Array2ND[np.float64])
assert_type(np.linalg.tensorinv(py_c_2d), _Array2ND[np.complex128])

assert_type(np.linalg.inv(i8_nd), _Array2ND[np.float64])
assert_type(np.linalg.inv(f4_nd), _Array2ND[np.float32])
assert_type(np.linalg.inv(f8_nd), _Array2ND[np.float64])
assert_type(np.linalg.inv(c8_nd), _Array2ND[np.complex64])
assert_type(np.linalg.inv(c16_nd), _Array2ND[np.complex128])
assert_type(np.linalg.inv(py_i_2d), _Array2ND[np.float64])
assert_type(np.linalg.inv(py_f_2d), _Array2ND[np.float64])
assert_type(np.linalg.inv(py_c_2d), _Array2ND[np.complex128])

assert_type(np.linalg.matrix_power(i8_nd, -1), _Array2ND[np.float64])
assert_type(np.linalg.matrix_power(f8_nd, 0), _Array2ND[np.float64])
assert_type(np.linalg.matrix_power(c16_nd, 1), _Array2ND[np.complex128])
assert_type(np.linalg.matrix_power(O_nd, 2), _Array2ND[np.object_])

assert_type(np.linalg.cholesky(i8_nd), _Array2ND[np.float64])
assert_type(np.linalg.cholesky(f8_nd), _Array2ND[np.float64])
assert_type(np.linalg.cholesky(c16_nd), _Array2ND[np.complex128])

assert_type(np.linalg.outer(i8_nd, i8_nd), _nt.Array2D[np.int64])
assert_type(np.linalg.outer(f8_nd, f8_nd), _nt.Array2D[np.float64])
assert_type(np.linalg.outer(c16_nd, c16_nd), _nt.Array2D[np.complex128])
assert_type(np.linalg.outer(b_nd, b_nd), _nt.Array2D[np.bool])
assert_type(np.linalg.outer(O_nd, O_nd), _nt.Array2D[np.object_])
assert_type(np.linalg.outer(i8_nd, m_nd), _nt.Array2D[np.timedelta64])

assert_type(np.linalg.qr(i8_nd), QRResult[np.float64])
assert_type(np.linalg.qr(f8_nd), QRResult[np.float64])
assert_type(np.linalg.qr(c16_nd), QRResult[np.complex128])

assert_type(np.linalg.eigvals(i8_nd), _nt.Array[np.float64] | _nt.Array[np.complex128])
assert_type(np.linalg.eigvals(f8_nd), _nt.Array[np.float64] | _nt.Array[np.complex128])
assert_type(np.linalg.eigvals(c16_nd), _nt.Array[np.complex128])

assert_type(np.linalg.eigvalsh(i8_nd), _nt.Array[np.float64])
assert_type(np.linalg.eigvalsh(f8_nd), _nt.Array[np.float64])
assert_type(np.linalg.eigvalsh(c16_nd), _nt.Array[np.float64])

assert_type(np.linalg.eig(i8_nd), EigResult[np.float64] | EigResult[np.complex128])
assert_type(np.linalg.eig(f8_nd), EigResult[np.float64] | EigResult[np.complex128])
assert_type(np.linalg.eig(c16_nd), EigResult[np.complex128])

assert_type(np.linalg.eigh(i8_nd), EighResult[np.float64, np.float64])
assert_type(np.linalg.eigh(f8_nd), EighResult[np.float64, np.float64])
assert_type(np.linalg.eigh(c16_nd), EighResult[np.float64, np.complex128])

assert_type(np.linalg.svd(i8_nd), SVDResult[np.float64, np.float64])
assert_type(np.linalg.svd(f8_nd), SVDResult[np.float64, np.float64])
assert_type(np.linalg.svd(c16_nd), SVDResult[np.float64, np.complex128])
assert_type(np.linalg.svd(i8_nd, compute_uv=False), _nt.Array[np.float64])
assert_type(np.linalg.svd(f8_nd, compute_uv=False), _nt.Array[np.float64])
assert_type(np.linalg.svd(c16_nd, compute_uv=False), _nt.Array[np.float64])

assert_type(np.linalg.cond([[1, 0], [0, 1]]), np.float64)
assert_type(np.linalg.cond([[[1, 0], [0, 1]]]), _nt.Array[np.float64])
assert_type(np.linalg.cond(i8_nd), Any)
assert_type(np.linalg.cond(f8_nd), Any)
assert_type(np.linalg.cond(c16_nd), Any)

assert_type(np.linalg.matrix_rank(py_i_0d), Literal[0, 1])
assert_type(np.linalg.matrix_rank(py_i_1d), Literal[0, 1])
assert_type(np.linalg.matrix_rank(py_i_2d), np.int_)
assert_type(np.linalg.matrix_rank(py_i_3d), _nt.Array[np.int_])
assert_type(np.linalg.matrix_rank(py_i_4d), _nt.Array[np.int_])
assert_type(np.linalg.matrix_rank(i8_nd), Any)
assert_type(np.linalg.matrix_rank(f8_nd), Any)
assert_type(np.linalg.matrix_rank(c16_nd), Any)

assert_type(np.linalg.pinv(i8_nd), _Array2ND[np.float64])
assert_type(np.linalg.pinv(f8_nd), _Array2ND[np.float64])
assert_type(np.linalg.pinv(c16_nd), _Array2ND[np.complex128])

assert_type(np.linalg.slogdet(py_i_2d), SlogdetResult[np.float64, np.float64])
assert_type(np.linalg.slogdet([py_f_1d]), SlogdetResult[np.float64, np.float64])
assert_type(np.linalg.slogdet(py_c_2d), SlogdetResult[np.float64, np.complex128])
assert_type(np.linalg.slogdet(py_i_3d), SlogdetResult[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(np.linalg.slogdet(py_f_3d), SlogdetResult[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(np.linalg.slogdet(py_c_3d), SlogdetResult[_nt.Array[np.float64], _nt.Array[np.complex128]])
assert_type(np.linalg.slogdet(i8_nd), SlogdetResult)
assert_type(np.linalg.slogdet(f8_nd), SlogdetResult)
assert_type(np.linalg.slogdet(c16_nd), SlogdetResult)

assert_type(np.linalg.det(i8_nd), Any)
assert_type(np.linalg.det(f8_nd), Any)
assert_type(np.linalg.det(c16_nd), Any)

assert_type(
    np.linalg.lstsq(i8_nd, i8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64], np.int32, _nt.Array[np.float64]]
)
assert_type(
    np.linalg.lstsq(i8_nd, f8_nd), tuple[_nt.Array[np.float64], _nt.Array[np.float64], np.int32, _nt.Array[np.float64]]
)
assert_type(
    np.linalg.lstsq(f8_nd, c16_nd),
    tuple[_nt.Array[np.complex128], _nt.Array[np.float64], np.int32, _nt.Array[np.float64]],
)

assert_type(np.linalg.norm(i8_nd), np.float64)
assert_type(np.linalg.norm(f8_nd), np.float64)
assert_type(np.linalg.norm(c16_nd), np.float64)
assert_type(np.linalg.norm(S_nd), np.float64)
assert_type(np.linalg.norm(f8_nd, axis=0), _nt.Array[np.float64])
assert_type(np.linalg.norm(f8_nd, keepdims=True), _Array2ND[np.float64])

assert_type(np.linalg.matrix_norm(py_b_2d), np.float64)
assert_type(np.linalg.matrix_norm(py_i_2d), np.float64)
assert_type(np.linalg.matrix_norm(py_c_2d), np.float64)
assert_type(np.linalg.matrix_norm(py_U_2d), np.float64)
assert_type(np.linalg.matrix_norm(py_S_2d), np.float64)
assert_type(np.linalg.matrix_norm([py_b_2d]), _nt.Array[np.float64])
assert_type(np.linalg.matrix_norm(py_i_3d), _nt.Array[np.float64])
assert_type(np.linalg.matrix_norm(py_c_3d), _nt.Array[np.float64])
assert_type(np.linalg.matrix_norm([py_U_2d]), _nt.Array[np.float64])
assert_type(np.linalg.matrix_norm([py_S_2d]), _nt.Array[np.float64])
assert_type(np.linalg.matrix_norm(i8_nd), Any)
assert_type(np.linalg.matrix_norm(f8_nd), Any)
assert_type(np.linalg.matrix_norm(c16_nd), Any)
assert_type(np.linalg.matrix_norm(S_nd), Any)

assert_type(np.linalg.vector_norm(i8_nd), np.float64)
assert_type(np.linalg.vector_norm(f8_nd), np.float64)
assert_type(np.linalg.vector_norm(c16_nd), np.float64)
assert_type(np.linalg.vector_norm(S_nd), np.float64)

assert_type(np.linalg.multi_dot(py_b_2d), np.bool)
assert_type(np.linalg.multi_dot(py_i_2d), np.int_)
assert_type(np.linalg.multi_dot(py_f_2d), np.float64)
assert_type(np.linalg.multi_dot(py_c_2d), np.complex128)
assert_type(np.linalg.multi_dot([i8_nd, i8_nd]), Any)
assert_type(np.linalg.multi_dot([i8_nd, f8_nd]), Any)
assert_type(np.linalg.multi_dot([f8_nd, c16_nd]), Any)
assert_type(np.linalg.multi_dot([O_nd, O_nd]), Any)
assert_type(np.linalg.multi_dot([m_nd, m_nd]), Any)

assert_type(np.linalg.cross(i8_nd, i8_nd), _nt.Array[np.int64])
assert_type(np.linalg.cross(f8_nd, f8_nd), _nt.Array[np.float64])
assert_type(np.linalg.cross(c16_nd, c16_nd), _nt.Array[np.complex128])

assert_type(np.linalg.matmul(py_b_1d, py_b_1d), np.bool)
assert_type(np.linalg.matmul(py_i_1d, py_i_1d), np.int_)
assert_type(np.linalg.matmul(py_i_1d, py_b_1d), np.int_)
assert_type(np.linalg.matmul(py_f_1d, py_f_1d), np.float64)
assert_type(np.linalg.matmul(py_f_1d, py_i_1d), np.float64)
assert_type(np.linalg.matmul(py_c_1d, py_c_1d), np.complex128)
assert_type(np.linalg.matmul(py_b_1d, py_c_1d), np.complex128)
assert_type(np.linalg.matmul(i8_nd, i8_nd), Any)
assert_type(np.linalg.matmul(f8_nd, f8_nd), Any)
assert_type(np.linalg.matmul(c16_nd, c16_nd), Any)
