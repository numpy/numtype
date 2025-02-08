import numpy as np

np.bob  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
np.testing.bob  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

# Stdlib modules in the namespace by accident
np.warnings  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
np.sys  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
np.os  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
np.math  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]

np.__deprecated_attrs__  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
np.__expired_functions__  # type: ignore[attr-defined]  # pyright: ignore[reportAttributeAccessIssue]
