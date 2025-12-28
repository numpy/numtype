from _typeshed import Incomplete, StrOrBytesPath, SupportsWrite
from typing import (
    Any,
    ClassVar,
    Final,
    Generic,
    Literal as L,
    Protocol,
    Self,
    SupportsIndex,
    TypeAlias,
    overload,
    type_check_only,
)
from typing_extensions import TypeVar, override

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy import _OrderKACF  # noqa: ICN003
from numpy._typing import _DTypeLike, _ShapeLike

__all__ = ["memmap"]

###

_ShapeT_co = TypeVar("_ShapeT_co", bound=_nt.Shape, default=_nt.AnyShape, covariant=True)
_DTypeT_co = TypeVar("_DTypeT_co", bound=np.dtype[Any], default=np.dtype[Any], covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic[Any])

_Mode: TypeAlias = L["r", "c", "r+", "w+"]
_ToMode: TypeAlias = L["readonly", "r", "copyonwrite", "c", "readwrite", "r+", "write", "w+"]
_ToFileName: TypeAlias = StrOrBytesPath | _SupportsFileMethodsRW

@type_check_only
class _SupportsFileMethodsRW(SupportsWrite[bytes], Protocol):
    def fileno(self, /) -> SupportsIndex: ...
    def tell(self, /) -> SupportsIndex: ...
    def seek(self, offset: int, whence: int, /) -> object: ...

###

class memmap(np.ndarray[_ShapeT_co, _DTypeT_co], Generic[_ShapeT_co, _DTypeT_co]):
    __array_priority__: ClassVar[float] = -100.0  # pyright: ignore[reportIncompatibleMethodOverride]

    filename: Final[str | None]
    offset: Final[int]
    mode: Final[_Mode]

    @overload
    def __new__(
        subtype,
        filename: _ToFileName,
        dtype: type[np.uint8] = ...,
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: int | tuple[int, ...] | None = None,
        order: _OrderKACF = "C",
    ) -> memmap[Incomplete, np.dtype[np.uint8]]: ...
    @overload
    def __new__(
        subtype,
        filename: _ToFileName,
        dtype: _DTypeT_co,
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: _ShapeLike | None = None,
        order: _OrderKACF = "C",
    ) -> memmap[Incomplete, _DTypeT_co]: ...
    @overload
    def __new__(
        subtype,
        filename: _ToFileName,
        dtype: _DTypeLike[_ScalarT],
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: _ShapeLike | None = None,
        order: _OrderKACF = "C",
    ) -> memmap[Incomplete, np.dtype[_ScalarT]]: ...
    @overload
    def __new__(
        subtype,
        filename: _ToFileName,
        dtype: npt.DTypeLike | None,
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: int | tuple[int, ...] | None = None,
        order: _OrderKACF = "C",
    ) -> Self: ...

    #
    @override
    def __array_wrap__(  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        array: memmap[_ShapeT_co, _DTypeT_co],  # type: ignore[override]
        context: tuple[np.ufunc, tuple[Any, ...], int] | None = None,
        return_scalar: bool = False,
    ) -> Any: ...

    #
    def flush(self) -> None: ...
