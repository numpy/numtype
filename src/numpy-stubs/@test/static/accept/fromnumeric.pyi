from typing import Any, assert_type

import _numtype as _nt
import numpy as np

class NDArraySubclass(np.ndarray[_nt.Shape, np.dtype[np.complex128]]): ...

AR_b1: _nt.Array[np.bool]
AR_f4: _nt.Array[np.float32]
AR_c16: _nt.Array[np.complex128]
AR_u8: _nt.Array[np.uint64]
AR_i8: _nt.Array[np.int64]
AR_O: _nt.Array[np.object_]
AR_subclass: NDArraySubclass
AR_m: _nt.Array[np.timedelta64]
AR_0d: np.ndarray[tuple[()], np.dtype]
AR_1d: np.ndarray[tuple[int], np.dtype]
AR_nd: np.ndarray[tuple[int, ...], np.dtype]

b1: np.bool
f4: np.float32
i8: np.int64

i_0d: int
f_0d: float

b_1d: list[bool]
i_1d: list[int]
f_1d: list[float]

i_2d: list[list[int]]
i_3d: list[list[list[int]]]
i_4d: list[list[list[list[int]]]]

assert_type(np.take(b1, 0), np.bool)
assert_type(np.take(f4, 0), np.float32)
assert_type(np.take(f_0d, 0), Any)
assert_type(np.take(AR_b1, 0), np.bool)
assert_type(np.take(AR_f4, 0), np.float32)
assert_type(np.take(AR_b1, i_1d), _nt.Array[np.bool])
assert_type(np.take(AR_f4, i_1d), _nt.Array[np.float32])
assert_type(np.take(i_1d, i_1d), _nt.Array[Any])
assert_type(np.take(AR_f4, i_1d, out=AR_subclass), NDArraySubclass)

assert_type(np.reshape(b1, 1), _nt.Array1D[np.bool])
assert_type(np.reshape(f4, 1), _nt.Array1D[np.float32])
assert_type(np.reshape(f_0d, 1), _nt.Array1D)
assert_type(np.reshape(AR_b1, 1), _nt.Array1D[np.bool])
assert_type(np.reshape(AR_f4, 1), _nt.Array1D[np.float32])

assert_type(np.choose(1, b_1d), Any)
assert_type(np.choose(i_1d, b_1d), _nt.Array[Any])
assert_type(np.choose(i_1d, AR_b1), _nt.Array[np.bool])
assert_type(np.choose(i_1d, AR_b1, out=AR_f4), _nt.Array[np.float32])

assert_type(np.repeat(b1, 1), _nt.Array[np.bool])
assert_type(np.repeat(f4, 1), _nt.Array[np.float32])
assert_type(np.repeat(f_0d, 1), _nt.Array[Any])
assert_type(np.repeat(AR_b1, 1), _nt.Array[np.bool])
assert_type(np.repeat(AR_f4, 1), _nt.Array[np.float32])

assert_type(np.put(AR_b1, i_1d, b_1d), None)
assert_type(np.put(AR_f4, i_1d, f_1d), None)
assert_type(np.put(AR_b1, i_1d, b_1d, mode="raise"), None)
assert_type(np.put(AR_f4, i_1d, f_1d, mode="raise"), None)
assert_type(np.put(AR_b1, i_1d, b_1d, mode="wrap"), None)
assert_type(np.put(AR_f4, i_1d, f_1d, mode="wrap"), None)
assert_type(np.put(AR_b1, i_1d, b_1d, mode="clip"), None)
assert_type(np.put(AR_f4, i_1d, f_1d, mode="clip"), None)

assert_type(np.swapaxes(i_2d, 0, 0), _nt.Array[Any])
assert_type(np.swapaxes(AR_b1, 0, 0), _nt.Array[np.bool])
assert_type(np.swapaxes(AR_f4, 0, 0), _nt.Array[np.float32])

assert_type(np.transpose(b1), _nt.Array[np.bool])
assert_type(np.transpose(f4), _nt.Array[np.float32])
assert_type(np.transpose(f_0d), _nt.Array[Any])
assert_type(np.transpose(AR_b1), _nt.Array[np.bool])
assert_type(np.transpose(AR_f4), _nt.Array[np.float32])

assert_type(np.partition(b1, 0, axis=None), _nt.Array[np.bool])
assert_type(np.partition(f4, 0, axis=None), _nt.Array[np.float32])
assert_type(np.partition(f_0d, 0, axis=None), _nt.Array[Any])
assert_type(np.partition(AR_b1, 0), _nt.Array[np.bool])
assert_type(np.partition(AR_f4, 0), _nt.Array[np.float32])

assert_type(np.argpartition(b1, 0), _nt.Array[np.intp])
assert_type(np.argpartition(f4, 0), _nt.Array[np.intp])
assert_type(np.argpartition(f_0d, 0), _nt.Array[np.intp])
assert_type(np.argpartition(AR_b1, 0), _nt.Array[np.intp])
assert_type(np.argpartition(AR_f4, 0), _nt.Array[np.intp])

assert_type(np.sort(i_1d, 0), _nt.Array[Any])
assert_type(np.sort(AR_b1, 0), _nt.Array[np.bool])
assert_type(np.sort(AR_f4, 0), _nt.Array[np.float32])

assert_type(np.argsort(AR_b1, 0), _nt.Array[np.intp])
assert_type(np.argsort(AR_f4, 0), _nt.Array[np.intp])

assert_type(np.argmax(AR_b1), np.intp)
assert_type(np.argmax(AR_f4), np.intp)
assert_type(np.argmax(AR_b1, axis=0), Any)
assert_type(np.argmax(AR_f4, axis=0), Any)
assert_type(np.argmax(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.argmin(AR_b1), np.intp)
assert_type(np.argmin(AR_f4), np.intp)
assert_type(np.argmin(AR_b1, axis=0), Any)
assert_type(np.argmin(AR_f4, axis=0), Any)
assert_type(np.argmin(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.searchsorted(AR_b1[0], 0), np.intp)
assert_type(np.searchsorted(AR_f4[0], 0), np.intp)
assert_type(np.searchsorted(AR_b1[0], i_1d), _nt.Array[np.intp])
assert_type(np.searchsorted(AR_f4[0], i_1d), _nt.Array[np.intp])

assert_type(np.resize(b1, (5, 5)), _nt.Array[np.bool, _nt.Shape2])
assert_type(np.resize(f4, (5, 5)), _nt.Array[np.float32, _nt.Shape2])
assert_type(np.resize(f_0d, (5, 5)), _nt.Array[Any, _nt.Shape2])
assert_type(np.resize(AR_b1, (5, 5)), _nt.Array[np.bool, _nt.Shape2])
assert_type(np.resize(AR_f4, (5, 5)), _nt.Array[np.float32, _nt.Shape2])

assert_type(np.squeeze(b1), _nt.Array0D[np.bool])
assert_type(np.squeeze(f4), _nt.Array0D[np.float32])
assert_type(np.squeeze(f_0d), _nt.Array[Any])
assert_type(np.squeeze(AR_b1), _nt.Array[np.bool])
assert_type(np.squeeze(AR_f4), _nt.Array[np.float32])

assert_type(np.diagonal(AR_b1), _nt.Array[np.bool])
assert_type(np.diagonal(AR_f4), _nt.Array[np.float32])

assert_type(np.trace(AR_b1), Any)
assert_type(np.trace(AR_f4), Any)
assert_type(np.trace(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.ravel(b1), _nt.Array1D[np.bool])
assert_type(np.ravel(f4), _nt.Array1D[np.float32])
assert_type(np.ravel(f_0d), _nt.Array1D[np.float64])
assert_type(np.ravel(AR_b1), _nt.Array1D[np.bool])
assert_type(np.ravel(AR_f4), _nt.Array1D[np.float32])

assert_type(np.nonzero(AR_b1), tuple[_nt.Array[np.intp], ...])
assert_type(np.nonzero(AR_f4), tuple[_nt.Array[np.intp], ...])
assert_type(np.nonzero(AR_1d), tuple[_nt.Array[np.intp], ...])
assert_type(np.nonzero(AR_nd), tuple[_nt.Array[np.intp], ...])

assert_type(np.shape(b1), tuple[()])
assert_type(np.shape(f_0d), tuple[()])
assert_type(np.shape(i_1d), tuple[int])
assert_type(np.shape(i_2d), tuple[int, int])
assert_type(np.shape(i_3d), tuple[int, int, int])
assert_type(np.shape(i_4d), tuple[int, ...])
assert_type(np.shape(AR_b1), tuple[Any, ...])
assert_type(np.shape(AR_nd), tuple[int, ...])
# these fail on mypy, but it works as expected with pyright/pylance
assert_type(np.shape(AR_0d), tuple[()])  # type: ignore[assert-type]
assert_type(np.shape(AR_1d), tuple[int])  # type: ignore[assert-type]

assert_type(np.compress(b_1d, b1), _nt.Array[np.bool])
assert_type(np.compress(b_1d, f4), _nt.Array[np.float32])
assert_type(np.compress(b_1d, f_0d), _nt.Array[Any])
assert_type(np.compress(b_1d, AR_b1), _nt.Array[np.bool])
assert_type(np.compress(b_1d, AR_f4), _nt.Array[np.float32])

assert_type(np.clip(b1, 0, 1.0), np.bool)
assert_type(np.clip(f4, -1, 1), np.float32)
assert_type(np.clip(f_0d, 0, 1), Any)
assert_type(np.clip(AR_b1, 0, 1), _nt.Array[np.bool])
assert_type(np.clip(AR_f4, 0, 1), _nt.Array[np.float32])
assert_type(np.clip(i_1d, 0, 1), _nt.Array[Any])
assert_type(np.clip(AR_b1, 0, 1, out=AR_subclass), NDArraySubclass)

assert_type(np.sum(b1), np.bool)
assert_type(np.sum(f4), np.float32)
assert_type(np.sum(f_0d), Any)
assert_type(np.sum(AR_b1), np.bool)
assert_type(np.sum(AR_f4), np.float32)
assert_type(np.sum(AR_b1, axis=0), Any)
assert_type(np.sum(AR_f4, axis=0), Any)
assert_type(np.sum(AR_f4, out=AR_subclass), NDArraySubclass)
assert_type(np.sum(AR_f4, dtype=np.float64), np.float64)
assert_type(np.sum(AR_f4, None, np.float64), np.float64)
assert_type(np.sum(AR_f4, dtype=np.float64, keepdims=False), np.float64)
assert_type(np.sum(AR_f4, None, np.float64, keepdims=False), np.float64)
assert_type(np.sum(AR_f4, dtype=np.float64, keepdims=True), np.float64 | _nt.Array[np.float64])
assert_type(np.sum(AR_f4, None, np.float64, keepdims=True), np.float64 | _nt.Array[np.float64])

assert_type(np.all(b1), np.bool)
assert_type(np.all(f4), np.bool)
assert_type(np.all(f_0d), np.bool)
assert_type(np.all(AR_b1), np.bool)
assert_type(np.all(AR_f4), np.bool)
assert_type(np.all(AR_b1, axis=0), np.bool | _nt.Array[np.bool])
assert_type(np.all(AR_f4, axis=0), np.bool | _nt.Array[np.bool])
assert_type(np.all(AR_b1, keepdims=True), _nt.Array[np.bool])
assert_type(np.all(AR_f4, keepdims=True), _nt.Array[np.bool])
assert_type(np.all(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.any(b1), np.bool)
assert_type(np.any(f4), np.bool)
assert_type(np.any(f_0d), np.bool)
assert_type(np.any(AR_b1), np.bool)
assert_type(np.any(AR_f4), np.bool)
assert_type(np.any(AR_b1, axis=0), np.bool | _nt.Array[np.bool])
assert_type(np.any(AR_f4, axis=0), np.bool | _nt.Array[np.bool])
assert_type(np.any(AR_b1, keepdims=True), _nt.Array[np.bool])
assert_type(np.any(AR_f4, keepdims=True), _nt.Array[np.bool])
assert_type(np.any(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.cumsum(b1), _nt.Array[np.bool])
assert_type(np.cumsum(f4), _nt.Array[np.float32])
assert_type(np.cumsum(f_0d), _nt.Array[Any])
assert_type(np.cumsum(AR_b1), _nt.Array[np.bool])
assert_type(np.cumsum(AR_f4), _nt.Array[np.float32])
assert_type(np.cumsum(f_0d, dtype=float), _nt.Array[Any])
assert_type(np.cumsum(f_0d, dtype=np.float64), _nt.Array[np.float64])
assert_type(np.cumsum(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.cumulative_sum(b1), _nt.Array[np.bool])
assert_type(np.cumulative_sum(f4), _nt.Array[np.float32])
assert_type(np.cumulative_sum(f_0d), _nt.Array[Any])
assert_type(np.cumulative_sum(AR_b1), _nt.Array[np.bool])
assert_type(np.cumulative_sum(AR_f4), _nt.Array[np.float32])
assert_type(np.cumulative_sum(f_0d, dtype=float), _nt.Array[Any])
assert_type(np.cumulative_sum(f_0d, dtype=np.float64), _nt.Array[np.float64])
assert_type(np.cumulative_sum(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.ptp(b1), np.bool)
assert_type(np.ptp(f4), np.float32)
assert_type(np.ptp(f_0d), Any)
assert_type(np.ptp(AR_b1), np.bool)
assert_type(np.ptp(AR_f4), np.float32)
assert_type(np.ptp(AR_b1, axis=0), Any)
assert_type(np.ptp(AR_f4, axis=0), Any)
assert_type(np.ptp(AR_b1, keepdims=True), Any)
assert_type(np.ptp(AR_f4, keepdims=True), Any)
assert_type(np.ptp(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.amax(b1), np.bool)
assert_type(np.amax(f4), np.float32)
assert_type(np.amax(f_0d), Any)
assert_type(np.amax(AR_b1), np.bool)
assert_type(np.amax(AR_f4), np.float32)
assert_type(np.amax(AR_b1, axis=0), Any)
assert_type(np.amax(AR_f4, axis=0), Any)
assert_type(np.amax(AR_b1, keepdims=True), Any)
assert_type(np.amax(AR_f4, keepdims=True), Any)
assert_type(np.amax(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.amin(b1), np.bool)
assert_type(np.amin(f4), np.float32)
assert_type(np.amin(f_0d), Any)
assert_type(np.amin(AR_b1), np.bool)
assert_type(np.amin(AR_f4), np.float32)
assert_type(np.amin(AR_b1, axis=0), Any)
assert_type(np.amin(AR_f4, axis=0), Any)
assert_type(np.amin(AR_b1, keepdims=True), Any)
assert_type(np.amin(AR_f4, keepdims=True), Any)
assert_type(np.amin(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.prod(AR_b1), np.int_)
assert_type(np.prod(AR_u8), np.uint64)
assert_type(np.prod(AR_i8), np.int64)
assert_type(np.prod(AR_f4), np.floating)
assert_type(np.prod(AR_c16), np.complexfloating)
assert_type(np.prod(AR_O), Any)
assert_type(np.prod(AR_f4, axis=0), Any)
assert_type(np.prod(AR_f4, keepdims=True), Any)
assert_type(np.prod(AR_f4, dtype=np.float64), np.float64)
assert_type(np.prod(AR_f4, dtype=float), Any)
assert_type(np.prod(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.cumprod(AR_b1), _nt.Array[np.int_])
assert_type(np.cumprod(AR_u8), _nt.Array[np.uint64])
assert_type(np.cumprod(AR_i8), _nt.Array[np.int64])
assert_type(np.cumprod(AR_f4), _nt.Array[np.floating])
assert_type(np.cumprod(AR_c16), _nt.Array[np.complexfloating])
assert_type(np.cumprod(AR_O), _nt.Array[np.object_])
assert_type(np.cumprod(AR_f4, axis=0), _nt.Array[np.floating])
assert_type(np.cumprod(AR_f4, dtype=np.float64), _nt.Array[np.float64])
assert_type(np.cumprod(AR_f4, dtype=float), _nt.Array[Any])
assert_type(np.cumprod(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.cumulative_prod(AR_b1), _nt.Array[np.int_])
assert_type(np.cumulative_prod(AR_u8), _nt.Array[np.uint64])
assert_type(np.cumulative_prod(AR_i8), _nt.Array[np.int64])
assert_type(np.cumulative_prod(AR_f4), _nt.Array[np.floating])
assert_type(np.cumulative_prod(AR_c16), _nt.Array[np.complexfloating])
assert_type(np.cumulative_prod(AR_O), _nt.Array[np.object_])
assert_type(np.cumulative_prod(AR_f4, axis=0), _nt.Array[np.floating])
assert_type(np.cumulative_prod(AR_f4, dtype=np.float64), _nt.Array[np.float64])
assert_type(np.cumulative_prod(AR_f4, dtype=float), _nt.Array[Any])
assert_type(np.cumulative_prod(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.ndim(b1), int)
assert_type(np.ndim(f4), int)
assert_type(np.ndim(f_0d), int)
assert_type(np.ndim(AR_b1), int)
assert_type(np.ndim(AR_f4), int)

assert_type(np.size(b1), int)
assert_type(np.size(f4), int)
assert_type(np.size(f_0d), int)
assert_type(np.size(AR_b1), int)
assert_type(np.size(AR_f4), int)

assert_type(np.around(b1), np.float16)
assert_type(np.around(f_0d), np.float64)
assert_type(np.around(i8), np.int64)
assert_type(np.around(f4), np.float32)
assert_type(np.around(AR_b1), _nt.Array[np.float16])
assert_type(np.around(AR_i8), _nt.Array[np.int64])
assert_type(np.around(AR_f4), _nt.Array[np.float32])
assert_type(np.around(f_1d), _nt.Array[Any])
assert_type(np.around(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.mean(AR_b1), np.floating)
assert_type(np.mean(AR_i8), np.floating)
assert_type(np.mean(AR_f4), np.floating)
# mypy incorrectly infers this as "Any" but pyright behaves correctly
assert_type(np.mean(AR_m), np.timedelta64)  # type: ignore[assert-type]
assert_type(np.mean(AR_c16), np.complexfloating)
assert_type(np.mean(AR_O), Any)
assert_type(np.mean(AR_f4, axis=0), Any)
assert_type(np.mean(AR_f4, keepdims=True), Any)
assert_type(np.mean(AR_f4, dtype=float), Any)
assert_type(np.mean(AR_f4, dtype=np.float64), np.float64)
assert_type(np.mean(AR_f4, out=AR_subclass), NDArraySubclass)
assert_type(np.mean(AR_f4, dtype=np.float64), np.float64)
assert_type(np.mean(AR_f4, None, np.float64), np.float64)
assert_type(np.mean(AR_f4, dtype=np.float64, keepdims=False), np.float64)
assert_type(np.mean(AR_f4, None, np.float64, keepdims=False), np.float64)
assert_type(np.mean(AR_f4, dtype=np.float64, keepdims=True), np.float64 | _nt.Array[np.float64])
assert_type(np.mean(AR_f4, None, np.float64, keepdims=True), np.float64 | _nt.Array[np.float64])

assert_type(np.std(AR_b1), np.floating)
assert_type(np.std(AR_i8), np.floating)
assert_type(np.std(AR_f4), np.floating)
assert_type(np.std(AR_c16), np.floating)
assert_type(np.std(AR_O), Any)
assert_type(np.std(AR_f4, axis=0), Any)
assert_type(np.std(AR_f4, keepdims=True), Any)
assert_type(np.std(AR_f4, dtype=float), Any)
assert_type(np.std(AR_f4, dtype=np.float64), np.float64)
assert_type(np.std(AR_f4, out=AR_subclass), NDArraySubclass)

assert_type(np.var(AR_b1), np.floating)
assert_type(np.var(AR_i8), np.floating)
assert_type(np.var(AR_f4), np.floating)
assert_type(np.var(AR_c16), np.floating)
assert_type(np.var(AR_O), Any)
assert_type(np.var(AR_f4, axis=0), Any)
assert_type(np.var(AR_f4, keepdims=True), Any)
assert_type(np.var(AR_f4, dtype=float), Any)
assert_type(np.var(AR_f4, dtype=np.float64), np.float64)
assert_type(np.var(AR_f4, out=AR_subclass), NDArraySubclass)
