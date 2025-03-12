# mypy: disable-error-code=override
# pyright: reportIncompatibleMethodOverride=false

import datetime as dt
from typing import Protocol, SupportsFloat, SupportsIndex, TypeAlias, final, type_check_only
from typing_extensions import Self, TypeVar

__all__ = ["Just", "JustBytes", "JustComplex", "JustFloat", "JustInt", "JustObject", "JustStr"]

###

_T = TypeVar("_T")

_CanFloatOrIndex: TypeAlias = SupportsFloat | SupportsIndex

###

# Type-check-only equivalents of the `optype.Just*` types, see
# https://github.com/jorenham/optype#just

# NOTE: These should only be used to annotate _input_, never _output_.

@final  # the pyright and mypy errors are false positives because of this @final
@type_check_only
class Just(Protocol[_T]):
    @property
    def __class__(self, /) -> type[_T]: ...
    @__class__.setter
    def __class__(self, t: type[_T], /) -> None: ...

@final
@type_check_only
class JustInt(Protocol):
    @property
    def __class__(self, /) -> type[int]: ...
    @__class__.setter
    def __class__(self, t: type[int], /) -> None: ...

    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def __new__(cls, x: str | bytes | bytearray, /, base: SupportsIndex) -> Self: ...

@final
@type_check_only
class JustFloat(Protocol):
    @property
    def __class__(self, /) -> type[float]: ...
    @__class__.setter
    def __class__(self, t: type[float], /) -> None: ...

    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def hex(self, /) -> str: ...

@final
@type_check_only
class JustComplex(Protocol):
    @property
    def __class__(self, /) -> type[complex]: ...
    @__class__.setter
    def __class__(self, t: type[complex], /) -> None: ...

    # workaround for `pyright<1.1.390` and `basedpyright<1.22.1`
    def __new__(cls, /, real: _CanFloatOrIndex, imag: _CanFloatOrIndex) -> Self: ...

@final
@type_check_only
class JustBytes(Protocol):
    @property
    def __class__(self, /) -> type[bytes]: ...
    @__class__.setter
    def __class__(self, t: type[bytes], /) -> None: ...

@final
@type_check_only
class JustStr(Protocol):
    @property
    def __class__(self, /) -> type[str]: ...
    @__class__.setter
    def __class__(self, t: type[str], /) -> None: ...

@final
@type_check_only
class JustDate(Protocol):
    @property
    def __class__(self, /) -> type[dt.date]: ...
    @__class__.setter
    def __class__(self, t: type[dt.date], /) -> None: ...

@final
@type_check_only
class JustObject(Protocol):
    @property
    def __class__(self, /) -> type[object]: ...
    @__class__.setter
    def __class__(self, t: type[object], /) -> None: ...
