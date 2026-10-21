from typing import List
from app.commands.base_command import BaseCommand
from app.core.workspace_manager import WorkspaceManager


class CreateFileCommand(BaseCommand):

    def __init__(self, workspace: WorkspaceManager) -> None:
        self._workspace = workspace

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso incorrecto]: touch <nombre_archivo>")
            return

        file_name = args[0].strip()
        self._workspace.create_file(file_name)
        print(f"Archivo '{file_name}' creado con éxito.")

    def get_description(self) -> str:
        return "touch <archivo> - Crea un archivo de código vacío en la ubicación actual."