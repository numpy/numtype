from typing import Literal, TypeAlias

_BoolCodes: TypeAlias = Literal["bool", "bool_", "?", "|?", "=?", "<?", ">?"]

_UInt8Codes: TypeAlias = Literal["uint8", "u1", "|u1", "=u1", "<u1", ">u1"]
_UInt16Codes: TypeAlias = Literal["uint16", "u2", "|u2", "=u2", "<u2", ">u2"]
_UInt32Codes: TypeAlias = Literal["uint32", "u4", "|u4", "=u4", "<u4", ">u4"]
_UInt64Codes: TypeAlias = Literal["uint64", "u8", "|u8", "=u8", "<u8", ">u8"]

_Int8Codes: TypeAlias = Literal["int8", "i1", "|i1", "=i1", "<i1", ">i1"]
_Int16Codes: TypeAlias = Literal["int16", "i2", "|i2", "=i2", "<i2", ">i2"]
_Int32Codes: TypeAlias = Literal["int32", "i4", "|i4", "=i4", "<i4", ">i4"]
_Int64Codes: TypeAlias = Literal["int64", "i8", "|i8", "=i8", "<i8", ">i8"]

_Float16Codes: TypeAlias = Literal["float16", "f2", "|f2", "=f2", "<f2", ">f2"]
_Float32Codes: TypeAlias = Literal["float32", "f4", "|f4", "=f4", "<f4", ">f4"]
_Float64Codes: TypeAlias = Literal["float64", "f8", "|f8", "=f8", "<f8", ">f8"]

_Complex64Codes: TypeAlias = Literal["complex64", "c8", "|c8", "=c8", "<c8", ">c8"]
_Complex128Codes: TypeAlias = Literal["complex128", "c16", "|c16", "=c16", "<c16", ">c16"]

_ByteCodes: TypeAlias = Literal["byte", "b", "|b", "=b", "<b", ">b"]
_ShortCodes: TypeAlias = Literal["short", "h", "|h", "=h", "<h", ">h"]
_IntCCodes: TypeAlias = Literal["intc", "i", "|i", "=i", "<i", ">i"]
_IntPCodes: TypeAlias = Literal["intp", "int", "int_", "n", "|n", "=n", "<n", ">n"]
_LongCodes: TypeAlias = Literal["long", "l", "|l", "=l", "<l", ">l"]
_IntCodes = _IntPCodes
_LongLongCodes: TypeAlias = Literal["longlong", "q", "|q", "=q", "<q", ">q"]

_UByteCodes: TypeAlias = Literal["ubyte", "B", "|B", "=B", "<B", ">B"]
_UShortCodes: TypeAlias = Literal["ushort", "H", "|H", "=H", "<H", ">H"]
_UIntCCodes: TypeAlias = Literal["uintc", "I", "|I", "=I", "<I", ">I"]
_UIntPCodes: TypeAlias = Literal["uintp", "uint", "N", "|N", "=N", "<N", ">N"]
_ULongCodes: TypeAlias = Literal["ulong", "L", "|L", "=L", "<L", ">L"]
_UIntCodes = _UIntPCodes
_ULongLongCodes: TypeAlias = Literal["ulonglong", "Q", "|Q", "=Q", "<Q", ">Q"]

_HalfCodes: TypeAlias = Literal["half", "e", "|e", "=e", "<e", ">e"]
_SingleCodes: TypeAlias = Literal["single", "f", "|f", "=f", "<f", ">f"]
_DoubleCodes: TypeAlias = Literal["double", "float", "d", "|d", "=d", "<d", ">d"]
_LongDoubleCodes: TypeAlias = Literal["longdouble", "g", "|g", "=g", "<g", ">g"]

_CSingleCodes: TypeAlias = Literal["csingle", "F", "|F", "=F", "<F", ">F"]
_CDoubleCodes: TypeAlias = Literal["cdouble", "complex", "D", "|D", "=D", "<D", ">D"]
_CLongDoubleCodes: TypeAlias = Literal["clongdouble", "G", "|G", "=G", "<G", ">G"]

_StrCodes: TypeAlias = Literal["str", "str_", "unicode", "U", "|U", "=U", "<U", ">U"]
_BytesCodes: TypeAlias = Literal["bytes", "bytes_", "S", "|S", "=S", "<S", ">S"]
_VoidCodes: TypeAlias = Literal["void", "V", "|V", "=V", "<V", ">V"]
_ObjectCodes: TypeAlias = Literal["object", "object_", "O", "|O", "=O", "<O", ">O"]

_DT64Codes: TypeAlias = Literal[
    "datetime64", "|datetime64", "=datetime64", "<datetime64", ">datetime64",
    "datetime64[Y]", "|datetime64[Y]", "=datetime64[Y]", "<datetime64[Y]", ">datetime64[Y]",
    "datetime64[M]", "|datetime64[M]", "=datetime64[M]", "<datetime64[M]", ">datetime64[M]",
    "datetime64[W]", "|datetime64[W]", "=datetime64[W]", "<datetime64[W]", ">datetime64[W]",
    "datetime64[D]", "|datetime64[D]", "=datetime64[D]", "<datetime64[D]", ">datetime64[D]",
    "datetime64[h]", "|datetime64[h]", "=datetime64[h]", "<datetime64[h]", ">datetime64[h]",
    "datetime64[m]", "|datetime64[m]", "=datetime64[m]", "<datetime64[m]", ">datetime64[m]",
    "datetime64[s]", "|datetime64[s]", "=datetime64[s]", "<datetime64[s]", ">datetime64[s]",
    "datetime64[ms]", "|datetime64[ms]", "=datetime64[ms]", "<datetime64[ms]", ">datetime64[ms]",
    "datetime64[us]", "|datetime64[us]", "=datetime64[us]", "<datetime64[us]", ">datetime64[us]",
    "datetime64[ns]", "|datetime64[ns]", "=datetime64[ns]", "<datetime64[ns]", ">datetime64[ns]",
    "datetime64[ps]", "|datetime64[ps]", "=datetime64[ps]", "<datetime64[ps]", ">datetime64[ps]",
    "datetime64[fs]", "|datetime64[fs]", "=datetime64[fs]", "<datetime64[fs]", ">datetime64[fs]",
    "datetime64[as]", "|datetime64[as]", "=datetime64[as]", "<datetime64[as]", ">datetime64[as]",
    "M", "|M", "=M", "<M", ">M",
    "M8", "|M8", "=M8", "<M8", ">M8",
    "M8[Y]", "|M8[Y]", "=M8[Y]", "<M8[Y]", ">M8[Y]",
    "M8[M]", "|M8[M]", "=M8[M]", "<M8[M]", ">M8[M]",
    "M8[W]", "|M8[W]", "=M8[W]", "<M8[W]", ">M8[W]",
    "M8[D]", "|M8[D]", "=M8[D]", "<M8[D]", ">M8[D]",
    "M8[h]", "|M8[h]", "=M8[h]", "<M8[h]", ">M8[h]",
    "M8[m]", "|M8[m]", "=M8[m]", "<M8[m]", ">M8[m]",
    "M8[s]", "|M8[s]", "=M8[s]", "<M8[s]", ">M8[s]",
    "M8[ms]", "|M8[ms]", "=M8[ms]", "<M8[ms]", ">M8[ms]",
    "M8[us]", "|M8[us]", "=M8[us]", "<M8[us]", ">M8[us]",
    "M8[ns]", "|M8[ns]", "=M8[ns]", "<M8[ns]", ">M8[ns]",
    "M8[ps]", "|M8[ps]", "=M8[ps]", "<M8[ps]", ">M8[ps]",
    "M8[fs]", "|M8[fs]", "=M8[fs]", "<M8[fs]", ">M8[fs]",
    "M8[as]", "|M8[as]", "=M8[as]", "<M8[as]", ">M8[as]",
]  # fmt: skip
_TD64Codes: TypeAlias = Literal[
    "timedelta64", "|timedelta64", "=timedelta64", "<timedelta64", ">timedelta64",
    "timedelta64[Y]", "|timedelta64[Y]", "=timedelta64[Y]", "<timedelta64[Y]", ">timedelta64[Y]",
    "timedelta64[M]", "|timedelta64[M]", "=timedelta64[M]", "<timedelta64[M]", ">timedelta64[M]",
    "timedelta64[W]", "|timedelta64[W]", "=timedelta64[W]", "<timedelta64[W]", ">timedelta64[W]",
    "timedelta64[D]", "|timedelta64[D]", "=timedelta64[D]", "<timedelta64[D]", ">timedelta64[D]",
    "timedelta64[h]", "|timedelta64[h]", "=timedelta64[h]", "<timedelta64[h]", ">timedelta64[h]",
    "timedelta64[m]", "|timedelta64[m]", "=timedelta64[m]", "<timedelta64[m]", ">timedelta64[m]",
    "timedelta64[s]", "|timedelta64[s]", "=timedelta64[s]", "<timedelta64[s]", ">timedelta64[s]",
    "timedelta64[ms]", "|timedelta64[ms]", "=timedelta64[ms]", "<timedelta64[ms]", ">timedelta64[ms]",
    "timedelta64[us]", "|timedelta64[us]", "=timedelta64[us]", "<timedelta64[us]", ">timedelta64[us]",
    "timedelta64[ns]", "|timedelta64[ns]", "=timedelta64[ns]", "<timedelta64[ns]", ">timedelta64[ns]",
    "timedelta64[ps]", "|timedelta64[ps]", "=timedelta64[ps]", "<timedelta64[ps]", ">timedelta64[ps]",
    "timedelta64[fs]", "|timedelta64[fs]", "=timedelta64[fs]", "<timedelta64[fs]", ">timedelta64[fs]",
    "timedelta64[as]", "|timedelta64[as]", "=timedelta64[as]", "<timedelta64[as]", ">timedelta64[as]",
    "m", "|m", "=m", "<m", ">m",
    "m8", "|m8", "=m8", "<m8", ">m8",
    "m8[Y]", "|m8[Y]", "=m8[Y]", "<m8[Y]", ">m8[Y]",
    "m8[M]", "|m8[M]", "=m8[M]", "<m8[M]", ">m8[M]",
    "m8[W]", "|m8[W]", "=m8[W]", "<m8[W]", ">m8[W]",
    "m8[D]", "|m8[D]", "=m8[D]", "<m8[D]", ">m8[D]",
    "m8[h]", "|m8[h]", "=m8[h]", "<m8[h]", ">m8[h]",
    "m8[m]", "|m8[m]", "=m8[m]", "<m8[m]", ">m8[m]",
    "m8[s]", "|m8[s]", "=m8[s]", "<m8[s]", ">m8[s]",
    "m8[ms]", "|m8[ms]", "=m8[ms]", "<m8[ms]", ">m8[ms]",
    "m8[us]", "|m8[us]", "=m8[us]", "<m8[us]", ">m8[us]",
    "m8[ns]", "|m8[ns]", "=m8[ns]", "<m8[ns]", ">m8[ns]",
    "m8[ps]", "|m8[ps]", "=m8[ps]", "<m8[ps]", ">m8[ps]",
    "m8[fs]", "|m8[fs]", "=m8[fs]", "<m8[fs]", ">m8[fs]",
    "m8[as]", "|m8[as]", "=m8[as]", "<m8[as]", ">m8[as]",
]  # fmt: skip

# NOTE: `StringDType' has no scalar type, and therefore has no name that can
# be passed to the `dtype` constructor
_StringCodes: TypeAlias = Literal["T", "|T", "=T", "<T", ">T"]

# NOTE: Nested literals get flattened and de-duplicated at runtime, which isn't
# the case for a `Union` of `Literal`s.
# So even though they're equivalent when type-checking, they differ at runtime.
# Another advantage of nesting, is that they always have a "flat"
# `Literal.__args__`, which is a tuple of *literally* all its literal values.

_UnsignedIntegerCodes: TypeAlias = Literal[
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntCodes,
    _UByteCodes,
    _UShortCodes,
    _UIntCCodes,
    _ULongCodes,
    _ULongLongCodes,
]
_SignedIntegerCodes: TypeAlias = Literal[
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntCodes,
    _ByteCodes,
    _ShortCodes,
    _IntCCodes,
    _LongCodes,
    _LongLongCodes,
]
_FloatingCodes: TypeAlias = Literal[
    _Float16Codes, _Float32Codes, _Float64Codes, _HalfCodes, _SingleCodes, _DoubleCodes, _LongDoubleCodes
]
_ComplexFloatingCodes: TypeAlias = Literal[
    _Complex64Codes,
    _Complex128Codes,
    _CSingleCodes,
    _CDoubleCodes,
    _CLongDoubleCodes,
]
_IntegerCodes: TypeAlias = Literal[_UnsignedIntegerCodes, _SignedIntegerCodes]
_InexactCodes: TypeAlias = Literal[_FloatingCodes, _ComplexFloatingCodes]
_NumberCodes: TypeAlias = Literal[_IntegerCodes, _InexactCodes]

_CharacterCodes: TypeAlias = Literal[_StrCodes, _BytesCodes]
_FlexibleCodes: TypeAlias = Literal[_VoidCodes, _CharacterCodes]

_GenericCodes: TypeAlias = Literal[_BoolCodes, _NumberCodes, _FlexibleCodes, _DT64Codes, _TD64Codes, _ObjectCodes]
