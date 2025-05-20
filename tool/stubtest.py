# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numtype[numpy]",
#     "mypy[faster-cache]>=1.15.0",  # keep in sync with pyproject.toml
#
#     "PyInstaller",
#     "hypothesis",
#     "pytest",
#     "types-setuptools",
# ]
#
# [tool.uv]
# reinstall-package = ["numtype"]
#
# [tool.uv.sources]
# numtype = {path = ".."}
# ///

"""Usage: `uv run tool/stubtest.py <OPTIONS>`."""

import os
import subprocess
import sys
import sysconfig
from pathlib import Path

VERBOSE = True

CWD = Path.cwd()
TOOL_DIR = Path(__file__).parent
SITE_DIR = Path(sysconfig.get_paths()["purelib"])

ROOT_DIR = TOOL_DIR.parent
__root_site: Path | None
if (ROOT_DIR / ".venv").is_dir():
    __root_venv = ROOT_DIR / ".venv"
    __root_site = (
        __root_venv / "Lib" / "site-packages"
        if sys.platform == "win32"
        else next((__root_venv / "lib").glob("*/site-packages"))
    )
else:
    __root_site = None
ROOT_SITE_DIR = __root_site

ALLOWLISTS = [
    "common.txt",
    ("ge" if sys.version_info >= (3, 12) else "lt") + "-py312.txt",
]

if sys.platform == "win32":
    if sys.version_info[:2] == (3, 12):
        ALLOWLISTS.append("path-py312.txt")
    elif sys.version_info[:2] <= (3, 11):
        ALLOWLISTS.append("path-py311.txt")


def __check_simd() -> None:
    try:
        from numpy._core import _simd  # noqa: PLC0415, PLC2701
    except ImportError:
        return

    if not hasattr(_simd, "AVX512F"):
        ALLOWLISTS.append("simd.txt")


__check_simd()


def __commit_pyi_genocide_for_mypy() -> None:
    """
    Remove all ``__init__.pyi`` files from the installed numpy package.

    This works around https://github.com/python/mypy/issues/18997 on `mypy<1.16.0`.

    Raises
    ------
    NotADirectoryError
        If `numpy` does not exist in the site-packages.
    """
    package = SITE_DIR / "numpy"
    if not package.is_dir():
        raise NotADirectoryError(f"{package} does not exist")

    graveyard_size = sum(not pyi.unlink() for pyi in package.rglob("__init__.pyi"))  # type: ignore[func-returns-value]
    if VERBOSE and graveyard_size:
        print(f"deleted {graveyard_size} __init__.pyi from {package}\n")


def _allowlists() -> list[str]:
    relpath = (TOOL_DIR / "allowlists").relative_to(CWD)
    return [str(relpath / fname) for fname in ALLOWLISTS]


def _stubtest_command() -> list[str]:
    cmd = ["stubtest"]
    args_extra = sys.argv[1:]

    if not any("--mypy-config-file" in arg for arg in args_extra):
        config_path = (ROOT_DIR / "pyproject.toml").relative_to(CWD)
        cmd.extend(("--mypy-config-file", str(config_path)))

    if not any("--allowlist" in arg for arg in args_extra):
        for allowlist in _allowlists():
            cmd.extend(["--allowlist", allowlist])

    cmd.extend(args_extra)
    cmd.append("numpy")

    return cmd


def _rewrite_mypy_output(line: bytes, /) -> bytes:
    """
    Replace the paths with relative local ones that vscode understands.

    Returns
    -------
    str
    """
    line = line.replace(b"builtins.", b"")

    if len(line.strip()) <= len(str(SITE_DIR)):
        return line

    for package_name in ("_numtype", "numpy-stubs", "numtype"):
        package_lib = str(SITE_DIR / package_name).encode()
        package_src = str((ROOT_DIR / "src" / package_name).relative_to(CWD)).encode()
        if package_lib in line:
            line = line.replace(package_lib, package_src)

    if ROOT_SITE_DIR is not None:
        site_dir = str(SITE_DIR).encode()
        if site_dir in line:
            line = line.replace(site_dir, str(ROOT_SITE_DIR.relative_to(CWD)).encode())

    return line


def main() -> int:
    """
    Run stubtest.

    Returns
    -------
    exit_code : int
    """
    __commit_pyi_genocide_for_mypy()

    if VERBOSE:
        import numpy as np  # noqa: PLC0415
        import numtype as nt  # noqa: PLC0415

        print(f"python {sys.version}")
        print(f"numtype {nt.__version__} (numpy {np.__version__})")
        print()

    cmd = _stubtest_command()
    if VERBOSE and "--generate-allowlist" not in cmd:
        print(*cmd)

    result = subprocess.run(
        cmd,
        check=False,
        capture_output=True,
        env={"FORCE_COLOR": "1"} | os.environ,
    )
    for std in "stdout", "stderr":
        stream = getattr(sys, std)
        stream.buffer.write(_rewrite_mypy_output(getattr(result, std)))
        stream.buffer.flush()

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
