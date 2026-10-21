import sys
from typing import List
from app.commands.base_command import BaseCommand


class ExitCommand(BaseCommand):

    def execute(self, args: List[str]) -> None:
        print("\nSaliendo de Synthetix Studio. ¡Hasta pronto!")
        sys.exit(0)

    def get_description(self) -> str:
        return "exit - Cierra la sesión de Synthetix Studio."