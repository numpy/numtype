from typing import Literal, TypeAlias

# bool
_BoolCodes: TypeAlias = Literal["bool", "bool_", "?", "|?", "=?", "<?", ">?"]

# signed integer
_Int8Codes: TypeAlias = Literal["int8", "byte", "i1", "b", "|i1", "|b", "=i1", "=b", "<i1", "<b", ">i1", ">b"]
_Int16Codes: TypeAlias = Literal["int16", "short", "i2", "h", "|i2", "|h", "=i2", "=h", "<i2", "<h", ">i2", ">h"]
_Int32Codes: TypeAlias = Literal["int32", "intc", "i4", "i", "|i4", "|i", "=i4", "=i", "<i4", "<i", ">i4", ">i"]
_Int64Codes: TypeAlias = Literal["int64", "longlong", "i8", "q", "|i8", "|q", "=i8", "=q", "<i8", "<q", ">i8", ">q"]
_IntPCodes: TypeAlias = Literal["intp", "int", "int_", "n", "|n", "=n", "<n", ">n"]  # either int32 or int64
_LongCodes: TypeAlias = Literal["long", "l", "|l", "=l", "<l", ">l"]  # either int32 or int64
_LongLongCodes: TypeAlias = Literal["longlong", "q", "|q", "=q", "<q", ">q"]
_ByteCodes: TypeAlias = _Int8Codes
_ShortCodes: TypeAlias = _Int16Codes
_IntCCodes: TypeAlias = _Int32Codes
_IntCodes: TypeAlias = _IntPCodes
_SignedIntegerCodes: TypeAlias = Literal[_Int8Codes, _Int16Codes, _Int32Codes, _Int64Codes, _IntPCodes, _LongCodes]

# unsigned integer
_UInt8Codes: TypeAlias = Literal["uint8", "ubyte", "u1", "B", "|u1", "|B", "=u1", "=B", "<u1", "<B", ">u1", ">B"]
_UInt16Codes: TypeAlias = Literal["uint16", "ushort", "u2", "H", "|u2", "|H", "=u2", "=H", "<u2", "<H", ">u2", ">H"]
_UInt32Codes: TypeAlias = Literal["uint32", "uintc", "u4", "I", "|u4", "|I", "=u4", "=I", "<u4", "<I", ">u4", ">I"]
_UInt64Codes: TypeAlias = Literal["uint64", "ulonglong", "u8", "Q", "|u8", "|Q", "=u8", "=Q", "<u8", "<Q", ">u8", ">Q"]
_UIntPCodes: TypeAlias = Literal["uintp", "uint", "N", "|N", "=N", "<N", ">N"]  # either uint32 or uint64
_ULongCodes: TypeAlias = Literal["ulong", "L", "|L", "=L", "<L", ">L"]  # either uint32 or uint64
_ULongLongCodes: TypeAlias = Literal["ulonglong", "Q", "|Q", "=Q", "<Q", ">Q"]
_UByteCodes: TypeAlias = _UInt8Codes
_UShortCodes: TypeAlias = _UInt16Codes
_UIntCCodes: TypeAlias = _UInt32Codes
_UIntCodes: TypeAlias = _UIntPCodes
_UnsignedIntegerCodes: TypeAlias = Literal[_UInt8Codes, _UInt16Codes, _UInt32Codes, _UInt64Codes, _UIntPCodes, _ULongCodes]

# real floating
_Float16Codes: TypeAlias = Literal["float16", "half", "f2", "e", "|f2", "|e", "=f2", "=e", "<f2", "<e", ">f2", ">2"]
_Float32Codes: TypeAlias = Literal["float32", "single", "f4", "f", "|f4", "|f", "=f4", "=f", "<f4", "<f", ">4f", ">f"]
_Float64Codes: TypeAlias = Literal["float64", "double", "float", "f8", "d", "|f8", "|d", "=f8", "=d", "<f8", "<d", ">f8", ">d"]
_Float96Codes: TypeAlias = Literal["float96", "f12", "|f12", "=f12", "<f12", ">f12"]
_Float128Codes: TypeAlias = Literal["float128", "f16", "|f16", "=f16", "<f16", ">f16"]
_LongDoubleCodes: TypeAlias = Literal["longdouble", "g", "|g", "=g", "<g", ">g", _Float96Codes, _Float128Codes]
_HalfCodes: TypeAlias = _Float16Codes
_SingleCodes: TypeAlias = _Float32Codes
_DoubleCodes: TypeAlias = _Float64Codes
_FloatingCodes: TypeAlias = Literal[_Float16Codes, _Float32Codes, _Float64Codes, _LongDoubleCodes]

# complex floating
_Complex64Codes: TypeAlias = Literal["complex64", "csingle", "c8", "F", "|c8", "|F", "=c8", "=F", "<c8", "<F", ">c8", ">F"]
_Complex128Codes: TypeAlias = Literal[
    "complex128", "cdouble", "complex",
    "c16", "D", "|c16", "|D", "=c16", "=D", "<c16", "<D", ">c16", ">D",
]  # fmt: skip
_Complex192Codes: TypeAlias = Literal["complex192", "c24", "|c24", "=c24", "<c24", ">c24"]
_Complex256Codes: TypeAlias = Literal["complex256", "c32", "|c32", "=c32", "<c32", ">c32"]
_CLongDoubleCodes: TypeAlias = Literal["clongdouble", "G", "|G", "=G", "<G", ">G", _Complex192Codes, _Complex256Codes]
_CSingleCodes: TypeAlias = _Complex64Codes
_CDoubleCodes: TypeAlias = _Complex128Codes
_ComplexFloatingCodes: TypeAlias = Literal[_Complex64Codes, _Complex128Codes, _CLongDoubleCodes]

_IntegerCodes: TypeAlias = Literal[_UnsignedIntegerCodes, _SignedIntegerCodes]
_InexactCodes: TypeAlias = Literal[_FloatingCodes, _ComplexFloatingCodes]
_NumberCodes: TypeAlias = Literal[_IntegerCodes, _InexactCodes]

# NOTE: These are infinitely many "flexible" codes
_StrCodes: TypeAlias = Literal["str", "str_", "unicode", "U", "|U", "=U", "<U", ">U"]
_BytesCodes: TypeAlias = Literal["bytes", "bytes_", "S", "|S", "=S", "<S", ">S"]
_CharacterCodes: TypeAlias = Literal[_StrCodes, _BytesCodes]
_VoidCodes: TypeAlias = Literal["void", "V", "|V", "=V", "<V", ">V"]
_FlexibleCodes: TypeAlias = Literal[_VoidCodes, _CharacterCodes]

_ObjectCodes: TypeAlias = Literal["object", "object_", "O", "|O", "=O", "<O", ">O"]

# NOTE: `StringDType' has no scalar type, and therefore has no name that can be passed to the `dtype` constructor
_StringCodes: TypeAlias = Literal["T", "|T", "=T", "<T", ">T"]

# NOTE: The datetime64 and timedelta64 aren't complete, because e.g. "M8[6D]" is also valid.
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

_GenericCodes: TypeAlias = Literal[_BoolCodes, _NumberCodes, _FlexibleCodes, _DT64Codes, _TD64Codes, _ObjectCodes]
