import importlib
import sys
from pathlib import Path

import pytest

TEST_DIR = Path(__file__).parent
sys.path.insert(0, str(TEST_DIR))


@pytest.mark.parametrize(
    "module",
    [
        path.stem
        for path in (Path(__file__).parent / "legacy").iterdir()
        if path.suffix == ".py" and path.stem != "__init__"
    ],
    ids="test/runtime/legacy/{}.py".format,
)
def test_legacy(module: str) -> None:
    importlib.import_module(f"legacy.{module}")
