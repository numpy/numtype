from _typeshed import Incomplete
from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Literal, TypeAlias, overload
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np
import numpy.typing as npt
from numpy._typing import _DTypeLike, _DTypeLikeVoid
from numpy.ma.mrecords import MaskedRecords

__all__ = [
    "append_fields",
    "apply_along_fields",
    "assign_fields_by_name",
    "drop_fields",
    "find_duplicates",
    "flatten_descr",
    "get_fieldstructure",
    "get_names",
    "get_names_flat",
    "join_by",
    "merge_arrays",
    "rec_append_fields",
    "rec_drop_fields",
    "rec_join",
    "recursive_fill_fields",
    "rename_fields",
    "repack_fields",
    "require_fields",
    "stack_arrays",
    "structured_to_unstructured",
    "unstructured_to_structured",
]

###

_T = TypeVar("_T")
_ShapeT = TypeVar("_ShapeT", bound=_nt.Shape)
_ScalarT = TypeVar("_ScalarT", bound=np.generic)
_DTypeT = TypeVar("_DTypeT", bound=np.dtype)
_ArrayT = TypeVar("_ArrayT", bound=_nt.Array)
_VoidArrayT = TypeVar("_VoidArrayT", bound=_nt.Array[np.void])
_NonVoidDTypeT = TypeVar("_NonVoidDTypeT", bound=_NonVoidDType)

_OneOrMany: TypeAlias = _T | Iterable[_T]
_BuiltinSequence: TypeAlias = tuple[_T, ...] | list[_T]

_NestedNames: TypeAlias = tuple[str | _NestedNames, ...]
_NonVoid: TypeAlias = np.bool | np.number | np.character | np.datetime64 | np.timedelta64 | np.object_
_NonVoidDType: TypeAlias = np.dtype[_NonVoid] | np.dtypes.StringDType

_JoinType: TypeAlias = Literal["inner", "outer", "leftouter"]

###

def recursive_fill_fields(input: _nt.Array[np.void], output: _VoidArrayT) -> _VoidArrayT: ...

#
def get_names(adtype: np.dtype[np.void]) -> _NestedNames: ...
def get_names_flat(adtype: np.dtype[np.void]) -> tuple[str, ...]: ...

#
@overload
def flatten_descr(ndtype: _NonVoidDTypeT) -> tuple[tuple[Literal[""], _NonVoidDTypeT]]: ...
@overload
def flatten_descr(ndtype: np.dtype[np.void]) -> tuple[tuple[str, np.dtype]]: ...

#
def get_fieldstructure(
    adtype: np.dtype[np.void],
    lastname: str | None = None,
    parents: dict[str, list[str]] | None = None,
) -> dict[str, list[str]]: ...

#
@overload
def merge_arrays(
    seqarrays: Sequence[_nt.Array[Any, _ShapeT]] | _nt.Array[Any, _ShapeT],
    fill_value: float = -1,
    flatten: bool = False,
    usemask: bool = False,
    asrecarray: bool = False,
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...
@overload
def merge_arrays(
    seqarrays: Sequence[npt.ArrayLike] | np.void,
    fill_value: float = -1,
    flatten: bool = False,
    usemask: bool = False,
    asrecarray: bool = False,
) -> np.recarray[Any, np.dtype[np.void]]: ...

#
@overload
def drop_fields(
    base: _nt.Array[np.void, _ShapeT],
    drop_names: str | Iterable[str],
    usemask: bool = True,
    asrecarray: Literal[False] = False,
) -> _nt.Array[np.void, _ShapeT]: ...
@overload
def drop_fields(
    base: _nt.Array[np.void, _ShapeT],
    drop_names: str | Iterable[str],
    usemask: bool,
    asrecarray: Literal[True],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...
@overload
def drop_fields(
    base: _nt.Array[np.void, _ShapeT],
    drop_names: str | Iterable[str],
    usemask: bool = True,
    *,
    asrecarray: Literal[True],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...

#
@overload
def rename_fields(
    base: MaskedRecords[_ShapeT, np.dtype[np.void]],
    namemapper: Mapping[str, str],
) -> MaskedRecords[_ShapeT, np.dtype[np.void]]: ...
@overload
def rename_fields(
    base: _nt.MArray[np.void, _ShapeT],
    namemapper: Mapping[str, str],
) -> _nt.MArray[np.void, _ShapeT]: ...
@overload
def rename_fields(
    base: np.recarray[_ShapeT, np.dtype[np.void]],
    namemapper: Mapping[str, str],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...
@overload
def rename_fields(
    base: _nt.Array[np.void, _ShapeT],
    namemapper: Mapping[str, str],
) -> _nt.Array[np.void, _ShapeT]: ...

#
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None,
    fill_value: int,
    usemask: Literal[False],
    asrecarray: Literal[False] = False,
) -> _nt.Array[np.void, _ShapeT]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None = None,
    fill_value: int = -1,
    *,
    usemask: Literal[False],
    asrecarray: Literal[False] = False,
) -> _nt.Array[np.void, _ShapeT]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None,
    fill_value: int,
    usemask: Literal[False],
    asrecarray: Literal[True],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None = None,
    fill_value: int = -1,
    *,
    usemask: Literal[False],
    asrecarray: Literal[True],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None = None,
    fill_value: int = -1,
    usemask: Literal[True] = True,
    asrecarray: Literal[False] = False,
) -> _nt.MArray[np.void, _ShapeT]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None,
    fill_value: int,
    usemask: Literal[True],
    asrecarray: Literal[True],
) -> MaskedRecords[_ShapeT, np.dtype[np.void]]: ...
@overload
def append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None = None,
    fill_value: int = -1,
    usemask: Literal[True] = True,
    *,
    asrecarray: Literal[True],
) -> MaskedRecords[_ShapeT, np.dtype[np.void]]: ...

#
def rec_drop_fields(
    base: _nt.Array[np.void, _ShapeT],
    drop_names: str | Iterable[str],
) -> np.recarray[_ShapeT, np.dtype[np.void]]: ...

#
def rec_append_fields(
    base: _nt.Array[np.void, _ShapeT],
    names: _OneOrMany[str],
    data: _OneOrMany[_nt.Array],
    dtypes: _BuiltinSequence[np.dtype] | None = None,
) -> _nt.MArray[np.void, _ShapeT]: ...

# TODO(jorenham): Stop passing `void` directly once structured dtypes are implemented,
# e.g. using a `TypeVar` with constraints.
# https://github.com/numpy/numtype/issues/92
@overload
def repack_fields(a: _DTypeT, align: bool = False, recurse: bool = False) -> _DTypeT: ...
@overload
def repack_fields(a: _ScalarT, align: bool = False, recurse: bool = False) -> _ScalarT: ...
@overload
def repack_fields(a: _ArrayT, align: bool = False, recurse: bool = False) -> _ArrayT: ...

# TODO(jorenham): Attempt shape-typing (return type has ndim == arr.ndim + 1)
@overload
def structured_to_unstructured(
    arr: _nt.Array[np.void],
    dtype: _DTypeLike[_ScalarT],
    copy: bool = False,
    casting: np._CastingKind = "unsafe",
) -> _nt.Array[_ScalarT]: ...
@overload
def structured_to_unstructured(
    arr: _nt.Array[np.void],
    dtype: npt.DTypeLike | None = None,
    copy: bool = False,
    casting: np._CastingKind = "unsafe",
) -> _nt.Array: ...

#
@overload
def unstructured_to_structured(
    arr: _nt.Array,
    dtype: npt.DTypeLike,
    names: None = None,
    align: bool = False,
    copy: bool = False,
    casting: str = "unsafe",
) -> _nt.Array[np.void]: ...
@overload
def unstructured_to_structured(
    arr: _nt.Array,
    dtype: None,
    names: _OneOrMany[str],
    align: bool = False,
    copy: bool = False,
    casting: str = "unsafe",
) -> _nt.Array[np.void]: ...
@overload
def unstructured_to_structured(
    arr: _nt.Array,
    dtype: None = None,
    *,
    names: _OneOrMany[str],
    align: bool = False,
    copy: bool = False,
    casting: str = "unsafe",
) -> _nt.Array[np.void]: ...

#
def apply_along_fields(
    func: Callable[[_nt.Array[Any, _ShapeT]], _nt.Array],
    arr: _nt.Array[np.void, _ShapeT],
) -> _nt.Array[np.void, _ShapeT]: ...

#
def assign_fields_by_name(dst: _nt.Array[np.void], src: _nt.Array[np.void], zero_unassigned: bool = True) -> None: ...

#
def require_fields(
    array: _nt.Array[np.void, _ShapeT],
    required_dtype: _DTypeLikeVoid,
) -> _nt.Array[np.void, _ShapeT]: ...

# TODO(jorenham): Attempt shape-typing
@overload
def stack_arrays(
    arrays: _ArrayT,
    defaults: Mapping[str, object] | None = None,
    usemask: bool = True,
    asrecarray: bool = False,
    autoconvert: bool = False,
) -> _ArrayT: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None,
    usemask: Literal[False],
    asrecarray: Literal[False] = False,
    autoconvert: bool = False,
) -> _nt.Array[np.void]: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None = None,
    *,
    usemask: Literal[False],
    asrecarray: Literal[False] = False,
    autoconvert: bool = False,
) -> _nt.Array[np.void]: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None = None,
    usemask: Literal[True] = True,
    asrecarray: Literal[False] = False,
    autoconvert: bool = False,
) -> _nt.MArray[np.void]: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None = None,
    *,
    usemask: Literal[False],
    asrecarray: Literal[True],
    autoconvert: bool = False,
) -> np.recarray[_nt.Shape, np.dtype[np.void]]: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None,
    usemask: Literal[True],
    asrecarray: Literal[True],
    autoconvert: bool = False,
) -> MaskedRecords[_nt.Shape, np.dtype[np.void]]: ...
@overload
def stack_arrays(
    arrays: Sequence[_nt.Array],
    defaults: Mapping[str, Incomplete] | None = None,
    usemask: Literal[True] = True,
    *,
    asrecarray: Literal[True],
    autoconvert: bool = False,
) -> MaskedRecords[_nt.Shape, np.dtype[np.void]]: ...

#
@overload
def find_duplicates(
    a: _nt.MArray[np.void, _ShapeT],
    key: str | None = None,
    ignoremask: bool = True,
    return_index: Literal[False] = False,
) -> _nt.MArray[np.void, _ShapeT]: ...
@overload
def find_duplicates(
    a: _nt.MArray[np.void, _ShapeT],
    key: str | None,
    ignoremask: bool,
    return_index: Literal[True],
) -> tuple[_nt.MArray[np.void, _ShapeT], _nt.Array[np.intp, _ShapeT]]: ...
@overload
def find_duplicates(
    a: _nt.MArray[np.void, _ShapeT],
    key: str | None = None,
    ignoremask: bool = True,
    *,
    return_index: Literal[True],
) -> tuple[_nt.MArray[np.void, _ShapeT], _nt.Array[np.intp, _ShapeT]]: ...

#
@overload
def join_by(
    key: str | Sequence[str],
    r1: _nt.Array[np.void],
    r2: _nt.Array[np.void],
    jointype: _JoinType = "inner",
    r1postfix: str = "1",
    r2postfix: str = "2",
    defaults: Mapping[str, object] | None = None,
    *,
    usemask: Literal[False],
    asrecarray: Literal[False] = False,
) -> _nt.Array1D[np.void]: ...
@overload
def join_by(
    key: str | Sequence[str],
    r1: _nt.Array[np.void],
    r2: _nt.Array[np.void],
    jointype: _JoinType = "inner",
    r1postfix: str = "1",
    r2postfix: str = "2",
    defaults: Mapping[str, object] | None = None,
    usemask: Literal[True] = True,
    asrecarray: Literal[False] = False,
) -> _nt.MArray1D[np.void]: ...
@overload
def join_by(
    key: str | Sequence[str],
    r1: _nt.Array[np.void],
    r2: _nt.Array[np.void],
    jointype: _JoinType = "inner",
    r1postfix: str = "1",
    r2postfix: str = "2",
    defaults: Mapping[str, object] | None = None,
    *,
    usemask: Literal[False],
    asrecarray: Literal[True],
) -> np.recarray[_nt.Rank1, np.dtype[np.void]]: ...
@overload
def join_by(
    key: str | Sequence[str],
    r1: _nt.Array[np.void],
    r2: _nt.Array[np.void],
    jointype: _JoinType = "inner",
    r1postfix: str = "1",
    r2postfix: str = "2",
    defaults: Mapping[str, object] | None = None,
    usemask: Literal[True] = True,
    *,
    asrecarray: Literal[True],
) -> MaskedRecords[_nt.Rank1, np.dtype[np.void]]: ...

#
def rec_join(
    key: str | Sequence[str],
    r1: _nt.Array[np.void],
    r2: _nt.Array[np.void],
    jointype: _JoinType = "inner",
    r1postfix: str = "1",
    r2postfix: str = "2",
    defaults: Mapping[str, object] | None = None,
) -> np.recarray[_nt.Rank1, np.dtype[np.void]]: ...
