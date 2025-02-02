# Ensure that mypy uses `numpy-stubs`, as opposed to the bundle `numpy` stubs.
# in `uv` mypy only works.
# To verify this, run `tool/my.py test/static/sanity`.

from typing import Literal
from typing_extensions import assert_type

import numpy._numtype

assert_type(numpy._numtype.TARGET, Literal["2.2.2"])
