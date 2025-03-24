"""Format pyright ignore comments with proper sorting and spacing.

Ensures that pyright ignore comments in Python files have their entries sorted
alphabetically and formatted with proper spacing between items.

Usage: uv run tool/format_ignores.py [-h] [--pattern PATTERN] [--check] [PATH]
"""

import argparse
import errno
import os
import re
import sys
from collections.abc import Sequence
from pathlib import Path

combined_pattern = re.compile(r"(\s*#\s*(pyright|type):\s*ignore\[)([^\]]+)(\])")


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
    return ", ".join(sorted(set(filter(bool, map(str.strip, ignore_text.split(","))))))


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

    # Process both pyright and mypy ignore comments
    def replace_match(match: re.Match[str], /) -> str:
        prefix = match.group(1)
        # group(2) contains either "pyright" or "type", which we don't need separately
        ignore_list = match.group(3)
        suffix = match.group(4)
        sorted_ignore = _sort_ignore_list(ignore_list)
        return f"{prefix}{sorted_ignore}{suffix}"

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
        description="Format pyright ignore comments in Python files.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to file or directory to process (default: current directory)",
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
    path = namespace.path
    check_only = namespace.check
    glob_pattern = namespace.pattern
    path_obj = Path(path)

    if path_obj.is_dir():
        modified, total = _process_directory(
            path,
            glob_pattern=glob_pattern,
            check_only=check_only,
        )
        if check_only:
            print(
                f"Found {modified} files that would be modified out of {total} checked",
            )
            return errno.EAGAIN if modified > 0 else 0
        print(f"Updated {modified} files out of {total} checked")
        return 0
    if path_obj.is_file():
        modified = _process_file(path, check_only=check_only)
        if check_only:
            if modified:
                print(f"File {path} would be modified")
                return errno.EAGAIN
            print(f"File {path} is correctly formatted")
            return 0
        return 0
    print(f"Path not found: {path}", file=sys.stderr)
    return errno.ENOENT


if __name__ == "__main__":
    sys.exit(main())
