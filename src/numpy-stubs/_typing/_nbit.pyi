from typing import TypeAlias

from ._nbit_base import _32Bit, _64Bit, _96Bit, _128Bit

_NBitIntP: TypeAlias = _32Bit | _64Bit
_NBitLong: TypeAlias = _32Bit | _64Bit
_NBitLongLong: TypeAlias = _64Bit
_NBitLongDouble: TypeAlias = _96Bit | _128Bit
