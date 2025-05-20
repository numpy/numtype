"""
Delete all `__init__.pyi` files in the `numpy` site-packages directory.

This is a workaround for https://github.com/python/mypy/issues/18997 on `mypy<1.16.0`

Run with `uv run tool/unstub.py`.
"""

import sysconfig
from pathlib import Path

package = Path(sysconfig.get_paths()["purelib"]) / "numpy"
assert package.is_dir(), package

bodycount = sum(not pyi.unlink() for pyi in package.rglob("__init__.pyi"))  # type: ignore[func-returns-value]
print(f"{bodycount} files deleted from {package.relative_to(Path.cwd())}")
