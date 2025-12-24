from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
from numpy import _OrderKACF  # noqa: ICN003
from numpy._typing import (
    _ArrayLikeBool_co,
    _ArrayLikeComplex_co,
    _ArrayLikeFloat_co,
    _ArrayLikeInt_co,
    _ArrayLikeObject_co,
    _ArrayLikeUInt_co,
    _DTypeLikeBool,
    _DTypeLikeComplex,
    _DTypeLikeComplex_co,
    _DTypeLikeFloat,
    _DTypeLikeInt,
    _DTypeLikeObject,
    _DTypeLikeUInt,
)

__all__ = ["einsum", "einsum_path"]

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array[_nt.co_complex])

# TODO (@jorenham): Annotate the `Sequence` value (numpy/numtype#724)
_OptimizeKind: TypeAlias = bool | Literal["greedy", "optimal"] | Sequence[str | tuple[int, ...]]
_CastingSafe: TypeAlias = Literal["no", "equiv", "safe", "same_kind", "same_value"]
_CastingUnsafe: TypeAlias = Literal["unsafe"]

# TODO: Properly handle the `casting`-based combinatorics
# TODO: We need to evaluate the content `__subscripts` in order
# to identify whether or an array or scalar is returned. At a cursory
# glance this seems like something that can quite easily be done with
# a mypy plugin.
# Something like `is_scalar = bool(__subscripts.partition("->")[-1])`
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeBool_co,
    out: None = None,
    optimize: _OptimizeKind = False,
    dtype: _DTypeLikeBool | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeUInt_co,
    out: None = None,
    dtype: _DTypeLikeUInt | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeInt_co,
    out: None = None,
    dtype: _DTypeLikeInt | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeFloat_co,
    out: None = None,
    dtype: _DTypeLikeFloat | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeComplex_co,
    out: None = None,
    dtype: _DTypeLikeComplex | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: Any,
    casting: _CastingUnsafe,
    dtype: _DTypeLikeComplex_co | None = None,
    out: None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeComplex_co,
    out: _ArrayT,
    dtype: _DTypeLikeComplex_co | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: Any,
    out: _ArrayT,
    casting: _CastingUnsafe,
    dtype: _DTypeLikeComplex_co | None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeObject_co,
    out: None = None,
    dtype: _DTypeLikeObject | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: Any,
    casting: _CastingUnsafe,
    dtype: _DTypeLikeObject | None = None,
    out: None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeObject_co,
    out: _ArrayT,
    dtype: _DTypeLikeObject | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: Any,
    out: _ArrayT,
    casting: _CastingUnsafe,
    dtype: _DTypeLikeObject | None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...

# TODO (@jorenham): Annotate the `Sequence` value (numpy/numtype#724)
# NOTE: `einsum_call` is a hidden kwarg unavailable for public use.
# It is therefore excluded from the signatures below.
def einsum_path(
    subscripts: str | _ArrayLikeInt_co,
    /,
    *operands: _ArrayLikeComplex_co | _DTypeLikeObject,
    optimize: _OptimizeKind = "greedy",
    einsum_call: L[False] = False,
) -> tuple[list[str | tuple[int, ...]], str]: ...
