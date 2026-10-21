from typing import List, Optional
from app.structures.file_node_type import FileNodeType


class NAryNode:

    def __init__(self, name: str, node_type: FileNodeType, parent: Optional["NAryNode"] = None) -> None:
        self.name: str = name
        self.node_type: FileNodeType = node_type
        self.parent: Optional["NAryNode"] = parent
        self.children: List["NAryNode"] = []

    def is_directory(self) -> bool:
        return self.node_type == FileNodeType.DIRECTORY

    def is_file(self) -> bool:
        return self.node_type == FileNodeType.FILE

    def find_child(self, name: str) -> Optional["NAryNode"]:
        for child in self.children:
            if child.name == name:
                return child
        return None

    def add_child(self, child_node: "NAryNode") -> None:
        child_node.parent = self
        self.children.append(child_node)

    def remove_child(self, name: str) -> Optional["NAryNode"]:
        for index, child in enumerate(self.children):
            if child.name == name:
                removed_node = self.children.pop(index)
                removed_node.parent = None
                return removed_node
        return None

    def get_relative_path(self) -> str:
        segments = []
        current: Optional["NAryNode"] = self
        while current is not None and current.parent is not None:
            segments.append(current.name)
            current = current.parent
        segments.reverse()
        return "/".join(segments) if segments else "."