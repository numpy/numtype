"""LibCST codemods."""

from collections.abc import Sequence
from typing_extensions import override

import libcst as cst
from libcst.codemod import VisitorBasedCodemodCommand


class MoveNoneToEnd(VisitorBasedCodemodCommand):
    """
    A codemod that moves `None` to the end of union types when using the `|` operator, fixing `RUF036`.

    To run this codemod, run the following command from the root directory:

    ```shell
    uv run -m libcst.tool codemod -x --include-stubs tools.codemods.MoveNoneToEnd src/numpy-stubs
    ```

    Example:
        - Before: None | str | int
        - After:  str | int | None
    """

    @override
    def leave_BinaryOperation(
        self,
        original_node: cst.BinaryOperation,
        updated_node: cst.BinaryOperation,
    ) -> cst.BaseExpression:
        # Only process union operations using |
        if not isinstance(updated_node.operator, cst.BitOr):
            return updated_node

        # Collect all types in the union
        def collect_types(node: cst.BaseExpression) -> list[cst.BaseExpression]:
            if isinstance(node, cst.BinaryOperation) and isinstance(node.operator, cst.BitOr):
                return collect_types(node.left) + collect_types(node.right)
            return [node]

        types = collect_types(updated_node)

        # Check if None exists and is not already at the end
        none_types = [t for t in types if isinstance(t, cst.Name) and t.value == "None"]
        if not none_types or (len(types) > 1 and types[-1] in none_types):
            return updated_node

        # Remove None and add it to the ends
        other_types = [t for t in types if not (isinstance(t, cst.Name) and t.value == "None")]
        reordered_types = other_types + none_types

        # Rebuild the union expression
        def build_union(exprs: Sequence[cst.BaseExpression]) -> cst.BaseExpression:
            if len(exprs) == 1:
                return exprs[0]
            return cst.BinaryOperation(build_union(exprs[:-1]), cst.BitOr(), exprs[-1])

        return build_union(reordered_types)
