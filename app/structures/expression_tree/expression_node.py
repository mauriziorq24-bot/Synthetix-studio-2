from typing import Optional


class ExpressionNode:
    def __init__(
        self,
        value: str,
        left: Optional["ExpressionNode"] = None,
        right: Optional["ExpressionNode"] = None,
    ) -> None:
        self.value: str = value
        self.left: Optional["ExpressionNode"] = left
        self.right: Optional["ExpressionNode"] = right

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None