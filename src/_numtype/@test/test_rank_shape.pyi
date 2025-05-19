from typing import assert_type

import _numtype as _nt

# TODO: remove the `# type: ignore`s once python/mypy#19110 is fixed

a0: _nt.Array0D
assert_type(a0.__inner_shape__, _nt.Rank0)
assert_type(a0.shape, _nt.Shape0)  # type: ignore[assert-type]

a1: _nt.Array1D
assert_type(a1.__inner_shape__, _nt.Rank1)
assert_type(a1.shape, _nt.Shape1)  # type: ignore[assert-type]

a2: _nt.Array2D
assert_type(a2.__inner_shape__, _nt.Rank2)
assert_type(a2.shape, _nt.Shape2)  # type: ignore[assert-type]

a3: _nt.Array3D
assert_type(a3.__inner_shape__, _nt.Rank3)
assert_type(a3.shape, _nt.Shape3)  # type: ignore[assert-type]

a4: _nt.Array4D
assert_type(a4.__inner_shape__, _nt.Rank4)
assert_type(a4.shape, _nt.Shape4)  # type: ignore[assert-type]
