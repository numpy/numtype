# mypy: disable-error-code="misc"
from typing import final, type_check_only
from typing_extensions import Never

# exported as numpy.typing.NBitBase

@final
class NBitBase: ...

###
#

@type_check_only
class _LD(NBitBase): ...  # pyright: ignore[reportGeneralTypeIssues]

@type_check_only
class _64(_LD): ...

@type_check_only
class _32(_64): ...

@type_check_only
class _16(_32): ...

@type_check_only
class _8(_16): ...

###
# legacy `numpy._typing` runtime definitions

_128Bit = _LD
_96Bit = _LD
_64Bit = _64
_32Bit = _32
_16Bit = _16
_8Bit = _8

# non-existant
_256Bit = Never
_80Bit = Never
