# NumType Tools

## ufunc.py

Introspect NumPy universal functions (ufuncs) by examining their type signatures.

```python
uv run tool/ufunc.py [-h] [-p] [-f <TABULATE_FORMAT>] <NIN> <NOUT>
```

## testgen.py

Generate type tests for NumType's NumPy integration.

```python
uv run tool/testgen.py
```

## stubtest.py

Test type stubs against actual implementations using MyPy's stubtest.

```python
uv run tool/stubtest.py <OPTIONS>
```

## unstub.py

Remove all `.pyi` files from the NumPy site-packages directory.

```python
uv run tool/unstub.py
```
