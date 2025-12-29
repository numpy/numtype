import io
import os
from _typeshed import SupportsRead, SupportsWrite
from collections.abc import Mapping, Sequence
from typing import Any, Final, Literal as L, TypeAlias, TypeGuard, TypedDict, overload, type_check_only
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
from numpy import _AnyShapeT, _DTypeDescr  # noqa: ICN003
from numpy._typing import DTypeLike, _DTypeLike

from ._utils_impl import drop_metadata as drop_metadata

__all__: list[str] = []

###

_ScalarT = TypeVar("_ScalarT", bound=np.generic)

_ToDescr: TypeAlias = str | Sequence[tuple[str, str] | tuple[str, str, tuple[int, ...]]]
_HeaderVersion: TypeAlias = tuple[L[1, 2, 3], L[0]]
_MemmapMode: TypeAlias = L["r", "c", "r+", "w+"]
_ArrayHeader: TypeAlias = tuple[tuple[int, ...], bool, np.dtype]

@type_check_only
class _HeaderDict_1_0(TypedDict):
    shape: _nt.Shape
    fortran_order: bool
    descr: _DTypeDescr

###

EXPECTED_KEYS: Final[set[str]] = ...
MAGIC_PREFIX: Final = b"\x93NUMPY"
MAGIC_LEN: Final = 16
ARRAY_ALIGN: Final = 64
BUFFER_SIZE: Final = 262_144  # 2**18
GROWTH_AXIS_MAX_DIGITS: Final = 21
_MAX_HEADER_SIZE: Final = 10_000

#
def _check_version(version: _HeaderVersion | None) -> None: ...
def _filter_header(s: str) -> str: ...
def _wrap_header(header: str, version: _HeaderVersion) -> bytes: ...
def _wrap_header_guess_version(header: str) -> bytes: ...
def _read_bytes(fp: SupportsRead[bytes], size: int, error_template: str = "ran out of data") -> bytes: ...

# NOTE: Don't use `TypeIs` here: It might still be of this IO type if `False` is returned
def isfileobj(f: object) -> TypeGuard[io.FileIO | io.BufferedReader | io.BufferedWriter]: ...

#
def magic(major: int, minor: int) -> bytes: ...
def read_magic(fp: SupportsRead[bytes]) -> tuple[int, int]: ...

#
def dtype_to_descr(dtype: np.dtype) -> _DTypeDescr | str: ...
def descr_to_dtype(descr: _ToDescr) -> np.dtype: ...

#
@overload  # known dtype, known shape (positional)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode,
    dtype: _DTypeLike[_ScalarT],
    shape: _AnyShapeT,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    *,
    max_header_size: int = 10_000,
) -> np.memmap[_AnyShapeT, np.dtype[_ScalarT]]: ...
@overload  # known dtype, known shape (keyword)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode = "r+",
    *,
    dtype: _DTypeLike[_ScalarT],
    shape: _AnyShapeT,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    max_header_size: int = 10_000,
) -> np.memmap[_AnyShapeT, np.dtype[_ScalarT]]: ...
@overload  # unknown dtype, known shape (positional)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode,
    dtype: DTypeLike | None,
    shape: _AnyShapeT,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    *,
    max_header_size: int = 10_000,
) -> np.memmap[_AnyShapeT, np.dtype]: ...
@overload  # unknown dtype, known shape (keyword)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode = "r+",
    dtype: DTypeLike | None = None,
    *,
    shape: _AnyShapeT,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    max_header_size: int = 10_000,
) -> np.memmap[_AnyShapeT, np.dtype]: ...
@overload  # known dtype, unknown shape (positional)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode,
    dtype: _DTypeLike[_ScalarT],
    shape: tuple[int, ...] | None = None,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    *,
    max_header_size: int = 10_000,
) -> np.memmap[_nt.AnyShape, np.dtype[_ScalarT]]: ...
@overload  # known dtype, unknown shape (keyword)
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode = "r+",
    *,
    dtype: _DTypeLike[_ScalarT],
    shape: tuple[int, ...] | None = None,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    max_header_size: int = 10_000,
) -> np.memmap[_nt.AnyShape, np.dtype[_ScalarT]]: ...
@overload  # unknown dtype, unknown shape
def open_memmap(
    filename: str | os.PathLike[str],
    mode: _MemmapMode = "r+",
    dtype: DTypeLike | None = None,
    shape: tuple[int, ...] | None = None,
    fortran_order: bool = False,
    version: _HeaderVersion | None = None,
    *,
    max_header_size: int = 10_000,
) -> np.memmap[_nt.AnyShape, np.dtype]: ...

#
def header_data_from_array_1_0(array: np.ndarray[Any, Any]) -> _HeaderDict_1_0: ...

#
def _read_array_header(
    fp: SupportsRead[bytes], version: _HeaderVersion, max_header_size: int = 10_000
) -> _ArrayHeader: ...
def read_array_header_1_0(fp: SupportsRead[bytes], max_header_size: int = 10_000) -> _ArrayHeader: ...
def read_array_header_2_0(fp: SupportsRead[bytes], max_header_size: int = 10_000) -> _ArrayHeader: ...
def read_array(
    fp: SupportsRead[bytes],
    allow_pickle: bool = False,
    pickle_kwargs: Mapping[str, object] | None = None,
    *,
    max_header_size: int = 10_000,
) -> np.ndarray: ...

#
def _write_array_header(
    fp: SupportsWrite[str], d: Mapping[str, str], version: _HeaderVersion | None = None
) -> None: ...
def write_array_header_1_0(fp: SupportsWrite[str], d: Mapping[str, str]) -> None: ...
def write_array_header_2_0(fp: SupportsWrite[str], d: Mapping[str, str]) -> None: ...
def write_array(
    fp: SupportsWrite[str],
    array: np.ndarray[Any, Any],
    version: _HeaderVersion | None = None,
    allow_pickle: bool = True,
    pickle_kwargs: Mapping[str, object] | None = None,
) -> None: ...
