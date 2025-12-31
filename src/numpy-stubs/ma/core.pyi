import datetime as dt
import types
from _typeshed import ConvertibleToFloat, ConvertibleToInt, Incomplete
from collections.abc import Callable, Iterator, Sequence
from typing import (
    Any,
    ClassVar,
    Concatenate,
    Final,
    Generic,
    Literal as L,
    Never,
    ParamSpec,
    Protocol,
    Self,
    SupportsComplex,
    SupportsIndex as CanIndex,
    TypeAlias,
    TypedDict,
    Unpack,
    final,
    overload,
    type_check_only,
)
from typing_extensions import Buffer, TypeVar, override

import _numtype as _nt
import numpy as np
from numpy import (  # noqa: ICN003
    _AnyItemT,
    _HasType,
    _OrderKACF,
    _PyComplexND,
    _PyFloatND,
    _PyIntND,
    _ToIndices,
    amax,
    amin,
    bool_,
    expand_dims,
)
from numpy._globals import _NoValueType
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    _ArrayLike,
    _DTypeLike,
    _ScalarLike_co,
    _ShapeLike,
    _SupportsArrayFunc as _CanArrayFunc,
    _SupportsDType as _HasDType,
    _VoidDTypeLike,
)

__all__ = [
    "MAError",
    "MaskError",
    "MaskType",
    "MaskedArray",
    "abs",
    "absolute",
    "add",
    "all",
    "allclose",
    "allequal",
    "alltrue",
    "amax",
    "amin",
    "angle",
    "anom",
    "anomalies",
    "any",
    "append",
    "arange",
    "arccos",
    "arccosh",
    "arcsin",
    "arcsinh",
    "arctan",
    "arctan2",
    "arctanh",
    "argmax",
    "argmin",
    "argsort",
    "around",
    "array",
    "asanyarray",
    "asarray",
    "bitwise_and",
    "bitwise_or",
    "bitwise_xor",
    "bool_",
    "ceil",
    "choose",
    "clip",
    "common_fill_value",
    "compress",
    "compressed",
    "concatenate",
    "conjugate",
    "convolve",
    "copy",
    "correlate",
    "cos",
    "cosh",
    "count",
    "cumprod",
    "cumsum",
    "default_fill_value",
    "diag",
    "diagonal",
    "diff",
    "divide",
    "empty",
    "empty_like",
    "equal",
    "exp",
    "expand_dims",
    "fabs",
    "filled",
    "fix_invalid",
    "flatten_mask",
    "flatten_structured_array",
    "floor",
    "floor_divide",
    "fmod",
    "frombuffer",
    "fromflex",
    "fromfunction",
    "getdata",
    "getmask",
    "getmaskarray",
    "greater",
    "greater_equal",
    "harden_mask",
    "hypot",
    "identity",
    "ids",
    "indices",
    "inner",
    "innerproduct",
    "isMA",
    "isMaskedArray",
    "is_mask",
    "is_masked",
    "isarray",
    "left_shift",
    "less",
    "less_equal",
    "log",
    "log2",
    "log10",
    "logical_and",
    "logical_not",
    "logical_or",
    "logical_xor",
    "make_mask",
    "make_mask_descr",
    "make_mask_none",
    "mask_or",
    "masked",
    "masked_array",
    "masked_equal",
    "masked_greater",
    "masked_greater_equal",
    "masked_inside",
    "masked_invalid",
    "masked_less",
    "masked_less_equal",
    "masked_not_equal",
    "masked_object",
    "masked_outside",
    "masked_print_option",
    "masked_singleton",
    "masked_values",
    "masked_where",
    "max",
    "maximum",
    "maximum_fill_value",
    "mean",
    "min",
    "minimum",
    "minimum_fill_value",
    "mod",
    "multiply",
    "mvoid",
    "ndim",
    "negative",
    "nomask",
    "nonzero",
    "not_equal",
    "ones",
    "ones_like",
    "outer",
    "outerproduct",
    "power",
    "prod",
    "product",
    "ptp",
    "put",
    "putmask",
    "ravel",
    "remainder",
    "repeat",
    "reshape",
    "resize",
    "right_shift",
    "round",
    "round_",
    "set_fill_value",
    "shape",
    "sin",
    "sinh",
    "size",
    "soften_mask",
    "sometrue",
    "sort",
    "sqrt",
    "squeeze",
    "std",
    "subtract",
    "sum",
    "swapaxes",
    "take",
    "tan",
    "tanh",
    "trace",
    "transpose",
    "true_divide",
    "var",
    "where",
    "zeros",
    "zeros_like",
]

_T = TypeVar("_T")
_Tss = ParamSpec("_Tss")
_ArrayT = TypeVar("_ArrayT", bound=np.ndarray[Any, Any])
_ArrayT_co = TypeVar("_ArrayT_co", bound=np.ndarray[Any, Any], covariant=True)
_MArrayT = TypeVar("_MArrayT", bound=MaskedArray[Any, Any])
# the additional `Callable[...]` bound simplifies self-binding to the ufunc's callable signature
_UFuncT_co = TypeVar("_UFuncT_co", bound=np.ufunc | Callable[..., object], default=np.ufunc, covariant=True)

_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_SelfScalarT = TypeVar("_SelfScalarT", bound=np.generic)
_RealScalarT = TypeVar("_RealScalarT", bound=_nt.co_float | np.object_)
_RealNumberT = TypeVar("_RealNumberT", bound=np.integer | np.floating)
_InexactT = TypeVar("_InexactT", bound=np.inexact)
_NumberT = TypeVar("_NumberT", bound=np.number)
_NumericT = TypeVar("_NumericT", bound=np.number | np.timedelta64)
_CoNumberT = TypeVar("_CoNumberT", bound=_nt.co_complex)

_AnyNumberItemT = TypeVar("_AnyNumberItemT", int, float, complex)

_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype, default=np.dtype, covariant=True)
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
# TODO: use `Shape` instead of `AnyShape` once python/mypy#19110 is fixed
_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.AnyShape, default=_nt.Shape, covariant=True)

_Ignored: TypeAlias = object

_ToInt: TypeAlias = int | _nt.co_integer
_ToTD64: TypeAlias = int | _nt.co_timedelta
_ToFloat: TypeAlias = float | _nt.co_float

_ToMask: TypeAlias = _nt.ToBool_nd

_ArangeScalar: TypeAlias = np.integer | np.floating | np.datetime64 | np.timedelta64
_ArangeScalarT = TypeVar("_ArangeScalarT", bound=_ArangeScalar)

_ShapeLike1D: TypeAlias = CanIndex | tuple[CanIndex]
_ShapeLike2D: TypeAlias = tuple[CanIndex, CanIndex]
_ShapeLike3D: TypeAlias = tuple[CanIndex, CanIndex, CanIndex]

_FillValueCallable: TypeAlias = Callable[[np.dtype | ArrayLike], complex | None]
_DomainCallable: TypeAlias = Callable[..., _nt.Array[np.bool]]

_ConvertibleToComplex: TypeAlias = SupportsComplex | ConvertibleToFloat
_ConvertibleToTD64: TypeAlias = dt.timedelta | np.timedelta64 | int | _nt.co_complex | str | bytes | np.character
_ConvertibleToDT64: TypeAlias = dt.date | np.datetime64 | int | _nt.co_complex | str | bytes | np.character

_Device: TypeAlias = L["cpu"]

@type_check_only
class _UFuncKwargs(TypedDict, total=False):
    where: _nt.ToBool_nd | None
    order: _OrderKACF
    subok: bool
    signature: str | tuple[str | None, ...]
    casting: np._CastingKind

@type_check_only
class _CanArray(Protocol[_ArrayT_co]):
    def __array__(self, /) -> _ArrayT_co: ...

###

MaskType: Final[type[np.bool_]] = ...
nomask: np.bool_[L[False]] = ...
masked_print_option: Final[_MaskedPrintOption] = ...

###

class MaskedArrayFutureWarning(FutureWarning): ...
class MAError(Exception): ...
class MaskError(MAError): ...

###

@type_check_only
class _DomainBase:
    @overload
    def __call__(self, /, x: _nt.ToGeneric_0d) -> np.bool_: ...
    @overload
    def __call__(self, /, x: _nt.ToGeneric_1nd) -> _nt.Array[np.bool_]: ...

class _DomainCheckInterval(_DomainBase):
    a: Final[float]
    b: Final[float]
    def __init__(self, /, a: float, b: float) -> None: ...

class _DomainTan(_DomainBase):
    eps: Final[float]
    def __init__(self, /, eps: float) -> None: ...

class _DomainGreater(_DomainBase):
    critical_value: Final[float]
    def __init__(self, /, critical_value: float) -> None: ...

class _DomainGreaterEqual(_DomainBase):
    critical_value: Final[float]
    def __init__(self, /, critical_value: float) -> None: ...

class _DomainSafeDivide:
    tolerance: float
    def __init__(self, /, tolerance: float | None = None) -> None: ...
    def __call__(self, /, a: _nt.ToGeneric_nd, b: _nt.ToGeneric_nd) -> _nt.Array[Incomplete]: ...

###

# not generic at runtime
class _MaskedUFunc(Generic[_UFuncT_co]):
    f: _UFuncT_co  # readonly
    def __init__(self, /, ufunc: _UFuncT_co) -> None: ...

# not generic at runtime
class _MaskedUnaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    fill: Final[complex | None]
    domain: Final[_DomainCallable | None]

    def __init__(
        self, /, mufunc: _UFuncT_co, fill: complex | None = 0, domain: _DomainCallable | None = None
    ) -> None: ...

    # NOTE: This might not work with overloaded callable signatures might not work on
    # pyright, which is a long-standing issue, and is unique to pyright:
    # https://github.com/microsoft/pyright/issues/9663
    # https://github.com/microsoft/pyright/issues/10849
    # https://github.com/microsoft/pyright/issues/10899
    # https://github.com/microsoft/pyright/issues/11049
    def __call__(
        self: _MaskedUnaryOperation[Callable[Concatenate[Any, _Tss], _T]],
        /,
        a: ArrayLike,
        *args: _Tss.args,
        **kwargs: _Tss.kwargs,
    ) -> _T: ...

# not generic at runtime
class _MaskedBinaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    fillx: Final[complex | None]
    filly: Final[complex | None]

    def __init__(self, /, mbfunc: _UFuncT_co, fillx: complex | None = 0, filly: complex | None = 0) -> None: ...

    # NOTE: See the comment in `_MaskedUnaryOperation.__call__`
    def __call__(
        self: _MaskedBinaryOperation[Callable[Concatenate[Any, Any, _Tss], _T]],
        /,
        a: ArrayLike,
        b: ArrayLike,
        *args: _Tss.args,
        **kwargs: _Tss.kwargs,
    ) -> _T: ...

    # NOTE: We cannot meaningfully annotate the return (d)types of these methods until
    # the signatures of the corresponding `numpy.ufunc` methods are specified.
    def reduce(self, /, target: ArrayLike, axis: CanIndex = 0, dtype: DTypeLike | None = None) -> Incomplete: ...
    def outer(self, /, a: ArrayLike, b: ArrayLike) -> _nt.MArray[Incomplete]: ...
    def accumulate(self, /, target: ArrayLike, axis: CanIndex = 0) -> _nt.MArray[Incomplete]: ...

# not generic at runtime
class _DomainedBinaryOperation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    domain: Final[_DomainCallable]
    fillx: Final[complex | None]
    filly: Final[complex | None]

    def __init__(
        self, /, dbfunc: _UFuncT_co, domain: _DomainCallable, fillx: complex | None = 0, filly: complex | None = 0
    ) -> None: ...

    # NOTE: See the comment in `_MaskedUnaryOperation.__call__`
    def __call__(
        self: _DomainedBinaryOperation[Callable[Concatenate[Any, Any, _Tss], _T]],
        /,
        a: ArrayLike,
        b: ArrayLike,
        *args: _Tss.args,
        **kwargs: _Tss.kwargs,
    ) -> _T: ...

# not generic at runtime
class _extrema_operation(_MaskedUFunc[_UFuncT_co], Generic[_UFuncT_co]):
    compare: Final[_MaskedBinaryOperation]
    fill_value_func: Final[_FillValueCallable]

    def __init__(
        self, /, ufunc: _UFuncT_co, compare: _MaskedBinaryOperation, fill_value: _FillValueCallable
    ) -> None: ...

    # NOTE: This class is only used internally for `maximum` and `minimum`, so we are
    # able to annotate the `__call__` method specifically for those two functions.
    @overload
    def __call__(self, /, a: _ArrayLike[_ScalarT], b: _ArrayLike[_ScalarT]) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __call__(self, /, a: ArrayLike, b: ArrayLike) -> _nt.MArray[Incomplete]: ...

    # NOTE: We cannot meaningfully annotate the return (d)types of these methods until
    # the signatures of the corresponding `numpy.ufunc` methods are specified.
    def reduce(self, /, target: ArrayLike, axis: CanIndex | _NoValueType = ...) -> Incomplete: ...
    def outer(self, /, a: ArrayLike, b: ArrayLike) -> _nt.MArray[Incomplete]: ...

###

@final
class _MaskedPrintOption:
    _display: str
    _enabled: bool | L[0, 1]
    def __init__(self, /, display: str) -> None: ...
    def display(self, /) -> str: ...
    def set_display(self, /, s: str) -> None: ...
    def enabled(self, /) -> bool: ...
    def enable(self, /, shrink: bool | L[0, 1] = 1) -> None: ...

# TODO: Support non-boolean mask dtypes, such as `np.void`. This will require adding an
# additional generic type parameter to (at least) `MaskedArray` and `MaskedIterator` to
# hold the np.dtype of the mask.

class MaskedIterator(Generic[_ShapeT_co, _DTypeT_co]):
    ma: MaskedArray[_ShapeT_co, _DTypeT_co]  # readonly
    dataiter: np.flatiter[np.ndarray[_ShapeT_co, _DTypeT_co]]  # readonly
    maskiter: Final[np.flatiter[_nt.Array[np.bool]]]

    def __init__(self, ma: MaskedArray[_ShapeT_co, _DTypeT_co]) -> None: ...
    def __iter__(self) -> Self: ...

    # Similar to `MaskedArray.__getitem__` but without the `void` case.
    @overload
    def __getitem__(
        self, indx: _nt.Array[np.integer | np.bool] | tuple[_nt.Array[np.integer | np.bool], ...], /
    ) -> MaskedArray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self, indx: CanIndex | tuple[CanIndex, ...], /) -> Incomplete: ...
    @overload
    def __getitem__(self, indx: _ToIndices, /) -> MaskedArray[_nt.AnyShape, _DTypeT_co]: ...

    # Similar to `ndarray.__setitem__` but without the `void` case.
    @overload  # flexible | object_ | bool
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.flexible | np.object_ | np.bool] | np.dtypes.StringDType],
        index: _ToIndices,
        value: object,
        /,
    ) -> None: ...
    @overload  # integer
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.integer]],
        index: _ToIndices,
        value: ConvertibleToInt | _nt.Sequence1ND[ConvertibleToInt] | _nt.CoInteger_nd,
        /,
    ) -> None: ...
    @overload  # floating
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.floating]],
        index: _ToIndices,
        value: ConvertibleToFloat | _nt.Sequence1ND[ConvertibleToFloat | None] | _nt.CoFloating_nd | None,
        /,
    ) -> None: ...
    @overload  # complexfloating
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.complexfloating]],
        index: _ToIndices,
        value: _ConvertibleToComplex | _nt.Sequence1ND[_ConvertibleToComplex | None] | _nt.CoComplex_nd | None,
        /,
    ) -> None: ...
    @overload  # timedelta64
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.timedelta64]],
        index: _ToIndices,
        value: _ConvertibleToTD64 | _nt.Sequence1ND[_ConvertibleToTD64 | None] | None,
        /,
    ) -> None: ...
    @overload  # datetime64
    def __setitem__(
        self: MaskedIterator[Any, np.dtype[np.datetime64]],
        index: _ToIndices,
        value: _ConvertibleToDT64 | _nt.Sequence1ND[_ConvertibleToDT64 | None] | None,
        /,
    ) -> None: ...
    @overload  # catch-all
    def __setitem__(self, index: _ToIndices, value: ArrayLike, /) -> None: ...

    # TODO: Returns `mvoid[(), _DTypeT_co]` for masks with `np.void` np.dtype.
    def __next__(self: MaskedIterator[Any, np.dtype[_ScalarT]]) -> _ScalarT: ...

class MaskedArray(np.ndarray[_ShapeT_co, _DTypeT_co]):
    __array_priority__: ClassVar[float] = 15  # pyright: ignore[reportIncompatibleMethodOverride]

    @overload
    def __new__(
        cls,
        data: _ArrayLike[_ScalarT],
        mask: _ToMask = ...,
        dtype: None = None,
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object,
        mask: _ToMask,
        dtype: _DTypeLike[_ScalarT],
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object,
        mask: _ToMask = ...,
        *,
        dtype: _DTypeLike[_ScalarT],
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __new__(
        cls,
        data: object = None,
        mask: _ToMask = ...,
        dtype: DTypeLike | None = None,
        copy: bool = False,
        subok: bool = True,
        ndmin: int = 0,
        fill_value: _ScalarLike_co | None = None,
        keep_mask: bool = True,
        hard_mask: bool | None = None,
        shrink: bool = True,
        order: _OrderKACF | None = None,
    ) -> _nt.MArray[Any]: ...

    #
    @override
    def __array_wrap__(
        self,
        obj: np.ndarray[_ShapeT, _DTypeT],
        context: tuple[np.ufunc, tuple[Any, ...], int] | None = None,
        return_scalar: bool = False,
    ) -> MaskedArray[_ShapeT, _DTypeT]: ...

    #
    @override  # type: ignore[override]
    @overload  # ()
    def view(self, /, dtype: None = None, type: None = None, fill_value: _ScalarLike_co | None = None) -> Self: ...
    @overload  # (dtype: DTypeT)
    def view(
        self, /, dtype: _DTypeT | _HasDType[_DTypeT], type: None = None, fill_value: _ScalarLike_co | None = None
    ) -> MaskedArray[_ShapeT_co, _DTypeT]: ...
    @overload  # (dtype: dtype[ScalarT])
    def view(
        self, /, dtype: _DTypeLike[_ScalarT], type: None = None, fill_value: _ScalarLike_co | None = None
    ) -> MaskedArray[_ShapeT_co, np.dtype[_ScalarT]]: ...
    @overload  # ([dtype: _, ]*, type: ArrayT)
    def view(
        self, /, dtype: DTypeLike | None = None, *, type: type[_ArrayT], fill_value: _ScalarLike_co | None = None
    ) -> _ArrayT: ...
    @overload  # (dtype: _, type: ArrayT)
    def view(
        self, /, dtype: DTypeLike | None, type: type[_ArrayT], fill_value: _ScalarLike_co | None = None
    ) -> _ArrayT: ...
    @overload  # (dtype: ArrayT, /)
    def view(self, /, dtype: type[_ArrayT], type: None = None, fill_value: _ScalarLike_co | None = None) -> _ArrayT: ...
    @overload  # (dtype: ?)
    def view(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        # `_VoidDTypeLike | str | None` is like `DTypeLike` but without `_DTypeLike[Any]` to avoid
        # overlaps with previous overloads.
        dtype: _VoidDTypeLike | str | None,
        type: None = None,
        fill_value: _ScalarLike_co | None = None,
    ) -> MaskedArray[_ShapeT_co, np.dtype]: ...

    # Keep in sync with `ndarray.__getitem__`
    @override
    @overload
    def __getitem__(
        self, key: _nt.Array[_nt.co_integer] | tuple[_nt.Array[_nt.co_integer], ...], /
    ) -> MaskedArray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self, key: CanIndex | tuple[CanIndex, ...], /) -> Any: ...
    @overload
    def __getitem__(self, key: _ToIndices, /) -> MaskedArray[_nt.AnyShape, _DTypeT_co]: ...
    @overload
    def __getitem__(self: _nt.MArray[np.void], indx: str, /) -> MaskedArray[_ShapeT_co]: ...
    @overload
    def __getitem__(self: _nt.MArray[np.void], indx: list[str], /) -> MaskedArray[_ShapeT_co, np.dtype[np.void]]: ...

    #
    def __setmask__(self, mask: _ToMask, copy: bool = False) -> None: ...
    @property
    def mask(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool_]] | np.bool_: ...
    @mask.setter
    def mask(self, value: _ToMask, /) -> None: ...
    @property
    def recordmask(self) -> np.ndarray[_ShapeT_co, np.dtype[np.bool_]] | np.bool_: ...
    @recordmask.setter
    def recordmask(self, mask: Never, /) -> Never: ...
    def harden_mask(self) -> Self: ...
    def soften_mask(self) -> Self: ...
    @property
    def hardmask(self) -> bool: ...
    def unshare_mask(self) -> Self: ...
    @property
    def sharedmask(self) -> bool: ...
    def shrink_mask(self) -> Self: ...

    #
    @property
    def baseclass(self) -> type[np.ndarray]: ...

    #
    @property
    def _data(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...
    @property
    @override
    def data(self) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    # the `explicit-override` error is an obvious false positive from mypy
    @property  # type: ignore[explicit-override, override]
    @override
    def flat(self) -> MaskedIterator[_ShapeT_co, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @flat.setter
    def flat(self, value: ArrayLike, /) -> None: ...

    #
    @property
    def fill_value(self: _nt.MArray[_ScalarT]) -> _ScalarT: ...
    @fill_value.setter
    def fill_value(self, value: _ScalarLike_co | None = None, /) -> None: ...
    def get_fill_value(self: _nt.MArray[_ScalarT]) -> _ScalarT: ...
    def set_fill_value(self, /, value: _ScalarLike_co | None = None) -> None: ...

    #
    def filled(self, /, fill_value: _ScalarLike_co | None = None) -> np.ndarray[_ShapeT_co, _DTypeT_co]: ...

    #
    def compressed(self) -> np.ndarray[_nt.Rank1, _DTypeT_co]: ...

    # keep roughly in sync with `ma.core.compress`, but swap the first two arguments
    @override  # type: ignore[override]
    @overload
    def compress(self, condition: _nt.ToBool_nd, axis: _ShapeLike | None, out: _ArrayT) -> _ArrayT: ...
    @overload
    def compress(self, condition: _nt.ToBool_nd, axis: _ShapeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...
    @overload
    def compress(
        self, condition: _nt.ToBool_nd, axis: None = None, out: None = None
    ) -> MaskedArray[_nt.Rank1, _DTypeT_co]: ...
    @overload
    def compress(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, condition: _nt.ToBool_nd, axis: _ShapeLike | None = None, out: None = None
    ) -> MaskedArray[_nt.AnyShape, _DTypeT_co]: ...

    # TODO: How to deal with the non-commutative nature of `==` and `!=`?
    # xref numpy/numpy#17368
    @override
    def __eq__(self, other: Incomplete, /) -> Incomplete: ...
    @override
    def __ne__(self, other: Incomplete, /) -> Incomplete: ...

    #
    @override
    def __ge__(self, other: ArrayLike, /) -> _nt.MArray[np.bool_]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __gt__(self, other: ArrayLike, /) -> _nt.MArray[np.bool_]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __le__(self, other: ArrayLike, /) -> _nt.MArray[np.bool_]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __lt__(self, other: ArrayLike, /) -> _nt.MArray[np.bool_]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __add__(self: _nt.MArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(
        self: _nt.MArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __add__(self: _nt.MArray[np.datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.MArray[np.datetime64]: ...
    @overload
    def __add__(self: _nt.MArray[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.MArray[np.datetime64]: ...  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __add__(self: _nt.MArray[np.object_, Any], x: object, /) -> _nt.MArray[np.object_]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __add__(  # pyright: ignore[reportOverlappingOverload]
        self: _nt.MArray[np.str_], x: _nt.ToString_nd[_T], /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType]: ...
    @overload
    def __add__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __add__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRAdd[_AnyItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __radd__(self: _nt.MArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(
        self: _nt.MArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __radd__(self: _nt.MArray[np.datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.MArray[np.datetime64]: ...
    @overload
    def __radd__(self: _nt.MArray[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.MArray[np.datetime64]: ...  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __radd__(self: _nt.MArray[np.object_, Any], x: object, /) -> _nt.MArray[np.object_]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __radd__(  # pyright: ignore[reportOverlappingOverload]
        self: _nt.MArray[np.str_], x: _nt.ToString_nd[_T], /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __radd__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __radd__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanAdd[_AnyItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override  # type: ignore[misc, override]
    @overload
    def __iadd__(self: _nt.MArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.MArray[np.bool_], x: _nt.SequenceND[bool], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.MArray[np.number], x: _nt.SequenceND[int], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.MArray[np.inexact], x: _nt.SequenceND[float], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: _nt.MArray[np.complexfloating], x: _nt.SequenceND[complex], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.MArray[np.datetime64], x: _nt.CoTimeDelta_nd, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToString_nd[_T] | _nt.ToStr_nd, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __iadd__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRAdd[_AnyItemT, _AnyItemT]], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    #
    @override
    @overload
    def __sub__(self: _nt.MArray[_NumericT], x: _nt.Casts[_NumericT], /) -> _nt.MArray[_NumericT]: ...
    @overload
    def __sub__(self: _nt.MArray[_CoNumberT], x: _nt.CastsWith[_CoNumberT, _ScalarT], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithBuiltin[_T, _NumericT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_NumericT]: ...
    @overload
    def __sub__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __sub__(self: _nt.MArray[np.datetime64], x: _nt.ToDateTime_nd, /) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __sub__(self: _nt.MArray[np.datetime64], x: _nt.CoTimeDelta_nd, /) -> _nt.MArray[np.datetime64]: ...
    @overload
    def __sub__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...
    @overload
    def __sub__(  # pyright: ignore[reportIncompatibleMethodOverride, reportOverlappingOverload]
        self: _nt.MArray[np.number[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanRSub[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override
    @overload
    def __rsub__(self: _nt.MArray[_NumericT], x: _nt.Casts[_NumericT], /) -> _nt.MArray[_NumericT]: ...
    @overload
    def __rsub__(self: _nt.MArray[_CoNumberT], x: _nt.CastsWith[_CoNumberT, _ScalarT], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithBuiltin[_T, _NumericT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_NumericT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithInt[_ScalarT], x: _PyIntND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rsub__(self: _nt.MArray[np.datetime64], x: _nt.ToDateTime_nd, /) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __rsub__(self: _nt.MArray[_nt.co_timedelta], x: _nt.ToDateTime_nd, /) -> _nt.MArray[np.datetime64]: ...
    @overload
    def __rsub__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...
    @overload
    def __rsub__(  # pyright: ignore[reportIncompatibleMethodOverride, reportOverlappingOverload]
        self: _nt.MArray[np.number[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanSub[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override  # type: ignore[misc, override]
    @overload
    def __isub__(self: _nt.MArray[_ScalarT], x: _nt.Casts[_ScalarT], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.MArray[np.number], x: _nt.SequenceND[int], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.MArray[np.inexact], x: _nt.SequenceND[float], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(
        self: _nt.MArray[np.complexfloating], x: _nt.SequenceND[complex], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.MArray[np.datetime64], x: _nt.CoTimeDelta_nd, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __isub__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.number[_AnyNumberItemT]],
        x: _nt.Sequence1ND[_nt.op.CanRSub[_AnyNumberItemT, _AnyNumberItemT]],
        /,
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __mul__(self: _nt.MArray[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> _nt.MArray[_CoNumberT]: ...
    @overload
    def __mul__(
        self: _nt.MArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithInt[_ScalarT], x: _nt.SequenceND[int], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __mul__(self: _nt.MArray[np.timedelta64], x: _nt.ToFloating_nd, /) -> _nt.MArray[np.timedelta64]: ...  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __mul__(self: _nt.MArray[np.object_, Any], x: object, /) -> _nt.MArray[np.object_]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __mul__(  # pyright: ignore[reportOverlappingOverload]
        self: _nt.MArray[np.integer], x: _nt.ToString_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __mul__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToInteger_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __mul__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMul[_AnyItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override  # type: ignore[override]
    @overload
    def __rmul__(self: _nt.MArray[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> _nt.MArray[_CoNumberT]: ...
    @overload
    def __rmul__(
        self: _nt.MArray[_SelfScalarT], x: _nt.CastsWith[_SelfScalarT, _ScalarT], /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithBuiltin[_T, _ScalarT], x: _nt.SequenceND[_T], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithInt[_ScalarT], x: _nt.SequenceND[int], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rmul__(self: _nt.MArray[np.timedelta64], x: _nt.ToFloating_nd, /) -> _nt.MArray[np.timedelta64]: ...  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rmul__(self: _nt.MArray[np.object_, Any], x: object, /) -> _nt.MArray[np.object_]: ...  # type: ignore[overload-cannot-match]  # pyright: ignore[reportOverlappingOverload]
    @overload
    def __rmul__(  # pyright: ignore[reportOverlappingOverload]
        self: _nt.MArray[np.integer], x: _nt.ToString_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __rmul__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToInteger_nd, /
    ) -> MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]]: ...
    @overload
    def __rmul__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanMul[_AnyItemT]], /
    ) -> _nt.MArray[Incomplete]: ...

    #
    @override  # type: ignore[misc, override]
    @overload
    def __imul__(self: _nt.MArray[_CoNumberT], x: _nt.Casts[_CoNumberT], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.MArray[bool_], x: _nt.SequenceND[bool], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.MArray[np.number], x: _nt.SequenceND[int], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.MArray[np.inexact], x: _nt.SequenceND[float], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: _nt.MArray[np.complexfloating], x: _nt.SequenceND[complex], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.MArray[np.timedelta64], x: _nt.CoFloating_nd, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(
        self: MaskedArray[_nt.AnyShape, np.dtypes.StringDType[_T]], x: _nt.ToInteger_nd, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __imul__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRMul[_AnyItemT, _AnyItemT]], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...

    #
    @override
    @overload
    def __pow__(self: _nt.MArray[_NumberT], x: _nt.Casts[_NumberT], k: None = None, /) -> _nt.MArray[_NumberT]: ...
    @overload
    def __pow__(self: _nt.MArray[bool_], x: _nt.ToBool_nd, k: None = None, /) -> _nt.MArray[np.int8]: ...
    @overload
    def __pow__(
        self: _nt.MArray[_NumberT], x: _nt.CastsWith[_NumberT, _ScalarT], k: None = None, /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __pow__(
        self: _nt.CastsWithInt[_NumberT], x: _nt.SequenceND[int], k: None = None, /
    ) -> _nt.MArray[_NumberT]: ...
    @overload
    def __pow__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, k: None = None, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __pow__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, k: None = None, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __pow__(self: _nt.MArray[np.object_], x: object, k: None = None, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    @overload
    def __rpow__(self: _nt.MArray[_NumberT], x: _nt.Casts[_NumberT], k: None = None, /) -> _nt.MArray[_NumberT]: ...
    @overload
    def __rpow__(self: _nt.MArray[bool_], x: _nt.ToBool_nd, k: None = None, /) -> _nt.MArray[np.int8]: ...
    @overload
    def __rpow__(
        self: _nt.MArray[_NumberT], x: _nt.CastsWith[_NumberT, _ScalarT], k: None = None, /
    ) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rpow__(
        self: _nt.CastsWithInt[_NumberT], x: _nt.SequenceND[int], k: None = None, /
    ) -> _nt.MArray[_NumberT]: ...
    @overload
    def __rpow__(self: _nt.CastsWithFloat[_ScalarT], x: _PyFloatND, k: None = None, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rpow__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, k: None = None, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rpow__(self: _nt.MArray[np.object_], x: object, k: None = None, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[misc, override]
    @overload
    def __ipow__(self: _nt.MArray[_NumberT], x: _nt.Casts[_NumberT], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.MArray[np.number], x: _nt.SequenceND[int], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.MArray[np.inexact], x: _nt.SequenceND[float], /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(
        self: _nt.MArray[np.complexfloating], x: _nt.SequenceND[complex], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ipow__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    @overload
    def __truediv__(
        self: np._HasDType[_HasType[_nt.Just[np.number]]],
        x: _nt.CoFloat64_nd | np._HasDType[_HasType[_nt.Just[np.number]]],
        /,
    ) -> _nt.MArray[np.inexact]: ...
    @overload
    def __truediv__(self: _nt.MArray[_InexactT], x: _nt.Casts[_InexactT], /) -> _nt.MArray[_InexactT]: ...
    @overload
    def __truediv__(self: _nt.MArray[_ScalarT], x: _nt.CastsWith[_ScalarT, _InexactT], /) -> _nt.MArray[_InexactT]: ...  # type: ignore[overload-overlap]
    @overload
    def __truediv__(self: _nt.CastsWithFloat[_ScalarT], x: _nt.SequenceND[float], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __truediv__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __truediv__(self: _nt.MArray[_nt.co_integer], x: _nt.CoInteger_nd, /) -> _nt.MArray[np.float64]: ...
    @overload
    def __truediv__(self: _nt.MArray[np.timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.MArray[np.float64]: ...
    @overload
    def __truediv__(
        self: _nt.MArray[np.timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __truediv__(
        self: _nt.MArray[np.generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanRTruediv[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...
    @overload
    def __truediv__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    @overload
    def __rtruediv__(
        self: np._HasDType[_HasType[_nt.Just[np.number]]],
        x: _nt.CoFloat64_nd | np._HasDType[_HasType[_nt.Just[np.number]]],
        /,
    ) -> _nt.MArray[np.inexact]: ...
    @overload
    def __rtruediv__(self: _nt.MArray[_InexactT], x: _nt.Casts[_InexactT], /) -> _nt.MArray[_InexactT]: ...
    @overload
    def __rtruediv__(self: _nt.MArray[_ScalarT], x: _nt.CastsWith[_ScalarT, _InexactT], /) -> _nt.MArray[_InexactT]: ...  # type: ignore[overload-overlap]
    @overload
    def __rtruediv__(self: _nt.CastsWithFloat[_ScalarT], x: _nt.SequenceND[float], /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rtruediv__(self: _nt.CastsWithComplex[_ScalarT], x: _PyComplexND, /) -> _nt.MArray[_ScalarT]: ...
    @overload
    def __rtruediv__(self: _nt.MArray[_nt.co_integer], x: _nt.CoInteger_nd, /) -> _nt.MArray[np.float64]: ...
    @overload
    def __rtruediv__(self: _nt.MArray[np.timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.MArray[np.float64]: ...
    @overload
    def __rtruediv__(
        self: _nt.MArray[np.integer | np.floating], x: _nt.ToTimeDelta_nd, /
    ) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __rtruediv__(
        self: _nt.MArray[np.generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanTruediv[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...
    @overload
    def __rtruediv__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[misc, override]
    @overload
    def __itruediv__(
        self: _nt.MArray[_InexactT], x: _nt.Casts[_InexactT], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.MArray[np.inexact], x: _nt.SequenceND[float], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.MArray[np.complexfloating], x: _nt.SequenceND[complex], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.MArray[np.timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(
        self: _nt.MArray[np.generic[_AnyNumberItemT]],
        x: _nt.Sequence1ND[_nt.op.CanRTruediv[_AnyNumberItemT, _AnyNumberItemT]],
        /,
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __itruediv__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    @overload
    def __floordiv__(self: _nt.MArray[bool_], x: _nt.ToBool_nd, /) -> _nt.MArray[np.int8]: ...
    @overload
    def __floordiv__(
        self: _nt.MArray[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.MArray[_RealNumberT]: ...
    @overload
    def __floordiv__(
        self: _nt.MArray[_RealNumberT], x: _nt.CastsWith[_RealNumberT, _RealScalarT], /
    ) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.CastsWithInt[_RealScalarT], x: _PyIntND, /) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __floordiv__(self: _nt.MArray[np.timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.MArray[np.int64]: ...
    @overload
    def __floordiv__(
        self: _nt.MArray[np.timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __floordiv__(
        self: _nt.MArray[np.generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanRFloordiv[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...
    @overload
    def __floordiv__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[override]
    @overload
    def __rfloordiv__(self: _nt.MArray[bool_], x: _nt.ToBool_nd, /) -> _nt.MArray[np.int8]: ...
    @overload
    def __rfloordiv__(
        self: _nt.MArray[_RealNumberT], x: _nt.Casts[_RealNumberT] | _nt.ToBool_nd, /
    ) -> _nt.MArray[_RealNumberT]: ...
    @overload
    def __rfloordiv__(
        self: _nt.MArray[_RealNumberT], x: _nt.CastsWith[_RealNumberT, _RealScalarT], /
    ) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.CastsWithInt[_RealScalarT], x: _nt.SequenceND[int], /) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.CastsWithFloat[_RealScalarT], x: _PyFloatND, /) -> _nt.MArray[_RealScalarT]: ...
    @overload
    def __rfloordiv__(self: _nt.MArray[np.timedelta64], x: _nt.ToTimeDelta_nd, /) -> _nt.MArray[np.int64]: ...
    @overload
    def __rfloordiv__(
        self: _nt.MArray[np.integer | np.floating], x: _nt.ToTimeDelta_nd, /
    ) -> _nt.MArray[np.timedelta64]: ...
    @overload
    def __rfloordiv__(
        self: _nt.MArray[np.generic[_AnyNumberItemT]], x: _nt.Sequence1ND[_nt.op.CanFloordiv[_AnyNumberItemT]], /
    ) -> _nt.MArray[Incomplete]: ...
    @overload
    def __rfloordiv__(self: _nt.MArray[np.object_], x: object, /) -> _nt.MArray[np.object_]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override  # type: ignore[misc, override]
    @overload
    def __ifloordiv__(
        self: _nt.MArray[_RealNumberT], x: _nt.Casts[_RealNumberT], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.MArray[np.integer], x: _nt.SequenceND[int], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.MArray[np.floating], x: _nt.SequenceND[float], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.MArray[np.timedelta64], x: _nt.ToInteger_nd | _nt.ToFloating_nd, /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(
        self: _nt.MArray[np.generic[_AnyItemT]], x: _nt.Sequence1ND[_nt.op.CanRFloordiv[_AnyItemT, _AnyItemT]], /
    ) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...
    @overload
    def __ifloordiv__(self: _nt.MArray[np.object_], x: object, /) -> MaskedArray[_ShapeT_co, _DTypeT_co]: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @property  # type: ignore[explicit-override]
    @override
    def real(self: np._HasDTypeWithReal[_ScalarT], /) -> _nt.MArray[_ScalarT, _ShapeT_co]: ...
    @real.setter
    def real(self, value: ArrayLike, /) -> None: ...

    #
    @property  # type: ignore[explicit-override]
    @override
    def imag(self: np._HasDTypeWithImag[_ScalarT], /) -> _nt.MArray[_ScalarT, _ShapeT_co]: ...
    @imag.setter
    def imag(self, value: ArrayLike, /) -> None: ...

    # keep in sync with `np.ma.count`
    @overload
    def count(self, axis: None = None, keepdims: L[False] | _NoValueType = ...) -> int: ...
    @overload
    def count(self, axis: _ShapeLike, keepdims: bool | _NoValueType = ...) -> _nt.MArray[np.int_]: ...
    @overload
    def count(self, axis: _ShapeLike | None = None, *, keepdims: L[True]) -> _nt.MArray[np.int_]: ...
    @overload
    def count(self, axis: _ShapeLike | None, keepdims: L[True]) -> _nt.MArray[np.int_]: ...

    # Keep in sync with `ndarray.reshape`
    @override
    @overload  # (None)
    def reshape(self, shape: None, /, *, order: np._OrderACF = "C", copy: bool | None = None) -> Self: ...
    @overload  # (empty_sequence)
    def reshape(  # type: ignore[overload-overlap]  # mypy false positive
        self, shape: Sequence[Never] | _nt.Shape0, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank0, _DTypeT_co]: ...
    @overload  # (index)
    def reshape(
        self, size1: CanIndex | _nt.Shape1, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank1, _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self, size1: _nt.Shape2, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (index, index)
    def reshape(
        self, size1: CanIndex, size2: CanIndex, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank2, _DTypeT_co]: ...
    @overload  # (index, index, index)
    def reshape(
        self, size1: _nt.Shape3, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank3, _DTypeT_co]: ...
    @overload  # (index, index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        /,
        *,
        order: np._OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[_nt.Rank3, _DTypeT_co]: ...
    @overload  # (index, index, index, index)
    def reshape(
        self, size1: _nt.Shape4, /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[_nt.Rank4, _DTypeT_co]: ...
    @overload  # (index, index, index, index)
    def reshape(
        self,
        size1: CanIndex,
        size2: CanIndex,
        size3: CanIndex,
        size4: CanIndex,
        /,
        *,
        order: np._OrderACF = "C",
        copy: bool | None = None,
    ) -> MaskedArray[_nt.Rank4, _DTypeT_co]: ...
    @overload  # (int, *(index, ...))
    def reshape(
        self, size0: CanIndex, /, *shape: CanIndex, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[Incomplete, _DTypeT_co]: ...
    @overload  # (sequence[index])
    def reshape(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, shape: Sequence[CanIndex], /, *, order: np._OrderACF = "C", copy: bool | None = None
    ) -> MaskedArray[Incomplete, _DTypeT_co]: ...

    #
    @override
    def resize(self, newshape: Never, refcheck: bool = True, order: bool = False) -> Never: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def put(self, indices: _nt.CoInteger_nd, values: ArrayLike, mode: np._ModeKind = "raise") -> None: ...

    #
    def ids(self) -> tuple[int, int]: ...
    def iscontiguous(self) -> bool: ...

    # Keep in sync with `ma.core.all`
    @override  # type: ignore[override]
    @overload
    def all(self, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> bool_: ...
    @overload
    def all(self, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]) -> _nt.MArray[bool_]: ...
    @overload
    def all(self, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[bool_]: ...
    @overload
    def all(
        self, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
    ) -> bool_ | _nt.MArray[bool_]: ...
    @overload
    def all(self, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
    @overload
    def all(self, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # Keep in sync with `ma.core.any`
    @override  # type: ignore[override]
    @overload
    def any(self, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> bool_: ...
    @overload
    def any(self, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]) -> _nt.MArray[bool_]: ...
    @overload
    def any(self, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[bool_]: ...
    @overload
    def any(
        self, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
    ) -> bool_ | _nt.MArray[bool_]: ...
    @overload
    def any(self, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
    @overload
    def any(self, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    # Keep in sync with `ndarray.trace` and `ma.core.trace`
    @override  # type: ignore[override]
    @overload
    def trace(
        self,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: DTypeLike | None = None,
        out: None = None,
    ) -> Any: ...
    @overload
    def trace(
        self,
        offset: CanIndex = 0,
        axis1: CanIndex = 0,
        axis2: CanIndex = 1,
        dtype: DTypeLike | None = None,
        *,
        out: _ArrayT,
    ) -> _ArrayT: ...
    @overload
    def trace(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, offset: CanIndex, axis1: CanIndex, axis2: CanIndex, dtype: DTypeLike | None, out: _ArrayT
    ) -> _ArrayT: ...

    # This differs from `ndarray.dot`, in that 1D dot 1D returns a 0D array.
    @override  # typoe: ignore[override]
    @overload
    def dot(self, b: ArrayLike, out: None = None, strict: bool = False) -> _nt.MArray[Any]: ...
    @overload
    def dot(self, b: ArrayLike, out: _ArrayT, strict: bool = False) -> _ArrayT: ...

    #
    @property
    @override
    def mT(self) -> Self: ...
    @property
    @override
    def T(self) -> Self: ...

    #
    @override
    def __array_finalize__(self, /, obj: Incomplete) -> None: ...

    #
    @override
    def __reduce__(self) -> Incomplete: ...
    @override
    def __deepcopy__(self, /, memo: Incomplete = ...) -> Self: ...

    #
    @override
    def ravel(self, order: Incomplete = ...) -> Incomplete: ...

    #
    @override
    def sum(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def cumsum(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def prod(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    product = prod
    @override
    def cumprod(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def mean(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., dtype: Incomplete = ..., out: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    def anom(self, axis: Incomplete = ..., dtype: Incomplete = ...) -> Incomplete: ...
    @override
    def var(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: float = 0,
        keepdims: Incomplete = ...,
        mean: Incomplete = ...,
    ) -> Incomplete: ...
    @override
    def std(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        dtype: Incomplete = ...,
        out: Incomplete = ...,
        ddof: float = 0,
        keepdims: Incomplete = ...,
        mean: Incomplete = ...,
    ) -> Incomplete: ...

    #
    @override
    def round(self, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def sort(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = -1,
        kind: Incomplete | None = None,
        order: Incomplete | None = None,
        endwith: bool = True,
        fill_value: Incomplete | None = None,
        *,
        stable: bool = False,
    ) -> Incomplete: ...
    @override
    def argsort(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        axis: Incomplete = ...,
        kind: Incomplete | None = None,
        order: Incomplete | None = None,
        endwith: bool = True,
        fill_value: Incomplete | None = None,
        *,
        stable: bool = False,
    ) -> Incomplete: ...

    #
    @override
    def min(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def argmin(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., fill_value: Incomplete = ..., out: Incomplete = ..., *, keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def max(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...
    @override
    def argmax(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self, axis: Incomplete = ..., fill_value: Incomplete = ..., out: Incomplete = ..., *, keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def ptp(  # pyright: ignore[reportIncompatibleVariableOverride]
        self, axis: Incomplete = ..., out: Incomplete = ..., fill_value: Incomplete = ..., keepdims: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def partition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...
    @override
    def argpartition(self, *args: Incomplete, **kwargs: Incomplete) -> Incomplete: ...

    #
    @override
    def take(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, /, indices: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., mode: Incomplete = ...
    ) -> Incomplete: ...

    #
    @override
    def copy(self, /, order: _OrderKACF = "C") -> Self: ...

    #
    diagonal: Incomplete
    flatten: Incomplete
    repeat: Incomplete
    squeeze: Incomplete
    swapaxes: Incomplete
    transpose: Incomplete

    #
    def toflex(self) -> Incomplete: ...
    def torecords(self) -> Incomplete: ...
    @override
    def tolist(self, fill_value: Incomplete | None = None) -> Incomplete: ...
    @override
    def tobytes(self, /, fill_value: Incomplete | None = None, order: _OrderKACF = "C") -> bytes: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def tofile(self, /, fid: Incomplete, sep: str = "", format: str = "%s") -> Incomplete: ...

class mvoid(MaskedArray[_ShapeT_co, _DTypeT_co]):
    def __new__(
        self,  # noqa: PLW0211
        data: ArrayLike,
        mask: _ToMask = ...,
        dtype: DTypeLike | None = None,
        fill_value: complex | None = None,
        hardmask: bool = False,
        copy: bool = False,
        subok: bool = True,
    ) -> Self: ...

    #
    @override
    def __getitem__(self, indx: _ToIndices, /) -> Incomplete: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __setitem__(self, indx: _ToIndices, value: ArrayLike, /) -> None: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

    #
    @override
    def __iter__(self: mvoid[Any, np.dtype[_ScalarT]], /) -> Iterator[MaskedConstant | _ScalarT]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __len__(self, /) -> int: ...

    #
    @override
    def filled(self, /, fill_value: _ScalarLike_co | None = None) -> Self | np.void: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override  # list or tuple
    def tolist(self) -> Sequence[Incomplete]: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]

# 0D float64 array
class MaskedConstant(MaskedArray[tuple[()], np.dtype[np.float64]]):
    def __new__(cls) -> Self: ...

    # these overrides are no-ops
    @override
    def __iadd__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __isub__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __imul__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __ifloordiv__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __itruediv__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __ipow__(self, other: _Ignored, /) -> Self: ...  # type: ignore[override]
    @override
    def __deepcopy__(self, /, memo: _Ignored) -> Self: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def copy(self, /, *args: _Ignored, **kwargs: _Ignored) -> Self: ...

# we cannot meaningfully annotate `frommethod` further, because the callable signature
# of the return type fully depends on the *value* of `methodname` and `reversed` in
# a way that cannot be expressed in the Python type system.
def _frommethod(methodname: str, reversed: bool = False) -> types.FunctionType: ...

# TODO: sync with `MaskedArray` methods
def harden_mask(a: _MArrayT) -> _MArrayT: ...
def soften_mask(a: _MArrayT) -> _MArrayT: ...
def shrink_mask(a: _MArrayT) -> _MArrayT: ...
def ids(a: ArrayLike) -> tuple[int, int]: ...

# keep in sync with `ndarray.nonzero`
def nonzero(a: ArrayLike) -> tuple[_nt.Array1D[np.intp], ...]: ...

# TODO: sync with `MaskedArray.ravel`
@overload
def ravel(a: np.ndarray[Any, _DTypeT], order: _OrderKACF = "C") -> MaskedArray[_nt.Rank1, _DTypeT]: ...
@overload
def ravel(a: _ArrayLike[_ScalarT], order: _OrderKACF = "C") -> _nt.MArray1D[_ScalarT]: ...
@overload
def ravel(a: ArrayLike, order: _OrderKACF = "C") -> _nt.MArray1D[Incomplete]: ...

# keep roughly in sync with `lib._function_base_impl.copy`
@overload
def copy(a: _MArrayT, order: _OrderKACF = "C") -> _MArrayT: ...
@overload
def copy(a: np.ndarray[_ShapeT, _DTypeT], order: _OrderKACF = "C") -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload
def copy(a: _ArrayLike[_ScalarT], order: _OrderKACF = "C") -> _nt.MArray[_ScalarT]: ...
@overload
def copy(a: ArrayLike, order: _OrderKACF = "C") -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.diagonal`
@overload
def diagonal(
    a: _nt._ToArray_nd[_ScalarT], offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
) -> _nt.MArray[_ScalarT]: ...
@overload
def diagonal(
    a: ArrayLike, offset: CanIndex = 0, axis1: CanIndex = 0, axis2: CanIndex = 1
) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.repeat`
@overload
def repeat(
    a: _nt._ToArray_nd[_ScalarT], repeats: _nt.CoInteger_nd, axis: CanIndex | None = None
) -> _nt.MArray[_ScalarT]: ...
@overload
def repeat(a: ArrayLike, repeats: _nt.CoInteger_nd, axis: CanIndex | None = None) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core.fromnumeric.swapaxes`
@overload
def swapaxes(a: _nt._ToArray_nd[_ScalarT], axis1: CanIndex, axis2: CanIndex) -> _nt.MArray[_ScalarT]: ...
@overload
def swapaxes(a: ArrayLike, axis1: CanIndex, axis2: CanIndex) -> _nt.MArray[Incomplete]: ...

# TODO: roughly sync with `MaskedArray.anom`
# The `MaskedArray.anom` definition is specific to `MaskedArray`, so we need
# additional overloads to cover the array-like input here.
@overload  # a: MaskedArray, dtype=None
def anom(a: _MArrayT, axis: CanIndex | None = None, dtype: None = None) -> _MArrayT: ...
@overload  # a: array-like, dtype=None
def anom(a: _ArrayLike[_ScalarT], axis: CanIndex | None = None, dtype: None = None) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: dtype-like (positional)
def anom(a: ArrayLike, axis: CanIndex | None, dtype: _DTypeLike[_ScalarT]) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: dtype-like (keyword)
def anom(a: ArrayLike, axis: CanIndex | None = None, *, dtype: _DTypeLike[_ScalarT]) -> _nt.MArray[_ScalarT]: ...
@overload  # a: unknown array-like, dtype: unknown dtype-like (positional)
def anom(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike | None) -> _nt.MArray[Incomplete]: ...
@overload  # a: unknown array-like, dtype: unknown dtype-like (keyword)
def anom(a: ArrayLike, axis: CanIndex | None = None, *, dtype: DTypeLike | None) -> _nt.MArray[Incomplete]: ...

anomalies = anom

# TODO: sync with `MaskedArray.all`
# Keep in sync with `any`
@overload
def all(a: ArrayLike, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> np.bool: ...
@overload
def all(a: ArrayLike, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[np.bool]: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]
) -> _nt.MArray[np.bool]: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
) -> np.bool | _nt.MArray[np.bool]: ...
@overload
def all(a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload
def all(
    a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.any`
# Keep in sync with `all`
@overload
def any(a: ArrayLike, axis: None = None, out: None = None, keepdims: L[False] | _NoValueType = ...) -> np.bool: ...
@overload
def any(a: ArrayLike, axis: _ShapeLike | None, out: None, keepdims: L[True]) -> _nt.MArray[np.bool]: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, *, keepdims: L[True]
) -> _nt.MArray[np.bool]: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, out: None = None, keepdims: bool | _NoValueType = ...
) -> np.bool | _nt.MArray[np.bool]: ...
@overload
def any(a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...) -> _ArrayT: ...
@overload
def any(
    a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.compress`
# NOTE: The `MaskedArray.compress` definition uses its `DTypeT_co` type parameter,
# which wouldn't work here for array-like inputs, so we need additional overloads.
@overload
def compress(
    condition: _nt.ToBool_nd, a: _ArrayLike[_ScalarT], axis: None = None, out: None = None
) -> _nt.MArray1D[_ScalarT]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: _ArrayLike[_ScalarT], axis: _ShapeLike, out: None = None
) -> _nt.MArray[_ScalarT]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: ArrayLike, axis: None = None, out: None = None
) -> _nt.MArray1D[Incomplete]: ...
@overload
def compress(
    condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload
def compress(condition: _nt.ToBool_nd, a: ArrayLike, axis: _ShapeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

# TODO: sync with `MaskedArray.cumsum`
# Keep in sync with `cumprod`
@overload  # out: None (default)
def cumsum(
    a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload  # out: ndarray (positional)
def cumsum(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload  # out: ndarray (kwarg)
def cumsum(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

# TODO: sync with `MaskedArray.cumprod`
# Keep in sync with `cumsum`
@overload  # out: None (default)
def cumprod(
    a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, out: None = None
) -> _nt.MArray[Incomplete]: ...
@overload  # out: ndarray (positional)
def cumprod(a: ArrayLike, axis: CanIndex | None, dtype: DTypeLike | None, out: _ArrayT) -> _ArrayT: ...
@overload  # out: ndarray (kwarg)
def cumprod(a: ArrayLike, axis: CanIndex | None = None, dtype: DTypeLike | None = None, *, out: _ArrayT) -> _ArrayT: ...

# TODO: sync with `MaskedArray.mean`
# Keep in sync with `sum`, `prod`, and `product`
@overload
def mean(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...
@overload
def mean(
    a: ArrayLike, axis: _ShapeLike | None, dtype: DTypeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...
@overload
def mean(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.sum`
# Keep in sync with `mean`, `prod`, and `product`
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...
@overload
def sum(
    a: ArrayLike, axis: _ShapeLike | None, dtype: DTypeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...
@overload
def sum(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.prod`
# Keep in sync with `mean`, `sum`, and `product`
@overload
def prod(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    keepdims: bool | _NoValueType = ...,
) -> Incomplete: ...
@overload
def prod(
    a: ArrayLike, axis: _ShapeLike | None, dtype: DTypeLike | None, out: _ArrayT, keepdims: bool | _NoValueType = ...
) -> _ArrayT: ...
@overload
def prod(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

product = prod

# TODO: sync with `MaskedArray.trace`
# Keep in sync with `_core.fromnumeric.trace`
@overload
def trace(
    a: ArrayLike,
    offset: CanIndex = 0,
    axis1: CanIndex = 0,
    axis2: CanIndex = 1,
    dtype: DTypeLike | None = None,
    out: None = None,
) -> Incomplete: ...
@overload
def trace(
    a: ArrayLike, offset: CanIndex, axis1: CanIndex, axis2: CanIndex, dtype: DTypeLike | None, out: _ArrayT
) -> _ArrayT: ...
@overload
def trace(
    a: ArrayLike,
    offset: CanIndex = 0,
    axis1: CanIndex = 0,
    axis2: CanIndex = 1,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.std`
# keep in sync with `var`
@overload
def std(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> Incomplete: ...
@overload
def std(
    a: ArrayLike,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def std(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.var`
# keep in sync with `std`
@overload
def var(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    out: None = None,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> Incomplete: ...
@overload
def var(
    a: ArrayLike,
    axis: _ShapeLike | None,
    dtype: DTypeLike | None,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def var(
    a: ArrayLike,
    axis: _ShapeLike | None = None,
    dtype: DTypeLike | None = None,
    *,
    out: _ArrayT,
    ddof: float = 0,
    keepdims: bool | _NoValueType = ...,
    mean: _nt.CoComplex_nd | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.count`
@overload
def count(a: ArrayLike, axis: None = None, keepdims: L[False] | _NoValueType = ...) -> int: ...
@overload
def count(a: ArrayLike, axis: _ShapeLike, keepdims: bool | _NoValueType = ...) -> _nt.Array[np.int_]: ...
@overload
def count(a: ArrayLike, axis: _ShapeLike | None = None, *, keepdims: L[True]) -> _nt.Array[np.int_]: ...
@overload
def count(a: ArrayLike, axis: _ShapeLike | None, keepdims: L[True]) -> _nt.Array[np.int_]: ...

# TODO: sync with `MaskedArray.argmin`
# Keep in sync with `argmax`
@overload
def argmin(
    a: ArrayLike,
    axis: None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def argmin(
    a: ArrayLike,
    axis: CanIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def argmin(
    a: ArrayLike,
    axis: CanIndex | None,
    fill_value: _ScalarLike_co | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

# TODO: sync with `MaskedArray.argmax`
# Keep in sync with `argmin`
@overload
def argmax(
    a: ArrayLike,
    axis: None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: L[False] | _NoValueType = ...,
) -> np.intp: ...
@overload
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    out: None = None,
    *,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def argmax(
    a: ArrayLike,
    axis: CanIndex | None = None,
    fill_value: _ScalarLike_co | None = None,
    *,
    out: _ArrayT,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def argmax(
    a: ArrayLike,
    axis: CanIndex | None,
    fill_value: _ScalarLike_co | None,
    out: _ArrayT,
    *,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

minimum: _extrema_operation
maximum: _extrema_operation

#
def array(
    data: Incomplete,
    dtype: Incomplete = ...,
    copy: Incomplete = ...,
    order: Incomplete = ...,
    mask: Incomplete = ...,
    fill_value: Incomplete = ...,
    keep_mask: Incomplete = ...,
    hard_mask: Incomplete = ...,
    shrink: Incomplete = ...,
    subok: Incomplete = ...,
    ndmin: Incomplete = ...,
) -> Incomplete: ...

#
@overload
def min(
    obj: _ArrayLike[_ScalarT],
    axis: None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: L[False] | _NoValueType = ...,
) -> _ScalarT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    out: None = None,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> Any: ...
@overload
def min(
    obj: ArrayLike,
    axis: None,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...
@overload
def min(
    obj: ArrayLike,
    axis: _ShapeLike | None = None,
    *,
    out: _ArrayT,
    fill_value: _ScalarLike_co | None = None,
    keepdims: bool | _NoValueType = ...,
) -> _ArrayT: ...

#
def max(
    obj: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    fill_value: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...
def ptp(
    obj: Incomplete,
    axis: Incomplete = ...,
    out: Incomplete = ...,
    fill_value: Incomplete = ...,
    keepdims: Incomplete = ...,
) -> Incomplete: ...

#
def take(
    a: Incomplete, indices: Incomplete, axis: Incomplete = ..., out: Incomplete = ..., mode: Incomplete = ...
) -> Incomplete: ...
def power(a: Incomplete, b: Incomplete, third: Incomplete = ...) -> Incomplete: ...
def argsort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
    *,
    stable: Incomplete = ...,
) -> Incomplete: ...
def sort(
    a: Incomplete,
    axis: Incomplete = ...,
    kind: Incomplete = ...,
    order: Incomplete = ...,
    endwith: Incomplete = ...,
    fill_value: Incomplete = ...,
    *,
    stable: Incomplete = ...,
) -> Incomplete: ...
def compressed(x: Incomplete) -> Incomplete: ...
def concatenate(arrays: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def diag(v: Incomplete, k: Incomplete = ...) -> Incomplete: ...
def left_shift(a: Incomplete, n: Incomplete) -> Incomplete: ...
def right_shift(a: Incomplete, n: Incomplete) -> Incomplete: ...
def put(a: Incomplete, indices: Incomplete, values: Incomplete, mode: Incomplete = ...) -> Incomplete: ...
def putmask(a: Incomplete, mask: Incomplete, values: Incomplete) -> Incomplete: ...
def transpose(a: Incomplete, axes: Incomplete = ...) -> Incomplete: ...
def reshape(a: Incomplete, new_shape: Incomplete, order: Incomplete = ...) -> Incomplete: ...
def resize(x: Incomplete, new_shape: Incomplete) -> Incomplete: ...
def ndim(obj: Incomplete) -> Incomplete: ...
def shape(obj: Incomplete) -> Incomplete: ...
def size(obj: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def diff(
    a: Incomplete, /, n: Incomplete = ..., axis: Incomplete = ..., prepend: Incomplete = ..., append: Incomplete = ...
) -> Incomplete: ...
def where(condition: Incomplete, x: Incomplete = ..., y: Incomplete = ...) -> Incomplete: ...
def choose(indices: Incomplete, choices: Incomplete, out: Incomplete = ..., mode: Incomplete = ...) -> Incomplete: ...
def round_(a: Incomplete, decimals: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
def inner(a: Incomplete, b: Incomplete) -> Incomplete: ...
def outer(a: Incomplete, b: Incomplete) -> Incomplete: ...
def correlate(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def convolve(a: Incomplete, v: Incomplete, mode: Incomplete = ..., propagate_mask: Incomplete = ...) -> Incomplete: ...
def allequal(a: Incomplete, b: Incomplete, fill_value: Incomplete = ...) -> Incomplete: ...
def allclose(
    a: Incomplete, b: Incomplete, masked_equal: Incomplete = ..., rtol: Incomplete = ..., atol: Incomplete = ...
) -> Incomplete: ...

# keep in sync with `array`
@overload
def asarray(a: _ArrayLike[_ScalarT], dtype: None = None, order: _OrderKACF | None = None) -> _nt.MArray[_ScalarT]: ...
@overload
def asarray(a: object, dtype: _DTypeLike[_ScalarT], order: _OrderKACF | None = None) -> _nt.MArray[_ScalarT]: ...
@overload
def asarray(a: object, dtype: DTypeLike | None = None, order: _OrderKACF | None = None) -> _nt.MArray[_ScalarT]: ...

# keep in sync with `asarray` (but note the additional first overload)
@overload
def asanyarray(a: _MArrayT, dtype: None = None, order: _OrderKACF | None = None) -> _MArrayT: ...
@overload
def asanyarray(
    a: _ArrayLike[_ScalarT], dtype: None = None, order: _OrderKACF | None = None
) -> _nt.MArray[_ScalarT]: ...
@overload
def asanyarray(a: object, dtype: _DTypeLike[_ScalarT], order: _OrderKACF | None = None) -> _nt.MArray[_ScalarT]: ...
@overload
def asanyarray(a: object, dtype: DTypeLike | None = None, order: _OrderKACF | None = None) -> _nt.MArray[_ScalarT]: ...

#
def fromflex(fxarray: Incomplete) -> Incomplete: ...
def make_mask_descr(ndtype: Incomplete) -> Incomplete: ...
def getmask(a: Incomplete) -> Incomplete: ...
def getmaskarray(arr: Incomplete) -> Incomplete: ...
def is_mask(m: Incomplete) -> Incomplete: ...
def make_mask(
    m: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ..., dtype: Incomplete = ...
) -> Incomplete: ...
def make_mask_none(newshape: Incomplete, dtype: Incomplete = ...) -> Incomplete: ...
def mask_or(m1: Incomplete, m2: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ...) -> Incomplete: ...
def flatten_mask(mask: Incomplete) -> Incomplete: ...
def masked_where(condition: Incomplete, a: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_greater(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_greater_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_less(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_less_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_not_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_equal(x: Incomplete, value: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_inside(x: Incomplete, v1: Incomplete, v2: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_outside(x: Incomplete, v1: Incomplete, v2: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def masked_object(x: Incomplete, value: Incomplete, copy: Incomplete = ..., shrink: Incomplete = ...) -> Incomplete: ...
def masked_values(
    x: Incomplete,
    value: Incomplete,
    rtol: Incomplete = ...,
    atol: Incomplete = ...,
    copy: Incomplete = ...,
    shrink: Incomplete = ...,
) -> Incomplete: ...
def masked_invalid(a: Incomplete, copy: Incomplete = ...) -> Incomplete: ...
def flatten_structured_array(a: Incomplete) -> Incomplete: ...
def append(a: Incomplete, b: Incomplete, axis: Incomplete = ...) -> Incomplete: ...
def dot(a: Incomplete, b: Incomplete, strict: Incomplete = ..., out: Incomplete = ...) -> Incomplete: ...
def default_fill_value(obj: Incomplete) -> Incomplete: ...
def minimum_fill_value(obj: Incomplete) -> Incomplete: ...
def maximum_fill_value(obj: Incomplete) -> Incomplete: ...
def set_fill_value(a: Incomplete, fill_value: Incomplete) -> Incomplete: ...
def common_fill_value(a: Incomplete, b: Incomplete) -> Incomplete: ...
def filled(a: Incomplete, fill_value: Incomplete | None = None) -> Incomplete: ...
def getdata(a: Incomplete, subok: bool = True) -> Incomplete: ...
def fix_invalid(
    a: Incomplete, mask: Incomplete = ..., copy: bool = True, fill_value: Incomplete | None = None
) -> Incomplete: ...
def is_masked(x: Incomplete) -> Incomplete: ...
def isMaskedArray(x: Incomplete) -> Incomplete: ...

#
masked: Final[MaskedConstant] = ...
masked_singleton: Final[MaskedConstant] = ...

masked_array = MaskedArray

#
isarray = isMaskedArray
isMA = isMaskedArray
round = round_
innerproduct = inner
outerproduct = outer
get_mask = getmask
get_data = getdata

exp: _MaskedUnaryOperation
conjugate: _MaskedUnaryOperation
sin: _MaskedUnaryOperation
cos: _MaskedUnaryOperation
arctan: _MaskedUnaryOperation
arcsinh: _MaskedUnaryOperation
sinh: _MaskedUnaryOperation
cosh: _MaskedUnaryOperation
tanh: _MaskedUnaryOperation
abs: _MaskedUnaryOperation
absolute: _MaskedUnaryOperation
angle: _MaskedUnaryOperation
fabs: _MaskedUnaryOperation
negative: _MaskedUnaryOperation
floor: _MaskedUnaryOperation
ceil: _MaskedUnaryOperation
around: _MaskedUnaryOperation
logical_not: _MaskedUnaryOperation
sqrt: _MaskedUnaryOperation
log: _MaskedUnaryOperation
log2: _MaskedUnaryOperation
log10: _MaskedUnaryOperation
tan: _MaskedUnaryOperation
arcsin: _MaskedUnaryOperation
arccos: _MaskedUnaryOperation
arccosh: _MaskedUnaryOperation
arctanh: _MaskedUnaryOperation

add: _MaskedBinaryOperation
subtract: _MaskedBinaryOperation
multiply: _MaskedBinaryOperation
arctan2: _MaskedBinaryOperation
equal: _MaskedBinaryOperation
not_equal: _MaskedBinaryOperation
less_equal: _MaskedBinaryOperation
greater_equal: _MaskedBinaryOperation
less: _MaskedBinaryOperation
greater: _MaskedBinaryOperation
logical_and: _MaskedBinaryOperation

def alltrue(
    target: _nt.ToGeneric_nd, axis: CanIndex | None = 0, dtype: _nt.ToDTypeBool | None = None
) -> Incomplete: ...

logical_or: _MaskedBinaryOperation

def sometrue(
    target: _nt.ToGeneric_nd, axis: CanIndex | None = 0, dtype: _nt.ToDTypeBool | None = None
) -> Incomplete: ...

logical_xor: _MaskedBinaryOperation
bitwise_and: _MaskedBinaryOperation
bitwise_or: _MaskedBinaryOperation
bitwise_xor: _MaskedBinaryOperation
hypot: _MaskedBinaryOperation

divide: _DomainedBinaryOperation
true_divide: _DomainedBinaryOperation
floor_divide: _DomainedBinaryOperation
remainder: _DomainedBinaryOperation
fmod: _DomainedBinaryOperation
mod: _DomainedBinaryOperation

# internal wrapper functions for the functions below
def _convert2ma(
    funcname: str, np_ret: str, np_ma_ret: str, params: dict[str, Any] | None = None
) -> Callable[..., Any]: ...

# keep in sync with `_core.multiarray.arange`
@overload  # (int-like, int-like?, int-like?)
def arange(
    start_or_stop: _ToInt,
    /,
    stop: _ToInt | None = None,
    step: _ToInt | None = 1,
    *,
    dtype: _nt.ToDTypeInt64 | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: int | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.int64]: ...
@overload  # (float, float-like?, float-like?)
def arange(
    start_or_stop: float | np.floating,
    /,
    stop: _ToFloat | None = None,
    step: _ToFloat | None = 1,
    *,
    dtype: type[float] | _DTypeLike[np.float64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64 | Any]: ...
@overload  # (float-like, float, float-like?)
def arange(
    start_or_stop: _ToFloat,
    /,
    stop: float | np.floating,
    step: _ToFloat | None = 1,
    *,
    dtype: type[float] | _DTypeLike[np.float64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64 | Any]: ...
@overload  # (timedelta, timedelta-like?, timedelta-like?)
def arange(
    start_or_stop: np.timedelta64,
    /,
    stop: _ToTD64 | None = None,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.timedelta64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: _ToTD64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.timedelta64[Incomplete]]: ...
@overload  # (timedelta-like, timedelta, timedelta-like?)
def arange(
    start_or_stop: _ToTD64,
    /,
    stop: np.timedelta64,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.timedelta64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: _ToTD64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.timedelta64[Incomplete]]: ...
@overload  # (datetime, datetime, timedelta-like) (requires both start and stop)
def arange(
    start_or_stop: np.datetime64,
    /,
    stop: np.datetime64,
    step: _ToTD64 | None = 1,
    *,
    dtype: _DTypeLike[np.datetime64] | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: np.datetime64 | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.datetime64[Incomplete]]: ...
@overload  # dtype=<known>
def arange(
    start_or_stop: _ArangeScalar | float,
    /,
    stop: _ArangeScalar | float | None = None,
    step: _ArangeScalar | float | None = 1,
    *,
    dtype: _DTypeLike[_ArangeScalarT],
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[_ArangeScalarT]: ...
@overload  # dtype=<unknown>
def arange(
    start_or_stop: _ArangeScalar | float,
    /,
    stop: _ArangeScalar | float | None = None,
    step: _ArangeScalar | float | None = 1,
    *,
    dtype: DTypeLike | None = None,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[Incomplete]: ...

# based on `_core.fromnumeric.clip`
@overload
def clip(
    a: _ScalarT,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _ScalarT: ...
@overload
def clip(
    a: _nt.Array[_ScalarT],
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _nt.MArray[_ScalarT]: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | None,
    a_max: ArrayLike | None,
    out: _MArrayT,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _MArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    *,
    out: _MArrayT,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> _MArrayT: ...
@overload
def clip(
    a: ArrayLike,
    a_min: ArrayLike | _NoValueType | None = ...,
    a_max: ArrayLike | _NoValueType | None = ...,
    out: None = None,
    *,
    min: ArrayLike | _NoValueType | None = ...,
    max: ArrayLike | _NoValueType | None = ...,
    fill_value: complex | None = None,
    hardmask: bool = False,
    dtype: DTypeLike | None = None,
    **kwargs: Unpack[_UFuncKwargs],
) -> Incomplete: ...

# keep in sync with `_core._multiarray_umath.empty`
@overload  # 1d shape, default dtype (float64)
def empty(
    shape: _ShapeLike1D,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[np.float64]: ...
@overload  # 1d shape, known dtype
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[_nt.Rank1, _DTypeT]: ...
@overload  # 1d shape, known scalar-type
def empty(
    shape: _ShapeLike1D,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[_ScalarT]: ...
@overload  # 1d shape, unknown dtype
def empty(
    shape: _ShapeLike1D,
    dtype: DTypeLike | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray1D[Incomplete]: ...
@overload  # known shape, default dtype (float64)
def empty(
    shape: _ShapeT,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.float64, _ShapeT]: ...
@overload  # known shape, known dtype  (mypy reports a false positive)
def empty(
    shape: _ShapeT,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # known shape, known scalar-type
def empty(
    shape: _ShapeT,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # known shape, unknown scalar-type
def empty(
    shape: _ShapeT,
    dtype: DTypeLike | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete, _ShapeT]: ...
@overload  # unknown shape, default dtype
def empty(
    shape: _ShapeLike,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.float64]: ...
@overload  # unknown shape, known dtype
def empty(
    shape: _ShapeLike,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> MaskedArray[Incomplete, _DTypeT]: ...
@overload  # unknown shape, known scalar-type
def empty(
    shape: _ShapeLike,
    dtype: _DTypeLike[_ScalarT],
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload  # unknown shape, unknown dtype
def empty(
    shape: _ShapeLike,
    dtype: DTypeLike | None = None,
    order: np._OrderCF = "C",
    *,
    device: _Device | None = None,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete]: ...

# keep in sync with `_core._multiarray_umath.empty_like`
@overload  # known array, subok=True
def empty_like(
    prototype: _MArrayT,
    /,
    dtype: None = None,
    order: _OrderKACF = "K",
    subok: L[True] = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> _MArrayT: ...
@overload  # array-like with known shape and type
def empty_like(
    prototype: _CanArray[np.ndarray[_ShapeT, _DTypeT]],
    /,
    dtype: _DTypeT | _HasDType[_DTypeT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: None = None,
    *,
    device: _Device | None = None,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.bool_],
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.bool_]: ...
@overload  # bool 0d array-like
def empty_like(
    prototype: _nt.ToBool_0d,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.bool_]: ...
@overload  # bool 1d array-like
def empty_like(
    prototype: _nt.ToBool_1ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.bool_]: ...
@overload  # bool 2d array-like
def empty_like(
    prototype: _nt.ToBool_2ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.bool_]: ...
@overload  # bool 3d array-like
def empty_like(
    prototype: _nt.ToBool_3ds,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.bool_]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(  # type: ignore[overload-overlap]  # python/mypy#19908
    prototype: _nt._ToArray_nnd[np.intp],
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.intp]: ...
@overload  # int 0d array-like
def empty_like(
    prototype: _nt.ToInt_0d,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.intp]: ...
@overload  # int 1d array-like
def empty_like(
    prototype: _nt.ToInt_1ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.intp]: ...
@overload  # int 2d array-like
def empty_like(
    prototype: _nt.ToInt_2ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.intp]: ...
@overload  # int 3d array-like
def empty_like(
    prototype: _nt.ToInt_3ds,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.intp]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(  # type: ignore[overload-overlap]  # python/mypy#19908
    prototype: _nt._ToArray_nnd[np.float64],
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.float64]: ...
@overload  # float 0d array-like
def empty_like(
    prototype: _nt.ToFloat64_0d,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.float64]: ...
@overload  # float 1d array-like
def empty_like(
    prototype: _nt.ToFloat64_1ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.float64]: ...
@overload  # float 2d array-like
def empty_like(
    prototype: _nt.ToFloat64_2ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.float64]: ...
@overload  # float 3d array-like
def empty_like(
    prototype: _nt.ToFloat64_3ds,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.float64]: ...
@overload  # complex 0d array-like
def empty_like(
    prototype: _nt.ToComplex128_0d,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray0D[np.complex128]: ...
@overload  # workaround for microsoft/pyright#10232
def empty_like(
    prototype: _nt._ToArray_nnd[np.complex128],
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: tuple[()] | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.complex128]: ...
@overload  # complex 1d array-like
def empty_like(
    prototype: _nt.ToComplex128_1ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike1D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray1D[np.complex128]: ...
@overload  # complex 2d array-like
def empty_like(
    prototype: _nt.ToComplex128_2ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike2D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray2D[np.complex128]: ...
@overload  # complex 3d array-like
def empty_like(
    prototype: _nt.ToComplex128_3ds,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike3D | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray3D[np.complex128]: ...
@overload  # array-like with known scalar-type, given shape
def empty_like(
    prototype: _ArrayLike[_ScalarT],
    /,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # array-like with known scalar-type, unknown shape
def empty_like(
    prototype: _ArrayLike[_ScalarT],
    /,
    dtype: np.dtype[_ScalarT] | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload  # given shape, given dtype
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> MaskedArray[_ShapeT, _DTypeT]: ...
@overload  # unknown shape, given dtype
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeT | _HasDType[_DTypeT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> MaskedArray[Incomplete, _DTypeT]: ...
@overload  # given shape, given scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT, _ShapeT]: ...
@overload  # unknown shape, given scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: _DTypeLike[_ScalarT],
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload  # bool array-like
def empty_like(
    prototype: _nt.ToBool_nd,
    /,
    dtype: _nt.ToDTypeBool | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.bool_]: ...
@overload  # int array-like
def empty_like(
    prototype: _nt.ToInt_nd,
    /,
    dtype: _nt.ToDTypeInt64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.intp]: ...
@overload  # float array-like
def empty_like(
    prototype: _nt.ToFloat64_nd,
    /,
    dtype: _nt.ToDTypeFloat64 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.float64]: ...
@overload  # complex array-like
def empty_like(
    prototype: _nt.ToComplex128_nd,
    /,
    dtype: _nt.ToDTypeComplex128 | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[np.complex128]: ...
@overload  # given shape, unknown scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    *,
    shape: _ShapeT,
    device: _Device | None = None,
) -> _nt.MArray[Incomplete, _ShapeT]: ...
@overload  # unknown shape, unknown scalar-type
def empty_like(
    prototype: object,
    /,
    dtype: DTypeLike | None = None,
    order: _OrderKACF = "K",
    subok: bool = True,
    shape: _ShapeLike | None = None,
    *,
    device: _Device | None = None,
) -> _nt.MArray[Incomplete]: ...

# This is a bit of a hack to avoid having to duplicate all those `empty` overloads for
# `ones` and `zeros`, that relies on the fact that empty/zeros/ones have identical
# type signatures, but may cause some type-checkers to report incorrect names in case
# of user errors. Mypy and Pyright seem to handle this just fine.
ones = empty
ones_like = empty_like
zeros = empty
zeros_like = empty_like

# keep in sync with `_core._multiarray_umath.frombuffer`
@overload
def frombuffer(
    buffer: Buffer, *, count: CanIndex = -1, offset: CanIndex = 0, like: _CanArrayFunc | None = None
) -> _nt.MArray[np.float64]: ...
@overload
def frombuffer(
    buffer: Buffer,
    dtype: _DTypeLike[_ScalarT],
    count: CanIndex = -1,
    offset: CanIndex = 0,
    *,
    like: _CanArrayFunc | None = None,
) -> _nt.MArray[_ScalarT]: ...
@overload
def frombuffer(
    buffer: Buffer,
    dtype: DTypeLike | None,
    count: CanIndex = -1,
    offset: CanIndex = 0,
    *,
    like: _CanArrayFunc | None = None,
) -> _nt.MArray[Incomplete]: ...

# keep roughly in sync with `_core.numeric.fromfunction`
def fromfunction(
    function: Callable[..., np.ndarray[_ShapeT, _DTypeT]],
    shape: Sequence[int],
    *,
    dtype: DTypeLike | None = ...,  # = float
    like: _CanArrayFunc | None = None,
    **kwargs: object,
) -> MaskedArray[_ShapeT, _DTypeT]: ...

# keep roughly in sync with `_core.numeric.identity`
@overload
def identity(
    n: int,
    dtype: _nt.ToDTypeFloat64 | None = None,
    *,
    like: _CanArrayFunc | None = None,
    fill_value: float | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[np.float64]: ...
@overload
def identity(
    n: int,
    dtype: _DTypeLike[_ScalarT],
    *,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[_ScalarT]: ...
@overload
def identity(
    n: int,
    dtype: DTypeLike | None = None,
    *,
    like: _CanArrayFunc | None = None,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray2D[Incomplete]: ...

# keep roughly in sync with `_core.numeric.indices`
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt] = ...,
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[np.intp]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt],
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: type[_nt.JustInt] = ...,
    *,
    sparse: L[True],
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[np.intp], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: _DTypeLike[_ScalarT],
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: _DTypeLike[_ScalarT],
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[_ScalarT], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike | None = None,
    sparse: L[False] = False,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[Incomplete]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike | None,
    sparse: L[True],
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[Incomplete], ...]: ...
@overload
def indices(
    dimensions: _nt.ToInteger_1d,
    dtype: DTypeLike | None = None,
    *,
    sparse: L[True],
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> tuple[_nt.MArray[Incomplete], ...]: ...

# keep roughly in sync with `_core.fromnumeric.squeeze`
@overload  # workaround for microsoft/pyright#10232
def squeeze(
    a: _ScalarT, axis: _ShapeLike | None = None, *, fill_value: complex | None = None, hardmask: bool = False
) -> _nt.MArray0D[_ScalarT]: ...
@overload  # workaround for microsoft/pyright#10232
def squeeze(
    a: _nt._ToArray_nnd[_ScalarT],
    axis: _ShapeLike | None = None,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def squeeze(
    a: _nt._ToArray_nd[_ScalarT],
    axis: _ShapeLike | None = None,
    *,
    fill_value: complex | None = None,
    hardmask: bool = False,
) -> _nt.MArray[_ScalarT]: ...
@overload
def squeeze(
    a: ArrayLike, axis: _ShapeLike | None = None, *, fill_value: complex | None = None, hardmask: bool = False
) -> _nt.MArray[Incomplete]: ...
