import pathlib
from typing import IO

import _numtype as _nt
import numpy as np

str_path: str
bytes_path: bytes
pathlib_path: pathlib.Path
str_file: IO[str]
AR_i8: _nt.Array[np.int64]

np.save(bytes_path, AR_i8)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType]
np.savez(bytes_path, AR_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.savez_compressed(bytes_path, AR_i8)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.load(str_file)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.loadtxt(bytes_path)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.fromregex(bytes_path, ".", np.int64)  # type: ignore[call-overload]  # pyright: ignore[reportArgumentType, reportCallIssue]
