from abc import ABC, abstractmethod


class IdGenerator(ABC):

    @abstractmethod
    def generate(self) -> str:
        pass
