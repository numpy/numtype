from typing import Protocol, SupportsFloat, SupportsIndex, TypeAlias, final, type_check_only
from typing_extensions import Self, TypeVar

__all__ = ["Just", "JustComplex", "JustFloat", "JustInt"]

###

_T = TypeVar("_T")

_ToFloat: TypeAlias = SupportsFloat | SupportsIndex

###

# Type-check-only equivalents of the `optype.Just*` types, see
# https://github.com/jorenham/optype#just

@final  # the pyright and mypy errors are false positives because of this @final
@type_check_only
class Just(Protocol[_T]):
    @property  # type: ignore[override]
    def __class__(self, /) -> type[_T]: ...  # pyright: ignore[reportIncompatibleMethodOverride]
    @__class__.setter
    def __class__(self, t: type[_T], /) -> None: ...

@final
@type_check_only
class JustInt(Just[int], Protocol):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def __new__(cls, x: str | bytes | bytearray, /, base: SupportsIndex) -> Self: ...

@final
@type_check_only
class JustFloat(Just[float], Protocol):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def hex(self, /) -> str: ...

@final
@type_check_only
class JustComplex(Just[complex], Protocol):  # type: ignore[misc]  # pyright: ignore[reportGeneralTypeIssues]
    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def __new__(cls, /, real: _ToFloat, imag: _ToFloat) -> Self: ...
