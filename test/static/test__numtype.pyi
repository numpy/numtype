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

bool_0d_accept: _nt.As0D_bool = like_bool_0d
bool_0d_reject_sc: _nt.As0D_bool = f_  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_1d: _nt.As0D_bool = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_2d: _nt.As0D_bool = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_3d: _nt.As0D_bool = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_0d_reject_nd: _nt.As0D_bool = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_1d_accept: _nt.As1D_bool = like_bool_1d
bool_1d_reject_sc: _nt.As1D_bool = [f_]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_0d: _nt.As1D_bool = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_2d: _nt.As1D_bool = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_3d: _nt.As1D_bool = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_1d_reject_nd: _nt.As1D_bool = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_2d_accept: _nt.As2D_bool = like_bool_2d
bool_2d_reject_sc: _nt.As2D_bool = [[f_]]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_0d: _nt.As2D_bool = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_1d: _nt.As2D_bool = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_3d: _nt.As2D_bool = b1_3d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_2d_reject_nd: _nt.As2D_bool = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_3d_accept: _nt.As3D_bool = like_bool_3d
bool_3d_reject_sc: _nt.As3D_bool = [[[f_]]]  # type: ignore[list-item]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_0d: _nt.As3D_bool = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_1d: _nt.As3D_bool = b1_1d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_2d: _nt.As3D_bool = b1_2d  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_3d_reject_nd: _nt.As3D_bool = b1_nd  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

bool_nd_accept_0d: _nt.AsND_bool = b1_0d
bool_nd_accept_1d: _nt.AsND_bool = like_bool_1d
bool_nd_accept_2d: _nt.AsND_bool = like_bool_2d
bool_nd_accept_3d: _nt.AsND_bool = like_bool_3d
bool_nd_reject_0d: _nt.AsND_bool = b1  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_1d_sc: _nt.AsND_bool = [f_]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_2d_sc: _nt.AsND_bool = [[f_]]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]
bool_nd_reject_3d_sc: _nt.AsND_bool = [[[f_]]]  # type: ignore[assignment]  # pyright: ignore[reportAssignmentType]

# TODO: repeat for all the other `_As` types
# TODO: repeat for the `_To` types
# TODO: realize that I'm not a factory worker => codegen it (parametrized pytests)
