import numtype as nt
import pytest

import numpy as np
import numpy.typing as npt


def test_superset() -> None:
    assert set(nt.__all__) > set(npt.__all__)


@pytest.mark.parametrize("name", npt.__all__)
def test_reexport(name: str) -> None:
    assert getattr(nt, name) is getattr(npt, name)


def test_version() -> None:
    assert nt.__version__.startswith(np.__version__)
