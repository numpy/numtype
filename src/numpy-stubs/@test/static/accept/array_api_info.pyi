from typing import Literal, assert_type

import numpy as np

info = np.__array_namespace_info__()

assert_type(info.__module__, Literal["numpy"])

assert_type(info.default_device(), Literal["cpu"])
assert_type(info.devices()[0], Literal["cpu"])
assert_type(info.devices()[-1], Literal["cpu"])

assert_type(info.capabilities()["boolean indexing"], Literal[True])
assert_type(info.capabilities()["data-dependent shapes"], Literal[True])

assert_type(info.default_dtypes()["real floating"], np.dtypes.Float64DType)
assert_type(info.default_dtypes()["complex floating"], np.dtypes.Complex128DType)
assert_type(info.default_dtypes()["integral"], np.dtype[np.int_])
assert_type(info.default_dtypes()["indexing"], np.dtype[np.intp])

assert_type(info.dtypes()["bool"], np.dtypes.BoolDType)
assert_type(info.dtypes()["int8"], np.dtypes.Int8DType)
assert_type(info.dtypes()["uint8"], np.dtypes.UInt8DType)
assert_type(info.dtypes()["float32"], np.dtypes.Float32DType)
assert_type(info.dtypes()["complex64"], np.dtypes.Complex64DType)

assert_type(info.dtypes(kind="bool")["bool"], np.dtypes.BoolDType)
assert_type(info.dtypes(kind="signed integer")["int64"], np.dtypes.Int64DType)
assert_type(info.dtypes(kind="unsigned integer")["uint64"], np.dtypes.UInt64DType)
assert_type(info.dtypes(kind="integral")["int32"], np.dtypes.Int32DType)
assert_type(info.dtypes(kind="integral")["uint32"], np.dtypes.UInt32DType)
assert_type(info.dtypes(kind="real floating")["float64"], np.dtypes.Float64DType)
assert_type(info.dtypes(kind="complex floating")["complex128"], np.dtypes.Complex128DType)
assert_type(info.dtypes(kind="numeric")["int16"], np.dtypes.Int16DType)
assert_type(info.dtypes(kind="numeric")["uint16"], np.dtypes.UInt16DType)
assert_type(info.dtypes(kind="numeric")["float64"], np.dtypes.Float64DType)
assert_type(info.dtypes(kind="numeric")["complex128"], np.dtypes.Complex128DType)

assert_type(info.dtypes(kind=("bool",))["bool"], np.dtypes.BoolDType)
assert_type(info.dtypes(kind=("signed integer",))["int64"], np.dtypes.Int64DType)
assert_type(info.dtypes(kind=("integral",))["uint32"], np.dtypes.UInt32DType)
assert_type(info.dtypes(kind=("complex floating",))["complex128"], np.dtypes.Complex128DType)
assert_type(info.dtypes(kind=("numeric",))["float64"], np.dtypes.Float64DType)

assert_type(info.dtypes(kind=("signed integer", "unsigned integer"))["int8"], np.dtypes.Int8DType)
assert_type(info.dtypes(kind=("signed integer", "unsigned integer"))["uint8"], np.dtypes.UInt8DType)
assert_type(info.dtypes(kind=("integral", "real floating", "complex floating"))["int16"], np.dtypes.Int16DType)
assert_type(info.dtypes(kind=("integral", "real floating", "complex floating"))["uint16"], np.dtypes.UInt16DType)
assert_type(info.dtypes(kind=("integral", "real floating", "complex floating"))["float32"], np.dtypes.Float32DType)
assert_type(info.dtypes(kind=("integral", "real floating", "complex floating"))["complex64"], np.dtypes.Complex64DType)
