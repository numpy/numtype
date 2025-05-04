from _numtype._rank import (
    Broadcastable,
    Broadcaster,
    Rank0,
    Rank0ToN,
    Rank1,
    Rank1ToN,
    Rank2,
    Rank2ToN,
    Rank3,
    Rank3ToN,
    Rank4,
    Rank4ToN,
)
from _numtype._shape import (
    Shape as Shape0_,
    Shape0,
    Shape1,
    Shape1_,
    Shape2,
    Shape2_,
    Shape3,
    Shape3_,
    Shape4,
    Shape4_,
)

###

s0: Shape0
s1: Shape1
s2: Shape2
s3: Shape3
s4: Shape4

s0n: Shape0_
s1n: Shape1_
s2n: Shape2_
s3n: Shape3_
s4n: Shape4_

r0: Rank0
r1: Rank1
r2: Rank2
r3: Rank3
r4: Rank4

r0n: Rank0ToN
r1n: Rank1ToN
r2n: Rank2ToN
r3n: Rank3ToN
r4n: Rank4ToN

###

s0_r0_u: Broadcastable[Shape0] = r0
s0_r1_u: Broadcastable[Shape0] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r2_u: Broadcastable[Shape0] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r3_u: Broadcastable[Shape0] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r4_u: Broadcastable[Shape0] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r0_u: Broadcastable[Shape1] = r0
s1_r1_u: Broadcastable[Shape1] = r1
s1_r2_u: Broadcastable[Shape1] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r3_u: Broadcastable[Shape1] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r4_u: Broadcastable[Shape1] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r0_u: Broadcastable[Shape2] = r0
s2_r1_u: Broadcastable[Shape2] = r1
s2_r2_u: Broadcastable[Shape2] = r2
s2_r3_u: Broadcastable[Shape2] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r4_u: Broadcastable[Shape2] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r0_u: Broadcastable[Shape3] = r0
s3_r1_u: Broadcastable[Shape3] = r1
s3_r2_u: Broadcastable[Shape3] = r2
s3_r3_u: Broadcastable[Shape3] = r3
s3_r4_u: Broadcastable[Shape3] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r0_u: Broadcastable[Shape4] = r0
s4_r1_u: Broadcastable[Shape4] = r1
s4_r2_u: Broadcastable[Shape4] = r2
s4_r3_u: Broadcastable[Shape4] = r3
s4_r4_u: Broadcastable[Shape4] = r4

s0_r0_n: Broadcaster[Shape0] = r0
s0_r1_n: Broadcaster[Shape0] = r1
s0_r2_n: Broadcaster[Shape0] = r2
s0_r3_n: Broadcaster[Shape0] = r3
s0_r4_n: Broadcaster[Shape0] = r4
s1_r0_n: Broadcaster[Shape1] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r1_n: Broadcaster[Shape1] = r1
s1_r2_n: Broadcaster[Shape1] = r2
s1_r3_n: Broadcaster[Shape1] = r3
s1_r4_n: Broadcaster[Shape1] = r4
s2_r0_n: Broadcaster[Shape2] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r1_n: Broadcaster[Shape2] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r2_n: Broadcaster[Shape2] = r2
s2_r3_n: Broadcaster[Shape2] = r3
s2_r4_n: Broadcaster[Shape2] = r4
s3_r0_n: Broadcaster[Shape3] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r1_n: Broadcaster[Shape3] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r2_n: Broadcaster[Shape3] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r3_n: Broadcaster[Shape3] = r3
s3_r4_n: Broadcaster[Shape3] = r4
s4_r0_n: Broadcaster[Shape4] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r1_n: Broadcaster[Shape4] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r2_n: Broadcaster[Shape4] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r3_n: Broadcaster[Shape4] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r4_n: Broadcaster[Shape4] = r4

###

s0_r0n_u: Broadcastable[Shape0] = r0n
s0_r1n_u: Broadcastable[Shape0] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r2n_u: Broadcastable[Shape0] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r3n_u: Broadcastable[Shape0] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0_r4n_u: Broadcastable[Shape0] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r0n_u: Broadcastable[Shape1] = r0n
s1_r1n_u: Broadcastable[Shape1] = r1n
s1_r2n_u: Broadcastable[Shape1] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r3n_u: Broadcastable[Shape1] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1_r4n_u: Broadcastable[Shape1] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r0n_u: Broadcastable[Shape2] = r0n
s2_r1n_u: Broadcastable[Shape2] = r1n
s2_r2n_u: Broadcastable[Shape2] = r2n
s2_r3n_u: Broadcastable[Shape2] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2_r4n_u: Broadcastable[Shape2] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3_r0n_u: Broadcastable[Shape3] = r0n
s3_r1n_u: Broadcastable[Shape3] = r1n
s3_r2n_u: Broadcastable[Shape3] = r2n
s3_r3n_u: Broadcastable[Shape3] = r3n
s3_r4n_u: Broadcastable[Shape3] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4_r0n_u: Broadcastable[Shape4] = r0n
s4_r1n_u: Broadcastable[Shape4] = r1n
s4_r2n_u: Broadcastable[Shape4] = r2n
s4_r3n_u: Broadcastable[Shape4] = r3n
s4_r4n_u: Broadcastable[Shape4] = r4n

s0_r0n_n: Broadcaster[Shape0] = r0n
s0_r1n_n: Broadcaster[Shape0] = r1n
s0_r2n_n: Broadcaster[Shape0] = r2n
s0_r3n_n: Broadcaster[Shape0] = r3n
s0_r4n_n: Broadcaster[Shape0] = r4n
s1_r0n_n: Broadcaster[Shape1] = r0n
s1_r1n_n: Broadcaster[Shape1] = r1n
s1_r2n_n: Broadcaster[Shape1] = r2n
s1_r3n_n: Broadcaster[Shape1] = r3n
s1_r4n_n: Broadcaster[Shape1] = r4n
s2_r0n_n: Broadcaster[Shape2] = r0n
s2_r1n_n: Broadcaster[Shape2] = r1n
s2_r2n_n: Broadcaster[Shape2] = r2n
s2_r3n_n: Broadcaster[Shape2] = r3n
s2_r4n_n: Broadcaster[Shape2] = r4n
s3_r0n_n: Broadcaster[Shape3] = r0n
s3_r1n_n: Broadcaster[Shape3] = r1n
s3_r2n_n: Broadcaster[Shape3] = r2n
s3_r3n_n: Broadcaster[Shape3] = r3n
s3_r4n_n: Broadcaster[Shape3] = r4n
s4_r0n_n: Broadcaster[Shape4] = r0n
s4_r1n_n: Broadcaster[Shape4] = r1n
s4_r2n_n: Broadcaster[Shape4] = r2n
s4_r3n_n: Broadcaster[Shape4] = r3n
s4_r4n_n: Broadcaster[Shape4] = r4n

###

s0n_r0_u: Broadcastable[Shape0_] = r0
s0n_r1_u: Broadcastable[Shape0_] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r2_u: Broadcastable[Shape0_] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r3_u: Broadcastable[Shape0_] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r4_u: Broadcastable[Shape0_] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r0_u: Broadcastable[Shape1_] = r0
s1n_r1_u: Broadcastable[Shape1_] = r1
s1n_r2_u: Broadcastable[Shape1_] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r3_u: Broadcastable[Shape1_] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r4_u: Broadcastable[Shape1_] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r0_u: Broadcastable[Shape2_] = r0
s2n_r1_u: Broadcastable[Shape2_] = r1
s2n_r2_u: Broadcastable[Shape2_] = r2
s2n_r3_u: Broadcastable[Shape2_] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r4_u: Broadcastable[Shape2_] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r0_u: Broadcastable[Shape3_] = r0
s3n_r1_u: Broadcastable[Shape3_] = r1
s3n_r2_u: Broadcastable[Shape3_] = r2
s3n_r3_u: Broadcastable[Shape3_] = r3
s3n_r4_u: Broadcastable[Shape3_] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r0_u: Broadcastable[Shape4_] = r0
s4n_r1_u: Broadcastable[Shape4_] = r1
s4n_r2_u: Broadcastable[Shape4_] = r2
s4n_r3_u: Broadcastable[Shape4_] = r3
s4n_r4_u: Broadcastable[Shape4_] = r4

s0n_r0_n: Broadcaster[Shape0_] = r0
s0n_r1_n: Broadcaster[Shape0_] = r1
s0n_r2_n: Broadcaster[Shape0_] = r2
s0n_r3_n: Broadcaster[Shape0_] = r3
s0n_r4_n: Broadcaster[Shape0_] = r4
s1n_r0_n: Broadcaster[Shape1_] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r1_n: Broadcaster[Shape1_] = r1
s1n_r2_n: Broadcaster[Shape1_] = r2
s1n_r3_n: Broadcaster[Shape1_] = r3
s1n_r4_n: Broadcaster[Shape1_] = r4
s2n_r0_n: Broadcaster[Shape2_] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r1_n: Broadcaster[Shape2_] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r2_n: Broadcaster[Shape2_] = r2
s2n_r3_n: Broadcaster[Shape2_] = r3
s2n_r4_n: Broadcaster[Shape2_] = r4
s3n_r0_n: Broadcaster[Shape3_] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r1_n: Broadcaster[Shape3_] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r2_n: Broadcaster[Shape3_] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r3_n: Broadcaster[Shape3_] = r3
s3n_r4_n: Broadcaster[Shape3_] = r4
s4n_r0_n: Broadcaster[Shape4_] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r1_n: Broadcaster[Shape4_] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r2_n: Broadcaster[Shape4_] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r3_n: Broadcaster[Shape4_] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r4_n: Broadcaster[Shape4_] = r4

###

s0n_r0n_u: Broadcastable[Shape0_] = r0n
s0n_r1n_u: Broadcastable[Shape0_] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r2n_u: Broadcastable[Shape0_] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r3n_u: Broadcastable[Shape0_] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s0n_r4n_u: Broadcastable[Shape0_] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r0n_u: Broadcastable[Shape1_] = r0n
s1n_r1n_u: Broadcastable[Shape1_] = r1n
s1n_r2n_u: Broadcastable[Shape1_] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r3n_u: Broadcastable[Shape1_] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s1n_r4n_u: Broadcastable[Shape1_] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r0n_u: Broadcastable[Shape2_] = r0n
s2n_r1n_u: Broadcastable[Shape2_] = r1n
s2n_r2n_u: Broadcastable[Shape2_] = r2n
s2n_r3n_u: Broadcastable[Shape2_] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s2n_r4n_u: Broadcastable[Shape2_] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s3n_r0n_u: Broadcastable[Shape3_] = r0n
s3n_r1n_u: Broadcastable[Shape3_] = r1n
s3n_r2n_u: Broadcastable[Shape3_] = r2n
s3n_r3n_u: Broadcastable[Shape3_] = r3n
s3n_r4n_u: Broadcastable[Shape3_] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
s4n_r0n_u: Broadcastable[Shape4_] = r0n
s4n_r1n_u: Broadcastable[Shape4_] = r1n
s4n_r2n_u: Broadcastable[Shape4_] = r2n
s4n_r3n_u: Broadcastable[Shape4_] = r3n
s4n_r4n_u: Broadcastable[Shape4_] = r4n

s0n_r0n_n: Broadcaster[Shape0_] = r0n
s0n_r1n_n: Broadcaster[Shape0_] = r1n
s0n_r2n_n: Broadcaster[Shape0_] = r2n
s0n_r3n_n: Broadcaster[Shape0_] = r3n
s0n_r4n_n: Broadcaster[Shape0_] = r4n
s1n_r0n_n: Broadcaster[Shape1_] = r0n
s1n_r1n_n: Broadcaster[Shape1_] = r1n
s1n_r2n_n: Broadcaster[Shape1_] = r2n
s1n_r3n_n: Broadcaster[Shape1_] = r3n
s1n_r4n_n: Broadcaster[Shape1_] = r4n
s2n_r0n_n: Broadcaster[Shape2_] = r0n
s2n_r1n_n: Broadcaster[Shape2_] = r1n
s2n_r2n_n: Broadcaster[Shape2_] = r2n
s2n_r3n_n: Broadcaster[Shape2_] = r3n
s2n_r4n_n: Broadcaster[Shape2_] = r4n
s3n_r0n_n: Broadcaster[Shape3_] = r0n
s3n_r1n_n: Broadcaster[Shape3_] = r1n
s3n_r2n_n: Broadcaster[Shape3_] = r2n
s3n_r3n_n: Broadcaster[Shape3_] = r3n
s3n_r4n_n: Broadcaster[Shape3_] = r4n
s4n_r0n_n: Broadcaster[Shape4_] = r0n
s4n_r1n_n: Broadcaster[Shape4_] = r1n
s4n_r2n_n: Broadcaster[Shape4_] = r2n
s4n_r3n_n: Broadcaster[Shape4_] = r3n
s4n_r4n_n: Broadcaster[Shape4_] = r4n

###

r0_r0_u: Broadcastable[Rank0] = r0
r0_r1_u: Broadcastable[Rank0] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r2_u: Broadcastable[Rank0] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r3_u: Broadcastable[Rank0] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r4_u: Broadcastable[Rank0] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r0_u: Broadcastable[Rank1] = r0
r1_r1_u: Broadcastable[Rank1] = r1
r1_r2_u: Broadcastable[Rank1] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r3_u: Broadcastable[Rank1] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r4_u: Broadcastable[Rank1] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r0_u: Broadcastable[Rank2] = r0
r2_r1_u: Broadcastable[Rank2] = r1
r2_r2_u: Broadcastable[Rank2] = r2
r2_r3_u: Broadcastable[Rank2] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r4_u: Broadcastable[Rank2] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r0_u: Broadcastable[Rank3] = r0
r3_r1_u: Broadcastable[Rank3] = r1
r3_r2_u: Broadcastable[Rank3] = r2
r3_r3_u: Broadcastable[Rank3] = r3
r3_r4_u: Broadcastable[Rank3] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r0_u: Broadcastable[Rank4] = r0
r4_r1_u: Broadcastable[Rank4] = r1
r4_r2_u: Broadcastable[Rank4] = r2
r4_r3_u: Broadcastable[Rank4] = r3
r4_r4_u: Broadcastable[Rank4] = r4

r0_r0_n: Broadcaster[Rank0] = r0
r0_r1_n: Broadcaster[Rank0] = r1
r0_r2_n: Broadcaster[Rank0] = r2
r0_r3_n: Broadcaster[Rank0] = r3
r0_r4_n: Broadcaster[Rank0] = r4
r1_r0_n: Broadcaster[Rank1] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r1_n: Broadcaster[Rank1] = r1
r1_r2_n: Broadcaster[Rank1] = r2
r1_r3_n: Broadcaster[Rank1] = r3
r1_r4_n: Broadcaster[Rank1] = r4
r2_r0_n: Broadcaster[Rank2] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r1_n: Broadcaster[Rank2] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r2_n: Broadcaster[Rank2] = r2
r2_r3_n: Broadcaster[Rank2] = r3
r2_r4_n: Broadcaster[Rank2] = r4
r3_r0_n: Broadcaster[Rank3] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r1_n: Broadcaster[Rank3] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r2_n: Broadcaster[Rank3] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r3_n: Broadcaster[Rank3] = r3
r3_r4_n: Broadcaster[Rank3] = r4
r4_r0_n: Broadcaster[Rank4] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r1_n: Broadcaster[Rank4] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r2_n: Broadcaster[Rank4] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r3_n: Broadcaster[Rank4] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r4_n: Broadcaster[Rank4] = r4

###

r0_r0n_u: Broadcastable[Rank0] = r0n
r0_r1n_u: Broadcastable[Rank0] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r2n_u: Broadcastable[Rank0] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r3n_u: Broadcastable[Rank0] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0_r4n_u: Broadcastable[Rank0] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r0n_u: Broadcastable[Rank1] = r0n
r1_r1n_u: Broadcastable[Rank1] = r1n
r1_r2n_u: Broadcastable[Rank1] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r3n_u: Broadcastable[Rank1] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1_r4n_u: Broadcastable[Rank1] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r0n_u: Broadcastable[Rank2] = r0n
r2_r1n_u: Broadcastable[Rank2] = r1n
r2_r2n_u: Broadcastable[Rank2] = r2n
r2_r3n_u: Broadcastable[Rank2] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2_r4n_u: Broadcastable[Rank2] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3_r0n_u: Broadcastable[Rank3] = r0n
r3_r1n_u: Broadcastable[Rank3] = r1n
r3_r2n_u: Broadcastable[Rank3] = r2n
r3_r3n_u: Broadcastable[Rank3] = r3n
r3_r4n_u: Broadcastable[Rank3] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4_r0n_u: Broadcastable[Rank4] = r0n
r4_r1n_u: Broadcastable[Rank4] = r1n
r4_r2n_u: Broadcastable[Rank4] = r2n
r4_r3n_u: Broadcastable[Rank4] = r3n
r4_r4n_u: Broadcastable[Rank4] = r4n

r0_r0n_n: Broadcaster[Rank0] = r0n
r0_r1n_n: Broadcaster[Rank0] = r1n
r0_r2n_n: Broadcaster[Rank0] = r2n
r0_r3n_n: Broadcaster[Rank0] = r3n
r0_r4n_n: Broadcaster[Rank0] = r4n
r1_r0n_n: Broadcaster[Rank1] = r0n
r1_r1n_n: Broadcaster[Rank1] = r1n
r1_r2n_n: Broadcaster[Rank1] = r2n
r1_r3n_n: Broadcaster[Rank1] = r3n
r1_r4n_n: Broadcaster[Rank1] = r4n
r2_r0n_n: Broadcaster[Rank2] = r0n
r2_r1n_n: Broadcaster[Rank2] = r1n
r2_r2n_n: Broadcaster[Rank2] = r2n
r2_r3n_n: Broadcaster[Rank2] = r3n
r2_r4n_n: Broadcaster[Rank2] = r4n
r3_r0n_n: Broadcaster[Rank3] = r0n
r3_r1n_n: Broadcaster[Rank3] = r1n
r3_r2n_n: Broadcaster[Rank3] = r2n
r3_r3n_n: Broadcaster[Rank3] = r3n
r3_r4n_n: Broadcaster[Rank3] = r4n
r4_r0n_n: Broadcaster[Rank4] = r0n
r4_r1n_n: Broadcaster[Rank4] = r1n
r4_r2n_n: Broadcaster[Rank4] = r2n
r4_r3n_n: Broadcaster[Rank4] = r3n
r4_r4n_n: Broadcaster[Rank4] = r4n

###

r0n_r0_u: Broadcastable[Rank0ToN] = r0
r0n_r1_u: Broadcastable[Rank0ToN] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r2_u: Broadcastable[Rank0ToN] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r3_u: Broadcastable[Rank0ToN] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r4_u: Broadcastable[Rank0ToN] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r0_u: Broadcastable[Rank1ToN] = r0
r1n_r1_u: Broadcastable[Rank1ToN] = r1
r1n_r2_u: Broadcastable[Rank1ToN] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r3_u: Broadcastable[Rank1ToN] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r4_u: Broadcastable[Rank1ToN] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r0_u: Broadcastable[Rank2ToN] = r0
r2n_r1_u: Broadcastable[Rank2ToN] = r1
r2n_r2_u: Broadcastable[Rank2ToN] = r2
r2n_r3_u: Broadcastable[Rank2ToN] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r4_u: Broadcastable[Rank2ToN] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r0_u: Broadcastable[Rank3ToN] = r0
r3n_r1_u: Broadcastable[Rank3ToN] = r1
r3n_r2_u: Broadcastable[Rank3ToN] = r2
r3n_r3_u: Broadcastable[Rank3ToN] = r3
r3n_r4_u: Broadcastable[Rank3ToN] = r4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r0_u: Broadcastable[Rank4ToN] = r0
r4n_r1_u: Broadcastable[Rank4ToN] = r1
r4n_r2_u: Broadcastable[Rank4ToN] = r2
r4n_r3_u: Broadcastable[Rank4ToN] = r3
r4n_r4_u: Broadcastable[Rank4ToN] = r4

r0n_r0_n: Broadcaster[Rank0ToN] = r0
r0n_r1_n: Broadcaster[Rank0ToN] = r1
r0n_r2_n: Broadcaster[Rank0ToN] = r2
r0n_r3_n: Broadcaster[Rank0ToN] = r3
r0n_r4_n: Broadcaster[Rank0ToN] = r4
r1n_r0_n: Broadcaster[Rank1ToN] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r1_n: Broadcaster[Rank1ToN] = r1
r1n_r2_n: Broadcaster[Rank1ToN] = r2
r1n_r3_n: Broadcaster[Rank1ToN] = r3
r1n_r4_n: Broadcaster[Rank1ToN] = r4
r2n_r0_n: Broadcaster[Rank2ToN] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r1_n: Broadcaster[Rank2ToN] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r2_n: Broadcaster[Rank2ToN] = r2
r2n_r3_n: Broadcaster[Rank2ToN] = r3
r2n_r4_n: Broadcaster[Rank2ToN] = r4
r3n_r0_n: Broadcaster[Rank3ToN] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r1_n: Broadcaster[Rank3ToN] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r2_n: Broadcaster[Rank3ToN] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r3_n: Broadcaster[Rank3ToN] = r3
r3n_r4_n: Broadcaster[Rank3ToN] = r4
r4n_r0_n: Broadcaster[Rank4ToN] = r0  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r1_n: Broadcaster[Rank4ToN] = r1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r2_n: Broadcaster[Rank4ToN] = r2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r3_n: Broadcaster[Rank4ToN] = r3  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r4_n: Broadcaster[Rank4ToN] = r4

###

r0n_r0n_u: Broadcastable[Rank0ToN] = r0n
r0n_r1n_u: Broadcastable[Rank0ToN] = r1n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r2n_u: Broadcastable[Rank0ToN] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r3n_u: Broadcastable[Rank0ToN] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r0n_r4n_u: Broadcastable[Rank0ToN] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r0n_u: Broadcastable[Rank1ToN] = r0n
r1n_r1n_u: Broadcastable[Rank1ToN] = r1n
r1n_r2n_u: Broadcastable[Rank1ToN] = r2n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r3n_u: Broadcastable[Rank1ToN] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r1n_r4n_u: Broadcastable[Rank1ToN] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r0n_u: Broadcastable[Rank2ToN] = r0n
r2n_r1n_u: Broadcastable[Rank2ToN] = r1n
r2n_r2n_u: Broadcastable[Rank2ToN] = r2n
r2n_r3n_u: Broadcastable[Rank2ToN] = r3n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r2n_r4n_u: Broadcastable[Rank2ToN] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r3n_r0n_u: Broadcastable[Rank3ToN] = r0n
r3n_r1n_u: Broadcastable[Rank3ToN] = r1n
r3n_r2n_u: Broadcastable[Rank3ToN] = r2n
r3n_r3n_u: Broadcastable[Rank3ToN] = r3n
r3n_r4n_u: Broadcastable[Rank3ToN] = r4n  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
r4n_r0n_u: Broadcastable[Rank4ToN] = r0n
r4n_r1n_u: Broadcastable[Rank4ToN] = r1n
r4n_r2n_u: Broadcastable[Rank4ToN] = r2n
r4n_r3n_u: Broadcastable[Rank4ToN] = r3n
r4n_r4n_u: Broadcastable[Rank4ToN] = r4n

r0n_r0n_n: Broadcaster[Rank0ToN] = r0n
r0n_r1n_n: Broadcaster[Rank0ToN] = r1n
r0n_r2n_n: Broadcaster[Rank0ToN] = r2n
r0n_r3n_n: Broadcaster[Rank0ToN] = r3n
r0n_r4n_n: Broadcaster[Rank0ToN] = r4n
r1n_r0n_n: Broadcaster[Rank1ToN] = r0n
r1n_r1n_n: Broadcaster[Rank1ToN] = r1n
r1n_r2n_n: Broadcaster[Rank1ToN] = r2n
r1n_r3n_n: Broadcaster[Rank1ToN] = r3n
r1n_r4n_n: Broadcaster[Rank1ToN] = r4n
r2n_r0n_n: Broadcaster[Rank2ToN] = r0n
r2n_r1n_n: Broadcaster[Rank2ToN] = r1n
r2n_r2n_n: Broadcaster[Rank2ToN] = r2n
r2n_r3n_n: Broadcaster[Rank2ToN] = r3n
r2n_r4n_n: Broadcaster[Rank2ToN] = r4n
r3n_r0n_n: Broadcaster[Rank3ToN] = r0n
r3n_r1n_n: Broadcaster[Rank3ToN] = r1n
r3n_r2n_n: Broadcaster[Rank3ToN] = r2n
r3n_r3n_n: Broadcaster[Rank3ToN] = r3n
r3n_r4n_n: Broadcaster[Rank3ToN] = r4n
r4n_r0n_n: Broadcaster[Rank4ToN] = r0n
r4n_r1n_n: Broadcaster[Rank4ToN] = r1n
r4n_r2n_n: Broadcaster[Rank4ToN] = r2n
r4n_r3n_n: Broadcaster[Rank4ToN] = r3n
r4n_r4n_n: Broadcaster[Rank4ToN] = r4n
