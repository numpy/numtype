import numpy as np

with open("file.txt", encoding="utf-8") as f:
    np.memmap(f)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]

np.memmap("test.txt", shape=[10, 5])  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
