from threading import Lock

import numpy as np
import numpy.typing as npt
from numpy._typing import _ArrayLikeInt_co
from numpy.random.bit_generator import BitGenerator

__all__: list[str] = []

#
def _gen_mask(max_val: np.uint64) -> np.uint64: ...

#
def _rand_uint64(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> npt.NDArray[np.uint64]: ...
def _rand_uint32(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> npt.NDArray[np.uint32]: ...
def _rand_uint16(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.uint16 | npt.NDArray[np.uint16]: ...
def _rand_uint8(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.uint8 | npt.NDArray[np.uint8]: ...
def _rand_bool(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.bool_ | npt.NDArray[np.bool_]: ...
def _rand_int64(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.int64 | npt.NDArray[np.int64]: ...
def _rand_int32(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.int32 | npt.NDArray[np.int32]: ...
def _rand_int16(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.int16 | npt.NDArray[np.int16]: ...
def _rand_int8(
    low: int | _ArrayLikeInt_co,
    high: int | _ArrayLikeInt_co | None = None,
    size: int | tuple[int, ...] | None = None,
    use_masked: bool = True,
    closed: bool = True,
    state: BitGenerator = ...,
    lock: Lock = ...,
) -> np.int8 | npt.NDArray[np.int8]: ...
