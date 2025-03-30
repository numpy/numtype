# mypy: disable-error-code="misc"
from typing import final, type_check_only
from typing_extensions import deprecated

# exported as numpy.typing.NBitBase

# Documentation: https://numpy.org/numtype/user_guide/differences/#no-more-nbitbase
@final
@deprecated(
    "NBitBase is deprecated and should not be used. "
    "NumPy scalar types are now concrete and no longer accept generic bounds like np.floating[T]. "
    "Use abstract types (e.g., np.floating) as bounds instead."
)
class NBitBase: ...

###
#

# long double
@type_check_only
class _64L(NBitBase): ...  # pyright: ignore[reportDeprecated, reportGeneralTypeIssues]

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
