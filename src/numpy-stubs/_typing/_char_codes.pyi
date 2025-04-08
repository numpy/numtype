from typing import Literal, TypeAlias

_BoolCodes: TypeAlias = Literal["bool", "bool_", "b1", "?", "|?", "=?", "<?", ">?", "\x00"]

_Int8Codes: TypeAlias = Literal["int8", "byte", "i1", "b", "|i1", "|b", "=i1", "=b", "<i1", "<b", ">i1", ">b", "\x01"]
_UInt8Codes: TypeAlias = Literal["uint8", "ubyte", "u1", "B", "|u1", "|B", "=u1", "=B", "<u1", "<B", ">u1", ">B", "\x02"]
_ByteCodes: TypeAlias = _Int8Codes
_UByteCodes: TypeAlias = _UInt8Codes
_Int16Codes: TypeAlias = Literal["int16", "short", "i2", "h", "|i2", "|h", "=i2", "=h", "<i2", "<h", ">i2", ">h", "\x03"]
_UInt16Codes: TypeAlias = Literal["uint16", "ushort", "u2", "H", "|u2", "|H", "=u2", "=H", "<u2", "<H", ">u2", ">H", "\x04"]
_ShortCodes: TypeAlias = _Int16Codes
_UShortCodes: TypeAlias = _UInt16Codes
_Int32Codes: TypeAlias = Literal["int32", "intc", "i4", "i", "|i4", "|i", "=i4", "=i", "<i4", "<i", ">i4", ">i", "\x05"]
_UInt32Codes: TypeAlias = Literal["uint32", "uintc", "u4", "I", "|u4", "|I", "=u4", "=I", "<u4", "<I", ">u4", ">I", "\x06"]
_IntCCodes: TypeAlias = _Int32Codes
_UIntCCodes: TypeAlias = _UInt32Codes
_LongCodes: TypeAlias = Literal["long", "l", "|l", "=l", "<l", ">l", "\x07"]  # either int32 or intp
_ULongCodes: TypeAlias = Literal["ulong", "L", "|L", "=L", "<L", ">L", "\x08"]  # either uint32 or uint64
_Int64Codes: TypeAlias = Literal["int64", "longlong", "i8", "q", "|i8", "|q", "=i8", "=q", "<i8", "<q", ">i8", ">q", "\x09"]
_UInt64Codes: TypeAlias = Literal["uint64", "ulonglong", "u8", "Q", "|u8", "|Q", "=u8", "=Q", "<u8", "<Q", ">u8", ">Q", "\x0a"]
_LongLongCodes: TypeAlias = _Int64Codes
_ULongLongCodes: TypeAlias = _UInt64Codes
_IntPCodes: TypeAlias = Literal["intp", "int", "int_", "n", "|n", "=n", "<n", ">n"]  # usually int64
_UIntPCodes: TypeAlias = Literal["uintp", "uint", "N", "|N", "=N", "<N", ">N"]  # usually uint64
_IntCodes: TypeAlias = _IntPCodes
_UIntCodes: TypeAlias = _UIntPCodes

_Float16Codes: TypeAlias = Literal["float16", "half", "f2", "e", "|f2", "|e", "=f2", "=e", "<f2", "<e", ">f2", ">2", "\x17"]
_HalfCodes: TypeAlias = _Float16Codes
_Float32Codes: TypeAlias = Literal["float32", "single", "f4", "f", "|f4", "|f", "=f4", "=f", "<f4", "<f", ">4f", ">f", "\x0b"]
_SingleCodes: TypeAlias = _Float32Codes
_Float64Codes: TypeAlias = Literal[
    "float64", "double", "float", "f8", "d", "|f8", "|d", "=f8", "=d", "<f8", "<d", ">f8", ">d", "\x0c"
]
_DoubleCodes: TypeAlias = _Float64Codes
_Float96Codes: TypeAlias = Literal["float96", "f12", "|f12", "=f12", "<f12", ">f12"]
_Float128Codes: TypeAlias = Literal["float128", "f16", "|f16", "=f16", "<f16", ">f16"]
_LongDoubleCodes: TypeAlias = Literal["longdouble", "g", "|g", "=g", "<g", ">g", _Float96Codes, _Float128Codes, "\x0d"]

_Complex64Codes: TypeAlias = Literal[
    "complex64", "csingle", "c8", "F", "|c8", "|F", "=c8", "=F", "<c8", "<F", ">c8", ">F", "\x0e"
]
_CSingleCodes: TypeAlias = _Complex64Codes
_Complex128Codes: TypeAlias = Literal[
    "complex128", "cdouble", "complex", "c16", "D", "|c16", "|D", "=c16", "=D", "<c16", "<D", ">c16", ">D", "\x0f"
]
_CDoubleCodes: TypeAlias = _Complex128Codes
_Complex192Codes: TypeAlias = Literal["complex192", "c24", "|c24", "=c24", "<c24", ">c24"]
_Complex256Codes: TypeAlias = Literal["complex256", "c32", "|c32", "=c32", "<c32", ">c32"]
_CLongDoubleCodes: TypeAlias = Literal["clongdouble", "G", "|G", "=G", "<G", ">G", _Complex192Codes, _Complex256Codes, "\x10"]

_ObjectCodes: TypeAlias = Literal["object", "object_", "O", "|O", "=O", "<O", ">O", "\x11"]

# NOTE: These are infinitely many "flexible" codes
_BytesCodes: TypeAlias = Literal["bytes", "bytes_", "S", "|S", "=S", "<S", ">S", "\x12"]
_StrCodes: TypeAlias = Literal["str", "str_", "unicode", "U", "|U", "=U", "<U", ">U", "\x13"]
_VoidCodes: TypeAlias = Literal["void", "V", "|V", "=V", "<V", ">V", "\x14"]

# NOTE: The datetime64 and timedelta64 aren't complete, because e.g. "M8[6D]" is also valid.
_DT64Codes: TypeAlias = Literal[
    "datetime64", "M",
    "datetime64[Y]", "M8[Y]",
    "datetime64[M]", "M8[M]",
    "datetime64[W]", "M8[W]",
    "datetime64[D]", "M8[D]",
    "datetime64[h]", "M8[h]",
    "datetime64[m]", "M8[m]",
    "datetime64[s]", "M8[s]",
    "datetime64[ms]", "M8[ms]",
    "datetime64[us]", "M8[us]",
    "datetime64[ns]", "M8[ns]",
    "datetime64[ps]", "M8[ps]",
    "datetime64[fs]", "M8[fs]",
    "datetime64[as]", "M8[as]",
    "|M", "=M", "<M", ">M", "M8", "|M8", "=M8", "<M8", ">M8", "\x15",
]  # fmt: skip
_TD64Codes: TypeAlias = Literal[
    "timedelta64", "m",
    "timedelta64[Y]", "m8[Y]",
    "timedelta64[M]", "m8[M]",
    "timedelta64[W]", "m8[W]",
    "timedelta64[D]", "m8[D]",
    "timedelta64[h]", "m8[h]",
    "timedelta64[m]", "m8[m]",
    "timedelta64[s]", "m8[s]",
    "timedelta64[ms]", "m8[ms]",
    "timedelta64[us]", "m8[us]",
    "timedelta64[ns]", "m8[ns]",
    "timedelta64[ps]", "m8[ps]",
    "timedelta64[fs]", "m8[fs]",
    "timedelta64[as]", "m8[as]",
     "|m", "=m", "<m", ">m", "m8", "|m8", "=m8", "<m8", ">m8", "\x16",
]  # fmt: skip

# NOTE: `StringDType' has no scalar type, and therefore has no name that can be passed to the `dtype` constructor
_StringCodes: TypeAlias = Literal["T", "|T", "=T", "<T", ">T"]

_SignedIntegerCodes: TypeAlias = Literal[_Int8Codes, _Int16Codes, _Int32Codes, _Int64Codes, _IntPCodes, _LongCodes]
_UnsignedIntegerCodes: TypeAlias = Literal[_UInt8Codes, _UInt16Codes, _UInt32Codes, _UInt64Codes, _UIntPCodes, _ULongCodes]
_FloatingCodes: TypeAlias = Literal[_Float16Codes, _Float32Codes, _Float64Codes, _LongDoubleCodes]
_ComplexFloatingCodes: TypeAlias = Literal[_Complex64Codes, _Complex128Codes, _CLongDoubleCodes]
_IntegerCodes: TypeAlias = Literal[_UnsignedIntegerCodes, _SignedIntegerCodes]
_InexactCodes: TypeAlias = Literal[_FloatingCodes, _ComplexFloatingCodes]
_NumberCodes: TypeAlias = Literal[_IntegerCodes, _InexactCodes]
_CharacterCodes: TypeAlias = Literal[_StrCodes, _BytesCodes]
_FlexibleCodes: TypeAlias = Literal[_VoidCodes, _CharacterCodes]
_GenericCodes: TypeAlias = Literal[_BoolCodes, _IntegerCodes, _InexactCodes, _FlexibleCodes, _DT64Codes, _TD64Codes, _ObjectCodes]
