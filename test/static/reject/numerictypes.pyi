import numpy as np

np.isdtype(1, np.int64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.issubdtype(1, np.int64)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
