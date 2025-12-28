import sys
from collections import deque
from pathlib import Path
from typing import Any, assert_type
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
import numpy.typing as npt

_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)

class MyArray(np.ndarray[_nt.Rank1, np.dtype[_ScalarT_co]]): ...

i8: np.int64

A: _nt.Array[np.float64]
B: MyArray[np.float64]
C: list[int]
D: MyArray[np.float64 | np.int64]

def func(i: int, j: int, **kwargs: object) -> MyArray[np.float64]: ...

assert_type(np.array(A), _nt.Array[np.float64])
assert_type(np.array(B), _nt.Array1D[np.float64])
assert_type(np.array(D), _nt.Array1D[np.float64 | np.int64])
assert_type(np.array([1, 1.0]), _nt.Array)
assert_type(np.array(deque([1, 2, 3])), _nt.Array)
assert_type(np.array(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.array(A, dtype="c16"), _nt.Array)
assert_type(np.array(A, like=A), _nt.Array[np.float64])
assert_type(np.array(A, subok=True), _nt.Array[np.float64])
assert_type(np.array(B, subok=True), MyArray[np.float64])
assert_type(np.array(B, subok=True, ndmin=0), MyArray[np.float64])
assert_type(np.array(B, subok=True, ndmin=1), MyArray[np.float64])

assert_type(np.zeros([1, 5, 6]), _nt.Array[np.float64])
assert_type(np.zeros([1, 5, 6], dtype=np.int64), _nt.Array[np.int64])
assert_type(np.zeros([1, 5, 6], dtype="c16"), _nt.Array)

assert_type(np.empty([1, 5, 6]), _nt.Array[np.float64])
assert_type(np.empty([1, 5, 6], dtype=np.int64), _nt.Array[np.int64])
assert_type(np.empty([1, 5, 6], dtype="c16"), _nt.Array)

assert_type(np.concatenate(A), _nt.Array[np.float64])
assert_type(np.concatenate([A, A]), _nt.Array[np.float64])  # type: ignore[assert-type]  # mypy fail
assert_type(np.concatenate([[1], A]), _nt.Array)
assert_type(np.concatenate([[1], [1]]), _nt.Array)
assert_type(np.concatenate((A, A)), _nt.Array[np.float64])
assert_type(np.concatenate(([1], [1])), _nt.Array)
assert_type(np.concatenate([1, 1.0]), _nt.Array)
assert_type(np.concatenate(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.concatenate(A, dtype="c16"), _nt.Array)
assert_type(np.concatenate([1, 1.0], out=A), _nt.Array[np.float64])

assert_type(np.asarray(A), _nt.Array[np.float64])
assert_type(np.asarray(B), _nt.Array1D[np.float64])
assert_type(np.asarray([1, 1.0]), _nt.Array)
assert_type(np.asarray(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.asarray(A, dtype="c16"), _nt.Array)

assert_type(np.asanyarray(A), _nt.Array[np.float64])
assert_type(np.asanyarray(B), MyArray[np.float64])
assert_type(np.asanyarray([1, 1.0]), _nt.Array)
assert_type(np.asanyarray(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.asanyarray(A, dtype="c16"), _nt.Array)

assert_type(np.ascontiguousarray(A), _nt.Array[np.float64])
assert_type(np.ascontiguousarray(B), _nt.Array1D[np.float64])
assert_type(np.ascontiguousarray([1, 1.0]), _nt.Array)
assert_type(np.ascontiguousarray(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.ascontiguousarray(A, dtype="c16"), _nt.Array)

assert_type(np.asfortranarray(A), _nt.Array[np.float64])
assert_type(np.asfortranarray(B), _nt.Array1D[np.float64])
assert_type(np.asfortranarray([1, 1.0]), _nt.Array)
assert_type(np.asfortranarray(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.asfortranarray(A, dtype="c16"), _nt.Array)

assert_type(np.fromstring("1 1 1", sep=" "), _nt.Array[np.float64])
assert_type(np.fromstring(b"1 1 1", sep=" "), _nt.Array[np.float64])
assert_type(np.fromstring("1 1 1", dtype=np.int64, sep=" "), _nt.Array[np.int64])
assert_type(np.fromstring(b"1 1 1", dtype=np.int64, sep=" "), _nt.Array[np.int64])
assert_type(np.fromstring("1 1 1", dtype="c16", sep=" "), _nt.Array)
assert_type(np.fromstring(b"1 1 1", dtype="c16", sep=" "), _nt.Array)

assert_type(np.fromfile("test.txt", sep=" "), _nt.Array[np.float64])
assert_type(np.fromfile("test.txt", dtype=np.int64, sep=" "), _nt.Array[np.int64])
assert_type(np.fromfile("test.txt", dtype="c16", sep=" "), _nt.Array)
with open("test.txt", encoding="utf-8") as f:
    assert_type(np.fromfile(f, sep=" "), _nt.Array[np.float64])
    assert_type(np.fromfile(b"test.txt", sep=" "), _nt.Array[np.float64])
    assert_type(np.fromfile(Path("test.txt"), sep=" "), _nt.Array[np.float64])

assert_type(np.fromiter("12345", np.float64), _nt.Array[np.float64])
assert_type(np.fromiter("12345", float), _nt.Array)

assert_type(np.frombuffer(A), _nt.Array[np.float64])
assert_type(np.frombuffer(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.frombuffer(A, dtype="c16"), _nt.Array)

assert_type(np.arange(False, True), _nt.Array1D[np.int_])
assert_type(np.arange(10), _nt.Array1D[np.int_])
assert_type(np.arange(0, 10, step=2), _nt.Array1D[np.int_])
assert_type(np.arange(10.0), _nt.Array1D[np.float64 | Any])
assert_type(np.arange(0, stop=10.0), _nt.Array1D[np.float64 | Any])
assert_type(np.arange(np.timedelta64(0)), _nt.Array1D[np.timedelta64[Any]])
assert_type(np.arange(0, np.timedelta64(10)), _nt.Array1D[np.timedelta64[Any]])
# mypy incorrectly infers this as "ndarray[Any, Any]" but pyright behaves correctly
assert_type(np.arange(np.datetime64("0"), np.datetime64("10")), _nt.Array1D[np.datetime64[Any]])  # type: ignore[assert-type]
assert_type(np.arange(10, dtype=np.float64), _nt.Array1D[np.float64 | Any])
assert_type(np.arange(0, 10, step=2, dtype=np.int16), _nt.Array1D[np.int16])
assert_type(np.arange(10, dtype=int), _nt.Array1D[np.int_])
assert_type(np.arange(0, 10, dtype="f8"), _nt.Array1D[Any])

assert_type(np.require(A), _nt.Array[np.float64])
assert_type(np.require(B), MyArray[np.float64])
assert_type(np.require(B, requirements=None), MyArray[np.float64])
assert_type(np.require(B, dtype=int), _nt.Array)
assert_type(np.require(B, requirements="E"), _nt.Array[np.float64])
assert_type(np.require(B, requirements=["ENSUREARRAY"]), _nt.Array[np.float64])
assert_type(np.require(B, requirements={"F", "E"}), _nt.Array[np.float64])
assert_type(np.require(B, requirements=["C", "OWNDATA"]), MyArray[np.float64])
assert_type(np.require(B, requirements="W"), MyArray[np.float64])
assert_type(np.require(B, requirements="A"), MyArray[np.float64])
assert_type(np.require(C), _nt.Array[np.intp])

assert_type(np.linspace(0, 10), _nt.Array1D[np.float64])
assert_type(np.linspace(0, 10j), _nt.Array1D[np.complex128 | Any])
assert_type(np.linspace(0, 10, dtype=np.int64), _nt.Array1D[np.int64])
assert_type(np.linspace(0, 10, dtype=int), _nt.Array)
assert_type(np.linspace(0, 10, retstep=True), tuple[_nt.Array1D[np.float64], np.float64])
assert_type(np.linspace(0j, 10, retstep=True), tuple[_nt.Array1D[np.complex128 | Any], np.complex128 | Any])
assert_type(np.linspace(0, 10, retstep=True, dtype=np.int64), tuple[_nt.Array1D[np.int64], np.int64])
assert_type(np.linspace(0j, 10, retstep=True, dtype=int), tuple[_nt.Array, Any])

assert_type(np.logspace(0, 10), _nt.Array1D[np.float64])
assert_type(np.logspace(0, 10j), _nt.Array1D[np.complex128 | Any])
assert_type(np.logspace(0, 10, dtype=np.int64), _nt.Array1D[np.int64])
assert_type(np.logspace(0, 10, dtype=int), _nt.Array)

assert_type(np.geomspace(0, 10), _nt.Array1D[np.float64])
assert_type(np.geomspace(0, 10j), _nt.Array1D[np.complex128 | Any])
assert_type(np.geomspace(0, 10, dtype=np.int64), _nt.Array1D[np.int64])
assert_type(np.geomspace(0, 10, dtype=int), _nt.Array)

assert_type(np.empty_like(A), _nt.Array[np.float64])
assert_type(np.empty_like(A, dtype=float), _nt.Array[np.float64])
assert_type(np.empty_like(A, shape=(2, 2)), _nt.Array2D[np.float64])
assert_type(np.empty_like(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.empty_like(A, dtype=np.int64, shape=(2, 2)), _nt.Array[np.int64, _nt.Shape2])
assert_type(np.empty_like(A, dtype="c16"), _nt.Array)
assert_type(np.empty_like(A, dtype="c16", shape=(2, 2)), np.ndarray[_nt.Shape2, np.dtype])
assert_type(np.empty_like(B), MyArray[np.float64])
assert_type(np.empty_like(B, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.empty_like(True), _nt.Array0D[np.bool])
assert_type(np.empty_like([True]), _nt.Array1D[np.bool])
assert_type(np.empty_like([[True]]), _nt.Array2D[np.bool])
assert_type(np.empty_like([[[True]]]), _nt.Array3D[np.bool])
assert_type(np.empty_like(2), _nt.Array0D[np.intp])
assert_type(np.empty_like([2]), _nt.Array1D[np.intp])
assert_type(np.empty_like([[2]]), _nt.Array2D[np.intp])
assert_type(np.empty_like([[[2]]]), _nt.Array3D[np.intp])
assert_type(np.empty_like(0.3), _nt.Array0D[np.float64])
assert_type(np.empty_like([0.3]), _nt.Array1D[np.float64])
assert_type(np.empty_like([[0.3]]), _nt.Array2D[np.float64])
assert_type(np.empty_like([[[0.3]]]), _nt.Array3D[np.float64])
assert_type(np.empty_like(4j), _nt.Array0D[np.complex128])
assert_type(np.empty_like([4j]), _nt.Array1D[np.complex128])
assert_type(np.empty_like([[4j]]), _nt.Array2D[np.complex128])
assert_type(np.empty_like([[[4j]]]), _nt.Array3D[np.complex128])

assert_type(np.zeros_like(A), _nt.Array[np.float64])
assert_type(np.zeros_like(A, dtype=float), _nt.Array[np.float64])
assert_type(np.zeros_like(A, shape=(2, 2)), _nt.Array2D[np.float64])
assert_type(np.zeros_like(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.zeros_like(A, dtype=np.int64, shape=(2, 2)), _nt.Array[np.int64, _nt.Shape2])
assert_type(np.zeros_like(A, dtype="c16"), _nt.Array)
assert_type(np.zeros_like(A, dtype="c16", shape=(2, 2)), np.ndarray[_nt.Shape2, np.dtype])
assert_type(np.zeros_like(B), MyArray[np.float64])
assert_type(np.zeros_like(B, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.zeros_like(True), _nt.Array0D[np.bool])
assert_type(np.zeros_like([True]), _nt.Array1D[np.bool])
assert_type(np.zeros_like([[True]]), _nt.Array2D[np.bool])
assert_type(np.zeros_like([[[True]]]), _nt.Array3D[np.bool])
assert_type(np.zeros_like(2), _nt.Array0D[np.intp])
assert_type(np.zeros_like([2]), _nt.Array1D[np.intp])
assert_type(np.zeros_like([[2]]), _nt.Array2D[np.intp])
assert_type(np.zeros_like([[[2]]]), _nt.Array3D[np.intp])
assert_type(np.zeros_like(0.3), _nt.Array0D[np.float64])
assert_type(np.zeros_like([0.3]), _nt.Array1D[np.float64])
assert_type(np.zeros_like([[0.3]]), _nt.Array2D[np.float64])
assert_type(np.zeros_like([[[0.3]]]), _nt.Array3D[np.float64])
assert_type(np.zeros_like(4j), _nt.Array0D[np.complex128])
assert_type(np.zeros_like([4j]), _nt.Array1D[np.complex128])
assert_type(np.zeros_like([[4j]]), _nt.Array2D[np.complex128])
assert_type(np.zeros_like([[[4j]]]), _nt.Array3D[np.complex128])

assert_type(np.ones_like(A), _nt.Array[np.float64])
assert_type(np.ones_like(A, dtype=float), _nt.Array[np.float64])
assert_type(np.ones_like(A, shape=(2, 2)), _nt.Array2D[np.float64])
assert_type(np.ones_like(A, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.ones_like(A, dtype=np.int64, shape=(2, 2)), _nt.Array[np.int64, _nt.Shape2])
assert_type(np.ones_like(A, dtype="c16"), _nt.Array)
assert_type(np.ones_like(A, dtype="c16", shape=(2, 2)), np.ndarray[_nt.Shape2, np.dtype])
assert_type(np.ones_like(B), MyArray[np.float64])
assert_type(np.ones_like(B, dtype=np.int64), _nt.Array[np.int64])
assert_type(np.ones_like(True), _nt.Array0D[np.bool])
assert_type(np.ones_like([True]), _nt.Array1D[np.bool])
assert_type(np.ones_like([[True]]), _nt.Array2D[np.bool])
assert_type(np.ones_like([[[True]]]), _nt.Array3D[np.bool])
assert_type(np.ones_like(2), _nt.Array0D[np.intp])
assert_type(np.ones_like([2]), _nt.Array1D[np.intp])
assert_type(np.ones_like([[2]]), _nt.Array2D[np.intp])
assert_type(np.ones_like([[[2]]]), _nt.Array3D[np.intp])
assert_type(np.ones_like(0.3), _nt.Array0D[np.float64])
assert_type(np.ones_like([0.3]), _nt.Array1D[np.float64])
assert_type(np.ones_like([[0.3]]), _nt.Array2D[np.float64])
assert_type(np.ones_like([[[0.3]]]), _nt.Array3D[np.float64])
assert_type(np.ones_like(4j), _nt.Array0D[np.complex128])
assert_type(np.ones_like([4j]), _nt.Array1D[np.complex128])
assert_type(np.ones_like([[4j]]), _nt.Array2D[np.complex128])
assert_type(np.ones_like([[[4j]]]), _nt.Array3D[np.complex128])

assert_type(np.full_like(A, i8), _nt.Array[np.float64])
assert_type(np.full_like(C, i8), _nt.Array1D[np.intp])
assert_type(np.full_like(A, i8, dtype=int), _nt.Array)
assert_type(np.full_like(B, i8), MyArray[np.float64])
assert_type(np.full_like(B, i8, dtype=np.int64), _nt.Array[np.int64])

_size: int
_shape_0d: _nt.Shape0
_shape_1d: _nt.Shape1
_shape_2d: _nt.Shape2
_shape_nd: _nt.Shape
_shape_like: list[int]

assert_type(np.ones(_shape_0d), _nt.Array[np.float64, _nt.Shape0])
assert_type(np.ones(_size), _nt.Array1D[np.float64])
assert_type(np.ones(_shape_2d), _nt.Array[np.float64, _nt.Shape2])
assert_type(np.ones(_shape_nd), np.ndarray[_nt.Shape, np.dtype[np.float64]])
assert_type(np.ones(_shape_1d, dtype=np.int64), _nt.Array1D[np.int64])
assert_type(np.ones(_shape_like), _nt.Array[np.float64])
assert_type(np.ones(_shape_like, dtype=np.dtypes.StringDType()), np.ndarray[_nt.AnyShape, np.dtypes.StringDType])
assert_type(np.ones(_shape_like, dtype=int), _nt.Array)

assert_type(np.full(_size, i8), _nt.Array1D[np.int64])
assert_type(np.full(_shape_2d, i8), _nt.Array[np.int64, _nt.Shape2])
assert_type(np.full(_shape_like, i8), _nt.Array[np.int64])
assert_type(np.full(_shape_like, True), _nt.Array[np.bool])
assert_type(np.full(_shape_like, 42), _nt.Array[np.intp])
assert_type(np.full(_shape_like, 0.3), _nt.Array[np.float64])
assert_type(np.full(_shape_like, 2j), _nt.Array[np.complex128])
assert_type(np.full(_size, i8, dtype=np.float64), _nt.Array1D[np.float64])
assert_type(np.full(_size, i8, dtype=float), _nt.Array1D[np.float64])
assert_type(np.full(_shape_like, 42, dtype=float), _nt.Array[np.float64])
assert_type(np.full(_shape_0d, i8, dtype=object), np.ndarray[_nt.Shape0, np.dtype])

assert_type(np.indices([1, 2, 3]), _nt.Array[np.int_])
assert_type(np.indices([1, 2, 3], sparse=True), tuple[_nt.Array[np.int_], ...])

assert_type(np.fromfunction(func, (3, 5)), MyArray[np.float64])

assert_type(np.identity(10), _nt.Array2D[np.float64])
assert_type(np.identity(10, dtype=np.int64), _nt.Array2D[np.int64])
assert_type(np.identity(10, dtype=int), _nt.Array2D)

assert_type(np.atleast_1d(A), _nt.Array[np.float64])
assert_type(np.atleast_1d(C), _nt.Array)
assert_type(np.atleast_1d(A, A), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(np.atleast_1d(A, C), tuple[_nt.Array, _nt.Array])
assert_type(np.atleast_1d(C, C), tuple[_nt.Array, _nt.Array])
assert_type(np.atleast_1d(A, A, A), tuple[_nt.Array[np.float64], ...])
assert_type(np.atleast_1d(C, C, C), tuple[_nt.Array, ...])

assert_type(np.atleast_2d(A), _nt.Array[np.float64])
assert_type(np.atleast_2d(A, A), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(np.atleast_2d(A, A, A), tuple[_nt.Array[np.float64], ...])

assert_type(np.atleast_3d(A), _nt.Array[np.float64])
assert_type(np.atleast_3d(A, A), tuple[_nt.Array[np.float64], _nt.Array[np.float64]])
assert_type(np.atleast_3d(A, A, A), tuple[_nt.Array[np.float64], ...])

assert_type(np.vstack([A, A]), _nt.Array[np.float64])
assert_type(np.vstack([A, A], dtype=np.float32), _nt.Array[np.float32])
assert_type(np.vstack([A, C]), _nt.Array)
assert_type(np.vstack([C, C]), _nt.Array)

assert_type(np.hstack([A, A]), _nt.Array[np.float64])
assert_type(np.hstack([A, A], dtype=np.float32), _nt.Array[np.float32])

assert_type(np.stack([A, A]), _nt.Array[np.float64])
assert_type(np.stack([A, A], dtype=np.float32), _nt.Array[np.float32])
assert_type(np.stack([A, C]), _nt.Array)
assert_type(np.stack([C, C]), _nt.Array)
assert_type(np.stack([A, A], axis=0), _nt.Array[np.float64])
assert_type(np.stack([A, A], out=B), MyArray[np.float64])

assert_type(np.block([[A, A], [A, A]]), _nt.Array)  # pyright: ignore[reportAssertTypeFailure]  # _nt.Array[np.float64]
assert_type(np.block(C), _nt.Array)

if sys.version_info >= (3, 12):
    from collections.abc import Buffer

    def create_array(obj: npt.ArrayLike) -> _nt.Array: ...

    buffer: Buffer
    assert_type(create_array(buffer), _nt.Array)
