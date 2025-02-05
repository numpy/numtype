# /// script
# dependencies = [
#     "numtype",
#     # "basedmypy[faster-cache]",
#     "mypy[faster-cache]",
#     "pytest",  # imported in test/runtime
# ]
#
# [tool.uv]
# reinstall-package = ["numtype"]
#
# [tool.uv.sources]
# numtype = {path = ".."}
# ///

"""
Usage: `uv run test/mypy.py <OPTIONS>`
"""

import subprocess
import sys
from pathlib import Path

TEST_DIR = Path(__file__).parent
CWD = Path.cwd()


cmd = ["mypy"]

if TEST_DIR.parent != CWD and "--config-file" not in sys.argv:
    config_path = TEST_DIR.parent / "pyproject.toml"
    try:  # noqa: SIM105
        config_path = config_path.relative_to(CWD)
    except ValueError:
        pass

    cmd.extend(("--config-file", str(config_path)))

if len(sys.argv) > 1 or any(not arg.lstrip().startswith("-") for arg in sys.argv[1:]):
    cmd.extend(sys.argv[1:])
else:
    cmd.append("--explicit-package-bases")  # avoids submodule name clashes
    cmd.extend(sys.argv[1:])
    cmd.append(str(TEST_DIR.relative_to(CWD)))


if "--ide" not in sys.argv:
    print(*cmd)

sys.exit(subprocess.call(cmd))
