# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numtype[numpy]",
#     "tabulate",
# ]
#
# [tool.uv.sources]
# numtype = {path = ".."}
# ///

"""
UFunc introspection tools.

Usage: uv run tool/ufunc.py [-h] [-p] [-f <TABULATE_FORMAT>] <NIN> <NOUT>
"""

import argparse
import itertools
import sys
from collections.abc import Sequence
from functools import cache
from typing import TYPE_CHECKING, Any, Final, TypeAlias

if TYPE_CHECKING:
    import _numtype as _nt

import numpy as np
import numpy._core.umath as um  # noqa: PLC2701

_ScalarLike: TypeAlias = np.generic | np.ndarray["_nt.Shape0", np.dtype]

_EXTRA_SCALARS: Final[tuple[_ScalarLike, ...]] = (
    np.str_(""),
    np.array("", dtype="T"),
    np.bytes_(b""),
    np.void(b""),
)


@cache
def _qualname(u: np.ufunc, /) -> str:
    name = u.__name__
    if hasattr(u, "__module__"):
        return f"{u.__module__}.{name}"
    if hasattr(np, name) and isinstance(getattr(np, name), np.ufunc):
        return f"numpy.{name}"
    if hasattr(np.strings, name) and isinstance(getattr(np.strings, name), np.ufunc):
        return f"numpy.strings.{name}"
    if hasattr(np.linalg._umath_linalg, name):  # noqa: SLF001
        return f"numpy.linalg._umath_linalg.{name}"
    if hasattr(um, name):
        return f"numpy._core.umath.{name}"
    raise NameError(u.__name__)


@cache
def _all_types(u: np.ufunc) -> tuple[str, ...]:
    """Return all supported ufunc type signatures, including unlisted `'SUVT'` ones.

    Returns
    -------
    extra_types : tuple of string-like type signatures like "ab->c"
    """
    extra_types: list[str] = []

    # ugly workaround for weird string ufuncs in `_core.umath`
    prod_args = [_EXTRA_SCALARS] * u.nin
    if u.nin > 1 and not u.types and _qualname(u).startswith("numpy._"):
        prod_args = [
            (np.longlong(0), np.longlong(1), *_EXTRA_SCALARS),
        ] * u.nin

    for args in itertools.product(*prod_args):
        try:
            vouts = u(*args)
        except (ValueError, TypeError):
            continue

        tin = "".join(v.dtype.char for v in args)

        tout = ""
        if u.nout == 1:
            vouts = (vouts,)
        for vout in vouts:
            if type(vout) is str:
                tout += "T"
            else:
                char = vout.dtype.char
                # avoid system dependent return types for `NPY_DEFAULT_INT`
                tout += "n" if char == np.dtype("n").char else char

        extra_types.append(f"{tin}->{tout}")

    return tuple(dict.fromkeys(u.types + extra_types))


def _unzip_types(
    u: np.ufunc,
    /,
    *,
    unique: bool = False,
) -> tuple[tuple[list[str], ...], tuple[list[str], ...]]:
    tinss: tuple[list[str], ...] = tuple([] for _ in range(u.nin))
    toutss: tuple[list[str], ...] = tuple([] for _ in range(u.nout))

    for t in dict.fromkeys(_all_types(u)):
        for targss, targs_str in zip((tinss, toutss), t.split("->"), strict=True):
            for targs, targ in zip(targss, targs_str, strict=True):
                targs.append(targ)

    if unique:
        tinss = tuple(list(dict.fromkeys(tins)) for tins in tinss)
        toutss = tuple(list(dict.fromkeys(touts)) for touts in toutss)

    return tinss, toutss


def _ufunc_list(
    *,
    nin: int | None = None,
    nout: int | None = None,
    private: bool = False,
) -> list[dict[str, str]]:
    def _sort_key(ufunc: np.ufunc, /) -> tuple[Any, ...]:
        tins, touts = _unzip_types(ufunc, unique=True)
        return (
            _qualname(ufunc).count("."),
            _qualname(ufunc).split(".", 1)[0],
            ufunc.nin,
            ufunc.nout,
            tuple(map(len, touts)),
            tuple(map(len, tins)),
            "".join(_all_types(ufunc)),
            _qualname(ufunc),
        )

    out: list[dict[str, str]] = []
    for u in sorted(np.testing.overrides.get_overridable_numpy_ufuncs(), key=_sort_key):
        if nin is not None and u.nin != nin:
            continue
        if nout is not None and u.nout != nout:
            continue
        if not private and u.__name__.startswith("_"):
            continue

        out.append(entry := {"name": _qualname(u).replace("numpy.", "")})

        for param, n, targss in zip(
            ("arg", "out"),
            (nin, nout),
            _unzip_types(u, unique=True),
            strict=True,
        ):
            if n is not None and len(targss) == 1:
                entry[param] = "".join(targss[0])
            else:
                for i, targs in enumerate(targss):
                    entry[f"{param}{i}"] = (
                        "".join(targs).replace("Tq", "qT").replace("TU", "UT")
                    )

    return out


def _parse_args(args: Sequence[str] | None, /) -> argparse.Namespace:
    import tabulate  # pyright: ignore[reportMissingModuleSource]  # noqa: PLC0415

    parser = argparse.ArgumentParser(prog="ufunc.py")

    parser.add_argument("nin", type=int, help="filter by `ufunc.nin`")
    parser.add_argument("nout", type=int, help="filter by `ufunc.nout")
    parser.add_argument(
        "-p",
        "--private",
        action="store_true",
        required=False,
        help="show private ufuncs",
    )
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=sorted(tabulate.tabulate_formats),
        default="github",
        help="output table format",
    )

    return parser.parse_args(args)


def main(args: Sequence[str] | None = None, /) -> int:
    """
    Run it.

    Returns
    -------
    exit_code : int
    """
    namespace = _parse_args(args)

    data = _ufunc_list(
        nin=namespace.nin,
        nout=namespace.nout,
        private=namespace.private,
    )

    match namespace.format:
        case "github":
            as_code = "`{}`".format
        case "rst":
            as_code = "``{}``".format
        case _:
            as_code = "{}".format

    if data:
        import tabulate  # pyright: ignore[reportMissingModuleSource]  # noqa: PLC0415

        print(
            tabulate.tabulate(
                [list(map(as_code, entry.values())) for entry in data],
                headers=[as_code("ufunc"), *list(map(as_code, data[0]))[1:]],
                tablefmt=namespace.format,
            )
            # needed for consistent ordering of string-like types
            .replace("TS", "ST")
            .replace("TV", "VT")
            .replace("US", "SU"),
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
