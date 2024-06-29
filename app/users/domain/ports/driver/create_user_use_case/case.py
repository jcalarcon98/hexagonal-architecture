from abc import ABC, abstractmethod

from .request import CreateUserUseCaseRequest
from .response import CreateUserUseCaseResponse


class CreateUserUseCase(ABC):
    @abstractmethod
    def handle(self, request: CreateUserUseCaseRequest) -> CreateUserUseCaseResponse:
        pass
