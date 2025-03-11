"""Type-tests generation."""

# ruff: noqa: PLR6301, TD003, ERA001, D101, D102

import abc
import itertools
import operator as op
from collections.abc import Callable, Generator, Iterable, Sequence
from pathlib import Path
from typing import Any, ClassVar, Final, cast, final
from typing_extensions import override

import numpy as np

ROOT_DIR: Final = Path(__file__).parent.parent
TEST_DIR: Final = ROOT_DIR / "test"
OUTPUT_DIR: Final = TEST_DIR / "generated"

TAB: Final = " " * 4
LINEBREAK: Final = "\n"

TYPES_I: Final = frozenset({"np.int8", "np.int16", "np.int32", "np.int64"})
TYPES_U: Final = frozenset({"np.uint8", "np.uint16", "np.uint32", "np.uint64"})
TYPES_F: Final = frozenset({"np.float32", "np.float64", "np.longdouble"})
TYPES_C: Final = frozenset({"np.complex64", "np.complex128", "np.clongdouble"})
TYPES_IU: Final = TYPES_I | TYPES_U
TYPES_FC: Final = TYPES_F | TYPES_C
TYPES_IUFC: Final = TYPES_IU | TYPES_FC


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


def _union(*types: str) -> str:
    ints: set[str] = set()
    uints: set[str] = set()
    floats: set[str] = set()
    cfloats: set[str] = set()
    others: set[str] = set()

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


class TestGen(abc.ABC):
    testname: ClassVar[str]  # abstract

    _names: Final[dict[str, str]]
    _current_indent: int

    def __init__(self) -> None:
        self._names = {tp: name for name, tp in self.get_names()}
        self._current_indent = 0

    @property
    def output_file(self) -> Path:
        return OUTPUT_DIR / f"{self.testname}.pyi"

    @abc.abstractmethod
    def get_names(self) -> Iterable[tuple[str, str]]:
        return ()

    @abc.abstractmethod
    def get_testcases(self) -> Iterable[str | None]:
        # yield None to indicate a section break
        yield from ()

    @final
    def indent(self) -> None:
        self._current_indent += 1

    @final
    def dedent(self) -> None:
        assert self._current_indent > 0
        self._current_indent -= 1

    def _generate_section(self, /, *lines: str) -> Generator[str]:
        yield ""
        yield "###"
        for line in lines:
            yield f"# {line}"
        yield ""

    def _generate_preamble(self) -> Generator[str]:
        timestamp = f"{np.datetime64('now')}Z"
        here = Path(__file__).relative_to(ROOT_DIR)

        yield f"# @generated {timestamp} with {here}"

    def _generate_imports(self) -> Generator[str]:
        # NOTE: The trailing newlines are required for ruff compatibility
        yield "from typing_extensions import assert_type"
        yield ""
        yield "import numpy as np"
        yield ""

    def _generate_names_section(self) -> Generator[str]:
        yield from self._generate_section()

    def _generate_names(self) -> Generator[str]:
        yield from self._generate_names_section()
        for name, annotation in self.get_names():
            yield f"{name}: {annotation}"

    def _generate_testcases(self) -> Generator[str]:
        # yield from self._generate_section()
        for testcase in self.get_testcases():
            if testcase is None:
                yield from self._generate_section()
            else:
                yield testcase

    def _generate(self) -> Generator[str]:
        yield from self._generate_preamble()
        yield from self._generate_imports()
        yield from self._generate_names()
        yield from self._generate_testcases()

    @final
    def build(self) -> str:
        # pretend we have already seen one empty line to avoid leading newline
        n_empty = 1

        lines: list[str] = []
        for item in self._generate():
            for rawline in item.splitlines(keepends=True) if "\n" in item else [item]:
                # remove trailing whitespace
                line = rawline.rstrip()

                # skip consecutive empty lines
                if not line:
                    n_empty += 1
                    if n_empty > 1:
                        continue
                else:
                    n_empty = 0

                    # indent non-empty lines
                    line = TAB * self._current_indent + line

                lines.append(line)

        # ensure trailing newline
        if not n_empty:
            lines.append("")

        return LINEBREAK.join(lines)

    @final
    def generate(self, /) -> tuple[Path, bool]:
        output = self.build()
        output_file = self.output_file
        exists = output_file.exists()
        output_file.write_text(output, encoding="utf-8", newline=LINEBREAK)
        return output_file, exists


@final
class EMathTestGen(TestGen):
    testname = "emath"

    VALUES: Final[dict[str, list[Any]]] = {
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

    def __init__(self, /, *, binary: bool = False) -> None:
        self._binary = binary
        super().__init__()

    def get_names(self) -> Iterable[tuple[str, str]]:
        for sct in self.VALUES:
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

            yield name, sct

    def _gen_unary(self, fn: Callable[[Any], Any], /) -> Generator[tuple[str, str]]:
        for sct_arg, vals in self.VALUES.items():
            types_out_seen: set[str] = set()
            types_out: list[str] = []
            for arg in vals:
                tp = (
                    type(cast("np.generic", out))  # type: ignore[redundant-cast]
                    if isinstance(out := fn(arg), np.generic)
                    else np.object_
                )

                if (sct := tp.__name__) not in types_out_seen:
                    types_out_seen.add(sct)
                    types_out.append(f"np.{sct}")

            yield self._names[sct_arg], _union(*types_out)

    def _gen_binary(
        self,
        fn: Callable[[Any, Any], Any],
        /,
    ) -> Generator[tuple[str, str, str] | None]:
        results: dict[tuple[str, str], list[str]] = {}
        for sct_lhs, vals_lhs in self.VALUES.items():
            for sct_rhs, vals_rhs in self.VALUES.items():
                types_out_seen: set[str] = set()
                types_out: list[str]
                results[sct_lhs, sct_rhs] = types_out = []
                for lhs, rhs in itertools.product(vals_lhs, vals_rhs):
                    val = fn(lhs, rhs)
                    tp = (
                        type(cast("np.generic", val))  # type: ignore[redundant-cast]
                        if isinstance(val, np.generic)
                        else np.object_
                    )

                    if (sct := tp.__name__) not in types_out_seen:
                        types_out_seen.add(sct)
                        types_out.append(f"np.{sct}")

        names = self._names
        sct_lhs_prev = None
        for (sct_lhs, sct_rhs), types_out in results.items():
            if sct_lhs_prev and sct_lhs != sct_lhs_prev:
                yield None

            yield names[sct_lhs], names[sct_rhs], _union(*types_out)

            sct_lhs_prev = sct_lhs

    def get_testcases(self) -> Iterable[str | None]:
        # yield None to indicate a section break
        binary_fns = {"logn", "power"}
        for fname in np.emath.__all__:
            if fname in binary_fns:
                continue

            qualname = f"np.emath.{fname}"
            func1 = getattr(np.emath, fname)

            yield from self._generate_section(qualname)
            for arg, expect in self._gen_unary(func1):
                yield f"assert_type({qualname}({arg}), {expect})"

        if self._binary:
            for fname in binary_fns:
                qualname = f"np.emath.{fname}"
                func2 = getattr(np.emath, fname)

                yield from self._generate_section(qualname)
                for item in self._gen_binary(func2):
                    if item is None:
                        yield ""
                    else:
                        lhs, rhs, expect = item
                        yield f"assert_type({qualname}({lhs}, {rhs}), {expect})"

        yield ""


@final
class ScalarBinopTestGen(TestGen):
    testname = "scalar_binops"

    OPS: ClassVar = {
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

    NAMES: ClassVar = {
        # builtins (key length > 1)
        "bool": "b0",
        # TODO(jorenham): Re-enable after binops use `_numtype.Is` (avoid promotions)
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

    def _assert_stmt(self, op: str, lhs: str, rhs: str, /) -> str | None:
        pad = " " * (
            op != "**"
        )  # ruff doesn't like whitespace around `**` for some reason
        expr_eval = f"{self.NAMES[lhs]}{pad}{op}{pad}{self.NAMES[rhs]}"

        try:
            val_out = self.OPS[op](_scalar(lhs), _scalar(rhs))
        except TypeError:
            # generate rejection test, while avoiding trivial cases
            if op not in DATETIME_OPS and (lhs == "M" or rhs == "M"):
                return None
            if op not in TIMEDELTA_OPS and (lhs == "m" or rhs == "m"):
                return None
            if op in BITWISE_OPS and not (
                lhs in BITWISE_CHARS and rhs in BITWISE_CHARS
            ):
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

    @override
    def _generate_names_section(self) -> Generator[str]:
        yield from self._generate_section("scalars")

    @override
    def get_names(self) -> Iterable[tuple[str, str]]:
        for builtin, name in self.NAMES.items():
            if len(builtin) > 1:
                yield name, builtin

        # numpy scalars
        for char, name in self.NAMES.items():
            if len(char) == 1:
                yield name, _sctype_expr(np.dtype(char))

    @override
    def get_testcases(self) -> Iterable[str | None]:
        for symbol, fn in self.OPS.items():
            opname = fn.__name__.removesuffix("_")

            yield from self._generate_section(f"__[r]{opname}__")

            for lhs in self.NAMES:
                # skip builtins on the lhs; avoid a pyright ~bug~ "as designed"
                if len(lhs) > 1:
                    continue

                n = 0
                for rhs in self.NAMES:
                    if stmt := self._assert_stmt(symbol, lhs, rhs):
                        yield stmt
                        n += 1
                if n:
                    yield ""


TESTGENS: Final[Sequence[TestGen]] = [
    EMathTestGen(binary=False),
    ScalarBinopTestGen(),
]


@np.errstate(all="ignore")
def main() -> None:
    """(Re)generate the `test/generated/{}.pyi` type-tests."""
    for testgen in TESTGENS:
        path, exists = testgen.generate()
        relpath = path.relative_to(ROOT_DIR)
        print("regenerated" if exists else "  generated", str(relpath))


if __name__ == "__main__":
    main()
