from _typeshed import Incomplete

__all__ = [
    "Configuration",
    "all_strings",
    "allpath",
    "appendpath",
    "as_list",
    "blue_text",
    "cyan_text",
    "cyg2win32",
    "default_config_dict",
    "dict_append",
    "dot_join",
    "exec_mod_from_location",
    "filter_sources",
    "generate_config_py",
    "get_build_architecture",
    "get_cmd",
    "get_data_files",
    "get_dependencies",
    "get_ext_source_files",
    "get_frame",
    "get_info",
    "get_language",
    "get_lib_source_files",
    "get_mathlibs",
    "get_num_build_jobs",
    "get_numpy_include_dirs",
    "get_pkg_info",
    "get_script_files",
    "gpaths",
    "green_text",
    "has_cxx_sources",
    "has_f_sources",
    "is_local_src_dir",
    "is_sequence",
    "is_string",
    "mingw32",
    "minrelpath",
    "njoin",
    "red_text",
    "sanitize_cxx_flags",
    "terminal_has_colors",
    "yellow_text",
]

class InstallableLib:
    name: Incomplete
    build_info: Incomplete
    target_dir: Incomplete
    def __init__(self, name: str, build_info: Incomplete, target_dir: Incomplete) -> None: ...

def get_num_build_jobs() -> int: ...
def allpath(name: str) -> Incomplete: ...
def njoin(*pat: str) -> Incomplete: ...
def get_mathlibs(path: str | None = None) -> Incomplete: ...
def minrelpath(path: str) -> Incomplete: ...
def gpaths(paths: Incomplete, local_path: str = "", include_non_existing: bool = True) -> Incomplete: ...
def terminal_has_colors() -> Incomplete: ...
def red_text(s: str) -> Incomplete: ...
def green_text(s: str) -> Incomplete: ...
def yellow_text(s: str) -> Incomplete: ...
def cyan_text(s: str) -> Incomplete: ...
def blue_text(s: str) -> Incomplete: ...
def cyg2win32(path: str) -> str: ...
def mingw32() -> Incomplete: ...
def is_string(s: str) -> Incomplete: ...
def all_strings(lst: Incomplete) -> Incomplete: ...
def is_sequence(seq: Incomplete) -> Incomplete: ...
def as_list(seq: Incomplete) -> Incomplete: ...
def get_language(sources: Incomplete) -> Incomplete: ...
def has_f_sources(sources: Incomplete) -> Incomplete: ...
def has_cxx_sources(sources: Incomplete) -> Incomplete: ...
def filter_sources(sources: Incomplete) -> Incomplete: ...
def get_dependencies(sources: Incomplete) -> Incomplete: ...
def is_local_src_dir(directory: Incomplete) -> Incomplete: ...
def get_ext_source_files(ext: Incomplete) -> Incomplete: ...
def get_script_files(scripts: Incomplete) -> Incomplete: ...
def get_lib_source_files(lib: Incomplete) -> Incomplete: ...
def get_data_files(data: Incomplete) -> Incomplete: ...
def dot_join(*args: Incomplete) -> Incomplete: ...
def get_frame(level: int = 0) -> Incomplete: ...

class Configuration:
    _list_keys: Incomplete
    _dict_keys: Incomplete
    _extra_keys: Incomplete
    numpy_include_dirs: Incomplete
    name: Incomplete
    version: Incomplete
    local_path: Incomplete
    top_path: Incomplete
    package_path: Incomplete
    path_in_package: Incomplete
    list_keys: Incomplete
    dict_keys: Incomplete
    extra_keys: Incomplete
    options: Incomplete
    setup_name: Incomplete
    def __init__(
        self,
        package_name: Incomplete | None = None,
        parent_name: Incomplete | None = None,
        top_path: Incomplete | None = None,
        package_path: Incomplete | None = None,
        caller_level: int = 1,
        setup_name: str = "setup.py",
        **attrs: Incomplete,
    ) -> None: ...
    def todict(self) -> Incomplete: ...
    def info(self, message: str) -> None: ...
    def warn(self, message: str) -> None: ...
    def set_options(self, **options: Incomplete) -> None: ...
    def get_distribution(self) -> Incomplete: ...
    def _wildcard_get_subpackage(self, subpackage_name: str, parent_name: str, caller_level: int = 1) -> Incomplete: ...
    def _get_configuration_from_setup_py(
        self,
        setup_py: Incomplete,
        subpackage_name: str,
        subpackage_path: Incomplete,
        parent_name: str,
        caller_level: int = 1,
    ) -> Incomplete: ...
    def get_subpackage(
        self,
        subpackage_name: str,
        subpackage_path: Incomplete | None = None,
        parent_name: Incomplete | None = None,
        caller_level: int = 1,
    ) -> Incomplete: ...
    def add_subpackage(
        self, subpackage_name: str, subpackage_path: Incomplete | None = None, standalone: bool = False
    ) -> None: ...
    def add_data_dir(self, data_path: Incomplete) -> Incomplete: ...
    def add_data_files(self, *files: Incomplete) -> None: ...
    def add_define_macros(self, macros: Incomplete) -> None: ...
    def add_include_dirs(self, *paths: Incomplete) -> None: ...
    def add_headers(self, *files: Incomplete) -> None: ...
    def paths(self, *paths: Incomplete, **kws: Incomplete) -> Incomplete: ...
    def add_extension(self, name: str, sources: Incomplete, **kw: Incomplete) -> Incomplete: ...
    def add_library(self, name: str, sources: Incomplete, **build_info: Incomplete) -> None: ...
    def add_installed_library(
        self, name: str, sources: Incomplete, install_dir: Incomplete, build_info: Incomplete | None = None
    ) -> None: ...
    def add_npy_pkg_config(
        self, template: str, install_dir: Incomplete, subst_dict: Incomplete | None = None
    ) -> None: ...
    def add_scripts(self, *files: Incomplete) -> None: ...
    def dict_append(self, **dict: Incomplete) -> None: ...
    def get_config_cmd(self) -> Incomplete: ...
    def get_build_temp_dir(self) -> Incomplete: ...
    def have_f77c(self) -> Incomplete: ...
    def have_f90c(self) -> Incomplete: ...
    def append_to(self, extlib: Incomplete) -> None: ...
    def get_version(
        self, version_file: Incomplete | None = None, version_variable: Incomplete | None = None
    ) -> Incomplete: ...
    def make_svn_version_py(self, delete: bool = True) -> Incomplete: ...
    def make_hg_version_py(self, delete: bool = True) -> Incomplete: ...
    def make_config_py(self, name: str = "__config__") -> None: ...
    def get_info(self, *names: str) -> Incomplete: ...

def get_cmd(cmdname: str, _cache: dict[Incomplete, Incomplete] = {}) -> Incomplete: ...
def get_numpy_include_dirs() -> Incomplete: ...
def get_pkg_info(pkgname: str, dirs: Incomplete | None = None) -> Incomplete: ...
def get_info(pkgname: str, dirs: Incomplete | None = None) -> Incomplete: ...
def default_config_dict(
    name: Incomplete | None = None, parent_name: Incomplete | None = None, local_path: Incomplete | None = None
) -> Incomplete: ...
def dict_append(d: Incomplete, **kws: Incomplete) -> None: ...
def appendpath(prefix: str, path: Incomplete) -> Incomplete: ...
def generate_config_py(target: Incomplete) -> Incomplete: ...
def get_build_architecture() -> Incomplete: ...
def sanitize_cxx_flags(cxxflags: Incomplete) -> Incomplete: ...
def exec_mod_from_location(modname: str, modfile: Incomplete) -> Incomplete: ...
