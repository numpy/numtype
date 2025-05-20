from typing import Literal as L, TypeAlias, TypedDict, overload, type_check_only
from typing_extensions import TypeVar

import numpy as np

###

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")
_T3 = TypeVar("_T3")

_Permute1: TypeAlias = _T | tuple[_T]
_Permute2: TypeAlias = tuple[_T1, _T2] | tuple[_T2, _T1]
_Permute3: TypeAlias = (
    tuple[_T1, _T2, _T3]
    | tuple[_T1, _T3, _T2]
    | tuple[_T2, _T1, _T3]
    | tuple[_T2, _T3, _T1]
    | tuple[_T3, _T1, _T2]
    | tuple[_T3, _T2, _T1]
)
_Permute12: TypeAlias = _Permute1[_T] | _Permute2[_T1, _T2]
_Permute13: TypeAlias = _Permute1[_T] | _Permute3[_T1, _T2, _T3]

_Device: TypeAlias = L["cpu"]
_KindBool: TypeAlias = L["bool"]
_KindInt: TypeAlias = L["signed integer"]
_KindUInt: TypeAlias = L["unsigned integer"]
_KindInteger: TypeAlias = L["integral"]
_KindFloat: TypeAlias = L["real floating"]
_KindComplex: TypeAlias = L["complex floating"]
_KindNumber: TypeAlias = L["numeric"]
_Kind: TypeAlias = L[_KindBool, _KindInt, _KindUInt, _KindInteger, _KindFloat, _KindComplex, _KindNumber]

###

_Capabilities = TypedDict(
    "_Capabilities",
    {
        "boolean indexing": L[True],
        "data-dependent shapes": L[True],
        # 'max rank' will be part of the 2024.12 standard
        # "max rank": 64,
    },
)
_DefaultDTypes = TypedDict(
    "_DefaultDTypes",
    {
        "real floating": np.dtypes.Float64DType,
        "complex floating": np.dtypes.Complex128DType,
        "integral": np.dtype[np.int_],
        "indexing": np.dtype[np.intp],
    },
)

@type_check_only
class _DTypesBool(TypedDict):
    bool: np.dtypes.BoolDType

@type_check_only
class _DTypesInt(TypedDict):
    int8: np.dtypes.Int8DType
    int16: np.dtypes.Int16DType
    int32: np.dtypes.Int32DType
    int64: np.dtypes.Int64DType

@type_check_only
class _DTypesUInt(TypedDict):
    uint8: np.dtypes.UInt8DType
    uint16: np.dtypes.UInt16DType
    uint32: np.dtypes.UInt32DType
    uint64: np.dtypes.UInt64DType

@type_check_only
class _DTypesFloat(TypedDict):
    float32: np.dtypes.Float32DType
    float64: np.dtypes.Float64DType

@type_check_only
class _DTypesComplex(TypedDict):
    complex64: np.dtypes.Complex64DType
    complex128: np.dtypes.Complex128DType

@type_check_only
class _DTypesEmpty(TypedDict): ...

@type_check_only
class _DTypesInteger(_DTypesInt, _DTypesUInt): ...

@type_check_only
class _DTypesNumber(_DTypesInteger, _DTypesFloat, _DTypesComplex): ...

@type_check_only
class _DTypes(_DTypesBool, _DTypesNumber): ...

@type_check_only
class _DTypesUnion(TypedDict, total=False):
    bool: np.dtypes.BoolDType
    int8: np.dtypes.Int8DType
    int16: np.dtypes.Int16DType
    int32: np.dtypes.Int32DType
    int64: np.dtypes.Int64DType
    uint8: np.dtypes.UInt8DType
    uint16: np.dtypes.UInt16DType
    uint32: np.dtypes.UInt32DType
    uint64: np.dtypes.UInt64DType
    float32: np.dtypes.Float32DType
    float64: np.dtypes.Float64DType
    complex64: np.dtypes.Complex64DType
    complex128: np.dtypes.Complex128DType

###

class __array_namespace_info__:
    __module__: L["numpy"] = "numpy"

    def capabilities(self, /) -> _Capabilities: ...
    def devices(self, /) -> list[_Device]: ...
    def default_device(self, /) -> _Device: ...
    def default_dtypes(self, /, *, device: _Device | None = None) -> _DefaultDTypes: ...

    # the mypy errors are false positives
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: None = ...) -> _DTypes: ...
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: tuple[()]) -> _DTypesEmpty: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: _Permute1[_KindBool]) -> _DTypesBool: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: _Permute1[_KindInt]) -> _DTypesInt: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: _Permute1[_KindUInt]) -> _DTypesUInt: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: _Permute1[_KindFloat]) -> _DTypesFloat: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: _Permute1[_KindComplex]) -> _DTypesComplex: ...  # type: ignore[overload-overlap]
    @overload
    def dtypes(  # type: ignore[overload-overlap]
        self, /, *, device: _Device | None = None, kind: _Permute12[_KindInteger, _KindInt, _KindUInt]
    ) -> _DTypesInteger: ...
    @overload
    def dtypes(  # type: ignore[overload-overlap]
        self, /, *, device: _Device | None = None, kind: _Permute13[_KindNumber, _KindInteger, _KindFloat, _KindComplex]
    ) -> _DTypesNumber: ...
    @overload
    def dtypes(self, /, *, device: _Device | None = None, kind: tuple[_Kind, ...]) -> _DTypesUnion: ...
