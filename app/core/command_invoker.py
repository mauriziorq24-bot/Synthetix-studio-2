from typing import Dict, List, Optional
from app.commands.base_command import BaseCommand


class CommandInvoker:

    def __init__(self) -> None:
        self._commands: Dict[str, BaseCommand] = {}

    def register_command(self, name: str, command: BaseCommand) -> None:
        self._commands[name.strip().lower()] = command

    def execute_command(self, name: str, args: List[str]) -> None:
        command_key = name.strip().lower()
        command = self._commands.get(command_key)

        if command is None:
            print(f"[Error]: Comando desconocido '{name}'. Escribe 'help' para ver la lista de comandos.")
            return

        try:
            command.execute(args)
        except Exception as error:
            print(f"[Error en '{name}']: {error}")

    def get_commands(self) -> Dict[str, BaseCommand]:
        return dict(self._commands)