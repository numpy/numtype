from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Any, Literal, Literal as L, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
from numpy import _OrderKACF  # noqa: ICN003

__all__ = ["einsum", "einsum_path"]

_ArrayT = TypeVar("_ArrayT", bound=_nt.Array[_nt.co_complex])

# TODO (@jorenham): Annotate the `Sequence` value (numpy/numtype#724)
_OptimizeKind: TypeAlias = bool | Literal["greedy", "optimal"] | Sequence[str | tuple[int, ...]]
_CastingSafe: TypeAlias = Literal["no", "equiv", "safe", "same_kind", "same_value"]
_CastingUnsafe: TypeAlias = Literal["unsafe"]

_ToDTypeUInt: TypeAlias = (
    _nt.ToDTypeUInt8 | _nt.ToDTypeUInt16 | _nt.ToDTypeUInt32 | _nt.ToDTypeUInt64 | _nt.ToDTypeULong
)
_ToDTypeInt: TypeAlias = _nt.ToDTypeInt8 | _nt.ToDTypeInt16 | _nt.ToDTypeInt32 | _nt.ToDTypeInt64 | _nt.ToDTypeLong
_ToDTypeFloat: TypeAlias = _nt.ToDTypeFloat16 | _nt.ToDTypeFloat32 | _nt.ToDTypeFloat64 | _nt.ToDTypeLongDouble
_ToDTypeComplex: TypeAlias = _nt.ToDTypeComplex64 | _nt.ToDTypeComplex128 | _nt.ToDTypeCLongDouble
_ToDTypeComplex_co: TypeAlias = _nt.ToDTypeBool | _ToDTypeUInt | _ToDTypeInt | _ToDTypeFloat | _ToDTypeComplex

# TODO: Properly handle the `casting`-based combinatorics
# TODO: We need to evaluate the content `__subscripts` in order
# to identify whether or an array or scalar is returned. At a cursory
# glance this seems like something that can quite easily be done with
# a mypy plugin.
# Something like `is_scalar = bool(__subscripts.partition("->")[-1])`
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.ToBool_nd,
    out: None = None,
    optimize: _OptimizeKind = False,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoUInt64_nd,
    out: None = None,
    dtype: _ToDTypeUInt | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoInteger_nd,
    out: None = None,
    dtype: _ToDTypeInt | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoFloating_nd,
    out: None = None,
    dtype: _ToDTypeFloat | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoComplex_nd,
    out: None = None,
    dtype: _ToDTypeComplex | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: Any,
    casting: _CastingUnsafe,
    dtype: _ToDTypeComplex_co | None = None,
    out: None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoComplex_nd,
    out: _ArrayT,
    dtype: _ToDTypeComplex_co | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: Any,
    out: _ArrayT,
    casting: _CastingUnsafe,
    dtype: _ToDTypeComplex_co | None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.ToObject_nd,
    out: None = None,
    dtype: _nt.ToDTypeObject | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: Any,
    casting: _CastingUnsafe,
    dtype: _nt.ToDTypeObject | None = None,
    out: None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> Incomplete: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.ToObject_nd,
    out: _ArrayT,
    dtype: _nt.ToDTypeObject | None = None,
    order: _OrderKACF = "K",
    casting: _CastingSafe = "safe",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...
@overload
def einsum(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: Any,
    out: _ArrayT,
    casting: _CastingUnsafe,
    dtype: _nt.ToDTypeObject | None = None,
    order: _OrderKACF = "K",
    optimize: _OptimizeKind = False,
) -> _ArrayT: ...

# TODO (@jorenham): Annotate the `Sequence` value (numpy/numtype#724)
# NOTE: `einsum_call` is a hidden kwarg unavailable for public use.
# It is therefore excluded from the signatures below.
def einsum_path(
    subscripts: str | _nt.CoInteger_nd,
    /,
    *operands: _nt.CoComplex_nd | _nt.ToDTypeObject,
    optimize: _OptimizeKind = "greedy",
    einsum_call: L[False] = False,
) -> tuple[list[str | tuple[int, ...]], str]: ...
