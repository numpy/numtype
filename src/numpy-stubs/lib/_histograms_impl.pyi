from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Literal as L, SupportsIndex, TypeAlias

import _numtype as _nt
from numpy._typing import ArrayLike

__all__ = ["histogram", "histogram_bin_edges", "histogramdd"]

###

_BinKind: TypeAlias = L["stone", "auto", "doane", "fd", "rice", "scott", "sqrt", "sturges"]

###

def histogram_bin_edges(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: tuple[float, float] | None = None,
    weights: ArrayLike | None = None,
) -> _nt.Array[Incomplete]: ...

#
def histogram(
    a: ArrayLike,
    bins: _BinKind | SupportsIndex | ArrayLike = 10,
    range: tuple[float, float] | None = None,
    density: bool | None = None,
    weights: ArrayLike | None = None,
) -> tuple[_nt.Array[Incomplete], _nt.Array[Incomplete]]: ...

#
def histogramdd(
    sample: ArrayLike,
    bins: SupportsIndex | ArrayLike = 10,
    range: Sequence[tuple[float, float]] | None = None,
    density: bool | None = None,
    weights: ArrayLike | None = None,
) -> tuple[_nt.Array[Incomplete], tuple[_nt.Array[Incomplete], ...]]: ...
