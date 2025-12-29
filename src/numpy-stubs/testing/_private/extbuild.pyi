import pathlib
import types
from collections.abc import Iterable, Sequence

__all__ = ["build_and_import_extension", "compile_extension_module"]

def build_and_import_extension(
    modname: str,
    functions: Sequence[tuple[str, str, str]],
    *,
    prologue: str = "",
    build_dir: pathlib.Path | None = None,
    include_dirs: Sequence[str] | None = None,
    more_init: str = "",
) -> types.ModuleType: ...

#
def compile_extension_module(
    name: str,
    builddir: pathlib.Path,
    include_dirs: Sequence[str],
    source_string: str,
    libraries: Sequence[str] | None = None,
    library_dirs: Sequence[str] | None = None,
) -> pathlib.Path: ...

#
def build(
    cfile: pathlib.Path,
    outputfilename: pathlib.Path,
    compile_extra: str,
    link_extra: str,
    include_dirs: str,
    libraries: object,  # unused
    library_dirs: Iterable[str],
) -> pathlib.Path: ...  # undocumented

#
def get_so_suffix() -> str: ...  # undocumented
