# ruff: noqa: TD003
"""
Quick and dirty code generator for type-tests of the scalar binary operations.

Run as `uv run test/generate_scalar_binops.py` to (re)generate `.pyi` type-tests.
"""

import operator as op
from collections.abc import Generator
from pathlib import Path
from typing import Any, Final, cast

import numpy as np

OUTPUT_FILE = Path(__file__).parent / "generated/scalar_binops.pyi"

LINESEP: Final = "###"

OPS = {
    "+": op.__add__,
    "-": op.__sub__,
    "*": op.__mul__,
    "**": op.__pow__,
    "/": op.__truediv__,
    "//": op.__floordiv__,
    "%": op.__mod__,
    "<<": op.__lshift__,
    ">>": op.__rshift__,
    "&": op.__and__,
    "^": op.__xor__,
    "|": op.__or__,
    "<": op.__lt__,
    "<=": op.__le__,
    ">=": op.__ge__,
    ">": op.__gt__,
    "==": op.__eq__,
}
NAMES = {
    # builtins (key length > 1)
    "bool": "b0",
    # TODO(jorenham): Re-enable after the binops use `_numtype.Is` (avoid promotions)
    # "int": "i0",
    # "float": "f0",
    # "complex": "c0",
    #
    # bool
    "?": "b1",
    # unsigned integers
    "B": "u1",
    "H": "u2",
    "I": "u4",
    "L": "u8",
    # signed integers
    "b": "i1",
    "h": "i2",
    "i": "i4",
    "l": "i8",
    # real floating
    "e": "f2",
    "f": "f4",
    "d": "f8",
    "g": "ld",
    # complexes
    "F": "c8",
    "D": "c16",
    "G": "cld",
    "m": "m8",
    "M": "M8",
}

DATETIME_OPS = {"+", "-"}
TIMEDELTA_OPS = DATETIME_OPS | {"*", "/", "//", "%"}
BITWISE_OPS = {"<<", ">>", "&", "^", "|"}

BITWISE_CHARS = "?bhilqBHILQ"


def _scalar(key: str, /) -> np.number | np.bool | np.timedelta64 | np.datetime64 | bool:
    if len(key) > 1:
        # must be one of the builtin scalars
        pytype: type[bool] = getattr(__builtins__, key)
        return pytype(1)

    dtype = np.dtype(key)

    if dtype.char == "M":
        # datetime64(1) is not valid, so use `NaT` instead (unitless)
        return np.datetime64()

    return dtype.type(max(dtype.num, 1))  # type: ignore[no-any-return]


def _sctype_expr(dtype: np.dtype[Any]) -> str:
    if dtype.char == "q":
        return "np.longlong"
    if dtype.char == "Q":
        return "np.ulonglong"
    if dtype.char == "g":
        return "np.longdouble"
    if dtype.char == "G":
        return "np.clongdouble"

    name = dtype.name
    assert "[" not in name, "units not supported yet"
    return f"np.{name}"


def _assert_stmt(op: str, lhs: str, rhs: str, /) -> str | None:
    pad = " " * (op != "**")  # ruff doesn't like whitespace around `**` for some reason
    expr_eval = f"{NAMES[lhs]}{pad}{op}{pad}{NAMES[rhs]}"

    try:
        val_out = OPS[op](_scalar(lhs), _scalar(rhs))
    except TypeError:
        # generate rejection test, while avoiding trivial cases
        if op not in DATETIME_OPS and (lhs == "M" or rhs == "M"):
            return None
        if op not in TIMEDELTA_OPS and (lhs == "m" or rhs == "m"):
            return None
        if op in BITWISE_OPS and not (lhs in BITWISE_CHARS and rhs in BITWISE_CHARS):
            return None

        if len(lhs) > 1 or len(rhs) > 1:
            # skip rejection tests with builtins for now
            # TODO(jorenham): Re-enable this once `Is[int]` is used.
            return None

        return "  ".join((  # noqa: FLY002
            expr_eval,
            "# type: ignore[operator]",
            "# pyright: ignore[reportOperatorIssue]",
        ))

    expr_type = (
        _sctype_expr(cast("np.generic", val_out).dtype)  # type: ignore[redundant-cast]
        if isinstance(val_out, np.generic)
        else type(val_out).__qualname__
    )
    return f"assert_type({expr_eval}, {expr_type})" if expr_type != "bool" else None


def _gen_imports() -> Generator[str]:
    # the blank lines are required for ruff compatibility
    yield "from typing_extensions import assert_type"
    yield ""
    yield "import numpy as np"
    yield ""


def _gen_names() -> Generator[str]:
    yield LINESEP
    yield "# scalars"
    yield ""

    # builtin scalars
    for builtin, name in NAMES.items():
        if len(builtin) > 1:
            yield f"{name}: {builtin}"

    # numpy scalars
    for char, name in NAMES.items():
        if len(char) == 1:
            yield f"{name}: {_sctype_expr(np.dtype(char))}"
    yield ""


def _gen_asserts(op: str, /) -> Generator[str]:
    opname = OPS[op].__name__.removesuffix("_")
    yield LINESEP
    yield f"# __[r]{opname}__"
    yield ""

    for lhs in NAMES:
        # skip builtins on the left-hand side, to avoid a pyright bug "as designed"
        if len(lhs) > 1:
            continue

        n = 0
        for rhs in NAMES:
            if stmt := _assert_stmt(op, lhs, rhs):
                yield stmt
                n += 1
        if n:
            yield ""


def _gen_all() -> Generator[str]:
    yield f"# @generated {np.datetime64('now')}Z"
    yield from _gen_imports()
    yield from _gen_names()

    for symbol in OPS:
        yield from _gen_asserts(symbol)


@np.errstate(all="ignore")
def main() -> None:
    """Regenerate the `test/generated/{}.pyi` type-tests."""
    OUTPUT_FILE.write_text("\n".join(_gen_all()), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
