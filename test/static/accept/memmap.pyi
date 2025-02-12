from typing import Any, Literal
from typing_extensions import assert_type

import numpy as np

memmap_obj: np.memmap[Any, np.dtype[np.str_]]

assert_type(np.memmap.__array_priority__, float)
assert_type(memmap_obj.__array_priority__, float)
assert_type(memmap_obj.filename, str | None)
assert_type(memmap_obj.offset, int)
assert_type(memmap_obj.mode, Literal["r", "c", "r+", "w+"])
assert_type(memmap_obj.flush(), None)

assert_type(np.memmap("file.txt", offset=5), np.memmap[Any, np.dtype[np.uint8]])
assert_type(np.memmap(b"file.txt", dtype=np.float64, shape=(10, 3)), np.memmap[Any, np.dtype[np.float64]])
with open("file.txt", "rb") as f:
    assert_type(np.memmap(f, dtype=float, order="K"), np.memmap)
    assert_type(np.memmap(f, dtype=np.float16), np.memmap[Any, np.dtype[np.float16]])
    assert_type(np.memmap(f, dtype=np.dtypes.StringDType()), np.memmap[Any, np.dtypes.StringDType])
