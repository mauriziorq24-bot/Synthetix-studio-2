from typing import List
from app.commands.base_command import BaseCommand
from app.core.workspace_manager import WorkspaceManager


class MkdirCommand(BaseCommand):

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso incorrecto]: mkdir <nombre_directorio>")
            return

        folder_name = args[0].strip()
        self._workspace.create_directory(folder_name)
        print(f"Directorio '{folder_name}' creado con éxito.")

    def get_description(self) -> str:
        return "mkdir <nombre> - Crea un nuevo subdirectorio en la ubicación actual."