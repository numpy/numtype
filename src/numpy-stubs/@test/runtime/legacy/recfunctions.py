"""These tests are based on the doctests from `numpy/lib/recfunctions.py`."""

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, assert_type

import numpy as np
from numpy.lib import recfunctions as rfn

if TYPE_CHECKING:
    import _numtype as _nt

# ruff: noqa: S101


def _test(fn: Callable[[], None]) -> None:
    fn()


@_test
def test_recursive_fill_fields() -> None:
    a: _nt.Array[np.void] = np.array(
        [(1, 10.0), (2, 20.0)], dtype=[("A", np.int64), ("B", np.float64)]
    )
    b = np.zeros((3,), dtype=a.dtype)
    out = rfn.recursive_fill_fields(a, b)
    assert_type(out, "_nt.Array1D[np.void]")


@_test
def test_get_names() -> None:
    names: tuple[str | Any, ...]
    names = rfn.get_names(np.empty((1,), dtype=[("A", int)]).dtype)
    names = rfn.get_names(np.empty((1,), dtype=[("A", int), ("B", float)]).dtype)

    adtype = np.dtype([("a", int), ("b", [("b_a", int), ("b_b", int)])])
    names = rfn.get_names(adtype)
    assert names


@_test
def test_get_names_flat() -> None:
    names: tuple[str, ...]
    names = rfn.get_names_flat(np.empty((1,), dtype=[("A", int)]).dtype)
    names = rfn.get_names_flat(np.empty((1,), dtype=[("A", int), ("B", float)]).dtype)

    adtype = np.dtype([("a", int), ("b", [("b_a", int), ("b_b", int)])])
    names = rfn.get_names_flat(adtype)
    assert names


@_test
def test_flatten_descr() -> None:
    ndtype = np.dtype([("a", "<i4"), ("b", [("b_a", "<f8"), ("b_b", "<i4")])])
    assert_type(rfn.flatten_descr(ndtype), tuple[tuple[str, np.dtype]])


@_test
def test_get_fieldstructure() -> None:
    ndtype = np.dtype([
        ("A", int),
        ("B", [("B_A", int), ("B_B", [("B_B_A", int), ("B_B_B", int)])]),
    ])
    assert_type(rfn.get_fieldstructure(ndtype), dict[str, list[str]])


@_test
def test_merge_arrays() -> None:
    assert_type(
        rfn.merge_arrays((np.ones(((2),), np.int_), np.ones(((3),), np.float64))),
        "np.recarray[_nt.Rank1, np.dtype[np.void]]",
    )


@_test
def test_drop_fields() -> None:
    ndtype = [("a", np.int64), ("b", [("b_a", np.double), ("b_b", np.int64)])]
    a = np.ones(((3),), dtype=ndtype)

    assert_type(rfn.drop_fields(a, "a"), "_nt.Array1D[np.void]")
    assert_type(
        rfn.drop_fields(a, "a", asrecarray=True),
        "np.rec.recarray[_nt.Rank1, np.dtype[np.void]]",
    )
    assert_type(
        rfn.rec_drop_fields(a, "a"), "np.rec.recarray[_nt.Rank1, np.dtype[np.void]]"
    )


@_test
def test_rename_fields() -> None:
    ndtype = [("a", np.int64), ("b", [("b_a", np.double), ("b_b", np.int64)])]
    a = np.ones(((3),), dtype=ndtype)

    assert_type(rfn.rename_fields(a, {"a": "A", "b_b": "B_B"}), "_nt.Array1D[np.void]")


@_test
def test_repack_fields() -> None:
    dt: np.dtype[np.void] = np.dtype("u1, <i8, <f8", align=True)

    assert_type(rfn.repack_fields(dt), np.dtype[np.void])
    assert_type(rfn.repack_fields(dt.type(0)), np.void)
    assert_type(rfn.repack_fields(np.ones((3,), dtype=dt)), "_nt.Array1D[np.void]")


@_test
def test_structured_to_unstructured() -> None:
    a = np.zeros(4, dtype=[("a", "i4"), ("b", "f4,u2"), ("c", "f4", 2)])
    assert_type(rfn.structured_to_unstructured(a), "_nt.Array")


@_test
def unstructured_to_structured() -> None:
    dt: np.dtype[np.void] = np.dtype([("a", "i4"), ("b", "f4,u2"), ("c", "f4", 2)])
    a = np.arange(20, dtype=np.int32).reshape((4, 5))
    assert_type(rfn.unstructured_to_structured(a, dt), "_nt.Array[np.void]")


@_test
def test_apply_along_fields() -> None:
    b = np.ones(4, dtype=[("x", "i4"), ("y", "f4"), ("z", "f8")])
    assert_type(rfn.apply_along_fields(np.mean, b), "_nt.Array1D[np.void]")


@_test
def test_assign_fields_by_name() -> None:
    b = np.ones(4, dtype=[("x", "i4"), ("y", "f4"), ("z", "f8")])
    assert_type(rfn.apply_along_fields(np.mean, b), "_nt.Array1D[np.void]")


@_test
def test_require_fields() -> None:
    a = np.ones(4, dtype=[("a", "i4"), ("b", "f8"), ("c", "u1")])
    assert_type(
        rfn.require_fields(a, [("b", "f4"), ("c", "u1")]), "_nt.Array1D[np.void]"
    )


@_test
def test_stack_arrays() -> None:
    x = np.zeros(((2),), np.int32)
    assert_type(rfn.stack_arrays(x), "_nt.Array1D[np.int32]")

    z = np.ones(((2),), [("A", "|S3"), ("B", float)])
    zz = np.ones(((2),), [("A", "|S3"), ("B", np.float64), ("C", np.float64)])
    assert_type(rfn.stack_arrays((z, zz)), "_nt.MArray[np.void]")


@_test
def test_find_duplicates() -> None:
    ndtype = np.dtype([("a", int)])

    a = np.ma.ones(7).view(ndtype)
    assert_type(rfn.find_duplicates(a), "_nt.MArray[np.void, _nt.Rank1]")
    assert_type(
        rfn.find_duplicates(a, ignoremask=True, return_index=True),
        "tuple[_nt.MArray[np.void, _nt.Rank1], _nt.Array[np.intp, _nt.Rank1]]",
    )
