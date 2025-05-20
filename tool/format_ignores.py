"""Format `(type|pyright): ignore[...]` comments with proper sorting and spacing.

Ensures that `(type|pyright): ignore[...]` comments in Python files have their entries
sorted alphabetically and formatted with proper spacing between items.

Usage: uv run tool/format_ignores.py [-h] [--pattern PATTERN] [--check] [PATH...]
"""

import argparse
import errno
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

combined_pattern = re.compile(r"(\s*#\s*)(pyright|type)(\s*:\s*ignore\[)([^\]]+)(\])")


def _sort_ignore_list(ignore_text: str, /) -> str:
    """
    Sort the items in a `(type|pyright): ignore[...]` list and ensure proper spacing.

    Parameters
    ----------
    ignore_text : str
        Text inside the ignore brackets

    Returns
    -------
    str
        Sorted and formatted ignore list
    """
    items = filter(bool, map(str.strip, ignore_text.split(",")))
    sorted_items = sorted(set(items))
    return ", ".join(sorted_items)


def _process_file(
    file_path: str | os.PathLike[str], /, *, check_only: bool = False
) -> bool:
    """
    Process a file to sort `(type|pyright): ignore[...]` comments.

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

    # Process both pyright and mypy ignore comments
    def replace_match(match: re.Match[str], /) -> str:
        prefix = match.group(1)  # Whitespace and '#'
        type_or_pyright = match.group(2)  # "pyright" or "type"
        match.group(3)  # ":" and any surrounding whitespace plus "ignore["
        ignore_list = match.group(4)  # The content inside the brackets
        suffix = match.group(5)  # The closing bracket "]"
        sorted_ignore = _sort_ignore_list(ignore_list)
        return f"{prefix}{type_or_pyright}: ignore[{sorted_ignore}{suffix}"

    updated_content = combined_pattern.sub(replace_match, content)

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
    glob_pattern: str = "**/*.pyi",
    check_only: bool = False,
) -> tuple[int, int]:
    """
    Process all files matching the glob pattern in a directory and its subdirectories.

    Parameters
    ----------
    directory_path : str or os.PathLike[str]
        The path to the directory to process
    glob_pattern : str, default='**/*.pyi'
        Glob pattern to match files
    check_only : bool, default=False
        If True, don't modify files, just check them

    Returns
    -------
    tuple of (int, int)
        (count of files that would be modified, total files checked)
    """
    modified_count = 0
    total_count = 0

    dir_path = Path(directory_path)

    # Walk the directory tree manually to avoid hidden directories
    for root, dirs, files in os.walk(dir_path):
        # Skip directories that start with a dot
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        # Extract the file extension from the pattern
        if "*." not in glob_pattern:
            continue

        ext = glob_pattern.split("*.", 1)[1]
        root_path = Path(root)

        # Process matching files in the current directory
        for file in files:
            if not file.endswith(f".{ext}"):
                continue

            file_path = root_path / file
            total_count += 1
            if _process_file(file_path, check_only=check_only):
                modified_count += 1
                if check_only:
                    print(f"Would update {file_path}")

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
        description="Format `(type|pyright): ignore[...]` comments in Python files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="Path(s) to file or directory to process (default: current directory)",
    )
    parser.add_argument(
        "--pattern",
        default="**/*.pyi",
        help="Glob pattern to match files (default: **/*.pyi)",
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
        Exit code:
        - 0: Success
        - errno.EAGAIN: Files would be modified (in check mode)
        - errno.ENOENT: Path not found
    """
    namespace = _parse_args(args)
    paths = namespace.paths
    check_only = namespace.check
    glob_pattern = namespace.pattern

    total_modified = 0
    total_files = 0
    total_failures = 0

    for path in paths:
        path_obj = Path(path)

        if path_obj.is_dir():
            modified, checked = _process_directory(
                path, glob_pattern=glob_pattern, check_only=check_only
            )
            total_modified += modified
            total_files += checked
        elif path_obj.is_file():
            total_files += 1
            if _process_file(path, check_only=check_only):
                total_modified += 1
                if check_only:
                    print(f"File {path} would be modified")
        else:
            print(f"Path not found: {path}", file=sys.stderr)
            total_failures += 1

    if total_failures > 0 and len(paths) == total_failures:
        return errno.ENOENT

    if check_only and total_files > 0:
        print(
            f"Found {total_modified} files that would be modified "
            f"out of {total_files} checked"
        )
        return errno.EAGAIN if total_modified > 0 else 0

    if total_files > 0:
        print(f"Updated {total_modified} files out of {total_files} checked")

    return 0


if __name__ == "__main__":
    sys.exit(main())
