from collections.abc import Callable
from fractions import Fraction
from typing import Any, TypeAlias
from typing_extensions import LiteralString, TypeVar, assert_type

import numpy as np
import numpy.typing as npt

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic, default=Any)
_Array1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_ScalarT]]
_Array2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_ScalarT]]
_Array3D: TypeAlias = np.ndarray[tuple[int, int, int], np.dtype[_ScalarT]]
_Array4D: TypeAlias = np.ndarray[tuple[int, int, int, int], np.dtype[_ScalarT]]

###

vectorized_func: np.vectorize

f8: np.float64
AR_LIKE_f8: list[float]
AR_LIKE_c16: list[complex]
AR_LIKE_O: list[Fraction]

AR_i8: npt.NDArray[np.int64]
AR_f8: npt.NDArray[np.float64]
AR_c16: npt.NDArray[np.complex128]
AR_m: npt.NDArray[np.timedelta64]
AR_M: npt.NDArray[np.datetime64]
AR_O: npt.NDArray[np.object_]
AR_b: npt.NDArray[np.bool]
AR_U: npt.NDArray[np.str_]
CHAR_AR_U: np.char.chararray[tuple[int, ...], np.dtype[np.str_]]

AR_b_list: list[npt.NDArray[np.bool]]

def func(a: npt.NDArray[Any], posarg: bool = ..., /, arg: int = ..., *, kwarg: str = ...) -> npt.NDArray[Any]: ...

###

assert_type(vectorized_func.pyfunc, Callable[..., Any])
assert_type(vectorized_func.cache, bool)
assert_type(vectorized_func.signature, LiteralString | None)
assert_type(vectorized_func.otypes, LiteralString | None)
assert_type(vectorized_func.excluded, set[int | str])
assert_type(vectorized_func.__doc__, str | None)
assert_type(vectorized_func([1]), Any)
assert_type(np.vectorize(int), np.vectorize)
assert_type(
    np.vectorize(int, otypes="i", doc="doc", excluded=(), cache=True, signature=None),
    np.vectorize,
)

assert_type(np.rot90(AR_f8, k=2), npt.NDArray[np.float64])
assert_type(np.rot90(AR_LIKE_f8, axes=(0, 1)), npt.NDArray[Any])

assert_type(np.flip(f8), np.float64)
assert_type(np.flip(1.0), Any)
assert_type(np.flip(AR_f8, axis=(0, 1)), npt.NDArray[np.float64])
assert_type(np.flip(AR_LIKE_f8, axis=0), npt.NDArray[Any])

assert_type(np.iterable(1), bool)
assert_type(np.iterable([1]), bool)

assert_type(np.average(AR_f8), np.float64)
assert_type(np.average(AR_f8, returned=True), tuple[np.float64, np.float64])
assert_type(np.average(AR_f8, weights=AR_c16), np.complexfloating)
assert_type(np.average(AR_f8, weights=AR_c16, returned=True), tuple[np.complexfloating, np.complexfloating])
assert_type(np.average(AR_O), Any)
assert_type(np.average(AR_O, returned=True), tuple[Any, Any])
assert_type(np.average(AR_f8, axis=0), Any)
assert_type(np.average(AR_f8, axis=0, returned=True), tuple[Any, Any])

assert_type(np.asarray_chkfinite(AR_f8), npt.NDArray[np.float64])
assert_type(np.asarray_chkfinite(AR_LIKE_f8), npt.NDArray[Any])
assert_type(np.asarray_chkfinite(AR_f8, dtype=np.float64), npt.NDArray[np.float64])
assert_type(np.asarray_chkfinite(AR_f8, dtype=float), npt.NDArray[Any])

assert_type(np.piecewise(AR_f8, AR_b, [func]), npt.NDArray[np.float64])
assert_type(np.piecewise(AR_f8, AR_b_list, [func]), npt.NDArray[np.float64])
assert_type(np.piecewise(AR_f8, AR_b_list, [func], True, -1, kwarg=""), npt.NDArray[np.float64])
assert_type(np.piecewise(AR_f8, AR_b_list, [func], True, arg=-1, kwarg=""), npt.NDArray[np.float64])
assert_type(np.piecewise(AR_LIKE_f8, AR_b_list, [func]), npt.NDArray[Any])

assert_type(np.select([AR_f8], [AR_f8]), npt.NDArray[np.float64])

assert_type(np.copy(AR_LIKE_f8), npt.NDArray[Any])
assert_type(np.copy(AR_U), npt.NDArray[np.str_])
assert_type(np.copy(CHAR_AR_U), npt.NDArray[np.str_])
assert_type(np.copy(CHAR_AR_U, "K", subok=True), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])
assert_type(np.copy(CHAR_AR_U, subok=True), np.char.chararray[tuple[int, ...], np.dtype[np.str_]])

assert_type(np.gradient(AR_f8, axis=None), Any)
assert_type(np.gradient(AR_LIKE_f8, edge_order=2), Any)

assert_type(np.diff("bob", n=0), str)
assert_type(np.diff(AR_f8, axis=0), npt.NDArray[np.float64])
assert_type(np.diff(AR_LIKE_f8, prepend=1.5), npt.NDArray[Any])

assert_type(np.interp(1, [1], AR_f8), np.float64)
assert_type(np.interp(1, [1], [1]), np.float64)
assert_type(np.interp(1, [1], AR_c16), np.complex128)
assert_type(np.interp([1], [1], AR_f8), npt.NDArray[np.float64])
assert_type(np.interp([1], [1], [1]), npt.NDArray[np.float64])
assert_type(np.interp([1], [1], AR_c16), npt.NDArray[np.complex128])
# mypy is incorrect here
assert_type(np.interp(1, [1], [1j]), np.float64 | np.complex128)  # type: ignore[assert-type]
assert_type(np.interp([1], [1], [1j]), npt.NDArray[np.float64 | np.complex128])  # type: ignore[assert-type]

assert_type(np.angle(f8), np.floating)
assert_type(np.angle(AR_f8), npt.NDArray[np.floating])
assert_type(np.angle(AR_c16, deg=True), npt.NDArray[np.floating])
assert_type(np.angle(AR_O), npt.NDArray[np.object_])

assert_type(np.unwrap(AR_f8), npt.NDArray[np.floating])
assert_type(np.unwrap(AR_O), npt.NDArray[np.object_])

assert_type(np.sort_complex(AR_f8), npt.NDArray[np.complexfloating])

assert_type(np.trim_zeros(AR_f8), npt.NDArray[np.float64])
assert_type(np.trim_zeros(AR_LIKE_f8), list[float])

assert_type(np.extract(AR_i8, AR_f8), npt.NDArray[np.float64])
assert_type(np.extract(AR_i8, AR_LIKE_f8), npt.NDArray[Any])

assert_type(np.place(AR_f8, mask=AR_i8, vals=5.0), None)

assert_type(np.cov(AR_f8, bias=True), npt.NDArray[np.float64])
assert_type(np.cov(AR_f8, AR_c16, ddof=1), npt.NDArray[np.complex128])
assert_type(np.cov(AR_f8, aweights=AR_f8, dtype=np.float32), npt.NDArray[np.float32])
assert_type(np.cov(AR_f8, fweights=AR_i8, dtype=float), npt.NDArray[np.float64])

assert_type(np.corrcoef(AR_f8, rowvar=True), npt.NDArray[np.float64])
assert_type(np.corrcoef(AR_f8, AR_c16), npt.NDArray[np.complex128])
assert_type(np.corrcoef(AR_f8, dtype=np.float32), npt.NDArray[np.float32])
assert_type(np.corrcoef(AR_f8, dtype=float), npt.NDArray[np.float64])

assert_type(np.blackman(5), _Array1D[np.floating])
assert_type(np.bartlett(6), _Array1D[np.floating])
assert_type(np.hanning(4.5), _Array1D[np.floating])
assert_type(np.hamming(0), _Array1D[np.floating])
assert_type(np.kaiser(4, 5.9), _Array1D[np.floating])
assert_type(np.i0(AR_i8), npt.NDArray[np.floating])

assert_type(np.sinc(1.0), np.floating)
assert_type(np.sinc(1j), np.complexfloating)
assert_type(np.sinc(AR_f8), npt.NDArray[np.floating])
assert_type(np.sinc(AR_c16), npt.NDArray[np.complexfloating])

assert_type(np.median(AR_f8, keepdims=False), np.floating)
assert_type(np.median(AR_c16, overwrite_input=True), np.complexfloating)
assert_type(np.median(AR_m), np.timedelta64)
assert_type(np.median(AR_O), Any)
assert_type(np.median(AR_f8, keepdims=True), Any)
assert_type(np.median(AR_c16, axis=0), Any)
assert_type(np.median(AR_LIKE_f8, out=AR_c16), npt.NDArray[np.complex128])

assert_type(np.percentile(AR_f8, 50), np.floating)
assert_type(np.percentile(AR_c16, 50), np.complexfloating)
assert_type(np.percentile(AR_m, 50), np.timedelta64)
assert_type(np.percentile(AR_M, 50, overwrite_input=True), np.datetime64)
assert_type(np.percentile(AR_O, 50), Any)
assert_type(np.percentile(AR_f8, [50]), npt.NDArray[np.floating])
assert_type(np.percentile(AR_c16, [50]), npt.NDArray[np.complexfloating])
assert_type(np.percentile(AR_m, [50]), npt.NDArray[np.timedelta64])
assert_type(np.percentile(AR_M, [50], method="nearest"), npt.NDArray[np.datetime64])
assert_type(np.percentile(AR_O, [50]), npt.NDArray[np.object_])
assert_type(np.percentile(AR_f8, [50], keepdims=True), Any)
assert_type(np.percentile(AR_f8, [50], axis=[1]), Any)
assert_type(np.percentile(AR_f8, [50], out=AR_c16), npt.NDArray[np.complex128])

assert_type(np.quantile(AR_f8, 0.5), np.floating)
assert_type(np.quantile(AR_c16, 0.5), np.complexfloating)
assert_type(np.quantile(AR_m, 0.5), np.timedelta64)
assert_type(np.quantile(AR_M, 0.5, overwrite_input=True), np.datetime64)
assert_type(np.quantile(AR_O, 0.5), Any)
assert_type(np.quantile(AR_f8, [0.5]), npt.NDArray[np.floating])
assert_type(np.quantile(AR_c16, [0.5]), npt.NDArray[np.complexfloating])
assert_type(np.quantile(AR_m, [0.5]), npt.NDArray[np.timedelta64])
assert_type(np.quantile(AR_M, [0.5], method="nearest"), npt.NDArray[np.datetime64])
assert_type(np.quantile(AR_O, [0.5]), npt.NDArray[np.object_])
assert_type(np.quantile(AR_f8, [0.5], keepdims=True), Any)
assert_type(np.quantile(AR_f8, [0.5], axis=[1]), Any)
assert_type(np.quantile(AR_f8, [0.5], out=AR_c16), npt.NDArray[np.complex128])

assert_type(np.trapezoid(AR_LIKE_f8), np.float64)
assert_type(np.trapezoid(AR_LIKE_f8, AR_LIKE_f8), np.float64)
assert_type(np.trapezoid(AR_LIKE_c16), np.complexfloating)
assert_type(np.trapezoid(AR_LIKE_c16, AR_LIKE_f8), np.complexfloating)
assert_type(np.trapezoid(AR_LIKE_f8, AR_LIKE_c16), np.complexfloating)
# pyright bug: https://github.com/microsoft/pyright/issues/9896
assert_type(np.trapezoid(AR_LIKE_O), float)  # pyright: ignore[reportAssertTypeFailure]
assert_type(np.trapezoid(AR_LIKE_O, AR_LIKE_f8), float)  # pyright: ignore[reportAssertTypeFailure]
assert_type(np.trapezoid(AR_f8), np.floating | npt.NDArray[np.floating])
assert_type(np.trapezoid(AR_f8, AR_f8), np.floating | npt.NDArray[np.floating])
assert_type(np.trapezoid(AR_c16), np.complexfloating | npt.NDArray[np.complexfloating])
assert_type(np.trapezoid(AR_c16, AR_c16), np.complexfloating | npt.NDArray[np.complexfloating])
assert_type(np.trapezoid(AR_m), np.timedelta64 | npt.NDArray[np.timedelta64])
assert_type(np.trapezoid(AR_O), Any)
assert_type(np.trapezoid(AR_O, AR_LIKE_f8), Any)

assert_type(np.meshgrid(), tuple[()])
assert_type(np.meshgrid(AR_c16, indexing="ij"), tuple[_Array1D[np.complex128]])
assert_type(np.meshgrid(AR_i8, AR_f8, copy=False), tuple[_Array2D[np.int64], _Array2D[np.float64]])
assert_type(np.meshgrid(AR_LIKE_f8, AR_f8), tuple[_Array2D, _Array2D[np.float64]])
assert_type(np.meshgrid(AR_LIKE_f8, AR_i8, AR_c16), tuple[_Array3D, _Array3D, _Array3D])
assert_type(np.meshgrid(AR_f8, AR_f8, AR_f8, AR_f8), tuple[_Array4D, _Array4D, _Array4D, _Array4D])
assert_type(np.meshgrid(*AR_LIKE_f8), tuple[npt.NDArray[Any], ...])

assert_type(np.delete(AR_f8, np.s_[:5]), npt.NDArray[np.float64])
assert_type(np.delete(AR_LIKE_f8, [0, 4, 9], axis=0), npt.NDArray[Any])

assert_type(np.insert(AR_f8, np.s_[:5], 5), npt.NDArray[np.float64])
assert_type(np.insert(AR_LIKE_f8, [0, 4, 9], [0.5, 9.2, 7], axis=0), npt.NDArray[Any])

assert_type(np.append(AR_f8, 5), npt.NDArray[Any])
assert_type(np.append(AR_LIKE_f8, 1j, axis=0), npt.NDArray[Any])

assert_type(np.digitize(4.5, [1]), np.intp)
assert_type(np.digitize(AR_f8, [1, 2, 3]), npt.NDArray[np.intp])
