from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Final

__version__: Final[str] = ...
f2py_version: Final = "See `f2py -v`"
usemodule_rules: Final[dict[str, str | list[str]]] = ...

def buildusevars(m: Mapping[str, Incomplete], r: Mapping[str, Mapping[str, Incomplete]]) -> dict[str, Incomplete]: ...
def buildusevar(name: str, realname: str, vars: Mapping[str, Mapping[str, str]], usemodulename: str) -> dict[str, Incomplete]: ...
