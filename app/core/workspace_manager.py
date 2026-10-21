import os
import shutil
from typing import List
from app.structures.file_node_type import FileNodeType
from app.structures.n_ary_node import NAryNode
from app.structures.n_ary_tree import NAryTree


class WorkspaceManager:

    def __init__(self, base_physical_path: str = "workspace_root") -> None:
        self._base_physical_path: str = os.path.abspath(base_physical_path)
        os.makedirs(self._base_physical_path, exist_ok=True)

        self._tree: NAryTree = NAryTree(os.path.basename(self._base_physical_path))
        self._current_node: NAryNode = self._tree.root

    @property
    def current_node(self) -> NAryNode:
        return self._current_node

    @property
    def tree(self) -> NAryTree:
        return self._tree

    def get_physical_path(self, node: NAryNode) -> str:
        relative = node.get_relative_path()
        if relative == ".":
            return self._base_physical_path
        return os.path.join(self._base_physical_path, relative)

    def create_directory(self, folder_name: str) -> None:
        if self._current_node.find_child(folder_name):
            raise ValueError(f"Ya existe un elemento llamado '{folder_name}' en este nivel.")

        new_node = NAryNode(folder_name, FileNodeType.DIRECTORY, parent=self._current_node)
        self._current_node.add_child(new_node)

        # Creación en disco
        folder_path = self.get_physical_path(new_node)
        os.makedirs(folder_path, exist_ok=True)

    def create_file(self, file_name: str, initial_content: str = "") -> None:
        if self._current_node.find_child(file_name):
            raise ValueError(f"Ya existe un elemento llamado '{file_name}' en este nivel.")

        new_file_node = NAryNode(file_name, FileNodeType.FILE, parent=self._current_node)
        self._current_node.add_child(new_file_node)

        # Creación en disco
        file_path = self.get_physical_path(new_file_node)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(initial_content)

    def change_directory(self, target: str) -> None:
        if target == "..":
            if self._current_node.parent is not None:
                self._current_node = self._current_node.parent
            else:
                print("[Aviso]: Ya te encuentras en el directorio raíz.")
            return

        child = self._current_node.find_child(target)
        if child is None:
            raise ValueError(f"No existe el directorio '{target}'.")
        if not child.is_directory():
            raise ValueError(f"'{target}' es un archivo, no un directorio.")

        self._current_node = child

    def move_node(self, node_name: str, target_folder_name: str) -> None:
        source_node = self._current_node.find_child(node_name)
        if source_node is None:
            raise ValueError(f"'{node_name}' no existe en el directorio actual.")

        target_folder = self._current_node.find_child(target_folder_name)
        if target_folder is None:
            raise ValueError(f"El directorio destino '{target_folder_name}' no existe.")
        if not target_folder.is_directory():
            raise ValueError(f"'{target_folder_name}' no es un directorio.")

        old_path = self.get_physical_path(source_node)

        # Desplazamiento lógico en el árbol
        self._current_node.remove_child(node_name)
        target_folder.add_child(source_node)

        # Desplazamiento físico en disco
        new_path = self.get_physical_path(source_node)
        shutil.move(old_path, new_path)

    def get_all_code_files(self) -> List[NAryNode]:
        """
        Recolecta recursivamente todos los nodos de tipo archivo (usado luego en index-all).
        """
        files: List[NAryNode] = []
        self._collect_files(self._tree.root, files)
        return files

    def _collect_files(self, current: NAryNode, accumulator: List[NAryNode]) -> None:
        if current.is_file():
            accumulator.append(current)
        for child in current.children:
            self._collect_files(child, accumulator)