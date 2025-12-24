"""Base on the `if __name__ == "__main__"` test code in `lib/_user_array_impl.py`."""

from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from numpy.lib.user_array import container  # pyright: ignore[reportDeprecated]

if TYPE_CHECKING:
    import _numtype as _nt

N = 10_000
W = H = int(N**0.5)

a: _nt.Array2D[np.int32]
ua: container[_nt.Rank2, np.dtype[np.int32]]  # pyright: ignore[reportDeprecated]

a = np.arange(N, dtype=np.int32).reshape(W, H)
ua = container(a)  # pyright: ignore[reportDeprecated]

ua_small: container[_nt.Rank2, np.dtype[np.int32]] = ua[:3, :5]  # pyright: ignore[reportDeprecated]
ua_small[0, 0] = 10

ua_bool: container[_nt.Rank2, np.dtype[np.bool]] = ua_small > 1  # pyright: ignore[reportDeprecated]

shape: tuple[int, int] = np.shape(ua)
