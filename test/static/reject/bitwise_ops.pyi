from typing import Final

import numpy as np

i0: Final[int] = ...

b1: Final[np.bool] = ...
i4: Final[np.int32] = ...
i8: Final[np.int64] = ...
u8: Final[np.uint64] = ...
f8: Final[np.float64] = ...

###

# TODO: Certain mixes like i4 << u8 go to float and thus should fail

~f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

b1 >> f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 >> b1  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

i8 << f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
f8 << i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f8 | i0  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i0 | f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f8 ^ i8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]
i8 ^ f8  # type: ignore[operator]  # pyright: ignore[reportOperatorIssue]

f8 & u8  # type: ignore[call-overload]  # pyright: ignore[reportOperatorIssue]
u8 & f8  # type: ignore[call-overload]  # pyright: ignore[reportOperatorIssue]
