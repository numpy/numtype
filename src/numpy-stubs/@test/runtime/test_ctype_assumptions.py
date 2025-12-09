# ruff: noqa: S101, PLR2004

import ctypes as ct
import sys

import pytest

import numpy as np

WIN32 = sys.platform == "win32"
SIZE_P = ct.sizeof(ct.c_ssize_t) * 8


def test_maxsize_32_or_64() -> None:
    # assume we're either on a 32 or a 64 bit system
    assert SIZE_P in {32, 64}
    assert sys.maxsize == (1 << (SIZE_P - 1)) - 1


@pytest.mark.parametrize("char", ["q", "Q"])
def test_longlong_64(char: str) -> None:
    assert np.dtype(char).itemsize == 8
    assert np.dtype(char).alignment == 8


@pytest.mark.parametrize(
    ("name_c", "name_expect"),
    [
        ("byte", "int8"),
        ("short", "int16"),
        ("intc", "int32"),
        ("intp", f"int{SIZE_P}"),
        ("long", "int32" if WIN32 else f"int{SIZE_P}"),
    ],
)
def test_alias_integer(name_c: str, name_expect: str) -> None:
    signed_c: type[np.signedinteger] = getattr(np, name_c)
    signed_expect: type[np.signedinteger] = getattr(np, name_expect)
    assert signed_c is signed_expect

    unsigned_c: type[np.unsignedinteger] = getattr(np, f"u{name_c}")
    unsigned_expect: type[np.unsignedinteger] = getattr(np, f"u{name_expect}")
    assert unsigned_c is unsigned_expect


@pytest.mark.parametrize(
    ("name_c", "name_expect"),
    [("half", "float16"), ("single", "float32"), ("double", "float64")],
)
def test_alias_floating_standard(name_c: str, name_expect: str) -> None:
    floating_c: type[np.floating] = getattr(np, name_c)
    floating_expect: type[np.floating] = getattr(np, name_expect)
    assert floating_c is floating_expect


def test_alias_longdouble() -> None:
    ld_name = np.dtype(np.longdouble).name

    if WIN32:
        assert ld_name in {"float64", "float96"}
    else:
        assert ld_name == "float128"

    assert np.longdouble is getattr(np, ld_name)
