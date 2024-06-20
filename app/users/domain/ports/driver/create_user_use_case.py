from abc import ABC, abstractmethod

from app.users.domain import User


class CreateUserUseCase(ABC):

    @abstractmethod
    def handle(self, name: str, lastname: str, email: str, age: int) -> User:
        pass
