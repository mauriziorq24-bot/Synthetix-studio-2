from typing import List
from app.structures.b_tree.token_occurrence import TokenOccurrence


class BTreeEntry:
    def __init__(self, key: str) -> None:
        self.key: str = key
        self.occurrences: List[TokenOccurrence] = []

    def add_occurrence(self, file_path: str, line_number: int) -> None:
        self.occurrences.append(TokenOccurrence(file_path, line_number))