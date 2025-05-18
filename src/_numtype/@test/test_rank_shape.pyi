from typing import assert_type

import _numtype as _nt

a0: _nt.Array0D
assert_type(a0.__inner_shape__, _nt.Rank0)
r0: _nt.Rank0 = a0.shape  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0: _nt.Shape0 = a0.shape

a1: _nt.Array1D
assert_type(a1.__inner_shape__, _nt.Rank1)
r1: _nt.Rank1 = a1.shape  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1: _nt.Shape1 = a1.shape

a2: _nt.Array2D
assert_type(a2.__inner_shape__, _nt.Rank2)
r2: _nt.Rank2 = a2.shape  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2: _nt.Shape2 = a2.shape

a3: _nt.Array3D
assert_type(a3.__inner_shape__, _nt.Rank3)
r3: _nt.Rank3 = a3.shape  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3: _nt.Shape3 = a3.shape

a4: _nt.Array4D
assert_type(a4.__inner_shape__, _nt.Rank4)
r4: _nt.Rank4 = a4.shape  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4: _nt.Shape4 = a4.shape
