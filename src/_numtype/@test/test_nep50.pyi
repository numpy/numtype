from typing import Any

import numpy as np
from _numtype._nep50 import _CanNEP50

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

b1_from_b1: _CanNEP50[np.bool, Any, Any] = b1
b1_from_i1: _CanNEP50[np.bool, Any, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u1: _CanNEP50[np.bool, Any, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i2: _CanNEP50[np.bool, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u2: _CanNEP50[np.bool, Any, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i4: _CanNEP50[np.bool, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u4: _CanNEP50[np.bool, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_i8: _CanNEP50[np.bool, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_u8: _CanNEP50[np.bool, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f2: _CanNEP50[np.bool, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f4: _CanNEP50[np.bool, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_f8: _CanNEP50[np.bool, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_ld: _CanNEP50[np.bool, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_c8: _CanNEP50[np.bool, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_c16: _CanNEP50[np.bool, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_from_cld: _CanNEP50[np.bool, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

b1_to_b1: _CanNEP50[Any, np.bool, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
b1_to_i1: _CanNEP50[Any, np.bool, Any] = i1
b1_to_u1: _CanNEP50[Any, np.bool, Any] = u1
b1_to_i2: _CanNEP50[Any, np.bool, Any] = i2
b1_to_u2: _CanNEP50[Any, np.bool, Any] = u2
b1_to_i4: _CanNEP50[Any, np.bool, Any] = i4
b1_to_u4: _CanNEP50[Any, np.bool, Any] = u4
b1_to_i8: _CanNEP50[Any, np.bool, Any] = i8
b1_to_u8: _CanNEP50[Any, np.bool, Any] = u8
b1_to_f2: _CanNEP50[Any, np.bool, Any] = f2
b1_to_f4: _CanNEP50[Any, np.bool, Any] = f4
b1_to_f8: _CanNEP50[Any, np.bool, Any] = f8
b1_to_ld: _CanNEP50[Any, np.bool, Any] = ld
b1_to_c8: _CanNEP50[Any, np.bool, Any] = c8
b1_to_c16: _CanNEP50[Any, np.bool, Any] = c16
b1_to_cld: _CanNEP50[Any, np.bool, Any] = cld

i1_from_b1: _CanNEP50[np.int8, Any, Any] = b1
i1_from_i1: _CanNEP50[np.int8, Any, Any] = i1
i1_from_u1: _CanNEP50[np.int8, Any, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i2: _CanNEP50[np.int8, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u2: _CanNEP50[np.int8, Any, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i4: _CanNEP50[np.int8, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u4: _CanNEP50[np.int8, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_i8: _CanNEP50[np.int8, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_u8: _CanNEP50[np.int8, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f2: _CanNEP50[np.int8, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f4: _CanNEP50[np.int8, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_f8: _CanNEP50[np.int8, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_ld: _CanNEP50[np.int8, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_c8: _CanNEP50[np.int8, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_c16: _CanNEP50[np.int8, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_from_cld: _CanNEP50[np.int8, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i1_to_b1: _CanNEP50[Any, np.int8, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i1: _CanNEP50[Any, np.int8, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_u1: _CanNEP50[Any, np.int8, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i2: _CanNEP50[Any, np.int8, Any] = i2
i1_to_u2: _CanNEP50[Any, np.int8, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i4: _CanNEP50[Any, np.int8, Any] = i4
i1_to_u4: _CanNEP50[Any, np.int8, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_i8: _CanNEP50[Any, np.int8, Any] = i8
i1_to_u8: _CanNEP50[Any, np.int8, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i1_to_f2: _CanNEP50[Any, np.int8, Any] = f2
i1_to_f4: _CanNEP50[Any, np.int8, Any] = f4
i1_to_f8: _CanNEP50[Any, np.int8, Any] = f8
i1_to_ld: _CanNEP50[Any, np.int8, Any] = ld
i1_to_c8: _CanNEP50[Any, np.int8, Any] = c8
i1_to_c16: _CanNEP50[Any, np.int8, Any] = c16
i1_to_cld: _CanNEP50[Any, np.int8, Any] = cld

u1_from_b1: _CanNEP50[np.uint8, Any, Any] = b1
u1_from_i1: _CanNEP50[np.uint8, Any, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u1: _CanNEP50[np.uint8, Any, Any] = u1
u1_from_i2: _CanNEP50[np.uint8, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u2: _CanNEP50[np.uint8, Any, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_i4: _CanNEP50[np.uint8, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u4: _CanNEP50[np.uint8, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_i8: _CanNEP50[np.uint8, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_u8: _CanNEP50[np.uint8, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f2: _CanNEP50[np.uint8, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f4: _CanNEP50[np.uint8, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_f8: _CanNEP50[np.uint8, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_ld: _CanNEP50[np.uint8, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_c8: _CanNEP50[np.uint8, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_c16: _CanNEP50[np.uint8, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_from_cld: _CanNEP50[np.uint8, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u1_to_b1: _CanNEP50[Any, np.uint8, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_to_i1: _CanNEP50[Any, np.uint8, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_to_u1: _CanNEP50[Any, np.uint8, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u1_to_i2: _CanNEP50[Any, np.uint8, Any] = i2
u1_to_u2: _CanNEP50[Any, np.uint8, Any] = u2
u1_to_i4: _CanNEP50[Any, np.uint8, Any] = i4
u1_to_u4: _CanNEP50[Any, np.uint8, Any] = u4
u1_to_i8: _CanNEP50[Any, np.uint8, Any] = i8
u1_to_u8: _CanNEP50[Any, np.uint8, Any] = u8
u1_to_f2: _CanNEP50[Any, np.uint8, Any] = f2
u1_to_f4: _CanNEP50[Any, np.uint8, Any] = f4
u1_to_f8: _CanNEP50[Any, np.uint8, Any] = f8
u1_to_ld: _CanNEP50[Any, np.uint8, Any] = ld
u1_to_c8: _CanNEP50[Any, np.uint8, Any] = c8
u1_to_c16: _CanNEP50[Any, np.uint8, Any] = c16
u1_to_cld: _CanNEP50[Any, np.uint8, Any] = cld

i2_from_b1: _CanNEP50[np.int16, Any, Any] = b1
i2_from_i1: _CanNEP50[np.int16, Any, Any] = i1
i2_from_u1: _CanNEP50[np.int16, Any, Any] = u1
i2_from_i2: _CanNEP50[np.int16, Any, Any] = i2
i2_from_u2: _CanNEP50[np.int16, Any, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_i4: _CanNEP50[np.int16, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_u4: _CanNEP50[np.int16, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_i8: _CanNEP50[np.int16, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_u8: _CanNEP50[np.int16, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f2: _CanNEP50[np.int16, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f4: _CanNEP50[np.int16, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_f8: _CanNEP50[np.int16, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_ld: _CanNEP50[np.int16, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_c8: _CanNEP50[np.int16, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_c16: _CanNEP50[np.int16, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_from_cld: _CanNEP50[np.int16, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i2_to_b1: _CanNEP50[Any, np.int16, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i1: _CanNEP50[Any, np.int16, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_u1: _CanNEP50[Any, np.int16, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i2: _CanNEP50[Any, np.int16, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_u2: _CanNEP50[Any, np.int16, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i4: _CanNEP50[Any, np.int16, Any] = i4
i2_to_u4: _CanNEP50[Any, np.int16, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_i8: _CanNEP50[Any, np.int16, Any] = i8
i2_to_u8: _CanNEP50[Any, np.int16, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_f2: _CanNEP50[Any, np.int16, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i2_to_f4: _CanNEP50[Any, np.int16, Any] = f4
i2_to_f8: _CanNEP50[Any, np.int16, Any] = f8
i2_to_ld: _CanNEP50[Any, np.int16, Any] = ld
i2_to_c8: _CanNEP50[Any, np.int16, Any] = c8
i2_to_c16: _CanNEP50[Any, np.int16, Any] = c16
i2_to_cld: _CanNEP50[Any, np.int16, Any] = cld

u2_from_b1: _CanNEP50[np.uint16, Any, Any] = b1
u2_from_i1: _CanNEP50[np.uint16, Any, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u1: _CanNEP50[np.uint16, Any, Any] = u1
u2_from_i2: _CanNEP50[np.uint16, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u2: _CanNEP50[np.uint16, Any, Any] = u2
u2_from_i4: _CanNEP50[np.uint16, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u4: _CanNEP50[np.uint16, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_i8: _CanNEP50[np.uint16, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_u8: _CanNEP50[np.uint16, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f2: _CanNEP50[np.uint16, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f4: _CanNEP50[np.uint16, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_f8: _CanNEP50[np.uint16, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_ld: _CanNEP50[np.uint16, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_c8: _CanNEP50[np.uint16, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_c16: _CanNEP50[np.uint16, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_from_cld: _CanNEP50[np.uint16, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u2_to_b1: _CanNEP50[Any, np.uint16, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_i1: _CanNEP50[Any, np.uint16, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_u1: _CanNEP50[Any, np.uint16, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_i2: _CanNEP50[Any, np.uint16, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_u2: _CanNEP50[Any, np.uint16, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_i4: _CanNEP50[Any, np.uint16, Any] = i4
u2_to_u4: _CanNEP50[Any, np.uint16, Any] = u4
u2_to_i8: _CanNEP50[Any, np.uint16, Any] = i8
u2_to_u8: _CanNEP50[Any, np.uint16, Any] = u8
u2_to_f2: _CanNEP50[Any, np.uint16, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u2_to_f4: _CanNEP50[Any, np.uint16, Any] = f4
u2_to_f8: _CanNEP50[Any, np.uint16, Any] = f8
u2_to_ld: _CanNEP50[Any, np.uint16, Any] = ld
u2_to_c8: _CanNEP50[Any, np.uint16, Any] = c8
u2_to_c16: _CanNEP50[Any, np.uint16, Any] = c16
u2_to_cld: _CanNEP50[Any, np.uint16, Any] = cld

i4_from_b1: _CanNEP50[np.int32, Any, Any] = b1
i4_from_i1: _CanNEP50[np.int32, Any, Any] = i1
i4_from_u1: _CanNEP50[np.int32, Any, Any] = u1
i4_from_i2: _CanNEP50[np.int32, Any, Any] = i2
i4_from_u2: _CanNEP50[np.int32, Any, Any] = u2
i4_from_i4: _CanNEP50[np.int32, Any, Any] = i4
i4_from_u4: _CanNEP50[np.int32, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_i8: _CanNEP50[np.int32, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_u8: _CanNEP50[np.int32, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f2: _CanNEP50[np.int32, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f4: _CanNEP50[np.int32, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_f8: _CanNEP50[np.int32, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_ld: _CanNEP50[np.int32, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_c8: _CanNEP50[np.int32, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_c16: _CanNEP50[np.int32, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_from_cld: _CanNEP50[np.int32, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i4_to_b1: _CanNEP50[Any, np.int32, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i1: _CanNEP50[Any, np.int32, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_u1: _CanNEP50[Any, np.int32, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i2: _CanNEP50[Any, np.int32, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_u2: _CanNEP50[Any, np.int32, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i4: _CanNEP50[Any, np.int32, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_u4: _CanNEP50[Any, np.int32, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_i8: _CanNEP50[Any, np.int32, Any] = i8
i4_to_u8: _CanNEP50[Any, np.int32, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f2: _CanNEP50[Any, np.int32, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f4: _CanNEP50[Any, np.int32, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_f8: _CanNEP50[Any, np.int32, Any] = f8
i4_to_ld: _CanNEP50[Any, np.int32, Any] = ld
i4_to_c8: _CanNEP50[Any, np.int32, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i4_to_c16: _CanNEP50[Any, np.int32, Any] = c16
i4_to_cld: _CanNEP50[Any, np.int32, Any] = cld

u4_from_b1: _CanNEP50[np.uint32, Any, Any] = b1
u4_from_i1: _CanNEP50[np.uint32, Any, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u1: _CanNEP50[np.uint32, Any, Any] = u1
u4_from_i2: _CanNEP50[np.uint32, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u2: _CanNEP50[np.uint32, Any, Any] = u2
u4_from_i4: _CanNEP50[np.uint32, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u4: _CanNEP50[np.uint32, Any, Any] = u4
u4_from_i8: _CanNEP50[np.uint32, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_u8: _CanNEP50[np.uint32, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f2: _CanNEP50[np.uint32, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f4: _CanNEP50[np.uint32, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_f8: _CanNEP50[np.uint32, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_ld: _CanNEP50[np.uint32, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_c8: _CanNEP50[np.uint32, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_c16: _CanNEP50[np.uint32, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_from_cld: _CanNEP50[np.uint32, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u4_to_b1: _CanNEP50[Any, np.uint32, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i1: _CanNEP50[Any, np.uint32, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u1: _CanNEP50[Any, np.uint32, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i2: _CanNEP50[Any, np.uint32, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u2: _CanNEP50[Any, np.uint32, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i4: _CanNEP50[Any, np.uint32, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_u4: _CanNEP50[Any, np.uint32, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_i8: _CanNEP50[Any, np.uint32, Any] = i8
u4_to_u8: _CanNEP50[Any, np.uint32, Any] = u8
u4_to_f2: _CanNEP50[Any, np.uint32, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_f4: _CanNEP50[Any, np.uint32, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_f8: _CanNEP50[Any, np.uint32, Any] = f8
u4_to_ld: _CanNEP50[Any, np.uint32, Any] = ld
u4_to_c8: _CanNEP50[Any, np.uint32, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u4_to_c16: _CanNEP50[Any, np.uint32, Any] = c16
u4_to_cld: _CanNEP50[Any, np.uint32, Any] = cld

i8_from_b1: _CanNEP50[np.int64, Any, Any] = b1
i8_from_i1: _CanNEP50[np.int64, Any, Any] = i1
i8_from_u1: _CanNEP50[np.int64, Any, Any] = u1
i8_from_i2: _CanNEP50[np.int64, Any, Any] = i2
i8_from_u2: _CanNEP50[np.int64, Any, Any] = u2
i8_from_i4: _CanNEP50[np.int64, Any, Any] = i4
i8_from_u4: _CanNEP50[np.int64, Any, Any] = u4
i8_from_i8: _CanNEP50[np.int64, Any, Any] = i8
i8_from_u8: _CanNEP50[np.int64, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f2: _CanNEP50[np.int64, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f4: _CanNEP50[np.int64, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_f8: _CanNEP50[np.int64, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_ld: _CanNEP50[np.int64, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_c8: _CanNEP50[np.int64, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_c16: _CanNEP50[np.int64, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_from_cld: _CanNEP50[np.int64, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

i8_to_b1: _CanNEP50[Any, np.int64, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i1: _CanNEP50[Any, np.int64, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u1: _CanNEP50[Any, np.int64, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i2: _CanNEP50[Any, np.int64, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u2: _CanNEP50[Any, np.int64, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i4: _CanNEP50[Any, np.int64, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u4: _CanNEP50[Any, np.int64, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_i8: _CanNEP50[Any, np.int64, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_u8: _CanNEP50[Any, np.int64, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f2: _CanNEP50[Any, np.int64, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f4: _CanNEP50[Any, np.int64, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_f8: _CanNEP50[Any, np.int64, Any] = f8
i8_to_ld: _CanNEP50[Any, np.int64, Any] = ld
i8_to_c8: _CanNEP50[Any, np.int64, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
i8_to_c16: _CanNEP50[Any, np.int64, Any] = c16
i8_to_cld: _CanNEP50[Any, np.int64, Any] = cld

u8_from_b1: _CanNEP50[np.uint64, Any, Any] = b1
u8_from_i1: _CanNEP50[np.uint64, Any, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u1: _CanNEP50[np.uint64, Any, Any] = u1
u8_from_i2: _CanNEP50[np.uint64, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u2: _CanNEP50[np.uint64, Any, Any] = u2
u8_from_i4: _CanNEP50[np.uint64, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u4: _CanNEP50[np.uint64, Any, Any] = u4
u8_from_i8: _CanNEP50[np.uint64, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_u8: _CanNEP50[np.uint64, Any, Any] = u8
u8_from_f2: _CanNEP50[np.uint64, Any, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_f4: _CanNEP50[np.uint64, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_f8: _CanNEP50[np.uint64, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_ld: _CanNEP50[np.uint64, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_c8: _CanNEP50[np.uint64, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_c16: _CanNEP50[np.uint64, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_from_cld: _CanNEP50[np.uint64, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

u8_to_b1: _CanNEP50[Any, np.uint64, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i1: _CanNEP50[Any, np.uint64, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u1: _CanNEP50[Any, np.uint64, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i2: _CanNEP50[Any, np.uint64, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u2: _CanNEP50[Any, np.uint64, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i4: _CanNEP50[Any, np.uint64, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u4: _CanNEP50[Any, np.uint64, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_i8: _CanNEP50[Any, np.uint64, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_u8: _CanNEP50[Any, np.uint64, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_f2: _CanNEP50[Any, np.uint64, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_f4: _CanNEP50[Any, np.uint64, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_f8: _CanNEP50[Any, np.uint64, Any] = f8
u8_to_ld: _CanNEP50[Any, np.uint64, Any] = ld
u8_to_c8: _CanNEP50[Any, np.uint64, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
u8_to_c16: _CanNEP50[Any, np.uint64, Any] = c16
u8_to_cld: _CanNEP50[Any, np.uint64, Any] = cld

f2_from_b1: _CanNEP50[np.float16, Any, Any] = b1
f2_from_i1: _CanNEP50[np.float16, Any, Any] = i1
f2_from_u1: _CanNEP50[np.float16, Any, Any] = u1
f2_from_i2: _CanNEP50[np.float16, Any, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u2: _CanNEP50[np.float16, Any, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_i4: _CanNEP50[np.float16, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u4: _CanNEP50[np.float16, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_i8: _CanNEP50[np.float16, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_u8: _CanNEP50[np.float16, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_f2: _CanNEP50[np.float16, Any, Any] = f2
f2_from_f4: _CanNEP50[np.float16, Any, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_f8: _CanNEP50[np.float16, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_ld: _CanNEP50[np.float16, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_c8: _CanNEP50[np.float16, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_c16: _CanNEP50[np.float16, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_from_cld: _CanNEP50[np.float16, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f2_to_b1: _CanNEP50[Any, np.float16, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i1: _CanNEP50[Any, np.float16, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u1: _CanNEP50[Any, np.float16, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i2: _CanNEP50[Any, np.float16, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u2: _CanNEP50[Any, np.float16, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i4: _CanNEP50[Any, np.float16, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u4: _CanNEP50[Any, np.float16, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_i8: _CanNEP50[Any, np.float16, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_u8: _CanNEP50[Any, np.float16, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_f2: _CanNEP50[Any, np.float16, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f2_to_f4: _CanNEP50[Any, np.float16, Any] = f4
f2_to_f8: _CanNEP50[Any, np.float16, Any] = f8
f2_to_ld: _CanNEP50[Any, np.float16, Any] = ld
f2_to_c8: _CanNEP50[Any, np.float16, Any] = c8
f2_to_c16: _CanNEP50[Any, np.float16, Any] = c16
f2_to_cld: _CanNEP50[Any, np.float16, Any] = cld

f4_from_b1: _CanNEP50[np.float32, Any, Any] = b1
f4_from_i1: _CanNEP50[np.float32, Any, Any] = i1
f4_from_u1: _CanNEP50[np.float32, Any, Any] = u1
f4_from_i2: _CanNEP50[np.float32, Any, Any] = i2
f4_from_u2: _CanNEP50[np.float32, Any, Any] = u2
f4_from_i4: _CanNEP50[np.float32, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_u4: _CanNEP50[np.float32, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_i8: _CanNEP50[np.float32, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_u8: _CanNEP50[np.float32, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_f2: _CanNEP50[np.float32, Any, Any] = f2
f4_from_f4: _CanNEP50[np.float32, Any, Any] = f4
f4_from_f8: _CanNEP50[np.float32, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_ld: _CanNEP50[np.float32, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_c8: _CanNEP50[np.float32, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_c16: _CanNEP50[np.float32, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_from_cld: _CanNEP50[np.float32, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f4_to_b1: _CanNEP50[Any, np.float32, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i1: _CanNEP50[Any, np.float32, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u1: _CanNEP50[Any, np.float32, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i2: _CanNEP50[Any, np.float32, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u2: _CanNEP50[Any, np.float32, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i4: _CanNEP50[Any, np.float32, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u4: _CanNEP50[Any, np.float32, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_i8: _CanNEP50[Any, np.float32, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_u8: _CanNEP50[Any, np.float32, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_f2: _CanNEP50[Any, np.float32, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_f4: _CanNEP50[Any, np.float32, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f4_to_f8: _CanNEP50[Any, np.float32, Any] = f8
f4_to_ld: _CanNEP50[Any, np.float32, Any] = ld
f4_to_c8: _CanNEP50[Any, np.float32, Any] = c8
f4_to_c16: _CanNEP50[Any, np.float32, Any] = c16
f4_to_cld: _CanNEP50[Any, np.float32, Any] = cld

f8_from_b1: _CanNEP50[np.float64, Any, Any] = b1
f8_from_i1: _CanNEP50[np.float64, Any, Any] = i1
f8_from_u1: _CanNEP50[np.float64, Any, Any] = u1
f8_from_i2: _CanNEP50[np.float64, Any, Any] = i2
f8_from_u2: _CanNEP50[np.float64, Any, Any] = u2
f8_from_i4: _CanNEP50[np.float64, Any, Any] = i4
f8_from_u4: _CanNEP50[np.float64, Any, Any] = u4
f8_from_i8: _CanNEP50[np.float64, Any, Any] = i8
f8_from_u8: _CanNEP50[np.float64, Any, Any] = u8
f8_from_f2: _CanNEP50[np.float64, Any, Any] = f2
f8_from_f4: _CanNEP50[np.float64, Any, Any] = f4
f8_from_f8: _CanNEP50[np.float64, Any, Any] = f8
f8_from_ld: _CanNEP50[np.float64, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_c8: _CanNEP50[np.float64, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_c16: _CanNEP50[np.float64, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_from_cld: _CanNEP50[np.float64, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

f8_to_b1: _CanNEP50[Any, np.float64, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i1: _CanNEP50[Any, np.float64, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u1: _CanNEP50[Any, np.float64, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i2: _CanNEP50[Any, np.float64, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u2: _CanNEP50[Any, np.float64, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i4: _CanNEP50[Any, np.float64, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u4: _CanNEP50[Any, np.float64, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_i8: _CanNEP50[Any, np.float64, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_u8: _CanNEP50[Any, np.float64, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f2: _CanNEP50[Any, np.float64, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f4: _CanNEP50[Any, np.float64, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_f8: _CanNEP50[Any, np.float64, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_ld: _CanNEP50[Any, np.float64, Any] = ld
f8_to_c8: _CanNEP50[Any, np.float64, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
f8_to_c16: _CanNEP50[Any, np.float64, Any] = c16
f8_to_cld: _CanNEP50[Any, np.float64, Any] = cld

ld_from_b1: _CanNEP50[np.longdouble, Any, Any] = b1
ld_from_i1: _CanNEP50[np.longdouble, Any, Any] = i1
ld_from_u1: _CanNEP50[np.longdouble, Any, Any] = u1
ld_from_i2: _CanNEP50[np.longdouble, Any, Any] = i2
ld_from_u2: _CanNEP50[np.longdouble, Any, Any] = u2
ld_from_i4: _CanNEP50[np.longdouble, Any, Any] = i4
ld_from_u4: _CanNEP50[np.longdouble, Any, Any] = u4
ld_from_i8: _CanNEP50[np.longdouble, Any, Any] = i8
ld_from_u8: _CanNEP50[np.longdouble, Any, Any] = u8
ld_from_f2: _CanNEP50[np.longdouble, Any, Any] = f2
ld_from_f4: _CanNEP50[np.longdouble, Any, Any] = f4
ld_from_f8: _CanNEP50[np.longdouble, Any, Any] = f8
ld_from_ld: _CanNEP50[np.longdouble, Any, Any] = ld
ld_from_c8: _CanNEP50[np.longdouble, Any, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_from_c16: _CanNEP50[np.longdouble, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_from_cld: _CanNEP50[np.longdouble, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

ld_to_b1: _CanNEP50[Any, np.longdouble, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i1: _CanNEP50[Any, np.longdouble, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u1: _CanNEP50[Any, np.longdouble, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i2: _CanNEP50[Any, np.longdouble, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u2: _CanNEP50[Any, np.longdouble, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i4: _CanNEP50[Any, np.longdouble, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u4: _CanNEP50[Any, np.longdouble, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_i8: _CanNEP50[Any, np.longdouble, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_u8: _CanNEP50[Any, np.longdouble, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f2: _CanNEP50[Any, np.longdouble, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f4: _CanNEP50[Any, np.longdouble, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_f8: _CanNEP50[Any, np.longdouble, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_ld: _CanNEP50[Any, np.longdouble, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_c8: _CanNEP50[Any, np.longdouble, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_c16: _CanNEP50[Any, np.longdouble, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
ld_to_cld: _CanNEP50[Any, np.longdouble, Any] = cld

c8_from_b1: _CanNEP50[np.complex64, Any, Any] = b1
c8_from_i1: _CanNEP50[np.complex64, Any, Any] = i1
c8_from_u1: _CanNEP50[np.complex64, Any, Any] = u1
c8_from_i2: _CanNEP50[np.complex64, Any, Any] = i2
c8_from_u2: _CanNEP50[np.complex64, Any, Any] = u2
c8_from_i4: _CanNEP50[np.complex64, Any, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_u4: _CanNEP50[np.complex64, Any, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_i8: _CanNEP50[np.complex64, Any, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_u8: _CanNEP50[np.complex64, Any, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_f2: _CanNEP50[np.complex64, Any, Any] = f2
c8_from_f4: _CanNEP50[np.complex64, Any, Any] = f4
c8_from_f8: _CanNEP50[np.complex64, Any, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_ld: _CanNEP50[np.complex64, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_c8: _CanNEP50[np.complex64, Any, Any] = c8
c8_from_c16: _CanNEP50[np.complex64, Any, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_from_cld: _CanNEP50[np.complex64, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

c8_to_b1: _CanNEP50[Any, np.complex64, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i1: _CanNEP50[Any, np.complex64, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u1: _CanNEP50[Any, np.complex64, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i2: _CanNEP50[Any, np.complex64, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u2: _CanNEP50[Any, np.complex64, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i4: _CanNEP50[Any, np.complex64, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u4: _CanNEP50[Any, np.complex64, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_i8: _CanNEP50[Any, np.complex64, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_u8: _CanNEP50[Any, np.complex64, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f2: _CanNEP50[Any, np.complex64, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f4: _CanNEP50[Any, np.complex64, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_f8: _CanNEP50[Any, np.complex64, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_ld: _CanNEP50[Any, np.complex64, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_c8: _CanNEP50[Any, np.complex64, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c8_to_c16: _CanNEP50[Any, np.complex64, Any] = c16
c8_to_cld: _CanNEP50[Any, np.complex64, Any] = cld

c16_from_b1: _CanNEP50[np.complex128, Any, Any] = b1
c16_from_i1: _CanNEP50[np.complex128, Any, Any] = i1
c16_from_u1: _CanNEP50[np.complex128, Any, Any] = u1
c16_from_i2: _CanNEP50[np.complex128, Any, Any] = i2
c16_from_u2: _CanNEP50[np.complex128, Any, Any] = u2
c16_from_i4: _CanNEP50[np.complex128, Any, Any] = i4
c16_from_u4: _CanNEP50[np.complex128, Any, Any] = u4
c16_from_i8: _CanNEP50[np.complex128, Any, Any] = i8
c16_from_u8: _CanNEP50[np.complex128, Any, Any] = u8
c16_from_f2: _CanNEP50[np.complex128, Any, Any] = f2
c16_from_f4: _CanNEP50[np.complex128, Any, Any] = f4
c16_from_f8: _CanNEP50[np.complex128, Any, Any] = f8
c16_from_ld: _CanNEP50[np.complex128, Any, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_from_c8: _CanNEP50[np.complex128, Any, Any] = c8
c16_from_c16: _CanNEP50[np.complex128, Any, Any] = c16
c16_from_cld: _CanNEP50[np.complex128, Any, Any] = cld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

c16_to_b1: _CanNEP50[Any, np.complex128, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i1: _CanNEP50[Any, np.complex128, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u1: _CanNEP50[Any, np.complex128, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i2: _CanNEP50[Any, np.complex128, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u2: _CanNEP50[Any, np.complex128, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i4: _CanNEP50[Any, np.complex128, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u4: _CanNEP50[Any, np.complex128, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_i8: _CanNEP50[Any, np.complex128, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_u8: _CanNEP50[Any, np.complex128, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f2: _CanNEP50[Any, np.complex128, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f4: _CanNEP50[Any, np.complex128, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_f8: _CanNEP50[Any, np.complex128, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_ld: _CanNEP50[Any, np.complex128, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_c8: _CanNEP50[Any, np.complex128, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_c16: _CanNEP50[Any, np.complex128, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
c16_to_cld: _CanNEP50[Any, np.complex128, Any] = cld

cld_from_b1: _CanNEP50[np.clongdouble, Any, Any] = b1
cld_from_i1: _CanNEP50[np.clongdouble, Any, Any] = i1
cld_from_u1: _CanNEP50[np.clongdouble, Any, Any] = u1
cld_from_i2: _CanNEP50[np.clongdouble, Any, Any] = i2
cld_from_u2: _CanNEP50[np.clongdouble, Any, Any] = u2
cld_from_i4: _CanNEP50[np.clongdouble, Any, Any] = i4
cld_from_u4: _CanNEP50[np.clongdouble, Any, Any] = u4
cld_from_i8: _CanNEP50[np.clongdouble, Any, Any] = i8
cld_from_u8: _CanNEP50[np.clongdouble, Any, Any] = u8
cld_from_f2: _CanNEP50[np.clongdouble, Any, Any] = f2
cld_from_f4: _CanNEP50[np.clongdouble, Any, Any] = f4
cld_from_f8: _CanNEP50[np.clongdouble, Any, Any] = f8
cld_from_ld: _CanNEP50[np.clongdouble, Any, Any] = ld
cld_from_c8: _CanNEP50[np.clongdouble, Any, Any] = c8
cld_from_c16: _CanNEP50[np.clongdouble, Any, Any] = c16
cld_from_cld: _CanNEP50[np.clongdouble, Any, Any] = cld

cld_to_b1: _CanNEP50[Any, np.clongdouble, Any] = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i1: _CanNEP50[Any, np.clongdouble, Any] = i1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u1: _CanNEP50[Any, np.clongdouble, Any] = u1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i2: _CanNEP50[Any, np.clongdouble, Any] = i2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u2: _CanNEP50[Any, np.clongdouble, Any] = u2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i4: _CanNEP50[Any, np.clongdouble, Any] = i4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u4: _CanNEP50[Any, np.clongdouble, Any] = u4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_i8: _CanNEP50[Any, np.clongdouble, Any] = i8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_u8: _CanNEP50[Any, np.clongdouble, Any] = u8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f2: _CanNEP50[Any, np.clongdouble, Any] = f2  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f4: _CanNEP50[Any, np.clongdouble, Any] = f4  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_f8: _CanNEP50[Any, np.clongdouble, Any] = f8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_ld: _CanNEP50[Any, np.clongdouble, Any] = ld  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_c8: _CanNEP50[Any, np.clongdouble, Any] = c8  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_c16: _CanNEP50[Any, np.clongdouble, Any] = c16  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
cld_to_cld: _CanNEP50[Any, np.clongdouble, Any] = cld  # NOTE: allowing this simplifies the __nep50__ definition
