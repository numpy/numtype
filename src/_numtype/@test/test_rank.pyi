import _numtype as _nt
from _numtype._rank import _BroadcastableShape, _CanBroadcastTo

###

s0: _nt.Shape0
s1: _nt.Shape1
s2: _nt.Shape2
s3: _nt.Shape3
s4: _nt.Shape4

s0n: _nt.Shape0N
s1n: _nt.Shape1N
s2n: _nt.Shape2N
s3n: _nt.Shape3N
s4n: _nt.Shape4N

r0: _nt.Rank0
r1: _nt.Rank1
r2: _nt.Rank2
r3: _nt.Rank3
r4: _nt.Rank4

r0n: _nt.Rank0N
r1n: _nt.Rank1N
r2n: _nt.Rank2N
r3n: _nt.Rank3N
r4n: _nt.Rank4N

###

s0_r0_u: _CanBroadcastTo[_nt.Shape0] = r0
s0_r1_u: _CanBroadcastTo[_nt.Shape0] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r2_u: _CanBroadcastTo[_nt.Shape0] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r3_u: _CanBroadcastTo[_nt.Shape0] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r4_u: _CanBroadcastTo[_nt.Shape0] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r0_u: _CanBroadcastTo[_nt.Shape1] = r0
s1_r1_u: _CanBroadcastTo[_nt.Shape1] = r1
s1_r2_u: _CanBroadcastTo[_nt.Shape1] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r3_u: _CanBroadcastTo[_nt.Shape1] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r4_u: _CanBroadcastTo[_nt.Shape1] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r0_u: _CanBroadcastTo[_nt.Shape2] = r0
s2_r1_u: _CanBroadcastTo[_nt.Shape2] = r1
s2_r2_u: _CanBroadcastTo[_nt.Shape2] = r2
s2_r3_u: _CanBroadcastTo[_nt.Shape2] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r4_u: _CanBroadcastTo[_nt.Shape2] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r0_u: _CanBroadcastTo[_nt.Shape3] = r0
s3_r1_u: _CanBroadcastTo[_nt.Shape3] = r1
s3_r2_u: _CanBroadcastTo[_nt.Shape3] = r2
s3_r3_u: _CanBroadcastTo[_nt.Shape3] = r3
s3_r4_u: _CanBroadcastTo[_nt.Shape3] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r0_u: _CanBroadcastTo[_nt.Shape4] = r0
s4_r1_u: _CanBroadcastTo[_nt.Shape4] = r1
s4_r2_u: _CanBroadcastTo[_nt.Shape4] = r2
s4_r3_u: _CanBroadcastTo[_nt.Shape4] = r3
s4_r4_u: _CanBroadcastTo[_nt.Shape4] = r4

s0_r0_n: _BroadcastableShape[_nt.Shape0] = r0
s0_r1_n: _BroadcastableShape[_nt.Shape0] = r1
s0_r2_n: _BroadcastableShape[_nt.Shape0] = r2
s0_r3_n: _BroadcastableShape[_nt.Shape0] = r3
s0_r4_n: _BroadcastableShape[_nt.Shape0] = r4
s1_r0_n: _BroadcastableShape[_nt.Shape1] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r1_n: _BroadcastableShape[_nt.Shape1] = r1
s1_r2_n: _BroadcastableShape[_nt.Shape1] = r2
s1_r3_n: _BroadcastableShape[_nt.Shape1] = r3
s1_r4_n: _BroadcastableShape[_nt.Shape1] = r4
s2_r0_n: _BroadcastableShape[_nt.Shape2] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r1_n: _BroadcastableShape[_nt.Shape2] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r2_n: _BroadcastableShape[_nt.Shape2] = r2
s2_r3_n: _BroadcastableShape[_nt.Shape2] = r3
s2_r4_n: _BroadcastableShape[_nt.Shape2] = r4
s3_r0_n: _BroadcastableShape[_nt.Shape3] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r1_n: _BroadcastableShape[_nt.Shape3] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r2_n: _BroadcastableShape[_nt.Shape3] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r3_n: _BroadcastableShape[_nt.Shape3] = r3
s3_r4_n: _BroadcastableShape[_nt.Shape3] = r4
s4_r0_n: _BroadcastableShape[_nt.Shape4] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r1_n: _BroadcastableShape[_nt.Shape4] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r2_n: _BroadcastableShape[_nt.Shape4] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r3_n: _BroadcastableShape[_nt.Shape4] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r4_n: _BroadcastableShape[_nt.Shape4] = r4

###

s0_r0n_u: _CanBroadcastTo[_nt.Shape0] = r0n
s0_r1n_u: _CanBroadcastTo[_nt.Shape0] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r2n_u: _CanBroadcastTo[_nt.Shape0] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r3n_u: _CanBroadcastTo[_nt.Shape0] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r4n_u: _CanBroadcastTo[_nt.Shape0] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r0n_u: _CanBroadcastTo[_nt.Shape1] = r0n
s1_r1n_u: _CanBroadcastTo[_nt.Shape1] = r1n
s1_r2n_u: _CanBroadcastTo[_nt.Shape1] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r3n_u: _CanBroadcastTo[_nt.Shape1] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r4n_u: _CanBroadcastTo[_nt.Shape1] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r0n_u: _CanBroadcastTo[_nt.Shape2] = r0n
s2_r1n_u: _CanBroadcastTo[_nt.Shape2] = r1n
s2_r2n_u: _CanBroadcastTo[_nt.Shape2] = r2n
s2_r3n_u: _CanBroadcastTo[_nt.Shape2] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r4n_u: _CanBroadcastTo[_nt.Shape2] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r0n_u: _CanBroadcastTo[_nt.Shape3] = r0n
s3_r1n_u: _CanBroadcastTo[_nt.Shape3] = r1n
s3_r2n_u: _CanBroadcastTo[_nt.Shape3] = r2n
s3_r3n_u: _CanBroadcastTo[_nt.Shape3] = r3n
s3_r4n_u: _CanBroadcastTo[_nt.Shape3] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r0n_u: _CanBroadcastTo[_nt.Shape4] = r0n
s4_r1n_u: _CanBroadcastTo[_nt.Shape4] = r1n
s4_r2n_u: _CanBroadcastTo[_nt.Shape4] = r2n
s4_r3n_u: _CanBroadcastTo[_nt.Shape4] = r3n
s4_r4n_u: _CanBroadcastTo[_nt.Shape4] = r4n

s0_r0n_n: _BroadcastableShape[_nt.Shape0] = r0n
s0_r1n_n: _BroadcastableShape[_nt.Shape0] = r1n
s0_r2n_n: _BroadcastableShape[_nt.Shape0] = r2n
s0_r3n_n: _BroadcastableShape[_nt.Shape0] = r3n
s0_r4n_n: _BroadcastableShape[_nt.Shape0] = r4n
s1_r0n_n: _BroadcastableShape[_nt.Shape1] = r0n
s1_r1n_n: _BroadcastableShape[_nt.Shape1] = r1n
s1_r2n_n: _BroadcastableShape[_nt.Shape1] = r2n
s1_r3n_n: _BroadcastableShape[_nt.Shape1] = r3n
s1_r4n_n: _BroadcastableShape[_nt.Shape1] = r4n
s2_r0n_n: _BroadcastableShape[_nt.Shape2] = r0n
s2_r1n_n: _BroadcastableShape[_nt.Shape2] = r1n
s2_r2n_n: _BroadcastableShape[_nt.Shape2] = r2n
s2_r3n_n: _BroadcastableShape[_nt.Shape2] = r3n
s2_r4n_n: _BroadcastableShape[_nt.Shape2] = r4n
s3_r0n_n: _BroadcastableShape[_nt.Shape3] = r0n
s3_r1n_n: _BroadcastableShape[_nt.Shape3] = r1n
s3_r2n_n: _BroadcastableShape[_nt.Shape3] = r2n
s3_r3n_n: _BroadcastableShape[_nt.Shape3] = r3n
s3_r4n_n: _BroadcastableShape[_nt.Shape3] = r4n
s4_r0n_n: _BroadcastableShape[_nt.Shape4] = r0n
s4_r1n_n: _BroadcastableShape[_nt.Shape4] = r1n
s4_r2n_n: _BroadcastableShape[_nt.Shape4] = r2n
s4_r3n_n: _BroadcastableShape[_nt.Shape4] = r3n
s4_r4n_n: _BroadcastableShape[_nt.Shape4] = r4n

###

s0n_r0_u: _CanBroadcastTo[_nt.Shape0N] = r0
s0n_r1_u: _CanBroadcastTo[_nt.Shape0N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r2_u: _CanBroadcastTo[_nt.Shape0N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r3_u: _CanBroadcastTo[_nt.Shape0N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r4_u: _CanBroadcastTo[_nt.Shape0N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r0_u: _CanBroadcastTo[_nt.Shape1N] = r0
s1n_r1_u: _CanBroadcastTo[_nt.Shape1N] = r1
s1n_r2_u: _CanBroadcastTo[_nt.Shape1N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r3_u: _CanBroadcastTo[_nt.Shape1N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r4_u: _CanBroadcastTo[_nt.Shape1N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r0_u: _CanBroadcastTo[_nt.Shape2N] = r0
s2n_r1_u: _CanBroadcastTo[_nt.Shape2N] = r1
s2n_r2_u: _CanBroadcastTo[_nt.Shape2N] = r2
s2n_r3_u: _CanBroadcastTo[_nt.Shape2N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r4_u: _CanBroadcastTo[_nt.Shape2N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r0_u: _CanBroadcastTo[_nt.Shape3N] = r0
s3n_r1_u: _CanBroadcastTo[_nt.Shape3N] = r1
s3n_r2_u: _CanBroadcastTo[_nt.Shape3N] = r2
s3n_r3_u: _CanBroadcastTo[_nt.Shape3N] = r3
s3n_r4_u: _CanBroadcastTo[_nt.Shape3N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r0_u: _CanBroadcastTo[_nt.Shape4N] = r0
s4n_r1_u: _CanBroadcastTo[_nt.Shape4N] = r1
s4n_r2_u: _CanBroadcastTo[_nt.Shape4N] = r2
s4n_r3_u: _CanBroadcastTo[_nt.Shape4N] = r3
s4n_r4_u: _CanBroadcastTo[_nt.Shape4N] = r4

s0n_r0_n: _BroadcastableShape[_nt.Shape0N] = r0
s0n_r1_n: _BroadcastableShape[_nt.Shape0N] = r1
s0n_r2_n: _BroadcastableShape[_nt.Shape0N] = r2
s0n_r3_n: _BroadcastableShape[_nt.Shape0N] = r3
s0n_r4_n: _BroadcastableShape[_nt.Shape0N] = r4
s1n_r0_n: _BroadcastableShape[_nt.Shape1N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r1_n: _BroadcastableShape[_nt.Shape1N] = r1
s1n_r2_n: _BroadcastableShape[_nt.Shape1N] = r2
s1n_r3_n: _BroadcastableShape[_nt.Shape1N] = r3
s1n_r4_n: _BroadcastableShape[_nt.Shape1N] = r4
s2n_r0_n: _BroadcastableShape[_nt.Shape2N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r1_n: _BroadcastableShape[_nt.Shape2N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r2_n: _BroadcastableShape[_nt.Shape2N] = r2
s2n_r3_n: _BroadcastableShape[_nt.Shape2N] = r3
s2n_r4_n: _BroadcastableShape[_nt.Shape2N] = r4
s3n_r0_n: _BroadcastableShape[_nt.Shape3N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r1_n: _BroadcastableShape[_nt.Shape3N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r2_n: _BroadcastableShape[_nt.Shape3N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r3_n: _BroadcastableShape[_nt.Shape3N] = r3
s3n_r4_n: _BroadcastableShape[_nt.Shape3N] = r4
s4n_r0_n: _BroadcastableShape[_nt.Shape4N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r1_n: _BroadcastableShape[_nt.Shape4N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r2_n: _BroadcastableShape[_nt.Shape4N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r3_n: _BroadcastableShape[_nt.Shape4N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r4_n: _BroadcastableShape[_nt.Shape4N] = r4

###

s0n_r0n_u: _CanBroadcastTo[_nt.Shape0N] = r0n
s0n_r1n_u: _CanBroadcastTo[_nt.Shape0N] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r2n_u: _CanBroadcastTo[_nt.Shape0N] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r3n_u: _CanBroadcastTo[_nt.Shape0N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r4n_u: _CanBroadcastTo[_nt.Shape0N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r0n_u: _CanBroadcastTo[_nt.Shape1N] = r0n
s1n_r1n_u: _CanBroadcastTo[_nt.Shape1N] = r1n
s1n_r2n_u: _CanBroadcastTo[_nt.Shape1N] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r3n_u: _CanBroadcastTo[_nt.Shape1N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r4n_u: _CanBroadcastTo[_nt.Shape1N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r0n_u: _CanBroadcastTo[_nt.Shape2N] = r0n
s2n_r1n_u: _CanBroadcastTo[_nt.Shape2N] = r1n
s2n_r2n_u: _CanBroadcastTo[_nt.Shape2N] = r2n
s2n_r3n_u: _CanBroadcastTo[_nt.Shape2N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r4n_u: _CanBroadcastTo[_nt.Shape2N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r0n_u: _CanBroadcastTo[_nt.Shape3N] = r0n
s3n_r1n_u: _CanBroadcastTo[_nt.Shape3N] = r1n
s3n_r2n_u: _CanBroadcastTo[_nt.Shape3N] = r2n
s3n_r3n_u: _CanBroadcastTo[_nt.Shape3N] = r3n
s3n_r4n_u: _CanBroadcastTo[_nt.Shape3N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r0n_u: _CanBroadcastTo[_nt.Shape4N] = r0n
s4n_r1n_u: _CanBroadcastTo[_nt.Shape4N] = r1n
s4n_r2n_u: _CanBroadcastTo[_nt.Shape4N] = r2n
s4n_r3n_u: _CanBroadcastTo[_nt.Shape4N] = r3n
s4n_r4n_u: _CanBroadcastTo[_nt.Shape4N] = r4n

s0n_r0n_n: _BroadcastableShape[_nt.Shape0N] = r0n
s0n_r1n_n: _BroadcastableShape[_nt.Shape0N] = r1n
s0n_r2n_n: _BroadcastableShape[_nt.Shape0N] = r2n
s0n_r3n_n: _BroadcastableShape[_nt.Shape0N] = r3n
s0n_r4n_n: _BroadcastableShape[_nt.Shape0N] = r4n
s1n_r0n_n: _BroadcastableShape[_nt.Shape1N] = r0n
s1n_r1n_n: _BroadcastableShape[_nt.Shape1N] = r1n
s1n_r2n_n: _BroadcastableShape[_nt.Shape1N] = r2n
s1n_r3n_n: _BroadcastableShape[_nt.Shape1N] = r3n
s1n_r4n_n: _BroadcastableShape[_nt.Shape1N] = r4n
s2n_r0n_n: _BroadcastableShape[_nt.Shape2N] = r0n
s2n_r1n_n: _BroadcastableShape[_nt.Shape2N] = r1n
s2n_r2n_n: _BroadcastableShape[_nt.Shape2N] = r2n
s2n_r3n_n: _BroadcastableShape[_nt.Shape2N] = r3n
s2n_r4n_n: _BroadcastableShape[_nt.Shape2N] = r4n
s3n_r0n_n: _BroadcastableShape[_nt.Shape3N] = r0n
s3n_r1n_n: _BroadcastableShape[_nt.Shape3N] = r1n
s3n_r2n_n: _BroadcastableShape[_nt.Shape3N] = r2n
s3n_r3n_n: _BroadcastableShape[_nt.Shape3N] = r3n
s3n_r4n_n: _BroadcastableShape[_nt.Shape3N] = r4n
s4n_r0n_n: _BroadcastableShape[_nt.Shape4N] = r0n
s4n_r1n_n: _BroadcastableShape[_nt.Shape4N] = r1n
s4n_r2n_n: _BroadcastableShape[_nt.Shape4N] = r2n
s4n_r3n_n: _BroadcastableShape[_nt.Shape4N] = r3n
s4n_r4n_n: _BroadcastableShape[_nt.Shape4N] = r4n

###

r0_r0_u: _CanBroadcastTo[_nt.Rank0] = r0
r0_r1_u: _CanBroadcastTo[_nt.Rank0] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r2_u: _CanBroadcastTo[_nt.Rank0] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r3_u: _CanBroadcastTo[_nt.Rank0] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r4_u: _CanBroadcastTo[_nt.Rank0] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r0_u: _CanBroadcastTo[_nt.Rank1] = r0
r1_r1_u: _CanBroadcastTo[_nt.Rank1] = r1
r1_r2_u: _CanBroadcastTo[_nt.Rank1] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r3_u: _CanBroadcastTo[_nt.Rank1] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r4_u: _CanBroadcastTo[_nt.Rank1] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r0_u: _CanBroadcastTo[_nt.Rank2] = r0
r2_r1_u: _CanBroadcastTo[_nt.Rank2] = r1
r2_r2_u: _CanBroadcastTo[_nt.Rank2] = r2
r2_r3_u: _CanBroadcastTo[_nt.Rank2] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r4_u: _CanBroadcastTo[_nt.Rank2] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r0_u: _CanBroadcastTo[_nt.Rank3] = r0
r3_r1_u: _CanBroadcastTo[_nt.Rank3] = r1
r3_r2_u: _CanBroadcastTo[_nt.Rank3] = r2
r3_r3_u: _CanBroadcastTo[_nt.Rank3] = r3
r3_r4_u: _CanBroadcastTo[_nt.Rank3] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r0_u: _CanBroadcastTo[_nt.Rank4] = r0
r4_r1_u: _CanBroadcastTo[_nt.Rank4] = r1
r4_r2_u: _CanBroadcastTo[_nt.Rank4] = r2
r4_r3_u: _CanBroadcastTo[_nt.Rank4] = r3
r4_r4_u: _CanBroadcastTo[_nt.Rank4] = r4

r0_r0_n: _BroadcastableShape[_nt.Rank0] = r0
r0_r1_n: _BroadcastableShape[_nt.Rank0] = r1
r0_r2_n: _BroadcastableShape[_nt.Rank0] = r2
r0_r3_n: _BroadcastableShape[_nt.Rank0] = r3
r0_r4_n: _BroadcastableShape[_nt.Rank0] = r4
r1_r0_n: _BroadcastableShape[_nt.Rank1] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r1_n: _BroadcastableShape[_nt.Rank1] = r1
r1_r2_n: _BroadcastableShape[_nt.Rank1] = r2
r1_r3_n: _BroadcastableShape[_nt.Rank1] = r3
r1_r4_n: _BroadcastableShape[_nt.Rank1] = r4
r2_r0_n: _BroadcastableShape[_nt.Rank2] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r1_n: _BroadcastableShape[_nt.Rank2] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r2_n: _BroadcastableShape[_nt.Rank2] = r2
r2_r3_n: _BroadcastableShape[_nt.Rank2] = r3
r2_r4_n: _BroadcastableShape[_nt.Rank2] = r4
r3_r0_n: _BroadcastableShape[_nt.Rank3] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r1_n: _BroadcastableShape[_nt.Rank3] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r2_n: _BroadcastableShape[_nt.Rank3] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r3_n: _BroadcastableShape[_nt.Rank3] = r3
r3_r4_n: _BroadcastableShape[_nt.Rank3] = r4
r4_r0_n: _BroadcastableShape[_nt.Rank4] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r1_n: _BroadcastableShape[_nt.Rank4] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r2_n: _BroadcastableShape[_nt.Rank4] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r3_n: _BroadcastableShape[_nt.Rank4] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r4_n: _BroadcastableShape[_nt.Rank4] = r4

###

r0_r0n_u: _CanBroadcastTo[_nt.Rank0] = r0n
r0_r1n_u: _CanBroadcastTo[_nt.Rank0] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r2n_u: _CanBroadcastTo[_nt.Rank0] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r3n_u: _CanBroadcastTo[_nt.Rank0] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r4n_u: _CanBroadcastTo[_nt.Rank0] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r0n_u: _CanBroadcastTo[_nt.Rank1] = r0n
r1_r1n_u: _CanBroadcastTo[_nt.Rank1] = r1n
r1_r2n_u: _CanBroadcastTo[_nt.Rank1] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r3n_u: _CanBroadcastTo[_nt.Rank1] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r4n_u: _CanBroadcastTo[_nt.Rank1] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r0n_u: _CanBroadcastTo[_nt.Rank2] = r0n
r2_r1n_u: _CanBroadcastTo[_nt.Rank2] = r1n
r2_r2n_u: _CanBroadcastTo[_nt.Rank2] = r2n
r2_r3n_u: _CanBroadcastTo[_nt.Rank2] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r4n_u: _CanBroadcastTo[_nt.Rank2] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r0n_u: _CanBroadcastTo[_nt.Rank3] = r0n
r3_r1n_u: _CanBroadcastTo[_nt.Rank3] = r1n
r3_r2n_u: _CanBroadcastTo[_nt.Rank3] = r2n
r3_r3n_u: _CanBroadcastTo[_nt.Rank3] = r3n
r3_r4n_u: _CanBroadcastTo[_nt.Rank3] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r0n_u: _CanBroadcastTo[_nt.Rank4] = r0n
r4_r1n_u: _CanBroadcastTo[_nt.Rank4] = r1n
r4_r2n_u: _CanBroadcastTo[_nt.Rank4] = r2n
r4_r3n_u: _CanBroadcastTo[_nt.Rank4] = r3n
r4_r4n_u: _CanBroadcastTo[_nt.Rank4] = r4n

r0_r0n_n: _BroadcastableShape[_nt.Rank0] = r0n
r0_r1n_n: _BroadcastableShape[_nt.Rank0] = r1n
r0_r2n_n: _BroadcastableShape[_nt.Rank0] = r2n
r0_r3n_n: _BroadcastableShape[_nt.Rank0] = r3n
r0_r4n_n: _BroadcastableShape[_nt.Rank0] = r4n
r1_r0n_n: _BroadcastableShape[_nt.Rank1] = r0n
r1_r1n_n: _BroadcastableShape[_nt.Rank1] = r1n
r1_r2n_n: _BroadcastableShape[_nt.Rank1] = r2n
r1_r3n_n: _BroadcastableShape[_nt.Rank1] = r3n
r1_r4n_n: _BroadcastableShape[_nt.Rank1] = r4n
r2_r0n_n: _BroadcastableShape[_nt.Rank2] = r0n
r2_r1n_n: _BroadcastableShape[_nt.Rank2] = r1n
r2_r2n_n: _BroadcastableShape[_nt.Rank2] = r2n
r2_r3n_n: _BroadcastableShape[_nt.Rank2] = r3n
r2_r4n_n: _BroadcastableShape[_nt.Rank2] = r4n
r3_r0n_n: _BroadcastableShape[_nt.Rank3] = r0n
r3_r1n_n: _BroadcastableShape[_nt.Rank3] = r1n
r3_r2n_n: _BroadcastableShape[_nt.Rank3] = r2n
r3_r3n_n: _BroadcastableShape[_nt.Rank3] = r3n
r3_r4n_n: _BroadcastableShape[_nt.Rank3] = r4n
r4_r0n_n: _BroadcastableShape[_nt.Rank4] = r0n
r4_r1n_n: _BroadcastableShape[_nt.Rank4] = r1n
r4_r2n_n: _BroadcastableShape[_nt.Rank4] = r2n
r4_r3n_n: _BroadcastableShape[_nt.Rank4] = r3n
r4_r4n_n: _BroadcastableShape[_nt.Rank4] = r4n

###

r0n_r0_u: _CanBroadcastTo[_nt.Rank0N] = r0
r0n_r1_u: _CanBroadcastTo[_nt.Rank0N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r2_u: _CanBroadcastTo[_nt.Rank0N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r3_u: _CanBroadcastTo[_nt.Rank0N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r4_u: _CanBroadcastTo[_nt.Rank0N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r0_u: _CanBroadcastTo[_nt.Rank1N] = r0
r1n_r1_u: _CanBroadcastTo[_nt.Rank1N] = r1
r1n_r2_u: _CanBroadcastTo[_nt.Rank1N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r3_u: _CanBroadcastTo[_nt.Rank1N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r4_u: _CanBroadcastTo[_nt.Rank1N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r0_u: _CanBroadcastTo[_nt.Rank2N] = r0
r2n_r1_u: _CanBroadcastTo[_nt.Rank2N] = r1
r2n_r2_u: _CanBroadcastTo[_nt.Rank2N] = r2
r2n_r3_u: _CanBroadcastTo[_nt.Rank2N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r4_u: _CanBroadcastTo[_nt.Rank2N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r0_u: _CanBroadcastTo[_nt.Rank3N] = r0
r3n_r1_u: _CanBroadcastTo[_nt.Rank3N] = r1
r3n_r2_u: _CanBroadcastTo[_nt.Rank3N] = r2
r3n_r3_u: _CanBroadcastTo[_nt.Rank3N] = r3
r3n_r4_u: _CanBroadcastTo[_nt.Rank3N] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r0_u: _CanBroadcastTo[_nt.Rank4N] = r0
r4n_r1_u: _CanBroadcastTo[_nt.Rank4N] = r1
r4n_r2_u: _CanBroadcastTo[_nt.Rank4N] = r2
r4n_r3_u: _CanBroadcastTo[_nt.Rank4N] = r3
r4n_r4_u: _CanBroadcastTo[_nt.Rank4N] = r4

r0n_r0_n: _BroadcastableShape[_nt.Rank0N] = r0
r0n_r1_n: _BroadcastableShape[_nt.Rank0N] = r1
r0n_r2_n: _BroadcastableShape[_nt.Rank0N] = r2
r0n_r3_n: _BroadcastableShape[_nt.Rank0N] = r3
r0n_r4_n: _BroadcastableShape[_nt.Rank0N] = r4
r1n_r0_n: _BroadcastableShape[_nt.Rank1N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r1_n: _BroadcastableShape[_nt.Rank1N] = r1
r1n_r2_n: _BroadcastableShape[_nt.Rank1N] = r2
r1n_r3_n: _BroadcastableShape[_nt.Rank1N] = r3
r1n_r4_n: _BroadcastableShape[_nt.Rank1N] = r4
r2n_r0_n: _BroadcastableShape[_nt.Rank2N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r1_n: _BroadcastableShape[_nt.Rank2N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r2_n: _BroadcastableShape[_nt.Rank2N] = r2
r2n_r3_n: _BroadcastableShape[_nt.Rank2N] = r3
r2n_r4_n: _BroadcastableShape[_nt.Rank2N] = r4
r3n_r0_n: _BroadcastableShape[_nt.Rank3N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r1_n: _BroadcastableShape[_nt.Rank3N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r2_n: _BroadcastableShape[_nt.Rank3N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r3_n: _BroadcastableShape[_nt.Rank3N] = r3
r3n_r4_n: _BroadcastableShape[_nt.Rank3N] = r4
r4n_r0_n: _BroadcastableShape[_nt.Rank4N] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r1_n: _BroadcastableShape[_nt.Rank4N] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r2_n: _BroadcastableShape[_nt.Rank4N] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r3_n: _BroadcastableShape[_nt.Rank4N] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r4_n: _BroadcastableShape[_nt.Rank4N] = r4

###

r0n_r0n_u: _CanBroadcastTo[_nt.Rank0N] = r0n
r0n_r1n_u: _CanBroadcastTo[_nt.Rank0N] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r2n_u: _CanBroadcastTo[_nt.Rank0N] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r3n_u: _CanBroadcastTo[_nt.Rank0N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r4n_u: _CanBroadcastTo[_nt.Rank0N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r0n_u: _CanBroadcastTo[_nt.Rank1N] = r0n
r1n_r1n_u: _CanBroadcastTo[_nt.Rank1N] = r1n
r1n_r2n_u: _CanBroadcastTo[_nt.Rank1N] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r3n_u: _CanBroadcastTo[_nt.Rank1N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r4n_u: _CanBroadcastTo[_nt.Rank1N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r0n_u: _CanBroadcastTo[_nt.Rank2N] = r0n
r2n_r1n_u: _CanBroadcastTo[_nt.Rank2N] = r1n
r2n_r2n_u: _CanBroadcastTo[_nt.Rank2N] = r2n
r2n_r3n_u: _CanBroadcastTo[_nt.Rank2N] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r4n_u: _CanBroadcastTo[_nt.Rank2N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r0n_u: _CanBroadcastTo[_nt.Rank3N] = r0n
r3n_r1n_u: _CanBroadcastTo[_nt.Rank3N] = r1n
r3n_r2n_u: _CanBroadcastTo[_nt.Rank3N] = r2n
r3n_r3n_u: _CanBroadcastTo[_nt.Rank3N] = r3n
r3n_r4n_u: _CanBroadcastTo[_nt.Rank3N] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r0n_u: _CanBroadcastTo[_nt.Rank4N] = r0n
r4n_r1n_u: _CanBroadcastTo[_nt.Rank4N] = r1n
r4n_r2n_u: _CanBroadcastTo[_nt.Rank4N] = r2n
r4n_r3n_u: _CanBroadcastTo[_nt.Rank4N] = r3n
r4n_r4n_u: _CanBroadcastTo[_nt.Rank4N] = r4n

r0n_r0n_n: _BroadcastableShape[_nt.Rank0N] = r0n
r0n_r1n_n: _BroadcastableShape[_nt.Rank0N] = r1n
r0n_r2n_n: _BroadcastableShape[_nt.Rank0N] = r2n
r0n_r3n_n: _BroadcastableShape[_nt.Rank0N] = r3n
r0n_r4n_n: _BroadcastableShape[_nt.Rank0N] = r4n
r1n_r0n_n: _BroadcastableShape[_nt.Rank1N] = r0n
r1n_r1n_n: _BroadcastableShape[_nt.Rank1N] = r1n
r1n_r2n_n: _BroadcastableShape[_nt.Rank1N] = r2n
r1n_r3n_n: _BroadcastableShape[_nt.Rank1N] = r3n
r1n_r4n_n: _BroadcastableShape[_nt.Rank1N] = r4n
r2n_r0n_n: _BroadcastableShape[_nt.Rank2N] = r0n
r2n_r1n_n: _BroadcastableShape[_nt.Rank2N] = r1n
r2n_r2n_n: _BroadcastableShape[_nt.Rank2N] = r2n
r2n_r3n_n: _BroadcastableShape[_nt.Rank2N] = r3n
r2n_r4n_n: _BroadcastableShape[_nt.Rank2N] = r4n
r3n_r0n_n: _BroadcastableShape[_nt.Rank3N] = r0n
r3n_r1n_n: _BroadcastableShape[_nt.Rank3N] = r1n
r3n_r2n_n: _BroadcastableShape[_nt.Rank3N] = r2n
r3n_r3n_n: _BroadcastableShape[_nt.Rank3N] = r3n
r3n_r4n_n: _BroadcastableShape[_nt.Rank3N] = r4n
r4n_r0n_n: _BroadcastableShape[_nt.Rank4N] = r0n
r4n_r1n_n: _BroadcastableShape[_nt.Rank4N] = r1n
r4n_r2n_n: _BroadcastableShape[_nt.Rank4N] = r2n
r4n_r3n_n: _BroadcastableShape[_nt.Rank4N] = r3n
r4n_r4n_n: _BroadcastableShape[_nt.Rank4N] = r4n
