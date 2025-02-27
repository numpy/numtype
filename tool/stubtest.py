# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numtype[numpy]",
#
#     # Keep in sync with pyproject.toml
#     "mypy[faster-cache]>=1.15.0",
#
#     # numpy dev dependencies
#     "pytest>=8.3.4",
#     "hypothesis>=6.127.2",
#     "pyinstaller==6.12.0",
# ]
#
# [tool.uv]
# reinstall-package = ["numtype"]
#
# [tool.uv.sources]
# numtype = {path = ".."}
# ///

"""Usage: `uv run tool/stubtest.py <OPTIONS>`."""

# ruff: noqa: ERA001, TRY003

import os
import subprocess
import sys
import sysconfig
from pathlib import Path

VERBOSE = True

CWD = Path.cwd()
BASE_DIR = Path(__file__).parent.parent
SITE_DIR = Path(sysconfig.get_paths()["purelib"])


def __get_local_site_dir() -> Path:
    lib = BASE_DIR / ".venv" / "lib"
    if not lib.is_dir():
        raise NotADirectoryError(f"{lib} does not exist")

    for out in lib.glob("*/site-packages"):
        return out

    raise NotADirectoryError(f"Could not find {lib}/**/site-packages")


SITE_DIR_LOCAL = __get_local_site_dir()


def __commit_pyi_genocide_for_mypy() -> None:
    """
    Remove the ``py.typed`` and all ``*.pyi`` files from the installed numpy package.

    Raises
    ------
    NotADirectoryError
        If `numpy` does not exist in the site-packages.
    """
    package = SITE_DIR / "numpy"
    if not package.is_dir():
        raise NotADirectoryError(f"{package} does not exist")

    py_typed = package / "py.typed"
    if py_typed.is_file():
        py_typed.unlink()
        if VERBOSE:
            print(f"deleted {py_typed} (1)")

    graveyard_size = sum(not pyi.unlink() for pyi in package.rglob("*.pyi"))  # type: ignore[func-returns-value]
    if VERBOSE and graveyard_size:
        print(f"deleted {package}/**/*.pyi ({graveyard_size})\n")


def _stubtest_command() -> list[str]:
    cmd = ["stubtest"]

    if "--mypy-config-file" not in sys.argv:
        config_path = BASE_DIR / "pyproject.toml"
        assert config_path.is_file(), config_path

        cmd.extend(("--mypy-config-file", str(config_path)))

    if len(sys.argv) > 1:
        cmd.extend(sys.argv[1:])
    else:
        cmd.extend(["--allowlist", str(BASE_DIR / ".mypyignore")])
        cmd.extend(["--allowlist", str(BASE_DIR / ".mypyignore-todo")])

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
    line = line.replace(b"typing.Sequence", b"")

    if len(line.strip()) <= len(str(SITE_DIR)):
        return line

    for package_name in ("_numtype", "numpy-stubs", "numtype"):
        package_lib = str(SITE_DIR / package_name).encode()
        package_src = str((BASE_DIR / "src" / package_name).relative_to(CWD)).encode()
        if package_lib in line:
            line = line.replace(package_lib, package_src)

    site_dir = str(SITE_DIR).encode()
    if site_dir in line:
        line = line.replace(site_dir, str(SITE_DIR_LOCAL.relative_to(CWD)).encode())

    return line


def main() -> int:
    """
    Run stubtest.

    Returns
    -------
    exit_code : int
    """
    __commit_pyi_genocide_for_mypy()

    cmd = _stubtest_command()
    if VERBOSE and "--generate-allowlist" not in cmd:
        print(*cmd)

    result = subprocess.run(
        cmd,
        check=False,
        capture_output=True,
        env={"FORCE_COLOR": "1"} | os.environ,
    )
    output = _rewrite_mypy_output(result.stdout)
    sys.stdout.buffer.write(output)
    sys.stdout.buffer.flush()

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
