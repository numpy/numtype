from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Final

from .__version__ import version

f2py_version: Final = version

def findcommonblocks(block: Mapping[str, Incomplete], top: int = 1) -> list[tuple[str, list[str], dict[str, Incomplete]]]: ...
def buildhooks(m: Mapping[str, Incomplete]) -> tuple[dict[str, Incomplete], str]: ...
