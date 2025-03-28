"""Test the format_ignores module."""

# ruff: noqa: PLC2701
import errno
import sys
from pathlib import Path

import pytest

from tool.format_ignores import (
    _process_directory,
    _process_file,
    _sort_ignore_list,
    main,
)


@pytest.mark.parametrize(
    ("input_text", "expected_output"),
    [
        ("error1, error2", "error1, error2"),
        ("error2, error1", "error1, error2"),
        ("error1,error2", "error1, error2"),
        ("error1,  error2", "error1, error2"),
        ("error1, error1, error2", "error1, error2"),
        ("", ""),
        (" , error1, ,error2, ", "error1, error2"),
    ],
)
def test_sort_ignore_list(input_text: str, expected_output: str) -> None:
    """Test _sort_ignore_list function."""
    result = _sort_ignore_list(input_text)
    assert result == expected_output


def test_process_file(tmpdir: pytest.TempdirFactory) -> None:
    """Test _process_file function."""
    test_file = Path(str(tmpdir)) / "test.pyi"
    test_content = """def func1() -> None:
    # type: ignore[attr-defined, no-any-return]
    pass

    def func2() -> None:
        # pyright: ignore[reportUnknownMemberType,reportUnknownVariableType]
        pass
    """
    test_file.write_text(test_content, encoding="utf-8")

    # Check-only mode
    modified = _process_file(test_file, check_only=True)
    assert modified is True
    assert test_file.read_text(encoding="utf-8") == test_content

    # Processing mode
    modified = _process_file(test_file)
    assert modified is True

    expected_content = """def func1() -> None:
    # type: ignore[attr-defined, no-any-return]
    pass

    def func2() -> None:
        # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
        pass
    """
    assert test_file.read_text(encoding="utf-8") == expected_content

    # Re-processing
    modified = _process_file(test_file)
    assert modified is False


def test_process_directory(tmpdir: pytest.TempdirFactory) -> None:
    """Test _process_directory function."""
    temp_dir = Path(str(tmpdir))
    # Create directory structure
    (temp_dir / "subdir").mkdir()
    (temp_dir / ".hidden_dir").mkdir()

    # Create test files
    test_files = [
        temp_dir / "test1_formatted.pyi",
        temp_dir / "test2_formatted.pyi",
        temp_dir / "subdir" / "test3_unformatted.pyi",
        temp_dir / ".hidden_dir" / "test4_hidden.pyi",
        temp_dir / "test5_wrong_extension.py",
    ]

    test_files[0].write_text(
        "# type: ignore[attr-defined, no-any-return]",
        encoding="utf-8",
    )
    test_files[1].write_text(
        "# type: ignore[attr-defined, no-any-return]",
        encoding="utf-8",
    )
    test_files[2].write_text(
        "# pyright: ignore[reportUnknownVariableType,reportUnknownMemberType]",
        encoding="utf-8",
    )
    test_files[3].write_text(
        "# type: ignore[no-any-return, attr-defined]",
        encoding="utf-8",
    )
    test_files[4].write_text(
        "# type: ignore[no-any-return, attr-defined]",
        encoding="utf-8",
    )

    # Check-only mode
    modified, total = _process_directory(
        temp_dir,
        glob_pattern="**/*.pyi",
        check_only=True,
    )
    correct_total = 3

    assert modified == 1  # Only test3.pyi needs modification
    assert total == correct_total

    # Processing mode
    modified, total = _process_directory(temp_dir, glob_pattern="**/*.pyi")
    assert modified == 1
    assert total == correct_total

    # Verify results
    assert (
        test_files[0].read_text(encoding="utf-8")
        == "# type: ignore[attr-defined, no-any-return]"
    )
    assert (
        test_files[1].read_text(encoding="utf-8")
        == "# type: ignore[attr-defined, no-any-return]"
    )
    assert (
        test_files[2].read_text(encoding="utf-8")
        == "# pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]"
    )
    assert (
        test_files[3].read_text(encoding="utf-8")
        == "# type: ignore[no-any-return, attr-defined]"
    )
    assert (
        test_files[4].read_text(encoding="utf-8")
        == "# type: ignore[no-any-return, attr-defined]"
    )


def test_main_success(
    tmpdir: pytest.TempdirFactory,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test main function with valid path."""
    test_file = Path(str(tmpdir)) / "test.pyi"
    test_file.write_text(
        "# type: ignore[no-any-return, attr-defined]",
        encoding="utf-8",
    )

    monkeypatch.setattr(sys, "argv", ["format_ignores.py", str(test_file)])

    exit_code = main()
    assert exit_code == 0

    assert (
        test_file.read_text(encoding="utf-8")
        == "# type: ignore[attr-defined, no-any-return]"
    )


def test_main_check_mode(
    tmpdir: pytest.TempdirFactory,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test main function in check-only mode."""
    test_file = Path(str(tmpdir)) / "test.pyi"
    test_file.write_text(
        "# type: ignore[no-any-return, attr-defined]",
        encoding="utf-8",
    )

    monkeypatch.setattr(sys, "argv", ["format_ignores.py", "--check", str(test_file)])

    exit_code = main()
    assert exit_code == errno.EAGAIN  # Changes needed

    assert (
        test_file.read_text(encoding="utf-8")
        == "# type: ignore[no-any-return, attr-defined]"
    )


def test_main_path_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test main function with non-existent path."""
    non_existent_path = "/non/existent/path"
    monkeypatch.setattr(sys, "argv", ["format_ignores.py", non_existent_path])

    exit_code = main()
    assert exit_code == errno.ENOENT  # Path not found


def test_main_custom_pattern(
    tmpdir: pytest.TempdirFactory,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test main function with custom pattern."""
    temp_dir = Path(str(tmpdir))
    test_py = temp_dir / "test.py"
    test_py.write_text("# type: ignore[no-any-return, attr-defined]", encoding="utf-8")

    monkeypatch.setattr(
        sys,
        "argv",
        ["format_ignores.py", "--pattern", "**/*.py", str(temp_dir)],
    )

    exit_code = main()
    assert exit_code == 0

    assert (
        test_py.read_text(encoding="utf-8")
        == "# type: ignore[attr-defined, no-any-return]"
    )
