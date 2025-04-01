import pytest

import numpy as np
import numpy.typing as npt
import numtype as nt

NPT_DIR = tuple(k for k in npt.__all__ if k != "NBitBase")


def test_superset() -> None:
    assert set(nt.__all__) > set(NPT_DIR)


@pytest.mark.parametrize("name", NPT_DIR)
def test_reexport(name: str) -> None:
    assert getattr(nt, name) is getattr(npt, name)


def test_version() -> None:
    assert nt.__version__.startswith(np.__version__)
