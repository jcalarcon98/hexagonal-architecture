import typing
from abc import ABC, abstractmethod

from app.users.domain import User


class UserService(ABC):
    @abstractmethod
    def get(self) -> typing.List[User]:
        pass

    @abstractmethod
    def get_by_id(self, user_id: str) -> User:
        pass
