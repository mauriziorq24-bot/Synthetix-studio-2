import re
from typing import List, Tuple
from app.core.workspace_manager import WorkspaceManager
from app.structures.b_tree.b_tree import BTree


class TokenExtractor:
    _IDENTIFIER_REGEX = re.compile(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b")

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def index_workspace(self, b_tree: BTree) -> int:
        files = self._workspace.get_all_code_files()
        total_tokens = 0

        for file_node in files:
            physical_path = self._workspace.get_physical_path(file_node)
            rel_path = file_node.get_relative_path()

            try:
                with open(physical_path, "r", encoding="utf-8") as f:
                    for line_idx, line in enumerate(f, start=1):
                        matches = self._IDENTIFIER_REGEX.findall(line)
                        for token in matches:
                            b_tree.insert(token, rel_path, line_idx)
                            total_tokens += 1
            except Exception:
                continue

        return total_tokens