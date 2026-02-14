import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # ruff should be optional during type-checking
    def find_ruff_bin() -> str: ...

else:
    # see https://github.com/astral-sh/ruff/pull/18224
    from ruff.__main__ import find_ruff_bin  # type: ignore[import-untyped]


def ruff_format(source: str) -> str:
    result = subprocess.run(
        [find_ruff_bin(), "format", "-"],
        input=source,
        text=True,
        capture_output=True,
        check=True,
        cwd=Path.cwd(),
    )
    result.check_returncode()
    return result.stdout
