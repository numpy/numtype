import numpy as np

m: np.ma.MaskedArray[tuple[int], np.dtype[np.float64]]

m.shape = (3, 1)  # type: ignore[assignment]
m.dtype = np.bool  # type: ignore[assignment]  # pyright: ignore[reportAttributeAccessIssue]
