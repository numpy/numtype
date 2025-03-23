# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "numtype[numpy]",
# ]
#
# [tool.uv.sources]
# numtype = {path = ".."}
# ///

"""Format pyright ignore comments with proper sorting and spacing.

Ensures that pyright ignore comments in Python files have their entries sorted
alphabetically and formatted with proper spacing between items.

Usage: uv run tool/format_ignores.py [-h] [--extensions EXTENSIONS] [--check] [PATH]
"""

import argparse
import os
import re
import sys
from collections.abc import Iterable, Sequence
from pathlib import Path


def _sort_ignore_list(ignore_text: str, /) -> str:
    """
    Sort the items in a pyright ignore list and ensure proper spacing.

    Parameters
    ----------
    ignore_text : str
        Text inside the ignore brackets

    Returns
    -------
    str
        Sorted and formatted ignore list
    """
    # Extract items from the ignore list
    items = ignore_text.strip("[]").split(",")

    # Clean up each item and sort
    cleaned_items = [item.strip() for item in items if item.strip()]
    sorted_items = sorted(cleaned_items)

    # Join with comma and space
    return ", ".join(sorted_items)


def _process_file(
    file_path: str | os.PathLike[str],
    /,
    *,
    check_only: bool = False,
) -> bool:
    """
    Process a file to sort pyright ignore comments.

    Parameters
    ----------
    file_path : str or os.PathLike[str]
        Path to the file to process
    check_only : bool, default=False
        If True, don't modify the file, just check if changes are needed

    Returns
    -------
    bool
        True if the file was modified or would be modified (in check mode)
    """
    path_obj = Path(file_path)
    content = path_obj.read_text(encoding="utf-8")

    # Find all pyright ignore comments and sort them
    pattern = r"(# pyright: ignore\[)([^\]]+)(\])"

    def replace_match(match: re.Match[str], /) -> str:
        prefix = match.group(1)
        ignore_list = match.group(2)
        suffix = match.group(3)
        sorted_ignore = _sort_ignore_list(ignore_list)
        return f"{prefix}{sorted_ignore}{suffix}"

    updated_content = re.sub(pattern, replace_match, content)

    # Check if changes would be made
    needs_changes = content != updated_content

    # Write the updated content back if changes were made and not in check mode
    if needs_changes and not check_only:
        path_obj.write_text(updated_content, encoding="utf-8")
        print(f"Updated {file_path}")

    return needs_changes


def _process_directory(
    directory_path: str | os.PathLike[str],
    /,
    *,
    extensions: Iterable[str] = (".pyi",),
    check_only: bool = False,
) -> tuple[int, int]:
    """
    Process all files with the given extensions in a directory and its subdirectories.

    Parameters
    ----------
    directory_path : str or os.PathLike[str]
        The path to the directory to process
    extensions : iterable of str, default=('.pyi',)
        File extensions to process
    check_only : bool, default=False
        If True, don't modify files, just check them

    Returns
    -------
    tuple of (int, int)
        (count of files that would be modified, total files checked)
    """
    modified_count = 0
    total_count = 0

    dir_path = Path(str(directory_path))

    for ext in extensions:
        for path in dir_path.rglob(f"*{ext}"):
            total_count += 1
            if _process_file(path, check_only=check_only):
                modified_count += 1
                if check_only:
                    print(f"Would update {path}")

    return modified_count, total_count


def _parse_args(args: Sequence[str] | None = None, /) -> argparse.Namespace:
    """
    Parse command line arguments.

    Parameters
    ----------
    args : sequence of str, optional
        Command line arguments to parse. Defaults to sys.argv[1:].

    Returns
    -------
    argparse.Namespace
        Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Format pyright ignore comments in Python files.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to file or directory to process (default: current directory)",
    )
    parser.add_argument(
        "--extensions",
        default=".pyi",
        help="Comma-separated list of file extensions to process (default: .pyi)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check files without modifying them, exit with error if files "
        "would be modified",
    )

    return parser.parse_args(args)


def main(args: Sequence[str] | None = None, /) -> int:
    """
    Run the formatter.

    Parameters
    ----------
    args : sequence of str, optional
        Command line arguments to parse. Defaults to sys.argv[1:].

    Returns
    -------
    int
        Exit code: 0 for success, 1 for error or (in check mode) if files would
        be modified
    """
    namespace = _parse_args(args)
    extensions = tuple(ext.strip() for ext in namespace.extensions.split(","))

    path = namespace.path
    check_only = namespace.check
    path_obj = Path(path)

    if path_obj.is_dir():
        modified, total = _process_directory(
            path,
            extensions=extensions,
            check_only=check_only,
        )
        if check_only:
            print(
                f"Found {modified} files that would be modified out of {total} checked",
            )
            return 1 if modified > 0 else 0
        print(f"Updated {modified} files out of {total} checked")
        return 0
    if path_obj.is_file():
        modified = _process_file(path, check_only=check_only)
        if check_only:
            if modified:
                print(f"File {path} would be modified")
                return 1
            print(f"File {path} is correctly formatted")
            return 0
        return 0
    print(f"Path not found: {path}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
