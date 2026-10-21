from typing import Optional


class AVLNode:
    def __init__(self, keyword: str, description: str) -> None:
        self.keyword: str = keyword
        self.description: str = description
        self.height: int = 1
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None