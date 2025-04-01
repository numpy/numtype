from collections.abc import Sequence

from numpy._typing import _NestedSequence

a: Sequence[float]
b: list[complex]
c: tuple[str, ...]
d: int
e: str

def func(a: _NestedSequence[int]) -> None: ...

func(a)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
func(b)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
func(c)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
func(d)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
func(e)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
