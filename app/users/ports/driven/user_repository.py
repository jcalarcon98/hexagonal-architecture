import typing
from abc import ABC, abstractmethod

from app.users.entity import User


class UserRepository(ABC):
    @abstractmethod
    def get(self) -> typing.List[User]:
        pass

    @abstractmethod
    def get_by_id(self, identifier: str) -> typing.Optional[User]:
        pass
