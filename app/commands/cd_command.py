from typing import List
from app.commands.base_command import BaseCommand
from app.core.workspace_manager import WorkspaceManager


class CdCommand(BaseCommand):

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso incorrecto]: cd <directorio> | cd ..")
            return

        target = args[0].strip()
        self._workspace.change_directory(target)
        current_path = self._workspace.current_node.get_relative_path()
        print(f"Directorio actual: [{current_path}]")

    def get_description(self) -> str:
        return "cd <nombre|..> - Cambia de directorio (un nivel hacia adentro o '..' hacia el padre)."