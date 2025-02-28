"""
Delete all `.pyi` files in the `numpy` site-packages directory.

Run with `uv run tool/unstub.py`.
"""

import sysconfig
from pathlib import Path

package = Path(sysconfig.get_paths()["purelib"]) / "numpy"
assert package.is_dir(), package

(package / "py.typed").unlink(missing_ok=True)
bodycount = sum(not pyi.unlink() for pyi in package.rglob("*.pyi"))  # type: ignore[func-returns-value]
print(f"{bodycount} files deleted from {package.relative_to(Path.cwd())}/**/*.pyi")
