import typing
from abc import ABC, abstractmethod

from app.users.domain import User


class GetUsersUseCase(ABC):
    @abstractmethod
    def handle(self) -> typing.List[User]:
        pass
