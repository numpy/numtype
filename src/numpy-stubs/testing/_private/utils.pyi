# pyright: reportRedeclaration=false

import ast
import sys
import types
import unittest
import warnings
from _typeshed import ConvertibleToFloat, GenericPath, StrOrBytesPath, StrPath
from collections.abc import Callable, Iterable, Sequence
from contextlib import _GeneratorContextManager
from re import Pattern
from typing import (
    Any,
    AnyStr,
    ClassVar,
    Final,
    Generic,
    Literal as L,
    NoReturn,
    SupportsIndex,
    TypeAlias,
    overload,
)
from typing_extensions import ParamSpec, Self, TypeVar
from unittest.case import SkipTest

import numpy as np
from numpy._typing import (
    ArrayLike,
    DTypeLike,
    NDArray,
    _ArrayLikeDT64_co,
    _ArrayLikeNumber_co,
    _ArrayLikeObject_co,
    _ArrayLikeTD64_co,
)

__all__ = [
    "HAS_LAPACK64",
    "HAS_REFCOUNT",
    "IS_EDITABLE",
    "IS_MUSL",
    "IS_PYPY",
    "IS_PYSTON",
    "IS_WASM",
    "NOGIL_BUILD",
    "IgnoreException",
    "KnownFailureException",
    "SkipTest",
    "assert_",
    "assert_allclose",
    "assert_almost_equal",
    "assert_approx_equal",
    "assert_array_almost_equal",
    "assert_array_almost_equal_nulp",
    "assert_array_compare",
    "assert_array_equal",
    "assert_array_less",
    "assert_array_max_ulp",
    "assert_equal",
    "assert_no_gc_cycles",
    "assert_no_warnings",
    "assert_raises",
    "assert_raises_regex",
    "assert_string_equal",
    "assert_warns",
    "break_cycles",
    "build_err_msg",
    "check_support_sve",
    "clear_and_catch_warnings",
    "decorate_methods",
    "jiffies",
    "measure",
    "memusage",
    "print_assert_equal",
    "run_threaded",
    "rundocs",
    "runstring",
    "suppress_warnings",
    "tempdir",
    "temppath",
    "verbose",
]

_WarnLog: TypeAlias = list[warnings.WarningMessage]
_ToModules: TypeAlias = Iterable[types.ModuleType]
_ComparisonFunc: TypeAlias = Callable[
    [NDArray[Any], NDArray[Any]],
    bool | np.bool | np.number | NDArray[np.bool | np.number | np.object_],
]

_P = ParamSpec("_P")
_T = TypeVar("_T")
_ET = TypeVar("_ET", bound=BaseException)
_FT = TypeVar("_FT", bound=Callable[..., object])
_W_co = TypeVar("_W_co", bound=_WarnLog | None, default=_WarnLog | None, covariant=True)

###

verbose: int = 0
IS_EDITABLE: Final[bool] = ...
IS_MUSL: Final[bool] = ...
IS_PYPY: Final[bool] = ...
IS_PYSTON: Final[bool] = ...
IS_WASM: Final[bool] = ...
HAS_REFCOUNT: Final[bool] = ...
HAS_LAPACK64: Final[bool] = ...
NOGIL_BUILD: Final[bool] = ...

class KnownFailureException(Exception): ...
class IgnoreException(Exception): ...

# NOTE: `warnings.catch_warnings` is incorrectly defined as invariant in typeshed
class clear_and_catch_warnings(warnings.catch_warnings[_W_co], Generic[_W_co]):  # type: ignore[type-var]  # pyright: ignore[reportInvalidTypeArguments]
    class_modules: ClassVar[tuple[types.ModuleType, ...]] = ()
    modules: Final[set[types.ModuleType]]

    @overload  # record: True
    def __init__(self: clear_and_catch_warnings[_WarnLog], /, record: L[True], modules: _ToModules = ()) -> None: ...
    @overload  # record: False (default)
    def __init__(self: clear_and_catch_warnings[None], /, record: L[False] = False, modules: _ToModules = ()) -> None: ...
    @overload  # record; bool
    def __init__(self, /, record: bool, modules: _ToModules = ()) -> None: ...

class suppress_warnings:
    log: Final[_WarnLog]

    def __init__(self, /, forwarding_rule: L["always", "module", "once", "location"] = "always") -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, cls: type[BaseException] | None, exc: BaseException | None, tb: types.TracebackType | None, /) -> None: ...
    def __call__(self, /, func: _FT) -> _FT: ...

    #
    def filter(self, /, category: type[Warning] = ..., message: str = "", module: types.ModuleType | None = None) -> None: ...
    def record(self, /, category: type[Warning] = ..., message: str = "", module: types.ModuleType | None = None) -> _WarnLog: ...

# Contrary to runtime we can't do `os.name` checks while type checking,
# only `sys.platform` checks
if sys.platform != "win32" and sys.platform != "cygwin" and sys.platform != "linux":
    def memusage() -> NoReturn: ...

elif sys.platform == "win32" or sys.platform == "cygwin":
    def memusage(processName: str = ..., instance: int = ...) -> int: ...

else:
    def memusage(_proc_pid_stat: StrOrBytesPath = ...) -> int | None: ...

#
if sys.platform == "linux":
    def jiffies(_proc_pid_stat: StrOrBytesPath = ..., _load_time: list[float] = ...) -> int: ...

else:
    def jiffies(_load_time: list[float] = ...) -> int: ...

#
def assert_(val: object, msg: str | Callable[[], str] = ...) -> None: ...
def assert_equal(actual: object, desired: object, err_msg: object = ..., verbose: bool = ..., *, strict: bool = ...) -> None: ...
def print_assert_equal(test_string: str, actual: object, desired: object) -> None: ...

#
def assert_almost_equal(
    actual: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    desired: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    decimal: int = 7,
    err_msg: object = "",
    verbose: bool = True,
) -> None: ...

#
def assert_approx_equal(
    actual: ConvertibleToFloat,
    desired: ConvertibleToFloat,
    significant: int = 7,
    err_msg: object = "",
    verbose: bool = True,
) -> None: ...

#
def assert_array_compare(
    comparison: _ComparisonFunc,
    x: ArrayLike,
    y: ArrayLike,
    err_msg: object = "",
    verbose: bool = True,
    header: str = "",
    precision: SupportsIndex = 6,
    equal_nan: bool = True,
    equal_inf: bool = True,
    *,
    strict: bool = False,
    names: tuple[str, str] = ("actual", "desired"),
) -> None: ...

#
def assert_array_equal(
    x: ArrayLike,
    y: ArrayLike,
    /,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...

#
def assert_array_almost_equal(
    x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    y: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    /,
    decimal: float = ...,
    err_msg: object = ...,
    verbose: bool = ...,
) -> None: ...

#
@overload
def assert_array_less(
    x: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    y: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
@overload
def assert_array_less(
    x: _ArrayLikeTD64_co,
    y: _ArrayLikeTD64_co,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
@overload
def assert_array_less(
    x: _ArrayLikeDT64_co,
    y: _ArrayLikeDT64_co,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...

#
def assert_string_equal(actual: str, desired: str) -> None: ...

#
@overload
def assert_raises(
    expected_exception: type[BaseException] | tuple[type[BaseException], ...],
    callable: Callable[_P, Any],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None: ...
@overload
def assert_raises(
    expected_exception: type[_ET] | tuple[type[_ET], ...],
    *,
    msg: str | None = ...,
) -> unittest.case._AssertRaisesContext[_ET]: ...

#
@overload
def assert_raises_regex(
    expected_exception: type[BaseException] | tuple[type[BaseException], ...],
    expected_regex: str | bytes | Pattern[Any],
    callable: Callable[_P, Any],
    /,
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> None: ...
@overload
def assert_raises_regex(
    expected_exception: type[_ET] | tuple[type[_ET], ...],
    expected_regex: str | bytes | Pattern[Any],
    *,
    msg: str | None = ...,
) -> unittest.case._AssertRaisesContext[_ET]: ...

#

#
@overload
def assert_allclose(
    actual: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    desired: _ArrayLikeNumber_co | _ArrayLikeObject_co,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...
@overload
def assert_allclose(
    actual: _ArrayLikeTD64_co,
    desired: _ArrayLikeTD64_co,
    rtol: float = ...,
    atol: float = ...,
    equal_nan: bool = ...,
    err_msg: object = ...,
    verbose: bool = ...,
    *,
    strict: bool = ...,
) -> None: ...

#
def assert_array_almost_equal_nulp(x: _ArrayLikeNumber_co, y: _ArrayLikeNumber_co, nulp: float = ...) -> None: ...

#
def assert_array_max_ulp(
    a: _ArrayLikeNumber_co,
    b: _ArrayLikeNumber_co,
    maxulp: float = ...,
    dtype: DTypeLike = ...,
) -> NDArray[Any]: ...

#
@overload
def assert_warns(warning_class: type[Warning]) -> _GeneratorContextManager[None]: ...
@overload
def assert_warns(warning_class: type[Warning], func: Callable[_P, _T], /, *args: _P.args, **kwargs: _P.kwargs) -> _T: ...

#
@overload
def assert_no_warnings() -> _GeneratorContextManager[None]: ...
@overload
def assert_no_warnings(func: Callable[_P, _T], /, *args: _P.args, **kwargs: _P.kwargs) -> _T: ...

#
@overload
def assert_no_gc_cycles() -> _GeneratorContextManager[None]: ...
@overload
def assert_no_gc_cycles(func: Callable[_P, Any], /, *args: _P.args, **kwargs: _P.kwargs) -> None: ...

#
@overload
def tempdir(suffix: None = None, prefix: None = None, dir: None = None) -> _GeneratorContextManager[str]: ...
@overload
def tempdir(
    suffix: AnyStr | None = None,
    prefix: AnyStr | None = None,
    *,
    dir: GenericPath[AnyStr],
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def tempdir(
    suffix: AnyStr | None = None,
    *,
    prefix: AnyStr,
    dir: GenericPath[AnyStr] | None = None,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def tempdir(
    suffix: AnyStr,
    prefix: AnyStr | None = None,
    dir: GenericPath[AnyStr] | None = None,
) -> _GeneratorContextManager[AnyStr]: ...

#
@overload
def temppath(suffix: None = None, prefix: None = None, dir: None = None, text: bool = False) -> _GeneratorContextManager[str]: ...
@overload
def temppath(
    suffix: AnyStr | None,
    prefix: AnyStr | None,
    dir: GenericPath[AnyStr],
    text: bool = False,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def temppath(
    suffix: AnyStr | None = None,
    prefix: AnyStr | None = None,
    *,
    dir: GenericPath[AnyStr],
    text: bool = False,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def temppath(
    suffix: AnyStr | None,
    prefix: AnyStr,
    dir: GenericPath[AnyStr] | None = None,
    text: bool = False,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def temppath(
    suffix: AnyStr | None = None,
    *,
    prefix: AnyStr,
    dir: GenericPath[AnyStr] | None = None,
    text: bool = False,
) -> _GeneratorContextManager[AnyStr]: ...
@overload
def temppath(
    suffix: AnyStr,
    prefix: AnyStr | None = None,
    dir: GenericPath[AnyStr] | None = None,
    text: bool = False,
) -> _GeneratorContextManager[AnyStr]: ...

#
def raises(*args: type[BaseException]) -> Callable[[_FT], _FT]: ...

#
def decorate_methods(
    cls: type[Any],
    decorator: Callable[[Callable[..., Any]], Any],
    testmatch: str | bytes | Pattern[Any] | None = None,
) -> None: ...

#
def build_err_msg(
    arrays: Iterable[object],
    err_msg: str,
    header: str = ...,
    verbose: bool = ...,
    names: Sequence[str] = ...,
    precision: SupportsIndex | None = ...,
) -> str: ...
def measure(code_str: str | bytes | ast.mod | ast.AST, times: int = ..., label: str | None = ...) -> float: ...
def break_cycles() -> None: ...
def run_threaded(func: Callable[[], None], iters: int, pass_count: bool = False) -> None: ...
def runstring(astr: str | bytes | types.CodeType, dict: dict[str, Any] | None) -> Any: ...
def rundocs(filename: StrPath | None = ..., raise_on_error: bool = ...) -> None: ...
def check_support_sve(cache: list[_T], /) -> _T: ...
