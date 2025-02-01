# ensure that mypy uses `numpy-stubs`, as opposed to the bundle `numpy` stubs.
# in `uv` mypy only works if run as e.g.:
# ```
# uv run
#   --isolated
#   --no-ediitable
#   --refresh-package=numtype
#   mypy
#   test/static/stubs_exist.py
# ```

from typing import Literal
from typing_extensions import assert_type

import numpy._numtype

assert_type(numpy._numtype.TARGET, Literal["2.2.2"])
