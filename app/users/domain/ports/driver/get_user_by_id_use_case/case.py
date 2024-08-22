from abc import ABC, abstractmethod

from .request import GetUserBydIdUseCaseRequest
from .response import GetUserBydIdUseCaseResponse


class GetUserByIdUseCase(ABC):

    @abstractmethod
    def handle(self, request: GetUserBydIdUseCaseRequest) -> GetUserBydIdUseCaseResponse:
        pass
