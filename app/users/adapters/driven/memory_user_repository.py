import typing

from app.users.domain import User
from app.users.domain.ports import UserRepository


class MemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: typing.Dict[str, User] = {}

    def get(self) -> typing.List[User]:
        return [user for user in self.users.values()]

    def get_by_id(self, identifier: str) -> typing.Optional[User]:
        return self.users.get(identifier)

    def add_multiple(self, users: typing.List[User]) -> None:
        for user in users:
            self.users[user.identifier] = user
