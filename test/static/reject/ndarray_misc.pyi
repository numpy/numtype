import numpy as np
import numpy.typing as npt

f8: np.float64
AR_f8: npt.NDArray[np.float64]
AR_M: npt.NDArray[np.datetime64]
AR_b: npt.NDArray[np.bool]

ctypes_obj = AR_f8.ctypes

###

ctypes_obj.get_data()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
ctypes_obj.get_shape()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
ctypes_obj.get_strides()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
ctypes_obj.get_as_parameter()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

f8.argpartition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.diagonal()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.dot(1)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.nonzero()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.partition(0)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.put(0, 2)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.setfield(2, np.float64)  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.sort()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
f8.trace()  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

int(AR_M)  # pyright: ignore[reportArgumentType]
float(AR_M)  # pyright: ignore[reportArgumentType]
complex(AR_M)  # pyright: ignore[reportCallIssue,reportArgumentType]
AR_b.__index__()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue]

AR_f8[1.5]  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
AR_f8["field_a"]  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue,reportArgumentType]
AR_f8[["field_a", "field_b"]]  # type: ignore[index]  # pyright: ignore[reportCallIssue,reportArgumentType]

AR_f8.__array_finalize__(object())  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
