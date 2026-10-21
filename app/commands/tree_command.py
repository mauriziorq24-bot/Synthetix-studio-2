from typing import List
from app.commands.base_command import BaseCommand
from app.core.workspace_manager import WorkspaceManager


class TreeCommand(BaseCommand):

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def execute(self, args: List[str]) -> None:
        tree_view = self._workspace.tree.render_tree(self._workspace.tree.root)
        print("\n" + tree_view + "\n")

    def get_description(self) -> str:
        return "tree - Muestra la jerarquía de carpetas y archivos en forma de árbol."