from collections.abc import Callable, Sequence
from typing import (
    Any,
    Literal as L,
    Protocol,
    SupportsIndex as CanIndex,
    SupportsInt,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import LiteralString, Self, TypeVar

import numpy as np
import numpy.typing as npt
from _numtype import (
    Array,
    Array_1d,
    Array_2d,
    CoComplex128_0d,
    CoComplex_0d,
    CoComplex_1d,
    CoComplex_1nd,
    CoComplex_nd,
    CoFloat64_0d,
    CoFloating_0d,
    CoFloating_1d,
    CoFloating_1nd,
    CoFloating_nd,
    CoIntP_0d,
    CoInteger_0d,
    CoInteger_1d,
    CoInteger_nd,
    ToComplex128_0d,
    ToComplex_0d,
    ToComplex_1d,
    ToComplex_1nd,
    ToComplex_nd,
    ToFloat64_0d,
    ToFloat64_nd,
    ToFloating_1d,
    ToFloating_nd,
    ToObject_1d,
    ToObject_1nd,
    ToObject_nd,
    ToReal_1d,
    _ToArray_1d,
    _ToArray_nd,
)
from numpy._typing import _NestedSequence, _NumberLike_co

_T = TypeVar("_T")
_T_contra = TypeVar("_T_contra", contravariant=True, default=Any)
_CoefT = TypeVar("_CoefT", bound=np.number | np.bool | np.object_)
_NameT_co = TypeVar("_NameT_co", bound=str, default=LiteralString, covariant=True)

# compatible with e.g. int, float, complex, Decimal, Fraction, and ABCPolyBase
@type_check_only
class _SupportsCoefOps(Protocol[_T_contra]):
    def __eq__(self, x: object, /) -> bool: ...
    def __ne__(self, x: object, /) -> bool: ...
    def __neg__(self, /) -> Self: ...
    def __pos__(self, /) -> Self: ...
    def __add__(self, x: _T_contra, /) -> Self: ...
    def __sub__(self, x: _T_contra, /) -> Self: ...
    def __mul__(self, x: _T_contra, /) -> Self: ...
    def __pow__(self, x: _T_contra, /) -> Self | float: ...
    def __radd__(self, x: _T_contra, /) -> Self: ...
    def __rsub__(self, x: _T_contra, /) -> Self: ...
    def __rmul__(self, x: _T_contra, /) -> Self: ...

_Tuple2: TypeAlias = tuple[_T, _T]
_ToInt: TypeAlias = SupportsInt | CanIndex

_InexactObject_1d: TypeAlias = Array_1d[np.inexact | np.object_]
_InexactObject_nd: TypeAlias = Array[np.inexact | np.object_]

_ToNumericObject_0d: TypeAlias = np.object_ | _SupportsCoefOps
_ToNumericObject_nd: TypeAlias = _ToNumericObject_0d | ToObject_1d | _NestedSequence[ToObject_1d]

_ToNumeric_0d: TypeAlias = _NumberLike_co | _ToNumericObject_0d
_ToNumeric_1d: TypeAlias = _ToArray_1d[np.number | np.bool | np.object_, complex | _SupportsCoefOps]
_ToNumeric_nd: TypeAlias = _ToArray_nd[np.number | np.bool | np.object_, complex | _SupportsCoefOps]

_ToValF: TypeAlias = Callable[[Array[Any], Array[Any], bool], _ToNumeric_nd]
_ToVanderF: TypeAlias = Callable[[Array[Any], int], _ToNumericObject_nd]

@type_check_only
class _HasName(Protocol[_NameT_co]):
    @property
    def __name__(self, /) -> _NameT_co: ...

@type_check_only
class _FuncLine(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, off: CoIntP_0d, scl: CoIntP_0d) -> Array_1d[np.intp]: ...
    @overload
    def __call__(self, /, off: ToFloat64_0d, scl: CoFloat64_0d) -> Array_1d[np.float64]: ...
    @overload
    def __call__(self, /, off: CoFloat64_0d, scl: ToFloat64_0d) -> Array_1d[np.float64]: ...
    @overload
    def __call__(self, /, off: ToComplex128_0d, scl: CoComplex128_0d) -> Array_1d[np.complex128]: ...
    @overload
    def __call__(self, /, off: CoComplex128_0d, scl: ToComplex128_0d) -> Array_1d[np.complex128]: ...
    @overload
    def __call__(self, /, off: _CoefT, scl: _CoefT) -> Array_1d[_CoefT]: ...
    @overload
    def __call__(self, /, off: _SupportsCoefOps, scl: _SupportsCoefOps) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncFromRoots(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, roots: CoFloating_1d) -> Array_1d[np.floating]: ...
    @overload
    def __call__(self, /, roots: ToComplex_1d) -> Array_1d[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, roots: ToObject_1d) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncUnOp(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c: CoFloating_1d) -> Array_1d[np.floating]: ...
    @overload
    def __call__(self, /, c: ToComplex_1d) -> Array_1d[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c: ToObject_1d) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncPoly2Ortho(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, pol: CoFloating_1d) -> Array_1d[np.floating]: ...
    @overload
    def __call__(self, /, pol: ToComplex_1d) -> Array_1d[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, pol: ToObject_1d) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncPow(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c: CoFloating_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array_1d[np.floating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        c: ToComplex_1d,
        pow: CoInteger_0d,
        maxpower: CoInteger_0d | None = None,
    ) -> Array_1d[np.complexfloating]: ...
    @overload
    def __call__(self, /, c: ToObject_1d, pow: CoInteger_0d, maxpower: CoInteger_0d | None = None) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncBinOp(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c1: ToReal_1d, c2: CoFloating_1d) -> Array_1d[np.floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c1: CoFloating_1d, c2: ToReal_1d) -> Array_1d[np.floating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c1: ToComplex_1d, c2: CoComplex_1d) -> Array_1d[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c1: CoComplex_1d, c2: ToComplex_1d) -> Array_1d[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c1: ToObject_1d, c2: _ToNumeric_1d) -> Array_1d[np.object_]: ...
    @overload
    def __call__(self, /, c1: _ToNumeric_1d, c2: ToObject_1d) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncDer(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        c: ToFloat64_nd | CoInteger_nd,
        m: CanIndex = 1,
        scl: CoFloating_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.float64]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        c: ToFloating_nd,
        m: CanIndex = 1,
        scl: CoFloating_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.floating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        c: ToComplex_nd,
        m: CanIndex = 1,
        scl: CoComplex_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, /, c: ToObject_nd, m: CanIndex = 1, scl: _ToNumeric_0d = 1, axis: CanIndex = 0) -> Array[np.object_]: ...

@type_check_only
class _FuncInteg(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(
        self,
        /,
        c: CoFloating_nd,
        m: CanIndex = 1,
        k: CoFloating_0d | CoFloating_1d = ...,
        lbnd: CoFloating_0d = 0,
        scl: CoFloating_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.floating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        c: ToComplex_nd,
        m: CanIndex = 1,
        k: CoComplex_0d | CoComplex_1d = ...,
        lbnd: CoComplex_0d = 0,
        scl: CoComplex_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(
        self,
        /,
        c: CoComplex_nd,
        m: CanIndex = 1,
        *,
        k: ToComplex_0d | ToComplex_1d,
        lbnd: CoComplex_0d = 0,
        scl: CoComplex_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(
        self,
        /,
        c: ToObject_nd,
        m: CanIndex = 1,
        k: _ToNumeric_0d | _ToNumeric_1d = ...,
        lbnd: _ToNumeric_0d = 0,
        scl: _ToNumeric_0d = 1,
        axis: CanIndex = 0,
    ) -> Array[np.object_]: ...

@type_check_only
class _FuncValFromRoots(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_0d, r: CoFloating_0d, tensor: bool = True) -> np.floating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoFloating_1nd, r: CoFloating_nd, tensor: bool = True) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: CoFloating_nd, r: CoFloating_1nd, tensor: bool = True) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_0d, r: CoComplex_0d, tensor: bool = True) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, r: ToComplex_0d, tensor: bool = True) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToComplex_1nd, r: CoComplex_nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToComplex_nd, r: CoComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_1nd, r: ToComplex_nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, r: ToComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToObject_1nd, r: _ToNumeric_nd, tensor: bool = True) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, r: ToObject_1nd, tensor: bool = True) -> Array[np.object_]: ...

@type_check_only
class _FuncVal(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_0d, c: CoFloating_1d, tensor: bool = True) -> np.floating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToComplex_0d, c: CoComplex_1d, tensor: bool = True) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, c: ToComplex_1d, tensor: bool = True) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoFloating_1nd, c: CoFloating_1nd, tensor: bool = True) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_1nd, c: CoComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_1nd, c: ToComplex_1nd, tensor: bool = True) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToObject_1nd, c: _ToNumeric_nd, tensor: bool = True) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, c: ToObject_1nd, tensor: bool = True) -> Array[np.object_]: ...

@type_check_only
class _FuncVal2D(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_0d, y: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToComplex_0d, y: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, y: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, y: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoFloating_1nd, y: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: CoFloating_nd, y: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_1nd, y: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_1nd, y: ToComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_1nd, y: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, /, x: ToComplex_nd, y: CoComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, /, x: ToObject_1nd, y: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...

@type_check_only
class _FuncVal3D(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_0d, y: CoFloating_0d, z: CoFloating_0d, c: CoFloating_1d) -> np.floating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoFloating_1nd, y: CoFloating_nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: CoFloating_nd, y: CoFloating_1nd, z: CoFloating_nd, c: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: CoFloating_nd, y: CoFloating_nd, z: CoFloating_1nd, c: CoFloating_1nd) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, y: ToComplex_0d, z: CoComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, y: CoComplex_0d, z: ToComplex_0d, c: CoComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_0d, y: CoComplex_0d, z: CoComplex_0d, c: ToComplex_1d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: ToComplex_1nd, z: CoComplex_nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, /, x: CoComplex_nd, y: CoComplex_nd, z: ToComplex_1nd, c: CoComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_1nd, y: CoComplex_nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: CoComplex_1nd, z: CoComplex_nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: CoComplex_nd, z: CoComplex_1nd, c: ToComplex_1nd) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToObject_1nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: ToObject_1nd, y: ToObject_1nd, z: _ToNumeric_nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: _ToNumeric_nd, z: ToObject_1nd, c: _ToNumeric_nd) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, c: ToObject_1nd) -> Array[np.object_]: ...

@type_check_only
class _FuncValND(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, val_f: _ToValF, c: CoFloating_1d, arg0: CoFloating_0d, /, *args: CoFloating_0d) -> np.floating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, val_f: _ToValF, c: ToComplex_1d, arg0: CoComplex_0d, /, *args: CoComplex_0d) -> np.complexfloating: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(
        self,
        val_f: _ToValF,
        c: CoFloating_1nd,
        arg0: CoFloating_1nd,
        /,
        *args: CoFloating_nd,
    ) -> Array[np.floating]: ...
    @overload
    def __call__(
        self,
        val_f: _ToValF,
        c: ToComplex_1nd,
        arg0: CoComplex_1nd,
        /,
        *args: CoComplex_nd,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, val_f: _ToValF, c: ToObject_1nd, /, *args: _ToNumeric_nd) -> Any: ...

@type_check_only
class _FuncVander(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_nd, deg: CanIndex) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_nd, deg: CanIndex) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToObject_nd, deg: CanIndex) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: npt.ArrayLike, deg: CanIndex) -> Array[Any]: ...

_Indices: TypeAlias = Sequence[CanIndex]

@type_check_only
class _FuncVander2D(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, x: CoFloating_nd, y: CoFloating_nd, deg: _Indices) -> Array[np.floating]: ...
    @overload
    def __call__(self, /, x: ToComplex_nd, y: CoComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: CoComplex_nd, y: ToComplex_nd, deg: _Indices) -> Array[np.complexfloating]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, x: ToObject_nd, y: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: ToObject_nd, deg: _Indices) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: npt.ArrayLike, y: npt.ArrayLike, deg: _Indices) -> Array[Any]: ...

@type_check_only
class _FuncVander3D(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(
        self,
        /,
        x: CoFloating_nd,
        y: CoFloating_nd,
        z: CoFloating_nd,
        deg: _Indices,
    ) -> Array[np.floating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: ToComplex_nd,
        y: CoComplex_nd,
        z: CoComplex_nd,
        deg: _Indices,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: CoComplex_nd,
        y: ToComplex_nd,
        z: CoComplex_nd,
        deg: _Indices,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: CoComplex_nd,
        y: CoComplex_nd,
        z: ToComplex_nd,
        deg: _Indices,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(self, /, x: ToObject_nd, y: _ToNumeric_nd, z: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: ToObject_nd, z: _ToNumeric_nd, deg: _Indices) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: _ToNumeric_nd, y: _ToNumeric_nd, z: ToObject_nd, deg: _Indices) -> Array[np.object_]: ...
    @overload
    def __call__(self, /, x: npt.ArrayLike, y: npt.ArrayLike, z: npt.ArrayLike, deg: _Indices) -> Array[Any]: ...

# keep in sync with the broadest overload of `._FuncVander`

@type_check_only
class _FuncVanderND(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(
        self,
        /,
        vander_fs: Sequence[_ToVanderF],
        points: Sequence[CoFloating_nd],
        degrees: Sequence[CanIndex],
    ) -> Array[np.floating]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        vander_fs: Sequence[_ToVanderF],
        points: Sequence[ToComplex_nd],
        degrees: Sequence[CanIndex],
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(
        self,
        /,
        vander_fs: Sequence[_ToVanderF],
        points: Sequence[ToObject_nd],
        degrees: Sequence[CanIndex],
    ) -> Array[np.object_]: ...
    @overload
    def __call__(
        self,
        /,
        vander_fs: Sequence[_ToVanderF],
        points: Sequence[npt.ArrayLike],
        degrees: Sequence[CanIndex],
    ) -> Array[Any]: ...

_FullFitResult: TypeAlias = Sequence[np.inexact | np.int32]

@type_check_only
class _FuncFit(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: ToFloating_1d,
        y: CoFloating_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        full: L[False] = False,
        w: ToFloating_1d | None = None,
    ) -> Array[np.floating]: ...
    @overload
    def __call__(
        self,
        /,
        x: ToFloating_1d,
        y: CoFloating_nd,
        deg: int | CoInteger_1d,
        rcond: float | None,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.floating], _FullFitResult]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: ToFloating_1d,
        y: CoFloating_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        *,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.floating], _FullFitResult]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: ToComplex_1d,
        y: CoComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        full: L[False] = False,
        w: ToFloating_1d | None = None,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(
        self,
        /,
        x: CoComplex_1d,
        y: ToComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        full: L[False] = False,
        w: ToFloating_1d | None = None,
    ) -> Array[np.complexfloating]: ...
    @overload
    def __call__(
        self,
        /,
        x: ToComplex_1d,
        y: CoComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.complexfloating], _FullFitResult]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: CoComplex_1d,
        y: ToComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.complexfloating], _FullFitResult]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: CoComplex_1d,
        y: ToComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        *,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.complexfloating], _FullFitResult]: ...
    @overload
    def __call__(  # type: ignore[overload-overlap]
        self,
        /,
        x: ToComplex_1d,
        y: CoComplex_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        *,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.complexfloating], _FullFitResult]: ...
    @overload
    def __call__(
        self,
        /,
        x: ToObject_1d,
        y: _ToNumeric_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        full: L[False] = False,
        w: ToFloating_1d | None = None,
    ) -> Array[np.object_]: ...
    @overload
    def __call__(
        self,
        /,
        x: _ToNumeric_1d,
        y: ToObject_nd,
        deg: int | CoInteger_1d,
        rcond: float | None,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.object_], _FullFitResult]: ...
    @overload
    def __call__(
        self,
        /,
        x: ToObject_1d,
        y: _ToNumeric_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        *,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.object_], _FullFitResult]: ...
    @overload
    def __call__(
        self,
        /,
        x: _ToNumeric_1d,
        y: ToObject_nd,
        deg: int | CoInteger_1d,
        rcond: float | None = None,
        *,
        full: L[True],
        w: ToFloating_1d | None = None,
    ) -> tuple[Array[np.object_], _FullFitResult]: ...

@type_check_only
class _FuncRoots(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c: CoFloating_1d) -> Array_1d[np.float64]: ...
    @overload
    def __call__(self, /, c: ToComplex_1d) -> Array_1d[np.complex128]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c: ToObject_1d) -> Array_1d[np.object_]: ...

@type_check_only
class _FuncCompanion(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c: CoFloating_1d) -> Array_2d[np.float64]: ...
    @overload
    def __call__(self, /, c: ToComplex_1d) -> Array_2d[np.complex128]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c: ToObject_1d) -> Array_2d[np.object_]: ...

@type_check_only
class _FuncGauss(_HasName[_NameT_co], Protocol[_NameT_co]):
    def __call__(self, /, deg: CanIndex) -> _Tuple2[Array_1d[np.float64]]: ...

@type_check_only
class _FuncWeight(_HasName[_NameT_co], Protocol[_NameT_co]):
    @overload
    def __call__(self, /, c: CoFloating_nd) -> Array[np.float64]: ...
    @overload
    def __call__(self, /, c: ToComplex_nd) -> Array[np.complex128]: ...  # type: ignore[overload-overlap]
    @overload
    def __call__(self, /, c: ToObject_nd) -> Array[np.object_]: ...

@type_check_only
class _FuncPts(_HasName[_NameT_co], Protocol[_NameT_co]):
    def __call__(self, /, npts: _ToInt) -> Array_1d[np.float64]: ...
