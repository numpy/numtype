"""Run basedmypy, so that uses `numpy-stubs` instead of numpy's own stubs."""

# ruff: noqa: T201, S603, S404, D103, DOC201

import subprocess
import sys
from pathlib import Path

PROJECT_PATH = Path(__file__).parent.parent.resolve()


def _call_static(args: list[str], *base_cmd: str) -> int:
    if not args or all(arg.startswith("-") for arg in args):  # noqa: SIM108
        cmd = [*base_cmd, *args, "static"]
    else:
        cmd = [*base_cmd, *args]

    print(*cmd)
    return subprocess.call(cmd)


def _static_bmp(args: list[str], /) -> int:
    return _call_static(
        args,
        "mypy",
        "--explicit-package-bases",
        "--hide-error-context",
        "--hide-error-code-links",
        "--no-pretty",
        "--tb",
        "--config-file=../pyproject.toml",
    )


def _static_bpr(args: list[str], /) -> int:
    return _call_static(args, "basedpyright", "--project=../")


def static(args: list[str] | None = None, /) -> int:
    if args is None:
        args = sys.argv[1:]
    if args:
        if args[0] == "all":
            return _static_bpr(args[1:]) or _static_bmp(args[1:])
        if args[0] == "bpr":
            return _static_bpr(args[1:])
        if args[0] == "bmp":
            return _static_bmp(args[1:])

    print("Usage: uv run test static [<COMMAND> [OPTIONS]]")
    print()
    print("Commands:")
    print("  all", "Run all static tests", sep="\t")
    print("  bpr", "Run basedpyright", sep="\t")
    print("  bmp", "Run basedmypy", sep="\t")
    return 1


def main(args: list[str] | None = None, /) -> int:
    if args is None:
        args = sys.argv[1:]
    if not args or args[0] != "static":
        print("Usage: uv run test <COMMAND>")
        print()
        print("Commands:")
        print("  static", "Static type-testing", sep="\t")
        return 1

    return static(args[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
