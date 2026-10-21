from typing import List
from app.structures.file_node_type import FileNodeType
from app.structures.n_ary_node import NAryNode


class NAryTree:

    def __init__(self, root_name: str = "workspace_root") -> None:
        self.root: NAryNode = NAryNode(root_name, FileNodeType.DIRECTORY, parent=None)

    def render_tree(self, start_node: NAryNode) -> str:
        lines: List[str] = [f"{start_node.name}/" if start_node.is_directory() else start_node.name]
        self._build_tree_view(start_node, "", lines)
        return "\n".join(lines)

    def _build_tree_view(self, current: NAryNode, prefix: str, lines: List[str]) -> None:
        total_children = len(current.children)
        for index, child in enumerate(current.children):
            is_last = (index == total_children - 1)
            connector = "└── " if is_last else "├── "
            child_label = f"{child.name}/" if child.is_directory() else child.name
            lines.append(f"{prefix}{connector}{child_label}")

            if child.is_directory():
                extension = "    " if is_last else "│   "
                self._build_tree_view(child, prefix + extension, lines)