from typing import assert_type

import numpy as np
import numpy.polynomial as npp
from numpy._pytesttester import PytestTester

assert_type(np.__file__, str)
assert_type(np.char.__file__, str)
assert_type(np.ctypeslib.__file__, str)
assert_type(np.emath.__file__, str)
assert_type(np.fft.__file__, str)
assert_type(np.lib.__file__, str)
assert_type(np.linalg.__file__, str)
assert_type(np.ma.__file__, str)
assert_type(np.matrixlib.__file__, str)
assert_type(np.polynomial.__file__, str)
assert_type(np.random.__file__, str)
assert_type(np.rec.__file__, str)
assert_type(np.testing.__file__, str)
assert_type(np.version.__file__, str)
assert_type(np.exceptions.__file__, str)
assert_type(np.dtypes.__file__, str)

assert_type(np.lib.format.__file__, str)
assert_type(np.lib.mixins.__file__, str)
assert_type(np.lib.scimath.__file__, str)
assert_type(np.lib.stride_tricks.__file__, str)
assert_type(np.ma.extras.__file__, str)
assert_type(npp.chebyshev.__file__, str)
assert_type(npp.hermite.__file__, str)
assert_type(npp.hermite_e.__file__, str)
assert_type(npp.laguerre.__file__, str)
assert_type(npp.legendre.__file__, str)
assert_type(npp.polynomial.__file__, str)

assert_type(np.test, PytestTester)
assert_type(np.test.module_name, str)

assert_type(np.__all__, list[str])
assert_type(np.char.__all__, list[str])
assert_type(np.ctypeslib.__all__, list[str])
assert_type(np.emath.__all__, list[str])
assert_type(np.lib.__all__, list[str])
assert_type(np.ma.__all__, list[str])
assert_type(np.random.__all__, list[str])
assert_type(np.rec.__all__, list[str])
assert_type(np.testing.__all__, list[str])
assert_type(np.f2py.__all__, list[str])
