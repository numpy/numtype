# NumType testing

## basedmypy

Mypy and basedmypy will only recognize the `src/numpy-stubs` if `numtype` is installed in an
isolated project, and it cannot be editable.

The `mypy.py` script creates an isolated environment, that doesn't include numpy, and will run
basedmypy. If no paths are provided, it will default to `--explicit-package-bases test`.

```bash
uv run test/mypy.py [OPTIONS]
```

## basedpyright

Unlike mypy, no additional project isolation trickery is required, so it can be run directly
from the main project:

```bash
uv run basedpyright [OPTIONS]
```

## pytest

Pytest also works out-of-the box, and will, by default, run the tests in `test/runtime`:

```bash
uv run pytest [OPTIONS]
```
