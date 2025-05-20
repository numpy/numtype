from collections.abc import Sequence
from typing import SupportsIndex, TypeAlias

# TODO(jorenham): https://github.com/numpy/numtype/issues/565

# Anything that can be coerced to a shape tuple
_ShapeLike: TypeAlias = SupportsIndex | Sequence[SupportsIndex]  # noqa: PYI047
