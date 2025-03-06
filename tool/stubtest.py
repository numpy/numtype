# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numtype[numpy]",
#     "mypy[faster-cache]>=1.15.0",  # keep in sync with pyproject.toml
#     "PyInstaller",
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
ROOT_SITE_DIR = next((ROOT_DIR / ".venv" / "lib").glob("*/site-packages"))

ALLOWLISTS = [
    ".mypyignore.txt",
    ".mypyignore-todo.txt",
    ".mypyignore-gt312.txt" if sys.version_info >= (3, 12) else ".mypyignore-lt312.txt",
]


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
        raise NotADirectoryError(f"{package} does not exist")  # noqa: TRY003

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
    args_extra = sys.argv[1:]

    if not any("--mypy-config-file" in arg for arg in args_extra):
        config_path = (ROOT_DIR / "pyproject.toml").relative_to(CWD)
        cmd.extend(("--mypy-config-file", str(config_path)))

    if not any("--allowlist" in arg for arg in args_extra):
        for allowlist_name in ALLOWLISTS:
            allowlist_path = (TOOL_DIR / allowlist_name).relative_to(CWD)
            cmd.extend(["--allowlist", str(allowlist_path)])

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
