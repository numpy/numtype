#!/usr/bin/env python

"""Run basedmypy, so that uses `numpy-stubs` instead of numpy's own stubs."""

import subprocess
import sys
from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent.resolve()


def _main(*args: str) -> int:
    uv_cmd: list[str] = [
        "uv",
        "run",
        "--frozen",
        "--isolated",
        "--no-editable",
        f"--directory={PROJECT_PATH}",
        "--refresh-package=numtype",
    ]
    mypy_cmd: list[str] = [
        "mypy",
        "--hide-error-context",
        "--hide-error-code-links",
        "--no-pretty",
        "--explicit-package-bases",
        "--tb",
    ]

    if not args or all(arg.startswith("-") for arg in args):
        mypy_cmd.append(".")
    else:
        mypy_cmd.extend(args)

    print(*uv_cmd)
    print(*mypy_cmd)

    return subprocess.call(uv_cmd + mypy_cmd)


if __name__ == "__main__":
    sys.exit(_main(*sys.argv[1:]))
