from enum import Enum, auto


class FileNodeType(Enum):
    DIRECTORY = auto()
    FILE = auto()