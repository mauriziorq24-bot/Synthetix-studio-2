from typing import List
from app.commands.base_command import BaseCommand
from app.core.token_extractor import TokenExtractor
from app.structures.b_tree.b_tree import BTree


class IndexAllCommand(BaseCommand):
    def __init__(self, extractor: TokenExtractor, b_tree: BTree) -> None:
        self._extractor = extractor
        self._b_tree = b_tree

    def execute(self, args: List[str]) -> None:
        print("Indexando tokens de todos los archivos del workspace...")
        total = self._extractor.index_workspace(self._b_tree)
        print(f"Indexación completada. Se procesaron {total} tokens en el Árbol B.")

    def get_description(self) -> str:
        return "index-all - Escanea todos los archivos de código e indexa sus tokens en el Árbol B."