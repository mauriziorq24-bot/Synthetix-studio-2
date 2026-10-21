from typing import List, Optional
from app.structures.b_tree.b_tree_entry import BTreeEntry


class BTreeNode:
    def __init__(self, is_leaf: bool = True) -> None:
        self.is_leaf: bool = is_leaf
        self.entries: List[BTreeEntry] = []
        self.children: List["BTreeNode"] = []

    def find_entry(self, key: str) -> Optional[BTreeEntry]:
        for entry in self.entries:
            if entry.key == key:
                return entry
        return None