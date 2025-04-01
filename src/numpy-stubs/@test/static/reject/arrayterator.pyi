import numpy as np
import numpy.typing as npt

AR_i8: npt.NDArray[np.int64]
ar_iter = np.lib.Arrayterator(AR_i8)

np.lib.Arrayterator(np.int64())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
ar_iter.shape = (10, 5)  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue]
ar_iter[None]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
ar_iter[None, 1]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
ar_iter[np.intp()]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
ar_iter[np.intp(), ...]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
ar_iter[AR_i8]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
ar_iter[AR_i8, :]  # type: ignore[index]  # pyright: ignore[reportArgumentType]
