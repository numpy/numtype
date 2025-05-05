import pathlib
import re
import zipfile
from collections.abc import Mapping
from typing import IO, Any, assert_type

import _numtype as _nt
import numpy as np
from numpy.lib._npyio_impl import BagObj

str_path: str
pathlib_path: pathlib.Path
str_file: IO[str]
bytes_file: IO[bytes]

npz_file: np.lib.npyio.NpzFile

AR_i8: _nt.Array[np.int64]
AR_LIKE_f8: list[float]

class BytesWriter:
    def write(self, data: bytes) -> None: ...

class BytesReader:
    def read(self, n: int = ...) -> bytes: ...
    def seek(self, offset: int, whence: int = ...) -> int: ...

bytes_writer: BytesWriter
bytes_reader: BytesReader

assert_type(npz_file.zip, zipfile.ZipFile | None)
assert_type(npz_file.fid, IO[str] | None)
assert_type(npz_file.files, list[str])
assert_type(npz_file.allow_pickle, bool)
assert_type(npz_file.pickle_kwargs, Mapping[str, Any] | None)
assert_type(npz_file.f, BagObj[np.lib.npyio.NpzFile] | None)
assert_type(npz_file["test"], _nt.Array)
assert_type(len(npz_file), int)
with npz_file as f:
    assert_type(f, np.lib.npyio.NpzFile)

assert_type(np.load(bytes_file), Any)
assert_type(np.load(pathlib_path, allow_pickle=True), Any)
assert_type(np.load(str_path, encoding="bytes"), Any)
assert_type(np.load(bytes_reader), Any)

assert_type(np.save(bytes_file, AR_LIKE_f8), None)
assert_type(np.save(pathlib_path, AR_i8, allow_pickle=True), None)
assert_type(np.save(str_path, AR_LIKE_f8), None)
assert_type(np.save(bytes_writer, AR_LIKE_f8), None)

assert_type(np.savez(bytes_file, AR_LIKE_f8), None)
assert_type(np.savez(pathlib_path, ar1=AR_i8, ar2=AR_i8), None)
assert_type(np.savez(str_path, AR_LIKE_f8, ar1=AR_i8), None)
assert_type(np.savez(bytes_writer, AR_LIKE_f8, ar1=AR_i8), None)

assert_type(np.savez_compressed(bytes_file, AR_LIKE_f8), None)
assert_type(np.savez_compressed(pathlib_path, ar1=AR_i8, ar2=AR_i8), None)
assert_type(np.savez_compressed(str_path, AR_LIKE_f8, ar1=AR_i8), None)
assert_type(np.savez_compressed(bytes_writer, AR_LIKE_f8, ar1=AR_i8), None)

assert_type(np.loadtxt(bytes_file), _nt.Array[np.float64])
assert_type(np.loadtxt(pathlib_path, dtype=np.str_), _nt.Array[np.str_])
assert_type(np.loadtxt(str_path, dtype=str, skiprows=2), _nt.Array)
assert_type(np.loadtxt(str_file, comments="test"), _nt.Array[np.float64])
assert_type(np.loadtxt(str_file, comments=None), _nt.Array[np.float64])
assert_type(np.loadtxt(str_path, delimiter="\n"), _nt.Array[np.float64])
assert_type(np.loadtxt(str_path, ndmin=2), _nt.Array[np.float64])
assert_type(np.loadtxt(["1", "2", "3"]), _nt.Array[np.float64])

assert_type(np.fromregex(bytes_file, "test", np.float64), _nt.Array[np.float64])
assert_type(np.fromregex(str_file, b"test", dtype=float), _nt.Array)
assert_type(np.fromregex(str_path, re.compile(r"test"), dtype=np.str_, encoding="utf8"), _nt.Array[np.str_])
assert_type(np.fromregex(pathlib_path, "test", np.float64), _nt.Array[np.float64])
assert_type(np.fromregex(bytes_reader, "test", np.float64), _nt.Array[np.float64])

assert_type(np.genfromtxt(bytes_file), _nt.Array[np.float64])
assert_type(np.genfromtxt(pathlib_path, dtype=np.str_), _nt.Array[np.str_])
assert_type(np.genfromtxt(str_path, dtype=str, skip_header=2), _nt.Array)
assert_type(np.genfromtxt(str_file, comments="test"), _nt.Array[np.float64])
assert_type(np.genfromtxt(str_path, delimiter="\n"), _nt.Array[np.float64])
assert_type(np.genfromtxt(str_path, ndmin=2), _nt.Array[np.float64])
assert_type(np.genfromtxt(["1", "2", "3"], ndmin=2), _nt.Array[np.float64])
