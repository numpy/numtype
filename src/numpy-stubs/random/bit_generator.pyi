import abc
from collections.abc import Callable, Mapping, Sequence
from threading import Lock
from typing import (
    Any,
    Literal,
    NamedTuple,
    TypeAlias,
    TypeVar,
    TypedDict,
    overload,
    type_check_only,
)

import numpy as np
from numpy._typing import NDArray, _ArrayLikeInt_co, _DTypeLike, _ShapeLike, _UInt32Codes, _UInt64Codes

_T = TypeVar("_T")

_DTypeLikeUint32: TypeAlias = _DTypeLike[np.uint32] | _UInt32Codes
_DTypeLikeUint64: TypeAlias = _DTypeLike[np.uint64] | _UInt64Codes

@type_check_only
class _SeedSeqState(TypedDict):
    entropy: int | Sequence[int] | None
    spawn_key: tuple[int, ...]
    pool_size: int
    n_children_spawned: int

@type_check_only
class _Interface(NamedTuple):
    state_address: Any
    state: Any
    next_uint64: Any
    next_uint32: Any
    next_double: Any
    bit_generator: Any

class ISeedSequence(abc.ABC):
    @abc.abstractmethod
    def generate_state(
        self, n_words: int, dtype: _DTypeLikeUint32 | _DTypeLikeUint64 = ...
    ) -> NDArray[np.uint32 | np.uint64]: ...

class ISpawnableSeedSequence(ISeedSequence):
    @abc.abstractmethod
    def spawn(self: _T, n_children: int) -> list[_T]: ...

class SeedlessSeedSequence(ISpawnableSeedSequence):
    def generate_state(
        self, n_words: int, dtype: _DTypeLikeUint32 | _DTypeLikeUint64 = ...
    ) -> NDArray[np.uint32 | np.uint64]: ...
    def spawn(self: _T, n_children: int) -> list[_T]: ...

class SeedSequence(ISpawnableSeedSequence):
    entropy: int | Sequence[int] | None
    spawn_key: tuple[int, ...]
    pool_size: int
    n_children_spawned: int
    pool: NDArray[np.uint32]
    def __init__(
        self,
        entropy: int | Sequence[int] | _ArrayLikeInt_co | None = ...,
        *,
        spawn_key: Sequence[int] = ...,
        pool_size: int = ...,
        n_children_spawned: int = ...,
    ) -> None: ...
    @property
    def state(self) -> _SeedSeqState: ...
    def generate_state(
        self, n_words: int, dtype: _DTypeLikeUint32 | _DTypeLikeUint64 = ...
    ) -> NDArray[np.uint32 | np.uint64]: ...
    def spawn(self, n_children: int) -> list[SeedSequence]: ...

class BitGenerator(abc.ABC):
    lock: Lock
    def __init__(self, seed: _ArrayLikeInt_co | SeedSequence | None = ...) -> None: ...
    def __getstate__(self) -> tuple[dict[str, Any], ISeedSequence]: ...
    def __setstate__(self, state_seed_seq: dict[str, Any] | tuple[dict[str, Any], ISeedSequence]) -> None: ...
    def __reduce__(self) -> tuple[Callable[[str], BitGenerator], tuple[str], tuple[dict[str, Any], ISeedSequence]]: ...
    @abc.abstractmethod
    @property
    def state(self) -> Mapping[str, Any]: ...
    @state.setter
    def state(self, value: Mapping[str, Any], /) -> None: ...
    @property
    def seed_seq(self) -> ISeedSequence: ...
    def spawn(self, n_children: int) -> list[BitGenerator]: ...
    @overload
    def random_raw(self, size: None = ..., output: Literal[True] = ...) -> int: ...
    @overload
    def random_raw(self, size: _ShapeLike = ..., output: Literal[True] = ...) -> NDArray[np.uint64]: ...
    @overload
    def random_raw(self, size: _ShapeLike | None = ..., output: Literal[False] = ...) -> None: ...
    def _benchmark(self, cnt: int, method: str = ...) -> None: ...
    @property
    def ctypes(self) -> _Interface: ...
    @property
    def cffi(self) -> _Interface: ...
