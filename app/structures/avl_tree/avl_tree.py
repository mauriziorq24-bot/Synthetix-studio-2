from typing import List, Optional, Tuple
from app.structures.avl_tree.avl_node import AVLNode


class AVLTree:
    def __init__(self) -> None:
        self.root: Optional[AVLNode] = None

    def get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def get_balance(self, node: Optional[AVLNode]) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, keyword: str, description: str) -> None:
        self.root = self._insert_node(self.root, keyword.strip(), description.strip())

    def _insert_node(self, node: Optional[AVLNode], keyword: str, description: str) -> AVLNode:
        if node is None:
            return AVLNode(keyword, description)

        if keyword < node.keyword:
            node.left = self._insert_node(node.left, keyword, description)
        elif keyword > node.keyword:
            node.right = self._insert_node(node.right, keyword, description)
        else:
            node.description = description
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # Rotación simple a la derecha (LL)
        if balance > 1 and keyword < node.left.keyword:
            return self._rotate_right(node)

        # Rotación simple a la izquierda (RR)
        if balance < -1 and keyword > node.right.keyword:
            return self._rotate_left(node)

        # Rotación doble izquierda-derecha (LR)
        if balance > 1 and keyword > node.left.keyword:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Rotación doble derecha-izquierda (RL)
        if balance < -1 and keyword < node.right.keyword:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def delete(self, keyword: str) -> None:
        self.root = self._delete_node(self.root, keyword.strip())

    def _get_min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete_node(self, node: Optional[AVLNode], keyword: str) -> Optional[AVLNode]:
        if node is None:
            return None

        if keyword < node.keyword:
            node.left = self._delete_node(node.left, keyword)
        elif keyword > node.keyword:
            node.right = self._delete_node(node.right, keyword)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            successor = self._get_min_value_node(node.right)
            node.keyword = successor.keyword
            node.description = successor.description
            node.right = self._delete_node(node.right, successor.keyword)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self._rotate_right(node)

        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self._rotate_left(node)

        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def search_by_prefix(self, prefix: str) -> List[Tuple[str, str]]:
        results: List[Tuple[str, str]] = []
        self._inorder_prefix(self.root, prefix.strip().lower(), results)
        return results

    def _inorder_prefix(self, node: Optional[AVLNode], prefix: str, results: List[Tuple[str, str]]) -> None:
        if node is None:
            return

        self._inorder_prefix(node.left, prefix, results)
        if node.keyword.lower().startswith(prefix):
            results.append((node.keyword, node.description))
        self._inorder_prefix(node.right, prefix, results)