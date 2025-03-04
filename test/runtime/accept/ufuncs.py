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
