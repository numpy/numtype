"""A superset of `numpy.typing`. Will be expanded in the future."""

from numpy.typing import ArrayLike, DTypeLike, NDArray  # noqa: ICN003

from .version import __version__

__all__ = ["ArrayLike", "DTypeLike", "NDArray", "__version__"]
