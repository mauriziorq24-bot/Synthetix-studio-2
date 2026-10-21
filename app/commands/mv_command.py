from typing import List
from app.commands.base_command import BaseCommand
from app.core.workspace_manager import WorkspaceManager


class MvCommand(BaseCommand):

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def execute(self, args: List[str]) -> None:
        if len(args) != 2:
            print("[Uso incorrecto]: mv <origen> <carpeta_destino>")
            return

        source = args[0].strip()
        target_folder = args[1].strip()

        self._workspace.move_node(source, target_folder)
        print(f"'{source}' movido a '{target_folder}' correctamente.")

    def get_description(self) -> str:
        return "mv <origen> <destino> - Mueve un elemento actual hacia otra carpeta."