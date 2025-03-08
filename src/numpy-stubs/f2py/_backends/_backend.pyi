import abc
from _typeshed import Incomplete
from typing import Any

class Backend(abc.ABC):
    modulename: str
    sources: list[str]
    extra_objects: Incomplete
    build_dir: Incomplete
    include_dirs: Incomplete
    library_dirs: Incomplete
    libraries: Incomplete
    define_macros: Incomplete
    undef_macros: Incomplete
    f2py_flags: Incomplete
    sysinfo_flags: Incomplete
    fc_flags: Incomplete
    flib_flags: Incomplete
    setup_flags: Incomplete
    remove_build_dir: Incomplete
    extra_dat: dict[str, Any]

    def __init__(
        self,
        /,
        modulename: str,
        sources: list[str],
        extra_objects: Incomplete,
        build_dir: Incomplete,
        include_dirs: Incomplete,
        library_dirs: Incomplete,
        libraries: list[str],
        define_macros: Incomplete,
        undef_macros: Incomplete,
        f2py_flags: Incomplete,
        sysinfo_flags: Incomplete,
        fc_flags: Incomplete,
        flib_flags: Incomplete,
        setup_flags: Incomplete,
        remove_build_dir: Incomplete,
        extra_dat: Incomplete,
    ) -> None: ...
    @abc.abstractmethod
    def compile(self) -> None: ...
