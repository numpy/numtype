# NumType testing

Mypy and basedmypy will only recognize the `src/numpy-stubs` if `numtype` is installed in an
isolated project, and it cannot be editable.
The private `numtype-test` project in this directory provides entrypoints that will run basedmypy
and basedpyright.

To run basedmypy (`bmp` for short) on the static tests, run

```bash
uv run static <bmp|bpr|all> [OPTIONS]
```

Here, `bmp` runs (based)`mypy`, `bpr` runs `basedpyright`, and `all` runs both.
If no options are provided, it defaults to `static/`.

To run this form the root `numtype` directory, you can pass an additional `--project=test` flag
to the `uv run` command (i.e. before `static`).
