from abc import ABC, abstractmethod
from .response import GetUsersUseCaseResponse


class GetUsersUseCase(ABC):
    @abstractmethod
    def handle(self) -> GetUsersUseCaseResponse:
        pass
