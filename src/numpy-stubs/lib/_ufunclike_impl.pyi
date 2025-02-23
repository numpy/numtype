from collections.abc import Sequence
from typing import overload
from typing_extensions import TypeVar

import numpy as np
from _numtype import (
    Array,
    Array_1d,
    Array_2d,
    Array_3d,
    CanArraySized,
    CoFloating_0d,
    CoFloating_1ds,
    CoFloating_1nd,
    CoFloating_2ds,
    CoFloating_3ds,
    CoFloating_nd,
    Is,
    ToBool_0d,
    ToBool_1nd,
    ToFloat64_0d,
    ToFloat64_1nd,
    ToIntP_0d,
    ToIntP_1nd,
    _ToArray1_0d,
    _ToArray1_1ds,
    _ToArray1_1nd,
    _ToArray1_2ds,
    _ToArray1_3ds,
)

__all__ = ["fix", "isneginf", "isposinf"]

###

_ArrayT = TypeVar("_ArrayT", bound=Array)
_ShapeT = TypeVar("_ShapeT", bound=tuple[int, ...])
_RealT = TypeVar("_RealT", bound=np.integer | np.floating | np.object_)

###

#
@overload
def fix(x: CoFloating_nd, out: _ArrayT) -> _ArrayT: ...
@overload
def fix(x: _ArrayT, out: None) -> _ArrayT: ...
@overload
def fix(x: ToBool_0d, out: None = None) -> np.bool: ...  # type: ignore[overload-overlap]
@overload
def fix(x: ToIntP_0d, out: None = None) -> np.intp: ...  # type: ignore[overload-overlap]
@overload
def fix(x: ToFloat64_0d, out: None = None) -> np.float64: ...  # type: ignore[overload-overlap]
@overload
def fix(x: _ToArray1_0d[_RealT], out: None = None) -> _RealT: ...  # type: ignore[overload-overlap]
@overload
def fix(x: _ToArray1_1ds[_RealT], out: None = None) -> Array_1d[_RealT]: ...
@overload
def fix(x: _ToArray1_2ds[_RealT], out: None = None) -> Array_2d[_RealT]: ...
@overload
def fix(x: _ToArray1_3ds[_RealT], out: None = None) -> Array_3d[_RealT]: ...
@overload
def fix(x: ToBool_1nd, out: None = None) -> Array[np.bool]: ...
@overload
def fix(x: ToIntP_1nd, out: None = None) -> Array[np.intp]: ...
@overload  # the `Sequence` is a workaround for a pyright promotion bug
def fix(x: ToFloat64_1nd | Sequence[Is[float]], out: None = None) -> Array[np.float64]: ...
@overload
def fix(x: _ToArray1_1nd[_RealT], out: None = None) -> Array[_RealT]: ...

#
@overload
def isposinf(x: CoFloating_0d, out: None = None) -> np.bool: ...  # type: ignore[overload-overlap]
@overload
def isposinf(x: CanArraySized[np.bool | np.integer | np.floating, _ShapeT], out: None = None) -> Array[np.bool, _ShapeT]: ...  # type: ignore[overload-overlap]
@overload
def isposinf(x: CoFloating_1ds, out: None = None) -> Array_1d[np.bool]: ...
@overload
def isposinf(x: CoFloating_2ds, out: None = None) -> Array_2d[np.bool]: ...
@overload
def isposinf(x: CoFloating_3ds, out: None = None) -> Array_3d[np.bool]: ...
@overload
def isposinf(x: CoFloating_1nd, out: None = None) -> Array[np.bool]: ...
@overload
def isposinf(x: CoFloating_nd, out: _ArrayT) -> _ArrayT: ...

#
@overload
def isneginf(x: CoFloating_0d, out: None = None) -> np.bool: ...  # type: ignore[overload-overlap]
@overload
def isneginf(x: CanArraySized[np.bool | np.integer | np.floating, _ShapeT], out: None = None) -> Array[np.bool, _ShapeT]: ...  # type: ignore[overload-overlap]
@overload
def isneginf(x: CoFloating_1ds, out: None = None) -> Array_1d[np.bool]: ...
@overload
def isneginf(x: CoFloating_2ds, out: None = None) -> Array_2d[np.bool]: ...
@overload
def isneginf(x: CoFloating_3ds, out: None = None) -> Array_3d[np.bool]: ...
@overload
def isneginf(x: CoFloating_1nd, out: None = None) -> Array[np.bool]: ...
@overload
def isneginf(x: CoFloating_nd, out: _ArrayT) -> _ArrayT: ...
