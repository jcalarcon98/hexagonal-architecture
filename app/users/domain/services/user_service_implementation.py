import typing

from app.users.domain import User
from app.users.domain.exceptions import UserNotFound
from app.users.domain.ports import UserRepository, UserService


class UserServiceImplementation(UserService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get(self) -> typing.List[User]:
        return self.user_repository.get()

    def get_by_id(self, user_id: str) -> User:
        user = self.user_repository.get_by_id(identifier=user_id)

        if not user:
            raise UserNotFound(f"The user with the identifier {user_id} does not exist")

        return user
