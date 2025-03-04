from collections.abc import Callable
from typing_extensions import deprecated

__all__ = ["MachAr"]

@deprecated("deprecated in numpy 1.22")
class MachAr:
    ibeta: int
    it: int
    machep: int
    eps: float
    negep: int
    epsneg: float
    iexp: int
    minexp: int
    xmin: float
    maxexp: int
    xmax: float
    irnd: int
    ngrd: int
    epsilon: float
    tiny: float
    huge: float
    precision: float
    resolution: float
    smallest_normal: float
    smallest_subnormal: float
    title: str | None

    def __init__(
        self,
        /,
        float_conv: Callable[[int], float] = ...,
        int_conv: Callable[[float], int] = ...,
        float_to_float: Callable[[float], float] = ...,
        float_to_str: Callable[[float], str] = ...,
        title: str = "Python floating point number",
    ) -> None: ...
