from typing import final

@final
class NBitBase: ...

class _128Bit(NBitBase): ...  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
class _96Bit(_128Bit): ...  # type: ignore[misc]
class _64Bit(_96Bit): ...  # type: ignore[misc]
class _32Bit(_64Bit): ...  # type: ignore[misc]
class _16Bit(_32Bit): ...  # type: ignore[misc]
class _8Bit(_16Bit): ...  # type: ignore[misc]
