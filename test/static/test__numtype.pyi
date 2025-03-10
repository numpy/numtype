# ruff: noqa: PYI042, UP018
from typing import TypeAlias
from typing_extensions import TypeVar

import _numtype as _nt
import numpy as np

_SCT = TypeVar("_SCT", bound=np.generic)
_0D: TypeAlias = np.ndarray[tuple[()], np.dtype[_SCT]]
_1D: TypeAlias = np.ndarray[tuple[int], np.dtype[_SCT]]
_2D: TypeAlias = np.ndarray[tuple[int, int], np.dtype[_SCT]]
_3D: TypeAlias = np.ndarray[tuple[int, int, int], np.dtype[_SCT]]
_ND: TypeAlias = np.ndarray[tuple[int, ...], np.dtype[_SCT]]

b_: bool
i_: int
f_: float
c_: complex
S_: bytes
U_: str
O_: object

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

###
# bool

b1: np.bool
b1_0d: _0D[np.bool]
b1_1d: _1D[np.bool]
b1_2d: _2D[np.bool]
b1_3d: _3D[np.bool]
b1_nd: _ND[np.bool]

like_bool_0d: bool | np.bool | _0D[np.bool]
like_bool_1d: list[bool | np.bool] | _1D[np.bool]
like_bool_2d: list[list[bool | np.bool]] | list[_1D[np.bool]] | _2D[np.bool]
like_bool_3d: list[list[list[bool | np.bool]]] | list[_2D[np.bool]] | list[list[_1D[np.bool]]] | _3D[np.bool]
like_bool_nd: list[list[list[list[bool | np.bool]]]] | list[_2D[np.bool]] | _ND[np.bool]

bool_0d_accept: _nt.ToBool_0d = like_bool_0d
bool_0d_reject_sc: _nt.ToBool_0d = f_  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_1d: _nt.ToBool_0d = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_2d: _nt.ToBool_0d = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_3d: _nt.ToBool_0d = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_nd: _nt.ToBool_0d = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_1d_accept: _nt.ToBool_1d = like_bool_1d
bool_1d_reject_sc: _nt.ToBool_1d = [f_]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_0d: _nt.ToBool_1d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_2d: _nt.ToBool_1ds = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_3d: _nt.ToBool_1ds = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_nd: _nt.ToBool_1ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_2d_accept: _nt.ToBool_2d = like_bool_2d
bool_2d_reject_sc: _nt.ToBool_2d = [[f_]]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_0d: _nt.ToBool_2d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_1d: _nt.ToBool_2ds = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_3d: _nt.ToBool_2ds = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_nd: _nt.ToBool_2ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_3d_accept: _nt.ToBool_3d = like_bool_3d
bool_3d_reject_sc: _nt.ToBool_3d = [[[f_]]]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_0d: _nt.ToBool_3d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_1d: _nt.ToBool_3ds = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_2d: _nt.ToBool_3ds = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_nd: _nt.ToBool_3ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_nd_accept_0d: _nt.ToBool_nd = b1_0d
bool_nd_accept_1d: _nt.ToBool_nd = like_bool_1d
bool_nd_accept_2d: _nt.ToBool_nd = like_bool_2d
bool_nd_accept_3d: _nt.ToBool_nd = like_bool_3d
bool_nd_reject_1d_sc: _nt.ToBool_nd = [f_]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_2d_sc: _nt.ToBool_nd = [[f_]]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_3d_sc: _nt.ToBool_nd = [[[f_]]]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_1nd_reject_0d: _nt.ToBool_1nd = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1nd_accept_1d: _nt.ToBool_1nd = b1_1d
bool_1nd_accept_2d: _nt.ToBool_1nd = b1_2d
bool_1nd_accept_3d: _nt.ToBool_1nd = b1_3d

bool_2nd_reject_0d: _nt.ToBool_2nd = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2nd_reject_1d: _nt.ToBool_2nd = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2nd_accept_2d: _nt.ToBool_2nd = b1_2d
bool_2nd_accept_3d: _nt.ToBool_2nd = b1_3d

bool_3nd_reject_0d: _nt.ToBool_3nd = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3nd_reject_1d: _nt.ToBool_3nd = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3nd_reject_2d: _nt.ToBool_3nd = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3nd_accept_3d: _nt.ToBool_3nd = b1_3d

###
# TODO(jorenham): repeat for all the other `_To` and `_Co` types (codegen)
