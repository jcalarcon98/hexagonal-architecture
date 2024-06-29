import typing

from app.users.domain import User
from app.users.domain.ports.driven import UserRepository


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

    def create(self, user: User) -> User:
        self.users[user.identifier] = user
        return user

    def get_by_email(self, email: str) -> typing.Optional[User]:
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def has_user_been_created(self, user: User) -> bool:
        saved_user = self.get_by_id(identifier=user.identifier)
        return saved_user == user
