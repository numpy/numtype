"""Type-tests generation."""

# ruff: noqa: PLR0916, PLR6301, ERA001, D101, D102, DOC201

import functools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import abc
import difflib
import itertools
import operator as op
import textwrap
from collections.abc import Callable, Generator, Iterable, Iterator, Mapping, Sequence
from typing import (
    Any,
    ClassVar,
    Final,
    Literal,
    TypeAlias,
    TypeVar,
    cast,
    final,
    overload,
)
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
    "matmul",
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
_UnOpName: TypeAlias = Literal["abs", "neg", "pos", "invert"]
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
    "matmul": np.matmul,
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


def _expr_assert_type(
    val_expr: str,
    type_expr: str,
    /,
    *,
    wrap: int = 120,
) -> str:
    out = f"assert_type({val_expr}, {type_expr})"
    if len(out) > wrap or "\n" in out:
        val_expr = textwrap.indent(val_expr, TAB)
        type_expr = textwrap.indent(type_expr, TAB)
        out = f"assert_type(\n{val_expr},\n{type_expr},\n)"
    return out


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


def _array_expr_single(
    *dtypes: np.dtype,
    ndim: int | None = None,
    npt: bool = False,
) -> str:
    assert dtypes

    chars = {dtype.char for dtype in dtypes}
    kinds = {dtype.kind for dtype in dtypes}
    assert len(chars) == 1 or not kinds - {"i", "u", "f", "c"}, (
        "unsupported multiple dtypes"
    )

    if "T" in chars:
        assert len(chars) == 1
        dtype_expr = f"{NP}.dtypes.StringDType"
    else:
        sctype_exprs = [_sctype_expr(dtype) for dtype in dtypes]
        if len(sctype_exprs) == 1:
            sctype_expr = sctype_exprs[0]
        else:
            sctype_expr = _join(*sctype_exprs)

        if ndim is None and npt:
            return f"npt.NDArray[{sctype_expr}]"

        dtype_expr = f"{NP}.dtype[{sctype_expr}]"

    if ndim is None:
        shape_expr = "tuple[int, ...]"
    else:
        shape_expr_args = ", ".join(["int"] * ndim) if ndim else "()"
        shape_expr = f"tuple[{shape_expr_args}]"

    return f"{NP}.ndarray[{shape_expr}, {dtype_expr}]"


def _array_expr(
    *dtypess: tuple[np.dtype, ...],
    ndim: int | None = None,
    npt: bool = False,
) -> str:
    assert dtypess

    ntypes = len(dtypess[0])
    assert ntypes in {1, 2}

    expr1 = _array_expr_single(*(dts[0] for dts in dtypess), ndim=ndim, npt=npt)

    if ntypes == 1:
        return expr1

    expr2 = _array_expr_single(*(dts[1] for dts in dtypess), ndim=ndim, npt=npt)

    expr = f"tuple[{expr1}, {expr2}]"
    if "\n" in expr or "|" in expr:
        expr1 = textwrap.indent(expr1, TAB)
        expr2 = textwrap.indent(expr2, TAB)
        expr = f"tuple[\n{expr1},\n{expr2},\n]"

    return expr


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
    if len(types) == 1:
        return types[0]

    numbers, other = __group_types(*types)
    if other and numbers:
        raise NotImplementedError(f"join of non-number types: {types}")

    if len(types) == len(numbers) == 2 and not other:
        # union two types if they're different kinds, e.g. `np.int8 | np.uint8` instead
        # of `np.integer`
        return " | ".join(kind_types[0] for kind_types in numbers.values())

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

    def _evaluate(self, op: str, lhs: str, rhs: str, /) -> str | None:
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
                return None

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

        if not (expr_type := self._evaluate(op, lhs, rhs)):
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

        return _expr_assert_type(expr_eval, expr_type)

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
    testname = "ndarray_{}"
    numpy_imports_extra = ("import numpy.typing as npt",)

    shape: Final[tuple[int, ...]]
    opname: _OpName
    opfunc: Callable[..., Any]
    n_in: Literal[1, 2]
    n_out: Literal[1, 2]

    dtypes: dict[str, tuple[np.dtype, ...]]

    def __init__(self, opname: _OpName, /, *, shape: tuple[int, ...] = (1, 1)) -> None:
        self.shape = shape

        ufunc = OP_UFUNCS[opname]

        if ufunc.nin == 1:
            self.n_in = 1
        elif ufunc.nin == 2:
            self.n_in = 2
        else:
            raise TypeError("operator must be unary or binary")

        if ufunc.nout == 1:
            self.n_out = 1
        elif ufunc.nout == 2:
            self.n_out = 2
        else:
            raise TypeError("operator must return either one or two values")

        self.opname = opname
        if opname == "abs":
            self.opfunc = abs
        elif opname == "divmod":
            self.opfunc = divmod
        else:
            self.opfunc = getattr(op, opname, None) or getattr(op, opname + "_")

        self.testname = self.testname.format(opname)

        self.dtypes = {}
        self.__init_dtypes()

        super().__init__()

    @functools.cached_property
    def __op_expr_template(self) -> str:
        if self.opname == "abs":
            return "abs({})"
        if self.opname == "pow":
            return "{}**{}"
        if self.opname == "divmod":
            return "divmod({}, {})"

        doc = self.opfunc.__doc__
        assert doc, "running python with -OO is not supported"
        assert doc.startswith("Same as "), doc
        assert doc.endswith("."), doc

        doc_expr = doc[8:-1]

        placeholder = "{}"
        if doc_expr[-1] == "a":
            # unary
            assert "b" not in doc_expr, doc_expr
            template = doc_expr[:-1] + placeholder
        else:
            # binary
            assert doc_expr[0] == "a", doc_expr
            assert doc_expr[-1] == "b", doc_expr
            template = placeholder + doc_expr[1:-1] + placeholder
        return template

    @property
    def _scalars_py(self) -> Mapping[str, type[complex | bytes | str]]:
        kindmap = {"b": bool, "i": int, "f": float, "c": complex, "S": bytes, "U": str}
        kinds = {
            dtypes[0].kind: "" for dtypes in self.dtypes.values() if len(dtypes) == 1
        }
        return {f"{kind}_py": kindmap[kind] for kind in kinds if kind in kindmap}

    @property
    def _mypy_rules(self) -> str:
        return "misc" if self.n_in == 1 else "operator"

    @property
    def _pyright_rules(self) -> str:
        if self.opname in {"abs", "divmod"}:
            return "reportArgumentType, reportCallIssue"
        return "reportOperatorIssue"

    @staticmethod
    def _abstract_expr(label: str, /) -> str:
        sctype_name = {
            "i": "signedinteger",
            "u": "unsignedinteger",
            "f": "floating",
            "c": "complexfloating",
            "iu": "integer",
            "fc": "inexact",
            "iufc": "number",
        }[label]
        return f"{NP}.{sctype_name}"

    def __init_dtypes(self) -> None:
        seen_dtypes: set[str] = set()
        unseen_abstract = {
            "i": {dtype_label(np.dtype(f"i{nbit}")) for nbit in (1, 2, 4, 8)},
            "u": {dtype_label(np.dtype(f"u{nbit}")) for nbit in (1, 2, 4, 8)},
            "f": {dtype_label(np.dtype(char)) for char in "efdg"},
            "c": {dtype_label(np.dtype(char)) for char in "FDG"},
        }
        seen_abstract: dict[str, list[np.dtype]] = {
            kind: [] for kind in unseen_abstract
        }

        extra_defaults: tuple[str, ...]  # irony
        if self.opname in {"lshift", "rshift", "and", "xor", "or"}:
            # 🐴
            extra_defaults = ()
        else:
            extra_defaults = "f8", "c16"

        dtypes_default = map(
            np.dtype,
            ("b1", "i1", "i2", "i4", "i8", "u1", "u2", "u4", "u8", *extra_defaults),
        )
        dtypes_op = *dtypes_default, *_get_op_types(self.opname)
        for dtype in sorted(dtypes_op, key=lambda dt: DTYPE_CHARS.index(dt.char)):
            label = dtype_label(dtype)
            if label in seen_dtypes:
                continue
            seen_dtypes.add(label)

            kind: str = dtype.kind
            if kind in "SU":
                kind = "w"
            if kind in unseen_abstract and label in unseen_abstract[kind]:
                unseen_abstract[kind].remove(label)
                seen_abstract[kind].append(dtype)

            self.dtypes[label] = (dtype,)

        for kindkind in "iu", "fc", "iufc":
            unseen_abstract[kindkind] = set()
            seen_abstract[kindkind] = []
            for kind in kindkind:
                unseen_abstract[kindkind] |= unseen_abstract[kind]
                seen_abstract[kindkind] += seen_abstract[kind]

        for kind, dtypes in seen_abstract.items():
            if unseen_abstract[kind]:
                continue

            assert dtypes
            assert kind not in self.dtypes

            self.dtypes[kind] = tuple(dtypes)

    def _get_arrays(
        self,
        dtype1: np.dtype,
        dtype2: np.dtype,
    ) -> tuple[npt.NDArray[Any], npt.NDArray[Any]]:
        arr1 = np.ones(self.shape, dtype=dtype1)
        arr2 = np.ones(self.shape, dtype=dtype2)

        if dtype1 != dtype2:
            # prefer compatible object_ arrays
            if dtype1.char == "O":
                arr1 = arr2.astype("O")
            if dtype2.char == "O":
                arr2 = arr1.astype("O")

        return arr1, arr2

    @overload
    def _op_expr(self, arg_expr: str, /) -> str: ...
    @overload
    def _op_expr(self, arg_expr_a: str, arg_expr_b: str, /) -> str: ...
    def _op_expr(self, /, *arg_exprs: str) -> str:
        return self.__op_expr_template.format(*arg_exprs)

    def _evaluate_unnop(self, arg: npt.ArrayLike, /) -> np.dtype | None:
        try:
            dtype: np.dtype = self.opfunc(arg).dtype
        except TypeError:
            return None

        return dtype

    def _evaluate_binop(
        self,
        lhs: npt.ArrayLike,
        rhs: npt.ArrayLike,
        /,
        reflect: bool = False,
    ) -> tuple[np.dtype, ...]:
        if reflect:
            lhs, rhs = rhs, lhs

        try:
            out = self.opfunc(lhs, rhs)
        except TypeError:
            return ()

        match out:
            case np.ndarray(dtype=dtype):
                return (dtype,)
            case (np.ndarray(dtype=dtype1), np.ndarray(dtype=dtype2)):
                return (dtype1, dtype2)
            case _:
                raise AssertionError(repr(out))

    def _gen_unop(self, /) -> Generator[str | None]:
        for label, dtypes in self.dtypes.items():
            out_dtypes: set[np.dtype] = set()
            for dtype in dtypes:
                arr = np.ones((1, 1), dtype=dtype)
                if (out_dtype := self._evaluate_unnop(arr)) is None:
                    out_dtypes.clear()
                    break
                out_dtypes.add(out_dtype)

            expr = self._op_expr(f"{label}_nd")
            if out_dtypes:
                out_type_expr = _array_expr_single(*out_dtypes, npt=True)
                yield _expr_assert_type(expr, out_type_expr)
            else:
                yield "  ".join((
                    expr,
                    f"# type: ignore[{self._mypy_rules}]",
                    f"# pyright: ignore[{self._pyright_rules}]",
                ))

    def _gen_testcases_binop_np_nd(self, label1: str, /) -> Generator[str | None]:
        name1 = f"{label1}_nd"
        dtypes1 = self.dtypes[label1]

        for label2, dtypes2 in self.dtypes.items():
            name2 = f"{label2}_nd"
            expr = self._op_expr(name1, name2)

            out_dtypes_set: set[tuple[np.dtype, ...]] = set()
            for dtype1, dtype2 in itertools.product(dtypes1, dtypes2):
                arr1, arr2 = self._get_arrays(dtype1, dtype2)

                if not (out_dtypes := self._evaluate_binop(arr1, arr2)):
                    out_dtypes_set.clear()
                    break
                out_dtypes_set.add(out_dtypes)

            if out_dtypes_set:
                out_type_expr = _array_expr(*out_dtypes_set, npt=True)
                yield _expr_assert_type(expr, out_type_expr)
            elif "O" not in {dtypes1[0].char, dtypes2[0].char}:  # impossible to reject
                # 🐴
                if (
                    self.opname == "truediv"
                    and label2 == "m8"
                    and label1[0] in "biu"
                    and label1 != "iufc"
                ):
                    mypy_rules = "type-var"
                else:
                    mypy_rules = self._mypy_rules

                yield "  ".join((
                    expr,
                    f"# type: ignore[{mypy_rules}]",
                    f"# pyright: ignore[{self._pyright_rules}]",
                ))

    def _gen_testcases_binop_py_0d(
        self,
        label_np: str,
        /,
        *,
        reflect: bool = False,
    ) -> Generator[str | None]:
        name_np = f"{label_np}_nd"
        dtypes_np = self.dtypes[label_np]

        for name_py, pytype in self._scalars_py.items():
            if reflect and pytype is bytes:
                # impossible to reject because of `ndarray.__buffer__`
                continue

            name1, name2 = (name_py, name_np) if reflect else (name_np, name_py)

            val_py: Any
            dtype_py, val_py = np.dtype(pytype), pytype(1)
            if self.opname == "matmul":
                for n in self.shape[::-1]:
                    val_py = [val_py] * n

            out_dtypes_set: set[tuple[np.dtype, ...]] = set()
            for dtype_np in dtypes_np:
                arr = self._get_arrays(dtype_np, dtype_py)[0]

                if not (out_dtypes := self._evaluate_binop(arr, val_py, reflect)):
                    out_dtypes_set.clear()
                    break
                out_dtypes_set.add(out_dtypes)

            expr = self._op_expr(name1, name2)

            if out_dtypes_set:
                out_type_expr = _array_expr(*out_dtypes_set, npt=True)
                testcase = _expr_assert_type(expr, out_type_expr)
            elif label_np == "O":
                # impossible to reject
                testcase = None
            elif (
                (
                    self.opname == "sub"
                    and label_np == "b1"
                    and name_py[0] == "b"
                )
                or (
                    self.opname in {"floordiv", "mod", "divmod"}
                    and label_np == "c16"
                    and name_py[0] in "if"
                )
            ):  # fmt: skip
                testcase = "  ".join((
                    expr,
                    "# 🐴",
                    f"# pyright: ignore[{self._pyright_rules}]",
                ))
            else:
                testcase = "  ".join((
                    expr,
                    f"# type: ignore[{self._mypy_rules}]",
                    f"# pyright: ignore[{self._pyright_rules}]",
                ))

            yield testcase

    def _gen_binop(self, /) -> Generator[str | None]:
        for label in self.dtypes:
            yield from self._gen_testcases_binop_np_nd(label)
            yield ""
            yield from self._gen_testcases_binop_py_0d(label)
            yield ""
            yield from self._gen_testcases_binop_py_0d(label, reflect=True)
            yield ""

    @override
    def get_names(self) -> Iterable[tuple[str, str]]:
        # ndarays
        for label, dtypes in self.dtypes.items():
            if len(dtypes) == 1:
                array_expr = _array_expr_single(dtypes[0], npt=True)
            else:
                array_expr = f"npt.NDArray[{self._abstract_expr(label)}]"

            yield f"{label}_nd", array_expr

        if self.n_in == 1:
            return

        # linebreak
        yield "", ""

        # builtin types
        py_template = "list[list[{}]]" if self.opname == "matmul" else "{}"
        for name, pytype in self._scalars_py.items():
            yield name, py_template.format(pytype.__name__)

    @override
    def get_testcases(self) -> Iterable[str | None]:
        yield from self._generate_section()
        if self.n_out == 2:
            yield ""
            yield from self._generate_section()

        yield from self._gen_unop() if self.n_in == 1 else self._gen_binop()


TESTGENS: Final[Sequence[TestGen]] = [
    EMath(binary=False),
    LiteralBoolOps(),
    ScalarOps("arithmetic"),
    ScalarOps("modular"),
    ScalarOps("bitwise"),
    ScalarOps("comparison"),
    NDArrayOps("pos"),
    NDArrayOps("neg"),
    NDArrayOps("abs"),
    NDArrayOps("invert"),
    NDArrayOps("add"),
    NDArrayOps("sub"),
    NDArrayOps("mul"),
    NDArrayOps("matmul"),
    NDArrayOps("pow"),
    NDArrayOps("truediv"),
    NDArrayOps("floordiv"),
    NDArrayOps("mod"),
    NDArrayOps("divmod"),
    NDArrayOps("lshift"),
    NDArrayOps("rshift"),
    # NDArrayOps("and"),
    # NDArrayOps("xor"),
    # NDArrayOps("or"),
]


@np.errstate(all="ignore")
def main() -> None:
    """(Re)generate the `src/numpy-stubs/@test/generated/{}.pyi` type-tests."""
    for testgen in TESTGENS:
        sys.stdout.writelines(testgen.regenerate())


if __name__ == "__main__":
    main()
