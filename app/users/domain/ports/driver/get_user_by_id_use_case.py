from abc import ABC, abstractmethod

from app.users.domain import User


class GetUserByIdUseCase(ABC):

    @abstractmethod
    def handle(self, user_id: str) -> User:
        pass
