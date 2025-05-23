import _numtype as _nt
import numpy as np

AR_U: _nt.Array[np.str_]

def func(x: object) -> bool: ...

np.testing.assert_(True, msg=1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]  # noqa: PT009
np.testing.build_err_msg(1, "test")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.testing.assert_almost_equal(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.testing.assert_approx_equal([1, 2, 3], [1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.testing.assert_array_almost_equal(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.testing.assert_array_less(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.testing.assert_string_equal(b"a", b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.testing.assert_raises(expected_exception=TypeError, callable=func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.testing.assert_raises_regex(expected_exception=TypeError, expected_regex="T", callable=func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.testing.assert_allclose(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType, reportCallIssue]
np.testing.assert_array_almost_equal_nulp(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.testing.assert_array_max_ulp(AR_U, AR_U)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.testing.assert_warns(RuntimeWarning, func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.testing.assert_no_warnings(func=func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.testing.assert_no_warnings(func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
np.testing.assert_no_warnings(func, y=None)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]

np.testing.assert_no_gc_cycles(func=func)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue]
