from typing import TypeAlias
from typing_extensions import Never

from ._nbit_base import _32Bit, _64Bit, _96Bit, _128Bit

###
# TODO(jorenham): Stop using these:
# https://github.com/numpy/numtype/issues/136

_NBitIntP: TypeAlias = _32Bit | _64Bit
_NBitLong: TypeAlias = _32Bit | _64Bit
_NBitLongLong: TypeAlias = _64Bit
_NBitLongDouble: TypeAlias = _96Bit | _128Bit

###
# unused legacy aliases

_NBitByte: TypeAlias = Never
_NBitShort: TypeAlias = Never
_NBitIntC: TypeAlias = Never
_NBitInt: TypeAlias = Never

_NBitHalf: TypeAlias = Never
_NBitSingle: TypeAlias = Never
_NBitDouble: TypeAlias = Never
