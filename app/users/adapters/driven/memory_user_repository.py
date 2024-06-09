import typing

from app.users.domain import User
from app.users.domain.ports import UserRepository


class MemoryUserRepository(UserRepository):

    def __init__(self):
        self.users: typing.Dict[str, User] = {
            "1": User(
                identifier="1",
                name="Jean Carlos",
                lastname="Alarcon",
                age=30,
                email="jean.alarcon@gmail.com"
            )
        }

    def get(self) -> typing.List[User]:
        return [user for user in self.users.values()]

    def get_by_id(self, identifier: str) -> typing.Optional[User]:
        return self.users.get(identifier)
