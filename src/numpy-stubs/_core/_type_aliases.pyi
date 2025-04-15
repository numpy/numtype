from collections.abc import Collection
from typing import Final, Literal as L, TypeAlias, TypedDict, type_check_only

import numpy as np

###

@type_check_only
class _CNamesDict(TypedDict):
    BOOL: np.dtypes.BoolDType
    BYTE: np.dtypes.ByteDType
    UBYTE: np.dtypes.UByteDType
    SHORT: np.dtypes.ShortDType
    USHORT: np.dtypes.UShortDType
    INT: np.dtypes.IntDType
    UINT: np.dtypes.UIntDType
    LONG: np.dtypes.LongDType
    ULONG: np.dtypes.ULongDType
    LONGLONG: np.dtypes.LongLongDType
    ULONGLONG: np.dtypes.ULongLongDType
    HALF: np.dtypes.Float16DType
    FLOAT: np.dtypes.Float32DType
    DOUBLE: np.dtypes.Float64DType
    LONGDOUBLE: np.dtypes.LongDoubleDType
    CFLOAT: np.dtypes.Complex64DType
    CDOUBLE: np.dtypes.Complex128DType
    CLONGDOUBLE: np.dtypes.CLongDoubleDType
    STRING: np.dtypes.BytesDType
    UNICODE: np.dtypes.StrDType
    VOID: np.dtypes.VoidDType
    OBJECT: np.dtypes.ObjectDType
    DATETIME: np.dtypes.DateTime64DType
    TIMEDELTA: np.dtypes.TimeDelta64DType

_AbstractTypeName: TypeAlias = L[
    "generic",
    "flexible",
    "character",
    "number",
    "integer",
    "inexact",
    "unsignedinteger",
    "signedinteger",
    "floating",
    "complexfloating",
]

@type_check_only
class _AliasesType(TypedDict):
    double: L["float64"]
    cdouble: L["complex128"]
    single: L["float32"]
    csingle: L["complex64"]
    half: L["float16"]
    bool_: L["bool"]
    int_: L["intp"]
    uint: L["intp"]

@type_check_only
class _ExtraAliasesType(TypedDict):
    float: L["float64"]
    complex: L["complex128"]
    object: L["object_"]
    bytes: L["bytes_"]
    a: L["bytes_"]
    int: L["int_"]
    str: L["str_"]
    unicode: L["str_"]

@type_check_only
class _SCTypes(TypedDict):
    int: Collection[type[np.signedinteger]]
    uint: Collection[type[np.unsignedinteger]]
    float: Collection[type[np.floating]]
    complex: Collection[type[np.complexfloating]]
    others: Collection[type[np.flexible | np.bool | np.object_]]

###

sctypeDict: Final[dict[str, type[np.generic]]] = ...
allTypes: Final[dict[str, type[np.generic]]] = ...
c_names_dict: Final[_CNamesDict] = ...
sctypes: Final[_SCTypes] = ...

_abstract_type_names: Final[set[_AbstractTypeName]] = ...
_aliases: Final[_AliasesType] = ...
_extra_aliases: Final[_ExtraAliasesType] = ...

# namespace pollution
k: str
v: str
is_complex: bool
full_name: str
longdouble_type: type[np.longdouble | np.clongdouble]
bits: int
base_name: str
extended_prec_name: str
type_info: np.dtype
type_group: str
concrete_type: type[np.generic]
abstract_type: type[np.generic]
sctype_key: str
sctype_list: list[type[np.generic]]
