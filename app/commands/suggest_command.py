from typing import List
from app.commands.base_command import BaseCommand
from app.structures.avl_tree.avl_tree import AVLTree


class SuggestCommand(BaseCommand):
    def __init__(self, avl_tree: AVLTree) -> None:
        self._avl_tree = avl_tree

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso]: suggest <prefijo>")
            return

        prefix = args[0].strip()
        matches = self._avl_tree.search_by_prefix(prefix)

        if not matches:
            print(f"No se encontraron sugerencias con el prefijo '{prefix}'.")
            return

        print(f"\nSugerencias para '{prefix}':")
        for keyword, desc in matches:
            print(f" • {keyword:<12} : {desc}")
        print()

    def get_description(self) -> str:
        return "suggest <prefijo> - Sugiere autocompletado ordenado inorden desde el AVL."