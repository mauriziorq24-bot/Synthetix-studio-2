from abc import ABC, abstractmethod
from typing import List


class BaseCommand(ABC):

    @abstractmethod
    def execute(self, args: List[str]) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass