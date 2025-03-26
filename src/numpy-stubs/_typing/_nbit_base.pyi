# mypy: disable-error-code="misc"
from typing import final, type_check_only

# exported as numpy.typing.NBitBase

@final
class NBitBase: ...

###
#

# long double
@type_check_only
class _64L(NBitBase): ...  # pyright: ignore[reportGeneralTypeIssues]

@type_check_only
class _64(_64L): ...

@type_check_only
class _32(_64): ...

@type_check_only
class _32_64(_32, _64): ...

@type_check_only
class _16(_32_64): ...

@type_check_only
class _8(_16): ...
