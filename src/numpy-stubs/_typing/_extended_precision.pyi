from typing import TypeAlias

import numpy as np

from . import _80Bit, _96Bit, _128Bit, _256Bit

uint128: TypeAlias = np.unsignedinteger[_128Bit]
uint256: TypeAlias = np.unsignedinteger[_256Bit]
int128: TypeAlias = np.signedinteger[_128Bit]
int256: TypeAlias = np.signedinteger[_256Bit]
float80: TypeAlias = np.floating[_80Bit]
float96: TypeAlias = np.floating[_96Bit]
float128: TypeAlias = np.floating[_128Bit]
float256: TypeAlias = np.floating[_256Bit]
complex160: TypeAlias = np.complexfloating[_80Bit]
complex192: TypeAlias = np.complexfloating[_96Bit]
complex256: TypeAlias = np.complexfloating[_128Bit]
complex512: TypeAlias = np.complexfloating[_256Bit]
