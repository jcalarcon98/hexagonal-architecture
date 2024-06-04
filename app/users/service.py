import typing

from app.users.entity import User
from app.users.repository import UserRepository


class UserService:

    def __init__(self):
        self.user_repository = UserRepository()

    def get(self) -> typing.List[User]:
        return self.user_repository.get()

    def get_by_id(self, user_id: str) -> User:
        return self.user_repository.get_by_id(user_id=user_id)
