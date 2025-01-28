from numpy.lib import NumpyVersion

version: NumpyVersion

version >= b"1.8.0"  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
NumpyVersion(b"1.8.0")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
