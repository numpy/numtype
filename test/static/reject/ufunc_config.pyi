import numpy as np

class Write1:
    def write1(self, a: str) -> None: ...

class Write2:
    def write(self, a: str, b: str) -> None: ...

class Write3:
    def write(self, *, a: str) -> None: ...

def func1(a: str, b: int, c: float) -> None: ...
def func2(a: str, *, b: int) -> None: ...

###

np.seterrcall(func1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.seterrcall(func2)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.seterrcall(Write1())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.seterrcall(Write2())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.seterrcall(Write3())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
