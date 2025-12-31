import numpy as np
import numtype as nt


def test_version() -> None:
    assert nt.__version__.startswith(np.__version__.split("rc")[0])
