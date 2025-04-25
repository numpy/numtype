import _numtype as _nt
import numpy as np

AR_U: np.char.chararray[_nt.Shape, np.dtype[np.str_]]
AR_S: np.char.chararray[_nt.Shape, np.dtype[np.bytes_]]

###

AR_S.encode()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]
AR_U.decode()  # type: ignore[misc]  # pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType]

AR_U.join(b"_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.join("_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.lstrip(chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.lstrip(chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.strip(chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.strip(chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.rstrip(chars=b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.rstrip(chars="a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.partition(b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.partition("a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.rpartition(b"a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.rpartition("a")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.replace(b"_", b"-")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.replace("_", "-")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.split(b"_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.split("_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.split(1)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.rsplit(b"_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.rsplit("_")  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.count(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.count("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.endswith(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.endswith("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.startswith(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.startswith("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.find(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.find("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.rfind(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.rfind("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]

AR_U.index(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.index("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_U.rindex(b"a", start=[1, 2, 3])  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
AR_S.rindex("a", end=9)  # type: ignore[arg-type]  # pyright: ignore[reportArgumentType]
