# NOTE: In reality these functions are not aliases but distinct functions with identical signatures.
from numpy._core.fromnumeric import (
    amax as nanmax,
    amin as nanmin,
    argmax as nanargmax,
    argmin as nanargmin,
    cumprod as nancumprod,
    cumsum as nancumsum,
    mean as nanmean,
    prod as nanprod,
    std as nanstd,
    sum as nansum,
    var as nanvar,
)
from numpy.lib._function_base_impl import median as nanmedian, percentile as nanpercentile, quantile as nanquantile

__all__ = [
    "nanargmax",
    "nanargmin",
    "nancumprod",
    "nancumsum",
    "nanmax",
    "nanmean",
    "nanmedian",
    "nanmin",
    "nanpercentile",
    "nanprod",
    "nanquantile",
    "nanstd",
    "nansum",
    "nanvar",
]
