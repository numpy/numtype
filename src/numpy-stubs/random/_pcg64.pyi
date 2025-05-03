from typing import Self, TypedDict, type_check_only

from numpy.random.bit_generator import BitGenerator

__all__ = ["PCG64"]

###

@type_check_only
class _PCG64Internal(TypedDict):
    state: int
    inc: int

@type_check_only
class _PCG64State(TypedDict):
    bit_generator: str
    state: _PCG64Internal
    has_uint32: int
    uinteger: int

###

class PCG64(BitGenerator[_PCG64State]):
    def jumped(self, jumps: int = ...) -> Self: ...
    def advance(self, delta: int) -> Self: ...

class PCG64DXSM(BitGenerator[_PCG64State]):
    def jumped(self, jumps: int = ...) -> Self: ...
    def advance(self, delta: int) -> Self: ...
