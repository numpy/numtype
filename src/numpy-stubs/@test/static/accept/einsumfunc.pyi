from typing import Any, assert_type

import _numtype as _nt
import numpy as np

AR_LIKE_b: list[bool]
AR_LIKE_u: list[np.uint32]
AR_LIKE_i: list[int]
AR_LIKE_f: list[float]
AR_LIKE_c: list[complex]
AR_LIKE_U: list[str]
AR_o: _nt.Array[np.object_]

OUT_f: _nt.Array[np.float64]

assert_type(np.einsum("i,i->i", AR_LIKE_b, AR_LIKE_b), Any)
assert_type(np.einsum("i,i->i", AR_o, AR_o), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_u, AR_LIKE_u), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_i, AR_LIKE_i), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_f, AR_LIKE_f), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_c, AR_LIKE_c), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_b, AR_LIKE_i), Any)
assert_type(np.einsum("i,i,i,i->i", AR_LIKE_b, AR_LIKE_u, AR_LIKE_i, AR_LIKE_c), Any)

assert_type(np.einsum("i,i->i", AR_LIKE_c, AR_LIKE_c, out=OUT_f), _nt.Array[np.float64])
assert_type(np.einsum("i,i->i", AR_LIKE_U, AR_LIKE_U, dtype=bool, casting="unsafe", out=OUT_f), _nt.Array[np.float64])
assert_type(np.einsum("i,i->i", AR_LIKE_f, AR_LIKE_f, dtype="c16"), Any)
assert_type(np.einsum("i,i->i", AR_LIKE_U, AR_LIKE_U, dtype=bool, casting="unsafe"), Any)

assert_type(np.einsum_path("i,i->i", AR_LIKE_b, AR_LIKE_b), tuple[list[str | tuple[int, ...]], str])
assert_type(np.einsum_path("i,i->i", AR_LIKE_u, AR_LIKE_u), tuple[list[str | tuple[int, ...]], str])
assert_type(np.einsum_path("i,i->i", AR_LIKE_i, AR_LIKE_i), tuple[list[str | tuple[int, ...]], str])
assert_type(np.einsum_path("i,i->i", AR_LIKE_f, AR_LIKE_f), tuple[list[str | tuple[int, ...]], str])
assert_type(np.einsum_path("i,i->i", AR_LIKE_c, AR_LIKE_c), tuple[list[str | tuple[int, ...]], str])
assert_type(np.einsum_path("i,i->i", AR_LIKE_b, AR_LIKE_i), tuple[list[str | tuple[int, ...]], str])
assert_type(
    np.einsum_path("i,i,i,i->i", AR_LIKE_b, AR_LIKE_u, AR_LIKE_i, AR_LIKE_c),
    tuple[list[str | tuple[int, ...]], str],
)

assert_type(np.einsum([[1, 1], [1, 1]], AR_LIKE_i, AR_LIKE_i), Any)
assert_type(np.einsum_path([[1, 1], [1, 1]], AR_LIKE_i, AR_LIKE_i), tuple[list[str | tuple[int, ...]], str])
