# Style Guide

## `TypeVar` names

Use `_{}T` for invariant `TypeVar` names, where `{}` is a concise human-readable description of the upper bound.
Use a `*_co` or `*_contra` suffix to indicate co- or contra-variance.

| Yes &nbsp; :ballot_box_with_check: | No &nbsp; :x: |
| ---------------------------------- | ------------- |
| `_T_co`                            | `T_co`        |
| `_ScalarT`                         | `_SCT`        |
| `_DTypeT`                          | `_DType`      |

## Protocol names

Use `Can{}` for `Protocol` types with a single method, where `{}` is the CamelCase name of that method.
This naming convention was originally introduced by <https://github.com/jorenham/optype>,
and has been gaining popularity since.
Note that this deviates from `Supports{}` from [Python style guide for stubs][SPEC-STYLE],
which is arguably more verbose and less descriptive.

In line with both `optype` and the stub style guide, NumType also uses `Has{}` for single-attribute protocols,
with `{}` the CamelCase attribute name.

| Protocol member | Yes &nbsp; :ballot_box_with_check: | No &nbsp; :x: |
| --------------- | ---------------------------------- | ------------- |
| `__len__()`     | `CanLen`                           | `Sized`       |
| `__fspath__()`  | `CanFSPath`                        | `PathLike`    |
| `fileno()`      | `CanFileno`                        | `HasFileno`   |
| `dtype`         | `HasDType`                         | `DTypeLike`   |

## Newlines between overloaded functions

The ruff formatter tends to remove all whitespace between all functions. But for overloaded functions this is often bad
for readability. To get around this, place a `\n\n#\n` between first overload definition.
For non-overloaded functions this should only be done to separate semantically different *groups* of functions.
For an example, see [`src/numpy-stubs/lib/_type_check_impl.pyi`](https://github.com/numpy/numtype/blob/main/src/numpy-stubs/lib/_type_check_impl.pyi):

```pyi
@overload
def iscomplex(x: ToGeneric_0d) -> np.bool: ...
@overload
def iscomplex(x: ToGeneric_1nd) -> Array[np.bool]: ...

#
@overload
def isreal(x: ToGeneric_0d) -> np.bool: ...
@overload
def isreal(x: ToGeneric_1nd) -> Array[np.bool]: ...

#
def iscomplexobj(x: _HasDType[Any] | ToGeneric_nd) -> bool: ...
def isrealobj(x: _HasDType[Any] | ToGeneric_nd) -> bool: ...
```

## Max line length

For `.py` files the lines must not exceed **88** characters in width, compatible with the [black][BLACK] style.

For `.pyi` stubs, a maximum line length of **120** characters applies.
Note that this is different from the [Python stub style guide][SPEC-STYLE], which recommends 130.
There are several reasons for this choice:

- The github diff viewer supports at most 125 characters.
- In general, 120 is used far more often than 130 as character limit.

[SPEC-STYLE]: https://typing.python.org/en/latest/guides/writing_stubs.html
[BLACK]: https://github.com/psf/black
