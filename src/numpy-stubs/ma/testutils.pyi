from collections.abc import Callable
from typing import Any, TypeAlias
from unittest import TestCase as _TestCase

import numpy as np
from numpy.testing import assert_, assert_allclose, assert_array_almost_equal_nulp, assert_raises

__all__: list[str] = [
    "TestCase",
    "almost",
    "approx",
    "assert_",
    "assert_allclose",
    "assert_almost_equal",
    "assert_array_almost_equal",
    "assert_array_almost_equal_nulp",
    "assert_array_approx_equal",
    "assert_array_compare",
    "assert_array_equal",
    "assert_array_less",
    "assert_close",
    "assert_equal",
    "assert_equal_records",
    "assert_mask_equal",
    "assert_not_equal",
    "assert_raises",
    "fail_if_array_equal",
]

_ComparisonFunc: TypeAlias = Callable[[Any, Any], bool]

def approx(
    a: Any,
    b: Any,
    fill_value: bool = True,
    rtol: float = 1e-5,
    atol: float = 1e-8,
) -> np.ndarray[Any, np.dtype[np.bool_]]: ...
def almost(
    a: Any,
    b: Any,
    decimal: int = 6,
    fill_value: bool = True,
) -> np.ndarray[Any, np.dtype[np.bool_]]: ...
def _assert_equal_on_sequences(
    actual: Any,
    desired: Any,
    err_msg: str = "",
) -> None: ...
def assert_equal_records(a: Any, b: Any) -> None: ...
def assert_equal(actual: Any, desired: Any, err_msg: str = "") -> None: ...
def fail_if_equal(actual: Any, desired: Any, err_msg: str = "") -> None: ...
def assert_not_equal(actual: Any, desired: Any, err_msg: str = "") -> None: ...
def assert_almost_equal(
    actual: Any,
    desired: Any,
    decimal: int = 7,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...
def assert_close(
    actual: Any,
    desired: Any,
    decimal: int = 7,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...
def assert_array_compare(
    comparison: _ComparisonFunc,
    x: Any,
    y: Any,
    err_msg: str = "",
    verbose: bool = True,
    header: str = "",
    fill_value: bool = True,
) -> None: ...
def assert_array_equal(
    x: Any,
    y: Any,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...
def fail_if_array_equal(
    x: Any,
    y: Any,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...

#
def assert_array_approx_equal(
    x: Any,
    y: Any,
    decimal: int = 6,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...
def assert_array_almost_equal(
    x: Any,
    y: Any,
    decimal: int = 6,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...

#
def assert_array_less(
    x: Any,
    y: Any,
    err_msg: str = "",
    verbose: bool = True,
) -> None: ...
def assert_mask_equal(m1: Any, m2: Any, err_msg: str = "") -> None: ...

class TestCase(_TestCase):
    def __init_subclass__(cls, *args: Any, **kwargs: Any) -> None: ...
