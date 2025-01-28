import numpy as np

with open("file.txt", encoding="utf-8") as f:
    np.memmap(f)  # E: No overload variant
np.memmap("test.txt", shape=[10, 5])  # E: No overload variant
