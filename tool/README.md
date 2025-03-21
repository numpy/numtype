# NumType development tools

## ufunc.py

Introspect NumPy universal functions (ufuncs) by examining their type signatures.

```shell
uv run tool/ufunc.py [-h] [-p] [-f <TABULATE_FORMAT>] <NIN> <NOUT>
```

## testgen.py

Generate type tests for NumType's NumPy integration.

```shell
uv run tool/testgen.py
```

## stubtest.py

Test type stubs against actual implementations using MyPy's stubtest.

```shell
uv run tool/stubtest.py <OPTIONS>
```

## unstub.py

Remove all `.pyi` files from the NumPy site-packages directory.

```shell
uv run tool/unstub.py
```
