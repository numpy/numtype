"""List local numpy-stubs that are older than NumPy."""

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

UPSTREAM_URL = "https://github.com/numpy/numpy.git"
UPSTREAM_BRANCH = "maintenance/2.4.x"
LOCAL_STUBS_ROOT = Path(__file__).resolve().parents[1] / "src" / "numpy-stubs"
GIT_BIN = shutil.which("git") or "git"


def _run_git(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(
        [GIT_BIN, *args], cwd=cwd, check=False, capture_output=True, text=True
    )
    proc.check_returncode()
    return proc.stdout.strip()


def _latest_commit_ts(repo: Path, path: Path) -> int | None:
    rel = path.relative_to(repo)
    out = _run_git(["log", "-1", "--format=%ct", "--", str(rel)], cwd=repo)
    return int(out)


def _list_outdated(local_repo: Path, upstream_repo: Path) -> list[str]:
    outdated: list[str] = []
    for local_file in LOCAL_STUBS_ROOT.rglob("*.pyi"):
        rel = local_file.relative_to(LOCAL_STUBS_ROOT)
        upstream_file = upstream_repo / "numpy" / rel
        if not upstream_file.exists():
            continue

        ts_local = _latest_commit_ts(local_repo, local_file)
        ts_upstream = _latest_commit_ts(upstream_repo, upstream_file)
        if ts_upstream is None:
            continue

        if ts_local is None or ts_upstream > ts_local:
            if local_file.read_bytes() == upstream_file.read_bytes():
                continue
            outdated.append(str(rel))

    return sorted(outdated)


def _main() -> int:
    local_repo = Path(__file__).resolve().parents[1]
    if not LOCAL_STUBS_ROOT.is_dir():
        print(f"Local stubs not found at {LOCAL_STUBS_ROOT}", file=sys.stderr)
        return 2

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        print(f"Cloning upstream {UPSTREAM_BRANCH}...", file=sys.stderr)
        _run_git(
            [
                "clone",
                "--depth=1",
                "--branch",
                UPSTREAM_BRANCH,
                UPSTREAM_URL,
                str(tmp_path),
            ],
            cwd=tmp_path,
        )
        outdated = _list_outdated(local_repo, tmp_path)

    if outdated:
        print("Upstream is newer for:")
        for rel in outdated:
            print(f"https://github.com/numpy/numpy/blob/{UPSTREAM_BRANCH}/numpy/{rel}")
    else:
        print("All tracked stubs are up-to-date relative to upstream.")

    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
