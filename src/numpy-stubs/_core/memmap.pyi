from _typeshed import Incomplete, StrOrBytesPath, SupportsWrite
from typing import Any, ClassVar, Final, Generic, Literal as L, Protocol, SupportsIndex, TypeAlias, overload, type_check_only
from typing_extensions import Self, TypeVar

import numpy as np
import numpy.typing as npt
from numpy import _OrderKACF  # noqa: ICN003
from numpy._typing import _DTypeLike, _ShapeLike

__all__ = ["memmap"]

###

_ShapeT_co = TypeVar("_ShapeT_co", bound=tuple[int, ...], default=Any, covariant=True)
_DType_co = TypeVar("_DType_co", bound=np.dtype, default=np.dtype, covariant=True)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_Mode: TypeAlias = L["r", "c", "r+", "w+"]
_ToMode: TypeAlias = L["readonly", "r", "copyonwrite", "c", "readwrite", "r+", "write", "w+"]
_ToFileName: TypeAlias = StrOrBytesPath | _SupportsFileMethodsRW

@type_check_only
class _SupportsFileMethodsRW(SupportsWrite[bytes], Protocol):
    def fileno(self, /) -> SupportsIndex: ...
    def tell(self, /) -> SupportsIndex: ...
    def seek(self, offset: int, whence: int, /) -> object: ...

###

class memmap(np.ndarray[_ShapeT_co, _DType_co], Generic[_ShapeT_co, _DType_co]):
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
        dtype: _DType_co,
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: _ShapeLike | None = None,
        order: _OrderKACF = "C",
    ) -> memmap[Incomplete, _DType_co]: ...
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
        dtype: npt.DTypeLike,
        mode: _ToMode = "r+",
        offset: int = 0,
        shape: int | tuple[int, ...] | None = None,
        order: _OrderKACF = "C",
    ) -> Self: ...

    #
    def flush(self) -> None: ...
