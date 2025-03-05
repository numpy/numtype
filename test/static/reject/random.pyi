from typing import Final

import numpy as np
import numpy.typing as npt

SEED_FLOAT: Final[float] = ...
SEED_ARR_FLOAT: Final[npt.NDArray[np.float64]] = ...
SEED_ARRLIKE_FLOAT: Final[list[float]] = ...
SEED_SEED_SEQ: Final[np.random.SeedSequence] = ...
SEED_STR: Final[str] = ...

# default rng
np.random.default_rng(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.default_rng(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.default_rng(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.default_rng(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

# Seed Sequence
np.random.SeedSequence(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SeedSequence(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SeedSequence(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SeedSequence(SEED_SEED_SEQ)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SeedSequence(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

seed_seq: np.random.bit_generator.SeedSequence = ...
seed_seq.spawn(11.5)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
seed_seq.generate_state(3.2)  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, np.uint8)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "uint8")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "u1")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, np.uint16)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "uint16")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "u2")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, np.int32)  # type: ignore[arg-type]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "int32")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]
seed_seq.generate_state(3, "i4")  # type: ignore[call-overload]  # pyright: ignore[reportCallIssue, reportArgumentType]

# Bit Generators
np.random.MT19937(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.MT19937(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.MT19937(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.MT19937(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.random.PCG64(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.PCG64(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.PCG64(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.PCG64(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.random.Philox(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Philox(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Philox(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Philox(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

np.random.SFC64(SEED_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SFC64(SEED_ARR_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SFC64(SEED_ARRLIKE_FLOAT)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.SFC64(SEED_STR)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

# Generator
np.random.Generator(None)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Generator(12333283902830213)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Generator("OxFEEDF00D")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Generator([123, 234])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
np.random.Generator(np.array([123, 234], dtype="u4"))  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
