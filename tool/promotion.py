"""
Displays the scsalar promotion rules as a Github markdown table.

Usage: uv run tool/promotion.py [table|graph] <CHARS="?bBhHiIlLqQefdgFDGOSTUVMm">
"""

import argparse
import functools
import sys
from collections.abc import Sequence
from graphlib import TopologicalSorter
from typing import TypeAlias

import numpy as np
import numpy.typing as npt

_ToScalar: TypeAlias = complex | bytes | str | np.generic
_ToScalarType: TypeAlias = type[_ToScalar]

CHARS = "?bBhHiIlLqQefdgFDGOSTUVMm"
CHARS_CO = "mO"
CHARS_CONTRA = ""


@functools.cache
def _types_to(chars: str, /) -> tuple[type[np.generic], ...]:
    return tuple(dict.fromkeys(np.dtype(char).type for char in chars))


@functools.cache
def _types_co(chars: str, /) -> tuple[_ToScalarType, ...]:
    return tuple(
        type_in
        for type_in in _types_to(chars)
        if np.dtype(type_in).char not in CHARS_CO
    )


def _promotes_to(sct: npt.DTypeLike | None) -> tuple[_ToScalarType, ...]:
    out: list[_ToScalarType] = []
    for t in (bool, int, float, complex, str, bytes, *np.sctypeDict.values()):
        try:
            dt = np.result_type(sct, t)
        except (ValueError, TypeError):
            continue
        if np.dtype(dt) == sct:
            out.append(t)
    return tuple(dict.fromkeys(out))


def _typename(sct: npt.DTypeLike | None) -> str:
    if sct is None:
        return "None"
    if sct is str and "T" in CHARS:
        return "T"
    if sct in {bool, int, float, complex, bytes, str}:
        assert isinstance(sct, type)
        return sct.__name__

    dt = np.dtype(sct)
    if (kind := dt.kind) in "OSTUV":
        return kind

    if dt.char in "gG":
        return f"{kind}ld"
    return f"{kind}{dt.itemsize}"


def _comap(chars: str) -> dict[str, dict[str, str]]:
    typemap: dict[type, set[type]] = {}
    for sct in _types_to(chars):
        if np.dtype(sct).char not in CHARS_CONTRA:
            typemap[sct] = set(_promotes_to(sct))

    table: dict[str, dict[str, str]] = {}
    for t, subt in typemap.items():
        table["T" if t is str else _typename(t)] = {
            _typename(s): "^" if s in subt else " " for s in _types_co(chars)
        }

    return table


def _as_table(chars: str = CHARS, /) -> str:
    """
    Render the promotion rules as a github markdown table.

    Returns
    -------
    output : str
    """
    data = _comap(chars)

    row_keys = list(next(iter(_comap(chars).values())))
    col_keys = list(data)

    rows_width = max(3, *map(len, row_keys))
    cols_width = max(3, *map(len, col_keys))
    col0_width = rows_width + 2
    cell_width = cols_width + 2

    tbody_tr: dict[str, list[str]] = {k: [] for k in row_keys}
    for col in data.values():
        for th, td in col.items():
            tbody_tr[th].append(td.center(cell_width))

    head_sep = f":{'-' * (cols_width)}:"
    return "\n".join([
        "|".join([
            "",
            " " * col0_width,
            *(f" {col: <{cols_width}} " for col in col_keys),
            "",
        ]),
        "|".join(["", "-" * col0_width, *([head_sep] * len(col_keys)), ""]),
        *[
            "|".join(["", f" {name: <{rows_width}} ", *cell, ""])
            for name, cell in tbody_tr.items()
        ],
    ])


def _as_graph(chars: str = CHARS, /) -> str:  # noqa: C901, PLR0912
    """
    Render the promotion rules as a mermaid flowchart.

    Returns
    -------
    output : str
    """
    graph: dict[str, set[str]] = {}
    for char_co in chars:
        if char_co in CHARS_CONTRA:
            continue

        name_co = _typename(char_co)
        names_contra: set[str] = set()
        for char_contra in chars:
            name_contra = _typename(char_contra)
            if name_contra == name_co:
                continue

            try:
                dtype = np.result_type(char_contra, char_co)
            except np.exceptions.DTypePromotionError:
                continue

            if _typename(dtype) == name_co:
                names_contra.add(name_contra)

        if names_contra:
            graph[name_co] = names_contra

    ts = TopologicalSorter(graph)
    nodes_sorted = tuple(ts.static_order())

    # dedupe edges
    for contra in nodes_sorted:
        co_out: set[str] = set()

        for other in nodes_sorted:
            if other == contra or other not in graph:
                continue

            co_in = graph[other]
            if contra not in co_in:
                continue

            if co_out & co_in:
                graph[other].remove(contra)

            co_out.add(other)

    # draw the graph
    lines = ["flowchart BT"]
    for node in nodes_sorted:
        if node not in graph:
            continue
        sources = graph[node]
        source = " & ".join(sorted(sources, key=nodes_sorted.index))
        lines.append(f"    {source}-->{node}")

    return "\n".join(lines)


def _parse_args(args: Sequence[str] | None, /) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="promotion.py")

    parser.add_argument(
        "format",
        nargs="?",
        choices=["table", "graph"],
        default="table",
        help="display format",
    )
    parser.add_argument("-d", "--dtypes", type=str, default=CHARS, help="dtype chars")

    return parser.parse_args(args)


def main(args: Sequence[str] | None = None, /) -> int:
    """
    Run it.

    Returns
    -------
    exit_code : int
    """
    namespace = _parse_args(args)

    if namespace.format == "table":
        print(_as_table(namespace.dtypes))
    elif namespace.format == "graph":
        print(_as_graph(namespace.dtypes))
    else:
        print(f"unknown format: {namespace.format!r}")
        return -1
    return 0


if __name__ == "__main__":
    sys.exit(main())
