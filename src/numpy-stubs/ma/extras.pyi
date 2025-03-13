from _typeshed import Incomplete
from typing import Final
from typing_extensions import override

import numpy as np
from numpy.lib._function_base_impl import average
from numpy.lib._index_tricks_impl import AxisConcatenator

from .core import MaskedArray, dot

__all__ = [
    "apply_along_axis",
    "apply_over_axes",
    "atleast_1d",
    "atleast_2d",
    "atleast_3d",
    "average",
    "clump_masked",
    "clump_unmasked",
    "column_stack",
    "compress_cols",
    "compress_nd",
    "compress_rowcols",
    "compress_rows",
    "corrcoef",
    "count_masked",
    "cov",
    "diagflat",
    "dot",
    "dstack",
    "ediff1d",
    "flatnotmasked_contiguous",
    "flatnotmasked_edges",
    "hsplit",
    "hstack",
    "in1d",
    "intersect1d",
    "isin",
    "mask_cols",
    "mask_rowcols",
    "mask_rows",
    "masked_all",
    "masked_all_like",
    "median",
    "mr_",
    "ndenumerate",
    "notmasked_contiguous",
    "notmasked_edges",
    "polyfit",
    "row_stack",
    "setdiff1d",
    "setxor1d",
    "stack",
    "union1d",
    "unique",
    "vander",
    "vstack",
]

class _fromnxfunction:
    __name__: str
    __doc__: str
    def __init__(self, funcname: Incomplete) -> None: ...
    def getdoc(self) -> Incomplete: ...
    def __call__(self, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

class _fromnxfunction_single(_fromnxfunction):
    __doc__: str
    @override
    def __call__(self, x: Incomplete, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

class _fromnxfunction_seq(_fromnxfunction):
    __doc__: str
    @override
    def __call__(self, x: Incomplete, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

class _fromnxfunction_allargs(_fromnxfunction):
    __doc__: str
    @override
    def __call__(self, *args: Incomplete, **params: Incomplete) -> Incomplete: ...

class MAxisConcatenator(AxisConcatenator):
    @staticmethod
    @override
    def concatenate(arrays: Incomplete, axis: int = 0) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @classmethod
    @override
    def makemat(cls, arr: Incomplete) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleVariableOverride]

class mr_class(MAxisConcatenator):
    def __init__(self) -> None: ...

def count_masked(arr: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def masked_all(shape: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def masked_all_like(arr: Incomplete) -> Incomplete: ...
def apply_along_axis(
    func1d: Incomplete,
    axis: Incomplete,
    arr: Incomplete,
    *args: Incomplete,
    **kwargs: Incomplete,
) -> Incomplete: ...
def apply_over_axes(func: Incomplete, a: Incomplete, axes: Incomplete) -> Incomplete: ...
def median(
    a: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    overwrite_input: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...
def compress_nd(x: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def compress_rowcols(x: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def compress_rows(a: Incomplete) -> Incomplete: ...
def compress_cols(a: Incomplete) -> Incomplete: ...
def mask_rows(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def mask_cols(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def ediff1d(arr: Incomplete, to_end: Incomplete = ..., to_begin: Incomplete = ...) -> Incomplete: ...
def unique(ar1: Incomplete, return_index: Incomplete = ..., return_inverse: Incomplete = ...) -> Incomplete: ...
def intersect1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def setxor1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def in1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ..., invert: Incomplete = ...) -> Incomplete: ...
def isin(
    element: Incomplete,
    test_elements: Incomplete,
    assume_unique: Incomplete = ...,
    invert: Incomplete = ...,
) -> Incomplete: ...
def union1d(ar1: Incomplete, ar2: Incomplete) -> Incomplete: ...
def setdiff1d(ar1: Incomplete, ar2: Incomplete, assume_unique: Incomplete = ...) -> Incomplete: ...
def cov(
    x: Incomplete,
    y: Incomplete = ...,
    rowvar: Incomplete = ...,
    bias: Incomplete = ...,
    allow_masked: Incomplete = ...,
    ddof: Incomplete = ...,
) -> Incomplete: ...
def corrcoef(
    x: Incomplete,
    y: Incomplete = ...,
    rowvar: Incomplete = ...,
    bias: Incomplete = ...,
    allow_masked: Incomplete = ...,
    ddof: Incomplete = ...,
) -> Incomplete: ...
def ndenumerate(a: Incomplete, compressed: Incomplete = ...) -> Incomplete: ...
def flatnotmasked_edges(a: Incomplete) -> Incomplete: ...
def notmasked_edges(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def flatnotmasked_contiguous(a: Incomplete) -> Incomplete: ...
def notmasked_contiguous(a: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def clump_unmasked(a: Incomplete) -> Incomplete: ...
def clump_masked(a: Incomplete) -> Incomplete: ...
def vander(x: Incomplete, n: Incomplete = ...) -> Incomplete: ...
def polyfit(
    x: Incomplete,
    y: Incomplete,
    deg: Incomplete,
    rcond: Incomplete = ...,
    full: Incomplete = ...,
    w: Incomplete = ...,
    cov: Incomplete = ...,
) -> Incomplete: ...

mr_: Final[mr_class] = ...

atleast_1d: _fromnxfunction_allargs
atleast_2d: _fromnxfunction_allargs
atleast_3d: _fromnxfunction_allargs

vstack: _fromnxfunction_seq
row_stack: _fromnxfunction_seq
hstack: _fromnxfunction_seq
column_stack: _fromnxfunction_seq
dstack: _fromnxfunction_seq
stack: _fromnxfunction_seq

hsplit: _fromnxfunction_single
diagflat: _fromnxfunction_single

def mask_rowcols(a: Incomplete, axis: Incomplete | None = None) -> MaskedArray[tuple[int, ...], np.dtype[Incomplete]]: ...
