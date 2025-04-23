import _numtype as _nt
import numpy as np

b_0d: bool
i_0d: int
f_0d: float
c_0d: complex
S_0d: bytes
U_0d: str
O_0d: object

b_1d: list[bool]
i_1d: list[int]
f_1d: list[float]
c_1d: list[complex]
S_1d: list[bytes]
U_1d: list[str]
O_1d: list[object]

b_2d: list[list[bool]]
i_2d: list[list[int]]
f_2d: list[list[float]]
c_2d: list[list[complex]]
S_2d: list[list[bytes]]
U_2d: list[list[str]]
O_2d: list[list[object]]

b_3d: list[list[list[bool]]]
i_3d: list[list[list[int]]]
f_3d: list[list[list[float]]]
c_3d: list[list[list[complex]]]
S_3d: list[list[list[bytes]]]
U_3d: list[list[list[str]]]
O_3d: list[list[list[object]]]

###
# bool

b1: np.bool
b1_0d: _nt.Array0D[np.bool]
b1_1d: _nt.Array1D[np.bool]
b1_2d: _nt.Array2D[np.bool]
b1_3d: _nt.Array3D[np.bool]
b1_nd: _nt.Array[np.bool]

like_bool_0d: bool | np.bool | _nt.Array0D[np.bool]
like_bool_1d: list[bool | np.bool] | _nt.Array1D[np.bool]
like_bool_2d: list[list[bool | np.bool]] | list[_nt.Array1D[np.bool]] | _nt.Array2D[np.bool]
like_bool_3d: (
    list[list[list[bool | np.bool]]]
    | list[_nt.Array2D[np.bool]]
    | list[list[_nt.Array1D[np.bool]]]
    | _nt.Array3D[np.bool]
)
like_bool_nd: list[list[list[list[bool | np.bool]]]] | list[_nt.Array2D[np.bool]] | _nt.Array[np.bool]

bool_0d_accept: _nt.ToBool_0d = like_bool_0d
bool_0d_reject_sc: _nt.ToBool_0d = f_0d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_1d: _nt.ToBool_0d = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_2d: _nt.ToBool_0d = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_3d: _nt.ToBool_0d = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_nd: _nt.ToBool_0d = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_1d_accept: _nt.ToBool_1d = like_bool_1d
bool_1d_reject_sc: _nt.ToBool_1d = f_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_0d: _nt.ToBool_1d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_2d: _nt.ToBool_1ds = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_3d: _nt.ToBool_1ds = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_nd: _nt.ToBool_1ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_2d_accept: _nt.ToBool_2d = like_bool_2d
bool_2d_reject_sc: _nt.ToBool_2d = f_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_0d: _nt.ToBool_2d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_1d: _nt.ToBool_2ds = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_3d: _nt.ToBool_2ds = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_nd: _nt.ToBool_2ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_3d_accept: _nt.ToBool_3d = like_bool_3d
bool_3d_reject_sc: _nt.ToBool_3d = f_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_0d: _nt.ToBool_3d = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_1d: _nt.ToBool_3ds = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_2d: _nt.ToBool_3ds = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_nd: _nt.ToBool_3ds = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_nd_accept_0d: _nt.ToBool_nd = b1_0d
bool_nd_accept_1d: _nt.ToBool_nd = like_bool_1d
bool_nd_accept_2d: _nt.ToBool_nd = like_bool_2d
bool_nd_accept_3d: _nt.ToBool_nd = like_bool_3d
bool_nd_reject_1d_sc: _nt.ToBool_nd = f_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_2d_sc: _nt.ToBool_nd = f_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_3d_sc: _nt.ToBool_nd = f_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

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
# TODO(jorenham): repeat for all the other `_To` array-like types (codegen)
