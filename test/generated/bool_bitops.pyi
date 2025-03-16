# @generated 2025-03-16T15:52:15Z with tool/testgen.py
from typing import Literal, TypeAlias
from typing_extensions import assert_type

import numpy as np

###

Bool_: TypeAlias = np.bool
Bool0: TypeAlias = np.bool[Literal[False]]
Bool1: TypeAlias = np.bool[Literal[True]]

###

py_: bool
py0: Literal[False]
py1: Literal[True]

np_: Bool_
np0: Bool0
np1: Bool1

###
# __bool__

assert_type(np0.__bool__(), Literal[False])
assert_type(np1.__bool__(), Literal[True])
assert_type(np_.__bool__(), bool)

###
# __abs__

assert_type(abs(np0), Bool0)
assert_type(abs(np1), Bool1)
assert_type(abs(np_), Bool_)

###
# __invert__

assert_type(~np0, Bool1)
assert_type(~np1, Bool0)
assert_type(~np_, Bool_)

###
# __eq__

assert_type(np0 == np0, Bool1)
assert_type(np0 == np1, Bool0)
assert_type(np1 == np0, Bool0)
assert_type(np1 == np1, Bool1)

assert_type(np0 == np_, Bool_)
assert_type(np1 == np_, Bool_)
assert_type(np_ == np0, Bool_)
assert_type(np_ == np1, Bool_)
assert_type(np_ == np_, Bool_)

assert_type(np0 == py0, Bool1)
assert_type(np0 == py1, Bool0)
assert_type(np0 == py_, Bool_)
assert_type(np1 == py0, Bool0)
assert_type(np1 == py1, Bool1)
assert_type(np1 == py_, Bool_)
assert_type(np_ == py0, Bool_)
assert_type(np_ == py1, Bool_)
assert_type(np_ == py_, Bool_)

###
# __ne__

assert_type(np0 != np0, Bool0)
assert_type(np0 != np1, Bool1)
assert_type(np1 != np0, Bool1)
assert_type(np1 != np1, Bool0)

assert_type(np0 != np_, Bool_)
assert_type(np1 != np_, Bool_)
assert_type(np_ != np0, Bool_)
assert_type(np_ != np1, Bool_)
assert_type(np_ != np_, Bool_)

assert_type(np0 != py0, Bool0)
assert_type(np0 != py1, Bool1)
assert_type(np0 != py_, Bool_)
assert_type(np1 != py0, Bool1)
assert_type(np1 != py1, Bool0)
assert_type(np1 != py_, Bool_)
assert_type(np_ != py0, Bool_)
assert_type(np_ != py1, Bool_)
assert_type(np_ != py_, Bool_)

###
# __lt__

assert_type(np0 < np0, Bool0)
assert_type(np0 < np1, Bool1)
assert_type(np1 < np0, Bool0)
assert_type(np1 < np1, Bool0)

assert_type(np0 < np_, Bool_)
assert_type(np1 < np_, Bool0)
assert_type(np_ < np0, Bool0)
assert_type(np_ < np1, Bool_)
assert_type(np_ < np_, Bool_)

assert_type(np0 < py0, Bool0)
assert_type(np0 < py1, Bool1)
assert_type(np0 < py_, Bool_)
assert_type(np1 < py0, Bool0)
assert_type(np1 < py1, Bool0)
assert_type(np1 < py_, Bool0)
assert_type(np_ < py0, Bool0)
assert_type(np_ < py1, Bool_)
assert_type(np_ < py_, Bool_)

###
# __le__

assert_type(np0 <= np0, Bool1)
assert_type(np0 <= np1, Bool1)
assert_type(np1 <= np0, Bool0)
assert_type(np1 <= np1, Bool1)

assert_type(np0 <= np_, Bool1)
assert_type(np1 <= np_, Bool_)
assert_type(np_ <= np0, Bool_)
assert_type(np_ <= np1, Bool1)
assert_type(np_ <= np_, Bool_)

assert_type(np0 <= py0, Bool1)
assert_type(np0 <= py1, Bool1)
assert_type(np0 <= py_, Bool1)
assert_type(np1 <= py0, Bool0)
assert_type(np1 <= py1, Bool1)
assert_type(np1 <= py_, Bool_)
assert_type(np_ <= py0, Bool_)
assert_type(np_ <= py1, Bool1)
assert_type(np_ <= py_, Bool_)

###
# __gt__

assert_type(np0 > np0, Bool0)
assert_type(np0 > np1, Bool0)
assert_type(np1 > np0, Bool1)
assert_type(np1 > np1, Bool0)

assert_type(np0 > np_, Bool0)
assert_type(np1 > np_, Bool_)
assert_type(np_ > np0, Bool_)
assert_type(np_ > np1, Bool0)
assert_type(np_ > np_, Bool_)

assert_type(np0 > py0, Bool0)
assert_type(np0 > py1, Bool0)
assert_type(np0 > py_, Bool0)
assert_type(np1 > py0, Bool1)
assert_type(np1 > py1, Bool0)
assert_type(np1 > py_, Bool_)
assert_type(np_ > py0, Bool_)
assert_type(np_ > py1, Bool0)
assert_type(np_ > py_, Bool_)

###
# __ge__

assert_type(np0 >= np0, Bool1)
assert_type(np0 >= np1, Bool0)
assert_type(np1 >= np0, Bool1)
assert_type(np1 >= np1, Bool1)

assert_type(np0 >= np_, Bool_)
assert_type(np1 >= np_, Bool1)
assert_type(np_ >= np0, Bool1)
assert_type(np_ >= np1, Bool_)
assert_type(np_ >= np_, Bool_)

assert_type(np0 >= py0, Bool1)
assert_type(np0 >= py1, Bool0)
assert_type(np0 >= py_, Bool_)
assert_type(np1 >= py0, Bool1)
assert_type(np1 >= py1, Bool1)
assert_type(np1 >= py_, Bool1)
assert_type(np_ >= py0, Bool1)
assert_type(np_ >= py1, Bool_)
assert_type(np_ >= py_, Bool_)

###
# __[r]add__

assert_type(np0 + np0, Bool0)
assert_type(np0 + np1, Bool1)
assert_type(np1 + np0, Bool1)
assert_type(np1 + np1, Bool1)

assert_type(np0 + np_, Bool_)
assert_type(np1 + np_, Bool1)
assert_type(np_ + np0, Bool_)
assert_type(np_ + np1, Bool1)
assert_type(np_ + np_, Bool_)

assert_type(np0 + py0, Bool0)
assert_type(np0 + py1, Bool1)
assert_type(np0 + py_, Bool_)
assert_type(np1 + py0, Bool1)
assert_type(np1 + py1, Bool1)
assert_type(np1 + py_, Bool1)
assert_type(np_ + py0, Bool_)
assert_type(np_ + py1, Bool1)
assert_type(np_ + py_, Bool_)

assert_type(py0 + np0, Bool0)
assert_type(py0 + np1, Bool1)
assert_type(py0 + np_, Bool_)
assert_type(py1 + np0, Bool1)
assert_type(py1 + np1, Bool1)
assert_type(py1 + np_, Bool1)
assert_type(py_ + np0, Bool_)
assert_type(py_ + np1, Bool1)
assert_type(py_ + np_, Bool_)

###
# __[r]mul__

assert_type(np0 * np0, Bool0)
assert_type(np0 * np1, Bool0)
assert_type(np1 * np0, Bool0)
assert_type(np1 * np1, Bool1)

assert_type(np0 * np_, Bool0)
assert_type(np1 * np_, Bool_)
assert_type(np_ * np0, Bool0)
assert_type(np_ * np1, Bool_)
assert_type(np_ * np_, Bool_)

assert_type(np0 * py0, Bool0)
assert_type(np0 * py1, Bool0)
assert_type(np0 * py_, Bool0)
assert_type(np1 * py0, Bool0)
assert_type(np1 * py1, Bool1)
assert_type(np1 * py_, Bool_)
assert_type(np_ * py0, Bool0)
assert_type(np_ * py1, Bool_)
assert_type(np_ * py_, Bool_)

assert_type(py0 * np0, Bool0)
assert_type(py0 * np1, Bool0)
assert_type(py0 * np_, Bool0)
assert_type(py1 * np0, Bool0)
assert_type(py1 * np1, Bool1)
assert_type(py1 * np_, Bool_)
assert_type(py_ * np0, Bool0)
assert_type(py_ * np1, Bool_)
assert_type(py_ * np_, Bool_)

###
# __[r]and__

assert_type(np0 & np0, Bool0)
assert_type(np0 & np1, Bool0)
assert_type(np1 & np0, Bool0)
assert_type(np1 & np1, Bool1)

assert_type(np0 & np_, Bool0)
assert_type(np1 & np_, Bool_)
assert_type(np_ & np0, Bool0)
assert_type(np_ & np1, Bool_)
assert_type(np_ & np_, Bool_)

assert_type(np0 & py0, Bool0)
assert_type(np0 & py1, Bool0)
assert_type(np0 & py_, Bool0)
assert_type(np1 & py0, Bool0)
assert_type(np1 & py1, Bool1)
assert_type(np1 & py_, Bool_)
assert_type(np_ & py0, Bool0)
assert_type(np_ & py1, Bool_)
assert_type(np_ & py_, Bool_)

assert_type(py0 & np0, Bool0)
assert_type(py0 & np1, Bool0)
assert_type(py0 & np_, Bool0)
assert_type(py1 & np0, Bool0)
assert_type(py1 & np1, Bool1)
assert_type(py1 & np_, Bool_)
assert_type(py_ & np0, Bool0)
assert_type(py_ & np1, Bool_)
assert_type(py_ & np_, Bool_)

###
# __[r]xor__

assert_type(np0 ^ np0, Bool0)
assert_type(np0 ^ np1, Bool1)
assert_type(np1 ^ np0, Bool1)
assert_type(np1 ^ np1, Bool0)

assert_type(np0 ^ np_, Bool_)
assert_type(np1 ^ np_, Bool_)
assert_type(np_ ^ np0, Bool_)
assert_type(np_ ^ np1, Bool_)
assert_type(np_ ^ np_, Bool_)

assert_type(np0 ^ py0, Bool0)
assert_type(np0 ^ py1, Bool1)
assert_type(np0 ^ py_, Bool_)
assert_type(np1 ^ py0, Bool1)
assert_type(np1 ^ py1, Bool0)
assert_type(np1 ^ py_, Bool_)
assert_type(np_ ^ py0, Bool_)
assert_type(np_ ^ py1, Bool_)
assert_type(np_ ^ py_, Bool_)

assert_type(py0 ^ np0, Bool0)
assert_type(py0 ^ np1, Bool1)
assert_type(py0 ^ np_, Bool_)
assert_type(py1 ^ np0, Bool1)
assert_type(py1 ^ np1, Bool0)
assert_type(py1 ^ np_, Bool_)
assert_type(py_ ^ np0, Bool_)
assert_type(py_ ^ np1, Bool_)
assert_type(py_ ^ np_, Bool_)

###
# __[r]or__

assert_type(np0 | np0, Bool0)
assert_type(np0 | np1, Bool1)
assert_type(np1 | np0, Bool1)
assert_type(np1 | np1, Bool1)

assert_type(np0 | np_, Bool_)
assert_type(np1 | np_, Bool1)
assert_type(np_ | np0, Bool_)
assert_type(np_ | np1, Bool1)
assert_type(np_ | np_, Bool_)

assert_type(np0 | py0, Bool0)
assert_type(np0 | py1, Bool1)
assert_type(np0 | py_, Bool_)
assert_type(np1 | py0, Bool1)
assert_type(np1 | py1, Bool1)
assert_type(np1 | py_, Bool1)
assert_type(np_ | py0, Bool_)
assert_type(np_ | py1, Bool1)
assert_type(np_ | py_, Bool_)

assert_type(py0 | np0, Bool0)
assert_type(py0 | np1, Bool1)
assert_type(py0 | np_, Bool_)
assert_type(py1 | np0, Bool1)
assert_type(py1 | np1, Bool1)
assert_type(py1 | np_, Bool1)
assert_type(py_ | np0, Bool_)
assert_type(py_ | np1, Bool1)
assert_type(py_ | np_, Bool_)
