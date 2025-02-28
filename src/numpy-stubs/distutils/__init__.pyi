from typing import Any

# TODO(jorenham): remove when the full numpy namespace is defined
# https://github.com/numpy/numtype/issues/41
def __getattr__(name: str) -> Any: ...  # pyright: ignore[reportIncompleteStub]
