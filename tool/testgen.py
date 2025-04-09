"""Type-tests generation."""

# ruff: noqa: PLR0916, PLR6301, TD003, ERA001, D101, D102, DOC201

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import abc
import difflib
import itertools
import operator as op
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from typing import Any, ClassVar, Final, Literal, TypeAlias, TypeVar, cast, final
from typing_extensions import override

import numpy as np
import numpy.typing as npt
from tool.promotion import _typename as dtype_label
from tool.ufunc import _all_types as ufunc_signatures

###

_T = TypeVar("_T")

_Scalar: TypeAlias = np.number | np.bool | np.timedelta64 | np.datetime64 | complex
_BinOp: TypeAlias = Callable[[Any, Any], Any]
_BinOpKind: TypeAlias = Literal["arithmetic", "modular", "bitwise", "comparison"]
_BinOpName: TypeAlias = Literal[
    "add",
    "sub",
    "mul",
    "pow",
    "truediv",
    "floordiv",
    "mod",
    "divmod",
    "lshift",
    "rshift",
    "and",
    "or",
    "xor",
]
_UnOpName: TypeAlias = Literal["neg", "pos", "invert", "abs"]
_OpName: TypeAlias = Literal[_BinOpName, _UnOpName]

###

ROOT_DIR: Final = Path(__file__).parent.parent
TARGET_DIR: Final = ROOT_DIR / "src" / "numpy-stubs" / "@test" / "generated"

TAB: Final = " " * 4
BR: Final = "\n"

NP: Final = "np"
PREAMBLE_PREFIX: Final = "@generated"

_NUMBERS_ABSTRACT: Final = {
    "i": "signedinteger",
    "u": "unsignedinteger",
    "f": "floating",
    "c": "complexfloating",
    "".join(set("iu")): "integer",
    "".join(set("fc")): "inexact",
    "".join(set("iufc")): "number",
}
_NUMBERS_CONCRETE: Final = {
    "i": frozenset({f"{NP}.int8", f"{NP}.int16", f"{NP}.int32", f"{NP}.int64"}),
    "u": frozenset({f"{NP}.uint8", f"{NP}.uint16", f"{NP}.uint32", f"{NP}.uint64"}),
    "f": frozenset({f"{NP}.float32", f"{NP}.float64", f"{NP}.longdouble"}),
    "c": frozenset({f"{NP}.complex64", f"{NP}.complex128", f"{NP}.clongdouble"}),
}

DTYPE_CHARS: Final = "?bhilqBHILQefdgFDGMmOScUVT"  # ordered by personal preference

DATETIME_OPS: Final = {"add", "sub"}
TIMEDELTA_OPS: Final = DATETIME_OPS | {"mul", "truediv", "floordiv", "mod", "divmod"}
BITWISE_OPS: Final = {"lshift", "rshift", "and", "or", "xor"}
BITWISE_CHARS: Final = "?bhilqBHILQ"

INTP_EXPR: Final = f"{NP}.{np.intp.__name__}"

OP_UFUNCS: Final[dict[_OpName, np.ufunc]] = {
    "add": np.add,
    "sub": np.subtract,
    "mul": np.multiply,
    "pow": np.power,
    "truediv": np.true_divide,
    "floordiv": np.floor_divide,
    "mod": np.mod,
    "divmod": np.divmod,
    "lshift": np.left_shift,
    "rshift": np.right_shift,
    "and": np.bitwise_and,
    "or": np.bitwise_or,
    "xor": np.bitwise_xor,
    "invert": np.bitwise_not,
    "neg": np.negative,
    "pos": np.positive,
    "abs": np.abs,
}

###


def _ensure_tuple(x: _T | tuple[_T, ...], /) -> tuple[_T, ...]:
    if isinstance(x, tuple):
        return cast("tuple[_T, ...]", x)
    return (x,)


def _expr_assert_type(val_expr: str, type_expr: str, /) -> str:
    return f"assert_type({val_expr}, {type_expr})"


def _get_op_types(op: _OpName) -> tuple[np.dtype, ...]:
    ufunc = OP_UFUNCS[op]
    in_types = "".join(sig.split("->")[0] for sig in ufunc_signatures(ufunc))
    in_types = "".join(dict.fromkeys(in_types))  # dedupe in order
    return tuple(map(np.dtype, in_types))


def _scalar(key: str, /) -> _Scalar:
    if len(key) > 1:
        # must be one of the builtin scalars
        pytype: type[bool] = getattr(__builtins__, key)
        return pytype(1)

    dtype = np.dtype(key)

    if dtype.char == "M":
        # datetime64(1) is not valid, so use `NaT` instead (unitless)
        return np.datetime64()

    return dtype.type(max(dtype.num, 1))  # type: ignore[no-any-return]


def _sctype_expr(dtype: np.dtype | type[complex]) -> str:
    if isinstance(dtype, type):
        assert type.__module__ == "builtins", type
        return dtype.__name__

    if dtype.char == "T":
        return "str"

    if dtype.char == "g":
        name = "longdouble"
    elif dtype.char == "G":
        name = "clongdouble"
    elif dtype.char in "OSUVMm":
        name = dtype.type.__name__
    else:
        name = dtype.name

    return f"{NP}.{name}"


def _sctype_expr_from_value(value: _Scalar | tuple[_Scalar, ...], /) -> str:
    if isinstance(value, tuple):
        expr_args = ", ".join(map(_sctype_expr_from_value, value))
        return f"tuple[{expr_args}]"

    if isinstance(value, np.generic):
        return _sctype_expr(value.dtype)

    return type(value).__qualname__


def _dtype_expr(dtype: np.dtype, /) -> str:
    if dtype.char == "T":
        return f"{NP}.dtypes.StringDType"
    sctype_expr = _sctype_expr(dtype)
    return f"{NP}.dtype[{sctype_expr}]"


def _array_expr(
    dtype: np.dtype,
    /,
    *,
    ndim: int | None = None,
    npt: bool = False,
) -> str:
    if ndim is None and npt and dtype.char != "T":
        return f"npt.NDArray[{_sctype_expr(dtype)}]"

    if ndim is None:
        shape_expr = "tuple[int, ...]"
    else:
        shape_expr_args = ", ".join(["int"] * ndim) if ndim else "()"
        shape_expr = f"tuple[{shape_expr_args}]"

    dtype_expr = _dtype_expr(dtype)

    return f"{NP}.ndarray[{shape_expr}, {dtype_expr}]"


def __group_types(*types: str) -> tuple[dict[str, list[str]], list[str]]:
    # TODO(jorenham): character and flexible
    numbers: dict[str, list[str]] = {"i": [], "u": [], "f": [], "c": []}
    other: list[str] = []

    for tp in dict.fromkeys(types):
        kind: str = np.dtype(tp.removeprefix(f"{NP}.")).kind
        numbers.get(kind, other).append(tp)

    return {kind: tps for kind, tps in numbers.items() if tps}, other


def _union(*types: str) -> str:
    # union the types, and join unions if they contain each of the concrete subtypes
    numbers, other = __group_types(*types)

    kind_expr: dict[str, str] = {}
    combined: list[str] = []
    for kind, base in _NUMBERS_ABSTRACT.items():
        if kind not in numbers:
            continue

        if set(numbers[kind]) >= _NUMBERS_CONCRETE[kind]:
            expr = f"{NP}.{base}"
            kind_expr[kind] = expr
            combined.append(expr)
        else:
            combined.extend(numbers[kind])

    if other:
        if other[0] == f"{NP}.bool":
            combined = [other[0], *combined, *other[1:]]
        else:
            combined.extend(other)

    if len(kind_expr) == 4:
        expr_map = dict.fromkeys(kind_expr.values(), f"{NP}.number")
        combined = [expr_map.get(expr, expr) for expr in combined]
    elif len(kind_expr) > 1:
        if "u" in kind_expr and "i" in kind_expr:
            expr_map = dict.fromkeys([kind_expr["u"], kind_expr["i"]], f"{NP}.integer")
        elif "f" in kind_expr and "c" in kind_expr:
            expr_map = dict.fromkeys([kind_expr["f"], kind_expr["c"]], f"{NP}.inexact")
        else:
            expr_map = {}

        combined = [expr_map.get(expr, expr) for expr in combined]

    return " | ".join(dict.fromkeys(combined))


def _join(*types: str) -> str:
    """Find the common base type, i.e. union + upcast."""
    numbers, other = __group_types(*types)
    if other and numbers:
        raise NotImplementedError(f"join of non-number types: {types}")

    # special case for accidental `bool` return from `timedelta64.__eq__` on numpy <2.3
    if not numbers and len(other) == 2 and set(other) == {f"{NP}.bool", "bool"}:
        return f"{NP}.bool"

    # special case to avoid upcasting e.g. `[un]signedinteger | float64` to `number`
    if len(numbers) > 1 and len(numbers.get("f", [])) == 1 and "c" not in numbers:
        other.extend(numbers.pop("f"))

    if numbers:
        kinds = "".join(set(numbers))
        if len(kinds) == 1 and len(numbers[kinds]) == 1:
            expr = numbers[kinds][0]
        elif kinds in _NUMBERS_ABSTRACT:
            expr = f"{NP}.{_NUMBERS_ABSTRACT[kinds]}"
        else:
            expr = f"{NP}.number"
        other.insert(0, expr)

    return " | ".join(other)


def _strip_preamble(source: str) -> tuple[str | None, str]:
    preamble_prefix = f"# {PREAMBLE_PREFIX}"

    preamble: str | None = None
    lines: list[str] = []

    for line in source.splitlines(keepends=True):
        if preamble is None and line.startswith(preamble_prefix):
            preamble = line.removeprefix(preamble_prefix).strip()
        else:
            lines.append(line)

    return preamble, "".join(lines)


###


class TestGen(abc.ABC):
    stdlib_imports: ClassVar[tuple[str, ...]] = (
        "from typing_extensions import assert_type",
    )
    numpy_imports: ClassVar[tuple[str, ...]] = (f"import numpy as {NP}",)

    testname: str  # abstract
    stdlib_imports_extra: tuple[str, ...] = ()
    numpy_imports_extra: tuple[str, ...] = ()

    _names: Final[dict[str, str]]
    _current_indent: int

    def __init__(self) -> None:
        self._names = {tp: name for name, tp in self.get_names() if tp and name}
        self._current_indent = 0

    @property
    def path(self) -> Path:
        assert self.testname
        return TARGET_DIR / f"{self.testname}.pyi"

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

        yield f"# {PREAMBLE_PREFIX} {timestamp} with {here}"

    def _generate_imports(self) -> Generator[str]:
        # NOTE: The trailing newlines are required for ruff compatibility
        yield from sorted(self.stdlib_imports + self.stdlib_imports_extra)
        yield ""
        yield from sorted(self.numpy_imports + self.numpy_imports_extra)
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

        return BR.join(lines)

    @final
    def _read(self, /) -> str | None:
        if not self.path.exists():
            return None
        return self.path.read_text(encoding="utf-8")

    @final
    def _write(self, src: str, /) -> int:
        assert src, "cannot write empty test file"
        return self.path.write_text(src, encoding="utf-8", newline=BR)

    @final
    def regenerate(self, /, *, always: bool = False) -> Iterator[str]:
        src_new = self.build()

        head_new, body_new = _strip_preamble(src_new)
        assert head_new, src_new

        path_new = str(self.path.relative_to(ROOT_DIR))
        date_new = head_new.split(" ", 1)[0]

        if src_old := self._read():
            head_old, body_old = _strip_preamble(src_old)
            date_old = head_old.split(" ", 1)[0] if head_old else ""
            path_old = path_new
            write = always or not head_old or body_old != body_new
        else:
            body_old = path_old = date_old = ""
            write = True

        if write:
            self._write(src_new)

        lines_old = body_old.splitlines(keepends=True)
        lines_new = body_new.splitlines(keepends=True) if write else lines_old
        return difflib.unified_diff(
            lines_old,
            lines_new,
            fromfile=path_old,
            tofile=path_new,
            fromfiledate=date_old,
            tofiledate=date_new if write else date_old,
            n=0,
            lineterm=BR,
        )


@final
class EMath(TestGen):
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

    def _gen_binary(self, fn: _BinOp, /) -> Generator[tuple[str, str, str] | None]:
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
class LiteralBoolOps(TestGen):
    testname = "literal_bool_ops"

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

        assert len(results) == 2, results
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


@final
class ScalarOps(TestGen):
    testname = "scalar_ops_{}"

    OPS_ARITHMETIC: ClassVar[dict[str, _BinOp]] = {
        "{} + {}": op.__add__,
        "{} - {}": op.__sub__,
        "{} * {}": op.__mul__,
        "{}**{}": op.__pow__,
        "{} / {}": op.__truediv__,
    }
    OPS_MODULAR: ClassVar[dict[str, _BinOp]] = {
        "{} // {}": op.__floordiv__,
        "{} % {}": op.__mod__,
        "divmod({}, {})": divmod,
    }
    OPS_BITWISE: ClassVar[dict[str, _BinOp]] = {
        "{} << {}": op.__lshift__,
        "{} >> {}": op.__rshift__,
        "{} & {}": op.__and__,
        "{} ^ {}": op.__xor__,
        "{} | {}": op.__or__,
    }
    OPS_COMPARISON: ClassVar[dict[str, _BinOp]] = {
        "{} < {}": op.__lt__,
        "{} <= {}": op.__le__,
        "{} >= {}": op.__ge__,
        "{} > {}": op.__gt__,
        "{} == {}": op.__eq__,
        "{} != {}": op.__ne__,
    }

    NAMES: ClassVar = {
        # builtins (key length > 1)
        "bool": "b_py",
        "int": "i_py",
        "float": "f_py",
        "complex": "c_py",
        # numpy boolean
        "?": "b1",
        # signed integers
        "b": "i8",
        "h": "i16",
        np.dtype("int32").char: "i32",
        np.dtype("int64").char: "i64",
        # unsigned integers
        "B": "u8",
        "H": "u16",
        np.dtype("uint32").char: "u32",
        np.dtype("uint64").char: "u64",
        # real floating
        "e": "f16",
        "f": "f32",
        "d": "f64",
        "g": "f64l",
        # complex floating
        "F": "c64",
        "D": "c128",
        "G": "c128l",
        # temporal
        "M": "M64",
        "m": "m64",
        # # abstract numeric
        "bhil": "i",  # signedinteger
        "BHIL": "u",  # unsignedinteger
        "efdg": "f",  # floating
        "FDG": "c",  # complexfloating
        "bhilBHIL": "iu",  # integer
        "efdgFDG": "fc",  # inexact
        "bhilBHILefdgFDG": "iufc",  # number
    }
    ABSTRACT_TYPES: ClassVar = {
        "i": "signedinteger",
        "u": "unsignedinteger",
        "f": "floating",
        "c": "complexfloating",
        "iu": "integer",
        "fc": "inexact",
        "iufc": "number",
    }

    ops: Final[dict[str, _BinOp]]
    names: Final[dict[str, str]]
    reject: Final[frozenset[str]]

    def __init__(self, kind: _BinOpKind, /) -> None:
        reject: set[str] = set()
        ignore: set[str] = set()

        if kind in {"modular", "bitwise"}:
            # TODO(jorenham): Reject `inexact`
            reject |= {"bhilBHILefdgFDG", "FDG", "F", "D", "G"}

            # ignore the non-standard concrete complex (and float if bitwise) types
            # to avoid generating many redundant rejection tests
            ignore |= set("FGM")
            if kind == "bitwise":
                ignore |= set("efgm")

        match kind:
            case "arithmetic":
                ops = self.OPS_ARITHMETIC
            case "modular":
                ops = self.OPS_MODULAR
            case "bitwise":
                ops = self.OPS_BITWISE
                reject |= {"efdgFDG", "efdg", "e", "f", "d", "g"}
            case "comparison":
                ops = self.OPS_COMPARISON

        self.ops = ops
        self.names = {k: name for k, name in self.NAMES.items() if k not in ignore}
        self.reject = frozenset(reject)

        self.testname = self.testname.format(kind)

        super().__init__()

    def _is_builtin(self, key: str, /) -> bool:
        return len(key) > 1 and self.names[key].endswith("_py")

    def _is_abstract(self, key: str, /) -> bool:
        return len(key) > 1 and not self.names[key].endswith("_py")

    def _decompose(self, key: str, /) -> tuple[_Scalar, ...]:
        if not self._is_abstract(key):
            return (_scalar(key),)
        return tuple(map(_scalar, key))

    def _evaluate_concrete(self, op: str, lhs: str, rhs: str, /) -> str | None:
        if lhs in self.reject or rhs in self.reject:
            return None

        fn = self.ops[op]
        nout = 2 if fn.__module__ == "builtins" else 1

        exprs_seen: set[tuple[str, ...]] = set()
        expr_lists: tuple[list[str], ...] = tuple([] for _ in range(nout))
        for val_lhs, val_rhs in itertools.product(
            self._decompose(lhs),
            self._decompose(rhs),
        ):
            try:
                vals_out = fn(val_lhs, val_rhs)
            except TypeError:
                continue
            else:
                vals_out = _ensure_tuple(vals_out)
                exprs_out = tuple(map(_sctype_expr_from_value, vals_out))
                if exprs_out in exprs_seen:
                    continue
                exprs_seen.add(exprs_out)

            for expr_out, expr_list in zip(exprs_out, expr_lists, strict=True):
                expr_list.append(expr_out)

        if not expr_lists[0]:
            return None

        if len(expr_lists[0]) == 1:
            result_exprs = [expr_list[0] for expr_list in expr_lists]
        else:
            result_exprs = list(itertools.starmap(_join, expr_lists))

        return f"tuple[{', '.join(result_exprs)}]" if nout > 1 else result_exprs[0]

    def _assert_stmt(self, op: str, lhs: str, rhs: str, /) -> str | None:
        expr_eval = op.format(self.names[lhs], self.names[rhs])

        if not (expr_type := self._evaluate_concrete(op, lhs, rhs)):
            # generate rejection test, while avoiding trivial cases
            opname = self.ops[op].__name__.removesuffix("_")
            if (
                # ignore bitwise ops if neither arg is a bitwise char
                (opname in BITWISE_OPS and not {lhs, rhs} & set(BITWISE_CHARS))
                # ignore if either arg is datetime and and not a datetime op
                or (opname not in DATETIME_OPS and "M" in {lhs, rhs})
                # ignore if either arg is timedelta and and not a timedelta op
                or (opname not in TIMEDELTA_OPS and "m" in {lhs, rhs})
            ):
                return None

            # pyright special casing
            if opname == "divmod":
                pyright_rules = ["ArgumentType", "CallIssue"]
            else:
                pyright_rules = ["OperatorIssue"]
            pyright_ignore = ", ".join(map("report{}".format, pyright_rules))

            return "  ".join((
                expr_eval,
                "# type: ignore[operator]",
                f"# pyright: ignore[{pyright_ignore}]",
            ))

        # for `builtins.int` input, if the sctype is the alias of `intp`, then assume
        # that it actually originated from `intp`, and use that instead.
        if (
            "int" in {lhs, rhs}
            and lhs not in "lLqQ"
            and rhs not in "lLqQ"
            and expr_type == INTP_EXPR
        ):
            expr_type = f"{NP}.int_"

        if expr_type == "bool":
            return None

        stmt = _expr_assert_type(expr_eval, expr_type)

        # workaround for mypy's lack of support for reflected binary ops like __radd__
        if (
            op in self.OPS_ARITHMETIC | self.OPS_MODULAR
            and lhs == rhs
            and (abstract_arg := self.ABSTRACT_TYPES.get(self.names[lhs]))
        ):
            if abstract_arg == "integer" and " / " not in op:
                mypy_ignore = "assert-type, operator"
            elif abstract_arg == "inexact":
                mypy_ignore = "operator"
            else:
                mypy_ignore = ""

            if mypy_ignore:
                stmt = "  # ".join((stmt, f"type: ignore[{mypy_ignore}]", "🐴"))

        return stmt

    @override
    def _generate_names_section(self) -> Generator[str]:
        yield from self._generate_section("scalars")

    @override
    def get_names(self) -> Iterable[tuple[str, str]]:
        # builtin scalars
        for builtin, name in self.names.items():
            if self._is_builtin(builtin):
                yield name, builtin

        # concrete numpy scalars
        yield "", ""
        for char, name in self.names.items():
            if len(char) == 1:
                yield name, _sctype_expr(np.dtype(char))

        # abstract numpy scalars
        yield "", ""
        for char, kind in self.names.items():
            if self._is_abstract(char):
                yield kind, f"{NP}.{self.ABSTRACT_TYPES[kind]}"

    @override
    def get_testcases(self) -> Iterable[str | None]:
        for symbol, fn in self.ops.items():
            opname = fn.__name__.removesuffix("_")

            yield from self._generate_section(f"__[r]{opname}__")

            for lhs in self.names:
                if self._is_builtin(lhs):
                    # will cause false positives on pyright; as designed, of course
                    continue

                n = 0
                for rhs in self.names:
                    if fn.__name__ in {"eq", "ne"} and self._is_abstract(rhs):
                        # will be inferred by mypy as `Any` for some reason
                        continue

                    if stmt := self._assert_stmt(symbol, lhs, rhs):
                        yield stmt
                        n += 1
                if n:
                    yield ""


class NDArrayOps(TestGen):
    testname = "ndarray_ops_{}"
    numpy_imports_extra = ("import numpy.typing as npt",)

    opname: _OpName
    opfunc: Callable[..., Any]
    dtypes: list[np.dtype]

    def __init__(self, opname: _OpName, /) -> None:
        ufunc = OP_UFUNCS[opname]
        if not ufunc.nin == 2 and not ufunc.nout == 1:
            raise NotImplementedError("non-binops not supported")

        self.opname = opname
        if opname == "divmod":
            self.opfunc = divmod
        else:
            self.opfunc = getattr(op, opname, None) or getattr(op, opname + "_")
        self.testname = self.testname.format(opname)

        dtypes_seen: set[str] = set()
        self.dtypes = []
        for dtype in sorted(
            _get_op_types(opname),
            key=lambda dt: DTYPE_CHARS.index(dt.char),
        ):
            label = dtype_label(dtype)
            if label in dtypes_seen:
                continue
            dtypes_seen.add(label)

            if dtype not in dtypes_seen:
                self.dtypes.append(dtype)

        super().__init__()

    @staticmethod
    def _get_arrays(
        dtype1: np.dtype,
        dtype2: np.dtype,
    ) -> tuple[npt.NDArray[Any], npt.NDArray[Any]]:
        arr1 = np.ones((1, 1), dtype=dtype1)
        arr2 = np.ones((1, 1), dtype=dtype2)

        if dtype1 != dtype2:
            # prefer compatible object_ arrays
            if dtype1.char == "O":
                arr1 = arr2.astype("O")
            if dtype2.char == "O":
                arr2 = arr1.astype("O")

        return arr1, arr2

    @override
    def get_names(self) -> Iterable[tuple[str, str]]:
        for dtype in self.dtypes:
            yield f"array_{dtype_label(dtype)}_nd", _array_expr(dtype, npt=True)

    @override
    def get_testcases(self) -> Iterable[str | None]:
        op_expr_template = str(self.opfunc.__doc__)[8:-1]
        op_expr_template = op_expr_template.replace("a", "{}").replace("b", "{}")

        yield from self._generate_section()

        for dtype1 in self.dtypes:
            yielded = 0
            for dtype2 in self.dtypes:
                name1 = f"array_{dtype_label(dtype1)}_nd"
                name2 = f"array_{dtype_label(dtype2)}_nd"
                op_expr = op_expr_template.format(name1, name2)

                arr1, arr2 = self._get_arrays(dtype1, dtype2)

                try:
                    out = self.opfunc(arr1, arr2)
                except TypeError:
                    testcase = "  ".join((  # noqa: FLY002
                        op_expr,
                        "# type: ignore[operator]",
                        "# pyright: ignore[reportOperatorIssue]",
                    ))
                else:
                    out_type_expr = _array_expr(out.dtype, npt=True)
                    testcase = _expr_assert_type(op_expr, out_type_expr)

                yield testcase
                yielded += 1

            if yielded > 2:
                # avoid inserting excessive newlines
                yield ""


TESTGENS: Final[Sequence[TestGen]] = [
    EMath(binary=False),
    LiteralBoolOps(),
    ScalarOps("arithmetic"),
    ScalarOps("modular"),
    ScalarOps("bitwise"),
    ScalarOps("comparison"),
]


@np.errstate(all="ignore")
def main() -> None:
    """(Re)generate the `src/numpy-stubs/@test/generated/{}.pyi` type-tests."""
    for testgen in TESTGENS:
        sys.stdout.writelines(testgen.regenerate())


if __name__ == "__main__":
    main()
