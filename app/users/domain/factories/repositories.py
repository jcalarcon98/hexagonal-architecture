import typing

from app.users.adapters.driven import MemoryUserRepository
from app.users.domain.ports.driven import UserRepository

user_repository: typing.Optional[UserRepository] = None


def get_user_repository() -> UserRepository:
    global user_repository
    if not user_repository:
        user_repository = MemoryUserRepository()
    return user_repository
