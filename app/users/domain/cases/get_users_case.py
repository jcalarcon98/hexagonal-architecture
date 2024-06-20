import typing

from app.users.domain import User
from app.users.domain.ports.driven import UserRepository
from app.users.domain.ports.driver import GetUsersUseCase


class GetUsersCase(GetUsersUseCase):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def handle(self) -> typing.List[User]:
        return self.user_repository.get()
