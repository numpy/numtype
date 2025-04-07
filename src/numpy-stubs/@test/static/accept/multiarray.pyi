import datetime as dt
from typing import Any
from typing_extensions import TypeVar, assert_type

import numpy as np
import numpy.typing as npt

###

_ScalarT_co = TypeVar("_ScalarT_co", bound=np.generic, covariant=True)

class SubClass(npt.NDArray[_ScalarT_co]): ...

subclass: SubClass[np.float64]

AR_f8: npt.NDArray[np.float64]
AR_i8: npt.NDArray[np.int64]
AR_u1: npt.NDArray[np.uint8]
AR_m: npt.NDArray[np.timedelta64]
AR_M: npt.NDArray[np.datetime64]

AR_LIKE_f: list[float]
AR_LIKE_i: list[int]

m: np.timedelta64
M: np.datetime64

b_f8 = np.broadcast(AR_f8)
b_i8_f8_f8 = np.broadcast(AR_i8, AR_f8, AR_f8)

nditer_obj: np.nditer

date_scalar: dt.date
date_seq: list[dt.date]
timedelta_seq: list[dt.timedelta]

f8: np.float64

def func11(a: int) -> bool: ...
def func21(a: int, b: int) -> int: ...
def func12(a: int) -> tuple[complex, str]: ...

###

assert_type(next(b_f8), tuple[Any, ...])
assert_type(b_f8.reset(), None)
assert_type(b_f8.index, int)
assert_type(b_f8.iters, tuple[np.flatiter[Any], ...])
assert_type(b_f8.nd, int)
assert_type(b_f8.ndim, int)
assert_type(b_f8.numiter, int)
assert_type(b_f8.shape, tuple[int, ...])
assert_type(b_f8.size, int)

assert_type(next(b_i8_f8_f8), tuple[Any, ...])
assert_type(b_i8_f8_f8.reset(), None)
assert_type(b_i8_f8_f8.index, int)
assert_type(b_i8_f8_f8.iters, tuple[np.flatiter[Any], ...])
assert_type(b_i8_f8_f8.nd, int)
assert_type(b_i8_f8_f8.ndim, int)
assert_type(b_i8_f8_f8.numiter, int)
assert_type(b_i8_f8_f8.shape, tuple[int, ...])
assert_type(b_i8_f8_f8.size, int)

assert_type(np.inner(AR_f8, AR_i8), Any)

assert_type(np.where([True, True, False], 1, 0), npt.NDArray[Any])
assert_type(np.where([True, True, False]), tuple[npt.NDArray[np.intp], ...])

assert_type(np.lexsort([0, 1, 2]), np.int_)

assert_type(np.can_cast(np.dtype("i8"), int), bool)
assert_type(np.can_cast(AR_f8, "f8"), bool)
assert_type(np.can_cast(AR_f8, np.complex128, casting="unsafe"), bool)

assert_type(np.min_scalar_type([1]), np.dtype)
assert_type(np.min_scalar_type(AR_f8), np.dtype)

assert_type(np.result_type(int, [1]), np.dtype)
assert_type(np.result_type(AR_f8, AR_u1), np.dtype)
assert_type(np.result_type(AR_f8, np.complex128), np.dtype)

assert_type(np.dot(AR_LIKE_f, AR_i8), Any)
assert_type(np.dot(AR_u1, 1), Any)
assert_type(np.dot(1.5j, 1), Any)
assert_type(np.dot(AR_u1, 1, out=AR_f8), npt.NDArray[np.float64])

assert_type(np.vdot(AR_u1, 1), np.signedinteger)
assert_type(np.vdot(AR_LIKE_f, AR_i8), np.floating | np.signedinteger)
assert_type(np.vdot(1.5j, 1), np.inexact | np.signedinteger)

assert_type(np.bincount(AR_i8), npt.NDArray[np.intp])

assert_type(np.copyto(AR_f8, [1.0, 1.5, 1.6]), None)

assert_type(np.putmask(AR_f8, [True, True, False], 1.5), None)

assert_type(np.packbits(AR_i8), npt.NDArray[np.uint8])
assert_type(np.packbits(AR_u1), npt.NDArray[np.uint8])

assert_type(np.unpackbits(AR_u1), npt.NDArray[np.uint8])

assert_type(np.shares_memory(1, 2), bool)
assert_type(np.shares_memory(AR_f8, AR_f8, max_work=1), bool)

assert_type(np.may_share_memory(1, 2), bool)
assert_type(np.may_share_memory(AR_f8, AR_f8, max_work=1), bool)

assert_type(np.promote_types(np.int32, np.int64), np.dtype)
assert_type(np.promote_types("f4", float), np.dtype)

assert_type(np.frompyfunc(func11, 1, 1).nin, int)
assert_type(np.frompyfunc(func11, 1, 1).nout, int)
assert_type(np.frompyfunc(func11, 1, 1).nargs, int)
assert_type(np.frompyfunc(func11, 1, 1).ntypes, int)
assert_type(np.frompyfunc(func11, 1, 1).identity, Any | None)
assert_type(np.frompyfunc(func11, 1, 1).signature, str | None)
assert_type(np.frompyfunc(func11, 1, 1)(f8), bool)
assert_type(np.frompyfunc(func11, 1, 1).at(AR_f8, AR_i8), None)
assert_type(np.frompyfunc(func11, 1, 1)(AR_f8), bool | npt.NDArray[np.object_])

assert_type(np.frompyfunc(func21, 2, 1).nin, int)
assert_type(np.frompyfunc(func21, 2, 1).nout, int)
assert_type(np.frompyfunc(func21, 2, 1).nargs, int)
assert_type(np.frompyfunc(func21, 2, 1).ntypes, int)
assert_type(np.frompyfunc(func21, 2, 1).identity, Any | None)
assert_type(np.frompyfunc(func21, 2, 1).signature, str | None)
assert_type(np.frompyfunc(func21, 2, 1)(f8, f8), int)
assert_type(np.frompyfunc(func21, 2, 1)(AR_f8, f8), int | npt.NDArray[np.object_])
assert_type(np.frompyfunc(func21, 2, 1)(f8, AR_f8), int | npt.NDArray[np.object_])
assert_type(np.frompyfunc(func21, 2, 1).reduce(AR_f8, axis=0), Any)
assert_type(np.frompyfunc(func21, 2, 1).accumulate(AR_f8), npt.NDArray[Any])
assert_type(np.frompyfunc(func21, 2, 1).reduceat(AR_f8, AR_i8), npt.NDArray[Any])
assert_type(np.frompyfunc(func21, 2, 1).outer(AR_f8, f8), npt.NDArray[Any])

assert_type(np.frompyfunc(func21, 2, 1, identity=0).nin, int)
assert_type(np.frompyfunc(func21, 2, 1, identity=0).nout, int)
assert_type(np.frompyfunc(func21, 2, 1, identity=0).nargs, int)
assert_type(np.frompyfunc(func21, 2, 1, identity=0).ntypes, int)
assert_type(np.frompyfunc(func21, 2, 1, identity=0).identity, Any | None)
assert_type(np.frompyfunc(func21, 2, 1, identity=0).signature, str | None)

assert_type(np.frompyfunc(func12, 1, 2).nin, int)
assert_type(np.frompyfunc(func12, 1, 2).nout, int)
assert_type(np.frompyfunc(func12, 1, 2).nargs, int)
assert_type(np.frompyfunc(func12, 1, 2).ntypes, int)
assert_type(np.frompyfunc(func12, 1, 2).identity, Any | None)
assert_type(np.frompyfunc(func12, 1, 2).signature, str | None)
assert_type(np.frompyfunc(func12, 1, 2)(f8, f8), tuple[complex, str])
assert_type(np.frompyfunc(func12, 1, 2)(AR_f8, f8), tuple[complex | npt.NDArray[np.object_], str | npt.NDArray[np.object_]])

assert_type(np.datetime_data("m8[D]"), tuple[str, int])
assert_type(np.datetime_data(np.datetime64), tuple[str, int])
assert_type(np.datetime_data(np.dtype(np.timedelta64)), tuple[str, int])

assert_type(np.busday_count("2011-01", "2011-02"), np.int_)
assert_type(np.busday_count(["2011-01"], "2011-02"), npt.NDArray[np.int_])
assert_type(np.busday_count(["2011-01"], date_scalar), npt.NDArray[np.int_])

assert_type(np.busday_offset(date_scalar, m), np.datetime64[dt.datetime])
assert_type(np.busday_offset(M, m), np.datetime64[dt.datetime])
assert_type(np.busday_offset(M, 5), np.datetime64[dt.datetime])
assert_type(np.busday_offset(AR_M, m), npt.NDArray[np.datetime64[dt.datetime]])
assert_type(np.busday_offset(M, timedelta_seq), npt.NDArray[np.datetime64[dt.datetime]])
assert_type(np.busday_offset("2011-01", 1, roll="forward"), np.datetime64[dt.datetime])
assert_type(np.busday_offset(["2011-01"], 1, roll="forward"), npt.NDArray[np.datetime64[dt.datetime]])
assert_type(np.busday_offset(["2011-01"], [1], roll="forward"), npt.NDArray[np.datetime64[dt.datetime]])

assert_type(np.is_busday("2012"), np.bool)
assert_type(np.is_busday(date_scalar), np.bool)
assert_type(np.is_busday(["2012"]), npt.NDArray[np.bool])

assert_type(np.datetime_as_string(M), np.str_)
assert_type(np.datetime_as_string(AR_M), npt.NDArray[np.str_])

assert_type(np.busdaycalendar(holidays=date_seq), np.busdaycalendar)
assert_type(np.busdaycalendar(holidays=[M]), np.busdaycalendar)

assert_type(np.char.compare_chararrays("a", "b", "!=", rstrip=False), npt.NDArray[np.bool])
assert_type(np.char.compare_chararrays(b"a", b"a", "==", True), npt.NDArray[np.bool])

assert_type(np.nested_iters([AR_i8, AR_i8], [[0], [1]], flags=["c_index"]), tuple[np.nditer, ...])
assert_type(np.nested_iters([AR_i8, AR_i8], [[0], [1]], op_flags=[["readonly", "readonly"]]), tuple[np.nditer, ...])
assert_type(np.nested_iters([AR_i8, AR_i8], [[0], [1]], op_dtypes=np.int_), tuple[np.nditer, ...])
assert_type(np.nested_iters([AR_i8, AR_i8], [[0], [1]], order="C", casting="no"), tuple[np.nditer, ...])
