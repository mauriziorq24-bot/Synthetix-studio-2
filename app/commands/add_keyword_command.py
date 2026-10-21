from typing import List
from app.commands.base_command import BaseCommand
from app.structures.avl_tree.avl_tree import AVLTree


class AddKeywordCommand(BaseCommand):
    def __init__(self, avl_tree: AVLTree) -> None:
        self._avl_tree = avl_tree

    def execute(self, args: List[str]) -> None:
        if len(args) < 2:
            print('[Uso]: add-keyword <palabra> "<descripcion>"')
            return

        keyword = args[0].strip()
        description = " ".join(args[1:]).strip()
        self._avl_tree.insert(keyword, description)
        print(f"Palabra clave '{keyword}' agregada exitosamente al árbol AVL.")

    def get_description(self) -> str:
        return 'add-keyword <palabra> "<desc>" - Inserta una palabra clave en el árbol AVL.'