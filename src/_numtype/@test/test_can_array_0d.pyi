import _numtype as _nt
import numpy as np

###
# _ToArray1_0d

can_b1_0d: _nt.CanArray0D[np.bool] = np.bool()
can_i1_0d: _nt.CanArray0D[np.int8] = np.int8()
can_i2_0d: _nt.CanArray0D[np.int16] = np.int16()
can_i4_0d: _nt.CanArray0D[np.int32] = np.int32()
can_i8_0d: _nt.CanArray0D[np.int64] = np.int64()
can_u1_0d: _nt.CanArray0D[np.uint8] = np.uint8()
can_u2_0d: _nt.CanArray0D[np.uint16] = np.uint16()
can_u4_0d: _nt.CanArray0D[np.uint32] = np.uint32()
can_u8_0d: _nt.CanArray0D[np.uint64] = np.uint64()
can_f2_0d: _nt.CanArray0D[np.float16] = np.float16()
can_f4_0d: _nt.CanArray0D[np.float32] = np.float32()
can_f8_0d: _nt.CanArray0D[np.float64] = np.float64()
can_ld_0d: _nt.CanArray0D[np.longdouble] = np.longdouble()
can_c8_0d: _nt.CanArray0D[np.complex64] = np.complex64()
can_c16_0d: _nt.CanArray0D[np.complex128] = np.complex128()
can_cld_0d: _nt.CanArray0D[np.clongdouble] = np.clongdouble()
can_O_0d: _nt.CanArray0D[np.object_] = np.empty((), np.object_)
can_M_0d: _nt.CanArray0D[np.datetime64] = np.datetime64(None)
can_m_0d: _nt.CanArray0D[np.timedelta64] = np.timedelta64(None)
can_S_0d: _nt.CanArray0D[np.bytes_] = np.bytes_(b"")
can_U_0d: _nt.CanArray0D[np.str_] = np.str_("")
can_V_0d: _nt.CanArray0D[np.void] = np.void(b"")
