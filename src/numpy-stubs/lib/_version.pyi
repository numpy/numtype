from typing import Final
from typing_extensions import override

__all__ = ["NumpyVersion"]

class NumpyVersion:
    vstring: Final[str]
    version: Final[str]
    major: Final[int]
    minor: Final[int]
    bugfix: Final[int]
    pre_release: Final[str]
    is_devversion: Final[bool]

    def __init__(self, /, vstring: str) -> None: ...
    def __lt__(self, other: str | NumpyVersion, /) -> bool: ...
    def __le__(self, other: str | NumpyVersion, /) -> bool: ...
    @override
    def __eq__(self, other: str | NumpyVersion, /) -> bool: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    @override
    def __ne__(self, other: str | NumpyVersion, /) -> bool: ...  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
    def __gt__(self, other: str | NumpyVersion, /) -> bool: ...
    def __ge__(self, other: str | NumpyVersion, /) -> bool: ...
