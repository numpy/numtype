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

NP = "np"

TYPES_I: Final = frozenset({f"{NP}.int8", f"{NP}.int16", f"{NP}.int32", f"{NP}.int64"})
TYPES_U: Final = frozenset({
    f"{NP}.uint8",
    f"{NP}.uint16",
    f"{NP}.uint32",
    f"{NP}.uint64",
})
TYPES_F: Final = frozenset({f"{NP}.float32", f"{NP}.float64", f"{NP}.longdouble"})
TYPES_C: Final = frozenset({f"{NP}.complex64", f"{NP}.complex128", f"{NP}.clongdouble"})
TYPES_IU: Final = TYPES_I | TYPES_U
TYPES_FC: Final = TYPES_F | TYPES_C
TYPES_IUFC: Final = TYPES_IU | TYPES_FC

DATETIME_OPS = {"+", "-"}
TIMEDELTA_OPS = DATETIME_OPS | {"*", "/", "//", "%"}
BITWISE_OPS = {"<<", ">>", "&", "^", "|"}
BITWISE_CHARS = "?bhilqBHILQ"


def _expr_assert_type(val_expr: str, type_expr: str, /) -> str:
    return f"assert_type({val_expr}, {type_expr})"


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
        return f"{NP}.longlong"
    if dtype.char == "Q":
        return f"{NP}.ulonglong"
    if dtype.char == "g":
        return f"{NP}.longdouble"
    if dtype.char == "G":
        return f"{NP}.clongdouble"

    name = dtype.name
    assert "[" not in name, "units not supported yet"
    return f"{NP}.{name}"


def _union(*types: str) -> str:
    ints: set[str] = set()
    uints: set[str] = set()
    floats: set[str] = set()
    cfloats: set[str] = set()
    others: set[str] = set()

    for tp in types:
        kind = np.dtype(tp.removeprefix(f"{NP}.")).kind
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
            yield f"{name}: {annotation}" if name else ""

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
        # f"{NP}.bool": [np.True_],  # same as int8
        f"{NP}.uint8": [np.uint8(0), np.uint8(1), np.uint8(9)],
        f"{NP}.uint16": [np.uint16(0), np.uint16(1), np.uint16(9)],
        f"{NP}.uint32": [np.uint32(0), np.uint32(1), np.uint32(9)],
        f"{NP}.uint64": [np.uint64(0), np.uint64(1), np.uint64(9)],
        f"{NP}.int8": [np.int8(0), np.int8(1), np.int8(9), np.int8(-9), np.int8(-1)],
        f"{NP}.int16": [
            np.int16(0),
            np.int16(1),
            np.int16(9),
            np.int16(-9),
            np.int16(-1),
        ],
        f"{NP}.int32": [
            np.int32(0),
            np.int32(1),
            np.int32(9),
            np.int32(-9),
            np.int32(-1),
        ],
        f"{NP}.int64": [
            np.int64(0),
            np.int64(1),
            np.int64(9),
            np.int64(-9),
            np.int64(-1),
        ],
        f"{NP}.float16": [
            np.float16(0),
            np.float16(1),
            np.float16(9),
            np.float16(-9),
            np.float16(-1),
        ],
        f"{NP}.float32": [
            np.float32(0),
            np.float32(1),
            np.float32(9),
            np.float32(-9),
            np.float32(-1),
        ],
        f"{NP}.float64": [
            np.float64(0),
            np.float64(1),
            np.float64(9),
            np.float64(-9),
            np.float64(-1),
        ],
        f"{NP}.longdouble": [
            np.longdouble(0),
            np.longdouble(1),
            np.longdouble(9),
            np.longdouble(-9),
            np.longdouble(-1),
        ],
        f"{NP}.complex64": [
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
        f"{NP}.complex128": [
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
        f"{NP}.clongdouble": [
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

    @override
    def get_names(self) -> Iterable[tuple[str, str]]:
        for sct in self.VALUES:
            if sct.startswith(f"{NP}."):
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
                    types_out.append(f"{NP}.{sct}")

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
                        types_out.append(f"{NP}.{sct}")

        names = self._names
        sct_lhs_prev = None
        for (sct_lhs, sct_rhs), types_out in results.items():
            if sct_lhs_prev and sct_lhs != sct_lhs_prev:
                yield None

            yield names[sct_lhs], names[sct_rhs], _union(*types_out)

            sct_lhs_prev = sct_lhs

    @override
    def get_testcases(self) -> Iterable[str | None]:
        # yield None to indicate a section break
        binary_fns = {"logn", "power"}
        for fname in np.emath.__all__:
            if fname in binary_fns:
                continue

            qualname = f"{NP}.emath.{fname}"
            func1 = getattr(np.emath, fname)

            yield from self._generate_section(qualname)
            for arg, expect in self._gen_unary(func1):
                yield _expr_assert_type(f"{qualname}({arg})", expect)

        if self._binary:
            for fname in binary_fns:
                qualname = f"{NP}.emath.{fname}"
                func2 = getattr(np.emath, fname)

                yield from self._generate_section(qualname)
                for item in self._gen_binary(func2):
                    if item is None:
                        yield ""
                    else:
                        lhs, rhs, expect = item
                        yield _expr_assert_type(f"{qualname}({lhs}, {rhs})", expect)

        yield ""


@final
class ScalarBinOpTestGen(TestGen):
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
        "int": "i0",
        "float": "f0",
        "complex": "c0",
        # numpy boolean
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
    INTP_EXPR: ClassVar = np.intp.__name__

    def _assert_stmt(self, op: str, lhs: str, rhs: str, /) -> str | None:
        # ruff doesn't like whitespace around `**` for some reason
        pad = " " * (op != "**")
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

            return "  ".join((  # noqa: FLY002
                expr_eval,
                "# type: ignore[operator]",
                "# pyright: ignore[reportOperatorIssue]",
            ))

        expr_type = (  # redundant cast is needed for pyright compat
            _sctype_expr(cast("np.generic", val_out).dtype)  # type: ignore[redundant-cast]
            if isinstance(val_out, np.generic)
            else type(val_out).__qualname__
        )

        # for `builtins.int` input, if the sctype is the alias of `intp`, then assume
        # that it actually originated from `intp`, and use that instead.
        if "int" in {lhs, rhs} and lhs not in "lLqQ" and rhs not in "lLqQ":
            expr_name = expr_type.removeprefix(f"{NP}.")
            if expr_name == self.INTP_EXPR:
                expr_type = f"{NP}.int_"

        return None if expr_type == "bool" else _expr_assert_type(expr_eval, expr_type)

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


@final
class BoolBitOpTestGen(TestGen):
    testname = "bool_bitops"

    UNOPS: ClassVar = {
        "{}.__bool__()": bool,
        "abs({})": abs,
        "~{}": op.__invert__,
    }
    CMPOPS: ClassVar = {
        "{} == {}": op.__eq__,
        "{} != {}": op.__ne__,
        "{} < {}": op.__lt__,
        "{} <= {}": op.__le__,
        "{} > {}": op.__gt__,
        "{} >= {}": op.__ge__,
    }
    BINOPS: ClassVar = {
        "{} + {}": op.__add__,
        "{} * {}": op.__mul__,
        "{} & {}": op.__and__,
        "{} ^ {}": op.__xor__,
        "{} | {}": op.__or__,
    }

    NAMES_NP: ClassVar = [f"np{v}" for v in "01_"]
    NAMES_PY: ClassVar = [f"py{v}" for v in "01_"]

    @staticmethod
    def values(name: str) -> Generator[bool | np.bool]:
        tp = {"py": bool, "np": np.bool}[name[:2]]
        if name[-1] in "_0":
            yield tp(0)
        if name[-1] in "_1":
            yield tp(1)

    @staticmethod
    def _eval_results_to_str(results: Iterable[bool | np.bool]) -> str:
        results = set(results)
        if len(results) == 1:
            val = results.pop()
            return f"Literal[{val}]" if isinstance(val, bool) else f"Bool{int(val)}"

        assert len(results) == 2, results  # noqa: PLR2004
        return "bool" if isinstance(results.pop(), bool) else "Bool_"

    @classmethod
    def eval1(cls, fn: Callable[[Any], bool | np.bool], arg: str) -> str:
        return cls._eval_results_to_str({fn(a) for a in cls.values(arg)})

    @classmethod
    def eval2(cls, fn: Callable[[Any, Any], np.bool], lhs: str, rhs: str) -> str:
        results: set[np.bool] = set()
        for a in cls.values(lhs):
            for b in cls.values(rhs):
                out = fn(a, b)
                assert isinstance(out, np.bool), out
                results.add(out)
        return cls._eval_results_to_str(results)

    @override
    def _generate_imports(self) -> Generator[str]:
        # NOTE: The trailing newlines are required for ruff compatibility
        yield "from typing import Literal, TypeAlias"
        yield from super()._generate_imports()

    @override
    def _generate_names(self) -> Generator[str]:
        yield from self._generate_section()
        yield "Bool_: TypeAlias = np.bool"
        yield "Bool0: TypeAlias = np.bool[Literal[False]]"
        yield "Bool1: TypeAlias = np.bool[Literal[True]]"

        yield from self._generate_section()
        yield "py_: bool"
        yield "py0: Literal[False]"
        yield "py1: Literal[True]"
        yield ""
        yield "np_: Bool_"
        yield "np0: Bool0"
        yield "np1: Bool1"

    def _gen_unary(self) -> Generator[str]:
        for tmpl, fn in self.UNOPS.items():
            yield from self._generate_section(f"__{fn.__name__.removesuffix('_')}__")

            for a in self.NAMES_NP:
                yield _expr_assert_type(tmpl.format(a), self.eval1(fn, a))

    def _gen_comparison(self) -> Generator[str]:
        for tmpl, fn in self.CMPOPS.items():
            yield from self._generate_section(f"__{fn.__name__.removesuffix('_')}__")

            # np, np
            deferred: list[str] = []
            seen_a: set[str] = set()
            for a, b in itertools.product(self.NAMES_NP, self.NAMES_NP):
                # if b in seen_a:
                #     continue
                line = _expr_assert_type(tmpl.format(a, b), self.eval2(fn, a, b))
                if "_" in {a[-1], b[-1]}:
                    deferred.append(line)
                else:
                    yield line
                seen_a.add(a)

            # np, np (mixed)
            yield ""
            yield from iter(deferred)

            # np, py
            yield ""
            for a, b in itertools.product(self.NAMES_NP, self.NAMES_PY):
                yield _expr_assert_type(tmpl.format(a, b), self.eval2(fn, a, b))

    def _gen_binary(self) -> Generator[str]:
        for tmpl, fn in self.BINOPS.items():
            opname = fn.__name__.removesuffix("_")
            yield from self._generate_section(f"__[r]{opname}__")

            # np, np (literals)
            deferred: list[str] = []
            for a, b in itertools.product(self.NAMES_NP, self.NAMES_NP):
                line = _expr_assert_type(tmpl.format(a, b), self.eval2(fn, a, b))
                if "_" in {a[-1], b[-1]}:
                    deferred.append(line)
                else:
                    yield line

            # np, np (mixed)
            yield ""
            yield from iter(deferred)

            # np, py
            yield ""
            for a, b in itertools.product(self.NAMES_NP, self.NAMES_PY):
                yield _expr_assert_type(tmpl.format(a, b), self.eval2(fn, a, b))

            # py, np
            yield ""
            for a, b in itertools.product(self.NAMES_PY, self.NAMES_NP):
                yield _expr_assert_type(tmpl.format(a, b), self.eval2(fn, a, b))

    @override
    def get_testcases(self) -> Iterable[str | None]:
        yield from self._gen_unary()
        yield from self._gen_comparison()
        yield from self._gen_binary()


TESTGENS: Final[Sequence[TestGen]] = [
    EMathTestGen(binary=False),
    ScalarBinOpTestGen(),
    BoolBitOpTestGen(),
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
