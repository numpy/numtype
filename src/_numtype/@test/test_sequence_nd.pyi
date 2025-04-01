import _numtype as _nt

class A: ...

a0d: A
a1d: list[A]
a2d: list[list[A]]
a3d: list[list[list[A]]]
a4d: list[list[list[list[A]]]]

###

a1nd__a_0d: _nt.Sequence1ND[A] = a0d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
a1nd__a_1d: _nt.Sequence1ND[A] = a1d
a1nd__a_2d: _nt.Sequence1ND[A] = a2d
a1nd__a_3d: _nt.Sequence1ND[A] = a3d
a1nd__a_4d: _nt.Sequence1ND[A] = a4d
