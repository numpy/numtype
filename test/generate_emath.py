"""
Quick and dirty code generator for static `numpy.emath` acceptance tests.

When with `uv run test/generate_emath.py`, this will create or overwrite the
`test/generated/emath.pyi` static type-tests.
"""

import itertools
from collections.abc import Callable, Generator
from pathlib import Path
from typing import Any, Final

import numpy as np

OUTPUT_FILE = Path(__file__).parent / "generated/emath.pyi"

LINESEP: Final = "\n###\n"

# TODO(jorenham): object_  # noqa: TD003
VALS_EMATH: Final[dict[str, list[Any]]] = {
    # "np.bool": [np.True_],  # same as int8
    "np.uint8": [np.uint8(0), np.uint8(1), np.uint8(9)],
    "np.uint16": [np.uint16(0), np.uint16(1), np.uint16(9)],
    "np.uint32": [np.uint32(0), np.uint32(1), np.uint32(9)],
    "np.uint64": [np.uint64(0), np.uint64(1), np.uint64(9)],
    "np.int8": [np.int8(0), np.int8(1), np.int8(9), np.int8(-9), np.int8(-1)],
    "np.int16": [np.int16(0), np.int16(1), np.int16(9), np.int16(-9), np.int16(-1)],
    "np.int32": [np.int32(0), np.int32(1), np.int32(9), np.int32(-9), np.int32(-1)],
    "np.int64": [np.int64(0), np.int64(1), np.int64(9), np.int64(-9), np.int64(-1)],
    "np.float16": [
        np.float16(0),
        np.float16(1),
        np.float16(9),
        np.float16(-9),
        np.float16(-1),
    ],
    "np.float32": [
        np.float32(0),
        np.float32(1),
        np.float32(9),
        np.float32(-9),
        np.float32(-1),
    ],
    "np.float64": [
        np.float64(0),
        np.float64(1),
        np.float64(9),
        np.float64(-9),
        np.float64(-1),
    ],
    "np.longdouble": [
        np.longdouble(0),
        np.longdouble(1),
        np.longdouble(9),
        np.longdouble(-9),
        np.longdouble(-1),
    ],
    "np.complex64": [
        np.complex64(0),
        np.complex64(1),
        np.complex64(9),
        np.complex64(1j),
        np.complex64(9j),
        np.complex64(1 + 1j),
        np.complex64(9 + 9j),
        np.complex64(-9 - 9j),
        np.complex64(-1 - 1j),
        np.complex64(-9j),
        np.complex64(-1j),
        np.complex64(-9),
        np.complex64(-1),
    ],
    "np.complex128": [
        np.complex128(0),
        np.complex128(1),
        np.complex128(9),
        np.complex128(1j),
        np.complex128(9j),
        np.complex128(1 + 1j),
        np.complex128(9 + 9j),
        np.complex128(-9 - 9j),
        np.complex128(-1 - 1j),
        np.complex128(-9j),
        np.complex128(-1j),
        np.complex128(-9),
        np.complex128(-1),
    ],
    "np.clongdouble": [
        np.clongdouble(0),
        np.clongdouble(1),
        np.clongdouble(9),
        np.clongdouble(1j),
        np.clongdouble(9j),
        np.clongdouble(1 + 1j),
        np.clongdouble(9 + 9j),
        np.clongdouble(-9 - 9j),
        np.clongdouble(-1 - 1j),
        np.clongdouble(-9j),
        np.clongdouble(-1j),
        np.clongdouble(-9),
        np.clongdouble(-1),
    ],
}
TYPES_I: Final = frozenset({"np.int8", "np.int16", "np.int32", "np.int64"})
TYPES_U: Final = frozenset({"np.uint8", "np.uint16", "np.uint32", "np.uint64"})
TYPES_F: Final = frozenset({"np.float32", "np.float64", "np.longdouble"})
TYPES_C: Final = frozenset({"np.complex64", "np.complex128", "np.clongdouble"})
TYPES_IU: Final = TYPES_I | TYPES_U
TYPES_FC: Final = TYPES_F | TYPES_C
TYPES_IUFC: Final = TYPES_IU | TYPES_FC


def _union(*types: str) -> str:
    ints = set()
    uints = set()
    floats = set()
    cfloats = set()
    others = set()

    for tp in types:
        kind = np.dtype(tp.removeprefix("np.")).kind
        if kind == "i":
            ints.add(tp)
        elif kind == "u":
            uints.add(tp)
        elif kind == "f":
            floats.add(tp)
        elif kind == "c":
            cfloats.add(tp)
        else:
            others.add(tp)

    if ints >= TYPES_I:
        ints = {"signedinteger"}
    if uints >= TYPES_U:
        uints = {"unsignedinteger"}
    if floats >= TYPES_F:
        floats = {"floating"}
    if cfloats >= TYPES_C:
        cfloats = {"complexfloating"}

    return " | ".join((*others, *ints, *uints, *floats, *cfloats))


def _gen_names() -> Generator[str, None, dict[str, str]]:
    yield f"# @generated {np.datetime64('now')}"
    yield "from typing_extensions import assert_type"
    yield ""
    yield "import numpy as np"
    yield ""

    names: dict[str, str] = {}
    for sct in VALS_EMATH:
        if sct.startswith("np."):
            if sct.endswith("intp"):
                char = "N" if sct[3] == "u" else "n"
            elif sct.endswith("longlong"):
                char = "Q" if sct[3] == "u" else "q"
            elif sct.endswith("long"):
                char = "L" if sct[3] == "u" else "l"
            else:
                dt = np.dtype(sct[3:])
                if sct[-1].isdigit() or not dt.char.isidentifier():
                    char = dt.str[1:]
                else:
                    char = dt.char
            name = f"SC_{char}"
        else:
            # builtins
            kind = np.dtype(globals()[sct]).kind
            name = f"PY_{kind}"

        names[sct] = name
        yield f"{name}: {sct}"

    return names  # noqa: B901


def __char(asdf: str) -> str:
    return np.dtype(asdf[3:]).char


def _gen_unary(fname: str, names: dict[str, str]) -> Generator[str]:
    fn: Callable[[Any], Any] = getattr(np.emath, fname)

    results: dict[str, list[str]] = {}
    for sct_arg, vals in VALS_EMATH.items():
        types_out_seen = set()
        results[sct_arg] = types_out = []
        for arg in vals:
            tp = type(out) if isinstance(out := fn(arg), np.generic) else np.object_

            if (sct := tp.__name__) not in types_out_seen:
                types_out_seen.add(sct)
                types_out.append(f"np.{sct}")

    print(f"{fname}:")
    for arg, types_out in results.items():
        yield f"assert_type(np.emath.{fname}({names[arg]}), {_union(*types_out)})"
        print(" ", f"{__char(arg)} -> {' | '.join(map(__char, types_out))}")
    print()


def _gen_binary(fname: str, names: dict[str, str]) -> Generator[str]:
    fn: Callable[[Any, Any], Any] = getattr(np.emath, fname)

    results: dict[tuple[str, str], list[str]] = {}
    for sct_lhs, vals_lhs in VALS_EMATH.items():
        for sct_rhs, vals_rhs in VALS_EMATH.items():
            types_out_seen = set()
            results[sct_lhs, sct_rhs] = types_out = []
            for lhs, rhs in itertools.product(vals_lhs, vals_rhs):
                val = fn(lhs, rhs)
                tp = type(val) if isinstance(val, np.generic) else np.object_

                if (sct := tp.__name__) not in types_out_seen:
                    types_out_seen.add(sct)
                    types_out.append(f"np.{sct}")

    print(f"{fname}:")
    sct_lhs_prev = None
    for (sct_lhs, sct_rhs), types_out in results.items():
        if sct_lhs_prev and sct_lhs != sct_lhs_prev:
            yield ""

        name_lhs, name_rhs = names[sct_lhs], names[sct_rhs]
        expr = f"np.emath.{fname}({name_lhs}, {name_rhs})"
        yield f"assert_type({expr}, {_union(*types_out)})"

        sct_lhs_prev = sct_lhs

        print(
            " ",
            f"({__char(sct_lhs)}, {__char(sct_rhs)}) "
            f"-> {' | '.join(map(__char, types_out))}",
        )
    print()


def _gen_all() -> Generator[str]:
    names = yield from _gen_names()

    binary_fns = {"logn", "power"}
    for fname in np.emath.__all__:
        if fname in binary_fns:
            continue

        yield LINESEP
        yield from _gen_unary(fname, names)

    # Yea... maybe later
    # https://github.com/numpy/numpy/issues/28367
    # for fname in binary_fns:
    #     yield LINESEP
    #     yield from _gen_binary(fname, names)

    yield ""


@np.errstate(all="ignore")
def main() -> None:
    """
    Output the generated `.pyi` source to stdout.

    TODO:
        - `intp`
        - `object_`
    """
    OUTPUT_FILE.write_text("\n".join(_gen_all()), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
