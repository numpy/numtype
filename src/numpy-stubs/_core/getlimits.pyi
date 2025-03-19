from types import GenericAlias
from typing import Final, Generic, Literal as L, overload
from typing_extensions import Self, TypeVar

import numpy as np
from _numtype import Inexact32, Inexact64, InexactLD
from numpy._typing import _96Bit, _128Bit, _DTypeLike
from numpy._typing._char_codes import (
    _CLongDoubleCodes,
    _Complex64Codes,
    _Complex128Codes,
    _Complex192Codes,
    _Complex256Codes,
    _Float16Codes,
    _Float32Codes,
    _Float64Codes,
    _Float96Codes,
    _Float128Codes,
    _Int8Codes,
    _Int16Codes,
    _Int32Codes,
    _Int64Codes,
    _IntPCodes,
    _LongCodes,
    _LongDoubleCodes,
    _UInt8Codes,
    _UInt16Codes,
    _UInt32Codes,
    _UInt64Codes,
    _UIntPCodes,
    _ULongCodes,
)

__all__ = ["finfo", "iinfo"]

###

_FloatingT_co = TypeVar("_FloatingT_co", bound=np.floating, default=np.floating, covariant=True)
_IntegerT_co = TypeVar("_IntegerT_co", bound=np.integer, default=np.integer, covariant=True)

###

class iinfo(Generic[_IntegerT_co]):
    dtype: np.dtype[_IntegerT_co]
    bits: Final[L[8, 16, 32, 64]]
    kind: Final[L["i", "u"]]
    key: Final[L["i8", "i16", "i32", "i64", "u8", "u16", "u32", "u64"]]

    @property
    def min(self, /) -> int: ...
    @property
    def max(self, /) -> int: ...

    #
    @overload
    def __init__(self, /, int_type: _IntegerT_co | _DTypeLike[_IntegerT_co]) -> None: ...
    @overload
    def __init__(self: iinfo[np.int8], /, int_type: _Int8Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint8], /, int_type: _UInt8Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.int16], /, int_type: _Int16Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint16], /, int_type: _UInt16Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.int32], /, int_type: _Int32Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint32], /, int_type: _UInt32Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.int64], /, int_type: _Int64Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.uint64], /, int_type: _UInt64Codes) -> None: ...
    @overload
    def __init__(self: iinfo[np.long], /, int_type: _LongCodes) -> None: ...
    @overload
    def __init__(self: iinfo[np.ulong], /, int_type: _ULongCodes) -> None: ...
    @overload
    def __init__(self: iinfo[np.intp], /, int_type: int | type[int] | _IntPCodes) -> None: ...
    @overload
    def __init__(self: iinfo[np.uintp], /, int_type: _UIntPCodes) -> None: ...

    #
    @classmethod
    def __class_getitem__(cls, item: object, /) -> GenericAlias: ...

#
class finfo(Generic[_FloatingT_co]):
    dtype: np.dtype[_FloatingT_co]
    eps: _FloatingT_co
    epsneg: _FloatingT_co
    resolution: _FloatingT_co
    smallest_subnormal: _FloatingT_co
    max: _FloatingT_co
    min: _FloatingT_co

    bits: Final[L[2, 4, 8, 12, 16]]
    iexp: Final[int]
    machep: Final[int]
    maxexp: Final[int]
    minexp: Final[int]
    negep: Final[int]
    nexp: Final[int]
    nmant: Final[int]
    precision: Final[int]

    @property
    def smallest_normal(self, /) -> _FloatingT_co: ...
    @property
    def tiny(self, /) -> _FloatingT_co: ...

    #
    @overload
    def __new__(cls, dtype: _FloatingT_co | _DTypeLike[_FloatingT_co]) -> Self: ...
    @overload
    def __new__(cls, dtype: type[complex] | complex) -> finfo[np.float64]: ...
    @overload
    def __new__(cls, dtype: np.float16 | _DTypeLike[np.float16] | _Float16Codes) -> finfo[np.float16]: ...
    @overload
    def __new__(cls, dtype: Inexact32 | _DTypeLike[Inexact32] | _Float32Codes | _Complex64Codes) -> finfo[np.float32]: ...
    @overload
    def __new__(cls, dtype: Inexact64 | _DTypeLike[Inexact64] | _Float64Codes | _Complex128Codes) -> finfo[np.float64]: ...
    @overload
    def __new__(
        cls,
        dtype: np.inexact[_96Bit] | _DTypeLike[np.inexact[_96Bit]] | _Float96Codes | _Complex192Codes,
    ) -> finfo[np.float96]: ...
    @overload
    def __new__(
        cls,
        dtype: np.inexact[_128Bit] | _DTypeLike[np.inexact[_128Bit]] | _Float128Codes | _Complex256Codes,
    ) -> finfo[np.float128]: ...
    @overload
    def __new__(
        cls,
        dtype: InexactLD | _DTypeLike[InexactLD] | _LongDoubleCodes | _CLongDoubleCodes,
    ) -> finfo[np.float96 | np.float128]: ...

    #
    @classmethod
    def __class_getitem__(cls, item: object, /) -> GenericAlias: ...
