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


# --- Integer Aliases ---
_int_aliases = [
    ("byte", "int8"),
    ("short", "int16"),
    ("intc", "int32"),
    ("intp", f"int{SIZE_P}"),
    # On Windows long is int32 (LLP64), on Linux it matches pointer size (LP64).
    ("long", "int32" if WIN32 else f"int{SIZE_P}"),
]


@pytest.mark.parametrize(("name_c", "name_expect"), _int_aliases)
def test_alias_integer(name_c: str, name_expect: str) -> None:
    signed_c: type[np.signedinteger] = getattr(np, name_c)
    signed_expect: type[np.signedinteger] = getattr(np, name_expect)
    assert np.dtype(signed_c) == np.dtype(signed_expect)

    unsigned_c: type[np.unsignedinteger] = getattr(np, f"u{name_c}")
    unsigned_expect: type[np.unsignedinteger] = getattr(np, f"u{name_expect}")
    assert np.dtype(unsigned_c) == np.dtype(unsigned_expect)


# --- Floating Point Aliases ---
_longdouble_name = np.dtype(np.longdouble).name
assert _longdouble_name in {"float64", "float96", "float128"}, \
    f"Unrecognized longdouble type: {_longdouble_name}"
    
_float_aliases = [
    ("half", "float16"),
    ("single", "float32"),
    ("double", "float64"),
    ("longdouble", np.dtype(np.longdouble).name),
]


@pytest.mark.parametrize(("name_c", "name_expect"), _float_aliases)
def test_alias_floating(name_c: str, name_expect: str) -> None:
    floating_c: type[np.floating] = getattr(np, name_c)
    floating_expect: type[np.floating] = getattr(np, name_expect)
    assert np.dtype(floating_c) == np.dtype(floating_expect)
