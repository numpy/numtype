from collections.abc import Callable

import numpy as np

np.sin(1)
np.sin([1, 2, 3])
np.sin(1, out=np.empty(1))
np.matmul(np.ones((2, 2, 2)), np.ones((2, 2, 2)), axes=[(0, 1), (0, 1), (0, 1)])
np.sin(1, signature="D->D")
# NOTE: `np.generic` subclasses are not guaranteed to support addition;
# re-enable this we can infer the exact return type of `np.sin(...)`.
#
# np.sin(1) + np.sin(1)
np.sin.types[0]
np.sin.__name__
np.sin.__doc__

np.abs(np.array([1]))


u11: np.ufunc = np.log
u11_alias: np.ufunc = np.abs
u12: np.ufunc = np.modf
u21: np.ufunc = np.gcd
u22: np.ufunc = np.divmod
gu21: np.ufunc = np.matmul

f11: Callable[..., object] = np.log
f11_alias: Callable[..., object] = np.abs
f12: Callable[..., object] = np.modf
f21: Callable[..., object] = np.gcd
f22: Callable[..., object] = np.divmod
gf21: Callable[..., object] = np.matmul

c11: Callable[..., object] = np.log.__call__
c11_alias: Callable[..., object] = np.abs.__call__
c12: Callable[..., object] = np.modf.__call__
c21: Callable[..., object] = np.gcd.__call__
c22: Callable[..., object] = np.divmod.__call__
gc21: Callable[..., object] = np.matmul.__call__
