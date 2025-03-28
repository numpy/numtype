import errno
import sys
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest

tool_path = str(Path(__file__).parent.parent.parent)
if tool_path not in sys.path:
    sys.path.insert(0, tool_path)

from tool.format_ignores import (  # noqa: E402
    _process_directory,  # noqa: PLC2701
    _process_file,  # noqa: PLC2701
    _sort_ignore_list,  # noqa: PLC2701
    main,
)


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Temporary directory for testing

    Yields:
        Path: The path to the temporary directory.
    """
    with tempfile.TemporaryDirectory() as temp_dir_path:
        yield Path(temp_dir_path)


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
    """Test _sort_ignore_list function"""
    result = _sort_ignore_list(input_text)
    assert result == expected_output


def test_process_file(temp_dir: Path) -> None:
    """Test _process_file function"""
    test_file = temp_dir / "test.pyi"
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


def test_process_directory(temp_dir: Path) -> None:
    """Test _process_directory function"""
    # Create directory structure
    (temp_dir / "subdir").mkdir()
    (temp_dir / ".hidden_dir").mkdir()

    # Create test files
    test_files = [
        temp_dir / "test1.pyi",  # Already formatted
        temp_dir / "test2.pyi",  # Already formatted
        temp_dir / "subdir" / "test3.pyi",  # Needs formatting
        temp_dir / ".hidden_dir" / "test4.pyi",  # In hidden dir
        temp_dir / "test5.py",  # Wrong extension
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
    assert modified == 1  # Only test3.pyi needs modification
    assert total == 3  # Three files checked

    # Processing mode
    modified, total = _process_directory(temp_dir, glob_pattern="**/*.pyi")
    assert modified == 1
    assert total == 3

    # Verify results
    assert (
        test_files[0].read_text(encoding="utf-8")
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


def test_main_success(temp_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test main function with valid path"""
    test_file = temp_dir / "test.pyi"
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


def test_main_check_mode(temp_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test main function in check-only mode"""
    test_file = temp_dir / "test.pyi"
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
    """Test main function with non-existent path"""
    non_existent_path = "/non/existent/path"
    monkeypatch.setattr(sys, "argv", ["format_ignores.py", non_existent_path])

    exit_code = main()
    assert exit_code == errno.ENOENT  # Path not found


def test_main_custom_pattern(temp_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test main function with custom pattern"""
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
