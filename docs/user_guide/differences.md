# Differences with NumPy

## Concrete scalar types

Since NumPy 2.2, the `float64` and `complex128` scalar types were made into _concrete_ types.
Before that, they were aliases of `#!py floating[_64Bit]` and `#!py complexfloating[_64Bit, _64Bit]`,
respectively. But at runtime, `floating` is not the same as `float64`, so this was incorrect.

Before Numpy 2.2, type-checkers accepted the following assignment:

```py
x: np.float64 = np.floating
```

But now that `float64` is a proper subclass of `floating`, this is no longer valid.
Type-checkers will therefore report this as an error.

However, many users did not like this, because it often required them to change
a lot of their code. So for a smooth transition, we kept the other scalar types
such as `int8` as aliases to `#!py np.integer[_8Bit]` in NumPy. This is, in fact, one of
the main reasons for why NumType was created.

In NumType all scalar types are annotated as concrete subtypes, or aliases thereof.
That means that `#!py x: np.integer = int8` is **not** allowed in NumType, which in NumPy you
could get away with.

To be specific, the following scalar types are proper subclasses in NumType:

- `int8`, `int16`, `int32`, and `int64`
- `uint8`, `uint16`, `uint32`, and `uint64`
- `float16`, `float32`, _`float64`_, and `longdouble`
- `complex64`, _`complex128`_, and `clongdouble`

The other numeric scalar types are defined as aliases, and assume a 64-bit platform.

## No more `NBitBase`

The purpose of [`#!py numpy.typing.NBitBase`][numpy.typing.NBitBase] was as upper bound to
a type parameter, for use in generic abstract scalar types like `#!py floating[T]`.
But the now concrete scalar types will no longer accept _any_ `#!py floating[T]`.
`NBitBase` should therefore not be used anymore.

### Alternatives

Type parameters can instead use an abstract scalar type as an upper bound. So instead of

/// tab | Python 3.10 and above

```py
import numpy as np
import numpy.typing as npt
from typing import TypeVar

NT = TypeVar("NT", bound=npt.NBitBase)

def f(x: np.floating[NT]) -> np.floating[NT]: ...
```

///
/// tab | Python 3.12 and above
select: True

```py
import numpy as np
import numpy.typing as npt

def f[NT: npt.NBitBase](x: np.floating[NT]) -> np.floating[NT]: ...
```

///

you can write

/// tab | Python 3.10 and above

```py
import numpy as np
from typing import TypeVar

FloatT = TypeVar("FloatT", bound=np.floating)

def f(x: FloatT) -> FloatT: ...
```

///
/// tab | Python 3.12 and above
select: True

```py
import numpy as np

def f[FloatT: np.floating](x: FloatT) -> FloatT: ...
```

///

As you can see, this also makes the code more readable.

But what if that isn't possible? For instance, you might have the following function:

/// tab | Python 3.10 and above

```py
import numpy as np
import numpy.typing as npt
from typing import TypeVar

NT = TypeVar("NT", bound=npt.NBitBase)

def f(x: np.complexfloating[NT]) -> np.floating[NT]: ...
```

///
/// tab | Python 3.12 and above
select: True

```py
import numpy as np
import numpy.typing as npt

def f[NT: npt.NBitBase](x: np.complexfloating[NT]) -> np.floating[NT]: ...
```

///

In that case, you can rewrite it by using
[`#!py typing.overload`](https://typing.python.org/en/latest/spec/overload.html):

```py
import numpy as np
from typing import overload

@overload
def f(x: np.complex64) -> np.float32: ...
@overload
def f(x: np.complex128) -> np.float64: ...
@overload
def f(x: np.clongdouble) -> np.longdouble: ...
```

And even though it has gotten more verbose, it requires less mental to interpret.

## Extended precision removals

The following non-existent scalar types have been removed (numpy/numtype#209):

- `int128` and `int256`
- `uint128` and `uint256`
- `float80` and `float256`
- `complex160` and `complex512`

These types will not be defined on any supported platform.

## Aliases of `[c]longdouble`

The platform-dependent `float96` and `float128` types are equivalent aliases of
`longdouble` (numpy/numtype#397):, and their complex analogues, `complex192` and `complex256`,
alias `clongdouble` (numpy/numtype#391).
This was done in order to minimize the expected amount of "but it works on my machine".

## Return types of `[c]longdouble.item()` and `.tolist()`

In Numpy, `longdouble` and `clongdouble` aren't annotated as concrete subclasses of
`[complex]floating`, but as _aliases_. A consequence of this is that their `item` and `tolist`
methods had to return the same type as that of all other `floating` and `complexfloating` types,
i.e. `float` and `complex`. But this is incorrect for `longdouble` and `clongdouble`:

```pycon
>>> import numpy as np
>>> np.longdouble(1).item()
np.longdouble('1.0')
>>> np.clongdouble(1).item()
np.clongdouble('1+0j')
```

In NumType, the stubs correctly reflect this runtime behaviour.

## Removed `number.__floordiv__`

The abstract `numpy.number` type represents a scalar that's either integer, float, or complex.
But the builtin "floordiv" operator, `//` is only supported for integer and floating scalars.
Complex numpy scalars will raise an error. But in NumPy, type-checkers will allow you to write
the following type-unsafe code:

```py
import numpy as np

def half(a: np.number) -> np.number:
    return a // 2

half(np.complex128(1j))  # accepted
```

In NumType's `numpy-stubs`, the `numpy.number.__[r]floordiv__` methods don't exist. This means that
if you have `numtype` installed, your type-checker will report `a // 2` as an error.

## Mypy plugin

NumType does not support the numpy mypy plugin. The reasons for this are explained in the
[NumPy 2.3.0 deprecation notes](https://numpy.org/devdocs/release/2.3.0-notes.html#deprecations).
