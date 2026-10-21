from typing import List
from app.commands.base_command import BaseCommand
from app.structures.avl_tree.avl_tree import AVLTree


class RemoveKeywordCommand(BaseCommand):
    def __init__(self, avl_tree: AVLTree) -> None:
        self._avl_tree = avl_tree

    def execute(self, args: List[str]) -> None:
        if len(args) != 1:
            print("[Uso]: remove-keyword <palabra>")
            return

        keyword = args[0].strip()
        self._avl_tree.delete(keyword)
        print(f"Palabra clave '{keyword}' eliminada del árbol AVL (rebalanceo aplicado).")

    def get_description(self) -> str:
        return "remove-keyword <palabra> - Elimina una palabra clave y rebalancea el AVL."