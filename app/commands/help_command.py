from typing import List, TYPE_CHECKING
from app.commands.base_command import BaseCommand

if TYPE_CHECKING:
    from app.core.command_invoker import CommandInvoker


class HelpCommand(BaseCommand):

    def __init__(self, invoker: "CommandInvoker") -> None:
        self._invoker = invoker

    def execute(self, args: List[str]) -> None:
        print("\n" + "=" * 55)
        print("          SYNTHETIX STUDIO - COMANDOS DISPONIBLES")
        print("=" * 55)
        commands = self._invoker.get_commands()
        
        for name, cmd in sorted(commands.items()):
            print(f" • {name:<14} : {cmd.get_description()}")
        print("=" * 55 + "\n")

    def get_description(self) -> str:
        return "help - Muestra la lista de todos los comandos y su uso."