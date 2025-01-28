from typing import Any

import numpy as np

# test bounds of _ShapeType_co

np.ndarray[tuple[str, str], Any]  # type: ignore[type-var]  # pyright: ignore[reportInvalidTypeArguments]
