import numpy as np
from typing_extensions import assert_type

# 1. Run the function
path_info = np.einsum_path("ii->i", np.eye(3))

# 2. Unpack the result (tuple of list and string)
path_list, path_str = path_info

# 3. Verify that Mypy recognizes the specific types we just added
assert_type(path_list, list[str | tuple[int, ...]])
assert_type(path_str, str)