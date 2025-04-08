from typing import Any

import numpy as np
from _numtype._scalar_co import CanPromote

b1: np.bool
i1: np.int8
i2: np.int16
i4: np.int32
i8: np.int64
u1: np.uint8
u2: np.uint16
u4: np.uint32
u8: np.uint64
f2: np.float16
f4: np.float32
f8: np.float64
ld: np.longdouble
c8: np.complex64
c16: np.complex128
cld: np.clongdouble

###
# See https://numpy.org/neps/nep-0050-scalar-promotion.html

b1_from_b1: CanPromote[np.bool] = b1
b1_from_i1: CanPromote[np.bool] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u1: CanPromote[np.bool] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i2: CanPromote[np.bool] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u2: CanPromote[np.bool] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i4: CanPromote[np.bool] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u4: CanPromote[np.bool] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i8: CanPromote[np.bool] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u8: CanPromote[np.bool] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f2: CanPromote[np.bool] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f4: CanPromote[np.bool] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f8: CanPromote[np.bool] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_ld: CanPromote[np.bool] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_c8: CanPromote[np.bool] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_c16: CanPromote[np.bool] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_cld: CanPromote[np.bool] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

b1_to_b1: CanPromote[Any, np.bool] = b1
b1_to_i1: CanPromote[Any, np.bool] = i1
b1_to_u1: CanPromote[Any, np.bool] = u1
b1_to_i2: CanPromote[Any, np.bool] = i2
b1_to_u2: CanPromote[Any, np.bool] = u2
b1_to_i4: CanPromote[Any, np.bool] = i4
b1_to_u4: CanPromote[Any, np.bool] = u4
b1_to_i8: CanPromote[Any, np.bool] = i8
b1_to_u8: CanPromote[Any, np.bool] = u8
b1_to_f2: CanPromote[Any, np.bool] = f2
b1_to_f4: CanPromote[Any, np.bool] = f4
b1_to_f8: CanPromote[Any, np.bool] = f8
b1_to_ld: CanPromote[Any, np.bool] = ld
b1_to_c8: CanPromote[Any, np.bool] = c8
b1_to_c16: CanPromote[Any, np.bool] = c16
b1_to_cld: CanPromote[Any, np.bool] = cld

i1_from_b1: CanPromote[np.int8] = b1
i1_from_i1: CanPromote[np.int8] = i1
i1_from_u1: CanPromote[np.int8] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i2: CanPromote[np.int8] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u2: CanPromote[np.int8] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i4: CanPromote[np.int8] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u4: CanPromote[np.int8] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i8: CanPromote[np.int8] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u8: CanPromote[np.int8] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f2: CanPromote[np.int8] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f4: CanPromote[np.int8] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f8: CanPromote[np.int8] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_ld: CanPromote[np.int8] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_c8: CanPromote[np.int8] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_c16: CanPromote[np.int8] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_cld: CanPromote[np.int8] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i1_to_b1: CanPromote[Any, np.int8] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i1: CanPromote[Any, np.int8] = i1
i1_to_u1: CanPromote[Any, np.int8] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i2: CanPromote[Any, np.int8] = i2
i1_to_u2: CanPromote[Any, np.int8] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i4: CanPromote[Any, np.int8] = i4
i1_to_u4: CanPromote[Any, np.int8] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i8: CanPromote[Any, np.int8] = i8
i1_to_u8: CanPromote[Any, np.int8] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_f2: CanPromote[Any, np.int8] = f2
i1_to_f4: CanPromote[Any, np.int8] = f4
i1_to_f8: CanPromote[Any, np.int8] = f8
i1_to_ld: CanPromote[Any, np.int8] = ld
i1_to_c8: CanPromote[Any, np.int8] = c8
i1_to_c16: CanPromote[Any, np.int8] = c16
i1_to_cld: CanPromote[Any, np.int8] = cld

u1_from_b1: CanPromote[np.uint8] = b1
u1_from_i1: CanPromote[np.uint8] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u1: CanPromote[np.uint8] = u1
u1_from_i2: CanPromote[np.uint8] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u2: CanPromote[np.uint8] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_i4: CanPromote[np.uint8] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u4: CanPromote[np.uint8] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_i8: CanPromote[np.uint8] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u8: CanPromote[np.uint8] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f2: CanPromote[np.uint8] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f4: CanPromote[np.uint8] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f8: CanPromote[np.uint8] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_ld: CanPromote[np.uint8] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_c8: CanPromote[np.uint8] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_c16: CanPromote[np.uint8] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_cld: CanPromote[np.uint8] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u1_to_b1: CanPromote[Any, np.uint8] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_to_i1: CanPromote[Any, np.uint8] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_to_u1: CanPromote[Any, np.uint8] = u1
u1_to_i2: CanPromote[Any, np.uint8] = i2
u1_to_u2: CanPromote[Any, np.uint8] = u2
u1_to_i4: CanPromote[Any, np.uint8] = i4
u1_to_u4: CanPromote[Any, np.uint8] = u4
u1_to_i8: CanPromote[Any, np.uint8] = i8
u1_to_u8: CanPromote[Any, np.uint8] = u8
u1_to_f2: CanPromote[Any, np.uint8] = f2
u1_to_f4: CanPromote[Any, np.uint8] = f4
u1_to_f8: CanPromote[Any, np.uint8] = f8
u1_to_ld: CanPromote[Any, np.uint8] = ld
u1_to_c8: CanPromote[Any, np.uint8] = c8
u1_to_c16: CanPromote[Any, np.uint8] = c16
u1_to_cld: CanPromote[Any, np.uint8] = cld

i2_from_b1: CanPromote[np.int16] = b1
i2_from_i1: CanPromote[np.int16] = i1
i2_from_u1: CanPromote[np.int16] = u1
i2_from_i2: CanPromote[np.int16] = i2
i2_from_u2: CanPromote[np.int16] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_i4: CanPromote[np.int16] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_u4: CanPromote[np.int16] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_i8: CanPromote[np.int16] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_u8: CanPromote[np.int16] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f2: CanPromote[np.int16] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f4: CanPromote[np.int16] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f8: CanPromote[np.int16] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_ld: CanPromote[np.int16] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_c8: CanPromote[np.int16] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_c16: CanPromote[np.int16] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_cld: CanPromote[np.int16] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i2_to_b1: CanPromote[Any, np.int16] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i1: CanPromote[Any, np.int16] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_u1: CanPromote[Any, np.int16] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i2: CanPromote[Any, np.int16] = i2
i2_to_u2: CanPromote[Any, np.int16] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i4: CanPromote[Any, np.int16] = i4
i2_to_u4: CanPromote[Any, np.int16] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i8: CanPromote[Any, np.int16] = i8
i2_to_u8: CanPromote[Any, np.int16] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_f2: CanPromote[Any, np.int16] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_f4: CanPromote[Any, np.int16] = f4
i2_to_f8: CanPromote[Any, np.int16] = f8
i2_to_ld: CanPromote[Any, np.int16] = ld
i2_to_c8: CanPromote[Any, np.int16] = c8
i2_to_c16: CanPromote[Any, np.int16] = c16
i2_to_cld: CanPromote[Any, np.int16] = cld

u2_from_b1: CanPromote[np.uint16] = b1
u2_from_i1: CanPromote[np.uint16] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u1: CanPromote[np.uint16] = u1
u2_from_i2: CanPromote[np.uint16] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u2: CanPromote[np.uint16] = u2
u2_from_i4: CanPromote[np.uint16] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u4: CanPromote[np.uint16] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_i8: CanPromote[np.uint16] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u8: CanPromote[np.uint16] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f2: CanPromote[np.uint16] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f4: CanPromote[np.uint16] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f8: CanPromote[np.uint16] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_ld: CanPromote[np.uint16] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_c8: CanPromote[np.uint16] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_c16: CanPromote[np.uint16] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_cld: CanPromote[np.uint16] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u2_to_b1: CanPromote[Any, np.uint16] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_i1: CanPromote[Any, np.uint16] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_u1: CanPromote[Any, np.uint16] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_i2: CanPromote[Any, np.uint16] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_u2: CanPromote[Any, np.uint16] = u2
u2_to_i4: CanPromote[Any, np.uint16] = i4
u2_to_u4: CanPromote[Any, np.uint16] = u4
u2_to_i8: CanPromote[Any, np.uint16] = i8
u2_to_u8: CanPromote[Any, np.uint16] = u8
u2_to_f2: CanPromote[Any, np.uint16] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_f4: CanPromote[Any, np.uint16] = f4
u2_to_f8: CanPromote[Any, np.uint16] = f8
u2_to_ld: CanPromote[Any, np.uint16] = ld
u2_to_c8: CanPromote[Any, np.uint16] = c8
u2_to_c16: CanPromote[Any, np.uint16] = c16
u2_to_cld: CanPromote[Any, np.uint16] = cld

i4_from_b1: CanPromote[np.int32] = b1
i4_from_i1: CanPromote[np.int32] = i1
i4_from_u1: CanPromote[np.int32] = u1
i4_from_i2: CanPromote[np.int32] = i2
i4_from_u2: CanPromote[np.int32] = u2
i4_from_i4: CanPromote[np.int32] = i4
i4_from_u4: CanPromote[np.int32] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_i8: CanPromote[np.int32] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_u8: CanPromote[np.int32] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f2: CanPromote[np.int32] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f4: CanPromote[np.int32] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f8: CanPromote[np.int32] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_ld: CanPromote[np.int32] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_c8: CanPromote[np.int32] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_c16: CanPromote[np.int32] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_cld: CanPromote[np.int32] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i4_to_b1: CanPromote[Any, np.int32] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i1: CanPromote[Any, np.int32] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_u1: CanPromote[Any, np.int32] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i2: CanPromote[Any, np.int32] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_u2: CanPromote[Any, np.int32] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i4: CanPromote[Any, np.int32] = i4
i4_to_u4: CanPromote[Any, np.int32] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i8: CanPromote[Any, np.int32] = i8
i4_to_u8: CanPromote[Any, np.int32] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f2: CanPromote[Any, np.int32] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f4: CanPromote[Any, np.int32] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f8: CanPromote[Any, np.int32] = f8
i4_to_ld: CanPromote[Any, np.int32] = ld
i4_to_c8: CanPromote[Any, np.int32] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_c16: CanPromote[Any, np.int32] = c16
i4_to_cld: CanPromote[Any, np.int32] = cld

u4_from_b1: CanPromote[np.uint32] = b1
u4_from_i1: CanPromote[np.uint32] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u1: CanPromote[np.uint32] = u1
u4_from_i2: CanPromote[np.uint32] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u2: CanPromote[np.uint32] = u2
u4_from_i4: CanPromote[np.uint32] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u4: CanPromote[np.uint32] = u4
u4_from_i8: CanPromote[np.uint32] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u8: CanPromote[np.uint32] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f2: CanPromote[np.uint32] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f4: CanPromote[np.uint32] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f8: CanPromote[np.uint32] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_ld: CanPromote[np.uint32] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_c8: CanPromote[np.uint32] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_c16: CanPromote[np.uint32] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_cld: CanPromote[np.uint32] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u4_to_b1: CanPromote[Any, np.uint32] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i1: CanPromote[Any, np.uint32] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u1: CanPromote[Any, np.uint32] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i2: CanPromote[Any, np.uint32] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u2: CanPromote[Any, np.uint32] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i4: CanPromote[Any, np.uint32] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u4: CanPromote[Any, np.uint32] = u4
u4_to_i8: CanPromote[Any, np.uint32] = i8
u4_to_u8: CanPromote[Any, np.uint32] = u8
u4_to_f2: CanPromote[Any, np.uint32] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_f4: CanPromote[Any, np.uint32] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_f8: CanPromote[Any, np.uint32] = f8
u4_to_ld: CanPromote[Any, np.uint32] = ld
u4_to_c8: CanPromote[Any, np.uint32] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_c16: CanPromote[Any, np.uint32] = c16
u4_to_cld: CanPromote[Any, np.uint32] = cld

i8_from_b1: CanPromote[np.int64] = b1
i8_from_i1: CanPromote[np.int64] = i1
i8_from_u1: CanPromote[np.int64] = u1
i8_from_i2: CanPromote[np.int64] = i2
i8_from_u2: CanPromote[np.int64] = u2
i8_from_i4: CanPromote[np.int64] = i4
i8_from_u4: CanPromote[np.int64] = u4
i8_from_i8: CanPromote[np.int64] = i8
i8_from_u8: CanPromote[np.int64] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f2: CanPromote[np.int64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f4: CanPromote[np.int64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f8: CanPromote[np.int64] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_ld: CanPromote[np.int64] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_c8: CanPromote[np.int64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_c16: CanPromote[np.int64] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_cld: CanPromote[np.int64] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i8_to_b1: CanPromote[Any, np.int64] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i1: CanPromote[Any, np.int64] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u1: CanPromote[Any, np.int64] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i2: CanPromote[Any, np.int64] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u2: CanPromote[Any, np.int64] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i4: CanPromote[Any, np.int64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u4: CanPromote[Any, np.int64] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i8: CanPromote[Any, np.int64] = i8
i8_to_u8: CanPromote[Any, np.int64] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f2: CanPromote[Any, np.int64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f4: CanPromote[Any, np.int64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f8: CanPromote[Any, np.int64] = f8
i8_to_ld: CanPromote[Any, np.int64] = ld
i8_to_c8: CanPromote[Any, np.int64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_c16: CanPromote[Any, np.int64] = c16
i8_to_cld: CanPromote[Any, np.int64] = cld

u8_from_b1: CanPromote[np.uint64] = b1
u8_from_i1: CanPromote[np.uint64] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u1: CanPromote[np.uint64] = u1
u8_from_i2: CanPromote[np.uint64] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u2: CanPromote[np.uint64] = u2
u8_from_i4: CanPromote[np.uint64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u4: CanPromote[np.uint64] = u4
u8_from_i8: CanPromote[np.uint64] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u8: CanPromote[np.uint64] = u8
u8_from_f2: CanPromote[np.uint64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_f4: CanPromote[np.uint64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_f8: CanPromote[np.uint64] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_ld: CanPromote[np.uint64] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_c8: CanPromote[np.uint64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_c16: CanPromote[np.uint64] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_cld: CanPromote[np.uint64] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u8_to_b1: CanPromote[Any, np.uint64] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i1: CanPromote[Any, np.uint64] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u1: CanPromote[Any, np.uint64] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i2: CanPromote[Any, np.uint64] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u2: CanPromote[Any, np.uint64] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i4: CanPromote[Any, np.uint64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u4: CanPromote[Any, np.uint64] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i8: CanPromote[Any, np.uint64] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u8: CanPromote[Any, np.uint64] = u8
u8_to_f2: CanPromote[Any, np.uint64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_f4: CanPromote[Any, np.uint64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_f8: CanPromote[Any, np.uint64] = f8
u8_to_ld: CanPromote[Any, np.uint64] = ld
u8_to_c8: CanPromote[Any, np.uint64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_c16: CanPromote[Any, np.uint64] = c16
u8_to_cld: CanPromote[Any, np.uint64] = cld

f2_from_b1: CanPromote[np.float16] = b1
f2_from_i1: CanPromote[np.float16] = i1
f2_from_u1: CanPromote[np.float16] = u1
f2_from_i2: CanPromote[np.float16] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u2: CanPromote[np.float16] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_i4: CanPromote[np.float16] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u4: CanPromote[np.float16] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_i8: CanPromote[np.float16] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u8: CanPromote[np.float16] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_f2: CanPromote[np.float16] = f2
f2_from_f4: CanPromote[np.float16] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_f8: CanPromote[np.float16] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_ld: CanPromote[np.float16] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_c8: CanPromote[np.float16] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_c16: CanPromote[np.float16] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_cld: CanPromote[np.float16] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f2_to_b1: CanPromote[Any, np.float16] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i1: CanPromote[Any, np.float16] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u1: CanPromote[Any, np.float16] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i2: CanPromote[Any, np.float16] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u2: CanPromote[Any, np.float16] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i4: CanPromote[Any, np.float16] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u4: CanPromote[Any, np.float16] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i8: CanPromote[Any, np.float16] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u8: CanPromote[Any, np.float16] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_f2: CanPromote[Any, np.float16] = f2
f2_to_f4: CanPromote[Any, np.float16] = f4
f2_to_f8: CanPromote[Any, np.float16] = f8
f2_to_ld: CanPromote[Any, np.float16] = ld
f2_to_c8: CanPromote[Any, np.float16] = c8
f2_to_c16: CanPromote[Any, np.float16] = c16
f2_to_cld: CanPromote[Any, np.float16] = cld

f4_from_b1: CanPromote[np.float32] = b1
f4_from_i1: CanPromote[np.float32] = i1
f4_from_u1: CanPromote[np.float32] = u1
f4_from_i2: CanPromote[np.float32] = i2
f4_from_u2: CanPromote[np.float32] = u2
f4_from_i4: CanPromote[np.float32] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_u4: CanPromote[np.float32] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_i8: CanPromote[np.float32] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_u8: CanPromote[np.float32] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_f2: CanPromote[np.float32] = f2
f4_from_f4: CanPromote[np.float32] = f4
f4_from_f8: CanPromote[np.float32] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_ld: CanPromote[np.float32] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_c8: CanPromote[np.float32] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_c16: CanPromote[np.float32] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_cld: CanPromote[np.float32] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f4_to_b1: CanPromote[Any, np.float32] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i1: CanPromote[Any, np.float32] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u1: CanPromote[Any, np.float32] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i2: CanPromote[Any, np.float32] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u2: CanPromote[Any, np.float32] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i4: CanPromote[Any, np.float32] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u4: CanPromote[Any, np.float32] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i8: CanPromote[Any, np.float32] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u8: CanPromote[Any, np.float32] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_f2: CanPromote[Any, np.float32] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_f4: CanPromote[Any, np.float32] = f4
f4_to_f8: CanPromote[Any, np.float32] = f8
f4_to_ld: CanPromote[Any, np.float32] = ld
f4_to_c8: CanPromote[Any, np.float32] = c8
f4_to_c16: CanPromote[Any, np.float32] = c16
f4_to_cld: CanPromote[Any, np.float32] = cld

f8_from_b1: CanPromote[np.float64] = b1
f8_from_i1: CanPromote[np.float64] = i1
f8_from_u1: CanPromote[np.float64] = u1
f8_from_i2: CanPromote[np.float64] = i2
f8_from_u2: CanPromote[np.float64] = u2
f8_from_i4: CanPromote[np.float64] = i4
f8_from_u4: CanPromote[np.float64] = u4
f8_from_i8: CanPromote[np.float64] = i8
f8_from_u8: CanPromote[np.float64] = u8
f8_from_f2: CanPromote[np.float64] = f2
f8_from_f4: CanPromote[np.float64] = f4
f8_from_f8: CanPromote[np.float64] = f8
f8_from_ld: CanPromote[np.float64] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_c8: CanPromote[np.float64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_c16: CanPromote[np.float64] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_cld: CanPromote[np.float64] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f8_to_b1: CanPromote[Any, np.float64] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i1: CanPromote[Any, np.float64] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u1: CanPromote[Any, np.float64] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i2: CanPromote[Any, np.float64] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u2: CanPromote[Any, np.float64] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i4: CanPromote[Any, np.float64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u4: CanPromote[Any, np.float64] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i8: CanPromote[Any, np.float64] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u8: CanPromote[Any, np.float64] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f2: CanPromote[Any, np.float64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f4: CanPromote[Any, np.float64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f8: CanPromote[Any, np.float64] = f8
f8_to_ld: CanPromote[Any, np.float64] = ld
f8_to_c8: CanPromote[Any, np.float64] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_c16: CanPromote[Any, np.float64] = c16
f8_to_cld: CanPromote[Any, np.float64] = cld

ld_from_b1: CanPromote[np.longdouble] = b1
ld_from_i1: CanPromote[np.longdouble] = i1
ld_from_u1: CanPromote[np.longdouble] = u1
ld_from_i2: CanPromote[np.longdouble] = i2
ld_from_u2: CanPromote[np.longdouble] = u2
ld_from_i4: CanPromote[np.longdouble] = i4
ld_from_u4: CanPromote[np.longdouble] = u4
ld_from_i8: CanPromote[np.longdouble] = i8
ld_from_u8: CanPromote[np.longdouble] = u8
ld_from_f2: CanPromote[np.longdouble] = f2
ld_from_f4: CanPromote[np.longdouble] = f4
ld_from_f8: CanPromote[np.longdouble] = f8
ld_from_ld: CanPromote[np.longdouble] = ld
ld_from_c8: CanPromote[np.longdouble] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_from_c16: CanPromote[np.longdouble] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_from_cld: CanPromote[np.longdouble] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

ld_to_b1: CanPromote[Any, np.longdouble] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i1: CanPromote[Any, np.longdouble] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u1: CanPromote[Any, np.longdouble] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i2: CanPromote[Any, np.longdouble] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u2: CanPromote[Any, np.longdouble] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i4: CanPromote[Any, np.longdouble] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u4: CanPromote[Any, np.longdouble] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i8: CanPromote[Any, np.longdouble] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u8: CanPromote[Any, np.longdouble] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f2: CanPromote[Any, np.longdouble] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f4: CanPromote[Any, np.longdouble] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f8: CanPromote[Any, np.longdouble] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_ld: CanPromote[Any, np.longdouble] = ld
ld_to_c8: CanPromote[Any, np.longdouble] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_c16: CanPromote[Any, np.longdouble] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_cld: CanPromote[Any, np.longdouble] = cld

c8_from_b1: CanPromote[np.complex64] = b1
c8_from_i1: CanPromote[np.complex64] = i1
c8_from_u1: CanPromote[np.complex64] = u1
c8_from_i2: CanPromote[np.complex64] = i2
c8_from_u2: CanPromote[np.complex64] = u2
c8_from_i4: CanPromote[np.complex64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_u4: CanPromote[np.complex64] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_i8: CanPromote[np.complex64] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_u8: CanPromote[np.complex64] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_f2: CanPromote[np.complex64] = f2
c8_from_f4: CanPromote[np.complex64] = f4
c8_from_f8: CanPromote[np.complex64] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_ld: CanPromote[np.complex64] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_c8: CanPromote[np.complex64] = c8
c8_from_c16: CanPromote[np.complex64] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_cld: CanPromote[np.complex64] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

c8_to_b1: CanPromote[Any, np.complex64] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i1: CanPromote[Any, np.complex64] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u1: CanPromote[Any, np.complex64] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i2: CanPromote[Any, np.complex64] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u2: CanPromote[Any, np.complex64] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i4: CanPromote[Any, np.complex64] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u4: CanPromote[Any, np.complex64] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i8: CanPromote[Any, np.complex64] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u8: CanPromote[Any, np.complex64] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f2: CanPromote[Any, np.complex64] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f4: CanPromote[Any, np.complex64] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f8: CanPromote[Any, np.complex64] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_ld: CanPromote[Any, np.complex64] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_c8: CanPromote[Any, np.complex64] = c8
c8_to_c16: CanPromote[Any, np.complex64] = c16
c8_to_cld: CanPromote[Any, np.complex64] = cld

c16_from_b1: CanPromote[np.complex128] = b1
c16_from_i1: CanPromote[np.complex128] = i1
c16_from_u1: CanPromote[np.complex128] = u1
c16_from_i2: CanPromote[np.complex128] = i2
c16_from_u2: CanPromote[np.complex128] = u2
c16_from_i4: CanPromote[np.complex128] = i4
c16_from_u4: CanPromote[np.complex128] = u4
c16_from_i8: CanPromote[np.complex128] = i8
c16_from_u8: CanPromote[np.complex128] = u8
c16_from_f2: CanPromote[np.complex128] = f2
c16_from_f4: CanPromote[np.complex128] = f4
c16_from_f8: CanPromote[np.complex128] = f8
c16_from_ld: CanPromote[np.complex128] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_from_c8: CanPromote[np.complex128] = c8
c16_from_c16: CanPromote[np.complex128] = c16
c16_from_cld: CanPromote[np.complex128] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

c16_to_b1: CanPromote[Any, np.complex128] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i1: CanPromote[Any, np.complex128] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u1: CanPromote[Any, np.complex128] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i2: CanPromote[Any, np.complex128] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u2: CanPromote[Any, np.complex128] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i4: CanPromote[Any, np.complex128] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u4: CanPromote[Any, np.complex128] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i8: CanPromote[Any, np.complex128] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u8: CanPromote[Any, np.complex128] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f2: CanPromote[Any, np.complex128] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f4: CanPromote[Any, np.complex128] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f8: CanPromote[Any, np.complex128] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_ld: CanPromote[Any, np.complex128] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_c8: CanPromote[Any, np.complex128] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_c16: CanPromote[Any, np.complex128] = c16
c16_to_cld: CanPromote[Any, np.complex128] = cld

cld_from_b1: CanPromote[np.clongdouble] = b1
cld_from_i1: CanPromote[np.clongdouble] = i1
cld_from_u1: CanPromote[np.clongdouble] = u1
cld_from_i2: CanPromote[np.clongdouble] = i2
cld_from_u2: CanPromote[np.clongdouble] = u2
cld_from_i4: CanPromote[np.clongdouble] = i4
cld_from_u4: CanPromote[np.clongdouble] = u4
cld_from_i8: CanPromote[np.clongdouble] = i8
cld_from_u8: CanPromote[np.clongdouble] = u8
cld_from_f2: CanPromote[np.clongdouble] = f2
cld_from_f4: CanPromote[np.clongdouble] = f4
cld_from_f8: CanPromote[np.clongdouble] = f8
cld_from_ld: CanPromote[np.clongdouble] = ld
cld_from_c8: CanPromote[np.clongdouble] = c8
cld_from_c16: CanPromote[np.clongdouble] = c16
cld_from_cld: CanPromote[np.clongdouble] = cld

cld_to_b1: CanPromote[Any, np.clongdouble] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i1: CanPromote[Any, np.clongdouble] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u1: CanPromote[Any, np.clongdouble] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i2: CanPromote[Any, np.clongdouble] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u2: CanPromote[Any, np.clongdouble] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i4: CanPromote[Any, np.clongdouble] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u4: CanPromote[Any, np.clongdouble] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i8: CanPromote[Any, np.clongdouble] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u8: CanPromote[Any, np.clongdouble] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f2: CanPromote[Any, np.clongdouble] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f4: CanPromote[Any, np.clongdouble] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f8: CanPromote[Any, np.clongdouble] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_ld: CanPromote[Any, np.clongdouble] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_c8: CanPromote[Any, np.clongdouble] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_c16: CanPromote[Any, np.clongdouble] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_cld: CanPromote[Any, np.clongdouble] = cld
