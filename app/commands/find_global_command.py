from typing import List
from app.commands.base_command import BaseCommand
from app.structures.b_tree.b_tree import BTree


class FindGlobalCommand(BaseCommand):
    def __init__(self, b_tree: BTree) -> None:
        self._b_tree = b_tree

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso]: find-global <token>")
            return

        token = args[0].strip()
        entry = self._b_tree.search(token)

        if entry is None or not entry.occurrences:
            print(f"Token '{token}' no encontrado en el índice del Árbol B.")
            return

        print(f"\nOcurrencias encontradas para '{token}' ({len(entry.occurrences)} total):")
        for occ in entry.occurrences:
            print(f" • Archivo: {occ.file_path:<25} | Línea: {occ.line_number}")
        print()

    def get_description(self) -> str:
        return "find-global <token> - Busca un token globalmente en el Árbol B."