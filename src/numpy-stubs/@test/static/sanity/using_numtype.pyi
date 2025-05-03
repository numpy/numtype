# Ensure that mypy uses `numpy-stubs`, as opposed to the bundle `numpy` stubs.
# in `uv` mypy only works.
# To verify this, run `uv run --directory test static static/sanity`.

from typing import Literal, assert_type

import numpy as np

assert_type(np.__numtype__, Literal[True])
