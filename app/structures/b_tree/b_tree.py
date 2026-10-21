from typing import Optional
from app.structures.b_tree.b_tree_entry import BTreeEntry
from app.structures.b_tree.b_tree_node import BTreeNode


class BTree:
    def __init__(self, minimum_degree: int = 2) -> None:
        self.t: int = minimum_degree
        self.root: BTreeNode = BTreeNode(is_leaf=True)

    def search(self, key: str) -> Optional[BTreeEntry]:
        return self._search_node(self.root, key)

    def _search_node(self, node: BTreeNode, key: str) -> Optional[BTreeEntry]:
        i = 0
        while i < len(node.entries) and key > node.entries[i].key:
            i += 1

        if i < len(node.entries) and node.entries[i].key == key:
            return node.entries[i]

        if node.is_leaf:
            return None

        return self._search_node(node.children[i], key)

    def insert(self, key: str, file_path: str, line_number: int) -> None:
        existing = self.search(key)
        if existing is not None:
            existing.add_occurrence(file_path, line_number)
            return

        root = self.root
        if len(root.entries) == (2 * self.t - 1):
            new_root = BTreeNode(is_leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0, self.root)
            self.root = new_root
            self._insert_non_full(new_root, key, file_path, line_number)
        else:
            self._insert_non_full(root, key, file_path, line_number)

    def _insert_non_full(self, node: BTreeNode, key: str, file_path: str, line_number: int) -> None:
        i = len(node.entries) - 1

        if node.is_leaf:
            entry = BTreeEntry(key)
            entry.add_occurrence(file_path, line_number)
            node.entries.append(entry)
            node.entries.sort(key=lambda x: x.key)
        else:
            while i >= 0 and key < node.entries[i].key:
                i -= 1
            i += 1

            if len(node.children[i].entries) == (2 * self.t - 1):
                self._split_child(node, i, node.children[i])
                if key > node.entries[i].key:
                    i += 1
            self._insert_non_full(node.children[i], key, file_path, line_number)

    def _split_child(self, parent: BTreeNode, index: int, full_child: BTreeNode) -> None:
        t = self.t
        new_child = BTreeNode(is_leaf=full_child.is_leaf)

        median_entry = full_child.entries[t - 1]

        new_child.entries = full_child.entries[t:]
        full_child.entries = full_child.entries[:t - 1]

        if not full_child.is_leaf:
            new_child.children = full_child.children[t:]
            full_child.children = full_child.children[:t]

        parent.children.insert(index + 1, new_child)
        parent.entries.insert(index, median_entry)