# NumType's Contributing guidelines

Welcome to the NumPy community! We're excited to have you here. Whether
you're new to open source or experienced, your contributions help us
grow.

Pull requests (PRs) are always welcome, but making a PR is just the
start. Please respond to comments and requests for changes to help move
the process forward. Please follow our [Code of
Conduct](https://numpy.org/code-of-conduct/), which applies to all
interactions, including issues and PRs.

For more, please read <https://www.numpy.org/devdocs/dev/index.html>

Thank you for contributing, and happy coding!

______________________________________________________________________

<!--overview-start-->

## Setting up the environment

Ensure you have [`uv`](https://docs.astral.sh/uv/getting-started/installation/)
installed. Now you can install the project with the dev dependencies:

```shell
uv sync
```

You can also install it with a specific Python version, e.g. `3.10`, as

```shell
uv sync --python 3.10
```

## Linting and formatting with `ruff`

NumType uses `ruff` for linting and formatting, and is automatically installed
as a local development dependency. This way, you can lint all `.py` and `.pyi`
files with:

```bash
$ uv run ruff check
All checks passed!
```

Or, to format your code, run

```bash
$ uv run ruff format
351 files left unchanged
```

Be sure to do this before you open a pull request — the CI will complain
if you don't.

For more details, see <https://docs.astral.sh/ruff/>.

## Type-checking

To validate that the annotations are correct, we use two type-checkers:
[basedpyright](https://github.com/detachhead/basedpyright) and
[mypy](https://github.com/python/mypy). Both are included as development
dependency, and therefore automatically installed with `uv sync`.

### basedpyright

You can run basedpyright on the entire project using

```bash
$ uv run basedpyright
0 errors, 0 warnings, 0 notes
```

Since this can take somewhere between 20 to 50 seconds to run, you may want to
limit this to a subdirectory or a specific file that you're working on.

See <https://docs.basedpyright.com/> for IDE integration and other info.

### mypy

Mypy requires a bit more effort to run, since it doesn't play well with
editable dependencies, and it doesn't seem to recognize NumType's `numpy-stubs`
if `numpy` is also installed. You can get around that by running:

```shell
uv run --no-editable --no-group=numpy mypy .
```

In rare cases, the cache can get corrupted, which can lead to incorrect
results. So in case the CI output of mypy differs from your local output, you
should delete the `.mypy_cache` directory in the `numtype` root.

The documentation can be found at <https://mypy.readthedocs.io/>, and issues can
be reported at <https://github.com/python/mypy>.

## Lefthook

Lefthook is a modern Git hooks manager, which automatically lints and formats
your code before you committing it. It will also keep your `uv` environment
up-to-date with the lockfile when you `git pull`.

To install it as a `uv` tool, run

```shell
uv tool install lefthook --upgrade
```

To set it up, navigate to the root of the `numtype` repo, and run

```shell
lefthook install
```

or

```shell
uvx lefthook install
```

Now let's see it all works:

```bash
$ lefthook validate
All good
```

See <https://lefthook.dev/> for more information.

## Tox

You can run the linters, type-checkers, runtime tests, and `stubtest`, all at
once through a single [tox](https://github.com/tox-dev/tox) command.

It's easiest to install it as a `uv` tool:

```shell
uv tool install tox --with tox-uv --upgrade
```

To run it, navigate to the root of the cloned `numtype` directory, and run

```shell
tox p
```

or alternatively,

```shell
uvx tox p
```

If all is good, then you should see something like this appear:

```plaintext
ruff: OK ✔ in 0.05 seconds
pytest: OK ✔ in 0.34 seconds
3.11: OK ✔ in 20.44 seconds
3.10: OK ✔ in 21.53 seconds
3.12: OK ✔ in 22.32 seconds
3.13: OK ✔ in 26.41 seconds
basedpyright: OK ✔ in 27.33 seconds
  ruff: OK (0.05=setup[0.03]+cmd[0.01,0.01] seconds)
  pytest: OK (0.34=setup[0.02]+cmd[0.32] seconds)
  basedpyright: OK (27.33=setup[0.02]+cmd[27.31] seconds)
  mypy: OK (36.39=setup[0.02]+cmd[36.37] seconds)
  3.10: OK (21.53=setup[0.43]+cmd[21.10] seconds)
  3.11: OK (20.44=setup[0.42]+cmd[20.01] seconds)
  3.12: OK (22.32=setup[0.44]+cmd[21.88] seconds)
  3.13: OK (26.41=setup[0.48]+cmd[25.93] seconds)
  congratulations :) (36.44 seconds)
```

Tox installs everything in isolated environments, so you don't have to worry
about your local or global `pip` or `uv` environments.

See <https://tox.wiki/en/stable/> for more information.

## Testing

See the `README.md` in [`numtype/test`][test-docs].

## Documentation

All documentation lives in the `README.md`. Please read it carefully
before proposing any changes. Ensure that the markdown is formatted correctly
with [markdownlint](https://github.com/DavidAnson/markdownlint/tree/main).

## Development Tools

NumType provides several development tools to help with development.

For detailed usage of each tool, please refer to the `README.md`
in the [`tool`][tool-docs] directory or the docstrings within each tool.

## Commit message style

For the most part, commit messages in NumType should follow
[NumPy's guidelines for writing commit messages][numpy-commit-style].
The main difference is that we don't use the prefix acronyms (e.g. `TYP`).
Instead, we use [Gitmoji](https://gitmoji.dev/) as a modern alternative.
Using it gitmoji is not a hard requirement, just a colorful recommendation.
For VSCode users it's most convenient to use the
[`gitmoji-vscode` extension](https://github.com/seatonjiang/gitmoji-vscode).

## Code style

For `.py` files, NumType follows the `black` style, and the `.pyi` stubs follow
the official [style guide for stubs][stub-style].
Both `.py` and `.pyi` are linted and formatted using [`ruff`][ruff], which is
one of the development dependencies.

[numpy-commit-style]: https://numpy.org/devdocs/dev/development_workflow.html#writing-the-commit-message
[ruff]: https://docs.astral.sh/ruff/
[stub-style]: https://typing.python.org/en/latest/guides/writing_stubs.html#style-guide
[test-docs]: https://github.com/numpy/numtype/tree/main/test
[tool-docs]: https://github.com/numpy/numtype/tree/main/tool

<!--overview-end-->
